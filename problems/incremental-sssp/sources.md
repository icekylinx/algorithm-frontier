# Sources and proof dependencies

## Canonical manuscripts

- [Incremental directed SSSP from the frozen-barrier detector](proof.md)

## Linked mathematical dependencies

These manuscripts contain the interfaces, auxiliary arguments or source
comparisons referenced by this result. Their stated hypotheses remain
part of each use; an interface analysis does not supply an omitted backend.

| Dependency | Exact role and remaining obligation |
|---|---|
| Frozen-barrier detector | A settled LOW answer must respect the residual divergence after frozen logical edges retire. Frozen costs remain in the affine objective, and raw copies, callbacks, births and price changes must all be charged. The full numerical implementation is still an explicit premise. |
| Outer reduction, main Sections 3–9 | Proves reachable-vertex activation, changing-demand phase counts, child quotas, uniform integer ranges and the placement of the raw loss only once in the exponent. It is deterministic given the detector interface. |
| Tree-segment reporting | Gives its own sparse four-coordinate index and loop-removal construction. It needs immutable current phase trees, ancestor/descendant version ownership and charged index construction, rather than a distance-only oracle. |
| Nonnegative-integer extension, main Section 10.1 | Uses fixed positive perturbation and exact flooring. It adds no dynamic SCC primitive and makes no claim for arbitrary real or negative lengths. |

- [A distance-decrease detector with frozen auxiliary barriers](../../manuscripts/graph-backends/frozen-barrier-distance-detector.md)
- [Simple-path reporting from a logarithmic number of tree segments](../../manuscripts/graph-backends/simple-path-reporting-from-tree-segments.md)
- [Exact small-instance solver for the frozen detector](../../manuscripts/graph-backends/small-local-detector-exact-solver.md)

The small-instance note supplies a deterministic Bellman–Ford based
alternative for the explicitly bounded local base cases. It closes
that base-case dependency only; it does not replace the fast raw
interface on large instances.

## Primary references and comparison scope

[Liu, arXiv:2506.19207v1, Sections 3–4](https://arxiv.org/html/2506.19207v1)
is the public starting point for the incremental SSSP reduction.
The frozen-barrier retirement argument, its reporting budget, and the
tree-segment output construction are the local additions in this
repository. The public theorem is not cited as a proof of those additions.

The comparison with the public $`20/21`$ raw engine cites
[arXiv:2609.23852v1](https://arxiv.org/html/2609.23852v1). That comparison
still requires the stated raw-interface composition check. A numerical
objective solver alone does not provide exact nonzero-flow retirement
or output-sensitive path reporting.

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
