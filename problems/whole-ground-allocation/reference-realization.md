# Realization of weighted prefix omission, streamed covers and rational recovery

The [reference](reference/README.md) implements the actual combinatorial
algorithms of the selection, adaptive-selection, global-conversion and
rational-optimization manuscripts. Its native selected-flow client calls
real original-network separation and exact certificate recovery. It does
not replace the prefix recursion with exhaustive selected-set enumeration.

## 1. Exact first-crossing enumeration and its local cost

**Lemma 1.** `first_crossings` lists exactly the first-crossing certificates
in the selection theorem, with its full unfinished-state accounting and
polynomial workspace, including binary-large ratios.

**Proof.** Each DFS record stores a prefix length, its one and zero counts,
its deleted original IDs and its binary word. The one budget is the current
omission deficit. The zero budget is exactly the ceiling of the ratio minus
one times that deficit, less one. Check the strict density inequality before
extending a record. On its first violation emit it and do not recurse below
it. Otherwise append either bit whose count budget and original-order length
permit it. Thus every emitted word has precisely the proper-prefix and final
strict-violation properties. Its last bit is one.

Every required word fits both budgets: its zero count is strictly smaller
than the ratio minus one times its one count. Every earlier prefix fits as
well. Consequently DFS reaches and emits it. No density-crossed word is
extended, so the cylinders are prefix free. The selection proof's Bernoulli
mass bound and the injection of same-length unfinished words into completed
count-budget words therefore apply verbatim to the actual states visited.
Dead ends are counted; they are not silently treated as free failed work.

Only an original-order-length word is stored. The numerical zero budget is
an encoded integer, never an array size or loop limit independent of that
length. An explicit DFS stack has at most one pending sibling per word
position; storing its polynomial-size records uses polynomial workspace.
Exact rational cross multiplication decides every strict boundary. No
Gamma value, entropy or sampled random bit is used by the enumerator.

## 2. The actual weighted recursion and attaining adaptive choices

**Proposition 2.** `gap` implements the selection theorem and its protected-
witness adaptive extension, with the original fixed cardinality and stated
all-input corank bound, provided its paid interfaces satisfy their contracts.

**Proof.** Every new frame first calls its restriction selector and counts
that work even when it rejects. A choice is checked for distinct original
IDs, the required size and containment in the current allowed ground. Query
weak service on that whole allowed ground, inserting zero in all other
original coordinates. Membership permits discarding outside the selected
choice by downward closure. A successful adaptive choice retains the exact
attaining completion used to define that node's residual region.

A rejected query must supply a nonnegative, nonnegative-capacity row that
is strictly violated; the program checks these algebraic conditions.
Global validity is a mathematical oracle contract, not inferred from local
violation. At positive residual deficit, sort original IDs by decreasing
row coefficient with deterministic original-ID ties. Pause exactly Lemma 1's
certificate iterator in the frame. For each output, create the child obtained
by removing its one-positions. At deficit zero a violated query fails without
an invalid positive deletion. All failed selector children are processed and
counted, rather than pruned from the running-time argument.

In a fixed region, the weighted omitted-mass and layer-cake argument proves
that a protected full-target selected set has one enumerated child retaining
it. In an adaptive region, the exact minimum completion and the single
original protected completion give the same invariant, as proved in
[adaptive selection, Sections 4–6](adaptive-selection.md#4-the-recursive-algorithm).
Every child recomputes its own exact choice and separator; no old row is
reused to describe a changed region. Induction gives completeness and sound
full-target rejection. Weak success need not certify its nominal full target.

The prefix-free branch inequality and Lemma 1's actual local-state bound
are precisely the recurrence inputs in
[selection, Sections 5–6](selection.md#5-an-explicit-certificate-enumerator-and-its-complete-local-cost).
Their all-input bound pays for each processed node, rejected selector and
unfinished word. Omission depth is at most original corank. An iterative
stack avoids a language recursion-depth restriction, and one paused
polynomial-space iterator per depth remains polynomial space. Context and
row sizes have the uniform bit bounds required by their paid interfaces;
they do not accumulate old target descriptions.

The explicit-row adapter supplies genuinely globally valid fixed packing
rows. The unrestricted cost selector returns the cheapest actual subset,
while the two-matroid selector uses the canonical weighted intersection
with outside elements made loops in both matroids. Its attained minimum
and fixed threshold implement exactly the family restriction interface.
Signed selection costs are allowed because cardinality and the exact
minimum remain fixed; a scalar completion/setup budget still uses its
actual original nonnegative costs.

## 3. Real logarithmic-block covers and streaming

**Proposition 3.** `cover_seeds` and `whole_ground` realize the deterministic
whole-ground conversion and its corank-profile refinement with polynomial
workspace for a supplied admissible rational base.

**Proof.** For each block size and local omitted count, evaluate every
possible seed size using exact binomial coefficients and powers of the
supplied rational base. Choose a minimizing size. The local universe is
all omitted-count subsets and the candidates are all subsets of that seed
size. Greedily choose a candidate covering the most still-uncovered local
sets; fixed combination order resolves ties lexicographically. Delete the
covered universe elements and repeat. This is exactly the uniform-fractional-
cover/greedy construction of the global proof, including empty seeds.

For at least four original elements, blocks have floor binary-logarithm
size, with a final possibly shorter block. Precompute only those local
covers, then stream the bounded count profiles whose sum is the original
corank. The implementation also counts rejected count profiles; their
number is no larger than the full product bound already charged by the
proof. Stream the Cartesian product of the chosen local covers and map
its block masks back to original IDs. No global seed list is stored.
For smaller grounds, directly enumerate full-size omitted complements,
calling the extension at residual deficit zero.

Every original omitted set has one matching count profile and contains
one listed local seed per block. Their union is one streamed seed contained
in that same omitted set. Thus its protected original selected set survives
an extension call. Every accepted callback output must be a legal weak
solution; full exhaustion then excludes all full witnesses. The wrapper
never repeats approximation across blocks. A client with an additional
structural outcome must propagate it as a distinct result, not count it
as failed extension.

The exact local minimizing-size identity, greedy cover bound, profile
factor and full extension work are those in
[global conversion, Sections 2–7](global-conversion.md#2-an-exact-local-weighted-count-identity).
They pay for every seed, failed extension and rejected profile. The same
local minimum satisfies every analytical averaging parameter, so the
[corank-sensitive profile refinement](../../manuscripts/allocation-and-scheduling/global-gap-corank-profile-bound.md)
applies to this identical algorithm. The executable does not estimate its
unknown analytical optimizer.

A logarithmic block has at most the original ground size many local sets.
All stored local covers, candidate lists and universes therefore occupy
polynomial space. Product iterators retain only local pools and current
indices. Powers used in local rational comparisons have exponent at most
the block size and polynomial bit length even for a binary-varying supplied
base. Arbitrary huge numerical approximation parameters are not expanded.
Sharp nonrational Gamma displays retain their fixed-rational-accuracy
comparison proof; the software here accepts a supplied rational bound.

## 4. Fixed-family rational search and native flow execution

**Proposition 4.** `rational_optimize` implements the original fixed-family
rational-comparator lemma without splitting its requested accuracy.
`flow_gap` implements actual fixed/adaptive selected-flow omission with
exact primal/dual recovery, using the canonical finite LP backend.

**Proof.** The comparator helper constructs exactly the denominator-bound
rational grid, initializes its external upper endpoint strictly above the
supplied value bound, and performs integer midpoint search. `None` is the
only failure value, so a legal choice encoded by zero is retained correctly.
Every failure is strictly above the original fixed-family optimum; weak
successes may be nonmonotone. At adjacent endpoints the saved nominal lower
value is within one grid step of the comparator. Reoptimize the original
saved set, not its artificially grid-constrained LP. The lemma's rational
gap bound then gives the full requested relative factor. The helper checks
returned value encoding, denominator and saved weak lower bound; validity
of the uniform family bound and gap promise remains the declared model.
All loop counts are logarithmic in binary grid indices, not proportional
to the denominator bound's numerical value.

The flow client materializes every original budget and setup record before
repeated calls. Without setup, its separator is the canonical fixed original-
network normalized Farkas separator. With one setup/routing budget, the
selector attains minimum setup on the restricted family and the client
subtracts that very choice's original fees. A negative residual rejects
the node; otherwise the routing-charge row uses precisely that residual.
The selected-flow/shared-setup protected-witness proof therefore instantiates
Proposition 2 without changing network capacities or original coordinates.
Fixed extra routing budgets remain in the same separator.

At success, optimize the original returned set with all original routing
and setup constraints, then return its exact primal/dual certificate.
Its rate is at least the queried weak target, or an invariant exception is
raised. This is actual routing recovery. The finite Bland-simplex pivot
bound remains charged: the native integration does not turn that backend
into a polynomial-time LP algorithm merely by using the fast combinatorial
recursion. The generic engine's polynomial-oracle theorem and the native
backend's complete finite cost are distinct valid statements.

## 5. Complete transfer and lower-bound audit

Internal mathematical review covers the whole main transfer theorem and
all six canonical shared components, rather than treating executable
examples as an asymptotic proof. The checked dependencies include:

- One-value exact-budget allocation: fixed original bases, separately exact
  unit endpoint, unchanged positive-quota region, integral full-total cost
  recovery and one-sided integer optimization.
- Compulsory two-value arbitrary-cost allocation: attaining original heavy
  assignments, all heavy options outside omitted light seeds, exact small
  quota recovery, the one-unit and pure-heavy exits, high-target LP rounding
  and fixed value-grid search.
- Arbitrary intrinsic values with one scalar assignment budget: the actual
  parallel-extension/type-copy weighted completion, fixed split/support
  joint benchmark, all-support globalization, and disposal/complement-prefix
  exact-cost rounding. Heavy and light resource types remain disjoint;
  equality at the optimum threshold belongs to the heavy side.
- Two-size scheduling: original mandatory job totals, Boolean-rank failure
  as a polynomial branch, full-physical duality, unchanged dual under seed
  omission, binary base completion and exact one-unit/high-target endpoints.
- Selected flow, explicit adaptive scenarios and one shared setup/routing
  budget: actual original set selection, globally valid nonnegative Farkas
  rows, attaining setup, fixed-family denominator bounds and original exact
  reoptimization. Flow remains splittable and scenario lists remain explicit.
- Integer-quota tradeoffs: every small nominal target uses a saved exact
  unit witness; larger quotas obey the sharp integer ratio. Scalar budgets
  are recovered by minimizing one objective on integral faces. Fixed
  tradeoffs permit exact constant-degree algebraic comparisons; variable
  binary parameters retain the rational upper-envelope alternative.
- The balanced hidden-subset ranks are normalized, monotone and submodular;
  the raised hidden row consumes exactly the available slack. Strictly
  better allocation or scheduling factors force the unique hidden set.
  The complement-dual scheduling oracle has exactly one exceptional query.
  Central-binomial many possible hidden sets give the stated deterministic
  black-box barrier, without explicit-input hardness or an optimal threshold
  base claim.

The additional selector-cost and corank-profile companion proofs have also
been checked at their actual input/oracle, comparator, grid and forced-seed
interfaces. This does not certify independent unbudgeted intrinsic-value
family companions merely because one budgeted intrinsic transfer is valid.
The public monotone-local-search base formula retains its attribution and
public rounding theorems retain their named dependencies. Mathematical LP,
SFM, integral intersection and decomposition costs remain paid and explicit.

The executable scope is the four generic combinatorial/search primitives,
actual certified selectors and the native flow integration. It does not
implement every allocation/scheduling recovery, arbitrary algebraic-number
input, implicit uncertainty family or an externally unproved oracle.
Internal review and finite checks are not external peer review or proof-
assistant verification.

**Attribution:** icekylinx and GPT-6 Astra Pro.
