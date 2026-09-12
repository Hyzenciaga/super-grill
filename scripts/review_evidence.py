#!/usr/bin/env python3
"""Capture path-scoped Git review evidence without changing Git state."""
import argparse
import hashlib
import json
import shutil
import stat
import subprocess
import sys
from pathlib import Path

def fail(message):
    raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def git(repo, *args, allowed=(0,)):
    result = subprocess.run(
        ["git", "-C", str(repo), "--literal-pathspecs", *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode not in allowed:
        fail("git %s: %s" % (" ".join(args), result.stderr.decode(errors="replace").strip()))
    return result


def repository(path):
    return Path(git(path, "rev-parse", "--show-toplevel").stdout.decode().strip()).resolve()


def unborn(root):
    return git(root, "rev-parse", "--verify", "HEAD", allowed=(0, 128)).returncode == 128

def root_path(root, raw):
    item = Path(raw)
    if item.is_absolute() or ".." in item.parts or ".git" in item.parts or not item.parts or str(item) == ".":
        fail("path must be a relative repository path without .. or .git: %s" % raw)
    candidate = root.joinpath(item)
    parent = root
    for part in item.parts:
        parent = parent / part
        try:
            info = parent.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode):
            fail("symlink paths and symlink ancestors are not allowed: %s" % raw)
    return candidate, item.as_posix()

def selection_roots(root, raw_paths, output=None):
    if not raw_paths: fail("at least one explicit --path is required")
    if output:
        try: output.resolve().relative_to(root)
        except ValueError: pass
        else: fail("output must be outside repository to avoid capturing it")
    return sorted({root_path(root, raw)[1] for raw in raw_paths})

def expand(root, roots):
    paths = set()
    tracked = git(root, "ls-files", "--cached", "--deleted", "-z").stdout.decode(errors="surrogateescape").split("\0")
    for rel in filter(None, tracked):
        if any(rel == item or rel.startswith(item + "/") for item in roots): paths.add(rel)
    for item in roots:
        full, rel = root_path(root, item)
        if full.exists() and full.is_dir():
            for child in full.rglob("*"):
                relative = child.relative_to(root).as_posix()
                root_path(root, relative)
                if child.is_file():
                    paths.add(relative)
        elif full.exists() and full.is_file(): paths.add(rel)
        elif not full.exists(): paths.add(rel)
        else: fail("path must be a regular file, directory, or missing: %s" % item)
    return sorted(paths)

def root_states(root, roots):
    states = []
    for rel in roots:
        full, _ = root_path(root, rel)
        if full.is_dir():
            state = "directory"
        elif full.is_file():
            state = "file"
        else:
            state = "missing"
        states.append({"path": rel, "state": state})
    return states


def without_directory_markers(paths, roots, baseline_states, current_states):
    """Remove only synthetic missing-directory scope markers from file paths."""
    baseline = {item["path"]: item["state"] for item in baseline_states}
    current = {item["path"]: item["state"] for item in current_states}
    result = set(paths)
    for root in roots:
        # A current file is a real selected file. A directory at either end of
        # the comparison is merely a root that expands to its descendants.
        if current.get(root) != "file" and (
            baseline.get(root) == "directory" or current.get(root) == "directory"
        ):
            result.discard(root)
    return result

def index_entries(root, rel):
    entries = []
    for row in git(root, "ls-files", "-s", "--", rel).stdout.decode(errors="surrogateescape").splitlines():
        meta, _ = row.split("\t", 1)
        mode, blob, stage = meta.split()
        entries.append({"mode": mode, "blob": blob, "stage": int(stage)})
    return entries
def object_bytes(root, spec): return git(root, "show", spec).stdout

def record(root, rel):
    full, _ = root_path(root, rel)
    if full.exists() and not full.is_file():
        fail("selected item is no longer a regular file: %s" % rel)
    data = full.read_bytes() if full.is_file() else None
    entries = index_entries(root, rel)
    for entry in entries: entry["sha256"] = sha(object_bytes(root, ":%s:%s" % (entry["stage"], rel)))
    head = git(root, "rev-parse", "--verify", "HEAD", allowed=(0, 128))
    head_blob = git(root, "rev-parse", "HEAD:%s" % rel, allowed=(0, 128))
    tree = git(root, "ls-tree", "HEAD", "--", rel, allowed=(0, 128)).stdout.decode().split()
    return {"path": rel, "exists": data is not None, "tracked": bool(entries), "worktree_sha256": sha(data) if data is not None else None,
            "bytes": len(data) if data is not None else None, "worktree_mode": format(stat.S_IMODE(full.stat().st_mode), "04o") if data is not None else None,
            "index_entries": entries, "conflicted_index": len(entries) > 1, "head_blob": head_blob.stdout.decode().strip() if head_blob.returncode == 0 else None,
            "head_mode": tree[0] if tree else None, "head": head.stdout.decode().strip() if head.returncode == 0 else None,
            "staged_dirty": git(root, "diff", "--cached", "--quiet", "--", rel, allowed=(0, 1)).returncode == 1,
            "unstaged_dirty": git(root, "diff", "--quiet", "--", rel, allowed=(0, 1)).returncode == 1, "data": data}

def save_blobs(directory, item, root):
    data = item.pop("data")
    def put(digest, content):
        target = directory / "blobs" / digest; target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists(): target.write_bytes(content)
    if data is not None: put(item["worktree_sha256"], data)
    for entry in item["index_entries"]: put(entry["sha256"], object_bytes(root, ":%s:%s" % (entry["stage"], item["path"])))

def capture(args):
    root, out = repository(Path(args.repo)), Path(args.output).absolute()
    if out.exists(): fail("refusing to overwrite existing output: %s" % out)
    roots = selection_roots(root, args.path, out); out.mkdir(parents=True); records = []
    for rel in expand(root, roots):
        item = record(root, rel); save_blobs(out, item, root); records.append(item)
    manifest = {"format": 2, "repo": str(root), "selection_roots": roots,
                "root_states": root_states(root, roots),
                "head": None if unborn(root) else git(root, "rev-parse", "HEAD").stdout.decode().strip(), "paths": records}
    write_json(out / "baseline.json", manifest)
    return {"action": "capture", "output": str(out), "path_count": len(records), "unborn": manifest["head"] is None}

def materialize(tree, records, blobdir):
    tree.mkdir(parents=True, exist_ok=True)
    for item in records:
        if item["worktree_sha256"] is not None:
            target = tree / item["path"]; target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(blobdir / "blobs" / item["worktree_sha256"], target); target.chmod(int(item["worktree_mode"], 8))
def copy_blobs(source, dest, records):
    for item in records:
        for digest in [item.get("worktree_sha256")] + [x["sha256"] for x in item["index_entries"]]:
            if digest:
                blob = source / "blobs" / digest
                if not blob.is_file() or sha(blob.read_bytes()) != digest: fail("snapshot blob missing or tampered: %s" % digest)
                target = dest / "blobs" / digest; target.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(blob, target)
def patch(root, output, args, roots): output.write_bytes(git(root, *args, "--", *roots).stdout)


def verify_tree(tree, records):
    """Ensure the readable package tree matches its recorded byte snapshots."""
    expected_files = {
        item["path"] for item in records if item["worktree_sha256"] is not None
    }
    expected_directories = set()
    for path in expected_files:
        parent = Path(path).parent
        while str(parent) != ".":
            expected_directories.add(parent.as_posix())
            parent = parent.parent
    if not tree.is_dir() or tree.is_symlink():
        fail("package tree is missing or is not a directory: %s" % tree)
    for child in tree.rglob("*"):
        relative = child.relative_to(tree).as_posix()
        info = child.lstat()
        if stat.S_ISLNK(info.st_mode):
            fail("package tree has an unexpected symlink: %s" % relative)
        if stat.S_ISREG(info.st_mode):
            if relative not in expected_files:
                fail("package tree has an unexpected file: %s" % relative)
        elif stat.S_ISDIR(info.st_mode):
            if relative not in expected_directories:
                fail("package tree has an unexpected directory: %s" % relative)
        else:
            fail("package tree has an unexpected non-regular item: %s" % relative)
    for item in records:
        path = tree / item["path"]
        expected = item["worktree_sha256"]
        if expected is None:
            if path.exists():
                fail("package tree has an unexpected file: %s" % item["path"])
            continue
        if not path.is_file() or sha(path.read_bytes()) != expected:
            fail("package tree content is missing or tampered: %s" % item["path"])
        mode = format(stat.S_IMODE(path.stat().st_mode), "04o")
        if mode != item["worktree_mode"]:
            fail("package tree mode is missing or tampered: %s" % item["path"])

def package(args):
    base, out = Path(args.baseline).absolute(), Path(args.output).absolute()
    if out.exists(): fail("refusing to overwrite existing output: %s" % out)
    try: baseline = json.loads((base / "baseline.json").read_text())
    except FileNotFoundError: fail("baseline.json is missing")
    root = repository(Path(args.repo))
    if str(root) != baseline.get("repo"): fail("baseline belongs to a different repository")
    roots = selection_roots(root, args.path, out)
    if roots != baseline.get("selection_roots"): fail("package roots must exactly match baseline roots")
    old = {x["path"]: x for x in baseline["paths"]}
    # A missing directory root is a scope marker, not a missing file. Once the
    # directory appears, replace that marker with its newly discovered files.
    current_root_states = root_states(root, roots)
    paths = without_directory_markers(
        set(old) | set(expand(root, roots)), roots,
        baseline.get("root_states", []), current_root_states,
    )
    current = []
    for rel in sorted(paths):
        item = record(root, rel); current.append(item)
    out.mkdir(parents=True); copy_blobs(base, out / "before", list(old.values()))
    for item in current: save_blobs(out, item, root)
    materialize(out / "before-tree", list(old.values()), out / "before"); materialize(out / "after-tree", current, out)
    d = subprocess.run(["git", "diff", "--no-index", "--binary", str(out / "before-tree"), str(out / "after-tree")], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if d.returncode not in (0, 1): fail("git diff --no-index: " + d.stderr.decode(errors="replace"))
    (out / "task.patch").write_bytes(d.stdout)
    pre = [x["path"] for x in old.values() if x["staged_dirty"] or x["unstaged_dirty"] or (not x["tracked"] and x["exists"])]
    keys = ("exists", "tracked", "worktree_sha256", "worktree_mode", "index_entries", "conflicted_index", "head_blob", "head_mode")
    drift = [{"path": x["path"], "changed_identifiers": {k: (old.get(x["path"], {}).get(k), x.get(k)) for k in keys if old.get(x["path"], {}).get(k) != x.get(k)}} for x in current if any(old.get(x["path"], {}).get(k) != x.get(k) for k in keys)]
    if baseline["head"] is None: (out / "committed.patch").write_text("# Baseline had no commits. See task.patch and before-tree/after-tree.\n")
    else: patch(root, out / "committed.patch", ["diff", "--binary", baseline["head"] + "..HEAD"], roots)
    patch(root, out / "staged.patch", ["diff", "--binary", "--cached"], roots); patch(root, out / "unstaged.patch", ["diff", "--binary"], roots)
    report = {"format": 2, "repo": str(root), "selection_roots": roots,
              "baseline_root_states": baseline.get("root_states", []), "current_root_states": current_root_states,
              "baseline_head": baseline["head"], "current_head": None if unborn(root) else git(root, "rev-parse", "HEAD").stdout.decode().strip(), "paths": current, "baseline_paths": list(old.values()), "drift": drift, "preexisting_dirty_paths": pre, "untracked_paths": [x["path"] for x in current if not x["tracked"] and x["exists"]], "baseline_manifest_sha256": sha((base / "baseline.json").read_bytes()), "task_patch_sha256": sha((out / "task.patch").read_bytes()), "attribution": ("Task paths overlap pre-existing dirty work: " + ", ".join(pre) + ". Review task.patch and before-tree/after-tree snapshots; this package does not attribute all path changes to the task.") if pre else "No selected path was dirty at baseline."}
    write_json(out / "review.json", report); return {"action": "package", "output": str(out), "drift_count": len(drift), "preexisting_dirty_count": len(pre)}

def verify(args):
    directory = Path(args.package).absolute()
    report = json.loads((directory / "review.json").read_text())
    root = repository(Path(args.repo))
    roots = selection_roots(root, args.path, directory)
    if str(root) != report.get("repo") or roots != report.get("selection_roots"):
        fail("package identity or roots mismatch")
    patch_file = directory / "task.patch"
    if not patch_file.is_file() or sha(patch_file.read_bytes()) != report.get("task_patch_sha256"):
        fail("task.patch is missing or tampered")
    verify_tree(directory / "before-tree", report.get("baseline_paths", []))
    verify_tree(directory / "after-tree", report["paths"])
    old = {x["path"]: x for x in report["paths"]}; current = []
    for prior in old.values():
        for digest in [prior.get("worktree_sha256")] + [x["sha256"] for x in prior["index_entries"]]:
            if digest:
                blob = directory / "blobs" / digest
                if not blob.is_file() or sha(blob.read_bytes()) != digest: fail("package snapshot blob missing or tampered: %s" % digest)
    paths = without_directory_markers(
        set(old) | set(expand(root, roots)), roots,
        report.get("baseline_root_states", []), root_states(root, roots),
    )
    for rel in sorted(paths):
        item = record(root, rel); item.pop("data"); current.append(item)
    keys = ("exists", "tracked", "worktree_sha256", "bytes", "worktree_mode", "index_entries", "conflicted_index", "head_blob", "head_mode")
    drift = [{"path": x["path"], "changed_identifiers": {k: (old.get(x["path"], {}).get(k), x.get(k)) for k in keys if old.get(x["path"], {}).get(k) != x.get(k)}} for x in current if any(old.get(x["path"], {}).get(k) != x.get(k) for k in keys)]
    result = {"action": "verify", "valid": not drift, "drift": drift, "scope": "exact worktree bytes/mode, missing/untracked state, index records, and HEAD records under selected roots"}; print(json.dumps({"ok": True, **result}, sort_keys=True)); return 0 if result["valid"] else 1

def main():
    p = argparse.ArgumentParser(description=__doc__); sub = p.add_subparsers(dest="command", required=True)
    for name in ("capture", "package", "verify"):
        q = sub.add_parser(name); q.add_argument("--repo", required=True); q.add_argument("--path", action="append", required=True)
    sub.choices["capture"].add_argument("--output", required=True); sub.choices["package"].add_argument("--output", required=True); sub.choices["package"].add_argument("--baseline", required=True); sub.choices["verify"].add_argument("--package", required=True); a = p.parse_args()
    try:
        if a.command == "verify": return verify(a)
        result = capture(a) if a.command == "capture" else package(a); print(json.dumps({"ok": True, **result}, sort_keys=True)); return 0
    except (ValueError, OSError, json.JSONDecodeError) as exc: print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr); return 2
if __name__ == "__main__": sys.exit(main())
