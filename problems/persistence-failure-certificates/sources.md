# Sources and proof dependencies: Exact persistence under correlated failures

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Exact incidence and persistence summaries](manuscripts/correlated-fault-boundary-and-persistence-sparsifiers.md) | The common-scalar incidence decoder, sharp rank envelopes, surviving prefix spans, and natural persistence-module isomorphisms. |
| [Construction from the actual feature rank](manuscripts/feature-rank-construction.md) | Degree-bounded evaluation-module closure, canonical column pivots, nonzero feature shifts, shared original-row compression, streamed boundary/lift construction and exact arithmetic costs. |

## Related results and model distinctions

| Result | Role |
|---|---|
| [Spectral incidence summaries](../correlated-spectral-regression/manuscripts/graded-incidence-and-simplicial-spectral-sparsification.md) | A separate real-valued approximation theorem. It is not a premise of the exact persistence proof and does not add a guarantee for all filtration thresholds. |

## External inputs

The exact result follows from the incidence identity, ordered linear-basis selection, and chain-complex comparison proved in the companion. Its bibliography distinguishes ordinary simplicial sparsification and colored-graph antecedents from the exact failure-and-filtration statement.

The new feature construction includes a complete elementary proof rather
than invoking a rank oracle on a hidden exponential matrix. Its bibliography
credits the finite-point linear algebra of Buchberger–Möller and later
ideals-of-points algorithms. These are historical and comparison sources;
Theorems 1–3 supply the actual algorithm used here.

The [reference package](reference/README.md) implements rational and
supplied prime fields. Finite-field extension construction and the
conservative rational bit bound remain explicit mathematical components,
with their executable boundary stated beside the algorithm.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
