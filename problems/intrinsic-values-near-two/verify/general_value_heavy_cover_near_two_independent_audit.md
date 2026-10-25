# Verification note

**Curated source path:** `sources/checkpoint-p/general_value_heavy_cover_near_two_independent_audit.md`

The source audit follows.

# Independent audit of general-value allocation near factor two

**25 October 2026. Full independent mathematical review of A1--A14.**

Reviewed manuscript:
`general_value_allocation_heavy_cover_near_two.md`.

The argument passes. For compulsory players and arbitrary positive
intrinsic resource values, the algorithm gives factor 2/(1-epsilon)
within Gamma(1/epsilon)^k poly(H) time whenever the stated heavy-cover
condition at (1-epsilon)OPT/2 holds. Its unconditional fallback and
the optional coloop refinement have the correct scope. The proof
does not import any ordered-layer local-search invariant.

This audit checks the complete manuscript. The decomposition and
per-player rounding interface is also proved in full in
`corank_arbitrary_value_additive_allocation.md`, Sections 3--4;
there is no need to duplicate that proof here.

## 1. Enumerating value splits preserves the required strict boundary

After zero-rank and zero-value types are removed, sorting the distinct
positive values produces all heavy suffix/light prefix partitions.
For any positive real threshold theta, the classification
v_j>=theta versus v_j<theta is one of these partitions. Hence the
partition at theta*=(1-epsilon)OPT/2 is included even if theta* is
not on the value grid or coincides exactly with a resource value.

The equality convention is essential: values equal to theta* must
be heavy. It yields u_L<theta* on the light side, whereas heavy
units all have value at least theta*. The manuscript uses exactly
this convention.

For each fixed split, the aggregate heavy Boolean cap is a matroid
N. Its dual M=N* has rank q-nu and corank nu. Deleting M-loops,
equivalently N-coloops, reduces the corank to c=nu-z without
changing its bases. The light workload is restricted, not contracted.
A returned basis is still a basis of the original M, so its
complement is a basis of the original N. Deleted M-loops are thus
served by the heavy complement in the final allocation.

## 2. The exact quota engineering is valid at every positive target

Take the common original value quantum g and write epsilon=e/d,
where 0<e<d. The artificial quantum Delta=g/d makes each
coefficient v_j/Delta a positive integer for a light type. For a
target T=mg with integer m>=1, the quotas

\[
                    t=md,\qquad b=m(d-e)
\]

are integers with 1<=b<t and t/(t-b)=1/epsilon. Thus every queried
positive target satisfies the genuine gap hypothesis. There is no
call with t=b, even at the first original grid point T=g.

All scaled ranks are queried through the fixed light-workload
function F. A recursive deletion only restricts its ground. Binary
arithmetic suffices for d, m and the scaled ranks; no number of
iterations is proportional to their numerical magnitude.

## 3. The fixed-split auxiliary maximization search is sound

The auxiliary benchmark X is the largest original-grid target whose
full workload quota is feasible on an M-basis. This benchmark is
well-defined and finite when M has positive rank; target zero is
always feasible and total light value V_L bounds X.

The upper endpoint above V_L/(1-epsilon) is stronger than needed
for original-target infeasibility, but also makes a gap success
impossible. Its b*Delta output on even one selected player would
exceed total light value. For V_L=0, the first positive grid point
has the same property. This is valid both before and after deleting
M-loops, since restriction cannot increase the available total.

Every failed batch call proves that its full auxiliary target is
infeasible. Therefore the maintained failed upper endpoint stays
strictly above X. At adjacent grid endpoints, the saved successful
lower target L is at least X. Its actual workload quota is
(1-epsilon)L, at least (1-epsilon)X. Success need not be monotone
or certify feasibility of L itself. The manuscript uses only the
sound direction of failure.

The target range and the factor 1/(1-epsilon) have polynomial bit
length. Consequently the number of fixed-split trials is polynomial.
There is no binary search across different heavy splits, across
different player matroids, or across a parameter-cap predicate.

## 4. Reconstruction pays exactly one largest-light-unit loss

After a successful quota call, zero extension restores the full
original player set. The independent workload vector can be
extended to an integer base of the full light-workload rank. Its
decomposition into the scaled original resource ranks yields
fractional original bases with exactly the same aggregate workload
value at each player.

The explicit polynomial-size intersection proof in the additive
manuscript verifies this decomposition for binary scaling factors.
It does not require scaled component counts to be divisible by
their scaling factors. The separate lower-rounding lemma handles
that fractional remainder and loses at most u_L at each individual
selected player. Thus the selected M-basis has light value at
least b*Delta-u_L.

The complementary N-basis can receive one unit per player from
the unweighted aggregate heavy polymatroid. Integral sum
decomposition assigns these units among the original heavy types.
Every chosen unit has value at least a_H, regardless of differences
between heavy values. Extra assignments when resource vectors are
extended to bases cannot reduce any player's value. Therefore the
candidate's minimum value is at least

\[
                         \min\{a_H,b\Delta-u_L\}.
\]

This combines independently feasible heavy and light resource
families. It requires compulsory players and no additional local
cross-type constraints, exactly as stated in the model.

## 5. The optimum supplies the correct small-only basis

In a fixed integer optimum, let R contain every player receiving
some heavy resource at threshold theta*. Keeping one aggregate
heavy unit per member proves that R is independent in N. Extend
R to an N-basis B. The complement I*=P minus B is an M-basis
contained in the players receiving no heavy unit in the optimum.

Every member of I* therefore has original light value at least OPT.
The scaled original integer light allocation dominates
(OPT/Delta)*1_(I*), and this quota is integral because OPT is on
the original g-grid. Thus the auxiliary X for this split is at
least OPT. Deleting M-loops does not remove any element of I*.

If M has positive rank and this split is processed, its light
output has value at least

\[
              (1-\epsilon)\mathrm{OPT}-u_L
                         =2\theta^*-u_L>\theta^*.
\]

Its heavy complement has value at least a_H>=theta*. This proves
the claimed minimum value. Equivalently, the integer light-only
optional-basis optimum is at least OPT, so the additive theorem
applied to that light instance already proves the same comparison.
The manuscript's stronger auxiliary workload benchmark is also
valid by the direct argument above.

## 6. Boundary cases and parameter budgeting

If rank(M)=0, the heavy Boolean basis covers all players. A pure
heavy candidate of value at least a_H is constructed directly.
For the optimum split this already gives theta*. Such a branch may
be retained even when the budget on nu would otherwise reject it;
it is polynomial and does not invoke a rank-zero quota problem.

If the heavy side is empty, N has rank zero and M is free. The
light branch then has corank zero; the infinite a_H convention
merely removes the heavy term from the displayed minimum. If the
light side is empty and M has positive rank, its auxiliary optimum
is zero. This split still produces a legal candidate but cannot
be the good split of a positive optimum, since that would force
the positive small-only promise just proved. Empty resource
families and OPT=0 are separately harmless.

The sufficient headline condition nu(theta*)<=k ensures that the
good split's corank is within budget. The optional condition
nu(theta*)-coloops(N_theta*)<=k is also sufficient. That refined
quantity need not be monotone in theta, but the proof does not
require monotonicity: every split is treated separately. Skipping
a split is never treated as evidence against the original optimum.

## 7. Runtime, fallback and lower-bound scope

There are polynomially many splits and polynomially many target
trials per processed split. Every nontrivial core has c<=k, and
the batch tree charges failed rank attempts as well as recursive
calls. This proves Gamma(1/epsilon)^k poly(H), with a polynomial
degree independent of k and epsilon. Depth-first cores and
sequential split processing use polynomial workspace.

Taking the best actual allocation together with the public
(8+zeta) allocation, for fixed zeta>0, gives a valid guarantee on
every input. When the condition at theta* holds, the near-two
candidate adds its stronger conditional guarantee. Neither actual
objective comparison nor the fallback needs the unknown optimum
threshold to be identified during execution.

Substituting epsilon=eta/(2+eta) gives exactly factor 2+eta and
the stated (O(1+eta^-1))^k dependence. Setting epsilon=0 is not
permitted: it would remove the quota gap. The manuscript correctly
keeps that limitation visible.

The separate two-value oracle barrier does not automatically become
a matching barrier for every heavy-threshold convention here.
For example, on its OPT=2 hidden instance, the present threshold
1-epsilon puts small value-one units on the heavy side. The
resulting heavy-cover rank can be very different from the number
of value-two units. The manuscript explicitly warns that the
parameter must be aligned before transferring a lower bound; no
unsupported sharpness claim is made.

No gap was found in A1--A14. This is an independent internal
mathematical review, not formal verification, external peer review,
or an exhaustive publication-priority assessment.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
