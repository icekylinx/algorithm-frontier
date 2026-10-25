# Proof note

This file is the curated proof record for the result in `README.md`. The original source note follows.

**Original source:** `sources/checkpoint-q/many_small_sizes_workload_makespan_transfer.md`

# Arbitrary small sizes through workload aggregation and per-machine rounding

**25 October 2026. Scheduling extension with two independent internal mathematical reviews.**

The rank-dependent unit-quota technique extends beyond exactly two job
sizes. Keep the largest-size job class integral, aggregate every other
class as divisible workload, use the new unit algorithm on its dual,
then round only those smaller jobs. Artificially refining the workload
unit makes the quota large enough for the quasipolynomial search. This
does not remove the original integer-quota gate for free: the final
schedule pays an explicit additive largest-small-job error.

## 1. Model and guarantee

There are q machines and integral job polymatroids on those machines.
Each supplied job type has a common positive rational size p_j and a
value-oracle rank f_j. A schedule chooses an integer base x_j of every
job polymatroid. All counts and ranks are binary encoded; aggregation
and original-type decomposition are paid polynomial oracle operations.

Let a be the largest positive job size with nonzero required total rank.
Aggregate all a-sized jobs into one polymatroid f_b and put

\[
 h=f_b(P),\qquad
 u=\max_{j:p_j<a,\ f_j(P)>0}p_j,
 \tag{W1}
\]

with u=0 if there are no smaller jobs. Thus h counts units of the
largest job size. The smaller jobs may have arbitrarily many different
sizes and arbitrary integral polymatroid constraints.

For every rational 0<eta<=1, define

\[
                         \alpha_\eta=2-\frac1{3+\eta}.
 \tag{W2}
\]

The deterministic construction returns an integral schedule with

\[
 \boxed{\quad C_{\max}\le\alpha_\eta\,\mathrm{OPT}+u\quad}
 \tag{W3}
\]

in time

\[
 \operatorname{poly}(H)
 \min\{2^{O(h)},(h+1)^{O((1+\eta^{-1})\log(h+1))}\}.
 \tag{W4}
\]

H pays all input bits, numeric scaling, original and derived oracles,
deterministic submodular minimization, decomposition and rounding.
Wrapper space is polynomial, plus oracle workspace. Numerical workload
units are never expanded.

Combining with the public polynomial two-approximation gives the
unconditional bound min{2 OPT, alpha_eta OPT+u}. Under the explicit
size-gap condition u<=epsilon OPT, (W3) gives factor

\[
                  \alpha_\eta+\epsilon
                      \le\frac53+\frac\eta9+\epsilon.
 \tag{W5}
\]

This is a general-many-sizes statement with an additive error or a
stated size-gap promise. It is not an unconditional near-5/3 result
for arbitrary job sizes. For exactly two sizes, the earlier exact
5/3 rank-exponential theorem remains stronger in its own regime.

## 2. The per-machine form of the public rounding lemma

The proof of Bamas et al., Theorem 23, establishes the following form.
Given fractional bases x_j of integral job polymatroids, with smaller
job sizes p_j<=u, one can compute integer bases x'_j such that for
**each** machine p,

\[
                   \sum_jp_jx'_j(p)
                      \le\sum_jp_jx_j(p)+u.
 \tag{W6}
\]

The printed theorem states a uniform makespan bound, but its proof
tracks the load difference Delta_p separately on each machine. Ordering
the job sizes and using its cumulative-ceiling construction gives

\[
 \Delta_p\le\sum_j(p_j-p_{j+1})R_j\le p_1\le u,
             \qquad 0\le R_j\le1.
\]

The integral solution is obtained by the stated integral polymatroid
intersection routine. Thus (W6) is a direct consequence of the checked
per-machine proof, not an assumption that a uniform-load theorem
automatically preserves arbitrary residual capacities.

The source is
[BLMRS23, Theorem 23 and its proof](https://arxiv.org/html/2307.08453v1),
especially the displayed Delta_i calculation. Proposition 9 and its
appendix proof supply aggregation and polynomial integral decomposition.

For completeness, the first independent audit supplies a direct proof
of the precise rounding interface. Sort the smaller sizes as
`p_1 >= ... >= p_m > 0` and use the ground set of pairs `(p,j)`.
One integral polymatroid is the direct sum of the original f_j.
For each machine define `C_(p,j)=ceil(sum_(l<=j) x_l(p))`. A second
integral polymatroid has rank

\[
 B(S)=\sum_p\max\{C_{p,j}:(p,j)\in S\},
\]

with empty maxima zero. Its independent polytope is exactly the set
of nonnegative vectors satisfying the nested prefix bounds
`sum_(l<=j) y_l(p) <= C_(p,j)`. The maximum of nonnegative element
weights is submodular, so this is a valid integral polymatroid.
The fractional original vector belongs to both polymatroids and has
the full required total count. Integral polymatroid intersection
therefore returns a common integer vector with that total, and each
original job component is a base. Telescoping the weighted prefix
bounds, with `p_(m+1)=0`, gives

\[
 \sum_j p_j y_j(p)
 \le\sum_j(p_j-p_{j+1})C_{p,j}
 \le\sum_jp_jx_j(p)+p_1.
\]

This proves (W6) independently on each machine. The pair ground set
has only q*m elements and no numerical job-copy expansion is needed.

## 3. A fine workload unit with polynomial encoding

Choose a common rational grid g=1/Q such that every original job size
is an integer multiple of g. The product of the input denominators
is a valid Q and has polynomial bit length. All integral schedule
loads, hence OPT, lie on this grid. Target search uses T in g Z.

Let

\[
             L=\lceil18/\eta\rceil,
             \Delta=g/L,
             m_j=p_j/\Delta\in\mathbb Z_{>0}.
 \tag{W7}
\]

Define the smaller-job workload polymatroid

\[
                       F(S)=\sum_{j:p_j<a}m_j f_j(S).
 \tag{W8}
\]

It is integral, normalized, monotone and submodular. Its oracle simply
evaluates the supplied ranks and a binary weighted sum. Each original
small job unit contributes m_j units of conceptual workload. This is
an algebraic polymatroid scaling, not an enumeration of those units.
Every m_j and every computed rank has polynomial encoding length in H.

For a target T on the original grid, c=T/Delta is an integer. Thus no
floor loss is introduced when bounding a machine's small workload by c.

## 4. Target preprocessing and the rank-h player matroid

If the largest size satisfies a<=T/2, apply the public assignment LP
and rounding to all jobs. Infeasibility of the relaxation rejects T;
otherwise the schedule has load at most T+a<=3T/2, which satisfies
(W3) at this target. If T<a and h>0, the target is infeasible.

In the remaining branch T/2<a<=T, a target-feasible schedule assigns
at most one largest-size unit per machine. Cap P(f_b) at one per
coordinate and check that its total rank is still h. Otherwise reject
T. The resulting Boolean matroid M_b has rank h.

Cap the workload polymatroid P(F) at c on every machine, obtaining
rank G. Check G(P)=F(P); failure again certifies that no target-T
schedule exists. A true schedule's small workloads are an integer
base of F under this cap, so the check is necessary.

Dualize the capped workload polymatroid with respect to c*1:

\[
                  \bar G(S)=c|S|+G(P\setminus S)-G(P).
 \tag{W9}
\]

This is an integral polymatroid with polynomial count-oracle access.
Its bases are complements c*1-w of the capped workload bases.

## 5. The target promise is a large integer quota

Suppose the target T is feasible. Its largest-unit recipients form an
M_b-basis I. If w is its smaller-job workload base, then for p in I,

\[
                     a+\Delta w_p\le T=c\Delta.
\]

Hence the dual base y=c*1-w supplies

\[
                        K=a/\Delta
 \tag{W10}
\]

units to every p in I. This K is integral because a lies on the original
grid. Since a/g>=1,

\[
                     K\ge L\ge18/\eta
                                \ge2(3+\eta)/\eta.
\]

Therefore the independently proved large-quota unit theorem applies
with output

\[
                      b=\lceil K/(3+\eta)\rceil
 \tag{W11}
\]

and a uniform Omega(eta) layer-growth parameter. It either returns an
M_b-basis I and a dual-independent count vector y giving at least b
units on I, or soundly rejects the target promise. Its nonlinear time
is in h, as in (W4).

Artificial refinement has made this **workload** quota large. It does
not assert that original indivisible small jobs can be subdivided in
the final schedule. Their integrality is restored, and its cost paid,
in the next section.

## 6. Fractional reconstruction followed by paid integral rounding

Extend y to an integral base of P(bar G), and put w=c*1-y. This is an
integral base of G and, by total-rank preservation, of F. Its workload
is at most T on all machines and at most

\[
                 T-b\Delta\le T-a/(3+\eta)
 \tag{W12}
\]

on every machine in I.

Decompose w into integer bases w^j of the scaled polymatroids m_j f_j,
using the polynomial integral polymatroid decomposition primitive.
Set x_j=w^j/m_j. Then x_j is a **fractional** base of the original
smaller-job polymatroid f_j, and its actual total workload on machine p is

\[
                  \sum_jp_jx_j(p)=\Delta w_p.
 \tag{W13}
\]

Apply (W6) only to these smaller jobs. Keep the largest-size allocation
1_I fixed and integral. On a machine in I the final load is at most

\[
 a+T-a/(3+\eta)+u
       =T+(1-1/(3+\eta))a+u
       \le\alpha_\eta T+u.
 \tag{W14}
\]

On other machines it is at most T+u, also within this bound. All job
types now have integer base assignments; none of their original
polymatroid constraints was replaced by a fractional final allocation.
Recovering separately supplied same-size original components, when
needed, is another paid integral decomposition.

## 7. Optimization and bit complexity

This target procedure either certifies OPT>T or supplies a schedule
of load at most alpha_eta T+u. Target zero and empty job systems are
handled separately. An arbitrary feasible set of job bases supplies
a successful upper grid endpoint. The one-sided grid search keeps a
failed lower target and a successful upper target with its actual
schedule. At adjacent grid points, the upper target is at most OPT,
because OPT itself is on the grid and failures are sound. Thus (W3)
follows. No monotone-success assumption is made.

The grid range, scaled ranks, workload decomposition and rounded
solutions have polynomial bit length. Every rank query in G or bar G
uses paid submodular minimization on q machines with polynomial-bit
modular terms. L and m_j enter numeric bit lengths, not a count of
explicit job copies. The number of inner augmentation states is the
unit theorem's function of h and eta. All outer target trials and
reconstruction operations add only polynomial input factors.

If only one positive job size exists, checking a polymatroid base under
coordinate cap floor(T/a) solves the target exactly in polynomial time.
If no largest-size units remain after removing zero-rank types, the
ordinary additive rounding branch suffices. These cases avoid a
meaningless maximum over an empty smaller-job set.

## 8. Comparison and limits

This extends the new rank-h scheduling technique to arbitrary smaller
sizes by using a classical workload polymatroid and an explicitly paid
rounding loss. The public general job-polymatroid baseline is a
polynomial two-approximation; its two-value 7/4+epsilon guarantee must
not be cited as an arbitrary-many-values theorem.

For exactly two sizes, the earlier 5/3 rank-exponential result, and
its no-additive-loss fine-size quasipolynomial branch, remain available.
The present theorem has a different advantage: the small job sizes may
be numerous and unequal, and the search can deliberately refine a
divisible workload unit while keeping its capacity representation binary.

No uniform ratio below two is asserted without the displayed additive
term or a sufficient size-gap condition. No claim of exhaustive
publication priority is made. The full proof passed the two independent
internal reviews in `many_small_sizes_workload_independent_audit.md`
and `many_small_sizes_workload_second_audit.md`. These reviews cover
the workload decomposition, per-machine rounding interface, binary
arithmetic and target search. They are not formal verification or
external peer review.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
