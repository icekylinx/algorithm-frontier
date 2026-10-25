# Verification note

**Curated source path:** `sources/checkpoint-p/corank_batch_allocation_scheduling_root_audit.md`

The source audit follows.

# Root audit: single-exponential corank branching and three complete applications

**25 October 2026. Complete internal mathematical review; accepted for the next checkpoint.**

This audit covers the current full manuscripts
`unit_quota_corank_gap_branching.md`,
`unit_quota_corank_batch_branching_improvement.md`,
`two_size_makespan_corank_three_halves_transfer.md`, and
`two_value_allocation_large_cover_two_transfer.md`, together with the
hidden-set construction in
`recipient_polymatroid_below_two_oracle_barrier.md`.
The first three were also read independently by two other reviewers.
The two-value compulsory-allocation composition has a separate
independent review. These are mathematical research checks, not
external peer review or a claim of exhaustive publication priority.

## 1. Accepted results and their distinct parameters

Let Gamma(R)=R^R/(R-1)^(R-1), for R>1. The accepted deterministic
gap algorithm returns a player-matroid basis receiving b units per
selected player, or proves that no such basis can receive t units,
for integers t>b>=1. Its time is Gamma(t/(t-b))^c poly(H), where c
is the player corank after loop deletion. Its workspace is polynomial.
The oracle and bit model pays for every rank query, submodular
minimization, decomposition, and rational optimization operation.

The complete applications are:

| Problem | Guarantee against integer OPT | Nonlinear parameter | Time, up to polynomial factors |
|---|---|---|---|
| Unit-value allocation with an arbitrary player matroid and arbitrary recipient polymatroid | at least ceil(OPT/2) units per selected player | loop-deleted player corank c | (27/4)^c |
| Two-size job-polymatroid makespan | at most 3 OPT/2, with no additive small-job term | c = eligible large positions minus large-unit rank, when the Boolean cap retains that rank | (27/4)^c; rank loss is an easy polynomial branch |
| Two-value recipient-polymatroid allocation with every player compulsory | value at least OPT/2 | nu = rank of the large-resource Boolean cap | (27/4)^nu |

The four-unit-promise/two-unit-output subproblem takes 4^c poly(H).
The refinement nu minus the number of large-cap coloops is valid for
the nonempty compulsory-allocation core. These parameters describe
different regimes; no common small-parameter assumption is implicit.

## 2. The batch certificate and the direction of the promise

At a current ground Q of retained player rank r, put d=|Q|-r.
The algorithm separates b times the all-ones vector on Q. If a
deficient set S is found, set m=|S| and

    ell = m - floor(f(S)/t).

The inequalities 0<=f(S)<bm<tm imply 1<=ell<=m. Any t-unit
basis I* inside Q has t|I* intersection S|<=f(S), so it must omit
at least ell elements of S. If ell>d, no such basis exists. This
guard is tested before enumeration and makes the running-time proof
valid on inputs without a promised solution.

If ell<=d, enumerate all ell-subsets D of S. At least one such D
is contained in S minus I*. That branch preserves the same promised
basis, hence passes the retained-rank test. Its remaining corank is
d-ell. This gives a complete induction proving that a promised node
cannot fail. A successful node verifies b*1_Q, then chooses any
player basis within Q, so its output is feasible regardless of the
stronger promise.

The resource is always a restriction of the same original function.
Zero extension is justified by f(A intersection Q)<=f(A). Player
deletion never means resource contraction. In the scheduling
application, the full-ground complement dual is formed once for a
target before any player-ground restriction.

## 3. The single-exponential count charges all work

Put R=t/(t-b)>1. Deficiency implies ell>m/R. The binomial
probability estimate gives

    binom(m,ell) <= R^ell (R/(R-1))^(m-ell) <= Gamma(R)^ell.

This proof includes ell=m directly. Every attempted D is represented
in the computation tree, even when its rank test rejects it without
recursion. Such a terminal child is given remaining budget d-ell.
The induction

    1 + binom(m,ell)(d-ell+1) Gamma(R)^(d-ell)
       <= (d+1) Gamma(R)^d

bounds the entire augmented computation tree. It therefore pays for
all skipped deletions as well as recursive calls. Each call has
polynomial input and bit cost. A depth-first combination iterator
retains polynomial space and never expands binary resource supply.

For t=4,b=2, R=2 and Gamma(R)=4. For t=K>=2 and b=ceil(K/2),
R<=3 and Gamma(3)=27/4. The exact one-unit matroid-intersection
case handles K=1; no division by t-b occurs there.

The numerical constants arise from the algorithm's actual branching
measure. Their optimality has not been established.

## 4. One-sided optimization searches are valid without monotone success

For unit maximization, the direct total-rank bound gives
OPT<=floor(f(P)/r), for r>0. Initialize a zero successful lower
index and an upper integer index strictly above this bound. The
upper index is certified externally and need not be queried: a gap
algorithm may succeed at a stronger infeasible target. Each later
failure still proves that its target exceeds OPT. At adjacent
endpoints, the successful lower target is at least OPT, giving the
claimed half-quota guarantee. Rank zero is handled separately.

For scheduling minimization, total workload supplies a genuinely
feasible upper target, while zero is infeasible when large jobs
exist. All loads lie on a common rational grid. A failure proves
its target below OPT. Adjacent failed-lower and successful-upper
grid indices imply that the successful target is at most OPT. The
saved schedule has the corresponding approximation guarantee.

For compulsory two-value allocation, the manuscript uses an upper
target exceeding twice the total value. No returned half-target
allocation can meet this endpoint, and the original target is also
externally certified infeasible. The maximization orientation is
the same as above. All search ranges have polynomial bit length.

## 5. Exact three-halves scheduling reconstruction

Write a>u>0 for the two sizes, h for large total rank and s for
small total rank. If the large Boolean cap has rank below h, every
legal schedule has a large collision, hence OPT>=2a. Public
largest-job additive rounding supplies OPT+a<=3OPT/2. This covers
h exceeding the number of machines and excludes no input instance.

Otherwise, in a hard target a<=T<2a, cap the small resource at
C=floor(T/u) and check that total rank s is retained. Form, on all
original machines P,

    f_T(S)=C|S|+g(P minus S)-s.

Only afterward delete large-matroid loops from the player ground.
Put delta=a+Cu-T and K=ceil(delta/u). The integer identity
K=C-floor((T-a)/u) proves 1<=K<=C. Also 0<delta<=a<=T.
An original target schedule supplies a K-unit large-recipient basis
in f_T. The core returns b=ceil(K/2) units, or soundly rejects T.

Zero-extend the returned quota vector to P and complete it to an
integer dual base y. Then x_s=C*1-y is an original small base and
x_b=1_I is an original large base. On a large recipient,

    a+u x_s(p) <= T+delta-bu <= T+delta/2 <= 3T/2.

Other machines have load at most T. No fractional small-job rounding
is used in this branch, so no additive u or epsilon term is hidden.
Machines removed only from the player ground remain present in the
original small resource and final base completion.

## 6. Exact factor two for compulsory two-value allocation

Let N be the Boolean cap of the large recipient resource and let
nu=rank N. At a target 0<T<=2a, any original target allocation has
a large-recipient support R independent in N. Extend R to an N-basis
F. Its complement is an N*-basis consisting entirely of players
that had no large unit in that allocation. Each has at least
K=ceil(T/u) small units. This is the required stronger promise.

Apply the corank core to player matroid N* and the small resource.
It returns a basis I receiving ceil(K/2) small units. Its complement
is an N-basis and can receive one large unit per player. Every
player therefore gets at least min(a,u ceil(K/2))>=T/2. The case
nu=q has an empty small-only basis and is served directly by one
large unit per player for this target range.

At T>2a, the all-player fractional allocation relaxation and
largest-unit additive rounding return value T-a>T/2 or reject the
original target. Complement-dual rounding proves the additive lemma:
with coordinate bound z_j(p)=f_j({p}), round the dual fractional
bases z_j-x_j upward with error at most a, then complement back.
The resulting original integer bases lose at most a in every
player's value. This easy branch requires all players compulsory;
it has not been silently applied to a general optional-selection
matroid.

If N has z coloops, N* has z loops. Removing them leaves corank
nu-z while the corresponding forced-large players are served by
the complementary large basis. This proves the optional refinement.

## 7. Threshold lower bounds and what they do not prove

For q>r>=1, the hidden-set resource

    f_A(S)=min(2|S|,2r)-1[|S|=r]+1[S=A], |A|=r,

is integral, monotone and submodular. The unraised cardinality
function has increments 2,...,2,1,1,0,...,0. Raising the single
set A uses exactly the available unit of slack in each relevant
union/intersection inequality. A two-unit r-player basis must be A.
Oracle answers differ from the symmetric reference only at A.

The deterministic transcript argument leaves at least two possible
hidden sets unless binom(q,r)-1 queries have been made. Its corank
form is binom(q,c)-1 for c=q-r. A factor below two for unit
allocation must identify A. Complement duality with sizes 2 and 1
gives a makespan-two instance where any factor below three halves
must also identify A. For the latter, c>=2 ensures the stated
singleton capacities. Adding a large-value-two uniform recipient
resource of rank c gives the compulsory-allocation lower instance:
the r players with no large unit must be exactly A for any output
of value at least two.

Fixing c, or nu, above a proposed uniform polynomial input exponent
rules out F(parameter) poly(H) query bounds for strictly better
uniform factors. Oracle answers have only O(log q) bits.

Thus the approximation thresholds two, three halves, and two match
in their stated arbitrary-polymatroid value-oracle models. These
are not exponential-base lower bounds, ETH statements, or hardness
results for explicit ordinary restricted assignment. No bounded
literature search establishes publication priority. The new
parameterized algorithms also do not dominate public polynomial
algorithms when their parameters are unbounded.

## 8. Public dependency boundary

The aggregation, integral decomposition, and largest-job additive
rounding primitives are the standard polymatroid tools used in
Bamas, Lindermayr, Megow, Rohwedder and Schloeter,
*Santa Claus Meets Makespan and Matroids*, arXiv:2307.08453v1:
<https://arxiv.org/html/2307.08453v1>.
Its Theorem 4 states a polynomial factor 4+epsilon for compulsory
two-value allocation, while Theorems 21 and 23 provide the additive
allocation and scheduling primitives. The new branching proof is
self-contained and does not import a superseded DRZ local-search
claim. The current-version audit remains a separate checkpoint note.

All three complete compositions pass this root review. The ongoing
arbitrary-value and generic packing extensions are separate results
and require their own completed proofs and reviews before inclusion.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
