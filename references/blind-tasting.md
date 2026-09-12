# Kitchen Blind Tasting

Use this protocol when a consequential choice has two or more viable approaches
and comparing them would change a decision. It is a fair comparison, not a
machine for manufacturing debate. Link its goal, assumptions, decision,
requirements, tasks, and evidence in [Ingredient traceability](traceability.md)
with stable IDs (for example `G-01`, `A-03`, `D-02`, `R-04`, `T-06`, `E-09`).

## Set the tasting card

Before producing alternatives, record the decision (`D-*`), the shared goal and
requirements (`G-*`, `R-*`), the testable assumptions (`A-*`), the scenario or
interface to compare, and the evidence each alternative must supply (`E-*`).
Use the same facts, constraints, budget, time limit, inputs, success criteria,
and output format for every entrant. State any unavoidable asymmetric capability
or access difference on the card.

Do not leak the coordinator's preference, a preferred implementation sketch, a
score to chase, or another entrant's draft into an entrant brief. A brief may
say “compare two error-recovery designs under these requirements”; it may not
say “make the reliable queue design win.” Each entrant works from its own fresh
brief and labels provenance honestly: independently produced, sequential
alternative, or adapted follow-up.

Useful entrant lenses include a minimal-state design, a strongest-counterproposal
design, and a failure/recovery-first design. Give each the same hard requirements
while changing its optimization lens. Choose enough genuinely different entries
to examine the trade-off; do not prescribe headcount regardless of the question.

## Produce and compare

Use independent workers only when the host has authorized delegation and has
the needed capability. Give each one a bounded read-only or isolated task,
exact constraints, evidence target, and return format. Do not give an agent an
authority the user did not delegate, ask it to contact outside systems, or call
an apparent vote an approval.

When independent work is unavailable, produce alternatives sequentially. Say so
in the record: sequential work can broaden thought but cannot certify
independence. Keep later alternatives from reading earlier drafts where the
environment allows; otherwise disclose the exposure and use a deliberate
counter-case prompt. One honest solo comparison is preferable to two fake
"independent" chefs in the same apron.

For each entry, separate the mechanism actually specified from additional
conditions needed for its claimed guarantees. Give a losing option its smallest
viable repair within the shared scope; do not assume every repair makes it the
winning architecture. Distinguish different failure properties instead of using
one attractive label as proof of all of them.

Evaluate all entries through the same comparable interface or user scenarios.
For example, run each recovery design against the same timeout, duplicate
request, and restart cases; run each UI against the same user task, viewport,
and accessibility path. Preserve raw outputs, commands, screenshots, tests, or
reasoned scenario traces as `E-*`; do not replace them with a chef's impression.

| Lens | Ask of every alternative |
| --- | --- |
| Requirement fit | Which `R-*` items does it satisfy, miss, or reinterpret? |
| User outcome | What does the same user do, see, and recover from? |
| Evidence | What was observed, simulated, inspected, or still assumed? |
| Cost and risk | What new complexity, failure mode, or authority does it require? |
| Reversibility | What is cheap to change, and what would lock in a decision? |

## Plate the verdict

Write a compact tasting report containing the card, entrant provenance,
side-by-side scenario outcomes, evidence links, and a recommendation. Include
a repair card for **each** option, with these explicit fields:

- As specified: mechanisms actually present and failure under the shared cases.
- Smallest viable repair: additional mechanism and cost, or the specific reason
  no repair fits the hard constraints.
- Repaired option: where it is viable and which uncertainty remains.

Compare original with original, then repaired with repaired. A favorite augmented
with unprovided guarantees must not compete against an unrepaired alternative.
Different protocols may satisfy the same requirement without becoming identical. Separate
facts from the coordinator's judgment. Record the selected decision as `D-*`,
why it won, and rejected alternatives with their surviving merits. The user
still owns an undelegated material choice; “you decide” records a bounded
delegation scope and permits the coordinator to choose within it.

If a premise changes, issue Ingredient Recall from the changed `A-*` or `E-*`.
Revisit only reachable decision, requirement, task, and evidence nodes. A
winning sauce does not invalidate the whole pantry.

## Stop conditions

End the tasting when the viable alternatives have comparable evidence and the
decision is made, delegated, or explicitly deferred. Do not add entrants merely
to make the bracket look televised. A plain-language stop, cancel, pause, or
“take it off the grill” ends new generation and delegation immediately; retain
the evidence and report the current state. No joke authorizes a dispatch,
approval, publication, or external operation.
