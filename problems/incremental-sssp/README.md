# Incremental directed SSSP with simple-path reporting

This is a Tier A conditional record for incremental directed shortest paths with explicit path output.

| Field | Curated statement |
|---|---|
| **Guarantee** | Maintains one-source approximate distances under arbitrary online edge insertions and returns a simple directed path with original edge identifiers. |
| **Objective and output** | For every reachable vertex, the estimate is between the true distance and one plus epsilon times the true distance. Unreachable vertices return infinity. A reported path with **k** edges costs linear output work times a polynomial in log of the global size. |
| **Update time** | Linear input assembly plus the graph size multiplied by an exponential factor whose leading term is the four-fifths hierarchy envelope and whose accuracy term is the square root of the master logarithm times the sum of **h** and log of one over epsilon. This is conditional on the raw detector interface. |
| **Space** | Actual root vertices, inserted edges, and auxiliary copies over their lifetimes, with no graph padded to the master cap. |
| **Parameters** | **N** is the power-of-two master cap for root vertices and inserted edge records; **U** is log of N; **h** is log of U plus a constant; **epsilon** is between zero and one-half; **c** is the fixed constant in the restriction log of one over epsilon at most c times U; **k** is the number of edges returned. |
| **Model and representation** | Nonnegative incremental directed weights, positive polynomial-range root lengths, parallel edges allowed, and the frozen-detector raw interface with exact retirement and callback accounting. |
| **Lower-bound scope** | This is a conditional upper-bound candidate. It is not an unconditional published theorem and carries no new lower-bound claim. |
| **Review status** | Internal proof, algorithm, and source review is tracked in the [headline review report](../../reviews/headline/dynamic-graph-frontier.md). Finite detector and path audits are evidence for the composition; they are not formal verification. |

Read the [proof map](proof.md), [source map](sources.md), and [complexity guide](../../docs/COMPLEXITY.md) for the exact accuracy and backend hypotheses.

**Source.** [Frozen-detector incremental SSSP](../../sources/checkpoint-o/frozen_detector_incremental_sssp.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
