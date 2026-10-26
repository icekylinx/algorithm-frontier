# Overlap-density bounds for aligned nonlinear numeric rows

**25 October 2026. Complete new transfer and proof; root and independent full mathematical reviews passed.**

The overlap-density algorithm extends to compressed separable nonlinear constraints when their marginal directions are aligned with the inequality directions. The incidence condition is imposed on the explicit common marginal-band columns. It is not inferred merely from a list of original function dependencies.

Under the model below, if each refined band is positive in at most two target rows and the band-row interaction graph has `m_B` edges, exact scalar optimization takes

$$
\boxed{
\exp\!\left(O\!\left(T\log\left(2+\frac{m_B}{T}\right)\right)\right)
\operatorname{poly}(H)
}
\tag{ND1}
$$

for `T>0`, with polynomial binary workspace. The zero-target case is polynomial. Original mandatory resource totals and all function domains are retained. The proof is exact and introduces no approximation error.

This is a new refinement of [aligned-nonlinear-mixed-numeric-targets.md](aligned-nonlinear-mixed-numeric-targets.md), using [row-overlap-density-numeric-target-refinement.md](row-overlap-density-numeric-target-refinement.md). Neither frozen manuscript is modified.

## 1. Nonlinear input model

Let `F` be one integral polymatroid rank on an explicit ground `E`, and let the integer resource vector belong to either `P(F)` or the original base `B(F)`. Put `R=F(E)` before masks and genuine hard domains. An eligibility mask is allowed. Coordinate `e` has a binary integer domain `0<=x_e<=d_e`; a shorter supplied domain may make the mandatory model infeasible and does not redefine `R`.

For each target row `j`,

$$
A_j(x)=\sum_e A_{je}(x_e)\ \rho_j\ T_j,
\qquad
T_j\in\mathbb Z_{\ge0},
\qquad T=\sum_jT_j.
\tag{ND2}
$$

Every coordinate function is zero at zero and is specified over its whole domain by explicit constant marginal bands with nonnegative integer slopes. Required shapes are:

| Target relation | Coordinate-function condition |
|---|---|
| `A_j(x)<=T_j` | Convex: marginal slopes are nondecreasing |
| `A_j(x)>=T_j` | Concave: marginal slopes are nonincreasing |
| `A_j(x)=T_j` | Linear: one constant marginal slope |

The scalar objective is `W(x)=sum_e W_e(x_e)`, with explicit rational marginal bands and `W_e(0)=0`. For exact **minimization**, its marginal slopes must be nondecreasing; for exact **maximization**, they must be nonincreasing.

For this exact-optimization transfer, scalar marginal slopes need not be nonnegative. This slightly extends the nonnegative-scalar convention of the earlier aligned note: the proof below uses only their order, and the linear profile primitive permits arbitrary rational scalar weights. Finite domains keep the objective bounded. Target-row slopes remain nonnegative integers.

There is one scalar objective. An upper side condition on a minimized scalar, or a lower side condition on a maximized scalar, can be decided by its exact extremum. No unrelated second scalar optimization under that side condition is claimed.

## 2. Common marginal bands and the shared resource

Refine the breakpoints of all target functions and the scalar function on each original coordinate into common intervals. Let the positive integer interval lengths be `ell_(e,i)`, the integer target slopes be `a^j_(e,i)`, and the rational scalar slopes be `w_(e,i)`. The number of refined intervals is bounded by the total number of supplied breakpoints. Binary lengths are not expanded into unit coordinates.

Let `D` be the explicit band ground, and let `pi` map a band to its original coordinate. The shared, box-restricted band rank is

$$
G(S)=\min_{A\subseteq E}
\left\{F(A)+
\sum_{e\notin A}\sum_{i:(e,i)\in S}\ell_{e,i}\right\}.
\tag{ND3}
$$

This is an integral polymatroid rank with

$$
P(G)=P\bigl(S\mapsto F(\pi(S))\bigr)
\cap\{0\le z_{e,i}\le\ell_{e,i}\}.
\tag{ND4}
$$

One proof writes the coordinate-box intersection rank as
`min_(Y subset S) [F(pi(Y))+ell(S\Y)]`. Once a band of an original coordinate is placed in `Y`, including all its bands present in `S` leaves the first term unchanged and can only decrease the second, giving ND3. The modular-convolution formula is submodular by applying submodularity to two minimizers and modularity to their complementary pieces. It is normalized, monotone, and integral. The two inclusions in ND4 follow by splitting every set into `Y` and its complement, and by separately recovering the original rank and singleton bounds.

Rank evaluation uses submodular minimization on the original explicit coordinate ground with a modular adjustment. Its bit complexity is polynomial in the complete band input.

Aggregating `x_e=sum_i z_(e,i)` gives exactly `P(F)` intersected with the original domains. Conversely, each aggregate count has its canonical prefix-band representation. Total mass is unchanged. In the mandatory model keep `z(D)=R`; if a domain or eligibility mask reduces the available band rank below `R`, reject infeasibility. The required total is never replaced by a restricted rank.

## 3. Prefix repacking and all row directions

For aggregate count `x_e`, let `z^*_(e,i)` fill the bands in their original order up to that count. Its cumulative count through every initial band is at least that of any other band vector with the same aggregate. If `Z_h` and `Z_h^*` are these cumulative counts, then for arbitrary marginal slopes `v_i`,

$$
\sum_i v_i(z_i^*-z_i)
=\sum_{h<m_e}(v_h-v_{h+1})(Z_h^*-Z_h).
\tag{ND5}
$$

The total difference is zero, and every cumulative difference is nonnegative. Therefore prefix repacking decreases convex marginal sums, increases concave marginal sums, and preserves linear sums exactly. No sign assumption on the scalar slopes is used in ND5.

Consequently, if a linear band vector meets the target rows, its original aggregate satisfies

$$
\begin{array}{c|c}
\text{row type}&\text{comparison after aggregation}\\ \hline
\text{convex upper}&A_j(x)\le\sum_{e,i}a^j_{e,i}z_{e,i}\le T_j\\
\text{concave cover}&A_j(x)\ge\sum_{e,i}a^j_{e,i}z_{e,i}\ge T_j\\
\text{linear equality}&A_j(x)=\sum_{e,i}a^j_{e,i}z_{e,i}=T_j.
\end{array}
\tag{ND6}
$$

The aggregate keeps the same original coordinate counts, domains, eligibility, and mandatory total. A target routine's internal band masks do not become new original eligibility rules: canonical reconstruction may use another band of the same allowed original coordinate, and ND6 remains the validity guarantee.

For the scalar, repacking gives

$$
W(x)\le\sum_{e,i}w_{e,i}z_{e,i}
\quad\text{in the minimization case},
\qquad
W(x)\ge\sum_{e,i}w_{e,i}z_{e,i}
\quad\text{in the maximization case}.
\tag{ND7}
$$

Canonical lifting of an original count vector gives equality in every original function, including the scalar.

## 4. Exact equality of the nonlinear and linear optima

For minimization, every feasible original vector canonically lifts to a feasible band vector with the same scalar, so the linear band optimum is at most the original optimum. Conversely, an optimal band vector aggregates by ND6–ND7 to an original feasible vector with scalar no larger. The reverse inequality follows, and the optima are equal. The recovered original vector is an exact optimum.

For maximization the same two maps give the inequalities in the opposite directions and again exact equality. These maps also prove feasibility equivalence. They concern integer vectors; no unproved fractional-optimum equivalence is needed.

All-zero target bands and zero scalar bands are retained as necessary. A band with zero target coefficients but nonzero scalar may matter to the optimum, and a zero-valued band may be needed to attain an original mandatory total.

## 5. Measure overlap on the actual band columns

Apply the linear target preprocessing on the band instance. Delete automatic zero cover rows, mask bands exceeding an upper/equality target, remove the resulting zero target rows, and retain the original total. This is exact for integer band counts. Every original feasible vector has a feasible canonical lift, so this preprocessing loses no original witness.

On the surviving common-band coefficient columns, require

$$
\left|\{j:a^j_{e,i}>0\}\right|\le2
\quad\text{for every band }(e,i).
\tag{ND8}
$$

Define the band-row interaction graph by joining `j` and `k` when some surviving band has both marginal slopes positive. Let `m_B` be its number of distinct edges. This is the parameter in ND1.

The original function-dependency graph may be strictly denser. For example, on domain `{0,1,2}`, the concave covering function `A(x)=min(x,1)` and the convex upper function `B(x)=max(0,x-1)` both depend on the same original coordinate. Their common marginal columns are `(1,0)` and `(0,1)`, so they do not interact in the band graph.

A stronger example uses two copies of the first covering function and two copies of the second upper function. One original coordinate then affects four rows, while each of its two bands has support two. The original dependency graph would be a four-vertex clique; the band graph has only two disjoint edges.

If original coordinate dependency support is already at most two, it does imply ND8 and its graph edge count safely upper-bounds `m_B`. Without such an implication, original dependency data alone are not a substitute for checking the refined band columns.

## 6. Applying the density algorithm

The band model has one global integral resource polymatroid `G`, explicit nonnegative integer target coefficients, binary counts, and one arbitrary rational scalar. It therefore satisfies every input condition of the linear overlap-density theorem.

For the positive targets define `U_j=T_j` for upper/equality rows and `U_j=2T_j-1` for cover rows, with `U=sum_j U_j`. At most four local shared copies per band mark its positive covering rows. No interaction edge is added by this marking. If `Q_B` is the resulting number of distinct nonempty support patterns, then

$$
T\le U\le2T,
\qquad Q_B\le d'+m_B\le T+m_B.
\tag{ND9}
$$

The exact profile bound is

$$
2^U\binom{Q_B+U}{U}\operatorname{poly}(H).
\tag{ND10}
$$

One global zero-vector remainder retains all original mandatory mass. Each profile is solved by the shared resource/partition-count integral intersection; the copied scalar is the original linear marginal scalar. Taking the exact best profile and reconstructing the original aggregate is optimal by Section 4.

RD's binomial estimate gives ND1. All-input traversal, including failed filters and infeasible resource faces, has the same bound. The number of common bands and the copied ground are polynomial in the explicit description, and all interval lengths, target counts, and rank registers remain binary. This proves the stated polynomial workspace.

If every band has support at most one, the sharper bound

$$
\exp\!\left(3\sum_j\sqrt{U_j}\right)\operatorname{poly}(H)
\le e^{3T}\operatorname{poly}(H)
\tag{ND11}
$$

follows from the support-one theorem. For any fixed band-support bound `s`, the more general pattern count ND10 still applies with the actual support-pattern count after at most `2^s` local copies; the polynomial-space guarantee for that implementation is then for fixed `s`.

## 7. Sharpness and boundaries

Linear functions are permitted by every required convexity or concavity condition. Unit domains on ordinary matroids give the linear density lower families as special cases. Thus the unconditional rank-oracle lower bounds, and the conditional rank-program/circuit ETH density bounds when that representation is used, transfer directly to this nonlinear class. This is a subclass argument, not a new hardness claim for a special nonlinear representation.

Nonlinear equality rows are not covered. Prefix repacking may change such a row's value in a direction that destroys equality. For instance, on one coordinate of domain two, `A(x)=min(x,1)` has slopes `(1,0)`. A band vector using one unit only in the second band has linearized `A` value zero but aggregate count one with true value one. Adding the legitimate linear count equality `x=1` shows that this is a real feasibility mismatch, not merely a change in an unconstrained objective.

All nonlinear rows must use the same original ordering of units on each coordinate. Their marginal bands may have different breakpoints, which common refinement resolves, but there is no permission to reorder one function's units independently of another's. The target marginal slopes are nonnegative integers; arbitrary signed target cancellations are not included.

Only one exact scalar optimization is asserted. Its shape must match minimization or maximization as above, although its marginal signs may be arbitrary. The global resource remains one integral polymatroid. Original hard domains and full-base totals remain part of every feasibility check.

The complete proof uses the already reviewed band rank and prefix identity from [compressed-nonlinear-marginal-band-transfers.md](compressed-nonlinear-marginal-band-transfers.md), together with the direct exact-profile density count. No change to the frozen earlier files is required.
