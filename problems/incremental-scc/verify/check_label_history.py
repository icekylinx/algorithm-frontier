#!/usr/bin/env python3
"""Exhaustively check historical equality and first-coalescence queries.

Enumerates merge-only partition histories through five vertices, with every
grouping of consecutive internal merges into settled external updates.
This verifies the label representation only, not an SCC or raw-cycle solver.
"""
from bisect import bisect_right
from itertools import combinations


def merge_sequences(blocks, prefix=()):
    yield prefix
    for i, j in combinations(range(len(blocks)), 2):
        merged = blocks[i] | blocks[j]
        following = tuple(b for k, b in enumerate(blocks) if k not in (i, j)) + (merged,)
        yield from merge_sequences(following, (*prefix, (blocks[i], blocks[j])))


def historical_label(history, time):
    index = bisect_right(history, (time, float("inf"))) - 1
    return history[index][1]


def first_coalescence(histories, u, v):
    """Return the time and comparison count using a common label suffix."""
    if u == v:
        return 0, 0
    first, second = histories[u], histories[v]
    if first[-1][1] != second[-1][1]:
        return None, 1
    # Equal labels occupy exactly one common suffix: representatives are
    # never reused after retirement, and merged vertices never separate.
    low, high = 1, min(len(first), len(second))
    comparisons = 1
    while low < high:
        middle = (low + high + 1) // 2
        comparisons += 1
        if first[-middle][1] == second[-middle][1]:
            low = middle
        else:
            high = middle - 1
    return max(first[-low][0], second[-low][0]), comparisons


def main():
    if not __debug__:
        raise SystemExit("This checker requires assertions; run Python without -O.")
    histories_checked = equality_queries = first_queries = suffix_comparisons = 0
    for n in range(1, 6):
        initial = tuple(frozenset((v,)) for v in range(n))
        for sequence in merge_sequences(initial):
            batching_count = 1 << max(0, len(sequence) - 1)
            for boundaries in range(batching_count):
                labels = list(range(n))
                histories = [[(0, v)] for v in range(n)]
                snapshots = [tuple(labels)]
                time = 1
                for step, (a, b) in enumerate(sequence):
                    ra, rb = labels[min(a)], labels[min(b)]
                    if (len(a), -ra) < (len(b), -rb):
                        a, b, ra, rb = b, a, rb, ra
                    for v in b:
                        labels[v] = ra
                        record = (time, ra)
                        if histories[v][-1][0] == time:
                            histories[v][-1] = record
                        else:
                            histories[v].append(record)
                    if step == len(sequence) - 1 or boundaries & (1 << step):
                        snapshots.append(tuple(labels))
                        time += 1
                for history in histories:
                    assert len(history) <= n.bit_length()
                for u in range(n):
                    for v in range(n):
                        for t, snapshot in enumerate(snapshots):
                            assert (
                                historical_label(histories[u], t) == historical_label(histories[v], t)
                            ) == (snapshot[u] == snapshot[v])
                            equality_queries += 1
                        expected = next(
                            (t for t, snapshot in enumerate(snapshots) if snapshot[u] == snapshot[v]), None
                        )
                        answer, comparisons = first_coalescence(histories, u, v)
                        assert answer == expected
                        length = min(len(histories[u]), len(histories[v]))
                        assert comparisons <= 1 + (length - 1).bit_length()
                        suffix_comparisons += comparisons
                        reverse_equalities = [
                            histories[u][-i][1] == histories[v][-i][1]
                            for i in range(1, length + 1)
                        ]
                        assert reverse_equalities == sorted(reverse_equalities, reverse=True)
                        common_count = len(
                            {label for _, label in histories[u]}
                            & {label for _, label in histories[v]}
                        )
                        assert common_count == sum(reverse_equalities)
                        first_queries += 1
                histories_checked += 1
    print(f"Histories: {histories_checked} merge/batching cases through five vertices.")
    print(f"Queries: {equality_queries} historical equalities; {first_queries} first-coalescence answers.")
    print(f"Common-suffix algorithm: {suffix_comparisons} direct label comparisons, with logarithmic history bounds.")
    print("PASS: merge-only label representation; no SCC-maintenance certification.")


if __name__ == "__main__":
    main()
