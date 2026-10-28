"""Certified supplied-baseline valuated single-element-failure reporting.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0

Valid minimization-convention valuated matroids of the stated fixed rank
are assumed. Value callbacks return exact int/Fraction on bases and None
outside the effective domain. No valuated baseline search is implemented.
"""
from dataclasses import dataclass
from fractions import Fraction

import arborescence_reporting as reporting
import matroid_reporting as ordinary


@dataclass(frozen=True)
class BaselineCertificate:
    baseline: tuple
    value: Fraction
    prices: tuple  # original N-coordinate price vector; preprocessing only


def _input(n, rank, value1, value2, baseline):
    baseline = tuple(baseline)
    if (type(n) is not int or n < 0 or type(rank) is not int or not 0 <= rank <= n
            or len(baseline) != rank or len(set(baseline)) != rank
            or any(type(a) is not int or not 0 <= a < n for a in baseline)
            or not callable(value1) or not callable(value2)):
        raise ValueError('explicit ground, fixed rank, two valuations and a distinct common baseline required')
    return baseline


def _value(callback, chosen):
    answer = callback(frozenset(chosen))
    return None if answer is None else ordinary.weighted.rational(answer)


def _table(n, rank, value1, value2, baseline):
    baseline = _input(n, rank, value1, value2, baseline)
    chosen = frozenset(baseline)
    values = tuple(_value(callback, chosen) for callback in (value1, value2))
    if any(value is None for value in values):
        raise ValueError('baseline is not common finite-valued')
    tables = []
    for callback, value in zip((value1, value2), values):
        table = {}
        for e in range(n):
            if e in chosen:
                continue
            for a in baseline:
                exchanged = _value(callback, (chosen - {a}) | {e})
                if exchanged is not None:
                    table[a, e] = exchanged - value
        tables.append(table)
    return baseline, sum(values, Fraction(0)), tuple(tables)


def _candidates(n, baseline, tables):
    chosen = frozenset(baseline)
    candidates = {}
    for e in range(n):
        if e in chosen:
            continue
        first = tuple(a for a in baseline if (a, e) in tables[0])
        second = tuple(b for b in baseline if (b, e) in tables[1])
        for a in first:
            for b in second:
                length = tables[0][a, e] + tables[1][b, e]
                old = candidates.get((a, b))
                if old is None or (length, e) < old:
                    candidates[a, b] = length, e
    return candidates


def _certify(n, baseline, value, tables, candidates):
    # Super-source distances in the k-vertex compressed graph. Negative
    # cycles exactly obstruct a split price for the supplied common baseline.
    prices = {a: Fraction(0) for a in baseline}
    changed = False
    for _ in range(len(baseline)):
        changed = False
        for (a, b), (length, _) in candidates.items():
            if prices[b] > prices[a] + length:
                prices[b] = prices[a] + length
                changed = True
        if not changed:
            break
    else:
        if changed:
            raise ValueError('supplied common baseline is not optimal')
    original = [Fraction(0)] * n
    for a, price in prices.items():
        original[a] = price
    chosen = frozenset(baseline)
    for e in range(n):
        if e in chosen:
            continue
        upper = tuple(prices[a] + tables[0][a, e] for a in baseline if (a, e) in tables[0])
        lower = tuple(prices[b] - tables[1][b, e] for b in baseline if (b, e) in tables[1])
        lo, hi = (max(lower) if lower else None), (min(upper) if upper else None)
        if lo is not None and hi is not None and lo > hi:
            raise RuntimeError('compressed potential did not give an original split price')
        original[e] = hi if hi is not None else lo if lo is not None else Fraction(0)
    certificate = BaselineCertificate(baseline, value, tuple(original))
    if not _verify_table(n, certificate, value, tables):
        raise RuntimeError('constructed baseline optimality certificate failed')
    return certificate


def _verify_table(n, certificate, value, tables):
    if (type(certificate) is not BaselineCertificate or type(certificate.prices) is not tuple
            or len(certificate.prices) != n or certificate.value != value):
        return False
    prices = tuple(ordinary.weighted.rational(x) for x in certificate.prices)
    ordinary.weighted.rational(certificate.value)
    return (all(gamma >= prices[e] - prices[a] for (a, e), gamma in tables[0].items())
            and all(gamma >= prices[b] - prices[e] for (b, e), gamma in tables[1].items()))


def certify(n, rank, value1, value2, baseline):
    """Certify the supplied common optimum, or reject a nonoptimal baseline.

    This is a baseline validator, not a search for an optimal common basis.
    The ground-sized split prices are independent preprocessing evidence.
    """
    baseline, value, tables = _table(n, rank, value1, value2, baseline)
    return _certify(n, baseline, value, tables, _candidates(n, baseline, tables))


def verify_optimality(n, rank, value1, value2, certificate):
    """Original local-exchange check; no graph, optimizer or producer calls."""
    try:
        if type(certificate) is not BaselineCertificate or type(certificate.baseline) is not tuple:
            return False
        _, value, tables = _table(n, rank, value1, value2, certificate.baseline)
        return _verify_table(n, certificate, value, tables)
    except (ValueError, TypeError, AttributeError, IndexError):
        return False


def build(n, rank, value1, value2, baseline):
    """Return the compact exact fixed-rank deletion reporter.

    The supplied common baseline is independently certified optimal. All
    prices, exchange tables and original callbacks are discarded before
    returning. Queries evaluate neither valuation nor independence oracle.
    """
    baseline, value, tables = _table(n, rank, value1, value2, baseline)
    candidates = _candidates(n, baseline, tables)
    _certify(n, baseline, value, tables, candidates)
    minus = {a: 2 * j for j, a in enumerate(baseline)}
    plus = {a: node + 1 for a, node in minus.items()}
    arcs = [reporting._AuxArc(minus[a], plus[a], (Fraction(0), 0)) for a in baseline]
    arcs.extend(reporting._AuxArc(plus[a], minus[b], (length, 1), label=e, removed=a)
                for (a, b), (length, e) in sorted(candidates.items()))
    return reporting._finish(baseline, value, 2 * rank, tuple(arcs), minus, plus)
