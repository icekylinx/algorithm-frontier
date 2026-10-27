"""Independent direct original-input checks of the reusable six-profile client.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
No activation family or setup transformation is used in this checker.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'reference'))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'arbitrary-processing-scheduling/verify'))
from activation import Instance, SixBackend, SIX
from original_schedule_oracle import schedules, uniform


def unique_fixtures():
    # At target one, the listed job multiset fits precisely its intended label.
    for label, values in enumerate(((F(1, 2), F(1, 2)), (F(3, 4), F(1, 4)),
                                    (F(1),), (F(3, 8), F(5, 8)),
                                    (F(5, 16), F(11, 16)), (F(7, 16), F(9, 16)))):
        yield label, Instance((uniform(1, 1),)*len(values), (values,), ((0,)*len(values),), 0)


def fixtures():
    yield Instance((), ((), ()), ((), ()), 0)
    for first, second in product((None, 0, F(1, 2), 1), repeat=2):
        yield Instance((uniform(2, 1),), ((first,), (second,)), ((0,), (1,)), F(1, 2))
    for budget in (F(1, 2), 1, 2):
        yield Instance((uniform(2, 1),)*3,
                       ((F(1, 4), F(1, 2), 1), (0, F(1, 3), F(2, 3))),
                       ((1, 0, 1), (0, 1, 0)), budget)
    yield Instance(((0, 2, 1, 2), (0, 0, 1, 1)), ((1, None), (F(1, 3), 2)),
                   ((0, 0), (1, 0)), 2)
    yield Instance(((0, 1, 0, 1),), ((None,), (0,)), ((0,), (0,)), 0)
    yield Instance((uniform(3, 1),), ((1,), (F(1, 2),), (0,)), ((0,), (1,), (2,)), 1)
    for _, instance in unique_fixtures():
        yield instance


def main():
    counts = dict(instances=0, target_checks=0, optimization_checks=0,
                  fixed_profiles=0, joint_recoveries=0, fractional_witnesses=0,
                  protected_profile_vectors=0, unique_profile_cases=0,
                  endpoint_checks=0, invalid_rejections=0)
    for intended, instance in unique_fixtures():
        solver = SixBackend(instance)
        feasible = [label for label in range(6) if solver.fixed_vertices(solver.plan(1, (label,)))]
        assert feasible == [intended]
        counts['unique_profile_cases'] += 1
    for instance in fixtures():
        counts['instances'] += 1
        original = schedules(instance)
        legal = {x: values for x, values in original.items() if values[0] <= instance.budget}
        solver = SixBackend(instance)
        output = solver.optimize()
        counts['optimization_checks'] += 1
        assert (output is None) == (not legal)
        if output is not None:
            assert output in legal and legal[output][1] <= F(3, 2)*min(v[1] for v in legal.values())
        for target in (F(0), F(1, 2), F(1), F(3, 2), F(2)):
            output = solver.target(target)
            counts['target_checks'] += 1
            feasible = [x for x, v in legal.items() if v[1] <= target]
            if output is None:
                assert not feasible
            else:
                assert output in legal and legal[output][1] <= F(3, 2)*target
            if target == 0:
                continue
            protected = {x: False for x in feasible}
            for labels in product(range(6), repeat=solver.q):
                plan = solver.plan(target, labels)
                counts['fixed_profiles'] += 1
                points = solver.fixed_vertices(plan)
                for x in feasible:
                    if any(x[p*solver.m+j] and (p, j) not in plan.allowed
                           for p in range(solver.q) for j in range(solver.m)):
                        continue
                    if any(sum(x[p*solver.m+j] for p, j in group) > cap for group, cap in plan.counts):
                        continue
                    if any(sum(instance.times[p][j]*x[p*solver.m+j] for p, j in group) > cap
                           for group, cap in plan.loads):
                        continue
                    assert points
                    protected[x] = True
                for point in points:
                    witness = solver.expand(point)
                    counts['fractional_witnesses'] += int(any(v.denominator > 1 for v in witness))
                    recovered = solver.recover(plan, witness)
                    counts['joint_recoveries'] += 1
                    assert recovered in legal and legal[recovered][1] <= F(3, 2)*target
                    witness_cost = sum(instance.costs[p][j]*witness[p*solver.m+j]
                                       for p in range(solver.q) for j in range(solver.m))
                    assert legal[recovered][0] <= witness_cost
            assert all(protected.values())
            counts['protected_profile_vectors'] += len(protected)
    for label, (groups, _) in enumerate(SIX, 1):
        for index, (lo, hi) in enumerate(groups):
            for value, expected in ((lo, False), ((lo+hi)/2, True), (hi, True)):
                solver = SixBackend(Instance((uniform(1, 1),), ((value,),), ((0,),), 0))
                plan = solver.plan(1, (label,))
                assert bool(plan.counts[index][0]) == expected
                counts['endpoint_checks'] += 1
    for call in (lambda: SixBackend(Instance((), ((),), ((),), 0)).plan(0, (0,)),
                 lambda: SixBackend(Instance((), ((),), ((),), 0)).plan(1, (6,))):
        try:
            call()
        except ValueError:
            counts['invalid_rejections'] += 1
        else:
            raise AssertionError('invalid profile query accepted')
    assert counts['fractional_witnesses'] and counts['protected_profile_vectors']
    print(json.dumps(counts, sort_keys=True))


if __name__ == '__main__':
    main()
