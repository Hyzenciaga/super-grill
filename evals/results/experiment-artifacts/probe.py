"""Disposable comparison for replaying the supplied import fixture."""

import json
from pathlib import Path

from baseline import import_items as baseline_import


ROOT = Path(__file__).parent


def import_items_by_stable_id(current, incoming):
    """Merge in encounter order, retaining one item for every nonempty string id."""
    by_id = {}
    for item in [*current, *incoming]:
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id:
            raise ValueError("every imported item needs a nonempty string id")
        by_id[item_id] = item
    return list(by_id.values())


def summary(items):
    ids = [item["id"] for item in items]
    return {"count": len(items), "ids": ids, "unique_id_count": len(set(ids))}


fixture = json.loads((ROOT / "items.json").read_text())

baseline_once = baseline_import([], fixture)
baseline_twice = baseline_import(baseline_once, fixture)

candidate_once = import_items_by_stable_id([], fixture)
candidate_twice = import_items_by_stable_id(candidate_once, fixture)

assert summary(baseline_twice) == {
    "count": 6,
    "ids": ["a", "b", "c", "a", "b", "c"],
    "unique_id_count": 3,
}
assert summary(candidate_twice) == {
    "count": 3,
    "ids": ["a", "b", "c"],
    "unique_id_count": 3,
}

print(
    json.dumps(
        {
            "fixture": summary(fixture),
            "baseline_once": summary(baseline_once),
            "baseline_twice": summary(baseline_twice),
            "candidate_once": summary(candidate_once),
            "candidate_twice": summary(candidate_twice),
        },
        ensure_ascii=False,
        indent=2,
    )
)
