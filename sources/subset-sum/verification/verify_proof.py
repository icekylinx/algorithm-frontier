"""Self-contained exact finite numerical certificate for proof.md.

This proves the finite profile and cost inequalities only. It does not prove
circuit construction, rebalancing, or the Subset Sum reduction.

The landscape checker functions below adapt Swapnil Jain's Apache-2.0
lean/gen_stage4_cells.py (pinned source SHA256
745f94ef74c8b9a1eecb7644620110464fbbeed6a2750a45586ab247210c4b1d).
Copyright 2026 Swapnil Jain. Licensed under the Apache License, Version 2.0.
This adaptation modifies tangent selection to use exact rational arithmetic.
The repository retains the original LICENSE and NOTICE.
No archived hash or historical receipt is used to establish an inequality.
"""
import math
import argparse
import hashlib
import json
from pathlib import Path
import time
from fractions import Fraction as F

if not __debug__:
    raise RuntimeError('Run with assertions enabled.')

"""Small exact rational interval bounds used by the research certificates.

No floating-point logarithm is used in any accepted inequality.  The only
analytic ingredient is the geometric remainder of the atanh logarithm series.
All outward rounding is performed by integer division.
"""
from fractions import Fraction as Q
from functools import lru_cache

BITS = 70
TERMS = 32
SCALE = 1 << BITS


def down(x):
    x = Q(x)
    return Q(x.numerator * SCALE // x.denominator, SCALE)


def up(x):
    x = Q(x)
    return Q(-((-x.numerator * SCALE) // x.denominator), SCALE)


def atanh_log_bounds(x):
    """Bounds ln(x) for rational 1 <= x <= 2, including both endpoints."""
    x = Q(x)
    assert 1 <= x <= 2
    t = (x - 1) / (x + 1)
    t2, power, total = t * t, t, Q(0)
    for j in range(TERMS):
        total += 2 * power / (2 * j + 1)
        power *= t2
    tail = 2 * power / ((2 * TERMS + 1) * (1 - t2))
    return total, total + tail


LN2_LO, LN2_HI = atanh_log_bounds(Q(2))


@lru_cache(maxsize=200000)
def log2_bounds(x):
    x = Q(x)
    assert x > 0
    k = x.numerator.bit_length() - x.denominator.bit_length()
    unit = Q(2) ** k
    while x < unit:
        k -= 1
        unit /= 2
    while x >= 2 * unit:
        k += 1
        unit *= 2
    lo, hi = atanh_log_bounds(x / unit)
    return down(k + lo / LN2_HI), up(k + hi / LN2_LO)


@lru_cache(maxsize=200000)
def entropy_bounds(x):
    x = Q(x)
    assert 0 <= x <= 1
    if x == 0 or x == 1:
        return Q(0), Q(0)
    a, b = log2_bounds(1 / x)
    c, d = log2_bounds(1 / (1 - x))
    return down(x * a + (1 - x) * c), up(x * b + (1 - x) * d)


def entropy_interval(lo, hi):
    lo, hi = Q(lo), Q(hi)
    assert 0 <= lo <= hi <= 1
    a, b = entropy_bounds(lo)
    c, d = entropy_bounds(hi)
    return min(a, c), Q(1) if lo <= Q(1, 2) <= hi else max(b, d)


class I:
    """Closed intervals with exact rational endpoints."""
    def __init__(self, lo, hi=None):
        if isinstance(lo, I):
            self.lo, self.hi = lo.lo, lo.hi
        else:
            self.lo, self.hi = Q(lo), Q(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        o = I(other)
        return I(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -I(other)

    def __rsub__(self, other):
        return I(other) + -self

    def __mul__(self, other):
        o = I(other)
        vals = (self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi)
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = I(other)
        assert o.lo > 0 or o.hi < 0
        return self * I(1/o.hi, 1/o.lo)

    def __repr__(self):
        return f"I({self.lo!r}, {self.hi!r})"


def h(x):
    x = I(x)
    return I(*entropy_interval(x.lo, x.hi))


def log2(x):
    x = I(x)
    return I(log2_bounds(x.lo)[0], log2_bounds(x.hi)[1])



# All quoted logarithm constants are derived by the proved series above.
L2lo, L2hi = LN2_LO, LN2_HI
NT = 26
PD = 10**12
LD = 10**14
LOGC = {}
HLC = {}

def p2(k):
    return F(2) ** k if k >= 0 else F(1) / F(2) ** (-k)

def lsum(t, n):
    s, p = F(0), F(1)
    for i in range(n):
        p *= t
        s += p / (i + 1)
    return s

def lrem(t, n):
    return abs(t) ** (n + 1) / (1 - abs(t))

def kfor(x):
    k = 0
    while x / p2(k) > F(4, 3):
        k += 1
    while x / p2(k) < F(2, 3):
        k -= 1
    return k

def log_bounds(x):
    """(k, lower, upper) of the kernel's series bound on ln x (exact; cached)."""
    if x not in LOGC:
        k = kfor(x)
        t = 1 - x / p2(k)
        S, R = lsum(t, NT), lrem(t, NT)
        LOGC[x] = (k, -S - R + min(k * L2lo, k * L2hi), -S + R + max(k * L2lo, k * L2hi))
    return LOGC[x]

def dn(x):
    return F(math.floor(x * LD), LD)

def up14(x):
    return F(math.ceil(x * LD), LD)

def logGe(x, k, l):
    if not (x > 0 and abs(1 - x / p2(k)) < 1):
        return False
    t = 1 - x / p2(k)
    return l <= -lsum(t, NT) - lrem(t, NT) + min(k * L2lo, k * L2hi)

def logLe(x, k, u):
    if not (x > 0 and abs(1 - x / p2(k)) < 1):
        return False
    t = 1 - x / p2(k)
    return -lsum(t, NT) + lrem(t, NT) + max(k * L2lo, k * L2hi) <= u

def gib_ok(g):
    p, k1, k2, l1, l2, cp, cq = g
    return (0 < p < 1 and logGe(p, k1, l1) and logGe(1 - p, k2, l2) and cp >= 0 and cq >= 0
            and -l1 <= cp * L2lo and -l2 <= cq * L2lo)

def hlo_ok(c, x, e):
    kc, kx, ky, lc, ux, uy, lo = e
    if x == 0:
        return lo <= 0
    return (0 < x < c and logGe(c, kc, lc) and logLe(x, kx, ux) and logLe(c - x, ky, uy) and lo >= 0
            and lo * L2hi <= c * lc - x * ux - (c - x) * uy)

def bq(P, m):
    return P["k"] + P["rho"] * (m - P["k"])

def Uq(P, g, e0, e1, m0, m1, m, d):
    gA, gB, gC, gD = g
    k, tau, b = P["k"], P["tau"], bq(P, m)
    L = ((d * gA[5] + (F(1, 2) - d) * gA[6]) + ((b - d) * gB[5] + (F(1, 2) - (b - d)) * gB[6])
         - (e0 + (e1 - e0) * (m - m0) / (m1 - m0)))
    R = ((m - k) * gC[5] + (k - (m - k)) * gC[6]) + ((d - m) * gD[5] + ((b - m) - (d - m)) * gD[6])
    return tau * L + (1 - tau) * R, (1 - tau) * R

def leaf_ok(P, m0, m1, d0, d1, g, h0, h1):
    k, rho, T = P["k"], P["rho"], P["T"]
    if not (k <= m0 < m1 <= 2 * k):
        return False
    if not all(gib_ok(x) for x in g):
        return False
    if not (hlo_ok(1 - m0, (rho - 1) * (m0 - k), h0) and hlo_ok(1 - m1, (rho - 1) * (m1 - k), h1)):
        return False
    for m in (m0, m1):
        for d in (d0, d1):
            u, r = Uq(P, g, h0[6], h1[6], m0, m1, m, d)
            if u > T or r > T:
                return False
    return True

def prob_ok(P):
    return P["k"] > 0 and P["rho"] >= 1 and 0 <= P["tau"] <= 1 and bq(P, 2 * P["k"]) <= F(1, 2)

def chk(P, t, m0, m1, d0, d1):
    a, c = max(d0, m0), min(d1, bq(P, m1))
    if t[0] == "none":
        return c < a
    if t[0] == "leaf":
        return leaf_ok(P, m0, m1, a, c, t[1], t[2], t[3])
    if t[0] == "sm":
        mm = (m0 + m1) / 2
        return chk(P, t[1], m0, mm, a, c) and chk(P, t[2], mm, m1, a, c)
    dm = (a + c) / 2
    return chk(P, t[1], m0, m1, a, dm) and chk(P, t[2], m0, m1, dm, c)

def gib_at(pf):
    """Gibbs data at the tangent point nearest the exact rational pf in (0, 1)."""
    p = F(min(max(round(pf * PD), 1), PD - 1), PD)
    k1, lo1, _ = log_bounds(p)
    k2, lo2, _ = log_bounds(1 - p)
    l1, l2 = dn(lo1), dn(lo2)
    cp, cq = up14(-l1 / L2lo), up14(-l2 / L2lo)
    g = (p, k1, k2, l1, l2, max(cp, F(0)), max(cq, F(0)))
    assert gib_ok(g)
    return g

def hlo_at(P, m):
    c, x = 1 - m, (P["rho"] - 1) * (m - P["k"])
    key = (c, x)
    if key not in HLC:
        if x == 0:
            HLC[key] = (0, 0, 0, F(0), F(0), F(0), F(0))
        else:
            kc, lc, _ = log_bounds(c)
            kx, _, ux = log_bounds(x)
            ky, _, uy = log_bounds(c - x)
            lc, ux, uy = dn(lc), up14(ux), up14(uy)
            lo = max(F(0), dn((c * lc - x * ux - (c - x) * uy) / L2hi))
            HLC[key] = (kc, kx, ky, lc, ux, uy, lo)
        assert hlo_ok(c, x, HLC[key]), (c, x)
    return HLC[key]

def count(t):
    if t[0] in ("none", "leaf"):
        return (t[0] == "leaf", t[0] == "none", 0)
    a, b = count(t[1]), count(t[2])
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2] + 1)


def clampq(x):
    return min(max(x, F(1, 10**9)), 1-F(1, 10**9))


def build(P, m0, m1, d0, d1, depth=0):
    a, c = max(d0, m0), min(d1, bq(P, m1))
    if c < a:
        return ('none',)
    k, rho = P['k'], P['rho']
    mc, dc = (m0+m1)/2, (a+c)/2
    bc = k + rho*(mc-k)
    dc = min(max(dc, mc), bc)
    n5 = (rho-1)*(mc-k)
    g = (gib_at(clampq(2*dc)), gib_at(clampq(2*(bc-dc))),
         gib_at(clampq((mc-k)/k)),
         gib_at(clampq((dc-mc)/n5) if n5>0 else F(1,2)))
    h0, h1 = hlo_at(P, m0), hlo_at(P, m1)
    if leaf_ok(P,m0,m1,a,c,g,h0,h1):
        return ('leaf',g,h0,h1)
    assert depth<60, 'Finite tree depth bound exceeded.'
    if (m1-m0)*3 >= c-a:
        mm = (m0+m1)/2
        return ('sm',build(P,m0,mm,a,c,depth+1),build(P,mm,m1,a,c,depth+1))
    dm = (a+c)/2
    return ('sd',build(P,m0,m1,a,dm,depth+1),build(P,m0,m1,dm,c,depth+1))


HALF = Q(1,2)
PIECE = 8_000_000_000
OVERHEAD = Q(24,10**9)
SLACK = Q(1,10**8)

class Checker:
    def __init__(self, menu, mu, claim):
        self.menu = [tuple(Q(d[k]) for k in ('s', 'l', 'r')) for d in menu]
        self.mu, self.claim = Q(mu), Q(claim)
        assert 0 < self.mu < HALF and 0 < self.claim < HALF
        self.l3 = (log2(I(3)) + 1) / 4
        overhead = (log2(I(PIECE)) + 3 + log2(1 + PIECE * I(LN2_LO, LN2_HI))
                    + 4 * log2(I(Q(PIECE, 4) + 1))) / PIECE
        assert overhead.hi < OVERHEAD
        self.overhead_upper = overhead.hi

    @lru_cache(maxsize=None)
    def balance(self, a, i, j):
        s, l, r = self.menu[i]
        t, v, u = self.menu[j]
        delta = a / 2 * (I(s-t+r+v-l-u) + h(s) - h(t))
        w = -self.mu * delta / (2 * (1-self.mu))
        mid = (w.lo + w.hi) / 2
        den = 10**12
        return Q((2*mid.numerator*den+mid.denominator)//(2*mid.denominator), den)

    def terms(self, lo, hi, a, i, j, w):
        s, l, r = self.menu[i]
        t, v, u = self.menu[j]
        assert (1-self.mu)*(HALF-abs(w)) >= self.mu
        k = I(lo, hi)
        residual = (2*k-a*(s+1-t))/(2*(1-a))
        assert Q(1, 1000) < residual.lo <= residual.hi < Q(999, 1000)
        residual_piece = Q(PIECE, 2)*(1-a)
        assert residual_piece.denominator == 1
        assert residual_piece*min(residual.lo, 1-residual.hi) > 2
        hk, ht = h(k), h(residual)
        common = hk-(1-a)*ht/2+(1-a)/2-1+OVERHEAD
        left = HALF+self.mu*(common+a/2*(s-h(t)+r+v))+(1-self.mu)*w
        right = HALF+self.mu*(common+a/2*(t-h(s)+l+u))-(1-self.mu)*w
        loss = hk-a/2*(h(s)+h(t))-(1-a)*ht
        p4 = self.mu*(loss+OVERHEAD+self.l3)+max(self.mu, (1-self.mu)*(HALF+abs(w))-self.mu)
        p6 = self.mu*(1+hk+loss+OVERHEAD)
        return max(left.hi, right.hi), p4.hi, p6.hi

    def cell(self, lo, hi, a, i, j, w=None):
        assert Q(2, 5) <= lo < hi <= HALF and 0 <= a < 1
        assert 0 <= i < len(self.menu) and 0 <= j < len(self.menu)
        core = PIECE*a/2
        assert core.denominator == 1
        assert all((core*self.menu[v][0]).denominator == 1 for v in (i, j))
        w = self.balance(a, i, j) if w is None else w
        if a >= Q(13, 25):
            first, last = self.terms(lo, lo, a, i, j, w), self.terms(hi, hi, a, i, j, w)
            values = tuple(max(x, y) for x, y in zip(first, last))
            method = 'convex endpoints'
        else:
            values = self.terms(lo, hi, a, i, j, w)
            method = 'natural exact interval'
        assert max(values) + a*self.mu*SLACK < self.claim
        return dict(lo=str(lo), hi=str(hi), alpha=str(a), i=i, j=j, w=str(w),
                    method=method, bounds=list(map(str, values)))

    def auxiliary(self):
        tail_entropy = h(Q(2, 5))
        values = dict(
            tail_P3=(HALF-self.mu*(1-tail_entropy)/2+self.mu*OVERHEAD).hi,
            tail_P4=(self.mu*(OVERHEAD+self.l3)+max(self.mu, (1-self.mu)/2-self.mu)).hi,
            tail_P6=(self.mu*(1+tail_entropy+OVERHEAD)).hi,
            P1=self.mu, P5=2*self.mu, Kenum=self.mu*(2+OVERHEAD))
        assert max(values.values()) < self.claim
        return {k: str(v) for k, v in values.items()}

MENU = [
    ('2/25', '240685651/1000000000', '34085267/500000000', ['47/20', '5/2', '14/5'], ['148409/500000', '7699/15625', '255379/500000', '780429/1000000']),
    ('19/200', '13021319/50000000', '16691369/200000000', ['12/5', '51/20', '14/5'], ['60343/200000', '495413/1000000', '511053/1000000', '94997/125000']),
    ('13/125', '67888743/250000000', '18349349/200000000', ['12/5', '51/20', '11/4'], ['151519/500000', '247273/500000', '254107/500000', '149527/200000']),
    ('21/200', '272724777/1000000000', '46337503/500000000', ['12/5', '51/20', '11/4'], ['909533/3000000', '593341/1200000', '508107/1000000', '1492829/2000000']),
    ('53/500', '136947291/500000000', '93603267/1000000000', ['12/5', '51/20', '11/4'], ['14218/46875', '1483067/3000000', '127/250', '372597/500000']),
    ('107/1000', '275044387/1000000000', '11813941/125000000', ['12/5', '51/20', '11/4'], ['303457/1000000', '988521/2000000', '507893/1000000', '1487947/2000000']),
    ('27/250', '17262137/62500000', '95419789/1000000000', ['12/5', '51/20', '11/4'], ['91079/300000', '23164/46875', '253893/500000', '742753/1000000']),
    ('27/250', '55259053/200000000', '95282789/1000000000', ['12/5', '101/40', '51/20', '109/40', '61/20'], ['38/125', '493/1000', '499/1000', '507/1000', '727/1000', '743/1000']),
    ('109/1000', '277318079/1000000000', '96298811/1000000000', ['12/5', '101/40', '51/20', '53/20', '61/20'], ['38/125', '493/1000', '499/1000', '63/125', '127/200', '371/500']),
    ('11/100', '139182629/500000000', '97277969/1000000000', ['97/40', '101/40', '51/20', '21/8', '61/20'], ['61/200', '247/500', '499/1000', '503/1000', '601/1000', '741/1000']),
    ('11/100', '139226901/500000000', '97196311/1000000000', ['12/5', '51/20', '11/4'], ['75969/250000', '19759/40000', '126893/250000', '92539/125000']),
    ('111/1000', '27949211/100000000', '24541277/250000000', ['97/40', '101/40', '51/20', '21/8', '61/20'], ['61/200', '247/500', '499/1000', '503/1000', '301/500', '739/1000']),
    ('111/1000', '279562383/1000000000', '98101829/1000000000', ['12/5', '51/20', '11/4'], ['76003/250000', '49387/100000', '101491/200000', '92389/125000']),
    ('14/125', '35074469/125000000', '49531559/500000000', ['97/40', '101/40', '51/20', '21/8', '121/40'], ['61/200', '247/500', '499/1000', '503/1000', '301/500', '369/500']),
    ('14/125', '392906687/1400000000', '138631149/1400000000', ['12/5', '51/20', '11/4'], ['1064509/3500000', '3456431/7000000', '1775719/3500000', '645691/875000']),
    ('113/1000', '5633767/20000000', '12494999/125000000', ['97/40', '101/40', '51/20', '21/8', '121/40'], ['61/200', '247/500', '499/1000', '503/1000', '301/500', '737/1000']),
    ('113/1000', '1972130189/7000000000', '699598687/7000000000', ['12/5', '51/20', '11/4'], ['66561/218750', '863943/1750000', '3550691/7000000', '644659/875000']),
    ('57/500', '56554007/200000000', '10085571/100000000', ['97/40', '101/40', '51/20', '21/8', '121/40'], ['61/200', '247/500', '249/500', '503/1000', '603/1000', '92/125']),
    ('57/500', '1979586943/7000000000', '705901629/7000000000', ['12/5', '51/20', '11/4'], ['1065443/3500000', '3455113/7000000', '443743/875000', '643627/875000']),
    ('23/200', '70960233/250000000', '50875127/500000000', ['97/40', '101/40', '51/20', '21/8', '121/40'], ['61/200', '247/500', '249/500', '503/1000', '603/1000', '147/200']),
    ('23/200', '1987043697/7000000000', '712204571/7000000000', ['12/5', '51/20', '11/4'], ['106591/350000', '1727227/3500000', '3549197/7000000', '128519/175000']),
    ('29/250', '142450583/500000000', '20528721/200000000', ['97/40', '101/40', '51/20', '21/8', '121/40'], ['61/200', '247/500', '249/500', '503/1000', '603/1000', '733/1000']),
    ('117/1000', '14297543/50000000', '51767873/500000000', ['97/40', '101/40', '51/20', '21/8', '121/40'], ['153/500', '247/500', '249/500', '503/1000', '603/1000', '183/250']),
    ('117/1000', '400363441/1400000000', '144934091/1400000000', ['12/5', '51/20', '11/4'], ['266711/875000', '215821/437500', '3547703/7000000', '640531/875000']),
    ('59/500', '286990133/1000000000', '104426659/1000000000', ['97/40', '101/40', '51/20', '53/20', '121/40'], ['153/500', '247/500', '249/500', '503/1000', '159/250', '731/1000']),
    ('59/500', '287019137/1000000000', '104404771/1000000000', ['12/5', '51/20', '11/4'], ['152473/500000', '493211/1000000', '126677/250000', '91357/125000']),
    ('119/1000', '403246723/1400000000', '368603511/3500000000', ['12/5', '51/20', '11/4'], ['152537/500000', '1725909/3500000', '443281/875000', '72971/100000']),
    ('3/25', '2023333271/7000000000', '743580647/7000000000', ['12/5', '51/20', '11/4'], ['152601/500000', '3451159/7000000', '177277/350000', '182141/250000']),
    ('121/1000', '2030292927/7000000000', '1464481/13671875', ['12/5', '51/20', '11/4'], ['30533/100000', '6901/14000', '55388/109375', '363709/500000']),
    ('61/500', '2037252583/7000000000', '756047897/7000000000', ['12/5', '51/20', '11/4'], ['152729/500000', '3449841/7000000', '886031/1750000', '11348/15625']),
    ('123/1000', '2044212239/7000000000', '381140761/3500000000', ['12/5', '51/20', '11/4'], ['152793/500000', '1724591/3500000', '442927/875000', '362563/500000']),
    ('31/250', '410206379/1400000000', '768375147/7000000000', ['12/5', '51/20', '11/4'], ['152857/500000', '3448523/7000000', '885677/1750000', '36199/50000']),
    ('1/8', '293978793/1000000000', '27659599/250000000', ['12/5', '51/20', '11/4'], ['152921/500000', '61569/125000', '253/500', '361417/500000']),
    ('29/200', '772347/2500000', '130510881/1000000000', ['49/20', '13/5', '14/5'], ['310451/1000000', '494561/1000000', '31717/62500', '701931/1000000']),
]

CELLS = [
    ('2/5', '33/80', '335589/2000000', 0, 33, '1339651079/500000000000'),
    ('33/80', '67/160', '1180691/4000000', 0, 33, '4713247371/1000000000000'),
    ('67/160', '17/40', '1520367/4000000', 0, 33, '1517303377/250000000000'),
    ('17/40', '9/20', '2369557/4000000', 0, 33, '189182577/20000000000'),
    ('9/20', '37/80', '423573/500000', 0, 33, '13527023269/1000000000000'),
    ('37/80', '15/32', '1941963/2000000', 0, 33, '15504398703/1000000000000'),
    ('15/32', '19/40', '3765287/4000000', 0, 33, '187884987/12500000000'),
    ('19/40', '77/160', '1812199/2000000', 0, 27, '8932659491/1000000000000'),
    ('77/160', '309/640', '3969951/4000000', 7, 33, '8913675497/1000000000000'),
    ('309/640', '31/64', '1983113/2000000', 11, 33, '8172735847/1000000000000'),
    ('31/64', '39/80', '3817741/4000000', 1, 29, '3091317159/500000000000'),
    ('39/80', '1249/2560', '1908479/2000000', 1, 29, '618136629/100000000000'),
    ('1249/2560', '125/256', '3919399/4000000', 2, 32, '4894281033/1000000000000'),
    ('125/256', '313/640', '3952797/4000000', 2, 32, '2467993101/500000000000'),
    ('313/640', '157/320', '1973753/2000000', 2, 31, '2349639543/500000000000'),
    ('157/320', '629/1280', '3971841/4000000', 4, 31, '4247773227/1000000000000'),
    ('629/1280', '63/128', '3988387/4000000', 7, 31, '3801725397/1000000000000'),
    ('63/128', '631/1280', '1980327/2000000', 5, 29, '1766727489/500000000000'),
    ('631/1280', '79/160', '3961023/4000000', 7, 28, '153899793/50000000000'),
    ('79/160', '253/512', '3973101/4000000', 8, 28, '1417860517/500000000000'),
    ('253/512', '633/1280', '199257/200000', 9, 28, '1298327153/500000000000'),
    ('633/1280', '1267/2560', '3987049/4000000', 11, 29, '2596716261/1000000000000'),
    ('1267/2560', '317/640', '794681/800000', 9, 27, '588511681/250000000000'),
    ('317/640', '1269/2560', '3985517/4000000', 11, 27, '1062606447/500000000000'),
    ('1269/2560', '127/256', '3973661/4000000', 11, 26, '941530797/500000000000'),
    ('127/256', '2541/5120', '498631/500000', 13, 27, '236207181/125000000000'),
    ('2541/5120', '1271/2560', '3985683/4000000', 13, 26, '206440081/125000000000'),
    ('1271/2560', '2543/5120', '3985687/4000000', 13, 26, '825761153/500000000000'),
    ('2543/5120', '159/320', '1993621/2000000', 15, 26, '1415123873/1000000000000'),
    ('159/320', '509/1024', '496731/500000', 13, 24, '176636801/125000000000'),
    ('509/1024', '1273/2560', '1995193/2000000', 15, 26, '1416239719/1000000000000'),
    ('1273/2560', '637/1280', '3985861/4000000', 15, 24, '590202773/500000000000'),
    ('637/1280', '5097/10240', '1992857/2000000', 15, 24, '295090503/250000000000'),
    ('5097/10240', '2549/5120', '1994349/2000000', 17, 24, '472203479/500000000000'),
    ('2549/5120', '255/512', '3997091/4000000', 17, 24, '37855767/40000000000'),
    ('255/512', '2551/5120', '1995863/2000000', 17, 24, '9451239/10000000000'),
    ('2551/5120', '2041/4096', '3985809/4000000', 17, 22, '708238343/1000000000000'),
    ('2041/4096', '5103/10240', '31887/32000', 17, 22, '70825007/100000000000'),
    ('5103/10240', '319/640', '498243/500000', 17, 22, '708262331/1000000000000'),
    ('319/640', '2553/5120', '159439/160000', 17, 22, '708267839/1000000000000'),
    ('2553/5120', '5107/10240', '797173/800000', 17, 22, '708248293/1000000000000'),
    ('5107/10240', '2043/4096', '398541/400000', 17, 22, '177041861/250000000000'),
    ('2043/4096', '1277/2560', '1994377/2000000', 19, 22, '59026523/125000000000'),
    ('1277/2560', '511/1024', '998937/1000000', 19, 22, '18921607/40000000000'),
    ('511/1024', '5111/10240', '3995861/4000000', 19, 22, '29565847/62500000000'),
    ('5111/10240', '639/1280', '3990269/4000000', 19, 22, '236195769/500000000000'),
    ('639/1280', '20449/40960', '3986773/4000000', 19, 22, '471977661/1000000000000'),
    ('20449/40960', '2045/4096', '996461/1000000', 19, 21, '14755139/62500000000'),
    ('2045/4096', '5113/10240', '1992949/2000000', 19, 21, '118042711/500000000000'),
    ('5113/10240', '2557/5120', '199299/200000', 19, 21, '236090279/1000000000000'),
    ('2557/5120', '1279/2560', '3986039/4000000', 19, 21, '118046887/500000000000'),
    ('1279/2560', '5117/10240', '1992977/2000000', 19, 21, '236088739/1000000000000'),
    ('5117/10240', '20469/40960', '3985877/4000000', 19, 21, '236084179/1000000000000'),
    ('20469/40960', '40939/81920', '79717/80000', 19, 21, '236082579/1000000000000'),
    ('40939/81920', '2047/4096', '3985699/4000000', 19, 21, '59018409/250000000000'),
    ('2047/4096', '81881/163840', '159407/160000', 19, 21, '236042599/1000000000000'),
    ('81881/163840', '40941/81920', '3986539/4000000', 21, 21, '0'),
    ('40941/81920', '20471/40960', '498383/500000', 21, 21, '0'),
    ('20471/40960', '2559/5120', '249257/250000', 21, 21, '0'),
    ('2559/5120', '5119/10240', '3991609/4000000', 21, 21, '0'),
    ('5119/10240', '1/2', '3997203/4000000', 21, 21, '0'),
]


def verify_family(job):
    index, row = job
    LOGC.clear(); HLC.clear()
    s,l,r = map(Q,row[:3]); rhos,bps = [list(map(Q,x)) for x in row[3:]]
    assert 0<s<HALF and l>=0 and r>=0
    assert len(bps)==len(rhos)+1 and 0<bps[0]<bps[-1]<1
    assert all(x<y for x,y in zip(bps,bps[1:]))
    assert all(rho>1 and s*rho<HALF for rho in rhos)
    line = lambda tau: r+(l-r)*tau
    assert bps[0]*entropy_bounds(s)[1] <= line(bps[0])
    assert (1-bps[-1])*(1-s) <= line(bps[-1])
    leaves = 0
    contacts = []
    for j,rho in enumerate(rhos):
        for tau in bps[j:j+2]:
            P = dict(k=s/2,rho=rho,tau=tau,T=line(tau))
            assert prob_ok(P)
            box = (s/2,s,s/2,bq(P,s))
            tree = build(P,*box)
            assert chk(P,tree,*box)
            nl,ne,ni=count(tree)
            leaves += nl
            contacts.append(dict(rho=str(rho),tau=str(tau),target=str(line(tau)),
                                 leaves=nl,empty_leaves=ne,internal_nodes=ni))
    return dict(index=index,s=str(s),leaves=leaves,contacts=contacts)


def verify_costs():
    menu = [dict(zip(('s','l','r'),row[:3])) for row in MENU]
    C = Checker(menu,Q(1607,8000),Q(4985829,10000000))
    auxiliary = C.auxiliary()
    last = Q(2,5); maximum = max(map(Q,auxiliary.values()))
    minimum_residual = Q(PIECE)
    for lo,hi,a,i,j,w in CELLS:
        lo,hi,a,w = map(Q,(lo,hi,a,w))
        assert lo==last
        fresh=C.cell(lo,hi,a,i,j,w)
        s,t=Q(MENU[i][0]),Q(MENU[j][0])
        residual=I(lo,hi)
        residual=(2*residual-a*(s+1-t))/(2*(1-a))
        minimum_residual=min(minimum_residual,Q(PIECE,2)*(1-a)*min(residual.lo,1-residual.hi))
        maximum=max(maximum,max(map(Q,fresh['bounds']))+a*C.mu*SLACK)
        last=hi
    assert last==HALF
    print('Exact finite cost certificate: PASS; 61 cells; maximum =', maximum,flush=True)
    print('Exact remaining margin =', C.claim-maximum,flush=True)
    assert minimum_residual==854932
    print('Minimum residual-piece distance from either endpoint =',minimum_residual,flush=True)
    return dict(claim=str(C.claim),cells=len(CELLS),circuit_slack=str(SLACK),
                maximum_with_circuit_slack=str(maximum),remaining_margin=str(C.claim-maximum),
                minimum_residual_piece_distance=str(minimum_residual))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--costs-only',action='store_true')
    parser.add_argument('--all-menu',action='store_true')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    started=time.monotonic()
    result=verify_costs()
    complete=[]
    if not args.costs_only:
        used=set(range(len(MENU))) if args.all_menu else {c[k] for c in CELLS for k in (3,4)}
        jobs=[(i,MENU[i]) for i in sorted(used)]
        for family in map(verify_family,jobs):
            complete.append(family)
            print('Exact family',family['index'],'PASS; leaves =',family['leaves'],flush=True)
        print('All required finite profile inequalities: PASS;',len(jobs),'families;',
              round(time.monotonic()-started,3),'seconds',flush=True)
    if args.output:
        # This output is a report of this execution, never an input to acceptance.
        result.update(status='COSTS_PASS' if args.costs_only else 'PASS',
                      profiles_status='SKIPPED' if args.costs_only else 'PASS',
                      families_checked=len(complete),
                      contacts_checked=sum(len(f['contacts']) for f in complete),
                      tree_leaves=sum(f['leaves'] for f in complete),families=complete,
                      elapsed_seconds=round(time.monotonic()-started,6),
                      script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      scope=('Self-contained exact finite cost inequalities only; profiles skipped; ' if args.costs_only else
                             'Self-contained exact finite profile and cost inequalities; ')+
                            'circuit realization and Subset Sum reduction are proved separately. '
                            'This execution report is not a logical input to the proof.')
        args.output.write_text(json.dumps(result,indent=2)+'\n')
