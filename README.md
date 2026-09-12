# Super Grill

Super Grill combines Superpowers and Grill Me into one advanced skill—a complete
development workflow that questions every decision from idea to completion.

Your agent wants to write code after asking two clarifying questions. Super Grill
has already convened the Committee for the Approval of Clarifying Questions.

![Superpowers writes a twelve-stage plan, Grill Me asks forty-two questions, and Super Grill does both to rename one button.](assets/super-grill-comparison.png)

## What's new in 1.0

The committee now interrogates its own evidence.

- **Ingredient Recall:** trace goals, assumptions, decisions, requirements,
  tasks and evidence. A changed premise recalls its dependents while unrelated
  work stays approved. The typography remains legally edible.
- **Kitchen Blind Tasting:** produce alternatives from separate briefs, compare
  the same scenarios, and preserve the strongest losing argument. Sequential
  fallback is labeled honestly; three hats do not create three employees.
- **Taste Before Testimony:** settle an empirical question with a disposable
  prototype, a prediction, a baseline and an observed verdict. An inconclusive
  experiment is allowed to be inconclusive in writing.
- **Four routes, four heats:** ideas, documents, experiments and builds have
  distinct endpoints. A planning order can be charcoal without accidentally
  becoming a software project.
- **Evidence that survives the kitchen:** optional local tools validate trace
  graphs, recall dependencies, and package committed, staged, unstaged and new
  files for review. Run identity and current snapshots guide resumption.
- **An actual off switch:** ordinary stop requests work in any language.
  “You decide” delegates the stated choices. The bureaucracy has reluctantly
  acknowledged the existence of its customer.

This remains a deliberately excessive, self-contained Agent Skill. The requested
result is still owed; the spectacle is in how it gets there.

## Quickstart

Install from the published repository:

```bash
npx skills@latest add Hyzenciaga/super-grill
```

Then ask:

```text
Use $super-grill in well-done mode to plan this one-line button rename.
```

Or grill an idea without making it a build:

```text
Use $super-grill to analyze my offline shopping-list idea. Analysis only.
You decide the small details; give me the conclusion without questions.
```

Defaults are `well-done` and `single-skewer`. Say `take it off the grill`,
“stop and summarize”, or “别问了，先总结” to end the questioning. No password,
minimum question count or final confirmation is required.

## Order the dish, then choose the heat

The agent infers the route from your requested result:

| Route | You order | You receive |
| --- | --- | --- |
| `analysis` | Stress-test an idea or write a plan | Findings, decisions, uncertainties and recommendation/plan |
| `artifact` | Review or revise a document or code artifact | Findings; edits only when requested |
| `experiment` | Find out whether something works or feels right | A bounded probe, observed result and limitations |
| `build` | Implement the change | Working result, verification, review and authorized delivery |

Heat changes the examination depth, not the scope:

| Heat | The ceremony |
| --- | --- |
| `medium-rare` | One complete applicable pass; you may still have an afternoon |
| `well-done` | Constructive and skeptical examinations; the house experience |
| `charcoal` | Three perspectives, all relevant lenses, two clean whole-order passes |
| `eternal-flame` | Charcoal continues with new material; an empty frontier waits for you |

`eternal-flame` is explicitly ordered, never inferred from “be thorough”. It does
not create background jobs or invent busywork when the evidence stops changing.

Question delivery is separate: `single-skewer` asks one decision at a time;
explicit `frontier-buffet` serves all currently independent decisions together.
Facts are investigated by the agent. Previously answered decisions stay answered.
Explicitly delegated choices get a recorded ruling, not another approval request.

## The twelve-station tasting menu

1. **Seat the Party:** investigate the actual environment and original order.
2. **Menu Inquisition:** work a dependency-aware decision tree and resolve language.
3. **Flight of Competing Sauces:** compare alternatives, with blind tasting when useful.
4. **Architectural Dry Rub:** examine behavior, boundaries, failure and recovery.
5. **Recipe Deposition:** cross-examine the specification and its assumptions.
6. **Skewer Bureaucracy:** plan testable slices with clear interfaces and evidence.
7. **Kitchen Quarantine:** identify existing work and establish a relevant baseline.
8. **Sous-Chef Conveyor Belt:** execute with scoped agents or an honest solo route.
9. **Smoke Autopsy:** reproduce failures and test a root-cause hypothesis.
10. **Health Inspector Carousel:** produce recipe and quality verdicts; fix real defects.
11. **Thermometer Court:** match completion claims to current evidence.
12. **Closing-Time Tribunal:** deliver the ordered result and authorized next state.

Only stations relevant to the route apply. A document review does not require a
Git worktree; an analysis does not owe a pretend failing unit test. A changed
assumption can return affected work to an earlier station. This is thermal
recirculation, now with a traceable recall notice.

## From assumption to evidence

A typical Ingredient Recall might look like this:

```text
A-01: one device edits the list
  └─ D-01: overwrite the latest saved list
      └─ R-01: local whole-list persistence
          └─ T-01: implement saving
              └─ E-01: single-device restart test passes
```

Now a second device appears. The agent marks the dependent decision, requirement,
task and evidence stale, preserves their history, and checks what remains valid.
The test result still happened; it never established two-device correctness.
An unrelated typography task stays settled.

For short/read-only work, the ledger stays in conversation. Authorized durable
artifacts live under `docs/super-grill/<run-id>/` or your chosen location. See the
[illustrative ledger](examples/ingredient-recall/ledger.md) and
[machine-readable example](examples/ingredient-recall/state.json).

## Optional local evidence tools

The skill works without scripts. If Python 3 and Git are available, the bundled
helpers make structural and snapshot checks reproducible. They use the Python
standard library and do not call a network or change Git state.

Run these from this skill's directory. Try a recall on a temporary copy:

```bash
grill_demo=$(mktemp -d)
cp examples/ingredient-recall/state.json "$grill_demo/state.json"
python3 scripts/state_graph.py validate "$grill_demo/state.json" --run-id demo-recall --plan-id demo-plan
python3 scripts/state_graph.py recall "$grill_demo/state.json" --run-id demo-recall --plan-id demo-plan --changed A-01 --reason 'A second device can edit'
```

Capture task paths **before** execution, package them after, and check whether a
review still matches current files. Use new output directories outside the target
repository. Replace the example paths with the actual task scope:

```bash
python3 scripts/review_evidence.py capture --repo /path/to/project --output /tmp/grill-before --path src --path tests
python3 scripts/review_evidence.py package --repo /path/to/project --baseline /tmp/grill-before --output /tmp/grill-review --path src --path tests
python3 scripts/review_evidence.py verify --repo /path/to/project --package /tmp/grill-review --path src --path tests
```

Select relevant files/directories; do not include credential or private-data
paths. The package distinguishes pre-existing dirty paths from changes observed
since capture. It cannot determine which human/agent authored an overlapping edit.
The graph checker validates identity and dependency structure, not approval or
business correctness. Full contracts: [traceability](references/traceability.md)
and [kitchen operations](references/kitchen-industrial-complex.md).

## Installation and updating

Super Grill requires neither upstream skill at runtime, nor a server, API key,
external tracker, subagent facility, or actual cooking equipment.

[Skills CLI](https://github.com/vercel-labs/skills) supports compatible clients
including Codex and Claude Code. For a global noninteractive install:

```bash
npx skills@latest add Hyzenciaga/super-grill -g -y
```

For a checkout you are developing, use `npx skills@latest add .` from its root;
this installs that local checkout rather than the last published repository state.

Claude Code's native plugin installation is also supported:

```text
/plugin marketplace add Hyzenciaga/super-grill
/plugin install super-grill@super-grill
```

Update through the installer you used:

```bash
npx skills update super-grill
```

```text
/plugin update super-grill@super-grill
```

Start a new session if your client has cached the old kitchen manual. Upgrading
from 0.2 does not rewrite old ledgers automatically: reconcile the old record and
current files, assign run/plan identity, and add trace links only where meaningful.
Never infer task completion or delegated authority from missing migration fields.

## What's inside

- [SKILL.md](SKILL.md): routes, authority, stop behavior and station routing.
- [references/](references/): heat, questioning, traceability, blind tasting,
  prototypes, design/plans, execution, verification and achievements.
- [scripts/](scripts/): optional trace graph and review evidence helpers.
- [tests/](tests/): executable helper tests using disposable Git repositories.
- [evals/](evals/README.md): reusable behavior scenarios and validation method.
- [docs/upgrade-v1.md](docs/upgrade-v1.md): this upgrade's acceptance contract.
- [docs/validation-v1.md](docs/validation-v1.md): actual validation outcomes and limits.
- [.claude-plugin/](.claude-plugin/), [agents/openai.yaml](agents/openai.yaml): packaging and UI metadata.

Run helper tests with:

```bash
python3 -m unittest discover -s tests -v
```

Passing file validation is not proof of good agent behavior. The behavioral suite
checks observable actions such as respecting analysis scope, stopping in Chinese,
preserving authority, reporting honest review limits and resuming actual work.

For 1.0, all **11 helper tests** passed, as did the skill frontmatter and Claude
Code plugin/marketplace validators. Fresh-context actors exercised all four
routes, cancellation, recall, recovery and independent alternative generation.
An independent final review passed the upgrade's ten acceptance requirements.

The **11 reusable behavior scenarios** are a separate evaluation pack; not every
case was run verbatim. Recorded limitations include biased sequential design
comparisons, severity overstatement and untested live-worker timeout recovery.
See the [validation record](docs/validation-v1.md) for actual results, source
fingerprints and retained examples. The committee has published its own inspection
report, including the parts it would have preferred to season more heavily.

## Professional recognitions

The Grill Ledger awards evidence-based certifications with no monetary value:

- **Enterprise Tapas:** more than ten decisions for a one-line change.
- **Sauce Schism:** independent designs expose a meaningful disagreement.
- **Hypothesis, Tenderized:** a prototype disproves its own prediction.
- **Mise en Place Recovered:** resumption reconciles real progress without duplication.
- **Lonely Michelin Star:** self-review is accurately labeled as self-review.
- **Health Inspector Intervention:** the diner has exercised the right to leave.

More [achievements](references/easter-eggs.md) await discovery. None authorizes a
file write, release, extra agent, or risk invented to keep the committee occupied.

## Influences and philosophy

Inspired by [obra/superpowers](https://github.com/obra/superpowers) and
[mattpocock/skills](https://github.com/mattpocock/skills), both MIT-licensed.
Super Grill adapts their mechanisms locally and remains the only top-level router.

Ceremony over throughput. Evidence over confidence. Reversibility over optimism.
A simple task is merely a complex task that has not completed intake.

This is parody software, best enjoyed for recreational overthinking, requirements
workshops, workflow demonstrations and tiny changes seeking a larger organization.
The joke is the institutional excess; user consent and evidence stay literal.

## Contributing

Before proposing a simplification, document which committee approved it and the
rollback plan if users understand the workflow too quickly. Practical fixes may
skip this form when accompanied by a regression scenario.

MIT. See [LICENSE](LICENSE).
