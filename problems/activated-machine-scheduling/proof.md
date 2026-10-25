# Proof note

This file is the curated proof record for the result in `README.md`. The original source note follows.

**Original source:** `sources/checkpoint-q/activated_machine_profile_scheduling.md`

# Machine activation and a shared setup/assignment budget

**25 October 2026. Root and independent full mathematical reviews completed.**

The physical-machine profile algorithms also support choosing an actual
basis of an original machine matroid and paying its setup fees from
the same budget as job assignment. The enumeration is over the whole
physical ground, so it does not require the unsupported polynomial
active-basis selector or corank routine excluded in earlier notes.

## 1. Exact model and guarantee

Let P be q physical candidate machines, with an original matroid M
whose actual basis B must be activated. Type j has original mandatory
count n_j=f_j(P) and must receive an integer base allocation in its
recipient polymatroid. Counts outside B are zero. Processing times
ell_pj are arbitrary nonnegative rationals, and assignment costs c_pj
and setup fees sigma_p are nonnegative rationals. One budget is

    sum_(p in B)sigma_p + sum_(p,j)c_pj*x_j(p) <= C.                (AS1)

All original n_j remain mandatory even if removing inactive machines
or a matroid loop reduces available resource rank. Define OPT as the
minimum makespan over legal activated bases and all their assigned
jobs. Let H include all original binary and oracle data.

**Theorem AS.** For 0<epsilon<=1, there is a deterministic
(1+epsilon)-approximation in 2^{O(q/epsilon)} poly(H+size(epsilon))
time and polynomial space in that full binary input. It detects
infeasibility if no activated basis can schedule all mandatory jobs
under AS1. It preserves the actual M-basis, all original job totals,
and the shared budget exactly.

More explicitly, for the k-bucket theorem AB, the same adapter gives
factor gamma_k=(3*2^k-1)/(2^(k+1)-1) in

    (k+2)^q poly(H+k)                                             (AS2)

time and polynomial space. Thus factor5/3 has base3 with activation,
and factor11/7 has base4. These are whole-ground bounds, not claims
of an active-machine corank algorithm.

## 2. Feasibility cannot be initialized by setup cost alone

A cheap M-basis may have insufficient recipient rank to receive all
mandatory jobs. Therefore minimum-setup basis selection is not a
correct unbounded-load feasibility gate for this problem.

Instead enumerate the actual M-bases, streamed as subsets of P. For
each B, first require sigma(B)<=C. Restrict every resource type to B
while keeping its original total n_j. Check whether its full original
base total can be attained, and minimize assignment cost over the
product of those restricted bases. If the minimum plus sigma(B) is
at most C, retain the actual integer schedule. If every basis fails,
the original scheduling instance is infeasible.

This uses at most 2^q polynomial work and polynomial space. The
product-base optimization is integral, because before load bounds
the resource types are independent. Inactive machines cannot be
silently removed from the definition of n_j.

For target zero, repeat this enumeration with all positive-time pairs
forbidden. Success gives an optimum-zero schedule. Failure certifies
OPT>0, provided the initial feasibility search succeeded. If there
are no job units, choose any affordable basis, for example a minimum-
setup basis, and return zero load. Rank zero is feasible only when
all mandatory counts are zero, since every machine is then inactive.

## 3. Add one inactive label and fix the selected set before rounding

At positive target T, give each machine either the label INACTIVE
or one of its occupied-bin profiles from the PS theorem. Let B be
the machines with active profiles. Require that B is an actual
original M-basis and sigma(B)<=C. Forbid every pair outside B.

The active profiles impose their original PS big-bin count caps and
small-load constraints. Solve one joint LP with every original n_j
and residual assignment budget C-sigma(B). Recovery is exactly PS:
one resource-direct-sum/machine-polymatroid intersection, total
sum_j n_j, minimum assignment cost on its integral full-total face.
The same activated B remains fixed before and after recovery, so its
setup cost is unchanged. Actual assignment cost does not increase.
This proves AS1 and the (1+epsilon) load bound.

A full target-T original optimum supplies its true active basis B
and its actual big-bin count profiles. Its unchanged schedule is
feasible for that enumerated joint LP. Therefore total target failure
soundly excludes every full target-T schedule. Every success returns
a complete legal original schedule, including its actual active basis.

If p_epsilon bounds profiles per active machine, there are at most
(1+p_epsilon)^q label vectors. With the PS partition bound,
p_epsilon<=exp(3(K+1)), K=floor(2/epsilon), this is
2^{O(q/epsilon)}. The initial 2^q searches are absorbed. Occupied bins
and all profile counters remain polynomial in full binary input,
including the actual rational encoding of epsilon.

The AB adapter is identical, with k+1 active labels and one inactive
label, proving AS2. The selected subset test and setup computation
are polynomial for each vector. One never creates separate copies
of a resource for different labels or different machine roles.

## 4. Target search and scope

The initial feasible schedule gives an upper makespan. After the exact
zero test, use the common rational processing grid and one-sided
minimization from PS. Failures update only the lower endpoint; weak
successes save actual schedules and update the upper endpoint. At
adjacent grid endpoints the saved upper target is at most OPT, giving
the claimed approximation with no extra accuracy loss.

The method also permits any specified family of active subsets with
a polynomial-time membership test: the enumeration tests that family
in place of M-basis membership. Initialization must still enumerate
all candidate sets and test full mandatory-job feasibility. No
polynomial optimization oracle for that selection family is presumed.
The theorem's main stated case remains the actual original M-basis.

This is a direct whole-ground enumeration adapter. It does not repair
the failed corank active-machine reduction: on a protected omission
path, jobs formerly assigned to a removed machine cannot simply be
discarded. Here the complete active set is fixed before its LP and
rounding. Several independent exact assignment-cost rows on one
integer schedule are not supported by this scalar-cost argument.

The result carries no first-publication or formal/external verification
claim. Its purpose is to make this additional model scope concrete,
including the necessary exponential initialization and original-total
accounting that a naive activation extension would omit.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
