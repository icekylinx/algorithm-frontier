"""Complete-table client for two-size corank scheduling.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
The hard path executes guarded batch branching and binary count completion.
The high-target LP/recovery reuses the two-time explicit-table baseline.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import importlib.util
import sys

# Load the canonical sibling implementation without assuming a package name or
# shadowing another module named scheduling in a larger verification process.
_name = '_algorithm_frontier_two_time_scheduling'
if _name not in sys.modules:
    _path = Path(__file__).resolve().parents[2] / 'two-time-scheduling/reference/scheduling.py'
    _spec = importlib.util.spec_from_file_location(_name, _path)
    _module = importlib.util.module_from_spec(_spec)
    sys.modules[_name] = _module
    _spec.loader.exec_module(_module)
_shared = sys.modules[_name]


def subsets(mask):
    current = mask
    while True:
        yield current
        if not current:
            break
        current = (current-1) & mask


def box_rank(rank, cap):
    """Full table of P(rank) intersected with the uniform integral box."""
    if type(cap) is not int or cap < 0:
        raise ValueError('nonnegative integer cap required')
    return tuple(min(rank[a]+cap*(s ^ a).bit_count() for a in subsets(s))
                 for s in range(len(rank)))


def independent(rank, vector):
    return (all(type(v) is int and v >= 0 for v in vector)
            and all(sum(vector[p] for p in range(len(vector)) if s >> p & 1) <= rank[s]
                    for s in range(len(rank))))


def complete_base(rank, lower):
    """Coordinatewise integral augmentation with one binary increment per p."""
    if not independent(rank, lower):
        raise ValueError('lower vector is not independent')
    y = list(lower)
    for p in range(len(y)):
        increment = min(rank[s]-sum(y[v] for v in range(len(y)) if s >> v & 1)
                        for s in range(len(rank)) if s >> p & 1)
        y[p] += increment
    if sum(y) != rank[-1]:
        raise AssertionError('augmentation did not complete a base')
    return tuple(y)


def batch_gap(player_rank, resource_rank, ground, required, full, weak):
    """Actual guarded batch recursion, returning a basis mask and node counts.

    Rank and resource tables always use the full physical-machine bit indices.
    """
    if not (type(full) is int and type(weak) is int and full > weak >= 1):
        raise ValueError('integer full > weak >= 1 required')
    counts = dict(batch_nodes=0, batch_branches=0, rank_rejections=0, guards=0)

    def basis(q):
        chosen = 0
        for p in range(q.bit_length()):
            if q >> p & 1 and player_rank[chosen | (1 << p)] > player_rank[chosen]:
                chosen |= 1 << p
        return chosen

    def visit(q):
        counts['batch_nodes'] += 1
        if player_rank[q] < required:
            counts['rank_rejections'] += 1
            return None
        deficit = q.bit_count()-required
        deficient = min(subsets(q), key=lambda s: (resource_rank[s]-weak*s.bit_count(), s))
        if resource_rank[deficient] >= weak*deficient.bit_count():
            return basis(q)
        amount = deficient.bit_count()-resource_rank[deficient]//full
        if amount > deficit:
            counts['guards'] += 1
            return None
        vertices = [p for p in range(q.bit_length()) if deficient >> p & 1]
        for omitted in combinations(vertices, amount):
            counts['batch_branches'] += 1
            deletion = sum(1 << p for p in omitted)
            result = visit(q ^ deletion)
            if result is not None:
                return result
        return None

    return visit(ground), counts


class CorankBackend:
    """Two original rank tables and positive common times, arbitrary finite q."""

    def __init__(self, small_rank, large_rank, small_size, large_size):
        self.small, self.large = tuple(small_rank), tuple(large_rank)
        length = len(self.small)
        if length == 0 or length & (length-1) or len(self.large) != length:
            raise ValueError('matching complete rank tables required')
        self.q = length.bit_length()-1
        self.u, self.a = _shared.exact(small_size), _shared.exact(large_size)
        if not 0 < self.u < self.a:
            raise ValueError('positive common sizes u < a required')
        if self.q:
            instance = _shared.Instance((self.small, self.large),
                        tuple((self.u, self.a) for _ in range(self.q)),
                        tuple((0, 0) for _ in range(self.q)), 0)
            self.shared = _shared.Backend(instance)
        elif self.small != (0,) or self.large != (0,):
            raise ValueError('empty ground has zero rank')
        self.h, self.s = self.large[-1], self.small[-1]
        self.player = box_rank(self.large, 1)
        self.eligible = sum(1 << p for p in range(self.q) if self.player[1 << p])
        self.corank = self.eligible.bit_count()-self.h if self.player[-1] == self.h else None
        self.last_trace = {}

    def load(self, output):
        return max((self.u*output[2*p]+self.a*output[2*p+1]
                    for p in range(self.q)), default=F(0))

    def target(self, target, d=2):
        target = _shared.exact(target)
        if target < 0 or type(d) is not int or d < 2:
            raise ValueError('nonnegative target and integer d >= 2 required')
        self.last_trace = dict(branch='empty', batch_nodes=0, batch_branches=0,
                               rank_rejections=0, guards=0, full_quota=0,
                               weak_quota=0, corank=self.corank)
        if not self.h:
            self.last_trace['branch'] = 'one-size'
            cap = target//self.u
            rank = box_rank(self.small, cap)
            if rank[-1] != self.s:
                return None
            small = complete_base(rank, (0,)*self.q)
            return tuple(v for count in small for v in (count, 0))
        if target < self.a:
            self.last_trace['branch'] = 'below-large'
            return None
        if target >= F(d, d-1)*self.a:
            self.last_trace['branch'] = 'shared-high-target'
            return self.shared.target(target, d)
        if self.player[-1] < self.h:
            self.last_trace['branch'] = 'boolean-rank-failure'
            return None
        cap = target//self.u
        boxed = box_rank(self.small, cap)
        if boxed[-1] != self.s:
            self.last_trace['branch'] = 'small-rank-failure'
            return None
        full_ground = len(self.small)-1
        dual = tuple(cap*s.bit_count()+boxed[full_ground ^ s]-self.s
                     for s in range(len(self.small)))
        full = cap-(target-self.a)//self.u
        weak = -(-full//d)
        self.last_trace.update(full_quota=full, weak_quota=weak)
        if full <= d:
            self.last_trace['branch'] = 'one-unit'
            chosen = None
            for candidate in subsets(self.eligible):
                if candidate.bit_count() != self.h or self.player[candidate] != self.h:
                    continue
                vector = tuple(int(candidate >> p & 1) for p in range(self.q))
                if independent(dual, vector):
                    chosen = candidate
                    break
        else:
            self.last_trace['branch'] = 'batch'
            chosen, counts = batch_gap(self.player, dual, self.eligible, self.h, full, weak)
            self.last_trace.update(counts)
        if chosen is None:
            return None
        lower = tuple(weak*int(chosen >> p & 1) for p in range(self.q))
        y = complete_base(dual, lower)
        output = tuple(v for p in range(self.q) for v in (cap-y[p], int(chosen >> p & 1)))
        if self.load(output) > F(2*d-1, d)*target:
            raise AssertionError('target load bound failed')
        return output

    def optimize(self, d=2):
        if type(d) is not int or d < 2:
            raise ValueError('integer d >= 2 required')
        small = complete_base(self.small, (0,)*self.q)
        large = complete_base(self.large, (0,)*self.q)
        saved = tuple(v for p in range(self.q) for v in (small[p], large[p]))
        if not self.h and not self.s:
            return saved
        denominator = lcm(self.u.denominator, self.a.denominator)
        grid = F(gcd(int(self.u*denominator), int(self.a*denominator)), denominator)
        low, high = 0, int(self.load(saved)/grid)
        while high-low > 1:
            mid = (high+low)//2
            output = self.target(mid*grid, d)
            if output is None:
                low = mid
            else:
                high, saved = mid, output
        return saved
