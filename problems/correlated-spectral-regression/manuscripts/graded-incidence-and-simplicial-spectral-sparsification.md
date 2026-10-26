# Graded exterior incidence lifts: spectral sparsification under correlated vertex failures

**Abstract.** We construct a rank-compressed graded exterior lift whose degree is the number of new labels introduced by an incidence. A scalar coordinate handles repeated labels. One PSD sparsification in this space preserves every allowed correlated deletion, with linear failure-budget dependence for simplicial boundary matrices of fixed dimension.

## 1. Simplicial theorem

Let K be a finite p-dimensional simplicial complex, p at least one. Let N be its number of p-simplices and let A be its oriented boundary matrix from p-chains to (p-1)-chains. Write r=rank(A), over the real numbers. Each vertex has one color from an explicit universe of L occurring colors. A failure set F of at most h colors deletes all vertices carrying those colors and every incident simplex. A color may occur on arbitrarily many vertices, and a simplex may contain several vertices of the same color.

Fix positive weights w_sigma on the p-simplices. In the common ambient space of original (p-1)-faces, put

```math
L_F=\sum_{\sigma:\ c(\sigma)\cap F=\varnothing}
                   w_\sigma a_\sigma a_\sigma^{\mathsf T},
\tag{1}
```

where a_sigma is a boundary column. Rows belonging to deleted faces are automatically zero. Let q be the largest number of **distinct** colors on a top simplex; thus q at most p+1, and q can be smaller.

Clip h at L and set

```math
s=\min\{L,h+q\},\qquad
 B=s\log\frac{eL}{s}+\log\frac2\zeta,
```

where epsilon,zeta belong to (0,1). There is a randomized construction of a subset H of original p-simplices and fixed nonnegative weights such that, with probability at least 1-zeta, simultaneously for every allowed F,

```math
(1-\epsilon)L_F\preceq
 \widetilde L_F:=
 \sum_{\sigma\in H:\ c(\sigma)\cap F=\varnothing}
                  \widetilde w_\sigma a_\sigma a_\sigma^{\mathsf T}
 \preceq(1+\epsilon)L_F.
\tag{2}
```

The same H and the same weights work for all queries. The lower skeleton is retained. In the standard polynomial-arithmetic PSD-sparsification model, the support bound is

```math
\boxed{\quad
 |H|=O\!\left(\min\left\{N,
 \frac r{\epsilon^2}
 \left[1+\min\left\{L,\frac{qB}{\epsilon}\right\}\right]
 \right\}\right).
 \quad}
\tag{3}
```

For fixed p and epsilon and h at least p+1, this has linear h dependence up to logarithms. It is polynomial in the explicitly supplied boundary matrix and face vertex sets **even when p is part of the input**. No full listing of every lower-dimensional face is needed to construct the top-dimensional spectral summary, and no proper-coloring assumption is used.

The displayed support bound invokes the ordinary O(R/epsilon^2)-support sparsification theorem in lifted rank R. For an explicitly specified rational polynomial-bit implementation, ordinary leverage sampling on that one lifted matrix adds a factor log(2R/zeta); standard two-sided trace-exponential derandomization adds log(2R). These are alternative implementations of the last, classical, single-matrix step. All new coding, normalization, rank compression, and lifting steps below have polynomial rational bit complexity. Neither implementation enumerates failure sets.

If h=0 or no relevant label occurs, ordinary O(r/epsilon^2) sparsification suffices. If r=0, the empty top summary suffices. Zero-weight top cells can be removed before defining the target matrix. Uncolored vertices can be given a permanent color that is excluded from every failure query.

## 2. A general incidence theorem

The proof works for a broader and simple matrix structure. Let A be any real matrix with N columns and rank r. Each row i has a fixed **set** R_i of labels and each column j a set S_j. Assume

```math
A_{ij}\ne0\quad\Longrightarrow\quad R_i\subseteq S_j,
 \qquad |S_j\setminus R_i|\le k,
 \qquad |S_j|\le q.
\tag{4}
```

Failing F deletes column j exactly when S_j meets F. For any fixed positive column weights, we seek the same common-weight spectral guarantee for all these column deletions.

Let V have D-dimensional color vectors with sufficiently small restricted isometry constant on every set of at most s=min(L,h+q) colors. Define

```math
\mathcal E_{\le k}
   =\bigoplus_{a=0}^{\min\{k,D\}}\bigwedge^a\mathbb R^D,
 \qquad
 K_D=\dim\mathcal E_{\le k}
     =\sum_{a=0}^{\min\{k,D\}}\binom Da.
\tag{5}
```

The degree-zero summand is one-dimensional. The incidence theorem gives support

```math
O\!\left(\min\left\{N,\frac{rK_D}{\epsilon^2}\right\}\right),
\tag{6}
```

with D as in (3), and with the same bit-implementation qualification. For fixed k, its dependence on the failure budget is h^k up to logarithms, regardless of the total number q of labels on a column. The more precise finite sum in (5) applies when k varies.

For a simplicial boundary, let R_tau be the set of distinct vertex colors on a facet tau, and S_sigma the corresponding set on a top simplex sigma. If tau is a facet of sigma, then S_sigma minus R_tau is either empty or a singleton. It is empty exactly when the missing vertex's color already occurs elsewhere on tau. Thus k=1 and K_D=D+1, proving the dimension in (3).

This use of **sets** is deliberate. Failure membership is idempotent: a repeated color on one simplex does not create a second independent failure condition. The scalar degree-zero coordinate is what allows this idempotence to be reflected in a linear incidence lift.

## 3. Basis-row compression

Select r independent **original** rows of A and let P be the selection matrix. There is a fixed matrix C such that

```math
A=C(PA).
\tag{7}
```

Every later restriction of the column set satisfies the same identity. Hence a PSD approximation for weighted sums of selected-row columns lifts to the full matrix by congruence with C. This remains valid when failures lower the rank. Selecting original rows also preserves their associated label sets R_i.

The lift therefore needs only rK_D coordinates. It does not require a generic-code rank argument, and it does not assume that the original boundary matrix has full row rank.

## 4. Uniform control of live color spans

Use unit color vectors v_c with the delta restricted isometry property

```math
(1-\delta)I\preceq V_T^{\mathsf T}V_T
                     \preceq(1+\delta)I
       \quad (|T|\le s).
\tag{8}
```

Let P_F be orthogonal projection away from span{v_f:f in F}. If S is disjoint from F and |S| at most q, then on W_S=span{v_c:c in S},

```math
(1-\tau)\|x\|^2\le\|P_Fx\|^2\le\|x\|^2,
 \qquad \tau=\frac{\delta^2}{(1-\delta)^2}.
\tag{9}
```

Indeed, the cross-Gram norm ||V_F^T V_S|| is at most delta. Both within-set Grams have minimum eigenvalue at least 1-delta. For x=V_S y, the norm of its projection onto span(V_F) is at most delta||y||/sqrt(1-delta), whereas ||x|| is at least sqrt(1-delta)||y||. Squaring gives (9).

If u is a nonzero exterior product of a at most q vectors from W_S, its normalized squared volume after projection satisfies

```math
(1-\tau)^a
 \le\frac{\|(\bigwedge^aP_F)u\|^2}{\|u\|^2}\le1.
\tag{10}
```

This is the product of the squared singular values of the projection on their span. The square in tau is essential; a first-order use of RIP would introduce another inverse-accuracy factor.

Standard normalized random sign matrices satisfy (8), with probability at least 1-zeta, in

```math
D=O\!\left(\delta^{-2}
       \left[s\log\frac{eL}{s}+\log\frac2\zeta\right]\right)
\tag{11}
```

dimensions. If the proposed dimension reaches L, use the L orthonormal color vectors instead. That branch is deterministic and has tau=0. The code is Monte Carlo; no polynomial-time RIP verification is assumed. The RIP event already covers all relevant S and F.

## 5. The graded exterior lift

Fix one total order on the labels. For a set S write

```math
u_S=\bigwedge_{c\in S}^{\text{in order}}v_c,
 \qquad
 \nu_S=\|u_S\|^2=\det(V_S^{\mathsf T}V_S).
\tag{12}
```

For the empty set, u_empty=1 and nu_empty=1. On the RIP event all supplied column normalizers are positive. These are Gram determinants, not permanents.

For a nonzero selected-row incidence i,j, put U_ij=S_j minus R_i. Let e_ij in {+1,-1} be the wedge-insertion sign determined by

```math
u_{R_i}\wedge u_{U_{ij}}=e_{ij}u_{S_j}.
\tag{13}
```

This sign is purely combinatorial, from the fixed label order. Lift column j to

```math
z_j=\nu_{S_j}^{-1/2}
   \sum_{i\text{ selected}} A_{ij}e_{ij}\,
                 e_i\otimes u_{U_{ij}}
       \quad\in\mathbb R^r\otimes\mathcal E_{\le k}.
\tag{14}
```

If U_ij is empty, its contribution is in the scalar degree-zero coordinate. For a simplicial incidence introducing a new color c, it contributes the signed vector v_c in degree one. These are the only two possibilities in the simplicial theorem.

Apply ordinary PSD sparsification, with accuracy eta=epsilon/4, to the rank-one items w_j z_j z_j^T. It produces nonnegative multipliers theta_j, supported on O(rK_D/epsilon^2) original columns, such that

```math
(1-\eta)\sum_jw_jz_jz_j^{\mathsf T}
 \preceq\sum_j\theta_jw_jz_jz_j^{\mathsf T}
 \preceq(1+\eta)\sum_jw_jz_jz_j^{\mathsf T}.
\tag{15}
```

The output weight of item j is theta_j w_j.

## 6. All failure queries from one PSD inequality

The common proof target is the full graded exterior algebra

```math
\mathcal E=\bigoplus_{a=0}^{D}\bigwedge^a\mathbb R^D.
```

It need not be constructed. For each row i and query F, define a linear map on a homogeneous y of degree a by

```math
T_F(e_i\otimes y)
 =e_i\otimes
    \left[\left(\bigwedge_{c\in R_i}^{\text{in order}}P_Fv_c\right)
                \wedge(\bigwedge^aP_F)y\right],
\tag{16}
```

and extend linearly to the direct sum. Different input grades may be sent to different output grades. This causes no problem because every nonzero incidence in column j lands in the common grade |S_j|.

By (13), appending the row labels gives the exact factorization

```math
T_Fz_j=(Pa_j)\otimes\phi_j(F),
 \qquad
 \phi_j(F)=\nu_{S_j}^{-1/2}
             (\bigwedge^{|S_j|}P_F)u_{S_j}.
\tag{17}
```

The two insertion signs multiply to one. If S_j meets F, one wedge factor is zero, so phi_j(F)=0 exactly. If j survives, (10) gives

```math
\alpha\le\|\phi_j(F)\|^2\le1,
 \qquad \alpha=(1-\tau)^q.
\tag{18}
```

Apply the congruence T_F to (15), take the partial trace over the common graded algebra, and apply congruence C from (7). Partial trace preserves PSD order and replaces phi_j phi_j^T by its trace ||phi_j||^2. The resulting inequality is (15) for the true and selected surviving original-column sums, with each weight multiplied by the common factor ||phi_j(F)||^2.

Let M_F be the true surviving sum and let Mhat_F be the output sum with its original fixed weights theta_j w_j. Using (18) on both sides gives

```math
(1-\eta)\alpha M_F\preceq\widehat M_F
       \preceq\frac{1+\eta}{\alpha}M_F.
\tag{19}
```

Choose delta^2=epsilon/(64q) when q is positive. Then tau at most 2delta^2 and alpha at least 1-epsilon/32. With eta=epsilon/4, (19) implies the required 1 plus or minus epsilon inequality. Equations (11), (14), and (15) prove (3) and (6).

The large graded algebra and all maps T_F are only proof objects. Preprocessing builds the rK_D-dimensional lift. A query merely deletes failed original items and retains their preassigned weights.

## 7. Uniform preprocessing and rational arithmetic

The column normalizer nu_S is a determinant of size at most q. Thus the construction is polynomial in the boundary-only simplicial input even when p grows. Repeated colors have already been removed from S, and create no normalization difficulty.

Mixed grades in (14) can be implemented without algebraic square roots. Use the **unnormalized integer sign columns** in every exterior product and recompute each Gram determinant with those columns. The RIP statement is analyzed after dividing the columns by sqrt(D); the subspaces, projection operators, and normalized exterior volume ratios are unchanged. More directly, (13)--(19) hold for these uniformly rescaled color vectors as written, with the recomputed normalizers. Each coordinate of u_U is then an integer determinant, and every lifted PSD entry has the rational form

```math
w_j\,
 \frac{A_{ij}A_{i'j}e_{ij}e_{i'j}
                 (u_{U_{ij}})_a(u_{U_{i'j}})_b}{\nu_{S_j}}.
\tag{20}
```

The numerator determinants and Gram determinants have polynomial bit length. This also handles cross terms between different exterior grades. A rational basis-row reduction and a rational matrix C suffice; no orthonormal basis of the original column space is required.

Before forming any exterior coordinates, compute K_D and compare the promised support bound with N. If that bound reaches N, return the original input with weight one. Otherwise rK_D and the relevant reciprocal-accuracy factors are polynomially bounded by N. The binomial sum itself has polynomial encoding length because D at most L and k at most q at most L. Consequently all explicitly materialized exterior coordinates and lifted matrices have polynomial size, even when h,k,q are input parameters.

If a random code makes a supplied column Gram determinant zero, detect that before division and declare failure. This occurs only outside the sufficient RIP event. There is no test of all deletion scenarios. The identity-code branch never has this issue.

For a completely specified polynomial-bit randomized last step, compute the lifted leverage traces exactly and perform ordinary leverage sampling on this one matrix. Matrix Chernoff yields O(R epsilon^{-2}log(2R/zeta)) retained items, where R is its actual rank. Allocate half the failure probability to the code and half to this sampling step. A standard finite-precision trace-exponential conditional-expectation implementation instead gives O(R epsilon^{-2}log(2R)) items deterministically after the code is fixed. These classical alternatives preserve the same single-event, all-query conclusion. The logarithmic overhead should remain explicit when this bit implementation is the intended guarantee.

## 8. An explicit deterministic code tradeoff

Full RIP is not necessary for a deterministic version. Assume h,q are positive. Take unit color vectors with pairwise coherence at most mu, chosen so that

```math
\mu\le\frac1{4\max\{h,q\}},\qquad
 \mu^2\le\frac{\epsilon}{64h q^2}.
\tag{21}
```

For disjoint F,S of sizes at most h,q, respectively, Gershgorin gives both within-set Gram minima at least 3/4. The cross-Gram norm is at most mu sqrt(hq), by its Frobenius norm. After orthonormalizing the two spans, their cross norm is at most (4/3)mu sqrt(hq). Thus the squared projection loss on the live span is at most 2hq mu^2. A normalized exterior feature of degree at most q loses at most 2h q^2mu^2, at most epsilon/32. The proof of (18)--(19) therefore applies directly.

There is a deterministic rational construction of such sign codes in

```math
D_{\rm det}=O\!\left[
       \left(h^2+q^2+\frac{hq^2}{\epsilon}\right)\log(2L)
                    \right]
\tag{22}
```

dimensions, with the identity-code cap D at most L. Here is a self-contained conditional-expectation construction. Choose a rational mu=1/b within a factor two below its required upper bound, let lambda=mu/2, and choose D to be a sufficiently large multiple of b^2 ceil(log_2(2L)). For D-by-L signs s_jc, consider

```math
\sum_{c<c'}\left[
   \prod_{j=1}^D(1+\lambda s_{jc}s_{jc'})+
   \prod_{j=1}^D(1-\lambda s_{jc}s_{jc'})\right].
\tag{23}
```

Its initial expectation is L(L-1). Fix the signs one at a time, always choosing the smaller conditional expectation. Every conditional mean is an explicit rational product sum. If a final pair has absolute correlation at least mu D, its corresponding product is at least exp(mu^2D/4), greater than the initial whole potential. Thus no such pair exists. Normalizing the sign columns gives the required coherence, and all calculations have polynomial bit complexity.

For the simplicial theorem this gives deterministic arithmetic-operation support

```math
O\!\left(\min\left\{N,
 \frac r{\epsilon^2}
 \left[1+\min\left\{L,
 C\left(h^2+q^2+\frac{hq^2}{\epsilon}\right)\log(2L)
 \right\}\right]\right\}\right).
\tag{24}
```

For fixed p, the code dimension has the form h^2+h/epsilon. The general incidence theorem uses K_D from (5) with this deterministic D. The arithmetic-operation versus explicit polynomial-bit logarithmic qualification is the same as in Section 1. L at most one is handled by the identity code directly.

## 9. A lower bound for the simplicial problem

For fixed dimension, linear dependence on h is necessary even for distinct vertex colors. Put t=p+1 and take the complete p-dimensional skeleton on h+t vertices, with positive weights and a distinct color on each vertex. For any particular top simplex sigma, failing its h complementary vertices leaves sigma as the sole top simplex. If a multiplicative sparsifier with epsilon less than one omitted sigma, its matrix for this query would be zero while the true matrix is nonzero. Hence every top simplex must be retained:

```math
N=\binom{h+t}{t}.
```

The real boundary rank is

```math
r=\binom{h+t-1}{t-1},\qquad
 N=\frac{h+t}{t}\,r.
\tag{25}
```

For a direct rank proof, the boundaries of top simplices containing a fixed apex form a basis: the facets omitting the apex give pivots, and the boundary-of-boundary identity expresses every other top boundary in that basis. Disjoint copies yield the same ratio for arbitrarily large ranks.

Thus the randomized theorem has optimal linear h dependence for fixed p, up to logarithms and its accuracy dependence. This lower argument does not claim that the epsilon^{-3} dependence is optimal.

## 10. Topological scope and comparison

After any F, the retained lower skeleton is exactly the original surviving lower skeleton. Therefore the down-Laplacian in degree p-1 is unchanged. Adding this common PSD matrix to (2) gives the same relative approximation for the full Hodge Laplacian in degree p-1. Its kernel, and therefore real (p-1)-homology, is preserved exactly after every allowed failure. Fixed positive lower-cochain inner products can be included by congruence.

The size bound counts top simplices; the lower skeleton remains part of the output. The input weighting is fixed before preprocessing. This is a real spectral theorem. It does not assert preservation of top-degree homology or simultaneous spectral approximation at every filtration threshold.

Static up-Laplacian sparsification is established. Osting--Palande--Wang [3] extends effective-resistance sampling to fixed-dimensional simplicial complexes. Savostianov--Schaub--Guglielmi--Tudisco [4] develops efficient approximation of the generalized effective-resistance probabilities. Their stated static guarantees do not themselves supply one fixed-weight summary for every correlated vertex-color deletion.

The graph case has specialized fault-tolerant sparsification results, including Zhu et al. [5]. Oko--Sakaue--Tanigawa [6, Section 7.8.2] distinguishes a high-probability guarantee for each fixed fault set from one common high-probability event for all fault sets. The present construction has the latter quantifier. Its comparison concerns arbitrary-dimensional incidence matrices and failed color classes of unbounded size; it is not a claim to improve every specialized graph bound for individual faults.

The 2026 unified sparsification framework of Khanna--Putterman--Sudan [7] is a relevant broad antecedent. Its general existence theorem is expressed through CVNRD at a substantially rescaled accuracy and does not by itself provide the explicit polynomial incidence construction and parameter bounds proved here. No implication from a total-sensitivity bound alone to its CVNRD parameter is assumed. Further priority checking should compare the precise simultaneous common-weight query model.

The contribution is the graded incidence factorization (14)--(17), especially the scalar treatment of repeated colors and its r(D+1) simplicial dimension. RIP, PSD sparsification, exterior algebra, and ordinary spectral consequences are credited ingredients.

### Primary sources

1. Joshua Batson, Daniel A. Spielman, and Nikhil Srivastava. *Twice-Ramanujan Sparsifiers*. General vector sparsification and its deterministic arithmetic construction. https://cs-www.cs.yale.edu/homes/spielman/PAPERS/77287.pdf
2. Richard Baraniuk, Mark Davenport, Ronald DeVore, and Michael Wakin. *A Simple Proof of the Restricted Isometry Property for Random Matrices*. Constructive Approximation 28 (2008), 253--263. https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/2/436/files/2011/04/baraniuk08si.pdf
3. Braxton Osting, Sourabh Palande, and Bei Wang. *Spectral Sparsification of Simplicial Complexes for Clustering and Label Propagation*. Journal of Computational Geometry 11(1) (2020), 176--211. https://jocg.org/index.php/jocg/article/view/3098 and https://arxiv.org/pdf/1708.08436
4. Anton Savostianov, Michael T. Schaub, Nicola Guglielmi, and Francesco Tudisco. *Efficient Sparsification of Simplicial Complexes via Local Densities of States*. https://arxiv.org/pdf/2502.07558
5. Chunjiang Zhu, Sabine Storandt, Kam-Yiu Lam, Song Han, and Jinbo Bi. *Improved Dynamic Graph Learning through Fault-Tolerant Sparsification*. ICML 2019. https://proceedings.mlr.press/v97/zhu19b/zhu19b.pdf
6. Kazusato Oko, Shinsaku Sakaue, and Shin-ichi Tanigawa. *Nearly Tight Spectral Sparsification of Directed Hypergraphs by a Simple Iterative Sampling Algorithm*. Section 7.8.2. https://arxiv.org/pdf/2204.02537
7. Sanjeev Khanna, Aaron Putterman, and Madhu Sudan. *A Unified Theory of Sparsification*. July 2026. https://arxiv.org/abs/2607.16126
8. Avi Wigderson and David Xiao. *Derandomizing the Ahlswede--Winter Matrix-Valued Chernoff Bound Using Pessimistic Estimators, and Applications*. Theory of Computing 4 (2008). https://theoryofcomputing.org/articles/v004a003/v004a003.pdf
