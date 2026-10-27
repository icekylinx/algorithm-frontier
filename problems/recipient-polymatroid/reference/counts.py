"""Exact binary-count polymatroid representation; explicit rank-table costs.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class RankTable:
    n: int
    values: tuple[int, ...]

    def __post_init__(self):
        if type(self.n) is not int or self.n < 0:
            raise ValueError('nonnegative player count required')
        f = tuple(self.values)
        if len(f) != 1 << self.n or any(type(v) is not int or v < 0 for v in f) or f[0]:
            raise ValueError('complete normalized integral rank table required')
        for a in range(len(f)):
            for i in range(self.n):
                if not a >> i & 1 and f[a] > f[a | 1 << i]:
                    raise ValueError('rank is not monotone')
            for b in range(len(f)):
                if f[a] + f[b] < f[a | b] + f[a & b]:
                    raise ValueError('rank is not submodular')
        object.__setattr__(self, 'values', f)

    @property
    def caps(self):
        return tuple(self.values[1 << p] for p in range(self.n))

    def counts(self, z, *, bounded=True):
        z = tuple(z)
        if len(z) != self.n or any(type(x) is not int or x < 0 for x in z):
            raise ValueError('nonnegative integral original-player counts required')
        if bounded and any(x > c for x, c in zip(z, self.caps)):
            raise ValueError('count exceeds its conceptual block')
        return z

    def rank(self, z):
        z = self.counts(z)
        return min(f + sum(x for p, x in enumerate(z) if not a >> p & 1)
                   for a, f in enumerate(self.values))

    def independent(self, z):
        z = self.counts(z)
        return all(sum(x for p, x in enumerate(z) if a >> p & 1) <= f
                   for a, f in enumerate(self.values))

    def contracted(self, z):
        """Rank of unions of whole owner blocks after contracting z."""
        z = self.counts(z)
        base = self.rank(z)
        caps = self.caps
        return tuple(self.rank(tuple(caps[p] if a >> p & 1 else z[p]
                                     for p in range(self.n))) - base
                     for a in range(1 << self.n))

    def availability(self, z):
        z = self.counts(z)
        base, caps = self.rank(z), self.caps
        return tuple(self.rank(z[:p] + (caps[p],) + z[p+1:]) - base
                     for p in range(self.n))

    def recover_comparator(self, z, original):
        """Retain an integral contracted allocation inside an original count box.

        No count expansion: one capped-rank greedy step per original player.
        """
        z, original = self.counts(z), self.counts(original)
        if not self.independent(original):
            raise ValueError('original comparator must satisfy all original ranks')
        g = self.contracted(z)
        h, prefix, previous = [], 0, 0
        for p in range(self.n):
            prefix |= 1 << p
            a, best = prefix, None
            while True:
                value = g[a] + sum(original[q] for q in range(self.n)
                                   if prefix >> q & 1 and not a >> q & 1)
                best = value if best is None else min(best, value)
                if a == 0:
                    break
                a = (a - 1) & prefix
            h.append(best - previous)
            previous = best
        return tuple(h)


def minimal_bundle(counts, values, threshold):
    """One pass of binary bulk deletions; every remaining unit is essential."""
    counts, values = tuple(counts), tuple(values)
    exact = lambda x: type(x) in (int, Fraction)
    if (len(counts) != len(values) or any(type(x) is not int or x < 0 for x in counts)
            or any(not exact(v) or v < 0 for v in values)
            or not exact(threshold) or threshold <= 0):
        raise ValueError('exact nonnegative bundle and positive threshold required')
    values, threshold = tuple(map(Fraction, values)), Fraction(threshold)
    value = sum(n * v for n, v in zip(counts, values))
    if value < threshold:
        raise ValueError('bundle does not reach threshold')
    result = list(counts)
    for j, v in enumerate(values):
        if not v:
            result[j] = 0
            continue
        remove = min(result[j], (value - threshold) // v)
        result[j] -= remove
        value -= remove * v
    return tuple(result)
