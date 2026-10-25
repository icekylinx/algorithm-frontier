# Faster global time for coarser integer-quota approximation

**25 October 2026. New tradeoff manuscript; independent and root full
review requested.**

The exact integer quota in the one-value and compulsory two-value
budgeted allocation algorithms gives a useful approximation/time
tradeoff. For every fixed integer d>=2, replace the half quota by
ceil(K/d), and solve all targets K<=d through the exact one-unit
coverage gate. The remaining positive-gap calls have worst ratio
(d+1)/(d-1), which improves the corank and whole-ground time bases.

In particular, exact factor three in these allocation models has
deterministic whole-ground time `(7/4)^(q+o(q)) poly(H)` and polynomial
space, while preserving the assignment budget exactly. The same
quota choice gives two-size job-polymatroid scheduling factor five
thirds at this base. The d=2 endpoints recover the accepted exact-two
and exact-three-halves results.

## 1. Constants and the three model scopes

Fix an integer d>=2 and define

\[
 R_d=\frac{d+1}{d-1},\qquad
 A_d=\Gamma(R_d)=\frac{R_d^{R_d}}{(R_d-1)^{R_d-1}},\qquad
 B_d=2-\frac1{A_d}.
\tag{QT1}
\]

For a supplied admissible base A, write

\[
 \mathcal T_A(q,H)=
 (2-1/A)^q
 2^{O(q\log\log(q+2)/\log(q+2))}\operatorname{poly}(H).
\tag{QT2}
\]

The ground is explicit, and H includes its size, all original rational
bits, and the paid polynomial oracle, LP, intersection, and decomposition
work. Numerical resource supplies remain binary. The following models
have the same assumptions as their already reviewed source manuscripts.

**One-value allocation.** An original player matroid M has rank r>=1
on q nonloops. Each resource type has an arbitrary integral recipient
polymatroid, unused units are allowed, all units have one common value
v>0, and each type-player pair has an arbitrary nonnegative assignment
cost. One total assignment budget C is exact. A genuine M-basis must
be selected. Write c=q-r and let K* be the integer optimum minimum
unit count. The utility optimum is vK*.

**Compulsory two-value allocation.** Every one of q players must be
served. Positive intrinsic values are u<a, recipient polymatroids and
nonnegative assignment costs are arbitrary, and one assignment budget
C is exact. Let OPT_C be the integer maximum minimum utility. Let h_C
be the largest affordable number of distinct recipients of one feasible
large unit, computed from actual large type-player costs as in the
accepted exact-two theorem.

**Two-size scheduling.** All job units must be assigned. Sizes are
u<a and aggregate integral job-polymatroid ranks are f_s,f_b on q_0
physical machines. Put h=f_b(P), let M_b be the Boolean-cap large-job
matroid, and let P^+ be its nonloop set. When rank(M_b)=h>0, put
q=|P^+| and c=q-h. Scheduling here has no assignment-budget extension.

The theorems below preserve these distinctions. In particular, the
compulsory two-value high-target LP is not asserted for unknown optional
player-basis selection.

## 2. The integer quota ratio

For every positive integer full target K use

\[
                         b=\left\lceil\frac Kd\right\rceil.
\tag{QT3}
\]

For 1<=K<=d, b=1. These cases will use exact one-unit feasibility,
not the positive-gap recursion.

For K>=d+1, write uniquely K=jd+s with j>=1 and 1<=s<=d. Then
b=j+1 and

\[
 \frac K{K-b}
 =\frac{jd+s}{j(d-1)+s-1}
 \le\frac{jd+1}{j(d-1)}
 =\frac d{d-1}+\frac1{j(d-1)}
 \le\frac{d+1}{d-1}=R_d.
\tag{QT4}
\]

The first inequality follows because increasing s adds the same
positive amount to numerator and denominator, and the numerator is
larger. Equality in the final bound is attained at K=d+1, where b=2.
The denominator is positive, so K>b>0 throughout this branch.

Since Gamma is increasing on (1,infinity), the weighted prefix-free
gap costs at most A_d raised to its remaining omission deficit.
Solving every small target K<=d by an exact gate is consequential:
using a positive-gap call at K=2 would give ratio two, which is larger
than R_d when d>3 and would lose the sharper base.

The guarantee b>=K/d will suffice for each approximation. Integer
quota recovery will preserve the stronger ceiling in one-value
allocation.

## 3. One-value allocation: the small-target gate

Use the exact minimum-cost one-unit coverage test from
`one_value_exact_budget_corank_two_allocation.md`. On eligible
player-type pairs, intersect the parallel extension of M with the
direct sum of the resource Boolean-cap matroids. A minimum-cost common
independent set of size r assigns one feasible original unit to every
member of an actual M-basis.

For any target 1<=K<=d, run this same test. If its minimum cost is at
most C, return that one-unit allocation. It gives precisely the needed
weak quota ceil(K/d)=1. If the test fails, no budget-feasible integer
allocation of any positive quota exists: such an allocation could
be trimmed to one original unit per selected player without increasing
cost. In particular it excludes the queried full K.

Thus the gate is exact for the one-unit coverage problem and one-sided
for the larger full quota K. A successful gate is not a claim that K
units are feasible. This distinction is preserved by the target search.

Under forced omissions Z, simply remove the corresponding player pairs
from the coverage test. A full-K basis avoiding Z still supplies its
trimmed one-unit witness. This remains polynomial work on all inputs.

## 4. One-value allocation: positive gaps, exact recovery, and optimization

For K>=d+1, use the fixed budgeted fractional count-service region
of the one-value theorem, with full quota t=K and output quota b in
QT3. Its nonnegative projected separator retains all original resource
constraints and actual assignment costs. The original M restriction
selector and weighted prefix-free routine return b-service on a
genuine basis, or soundly exclude every full-K basis in that region.

A full integer K-allocation is a full fractional witness. With forced
omissions Z, it survives whenever its selected basis avoids Z. The
remaining omission deficit is c-|Z|, and QT4 bounds the complete
extension cost by

\[
                         A_d^{c-|Z|}\operatorname{poly}(H).
\tag{QT5}
\]

This includes unpromised targets and failed selectors.

At a success, discard counts outside the selected basis and trim each
selected total to exactly b. Intersect the direct sum of the restricted
recipient polymatroids with the partition polymatroid of cap b at each
selected player. Its maximum-total face of total br is nonempty and
integral. Minimize actual assignment cost on that face. An integer
minimizer costs no more than the given fractional witness and supplies
exactly b units to every selected player. No unit is lost, and C stays
exact. This uses an integral face and a cost objective, rather than an
unjustified claim that adding a cost inequality preserves integrality.

Use the original integer search with external upper target
floor(sum_j f_j(P)/r)+1, zero lower target, and a saved actual allocation.
Every failure excludes the full queried K, while every success supplies
ceil(K/d) units. At adjacent integer endpoints the saved nominal target
L is at least K*, so the output has at least

\[
                            \left\lceil\frac{K^*}{d}\right\rceil
\tag{QT6}
\]

units per selected player. This argument needs no monotonicity of
successes. Zero optimum and missing resources use the zero allocation.
An empty player rank is returned separately with the original empty-set
convention. For a fixed prescribed player basis, the problem remains
exactly polynomially solvable by the quota intersection.

**Theorem QT-A.** One-value allocation in the stated optional-basis
model admits QT6, exact assignment budget, and polynomial space in
either

\[
 A_d^c\operatorname{poly}(H)
 \quad\text{or}\quad
 \mathcal T_{A_d}(q,H)
\tag{QT7}
\]

time. The global bound follows by applying the accepted block wrapper
to QT5 for every positive-gap target. Dovetailing retains the smaller
valid bound.

## 5. Compulsory two-value allocation: the adaptive count gap

For a positive utility target T, put K=ceil(T/u) and use b=ceil(K/d).
Consider first targets for which one large unit suffices for the weak
guarantee, namely T<d*a. Fix a possible heavy-recipient cardinality k.

The minimum-heavy completion oracle retains every original heavy
player-type pair and allows small labels only in the current ground Q.
It returns an attaining actual heavy assignment H_Q of cardinality k,
its complementary small set I_Q, and minimum cost h_k(Q). The small
count-service region has current budget C-h_k(Q), retaining the original
small type costs and capacities.

Suppose an integer full-T allocation exists. At every recipient of a
large unit, keep one originally assigned large unit of its original
type and discard the other counts there. Let H* be this assignment,
let its support size be k, and let I* be the complementary small-only
set. Each member of I* originally had at least K small units. The
retained pair costs at most C and k<=h_C.

Whenever I* is contained in Q, including after any forced omission
avoided by I*, the unchanged H* remains a feasible completion. Thus

\[
 h_k(Q)\le c(H^*),\qquad
 c(x_s^*)\le C-c(H^*)\le C-h_k(Q).
\tag{QT8}
\]

The original full-K small allocation remains feasible in every current
region along the surviving branch. This supplies exactly the adaptive
paired-witness invariant, with remaining omission budget k-|Z|.

For K>=d+1 and k<q, the positive-gap routine therefore costs at most
A_d^(k-|Z|) times polynomial work. At success it restricts the fractional
small allocation to the small set attaining h_k(Q), recovers an integer
b-quota by the same cost-minimizing full-total intersection, and adds
that same H_Q. Total assignment cost remains at most C. Its small
utility is bu>=T/d and its heavy utility is a>T/d.

Enumerate every k<=h_C, or every k<=q with unaffordable cardinalities
rejected by the completion oracle. For k=q, test affordable all-heavy
coverage directly. If all relevant calls fail, the original full-T
integer target is infeasible. No original heavy support is enlarged,
and no replacement heavy assignment is bought without accounting for
its actual cost.

## 6. Compulsory two-value allocation: all boundary gates and target search

If K<=d, then T<=d*u. Run exact minimum-cost one-unit coverage using
all positive resource types and all compulsory players. Any full
positive integer allocation can be trimmed to such a coverage, so
failure excludes the full target. Success gives utility at least
u>=T/d at cost at most C. This is the same exact coverage problem
for every K<=d; it is not an exact test of the larger nominal target.

For high targets the fixed-player fractional allocation LP and
cost-preserving lower rounding lose at most the largest unit a.
They already provide the desired weak guarantee whenever

\[
                       T\ge\frac{d}{d-1}a,
       \qquad T-a\ge\frac Td.
\tag{QT9}
\]

LP infeasibility soundly excludes the integer target. A feasible LP
is rounded with the accepted free-disposal and full-total dual-cost
construction, preserving the actual assignment budget. All original
fractional assignment coordinates are retained, even if one full unit
on a coordinate would cost more than C.

For a complete target procedure, use QT9 first. Below its threshold,
one has T<d*a because d>=2, so Section 5 applies whenever K>=d+1.
Use the one-unit gate otherwise. This covers every positive target.
The weaker high cutoff T>=d*a would also be valid, but is unnecessary.

The original common value grid g divides u and a. Initialize lower
target zero with zero counts and use external upper grid bound
sum_j v_j f_j(P)+g. Every failure excludes the full original integer
target, and every success gives at least T/d. Adjacent grid endpoints
therefore give a saved nominal target at least OPT_C, hence actual
minimum utility at least OPT_C/d. Successes need not be monotone or
feasible at their nominal full targets.

With only one positive value, the compulsory-player instance is solved
exactly by fixed-player minimum-cost quota intersection. With no
positive resources, zero counts are optimal. Zero budget, zero costs,
and empty heavy or small classes are therefore covered.

**Theorem QT-B.** Compulsory two-value arbitrary-cost allocation admits
exact factor d, one exact assignment budget, and polynomial space in
either

\[
 A_d^{h_C}\operatorname{poly}(H)
 \quad\text{or}\quad
 \mathcal T_{A_d}(q,H)
\tag{QT10}
\]

time. The second bound is unconditional in h_C. The support-cardinality
loop has only q+1 possibilities, and every hard extension uses the
original player ground. No cost-diversity parameter is introduced.

## 7. Two-size scheduling corollary

This uses the model and full-machine dual of
`two_size_makespan_corank_three_halves_transfer.md`; it does not add an
assignment budget to scheduling.

If h=0, solve the one-size problem exactly. If rank(M_b)<h, then
OPT>=2a and the usual additive-a rounding already gives factor 3/2,
which is no larger than 2-1/d. Otherwise rank(M_b)=h>0, and the
nonloop large-position ground P^+ is explicit.

At a hard target a<=T<2a, retain the original definitions

\[
 \begin{aligned}
 C_T&=\lfloor T/u\rfloor,
   &P(g_T)&=P(f_s)\cap[0,C_T]^P,\\
 F_T(S)&=C_T|S|+g_T(P\setminus S)-f_s(P),
   &K_T&=C_T-\left\lfloor\frac{T-a}{u}\right\rfloor.
 \end{aligned}
\tag{QT11}
\]

The retained-rank test g_T(P)=f_s(P) precedes dualization. The dual
is formed on all physical machines. A full target supplies K_T units
of this dual resource to a large-job M_b-basis, with

\[
 \delta_T=a+C_Tu-T,\qquad
                  0<\delta_T\le a,\qquad K_Tu\ge\delta_T.
\tag{QT12}
\]

Set b_T=ceil(K_T/d). For K_T<=d, solve exact one-unit feasibility by
intersecting the large-position player matroid and the Boolean cap of
the fixed dual resource. A full K_T basis supplies such a one-unit
basis, so failure is sound; success gives the required b_T=1.
For K_T>=d+1, use the quota gap and QT4. Forced omissions delete only
large-position candidates, leaving the full-machine dual unchanged.
The remaining deficit is c-|Z|.

Zero-extend the returned b_T-quota to the full machine ground and
complete it to an integer F_T-base y. Then x_b=1_I and x_s=C_T*1-y
are full original large and small bases. A machine in I has load at
most

\[
 \begin{aligned}
 a+C_Tu-b_Tu
 &=T+\delta_T-b_Tu\\
 &\le T+\left(1-\frac1d\right)\delta_T
 \le\left(2-\frac1d\right)T.
 \end{aligned}
\tag{QT13}
\]

The inequality uses b_Tu>=K_Tu/d>=delta_T/d and a<=T. Machines
outside I have load at most T. This bound applies to the small-quota
gate as well, because b_T=ceil(K_T/d) there. No extra unit-rounding
term appears.

For the high branch, the usual additive-a rounding satisfies the
same factor whenever T>=d*a/(d-1), because
T+a<=(2-1/d)T. This cutoff is at most 2a, so every remaining target
lies in the valid one-large-unit hard regime. Targets below a fail.
The original common-size grid, feasible upper target, and one-sided
minimization search give a final schedule of makespan at most
(2-1/d)OPT.

**Corollary QT-C.** In the nontrivial rank-retained branch, scheduling
has approximation factor 2-1/d and polynomial space in either

\[
 A_d^c\operatorname{poly}(H)
 \quad\text{or}\quad
 \mathcal T_{A_d}(|P^+|,H).
\tag{QT14}
\]

The other branches are polynomial. Since |P^+| is at most the number
of physical machines, this is also a whole-machine bound. It is not
a globalization over a binary-expanded slot ground.

## 8. Constants, exact encodings, and profile-sensitive bounds

The first few fixed choices are:

| d | R_d | A_d | Whole-ground base B_d | Allocation factor | Scheduling factor |
| --- | --- | --- | --- | --- | --- |
| 2 | 3 | 27/4 | 50/27, about 1.851852 | 2 | 3/2 |
| 3 | 2 | 4 | 7/4=1.75 | 3 | 5/3 |
| 4 | 5/3 | (3125/108)^(1/3) | about 1.674270 | 4 | 7/4 |
| 5 | 3/2 | 3*sqrt(3)/2 | about 1.615100 | 5 | 9/5 |

For fixed d, R_d is a fixed rational. After reducing R_d=a/b,
Gamma(R_d)^b=a^a/(b^b*(a-b)^(a-b)). The block conversion's local
comparisons can therefore be performed exactly by raising positive
quantities to the fixed power b. All relevant arithmetic has polynomial
bit length. The approximation integer d is fixed in the sharp-base
global displays; no oracle for an arbitrary exact real constant is used.

If d varies as a binary input, the original corank gap still has the
analytical A_d bound and performs only rational quota comparisons.
For the global wrapper, a supplied certified polynomial-bit bound
on A_d can be used. The simple rational choice 3R_d>A_d always gives
a valid uniform version of QT2. Expanding powers whose exponent is
the numeric input d is not charged as polynomial work.

For the fixed-deficit applications, the accepted profile refinement
also gives

\[
 \min\left\{A_d^c,
       E(q)\Psi_{A_d}(q,c),\binom qc\right\}
                      \operatorname{poly}(H),
\tag{QT15}
\]

with the definitions of `global_gap_corank_profile_bound.md`. In
compulsory two-value allocation it may be applied separately to every
support k, with c replaced by k. The polynomial support loop preserves
these per-target improvements. The binomial option uses zero-deficit
gaps, not an unprovided exact selected-set optimizer.

Every algorithm stores only polynomially many count coordinates,
rational LP data, local cover tables, and current search counters.
Binary target search takes polynomially many calls. No primitive
enumerates resource units or numerical quotas. The exact budget
arguments use one cost objective; multiple independent assignment
budgets are outside these theorems.

## 9. Meaning and provenance of the tradeoff

The d=3 allocation result improves the global time base from 50/27
to 7/4 when a factor-three guarantee is acceptable in the specified
one-value or compulsory two-value arbitrary-cost models. The generic
intrinsic-value factor-three theorem has base 50/27; the sharper base
here comes from an integer count quota and exact quota recovery, not
from applying its largest-light-unit rounding formula.

The underlying costed count projection, adaptive residual budget,
integer quota recovery, and full-machine scheduling dual retain their
separate proofs and audits. The new ingredient in this note is the
complete handling of all K<=d targets by the exact one-unit gate,
which permits the sharper worst ratio in QT4 for every remaining call.
The target-search semantics and all-input time bounds are part of the
composition, not additional promises.

The whole-ground base transformation is established monotone-local-
search background, attributed in
`polynomial_space_global_gap_conversion.md` to Fomin, Gaspers,
Lokshtanov and Saurabh,
[*Exact Algorithms via Monotone Local Search*](https://sites.cs.ucsb.edu/~daniello/papers/monotoneLocalSearch19.pdf).
The present results are internally proposed theorem compositions, not
claims of exhaustive publication priority. They concern exponential
time in an explicit ground, exact stated budgets and capacities, and
arbitrary recipient or job polymatroid oracles. They do not assert
polynomial-time constant approximation or extend the one-unit
selection gate to unsupported intersections of additional matroids.
