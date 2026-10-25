# Additive corank allocation with an exact assignment-cost budget

**25 October 2026. Separate extension manuscript; root and independent audits requested.**

This note adds one hard linear cost budget to
`unrelated_values_corank_additive_allocation.md`. Values may depend
arbitrarily on both player and resource type. Counts remain governed
by arbitrary integral recipient polymatroids, and selected players
form an actual basis of a given matroid. The budget is on the
player-resource assignments themselves, not merely on choosing players.

The same two additive guarantees hold, with the budget preserved
exactly: `(1-epsilon) OPT_C-u` in `Gamma(1/epsilon)^c poly(H)` time,
and `(1-epsilon) FOPT_C-u` in `Gamma(2/epsilon)^c poly(H)` time.
Only one assignment-cost budget is claimed. The proof does not
infer a multiplicative approximation when the largest-unit loss
is large.

## 1. Model and theorem

Use the player matroid, nonnegative values v_pj and integral recipient
ranks f_j from the unrelated-value manuscript. Let the selected rank
be r>0 and the loop-deleted player ground have size q, with c=q-r.
For each possible assignment prescribe a nonnegative rational cost
c_pj and a nonnegative rational budget C. The additional requirement
on the integer count vectors is

\[
                             \sum_{p,j}c_{pj}n_j(p)\le C.
 \tag{B1}
\]

Unused resource units are allowed. Let OPT_C be the integer max-min
optimum under (B1), and define FOPT_C by choosing one genuine allowed
player basis and fractionally allocating the resources under the
same budget. Again, this comparator does not mix player bases.

After original player-loop deletion and the zero-budget coordinate
preprocessing of Section 7 when C=0, define precisely

    u_p = max{v_pj : f_j({p})>=1},    u = max_p u_p,

with empty maxima zero. Set v_pj to zero on newly zero-singleton
coordinates before constructing the local value orders: those
coordinates are identically zero in both the primal and complement
rounding vectors, so this changes no utility. Only zero caps preserving
the fractional feasible region are used for this definition. In particular, when
C>0, a coordinate with c_pj>C must not be discarded merely because
one whole unit is unaffordable: a fractional unit can still be
feasible and can affect FOPT_C. Deleting such coordinates would
change the stated fractional comparator. Fix rational `0<epsilon<1`.

**Theorem B.** Deterministic algorithms return a genuine selected basis
I and an integer allocation satisfying (B1) exactly. Their per-selected-
player utility guarantees and running times are respectively

\[
 \begin{array}{c|c}
 \text{utility at }p\in I&\text{running time}\\ \hline
 \max\{0,(1-\epsilon)\mathrm{OPT}_C-u_p\}
     &\Gamma(1/\epsilon)^c\operatorname{poly}(H)\\
 \max\{0,(1-\epsilon)\operatorname{FOPT}_C-u_p\}
     &\Gamma(2/\epsilon)^c\operatorname{poly}(H).
 \end{array}
 \tag{B2}
\]

Both use polynomial workspace. H additionally includes all assignment
cost and budget encodings. The polynomial degree is independent of c
and epsilon. The theorem also allows any fixed-cardinality restriction
selection oracle from the unrelated-value manuscript, including two
exact common-basis matroids and a separate player-selection cost bound.

Nonnegative assignment costs matter when counts outside the selected
set are discarded. Multiple independent assignment budgets are outside
the theorem: optimizing one rounding objective does not preserve
several unrelated cost inequalities simultaneously.

## 2. The budgeted fractional utility region

Define the compact, nonempty fractional allocation polytope

\[
 \mathcal X_C=\left\{(x_j)_j:
            x_j\in P(f_j),\quad\sum_{p,j}c_{pj}x_j(p)\le C\right\}.
 \tag{B3}
\]

Zero counts are feasible. Its lower utility projection is

\[
 \mathcal U_C=\left\{z\ge0:
       \exists x\in\mathcal X_C,\quad
       z_p\le\sum_jv_{pj}x_j(p)\text{ for every }p\right\}.
 \tag{B4}
\]

This is a compact convex downward region. It remains fixed during
all omission branches. For a>=0 its exact support is

\[
          h_C(a)=\max_{x\in\mathcal X_C}
                              \sum_{p,j}a_pv_{pj}x_j(p).
 \tag{B5}
\]

Unlike the unbudgeted case, this maximum need not decompose by type.
It is nevertheless a polynomial-size-variable rational LP. The
resource inequalities have exact separation through submodular
minimization, and the cost constraint is explicit. Therefore exact
support optimization is polynomial oracle work.

Every vertex of X_C has polynomial binary length. To see this
uniformly, its dimension is q times the number of types; its resource
inequalities have zero-one coefficients and encoded integer right
hand sides, while its one budget row has encoded rational coefficients.
A vertex is determined by an independent set of at most that many
tight rows. Cramer's determinant bound gives a polynomial encoding
bound independent of the exponential number of possible resource
subsets. An extreme optimal support solution can be selected by
ordinary lexicographic LP refinement.

## 3. A concrete nonnegative packing separator

Let `V=sum_(p,j) v_pj f_j({p})`, an encoded upper bound on every
possible total utility. For z>=0 solve the support LP

\[
 \begin{array}{ll}
 \text{maximize}&a\cdot z-t,\\
 \text{subject to}&a\ge0,\quad a(P)=1,\quad0\le t\le V,\\
                 &t\ge\sum_{p,j}a_pv_{pj}x_j(p)
                         \quad\text{for every vertex }x\in\mathcal X_C.
 \end{array}
 \tag{B6}
\]

At a candidate a,t, compute (B5) by the inner LP. If h_C(a)>t,
an attaining vertex supplies a violated linear inequality of (B6).
All its coefficients have polynomial binary length by Section 2.
Thus the outer LP has polynomial dimension and exact polynomial
separation. Nested polynomial LP-oracle computations remain polynomial
in the original bit encoding; no numerical capacity enumeration is
introduced.

If the exact optimum is positive, recompute the support and return

\[
                               a\cdot z'\le h_C(a),\qquad a\ge0.
 \tag{B7}
\]

This is a valid nonnegative-capacity packing row for U_C, strictly
violated by the proposed z. If the optimum is nonpositive, z lies
in U_C. The latter follows from the downward-polytope separation
argument in the unrelated-value note: any signed separator can be
replaced by its positive part without changing its support, and
then normalized. The argument does not require full dimension.

Given a feasible `b 1_I`, reconstruct x in X_C with utility at least
b on I by the corresponding direct fractional feasibility LP.
All variables, resource separators and the budget row are explicit
at polynomial dimension. There is no unsupported inference from a
utility membership answer to an allocation witness.

## 4. Free disposal makes base completion cost-neutral

Completing an independent fractional allocation to an original resource
base could increase its cost. We avoid that operation by adding one
auxiliary disposal coordinate, denoted by bottom, for every resource.
It is not a candidate player and does not change q, r or c.

On `Pbar=P union {bottom}`, extend each resource rank to

\[
 \overline f_j(S)=
 \begin{cases}
 f_j(S),&\text{if bottom is not in }S,\\
 f_j(P),&\text{if bottom is in }S.
 \end{cases}
 \tag{B8}
\]

This is normalized, monotone, integral and submodular. The only
mixed submodularity case has one set containing bottom; its inequality
reduces to monotonicity of f_j on the other set and the intersection.
The cases with neither or both sets containing bottom are immediate.

For any x_j in P(f_j), the vector

\[
       \overline x_j(p)=x_j(p)\ (p\in P),
       \qquad
       \overline x_j(\mathrm{bottom})=f_j(P)-x_j(P)
 \tag{B9}
\]

is a base of the extended rank. Subsets without bottom use the
original inequalities; subsets with bottom have total at most the
full base total f_j(P). Conversely, restricting an extended base
to P gives an original independent vector.

Give every disposal assignment value and cost zero. Equation (B9)
then turns the fractional budget witness into full resource bases
without changing any real-player utility or the total cost. Numerical
supplies still occupy binary counters; there are only q+1 resource
ground elements per type.

## 5. One weighted intersection preserves the cost exactly

Apply the per-player complement and prefix construction to the extended
fractional bases. In detail, let

\[
       a_j(p)=\overline f_j(\{p\}),\qquad
       y_j=a_j-\overline x_j,
 \tag{B10}
\]

so y_j is a base of the complement rank
`fbar_j#(S)=a_j(S)+fbar_j(Pbar\S)-fbar_j(Pbar)`.
At each real player use its own decreasing order of the values v_pj
and the ceiling prefix bounds of y. At bottom all values are zero,
so any order is valid. Let A be the direct-sum dual resource rank
and R the integral sum-of-prefix-maxima rank on Pbar times the types.

The fractional y belongs to P(A) intersect P(R) and has total

\[
                          L=\sum_j\overline f_j^\#(\overline P).
 \tag{B11}
\]

This is the maximum possible total in that intersection. The
maximum-total face is integral, because integral polymatroid
intersection is integral and a maximizing face retains integrality.
Choose an integer vector y' on this face maximizing the linear
objective

\[
                                  \sum_{p,j}c_{pj}y'_j(p),
 \tag{B12}
\]

where disposal costs are zero. Weighted polymatroid intersection,
or exact LP optimization over this integral face followed by vertex
selection, implements this in polynomial oracle time. The total L
is required first; maximizing cost over arbitrary smaller independent
vectors would not establish the needed base complement.

Since the original fractional y is feasible on the same face,

\[
                         \sum_{p,j}c_{pj}y'_j(p)
                              \ge\sum_{p,j}c_{pj}y_j(p).
 \tag{B13}
\]

Each component of y' is a full dual resource base. Complementing
back gives integral extended bases `x'_j=a_j-y'_j`, and

\[
 \sum_{p,j}c_{pj}x'_j(p)
     =\sum_{p,j}c_{pj}a_j(p)-\sum_{p,j}c_{pj}y'_j(p)
     \le\sum_{p,j}c_{pj}\overline x_j(p)\le C.
 \tag{B14}
\]

At every real player the same prefix telescoping as in the unrelated-
value manuscript gives

\[
                    \sum_jv_{pj}x'_j(p)
                         \ge\sum_jv_{pj}x_j(p)-u_p.
 \tag{B15}
\]

The choice of a cost-optimal point on the integral intersection
does not affect these prefix inequalities. Discard bottom and all
counts outside the selected set I. The former operation is free
disposal; the latter cannot increase cost because all costs are
nonnegative. Selected utilities are unchanged, and all original
resource vectors remain independent. This proves a cost-preserving
per-player largest-unit lower-rounding lemma for the present model.

## 6. The quota gap and integer-optimum optimization

Apply the weighted prefix-free omission theorem to the fixed utility
region U_C and the original player restriction selector. For any
rational T>0, use t=T and b=(1-epsilon)T. A full fractional target
on one genuine basis supplies the stronger promise. The algorithm
returns a b-service basis or soundly rules out that full target,
in `Gamma(1/epsilon)^c poly(H)` time.

Choose the common original value grid g. OPT_C lies on it even
though the assignment costs and budget need not lie on the same
grid: every integral utility is still a sum of integer counts times
the original values. The external upper target V+g is infeasible,
and zero is a legal saved lower target with any allowed basis.
The one-sided maximization search from the unrelated-value note
therefore finds a saved lower target at least OPT_C.

Reconstruct its fractional budget witness and use Sections 4--5.
The resulting integer allocation proves the first line of (B2).
All target failures are fractional service infeasibility statements,
so they are also sound for the integer optimum. Successes need not
be exact target feasibility certificates or monotone.

## 7. Zero budget, positive fractional scale and relative search

The fractional-comparator search needs a positive lower bound when
FOPT_C is nonzero. If C=0, every coordinate with c_pj>0 must be zero
in any feasible allocation. Enforce these zero coordinate caps in
the corresponding resource rank. Equivalently, if Z_j is the set of
players with c_pj=0, replace f_j(S) by f_j(S intersect Z_j), which
extends its restriction to Z_j by loops. This exactly represents the
original zero-budget independent allocations. The remaining usable
coordinates have zero cost, so the unbudgeted positive lower scale
applies to the capped ranks.

For C>0, let P+ be the players with at least one positive-valued
eligible coordinate. If the selection family has no member in P+,
then FOPT_C=0 and the claim is trivial. Otherwise choose such a
genuine r-set. Let v_min be the smallest positive eligible value,
and let C_max be the largest assignment cost. Define

\[
 \alpha=\begin{cases}
 1,&C_{\max}=0,\\
 \min\{1,C/C_{\max}\},&C_{\max}>0,
 \end{cases}
          \qquad \lambda_C={\alpha v_{\min}\over r}>0.
 \tag{B16}
\]

Give one eligible unit in turn to each member of the chosen set and
average these r feasible resource allocations. Its total cost is
at most C_max and every selected player receives at least v_min/r.
Scale every count by alpha. Resource feasibility is preserved and
the cost is at most C, so FOPT_C>=lambda_C. This constructs the
initial saved fractional basis explicitly.

For C=0 after the zero-cost preprocessing, use the same formula with
alpha=1. If the remaining positive eligible set contains no allowed
basis, FOPT_C=0. No division by zero or positive-lower-scale claim
is used in that case.

Now run the service gap with loss epsilon/2, a successful lower
endpoint lambda_C, and an external upper endpoint V+lambda_C.
Stop when their distance is at most epsilon lambda_C/2. Exactly
as before, the saved lower target L satisfies

\[
        L\ge(1-\epsilon/2)\operatorname{FOPT}_C,
       \qquad
        (1-\epsilon/2)L\ge(1-\epsilon)\operatorname{FOPT}_C.
 \tag{B17}
\]

Reconstruction followed by budget-preserving rounding proves the
second line of (B2). The number of trials is polynomial in
`log(1+V/(epsilon lambda_C))`. All factors in (B16) have polynomial
binary length; a very small budget or a large assignment cost does
not cause a numerical-unit loop.

## 8. Complexity and scope of the budget transfer

The support and reconstruction LPs have polynomially many variables
and exact polynomial resource separators. The outer support LP has
polynomial-bit inequalities supplied by inner extreme optimizers.
The weighted prefix-free recursion only uses the fixed utility
region's nonnegative packing rows and exact player restriction
selection. Its corank and entropy accounting are unchanged.

The disposal extension adds one resource-ground coordinate but no
candidate player. The cost-optimal rounding intersection uses only
(q+1) times the number of types coordinates. Counts, costs, prefix
ceilings and all totals are binary encoded. All nested polynomial
primitives and the depth-first omission search use polynomial
workspace. These facts justify both runtime statements in (B2).

A separate bound on the sum of selected-player costs can coexist
with (B1), provided it is part of a polynomial restriction selector.
It constrains the selected set, while (B1) constrains resource
assignment counts. This does not imply that two unrelated assignment
budgets can both be preserved by the same rounding operation.

If u<=epsilon OPT_C, the integer-comparator result gives
`(1-2epsilon)OPT_C` without violating the budget. Without such a
small-unit condition the additive loss may absorb the entire
comparator. No unconditional constant factor for the general
Budgeted Santa Claus problem follows from the additive statement.

## 9. Primary public comparison

Rohwedder, Rouhani and Wennmann,
[*Cost Preserving Dependent Rounding for Allocation Problems*,
ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127), Section 1
and Lemma 10, explicitly record the classical largest-unit additive
allocation rounding without increasing assignment cost, including
its unrelated-value interpretation. Their Theorem 3 gives a
randomized polynomial `O(log n)` multiplicative guarantee for the
ordinary-item Budgeted Santa Claus model with intrinsic values.
These are different statements from the parameterized additive
result proved here; the ordinary cost-preserving rounding is not
claimed new or superseded.

The contribution of this transfer is the optional selected-basis
search in corank time, the explicit budgeted fractional support
oracle, and its composition with a binary-capacity recipient-
polymatroid rounding implementation. The fractional comparator
selects one actual basis, and the assignment budget is satisfied
exactly. No exhaustive priority claim is made for the combined
parameterized theorem or its rounding sublemma.

The manuscript is submitted for root and independent internal
review, without a claim of formal verification or external peer
review.
