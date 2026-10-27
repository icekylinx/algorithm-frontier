# Exact correlated-failure cuts and whole-block quotients

A polynomial label decoder turns every permitted failure and query into an ordinary quotient query. One nonnegative coefficient per original item then works simultaneously for all queries, including those chosen after the summary is revealed.

## Results

Write

<!-- math-display: 3d659e4d96e4f0cbcef9263c
S(D,\varepsilon)=O\!\left(\min\left\{m,\frac{D\log(2D/\varepsilon)}{\varepsilon^2}\right\}\right).
-->
![Formula](../../assets/math/3d659e4d96e4f0cbcef9263c.svg)

All constructions below are Monte Carlo randomized polynomial time in the explicit compact matrix/graph input and inverse accuracy. One event of probability at least <code class="math">2/3</code> covers every allowed failure and the entire query family, including queries selected after the output. The exact polynomial decoder and field-extension steps are deterministic; a failed sampling event can silently violate an approximation guarantee.

**Ordinary normalized monotone submodular quotients of rank <code class="math">r</code>, positive marginals at least one**

**Lifted rank parameter <code class="math">D</code>.** <code class="math">r</code>

**Retained support and output.** Original items:

<!-- math-display: 6bc25c9dede4850a310135b8
S(r,\varepsilon)
-->
![Formula](../../assets/math/6bc25c9dede4850a310135b8.svg)

Backend calls:

<!-- math-display: 9bd553d56797a32a14b94d9d
O(\log\log(2m))
-->
![Formula](../../assets/math/9bd553d56797a32a14b94d9d.svg)

**Proof.** [Adaptive resparsification theorem](manuscripts/adaptive-quotient-resparsification.md)

**Represented columns or whole represented subspaces with incidence label deficit at most <code class="math">k</code>**

**Lifted rank parameter <code class="math">D</code>.** <code class="math">r\binom{h+k}{k}</code>

**Retained support and output.** Original columns or whole blocks preserve all subspace-complement queries. Their support bound is:

<!-- math-display: 02702298cf7b5742f431f05e
S(D,\varepsilon)
-->
![Formula](../../assets/math/02702298cf7b5742f431f05e.svg)

**Proof.** [Column theorem](manuscripts/exact-label-cut-and-matroid-quotient-sparsification.md), [Theorem B1](manuscripts/exact-label-whole-blocks-and-hyperedges.md)

**Undirected graph: at most <code class="math">a</code> labels per vertex and <code class="math">b</code> additional labels per edge**

**Lifted rank parameter <code class="math">D</code>.** <code class="math">(n-c)\binom{h+a+b}{a+b}</code>

**Retained support and output.** Retained edges preserve every cut after every allowed failure. Their support bound is:

<!-- math-display: 02702298cf7b5742f431f05e
S(D,\varepsilon)
-->
![Formula](../../assets/math/02702298cf7b5742f431f05e.svg)

**Proof.** [Equation EC1](manuscripts/exact-label-cut-and-matroid-quotient-sparsification.md)

**One vertex color per graph vertex, no additional edge labels**

**Lifted rank parameter <code class="math">D</code>.** <code class="math">(n-c)(h+1)</code>

**Retained support and output.** Retain original edges with one fixed coefficient each, with support bound:

<!-- math-display: 02702298cf7b5742f431f05e
S(D,\varepsilon)
-->
![Formula](../../assets/math/02702298cf7b5742f431f05e.svg)

**Proof.** [Equation EC2](manuscripts/exact-label-cut-and-matroid-quotient-sparsification.md)

**Hyperedges of size at most <code class="math">t</code>, with at most <code class="math">a</code> vertex labels and <code class="math">b</code> additional item labels**

**Lifted rank parameter <code class="math">D</code>.** <code class="math">(n-c)\binom{h+a(t-1)+b}{a(t-1)+b}</code>

**Retained support and output.** Whole hyperedges preserve cuts and partition-crossing objectives, with support bound:

<!-- math-display: 02702298cf7b5742f431f05e
S(D,\varepsilon)
-->
![Formula](../../assets/math/02702298cf7b5742f431f05e.svg)

**Proof.** [Equation B6](manuscripts/exact-label-whole-blocks-and-hyperedges.md)

**Whole hedges, with at most <code class="math">d</code> labels per hedge**

**Lifted rank parameter <code class="math">D</code>.** At most <code class="math">(n-c)\binom{h+d}{d}</code>

**Retained support and output.** Whole hedges have the following support bound, with no factor for the number of constituent edges:

<!-- math-display: 02702298cf7b5742f431f05e
S(D,\varepsilon)
-->
![Formula](../../assets/math/02702298cf7b5742f431f05e.svg)

**Proof.** [Equation B9](manuscripts/exact-label-whole-blocks-and-hyperedges.md)

**Globally commuting prime-dimensional stabilizer blocks, at most <code class="math">d</code> labels per block**

**Lifted rank parameter <code class="math">D</code>.** <code class="math">(n+1)\binom{h+d}{d}</code>

**Retained support and output.** Whole blocks simultaneously preserve all-state energy and the kernel, with support bound:

<!-- math-display: 02702298cf7b5742f431f05e
S(D,\varepsilon)
-->
![Formula](../../assets/math/02702298cf7b5742f431f05e.svg)

**Proof.** [Equations B10–B11](manuscripts/exact-label-whole-blocks-and-hyperedges.md)

## Contract

**Objective and output**

One original-item reweighting preserving every stated cut, partition, represented quotient, or commuting-block energy after all sets of at most <code class="math">h</code> failed labels.

**Randomness**

Monte Carlo randomized preprocessing, with success probability at least <code class="math">2/3</code> for one event covering every allowed failure and quotient/cut query. Queries and failed labels may be chosen after the summary is revealed. The exact label decoder and field-extension arithmetic are deterministic.

**Time**

Polynomial in explicit compact input length and <code class="math">\varepsilon^{-1}</code>; the construction returns the whole input before materializing a lift whose dimension exceeds the item count. No failure set is enumerated.

**Space**

Lifted rank bounds and retained support are separate from workspace. Only the polynomial-sized capped lift is materialized; no independent optimized space bound is claimed.

**Parameters**

<code class="math">m</code> counts original items, <code class="math">r</code> is original concatenated-column rank, <code class="math">c</code> counts positive-input components including isolated vertices, <code class="math">h</code> is the failure budget, and <code class="math">k</code> bounds item labels absent from an incident row.

**Model and representation**

Explicit rational or finite-field matrices and rational item weights. A failed vertex deletes every incident hyperedge as a whole. A partition charges a crossing hyperedge once. Stabilizer failure results require global commutation.

**Lower-bound scope**

Simple unweighted graph and hypergraph families require <code class="math">\Omega\!\left(\frac{n\binom{h+k}{k}}{\varepsilon^2}\right)</code> original items in the stated large-<code class="math">n</code> regimes. Repeated labeled commuting-check families require <code class="math">\Omega\!\left(\frac{n\binom{h+d}{d}}{\varepsilon^2}\right)</code> when <code class="math">n\ge2\left\lceil\varepsilon^{-2}\right\rceil</code>. These are support lower bounds allowing arbitrary nonnegative output weights.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Proofs](proof.md), [manuscript and reference map](sources.md), [decoder review](verify/README.md), [finite evidence](verify/README.md).

The graph theorem concerns cuts; [spectral and seminorm summaries](../correlated-spectral-regression/) have separate guarantees and parameter bounds.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
