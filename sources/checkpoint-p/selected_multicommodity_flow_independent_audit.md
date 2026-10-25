# Independent audit of selected concurrent flow

**25 October 2026. Reviewer: the allocation/corank branch.**

I read `selected_multicommodity_flow_corank_scheme.md` in full,
including the revised F1--F16, its several-budget extension, and the
model and comparison sections. The complete
construction passes this independent mathematical audit. It selects
one actual allowed set of q-c commodities, preserves capacities and
every explicitly listed nonnegative routing budget exactly, and obtains
`(1-epsilon) OPT` for splittable flow.

The current headline is `Gamma(1/epsilon)^c poly(H)`, using exact
fixed-set reoptimization and `rational_comparator_gap_optimization.md`.
The independently correct relative-search predecessor with
`Gamma(2/epsilon)^c poly(H)` remains in Section 7.1 of the main note.
Both proofs are checked and distinguished below. Sections 1--5 below
use one representative budget in their notation; Section 8 explicitly
checks the final several-budget revision.

## 1. Bounded downward region and the intended comparator

The flow equations use the tail-positive incidence convention. For
nonnegative normalized service z_i, conservation gives a net source
outflow d_i*z_i. The source outflow is bounded by the sum of outgoing
capacities, so positive d_i and distinct terminals give a finite
rate bound. Every individual arc-flow variable is also bounded by
its shared capacity. The projected service region is therefore
compact, including for zero capacities or disconnected terminals.

Reducing a commodity's rate scales all its flow by the same factor.
This preserves conservation and only decreases nonnegative shared
loads and cost. Thus the region is downward closed. Its definition
continues to use all original commodities and the original network;
omitted commodities simply have rate zero.

The comparator chooses one permitted set and then routes it
fractionally. It never mixes selected commodity sets. The exact
selector therefore matches the discrete part of the comparator,
while the flow LP matches its continuous part.

## 2. Farkas signs and clipping are correct

With the stated incidence convention, multiplying a commodity's
conservation equations by pi_i gives

    d_i*z_i*(pi_i(s_i)-pi_i(t_i))
      = sum_(e=(v,w)) x_ie*(pi_i(v)-pi_i(w)).

The correct arc inequality is consequently
`pi_i(v)-pi_i(w)<=ell_e+kappa*w_ie`. Its right side is nonnegative.
Summing over flows and using the capacity and budget upper bounds
gives the advertised valid packing row. Both the sign of the
terminal difference and the sign of the budget multiplier agree
with this calculation.

Farkas infeasibility of the primal system yields precisely a strict
positive excess of the terminal expression over
`sum_e u_e*ell_e+C*kappa`. A certificate need not initially have
nonnegative terminal differences. Replacing an entire negative-gap
commodity potential by zero is safe: all of its arc inequalities
become `0<=ell_e+kappa*w_ie`, and its contribution to the separating
objective can only increase because the queried z_i is nonnegative.
The strict inequality survives.

Clipping only the terminal coefficient without modifying its
potential would not have proved a valid row. The manuscript uses
the safe whole-potential replacement. Its argument requires the
nonnegative routing costs it explicitly assumes.

## 3. Normalization supplies an exact polynomial-bit separator

All the certificate constraints before normalization are homogeneous.
A nonzero strict certificate can therefore be scaled so the sum of
lengths, the budget multiplier and all split positive/negative
potential coordinates is at most one. Conversely, normalization
does not change validity of any returned row.

The resulting LP is bounded, always contains zero, and has explicitly
polynomial dimension and constraint count. Its coefficients are
original rational network data together with the queried service
vector. A rational optimal vertex has polynomial encoding by the
ordinary determinant bound. Multiplying its potential differences
by d_i and forming its capacity h preserves polynomial bit length.

A positive objective yields a strictly violated row with all service
coefficients nonnegative and h>=0. If the optimum is zero, the
Farkas equivalence proves primal feasibility; a separate primal LP
returns the actual flows. This is an implemented separation and
reconstruction interface, rather than an assumption about arbitrary
convex projections.

The same proof handles C=0 without division. With no budget, its
variable and all associated terms are omitted. For an undirected
physical edge, both directional variables share its single capacity
and its single dual length. Thus the reduction does not accidentally
double undirected capacity.

## 4. The corank gap applies to a fixed global family

Every separating row is valid for the same original service region.
At a node Q the query is b*1_Q. A stronger promised set contained
in Q must omit a sufficiently large fraction of each violated
row's nonnegative weight. The weighted first-crossing theorem thus
applies with t=T, b=(1-beta)T and R=1/beta.

The exact restriction selector returns an actual r-element permitted
set. If membership was established for the larger Q, discarding all
other commodity flows keeps its chosen subset's rate, capacities
and cost valid. This also supplies a direct output witness without
needing any rounding theorem.

All failed selector and separation attempts are paid by the reviewed
weighted omission analysis. The runtime claim does not assume the
input target was feasible. Exact matroid or common-basis constraints,
and one polynomially implementable selection-cost bound, stay inside
the fixed selector. The routing budget remains a separate constraint
in the service region.

## 5. Zero rate and the original relative search

The singleton LPs are bounded and have polynomial-bit optima. If
every permitted set contains a commodity of zero singleton rate,
positive common rate is impossible. Otherwise the selector finds
a set of positive singleton rates. Averaging its r singleton
routings preserves every shared capacity and the one cost budget;
scaling individual commodities down then realizes the positive
common lower scale in F13.

The external upper endpoint `rho_max+lambda_0` is strictly above
every permitted-set common rate. Failure of a gap query certifies
its target exceeds OPT. Success only promises its reduced rate,
which is sufficient for the saved lower endpoint. The proof never
uses monotonicity of successes.

At interval length at most `beta*lambda_0`, the saved lower target
exceeds `(1-beta)OPT`. Taking beta=epsilon/2 and retaining the
gap's own factor gives `(1-beta)^2 OPT >= (1-epsilon)OPT`. All
ratios and midpoint denominators have polynomial encoding, so this
does not introduce a numerical loop. The original
`Gamma(2/epsilon)^c` statement is valid as written.

The empty selected family is correctly detected before optimization;
rank-zero selection is separated from the positive-rank objective.
Zero-capacity networks, unreachable terminals and zero optimum are
covered. Optional path decomposition deletes cycles without raising
cost, but no unsplittable or bounded-path guarantee is inferred.

## 6. The rational-comparator improvement applies

For a fixed selected set I, maximizing its common rate is a bounded
explicit rational LP whose coefficients depend only on the original
network, demands, costs and budget. A common dimension and coefficient
bound give a known polynomial-bit denominator bound D for every
fixed-set optimum lambda_I. There are finitely many permitted I, so
OPT itself is one of those optima and has the same denominator bound.

The family and each fixed-set LP are independent of the target.
Thus they satisfy the exact hypotheses of RG1. If
alpha=1-epsilon=A/B, a target grid finer than `1/(B*D^2)` leaves a
saved I with lambda_I within less than that amount below alpha*OPT.
Exact reoptimization of I is essential: the saved target-dependent
flow need not have the fixed-LP denominator bound. If the exact
lambda_I were smaller than alpha*OPT, rational separation would
force a gap at least `1/(B*D^2)`, a contradiction.

This independently confirms the RG proof's applicability and gives
the improved `Gamma(1/epsilon)^c poly(H)` guarantee with exact
capacities and cost. It introduces no additive flow loss and no
integer-flow assertion. The earlier relative-search proof remains
a valid independent predecessor.

## 7. Public-model comparison and status

I freshly opened Mądry's primary
[*Faster Approximation Schemes for Fractional Multicommodity Flow
Problems via Dynamic Graph Algorithms*](https://madry.mit.edu/docs/multiflow.pdf).
Its introduction explicitly defines concurrent flow, the routing
budget version, and their polynomial LP formulations for fixed
commodities. Those are the appropriate continuous baselines here.

I also opened Chekuri--Khanna--Shepherd's primary
[*The All-or-Nothing Multicommodity Flow Problem*](https://chekuri.cs.illinois.edu/papers/anflow-sicomp.pdf).
Its model maximizes the admitted request count or weight, and its
introduction distinguishes fractional routing of a fixed subset
from edge-disjoint paths. The present exact-cardinality/common-rate
objective is correctly kept separate. This audit does not establish
an exhaustive literature or priority claim.

The proof chain therefore closes in the stated splittable-flow
model: a direct finite nonnegative separator, exact permitted-set
selection in corank time, rational optimization, and explicit legal
flow recovery. No allocation approximation or job-size rounding
result is needed. This is an internal mathematical audit, not
formal verification or external peer review.

## 8. Final several-budget revision

I reread the final main manuscript after it replaced one budget by
an explicitly listed polynomial-size collection. In every potential
arc inequality the right side is now
`ell_e+sum_h kappa_h*w_hie`, and the packing-row capacity is
`sum_e u_e*ell_e+sum_h C_h*kappa_h`. All multipliers and charges are
nonnegative. The whole-potential clipping argument therefore remains
valid without modification of its logic. The normalization includes
the sum of every budget multiplier, so the certificate LP is still
bounded and polynomial in the complete row encoding.

Scaling a commodity, averaging singleton routings, discarding
unselected flows and deleting cycles decrease or convexly preserve
every one of these budget rows. Exact reconstruction and fixed-set
reoptimization include all rows simultaneously. No integral rounding
step is performed here, so the one-objective limitation of the
allocation cost-preserving rounding theorem is irrelevant.

The several-budget extension is therefore sound. The budget count
affects the polynomial input size and determinant bound, not the
corank exponent. This does not extend the exact selector to several
selection budgets; that separate interface remains exactly as stated
in the main theorem.
