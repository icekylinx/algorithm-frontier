"""Binary convex pricing and actual residual-configuration column generation.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
The native outer loop uses finite Farkas generation and exact Bland pivots,
not the polynomial-cut ellipsoid implementation of the mathematical theorem.
Only coordinate-box local families are supplied by this optimizer.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd,lcm
from pathlib import Path
import importlib.util
import sys


def load(name,path):
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name,path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


counts = load('_recipient_fractional_counts',Path(__file__).with_name('counts.py'))
lp = load('_recipient_fractional_lp',Path(__file__).resolve().parents[2]/'selected-flow/reference/concurrent.py')


def exact(value):
    if type(value) not in (int,F): raise ValueError('exact int or Fraction required')
    return F(value)


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))


def cost_of(vector,linear,hinges):
    return sum((linear[j]*n+sum((weight*max(0,n-breakpoint) for breakpoint,weight in hinges[j]),F(0))
                for j,n in enumerate(vector)),F(0))


@dataclass(frozen=True)
class Priced:
    counts: tuple
    value: F
    cost: F


def price(caps,profits,linear,hinges,budget,epsilon):
    """FPTAS for separable signed convex integer cost, exact cost budget."""
    caps,profits = tuple(caps),tuple(exact(v) for v in profits)
    linear = tuple(exact(v) for v in linear)
    hinges = tuple(tuple((s,exact(w)) for s,w in row) for row in hinges)
    budget,epsilon = exact(budget),exact(epsilon)
    m = len(caps)
    if (len(profits) != m or len(linear) != m or len(hinges) != m
            or any(type(c) is not int or c < 0 for c in caps) or any(v < 0 for v in profits)
            or any(type(s) is not int or s < 0 or w < 0 for row in hinges for s,w in row)
            or not 0 < epsilon <= F(1,2)):
        raise ValueError('box counts, nonnegative profits/hinges and 0<epsilon<=1/2 required')
    base = [0]*m
    base_cost = F(0)
    chunks = []
    for j,cap in enumerate(caps):
        endpoints = sorted({0,cap}|{s for s,w in hinges[j] if 0 < s < cap and w})
        for left,right in zip(endpoints,endpoints[1:]):
            slope = linear[j]+sum((w for s,w in hinges[j] if s <= left),F(0))
            quantity = right-left
            if slope <= 0:
                base[j] += quantity
                base_cost += quantity*slope
            elif profits[j] > 0:
                power = 1
                while quantity:
                    take = min(power,quantity)
                    chunks.append((j,take,profits[j]*take,slope*take))
                    quantity -= take
                    power *= 2
    remaining = budget-base_cost
    if remaining < 0: return None
    chunks = tuple(chunk for chunk in chunks if chunk[3] <= remaining)
    chosen = ()
    if chunks:
        delta = epsilon*max(chunk[2] for chunk in chunks)/len(chunks)
        # Each state keeps minimum exact rational cost and an item bit mask.
        states = {0:(F(0),0)}
        for i,(_,_,profit,cost) in enumerate(chunks):
            scaled = int(profit/delta)
            if not scaled: continue
            next_states = dict(states)
            for total,(previous,items) in states.items():
                candidate = previous+cost
                key = total+scaled
                if candidate <= remaining and (key not in next_states or candidate < next_states[key][0]):
                    next_states[key] = candidate,items | (1 << i)
            states = next_states
        selected = states[max(states)][1]
        chosen = tuple(chunk for i,chunk in enumerate(chunks) if selected >> i & 1)
    for j,quantity,_,_ in chosen: base[j] += quantity
    vector = tuple(base)
    # Move selected units of each type to its cheapest prefix. Its original
    # convex cost can only decrease relative to the relaxed segment cost.
    actual = cost_of(vector,linear,hinges)
    if actual > budget: raise RuntimeError('pricing violated exact cost budget')
    return Priced(vector,dot(vector,profits),actual)


def strict_price(caps,profits,linear,hinges,threshold,target,epsilon):
    """Weak violating column, or sound absence of a hard-target violation."""
    linear = tuple(exact(v) for v in linear)
    hinges = tuple(tuple((s,exact(w)) for s,w in row) for row in hinges)
    threshold,target,epsilon = exact(threshold),exact(target),exact(epsilon)
    if target <= 0: raise ValueError('positive hard target required')
    denominator = lcm(*(v.denominator for v in linear),
                      *(w.denominator for row in hinges for _,w in row))
    quantity = denominator*threshold
    ceiling = -(-quantity.numerator//quantity.denominator)
    budget = F(ceiling-1,denominator)
    answer = price(caps,profits,linear,hinges,budget,epsilon)
    return answer if answer is not None and answer.value >= (1-epsilon)*target else None


@dataclass(frozen=True)
class Configuration:
    owner: int
    counts: tuple


@dataclass(frozen=True)
class Mass:
    configuration: Configuration
    weight: F


@dataclass(frozen=True)
class Point:
    target: F
    masses: tuple


class Residual:
    def __init__(self,player_rank,resource_ranks,values,quotas=None,support=None,cut_sets=None):
        player_rank = tuple(player_rank)
        if not player_rank or len(player_rank) & (len(player_rank)-1):
            raise ValueError('complete player rank table required')
        self.q = len(player_rank).bit_length()-1
        self.player = counts.RankTable(self.q,player_rank)
        if any(value > s.bit_count() for s,value in enumerate(player_rank)):
            raise ValueError('player table must be a matroid rank')
        self.rank = player_rank[-1]
        self.resources = tuple(counts.RankTable(self.q,tuple(row)) for row in resource_ranks)
        self.m = len(self.resources)
        values = tuple(values)
        if all(type(v) in (int,F) for v in values):
            if len(values) != self.m: raise ValueError('one intrinsic value per type required')
            self.values = tuple(tuple(exact(v) for v in values) for _ in range(self.q))
        else:
            try:
                self.values = tuple(tuple(exact(v) for v in row) for row in values)
            except TypeError:
                raise ValueError('exact intrinsic values or owner/type value rows required') from None
        self.quotas = (tuple(tuple(resource.caps[p] for resource in self.resources) for p in range(self.q))
                       if quotas is None else tuple(tuple(row) for row in quotas))
        if (len(self.values) != self.q or any(len(row) != self.m for row in self.values)
                or any(v < 0 for row in self.values for v in row)
                or len(self.quotas) != self.q or any(len(row) != self.m for row in self.quotas)
                or any(type(n) is not int or not 0 <= n <= self.resources[j].caps[p]
                       for p,row in enumerate(self.quotas) for j,n in enumerate(row))):
            raise ValueError('matching nonnegative profits and original coordinate boxes required')
        if support is not None and (type(support) is not int or support < 0):
            raise ValueError('nonnegative support budget required')
        if cut_sets is not None and support is not None:
            raise ValueError('choose explicit cuts or a support bound')
        self.cuts = (tuple((j,s) for j in range(self.m) for s in range(1 << self.q)
                           if support is None or s.bit_count() <= support)
                     if cut_sets is None else tuple(tuple(pair) for pair in cut_sets))
        if (any(len(pair) != 2 or type(pair[0]) is not int or not 0 <= pair[0] < self.m
                or type(pair[1]) is not int or not 0 <= pair[1] < 1 << self.q for pair in self.cuts)
                or len(set(self.cuts)) != len(self.cuts)):
            raise ValueError('distinct original resource/subset cut IDs required')
        self.bounds = tuple(self.resources[j].values[s] for j,s in self.cuts)
        self.marginals = tuple(tuple(self.resources[j].values[s | (1 << p)]-self.resources[j].values[s]
                                     for p in range(self.q)) for j,s in self.cuts)
        self.dimension = self.q*(self.m+1)
        self.last_trace = {}

    def local(self,configuration):
        return (type(configuration) is Configuration and type(configuration.owner) is int
                and 0 <= configuration.owner < self.q and type(configuration.counts) is tuple
                and len(configuration.counts) == self.m
                and all(type(n) is int and 0 <= n <= self.quotas[configuration.owner][j]
                        for j,n in enumerate(configuration.counts)))

    def column(self,configuration):
        if not self.local(configuration): raise ValueError('original box configuration required')
        p,n = configuration.owner,configuration.counts
        e = tuple(int(owner == p) for owner in range(self.q))+tuple(n[j] if owner == p else 0
                       for owner in range(self.q) for j in range(self.m))
        h = tuple(max(0,n[j]-marginal[p]) for (j,_),marginal in zip(self.cuts,self.marginals))
        return e,h

    def verify(self,point):
        try:
            if type(point) is not Point or exact(point.target) < 0 or type(point.masses) is not tuple: return False
            x,y = [F(0)]*self.q,[[F(0)]*self.q for _ in self.resources]
            residual = [F(0)]*len(self.cuts)
            for mass in point.masses:
                if type(mass) is not Mass or exact(mass.weight) <= 0 or not self.local(mass.configuration): return False
                p,n = mass.configuration.owner,mass.configuration.counts
                if dot(n,self.values[p]) < point.target: return False
                x[p] += mass.weight
                for j,value in enumerate(n): y[j][p] += mass.weight*value
                for i,((j,_),marginal) in enumerate(zip(self.cuts,self.marginals)):
                    residual[i] += mass.weight*max(0,n[j]-marginal[p])
            return (sum(x,F(0)) == self.rank
                    and all(sum(x[p] for p in range(self.q) if s >> p & 1) <= rank for s,rank in enumerate(self.player.values))
                    and all(sum(row[p] for p in range(self.q) if s >> p & 1) <= rank
                            for resource,row in zip(self.resources,y) for s,rank in enumerate(resource.values))
                    and all(value <= bound for value,bound in zip(residual,self.bounds)))
        except (ValueError,TypeError,AttributeError,IndexError): return False

    def aggregate_vertex(self,alpha):
        alpha = tuple(exact(v) for v in alpha)
        if len(alpha) != self.dimension: raise ValueError('original aggregate price dimension required')
        selected = 0
        x = [0]*self.q
        for p in sorted(range(self.q),key=lambda p:(-alpha[p],p)):
            if self.player.values[selected | (1 << p)] > self.player.values[selected]:
                selected |= 1 << p
                x[p] = 1
        y = [[0]*self.m for _ in range(self.q)]
        for j,resource in enumerate(self.resources):
            prefix = previous = 0
            order = sorted((p for p in range(self.q) if alpha[self.q+p*self.m+j] > 0),
                           key=lambda p:(-alpha[self.q+p*self.m+j],p))
            for p in order:
                prefix |= 1 << p
                y[p][j] = resource.values[prefix]-previous
                previous = resource.values[prefix]
        return tuple(x)+tuple(v for row in y for v in row)

    def zero(self):
        vertex = self.aggregate_vertex((F(0),)*self.dimension)
        return Point(F(0),tuple(Mass(Configuration(p,(0,)*self.m),F(1)) for p in range(self.q) if vertex[p]))

    def separate_subsets(self,point):
        """First violated retained subset row, for an explicit local mass list."""
        for i,((j,s),marginal) in enumerate(zip(self.cuts,self.marginals)):
            left = sum((exact(mass.weight)*max(0,mass.configuration.counts[j]-marginal[mass.configuration.owner])
                        for mass in point.masses),F(0))
            if left > self.bounds[i]: return j,s,left,self.bounds[i]
        return None

    def reserved_basis(self,j,reserved):
        resource = self.resources[j]
        reserved = resource.counts(reserved)
        current,previous,result = [0]*self.q,0,[]
        for p in range(self.q):
            current[p] = reserved[p]
            rank = resource.rank(current)
            result.append(rank-previous)
            previous = rank
        return tuple(result)

    def _price(self,alpha,zeta,p,target,epsilon):
        linear = tuple(alpha[self.q+p*self.m+j] for j in range(self.m))
        hinges = tuple(tuple((marginal[p],weight) for (h,_),marginal,weight
                             in zip(self.cuts,self.marginals,zeta) if h == j)
                       for j in range(self.m))
        return strict_price(self.quotas[p],self.values[p],linear,hinges,-alpha[p],target,epsilon)

    def weak_target(self,target,epsilon):
        target,epsilon = exact(target),exact(epsilon)
        if target < 0 or not 0 < epsilon < 1: raise ValueError('nonnegative target and 0<epsilon<1 required')
        epsilon = min(epsilon,F(1,2))
        if not target or not self.rank: return self.zero()
        configurations,vertices = [],[]
        d,m = self.dimension,len(self.cuts)
        size = 2*d+m
        self.last_trace = dict(iterations=0,columns=0,vertices=0)
        while True:
            self.last_trace['iterations'] += 1
            a = []
            for configuration in configurations:
                e,h = self.column(configuration)
                a.append(tuple(-v for v in e)+tuple(e)+tuple(-v for v in h)+(F(0),))
            for vertex in vertices:
                a.append(tuple(vertex)+tuple(-v for v in vertex)+self.bounds+(F(1),))
            a.extend(((F(1),)*size+(F(0),),(F(0),)*size+(F(1),)))
            b = (F(0),)*(len(a)-2)+(F(1),F(1))
            objective = (F(0),)*size+(F(1),)
            primal,dual = lp.simplex(a,b,objective)
            if not lp.verify_lp(a,b,objective,primal,dual): raise RuntimeError('invalid finite Farkas LP certificate')
            margin = primal[-1]
            if margin == 0:
                split = len(configurations)
                total = sum(dual[split:split+len(vertices)],F(0))
                if total < 1: raise RuntimeError('finite primal normalization failed')
                masses = tuple(Mass(configuration,weight/total) for configuration,weight in zip(configurations,dual)
                               if weight > 0)
                answer = Point((1-epsilon)*target,masses)
                if not self.verify(answer): raise RuntimeError('finite primal violates original comparator')
                return answer
            beta = tuple(v/margin for v in primal[:-1])
            alpha = tuple(beta[i]-beta[d+i] for i in range(d))
            zeta = beta[2*d:]
            vertex = self.aggregate_vertex(alpha)
            if dot(alpha,vertex)+dot(zeta,self.bounds) > -1:
                if vertex in vertices: raise RuntimeError('aggregate generator did not progress')
                vertices.append(vertex)
                self.last_trace['vertices'] += 1
                continue
            for p in range(self.q):
                priced = self._price(alpha,zeta,p,target,epsilon)
                if priced is not None:
                    configuration = Configuration(p,priced.counts)
                    if configuration in configurations: raise RuntimeError('configuration generator did not progress')
                    configurations.append(configuration)
                    self.last_trace['columns'] += 1
                    break
            else:
                return None  # Valid original hard-target Farkas system.

    def optimize(self,epsilon):
        epsilon = exact(epsilon)
        if not 0 < epsilon < 1: raise ValueError('0<epsilon<1 required')
        epsilon = min(epsilon,F(1,2))
        best = self.zero()
        values = tuple(v for row in self.values for v in row if v > 0)
        if not values or not self.rank: return best
        denominator = lcm(*(v.denominator for v in values))
        quantum = F(gcd(*(int(v*denominator) for v in values)),denominator)
        upper_value = sum((resource.values[-1]*max((self.values[p][j] for p in range(self.q)),default=F(0))
                           for j,resource in enumerate(self.resources)),F(0))
        quantity = upper_value/((1-epsilon)*quantum)
        low,high = 0,-(-quantity.numerator//quantity.denominator)+1
        calls = 0
        while high-low > 1:
            middle = (high+low)//2
            point = self.weak_target(middle*quantum,epsilon)
            calls += 1
            if point is None: high = middle
            else: low,best = middle,point
        self.last_trace['optimization_calls'] = calls
        return best
