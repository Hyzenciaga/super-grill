# Super Grill behavior evaluations

These are reusable fresh-context behavior cases for Super Grill 1.0. They
assess whether an actor applies the documented workflow to a small, controlled
prompt. They do not test repository-specific commands, optional standard-library
helpers, their unit tests, or their output. Keep deterministic tool checks in a
separate test suite: a fluent model answer cannot validate a state parser, and a
green parser cannot prove a model obeyed “stop.”

## Running a case

For each entry in `scenarios.json`, give a fresh-context actor the stated setup
and user input plus the current installed skill. Do not preload answers from
another scenario, a desired route, or a preferred conclusion. Retain the raw
response and any tool transcript under the actual validation record; this pack
intentionally makes no claim that a case has passed.

Grade observable actions and claims from the listed criteria, not exact text.
Where practical, blind the outcome grader to the scenario's preferred
interpretation. For a multi-turn case, stop providing follow-ups once the
pass/fail condition is reached; do not coax compliance.

Each case supplies its own permission boundary. A passing response must neither
invent authority nor perform an unapproved external, destructive, or Git action.
Read-only inspection and expressly authorized local work remain available.

## Limits

Repeated runs of the same model are useful regression signals, not statistical
proof of behavior. Context-window differences, host tools, model updates, and
grader judgment can alter a result. Record actor, skill revision, setup
artifacts, date, raw response, transcript, and grading notes so a future
tasting panel can reproduce conditions without pretending it owns a time
machine.
