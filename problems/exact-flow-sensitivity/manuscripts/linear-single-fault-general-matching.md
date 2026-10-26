# Linear single-fault certificates for maximum matching in general graphs

## Theorem and scope

The central statement is about arbitrary undirected graphs, including nonbipartite graphs. It preserves exact maximum cardinality under a single original edge failure. The construction uses the full matching polytope and therefore retains the odd-set constraints that invalidate a direct ordinary-path reduction.

**Theorem.** Let $G=(V,E)$ be a finite loopless undirected graph, let $\mu=\nu(G)$, and fix a maximum matching $M$. There is a deterministic polynomial-time construction of a subgraph $H\subseteq G$, containing $M$, with at most
$$
4\mu+2
$$
edges such that
$$
\nu(H-f)=\nu(G-f)\qquad\text{for every }f\in E.
$$
The graph can be stored using $O(\mu)$ original edge and vertex identifiers. After one edge failure, an exact maximum matching can be reported in $O(\mu)$ time using a classical linear-time general-graph augmentation algorithm. The existence proof uses rational polyhedral optimization; a polynomial construction can use only ordinary matching computations. No near-linear preprocessing bound is asserted.

The same construction can support one edge failure **or** one vertex failure in a single certificate of at most $6\mu+2$ edges. These are alternative single-failure queries, not simultaneous edge-and-vertex failures.

Banerjee, Gupta, Raman, and Saurabh (CSR 2022) give a linear-size single-edge-failure certificate for bipartite graphs, an $O(\mu^2+\mu f)$-edge certificate for general graphs, and explicitly ask whether the single-edge-failure bound in general graphs can be $O(\mu)$. Their work already treats vertex failures more strongly when $f=1$. A separate 2026 algebraic sensitivity-oracle line supports arbitrary numbers of updates, with different space and output guarantees. [1, 4]

**Current baseline qualification.** Xiaoling He's September 2026 theorem bounds a minimal matching-covered nonbipartite graph by $5(n-2)/2$ edges. Together with the $O(\mu)$-vertex kernel in [1], it already implies an $O(\mu)$-edge single-failure certificate; the reduction is explained in Section 6. Therefore this manuscript does **not** claim the first asymptotic resolution of the CSR 2022 question. Its contribution is an independent short polyhedral proof, the explicit $4\mu+2$ bound directly in the original graph, and the general sparse-support lemma with additional linear constraints. [5]

## 1. Fractional caps express separate repairability

The case $\mu=0$ is immediate. Assume $\mu\ge1$.

Only failures of edges in $M$ can require a different maximum matching. Let
$$
Q=\{f\in M:\nu(G-f)=\mu\},\qquad k=|Q|.
$$
For each $f\in Q$, choose a maximum matching $M_f$ avoiding $f$. Put
$$
\varepsilon=\frac1{2(\mu+1)(k+1)}.
$$
If $k=0$, return $M$. Otherwise the convex combination
$$
\bar x=(1-k\varepsilon)\chi^M+
\varepsilon\sum_{f\in Q}\chi^{M_f}
$$
is a fractional maximum matching satisfying $\bar x_f\le1-\varepsilon$ for every $f\in Q$. It also satisfies
$$
\bar x(E\setminus M)\le\varepsilon k\mu<1/2.
$$

Let $P(G)$ be the matching polytope. By Edmonds' theorem it is given by
$$
\begin{aligned}
x_e&\ge0 &&(e\in E),\\
x(\delta(v))&\le1 &&(v\in V),\\
x(E(S))&\le\frac{|S|-1}{2}
&&(\text{odd }S\subseteq V,\ |S|\ge3).
\end{aligned}
\tag{1}
$$
Consider the nonempty capped face
$$
K=\left\{x\in P(G):
x(E)=\mu,\quad x_f\le1-\varepsilon\ (f\in Q),\quad
x(E\setminus M)\le1/2\right\}.
\tag{2}
$$
The crucial point is that a cap is a condition on an average of matchings. It does not require one matching to avoid all edges in $Q$ simultaneously.

The last inequality keeps the point near the original matching. For every $x\in K$,
$$
x(M)\ge\mu-1/2.
$$
Since each $x_f\le1$ and $M$ has $\mu$ edges, this implies $x_f\ge1/2$ for every $f\in M$. Thus the positive support automatically contains $M$.

We will prove that $K$ contains a point with at most $4\mu+2$ positive coordinates.

## 2. A support bound with extra linear constraints

It is useful to isolate the polyhedral statement.

**Support lemma.** Suppose a nonempty polytope $K'$ is obtained by intersecting the cardinality-$\mu$ face of $P(G)$ with $k$ additional rational linear inequalities. Then $K'$ contains a point supported on at most
$$
3\mu+k+1
\tag{3}
$$
original edges.

For the algorithmic application, the added inequalities have $0/1$ coefficients. The existence proof works for arbitrary rational added rows; their number, rather than their sparsity, controls (3).

### 2.1 A generic objective

Maximize $c^\top x$ over $K'$, where $c$ is chosen outside the span of every rank-deficient subset of its finite constraint normals. Nonnegativity normals, degree normals, odd-set normals, the cardinality normal, and the added normals are included in this collection.

Such a rational vector exists and can be chosen with polynomial encoding length when the constraint rows have polynomial encoding length. In the $0/1$-row application, enumerate the $m$ edges, take
$$
B=4(m+1)^m,\qquad c=(1,B,B^2,\ldots,B^{m-1}).
\tag{4}
$$
To see why this works, any proper subspace spanned by $0/1$ and signed unit rows has a nonzero integer normal vector $z$ whose entries are bounded by a Hadamard cofactor bound, at most $m^{m/2}$. The largest nonzero term of $\sum_i z_iB^i$ dominates all preceding terms. Therefore $c\cdot z\ne0$. Each coordinate in (4) has polynomial bit length. For rational added rows, clear row denominators and increase $B$ according to the resulting cofactor bound.

Let $x$ be an optimum. Take an optimum dual. Its variables are nonnegative multipliers $y_v$ for degree inequalities, $z_S$ for odd-set inequalities, and multipliers for the added inequalities; the cardinality equality has a free multiplier $\tau$.

### 2.2 Uncrossing still works in the presence of the added rows

Leave the multipliers of all added rows and the cardinality equality fixed during uncrossing. Among optimal dual solutions, choose one lexicographically minimizing
$$
\left(
\sum_S z_S|S|(n-|S|),\
\sum_S z_S|S|
\right),\qquad n=|V|.
\tag{5}
$$
Both quantities are nonnegative linear functions on the optimal-dual polyhedron, so minima are attained.

Suppose two odd sets $A,B$ with positive $z_A,z_B$ cross. Let $I=A\cap B$, $U=A\cup B$, and $\eta=\min(z_A,z_B)>0$.

If $|I|$ is odd, subtract $\eta$ from $z_A,z_B$ and add it to $z_I,z_U$. The dual objective is unchanged because the right-hand sides satisfy
$$
\frac{|A|-1}{2}+\frac{|B|-1}{2}
=\frac{|I|-1}{2}+\frac{|U|-1}{2}.
$$
The edge coefficients only increase, by $\eta$ on edges between $A\setminus B$ and $B\setminus A$; hence the dual remains feasible. The first potential in (5) decreases by
$$
2\eta\,|A\setminus B|\,|B\setminus A|>0.
$$

If $|I|$ is even, replace the same amount of $z_A,z_B$ by multipliers on the odd sets $A\setminus B,B\setminus A$, and add $\eta$ to $y_v$ for each $v\in I$. Again the dual objective is unchanged. Its edge coefficients only increase, this time on edges between $I$ and $V\setminus U$. The first potential decreases by
$$
2\eta\,|I|\,(n-|U|).
$$
If this quantity is zero, the second potential decreases by $2\eta|I|>0$.

Odd singleton rows have both zero coefficients and zero right-hand sides and are simply omitted; omitting them can only further decrease the potentials. Thus either uncrossing contradicts (5). The sets with positive $z_S$ form a laminar family $\mathcal L$.

### 2.3 Counting the tight rows

Complementary slackness gives $x(\delta(v))=1$ whenever $y_v>0$. Since
$$
\sum_v x(\delta(v))=2x(E)=2\mu,
$$
there are at most $2\mu$ such degree rows.

Also, every $S\in\mathcal L$ is tight:
$$
x(E(S))=(|S|-1)/2.
\tag{6}
$$
The maximal members of $\mathcal L$ are pairwise disjoint. For each maximal member $R$, complete its laminar inclusion tree by adding singleton leaves. Every internal node has an odd number of children and, because it is a proper set containing at least three vertices, at least three children. Consequently the number of members of $\mathcal L$ contained in $R$ is at most
$$
(|R|-1)/2=x(E(R)).
$$
Summing over the disjoint maximal roots yields
$$
|\mathcal L|\le\sum_Rx(E(R))\le\mu.
\tag{7}
$$

Let $s=|\mathrm{supp}(x)|$. The dual equality expressing $c$ consists of at most $2\mu$ positive degree rows, at most $\mu$ positive laminar odd-set rows, at most $k$ added rows, the cardinality row, and dual-slack unit vectors on zero coordinates. There are at most $m-s$ of the latter. If
$$
s>3\mu+k+1,
$$
these rows span a proper subspace of $\mathbb R^m$, contradicting the generic choice of $c$.

This proves (3). This use of a generic objective is deliberate: the existence of a laminar optimal dual alone does not imply that its positive rows span the entire minimal face.

## 3. From fractional support to an exact single-fault certificate

Apply the support lemma to (2). There are $k\le\mu$ avoidance caps and one outside-mass cap, so choose $x\in K$ with
$$
|\mathrm{supp}(x)|\le4\mu+2.
$$
Return
$$
E(H)=\mathrm{supp}(x).
$$
The outside-mass cap proves $M\subseteq E(H)$, and $|E(H)|\le4\mu+2$.

Because $x\in P(G)$, it is a convex combination of matching incidence vectors. Because $x(E)=\mu$, every matching with positive coefficient in this combination has cardinality exactly $\mu$. Every such matching uses only edges of $\mathrm{supp}(x)$.

For $f\in Q$, the inequality $x_f<1$ implies that at least one matching in this combination avoids $f$. Therefore $\nu(H-f)=\mu=\nu(G-f)$.

For $f\in M\setminus Q$, the matching $M-f$ has size $\mu-1=\nu(G-f)$ and lies in $H-f$. For $f\notin M$, the original $M$ survives. These cases exhaust all edge failures.

The linear dependence on $\mu$ is optimal up to constants, since even the no-failure query must retain $\mu$ matching edges.

## 4. One vertex or one edge, in the same structure

Only vertices covered by $M$ need a nontrivial vertex-failure response. Let
$$
Q_V=\{v\in V(M):\nu(G-v)=\mu\}.
$$
Add the caps
$$
x(\delta(v))\le1-\varepsilon\qquad(v\in Q_V),
\tag{8}
$$
along with the edge caps and the outside-mass cap. There are at most $2\mu$ vertex caps and $\mu$ edge caps. Take $\varepsilon=1/[2(\mu+1)(k+1)]$, where $k$ is their total number, and put mass $\varepsilon$ on one maximum-matching witness for each avoidance cap, with the remaining mass on $M$. This proves feasibility exactly as before.

The support lemma gives at most $6\mu+2$ positive edges, already containing $M$. In the convex decomposition, a degree expectation strictly below one guarantees a matching leaving that vertex uncovered. The remaining vertex-failure cases are handled by $M$ or by deleting its unique incident matching edge.

## 5. Deterministic construction and output queries

Compute $M$ and test the at most $\mu$ edge failures, or at most $3\mu$ combined edge/vertex failures, that meet $M$. This determines the designated scenarios and supplies their witness matchings.

One construction optimizes the generic objective over the capped matching polytope by rational linear programming with a separation oracle for the matching polytope. Polynomial-time weighted matching optimization, and the standard optimization/separation equivalence, supply the required oracle. The construction is deterministic and polynomial in input encoding length. Its proof does not require constructing a convex decomposition.

There is also a construction using only ordinary maximum-matching computations. Start with the union of $M$ and one witness matching for each designated scenario; this contains $O(\mu^2)$ edges. Process edges outside $M$ in a fixed order, deleting an edge whenever every designated scenario still admits a size-$\mu$ matching. A single pass suffices: once deleting an edge would break a scenario, further deletions cannot restore that scenario.

At termination, apply the support theorem to the retained graph itself, with the same $M$ and the same designated scenarios. It supplies a smaller preserving subgraph with at most $4\mu+2$ edges, or $6\mu+2$ in the combined case, containing $M$. If the terminal graph exceeded the bound, an edge outside this smaller subgraph would still be deletable, contradicting termination. Thus greedy deletion attains the same support bound. It uses $O(\mu^3)$ ordinary maximum-matching calls after the initial witnesses; no fast preprocessing claim is needed.

Store $H$, $M$, and original identifiers. On a query, remove the failed edge or vertex and at most one edge of $M$. The resulting matching is at most one below the new optimum. A single general-graph augmenting-path search therefore either restores cardinality $\mu$ or certifies that the current $\mu-1$ matching is maximum.

A linear-time search can be obtained from the classical skew-symmetric regular-reachability algorithm. Goldberg and Karzanov state the $O(m)$ regular-reachability bound in Theorem 2.2 and give the matching reduction in Section 2.1. This is the appropriate general-graph augmentation primitive; ordinary directed reachability does not suffice. Since $H$ has $O(\mu)$ edges and active vertices, the full query, including writing the matching, takes $O(\mu)$ time and $O(\mu)$ space. Identifier lookup can use a sorted dictionary; its logarithmic cost is absorbed by the output bound. [3]

## 6. The recent matching-covered baseline and the weighted boundary

Here is the inference from [1, 5] that prevents an unsupported first-result claim. Use [1] to obtain a one-edge-fault certificate $K$ on $n'=O(\mu)$ active vertices, with matching number $\mu$. Add $n'-2\mu$ new dummy vertices, each adjacent to every original vertex, with no edges between dummies. The augmented graph has a perfect matching exactly when the original graph has a matching of size $\mu$; the same equivalence holds after any original edge failure.

Remove edges that lie in no perfect matching of the augmented graph. Each remaining connected component is matching covered. A two-vertex component may contain a forced edge. Every larger matching-covered component has no forced edge: if an edge occurred in every perfect matching, each endpoint would have no other allowed incident edge, contradicting connectedness. Replace every larger component by a minimal spanning matching-covered subgraph. The bounds of He and the classical bipartite theorem give $O(n')$ retained edges; small components and parallel-edge cases require only constant-size handling. Each resulting larger component still has no forced edge, so perfect-matching existence after every single edge deletion is preserved. Project retained original edges back to $K$ and add $M$ to handle the cases where the optimum drops to $\mu-1$. This yields $O(\mu)$ original edges. This is a consequence of the cited ingredients, not a theorem attributed verbatim to either paper.

The theorem preserves exact **cardinality**. It does not prove an $O(n^{3/2})$ exact replacement-cost preserver for arbitrary weighted nonbipartite matching.

The fractional-cap argument does extend to a fixed optimal face. For example, intersect with $w^\top x=\mathrm{OPT}$, and cap only baseline edges that some original minimum-cost maximum matching avoids. One additional row changes the support bound by at most one. This preserves whether a failure can be repaired without increasing the original optimum cost. It does not preserve the potentially larger optimum after every failure.

A direct alternating-walk reduction for the stronger weighted question fails. Take two zero-cost triangles $a_1a_2a_3$ and $b_1b_2b_3$, joined only by an edge $a_3b_3$ of cost one. The unique perfect matching is
$$
M=\{a_1a_2,b_1b_2,a_3b_3\}.
$$
In the naive transition digraph, a nonmatching edge $uv$ gives an arc $u\to\mathrm{mate}_M(v)$ of length $w(uv)-w(v\mathrm{mate}_M(v))$. It contains the directed cycle
$$
a_3\to a_2\to b_3\to b_1\to a_3
$$
of length $-2$. Nevertheless $M$ is optimum, and deleting $a_3b_3$ leaves no perfect matching. The corresponding fractional direction removes the bridge twice and violates the odd-cut constraint of either triangle. Setting the bridge cost to zero gives the same infeasibility counterexample with every raw transition length zero, so merely arranging nonnegative arc lengths cannot fix the reduction. Thus the ordinary no-negative-cycle and pair-distance-preserver route cannot simply be reused. The weighted extension would require a new argument preserving legal blossom-aware paths or alternating cycles.

## 7. Integrality alone does not give a linear certificate

The following scope boundary is an elementary construction, without a priority claim. Even maximum independent set in perfect graphs may require $\Omega(\alpha^2)$ retained original vertices to preserve its exact cardinality after one vertex failure, where $\alpha$ is the original independence number.

Let $B=C\cup U$ be independent, with $|C|=q$ and $U=\{u_1,\ldots,u_p\}$. For each $i$, add an independent block $A_i$ of $q+1$ vertices. Put every edge between different $A_i$ blocks. Join every vertex of $A_i$ to all of $C$ and to $u_i$, and to no other vertex of $B$.

An independent set either lies in $B$, or uses only one block $A_i$ and vertices of $U\setminus\{u_i\}$. Thus $\alpha=p+q$, and the maximum independent sets are exactly
$$
B,\qquad J_i=A_i\cup(U\setminus\{u_i\}).
$$
After deleting $u_i$, the unique maximum independent set is $J_i$. Any retained-vertex certificate must therefore contain all $p(q+1)$ vertices in the $A_i$ blocks. Taking $p=q$ gives the quadratic bound.

For completeness, every induced subgraph is perfect. Give each nonempty $A_i$ block its own color, and let their number be $s$. If a vertex of $C$ is present, the clique number and a valid coloring both use $s+1$ colors. If $C$ is absent and $s\ge2$, every remaining $u_i$ can use a block color different from that of $A_i$; this uses $s$ colors, matching the clique number. The cases $s\le1$ are immediate, with a second color needed exactly when an edge is present. The same argument applies to every induced subgraph.

This is a lower bound for retained original vertices, not for an arbitrary encoded value oracle. It illustrates why the laminar-dual or tight-rank dimension argument is substantive: polynomial optimization and an integral feasible-set polytope alone do not imply linear single-fault sparsification.

## References

1. Niranka Banerjee, Manoj Gupta, Venkatesh Raman, and Saket Saurabh. **Output Sensitive Fault Tolerant Maximum Matching.** CSR 2022, pp. 115–132. The publisher abstract states both the general-graph quadratic bound and the linear-size single-edge-failure open question. <https://link.springer.com/chapter/10.1007/978-3-031-09574-0_8>
2. Jack Edmonds. **Maximum Matching and a Polyhedron with 0,1-Vertices.** Journal of Research of the National Bureau of Standards, Section B, 69B (1965), 125–130. The matching-polytope theorem is classical; the uncrossing and support argument needed here is supplied above. See also the original polyhedral algorithmic framework in Grötschel, Lovász, and Schrijver, *Geometric Algorithms and Combinatorial Optimization*, Section 8.5: <https://www.zib.de/userpage/groetschel/pubnew/paper/groetschellovaszschrijver1988.pdf>
3. Andrew V. Goldberg and Alexander V. Karzanov. **Maximum Skew-Symmetric Flows and Matchings.** Mathematical Programming 100 (2004), 537–568. Theorem 2.2 and Section 2.1. <https://arxiv.org/pdf/math/0304290> Their regular-path algorithm originates in **Path Problems in Skew-Symmetric Graphs**, Combinatorica 16 (1996), 353–382.
4. Keerti Choudhary, Amit Kumar, and Lakshay Saggi. **Sensitivity Oracles for Matroid Packing, Matroid Covering, and Matching Problems with Applications.** September 2026 preprint. Arbitrary-update algebraic sensitivity oracles, distinct from the single-deletion sparse original-edge certificate considered here. <https://arxiv.org/abs/2609.01283>
5. Xiaoling He. **The Maximum Number of Edges in Minimal Matching Covered Graphs.** September 2026 preprint, Theorem 1.2. <https://arxiv.org/html/2609.30978v2> The paper also recalls the Lovász–Plummer 1977 bound for minimal bipartite matching-covered graphs.
