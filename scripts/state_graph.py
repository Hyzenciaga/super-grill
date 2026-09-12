#!/usr/bin/env python3
"""Create, validate, and recall Super Grill state graph version 1."""
import argparse
import json
import os
from datetime import datetime, timezone
import sys
from collections import defaultdict, deque
from pathlib import Path

KINDS = {"goal", "assumption", "decision", "requirement", "task", "evidence"}


def fail(message):
    raise ValueError(message)


def read_state(path):
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail("state file does not exist: %s" % path)
    except json.JSONDecodeError as exc:
        fail("invalid JSON: %s" % exc)
    if not isinstance(value, dict):
        fail("state must be a JSON object")
    return value


def validate(state, run_id=None, plan_id=None):
    if state.get("schema_version") != 1:
        fail("schema_version must be 1")
    if not isinstance(state.get("run_id"), str) or not state["run_id"]:
        fail("run_id must be a non-empty string")
    if not isinstance(state.get("plan_id"), str) or not state["plan_id"]:
        fail("plan_id must be a non-empty string")
    if run_id is not None and state["run_id"] != run_id:
        fail("run identity mismatch")
    if plan_id is not None and state["plan_id"] != plan_id:
        fail("plan identity mismatch")
    nodes = state.get("nodes")
    if not isinstance(nodes, dict):
        fail("nodes must be an object keyed by node id")
    if "history" in state and not isinstance(state["history"], list):
        fail("state history must be a list")
    for node_id, node in nodes.items():
        if not isinstance(node_id, str) or not node_id:
            fail("node ids must be non-empty strings")
        if not isinstance(node, dict):
            fail("node %s must be an object" % node_id)
        required = ("id", "kind", "summary", "depends_on", "status", "revision")
        if any(key not in node for key in required):
            fail("node %s is missing a required field" % node_id)
        if node["id"] != node_id:
            fail("node key and id differ: %s" % node_id)
        if not isinstance(node["kind"], str) or node["kind"] not in KINDS:
            fail("node %s has unknown kind" % node_id)
        if not isinstance(node["summary"], str):
            fail("node %s summary must be a string" % node_id)
        if not isinstance(node["depends_on"], list) or not all(isinstance(x, str) for x in node["depends_on"]):
            fail("node %s depends_on must be a string list" % node_id)
        if len(set(node["depends_on"])) != len(node["depends_on"]):
            fail("node %s has duplicate dependencies" % node_id)
        if any(x not in nodes for x in node["depends_on"]):
            fail("node %s refers to a missing prerequisite" % node_id)
        if not isinstance(node["status"], str):
            fail("node %s status must be a string" % node_id)
        if not isinstance(node["revision"], int) or isinstance(node["revision"], bool) or node["revision"] < 0:
            fail("node %s revision must be a non-negative integer" % node_id)
        if "history" in node and not isinstance(node["history"], list):
            fail("node %s history must be a list" % node_id)
    visiting, visited = set(), set()
    def visit(node_id):
        if node_id in visiting:
            fail("dependency cycle includes %s" % node_id)
        if node_id not in visited:
            visiting.add(node_id)
            for prerequisite in nodes[node_id]["depends_on"]:
                visit(prerequisite)
            visiting.remove(node_id)
            visited.add(node_id)
    for node_id in nodes:
        visit(node_id)
    return nodes


def write_json(path, value):
    temporary = path.with_name(path.name + ".tmp-%d" % os.getpid())
    try:
        temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def command_init(args):
    path = Path(args.state)
    if not args.run_id or not args.plan_id:
        fail("run_id and plan_id must be non-empty")
    if path.exists() or path.is_symlink():
        fail("refusing to overwrite existing state: %s" % path)
    if not path.parent.exists():
        fail("parent directory does not exist: %s" % path.parent)
    state = {"schema_version": 1, "run_id": args.run_id, "plan_id": args.plan_id, "nodes": {}}
    # O_EXCL closes the check/create race; replace is only used for later updates.
    payload = json.dumps(state, indent=2, sort_keys=True) + "\n"
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        fail("refusing to overwrite existing state: %s" % path)
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        handle.write(payload)
    return {"action": "init", "state": str(path), "run_id": args.run_id, "plan_id": args.plan_id}


def command_validate(args):
    state = read_state(Path(args.state))
    nodes = validate(state, args.run_id, args.plan_id)
    return {"action": "validate", "valid": True, "node_count": len(nodes), "run_id": state["run_id"], "plan_id": state["plan_id"]}


def command_recall(args):
    path = Path(args.state)
    if path.is_symlink():
        fail("refusing to write through symlink state file")
    state = read_state(path)
    nodes = validate(state, args.run_id, args.plan_id)
    changed = list(dict.fromkeys(args.changed))
    absent = [node_id for node_id in changed if node_id not in nodes]
    if absent:
        fail("unknown changed node(s): %s" % ", ".join(absent))
    reverse = defaultdict(list)
    for node_id, node in nodes.items():
        for prerequisite in node["depends_on"]:
            reverse[prerequisite].append(node_id)
    stale, queue = set(), deque(changed)
    while queue:
        prerequisite = queue.popleft()
        for dependent in reverse[prerequisite]:
            if dependent not in stale and dependent not in changed:
                stale.add(dependent)
                queue.append(dependent)
    event = {
        "action": "recall",
        "changed": changed,
        "invalidated": sorted(stale),
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }
    if args.reason:
        event["reason"] = args.reason
    if "history" in state and not isinstance(state["history"], list):
        fail("state history must be a list")
    state.setdefault("history", []).append(event)
    for node_id in changed:
        if "history" in nodes[node_id] and not isinstance(nodes[node_id]["history"], list):
            fail("node %s history must be a list" % node_id)
        node = nodes[node_id]
        node.setdefault("history", []).append({
            **event,
            "node": node_id,
            "previous_status": node["status"],
            "previous_revision": node["revision"],
        })
        node["revision"] += 1
    for node_id in stale:
        node = nodes[node_id]
        if "history" in node and not isinstance(node["history"], list):
            fail("node %s history must be a list" % node_id)
        node.setdefault("history", []).append({
            **event,
            "node": node_id,
            "previous_status": node["status"],
            "previous_revision": node["revision"],
        })
        node["status"] = "stale"
    write_json(path, state)
    return event


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("init", "validate", "recall"):
        item = sub.add_parser(name)
        item.add_argument("state")
        item.add_argument("--run-id", required=True)
        item.add_argument("--plan-id", required=True)
    sub.choices["recall"].add_argument("--changed", action="append", required=True)
    sub.choices["recall"].add_argument("--reason")
    args = parser.parse_args()
    try:
        result = {"init": command_init, "validate": command_validate, "recall": command_recall}[args.command](args)
    except (ValueError, OSError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps({"ok": True, **result}, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
