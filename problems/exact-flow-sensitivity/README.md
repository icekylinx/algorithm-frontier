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

Flow and vertex-disjoint paths: deterministic $\widetilde O(mn)$ arithmetic preprocessing. General matching and oracle matroids: deterministic polynomial preprocessing. Price sensitivity beyond a baseline optimum uses $O(Nr)$ independence tests and $O(Nr^2+r^3)$ arithmetic work. Query bounds are listed separately.

**Space**

Support and reporting records are listed below. Rational values occupy their actual bit length; construction workspace and external oracle storage are separate.

**Parameters**

$n,m$ are graph sizes; $\lambda$ is a feasible flow value; $s_x$ is a fixed optimum flow support; $\mu$ is graph matching number; $N,r$ are matroid ground size and prescribed rank.

**Model and representation**

Simple directed unit-capacity graphs with nonnegative rational costs for the uniform flow exponent; loopless undirected general graphs for cardinality matching; independence-oracle matroids for intersection. All queries are independent relative to the preprocessed input.

**Lower-bound scope**

General-matching certificates preserve cardinality, not every increased replacement cost. Integrality alone does not imply a linear certificate: the manuscript gives a quadratic retained-vertex obstruction for maximum independent set even in perfect graphs.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete proof](proof.md) and [canonical manuscript map](sources.md).

## Results

**Fixed optimal unit flow of support $s_x$, general balances/signed costs**

**Retained support / records.** $O(s_x+n\sqrt{s_x})$

**Query time or report.** $O(n)$ difference; $O(s_x+n)$ full support

**Min-cost $\lambda$-flow, simple nonnegative-cost digraph**

**Retained support / records.** $O(n^{3/2}\lambda^{1/4})$

**Query time or report.** $O(n)$ difference; $O(n\sqrt{\lambda})$ full support

**Cost-only $\lambda$-flow sensitivity**

**Retained support / records.** $O(n\sqrt{\lambda})$

**Query time or report.** $O(\log(n+1))$

**Min-cost maximum flow**

**Retained support / records.** $O(n^{3/2}\lambda^{1/4})\le O(n^{7/4})$

**Query time or report.** Two consecutive flow-value structures

**Min-cost maximum internally vertex-disjoint $s$–$t$ paths**

**Retained support / records.** $O(n^{3/2})$

**Query time or report.** $O(n)$ full output; one arc or one internal vertex failure

**General matching, one edge failure**

**Retained support / records.** At most $4\mu+2$ edges

**Query time or report.** $O(\mu)$ via one blossom-aware augmentation

**General matching, one edge or one vertex failure**

**Retained support / records.** At most $6\mu+2$ edges

**Query time or report.** $O(\mu)$; alternative single failures

**Two arbitrary matroids, cardinality only**

**Retained support / records.** At most $2r+k\le3r$ elements

**Query time or report.** Optimize on retained ground using original oracles; $k$ avoidable baseline elements

**One-element price change, two matroids**

**Retained support / records.** $O(N+r\sqrt{\min\{N,r^2\}})$

**Query time or report.** $O(r)$ exact output, no query oracle calls

**Arbitrary new arborescence arc, prescribed spanning size**

**Retained support / records.** $O(n^2)$ records

**Query time or report.** $O(\log^2 n)$ gap evaluation; $O(n+\log^2 n)$ full output

The weighted two-matroid and arborescence single-deletion theorems have their own [preserver card](../exact-failure-preservers/). Supplied-catalog insertion in the price structure keeps rank fixed; it does not handle an insertion that increases maximum rank.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
