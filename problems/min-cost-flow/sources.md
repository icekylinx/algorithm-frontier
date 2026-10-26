# Sources and proof dependencies

## Canonical manuscripts

- [A moving-box logarithmic client for exact minimum-cost flow](proof.md)

## Dependency status and reading order

**Proved local steps.** Section 11 proves affine-penalty rounding of an
exactly conserved dyadic flow; Section 12 proves the artificial-arc
initialization and its incremental lazy variant. Their correctness is
independent of a minimum-ratio-cycle oracle. The
[exact finite checker](verify/check_recovery.py) exercises these steps
without the proposed fast backend. The fast rounding implementation
uses the named standard dynamic-forest operations.

**Unresolved quantitative backend.** Section 1 requires a fixed
deterministic raw-cycle implementation with one cap for inverse quality,
initialization, updates, queries, occurrence inventory, answer pieces and
complete lifetime logs. It must handle adaptive polynomial histories,
positive integer lengths and the stated numerical bit envelope. The
proposed realization retains [the required deterministic cycle-search implementation](../general-matching/proof.md#116-explicit-raw-backend-realization-contract).
An ordinary net-norm circulation approximation does not supply the raw
traversal bound needed for positivity during a path-list transaction.

**Online initialization.** The penalty for artificial arcs is chosen
from a declared bound on all future original costs/capacities and the
fixed threshold. Repricing it after every insertion is not part of the
proved interface. The lazy incidence test preserves the linear record
bound when nonzero-demand vertices start isolated.

**Independent static acceptance.** Section 14 uses
[Haeupler–Jiang–Saranurak, arXiv:2511.08551v1](https://arxiv.org/html/2511.08551v1),
Theorem 1.1, to find residual distances or a negative cycle. A supplied
integral potential is checked on every residual arc. This establishes
optimality of an accepted static flow, not the fast client's progress
or an online NO certificate for an unknown backend parameter choice.

## Linked mathematical dependencies

These manuscripts contain the interfaces, auxiliary arguments or source
comparisons referenced by this result. Their stated hypotheses remain
part of each use; an interface analysis does not supply an omitted backend.

- [A numerical client independent of the ledger radix](../../manuscripts/graph-backends/decoupled-numerical-client.md)
- [Raw-cycle quality through the 2026 distance-oracle hierarchy](../../manuscripts/graph-backends/distance-oracle-raw-lift.md)
- [Exact acceptance and general-flow reductions](../../manuscripts/graph-backends/exact-flow-acceptance-and-reductions.md)
- [Numerical lifetime discipline and a loop wrapper for flat cycle oracles](../../manuscripts/graph-backends/numerical-backend-lifetime-and-loops.md)
- [A 4/5 research composition from sequential expander routing](../../manuscripts/graph-backends/quantitative-matching-4-5-composition.md)

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
