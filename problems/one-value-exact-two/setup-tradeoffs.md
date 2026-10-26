# One-value optional allocation with a shared setup and assignment budget


For one common unit value, optional player selection can pay setup fees
from the same budget as arbitrary assignment costs while retaining the
exact integer-quota tradeoff. In particular, factor two has whole-player
time base 50/27 and factor three has base 7/4, with polynomial space and
no violation of the shared budget.

The current minimum setup cost determines the residual assignment budget.
A successful count query is paired with the basis attaining that setup
cost. Small full targets are handled by a separate one-unit intersection
whose pair cost pays the setup fee exactly once.

## 1. Model, feasibility at zero, and theorem

Let M have rank r>=1. Delete its loops, restrict every recipient rank to
the remaining ground P, and put q=|P| and c=q-r. Every resource unit has
one common positive value v. Type j has normalized monotone integral
submodular recipient rank f_j, and its integer counts x_j belong to
P(f_j). Unused units are allowed. Each selected player p has a nonnegative
rational setup fee sigma_p; each assigned type-player unit has a
nonnegative rational cost c_pj. The shared budget is

$$
\sigma(I)+\sum_{p,j}c_{pj}x_j(p)\le C,
       \qquad \sigma(I)=\sum_{p\in I}\sigma_p,\quad C\ge0,
\tag{SU1}
$$

where I must be a genuine M-basis. Counts outside I may be discarded.
The objective is the minimum unit count on I, multiplied by v.

First find a minimum-setup M-basis. If its cost exceeds C, report that
no budget-feasible selected basis exists, even with zero allocation.
Otherwise this basis with zero counts is a legal initial solution.
Let K* be the integer optimum minimum count on budget-feasible bases.

For a fixed integer d>=2 define

$$
R_d=\frac{d+1}{d-1},\qquad
 A_d=\Gamma(R_d),\quad
 \Gamma(R)=\frac{R^R}{(R-1)^{R-1}},\qquad
 B_d=2-1/A_d.
\tag{SU2}
$$

**Theorem SU.** On every zero-feasible instance, deterministic algorithms
return a genuine M-basis and an integer allocation satisfying SU1 with
at least ceil(K*/d) units per selected player, using either

$$
A_d^c\operatorname{poly}(H)
 \quad\text{or}\quad
 B_d^q\,
 2^{O(q\log\log(q+2)/\log(q+2))}\operatorname{poly}(H)
\tag{SU3}
$$

time and polynomial workspace. H includes all encoded setup fees,
assignment costs, capacities and the paid polynomial oracle work.
The shared budget is exact. No numerical supply or count quota is
expanded into individual units.

For d=2 the guarantee is exact factor two with A_2=27/4 and B_2=50/27.
For d=3 it is exact factor three with A_3=4 and B_3=7/4. The rank-zero
case is returned separately with the usual empty-selection convention.

## 2. The attaining minimum-setup restriction oracle

At an allowed player ground Q, compute

$$
h(Q)=\min\{\sigma(I):I\subseteq Q,
                                      \ I\text{ is an M-basis}\}.
\tag{SU4}
$$

If no such basis exists, reject the node. Otherwise return an attaining
basis I_Q and its cost. This is ordinary minimum-weight matroid basis
selection on the restriction, retaining the original required rank r.
If h(Q)>C, reject as well. Every attained cost is a sum of r original
setup fees and therefore has uniform polynomial binary length.

For Q' contained in Q the possible bases form a subfamily, so h(Q') is
at least h(Q). More importantly, any particular basis I* contained in Q
satisfies h(Q)<=sigma(I*). The proof below uses this explicit comparison
with a protected full witness.

## 3. The residual assignment-count region

For D>=0, use the original fixed resource data to define

$$
U(D)=\left\{z\ge0:\ \exists x_j\in P(f_j),\quad
       \sum_jx_j(p)\ge z_p\ (p\in P),\quad
       \sum_{p,j}c_{pj}x_j(p)\le D\right\}.
\tag{SU5}
$$

This is the compact downward budgeted count region from
[Exact factor two for one-value allocation with arbitrary assignment costs](proof.md). Exact fractional
support LPs and their normalized nonnegative support separator run in
polynomial oracle time with uniform polynomial-bit rows. Membership
reconstructs an actual fractional count allocation. The region uses
original recipient constraints, not a new contraction of capacity to Q.

At a node with an attaining minimum-setup basis, put D_Q=C-h(Q).
This has polynomial encoding. For integer full target K and weak quota
b with K>b>0, query b*1_Q in U(D_Q).

On success, restrict the fractional allocation to I_Q. This preserves
the weak quota and cannot raise assignment cost. Keep the very same
attaining basis I_Q for the final output. Its setup plus fractional
assignment cost is at most h(Q)+D_Q=C.

## 4. The original full basis survives the changing budget

Suppose a basis I* has an integer or fractional K-unit allocation x*
with sigma(I*)+c(x*)<=C. Drop counts outside I*. At any Q containing I*,

$$
h(Q)\le\sigma(I^*),\qquad
 c(x^*)\le C-\sigma(I^*)\le C-h(Q)=D_Q.
\tag{SU6}
$$

Thus the stronger K*1_(I*) belongs to the current residual region, and
neither the rank nor the budget gate rejects this protected node. A
nonnegative row a*z<=U violated by b*1_Q therefore gives

$$
a(Q\setminus I^*)\ge a(Q)-U/K
                       >(1-b/K)a(Q).
\tag{SU7}
$$

The weighted first-crossing omission routine has a child contained in
Q\I*. Deleting that certificate preserves the same I*, and SU6 applies
again. The accepted adaptive residual-budget proof consequently gives
a gap routine of all-input time

$$
\Gamma\!\left(\frac{K}{K-b}\right)^{c-|Z|}
                                      \operatorname{poly}(H)
\tag{SU8}
$$

after any forced omitted seed Z. Every failed restriction, budget gate,
separator and recursion child is included. Successful outputs retain an
actual attaining basis. No approximate setup minimizer or unattained
cost lower bound is substituted in this argument.

## 5. Exact integer count recovery preserves the shared budget

For an integer weak quota b, trim the successful fractional counts to
exactly b per member of I_Q. All assignment costs are nonnegative.
On I_Q times the resource types, intersect the resource direct-sum
polymatroid with the partition polymatroid of cap b at every player.
The fractional vector attains total br, the maximum possible total.
This maximum-total face is nonempty and integral.

Choose a minimum-actual-assignment-cost integer point on that face.
Its assignment cost is no greater than the supplied fractional cost,
and total equality forces every player quota exactly. Adding the
unchanged setup fee sigma(I_Q)=h(Q) keeps the total at most C.

This is a scalar cost optimization on an integral face. It does not
assume that intersecting an integral polytope with the shared budget
row preserves integrality. There is no largest-unit loss in recovery.

## 6. Every target K<=d uses an exact one-unit gate

For positive integer K put b=ceil(K/d). If K<=d, then b=1.
Make one element for every eligible player-type pair (p,j). Intersect
the parallel extension of M with the direct sum of the types' Boolean
recipient matroids, and require cardinality r. Assign pair weight

$$
w_{pj}=\sigma_p+c_{pj}.
\tag{SU9}
$$

The parallel player matroid forces distinct owners forming a genuine
M-basis. The resource matroids make their one-unit assignment feasible.
Each selected player appears in exactly one pair, so the sum of SU9
pays each setup fee exactly once and the actual cost of its one unit.
Minimum-weight matroid intersection therefore finds the cheapest legal
one-unit basis under the shared budget.

If its cost is at most C, return that actual one-unit allocation. It
supplies exactly the needed weak count ceil(K/d)=1. Otherwise reject
the full K target: any positive integer allocation could be trimmed to
one original unit per selected player while retaining the same setup
fees and never increasing assignment cost.

The gate is exact for one-unit coverage, and one-sided for larger
nominal K<=d. It does not claim full-K feasibility on success. Forced
omissions simply remove the corresponding player pairs. No second
selection-cost constraint or unsupported third matroid is introduced.

## 7. Larger quotas, optimization, and complete time

For K>=d+1 use SU8 with b=ceil(K/d). The verified integer-quota identity
from [Faster global time for coarser integer-quota approximation](../whole-ground-allocation/integer-quotas.md) gives

$$
\frac{K}{K-b}\le R_d.
\tag{SU10}
$$

Hence every such forced-omission call costs at most
A_d^(c-|Z|) poly(H), with exact integer recovery from Section 5. Every
full integer K allocation supplies its protected stronger witness.
All target failures therefore exclude the full integer target, while
every success provides ceil(K/d) units at actual shared cost at most C.

After the zero-feasibility check of Section 1, initialize the legal
minimum-setup basis with zero counts. A hard external upper target is

$$
U_0+1,\qquad
                U_0=\left\lfloor\frac{\sum_jf_j(P)}r\right\rfloor.
\tag{SU11}
$$

Run one-sided integer maximization, saving actual outputs on success
and reducing the upper endpoint only on full-target failure. At
adjacent endpoints the saved nominal lower target L is at least K*.
Its actual output has ceil(L/d)>=ceil(K*/d) units. Successes need not
be monotone or certify their nominal full target. There are only
polynomially many target calls in binary encoding length.

For the whole-q algorithm, apply the accepted streamed block wrapper
to the uniform forced-omission routine at each positive-gap target.
The promised omitted set is the complement of an original M-basis,
so it has exactly c elements. Forced omissions preserve the full
original witness whenever they avoid that basis. No second utility
loss is applied in the wrapper. The small-target gates are already
polynomial. This proves both bounds in SU3.

All count and rank totals remain binary, the pair grounds have
polynomial size, and the recursion and cover iterators use polynomial
space. One may select or dovetail the corank and whole-q algorithms
to retain the smaller applicable time bound.

## 8. Encoding and scope

The sharp A_d and B_d displays are fixed-d statements. For fixed
rational R=a/b, Gamma(R)^b=a^a/[b^b(a-b)^(a-b)], permitting the exact
local comparisons of the global conversion. If d is a varying binary
input, the core uses only rational quotas and comparisons; a supplied
polynomial-bit rational upper bound such as 3R_d can be used in the
global wrapper instead of expanding powers with numeric exponent d.

There is one shared scalar budget. Setup fees are paid exactly on the
selected original M-basis and assignment costs on its actual resource
counts. Nonnegative costs justify trimming. The result does not assert
several independent setup/assignment budgets, an unrelated-value
exact-integer-quota theorem, or an unsupported extension of the
one-unit gate to arbitrary additional matroid intersections.

The proof combines the accepted adaptive residual-budget interface,
the one-value integral quota face, the small-target weighted unit
gate, and the streamed global conversion. The generic time base is
public monotone-local-search background, as attributed in the global
conversion note. No exhaustive publication-priority claim is made.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
