# Root audit of unit quotas, the large-job scheduling transfer, and oracle bounds

**25 October 2026. Independent internal mathematical review.**

The reviewed notes are
`unit_quota_three_transfer_and_discrete_time_gate.md`,
`two_size_makespan_few_large_jobs_transfer.md`, and
`recipient_polymatroid_below_two_oracle_barrier.md`.
The main new scheduling statement constructs a 5/3 approximation in
2^{O(h)} poly(H) time, where h is the total number of large job units,
for two-size jobs with arbitrary integral job-polymatroid constraints.

These are internally reviewed research derivations. Neither a new
publication priority for the number 5/3 nor external peer review is
claimed. The ordinary-scheduling literature already contains a 5/3
estimation/gap bound and a non-polynomial constructive claim; the
parameter and full oracle model must be compared explicitly.

## 1. Exact quota arithmetic is sound

For unit value u and an integer output quota b, every stored minimal
bundle has exactly b units. After all-center normalization, a singleton
blocker group saves at least one rank unit. Larger groups have at
most (t+1)b units and satisfy (t+1)b<=t(2b-1) for b>=2,t>=2.
For b=1 the normalized singleton-resource case saves the center's rank.
Thus the exact upper coefficient is (2b-1)u.

Under an integer k-unit basis promise, a failed exact available scan
has value at most (b-1)u. The contraction loss proof gives a non-strict
lower coefficient (k-b+1)u. Hence the required strict contradiction is

\[
                    k-b+1>\rho(2b-1),
 \qquad \rho=(r-1)/r.
\]

The algebraic equivalent in the note is correct. At b=ceil(k/3),
the only small-margin residue k=3a+1 has gap (2a+1)/r>0, and the
other two residues have larger gaps. At r=2, b=ceil(k/2) is also
valid. Rank one can be solved exactly.

The same integer arithmetic holds against the newly proved residual-
capacity configuration relaxation: each truncated integer configuration
has at most b-1 units, and its cut bounds the exact lost expectation.
It need not be restricted to the old integer comparison once that
stronger comparator is named explicitly.

## 2. The quasipolynomial quota restriction is necessary for this proof

With d=3-2/r and b=ceil(k/(d+eta)), the gap is at least
k eta/(d+eta)-rho. If k>=2(d+eta)/eta, this is at least half the
first term, while the cover coefficient is at most 3k/(d+eta).
Thus the displayed Omega(eta) growth margin and time bound follow.

For the looser factor 3+eta corollary, use b=ceil(k/(3+eta))
explicitly. The same calculation gives gap at least
k eta/(3+eta)-rho and requires k>=2(3+eta)/eta. Then a fat value
only needs to be at least T/(3+eta). One must not keep the stronger
d+eta output quota while silently weakening the fat-value condition.

At k=4,b=2, the gap is exactly 3/r. For eta<1, a 3+eta value
approximation still requires two units. Hence multiplicative error
does not remove this discrete case; no uniform near-three rank-
quasipolynomial result follows from the present counting proof.

## 3. The all-player exponential-time baseline is a real comparison

For two resource values a>=u>0 and all q players compulsory, if
a<=epsilon T the public additive rounding gives at least
(1-epsilon)T. Otherwise a feasible target allocation can be trimmed
to at most ceil(T/a)<=ceil(1/epsilon) big units per player. Enumerating
those q counts and checking the big vector and the necessary small
count vector in their two polymatroids is sufficient and necessary
for that enumerated choice. Downward closure permits unused resource
capacity; original component allocations are recovered by the paid
aggregation/decomposition primitive.

The scheduling analogue checks a big **base** and whether the small
polymatroid has a base under the remaining per-machine capacity.
These tests use submodular minimization with binary arithmetic.
They justify the stated fixed-accuracy (1+epsilon^-1)^{O(q)} baseline.
It does not replace q by the smaller selected rank or large-job count.

## 4. The scheduling hard branch has exactly rank h

For a makespan target T, if a<=T/2 the public additive rounding gives
load at most T+a<=3T/2. If a>T/2, every target-feasible schedule has
at most one large unit per machine. The Boolean cap of the large-job
polymatroid is therefore the right player matroid.

The cap must preserve the original total rank h=f_b(P). If it does
not, infeasibility of target T is sound. The same is true of c=floor(T/u)
for the small-job coordinate cap. When the checks succeed, the large
Boolean matroid has rank **h**, independent of q, and the capped
small polymatroid has the original small total rank.

Positive h and T<a permit immediate rejection. Otherwise c>=1 and
the small dual rank

\[
 \bar g_s(S)=c|S|+g_s(P\setminus S)-g_s(P)
\]

is normalized, monotone, integral and submodular. Monotonicity uses
the cap c on every primal coordinate. Its bases are precisely the
complements c*1-x_s of capped small bases. All of this is evaluated
through count oracles; c copies per machine are not constructed.

## 5. The target promise and reconstruction give 5/3

Put t=a+cu-T and K=ceil(t/u). Since T-u<cu<=T and a>u,
one has 0<a-u<t<=a<=T. A feasible target schedule supplies a basis
I of the large-job matroid. Its small dual y=c*1-x_s obeys
y_p>=K on I. Restricting y to I is a legal independent allocation
in the dual polymatroid, so the unit-quota theorem applies with
player rank h.

The output b=ceil(K/3) is at least t/(3u). Extend the dual allocation
to an integral dual base, which only increases its coordinates and
can be done by paid polymatroid base augmentation. Set x_b=1_I and
x_s=c*1-y. Total-rank preservation makes these bases of the original
job polymatroids. On non-big machines the load is at most cu<=T.
On big machines it is at most

\[
                 T+t-bu\le T+2t/3\le5T/3.
\]

This is an actual schedule, not an estimate of optimum or a fractional
certificate. Individual job assignments can be obtained by the paid
integral decomposition used in the public aggregation primitive.
The exponential state count is in h; all other work is polynomial
in the complete original input and its numeric bits.

## 6. The fine-small-job branch and target search are paid

If u<=eta T/18 with 0<eta<=1 and a>T/2, then

\[
 t/u>T/(2u)-1\ge9/\eta-1\ge2(3+\eta)/\eta.
\]

Thus K satisfies the large-quota condition for b=ceil(K/(3+eta)).
The allocation time is rank-quasipolynomial in h, and the reconstructed
load is at most (2-1/(3+eta))T. The easy branch remains at most 3T/2,
which is no larger than that ratio.

For optimization under the promise u<=eta OPT/18, start the target
grid at or above 18u/eta. The immediately preceding grid point is
strictly below OPT by that promise. Every actual query is in the
valid size regime. An arbitrary feasible schedule supplies an upper
endpoint of polynomial bit length. Algorithmic failure proves OPT>T;
success supplies an explicit schedule of load at most alpha T.
At adjacent grid endpoints the successful upper target is no larger
than the grid-valued optimum. Monotonicity of the successful-target
set is not required.

The exact 5/3 branch uses the same one-sided search without the size
restriction. Empty job classes and zero-size units are handled by
the stated simpler cases; they do not require a quota formula with
an undefined zero denominator.

## 7. The allocation oracle lower bound is valid

For q>r>=1, the base function

\[
 f_0(S)=\min(2|S|,2r)-\mathbf1[|S|=r]
\]

has nonincreasing nonnegative cardinality increments, hence is a
normalized monotone submodular integer function. Raise only the value
of one hidden r-set A by one. Monotonicity still holds. A potentially
damaging submodular inequality must have union or intersection exactly
A and neither argument equal to A; each such inequality had slack
exactly one, sufficient for the raise. Nested cases cancel the raise.

The hidden A admits two units per selected player. Every other r-set
has capacity 2r-1 and therefore cannot supply two to all its members.
Every r-set admits one unit each, and the total capacity gives optimum
exactly two. Hence a factor strictly below two must return the hidden
A. The value oracle differs from f_0 only at A, so at least
binom(q,r)-1 queries are necessary in the worst case by the two
remaining-unqueried-sets adversary.

This excludes a deterministic f(r)q^c query bound for a uniform
approximation strictly below two: choose fixed r>c and let q grow.
The oracle values have only logarithmic numeric bit length. The
statement is about black-box arbitrary polymatroids, not hidden
information in an explicit graph or a standard complexity assumption.

## 8. The dual scheduling lower bound uses the same parameter

Take q>=r+2, large units of size two with matroid U_(r,q), and small
units of size one with rank

\[
 g_A(S)=2|S|+f_A(P\setminus S)-2r.
\]

This is the box dual of f_A with cap two. It is an integral polymatroid
of rank 2q-2r. A hidden-A schedule assigns large units to A and two
small units to every other machine; its makespan is exactly two.

A schedule with ratio strictly below 3/2 has integral load at most
two on every machine. Every large-unit machine must therefore have
zero small units. Dualizing its small base yields two units on every
large-unit recipient, forcing that r-set to be A. The small rank oracle
differs from its baseline only on P minus A. Thus the same query lower
bound applies with h=r, excluding uniform f(h)poly(q) approximation
strictly below 3/2 in this full oracle model.

This explains a genuine parameterized boundary for the new scheduling
upper bound, but leaves the interval from 3/2 to 5/3 open. It does
not apply automatically to explicitly represented ordinary restricted
assignment, nor to the four-unit-promise/two-unit-output allocation
question. That latter promise is absent from the lower-bound family.

## 9. Primary-source scope and assessment

The external primitives were checked in
[BLMRS23](https://arxiv.org/html/2307.08453v1): Proposition 9 for
aggregation and integral decomposition; Theorems 21 and 23 for additive
resource loss and scheduling load; and the polymatroid-dual constructions
around Lemma 15. The public general job-polymatroid two-size approximation
is 7/4+epsilon in polynomial time.

[Jansen--Land--Maack, SWAT 2016](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SWAT.2016.24)
explicitly proves a 5/3 configuration-LP gap and estimation result in
ordinary two-size restricted assignment. The primary abstract of
[Sengupta's 2025 thesis](https://www.ideals.illinois.edu/items/139520)
reports a non-polynomial 5/3 local search for that ordinary problem;
the full thesis was not inspected because direct retrieval was blocked.
These facts prevent a first-5/3 or first-constructive-5/3 claim.

The root audit finds no unclosed mathematical step in the reviewed
unit quota theorem, rank-h scheduling wrapper, fine-size promise,
derived all-player comparison, or either oracle lower bound. The
positive result's distinguishing claim is its proved dependence on h
and its full arbitrary job-polymatroid model, with its primary-source
and derived baselines retained.
