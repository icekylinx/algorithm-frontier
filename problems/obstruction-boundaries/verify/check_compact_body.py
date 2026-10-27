#!/usr/bin/env python3
"""Independent original graph cuts and exact compact-body identities.
Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import subprocess
import sys
REFERENCE=Path(__file__).resolve().parents[1]/'reference'
sys.path.insert(0,str(REFERENCE))
from compact_body import Body,QueryViolation,SparseQueryViolation,CubeViolation,reduce_maxcut,evaluate,verify_violation,separate,recover_cut
counts=dict(graphs=0,thresholds=0,queries=0,nonmembers=0,recovered=0,rejected=0)


def need(condition,message):
    if not condition: raise AssertionError(message)


def check(n,edges):
    cuts=[(bits,sum(w for u,v,w in edges if bits[u]!=bits[v])) for bits in product((0,1),repeat=n)]
    optimum=max(cost for _,cost in cuts)
    degree=[sum(w for u,v,w in edges if x in (u,v)) for x in range(n)]
    maximum=max(degree,default=0)
    total=sum(w for _,_,w in edges)
    for threshold in sorted({-1,0,optimum-1,optimum,total,total+1,maximum*n//2}):
        body=reduce_maxcut(n,edges,threshold)
        need(body.dimension==n+1 and len(body.checks)<=len(edges)+2*n+1,'size bound')
        need(all(len(row)<=2 for row in body.checks),'arity bound')
        need(all(z in (0,F(1,2)) for z in body.point),'point alphabet')
        need(all(w>0 and w.denominator==1 for w in body.weights),'positive integer weights')
        for bits,cost in cuts:
            for t in (0,1):
                value,weight=evaluate(body,(*bits,t))
                expected=cost-threshold if t else cost-maximum*sum(bits)
                need(value-F(1,4)*weight==expected,'signed reduction identity')
                need(value>=0 and value>=-F(1,4)*weight,'lower inequality')
                need(verify_violation(body,QueryViolation((*bits,t)))==(expected>0),'certificate implication')
                counts['queries']+=1
        witness=separate(body)
        need((witness is None)==(optimum<=threshold),'membership equivalence')
        if witness is not None:
            need(type(witness) is SparseQueryViolation,'streamed sparse query')
            dense=QueryViolation(tuple(int(i in witness.ones) for i in range(n+1)))
            need(verify_violation(body,dense),'dense cut query')
            need(recover_cut(n,edges,threshold,dense)==recover_cut(n,edges,threshold,witness),'sparse cut recovery')
            counts['nonmembers']+=1
            selected=set(recover_cut(n,edges,threshold,witness))
            need(sum(w for u,v,w in edges if (u in selected)!=(v in selected))>threshold,'cut recovery')
            counts['recovered']+=1
        counts['thresholds']+=1
    counts['graphs']+=1


def boundaries():
    lower=Body(1,((0,),),(1,),(-F(1,2),))
    need(verify_violation(lower,QueryViolation((1,))),'lower inequality witness')
    need(not verify_violation(lower,QueryViolation((0,))),'zero query')
    cube=Body(0,((),),(1,),(2,))
    need(separate(cube)==CubeViolation(0) and verify_violation(cube,CubeViolation(0)),'cube witness')
    need(separate(Body(0,(),(),())) is None,'empty body')
    need(separate(Body(10**100,((),),(1,),(0,))) is None,'empty-check dimension gate')
    sparse_body=Body(10**100,((10**100-1,),),(1,),(F(1,2),))
    need(verify_violation(sparse_body,SparseQueryViolation((10**100-1,))),'binary-dimension sparse witness')
    need(separate(sparse_body)==SparseQueryViolation((10**100-1,)),'unused-dimension compression')
    for bad in [SparseQueryViolation((0,0)),SparseQueryViolation((True,)),SparseQueryViolation((1,)),SparseQueryViolation([0]),None,{},QueryViolation((True,)),QueryViolation((2,)),QueryViolation(()),QueryViolation([1]),CubeViolation(True),CubeViolation(-1),CubeViolation(1)]:
        need(not verify_violation(lower,bad),'malformed witness')
        counts['rejected']+=1
    invalid=[lambda:Body(True,(),(),()),lambda:Body(1,((1,),),(1,),(0,)),
             lambda:Body(1,((0,0),),(1,),(0,)),lambda:Body(1,((0,),),(0,),(0,)),
             lambda:Body(1,((0,),),(1.0,),(0,)),lambda:Body(1,((0,),),(1,),(True,)),
             lambda:Body(1,((0,),),(1,),(0,),F(3,4)),lambda:reduce_maxcut(2,((0,0,1),),0),
             lambda:reduce_maxcut(2,((0,1,-1),),0),lambda:reduce_maxcut(2,((0,True,1),),0),
             lambda:reduce_maxcut(2,((0,1,1),),False)]
    for call in invalid:
        try: call()
        except ValueError: pass
        else: raise AssertionError('malformed input accepted')
        counts['rejected']+=1
    code='''
import compact_body as c
body=c.Body(1,((0,),),(1,),(c.F(1,2),))
c.separate=lambda *args: (_ for _ in ()).throw(RuntimeError('search forbidden'))
c.reduce_maxcut=c.separate
if not c.verify_violation(body,c.QueryViolation((1,))):
 raise SystemExit('search-free verification failed')
'''
    subprocess.run([sys.executable,'-B','-c',code],cwd=REFERENCE,check=True)


if __name__=='__main__':
    check(0,());check(1,())
    for n in range(2,5):
        pairs=tuple(combinations(range(n),2))
        for mask in range(1<<len(pairs)):
            for profile in range(3):
                edges=tuple((u,v,1 if profile==0 else (j+profile)%4) for j,(u,v) in enumerate(pairs) if mask>>j&1)
                check(n,edges)
    check(3,((0,1,2),(0,1,3),(1,2,0),(0,2,5)))
    check(3,((0,1,10**100),(0,2,10**100+1),(1,2,7)))
    boundaries()
    print('PASS compact body reduction:',counts)
