#!/usr/bin/env python3
"""Independent original graph/failure/prefix and exchange-wrapper checks.
Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reference'))
import list_colors as native


def partition(n,edge_pairs):
    adjacency = [[] for _ in range(n)]
    for u,v in edge_pairs:
        adjacency[u].append(v)
        adjacency[v].append(u)
    unseen,parts = set(range(n)),[]
    while unseen:
        root = min(unseen)
        reached,stack = {root},[root]
        while stack:
            v = stack.pop()
            for w in adjacency[v]:
                if w not in reached:
                    reached.add(w)
                    stack.append(w)
        unseen -= reached
        parts.append(tuple(sorted(reached)))
    return tuple(parts)


def original(vl,edges,failed=(),threshold=None):
    failed = set(failed)
    chosen,pairs = [],[]
    for i,e in sorted(enumerate(edges),key=lambda item:(item[1].weight,item[0])):
        if threshold is not None and (e.weight,i) > threshold: break
        if e.u == e.v or (set(vl[e.u]) | set(vl[e.v]) | set(e.colors)) & failed: continue
        before = partition(len(vl),pairs)
        after = partition(len(vl),pairs+[(e.u,e.v)])
        if after != before:
            chosen.append(i)
            pairs.append((e.u,e.v))
    return tuple(chosen)


totals = dict(graphs=0,prefixes=0,wrappers=0,exchanges=0,feature_matrices=0)
def compare(vl,edges,h,modulus=None,wrapper=False):
    certificate = native.build(vl,edges,h,modulus)
    assert len(certificate.records) <= certificate.support_bound
    assert len({i for i,_ in certificate.records}) == len(certificate.records)
    for i,e in certificate.records:
        assert (e.u,e.v,e.weight,set(e.colors)) == (edges[i].u,edges[i].v,F(edges[i].weight),set(edges[i].colors))
    palette = sorted(set().union(*(set(x) for x in vl),*(set(e.colors) for e in edges)))
    threshold = [None]+[(F(e.weight),i) for i,e in enumerate(edges)]
    for quantity in range(min(h,len(palette))+1):
        for failed in combinations(palette,quantity):
            for key in threshold:
                expected = original(vl,edges,failed,key)
                answer = certificate.forest(failed,key)
                assert answer == expected,(vl,edges,h,failed,key,certificate)
                # The canonical forests encode the same surviving original
                # prefix partition; derive it by graph flood fill again.
                full_edges = [(e.u,e.v) for i,e in enumerate(edges)
                              if e.u != e.v and (key is None or (e.weight,i) <= key)
                              and not (set(vl[e.u]) | set(vl[e.v]) | set(e.colors)) & set(failed)]
                assert partition(len(vl),full_edges) == partition(len(vl),[(edges[i].u,edges[i].v) for i in answer])
                totals['prefixes'] += 1
    assert certificate.forest((10**100,)) == original(vl,edges) if h else certificate.forest() == original(vl,edges)
    if wrapper:
        summary = native.single_failure(vl,edges)
        baseline = original(vl,edges)
        assert summary.baseline == baseline
        baseline_value = sum((F(edges[i].weight) for i in baseline),F(0))
        assert summary.baseline_value == baseline_value
        union = set(baseline)
        actual_incidence = sum(len(set(vl[e.u]) | set(vl[e.v]) | set(e.colors)) for e in edges if e.u != e.v)
        assert summary.incidence_total == actual_incidence
        assert summary.updates <= sum(e.u != e.v for e in edges)+2*actual_incidence
        replacements = destroyed_tree = 0
        for index,c in enumerate(summary.palette):
            forest = original(vl,edges,(c,))
            difference = summary.color(c)
            assert summary.indexed(index) == difference
            assert summary.forest(c) == forest
            assert set(difference.removed) == set(baseline)-set(forest)
            assert set(difference.added) == set(forest)-set(baseline)
            assert difference.value == sum((F(edges[i].weight) for i in forest),F(0))
            assert len(difference.added) <= len(difference.removed)
            replacements += len(difference.added)
            destroyed_tree += len(difference.removed)
            union.update(forest)
        assert summary.replacement_total == replacements <= destroyed_tree
        assert {i for i,_ in summary.records} == union
        assert summary.forest(10**100) == baseline and summary.color(10**100).value == baseline_value
        saved = native.ReferenceMSF.update,native.build
        def unavailable(*a,**kw): raise AssertionError('query called preprocessing')
        try:
            native.ReferenceMSF.update=native.build=unavailable
            assert summary.forest(10**100) == baseline and certificate.forest() == baseline
        finally: native.ReferenceMSF.update,native.build=saved
        totals['wrappers'] += 1
        totals['exchanges'] += summary.updates
    totals['graphs'] += 1
    return certificate


def monomials(variables,degree):
    return tuple(powers for powers in product(range(degree+1),repeat=variables) if sum(powers) <= degree)


def independent_rank(rows,modulus=None):
    a = [[F(x) if modulus is None else int(x)%modulus for x in row] for row in rows]
    if not a: return 0
    rank = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(rank,len(a)) if a[i][j]),None)
        if pivot is None: continue
        a[rank],a[pivot] = a[pivot],a[rank]
        factor = 1/a[rank][j] if modulus is None else pow(a[rank][j],-1,modulus)
        a[rank] = [x*factor if modulus is None else x*factor%modulus for x in a[rank]]
        for i in range(rank+1,len(a)):
            value = a[i][j]
            a[i] = [x-value*y if modulus is None else (x-value*y)%modulus for x,y in zip(a[i],a[rank])]
        rank += 1
        if rank == len(a): break
    return rank


def main():
    palette = ((),(0,),(1,),(0,1))
    for vl in product(palette,repeat=3):
        for edge_mask in range(8):
            edges = tuple(native.Edge(u,v,F(i%2)) for i,(u,v) in enumerate(combinations(range(3),2)) if edge_mask >> i & 1)
            for h in (0,1,2): compare(vl,edges,h,wrapper=h == 1 and edge_mask == 7)
    rng = random.Random(10028)
    for case in range(90):
        n = rng.randrange(1,6)
        vl = tuple(tuple(c for c in range(3) if rng.randrange(3) == 0) for _ in range(n))
        edges = tuple(native.Edge(rng.randrange(n),rng.randrange(n),F(rng.randrange(-4,5),2),
                                  tuple(c for c in range(3) if rng.randrange(4) == 0)) for _ in range(rng.randrange(9)))
        compare(vl,edges,case % 3,modulus=7 if case % 2 else None,wrapper=True)
    # Genuine cubic cases, including repeated endpoint/edge colors and parallel
    # edges; compare exact feature rank with the explicit small monomial matrix.
    for case in range(30):
        n = 4
        vl = tuple((rng.randrange(3),) for _ in range(n))
        edges = tuple(native.Edge(u,v,rng.randrange(-2,3),(rng.randrange(3),)) for u,v in combinations(range(n),2))
        edges += (native.Edge(0,1,F(-1,2),(2,)),)
        certificate = compare(vl,edges,case % 3,modulus=7 if case % 2 else None,wrapper=True)
        assert all(c.mode == 'CUBIC' for c in certificate.components)
        f = native.field(7 if case % 2 else None)
        normalized,records = native.validate(vl,edges)
        _,info = native.component_features(tuple(range(n)),records,normalized,case % 3,f)
        universe = sorted(set().union(*(set(v) for v in vl),*(set(e.colors) for e in edges)))
        codes = {c:i+1 for i,c in enumerate(universe)}
        points = tuple((codes[next(iter(vl[v]))],codes[e.colors[0]]) for _,e in records for v in (e.u,e.v))
        # The nonleading coefficients of (T-x)(T-y) are xy and -(x+y).
        matrix = [[(x*y)**a*(-x-y)**b for x,y in points] for a,b in monomials(2,min(case % 3,len(universe)))]
        assert independent_rank(matrix,f.modulus) == info.feature_rank
        full_rows = tuple(tuple(row[2*j+1] if e.u == v else -row[2*j] if e.v == v else 0
                                for j,(_,e) in enumerate(records)) for v in range(n) for row in matrix)
        chosen,previous = [],0
        for stop,(i,_) in enumerate(records,1):
            current = independent_rank(tuple(row[:stop] for row in full_rows),f.modulus)
            if current > previous: chosen.append(i)
            previous = current
        assert tuple(i for i,_ in certificate.records) == tuple(chosen)
        totals['feature_matrices'] += 1
    # Characteristic two, empty lists and overlapping lists share the same
    # decoder; one real label plus dummy zero fits F_2 exactly.
    compare(((),(0,),(),(0,)),tuple(native.Edge(u,v,i%2,(0,) if i%3 == 0 else ())
             for i,(u,v) in enumerate(combinations(range(4),2))),2,modulus=2,wrapper=True)
    # Huge encoded h never enumerates a formal universe. Formal dimension can
    # be exponentially larger than the actual pair-feature rank.
    labels = tuple(tuple(range(i,18+i)) for i in range(6))
    edges = tuple(native.Edge(u,v,u-v,tuple(range(40,48))) for u,v in combinations(range(6),2))
    certificate = native.build(labels,edges,10**100)
    assert all(c.feature_rank <= 2*len(edges) for c in certificate.components)
    assert any(c.formal_dimension > 10**10 for c in certificate.components)
    assert certificate.forest() == original(labels,edges)
    assert certificate.forest(tuple(range(18))) == original(labels,edges,tuple(range(18)))
    # Lower examples: every original edge is compulsory under an allowed query.
    # Vertex lists and mixed lists use the simple apex/base construction.
    lower = 0
    for h,dv,de in ((1,1,0),(1,2,0),(1,1,1),(2,1,1)):
        degree = dv+de
        subsets = tuple(combinations(range(h+degree),degree))
        vl = tuple(tuple(s[:dv]) for s in subsets)+((),)*3
        edges = tuple(native.Edge(i,len(subsets)+j,1,tuple(s[dv:])) for i,s in enumerate(subsets) for j in range(3))
        certificate = compare(vl,edges,h)
        assert len(certificate.records) == len(edges)
        lower += 1
    # Mixed multigraph sharp leading coefficient includes the compulsory core.
    for h in (0,1,2):
        q = h+2
        vl = tuple((c,) for c in range(1,q+1))+((0,),)*3
        edges = tuple(native.Edge(a,b,1,(0,)) for a,b in combinations(range(q),2))
        edges += tuple(native.Edge(q+j,a-1,1,(b,)) for j in range(3) for a,b in combinations(range(1,q+1),2))
        certificate = compare(vl,edges,h,wrapper=h == 1)
        assert len(certificate.records) == len(edges)
        lower += 1
    # Both query objects reject invalid failure indices and repeated colors.
    small = native.build(((0,),()),(native.Edge(0,1,1),),1)
    one = native.single_failure(((0,),()),(native.Edge(0,1,1),))
    invalid = 0
    for thunk in (lambda:native.build(((0,0),),(),1),lambda:native.build((('a',),),(),1),
                  lambda:native.build(((),),(native.Edge(0,1,1),),1),lambda:native.build(((),),(native.Edge(0,0,1.0),),1),
                  lambda:native.build(((),),(),True),lambda:native.build(((0,1),()),(native.Edge(0,1,1),),1,2),
                  lambda:small.forest((0,0)),lambda:small.forest((0,1)),lambda:small.forest((True,)),
                  lambda:small.forest(threshold=(1.0,0)),lambda:one.indexed(True),lambda:one.color(-1)):
        try: thunk()
        except ValueError: invalid += 1
        else: raise AssertionError('malformed input accepted')
    print('PASS mixed/list graph:',totals,f'; {lower} compulsory lower-bound fixtures; huge binary h/formal dimension; '
          f'Q/F7/F2; signed rational ties; producer-disabled queries; {invalid} malformed inputs')


if __name__ == '__main__': main()
