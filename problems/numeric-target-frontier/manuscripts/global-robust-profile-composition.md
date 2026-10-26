# Robust profile schemes with global resources and one common selection

**25 October 2026. Root composition theorem; full independent
mathematical review completed.**

The common-selection robust schemes also allow a single global
polymatroid in every scenario. That rank may couple different item
types and recipient blocks. For fairness, each scenario may require
either an independent resource vector or an entire resource base.
The selected recipient basis is the same in every scenario, while
integer resource assignments adapt separately.

## 1. Model and guarantees

Let M have rank r>=1 on q explicit candidate recipients P. Scenario
omega in a nonempty explicit list has its own coordinate ground

    E_omega=disjoint_union_(p in P) E_(omega,p),

an eligibility mask A_omega, a normalized monotone integral resource
rank F_omega, and original total R_omega=F_omega(E_omega). It has
nonnegative rational values v_omega, assignment costs c_omega,
setup fees sigma^omega on P, and budget C_omega>=0.

A common actual M-basis B is selected. The original budget in each
scenario is

    sigma^omega(B)+c_omega*x^omega<=C_omega.                    (GR1)

Real coordinates outside the selected blocks and eligibility mask
are zero. The scenario vectors are separate adaptive decisions.
Setup vectors need not agree between scenarios.

For max-min fairness, each scenario specifies one of

    x^omega integer in P(F_omega),
    x^omega integer in B(F_omega),                             (GR2)

and its required choice must be obeyed. The robust objective is
the minimum utility over all selected recipients and scenarios.
Let OPT_A be its integer optimum.

For makespan, every scenario requires the second family in GR2,
has arbitrary nonnegative rational processing times ell_omega,
and the objective is the largest block load over every scenario.
Let OPT_S be the corresponding integer optimum.

Let H include the complete scenario list, all binary data and paid
polynomial exact oracle, SFM, LP and integral-intersection work.
Set H_epsilon=H+size(epsilon) for rational 0<epsilon<=1.

**Theorem GR.** The following deterministic guarantees hold with
polynomial workspace and every original budget GR1 exact:

| Model | Integer approximation | Time up to poly(H_epsilon) |
| --- | --- | --- |
| Robust max-min, scenario-wise independent or mandatory-base global resource | at least (1-epsilon)OPT_A | binom(q,r) exp(4r(floor(3/epsilon)+1)) |
| Robust makespan, mandatory global base in every scenario | at most (1+epsilon)OPT_S | binom(q,r) exp(3r(floor(2/epsilon)+1)) |

Both are binom(q,r)*exp(O(r/epsilon))*poly(H_epsilon). The scenario
count enters polynomial work, not an exponential Cartesian product.
Original feasibility is also decided by the algorithm.

## 2. Original-base semantics survive selection and masks

For a fixed B, write

    A_(omega,B)=A_omega intersect union_(p in B) E_(omega,p).

In an independent scenario, restricting F_omega to this ground
legitimately permits unused units. In a mandatory scenario, retain
the original R_omega. If F_omega(A_(omega,B))<R_omega, reject B.
The required total is never changed to a smaller restricted rank.

A global base enforces the supplied global rank and its total.
Named type totals follow only when they are actually encoded by
that rank, for example by a direct sum of original type ranks.
The theorem does not infer additional per-job equalities from
an arbitrary global total.

## 3. Exact common-selection feasibility

Stream all r-subsets and reject nonbases of M. For each remaining
B, test every scenario's setup fee. If any exceeds its own budget,
reject B. For every mandatory scenario also test its original
rank and minimize assignment cost on the restricted total-R_omega
base face. Reject B if the minimum exceeds the residual budget.

For an independent scenario, zero allocation is feasible whenever
the setup test passes. For a mandatory one, its integral minimum-
cost base supplies an actual allocation. If all scenario tests
pass on the same B, retain that B and their actual vectors.
Otherwise, if all bases are exhausted, the original instance is
infeasible even without an objective target.

The searches cost binom(q,r) times polynomial work. Separately
minimizing the different setup vectors is not a substitute for
this common-basis enumeration. A cheap basis can also fail a
mandatory scenario's original-rank test.

Rank-zero selection uses the specified empty-objective convention.
It cannot support a positive mandatory resource total. In the
nonempty theorem, zero resource ranks and zero utility values
are handled by the preceding original feasibility tests.

## 4. Fix B, then solve the scenario profile gates independently

At positive target T, first apply the same setup and original-rank
guards for the current B. Every selected scenario gate now has
a fixed residual scalar budget C_omega-sigma^omega(B).

For an independent fairness scenario, use the global-resource
allocation theorem in [global-polymatroid-profile-transfers.md](global-polymatroid-profile-transfers.md).
For a mandatory fairness scenario, use the charged active/passive
lift in [mandatory-base-fair-allocation-passive-lift.md](mandatory-base-fair-allocation-passive-lift.md). Both
return a legal integer vector of utility at least (1-epsilon)T
at every selected block, or exclude an integer full-T witness on
that fixed B. Mandatory passive units remain charged and assigned
when their two copies are merged.

For a makespan scenario, use the global-base scheduling theorem
in [global-polymatroid-profile-transfers.md](global-polymatroid-profile-transfers.md), retaining its original
R_omega after all time masks. It returns an original base of
load at most (1+epsilon)T, or excludes every full-T schedule on B.

If any scenario fails, try the next basis. If all succeed, return
their actual original vectors on the SAME B. Resource coupling
inside a scenario is fully handled by its one global rank; the
different scenarios do not have to share one assignment vector.

An original robust full-T solution supplies a common B* and one
protected integer witness for each scenario. Every scenario gate
therefore succeeds on that B*. Complete common-basis failure
implies T>OPT_A for fairness and T<OPT_S for makespan.

## 5. Running times add over scenarios

Let p_A=exp(4(floor(3/epsilon)+1)) and
p_S=exp(3(floor(2/epsilon)+1)). For a fixed B, an appropriate
gate costs at most p^r times polynomial work in its scenario
encoding. Running the gates in sequence costs

    sum_omega p^r poly(H_omega+size(epsilon))
       <= p^r poly(H_epsilon).                                (GR3)

This also counts a basis that fails only at the last scenario.
Multiplying by all binom(q,r) candidates proves the per-target
bound. No scenario-product profile enumeration is necessary,
because scenario assignments are adaptive after B is fixed.

Only the current basis, one scenario solver state and the actual
outputs collected for that basis are stored. Those explicitly
many vectors have total polynomial binary size in H. The current
best robust solution also has polynomial total encoding.

## 6. Target optimization and exact zero makespan

For fairness, the exactly feasible initializer from Section 3
has utility at least zero. Choose a common rational grid g dividing
every positive original value in every scenario. Every integer
robust utility is a grid value. A finite upper bound is

    V_A=min_omega R_omega*max_(e in E_omega) v_(omega,e),        (GR4)

with an empty maximum interpreted as zero. If this bound is zero,
the initializer is optimal. Otherwise run the usual one-sided
maximization search from nominal zero to external upper V_A+g.
At adjacent endpoints the saved lower target is at least OPT_A.

For makespan, first repeat the entire basis enumeration with all
positive-time pairs removed in every scenario, retaining every
original R_omega. Success gives an exact zero-makespan solution.
After failure, zero is a certified failed lower target. The
original feasible initializer supplies an upper target, bounded by

    V_S=max_omega R_omega*max_(e in E_omega) ell_(omega,e).      (GR5)

Use the common original-time grid and one-sided minimization.
At adjacent endpoints the saved upper target is at most OPT_S.

Both arguments use only sound complete failures and actual legal
weak outputs; neither assumes monotone weak successes. All grid
and target arithmetic has polynomial bit length. Thus polynomially
many target calls prove the theorem without an additional loss.

## 7. Precise scope

The original selection is common. Assignments, resource ranks,
fees and budgets may vary with the explicit scenario. One scalar
budget is preserved on each separate recovered vector. This is
not a procedure for preserving several arbitrary exact costs on
one shared integer vector.

The theorem permits a mixture of optional and mandatory resource
families across fairness scenarios. It requires disjoint objective
blocks within each scenario and one integral resource polymatroid
there. Arbitrary overlapping value rows or an intersection of
unrelated resource ranks are not assumed to retain integrality.

Replacing actual M-bases by a supplied family with polynomial-time
membership permits full subset enumeration, with time
(1+p)^q poly(H_epsilon). No efficient optimization oracle for that
family is presumed. For fairness, use nonempty selected sets or
specify the empty-set objective separately. An empty scheduling
selection can support only zero mandatory resource totals. The
principal statement retains the sharper
rank-sensitive matroid-basis bound.

This note is a direct composition of the reviewed global-resource,
passive-lift and fixed-basis scenario interfaces. It makes no
publication-priority or formal-verification claim.
