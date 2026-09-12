# Taste Before Testimony

Use this protocol for an empirical uncertainty about logic, a UI, a technical
boundary, or feasibility. The probe exists to learn one bounded thing. It is
disposable unless the user separately authorizes production work. Link its
question and record through [Ingredient traceability](traceability.md): goal
`G-*`, assumption `A-*`, decision `D-*`, requirement `R-*`, task `T-*`, and
observed evidence `E-*`.

## Start with a question, not a feature

Write one question that observation can answer. State the smallest prototype
needed, its boundary, and a falsifiable prediction before building it:

> `A-07`: Importing the same list twice does not duplicate its items.
> Prediction: starting from three items, replaying the same import twice leaves
> exactly three items; the current importer is the baseline.

Name the baseline or comparison. It may be current behavior, a minimal stub,
an established implementation, or a second disposable variation. Define the
same inputs, environment, user scenario, measurement, and success/failure
threshold for both sides. If no meaningful observation can be made, do
analysis instead; a prototype that only expresses confidence is decorative
toothpicks.

## Build the smallest edible sample

Keep scope to the question: throwaway fixtures, a local mock, a narrow branch,
or a temporary screen are all acceptable when authorized. Mark simulated data,
manual observation, and untested integration boundaries clearly. Do not turn
the probe into a production feature, alter unrelated behavior, create external
records, or infer authorization from the experiment.

For a logic or technical probe, run the proposed input through the baseline and
candidate, then retain commands, output, environment details, and failures.
For a UI probe, use the same task script, state, device or viewport, and
accessibility route for baseline and candidate; retain screenshots or a concise
step trace. For a user scenario, state who observed it and the sample limits.
No result is stronger than its setup.

## Taste, record, and decide

Record a short result card:

| Field | Record |
| --- | --- |
| Question and prediction | The `A-*` claim and what would falsify it |
| Baseline and candidate | Exact comparison and shared scenario |
| Observations | Measurements, traces, raw outputs, or screenshots as `E-*` |
| Verdict | Supported, disproved, inconclusive, or blocked |
| Limits | Sample, simulation, confounders, failures, and what was not tested |
| Consequence | Which `D-*` or `R-*` is now supported, reopened, or still deferred |

Use “supported” rather than “proved” when the sample is narrow. A negative or
inconclusive result is a successful experiment when it rules out a premise.
If it disproves an assumption, mark that `A-*` accordingly and use Ingredient
Recall to mark only its dependents stale. Preserve the failed sample and its
evidence; it prevents a future committee from confidently rediscovering the
same burnt crostini.

## End the experiment

Dispose of or clearly quarantine the prototype according to its authorized
workspace rules, then state whether it was removed, retained as evidence, or
promoted by a separate authorized build decision. End when the prediction has
been tested and the result card is complete, even when the answer is “we do not
know yet.” Production scope, releases, commits, deployments, and external
operations require their own authorization.

A natural-language stop, cancel, or pause has priority over this ceremony.
Stop new runs and dispatches immediately. “You decide” instead permits
continuing within the explicitly delegated, reversible decision scope; it does not make a probe
approve itself or grant outside authority.
