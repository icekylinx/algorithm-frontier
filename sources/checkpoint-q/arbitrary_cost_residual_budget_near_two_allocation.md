# Arbitrary-cost allocation near factor two with an adaptive residual budget

**25 October 2026. New unrestricted-cost theorem manuscript;
root and independent full review requested.**

This theorem removes the proportional-cost and price-diversity
conditions of the preceding budgeted transfers. Resource values
remain intrinsic, while every player-type assignment cost may be
an arbitrary nonnegative rational. The output selects an actual
basis of an original player matroid, uses integer recipient-
polymatroid allocations, and preserves one assignment budget exactly.

The algorithm repeatedly computes the minimum cost of completing
some permitted light set to a selected basis with one heavy unit
per remaining selected player. It tests light service using the
budget left by that cheapest completion. The light budget changes
after omissions. A single surviving optimal pair remains feasible
in every current light region, which is the invariant needed by
the weighted omission proof.

## 1. Model, support parameter, and theorem

Let M have rank r>=1. Delete its loops, restrict all recipient ranks
to the remaining player ground P, and write q=|P| and c=q-r.
Type j has a positive rational intrinsic value v_j, an integral
normalized monotone submodular recipient rank f_j, and arbitrary
nonnegative rational costs c_pj. Integer allocation vectors belong
to P(f_j); unused resource capacity is permitted. The selected
players form an actual M-basis, and total assignment cost is at
most C>=0. Let OPT_C be the integer maximum selected minimum utility.

For a threshold theta>0, types with v_j>=theta are heavy and types
with v_j<theta are light. Fix rational 0<epsilon<1 and an integer
support budget K>=0, clipped to r. Define

\[
                   \theta^*={(1-\epsilon)\mathrm{OPT}_C\over2},
                  \qquad \Gamma(R)={R^R\over(R-1)^{R-1}}\le eR.
 \tag{R1}
\]

**Theorem R.** A deterministic algorithm always returns a genuine
M-basis and an integer allocation of cost at most C. Its time is

\[
                         \Gamma(1/\epsilon)^{c+K}
                                          \operatorname{poly}(H),
 \tag{R2}
\]

and its workspace is polynomial. If OPT_C>0 and some integer
optimal allocation has at most K selected recipients of heavy
units at theta*, its returned minimum utility is at least theta*.
For OPT_C=0 the guarantee is trivial without evaluating a parameter
at threshold zero.

In particular, choosing epsilon=eta/(2+eta) gives factor 2+eta in

\[
            \Gamma\!\left({2+\eta\over\eta}\right)^{c+K}
                                    \operatorname{poly}(H).
 \tag{R3}
\]

The computed heavy Boolean rank being at most K is a sufficient
condition. Section 11 gives the stronger computable sufficient
condition using the largest affordable heavy recipient set.
No price-diversity or cost-ratio parameter occurs in (R2).

The algorithm enumerates every distinct value split and every
support cardinality through K. A support beyond K is simply not
processed; this omission is never called original-target
infeasibility. The unconditional additive guarantee in Section 10
is retained on every input.

## 2. Fixed split and the minimum heavy-completion oracle

For one fixed split, write J_s,J_b for the light and heavy types,
u_L=max_(j in J_s) v_j, and a_H=min_(j in J_b) v_j. Empty maxima
are zero and an empty heavy minimum is infinity. Fix 0<=k<=K.

For Q subseteq P, let h_k(Q) be the minimum cost of a feasible
one-heavy-unit assignment H to k distinct players F for which
there is a disjoint light set I subseteq Q of size r-k such that
I union F is an M-basis. If no such pair exists, set h_k(Q)=infinity.
The oracle returns an attaining pair I_Q,H_Q as well as its cost.

This is polynomial weighted matroid intersection. Form one light
copy of every p in Q and every eligible heavy pair (p,j). The
first matroid is the parallel extension of M to these copies.
The second is the direct sum of the uniform rank-at-most-(r-k)
light-copy matroid and the rank-k truncation of the direct sum
of the heavy types' Boolean recipient matroids. A common independent
set of cardinality r must have exactly r-k light copies and k heavy
pairs at distinct original players forming an M-basis.

Give every light copy weight zero and every heavy pair its actual
cost c_pj. Minimum weight at cardinality r computes h_k(Q) and
its pair. The pair ground is polynomial in q and the number of
types, independently of binary resource supplies. The attained
cost is a sum of at most k original encoded costs and has a
uniform polynomial bit length.

If Q' subseteq Q, its permitted completions are a subfamily, so

\[
                                  h_k(Q')\ge h_k(Q).
 \tag{R4}
\]

This monotonicity is useful, but the proof below uses the stronger
explicit comparison with a fixed promised heavy assignment.

## 3. The light utility region at a current residual budget

For every D>=0 define

\[
 \mathcal X_s(D)=\{(x_j)_{j\in J_s}:x_j\in P(f_j),\quad
                   \sum_{p,j\in J_s}c_{pj}x_j(p)\le D\},
 \tag{R5}
\]

\[
 \mathcal U_s(D)=\{z\ge0:\exists x\in\mathcal X_s(D),\quad
                  z_p\le\sum_{j\in J_s}v_jx_j(p)\quad(p\in P)\}.
 \tag{R6}
\]

This is a compact convex downward rational region. It has the
exact nonnegative packing separator proved in
`unrelated_values_exact_budget_additive_allocation.md`: optimize
support in nonnegative directions using the fractional allocation
LP with original resource separation and the one explicit budget,
then use the normalized outer support LP. A positive support gap
returns a valid nonnegative packing row; a nonpositive gap proves
membership. Reconstruction uses the direct fractional feasibility
LP including the same budget D.

All its LPs have polynomial dimension and a uniform polynomial-bit
vertex and separating-row bound. At an omission node Q, the only
changing input is D=C-h_k(Q), whose bit length is polynomial by
Section 2. The original light recipient ranks and original player
ground remain fixed. In particular, no contraction of resource
capacity to Q is substituted for the utility projection.

## 4. The adaptive gap routine

Fix rational target t>b>0. The promise is that there exist an
M-basis split I* union F*, with |I*|=r-k, a feasible one-heavy-unit
assignment H* to F*, and a fractional light allocation x* giving
each player in I* utility at least t, such that

\[
                             c(x^*)+c(H^*)\le C.
 \tag{R7}
\]

The light counts can be discarded outside I*. Starting from Q=P,
compute h_k(Q). If no pair exists or h_k(Q)>C, fail this node.
Otherwise let D_Q=C-h_k(Q) and separate b*1_Q in U_s(D_Q).

If membership succeeds, retain the attaining completion I_Q,H_Q.
Reconstruct a light allocation serving all of Q at level b with
cost at most D_Q, and discard its counts outside I_Q. It still
serves I_Q at b and its cost did not increase. Since c(H_Q)=h_k(Q),
the actual combined cost is at most C. Return this pair and the
fractional light witness.

If membership fails, take the returned nonnegative violated row
and perform the weighted first-violation prefix omissions from
`corank_weighted_prefix_free_batching.md`, with ratio t/(t-b).
Recurse on every enumerated child until a success, or fail after
all children fail. The number of omitted coordinates available
at Q is |Q|-(r-k).

The attaining minimum-cost completion is essential at a success.
An arbitrary completion could cost more than h_k(Q) and would
not justify adding it to a light allocation charged against D_Q.

## 5. The same promised pair survives every relevant row

Suppose the pair I*,H*,x* in (R7) has I* subseteq Q. It remains
an eligible completion in the definition of h_k(Q). Hence

\[
             h_k(Q)\le c(H^*),\qquad
             c(x^*)\le C-c(H^*)\le C-h_k(Q)=D_Q.
 \tag{R8}
\]

Thus the node cannot fail its completion check, and its full
target t*1_(I*) belongs to the *current* region U_s(D_Q).
Every nonnegative row returned at this node is valid for that
full target. If the row is a·z<=U and is violated by b*1_Q,
then the omitted set Q\I* has exactly |Q|-(r-k) elements and

\[
           a(Q\I^*)\ge a(Q)-U/t
                      >\left(1-{b\over t}\right)a(Q).
 \tag{R9}
\]

The same layer-cake argument therefore supplies a first-crossing
prefix certificate contained in Q\I*. Deleting that certificate
preserves the fixed I*, and (R8) applies again at the child.
Induction proves that a promised input cannot fail.

This is why changing the region is sound here. The proof does
not assume all rows come from one fixed budget region. It proves
directly that the same full target remains feasible in every
region along the surviving path. The adaptive abstract theorem
is written separately in `adaptive_residual_budget_corank_gap.md`.

At every node the prefix-free counting inequality depends only
on t/(t-b), not on the row values or on which admissible region
supplied them. The same polynomial-bit row and polynomial selector
cost bounds hold uniformly. The gap routine therefore runs in

\[
                 \Gamma\!\left({t\over t-b}\right)^{c+k}
                                          \operatorname{poly}(H)
 \tag{R10}
\]

time and polynomial space, including unpromised inputs and all
failed completion calls. The zero-light-rank case k=r is tested
directly by minimum-cost all-heavy basis selection instead.

## 6. The fixed joint benchmark and target search

Choose a positive rational grid g dividing every original value.
Every integer selected minimum utility, including OPT_C, lies on
the g-grid. For this split and k<r, let X be the largest g-grid
T for which a pair of the form (R7) exists with light service T.
Heavy assignments in this benchmark are integral one-unit choices;
light allocations are fractional. The selected original basis is
genuine, not a mixture of player bases.

This joint benchmark is downward in T by trimming light allocations.
At a positive grid query T, run the adaptive gap with

\[
                            t=T,\qquad b=(1-\epsilon)T.
 \tag{R11}
\]

A failure puts T strictly above X; a success returns the weaker
light service together with its costed heavy completion. The
ratio in (R10) is 1/epsilon exactly, and no numerical workload
unit expansion or integer rounding of (R11) is needed.

If h_k(P)>C or is infinite, the zero-service pair is unavailable,
so skip this split and k. Otherwise initialize a legal saved
zero-service pair. Set V_L=sum_(j in J_s) v_j f_j(P). Since k<r,
a full target serves at least one light player and X<=V_L. Use
external upper grid bound V_L+g.

One-sided maximization moves the lower endpoint on success and
the upper endpoint only on failure. At adjacent grid endpoints
the saved lower target is at least X. Successes need not be
monotone or certify the queried full target; the externally
bounded upper endpoint need not itself have been queried. There
are polynomially many calls in the binary input length.

An empty light class has V_L=0 and only a zero-light candidate
when k<r. For k=r, record an affordable all-heavy M-basis directly,
without assigning a finite workload benchmark to an empty set.

## 7. Cost-preserving integer recovery

For a saved positive-target pair I,H,x, the fractional light
allocation gives every p in I at least b and costs at most
C-c(H). Apply the lower-rounding construction from
`unrelated_values_exact_budget_additive_allocation.md`, Sections
4--5, to the light resources alone.

Briefly, add a zero-cost disposal coordinate so every independent
fractional resource vector becomes a full extended base without
paying for unused units. Form its complement bases and the
per-player ceiling-prefix polymatroid. On the integral full-total
intersection face maximize the actual cost coefficients applied
to the dual vector, equivalently minimize cost of the original
base complement. The resulting integer light allocation costs
no more than x and loses at most u_L utility per selected player.
Discard disposal and all counts outside I.

Keep H and its original types unchanged. Heavy and light types
are disjoint because the split is by intrinsic resource value,
so the two resource allocations combine without capacity overlap.
Their total actual cost is at most C. The selected original basis
is I union rec(H), with minimum utility at least

\[
                              \min\{a_H,b-u_L\}.
 \tag{R12}
\]

Only nonnegative assignment costs are claimed; discarding counts
must not increase cost. A second independent hard assignment
budget is not preserved by the one scalar residual-budget oracle
or by one cost-optimal rounding objective.

## 8. An integer optimum gives the joint promise without spending more

Assume the support condition in Theorem R and choose the split at
theta* in (R1). Fix an optimal integer allocation whose selected
heavy-recipient set R has size k<=K. Discard counts outside its
selected basis. Keep one originally assigned heavy unit at each
p in R, preserving its type, and delete its other counts. Let I*
be the remaining selected players. Their original utility is
entirely light and at least OPT_C.

Use those original light allocations only on I* and the retained
heavy assignment H*. The sets are disjoint, their union is the
original selected basis, and neither dropping resource units nor
discarding recipients increases total cost. This is exactly a
joint witness (R7) at t=OPT_C.

If k=r, it supplies an affordable pure-heavy M-basis giving value
at least a_H. Otherwise OPT_C is a g-grid value, so the fixed
benchmark X is at least OPT_C. Its optimized saved b is therefore
at least (1-epsilon)OPT_C. The argument retains the actual support
and actual heavy types; it never extends R to a heavy matroid
basis or buys a replacement completion at an unaccounted cost.

## 9. Factor, time, and the intrinsic-value boundary

The comparator split puts equality on the heavy side, so

\[
                     u_L<\theta^*\le a_H,
        \qquad (1-\epsilon)\mathrm{OPT}_C-u_L
                               =2\theta^*-u_L>\theta^*.
 \tag{R13}
\]

Equation (R12), or the pure-heavy branch, proves the factor.
The number of distinct value splits is polynomial. For each,
the k values through K and their one-sided searches add only
polynomial factors to the maximum bound (R10), proving (R2).
All nested support LPs and completion-oracle costs have uniform
polynomial encoding; no cost-diversity exponent is hidden in
their polynomial work.

The arbitrary assignment costs are fully supported. Values must
remain intrinsic to a type: with unrelated player-dependent
values, one resource could occur on both sides of the heavy/light
split and the independently combined allocations could share
capacity. This theorem does not make that additional transfer.

## 10. Complete output and an unconditional additive guarantee

Initialize any M-basis with zero counts and cost zero. Enumerate
all distinct value splits and every k<=K, recording all legal
outcomes from Sections 6--7 and all affordable pure-heavy bases.
Run the accepted arbitrary-cost additive algorithm with the same
epsilon as well. It returns a genuine basis, preserves C, and
guarantees max{0,(1-epsilon)OPT_C-u}, where u is the largest
eligible original unit value. Its Gamma(1/epsilon)^c time is
absorbed by (R2).

Return the best actual minimum utility among these outputs.
This is complete even when the improved support promise fails.
Skipping support cardinalities is not used in an original-target
feasibility search; every target search belongs to its fixed
joint split/k benchmark. There is no budget-free fallback.

## 11. A computable affordable-heavy sufficient parameter

At a threshold theta, define h_C(theta) as the largest cardinality
of a feasible one-heavy-unit assignment whose distinct recipients
are M-independent and whose total heavy cost is at most C.
Compute it using the parallel lift of M on heavy pairs and the
direct sum of heavy Boolean recipient matroids. Minimum-weight
common independent sets of each cardinality are polynomial.
Their minimum costs are nondecreasing with cardinality because
costs are nonnegative and a common independent set can be trimmed.
One may consequently binary search the largest affordable size.

Every M-independent heavy recipient set can be extended to an
original M-basis without giving those added players heavy units;
they are just zero-cost light labels in the completion oracle.
Thus h_C(theta) is precisely the largest k with h_k(P)<=C.

For any budget-feasible original optimum, dropping to one unit
per selected heavy recipient gives such an affordable assignment.
Its heavy support is therefore at most h_C(theta). Consequently

\[
                               h_C(\theta^*)\le K
 \tag{R14}
\]

is a computable sufficient parameter condition for the theorem.
It is no weaker than using the uncosted maximum common rank of
M and the heavy Boolean matroid, or the latter's rank alone.
The main guarantee still allows the stronger existence of just
one optimum with at most K recipients even if h_C is larger.

## 12. Primary comparison and status

Rohwedder, Rouhani and Wennmann,
[*Cost Preserving Dependent Rounding for Allocation Problems*,
ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127), Theorem 3,
give a randomized polynomial O(log n) approximation for ordinary
Budgeted Santa Claus with intrinsic values and arbitrary costs.
Their cost-preserving additive rounding is public background.
The current theorem attains a deterministic near-two guarantee
with corank/support parameter dependence, arbitrary recipient
polymatroid oracles and optional player bases. It is a different
time regime, not an unconditional polynomial constant for that
ordinary problem.

The new interface is the minimum-heavy-cost residual budget and
the surviving full-pair invariant, together with the existing
weighted prefix-free count and exact-cost rounding. It avoids the
price-copy loss without asserting that a signed joint projection
is automatically a downward packing polytope.

Root and independent full mathematical review are requested for
the adaptive promise, use of the attaining completion, uniform
oracle bit bounds, all fixed-benchmark search cases, and the
computed affordable-heavy refinement. No formal verification,
external peer review or exhaustive priority claim is made.
