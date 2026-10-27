"""Independent finite schedule oracle against the exact reference backend.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
No backend rank, row, integer-enumeration or load helper is used by the oracle.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'reference'))
from scheduling import Backend, Instance, vertices


def oracle(instance):
    q, m = len(instance.times), len(instance.ranks)
    result = []
    # Enumerate every pair count independently, rather than eliminate totals.
    bounds = [range(instance.ranks[j][1 << p]+1) for p in range(q) for j in range(m)]
    for x in product(*bounds):
        if any(sum(x[p*m+j] for p in range(q)) != instance.ranks[j][-1] for j in range(m)):
            continue
        if any(x[p*m+j] and instance.times[p][j] is None for p in range(q) for j in range(m)):
            continue
        if any(sum(x[p*m+j] for p in range(q) if mask >> p & 1) > instance.ranks[j][mask]
               for j in range(m) for mask in range(1 << q)):
            continue
        cost = sum(instance.costs[p][j]*x[p*m+j] for p in range(q) for j in range(m))
        loads = tuple(sum(instance.times[p][j]*x[p*m+j] for j in range(m)
                          if instance.times[p][j] is not None) for p in range(q))
        result.append((tuple(x), F(cost), max(loads)))
    return result


def uniform(q, n):
    return tuple(0 if mask == 0 else n for mask in range(1 << q))


def fixtures():
    yield Instance((), ((), ()), ((), ()), 0)
    yield Instance(((0, 0, 0, 0),), ((0,), (None,)), ((0,), (1,)), 0)
    yield Instance(((0, 3), (0, 1), (0, 2)), ((1, 5, 0),), ((0, 0, 0),), 0)
    # Each row has its own positive pair; role quotas at T=6 differ (5 and 3).
    for budget in (0, 1, 3, 7):
        yield Instance((uniform(2, 3), uniform(2, 1), uniform(2, 1)),
                       ((1, 5, 0), (2, 6, 0)), ((0, 2, 1), (1, 0, 0)), budget)
    yield Instance((uniform(2, 6), uniform(2, 1), uniform(2, 1)),
                   ((1, 5, 0), (2, 6, 0)), ((0, 2, 1), (1, 0, 0)), 0)
    # Cost cuts yield fractional LP vertices; zero-time units retain real costs.
    for budget in (F(1, 2), 1, F(3, 2), 3):
        yield Instance((uniform(2, 1), uniform(2, 1), uniform(2, 1)),
                       ((0, 1, 2), (F(1, 2), F(3, 2), 0)),
                       ((2, 0, 1), (0, 1, 2)), budget)
    # Masks cannot lower original totals; asymmetric nonmodular rank tables.
    yield Instance(((0, 1, 0, 1), (0, 2, 1, 2)),
                   ((7, 1), (None, 3)), ((0, 1), (0, 0)), 3)
    yield Instance(((0, 2, 1, 2),), ((None,), (2,)), ((0,), (0,)), 0)
    # Arbitrary-q API, including a loop and a modular rank with forced counts.
    yield Instance(((0, 1, 1, 2, 0, 1, 1, 2),),
                   ((0,), (F(3, 2),), (None,)), ((2,), (0,), (0,)), 2)
    yield Instance((uniform(3, 2),), ((1,), (2,), (0,)), ((1,), (0,), (3,)), 1)
    # Broader small exhaustive model family, including zero and absent pairs.
    for t0, t1 in product((None, 0, 1, 2), repeat=2):
        for rank in ((0, 1, 1, 1), (0, 1, 0, 1), (0, 2, 1, 2)):
            yield Instance((rank,), ((t0,), (t1,)), ((0,), (1,)), F(1, 2))


def main():
    counts = dict(instances=0, target_checks=0, optimization_checks=0,
                  role_nodes=0, support_rows=0, protected_nodes=0,
                  fractional_witnesses=0, joint_recoveries=0, zero_time_outputs=0)
    seen_classes = set()
    heterogeneous = False
    for instance in fixtures():
        counts['instances'] += 1
        backend = Backend(instance)
        schedules = oracle(instance)
        legal = [s for s in schedules if s[1] <= instance.budget]
        by_output = {s[0]: s for s in schedules}
        for d in (2, 3, 4):
            output = backend.optimize(d)
            counts['optimization_checks'] += 1
            assert (output is None) == (not legal)
            if output is not None:
                assert output in by_output and by_output[output][1] <= instance.budget
                assert by_output[output][2] <= F(2*d-1, d)*min(s[2] for s in legal)
            for target in (F(0), F(1, 2), F(1), F(3, 2), F(2), F(3), F(4), F(6), F(8)):
                output = backend.target(target, d)
                counts['target_checks'] += 1
                feasible = [s for s in legal if s[2] <= target]
                if output is None:
                    assert not feasible
                else:
                    assert output in by_output and by_output[output][1] <= instance.budget
                    assert by_output[output][2] <= F(2*d-1, d)*target
                    if target == 0:
                        counts['zero_time_outputs'] += 1
                if target == 0:
                    continue
                classes = backend.classify(target, d)
                seen_classes.update(c[0] for c in classes)
                roles = [p for p, c in enumerate(classes) if c[0] == 'role']
                heterogeneous |= len({classes[p][4] for p in roles}) > 1
                for mask in range(1 << len(roles)):
                    selected = {p for i, p in enumerate(roles) if mask >> i & 1}
                    counts['role_nodes'] += 1
                    base_rows, _, _ = backend.node(target, d, selected, weak=False)
                    base_points = vertices(base_rows, backend.dimension)
                    weak_rows, _, _ = backend.node(target, d, selected)
                    weak_points = vertices(weak_rows, backend.dimension)
                    for point in weak_points:
                        witness = backend.expand(point)
                        if any(v.denominator > 1 for v in witness):
                            counts['fractional_witnesses'] += 1
                        recovered = backend.recover(target, d, selected, witness)
                        counts['joint_recoveries'] += 1
                        assert recovered in by_output
                        assert by_output[recovered][1] <= sum(instance.costs[p][j]*witness[p*backend.m+j]
                                                              for p in range(backend.q) for j in range(backend.m))
                        assert by_output[recovered][2] <= F(2*d-1, d)*target
                    protected_schedules = []
                    for full, _, _ in feasible:
                        protected = {p for p in roles if any(full[p*backend.m+j]
                                     and instance.times[p][j] == classes[p][2] for j in range(backend.m))}
                        if protected <= selected:
                            assert base_points
                            if protected == selected:
                                assert weak_points
                            protected_schedules.append((full, protected))
                    if not base_points:
                        try:
                            backend.separator(target, d, selected)
                        except ValueError as error:
                            assert str(error) == 'empty X_Q'
                        else:
                            raise AssertionError('empty underlying region was not rejected')
                        continue
                    row = backend.separator(target, d, selected)
                    assert (row is None) == bool(weak_points)
                    if row is not None:
                        normal, capacity = row
                        counts['support_rows'] += 1
                        assert all(v >= 0 for v in normal) and sum(normal) == 1
                        assert sum(normal[i]*classes[p][5] for i, p in enumerate(sorted(selected))) > capacity
                        for point in base_points:
                            x = backend.expand(point)
                            spare = [classes[p][3]-sum(x[p*backend.m+j] for j in range(backend.m)
                                     if instance.times[p][j] == classes[p][1]) for p in sorted(selected)]
                            assert sum(v*w for v, w in zip(normal, spare)) <= capacity
                    for full, protected in protected_schedules:
                        counts['protected_nodes'] += 1
                        # Evaluate the unchanged original schedule independently.
                        for p in protected:
                            small = sum(full[p*backend.m+j] for j in range(backend.m)
                                        if instance.times[p][j] == classes[p][1])
                            assert small+classes[p][4] <= classes[p][3]
                        if row is not None:
                            normal, capacity = row
                            weights = {p: normal[i]*classes[p][4] for i, p in enumerate(sorted(selected))}
                            assert sum(weights[p] for p in protected) <= capacity
                            assert sum(weights[p] for p in selected-protected) > F(d-1, d+1)*sum(weights.values())
    assert seen_classes == {'empty', 'single', 'easy', 'small', 'role'}
    assert heterogeneous and counts['support_rows'] and counts['fractional_witnesses']
    # Reject malformed ranks and inexact numerical data before doing optimization.
    invalid = [(((0, 1, 1, 3),), ((1,), (2,)), ((0,), (0,)), 0),
               (((0, 1, 1, 1),), ((0.5,), (2,)), ((0,), (0,)), 0)]
    for args in invalid:
        try:
            Instance(*args)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid instance accepted')
    print(json.dumps(dict(counts, classes=sorted(seen_classes), heterogeneous_quotas=True), sort_keys=True))


if __name__ == '__main__':
    main()
