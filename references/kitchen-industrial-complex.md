# Kitchen Industrial Complex

Use for authorized workspace changes, delegation, task execution, review evidence
and recovery. Apply the main skill's route, authority and stop rules throughout.
Read [traceability.md](traceability.md) when creating or resuming a durable run.

## Kitchen quarantine

Before code changes, inspect repository instructions, Git status/current branch,
existing worktree isolation, setup commands and the relevant test baseline.
Preserve pre-existing edits, staged changes and untracked files. Record existing
failures separately from regressions; investigate blockers that affect this task,
continue unaffected work, and ask only for missing material scope/authority.

Do not manufacture a worktree if the host already isolates the work. When needed,
use the host's native mechanism or a verified ignored project-local directory.
Respect authorized branch scope; do not commit on a protected/shared branch or
clean up someone else's checkout. Install dependencies only when required by the
order using the established project method. A research conversation needs none
of these side effects merely to fill a station.

## Brigade roles

| Role | Actual responsibility |
| --- | --- |
| Pantry Scout | Investigate one fact domain without editing |
| Skewer Mechanic | Implement a scoped task, test and self-review |
| Recipe Compliance Officer | Compare requested and delivered behavior |
| Texture Inspector | Review correctness, clarity, tests and maintainability |
| Smoke Coroner | Trace one concrete failure |
| Executive Health Inspector | Review cross-task behavior and the whole requested change |

Subagents require host support and authorization. Match capability to judgment
needed; follow an explicit requested model when available, and report unsupported
model/tool limitations honestly. The coordinator owns delegation and gates. A
worker does not recursively recruit helpers or reviewers unless that delegation
was explicitly included in its brief. Do not create user-owned app tasks merely
as a substitute for internal agents.

An implementer self-reviews but never certifies an independent review of its own
work. One independent inspector may issue both recipe and quality verdicts. With
no independent reviewer available/authorized, use the solo fallback below.

## Task brief and reports

For each independently reviewable slice, record a task ID, run/plan identity and
current snapshot before dispatch. Use fresh task context: the brief contains only
relevant requirements, global constraints, interfaces, earlier decisions it needs,
allowed paths, pre-existing changes, evidence requirements and report contract.
Do not paste the full session or expose the coordinator's preferred review verdict.
Give artifacts as file pointers when available; read-only tasks may return their
report in conversation rather than write files.

Required status vocabulary:

- `PLATED`: requested slice implemented, checked and self-reviewed.
- `PLATED_WITH_SMOKE`: complete with explicit concerns requiring adjudication.
- `NEEDS_INGREDIENTS`: missing context or prerequisite.
- `KITCHEN_ON_FIRE`: blocked after reasonable attempts.

Reports contain task/run identity, changed files and actual snapshot, commits if
any, tests and observed outcomes, self-review findings, limits and open concerns.
A report status is testimony, never the coordinator's completion evidence.

## Review evidence, including uncommitted work

A BASE-to-HEAD diff covers only commits. If committing was not requested, the task
can leave HEAD unchanged while changing every relevant file. Capture relevant
paths before execution, then compare with their actual contents after execution:
committed, index/staged, working-tree and untracked states all matter.

Optional standard-library helpers, run from the installed skill directory:

```bash
python3 scripts/review_evidence.py capture --repo /path/to/repo --output /tmp/grill-before --path src --path tests
python3 scripts/review_evidence.py package --repo /path/to/repo --baseline /tmp/grill-before --output /tmp/grill-review --path src --path tests
python3 scripts/review_evidence.py verify --repo /path/to/repo --package /tmp/grill-review --path src --path tests
```

A review package contains `task.patch` (captured before versus current content),
`before-tree/` and `after-tree/`, Git layer patches and `review.json`. Inspect the
actual task patch and pre-existing-work warnings, not just the Git layer patches.
The verifier exits 0 for a matching snapshot, 1 for current-state drift, and 2
for invalid inputs or unusable evidence. A failed verifier is not a clean review.

Use a fresh output location outside the repository. Choose exact task-owned paths;
never point indiscriminately at a repository containing private data or credentials.
Pass paths without following symlinks outside the checkout. See `--help` for the
package drift-verification command. The coordinator inspects package warnings and
file changes; a hash is a content identity, not correctness or attribution proof.

Without Python, capture the relevant pre-task file contents and `git status`,
then assemble committed/index/working-tree diffs and explicitly inspect new files.
For files already dirty, distinguish the earlier content from changes introduced
during this task. A final diff against Git's base alone cannot do that. If the
baseline was not captured, mark attribution uncertain rather than inventing it.
Keep baseline snapshots outside the paths being measured.

If a user or another worker changes a task file during execution, flag overlap
and reconcile before attribution or overwriting. Verify the review still matches
the current file snapshot before applying its verdict. A later change invalidates
a review of that content; retain the old review as historical evidence.

## Sous-chef conveyor belt

1. Reconcile run/plan identity and current assumptions; preflight task dependency
   and shared-interface consistency against the spec.
2. Capture a baseline. Dispatch the scoped Skewer Mechanic, or implement inline.
   Same-shape small edits can be one reviewable batch. Do not split each keystroke
   into an independent project solely to manufacture headcount.
3. Answer context requests using evidence and settled decisions. Make delegated
   reversible rulings; stop only dependent work for missing material authority.
4. Require applicable Raw → Sizzle → Rest evidence, or the documented alternative
   check for non-behavior/experimental work.
5. Inspect the report and actual files. Build the complete task review package.
6. Obtain both recipe and quality verdicts through an independent inspector when
   available, otherwise the honest solo fallback. Resolve unverifiable assertions.
7. Run the fix loop for material findings, record task evidence and completion,
   and continue the approved plan without another “should I continue?” prompt.

## Lonely chef with clipboard

When delegation is absent, declined or unnecessary, critically read the plan and
perform its scoped implementation and checks inline. Perform a distinct review
pass against requirements and actual changes, recording two verdicts with
`review_mode: self-reviewed` and `independence: unavailable` (or `not requested`).
This satisfies the fallback gate; it is never called independent review.
If the order explicitly requires an independent reviewer, report that unmet
requirement instead of silently substituting self-review.

The same material-defect and evidence standards apply. A tool limitation is not
a discovered defect and does not by itself prohibit completing a task through the
fallback. The clipboard does not create a second employee.

## Inspector carousel and Five-alarm fix loop

Every review has two separate verdicts:

- **Recipe:** implements approved requirements without material scope expansion.
- **Texture:** correct, clear, tested and proportionate to the task.

Give the inspector exact requirements and the actual reviewed snapshot. Do not
pre-instruct it to ignore a suspected issue; adjudicate findings against evidence.
Separate verified defects, unsupported concerns, and purely stylistic suggestions.
For an item not verifiable within a task diff, the coordinator gathers the missing
cross-task evidence before accepting a completion claim.

For material findings:

1. Rounds 1–3: return the actual finding to the original implementer when its live
   context exists; otherwise use a fresh brief carrying the report and finding.
2. Rounds 4–5: use fresh eyes and greater capability where authorized/available.
   A model change alone is not a new hypothesis.
3. Every round: fix, run covering checks, record evidence, re-review changed scope.
4. After round 5: adjudicate remaining findings. A changed approved requirement
   triggers recall; resolve routine implementation rulings within delegated scope.
   An unresolved load-bearing defect stays blocked. Park only minor findings with
   rationale for final review. Do not reset round numbering to bypass the limit.

Finite heat passes examine artifacts; fix rounds repair findings. Do not multiply
one loop by the other to create undocumented mandatory rework.

## Parallel buffet

Parallelize independent research, alternative design, non-overlapping artifacts,
or implementation slices only when ownership, interfaces and mutable state are
clear. Shared files, generated files, migrations and integration order count as
shared state. Assign exact scopes, evidence targets and output contracts. If work
cannot be safely separated, execute it sequentially. Review every result and run
integrated checks when combining changes.

For alternative design use [blind-tasting.md](blind-tasting.md); multiple role
names in one context are not independent sources.

## Recovery and agent closing time

Persist task ID, agent handle, status, brief/report paths, snapshot and fix round.
After compaction or interruption, follow [Cold-start recovery](traceability.md).
Poll a specific confirmed live handle; a wait timeout does not mean it died.
Continue unrelated local work while waiting. If the host reports a terminal or
missing handle, inspect its report and files before deciding whether to redispatch.

If an agent wrote a complete report but will not return, inspect the artifact,
send one finish request, then use a bounded wait and interrupt where supported.
Record **Inspector Squatting**. Continue only when actual evidence contains every
required result; do not invent a missing verdict. If the user stops, send the stop
to owned live workers, preserve their changes and report any task that could not
be stopped. Do not restart cancelled work without a new instruction.

## Executive inspection and disposition

Review the whole requested change against the spec/plan, current evidence and
parked findings. Use an independent whole-change inspector when available, or
label solo review. Permit a focused correction pass and scoped re-review, then
adjudicate residuals. Do not claim completion with a load-bearing defect.

Reconcile the trace from goal to evidence, apply the remaining heat examinations,
and enter the [Thermometer Court](food-safety-theater.md). Perform only the already
authorized branch disposition; leave unrelated branches, worktrees and files alone.
