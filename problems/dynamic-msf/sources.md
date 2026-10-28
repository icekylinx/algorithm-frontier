# Sources and proof dependencies

## Canonical manuscripts

- [A deterministic two-thirds worst-case minimum-spanning-forest baseline](proof.md)

## Published theorem-to-operation map

The three papers used in the bound are named here in full. Short author
labels in the longer proof refer to these versions.

| Published source and location | Required operation | Local check |
|---|---|---|
| Chuzhoy, Gao, Li, Nanongkai, Peng and Saranurak, [*A Deterministic Algorithm for Balanced Cut with Applications to Dynamic Connectivity, Flows, and Beyond*](https://arxiv.org/html/1910.08025v2), Corollary 6.1 | Deterministic decomposition on actual contracted graphs, including multigraphs of unbounded degree | The cut-player parameter is clipped to each local size. Protected blocks are expanded with the explicit conductance loss. |
| Meierhans, Probst Gutenberg and Saranurak, [*Expander Pruning with Polylogarithmic Worst-Case Recourse and Update Time*](https://arxiv.org/html/2504.00544v1), Theorems 1.3 and 6.4 | Deterministic worst-case pruning work and vertex publication, within its finite deletion horizon | The adapter publishes initial neighbors and deleted-edge endpoints to handle residual isolates. The chosen decremental period stays below every local horizon. |
| Nanongkai, Saranurak and Wulff-Nilsen, [*Dynamic Minimum Spanning Forest with Subpolynomial Worst-case Update Time*](https://arxiv.org/pdf/1708.03962v2), Theorem 7.1 and Section 9 | Worst-case batch insertion/contraction reduction, actual weighted certificate and child-MSF invariant | The recursive multiplier is logarithmic, not the pruning factor. Retired certificate edges prevent publication from creating many recursive deletions. |
| The same minimum-spanning-forest paper, Lemmas 2.5–2.7 | Deterministic worst-case forest operations and the small compressed-graph MSF routines | These are retained standard primitives; an amortized-only path implementation is insufficient for the displayed worst-case claim. |

The formal note proves the edge-addition and contraction facts used by
the certificate directly. The complete weighted construction in the third
paper remains an external published dependency. Its original headline
algorithm is randomized; determinism here comes from the decomposition
replacement explained in Section 6.2 of the first paper and the
deterministic pruning algorithm in the second. The proof retains the
actual weighted certificate, rather than inferring correctness merely
from connectivity of the unpruned vertices. No research matching or
cycle-search module is needed.

## Local derivation and comparison notes

- [Formal pruning substitution in the public NSW MSF framework](../../manuscripts/graph-backends/dynamic-msf-formal-pruning-substitution-audit.md)
- [Deterministic dynamic spanners: current public baselines and admissible comparisons](../../manuscripts/graph-backends/dynamic-spanner-public-baseline-audit.md)

The [2025 connectivity comparison](https://arxiv.org/html/2510.08297v1)
and [2026 minimum-spanning-forest comparison](https://arxiv.org/html/2610.00491v1)
are not inputs to the derivation. The bound uses only the three named
papers above. The
comparison-RAM or polynomial-logarithmic weight-bit convention, fixed
master cap, adaptive history and explicit edge-change output are
stated in the primary proof.

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** icekylinx · GPT-6 Astra Pro.
