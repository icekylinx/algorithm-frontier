"""Initialized exact ordinary two-matroid single-element-failure reporting.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0

The canonical weighted-intersection implementation supplies the baseline.
The existing distance/hub reporter supplies the final compact oracle. Neither
original independence callbacks nor ground-sized initializer certificates are
retained in that oracle. This does not implement valuated matroids.
"""
from fractions import Fraction
from pathlib import Path
import importlib.util
import sys

import arborescence_reporting as reporting


_name = "_algorithm_frontier_bounded"
if _name not in sys.modules:
    _path = (Path(__file__).resolve().parents[2]
             / "robust-bounded-certificates/reference/bounded.py")
    _spec = importlib.util.spec_from_file_location(_name, _path)
    _module = importlib.util.module_from_spec(_spec)
    sys.modules[_name] = _module
    _spec.loader.exec_module(_module)
weighted = sys.modules[_name]


def _baseline(costs, rank, independent1, independent2):
    """Initialize and verify before discarding every ground-sized record."""
    if rank > len(costs):
        return None
    certificate = weighted.minimum_cost(independent1, independent2, costs, rank)
    if not weighted.verify_intersection(independent1, independent2, costs, rank, certificate):
        raise RuntimeError("weighted initialization certificate failed")
    if len(certificate.chosen) < rank:
        return None
    return certificate.chosen


def _compressed(costs, baseline, independent1, independent2):
    """Cheapest original label per ordered pair, including exchange loops."""
    chosen = frozenset(baseline)
    candidates = {}
    for e in range(len(costs)):
        if e in chosen:
            continue
        first = tuple(a for a in baseline if independent1((chosen - {a}) | {e}))
        second = tuple(b for b in baseline if independent2((chosen - {b}) | {e}))
        for a in first:
            for b in second:
                old = candidates.get((a, b))
                if old is None or (costs[e], e) < (costs[old], old):
                    candidates[a, b] = e
    minus = {a: 2 * j for j, a in enumerate(baseline)}
    plus = {a: node + 1 for a, node in minus.items()}
    arcs = [reporting._AuxArc(minus[a], plus[a], (Fraction(0), 0)) for a in baseline]
    arcs.extend(reporting._AuxArc(plus[a], minus[b], (costs[e] - costs[a], 1),
                                  label=e, removed=a)
                for (a, b), e in sorted(candidates.items()))
    return tuple(arcs), minus, plus


def build(costs, rank, independent1, independent2):
    """Return a compact fixed-rank oracle, or None if no initial solution exists.

    Original IDs are range(len(costs)); signed integer/Fraction costs are
    fixed between independent failure queries. Both callables must be valid
    ordinary matroid independence oracles on frozensets of original IDs.
    Rank zero has the empty optimum. No supplied baseline is required.
    """
    costs = tuple(weighted.rational(x) for x in costs)
    if (type(rank) is not int or rank < 0
            or not callable(independent1) or not callable(independent2)):
        raise ValueError("nonnegative rank and two independence callbacks required")
    baseline = _baseline(costs, rank, independent1, independent2)
    if baseline is None:
        return None
    arcs, minus, plus = _compressed(costs, baseline, independent1, independent2)
    return reporting._finish(baseline, sum((costs[a] for a in baseline), Fraction(0)),
                             2 * rank, arcs, minus, plus)


def build_arborescence(n, root, arcs):
    """Initialize a nonnegative-cost rooted graph, then use its sparse HLD lift.

    Original arc IDs are input-list positions. Loops and root-entering arcs
    are loops of both oracle matroids. None means no rooted spanning tree.
    This wrapper has polynomial weighted-intersection initialization cost,
    not the manuscript's faster arborescence preprocessing bound.
    """
    arcs = reporting._graph_input(n, root, arcs)

    def graphic(chosen):
        parent = {}

        def find(v):
            parent.setdefault(v, v)
            while parent[v] != v:
                v = parent[v]
            return v

        for i in chosen:
            arc = arcs[i]
            if arc.head == root or arc.tail == arc.head:
                return False
            a, b = find(arc.tail), find(arc.head)
            if a == b:
                return False
            parent[a] = b
        return True

    def partition(chosen):
        heads = set()
        for i in chosen:
            arc = arcs[i]
            if arc.head == root or arc.head in heads or arc.tail == arc.head:
                return False
            heads.add(arc.head)
        return True

    baseline = _baseline(tuple(a.cost for a in arcs), n - 1, graphic, partition)
    return None if baseline is None else reporting.build(n, root, arcs, baseline)


class MaximumOracle:
    """Two compact fixed-rank reporters; original callbacks are not retained."""
    def __init__(self, primary, fallback):
        self.primary, self.fallback = primary, fallback
        self.rank = len(primary.baseline)
        self.support = tuple(sorted(set(primary.support) | set(() if fallback is None else fallback.support)))

    @property
    def record_count(self):
        return (1 + len(self.support) + self.primary.record_count
                + (0 if self.fallback is None else self.fallback.record_count))

    def _oracle(self, failed):
        return (self.primary if self.primary.optimum_cost(failed) is not None
                else self.fallback)

    def query(self, failed=None):
        """Minimum-cost maximum-cardinality common set after one deletion."""
        oracle = self._oracle(failed)
        if oracle is None:
            raise RuntimeError('one deletion dropped ordinary common rank by more than one')
        answer = oracle.query(failed)
        if answer is None:
            raise RuntimeError('consecutive-rank fallback was unexpectedly infeasible')
        return answer

    def optimum_cost(self, failed=None):
        return self._oracle(failed).optimum_cost(failed)

    def rank_after(self, failed=None):
        return len(self._oracle(failed).baseline)


def build_maximum(costs, independent1, independent2):
    """Initialize ordinary max cardinality, then preserve its exact signed cost.

    Rank drop has a linear-cost objective on both consecutive ranks. This
    interface does not interpret a fixed-rank valuation at any smaller rank.
    """
    costs = tuple(weighted.rational(x) for x in costs)
    if not callable(independent1) or not callable(independent2):
        raise ValueError('two ordinary independence callbacks required')
    certificate = weighted.minimum_cost(independent1, independent2, costs, len(costs))
    if not weighted.verify_intersection(independent1, independent2, costs, len(costs), certificate):
        raise RuntimeError('maximum-cardinality initialization certificate failed')
    baseline = certificate.chosen
    rank = len(baseline)
    arcs, minus, plus = _compressed(costs, baseline, independent1, independent2)
    primary = reporting._finish(baseline, sum((costs[a] for a in baseline), Fraction(0)),
                                2 * rank, arcs, minus, plus)
    fallback = None if rank == 0 else build(costs, rank - 1, independent1, independent2)
    if rank and fallback is None:
        raise RuntimeError('original lower common rank was unavailable')
    return MaximumOracle(primary, fallback)
