# Simultaneous spectral sparsifiers for correlated vertex and edge failures

**Abstract.** A rank-compressed graded incidence lift gives one original-edge spectral sparsifier for every allowed correlated vertex and edge failure. Repeated and overlapping labels are handled as sets. A single label-code event and one PSD inequality imply all failure guarantees with fixed output weights. Simple unweighted graphs give matching fault-parameter lower bounds.

## 1. Main statements

Let G be an arbitrary undirected graph with nonnegative rational edge weights, n vertices and m positive-weight nonloop edges. Parallel edges are allowed. Each vertex has at most a failure labels and each edge has at most b additional failure labels. Label sets may overlap arbitrarily. There are L occurring labels. A query F contains at most h labels and deletes every vertex or edge carrying one of them, together with edges incident to deleted vertices. Write G_F for the resulting graph. Its Laplacian is viewed on the original n coordinates, with zero rows and columns at deleted vertices.

The output is a subset H of ORIGINAL edges, with one fixed nonnegative multiplier for each retained edge. The required property is

```math
(1-\epsilon)L_{G_F}\preceq L_{H_F}\preceq(1+\epsilon)L_{G_F}
 \quad\text{for every }F,\ |F|\le h.
 \tag{1}
```

Both the retained subset and its weights are fixed before F is chosen. No new edges or query-dependent reweighting are used. One successful preprocessing event covers every F and every tested vector, including choices made after inspecting H.

Clip h at L and a,b at the actual maximum vertex and edge list sizes. If m=0 or r=rank(L_G)=0, return the empty graph. If L=0 or h=0, use ordinary spectral sparsification. Let R_u be the actual label set of vertex u and let T_e be the additional label set of edge e. Put

```math
p=a+b,\qquad S_e=R_u\cup R_v\cup T_e\quad(e=uv),
 \qquad q=\max_e|S_e|\le2a+b.
```

All unions are SET unions: repeated labels have one failure meaning. If q=0, ordinary sparsification suffices. Otherwise define

```math
s=\min\{L,h+q\},\qquad
 B_0=\left\lceil\frac{Cq}{\epsilon}
     \left(s\log\frac{eL}{s}+\log\frac2\zeta\right)\right\rceil,
 \qquad D=\min\{L,B_0\}.
 \tag{2}
```

Here C is a sufficiently large absolute constant and epsilon,zeta belong to (0,1). D is the actual rounded and capped dimension used before calculating the lift dimension. If the cap chooses D=L, use the identity code; otherwise use a random sign code. No later dimension rounding is hidden inside a parameter-dependent power.

Use the graded exterior feature space

```math
\mathcal E_{\le p}=\bigoplus_{j=0}^{\min\{p,D\}}
                              \bigwedge^j\mathbb R^D,
 \qquad K=\sum_{j=0}^{\min\{p,D\}}\binom Dj.
 \tag{3}
```

The degree-zero summand is a scalar coordinate. It is needed when an endpoint's labels already include every label on an edge.

**Mixed-label theorem.** There is a Monte Carlo polynomial-arithmetic construction satisfying (1), with success probability at least 1-zeta and support

```math
|H|=O\!\left(\min\left\{m,\frac r{\epsilon^2}
       \sum_{j=0}^{\min\{a+b,D\}}\binom Dj\right\}\right).
 \tag{4}
```

An explicit rational polynomial-bit implementation, obtained from the companion trace-exponential PSD sparsification subroutine, adds log(2rK) to the nontrivial support bound. This distinction concerns the implementation of the established PSD sparsification black box. All coding, feature construction, determinant normalization, and decoding algebra below have polynomial rational bit complexity.

For fixed a,b, h at least a+b, and a fixed success probability, an uncapped convenient form is

```math
O_{a,b}\!\left(\min\left\{m,
 \frac{r h^{a+b}\log^{a+b}(2L)}{\epsilon^{a+b+2}}
 \right\}\right).
 \tag{5}
```

The finite sum (4) is the statement when a or b varies. The actual maximum deficit max_{e=uv,x in {u,v}}|S_e minus R_x| can replace a+b throughout for a more refined instance-specific bound.

**One color per vertex.** For a=1,b=0, K=D+1. With the cap in (2), the bound is

```math
O\!\left(\min\left\{m,
 \frac r{\epsilon^3}
 \left[(h+2)\log\frac{eL}{\min\{L,h+2\}}
                  +\log\frac2\zeta\right]\right\}\right).
 \tag{6}
```

In the usual range h+2 at most L this is O(rh log(eL/h)/epsilon^3) for fixed success probability. A failed color class may contain arbitrarily many vertices. The graph may be nonbipartite, weighted, dense, and of unbounded degree. Edges whose endpoints have the same color use the degree-zero incidence coordinate; no distinct-color assumption is made.

**One color per edge.** For a=0,b=1, the same near-linear dependence on h follows from the simpler PSD item lift in the companion note. Formula (4) also includes it.

**Deterministic alternative.** Replace the random code with the explicit incoherent sign construction described below. Its dimension can be chosen as

```math
D_{\rm det}=O\!\left(\min\left\{L,
   \left((h+q)^2+\frac{hq^2}{\epsilon}\right)\log(2L)
 \right\}\right).
 \tag{7}
```

Use the actual returned integer dimension before calculating K in (3). The same bound (4) is then deterministic in the polynomial-arithmetic model. The polynomial-bit version again adds log(2rK). In particular one vertex color or one edge color gives

```math
O\!\left(\min\left\{m,
 \frac r{\epsilon^2}
 \min\{L+1,(h^2+h/\epsilon)\log(2L)+1\}
 \right\}\right).
 \tag{8}
```

The linear-h randomized bound is not asserted to have a deterministic construction with the same dimension. No efficient verification of optimal-dimensional RIP is assumed.

## 2. Label projection and normalized exterior features

Choose unit vectors v_c in R^D, one per label, with restricted isometry constant delta on every set of at most s=min(L,h+q) distinct labels. Standard random sign matrices provide this with probability at least 1-zeta in dimension

```math
D=O\!\left(\delta^{-2}
       \left(s\log\frac{eL}{s}+\log\frac2\zeta\right)\right).
 \tag{9}
```

The standard proof uses a constant-radius net on each sparse coordinate subspace and a fixed-vector concentration bound. The algorithm draws the signs without enumerating these subspaces. Identity color vectors give a deterministic code of dimension L.

Let P_F project orthogonally away from span{v_f:f in F}. For a live set S of at most q labels, restricted isometry bounds the cross-Gram norm by delta and the two within-set Gram matrices below by (1-delta)I. Hence for all x in span(V_S),

```math
(1-\tau)\|x\|^2\le\|P_Fx\|^2\le\|x\|^2,
 \qquad \tau=\frac{\delta^2}{(1-\delta)^2}.
 \tag{10}
```

Indeed orthonormalizing the two spans bounds their cross operator by delta/(1-delta), and squaring gives the projection loss. Empty F has zero loss.

Fix one order on labels. For a label SET S, define

```math
u_S=\bigwedge_{c\in S}^{\mathrm{in\ order}}v_c,
 \qquad \nu_S=\|u_S\|^2=\det(V_S^{\mathsf T}V_S).
 \tag{11}
```

For the empty set put u_empty=1, nu_empty=1. On the code event, every supplied column feature is nonzero. If S contains a failed label, its projected exterior product is zero. Otherwise the singular-value bound (10) gives

```math
(1-\tau)^q\le
 \frac{\|(\bigwedge^{|S|}P_F)u_S\|^2}{\nu_S}\le1.
 \tag{12}
```

Choose delta^2=epsilon/(64q). Then q tau at most epsilon/32, so every live ratio lies in [1-epsilon/32,1]. Both the normalization and this bound use the set of distinct labels; no multiplicity correction, dummy padding, or permanent is needed.

## 3. Graded incidence lift and rank compression

Orient each edge arbitrarily, and let A be the signed vertex-edge incidence matrix, with column a_e=e_u-e_v. Choose r independent ORIGINAL rows of A. Let P select them and fix a rational matrix C with

```math
A=C(PA).
 \tag{13}
```

The selected rows retain their vertex label sets. Equation (13) holds after any column deletion, including rank-dropping deletions.

For each endpoint x of e, define

```math
U_{x,e}=S_e\setminus R_x,\qquad |U_{x,e}|\le a+b,
 \qquad \eta_e=\nu_{S_e}>0.
 \tag{14}
```

Let e_{x,e} in {+1,-1} be the insertion sign satisfying

```math
u_{R_x}\wedge u_{U_{x,e}}=e_{x,e}u_{S_e}.
```

The sign is found simply by sorting the two disjoint ordered label lists.

In one K-dimensional block per selected original vertex, lift e=uv to

```math
z_e=\eta_e^{-1/2}\left[
      e_{u,e}(Pe_u)\otimes u_{U_{u,e}}
     -e_{v,e}(Pe_v)\otimes u_{U_{v,e}}\right].
 \tag{15}
```

A term is zero if its endpoint row was not selected. The two endpoints may use different exterior degrees; both belong to the same graded feature space (3). Form the rank-one PSD item

```math
\widetilde B_e=w_e z_ez_e^{\mathsf T}.
 \tag{16}
```

For analysis, use the common full graded exterior algebra E=direct sum_{j=0}^D wedge^j R^D. On vertex block x and a homogeneous input y of degree j, define the linear decoder L_F to output

```math
(Pe_x)\otimes
 \left[\left(\bigwedge_{c\in R_x}^{\mathrm{in\ order}}P_Fv_c\right)
                \wedge(\bigwedge^jP_F)y\right].
```

Extend linearly across grades. The insertion sign in (15) ensures the exact identity

```math
L_Fz_e=(Pa_e)\otimes
       \frac{(\bigwedge^{|S_e|}P_F)u_{S_e}}{\sqrt{\eta_e}}.
 \tag{17}
```

Every incidence lands in the common column grade |S_e| and has the same full-edge exterior feature. When the complement U_{x,e} is empty, the scalar coordinate is mapped directly to the row's projected feature. This covers equal endpoint colors and all overlaps between vertex and edge label sets.

Apply L_F by congruence, take partial trace over E, and apply C by congruence. This positive linear map sends

```math
\widetilde B_e\longmapsto
       \alpha_e(F) w_ea_ea_e^{\mathsf T},\qquad
 \alpha_e(F)=
       \frac{\|(\bigwedge^{|S_e|}P_F)u_{S_e}\|^2}{\eta_e}.
 \tag{18}
```

The scalar is zero for a failed edge and lies in [1-kappa,1] for a survivor, with kappa at most epsilon/32. The potentially large full graded algebra and all decoders are only proof objects. They are never materialized by preprocessing.

## 4. One sparsification serves every query

Apply the standard PSD sparsification theorem to the lifted sum at accuracy theta=epsilon/4. It returns fixed nonnegative multipliers lambda_e, supported on O(rK/epsilon^2) original edges, such that

```math
(1-\theta)\sum_e\widetilde B_e
 \preceq\sum_e\lambda_e\widetilde B_e
 \preceq(1+\theta)\sum_e\widetilde B_e.
 \tag{19}
```

This is one matrix inequality after the code is fixed. Applying (18), simultaneously for every F, gives

```math
(1-\theta)\sum_{e\in E_F}\alpha_e(F)w_ea_ea_e^{\mathsf T}
 \preceq\sum_{e\in E_F}\lambda_e\alpha_e(F)w_ea_ea_e^{\mathsf T}
 \preceq(1+\theta)\sum_{e\in E_F}\alpha_e(F)w_ea_ea_e^{\mathsf T}.
 \tag{20}
```

Nonnegativity of all multipliers and the interval for live alpha_e give

```math
(1-\theta)(1-\kappa)L_{G_F}
 \preceq L_{H_F}
 \preceq\frac{1+\theta}{1-\kappa}L_{G_F}.
 \tag{21}
```

These factors lie within 1 plus or minus epsilon. The delivered edge multiplier is lambda_e, without any alpha correction. A query merely removes failed original vertices and edges from H. There is no union bound over fault sets after the single code event.

## 5. Determinism and finite representations

The companion label-vector note gives an explicit conditional-expectation construction of unit sign vectors with coherence at most mu in O(mu^-2 log(2L)) dimensions. Choose rational mu within a constant factor of

```math
\min\left\{\frac1{4(h+q)},
           \sqrt{\frac{\epsilon}{64hq^2}}\right\}.
 \tag{22}
```

For failed F and live S, Gershgorin bounds both within-set Gram matrices below by 3I/4. Their cross block has squared Frobenius norm at most hq mu^2. Thus the squared projection loss on the live span is at most 2hq mu^2, and a normalized exterior feature of degree at most q loses at most 2hq^2 mu^2. This proves (7), followed by the same decoding proof. L at most one uses the identity code directly.

For every implementation, calculate the actual D and K and compare the target support with m before building exterior coordinates. If the target is at least m, return G. Otherwise rK and the required accuracy factors are polynomially bounded by m. This is a uniform polynomial construction even when a,b,h vary. The binomial sum has polynomial encoding length because D,p are bounded by the explicit label input; dimension calculations may stop once the full-input cap is reached.

Each normalizer eta_e is a determinant of size at most q. Computing it is polynomial even when q is an input parameter. Only exterior products of degree at most p, in the explicitly bounded K-dimensional space, are constructed. No degree-q feature or full graded algebra is needed.

There is a rational implementation without perfect-square rounding. Use the unnormalized INTEGER sign columns in every exterior product and recompute the corresponding Gram determinant eta_e. Restricted isometry is analyzed for the normalized sign columns; the spans, projectors, and normalized exterior volume ratios are unchanged. The identities (15)--(21) remain valid with the rescaled features and recomputed normalizers. Every lifted matrix entry is then of the form

```math
w_e\,\frac{\text{product of two signed integer exterior coordinates}}
                     {\eta_e}.
 \tag{23}
```

This includes cross terms between different exterior degrees. Exterior coordinates are ordinary minors in an orthonormal exterior basis, and all determinants have polynomial bit length. No nonorthonormal symmetric-coordinate metric or square root of eta_e is needed. The original-row selection and reconstruction C are rational.

If a random code gives a zero supplied column Gram determinant, detect it before division and declare failure; this happens only outside the sufficient RIP event. No verification of every restricted subspace or query is performed. The identity and deterministic coherence codes have no such failure.

The O(rK/epsilon^2) support bound invokes the established deterministic PSD sparsification theorem in its arithmetic model. An explicit polynomial-bit fallback uses the companion rational leverage/trace-exponential method on this one lifted instance, giving O(rK epsilon^-2 log(2rK)) support. Neither implementation enumerates failures. Preprocessing may have a high polynomial degree; no near-linear time claim is made.

## 6. Lower bounds matching the fault exponent

The following lower bound concerns every original-edge spectral summary, even one found with unlimited computation. It holds on simple, unweighted graphs.

### 6.1 A weighted subgraph of K_{k,B} needs many edges

Suppose a nonnegatively weighted subgraph H is a (1+-epsilon) spectral approximation to K_{k,B}, where 0<epsilon<=1/2 and k<=B. Let W be its k-by-B matrix of cross-edge weights, and let s_H count its positive entries. The original degree matrix is D_0=diag(B I_k,k I_B). The normalized Laplacian of K_{k,B} has operator norm 2. Therefore

```math
\left\|D_0^{-1/2}(L_H-L_{K_{k,B}})D_0^{-1/2}\right\|
 \le2\epsilon.
 \tag{24}
```

The off-diagonal block is -(W-J)/sqrt(kB). Its rank is at most k, and hence

```math
\|W-J\|_F^2\le4\epsilon^2 k^2 B.
 \tag{25}
```

Testing each right-vertex coordinate gives a column weight sum at least (1-epsilon)k. Summing all degrees also gives total weight at most (1+epsilon)kB. Cauchy-Schwarz over the s_H positive entries yields

```math
\sum_{ij}W_{ij}^2\ge
 \frac{(1-\epsilon)^2 k^2B^2}{s_H}.
```

Expanding (25), and using the upper bound on total weight, gives

```math
s_H\ge
 \frac{(1-\epsilon)^2 kB}{4\epsilon^2k+1+2\epsilon}
 =\Omega\!\left(\frac{B}{\epsilon^2+1/k}\right).
 \tag{26}
```

In particular, k=ceil(epsilon^-2) forces Omega(B/epsilon^2) retained edges. This elementary argument permits arbitrary positive output weights.

### 6.2 One vertex color

Take h+1 disjoint left blocks, each of k=ceil(epsilon^-2) vertices, joined completely to the same B right vertices. Give each left block its own color. Right vertices can be unlabeled, or all have one additional color that the queries below do not fail. Choose B>=(h+1)k.

Deleting the other h left colors leaves one K_{k,B}. Equation (26) forces Omega(B/epsilon^2) edges in every left block's portion of the summary. Since n=B+(h+1)k=Theta(B),

```math
|H|=\Omega\!\left(\frac{n(h+1)}{\epsilon^2}\right)
 \tag{27}
```

whenever n is at least a sufficiently large constant times (h+1)/epsilon^2. For constant epsilon this already proves the optimality, up to logarithms, of the n,h dependence in (6). It also shows that the extra inverse-accuracy factor in the RIP upper bound is a genuine remaining gap of this method, rather than a hidden lower-bound match.

For the edge-color version, color all edges incident to a given left block by that block's color. The same argument applies.

### 6.3 Mixed overlapping lists

Let p=a+b>0 and q=binom(h+p,p). Take a label universe of size h+p. For each p-subset S, create a left block of k vertices and connect it completely to the same B right vertices. Choose any a-subset A_S of S. Give every vertex in this block the label set A_S, and give each of its incident edges the b-label set S minus A_S. Right vertices have empty label lists.

For each S, fail the complementary h labels F=[h+p] minus S. An edge of a block T survives exactly when T is disjoint from F, that is, T is a subset of S. Since both have size p, this means T=S. Surviving vertices of other blocks are isolated and have no effect on the Laplacian.

Thus every block independently requires Omega(B/epsilon^2) retained edges by (26). When B>=q ceil(epsilon^-2), n=Theta(B), and

```math
|H|=\Omega\!\left(
 \frac{n}{\epsilon^2}\binom{h+a+b}{a+b}\right).
 \tag{28}
```

The graph is simple and unweighted. The bound applies whenever n is at least a constant times q/epsilon^2. For fixed a,b and constant epsilon, it matches the exponent h^{a+b} in (5), up to logarithms. This is stronger than merely requiring connectivity preservation.

## 7. Baselines and boundaries

Random RIP codes and PSD sparsification are established results. The cross-incidence identity (17), the original-row rank reduction, and the all-failure positive decoding argument are the composition proved in this manuscript. The exact-rank colored graph lifts from the earlier checkpoint are not by themselves spectral sparsifiers: the relative feature-norm control in (12) is an additional ingredient.

Oko-Sakaue-Tanigawa, Section 7.8.2, distinguishes success for each fixed failure set from one event covering every set. It states an individual-hyperedge-failure result with the former quantifier and discusses a stronger uniform extension. Its quoted discussion also says that the prior Zhu et al. analysis does not establish uniformity over all failures. For ordinary graphs, the discussed uniform individual-edge extension has size O(h n log^2(n)/epsilon^2). That model cannot be applied with parameter h to h color classes containing arbitrarily many vertices or edges. This manuscript does not claim to improve the h exponent already known for individual edge failures.

Basu-Kothari-Liu-Meka gives general PSD sparsification governed by a quantitative connectivity threshold. Khanna-Putterman-Sudan develops a broad theory for real-valued code sparsification. These are important broader antecedents; neither graph independence from query directions nor ordinary PSD sparsification is claimed new. The specific comparison here is polynomial preprocessing for one common original-edge summary under correlated label deletion. Priority of that statement remains subject to further review.

The theorem preserves cuts, quadratic energies, kernels, and eigenvalue comparisons for each surviving graph through (1). Standard consequences such as effective-resistance comparisons follow on the common surviving range. It does not preserve shortest-path distances, directed nonlinear Laplacians, an arbitrary growing graph, or an unbounded failure budget after preprocessing. The labels, h, and epsilon are fixed before the summary is constructed.

### Primary references

1. Baraniuk, Davenport, DeVore, Wakin. *A Simple Proof of the Restricted Isometry Property for Random Matrices*. Constructive Approximation 28 (2008). https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/2/436/files/2011/04/baraniuk08si.pdf?bid=436
2. de Carli Silva, Harvey, Sato. *Sparse Sums of Positive Semidefinite Matrices*, Theorem 3. https://arxiv.org/pdf/1107.0088
3. Oko, Sakaue, Tanigawa. *Nearly Tight Spectral Sparsification of Directed Hypergraphs by a Simple Iterative Sampling Algorithm*, arXiv v2, Section 7.8.2. https://arxiv.org/pdf/2204.02537
4. Zhu et al. *Improved Dynamic Graph Learning through Fault-Tolerant Sparsification*. ICML 2019. https://proceedings.mlr.press/v97/zhu19b/zhu19b.pdf
5. Basu, Kothari, Liu, Meka. *Sparsifying Sums of Positive Semidefinite Matrices*. SODA 2026. https://arxiv.org/pdf/2508.08169
6. Khanna, Putterman, Sudan. *A Unified Theory of Sparsification*. July 2026. https://arxiv.org/pdf/2607.16126
7. Wigderson, Xiao. *Derandomizing the Ahlswede-Winter Matrix-Valued Chernoff Bound Using Pessimistic Estimators, and Applications*. Theory of Computing 4 (2008). https://theoryofcomputing.org/articles/v004a003/v004a003.pdf

