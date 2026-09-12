# Ingredient Traceability

Use a small evidence-linked record to answer: why is this choice valid, what
would invalidate it, and what work can safely resume? The paperwork should make
the next action clearer. It cannot manufacture approval or truth.

## Run identity and storage

For authorized repository artifacts, keep a human-readable `ledger.md` under
`docs/super-grill/<run-id>/` (or the user's location). Choose a distinct run ID;
record route, original order, decision authority and an exact plan identifier.
A plan identifier denotes the particular plan being executed; record revisions
when its requirements change. Separate runs do not share completion markers.
For short/read-only requests, keep equivalent records in conversation.

Optional `state.json` enables structural graph checks. It uses schema version 1,
`run_id`, `plan_id`, and a `nodes` object keyed by node ID. Each node has `id`, `kind`, `summary`,
`depends_on`, `status`, and integer `revision`. See the [complete example state](../examples/ingredient-recall/state.json) for
accepted syntax and the helper's `--help` for command arguments. Plain Markdown is a complete
fallback; do not install Python merely to run a ceremony.

## Link load-bearing ingredients

Use stable IDs when they improve traceability:

| Kind | Example | What to record |
| --- | --- | --- |
| goal | G-01 | User outcome and observation that would satisfy it |
| assumption | A-01 | Premise, supporting evidence, what would falsify it |
| decision | D-01 | Chosen behavior, alternatives, rationale, who decided and within what authority |
| requirement | R-01 | Exact behavior/constraint derived from goals and decisions |
| task | T-01 | Scope, prerequisites, status, artifacts and validation |
| evidence | E-01 | Claim tested, method, observation, file snapshot, limits |

`depends_on` points from a dependent to its prerequisites. For example:

```text
G-01: edit a shopping list offline
A-01: one device edits each list
D-01: use last-write-wins        depends_on: G-01, A-01
R-01: save the latest whole list depends_on: D-01
T-01: implement local save       depends_on: R-01
E-01: one-device save passes     depends_on: T-01, A-01
```

Do not introduce dependency cycles to express supporting observations. Evidence
validating a task depends on that task; the task may *cite* the evidence as its
validation without also depending on it. A new decision based on an observation
can depend on that evidence, provided the result remains acyclic. Separate causal
prerequisites, validation citations and documentary links.

Unknown is a valid state. Distinguish observed facts, user decisions, delegated
rulings, hypotheses and deferred questions in the human ledger. A graph's `status`
is a work marker, never proof of human authorization or business correctness.

## Evidence receipts

For each material claim record:

```markdown
Evidence: E-01
Claim: edits survive an application restart on one device
Depends on: T-01, A-01
Method: command or exact interaction sequence
Observed: actual output/exit status or visible state
Scope: paths/content snapshot, environment and scenario
Limit: does not establish concurrent multi-device behavior
Recorded at: timestamp
```

A test command that passed at an older content snapshot is historical evidence.
Re-run covering checks when that content or a relevant prerequisite changes.
Unchanged checks may retain their receipts; do not relabel a past run as fresh.
Capture only relevant paths and non-sensitive observations. Never copy secrets
into a trace just because a command printed them.

## Ingredient Recall

Trigger recall on contrary evidence, a user change, or an invalidated prerequisite.
Another ceremonial lens alone does not invalidate an answer; name its actual new
counterexample or uncertainty first.

1. Identify the changed node and record the new fact/decision, reason and revision.
2. Follow reverse dependency edges to collect all reachable dependents.
3. Preserve their old decisions, artifacts and observations; mark their validity
   `stale`, do not erase history or delete work.
4. List affected approvals, requirements, tasks and evidence; leave unrelated
   branches untouched. Stale means needs re-evaluation, not certainly wrong.
5. Resume at the earliest affected decision/station. Ask only for undelegated
   material choices. Revalidate surviving work instead of automatically rebuilding.
6. Attach new evidence/revisions and record which stale items have been resolved.

> Ingredient Recall: A-01 now permits two editors. D-01, R-01, T-01 and
> E-01 return to inspection. The typography remains legally edible.

An unsupported root or missing dependency blocks graph-based conclusions until
reconciled. A timeout alone does not invalidate a live agent or justify duplicating
its assignment.

## Cold-start recovery

Before resuming after interruption or context loss:

1. Match run ID, plan identity/revision, repository and worktree. A mismatch is
   a different run until reconciled; do not overwrite its state.
2. Read current user instructions and the relevant ledger frontier.
3. Check referenced files, actual Git status and relevant content snapshots.
   `HEAD` alone misses staged/unstaged/untracked work.
4. Check live agent handles through the host. Resume a confirmed live assignment;
   do not create a replacement merely because a wait timed out. A terminated or
   missing handle requires checking its report and actual files before redispatch.
5. For a completed task, verify its artifacts and evidence still match. Continue
   at the first incomplete/stale dependency. For a mid-fix task, retain the finding
   IDs and round number; do not reset the loop by forgetting it.
6. Record the reconciliation and next action. Unsupported completion becomes
   unverified work, not a green check adopted from conversation memory.

## Optional helper

Run from this installed skill's directory, using absolute state paths when needed:

```bash
python3 scripts/state_graph.py init /path/to/state.json --run-id dinner-01 --plan-id plan-01
python3 scripts/state_graph.py validate /path/to/state.json --run-id dinner-01 --plan-id plan-01
python3 scripts/state_graph.py recall /path/to/state.json --run-id dinner-01 --plan-id plan-01 --changed A-01 --reason 'Two devices can edit'
```

Populate nodes according to the schema before recall. A changed node's revision
increases; the helper preserves its status so the coordinator must explicitly
record whether the new premise is accepted, rejected, or unknown. Dependent
statuses become stale; previous receipts remain historical evidence. Inspect the affected IDs
and the human decision/evidence receipts after any helper operation. Validation
checks graph shape and identity; it cannot approve a decision, establish a
requirement is correct, or prove an implementation is complete.
