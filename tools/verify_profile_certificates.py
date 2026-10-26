#!/usr/bin/env python3
"""Exact finite checks for the allocation-quota and scheduling profiles.

Uses only Fraction arithmetic.  The six-profile check enumerates all 915
integer load multisets of total at most 16 and checks their membership in
at least one stated profile.  It also verifies every profile's rounded
load bound, the bucket identities, and the finite quota-ratio range.

These are reproducible regression checks of the formulas and interval
boundaries.  The symbolic manuscripts prove arbitrary rational inputs,
resource feasibility, integral recovery, exact budgets, and running time.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_integer_quotas() -> dict[str, int]:
    checked = 0
    for d in range(2, 31):
        for full in range(d + 1, 400):
            weak = (full + d - 1) // d
            require(full > weak > 0, "positive quota-gap domain")
            require(
                F(full, full - weak) <= F(d + 1, d - 1),
                f"quota ratio failed: d={d}, K={full}",
            )
            checked += 1
        for full in range(1, d + 1):
            require((full + d - 1) // d == 1, "small-target unit gate")
    return {"positive_gap_cases": checked, "minimum_d": 2, "maximum_d": 30}


def check_bucket_identities() -> dict[str, int]:
    require(F(3 * 2**0 - 1, 2**1 - 1) == 2, "polynomial endpoint")
    checked = 0
    for k in range(1, 14):
        denominator = 2 ** (k + 1) - 1
        gamma = F(3 * 2**k - 1, denominator)
        boundaries = [
            F(2**k + 2**i - 1, denominator) for i in range(k + 1)
        ]
        require(boundaries[0] > F(1, 2), "unique large-job threshold")
        require(boundaries[-1] == 1, "full interval coverage")
        require(boundaries[0] + 1 == gamma, "label-zero load")
        require(
            gamma == F(3, 2) + F(1, 2 * denominator),
            "bucket approximation formula",
        )
        for i in range(1, k + 1):
            require(boundaries[i - 1] < boundaries[i], "ordered intervals")
            require(
                boundaries[i] + 2 * (1 - boundaries[i - 1]) == gamma,
                f"bucket load identity failed: k={k}, i={i}",
            )
            checked += 1
    return {"positive_depths": 13, "bucket_load_identities": checked}


# Profiles 1--5.  Profile 0 allows every time <=1/2 and total load <=1.
# Every listed large interval is open on the left and closed on the right,
# with count at most one.  Their common small interval is [0,1/4].
PROFILES = (
    (((F(1, 2), F(3, 4)),), F(1, 2)),
    (((F(3, 4), F(1)),), F(1, 4)),
    (((F(1, 4), F(3, 8)), (F(1, 2), F(5, 8))), F(1, 4)),
    (((F(1, 4), F(3, 8)), (F(5, 8), F(3, 4))), F(1, 8)),
    (((F(3, 8), F(1, 2)), (F(1, 2), F(5, 8))), F(1, 8)),
)


def load_multisets(capacity: int, minimum: int = 1):
    """Every nondecreasing positive integer multiset of sum <= capacity."""
    yield ()
    for first in range(minimum, capacity + 1):
        for tail in load_multisets(capacity - first, first):
            yield (first,) + tail


def fits_profile(jobs: tuple[F, ...], groups, small_cap: F) -> bool:
    small = [time for time in jobs if time <= F(1, 4)]
    if sum(small) > small_cap:
        return False
    large = [time for time in jobs if time > F(1, 4)]
    if not all(any(lo < time <= hi for lo, hi in groups) for time in large):
        return False
    return all(sum(lo < time <= hi for time in large) <= 1 for lo, hi in groups)


def check_six_profiles() -> dict[str, int | list[int]]:
    for groups, small_cap in PROFILES:
        require(
            sum(hi for _, hi in groups) + small_cap + F(1, 4) == F(3, 2),
            "six-profile rounded load",
        )
    covered = [0] * 6
    total = 0
    for multiset in load_multisets(16):
        jobs = tuple(F(time, 16) for time in multiset)
        matches = [all(time <= F(1, 2) for time in jobs)]
        matches.extend(fits_profile(jobs, groups, cap) for groups, cap in PROFILES)
        require(any(matches), f"uncovered load multiset: {multiset}")
        for i, matches_i in enumerate(matches):
            covered[i] += int(matches_i)
        total += 1
    require(total == 915, "complete finite partition count")
    return {
        "capacity": 16,
        "load_multisets": total,
        "profile_memberships": covered,
        "rounded_profile_bounds": 5,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {
        "status": "PASS",
        "scope": "Finite exact formula and profile checks; symbolic proofs are separate.",
        "quotas": check_integer_quotas(),
        "buckets": check_bucket_identities(),
        "six_profiles": check_six_profiles(),
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
