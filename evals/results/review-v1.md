# Independent upgrade review and corrections

Reviewer: GPT-5.6 Terra, task `independent_review`, fresh context initially,
read-only inspection and disposable probes. Coordinator did not provide an
expected verdict. Reviewer compared current tracked and untracked upgrade files.

## Initial whole-upgrade review

One material acceptance gap: docs/validation-v1.md had not yet been created, while
README linked it and R10 required it. The real validation record was then added.
No pre-existing promotional PNG was included in upgrade scope.

## Focused helper review

The reviewer independently reproduced two material defects despite the then-green
9-test suite:

1. Selecting src, then deleting all tracked files and the directory, caused the
   package command to treat a synthetic directory marker as a Git index file.
2. Adding an unrecorded file under after-tree did not invalidate package verification.

The author fixed both, adding regression cases for deleted directory scopes and
unexpected readable tree members. Root also found/fixed missing-to-new directory
transitions and required task.patch to contain actual new-file content.

## Final reviewer response (verbatim)

Both prior defects are fixed.

- Full deletion repro now packages `src/a` and `src/b` as missing records, produces the deletion patch, and `verify` returns valid against the unchanged deleted state.
- Injecting `after-tree/not-reviewed.txt` now makes `verify` fail with exit 2 and `package tree has an unexpected file`.
- An injected empty directory is also rejected.

The revised marker filter preserves tracked deleted descendants while excluding only synthetic directory markers, and the tree verifier rejects extra files, directories, symlinks, and non-regular items. The complete helper suite passes: 11 tests; `git diff --check` is clean.

Spec verdict: **pass** for the helper scope reviewed.

Quality verdict: **pass**. I found no remaining material correctness, preservation, or evidence-integrity issue in the revised helper transitions.

## Final whole-upgrade acceptance response (verbatim)

No material actionable gaps found.

Spec verdict: **PASS for R1–R10.** The final package supplies each required protocol, helper, examples, reusable evaluation scenarios, synchronized 1.0.0 manifest/UI metadata, and a real validation record. The record appropriately limits claims: live-timeout recovery remains untested, sequential comparison quality was imperfect with reruns not retained, and independent alternatives establish provenance/design traces rather than executable correctness.

Quality verdict: **PASS.** Current source hashes match the recorded validation fingerprints; all local Markdown links resolve; JSON artifacts parse; the documented 11-test helper result, validators, and `git diff --check` outputs are retained. The final docs do not overstate the bounded behavioral evidence or claim independence where only sequential work occurred.
