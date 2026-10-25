# Independent exchange audit of all-remaining conservative blockers

**25 October 2026. Independent third-view audit of
general_resource_all_remaining_blockers.md.**

The construction passes this audit. The important new fact is that
all-subsets reservations can be maintained as an inductive invariant
without being tested or enumerated. The conservative blocker rule
preserves the hypotheses used by the earlier player-side signature
proof. Actual shared resources are needed by the old sharp star
coefficient, but are not needed by the coarse cover used here.

This audit addresses correctness and charged operations. Public
priority and the comparison with polynomial-time algorithms are
separate questions.

## 1. Distinguish bundle records from their player names

A current matching record has one player owner and one resource
bundle. The matching has no repeated player owner. Each selected
center has a set of current matching records designated as its
blocker group. These groups are disjoint.

If an old matching bundle is replaced by another bundle for the same
player, its old record must be removed from its group. The new record
is initially unmarked. It must not inherit a blocker flag merely
because its owner name or storage slot is reused.

For a resource j, selected centers using j have distinct player
owners, and their receiving names are disjoint from those of the
current matching at j. Repeated selected player names across
different resources are allowed. The all-subsets reservation is
always interpreted with distinct services, not with a set union
that silently merges duplicates.

The manuscript explicitly uses record IDs and states these
resource-level distinctness conditions.

## 2. Why removing all unmarked records is a simultaneous completion

Let Mcal be the current matching records, X the old centers, and
Y the union of their disjoint groups. A newly constructed candidate
c uses resource j only when its player p is outside

cl_Rj(X_j union Y_j).

Set D=Mcal minus Y. This is one common set of whole matching
records for every resource and every selected subset.

Fix any old subset Z of centers. Before adjoining p, its new
reservation at j is obtained from the old independent Q_j(Z)
by deleting the records in D. The surviving matching names lie
in Y_j, and the selected names lie in X_j. Thus it is an
independent subset of X_j union Y_j.

The union X_j union Y_j itself need not be independent.
Nevertheless p outside its closure lies outside the closure of
every subset. Therefore p can be adjoined to every one of the
independent surviving reservations simultaneously.

For resources not used by c, only deletions occur. Consequently
all new subsets Z union {c} satisfy the required reservation
invariant, while old subsets remain unchanged.

This proof does not call an independence oracle once per Z.
All actual work is constructing the available bundle and marking
the at most r-1 unmarked matching records.

For implementation of availability, one may greedily obtain a
basis of X_j union Y_j and test whether adding p increases its
rank. Testing independence of the possibly dependent full union
plus p would not by itself compute closure.

## 3. New candidates cannot duplicate an old service

Availability excludes p from both X_j and Y_j at every selected
resource j.

If p already belongs to the current player matching I, player-side
eligibility forces its matching record to be in the earlier blocker
prefix: otherwise p belongs to I minus that prefix and is in its
closure. Every resource of p's old matching bundle is therefore
unavailable to p. A newly chosen resource cannot duplicate its old
matched service.

This also explains why the all-remaining set D never inadvertently
removes the candidate's own old record in place of the player-side
exchange: that record, if present, is already in an earlier group.
The resource proof and player-circuit rule have consistent meanings.

## 4. Fresh and stored free candidates are jointly feasible

A fresh candidate is declared free when D is empty. Lemma 1 above
then says directly that it is feasible with every old subset Z,
without deleting any additional unmarked matching records.

For a stored center c with its designated group now empty, use the
old all-subsets invariant on Z union {c}. Since its own group
deletes nothing, this is exactly joint feasibility of c with the
reservation of every subset Z of the other centers.

The converse is not required. A center may already be feasible
against the actual matching while its conservative group remains
nonempty. Waiting until that group becomes empty loses no proof
invariant. The termination argument counts designated groups,
rather than requiring that each group be minimal or a set of
actual resource conflicts.

## 5. Exact record-level exchange calculation

Let incoming c be jointly free, and remove the old matching
record b in the earliest permitted player-side layer. Insert a
new record b^+ carrying c's bundle. Let X^ret be the retained
centers; it excludes c itself if c was stored, because the
exchange layer is strictly earlier than c's layer. On augmentation,
all layers are discarded.

For each retained center z, its new group is

D'(z)=D(z) minus {b}.

For any Z subseteq X^ret, the matching-record portion satisfies

Mcal' minus D'(Z)
 =
[(Mcal minus D(Z)) minus {b}] union {b^+}.

This identity holds whether or not b belonged to D(Z).
At a resource used by c, the new reservation is therefore a subset
of the old jointly feasible reservation for Z together with c.
At any other resource it is simply a subset of the old reservation.
Deletion preserves resource independence.

Distinctness also survives. A fresh c excluded every retained
occurrence of p(c) at its resources by availability. A stored c
already had different names from all other selected services at
each resource it uses. Its own old matching bundle, if present,
is removed. Since c itself is no longer retained as a selected
center, insertion does not create a selected/matched duplicate.

Thus the full all-subsets invariant and the stronger
X_j disjoint from M_j property survive every exchange.

## 6. Conservative groups preserve free cascades and old maximality

Only the one group containing removed record b can become empty.
An actual resource obstruction of another center might also
disappear, but the algorithm need not react to that event while
its designated group is nonempty.

For the newly empty group, its stored center is jointly free by
Section 4. Player eligibility is still valid by the imported
earliest-circuit span lemma. A nonaugmenting next exchange is in
a strictly earlier layer, so the same finite free cascade applies.

Truncation removes higher selected centers and releases their
groups without deleting the corresponding matching bundles.
For a subset of retained centers, its own group union has not
changed apart from the explicitly removed record. Hence releasing
other groups does not invalidate its reservation.

For a strictly lower retained layer, none of its selected or
designated matching records has changed. The new matching record
is unmarked in that prefix. Thus its X_j and Y_j sets, and
therefore every resource closure defining availability, are
literally the same as before.

The player-side eligibility flat is also unchanged. Old maximality
survives on the same eligible domain and the same available lists.
Only the last surviving layer is refreshed. None of these facts
uses a resource shared by a center and its designated blocker.

## 7. The coarse rank cover pays artificial blockers

For resource j, all unavailable players lie in
cl_Rj(X_j union Y_j). Any feasible fractional resource column has
at most r_Rj(X_j union Y_j) mass on this set.

Summing its value over resources gives

Phi(X,Y)
 <= sum_(c in X) v(c) + sum_(b in Y) v(b).

Each fully processed center has a nonempty designated group, and
groups are disjoint, so |X|<=|Y|. All matching and selected bundles
are minimal above B, hence have value below B+u. Therefore

Phi(X,Y) <= 2(B+u)|Y|.

An artificial blocker with no resource in its center is still a
real current matching bundle, with its full value counted on the
right. No fictional shared item or intersection subtraction is used.

At a completed failed availability scan, every positive eligible
player mass has strictly less than Bx_p fractional available value.
Base-polytope rank mass outside the eligibility flat is at least
w=r-|J_0|>0. Feasibility would therefore require

Phi(X,Y)>(T-B)w.

This is the same strict certificate mechanism with the coarser
coefficient. In particular an empty new layer is impossible under

B+2((r-1)/r)(B+u)<=T.

The old sharper singleton coefficient is not imported.

## 8. Compatibility with the charged signature theorem

The old player-side proof needs the following properties:

* a blocked insertion adds one selected center and at least one
  previously unmarked matching record to a disjoint group;
* a nonaugmenting free exchange deletes one record from the
  earliest affected group, retaining that layer's selected centers
  before higher coordinates matter;
* a newly empty selected center is processed immediately, with
  strictly earlier subsequent exchanges;
* lower completed maximality remains true, and the last surviving
  layer is fully refreshed before another growth test;
* all stable groups are nonempty, and at most r-1 matching records
  occur in a phase.

Sections 2--7 establish each property for conservative groups.
Actual resource intersections and minimum-size blocker sets are
not additional hypotheses of the lexicographic count argument.

A fresh free candidate is not inserted as an extra stable selected
record. A stored free center was already counted. The usual
rank-bounded composition count and the positive-growth depth bound
therefore apply to all charged microstates.

All actual actions have polynomial cost: resource rank queries on
O(r) names, player-matroid tests, explicit bundle scans, marking
Mcal minus Y, group-pointer changes, and truncation. The all-subsets
invariant is never enumerated. This is the point that removes the
previous exponential reservation-work factor.

## 9. Quality and wrapper checks

After the fat split at B_0=T/(1+4rho), every small resource has
u<B_0. At B=B_0,

B_0+2rho(B_0+u) <= (1+4rho)B_0=T.

The derived player matroid has rank at most the original rank,
so using rho=(r-1)/r is conservative. The exact rank-exponential
factor is therefore 5-4/r.

For positive eta, using B=T/(d+eta), d=1+4rho, gives cover gap

T-B-rho[2(B+B_0)]
 =(1+2rho)(B_0-B).

The manuscript's lower bound on this gap divided by the coarse
coefficient and its choice gamma=min(eta,1)/64 are valid.
Consequently the existing positive-growth signature count gives
the quasipolynomial branch, now with polynomial work per state
for arbitrary resource rank.

Fat-resource matroid union, dual-basis reconstruction, and the
configuration-LP split use only recipient independence and
downward closure. These were independently checked in the
preceding adapter audits and remain unchanged. Discarding players
during reconstruction preserves every resource's independence.

For a lambda-factor player-local oracle, replace B by B/lambda
in the strict outside-value bound. With tau=1/lambda, the same
algebra uses d=tau+4rho and coefficient gap
(tau+2rho)(B_0-B). Since tau>=1, the stated growth constant is
uniform in lambda; oracle accuracy and numerical encoding remain
paid.

## 10. Verdict and explicit scope

No hidden actual-blocker assumption remains in the exchange,
maximality, cascade, or signature import. The simultaneous
completion rule D=Mcal minus Y is sufficient to maintain all
subset reservations by induction, without oracle tests for those
subsets.

The construction passes this independent audit with current-record
identity, distinct service names, and the atomic exchange conventions
described above. It applies to arbitrary recipient matroids with one
service per player-resource pair and to the stated player-local
oracle extensions.

It does not silently include resource polymatroids allowing repeated
service units to the same player. Nor does the improved
approximation/time tradeoff change the current general-graph
maximum-matching exponent.

## 11. Independent check of the relevant-blocker refinement

The addendum general_resource_relevant_blocker_addendum.md also
passes this audit.

Replacing D=Mcal minus Y by all unmarked matching records whose
resource sets intersect c preserves the simultaneous completion
proof. For each resource j used by c, every unmarked matching
recipient at j is still deleted. The remaining independent set
is therefore still contained in X_j union Y_j. Resources outside
c only lose elements.

This is one common set of whole records, not separately chosen
per-resource deletions. An empty relevant group is sufficient even
when unrelated unmarked matching records remain. None of those
unrelated records can appear in a resource affected by c.

Every designated blocker now shares an actual resource index
with its center. The resources of a surviving record are fixed;
a changed bundle is a removed old record and a new unmarked one.
The shared-resource property therefore remains valid throughout
the lifetime of each designated group member.

The singleton/nonsingleton argument consequently restores

C_R(B,u)=max{2u, 2B+2 min(u,B)}.

It still does not use disjointness of resource indices across
stars or a fictitious physical item intersection.

For tau=1/lambda and rho=(r-1)/r, the equality
tau B+rho C_R(B,u)=T has the stated three branches. They arise
respectively from u<=B, B<=u<=2B, and u>=2B. Substitution gives

(T-2rho u)/(tau+2rho),  T/(tau+4rho),  (T-2rho u)/tau.

The branch boundaries u=T/(tau+4rho) and
u=2T/(tau+4rho) agree exactly, and the final branch is positive
precisely below T/(2rho). For rho=0, the equation is simply
B=lambda T.

With positive gap Delta, choosing
gamma<=Delta/(2C_R) leaves a strict half-gap in the cover
contradiction. Every operation remains polynomial and no subset
or resource-rank enumeration is reintroduced.

The arbitrary-size fat-wrapper denominator remains
lambda^(-1)+4-4/r. The refinement improves the compact-relaxation
curve and group selectivity, rather than changing that wrapper
factor.


