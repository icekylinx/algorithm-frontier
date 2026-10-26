# Sources and proof dependencies

## Canonical manuscripts

- [Incremental SCCs with a one-sided logarithmic flow barrier](proof.md)

## Dependency status

**Proved local facts.** Section 3 proves that a sufficiently positive
coordinate of a nearly nonnegative exact circulation joins vertices
within one true SCC. Sections 7 and 9 prove the small-to-large labeling
account and the exact quotient-partition argument. Corollary 9.1 gives
the faster first-coalescence query from two short label histories, once
an exact merge sequence is supplied. Its
[finite checker](verify/check_label_history.py) covers batched merge
histories independently of a numerical SCC algorithm.

**Constructed raw backend and exact maintenance.** Section 1 first gives
the generic SCC client and then instantiates it with
[the quantitative construction, Sections 1–7](../../manuscripts/graph-backends/quantitative-matching-4-5-composition.md).
The [raw-cycle bridge, Sections 2 and 6](../../manuscripts/graph-backends/raw-cycle-to-frozen-detector-bridge.md)
represents a logical flow as an explicit base plus all live and dormant
occurrence registers. New occurrences start at zero; a prescribed
nonzero logical value is stored in the base. The
[lifetime construction, Sections 1–4](../../manuscripts/graph-backends/numerical-backend-lifetime-and-loops.md)
transfers signed and absolute registers before retiring old metadata.
Main Section 7 combines these operations into an atomic endpoint change
that preserves surviving flows and is paid by small-to-large incidence
scans. The [uniform source audit](../../manuscripts/graph-backends/uniform-source-interfaces-for-4-5.md)
names the deterministic public inputs and their local parameter adapters.

**Public starting point.** The contraction principle is from Li Chen,
Rasmus Kyng, Yang P. Liu, Simon Meierhans and Maximilian Probst Gutenberg,
[*Almost-Linear Time Algorithms for Incremental Graphs: Cycle Detection,
SCCs, s–t Shortest Path, and Minimum-Cost Flow*](https://arxiv.org/html/2311.18295v1),
Section 8.3 and Theorem 1.8. The public theorem supplies deterministic
almost-linear SCC maintenance. The present client uses one logarithmic
barrier and explicit endpoint retargeting; its sharper displayed exponent
uses the separately constructed quantitative backend.

| Operation | Source of the guarantee | Boundary |
|---|---|---|
| Contract vertices certified by circulation flow | The incremental-graphs paper, Section 8.3; local Section 3 supplies the near-nonnegativity argument | The public theorem does not establish the new one-barrier running-time calculation. |
| Insert a logical edge with positive base flow, retire it exactly, or retarget its endpoints | Raw-cycle bridge Sections 2 and 6; lifetime construction Sections 1–4; main Section 7 | The local base and retirement registers supply the stronger operations. They are not inferred from the public solver's zero-flow insertion rule. |
| Maintain settled labels and answer first-coalescence queries | Main Sections 7 and 9, Corollary 9.1, and the local history checker | Requires an exact merge sequence; it has no numerical-cycle dependency of its own. |

The relevant public cycle engine is Rasmus Kyng, Simon Meierhans,
Maximilian Probst Gutenberg and Aurelio Sulser,
[*A Simpler and Faster Min-Cost Flow Solver via Min-Ratio Cycles from
Distance Oracles*](https://arxiv.org/html/2609.23852v1), Theorems 4.4–4.5
and Definition 5.1. It supplies its own published hierarchy parameters.
Definition 5.1's insertion starts at zero flow; it does not by itself
implement the stronger row above or prove the new exponent.

**Output boundary.** LOW certifies an acyclic quotient but does not
return a maintained topological potential. Topological order and
within-component path witnesses are excluded from the displayed SCC
and label-history bounds.

## Linked mathematical dependencies

The linked constructions supply the generic client's required operations.
Their numerical ranges, adaptive-history model and named published
theorem dependencies remain part of the instantiated result.

- [A direct exact solver for small local detector instances](../../manuscripts/graph-backends/small-local-detector-exact-solver.md)
- [Topological ordering: a valid transpose reduction and its missing interface](../../manuscripts/graph-backends/topological-order-transpose-interface-gap.md)

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
