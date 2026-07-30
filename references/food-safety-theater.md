# Food Safety Theater

Use this protocol for test-first work, debugging, review handling, final
verification, and branch disposition.

## Table of contents

- Raw, Sizzle, Rest
- Smoke autopsy
- Receiving inspector notes
- Thermometer Court
- Closing-time tribunal

## Raw, Sizzle, Rest

Every behavior change follows this cycle.

### Raw

Write one focused test that describes the desired behavior. Run it before
implementation and watch it fail for the expected missing behavior.

- If it passes, it does not prove the new behavior; correct the test.
- If it errors for setup reasons, fix the test until it fails correctly.
- If no automated test is reasonable, define another falsifiable check and
  obtain any necessary user agreement before proceeding.

### Sizzle

Implement the smallest change that satisfies the raw test. Run the focused test
and then the proportionate broader suite.

- Fix implementation failures, not the desired expectation.
- Stop if unrelated tests become red.
- Do not add speculative flexibility while the center is uncooked.

### Rest

Improve names, duplication, interfaces, and structure while tests remain
green. Re-run the focused and broader checks after resting.

Writing tests only after implementation unlocks **Microwave Retcon** and does
not count as observing Raw. Code written prematurely must return to the earliest
falsifiable state; ceremony cannot retroactively make it test-first.

## Smoke autopsy

Never season over a symptom.

### 1. Establish the fire

- Read the complete error and exit status.
- Reproduce consistently with the tightest command available.
- Inspect recent changes and relevant environment differences.
- In multi-component systems, gather boundary evidence showing where the first
  bad state appears.
- Trace the bad value backward to its origin.

### 2. Compare kitchens

- Find a working example in the same repository.
- Compare it with the failing path line by line.
- List every difference before deciding which matters.
- Identify assumptions, dependencies, and ownership.

### 3. Name one suspect

State one falsifiable hypothesis:

> I believe `<root cause>` because `<evidence>`; changing `<single variable>`
> should produce `<observation>`.

Test minimally. Do not stack fixes and call the pile an experiment.

### 4. Repair the source

Create or confirm a failing regression test, implement one root-cause fix, and
run focused plus broader verification.

After three failed fixes, stop and convene the **Architecture Arson Hearing**.
Question whether the chosen boundary or design is the real problem before
trying fix four.

## Receiving inspector notes

For every review finding:

1. Read the entire finding.
2. Restate the technical requirement or ask for clarification.
3. Verify it against the current repository.
4. Evaluate whether it is correct and in scope.
5. Respond with evidence, not gratitude theater.
6. Implement one accepted item at a time and test it.

Push back when a suggestion is technically wrong, violates the approved
recipe, or adds unrequested professional-sounding garnish. If the finding
conflicts with an approved decision, put both before the user.

Never blindly obey an inspector merely because they own a clipboard.

## Thermometer Court

Before claiming anything is complete, fixed, passing, safe, or ready:

1. **Charge:** write down the exact claim.
2. **Instrument:** identify the command or observation that proves it.
3. **Measurement:** run the complete check fresh.
4. **Cross-examination:** read full output, exit status, failure count, and
   warnings.
5. **Verdict:** compare evidence with the exact claim.
6. **Statement:** only then report success.

For regression proof when practical:

1. Run with the fix and observe pass.
2. Temporarily revert the fix without losing work.
3. Run and require the test to fail for the expected reason.
4. Restore the fix and run to pass again.

Subagent reports, old output, partial commands, "looks fine," and emotional
warmth are inadmissible.

## Closing-time tribunal

After fresh tests pass:

1. Detect whether the work is in a normal checkout, linked worktree, detached
   workspace, or host-owned environment.
2. Determine the base branch from evidence.
3. Present only options valid for that environment:
   - merge locally;
   - push and open a review request;
   - keep the branch and workspace as-is.
4. Execute only the user's chosen and authorized option.
5. Re-run tests after a local merge before cleanup.
6. Preserve the workspace for active review feedback.
7. Clean up only workspaces this workflow created and owns.

Discarding work is never a casual fourth menu item. It requires an explicit
request and confirmation of the exact target.
