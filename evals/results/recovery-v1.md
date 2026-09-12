# Raw response — stale-ledger recovery

Actor: GPT-5.6 Terra, fresh context, task `probe_recovery`.
Setup: run-17/plan-4 ledger says T-03 dispatched (multiply subtotal), T-04 pending
(zero boundaries), base 354b14110b9bf39457406e14d3d32bb14b696cb7, no retained worker
handle. The actual fixture is the completed solo-build working tree.
Input: 恢复这个 Super Grill run-17 / plan-4，先核对实际文件、Git 和测试，再完成下一步安全工作。我们没有可查询的旧 worker handle。不得提交、推送或改 notes.txt；先不要重新派发 T-03。

## Actor response (verbatim)

Firing up Super Grill: **build / well-done / single-skewer**. The recovery committee found the steak already cooked.

`run-17 / plan-4` reconciles to the supplied fixture: its `HEAD` is exactly `354b14110b9bf39457406e14d3d32bb14b696cb7`. That object is absent from the skill repository, so the fixture—not the skill repo—was correctly treated as the run workspace.

- **T-03:** verified complete in the current working tree. [`cart.py`](/var/folders/sx/xjl2wfwd6tvgprplsck9p1f80000gn/T/super-grill-v1-build-uaa3_jxa/cart.py) now returns `price_minor * quantity`; the base revision used addition.
- **T-04:** verified complete. [`test_cart.py`](/var/folders/sx/xjl2wfwd6tvgprplsck9p1f80000gn/T/super-grill-v1-build-uaa3_jxa/test_cart.py) includes zero-price and zero-quantity tests.
- Verification: `python3 -m unittest -v test_cart.py` and `python3 -m unittest discover -v` both passed all 3 tests. `git diff --check -- cart.py test_cart.py` was clean.
- Git remains on `main` with only unstaged changes to `cart.py`, `test_cart.py`, and the pre-existing `notes.txt` modification. I did not read or alter `notes.txt`, commit, push, or redispatch T-03. The test-created `__pycache__/` was removed.

Review verdicts: recipe **pass**; texture **pass**; `review_mode: self-reviewed`, `independence: unavailable`. No worker-handle claim was made or needed: the prior dispatched status is superseded by current file and test evidence. **Mise en Place Recovered**; second pass complete, moisture removed.

## Interpretation

This exercises recovery when no worker handle was retained, not a live-agent
polling timeout. The actor used current uncommitted files and tests instead of
reimplementing from the stale task label. Initial and resulting fixture bytes
are retained in [solo-build artifacts](solo-build-artifacts/); no additional
product changes were needed. Actual live-process timeout recovery is documented
but not demonstrated by this particular smoke test.
