"""Original-optimum bottleneck commitment clients on complete rank tables.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
The residual selector enumerates bases; fast rank-local search is not claimed.
"""
from fractions import Fraction as F
from pathlib import Path
import importlib.util
import sys
from absorption import RankTable,position_commitment,rational

_name='_algorithm_frontier_many_workload'
if _name not in sys.modules:
    _path=Path(__file__).resolve().parents[2]/'many-size-scheduling/reference/workload.py'
    _spec=importlib.util.spec_from_file_location(_name,_path)
    _module=importlib.util.module_from_spec(_spec)
    sys.modules[_name]=_module
    _spec.loader.exec_module(_module)
workload=sys.modules[_name]


class CommitmentBackend:
    def __init__(self,q,ranks,sizes,budget,divisor=None,mode='workload'):
        if type(budget) is not int or budget<1 or mode not in ('workload','two-size'):
            raise ValueError('positive residual-rank budget and known mode required')
        self.backend=workload.WorkloadBackend(q,ranks,sizes)
        b=self.backend
        self.mode,self.budget=mode,min(budget,b.h)
        if mode=='two-size' and (divisor is not None or len({b.sizes[j] for j in b.small})>1):
            raise ValueError('two-size mode requires at most two active sizes and no divisor')
        minimum=3-F(2,self.budget) if self.budget else F(1)
        self.divisor=minimum if divisor is None else rational(divisor)
        if self.divisor<minimum:
            raise ValueError('divisor below the finite-rank unit threshold')
        self.quantum=b.grid/self.divisor.numerator if mode=='workload' else b.grid
        self.factor=(max(F(3,2),2-1/self.divisor) if mode=='workload'
                     else F(3,2) if self.budget<=2 else F(5,3))
        self.additive=b.u if mode=='workload' else F(0)
        self.position=None
        if b.player[-1]==b.h:
            weights=tuple(sum((b.sizes[j]*b.ranks[j][1<<p] for j in b.small),F(0)) for p in range(q))
            self.position=position_commitment(RankTable(q,b.player),weights,self.budget)
        self.commitment_load=(b.a+self.position.bottleneck
                              if self.position is not None and self.position.committed else F(0))
        self.last_trace={}

    def bound(self,target):
        return max(self.factor*target+self.additive,self.commitment_load)

    def _integer_state(self,target):
        b=self.backend
        cap=int(target//b.u)
        original=tuple(sum(b.ranks[j][s] for j in b.small) for s in range(1<<b.q))
        boxed=workload.corank.box_rank(original,cap)
        if boxed[-1]!=original[-1]:
            return None
        full=(1<<b.q)-1
        dual=tuple(cap*s.bit_count()+boxed[full^s]-original[-1] for s in range(1<<b.q))
        quota=cap-int((target-b.a)//b.u)
        return workload.State(b.u,cap,(1,)*len(b.small),original,boxed,dual,quota)

    def target(self,target):
        target=rational(target)
        if target<0:
            raise ValueError('nonnegative target required')
        target=(target//self.quantum)*self.quantum
        b=self.backend
        self.last_trace={'branch':'degenerate'}
        if not b.active or not b.small:
            return b.target(target).counts
        if target<b.a:
            self.last_trace['branch']='below-largest'
            return None
        if target>=2*b.a:
            self.last_trace['branch']='fractional-upper'
            return b.fractional_target(target)
        if self.position is None:
            self.last_trace['branch']='large-rank-loss'
            return None
        state=(b.state(target,self.quantum) if self.mode=='workload' else self._integer_state(target))
        if state is None:
            self.last_trace['branch']='workload-rank-loss'
            return None
        if self.mode=='workload':
            value=F(state.full_quota)/self.divisor
            if value.denominator!=1:
                raise AssertionError('engineered workload quota is not integral')
            quota=int(value)
        else:
            k=self.budget
            quota=(k*state.full_quota+2*k-2)//(3*k-2)
        committed=self.position.committed
        residual=b.select(state,quota,committed)
        if residual is None:
            self.last_trace['branch']='no-weak-basis'
            return None
        # Only the residual basis receives a lower dual quota. Position
        # commitments are charged by their ORIGINAL final singleton bounds.
        recipients=frozenset((*committed,*residual))
        lower=tuple(quota if p in residual else 0 for p in range(b.q))
        counts=b.reconstruct(state,lower,tuple(int(p in recipients) for p in range(b.q)))
        self.last_trace=dict(branch='commitment',committed=committed,residual=residual,
                             lower=lower,full_quota=state.full_quota,weak_quota=quota)
        if b.load(counts)>self.bound(target):
            raise AssertionError('original-optimum commitment load bound failed')
        return counts

    def optimize(self,with_fallback=True):
        b=self.backend
        saved=b.initial()
        if not b.active:
            return saved
        low=0
        high=int(max(b.load(saved),2*b.a)/self.quantum)
        while high-low>1:
            mid=(high+low)//2
            output=self.target(mid*self.quantum)
            if output is None:
                low=mid
            else:
                high,saved=mid,output
        if with_fallback:
            candidate=b.fallback()
            if b.load(candidate)<b.load(saved):saved=candidate
        return saved
