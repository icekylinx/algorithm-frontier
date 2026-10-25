# Second audit of explicit all-subsets resource reservations

**25 October 2026. Independent mathematical review completed.**
The operative manuscript is
general_resource_matroid_subset_reservations.md, including G13--G15.
The later general_resource_all_remaining_blockers.md is a stronger
implementation for the arbitrary-size factor. This audit approves
the original explicit construction on its own stated interface.

## 1. Distinct services and marked matching records

Different selected centers using one resource have distinct owners,
and their receiving set is disjoint from the current matching's
receiving set at that resource. Without this condition, a set union
would incorrectly collapse multiple services.

Availability excludes a new owner from old selected and marked
receivers. If it is already matched, player eligibility puts its
matching record in the earlier blocker prefix, so its old resources
are unavailable. Future free exchanges preserve distinctness because
a fresh center excluded retained occurrences and a stored center was
already distinct from the other selected centers at each resource.

A same-player replacement must clear the old matching record's group
flag and install a new unmarked record. This is a record operation,
not only a replacement of an owner string.

## 2. Every failed new-subset test has a usable circuit member

The intended tested set is

\[
 \bigl(M_j\setminus\operatorname{owners}(D(Z)\cup D)\bigr)
          \mathbin{\dot\cup}X_j(Z)\mathbin{\dot\cup}\{p\}.
\]

Before adding \(p\) it is an independent deletion from the old
reservation. A circuit through \(p\) cannot consist otherwise only
of old selected or old marked names, because that would place
\(p\) in the forbidden closure of \(X_j\cup Y_j\).
It therefore contains a recipient of a matching record outside
\(Y\cup D\). Add that whole record to \(D\).

Each such step adds a distinct record. There are at most \(k-|Y|\)
steps. Later removals only shrink passed tests. Fundamental circuits
on \(O(r)\) names are obtained with polynomially many deletion tests.
Each chosen blocker receives the actual tested resource of the center;
this justifies the sharp coefficient later.

The shorthand that removes owners from \(Q_j(Z)\) is equivalent on
maintained states. Every selected owner that is currently matched must
belong to its earlier marked prefix, by player eligibility. A newly
chosen record outside \(Y\) cannot have such an owner. Nevertheless
the explicitly typed expression above is clearer.

## 3. Free exchange and old-prefix preservation

A fresh empty-group center is jointly feasible with every old selected
subset by its tests. For a stored empty-group center this follows from
the old invariant on \(Z\cup\{c\}\).

After deleting one matching record and installing that center, every
retained reservation is a subset of its old reservation plus the
incoming service. Removing a record already in \(D(Z)\) simply
removes a blocker that had already excluded it; otherwise it removes
a present recipient. Independence follows from the joint invariant.

The empty subset proves actual matching feasibility. At most one
retained group becomes empty because designated groups are disjoint.
Higher-layer retirement releases flags but keeps the matching
allocations themselves. For retained \(Z\), these retired groups
were never in \(D(Z)\).

Strictly lower selected and marked records remain identical. Their
resource receiving sets and closures are therefore identical, while
the earliest player exchange preserves their eligibility flat.
Last-layer refresh and the immediate free cascade satisfy the
accepted signature's operational hypotheses. No actual or minimal
recipient-conflict interpretation of the designated groups is used.

## 4. Rank cover and exact boundary

The unavailable receiving mass at resource \(j\) is at most the
rank of \(X_j\cup Y_j\). Hence the excluded value is bounded
by selected and marked matching values. A completed failed scan
gives a strict lower bound \((T-B)w\) when \(B\le T\).

Every stable center has at least one assigned blocker. A singleton
center forces every shared-resource minimal blocker to be a singleton.
A nonsingleton center has only items below \(B\); each assigned
blocker contains one of them and therefore cannot contain any item
at least \(B\). This proves the sharp
\(\max\{2u,2B+2\min(u,B)\}\) charge.

With \(s/w\le(r-1)/r\), equality in the sufficient upper-cover
condition is valid because the lower bound is strict. The usual
rank-composition count includes the zero-slack exact boundary.

## 5. Resource width and positive-error time

For resource \(j\), retain only the centers \(X(j)\) using it.
For \(Z_j=Z\cap X(j)\), the added recipients are unchanged and
the removed matching set only decreases on passing from \(Z\) to
\(Z_j\). Thus \(Q_j(Z)\subseteq Q_j(Z_j)\), also after new-group
deletion and addition of the candidate. Testing subsets of \(X(j)\)
therefore proves all the full-subset requirements.

The invariant implies \(X_j\) itself is independent, so
\(|X(j)|=|X_j|\le r(R_j)\). The claimed
\(2^{\min(r,\kappa)}\) per-state factor is an actual paid bound.
It is not a polynomial oracle in unrestricted recipient rank.

For \(\tau=\lambda^{-1}\), \(d=\tau+4\rho\),
\(B_0=T/d\), \(B=T/(d+\eta)\), and
\(\overline C=2(B+B_0)\), the gap is
\((\tau+2\rho)(B_0-B)\).
Since \(\tau\ge1\ge\rho\), \(\tau+2\rho\ge3d/5\).
Dividing by \(\overline C\le4T/d\) gives at least
\(3\min(\eta,1)/40\), so the manuscript's
\(\min(\eta,1)/64\) growth factor is safe. G15 follows, including
its lambda-uniform rank exponent.

## 6. Fat and configuration comparison

The fat object is the union of recipient matroids, not an assumed
transversal representation. Independence has a polynomial union
decomposition into legal one-fat-service assignments. The dual-union
complement construction and deletion of additionally selected dual
players preserve recipient independence.

For the configuration comparator, the chosen fat receiving vector
at each resource is coordinatewise at most its original column.
It remains in that recipient independence polytope, and the sum
belongs to the union polytope. Base domination and conditional
small-marginal scaling preserve all resource columns and any row
perspective constraints. Zero small mass and zero derived rank have
the stated zero/trivial conventions.

Common-grid target search uses a failed upper point greater than
the approximation ratio times total possible utility, not an
unjustified monotonicity of successful decisions.

## 7. Conclusion of the audit

The explicit-subset theorem, its sharp compact-relaxation condition,
resource-width refinement, paid oracle costs and configuration
comparison pass this review. Subsets can be streamed, so exponential
time does not imply exponential storage.

The all-remaining and relevant-remaining alternatives are different
completion rules, with separate inductive proofs. They should be
cited explicitly when removing the subset factor. The former uses
only the coarse coefficient; the latter restores the shared-resource
premise and the sharp coefficient.

