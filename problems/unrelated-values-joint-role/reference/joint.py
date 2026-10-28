"""Exact original-input shared-role reference (finite LP basis enumeration).

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
The actual prefix recursion is canonical; local LP enumeration is not the
polynomial oracle implementation charged in the asymptotic theorem.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from math import lcm
from pathlib import Path
import importlib.util
import sys


def load(name,path):
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name,Path(__file__).resolve().parents[2]/path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


core = load('_joint_weighted','robust-bounded-certificates/reference/bounded.py')
prefix = load('_joint_prefix','whole-ground-allocation/reference/selection.py')
linear = load('_joint_linear','two-time-scheduling/reference/scheduling.py')


def members(mask,q):
    return tuple(p for p in range(q) if mask >> p & 1)


def mask(players,q):
    players = tuple(players)
    if any(type(p) is not int or not 0 <= p < q for p in players) or len(set(players)) != len(players):
        raise ValueError('distinct original owner IDs required')
    return sum(1 << p for p in players)


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))


def vertices(rows,dimension):
    """Stream all active bases, without storing the vertex set or unit supply."""
    rows = tuple(sorted(set((tuple(map(F,a)),F(b)) for a,b in rows)))
    if dimension == 0:
        if all(b >= 0 for _,b in rows): yield ()
        return
    for active in combinations(rows,dimension):
        point = linear.solve_square(active)
        if point is not None and all(dot(a,point) <= b for a,b in rows):
            yield point


def optimize(rows,objective):
    best = None
    for point in vertices(rows,len(objective)):
        value = dot(objective,point)
        if best is None or value > best[0]: best = value,point
    return best


def greedy(player,allowed,costs):
    selected = 0
    for p in sorted(allowed,key=lambda p:(costs[p],p)):
        if player[selected | (1 << p)] > player[selected]: selected |= 1 << p
    return members(selected,len(player).bit_length()-1)


def admissible(base,ratio):
    base,ratio = core.rational(base),core.rational(ratio)
    if base > 1 and ratio > 1 and base >= 3*ratio:
        return base  # Uniform binary-accuracy envelope, with no huge powers.
    a,b = ratio.numerator,ratio.denominator
    if base <= 1 or ratio <= 1 or base**b < F(a**a,b**b*(a-b)**(a-b)):
        raise ValueError('cover base must dominate Gamma(full/(full-weak))')
    return base


@dataclass(frozen=True)
class Allocation:
    basis: tuple
    counts: tuple


@dataclass(frozen=True)
class RoleWitness:
    allowed: tuple
    counts: tuple  # real resources followed by the persistent dummy


class Region:
    """One original-resource product with masks, affine cost and count rows."""
    def __init__(self,q,ranks,values,costs,budget,allowed=None,forced_one=()):
        self.q,self.ranks = q,tuple(ranks)
        self.values,self.costs = tuple(values),tuple(costs)
        self.keys = tuple((j,p) for j,row in enumerate(ranks) for p in range(q)
                          if row[1 << p] > 0 and (allowed is None or (j,p) in allowed))
        self.dimension = len(self.keys)
        self.rows = []
        for i in range(self.dimension):
            row = [F(0)]*self.dimension
            row[i] = -1
            self.rows.append((tuple(row),F(0)))
        for j,rank in enumerate(ranks):
            for s,bound in enumerate(rank):
                self.rows.append((tuple(F(h == j and bool(s >> p & 1)) for h,p in self.keys),F(bound)))
        self.cost = tuple(costs[j][p] for j,p in self.keys)
        self.rows.append((self.cost,F(budget)))
        for p in forced_one:
            row = tuple(F(owner == p) for _,owner in self.keys)
            self.rows.extend(((row,F(1)),(tuple(-a for a in row),F(-1))))

    def expand(self,point):
        result = [[F(0)]*self.q for _ in self.ranks]
        for (j,p),x in zip(self.keys,point): result[j][p] = x
        return tuple(tuple(row) for row in result)

    def service_row(self,p):
        return tuple(self.values[j][p] if owner == p else F(0) for j,owner in self.keys)

    def feasible(self,service=()):
        rows = self.rows+[(tuple(-x for x in self.service_row(p)),-F(t)) for p,t in service]
        point = next(vertices(rows,self.dimension),None)
        return None if point is None else self.expand(point)

    def optimum(self,players):
        players = tuple(players)
        if not players: raise ValueError('nonempty utility ground required')
        rows = [(a+(F(0),),b) for a,b in self.rows]
        rows.append(((F(0),)*self.dimension+(F(-1),),F(0)))
        for p in players: rows.append((tuple(-x for x in self.service_row(p))+(F(1),),F(0)))
        answer = optimize(rows,(F(0),)*self.dimension+(F(1),))
        return None if answer is None else (answer[0],self.expand(answer[1][:-1]))

    def separate(self,players,rates):
        """Normalized nonnegative outer support LP; empty region is a gate."""
        players = tuple(sorted(players))
        witness = self.feasible((p,rates[p]) for p in players)
        if witness is not None: return None,witness
        samples = tuple(sorted({tuple(dot(self.service_row(p),point) for p in players)
                                for point in vertices(self.rows,self.dimension)}))
        if not samples: raise ValueError('empty region must be rejected before separation')
        # Eliminate the last normal coordinate: a_last=1-sum(a_i).
        k = len(players)
        if not k: raise ValueError('nonempty service ground required')
        rows = []
        for i in range(k-1):
            row = [F(0)]*k
            row[i] = -1
            rows.append((tuple(row),F(0)))
        rows.append(((F(1),)*(k-1)+(F(0),),F(1)))
        rows.append(((F(0),)*(k-1)+(F(-1),),F(0)))
        for service in samples:
            rows.append((tuple(x-service[-1] for x in service[:-1])+(F(-1),),-service[-1]))
        objective = tuple(rates[p]-rates[players[-1]] for p in players[:-1])+(F(-1),)
        answer = optimize(rows,objective)
        if answer is None: raise RuntimeError('support LP has no vertex')
        point = answer[1]
        normal = point[:-1]+(1-sum(point[:-1],F(0)),)
        coefficients = tuple(normal[players.index(p)] if p in players else F(0) for p in range(self.q))
        capacity = max(dot(normal,service) for service in samples)
        if dot(coefficients,rates) <= capacity: raise RuntimeError('missing strict support separator')
        return prefix.Row(coefficients,capacity),None


def round_counts(q,ranks,values,costs,fractional,allowed=None):
    """Signed-cost disposal/complement-prefix rounding, without unit expansion.

    Eliminating each disposal coordinate and complementing back leaves the
    original rank inequalities and lower floors for every owner value prefix.
    Remove the budget row: optimize its signed objective over the integral face.
    """
    region = Region(q,ranks,values,costs,0,allowed)
    rows = region.rows[:-1]
    for p in range(q):
        order = sorted(range(len(ranks)),key=lambda j:(-values[j][p],j))
        chosen = set()
        for j in order:
            chosen.add(j)
            total = sum((fractional[h][p] for h in chosen),F(0))
            floor = total.numerator//total.denominator
            rows.append((tuple(F(-1 if h in chosen and owner == p else 0) for h,owner in region.keys),F(-floor)))
    answer = optimize(rows,tuple(-c for c in region.cost))
    if answer is None: raise RuntimeError('empty prefix recovery')
    output = region.expand(answer[1])
    if any(x.denominator != 1 for row in output for x in row):
        raise RuntimeError('integral prefix face produced fractional vertex')
    before = sum((costs[j][p]*fractional[j][p] for j in range(len(ranks)) for p in range(q)),F(0))
    if -answer[0] > before: raise RuntimeError('signed rounding cost increased')
    return tuple(tuple(int(x) for x in row) for row in output)


class Joint:
    def __init__(self,player_rank,resource_ranks,values,costs,budget,setup=None):
        self.player = tuple(player_rank)
        length = len(self.player)
        if not length or length & (length-1): raise ValueError('complete player rank table required')
        self.q = length.bit_length()-1
        self.ranks = tuple(tuple(row) for row in resource_ranks)
        self.values = tuple(tuple(core.rational(x) for x in row) for row in values)
        self.costs = tuple(tuple(core.rational(x) for x in row) for row in costs)
        self.budget = core.rational(budget)
        self.setup = (F(0),)*self.q if setup is None else tuple(core.rational(x) for x in setup)
        if (len(self.values) != len(self.ranks) or len(self.costs) != len(self.ranks)
                or any(len(row) != self.q for row in self.values+self.costs) or len(self.setup) != self.q
                or any(x < 0 for row in self.values+self.costs for x in row)
                or any(x < 0 for x in self.setup) or self.budget < 0):
            raise ValueError('nonnegative original values, costs, setup and budget required')
        core.table_scenario((self.player,)+self.ranks,
                            tuple((0,)*(len(self.ranks)+1) for _ in range(self.q)),0)
        if any(value > s.bit_count() for s,value in enumerate(self.player)):
            raise ValueError('player rank must be a matroid rank')
        self.rank = self.player[-1]
        full = length-1
        self.dual = tuple(s.bit_count()+self.player[full ^ s]-self.rank for s in range(length))
        self.last_trace = {}

    def verify(self,allocation):
        try:
            if type(allocation) is not Allocation or type(allocation.basis) is not tuple: return False
            selected = mask(allocation.basis,self.q)
            if selected.bit_count() != self.rank or self.player[selected] != self.rank: return False
            if type(allocation.counts) is not tuple or len(allocation.counts) != len(self.ranks): return False
            cost = sum((self.setup[p] for p in allocation.basis),F(0))
            for j,(rank,row) in enumerate(zip(self.ranks,allocation.counts)):
                if (type(row) is not tuple or len(row) != self.q
                        or any(type(x) is not int or x < 0 or (not selected >> p & 1 and x != 0) for p,x in enumerate(row))):
                    return False
                if any(sum(row[p] for p in members(s,self.q)) > bound for s,bound in enumerate(rank)): return False
                cost += sum((self.costs[j][p]*row[p] for p in range(self.q)),F(0))
            return cost <= self.budget
        except (ValueError,TypeError,AttributeError,IndexError): return False

    def minimum(self,allocation):
        if not self.verify(allocation): raise ValueError('invalid original allocation')
        return min((sum((self.values[j][p]*allocation.counts[j][p] for j in range(len(self.ranks))),F(0))
                    for p in allocation.basis),default=None)

    def zero(self):
        basis = greedy(self.player,range(self.q),self.setup)
        answer = Allocation(basis,tuple((0,)*self.q for _ in self.ranks))
        return answer if self.verify(answer) else None

    def masks(self):
        values = sorted({self.values[j][p] for j in range(len(self.ranks)) for p in range(self.q)
                         if self.values[j][p] > 0 and self.ranks[j][1 << p] > 0})
        return tuple(values+([values[-1]+1] if values else []))

    def role_region(self,theta,allowed):
        theta = core.rational(theta)
        if theta <= 0: raise ValueError('positive threshold required')
        allowed = frozenset(allowed)
        real = {(j,p) for j,rank in enumerate(self.ranks) for p in range(self.q)
                if self.values[j][p] > 0 and ((p in allowed and self.values[j][p] < theta)
                                            or (p not in allowed and self.values[j][p] >= theta))}
        dummy = len(self.ranks)
        pairs = real | {(dummy,p) for p in range(self.q)}
        return Region(self.q,self.ranks+(self.dual,),self.values+((F(0),)*self.q,),
                      self.costs+(tuple(-s for s in self.setup),),self.budget-sum(self.setup,F(0)),
                      pairs,tuple(p for p in range(self.q) if p not in allowed))

    def recover(self,theta,witness):
        region = self.role_region(theta,witness.allowed)
        rounded = round_counts(self.q,region.ranks,region.values,region.costs,witness.counts,set(region.keys))
        dummy = rounded[-1]
        basis = greedy(self.player,(p for p in range(self.q) if not dummy[p]),self.setup)
        answer = Allocation(basis,tuple(tuple(row[p] if p in basis else 0 for p in range(self.q)) for row in rounded[:-1]))
        if not self.verify(answer): raise RuntimeError('original setup/assignment recovery failed')
        return answer

    def gap(self,theta,k,full,weak,forced=(),global_base=None,count_service=False):
        if not 0 <= k < self.q: raise ValueError('nonempty promised light set required')
        full,weak = core.rational(full),core.rational(weak)
        if not full > weak > 0: raise ValueError('positive full and weaker targets required')
        if global_base is not None: global_base = admissible(global_base,full/(full-weak))
        if global_base is not None and tuple(forced): raise ValueError('global cover owns its forced seed')
        def extension(seed):
            def prepare(allowed):
                region = self.role_region(theta,allowed)
                if count_service:
                    region.values = tuple(tuple(F(value > 0) for value in row) for row in self.values)+((F(0),)*self.q,)
                counts = region.feasible()
                if counts is None: return None
                return prefix.Choice(tuple(sorted(allowed))[:self.q-k],dict(region=region,allowed=tuple(sorted(allowed)),counts=counts))
            def separate(allowed,choice,rates):
                row,counts = choice.context['region'].separate(allowed,rates)
                if row is None: choice.context['counts'] = counts
                return row
            counts = {}
            result = prefix.gap(self.q,self.q-k,full,weak,prepare,separate,seed,counts=counts)
            for name,value in counts.items(): self.last_trace[name] = self.last_trace.get(name,0)+value
            if result is None: return None
            state = result.choice.context
            return RoleWitness(state['allowed'],state['counts'])
        return (extension(tuple(forced)) if global_base is None else
                prefix.whole_ground(self.q,self.q-k,global_base,extension))

    def pure(self,theta):
        region = self.role_region(theta,())
        # Full per-owner total exactly one makes this joint intersection integral.
        answer = optimize(region.rows[:-2*self.q-1]+region.rows[-2*self.q:],tuple(-c for c in region.cost))
        if answer is None or -answer[0] > self.budget-sum(self.setup,F(0)): return None
        counts = region.expand(answer[1])
        if any(x.denominator != 1 for row in counts for x in row): raise RuntimeError('fractional all-heavy vertex')
        return self.recover(theta,RoleWitness((),counts))

    def exact_two(self):
        best = self.zero()
        if best is None or not self.rank: return best
        for theta in self.masks():
            candidate = self.pure(theta)
            if candidate is not None and self.minimum(candidate) > self.minimum(best): best = candidate
            for s in range(1,1 << self.q):
                allowed = members(s,self.q)
                result = self.role_region(theta,allowed).optimum(allowed)
                if result is None: continue
                candidate = self.recover(theta,RoleWitness(allowed,result[1]))
                if self.minimum(candidate) > self.minimum(best): best = candidate
        return best

    def near(self,epsilon,heavy_budget=None,global_base=None):
        epsilon = core.rational(epsilon)
        if not 0 < epsilon < 1: raise ValueError('accuracy must lie strictly between zero and one')
        if global_base is not None: global_base = admissible(global_base,1/epsilon)
        if heavy_budget is None: heavy_budget = self.q
        if type(heavy_budget) is not int or heavy_budget < 0: raise ValueError('nonnegative omitted-role budget required')
        best = self.zero()
        if best is None or not self.rank: return best
        self.last_trace = {}
        quantum = F(1,lcm(*(x.denominator for row in self.values for x in row)))
        upper = sum((max(row,default=F(0))*rank[-1] for row,rank in zip(self.values,self.ranks)),F(0))
        for theta in self.masks():
            if heavy_budget >= self.q:
                candidate = self.pure(theta)
                if candidate is not None and self.minimum(candidate) > self.minimum(best): best = candidate
            for k in range(min(heavy_budget,self.q-1)+1):
                low,high = 0,int(upper/quantum)+1
                saved = None
                while high-low > 1:
                    mid = (low+high)//2
                    witness = self.gap(theta,k,mid*quantum,(1-epsilon)*mid*quantum,global_base=global_base)
                    if witness is None: high = mid
                    else: low,saved = mid,witness
                if saved is not None:
                    candidate = self.recover(theta,saved)
                    if self.minimum(candidate) > self.minimum(best): best = candidate
        return best

    def quota_target(self,target,factor=2,global_base=None):
        """Compulsory {0,u,a} full-target gap, including exact boundary gates."""
        target = core.rational(target)
        if (target <= 0 or type(factor) is not int or factor < 2 or self.rank != self.q
                or any(self.setup)):
            raise ValueError('positive target, integer factor, compulsory players and zero setup required')
        positive = sorted({value for row in self.values for value in row if value > 0})
        if len(positive) > 2: raise ValueError('at most two positive pair values required')
        if not positive: return None
        u,a = positive[0],positive[-1]
        pairs = {(j,p) for j in range(len(self.ranks)) for p in range(self.q) if self.values[j][p] > 0}
        original = Region(self.q,self.ranks,self.values,self.costs,self.budget,pairs)
        if target >= F(factor, factor-1)*a:
            counts = original.feasible((p,target) for p in range(self.q))
            if counts is None: return None
            rounded = round_counts(self.q,self.ranks,self.values,self.costs,counts,pairs)
            answer = Allocation(tuple(range(self.q)),rounded)
            if not self.verify(answer): raise RuntimeError('high-target recovery failed')
            return answer
        quantity = target/u
        quota = -(-quantity.numerator//quantity.denominator)
        def exact_quotas(region,quotas):
            # Remove the cost cap before integer optimization; all owner quotas
            # are integral and form a full-total partition face.
            rows = region.rows[:len(region.keys)+sum(len(rank) for rank in region.ranks)]
            for p,bound in enumerate(quotas):
                row = tuple(F(owner == p) for _,owner in region.keys)
                rows.extend(((row,F(bound)),(tuple(-x for x in row),F(-bound))))
            result = optimize(rows,tuple(-c for c in region.cost))
            if result is None or -result[0] > self.budget: return None
            counts = region.expand(result[1])[:len(self.ranks)]
            if any(x.denominator != 1 for row in counts for x in row): raise RuntimeError('fractional quota face')
            answer = Allocation(tuple(range(self.q)),tuple(tuple(int(x) for x in row) for row in counts))
            if not self.verify(answer): raise RuntimeError('quota recovery violated original input')
            return answer
        if quota <= factor: return exact_quotas(original,(1,)*self.q)
        weak = -(-quota//factor)
        for k in range(self.q+1):
            if k == self.q:
                answer = self.pure(a)
            else:
                witness = self.gap(a,k,quota,weak,global_base=global_base,count_service=True)
                if witness is None: continue
                answer = exact_quotas(self.role_region(a,witness.allowed),
                                      tuple(weak if p in witness.allowed else 1 for p in range(self.q)))
            if answer is not None: return answer
        return None
