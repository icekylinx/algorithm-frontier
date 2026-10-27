# Sources and proof dependencies: Exact single-failure preservers

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Arborescence and matroid-intersection preservers](manuscripts/exact-single-failure-arborescences-and-matroid-intersection.md) | Weighted exchange-cycle identities, minimum-hop repairs, distance-preserver reporting, sparse arborescence implementation, and lower bounds. |
| [Valuated matroid intersection](manuscripts/valuated-matroid-intersection.md) | Exchange lengths, feasible-domain initialization, exact rational oracle access, and the valuated reporting extension. |
| [Supplied-baseline arborescence realization](manuscripts/reference-arborescence-reporting.md) | Matches the executable heavy-light auxiliary graph, exact dense shortest paths, phased greedy hubs and original-ID reports to the ordinary companion. |

The [reference API](reference/README.md) requires a supplied optimum rooted
directed spanning arborescence. It implements preprocessing and queries after
that supply; the independent checker's tiny exhaustive baseline enumeration
is not a general baseline algorithm. General oracle-matroid and valuated
reporting remain mathematical constructions with separate initialization
and oracle models.

## External inputs

- Bodwin, [A Note on Distance-Preserving Graph Sparsification](https://arxiv.org/pdf/2001.07741), Theorem 3 and Lemma 1: the pairwise distance-preserver input and its path-reporting use. Theorem 3 attributes the underlying bound to Coppersmith and Elkin.
- Goemans, [Lecture Notes on Matroid Intersection](https://math.mit.edu/~goemans/18453S17/matroid-intersect-notes.pdf): basis-exchange matching, the common-independent-set polytope, and the graphic/partition formulation.
- The valuated companion states the precise shortest-path and oracle prerequisites of its cited valuated-intersection algorithm. It also separates comparison results, including [Low-Cost Arborescence Under Edge Faults](https://arxiv.org/html/2605.13800v1), from inputs to the proof.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
