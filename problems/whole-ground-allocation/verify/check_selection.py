"""Independent finite checks of actual prefix recursion and block streaming.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from pathlib import Path
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'reference'))
import selection as impl


def subsets(q):
    return tuple(frozenset(i for i in range(q) if mask >> i & 1) for mask in range(1 << q))


def binary_rank(columns, selected):
    pivots = {}
    for i in selected:
        value = columns[i]
        while value:
            bit = value.bit_length()-1
            if bit not in pivots:
                pivots[bit] = value
                break
            value ^= pivots[bit]
    return len(pivots)


def main():
    prefix = packing = matroid = covers = streams = recovery = flows = 0
    for n in range(9):
        for deficit in range(n+1):
            for ratio in (F(2),F(3),F(3,2),F(5,2)):
                expected = set()
                for length in range(1,n+1):
                    for word in product((0,1),repeat=length):
                        if (sum(word) <= deficit and ratio*sum(word) > length
                                and all(ratio*sum(word[:j]) <= j for j in range(length))):
                            expected.add(word)
                counts = {}
                answer = list(impl.first_crossings(tuple(reversed(range(n))),ratio,deficit,counts))
                assert {word for _,word in answer} == expected
                for deleted,word in answer:
                    assert deleted == tuple(n-1-j for j,bit in enumerate(word) if bit)
                assert all(not (len(w) < len(v) and v[:len(w)] == w) for _,w in answer for _,v in answer)
                mass = sum(((1/ratio)**sum(word)*(1-1/ratio)**(len(word)-sum(word)) for _,word in answer),F(0))
                assert mass <= 1
                if deficit:
                    quantity = (ratio-1)*deficit
                    zero_budget = (quantity.numerator+quantity.denominator-1)//quantity.denominator-1
                    assert counts['prefix_states'] <= (n+1)*comb(deficit+zero_budget,deficit)
                prefix += 1
    # Binary-large numerical ratio budgets are clipped by actual word length.
    for ratio in (F(1 << 150),F((1 << 150)+1,1 << 150)):
        counts = {}
        answer = list(impl.first_crossings(range(8),ratio,3,counts))
        assert answer and counts['prefix_states'] <= 2**9
    rng = random.Random(271032)
    for case in range(240):
        q = rng.randrange(1,8)
        rank = rng.randrange(1,q+1)
        allsets = subsets(q)
        rows = tuple(impl.Row(tuple(F(rng.randrange(5),rng.randrange(1,4)) for _ in range(q)),F(rng.randrange(13),2))
                     for _ in range(rng.randrange(1,5)))
        full,weak = ((F(2),F(1)),(F(3),F(2)),(F(5),F(3)))[case % 3]
        left,right = tuple(rng.randrange(8) for _ in range(q)),tuple(rng.randrange(8) for _ in range(q))
        costs = tuple(F(rng.randrange(-2,5),2) for _ in range(q))
        budget = F(rng.randrange(9),2)
        ind1 = lambda chosen: binary_rank(left,chosen) == len(chosen)
        ind2 = lambda chosen: binary_rank(right,chosen) == len(chosen)
        if case % 2:
            prepare = impl.common_matroid_selector(rank,ind1,ind2,costs,budget)
            family = [s for s in allsets if len(s) == rank and ind1(s) and ind2(s) and sum(costs[i] for i in s) <= budget]
            matroid += 1
        else:
            prepare = impl.uniform_selector(rank,costs,budget)
            family = [s for s in allsets if len(s) == rank and sum(costs[i] for i in s) <= budget]
        forced = tuple(sorted(rng.sample(range(q),rng.randrange(q-rank+1))))
        def feasible(chosen,target):
            return all(target*sum(row.coefficients[i] for i in chosen) <= row.capacity for row in rows)
        candidates = [s for s in family if not s & set(forced)]
        counts = {}
        answer = impl.gap(q,rank,full,weak,prepare,impl.explicit_separator(rows,q),forced,counts=counts)
        if answer is None:
            assert not any(feasible(s,full) for s in candidates)
        else:
            chosen = frozenset(answer.choice.selected)
            assert chosen in candidates and feasible(chosen,weak)
        ratio = full/(full-weak)
        a,b = ratio.numerator,ratio.denominator
        power = F(a**a,b**b*(a-b)**(a-b))
        h = q-rank-len(forced)
        assert counts['nodes']**b <= (h+1)**b*power**h
        assert counts['prefix_states']**b <= ((q+1)*(h+1))**b*power**h
        packing += 1
    # Failed selectors and zero-deficit rejections are actual reached work.
    counts = {}
    select = lambda allowed: impl.Choice((0,)) if 0 in allowed else None
    assert impl.gap(2,1,2,1,select,impl.explicit_separator((impl.Row((10,0),0),),2),counts=counts) is None
    assert counts['nodes'] == 2 and counts['selector_rejections'] == 1
    counts = {}
    assert impl.gap(1,1,2,1,impl.uniform_selector(1),impl.explicit_separator((impl.Row((1,),0),),1),counts=counts) is None
    assert counts['zero_deficit_rejections'] == 1
    reached = []
    assert impl.gap(4,1,2,1,impl.uniform_selector(1),
                    impl.explicit_separator((impl.Row((4,3,2,1),0),),4),
                    observe=lambda allowed,*args:reached.append(allowed)) is None
    assert frozenset((0,3)) in reached  # root word 011 deletes two at once
    for n in range(8):
        for p in range(n+1):
            for base in (F(2),F(4),F(27,4)):
                k,cover = impl.local_cover(n,p,base)
                values = [F(comb(n,t),comb(p,t))*base**(p-t) for t in range(p+1)]
                assert values[k] == min(values)
                assert len(cover) <= (n+2)*F(comb(n,k),comb(p,k))
                assert all(any(mask & target == mask for mask in cover)
                           for target in (sum(1 << i for i in chosen) for chosen in combinations(range(n),p)))
                assert values[k] <= (2-1/base)**n
                covers += 1
    for q in range(1,13):
        for c in range(q):
            counts = {}
            seeds = list(impl.cover_seeds(q,c,F(4),counts))
            assert all(len(seed) <= c for seed in seeds)
            assert all(any(set(seed) <= set(omitted) for seed in seeds) for omitted in combinations(range(q),c))
            if q >= 4:
                length = q.bit_length()-1
                blocks = (q+length-1)//length
                cost = sum((F(4)**(c-len(seed)) for seed in seeds),F(0))
                assert cost <= ((length+1)*(length+2))**blocks*F(7,4)**q
                assert counts['local_records'] <= (length+1)*2**length
            # Extension is allowed weak success and is complete on one fixed witness.
            protected_omissions = frozenset(range(c))
            answer = impl.whole_ground(q,q-c,F(4),lambda seed: ('actual',seed) if set(seed) <= protected_omissions else None)
            assert answer is not None and set(answer[1]) <= protected_omissions
            streams += 1
    # Nonmonotone weak answers, all-zero values and binary-large denominator grids.
    for case in range(80):
        values = tuple(F(rng.randrange(12),rng.randrange(1,6)) for _ in range(5))
        alpha = (F(1,2),F(2,3),F(3,4))[case % 3]
        bound = max(value.denominator for value in values)
        upper = max(values)+1
        counter = [0]
        def oracle(target):
            counter[0] += 1
            if target <= max(values):
                return next(i for i,value in enumerate(values) if value >= alpha*target)
            affordable = [i for i,value in enumerate(values) if value >= alpha*target]
            return affordable[0] if counter[0] % 2 and affordable else None
        result = impl.rational_optimize(alpha,bound,upper,0,oracle,lambda i:(values[i],('original',i)))
        assert result.value >= alpha*max(values) and result.witness == ('original',result.choice)
        recovery += 1
    zero = impl.rational_optimize(F(1,2),1,0,0,lambda target:None,lambda i:(0,()))
    assert zero.value == 0
    huge = 1 << 120
    tiny = F(1,huge)
    result = impl.rational_optimize(F(1,2),huge,tiny,0,lambda target:0 if target <= tiny else None,lambda i:(tiny,()))
    assert result.value == tiny and result.calls < 400
    flow = impl._load('_algorithm_frontier_concurrent','selected-flow/reference/concurrent.py')
    network = flow.Network(6,((0,1,5),(2,3,4),(4,5,3)),((0,1,1),(2,3,1),(4,5,1)))
    routing = ((F(100),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(3)))
    for fees,cap,rank,full,weak in product(((0,0,0),(0,4,2)),(0,5,8),(1,2),(F(2),F(4)),(F(1),)):
        setup = (fees,routing,cap)
        family = tuple(combinations(range(3),rank))
        def original_rate(chosen):
            residual = cap-sum(fees[i] for i in chosen)
            if residual < 0:
                return None
            charge = sum(routing[i][i] for i in chosen)
            return min(min(network.edges[i][2] for i in chosen),F(residual,charge))
        rates = [original_rate(chosen) for chosen in family]
        answer = impl.flow_gap(network,rank,full,weak,setup=setup)
        if answer is None:
            assert not any(rate is not None and rate >= full for rate in rates)
        else:
            gap_result,certificate = answer
            assert certificate.rate >= weak and flow.verify_fixed(network,certificate,setup=setup)
            assert certificate.rate == original_rate(certificate.selected)
            assert gap_result.counts['nodes'] >= 1
        flows += 1
    invalid = 0
    for thunk in (lambda: list(impl.first_crossings((0,),1,1)),
                  lambda: impl.gap(2,1,1,1,impl.uniform_selector(1),lambda *args:None),
                  lambda: impl.gap(2,1,2,1,lambda allowed:impl.Choice((2,)),lambda *args:None),
                  lambda: impl.gap(2,1,2,1,impl.uniform_selector(1),lambda *args:impl.Row((-1,2),0)),
                  lambda: impl.explicit_separator((impl.Row((1,),-1),),1),
                  lambda: list(impl.cover_seeds(4,4,2)),
                  lambda: impl.rational_optimize(F(1,2),0,1,0,lambda t:None,lambda i:(0,()))):
        try: thunk()
        except ValueError: invalid += 1
        else: raise AssertionError('invalid input accepted')
    print(f'PASS: {prefix} exhaustive first-crossing languages/Kraft/state bounds; {packing} original weighted packing gap cases ({matroid} certified two-matroid selectors); {covers} exact local containment covers; {streams} complete streamed seed families; {recovery} nonmonotone rational recoveries; {flows} native adaptive setup-flow gaps; {invalid} malformed inputs; binary-large ratios/denominators; failed selector and zero-deficit accounting.')


if __name__ == '__main__':
    main()
