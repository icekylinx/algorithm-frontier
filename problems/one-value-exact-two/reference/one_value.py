"""Binary-capacity exact-budget one-value allocation reference.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro. Apache-2.0.
The omission/cover and weighted intersection algorithms are canonical.
The exact Bland-simplex LP backend has a separate finite basis bound;
it is not the polynomial-time LP primitive charged by the theorem.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import importlib.util
import sys


def load(name, path):
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(
            name, Path(__file__).resolve().parents[2] / path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


lp = load('_one_value_lp', 'selected-flow/reference/concurrent.py')
weighted = load('_one_value_weighted', 'robust-bounded-certificates/reference/bounded.py')
prefix = load('_one_value_prefix', 'whole-ground-allocation/reference/selection.py')
counts = load('_one_value_counts', 'recipient-polymatroid/reference/counts.py')


def mask(players, q):
    players = tuple(players)
    if any(type(p) is not int or not 0 <= p < q for p in players) or len(set(players)) != len(players):
        raise ValueError('distinct original player IDs required')
    return sum(1 << p for p in players)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


@dataclass(frozen=True)
class Allocation:
    basis: tuple
    counts: tuple  # original type-major integer vectors, zero outside basis


class OneValue:
    def __init__(self, player_rank, resource_ranks, costs, budget, setup=None, value=1):
        self.player = tuple(player_rank)
        if not self.player or len(self.player) & (len(self.player)-1):
            raise ValueError('complete original player rank table required')
        self.q = len(self.player).bit_length()-1
        self.player = counts.RankTable(self.q, self.player).values
        if any(v > s.bit_count() for s, v in enumerate(self.player)):
            raise ValueError('player rank must be an ordinary matroid rank')
        self.ranks = tuple(counts.RankTable(self.q, tuple(row)).values for row in resource_ranks)
        if any(len(row) != len(self.player) for row in self.ranks):
            raise ValueError('ranks must use the same original player ground')
        self.costs = tuple(tuple(lp.rational(x) for x in row) for row in costs)
        self.setup = (F(0),)*self.q if setup is None else tuple(lp.rational(x) for x in setup)
        self.budget, self.value = lp.rational(budget), lp.rational(value)
        if (len(self.costs) != len(self.ranks) or any(len(row) != self.q for row in self.costs)
                or len(self.setup) != self.q or self.budget < 0 or self.value <= 0
                or any(x < 0 for row in self.costs for x in row) or any(x < 0 for x in self.setup)):
            raise ValueError('nonnegative original costs/setup/budget and positive common value required')
        self.rank = self.player[-1]
        self.nonloops = tuple(p for p in range(self.q) if self.player[1 << p])
        active = mask(self.nonloops, self.q)
        self.upper = sum(row[active] for row in self.ranks)//self.rank if self.rank else 0
        self.last_trace = {}

    def _basis(self, basis):
        basis = tuple(basis)
        s = mask(basis, self.q)
        if len(basis) != self.rank or self.player[s] != self.rank:
            raise ValueError('an actual original player basis is required')
        return basis

    def _greedy(self, allowed):
        selected = 0
        for p in sorted(allowed, key=lambda p: (self.setup[p], p)):
            if self.player[selected | (1 << p)] > self.player[selected]:
                selected |= 1 << p
        return tuple(p for p in range(self.q) if selected >> p & 1)

    def cost(self, allocation):
        return (sum((self.setup[p] for p in allocation.basis), F(0))
                + sum((c*x for row, charge in zip(allocation.counts, self.costs)
                       for x, c in zip(row, charge)), F(0)))

    def verify(self, allocation):
        try:
            if type(allocation) is not Allocation or type(allocation.basis) is not tuple:
                return False
            basis = self._basis(allocation.basis)
            if type(allocation.counts) is not tuple or len(allocation.counts) != len(self.ranks):
                return False
            for row, rank in zip(allocation.counts, self.ranks):
                if (type(row) is not tuple or len(row) != self.q
                        or any(type(x) is not int or x < 0 or (p not in basis and x != 0)
                               for p, x in enumerate(row))
                        or any(sum(row[p] for p in range(self.q) if s >> p & 1) > cap
                               for s, cap in enumerate(rank))):
                    return False
            return self.cost(allocation) <= self.budget
        except (ValueError, TypeError, AttributeError, IndexError):
            return False

    def minimum(self, allocation):
        if not self.verify(allocation):
            raise ValueError('invalid original allocation')
        return min((self.value*sum(row[p] for row in allocation.counts)
                    for p in allocation.basis), default=None)

    def zero(self, allowed=None):
        allowed = self.nonloops if allowed is None else tuple(allowed)
        mask(allowed, self.q)
        basis = self._greedy(allowed)
        if len(basis) != self.rank:
            return None
        answer = Allocation(basis, tuple((0,)*self.q for _ in self.ranks))
        return answer if self.verify(answer) else None

    def _rows(self, allowed):
        """Original independent resource vectors, masked only by free disposal."""
        keys = tuple((j, p) for j, rank in enumerate(self.ranks) for p in range(self.q)
                     if p in allowed and rank[1 << p] > 0)
        a, b = [], []
        for j, rank in enumerate(self.ranks):
            for s, cap in enumerate(rank):
                a.append(tuple(F(h == j and bool(s >> p & 1)) for h, p in keys))
                b.append(F(cap))
        return keys, a, b

    def _expand(self, keys, point, integral=False):
        result = [[0 if integral else F(0) for _ in range(self.q)] for _ in self.ranks]
        for (j, p), x in zip(keys, point):
            if integral and x.denominator != 1:
                raise RuntimeError('integral intersection returned a fractional vertex')
            result[j][p] = int(x) if integral else x
        return tuple(tuple(row) for row in result)

    def service(self, rates, residual):
        """Original count-region membership or a strict nonnegative packing row.

        residual is a nonnegative remaining assignment budget, already paired
        with an attaining setup basis by the caller. Returns (row, counts).
        """
        rates = tuple(lp.rational(x) for x in rates)
        residual = lp.rational(residual)
        if len(rates) != self.q or any(x < 0 for x in rates) or residual < 0:
            raise ValueError('nonnegative original rates and residual budget required')
        keys, a, b = self._rows(set(range(self.q)))
        resource_rows = len(b)
        a.append(tuple(self.costs[j][p] for j, p in keys)); b.append(residual)
        for p in range(self.q):
            a.append(tuple(F(owner == p) for _, owner in keys)); b.append(rates[p])
        objective = (F(1),)*len(keys)
        x, y = lp.simplex(a, b, objective)
        if not lp.verify_lp(a, b, objective, x, y):
            raise RuntimeError('invalid capped-service primal/dual certificate')
        if sum(x, F(0)) == sum(rates, F(0)):
            return None, self._expand(keys, x)
        # Dual service-cap prices may exceed one; positive-part clipping
        # increases the strict violation while preserving all resource bounds.
        normal = tuple(max(F(0), 1-t) for t in y[resource_rows+1:])
        capacity = dot(b[:resource_rows+1], y[:resource_rows+1])
        row = prefix.Row(normal, capacity)
        if dot(normal, rates) <= capacity:
            raise RuntimeError('capped-service dual failed to separate')
        return row, None

    def _recover(self, basis, quota):
        """Exact minimum assignment cost at a fixed integer quota, sans budget row."""
        basis = self._basis(basis)
        if type(quota) is not int or quota < 0:
            raise ValueError('nonnegative binary integer quota required')
        keys, a, b = self._rows(set(basis))
        for p in basis:
            a.append(tuple(F(owner == p) for _, owner in keys)); b.append(F(quota))
        charges = tuple(self.costs[j][p] for j, p in keys)
        total = quota*self.rank
        dominant = total*max(charges, default=F(0))+1
        objective = tuple(dominant-c for c in charges)
        x, y = lp.simplex(a, b, objective)
        if not lp.verify_lp(a, b, objective, x, y):
            raise RuntimeError('invalid integral-recovery LP certificate')
        output = self._expand(keys, x, integral=True)
        if sum(x, F(0)) != total:
            return None
        return Allocation(basis, output)

    def fixed_quota(self, basis, quota):
        """Exact shared-budget feasibility on a prescribed ORIGINAL basis."""
        answer = self._recover(basis, quota)
        return answer if answer is not None and self.verify(answer) else None

    def optimize_fixed(self, basis):
        """Exact integer optimum on a prescribed basis, with fixed setup paid."""
        basis = self._basis(basis)
        saved = self.fixed_quota(basis, 0)
        if saved is None or not self.rank:
            return saved
        low, high = 0, self.upper+1
        while high-low > 1:
            mid = (low+high)//2
            answer = self.fixed_quota(basis, mid)
            if answer is None: high = mid
            else: low, saved = mid, answer
        return saved

    def unit(self, allowed=None):
        """Actual weighted pair-matroid intersection; setup charged once per owner."""
        allowed = self.nonloops if allowed is None else tuple(allowed)
        mask(allowed, self.q)
        pairs = tuple((p, j) for p in allowed for j, rank in enumerate(self.ranks) if rank[1 << p])
        def first(chosen):
            owners = tuple(pairs[i][0] for i in chosen)
            return len(set(owners)) == len(owners) and self.player[mask(owners, self.q)] == len(owners)
        def second(chosen):
            return all(all(sum(1 for i in chosen if pairs[i][1] == j and s >> pairs[i][0] & 1) <= cap
                           for s, cap in enumerate(rank)) for j, rank in enumerate(self.ranks))
        charges = tuple(self.setup[p]+self.costs[j][p] for p, j in pairs)
        certificate = weighted.minimum_cost(first, second, charges, self.rank)
        if not weighted.verify_intersection(first, second, charges, self.rank, certificate):
            raise RuntimeError('invalid one-unit intersection certificate')
        if len(certificate.chosen) != self.rank:
            return None
        row = [[0]*self.q for _ in self.ranks]
        for i in certificate.chosen:
            p, j = pairs[i]; row[j][p] = 1
        answer = Allocation(tuple(sorted(pairs[i][0] for i in certificate.chosen)), tuple(tuple(x) for x in row))
        return answer if self.verify(answer) else None

    def _cover_base(self, d, supplied):
        # Sharp rational endpoints; a uniform binary-safe envelope otherwise.
        minimum = F(27, 4) if d == 2 else F(4) if d == 3 else 3*F(d+1, d-1)
        result = minimum if supplied is None else lp.rational(supplied)
        if result < minimum:
            raise ValueError('cover base below the supported certified envelope')
        return result

    def target(self, full, d=2, forced=(), whole_ground=False, cover_base=None, observe=None):
        """Weak ceil(full/d) output or sound exclusion of the original full target.

        forced contains original player IDs, and changes only selection options.
        An observer receives (original allowed IDs, basis, residual budget, row).
        """
        if type(full) is not int or full < 0 or type(d) is not int or d < 2 or type(whole_ground) is not bool:
            raise ValueError('nonnegative integer full target and integer d>=2 required')
        forced = tuple(forced); mask(forced, self.q)
        if whole_ground and forced:
            raise ValueError('the whole-ground cover owns its forced seed')
        if cover_base is not None and not whole_ground:
            raise ValueError('cover base requires whole-ground mode')
        base = self._cover_base(d, cover_base) if whole_ground else None
        self.last_trace = dict(nodes=0, selector_rejections=0, zero_deficit_rejections=0,
                               prefix_states=0, certificates=0, seeds=0, gate=0)
        allowed = tuple(p for p in self.nonloops if p not in forced)
        initial = self.zero(allowed)
        if initial is None or not self.rank or full == 0:
            return initial
        if full <= d:
            self.last_trace['gate'] = 1
            return self.unit(allowed)
        weak = (full+d-1)//d
        local = {p: i for i, p in enumerate(self.nonloops)}
        seed = tuple(local[p] for p in forced if p in local)
        def extension(omitted):
            def prepare(ground):
                players = tuple(self.nonloops[i] for i in sorted(ground))
                zero = self.zero(players)
                if zero is None: return None
                paid = self.cost(zero)
                return prefix.Choice(tuple(local[p] for p in zero.basis),
                                     dict(basis=zero.basis, residual=self.budget-paid))
            def separate(ground, choice, rates):
                original = tuple(rates[local[p]] if p in local else F(0) for p in range(self.q))
                row, witness = self.service(original, choice.context['residual'])
                choice.context['witness'] = witness
                if observe is not None:
                    observe(tuple(self.nonloops[i] for i in sorted(ground)), choice.context['basis'],
                            choice.context['residual'], row)
                return None if row is None else prefix.Row(tuple(row.coefficients[p] for p in self.nonloops), row.capacity)
            accounting = {}
            result = prefix.gap(len(self.nonloops), self.rank, full, weak, prepare, separate,
                                omitted, counts=accounting)
            for key, value in accounting.items():
                self.last_trace[key] = self.last_trace.get(key, 0)+value
            if result is None: return None
            answer = self.fixed_quota(result.choice.context['basis'], weak)
            if answer is None:
                raise RuntimeError('no-loss exact-budget quota recovery failed')
            return answer
        return (prefix.whole_ground(len(self.nonloops), self.rank, base, extension, self.last_trace)
                if whole_ground else extension(seed))

    def optimize(self, d=2, whole_ground=False, cover_base=None):
        # Validate parameters even when the instance has rank zero or zero supply.
        saved = self.target(0, d, whole_ground=whole_ground, cover_base=cover_base)
        if saved is None or not self.rank:
            return saved
        low, high = 0, self.upper+1
        while high-low > 1:
            mid = (low+high)//2
            answer = self.target(mid, d, whole_ground=whole_ground, cover_base=cover_base)
            if answer is None: high = mid
            else: low, saved = mid, answer
        return saved
