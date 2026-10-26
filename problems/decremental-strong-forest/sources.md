# Sources and proof dependencies

## Canonical manuscripts

- [Strong forests from uncontracted Steiner cores, without recursive degree resets](proof.md)

## Linked mathematical dependencies

These manuscripts contain the interfaces, auxiliary arguments or source
comparisons referenced by this result. Their stated hypotheses remain
part of each use; an interface analysis does not supply an omitted backend.

| Layer | Exact dependency and boundary |
|---|---|
| Static metric provider | The normalized quality and construction bounds in (2) are research premises. Their constants must be uniform in the growing parameters. |
| Native selected records | Requires stable forest identities, physical edge provenance, active-root events and the chronological bound (4), including initial credit used later. A distance-only sparsifier does not supply this transcript. |
| Uncontracted Steiner lift | Proves the fixed pool construction, native degree growth, typed-null handling and separate occurrence/work recurrences. All unused pools and historical isolates are counted. |
| Outer decremental covers | Uses Definition 5.2 of *A Dynamic Shortest Paths Toolbox*, named below, and the explicit-copy recurrence from Algorithm 10. Present-time overlap alone would not pay retained birth-cover ghosts. |
| Zero-length extension | Reweights an already valid positive-length flat output using a fixed perturbation and original integer lengths; it preserves topology and occurrence bounds. |
| Exact Gomory–Hu transfer | Separately needs exact flow, finite-arithmetic packing, the Li skeleton and fixed-parameter guide-tree interfaces. The forest improvement alone is insufficient. |

The native forest bound is <code class="math">(n+m)E_{6/7}</code>. The exact cut-tree
application additionally removes loops, zero-capacity edges and trivial
positive-support components, and has the distinct
<code class="math">O(n+m)+(m+1)E_{6/7}</code> bound. Their input/output inventories should
not be conflated.

- [Root audit of the proposed colored core-forest pool lift](../../manuscripts/graph-backends/colored-core-pool-root-audit.md)
- [Independent audit of compressed cores and colored forest pools](../../manuscripts/graph-backends/compressed-steiner-pool-independent-audit.md)
- [Finite arithmetic for the Steiner-packing client, and the Li skeleton dependency](../../manuscripts/graph-backends/finite-mwu-and-li-skeleton-independent-audit.md)
- [Independent audit of the global-max leaf repair](../../manuscripts/graph-backends/fixed-k-global-max-leaf-independent-audit.md)
- [A deterministic fixed-k guide-tree mincut adapter](../../manuscripts/graph-backends/deterministic-fixed-k-tree-mincut-adapter.md)
- [The fixed-k guide-tree mincut interface: what has and has not closed](../../manuscripts/graph-backends/fixed-k-tree-mincut-source-interface-audit.md)
- [A quantified Gomory--Hu transfer of the strong forest](../../manuscripts/graph-backends/gomory-hu-seven-eighths-dependency-audit.md)
- [Quantified outer Gomory--Hu factors and the fixed-k resolution](../../manuscripts/graph-backends/gomory-hu-external-factors-except-fixed-k.md)
- [A normalized static sparsifier with linear parameter dependence](../../manuscripts/graph-backends/linear-parameter-static-sparsifier.md)
- [Dynamic compression of marked subtrees: a local root audit](../../manuscripts/graph-backends/marked-steiner-compression-root-audit.md)
- [Joint public retuning for the strong forest: a conservative source audit](../../manuscripts/graph-backends/public-strong-forest-joint-retuning-audit.md)
- [Separating metric stretch, forest congestion, and work](../../manuscripts/graph-backends/separated-metric-forest-and-strong-sssp.md)
- [Compressed Steiner cores and colored full-forest pools](../../manuscripts/graph-backends/steiner-colored-pool-strong-forest-candidate.md)
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
| Section 3, Algorithms 2–4 | Maintain native selected records, forests and their physical provenance | The improved local factors and uncontracted pools are proved or assumed separately in the main manuscript. |
| Definition 5.2(1),(3), Theorem 5.3 | Decremental covers with an overlap bound over the entire history | A bound only on the currently present covers cannot pay retained birth-cover records. |
| Algorithm 10 and Claims 5.15–5.17 | Outer forest copies and their maintenance recurrence | The new pool construction must supply its explicit occurrence inventory before this recurrence is substituted. |

The source's headline theorem does not establish the proposed new
parameters. For the other public metric primitives, see the
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

Exact flow remains a separate named input to the
[quantified transfer](../../manuscripts/graph-backends/gomory-hu-seven-eighths-dependency-audit.md).
The source versions, fixed-parameter ranges and finite arithmetic remain
part of the application's assumptions.

## Evidence and provenance

The [verification note](verify/README.md) states the scope of executable
evidence and the remaining mathematical dependencies. The
[import record](../../provenance/README.md) preserves source revisions,
canonical paths, attribution and applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
