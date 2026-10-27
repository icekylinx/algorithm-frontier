#!/usr/bin/env python3
"""Independent finite support enumeration versus compact residual repairs.

No assertions are disabled by -O: every check uses require(). The enumerator
does not call a residual solver, shortest paths, or the oracle's verifier.
"""
from fractions import Fraction
from itertools import product
import json
from math import isqrt
from pathlib import Path
import random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
from unit_flow import Arc, CompactPaths, MaximumFlowOracle, Residual, fixed_flow
import unit_flow


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def enumerate_flows(n, arcs, source, target):
    feasible = []
    for mask in range(1 << len(arcs)):
        balance = [0] * n
        cost = Fraction(0)
        used = []
        for i, arc in enumerate(arcs):
            if mask >> i & 1:
                used.append(i)
                balance[arc.tail] += 1
                balance[arc.head] -= 1
                cost += arc.cost
        value = balance[source]
        if (value >= 0 and balance[target] == -value
                and all(balance[v] == 0 for v in range(n)
                        if v not in (source, target))):
            feasible.append((value, cost, frozenset(used)))
    return feasible


def verify_flow(n, arcs, value, cost, support, failed, retained):
    require(support is not None and len(support) == len(set(support)), "duplicate IDs")
    require(set(support) <= set(retained), "output outside preserver")
    require(failed not in support, "failed arc survives")
    balance = [0] * n
    total = Fraction(0)
    for i in support:
        require(0 <= i < len(arcs), "non-original record")
        arc = arcs[i]
        balance[arc.tail] += 1
        balance[arc.head] -= 1
        total += arc.cost
    expected = [0] * n
    expected[0], expected[n - 1] = value, -value
    require(balance == expected and total == cost, "output conservation/cost")


def acyclic(n, arcs, support):
    degree = [0] * n
    outgoing = [[] for _ in range(n)]
    for i in support:
        arc = arcs[i]
        degree[arc.head] += 1
        outgoing[arc.tail].append(arc.head)
    queue = [v for v in range(n) if degree[v] == 0]
    for vertex in queue:
        for head in outgoing[vertex]:
            degree[head] -= 1
            if degree[head] == 0:
                queue.append(head)
    return len(queue) == n


def check_case(n, arcs, counters):
    feasible = enumerate_flows(n, arcs, 0, n - 1)
    maximum = max(row[0] for row in feasible)
    oracle = MaximumFlowOracle(n, arcs, 0, n - 1)
    fixed = [fixed_flow(n, arcs, 0, n - 1, value) for value in range(maximum + 1)]
    require(fixed_flow(n, arcs, 0, n - 1, maximum + 1) is None,
            "infeasible original fixed value")
    for value, structure in enumerate(fixed):
        baseline_key = min((cost, len(used)) for val, cost, used in feasible if val == value)
        require((structure.baseline_cost, len(structure.baseline)) == baseline_key,
                "baseline lexicographic optimum")
        require(acyclic(n, arcs, structure.baseline), "baseline support cycle")
        require(not hasattr(structure, "arcs"), "original graph retained")
        for failed in (None, *range(len(arcs))):
            options = [(cost, used) for val, cost, used in feasible
                       if val == value and failed not in used]
            expected = min((cost for cost, _ in options), default=None)
            require(structure.cost(failed) == expected, "fixed cost mismatch")
            result = structure.flow(failed)
            difference = structure.difference(failed)
            if expected is None:
                require(result is None and difference is None, "infeasibility mismatch")
                counters["infeasible_fixed_queries"] += 1
            else:
                verify_flow(n, arcs, value, expected, result, failed, structure.retained)
                require(len(difference.removed) + len(difference.added) <= n,
                        "difference exceeds simple-cycle bound")
                require(set(difference.removed) <= set(structure.baseline), "bad removal")
                require(not set(difference.added) & set(structure.baseline), "bad addition")
                require(set(result) == ((set(structure.baseline) - set(difference.removed))
                                        | set(difference.added)), "difference replay")
                if difference.added and len(difference.removed) > 1:
                    counters["repairs_reversing_other_baseline_arcs"] += 1
            counters["fixed_queries"] += 1
    for failed in (None, *range(len(arcs))):
        options = [(val, cost) for val, cost, used in feasible if failed not in used]
        expected_value = max(val for val, _ in options)
        expected_cost = min(cost for val, cost in options if val == expected_value)
        value, cost, support = oracle.query(failed)
        require((value, cost) == (expected_value, expected_cost), "maximum query mismatch")
        selected = oracle.upper if value == maximum else oracle.lower
        verify_flow(n, arcs, value, cost, support, failed, selected.retained)
        if value < maximum:
            counters["maximum_value_drops"] += 1
        counters["maximum_queries"] += 1
    counters["graphs"] += 1


def check_hubs():
    # Signed costs from a potential transformation of positive rational costs.
    # All simple paths in this bidirected chain have an independent known optimum.
    n = 96
    arcs = []
    for vertex in range(n - 1):
        arcs.append(Residual(vertex, vertex + 1, Fraction(1, 3) - 2,
                             1, len(arcs), 1))
        arcs.append(Residual(vertex + 1, vertex, Fraction(2, 3) + 2,
                             1, len(arcs), 1))
    demands = {i: (i, i + 60) for i in range(36)}
    demands[36] = (80, 10)
    demands[37] = (12, 12)
    compact = CompactPaths(n, tuple(arcs), demands)
    require(compact.hubs, "hub branch untested")
    for key, (source, target) in demands.items():
        path = compact.report(key)
        vertices = [source, *(a.head for a in path)]
        require(len(vertices) == len(set(vertices)), "hub path repeats vertex")
        require(vertices[-1] == target, "hub target")
        require(all(a.tail == u for u, a in zip(vertices, path)), "hub continuity")
        delta = target - source
        expected = delta * (Fraction(1, 3) - 2) if delta >= 0 else -delta * (Fraction(2, 3) + 2)
        require(sum((a.cost for a in path), Fraction(0)) == expected, "hub distance")
        require(len(path) == abs(delta), "minimum-hop hub route")
    for count, length, initial_long, selections, remaining in compact.phase_counts:
        require(selections <= (n + length - 1) // length, "hub budget")
        require(2 * remaining <= initial_long, "phase does not halve long paths")
    require(compact.record_count() <= 16 * (len(demands) + n * (isqrt(len(demands)) + 1)),
            "compact record envelope")
    unreachable = CompactPaths(3, (), {0: (0, 1)})
    require(unreachable.report(0) is None, "unreachable descriptor")
    return {"demands": len(demands), "hubs": len(compact.hubs),
            "records": compact.record_count(), "phases": len(compact.phase_counts)}


def check_invalid_inputs():
    cases = [(2, [Arc(0, 1, 0.5)], 0, 1, 1),
             (2, [Arc(0, 1, -1)], 0, 1, 1),
             (2, [Arc(0, 0, 1)], 0, 1, 0),
             (2, [], 0, 0, 0), (2, [], 0, 1, -1), (2, [], True, 1, 0), (2, [], 0.5, 1, 0)]
    for args in cases:
        try:
            fixed_flow(*args)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid input accepted")
    structure = fixed_flow(2, [Arc(0, 1, 1)], 0, 1, 1)
    for failed in (-1, 1, True, (0, 1)):
        try:
            structure.flow(failed)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid or multiple failure accepted")
    try:
        CompactPaths(2, (Residual(0, 1, Fraction(-1), 1, 0, 1),
                         Residual(1, 0, Fraction(0), 1, 1, 1)), {0: (0, 1)})
    except ValueError:
        pass
    else:
        raise AssertionError("negative cycle accepted")
    return len(cases) + 5


def check_queries_without_search():
    arcs = [Arc(0, 1, Fraction(1, 3)), Arc(1, 3, 0),
            Arc(0, 2, 1), Arc(2, 3, 0)]
    fixed = fixed_flow(4, arcs, 0, 3, 1)
    maximum = MaximumFlowOracle(4, arcs, 0, 3)
    arcs.clear()
    names = ("_shortest", "_augmentations", "_residual")
    originals = {name: getattr(unit_flow, name) for name in names}

    def forbidden(*args, **kwargs):
        raise AssertionError("query invoked optimization or residual construction")

    try:
        for name in names:
            setattr(unit_flow, name, forbidden)
        for failed in (None, 0, 1, 2, 3):
            expected = Fraction(1) if failed in (0, 1) else Fraction(1, 3)
            require(fixed.cost(failed) == expected, "search-free cost")
            require(fixed.difference(failed).cost == expected, "search-free difference")
            require(fixed.flow(failed) == ((2, 3) if failed in (0, 1) else (0, 1)),
                    "search-free flow")
            value, cost, _ = maximum.query(failed)
            require(value == (2 if failed is None else 1), "search-free maximum value")
            require(cost == (Fraction(4, 3) if failed is None else expected),
                    "search-free maximum cost")
    finally:
        for name, original in originals.items():
            setattr(unit_flow, name, original)
    return 20


def main():
    counters = dict.fromkeys(("graphs", "fixed_queries", "maximum_queries",
                              "infeasible_fixed_queries", "maximum_value_drops",
                              "repairs_reversing_other_baseline_arcs"), 0)
    # Every loopless digraph on four vertices, including antiparallel arcs.
    edges = tuple((u, v) for u in range(4) for v in range(4) if u != v)
    profiles = (tuple(Fraction(0) for _ in edges),
                tuple(Fraction((i * 5 + 3) % 7, (i % 3) + 1) for i in range(len(edges))))
    for costs in profiles:
        for bits in product((0, 1), repeat=len(edges)):
            arcs = tuple(Arc(u, v, costs[i]) for i, (u, v) in enumerate(edges) if bits[i])
            check_case(4, arcs, counters)
    exhaustive = counters["graphs"]
    generator = random.Random(20261027)
    for _ in range(150):
        n = generator.randrange(2, 8)
        arcs = []
        for _ in range(generator.randrange(1, 13)):
            tail = generator.randrange(n)
            head = generator.randrange(n - 1)
            head += head >= tail
            arcs.append(Arc(tail, head, Fraction(generator.randrange(9), generator.randrange(1, 8))))
        check_case(n, tuple(arcs), counters)
    require(counters["repairs_reversing_other_baseline_arcs"] > 0,
            "reverse cancellation branch untested")
    print(json.dumps({"status": "pass", "scope": "finite exact unit-flow residual repairs and compact reports",
                      "exhaustive_graph_profiles": exhaustive, "seeded_multigraphs": 150,
                      **counters, "hub_fixture": check_hubs(),
                      "queries_with_search_disabled": check_queries_without_search(),
                      "rejected_invalid_cases": check_invalid_inputs()}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
