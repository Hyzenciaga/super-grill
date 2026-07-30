# Grill Levels

Select the heat once at the start. Increase or decrease it only after the user
agrees. Every mode asks one decision question at a time.

## Mode matrix

| Heat | Intended experience | Required passes | Implementation gates | Exit behavior |
| --- | --- | --- | --- | --- |
| `medium-rare` | You may still remember why you opened the terminal | One pass over intent, alternatives, design, plan, pre-mortem, and final verification | Verify each task; re-grill only changed assumptions | Stop when all gates pass or the user says `take it off the grill` |
| `well-done` | Default; project managers begin to feel seen | Two passes over each major artifact: constructive, then adversarial | Re-grill every task after verification; two whole-result review lenses | Require final goal replay and user confirmation |
| `charcoal` | Requirements and soot become indistinguishable | Three passes: author, skeptic, disaster; cover every lens below | Re-grill before and after every task; review spec compliance, quality, and operations separately | Require two consecutive passes with no material new issue |
| `eternal-flame` | Continue until the heat death of the universe or the exit phrase, whichever passes review first | Run the charcoal cycle, then restart from the original goal whenever an artifact or implementation changes | Re-open every affected branch after every task and review | Continue until the exact phrase `take it off the grill`; summarize every 10 questions and remind the user of the exit phrase |

`eternal-flame` is not permission to loop without progress. Do not repeat an
unchanged question. If the frontier is empty, replay the original goal through
the lenses below and look for contradictions between artifacts. If that also
produces nothing new, report that the grill is producing no new information,
then wait for either a new decision or the exit phrase.

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

Mode coverage:

- `medium-rare`: lenses 1–5, plus any clearly relevant later lens.
- `well-done`: lenses 1–8 and 9–10 for implementation work.
- `charcoal`: all twelve lenses.
- `eternal-flame`: all twelve, then replay them against cross-artifact
  contradictions and new evidence.

## Pass personalities

Use these as analytical stances, not fake people:

- **Constructive chef:** Make the chosen approach coherent and buildable.
- **Skeptical diner:** Search for ambiguity, unsupported claims, and stronger
  alternatives.
- **Fire marshal:** Assume failure, abuse, operational surprise, and rollback.
- **Future maintainer:** Check names, rationale, interfaces, and long-term
  comprehensibility.

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
- A completed `charcoal` cycle qualifies as a Full Stack Barbecue.
- `eternal-flame` has no numeric temperature because legal advised against it.
