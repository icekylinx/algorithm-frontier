"""Exact one-order mixed prefix quotas with signed scalar optimization.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
Binary original totals are retained. Occupied profiles are streamed through
the canonical iterative count/mass iterator; exact Bland LP time is separate
from the theorem's paid polynomial integral-intersection primitive.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import importlib.util
import sys


def load(name, path):
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, Path(__file__).resolve().parents[2]/path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


rank_module = load('_quota_rank', 'recipient-polymatroid/reference/counts.py')
linear = load('_quota_linear', 'selected-flow/reference/concurrent.py')
occupied = load('_quota_occupied', 'arbitrary-processing-scheduling/reference/profiles.py')


@dataclass(frozen=True)
class Solution:
    counts: tuple
    cost: F


class Prefix:
    """Coordinates are in the supplied rank table's order, numbered from zero.

    Each row is (prefix_length, '<=' or '=' or '>=', nonnegative target).
    The objective is minimized unless maximize=True. There is one resource
    polymatroid and one scalar; mandatory=True retains its ORIGINAL total.
    """
    def __init__(self, rank, weights, costs, rows=(), mandatory=True, allowed=None, maximize=False):
        rank = tuple(rank)
        if not rank or len(rank) & (len(rank)-1):
            raise ValueError('complete original rank table required')
        self.n = len(rank).bit_length()-1
        self.rank = rank_module.RankTable(self.n, rank).values
        self.weights = tuple(weights)
        self.costs = tuple(linear.rational(x) for x in costs)
        if (len(self.weights) != self.n or len(self.costs) != self.n
                or any(type(w) is not int or w < 0 for w in self.weights)
                or type(mandatory) is not bool or type(maximize) is not bool):
            raise ValueError('common nonnegative integer weights, exact scalar and Boolean mode required')
        self.mandatory, self.maximize = mandatory, maximize
        self.rows = tuple(tuple(row) for row in rows)
        if any(len(row) != 3 or type(row[0]) is not int or not 0 <= row[0] <= self.n
               or row[1] not in ('<=', '=', '>=') or type(row[2]) is not int or row[2] < 0
               for row in self.rows):
            raise ValueError('valid original prefix length, relation and integer target required')
        allowed = tuple(range(self.n)) if allowed is None else tuple(allowed)
        if (any(type(e) is not int or not 0 <= e < self.n for e in allowed)
                or len(set(allowed)) != len(allowed)):
            raise ValueError('distinct original eligible coordinate IDs required')
        self.allowed = frozenset(allowed)
        self.total = self.rank[-1]
        self.bound = max((b for _, _, b in self.rows), default=0)
        self.last_trace = {}
        self._prepare()

    def _prepare(self):
        upper, lower = {}, {}
        for endpoint, relation, target in self.rows:
            if relation in ('<=', '='): upper[endpoint] = min(upper.get(endpoint, target), target)
            if relation in ('>=', '='): lower[endpoint] = max(lower.get(endpoint, target), target)
        self.impossible = lower.get(0, 0) > 0
        # Individual integral prohibitions are safe on the ORIGINAL weights.
        # Lower-only large weights are retained and later capped for credit.
        self.eligible = tuple(e for e in range(self.n) if e in self.allowed and self.rank[1 << e] > 0
                              and not any(e < endpoint and self.weights[e] > target
                                          for endpoint, target in upper.items()))
        original_mask = sum(1 << e for e in self.eligible)
        if self.mandatory and self.rank[original_mask] < self.total:
            self.impossible = True
        kept, best = [], None
        for endpoint in sorted(upper, reverse=True):
            target = upper[endpoint]
            if target > 0 and (best is None or target < best): kept.append((endpoint, target))
            best = target if best is None else min(best, target)
        uppers = tuple(reversed(kept))
        kept, best = [], 0
        for endpoint in sorted(lower):
            if lower[endpoint] > best:
                kept.append((endpoint, lower[endpoint])); best = lower[endpoint]
        lowers = tuple(kept)
        self.prepared = tuple((p, '<=', b) for p, b in uppers)+tuple((p, '>=', b) for p, b in lowers)
        largest_lower = max((b for _, b in lowers), default=0)
        self.mass_cap = self.bound+max(largest_lower-1, 0)
        # Each positive coordinate has at most one active and one passive
        # coordinate. Zero weight and no-lower systems need only passive ones.
        self.copies = tuple((e, bit) for e in self.eligible
                            for bit in ((0, 1) if self.weights[e] and lowers else (0,)))
        if not self.mandatory:
            self.copies += ((self.n, 0),)  # zero-cost disposal, outside all prefixes
        grouped, zero = {}, []
        for i, (e, active) in enumerate(self.copies):
            weight = min(self.weights[e], self.bound) if e < self.n else 0
            support = tuple(j for j, (end, relation, _) in enumerate(self.prepared)
                            if e < end and weight and (relation == '<=' or active))
            if support: grouped.setdefault((support, weight), []).append(i)
            else: zero.append(i)
        self.classes = tuple((weight, support, tuple(grouped[support, weight]))
                             for support, weight in sorted(grouped))
        self.zero_group = tuple(zero)

    def profiles(self):
        """Only actual occupied classes, with binary total and weighted cap."""
        if self.impossible:
            return
        if not self.classes or not self.mass_cap:
            yield (0,)*len(self.classes)
            return
        yield from occupied.profile_counts(tuple(F(weight, self.mass_cap) for weight, _, _ in self.classes), self.total)

    def _profile(self, profile):
        profile = tuple(profile)
        if (len(profile) != len(self.classes) or any(type(x) is not int or x < 0 for x in profile)
                or sum(profile) > self.total
                or sum(weight*x for (weight, _, _), x in zip(self.classes, profile)) > self.mass_cap):
            raise ValueError('valid binary occupied-class profile required')
        return profile

    def _filter(self, profile):
        for j, (_, relation, target) in enumerate(self.prepared):
            value = sum(weight*x for (weight, support, _), x in zip(self.classes, profile) if j in support)
            if (relation == '<=' and value > target) or (relation == '>=' and value < target):
                return False
        return True

    def realize(self, profile):
        """Exact signed optimum on one integer profile; no extra budget row."""
        profile = self._profile(profile)
        if self.impossible or not self._filter(profile):
            return None
        remainder = self.total-sum(profile)
        if remainder and not self.zero_group:
            return None
        size = len(self.copies)
        a, b = [], []
        # Aggregation gives exactly the shared copied resource inequalities;
        # no complete rank table on the copied ground is ever constructed.
        for subset, cap in enumerate(self.rank):
            a.append(tuple(F(e < self.n and bool(subset >> e & 1)) for e, _ in self.copies))
            b.append(F(cap))
        a.append((F(1),)*size); b.append(F(self.total))
        for (_, _, group), cap in zip(self.classes, profile):
            members = set(group)
            a.append(tuple(F(i in members) for i in range(size))); b.append(F(cap))
        members = set(self.zero_group)
        a.append(tuple(F(i in members) for i in range(size))); b.append(F(remainder))
        cost = tuple(self.costs[e] if e < self.n else F(0) for e, _ in self.copies)
        dominant = 2*self.total*max((abs(c) for c in cost), default=F(0))+1
        objective = tuple(dominant+(c if self.maximize else -c) for c in cost)
        x, y = linear.simplex(a, b, objective)
        if not linear.verify_lp(a, b, objective, x, y):
            raise RuntimeError('invalid shared-resource profile LP certificate')
        if any(v.denominator != 1 for v in x):
            raise RuntimeError('integral resource/partition intersection returned fractional counts')
        if sum(x, F(0)) != self.total:
            return None
        answer = [0]*self.n
        for (e, _), count in zip(self.copies, x):
            if e < self.n: answer[e] += int(count)
        answer = tuple(answer)
        result = Solution(answer, sum((c*v for c, v in zip(self.costs, answer)), F(0)))
        if not self.verify(result):
            raise RuntimeError('profile projection failed original-input verification')
        return result

    def verify(self, solution):
        try:
            if (type(solution) is not Solution or type(solution.counts) is not tuple
                    or len(solution.counts) != self.n or type(solution.cost) not in (int, F)):
                return False
            x = solution.counts
            if any(type(v) is not int or v < 0 or (e not in self.allowed and v)
                   for e, v in enumerate(x)):
                return False
            if self.mandatory and sum(x) != self.total:
                return False
            if any(sum(x[e] for e in range(self.n) if s >> e & 1) > cap for s, cap in enumerate(self.rank)):
                return False
            for endpoint, relation, target in self.rows:
                value = sum(self.weights[e]*x[e] for e in range(endpoint))
                if ((relation in ('<=', '=') and value > target)
                        or (relation in ('>=', '=') and value < target)):
                    return False
            return solution.cost == sum((c*v for c, v in zip(self.costs, x)), F(0))
        except (ValueError, TypeError, AttributeError, IndexError):
            return False

    def solve(self):
        """Return exact original optimum or None; profile success is exact."""
        self.last_trace = dict(profiles=0, row_rejections=0, empty_faces=0, recovered=0,
                               copies=len(self.copies), classes=len(self.classes),
                               colors=len({support for _, support, _ in self.classes}))
        best = None
        for profile in self.profiles():
            self.last_trace['profiles'] += 1
            if not self._filter(profile):
                self.last_trace['row_rejections'] += 1
                continue
            answer = self.realize(profile)
            if answer is None:
                self.last_trace['empty_faces'] += 1
                continue
            self.last_trace['recovered'] += 1
            if best is None or (answer.cost > best.cost if self.maximize else answer.cost < best.cost):
                best = answer
        return best
