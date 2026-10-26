"""Exact finite checks for range decomposition, batches, and packed convolution.

This checks finite mathematical identities, not the resource-bounded solver.
"""

from collections import defaultdict
from math import gcd
from pathlib import Path
import json
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path, help="write the full deterministic receipt to this path")
args = parser.parse_args()

if not __debug__:
    raise SystemExit("Run with assertions enabled.")

counts = {"configurations": 0, "quotient_identities": 0,
          "target_batch_bounds": 0, "convolutions": 0}


def classes(length, modulus):
    result = defaultdict(list)
    for value in range(length + 1):
        result[value % modulus].append(value // modulus)
    return result


for capacity in range(1, 5):
    for left in range(1 << capacity):
        for right in range(1 << capacity):
            bits = capacity.bit_length()
            packed_left = sum(((left >> j) & 1) << (bits * j)
                              for j in range(capacity))
            packed_right = sum(((right >> j) & 1) << (bits * j)
                               for j in range(capacity))
            product = packed_left * packed_right
            for k in range(2 * capacity - 1):
                expected = sum(((left >> i) & 1) * ((right >> (k - i)) & 1)
                               for i in range(capacity)
                               if 0 <= k - i < capacity)
                assert (product >> (bits * k)) & ((1 << bits) - 1) == expected
            counts["convolutions"] += 1

    scales = [(a, b) for a in range(1, 2 * capacity + 2)
              for b in range(a, 2 * capacity + 2) if gcd(a, b) == 1]
    scales += [(1, 1000003), (101, 103), (101, 1000003)]
    ranges = sorted({0, capacity * capacity - 1,
                     max(0, capacity * capacity - capacity)})
    for alpha, beta in scales:
        for wa in ranges:
            for wb in ranges:
                ac, bc = classes(wa, beta), classes(wb, alpha)
                assert sum(map(len, ac.values())) == wa + 1
                assert sum(map(len, bc.values())) == wb + 1
                targets = {-1, 0, alpha * wa + beta * wb + 1}
                for x in range(wa + 1):
                    for y in range(wb + 1):
                        target = alpha * x + beta * y
                        x0 = target * pow(alpha, -1, beta) % beta
                        y0 = target * pow(beta, -1, alpha) % alpha
                        assert x0 == x % beta and y0 == y % alpha
                        q, rem = divmod(target - alpha * x0 - beta * y0,
                                        alpha * beta)
                        assert rem == 0 and q == x // beta + y // alpha
                        targets.add(target)
                        counts["quotient_identities"] += 1

                if beta <= capacity:
                    ablocks = [(r, start, min(capacity, len(values) - start))
                               for r, values in ac.items()
                               for start in range(0, len(values), capacity)]
                    bblocks = [(r, start, min(capacity, len(values) - start))
                               for r, values in bc.items()
                               for start in range(0, len(values), capacity)]
                    assert len(ablocks) <= 2 * capacity
                    assert len(bblocks) <= 2 * capacity
                    for target in targets:
                        x0 = target * pow(alpha, -1, beta) % beta
                        y0 = target * pow(beta, -1, alpha) % alpha
                        q = (target - alpha * x0 - beta * y0) // (alpha * beta)
                        hits = sum(sa + sb <= q <= sa + sb + 2 * capacity - 2
                                   for ra, sa, _ in ablocks
                                   for rb, sb, _ in bblocks
                                   if ra == x0 and rb == y0)
                        assert hits <= 4 * capacity
                        counts["target_batch_bounds"] += 1
                else:
                    assert all(len(v) <= capacity for v in ac.values())
                    batches = []
                    if alpha <= capacity:
                        for residue, values in bc.items():
                            for start in range(0, len(values), capacity):
                                batches.append({residue: (start,
                                    min(capacity, len(values) - start))})
                        assert len(batches) <= 2 * capacity
                    else:
                        batch, size = {}, 0
                        for residue, values in bc.items():
                            assert len(values) <= capacity
                            if size + len(values) > 2 * capacity:
                                assert size > capacity
                                batches.append(batch)
                                batch, size = {}, 0
                            batch[residue] = (0, len(values))
                            size += len(values)
                        if batch:
                            batches.append(batch)
                        assert len(batches) <= capacity + 1
                    for target in targets:
                        primary = target % beta
                        x0 = target * pow(alpha, -1, beta) % beta
                        if x0 not in ac:
                            continue
                        assert primary == alpha * x0 % beta
                        secondary = target % (alpha * beta)
                        assert (secondary - alpha * x0) % beta == 0
                        y0 = ((secondary - alpha * x0) // beta) % alpha
                        assert y0 == target * pow(beta, -1, alpha) % alpha
                        q = (target - alpha * x0 - beta * y0) // (alpha * beta)
                        hits = 0
                        for batch in batches:
                            if y0 in batch:
                                start, length = batch[y0]
                                hits += start <= q <= start + length + len(ac[x0]) - 2
                        assert hits <= (2 if alpha <= capacity else 1)
                        counts["target_batch_bounds"] += 1
                counts["configurations"] += 1

receipt = {"status": "PASS", "checks": counts,
           "scope": "Finite quotient/residue identities, ambient batch incidence bounds, and exact packed convolution; not a full solver or asymptotic proof."}
if args.output:
    args.output.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
