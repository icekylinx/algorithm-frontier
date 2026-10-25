# Focused audit of relevant conservative blockers

**25 October 2026. Reviewer: transfer_baselines.**

The addendum `general_resource_relevant_blocker_addendum.md` passes.
This audit supplements `general_resource_all_remaining_source_audit.md`;
it does not alter the all-remaining manuscript or retroactively assign
resource-sharing properties to its deliberately coarse blocker rule.

For a candidate c, mark all unmarked current matching records whose
resource-index sets intersect c. At each used resource j, this removes
every unmarked matching receiver at j. Thus, for every old selected
subset Z, the prospective reserved set before adjoining p(c) is both
an independent deletion from Q_j(Z) and a subset of X_j union Y_j.
Availability again puts p(c) outside its span. At every unused resource
there are only deletions. The simultaneous all-subsets invariant follows
without executing a subset test.

An empty relevant group is sufficient even when unmarked matching
records elsewhere remain. None of those records uses a resource of c,
so none appears in an affected recipient-matroid reservation. The fresh
and stored free-center exchange arguments require precisely this joint
feasibility, not that the complete matching is marked. Distinctness,
group retirement, lower-prefix identity and the player-flat invariant
therefore retain their earlier proofs.

Each newly designated blocker now shares at least one resource index
with its center. Records remain unchanged until they are removed from
the matching; a replacement is a new record. Consequently that shared
resource remains present for every surviving blocker in the group.
This is enough to recover the sharp star charge:

* A singleton center has value at least B. Any minimal B-blocker sharing
  its resource is the same-resource singleton. A star with t blockers
  costs at most (t+1)u<=2tu.
* A nonsingleton center uses only resources below B. A minimal blocker
  sharing one cannot contain a resource of value at least B, since that
  would itself be a sufficient singleton. Every bundle in the star has
  value below B+min(u,B), and there are at most 2t bundles.

The resulting coefficient is

\[
 C_R(B,u)=\max\{2u,2B+2\min(u,B)\}.
\]

The sum is over designated stars, not disjoint resource names. The
rank-cover inequality only needs the sum of their service values.

For tau=1/lambda and rho=(r-1)/r, the strict fractional lower bound
and this upper coefficient give tau B+rho C_R(B,u)<=T. At positive
gap Delta, gamma=min{1/2,Delta/(2C_R)} is safe. For T>0 and B>0
the denominator C_R is positive, so there is no zero division.

Solving the three pieces gives B0=T/(tau+4rho), with

\[
 B^*=(T-2\rho u)/(\tau+2\rho)\quad(u\le B_0),
\]

\[
 B^*=B_0\quad(B_0\le u\le2B_0),
\]

\[
 B^*=(T-2\rho u)/\tau\quad(2B_0\le u<T/(2\rho)).
\]

Adjacent formulas agree. Rank one is the separate rho=0 case
B*=lambda T. The upper endpoint is a boundary of this sufficient
certificate, not a proved integrality gap or algorithmic lower bound.

The group can be found by scanning explicit current matching bundles.
All actual work stays polynomial per charged state. Since the state
updates and signature changes are unchanged, the exact rank-exponential
and positive-gap rank-quasipolynomial counts still hold without a
recipient-rank factor. The fat threshold leaves u<B0, so the final
arbitrary-size ratio remains lambda^-1+4-4/r, or that value plus eta.

This is a valid strengthening of the small-resource relaxation guarantee
and a more selective implementation. It does not improve the leading
five in the final exact-oracle arbitrary-size guarantee.
