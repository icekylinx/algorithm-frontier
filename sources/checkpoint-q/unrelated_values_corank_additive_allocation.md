# Corank additive allocation with player-dependent values

**25 October 2026. New research manuscript; root and independent audits requested.**

The weighted prefix-free omission algorithm removes the common-intrinsic-
value restriction from the additive allocation theorem. Resources may
have an arbitrary nonnegative rational value at each player. Resource
feasibility remains an independent integral recipient polymatroid for
each type. The selected players form a genuine matroid basis.

Two guarantees are proved. Against the integer optimum, the running
time is `Gamma(1/epsilon)^c poly(H)` and the value is at least
`(1-epsilon) OPT-u`. Against the stronger optimum obtained by choosing
one genuine basis and allocating resources fractionally to it, the
time is `Gamma(2/epsilon)^c poly(H)` with the same additive expression.
Neither comparator fractionally mixes selected player bases.

## 1. Model, comparators and theorem

Let M be a player matroid of positive rank r on P. Resource type j
has a normalized monotone integral submodular rank f_j on P, and a
nonnegative rational value v_pj at player p. An integer allocation
uses a count vector n_j in P(f_j) for every type. Unused resources
are permitted. Its objective on a selected M-basis I is

\[
                      \min_{p\in I}\sum_jv_{pj}n_j(p).
 \tag{U1}
\]

There are no additional constraints coupling different resource types.
Per-type coordinate caps may already be included in their ranks.
Delete player-matroid loops and restrict the resource ranks to the
remaining ground. Rename it P, put q=|P|, and let c=q-r. This preserves
the optimum, because all original bases avoid those loops and the
resource constraints are downward closed.

Set v_pj to zero when f_j({p})=0; such a coordinate can never receive
that resource. This does not change any attainable utility. Define

\[
                            u_p=\max_j v_{pj},
                         \qquad u=\max_pu_p,
 \tag{U2}
\]

with empty maxima equal to zero. Let OPT be the integer optimum, and
let

\[
 \operatorname{FOPT}
   =\max_{I\text{ an M-basis}}
      \max_{x_j\in P(f_j)}\ \min_{p\in I}\sum_jv_{pj}x_j(p).
 \tag{U3}
\]

The inner allocations are fractional, but the basis I in (U3) is
an actual integral set. This is not a relaxation that replaces the
basis by a fractional point of the player base polytope. Clearly
FOPT>=OPT. Both are finite and attained, since there are finitely many
bases and each resource polytope is compact.

Fix rational `0<epsilon<1`, and write
`Gamma(R)=R^R/(R-1)^(R-1)<=eR` for R>1.

**Theorem U.** A deterministic algorithm returns an M-basis I and
integer resource counts such that every selected player has utility
at least

\[
                  \max\{0,(1-\epsilon)\mathrm{OPT}-u_p\}
 \tag{U4}
\]

in time `Gamma(1/epsilon)^c poly(H)`. A second algorithm guarantees

\[
                  \max\{0,(1-\epsilon)\operatorname{FOPT}-u_p\}
 \tag{U5}
\]

in time `Gamma(2/epsilon)^c poly(H)`. Thus their minimum selected
utilities satisfy the corresponding inequalities with u replacing
u_p. Both use polynomial workspace. H includes the input and
accuracy bits, oracle-answer lengths and the paid polynomial
rank, submodular minimization and exact rational LP primitives.

The theorem is additive. It does not claim a constant multiplicative
approximation for unrelated values without a small-unit hypothesis.
In particular, no intrinsic-value heavy/light theorem is imported
into this model.

## 2. A fixed downward fractional utility polytope

For each type, let D_j be the diagonal matrix with entries v_pj.
Define

\[
                         \mathcal U=\sum_j D_jP(f_j).
 \tag{U6}
\]

Each summand is compact, convex, nonnegative and downward closed.
For downward closure, reduce a positive-value coordinate of its
underlying x_j and use downward closure of P(f_j); zero-valued
coordinates already have zero image. The sum is also downward
closed, since a coordinatewise decrease of a sum can be distributed
among its nonnegative summands. Thus equivalently

\[
 z\in\mathcal U
  \quad\Longleftrightarrow\quad
 \exists x_j\in P(f_j):\ z_p\le\sum_jv_{pj}x_j(p)\quad(p\in P),
                  \qquad z\ge0.
 \tag{U7}
\]

This region stays fixed during the omission recursion. A current
candidate ground Q is queried by the vector `b 1_Q`, zero outside
Q. Resource ranks are not contracted or recomputed after candidate
players are deleted.

For a nonnegative weight vector a, the support function is

\[
 h(a)=\max_{z\in\mathcal U}a\cdot z
      =\sum_j h_j(a),\qquad
 h_j(a)=\max_{x\in P(f_j)}\sum_p a_pv_{pj}x_p.
 \tag{U8}
\]

Every h_j(a), and an attaining integer vector, is obtained by ordinary
polymatroid greedy optimization with weights a_pv_pj. Nonnegativity
permits an attaining resource base. Thus all support maximizers and
their values have polynomial binary length, with no unit expansion.

## 3. Exact nonnegative separation through a small-dimensional LP

The weighted omission theorem requires an explicit nonnegative
packing row when `b 1_Q` is infeasible. A generic signed separating
hyperplane is insufficient unless this sign issue is resolved.
Here it is resolved directly.

Let

\[
                         V_j=\sum_pv_{pj}f_j(\{p\}),
                        \qquad V=\sum_jV_j.
 \tag{U9}
\]

For a proposed z>=0, solve the following rational LP in q plus the
number of resource types variables:

\[
 \begin{array}{ll}
 \text{maximize}&a\cdot z-\sum_j t_j,\\
 \text{subject to}&a\ge0,\quad\sum_pa_p=1,\\
                 &0\le t_j\le V_j,\\
                 &t_j\ge\sum_pa_pv_{pj}x_p
                    \quad\text{for every base vertex }x\in B(f_j).
 \end{array}
 \tag{U10}
\]

The exponentially many last constraints have polynomial-time exact
separation: greedily compute h_j(a); if it exceeds t_j, return the
inequality from the attaining base vertex. Other constraints are
explicit. A base vertex has integral coordinates bounded by the
encoded ranks, so every possible inequality has polynomial-bit
coefficients. The dimension and all bounds are polynomial. Standard
exact rational LP with strong separation therefore returns an exact
optimum and a polynomial-bit optimizer. It does not enumerate the
base vertices.

The upper t_j bounds are valid because a lies in the simplex and
every independent x has x_p<=f_j({p}). The LP is always feasible:
any such a with t_j=V_j satisfies it. At its optimum, each t_j may
be reduced to h_j(a), so its value is

\[
                \max_{a\ge0,\,a(P)=1}\{a\cdot z-h(a)\}.
 \tag{U11}
\]

If the value is positive, recompute all h_j(a) exactly. The returned
row is

\[
                              a\cdot y\le h(a),\qquad a\ge0.
 \tag{U12}
\]

It is valid for every y in the fixed region and strictly violated
by z. Its capacity h(a) is nonnegative and of polynomial binary
length. In particular, for z=b 1_Q it has precisely the form needed
by weighted prefix branching.

If (U11) is nonpositive, then z belongs to the region. To verify
this equivalence, suppose z>=0 is outside the compact convex region.
Strong separation gives a signed normal a with a·z>h(a). Downward
closure implies `h(a)=h(a_+)`: negative-weight coordinates can be
set to zero without sacrificing positive coordinates. Since z>=0,
`a_+·z>=a·z`, and a_+ is nonzero. Normalize a_+ to sum one to
obtain a positive objective in (U11), a contradiction. This argument
also handles zero-utility coordinates and lower-dimensional regions.

## 4. A rational service gap on genuine selected bases

Fix rational t>b>0. The stronger promise is an M-basis I* with
`t 1_(I*) in U`; the requested output is an M-basis I with
`b 1_I in U`. Use the restriction rank-and-basis oracle of M
together with the nonnegative packing separator (U10)--(U12).

The weighted prefix-free theorem in
`corank_weighted_prefix_free_batching.md` then solves this gap in

\[
             \Gamma\!\left({t\over t-b}\right)^c\operatorname{poly}(H)
 \tag{U13}
\]

time and polynomial workspace. It either returns the valid b-service
basis or certifies that no full t-service basis exists. Every queried
row is valid for the original fixed fractional utility region, even
though its coefficients and its maximizing resource bases are found
adaptively by LPs. The proof does not require a finite list of rows
to be written in advance.

In particular, at target T>0 choose `t=T`, `b=(1-beta)T` for any
rational `0<beta<1`. Then the ratio in (U13) is exactly 1/beta.
The weighted theorem accepts rational quotas, so no artificial
workload quantum or numerical rounding is needed here.

## 5. Reconstructing the selected fractional allocation

Given `b 1_I in U`, solve the primal feasibility LP

\[
       x_j\in P(f_j)\quad\text{for all }j,\qquad
       \sum_jv_{pj}x_j(p)\ge b\quad(p\in I).
 \tag{U14}
\]

It has polynomially many variables. For each type, submodular
minimization of `f_j(S)-x_j(S)` supplies an exact resource separator;
the other inequalities are explicit. Existence follows from (U7).
Standard exact rational LP returns polynomial-bit fractional counts.

Each x_j can be extended to a fractional resource base without
decreasing any coordinate. There are no costs or other cross-type
constraints in the present theorem, so this preserves every lower
utility requirement. Coordinate saturation using submodular
minimization gives a binary polynomial implementation. The next
section rounds these bases to integer bases with a per-player loss.

## 6. Lower rounding with a different type order at each player

Let x_j be arbitrary fractional bases of the resource ranks. Put
`a_j(p)=f_j({p})` and define the complement ranks

\[
       f_j^\#(S)=a_j(S)+f_j(P\setminus S)-f_j(P).
 \tag{U15}
\]

As proved in the intrinsic-value additive note, these are integral
monotone submodular ranks and `y_j=a_j-x_j` is a base of f_j#.
The affine complement map is an exact bijection of base polytopes.

For each player p independently, order the types as
`j_p(1),...,j_p(m)` so that its values are nonincreasing. Let

\[
       C_{p,k}=\left\lceil\sum_{\ell=1}^k y_{j_p(\ell)}(p)\right\rceil.
 \tag{U16}
\]

On the product ground P times J, intersect the direct sum of the
dual resource polymatroids with the integral prefix polymatroid
whose rank on a subset S is

\[
       R(S)=\sum_p\max\{C_{p,k}:(p,j_p(k))\in S\},
 \tag{U17}
\]

where an empty maximum is zero. This is a sum of submodular
max-weight ranks. The nondecreasing C_p,k make its rank inequalities
equivalent to all the required prefix upper bounds. The permutations
j_p may differ arbitrarily between players; they do not change the
separate direct-sum resource rank.

The starting fractional y lies in the intersection. Integral
polymatroid intersection supplies an integer vector y' of the same
maximum total rank, forcing every resource component to be a dual
base. At each player, telescoping its own decreasing sequence of
values gives

\[
                  \sum_jv_{pj}y'_j(p)
                         \le\sum_jv_{pj}y_j(p)+u_p.
 \tag{U18}
\]

Complement back to `x'_j=a_j-y'_j`. These are nonnegative integer
original-resource bases, and

\[
                  \sum_jv_{pj}x'_j(p)
                         \ge\sum_jv_{pj}x_j(p)-u_p.
 \tag{U19}
\]

Thus a fractional b-service basis becomes an integer allocation
with utility at least b-u_p at each selected player. Discard all
counts outside I; selected utilities stay unchanged and resource
feasibility is preserved. The product ground has only q times m
elements, and all complement ranks and prefix ceilings remain
binary encoded. No number of resource units is expanded.

## 7. Integer-optimum search with the sharper runtime base

Choose a positive rational grid g dividing every v_pj. All integer
player utilities and OPT are multiples of g. The value V from (U9)
is such a multiple and is an upper bound on any selected player's
utility, since every resource coordinate is bounded by its singleton
rank. Therefore V+g is a sound external infeasible upper target.

Use beta=epsilon in Section 4, start with successful target zero
and an arbitrary M-basis with zero counts, and perform one-sided
maximization on the g-grid. A service-gap failure excludes the
fractional target and hence also the original integer target. A
success saves its actual fractional b-service basis and raises the
lower endpoint. There is no assumption that successes are exact
feasibility certificates or monotone.

At adjacent endpoints the lower target is at least OPT, because
the upper endpoint remains strictly above OPT and OPT lies on the
grid. Reconstruct and round the saved successful basis once. Its
utility satisfies (U4). If the saved target is zero, zero counts
already satisfy the claimed lower bound whenever this case occurs.

There are polynomially many target trials in log(V/g+1). Each has
ratio 1/epsilon in (U13). This proves the first runtime in Theorem U.

## 8. A positive lower scale for the selected-basis fractional optimum

The stronger FOPT need not lie on the original utility grid. We avoid
assuming that it does by constructing a polynomial-bit positive lower
bound when it is nonzero.

Let

\[
             P^+=\{p:\exists j,\ v_{pj}>0,\ f_j(\{p\})\ge1\}.
 \tag{U20}
\]

If M restricted to P+ has rank less than r, every original basis
contains a player of zero attainable utility. Thus FOPT=OPT=0,
and any legal basis allocation suffices. If the rank remains r,
restrict candidate players to P+; the positive fractional optimum
is preserved. This may further reduce the corank to |P+|-r, and
the stated c remains a valid upper parameter.

Let v_min be the smallest positive value on an eligible pair in
(U20), and set

\[
                                  \lambda=v_{\min}/r.
 \tag{U21}
\]

Choose any M-basis I in P+. For each p in I, select an eligible
type and consider the feasible allocation giving one unit only to p.
Average these r whole-instance allocations. Convexity preserves each
resource polymatroid, and every player in I receives value at least
v_min/r. Hence FOPT>=lambda>0, and this also explicitly constructs
a saved feasible fractional basis at target lambda.

The small value of lambda causes no numerical loop. Its binary length
is polynomial in the input length and log r.

## 9. Fractional-comparator search with relative precision

Set beta=epsilon/2 in the gap algorithm. Start with the feasible
lower target lambda and its fractional allocation from Section 8.
Use V+lambda as an externally infeasible upper target. It is strictly
above FOPT. At rational midpoints, a success raises the lower endpoint
and saves a fractional basis with uniform utility at least
`(1-beta)T`; a failure lowers the upper endpoint and soundly certifies
that its target exceeds FOPT.

Stop as soon as the endpoint distance is at most

\[
                                  \epsilon\lambda/2.
 \tag{U22}
\]

If the saved lower endpoint is L, the upper certificate implies

\[
 L\ge\operatorname{FOPT}-\epsilon\lambda/2
       \ge(1-\epsilon/2)\operatorname{FOPT}.
 \tag{U23}
\]

The saved fractional basis then has uniform service at least

\[
       (1-\epsilon/2)L
          \ge(1-\epsilon/2)^2\operatorname{FOPT}
          \ge(1-\epsilon)\operatorname{FOPT}.
 \tag{U24}
\]

The initial lambda allocation is also at least the required saved
service, so the argument covers termination without a midpoint call.
Rounding once proves (U5).

The number of iterations is
`O(1+log(1+V/(epsilon lambda)))`, polynomial in the input and
accuracy encoding lengths. Midpoint denominators grow by only that
many bits. The gap ratio is now 2/epsilon, proving the second runtime.
This comparison is against the genuine selected-basis fractional
optimum (U3), with no appeal to a mixed player-base LP.

## 10. General restriction selectors and exact selection budgets

The weighted omission theorem only requires a polynomial restriction
selection oracle for a family of r-element sets. Consequently both
algorithms extend from matroid bases to any such fixed-cardinality
family. Its parameter is q-r after any justified preprocessing.
If the family is empty, report that no permitted selected set exists;
if no member lies in P+, its fractional utility optimum is zero.
The averaging proof of (U21) uses a genuine permitted set and remains
valid without exchange axioms.

For example, the allowed set may be a common basis of two matroids,
possibly with a prescribed bound on the sum of player-selection
costs. Weighted matroid intersection implements the restriction
oracle, as detailed in `corank_degree_bounded_common_bases.md`.
The selection costs remain exact because rounding changes resource
counts, not the selected set. This is distinct from a cost budget
on player-resource assignments, which is treated separately and is
not silently imported into Sections 1--9.

The rational positive quota gap avoids the exact one-unit gate that
prevented an automatic factor-two unit-optimization transfer to two
exact player matroids. No exact algorithm for three unrestricted
matroid intersections is assumed.

## 11. Public comparison and scope

The largest-unit additive rounding is established background in the
ordinary item-assignment model. Rohwedder, Rouhani and Wennmann's
primary [ICALP 2025 paper](https://doi.org/10.4230/LIPIcs.ICALP.2025.127),
Section 1 and Lemma 10, records the Shmoys--Tardos additive allocation
rounding and explicitly discusses its unrelated-value version. The
present note does not claim that ordinary-item rounding as new.
The proof above supplies the recipient-polymatroid and player-basis
interfaces needed for this parameterized transfer.

For intrinsic values and compulsory players, Bamas et al.,
[arXiv:2307.08453v1, Theorem 21](https://arxiv.org/html/2307.08453v1),
is the corresponding additive primary anchor used by the earlier
manuscripts. Its intrinsic-value factor-eight theorem must not be
advertised as a theorem for arbitrary player-dependent values.

The new ingredients used here are the fixed-corank weighted omission
algorithm, a polynomial-bit nonnegative support separator for the
fractional utility projection, and a target search that preserves the
genuine selected-basis fractional comparator. The last-unit loss is
fully retained. If u<=epsilon OPT, (U4) gives `(1-2epsilon)OPT`;
without such a condition it need not imply a positive multiplicative
guarantee.

The heavy/light near-two proof does not transfer automatically: a
resource can be heavy for one player and light for another, so its
two uses share the same original feasibility constraints. Treating
them as separate independent resources would be incorrect. No such
split is used here.

All claims are submitted for independent internal mathematical review.
There is no claim of external peer review, formal verification, or
exhaustive publication priority.
