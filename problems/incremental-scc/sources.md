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

**Public starting point.** The contraction principle is from
[Chen–Kyng–Liu–Meierhans–Probst Gutenberg, arXiv:2311.18295v1](https://arxiv.org/html/2311.18295v1),
Section 8.3 and Theorem 1.8. The present client uses one logarithmic
barrier and explicit endpoint retargeting. Its claimed exponent requires
the separately stated quantitative backend assumptions.

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
