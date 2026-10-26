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

**Independent static acceptance.** Section 14 uses Bernhard Haeupler,
Yonggang Jiang and Thatchaphol Saranurak,
[*Deterministic Negative-Weight Shortest Paths in Nearly Linear Time via
Path Covers*](https://arxiv.org/html/2511.08551v1), Theorem 1.1, to find
residual distances or a negative cycle. A supplied
integral potential is checked on every residual arc. This establishes
optimality of an accepted static flow, not the fast client's progress
or an online NO certificate for an unknown backend parameter choice.

## Published cycle engine and the stronger local requirements

Rasmus Kyng, Simon Meierhans, Maximilian Probst Gutenberg and Aurelio
Sulser, [*A Simpler and Faster Min-Cost Flow Solver via Min-Ratio Cycles
from Distance Oracles*](https://arxiv.org/html/2609.23852v1), is the
specific public construction used for comparison and for the raw-lift
reconstruction. Its relevant locations are:

| Source location | Supplied ingredient | Remaining local obligation |
|---|---|---|
| Theorems 4.4–4.5 | Deterministic distance-oracle cycle hierarchy with the paper's published parameters | The faster parameters require the separate construction and uniform-cost proof; citing these theorems does not prove the four-fifths bound. |
| Definition 5.1 and Theorem 5.2 | A dynamic numerical interface and its flow solver | New edges enter at zero flow. The local client must separately pay for every stronger insertion, frozen-flow retirement and notification it requests. |
| Lemma 5.4 and the underlying path embeddings | Projection of a cycle to physical graph edges | The printed length inequality in Lemma 5.4 points the wrong way for the raw upper bound needed here. The local raw-lift note reconstructs physical-length domination from the actual embeddings; it does not use that inequality as written. |

The underlying embeddings come from Rasmus Kyng, Simon Meierhans and
Maximilian Probst Gutenberg, [*A Dynamic Shortest Paths Toolbox:
Low-Congestion Vertex Sparsifiers and their Applications*](https://arxiv.org/abs/2311.06402v1),
Definition 3.4, Lemma 3.21 and Algorithm 5. The
[raw-lift proof](../../manuscripts/graph-backends/distance-oracle-raw-lift.md)
tracks each traversal before cancellation and handles loops explicitly.
It establishes the stated geometric implication, while the stronger
chronological repair and complete lifetime requirements remain hypotheses
of the fast numerical implementation.

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
