# Exact flow, matching, and price sensitivity

Original-subinstance certificates and reporting structures for independent single failures or single price changes.

[Proof](proof.md) · [Sources](sources.md)

**Guarantee**

Exact surviving optimum or cardinality for each model below; each result has its own failure/change semantics and parameters.

**Objective and output**

Minimum-cost unit flows and path packings; exact cardinality matchings; common independent sets; and exact prescribed-rank price-change optima.

**Randomness**

Deterministic preprocessing and queries in each stated flow, matching, matroid and price-sensitivity model; the required exact optimization and independence oracles retain their specified costs.

**Time**

Flow and vertex-disjoint paths: deterministic <code class="math">\widetilde O(mn)</code> arithmetic preprocessing. General matching and oracle matroids: deterministic polynomial preprocessing. Price sensitivity beyond a baseline optimum uses <code class="math">O(Nr)</code> independence tests and <code class="math">O(Nr^2+r^3)</code> arithmetic work. Query bounds are listed separately.

**Space**

Support and reporting records are listed below. Rational values occupy their actual bit length; construction workspace and external oracle storage are separate.

**Parameters**

<code class="math">n,m</code> are graph sizes; <code class="math">\lambda</code> is a feasible flow value; <code class="math">s_x</code> is a fixed optimum flow support; <code class="math">\mu</code> is graph matching number; <code class="math">N,r</code> are matroid ground size and prescribed rank.

**Model and representation**

Simple directed unit-capacity graphs with nonnegative rational costs for the uniform flow exponent; loopless undirected general graphs for cardinality matching; independence-oracle matroids for intersection. All queries are independent relative to the preprocessed input.

**Lower-bound scope**

General-matching certificates preserve cardinality, not every increased replacement cost. Integrality alone does not imply a linear certificate: the manuscript gives a quadratic retained-vertex obstruction for maximum independent set even in perfect graphs.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete proof](proof.md) and [canonical manuscript map](sources.md).

## Results

**Fixed optimal unit flow of support <code class="math">s_x</code>, general balances/signed costs**

**Retained support / records.** <code class="math">O(s_x+n\sqrt{s_x})</code>

**Query time or report.** <code class="math">O(n)</code> difference; <code class="math">O(s_x+n)</code> full support

**Min-cost <code class="math">\lambda</code>-flow, simple nonnegative-cost digraph**

**Retained support / records.** <code class="math">O(n^{3/2}\lambda^{1/4})</code>

**Query time or report.** <code class="math">O(n)</code> difference; <code class="math">O(n\sqrt{\lambda})</code> full support

**Cost-only <code class="math">\lambda</code>-flow sensitivity**

**Retained support / records.** <code class="math">O(n\sqrt{\lambda})</code>

**Query time or report.** <code class="math">O(\log(n+1))</code>

**Min-cost maximum flow**

**Retained support / records.** <code class="math">O(n^{3/2}\lambda^{1/4})\le O(n^{7/4})</code>

**Query time or report.** Two consecutive flow-value structures

**Min-cost maximum internally vertex-disjoint <code class="math">s</code>–<code class="math">t</code> paths**

**Retained support / records.** <code class="math">O(n^{3/2})</code>

**Query time or report.** <code class="math">O(n)</code> full output; one arc or one internal vertex failure

**General matching, one edge failure**

**Retained support / records.** At most <code class="math">4\mu+2</code> edges

**Query time or report.** <code class="math">O(\mu)</code> via one blossom-aware augmentation

**General matching, one edge or one vertex failure**

**Retained support / records.** At most <code class="math">6\mu+2</code> edges

**Query time or report.** <code class="math">O(\mu)</code>; alternative single failures

**Two arbitrary matroids, cardinality only**

**Retained support / records.** At most <code class="math">2r+k\le3r</code> elements

**Query time or report.** Optimize on retained ground using original oracles; <code class="math">k</code> avoidable baseline elements

**One-element price change, two matroids**

**Retained support / records.** <code class="math">O(N+r\sqrt{\min\{N,r^2\}})</code>

**Query time or report.** <code class="math">O(r)</code> exact output, no query oracle calls

**Arbitrary new arborescence arc, prescribed spanning size**

**Retained support / records.** <code class="math">O(n^2)</code> records

**Query time or report.** <code class="math">O(\log^2 n)</code> gap evaluation; <code class="math">O(n+\log^2 n)</code> full output

The weighted two-matroid and arborescence single-deletion theorems have their own [preserver card](../exact-failure-preservers/). Supplied-catalog insertion in the price structure keeps rank fixed; it does not handle an insertion that increases maximum rank.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
