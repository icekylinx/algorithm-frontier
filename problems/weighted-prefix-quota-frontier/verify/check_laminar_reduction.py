#!/usr/bin/env python3
"""Exhaustively check aggregate lower-demand compression on finite laminar trees.

For each listed laminar topology, every lower-bound assignment in the stated
range is checked against every integral nonnegative mass vector under the root
cap. The reference tests original and retained inequalities literally. It does
not use the aggregate-demand recurrence to decide feasibility. The checker
also checks the telescoping charge identity and the at-most-B row bound.

This finite test does not verify the separate valuated-matroid completion
oracle, upper-row coloring theorem, or asymptotic enumeration bound.
"""
from __future__ import annotations

from itertools import product
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def compress(nodes: tuple[int, ...], lower: tuple[int, ...]):
    lower_by_node = dict(zip(nodes, lower))
    children = {
        node: tuple(
            candidate for candidate in nodes
            if candidate != node and candidate & ~node == 0
            and not any(
                middle not in (candidate, node)
                and candidate & ~middle == 0 and middle & ~node == 0
                for middle in nodes
            )
        )
        for node in nodes
    }
    demand = {}
    retained = []
    charges = {}
    for node in sorted(nodes, key=int.bit_count):
        child_sum = sum(demand[child] for child in children[node])
        demand[node] = max(lower_by_node[node], child_sum)
        charges[node] = demand[node] - child_sum
        if lower_by_node[node] > child_sum:
            retained.append(node)
    roots = tuple(
        node for node in nodes
        if not any(node != other and node & ~other == 0 for other in nodes)
    )
    root_demand = sum(demand[node] for node in roots)
    return tuple(retained), root_demand, charges


def mass_in(mask: int, vector: tuple[int, ...]) -> int:
    return sum(value for i, value in enumerate(vector) if mask >> i & 1)


def main() -> None:
    require(__debug__, "run with assertions enabled")
    topologies = (
        (1, 3, 7, 15),                    # One nested chain.
        (1, 2, 4, 8, 15),                 # A four-leaf star.
        (1, 2, 3, 4, 8, 12, 15),          # A complete binary hierarchy.
        (1, 2, 3, 4, 12),                 # A forest, one uncovered coordinate per root.
        (),                               # No lower row at all.
    )
    assignments = comparisons = rejected = reduced = 0
    for nodes in topologies:
        require(all(
            not a & b or a & ~b == 0 or b & ~a == 0
            for a in nodes for b in nodes
        ), "test topology must be laminar")
        for root_cap in range(4):
            vectors = tuple(
                vector for vector in product(range(root_cap + 1), repeat=4)
                if sum(vector) <= root_cap
            )
            for lower in product(range(root_cap + 1), repeat=len(nodes)):
                assignments += 1
                retained, demand, charges = compress(nodes, lower)
                thresholds = dict(zip(nodes, lower))
                require(sum(charges.values()) == demand, "telescoping charge identity")
                require(
                    set(retained) == {node for node, charge in charges.items() if charge > 0},
                    "positive charges identify retained rows",
                )
                if demand > root_cap:
                    rejected += 1
                else:
                    require(len(retained) <= root_cap, "at-most-B lower rows")
                    patterns = {tuple(node for node in retained if node >> e & 1)
                                for e in range(4)}
                    require(len(patterns) <= len(retained) + 1, "lower membership patterns")
                if len(retained) < len(nodes):
                    reduced += 1
                for vector in vectors:
                    comparisons += 1
                    original = all(mass_in(node, vector) >= thresholds[node] for node in nodes)
                    compressed = all(mass_in(node, vector) >= thresholds[node] for node in retained)
                    require(original == compressed, "all original lower rows remain equivalent")
                    require(not original or demand <= root_cap, "aggregate rejection is sound")
    print(json.dumps({
        "status": "passed",
        "scope": "finite lower-row equivalence, aggregate infeasibility, and telescoping row bound",
        "laminar_topologies": len(topologies),
        "root_caps": [0, 1, 2, 3],
        "lower_bound_assignments": assignments,
        "integral_mass_comparisons": comparisons,
        "aggregate_rejections": rejected,
        "strict_row_reductions": reduced,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
