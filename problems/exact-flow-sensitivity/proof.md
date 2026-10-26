# Exact flow, matching, and price sensitivity

## 1. Unit-capacity flow theorem

For a simple directed graph with unit capacities, nonnegative rational costs, and fixed terminals, feasible flow value $\lambda\ge1$ admits an exact one-arc-failure preserver of $O(n^{3/2}\lambda^{1/4})$ original arcs. Deterministic preprocessing is $\widetilde O(mn)$ arithmetic operations. Reporting takes $O(n)$ for a difference or $O(n\sqrt\lambda)$ for full support. A cost-only structure uses $O(n\sqrt\lambda)$ records and $O(\log(n+1))$ lookup time.

**Lemma 1.1 (acyclic support).** An acyclic integral unit $\lambda$-flow has $O(n\sqrt\lambda)$ support arcs.

**Proof.** In a topological order $\pi$, conservation gives
$$
\sum_{uv:x_{uv}=1}(\pi(v)-\pi(u))
=\lambda(\pi(t)-\pi(s))\le\lambda(n-1).
$$
Simplicity bounds arcs of span below $L$ by $nL$; the rest number at most $\lambda(n-1)/L$. Take $L=\lceil\sqrt\lambda\rceil$. A nonnegative-cost optimum is made acyclic by cancelling zero-cost cycles, or minimizing used-arc count secondarily. $\square$

**Lemma 1.2 (residual identity).** For an optimal integral flow $x$ and used failed arc $f=(u,v)$,
$$
\operatorname{OPT}_{G-f}(\lambda)=c(x)-c(f)+\operatorname{dist}_{R_x}(u,v).
$$

**Proof.** The residual graph has no negative cycle. A simple residual $u$-to-$v$ path cannot use the reverse $v$-to-$u$ of $f$. Remove $f$ and augment along that path to repair conservation and capacities at the displayed cost. Conversely, decompose any repair difference into residual cycles. Each costs nonnegatively. Remove the reverse of $f$ from its cycle to obtain a path costing at most the repair gap plus $c(f)$. This proves equality and the infeasibility convention. $\square$

If $s_x$ is baseline support, all relevant failures give at most $s_x$ demands in this one residual graph. Classical directed pairwise distance preservation keeps $O(n\sqrt{s_x})$ residual arcs. Include their original labels and the baseline, yielding $O(s_x+n\sqrt{s_x})$ original arcs. Lemma 1.1 gives the headline. Lexicographic cost/hop paths are simple and report $O(n)$ changes; full output scans only the stored baseline and changes.

One unit-arc deletion lowers maximum flow by at most one, so two consecutive value constructions handle minimum-cost maximum flow. Since $\lambda\le n-1$, the uniform bound is $O(n^{7/4})$. For general balances or signed costs the support-sensitive theorem remains valid, but the acyclic support estimate needs its stated assumptions.

## 2. Internally vertex-disjoint paths

Split each internal vertex into in/out copies with a capacity-one gate. An acyclic packing uses at most $n-2$ internal vertices and $n-2+\lambda=O(n)$ original arcs; its split support is $O(n)$. A gate deletion forces incident flow to zero by conservation and represents deletion of that internal vertex.

Apply Lemma 1.2 to both gates and original arcs. This gives $O(n^{3/2})$ original arcs and records, $\widetilde O(mn)$ arithmetic preprocessing, and $O(n)$ full path output. A single failure destroys at most one path, so two consecutive values preserve maximum cardinality with minimum total cost. The terminal pair is fixed; simplicity controls direct terminal-to-terminal multiplicity.

## 3. General-graph cardinality matching

For matching number $\mu$ and fixed maximum matching $M$, one-edge-failure certificates need at most $4\mu+2$ original edges. A joint certificate for one edge **or** one vertex failure needs at most $6\mu+2$. Deterministic preprocessing is polynomial and queries take $O(\mu)$.

Impose a small fractional avoidance cap for each baseline edge or covered vertex whose deletion still allows size $\mu$. A convex combination of its avoiding witnesses with $M$ proves feasibility. Add the outside-mass cap $x(E\setminus M)\le1/2$, which keeps every edge of $M$ positive.

**Support lemma.** Intersecting the cardinality-$\mu$ matching face with $k$ rational inequalities yields a point with at most $3\mu+k+1$ positive coordinates.

**Proof.** Maximize a rational objective outside every proper span of the finite constraint normals. Uncross an optimal dual, keeping the additional rows fixed, so its positive odd-set rows are laminar. At most $2\mu$ degree rows have positive multipliers, since each is tight and total fractional degree is $2\mu$. At most $\mu$ laminar odd-set rows are positive: after adding singleton leaves, each internal node has an odd number of children, at least three, and its tree count is bounded by the tight internal matching mass of its root. Disjoint roots have total mass at most $\mu$.

There are additionally at most $k$ new rows, one cardinality row, and $m-s$ slack unit rows for a support of size $s$. If $s>3\mu+k+1$, these rows span a proper subspace, contradicting the objective. The complete proof supplies the uncrossing potentials and polynomial-bit generic objective. $\square$

At most $\mu$ edge caps plus the outside-mass cap give $4\mu+2$; at most $2\mu$ additional vertex caps give $6\mu+2$. Integrality decomposes the point into maximum matchings. Expectation below one at a cap ensures a component avoiding that failure. Other failures use $M$ or $M$ minus one edge.

Start from the union of $M$ and avoiding witnesses, then greedily delete nonbaseline edges whenever all designated scenarios remain feasible. A terminal graph larger than the support bound contradicts the lemma applied to that graph. Queries need at most one blossom-aware augmentation on its $O(\mu)$ edges. Classical skew-symmetric regular reachability supplies linear time; ordinary directed reachability does not.

## 4. Two-matroid cardinality

For two arbitrary matroids with maximum common size $r$, the analogous caps yield at most $2r+k\le3r$ original elements, where $k$ is the number of avoidable baseline elements.

For each matroid, tight rank rows restricted to positive support form a lattice. A maximal tight chain has at most $r$ increments because each has positive integral rank. Every tight set is a union of chain blocks, so the row-space dimension is at most $r$. The two spaces share the cardinality row, bounding their combined dimension by $2r-1$. The $k$ avoidance rows and one outside-mass row give support at most $2r+k$. Common-base integrality supplies the failure witnesses. Query optimization on this restriction still uses the original oracles.

## 5. One-element price changes

A separate structure for prescribed rank $r$, fixed rational prices, and $N$ original elements uses
$$
O\left(N+r\sqrt{\min\{N,r^2\}}\right)
$$
records and reports an optimum in $O(r)$ time after an independent one-element price change.

For an outside element $e$, take one explicit eligible exchange arc labeled $e$, followed by a shortest return path in the compressed exchange graph. Conditional convex decomposition gives an $e$-containing basis of no larger gap; reverse exchange decomposition proves equality. Choosing a minimum-hop optimum cycle forces distinct labels and makes its toggle feasible. Baseline elements use the analogous exclusion gap. A price query compares its best containing and avoiding alternatives.

There is one starter/return-pair descriptor per element and at most $\min\{N,r^2\}$ distinct return pairs. Pairwise distance reporting gives the displayed space and output bound. Supplied-catalog insertion uses the same argument at fixed rank; it does not cover rank-increasing insertion. Arbitrary new arborescence arcs admit the separate $O(n^2)$-record heavy-light implementation in the complete proof.

## Complete proofs

[Flow and paths](manuscripts/exact-min-cost-flow-and-vertex-disjoint-paths.md); [matching and uncrossing](manuscripts/linear-single-fault-general-matching.md); [two-matroid cardinality](manuscripts/linear-unweighted-two-matroid-certificate.md); [price sensitivity](manuscripts/compact-one-element-price-sensitivity.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
