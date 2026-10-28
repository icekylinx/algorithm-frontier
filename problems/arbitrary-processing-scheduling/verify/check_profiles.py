"""Independent finite checks for occupied profiles and joint exact-cost recovery.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import combinations, islice, product
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'reference'))
from profiles import Instance, Plan, ProfileBackend, bin_index, profile_counts
from original_schedule_oracle import schedules, uniform


def fixtures():
    yield Instance((), ((), ()), ((), ()), 0)
    yield Instance((uniform(1, 1),)*4, ((0, F(1, 4), F(1, 2), 1),), ((0, 0, 0, 0),), 0)
    for first, second in product((None, 0, F(1, 2), 1), repeat=2):
        yield Instance((uniform(2, 1),), ((first,), (second,)), ((0,), (1,)), F(1, 2))
    for budget in (F(1, 2), 1, 2):
        yield Instance((uniform(2, 1), uniform(2, 1)),
                       ((F(1, 4), 1), (F(2, 3), 0)), ((0, 1), (1, 2)), budget)
    # More than two positive times on one machine; fractional cost/load vertices.
    yield Instance((uniform(2, 1),)*3,
                   ((F(1, 4), F(1, 2), 1), (0, F(1, 3), F(2, 3))),
                   ((1, 0, 1), (0, 1, 0)), F(3, 2))
    # Original totals survive masks and nonmodular recipient restrictions.
    yield Instance(((0, 2, 1, 2), (0, 0, 1, 1)), ((1, None), (F(1, 3), 2)),
                   ((0, 0), (1, 0)), 2)
    yield Instance(((0, 1, 0, 1),), ((None,), (0,)), ((0,), (0,)), 0)
    yield Instance((uniform(3, 1),), ((1,), (F(1, 2),), (0,)), ((0,), (1,), (2,)), 1)


def check_generator(counts):
    for delta in (F(1, 2), F(1, 3), F(1, 4)):
        cap = 1//delta
        bins = -(-((1-delta)/(delta*delta))//1)
        for width in range(min(3, bins)+1):
            for occupied in combinations(range(bins), width):
                lower = tuple(delta+i*delta*delta for i in occupied)
                actual = list(profile_counts(lower, cap))
                expected = {v for v in product(range(cap+1), repeat=width)
                            if sum(v) <= cap and sum((a*b for a, b in zip(v, lower)), F(0)) <= 1}
                assert len(actual) == len(set(actual)) and set(actual) == expected
                counts['profile_families'] += 1
                counts['profile_vectors'] += len(actual)
        # Open-left, closed-right bin boundaries, including the final cap at one.
        for index in range(bins):
            lo = delta+index*delta*delta
            hi = min(F(1), lo+delta*delta)
            for value in ((lo+hi)/2, hi):
                assert bin_index(value, 1, delta) == index
                counts['boundary_checks'] += 1
    # Occupied-bin/counter storage depends on actual coordinates, not 1/epsilon.
    epsilon = F(1, 1 << 80)
    solver = ProfileBackend(Instance((uniform(1, 1),), ((epsilon,),), ((0,),), 0), epsilon)
    assert solver.bin_count > 1 << 150 and solver.count_cap > 1 << 70
    grouped = solver.grouping(F(1))
    assert len(grouped[0][1]) == 1
    lower = tuple(solver.delta+i*solver.delta*solver.delta for i, _ in grouped[0][1])
    assert list(islice(profile_counts(lower, solver.count_cap), 3)) == [(0,), (1,), (2,)]
    counts['binary_accuracy_checks'] += 3
    # A full tiny-accuracy solve with only actually occupied large bins.
    solver = ProfileBackend(Instance((uniform(1, 1),), ((1,),), ((0,),), 0), epsilon)
    assert solver.target(1) == (1,) and solver.optimize() == (1,)
    counts['binary_accuracy_checks'] += 2
    # Valid deep inputs must not depend on the interpreter's recursion limit.
    width = 1100
    assert next(profile_counts((F(1),)*width, 0)) == (0,)*width
    assert list(islice(profile_counts((F(1),)*width, 1), 3)) == [
        (0,)*width, (0,)*(width-1)+(1,), (0,)*(width-2)+(1, 0)]
    counts['deep_stream_checks'] += 2
    # No job types are needed to exercise >1000 actual machine iterators;
    # this remains a compact legal explicit input, without huge rank tables.
    empty_rows = ((),)*width
    solver = ProfileBackend(Instance((), empty_rows, empty_rows, 0), 1)
    plan = next(solver.plans(F(1)))
    assert not plan.allowed and not plan.counts and len(plan.loads) == width
    assert all(group == () and cap == 1 for group, cap in plan.loads)
    assert solver.target(1) == ()
    counts['deep_stream_checks'] += 2


def main():
    counts = dict(instances=0, target_checks=0, optimization_checks=0,
                  fixed_plans=0, joint_recoveries=0, fractional_witnesses=0,
                  protected_profiles=0, profile_families=0, profile_vectors=0,
                  boundary_checks=0, binary_accuracy_checks=0, deep_stream_checks=0,
                  invalid_rejections=0)
    check_generator(counts)
    for instance in fixtures():
        counts['instances'] += 1
        original = schedules(instance)
        legal = {x: values for x, values in original.items() if values[0] <= instance.budget}
        for epsilon in (F(1), F(1, 2)):
            solver = ProfileBackend(instance, epsilon)
            output = solver.optimize()
            counts['optimization_checks'] += 1
            assert (output is None) == (not legal)
            if output is not None:
                assert output in legal and legal[output][1] <= (1+epsilon)*min(v[1] for v in legal.values())
            for target in (F(0), F(1, 2), F(1), F(3, 2), F(2)):
                output = solver.target(target)
                counts['target_checks'] += 1
                feasible = [x for x, v in legal.items() if v[1] <= target]
                if output is None:
                    assert not feasible
                else:
                    assert output in legal and legal[output][1] <= (1+epsilon)*target
                if target == 0:
                    continue
                for plan in solver.plans(target):
                    counts['fixed_plans'] += 1
                    points = solver.fixed_vertices(plan)
                    for point in points:
                        witness = solver.expand(point)
                        counts['fractional_witnesses'] += int(any(v.denominator > 1 for v in witness))
                        recovered = solver.recover(plan, witness)
                        counts['joint_recoveries'] += 1
                        assert recovered in legal
                        witness_cost = sum(instance.costs[p][j]*witness[p*solver.m+j]
                                           for p in range(solver.q) for j in range(solver.m))
                        assert legal[recovered][0] <= witness_cost
                        assert legal[recovered][1] <= (1+epsilon)*target
                # Construct the protected profile from each full integer schedule
                # and check it among the independently inspected fixed plans.
                for x in feasible:
                    machines = solver.grouping(target)
                    count_groups, load_groups = [], []
                    allowed = set()
                    for p, (small, bins) in enumerate(machines):
                        load = F(0)
                        for i, group in bins:
                            cap = sum(x[p*solver.m+j] for _, j in group)
                            count_groups.append((group, cap))
                            load += (solver.delta+i*solver.delta*solver.delta)*cap
                            allowed.update(group)
                        load_groups.append((small, (1-load)*target))
                        allowed.update(small)
                    plan = Plan(frozenset(allowed), tuple(count_groups), tuple(load_groups))
                    assert solver.fixed_vertices(plan)
                    counts['protected_profiles'] += 1
    bad = [lambda: ProfileBackend(Instance((), ((),), ((),), 0), 0),
           lambda: Instance(((0, 1),), ((0.5,),), ((0,),), 0),
           lambda: bin_index(F(1, 2), 1, F(1, 2)),
           lambda: list(profile_counts((0,), 2))]
    for call in bad:
        try:
            call()
        except ValueError:
            counts['invalid_rejections'] += 1
        else:
            raise AssertionError('invalid data accepted')
    assert counts['fractional_witnesses'] and counts['protected_profiles']
    print(json.dumps(counts, sort_keys=True))


if __name__ == '__main__':
    main()
