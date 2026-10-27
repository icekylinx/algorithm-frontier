#!/usr/bin/env python3
"""Independent common-set and rooted-tree enumeration for initialized reports.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
"""
from fractions import Fraction as Q
from itertools import combinations
import json
from pathlib import Path
import random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
import matroid_reporting as impl
import arborescence_reporting as reporting
from check_arborescence_reporting import all_trees, tree


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def subsets(n):
    return (frozenset(i for i in range(n) if mask >> i & 1) for mask in range(1 << n))


def binary_rank(columns, chosen):
    pivots = {}
    for e in sorted(chosen):
        value = columns[e]
        while value:
            j = value.bit_length() - 1
            if j not in pivots:
                pivots[j] = value
                break
            value ^= pivots[j]
    return len(pivots)


def check_instance(costs, independent1, independent2, ranks, counts):
    n = len(costs)
    common = [chosen for chosen in subsets(n) if independent1(chosen) and independent2(chosen)]
    for rank in ranks:
        candidates = [chosen for chosen in common if len(chosen) == rank]
        oracle = impl.build(costs, rank, independent1, independent2)
        counts["fixed_rank_constructions"] += 1
        if not candidates:
            require(oracle is None, "initializer failed to report original rank infeasibility")
            counts["initial_infeasibilities"] += 1
            continue
        require(oracle is not None and len(oracle.baseline) == rank, "baseline has wrong rank")
        optimum = min(sum((costs[e] for e in chosen), Q(0)) for chosen in candidates)
        require(oracle.baseline_cost == optimum, "baseline is not independently optimal")
        require(oracle.auxiliary_nodes == 2 * rank, "compressed graph has wrong split dimension")
        require(oracle.auxiliary_arcs <= rank * rank + rank, "compressed graph has too many arcs")
        for failed in (None, *range(n), n + 99):
            surviving = [chosen for chosen in candidates if failed not in chosen]
            answer = oracle.query(failed)
            counts["ordinary_queries"] += 1
            if not surviving:
                require(answer is None and oracle.optimum_cost(failed) is None,
                        "failure infeasibility differs from enumeration")
                counts["failure_infeasibilities"] += 1
                continue
            expected = min(sum((costs[e] for e in chosen), Q(0)) for chosen in surviving)
            require(answer is not None and len(answer) == len(set(answer)) == rank,
                    "literal toggle repeats an original element")
            chosen = frozenset(answer)
            require(chosen in surviving and chosen <= set(oracle.support),
                    "reported set is infeasible or outside retained support")
            require(sum((costs[e] for e in answer), Q(0)) == expected
                    and oracle.optimum_cost(failed) == expected, "reported cost is not exact")
            minimum_added = min(len(c - set(oracle.baseline)) for c in surviving
                                if sum((costs[e] for e in c), Q(0)) == expected)
            require(len(chosen - set(oracle.baseline)) == minimum_added,
                    "minimum-hop literal update is not minimal among optimal repairs")
            if failed in oracle.routes:
                route = oracle.routes[failed]
                path = oracle._report(route)
                vertices = (route.source,) + tuple(a.head for a in path)
                require(len(vertices) == len(set(vertices)), "reported demand path repeats a vertex")
                counts["hub_reports" if route.hub is not None else "explicit_reports"] += 1
            counts["feasible_queries"] += 1


def check_partition(counts):
    possible = tuple((u, v) for u in range(3) for v in range(3))
    profiles = (tuple(0 for _ in possible),
                tuple((i * i + i) % 7 - 3 for i in range(9)),
                tuple(Q((5 * i + 2) % 9 - 4, i % 3 + 1) for i in range(9)))
    for mask in range(1 << len(possible)):
        edges = tuple(e for i, e in enumerate(possible) if mask >> i & 1)
        first = lambda chosen: len({edges[i][0] for i in chosen}) == len(chosen)
        second = lambda chosen: len({edges[i][1] for i in chosen}) == len(chosen)
        for profile in profiles:
            costs = tuple(value for i, value in enumerate(profile) if mask >> i & 1)
            check_instance(costs, first, second, range(5), counts)
        counts["bipartite_topologies"] += 1


def check_other_matroids(counts):
    rng = random.Random(271034)
    for _ in range(160):
        n = rng.randrange(9)
        first_columns = tuple(rng.randrange(16) for _ in range(n))
        second_columns = tuple(rng.randrange(16) for _ in range(n))
        first = lambda chosen: binary_rank(first_columns, chosen) == len(chosen)
        second = lambda chosen: binary_rank(second_columns, chosen) == len(chosen)
        costs = tuple(Q(rng.randrange(-4, 5), rng.randrange(1, 4)) for _ in range(n))
        check_instance(costs, first, second, range(n + 2), counts)
        counts["represented_matroid_pairs"] += 1
    excluded = tuple(map(frozenset, ((0, 1, 2, 3), (0, 1, 4, 5), (0, 1, 6, 7),
                                     (2, 3, 4, 5), (2, 3, 6, 7))))
    paving = lambda chosen: len(chosen) < 4 or (len(chosen) == 4 and chosen not in excluded)
    family = tuple(chosen for chosen in subsets(8) if paving(chosen))
    for chosen in family:
        require(all(paving(chosen - {e}) for e in chosen), "fixture violates heredity")
        for larger in family:
            if len(chosen) < len(larger):
                require(any(paving(chosen | {e}) for e in larger - chosen),
                        "fixture violates matroid augmentation")
                counts["fixture_augmentation_axioms"] += 1
    partition = lambda chosen: len({e // 2 for e in chosen}) == len(chosen)
    for other in (partition, lambda chosen: len(chosen) <= 4):
        for costs in ((0,) * 8, tuple(range(-4, 4)), tuple(Q((5 * i) % 7 - 3, 3) for i in range(8))):
            check_instance(costs, paving, other, range(6), counts)
            counts["sparse_paving_profiles"] += 1
    huge = 1 << 300
    check_instance((-huge, 1 - huge, Q(1, huge), 0, huge),
                   lambda chosen: len(chosen) <= 2, lambda chosen: len(chosen) <= 3,
                   range(5), counts)
    counts["large_cost_profiles"] += 1


def check_arborescences(counts):
    n, root = 4, 0
    possible = tuple((u, v) for u in range(n) for v in range(1, n) if u != v)
    for mask in range(1 << len(possible)):
        for profile in (tuple(0 for _ in possible),
                        tuple(Q((i * i + 2 * i) % 7, i % 3 + 1) for i in range(9))):
            arcs = tuple(reporting.Arc(u, v, profile[i]) for i, (u, v) in enumerate(possible)
                         if mask >> i & 1)
            candidates = all_trees(n, root, arcs)
            oracle = impl.build_arborescence(n, root, arcs)
            counts["initialized_graph_profiles"] += 1
            if not candidates:
                require(oracle is None, "initial arborescence infeasibility missed")
                counts["graph_initial_infeasibilities"] += 1
                continue
            for failed in (None, *range(len(arcs)), len(arcs) + 1):
                expected = min((cost for cost, chosen in candidates if failed not in chosen), default=None)
                answer = oracle.query(failed)
                if expected is None:
                    require(answer is None, "rooted tree failure infeasibility missed")
                else:
                    require(tree(n, root, arcs, answer) and failed not in answer
                            and sum((arcs[i].cost for i in answer), Q(0)) == expected,
                            "initialized directed tree report differs from enumeration")
                counts["initialized_graph_queries"] += 1
    fixtures = ((1, 0, (reporting.Arc(0, 0, 3),)),
                (3, 2, (reporting.Arc(2, 0, 0), reporting.Arc(0, 1, 2),
                         reporting.Arc(2, 1, 1), reporting.Arc(0, 1, 3),
                         reporting.Arc(1, 2, 0), reporting.Arc(0, 0, 0))))
    for n, root, arcs in fixtures:
        oracle = impl.build_arborescence(n, root, arcs)
        candidates = all_trees(n, root, arcs)
        for failed in (None, *range(len(arcs))):
            expected = min((cost for cost, chosen in candidates if failed not in chosen), default=None)
            answer = oracle.query(failed)
            require((answer is None) == (expected is None), "graph boundary feasibility differs")
            if answer is not None:
                require(tree(n, root, arcs, answer)
                        and sum((arcs[i].cost for i in answer), Q(0)) == expected,
                        "graph boundary optimum differs")
            counts["initialized_graph_queries"] += 1
        counts["graph_boundary_fixtures"] += 1


def check_hubs_and_storage(counts):
    for rank in (8, 25):
        edges = tuple((i, i) for i in range(rank)) + tuple((i, (i + 1) % rank) for i in range(rank))
        costs = (Q(0),) * rank + (Q(-1),) * rank
        first = lambda chosen: len({edges[i][0] for i in chosen}) == len(chosen)
        second = lambda chosen: len({edges[i][1] for i in chosen}) == len(chosen)
        oracle = impl.build(costs, rank, first, second)
        require(oracle.hubs and oracle.baseline_cost == -rank, "long signed cycle missed hubs")
        for failed in oracle.baseline:
            require(set(oracle.query(failed)) == set(range(rank))
                    and oracle.optimum_cost(failed) == 0, "long signed repair differs")
            require(oracle.routes[failed].hub is not None, "long cycle report was not hub-based")
            counts["long_signed_hub_queries"] += 1
    enabled = [True]

    def independent(chosen):
        if not enabled[0]:
            raise AssertionError("query called original independence oracle")
        return len(chosen) <= 2

    costs = list(range(-1024, 0))
    oracle = impl.build(costs, 2, independent, independent)
    require(oracle.baseline == (0, 1) and oracle.support == (0, 1, 2),
            "large-ground rank-two restriction is wrong")
    require(oracle.record_count < 50 and not any(callable(v) for v in vars(oracle).values()),
            "ground-sized initializer state escaped into final oracle")
    enabled[0] = False
    costs.clear()
    saved = impl.weighted.minimum_cost, reporting._distances, reporting._sparsify

    def unavailable(*args, **kwargs):
        raise AssertionError("query invoked preprocessing")

    try:
        impl.weighted.minimum_cost = reporting._distances = reporting._sparsify = unavailable
        for failed, expected in ((None, (0, 1)), (0, (1, 2)), (1, (0, 2)), (2, (0, 1)),
                                 (1024, (0, 1))):
            require(tuple(sorted(oracle.query(failed))) == expected,
                    "producer-free original-ground query is wrong")
            counts["producer_disabled_queries"] += 1
    finally:
        impl.weighted.minimum_cost, reporting._distances, reporting._sparsify = saved
    require(impl.build((), 10**100, lambda s: True, lambda s: True) is None,
            "huge infeasible rank was expanded")
    invalid = (lambda: impl.build((0.5,), 1, lambda s: True, lambda s: True),
               lambda: impl.build((0,), -1, lambda s: True, lambda s: True),
               lambda: impl.build((0,), 1, None, lambda s: True),
               lambda: impl.build_arborescence(2, 0, (reporting.Arc(0, 1, -1),)),
               lambda: impl.build_arborescence(2, 2, (reporting.Arc(0, 1, 1),)))
    for thunk in invalid:
        try:
            thunk()
        except ValueError:
            counts["malformed_inputs"] += 1
        else:
            raise AssertionError("malformed input accepted")


def main():
    names = ("bipartite_topologies", "fixed_rank_constructions", "initial_infeasibilities",
             "ordinary_queries", "feasible_queries", "failure_infeasibilities", "hub_reports",
             "explicit_reports", "represented_matroid_pairs", "fixture_augmentation_axioms",
             "sparse_paving_profiles", "initialized_graph_profiles", "graph_initial_infeasibilities",
             "large_cost_profiles",
             "initialized_graph_queries", "graph_boundary_fixtures", "long_signed_hub_queries",
             "producer_disabled_queries", "malformed_inputs")
    counts = dict.fromkeys(names, 0)
    check_partition(counts)
    check_other_matroids(counts)
    check_arborescences(counts)
    check_hubs_and_storage(counts)
    print(json.dumps({"status": "pass", "initialized_matroid_reporting": counts}, indent=2))


if __name__ == "__main__":
    main()
