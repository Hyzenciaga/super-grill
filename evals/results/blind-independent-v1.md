# Independent Kitchen Blind Tasting — actual two-worker run

Actors: GPT-5.6 Terra in separate fresh contexts, `blind_candidate_minimal` and
`blind_candidate_recovery`. Both received the same shared requirements/scenarios
and were instructed not to read evals or each other's outputs. Their sole
intentional difference was the optimization lens. No favored design was supplied.
The coordinator compared their outputs after both returned; no vote was treated
as user approval and no code was executed by the entrants.

## Shared tasting card

Local offline shopping-list import. Items have stable string IDs and names.
Identical reimports produce no duplicates; same ID/different name reports a
conflict; a conflicting batch leaves the list unchanged. Preserve existing order
and append new IDs in input order. No server or database is required.

Shared cases: exact replay, conflict plus new item, entirely new IDs, missing ID.
Minimal entrant lens: minimize public interface and persistent state.
Recovery entrant lens: explain failures and support preview/retry.

## Minimal entrant response (verbatim)

**Entrant: independently produced — minimal interface/state**

**Proposed interface**

```ts
type Item = { id: string; name: string };
type ImportResult =
  | { ok: true; added: number }
  | { ok: false; error: "malformed" | "conflict"; id?: string };

class ShoppingList {
  items(): readonly Item[];
  import(items: readonly Item[]): ImportResult;
}
```

Persistent state: one ordered `Item[]`, stored locally (for example a single JSON file/local-storage value). `id` is the sole identity key; no server/database.

`import` validates and prepares a prospective result entirely in memory, then persists/replaces the stored array only if valid. This is the atomicity mechanism.

**Scenario traces**

| Scenario | Initial | Input | Result / final ordered list |
|---|---|---|---|
| Exact replay | `[{a, Apples}]` | `[{a, Apples}]` | `ok, added: 0`; unchanged `[{a, Apples}]` |
| Existing conflict plus new | `[{a, Apples}]` | `[{a, Apricots}, {b, Bread}]` | `conflict, id: a`; unchanged `[{a, Apples}]` |
| Entirely new IDs | `[{a, Apples}]` | `[{b, Bread}, {c, Coffee}]` | `ok, added: 2`; `[{a, Apples}, {b, Bread}, {c, Coffee}]` |
| Missing ID | `[{a, Apples}]` | `[{name, Bread}]` | `malformed`; unchanged `[{a, Apples}]` |

The importer also rejects duplicate IDs within one batch when their names differ; identical in-batch duplicates are treated as replay/no-op. This avoids ambiguous batch semantics.

**Assumptions / required mechanisms**

- Item IDs and names are non-empty strings after validation.
- Build an in-memory `Map<id,name>` from current items and a candidate append list.
- Scan input in order: same known ID/name => no-op; same ID/different name => conflict; unknown ID => candidate append.
- Commit the concatenated array once after full validation; local persistence must support replace/atomic write (write temp then rename for a file).

**Costs**

One array and transient map proportional to list size; a single narrow mutation method. Reads return immutable snapshots to prevent bypassing identity/order rules.

**Weakest point**

Durability depends on the local storage replacement being crash-safe. Without atomic file replacement (or equivalent storage transaction), a process/power failure during persistence can corrupt or partially update the list, though logical conflicts remain all-or-nothing in memory.

## Recovery entrant response (verbatim)

**Independent entry — staging preview importer**

**Interface.** `previewImport(rawItems)` parses and validates a batch without changing the shopping list. It returns an `ImportPreview`:

- `accepted`: new items that would be appended, in input order
- `unchanged`: existing identical `(id, name)` replays
- `errors`: row-indexed diagnostics (`missing_id`, `invalid_name`, `id_name_conflict`, duplicate-in-batch conflict)
- `canCommit`: true only when `errors` is empty
- summary counts and the original list revision/fingerprint

`commitImport(preview)` applies only a valid preview against the same list revision; otherwise it returns `stale_preview` and asks for a fresh preview. The UI shows a row-by-row table, retains raw input, permits correction/retry, and has an explicit “Apply N new items” action.

**Scenario traces.**

| Scenario | Preview | Commit/list outcome |
|---|---|---|
| Exact replay `[{a, Apple}]` when `a/Apple` exists | unchanged: `a`; no errors | enabled; no write; order unchanged |
| Batch `[{a, Apricot},{b, Bread}]` when `a/Apple` exists | error at row 1: `id_name_conflict`, showing existing and supplied names; `b` may be labelled “would add, blocked by batch” | disabled; list remains exactly unchanged |
| Entirely new `[{b,Bread},{c,Cheese}]` | accepted `b,c`; no errors | append `b,c` after current items |
| `[{name, Bread}]` | error at row 1: `missing_id` | disabled; list unchanged |

**Required mechanisms/assumptions.** The canonical list is an ordered array plus an ID index (or an ordered map). IDs are non-empty strings; names are strings and equality is exact unless normalization is explicitly defined. Preview first validates every row, detects repeated IDs within the batch, compares each ID with the current index, and constructs a staged candidate list. Commit performs one atomic replacement/appending operation only after rechecking the preview fingerprint. Import source can be local JSON/CSV adapted to the shared item shape; no server/database is needed.

**Costs.** Stores preview state/raw input and requires a revision check; imports scan the batch and maintain an index.

**Weakest point.** “Same name” equivalence is product-sensitive: strict equality makes behavior deterministic but may surprise users over whitespace/case. A documented normalization policy, displayed in the preview, is needed before broad import use.

## Coordinator verdict

Both independently produced entries satisfy the four cases at the design level.
Their differences are real: a single validation/commit boundary versus a persisted
preview contract with stale-preview checks and richer diagnostics. Neither has
been implemented by this run. The minimal design is sufficient for the supplied
scope; a two-step preview becomes attractive when human correction before applying
an import is itself required. Row-level diagnostics can be borrowed without
requiring persistent preview state. The losing design retains its useful role.

Empty-name validity and normalization were not settled by the shared brief. Treat
those as additional assumptions, not new approved requirements. Likewise a claim
about crash-safe storage needs a concrete storage implementation and evidence.
This exercise demonstrates independent brief provenance, comparable scenarios and
honest synthesis; it does not prove that independent agents always disagree or
always produce correct designs.
