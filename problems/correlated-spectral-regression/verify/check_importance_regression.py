#!/usr/bin/env python3
"""Independent exact determinant/normal-equation checks; no sampling trials.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
"""
from dataclasses import replace
from fractions import Fraction as Q
from itertools import combinations, permutations, product
import json
from pathlib import Path
import random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
import importance as impl
import regression as ridge


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def subsets(values, bound=None):
    values = tuple(values)
    for size in range(min(len(values), bound if bound is not None else len(values)) + 1):
        yield from combinations(values, size)


def determinant(a):
    n = len(a)
    result = Q(0)
    for order in permutations(range(n)):
        term = Q((-1) ** sum(order[i] > order[j] for i in range(n) for j in range(i + 1, n)))
        for i, j in enumerate(order):
            term *= a[i][j]
        result += term
    return result


def inverse(a):
    n, det = len(a), determinant(a)
    require(bool(det), "independent inverse received singular matrix")
    return tuple(tuple(Q((-1) ** (i + j)) * determinant(
        tuple(tuple(a[u][v] for v in range(n) if v != i) for u in range(n) if u != j)) / det
        for j in range(n)) for i in range(n))


def transpose(a):
    return tuple(zip(*a))


def matmul(a, b):
    columns = tuple(zip(*b))
    return tuple(tuple(sum((x * y for x, y in zip(row, column)), Q(0))
                       for column in columns) for row in a)


def mp_inverse(a):
    """Independent range-coordinate Moore--Penrose inverse using cofactors."""
    n, selected = len(a), []
    for j in range(n):
        candidate = selected + [j]
        u = tuple(tuple(a[i][k] for k in candidate) for i in range(n))
        if determinant(matmul(transpose(u), u)):
            selected = candidate
    if not selected:
        return tuple((Q(0),) * n for _ in range(n))
    u = tuple(tuple(a[i][j] for j in selected) for i in range(n))
    left = matmul(inverse(matmul(transpose(u), u)), transpose(u))
    reduced = matmul(matmul(left, a), transpose(left))
    return matmul(matmul(transpose(left), inverse(reduced)), left)


def gram(vectors, n):
    return tuple(tuple(sum((Q(v[i]) * Q(v[j]) for v in vectors), Q(0))
                       for j in range(n)) for i in range(n))


def original_sum(instance, ids, background=True):
    n = instance.dimension
    return tuple(tuple((instance.background[i][j] if background else Q(0))
                       + sum((instance.matrices[e][i][j] for e in ids), Q(0))
                       for j in range(n)) for i in range(n))


def independent_masses(instance, ids):
    inverse = mp_inverse(original_sum(instance, ids))
    return tuple(sum((a[i][j] * inverse[j][i] for i in range(instance.dimension)
                      for j in range(instance.dimension)), Q(0)) if e in ids else Q(0)
                 for e, a in enumerate(instance.matrices))


def check_importance(counts):
    rng = random.Random(271032)
    for fixture in range(24):
        n = 2 + fixture % 2
        matrices = tuple(gram(tuple(tuple(Q(rng.randrange(-1, 2), 2) for _ in range(n))
                                    for _ in range(i % 3)), n) for i in range(4))
        background = gram(((1, 1) + ((0,) if n == 3 else ()),), n) if fixture % 3 else None
        instance = impl.PSDInstance(matrices, ({0}, {1}, {0, 2}, set()), background)
        original = independent_masses(instance, tuple(range(4)))
        cache = {}
        for ids in subsets(range(4)):
            cert = instance.masses(ids)
            expected = independent_masses(instance, ids)
            require(instance.verify_masses(cert) and cert.masses == expected,
                    "rational generalized-inverse traces differ from Moore--Penrose traces")
            require(cert.total <= sum(original, Q(0)), "effective dimension increased on restriction")
            cache[ids] = expected
            counts["subset_mass_certificates"] += 1
        for small, large in product(cache, repeat=2):
            if set(small) <= set(large):
                for e in small:
                    require(cache[small][e] >= cache[large][e], "deletion monotonicity failed")
                    counts["monotonicity_comparisons"] += 1
        one = instance.one_failure()
        require(instance.verify_one_failure(one), "one-failure accounting certificate failed")
        for e in range(4):
            require(one.scores[e] == max(independent_masses(instance, instance.survivors(f))[e]
                                        for f in ((), (0,), (1,), (2,))),
                    "single-failure maximum differs")
            counts["one_failure_maxima"] += 1
        all_pools = tuple(frozenset(p) for p in subsets(instance.universe))
        for pools in (*((pool,) for pool in all_pools), all_pools):
            scores = instance.pool_scores(2, pools)
            require(instance.verify_pool_scores(scores), "deterministic pool mass ledger failed")
            counts["supplied_pool_outcomes"] += 1
            for failed in subsets(instance.universe, 2):
                expected = independent_masses(instance, instance.survivors(failed))
                for e, labels in enumerate(instance.labels):
                    if labels & set(failed):
                        continue
                    protected = sum(labels <= pool and not set(failed) & pool for pool in pools)
                    if protected >= Q(len(pools), 2) / scores.gamma:
                        require(scores.scores[e] >= expected[e], "coverage implication failed")
                        counts["protected_pair_domination_checks"] += 1
        counts["psd_instances"] += 1
    # A poor pool can fail domination while retaining the deterministic mass bound.
    bad = impl.PSDInstance((((1,),),) * 50, ({1},) + ({0},) * 49)
    scores = bad.pool_scores(1, ({0, 1},))
    require(bad.verify_pool_scores(scores) and scores.scores[0] < bad.masses((0,)).masses[0],
            "bad-pool fixture must not be reported as universal domination")
    counts["certified_bad_pool_examples"] += 1
    # The manuscript's exact obstruction to random additive-order coupling.
    vectors = ((1, -10), (1, 10), (2, -10), (3, 15))
    obstruction = impl.PSDInstance(tuple(gram((v,), 2) for v in vectors), ({0}, {1}, {2}, {3}))
    chosen = ((1, (0, 1, 2), Q(13, 14)), (0, (0, 1, 3), Q(97, 106)),
              (3, (0, 2, 3), Q(225, 229)), (2, (1, 2, 3), Q(20, 21)))
    require(all(obstruction.masses(ids).masses[e] == value for e, ids, value in chosen),
            "rank-two coupling obstruction values changed")
    require(sum((value for _, _, value in chosen), Q(0)) == Q(963073, 254877) > 3,
            "coupling obstruction sum changed")
    counts["exact_obstruction_marginals"] += 4


def check_regression(counts):
    rng = random.Random(271033)
    for fixture in range(12):
        a = tuple(tuple(Q(rng.randrange(-2, 3), 2) for _ in range(2)) for _ in range(5))
        b = tuple(tuple(Q(rng.randrange(-2, 3), 3) for _ in range(2)) for _ in range(5))
        reg = ridge.Regression(a, b, ({0}, {1}, {0, 2}, set(), {2}), Q(fixture % 2, 2))
        design_gram = gram(a, 2)
        response_gram = gram(b, 2)
        regularized_design = tuple(tuple(design_gram[i][j]
                                          + (reg.base_regularization if i == j else 0)
                                          for j in range(2)) for i in range(2))
        design_inverse, response_inverse = mp_inverse(regularized_design), mp_inverse(response_gram)
        sd = sum((design_gram[i][j] * design_inverse[j][i] for i in range(2) for j in range(2)), Q(0))
        response_rank = sum((response_gram[i][j] * response_inverse[j][i]
                             for i in range(2) for j in range(2)), Q(0))
        require(reg.psd.masses().total <= sd + response_rank, "augmented effective dimension exceeded bound")
        counts["effective_dimension_bounds"] += 1
        weights = tuple(Q(8 + rng.randrange(-1, 2), 8) for _ in range(5))
        transforms = (((1,), (0,)), ((0, 1), (1, 1)), ((2, -1), (-1, Q(1, 2))))
        for failed in subsets((0, 1, 2), 2):
            require(reg.psd.verify_embedding(weights, failed, Q(1, 4)), "known row sandwich rejected")
            counts["all_vector_embedding_checks"] += 1
            for transform, regularization in product(transforms, (reg.base_regularization, Q(2))):
                original = reg.solve(transform, regularization, failed)
                sketched = reg.solve(transform, regularization, failed, weights)
                require(reg.verify_solution(original, transform, regularization, failed)
                        and reg.verify_solution(sketched, transform, regularization, failed, weights),
                        "normal-equation optimum certificate rejected")
                hessian, rhs = reg.normal_equations(transform, regularization, failed)
                independent = matmul(mp_inverse(hessian), rhs)
                require(reg.objective(independent, transform, regularization, failed)
                        == reg.objective(original, transform, regularization, failed),
                        "independent original ridge optimum differs")
                true_value = reg.objective(sketched, transform, regularization, failed)
                optimum = reg.objective(independent, transform, regularization, failed)
                require((1 - Q(1, 4) ** 2) * true_value <= optimum,
                        "weak-regression bilinear bound failed")
                counts["ridge_query_comparisons"] += 1
        counts["regression_instances"] += 1
    # Singular designs, zero response space, zero variables and zero-row input.
    for a, b, labels in ((((1, 1), (2, 2)), ((1,), (2,)), ({0}, {1})),
                          (((0,),), ((0,),), (set(),)),
                          (((),), ((1,),), (set(),)),
                          (((1,),), ((),), (set(),)),
                          ((), (), ())):
        reg = ridge.Regression(a, b, labels)
        transform = ((1,),) if reg.q else ()
        x = reg.solve(transform, 0)
        require(reg.verify_solution(x, transform, 0), "degenerate ridge certificate rejected")
        counts["degenerate_regression_queries"] += 1


def check_guards(counts):
    small = impl.PSDInstance((((1,),),), ({0},), ((1 << 200,),))
    empty = small.plan(1, Q(1, 4), Q(1, 4))
    require(empty.mode == "EMPTY" and small.verify_embedding(empty.weights, (), Q(1, 4)),
            "small-effective-dimension empty gate failed")
    huge = impl.PSDInstance((((1,),),), (set(range(100)),))
    full = huge.plan(10**100, Q(1, 4), Q(1, 4))
    require(full.mode == "FULL_INPUT" and full.pool_count == 0
            and full.gamma > 10**50 and huge.verify_embedding(full.weights),
            "whole-input gate failed before oversized pools")
    for labelled, mode in ((True, "POOLS_NEEDED"), (False, "ORDINARY_SCORES")):
        n = 4096
        instance = impl.PSDInstance((((1,),),) * n,
                                    tuple({i % 2} if labelled else set() for i in range(n)),
                                    ((3 * n // 4,),))
        plan = instance.plan(1, Q(1, 2), Q(1, 4))
        require(plan.mode == mode and plan.weights is None and plan.sample_cap < n,
                "nontrivial planner claimed a sampled summary")
    counts["planner_branches"] += 4
    instance = impl.PSDInstance((((1, 1), (1, 1)), ((1, 0), (0, 0))), ({0}, set()))
    mass, one, pools = instance.masses(), instance.one_failure(), instance.pool_scores(1, ((), (0,)))
    reg = ridge.Regression(((1,), (2,)), ((1,), (0,)), ({0}, set()))
    x = reg.solve(((1,),), 0)
    saved = impl.generalized_inverse, impl.PSDInstance.masses, ridge.solve

    def unavailable(*args, **kwargs):
        raise AssertionError("certificate verifier called its producer/solver")

    try:
        impl.generalized_inverse = impl.PSDInstance.masses = ridge.solve = unavailable
        require(instance.verify_masses(mass) and instance.verify_one_failure(one)
                and instance.verify_pool_scores(pools) and reg.verify_solution(x, ((1,),), 0),
                "search-free verifier failed")
        counts["producer_disabled_verifiers"] += 4
    finally:
        impl.generalized_inverse, impl.PSDInstance.masses, ridge.solve = saved
    forged = (replace(mass, inverse=((0, 0), (0, 0))),
              replace(mass, masses=(mass.masses[0] + 1, mass.masses[1])),
              replace(mass, items=(0, 0)), replace(mass, masses=(1.0, 1.0)))
    require(all(not instance.verify_masses(c) for c in forged), "forged mass certificate accepted")
    require(not instance.verify_one_failure(replace(one, scores=(0, 0)))
            and not instance.verify_pool_scores(replace(pools, gamma=1)),
            "forged robust score certificate accepted")
    require(not reg.verify_solution(((100,),), ((1,),), 0)
            and not reg.psd.verify_embedding((0, 0), error=Q(1, 4)),
            "forged regression certificate accepted")
    counts["forged_certificate_rejections"] += 8
    invalid = (
        lambda: impl.PSDInstance((((0, 1), (1, 0)),), (set(),)),
        lambda: impl.PSDInstance((((1, 0), (1, 1)),), (set(),)),
        lambda: impl.PSDInstance((((-1,),),), (set(),)),
        lambda: impl.PSDInstance((((1.0,),),), (set(),)),
        lambda: impl.PSDInstance((((1,),),), ()),
        lambda: impl.PSDInstance((((1,),),), ({-1},)),
        lambda: instance.plan(-1, Q(1, 4), Q(1, 4)),
        lambda: instance.plan(1, 0, Q(1, 4)),
        lambda: instance.pool_scores(1, ()),
        lambda: instance.masses((0, 0)),
        lambda: ridge.Regression(((1,),), ((1,),), (set(),), -1),
        lambda: reg.solve(((1,),), -1),
        lambda: reg.solve(((1,), (1,)), 0),
    )
    for thunk in invalid:
        try:
            thunk()
        except ValueError:
            counts["malformed_input_rejections"] += 1
        else:
            raise AssertionError("malformed input accepted")


def main():
    names = ("psd_instances", "subset_mass_certificates", "monotonicity_comparisons",
             "one_failure_maxima", "supplied_pool_outcomes", "protected_pair_domination_checks",
             "certified_bad_pool_examples", "exact_obstruction_marginals", "regression_instances",
             "effective_dimension_bounds",
             "all_vector_embedding_checks", "ridge_query_comparisons", "degenerate_regression_queries",
             "planner_branches", "producer_disabled_verifiers", "forged_certificate_rejections",
             "malformed_input_rejections")
    counts = dict.fromkeys(names, 0)
    check_importance(counts)
    check_regression(counts)
    check_guards(counts)
    print(json.dumps({"status": "pass", "importance_regression": counts}, indent=2))


if __name__ == "__main__":
    main()
