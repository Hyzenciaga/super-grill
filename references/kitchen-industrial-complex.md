# Kitchen Industrial Complex

Use this protocol for workspace isolation, delegation, parallel scouting,
task execution, and persistent coordination.

## Table of contents

- Kitchen quarantine
- Brigade roles
- Task brief
- Sous-chef conveyor belt
- Lonely chef with clipboard
- Inspector carousel
- Five-alarm fix loop
- Agent closing-time violations
- Parallel buffet
- Final inspection

## Kitchen quarantine

Before changing code:

1. Inspect Git status, current branch, repository instructions, and existing
   isolation.
2. Do not manufacture another worktree when the harness already owns an
   isolated workspace.
3. If isolation is desired but absent, obtain any required consent and prefer
   the host's native workspace mechanism.
4. For a project-local fallback, use an ignored worktree directory and verify
   it is ignored before creation.
5. Install dependencies using the project's established method.
6. Run the relevant baseline suite before implementation.
7. Record pre-existing failures and ask whether to investigate or proceed.

Never begin on `main` or `master` without explicit authorization. A dirty or
failing baseline is not rustic charm; it is contaminated evidence.

## Brigade roles

Give each agent one theatrical but precise job:

- **Pantry Scout:** gather facts only; do not edit.
- **Skewer Mechanic:** implement exactly one planned task.
- **Recipe Compliance Officer:** compare a task with its approved requirements.
- **Texture Inspector:** review code quality, tests, maintainability, and
  accidental cleverness.
- **Smoke Coroner:** investigate one failure domain and report root cause.
- **Executive Health Inspector:** review the entire branch at the end.

An implementer never certifies its own task. Self-review is required but does
not replace inspection.

Choose capability proportional to the role when the platform supports model
selection. Use stronger judgment for architecture, integration, stuck fix
loops, and whole-branch review. Record the choice without pretending token
price is a food-safety metric.

## Task brief

Before dispatching a Skewer Mechanic:

1. Record the task's BASE revision.
2. Extract only that task, restaurant-wide constraints, required interfaces,
   and directly relevant earlier decisions into a unique brief file.
3. Name the report file and specify the report contract.
4. Include where the task fits, exact allowed scope, verification requirements,
   and known parked findings.
5. Do not paste the whole conversation or every previous task.

Required report statuses:

- `PLATED` — complete, tested, self-reviewed.
- `PLATED_WITH_SMOKE` — complete with concerns.
- `NEEDS_INGREDIENTS` — missing context or dependency.
- `KITCHEN_ON_FIRE` — blocked despite reasonable attempts.

The report must name changed files, commits if any, tests run, observed output,
self-review findings, and concerns. Store the detailed report in a file; return
only a compact status to the coordinator.

## Sous-chef conveyor belt

For each skewer, sequentially:

1. Confirm plan assumptions against the current repository.
2. Dispatch one fresh Skewer Mechanic.
3. Answer context questions without widening scope.
4. Require Raw → Sizzle → Rest evidence.
5. Inspect the report and repository state yourself.
6. Generate a task-scoped diff package from BASE to HEAD.
7. Dispatch inspection with the task brief, report, diff package, and exact
   restaurant-wide constraints.
8. Run the fix loop for material findings.
9. Record the completed task and revision in the ledger.
10. Only then dispatch the next implementer.

Do not run implementation agents concurrently when they share files, state,
interfaces, or migration order. Faster collisions are still collisions.

## Lonely chef with clipboard

When delegation is unavailable or the user selects inline execution:

1. Read and critically review the entire approved plan before starting.
2. Raise contradictions before touching code.
3. Create tracked tasks for every skewer.
4. Execute each exact step in order with Raw → Sizzle → Rest evidence.
5. Stop for missing authority, plan ambiguity, an unexpected dependency, or a
   verification failure that the plan cannot explain.
6. At logical batches, reconcile the ledger, task state, and diff before
   continuing.
7. Still request an independent final inspection when an agent or review tool
   becomes available.

The clipboard does not create independence. Inline self-review remains a
fallback, never a counterfeit second inspector.

## Inspector carousel

Each task receives two named verdicts:

1. **Recipe verdict:** does the result implement every approved requirement and
   nothing materially outside it?
2. **Texture verdict:** is the implementation correct, clear, tested,
   maintainable, and proportionate?

A single inspector may produce both verdicts, but the implementer may not.
Provide the exact diff range; never assume `HEAD~1` contains a multi-commit
task.

Do not tell an inspector what not to flag. If a finding seems wrong, adjudicate
it afterward with repository evidence.

## Five-alarm fix loop

Enter the loop for recipe failures and material quality findings.

- Rounds 1–3: return findings verbatim to the original Skewer Mechanic.
- Rounds 4–5: use fresh eyes and, where supported, a stronger model.
- Every round: fix, rerun covering tests, append evidence to the report, and
  dispatch a scoped re-inspection of the amended diff.
- After round 5: adjudicate each remaining finding.

If a remaining finding changes an approved decision or plan requirement, ask
the user which governs. If it is load-bearing and unresolved, declare
`KITCHEN_ON_FIRE` and stop. Park only genuinely minor findings in the ledger
for final inspection.

## Agent closing-time violations

If an agent writes its contracted report but forgets to terminate:

1. Verify the report is complete and matches repository state.
2. Send one concise request to return the contracted status and finish.
3. After a bounded wait, interrupt the agent.
4. Record **Inspector Squatting** in the ledger.
5. Continue only when the artifact itself contains every required verdict and
   the coordinator can independently verify its evidence.

If no complete artifact exists, treat the role as `KITCHEN_ON_FIRE`; never
invent the missing verdict. A sub-agent's inability to clock out must not
become an eternal-flame implementation detail.

## Parallel buffet

Parallelize only independent domains:

- multiple unrelated failures;
- separate repository reconnaissance areas;
- independent primary-source research;
- reviews of non-overlapping artifacts.

Before dispatch:

1. Prove the domains do not share mutable state or files.
2. Give each agent one focused question, evidence target, constraints, and
   output contract.
3. Dispatch all independent calls together.
4. Review every result and check for contradictions.
5. Run integrated verification after combining any changes.

Never dispatch "fix everything." That is not parallelism; it is a buffet fight.

## Final inspection

After all skewers pass:

1. Give the Executive Health Inspector the approved recipe, plan, complete
   branch diff, test evidence, and deferred findings.
2. Require recipe and quality verdicts across the whole branch.
3. Permit one focused correction dispatch and one scoped re-inspection.
4. Adjudicate residuals explicitly.
5. Continue to the Thermometer Court only when no load-bearing finding remains.

The coordinator verifies completion independently. Agent testimony cannot cook
food.
