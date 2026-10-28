"""Independent weighted/unit/bounded-gate checks.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
"""
from dataclasses import replace
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
from types import SimpleNamespace
import importlib.util
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'reference'))
import bounded as impl


def subsets(q):
    return tuple(frozenset(p for p in range(q) if mask >> p & 1) for mask in range(1 << q))


def binary_rank(columns, selected):
    basis = {}
    for p in sorted(selected):
        value = columns[p]
        while value:
            bit = value.bit_length()-1
            if bit not in basis:
                basis[bit] = value
                break
            value ^= basis[bit]
    return len(basis)


def native_unit(ranks, costs, budget, selected):
    # Enumerate assignments and test ORIGINAL polymatroid subset inequalities.
    q = len(costs)
    chosen = sorted(selected)
    best = None
    for types in product(*(tuple(j for j,c in enumerate(costs[p]) if c is not None) for p in chosen)):
        if any(sum(1 for p,j in zip(chosen,types) if j == h and mask >> p & 1) > value
               for h,row in enumerate(ranks) for mask,value in enumerate(row)):
            continue
        cost = sum((costs[p][j] for p,j in zip(chosen,types)),F(0))
        if best is None or cost < best:
            best = cost
    return best


def pool_rank(q, blocks):
    return tuple(sum(cap for owners,cap in blocks if any(mask >> p & 1 for p in owners))
                 for mask in range(1 << q))


def main():
    rng = random.Random(271031)
    weighted = native = gates = violations = integrations = 0
    examples = []
    for _ in range(320):
        n = rng.randrange(0,9)
        left = tuple(rng.randrange(16) for _ in range(n))
        right = tuple(rng.randrange(16) for _ in range(n))
        first = lambda chosen,left=left: binary_rank(left,chosen) == len(chosen)
        second = lambda chosen,right=right: binary_rank(right,chosen) == len(chosen)
        costs = tuple(F(rng.randrange(-4,5),rng.randrange(1,4)) for _ in range(n))
        common = [s for s in subsets(n) if first(s) and second(s)]
        for target in range(n+2):
            certificate = impl.minimum_cost(first,second,costs,target)
            size = min(target,max(map(len,common)))
            expected = min(sum((costs[p] for p in s),F(0)) for s in common if len(s) == size)
            assert len(certificate.chosen) == size
            assert sum((costs[p] for p in certificate.chosen),F(0)) == expected
            assert impl.verify_intersection(first,second,costs,target,certificate)
            examples.append((first,second,costs,target,certificate))
            weighted += 1
    # A shortest cheapest augmentation must exchange an earlier greedy choice.
    left,right = (1,1,2),(1,2,1)
    first = lambda chosen: binary_rank(left,chosen) == len(chosen)
    second = lambda chosen: binary_rank(right,chosen) == len(chosen)
    certificate = impl.minimum_cost(first,second,(0,1,1),2)
    assert certificate.chosen == (1,2)
    # Matroid loops, signed/zero ties and enormous binary costs.
    huge = 1 << 300
    assert impl.minimum_cost(lambda s: len(s) <= 1,lambda s: len(s) <= 1,(huge,huge-1),1).chosen == (1,)
    scenarios = []
    for _ in range(60):
        q,m = rng.randrange(1,6),rng.randrange(1,4)
        ranks = []
        for j in range(m):
            blocks = [(frozenset(p for p in range(q) if p % 2 == parity),rng.randrange(3)) for parity in range(2)]
            ranks.append(pool_rank(q,blocks))
        costs = tuple(tuple(None if rng.randrange(5) == 0 else F(rng.randrange(5),2) for _ in range(m)) for _ in range(q))
        budget = F(rng.randrange(7),2)
        scenario = impl.table_scenario(ranks,costs,budget)
        for selected in subsets(q):
            expected = native_unit(ranks,costs,budget,selected)
            certificate = scenario.optimize(selected)
            assert scenario.verify(certificate)
            if len(certificate.assignment) == len(selected):
                assert expected is not None
                assert sum((costs[p][j] for p,j in certificate.assignment),F(0)) == expected
            else:
                assert expected is None
            answer = scenario(selected)
            assert (answer is not None) == (expected is not None and expected <= budget)
            if answer is not None:
                assert scenario.verify(answer) and set(p for p,_ in answer.assignment) == selected
            native += 1
        scenarios.append((q,scenario,ranks,costs,budget))
    # Large ranks do not create resource-unit records.
    big = impl.table_scenario(((0,huge,huge,huge),),((1,),(1,)),2)
    assert big(frozenset((0,1))).assignment == ((0,0),(1,0))
    # Exhaustive forbidden sets with uniform original matroids and all forced seeds.
    for q in range(1,5):
        allsets = subsets(q)
        for forbidden in allsets[1:]:
            test = lambda chosen, forbidden=forbidden: tuple(sorted(chosen)) if not forbidden <= chosen else None
            for rank in range(q+1):
                oracle = lambda chosen,rank=rank: min(rank,len(chosen))
                for forced in allsets:
                    for width in range(1,4):
                        answer = impl.gate(q,rank,oracle,(test,),width,forced)
                        feasible = [s for s in allsets if len(s) == rank and not s & forced and test(s) is not None]
                        if answer.status == 'SUCCESS':
                            assert frozenset(answer.selected) in feasible
                        elif answer.status == 'INFEASIBLE':
                            assert not feasible
                        else:
                            cert = frozenset(answer.certificate)
                            assert answer.status == 'WIDTH VIOLATION' and len(cert) > width and oracle(cert) == len(cert)
                            assert test(cert) is None and all(test(cert-{p}) is not None for p in cert)
                            violations += 1
                        if len(forbidden) <= width:
                            assert answer.status != 'WIDTH VIOLATION'
                            assert (answer.status == 'SUCCESS') == bool(feasible)
                        h = q-rank-len(forced)
                        if h >= 0:
                            assert answer.nodes <= sum(width**i for i in range(h+1))
                        gates += 1
    # Actual budget/resource unit tests feed both bounded and Fibonacci clients.
    path = Path(__file__).resolve().parents[2] / 'robust-width-two-allocation/reference/width_two.py'
    spec = importlib.util.spec_from_file_location('_width_two_client',path)
    width_two = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = width_two
    spec.loader.exec_module(width_two)
    for q in range(2,5):
        ranks = (pool_rank(q,[(frozenset(range(q)),1)]),)
        costs = tuple((F(p+1,2),) for p in range(q))
        scenario = impl.table_scenario(ranks,costs,10)
        for rank in range(q+1):
            oracle = lambda chosen,rank=rank: min(len(chosen),rank)
            for forced in subsets(q):
                expected = any(len(s) == rank and not s & forced and native_unit(ranks,costs,10,s) is not None for s in subsets(q))
                generic = impl.gate(q,rank,oracle,(scenario,),2,forced)
                special = width_two.solve(q,rank,oracle,(scenario,),forced)
                assert (generic.status == 'SUCCESS') == (special.status == 'SUCCESS') == expected
                assert generic.status != 'WIDTH VIOLATION' and special.status != 'WIDTH VIOLATION'
                for answer in (generic,special):
                    if answer.status == 'SUCCESS':
                        assert all(scenario.verify(w) for w in answer.witnesses)
                integrations += 1
    # Full native multi-type budgets and nonuniform binary-represented player matroids.
    for _ in range(100):
        q,scenario,ranks,costs,budget = rng.choice(scenarios)
        columns = tuple(rng.randrange(16) for _ in range(q))
        oracle = lambda chosen: binary_rank(columns,chosen)
        rank = oracle(frozenset(range(q)))
        answer = impl.gate(q,rank,oracle,(scenario,),q)
        expected = any(len(s) == rank and oracle(s) == rank and (value := native_unit(ranks,costs,budget,s)) is not None and value <= budget
                       for s in subsets(q))
        assert (answer.status == 'SUCCESS') == expected
        assert answer.status != 'WIDTH VIOLATION'
        if expected:
            assert scenario.verify(answer.witnesses[0])
        gates += 1
    # A failed minimum-cost record must remain verifiable without search.
    expensive = impl.table_scenario(((0,1,1,1),),((2,),(3,)),1)
    saved_certificate = expensive.optimize((0,))
    saved = impl.minimum_cost
    impl.minimum_cost = lambda *args: (_ for _ in ()).throw(AssertionError('optimizer called'))
    assert expensive.verify(saved_certificate) and not expensive.affordable(saved_certificate)
    impl.minimum_cost = saved
    first = second = lambda s: len(s) <= 1
    costs = (F(10),F(1))
    valid = impl.minimum_cost(first,second,costs,1)
    forged_potential = (valid.potential[0],valid.potential[1]+100)
    assert not impl.verify_intersection(first,second,costs,1,replace(valid,potential=forged_potential))
    assert not impl.verify_intersection(first,second,costs,1,replace(valid,chosen=(0,)))
    assert not impl.verify_intersection(first,second,costs,1,SimpleNamespace(chosen=valid.chosen,potential=valid.potential,cut=None))
    underfull = impl.minimum_cost(first,second,costs,2)
    assert not impl.verify_intersection(first,second,costs,2,replace(underfull,cut=None))
    assert not expensive.verify(replace(saved_certificate,assignment=((0,1),)))
    invalid = 0
    for thunk in (lambda: impl.minimum_cost(first,second,(0.5,),1),
                  lambda: impl.minimum_cost(first,second,(1,),-1),
                  lambda: impl.table_scenario(((0,1,1,3),),((1,),(1,)),0),
                  lambda: impl.table_scenario(((0,1,1,1),),((1,),(1,)),-1),
                  lambda: impl.gate(2,1,lambda s: min(1,len(s)),(lambda s: (),),0)):
        try: thunk()
        except ValueError: invalid += 1
        else: raise AssertionError('invalid input accepted')
    print(f'PASS: {weighted} independent exhaustive weighted-intersection optima/cuts; {native} native assignment optima; {gates} bounded-gate cases; {violations} valid width violations; {integrations} native budget/resource integrations with Fibonacci gate; five forged certificate rejections; {invalid} malformed inputs; huge binary ranks/costs; optimizer-disabled verifier.')


if __name__ == '__main__':
    main()
