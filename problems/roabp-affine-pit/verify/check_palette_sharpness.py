#!/usr/bin/env python3
"""Exact sparse-polynomial checks of the separate palette lower family.

This checks concrete instances over Z, so their identities reduce to every
characteristic. It is not a verification of the upper-bound PIT theorem.
No third-party package is needed. Every variable is used in exactly one
factor and represented by one bit in a squarefree monomial mask.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path


def support_bound(palette: tuple[int, ...]) -> int:
    return math.prod(b - a + 1 for a, b in zip(palette, palette[1:])) - 2


def construct(palette: tuple[int, ...]):
    """Return factors (rank, row, column), source, sink; indices are zero based."""
    width = palette[-1]
    assert palette[0] == 0 and all(a < b for a, b in zip(palette, palette[1:]))
    if len(palette) == 2:
        return [(width, j, j + 1) for j in range(width - 1)], 0, width - 1
    first_rank = palette[1]
    smaller = (0,) + tuple(p - first_rank for p in palette[2:])
    subword, alpha, beta = construct(smaller)
    embedded = [(s + first_rank, i + first_rank, j + first_rank)
                for s, i, j in subword]
    factors = list(embedded)
    for active in range(first_rank):
        factors.append((first_rank, first_rank + beta, active))
        factors.append((first_rank, active, first_rank + alpha))
        factors.extend(embedded)
    return factors, first_rank + alpha, first_rank + beta


def check_one(palette: tuple[int, ...]) -> dict:
    width = palette[-1]
    factors, source, sink = construct(palette)
    expected_support = support_bound(palette)
    assert len(factors) == expected_support

    # These elementary local forms have generic rank exactly s over any
    # field: their active block is either I_s or I_s+x E_ij with i!=j;
    # an off-active row/column is a multiple of one active row/column.
    # Constant products are nested flag projectors P_min. This certifies
    # every interval rank, without substituting finitely many field points.
    for s, i, j in factors:
        assert s in palette[1:] and 0 <= i < width and 0 <= j < width
        assert i != j and (i < s or j < s)
    interval_rank_counts = {}
    for start in range(len(factors)):
        smallest = width
        for end in range(start, len(factors)):
            smallest = min(smallest, factors[end][0])
            interval_rank_counts[str(smallest)] = interval_rank_counts.get(str(smallest), 0) + 1

    # Multiply the actual polynomial row. Dictionary keys are monomials,
    # values are exact integer coefficients, with no random specialization.
    row = [{} for _ in range(width)]
    row[source] = {0: 1}
    peak_terms = 1
    for variable, (s, i, j) in enumerate(factors):
        next_row = [dict(row[column]) if column < s else {} for column in range(width)]
        bit = 1 << variable
        for mask, coefficient in row[i].items():
            assert not mask & bit
            key = mask | bit
            next_row[j][key] = next_row[j].get(key, 0) + coefficient
        row = next_row
        peak_terms = max(peak_terms, sum(map(len, row)))
    assert row[sink] == {(1 << len(factors)) - 1: 1}, (palette, row[sink])
    return {
        "width": width,
        "palette": palette,
        "support": expected_support,
        "source_one_based": source + 1,
        "sink_one_based": sink + 1,
        "interval_count": len(factors) * (len(factors) + 1) // 2,
        "interval_rank_counts": interval_rank_counts,
        "peak_sparse_row_terms": peak_terms,
        "scalar_identity": "exact squarefree product, coefficient 1 over Z",
        "passed": True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-width", type=int, default=7)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_width < 1:
        parser.error("--max-width must be positive")
    cases = []
    for width in range(1, args.max_width + 1):
        for bits in itertools.product((0, 1), repeat=width - 1):
            palette = (0,) + tuple(i + 1 for i, present in enumerate(bits) if present) + (width,)
            cases.append(check_one(palette))
    output = {
        "status": "all exact instance checks passed",
        "scope": "lower-bound construction only; not a certificate of the PIT upper bound",
        "arithmetic": "integer sparse polynomial identities, valid after reduction to every field",
        "max_width": args.max_width,
        "case_count": len(cases),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "cases": cases,
    }
    encoded = json.dumps(output, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(json.dumps({key: value for key, value in output.items() if key != "cases"}))


if __name__ == "__main__":
    main()
