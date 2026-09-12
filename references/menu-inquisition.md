# Menu Inquisition

Use this protocol whenever intent, terminology, scope, or a decision remains
unsettled. Apply the main skill's route, stop and authority rules throughout.
A clear instruction to stop questioning ends the interview; record unresolved
choices as uncertainties or make them within explicit delegated authority.

## Table of contents

- The decision tree
- Service styles
- Fact scouts
- Wheeled visual-aid cart
- Paper-trail basting
- Artifact rotisserie
- The fog smoker
- Reverse searing
- Completion gate

## The decision tree

Treat each unresolved decision as a node. Record its prerequisites and the
branches its possible answers open. A node is ready only when its prerequisites
are settled.

For every ready node:

1. Investigate discoverable facts first.
2. State the decision and why it matters.
3. Give the house recommendation and reasoning.
4. For an undelegated material choice, ask according to the service style and
   wait. For an already answered choice, reuse the answer. For a delegated
   choice, record your ruling and rationale without another approval loop.
5. Do not treat silence as an answer or a recommendation as authorization.
6. Record the answer/ruling, rejected alternatives, rationale, and newly opened
   branches; link load-bearing nodes using [traceability.md](traceability.md).
7. Recompute the frontier.

Never ask a downstream question whose wording assumes an upstream answer.
An obvious recommendation alone does not delegate a decision. Explicit user
delegation does; preserve its scope across stations.

## Service styles

### Single-skewer

Ask exactly one decision per turn. Prefer a short multiple-choice menu when the
options are naturally discrete, but allow open responses. A topic requiring
five decisions becomes five skewers, not one kebab-shaped paragraph.

### Frontier-buffet

Compute every currently ready node. Ask the whole frontier in one numbered
round, each with a recommendation. Do not include a question that depends on
another answer in the same round. After the user answers, reshape the tree and
serve the next frontier.

The buffet exists for users who want their bewilderment delivered in bulk. Do
not select it implicitly.

## Fact scouts

Facts are kitchen labor, not diner homework.

- Search files, history, documentation, and tools before asking.
- When multiple fact questions are independent and delegation is available and
  authorized, dispatch
  focused scouts concurrently.
- Give each scout one domain, the exact evidence needed, constraints, and an
  authorized report location or in-conversation return contract. Without scouts,
  investigate directly; do not make tool availability a decision blocker.
- A running scout blocks only the dependent branch; continue grilling other
  ready branches.
- Inspect scout evidence yourself. A scout report is testimony, not proof.

## Wheeled visual-aid cart

Use a mockup, diagram, layout comparison, or flow when it makes a real decision
clearer. Use the host's available visualization tools within the existing order;
a visual already requested does not need another invitation. Ask only when a
new service, cost, or action genuinely needs authorization. Respect a declined
visual mode.

When discussion needs an observable test, read [taste-test.md](taste-test.md).
A static illustration cannot establish that logic, persistence, or performance
works. Mark predicted behavior separately from an observed interaction.

The cart is a tool, not a parallel restaurant. Its output returns to the same
decision tree and approval gates.

## Paper-trail basting

For repository work, turn settled language and expensive decisions into durable
parody records inside the current Super Grill artifact directory.

### Vocabulary on probation

Reuse the project's existing glossary/domain context when present. Otherwise
maintain `vocabulary.md` when project-specific terms matter:

- Challenge overloaded or conflicting terms immediately.
- Compare user language with existing docs and code.
- Choose one canonical term and list discouraged aliases.
- Keep definitions about meaning, not implementation.
- Update the file when the term settles, not in a final batch.

### Permanent menu decisions

Record a decision card under `decision-cards/NNNN-<slug>.md` only when all are
true:

1. Reversing it would be costly.
2. A future maintainer would find it surprising.
3. Real alternatives competed.

Keep a card short:

```markdown
# Decision: <title>

Context:
Ruling:
Why this sauce won:
Rejected sauces:
Consequences:
```

This preserves the behavior of a durable architectural record without forcing
the restaurant to use anyone else's menu terminology.

## Artifact rotisserie

When the user is grilling a named artifact rather than a new idea, distinguish
review from authorized editing. A review-only order produces findings without
writing a ledger or modifying the artifact. For authorized revisions:

1. Read the artifact completely before asking.
2. Re-read it from disk before every edit because the user may have changed it.
3. Apply each settled answer immediately instead of hoarding edits for a final
   batch.
4. Record what changed and which decision caused it.
5. Delete or rewrite invalidated sections rather than preserving contradictory
   leftovers for sentimental reasons.

The artifact rotates as understanding changes. The interview is not merely a
conversation whose conclusions evaporate at closing time.

## The fog smoker

When an effort is too large to hold in one session, do not pretend every
question is already sharp.

1. Name the destination and scope boundary.
2. Grill breadth-first to reveal the nearest decisions.
3. Put sharp, answerable questions on the frontier.
4. Put important but still unformable uncertainty in the `Fog bank`.
5. Delegate independent research patches in parallel.
6. After each resolution, graduate newly sharp fog into frontier nodes.
7. Move anything beyond the destination into `Out of kitchen`, not back into
   fog.

Keep large efforts centered on the current destination. Resolve its ready
decisions within the user's chosen service and authority; do not impose an
arbitrary one-decision-per-session stop. The output is a clearer route; a map
or a planning-only request does not authorize implementation.

## Reverse searing

Re-open a settled node only when:

- new evidence contradicts it;
- a downstream answer changes its prerequisites;
- the written artifact implements it ambiguously;
- code and vocabulary disagree;
- a heat-required lens reveals a concrete new counterexample; or
- the user asks for another pass.

Name the new lens and why the earlier answer is no longer sufficient. Never
repeat an identical question solely to consume time.

## Completion gate

The inquisition ends only when:

- the frontier is empty;
- every remaining fog item is explicitly deferred or out of scope;
- artifacts reflect settled decisions;
- no important term is still overloaded; and
- shared understanding is confirmed, already established by the request, or
  resolved within explicit delegated authority.

Deliver the route's requested result. Unresolved decisions outside delegated
authority remain explicit uncertainties; they never silently authorize a build.
