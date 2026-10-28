#!/usr/bin/env python3
"""Independent exact rational checks for whole-item label decoding.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
"""
from fractions import Fraction as Q
from itertools import combinations, product
import json
from pathlib import Path
import random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
import whole_blocks as impl


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def subsets(values, budget):
    values = tuple(sorted(values))
    for size in range(min(budget, len(values)) + 1):
        yield from combinations(values, size)


def rank(columns, dimension):
    """Independent row elimination on a transposed, explicitly supplied matrix."""
    columns = tuple(columns)
    rows = [[Q(c[i]) for c in columns] for i in range(dimension)]
    pivot = 0
    for j in range(len(columns)):
        found = next((i for i in range(pivot, dimension) if rows[i][j]), None)
        if found is None:
            continue
        rows[pivot], rows[found] = rows[found], rows[pivot]
        scale = rows[pivot][j]
        rows[pivot] = [x / scale for x in rows[pivot]]
        for i in range(pivot + 1, dimension):
            scale = rows[i][j]
            rows[i] = [x - scale * y for x, y in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == dimension:
            break
    return pivot


def outside(block, space, dimension):
    return rank(tuple(space) + tuple(block), dimension) > rank(space, dimension)


def direct_value(blocks, item_labels, weights, failed, space, dimension):
    return sum((w for block, item, w in zip(blocks, item_labels, weights)
                if not set(item) & set(failed) and outside(block, space, dimension)), Q(0))


def direct_polynomial(difference, points, h, k):
    """Expand all factor-index choices, not the backend's product frontier."""
    difference = tuple(sorted(difference))
    coefficients = {}
    for indices in product(range(h + 1), repeat=len(difference)):
        exponent = [k - len(difference)] + [0] * h
        coefficient = Q(1)
        for label, j in zip(difference, indices):
            exponent[j] += 1
            coefficient *= points[label] ** j
        key = tuple(exponent)
        coefficients[key] = coefficients.get(key, Q(0)) + coefficient
    return coefficients


def audit(compiled, spaces, counts):
    n = len(compiled.row_labels)
    counts["compilations"] += 1
    counts[compiled.mode.lower()] += 1
    if compiled.mode == "LIFT":
        require(compiled.dimension < len(compiled.blocks), "lift passed an invalid dimension gate")
        require(len(compiled.monomials) == compiled.feature_count, "wrong feature dimension")
        for block, item, lifted in zip(compiled.blocks, compiled.item_labels, compiled.lifted):
            for column, vector in zip(block, lifted):
                for j, i in enumerate(compiled.selected_rows):
                    expected = (direct_polynomial(item - compiled.row_labels[i], compiled.points,
                                                  compiled.effective_failures, compiled.deficit)
                                if column[i] else {})
                    actual = vector[j * compiled.feature_count:(j + 1) * compiled.feature_count]
                    require(actual == tuple(column[i] * expected.get(e, 0)
                                            for e in compiled.monomials),
                            "ordinary monomial expansion differs")
                    counts["coefficient_blocks"] += 1
        for block in compiled.blocks:
            for column in block:
                require(tuple(sum((c * column[i] for c, i in zip(row, compiled.selected_rows)), Q(0))
                              for row in compiled.compression) == column,
                        "C(PA) does not equal the original column")
                counts["rank_compression_columns"] += 1
        # A rank oracle is on complete original items, never individual columns.
        for ids in ((), (0,), tuple(range(min(3, len(compiled.blocks))))):
            expected = rank(tuple(c for i in ids for c in compiled.lifted[i]), compiled.dimension)
            require(compiled.rank_on(ids) == expected, "whole-item lifted rank differs")
            counts["rank_queries"] += 1
    for failed in subsets(compiled.points, compiled.failures):
        scalars = compiled.scalars(failed)
        require(all((scalar == 0) == bool(set(failed) & item)
                    for scalar, item in zip(scalars, compiled.item_labels)),
                "common-scalar zero pattern differs from original failures")
        counts["failure_patterns"] += 1
        if compiled.mode != "FULL_INPUT":
            decoded = compiled.decode(failed)
            for block, actual, scalar in zip(compiled.blocks, decoded, scalars):
                require(actual == tuple(tuple(scalar * x for x in column) for column in block),
                        "columns of one original item do not share the exact scalar")
                counts["common_scalar_blocks"] += 1
        for space in spaces:
            expected = direct_value(compiled.blocks, compiled.item_labels, compiled.weights,
                                    failed, space, n)
            require(compiled.value(space, failed) == expected, "subspace-complement value differs")
            counts["subspace_queries"] += 1
        # Arbitrary fixed original-item reweightings are decoded identically;
        # approximation quality is intentionally not inferred by the API.
        alternative = tuple(Q((7 * i) % 5, 3) for i in compiled.original_ids)
        require(compiled.value((), failed, alternative)
                == direct_value(compiled.blocks, compiled.item_labels, alternative, failed, (), n),
                "original-ID reweighting was split across columns")
        counts["reweighted_queries"] += 1


def check_algebra(counts):
    rng = random.Random(271031)
    for seed in range(12):
        # Row zero is unused and has an unrelated original label. Rows 2 and
        # 4 are dependent; selected rows must keep their own incidence labels.
        row_labels = ({999}, {10}, {10, 20}, {30}, set())
        blocks, item_labels = [], []
        for i in range(64):
            raw = [(rng.randrange(-1, 2), rng.randrange(-1, 2))
                   for _ in range(i % 3)]
            block = tuple((0, Q(x, 2), x, Q(y, 3), Q(x, 2) + Q(y, 3)) for x, y in raw)
            item = set()
            if any(x for x, _ in raw):
                item |= {10, 20}
            if any(y for _, y in raw):
                item |= {30}
            if i % 4 == 0:
                item.add(40)
            blocks.append(block)
            item_labels.append(item)
        compiled = impl.compile_blocks(blocks, row_labels, item_labels, seed % 4,
                                       weights=[Q(i % 7, 5) for i in range(64)])
        spaces = [(), ((0, 1, 2, 0, 1),), ((0, 0, 0, 1, 1),),
                  ((0, 1, 2, 0, 1), (0, 0, 0, 1, 1)),
                  tuple(tuple(int(i == j) for i in range(5)) for j in range(5))]
        audit(compiled, spaces, counts)
        require(compiled.selected_rows == (1, 3), "compression relabeled dependent original rows")
    # Empty rows, empty blocks, zero vectors, no labels, and degree zero.
    for blocks, rows, items, h in (([(), ((0, 0),)], ({7}, set()), (set(), {2}), 2),
                                   ([(), ()], (), (set(), {1}), 10**100),
                                   ([((1,),)] * 3, (set(),), (set(),) * 3, 10**100),
                                   ([((1,),)] * 3, ({5},), ({5},) * 3, 2)):
        audit(impl.compile_blocks(blocks, rows, items, h), [()], counts)


def check_graphs(counts):
    n = 4
    row_labels = ({0}, {0}, {1}, {2})
    possible = tuple(combinations(range(n), 2))
    for mask in range(1 << len(possible)):
        edges = [e for i, e in enumerate(possible) if mask >> i & 1]
        # One column per original graph edge, then duplicate original items so
        # some compact lifts fall below the item-count cap.
        blocks = [((tuple(int(i == u) - int(i == v) for i in range(n))),)
                  for u, v in edges] * 8
        items = [row_labels[u] | row_labels[v] for u, v in edges] * 8
        compiled = impl.compile_blocks(blocks, row_labels, items, 1)
        for failed in subsets((0, 1, 2), 1):
            for cut in product((0, 1), repeat=n):
                # A cut kernel's rational basis is made independently by
                # subtracting one coordinate in the cut from each other one.
                ones = [v for v in range(n) if cut[v]]
                space = [tuple(int(i == v) for i in range(n))
                         for v in range(n) if not cut[v]]
                if ones:
                    space.extend(tuple(int(i == v) - int(i == ones[0]) for i in range(n))
                                 for v in ones[1:])
                expected = 8 * sum(cut[u] != cut[v] and not (row_labels[u] | row_labels[v]) & set(failed)
                                   for u, v in edges)
                require(compiled.value(space, failed) == expected,
                        "graph cut decoder differs from original crossing edges")
                counts["graph_cut_queries"] += 1
        counts["graph_topologies"] += 1


def check_hyperedges(counts):
    n = 4
    edges = ((0, 1, 2), (1, 2, 3), (0, 3), (2,), ())
    row_labels = ({0}, {1}, {1}, set())
    extra = (set(), {2}, {0}, set(), {2})
    blocks = [tuple(tuple(int(i == edge[0]) - int(i == v) for i in range(n))
                    for v in edge[1:]) for edge in edges] * 12
    items = [set().union(*(row_labels[v] for v in edge), extra[j])
             for j, edge in enumerate(edges)] * 12
    compiled = impl.compile_blocks(blocks, row_labels, items, 2)
    for failed in subsets((0, 1, 2), 2):
        for partition in product(range(3), repeat=n):
            space = []
            for part in range(3):
                vertices = [v for v in range(n) if partition[v] == part]
                if vertices:
                    space.extend(tuple(int(i == vertices[0]) - int(i == v) for i in range(n))
                                 for v in vertices[1:])
            expected = 12 * sum(not items[j] & set(failed)
                                and len({partition[v] for v in edge}) >= 2
                                for j, edge in enumerate(edges))
            require(compiled.value(space, failed) == expected,
                    "atomic hyperedge partition indicator was split or shortened")
            counts["hyperedge_partition_queries"] += 1
    # Vertex 0 fails: hyperedge {0,1,2} disappears as a whole, although its
    # surviving pair {1,2} still crosses this partition.
    require(compiled.item_labels[0] & {0}, "atomic fixture did not delete whole item")


def check_guards(counts):
    # The cap must act before any monomial enumeration or polynomial product.
    saved = impl._monomials, impl._polynomial

    def unavailable(*args, **kwargs):
        raise AssertionError("large feature space was materialized")

    impl._monomials = impl._polynomial = unavailable
    try:
        big_labels = set(range(150))
        compiled = impl.compile_blocks([((1,),)], (set(),), (big_labels,), 10**100)
        require(compiled.mode == "FULL_INPUT" and compiled.dimension > 10**80,
                "feature cap did not protect a huge formal dimension")
        require(compiled.value((), (149,)) == 0 and compiled.value() == 1,
                "whole-input fallback changed original deletion semantics")
        counts["large_dimension_gates"] += 1
    finally:
        impl._monomials, impl._polynomial = saved
    valid = impl.compile_blocks([((1,),)] * 4, (set(),), ({1},) * 4, 1)
    invalid = [
        lambda: impl.compile_blocks([((1,),)], ({1},), (set(),), 1),
        lambda: impl.compile_blocks([((1,),)], (set(),), ({1},), 1, deficit=0),
        lambda: impl.compile_blocks([((0.5,),)], (set(),), ({1},), 1),
        lambda: impl.compile_blocks([((1, 2),)], (set(),), ({1},), 1),
        lambda: impl.compile_blocks([((1,),)], (set(),), (), 1),
        lambda: impl.compile_blocks([], (), (), -1),
        lambda: impl.compile_blocks([], (), (), 0, weights=(1,)),
        lambda: impl.compile_blocks([((1,),)], (set(),), ({-1},), 1),
        lambda: valid.decode((1, 1)),
        lambda: valid.decode((1, 2)),
        lambda: valid.value(((1, 2),)),
        lambda: valid.value(weights=(-1,) * 4),
        lambda: valid.rank_on((0, 0)),
        lambda: compiled.decode(()),
    ]
    for thunk in invalid:
        try:
            thunk()
        except ValueError:
            counts["rejected_inputs"] += 1
        else:
            raise AssertionError("invalid input was accepted")
    require(valid.value((), (999,)) == 4, "unknown label changed the objective")


def main():
    counts = dict.fromkeys(("compilations", "lift", "full_input", "zero", "coefficient_blocks",
                            "rank_compression_columns", "rank_queries", "failure_patterns",
                            "common_scalar_blocks", "subspace_queries", "reweighted_queries",
                            "graph_topologies", "graph_cut_queries", "hyperedge_partition_queries",
                            "large_dimension_gates", "rejected_inputs"), 0)
    check_algebra(counts)
    check_graphs(counts)
    check_hyperedges(counts)
    check_guards(counts)
    print(json.dumps({"status": "pass", "whole_block_decoder": counts}, indent=2))


if __name__ == "__main__":
    main()
