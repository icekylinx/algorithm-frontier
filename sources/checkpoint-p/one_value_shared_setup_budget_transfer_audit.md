# Independent audit: one-value allocation with setup and assignment costs

**25 October 2026. Fresh full read by the transfer-frontier researcher of
`one_value_shared_setup_assignment_budget_tradeoff.md`, Sections 1--8 and
SU1--SU11. Internal mathematical audit, not external or formal verification.**

The complete theorem passes. The same actual basis that attains the
current setup minimum is used for successful quota recovery. This closes
the setup/assignment budget coupling without assuming that separate
minimizers can be combined. The small-target gate correctly charges each
selected player's setup once, and the target search and forced-omission
time bounds preserve their stated semantics.

## 1. Zero-utility feasibility and the initial legal output

Every original solution pays the setup sum of a genuine M-basis, and
all original assignment costs are nonnegative. Therefore its total
cannot be below the minimum setup sum. If that minimum exceeds C, even
a zero allocation cannot be legal. Conversely, a minimum-setup basis
with zero counts is a valid original solution whenever its fee is at
most C. This proves the first gate in both directions, including C=0.

Deleting player loops and discarding any outside-selected assignments
are safe under the stated model. The rank-r requirement remains the
original rank during every later restriction; a rank loss means no
candidate basis exists and is correctly rejected. Rank zero is kept
separate from the positive-rank minimum-utility theorem.

## 2. The minimum-setup basis supports the adaptive promise

At every Q, ordinary weighted matroid basis selection finds the exact
minimum h(Q) and an attaining I_Q. If a protected full-service basis
I* remains in Q, then h(Q)<=sigma(I*). Its original fractional or
integer full-K allocation consequently fits the residual assignment
budget C-h(Q). Thus neither the basis/rank gate nor h(Q)>C can reject
the protected node.

The count region uses the original resource ranks and original actual
assignment costs. It is not a contraction to the current candidate
ground. Each changing residual right side is the difference between
the original budget and a sum of r original setup fees, so its binary
length remains uniformly polynomial.

For a violated nonnegative row, the protected stronger target gives
the usual omitted-weight inequality. Deleting the corresponding
certificate avoids I*, so the same inequality h(Q')<=sigma(I*) holds
after the next setup recomputation. This is the full-witness invariant
required by the adaptive weighted theorem; it does not assume a fixed
service budget along the recursion.

At a successful query, keeping I_Q is essential. The reconstructed
counts serve all of Q at the weak quota and have assignment cost at
most C-h(Q). Restricting to I_Q does not raise cost, and its setup is
exactly h(Q). No other permitted basis is substituted at recovery.

## 3. Exact integer quota recovery retains that same shared cost

Trim each selected fractional total to the integer quota b. Nonnegative
assignment costs and downward resource constraints make this safe.
On the chosen basis's product ground, intersect the direct sum of its
resource ranks with count cap b at every player. The trimmed vector
attains total br, the upper bound imposed by the player caps.

The maximum-total face is integral. Minimizing the original assignment
cost on that face gives an integer vector of no larger cost. Its total
equality forces exactly b units at every selected player. The unchanged
setup sum h(Q) plus this assignment cost is at most C.

This proof uses one cost-minimizing objective on an integral face. It
does not add the budget row and presume that the resulting intersection
is integral. All resource counts are binary encoded and the product
ground has polynomial size, so this recovery contains no numerical
unit expansion or hidden additive loss.

## 4. The small-target pair weights pay setup exactly once

For K<=d the required weak integer count is one. The first matroid on
the pair ground is the parallel lift of M; a cardinality-r independent
set uses distinct players forming an original basis. The second is
the direct sum of the resource Boolean-cap matroids. Their common
independent set represents one feasible resource unit per selected
player.

Assigning pair (p,j) weight sigma_p+c_pj pays the setup of p exactly
once because the first matroid allows only one pair for that player.
Weighted matroid intersection therefore minimizes the actual combined
cost of the complete one-unit solution, with no extra hard selection
constraint or third matroid.

Any original positive integer allocation can be trimmed to one unit
per selected player, keeping its selected basis and setup sum while
weakly lowering assignment cost. Thus failure of the gate excludes
every full positive K, whereas success is only the required one-unit
weak output. This is sufficient for every K<=d; success is correctly
not treated as exact feasibility of the nominal full K.

## 5. Larger targets and the integer search

For K>=d+1, b=ceil(K/d) obeys K>b>0 and the reviewed quota calculation
gives K/(K-b)<=(d+1)/(d-1). Every full integer K solution therefore
protects a path with the claimed A_d base, and every successful path
recovers the exact ceiling quota under the original shared budget.

The external count bound floor(sum_j f_j(P)/r)+1 is sound regardless
of setup costs or assignment costs. The initialized legal zero
solution supplies the lower endpoint. Since all genuine failures
exclude the full integer target, the upper endpoint remains strictly
above K*. At adjacent endpoints the saved nominal lower target is at
least K*, giving at least ceil(K*/d) actual units. No monotonicity of
weak successes is required.

Zero optimum, zero budget, empty resource lists, and zero assignment
costs are covered by the same initialization and tests. Fixed prescribed
player bases remain exactly optimizable by their minimum-cost quota
test; the approximation concerns optional basis selection.

## 6. Forced omissions, global time, and scope

An original full witness avoiding a forced Z remains eligible for the
same original rank-r basis selector. Its residual deficit is c-|Z|;
the minimum-setup comparison and fractional count promise still hold.
Every failed selector, budget gate and separator is polynomial on
unpromised inputs as well. The all-input extension bound therefore
has precisely the interface required by the streamed global cover.

The exact one-unit gates are already polynomial; applying the global
wrapper only to positive-gap calls preserves all target semantics and
gives the stated B_d base. Polynomial workspace includes the current
quota recovery LP, local cover tables and recursive counters. The
sharp algebraic constants are correctly stated for fixed d, with a
paid rational upper bound available for varying binary d.

The result has one common positive unit value, one original player
matroid and one shared scalar setup-plus-assignment budget. It does
not infer simultaneous preservation of several budgets, arbitrary
extra exact matroid constraints, or an unrelated-value no-loss quota
rounding. Those scope restrictions match the proof. No substantive
mathematical correction is requested.
