"""Independent original-activation/original-job checks of the activation adapter.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'reference'))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'arbitrary-processing-scheduling/verify'))
from activation import ActivatedBackend, Instance
from original_schedule_oracle import schedules, uniform


def activated_oracle(jobs, matroid, fees):
    """Use original physical schedules and independent activation enumeration."""
    q, m = len(jobs.times), len(jobs.ranks)
    original = schedules(jobs)
    result = {}
    for basis in combinations(range(q), matroid[-1]):
        mask = sum(1 << p for p in basis)
        if matroid[mask] != len(basis):
            continue
        setup = sum(fees[p] for p in basis)
        for counts, (assignment, load) in original.items():
            if any(counts[p*m+j] for p in range(q) if p not in basis for j in range(m)):
                continue
            if setup+assignment <= jobs.budget:
                result[(tuple(basis), counts)] = F(setup+assignment), load
    return result


def fixtures():
    mats = ((0, 0, 0, 0), (0, 1, 1, 1), (0, 1, 0, 1), (0, 1, 1, 2))
    ranks = ((0, 1, 1, 1), (0, 1, 0, 1), (0, 0, 1, 1), (0, 2, 1, 2))
    for matroid, rank, times in product(mats, ranks,
            (((None,), (0,)), ((0,), (1,)), ((F(1, 2),), (1,)), ((1,), (None,)))):
        yield Instance((rank,), times, ((0,), (1,)), F(3, 2)), matroid, (0, F(1, 2))
    # Empty mandatory totals still require a real affordable activation basis.
    yield Instance((), ((), ()), ((), ()), 0), (0, 1, 1, 1), (1, 0)
    yield Instance(((0, 0, 0, 0),), ((0,), (1,)), ((0,), (0,)), 0), (0, 1, 1, 1), (1, 1)
    # Cheapest setup lacks capacity; cheapest setup alone is not a feasibility gate.
    yield Instance(((0, 0, 1, 1),), ((1,), (0,)), ((0,), (0,)), 1), (0, 1, 1, 1), (0, 1)
    # A cheap setup's assignment is too expensive; another basis has zero load.
    yield Instance((uniform(2, 1),), ((1,), (0,)), ((5,), (0,)), 4), (0, 1, 1, 1), (0, 4)
    # Individually affordable pieces cannot be combined beyond the one budget.
    yield Instance((uniform(2, 1),), ((1,), (1,)), ((1,), (1,)), F(3, 2)), (0, 1, 1, 1), (1, 2)
    yield Instance((uniform(2, 1),)*2, ((F(1, 4), 1), (F(2, 3), 0)),
                   ((0, 1), (1, 2)), F(5, 2)), (0, 1, 1, 2), (F(1, 4), F(1, 4))
    # Nonuniform activation matroid: coloop 0 and a parallel class {1,2}.
    yield (Instance((uniform(3, 2),), ((1,), (F(1, 2),), (0,)), ((0,), (1,), (2,)), 4),
           (0, 1, 1, 2, 1, 2, 1, 2), (F(1, 2), 0, 1))
    # A loop machine's zero-time capacity is unavailable to every active basis.
    yield Instance(((0, 0, 0, 0, 1, 1, 1, 1),), ((1,), (1,), (0,)),
                   ((0,), (0,), (0,)), 0), (0, 1, 1, 1, 0, 1, 1, 1), (0, 0, 0)


def main():
    counts = dict(instances=0, feasibility_checks=0, target_checks=0,
                  optimization_checks=0, compressed_solver_checks=0,
                  binary_greedy_checks=0, invalid_rejections=0)
    for jobs, matroid, fees in fixtures():
        counts['instances'] += 1
        original = activated_oracle(jobs, matroid, fees)
        for method in ('profiles', 'six', 'buckets'):
            solver = ActivatedBackend(jobs, matroid, fees, method=method)
            feasible = solver.feasible()
            counts['feasibility_checks'] += 1
            assert (feasible is None) == (not original)
            if feasible is not None:
                assert (feasible.basis, feasible.counts) in original
            output = solver.optimize()
            counts['optimization_checks'] += 1
            assert (output is None) == (not original)
            if output is not None:
                key = output.basis, output.counts
                assert key in original and original[key][1] <= solver.factor*min(v[1] for v in original.values())
            for target in (F(0), F(1, 2), F(1), F(3, 2), F(2)):
                output = solver.target(target)
                counts['target_checks'] += 1
                if output is None:
                    assert not any(v[1] <= target for v in original.values())
                else:
                    key = output.basis, output.counts
                    assert key in original and original[key][1] <= solver.factor*target
                assert all(size == matroid[-1] for size in solver.last_active_sizes)
                counts['compressed_solver_checks'] += solver.last_solver_calls
    huge = 1 << 80
    jobs = Instance(((0, 0, huge, huge),), ((1,), (0,)), ((0,), (F(1, 2),)), F(huge, 2)+1)
    for method in ('profiles', 'six', 'buckets'):
        solver = ActivatedBackend(jobs, (0, 1, 1, 1), (0, 1), method=method)
        def forbidden(*args, **kwargs):
            raise AssertionError('binary greedy/zero gate called a positive-target solver')
        solver.make_solver = forbidden
        for result in (solver.feasible(), solver.target(0), solver.optimize()):
            assert result.basis == (1,) and result.counts == (0, huge)
            assert solver.cost(result) == F(huge, 2)+1 and solver.load(result) == 0
            counts['binary_greedy_checks'] += 1
    bad = [lambda: ActivatedBackend(jobs, (0, 2, 1, 2), (0, 0)),
           lambda: ActivatedBackend(jobs, (0, 1, 1, 1), (-1, 0)),
           lambda: ActivatedBackend(jobs, (0, 1, 1, 1), (0.5, 0)),
           lambda: ActivatedBackend(jobs, (0, 1, 1, 1), (0, 0), method='other'),
           lambda: ActivatedBackend(jobs, (0, 1, 1, 1), (0, 0)).restricted((0, 1)),
           lambda: ActivatedBackend.minimum_assignment(
               Instance((uniform(2, 1),), ((None,), (0,)), ((0,), (0,)), 0))]
    for call in bad:
        try:
            call()
        except ValueError:
            counts['invalid_rejections'] += 1
        else:
            raise AssertionError('invalid activation data accepted')
    print(json.dumps(counts, sort_keys=True))


if __name__ == '__main__':
    main()
