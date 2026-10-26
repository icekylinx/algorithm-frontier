#!/usr/bin/env python3
"""Reconstruct the X02 continuous-domain Subset Sum contact certificates.

Run ``python tools/verify_subset_sum_contacts.py --all --jobs 4`` to cover
every contact.  This is a branch-and-bound proof, not a numerical grid test.
Each initial box contains the entire color domain; every tightening is a
necessary affine inequality; bisection preserves coverage.  A nonempty leaf
is accepted only by exact rational inequalities at every box vertex.

The analytic ingredients are joint concavity of homogeneous binary entropy,
its Gibbs affine majorants, and the X02 trace lemma.  Negative entropies use
multiaffine interpolation of certified lower vertex values.  Every resulting
bound is separately convex.  Alternative trace bounds are minimized only
AFTER maximizing each whole-box bound over its vertices.

Floating point proposes tangent probabilities and rejects unpromising boxes.
It never accepts a box, discards a domain, or certifies a logarithm.  Logarithm
enclosures use integer interval arithmetic and the positive atanh series.
The checker validates the stated profile inequalities, conditional on the
analytic trace/circuit lemmas; it does not implement the input algorithm.
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
from pathlib import Path
import time

from verify_subset_sum_scalars import CONTACTS

CHECKER_SHA256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
EXPECTED_CHOICES = [
    dict(rho=rho, gamma=gamma, gamma2=gamma2, tau=tau, target=target, branch=branch)
    for rho, gamma, gamma2, points in CONTACTS
    for tau, target in points
    for branch in (["direct"] if gamma == "direct" else ["push", "recursive"])
]
MENU_SHA256 = hashlib.sha256(json.dumps(EXPECTED_CHOICES, sort_keys=True,
                                      separators=(",", ":")).encode()).hexdigest()

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
    # Coefficients are constant, m, z, v, auxiliary color.  The last
    # coordinate is eliminated with a globally valid affine endpoint.
    a = [F(0)] * 5
    a[0 if index is None else index] = F(value)
    return tuple(a)


def add(*args):
    return tuple(sum(a[i] for a in args) for i in range(5))


def mul(c, a):
    return tuple(c * x for x in a)


def sub(a, b):
    return add(a, mul(-1, b))


def at(a, point):
    return a[0] + sum(a[i + 1] * x for i, x in enumerate(point))


ZERO, ONE = aff(0), aff(1)
M, Z, V, AUX = (aff(1, i) for i in range(1, 5))


def corners(box):
    return list(product(*((lo,) if lo == hi else (lo, hi) for lo, hi in box)))


class Family:
    def __init__(self, rho: F, gamma: F | None, tau: F, target: F,
                 branch: str, gamma2: F = F(1, 2)):
        self.rho, self.gamma, self.gamma2 = rho, gamma, gamma2
        self.tau, self.target, self.branch = tau, target, branch
        if not (0 < A < S < 1 and B == S - A and 0 < T < 1
                and rho > 1 and 0 < tau < 1 and target > 0 and 0 < gamma2 < 1):
            raise ValueError("invalid fixed types or contact parameters")
        beta_top = A + rho * (S - A)
        if beta_top >= min(T, 1 - T, 1 - S):
            raise ValueError("the outer and trace entropy domains require a smaller beta")
        if branch != "direct" and (gamma is None or not 0 < gamma < 1):
            raise ValueError("recursive lookup fraction must lie in (0,1)")
        self.beta = add(aff(A * (1 - rho)), mul(rho, M))
        self.c = mul(gamma or F(0), self.beta)
        self.c2 = mul(gamma2, self.c)
        self.cut = mul(1 - gamma2, self.c)
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

    def initial(self):
        top = at(self.beta, (S, F(0), F(0)))
        vmax = at(self.c2, (S, F(0), F(0))) if self.branch == "recursive" else F(0)
        return ((A, S), (A, top), (F(0), vmax))

    def tighten(self, original):
        """Necessary affine propagation.  No floating-point pruning."""
        box = [list(pair) for pair in original]
        for _ in range(3):
            changed = False
            for constraint in self.constraints:
                terms = [max(constraint[i + 1] * box[i][0],
                             constraint[i + 1] * box[i][1]) for i in range(3)]
                maximum = constraint[0] + sum(terms)
                if maximum < 0:
                    return None
                for i in range(3):
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
        return tuple(tuple(pair) for pair in box)

    def center(self, box):
        m, z, v = (float((lo + hi) / 2) for lo, hi in box)
        beta = float(A) + float(self.rho) * (m - float(A))
        c = float(self.gamma or 0) * beta
        c2, cut = float(self.gamma2) * c, float(1 - self.gamma2) * c
        if self.branch == "push":
            z = min(beta, max(z, m, beta - cut))
            v = 0.0
        elif self.branch == "recursive":
            # A globally feasible center is sufficient to propose tangents;
            # it need not be inside the current relaxed box.
            vlo, vhi = max(0.0, c2 - m), min(c2, beta - m - cut)
            v = max(vlo, min(vhi, v))
            z = min(beta, max(z, m, beta - cut - v))
        else:
            z = min(beta, max(z, m))
        return m, z, v

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
        m, z, v = center = self.center(box)
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
                     first2=probability(q, m))
            lo, hi = max(q, c2 - q1, 0.0), min(d1, c2)
            def derivative(w):
                return (tau * (log(d1 - w) + log(c2 - w) - log(w)
                        - log(q1 - c2 + w))
                        + (1 - tau) * (log(c2 - w) - log(w - q)))
            w = self.stationary(lo, hi, derivative)
            p.update(inner1=probability(w, d1),
                     inner2=probability(c2 - w, q1),
                     inner3=probability(w - q, v))
            wzero = max(lo, min(hi, q + v / 2))
            p["innerzero"] = probability(wzero - q, v)
            if (beta >= float(S) or
                    at(self.beta, (box[0][0], F(0), F(0))) >= S):
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

    def closed_delta(self, box):
        vertices = corners(box)
        bounds = lambda f: (min(at(f, v) for v in vertices),
                            max(at(f, v) for v in vertices))
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
        vertices = corners(box)
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
            coef = f[4]
            endpoints = upper if coef >= 0 else lower
            # Each candidate is globally one-sided.  The center chooses one
            # affine expression, which remains fixed throughout this box.
            endpoint = (min(endpoints, key=lambda e: float(at(e, center)))
                        if coef >= 0 else
                        max(endpoints, key=lambda e: float(at(e, center))))
            base = tuple(f[i] if i != 4 else number(F(0)) for i in range(5))
            return add(base, mul(coef, convert(endpoint)))

        outer = add(gib("outer1", aff(T), Z),
                    gib("outer2", aff(1 - T), self.q1))
        bp = gib("B", aff(B), self.d)
        outer_values = [tau * max(0, at(outer, v) - h)
                        for v, h in zip(points, h0)]
        bvalues = [at(bp, v) for v in points]
        if self.branch == "direct":
            direct = gib("direct", sub(self.beta, M), sub(Z, M))
            (m0, m1), (z0, z1), _ = box
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
        raw = add(mul(tau, gib("inner1", self.d1, AUX)),
                  mul(tau, gib("inner2", self.q1, sub(self.c2, AUX))),
                  mul(rtau, gib("inner3", V, sub(AUX, self.q))))
        raw = eliminate(raw, [self.q, sub(self.c2, self.q1), ZERO],
                        [self.d1, self.c2])
        zero = eliminate(mul(rtau, gib("innerzero", V, AUX)),
                         [ZERO, sub(V, self.q1)], [V, sub(self.w1, self.q1)])
        common = [o + max(at(raw, v) - tau * h, at(zero, v))
                  for o, h, v in zip(outer_values, h2, points)]
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
    rho, gamma, gamma2, tau, target, branch, max_nodes = job
    family = Family(F(rho), None if gamma == "direct" else F(gamma),
                    F(tau), F(target), branch, F(1, 2) if gamma2 == "direct" else F(gamma2))
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
        widths = [(box[i][1] - box[i][0]) * weight
                  for i, weight in enumerate((3, 1, 2))]
        axis = max(range(3), key=lambda i: (widths[i], -i))
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
    return dict(rho=rho, gamma=gamma, gamma2=gamma2, tau=tau, target=target, branch=branch,
                leaves=leaves, empty=empty, nodes=nodes, depth=depthmax,
                maximum=str(largest), minimum_margin=None if margin is None else str(margin),
                methods=dict(methods),
                seconds=round(time.monotonic() - started, 3))


def check_receipt(path: Path):
    """Check provenance and coverage metadata, without rerunning every leaf.

    This is the inexpensive CI binding check for a committed full-run result.
    A receipt itself is not an independently replayed mathematical proof.
    """
    receipt = json.loads(path.read_text())
    def require(condition, message):
        if not condition:
            raise ValueError("invalid contact receipt: " + message)
    require(receipt.get("receipt_schema") == 2, "unsupported schema")
    require(receipt.get("status") == "PASS", "full run did not pass")
    require(receipt.get("complete_X02_contact_menu") is True, "incomplete menu")
    require(receipt.get("checker_sha256") == CHECKER_SHA256, "checker bytes changed")
    require(receipt.get("menu_sha256") == MENU_SHA256, "contact menu changed")
    require(receipt.get("expected_choices") == EXPECTED_CHOICES, "wrong expected choices")
    require(receipt.get("expected_branch_count") == len(EXPECTED_CHOICES) == 62,
            "wrong expected branch count")
    results = receipt.get("results", [])
    require(len(results) == receipt.get("branches") == 62, "wrong covered branch count")
    fields = ("rho", "gamma", "gamma2", "tau", "target", "branch")
    choices = lambda records: sorted(tuple(row.get(key) for key in fields) for row in records)
    require(choices(results) == choices(EXPECTED_CHOICES), "missing or repeated branch")
    total_leaves = 0
    for row in results:
        leaves, empty, nodes = (row.get(key) for key in ("leaves", "empty", "nodes"))
        require(all(type(x) is int and x >= 0 for x in (leaves, empty, nodes)),
                "invalid subdivision counts")
        require(nodes == 2 * (leaves + empty) - 1, "incomplete binary subdivision")
        methods = row.get("methods", {})
        allowed = ({"old", "closed", "continuous"} if row["branch"] == "recursive"
                   else {row["branch"]})
        require(set(methods) <= allowed and
                all(type(x) is int and x > 0 for x in methods.values()) and
                sum(methods.values()) == leaves, "invalid accepted-leaf counts")
        family = Family(F(row["rho"]), None if row["gamma"] == "direct" else F(row["gamma"]),
                        F(row["tau"]), F(row["target"]), row["branch"],
                        F(1, 2) if row["gamma2"] == "direct" else F(row["gamma2"]))
        maximum = F(row["maximum"])
        if leaves:
            margin = F(row["minimum_margin"])
            require(0 <= maximum <= family.target and margin >= 0 and
                    maximum + margin == family.target, "incorrect rational acceptance margin")
            require(family.tighten(family.initial()) is not None, "nonempty receipt for empty domain")
        else:
            require(empty > 0 and maximum == 0 and row["minimum_margin"] is None,
                    "invalid empty-domain record")
            require(family.tighten(family.initial()) is None, "unjustified empty domain")
        total_leaves += leaves
    require(total_leaves == receipt.get("leaves"), "wrong total leaf count")
    print(json.dumps(dict(status="receipt binding PASS", checker_sha256=CHECKER_SHA256,
                          menu_sha256=MENU_SHA256, branches=62, leaves=total_leaves,
                          scope="provenance and coverage metadata; full replay uses --all"),
                     sort_keys=True))


def main():
    if not __debug__:
        raise SystemExit('Run mathematical verification without python -O.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="verify all 62 branches")
    parser.add_argument("--rho", help="select an exact family parameter")
    parser.add_argument("--tau", help="select one exact contact")
    parser.add_argument("--branch", choices=("push", "recursive", "direct"))
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--max-nodes", type=int, default=5_000_000)
    parser.add_argument("--output", type=Path, help="write complete results only after success")
    parser.add_argument("--check-receipt", type=Path,
                        help="check the full receipt's code/menu binding and coverage metadata")
    args = parser.parse_args()
    if args.jobs < 1 or args.max_nodes < 1:
        parser.error("--jobs and --max-nodes must be positive")
    if args.check_receipt:
        if args.all or args.rho or args.tau or args.branch or args.output:
            parser.error("--check-receipt is separate from a new verification run")
        check_receipt(args.check_receipt)
        return
    if not args.all and not args.rho and not args.branch:
        parser.error("select --all, --rho, or --branch")
    jobs = []
    for rho, gamma, gamma2, points in CONTACTS:
        if args.rho and F(rho) != F(args.rho):
            continue
        for tau, target in points:
            if args.tau and F(tau) != F(args.tau):
                continue
            for branch in (["direct"] if gamma == "direct" else ["push", "recursive"]):
                if not args.branch or branch == args.branch:
                    jobs.append((rho, gamma, gamma2, tau, target, branch, args.max_nodes))
    if not jobs:
        parser.error("selection contains no contacts")
    results = []
    if args.jobs == 1:
        iterator = map(verify_contact, jobs)
        for result in iterator:
            results.append(result)
            print(json.dumps(result, sort_keys=True), flush=True)
    else:
        with ProcessPoolExecutor(max_workers=args.jobs) as pool:
            futures = [pool.submit(verify_contact, job) for job in jobs]
            for future in as_completed(futures):
                result = future.result()
                results.append(result)
                print(json.dumps(result, sort_keys=True), flush=True)
    if hashlib.sha256(Path(__file__).read_bytes()).hexdigest() != CHECKER_SHA256:
        raise RuntimeError("checker bytes changed during the run; no receipt will be written")
    complete = (len(results) == len(EXPECTED_CHOICES) == 62 and args.all and not args.rho
                and not args.tau and not args.branch)
    summary = dict(receipt_schema=2, status="PASS", complete_X02_contact_menu=complete,
                   checker_sha256=CHECKER_SHA256, menu_sha256=MENU_SHA256,
                   expected_branch_count=len(EXPECTED_CHOICES), expected_choices=EXPECTED_CHOICES,
                   branches=len(results), leaves=sum(r["leaves"] for r in results),
                   arithmetic="exact rationals; integer interval atanh logarithms",
                   scope="continuous profile inequalities conditional on the analytic circuit and trace lemmas",
                   results=sorted(results, key=lambda r: (F(r["rho"]), r["gamma"],
                                                         F(r["tau"]), r["branch"])))
    if args.output:
        args.output.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({k: v for k, v in summary.items()
                      if k not in ("results", "expected_choices")}, sort_keys=True))


if __name__ == "__main__":
    main()
