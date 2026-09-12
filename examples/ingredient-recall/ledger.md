# Example Grill Ledger — Ingredient Recall

This is an illustrative fixture, not evidence that a shopping-list app was built
or tested. All completion/status fields below are fictional inputs for the demo.

Run: demo-recall
Plan: demo-plan
Route: build
Heat/service: well-done / single-skewer
Order: local offline shopping list
Authority: example only; no actual user approval or external action is granted

## Settled record before recall

- G-01: edit a list offline.
- A-01: assume one device edits each list.
- D-01 depends on G-01/A-01: overwrite the latest list.
- R-01 depends on D-01: whole-list local persistence.
- T-01 depends on R-01: implement saving.
- E-01 depends on T-01/A-01: an illustrative one-device restart receipt.
- T-02 depends on G-01: readable typography, unrelated to editor concurrency.

## New information

Two devices may edit the same list. Recall from A-01, preserving the old record.
Expected structural result: D-01, R-01, T-01 and E-01 become stale; T-02 and G-01
remain unchanged. The helper increments A-01's revision but does not decide its
new truth/status for you. Record the new premise in the human ledger and state.

Next real decision: what synchronization/conflict behavior, if any, serves the
revised order? That is a user decision unless already delegated. A recall is not
authorization to add a cloud backend or rerun the entire project.

> A-01 has been recalled. Four dishes return to inspection. Typography continues
> to meet all known dietary requirements.
