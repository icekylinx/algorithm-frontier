#!/usr/bin/env python3
"""Independent finite rank/barrier checks; not an asymptotic oracle proof."""

from fractions import Fraction
from itertools import combinations, product


def require(condition, detail):
    if not condition:
        raise AssertionError(detail)


def rank_axioms(values, q):
    require(values[0] == 0, "normalization")
    require(all(isinstance(v, int) for v in values), "integrality")
    for s in range(1 << q):
        missing = [i for i in range(q) if not s >> i & 1]
        for i in missing:
            require(values[s | 1 << i] >= values[s], "monotonicity")
        # These local inequalities are equivalent to full submodularity.
        for i, j in combinations(missing, 2):
            require(values[s | 1 << i] + values[s | 1 << j]
                    >= values[s] + values[s | 1 << i | 1 << j],
                    "local submodularity")


def feasible(vector, values):
    return all(sum(v for i, v in enumerate(vector) if s >> i & 1) <= bound
               for s, bound in enumerate(values))


def hidden_family():
    families = candidates = duals = refined = 0
    for q in range(2, 8):
        full = (1 << q) - 1
        sizes = [s.bit_count() for s in range(1 << q)]
        for r in range(1, q):
            base = [min(2 * size, 2 * r) - (size == r) for size in sizes]
            rank_axioms(base, q)
            sets = [s for s in range(1 << q) if sizes[s] == r]
            for hidden in sets:
                values = base.copy()
                values[hidden] += 1
                rank_axioms(values, q)
                require(values[full] == 2 * r, "total rank")
                require(sum(a != b for a, b in zip(base, values)) == 1,
                        "unique exceptional query")
                for selected in sets:
                    one = [int(selected >> i & 1) for i in range(q)]
                    two = [2 * v for v in one]
                    require(feasible(one, values), "one-unit basis")
                    require(feasible(two, values) == (selected == hidden),
                            "unique two-unit basis")
                    candidates += 1
                if q >= r + 2:
                    dual = [2 * sizes[s] + values[full ^ s] - 2 * r
                            for s in range(1 << q)]
                    rank_axioms(dual, q)
                    require(all(dual[1 << i] == 2 for i in range(q)),
                            "small-job singleton bound")
                    complement = [2 * int(not (hidden >> i & 1))
                                  for i in range(q)]
                    require(feasible(complement, dual), "dual hidden schedule")
                    require(sum(complement) == dual[full], "dual base total")
                    duals += 1
                if q == 2 * r:
                    require(feasible([1] * q, values), "Boolean cap is free")
                    require(values[full] == q, "compulsory small-resource total")
                    # A free heavy matroid has all q coloops, while its union
                    # with M* is free and its dual has no nonloops.
                    require(all(values[s] >= sizes[s] for s in range(1 << q)),
                            "all subsets Boolean-independent")
                    refined += 1
                families += 1
    return families, candidates, duals, refined


def configuration_gaps():
    aggregate_rows = subset_rows = reserves = greedy_checks = 0
    for r in range(2, 8):
        for multiple in range(1, 7):
            d = r * multiple
            q = d * r
            quota = 1 + d // r
            for s in range(1, q + 1):
                require(Fraction(s * (d + 1), d) <= s + d,
                        "aggregate fractional recipient row")
                aggregate_rows += 1
            for s in range(r + 1):
                require(s * quota <= (s + d if s else 0),
                        "attaining integer quota")
            require(r * (quota + 1) > r + d, "integer quota upper bound")

    for r in range(3, 31):
        q = 2 * r
        f = lambda s: min(s, r - 1) + min(s, r + 1)
        require(f(r) == 2 * r - 1, "integer two-unit obstruction")
        for s in range(q + 1):
            marginal = f(s + 1) - f(s) if s < q else 0
            lhs = Fraction(2 * s + (q - s) * max(0, 2 - marginal), 2)
            require(lhs <= f(s), "full residual subset cut")
            require(f(s) >= s, "aggregate one vector")
            subset_rows += 1

    # Independently enumerate all bounded reserves for r=3; this does not
    # invoke the convexity/subset-equivalence lemma being checked.
    q, r = 6, 3
    full = (1 << q) - 1
    values = [min(s.bit_count(), r - 1) + min(s.bit_count(), r + 1)
              for s in range(1 << q)]
    rank_axioms(values, q)
    for z in product(range(3), repeat=q):
        if not feasible(z, values):
            continue
        margins = [min(values[s] - sum(z[i] for i in range(q) if s >> i & 1)
                       for s in range(1 << q) if s >> p & 1)
                   for p in range(q)]
        require(sum(Fraction(max(0, 2 - a), 2) for a in margins) <= sum(z),
                "direct all-reserve hinge cut")
        first = [int(v == 2) for v in z]
        second = first.copy()
        for p, value in enumerate(z):
            if value == 1:
                if sum(first) < r - 1:
                    first[p] = 1
                else:
                    second[p] = 1
        require(sum(first) <= r - 1 and sum(second) <= r + 1,
                "explicit uniform-component capacities")
        require(all(a + b == v for a, b, v in zip(first, second, z)),
                "explicit uniform-component count decomposition")
        reserves += 1

    # A second direct decomposition, for the free-plus-rank-one example.
    free_rank = [0 if not s else s.bit_count() + 2 for s in range(16)]
    for vector in product(range(4), repeat=4):
        excess = sum(max(0, v - 1) for v in vector)
        require(feasible(vector, free_rank) == (excess <= 2),
                "free-plus-two-rank-one count decomposition")

    # Every order on every subset tests the direct tight-support identity.
    # Repeated greedy vectors are deliberately retained as distinct orders.
    def visit(order, remaining):
        nonlocal greedy_checks
        s = 0
        z = [0] * q
        for i in order:
            z[i] = values[s | 1 << i] - values[s]
            s |= 1 << i
        require(feasible(z, values), "greedy reserve feasibility")
        for p in range(q):
            actual = min(values[a] - sum(z[i] for i in range(q) if a >> i & 1)
                         for a in range(1 << q) if a >> p & 1)
            require(actual == values[s | 1 << p] - values[s],
                    "tight-support residual identity")
            greedy_checks += 1
        for i in range(q):
            if remaining >> i & 1:
                visit(order + (i,), remaining ^ 1 << i)

    visit((), full)
    return aggregate_rows, subset_rows, reserves, greedy_checks


if __name__ == "__main__":
    h, c, d, z = hidden_family()
    a, s, r, g = configuration_gaps()
    print(f"PASS: {h} hidden ranks, {c} basis-quota comparisons, "
          f"{d} dual scheduling ranks, {z} refined-zero instances; "
          f"{a} aggregate rows, {s} residual subset cuts, "
          f"{r} directly enumerated reserves, {g} greedy residual identities.")
