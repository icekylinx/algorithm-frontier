# Sources and proof dependencies

## Canonical manuscripts

- [Incremental directed SSSP from the frozen-barrier detector](proof.md)

## Linked mathematical dependencies

These manuscripts construct the detector and reporting interfaces used
by the main theorem. The generic reduction and its four-fifths
instantiation are stated separately; the numerical ranges, graph model
and named deterministic public inputs remain explicit.

| Dependency | Construction and scope |
|---|---|
| Frozen-barrier detector | The detector proof and [raw-cycle bridge, Sections 2–8](../../manuscripts/graph-backends/raw-cycle-to-frozen-detector-bridge.md) preserve residual divergence and frozen costs, prove sound LOW thresholds and charge copies, callbacks, births and price changes. This is the constructed numerical interface used by the main theorem. |
| Outer reduction, main Sections 3–9 | Proves reachable-vertex activation, changing-demand phase counts, child quotas, uniform integer ranges and the placement of the raw loss only once in the exponent. It is deterministic given the detector interface. |
| Tree-segment reporting | Gives its own sparse four-coordinate index and loop-removal construction. It needs immutable current phase trees, ancestor/descendant version ownership and charged index construction, rather than a distance-only oracle. |
| Nonnegative-integer extension, main Section 10.1 | Uses fixed positive perturbation and exact flooring. It adds no dynamic SCC primitive and makes no claim for arbitrary real or negative lengths. |

- [A distance-decrease detector with frozen auxiliary barriers](../../manuscripts/graph-backends/frozen-barrier-distance-detector.md)
- [From the raw-cycle backend to the frozen-barrier detector](../../manuscripts/graph-backends/raw-cycle-to-frozen-detector-bridge.md)
- [The quantitative backend construction, Sections 1–7](../../manuscripts/graph-backends/quantitative-matching-4-5-composition.md)
- [Uniform deterministic source algorithms and finite-bit adapters](../../manuscripts/graph-backends/uniform-source-interfaces-for-4-5.md)
- [Simple-path reporting from a logarithmic number of tree segments](../../manuscripts/graph-backends/simple-path-reporting-from-tree-segments.md)
- [Exact small-instance solver for the frozen detector](../../manuscripts/graph-backends/small-local-detector-exact-solver.md)

The small-instance note supplies a deterministic Bellman–Ford based
alternative for the explicitly bounded local base cases. It closes
the bounded local base cases. The quantitative raw construction supplies
the larger instances without padding them to the global size.

## Primary references and comparison scope

Yang P. Liu's [*Incremental Shortest Paths in Almost Linear Time via a
Modified Interior Point Method*](https://arxiv.org/html/2506.19207v1),
Sections 3–4, is the public starting point for the incremental SSSP reduction.
The frozen-barrier retirement argument, its reporting budget, and the
tree-segment output construction are the local additions in this
repository. The public theorem is not cited as a proof of those additions.

The public cycle engine is Rasmus Kyng, Simon Meierhans, Maximilian
Probst Gutenberg and Aurelio Sulser, [*A Simpler and Faster Min-Cost Flow
Solver via Min-Ratio Cycles from Distance Oracles*](https://arxiv.org/html/2609.23852v1).
Its Theorems 4.4–4.5 supply the published <code class="math">20/21</code> hierarchy scale;
Definition 5.1 and Theorem 5.2 give the numerical interface and solver.
Definition 5.1 inserts new edges at zero flow. Neither that interface
nor a numerical objective bound supplies exact nonzero-flow retirement
or an output-sensitive simple path.

The detector's local Section 5 now proves the needed approximate
potential directly by difference constraints: the absence of a sufficiently
negative circulation implies no negative cycle in a bidirected constraint
graph, whose shortest-path labels satisfy both edge inequalities. This is
an existence proof for the analysis; it does not call an uncharged fast
shortest-path routine. The local tree-segment manuscript separately proves
the reporting algorithm and its construction/output charges. The
raw-cycle bridge supplies exact base registers, residual-demand
retirement, a fixed-cost path aggregate, integer pricing and its refresh
account. These local constructions complete the instantiated theorem;
the public zero-insertion flow interface alone is not being claimed to
supply the stronger operations.

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
