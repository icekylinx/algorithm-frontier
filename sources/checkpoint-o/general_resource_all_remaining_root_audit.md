# Root audit of the general-resource conservative-blocker algorithm

**25 October 2026. Internal mathematical review completed.** The
operative manuscript is `general_resource_all_remaining_blockers.md`.
It has also received the separate exchange and source audits by the
matching and baseline reviewers. This is not formal verification or
external peer review. The proved scope is arbitrary recipient matroids
with at most one service per player-resource pair, and an arbitrary
player-selection matroid.

## 1. The universal reservation is a maintained theorem, not an oracle

For each resource and every subset Z of selected centers, consider
the actual current matching after removing precisely the designated
blocker groups of Z and inserting Z's services. The invariant requires
that receiving set to be independent. Matching and selected service
names are distinct where needed, so a set union never conceals two
services to one player at one resource.

A new candidate uses only resources for which its owner p is outside
the closure of X_j union Y_j. Designate every currently unmarked
matching record as its new blocker group D. In any old reservation,
deleting D leaves only old selected receivers and receivers belonging
to marked matching bundles. This is an independent subset of
X_j union Y_j. Adjoining p is therefore independent for every old
subset Z at once. At a resource not used by the candidate, the new
reservation only removes matching elements.

This proves every new subset case without finding a circuit or
enumerating a subset. The proof does not assume that X_j union Y_j
is itself independent: being outside its closure suffices to extend
each independent subset of it. This distinction is essential.

If p already owns a matching bundle, its player-side eligibility
places that bundle in an earlier designated blocker prefix. All its
old resources are unavailable under the resource-closure test. Its
new service therefore cannot duplicate an old matching service.

The new blocker group may be deliberately larger than necessary, and
can contain bundles sharing no resource with the center. This affects
the value coefficient but not the reservation proof.

## 2. Free insertion and record identities

An empty new group gives simultaneous feasibility with every existing
selected subset. A stored center whose group becomes empty has the
same property by applying the old invariant to Z union {c}. Thus
both fresh and stored free candidates are justified by the same
mathematical invariant. A currently feasible candidate is allowed to
retain conservative blockers; completeness does not require the
converse of this free-candidate implication.

When one old matching record b is replaced by the free candidate,
the reservation of a retained subset Z is obtained from its old
reservation plus the incoming service by deleting b if it was still
present. If b had already been excluded by Z's designated group,
removing it from both the matching and that group does not reintroduce
it. This proves resource independence after the exchange, including
replacement of an existing owner's allocation.

The operation must use record IDs. A new bundle with the same player
name is a new record and does not inherit the old record's Y flag.
Truncation releases a discarded center's group while retaining the
actual matching allocations in that group. Those records can be
designated again later. No deleted or new record is silently attached
to an old group.

Only one retained group can lose its last member in one exchange,
because groups are disjoint. Its center is processed immediately,
with its stored bundle. Player eligibility puts the next permissible
exchange strictly earlier; otherwise the owner augments the matching.
Consequently the existing finite cascade argument applies.

## 3. Lower maximality and finite progress do not require real conflicts

Below the earliest exchange layer, the selected bundles and designated
blocker records are unchanged. Therefore their resource owner sets
X_j,Y_j and all their resource closures are literally unchanged.
The earliest player-circuit lemma separately preserves their player
eligibility flats. Earlier failed availability scans remain valid
on exactly the same domains. Only the last retained layer is
refreshed.

The signature proof needs the following facts: designated groups are
disjoint; stable groups are nonempty; a new blocked center increases
the last selected count; a free exchange decreases the earliest
retained blocker count; higher coordinates are truncated; appending
a layer uses the infinity sentinel. Each is true for conservative
groups. None of them requires a physical resource intersection.

Selected and blocker totals remain O(r), including temporary states.
The previous integer-composition count and positive-growth depth
therefore apply. Every actual operation here uses polynomially many
original resource/player independence queries on O(r)-size sets,
plus ordinary bundle scans. The all-subsets invariant is never
materialized. There is no residual 2^{resource rank} factor.

## 4. The coarse certificate is sufficient, and the sharp one is not imported

Define the unavailable-resource cover by

\[
 \Phi(X,Y)=\sum_j v_j r_{R_j}(X_j\cup Y_j).
\]

The resource-column LP inequalities bound the total fractional
service at unavailable players by Phi. A complete available-value
scan, the row bound y_pj<=x_p and the player-base rank inequality
give Phi>(T-B)w for w=r-|J_0|>0, provided B<=T.
With an approximate local oracle replace B by B/lambda and assume
B<=lambda T. The inequality remains strict at equality because
the available value is strictly below the applicable threshold on
every positive eligible coordinate.

On the other hand, rank is at most cardinality, so

\[
 \Phi(X,Y)\le\sum_{c\in X}v(c)+\sum_{b\in Y}v(b)
             \le2(B+u)|Y|.
\]

The last inequality uses minimal bundle values and |X|<=|Y|.
It is valid even when a designated blocker shares no resource with
its center. The sharper singleton-star coefficient from the earlier
explicit-subset construction is not justified by this rule and is
not used in the main theorem.

For rho=(r-1)/r, the exact sufficient condition is
B/lambda+2rho(B+u)<=T. With tau=1/lambda, d=tau+4rho,
fat threshold B_0=T/d and target B=T/(d+eta), small resources have
u<B_0. The upper coefficient Cbar=2(B+B_0) satisfies

\[
 T-\tau B-\rho\overline C
       =(\tau+2\rho)(B_0-B),\qquad
 \frac{T-\tau B-\rho\overline C}{\overline C}
       \ge\frac1{16}\min\{\eta,1\}.
\]

Thus gamma=min{eta,1}/64 safely gives multiplicative current growth.
The rank exponent is uniform in lambda, with all oracle and bit
costs paid. At the exact boundary use the rank-exponential signature
bound. Rank zero and zero optimum are handled separately, and an
approximate oracle is never used to claim exact rank-one optimization.

## 5. General fat resource matroids and the stronger comparator

The fat matroid is the union of the actual recipient matroids, with
any locally infeasible singletons removed as loops. Its independent
sets can be partitioned among those resources, supplying one legal
fat service to each player. The dual-union complement construction
therefore works without a transversal representation. Its independence,
rank and decomposition operations have paid polynomial oracle cost.

For the configuration LP, choose one fat resource from each fat
configuration. Each resulting column is coordinatewise at most its
old recipient marginal, hence still resource-independent fractionally.
Their sum f<=x belongs to the fat union polytope. Combine it with
1-x in the dual player-base polytope, extend to a union base vector,
and complement. The all-small marginals can be scaled to the new
player masses. All resource columns decrease, and local perspective
constraints, when present, remain valid.

This proves the configuration-LP comparator and inner failure
soundness without solving that LP. The finite common value grid and
the polynomial-bit upper target support the existing one-sided
target search. The proof does not rely on monotone success decisions.

## 6. Relevant-blocker refinement also passed root review

The later `general_resource_relevant_blocker_addendum.md` restricts
new blockers to all unmarked matching records sharing a resource
index with the candidate. For every resource used by the candidate,
this still removes all unmarked matching recipients at that resource.
Every prospective reservation is again an independent subset of
X_j union Y_j before adding the candidate owner. For unused resources
there is only deletion. Thus the implicit universal proof, including
empty relevant groups, remains valid.

Every designated blocker now shares a resource with its center.
That fact survives group shrinkage because retained bundle records
and their resource sets are immutable. It gives the sharp coefficient
max{2u,2B+2min(u,B)} without any subset enumeration. Singleton centers
have singleton blockers; nonsingleton centers have only nonsingleton
blockers. The three branches of the equality solution agree at
u=T/(tau+4rho) and u=2T/(tau+4rho), and the stated positive-gap
growth bound follows from the same strict cover inequality.

This recovers the earlier explicit-subset manuscript's sharp compact
quality curve with polynomial work per state. The arbitrary-size
factor remains tau+4rho, including the exact-oracle 5-4/r. The
coarse primary proof remains independently valid; its unrelated
blockers are not retroactively described as sharing a resource.

## 7. Accepted research conclusion and its limits

For exact available-bundle access, the internally reviewed conclusion
is factor 5-4/r in poly(input) times 2^{O(r)}, and factor 5-4/r+eta
in

\[
 \operatorname{poly}(\text{input})
 \min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}.
\]

It applies to arbitrary player and recipient matroids, with the
configuration-LP comparator. Local downward-closed bundle constraints
with factor-lambda available optimization give lambda^-1+4-4/r
and its positive-error counterpart, with the stated oracle costs.

The named public general-resource baseline is polynomial 8+epsilon;
its stronger two-value and other special cases remain in the
comparison. This is a quality/time and rank-parameter result, not a
claim to dominate the public polynomial bound on all inputs or to
be the first constant approximation for the model. Publication
priority has not been established exhaustively.

Recipient polymatroids with repeated units per player need a separate
certificate; they are not proved by this matroid argument. The
original unrestricted general-graph maximum-matching exponent is
still 4/5. This checkpoint records a second-problem transfer.
