# Featured results

[Download the overview PDF](overview.pdf) for a compact academic-style catalogue of problem statements, parameters, and complexity bounds.

The repository is indexed by [problem family](docs/FAMILIES.md). Use [Contents](CONTENTS.md) for every curated record and the [review registry](reviews/README.md) for proof, algorithm, source, and finite-check status.

## Headline records

| Family | Record | What the card fixes explicitly |
|---|---|---|
| Subset Sum | [Faster deterministic Subset Sum](problems/subset-sum-fast-deterministic/) | Signed binary input, target, witness, bit length, time exponent, and no claimed space exponent |
| Subset Sum | [Low-space deterministic Subset Sum](problems/subset-sum-low-space-deterministic/) | Signed binary input, target, witness, time exponent, writable-space exponent, and model |
| Numeric targets | [Numeric-target frontier](problems/numeric-target-frontier/) | Target magnitude, support budget, accuracy, representation, and lower-bound scope |
| Quota systems | [Weighted-prefix and sparse-quota frontier](problems/weighted-prefix-quota-frontier/) | Prefix order, weight-family count, laminar depth, sparse support, and kernel versus end-to-end cost |
| Dynamic graphs | [Dynamic APSP](problems/apsp-frontier/) | Update regime, stretch, query time, graph-size parameters, and backend assumptions |
| Matching | [General-graph matching](problems/general-matching/) | Exact objective, graph representation, and conditional backend boundary |

## Reading a card

1. Read the problem and output model.
2. Read time and space as separate rows, including every parameter.
3. Check the proof map and review report for claim boundaries.
4. Follow the source map to the exact checkpoint payload.

Finite certificate replay supports a stated proof component; it is not a formal verification of an arbitrary-input theorem.
