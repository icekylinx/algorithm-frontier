# Independent audit of machine activation for profile scheduling

**25 October 2026. Reviewer: allocation_four. Full fresh read of
activated_machine_profile_scheduling.md, AS1--AS2 and all four
sections, against the separately audited AB and PS rounding
primitives.**

## Verdict

The activation adapter passes. It allows an actual basis of an
original machine matroid, nonnegative setup fees and assignment
costs sharing one exact budget, arbitrary pair processing times,
and all original job-polymatroid bases remaining mandatory.

It proves the stated (1+epsilon) guarantee in
2^(O(q/epsilon))*poly(H+size(epsilon)) time and polynomial space.
The k-bucket alternative gives gamma_k in (k+2)^q polynomial time.
Neither result relies on an unproved polynomial or corank active-
basis selector.

## 1. Initialization must consider resource feasibility

A minimum-setup basis alone can fail to receive some mandatory
original type. The manuscript correctly avoids using that basis
as the unbounded-load initialization.

Instead it enumerates genuine active bases. At each B it retains
the original n_j=f_j(P), restricts assignments to B and permitted
pairs, and checks whether every type can still attain n_j. It
then minimizes actual assignment cost over the restricted product
of resource bases.

This product optimization is integral and separable across types,
because no machine-load constraints have yet been added. Together
with the fixed setup fee, it exactly tests that particular active
basis. Exhausting every basis therefore correctly detects original
infeasibility. A successful case yields an actual integer schedule
and finite upper makespan.

## 2. Original totals survive inactive machines and loops

Inactive-machine restriction must not redefine n_j as f_j(B).
The manuscript explicitly retains the original rank f_j(P), even
when resource availability on B is smaller.

If a player-matroid loop is the only place that can accept a
mandatory unit, no basis can activate it; initialization properly
declares infeasibility instead of dropping that unit. Eligibility
masks have the same accounting requirement.

The full-total recovery uses total sum_j n_j, while each type
remains capped by its own original n_j. Hence every type attains
its original mandatory count. There is no compensation by
extra units of a different type.

## 3. The active set is fixed before the joint rounding

The positive-target enumeration distinguishes the inactive label
from an active profile with no actual assigned jobs. This is
necessary: activating a machine still incurs its setup fee even
if its resulting load is zero.

For each complete label vector, the active set B is checked to
be an original M-basis, its fee is computed, and the residual
assignment budget is C-sigma(B). Every outside assignment is
masked to zero.

The LP and recovery are then exactly the PS procedure on that
fixed active set. All original types occur once in one resource
direct sum; active machine groups occur once in the other
polymatroid. The full-total integral face retains the mandatory
jobs, and minimizing actual assignment cost does not increase
the fractional cost.

The active set does not change during this rounding, so its setup
fee also does not change. Consequently the same combined budget
is preserved exactly.

## 4. Full-target completeness and output quality

A full original schedule of makespan T supplies both its actual
activated basis and the actual count profile of each active
machine. The original full schedule is feasible for that joint
LP, with identical setup and assignment costs.

The PS load argument gives at most (1+epsilon)T on every active
machine after recovery; inactive machines receive zero counts.
Thus some enumerated profile succeeds whenever the full target
is feasible. Total failure soundly excludes every full target.

The AB variant uses the same reasoning with k+1 active bucket
labels and one inactive label. Its quality gamma_k is unchanged,
because setup contributes only to the cost constraint, not to
the machine processing load.

## 5. Zero jobs, zero makespan and rank zero

When there are no mandatory job units, feasibility is exactly
the existence of an affordable active basis. A minimum-setup
basis solves that special case and the optimum makespan is zero.

When jobs exist, the zero-time test again enumerates active
bases, masks every positive-time pair, and keeps the original
mandatory totals. This is an exact test for optimum zero,
even if the initial minimum-cost assignment had positive load.

For player rank zero the only active basis is empty. A schedule
exists precisely when no mandatory units remain. These cases
are consistent with the stated initialization and are not
delegated to a positive-target division or bin construction.

## 6. Target optimization is the correct one-sided minimization

The retained actual schedule initializes a finite upper target.
After the exact zero test fails, zero is a certified lower target.
The original rational processing grid contains every integer
schedule load and OPT.

A failed midpoint is below OPT and raises the lower endpoint.
A weak success saves an actual schedule and lowers the upper
endpoint. No monotonicity of weak successes is required.

At adjacent grid endpoints, the upper nominal target is at most
OPT, so the saved schedule has the desired multiplicative load
bound. The fixed-set and target masks preserve the original
budgets and totals throughout.

## 7. Complete enumeration and workspace

If p_epsilon bounds active profiles at one machine, there are at
most (1+p_epsilon)^q complete label vectors. The PS partition
bound gives p_epsilon<=exp(3(K+1)), K=floor(2/epsilon).
The initial at-most-2^q feasibility and zero-time searches are
absorbed by this positive-target upper bound.

The complete traversal counts rejected nonbases, unaffordable
fees, infeasible LPs and failed resource-rank masks. The AB
case has exactly k+2 possible labels per machine, giving AS2.

Only occupied bins, binary cap counters, one current selected
set, one LP/intersection workspace and one best schedule are
stored. The full supplied rational accuracy length is included.
Thus the workspace claim does not hide a unary-sized bin table
or job expansion.

For a fixed rank r one can additionally count candidate selected
sets first, obtaining binom(q,r)*p_epsilon^r rather than the
coarser (1+p_epsilon)^q bound; this is optional and not needed
for validity of the manuscript.

## 8. Scope and the earlier active-support obstruction

The method enumerates complete active sets. It does not assert
that deleting candidate machines preserves a protected mandatory
job assignment, and it does not infer a corank algorithm from
a downward optional-allocation region.

The extension to any specified active-set family with polynomial
membership is valid for the same reason: enumerate its candidate
sets, perform the mandatory-resource feasibility checks, and then
fix the set before rounding. There is no assumed optimizer for
that family.

Several independent exact assignment-cost inequalities on one
integer allocation are outside the proof. The one exact scalar
budget, all mandatory totals, actual activation and approximation
claims are all justified. No substantive correction is requested.
