# Original-table realization of the intrinsic derived-matroid transfer

The [reference](reference/README.md) realizes the exact original-player
adapter, actual near-two omission search and XP exact-half candidate
construction. The mathematical family is internally reviewed with its
published fallback and lower-bound boundaries. The reference's streamed
active-basis LP costs remain distinct from paid polynomial LP/intersection
primitives in those theorems.

## 1. Validated original ranks and exact derived geometry

**Lemma 1.** Every accepted input has the stated original matroid and independent
integral recipient polymatroids. The computed heavy-cover, union, dual and
loop-deleted parameters are exactly those of the canonical manuscripts.

**Proof.** The canonical rank-table validator checks normalization,
nonnegative integer entries, monotonicity and submodularity on every original
subset pair. Requiring the player rank at each subset to be at most its
cardinality makes it a matroid rank. Original values are exact nonnegative
rationals. Ignored zero types can always be given zero counts because unused
capacity is allowed.

Aggregate original heavy resource ranks and apply the integral unit-box
formula on every original subset to obtain their Boolean-cap matroid `N`.
Compute the original player dual by its complement formula, the union
`M* vee N` by its subset min formula, and the derived player matroid by
another exact dual formula. Its singleton nonloops and full rank give
precisely the loop-deleted corank. Every submask of each queried subset is
visited; no maximal-subset or singleton shortcut replaces those formulas.

Original player loops can remain as named IDs: each is a coloop of `M*`,
and hence of its union with `N`, since it can be added to any union set
omitting it through the dual component. It is therefore a loop of the
derived light matroid. These IDs never belong to a selected light basis
or recovered original basis. This is equivalent to deleting original
loops and restricting original resource ranks, while preserving the IDs.
Full original resource rows are retained throughout actual recovery.

The constructive rank identity and spanning lemma in
[player selection, Section 2](player-selection.md#2-the-rank-identity-and-a-stronger-completion-fact)
therefore apply exactly. The computed rank is the original player rank
minus the maximum common heavy-cover cardinality. Original player corank
alone is not substituted for this derived parameter.

## 2. Actual union decomposition and original heavy allocations

**Proposition 2.** Every actual derived light basis is completed to an original
player basis containing it, with one legal original heavy unit on every newly
selected player, in polynomial work in the charged table/pair representation.

**Proof.** The light complement is a basis of the union. Create two color
copies of its original owners. On that explicit ground, intersect the
direct sum of the original dual and heavy-cover matroids with the owner
partition matroid. A maximum common independent set covering the complement
is an actual disjoint union decomposition. The code finds it through the
canonical [certified weighted matroid intersection](../robust-bounded-certificates/reference-realization.md)
with zero costs, instead of enumerating candidate original bases.

The union-basis spanning lemma guarantees that its dual component extends
to a full original dual basis using only owners in that same complement.
The implementation performs exactly that restricted extension. Taking its
complement gives an original player basis still containing every retained
light owner. The other selected owners remain a subset of the original
heavy component, and hence are Boolean heavy-independent.

The canonical exact unit scenario test on the original heavy type tables
then assigns one unit to those owners, retaining actual original type IDs.
Their heavy feasibility is not inferred from aggregate count totals alone.
No original unit is copied, even for binary-large capacities. Empty derived
rank uses this same recovery with an empty light basis and zero light
counts, bypassing the light LP entirely. It is a pure-heavy case, not a
finite objective on an empty light set.

## 3. Exact intrinsic workload oracle and real omission

**Lemma 3.** The original weighted workload rows realize the fractional
light-service region. Their exact fixed-basis common optimum has the
uniform denominator bound used by the native rational search.

**Proof.** On every original owner subset the workload rank is the sum of
its original light ranks multiplied by their intrinsic values. A uniform
service vector on a fixed nonempty light set belongs to that rank polytope
exactly when every original subset row holds. Thus its exact common optimum
is the minimum workload-row capacity divided by the number of selected
owners in that row, omitting rows meeting no selected owner.

Attainment in actual light resources follows from the
[binary workload decomposition](../arbitrary-processing-scheduling/slot-surplus.md),
Lemma 1. Choose a rational quantum making all original values and the queried
service integral multiples. Scale the workload rank, extend the independent
service to an integral aggregate base, decompose it among the scaled
original resource bases on the explicit owner/type ground, and divide by
the integer multipliers. This yields fractional original bases meeting
the service. All scalars retain polynomial bit length and no multiplier
is expanded into copies. Conversely, summing any actual allocation's
original rank rows gives every workload inequality, proving equality of
these service models.

Let `L` be the least common multiple of the active value denominators.
Every row capacity is an integer divided by `L`. Dividing by a selected
intersection size at most the original owner count gives a reduced
denominator at most that count times `L`. This is a uniform bound over
all fixed derived bases and is independent of the search target. The
sum of all original light resource values is a valid upper bound.

**Proposition 4.** The native near-two search uses actual first-crossing
omission and original fixed-basis rational reoptimization, preserving the
full requested accuracy before the one largest-light-unit rounding loss.

**Proof.** For each fixed split, the permitted family consists exactly of
bases of that split's derived matroid, with loops forcibly omitted. Greedy
rank extension is its exact restriction selector. Every original workload
rank row is explicitly available and nonnegative, so exact row scanning
is a valid fixed-region separator. The native method invokes the canonical
[weighted prefix recursion and rational comparator search](../whole-ground-allocation/reference-realization.md)
on those actual rows. It does not replace its selected-basis search by
exhaustive basis enumeration.

Forced derived loops reduce the starting deficit to exactly the loop-deleted
corank. The canonical proof pays for failed selectors, zero-deficit exits
and unfinished prefix words. The rational search uses Lemma 3's fixed
family, uniform denominator and original analytic fixed-basis optimum.
It therefore returns the full relative-accuracy fractional comparator,
including zero light service, without splitting accuracy or looping over
a numeric denominator. All splits are fixed before their target searches;
skipping one whose derived corank exceeds the budget is never failure of
an original target.

## 4. Original fractional realization and joint integral lower rounding

**Proposition 5.** Native recovery returns actual original integer resources
whose light value loses at most one largest light unit per retained owner.
It uses no numerical unit expansion, with the separate finite active-basis
cost described below.

**Proof.** Impose every original light resource base equality, eliminating
its last-owner coordinate. Keep every original subset-rank and coordinate
nonnegativity inequality. Add the exact utility lower bound on each retained
light owner. Lemma 3 and original base extension guarantee nonemptiness.
Every coordinate is bounded by an original singleton rank. Enumerating
full-size active systems, skipping singular ones and checking every row
therefore finds a vertex even on a lower-dimensional feasible face. The
zero-dimensional case checks all constant inequalities directly. Exact
Gaussian elimination yields actual fractional original base vectors.
No reduced resource rank or dropped original total replaces those vectors.

For each type complement its fractional base inside the vector of original
singleton ranks. The dual resource rank is formed on the full original
owner ground. At every owner, order the light types by decreasing value
and cap every dual prefix, including the full prefix, by the ceiling of
its fractional count. These caps define integral chain polymatroids.
Their direct sum intersects the original complement-resource direct sum
on its full-total face, which is integral. The fractional dual witness
belongs to this face.

The same active-system vertex routine finds an integral point there.
Each resource remains a dual base, so complementing gives legal integer
original bases. Every primal owner prefix is at least the floor of its
original fractional prefix. Summation by parts in decreasing values
then loses at most the largest light value at each owner. This is exactly
the [lower-prefix rounding proof](../unrelated-values-additive/proof.md#5-one-integral-rounding-preserves-every-prefix-and-the-cost)
with zero costs; no independent rounding of types or assumption about a
budget halfspace is used. The code checks integrality, original resource
feasibility and the actual lower-value inequality.

Add the original heavy assignment from Proposition 2. Heavy and light type
sets are disjoint, so they consume no common resource capacity. Discard
counts outside the recovered original player basis. This preserves every
selected owner's utility and every resource inequality. The standalone
output verifier checks only original basis membership, original integer
counts and every original resource row, without any union or LP search.
It proves feasibility, not optimality or a threshold-parameter promise.

## 5. Near-two, exact-half endpoints and full-family audit

At the near-two optimum threshold, the canonical optimum-complement proof
supplies one derived basis among the optimum's light-only owners. Its
fractional light optimum is at least the original integer optimum.
Proposition 4 retains the requested relative fraction and Proposition 5
pays one largest light unit, strictly below that threshold. Original heavy
units meet the threshold on every other selected owner. The best actual
candidate therefore has the main and optional-player near-two guarantees
under their respective exact derived-corank promises. In the compulsory
case the construction is the free-player specialization, including its
coloop-deleted refinement.

The native exact-half method instead enumerates all derived-basis complements
on permitted splits and reoptimizes each fixed light basis exactly through
Lemma 3. At the exact half-optimum split, its list contains the protected
basis. Its rounded light value is at least the optimum minus the largest
light unit, strictly above half. Heavy completion supplies the other half.
This realizes the XP and zero-corank candidate constructions with the
separate LP reference factor. No zero-gap invocation of the prefix theorem
is used. With a supplied quantitative light margin, the native near method
at that accuracy yields the quantified exact-half endpoint by the same
inequality in the canonical proof.

The complete mathematical audit also checks:

- Derived rank identity in both directions; union-basis spanning before
  extension; preservation of the specific retained light basis; and the
  optimum supplying a contained light-only derived basis.
- Original loop restriction, binary weighted-sum decomposition and
  full-accuracy additive comparator recovery; empty heavy/light/rank
  branches and equality on the heavy side of every split.
- The public fixed-constant fallback: [Bamas et al., arXiv:2307.08453v1,
  Theorem 4 and Definition 7](https://arxiv.org/html/2307.08453v1) give the
  compulsory full-resource-base `8+zeta` algorithm. The optional-player
  dummy resource is the original dual matroid, with value above total
  original value. Full original base extension proves that the augmented
  optimum dominates the original optimum. Extending the returned dummy
  recipients to a dual basis recovers original selected owners receiving
  no dummy, proving the stated fallback. Fixed positive slack is retained.
- Exact-half XP enumeration and the quantified-margin FPT regime use
  their half-optimum parameter, rather than the smaller near-two
  threshold. Arbitrarily tiny strict slack supplies no uniform FPT
  consequence. The two-unit coverage augmentation counterexample is
  valid, including its private-resource strengthening. A modular bonus
  helps arbitrary output bases too and proves no exact-half obstruction.
- The refined-parameter-zero hidden ranks are valid integral polymatroids
  with free Boolean cap. Near-two's exact threshold convention makes the
  refined corank zero, while every strictly-better-than-two output still
  identifies the hidden set. This is deterministic rank-oracle complexity,
  not explicit-table hardness, a lower bound for the unrefined heavy rank,
  or resolution of the unrestricted exact-half FPT question.

The broader deficit/fat-cover manuscript supplies structural context but
its local-search theorem is not imported silently into this corank proof.
The canonical optional and exact-half manuscripts prove their actual
adapters and target interfaces. Their named exact LP/SFM/intersection,
polymatroid decomposition and public fallback dependencies remain paid.
Missing software for a named polynomial primitive is not an unresolved
mathematical interface.

## 6. Exact implementation costs and software boundaries

The complete original rank tables are charged input. Their axiom validation
scans all subset pairs. Boolean and union table construction scan every
submask per queried subset. This is polynomial in the complete-table
encoding, but is not a polynomial rank-only procedure obtained by
materializing all subsets. Actual union decomposition and original heavy
assignment use polynomial explicit pair grounds and the certified weighted
intersection backend.

The exact copyable program accounting is:

```text
q = original owner count
m = number of light types for the current split
D = m * max(0,q-1)
L = the actual inequality count in one recovery LP
active systems inspected by one vertex call <= binom(L,D)
```

There is polynomial exact Gaussian/feasibility work per active system.
Thus the light LP realization and rounding may dominate the theorem's
fast corank bound. A streamed active-basis iterator retains only one
system, candidate vertex and current records, so the implementation uses
polynomial workspace in the charged input, while its time includes this
potentially exponential finite basis factor. All counts, targets and
intermediate rational entries have determinant-based polynomial bit
length. No loop is proportional to a binary resource count or workload
quantum denominator.

The native near method executes real prefix selection and rational search;
the exact-half method alone enumerates basis complements. The default
implementation supplies no unconditional public fallback when the parameter
promise fails. A supplied fallback callback is checked for original
feasibility and retained by actual value; its approximation and cost
contract are separately paid. The mathematical theorem includes the named
public fallback independently of this software boundary. No setup/assignment
budget, unrelated per-owner values or coupled local resource constraints
are introduced.

Internal mathematical review, exact finite examples and original-output
verification are not proof-assistant verification or external peer review.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
