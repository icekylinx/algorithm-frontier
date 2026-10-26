# Exact one-failure minimum-cost flow preservers from a sparse acyclic support

**Abstract.** We express every relevant single-arc failure of a fixed optimal unit-capacity flow as a distance demand in one residual graph. Combining this reduction with classical pairwise distance preservation and the acyclic-flow support bound gives exact sparse preservers, difference reporting, and cost oracles. Vertex splitting yields an output-sensitive analogue for internally vertex-disjoint paths.

## 1. Statement

Let $`G=(V,E)`$ be a simple directed graph on $`n`$ vertices and $`m`$ arcs, with capacity one on every arc, nonnegative rational arc costs, and fixed terminals $`s\ne t`$. Self-loops may be discarded: with nonnegative costs they are never needed in a minimum-cost flow, before or after a failure. For a feasible integer flow value $`\lambda\ge1`$, there is a deterministic exact one-edge-failure minimum-cost $`\lambda`$-flow preserver containing

```math
O(n^{3/2}\lambda^{1/4})
\tag{F1}
```

original arcs. The preserver contains an optimum flow in $`G-f`$ whenever value $`\lambda`$ remains feasible, for every individual original arc $`f`$, and also contains a no-failure optimum.

The same asymptotic number of pointer/ID records supports a reporting oracle. It reports the change from a stored optimum in $`O(n)`$ time, or the full surviving optimum as a sparse list of used arcs in $`O(n\sqrt\lambda)`$ time. If only the optimum cost and feasibility are needed, the stored path structure can be discarded: **$`O(n\sqrt\lambda)`$ cost/ID records and $`O(\log(n+1))`$ query time suffice**. The oracle has no access to the original graph at query time.

All preprocessing is deterministic and takes $`\widetilde O(mn)`$ arithmetic operations. Exact rational arithmetic has polynomial bit complexity; the records are a word-space bound when identifiers, pointers, and stored cost values fit in words.

If $`\lambda`$ is the original maximum-flow value, take the union of the constructions for values $`\lambda`$ and $`\lambda-1`$. A single unit-capacity edge deletion lowers maximum flow by at most one. This gives the same bounds for an **exact minimum-cost maximum-flow oracle after any one edge failure**. The zero-flow case is trivial.

In a simple graph, $`\lambda\le n-1`$. Thus (F1) is always

```math
O(n^{7/4}),
\tag{F2}
```

including when the original maximum flow is large. Both nonnegative costs and simplicity matter for this unconditional exponent. The more general support-sensitive statement below remains valid without those two assumptions.

## 2. Acyclic unit flows have only $`O(n\sqrt\lambda)`$ support arcs

This support bound is due to Karger--Levine (STOC 1998). We include a direct topological-span proof to make its application to directed minimum-cost flows explicit.

Fix an integral minimum-cost $`\lambda`$-flow $`x`$. Because all original costs are nonnegative, every directed cycle in its positive support has cost zero: otherwise cancelling one unit around that cycle would reduce the objective. Cancel such zero-cost cycles until the support is acyclic, without changing its value or cost.

Write $`s_x=|\{e:x_e=1\}|`$. Take any topological ordering $`\pi:V\to[n]`$ of its support. The sum of its positive arc spans telescopes using flow conservation:

```math
\begin{aligned}
 \sum_{(u,v):x_{uv}=1}\bigl(\pi(v)-\pi(u)\bigr)
 &=\sum_{v\in V}\pi(v)
       \bigl(\mathrm{indeg}_x(v)-\mathrm{outdeg}_x(v)\bigr)\\
 &=\lambda\bigl(\pi(t)-\pi(s)\bigr)
 \le \lambda(n-1).
\end{aligned}
\tag{F3}
```

For any integer $`L\ge1`$, simplicity bounds the number of support arcs with span less than $`L`$ by $`nL`$: for each tail there are fewer than $`L`$ possible heads in that range. Equation (F3) bounds the number with span at least $`L`$ by $`\lambda(n-1)/L`$. Setting $`L=\lceil\sqrt\lambda\rceil`$ gives

```math
s_x\le nL+\frac{\lambda(n-1)}L
                         =O(n\sqrt\lambda).
\tag{F4}
```

This is stronger than the immediate $`O(\lambda n)`$ bound from decomposing the flow into $`\lambda`$ paths. The proof uses only an acyclic integral unit flow in a simple digraph; it is independent of how the optimum was computed.

## 3. Every relevant failure is an ordinary residual-distance demand

Construct the residual graph $`R_x`$. For an unused original arc $`a=(u,v)`$, include $`u\to v`$ of length $`c(a)`$, labeled as adding $`a`$. For a used arc $`a=(u,v)`$, include its reverse $`v\to u`$ of length $`-c(a)`$, labeled as removing $`a`$. Distinct original arcs retain distinct IDs even if residual arcs become parallel. Optimality of $`x`$ implies that $`R_x`$ has no negative directed cycle.

If a failed arc $`f`$ is unused, $`x`$ remains optimum. Consider a used arc $`f=(u,v)`$. The key identity is

```math
\mathrm{OPT}_{G-f}(\lambda)
        =c(x)-c(f)+\mathrm{dist}_{R_x}(u,v),
\tag{F5}
```

with the convention $`+\infty`$ for infeasibility.

**A residual path gives a feasible repair.** A simple residual $`u`$-to-$`v`$ path cannot use the residual reverse $`v\to u`$ of the failed arc: it would visit its terminal $`v`$ before finishing, or revisit its source $`u`$. Delete $`f`$ from the flow, then augment one unit along this residual path. Original unused arcs on the path become used, and used arcs traversed in reverse become unused. All capacities remain respected. The endpoint imbalances caused by deleting $`f`$ are exactly repaired. Its cost is the right side of (F5).

**An optimum repair gives a residual path.** For any integral feasible $`\lambda`$-flow $`y`$ avoiding $`f`$, orient the signed difference $`y-x`$ as a circulation in $`R_x`$. It decomposes into directed cycles, including one that contains the reverse of $`f`$. All these cycles have nonnegative cost. Removing the reverse of $`f`$ from its cycle gives a residual $`u`$-to-$`v`$ path of cost at most $`c(y)-c(x)+c(f)`$. This proves the other inequality and the feasibility equivalence.

Thus all failures reduce to at most $`s_x`$ ordinary ordered-pair distance demands in the *same* residual graph. In particular, the residual graph need not be modified separately for each failed edge.

## 4. Preserving and reporting the repairs

Apply the classical directed weighted $`p`$-pair distance-preserver bound $`O(n\sqrt p)`$, with $`p\le s_x`$, to the demands in (F5). Keep the baseline support and every original arc whose forward or reverse residual copy is retained. The resulting original-arc subgraph has size

```math
O(s_x+n\sqrt{s_x}).
\tag{F6}
```

By (F5), it contains an optimum after every relevant failure; failures outside the baseline support keep $`x`$ feasible and optimum. Substituting (F4) proves (F1).

For constructive reporting, use the deterministic phased short-path/hub construction from the companion two-matroid manuscript. Give each residual arc the lexicographic length $`(\ell,1)`$. Every directed cycle is strictly positive in this order: its first coordinate is nonnegative and its second is positive. Consequently every lexicographically shortest demand walk is simple. Store explicit short demand paths and, for each selected hub, an in-tree and an out-tree of shortest paths, with a demand pointer to an appropriate hub. The total number of records is $`O(s_x+n\sqrt{s_x})`$; a demand path is reported in $`O(n)`$ time.

Its signed original-arc labels, together with removal of $`f`$, are the complete update from $`x`$. This reports a difference of at most $`n`$ original arcs. To output a full optimum, scan the stored support, omit its removed arcs, and append the added arcs. The result has at most $`s_x+n`$ used arcs and is produced in $`O(s_x+n)`$ time. Per-query timestamps on the baseline support, with positions recorded in the path labels, avoid scanning the full original ground set. A query for an unused arc is handled by the baseline dictionary.

Store the value in (F5) or an infinity flag for every used baseline arc. A cost query needs only dictionary lookup and the stored answer. If no path or flow output is requested, discard all paths and trees and retain only this $`O(s_x)`$-record table and the baseline cost. This is the elementary relevant-failures-table consequence of the support bound. It does not claim a faster baseline minimum-cost-flow algorithm; it is a static sensitivity representation.

For arbitrary integer balances and signed rational costs, the residual reduction and (F6) still hold for any fixed optimal integral unit-capacity flow of support size $`s_x`$. Nonnegative $`s`$-to-$`t`$ costs and simplicity are what supply the stronger uniform bound (F4).

## 5. Preprocessing and maximum-flow value changes

A deterministic successive-shortest-augmenting-path algorithm computes the minimum-cost flow of every feasible value up to $`\lambda`$ using $`O(\lambda(m+n\log n))`$ arithmetic operations with potentials. To obtain an acyclic optimum directly, use the lexicographic original-arc objective $`(c(e),1)`$: first minimize original cost, then total used-arc count. Every support cycle has a strictly positive lexicographic cost and could be cancelled, so none occurs in such an optimum. The second criterion does not change the primary optimum. Here $`\lambda\le n-1`$ and also $`\lambda\le m`$, so construction is $`\widetilde O(mn)`$. For the maximum-flow objective, retain optima at the last two feasible values. Alternatively, the cycle cancellation described in Section 2 makes an arbitrary optimum acyclic within the same preprocessing budget.

For each of the at most two baseline flows, Bellman--Ford potentials and all-source shortest paths in its residual graph use $`\widetilde O(mn)`$ arithmetic operations. Isolated vertices need not enter the residual shortest-path computation; the number of incident vertices is at most $`2m`$, so the apparent additional all-source $`n^2`$ term is absorbed by $`O(mn)`$. The at most $`s_x`$ demanded paths have $`O(ns_x)\subseteq O(nm)`$ total incidence size.

The phased greedy hitting construction can maintain vertex-to-unhit-path incidence lists and coverage counts. Each path is removed once in a phase, and the number of remaining demands decreases geometrically. This costs $`\widetilde O(ns_x)`$, within the same bound. Final stored tree records and retained original arcs satisfy (F6).

If the original maximum flow is $`\lambda`$, removing a single used arc from an integral flow loses at most one of its path units; equivalently, every cut loses at most one unit of capacity. Thus the new maximum value is either $`\lambda`$ or $`\lambda-1`$. The rank-$`\lambda`$ reporting oracle determines feasibility and supplies the optimum when feasible. Otherwise the separately constructed value-$`(\lambda-1)`$ oracle supplies the new exact minimum-cost maximum flow. This argument does not treat a single edge of capacity larger than one as a unit-capacity failure.

## 6. Vertex-disjoint path packings: $`O(n^{3/2})`$ space for both arc and vertex faults

Consider the minimum-total-cost maximum collection of internally vertex-disjoint directed paths from a fixed $`s`$ to a fixed $`t`$, with nonnegative rational costs, in a simple directed graph. The number of paths is unrestricted and is determined by the instance. There is an exact sensitivity preserver and reporting oracle with

```math
O(n^{3/2})\text{ original arcs and records},\qquad
         \widetilde O(mn)\text{ preprocessing},\qquad
         O(n)\text{ full path-packing output time},
\tag{F7}
```

handling either one original arc failure or one internal vertex failure in the same oracle.

Use the classical vertex-splitting reduction. Replace every internal vertex $`v`$ by $`v^{\mathrm{in}},v^{\mathrm{out}}`$ and its unit-capacity gate $`v^{\mathrm{in}}\to v^{\mathrm{out}}`$; original arcs go from the appropriate out-copy to the appropriate in-copy. Give gates zero cost and every original arc capacity one. Keep $`s,t`$ unsplit, discard arcs entering $`s`$ or leaving $`t`$, and keep the possible direct $`s\to t`$ arc at capacity one. Integral acyclic flows are precisely collections of internally vertex-disjoint paths.

An acyclic optimum packing uses each internal vertex in at most one path. Its original arcs number at most $`n-2+\lambda=O(n)`$, and its gates number at most $`n-2`$, because $`\lambda\le n-1`$. Therefore its full split-network support has $`s_x=O(n)`$, independently of the packing size. Apply the support-sensitive formula (F6) to this $`O(n)`$-vertex split graph, giving $`O(n^{3/2})`$ retained arcs and records. The support-sensitive proof does not need the generic bound (F4) here.

Failure of an original arc is failure of one corresponding unit arc. Failure of an internal vertex is failure of its one gate. In a feasible nonnegative flow, deleting that gate forces all incident original-arc flow at the vertex to zero by conservation at the in-copy and out-copy, so this is exactly the original vertex-deletion requirement. Relevant arc and gate queries together form only $`O(n)`$ residual-distance demands.

Removing one arc or one vertex destroys at most one path of a vertex-disjoint packing. Hence maximum packing size falls by at most one, and the union of two consecutive-value constructions handles the maximum-cardinality objective with minimum total cost as its secondary objective. A reported residual repair changes $`O(n)`$ split arcs. Its original-arc support is $`O(n)`$; any zero-cost directed cycles can be discarded, and the remaining paths can be enumerated, in $`O(n)`$ time. Positive-cost cycles cannot occur in an optimum.

The endpoint pair is fixed; this does not solve prescribed multi-commodity disjoint-path problems. The standard simple-graph assumption also rules out arbitrarily many parallel direct $`s\to t`$ arcs, which would otherwise permit arbitrarily large output without using any internal vertices. With $`d`$ such parallel arcs retained as separate objects, an $`O(n)`$ output bound would require an additional dependence on $`d`$.

## 7. Baselines and the scope of the increment

The $`O(n\sqrt p)`$ directed weighted pairwise-preserver ingredient is classical. Bodwin's simplified construction explicitly attributes it to Coppersmith--Elkin; the deterministic phased implementation and path-reporting records follow the companion manuscript.

For $`\lambda=1`$, the flow problem is ordinary weighted $`s`$-to-$`t`$ replacement-path preservation. Bodwin--Grandoni--Parter--Vassilevska Williams (ICALP 2017), Lemmas 4.5--4.6, already relate that problem to ordinary pairwise distance preservation, yielding the $`O(n^{3/2})`$ upper bound. The $`O(n\sqrt\lambda)`$ support lemma is likewise classical, due to Karger--Levine (STOC 1998). The contribution here is the general unit-flow residual-demand application and its composition with that lemma, leading to $`O(n^{3/2}\lambda^{1/4})`$ exact failure support and the universal $`O(n^{7/4})`$ consequence.

Bansal--Choudhary--Dhanoa--Wardhan (ISAAC 2024) preserve single-source bounded **flow value** under $`h`$ faults with $`O(\lambda 2^h n)`$ arcs; the requirement covers all targets but does not preserve an exact cost objective. Ahi--Choudhary--Pande--Pushpraj--Saggi (ITCS 2026) give compact oracles for unweighted maximum-flow and minimum-cut queries. Their cardinality-only guarantees are not being improved here.

Bilò et al. (STACS 2022) construct minimum-cost $`p`$-disjoint-path preservers from one source to all targets in the no-failure model, with $`p(n-1)`$ edges, and state an extension to vertex-disjoint paths. Their multipath guarantee fixes the cost optimum before faults; it does not assert that the surviving graph contains a new exact cost optimum after an arbitrary arc or vertex deletion. Formula (F7) concerns one fixed terminal pair and fault-sensitive exact optimality.

Choudhary--Kumar--Saggi (September 2026), Theorem 4.5, give randomized algebraic min-cost maximum-flow sensitivity oracles for an arbitrary number $`f`$ of updates and integer costs bounded by $`W`$, with $`\widetilde O(W(fn)^3)`$ preprocessing, $`O(W(fn)^3\log n)`$ space, and $`\widetilde O(f^{3\omega+1}Wn)`$ cost-query time. The present one-deletion construction is deterministic, uses arbitrary nonnegative rational costs, retains original arcs, and supports direct solution reporting. It has a narrower update model. This comparison is a concrete distinction from that general-purpose oracle, not a claim that every previous single-failure flow representation has been ruled out.

### Primary sources

1. Greg Bodwin. *A Note on Distance-Preserving Graph Sparsification*, Theorem 3 and Lemma 1. https://arxiv.org/pdf/2001.07741
2. Don Coppersmith, Michael Elkin. *Sparse Sourcewise and Pairwise Distance Preservers*. SIAM Journal on Discrete Mathematics 20(2), 463--501, 2006. DOI 10.1137/050630696.
3. Greg Bodwin, Fabrizio Grandoni, Merav Parter, Virginia Vassilevska Williams. *Preserving Distances in Very Faulty Graphs*. ICALP 2017, Lemmas 4.5--4.6. https://arxiv.org/pdf/1703.10293
4. Shivam Bansal, Keerti Choudhary, Harkirat Dhanoa, Harsh Wardhan. *Fault-Tolerant Bounded Flow Preservers*. ISAAC 2024, Article 9. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ISAAC.2024.9
5. Mridul Ahi, Keerti Choudhary, Shlok Pande, Pushpraj, Lakshay Saggi. *Maximum-Flow and Minimum-Cut Sensitivity Oracles for Directed Graphs*. ITCS 2026, Article 5. https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.5/LIPIcs.ITCS.2026.5.html
6. Keerti Choudhary, Amit Kumar, Lakshay Saggi. *Sensitivity Oracles for Matroid Packing, Matroid Covering, and Matching Problems with Applications*. arXiv:2609.01283v1, Theorem 4.5. https://arxiv.org/pdf/2609.01283
7. Jeff Erickson. *Algorithms, Lecture 25½: Minimum Cost Flows*. University of Illinois, Spring 2016. Residual cycle optimality and successive shortest augmenting paths. https://courses.grainger.illinois.edu/cs473/sp2016/notes/25bis-mincostflow.pdf
8. David R. Karger, Matthew S. Levine. *Finding Maximum Flows in Undirected Graphs Seems Easier than Bipartite Matching*. STOC 1998, 69--78, DOI 10.1145/276698.276714, Theorem 3.1. The acyclic $`O(n\sqrt\lambda)`$-support bound is a general simple-graph flow lemma used by their undirected-flow algorithms. https://people.csail.mit.edu/karger/Papers/stoc98.pdf . Accessible full-text mirror: https://kam.mff.cuni.cz/~matousek/cla/karger-levine-floweasierthanmatching.pdf
9. Davide Bilò, Gianlorenzo D'Angelo, Luciano Gualà, Stefano Leucci, Guido Proietti, Mirko Rossi. *Single-Source Shortest $`p`$-Disjoint Paths: Fast Computation and Sparse Preservers*. STACS 2022, Article 12. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2022.12
