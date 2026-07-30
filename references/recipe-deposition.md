# Recipe Deposition

Use this protocol for sectional design, the written specification, and the
implementation plan.

## Table of contents

- Architectural dry rub
- Written recipe
- Recipe cross-examination
- Imaginary food-poisoning banquet
- Skewer map
- Task format
- Plan cross-examination
- Catering tickets
- Cooking-route handoff

## Architectural dry rub

Start from repository evidence and settled decisions. Present the design in
sections scaled to complexity. After each section, ask whether it is correct
and run the heat-required lenses before moving on.

Cover when relevant:

- responsibilities and module boundaries;
- interfaces and dependencies;
- data creation, transformation, retention, and deletion;
- control flow and failure flow;
- security and privacy authority;
- tests and falsifiable success evidence;
- operations, observation, rollback, and recovery;
- compatibility and migration;
- explicitly excluded work.

Prefer small units with clear jobs and narrow interfaces. Improve adjacent
structure only when it directly serves the order; unrelated refactors belong
in the walk-in freezer.

## Written recipe

For repository work, save the approved design to:

`docs/super-grill/YYYY-MM-DD-<topic>/spec.md`

Write it so a cold reader can explain the goal, boundaries, chosen approach,
interfaces, failure behavior, tests, and non-goals without access to the
conversation.

Do not advance merely because the conversational design was approved. The
written artifact receives its own approval after cross-examination.

## Recipe cross-examination

Inspect the written recipe for:

1. **Mystery ingredients** — `TBD`, `TODO`, vague verbs, or unstated values.
2. **Contradictory temperatures** — two sections require incompatible
   behavior.
3. **Runaway catering** — the spec contains independent projects that need
   separate grill cycles.
4. **Ambiguous servings** — a requirement permits two materially different
   interpretations.
5. **Vocabulary fraud** — terms disagree with `vocabulary.md`, existing docs,
   or code.
6. **Sauce without a dish** — a component or feature has no approved
   requirement.
7. **Dish without a sauce** — an approved requirement has no design coverage.

Fix discovered issues in the artifact, then ask the user to review the file.
If they request changes, update it and repeat the cross-examination.

## Imaginary food-poisoning banquet

Before planning, assume the approved design failed spectacularly:

1. Name the most plausible cause.
2. Explain the first observable symptom.
3. Identify which check, log, test, or person would notice.
4. State the blast radius and irreversible consequence.
5. Describe rollback or recovery.
6. Name the design assumption the failure disproves.

Update the recipe before continuing when the banquet exposes a gap. If the risk
is knowingly accepted, record who accepted it and why. Award no resilience
points for imagining an outage without changing anything.

## Skewer map

Before listing tasks, map every file to one responsibility and every
cross-task interface to an exact name and type. Split work where a reviewer
could accept one unit while rejecting its neighbor. Fold scaffolding,
configuration, docs, and cleanup into the task whose deliverable needs them.

Every task must:

- produce an independently testable vertical slice;
- carry its own Raw → Sizzle → Rest cycle;
- name exact files;
- define what it consumes and produces;
- include runnable verification and expected output;
- end with an inspection gate;
- include a commit step only when commits are authorized.

## Task format

Save the plan beside the spec as `plan.md`. Start with:

```markdown
# <Feature> Catering Plan

> Required cooking route: Brigade or Lonely Chef.

Original order:
Architecture:
Kitchen equipment:

## Restaurant-wide constraints

- Exact versions, limits, copy, naming, platform, privacy, and compatibility
  requirements copied from the approved recipe.
```

Use this structure for every task:

````markdown
## Skewer N: <independently edible result>

Files:
- Create: `exact/path`
- Modify: `exact/path`
- Test: `exact/path`

Interfaces:
- Consumes: `exactName(type) -> type`
- Produces: `exactName(type) -> type`

- [ ] Raw: write the failing test with actual test code
- [ ] Prove rawness: run `<exact command>`
      Expected: FAIL for `<specific missing behavior>`
- [ ] Sizzle: write the smallest implementation with actual code or exact edits
- [ ] Check temperature: run `<exact command>`
      Expected: PASS with `<specific evidence>`
- [ ] Rest: improve structure without changing behavior
- [ ] Recheck temperature: run `<focused and broader commands>`
- [ ] Inspect: compare the diff with this skewer and the recipe
- [ ] Commit, only if authorized: exact paths and message
````

Each checkbox is one small action. Do not write:

- "add appropriate handling";
- "write tests";
- "similar to the previous task";
- `TBD`, `TODO`, or "implement later";
- an interface not defined in this or an earlier task;
- a command without the success or expected-failure evidence.

## Plan cross-examination

Run three passes:

1. **Coverage deposition:** map every recipe requirement to at least one
   skewer.
2. **Contraband scan:** remove placeholders, speculative extras, and vague
   instructions.
3. **Interface lineup:** verify names, signatures, types, files, and values
   agree across tasks.

Apply extra heat passes from `grill-levels.md`. Correct the plan inline, then
obtain explicit user approval.

## Catering tickets

When the approved effort spans multiple sessions and the user authorized an
issue tracker, convert skewers into agent-ready catering tickets:

- one independently testable result per ticket;
- exact recipe and plan pointers;
- explicit blocking edges;
- required interfaces and evidence;
- no duplicate interview questions already settled upstream.

Create tickets first and wire blocking relationships second, after identifiers
exist. Work unblocked tickets first. If no external tracker is authorized, the
checkbox plan remains the local ticket counter; do not create cloud paperwork
merely because the joke suggested it.

## Cooking-route handoff

After approval, offer:

1. **Sous-Chef Conveyor Belt** — fresh implementer per skewer, separate
   inspector, fix loops, final whole-kitchen inspection.
2. **Lonely Chef With Clipboard** — inline execution with the same tests,
   ledger, inspection gates, and stop conditions.

Record the choice. Do not start cooking in the same breath as asking.
