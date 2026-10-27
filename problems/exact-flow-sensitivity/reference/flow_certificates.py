"""Independent exact certificates on the full surviving unit-capacity input.

No optimizer or certificate producer is imported. Costs may be signed exact
integers/Fractions; loops and parallel original records are supported.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
"""
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class FlowCertificate:
    used: tuple[int, ...]
    cost: Fraction
    potential: tuple[Fraction, ...]


@dataclass(frozen=True)
class MaximumCertificate:
    value: int
    flow: FlowCertificate
    source_side: tuple[int, ...]


def _integer(x):
    return type(x) is int


def _exact(x):
    return type(x) in (int, Fraction)


def _instance(n, arcs, failed):
    if not _integer(n) or n < 1:
        raise ValueError('positive integer vertex count required')
    if failed is not None and (not _integer(failed) or not 0 <= failed < len(arcs)):
        raise ValueError('invalid failed original record')
    for a in arcs:
        if (not _integer(a.tail) or not _integer(a.head)
                or not 0 <= a.tail < n or not 0 <= a.head < n or not _exact(a.cost)):
            raise ValueError('invalid original arc')


def _ids(values, limit):
    if type(values) is not tuple or any(not _integer(i) or not 0 <= i < limit for i in values):
        raise ValueError('tuple of original integer identifiers required')
    result = set(values)
    if len(result) != len(values):
        raise ValueError('duplicate identifiers')
    return result


def _balances(n, balances):
    if len(balances) != n or any(not _integer(b) for b in balances) or sum(balances) != 0:
        raise ValueError('integral zero-sum outward balances required')


def verify_flow(n, arcs, balances, certificate, failed=None):
    """Check feasibility and minimum cost for prescribed out-minus-in balances.

    Returns False for malformed data and invalid certificates. Verification
    scans the ORIGINAL surviving input, not only the reported preserver.
    """
    try:
        _instance(n, arcs, failed)
        _balances(n, balances)
        if type(certificate) is not FlowCertificate or not _exact(certificate.cost):
            return False
        potential = certificate.potential
        if type(potential) is not tuple or len(potential) != n or any(not _exact(p) for p in potential):
            return False
        used = _ids(certificate.used, len(arcs))
        if failed in used:
            return False
        divergence = [0] * n
        cost = Fraction(0)
        for i, a in enumerate(arcs):
            if i == failed:
                continue
            reduced = a.cost + potential[a.tail] - potential[a.head]
            if i in used:
                divergence[a.tail] += 1
                divergence[a.head] -= 1
                cost += a.cost
                if reduced > 0:
                    return False
            elif reduced < 0:
                return False
        return divergence == list(balances) and cost == certificate.cost
    except (TypeError, ValueError, AttributeError, IndexError, OverflowError):
        return False


def verify_maximum(n, arcs, source, target, certificate, failed=None):
    """Check maximum value with a cut and minimum cost at that exact value."""
    try:
        _instance(n, arcs, failed)
        if (not _integer(source) or not _integer(target) or source == target
                or not 0 <= source < n or not 0 <= target < n
                or type(certificate) is not MaximumCertificate
                or not _integer(certificate.value) or certificate.value < 0):
            return False
        side = _ids(certificate.source_side, n)
        if source not in side or target in side:
            return False
        balances = [0] * n
        balances[source], balances[target] = certificate.value, -certificate.value
        capacity = sum(a.tail in side and a.head not in side
                       for i, a in enumerate(arcs) if i != failed)
        return capacity == certificate.value and verify_flow(n, arcs, balances, certificate.flow, failed)
    except (TypeError, ValueError, AttributeError, IndexError, OverflowError):
        return False


def verify_infeasible(n, arcs, balances, source_side, failed=None):
    """Check a strict violated cut b(S) > capacity(S, complement(S))."""
    try:
        _instance(n, arcs, failed)
        _balances(n, balances)
        side = _ids(source_side, n)
        capacity = sum(a.tail in side and a.head not in side
                       for i, a in enumerate(arcs) if i != failed)
        return sum(balances[v] for v in side) > capacity
    except (TypeError, ValueError, AttributeError, IndexError, OverflowError):
        return False
