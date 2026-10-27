"""Independent finite original-base checks of the two-size corank client.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
The original-base oracle does not use box ranks, duality or the batch engine.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'reference'))
from corank import CorankBackend, box_rank, complete_base


def legal(rank, vector, base=False):
    return (all(v >= 0 for v in vector)
            and (not base or sum(vector) == rank[-1])
            and all(sum(vector[p] for p in range(len(vector)) if s >> p & 1) <= rank[s]
                    for s in range(len(rank))))


def original_bases(rank):
    q = len(rank).bit_length()-1
    return [x for x in product(*(range(rank[1 << p]+1) for p in range(q)))
            if legal(rank, x, base=True)]


def original_schedules(small, large, u, a):
    q = len(small).bit_length()-1
    return {tuple(v for p in range(q) for v in (x[p], y[p])):
            max((u*x[p]+a*y[p] for p in range(q)), default=F(0))
            for x in original_bases(small) for y in original_bases(large)}


def rank_tables():
    return [(0, a, b, n) for n in range(4) for a in range(n+1) for b in range(n+1)
            if a+b >= n]


def fixtures():
    tables = rank_tables()
    for small, large in product(tables, repeat=2):
        yield small, large, F(1), F(3), (2,)
    yield (0,), (0,), F(1), F(3), (2, 3, 4)
    yield (0, 2), (0, 1), F(1, 2), F(3, 2), (2, 3, 4)
    yield (0, 3, 3, 6), (0, 1, 1, 1), F(1), F(2), (2, 3, 4)
    # Uniform large rank one/two, shared small capacity, and off-promise guards.
    small = (0, 3, 3, 6, 3, 6, 6, 6)
    for h in (1, 2):
        large = tuple(min(s.bit_count(), h) for s in range(8))
        yield small, large, F(1), F(3), (2, 3, 4)
    # A deficient coloop can only be deleted by a rejected rank-test child.
    yield (0, 2, 0, 2, 0, 2, 0, 2), (0, 1, 1, 2, 1, 2, 1, 2), F(1), F(3), (2,)
    # Large loops remain physical small-job machines throughout duality.
    yield small, (0, 1, 0, 1, 0, 1, 0, 1), F(1), F(3), (2, 3, 4)
    # Rational sizes exercise the common-denominator target grid.
    yield (0, 2, 2, 2), (0, 1, 1, 1), F(2, 3), F(7, 4), (2, 3, 4)


def main():
    counts = dict(instances=0, target_checks=0, optimization_checks=0,
                  box_support_checks=0, dual_vectors=0, dual_completions=0,
                  batch_nodes=0, batch_branches=0, rank_rejections=0, guards=0,
                  binary_large_checks=0)
    branches = set()
    # Box ranks are compared with direct maxima over original independent vectors.
    for rank in rank_tables():
        for cap in range(5):
            boxed = box_rank(rank, cap)
            vectors = [x for x in product(*(range(min(cap, rank[1 << p])+1) for p in range(2)))
                       if legal(rank, x)]
            for subset in range(4):
                expected = max(sum(x[p] for p in range(2) if subset >> p & 1) for x in vectors)
                assert boxed[subset] == expected
                counts['box_support_checks'] += 1
    dual_checked = set()
    for small, large, u, a, divisors in fixtures():
        counts['instances'] += 1
        backend = CorankBackend(small, large, u, a)
        schedules = original_schedules(small, large, u, a)
        optimum = min(schedules.values())
        for d in divisors:
            output = backend.optimize(d)
            counts['optimization_checks'] += 1
            assert output in schedules and schedules[output] <= F(2*d-1, d)*optimum
            targets = sorted({F(0), u, a-u, a, a+u, 2*a-u, 2*a, 3*a, F(3, 2)*a})
            for target in targets:
                output = backend.target(target, d)
                counts['target_checks'] += 1
                trace = backend.last_trace
                branches.add(trace['branch'])
                if output is None:
                    assert all(value > target for value in schedules.values())
                else:
                    assert output in schedules and schedules[output] <= F(2*d-1, d)*target
                for key in ('batch_nodes', 'batch_branches', 'rank_rejections', 'guards'):
                    counts[key] += trace[key]
                if trace['batch_nodes']:
                    c = backend.corank
                    # Gamma((d+1)/(d-1))^(d-1), compared without floating point.
                    power = F((d+1)**(d+1), 4*(d-1)**(d-1))
                    assert trace['batch_nodes']**(d-1) <= (c+1)**(d-1)*power**c
                if not backend.h or not a <= target < 2*a:
                    continue
                cap = target//u
                key = (small, cap)
                if key in dual_checked:
                    continue
                dual_checked.add(key)
                boxed = box_rank(small, cap)
                if boxed[-1] != small[-1]:
                    continue
                q, full = backend.q, len(small)-1
                dual = tuple(cap*s.bit_count()+boxed[full ^ s]-small[-1] for s in range(len(small)))
                # Both directions of the full-ground complement correspondence.
                for x in product(range(cap+1), repeat=q):
                    y = tuple(cap-v for v in x)
                    assert legal(boxed, x, base=True) == legal(dual, y, base=True)
                    counts['dual_vectors'] += 1
                # Every original capped small base has the retained original total.
                for x in original_bases(small):
                    if max(x, default=0) <= cap:
                        assert legal(boxed, x, base=True)
                # Check zero extension and greedy base completion of all binary
                # lower quotas on the full physical-machine set.
                for lower in product((0, 1), repeat=q):
                    if legal(dual, lower):
                        y = complete_base(dual, lower)
                        assert legal(dual, y, base=True) and all(v >= w for v, w in zip(y, lower))
                        assert legal(small, tuple(cap-v for v in y), base=True)
                        counts['dual_completions'] += 1
    # Binary counts are processed in the hard path without calling the inherited
    # numerical count enumerator or its LP/recovery implementation.
    huge = 1 << 80
    backend = CorankBackend((0, huge, 0, huge), (0, 0, 1, 1), 1, huge)
    def forbidden(*args, **kwargs):
        raise AssertionError('hard path called the inherited high-target backend')
    backend.shared.target = forbidden
    for d in (2, 3, 4):
        output = backend.target(huge, d)
        assert output == (huge, 0, 0, 1)
        assert backend.optimize(d) == output
        counts['binary_large_checks'] += 2
    assert {'one-size', 'below-large', 'shared-high-target', 'boolean-rank-failure',
            'small-rank-failure', 'one-unit', 'batch'} <= branches
    assert counts['batch_branches'] and counts['guards'] and counts['rank_rejections']
    invalid = [((0, 2, 2, 1), (0, 1, 1, 1), 1, 3),
               ((0, 1, 1), (0, 1, 1), 1, 3),
               ((0, 1), (0, 1), 0.5, 3)]
    for args in invalid:
        try:
            CorankBackend(*args)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid input accepted')
    print(json.dumps(dict(counts, branches=sorted(branches)), sort_keys=True))


if __name__ == '__main__':
    main()
