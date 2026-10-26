# Deterministic Exact General Matching through Persistent Integral Carriers and Normalized Routing

**Yilin Liu · GPT-6 Astra Pro**

**Theorem-and-proof manuscript.** The quantitative algorithm is conditional on the explicitly stated primitive interfaces and Contract R.

## Abstract

We organize a deterministic construction for exact maximum-cardinality matching in arbitrary undirected graphs around two interfaces: a persistent representation of the actual integral matching ledgers, and a dynamic minimum-ratio circulation backend with explicit traversal and lifetime guarantees. Our contributions are the carrier representation and its local exposure procedure, an optimum-gap formulation that applies without a perfect-matching promise, exact projection recovery from conserved near-feasible flows, and a sequential routing and normalized sparsification construction with separate structural and construction-work bounds. We prove the matching-side composition and the quantitative parameter balance. The complete time statement is conditional on the explicitly stated external primitive and raw-backend realization contracts. It yields a single deterministic program with logarithmic overhead exponent $4/5$. All returned edges retain their original input identifiers.

## 1. Result, contributions, and proof scope

Let $G$ be an undirected graph given by $n$ vertices and $m$ listed edge records. Loops and parallel records are permitted in the input. Write $m_s$ for the number of distinct nonloop edges and $\nu(G)$ for the maximum matching cardinality.

**Theorem 1.1 (quantitative composition).** Assume the deterministic external primitive interfaces in Section 2 and the complete raw-backend realization contract in Section 11.6. There is one deterministic program that returns an explicit maximum-cardinality matching of $G$, with original edge identifiers, in time

$$
O(n+m)+(m_s+1)
 \exp\!\left[O\!\left(
   (\log(m_s+2))^{4/5}
   (\log\log(m_s+4))^{1/5}
 \right)\right].
 \tag{1}
$$

The constants are independent of the input. The graph may be disconnected, nonbipartite, of odd order, or without a perfect matching. With the exact preprocessing kernel of Section 3.1, $m_s$ in the second term can instead be replaced by an actual edge count $m_H\leq\min\{m_s,O(\nu(G)^2)\}$. The input scan is performed once.

The central contributions are as follows.

1. **Actual integral carriers.** We maintain every integral ledger as an acyclic transportation carrier, retaining zero-valued carrier edges. A batch touching $q$ incidences needs only $O(q)$ forest pivots. At a settled bottom ledger, the carrier induces selected trees of bin weight less than $2L$, together with implicit forward and inverse row assignments.
2. **Local deterministic exposure and arbitrary optimum gaps.** Output-sensitive tight-set discovery and a local forest exchange supply the structural actions. A comparison matching with $K_{\mathrm g}$ additional edges supplies the augmenting prefixes needed by the phase proof. This gives an exact gap driver on every general graph.
3. **Exact projection and direct numerical parameters.** A conserved rational flow with total integral-bound violation below one can be rounded to exact feasibility. True-flow and optimistic-cut recovery give the complete residual peel. Binary ledger periods and independently chosen numerical accuracy give total client work $S E^4\operatorname{poly}(\log S)$.
4. **Sequential routing and normalized ambient sparsification.** We give explicit finite local procedures, a virtual hierarchy with one physical root map, and a scatter–meet–reverse query induction. The static provider has structural quality $\log\Gamma=O((p+r)\log U)$, while its larger construction factor remains local work.
5. **A complete quantitative composition.** We retain selected-edge recourse, late initial update credit, occurrence pools, finite arithmetic, and the full recursive quality product. Their simultaneous balance gives (1).

The proof separates the matching reduction, the geometric module interfaces, and the quantitative composition. Contract R in Section 11.6 is an explicit hypothesis of Theorem 1.1. Each use of that contract is identified before its cost is substituted. The output verifier establishes correctness of an accepted matching; the interface hypotheses and resource analysis establish the conditional running-time bound.

## 2. Model, notation, and inherited primitives

### 2.1 Computational and identity conventions

We use a word RAM with word size sufficient for an input vertex or edge identifier. Input vertex names are integers in $[n]$. Counting/radix sorting of endpoint pairs and compaction therefore take $O(n+m)$ time. All larger integers and rational arithmetic are charged by their actual word operations. A word never stores an uncharged arbitrarily long integer.

All logarithms are base two unless an entropy or exponential potential explicitly uses natural logarithms. The notation $\operatorname{poly}(U)$ always has a fixed absolute degree. Constants in $O(\cdot)$ are uniform in every growing parameter introduced below.

A *lifetime identifier* names one birth-to-retirement instance of a vertex, edge, or exposed occurrence. Reusing an address creates a new lifetime. Parallel edges have distinct identifiers. An *immediate* graph is the graph in which a path is currently defined; two distinct immediate vertices remain distinct even if they later project to the same physical vertex.

For a walk $P$, its raw length counts every traversal. For an ambient path table $\Pi$, $L(\Pi)$ is maximum path length and $C(\Pi)$ is maximum vertex-occurrence congestion, including endpoints. A fixed factor may count a shared endpoint twice. Empty paths retain endpoint annotations.

We separate the following parameters throughout.

| Symbol | Meaning |
|---|---|
| $S=2^s$ | Master size for the subcubic matching problem |
| $U=2s$ | Master logarithmic size for numerical instances of size at most $S^2$ |
| $h=\lceil\log(U+4)\rceil$ | Logarithmic auxiliary factor |
| $K_{\mathrm g}$ | Target matching improvement in a phase |
| $L$ | Integral allocation per row |
| $p,r$ | Routing and degree-band decomposition parameters |
| $K_{\mathrm r}$ | Number of touched-set repair layers |
| $k=2^x$ | Recursive size-reduction factor |
| $\Gamma,F$ | Static structural quality and construction-work factors |
| $P_{\mathrm d}$ | Parent ledger debt in a local projection |
| $P_{\mathrm b}$ | Encoded child-record and recurrence factor |
| $E,D,q$ | Backend cap, rounded numerical cap, and numerical accuracy |

### 2.2 External inputs

We assume the following source results at their indicated interfaces. The bibliography gives primary source locations. Only these local interfaces are inherited; the new parameterized composition is developed below.

| Input | Interface used |
|---|---|
| **[OAI], Sections 3–5** | Deterministic row/bin state identities, logarithmic descriptors, bounded objective and positivity service, and the local exchange-network exploration/lock invariants. Sections 4–8 below specify our representation, gap, numerical parameters, and exact recovery. |
| **[AHLT]** | Deterministic worst-case dynamic forests with link, cut, expose, path extrema, lazy path addition, and rooted ancestor queries; internal degree reduction is permitted. |
| **[CHHIP], Lemma 3.5** | Directed one-edge-out discovery in work proportional to a supplied exploration budget, with the stated bounded-volume output or absence conclusion. |
| **[KMPG], [CKL], and [AN]** | Deterministic center/stable-forest and original-edge weighted tree geometry, including pointwise fixed stretch labels and monotone forest cuts. Section 11.5 states the finite-bit interface used in our composition. |
| **[CGLNPS], [CS21]** | Deterministic balanced-cut and expander-pruning primitives. Section 10 composes them into the degree-band interface, with each call in its actual-size parameter range. |
| **[CS], [CHS], and [KMPS]** | Combinatorial hierarchy, shuffler, and distance-to-cycle geometry at the local interfaces described in Sections 9 and 11. Our sequential work, query, normalization, and raw-lift specifications are separate. |
| **[Gabow]** | A deterministic augmenting-path search from an arbitrary matching, including an exhausted-search outcome, in near-linear work. |

The matching-state localization input has a particularly useful precise form. A projection from an integral parent of floor $c+1$ and debt $P_{\mathrm d}$ to floor $c$ uses a frozen parent. Its threshold networks expose $O(P_{\mathrm d}+1)$ records, keep permanent sink locks, have total source deficit at most $P_{\mathrm d}$, and admit the true/optimistic-region recovery in Section 8. We inherit this locality and its bounded objective/lock accounting from the source framework; an exact flow existence argument alone is not its locality proof.

All external statements are assumed correct, as stipulated for this manuscript. Our own routing, normalization, lifetime, and parameter claims are not assigned to those external results merely because their constructions use them.

## 3. Exact input reductions

### 3.1 Cleanup and an optional quadratic edge kernel

Remove loops, keep one original identifier per unordered nonloop pair, and remove isolated vertices. The empty case returns immediately. Let the remaining simple graph have $v_0\leq2m_s$ vertices.

For the optional kernel, take a greedy maximal matching $M_0$, set $C=V(M_0)$, $c=|C|$, and $I=V(G)\setminus C$. Maximality makes $I$ independent. Keep every $C$-$C$ edge and, for each $u\in C$, at most $c+1$ distinct neighbors in $I$. Call the retained graph $H$, after removing its isolated vertices.

**Lemma 3.1.** The kernel is constructed in linear time and satisfies

$$
\nu(H)=\nu(G),\qquad
 m_H\leq\min\left\{m_s,\binom c2+c(c+1)\right\},\qquad
 c\leq2\nu(G).
 \tag{2}
$$

**Proof.** The endpoints of a maximal matching form a vertex cover, so every matching has at most $c$ edges. If a maximum matching uses an omitted edge $uv$, with $u\in C$ and $v\in I$, then $u$ has $c+1$ retained neighbors in $I$. At most $c$ vertices of $I$ are matched. Replace $uv$ by an edge from $u$ to an unused retained neighbor. Each replacement decreases the number of omitted edges and preserves cardinality. Hence some maximum matching lies in $H$. The reverse inequality follows from $H\subseteq G$. Finally $c=2|M_0|\leq2\nu(G)$. The edge and work bounds follow directly from the construction. ∎

All subsequent workers and verifiers use the same cleaned graph or the same kernel. Original identifiers remain passive labels until the winner is translated once.

### 3.2 An exact subcubic reduction with a decoder for every matching

For the graph to be solved, write $e$ and $v$ for its edge and nonisolated vertex counts. Replace a degree-$d_u$ vertex $u$ by a path with $2d_u-1$ vertices. Its odd positions are incidence ports. Each original edge joins its designated two ports. Let $J$ be the resulting subcubic graph and put

$$
A=\sum_u(d_u-1)=2e-v,\qquad N=4e-v.
 \tag{3}
$$

**Lemma 3.2.** We have $\nu(J)=A+\nu(G)$. Any matching $Q$ of $J$ can be decoded in linear time to a matching of $G$ of cardinality at least $ |Q|-A$.

**Proof.** An original matching lifts by leaving its occupied port available and matching the even path segments on either side. An unmatched gadget leaves its first port free. Each gadget contributes $d_u-1$ internal edges, proving one inequality.

For the converse, let $F$ be the set of external gadget edges of $Q$, viewed on original vertices, and let $t_u=\deg_F(u)$. If $t_u=0$, the gadget contributes at most $d_u-1$ internal edges. If $t_u\geq1$, deleting its occupied odd ports leaves path segments with total matching capacity $d_u-t_u$. Consequently

$$
|Q|\leq |F|+\sum_u(d_u-\max\{1,t_u\})
       =A+|V(F)|-|F|.
 \tag{4}
$$

Here $V(F)$ excludes isolated vertices. Each nonempty tree component of $F$ contributes one to $ |V(F)|-|F|$; each other component contributes at most zero. One edge from each tree component forms an original matching, with cardinality at least $ |Q|-A$. Component traversal gives the decoder. Apply it to a maximum $Q$ and combine the two inequalities. ∎

Choose $S=2^s$ with $N\leq S<2N$, using direct handling of bounded cases. A lifted greedy matching initializes the phase driver. Its remaining optimum gap is at most $\lfloor v/2\rfloor-|M_0|$, by (3).

## 4. The represented matching and minimal tight contractions

### 4.1 Bins, rows, and ledgers

A *bin* $d$ is an odd factor-critical physical block of size $2w_d-1$, where $w_d\geq1$. A *row* is a physical singleton outside the bins, with at most three physical incidences to bins. Let $\mathcal A$ be the rows and $\mathcal D$ the bins. An injection $\mu:\mathcal A\to\mathcal D$ assigns each row along one real incidence. The remaining vertices are explicitly matched pairs or unmatched blockers.

Each assigned bin exposes the endpoint of its assigned incidence, matches that row, and matches its other vertices internally. A free bin exposes one unmatched vertex. Thus the represented matching has cardinality

$$
|Q|=\sum_{d\in\mathcal D}(w_d-1)+|\mathcal A|
                      +\tfrac12|V_{\mathrm{paired}}|.
 \tag{5}
$$

Every valid injection represents a matching of this same size.

For bins $X$, define

$$
\mathcal A(X)=\{a:N(a)\subseteq X\},\qquad
 \eta(X)=|X|-|\mathcal A(X)|.
 \tag{6}
$$

A ledger of floor $c$ has nonnegative incidence allocations $x$, residuals $y_d=L-\sum_a x_{ad}$, and nonnegative debts $p_d$, with

$$
\sum_d x_{ad}=L,\qquad y_d+p_d\geq c w_d.
 \tag{7}
$$

Integral levels have integer values. At a settled bottom level, $c=1$ and $p=0$. Hence, for every nonempty $X$,

$$
L\eta(X)\geq y(X)\geq w(X)>0.
 \tag{8}
$$

In particular, $\eta(X)\geq1$; if $X$ is *tight*, meaning $\eta(X)=1$, then $w(X)\leq L$. A single bin also has weight at most $L$.

The positive top coordinates are $x^0$ and $\sigma_d=y_d^0+p_d^0-Cw_d$. Their logarithmic objective is the sum of their logarithms. Integral carrier normalization below leaves top coordinates unchanged.

### 4.2 Constructive contraction

**Lemma 4.1.** Let a physical edge join distinct bins $i,j$. If $X$ is an inclusion-minimal tight set containing $i,j$, then the union of its bins and its captive rows $\mathcal A(X)$ is factor-critical, has weight $w(X)$, and preserves the represented matching cardinality when contracted.

**Proof.** There are $ |X|-1$ captive rows, so the physical block has size $2w(X)-1$. For any nonempty captive row set $R$, strict surplus applied to $N(R)$ gives $ |N(R)|\geq |R|+1$. Removing any one child bin therefore preserves Hall's condition. This gives a captive-row injection avoiding whichever child contains a prescribed exposed physical vertex. Expose the requested vertex there; in every other child expose its assigned row contact.

To expose a captive row $a$, remove it and reserve $i,j$ for the joining edge. If the other captive rows could not be injected into $X\setminus\{i,j\}$, some row set $R\subseteq\mathcal A(X)\setminus\{a\}$ would satisfy $ |N(R)\setminus\{i,j\}|<|R|$. Strict surplus forces $i,j\in N(R)$ and $ |N(R)|=|R|+1$, with exactly those $R$ captive. This is a proper tight subset of $X$ containing $i,j$, contrary to minimality. Match the reserved contacts across the joining edge, match the remaining rows into their children, and leave only $a$ exposed.

The old injection uses $ |X|-1$ bins for captive rows, so at most one exterior row is assigned into $X$. Preserve that incidence as the exterior assignment of the new bin, if present. Equation (5) is unchanged. ∎

Each contraction stores one immutable record: child-bin records, captive row incidences, the joining edge, and the creation-time captive assignment. To materialize a prescribed exposure, repair that stored assignment by at most one bipartite augmentation for a child exposure, or at most two for a swallowed-row exposure. Each row has at most three incidences. The record tree has total arity linear in physical volume, so dissolution costs that volume times a logarithmic indexing factor. Later global assignment choices do not modify these creation-time records.

## 5. Persistent carriers for the actual integral ledgers

### 5.1 Sparse-batch normalization

A carrier is a forest in the bipartite row/bin incidence graph. It contains every positive allocation; its other edges may have allocation zero. Every off-carrier incidence has allocation zero. We store the actual integral ledger in this form.

**Lemma 5.1 (carrier normalization).** A legal old-to-final batch on $q$ incidences, including incidence births, deaths, or endpoint changes, can be applied and normalized with $O(q)$ signed path operations, cuts, and links. The resulting ledger has the batch's row and column margins and nonnegative integral values.

**Proof.** Read required old values from the designated version and coalesce repeated final writes. Apply the whole batch before pivoting. Cut dead or retargeted carrier edges, update surviving edge values, and keep the $O(q)$ positive off-carrier values in a pending dictionary.

Process one pending incidence $e=(a,d)$. If its endpoints are disconnected, link it. Otherwise traverse the unique carrier path from row $a$ to bin $d$, with every incidence permanently oriented row-to-bin. Let $\theta$ be the minimum value of a path edge agreeing with the traversal. This class is nonempty. Add $\theta$ to $e$; subtract it from agreeing path edges and add it to disagreeing ones. This is a transportation circulation, preserving all margins. Cut one agreeing minimizer, now zero, and link $e$. Retain every other zero edge. A zero minimum is permitted.

Each pending incidence uses at most one pivot. An earlier pivot touches only carrier edges and its own pending edge, so it cannot change an unprocessed pending value. Nonnegativity, integrality, and acyclicity follow at each step. ∎

An edge can become zero without an explicit notification. It remains represented until a charged topology operation removes it. The ledger fields $y,p,w$ are unchanged by every pivot, so (7) and (8) are preserved exactly.

### 5.2 Balanced selected trees and canonical point assignments

Root each carrier component at its minimum-identifier bin. Every row has at least two positive incidences: one positive incidence would equal $L$, exceeding its bin capacity $L-w_d<L$. Its carrier degree is therefore two or three. Keep both incidences of a degree-two row; for a degree-three row keep its two child incidences. Suppress rows to obtain a selected forest with one row-labelled edge per row.

**Lemma 5.2.** Each selected component $T$ has $w(T)<2L$. Its physical volume, including internal rows, is less than $4L$.

**Proof.** A selected component with bin set $D_T$ has $ |D_T|-1$ internal rows. At most one of those rows—the top degree-three row, if present—sends allocation outside the component. Its export $o$ is less than $L$, since at least one retained child incidence is positive. Let $i\geq0$ be incoming allocation from external rows. Then

$$
\operatorname{load}(D_T)=L(|D_T|-1)-o+i
                         \leq L|D_T|-w(D_T).
$$

Thus $w(D_T)\leq L+o-i<2L$. The physical volume is $2w(D_T)-1$. ∎

Assign a degree-two carrier row to its child bin and a degree-three row to its child with smaller incidence identifier. Each bin has only one carrier parent row, so the assignment is injective. To invert at a bin, inspect its parent row and that row's chosen child. These queries use a constant number of rooted forest operations and at most three incidences. This is an implicit representation of the complete current injection.

### 5.3 Persistence and transaction order

Use the worst-case dynamic-tree implementation of [AHLT]. Path clusters store two orientation classes, two minima, and two lazy tags; reversing a path swaps the classes. Internal degree-reduction connectors have zero incidence count and participate in neither allocation extrema nor additions.

Simulate its memory by a persistent balanced dictionary from addresses to words. Every write path-copies the dictionary, and a version is one dictionary root. The extra logarithmic factor preserves polylogarithmic worst-case operations. Frozen read queries may execute in temporary persistent branches and discard them afterward. All addresses and word operations are charged.

Version the full at-most-three incidence list of every row, including zero off-carrier choices, its physical contacts, and lifetime endpoints. Also version any adjacency dictionary read by a historical query. This makes an old version a complete incidence state.

A structural transaction uses the following order.

1. Freeze the pre-event bottom assignment version and create a sparse forward/inverse overlay for the event.
2. Save captive assignments before a contraction. Use the same version plus overlay for all assigned-row deletions.
3. Freeze each projection parent throughout threshold tests, locks, capacity reads, and final recovery.
4. Apply the full child allocation batch and all deleted-row load releases before normalizing that child. Apply preserving deletions separately to coarser ledgers.
5. Publish the new bottom canonical injection after the whole transaction settles.

Unchanged physical matching edges remain implicit through factor-critical records. Materialize only erased physical volume and phase-boundary output. Equation (5) justifies replacing one settled valid injection by another.

## 6. Deterministic local structural actions

### 6.1 Output-sensitive minimal tight-set discovery

For queried bins $i,j$, construct an implicit directed split graph. Each bin has $d_{\rm in}\to d_{\rm out}$. Add doubled arcs from a query source to $i_{\rm in},j_{\rm in}$; from an occupied $d_{\rm out}$ to every neighbor input of its assigned row; and from a free $d_{\rm out}$ to a sink. Outgoing degree is constant. Generate it by inverse assignment queries and the assigned row's three incidences.

For a tight set $X$ containing $i,j$, exactly $ |X|-1$ bins are occupied by captive rows. Include all inputs of $X$, the query source, and outputs of those occupied bins. There is exactly one outgoing split edge and $O(|X|+1)$ induced arcs.

Apply [CHHIP] with doubling budgets up to a constant multiple of $L$. A lazily generated doubled chain beyond the sink, longer than twice the largest returned-volume budget, excludes sink-containing outputs. A returned set is first restricted to vertices reachable from the query source in its original induced digraph. No doubled arc can cross its one-edge boundary, so the input bins form a tight witness containing $i,j$.

Refine this witness using only its captive rows: one unit augmentation in its split network, followed by residual reachability, returns the smallest source-side minimum cut. Tight sets containing the pair are closed under intersection, because $\eta$ is submodular and strict surplus holds on their nonempty intersection. Thus this is the globally inclusion-minimal tight witness. Doubling makes the total work $O((|X|+1)\operatorname{polylog}S)$ on a tight answer and $O(L\operatorname{polylog}S)$ on a certified freeable pair.

### 6.2 Joint exposure inside two small selected trees

If a certified freeable pair lies in different selected trees, enumerate those trees and root them at the pair. Otherwise enumerate its common selected tree $T$, whose physical volume is $O(L)$. A tight set containing both queried bins is contained in $T$: its $ |X|-1$ captive selected edges already connect its bins.

Prune row edges in parallel rounds whenever the row has a third neighbor outside its current component. Record the round and one exterior witness. Queue processing and scans of the smaller pieces give $O(|T|\operatorname{polylog}S)$ work. The final components are maximal tight blocks: within a terminal component every selected row is captive, and a first pruned internal edge prevents any tight set from crossing its split.

Add an artificial infinite-level edge $ij$, delete a minimum finite-level row edge on its cycle, and regard that row as a hole. Replace the hole's original edge by the pair consisting of an original endpoint and its recorded exterior witness. If this closes a cycle, delete a minimum-level edge on it and continue. The hole level strictly decreases. Indeed, at threshold $\ell$, every current edge of level at least $\ell$ lies within an original level-$\ell$ component, while the hole's witness lies outside that component. Any connecting path therefore contains a lower-level edge. The final operation links to one second original tree; deleting the artificial edge separates $i,j$.

All nonterminal exchanges remain in $T$. The second tree is enumerated only at the final link. There are at most $O(L)$ finite levels and total touched physical volume $O(L)$. Orient the two resulting trees to free the pair and record the explicit assignment overlay. This overlay is consumed immediately by the gain. The next settled ledger supplies its own balanced carrier forest.

Consequently, over contractions $X_1,\ldots,X_b$ and $g$ gains, local pair work is

$$
O\!\left(\left[\sum_{a=1}^{b}(|X_a|-1)+Lg\right]
                     \operatorname{polylog}S\right).
 \tag{9}
$$

## 7. An exact optimum-gap phase and binary ledger accounting

### 7.1 Phase specification

Start a phase with represented matching size $q_0$, target $K_{\mathrm g}\geq1$, and

$$
C=s+1,\qquad
 L=\left\lceil\frac{10000CN}{K_{\mathrm g}}\right\rceil,\qquad
 g_*=\max\left\{1,\left\lfloor\frac{K_{\mathrm g}}{100C}\right\rfloor\right\}.
 \tag{10}
$$

If $K_{\mathrm g}>\lfloor N/2\rfloor-q_0$, return LOW immediately with its cardinality justification. Otherwise initialize unmatched vertices as singleton bins, matched pairs as the paired remainder, and no rows or blockers. Initial debts vanish. Use levels $j=0,\ldots,s$ with floors $c_j=C-j$; the bottom floor is one.

At a settled state, perform the first applicable action.

1. **Bin contact.** For an edge between two bins, contract the minimal tight witness if one exists. Otherwise free the pair, expose the joining contacts, match across the edge, and return the two bins to the paired remainder. This increases matching cardinality by one.
2. **Expansion.** At a bin with a paired-remainder contact and cached top slack at least $4C$, make that contact vertex a row and its mate a singleton bin. Assign the row to the new bin.
3. **Pricing.** Request a priced circulation step in the top logarithmic coordinates. Apply a returned step exactly and settle notifications. A valid LOW ends the phase.

The $g_*$-th gain ends the phase immediately. Other structural actions are followed by the reset transaction below. A checked prerequisite or work-cap violation suspends its worker and is a distinct outcome from LOW.

### 7.2 Ledger algebra and erased-volume charges

A tight contraction replaces $X$ by a bin of weight $w(X)$, residual $y(X)$, and debt $p(X)$. Indeed, deleting its $ |X|-1$ captive rows removes $L(|X|-1)$ load, making the new residual $L|X|-\operatorname{load}(X)=y(X)$. All floor inequalities add.

An integral expansion puts $L$ on the new assigned incidence and debt $c_j$ on the child bin. At the top, put $C+1$ on the trigger-parent incidence and $L-C-1$ on the child incidence, with the source positivity service on any remaining coordinates. Eligibility gives enough actual parent slack; the new child slack is one. The guarded positivity service adds total debt less than $S^{-800}$ during a phase.

To erase bins $R$, remove every row assigned into $R$, under the frozen event injection. Redirect each surviving row's allocation from $R$ to its assigned exterior bin and add the same amount of debt there. If $f$ bins of $R$ are free, then $ |R|-f$ rows are removed. Let $I$ be their old exterior allocation and $O$ the redirected allocation. We have

$$
y(R)=Lf+I-O,\qquad
 I\leq L(\eta(R)-f).
$$

Subtracting deleted debt and using (7) gives

$$
\Delta p_{\rm total}=O-p(R)\leq L\eta(R)-c_jw(R).
 \tag{11}
$$

For a gain, its two erased bins are free, so the debt increase is at most $2L$. A failed projection to floor $c$ supplies the complete residual peel $R$ with $L\eta(R)<cw(R)$, as proved in Section 8. In every preserved coarser ledger, $c_j\geq c+1$; (11) therefore decreases debt by at least $w(R)$. The peel creates

$$
f\leq\eta(R)<\frac{Cw(R)}{L}
 \tag{12}
$$

new blockers.

Before the terminal gain, the top debt pays all peeled weight. Hence

$$
\sum_{\rm peels}w(R)\leq2L(g_*-1)+S^{-800},
 \qquad
 \#\mathrm{blockers}\leq2C(g_*-1).
 \tag{13}
$$

The latter follows from the strict inequality (12), integrality, and $CS^{-800}/L<1$. A peel materializes at most $2w(R)$ physical vertices; a gain erases bins of total weight at most $2L$. Also $Lg_*\leq10001CN$. Counting initial vertices, returned volume, expansions, and contraction arities gives $O(CN)$ structural volume. Retaining a largest child at each contraction moves a physical vertex only $O(\log S)$ times per stay in the bin system. Its original degree is at most three. All physical incidence work and all carrier updates over the $s$ levels consequently cost $S\operatorname{poly}(s)$, apart from numerical projection work.

### 7.3 A comparison matching prevents a false LOW

**Lemma 7.1.** If $\nu(J)\geq q_0+K_{\mathrm g}$, the phase cannot return a valid LOW before its $g_*$-th gain.

**Proof.** After $i<g_*$ gains, compare the current represented matching with one of size at least $q_0+K_{\mathrm g}$. Their symmetric difference contains at least $K_{\mathrm g}-i$ vertex-disjoint augmenting paths. Discard those meeting blockers. By (13), at least

$$
K_{\mathrm g}-i-2C(g_*-1)\geq K_{\mathrm g}/2
 \tag{14}
$$

remain.

At a settled state without a bin/bin edge, orient each remaining path from an unmatched endpoint. It starts at a free bin's exposed base. On entering a row, its next matching edge is that row's assigned incidence, entering the next bin at its unique exposed base. That bin's crossing matching edge has already been used, so a simple alternating path must leave by a nonmatching edge. Before reaching the paired remainder, every bin entry is therefore through its base.

Such a prefix cannot end in an assigned bin or enter another free bin through an assigned row. It must reach a bin with a paired-remainder contact. Distinct physical paths have disjoint bin bases and rows. Reassign each prefix row to its preceding bin. The resulting conceptual injection frees $r_0\geq K_{\mathrm g}/2$ distinct contact bins.

Scale the conceptual injection by $L$. Its top column capacities are $L+p_d^0-Cw_d$, nonnegative by top feasibility. Clip overloaded columns; at most $CN$ mass is removed. The existing feasible top allocation ensures completion under those capacities. Source-to-sink residual augmentations never decrease column sink flow, so initially empty contact columns receive at most the removed $CN$ mass. The alternative top slack on the contact set $Z$ therefore satisfies

$$
\sigma'(Z)\geq Lr_0-2CN.
 \tag{15}
$$

This completion is an existence argument. No flow solve is executed to obtain the comparison direction.

If no expansion is eligible, the source cache guarantees $\sigma_d\leq5C$ on $Z$. Allocation arcs and slack arcs both enter bins, so alternative minus current coordinates is a circulation. Every negative logarithmic derivative contribution has magnitude at most one, since the alternative coordinate is nonnegative. There are at most $4N$ such contributions. The positive contribution is at least

$$
\frac{Lr_0-2CN}{5C}-N>12N.
 \tag{16}
$$

Its signed derivative exceeds one half of the sum of absolute individual logarithmic derivatives. The priced-step interface of Section 8.2 excludes LOW in this case. Bounded objective range and positive progress per accepted step also preclude endless pricing. ∎

Thus a LOW after $i$ gains means precisely $\nu(J)<q_0+K_{\mathrm g}$, while the current matching has size $q_0+i$.

### 7.4 Binary resets and additive projection volume

Give level $j$ period $b_j=2^{s-j}$. Expansions and contractions add one tick; repaired gains add $L$; peels add none. On a positive tick increase, reset the smallest $j\geq1$ whose period quotient changes. A reset at level one uses all-expanded exact exchange recovery. At $j>1$, project from the just-current normalized parent, freeze it for the complete call, and share the settled child's persistent roots with deeper fresh levels.

Total ticks are $\tau=O(sS)$. If $j>1$ is selected, no $b_{j-1}$ boundary was crossed. Since expansions add at most $C$ debt per tick and gains at most twice their tick increase, the parent's debt obeys

$$
P_{\mathrm d}\leq(C+2)b_{j-1}.
 \tag{17}
$$

This applies to large tick jumps as well: crossing a coarser boundary would select that coarser reset. There are at most $\tau/b_j$ selections of level $j$, and $b_{j-1}=2b_j$. Consequently

$$
\sum_{\text{higher resets}}(P_{\mathrm d}+2)
 \leq\sum_{j=2}^{s}\frac{\tau}{b_j}
                         ((C+2)b_{j-1}+2)
 =O(s^3S).
 \tag{18}
$$

There are $O(s)$ level-one resets. Applying a structural batch to $s$ ledgers is an additive factor; the numerical accuracy is chosen independently below.

### 7.5 The optimum-gap driver

Maintain an integer $B\geq\nu(J)-|Q|$. While $B>0$, set $K_{\mathrm g}=\lceil B/2\rceil$ and run a phase.

~~~text
SUCCESS with g gains:       B <- B - g
LOW after i gains:          B <- K_g - 1 - i
SUSPENDED:                  suspend this worker
~~~

Both numerical updates preserve the bound, by Lemma 7.1 and integrality. For $B$ above a fixed multiple of $C$, success reduces it by an $\Omega(1/C)$ fraction, while LOW approximately halves it. Below that threshold, each success gains at least one. There are $O(C(1+\log N))=O(s^2)$ phases. At $B=0$, materialize the maximum gadget matching and use Lemma 3.2.

## 8. From raw circulations to exact projection

### 8.1 The raw numerical interface

For an oriented graph with positive integral lengths $\ell$ and integral gradient $\gamma$, put

$$
\rho^*=\sup_{\substack{Bc=0\\c\ne0}}
           \frac{|\gamma^{\mathsf T}c|}{\sum_e\ell_e|c_e|}.
 \tag{19}
$$

Here $B$ is the incidence matrix; take $\rho^*=0$ when there is no nonzero circulation. A backend answer consists of unit signed real-edge pieces and signed paths in exposed occurrence forests. Their total projects to a circulation $c$. A certificate $V$ dominates the sum of lengths of **all mapped traversals before cancellation**, and the useful answer guarantee is

$$
\frac{|\gamma^{\mathsf T}c|}{V}\geq\frac{\rho^*}{E}.
 \tag{20}
$$

Zero-score cases may return a certified zero alternative. A complete cap $E$ also bounds initialization per actual record, amortized edits and queries, exposed logs, occurrence multiplicity, and answer pieces. The interface includes disconnected graphs, genuine loops, native identities, stable path images, dormant occurrences, and complete retirement transfers. Numerical instances have actual nominal size at most $S^2$, $O(s)$-bit root prices, and a fixed polynomial master history. Section 11.6 specifies the realization obligations used by Theorem 1.1.

### 8.2 A direct master-scale priced client

Set

$$
D=\operatorname{pow2ceil}(\max\{16,4E\}),\qquad
 q=\frac1{16D},\qquad
 \delta=S^{-1000},\quad \varepsilon=S^{-3000},
 \quad H_{\rm price}=S^{100}.
 \tag{21}
$$

The logarithmic client has coordinate gradient $g$ and absolute derivative weight $\lambda$, counting individual logarithms before signed cancellation. At anchors use integer prices $\ell_e=\lceil H_{\rm price}\lambda_e\rceil$ and $\gamma_e=\operatorname{round}(H_{\rm price}g_e)$. Source argument and magnitude bounds give $\ell_e\geq S^{80}$ and prices below $S^{1200}$. Degree-three private port paths add at most $2M\sum_e|d_e|$ length to a logical circulation, with $M\leq S^2$. Thus any logical direction

$$
g^{\mathsf T}d>\tfrac12\sum_e\lambda_e|d_e|
 \tag{22}
$$

has integer-priced lifted ratio greater than $1/4$. With (20), $E\leq D/4$, and $1/(4D)>2q$, it passes the acceptance test $ |\gamma^{\mathsf T}c|\geq2qV$. This proves the no-LOW implication used above.

Choose one common dyadic step coefficient $\mu$ satisfying

$$
\frac q{400}\leq\frac{\mu V}{H_{\rm price}}\leq\frac q{200}.
 \tag{23}
$$

The raw traversal bound controls every partial application of the path list, so positivity is preserved throughout. Coordinate drift thresholds are dyadic values in

$$
\frac{qH_{\rm price}}{800D\ell_e}
 \leq\theta_e\leq
 \frac{qH_{\rm price}}{400D\ell_e}.
 \tag{24}
$$

The source descriptor/Taylor argument now gives exact $\varepsilon$-grid circulation steps, total relative absolute motion at most $q/100$, objective increase $\Omega(q^2)$, and settled register error at most $q/100$. A report consumes at least $q/(800D)$ raw priced motion, while one step creates at most $q/200$; genuine reports therefore number $O(D)$ per step. Common-grid compatibility and these conclusions require the checked inequalities $q\geq S^{-1}$ and $D\leq S^2$, which hold eventually for the subpolynomial cap obtained below.

Let $J_{\rm step}$ count accepted steps and $Q_{\rm own}$ requests from the owning client, including LOW and unsuccessful requests. Internal refreshes are counted separately. Complete initialization, point access, copy sweeps, and refresh work are bounded by

$$
T_{\rm priced}
 \leq O(MD+Q_{\rm own}D+D^2J_{\rm step})
                                      \operatorname{poly}(s).
 \tag{25}
$$

All exposed copies, including dormant ones, remain on signed and absolute-motion lists. Retirement transfers both counters before metadata expires. Obtaining and consuming or discarding a query answer is one transaction; representation-triggered refreshes are queued until afterward. Mutable numerical trees have one amortized history. The persistent integral carrier is a separate worst-case structure.

### 8.3 Exact rounding below one unit of violation

**Lemma 8.1 (conserved near-feasible rounding).** Let $f$ satisfy integral vertex demands exactly in an oriented multigraph with integral lower and upper bounds $l\leq u$. If

$$
\operatorname{viol}(f)=
 \sum_e((l_e-f_e)_++(f_e-u_e)_+)<1,
 \tag{26}
$$

then a deterministic algorithm finds an integral feasible vector with the same demands in $O(m\log(m+2))$ scalar/dynamic-tree operations, plus $O(n+m)$ input/demand bookkeeping if isolated vertices are supplied. A dyadic $b$-bit input uses $O(b+\log(m+2))$-bit arithmetic.

**Proof.** Restrict coordinate $e$ to $[\lfloor f_e\rfloor,\lceil f_e\rceil]$. On this box the original violation equals $a^{\mathsf T}x+\kappa$, with integral constant $\kappa$ and $a_e\in\{-1,0,1\}$, according as the original coordinate violates its lower bound, violates its upper bound, or is feasible. The total violation assumption places a violating coordinate less than one unit outside its bound, so these affine formulas hold throughout the box.

Freeze integral coordinates. Maintain a forest of nonintegral edges. Each off-forest edge closes a fundamental circulation; choose its sign with nonpositive $a$-cost and push maximally inside the rounding box. At least one edge becomes integral. Mask and enumerate all simultaneous zero residual minimizers on the exposed path before cutting them, then freeze and remove them. If the processed edge remains nonintegral, link it. A self-loop is a one-edge cycle.

Each edge is processed, linked, and removed at most once. The remaining fractional support is a forest. A nonempty fractional forest would have a leaf whose divergence is nonintegral after all other incident coordinates have become integral, contradicting the integral demand. Hence the final vector is integral. Its violation is a nonnegative integer no larger than the original value below one, so it is zero. Pushes are differences of dyadic coordinates and integer endpoints; no new denominator is introduced. ∎

### 8.4 Exact exchange and its residual peel

For an integral ledger and target floor $c$, put

$$
b_d=(cw_d-y_d)_+,\qquad
 u_d=(y_d-cw_d)_+,\qquad \beta=\sum_db_d.
$$

The exchange network has arcs $s\to d$ of capacity $b_d$, $d\to t$ of capacity $u_d$, and, for each incidence $e=(a,d)$, separate arcs $d\to a$ of capacity $x_e$ and $a\to d$ of capacity $L+1$. An integral maximum flow $F$ gives

$$
x'_e=x_e-F_{d,a}(e)+F_{a,d}(e),\qquad
 y'_d=y_d+F_{s,d}-F_{d,t}.
 \tag{27}
$$

Row conservation preserves sum $L$, and a row-to-bin arc cannot saturate its capacity $L+1$. If the value is $\beta$, all deficits are filled.

Otherwise let $R$ be all residual-reachable bins from $s$. The combined residual capacity from bin $d$ to row $a$ is exactly $x'_e$. A reachable row reaches all its neighboring bins. Therefore precisely the captive rows supply allocation to $R$, and

$$
y'(R)=L\eta(R)<cw(R).
 \tag{28}
$$

Outside $R$, deficits are filled. Restrict the new allocation after deleting $R$ and its assigned rows; a surviving row has no positive allocation into $R$. This is the exact zero-debt child needed by Section 7. When the frozen parent satisfies floor $c+1$, $\beta\leq P_{\mathrm d}$. Its captive rows also give $y_{\rm parent}(R)\leq L\eta(R)$, so
$(c+1)w(R)\leq y_{\rm parent}(R)+p(R)\leq L\eta(R)+P_{\mathrm d}<cw(R)+P_{\mathrm d}$.
Thus $w(R)<P_{\mathrm d}$.

### 8.5 Recovering the exact local maximum without another feasibility solver

The inherited localized threshold engine uses fewer than $1000(P_{\mathrm d}+1)$ ordinary arcs. Multiply capacities by 16, let the return arc $t\to s$ have value $z$, and test threshold $b$ with $T=16b$ and return weight $W=20000(P_{\mathrm d}+1)$. The objective is

$$
\Phi=\sum_{\text{ordinary }e}
  [\log(F_e-l_e+\zeta_e^-)+\log(U_e+\zeta_e^+-F_e)]
                  -W\log(T-z).
 \tag{29}
$$

The iterate is exactly conserved. Its ordinary unpadded violation is at most $\alpha<S^{-800}<1/100$. Positive locks occur only on sink arcs. An unexpanded boundary's flow stays below $10u_d$, while its true scaled sink capacity is $16u_d$. Success means $z\geq16b-1/4$; LOW has the strong-direction exclusion (22).

On success, discard locks, divide by 16, install true ordinary capacities, and give the return arc bounds $[b,\beta]$. Total violation is at most $1/64+\alpha/8<1$. Lemma 8.1 returns a true integral flow of value exactly $b$, because its return rounding interval has upper endpoint $b$.

For the final LOW test immediately above the optimum, write $b=v+1$, where the unlocked optimistic maximum is $v$. Locked bounds are feasible by Lemma 8.1. A feasible locked flow can reach the unlocked maximum without decreasing sink-arc flows: simple source-to-sink residual augmentations never use an arc leaving the sink. This proves existence of a lock-respecting comparator of value $16v$.

Put $d=16v-z$. If $d\geq8$, its return derivative is $Wd/(16+d)\geq W/3$, while total negative ordinary contributions are below $2000(P_{\mathrm d}+1)$. Their signed-to-absolute ratio exceeds one half, contradicting LOW. Thus $z>16v-8$. Removing locks and dividing by 16 gives violation below $1/2+\alpha/8<1$ with return lower bound $v$. Rounding returns an optimistic maximum flow of value $v$, and residual reachability returns its minimum cut.

Run $O(s)$ threshold tests to obtain the proposed optimum $v$; retain or rerun success at $v$ and LOW at $v+1$, with the natural one-sided cases at $0,\beta$. Check conservation, bounds, integrality, flow value, and cut capacity. An optimistic boundary cannot lie on the source side of this cut, since its sink capacity is $\beta+1>v$. Hence all outgoing full-network arcs of that cut are represented, and it is also a full cut of capacity $v$.

For the complete residual peel, unite the success and failure regions by original arc identifier, install true capacities, and extend the true success flow by zero. Equality of its value and the full cut capacity prevents any full residual arc from leaving that cut. Forward residual arcs inside it are present in the failure region; positive-flow reverse arcs are present in the success region. Reachability in the union is therefore exactly full residual reachability. All residual searches omit the numerical return arc.

This recovers (27) and the entire peel with $O(P_{\mathrm d}+1)$ records. All-expanded recovery uses the same argument with its actual graph volume in place of $P_{\mathrm d}+1$.

### 8.6 Complete matching-client cost

Each local threshold has objective range, including insertion and lock losses, $O((P_{\mathrm d}+1)s)$. Progress $\Omega(q^2)$ gives

$$
J_{\rm step}=(P_{\mathrm d}+1)D^2\operatorname{poly}(s),
 \qquad
 Q_{\rm own}=(P_{\mathrm d}+1)D^3\operatorname{poly}(s).
$$

Its nominal lifetime is at most $8192(P_{\mathrm d}+1)$, with power-of-two rounding $M=\operatorname{pow2ceil}(16(R+2))$. Equation (25), all $O(s)$ tests, rounding, and final recovery consequently cost

$$
T_{\rm projection}\leq
       (P_{\mathrm d}+1)D^4\operatorname{poly}(s).
 \tag{30}
$$

The top client uses $R_{\rm top}=S(s+1)^{10}$ and costs $SD^4\operatorname{poly}(s)$. By (17), local lifetimes are $O(sS)$; both top and local nominal sizes are below $S^2$ eventually. Root prices and logical capacity bounds are fixed before choosing $D,q$; repricing reuses endpoint slots.

Sum (30) using (18), add $O(s)$ all-expanded resets and structural work, and then include $O(s^2)$ phases. Since $D=O(E)$, the complete matching-side reduction is

$$
T_{\rm match}\leq S E^4\operatorname{poly}(s).
 \tag{31}
$$

Loose polynomial action, lifetime, and iteration guards are declared first. On their prefixes, tiny pad changes have total size below $S^{-800}$; the sharper objective and locality counts then imply eventual nonfailure when $E=S^{o(1)}$. This order establishes precision premises before using the final fast-time bound.

## 9. Sequential expander routing with explicit paths

The routing construction is useful because its output quality depends linearly on a depth parameter in the logarithmic exponent, whereas expensive local construction remains a separate cost.

**Proposition 9.1 (routing assembly).** On a connected loopless $m'$-edge multigraph of conductance at least $\phi>0$, and with master logarithmic inventory bound $U$, the hierarchy and local constructions specified below give preprocessing work

$$
m'\exp O(U/p+ph+\log\phi^{-1})\operatorname{poly}(U).
 \tag{32}
$$

A query with at most $D_{\rm tok}\deg(v)$ starts and destinations at every vertex returns explicit simple paths with length at most $Q$, edge-occurrence congestion at most $D_{\rm tok}Q$, and work at most $m'D_{\rm tok}Q\operatorname{poly}(U)$, where

$$
Q=\exp O(ph+\log\phi^{-1}).
 \tag{33}
$$

The polynomial degrees and constants are independent of $p$. The geometric hierarchy uses the module interfaces from [CS, CHS] and Contract R. The following subsections specify these interfaces and prove the sequential replacement and cost bounds used in the composition.

### 9.1 Incidence ports and actual-size recursion

Give each incidence a port. A vertex of degree $d$ receives a cube fiber with the next power of two above $d$ ports, and each genuine edge joins its designated ports. The elementary cube inequality

$$
|\partial X|\geq\min\{|X|,|V(Q_a)\setminus X|\}
 \tag{34}
$$

follows by induction on cube dimension, splitting the cut between the two smaller cubes and their joining matching. The port graph has at most $4m'$ vertices, $O(m'\log(m'+2))$ edges, and degree $O(\log(m'+2))$.

For a port cut, let $z$ be the number of minority ports over fibers. Internal cube boundaries contribute at least $z$; comparison with the majority-side original vertex cut contributes at least $c\phi\min\{|X|,|\overline X|\}-O(z)$ external crossings for a fixed $c>0$. Thus port-graph conductance is at least $\phi/O(\log(m'+2))$. This loss is a fixed polynomial in $U$. Distribute starts and destinations cyclically among genuine incidence ports; each port receives at most $D_{\rm tok}$ of either.

For the actual port graph order $n'$, put $v=\lceil\log(n'+2)\rceil$ and

$$
b_{\rm route}=2^{\max\{5,\lceil v/p\rceil\}},\qquad
 \lambda_{\rm cap}=C_\lambda(v+1)^2.
 \tag{35}
$$

Stop hierarchy recursion when an actual node has at most $C_{\rm leaf}b_{\rm route}^5\lambda_{\rm cap}^2$ vertices, with fixed sufficiently large constants. This is a leaf test, not an allocated padded graph. The depth is $O(p)$. A genuine internal partition has $2b_{\rm route}/3\leq t_{\rm part}\leq b_{\rm route}$, parts of size $\Theta(|X|/b_{\rm route})$, and $n'_X=6|X|/b_{\rm route}$. In particular $t_{\rm part}\geq16$. Its parts satisfy

$$
\min_i|Y_i|\geq8\lambda t_{\rm part}^2,\qquad
 n'_X\geq\lambda t_{\rm part}^2,\qquad
 t_{\rm part}\leq b_{\rm route},\quad \lambda\leq\lambda_{\rm cap}.
 \tag{36}
$$

These are the integer guards used in the query proof.

### 9.2 Short paths, actual cuts, and success coverage

The local matching primitive maintains a breadth-first-search tree truncated at depth $d+2$, with a supersource and supersink. Extract a shortest path of length at most $d$, delete all its physical vertices, and continue. Distances only increase; each arc is scanned $O(d+2)$ times. This gives an exact maximal packing of short vertex-disjoint paths in $O((n+m)(d+2))$ work. Processing at most $b_{\rm route}$ colors sequentially costs an additional construction factor $b_{\rm route}$, while the union remains vertex-disjoint in one round.

For $d=O(\Delta\psi^{-1}\log(n+2))$, either enough short paths are found, or distance balls give an actual sparse cut. A ball has some radius with relative growth $O(\log n/d)$, since the product of growth ratios is at most $n$. Temporarily isolated path vertices have total boundary at most $\Delta$ times their count; the small-packing inequality pays that restoration boundary. Every reported cut is therefore a cut of its declared full host.

Repeated matching rounds use the full unchanged host, update only matched terminal lists, and start with an empty exclusion set. In outer round $j$, use cutoff $\psi/(16j^2)$. The convergent boundary budget controls the union of failure cuts. Exact single-color covering either saturates every remaining source or returns an actual cut containing every uncovered source. All leftover terminals are thereby represented.

A weak cut-or-expander call on a current $N$-vertex host returns either a cut of size between $\beta N$ and $N/2$, or a virtual expander on at least $(1-\beta)N$ vertices, where $\beta=1/1000$. Spectral leaves remove small cuts only until the removed union first reaches $\beta N$. If they instead certify expansion, the retained graph has the same $(1-\beta)$ coverage. An exact rational Laplacian PSD test and a weighted-median sweep implement this leaf/coarse-cut decision in fixed polynomial local work.

The strong wrapper removes disjoint weak cuts until their union first reaches $N_0/4$, or retains the single final weak success. At a cut exit the removed union is below $5N_0/8$; complementation loses less than $5/3$ in sparsity. At a success exit, coverage exceeds

$$
(1-\beta)\frac{3N_0}{4}>\frac{2N_0}{3}.
 \tag{37}
$$

There are $O(1/\beta)$ weak calls. In a promised expander root, every actual-host cutoff is strictly below true sparsity. A first removed cut is impossible. Covering therefore covers the entire root; a first coarse removal is likewise impossible because its block boundary is exactly the corresponding original-host cut. Root coverage is exact.

### 9.3 Half-matching entropy progress

**Lemma 9.2.** Let an abstract $N$-vertex graph be the multigraph union of previous matchings. Suppose a continuing cut has $N/4\leq |S|=a\leq N/2$ and boundary at most $a/8$. Adding a matching from $S$ to its complement of size at least $a/2$, with lazy averaging on matched pairs, increases total transition entropy by at least $5N/1024$.

**Proof.** Write $p(j,k)$ for the previous doubly stochastic transition matrix. Unit mass initially on $S$ sends at most one half-unit across each previous crossing matching occurrence. Thus cross-cut mass in either direction is at most $a/16$.

Let $S_*$ be the new matching's source endpoints. The total mass $p(j,k)$ for $j\in S,k\in S_*$ is at least $a/2-a/16=7a/16$. Call a matched triple good if $p(j,k)\geq2p(j,\ell(k))$. Bad triples have total source-side mass at most twice the cross-cut mass, namely $a/8$. Good mass is therefore at least $5a/16\geq5N/64$.

For entropy density $H(z)=z\ln(1/z)$, averaging $u,w$ with $w\leq u/2$ gains at least $u/16$. Divide by $u$ and differentiate the resulting one-variable function; its minimum on $w/u\in[0,1/2]$ is $\frac12\ln(32/27)>1/16$. Every other pair has nonnegative gain by concavity. Multiply by the good-mass bound. ∎

Entropy lies in $[0,N\ln N]$, so $512\lceil\log(N+2)\rceil$ continuing rounds are more than sufficient. Every repeated matching occurrence remains a distinct multigraph edge.

### 9.4 Virtual hierarchy and polynomial local construction

Each successful node exports an explicit graph on exactly its terminal set $X$, partitioned as

$$
X=\dot\bigcup_{i=1}^{t_{\rm part}}Y_i,\qquad
 Y_i=X_i\dot\cup B_i,
 \tag{38}
$$

where an injective covering matching maps $B_i$ into the good child $X_i$. Child graphs and covering edges are inserted literally in the parent virtual graph. In particular, each good child graph is induced in the virtual root. A path interior is stored in the embedding and does not enlarge its terminal set.

The retained hierarchy has one physical map $f_0:H_{\rm root}\to G^\diamond$. Its length and congestion are $\phi^{-O(1)}v^{O(p)}$. Nonroot construction hosts are unions of $O(v)$ matchings, with degree $O(v)$; a success object ends its game. Their expansion losses are polynomial in $v$ per depth. Thus only the original root pays the original inverse conductance. Within one depth, good-node edge inventories are disjoint. Build shufflers and leaf circuits only after retaining the final hierarchy, union their primitive paths in the virtual root, and apply $f_0$ once. The complete primitive family has

$$
A_{\rm fam}=\phi^{-O(1)}v^{O(p)}
 \tag{39}
$$

as a common path-length and aggregate congestion bound.

Here are finite algorithms for the remaining local computations.

**Energy cut player.** For rational centered row vectors $v_i=R_i-\overline R$, let $\Phi=\sum_i\|v_i\|^2$ and $a_0=\lceil\log_4(8t_{\rm part}^3)\rceil$. Choose signs $z\in\{-1,1\}^{t_{\rm part}}$ by conditional expectations of

$$
\Psi(z)=\sum_i\langle v_i,z\rangle^2
 -t_{\rm part}\Phi\sum_{i<j:v_i\ne v_j}
 \left(\frac{\langle v_i-v_j,z\rangle^2}
 {8a_0\|v_i-v_j\|^2}\right)^{a_0}.
 \tag{40}
$$

The even-moment inequality
$\mathbb E\langle d,z\rangle^{2a_0}\leq(2a_0)^{a_0}\|d\|^{2a_0}$
gives $\mathbb E\Psi\geq7\Phi/8$. A maximizing conditional choice gives projected energy at least $7\Phi/8$, while every projected pair distance squared is at most $8a_0$ times its true distance squared. Sort the projections, take the heavier of the top and bottom eighth-tails relative to the median, and pair it with the opposite half. The sets $T,T'$ satisfy, for every map $\sigma:T\to T'$,

$$
\sum_{i\in T}\|R_i-R_{\sigma(i)}\|^2\geq\frac{\Phi}{512a_0}.
 \tag{41}
$$

Saturating the physical source clusters gives a fractional matching matrix with source row mass at least $1/18$. Its lazy symmetric update decreases $\Phi$ by at least $\Phi/(18432a_0)$. Hence $\lambda=O(\log(t_{\rm part}+2)\log(n'+2))$ rounds give a stochastic product within $1/(100t_{\rm part})$ of uniform in every entry.

Conditional even moments are computed by the recurrence

$$
M'_j=\sum_{\substack{0\leq z\leq j\\z\ {\rm even}}}
                       \binom jz d^z M_{j-z}.
 \tag{42}
$$

They need a fixed polynomial number of operations on polynomial-bit rationals. The larger temporary integers are charged to construction.

**Leaf circuits.** On an actual leaf of order $a$, maximum degree $\Delta$, and edge expansion $\psi$, use a symmetric lazy walk assigning probability $1/(2D_0)$ to each oriented edge, with $D_0$ a power of two above $\Delta$. In
$T=O(\Delta^2\psi^{-2}\log(a+2))$ steps its transition entries are at least $1/(2a)$. Route each bounded-load demand through a uniform intermediate vertex by two conditioned walks. Each half has density at most two relative to the ordinary walk. Expected total traversal load of an edge is $O(T/D_0)$.

Derandomize the potential $\sum_e(1+1/(2T))^{N_e}$ by fixing intermediates and successive oriented edges. Its exact conditional moments are matrix powers in which that edge's transitions are multiplied by $1+1/(2T)$. This gives explicit paths of length at most $2T$ and congestion $O(T\log(a+\Delta+2))$, with fixed polynomial bit work. Precompute these paths for the $O(\log^2 a)$ cross-block layers of a bitonic network. For load $L_{\rm tok}$, round block length to a power of two. Comparator distances below a block stay local; cross-block patterns are independent of that length. A query uses $O(aL_{\rm tok})$ actual slots and charges their arithmetic and trajectory records.

Finally, hierarchy construction satisfies an actual-size recurrence

$$
T(N,j)\leq v^{c_1}\sum_iT(N_i,j-1)
       +N b_{\rm route}^{c_2}v^{c_3}
                      \operatorname{poly}(\psi_{\rm cut}^{-1}),
 \quad \sum_iN_i\leq c_4N,
 \tag{43}
$$

with absolute constants. Local polynomial-$b_{\rm route}$ work is additive. Only polynomial-$v$ attempt factors multiply over $O(p)$ levels. Original inverse expansion occurs at the first host; nonroot thresholds are fixed constants on bounded-degree matching hosts. Together with the leaf and shuffler computations, this yields (32). This is a sequential-work argument including temporary bit operations and explicit lists.

### 9.5 Scatter, meet, reverse, and exact destinations

The query induction uses the retained hierarchy, its shuffler matrices, (36), and (39). To route inside a part $Y_i$, fold $B_i$ into $X_i$ along its injective covering matching, invoke the smaller child router, and unfold the destination. Every folding fiber has size at most two.

For color $\ell$, let $N_{i\ell}$ be its token count in part $i$. At shuffler step $a$, with $p_{ij}^a$ actual matching portals between parts, send exactly

$$
\left\lfloor\frac{p_{ij}^a N_{i\ell}}{2n'_X}\right\rfloor
 \tag{44}
$$

tokens from $i$ to $j$. Cyclically assign them to genuine portals and use part routers to reach those portals. Per-color accumulated rounding error is at most $\lambda t_{\rm part}$. After the shuffler, color mass in each part is between
$.99N_\ell/t_{\rm part}-\lambda t_{\rm part}$ and
$1.01N_\ell/t_{\rm part}+\lambda t_{\rm part}$.
The total quota at one portal is $O(L_{\rm tok})$, and vertex endpoint load during scattering is $O(L_{\rm tok}(\lambda+1))$.

Color each real token by its destination part. Separately scatter $2L_{\rm tok}$ dummy tokens from every vertex, colored by their origin part. In every current part and color, dummies outnumber reals, since

$$
.97L_{\rm tok}|Y_j|/t_{\rm part}
                       -2\lambda t_{\rm part}>0
 \tag{45}
$$

by (36). Match real tokens injectively to dummies of the same current part and color. Route reals to those dummy locations, then reverse the recorded dummy traces. They reach their correct parts with load at most $2L_{\rm tok}$. One final part-router call reaches the exact destinations.

All recursion goes to strictly smaller children. If $\mathcal V_j$ sums vertex-count times supplied load over depth-$j$ invocations, then

$$
\mathcal V_0=n'L_{\rm tok},\qquad
 \mathcal V_{j+1}\leq c(\lambda+1)^2\mathcal V_j.
 \tag{46}
$$

The same factor counts uses of each stored primitive and repeated trace consumption. Hence dilation is at most $A_{\rm fam}(c(\lambda+1))^{d+1}$, congestion at most $L_{\rm tok}A_{\rm fam}(c(\lambda+1)^2)^{d+1}$, and work at most $n'L_{\rm tok}$ times this non-load factor and logarithmic bookkeeping. Here $d=O(p)$. For quota enumeration, store portal groups in decreasing $p_{ij}^a$; every positive quota consumes a token, plus one stopping test per nonempty part/color. Work per step is $O((M_{\rm tok}+t_{\rm part}^2)\operatorname{polylog}(n'L_{\rm tok}+2))$, paid by (36).

Project cube-port moves to the original host, retaining genuine edge identifiers, then erase closed subwalks using immediate host lifetime IDs. Length and all loads decrease. Equations (39) and (46) give (33) and the full query-volume bound in Proposition 9.1.

## 10. A normalized static sparsifier

**Proposition 10.1 (static provider).** Let a loopless demand multigraph $J_0$ have native edge identifiers, maximum degree $\Delta_0$, and endpoint-preserving ambient walks $\Pi(e)$ of maximum length $L_0\geq1$ and vertex-occurrence congestion $C_0$. For $1\leq p,r\leq U$ with $(p+r)h\leq U$, the construction below returns a normalized table $\Pi'$, a selected subgraph $\widetilde J_0\subseteq J_0$, and routes $R:J_0\to\widetilde J_0$, with

$$
\begin{aligned}
 |E(\widetilde J_0)|&\leq |V(J_0)|\Gamma\operatorname{poly}(U),\\
 L(R)&\leq\Gamma,\qquad L(\Pi'\circ R)\leq\Gamma L_0,\\
 C(\Pi'\circ R)&\leq\Gamma(C_0+\Delta_0),
\end{aligned}
 \tag{47}
$$

where

$$
\log\Gamma=O((p+r)h),\qquad
 \log F=O(U/p+U/r+r^2h+(p+r)h).
 \tag{48}
$$

Full work, plus actual vertex bookkeeping, is

$$
|E(J_0)|F^{O(1)}\Gamma^{O(1)}(L_0+1)\operatorname{poly}(U).
 \tag{49}
$$

The statement is relative to Proposition 9.1 and the inherited degree-band primitive. Its proof follows.

### 10.1 Degree bands and explicit weighted witnesses

First loop-erase every individual ambient image, using immediate ambient lifetime identifiers. This gives simple $\Pi'(e)$, with length at most $L_0$ and congestion at most $C_0$.

The degree-band primitive, with parameter $r$, partitions demand edges into a residual graph with at most $|V(J_0)|$ edges and band graphs $J_i$. Their nontrivial components have conductance at least $\phi=\exp(-O(rh))$, minimum degree at least $\rho_i=\phi2^i$, and $\phi\leq\rho_i\leq\Delta_0$. Its work is $m_0\exp O(U/r+r^2h+rh)\operatorname{poly}(U)$, with $m_0=|E(J_0)|$.

For clarity, this is a reconstructed reduction from the external cut/pruning primitives. Start at $\ell=\max\{0,\lceil\log(2m_0/n_0)\rceil\}$, where $n_0$ counts nonisolated vertices, with invariant $|E(G_i)|\leq2^in_0$. Decompose $G_i$ with a fixed crossing-edge fraction; within each component prune vertices below $\phi2^i$, using a sufficiently small fixed rescaling of the common $\phi$. The pruning volume bound and component discard budget leave at most $2^{i-1}n_0$ edges for the next stage. Retained components have the stated minimum degree and conductance. Summing $\sum_{i\leq\ell}2^in_0=O(m_0)$ pays actual scanning work. There are $O(U)$ bands, and each retained band has at most $2^in_0$ edges. Calls on smaller graphs clip $r$ to the source's legal range; this improves expansion and stays within the master work envelope.

For each component, give vertex $v$ weight $w_v=\deg_{J_i}(v)/\rho_i$. These weights are at least one and balanced: no one exceeds the sum of all others. Round $\lceil w_v\rceil$ to group sizes between that value and twice it, summing to the next power of two and keeping every group at most half the total. This is possible by a linear capacity-filling scan. Contract those groups in a cube and discard within-group cube edges. By (34), the resulting loopless multigraph $W_i$, whose edges have common weight $\rho_i$, satisfies

$$
\deg_{J_i}(v)\leq\rho_i\deg_{W_i}(v)
                 \leq O(U)\deg_{J_i}(v),
 \qquad \Phi(W_i)\geq1/O(U).
 \tag{50}
$$

The degree-band inventory bounds, with the explicit cube factor, give

$$
\begin{aligned}
 \sum_i|E(W_i)|&\leq O(|V(J_0)|\phi^{-1}U^2),\\
 \sum_i|E(W_i)|&\leq O(m_0\phi^{-1}U),\\
 \sum_i\rho_i|E(W_i)|&\leq O(m_0U).
\end{aligned}
 \tag{51}
$$

Every host and witness is generated at its actual inventory.

### 10.2 Both routing directions pay full query volume

Route $\lceil\rho_i\rceil$ unit-token copies of every witness edge through $J_i$. Equation (50) gives endpoint load $O(U/\phi)$ relative to host degree. Aggregate full query volume is $O(m_0U/\phi)$.

In reverse, route one token per $J_i$ edge through $W_i$, with degree-relative load $D_i=\max\{1,\lceil\rho_i\rceil\}$. By (51),

$$
\sum_i|E(W_i)|D_i
 \leq\sum_i(\rho_i+1)|E(W_i)|
 =O(m_0U/\phi).
 \tag{52}
$$

Preprocess each actual $J_i$ and $W_i$ component once. Only query work multiplies load. Proposition 9.1 gives common simple-path quality $Q=\exp O((p+r)h)$ and the work factor in (48). Loop-erasing these token paths in their immediate hosts is separate from normalizing $\Pi$.

### 10.3 Sparse deterministic weighted path selection

**Lemma 10.2.** Suppose group $g$ has $q_g\geq1$ explicit options with nonnegative integer resource multiplicities $a_{gjx}$. The explicit-list size $S_{\rm list}$ counts all option headers and every unit resource occurrence; aggregated multiplicities retain that occurrence budget. Put

$$
\mu_x=\sum_g\sum_{j=1}^{q_g}a_{gjx},\qquad
 B_0=\max_{g,j,x}q_g a_{gjx}.
$$

One can choose $j(g)$ deterministically so that

$$
\sum_g q_g a_{g,j(g),x}
 \leq4\mu_x+4B_0\ln(2|X|+2)
 \tag{53}
$$

for every used resource, in explicit-list size times a polylogarithmic arithmetic factor. The same bound holds with any weights $0<w_g\leq q_g$ in place of $q_g$.

**Proof.** If $B_0=0$, choose arbitrarily. Otherwise, for unprocessed groups define

$$
E_{gx}=\frac1{q_g}\sum_j e^{q_ga_{gjx}/B_0},\qquad
 W_x=e^{(b_x-2\mu_x)/B_0}\prod_{\rm unprocessed\ g}E_{gx}.
$$

All individual exponents lie in $[0,1]$. From $e^u\leq1+(e-1)u$, initially $W_x\leq1$. Averaging over an option leaves the total potential unchanged. To choose a minimizing option sparsely, omit its common term and minimize only

$$
\sum_{x:a_{gjx}>0}\frac{W_x}{E_{gx}}
                                  (e^{q_ga_{gjx}/B_0}-1).
 \tag{54}
$$

All summands are nonnegative. Update only resources appearing in the group. Thus every resource occurrence is processed a logarithmic number of times. Exact expectations keep total potential at most $|X|$, giving the stronger bound $2\mu_x+B_0\ln|X|$.

For a finite implementation, evaluate positive exponential series and positive sums with a fixed multiple of $\log(S_{\rm list}+2)$ mantissa bits and explicit binary exponents. All exponents in the elementary factors lie in $[0,1]$; binary exponents of the accumulated weights need $O(\log(S_{\rm list}+2))$ bits. Choose elementary relative error $(S_{\rm list}+2)^{-c}$ for a sufficiently large fixed $c$. Approximate minimum scores increase the true potential by at most $1+O(1/(S_{\rm list}+1))$ per group. Their total increase is bounded by a constant, absorbed in (53). Computing $e^u-1$ by its positive series avoids subtractive cancellation. ∎

Apply this lemma to the forward candidate paths of each witness edge with $q_g=\lceil\rho_i\rceil$ and weight $\rho_i$. After composition with $\Pi'$, total candidate resource mass is $O(UQC_0/\phi)$. One candidate uses at most $Q$ host edges, each with a simple ambient image, so its multiplicity at any ambient vertex is $O(Q+1)$, independent of $L_0$. Thus

$$
B_0\leq O((\Delta_0+1)(Q+1)).
$$

Weighted ambient congestion of the chosen witness paths is at most

$$
Q\phi^{-O(1)}\operatorname{poly}(U)(C_0+\Delta_0).
 \tag{55}
$$

Only used ambient resources enter the logarithm; their logarithmic inventory is $O(U)$.

### 10.4 Selected input support and composition

Retain all native $J_0$-edge identifiers used by the selected witness paths, together with residual edges. By (51), their number is at most $|V(J_0)|Q\phi^{-O(1)}\operatorname{poly}(U)$.

Each reverse route uses a witness edge with congestion at most $D_iQ$, or relative to weight $\rho_i$, at most $2Q/\phi$. Substitute the chosen forward path for every witness occurrence. This multiplies (55) by at most $2Q/\phi$; final host length is at most $Q^2$. These fixed powers give (47)–(48). Scanning all composed occurrence lists costs the factor $L_0+1$ in (49). Thus ambient input length affects construction work while the congestion bound remains additive in $C_0+\Delta_0$.

### 10.5 Exact correction circulations after normalization

Let $R(e)$ be the current selected-support route for edge $e$, with the same immediate endpoints and raw weighted length at most $\delta_{\rm str}\ell_e$. The selected edge keeps its own native length and gradient. Define its correction $d_e=e-R(e)$. For every circulation $c$,

$$
c=\sum_e c_e(e-R(e))+R(c).
 \tag{56}
$$

Every term is a circulation in its appropriate graph. The sum of their raw denominator charges is at most

$$
(1+2\delta_{\rm str})\sum_e\ell_e|c_e|.
 \tag{57}
$$

Linearity of the numerator and weighted averaging therefore give a correction or a selected-graph circulation with at least the comparator's ratio divided by $1+2\delta_{\rm str}$. This is an existence/comparison statement; the algorithm maintains the corresponding alternatives.

Replacing a route $R_0(e)$ by $R_1(e)$ changes the correction by the exact circulation $R_0(e)-R_1(e)$. Normalization's entire gradient discrepancy is retained in the new $e-R_1(e)$. A selected projected edge contributes its central original identifier to support, even if geometric loop erasure removes that occurrence from its image. Distinct aliases remain distinct until their explicitly typed projection. These conventions preserve (56) and the raw lift.

## 11. Dynamic repair, degree reset, and the complete raw backend

This section specifies the current backend realization and its quantitative proof obligations. Its local structural and recurrence arguments are given explicitly. The large distance-geometry/occurrence implementation is retained as the realization contract in Section 11.6; the main theorem is conditional on that complete contract.

### 11.1 Actual-size stable cores

Every nonbase parent has maximum degree three. A fresh period begins with its actual nonisolated graph of resident size $m'$, and lasts $O(m'/k)$ parent edits. Within the period, newly isolated slots are retained and counted. A later period starts from the maintained nonisolated list, without rescanning unrelated private isolates.

The deterministic center interface uses $O((n'/k)\log^2(n'+2))$ large-component centers, strict balls of size at most $k$, and inverse clusters of size at most $2k$, with $O(n'k\operatorname{polylog}(n'+2))$ work. It follows by greedy hitting sets of nearest-vertex lists, then repeatedly hitting prefixes in the remaining oversized inverse clusters; at least half of the oversized vertices settle each round. Small connected components receive a common local center.

Stable forests have components of $O(k)$ physical vertices. Endpoint promotions and monotone cuts preserve the initial future-path inventory, apart from separately recorded new generating middle edges. Weighted future-path halving gives a polynomial-$U$ family of forests. We use $A=\operatorname{poly}(U)$ to cover their count, buckets, cut logs, and indexing factors. Then:

- native core degree is at most $Ak$;
- initially relevant nonloop roots number at most $Am'/k$;
- a parent edit or requested feedback cut creates at most $A$ native core edits;
- a native split partitions existing input incidences, preserving their edge lifetime IDs.

Whole small-component trees remain in parent storage and physical pool counts. Only selected nonloop endpoints are published recursively. A registered loop demand keeps its current endpoint annotations and an empty route. If a native split makes it nonloop, both endpoints are touched; this does not create a fresh batch of input lifetimes.

### 11.2 Touched-set repair and selected-edge feedback

Choose

$$
\rho=2^{\lceil8U/K_{\mathrm r}\rceil},\qquad
 N_{\rm sched}=\rho^{K_{\mathrm r}}.
 \tag{58}
$$

The latter is a counter, not an allocated universe. Initialize a sparse static base using Proposition 10.1. True new edge lifetimes enter the base by identity routes. Repair layers start empty, with periods $\rho^{K_{\mathrm r}-j}$; a native deletion or split increments the clock. At a period boundary, rebuild the least eligible layer and clear higher layers.

The touched-set schedule follows the local template of [CKLMPG, Section 7.2]; the static base, normalized paths, degree feedback, and chronological credit accounting here specify its present use.

The route-validity induction follows first-touched vertices: a demand had a valid lower route at its last relevant rebuild or its birth. Prefixes before their first touched vertices survive. The repair sparsifies the projected middle demand between those vertices. A selected projected edge inserts only its central native edge into support; its prefix and suffix already lie in retained lower layers.

For a layer of period $a$, a rebuild after $t$ native events has at most $O(\min\{t,\rho a\})$ touched vertices. Thus all its selected membership births through that prefix number at most $A\Gamma\rho t$. Summing the at most $U+1$ layers and absorbing that factor into $A$ gives

$$
I_{\rm repair}(t)\leq \alpha t,\qquad
 \alpha=A\Gamma\rho.
 \tag{59}
$$

The only initial selected credit is $I_0\leq A\Gamma m'/k$.

For degree feedback, partition a selected star only when its degree exceeds $6z$, with $z=\lceil64A\alpha\rceil$. The elementary tree partition [KMPG, Theorem 3.8] cuts its physical preimage into pieces of selected degree at most $3z$, all but one with at least $z$ incidences. Use the potential

$$
\Phi_{\rm deg}=\sum_v(\deg_{\rm selected}(v)-z)_+.
$$

One selected insertion raises it by at most two; deletions and splits do not raise it. A partition into $a\geq3$ pieces decreases it by at least $z(a-1)/2$. Let $f$ count requested feedback cuts and $q_{\rm par}$ parent edits. Since

$$
t\leq A(q_{\rm par}+f),\qquad
 I\leq I_0+Aq_{\rm par}+A\alpha(q_{\rm par}+f),
$$

the inequality $zf/2\leq2I$ absorbs the feedback term and gives, on every finite cascade prefix,

$$
f=O(I_0/z+q_{\rm par}),\qquad
 I=O(I_0+A\alpha q_{\rm par}).
 \tag{60}
$$

These prefix bounds prove cascade termination. Deduplicate central identifiers across owners before computing degrees or passing weights to the physical tree partition.

Publish a child transcript only after feedback settles. Continuously surviving selected edges are compared by their old and final endpoints. A transient unpublished birth followed by death emits no child edge. The resulting selected-degree and fully encoded edit factor $R_{\rm sel}$ has

$$
\log R_{\rm sel}=O(U/K_{\mathrm r}+\log\Gamma+\log U),
 \tag{61}
$$

with initial size and chronological child transcript at most
$O(m'R_{\rm sel}/k+R_{\rm sel}q_{\rm par})$.
The additive initial term is one credit for the period, and may be spent later.

At each repair, preliminary projected degree and ambient congestion are $O(C_j+\Delta_{\rm native})$, where $\Delta_{\rm native}=k\operatorname{poly}(U)$. This uses actual normalized route owners and their first-touched endpoints. Proposition 10.1 gives

$$
L_{j+1}\leq c\Gamma L_j,\qquad
 C_{j+1}\leq c\Gamma(C_j+k\operatorname{poly}(U)).
 \tag{62}
$$

Therefore $L_{K_{\mathrm r}}\leq\Gamma^{O(K_{\mathrm r})}$ and
$C_{K_{\mathrm r}}\leq k\operatorname{poly}(U)\Gamma^{O(K_{\mathrm r})}$.
Full route lists, reverse occurrence indices, moved incidences, native endpoint changes, and correction-score updates are local work bounded by

$$
W=k^{O(1)}\rho^{O(1)}F^{O(1)}
                       \Gamma^{O(K_{\mathrm r})}\operatorname{poly}(U).
 \tag{63}
$$

Only genuine selected-edge provenance and label changes propagate as recursive input edits. Updating a correction route changes its correction record under (56); it does not replace the selected edge's native gradient.

### 11.3 Fixed degree-three fibers and exact cycle comparison

After identifying equal physical roots with their correct frozen gauges, let the settled selected graph have maximum degree at most $C_{\rm port}$, a fixed dyadic envelope for $R_{\rm sel}$. Give each actual selected-vertex lifetime a fixed full binary tree with $C_{\rm port}$ leaves. Assign its current incidences to distinct leaves. Put a real child edge between the assigned leaves for every selected edge. Let

$$
H_{\rm port}=
 2^{\lceil\log(4(\log C_{\rm port}+1))\rceil}.
 \tag{64}
$$

Scale real lengths and gradients together by $H_{\rm port}$; give fiber connectors length one and gradient zero. The child has degree at most three. Reuse the same fiber across temporary selected-degree zero states, and recycle an incidence leaf only after complete retirement of its old lifetime. A deleted parent lifetime leaves a counted inactive fiber until the enclosing period is discarded.

A simple selected-graph cycle uses at most $2\log C_{\rm port}$ connector traversals per real edge. Since real lengths are at least one, its child lift has length at most twice the scaled original length and exactly the scaled gradient. Thus cycle quality loses at most two. Conversely, contracting fibers takes every child circulation to a selected-graph circulation. A fiber-only circulation is zero because a fiber is a tree.

If a child answer has numerator $N_{\rm ch}$ and raw certificate $V_{\rm ch}$, its parent image has

$$
N_{\rm par}=N_{\rm ch}/H_{\rm port},\qquad
 L_{\rm raw,par}\leq V_{\rm ch}/H_{\rm port}.
 \tag{65}
$$

Path coefficients stay unit signed integers. The selected edge's gradient is the exact gradient of its two forest legs and central parent edge. Frozen potential corrections telescope on complete circulations. They are not recomputed merely because a stable forest splits. Immediate-null links have their own typed provenance; an edge that becomes null only after a later projection remains a real edge in its immediate graph.

### 11.4 Flat occurrence pools and chronological recurrences

For each parent root $v$, let $T_v$ be the direct sum of its stable forest trees, identifying only their roots. If the child has $G_{\rm ch}$ occurrences per child vertex, reserve $O(C_{\rm port}(G_{\rm ch}+1))$ copies $T_{v,a}$, with common copy indices across roots. Assign each child occurrence over a port of $v$ a distinct index.

A real child forest edge is lifted by one connecting central parent edge between its two assigned pool copies, at the appropriate forest positions. A connector or immediate-null child edge becomes a typed null root-to-root connection. Contracting every assigned pool tree recovers the child forest, proving that the lift is a forest. Unassigned copies are separate counted trees.

Child occurrence births claim existing pool slots; child forest-edge changes alter one connecting record. They do not copy the whole $O(k)$-vertex parent tree. Parent stable-forest cuts have a different charge: apply their cut logs to current descendant copies, at the counted occurrence factor. Dormant copies remain counted, and retiring copies transfer both signed increments and absolute motion before any old image expires. Pool doubling is based on observed counts; all replacement and retirement work is charged.

Enlarge $R_{\rm sel}$ by fixed polynomial encoding and fiber factors to $P_{\mathrm b}$, so

$$
\log P_{\mathrm b}
 =O(U/K_{\mathrm r}+(p+r)h+h).
 \tag{66}
$$

For $d$ remaining recursive levels, let $G_d$ bound occurrences and answer pieces, $J_d$ be initial work allowance per actual record, and $T_d$ amortized update work. A safe recurrence is

$$
\begin{aligned}
 G_d&\leq P_{\mathrm b}(G_{d-1}+1),\\
 J_d&\leq W+P_{\mathrm b}(G_{d-1}+1)
        +(P_{\mathrm b}/k)(J_{d-1}+T_{d-1}),\\
 T_d&\leq O(kW+kP_{\mathrm b}(G_{d-1}+1))
                 +O(P_{\mathrm b})(J_{d-1}+T_{d-1}).
\end{aligned}
 \tag{67}
$$

The $T_{d-1}$ term in the initialization allowance pays child updates caused by late spending of initial credit. Setting $\mathcal H_d=J_d+T_d/k$ closes the recurrence:

$$
\mathcal H_d\leq
 O(W+P_{\mathrm b}(G_{d-1}+1))+O(P_{\mathrm b})\mathcal H_{d-1}.
 \tag{68}
$$

All work and occurrence factors are consequently bounded by
$k^{O(1)}W(cP_{\mathrm b})^{O(d)}$.
Small actual instances use an explicit polynomial-time minimum-ratio cycle base solver with charged multiword arithmetic. The polynomial-$k$ base factor occurs once in this envelope.

The local distance comparison and (56) give one-level inverse quality $\Gamma^{O(K_{\mathrm r})}$, up to fixed polynomial factors in $U$. Across $d$ levels, complete raw inverse quality is therefore bounded by

$$
k^{O(1)}\exp O(dK_{\mathrm r}\log\Gamma+d\log U).
 \tag{69}
$$

Local same-tree cycles and correction circulations are extracted with their actual expansion work paid in $W$. The raw certificate must dominate their literal traversals. Equation (69) includes every recursive level.

### 11.5 Finite-bit forests without recursive precision growth

The finite-bit tree interface required here is the following: on a connected $n'$-vertex, $m'$-edge graph with original edge lengths in $[1,2^b)$, return an original-edge spanning tree $T$ with

$$
\sum_{e=uv}\frac{d_T(u,v)}{\ell_e}\leq
       m'\operatorname{poly}(b+\log(n'+m'+4))
 \tag{70}
$$

in $(n'+m')\operatorname{poly}(b+\log(n'+m'+4))$ bit work. Its geometric realization uses the weighted petal construction of [AN]: exact weighted portals on a common dyadic grid, a static directed metric during each petal, exact midpoint tests, and separate working and inherited target paths. Temporary portal coordinates are removed before exporting the tree. We treat this finite-bit realization, including its geometric induction, as part of the backend contract; only its integration into the numerical hierarchy is proved here.

For weighted forest calls, use occurrence counts $N_e$ and integer importance $w_e=N_e\ell_e$. If a component has $a$ edges and total $W_0>0$, smooth by $v_e=aw_e+W_0$ and use replica counts $\lceil av_e/\sum_fv_f\rceil$, totaling at most $2a$. If $W_0=0$, use uniform positive weights. Reciprocal ordering uses the dyadic proxy $2^{-\lceil\log\ell_e\rceil}$. All these operations use integer arithmetic or one common power-of-two grid.

Crucially, one exported fixed stretch label has the exact realization

$$
\ell_e\widetilde{\mathrm{str}}(e)
       =2\sum_{j=0}^{O(\log^2(n'+2))}(\ell_e+P_j(e)),
 \tag{71}
$$

where each $P_j(e)$ is one simple original-tree path or two root legs. If $L_{\max}$ bounds parent lengths over the instance lifetime, the label is at most
$O((n'+1)\log^2(n'+2)L_{\max})$.
Its magnitude does not depend on the average stretch in (70), or on how many weighted forest calls are made.

Frozen corrected gradients likewise have magnitude at most $(2n'+1)G_{\max}$, using lifetime rather than current magnitude bounds. With actual-record guard $n'+m'\leq2^{c_{\rm size}U}$, each distance level therefore adds only $O(U)$ bits, plus the port scaling. Declare

$$
b_*=c_b U(d_*+1),
 \tag{72}
$$

with fixed $c_b$ large enough for the root-price and size constants. This label bound is proved before substituting the polynomial-bit tree cost. Consequently the input precision in (70) is $\operatorname{poly}(U)$, and its cost contributes fixed polynomial factors only.

The complete initial future-path occurrence inventory has size and total edge count $m'k^{O(1)}\operatorname{poly}(U)$, and maximum path length at most $k^{O(1)}\operatorname{poly}(U)2^{b_*}$. Weighted path halving thus uses
$O(\log(m'+2)+\log(k+2)+b_*+\log(U+2))=\operatorname{poly}(U)$
forests. This count includes the length aspect. Temporary spectral, moment, or portal arithmetic is charged locally and is not exported as a stored numerical label.

### 11.6 Explicit raw-backend realization contract

The following is the precise internal realization hypothesis used in Theorem 1.1. It states more than an ordinary distance oracle or a net-norm cycle oracle.

**Contract R.** There is a fixed finite deterministic implementation of the stable-core, normalized repair, degree-reset, and flat-lift assembly above such that:

1. **Geometric comparison.** The local distance-to-cycle decomposition is valid on its actual degree-three multigraphs. The one-level loss is bounded by a fixed power of $\Gamma^{K_{\mathrm r}}U$; complete recursion gives (69), with numerator identities and literal traversal certificates as in (56) and (65).
2. **Construction and recourse.** For every chronological prefix and the first attempted batch, actual local work, selected support/degree, published child edits, and initial credit satisfy (61)–(67). Old loop lifetimes, native splits, and disconnected small components obey Section 11.1.
3. **Occurrences and retirement.** The flat forests are actual forests with the pool inventory in Section 11.4. The implementation reports every exposed representation change, preserves the old immediate maps through retirement, counts dormant and isolated occurrences, and transfers both signed and absolute counters. Queries expose only settled transactions.
4. **Finite arithmetic.** The weighted original-edge tree realization satisfies (70); its exported labels satisfy (71)–(72). All temporary and stored arithmetic, explicit paths, dictionaries, and private resident records are charged. Root prices fit the fixed master envelope of Section 8.
5. **Uniform executable bounds.** Fixed, enumerable cap constants suffice for all these claims uniformly in $U,p,r,K_{\mathrm r},k$. Actual-size base cases and finite guards are implemented, and initialization is proportional to actual inventory.

The carrier, rounding, entropy, weighted selection, degree-feedback, recurrence solution, and parameter balance in this manuscript do not require assuming their own running-time conclusions. Contract R isolates the full backend implementation and geometric realization that the supplied checkpoint asserts. It is not identified with any unmodified published complete dynamic theorem. Under this contract, (67) and (69) give the cap in the next section, and hence the interface (19)–(20).

## 12. Parameter balance and one finite program

### 12.1 Rounded parameters and all charged terms

For sufficiently large $U$, compute

$$
\begin{gathered}
 h=\lceil\log(U+4)\rceil,\qquad
 t=\left\lfloor(U/h)^{1/5}\right\rfloor,\qquad
 p=r=t,\\
 K_{\mathrm r}=t^2,\qquad x=\lceil U/t\rceil,\qquad
 k=2^x,\qquad d_*=\lceil8U/x\rceil+10.
\end{gathered}
 \tag{73}
$$

Integer-root comparisons suffice. Check $t\geq2$, $(p+r)h\leq U$, and $K_{\mathrm r}\leq U$. Finitely many exceptional sizes are handled by the classical worker below. We have

$$
t^5h\leq U,\qquad
 x=\Theta(U^{4/5}h^{1/5}),\qquad d_*=O(t).
 \tag{74}
$$

Choose dyadic cap constants before the run. One convenient acyclic family, indexed by an integer $c_C$, has
$c_\phi=\max\{1,\lfloor c_C^{1/4}\rfloor\}$,
$c_\Lambda=\max\{1,\lfloor c_C^{1/2}\rfloor\}$, and
$c_\Gamma=\max\{1,\lfloor c_C^{3/4}\rfloor\}$.
Use expansion cap $2^{-c_\phi rh}$, routing cap $2^{c_\Lambda(p+r)h}$, static cap $2^{c_\Gamma(p+r)h}$, and port/record caps with logarithm
$O(c_C(\lceil U/K_{\mathrm r}\rceil+(p+r)h+h))$.
Their constants dominate one another in the displayed order. After fixing a sufficiently large $c_C$, a separate fixed $c_E$ bounds all work and inverse quality.

By (48),

$$
\log\Gamma=O(th),\qquad
 \log F=O(U/t+t^2h+th).
 \tag{75}
$$

The complete work/quality envelope is bounded by a constant multiple of

$$
x+\log F+K_{\mathrm r}\log\Gamma+
       \frac Ux\left(\frac{U}{K_{\mathrm r}}
                  +\log\Gamma+K_{\mathrm r}\log\Gamma+h\right).
 \tag{76}
$$

The following table pays each term separately.

| Charge | Bound under (73) |
|---|---|
| Recursive reduction and direct base | $x=O(U/t)$ |
| Static construction | $\log F=O(U/t+t^2h)$ |
| Local repair work | $K_{\mathrm r}\log\Gamma=O(t^3h)$ |
| Propagated records, work, and initial credit | $d_*\log P_{\mathrm b}=O(U/t+t^2h+th)$ |
| Full recursive inverse quality | $d_*K_{\mathrm r}\log\Gamma=O(t^4h)$ |
| Stored-label arithmetic | $b_*=O(Ut)$, charged polynomially |

Since $t^5h\leq U$, all logarithmic overhead charges are $O(U/t)$. Moreover
$\log P_{\mathrm b}/x=O(1/t+t^2h/U)=o(1)$, so the child size factor $P_{\mathrm b}/k\leq k^{-1/2}$ eventually; $d_*$ has fixed slack. On a nonbase graph $\log m'\geq x-O(1)$, and
$b_*/x^2=O(t^3/U)=o(1)$, satisfying the stored-label aspect guard. Smaller instances use their direct charged base solver.

Thus, under Contract R, a fixed sufficiently large pair $(c_C,c_E)$ gives the computable complete cap

$$
E_*=2^{c_E x},\qquad
 \log E_*=O(U^{4/5}(\log(U+4))^{1/5}).
 \tag{77}
$$

This covers initialization per actual record, amortized updates, queries, complete logs, occurrences, answer pieces, and inverse raw quality. A root answer with at most $E_*$ pieces in forests of at most $ME_*$ records has raw numerator and denominator bounded in magnitude by $ME_*^2$ times the corresponding root label bound. Their bit sizes are $O(U)$ for a favorable fixed tuple. Maintained path aggregates supply each returned forest path's length and signed gradient sum without expanding it to compute the certificate. Computing the actual raw denominator can only improve its ratio relative to the inherited upper certificate.

### 12.2 Uniform constants and independent acceptance

To obtain one program without numerical advice about sufficiently large constants, enumerate positive integer pairs $(c_C,c_E)$ in a fixed computable order. A scheduler reserves a fixed positive instruction share for a classical deterministic exact worker and assigns each fixed tuple a positive constant share, for example by a binary ruler schedule. Tuple generation and instruction simulation are charged. No worker preallocates its master bound.

Each worker checks degree, size, history, prefix-recourse, depth, label, and work caps before using a result. A cap violation suspends the worker, and an overlong path is never truncated. Before any candidate is accepted, validate its edge list and run one independent deterministic augmenting-path search [Gabow] on the shared compact graph. No augmenting path certifies maximum cardinality. Verification and candidate materialization are charged inside that worker's instruction share.

This arrangement always terminates and returns a correct answer: the classical worker receives positive share and supplies one, while no accepted candidate fails the augmenting-path criterion. Under the external interfaces and Contract R, some fixed tuple is favorable for every sufficiently large input. Its scheduling penalty is constant, its finite-word simulation overhead is polynomial in $s$, and its verified completion is bounded by (31). Any finite collection of exceptional input sizes is absorbed into a uniform constant.

The classical worker also bounds total pretermination instructions and allocated records by a fixed polynomial in the compact instance size, up to scheduler overhead. Addresses and live scheduling indices therefore need only $O(s)$ bits. This justifies the charged word simulation used by the persistent memory and the portfolio.

### 12.3 Completion of Theorem 1.1

Substitute $U=2s$ and (77) into (31). Since $S=\Theta(e+1)$ for the cleaned subcubic construction, all fixed polynomial factors in $s$ fit the exponential in (1). Cleanup and optional kernel construction cost $O(n+m)$; candidate checks use only that shared compact exact-preserving graph. Translate only the accepted matching's edge identifiers once. Lemmas 3.1 and 3.2 give exactness on the original input and the kernelized form of the second term. This proves the stated conditional composition theorem. ∎

## References

**[OAI]** OpenAI. *Almost-Linear-Time Maximum-Cardinality Matching in General Graphs*. Manuscript dated 24 September 2026, Sections 3–5. [Official manuscript directory](https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026).

**[AHLT]** Stephen Alstrup, Jacob Holm, Kristian de Lichtenberg, and Mikkel Thorup. *Maintaining Information in Fully-Dynamic Trees with Top Trees*. Version 2, 2003; ACM Transactions on Algorithms, 2005. [arXiv:cs/0310065v2](https://arxiv.org/abs/cs/0310065v2).

**[CHHIP]** Shiri Chechik, Thomas Dueholm Hansen, Giuseppe F. Italiano, Veronika Loitzenbauer, and Nikos Parotsidis. *Faster Algorithms for Computing Maximal 2-Connected Subgraphs in Sparse Directed Graphs*. 2017, Section 3.1, Lemma 3.5. [arXiv:1705.10709v1](https://arxiv.org/abs/1705.10709v1).

**[KMPG]** Rasmus Kyng, Simon Meierhans, and Maximilian Probst Gutenberg. *A Dynamic Shortest Paths Toolbox: Low-Congestion Vertex Sparsifiers and their Applications*. 2023, Theorems 3.2 and 3.8, Lemma 3.5, and Appendix A.1. [arXiv:2311.06402v1](https://arxiv.org/abs/2311.06402v1).

**[CKL]** Li Chen, Rasmus Kyng, Yang P. Liu, Richard Peng, Maximilian Probst Gutenberg, and Sushant Sachdeva. *Maximum Flow and Minimum-Cost Flow in Almost-Linear Time*. 2022, deterministic single-forest construction and fixed labels in Lemmas 6.5–6.6 and Appendix B.3. [arXiv:2203.00671v1](https://arxiv.org/abs/2203.00671v1).

**[AN]** Ittai Abraham and Ofer Neiman. *Using Petal-Decompositions to Build a Low Stretch Spanning Tree*. SIAM Journal on Computing 48(2), 2019. [DOI:10.1137/17M1115575](https://doi.org/10.1137/17M1115575).

**[CGLNPS]** Julia Chuzhoy, Yu Gao, Jason Li, Danupon Nanongkai, Richard Peng, and Thatchaphol Saranurak. *A Deterministic Algorithm for Balanced Cut with Applications to Dynamic Connectivity, Flows, and Beyond*. Version 2, 2020, Theorems 2.6 and 5.1. [arXiv:1910.08025v2](https://arxiv.org/abs/1910.08025v2).

**[CS21]** Julia Chuzhoy and Thatchaphol Saranurak. *Deterministic Algorithms for Decremental Shortest Paths via Layered Core Decomposition*. 2020 preprint, deterministic expander-pruning interface, Theorem 3.7. [arXiv:2009.08479v1](https://arxiv.org/abs/2009.08479v1).

**[CS]** Yi-Jun Chang and Thatchaphol Saranurak. *Deterministic Distributed Expander Decomposition and Routing with Applications in Distributed Derandomization*. 2020, Sections 4.1–4.3 and hierarchy geometry. [arXiv:2007.14898v1](https://arxiv.org/abs/2007.14898v1).

**[CHS]** Yi-Jun Chang, Shang-En Huang, and Hsin-Hao Su. *Deterministic Expander Routing: Faster and More Versatile*. 2024, hierarchy and shuffler architecture. [arXiv:2405.03908v1](https://arxiv.org/abs/2405.03908v1).

**[CKLMPG]** Li Chen, Rasmus Kyng, Yang P. Liu, Simon Meierhans, and Maximilian Probst Gutenberg. *Almost-Linear Time Algorithms for Incremental Graphs: Cycle Detection, SCCs, $s$-$t$ Shortest Path, and Minimum-Cost Flow*. 2023, Section 7.2, touched-set scheduling template. [arXiv:2311.18295v1](https://arxiv.org/abs/2311.18295v1).

**[KMPS]** Rasmus Kyng, Simon Meierhans, Maximilian Probst Gutenberg, and Aurelio Sulser. *A Simpler and Faster Min-Cost Flow Solver via Min-Ratio Cycles from Distance Oracles*. 2026, local distance-to-cycle comparison. [arXiv:2609.23852v1](https://arxiv.org/abs/2609.23852v1).

**[Gabow]** Harold N. Gabow. *The Weighted Matching Approach to Maximum Cardinality Matching*. 2017, first-search correctness and implementation, Sections 3 and 5. [arXiv:1703.03998v1](https://arxiv.org/abs/1703.03998v1).


---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.

The proofs use their named external interfaces. Finite checks are separate from proof-assistant verification.
