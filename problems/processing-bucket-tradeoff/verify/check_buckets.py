"""Independent original-schedule checks of the exact bucket client.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'reference'))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'arbitrary-processing-scheduling/verify'))
from buckets import BucketBackend, Instance
from original_schedule_oracle import schedules, uniform


def fixtures():
    yield Instance((), ((), ()), ((), ()), 0)
    yield Instance((uniform(1, 1),)*4, ((0, F(1, 4), F(1, 2), 1),), ((0, 0, 0, 0),), 0)
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


def main():
    counts = dict(instances=0, target_checks=0, optimization_checks=0,
                  fixed_labels=0, joint_recoveries=0, fractional_witnesses=0,
                  protected_labels=0, endpoint_checks=0)
    for instance in fixtures():
        counts['instances'] += 1
        original = schedules(instance)
        legal = {x: v for x, v in original.items() if v[0] <= instance.budget}
        for depth in (0, 1, 2):
            solver = BucketBackend(instance, depth)
            output = solver.optimize()
            counts['optimization_checks'] += 1
            assert (output is None) == (not legal)
            if output is not None:
                assert output in legal and legal[output][1] <= solver.factor*min(v[1] for v in legal.values())
            for target in (F(0), F(1, 2), F(1), F(3, 2), F(2)):
                output = solver.target(target)
                counts['target_checks'] += 1
                feasible = [x for x, v in legal.items() if v[1] <= target]
                if output is None:
                    assert not feasible
                else:
                    assert output in legal and legal[output][1] <= solver.factor*target
                if target == 0:
                    continue
                for plan in solver.plans(target):
                    counts['fixed_labels'] += 1
                    for point in solver.fixed_vertices(plan):
                        witness = solver.expand(point)
                        counts['fractional_witnesses'] += int(any(v.denominator > 1 for v in witness))
                        recovered = solver.recover(plan, witness)
                        counts['joint_recoveries'] += 1
                        assert recovered in legal and legal[recovered][1] <= solver.factor*target
                        assert legal[recovered][0] <= sum(instance.costs[p][j]*witness[p*solver.m+j]
                                                        for p in range(solver.q) for j in range(solver.m))
                for x in feasible:
                    labels = []
                    for p, row in enumerate(instance.times):
                        used = [v for j, v in enumerate(row) if v is not None and x[p*solver.m+j]]
                        maximum = max(used, default=0)
                        label = next((i for i, endpoint in enumerate(solver.endpoints) if maximum <= endpoint*target), None)
                        assert label is not None
                        labels.append(label)
                    assert solver.fixed_vertices(solver.plan(target, labels))
                    counts['protected_labels'] += 1
    for depth in range(1, 7):
        probe = BucketBackend(Instance((uniform(1, 1),), ((0,),), ((0,),), 0), depth)
        for label in range(1, depth+1):
            lo, hi = probe.endpoints[label-1:label+1]
            for value, expected in ((lo, False), ((lo+hi)/2, True), (hi, True)):
                solver = BucketBackend(Instance((uniform(1, 1),), ((value,),), ((0,),), 0), depth)
                plan = solver.plan(1, (label,))
                assert bool(plan.counts[0][0]) == expected
                counts['endpoint_checks'] += 1
    assert counts['fractional_witnesses'] and counts['protected_labels']
    print(json.dumps(counts, sort_keys=True))


if __name__ == '__main__':
    main()
