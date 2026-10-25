# Proof note

This file is the curated proof record for the result in `README.md`. The original source note follows.

**Original source:** `sources/checkpoint-q/arbitrary_processing_profile_approximation_scheme.md`

# Arbitrary-processing polymatroid scheduling: an exact-budget approximation scheme

**25 October 2026. Root and two independent full mathematical reviews completed.**

All job units remain mandatory. Processing times may depend arbitrarily
on both machine and type, recipient restrictions are arbitrary integral
polymatroids, supplies remain binary, and one assignment-cost budget
is preserved exactly. Enumerating integer big-job count profiles
extends the earlier one-big-group bucket tradeoff to every requested
approximation factor 1+epsilon.

The complete deterministic running time is

\[
           2^{O(q/\epsilon)}
              \operatorname{poly}(H_\epsilon)
 \tag{PS1}
\]

for 0<epsilon<=1, where q is the number of physical machines.
Space is polynomial in the full binary input encoding, including
the entire supplied rational accuracy, even when 1/epsilon itself
is exponentially large.
No individual job identity or resource-unit expansion is used.

## 1. Model and precise theorem

Let P consist of q>=1 machines. For every type j, the normalized
monotone integral submodular rank f_j has mandatory original count

\[
                        n_j=f_j(P),\qquad N=\sum_j n_j.
 \tag{PS2}
\]

An integer schedule consists of x_j in B(f_j). Each eligible pair
(p,j) has arbitrary nonnegative rational processing time ell_(p,j)
and nonnegative rational assignment cost a_(p,j). Additional
eligibility restrictions are allowed, but never reduce n_j. The
original cost budget C>=0 requires

\[
                           \sum_{p,j}a_{p,j}x_j(p)\le C.
 \tag{PS3}
\]

Every type base remains mandatory, and the objective is to minimize
the maximum load over all physical machines. Denote this integer
optimum by OPT when the original budget-feasible family is nonempty.
H includes the explicit machine-type coordinates, binary numerical
data, rank-oracle interfaces and the paid polynomial SFM, LP and
polymatroid-intersection work. Write H_epsilon=H+size(epsilon), where
size(epsilon) is the full binary encoding length of its supplied rational
numerator and denominator. This is necessary even when epsilon is near
one, since log(1/epsilon) alone need not bound its input length.

**Theorem PS.** For rational 0<epsilon<=1, a deterministic algorithm
either detects that no original schedule satisfies the budget, even
with unbounded makespan, or returns an integer schedule of makespan
at most (1+epsilon)OPT satisfying all original type bases and PS3.
It obeys PS1 and uses polynomial space in H_epsilon.

For an explicit state-count bound, put

\[
 \delta=\epsilon/2,\qquad
 K=\lfloor1/\delta\rfloor,\qquad
 B=\left\lceil\frac{1-\delta}{\delta^2}\right\rceil,\qquad
 C_\epsilon=\binom{B+K}{K}.
 \tag{PS4}
\]

The time is bounded by either of the following simultaneous upper
bounds on this same algorithm:

\[
 C_\epsilon^q\operatorname{poly}(H_\epsilon),
 \qquad
 \exp\bigl(3q(K+1)\bigr)
       \operatorname{poly}(H_\epsilon).
 \tag{PS5}
\]

The second bound proves PS1. The first is a direct finite-composition
bound and does not depend on an asymptotic partition formula.
Neither B nor K is expanded or stored in unary.

For epsilon>=1, the already proved polynomial-time factor-two
full-total upper-prefix routine suffices. Thus the nontrivial
accuracy regime is 0<epsilon<=1. The zero-job and zero-optimum
cases are treated explicitly below.

## 2. The one joint cost-preserving recovery primitive

The coordinate ground has one element per eligible machine-type
pair. Counts on a coordinate are nonnegative integers, and can
be binary-large. The direct sum of all resource polymatroids
contains the possible fractional resource allocations.

After any mask, the available rank of type j is at most n_j.
Retain the original total requirement

\[
                             \sum_{p,j}x_j(p)=N.
 \tag{PS6}
\]

Since every type is individually capped by n_j, equality in PS6
forces each type to attain its own original n_j. Missing units
cannot be replaced by units of a different type. A masked rank
loss makes this full-total requirement infeasible.

Given an integral machine-cap polymatroid containing a fractional
resource allocation of total N, intersect it with the resource
direct sum. The intersection is integral. Its nonempty full-total
face at N is also integral, because N is an upper bound on total
resource count.

Minimize actual assignment cost on this face and choose an integral
minimizer. Its cost is no greater than that of the given fractional
witness. Hence a fractional cost at most C yields an integer
schedule respecting C exactly and retaining every mandatory type
base.

This uses a scalar cost objective on an integral face. It does not
assume that an arbitrary added budget inequality preserves
integrality, and it does not preserve an input-sized list of
independent costs on the same integer allocation.

## 3. The small-group upper-prefix inequality

For a group of coordinates on one machine, sort processing times
v_1>=...>=v_m>=0. Given fractional x, set

\[
                   X_h=\sum_{i\le h}x_i,\qquad U_h=\lceil X_h\rceil.
 \tag{PS7}
\]

The caps x'({1,...,h})<=U_h define an integral chain polymatroid.
Its rank on a nonempty coordinate set S is max{U_h:h in S}; the
empty-set rank is zero. This is a normalized monotone submodular
integer rank. Conversely its rank inequalities are equivalent
to the prefix caps, so no implicit slot construction is needed.

With v_(m+1)=0, summation by parts gives

\[
 \begin{aligned}
 \sum_i v_i x'_i
   &=\sum_h(v_h-v_{h+1})x'(\{1,\ldots,h\})\\
   &\le\sum_h(v_h-v_{h+1})\lceil X_h\rceil\\
   &\le\sum_i v_i x_i+v_1.
 \end{aligned}
 \tag{PS8}
\]

Thus one small group incurs at most its largest processing time
in added load. Empty groups contribute zero. Zero-time coordinates
remain covered by their prefix caps and the global mandatory
total, while contributing no load.

## 4. Exact bins at a positive target

Fix a rational target T>0. All pairs with ell_(p,j)>T are forbidden:
no full-T schedule can use them. A permitted pair is small when
ell_(p,j)<=delta*T.

Normalize a big processing time by T. Partition (delta,1] into
B half-open intervals

\[
 (\lambda_i,\mu_i],\qquad
 \lambda_i=\delta+i\delta^2,\qquad
 \mu_i=\min\{1,\delta+(i+1)\delta^2\},
 \quad 0\le i<B.
 \tag{PS9}
\]

These intervals are disjoint and cover exactly (delta,1].
Their widths are positive and at most delta^2. For a normalized
big time t=ell_(p,j)/T, its unique index is

\[
                   i=\left\lceil\frac{t-\delta}{\delta^2}\right\rceil-1.
 \tag{PS10}
\]

Thus a time exactly equal to an internal upper endpoint belongs
to the preceding bin. A time exactly delta*T is small. A time
exactly T belongs to the final big bin. All threshold comparisons
are exact rational comparisons.

Only bins containing an actual eligible machine-type coordinate
are constructed for a machine. Every other bin is fixed at count
zero. There are at most the original number of pair coordinates
occupied bins, even when B is exponentially large in its encoding.
Computing indices by PS10, grouping coordinates by their binary
indices, and recovering their rational endpoints uses polynomial
time and bit space in H_epsilon and the target bit length.

## 5. Machine profiles and the fixed-profile LP

For a machine p, a profile consists of nonnegative integers h_(p,i)
for its occupied big bins, satisfying

\[
       \sum_i h_{p,i}\le K,\qquad
       L_p=\sum_i\lambda_i h_{p,i}\le1.
 \tag{PS11}
\]

Absent bins have cap zero. A profile is a vector of upper bounds,
not a choice of actual job identities.

For a fixed profile on every machine, solve the following rational
LP with the original resource constraints, mandatory type totals,
eligibility, and the one original budget:

- In each big bin i of machine p, cap the total count by h_(p,i).
- On machine p, cap the fractional load of all small pairs by
  (1-L_p)*T.
- Forbid every processing time greater than T.

No separate restriction is imposed on the total fractional machine
load. The displayed constraints are the ones needed for recovery.
They are sound for the full-target witness proved in Section 7.

An empty profile LP is skipped. A masked resource rank loss below
an original n_j, a budget failure, or an unavailable mandatory type
cannot be handled by discarding jobs. All original totals stay fixed.

Exact LP separation uses the original recipient ranks with polynomial
submodular minimization. Feasible rational witnesses and all cap/row
descriptions have polynomial bit length in the stated exact-oracle
model. Counts are bounded by the original resource totals.

## 6. One full-total rounding and the (1+epsilon) bound

Let x be a feasible fixed-profile fractional point. For each machine,
give every occupied big bin its integer total-count cap h_(p,i).
Such a group is an integral polymatroid with rank h_(p,i) on every
nonempty subset and rank zero on the empty subset.

Give the machine's small coordinates their separate upper-prefix
chain from Section 3. All these groups are disjoint; taking their
direct sum over all machines gives one integral machine polymatroid
containing x.

Use the single full-total minimum-cost recovery of Section 2.
It returns one integer schedule x' with every original type total
and cost at most C.

The integral big load on machine p is bounded by

\[
 \begin{aligned}
 \sum_i \mu_i T\,h_{p,i}
   &\le T\sum_i(\lambda_i+\delta^2)h_{p,i}\\
   &\le T L_p+\delta^2 T K\\
   &\le T L_p+\delta T.
 \end{aligned}
 \tag{PS12}
\]

This only uses upper caps. If rounding uses fewer big units than
the profile permits, its big load is smaller; there is no missing
lower-count constraint.

The fractional small load is at most (1-L_p)T and the largest
permitted small time is at most delta*T. By PS8 its integer load is
at most (1-L_p)T+delta*T. Adding this to PS12 yields

\[
                 \operatorname{load}_{x'}(p)
                    \le(1+2\delta)T=(1+\epsilon)T.
 \tag{PS13}
\]

All types are rounded jointly, including types that are big on one
machine and small on another. No recipient polymatroid is duplicated,
no cost is split between independent roundings, and no mandatory
assigned unit is discarded.

## 7. Every full-T schedule supplies valid profiles

Suppose an original integer schedule has makespan at most T and cost
at most C. On each machine let h_(p,i) be its actual number of assigned
big units in bin i.

Every big unit is strictly larger than delta*T. Therefore the total
number of big units is strictly smaller than 1/delta, and in particular
at most K=floor(1/delta). This remains true for multiple units of a
single type; no identity information is required.

The original big load is at least T times the sum of its bin lower
endpoints, so L_p<=1. The remaining small load is at most T minus
the actual big load, and hence at most (1-L_p)T. Thus the unchanged
original schedule is feasible for the fixed-profile LP associated
with these actual bin counts.

All its occupied bins appear in the finite input grouping from
Section 4. A full-target profile is never lost by omitting empty bins.

Enumerating all valid profiles consequently succeeds with makespan
at most (1+epsilon)T whenever the full target T is feasible. If every
profile LP fails, OPT>T. A weak success is not asserted to prove
full-T feasibility.

## 8. Exact occupied-bin enumeration with polynomial delay

For one machine, order its occupied bins deterministically. A
depth-first enumerator stores the current binary count vector,
the partial count s and the rational partial lower load L.
At the next bin of lower endpoint lambda>0, enumerate exactly

\[
           0\le h\le
             \min\left\{K-s,\
                    \left\lfloor\frac{1-L}{\lambda}\right\rfloor
                 \right\}.
 \tag{PS14}
\]

Update s and L and recurse. Every generated partial state satisfies
both monotone inequalities in PS11 and can be completed by assigning
zero to all later bins. Thus there are no dead partial subtrees.
Every valid profile appears exactly once.

At each fixed depth, distinct partial vectors have distinct
all-zero completions. Hence if a machine has m occupied bins and
p valid profiles, its entire enumeration tree has at most
(m+1)p nodes. The same reasoning gives polynomial delay and
polynomial amortized work per output. Binary counters are advanced
only across actually generated children.

The product of the machine profile families is streamed by nested
enumerators, or by one combined depth-first traversal. At each
partial global state, completing every remaining bin by zero gives
a valid profile on every remaining machine. The total traversal
overhead is polynomial in the explicit pair ground per full global
profile.

The counters h, K, B and bin indices have O(log(1/epsilon)) bits
apart from ordinary input and target bits. Rational endpoints and
partial sums also have polynomial encoding. The number of stored
coordinates is the original number of occupied input bins, not B,
K, or the total number of resource units.

This establishes all-input enumeration bounds even when every LP
fails. It also establishes polynomial workspace for a binary-small
epsilon, without an accuracy-sized table.

## 9. Two complete profile-count bounds

First, ignore the weighted inequality L<=1 and include all B bins.
The number of nonnegative count vectors with sum at most K is

\[
                              \binom{B+K}{K}=C_\epsilon.
 \tag{PS15}
\]

Every occupied-bin valid profile is one such vector, with zeros
in absent bins. This proves the first bound in PS5.

For the stronger bound, let

\[
                              n=\lfloor\delta^{-2}\rfloor.
\]

Since K=floor(1/delta), we have n<(K+1)^2. Moreover

\[
         \lambda_i=\delta+i\delta^2
                      \ge\delta^2(K+i).
\]

Therefore every valid profile satisfies

\[
                             \sum_i(K+i)h_i\le n.
 \tag{PS16}
\]

Its count vector injects into an integer partition of total at most n:
use h_i parts of size K+i. Different indices give different positive
integer part sizes, so this map is injective. Missing bins merely
restrict the allowed parts.

Here is a self-contained upper bound on the number p_(<=n) of all
integer partitions of total at most n. For any t>0, the convergent
partition generating function gives

\[
 p_{\le n}
       \le \exp(tn)\prod_{j\ge1}(1-\exp(-tj))^{-1}.
 \tag{PS17}
\]

Indeed each partition of weight at most n contributes at least
exp(-tn) to the product. The logarithm of the product equals

\[
 \sum_{\ell\ge1}\frac{1}{\ell(\exp(t\ell)-1)}
       \le\frac1t\sum_{\ell\ge1}\frac1{\ell^2}
       \le\frac2t.
 \tag{PS18}
\]

The first inequality uses exp(y)-1>=y. For the last, bound the first
term by one and the remaining decreasing sum by the integral of
x^(-2) from one to infinity. All series have nonnegative terms,
so their interchange is valid.

Choose t=1/(K+1). Because n<(K+1)^2, PS17--PS18 give

\[
                         p_{\le n}\le\exp(3(K+1)).
 \tag{PS19}
\]

This is an analysis-only bound; the algorithm neither evaluates
an infinite product nor computes partition tables. Combined with
the pruned enumerator of Section 8, it bounds actual enumeration
work by exp(3(K+1)) times a polynomial per machine family.

There are at most exp(3q(K+1)) global profiles. Since K<=2/epsilon,
this proves PS1 and the second bound in PS5. Merely checking L<=1
after enumerating all unweighted compositions would not establish
this sharper time; the monotone partial-load pruning in PS14 is
part of the algorithm.

## 10. Initialization and the zero target

Before choosing a load target, minimize assignment cost over the
original resource bases on eligible pairs, keeping all original n_j.
If full totals are unavailable or their minimum cost exceeds C,
declare the original instance infeasible even with unbounded load.
Otherwise keep an actual integral minimum-cost assignment as an
initial feasible schedule.

When N=0, the empty schedule is optimal. For N>0, test makespan zero
exactly by retaining only pairs of processing time zero and again
minimizing cost while preserving every original type total. If this
succeeds, return its load-zero schedule.

This test is needed even when the initially chosen minimum-cost
schedule has positive load: another budget-feasible assignment could
have zero load. If the zero test fails, OPT>0. The profile construction
is invoked only for T>0, so it never divides by a zero target.

## 11. Exact one-sided target optimization

Choose a positive rational grid g dividing all positive finite
processing times. A common denominator followed by an integer gcd
of the scaled numerators suffices. Its bit length is polynomial in
H. Every integral schedule load, and hence OPT, lies in
g times the nonnegative integers.

After failure at zero, initialize a certified lower target L=0
and an upper grid target U equal to the makespan of the retained
budget-feasible schedule. Retain that actual schedule as the initial
weak output. It has load U<=(1+epsilon)U.

At each grid midpoint T, run all profile LPs. A total failure implies
OPT>T and raises L to T. A weak success supplies an actual schedule
of load at most (1+epsilon)T, lowers U to T, and saves that schedule.
Every failed lower endpoint remains strictly below OPT, regardless
of nonmonotonicity in weak successes.

At adjacent grid targets U=L+g, integrality implies U<=OPT. The saved
schedule then has load at most (1+epsilon)U<=(1+epsilon)OPT.
There is no additional approximation loss from optimization.

The initial upper load is at most N times the largest eligible finite
processing time. Consequently the number of target calls is polynomial
in the original binary data and the grid encoding. All profile
arithmetic at these targets has polynomial bit length in
H_epsilon.

## 12. Complete time and space

At each target, grouping the actual pair coordinates into occupied
bins is polynomial in H_epsilon. The streamed enumeration
visits at most the smaller of the two PS5 profile-count bounds,
up to polynomial traversal work. Every fixed-profile LP, prefix
construction, full-total intersection and cost minimization is
polynomial in that same encoding.

Polynomially many target calls preserve PS1 and PS5. The bound is
uniform on all inputs, including infeasible targets, unsuccessful
profiles, zero capacities and all resource-mask rank failures.

Only the current profile counters, exact LP/intersection workspace
and the best actual schedule need be stored. All have polynomial
encoding in H_epsilon. Neither the bin universe, the collection
of profiles, a partition table, nor the individual resource units
are materialized.

## 13. Scope, relation to earlier results, and novelty boundary

The result allows arbitrary machine-dependent processing times,
arbitrary integral recipient-polymatroid bases, binary multiplicities,
eligibility restrictions, and one exact assignment-cost budget.
Machines themselves are fixed available locations. This is not an
optional active-machine-basis theorem, and no job is optional.

The earlier bucket-label theorem remains useful at coarser accuracy:
it gives smaller explicit bases such as 2^q for factor 5/3. This
profile scheme supplies the stronger quality endpoint for every
fixed epsilon, with a larger accuracy-dependent base. Its use of
multiple big-bin caps is outside the one-big-group template whose
analysis limit was three halves.

The inherited two-size oracle barrier below factor three halves
restricts polynomial or corank-FPT algorithms with its original
parameterization. Its hidden-set bound is at most 2^q, so it does
not rule out the present F(q,epsilon) polynomial-time scheme.
No optimality of the PS1 exponential dependence is inferred.

Ordinary unrelated scheduling already has fixed-machine approximation
schemes, and cost-preserving additive upper rounding is classical.
The present proof concerns the stated full oracle polymatroid model,
the exact one-budget guarantee, binary supplies, and polynomial space.
An exhaustive literature comparison is needed before any publication
priority claim. This manuscript makes no such claim and carries no
formal-verification claim.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
