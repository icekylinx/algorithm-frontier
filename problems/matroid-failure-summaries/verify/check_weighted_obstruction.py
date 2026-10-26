#!/usr/bin/env python3
"""Exact certificate for the weighted two-label-failure oracle obstruction.

All finite feasible sets and bases are enumerated directly. Rank values use
an exhaustive subset recurrence, and optimum values minimize literal costs
over all surviving bases. Greedy is a separately checked algorithm. No
floating-point arithmetic, random search, or external solver is used.
"""
from __future__ import annotations

from itertools import combinations
import json


FORBIDDEN = frozenset((15, 51, 195, 60, 204))
ITEMS = (
    (5, "B"), (2, "A"), (3, "A"), (1, "C"), (7, "D"),
    (4, "B"), (0, "C"), (6, "D"), (2, "D"), (1, "B"),
    (5, "C"), (4, "D"), (2, "C"),
)
EXPECTED = {
    "AB": (4, 5, 7, 9), "AC": (1, 5, 6, 8),
    "AD": (1, 4, 6, 13), "BC": (2, 3, 5, 12),
    "BD": (2, 3, 4, 11), "CD": (1, 2, 3, 10),
}
NECESSITY = ("CD", "CD", "CD", "BD", "BC", "AD", "AB",
             "AC", "AB", "CD", "BD", "BC", "AD")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def bits(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def class_independent(mask: int) -> bool:
    size = mask.bit_count()
    return size < 4 or (size == 4 and mask not in FORBIDDEN)


def independent(mask: int, items=ITEMS) -> bool:
    classes = 0
    for i in bits(mask):
        bit = 1 << items[i][0]
        if classes & bit:
            return False
        classes |= bit
    return class_independent(classes)


def mask_of_ids(ids) -> int:
    return sum(1 << (i - 1) for i in ids)


def surviving(items, failed) -> int:
    return sum(1 << i for i, (_, label) in enumerate(items) if label not in failed)


def greedy(live: int, items=ITEMS) -> int:
    selected = 0
    for i in bits(live):
        if independent(selected | (1 << i), items):
            selected |= 1 << i
    return selected


def cost(mask: int) -> int:
    return sum(2 ** i for i in bits(mask))


def basis_exchange(bases: tuple[int, ...]) -> int:
    base_set = frozenset(bases)
    require(bool(bases), "basis family must be nonempty")
    require(len({b.bit_count() for b in bases}) == 1, "bases have one size")
    checks = 0
    for left in bases:
        for right in bases:
            for removed in bits(left & ~right):
                checks += 1
                require(any(
                    (left ^ (1 << removed) | (1 << added)) in base_set
                    for added in bits(right & ~left)
                ), "basis exchange")
    return checks


def all_bases(items) -> tuple[int, ...]:
    return tuple(
        sum(1 << i for i in chosen)
        for chosen in combinations(range(len(items)), 4)
        if independent(sum(1 << i for i in chosen), items)
    )


def minimum_basis(live: int, bases: tuple[int, ...]) -> int | None:
    candidates = [b for b in bases if b & ~live == 0]
    if not candidates:
        return None
    result = min(candidates, key=cost)
    require(sum(cost(b) == cost(result) for b in candidates) == 1, "unique optimum")
    return result


def main() -> None:
    require(__debug__, "run without -O; exact certificate assertions must stay enabled")
    require(all((a & b).bit_count() <= 2 for a, b in combinations(FORBIDDEN, 2)),
            "forbidden sets form a sparse-paving family")
    underlying = tuple(mask for mask in range(256)
                       if mask.bit_count() == 4 and class_independent(mask))
    require(len(underlying) == 65, "underlying base count")
    original_exchange_checks = basis_exchange(underlying)
    bases = all_bases(ITEMS)
    require(len(bases) == 386, "extended base count")
    extended_exchange_checks = basis_exchange(bases)

    # This computes rank by the definition, not by a greedy rank algorithm.
    ranks = [0] * (1 << len(ITEMS))
    independent_count = 1
    for mask in range(1, len(ranks)):
        if independent(mask):
            ranks[mask] = mask.bit_count()
            independent_count += 1
        else:
            ranks[mask] = max(ranks[mask ^ (1 << i)] for i in bits(mask))
    require(independent_count == 694, "independent-set count")
    require(ranks[-1] == 4, "rank four")
    for mask, rank in enumerate(ranks):
        require(rank == max((mask & basis).bit_count() for basis in bases),
                "rank table agrees with all bases")

    query_report = []
    union = 0
    rank_only = mask_of_ids((1, 2, 3, 5, 7, 10, 11, 12, 13))
    queries = 0
    for failure_count in range(3):
        for failed in combinations("ABCD", failure_count):
            queries += 1
            live = surviving(ITEMS, failed)
            optimum = minimum_basis(live, bases)
            require(optimum is not None and ranks[live] == 4, "every allowed query keeps rank")
            require(greedy(live) == optimum, "greedy agrees with exhaustive optimum")
            require(ranks[live & rank_only] == 4, "nine-item rank-only preserver")
            for end in range(len(ITEMS) + 1):
                prefix = (1 << end) - 1
                require(ranks[live & prefix] == (optimum & prefix).bit_count(),
                        "optimal greedy basis spans every prefix")
            if failure_count == 2:
                name = "".join(failed)
                require(optimum == mask_of_ids(EXPECTED[name]), "displayed optimum table")
                union |= optimum
                query_report.append({
                    "failed_labels": name,
                    "unique_basis": [i + 1 for i in bits(optimum)],
                    "cost": cost(optimum),
                    "surviving_bases": sum(b & ~live == 0 for b in bases),
                })
    require(union == (1 << len(ITEMS)) - 1, "all 13 items are forced")

    for protected, failed in enumerate(NECESSITY):
        live = surviving(ITEMS, failed)
        optimum = minimum_basis(live, bases)
        require(bool(optimum & (1 << protected)), "stated necessity witness")
        replacement = minimum_basis(live & ~(1 << protected), bases)
        require(replacement is None or cost(replacement) > cost(optimum),
                "every item deletion destroys an exact optimum value")
        prefix = (1 << (protected + 1)) - 1
        require(ranks[live & prefix] == ranks[live & prefix & ~(1 << protected)] + 1,
                "every item deletion destroys a required prefix rank")

    amplified_queries = 0
    amplified_items = 0
    for budget in range(2, 7):
        prepended = tuple((cls, f"Z{j}") for j in range(budget - 2)
                          for cls in (1, 2, 3, 5))
        items = prepended + ITEMS
        extended = all_bases(items)
        union = 0
        for block in range(budget - 2):
            failed = {f"Z{j}" for j in range(block)}
            optimum = minimum_basis(surviving(items, failed), extended)
            expected = sum(1 << (4 * block + i) for i in range(4))
            require(optimum == expected, "prepended basis block is forced")
            union |= optimum
            amplified_queries += 1
        all_new_labels = {f"Z{j}" for j in range(budget - 2)}
        for name, ids in EXPECTED.items():
            failed = all_new_labels | set(name)
            require(len(failed) == budget, "amplified witness uses exactly h labels")
            optimum = minimum_basis(surviving(items, failed), extended)
            require(optimum == mask_of_ids(ids) << len(prepended),
                    "original item witnesses survive amplification")
            union |= optimum
            amplified_queries += 1
        require(union == (1 << len(items)) - 1, "all amplified items are forced")
        require(len(items) == 4 * (budget + 1) + 1, "amplified support formula")
        amplified_items += len(items)

    print(json.dumps({
        "status": "passed",
        "scope": "exact specified obstruction and finite amplified examples; general family proved in manuscript",
        "underlying_bases": len(underlying),
        "underlying_basis_exchange_requirements": original_exchange_checks,
        "extended_independent_sets": independent_count,
        "extended_bases": len(bases),
        "extended_basis_exchange_requirements": extended_exchange_checks,
        "complete_rank_table_entries": len(ranks),
        "allowed_base_queries": queries,
        "forced_items": len(ITEMS),
        "represented_binomial_target": 12,
        "rank_only_preserver_size": rank_only.bit_count(),
        "amplified_budgets_checked": [2, 3, 4, 5, 6],
        "amplified_necessity_queries": amplified_queries,
        "amplified_forced_items": amplified_items,
        "two_failure_optima": query_report,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
