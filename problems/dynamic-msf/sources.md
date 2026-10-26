# Sources and proof dependencies

## Canonical manuscripts

- [A deterministic two-thirds worst-case minimum-spanning-forest baseline](proof.md)

## Linked mathematical dependencies

These manuscripts contain the interfaces, auxiliary arguments or source
comparisons referenced by this result. Their stated hypotheses remain
part of each use; an interface analysis does not supply an omitted backend.

| Source | Required interface | Local check |
|---|---|---|
| CGLNPS Corollary 6.1 | Deterministic decomposition on actual contracted graphs, including multigraphs of unbounded degree | The cut-player parameter is clipped to each local size. Protected blocks are expanded with the explicit conductance loss. |
| MGS Theorems 1.3 and 6.4 | Deterministic worst-case pruning work and vertex publication, within its finite deletion horizon | The adapter publishes initial neighbors and deleted-edge endpoints to handle residual isolates. The chosen decremental period stays below every local horizon. |
| NSW Theorem 7.1 and Section 9 | Worst-case batch insertion/contraction reduction, actual weighted certificate and child-MSF invariant | The recursive multiplier is logarithmic, not the pruning factor. Retired certificate edges prevent publication from creating many recursive deletions. |
| NSW Lemmas 2.5–2.7 | Deterministic worst-case forest operations and the small compressed-graph MSF routines | These are retained standard primitives; an amortized-only path implementation is insufficient for the displayed worst-case claim. |

The formal note proves the edge-addition and contraction facts used by
the certificate directly. The full NSW weighted construction remains
an external published dependency. The stated bound uses the published decomposition, pruning and MSF
components above; it needs no research matching or cycle-search module.

- [Formal pruning substitution in the public NSW MSF framework](../../manuscripts/graph-backends/dynamic-msf-formal-pruning-substitution-audit.md)
- [Deterministic dynamic spanners: current public baselines and admissible comparisons](../../manuscripts/graph-backends/dynamic-spanner-public-baseline-audit.md)

## Primary references

The manuscripts identify the theorem and version used at each import.
Direct external references appearing in this reading path are:

- <https://arxiv.org/html/1910.08025v2>
- <https://arxiv.org/html/2504.00544v1>
- <https://arxiv.org/html/2510.08297v1>
- <https://arxiv.org/html/2610.00491v1>
- <https://arxiv.org/pdf/1708.03962>

The 2025 and 2026 connectivity/MSF papers in the list are comparison
sources only. The bound is obtained from CGLNPS, MGS and NSW. The
comparison-RAM or polynomial-logarithmic weight-bit convention, fixed
master cap, adaptive history and explicit edge-change output are
stated in the primary proof.

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
