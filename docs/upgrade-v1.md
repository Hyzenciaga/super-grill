# Super Grill 1.0 — Upgrade contract

## Product intent

Preserve the knowingly excessive culinary bureaucracy, default well-done heat,
single-skewer questioning, achievements, and self-contained skill installation.
Make the ceremony interrogate evidence as well as the user. Requested output
remains an obligation; the user can stop, change the route, or delegate choices.
This upgrade is authorized for implementation and parallel GPT-5.6 Terra work.
Publication and remote Git operations are not part of this request.

## Requirements and acceptance evidence

| ID | Requirement | Evidence |
| --- | --- | --- |
| R1 | Route analysis, artifact review, experiment, and build to explicit terminal states, independently of heat and question delivery | SKILL route table; behavior scenarios |
| R2 | Plain-language stop/pause/cancel and explicit bounded decision delegation override ceremony; earlier authorization is retained | Main protocol and heat rules; behavior scenarios |
| R3 | Ingredient Recall links goals, assumptions, decisions, requirements, tasks, evidence; changes invalidate only reachable dependents | Trace reference, optional standard-library Python helper and behavioral tests |
| R4 | Kitchen Blind Tasting compares independently generated alternatives with shared constraints; report sequential fallback honestly | Blind-tasting reference and role contracts; behavior scenario |
| R5 | Taste Before Testimony runs a question-led disposable probe with falsifiable observations, then records its verdict and limits | Prototype reference; behavior scenario |
| R6 | Execution recovers by run/plan identity, current files and Git state; no duplicate task dispatch from stale ledger | Execution and trace contracts; state helper tests |
| R7 | Review covers committed, staged, unstaged and untracked task changes, distinguishes pre-existing work and flags drift | Optional review snapshot/package helper with integration tests |
| R8 | No-agent execution has an honest, passable review fallback; material findings still block completion | Main and execution protocols; behavior scenario |
| R9 | Preserve decision trees, vocabulary/cards, specs/plans, Raw-Sizzle-Rest, root-cause debugging, two verdicts, bounded fix loops and branch disposition | Coverage review of all existing references |
| R10 | Deliver usable documentation, synchronized 1.0.0 packaging, reusable behavior-evaluation cases, and an actual validation record | README, manifests, evals, validation output |

## Shared contracts

- Work routes: `analysis`, `artifact`, `experiment`, `build`.
- Heat: `medium-rare`, `well-done` (default), `charcoal`, `eternal-flame` (explicit).
- Service: `single-skewer` (default), `frontier-buffet`; decision authority is a
  separate recorded scope, not a service style.
- Durable artifacts: `docs/super-grill/<run-id>/` when repository writes are
  authorized; otherwise conversation. Respect a user-specified artifact location.
- Optional machine state: `state.json`, schema version 1, `run_id`, `plan_id`,
  and a `nodes` object keyed by node ID. Each node has `id`, `kind` (goal/assumption/decision/requirement/
  task/evidence), `summary`, `depends_on` IDs, `status`, `revision` (integer).
  Dependencies point from a dependent to its prerequisites. Recall follows the
  reverse edges, retaining history/evidence and marking dependents `stale`.
- State records support reasoning and resumption; neither approval nor business
  correctness can be inferred from a green structural validator.
- Optional scripts must use Python 3 standard library, avoid network, avoid Git
  mutations, preserve user files, and expose `--help`. Their absence must not
  prevent the skill's documented manual workflow.
- Execution and evidence are grounded in actual current file snapshots, not
  just HEAD, task labels, an old report, or a claimed independent perspective.
- Upstream mechanisms are adapted locally; do not call upstream meta-routers.
- Existing untracked promotional images are outside this upgrade.

## Implementation plan

1. Preserve the 0.2 protocol in a temporary fixture for baseline evaluation.
2. Parallel work: deterministic evidence tools and tests; blind tasting and
   prototype protocols; baseline behavioral probe. Coordinator owns core routing,
   trace/recovery integration, existing reference edits and release docs.
3. Integrate tools with actual documented commands; run focused and complete
   checks, inspect failures and fix defects.
4. Run fresh-context Terra behavior probes against the resulting skill and
   perform independent whole-upgrade review. Record observed limits honestly.
5. Audit every requirement above against final files and evidence, then report
   the delivered upgrade and any remaining limitations.
