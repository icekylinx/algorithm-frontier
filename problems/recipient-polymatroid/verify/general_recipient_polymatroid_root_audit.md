# Verification note

**Curated source path:** `sources/checkpoint-p/general_recipient_polymatroid_root_audit.md`

The source audit follows.

# Root audit: arbitrary recipient polymatroids and the factor-four extension

**25 October 2026. Independent internal mathematical review.**

This review covers
`general_recipient_polymatroid_integer_optimum_transfer.md`,
`general_recipient_polymatroid_prefix_four_transfer.md`, and
`recipient_polymatroid_aggregate_configuration_gap.md`.
The combined result is a deterministic factor

\[
 d=\lambda^{-1}+3-3/r
\]

against **integer optimum**, with rank-exponential time at equality
and rank-quasipolynomial time for any positive additional error. It
allows arbitrary integral recipient polymatroids, binary numerical
capacities, an arbitrary player-selection matroid, and the explicitly
paid local downward-closed available-count oracle. This is an internal
proof audit, not formal verification or external peer review.

## 1. Numerical availability is the right whole-block rank increment

For an integral polymatroid f on players, the conceptual natural matroid
has f({p}) indistinguishable-under-permutation service copies in player
p's block. Independent copy sets have count vectors in P(f). Its rank
on a set with counts z is

\[
 R(z)=\min_{S\subseteq P}\{f(S)+z(P\setminus S)\}.
\]

Integral polymatroid box restriction proves this formula and the
existence of an attaining independent subset. The minimization is over
q players, not over all conceptual copies. Deterministic submodular
minimization therefore has polynomial oracle and bit cost.

Replacing z_p by f({p}) gives the rank of W union the whole p block.
Its difference A_p from R(z) is the largest size of a p-owned block
that is independent over W. To see that it is a joint block statement,
partition the rank minimum into sets containing p and sets not
containing p. Increasing z_p by a leaves one minimum unchanged and
adds a to the other. The resulting marginal increases one-for-one
until A_p is reached, and is then constant. Thus **any** a unused
p copies, for a<=A_p, are independent over W.

This corrects the tempting but invalid rule of treating every copy
outside cl(W) as simultaneously available. Individual nonmembership
in a closure alone would not prove that a multiunit block is legal.

## 2. Fixed copy identities need no exponential state

Different players own disjoint conceptual copy blocks. For one player,
all its selected records are reserved. If that player is currently
matched and eligible, its current matching record belongs to an earlier
blocker group and is also reserved. Hence A_p is at most the number
of its unused conceptual copies. Every new record can choose copies
disjoint from every current record of that owner.

Moving a stored free center to a matching record keeps its copies, then
retires its selected record. Removing another record or a higher center
only releases copies. This proves one fixed-universe execution for
the count algorithm. No global relabeling is needed to keep an old
prefix certificate true, and no subset-of-record copy pattern is needed
in the implementation.

All relevant ranks depend only on the count vector. At most O(r)
record count vectors are active. Every count is bounded by a singleton
oracle value; sums add only logarithmically many bits. Positive-unit
minimality pruning removes a type's dispensable units in one arithmetic
batch. These facts justify polynomial work and space per charged state,
even with exponentially large numerical capacities.

## 3. The integer loss lemma is valid for dependent reserved sets

Fix a feasible integral target allocation on a basis I* and restrict
it to the at least w eligible players outside the current eligibility
flat. For one resource let n* be its feasible count vector, W the
reserved copy set, and L=r(W). The contracted block polymatroid has

\[
 g(S)=r(W\cup E_S)-r(W)\ge f(S)-L.
\]

This remains valid when W is dependent. Contraction by its span has
the displayed rank difference; copies already in W contribute zero.
The natural-matroid rank of the whole block union E_S is f(S).

Box restriction of g by n* supplies an integral h<=n* in P(g) with

\[
 h(P)=\min_S\{g(S)+n^*(P\setminus S)\}
                         \ge n^*(P)-L.
\]

Every term in the minimum has that bound because n*(S)<=f(S).
Equivalently, one can start with an independent copy set representing
n* and retain an independent subset after contracting W; at most L
units need be lost. The box argument makes the simultaneous coordinate
bounds explicit.

For every player h_pj<=g_j({p})=A_pj. Combining the retained vectors
across types stays coordinatewise below that player's original bundle,
so local downward-closed feasibility is preserved. A completed failed
lambda-oracle scan bounds its value strictly below B/lambda. Summing
lost value and the per-resource losses at most r(W_j) proves

\[
 \sum_jv_jr(W_j)>(T-B/\lambda)w
\]

when B<=lambda T. The integer optimum is a proof witness only; the
algorithm is not given it. The proof does not assume independent
choices of optimal players or fractional row masses.

## 4. The prefix invariant extends to entire blocks

For every ordered center prefix, maintain U independent over W, now
with |U| equal to its number of service units. The whole new block C
is independent over W by Section 1. A problematic used resource is one
where C is not independent over W union U. At such a resource the new
group contains all records contributing to U. Thus no unmarked copy
remains after completion. At a nonproblematic resource, adding C
preserves additivity; moving any designated subset from U to W also
preserves it. Unused resources only perform the latter move.

The universal reservation induction is therefore valid for every
selected subset without enumeration. At problematic resources it extends
an independent subset of W by the whole C. At other resources C is
independent over the larger matching-plus-selected set.

For a stored center let V consist of its preceding reserved prefix and
its current designated group. If C is independent over V, then prefix
additivity after that center gives

\[
 r(V+C+U)=r(V)+|C|+|U|.
\]

Since r(V+U)<=r(V)+|U|, adjoining C to V+U increases rank by at least
|C|, and at most |C| by cardinality. It is therefore independent over
the whole matching and all preceding centers. This is the required
strong freedom, for an entire multiunit block, not just its elements
one at a time.

After an earliest player exchange every retained center precedes the
incoming center. For a fixed retained prefix, deleting the outgoing
block either shrinks W or shrinks U. Neither can destroy U's old
independence over W. The incoming block is independent over the whole
old W union U, hence over the post-deletion set, and is unmarked.
This proves additivity for every retained prefix, including an internal
prefix of the last retained layer.

All-center normalization, higher-group release, record identity, old
maximality, and signature decrease now have exactly the audited matroid
proof. The group itself is never discarded as a separate mutation.
Every eager release performs a genuine earliest exchange and truncation.

## 5. One lost rank unit suffices for the sharp charge

At a normalized center, a failed whole-block independence test has an
integer rank deficit of at least one. With a singleton designated group,
that deficit must occur at a resource also used by the blocker; otherwise
the inherited availability over the preceding prefix would be contradicted.
Counting both bundles separately therefore overestimates the current
rank increment by at least one unit of that resource's value v_j.

Deleting one unit of type j from a minimal blocker lowers its value
below B, even when it owns several units of j. Thus
value(blocker)-v_j<B. The singleton-group charge is below
2B+min(u,B) when the center is nonsingleton.

If the center itself is a single unit worth at least B, all its current
blockers are single units of that same type. Failed strong release saves
the new unit's rank, leaving charge at most u per blocker. For a
nonsingleton with t>=2 blockers, the existing inequality
(t+1)(B+a)<=t(2B+a), a=min(u,B), pays every bundle. This proves

\[
 \Phi\le\max\{u,2B+\min(u,B)\}|Y|.
\]

Together with the integer lower cover, this establishes the improved
factor-four compact threshold. No one-service-per-player assumption
has been imported into this charge.

## 6. Fat reduction, time and the unit-quota qualification

The Boolean cap P(f_j) intersect [0,1]^P is a matroid polytope, with
rank min_{A subset S}[f_j(A)+|S-A|]. It can be queried by paid
submodular minimization. A locally feasible singleton restriction
remains a matroid. Taking the union of the fat types and complementing
its union with M* gives the usual derived player matroid of rank at
most r.

An integral target allocation supplies the derived all-small promise
by choosing one fat unit for every fat-served player and extending
the corresponding dual-union independent set to a basis. Reverse
decomposition and deletion preserve all recipient and local constraints.
This proof is integer and does not depend on the invalid aggregate LP.

With d=tau+3rho, B0=T/d, and eta0=min(eta,1), choose
B=T/(d+eta0). Then B>=B0/2, u<B0, the cover coefficient is at most
3B, and the target slack is at least eta0 B. Thus gamma=eta0/16 is
safe and yields the stated rank-quasipolynomial signature bound.
All per-state rank work is polynomial in the binary input; the previous
finite-grid target search applies without assuming monotone success.

For unit quotas, the stronger coefficient 2b-1 and the integer residual
bound b-1 are correct. They prove output ceil(t/3) in rank-exponential
time. The three residue-class slack calculations in the manuscript
are correct. At t=4,b=2, however, the margin is only 3/r, so this
does not justify a uniform near-three rank-quasipolynomial statement.

## 7. The comparator obstruction is substantive

For q=Dr, selection matroid U_(r,q), and
f(S)=|S|+D for nonempty S, the aggregate configuration point
x_p=1/D, y_p=(D+1)/D satisfies all stated constraints. Its configuration
value is D+1. The integral optimum is exactly 1+floor(D/r), by the
bound on the r selected players and the matching uniform allocation.
The ratio tends to r for D=rL, L growing.

The construction is already a sum of a free-matroid rank and D rank-one
matroid ranks. Keeping those two supplied types separate rejects the
bad component configuration point; merging them admits it. Therefore
the distinction between integer optimum and a component-level
configuration comparator cannot be dismissed as a representation detail.

## 8. Assessment

The root audit found no unclosed step in the direct compressed
polymatroid construction, its integer-optimum cover, the prefix
normalization improvement to factor 4-3/r, or its positive-error time
bound. The rank-sized aggregate-LP gap is also verified.

The new theorem improves the quality/time tradeoff for a genuinely
general recipient-polymatroid allocation problem. It does not provide
a polynomial-time factor four, a constant gap for the refuted aggregate
configuration LP, or an automatically novel exponential-time result
for every special compulsory-player instance. Public and derived
baselines remain a separate comparison task.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
