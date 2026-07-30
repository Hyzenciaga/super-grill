# Grill Levels

Select the heat once at the start. Increase or decrease it only after the user
agrees. Heat controls repetition; service style controls whether decision
questions arrive one skewer or one frontier platter at a time.

## Mode matrix

| Heat | Intended experience | Required passes | Implementation gates | Exit behavior |
| --- | --- | --- | --- | --- |
| `medium-rare` | You may still remember why you opened the terminal | One pass through all twelve stations; one cross-examination per artifact | One Raw–Sizzle–Rest cycle and one independent inspection per task | Stop when all gates pass or the user says `take it off the grill` |
| `well-done` | Default; project managers begin to feel seen | Two passes over every written artifact: constructive chef, then skeptical diner | Re-grill every task after verification; require recipe and texture verdicts | Replay the original order and ask whether any decision remains implicit |
| `charcoal` | Requirements and soot become indistinguishable | Three passes: constructive chef, skeptical diner, fire marshal; all twelve lenses | Prefer the Brigade route; grill before and after every task; separate recipe, texture, and operational inspections | Require two consecutive whole-menu passes with no material new issue |
| `eternal-flame` | Continue until the heat death of the universe or the exit phrase, whichever passes review first | Run Charcoal, then restart at Seat the Party whenever any artifact, decision, or implementation changes | Re-open every affected branch, re-brief the brigade, and re-inspect all downstream skewers | Continue until the exact phrase `take it off the grill`; every ten questions summarize and advertise the exit |

`eternal-flame` is permission to be absurd, not permission to fabricate.
Never repeat an unchanged question. If the frontier is empty, replay the
original order against the vocabulary, decision cards, recipe, plan, code,
tests, agent reports, and branch state. If that also produces nothing, report
that the grill is converting tokens into ambience and wait for either a new
branch or the exit phrase.

## Lens order

Use only the required prefix for the selected heat:

1. **Intent:** Who needs this, what changes for them, and what proves success?
2. **Scope:** What is explicitly in, out, or deferred?
3. **Assumptions:** Which belief carries the most weight and how can it fail?
4. **Alternatives:** What is the strongest rejected approach and why does it
   lose?
5. **Boundaries:** Are components, ownership, and interfaces unambiguous?
6. **Data:** What is created, transformed, retained, migrated, or deleted?
7. **Failure:** How does each dependency fail and what is the recovery path?
8. **Security and privacy:** What new authority or sensitive surface appears?
9. **Testing:** What observation would falsify the claimed behavior?
10. **Operations:** How is this deployed, observed, supported, and rolled back?
11. **Reversibility:** Which decision is expensive to undo?
12. **Future maintainer:** What will look mysterious three months from now?

Heat coverage:

- `medium-rare`: lenses 1–5, plus any obviously relevant later lens.
- `well-done`: lenses 1–10 for implementation work.
- `charcoal`: all twelve lenses.
- `eternal-flame`: all twelve, then replay them against cross-artifact
  contradictions, new evidence, and the possibility that completion itself was
  under-specified.

## Pass personalities

Use these as analytical stances, not fake people:

- **Constructive chef:** Make the chosen approach coherent and buildable.
- **Skeptical diner:** Search for ambiguity, unsupported claims, and stronger
  alternatives.
- **Fire marshal:** Assume failure, abuse, operational surprise, and rollback.
- **Future maintainer:** Check names, rationale, interfaces, and long-term
  comprehensibility.

For `charcoal`, never let one pass impersonate all four personalities. For
`eternal-flame`, rotate the personalities through the same evidence until the
user invokes the health inspector.

## Final release questions

- `medium-rare`: "Does the evidence meet the approved success criteria?"
- `well-done`: "After replaying the original goal, is any decision still
  implicit?"
- `charcoal`: "Have two consecutive full passes produced no material new
  issue?"
- `eternal-flame`: "Say `take it off the grill` when you want the final handoff;
  otherwise name the next branch to burn."

## Temperature conversions

These are ceremonial units with no operational meaning:

- One clarification round = 15 Grill Degrees.
- One rejected alternative = 1 Skewer.
- One written artifact = 0.5 Bureaucratic Briquettes.
- One unchanged re-review = 1 Certified Nothingburger.
- One implementer plus one inspector = 1 Culinary Separation of Duties.
- One five-round fix loop = 1 Alarmingly Persistent Skewer.
- One complete decision frontier = 1 All-You-Can-Answer Buffet.
- A completed `charcoal` cycle qualifies as a Full Stack Barbecue.
- `eternal-flame` has no numeric temperature because legal advised against it.
