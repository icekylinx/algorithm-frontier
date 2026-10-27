#!/usr/bin/env python3
"""Independent finite checks of ordered resource reservations, not the allocator.
Attribution: Yilin Liu and GPT-6 Astra Pro. SPDX-License-Identifier: Apache-2.0
"""
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import random
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
from reservations import Bundle, Reservations

COUNTS = dict(states=0, reservations=0, prefixes=0, completed=0, exchanges=0,
              nonempty_releases=0, sharp_covers=0, rejected=0)


def subsets(items):
    items = tuple(items)
    return (frozenset(c) for k in range(len(items) + 1) for c in combinations(items, k))


def rank_oracle(vectors):
    def rank(owners):
        pivots = {}
        for owner in sorted(owners):
            v = vectors[owner]
            while v:
                lead = v.bit_length()
                if lead in pivots:
                    v ^= pivots[lead]
                else:
                    pivots[lead] = v
                    break
        return len(pivots)
    return rank


def independent_rank(vectors, owners):
    # Enumerate the entire span rather than importing the backend/oracle code.
    span = {0}
    for p in owners:
        span |= {v ^ vectors[p] for v in tuple(span)}
    assert len(span) & (len(span) - 1) == 0
    return len(span).bit_length() - 1


def audit(state, vectors, values=None, threshold=None):
    COUNTS['states'] += 1
    matching, centers = dict(state.matching), state.centers
    assert len({b.owner for b in matching.values()}) == len(matching)
    designated = [i for c in centers for i in c.blockers]
    assert len(designated) == len(set(designated))
    assert set(designated) <= matching.keys()
    for c in centers:
        assert all(matching[i].resources & c.bundle.resources for i in c.blockers)
    for j, columns in enumerate(vectors):
        rank = lambda owners: independent_rank(columns, owners)
        actual = {b.owner for b in matching.values() if j in b.resources}
        selected_list = [c.bundle.owner for c in centers if j in c.bundle.resources]
        assert len(selected_list) == len(set(selected_list))
        assert not actual.intersection(selected_list)
        assert rank(actual) == len(actual)
        for indices in subsets(range(len(centers))):
            removed = {i for h in indices for i in centers[h].blockers}
            kept = {b.owner for i, b in matching.items() if i not in removed and j in b.resources}
            selected = {centers[h].bundle.owner for h in indices if j in centers[h].bundle.resources}
            assert not kept & selected
            assert rank(kept | selected) == len(kept | selected)
            COUNTS['reservations'] += 1
        for count in range(len(centers) + 1):
            prefix = centers[:count]
            marked = {i for c in prefix for i in c.blockers}
            x = {c.bundle.owner for c in prefix if j in c.bundle.resources}
            y = {matching[i].owner for i in marked if j in matching[i].resources}
            w = x | y
            u = actual - y
            assert rank(w | u) == rank(w) + len(u)
            COUNTS['prefixes'] += 1
            if count < len(centers) and j in centers[count].bundle.resources:
                p = centers[count].bundle.owner
                assert rank(w | {p}) == rank(w) + 1
        for h, center in enumerate(centers):
            if state.releasable(h) and j in center.bundle.resources:
                earlier = {c.bundle.owner for c in centers[:h] if j in c.bundle.resources}
                assert rank(actual | earlier | {center.bundle.owner}) == rank(actual | earlier) + 1
    if values is not None:
        for b in tuple(matching.values()) + tuple(c.bundle for c in centers):
            total = sum(values[j] for j in b.resources)
            assert total >= threshold
            assert all(total - values[j] < threshold for j in b.resources)
        if all(not state.releasable(h) for h in range(len(centers))):
            phi = 0
            for j, columns in enumerate(vectors):
                owners = {c.bundle.owner for c in centers if j in c.bundle.resources}
                owners |= {matching[i].owner for i in designated if j in matching[i].resources}
                phi += values[j] * independent_rank(columns, owners)
            u = max(values, default=0)
            assert phi <= max(u, 2 * threshold + min(u, threshold)) * len(designated)
            COUNTS['sharp_covers'] += 1


def expect_reject(state, operation):
    before = state.matching, state.centers
    try:
        operation()
    except ValueError:
        COUNTS['rejected'] += 1
    else:
        raise AssertionError('expected rejection')
    assert (state.matching, state.centers) == before


def exhaustive_single_resource():
    for vectors in product(range(4), repeat=3):
        for owners in subsets(range(3)):
            if independent_rank(vectors, owners) != len(owners):
                continue
            matching = tuple(Bundle(p, frozenset({0})) for p in sorted(owners))
            for p in range(3):
                state = Reservations(3, [rank_oracle(vectors)], matching)
                audit(state, [vectors], [1], 1)
                candidate = Bundle(p, frozenset({0}))
                if p in owners or vectors[p] == 0:
                    expect_reject(state, lambda: state.complete(candidate))
                    continue
                blockers = state.complete(candidate)
                COUNTS['completed'] += 1
                audit(state, [vectors], [1], 1)
                if not blockers:
                    state.exchange(candidate, None, 0)
                    COUNTS['exchanges'] += 1
                    audit(state, [vectors], [1], 1)


def eager_fixture():
    # Removing e1 from a conservative {e1,e2} group and inserting e3 releases
    # the old center e1+e2, even though the group still contains e2.
    vectors = [(1, 2, 3, 4)]
    state = Reservations(4, [rank_oracle(vectors[0])],
                         [Bundle(0, frozenset({0})), Bundle(1, frozenset({0}))])
    assert state.complete(Bundle(2, frozenset({0}))) == {0, 1}
    audit(state, vectors)
    assert not state.releasable(0)
    state.exchange(Bundle(3, frozenset({0})), 0, 1)
    audit(state, vectors)
    assert state.centers[0].blockers == {1} and state.releasable(0)
    COUNTS['nonempty_releases'] += 1
    state.exchange(state.centers[0].bundle, 1, 0)
    audit(state, vectors)
    expect_reject(state, lambda: state.exchange(Bundle(0, frozenset({0})), None, 1))
    expect_reject(state, lambda: state.complete(Bundle(2, frozenset({0}))))
    expect_reject(state, lambda: state.exchange(Bundle(0, frozenset({0})), 77, 0))
    expect_reject(state, lambda: state.complete(Bundle(4, frozenset({0}))))


def randomized_traces():
    rng = random.Random(531407)
    for trial in range(160):
        q, m = 6, 4
        vectors = [tuple(rng.randrange(8) for _ in range(q)) for _ in range(m)]
        values = [Fraction(rng.randrange(1, 6), 2) for _ in range(m)]
        threshold = Fraction(rng.randrange(1, 7), 2)
        resources = [s for s in subsets(range(m)) if s and sum(values[j] for j in s) >= threshold
                     and all(sum(values[k] for k in s - {j}) < threshold for j in s)]
        state = Reservations(q, map(rank_oracle, vectors))
        for step in range(45):
            audit(state, vectors, values, threshold)
            candidates = [Bundle(p, s) for p in range(q) for s in resources]
            rng.shuffle(candidates)
            choices = [h for h in range(len(state.centers)) if state.releasable(h)]
            if choices:
                h = rng.choice(choices)
                candidate = state.centers[h].bundle
                out = [i for i, b in state.matching if b.owner == candidate.owner]
                if not out:
                    out = [None] + [i for i, _ in state.matching]
                keep = rng.randrange(h + 1)
                outgoing = rng.choice(out)
                if outgoing is None:
                    keep = 0
                if state.centers[h].blockers:
                    COUNTS['nonempty_releases'] += 1
                state.exchange(candidate, outgoing, keep)
                COUNTS['exchanges'] += 1
                continue
            moved = False
            for candidate in candidates:
                before = state.matching, state.centers
                try:
                    blockers = state.complete(candidate)
                except ValueError:
                    assert (state.matching, state.centers) == before
                    continue
                COUNTS['completed'] += 1
                moved = True
                if not blockers:
                    own = [i for i, b in state.matching if b.owner == candidate.owner]
                    outgoing = own[0] if own else rng.choice([None] + [i for i, _ in state.matching])
                    keep = 0 if outgoing is None else rng.randrange(len(state.centers) + 1)
                    state.exchange(candidate, outgoing, keep)
                    COUNTS['exchanges'] += 1
                break
            if not moved:
                # Explicitly exercise state changes that make old groups redundant.
                for candidate in candidates:
                    outgoing = next((i for i, b in state.matching if b.owner == candidate.owner), None)
                    if outgoing is None and state.matching:
                        outgoing = rng.choice(state.matching)[0]
                    keep = rng.randrange(len(state.centers) + 1) if outgoing is not None else 0
                    try:
                        state.exchange(candidate, outgoing, keep)
                    except ValueError:
                        continue
                    COUNTS['exchanges'] += 1
                    break
                else:
                    break
        audit(state, vectors, values, threshold)


if __name__ == '__main__':
    exhaustive_single_resource()
    eager_fixture()
    randomized_traces()
    assert COUNTS['nonempty_releases'] > 1
    print('PASS ordered recipient reservations:', ', '.join(f'{k}={v}' for k, v in COUNTS.items()))
