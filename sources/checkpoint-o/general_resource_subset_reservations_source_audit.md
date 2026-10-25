# Independent audit of the explicit subset reservation construction

**25 October 2026. Reviewer: transfer_baselines.**

This audits `general_resource_matroid_subset_reservations.md`, including
equations (G13)--(G15) added in Section 7.1. The explicit-subset algorithm,
its resource-rank width refinement, and its configuration comparator pass.
The subsequent conservative-blocker proposal is a different implementation
and is not being silently used to justify this note's time bound.

## 1. What is reserved

For selected centers X and their disjoint designated matching-blocker
groups B(c), the invariant asserts resource independence of

\[
 (M_j\setminus\operatorname{owners}B(Z))\mathbin{\dot\cup}X_j(Z)
 \qquad (Z\subseteq X)
\]

for every resource j. This says that every actual subset of selected
bundles can replace its own designated blockers. It is stronger than
individual feasibility, pairwise feasibility, or an exchange that reroutes
one resource allocation separately for each possible future candidate.

The independent-set oracle is called on sets of O(r) actual player names.
No linear representation, common basis ordering, or strongly base-orderable
property of resource matroids is needed. Resource ranks may exceed the
selection rank. All outside-ground players are treated as loops.

## 2. New candidates and the circuit witness

Availability requires p outside cl_Rj(X_j union Y_j). In particular p is
not a loop, and it is not already a selected receiver at j. If p is a
current matching owner, its player-side eligibility implies that its
matching bundle is in an earlier blocker layer. Every resource currently
assigned to p is therefore unavailable. Thus adding the new selected
service never identifies it with an old matching service at the same j.

For each tested old subset, first remove the newly designated matching
blockers D from the matching part only, then add p. The current manuscript
writes this as separate matching and selected terms in (G7). This avoids
silently deleting a selected service merely because its owner name appears
in a matching-blocker list. In fact retained player eligibility also
implies that a currently matched selected owner lies in an earlier Y layer,
but the separated formula is the cleaner contract.

The pre-addition set is an independent subset of the old reserved set.
If adding p creates its fundamental circuit, some other circuit member
must be a current matching receiver outside Y and D. Otherwise the circuit
would lie entirely in X_j union Y_j union {p}, contradicting availability.
Delete that member's matching bundle by adding it to D. It is not a selected
receiver at j, so the intended circuit member is actually removed.

Every such deletion makes all earlier successful resource tests easier.
After at most k-|Y| deletions all remaining tests pass. Equivalently, if
all undiscovered matching bundles were removed, every remaining tested set
would lie in X_j union Y_j and could accept p. The explicit circuit procedure
finds a subset of those deletions and each selected blocker receives some
resource in the candidate. This last fact is needed only for the sharper
star-value coefficient.

## 3. Exchange inclusion, checked by cases

Let c be a fresh free candidate, or a stored center whose designated group
has become empty. For every retained subset Z, the old invariant for
Z union {c} says that c is feasible jointly with Z. A fresh candidate's
completed tests say the same thing.

Replace a matching bundle y by c. At resource j there are four elementary
possibilities, according to whether y and c use j. If y uses j it is
deleted from the new matching. If it was a blocker of Z, it was already
absent from the old reserved set, and deleting its designation does not
reintroduce it because its matching record itself has been removed. If c
uses j its recipient is added. Thus the new reserved set is a subset of
the old reserved set for Z union {c}; if c does not use j it is a subset
of the old set for Z. Independence follows by downward closure.

The dotted unions remain valid. A fresh c excluded all old selected
receiver occurrences by availability. A stored c already had a distinct
receiver occurrence from every other selected center using the same
resource. Its old matching record, if present, is the record removed by
the player-side exchange. The new service never becomes a duplicate.

Only the designated owner of y can lose its last blocker. That center is
processed immediately, with the same exchange inclusion, and the earliest
player-circuit lemma makes the cascade move to a strictly earlier layer.
No extra resource circuit has to be discovered after a swap.

At any strictly lower surviving layer both its selected records and its
designated blocker records remain unchanged. Its resource closure and its
player eligibility flat are unchanged separately. The old maximality
certificate therefore survives. The last surviving layer is refreshed.

## 4. Fractional cover and the exact boundary

An independently computable cover is

\[
 \Phi_R=\sum_j v_j r_{R_j}(X_j\cup Y_j).
\]

The unavailable receiving set is the closure of X_j union Y_j and has
this same rank. Every feasible fractional column has at most that rank
mass on the closure. Hence Phi_R bounds the total unavailable value.

For a completed eligible scan the available value is strictly below B
for every eligible player. The perspective inequalities give the strict
fractional lower bound Phi_R>(T-B)w, where w=r-k+s and B<=T. The endpoint
B=T remains strict. Using the actual rank in Phi_R rather than the looser
sum of service counts can only strengthen a returned certificate.

The sum-of-service-values bound is at most 2(B+u)|Y|. For the explicit
circuit version, each designated blocker shares a candidate resource.
Singleton and nonsingleton stars therefore give exactly

\[
 C_R(B,u)=\max\{2u,2B+2\min(u,B)\}.
\]

Since s/w<=(r-1)/r, the sufficient condition B+rho C_R(B,u)<=T is valid
with equality. Fully blocked layers have distinct nonempty blocker groups,
so |X|<=|Y|<=r-1 at a stable state. A fresh free candidate is not stored.

## 5. Resource width really reduces the subset inventory

For a fixed j, let X(j) be the centers using j. If Z_j=Z intersect X(j),
then the selected receiver set at j is identical for Z and Z_j, while
B(Z_j) is a subset of B(Z). Consequently Q_j(Z) is a subset of Q_j(Z_j).
Deleting D from their matching parts preserves the inclusion. Testing
only subsets of X(j) therefore implies all original tests; it does not
replace the invariant by a weaker pairwise condition.

The full-set invariant makes X_j independent in R_j. Its distinct service
owners give |X(j)|=|X_j|<=r(R_j). Thus the explicitly performed tests per
state have multiplier at most 2^min(r,kappa), where kappa is the maximum
resource rank. The total selection rank r and the recipient rank kappa
are different parameters. Neither can be replaced by the total player
count q without changing the statement.

For tau=1/lambda, rho=(r-1)/r, d=tau+4rho, B0=T/d and
B=T/(d+eta), use Cbar=2(B+B0). The algebra is

\[
 T-\tau B-\rho\overline C=(\tau+2\rho)(B_0-B),
 \qquad \tau+2\rho\ge 3d/5,
 \qquad \overline C\le4T/d.
\]

The gap divided by Cbar is at least
3 eta d/[20(d+eta)] >= 3 min(eta,1)/40. The stated growth parameter
min(eta,1)/64 is consequently safe. Combining paid subset tests with the
audited rank-depth signature gives (G15). The first branch still costs
2^O(r) after multiplying two singly exponential factors; the second branch
is quasipolynomial for bounded or logarithmic recipient rank.

## 6. Wrappers and scope

The fat union uses arbitrary resource matroids legitimately: choosing one
fat resource for each fat-served player gives independent parts, hence an
independent set of their union. A decomposition supplies those resources
back after the player-dual complement construction. Deleting newly
discarded players preserves every recipient matroid.

The configuration proof uses downward-closed columns and the union rank
formula. Selected fat column vectors sum to a coordinatewise bounded
vector in the union polytope; extending fat plus the selection-dual base
to a base leaves a player vector dominated by small-configuration mass.
Scaling small rows preserves all resource columns and optional
player-local perspective families. No configuration optimization is
assumed as an oracle.

All oracle calls, resource scans, numerical precision, and target search
are in a polynomial multiplier in the full encoded input. Only the layer
count and explicit subset inventory have the displayed rank dependence.
An approximate available oracle must be called on a fresh scan; its
failures are not treated as a monotone fixed tie-breaking rule.

This audit passes the explicit construction and its bounded-rank
refinement. It does not establish that the explicit test cost is necessary.
In particular a later conservative choice of designated blockers may
maintain the same invariant by a direct induction without performing these
tests. That candidate must use its own value coefficient and time proof.
