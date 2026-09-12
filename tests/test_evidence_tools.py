import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "scripts" / "state_graph.py"
REVIEW = ROOT / "scripts" / "review_evidence.py"


def run(*args, cwd=None, ok=True):
    result = subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if ok and result.returncode:
        raise AssertionError("failed %r\nstdout=%s\nstderr=%s" % (args, result.stdout, result.stderr))
    return result


class StateGraphTests(unittest.TestCase):
    def test_init_identity_recall_and_transitive_invalidation(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "state.json"
            run(sys.executable, str(STATE), "init", str(state), "--run-id", "run-a", "--plan-id", "plan-a")
            doc = json.loads(state.read_text())
            doc["nodes"] = {
                "goal": {"id": "goal", "kind": "goal", "summary": "g", "depends_on": [], "status": "active", "revision": 0},
                "task": {"id": "task", "kind": "task", "summary": "t", "depends_on": ["goal"], "status": "active", "revision": 0},
                "evidence": {"id": "evidence", "kind": "evidence", "summary": "e", "depends_on": ["task"], "status": "accepted", "revision": 4, "history": [{"old": True}]},
                "other": {"id": "other", "kind": "task", "summary": "o", "depends_on": [], "status": "active", "revision": 0},
            }
            state.write_text(json.dumps(doc))
            run(sys.executable, str(STATE), "validate", str(state), "--run-id", "run-a", "--plan-id", "plan-a")
            bad = run(sys.executable, str(STATE), "validate", str(state), "--run-id", "run-b", "--plan-id", "plan-a", ok=False)
            self.assertEqual(2, bad.returncode)
            run(sys.executable, str(STATE), "recall", str(state), "--run-id", "run-a", "--plan-id", "plan-a", "--changed", "goal", "--reason", "changed premise")
            recalled = json.loads(state.read_text())
            self.assertEqual(1, recalled["nodes"]["goal"]["revision"])
            self.assertEqual("active", recalled["nodes"]["goal"]["status"])
            self.assertEqual("recall", recalled["nodes"]["goal"]["history"][0]["action"])
            self.assertEqual(0, recalled["nodes"]["goal"]["history"][0]["previous_revision"])
            self.assertEqual("active", recalled["nodes"]["goal"]["history"][0]["previous_status"])
            self.assertTrue(recalled["nodes"]["goal"]["history"][0]["timestamp"].endswith("Z"))
            self.assertEqual("stale", recalled["nodes"]["task"]["status"])
            self.assertEqual("stale", recalled["nodes"]["evidence"]["status"])
            self.assertEqual(4, recalled["nodes"]["evidence"]["revision"])
            self.assertEqual({"old": True}, recalled["nodes"]["evidence"]["history"][0])
            self.assertEqual("accepted", recalled["nodes"]["evidence"]["history"][1]["previous_status"])
            self.assertEqual("active", recalled["nodes"]["other"]["status"])

    def test_cycle_and_existing_init_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "state.json"
            run(sys.executable, str(STATE), "init", str(state), "--run-id", "r", "--plan-id", "p")
            self.assertEqual(2, run(sys.executable, str(STATE), "init", str(state), "--run-id", "r", "--plan-id", "p", ok=False).returncode)
            doc = json.loads(state.read_text())
            doc["nodes"] = {n: {"id": n, "kind": "task", "summary": n, "depends_on": [other], "status": "active", "revision": 0}
                            for n, other in (("a", "b"), ("b", "a"))}
            state.write_text(json.dumps(doc))
            self.assertEqual(2, run(sys.executable, str(STATE), "validate", str(state), "--run-id", "r", "--plan-id", "p", ok=False).returncode)

    def test_malformed_history_and_failed_recall_leave_state_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "state.json"
            run(sys.executable, str(STATE), "init", str(state), "--run-id", "r", "--plan-id", "p")
            doc = json.loads(state.read_text())
            doc["nodes"] = {"a": {"id": "a", "kind": "task", "summary": "a", "depends_on": [], "status": "active", "revision": 0, "history": "bad"}}
            state.write_text(json.dumps(doc)); before = state.read_bytes()
            self.assertEqual(2, run(sys.executable, str(STATE), "recall", str(state), "--run-id", "r", "--plan-id", "p", "--changed", "a", ok=False).returncode)
            self.assertEqual(before, state.read_bytes())
            self.assertEqual(2, run(sys.executable, str(STATE), "validate", str(state), "--run-id", "r", "--plan-id", "p", ok=False).returncode)

    def test_missing_dependency_and_identity_failed_recall_do_not_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "state.json"
            run(sys.executable, str(STATE), "init", str(state), "--run-id", "r", "--plan-id", "p")
            doc = json.loads(state.read_text())
            doc["nodes"] = {"a": {"id": "a", "kind": "task", "summary": "a", "depends_on": ["missing"], "status": "active", "revision": 0}}
            state.write_text(json.dumps(doc))
            self.assertEqual(2, run(sys.executable, str(STATE), "validate", str(state), "--run-id", "r", "--plan-id", "p", ok=False).returncode)
            doc["nodes"]["a"]["depends_on"] = []; state.write_text(json.dumps(doc)); before = state.read_bytes()
            self.assertEqual(2, run(sys.executable, str(STATE), "recall", str(state), "--run-id", "wrong", "--plan-id", "p", "--changed", "a", ok=False).returncode)
            self.assertEqual(before, state.read_bytes())
            doc["nodes"]["a"]["kind"] = []
            state.write_text(json.dumps(doc))
            invalid_kind = run(sys.executable, str(STATE), "validate", str(state), "--run-id", "r", "--plan-id", "p", ok=False)
            self.assertEqual(2, invalid_kind.returncode)
            self.assertIn('"error"', invalid_kind.stderr)


class ReviewEvidenceTests(unittest.TestCase):
    def make_repo(self, directory):
        repo = Path(directory) / "repo"
        repo.mkdir()
        run("git", "init", "-q", str(repo))
        run("git", "-C", str(repo), "config", "user.email", "tests@example.invalid")
        run("git", "-C", str(repo), "config", "user.name", "Tests")
        (repo / "tracked.txt").write_text("base\n")
        (repo / "committed.txt").write_text("base commit\n")
        run("git", "-C", str(repo), "add", "tracked.txt", "committed.txt")
        run("git", "-C", str(repo), "commit", "-qm", "base")
        return repo

    def test_captures_dirty_staged_untracked_and_detects_package_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); repo = self.make_repo(tmp)
            (repo / "tracked.txt").write_text("preexisting\n")
            (repo / "new.txt").write_text("new preexisting\n")
            baseline = tmp / "baseline"
            run(sys.executable, str(REVIEW), "capture", "--repo", str(repo), "--output", str(baseline), "--path", "tracked.txt", "--path", "new.txt", "--path", "committed.txt")
            (repo / "committed.txt").write_text("committed task change\n")
            run("git", "-C", str(repo), "add", "committed.txt")
            run("git", "-C", str(repo), "commit", "-qm", "task commit")
            (repo / "tracked.txt").write_text("staged task\n")
            run("git", "-C", str(repo), "add", "tracked.txt")
            (repo / "tracked.txt").write_text("staged plus unstaged\n")
            (repo / "new.txt").write_text("new task change\n")
            package = tmp / "package"
            run(sys.executable, str(REVIEW), "package", "--repo", str(repo), "--baseline", str(baseline), "--output", str(package), "--path", "tracked.txt", "--path", "new.txt", "--path", "committed.txt")
            report = json.loads((package / "review.json").read_text())
            self.assertEqual({"tracked.txt", "new.txt"}, set(report["preexisting_dirty_paths"]))
            self.assertIn("new.txt", report["untracked_paths"])
            self.assertIn("overlap pre-existing", report["attribution"])
            self.assertTrue((package / "staged.patch").read_text())
            self.assertTrue((package / "unstaged.patch").read_text())
            self.assertTrue((package / "committed.patch").read_text())
            self.assertEqual(0, run(sys.executable, str(REVIEW), "verify", "--repo", str(repo), "--package", str(package), "--path", "tracked.txt", "--path", "new.txt", "--path", "committed.txt").returncode)
            (repo / "new.txt").write_text("drift\n")
            verify = run(sys.executable, str(REVIEW), "verify", "--repo", str(repo), "--package", str(package), "--path", "tracked.txt", "--path", "new.txt", "--path", "committed.txt", ok=False)
            self.assertEqual(1, verify.returncode)
            self.assertFalse(json.loads(verify.stdout)["valid"])

    def test_no_commit_new_file_and_output_inside_repo_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); repo = self.make_repo(tmp)
            (repo / "only-new.txt").write_bytes(b"new\x00content")
            output = tmp / "baseline"
            run(sys.executable, str(REVIEW), "capture", "--repo", str(repo), "--output", str(output), "--path", "only-new.txt")
            data = json.loads((output / "baseline.json").read_text())
            self.assertFalse(data["paths"][0]["tracked"])
            self.assertEqual(11, data["paths"][0]["bytes"])
            rejected = run(sys.executable, str(REVIEW), "capture", "--repo", str(repo), "--output", str(repo / "review-output"), "--path", "only-new.txt", ok=False)
            self.assertEqual(2, rejected.returncode)

    def test_directory_scope_tracks_new_and_deleted_files_and_rejects_escapes(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); repo = self.make_repo(tmp); (repo / "src").mkdir()
            (repo / "src" / "old.txt").write_text("old\n")
            run("git", "-C", str(repo), "add", "src/old.txt"); run("git", "-C", str(repo), "commit", "-qm", "src")
            baseline = tmp / "baseline"; run(sys.executable, str(REVIEW), "capture", "--repo", str(repo), "--output", str(baseline), "--path", "src")
            (repo / "src" / "old.txt").unlink(); (repo / "src" / "new.txt").write_text("new\n")
            package = tmp / "package"; run(sys.executable, str(REVIEW), "package", "--repo", str(repo), "--baseline", str(baseline), "--output", str(package), "--path", "src")
            report = json.loads((package / "review.json").read_text())
            self.assertEqual({"src/old.txt", "src/new.txt"}, {x["path"] for x in report["paths"]})
            self.assertTrue((package / "task.patch").read_bytes())
            self.assertEqual(2, run(sys.executable, str(REVIEW), "capture", "--repo", str(repo), "--output", str(tmp / "bad"), "--path", "../outside", ok=False).returncode)
            (repo / "link").symlink_to(tmp)
            self.assertEqual(2, run(sys.executable, str(REVIEW), "capture", "--repo", str(repo), "--output", str(tmp / "bad-link"), "--path", "link/nope", ok=False).returncode)

    def test_unborn_baseline_and_tampered_snapshot_are_explicit(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); repo = tmp / "unborn"; repo.mkdir(); run("git", "init", "-q", str(repo))
            (repo / "a.txt").write_text("a\n"); baseline = tmp / "baseline"
            run(sys.executable, str(REVIEW), "capture", "--repo", str(repo), "--output", str(baseline), "--path", "a.txt")
            self.assertIsNone(json.loads((baseline / "baseline.json").read_text())["head"])
            package = tmp / "package"; run(sys.executable, str(REVIEW), "package", "--repo", str(repo), "--baseline", str(baseline), "--output", str(package), "--path", "a.txt")
            self.assertIn("no commits", (package / "committed.patch").read_text())
            package_digest = json.loads((package / "review.json").read_text())["paths"][0]["worktree_sha256"]
            (package / "blobs" / package_digest).write_text("tampered")
            self.assertEqual(2, run(sys.executable, str(REVIEW), "verify", "--repo", str(repo), "--package", str(package), "--path", "a.txt", ok=False).returncode)
            digest = json.loads((baseline / "baseline.json").read_text())["paths"][0]["worktree_sha256"]
            (baseline / "blobs" / digest).write_text("tampered")
            self.assertEqual(2, run(sys.executable, str(REVIEW), "package", "--repo", str(repo), "--baseline", str(baseline), "--output", str(tmp / "tampered-package"), "--path", "a.txt", ok=False).returncode)

    def test_missing_directory_scope_becomes_new_file_or_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); repo = self.make_repo(tmp)
            baseline = tmp / "missing-baseline"
            run(sys.executable, str(REVIEW), "capture", "--repo", str(repo), "--output", str(baseline), "--path", "src")
            (repo / "src").mkdir(); (repo / "src" / "new.py").write_text("print('new')\n")
            package = tmp / "new-package"
            run(sys.executable, str(REVIEW), "package", "--repo", str(repo), "--baseline", str(baseline), "--output", str(package), "--path", "src")
            self.assertIn("print('new')", (package / "task.patch").read_text())
            report = json.loads((package / "review.json").read_text())
            self.assertEqual([{"path": "src", "state": "missing"}], report["baseline_root_states"])
            self.assertEqual([{"path": "src", "state": "directory"}], report["current_root_states"])
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); repo = self.make_repo(tmp); baseline = tmp / "empty-baseline"
            run(sys.executable, str(REVIEW), "capture", "--repo", str(repo), "--output", str(baseline), "--path", "empty")
            (repo / "empty").mkdir(); package = tmp / "empty-package"
            run(sys.executable, str(REVIEW), "package", "--repo", str(repo), "--baseline", str(baseline), "--output", str(package), "--path", "empty")
            report = json.loads((package / "review.json").read_text()
            )
            self.assertEqual([{"path": "empty", "state": "directory"}], report["current_root_states"])

    def test_deleted_selected_directory_keeps_deleted_descendants_without_root_marker(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); repo = self.make_repo(tmp)
            (repo / "src").mkdir()
            (repo / "src" / "a.txt").write_text("a\n")
            (repo / "src" / "b.txt").write_text("b\n")
            run("git", "-C", str(repo), "add", "src")
            run("git", "-C", str(repo), "commit", "-qm", "src files")
            baseline = tmp / "baseline"
            run(sys.executable, str(REVIEW), "capture", "--repo", str(repo), "--output", str(baseline), "--path", "src")
            (repo / "src" / "a.txt").unlink(); (repo / "src" / "b.txt").unlink(); (repo / "src").rmdir()
            package = tmp / "package"
            run(sys.executable, str(REVIEW), "package", "--repo", str(repo), "--baseline", str(baseline), "--output", str(package), "--path", "src")
            report = json.loads((package / "review.json").read_text())
            self.assertEqual({"src/a.txt", "src/b.txt"}, {item["path"] for item in report["paths"]})
            self.assertTrue((package / "task.patch").read_bytes())

    def test_verify_rejects_fabricated_readable_tree_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); repo = self.make_repo(tmp)
            baseline = tmp / "baseline"
            run(sys.executable, str(REVIEW), "capture", "--repo", str(repo), "--output", str(baseline), "--path", "tracked.txt")
            (repo / "tracked.txt").write_text("changed\n")
            package = tmp / "package"
            run(sys.executable, str(REVIEW), "package", "--repo", str(repo), "--baseline", str(baseline), "--output", str(package), "--path", "tracked.txt")
            (package / "after-tree" / "not-reviewed.txt").write_text("fabricated\n")
            self.assertEqual(2, run(sys.executable, str(REVIEW), "verify", "--repo", str(repo), "--package", str(package), "--path", "tracked.txt", ok=False).returncode)


if __name__ == "__main__":
    unittest.main()
