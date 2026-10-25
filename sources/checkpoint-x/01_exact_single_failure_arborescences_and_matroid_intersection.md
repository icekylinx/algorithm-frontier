# Exact single-failure preservers and output-sensitive oracles for minimum-cost arborescences and two-matroid intersection

*Incremental research draft. The reduction below is the proposed contribution; the matroid-intersection polytope and directed pairwise distance-preserver bound are classical ingredients. This draft addresses individual element/arc failures, not correlated color failures.*

## 1. Main statement

Let two matroids \(M_1,M_2\) share a finite ground set \(E\), with a fixed rational cost function \(w:E\to\mathbb Q\). Suppose a common independent set of size \(k\ge1\) exists. There is a deterministically constructible set

\[
 S\subseteq E,\qquad |S|=O(k^{3/2}),
\tag{D1}
\]

such that, after deletion of any one element \(f\), whenever a size-\(k\) common independent set still exists, \(S\setminus\{f\}\) contains one of minimum original cost. The no-failure optimum is also retained. Moreover, an associated **\(O(k^{3/2})\)-record deterministic sensitivity oracle reports an optimum solution in \(O(k)\) time**, or reports infeasibility, after any one deletion. It makes no independence-oracle calls at query time. Construction is polynomial with independence oracles. No linear representation, genericity assumption, or random isolation is needed.

In particular, a directed graph on \(n\) vertices, a designated root, and arbitrary nonnegative rational arc costs admit an **exact single-edge-failure minimum-cost spanning-arborescence preserver with \(O(n^{3/2})\) original arcs**, together with an **\(O(n^{3/2})\)-record oracle reporting an optimal arborescence in \(O(n)\) time**. Deterministic preprocessing takes \(\widetilde O(mn)\) arithmetic operations. If a failure destroys all spanning arborescences, the oracle reports that fact. The query bound includes writing all \(n-1\) output arcs.

Dey--Kavitha (May 2026), Theorem 1.1, construct \(O(n^{3/2})\)-arc preservers with approximation factor two; their Section 5 explicitly asks whether sparse exact preservers exist. Subject to independent review of the reduction, (D1) gives an affirmative answer with the same size exponent and exact objective value. The reporting oracle additionally improves their \(O(n^{3/2})\) query bound to \(O(n)\), while preprocessing is within logarithmic factors of their \(O(mn+n^2\log n)\) bound.

Space counts records containing an original element ID, a pointer, or an exact cost; this is a word-space bound when those objects fit in words. Arithmetic-operation bounds treat comparisons and additions of exact costs as unit operations. For a bit-complexity statement, let \(\beta\) bound the bit length of input costs and of every finite value returned by an independence/optimization oracle; the exact rational operations below then have polynomial bit complexity in the explicit input size and \(\beta\). No machine-word bound for arbitrary rational costs is intended. A no-failure query simply reports the stored baseline optimum.

## 2. A compressed exchange graph

Fix a minimum-cost size-\(k\) common independent set \(B\). Equivalently, truncate both matroids to rank \(k\), so that \(B\) is a common basis. All exchange tests below are unchanged by this truncation.

Construct a directed graph \(D\) with vertex set \(B\). For each ordered pair \(a,b\in B\), including \(a=b\), consider the candidates

\[
 X_{a,b}=\{e\in E\setminus B:
 B-a+e\in\mathcal I_1,
 B-b+e\in\mathcal I_2\}.
\tag{D2}
\]

If this set is nonempty, choose a minimum-cost candidate \(e_{a,b}\), breaking ties arbitrarily but consistently, and include one arc \(a\to b\) with label \(e_{a,b}\) and length

\[
 \ell(a,b)=w(e_{a,b})-w(a).
\tag{D3}
\]

Thus \(D\) has \(k\) vertices and at most \(k^2\) arcs. Lengths may be negative. A label can occur on several arcs; this causes no difficulty in the argument below.

For a simple directed cycle \(C\) of \(D\), let \(m_C(e)\) be the number of its arcs labeled by \(e\). Define a vector \(d_C\in\mathbb R^E\) by

\[
 d_C(e)=m_C(e)\quad(e\notin B),\qquad
 d_C(a)=-\mathbf1[a\in V(C)]\quad(a\in B).
\tag{D4}
\]

A loop is a simple cycle with one vertex. We have

\[
 d_C(E)=0,\qquad w\cdot d_C=\ell(C).
\tag{D5}
\]

The multiplicities in (D4) are deliberate: a simple cycle in the compressed graph can repeat an outside-element label.

## 3. The tangent-direction lemma

Let \(P\) be the common-base polytope of the two rank-\(k\) truncations:

\[
 P=\{x\ge0:\ x(E)=k,\ x(A)\le r_i(A)
       \text{ for every }A\subseteq E,\ i=1,2\}.
\tag{D6}
\]

Here \(r_i\) denotes the truncated rank function. The matroid-intersection polytope theorem says that \(P\) is the convex hull of the indicators of size-\(k\) common independent sets.

**Lemma.** For every simple directed cycle \(C\) in \(D\),

\[
 \mathbf1_B+\varepsilon d_C\in P
 \quad\text{when }\varepsilon=1/(k+1).
\tag{D7}
\]

**Proof.** Write \(t=|C|\le k\). In the base polytope of the first rank-\(k\) truncation, the desired point has the explicit convex decomposition

\[
 \mathbf1_B+\varepsilon d_C
   =(1-t\varepsilon)\mathbf1_B
     +\varepsilon\sum_{(a,b)\in E(C)}
          \mathbf1_{B-a+e_{a,b}}.
\tag{D8}
\]

Every displayed exchanged set is a basis of the first matroid, by (D2). The coefficients are nonnegative and sum to one. For the second matroid, use the same formula with \(B-b+e_{a,b}\) instead. Because the cycle's heads and tails are the same vertex multiset, the resulting vector is again exactly \(\mathbf1_B+\varepsilon d_C\). Thus this point lies in both base polytopes, hence in their intersection (D6). Repeated outside labels are counted by their multiplicities in these sums; they require no distinctness assumption. This proves the lemma.

Since \(B\) minimizes the objective over \(P\), the lemma immediately implies

\[
                       \ell(C)\ge0
                 \quad\text{for every cycle }C.
\tag{D9}
\]

Thus the compressed graph has no negative directed cycle, despite possibly having negative arcs.

## 4. Exact replacement value equals a shortest-cycle value

For \(f\in B\), let \(\delta_f\) be the minimum length of a directed cycle of \(D\) containing \(f\), or \(+\infty\) if no such cycle exists. Let \(\operatorname{OPT}_{-f}(k)\) be the minimum cost of a size-\(k\) common independent set avoiding \(f\), with the same infinity convention. Then

\[
            \operatorname{OPT}_{-f}(k)=w(B)+\delta_f.
\tag{D10}
\]

Moreover, if \(C\) is a minimum-length cycle through \(f\), an optimum in (D10) exists using only \(B\) and the outside-element labels on \(C\).

### From a cycle to a replacement

Decompose the point in (D7), using integrality of \(P\), as a convex combination of common-basis indicators:

\[
       \mathbf1_B+\varepsilon d_C
                  =\sum_J\lambda_J\mathbf1_J.
\tag{D11}
\]

Every positive-coefficient \(J\) is contained in \(B\) together with the labels of \(C\): all other outside coordinates in (D11) are zero. It also contains \(B\setminus V(C)\), whose coordinates are one.

The \(f\)-coordinate of (D11) is \(1-\varepsilon\), so the total coefficient of bases avoiding \(f\) is exactly \(\varepsilon\). Every basis has cost at least \(w(B)\). Taking objectives in (D11), the total weighted cost increase is \(\varepsilon\ell(C)\). Hence at least one positive-coefficient basis avoiding \(f\) has cost increase at most \(\ell(C)\). This establishes both the upper inequality in (D10) and the claimed support restriction.

At this point the argument establishes existence within the cycle's labels. An additional minimum-hop choice below will make the entire cycle a valid explicit update.

### From a replacement to a cycle

Let \(J\) be any size-\(k\) common independent set avoiding \(f\). The standard basis-exchange matching lemma gives, separately in each matroid, a perfect matching between \(B\setminus J\) and \(J\setminus B\), using feasible single-element exchanges. Write \(a_i(e)\) for the element of \(B\setminus J\) matched to \(e\in J\setminus B\) by the matching for \(M_i\). For every outside element \(e\), form the directed arc \(a_1(e)\to a_2(e)\) and label it by \(e\). Since both \(e\mapsto a_i(e)\) are bijections, these arcs form a permutation of \(B\setminus J\), and therefore decompose into vertex-disjoint directed cycles, one containing \(f\).

Compress each outside element on one of these cycles to an arc on \(B\). Before minimizing arc labels as in (D2), each cycle's length is its added cost minus removed cost. Each such length is nonnegative by the same tangent-direction argument as above. Their sum is \(w(J)-w(B)\). The cycle containing \(f\) therefore has length at most that sum. Replacing each of its labels by the stored minimum-cost candidate can only decrease its length and gives a cycle of \(D\). Consequently

\[
                  \delta_f\le w(J)-w(B).
\tag{D12}
\]

Together these arguments prove (D10). They also prove that \(\delta_f<\infty\) exactly when a same-cardinality replacement exists. No uniqueness or perturbation assumption was used.

### Minimum-hop optimum cycles give explicit valid updates

Among cycles through \(f\) of weight \(\delta_f\), choose one \(C\) with the fewest arcs, and put \(t=|C|\). Let \(u\le t\) be its number of distinct outside-element labels. The cycle-to-replacement argument provides an optimum \(J\) avoiding \(f\), supported on \(B\) and these labels, and containing \(B\setminus V(C)\). Write \(q=|J\setminus B|\). Then \(q\le u\le t\).

Apply the replacement-to-cycle argument to this \(J\). Its alternating cycle through \(f\) uses some \(s\le q\) outside elements. Compressing and minimizing its labels gives a cycle through \(f\), with \(s\) arcs and weight at most \(w(J)-w(B)=\delta_f\). By the definition of \(\delta_f\), this weight equals \(\delta_f\); by the minimum-hop choice of \(C\), we have

\[
                       t\le s\le q\le u\le t.
\]

Every inequality is therefore an equality. In particular, the labels of \(C\) are all distinct, \(J\) contains all of them, and \(J\) removes all \(t\) elements of \(V(C)\). Consequently

\[
              J=(B\setminus V(C))\cup\{e_{a,b}:(a,b)\in E(C)\}
\]

is an exact optimum after deleting \(f\). This proves explicit update feasibility without a unique-optimum hypothesis. The minimum-hop condition is essential to this argument; an arbitrary minimum-weight compressed cycle was not assumed to be directly toggleable.

## 5. From all shortest cycles to ordinary pairwise distance preservation

Split every \(a\in B\) into \(a^-\) and \(a^+\). Add a zero-length arc \(a^-\to a^+\). Replace each compressed arc \(a\to b\) by an arc \(a^+\to b^-\) of the same length and with the same outside-element label. Call the resulting graph \(D^{\mathrm{split}}\).

For each \(f\in B\), introduce the ordered demand pair

\[
                           (f^+,f^-).
\tag{D13}
\]

The direction of this pair excludes a trivial zero-length split arc. A simple path from \(f^+\) to \(f^-\) is exactly a directed cycle through \(f\) in \(D\), with the split arcs inserted. Therefore

\[
       \operatorname{dist}_{D^{\mathrm{split}}}(f^+,f^-)=\delta_f.
\tag{D14}
\]

There are \(2k\) vertices and at most \(k\) finite demands. For reporting, give each compressed arc the lexicographic length \((\ell(a,b),1)\), and each split arc length \((0,0)\). We minimize weight first and the number of compressed arcs second. Every directed cycle has nonnegative first coordinate and strictly positive second coordinate. Thus every shortest walk is simple, and a shortest demand path yields exactly the minimum-weight, minimum-hop cycle used above. The primary arc lengths may be negative; when a shortest-path implementation requires nonnegative reduced lengths, compute a Bellman--Ford potential from a super-source (there is no negative directed cycle) and apply the usual reduced-cost transformation while retaining the ordered-pair tie coordinate. All arithmetic consists of rational primary coordinates and integer secondary coordinates.

The directed weighted pairwise distance-preserver theorem of Coppersmith--Elkin, restated and given a simplified proof by Bodwin, provides a distance preserver \(Q\) with

\[
                   |E(Q)|=O((2k)\sqrt{k})=O(k^{3/2}).
\tag{D15}
\]

The elementary construction below applies verbatim to lexicographic lengths, so it preserves both coordinates without an assumption about generic costs. Define \(S\) to contain \(B\) and every outside-element label appearing on a nonsplit arc of \(Q\). For \(f\in B\) with a feasible replacement, \(Q\) contains a shortest path for (D13), hence the labels of a minimum-weight, minimum-hop cycle through \(f\). Its explicit update from Section 4 is an optimum replacement in \(S\setminus\{f\}\). If \(f\notin B\), the original optimum \(B\) survives. This proves (D1).

### Deterministic construction of the distance preserver

The standard hitting argument can be made deterministic without a logarithmic size loss. In a phase with \(p\) remaining demands on \(N\) vertices, fix one lexicographically shortest simple path for each demand using a deterministic predecessor tie-break, and set \(L=\lceil N/\sqrt p\rceil\). Include every path of at most \(L\) arcs. For the others, greedily select vertices meeting the largest number of still-unhit paths. At most \(\lceil N/L\rceil\) selections hit a constant fraction: after each selection the unhit count falls by a factor at most \(1-L/N\). Include shortest-path in- and out-trees at the selected vertices. This phase costs \(O(pL+N^2/L)=O(N\sqrt p)\) arcs and satisfies at least a constant fraction of all remaining demands. Repeat; the geometric sum of \(\sqrt p\) gives \(O(N\sqrt{p_0})\). This is the slack-to-complete construction in Bodwin's proof, with greedy coverage replacing sampling.

### Path reporting within the same space bound

Store the actual short paths retained in each phase. At every chosen hub, store an in-tree and an out-tree of lexicographic shortest paths, using \(O(N)\) parent-pointer and arc-ID records; different hubs may store separate copies. For a long demand whose fixed shortest path is first hit at hub \(h\), store a pointer to that hub's two trees. The shortest path from its source to \(h\), followed by the shortest path from \(h\) to its target, has exactly the optimum lexicographic demand distance. This follows because \(h\) lies on the fixed shortest demand path, and shortest-path distances satisfy subpath optimality. This concatenation cannot repeat a vertex: deleting the resulting directed cycle would strictly improve its lexicographic length. Thus it has at most \(N-1\) arcs and can be reported by following at most two tree paths in \(O(N)\) time.

The phase's stored lists and tree records total \(O(pL+N^2/L)\); summing over phases gives \(O(N\sqrt{p_0})\) records. Demand descriptors take only \(O(p_0)\) additional records. With \(N=2k\), an oracle query for \(f\in B\) reports its shortest cycle and performs the valid update above in \(O(k)\) time. The cycle labels are distinct by the minimum-hop lemma. A sorted dictionary for the \(k\) baseline element IDs determines whether \(f\in B\) in \(O(\log(k+1))\) time, absorbed by the \(O(k)\) output bound; if not, the oracle returns \(B\). Infeasible baseline failures have stored infinity flags. No matroid oracle or optimization algorithm is invoked after preprocessing.

## 6. Construction costs and the arborescence specialization

For general independence-oracle matroids, the compressed graph can be built after \(B\) is known using \(O(|E|k)\) independence tests and \(O(|E|k^2)\) elementary processing: for each outside element, list its feasible exchanges in each matroid, and update all eligible ordered pairs. Distance computations and the deterministic sparsifier construction on the \(O(k)\)-vertex graph take polynomial time; dense shortest-path routines give an additional conservative \(O(k^3)\) arithmetic-operation bound. Rational arithmetic has polynomial bit complexity. A standard weighted matroid-intersection algorithm supplies \(B\).

For rooted arborescences, remove arcs entering the root. Take \(M_1\) to be the graphic matroid of the underlying undirected multigraph, keeping opposite arcs as different elements. Take \(M_2\) to be the partition matroid allowing at most one incoming arc at each nonroot vertex. A common independent set of size \(n-1\) is an undirected forest with \(n-1\) edges and therefore gives exactly one incoming arc at every nonroot vertex. A component not containing the root would then have indegree at least one at every vertex and hence contain a directed cycle, contradicting the underlying forest. Thus these common bases are exactly the root-spanning arborescences.

### A sparse auxiliary exchange graph for arborescences

Given a baseline arborescence \(T\), an outside arc \(e=(u,v)\) has exactly one possible exchange in \(M_2\), namely the current tree arc \(b_v\) entering \(v\). Its feasible \(M_1\) exchanges are the tree arcs on the undirected \(u\)-to-\(v\) path in \(T\). We represent these path-to-point transitions without materializing a dense compressed graph.

Take a heavy-light decomposition of \(T\), with tree edges assigned positions in one global base array. Build one segment tree on those positions, with zero-length arcs directed from a child toward its parent. There are \(O(n)\) segment-tree nodes and arcs. Make a normal node \(a\) for each tree arc, and connect it to its corresponding segment-tree leaf with length \(-w(a)\).

For each outside original arc \(e=(u,v)\), cover the tree-edge path \(P_T(u,v)\) by \(O(\log^2 n)\) canonical segment-tree intervals. For each covering interval node \(c\), add an arc \(c\to b_v\), of primary length \(w(e)\), labeled by \(e\). Give precisely these labeled arcs secondary length one; all other arcs have secondary length zero. A directed transition between consecutive normal nodes \(a,b_v\) exists exactly when \(a\in P_T(u,v)\), and its lexicographic length is \((w(e)-w(a),1)\). This is precisely the compressed exchange transition, with all labels retained instead of just the cheapest parallel candidate.

The resulting auxiliary graph has

\[
              N=O(n)\text{ nodes},\qquad
              M=O(n+m\log^2 n)\text{ arcs}.
\tag{D20}
\]

Its segment-tree portion is acyclic, so every directed cycle contains a normal node and at least one labeled arc, and projects to a closed exchange walk. Section 3 implies that every such cycle has nonnegative primary length; its positive secondary length makes it strictly positive lexicographically. Split only the normal nodes into minus and plus copies: arrivals terminate at the minus copy, departures start at the plus copy, and a \((0,0)\)-length arc joins minus to plus. The demands are again \((f^+,f^-)\).

Every exchange cycle realizes an auxiliary closed walk, and every auxiliary demand path projects to a nonempty exchange walk through \(f\). A realization could initially repeat segment-tree nodes, but deleting strictly positive closed subwalks improves its lexicographic length. These two directions show that the minimum auxiliary demand distance equals the lexicographically minimum exchange-cycle length through \(f\). A shortest auxiliary demand path projects to a minimum-weight, minimum-hop exchange cycle. Applying the construction and path-reporting scheme of Section 5 directly to this \(O(n)\)-node auxiliary graph therefore retains only \(O(n^{3/2})\) labeled original arcs and stores \(O(n^{3/2})\) records. Include the baseline tree as before.

Lexicographic shortest-path potentials take \(O(NM)\) arithmetic operations by Bellman--Ford. After reweighting, shortest-path trees from and to all auxiliary nodes can be computed deterministically in \(\widetilde O(NM+N^2)\) time. The demanded simple paths have total length \(O(n^2)\). The phased greedy hitting implementation also takes \(\widetilde O(n^2)\) time: maintain vertex-to-unhit-path incidence lists and a maximum-count heap; when a path is first hit, decrement the count at each of its vertices once. Across phases the demand counts decrease geometrically. Including the chosen tree records and mapping retained labeled arcs back to original IDs is within the same bound.

Thus the complete deterministic preprocessing takes

\[
                             \widetilde O(mn)
\tag{D21}
\]

arithmetic operations, including the initial arborescence computation, since an instance with a spanning arborescence has \(m\ge n-1\). Working storage may include \(O(n^2)\) shortest-path information and \(O(m\log^2n)\) auxiliary arcs; the final oracle retains only \(O(n^{3/2})\) records and original-arc IDs.

For a query, report the stored auxiliary shortest path in \(O(n)\) time, read its visited normal nodes and labeled arcs, and apply the feasible cycle update proved in Section 4. This outputs an optimal arborescence in \(O(n)\) time with no new optimization call. The output is a list of original arcs. The simpler certificate-only variant may instead run the usual minimum-cost arborescence algorithm on the \(O(n^{3/2})\)-arc retained graph, taking \(O(n^{3/2})\) arithmetic operations per query; the path-reporting oracle gives the stronger headline bound.

This is a general directed result. It assumes neither acyclicity, bounded degree, unit costs, nor special failure positions. The certificate consists only of original arcs, and all failures use the same fixed original cost function.

## 7. Maximum-cardinality solutions when rank can fall

Let \(r\) be the maximum common-independent-set size. Deleting one element lowers it by at most one, since a maximum set with that element removed still has size \(r-1\). Construct the certificate and reporting oracle for sizes \(r\) and \(r-1\), interpreting the latter as the empty optimum when \(r=1\). Their union still has \(O(r^{3/2})\) elements and records. A query uses the rank-\(r\) oracle if a same-cardinality solution remains feasible, and otherwise the rank-\((r-1)\) oracle. This reports an exact minimum-cost maximum-cardinality common independent set in \(O(r)\) time, without oracle calls. The case \(r=0\) is constant space and time.

Thus the theorem also applies to exact minimum-cost maximum-cardinality bipartite matching under one edge failure. This is a mathematical specialization; priority for the weighted matching formulation has not yet been checked exhaustively. A cost-only query can store the optimum costs for each baseline failure in each oracle, using \(O(r)\) additional cost records, and return the relevant value after the \(O(\log(r+1))\) membership lookup.

## 8. Equivalence to pairwise distance preservation and two sharp boundaries

### A reverse reduction already using bipartite perfect matching

Let \(G\) be a directed graph on \(N\) vertices with nonnegative costs at most \(W\), and let \(P=\{(s_i,t_i):i\in[p]\}\), \(p\le N\), be reachable nontrivial demands. Self-loops may be removed. Choose a positive rational \(K>(N-1)W\). Add one vertex \(q_i\) per demand and the arcs

\[
             t_i\to q_i\text{ of cost }K,
       \qquad q_i\to s_i\text{ of cost }0.
\tag{D16}
\]

Call the augmented graph \(A\). Every cycle through \(q_i\) pays its own cost-\(K\) arc. A shortest original \(s_i\)-to-\(t_i\) path is simple and costs less than \(K\), so a cycle through \(q_i\) of cost less than \(2K\) exists. Any cycle through another query vertex pays at least \(2K\). It follows that the minimum cycle through \(q_i\) visits no other query vertex and has cost

\[
                         K+\operatorname{dist}_G(s_i,t_i).
\tag{D17}
\]

Encode \(A\) as a bipartite perfect-matching instance: create a left and a right copy of each vertex; include every diagonal edge \(x_Lx_R\) at cost zero; and, for each arc \(x\to y\) of \(A\), include edge \(x_Ly_R\) with the arc's cost. The rank of this assignment instance is \(R=N+p\le2N\). The all-diagonal matching is optimum.

After the diagonal at \(q_i\) fails, every perfect matching includes a permutation cycle through \(q_i\). Other permutation cycles have nonnegative cost and can be replaced by their zero-cost diagonals. Therefore the exact optimum after this one failure is precisely (D17). Any optimum retained by a fault-tolerant matching subgraph must contain a minimum-cost \(q_i\)-cycle, and that cycle contains an original \(G\) shortest path for demand \((s_i,t_i)\). Consequently the original-\(G\) edges represented in any such matching subgraph form a distance preserver for every demand in \(P\).

Let \(\operatorname{DP}(N,p)\) denote worst-case directed nonnegative weighted pairwise-preserver size, and \(\operatorname{MI}(k)\) denote worst-case exact one-failure retained-element size for two-matroid size-\(k\) intersection. The two reductions give

\[
 \operatorname{MI}(k)\le k+\operatorname{DP}(2k,k),
 \qquad
 \operatorname{MI}(N+p)\ge\operatorname{DP}(N,p)
 \quad(p\le N).
\tag{D18}
\]

The lower reduction already uses two partition matroids. Thus the general weighted one-failure problem has, up to constant rescaling of rank, the same size-exponent question as \(\Theta(N)\)-pair directed weighted distance preservation. In particular, the classical \(\Omega(N^{4/3})\) distance-preserver lower bound transfers to

\[
                          \operatorname{MI}(R)=\Omega(R^{4/3})
\tag{D19}
\]

along an infinite family, already for nonnegative weighted bipartite perfect matching. The inherited distance lower bound is not new. This particular assignment reduction concerns two partition matroids; the next independent reduction establishes the arborescence counterpart.

### Arborescences also inherit the distance-preserver lower bound

Bodwin--Grandoni--Parter--Vassilevska Williams (2017), Lemmas 4.5--4.6, already prove that exact one-failure preservation of a single directed weighted \(s\)-to-\(t\) distance has, up to constant factors and vertex rescaling, the same worst-case size as preserving \(\Theta(N)\) ordinary directed weighted demand pairs. That replacement-path equivalence is a classical antecedent to the equivalence above.

There is a particularly simple transfer from their problem to arborescences. Given a nonnegative weighted directed graph \(G\) and distinct vertices \(s,t\), delete arcs leaving \(t\) and add a zero-cost arc \(t\to v\) for every \(v\notin\{s,t\}\). Root this graph \(A\) at \(s\). Deleting the old outgoing arcs of \(t\) changes no simple \(s\)-to-\(t\) path. For any failure set \(F\) of other original arcs, every rooted spanning arborescence contains an \(s\)-to-\(t\) path, so its cost is at least \(\operatorname{dist}_{G-F}(s,t)\). Conversely, a shortest simple \(s\)-to-\(t\) path, together with the zero arcs \(t\to v\) for vertices outside that path, is a spanning arborescence of exactly that cost. Consequently

\[
          \operatorname{OPT}_{A-F}(\text{arborescence})
                  =\operatorname{dist}_{G-F}(s,t),
\]

with equality of infeasibility as well.

An exact arborescence preserver must therefore retain, after every such failure, an \(s\)-to-\(t\) path of the original optimum distance. Its root-to-\(t\) tree path uses none of the added completion arcs. Thus the classical one-failure directed distance lower bound gives an \(\Omega(n^{4/3})\) lower bound for exact one-failure arborescence preservers, already in simple directed graphs with nonnegative rational costs. Together with the \(O(\operatorname{DP}(O(n),O(n)))\) upper reduction, the arborescence size-exponent question is equivalent to the same directed pairwise distance-preserver question. This transfers an existing distance lower bound; it does not improve that bound.

### Two failures already force quadratically many matching edges

Take \(K_{r,r}\), put cost zero on its diagonal edges and cost one on every off-diagonal edge. The no-failure optimum is the unique all-diagonal perfect matching. If diagonal edges \(i_Li_R\) and \(j_Lj_R\) fail, the optimum has cost two and uniquely uses \(i_Lj_R,j_Li_R\), together with all other diagonals. Any cost-two matching must be precisely this transposition: at least the two failed diagonal positions must move, and two off-diagonal edges in a permutation form a two-cycle.

Varying \(i,j\) forces all \(r(r-1)\) off-diagonal edges into an exact two-failure preserver; the no-failure query forces all diagonals. Every one of the \(r^2\) original edges is therefore necessary. This rules out an \(o(r^2)\) universal bound for two-matroid intersection with two failures. This particular example proves a retained-subgraph lower bound for matching. A separate arborescence example follows.

### Two failures force quadratic size for arborescences as well

The zero-cost completion transfer works for any original failure set. It therefore also transfers the quadratic two-failure weighted replacement-path lower bound of Bodwin--Grandoni--Parter--Vassilevska Williams, Theorem 4.4. For clarity, the following directed instance gives the complete argument.

Take zero-cost directed paths \(s=s_0\to s_1\to\cdots\to s_L\) and \(t_L\to t_{L-1}\to\cdots\to t_0=t\). Add \(x_0,\ldots,x_{L-1}\) and \(y_0,\ldots,y_{L-1}\). The arcs \(s_i\to x_i\) and \(y_j\to t_j\) have costs \(K(L-i)\) and \(K(L-j)\); include every \(x_i\to y_j\) at cost one. On failing \(s_i\to s_{i+1}\) and \(t_{j+1}\to t_j\), a surviving \(s\)-to-\(t\) path can choose only cross indices \(a\le i\) and \(b\le j\). Its cost is \(K(2L-a-b)+1\), uniquely minimized at \(a=i,b=j\). Thus each one of the \(L^2\) cross arcs is required by a query. The zero-cost completion from \(t\) makes this an arborescence instance on \(4L+2\) vertices with the same exact optimum for every query. Every exact two-arc-failure arborescence preserver requires \(\Omega(n^2)\) arcs.

The same construction also gives a quadratic *bit-space* lower bound for arbitrary exact cost oracles with two failures. Give cross arc \(x_i\to y_j\) cost \(1+b_{ij}\), with independently chosen \(b_{ij}\in\{0,1\}\), and set \(K=3\). The prescribed cross arc remains uniquely cheapest, and the query answer is \(3(2L-i-j)+1+b_{ij}\). All \(L^2\) bits can be recovered from the query answers. This is the arborescence transfer of the classical replacement-path incompressibility argument, not a new distance-oracle lower bound.

The same topology gives a stronger retained-subgraph boundary for approximation. Fix any finite multiplicative factor \(\alpha\ge1\), choose an integer \(A>\alpha\), put cost zero on the two backbones and all spokes, and give cross arc \(x_i\to y_j\) cost

\[
                              A^{\,2L-i-j}.
\]

Under the same pair of failures indexed by \(i,j\), every reachable cross has indices \(a\le i,b\le j\). The corner \((i,j)\) has optimum cost \(A^{2L-i-j}\), while every other reachable cross costs at least \(A\) times as much. Hence every \(\alpha\)-approximate surviving \(s\)-to-\(t\) path must use this particular cross arc. After zero-cost completion from \(t\), any \(\alpha\)-approximate arborescence must also contain it, because its root-to-\(t\) path costs no more than the whole arborescence. Varying the two failures again forces all \(L^2=\Omega(n^2)\) cross arcs.

Thus **for every fixed factor \(\alpha\ge1\), two edge failures preclude a universally subquadratic-size multiplicative-approximation arborescence preserver**. This uses nonnegative integer costs with exponential aspect ratio, but only \(O(n\log A)\) bits per cost; it is not asserted for polynomially bounded aspect ratio. The preceding exact lower bounds already use polynomially bounded costs.

A variant also rules out subquadratic-bit *self-contained deterministic approximate cost oracles*, with no access to the original input during queries. Independently choose bits \(b_{ij}\) and set cross cost \(A^{2L-i-j+b_{ij}}\). For the query indexed by \(i,j\), write \(w_{ij}=A^{2L-i-j}\). The corner costs \(w_{ij}A^{b_{ij}}\), while every other reachable cross costs at least \(Aw_{ij}\). Hence the optimum is exactly \(w_{ij}\) if \(b_{ij}=0\), and \(Aw_{ij}\) if \(b_{ij}=1\). Any answer satisfying \(\mathrm{OPT}\le\widehat c\le\alpha\mathrm{OPT}\) distinguishes these cases because \(A>\alpha\). The \(2^{L^2}\) bit matrices therefore require distinct oracle states, proving \(\Omega(n^2)\) bits. This does not rely on requiring a retained subgraph. The topology and transfer are explicit; priority for this multiplicative-distance formulation has not been established.

### Cardinality alone has a linear certificate

When all element costs are zero, \(D\) has zero arc lengths and only the existence of a cycle through each baseline element matters. In each nontrivial strongly connected component, retain an in-tree and an out-tree rooted at one vertex; in a singleton component, retain its loop if it has one. At most \(2k\) compressed arcs suffice, so their labels together with \(B\) give at most \(3k\) original elements. If a deletion lowers maximum cardinality, \(B-f\) already attains the new maximum. Hence arbitrary two-matroid maximum-cardinality intersection admits a linear-size one-element-failure certificate. The weighted lower bound (D19) explains why this elementary linear construction cannot preserve general exact costs. The unweighted bipartite matching specialization was already proved by Banerjee--Gupta--Raman--Saurabh (CSR 2022).

## 9. Baselines and proof dependencies

Huang--Sellier, *Robust Sparsification for Matroid Intersection with Applications* (SODA 2024; Mathematics of Operations Research, 2026), construct density-constrained subsets of size \(O(r/\varepsilon)\) preserving a \(3/2+\varepsilon\) approximation of maximum cardinality. Their robustness supports one-way communication and random-order streaming, including unknown future elements. The present static exact weighted single-deletion guarantee is different; it does not improve that unknown-future guarantee.

Choudhary--Kumar--Saggi (September 2026) give randomized algebraic sensitivity oracles for linear-matroid and graph optimization problems under multiple updates. The present oracle is deterministic, covers arbitrary oracle matroids, and also supplies a retained subinstance of original elements, while its failure scope is only one deletion. Banerjee--Gupta--Raman--Saurabh (CSR 2022) preserve unweighted matching cardinality under faults; the exact weighted objective here is a different requirement.

The new candidate is the rank-size reduction from exact single-failure two-matroid intersection to ordinary directed pairwise distance preservation, its output-sensitive reporting form, and its consequence for exact arborescence preservers and oracles. It does not claim a new pairwise distance-preserver bound or a new weighted matroid-intersection algorithm.

The reduction pattern has the explicit classical antecedent of Bodwin--Grandoni--Parter--Vassilevska Williams (2017), who relate weighted directed single-pair replacement paths to ordinary pairwise distance preservation. The additional step here is the exchange-cycle reduction for arbitrary two-matroid intersection and the resulting exact arborescence theorem, together with the lower-bound transfers above.

Agarwala--Alekseev--Vinciguerra (ITCS 2026), Lemma 30, state a closely related minimum exchange-cycle characterization for flipping one element's membership under a unique optimum. Sections 3--4 above prove the support-and-value statement directly from the integral common-base polytope, initially permit repeated compressed labels, and require no unique optimum. The added minimum-hop argument then proves distinctness and valid explicit update rather than assuming them.

The earlier correlated-color reachability direction has a different boundary: Parter--Petruschka's *Preserving Distances in Faulty Colored Graphs*, Theorem 1.6, already gives exponential dependence on the number of failed individual edges represented by the color classes. The present theorem is specifically for one original element failure; it does not overcome that color-failure obstruction.

### Primary references

1. Dipan Dey, Telikepalli Kavitha. *Low-Cost Arborescence Under Edge Faults*. arXiv:2605.13800v1, 13 May 2026. Theorem 1.1 and Section 5. https://arxiv.org/html/2605.13800v1
2. Greg Bodwin. *A Note on Distance-Preserving Graph Sparsification*. arXiv:2001.07741v3, 7 May 2021; Information Processing Letters, 2022. Theorem 3 and Lemma 1; Theorem 3 is attributed there to Coppersmith--Elkin. https://arxiv.org/pdf/2001.07741
3. Don Coppersmith, Michael Elkin. *Sparse Sourcewise and Pairwise Distance Preservers*. SIAM Journal on Discrete Mathematics 20(2), 463--501, 2006. DOI 10.1137/050630696. The directed weighted bound is explicitly restated in reference 2.
4. Michel X. Goemans. *Lecture Notes on Matroid Intersection*, 18.453, 2 May 2017. Basis-exchange matching, common-independent-set polytope, and the graphic/partition arborescence formulation. https://math.mit.edu/~goemans/18453S17/matroid-intersect-notes.pdf
5. Aryan Agarwala, Yaroslav Alekseev, Antoine Vinciguerra. *Linear Matroid Intersection Is in Catalytic Logspace*. ITCS 2026, Article 3, Section 5.1, Lemma 30. https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.3/LIPIcs.ITCS.2026.3.html
6. Merav Parter, Asaf Petruschka. *Preserving Distances in Faulty Colored Graphs*. arXiv:2504.17868v1, 24 April 2025, Theorem 1.6 and Section 5. https://arxiv.org/html/2504.17868v1

7. Gary Hoppenworth, Yinzhan Xu, Zixuan Xu. *New Separations and Reductions for Directed Preservers and Hopsets*. SODA 2025; arXiv:2411.08151v2, Table 1 records the directed weighted upper and lower bounds used in (D18)--(D19). https://arxiv.org/html/2411.08151v2
8. Niranka Banerjee, Manoj Gupta, Venkatesh Raman, Saket Saurabh. *Output Sensitive Fault Tolerant Maximum Matching*. CSR 2022, 115--132. The abstract explicitly distinguishes unweighted matching cardinality. https://link.springer.com/chapter/10.1007/978-3-031-09574-0_8
9. Keerti Choudhary, Amit Kumar, Lakshay Saggi. *Sensitivity Oracles for Matroid Packing, Matroid Covering, and Matching Problems with Applications*. arXiv:2609.01283v1, 1 September 2026. https://arxiv.org/pdf/2609.01283

10. Chien-Chung Huang, François Sellier. *Robust Sparsification for Matroid Intersection with Applications*. SODA 2024, 2916--2940, DOI 10.1137/1.9781611977912.104; Mathematics of Operations Research 51(3), 2643--2666, 2026, DOI 10.1287/moor.2024.0562. Full preprint, Theorems 4, 8, 9: https://arxiv.org/pdf/2310.16827

11. Greg Bodwin, Fabrizio Grandoni, Merav Parter, Virginia Vassilevska Williams. *Preserving Distances in Very Faulty Graphs*. ICALP 2017; arXiv:1703.10293v1. Lemmas 4.5--4.6 give the directed weighted one-failure single-pair equivalence; Theorem 4.4 gives the two-failure quadratic preserver and oracle lower bounds. https://arxiv.org/pdf/1703.10293
