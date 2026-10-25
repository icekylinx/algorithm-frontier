# Featured results

[Download the overview PDF](overview.pdf) for the visual catalogue, headline cards, explicit parameter definitions, review vocabulary, and checkpoint lineage.

This page is the short reading path. [`CONTENTS.md`](CONTENTS.md) is the complete machine-readable map; each linked record contains the exact source paths and review boundary.

## Headline cards

### Numeric-target frontier

The R/S family separates numeric target magnitude from support geometry. It contains exact target decisions, exact scalar optimization, fixed-dimensional variants, support-sensitive refinements, and separate oracle versus readable-program lower-bound statements.

[Open the R/S record](problems/numeric-target-frontier/) · [Open its review report](reviews/headline/numeric-target-frontier.md)

### Weighted-prefix and sparse-quota frontier

The T/U family covers common-order prefix quotas, several shared weight families, laminar root caps, sparse mixed quotas, sharp frequency-one lower bounds, and deterministic ground reductions. The kernel outputs are listed separately from end-to-end algorithm times.

[Open the T/U record](problems/weighted-prefix-quota-frontier/) · [Open its review report](reviews/headline/weighted-prefix-quota-frontier.md)

### Faster Subset Sum

An exact indexed-witness algorithm for arbitrary signed binary inputs. The record states the input count, full binary encoding length, exact witness output, time exponent, and the fact that no space exponent is claimed for this algorithm.

[Open the fast-time record](problems/subset-sum-fast-deterministic/) · [Open its review report](reviews/headline/faster-subset-sum.md)

### Low-space Subset Sum

A separate exact indexed-witness algorithm. Its card gives the full binary input length, bit-operation model, writable-bit space meaning, exact space exponent, and the distinction from the faster-time algorithm.

[Open the low-space record](problems/subset-sum-low-space-deterministic/) · [Open its review report](reviews/headline/low-space-subset-sum.md)

### Graph frontiers

Matching, dynamic APSP, dynamic spanners, incremental SSSP/SCC, and related records retain separate update, stretch, recourse, path-reporting, and backend assumptions instead of collapsing them into one number.

[Open the graph catalogue](CONTENTS.md#graph-algorithms-and-matching) · [Open the graph review report](reviews/headline/dynamic-graph-frontier.md)

## How to read a result

1. Read the result card for the guarantee and objective/output.
2. Check the separate time and space rows and the local parameter definitions.
3. Follow the proof map and review report before treating a claim as algorithmically complete.
4. Inspect the source map and checkpoint manifest for exact provenance.
5. Treat finite certificate replay as evidence for a proof component, not as formal verification of the full arbitrary-input algorithm.
