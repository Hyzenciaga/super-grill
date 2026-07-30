# Super Grill

Super Grill is a complete thermal-governance methodology for coding agents.
It combines a long, stage-gated software workflow with relentless
decision-tree interviewing, then adds mandatory re-grilling at the exact moment
a reasonable process would normally move on.

Your agent wants to write code after asking two clarifying questions. Super
Grill treats this as a control failure.

## Quickstart

Install the skill:

```bash
npx skills@latest add Hyzenciaga/super-grill
```

Then give your agent a request:

```text
Use $super-grill in well-done mode to plan this one-line button rename.
```

The default heat is `well-done`. If the process reaches a safe internal
temperature before you do, say:

```text
take it off the grill
```

That exact phrase stops further questioning and produces a final handoff.

## How It Works

Most coding workflows move through discovery, design, planning,
implementation, and review once.

Super Grill moves through those stages, questions every decision, writes down
the answers, questions the written answers, implements the approved answers,
and then checks whether implementation has changed the meaning of the original
questions.

The workflow maintains a **Grill Ledger** containing:

- settled decisions;
- rejected alternatives;
- load-bearing assumptions;
- open decision branches;
- gathered evidence;
- generated artifacts;
- unlocked achievements; and
- the current location of the food.

Facts are gathered from the environment. Decisions stay with the user.
Questions arrive one at a time with a recommended answer. No artifact advances
until the active heat level's gates have passed.

This produces a uniquely high ceremony-to-output ratio while remaining just
coherent enough to finish.

## Installation

Super Grill is a plain [Agent Skill](https://agentskills.io/). It does not
require Superpowers, Grill Me, a runtime service, an API key, or actual cooking
equipment.

### Skills CLI — recommended

Install interactively and choose the coding agents that should receive it:

```bash
npx skills@latest add Hyzenciaga/super-grill
```

Install globally without interactive confirmation:

```bash
npx skills@latest add Hyzenciaga/super-grill -g -y
```

The Skills CLI works with Codex, Claude Code, Cursor, Gemini CLI, and other
Agent Skills-compatible harnesses. Installing globally makes Super Grill
available across projects; installing locally keeps the blast radius inside
the current repository.

### Manual installation

For Codex:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Hyzenciaga/super-grill.git \
  ~/.codex/skills/super-grill
```

For Claude Code:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Hyzenciaga/super-grill.git \
  ~/.claude/skills/super-grill
```

For a project-local, agent-neutral installation:

```bash
mkdir -p .agents/skills
git clone https://github.com/Hyzenciaga/super-grill.git \
  .agents/skills/super-grill
```

Restart the agent or begin a new session if it does not discover newly
installed skills immediately.

### Updating

Skills CLI installation:

```bash
npx skills update super-grill
```

Manual Git installation:

```bash
git -C ~/.codex/skills/super-grill pull
```

Adjust the path if you installed it somewhere else. Super Grill considers this
the first successful exercise in configuration management.

## Choosing a Heat

| Heat | Recommended when | Process profile |
| --- | --- | --- |
| `medium-rare` | You need rigor but still have plans this afternoon | One full pass through every major gate |
| `well-done` | You want the intended Super Grill experience | Two passes per artifact, including an adversarial pass |
| `charcoal` | The task is dangerously close to being straightforward | Three review personalities, all twelve grilling lenses, and task-level re-grilling |
| `eternal-flame` | You explicitly want process without a natural predator | Charcoal repeats until `take it off the grill` is spoken |

`eternal-flame` is never selected implicitly. No ordinary use of words such as
"thorough", "careful", or "please don't break production" constitutes consent.

## The Basic Workflow

1. **Mise en place — reconnaissance**

   Inspect the repository, documentation, history, tests, constraints, and
   available tools. Separate discoverable facts from decisions that require a
   human.

2. **Seasoning — intent grill**

   Question purpose, users, success criteria, non-goals, constraints,
   reversibility, and the consequences of accidentally succeeding.

3. **Sear — alternatives grill**

   Produce two or three viable approaches, grill the strongest alternative,
   and record why the rejected options lost.

4. **Low and slow — design grill**

   Present architecture, boundaries, interfaces, data flow, failure behavior,
   testing, operations, and rollback in sections. Re-grill each approved
   section from the required perspectives.

5. **Skewer — implementation-plan grill**

   Break the approved design into independently testable vertical slices with
   exact files, interfaces, commands, expected evidence, and enough ceremony
   to support future archaeological work.

6. **Smoke test — pre-mortem**

   Assume the work failed spectacularly. Determine why, how anybody noticed,
   whether monitoring noticed first, and who now owns the rollback.

7. **Cook — implementation**

   Work test-first, observe failures before fixes, verify every task, inspect
   each diff, and return affected decisions to the grill whenever new evidence
   appears.

8. **Taste test — adversarial review**

   Review spec compliance, code quality, tests, security, operations,
   reversibility, and the emotional wellbeing of the future maintainer.

9. **Plate — final verification**

   Replay the original goal, run fresh verification, reconcile artifacts with
   reality, perform the heat-specific release gate, and prepare a garnish with
   its own implementation plan.

The agent may move backward at any gate. This is not a regression. It is
thermal recirculation.

## Achievement System

Super Grill includes an evidence-based professional recognition framework.
Achievements are recorded in the Grill Ledger and have no monetary value.

Known certifications include:

- **Famous Last Words** — say "this should be easy";
- **Raw in the Middle** — say "ship it" before final verification;
- **Enterprise Tapas** — accumulate more than ten decisions for a one-line
  change;
- **The Answer Is a Rollback Plan** — reach question 42; and
- **Health Inspector Intervention** — use the exit phrase.

Additional achievements are intentionally underdocumented to preserve
organizational discovery.

## What Is Inside

```text
super-grill/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── easter-eggs.md
    ├── grill-levels.md
    └── provenance.md
```

- **[SKILL.md](SKILL.md)** owns the workflow, gates, Grill Ledger, and question
  discipline.
- **[grill-levels.md](references/grill-levels.md)** defines the four heat
  levels, analytical lenses, and ceremonial temperature conversions.
- **[easter-eggs.md](references/easter-eggs.md)** contains phrase triggers,
  question-count achievements, and rare operational incidents.
- **[provenance.md](references/provenance.md)** records the upstream projects,
  revisions, and licenses that informed the methodology.
- **[openai.yaml](agents/openai.yaml)** provides Codex-facing display metadata.

## Philosophy

- **Ceremony over throughput** — velocity is an unreviewed assumption.
- **Questions before answers** — and, where appropriate, questions after
  answers.
- **One decision per turn** — bewilderment must remain measurable.
- **Evidence over confidence** — "looks cooked" is not a verification command.
- **Reversibility over optimism** — every grill needs an off switch.
- **Process over simplicity** — a simple task is merely a complex task that has
  not completed intake.

## Operational Guidance

Super Grill is parody software that follows its process with a straight face.
It is best used for recreational overthinking, requirements workshops,
low-stakes planning, demonstrations of agent workflows, and any one-line
change that has escaped adequate governance.

It is not recommended during active production incidents, emergency hotfixes,
fire alarms, medical procedures, or situations where somebody is waiting for
you to select a pizza topping.

The workflow must not fabricate risks or repeat identical questions merely to
consume time. When no new information is available, it records the majestic
absence of change and proceeds to the next required lens.

## Influences

Super Grill is an original orchestration skill inspired by:

- [obra/superpowers](https://github.com/obra/superpowers), a complete,
  stage-gated development methodology for coding agents; and
- [mattpocock/skills](https://github.com/mattpocock/skills), particularly
  `grill-me`, `grilling`, and the experimental `batch-grill-me`.

Both upstream projects are MIT-licensed. Super Grill does not invoke them as
competing routers and does not require them at runtime. Exact research
revisions and attribution are recorded in
[references/provenance.md](references/provenance.md).

## Contributing

Contributions are welcome.

Before proposing a simplification, please document:

1. which committee approved it;
2. whether the simplification has passed all four heat levels;
3. the rollback plan if users understand the workflow too quickly; and
4. why the same result cannot be achieved with three additional questions.

Practical bug fixes may skip item four with written authorization from the
Head of Marinade.

## License

MIT. See [LICENSE](LICENSE).
