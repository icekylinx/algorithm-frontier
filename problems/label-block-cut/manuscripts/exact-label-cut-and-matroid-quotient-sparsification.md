# Exact label annihilation for fault-tolerant cuts and matroid quotients

## Main result and scope

For a weighted undirected graph, put at most a labels on each vertex and at most b additional labels on each edge. Failure of a label deletes every vertex or edge carrying it, together with edges incident to deleted vertices. There is one nonnegative reweighting of original edges, valid simultaneously after every set of at most h label failures, that preserves **every cut** within 1±epsilon and has support

```math
O\!\left(\min\left\{m,\,
 D\epsilon^{-2}\log(2D/\epsilon)\right\}\right),
 \qquad
 D=(n-c)\binom{h+a+b}{a+b}.
 \tag{EC1}
```

Here c is the number of components of the positive-weight input. The construction is randomized polynomial time with constant success probability for the one event covering **all failures and cuts**. Color classes can be arbitrarily large, labels can overlap, and endpoint colors may repeat. The coefficients do not change with the queried failure set.

For one color per vertex and no additional edge labels, (EC1) becomes

```math
O\!\left(\min\{m,\,
 n(h+1)\epsilon^{-2}\log(2n(h+1)/\epsilon)\}\right).
 \tag{EC2}
```

This improves the inverse-accuracy dependence of the earlier label-vector route for cut queries. It does **not** replace that route's stronger spectral guarantee.

The classical backend is Quanrud's existing quotient-sparsification theorem, together with the support-size resparsification lemma in 27_adaptive_quotient_resparsification.md. The new transfer is an exact polynomial-label decoder.

## 1. General incidence statement

Let A have rank r over a field K. Row i has a set R_i of labels; column e has a set S_e. Assume

```math
A_{ie}\ne0 \Longrightarrow
 R_i\subseteq S_e,\qquad |S_e\setminus R_i|\le k.
 \tag{EC3}
```

Failure of F deletes exactly the columns with S_e intersecting F. Column weights w_e are nonnegative. For each linear subspace W of the original column ambient space, consider

```math
\Phi_F(W)=
 \sum_{\substack{e:S_e\cap F=\varnothing\\a_e\notin W}}w_e.
 \tag{EC4}
```

**Theorem 1 (exact labeled-incidence transfer).** For every $`0<\epsilon<1`$, one nonnegative original-column reweighting preserves (EC4) within $`1\pm\epsilon`$, simultaneously for every $`|F|\le h`$ and every linear subspace $`W`$, using

```math
O(\min\{|E|,D\epsilon^{-2}\log(2D/\epsilon)\}),
 \qquad D=r\binom{h+k}{k}.
 \tag{EC5}
```

For explicit rational or finite-field representations and rational item weights, the construction is randomized polynomial time in the input length and $`\epsilon^{-1}`$, with success probability at least $`2/3`$. The cap in Section 4 makes this assertion uniform when $`h`$ and $`k`$ are input parameters.

**Proof.** Zero columns can be discarded. Select r independent **original rows** with selection matrix P, and write

```math
A=C(PA).
 \tag{EC6}
```

Keep the selected rows' original labels. No label set is assigned to an artificial linear combination of rows.

## 2. Homogeneous polynomial features

Use pairwise distinct field elements alpha_0,...,alpha_L for the L genuine labels and one dummy label 0 which never fails. Extend a finite field if necessary. Put

```math
\ell_c(z_0,\ldots,z_h)=\sum_{t=0}^h\alpha_c^t z_t.
```

For a label set T with |T|≤k, use the coefficient vector of

```math
p_T(z)=
 \left(\prod_{c\in T}\ell_c(z)\right)
 \ell_0(z)^{k-|T|}.
 \tag{EC7}
```

These are homogeneous degree-k polynomials in h+1 variables, so the coefficient-space dimension is

```math
K_{h,k}=\binom{h+k}{k}.
```

Use ordinary monomial coefficients. There is no division by factorials, so the construction works in every characteristic.

For a failure set F, define

```math
q_F(t)=\prod_{f\in F}
 \frac{t-\alpha_f}{\alpha_0-\alpha_f}
       =\sum_{j=0}^h\theta_j(F)t^j.
 \tag{EC8}
```

It has degree at most h, equals 1 at alpha_0, and vanishes at precisely the failed genuine label points. Therefore

```math
p_T(\theta(F))=\prod_{c\in T}q_F(\alpha_c).
 \tag{EC9}
```

The dummy factors evaluate to one, including for empty label differences. Write gamma_F(S)=product_{c in S} q_F(alpha_c). Then gamma_F(S)=0 exactly when S intersects F.

## 3. Exact decoding, including rank compression

For each original column e, its lift z_e has r polynomial blocks. The block indexed by selected original row i is

```math
(PA)_{ie}\,p_{S_e\setminus R_i}
 \tag{EC10}
```

when (PA)_{ie} is nonzero, and zero otherwise. The dimension is D=rK_{h,k}.

Define a linear map T_F to K^r: evaluate polynomial block i at theta(F), then multiply by gamma_F(R_i). Since R_i is a subset of S_e on every nonzero incidence,

```math
T_F z_e=\gamma_F(S_e)(PA)_e,
 \qquad
 CT_F z_e=\gamma_F(S_e)a_e.
 \tag{EC11}
```

These identities are exact. The scalar is common to the whole column. Its magnitude is irrelevant; only whether it vanishes matters.

Given an original subspace W, its preimage

```math
\widehat W_F=(CT_F)^{-1}(W)
```

is a subspace of the lifted space. Since W contains zero and is invariant under multiplication by a nonzero field element,

```math
z_e\notin\widehat W_F
 \Longleftrightarrow
 S_e\cap F=\varnothing\ \text{and}\ a_e\notin W.
 \tag{EC12}
```

Thus all queries (F,W) become ordinary subspace-complement queries on one fixed lifted instance.

## 4. Quotient sparsification

The function f(T)=rank{z_e:e in T} is normalized, integer-valued, monotone and submodular, with rank at most D. For every subspace U, the set Z_U={e:z_e in U} is closed: every column spanned by Z_U still belongs to U. Its complement is consequently a quotient of f.

Quanrud's theorem preserves the weight of every quotient with one nonnegative original-item reweighting. The companion resparsification lemma gives support O(D log(2D/epsilon)/epsilon^2), with constant success probability. Applying it to the lifted rank oracle and using (EC12) proves (EC5).

This event covers all subspaces and all failures at once. No union bound over failure scenarios and no later coefficient adjustment is needed. Every retained lifted column retains its original identity and receives its output coefficient. Optional merging of proportional lifted columns is safe because they belong to exactly the same lifted subspaces, including every preimage in (EC12); merging is not needed for the support bound.

### Uniform construction and finite arithmetic

Only the coefficients in (EC10) are materialized. The failure-dependent maps are proof devices and are never enumerated. Products of at most k linear factors can be computed in polynomial time in the displayed feature dimension.

If D≥|E|, return the input before constructing features. Compute binomial coefficients with a cap sufficient for this comparison. This makes the construction uniformly polynomial even when h and k are supplied as variable parameters. Replace h by min(h,L), and replace k by the maximum actual nonzero-incidence label deficit (in particular, k≤L). When h=0, one may directly use the ordinary quotient backend without multiplying dummy factors.

For rational A, take integer alpha values and use exact rational rank computations. Coefficient bit lengths are polynomial in h, k, log L and the input bit length. For a finite input field of size q_0<L+1, choose the least t with q_0^t≥L+1. There are fewer than q_0(L+1)≤(L+1)^2 monic degree-t polynomials to try, and standard irreducibility tests deterministically find an extension in polynomial time in the explicit label universe. If q_0≥L+1, use the original field. Rank is unchanged by extension, and every original-field subspace extends to a subspace with the same membership for original columns.

Unused labels are removed. The construction does not assume a deterministic poly(log L) extension construction for an implicitly enormous label universe. All graph applications can use a binary extension field of size O(L+1).

The rank-zero case has zero value for every query. The formulas also handle h=0 and k=0; degree zero gives a one-dimensional feature space.

## 5. Arbitrarily correlated vertex and edge failures

Take A to be an oriented vertex-edge incidence matrix. For e=uv put S_e=R_u union R_v union T_e, where T_e is its set of additional edge labels. Every nonzero incidence satisfies

```math
|S_e\setminus R_u|\le a+b.
```

Its rank over every field is n-c. For a Boolean vertex indicator x, x^T a_e is nonzero exactly when e crosses the cut, including in characteristic two. Apply (EC4) with W=ker(x^T). This proves (EC1).

Every cut of the surviving graph extends to a Boolean vector on the original vertex set. All edges incident to failed vertices have zero decoded image already. The cut itself and the failure set may therefore be chosen after preprocessing.

Pointwise cut preservation also approximates every surviving minimum-cut value, terminal-set-cut value, and maximum-cut value. It does not provide a new optimization algorithm for otherwise hard cut problems.

## 6. Matching powers in a cut-specific lower bound

This lower bound uses cut inequalities directly, rather than relying on a spectral lower bound.

Consider the unweighted complete bipartite graph K_{s,B}. Let W be the s by B nonnegative weighted adjacency matrix of a cut sparsifier, J the all-ones matrix, E=W−J, and t its support size. Singleton cuts on the right imply that every column sum of W lies in (1±epsilon)s.

For signs sigma in {−1,1}^s and tau in {−1,1}^B, the cut value is (total weight−sigma^T W tau)/2. The input cut value is at most sB; comparing with the full bipartition cut gives

```math
|\sigma^\top E\tau|\le3\epsilon sB.
 \tag{EC13}
```

Choose tau coordinatewise according to the signs of E^T sigma. Average uniform sigma and use the Khintchine bound E|a dot sigma|≥||a||_2/sqrt(2):

```math
\sum_{j=1}^B\|E_{\cdot j}\|_2
 \le3\sqrt2\,\epsilon sB.
 \tag{EC14}
```

If t_j is the support size in column j, its degree bound gives

```math
\|E_{\cdot j}\|_2
 \ge (1-\epsilon)s/\sqrt{t_j}-\sqrt{s}.
```

Every t_j is positive for epsilon<1. Convexity of u to u^{-1/2} and sum_j t_j=t now imply

```math
t\ge
 \frac{(1-\epsilon)^2sB}
 {(1+3\sqrt2\,\epsilon\sqrt{s})^2}.
 \tag{EC15}
```

For s=ceil(epsilon^{-2}) and 0<epsilon≤1/2 this is Omega(B/epsilon^2).

Let k=a+b≥1 and q=binom(h+k,k). Make q left blocks of s vertices each and a shared right part of B≥qs vertices. Index the blocks by k-subsets S of a universe of h+k labels. Split S into an a-element set A_S and b-element set T_S. All left vertices in that block carry A_S, and all its edges to the right part carry the additional labels T_S. Right vertices have no labels.

Failing exactly the h labels outside S isolates the K_{s,B} edges of block S. Every other block contains a failed label. Therefore (EC15) must hold independently in all q edge-disjoint blocks. Since n=B+qs≤2B, every simultaneous cut sparsifier needs

```math
\Omega\!\left(
 n\epsilon^{-2}\binom{h+a+b}{a+b}
 \right)
 \tag{EC16}
```

edges. The stated regime requires n sufficiently large compared with q/epsilon^2. Each input graph is simple and unweighted; output weights may be arbitrary and nonnegative. Thus the failure exponent and inverse-square accuracy dependence in (EC1) are jointly necessary in this regime, up to its logarithm.

## 7. Additional applications

**Represented matroid quotients and linear codes.** With empty row labels and at most d failure labels per column, take k=d. The summary preserves the total weight outside every linear subspace after every h-label failure with D=r binom(h+d,d). This includes every matroid quotient and the weighted Hamming objective of every codeword of a supplied linear code.

**Finite-field simplicial cochain cuts.** Label each simplex and face by its distinct vertex colors. A nonzero boundary incidence misses at most one distinct color, even with repeated colors, so k=1. A boundary matrix of rank r then admits O(r(h+1) log(2r(h+1)/epsilon)/epsilon^2) retained top simplices preserving the weighted support size of every coboundary after all h-color failures. This differs from real quadratic-form preservation and from a claim about top homology.

## 8. Sources and comparison boundary

* Quanrud, SODA 2024, *Quotient sparsification for submodular functions*, Theorem 1.1 and the restriction property: <https://kentq.s3.amazonaws.com/submodular-sparsification.pdf>. The classical ordinary sparsifier is credited, and the companion gives the resparsification details.
* Chandrasekaran–Chekuri–Wang–Zhu, 2025, *Hedgegraph Polymatroids*, Theorem 7, already gives ordinary weighted hedgegraph partition sparsifiers of size O(n log n/epsilon^2): <https://arxiv.org/html/2510.25043v1>.
* Basu–Brakensiek–Chen–Putterman–Reis–Zhang, September 2026, *Optimal Sparsifiers for Minkowski Sums and Sums of Seminorms*, gives optimal ordinary seminorm and hypergraph-cut support existentially: <https://arxiv.org/pdf/2609.20238>.
* Oko–Sakaue–Tanigawa, *Nearly Tight Spectral Sparsification of Directed Hypergraphs*, Section 7.8.2, distinguishes per-fixed-failure guarantees from one summary simultaneously valid for all failures: <https://arxiv.org/pdf/2204.02537>.

The contribution is exact labeled-incidence decoding for simultaneous correlated failures, followed by ordinary quotient sparsification, with the cut-specific lower bound above. The input labels can describe arbitrary large correlated classes. The exact decoding identity and the quoted quotient theorem establish the simultaneous guarantee.

