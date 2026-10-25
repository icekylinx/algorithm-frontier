# Verification note

**Curated source path:** `sources/checkpoint-o/two_size_makespan_large_rank_independent_audit.md`

The source audit follows.

# Independent audit of the large-job-parameter scheduling transfer

**25 October 2026. Complete wrapper review passed.**

The reviewed manuscript is
`two_size_makespan_few_large_jobs_transfer.md`, together with the exact
and large-quota arithmetic in
`unit_quota_three_transfer_and_discrete_time_gate.md`.
The conclusion is the stated deterministic 5/3 makespan approximation
in 2^{O(h)}poly(H), where h is the total number of large-job units,
and the separately promised fine-small-job rank-quasipolynomial result.
This is an internal independent review, not external peer review or
formal verification.

## 1. The aggregation and easy branch have the required scope

An integral schedule chooses bases of the small- and large-size
polymatroids. When individual job objects are supplied, integral
polymatroid sum decomposition recovers their assignments from aggregate
bases. The rank h=f_b(P) counts all mandatory large units and does not
depend on a trial makespan target. It can be much smaller than the
number q of machines.

The public additive rounding theorem used in the easy branch was checked
directly in Bamas et al.,
[arXiv:2307.08453v1, Theorem 23](https://arxiv.org/html/2307.08453v1).
It states the T+maximum-job-size guarantee from the assignment LP, and
its proof explicitly uses the job polymatroids. Thus it applies to the
general oracle model here, rather than only to explicit ordinary job
lists. When a<=T/2, its output makespan is at most 3T/2. Assignment-LP
separation uses the supplied rank oracles and paid submodular
minimization; binary multiplicities need not be expanded.

If h=0, checking a small-job base under the uniform integer bound
floor(T/u) decides the one-size target exactly. Zero total job rank
and target zero have their separate trivial handling.

## 2. Hard-branch cap tests are sound target certificates

When a>T/2, every target-T schedule puts at most one large unit on
each machine. The unit-box restriction of the large polymatroid must
therefore retain total rank h. The small polymatroid restricted by
c=floor(T/u) must similarly retain its original total rank. If either
rank drops, no target-T schedule exists. If T<a and h>0, target
infeasibility is immediate.

After the cap tests, the large Boolean polymatroid is a matroid M_b of
rank h. A basis of it is an original large-job base because it is
originally feasible and has the original total rank. Necessarily h<=q
on every successful hard-branch cap test.

Let g_s be the capped small rank. Since every singleton marginal is
at most c, the complemented rank

\[
 \bar g_s(S)=c|S|+g_s(P\setminus S)-g_s(P)
\]

is normalized, monotone, integral and submodular. Base complementation
y=c*1-x_s is exact in both directions. Every dual independent vector
has coordinate at most c, making its eventual complement nonnegative.
The cap and dual rank operations have polynomial binary oracle cost.

## 3. The unit target keeps all rounding directions correct

Put t=a+c u-T and K=ceil(t/u). Since T-u<c u<=T and a>u,

\[
                    0<a-u<t\le a\le T.
\]

Moreover t<=c u because a<=T, so K<=c. A feasible target schedule has
large-recipient basis I in M_b. At each p in I, the small-job complement
satisfies y(p)>=t/u and is integral, hence y(p)>=K. This gives a
K-unit basis promise for the dual recipient polymatroid.

The exact unit theorem returns b=ceil(K/3) units to a player basis of
rank h, or soundly rejects that K-unit promise. A rejection therefore
certifies OPT>T. Its exponent is in h, with q remaining in the
polynomial explicit-input factor. No enumeration of h-machine
subsets or numerical capacities is hidden in this call.

## 4. Base extension yields a legal integral schedule

Extend the returned dual independent count vector coordinatewise to
an integral dual base. This can be done by ordinary integral
polymatroid augmentation, batching numerical increments; increasing
the vector preserves its lower quota on I. Complement it to obtain
the capped small base. The total-rank check makes that vector an
original small-job base. The large vector is 1_I and is likewise an
original base.

Machines outside I have load at most c u<=T. Machines in I have load
at most

\[
           T+t-bu\le T+2t/3\le5T/3,
\]

because K u>=t and b>=K/3. All comparisons use the ceilings in the
correct direction, including small K. The result is an actual integral
schedule, optionally followed by paid original-job decomposition.

## 5. The one-sided target search does not require monotone success

All integral loads lie on a common rational grid with polynomial-bit
denominator. An arbitrary pair of feasible bases gives a polynomial-bit
upper target, and a target below the positive optimum gives a lower
endpoint. Every algorithmic failure certifies that its target is below
OPT. Every success returns a schedule bounded by the stated factor
times its trial target, even if that target itself was not feasible.

Binary search can therefore keep a lower failed endpoint and a successful
upper endpoint. At adjacent grid values, the lower bound is below the
grid-valued optimum, so the successful upper target is at most OPT.
Keeping the best returned schedule gives the desired multiplicative
guarantee. This invariant is valid without assuming the algorithm's
success decisions are monotone.

## 6. The fine-small-job promise pays the quasipolynomial gap

For 0<eta<=1 and u<=eta T/18, the hard branch gives

\[
 t/u>T/(2u)-1\ge9/\eta-1
                         \ge2(3+\eta)/\eta.
\]

Thus K satisfies the large-quota hypothesis of the explicitly stated
unit-core corollary with b=ceil(K/(3+eta)). Its cover gap divided by
the cover coefficient is at least a constant times eta; the inherited
rank-quasipolynomial signature is applicable. Reconstruction gives

\[
          T+(1-1/(3+\eta))t\le(2-1/(3+\eta))T.
\]

For optimization, the promise u<=eta OPT/18 permits restricting the
target grid to T>=18u/eta. The preceding grid point is strictly below
OPT, while an arbitrary feasible upper schedule lies above OPT. Every
actual queried target satisfies the size promise. This avoids an
unpaid exponential small-quota call inside the claimed time bound.

The ratio is at most 5/3+eta/9, but this is a promised size regime.
The critical K=4, b=2 unit case has only a 3/h growth gap and is not
automatically covered by a uniform positive approximation error.

## 7. The comparison and parameter limitations are retained

The new assertion is a constructive bound with exponent h and the
arbitrary job-polymatroid oracle scope. It is not a claim that 5/3 was
previously unknown as an ordinary restricted-assignment integrality-gap
or estimation coefficient. Nor is it a polynomial-time 5/3 result on
unrestricted h. The simpler fixed-accuracy exponential-in-q enumeration
baseline does not imply the exponent h, since directly choosing h
large-unit recipients costs q^{Theta(h)} in general.

The independent below-3/2 scheduling oracle construction concerns the
same h parameter in the full polymatroid oracle model. It leaves the
interval between 3/2 and 5/3 open and does not make the present upper
bound optimal or establish hardness for explicit ordinary job lists.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
