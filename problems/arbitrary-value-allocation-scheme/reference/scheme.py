"""Exact complete-table arbitrary-value allocation profile scheme.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
LP recovery streams active systems; that finite cost is additional to the
manuscript's profile factor with paid polynomial LP/intersection primitives.
No binary supply, accuracy table, or individual resource unit is expanded.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import importlib.util
import sys


def load(name,path):
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name,Path(__file__).resolve().parents[2] / path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


intrinsic = load('_arbitrary_value_intrinsic','intrinsic-values-near-two/reference/intrinsic.py')
profiles = load('_arbitrary_value_profiles','arbitrary-processing-scheduling/reference/profiles.py')
exact = intrinsic.weighted.rational


def ceil(value):
    value = F(value)
    return -(-value.numerator//value.denominator)


def active_vertex(rows,dimension,objective=None,counts=None):
    """First feasible vertex, or exact linear minimum; stream active systems."""
    rows = tuple(sorted(set((tuple(map(F,a)),F(b)) for a,b in rows)))
    if counts is not None:
        counts['calls'] = counts.get('calls',0)+1
        counts['max_dimension'] = max(counts.get('max_dimension',0),dimension)
        counts['max_rows'] = max(counts.get('max_rows',0),len(rows))
    # Exact substitution of coordinates with coincident scalar lower/upper
    # bounds avoids carrying masked or profile-fixed coordinates through LPs.
    original_dimension = dimension
    free,fixed = list(range(dimension)),{}
    while True:
        if any(not any(a) and b < 0 for a,b in rows): return None
        rows = tuple((a,b) for a,b in rows if any(a))
        lower,upper = {},{}
        for row,bound in rows:
            support = tuple(i for i,a in enumerate(row) if a)
            if len(support) != 1: continue
            i = support[0]
            value = bound/row[i]
            table = upper if row[i] > 0 else lower
            table[i] = value if i not in table else (min if row[i] > 0 else max)(table[i],value)
        if any(lower[i] > upper[i] for i in lower.keys() & upper.keys()): return None
        equal = {i:lower[i] for i in lower.keys() & upper.keys() if lower[i] == upper[i]}
        if not equal: break
        kept = tuple(i for i in range(len(free)) if i not in equal)
        for i,value in equal.items(): fixed[free[i]] = value
        rows = tuple((tuple(a[i] for i in kept),b-sum((a[i]*v for i,v in equal.items()),F(0))) for a,b in rows)
        free = [free[i] for i in kept]
    def expand(point):
        answer = [F(0)]*original_dimension
        for i,value in fixed.items(): answer[i] = value
        for i,value in zip(free,point): answer[i] = value
        return tuple(answer)
    dimension = len(free)
    if counts is not None: counts['max_active_dimension'] = max(counts.get('max_active_dimension',0),dimension)
    if dimension == 0: return expand(())
    reduced_objective = None if objective is None else tuple(objective[i] for i in free)
    best = value = None
    for active in combinations(rows,dimension):
        if counts is not None: counts['active_systems'] = counts.get('active_systems',0)+1
        point = intrinsic.linear.solve_square(active)
        if point is None or any(sum((a*x for a,x in zip(row,point)),F(0)) > b for row,b in rows):
            continue
        if reduced_objective is None:
            return expand(point)
        score = sum((a*x for a,x in zip(reduced_objective,point)),F(0))
        if best is None or (score,point) < (value,best): best,value = point,score
    return None if best is None else expand(best)


@dataclass(frozen=True)
class Allocation:
    basis: tuple
    counts: tuple  # original type-major integer owner vectors


@dataclass(frozen=True)
class Bin:
    index: int
    lower: F
    upper: F
    types: tuple  # original type IDs at this original owner


@dataclass(frozen=True)
class PlayerGroups:
    owner: int
    small: tuple
    bins: tuple


@dataclass(frozen=True)
class Plan:
    basis: tuple
    target: F
    counts: tuple  # one occupied-bin count tuple per basis owner


class Scheme:
    def __init__(self,player_rank,resource_ranks,values,costs,setup,budget,epsilon):
        # Reuse canonical exact rank-table validation, including player loops.
        self.core = intrinsic.Intrinsic(player_rank,resource_ranks,(0,)*len(resource_ranks))
        self.player,self.ranks,self.q,self.rank = self.core.player,self.core.ranks,self.core.q,self.core.rank
        self.m = len(self.ranks)
        self.nonloops = tuple(p for p in range(self.q) if self.player[1 << p])
        self.values = tuple(tuple(None if v is None else exact(v) for v in row) for row in values)
        self.costs = tuple(tuple(exact(v) for v in row) for row in costs)
        self.setup = tuple(exact(v) for v in setup)
        self.budget,self.epsilon = exact(budget),exact(epsilon)
        if (len(self.values) != self.q or len(self.costs) != self.q or len(self.setup) != self.q
                or any(len(row) != self.m for row in (*self.values,*self.costs))
                or any(v is not None and v < 0 for row in self.values for v in row)
                or any(v < 0 for row in self.costs for v in row)
                or any(v < 0 for v in self.setup) or self.budget < 0
                or not 0 < self.epsilon <= 1):
            raise ValueError('exact nonnegative data, matching original dimensions, and 0<epsilon<=1 required')
        self.delta = self.epsilon/3
        self.count_cap = ceil(1/self.delta)
        self.bin_count = ceil((1-self.delta)/(self.delta*self.delta))
        self.last_stats = {}

    def basis_mask(self,basis):
        mask = intrinsic.mask_of(basis,self.q)
        if mask.bit_count() != self.rank or self.player[mask] != self.rank:
            raise ValueError('actual original player basis required')
        return mask

    def fee(self,basis):
        return sum((self.setup[p] for p in basis),F(0))

    def assignment_cost(self,counts):
        return sum((self.costs[p][j]*counts[j][p] for j in range(self.m) for p in range(self.q)),F(0))

    def verify(self,answer):
        try:
            if type(answer) is not Allocation or type(answer.basis) is not tuple:
                return False
            mask = self.basis_mask(answer.basis)
            if type(answer.counts) is not tuple or len(answer.counts) != self.m:
                return False
            for j,row in enumerate(answer.counts):
                if (type(row) is not tuple or len(row) != self.q
                        or any(type(x) is not int or x < 0 or (x and (not (mask >> p & 1) or self.values[p][j] is None))
                               for p,x in enumerate(row)) or not intrinsic.feasible(self.ranks[j],row)):
                    return False
            return self.fee(answer.basis)+self.assignment_cost(answer.counts) <= self.budget
        except (ValueError,TypeError,AttributeError,IndexError):
            return False

    def minimum(self,answer):
        if not self.verify(answer): raise ValueError('invalid original allocation')
        return min((sum(((self.values[p][j] or 0)*answer.counts[j][p] for j in range(self.m)),F(0))
                    for p in answer.basis),default=None)

    def zero(self):
        selected = 0
        for p in sorted(range(self.q),key=lambda p:(self.setup[p],p)):
            if self.player[selected | (1 << p)] > self.player[selected]: selected |= 1 << p
        basis = intrinsic.members(selected,self.q)
        return None if self.fee(basis) > self.budget else Allocation(basis,tuple((0,)*self.q for _ in self.ranks))

    def grouping(self,basis,target):
        self.basis_mask(basis)
        target = exact(target)
        if target <= 0: raise ValueError('positive target required')
        groups = []
        for p in basis:
            small,bins = [],{}
            for j,original in enumerate(self.values[p]):
                if original is None or original <= 0 or not self.ranks[j][1 << p]: continue
                value = min(original,target)
                if value <= self.delta*target:
                    small.append(j)
                else:
                    index = ceil((value/target-self.delta)/(self.delta*self.delta))-1
                    bins.setdefault(index,[]).append(j)
            occupied = tuple(Bin(i,self.delta+i*self.delta*self.delta,
                                 min(F(1),self.delta+(i+1)*self.delta*self.delta),tuple(bins[i])) for i in sorted(bins))
            groups.append(PlayerGroups(p,tuple(small),occupied))
        return tuple(groups)

    def plans(self,basis,target):
        basis,target = tuple(basis),exact(target)
        groups = self.grouping(basis,target)
        if not groups:
            yield Plan(basis,target,())
            return
        current = []
        def frame(i):
            # Canonical enumerator sum(lambda/2)*h<=1 is exactly PA9.
            return i,iter(profiles.profile_counts(tuple(b.lower/2 for b in groups[i].bins),self.count_cap))
        stack = [frame(0)]
        while stack:
            i,iterator = stack[-1]
            del current[i:]
            try: row = next(iterator)
            except StopIteration:
                stack.pop()
                continue
            current.append(row)
            if i+1 == len(groups): yield Plan(basis,target,tuple(current))
            else: stack.append(frame(i+1))

    def prepare(self,plan):
        if type(plan) is not Plan or type(plan.basis) is not tuple:
            raise ValueError('native plan record required')
        target = exact(plan.target)
        groups = self.grouping(plan.basis,target)
        if self.fee(plan.basis) > self.budget or len(plan.counts) != len(groups):
            raise ValueError('unaffordable basis or mismatched profile')
        allowed = [0]*self.m
        for group,row in zip(groups,plan.counts):
            if (type(row) is not tuple or len(row) != len(group.bins)
                    or any(type(x) is not int or x < 0 for x in row) or sum(row) > self.count_cap
                    or sum((b.lower*h for b,h in zip(group.bins,row)),F(0)) > 2):
                raise ValueError('invalid occupied-bin count profile')
            for j in (*group.small,*(j for b in group.bins for j in b.types)):
                allowed[j] |= 1 << group.owner
        # Mask each resource once, then add one disposal owner with masked total.
        augmented = tuple(tuple(rank[s & allowed[j]] if not s >> self.q & 1 else rank[allowed[j]]
                                for s in range(1 << (self.q+1))) for j,rank in enumerate(self.ranks))
        return groups,augmented

    def fractional(self,plan):
        groups,ranks = self.prepare(plan)
        system = intrinsic.BaseLP(ranks,self.q+1)
        rows = system.rows()
        for group,counts in zip(groups,plan.counts):
            p = group.owner
            for b,h in zip(group.bins,counts):
                rows.append(system.reduce(((j,p,1) for j in b.types),h))
                rows.append(system.reduce(((j,p,-1) for j in b.types),-h))
            upper = sum((b.upper*h for b,h in zip(group.bins,counts)),F(0))
            need = max(F(0),1-upper)*plan.target
            rows.append(system.reduce(((j,p,-self.values[p][j]) for j in group.small),-need))
        rows.append(system.reduce(((j,p,self.costs[p][j]) for j in range(self.m) for p in range(self.q)),
                                  self.budget-self.fee(plan.basis)))
        point = active_vertex(rows,system.dimension,counts=self.last_stats)
        return None if point is None else system.expand(point)

    def recover(self,plan,witness):
        groups,ranks = self.prepare(plan)
        # Supplied witness is verified against the original profile LP, not trusted.
        if (len(witness) != self.m or any(len(row) != self.q+1 for row in witness)
                or any(not intrinsic.feasible(rank,row) or sum(row) != rank[-1] for rank,row in zip(ranks,witness))
                or self.assignment_cost(witness)+self.fee(plan.basis) > self.budget):
            raise ValueError('invalid fractional original resource witness')
        for group,counts in zip(groups,plan.counts):
            p = group.owner
            if any(sum((witness[j][p] for j in b.types),F(0)) != h for b,h in zip(group.bins,counts)):
                raise ValueError('fractional bin equality failed')
            upper = sum((b.upper*h for b,h in zip(group.bins,counts)),F(0))
            if sum((self.values[p][j]*witness[j][p] for j in group.small),F(0)) < max(F(0),1-upper)*plan.target:
                raise ValueError('fractional small utility failed')
        caps = tuple(tuple(rank[1 << p] for p in range(self.q+1)) for rank in ranks)
        duals = tuple(tuple(rank[(len(rank)-1)^s]+sum(caps[j][p] for p in range(self.q+1) if s >> p & 1)-rank[-1]
                            for s in range(len(rank))) for j,rank in enumerate(ranks))
        system = intrinsic.BaseLP(duals,self.q+1)
        rows = system.rows()
        for group in groups:
            p = group.owner
            order = tuple(j for b in reversed(group.bins) for j in b.types)+tuple(sorted(group.small,key=lambda j:(-self.values[p][j],j)))
            for end in range(1,len(order)+1):
                prefix = order[:end]
                bound = ceil(sum((caps[j][p]-witness[j][p] for j in prefix),F(0)))
                rows.append(system.reduce(((j,p,1) for j in prefix),bound))
        # min original cost = max a*y = min -a*y on this integral face.
        objective,_ = system.reduce(((j,p,-self.costs[p][j]) for j in range(self.m) for p in range(self.q)),0)
        point = active_vertex(rows,system.dimension,objective,self.last_stats)
        if point is None: raise RuntimeError('complement-prefix face is empty')
        output = tuple(tuple(F(caps[j][p])-value for p,value in enumerate(row)) for j,row in enumerate(system.expand(point)))
        if any(x.denominator != 1 for row in output for x in row):
            raise RuntimeError('integral complement-prefix vertex was fractional')
        answer = Allocation(plan.basis,tuple(tuple(int(x) for x in row[:self.q]) for row in output))
        if not self.verify(answer) or self.assignment_cost(answer.counts) > self.assignment_cost(witness):
            raise RuntimeError('original cost/resource recovery failed')
        if self.rank and self.minimum(answer) < (1-self.epsilon)*plan.target:
            raise RuntimeError('profile target guarantee failed')
        return answer

    def target(self,target):
        target = exact(target)
        if target < 0: raise ValueError('nonnegative target required')
        zero = self.zero()
        if zero is None or not self.rank or target == 0: return zero
        self.last_stats = {'bases':0,'profiles':0}
        for basis in combinations(self.nonloops,self.rank):
            mask = sum(1 << p for p in basis)
            if self.player[mask] != self.rank or self.fee(basis) > self.budget: continue
            self.last_stats['bases'] += 1
            for plan in self.plans(basis,target):
                self.last_stats['profiles'] += 1
                witness = self.fractional(plan)
                if witness is not None: return self.recover(plan,witness)
        return None

    def optimize(self):
        best = self.zero()
        if best is None or not self.rank: return best
        values = tuple(v for row in self.values for v in row if v is not None and v > 0)
        if not values: return best
        denominator = lcm(*(v.denominator for v in values))
        divisor = gcd(*(int(v*denominator) for v in values))
        quantum = F(divisor,denominator)
        upper_value = sum((rank[-1]*max((self.values[p][j] or F(0) for p in range(self.q)),default=F(0))
                           for j,rank in enumerate(self.ranks)),F(0))
        lower,upper = 0,int(upper_value/quantum)+1
        calls = 0
        while upper-lower > 1:
            middle = (lower+upper)//2
            candidate = self.target(middle*quantum)
            calls += 1
            if candidate is None: upper = middle
            else:
                lower = middle
                if self.minimum(candidate) > self.minimum(best): best = candidate
        self.last_stats['optimization_calls'] = calls
        return best
