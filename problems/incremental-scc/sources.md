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

**Raw backend and maintenance hypothesis.** Section 1 requires more than
a minimum-ratio approximation: nonzero-base logical edge insertion,
exact point reads, complete signed/absolute retirement transfers,
preservation of surviving flow values, and atomic endpoint retargeting
must fit the declared cap. These remain conditions of the fast SCC
algorithm, including the proposed raw realization in
[the required deterministic cycle-search implementation](../general-matching/proof.md#116-explicit-raw-backend-realization-contract).
The direct small-instance solver below covers its stated local cutoff;
it does not realize the large-instance hierarchy.

**Public starting point.** The contraction principle is from Li Chen,
Rasmus Kyng, Yang P. Liu, Simon Meierhans and Maximilian Probst Gutenberg,
[*Almost-Linear Time Algorithms for Incremental Graphs: Cycle Detection,
SCCs, s–t Shortest Path, and Minimum-Cost Flow*](https://arxiv.org/html/2311.18295v1),
Section 8.3 and Theorem 1.8. The public theorem supplies deterministic
almost-linear SCC maintenance. The present client uses one logarithmic
barrier and explicit endpoint retargeting; its sharper displayed exponent
requires the separately stated quantitative backend assumptions.

| Operation | Source of the guarantee | Boundary |
|---|---|---|
| Contract vertices certified by circulation flow | The incremental-graphs paper, Section 8.3; local Section 3 supplies the near-nonnegativity argument | The public theorem does not establish the new one-barrier running-time calculation. |
| Insert a logical edge with positive base flow, retire it exactly, or retarget its endpoints | Explicit implementation requirements in main Section 1 | The distance-oracle flow solver below only specifies zero-flow insertion. These stronger operations remain unresolved at the required cost. |
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

These manuscripts contain the interfaces, auxiliary arguments or source
comparisons referenced by this result. Their stated hypotheses remain
part of each use; an interface analysis does not supply an omitted backend.

- [A direct exact solver for small local detector instances](../../manuscripts/graph-backends/small-local-detector-exact-solver.md)
- [Topological ordering: a valid transpose reduction and its missing interface](../../manuscripts/graph-backends/topological-order-transpose-interface-gap.md)

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
