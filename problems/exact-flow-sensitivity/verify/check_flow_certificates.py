#!/usr/bin/env python3
"""Independent Boolean-support optima, cut completeness, and hostile witnesses."""
from dataclasses import replace
from fractions import Fraction
from itertools import product
from pathlib import Path
import random
import subprocess
import sys

REFERENCE = Path(__file__).resolve().parents[1] / 'reference'
sys.path.insert(0, str(REFERENCE))
from unit_flow import Arc, fixed_flow, MaximumFlowOracle
from flow_certificates import (FlowCertificate, MaximumCertificate, verify_flow,
                               verify_maximum, verify_infeasible)
from certify_flow import certify_flow, certify_maximum, balance_feasibility

COUNTS = dict(instances=0, supports=0, optimum=0, maximum=0, cut_decisions=0,
              infeasible_cuts=0, oracle_queries=0, hostile=0)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def rejects(call):
    try:
        call()
    except ValueError:
        return True
    return False


def check(n, arcs):
    COUNTS['instances'] += 1
    for failed in (None, *range(len(arcs))):
        allowed = [i for i in range(len(arcs)) if i != failed]
        records, optima = [], {}
        for bits in product((0, 1), repeat=len(allowed)):
            used = tuple(i for i, bit in zip(allowed, bits) if bit)
            balance = [0] * n
            cost = Fraction(0)
            for i in used:
                a = arcs[i]
                balance[a.tail] += 1
                balance[a.head] -= 1
                cost += a.cost
            b = tuple(balance)
            optima[b] = min(optima.get(b, cost), cost)
            records.append((used, b, cost))
        for used, b, cost in records:
            COUNTS['supports'] += 1
            if cost != optima[b]:
                require(rejects(lambda: certify_flow(n, arcs, b, used, failed)), 'accepted nonoptimum')
                continue
            certificate = certify_flow(n, arcs, b, used, failed)
            require(certificate.cost == cost and verify_flow(n, arcs, b, certificate, failed), 'optimum rejected')
            COUNTS['optimum'] += 1
            require(not verify_flow(n, arcs, b, replace(certificate, cost=cost + 1), failed), 'wrong cost')
        candidates = [(b[0], c, used) for used, b, c in records
                      if b[0] >= 0 and b[-1] == -b[0] and all(x == 0 for x in b[1:-1])]
        value = max(v for v, _, _ in candidates)
        cost = min(c for v, c, _ in candidates if v == value)
        used = next(u for v, c, u in candidates if v == value and c == cost)
        cert = certify_maximum(n, arcs, 0, n-1, used, failed)
        require(cert.value == value and cert.flow.cost == cost
                and verify_maximum(n, arcs, 0, n-1, cert, failed), 'maximum certificate')
        require(not verify_maximum(n, arcs, 0, n-1, replace(cert, value=value+1), failed), 'wrong maximum value')
        COUNTS['maximum'] += 1
        cuts = [tuple(v for v, bit in enumerate(bits) if bit) for bits in product((0, 1), repeat=n)]
        for first in product(range(-2, 3), repeat=n-1):
            b = (*first, -sum(first))
            witness = next((s for s in cuts if verify_infeasible(n, arcs, b, s, failed)), None)
            require((witness is None) == (b in optima), 'cut/feasibility mismatch')
            support, cut = balance_feasibility(n, arcs, b, failed)
            if b not in optima:
                require(support is None and verify_infeasible(n, arcs, b, cut, failed), 'constructed cut')
            else:
                require(cut is None and any(u == support and bb == b for u, bb, _ in records), 'constructed feasible flow')
            COUNTS['cut_decisions'] += 1
            COUNTS['infeasible_cuts'] += witness is not None


def integration():
    rng = random.Random(70419)
    for _ in range(70):
        n = rng.randrange(2, 6)
        arcs = [Arc(u, v, Fraction(rng.randrange(5), 3)) for u, v in
                (rng.sample(range(n), 2) for _ in range(rng.randrange(1, 10)))]
        maximum = MaximumFlowOracle(n, arcs, 0, n-1)
        for failed in (None, *range(len(arcs))):
            value, cost, used = maximum.query(failed)
            cert = certify_maximum(n, arcs, 0, n-1, used, failed)
            require(cert.value == value and cert.flow.cost == cost, 'native maximum output')
            COUNTS['oracle_queries'] += 1
        for value in range(maximum.query()[0] + 1):
            oracle = fixed_flow(n, arcs, 0, n-1, value)
            b = (value, *([0] * (n-2)), -value)
            for failed in (None, *range(len(arcs))):
                used = oracle.flow(failed)
                if used is not None:
                    cert = certify_flow(n, arcs, b, used, failed)
                    require(cert.cost == oracle.cost(failed), 'native fixed output')
                    COUNTS['oracle_queries'] += 1


def hostile():
    arcs = [Arc(0, 1, 1), Arc(0, 1, 2), Arc(2, 2, -3)]
    b = (1, -1, 0)
    cert = certify_flow(3, arcs, b, (0, 2))
    bad = [replace(cert, used=(0,)), replace(cert, used=(0, 0, 2)),
           replace(cert, used=(False, 2)), replace(cert, used=(-1,)),
           replace(cert, used=(3,)), replace(cert, used=[0, 2]),
           replace(cert, cost=-2.0), replace(cert, potential=(0, 0, 0)),
           replace(cert, potential=(False, 1, 0)), replace(cert, potential=(0, 1)),
           None, {'used': (0, 2)}]
    for c in bad:
        require(not verify_flow(3, arcs, b, c), 'hostile witness accepted')
        COUNTS['hostile'] += 1
    for failure in (0, 2, -1, 3, True, (1,), 1.0):
        require(not verify_flow(3, arcs, b, cert, failure), 'hostile failure accepted')
        COUNTS['hostile'] += 1
    for balances in ((1, -1), (True, -1, 0), (1.0, -1, 0), (1, 0, 0)):
        require(not verify_flow(3, arcs, balances, cert), 'bad balances')
        COUNTS['hostile'] += 1
    require(rejects(lambda: certify_flow(3, arcs, b, (0,))), 'missed disconnected negative loop')
    require(rejects(lambda: certify_maximum(3, [Arc(0, 2, 0)], 0, 2, ())), 'accepted nonmaximum')
    COUNTS['hostile'] += 2
    support, cut = balance_feasibility(3, arcs, (10**100, -10**100, 0))
    require(support is None and verify_infeasible(3, arcs, (10**100, -10**100, 0), cut), 'binary supply cut')
    program = '''
import sys
from types import SimpleNamespace
sys.modules['unit_flow'] = None
sys.modules['certify_flow'] = None
from flow_certificates import FlowCertificate, MaximumCertificate, verify_flow, verify_maximum, verify_infeasible
arcs = [SimpleNamespace(tail=0, head=1, cost=-2)]
f = FlowCertificate((0,), -2, (0, 0))
if not (verify_flow(2, arcs, (1,-1), f) and verify_maximum(2, arcs, 0, 1, MaximumCertificate(1,f,(0,))) and verify_infeasible(2, arcs, (2,-2), (0,))):
    raise SystemExit('independent verifier failed')
'''
    subprocess.run([sys.executable, '-B', '-c', program], cwd=REFERENCE, check=True)


if __name__ == '__main__':
    pairs = [(u, v) for u in range(3) for v in range(3) if u != v]
    for costs in product((-1, 0, 1), repeat=6):
        check(3, [Arc(u, v, c) for (u, v), c in zip(pairs, costs)])
    rng = random.Random(72410)
    for _ in range(60):
        n = rng.randrange(2, 5)
        check(n, [Arc(rng.randrange(n), rng.randrange(n), Fraction(rng.randrange(-4, 5), 3))
                  for _ in range(rng.randrange(1, 8))])
    integration()
    hostile()
    print('PASS exact flow certificates:', COUNTS)
