#!/usr/bin/env python3
"""Independent exact packing/context checks for the product-feature reference.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
"""
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import importlib.util
import random
import sys

PATH = Path(__file__).resolve().parents[1] / "reference" / "packing_summary.py"
spec = importlib.util.spec_from_file_location("packing_summary", PATH)
backend = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = backend
spec.loader.exec_module(backend)
Item = backend.Item
counts = dict(instances=0, constructed=0, positive_feature_runs=0, gates=0, failures=0, contexts=0,
              optimum_comparisons=0, replacements=0, rejections=0)


def subsets(values, budget):
    values = tuple(values)
    return [frozenset(s) for k in range(min(budget, len(values)) + 1)
            for s in combinations(values, k)]


def independent(columns):
    # Independent column-oriented elimination with a fresh dense matrix.
    if not columns:
        return True
    matrix = [list(map(Fraction, row)) for row in zip(*columns)]
    r = 0
    for j in range(len(columns)):
        pivot = next((i for i in range(r, len(matrix)) if matrix[i][j]), None)
        if pivot is None:
            return False
        matrix[r], matrix[pivot] = matrix[pivot], matrix[r]
        divisor = matrix[r][j]
        matrix[r] = [x / divisor for x in matrix[r]]
        for i in range(len(matrix)):
            if i != r:
                factor = matrix[i][j]
                matrix[i] = [a - factor * b for a, b in zip(matrix[i], matrix[r])]
        r += 1
    return True


def check(items, k, hv=0, budgets=(), resource=None, backgrounds=((),)):
    answer = backend.summarize(items, k, hv, budgets, resource)
    counts['instances'] += 1
    counts['gates' if answer.gated else 'constructed'] += 1
    if not answer.gated and answer.feature_rank:
        counts['positive_feature_runs'] += 1
    assert len(set(answer.retained)) == len(answer.retained)
    assert len(answer.retained) <= min(len(items), answer.dimension_bound)
    assert all(0 <= i < len(items) for i in answer.retained)
    if not answer.gated:
        assert answer.feature_rank == len(answer.retained)
    universe = {x for item in items for x in item.support}
    palettes = [{x for item in items for x in item.labels[j]} for j in range(len(budgets))]
    selections = [tuple(s) for size in range(min(k, len(items)) + 1)
                  for s in combinations(range(len(items)), size)]
    retained = set(answer.retained)

    def feasible(selection, failed_universe, failed_labels, background):
        used = set()
        for i in selection:
            item = items[i]
            support = set(item.support)
            if used & support or support & failed_universe:
                return False
            used |= support
            if any(set(labels) & failed for labels, failed in zip(item.labels, failed_labels)):
                return False
        return resource is None or independent([resource[i] for i in selection] + list(background))

    for failed_universe in subsets(universe, hv):
        for failed_labels in product(*(subsets(palette, h) for palette, h in zip(palettes, budgets))):
            counts['failures'] += 1
            for background in backgrounds:
                counts['contexts'] += 1
                all_opt, reduced_opt = {}, {}
                for selection in selections:
                    if not feasible(selection, failed_universe, failed_labels, background):
                        continue
                    cost = sum((items[i].cost for i in selection), Fraction(0))
                    size = len(selection)
                    all_opt[size] = min(cost, all_opt.get(size, cost))
                    if set(selection) <= retained:
                        reduced_opt[size] = min(cost, reduced_opt.get(size, cost))
                    # Test the stronger pointwise replacement, keeping the full context.
                    for protected in selection:
                        other = tuple(i for i in selection if i != protected)
                        assert any(candidate not in other
                                   and items[candidate].cost <= items[protected].cost
                                   and feasible(other + (candidate,), failed_universe,
                                                failed_labels, background)
                                   for candidate in retained)
                        counts['replacements'] += 1
                assert all_opt == reduced_opt, (items, answer, failed_universe, failed_labels, background)
                counts['optimum_comparisons'] += min(k, len(items)) + 1
    return answer


def main():
    rng = random.Random(20261027)
    # Complete small support families with private empty-set padding, signed ties,
    # rational resource ranks and failed universe elements.
    supports = [(), (0,), (1,), (0, 1)]
    for assignment in product(supports, repeat=3):
        for k in (0, 1, 2):
            items = [Item(s, Fraction(i - 1, 2)) for i, s in enumerate(assignment)]
            check(items, k, hv=1)
    for _ in range(55):
        n = rng.randrange(5, 12)
        items = [Item(tuple(sorted(rng.sample(range(4), rng.randrange(3)))),
                      Fraction(rng.randrange(-4, 5), rng.randrange(1, 4)),
                      (tuple(sorted(rng.sample(range(3), rng.randrange(3)))),))
                 for _ in range(n)]
        check(items, rng.randrange(1, 3), rng.randrange(2), (rng.randrange(2),))
    # Force a genuinely reduced exterior construction, including parallel edges.
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)] * 3
    items = [Item(edge, Fraction((7 * i) % 11 - 5, 3)) for i, edge in enumerate(edges)]
    assert not check(items, 2, hv=1).gated
    # Two independent label systems; repetitions are original IDs, not merged.
    items = [Item((i % 2,), Fraction(i % 5 - 2), ((i % 2,), ((i // 2) % 2,)))
             for i in range(20)]
    assert not check(items, 1, budgets=(1, 1)).gated
    # Rational resource rank compression and represented later extensions.
    # Original positive columns span a proper subspace; background is fixed
    # in the larger space and may interact with the positive flat.
    resource = [(1, i % 3, 0, 2 + 2 * (i % 3)) for i in range(19)]
    backgrounds = ((), ((1, 0, 0, 2),), ((0, 0, 1, 0),),
                   ((1, 0, 1, 2), (0, 0, 1, 0)),
                   ((1, 0, 0, 2), (1, 0, 0, 2)))
    items = [Item((i % 3,), Fraction(i % 7 - 3, 2), ((i % 2,),)) for i in range(19)]
    assert not check(items, 2, hv=0, budgets=(1,), resource=resource,
                     backgrounds=backgrounds).gated
    for _ in range(25):
        items = [Item((rng.randrange(3),), Fraction(rng.randrange(-3, 4), 2),
                      ((rng.randrange(3),),)) for _ in range(16)]
        resource = [(rng.randrange(3), rng.randrange(3), 0) for _ in items]
        check(items, 2, budgets=(1,), resource=resource,
              backgrounds=((), ((1, 0, 0),), ((0, 0, 1),)))
    # Loops and rank zero, empty universe and empty failure palettes.
    check([Item((), -1), Item((), -2), Item((), 0)], 2,
          resource=[(0,), (0,), (0,)])
    check([Item((), -1), Item((), -2), Item((), 0)], 2)
    check([Item((0,), 0, ((),)), Item((0,), -1, ((),))], 1, budgets=(10**30,))
    check([], 2)
    # Feature enumeration must never occur in the identity branch, including
    # binary huge budgets and very wide explicit supports.
    original = backend._det
    backend._det = lambda *_: (_ for _ in ()).throw(AssertionError("feature work before gate"))
    try:
        answer = backend.summarize([Item((0, 1), 0), Item((1, 2), 0)], 10**100, 10**100)
        assert answer.gated and answer.retained == (0, 1)
    finally:
        backend._det = original
    bad = [lambda: backend.summarize([Item((0, 0), 0)], 1),
           lambda: backend.summarize([Item((-1,), 0)], 1),
           lambda: backend.summarize([Item((True,), 0)], 1),
           lambda: backend.summarize([Item((0,), 0.5)], 1),
           lambda: backend.summarize([Item((0,), 0)], -1),
           lambda: backend.summarize([Item((0,), 0)], True),
           lambda: backend.summarize([Item((0,), 0)], 1, label_failures=(1,)),
           lambda: backend.summarize([Item((0,), 0, ((1, 1),))], 1, label_failures=(1,)),
           lambda: backend.summarize([Item((0,), 0)], 1, resource_columns=[]),
           lambda: backend.summarize([Item((0,), 0)], 1, resource_columns=[(0.5,)]),
           lambda: backend.summarize([Item((0,), 0), Item((1,), 0)], 1,
                                     resource_columns=[(1,), (1, 2)])]
    for call in bad:
        try:
            call()
        except ValueError:
            counts['rejections'] += 1
        else:
            raise AssertionError("invalid input accepted")
    print("PASS product-feature packing summary:", ', '.join(f'{k}={v}' for k, v in counts.items()))


if __name__ == '__main__':
    main()
