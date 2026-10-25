# Independent audit: count-box pricing and the weak residual-configuration solver

**25 October 2026. Independent mathematical review, with an explicit interior-ball completion of the finite-column extraction argument.**

This note audits `residual_configuration_box_pricing_and_weak_solver.md`, equations W1--W13. The pricing reduction, strict rational cost test, uniform Farkas bound, extraction, and target search are valid for coordinate-box local configurations. The proof below replaces the potentially delicate invocation of exact lower-dimensional oracle LP with an elementary consequence of the special row signs in this relaxation. No full-dimensionality assumption is imposed on an arbitrary input polyhedron.

The resulting statement is a fractional weak optimizer in

\[
                 2^{O(q)}\operatorname{poly}(H,\epsilon^{-1}),
\]

where q is the number of potential players. It does not give an integer approximation scheme, a rank-r fixed-parameter optimizer, or pricing for arbitrary local downward-closed families.

## 1. The explicit rows and column signs

There are L=O((t+1)2^q) explicit rows: all resource subset-marginal cuts, all player-matroid subset upper bounds, and the single lower-total-mass row. Nonnegativity of configuration variables is separate. The resource-cut coefficients are nonnegative integers. Player-upper coefficients belong to {0,1}. The lower-total row has coefficient -1 on every configuration column and right side -r. In particular, the player upper bound for the whole ground set has coefficient 1 on every column and right side r.

All coefficients and right sides have absolute value at most an integer B>=1 with polynomial encoding length in the original input. Values and the target select allowed columns but do not occur in their constraint coefficients. Enumerating the rows and their rank values costs singly exponential time in q. Aggregate resource inequalities follow from the subset cuts: for a player in S the marginal at S is zero, so its entire expected count is included in the cut for S.

The rank-zero case is vacuous and should be handled separately. Below r>0, and hence q>=1. Accuracy may be restricted to 0<epsilon<=1/2; for a larger requested epsilon use 1/2 instead.

## 2. Convex-cost pricing is valid without expanding capacities

For fixed nonnegative row prices, a player's resource cost is a sum of separable nonnegative convex hinges with integer breakpoints. Constant marginal-cost segments have binary capacities. Ignoring the order of segments for a single type preserves the optimum under a cost budget: compress any chosen units to the cheapest prefix of that type, preserving their count and value and weakly decreasing cost. Conversely, any legal count vector is available in the segment relaxation.

Binary chunking represents every count in each segment and uses only logarithmically many chunks per segment. Selecting free positive-value chunks and deleting unaffordable positive-cost chunks are safe. On the remaining ordinary zero-one knapsack, profit scaling with Delta=epsilon Pmax/N gives an exact-budget solution with at least (1-epsilon) of the optimum value. Each remaining positive-value chunk individually fits, so Pmax is a valid lower bound on the remaining optimum. Exact rational minimum-cost dynamic programming uses polynomially bounded bit lengths. Compressing the output to prefixes returns a genuine count vector within the box and within the original budget.

The denominator argument also checks. If every integer configuration cost belongs to D^{-1}Z, then

\[
                    C=(\lceil Dw\rceil-1)/D
\]

is the largest grid budget strictly less than w. For w>0 this is nonnegative. A target-T violating configuration would therefore be feasible for this budget and would force the approximate maximum value to be at least (1-epsilon)T. Consequently the oracle either returns a genuinely violating column at the weaker target or certifies that there is no violating hard-target column. Equality of cost and w is correctly excluded. There is no accumulation of approximation factors over the oracle calls.

## 3. A uniform bounded Farkas witness

For any finite subset C of configuration columns, consider

\[
                    A_C\mu\le b,\qquad \mu\ge0.
\]

If this primal is infeasible, Farkas' lemma supplies

\[
       \beta_0\ge0,\qquad
       \beta_0^T A_C\ge0,\qquad \beta_0^T b=-1.
\]

A basic witness has all its coordinates at most

\[
                    U_0=(LB+1)^{L+1}.
                    \tag{A1}
\]

Indeed, the normalized certificate polyhedron is pointed because it is contained in the nonnegative orthant, so a nonempty one has a vertex. At a vertex, L independent active equations have integral coefficients bounded by B and right sides zero or -1. Cramer's rule and an integer nonzero determinant give (A1). The stated bound is deliberately loose. It applies to every subset C and every target, since neither L nor B changes. Its bit length is O(L(log L+log B)).

## 4. An explicit interior ball from the special row signs

Let theta be the L-dimensional vector whose coordinates are all 1, except that the coordinate for the player upper-total row is 2. Then every configuration column a satisfies

\[
                  \theta^T a\ge1,
       \qquad \theta^T b\le(L+1)B.
                  \tag{A2}
\]

For the first inequality, all resource contributions are nonnegative; the player upper-total row contributes 2, the lower-total row contributes -1, and the other player upper rows are nonnegative.

Set

\[
       \gamma=\frac1{4(L+1)B},\qquad
       \delta=\frac{\gamma}{2LB},\qquad
       U=4U_0.
                  \tag{A3}
\]

For any infeasible finite primal, choose beta_0 as above and put

\[
                        \beta_* = 2\beta_0+\gamma\theta.
                  \tag{A4}
\]

This point satisfies all the following quantitative inequalities:

\[
\begin{split}
  \beta_{*,i}&\ge\gamma,\\
  U-\beta_{*,i}&\ge U_0,\\
  \beta_*^T a&\ge\gamma \quad(a\in C),\\
  \beta_*^T b&\le-7/4.
\end{split}
                  \tag{A5}
\]

Each column normal and b have Euclidean norm at most B sqrt(L). A displacement of Euclidean norm at most delta changes their scalar products by at most gamma/2. It changes an individual coordinate by at most delta<=gamma/2. Therefore the entire closed Euclidean ball B(beta_*,delta) lies in

\[
 Q_C=\{\beta:0\le\beta\le U,\quad
             \beta^Tb\le-1,\quad
             \beta^Ta\ge0\ (a\in C)\}.
                  \tag{A6}
\]

This proves the precise property needed for extraction: **whenever the finite-column primal is infeasible, its bounded Farkas region contains a known-radius ball**. The argument remains valid when C is empty. It is independent of how C was generated and independent of its cardinality. The logarithm of delta^{-1} is O(log L+log B).

The same implication holds for the full finite, implicitly represented family of columns. Thus the relevant Farkas regions are either empty or contain such a ball; this fact is proved from the row structure, not assumed.

## 5. Ordinary ellipsoid volume exhaustion suffices

Search the weak-target Farkas region in the larger box [0,U]^L using a standard rational ellipsoid feasibility procedure. An initial ball of radius R=4LU_0 about the origin contains this box. Use explicit box and normalization inequalities whenever violated. At a remaining query point, apply the pricing oracle to every player.

If any player returns a violated weak-target column, use that exact original inequality as a cut and record the column. If all players certify the absence of a violated hard-target column, the current beta is a valid normalized hard-target Farkas witness; stop and report hard-target infeasibility. This is a valid early stopping rule even if beta has not been shown feasible for the weak-target system.

If this early stopping event does not happen, every continuation cut is an actual defining inequality of the weak-target system. Standard ellipsoid volume reduction, with rational rounding to polynomial precision, needs only polynomially many iterations in L and log(R/delta) to reach volume smaller than that of a radius-delta ball. Here

\[
            \log(R/\delta)=O\bigl(L(\log L+\log B)\bigr).
                  \tag{A7}
\]

Let C be the weak-target columns returned before volume exhaustion. Include all explicit box and normalization inequalities, whether or not they were queried. Their intersection with these retained column inequalities is contained in the final ellipsoid: the initial ball contains the box, and every ellipsoid update preserves the corresponding cut intersection.

If the finite primal on C were infeasible, Section 4 would put a radius-delta ball inside that same intersection. Its volume would exceed the volume of the final ellipsoid, a contradiction. Hence the finite primal on C is feasible. An ordinary explicit rational LP computation returns its configuration weights. Its L rows are all the original enumerated rows, so the resulting point satisfies the full weak-target relaxation, not merely the cuts encountered by the ellipsoid. Its support has at most the polynomial number of generated columns.

This argument does not infer primal feasibility from the mere failure to find a hard column. It uses the uniform witness bound and the derived interior ball for every retained-column subsystem. It also avoids the invalid inference that a very small volume by itself certifies emptiness of an arbitrary lower-dimensional polyhedron.

## 6. Bit complexity and optimization direction

All constants in (A1)--(A7) have polynomial bit length in L and log B. Standard rational ellipsoid implementation keeps query prices of polynomial encoding length in those parameters. The common cost denominator, hinge segment list, binary chunks, dynamic program, and the final explicit LP are therefore polynomial in L, H, and epsilon^{-1}. Since L is singly exponential in q, so is the complete weak solver.

The final target search has the correct orientation. A hard-target infeasibility outcome at T proves T>OPT_LP. A successful weak point at trial T need not make the hard target feasible. Maintain a successful lower trial and a failed upper trial, search on the common rational value grid, and stop when they are adjacent. The failed upper trial is strictly above OPT_LP; because the optimum is a grid point, the adjacent lower trial is at least OPT_LP. Its saved point consequently has value at least (1-epsilon)OPT_LP. Monotonicity of the algorithm's success choices is unnecessary.

For positive rank, OPT_LP<=sum_j v_j f_j(P), by total expected-value accounting. Thus an upper trial beyond this bound divided by (1-epsilon) cannot return a weak feasible point. The zero trial has an empty-configuration basis point. The number of grid bisections is polynomial in the encoded range. Zero values and zero optimum cause no difficulty.

## 7. Review conclusion and classical background

With the explicit box enlargement and interior-ball argument above, W1--W13 form a complete mathematical derivation for the stated count-box model. The original note may alternatively use a certifying exact rational-polyhedron algorithm, but that stronger primitive is unnecessary here.

The ordinary rational ellipsoid and knapsack approximation primitives are classical. A primary reference for the former is Groetschel, Lovasz and Schrijver, [*The ellipsoid method and its consequences in combinatorial optimization*, Combinatorica 1 (1981)](https://ir.cwi.nl/pub/10046/10046D.pdf). For an explicit modern exact oracle-LP theorem covering arbitrary dimension and returning a Farkas certificate, see Dadush, Vegh and Zambelli, [*On finding exact solutions of linear programs in the oracle model*, Theorem 1.3(i) and Remark 1.6](https://arxiv.org/html/2606.11820v1). The latter is an alternative background justification, not a prerequisite for the special-row proof above.

The contribution reviewed here is the particular strengthened-relaxation pricing, strict-grid weak oracle, and extraction argument. No independent implementation, formal verification, external peer review, or exhaustive publication-priority claim is made.
