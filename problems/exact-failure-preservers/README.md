# Exact single-failure preservers

Sparse original-element restrictions and output-sensitive reporting for exact weighted matroid intersection and rooted arborescences.

[Proof](proof.md) · [Sources](sources.md)

**Guarantee**

Preserve a minimum-cost prescribed-rank solution after every deletion of one original element, and the no-failure optimum; report infeasibility when that rank becomes unavailable.

**Objective and output**

An exact common basis, a rooted spanning arborescence, or an infeasibility answer. Reporting makes no independence or valuation calls.

**Randomness**

Deterministic preprocessing and reporting in the stated oracle model, including the valuated and arborescence variants. Randomness is not required by the distance-preserver reporting construction.

**Time**

Deterministic polynomial preprocessing. Beyond a baseline common optimum, the independence/value-test bound is:

<!-- math-display: 719e7435107ff08c8699684d
O(Nk)
-->
![Formula](../../assets/math/719e7435107ff08c8699684d.svg)

The additional arithmetic-work bound is:

<!-- math-display: 05b182418d78dd4dd1c505cb
O(Nk^2+k^3)
-->
![Formula](../../assets/math/05b182418d78dd4dd1c505cb.svg)

Arborescence arithmetic preprocessing takes:

<!-- math-display: b9d235996578dfc5ca86cac1
\widetilde O(mn)
-->
![Formula](../../assets/math/b9d235996578dfc5ca86cac1.svg)

Query work is respectively:

<!-- math-display: e9540ae1ed1bf27fec33357b
O(k)
-->
![Formula](../../assets/math/e9540ae1ed1bf27fec33357b.svg)

or, for arborescences:

<!-- math-display: 387008096a415eb2a5c95f1d
O(n)
-->
![Formula](../../assets/math/387008096a415eb2a5c95f1d.svg)

**Space**

<code class="math">O(k^{3/2})</code> retained original elements and reporting records; <code class="math">O(n^{3/2})</code> for arborescences. Exact values are charged by their actual bit length.

**Parameters**

<code class="math">N</code> is original ground size; <code class="math">k</code> is prescribed common rank; <code class="math">n,m</code> are directed vertex and arc counts. All costs and valuations remain fixed between independent queries.

**Model and representation**

Ordinary matroids use independence oracles. Valuated matroids additionally require one supplied finite-valued basis per effective domain, or independence access obtaining it, as well as rational value evaluations. Graph costs are nonnegative rational numbers.

**Lower-bound scope**

Inherited directed-distance constructions give <code class="math">\Omega(k^{4/3})</code> for weighted two-matroid restrictions and <code class="math">\Omega(n^{4/3})</code> for arborescences. Two failures require quadratic original support; approximation lower bounds allow the stated exponential cost aspect ratio.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete proof](proof.md) and [canonical manuscript map](sources.md).

## Results

**Minimum-cost common <code class="math">k</code>-set, two arbitrary matroids**

**Retained support / records.** <code class="math">O(k^{3/2})</code>

**Query output.** <code class="math">O(k)</code>

**Additional scope.** Fixed linear costs; one element deletion

**Two fixed-rank valuated matroids**

**Retained support / records.** <code class="math">O(k^{3/2})</code>

**Query output.** <code class="math">O(k)</code>

**Additional scope.** Effective-domain initialization is supplied; no smaller-rank valuation is inferred

**Rooted minimum-cost spanning arborescence**

**Retained support / records.** <code class="math">O(n^{3/2})</code>

**Query output.** <code class="math">O(n)</code>

**Additional scope.** Directed graph, one arc deletion; <code class="math">\widetilde O(mn)</code> preprocessing

**Minimum-cost maximum-cardinality common set**

**Retained support / records.** <code class="math">O(r^{3/2})</code>

**Query output.** <code class="math">O(r)</code>

**Additional scope.** Union of the <code class="math">r</code> and <code class="math">r-1</code> constructions; ordinary linear costs

**Two-failure exact matching/arborescence obstruction**

**Retained support / records.** <code class="math">\Omega(r^2)</code> / <code class="math">\Omega(n^2)</code>

**Query output.** Lower bound

**Additional scope.** Retained original elements/arcs

**Two-failure approximate arborescence obstruction**

**Retained support / records.** <code class="math">\Omega(n^2)</code>

**Query output.** Lower bound

**Additional scope.** Every fixed multiplicative factor; polynomial-bit costs with exponential aspect ratio

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
