#!/usr/bin/env python3
"""Exact continuous-domain bounds for three positive-containment lookups.

This standard-library module supplies the mathematical kernel for a separate
manifest-driven verifier. Four normalized box coordinates cover every legal
color. Gibbs planes, certified entropy lower bounds and whole-box maxima
are the only acceptance ingredients; numerical optimization proposes planes
but cannot accept a leaf. The analytic containment and pooled-trace lemmas
remain explicit mathematical premises.

The exact logarithm enclosure and the first trace bound follow the maintained
two-level checker. The third lookup, normalized coordinate, and multiaffine
necessary-constraint projection are proved in the accompanying manuscript.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from fractions import Fraction as F
from functools import lru_cache
import hashlib
from itertools import product
import json
import math
import multiprocessing
from pathlib import Path
import time


if not __debug__:
    raise SystemExit("Run mathematical verification without python -O.")


CHECKER_SHA256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
A, B, S, T = F(".065"), F(".075"), F(".14"), F(".45")
PD, LD = 10**12, 10**14
SCALE = 1 << 128
TERMS = 32


def ceildiv(n: int, d: int) -> int:
    if d <= 0:
        raise ValueError("positive denominator required")
    return -((-n) // d)


def ln_scaled(v: F) -> tuple[int, int]:
    """Integer bounds for SCALE*ln(v), for the exact rational 1<=v<=2."""
    if not 1 <= v <= 2:
        raise ValueError("normalized logarithm outside [1,2]")
    q = (v - 1) / (v + 1)
    lo = q.numerator * SCALE // q.denominator
    hi = ceildiv(q.numerator * SCALE, q.denominator)
    q2lo, q2hi = lo * lo // SCALE, ceildiv(hi * hi, SCALE)
    plo, phi, total_lo, total_hi = lo, hi, 0, 0
    for j in range(TERMS):
        total_lo += 2 * plo // (2 * j + 1)
        total_hi += ceildiv(2 * phi, 2 * j + 1)
        plo = plo * q2lo // SCALE
        phi = ceildiv(phi * q2hi, SCALE)
    # phi/SCALE >= q**65 and q2hi/SCALE >= q**2.
    total_hi += ceildiv(2 * phi * SCALE, 65 * (SCALE - q2hi))
    return total_lo, total_hi


LN2_LO, LN2_HI = ln_scaled(F(2))


@lru_cache(maxsize=200_000)
def log_scaled(x: F) -> tuple[int, int]:
    """Integer bounds for LD*log2(x); no floating-point arithmetic."""
    if x <= 0:
        raise ValueError("nonpositive logarithm argument")
    k = x.numerator.bit_length() - x.denominator.bit_length()
    v = x / (F(2) ** k)
    if v < 1:
        v *= 2
        k -= 1
    if v >= 2:
        v /= 2
        k += 1
    lo, hi = ln_scaled(v)
    # The normalized logarithm is nonnegative, hence opposite denominator
    # endpoints give valid quotients.  k is added exactly, including k<0.
    return (k * LD + lo * LD // LN2_HI,
            k * LD + ceildiv(hi * LD, LN2_LO))


@lru_cache(maxsize=200_000)
def entropy_lower(c: F, y: F) -> F:
    """A rational lower bound for LD*H(c,y)."""
    if not 0 <= y <= c:
        raise ValueError("entropy outside its closed domain")
    if y == 0 or y == c:
        return F(0)
    return max(F(0), -y * log_scaled(y / c)[1]
               - (c - y) * log_scaled((c - y) / c)[1])


def entropy_float(c: float, y: float) -> float:
    if c <= 0 or y <= 0 or y >= c:
        return 0.0
    p = y / c
    return -y * math.log2(p) - (c - y) * math.log2(1 - p)


def probability(y: float, c: float) -> int:
    p = y / c if c > 0 else 0.5
    return min(PD - 1000, max(1000, round(p * PD)))


@lru_cache(maxsize=200_000)
def gibbs_exact(p: int) -> tuple[int, int]:
    if not 0 < p < PD:
        raise ValueError("Gibbs probability must be in (0,1)")
    return -log_scaled(F(p, PD))[0], -log_scaled(F(PD - p, PD))[0]


def aff(value=0, index=None):
    # Coefficients are constant, m, z, v, w2, auxiliary third color.  The last
    # coordinate is eliminated with a globally valid affine endpoint.
    a = [F(0)] * 6
    a[0 if index is None else index] = F(value)
    return tuple(a)


def add(*args):
    return tuple(sum(a[i] for a in args) for i in range(6))


def mul(c, a):
    return tuple(c * x for x in a)


def sub(a, b):
    return add(a, mul(-1, b))


def at(a, point):
    value = a[0]
    for coefficient, coordinate in zip(a[1:], point):
        if coefficient:
            value += coefficient * coordinate
    return value


ZERO, ONE = aff(0), aff(1)
M, Z, V, W2, AUX = (aff(1, i) for i in range(1, 6))


def corners(box):
    return list(product(*((lo,) if lo == hi else (lo, hi) for lo, hi in box)))


class Family:
    def __init__(self, rho: F, gamma: F | None, tau: F, target: F,
                 branch: str, gamma2: F = F(1, 2), gamma3: F = F(1, 2)):
        self.rho, self.gamma, self.gamma2, self.gamma3 = rho, gamma, gamma2, gamma3
        self.tau, self.target, self.branch = tau, target, branch
        if not (0 < A < S < 1 and B == S - A and 0 < T < 1
                and rho > 1 and 0 < tau < 1 and target > 0 and 0 < gamma2 < 1 and 0 < gamma3 < 1):
            raise ValueError("invalid fixed types or contact parameters")
        beta_top = A + rho * (S - A)
        if beta_top >= min(T, 1 - T, 1 - S):
            raise ValueError("the outer and trace entropy domains require a smaller beta")
        if branch != "direct" and (gamma is None or not 0 < gamma < 1):
            raise ValueError("recursive lookup fraction must lie in (0,1)")
        if branch != "direct":
            # The certificate must cover every outer color. Dropping colors
            # whose first query does not fit would not justify a circuit.
            # The containment defect is affine in m, so both endpoints suffice.
            for endpoint in (A, S):
                beta = A + rho * (endpoint - A)
                if gamma * beta < beta - endpoint:
                    raise ValueError("first lookup misses an outer-domain query")
        self.beta = add(aff(A * (1 - rho)), mul(rho, M))
        self.c = mul(gamma or F(0), self.beta)
        self.c2 = mul(gamma2, self.c)
        self.cut = mul(1 - gamma2, self.c)
        self.c3 = mul(gamma3, self.c2)
        self.q3 = sub(self.c2, W2)
        self.d3 = sub(self.c3, self.q3)
        self.q1 = sub(self.beta, Z)
        self.d1 = sub(self.c, self.q1)
        self.w1 = add(self.cut, V)
        self.q = sub(self.c2, V)
        self.d = sub(M, aff(A))
        self.r = sub(aff(S), M)
        self.D = sub(sub(self.beta, M), self.w1)
        self.constraints = [sub(Z, M), sub(self.beta, Z)]
        if branch == "push":
            self.constraints += [sub(M, self.c2),
                                 sub(Z, sub(self.beta, self.cut))]
        elif branch == "recursive":
            self.constraints += [V, sub(V, sub(self.q1, self.cut)),
                                 sub(V, sub(self.c2, M)),
                                 sub(self.c2, V), self.D]
        elif branch != "direct":
            raise ValueError("unknown branch")
        self.h0 = (sub(ONE, M), sub(self.beta, M))
        self.h1 = (Z, self.d1)
        self.h2 = (self.w1, V)
        self.h3 = (W2, self.d3)
        self.second_constraints = [sub(W2, self.q), sub(W2, sub(self.c2, self.q1)),
                                   sub(self.d1, W2), sub(self.c2, W2)]

    def initial(self):
        top = at(self.beta, (S, F(0), F(0)))
        vmax = at(self.c2, (S, F(0), F(0))) if self.branch == "recursive" else F(0)
        return ((A, S), (A, top), (F(0), vmax),
                (F(0), F(1) if self.branch == "recursive" else F(0)))

    def tighten(self, original):
        """Necessary affine propagation.  No floating-point pruning."""
        box = [list(pair) for pair in original]
        for _ in range(3):
            changed = False
            for constraint in self.constraints:
                terms = [max(constraint[i + 1] * box[i][0],
                             constraint[i + 1] * box[i][1]) for i in range(4)]
                maximum = constraint[0] + sum(terms)
                if maximum < 0:
                    return None
                for i in range(4):
                    coef = constraint[i + 1]
                    if not coef:
                        continue
                    endpoint = -(maximum - terms[i]) / coef
                    side = 0 if coef > 0 else 1
                    if ((side == 0 and endpoint > box[i][0]) or
                            (side == 1 and endpoint < box[i][1])):
                        box[i][side] = endpoint
                        changed = True
                        if box[i][0] > box[i][1]:
                            return None
            if not changed:
                break
        result = tuple(tuple(pair) for pair in box)
        if self.branch == "recursive":
            # A multiaffine constraint is a convex combination of its
            # one-coordinate corner lines. Their feasible interval hull
            # supplies necessary coordinate bounds, without unsafe nonlinear
            # interval division or a sign assumption on a varying slope.
            for _ in range(2):
                changed = False
                for constraint in self.second_constraints:
                    raw = corners(result)
                    mapped = self.mapped_corners(result)
                    values = [at(constraint, vertex) for vertex in mapped]
                    if max(values) < 0:
                        return None
                    replacement = list(result)
                    for axis, (lo, hi) in enumerate(result):
                        if lo == hi:
                            continue
                        lines = {}
                        for point, value in zip(raw, values):
                            key = point[:axis] + point[axis+1:]
                            lines.setdefault(key, {})[point[axis]] = value
                        allowed = []
                        for endpoints in lines.values():
                            left, right = endpoints[lo], endpoints[hi]
                            if left >= 0 and right >= 0:
                                allowed = [(lo, hi)]
                                break
                            if left < 0 and right < 0:
                                continue
                            root = lo - left * (hi-lo) / (right-left)
                            allowed.append((lo, root) if left >= 0 else (root, hi))
                        if not allowed:
                            return None
                        interval = (min(pair[0] for pair in allowed),
                                    max(pair[1] for pair in allowed))
                        if interval != result[axis]:
                            replacement[axis] = interval
                            changed = True
                    result = tuple(replacement)
                if not changed:
                    break
        return result

    @lru_cache(maxsize=8)
    def mapped_corners(self, box):
        if self.branch != "recursive":
            return corners(box)
        result = []
        for m, z, v, theta in corners(box):
            point = (m, z, v, F(0))
            lo, hi = at(self.q, point), at(self.d1, point)
            result.append((m, z, v, lo + theta * (hi - lo)))
        return result

    def center(self, box):
        m, z, v, theta = (float((lo + hi) / 2) for lo, hi in box)
        w2 = 0.0
        beta = float(A) + float(self.rho) * (m - float(A))
        c = float(self.gamma or 0) * beta
        c2, cut = float(self.gamma2) * c, float(1 - self.gamma2) * c
        if self.branch == "push":
            z = min(beta, max(z, m, beta - cut))
            v, w2 = 0.0, 0.0
        elif self.branch == "recursive":
            vlo, vhi = max(0.0, c2 - m), min(c2, beta - m - cut)
            v = max(vlo, min(vhi, v))
            z = min(beta, max(z, m, beta - cut - v))
            q1, d1, q = beta - z, c - beta + z, c2 - v
            lo, hi = max(q, c2 - q1, 0.0), min(d1, c2)
            w2 = max(lo, min(hi, q + theta * (d1 - q)))
        else:
            z = min(beta, max(z, m))
            v, w2 = 0.0, 0.0
        return m, z, v, w2

    @staticmethod
    def stationary(lo, hi, derivative):
        if hi <= lo + 1e-17:
            return (lo + hi) / 2
        for _ in range(42):
            mid = (lo + hi) / 2
            if derivative(mid) > 0:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    def propose(self, box):
        m, z, v, w2 = center = self.center(box)
        rho, gamma, tau = float(self.rho), float(self.gamma or 0), float(self.tau)
        beta = float(A) + rho * (m - float(A))
        c, d, r = gamma * beta, m - float(A), float(S) - m
        c2, cut = float(self.gamma2) * c, float(1 - self.gamma2) * c
        q1, d1 = beta - z, c - beta + z
        p = {"outer1": probability(z, float(T)),
             "outer2": probability(beta - z, 1 - float(T)),
             "B": probability(d, float(B))}
        log = lambda x: math.log(max(x, 1e-300))
        if self.branch == "direct":
            p["direct"] = probability(z - m, beta - m)
        elif self.branch == "push":
            lo, hi = max(q1, c - m, 0.0), min(beta - m, cut)
            def derivative(w):
                return ((1 - tau) * (log(beta - m - w) + log(c - w)
                        - log(w) - log(m - c + w))
                        + tau * (log(c - w) - log(w - q1)))
            w = self.stationary(lo, hi, derivative)
            p.update(push1=probability(w, beta - m),
                     push2=probability(c - w, m),
                     push3=probability(w - q1, d1))
            wzero = max(lo, min(hi, q1 + d1 / 2))
            p["pushzero"] = probability(wzero - q1, d1)
        else:
            w1, q = cut + v, c2 - v
            D = beta - m - w1
            p.update(first1=probability(w1, beta - m),
                     first2=probability(q, m),
                     inner1=probability(w2, d1),
                     inner2=probability(c2 - w2, q1),
                     thirdpush=probability(w2 - q, v))
            c3, q3 = float(self.gamma3) * c2, c2 - w2
            d3 = c3 - q3
            lo3, hi3 = max(q3, c3 - q, 0.0), min(v, c3)
            def derivative3(w3):
                return ((1 - tau) * (log(v - w3) + log(c3 - w3)
                        - log(w3) - log(q - c3 + w3))
                        + tau * (log(c3 - w3) - log(w3 - q3)))
            w3 = self.stationary(lo3, hi3, derivative3)
            p.update(third1=probability(w3, v),
                     third2=probability(c3 - w3, q),
                     third3=probability(w3 - q3, d3))
            yz = max(0.0, d3 - q, min(d3, w2 - q, d3 / 2))
            p["thirdzero"] = probability(yz, d3)
            if (beta >= float(S) or
                    at(self.beta, (box[0][0], F(0), F(0), F(0))) >= S):
                glo, ghi = max(0.0, w1 - (beta - float(S))), min(r, w1)
                def dg(g):
                    return (log(float(B) - g) + log(float(S) - g - q)
                            + log(w1 - g) - log(g) - log(float(S) - g)
                            - log(beta - float(S) - w1 + g))
                g = self.stationary(glo, ghi, dg)
                p.update(A1=probability(g, float(B)),
                         A2=probability(q, float(S) - g),
                         A3=probability(w1 - g, beta - float(S)))
                def du(u):
                    return (log(r - u) + log(m + u) + log(D - u)
                            - log(d + u) - log(m + u - q)
                            - log(1 - float(S) - D + u))
                u = self.stationary(0.0, min(r, D), du)
                p.update(J1=probability(d + u, float(B)),
                         J2=probability(q, m + u),
                         J3=probability(D - u, 1 - float(S)),
                         J4=probability(w1, 1 - m - D))
        return center, p

    def negative(self, pair, vertices, exact):
        arguments = [(at(pair[0], v), at(pair[1], v)) for v in vertices]
        if any(not 0 <= y <= c for c, y in arguments):
            # The entropy is nonnegative on the feasible domain even when
            # an enlarged rectangular corner is invalid.
            return [F(0) if exact else 0.0 for _ in vertices]
        if exact:
            return [entropy_lower(c, y) for c, y in arguments]
        return [entropy_float(float(c), float(y)) for c, y in arguments]

    @lru_cache(maxsize=8)
    def closed_delta(self, box):
        # These forms depend only on the first three coordinates. Exact
        # affine extrema equal enumeration of all normalized-box vertices.
        def bounds(form):
            lower = upper = form[0]
            for coefficient, (left, right) in zip(form[1:], box):
                if coefficient:
                    first, second = coefficient * left, coefficient * right
                    lower += min(first, second)
                    upper += max(first, second)
            return lower, upper
        if bounds(self.beta)[0] < S:
            return F(0)
        d0, _ = bounds(self.d)
        mq0, _ = bounds(sub(M, self.q))
        dq0, _ = bounds(sub(self.d, self.q))
        wr0, _ = bounds(sub(self.w1, self.r))
        D0, D1 = bounds(self.D)
        _, r1 = bounds(self.r)
        m0, m1 = box[0]
        if min(dq0, mq0, wr0, D0) < 0:
            return F(0)
        if d0 * mq0 * wr0 < r1 * m1 * D1:
            return F(0)
        return F(7, 5) * (S - m1) * D0 / (1 - m0)

    def bound(self, box, proposal, exact):
        center, probabilities = proposal
        vertices = self.mapped_corners(box)
        number = (lambda x: x) if exact else float
        convert = lambda a: tuple(number(x) for x in a)
        scale = LD if exact else 1.0
        tau, rtau = number(self.tau), number(1 - self.tau)
        h0 = self.negative(self.h0, vertices, exact)
        h1 = self.negative(self.h1, vertices, exact) if self.branch != "direct" else None
        points = vertices if exact else [tuple(float(x) for x in v) for v in vertices]

        def gib(key, c, y):
            p = probabilities[key]
            if exact:
                cp, cq = gibbs_exact(p)
            else:
                cp, cq = -math.log2(p / PD), -math.log2((PD - p) / PD)
            c, y = convert(c), convert(y)
            return add(mul(cp, y), mul(cq, sub(c, y)))

        def eliminate(f, lower, upper):
            coef = f[5]
            endpoints = upper if coef >= 0 else lower
            # Each candidate is globally one-sided.  The center chooses one
            # affine expression, which remains fixed throughout this box.
            endpoint = (min(endpoints, key=lambda e: float(at(e, center)))
                        if coef >= 0 else
                        max(endpoints, key=lambda e: float(at(e, center))))
            base = tuple(f[i] if i != 5 else number(F(0)) for i in range(6))
            return add(base, mul(coef, convert(endpoint)))

        outer = add(gib("outer1", aff(T), Z),
                    gib("outer2", aff(1 - T), self.q1))
        bp = gib("B", aff(B), self.d)
        outer_values = [tau * max(0, at(outer, v) - h)
                        for v, h in zip(points, h0)]
        bvalues = [at(bp, v) for v in points]
        if self.branch == "direct":
            direct = gib("direct", sub(self.beta, M), sub(Z, M))
            (m0, m1), (z0, z1), _, _ = box
            delta = (F(7, 5) * (S - m1) * max(0, z0 - m1)
                     if m0 > A and self.rho * (m0 - A)**2 >= B * (z1 - A)
                     else F(0))
            value = max(o + rtau * (b + at(direct, v) - scale * number(delta))
                        for o, b, v in zip(outer_values, bvalues, points))
            return value, "direct"

        if self.branch == "push":
            lower = [self.q1, sub(self.c, M), ZERO]
            upper = [sub(self.beta, M), self.cut]
            raw = add(mul(rtau, gib("push1", sub(self.beta, M), AUX)),
                      mul(rtau, gib("push2", M, sub(self.c, AUX))),
                      mul(tau, gib("push3", self.d1, sub(AUX, self.q1))))
            raw = eliminate(raw, lower, upper)
            zero = eliminate(mul(tau, gib("pushzero", self.d1,
                                          sub(AUX, self.q1))), lower, upper)
            value = max(o + rtau * b + max(at(raw, v) - rtau * h, at(zero, v))
                        for o, b, h, v in zip(outer_values, bvalues, h1, points))
            return value, "push"

        h2 = self.negative(self.h2, vertices, exact)
        second = add(gib("inner1", self.d1, W2),
                     gib("inner2", self.q1, sub(self.c2, W2)))
        push3 = mul(rtau, gib("thirdpush", V, sub(W2, self.q)))
        side_lo = min(at(self.d3, v) for v in vertices)
        side_hi = max(at(self.d3, v) for v in vertices)
        third_values = [at(push3, v) for v in points]
        if side_hi > 0 or side_lo >= 0:
            h3 = self.negative(self.h3, vertices, exact)
            raw3 = add(mul(rtau, gib("third1", V, AUX)),
                       mul(rtau, gib("third2", self.q, sub(self.c3, AUX))),
                       mul(tau, gib("third3", self.d3, sub(AUX, self.q3))))
            raw3 = eliminate(raw3, [self.q3, sub(self.c3, self.q), ZERO],
                             [V, self.c3])
            zero3 = eliminate(mul(tau, gib("thirdzero", self.d3, AUX)),
                              [ZERO, sub(self.d3, self.q)],
                              [self.d3, sub(W2, self.q)])
            recursive3 = [max(at(raw3, v) - rtau * h, at(zero3, v))
                          for v, h in zip(points, h3)]
            if side_lo >= 0:
                third_values = recursive3
            else:
                # Both affine routing domains may meet this box. Taking
                # their maximum preserves coverage and separate convexity.
                third_values = [max(p, r) for p, r in zip(third_values, recursive3)]
        common = [o + tau * max(0, at(second, v) - h) + third
                  for o, h, v, third in zip(outer_values, h2, points, third_values)]
        first = add(gib("first1", sub(self.beta, M), self.w1),
                    gib("first2", M, self.q))
        delta = self.closed_delta(box)
        old = max(c + rtau * (b + max(0, at(first, v) - h - scale * number(delta)))
                  for c, b, h, v in zip(common, bvalues, h1, points))
        candidates = [(old, "closed" if delta else "old")]
        if min(at(self.beta, v) for v in vertices) >= S:
            ap = add(gib("A1", aff(B), AUX),
                     gib("A2", sub(aff(S), AUX), self.q),
                     gib("A3", sub(self.beta, aff(S)), sub(self.w1, AUX)))
            ap = eliminate(ap, [ZERO, sub(self.w1, sub(self.beta, aff(S)))],
                           [self.r, self.w1])
            jp = add(gib("J1", aff(B), add(self.d, AUX)),
                     gib("J2", add(M, AUX), self.q),
                     gib("J3", aff(1 - S), sub(self.D, AUX)),
                     gib("J4", sub(sub(ONE, M), self.D), self.w1))
            jp = eliminate(jp, [ZERO], [self.r, self.D])
            continuous = max(c + rtau * max(b, at(ap, v) - e1,
                                             at(jp, v) - e0 - e1)
                             for c, b, e0, e1, v in
                             zip(common, bvalues, h0, h1, points))
            candidates.append((continuous, "continuous"))
        # A pointwise minimum at vertices would not be separately convex.
        # Both candidates already bound their ENTIRE box before this minimum.
        return min(candidates)


def verify_contact(job):
    rho, gamma, gamma2, gamma3, tau, target, branch, max_nodes = job
    family = Family(F(rho), None if gamma == "direct" else F(gamma),
                    F(tau), F(target), branch, F(gamma2), F(gamma3))
    pending = [(family.initial(), 0)]
    nodes, leaves, empty, depthmax = 0, 0, 0, 0
    methods = Counter()
    largest, margin = F(0), None
    started = time.monotonic()
    while pending:
        original, depth = pending.pop()
        nodes += 1
        if nodes > max_nodes:
            raise RuntimeError(f"node limit reached: {rho}, {gamma}, {tau}, {branch}")
        box = family.tighten(original)
        if box is None:
            empty += 1
            continue
        proposal = family.propose(box)
        floating, _ = family.bound(box, proposal, False)
        if floating <= float(family.target) + 1e-12:
            upper, method = family.bound(box, proposal, True)
            if upper <= LD * family.target:
                leaves += 1
                methods[method] += 1
                largest = max(largest, upper / LD)
                difference = family.target - upper / LD
                margin = difference if margin is None else min(margin, difference)
                depthmax = max(depthmax, depth)
                continue
        gap = max(F(0), max(at(sub(family.d1, family.q), point)
                               for point in corners(box)))
        widths = [(box[i][1] - box[i][0]) * weight
                  for i, weight in enumerate((F(3), F(1), F(2), 2 * gap))]
        axis = max(range(4), key=lambda i: (widths[i], -i))
        if widths[axis] == 0 or depth >= 90:
            raise RuntimeError(f"unresolved box: rho={rho}, gamma={gamma}, tau={tau}, "
                               f"branch={branch}, box={box}, bound={floating}")
        mid = (box[axis][0] + box[axis][1]) / 2
        left, right = list(box), list(box)
        left[axis], right[axis] = (box[axis][0], mid), (mid, box[axis][1])
        pending.append((tuple(right), depth + 1))
        pending.append((tuple(left), depth + 1))
    if nodes != 2 * (leaves + empty) - 1:
        raise RuntimeError("the completed binary subdivision has inconsistent node counts")
    return dict(rho=rho, gamma=gamma, gamma2=gamma2, gamma3=gamma3, tau=tau, target=target, branch=branch,
                leaves=leaves, empty=empty, nodes=nodes, depth=depthmax,
                maximum=str(largest), minimum_margin=None if margin is None else str(margin),
                methods=dict(methods),
                seconds=round(time.monotonic() - started, 3))


ROOT = Path(__file__).resolve().parents[1]
MENU_PATH = ROOT / "problems/subset-sum-fast-deterministic/verify/third_contacts.json"
DRIVER_PATH = MENU_PATH.with_name("replay_third_contacts.py")
FIELDS = ("rho", "gamma", "gamma2", "gamma3", "tau", "target", "branch")


def require(condition, message):
    if not condition:
        raise ValueError("invalid third-lookup certificate: " + message)


def read_menu():
    """Read the fixed menu and validate every analytic family hypothesis.

    Loading this module in a spawned worker repeats this initialization;
    correctness does not depend on fork-inherited mutable globals.
    """
    global A, B, S, T
    raw = MENU_PATH.read_bytes()
    menu = json.loads(raw)
    require(set(menu) == {"types", "families"}, "menu fields")
    require(set(menu["types"]) == {"a", "b", "s", "t"}, "type fields")
    require(all(isinstance(value, str) for value in menu["types"].values()),
            "types must be exact rational strings")
    A, B, S, T = (F(menu["types"][key]) for key in ("a", "b", "s", "t"))
    require(isinstance(menu["families"], list) and menu["families"], "empty menu")
    seen_families, choices = set(), []
    for family in menu["families"]:
        require(set(family) == {"rho", "gamma", "gamma2", "gamma3", "contacts"},
                "family fields")
        values = tuple(family[key] for key in ("rho", "gamma", "gamma2", "gamma3"))
        require(all(isinstance(value, str) for value in values),
                "family parameters must be exact rational strings")
        rational_values = tuple(map(F, values))
        require(rational_values not in seen_families, "duplicate circuit family")
        seen_families.add(rational_values)
        require(isinstance(family["contacts"], list) and family["contacts"],
                "empty contact list")
        previous = F(0)
        for point in family["contacts"]:
            require(isinstance(point, list) and len(point) == 2
                    and all(isinstance(value, str) for value in point),
                    "contacts must be pairs of exact rational strings")
            tau, target = map(F, point)
            require(previous < tau < 1 and target > 0, "unordered or invalid contact")
            previous = tau
            rho, gamma, gamma2, gamma3 = rational_values
            for branch in ("push", "recursive"):
                Family(rho, gamma, tau, target, branch, gamma2, gamma3)
                choices.append(dict(zip(FIELDS, (*values, *point, branch))))
    return menu, hashlib.sha256(raw).hexdigest(), choices


MENU, MENU_SHA256, EXPECTED_CHOICES = read_menu()


def unchanged_sources():
    require(hashlib.sha256(Path(__file__).read_bytes()).hexdigest() == CHECKER_SHA256,
            "kernel bytes changed during replay")
    require(hashlib.sha256(MENU_PATH.read_bytes()).hexdigest() == MENU_SHA256,
            "menu bytes changed during replay")


def validate_result(row, choice):
    require({key: row.get(key) for key in FIELDS} == choice, "result choice")
    counts = tuple(row.get(key) for key in ("leaves", "empty", "nodes", "depth"))
    require(all(type(value) is int and value >= 0 for value in counts), "result counts")
    leaves, empty, nodes, depth = counts
    require(nodes == 2 * (leaves + empty) - 1, "incomplete binary subdivision")
    require(depth <= 90, "subdivision depth")
    allowed = {"push"} if choice["branch"] == "push" else {"old", "closed", "continuous"}
    methods = row.get("methods", {})
    require(set(methods) <= allowed
            and all(type(value) is int and value > 0 for value in methods.values())
            and sum(methods.values()) == leaves, "method counts")
    maximum = F(row["maximum"])
    if leaves:
        margin = F(row["minimum_margin"])
        require(0 <= maximum <= F(choice["target"]) and margin >= 0
                and maximum + margin == F(choice["target"]), "acceptance margin")
    else:
        require(empty > 0 and maximum == 0 and row["minimum_margin"] is None,
                "empty-domain result")


def make_receipt(results, segmented=None):
    unchanged_sources()
    require(len(results) == len(EXPECTED_CHOICES), "incomplete menu")
    indexed = {}
    for row in results:
        key = tuple(row[name] for name in FIELDS)
        require(key not in indexed, "duplicate branch result")
        indexed[key] = row
    ordered = []
    for choice in EXPECTED_CHOICES:
        key = tuple(choice[name] for name in FIELDS)
        require(key in indexed, "missing branch result")
        validate_result(indexed[key], choice)
        ordered.append(indexed[key])
    return dict(receipt_schema=1, certificate_kind="third_lookup_contacts", status="PASS",
                checker_sha256=CHECKER_SHA256, menu_sha256=MENU_SHA256,
                expected_choices=EXPECTED_CHOICES, expected_branch_count=len(EXPECTED_CHOICES),
                branches=len(ordered), leaves=sum(row["leaves"] for row in ordered),
                nodes=sum(row["nodes"] for row in ordered),
                empty=sum(row["empty"] for row in ordered),
                maximum_depth=max(row["depth"] for row in ordered),
                minimum_margin=min((row["minimum_margin"] for row in ordered
                                    if row["minimum_margin"] is not None), key=F),
                arithmetic="exact rationals; integer interval atanh logarithms",
                scope="Continuous-domain contact bounds conditional on the separate containment, pooled-trace, and four-dimensional acceptance proofs; this receipt alone does not establish an algorithmic exponent.",
                replay_kind="segmented_trusted_local" if segmented else "clean",
                segmented_replay=segmented, results=ordered)


def check_receipt(path):
    receipt = json.loads(path.read_text())
    require(receipt.get("receipt_schema") == 1
            and receipt.get("certificate_kind") == "third_lookup_contacts"
            and receipt.get("status") == "PASS", "receipt schema or status")
    require(receipt.get("checker_sha256") == CHECKER_SHA256, "kernel fingerprint")
    require(receipt.get("menu_sha256") == MENU_SHA256, "menu fingerprint")
    segmented = receipt.get("segmented_replay")
    if segmented is not None:
        require(DRIVER_PATH.exists(), "missing recovery driver")
        require(segmented.get("driver_sha256")
                == hashlib.sha256(DRIVER_PATH.read_bytes()).hexdigest(), "driver fingerprint")
        require(segmented.get("completed_branches") == len(EXPECTED_CHOICES),
                "segmented provenance count")
    rebuilt = make_receipt(receipt.get("results", []), segmented)
    for key in rebuilt:
        require(receipt.get(key) == rebuilt[key], "receipt field " + key)
    return {key: rebuilt[key] for key in ("status", "branches", "leaves", "nodes", "empty",
                                          "maximum_depth", "minimum_margin", "replay_kind")}


def write_receipt(path, receipt):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(receipt, indent=2) + "\n")
    temporary.replace(path)


def worker_sources(checker_digest, menu_digest):
    require(CHECKER_SHA256 == checker_digest and MENU_SHA256 == menu_digest,
            "spawned worker source mismatch")
    unchanged_sources()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    operation = parser.add_mutually_exclusive_group(required=True)
    operation.add_argument("--all", action="store_true", help="clean replay of all fixed-menu branches")
    operation.add_argument("--receipt", type=Path, help="check stored receipt binding and bookkeeping only")
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--max-nodes", type=int, default=5_000_000)
    parser.add_argument("--output", type=Path, help="write a complete receipt only after all branches pass")
    args = parser.parse_args()
    if args.jobs < 1 or args.max_nodes < 1:
        parser.error("positive jobs and node limit required")
    if args.receipt:
        if args.output:
            parser.error("--output applies only to --all")
        print(json.dumps(check_receipt(args.receipt), sort_keys=True))
        return
    jobs = [tuple(choice[key] for key in FIELDS) + (args.max_nodes,)
            for choice in EXPECTED_CHOICES]
    results = []
    with ProcessPoolExecutor(max_workers=args.jobs, mp_context=multiprocessing.get_context("spawn"),
                             initializer=worker_sources,
                             initargs=(CHECKER_SHA256, MENU_SHA256)) as pool:
        for future in as_completed([pool.submit(verify_contact, job) for job in jobs]):
            row = future.result()
            results.append(row)
            print(json.dumps(row, sort_keys=True), flush=True)
    receipt = make_receipt(results)
    if args.output:
        write_receipt(args.output, receipt)
    print(json.dumps({key: value for key, value in receipt.items()
                      if key not in {"results", "expected_choices"}}, sort_keys=True))


if __name__ == "__main__":
    main()
