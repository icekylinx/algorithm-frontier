# Verification note

**Curated source path:** `sources/checkpoint-o/two_value_large_cover_factor_two_independent_audit.md`

The source audit follows.

# Independent audit of the large-cover factor-two allocation theorem

**25 October 2026. Full independent mathematical review of F1--F13.**

Reviewed manuscript:
`two_value_allocation_large_cover_two_transfer.md`.

The theorem passes this review. For compulsory players, at most two
intrinsic positive values, and arbitrary integral recipient
polymatroids, it gives a deterministic factor-two allocation in
(27/4)^nu poly(H) time and polynomial workspace. The optional
coloop reduction of nu is valid. The strict-below-two value-oracle
barrier uses the same parameter and is also valid.

The core reduction needs integer resource counts in its target
promise, but not an integer configuration LP. Its large-target branch
uses all-player fractional feasibility and additive rounding. Neither
part uses the ordered-layer local-search proof or its collapse
invariants. This separation is useful when tracking dependencies.

## 1. The model restrictions needed by the proof are explicit

Every original player is compulsory. Resources have common intrinsic
values, so a given type has the same value at every recipient. There
are no additional local bundle constraints. Recipient feasibility is
the integer polymatroid independence condition for each type.

Under these assumptions, extending any independent resource vector
to a base cannot hurt the objective: values are nonnegative, and
there is no local upper constraint coupling different types. Thus
the independent-vector and full-base formulations have the same
max-min optimum. Integer sum decomposition restores original types
after aggregating all resources with the same intrinsic value.

This equivalence would require another argument in a model with
additional local restrictions or optional original players. The
manuscript does not claim either extension. In particular, its
all-player additive LP branch is not silently applied to the
optional-basis allocation problem.

## 2. The additive lower-rounding interface is correct

The proof uses a per-player additive bound, not just a statement
about the minimum of a previously rounded solution. For a resource
rank f, set z(p)=f({p}) and

\[
                 g(S)=z(S)+f(P\setminus S)-f(P).
\]

This is normalized and submodular. Its marginal when p is added to
S is z(p) minus a marginal of f, which is at most f({p})=z(p).
Therefore g is monotone and integral. Its singleton ranks are at
most z(p), so every g-independent vector is coordinatewise at most z.

The affine map y=z-x takes B(f) exactly to B(g). Indeed, when
x(P)=f(P), the complement inequality x(P minus S)<=f(P minus S)
is equivalent to y(S)<=g(S), and total ranks match. Conversely,
for y in B(g), nonnegativity of x=z-y follows from the singleton
bound. Its total is f(P), and

\[
 y(A)=g(P)-y(P\setminus A)
        \ge g(P)-g(P\setminus A)=z(A)-f(A)
\]

gives x(A)<=f(A) for every A. This establishes both directions
without assuming that z itself is a feasible resource base.

Apply the previously proved per-player upper-rounding lemma to the
dual bases, with each intrinsic resource value as its job size.
The dual weighted value at each player increases by at most a, the
largest value. Complementing the integer dual bases back therefore
decreases that player's original value by at most a. All original
resource vectors remain integer bases.

The upper-rounding lemma itself has a polynomial-size construction
in `many_small_sizes_workload_independent_audit.md`: direct-sum job
polymatroids are intersected with the polymatroid of integer prefix
ceilings at each player. No resource copies are expanded. This
also verifies polynomial bit complexity for binary capacities.

The public statement was freshly checked in the primary source:
Bamas, Lindermayr, Megow, Rohwedder and Schloeter,
[arXiv:2307.08453v1, Theorem 21](https://arxiv.org/html/2307.08453v1),
which supplies an integral all-player allocation losing at most the
largest resource value from an assignment-LP target. The complement
argument above provides an independent derivation of the interface
used here.

## 3. Extending the large-recipient support preserves the right promise

Fix an integer target allocation of value at least T at every player,
where 0<T<=2a. Let R be all players receiving a positive large count.
The aggregate large vector dominates 1_R. By downward closure,
1_R belongs to P(f_b), and hence R is independent in the Boolean
cap matroid N.

Extend R to any N-basis F. The complement I*=P minus F is a basis
of M=N*. Since F contains all of R, every member of I* received
only small units in the fixed target allocation. Integer counts then
give at least K=ceil(T/u) small units at each such player, so

\[
                         K\mathbf1_{I^*}\in P(f_s).
\]

The direction of containment is important: enlarging R removes
players from the small-only set and cannot introduce a player that
depended on large units. Multiple large units at one player cause
no difficulty, since only one of them is retained when certifying
independence of R.

The dual player matroid has rank q-nu and corank nu. Its rank
oracle is obtained from N by the standard dual-rank formula. The
Boolean-cap rank of f_b is computable by submodular minimization,
so this interface has polynomial oracle cost.

## 4. The integer half-quota and the pure-large boundary

For K>=2, b=ceil(K/2) is strictly below K. The ratio
K/(K-b) is at most three, including the worst small target K=3.
The batched omission theorem therefore applies in time at most
(27/4)^nu poly(H). At K=1, exact Boolean matroid intersection is
used instead of invoking a gap theorem with zero denominator.

A failed core trial proves that no K-unit M-basis exists. Section 3
then proves that the original integer target was infeasible. A
successful trial gives a feasible b-unit small allocation on an
M-basis I. Its complement is an N-basis, so one large unit is
feasible at every other player. Consequently every player receives
at least

\[
                         \min\{a,bu\}\ge T/2.
\]

The inequalities use a>=T/2 and bu>=Ku/2>=T/2 separately. They
do not require a to be an integer multiple of u or bu<=a. Extending
resource vectors or decomposing their sums preserves this guarantee.

If nu=q, M has rank zero and the small-only core is skipped. The
large Boolean basis already covers all players and has value a
per player. This handles targets up to 2a. The manuscript correctly
continues to the large-target branch for optimization; one large
unit per player need not be an optimal allocation when many units
are available.

## 5. Loops, coloops, and resource restriction

Loops of M=N* are exactly coloops of N. If there are z such
players, deleting them from the small-only player ground preserves
the rank q-nu and reduces corank to nu-z. The small resource is
restricted to that ground, without contraction. A successful small
count vector is later extended by zero to the full original set.

The omitted loops of M belong to every complementary large basis,
so they are still served. Recursive deletions in the unit core do
not delete original players from the final allocation: they select
which players are assigned the large side. This distinction closes
the possible ground-set mismatch.

## 6. Large targets use exactly the compulsory-player relaxation

For T>2a, an integer target allocation implies a fractional
all-player assignment-LP solution with the same target. Testing that
LP is polynomial by rank-inequality separation and the explicit
player-value rows. Fractional infeasibility is thus sound integer
infeasibility.

If the LP is feasible, Section 2 produces an integral allocation
of value at least T-a>T/2. At the boundary T=2a, the manuscript's
hard branch also gives T/2. Therefore the combined target procedure
always either returns an actual half-target allocation or proves
OPT<T. It may return a half-target allocation even when T exceeds
OPT; no later step mistakes such a return for exact target
feasibility.

## 7. Maximization search, binary arithmetic, and space

Let gamma divide both rational values. Every integer allocation value
and OPT lies on the gamma-grid. The total available value
V=a f_b(P)+u f_s(P) has polynomial encoding length and bounds the
minimum value of every allocation. A grid endpoint above 2V cannot
have even a half-target allocation, and is also directly certified
infeasible as an original target.

Maintain a successful lower endpoint and an infeasible upper
endpoint. The upper endpoint always remains strictly above OPT.
When the two grid indices become adjacent, the lower endpoint is
at least OPT. Its recorded half-target allocation has value at
least OPT/2. Algorithmic success does not have to be monotone for
this argument; only the one-sided failure implication is used.

The number of target trials is polynomial in the grid-index bit
length. All quotas and supplies remain binary encoded. The hard
branch uses the independently audited batch attempt-tree bound;
the easy branch uses polynomial-size rational LP and polymatroid
intersection. The depth-first core and the paid polynomial-space
oracle primitives give the claimed polynomial workspace.

Zero-rank resources, empty instances and a single positive value
are handled separately. In the single-value case, the all-player
integer quota test f(S)-k|S| is exact, so ordinary binary search
finds the exact optimum. These exits avoid an artificial second
class or an undefined positive target.

## 8. The below-two oracle barrier has the same parameter

Let r=q-c, use small value one and the hidden rank f_A from
`recipient_polymatroid_below_two_oracle_barrier.md`, and use large
value two with the uniform recipient matroid U_(c,q). This large
matroid has Boolean rank nu=c and no coloops. The two resources
provide an allocation of value two: two small units on A and one
large unit on its complement.

Any allocation has at least r players receiving no large unit,
while the total small rank is 2r. Thus the optimum is exactly two.
For a factor strictly below two, integer utilities force every
player's value to be at least two. If I is the no-large set,
then |I|>=r and the small vector uses at least 2|I| units. The
total bound forces |I|=r. Its rank inequality f_A(I)>=2r forces
I=A. Unused resources do not change this conclusion.

The resource oracle differs from the symmetric reference at only
the query A. With two unqueried r-sets remaining, the deterministic
transcript is compatible with either hidden set, while one output
cannot identify both. Hence the worst-case query bound is
binom(q,r)-1=binom(q,nu)-1. Fixing nu above any proposed uniform
polynomial degree and then growing q excludes F(nu) poly(q,H)
oracle time for every strictly better factor. Rank values have
only logarithmic bit length in q.

This is a barrier for arbitrary recipient ranks supplied by value
oracles. It does not prove ordinary NP-hardness or a lower bound
for explicit allowed-recipient lists. It also does not show that
the positive theorem's exponential base is best possible. The
absence of large coloops makes the same construction apply to the
refined parameter nu-z.

## 9. Comparison and review outcome

The primary source's Theorem 4 was also freshly checked: its
polynomial two-value resource-polymatroid guarantee is 4+epsilon.
The present factor two uses a parameterized time regime and does
not give polynomial-time domination when nu is unbounded. The
new manuscript appropriately avoids an exhaustive priority claim.

No gap was found in F1--F13. The delicate points are the support
extension direction, all-player scope of additive rounding, exact
K=1 boundary, zero-extension after deleting dual loops, and the
orientation of the maximization search. Each is accounted for.
This is independent internal mathematical review, not formal
verification or external peer review.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
