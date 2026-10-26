# Exact correlated-failure summaries for whole linear blocks, hyperedges, and commuting stabilizer checks

**Abstract.** We construct exact polynomial-label decoders for whole represented subspaces. One ordinary quotient sparsifier of the lifted blocks preserves all original subspace-complement queries after every allowed correlated deletion, using one fixed coefficient per original item. The same theorem gives cut and partition summaries for atomic hyperedge and hedge deletions, and all-state spectral summaries for globally commuting prime-dimensional stabilizer blocks. Explicit cut constructions establish the joint failure and inverse-accuracy support lower bounds in the stated size regimes.

## 1. A whole-block theorem

Let item $e$ have a positive rational weight $w_e$ and an explicitly represented subspace
$$
B_e=\operatorname{span}\{a_{e,1},\ldots,a_{e,t_e}\}
       \subseteq\mathbb K^N.
$$
Let $A$ be the concatenation of all these columns, of rank $r$. Each original row $i$ has a label set $R_i$, and every column belonging to item $e$ has the same label set $S_e$. Suppose every nonzero incidence satisfies
$$
A_{i,(e,j)}\ne0
 \quad\Longrightarrow\quad
 R_i\subseteq S_e,\qquad |S_e\setminus R_i|\le k.
 \tag{B1}
$$
A failure set $F$, with $|F|\le h$, deletes the whole item whenever $S_e\cap F\ne\varnothing$. For an arbitrary linear subspace $W\subseteq\mathbb K^N$, define
$$
\Phi_F(W)=
 \sum_{e:S_e\cap F=\varnothing}
        w_e\,\mathbf1[B_e\not\subseteq W].
 \tag{B2}
$$

**Theorem B1.** There is one nonnegative original-item reweighting, simultaneously preserving (B2) within $1\pm\epsilon$ for every allowed $F$ and every $W$, with support
$$
O\!\left(\min\left\{m,\,
    \frac{D\log(2D/\epsilon)}{\epsilon^2}\right\}\right),
 \qquad
 D=r\binom{h+k}{k}.
 \tag{B3}
$$
Here $m$ counts items, not columns. In particular there is no multiplicative dependence on the number of columns or the individual rank of a retained block. With explicit rational or finite-field matrices and rational weights, the construction is randomized polynomial time in the compact matrix input and $\epsilon^{-1}$, with constant success probability for one event covering every query. The uniform polynomial statement uses the cap described below.

### Exact decoder and the quotient backend

Select $r$ independent original rows with row-selection matrix $P$, and write $A=C(PA)$. Keep the actual labels of these selected rows. Choose pairwise distinct field points $\alpha_0,\ldots,\alpha_L$, where $0$ is a dummy label which never fails, and let
$$
\ell_c(z)=\sum_{t=0}^h\alpha_c^t z_t,
 \qquad
 p_T(z)=\prod_{c\in T}\ell_c(z)\,
                \ell_0(z)^{k-|T|}.
$$
These homogeneous degree-$k$ polynomials have coefficient dimension $\binom{h+k}{k}$. Ordinary monomial coefficients use no factorial denominators and are valid in every characteristic.

For each column $a_{e,j}$, lift its selected row $i$ to the coefficient block
$$
(PA)_{i,(e,j)}p_{S_e\setminus R_i}.
$$
Denote the lifted column by $z_{e,j}$, and let $\widehat B_e$ be the span of all lifted columns of item $e$. Given a failure set, the normalized polynomial
$$
q_F(t)=\prod_{f\in F}\frac{t-\alpha_f}{\alpha_0-\alpha_f}
$$
has degree at most $h$, equals one at $\alpha_0$, and vanishes at exactly the failed label points. Evaluating the row polynomial block at the coefficients of $q_F$, and multiplying that row by $\prod_{c\in R_i}q_F(\alpha_c)$, defines a linear map $T_F$ such that
$$
CT_Fz_{e,j}=\gamma_F(S_e)a_{e,j},
 \qquad
 \gamma_F(S_e)=\prod_{c\in S_e}q_F(\alpha_c).
 \tag{B4}
$$
The scalar is common to every column of the item. It is zero exactly when that item fails.

For $U=(CT_F)^{-1}(W)$, (B4) gives
$$
\widehat B_e\not\subseteq U
 \quad\Longleftrightarrow\quad
 S_e\cap F=\varnothing\ \text{and}\ B_e\not\subseteq W.
 \tag{B5}
$$
Now use the represented integer polymatroid
$$
f(T)=\dim\sum_{e\in T}\widehat B_e,
 \qquad f(E)\le D.
$$
For every subspace $U$, the item set $Z_U=\{e:\widehat B_e\subseteq U\}$ is closed: every block in the span of those blocks is also contained in $U$. Thus its complement is a quotient. Quanrud's theorem and adaptive resparsification preserve the total weight of every such complement, with the support (B3). Equation (B5) proves the theorem. The selected items retain their full original block representation and one coefficient each.

Every quotient of every surviving original represented polymatroid is included: take $W$ to be the span of the blocks in its closed set. Hence the result is not limited to hyperplane queries or scalar codewords.

### Arithmetic and the uniform cap

The decoder maps are proof devices; no failure set is enumerated. Remove unused labels, cap $h,k$ at their effective label-universe bounds, and handle $h=0$ directly by the ordinary backend. If $D\ge m$, retain the input before materializing the lifted blocks; compute the binomial coefficient with this cap. In the remaining branch the feature dimension is at most $m$, and all block columns together are explicit input, so materialization and rank evaluations are polynomial. Zero-dimensional blocks may be discarded; if the total rank is zero, return the empty summary.

For rational matrices, integer label points give polynomial-bit coefficients. For finite fields, extending to a field with at least $L+1$ elements preserves every original linear dependence and subspace-membership query. When an extension is required, enumeration of irreducible polynomials over the original field is polynomial in the explicit label count, as detailed in the companion exact-label-cut note. Rational output weights use the integer-rank implementation and bit ledger of the quotient-resparsification note. No real-valued logarithmic-rank oracle is needed.

## 2. Whole hyperedges under incident-vertex color deletion

Consider a weighted hypergraph on $n$ vertices, with maximum hyperedge size $t\ge2$. A vertex has at most $a$ labels and each hyperedge has at most $b$ additional labels. Failure deletes a vertex carrying a failed label and **removes every entire hyperedge incident to that vertex**; a failed additional hyperedge label also deletes the whole hyperedge. This is the atomic deletion convention. It does not mean that a hyperedge is shortened to its surviving vertices.

Represent hyperedge $e$ by the subspace spanned by $e_u-e_v$ for $u,v\in e$, using a star of $|e|-1$ columns if desired. Put
$$
S_e=\bigcup_{u\in e}R_u\ \cup\ T_e.
$$
On a nonzero incidence at vertex $u$,
$$
|S_e\setminus R_u|\le a(t-1)+b=:k.
$$
The concatenated incidence rank is $r=n-c$, where $c$ is the number of components of the positive-weight hypergraph, including isolated vertices. For a Boolean cut vector $x$, the block is not contained in $\ker x^T$ exactly when the hyperedge crosses that cut. Theorem B1 therefore gives
$$
O\!\left(\min\left\{m,\,
 \frac{(n-c)\binom{h+a(t-1)+b}{a(t-1)+b}}{\epsilon^2}
 \log\frac{2(n-c)\binom{h+a(t-1)+b}{a(t-1)+b}}{\epsilon}
 \right\}\right)
 \tag{B6}
$$
whole hyperedges, with one set of weights valid for every cut and every allowed label failure.

In particular, with one color per vertex and no additional edge labels, the failure factor is $\binom{h+t-1}{t-1}$. The row-incidence structure saves one degree compared with treating all $t$ possible vertex colors as unrelated item labels.

The same summary preserves every partition's total weight of hyperedges crossing at least two parts. For a partition, take $W$ to be the span of all within-part pair differences. A hyperedge block is contained in $W$ precisely when it lies in one part. This is the partition objective counting a crossing hyperedge once, not the objective counting its number of intersected parts minus one.

### Joint failure and accuracy lower bound

The failure factor and $\epsilon^{-2}$ in (B6) are jointly necessary, up to its logarithm, in a sufficiently large-$n$ regime. We give the argument for arbitrary $a,b\ge0$ with $k=a(t-1)+b\ge1$.

Put $s=\lceil\epsilon^{-2}\rceil$, where $0<\epsilon\le1/2$, and $q=\binom{h+k}{k}$. Index $q$ blocks by the $k$-subsets $S$ of an $(h+k)$-element label universe. Partition each $S$ into $t-1$ groups of size $a$ and one group of size $b$. In its block create $t-2$ core vertices, carrying the first $t-2$ vertex-label groups, and $s$ left vertices, each carrying the last vertex-label group. There is one shared unlabelled right part of $B\ge q(s+t-2)$ vertices. For each left-right pair, add the hyperedge consisting of the block's core, that left vertex, and that right vertex; attach the block's $b$ additional labels to it. Every hyperedge has size exactly $t$, and the input is simple and unweighted.

Failing the $h$ labels outside $S$ leaves precisely the hyperedges of block $S$. All other blocks have at least one failed vertex or hyperedge label. There are
$$
n=B+q(s+t-2)\le2B
$$
vertices.

For $t=2$, the surviving block is $K_{s,B}$, and the cut lower bound in the companion note applies directly. For $t\ge3$, place all its core vertices on side zero of a cut. A hyperedge then crosses exactly when at least one of its left and right vertices has Boolean value one. Let $W$ be the $s\times B$ matrix of output weights in this block, let $J$ be all ones, and put $E=W-J$. The cut with one right vertex on side one gives every column sum of $W$ in $(1\pm\epsilon)s$. A cut with zero-valued left subset $I$ and zero-valued right subset $J'$ has value
$$
w(\text{all block edges})-w(I\times J').
$$
Comparing it and the full block cut gives
$$
\left|\sum_{i\in I,j\in J'}E_{ij}\right|
       \le2\epsilon sB
 \quad\text{for every rectangle }I\times J'.
$$
For any signs $\sigma,\tau$, split their signed product into four rectangles. It follows that
$$
|\sigma^T E\tau|\le8\epsilon sB.
$$
Choose $\tau$ to agree with $E^T\sigma$, average independent uniform $\sigma_i\in\{-1,1\}$, and use the Khintchine inequality $\mathbb E|v\cdot\sigma|\ge\|v\|_2/\sqrt2$. Then
$$
\sum_j\|E_{\cdot j}\|_2\le8\sqrt2\,\epsilon sB.
$$
If column $j$ has $u_j$ nonzero output entries, its degree bound and the triangle inequality give
$$
\|E_{\cdot j}\|_2\ge
     (1-\epsilon)s/\sqrt{u_j}-\sqrt{s}.
$$
Every $u_j>0$. Convexity of $x^{-1/2}$, with $u=\sum_j u_j$, yields
$$
u\ge
 \frac{(1-\epsilon)^2sB}
       {(1+8\sqrt2\,\epsilon\sqrt{s})^2}
 =\Omega(B/\epsilon^2).
 \tag{B7}
$$
The $t=2$ cut bound is stronger and also implies (B7). Each isolated block must meet this lower bound on its own disjoint hyperedge set. Therefore every simultaneous summary needs
$$
\Omega\!\left(
 \frac{n}{\epsilon^2}\binom{h+a(t-1)+b}{a(t-1)+b}
 \right)
 \tag{B8}
$$
original hyperedges, even allowing arbitrary nonnegative output weights. The explicit regime is $n=B+q(s+t-2)$ with $B\ge q(s+t-2)$; additional isolated vertices are not used to inflate the lower bound. For one color per vertex, set $a=1,b=0$.

## 3. Hedges with correlated item-label failures

A hedge is a whole collection of hyperedges, and its cut weight is paid once if any constituent hyperedge crosses. Represent it by the span of star differences from all its constituent hyperedges. Give the whole hedge a failure-label list of size at most $d$; row labels are empty. Theorem B1, with $k=d$ and $r\le n-c$, preserves every cut and every partition-crossing objective after all $h$-label failures using
$$
O\!\left(\min\left\{m,\,
 \frac{(n-c)\binom{h+d}{d}}{\epsilon^2}
 \log\frac{2(n-c)\binom{h+d}{d}}{\epsilon}
 \right\}\right)
 \tag{B9}
$$
whole hedges. The number of constituent hyperedges, their individual ranks, and the number of connected components inside one hedge do not multiply this support bound. They remain part of the explicit input and evaluation cost.

The ordinary no-failure hedge theorem is already public. The asserted extension is the same coefficients for all later correlated whole-hedge deletions, rather than a new ordinary sparsification result.

## 4. Commuting stabilizer blocks with correlated clause deletions

Let the physical space be $n$ prime-dimensional qudits, of local dimension $p$. Each item is a whole stabilizer acceptance projector $E_e$, specified by any number of commuting Weyl eigenvalue checks, with penalty $w_e(I-E_e)$. In this section, **all supplied Weyl generators commute globally across items**, not merely within each item. Give each item at most $d$ external failure labels.

Phase-aware linear algebra expresses all generators in one independent commuting projective basis of dimension at most $n$. On its eigenvalue pattern $x$, the penalty for item $e$ is
$$
w_e\,\mathbf1[M_e(x,1)^T\ne0]
$$
for an explicit affine constraint matrix $M_e$ over $\mathbb F_p$. The extra coordinate homogenizes the affine phases. Inconsistent acceptance equations give a constant-one penalty and are represented by the same affine system; an empty or universally satisfied system contributes zero and may be removed.

Regard the row space of $M_e$ as the item's block in dimension at most $n+1$. Use empty row labels and the external item labels, so $k=d$. Theorem B1 gives one common coefficient per original stabilizer block and support
$$
O\!\left(\min\left\{m,\,
 \frac{D\log(2D/\epsilon)}{\epsilon^2}\right\}\right),
 \qquad D=(n+1)\binom{h+d}{d}.
 \tag{B10}
$$
All Hamiltonians obtained by deleting allowed item-label sets remain diagonal in the same basis. Preserving every surviving affine block predicate therefore yields
$$
(1-\epsilon)H_F\preceq\widehat H_F
                    \preceq(1+\epsilon)H_F
 \quad\text{simultaneously for all }|F|\le h.
 \tag{B11}
$$
Thus every quantum-state energy is preserved, including that of entangled states, and every surviving Hamiltonian kernel is preserved exactly. There is no support factor for the number of checks within a block. Finite-field extension used for label points changes only the classical compiler; it does not change the physical local dimension.

The failure and accuracy dependence in (B10) is jointly necessary up to its logarithm for original-item summaries. Let $q=\binom{h+d}{d}$, and form $q$ differently labelled copies of the same commuting two-local check family
$$
I-\Pi_{Z_uZ_v^{-1},1},\qquad uv\in E(K_{s,B}),
 \quad s=\lceil\epsilon^{-2}\rceil,\quad B=n-s\ge s.
$$
All copies use the same $n$ physical qudits. Index copies by the $d$-subsets $S$ of an $(h+d)$-label universe, giving every item of copy $S$ precisely those labels. Failure of the complement of $S$ isolates that copy. Restrict computational basis symbols to $\{0,1\}\subseteq\mathbb F_p$; every check is exactly the Boolean cut indicator. The complete-bipartite cut lower bound then requires $\Omega(n/\epsilon^2)$ original items in each copy, hence
$$
\Omega\!\left(n\binom{h+d}{d}/\epsilon^2\right)
$$
after summing all copies. This holds for $0<\epsilon\le1/2$, $n\ge2\lceil\epsilon^{-2}\rceil$. Identical operators with different failure lists are distinct input items and cannot be merged across their deletion patterns. The same construction, represented by scalar incidence-vector blocks, gives the corresponding $\Omega(r\binom{h+d}{d}/\epsilon^2)$ lower bound for Theorem B1 when row labels are empty and $k=d$. This uses the inherited cut lower bound and the explicit failure-isolation construction; no computational lower bound is asserted.

The construction is polynomial in the compact generator descriptions, the rational input bit length, $\log p$, and $\epsilon^{-1}$, with the feature cap above. It does not materialize $p^n$-dimensional matrices. Failure here deletes an entire specified clause/block; it does not physically erase a qudit or trace out a subsystem.

This statement cannot be obtained by simply applying the earlier noncommuting peeling procedure once and then deleting arbitrary clauses: a deletion may remove one side of a balanced incompatible pair and destroy its uniform spectral lower bound. The global commutation condition in this section is essential to the proof supplied here. No common all-failure summary of the same size is asserted for arbitrary noncommuting stabilizer blocks.

## 5. Baselines and scope

- **Quanrud, *Quotient sparsification for submodular functions*, SODA 2024.** Theorem 1.1 supplies the ordinary rank-dependent quotient sparsifier. The companion adaptive-resparsification note accounts for removing the original item-count logarithm, accumulated error, conditional success probability, and the integer-rank bit model. <https://kentq.s3.amazonaws.com/submodular-sparsification.pdf>.
- **Chandrasekaran, Chekuri, Wang, and Zhu, *Hedgegraph Polymatroids*, 2025.** Theorem 7 gives ordinary weighted hedgegraph partition sparsifiers with $O(n\log n/\epsilon^2)$ hedges. The cut convention in its introduction charges a hedge once if any constituent hyperedge crosses. These ordinary whole-object guarantees are antecedents, not newly claimed here. <https://arxiv.org/html/2510.25043v1>.
- **Basu, Brakensiek, Chen, Putterman, Reis, and Zhang, *Optimal Sparsifiers for Minkowski Sums and Sums of Seminorms*, September 2026.** The optimal ordinary seminorm theorem implies existential $O(n/\epsilon^2)$ ordinary hypergraph-cut support. It does not by itself supply the simultaneous labeled-incidence transfer above. <https://arxiv.org/pdf/2609.20238>.
- **Oko, Sakaue, and Tanigawa, *Nearly Tight Spectral Sparsification of Directed Hypergraphs by a Simple Iterative Sampling Algorithm*, Section 7.8.2.** Their hypergraph-failure guarantee distinguishes a fixed deletion from one event uniform over all deletions; the section also notes a uniform spectral construction with a larger bound. Its faults are individual hyperedges. The present hypergraph corollary concerns correlated vertex/edge labels, atomic incident-hyperedge removal, and cut/partition preservation; it is not a spectral improvement over that theorem. <https://arxiv.org/pdf/2204.02537>.

The contribution is the exact block decoder, its shared-weight failure guarantee, and the explicit colored hyperedge lower construction. The stronger quantum all-state conclusion in Section 4 uses global commutation and does not enlarge the scope of the general cut theorem.
