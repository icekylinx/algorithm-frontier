# Sources and proof dependencies

## Canonical manuscripts

- [Fully dynamic all-pairs distances: a time–stretch theorem](proof.md)

## Linked mathematical dependencies

Theorem 2.1 states the generic hierarchy implication; Corollary 2.2
instantiates it with the constructions below. Their graph models,
growing-parameter ranges and named public theorem dependencies remain
part of each use.

| Dependency | Exact obligation |
|---|---|
| Normalized local metric provider | [Linear-parameter static sparsifier, Sections 3–7](../../manuscripts/graph-backends/linear-parameter-static-sparsifier.md) constructs the quality, work and selected-record bounds in (1), with constants uniform in the growing integer parameters. |
| Hierarchy and lifetime accounting | [Normalized repair](../../manuscripts/graph-backends/normalized-projected-route-composition.md) and [the separated metric hierarchy, Sections 2–7](../../manuscripts/graph-backends/separated-metric-forest-and-strong-sssp.md) prove (2), actual base-table costs, late spending of initial credit and stable pivot handles. |
| Query interface | Reads a settled deterministic hierarchy in polynomial logarithmic time on adaptive histories. The result is a number, not an explicit all-pairs matrix or an output-sensitive simple path. |
| Degree-three proxy | Main Lemma 4.1 gives a local incidence-tree proof and charges every allocated connector; it never allocates a full cap-sized port tree per vertex. |
| Nonnegative integer extension | Main Corollary 6.1 applies the constructed positive-length oracle with an explicit full-stretch bound on a predeclared transformed length range. Exact flooring preserves zero distances. |

- [Joint retuning of the public deterministic APSP construction](../../manuscripts/graph-backends/public-apsp-joint-retuning-audit.md)
- [A stronger public APSP comparison at exactly the same stretch scale](../../manuscripts/graph-backends/same-stretch-apsp-comparison-and-root-audit.md)
- [Separating metric stretch, forest congestion, and work](../../manuscripts/graph-backends/separated-metric-forest-and-strong-sssp.md)
- [Uniform source interfaces and finite-bit constructions](../../manuscripts/graph-backends/uniform-source-interfaces-for-4-5.md)
- [Zero-length edges in integer distance and spanner interfaces](../../manuscripts/graph-backends/nonnegative-integer-distance-adapters.md)

## Named public sources and the operations they supply

The main hierarchy source is Rasmus Kyng, Simon Meierhans and Maximilian
Probst Gutenberg, [*A Dynamic Shortest Paths Toolbox: Low-Congestion Vertex
Sparsifiers and their Applications*](https://arxiv.org/abs/2311.06402v1).
Section 3.2 gives the pivot/ball/core construction; Claims 3.17–3.18
separate selected-edge changes from embedding work; Algorithm 6 and
Claim 4.4 supply numerical distance queries. These particular locations
matter because metric stretch alone does not imply a maintenance bound
or an output-sensitive path routine.

The [public retuning proof](../../manuscripts/graph-backends/public-apsp-joint-retuning-audit.md)
also uses the following pinned ingredients:

| Paper | Exact location | Operation used in the public comparison |
|---|---|---|
| Chuzhoy, Gao, Li, Nanongkai, Peng and Saranurak, [*A Deterministic Algorithm for Balanced Cut with Applications to Dynamic Connectivity, Flows, and Beyond*](https://arxiv.org/html/1910.08025v2) | Theorems 1.6, 2.4–2.5 and 5.1 | A deterministic cut player, auxiliary expanders and a balanced-cut construction; construction cost is kept separate from resulting conductance. |
| Julia Chuzhoy and Thatchaphol Saranurak, [*Deterministic Algorithms for Decremental Shortest Paths via Layered Core Decomposition*](https://arxiv.org/html/2009.08479v1) | Theorem B.9; Theorem 3.7 and Lemmas 3.10–3.11 | Terminal routing in expanders and the stage/path recurrences of the decremental path oracle. |
| Jan van den Brand and coauthors, [*A Deterministic Almost-Linear Time Algorithm for Minimum-Cost Flow*](https://arxiv.org/html/2309.16629v1) | Theorems 8.1–8.2, Algorithm 4, Theorems 8.4–8.6 and Appendix B | Deterministic static sparsification with an ambient embedding and the stated repair reduction. |
| Li Chen, Rasmus Kyng, Yang P. Liu, Richard Peng, Maximilian Probst Gutenberg and Sushant Sachdeva, [*Maximum Flow and Minimum-Cost Flow in Almost-Linear Time*](https://arxiv.org/pdf/2203.00671v1) | Section 5.1, Algorithm 1, Claims 5.7–5.8 and Lemma 5.9 | The touched-set repair hierarchy. Its randomized static provider is replaced by the preceding deterministic one. |

The improved normalized local factors are proved by the local static
sparsifier, sequential router and repair constructions linked above.
They are not attributed to the public theorems' original parameter
specializations. The comparison note separately reconstructs the public
parameter envelope within its allowed ranges. Its matched comparison
concerns these named families; it is not a lower bound on all dynamic
APSP algorithms.

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
