# Independent audit of conservative completion for arbitrary resource matroids

**25 October 2026. Reviewer: transfer_baselines.**

This reviews `general_resource_all_remaining_blockers.md`, equations
(A1)--(A14). I read the complete new manuscript and separately checked
its subset invariant, receiving-name conventions, old-prefix certificates,
coarse value charge, signature interface, fat union, and configuration
comparator. The construction passes this audit. Public priority and
named comparisons are treated separately in
`general_resource_matroid_public_parameter_comparison.md`.

## 1. Why the simultaneous invariant needs no algorithmic subset tests

Let X be selected centers and Y the disjoint union of their designated
matching-record groups. For every actual subset Z of X, retain the
mathematical assertion

\[
 Q_j(Z)=(M_j\setminus\operatorname{owners}D(Z))
                   \mathbin{\dot\cup}X_j(Z)\in\mathcal I(R_j).
\]

For a candidate c with owner p, take D to be all current matching
records outside Y. The new reserved set at a used resource j is

\[
 [M_j\setminus\operatorname{owners}(D(Z)\cup D)]
                   \mathbin{\dot\cup}X_j(Z)\mathbin{\dot\cup}\{p\}.
\]

Before adjoining p, this is an independent subset of Q_j(Z). Its
remaining matching receivers all belong to Y_j, so the complete set
lies in X_j union Y_j. Availability puts p outside the closure of
that union. It can therefore be adjoined to this independent set.
At a resource not used by c there are only deletions. This argument
works for every Z without distinguishing or enumerating subsets.

Crucially, no claim is made that the designated records are actual
intersections, a minimal deletion set, or individual circuit witnesses.
They are sufficient deletions for all the joint reservations. Their
overcounting is explicit in the later value bound.

## 2. Actual service identities remain distinct

A set union by itself could hide duplicate services to one player at
one resource. The stronger invariant prevents that: X_j has distinct
selected owners and is disjoint from M_j.

Availability already excludes p from X_j and Y_j. If p is currently
matched, eligibility outside the player flat of I minus the earlier
blockers forces its own matching record to lie in that earlier prefix.
Consequently every resource in its old allocation belongs to Y_j and
is unavailable for the new candidate. At a newly selected resource
p is absent from M_j as well.

The matching deletion in the new-reservation formula acts only on the
matching term. It never deletes a selected occurrence simply because
some other service has the same player name. The current formula has
the required separation.

On later insertion of a free bundle, the fresh case excludes all
retained same-resource selected occurrences by availability. The stored
case has them distinct already. If its player was matched, that same
player's old matching record is the removed one. Thus new matching
services remain distinct from retained selected services.

## 3. Both meanings of a free candidate are sound

For a fresh candidate, D empty means that all current matching records
are already in Y. The argument of Section 1 proves feasibility against
the actual matching and every selected subset simultaneously.

For a stored center c with its group now empty, the invariant on
Z union {c} gives exactly the same assertion. This is the important
direction: an empty designated group certifies freedom. The reverse
direction is not required. A feasible center may remain conservatively
blocked, and doing so does not invalidate a proof step or a signature.

After replacing matching record y by this free center, consider a
retained subset Z. At every resource its new reserved set is contained
in the old set certified for Z union {c}. If y was already excluded
as a designated blocker of Z, deleting its group membership does not
reintroduce it: y has also been removed from the matching itself.
If y was not excluded, its deletion only helps. The incoming service
is present in the old joint certificate. This proves the new invariant.

Exactly one designated group can lose y. Only its center can become
newly free, so the old-free-center cascade remains the accepted
earliest-layer cascade. The candidate's existing resource subset must
be retained through truncation and inserted unchanged.

Truncating an unrelated layer only removes its selected centers and
unmarks its matching records. For any retained subset Z neither its
selected set nor its designated group changes. Thus its reservation
is unchanged, even though some previously marked records become
eligible for the next all-remaining completion.

## 4. Earlier maximality does not refer to actual resource blockers

Below the earliest exchange layer, the exact selected records and
designated matching records are retained. The deleted record is not
among them, and the inserted record is not marked there. Therefore
both X_j and Y_j of that lower prefix are the same sets as before.
Its resource closure is identical.

Independently, the player-side earliest-circuit lemma preserves its
eligibility flat. The old complete-scan assertion remains valid on
the same eligible players and available resource lists. There is no
hidden need to update recipient fundamental circuits or reconstruct
an actual overlap graph. Refreshing the last surviving layer is
sufficient. These are precisely the historical-certificate conditions
used by the accepted rank signature proof.

## 5. The coarse coefficient is the correct one

Use the computable cover

\[
 \Phi=\sum_j v_j r_{R_j}(X_j\cup Y_j).
\]

Unavailable players lie in these resource closures. A feasible
recipient column has at most their rank in total mass on the closure.
Hence Phi bounds unavailable fractional value.

At a completed scan, every eligible player's available value is below
B. The player-base vector has at least w=r-k+s mass outside the
eligibility flat. Positive eligible coordinates give the strict bound
Phi>(T-B)w when B<=T. Strictness survives B=T and is what makes a
weak opposite certificate sufficient.

On the upper side, rank is bounded by the number of stored service
occurrences. Each stored minimal B-bundle has value below B+u, and
stable nonempty disjoint groups imply |X|<=|Y|. Thus

\[
       \Phi\le\operatorname{value}(X)+\operatorname{value}(Y)
                                      \le2(B+u)|Y|.
\]

This does not use a shared resource between a center and its blockers.
The sharper singleton coefficient of the explicit-circuit version is
not justified here and is correctly omitted. The coarse coefficient
is nevertheless sufficient after the fat/small threshold is fixed.

Since s/(r-k+s)<=(r-1)/r, an empty new layer certifies infeasibility
when B+2rho(B+u)<=T. With positive slack, a layer having only a small
fraction of w new blockers yields the analogous certificate.

## 6. Rechecking the complete time interface

Each candidate is an explicit subset of the input resources. Current
matched owners are distinct, and current matching size is at most r-1.
Stable selected centers are at most the number of designated blockers.
An actual operation requires resource-rank queries on O(r) names,
player-matroid queries, explicit value scans, and at most r-1 group
markings. Even rebuilding all auxiliary state at every operation is
polynomial in the full encoded input and the supplied oracle costs.

No independence test over a subset of centers is executed. The universal
invariant is established by the two direct inductions above, rather than
used as an unimplemented algorithmic oracle.

A blocked insertion increases the last selected count. A free exchange
decreases the blocker count in the earliest changed retained layer;
only later signature entries can be discarded or changed otherwise.
Appending a layer uses the same infinity-sentinel rule. These changes
are exactly the integer micro-signature changes of the imported proof.
That proof uses disjoint designated groups, positive group sizes at
stable states, retained eligibility/maximality, and these count changes.
It does not need actual physical intersections or minimal blockers.

The exact branch consequently has 2^O(r) charged states per phase.
With growth y>gamma(r-k+s), depth is O(gamma^-1 log(r+1)) and the
state count is (r+1)^O(gamma^-1 log(r+1)). There are at most r phases.
This supplies the claimed quasipolynomial branch for unrestricted
recipient rank. Neither q nor a recipient rank has been substituted
for r in the exponent. Their processing costs are paid in the
polynomial multiplier.

## 7. Fat threshold, error margin, and the LP comparator

Let rho=(r-1)/r and d=1+4rho. At B0=T/d, small resources have u<B0.
The derived small player rank r' is at most r, and

\[
 B_0+2\rho_{r'}(B_0+u)\le(1+4\rho)B_0=T.
\]

For B=T/(d+eta) use Cbar=2(B+B0). Its positive gap is
(1+2rho)(B0-B). Since 1+2rho>=d/2 and Cbar<=4T/d, the gap/Cbar
is at least min(eta,1)/16. The stated gamma=min(eta,1)/64 is safe.
Smaller derived rank or actual largest small value only improves
this inequality.

The fat union consists of independent recipient parts. Matroid union
and decomposition are polynomial oracle operations; the M* union N
complement argument has the required semantics. On reconstruction,
extending the dual part only deletes allocated players and therefore
preserves every recipient constraint.

For the configuration comparator, pick one fat resource in each
fat-containing configuration. Each fat column remains in its original
recipient polytope by downward closure. The union rank formula places
their sum f<=x in the fat union polytope. A dominating union base for
1-x+f leaves x'<=x-f. Scaling all-small configuration rows to x'
decreases every resource column and preserves target demand. Thus
the algorithm does not need an explicit configuration LP solver.

The common rational grid and finite total-utility bound justify
polynomially many one-sided target-search trials. The positive-target
construction uses B>0. The zero-optimum endpoint is handled by any
player basis with empty zero-value allocations, as in the established
target-search convention; zero-value resources can simply be removed.

## 8. Optional local families and the verdict

For a downward-closed local family, restrict each configuration to
the available resource list. A lambda-factor feasible oracle returning
below B implies a true available optimum below B/lambda. The resource
invariant and upper cover are unchanged. Fresh scans are required;
old failed approximate outputs are not cached through changed states.

With tau=1/lambda, d=tau+4rho, the gap is
(tau+2rho)(B0-B), and tau+2rho>=d/2. Thus the same normalized growth
constant works without an extra lambda^-1 in the rank exponent.
Singleton feasibility identifies the allowed restriction of each fat
resource matroid. The configuration row-perspective argument is
preserved by scaling, while resource columns only decrease.

The general-resource conservative-completion theorem passes this
independent audit. It is a new mathematical adapter over the accepted
player-side search. It does not assert polynomial time, does not
include repeated recipient units of an integral polymatroid without
another proof, and does not establish a global literature priority.
The named public comparisons and the distinction between r and q
remain essential to the interpretation of the result.
