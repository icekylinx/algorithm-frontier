# Compact reporting for one-element price changes in matroid intersection

**Abstract.** We prove a forced-element exchange-cycle identity and combine it with directed pairwise distance preservation. The resulting compact data structure reports an exact common-matroid optimum after one independent rational price change. Fixed-rank insertion and rooted-arborescence reporting follow from the same identity.

## 1. Statement and antecedents

Let two arbitrary matroids on a common $N$-element ground set have a feasible common independent set of prescribed cardinality $r\ge1$. Let $w$ be rational costs and $B$ a minimum-cost common $r$-set. No linear representation is assumed.

Deterministic polynomial oracle preprocessing gives a self-contained structure using

$$
O\!\left(N+r\sqrt{\min\{N,r^2\}}\right)
\tag{1}
$$

records. A query changes one original element's cost by an arbitrary rational amount $\Delta$, and reports a minimum-cost common $r$-set in $O(r)$ time, with no subsequent matroid-oracle calls. The simpler all-pairs-path implementation uses $O(N+r^2)$ records. Queries are independent changes relative to the original costs.

If $r$ is maximum common cardinality, cost-only changes do not affect it, so this also handles minimum-cost maximum-cardinality optimization. Records contain identifiers, rational values and pointers. Bit space includes their actual encoding lengths; the record count is not a claim that arbitrarily long costs fit into fixed machine words.

Brezovec, Cornuéjols, and Glover (1986) explicitly discuss weight sensitivity through exchange graphs. Camerini and Hamacher (1989) use condensed border graphs and shortest paths for ranking intersections. Neither sensitivity itself nor graph condensation is claimed new. The concrete contribution here is the forced-element identity with a repeated-label proof, followed by classical pair-distance preservation to obtain the reporting bound (1). Its priority needs comparison with the complete classical papers. [1–3]

## 2. Compressed exchange graph

Truncate both matroids to rank $r$. For $e\notin B$, let

$$
A_e=\{a\in B:B-a+e\text{ is a base of }M_1\},\qquad
C_e=\{b\in B:B-b+e\text{ is a base of }M_2\}.
$$

For every $a\in A_e,b\in C_e$, introduce an arc $a\to b$, labelled $e$, of cost

$$
w(e)-w(a).
\tag{2}
$$

Let $D$ retain the cheapest labelled arc for each ordered pair of baseline elements. Ties are deterministic. Every arc has secondary length one, and all paths/cycles minimize (cost, number of arcs) lexicographically.

Two facts from the companion manuscript are recalled. First, every directed exchange cycle has nonnegative cost. For a simple cycle $C$ of $t$ arcs, let $d$ remove each cycle vertex once and add outside labels with multiplicity. For $0<\eta\le1/t$,

$$
\chi^B+\eta d
=(1-t\eta)\chi^B+
\eta\sum_{a\to b\text{ on }C}\chi^{B-a+e}
$$

belongs to the first base polytope. Replacing each tail $a$ by its head $b$ proves membership in the second. The common-base polytope is integral, and optimality of $B$ implies nonnegative cycle cost.

Second, for any common base $J$, basis-exchange matchings in the two matroids decompose $B\triangle J$ into labelled exchange cycles with total cost $w(J)-w(B)$. Each outside element occurs exactly once. Replacing an unprotected arc by the cheapest corresponding arc of $D$ cannot increase cost.

## 3. Forcing an outside element

Fix $e\notin B$. A candidate consists of one explicit eligible $e$-arc $a\to b$, followed by a shortest path from $b$ to $a$ in $D$. A loop starter $a=b$ uses the empty return path. Otherwise the secondary hop objective makes the return path simple, so the candidate is a nonempty simple compressed cycle.

Define

$$
\delta_e^+
=\min_{a\in A_e,\ b\in C_e}
\bigl[w(e)-w(a)+\operatorname{dist}_D(b,a)\bigr],
\tag{3}
$$

with infinity when no candidate exists. Among minimum-cost candidates choose one of minimum hop count.

**Forced-element identity.**

$$
\min_{\substack{J\text{ common base}\\e\in J}} w(J)
=w(B)+\delta_e^+.
\tag{4}
$$

Moreover the chosen candidate can be toggled literally: its distinct baseline vertices leave and its distinct outside labels enter.

The return path may initially use the label $e$ again. This requires a proof, not an assumption. If a candidate $C$ uses $e$ with multiplicity $q_e\ge1$, the fractional point from Section 2 has coordinate $x_e=q_e\eta$. In an integral decomposition this is the total probability of bases containing $e$. All decomposed bases cost at least $w(B)$, while the expected cost increase is $\eta\ell(C)$. Hence some base containing $e$ has increase at most

$$
\ell(C)/q_e\le\ell(C),
$$

where nonnegative cycle cost justifies the last step.

Conversely, an optimum base containing $e$ has one exchange-decomposition cycle containing that label. All other cycles have nonnegative cost. Keep its one $e$-arc explicit and compress the other arcs into $D$; replacing the return route by a shortest path yields a candidate no more expensive than the optimum increase. This proves (4).

For literal feasibility, let the selected candidate have $t$ arcs and $u\le t$ distinct outside labels. Conditional decomposition gives an optimum $e$-containing base $J$ supported on these labels and $B$, retaining every baseline element outside the cycle. Put $q=|J\setminus B|\le u$. Reverse exchange decomposition gives an $e$-candidate of cost at most $\delta_e^+$ and at most $q$ arcs. Equation (4) makes its cost exactly $\delta_e^+$. Minimum hop count forces

$$
t\le q\le u\le t.
\tag{5}
$$

Thus all outside labels are distinct, $J$ uses all of them, and it removes all cycle vertices. This includes zero-cost and nonunique-baseline cases.

## 4. Excluding a baseline element and answering a price change

For $f\in B$, the companion deletion theorem identifies

$$
\delta_f^-=
\min_{\substack{J\text{ common base}\\f\notin J}}
w(J)-w(B)
$$

with the shortest nonempty exchange-cycle cost through $f$. It can be computed from all-pairs distances by choosing a starter arc:

$$
\delta_f^-=
\min_{f\to b\in E(D)}
\bigl[\ell(f,b)+\operatorname{dist}_D(b,f)\bigr].
\tag{6}
$$

Again minimize total hop count among ties. The support-and-minimum-hop proof makes this cycle a literal optimum toggle.

When $w(e)$ changes by $\Delta$:

- If $e\notin B$, compare $w(B)$ with $w(B)+\delta_e^++\Delta$. These are the best solutions excluding and containing $e$.
- If $e\in B$, compare $w(B)+\Delta$ with $w(B)+\delta_e^-$.

Ignore infinite alternatives and return the corresponding toggle or $B$. The comparison is valid for either sign and any magnitude of the price change.

## 5. Compact path storage

Compute $D$, lexicographic all-pairs shortest paths, and one optimal starter descriptor per original element: (6) for baseline elements and (3) for outside elements. A descriptor specifies its starter, the return pair $(b,a)$, and the optimum gap.

There is at most one demanded return pair per element. After deduplication,

$$
p\le\min\{N,r^2\}.
$$

The classical deterministic directed weighted pair-distance construction, in the path-reporting form developed in the companion manuscript, stores these paths in $O(r\sqrt p)$ records. Adding the $O(N)$ descriptors gives (1). All-source shortest-path trees give the simpler $O(N+r^2)$ alternative.

Vertex splitting is unnecessary: every descriptor supplies a real starter arc, so an empty return path represents a one-arc exchange loop, never an empty exchange cycle. The pair-preserver uses the same secondary hop objective. Its reported return paths remain lexicographically shortest. Each has at most $r-1$ arcs; the starter plus return path is the literal toggle already proved. Full output takes $O(r)$ time.

Beyond computing $B$, a direct implementation uses $O(Nr)$ independence tests for exchange eligibility and $O(Nr^2+r^3)$ arithmetic work to build $D$, compute distances, and choose descriptors. The deterministic path structure uses polynomial preprocessing. These time bounds are not claimed optimal.

## 6. Fixed-rank insertion from a supplied catalog

Suppose only an active subset is initially available, $B$ is optimal among its common $r$-sets, and inactive candidate elements are supplied for preprocessing. Build $D$ using only active outside elements.

For an inactive candidate $e$, (3) remains valid and may be negative. Its return path cannot contain $e$, so $q_e=1$. Every decomposed base not containing $e$ uses only active elements and costs at least $w(B)$. Conditioning therefore gives an $e$-containing base of increase at most the candidate length without requiring that length to be nonnegative. Reverse exchange and the minimum-hop argument are unchanged.

Thus one descriptor supports inserting that candidate at its specified or query-adjusted price, with $O(r)$ reporting. The cardinality is prescribed: an insertion that raises maximum common cardinality from $r$ to $r+1$ is not covered here. Every insertion query activates one candidate relative to the original active set.

## 7. Valuated and arborescence corollaries

For two valuated matroids with an additional linear price vector, use the companion valuated tangent and exchange-matching lemmas. Replace (2) by the sum of the two single-exchange valuation increments and the linear-price increment. Conditional mass, reverse exchange, and minimum-hop proofs then give the same bounds for changing one linear price.

For a rooted directed spanning arborescence $T$, a new arc $e=(u,v)$ has the unique partition-removal choice $b_v$, the tree edge entering $v$. Its graphic-removal choices are the tree edges on the undirected path $P_T(u,v)$. Therefore its forced-arc gap is

$$
w(e)+\min_{a\in P_T(u,v)}
\left[\operatorname{dist}_D(b_v,a)-w(a)\right].
\tag{7}
$$

For each $b$, store a range-minimum structure on a heavy-light decomposition of $T$ for the values $\operatorname{dist}_D(b,a)-w(a)$, breaking cost ties by return-path hop count. All $b$'s use $O(n^2)$ records, as do all-source return-path trees. An arbitrary new arc specified at query time is evaluated in $O(\log^2 n)$ time, and the resulting optimum arborescence is reported in $O(n+\log^2 n)$. Discard self-loops and arcs entering the root. For parallel original arcs, identities and original prices are retained as needed for price-change queries.

Directed-tree reoptimization through weighted matroid intersection is established work, including Jiang–Wang 2026. This is a static reporting-data-structure consequence, not a first dynamic directed-tree or sensitivity claim. [4]

## References

1. Carl Brezovec, Gérard Cornuéjols, and Fred Glover. **Two Algorithms for Weighted Matroid Intersection.** Mathematical Programming 36 (1986), 39–53. <https://link.springer.com/article/10.1007/BF02591988>
2. Paolo M. Camerini and Horst W. Hamacher. **Intersection of Two Matroids: (Condensed) Border Graphs and Ranking.** SIAM Journal on Discrete Mathematics 2 (1989), 16–27. <https://epubs.siam.org/doi/10.1137/0402002>
3. Don Coppersmith and Michael Elkin. **Sparse Sourcewise and Pairwise Distance Preservers.** SIAM Journal on Discrete Mathematics 20 (2006), 463–501. The directed weighted $O(n\sqrt p)$ bound is also stated in later primary literature, including <https://arxiv.org/pdf/2001.07741>.
4. Jiang and Wang. **Optimization of Directed Spanning Trees Using Weighted Matroid Intersection.** July 2026 preprint / Discrete Applied Mathematics, DOI 10.1016/j.dam.2026.07.027. <https://arxiv.org/abs/2607.25238> The comparison here uses the reported problem scope; the full paper's detailed time and space guarantees have not been independently verified in this manuscript.
