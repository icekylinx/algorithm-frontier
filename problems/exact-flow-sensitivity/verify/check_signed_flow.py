"""Independent exhaustive original unit flows, signed objectives and deletions.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reference'))
from unit_flow import Arc
import signed_flow as native
from flow_certificates import verify_flow,verify_infeasible,verify_maximum


def original_optima(n,arcs,failed):
    result={}
    for bits in product((0,1),repeat=len(arcs)):
        if failed is not None and bits[failed]:continue
        balance=[0]*n;cost=F(0)
        for used,arc in zip(bits,arcs):
            if used:
                balance[arc.tail]+=1;balance[arc.head]-=1;cost+=arc.cost
        balance=tuple(balance)
        if balance not in result or cost<result[balance]:result[balance]=cost
    return result


def validate(n,arcs,balance,used,failed):
    assert type(used) is tuple and len(set(used))==len(used)
    assert failed not in used
    actual=[0]*n;cost=F(0)
    for i in used:
        assert type(i) is int and 0<=i<len(arcs)
        a=arcs[i];actual[a.tail]+=1;actual[a.head]-=1;cost+=a.cost
    assert tuple(actual)==balance
    return cost


def fixtures():
    pairs=((0,0),(0,1),(1,0),(1,1))
    profiles=((1,1,1,1),(-2,1,-1,2),(F(-1,3),0,F(2,3),F(-1,2)))
    for mask in range(16):
        for costs in profiles:
            yield 2,tuple(Arc(*p,F(costs[i])) for i,p in enumerate(pairs) if mask>>i&1)
    pairs=((0,1),(1,2),(2,0),(0,2),(2,1),(1,0))
    for mask in range(64):
        for costs in ((-3,1,1,0,2,-1),(F(1,3),F(-2,3),F(1,2),F(-1,2),1,-1)):
            yield 3,tuple(Arc(*p,F(costs[i])) for i,p in enumerate(pairs) if mask>>i&1)
    yield 1,(Arc(0,0,F(-7)),Arc(0,0,F(-1,3)),Arc(0,0,F(0)),Arc(0,0,F(5)))
    yield 3,(Arc(0,1,F(1)),Arc(0,1,F(-2)),Arc(1,0,F(1)),Arc(1,2,F(0)),
             Arc(2,1,F(-3)),Arc(2,2,F(-2)))
    yield 4,(Arc(0,1,F(2)),Arc(2,3,F(-5)),Arc(3,2,F(1)),Arc(2,2,F(-3)))
    yield 2,(Arc(0,1,F(10**100)),Arc(1,0,F(-10**100)-F(1,10**100)),Arc(0,0,F(-1,10**100)))


counts=dict(graphs=0,balances=0,infeasible=0,maximum=0,maximum_queries=0,oracles=0,queries=0,unreachable=0,disabled=0,rejected=0,long_hubs=0)
for n,arcs in fixtures():
    m=len(arcs)
    optima={failed:original_optima(n,arcs,failed) for failed in (None,*range(m))}
    balances=set(optima[None])
    if n>1:
        extra=[0]*n;extra[0]=m+1;extra[-1]=-m-1;balances.add(tuple(extra))
    for balance in sorted(balances):
        for failed,expected in optima.items():
            cert,cut=native.minimum_balance(n,arcs,balance,failed)
            if balance in expected:
                assert cut is None and cert.cost==expected[balance]
                assert verify_flow(n,arcs,balance,cert,failed)
            else:
                assert cert is None and verify_infeasible(n,arcs,balance,cut,failed)
                counts['infeasible']+=1
            counts['balances']+=1
        oracle,cut=native.build_balance_oracle(n,arcs,balance)
        if balance not in optima[None]:
            assert oracle is None and verify_infeasible(n,arcs,balance,cut)
            continue
        assert cut is None
        counts['oracles']+=1
        k=len(oracle.baseline)
        assert oracle.record_count()<=30*(1+k+n*(isqrt(k)+1))
        assert set(vars(oracle))=={'baseline','baseline_cost','_paths','_values','support'}
        for failed in (None,*range(m),m+17,-1):
            key=failed if failed in optima else None
            expected=optima[key].get(balance)
            output=oracle.query(failed)
            assert oracle.value(failed)==expected
            if expected is None:
                assert output is None;counts['unreachable']+=1
            else:
                assert validate(n,arcs,balance,output,failed)==expected
                assert set(output)<=set(oracle.support)
            counts['queries']+=1
    if n>1:
        maximum_oracle=native.MaximumBalanceOracle(n,arcs,0,n-1)
        for failed,expected in optima.items():
            candidates=[(balance[0],cost) for balance,cost in expected.items()
                        if balance[0]>=0 and balance[-1]==-balance[0] and not any(balance[1:-1])]
            value=max(x[0] for x in candidates)
            cost=min(c for v,c in candidates if v==value)
            cert=native.minimum_maximum(n,arcs,0,n-1,failed)
            assert cert.value==value and cert.flow.cost==cost
            assert verify_maximum(n,arcs,0,n-1,cert,failed)
            query_value,query_cost,query_used=maximum_oracle.query(failed)
            balance=tuple(value if p==0 else -value if p==n-1 else 0 for p in range(n))
            assert query_value==value and query_cost==cost==validate(n,arcs,balance,query_used,failed)
            assert set(query_used)<=set(maximum_oracle.support)
            counts['maximum_queries']+=1
            counts['maximum']+=1
    counts['graphs']+=1
# A long negative cycle plus a single shortcut forces hub reports containing
# both removed baseline-position tags and an inserted original-ID tag.
size=40
long_arcs=tuple(arc for p in range(size) for arc in (Arc(p,p,F(9)),Arc(p,(p+1)%size,F(-1))))
long_arcs += (Arc(0,size//2,F(1)),)
long_oracle,_=native.build_balance_oracle(size,long_arcs,(0,)*size)
assert long_oracle._paths.hubs and long_oracle.baseline_cost==-size
for p in range(size):
    failed=2*p+1
    expected=F(1-size//2) if p<size//2 else F(0)
    output=long_oracle.query(failed)
    assert validate(size,long_arcs,(0,)*size,output,failed)==expected==long_oracle.value(failed)
    assert set(output)<=set(long_oracle.support)
    counts['long_hubs']+=1

# A dense original ground is discarded, while queries retain only compact data.
arcs=[Arc(0,1,F(i)) for i in range(1024)]
oracle,_=native.build_balance_oracle(2,arcs,(1,-1))
assert len(oracle.support)<=2 and oracle.record_count()<30
maximum_oracle=native.MaximumBalanceOracle(2,(Arc(0,1,F(-2)),Arc(1,1,F(-3))),0,1)
arcs.clear()
old_min,old_feasible,old_shortest=native.minimum_balance,native.balance_feasibility,sys.modules['unit_flow']._shortest
def forbidden(*args,**kwargs):raise AssertionError('producer called during compact query')
native.minimum_balance=native.balance_feasibility=sys.modules['unit_flow']._shortest=forbidden
try:
    assert oracle.query()==(0,)
    assert oracle.query(0)==(1,) and oracle.value(0)==1
    assert oracle.query(1)==(0,)
    assert long_oracle.value(1)==F(-19) and len(long_oracle.query(1))==21
    assert long_oracle.query(79)==()
    assert maximum_oracle.query(0)==(0,F(-3),(1,))
    assert maximum_oracle.query(1)==(1,F(-2),(0,))
    counts['disabled']+=7
finally:
    native.minimum_balance, native.balance_feasibility,sys.modules['unit_flow']._shortest=old_min,old_feasible,old_shortest
cert,cut=native.minimum_balance(2,(Arc(0,1,F(-1)),),(10**100,-10**100))
assert cert is None and verify_infeasible(2,(Arc(0,1,F(-1)),),(10**100,-10**100),cut)
for call in [lambda:native.minimum_balance(0,(),()),lambda:native.minimum_balance(2,(),(1,0)),
             lambda:native.minimum_balance(2,(Arc(0,1,0.5),),(0,0)),
             lambda:native.minimum_balance(2,(),(True,-1)),lambda:native.minimum_maximum(2,(),0,0),
             lambda:oracle.query(True),lambda:native.minimum_balance(2,(),(0,0),0)]:
    try:call()
    except ValueError:counts['rejected']+=1
    else:raise AssertionError('malformed query accepted')
print('PASS signed original unit flow:',counts,'; isolated cycles, loops, parallel arcs and100-digit guards')
