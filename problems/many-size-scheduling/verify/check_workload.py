"""Independent original-count checks of native workload decomposition/rounding.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
The comparator imports no workload, box, dual or LP construction helper.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'reference'))
from workload import WorkloadBackend, decompose, upper_round


def legal(rank, row):
    return (all(x >= 0 for x in row) and sum(row) == rank[-1]
            and all(sum(row[p] for p in range(len(row)) if mask >> p & 1) <= bound
                    for mask, bound in enumerate(rank)))


def bases(rank, q):
    return [row for row in product(*(range(rank[1 << p]+1) for p in range(q))) if legal(rank, row)]


def schedules(ranks, sizes, q):
    return {tuple(rows): max((sum(size*row[p] for size, row in zip(sizes, rows))
                              for p in range(q)), default=F(0))
            for rows in product(*(bases(rank, q) for rank in ranks))}


def uniform(q, n):
    return tuple(0 if mask == 0 else n for mask in range(1 << q))


def fixtures():
    yield 0, (), ()
    yield 2, (), ()
    yield 1, ((0, 0),), (F(100),)
    yield 1, ((0, 3), (0, 1)), (F(1), F(3))
    for rank in ((0, 1, 1, 1), (0, 1, 0, 1), (0, 0, 1, 1), (0, 2, 1, 2)):
        yield 2, (rank, uniform(2, 1)), (F(1), F(3))
        yield 2, (rank, uniform(2, 1), uniform(2, 1)), (F(1, 2), F(1), F(3, 2))
    # Equal largest classes must be decomposed back to their original types.
    yield 2, (uniform(2, 1),)*3, (F(1), F(3), F(3))
    # Zero-rank types with much larger sizes do not change a or rounding loss.
    yield 2, (uniform(2, 1), uniform(2, 1), (0, 0, 0, 0)), (F(1), F(3), F(100))
    # A full target at three is feasible, but rank-budget one cap fails there.
    yield 3, (uniform(3, 3), tuple(min(mask.bit_count(), 2) for mask in range(8))), (F(1), F(3))
    # Original large-loop machines remain useful to smaller resources.
    yield 3, (uniform(3, 3), (0, 1, 0, 1, 0, 1, 0, 1)), (F(1), F(3))


def check_native(counts):
    tables = ((0, 1, 1, 1), (0, 1, 0, 1), (0, 2, 1, 2), (0, 1, 1, 2))
    for ranks in product(tables, repeat=2):
        for multipliers in ((1, 1), (2, 3), (3, 2)):
            scaled = tuple(tuple(v*m for v in rank) for rank, m in zip(ranks, multipliers))
            expected = {tuple(sum(row[p] for row in rows) for p in range(2))
                        for rows in product(*(bases(rank, 2) for rank in scaled))}
            aggregate = tuple(sum(row[s] for row in scaled) for s in range(4))
            for workload in bases(aggregate, 2):
                assert workload in expected
                output = decompose(ranks, multipliers, workload)
                assert all(legal(rank, row) for rank, row in zip(scaled, output))
                assert all(sum(row[p] for row in output) == workload[p] for p in range(2))
                counts['scaled_decompositions'] += 1
        all_original = list(schedules(ranks, (F(1), F(2)), 2))
        for first in all_original[:3]:
            for last in all_original[-3:]:
                fractional = tuple(tuple(F(x+y, 2) for x, y in zip(a, b)) for a, b in zip(first, last))
                output = upper_round(ranks, (1, 2), fractional, 2)
                assert output in all_original
                for p in range(2):
                    before = sum(size*row[p] for size, row in zip((1, 2), fractional))
                    after = sum(size*row[p] for size, row in zip((1, 2), output))
                    assert after <= before+2
                    for prefix in ((1,), (1, 0)):
                        total = sum(fractional[j][p] for j in prefix)
                        assert sum(output[j][p] for j in prefix) <= -(-total//1)
                counts['upper_roundings'] += 1
    huge = 1 << 80
    ranks = (uniform(2, 1),)*2
    output = decompose(ranks, (huge, 2*huge), (1, 3*huge-1))
    assert all(legal(tuple(v*m for v in rank), row) for rank, m, row in zip(ranks, (huge, 2*huge), output))
    fractional = tuple(tuple(F(x, m) for x in row) for row, m in zip(output, (huge, 2*huge)))
    assert any(x.denominator >= huge for row in fractional for x in row)
    rounded = upper_round(ranks, (1, 2), fractional, 2)
    assert all(legal(rank, row) for rank, row in zip(ranks, rounded))
    for p in range(2):
        assert sum(size*row[p] for size, row in zip((1, 2), rounded)) <= sum(
            size*row[p] for size, row in zip((1, 2), fractional))+2
    counts['binary_checks'] += 2
    # Binary original multiplicity passes all-job LP/rounding and optimization.
    solver = WorkloadBackend(1, ((0, huge), (0, 1)), (1, 3))
    assert solver.optimize() == ((huge,), (1,))
    counts['binary_checks'] += 1
    solver = WorkloadBackend(2, (uniform(2, 1),)*3, (1, 2, 3), eta=F(1, huge))
    result = solver.target(3)
    assert result.counts is not None and solver.verify(result.counts)
    assert solver.last_trace['full_quota'] > huge
    counts['binary_checks'] += 1


def main():
    counts = dict(instances=0, main_targets=0, main_optimizations=0,
                  private_targets=0, private_optimizations=0, genuine_cap_failures=0,
                  scaled_decompositions=0, upper_roundings=0, binary_checks=0,
                  invalid_rejections=0)
    check_native(counts)
    for q, ranks, sizes in fixtures():
        counts['instances'] += 1
        original = schedules(ranks, sizes, q)
        optimum = min(original.values())
        for eta in (F(1), F(1, 3)):
            solver = WorkloadBackend(q, ranks, sizes, eta)
            output = solver.optimize()
            counts['main_optimizations'] += 1
            assert output in original and original[output] <= min(2*optimum, solver.alpha*optimum+solver.u)
            targets = sorted({F(0), solver.a/2, solver.a, F(3, 2)*solver.a, 2*solver.a, 3*solver.a})
            for target in targets:
                outcome = solver.target(target)
                counts['main_targets'] += 1
                if outcome.counts is None:
                    assert outcome.failure == 'infeasible' and all(value > target for value in original.values())
                else:
                    assert outcome.failure is None and outcome.counts in original
                    assert original[outcome.counts] <= solver.alpha*target+solver.u
            for budget, divisor in ((1, F(1)), (2, F(2)), (3, F(31, 12))):
                threshold = solver.threshold(budget, divisor)
                factor = max(F(3, 2), 2-1/divisor)
                output = solver.optimize(budget=budget, divisor=divisor, with_fallback=False)
                counts['private_optimizations'] += 1
                assert output in original and original[output] <= factor*max(optimum, threshold)+solver.u
                for target in targets:
                    outcome = solver.target(target, budget=budget, divisor=divisor)
                    counts['private_targets'] += 1
                    if outcome.failure == 'cap':
                        assert target < threshold
                        if any(value <= target for value in original.values()):
                            counts['genuine_cap_failures'] += 1
                    elif outcome.counts is None:
                        assert outcome.failure == 'infeasible' and all(value > target for value in original.values())
                    else:
                        assert outcome.counts in original and original[outcome.counts] <= factor*target+solver.u
    bad = [lambda: decompose((uniform(2, 1),), (1,), (0, 0)),
           lambda: decompose((uniform(2, 1),), (0,), (0, 0)),
           lambda: upper_round((uniform(2, 1),), (1,), ((F(1, 2), F(1, 3)),), 2),
           lambda: WorkloadBackend(1, ((0, 1),), (0.5,)),
           lambda: WorkloadBackend(1, ((0, 1),), (1,)).target(1, budget=1, divisor=F(1, 2))]
    for call in bad:
        try:
            call()
        except ValueError:
            counts['invalid_rejections'] += 1
        else:
            raise AssertionError('invalid workload input accepted')
    assert counts['genuine_cap_failures']
    print(json.dumps(counts, sort_keys=True))


if __name__ == '__main__':
    main()
