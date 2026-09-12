# Super Grill 1.0 validation record

This records observations from the 1.0 upgrade, not a promise that every model or
host will behave identically. The source base was `80eef24` (0.2.0); the candidate
is the local 1.0.0 working tree. Publication was not requested or performed.

## What was exercised

- Real Python helper integration tests run in disposable Git repositories.
- The bundled official skill frontmatter validator, using PyYAML in a temporary
  environment; the skill and its optional helpers do not require PyYAML.
- Claude Code plugin and marketplace manifest validators.
- Local Markdown links, JSON examples/eval cases, and whitespace checks.
- Fresh-context GPT-5.6 Terra actors, each receiving the skill plus a bounded user
  request; the coordinator inspected outcomes and actual generated artifacts.
- An independent Terra review of the upgrade and a focused helper follow-up.

The actor contexts did not receive prior conclusions or desired answers. The
coordinator graded outcomes against the upgrade contract, so grading was not
fully blinded. The first six probes were run against the evolving candidate;
relevant refinements and reruns are called out below rather than hidden behind
an invented immutable release test ID. Raw responses and retained fixtures are
linked under `evals/results/`.

## Observed behavior

| Probe | Observation | Evidence |
| --- | --- | --- |
| Delegated analysis, 0.2 baseline | FAILED the new requirement: asked for confirmation despite “do not ask; decide the details” | [Raw baseline](../evals/results/analysis-baseline.md) |
| Same request, 1.0 | Delivered analysis without a question or write; distinguished design from implementation/testing | [Raw candidate](../evals/results/analysis-v1.md) |
| Chinese stop during eternal flame | Stopped questioning, summarized settled/unresolved matters, did not demand English password | [Raw response](../evals/results/stop-v1.md) |
| Already-authorized solo build | Fixed actual code, 3 tests passed, no commit, preserved unrelated dirty note, labeled self-review | [Response and coordinator verification](../evals/results/solo-build-v1.md) |
| Disposable import experiment | Ran real baseline/candidate comparison (6 versus 3 items on replay), kept limits and source fixtures intact | [Response, artifacts and rerun](../evals/results/experiment-v1.md) |

| Review-only artifact | Found both supplied contradictions without editing; severity labels were stronger than the demonstrated impact | [Response and retained input](../evals/results/artifact-v1.md) |
| Stale-ledger recovery | Checked current files, Git and tests; recognized completed work without duplicate dispatch or invented worker-handle access | [Raw recovery](../evals/results/recovery-v1.md) |
| Recall and sequential comparison | Correctly recalled only the dependent chain and disclosed sequential provenance; technical comparison overstated the equivalence of different repairs | [Imperfect result and critique](../evals/results/recall-blind-initial.md) |
| Independent alternative generation | Two fresh contexts produced distinct minimal and preview/recovery designs against the same import scenarios; coordinator compared their scope and costs | [Brief contract and both responses](../evals/results/blind-independent-v1.md) |

The sequential comparison prompted explicit per-option repair cards and
original-to-original / repaired-to-repaired comparison rules. Subsequent bounded
reruns still showed technical overstatement; no claim is made that the instruction
change solved design bias. Their full raw responses were not retained in this
checkout, so they are a limitation of this evaluation record, not reproducible
passing cases. The independent import alternatives demonstrate separate brief
provenance and reasoned scenario traces, not executable correctness or an unbiased
final judge. Recovery exercised a missing handle, not a live-process timeout.

## Deterministic checks and independent review

[Command outputs and source fingerprints](../evals/results/tool-checks.json)
record all six checks with exit code 0:

- Python integration suite: **11 tests passed**, including invalid graphs,
  transitive recall, preservation on rejected writes, staged/unstaged/untracked
  snapshots, unborn repositories, changing directory scopes and evidence drift.
- Official skill frontmatter validation: `Skill is valid!`.
- Claude Code plugin manifest and marketplace validation: both passed.
- `git diff --check`: passed.
- The seven-node recall example: valid under its explicit run/plan identity.

The independent reviewer found two defects after an earlier nine-test suite
passed: complete deletion of a selected directory broke packaging, and an
unexpected file in the readable review tree escaped verification. Both were
fixed and covered by regression tests. The reviewer reran both reproductions,
also checked an injected empty directory, and issued spec and quality passes
for the revised helper scope. See [review and corrections](../evals/results/review-v1.md).
After documentation closeout, the same independent reviewer audited R1–R10
against the final package and issued whole-upgrade spec and quality passes,
with no material actionable gaps; its response is retained in that record.

Local documentation links, JSON parsing, packaging version/default consistency
and the recorded source fingerprints were checked again at closeout
([machine-readable result](../evals/results/closeout-checks.json)). Historical
absolute links in raw actor responses identify disposable fixtures; retained
copies are linked beside those responses. No live service, global skill install,
remote Git action or publication was exercised.

## Acceptance coverage

| Requirement | Delivered coverage and actual evidence |
| --- | --- |
| R1: routes | Main route/terminal table; actual analysis, artifact, experiment and build probes above |
| R2: stop and authority | Main and heat protocols; baseline/candidate delegation comparison, Chinese stop and preapproved solo build |
| R3: recall | Trace manual, graph helper and example; automated transitive/isolation checks and actor recall |
| R4: alternatives | Blind-tasting manual; two independent entrants plus explicitly imperfect sequential comparison |
| R5: empirical probes | Taste-test manual; executed import baseline/candidate and retained observations |
| R6: recovery | Execution/trace identity and live-handle rules; graph identity checks and stale-ledger recovery; live timeout behavior remains untested |
| R7: review evidence | Snapshot/package/verify helper; Git-layer, preservation, directory-transition and drift integration tests; independent defect reproduction and re-review |
| R8: solo fallback | Main/execution protocols; real solo build with two honest self-review verdicts |
| R9: original mechanisms | Main twelve stations and revised menu, recipe, kitchen, food-safety and heat manuals preserve decision trees, language/cards, plans, TDD/debugging, review/fix loops and authorized disposition; build probe exercises a bounded subset |
| R10: delivery | README, 1.0.0 manifest and UI defaults, eleven reusable scenario cases, retained observations, tool validation and this record |

## Interpretation

These bounded probes demonstrate particular behaviors; they do not establish a
statistical success rate. The reusable [scenario pack](../evals/scenarios.json)
contains more variants than any single smoke run. Read-only analysis is not an
experiment; sequential viewpoints are not independent design sources; a graph
validator is not a business-correctness or authorization verifier. No claim is
made that every scenario in the pack was executed verbatim.

The local upgrade meets its implementation contract with the limits above.
Protocol compliance, analytical accuracy and user experience are separate claims:
the current evidence supports particular scope/recovery behaviors and tested
helper transitions, while comparative reasoning, severity calibration and broader
multi-turn reliability warrant further evaluation.
