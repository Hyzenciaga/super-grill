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

Production behavior changes follow this cycle when meaningful automated tests
are available. For a document/configuration edit, use the relevant direct check;
for a disposable experiment, follow [taste-test.md](taste-test.md). Record what
was actually verified. Never invent a failing test merely to earn an achievement.

### Raw

Write one focused test that describes the desired behavior. Run it before
implementation and watch it fail for the expected missing behavior.

- If it passes, it does not prove the new behavior; correct the test.
- If it errors for setup reasons, fix the test until it fails correctly.
- If no automated test is reasonable, define another falsifiable check, record
  its scope and limits, and proceed within existing authorization.

### Sizzle

Implement the smallest change that satisfies the raw test. Run the focused test
and then the proportionate broader suite.

- Fix implementation failures, not the desired expectation.
- Investigate newly failing checks for regressions. Distinguish recorded
  pre-existing failures; do not declare them caused by this task or halt unrelated
  work without evidence.
- Do not add speculative flexibility while the center is uncooked.

### Rest

Improve names, duplication, interfaces, and structure while tests remain
green. Re-run the focused and broader checks after resting.

Tests written after implementation do not establish that a regression check
would catch the original defect. Where useful, demonstrate the failure in an
isolated copy or via a safe reversible comparison. Preserve user work; never
delete existing code for the ceremony. Report the actual sequence honestly;
**Microwave Retcon** cannot turn historical green output into observed Raw.

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
conflicts with an approved decision, identify the affected trace nodes. Rule
within delegated authority; otherwise put the material choice before the user.
Do not silently rewrite goals to satisfy a reviewer.

Never blindly obey an inspector merely because they own a clipboard.

## Thermometer Court

Before claiming anything is complete, fixed, passing, safe, or ready, match the
claim to its current content snapshot and relevant prerequisites. Review evidence
includes uncommitted and new files; see [kitchen operations](kitchen-industrial-complex.md).

For each material claim:

1. **Charge:** write down the exact claim.
2. **Instrument:** identify the command or observation that proves it.
3. **Measurement:** run the relevant complete check on the actual current result.
   Reuse an unchanged receipt only with its original timestamp and scope; never
   describe a reused observation as newly run.
4. **Cross-examination:** read full output, exit status, failure count, and
   warnings.
5. **Verdict:** compare evidence with the exact claim.
6. **Statement:** only then report success.

For regression proof when practical:

1. Run with the fix and observe pass.
2. In an isolated copy or safely reversible setup, remove only the fix without
   disturbing user changes, staged state, or other workers.
3. Run and require the test to fail for the expected reason.
4. Restore the fix and run to pass again.

Inspect subagent evidence and its match to current files; confidence-only reports,
partial commands, "looks fine," and emotional warmth are inadmissible. An analysis
conclusion uses source/scenario evidence; a visual claim needs visual inspection.
Passing unit tests alone does not establish a delivered user flow works.

## Closing-time tribunal

For a build whose relevant verification has passed:

1. Detect whether the work is in a normal checkout, linked worktree, detached
   workspace, or host-owned environment.
2. Determine the base branch from evidence.
3. Honor a disposition the user already authorized. If a material choice is
   missing, present only options valid for that environment:
   - merge locally;
   - push and open a review request;
   - keep the branch and workspace as-is.
4. Execute only the user's chosen and authorized option.
5. Re-run tests after a local merge before cleanup.
6. Preserve the workspace for active review feedback.
7. Clean up only workspaces this workflow created and owns.

Discarding work is never a casual fourth menu item. It requires explicit
authorization for the exact target, following host rules. Never infer cleanup
permission from a completion milestone. Other routes finish with their requested
result, not a manufactured branch ceremony.
