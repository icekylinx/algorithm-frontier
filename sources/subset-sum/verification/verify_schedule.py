"""Standard-library replay, bound to completed circuit receipts and fixed slack.

The circuit and algorithm implications are proved in proof.md. This command
checks their finite numerical premises, without NumPy, floats, or an optimizer.
"""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import argparse
import hashlib
import json
import sys

if not __debug__:
    raise RuntimeError('Exact verification requires assertions; disable Python optimization (-O/PYTHONOPTIMIZE).')

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'baseline'
sys.path.insert(0, str(BASE / 'code'))
from exact_bounds import I, h, log2, LN2_LO, LN2_HI

HALF = Q(1, 2)
PIECE = 8_000_000_000
OVERHEAD = Q(24, 10**9)
SLACK = Q(1, 10**8)


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


def completed_families():
    results = BASE / 'results'
    base = json.loads((results / 'exact_circuit_families.json').read_text())
    assert base['status'] == 'PASS' and base['completed'] == base['requested']
    families = base['families'][:]
    families += [json.loads(p.read_text()) for p in sorted(results.glob('expanded_rho_s*_certified.json'))]
    checker_hash = hashlib.sha256((BASE / 'agents/derandomization/subsetsum-derand-main/lean/gen_stage4_cells.py').read_bytes()).hexdigest()
    for d in families:
        assert d['status'] == 'EXACT_RATIONAL_LANDSCAPE_PASS'
        assert d['checker_sha256'] == checker_hash
        assert len(d['contacts']) == 2*len(d['rhos'])
        assert all(c['exact_checker'] == 'PASS' for c in d['contacts'])
    return families


def replay(path):
    data = json.loads(Path(path).read_text())
    assert data['status'] == 'EXACT_ALL_LAYER_COST_CERTIFICATE_PASS'
    assert data['piece_length'] == PIECE and Q(data['lambda_used']) == OVERHEAD
    families = completed_families()
    keys = ('s', 'l', 'r', 'rhos', 'bps')
    for d in data['menu']:
        assert any(all(d[k] == f[k] for k in keys) for f in families), 'Uncertified circuit family'
    checker = Checker(data['menu'], data['mu'], data['claim'])
    assert Q(data['lambda_certified_upper']) == checker.overhead_upper
    auxiliary = checker.auxiliary()
    assert data['auxiliary'] == auxiliary
    previous = Q(2, 5)
    largest = Q(0)
    for c in data['cells']:
        lo, hi, a, w = map(Q, (c['lo'], c['hi'], c['alpha'], c['w']))
        assert lo == previous
        fresh = checker.cell(lo, hi, a, c['i'], c['j'], w)
        assert fresh == c
        largest = max(largest, max(map(Q, c['bounds']))+a*checker.mu*SLACK)
        previous = hi
    assert previous == HALF
    auxiliary_maximum = max(map(Q, auxiliary.values()))
    central_maximum = largest
    largest = max(largest, auxiliary_maximum)
    return dict(status='PASS', claim=data['claim'], cells=len(data['cells']),
                circuit_slack=str(SLACK), maximum_with_circuit_slack=str(largest),
                maximum_central_with_circuit_slack=str(central_maximum),
                maximum_auxiliary=str(auxiliary_maximum),
                remaining_margin=str(checker.claim-largest), family_receipts_matched=True,
                scope='Exact all-layer numerical replay; family receipts matched, not recomputed. Algorithmic interpretation is proved in proof.md.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = replay(args.certificate)
    text = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    print(text, end='')
