# Sources and proof dependencies

## Canonical manuscripts

- [A moving-box logarithmic client for exact minimum-cost flow](proof.md)

## Dependency status and reading order

**Proved local steps.** Section 11 proves affine-penalty rounding of an
exactly conserved dyadic flow; Section 12 proves the artificial-arc
initialization and its incremental lazy variant. Their correctness is
independent of a minimum-ratio-cycle oracle. The
[exact finite checker](verify/check_recovery.py) exercises these steps
without executing the fast backend. The fast rounding implementation
uses the named standard dynamic-forest operations.

**Constructed quantitative backend.** Section 1 separates a generic
raw-interface client from its four-fifths instantiation. The
[quantitative construction, Sections 1–7](../../manuscripts/graph-backends/quantitative-matching-4-5-composition.md)
supplies one cap for inverse quality, initialization, updates, queries,
occurrence inventory, answer pieces and lifetime logs. The
[raw-lift proof, Sections 2–7](../../manuscripts/graph-backends/distance-oracle-raw-lift.md)
counts physical traversals before cancellation, and the
[lifetime construction, Sections 1–4](../../manuscripts/graph-backends/numerical-backend-lifetime-and-loops.md)
supplies signed and absolute retirement transfers under adaptive
polynomial histories. The [uniform source audit](../../manuscripts/graph-backends/uniform-source-interfaces-for-4-5.md)
states the retained deterministic public algorithms and the local
growing-parameter and finite-bit constructions. These supply the
interface; a net-norm approximation alone would be insufficient.

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

**An alternative published solver for the cut-tree application.**
The Gomory–Hu application can use a route with fewer local construction
dependencies than this manuscript's faster numerical client. Jan van
den Brand, Li Chen, Rasmus Kyng,
Yang P. Liu, Simon Meierhans, Maximilian Probst Gutenberg and Sushant
Sachdeva, [*Almost-Linear Time Algorithms for Decremental Graphs:
Min-Cost Flow and More via Duality*](https://arxiv.org/html/2407.10830v1),
Theorem 6.17 and Section 6.2 provide deterministic exact integral flow
with leading logarithmic power <code class="math">5/6</code>. The local
[capacity-bit reduction](../../manuscripts/graph-backends/published-flow-capacity-scaling.md)
extends its use to globally polynomial capacities on small recursive
graphs while each actual solver call has capacities bounded by its
own edge count. Its proof and
[finite checker](verify/check_capacity_scaling.py) are self-contained;
the named published fast solver remains an external theorem dependency.
Its five-sixths cost is absorbed by the six-sevenths forest bound.
This is an alternative to the already constructed four-fifths route,
not a repair of a missing proof of that route.

## Published cycle engine and the local extensions

Rasmus Kyng, Simon Meierhans, Maximilian Probst Gutenberg and Aurelio
Sulser, [*A Simpler and Faster Min-Cost Flow Solver via Min-Ratio Cycles
from Distance Oracles*](https://arxiv.org/html/2609.23852v1), is the
specific public construction used for comparison and for the raw-lift
reconstruction. Its relevant locations are:

| Source location | Supplied ingredient | Local construction used here |
|---|---|---|
| Theorems 4.4–4.5 | Deterministic distance-oracle cycle hierarchy with the paper's published parameters | The quantitative composition and uniform source audit above prove the faster parameters using the local router, normalization and repair constructions. |
| Definition 5.1 and Theorem 5.2 | A dynamic numerical interface and its flow solver | The published insertion starts at zero flow. The local base registers and signed/absolute retirement construction supply the stronger operations; [the raw-cycle bridge, Sections 2 and 6](../../manuscripts/graph-backends/raw-cycle-to-frozen-detector-bridge.md) makes their flow, cost and divergence semantics explicit. |
| Lemma 5.4 and the underlying path embeddings | Projection of a cycle to physical graph edges | The printed length inequality in Lemma 5.4 points the wrong way for the raw upper bound needed here. The local raw-lift note reconstructs physical-length domination from the actual embeddings; it does not use that inequality as written. |

The underlying embeddings come from Rasmus Kyng, Simon Meierhans and
Maximilian Probst Gutenberg, [*A Dynamic Shortest Paths Toolbox:
Low-Congestion Vertex Sparsifiers and their Applications*](https://arxiv.org/abs/2311.06402v1),
Definition 3.4, Lemma 3.21 and Algorithm 5. The
[raw-lift proof](../../manuscripts/graph-backends/distance-oracle-raw-lift.md)
tracks each traversal before cancellation and handles loops explicitly.
The [normalized repair proof](../../manuscripts/graph-backends/normalized-projected-route-composition.md)
and the lifetime construction supply the accompanying chronological
update and retirement guarantees. The complete proof uses these local
arguments rather than the public paper's printed inequality alone.

## Linked mathematical dependencies

These manuscripts construct the interfaces and prove the auxiliary
arguments used by the instantiated result. Their graph models,
parameter ranges and named published theorem dependencies remain part
of each use.

- [A numerical client independent of the ledger radix](../../manuscripts/graph-backends/decoupled-numerical-client.md)
- [Raw-cycle quality through the 2026 distance-oracle hierarchy](../../manuscripts/graph-backends/distance-oracle-raw-lift.md)
- [Exact acceptance and general-flow reductions](../../manuscripts/graph-backends/exact-flow-acceptance-and-reductions.md)
- [Numerical lifetime discipline and a loop wrapper for flat cycle oracles](../../manuscripts/graph-backends/numerical-backend-lifetime-and-loops.md)
- [A `4/5` research composition from sequential expander routing](../../manuscripts/graph-backends/quantitative-matching-4-5-composition.md)

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** icekylinx · GPT-6 Astra Pro.
