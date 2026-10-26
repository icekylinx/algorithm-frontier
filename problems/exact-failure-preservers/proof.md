# Exact single-failure preservers and reporting

## 1. Theorem

Two independence-oracle matroids on an explicit ground $`E`$, with fixed rational costs and a common independent $`k`$-set, admit a deterministic polynomial construction of an $`O(k^{3/2})`$-element restriction and reporting structure. After one element deletion it reports a minimum-cost common $`k`$-set in $`O(k)`$ operations, or infeasibility, with no query-time matroid-oracle calls.

For a directed rooted graph with nonnegative rational arc costs, this gives $`O(n^{3/2})`$ original arcs and records, $`\widetilde O(mn)`$ arithmetic preprocessing, and $`O(n)`$ optimum-arborescence output. Record counts and arithmetic costs include actual value lengths when interpreted in the bit model.

## 2. Exchange cycles

Truncate both matroids to rank $`k`$, and fix an optimum common basis $`B`$. For $`a,b\in B`$, keep the cheapest outside label $`e`$ with $`B-a+e`$ a first-matroid basis and $`B-b+e`$ a second-matroid basis. Its arc $`a\to b`$ has length $`w(e)-w(a)`$. Loops are allowed.

**Lemma 2.1.** For a simple cycle $`C`$, let $`d_C`$ remove every cycle vertex once and add outside labels with multiplicity. Then $`\chi_B+\eta d_C`$ is in both base polytopes for $`0<\eta\le1/|C|`$, and $`\ell(C)\ge0`$.

**Proof.** In the first base polytope use
```math
(1-|C|\eta)\chi_B+\eta\sum_{a\to b\in C}\chi_{B-a+e_{a,b}}.
```
In the second use the heads $`b`$ instead of the tails $`a`$. Both vectors agree because the cycle has the same head and tail multiset. Common-base integrality decomposes their common point into common bases. Since $`B`$ is optimal, its expected objective increment $`\eta\ell(C)`$ is nonnegative. $`\square`$

**Lemma 2.2 (replacement identity).** If $`\delta_f`$ is the shortest cycle length through $`f\in B`$, with infinity when none exists, then
```math
\mathrm{OPT}_{-f}(k)=w(B)+\delta_f.
```

**Proof.** In Lemma 2.1's decomposition for a cycle through $`f`$, bases avoiding $`f`$ have total coefficient $`\eta`$. All component gaps above $`w(B)`$ are nonnegative and their average is $`\eta\ell(C)`$. Some avoiding basis therefore has gap at most $`\ell(C)`$. Its support uses only $`B`$ and cycle labels, and it contains $`B\setminus V(C)`$.

Conversely, for a common basis $`J`$ avoiding $`f`$, the basis-exchange matching lemma separately matches $`J\setminus B`$ to $`B\setminus J`$ in the two matroids. Pair the matchings into directed permutation cycles. Each cycle has nonnegative cost by the same convex-decomposition argument, and their sum is $`w(J)-w(B)`$. The $`f`$-cycle costs no more than that total. Replacing its outside labels by the cheapest compressed choices cannot increase cost. These two directions prove the identity and its feasibility convention. $`\square`$

**Lemma 2.3 (literal update).** A minimum-cost cycle through $`f`$, chosen with the fewest arcs, has distinct outside labels. Replacing its vertices by its labels is an optimum avoiding $`f`$.

**Proof.** Let it have $`t`$ arcs and $`u\le t`$ distinct labels. The previous proof supplies an optimum $`J`$ supported there, retaining $`B\setminus V(C)`$. Write $`q=|J\setminus B|\le u`$. Reverse exchange decomposition supplies an optimal cycle through $`f`$ with at most $`q`$ arcs. Minimal hop count gives $`t\le q\le u\le t`$. Equality forces precisely the stated removals and insertions. $`\square`$

## 3. Sparse reporting

Split each baseline vertex into incoming and outgoing copies, with a zero arc between them. For each $`f`$, a cycle becomes an outgoing-to-incoming demand path. Give exchange arcs secondary length one, and minimize (cost, hop count) lexicographically. There are $`2k`$ vertices and at most $`k`$ finite demands; every directed cycle is strictly positive in this order.

The classical directed distance-preserver theorem keeps $`O(N\sqrt p)`$ arcs for $`p`$ demands on $`N`$ vertices. A deterministic reporting implementation stores short paths explicitly and long paths through hubs, each with an in-tree and out-tree. At threshold $`N/\sqrt p`$, a greedy hitting set of $`O(\sqrt p)`$ hubs serves a constant fraction of demands using $`O(N\sqrt p)`$ records. Remaining demand counts decrease geometrically, proving the total bound without a logarithmic loss.

A hub concatenation has the optimum lexicographic distance and cannot repeat a vertex: removing its strictly positive cycle would improve it. Reporting takes $`O(N)`$, and Lemma 2.3 converts it to a basis in $`O(k)`$. Failures outside $`B`$ return $`B`$; unreachable demands are marked infeasible.

## 4. Arborescence and valuated specializations

Arborescences are common bases of the underlying graphic matroid and the partition matroid allowing one incoming arc per nonroot vertex. For an outside arc $`u\to v`$, the partition removal is the tree arc entering $`v`$; graphic removals lie on the undirected tree path from $`u`$ to $`v`$. Heavy-light path intervals and a segment tree encode these transitions in $`O(n)`$ vertices and $`O(n+m\log^2 n)`$ arcs. The same reporting construction proves the graph bounds.

For two fixed-rank valuated matroids, use the sum of the two single-exchange valuation increments as the arc length. The complete valuated proof establishes the joint convex decomposition and valued exchange-matching inequality, after which Lemmas 2.2–2.3 apply. Preprocessing requires one supplied finite-valued basis in each effective domain, or independence access obtaining it, as well as value evaluations. A bare extended-value oracle cannot initialize a hidden unique basis efficiently.

For ordinary linear costs, the union of constructions at maximum ranks $`r`$ and $`r-1`$ handles rank drops. Arbitrary valuations have no implicit smaller-rank objective. The weighted lower bounds $`\Omega(k^{4/3})`$ and $`\Omega(n^{4/3})`$ are explicit transfers of classical distance-preserver lower bounds; two failures force quadratic support in the full manuscript's examples.

## Complete proofs and references

- [Exchange cycles, arborescence implementation, and lower bounds](manuscripts/exact-single-failure-arborescences-and-matroid-intersection.md).
- [Valuated extension and oracle interface](manuscripts/valuated-matroid-intersection.md).
- Goemans, [Matroid Intersection](https://math.mit.edu/~goemans/18453S17/matroid-intersect-notes.pdf).
- Bodwin, [A Note on Distance-Preserving Graph Sparsification](https://arxiv.org/pdf/2001.07741).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
