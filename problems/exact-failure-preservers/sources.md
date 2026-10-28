# Sources and proof dependencies: Exact single-failure preservers

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Arborescence and matroid-intersection preservers](manuscripts/exact-single-failure-arborescences-and-matroid-intersection.md) | Weighted exchange-cycle identities, minimum-hop repairs, distance-preserver reporting, sparse arborescence implementation, and lower bounds. |
| [Valuated matroid intersection](manuscripts/valuated-matroid-intersection.md) | Exchange lengths, feasible-domain initialization, exact rational oracle access, and the valuated reporting extension. |
| [Supplied-baseline arborescence realization](manuscripts/reference-arborescence-reporting.md) | Matches the executable heavy-light auxiliary graph, exact dense shortest paths, phased greedy hubs and original-ID reports to the ordinary companion. |
| [Initialized ordinary two-matroid realization](manuscripts/reference-ordinary-matroid-reporting.md) | Ordinary signed-cost initialization, cheapest compressed exchanges, canonical hub reporting, and the automatically initialized nonnegative rooted-arborescence wrapper. |

The [reference API](reference/README.md) now supplies ordinary two-matroid
initialization through the canonical
[weighted-intersection primitive](../robust-bounded-certificates/reference/bounded.py).
Its exact source is Bárász, Bérczi, Király, Oki, Yamaguchi and Yokoi,
[*Matroid Intersection under Minimum Rank Oracle*, arXiv version two,
Definition 2.2, Algorithm 2 and Lemma 2.5](https://arxiv.org/html/2407.03229v2#S2).
The initialized graph wrapper uses that same optimum to discharge the
lower-level HLD entry point's supplied-baseline promise. Tiny exhaustive
enumeration is only an independent comparator, not the initializer.
Valuated reporting retains its separate mathematical construction,
initialization and value-oracle model.

## External inputs

- Bodwin, [A Note on Distance-Preserving Graph Sparsification](https://arxiv.org/pdf/2001.07741), Theorem 3 and Lemma 1: the pairwise distance-preserver input and its path-reporting use. Theorem 3 attributes the underlying bound to Coppersmith and Elkin.
- Goemans, [Lecture Notes on Matroid Intersection](https://math.mit.edu/~goemans/18453S17/matroid-intersect-notes.pdf): basis-exchange matching, the common-independent-set polytope, and the graphic/partition formulation.
- The valuated companion states the precise shortest-path and oracle prerequisites of its cited valuated-intersection algorithm. It also separates comparison results, including [Low-Cost Arborescence Under Edge Faults](https://arxiv.org/html/2605.13800v1), from inputs to the proof.

**Attribution:** icekylinx and GPT-6 Astra Pro.


## Certified valuated and ordinary rank-drop realization

- [Realization and bounded audit](manuscripts/reference-valuated-and-rank-drop.md):
  original split-price optimality certificates, the complete fixed-rank valued
  exchange/reporting proof, and the ordinary two-consecutive-rank wrapper.
- [Native interfaces](reference/README.md), [valuated source](reference/valuated_reporting.py)
  and [independent original-input checker](verify/check_valuated_rank_drop.py).
- [Iwamasa and Takazawa, arXiv:2003.02424v3](https://arxiv.org/pdf/2003.02424),
  Lemma 7, printed page 9: the classical mathematical valuated initializer.
  Native software validates a supplied common optimum, rather than implementing
  that initializer or inferring a smaller-rank valuation.
