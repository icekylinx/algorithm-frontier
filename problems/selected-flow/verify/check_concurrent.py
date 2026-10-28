"""Independent path/vertex checks. Attribution: icekylinx and GPT-6 Astra Pro."""
from dataclasses import replace
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import random
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'reference'))
import concurrent as impl


def solve_square(a, b):
    n = len(b)
    t = [list(map(F, row)) + [F(rhs)] for row, rhs in zip(a,b)]
    for j in range(n):
        pivot = next((i for i in range(j,n) if t[i][j]), None)
        if pivot is None:
            return None
        t[j], t[pivot] = t[pivot], t[j]
        v = t[j][j]; t[j] = [x/v for x in t[j]]
        for i in range(n):
            if i != j:
                v = t[i][j]; t[i] = [x-v*y for x,y in zip(t[i],t[j])]
    return tuple(row[-1] for row in t)


def vertex_max(a,b,c):
    n = len(c)
    rows = list(a) + [tuple(-F(i == j) for j in range(n)) for i in range(n)]
    rhs = list(b) + [F(0)]*n
    best = None
    for active in combinations(range(len(rows)), n):
        x = solve_square([rows[i] for i in active], [rhs[i] for i in active])
        if x is not None and all(sum(v*w for v,w in zip(row,x)) <= cap for row,cap in zip(rows,rhs)):
            val = sum(v*w for v,w in zip(c,x))
            best = val if best is None else max(best,val)
    return best


def path_opt(net, selected, budgets=(), setup=None):
    # Native path formulation constructed independently of arc conservation LP.
    arcs = []
    for e,(u,v,_) in enumerate(net.edges):
        arcs.append((u,v,e))
        if net.undirected:
            arcs.append((v,u,e))
    paths = []
    for i in selected:
        s,t,_ = net.commodities[i]
        def visit(v, seen, ids):
            if v == t:
                paths.append((i,ids)); return
            for j,(u,w,_) in enumerate(arcs):
                if u == v and w not in seen:
                    visit(w, seen | {w}, ids+(j,))
        visit(s,{s},())
    n = 1+len(paths)
    a,b = [],[]
    def add(row, cap):
        a.append(tuple(map(F,row))); b.append(F(cap))
    for i in selected:
        row = [-net.commodities[i][2]] + [int(owner == i) for owner,_ in paths]
        add(row,0); add([-x for x in row],0)
    for e,(_,_,cap) in enumerate(net.edges):
        add([0]+[sum(arcs[j][2] == e for j in ids) for _,ids in paths],cap)
    rows = list(budgets)
    if setup:
        fees,costs,cap = setup
        residual = cap-sum(fees[i] for i in selected)
        if residual < 0:
            return None
        rows.append((costs,residual))
    for costs,cap in rows:
        add([0]+[sum(costs[i][j] for j in ids) for i,ids in paths],cap)
    return vertex_max(a,b,[F(1)]+[F(0)]*(n-1))


def main():
    rng = random.Random(271028)
    primitive = native = tampered = separators = 0
    for n in range(1,4):
        for _ in range(40):
            a = [[F(rng.randrange(-2,5),rng.randrange(1,4)) for _ in range(n)] for _ in range(3)]
            b = [F(rng.randrange(5)) for _ in a]
            for i in range(n):
                a.append([F(i == j) for j in range(n)]); b.append(F(3))
            c = [F(rng.randrange(-2,5)) for _ in range(n)]
            x,y = impl.simplex(a,b,c)
            assert impl.verify_lp(a,b,c,x,y)
            assert sum(v*w for v,w in zip(c,x)) == vertex_max(a,b,c)
            primitive += 1
    pairs = [(u,v) for u in range(3) for v in range(3) if u != v]
    for mask in range(64):
        edges = tuple((u,v,F(1+j%3,1+j%2)) for j,(u,v) in enumerate(pairs) if mask>>j&1)
        net = impl.Network(3,edges,((0,2,F(3,2)),))
        costs = (tuple(F((j+1)%3,2) for j in range(len(edges))),)
        for budgets in ((),((costs,F(2,3)),)):
            cert = impl.optimize_fixed(net,(0,),budgets)
            assert impl.verify_fixed(net,cert,budgets)
            assert cert.rate == path_opt(net,(0,),budgets)
            assert not impl.verify_fixed(net,replace(cert,primal=(cert.rate+1,)+cert.primal[1:]),budgets)
            assert not impl.verify_fixed(net,replace(cert,dual=tuple(F(0) for _ in cert.dual)),budgets)
            native += 1; tampered += 2
            for rate in (F(0),cert.rate,cert.rate+F(1,7)):
                row = impl.separate(net,(rate,),budgets)
                assert (row is None) == (rate <= cert.rate)
                if row is not None:
                    assert all(x >= 0 for x in (*row.lengths,*row.multipliers,*row.coefficients))
                    assert row.coefficients[0] == net.commodities[0][2]*(row.potentials[0][0]-row.potentials[0][2])
                    for j,(u,v,_) in enumerate(net.edges):
                        assert row.potentials[0][u]-row.potentials[0][v] <= row.lengths[j]+sum(row.multipliers[h]*charges[0][j] for h,(charges,_) in enumerate(budgets))
                    capacity = sum(row.lengths[j]*edge[2] for j,edge in enumerate(net.edges))+sum(row.multipliers[h]*cap for h,(_,cap) in enumerate(budgets))
                    assert row.capacity == capacity < row.coefficients[0]*rate
                    assert row.coefficients[0]*cert.rate <= capacity
                separators += 1
    # Shared physical capacity must include both commodity directions.
    for cap,d0,d1 in product(range(3),range(1,4),range(1,4)):
        net = impl.Network(2,((0,1,cap),),((0,1,d0),(1,0,d1)),True)
        cert = impl.optimize_fixed(net,(0,1))
        assert cert.rate == F(cap,d0+d1) == path_opt(net,(0,1))
        assert impl.verify_fixed(net,cert)
        native += 1
        row = impl.separate(net,(cert.rate+1,cert.rate+1))
        assert row is not None and sum(row.coefficients)*(cert.rate+1) > row.capacity
        assert len(row.lengths) == 1 and row.capacity == cap*row.lengths[0]
        for i,(source,target,_) in enumerate(net.commodities):
            assert abs(row.potentials[i][0]-row.potentials[i][1]) <= row.lengths[0]
        separators += 1
    for _ in range(20):
        edges = tuple((u,v,F(rng.randrange(3),2)) for u,v in pairs if rng.randrange(2))
        net = impl.Network(3,edges,((0,2,1),(1,2,F(3,2))))
        costs = tuple(tuple(F(rng.randrange(3),2) for _ in edges) for _ in range(2))
        budgets = ((costs,F(rng.randrange(3),2)),)
        cert = impl.optimize_fixed(net,(0,1),budgets)
        assert cert.rate == path_opt(net,(0,1),budgets)
        assert impl.verify_fixed(net,cert,budgets)
        native += 1
    # Shared-budget example from manuscript, varying budgets and fees.
    net = impl.Network(4,((0,1,100),(2,3,100)),((0,1,1),(2,3,1)))
    costs = ((F(100),F(0)),(F(0),F(1)))
    setups = 0
    for fee,cap in product((0,20,80,101),(0,1,50,100)):
        setup = ((F(0),F(fee)),costs,F(cap))
        best = impl.optimize_selected(net,1,setup=setup)
        expected = max(F(cap,100), min(F(100),F(cap-fee)) if cap>=fee else F(0))
        assert best.rate == expected and impl.verify_fixed(net,best,setup=setup)
        for i in range(2):
            cert = impl.optimize_fixed(net,(i,),setup=setup)
            expected_i = path_opt(net,(i,),setup=setup)
            assert (None if cert is None else cert.rate) == expected_i
        setups += 1
    setup = ((0,80),costs,100)
    best = impl.optimize_selected(net,1,setup=setup)
    assert best.selected == (1,) and best.rate == 20
    assert impl.optimize_selected(net,1,lambda selected: selected == (0,),setup=setup).rate == 1
    assert impl.optimize_selected(net,1,lambda selected: False) is None
    assert impl.optimize_selected(net,1,setup=((101,101),costs,100)) is None
    # Queries verify without any optimizer available.
    saved = impl.simplex
    impl.simplex = lambda *args: (_ for _ in ()).throw(AssertionError('search called'))
    assert impl.verify_fixed(net,best,setup=setup)
    impl.simplex = saved
    rejected = 0
    for thunk in (lambda: impl.Network(2,((0,1,0.5),),()),
                  lambda: impl.Network(2,((0,0,1),),()),
                  lambda: impl.Network(2,(),((0,1,0),)),
                  lambda: impl.optimize_fixed(net,()),
                  lambda: impl.optimize_fixed(net,(0,0)),
                  lambda: impl.optimize_fixed(net,(2,)),
                  lambda: impl.optimize_fixed(net,(0,),((costs,-1),)),
                  lambda: impl.optimize_fixed(net,(0,),setup=((-1,0),costs,10))):
        try: thunk()
        except ValueError: rejected += 1
        else: raise AssertionError('invalid input accepted')
    print(f'PASS: {primitive} independent LP vertex optima; {native} independent native path optima; {setups} setup-budget profiles; {tampered} certificate mutations; {rejected} malformed inputs; {separators} normalized Farkas queries; search-free verifier.')


if __name__ == '__main__':
    main()
