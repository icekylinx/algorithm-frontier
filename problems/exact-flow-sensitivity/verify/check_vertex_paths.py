#!/usr/bin/env python3
"""Independent finite path-packing and original-failure comparisons.

Enumerate simple native paths and compatible internal-vertex masks. This
oracle does not split vertices or use the flow solver. Explicit exceptions
remain active under optimized Python.

Attribution: Yilin Liu and GPT-6 Astra Pro.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import json
import random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
import unit_flow
from unit_flow import Arc
from vertex_paths import MaximumPathsOracle, fixed_paths


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def enumerate_paths(n, arcs, source, target):
    outgoing = [[] for _ in range(n)]
    for index, arc in enumerate(arcs):
        outgoing[arc.tail].append(index)
    result = []

    def visit(vertex, occupied, indices, cost):
        if vertex == target:
            result.append((tuple(indices), occupied & ~(1 << source) & ~(1 << target), cost))
            return
        for index in outgoing[vertex]:
            arc = arcs[index]
            if not occupied & (1 << arc.head):
                visit(arc.head, occupied | (1 << arc.head), indices + [index], cost + arc.cost)

    visit(source, 1 << source, [], Fraction(0))
    return result


def optima(paths, failed_arc=None, failed_vertex=None):
    states = {(0, 0): Fraction(0)}
    for ids, vertices, cost in paths:
        if failed_arc in ids or (failed_vertex is not None and vertices & (1 << failed_vertex)):
            continue
        for (used, value), old in list(states.items()):
            if not used & vertices:
                key = (used | vertices, value + 1)
                states[key] = min(states.get(key, old + cost), old + cost)
    best = {}
    for (_, value), cost in states.items():
        best[value] = min(best.get(value, cost), cost)
    return best


def check_answer(answer, expected, value, n, arcs, source, target, retained,
                 failed_arc=None, failed_vertex=None):
    if expected is None:
        require(answer is None, "an infeasible packing was reported")
        return
    require(answer is not None, "a feasible packing was omitted")
    require(answer.value == value and len(answer.paths) == value, "wrong path count")
    require(answer.cost == expected, "wrong optimum cost")
    occupied = set()
    edges = set()
    total = Fraction(0)
    for path in answer.paths:
        require(path.vertices[0] == source and path.vertices[-1] == target,
                "wrong native terminals")
        require(len(set(path.vertices)) == len(path.vertices), "nonsimple native path")
        require(len(path.arc_ids) + 1 == len(path.vertices), "wrong path encoding")
        for vertex in path.vertices[1:-1]:
            require(0 <= vertex < n and vertex not in occupied and vertex != failed_vertex,
                    "internal collision or failed vertex")
            occupied.add(vertex)
        for position, index in enumerate(path.arc_ids):
            require(type(index) is int and 0 <= index < len(arcs), "wrong original ID")
            require(index != failed_arc and index not in edges and index in retained,
                    "failed, repeated or nonretained original arc")
            edges.add(index)
            arc = arcs[index]
            require((arc.tail, arc.head) == path.vertices[position:position+2],
                    "wrong native endpoints")
            require(retained[index] == arc, "changed retained original record")
            total += arc.cost
    require(total == expected, "path cost does not match claimed cost")


def check_case(n, arcs, source, target, counts):
    original = tuple(arcs)
    paths = enumerate_paths(n, arcs, source, target)
    failures = [(None, None)] + [(i, None) for i in range(len(arcs))]
    failures += [(None, v) for v in range(n) if v not in (source, target)]
    expected = [optima(paths, edge, vertex) for edge, vertex in failures]
    maximum = max(expected[0])
    for value in range(maximum + 2):
        oracle = fixed_paths(n, arcs, source, target, value)
        if value > maximum:
            require(oracle is None, "originally infeasible value accepted")
            counts["infeasible_builds"] += 1
            continue
        for (edge, vertex), costs in zip(failures, expected):
            answer = oracle.query(failed_arc=edge, failed_vertex=vertex)
            require(oracle.cost(failed_arc=edge, failed_vertex=vertex) == costs.get(value),
                    "cost-only query mismatch")
            check_answer(answer, costs.get(value), value, n, arcs, source, target,
                         oracle.retained, edge, vertex)
            counts["fixed_queries"] += 1
            counts["infeasible_fixed_queries"] += answer is None
        # A simple packing's split baseline has at most three times n records.
        require(len(oracle._flow.baseline) <= 3*n-5 or value == 0,
                "split baseline exceeds the simple path inventory")
    maximum_oracle = MaximumPathsOracle(n, arcs, source, target)
    for (edge, vertex), costs in zip(failures, expected):
        value = max(costs)
        require(maximum - value in (0, 1), "one failure lost more than one path")
        answer = maximum_oracle.query(failed_arc=edge, failed_vertex=vertex)
        check_answer(answer, costs[value], value, n, arcs, source, target,
                     maximum_oracle.retained, edge, vertex)
        counts["maximum_queries"] += 1
        counts["maximum_drops"] += value < maximum
    require(tuple(arcs) == original, "input mutated")
    counts["graph_profiles"] += 1


def main():
    counts = Counter()
    for n in (2, 3, 4):
        universe = list(permutations(range(n), 2))
        for mask in range(1 << len(universe)):
            pairs = [pair for i, pair in enumerate(universe) if mask & (1 << i)]
            for profile in range(2):
                arcs = [Arc(u, v, Fraction(0) if profile == 0 else Fraction((i*3+u+v)%7, (i%3)+1))
                        for i, (u, v) in enumerate(pairs)]
                check_case(n, arcs, 0, n-1, counts)
    rng = random.Random(20261027)
    for _ in range(100):
        n = rng.randrange(5, 8)
        universe = list(permutations(range(n), 2))
        rng.shuffle(universe)
        arcs = [Arc(u, v, Fraction(rng.randrange(6), rng.randrange(1, 5)))
                for u, v in universe[:rng.randrange(0, min(14, len(universe))+1)]]
        source, target = rng.sample(range(n), 2)
        check_case(n, arcs, source, target, counts)
    counts["seeded_graphs"] = 100

    # A cheapest repair can leave a zero-cost circulation in the split flow.
    # The native decoder must remove it while preserving the optimum cost.
    cyclic = [Arc(0, 1, 0), Arc(1, 2, 0), Arc(2, 3, 0),
              Arc(0, 3, 1), Arc(2, 1, 0)]
    oracle = fixed_paths(4, cyclic, 0, 3, 1)
    repaired = oracle.query(failed_arc=0)
    require(repaired.paths[0].arc_ids == (3,), "circulation was not discarded")
    split_support = oracle._flow.flow(oracle._failure(0, None))
    native_support = {oracle._origin[i] for i in split_support if i in oracle._origin}
    require(native_support == {1, 3, 4}, "zero-circulation fixture did not exercise decoder")
    counts["zero_circulation_recovery"] = 1

    # Queries do not invoke searches and do not use the caller's graph again.
    arcs = [Arc(0, 3, 5), Arc(0, 1, 0), Arc(1, 3, 0),
            Arc(0, 2, 1), Arc(2, 3, 0), Arc(3, 0, 0)]
    original = tuple(arcs)
    fixed = fixed_paths(4, arcs, 0, 3, 2)
    maximum = MaximumPathsOracle(4, arcs, 0, 3)
    arcs.clear()
    saved = {name: getattr(unit_flow, name) for name in ("_shortest", "_residual", "_augmentations")}

    def disabled(*args, **kwargs):
        raise AssertionError("query invoked preprocessing")

    for name in saved:
        setattr(unit_flow, name, disabled)
    try:
        paths = enumerate_paths(4, original, 0, 3)
        for edge, vertex in [(None, None), (0, None), (5, None), (None, 1), (None, 2)]:
            costs = optima(paths, edge, vertex)
            check_answer(fixed.query(failed_arc=edge, failed_vertex=vertex), costs.get(2), 2,
                         4, original, 0, 3, fixed.retained, edge, vertex)
            value = max(costs)
            check_answer(maximum.query(failed_arc=edge, failed_vertex=vertex), costs[value], value,
                         4, original, 0, 3, maximum.retained, edge, vertex)
            counts["queries_without_search_or_input"] += 2
    finally:
        for name, function in saved.items():
            setattr(unit_flow, name, function)

    def reject(function):
        try:
            function()
        except ValueError:
            counts["rejections"] += 1
        else:
            raise AssertionError("malformed input accepted")

    for kwargs in ({"failed_arc": True}, {"failed_arc": -1}, {"failed_arc": 6},
                   {"failed_arc": 1.0}, {"failed_vertex": True}, {"failed_vertex": -1},
                   {"failed_vertex": 4}, {"failed_vertex": 0}, {"failed_vertex": 3},
                   {"failed_arc": 1, "failed_vertex": 1}):
        reject(lambda kwargs=kwargs: fixed.query(**kwargs))
        reject(lambda kwargs=kwargs: maximum.query(**kwargs))
    for bad in ([Arc(0, 1, 0), Arc(0, 1, 1)], [Arc(0, 0, 0)],
                [Arc(0, 1, -1)], [Arc(0, 1, 0.5)], [Arc(True, 1, 0)]):
        reject(lambda bad=bad: fixed_paths(2, bad, 0, 1, 1))
    for value in (-1, True, 1.0):
        reject(lambda value=value: fixed_paths(2, [], 0, 1, value))
    for source in (True, 0.0, -1, 2):
        reject(lambda source=source: MaximumPathsOracle(2, [], source, 1))
    reject(lambda: MaximumPathsOracle(2, [], 1, 1))
    print(json.dumps({"status": "pass", **dict(sorted(counts.items())),
                      "scope": "finite original-arc/internal-vertex path packing and compact query realization"}, indent=2))


if __name__ == "__main__":
    main()
