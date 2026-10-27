# Exact mixed-target cover-chain reference and scoped core audit

The [native reference](reference/README.md) implements the cover-chain (CC)
construction, bounded coefficient profiles and original signed-scalar
recovery. Its exact finite LP implementation has an additional active-system
cost. It does not implement UP's support-prefix interval compiler or all
refinements listed on the [result card](README.md).

## 1. Original model, masks and zero-target gates

**Lemma 1.** Preparation preserves exactly the original integer feasible
family. The original verifier checks feasibility and actual scalar value
without invoking preparation or a producer.

**Proof.** Input consists of a complete original normalized monotone integral
polymatroid rank table, original eligibility, nonnegative integer numeric
rows and targets with independent upper/equality/cover relations, and one
exact rational signed scalar. The canonical rank-table validator checks all
axioms. Optional vectors lie in the independent polytope; mandatory vectors
must have the original full rank as their total.

Every positive integer use of a coordinate exceeding an upper/equality
target is infeasible, so such a coordinate is masked. This includes all
positive coordinates in a zero upper/equality row. Zero covers are automatic;
all zero-target rows can then be dropped. Positive surviving row targets
bound the effective row count by total target. Original nonempty supports
are recorded after these masks; coefficient magnitudes do not distinguish
supports. The scalar is never counted as another target row.

A mandatory problem retains its original rank total and rejects masked rank
loss. An optional problem may instead complete to that total with one free
disposal coordinate; original feasible vectors are projected back after
recovery. Disposal is never added to the mandatory model. Eligibility and
original coordinate IDs, including masked zeros, are retained in the output.

If no rows or no nonempty supports remain, original numeric constraints
are automatic or impossible. Greedy polymatroid scalar optimization orders
eligible coordinates by signed weight, taking their rank increments. A
mandatory base uses every eligible coordinate in this order and retains the
full total. An optional minimum takes only negative weights; an optional
maximum takes only positive weights. This is the ordinary greedy linear
optimization rule on an integral polymatroid. The original verifier rejects
any impossible positive equality/cover. Thus these gates really run in
polynomial complete-table input time without numeric-rank iteration.

The verifier checks integer nonnegative original counts, eligibility, every
original subset-rank row, mandatory original total when required, every
original numeric relation and the exact signed scalar. It certifies a
feasible vector and its value, not an optimality certificate.

## 2. Shared chains with compressed identical layers

**Lemma 2.** The native chains represent every original feasible vector with
its scalar unchanged, and every feasible chain projection is original
feasible.

**Proof.** The [CC manuscript](manuscripts/mixed-target-cover-chain-compression.md)
proves the common-order stopping-prefix construction for each cover-row
permutation. Its layers are successive suffixes of that order. Upper and
equality coefficients stay original. A cover is credited its target-capped
coefficient until its removal, and zero thereafter. Its auxiliary interval
is from target through twice target minus one. The last unit of a stopping
prefix belongs to the still-active layer, including when several rows stop
on that same unit. Empty intermediate layers are legal.

Each copied coordinate retains its original scalar coefficient, and all
copies share the original resource. An optional disposal coordinate has zero
numeric and scalar entries and represents only original unused capacity.
No original real unit or signed scalar contribution is discarded.

The native compiler merges copies only if both their original owner and
entire auxiliary column coincide. Their resource projection and scalar are
identical, so any count split among these copies can be aggregated on the
retained copy and conversely split back. This preserves the whole polytope
and integer family. It also merges redundant disposal layers. It never
merges distinct original owners merely because their columns coincide;
those owners may have different scalar weights and resource interactions.

CC soundness follows because true covers dominate auxiliary credits, while
other rows and scalar values agree. Completeness uses one common conceptual
unit order and sorts first-reaching stopping positions. It is an existence
proof, not a resource-unit list in the implementation. Every original
integer optimum has a representative in one of the streamed permutations.
There are at most one plus the number of covers copies per eligible owner
before the safe identical-layer merge. This proves the lemma.

## 3. Occupied coefficient profiles and exact shared recovery

**Proposition 3.** The native profile solver exactly minimizes or maximizes
the original scalar within a chain, including detecting infeasibility. It
keeps one global resource and its original total.

**Proof.** Group copied coordinates by their complete auxiliary coefficient
vectors. Enumerate only occupied nonzero classes. At each explicit DFS frame,
the next multiplicity is bounded by remaining original rank and every
positive component's remaining upper allowance. The lower filters are applied
at complete profiles. Each partial state has a zero completion under the
upper caps, yielding the CC all-input traversal bound. There is no numeric
coefficient universe, numeric-rank coordinate list or recursive Python stack.

For one surviving profile, the global zero-vector class gets the original
rank minus its nonzero multiplicity sum. A positive remainder with no zero
class is infeasible. These prescribed class totals sum to the unchanged
original rank. The intersection of the shared-copy resource polymatroid and
the corresponding partition-count polymatroid is integral; on this full-total
face all class caps are equalities. The exact signed scalar can be optimized
on this face. This is one extra partition-count rank, not a third independent
resource or an arbitrary extra scalar side constraint.

The reference represents the shared-copy rank by one aggregate inequality
for each original resource subset: sum all real copies whose owner belongs
to that subset, and bound by its original rank. Complete inverse images and
nonnegativity show these are equivalent to all copied-subset rank inequalities.
The optional disposal coordinate consumes no original resource capacity.
With total fixed, its implicit complementary inequalities are automatic.
Consequently the code never materializes a rank table on the copied ground.

Eliminate one copied coordinate in each nonempty class by its exact prescribed
total. This is an integer-preserving affine bijection, retaining every original
rank and nonnegativity row. The generic PA active-system primitive further
substitutes coincident scalar lower/upper bounds exactly. Stream square active
systems, solve rationally, test every row and retain the best scalar. The
bounded integral face has an integer optimizing vertex when nonempty, even
on a lower-dimensional face. Zero-dimensional constant systems are checked
directly. Thus recovery either proves this profile empty or returns an
attaining original integer vector. The original output verifier checks its
projection and computed scalar independently of the compiler.

Taking the best value across every profile and chain, Lemma 2 proves exact
original optimization. Feasibility is decided by whether an answer exists.
A threshold on the same scalar is decided by its appropriate minimum or
maximum; optimizing a different scalar under an additional unbounded scalar
constraint is not an accepted interface.

## 4. Precisely scoped mathematical audit

The mathematical review in this increment covers:

- The complete central budget-classification proof (BC), including both
  original-support and total-target upper algorithms as its exact dependencies,
  monotonicity in both budgets, the hidden sparse-paving matroid lemma and
  bounded-error query transcript argument, both budget calibrations and the
  uniform lower constant. The lower statement remains worst-case under
  parameter budgets, not every exact parameter pair or every represented class.
- The complete unrestricted-support (UP) construction: zero-target preparation,
  exact-support composition/Vandermonde count, original-support block useful
  prefixes, binary stopping ordinals, polynomial interval-copy representation,
  exact interval-count rows, full scalar/mass preservation, support accounting,
  all-input enumeration and binary workspace. This is a mathematical audit;
  this reference does not implement the UP template/compiler algorithm.
- The complete CC reduction, direct bounded-profile recovery and its Bell
  injection giving a uniform total-target bound; the direct upper/equality
  support count also follows from RD Sections 3--5. Conceptual tokens and units
  in those counting/existence proofs are not constructed by the algorithms.

The BC lower proof is self-contained on the balanced-label and disjoint-clique
families it recalls. The balanced labels form a nonadjacent family of equal-rank
sets; complementary label pairs give the candidate count. The high-support
construction uses one hidden global matroid on all clique edges, rather than
independent resources per clique. The transcript differs only when the hidden
set is queried. The numerical calibrations give the stated uniform constant
for all sufficiently large budgets, with polynomial explicit non-oracle data.
These arguments establish rank-query bounds, including their stated randomized
scope, without claiming encoded-program ETH bounds or hardness of every
explicit representation.

The native solver uses CC's cover permutations and retains that explicit
factor; it does not claim UP's stronger mixed original-support running time.
For pure upper/equality rows there is no cover compiler, so its occupied
profile traversal is exactly the direct support-sensitive construction.
The paid exact intersection primitive and the finite reference LP cost remain
different implementations of the same recovery interface.

The other family members retain their linked statements and dependencies.
This increment does not review the seven approximation variants and constants,
single-objective refined exponent, fixed-dimension lower bounds, all encoded
ETH families, nonlinear aligned-band transfers, global/mandatory/robust
compositions, or every support-geometric refinement. They are neither marked
ready by this scope nor reclassified as mathematically unresolved merely
because their software is absent.

## 5. Actual reference costs

The complete original rank table and all subset-pair validation work are
charged input/work. The reference's copy and LP accounting is

```text
n = original coordinate count
s = surviving covering-row count
N <= (s+1)*(eligible original coordinates + optional disposal)
g = number of nonempty coefficient classes, including the zero class
D <= N-g       # actual free LP dimension after further exact substitutions
M = actual remaining nonconstant LP row count
active systems in one reference recovery <= binom(M,D)
```

There is polynomial exact Gaussian/row-check work per active system. Original
rank rows are represented directly, so row storage is polynomial in the
complete original table plus copied-coordinate encoding, not exponential in
`N`. A permutation, profile, current active system, best point and output are
streamed/stored one at a time. Determinant bounds give polynomial rational
record lengths in the full encoded data, including binary rank and targets.

The outer algorithm pays every cover permutation and upper-cap profile,
including failures. With named polynomial intersection/SFM primitives this is
CC's theorem cost; the native reference additionally pays the finite
active-system factor. Both use polynomial binary workspace and retain signed
zero-column costs and original mandatory totals. The zero-row/no-support gates
use actual greedy optimization, not this finite LP factor. No original unit
count, target-length resource ground or copied-ground subset table is expanded.

Internal proof review, exact finite checks and original-output verification
are not proof-assistant formalization, external peer review, or a public
priority claim for coefficient-count intersection.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
