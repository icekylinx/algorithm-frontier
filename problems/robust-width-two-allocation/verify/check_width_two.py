"""Independent finite oracle checks. Attribution: icekylinx and GPT-6 Astra Pro.

Apache-2.0. Brute-force selected bases never call the dual graph solver.
"""
from itertools import combinations, product
from pathlib import Path
import random
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'reference'))
import width_two as impl


def sets(q):
    return tuple(frozenset(i for i in range(q) if mask >> i & 1) for mask in range(1 << q))


def binary_rank(columns, selected):
    pivots = {}
    for i in sorted(selected):
        value = columns[i]
        while value:
            bit = value.bit_length()-1
            if bit not in pivots:
                pivots[bit] = value
                break
            value ^= pivots[bit]
    return len(pivots)


def boolean_scenario(q, conflict=frozenset()):
    # One genuine Boolean partition resource: conflict block cap |block|-1,
    # and independent unit blocks for other players. Size-one conflicts are loops.
    def test(selected):
        if conflict and conflict <= selected:
            return None
        return tuple((p, 'pool' if p in conflict else p) for p in sorted(selected))
    return test


def brute(q, rank, oracle, scenarios, forced):
    for selected in combinations(range(q),rank):
        chosen = frozenset(selected)
        if not chosen & forced and oracle(chosen) == rank and all(test(chosen) is not None for test in scenarios):
            return chosen
    return None


def check(q, rank, oracle, scenarios, forced=frozenset()):
    actual = impl.solve(q,rank,oracle,scenarios,forced)
    expected = brute(q,rank,oracle,scenarios,forced)
    assert actual.status != 'WIDTH VIOLATION'
    assert (actual.status == 'SUCCESS') == (expected is not None)
    if actual.status == 'SUCCESS':
        selected = frozenset(actual.selected)
        assert len(selected) == rank and oracle(selected) == rank and not selected & forced
        assert len(actual.witnesses) == len(scenarios)
        assert all(test(selected) == witness for test,witness in zip(scenarios,actual.witnesses))
    # Fibonacci leaf bound times depth bounds all processed nodes, including failures.
    h = q-rank-len(forced)
    if h >= 0:
        a,b = 0,1
        for _ in range(h+1): a,b = b,a+b
        assert actual.nodes <= (h+1)*a
    return actual


def main():
    exhaustive = represented = intersections = guarded = 0
    for q in range(5):
        allsets = sets(q)
        pairs = tuple(combinations(range(q),2))
        for mask in range(1 << len(pairs)):
            edges = tuple(frozenset(edge) for j,edge in enumerate(pairs) if mask >> j & 1)
            scenarios = tuple(boolean_scenario(q,edge) for edge in edges) or (boolean_scenario(q),)
            for rank in range(q+1):
                oracle = lambda selected, rank=rank: min(len(selected),rank)
                for forced in allsets:
                    if len(forced) <= q-rank:
                        check(q,rank,oracle,scenarios,forced)
                        exhaustive += 1
    rng = random.Random(271030)
    for _ in range(400):
        q = rng.randrange(1,8)
        columns = tuple(rng.randrange(1 << rng.randrange(1,5)) for _ in range(q))
        oracle = lambda selected, columns=columns: binary_rank(columns,selected)
        rank = oracle(frozenset(range(q)))
        conflicts = [frozenset(edge) for edge in combinations(range(q),2) if rng.randrange(3) == 0]
        conflicts.extend(frozenset((p,)) for p in range(q) if rng.randrange(9) == 0)
        scenarios = tuple(boolean_scenario(q,edge) for edge in conflicts) or (boolean_scenario(q),)
        forced = frozenset(p for p in range(q) if rng.randrange(4) == 0)
        check(q,rank,oracle,scenarios,forced)
        represented += 1
    # Exercise the polynomial terminal primitive independently of graph branching.
    for _ in range(300):
        q = rng.randrange(1,9)
        c1 = tuple(rng.randrange(16) for _ in range(q))
        c2 = tuple(rng.randrange(16) for _ in range(q))
        ind1 = lambda selected: binary_rank(c1,selected) == len(selected)
        ind2 = lambda selected: binary_rank(c2,selected) == len(selected)
        actual = impl.intersection(range(q),ind1,ind2)
        expected = max(len(s) for s in sets(q) if ind1(s) and ind2(s))
        assert len(actual) == expected and ind1(actual) and ind2(actual)
        intersections += 1
    # A matching terminal may need an augmenting exchange and may complete both ends.
    columns = (1,1,2,0)
    oracle = lambda selected: binary_rank(columns,selected)
    scenarios = (boolean_scenario(4,frozenset((0,2))),boolean_scenario(4,frozenset((1,3))))
    check(4,2,oracle,scenarios)
    both = impl.solve(3,1,lambda selected: int(bool(selected)),(boolean_scenario(3,frozenset((0,1))),))
    assert both.status == 'SUCCESS' and both.selected == (2,)
    first = (1,1,2)
    second = (1,2,1)
    assert impl.intersection(range(3),
                             lambda s: binary_rank(first,s) == len(s),
                             lambda s: binary_rank(second,s) == len(s)) == frozenset((1,2))
    # Larger minimal failures are reported as a third outcome, never failed seeds.
    for q in range(3,8):
        for width in range(3,q+1):
            conflict = frozenset(range(width))
            scenario = boolean_scenario(q,conflict)
            result = impl.solve(q,q,lambda selected: len(selected),(scenario,))
            assert result.status == 'WIDTH VIOLATION' and result.scenario == 0
            cert = frozenset(result.certificate)
            assert cert == conflict and scenario(cert) is None
            assert all(scenario(cert-{p}) is not None for p in cert)
            guarded += 1
    # Outside the width class a successful actual witness and exhausted failure stay sound.
    larger = boolean_scenario(4,frozenset((0,1,2)))
    result = impl.solve(4,2,lambda selected: min(2,len(selected)),(larger,))
    assert result.status == 'SUCCESS' and larger(frozenset(result.selected)) is not None
    assert impl.solve(4,3,lambda selected: min(3,len(selected)),(larger,),forced=(0,1)).status == 'INFEASIBLE'
    # Exact modular budget: failed triples do not masquerade as pair conflicts.
    cost_test = lambda selected: tuple((p,p) for p in sorted(selected)) if len(selected) <= 2 else None
    result = impl.solve(3,3,lambda selected: len(selected),(cost_test,))
    assert result.status == 'WIDTH VIOLATION' and len(result.certificate) == 3
    invalid = 0
    for thunk in (lambda: impl.solve(-1,0,lambda s: 0,(cost_test,)),
                  lambda: impl.solve(3,4,lambda s: len(s),(cost_test,)),
                  lambda: impl.solve(3,3,lambda s: len(s),()),
                  lambda: impl.solve(3,3,lambda s: len(s),(cost_test,),forced=(3,)),
                  lambda: impl.solve(3,2,lambda s: len(s),(cost_test,))):
        try: thunk()
        except ValueError: invalid += 1
        else: raise AssertionError('invalid input accepted')
    print(f'PASS: {exhaustive} exhaustive uniform-matroid graph/forced-seed cases; {represented} binary-represented matroid cases; {intersections} independent exhaustive matroid-intersection comparisons; {guarded} minimal higher-width certificates; matching/completion and budget guards; {invalid} malformed inputs; Fibonacci node accounting.')


if __name__ == '__main__':
    main()
