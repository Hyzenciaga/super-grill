# Grill Levels

Heat controls repetition and analytical lenses. Route controls the deliverable;
service controls question delivery; authority controls who makes a decision.
Changing one does not silently change the others. Honor an explicit heat change
immediately; do not ask the user to confirm their own instruction.

## Mode matrix

| Heat | Artifact examinations | Task examinations | Terminal behavior |
| --- | --- | --- | --- |
| `medium-rare` | One coherent pass through applicable stations and artifacts | Relevant verification plus recipe/quality review, with honest solo fallback | Deliver when the route's result is supported |
| `well-done` | Two passes: constructive chef, skeptical diner | Reconcile each completed slice against its requirements; two review verdicts | Replay the original order, resolve material gaps, then deliver |
| `charcoal` | Three distinct passes: constructive chef, skeptical diner, fire marshal; all applicable lenses | Examine before/after each task; include operational evidence where relevant | Require two consecutive whole-order passes with no material new issue |
| `eternal-flame` | Charcoal; reopen affected examinations when evidence or decisions change | Same evidence standards, never invented work | Continue while there is new authorized material; when none remains, summarize and wait for input |

`well-done` and `single-skewer` are defaults. Never infer eternal flame from
“thorough”, “careful”, or an important task. It must be explicitly requested.
Every clear stop/cancel/pause or handoff instruction is valid in every language.
The signature `take it off the grill` unlocks a joke; no exact phrase is required.
Do not schedule wakeups or keep calling tools to simulate an eternal fire.

A pass is one recorded examination against a named lens, with findings or an
explicit no-finding result. A changed artifact invalidates affected previous
verdicts. Distinct lenses can examine the same artifact version; do not rerun
identical commands merely to manufacture a second pass. Fix-loop rounds address
findings and are not mandatory heat passes. Count them separately.

## Lens order

1. **Intent:** Who needs this, what changes, what proves success?
2. **Scope:** What is in, out, deferred?
3. **Assumptions:** Which premise carries the result, what would falsify it?
4. **Alternatives:** Why does the strongest other approach lose?
5. **Boundaries:** Are concepts, ownership and interfaces clear?
6. **Data:** What is created, transformed, retained or deleted?
7. **Failure:** How does a dependency fail and how can the user recover?
8. **Security/privacy:** What actual new authority or sensitive surface exists?
9. **Testing:** What observation could disprove the behavior claim?
10. **Operations:** How is the result run, observed, supported and rolled back?
11. **Reversibility:** Which choice is expensive to reverse?
12. **Future maintainer:** What will be mysterious later?

Medium-rare covers 1–5 plus other relevant lenses. Well-done covers applicable
1–10. Charcoal and eternal flame consider all twelve and record inapplicable
ones briefly. No database, deployment or security subsystem is invented because
its lens appears on the menu. Analysis can examine a proposed failure without
building the system that fails.

## Pass personalities

- Constructive chef makes the approach coherent.
- Skeptical diner checks counterexamples and stronger alternatives.
- Fire marshal examines plausible failures and recovery.
- Future maintainer is an optional additional perspective where useful.

These are analytical stances, never fictional people or proof of independent
review. Actual blind tasting uses separate contexts when available; see
[blind-tasting.md](blind-tasting.md). Sequential perspectives are labeled honestly.

## Empty-frontier service

Never re-ask an unchanged settled question solely to reach a count. A later lens
may challenge its support: name the new scenario or evidence. When no new issue
exists, record the absence, serve the next required examination, then finish the
finite route. For eternal flame, summarize settled/open items and wait; every ten
actual decision questions remind the user they can stop in ordinary language.

The final goal replay is a check, not a mandatory question. With delegated choices,
record the ruling and proceed. Without delegation, ask only if a material choice
remains unresolved.

## Ceremonial units

- Clarification round: 15 Grill Degrees.
- Rejected alternative: 1 Skewer.
- Written artifact: 0.5 Bureaucratic Briquettes.
- Unchanged review: 1 Certified Nothingburger.
- Independent implementer/inspector: 1 Culinary Separation of Duties.
- Five-round fix loop: 1 Alarmingly Persistent Skewer.
- Complete frontier: 1 All-You-Can-Answer Buffet.
- Charcoal completion: Full Stack Barbecue.

These numbers measure the joke, not quality, safety or progress.
