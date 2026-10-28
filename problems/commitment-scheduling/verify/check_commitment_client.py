"""Original scheduling optima for the two bottleneck-commitment clients.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reference'))
from commitment import CommitmentBackend


def uniform(q,rank):return tuple(min(rank,s.bit_count()) for s in range(1<<q))


def original_schedules(q,ranks):
    columns=[]
    for f in ranks:
        columns.append(tuple(x for x in product(*(range(f[1<<p]+1) for p in range(q)))
                             if sum(x)==f[-1] and all(sum(v for p,v in enumerate(x) if s>>p&1)<=cap
                                                     for s,cap in enumerate(f))))
    return tuple(product(*columns))


def makespan(q,sizes,counts):
    return max((sum(size*row[p] for size,row in zip(sizes,counts)) for p in range(q)),default=F(0))


fixtures=[
    (0,(),()),(2,(),()),
    (2,(uniform(2,1),),(F(3,2),)),
    (2,(uniform(2,1),uniform(2,2)),(F(3),F(1))),
    (2,(uniform(2,1),uniform(2,1)),(F(5,2),F(1))),
    (2,((0,1,0,1),(0,0,2,2)),(F(2),F(1,3))),
    (2,((0,2,0,2),uniform(2,1)),(F(3),F(1))),
    (2,(uniform(2,1),uniform(2,1),uniform(2,1)),(F(4),F(1),F(2))),
    (3,(uniform(3,2),(0,2,2,4,2,4,2,4)),(F(3),F(1))),
]
counts=dict(instances=0,targets=0,optimizations=0,commitment_outputs=0,two_size=0,rejections=0)
for q,ranks,sizes in fixtures:
    native=original_schedules(q,ranks)
    optimum=min(makespan(q,sizes,x) for x in native)
    for mode in ['workload']+(['two-size'] if len(set(sizes))<=2 else []):
        for budget in (1,2):
            solver=CommitmentBackend(q,ranks,sizes,budget,mode=mode)
            b=solver.backend
            targets={F(0),b.a,F(3,2)*b.a,2*b.a,optimum,optimum+b.grid}
            for target in sorted(targets):
                output=solver.target(target)
                if output is None:assert optimum>target
                else:
                    assert output in native and makespan(q,sizes,output)<=solver.bound(target)
                    counts['commitment_outputs']+=int(solver.last_trace['branch']=='commitment')
                counts['targets']+=1
            for fallback in (False,True):
                output=solver.optimize(with_fallback=fallback)
                bound=solver.bound(optimum)
                if fallback:bound=min(bound,optimum+b.a)
                assert output in native and makespan(q,sizes,output)<=bound
                counts['optimizations']+=1
            counts['two_size']+=int(mode=='two-size')
    counts['instances']+=1
# The original optimum is four; private positive quotas on the committed
# machine are impossible. Zero extension still gives a valid commitment.
q=3;ranks=(uniform(3,2),(0,2,2,4,2,4,2,4));sizes=(F(3),F(1))
for mode in ('workload','two-size'):
    solver=CommitmentBackend(q,ranks,sizes,1,mode=mode)
    output=solver.target(4)
    assert output is not None and output in original_schedules(q,ranks)
    assert solver.last_trace['committed']==(0,) and solver.last_trace['lower'][0]==0
    assert solver.backend.target(4,budget=1,divisor=1).failure=='cap'
# Positive-slack workload quota uses engineered integer arithmetic.
solver=CommitmentBackend(2,(uniform(2,1),uniform(2,2)),(3,1),1,divisor=F(3,2))
assert solver.target(3) is not None
assert solver.last_trace['full_quota']*2==solver.last_trace['weak_quota']*3
# A binary-large one-size instance uses no unit enumeration.
huge=10**100
solver=CommitmentBackend(1,((0,huge),),(F(1,3),),1,mode='two-size')
assert solver.target(F(huge,3))==((huge,),)
bad=[lambda:CommitmentBackend(1,((0,1),),(1,),0),
     lambda:CommitmentBackend(1,((0,1),),(1,),1,divisor=F(1,2)),
     lambda:CommitmentBackend(1,((0,1),)*3,(1,2,3),1,mode='two-size'),
     lambda:solver.target(-1)]
for call in bad:
    try:call()
    except ValueError:counts['rejections']+=1
    else:raise AssertionError('malformed client input accepted')
print('PASS original-optimum commitment clients:',counts,'; zero-extension, slack and100-digit guards')
