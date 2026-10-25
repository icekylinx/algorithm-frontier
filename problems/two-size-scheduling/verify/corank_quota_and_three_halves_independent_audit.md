# Verification note

**Curated source path:** `sources/checkpoint-q/corank_quota_and_three_halves_independent_audit.md`

The source audit follows.

# Independent audit of corank quota branching and exact three-halves scheduling

**25 October 2026. Full independent mathematical review of C1--C19,
the batch improvement B1--B13, and D1--D17.**

Reviewed manuscripts:

* `unit_quota_corank_gap_branching.md`;
* `unit_quota_corank_batch_branching_improvement.md`;
* `two_size_makespan_corank_three_halves_transfer.md`.

All three derivations pass this review. The core algorithm has its own
deficient-set recursion and does not use the ordered-layer allocation
proof. Its factor-two unit-allocation and exact three-halves two-size
scheduling consequences have deterministic time (27/4)^c poly(H) and
polynomial workspace. The 4-to-2 unit promise has time 4^c poly(H).
The former 2^{O(c log c)} one-deletion count is retained below only
to explain the predecessor; the batch count is the current guarantee.

## 1. The deficient set bounds omissions, not matching exchanges

At a recursive node, let Q be the current player ground, M|Q have
the original rank r, and d=|Q|-r. The resource is the restriction
of one fixed integral polymatroid f. If the assignment b*1_Q fails,
exact submodular minimization returns a nonempty S subseteq Q with
f(S)<b|S|.

For any promised t-unit basis I*, the complement Q minus I* has
exactly d elements. Therefore

\[
        t(|S|-d)\le t|S\cap I^*|\le f(S)<b|S|,
\]

which gives the strict inequality (t-b)|S|<td. This is the source
of the bounded branch set. If I* contained all of S, its resource
count on S would be at least t|S|, contradicting deficiency. Thus
every promised basis omits some element of S.

Deleting such an omitted element preserves that same basis, the
player rank r, and the entire t-unit resource promise. This is a
plain deletion of the player ground together with a resource
restriction. No matroid exchange mapping, simultaneous reservation,
or retained-layer invariant is needed.

## 2. The large-witness guard is essential and is correctly included

The promised bound on |S| alone would not prove running time on
instances where the promise is false. A submodular minimizer can then
be large. The algorithm explicitly tests

\[
                       (t-b)|S|\ge td
\]

and immediately rejects the t-unit target when this happens. The
inequality from Section 1 proves the rejection sound. The test uses
integer cross multiplication; equality belongs to the rejection
case because the promised bound is strict.

Consequently the algorithm never branches on an unbounded deficient
set, even during failed scheduling target trials. This is the key
distinction between a promise-only running-time argument and the
complete one-sided algorithm actually needed by the wrappers.

If d=0, every nonempty deficient set triggers the guard. The unique
possible rank-r basis inside Q is Q itself, so this rejection is
also directly valid. If no deficiency exists, b*1_Q is feasible
and any matroid basis can be selected by downward closure.

## 3. Branch completeness and all return semantics

In the remaining case, the algorithm tries every p in S whose
deletion preserves rank r. A promised basis I* omits some p in S,
so the branch deleting that p is never skipped. Its corank is d-1
and it retains I*. Induction proves that a node containing a t-unit
basis cannot reject all its branches.

A successful leaf returns a size-r independent set of M|Q, hence
a basis of the original M. Its resource vector is bounded by the
verified feasible b*1_Q. For any original set A, zero extension gives

\[
                  b|I\cap A|\le f(A\cap Q)\le f(A).
\]

Thus every success is a valid b-unit allocation, whether or not the
t-unit promise held. Every failure proves that the t-unit promise
was false. The algorithm is allowed to succeed on an unpromised
input; neither optimization wrapper treats a success as exact
feasibility of its stronger target.

Removing player-matroid loops initially is safe for exactly the same
reason: no basis uses a loop. This reduces the parameter to the
loop-deleted corank without removing any promised basis. The optional
deletion of a player with f({p})<t also preserves every t-unit basis;
if it destroys rank, target failure is sound.

## 4. Batch omissions, all attempted deletions, and single-exponential time

For comparison, the one-player predecessor has permitted branch size

\[
                B_d=\left\lceil\frac{td}{t-b}\right\rceil-1.
\]

and at most

\[
                   (c+1)\prod_{d=1}^{c}B_d.
\]

attempted computation nodes. Writing R=t/(t-b), this is bounded by
(c+1)R^c c!, giving the old 2^{O(c log(c+1))} consequence for fixed R.
The following stronger certificate replaces that recursion.

For the same deficient set, put m=|S| and

\[
             \ell=m-\left\lfloor f(S)/t\right\rfloor.
\]

Any t-unit basis I* has t|I* intersection S|<=f(S), so it omits at
least ell elements of S. Since 0<=f(S)<bm<tm, one has
1<=ell<=m. Thus ell>d is a sound target rejection, tested before
enumerating any subsets. This remains valid on every unpromised
input. Otherwise

\[
       \ell\ge m-f(S)/t>m-bm/t=m/R,
              \qquad m<R\ell\le Rd.
\]

Enumerate all ell-subsets D of S. At least one of them lies entirely
outside any fixed target basis I*, so that deletion preserves its
rank and resource promise. Each rank-preserving child has corank
d-ell and still uses the restriction of the original resource.
The induction in Section 3 therefore applies to the batch recursion.
If d=0, every deficient set immediately fails the ell>d guard.

Define Gamma(R)=R^R/(R-1)^{R-1}. Here is a direct bound which also
covers the endpoint ell=m without a convention about zero powers.
The term with ell successes in a binomial distribution with success
probability 1/R is at most one, giving

\[
 {m\choose\ell}
     \le R^\ell\left(\frac{R}{R-1}\right)^{m-\ell}
     \le \left(\frac{R^R}{(R-1)^{R-1}}\right)^\ell
     =\Gamma(R)^\ell.
\]

The second inequality uses m<R ell. All bases are positive because
R>1. This is a finite binomial inequality, not an asymptotic estimate.
Equivalently, the author's entropy proof uses the monotonicity
(log Gamma)'(R)=log(R/(R-1))>0.

The accounting must charge rank-destroying attempted subsets as well
as recursive calls. The manuscript does this explicitly: attach every
enumerated D as a child, with a failed rank test represented by a
terminal child of remaining measure d-ell. If T(d) denotes the size
of this augmented computation tree, then

\[
\begin{split}
 T(d)&\le1+{m\choose\ell}(d-\ell+1)\Gamma(R)^{d-\ell}\\
     &\le1+(d-\ell+1)\Gamma(R)^d\\
     &\le(d+1)\Gamma(R)^d.
\end{split}
\]

Terminal nodes obey the same induction. No promised basis is used
anywhere in this runtime proof. In particular, a node whose entire
candidate list destroys player rank is still charged for the whole
list. An iterator for combinations takes polynomial delay and space.

For t=4,b=2, Gamma(2)=4. For t>=2 and b=ceil(t/2), one has R<=3,
so Gamma(R)<=Gamma(3)=27/4. Therefore the current quota and scheduling
runtimes are respectively 4^c poly(H) for the 4-to-2 promise and
(27/4)^c poly(H) for the rounded-half wrappers. The algorithm never
evaluates Gamma numerically; it only calculates integer ell and
enumerates exact subsets. For a general gap, the explicit dependence
on R remains part of the guarantee.

The submodular objective f(S)-b|S| is exact and integral. Its extra
bit cost is logarithmic in b and q. Rank-preservation queries on
restrictions can be implemented by ordinary matroid greedy. All
such costs are polynomial per attempted node in the paid oracle model.
Capacities are not represented by individual unit copies.

A depth-first recursion uses at most c+1 stack levels, each storing
polynomially encoded subsets and branch indices. It need not retain
the whole exponential tree. With the paid polynomial-space oracle
routines, the claimed polynomial workspace follows.

## 5. The one-unit exception and unit optimization

When output quota is one, P(f) intersected with the unit box is a
matroid independence polytope. Its rank formula

\[
                 \min_{A\subseteq S}\{f(A)+|S\setminus A|\}
\]

is computable by submodular minimization. Matroid intersection with
the player matroid therefore finds a one-unit basis exactly or
proves that none exists. This includes t=b=1; the gap recursion
is never invoked with zero denominator.

For unit optimization, the total-resource bound
K*<=floor(f(P)/r) supplies a certified failed upper target index.
At every queried K>=2, success gives ceil(K/2) units, while failure
proves K>K*. At K=1 the exact routine applies. A successful lower
trial and certified upper trial become adjacent on the integer
grid; the latter remains strictly above K*, so the former is at
least K*. Its saved allocation has value at least ceil(K*/2).
No monotonicity of algorithmic success is used.

This optimization is fractional neither in quota nor in output:
the returned service vector is integer. If several unit-value types
were aggregated, standard integral polymatroid decomposition restores
the original types. One can first extend the aggregate vector to
a base, decompose, then delete unnecessary assignments, so there is
no assumption that an independent aggregate vector was already a
base. Arbitrary additional local player constraints are not included
in this primitive.

## 6. The scheduling instance and the fixed original dual

For two sizes 0<u<a, the original counts are integer bases of f_s
and f_b. If the large Boolean cap has rank below h=f_b(P), every
large base has a machine with at least two large units. Therefore
OPT>=2a and the public additive schedule of load at most OPT+a
is already a three-halves approximation. This handles rank loss
and h>q without defining a negative corank or serving too few jobs.

In the remaining hard-target range a<=T<2a, every feasible schedule
has an h-element Boolean large-recipient basis. The Boolean matroid
is fixed throughout this interval. Its nonloops P+ can be used as
the player ground, with corank |P+|-h.

Let C=floor(T/u), and cap the small-job polymatroid at C. If its
total rank drops, the target is genuinely infeasible. Otherwise
form the complement dual on the **full original machine set**:

\[
                 f_T(S)=C|S|+g(P\setminus S)-f_s(P).
\]

This is integral and monotone because g has coordinate cap C.
Its bases are complements C*1-x_s of bases of g. Only afterward
is this fixed f_T restricted to P+ and subsequent recursive grounds.
The manuscript correctly forbids recomputing a new complement dual
on a smaller recursive ground, which would change the resource and
would not follow from the simple promise-preservation proof.

Machines outside P+, and players deleted in a recursive branch,
remain machines in the original scheduling instance. They are
excluded only from large-job selection. Their small-job capacity
is retained through the original dual and final zero extension.

## 7. Feasible-target quota and exact three-halves reconstruction

Write

\[
 \delta_T=a+Cu-T,
 \qquad K=C-\left\lfloor\frac{T-a}{u}\right\rfloor
              =\left\lceil\frac{\delta_T}{u}\right\rceil.
\]

The hard interval and a>u give 0<a-u<delta_T<=a<=T and
1<=K<=C. In a feasible target schedule, each large recipient has
small count at most floor((T-a)/u), so its original dual count is
at least K. This supplies a K-unit basis in the fixed restricted
dual, exactly the stronger promise of the corank theorem.

For K>=2, choose b=ceil(K/2), with K/(K-b)<=3. For K=1, use the
exact one-unit intersection. A quota failure is therefore original
target infeasibility in every case.

On success, zero-extend b*1_I to all original machines and extend it
to an integer base y of f_T. The complement x_s=C*1-y is a base
of g and hence, by the total-rank check, a base of f_s. Each dual
coordinate is at most C, so the complement is nonnegative. The
indicator x_b=1_I is a Boolean-independent vector of total h, hence
a base of f_b. Both original job types remain integral.

Unselected machines have load at most Cu<=T. A selected machine has

\[
 \begin{split}
 a+u x_s(p)
     &\le a+Cu-bu\\
     &=T+\delta_T-bu\\
     &\le T+\delta_T/2\le3T/2,
 \end{split}
\]

because bu>=Ku/2>=delta_T/2. This verifies the exact factor, including
the floor and ceiling boundaries. No fractional small-job rounding
is performed in this branch, so there is no hidden additive u.

## 8. Minimization search and total bit complexity

All original integer schedule loads lie on a common rational quantum
gamma for a and u. The total workload ah+us is a finite, genuinely
feasible upper target on that grid. Its integer grid index has
polynomial bit length, even if the number of small jobs is binary
encoded. Zero is a failed lower target when h>0.

Every failed trial proves T<OPT. Every successful trial supplies an
actual schedule of load at most 3T/2, even if T itself is below OPT.
With adjacent failed-lower and successful-upper grid indices, the
successful target is at most OPT. Its saved schedule therefore has
makespan at most 3OPT/2. This is the correct minimization search
direction and does not assume monotone success choices.

The corank is fixed across the hard interval. Every dual oracle
query calls the original small cap-rank oracle, whose submodular
formula is polynomial; nesting the paid routines remains polynomial
per recursive node. All capacities, deficits and rank values retain
polynomial binary length. The number of target trials is polynomial
in the encoded range. Rank-zero, empty-job and single-size exits
avoid undefined quotas or meaningless finite optima over empty bases.

## 9. Oracle-model approximation thresholds and scope

The hidden-basis construction in
`recipient_polymatroid_below_two_oracle_barrier.md` has
binomial(q,c) indistinguishable possibilities when reparameterized
by corank. A factor below two for the unit allocation forces the
hidden basis; a factor below three halves for the corresponding
two-size schedule forces its hidden complementary set. The supplied
rank values have only logarithmic bit length. Taking a fixed c
larger than any proposed uniform polynomial exponent rules out
F(c) polynomial-ground-size oracle time for these strictly better
factors. This matches the approximation thresholds here, not the
precise exponential base or even the necessity of exponential time
at the attained thresholds.

These are black-box value-oracle statements for arbitrary recipient
or job polymatroids. They do not establish complexity-theoretic
hardness for explicit restricted-assignment instances. The positive
three-halves algorithm does apply to that subclass, but its public
priority and specialized comparisons require a separate source
review.

No gap was found in the three complete manuscripts. The critical guard,
restriction-versus-contraction distinction, one-unit exception,
integer reconstruction, one-sided searches, and batch accounting of
every attempted deletion are all explicitly accounted for. This is
independent internal mathematical review,
without an implementation, formal verification, external peer review,
or an exhaustive publication-priority claim.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
