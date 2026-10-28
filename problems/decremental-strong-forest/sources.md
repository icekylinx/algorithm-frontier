# Sources and proof dependencies

## Canonical manuscripts

- [Strong forests from uncontracted Steiner cores, without recursive degree resets](proof.md)

## Linked mathematical dependencies

The generic interfaces are supplied by the local constructions and
published theorems below. The accepted no-reset forest avoids the
additional vertex-deletion interface needed by the older optional
ported-pool variant. Input models, source versions and parameter ranges
remain explicit.

| Layer | Exact dependency and boundary |
|---|---|
| Static metric provider | [The linear-parameter static construction, Sections 3–7](../../manuscripts/graph-backends/linear-parameter-static-sparsifier.md) proves (2); [the uniform source audit](../../manuscripts/graph-backends/uniform-source-interfaces-for-4-5.md) checks the growing parameters and finite arithmetic. |
| Native selected records | Main Sections 1–3 and [the metric/inventory audit, Sections 1–2 and 9](../../manuscripts/graph-backends/steiner-pool-metric-inventory-focused-audit.md) establish physical provenance, stable forest identities, active roots and chronological bound (4), including late spending of initial credit. |
| Uncontracted Steiner lift | Proves the fixed pool construction, native degree growth, typed-null handling and separate occurrence/work recurrences. All unused pools and historical isolates are counted. |
| Outer decremental covers | Uses Definition 5.2 of *A Dynamic Shortest Paths Toolbox*, named below, and the explicit-copy recurrence from Algorithm 10. Present-time overlap alone would not pay retained birth-cover ghosts. |
| Zero-length extension | Reweights an already valid positive-length flat output using a fixed perturbation and original integer lengths; it preserves topology and occurrence bounds. |
| Exact Gomory–Hu transfer | The [quantified application proof](../../manuscripts/graph-backends/gomory-hu-seven-eighths-dependency-audit.md) supplies the complete composition: finite-arithmetic packing, the Li skeleton, named exact flow and the locally proved fixed-parameter guide-tree adapter. |

The native forest bound is

<!-- math-display: a4c599ab8736bfc9981621c4
(n+m)E_{6/7}
-->
![Formula](../../assets/math/a4c599ab8736bfc9981621c4.svg)
. The exact cut-tree
application additionally removes loops, zero-capacity edges and trivial
positive-support components, and has the distinct
<!-- math-display: 515d9ca505a736ed1604df94
O(n+m)+(m+1)E_{6/7}
-->
![Formula](../../assets/math/515d9ca505a736ed1604df94.svg)
 bound. Their input/output inventories should
not be conflated.

- [Root audit of the proposed colored core-forest pool lift](../../manuscripts/graph-backends/colored-core-pool-root-audit.md)
- [Independent audit of compressed cores and colored forest pools](../../manuscripts/graph-backends/compressed-steiner-pool-independent-audit.md)
- [Finite arithmetic for the Steiner-packing client, and the Li skeleton dependency](../../manuscripts/graph-backends/finite-mwu-and-li-skeleton-independent-audit.md)
- [Independent audit of the global-max leaf repair](../../manuscripts/graph-backends/fixed-k-global-max-leaf-independent-audit.md)
- [A deterministic fixed-`k` guide-tree mincut adapter](../../manuscripts/graph-backends/deterministic-fixed-k-tree-mincut-adapter.md)
- [The fixed-`k` guide-tree mincut interface: what has and has not closed](../../manuscripts/graph-backends/fixed-k-tree-mincut-source-interface-audit.md)
- [A quantified Gomory--Hu transfer of the strong forest](../../manuscripts/graph-backends/gomory-hu-seven-eighths-dependency-audit.md)
- [Quantified outer Gomory--Hu factors and the fixed-`k` resolution](../../manuscripts/graph-backends/gomory-hu-external-factors-except-fixed-k.md)
- [A normalized static sparsifier with linear parameter dependence](../../manuscripts/graph-backends/linear-parameter-static-sparsifier.md)
- [Dynamic compression of marked subtrees: a local root audit](../../manuscripts/graph-backends/marked-steiner-compression-root-audit.md)
- [Joint public retuning for the strong forest: a conservative source audit](../../manuscripts/graph-backends/public-strong-forest-joint-retuning-audit.md)
- [Separating metric stretch, forest congestion, and work](../../manuscripts/graph-backends/separated-metric-forest-and-strong-sssp.md)
- [Independent audit of the Steiner pool: metric, inventory, and recursion](../../manuscripts/graph-backends/steiner-pool-metric-inventory-focused-audit.md)
- [Which mechanisms improve the strong-forest exponent?](../../manuscripts/graph-backends/strong-forest-mechanism-comparison.md)
- [Zero-length edges in integer distance and spanner interfaces](../../manuscripts/graph-backends/nonnegative-integer-distance-adapters.md)

## Named forest source and exact imports

Rasmus Kyng, Simon Meierhans and Maximilian Probst Gutenberg,
[*A Dynamic Shortest Paths Toolbox: Low-Congestion Vertex Sparsifiers
and their Applications*](https://arxiv.org/abs/2311.06402v1), supplies the
native sparsifier and forest framework.

| Source location | Required operation or invariant | Local boundary |
|---|---|---|
| Section 3, Algorithms 2–4 | Maintain native selected records, forests and their physical provenance | The static-provider proof establishes the improved local factors; main Sections 3–13 prove the active-root, uncontracted-pool and chronological inventory bounds. |
| Definition 5.2(1),(3), Theorem 5.3 | Decremental covers with an overlap bound over the entire history | A bound only on the currently present covers cannot pay retained birth-cover records. |
| Algorithm 10 and Claims 5.15–5.17 | Outer forest copies and their maintenance recurrence | Main Sections 11–14 supply historical ownership, explicit occurrence inventory and the separate work recurrence used in the substitution. |

The local construction establishes the new parameters using these
particular source operations. For the other public metric primitives, see the
[named APSP source map](../apsp-frontier/sources.md).

## Additional sources used only by the Gomory–Hu application

The cut-tree transfer has additional requirements beyond the forest.
They are pinned in the linked application proofs and can be located
without expanding author abbreviations:

- Amir Abboud and coauthors, [*Deterministic Almost-Linear-Time
  Gomory-Hu Trees*](https://arxiv.org/html/2507.20354v1): Section 4 and
  Algorithms 2–3 supply the Steiner-packing and terminal-sparsifier
  framework; Theorem 4.23 supplies tree packing; Algorithm 8, Appendix A,
  and Lemma 6.32 supply the outer reduction and aggregate inventory.
- Jason Li, [*Deterministic Mincut in Almost-Linear Time*](https://arxiv.org/html/2106.05513v2):
  Theorem 1.5, Claim 3.6 and Sections 3.4–3.5 supply the deterministic
  skeleton. Version 2 corrects the accuracy dependence to a seventh
  inverse power; the local finite-arithmetic proof charges that version.
- Tianyi Zhang, [*Gomory-Hu Trees in Quadratic Time*](https://arxiv.org/abs/2112.01042v1),
  Section 2.4, and the first paper's Section 5.1 supply the public
  guide-tree/centroid framework. The repository's
  [fixed-parameter adapter](../../manuscripts/graph-backends/deterministic-fixed-k-tree-mincut-adapter.md)
  proves the required leaf construction and its aggregate inventory;
  it does not infer those strengthened guarantees from a headline theorem.

- Jan van den Brand, Li Chen, Rasmus Kyng, Yang P. Liu, Simon Meierhans,
  Maximilian Probst Gutenberg and Sushant Sachdeva,
  [*Almost-Linear Time Algorithms for Decremental Graphs: Min-Cost Flow
  and More via Duality*](https://arxiv.org/html/2407.10830v1),
  Theorem 6.17 and Section 6.2 supply deterministic exact integral flow
  with leading logarithmic power <code class="math">5/6</code>, including
  final rounding. The local
  [capacity-bit reduction](../../manuscripts/graph-backends/published-flow-capacity-scaling.md)
  keeps each call's capacities at most its actual edge count and
  recovers an explicit cut. Its correctness is proved here; the fast
  solver itself remains a published external algorithm.

The [quantified transfer](../../manuscripts/graph-backends/gomory-hu-seven-eighths-dependency-audit.md)
can therefore use the published five-sixths flow theorem through the
capacity-bit adapter, as an alternative to the already constructed
four-fifths flow route. Both fit below the six-sevenths forest bound.
The source versions, fixed-parameter ranges and finite arithmetic of
the other components remain part of the theorem. The
[fixed-parameter interface review, Section 5](../../manuscripts/graph-backends/fixed-k-tree-mincut-source-interface-audit.md)
records how the global-max leaf construction closes the earlier guide-tree
gap; that historical issue is not an extra hypothesis of this application.

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
