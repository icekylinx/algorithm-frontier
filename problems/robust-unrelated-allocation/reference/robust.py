"""Exact adaptive-scenario allocation on one actual common player basis.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
Local rational LPs enumerate active bases; no fast oracle runtime is claimed
for that enumeration. Scenario costs/budgets are independent, setup is common.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import importlib.util
import sys


def load():
    name = '_robust_unrelated_joint'
    if name not in sys.modules:
        path = Path(__file__).resolve().parents[2]/'unrelated-values-joint-role/reference/joint.py'
        spec = importlib.util.spec_from_file_location(name,path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


joint = load()
prefix = joint.prefix


@dataclass(frozen=True)
class Allocation:
    basis: tuple
    scenarios: tuple  # original type-major counts in each explicitly indexed scenario


class Robust:
    def __init__(self,player_rank,scenarios,setup=None):
        # Scenario tuple: (resource_ranks, type-major values, type-major costs, budget).
        self.scenarios = tuple(joint.Joint(player_rank,ranks,values,costs,budget,setup)
                               for ranks,values,costs,budget in scenarios)
        if not self.scenarios: raise ValueError('nonempty explicit scenario list required')
        first = self.scenarios[0]
        self.q,self.rank,self.player,self.setup = first.q,first.rank,first.player,first.setup
        self.last_trace = {}

    def verify(self,allocation):
        try:
            return (type(allocation) is Allocation and type(allocation.scenarios) is tuple
                    and len(allocation.scenarios) == len(self.scenarios)
                    and all(scenario.verify(joint.Allocation(allocation.basis,counts))
                            for scenario,counts in zip(self.scenarios,allocation.scenarios)))
        except (TypeError,ValueError,AttributeError): return False

    def minimum(self,allocation):
        if not self.verify(allocation): raise ValueError('invalid original robust allocation')
        if not self.rank: return None
        return min((scenario.minimum(joint.Allocation(allocation.basis,counts))
                    for scenario,counts in zip(self.scenarios,allocation.scenarios)),default=None)

    def zero(self):
        basis = joint.greedy(self.player,range(self.q),self.setup)
        answer = Allocation(basis,tuple(tuple((0,)*self.q for _ in scenario.ranks) for scenario in self.scenarios))
        return answer if self.verify(answer) else None

    def region(self,scenario,basis):
        paid = sum((self.setup[p] for p in basis),F(0))
        return joint.Region(self.q,scenario.ranks,scenario.values,scenario.costs,scenario.budget-paid)

    def fractional(self,basis):
        basis = tuple(basis)
        selected = joint.mask(basis,self.q)
        if not basis or len(basis) != self.rank or self.player[selected] != self.rank:
            raise ValueError('nonempty actual basis required')
        paid = sum((self.setup[p] for p in basis),F(0))
        results = tuple(joint.Region(self.q,scenario.ranks,scenario.values,scenario.costs,scenario.budget-paid,
                                    {(j,p) for j in range(len(scenario.ranks)) for p in basis}).optimum(basis)
                        for scenario in self.scenarios)
        if any(result is None for result in results): raise ValueError('unaffordable common basis')
        value = min(result[0] for result in results)
        # Original fixed-basis reoptimization: safely discard assignments elsewhere.
        counts = tuple(tuple(tuple(row[p] if p in basis else F(0) for p in range(self.q)) for row in result[1])
                       for result in results)
        return value,counts

    def gap(self,full,weak,forced=(),global_base=None):
        full,weak = joint.core.rational(full),joint.core.rational(weak)
        if not full > weak > 0: raise ValueError('positive full and weaker targets required')
        if global_base is not None:
            global_base = joint.admissible(global_base,full/(full-weak))
            if tuple(forced): raise ValueError('global cover owns its forced seed')
        def extension(seed):
            def prepare(allowed):
                basis = joint.greedy(self.player,allowed,self.setup)
                if len(basis) != self.rank: return None
                if any(sum((self.setup[p] for p in basis),F(0)) > scenario.budget for scenario in self.scenarios): return None
                return prefix.Choice(basis)
            def separate(allowed,choice,rates):
                for scenario in self.scenarios:
                    region = self.region(scenario,choice.selected)
                    row,_ = region.separate(allowed,rates)
                    if row is not None: return row
                return None
            counts = {}
            answer = prefix.gap(self.q,self.rank,full,weak,prepare,separate,seed,counts=counts)
            for name,value in counts.items(): self.last_trace[name] = self.last_trace.get(name,0)+value
            return None if answer is None else answer.choice
        return (extension(tuple(forced)) if global_base is None else
                prefix.whole_ground(self.q,self.rank,global_base,extension))

    def denominator_bound(self):
        # Fixed-basis product LP: all scenario counts plus one common value.
        n = 1+self.rank*sum(len(scenario.ranks) for scenario in self.scenarios)
        data = [F(0),F(1),*self.setup]
        for scenario in self.scenarios:
            data.extend(F(x) for row in scenario.ranks for x in row)
            data.extend(x for row in scenario.values+scenario.costs for x in row)
            data.extend((scenario.budget,scenario.budget-sum(self.setup,F(0))))
        length = max(max(abs(x.numerator).bit_length(),x.denominator.bit_length()) for x in data)
        # Sum of any setup subset has numerator/denominator bounded by the
        # product of q input denominators times q input numerators.
        length = (self.q+2)*(length+1)
        return factorial(n)*(1 << ((n+2)*length*n))

    def recover(self,basis,fractional):
        output = []
        for scenario,counts in zip(self.scenarios,fractional):
            allowed = {(j,p) for j in range(len(scenario.ranks)) for p in basis}
            rounded = joint.round_counts(self.q,scenario.ranks,scenario.values,scenario.costs,counts,allowed)
            output.append(rounded)
        answer = Allocation(tuple(basis),tuple(output))
        if not self.verify(answer): raise RuntimeError('original robust rounding failed')
        return answer

    def optimize(self,epsilon,global_base=None):
        epsilon = joint.core.rational(epsilon)
        if not 0 < epsilon < 1: raise ValueError('accuracy must lie strictly between zero and one')
        if global_base is not None: global_base = joint.admissible(global_base,1/epsilon)
        initial = self.zero()
        if initial is None or not self.rank: return initial
        self.last_trace = {}
        upper = min(sum((max(row,default=F(0))*rank[-1] for row,rank in zip(scenario.values,scenario.ranks)),F(0))
                    for scenario in self.scenarios)
        if upper == 0: return initial
        result = prefix.rational_optimize(1-epsilon,self.denominator_bound(),upper,prefix.Choice(initial.basis),
                                         lambda t:self.gap(t,(1-epsilon)*t,global_base=global_base),
                                         lambda choice:self.fractional(choice.selected))
        return self.recover(result.choice.selected,result.witness)
