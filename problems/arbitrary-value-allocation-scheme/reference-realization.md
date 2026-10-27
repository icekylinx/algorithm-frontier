# Native exact-budget profile realization

The [reference](reference/README.md) implements the complete target/profile and
original-grid optimization construction in [Theorem PA](proof.md). It accepts
complete original rank tables and exact rational data. Its finite active-system
LP implementation has a separately charged cost; it is not the theorem's
paid polynomial LP or weighted-intersection implementation.

## 1. Original representation and affordable zero target

**Lemma 1.** The accepted input has the original model of Theorem PA. The
zero-target method returns an affordable original player basis exactly when
one exists, and the output verifier uses only original feasibility.

**Proof.** The canonical intrinsic reference's table validator checks every
normalization, monotonicity and submodularity inequality and requires the
player table to be a matroid rank. Values, assignment costs, setup fees,
budget and accuracy are exact nonnegative rational data; eligibility is
represented by `None` in the original owner/type value matrix. All original
IDs, including original player loops, remain named. Such loops are never in
a selected basis; candidate subsets are streamed only on original nonloop
IDs, preserving the canonical nonloop basis-enumeration factor. Ignoring zero values and zero singleton capacities in
positive-target search is legitimate because unused units are allowed and
costs are nonnegative.

Greedily adding rank-increasing players in increasing setup-fee order gives
a minimum-weight original basis. Comparing its fee with the one budget is
therefore an exact zero-target affordability gate. The retained allocation
has zero original counts. Rank zero returns the empty basis and no finite
minimum on the empty selection.

The standalone verifier checks distinct original basis IDs and its original
rank; nonnegative integer original counts, zero outside the basis and on
forbidden coordinates; every original recipient-rank inequality; and the
actual sum of setup and assignment costs. It invokes no profile, LP, target
or rounding producer. It certifies feasibility, not a claimed optimum.

## 2. Occupied profiles and the integer comparator

**Lemma 2.** The native profile iterator enumerates exactly the states in
Sections 3--5 and 9 of Theorem PA, with polynomial delay and workspace per
occupied input coordinate. A full original integer target witness produces
a feasible enumerated profile LP.

**Proof.** For each eligible original positive coordinate, first cap its
value at the positive target. Equality at the small threshold is small;
the ceiling-minus-one index puts equality at an internal big-bin boundary
in the preceding bin. Only occupied bins are stored. The index and both
endpoints have polynomial bit length in the encoded accuracy and target,
even when the numerical number of unoccupied bins is enormous.

The canonical scheduling profile iterator is invoked on lower endpoints
divided by two. Its lower-sum cap of one is exactly the PA lower-sum cap of
two; its supplied count cap is the PA ceiling count cap. Explicit paused
frames stream the product across the actual selected basis. No recursion
depth depends on the number of occupied bins or selected players. The
all-zero completion injection in PA Section 9 proves the traversal cost,
and PA Section 10 proves both complete state-count envelopes. The stronger
partition bound depends on this actual pruned traversal.

The first-reaching capped integer suballocation in PA Section 5 retains
at most the ceiling count cap, has lower sum at most two, and meets the
profile's upper-endpoint-derived small requirement. Coordinatewise
restriction preserves original ranks and actual nonnegative cost. This
argument is deliberately about integer targets: capping a high original
value can destroy a fractional full-target witness. The target routine
promises sound failure for original integer targets, not fractional-OPT
approximation or equivalence of the capped fractional relaxation.

## 3. Actual joint LP, masks and disposal

**Lemma 3.** One native profile feasibility call is exactly its joint
original-resource LP. Independent resource vectors and optional unused
capacity are preserved without unit expansion.

**Proof.** For each resource, let `A` be its eligible positive-value owners
in the fixed basis, and put `f_A(S)=f(S intersect A)` on the full original
owner ground. This is the legitimate zero restriction. Its total is
`f(A)`; no mandatory original base has been asserted. Add one disposal
owner with rank `f(A)` on every subset containing disposal and rank
`f_A(S)` on subsets without it. This normalized monotone submodular rank
has the exact base correspondence

```text
x in P(f_A)  <=>  (x, f(A)-sum(x)) is an augmented resource base.
```

The reference reuses the canonical exact `BaseLP` coordinate elimination:
disposal is the last owner, so eliminating its coordinate leaves precisely
the original owner coordinates. All augmented rank rows and all
nonnegativity rows are present. Bin count equalities are imposed in both
directions; the small group has the original true utility lower bound;
assignment cost is charged at original coefficients against the budget
remaining after the unchanged selected setup fee. The same resource
continues to govern all selected players and all bins. No type or resource
capacity is duplicated.

The bounded rational system has a vertex whenever nonempty, including on
a lower-dimensional face. Stream full-size independent active systems,
solve exactly and check every row. Before enumeration, repeated coincident
single-coordinate lower and upper bounds are substituted exactly. This
affine bijection preserves feasibility, vertices and every linear objective
up to a fixed constant. Constant negative rows are rejected immediately;
tautological constant rows can be discarded. Zero-dimensional
systems are decided by their constant rows. This yields a fractional
original-resource witness or exact infeasibility. The separately described
active-system factor pays for this finite implementation.

## 4. One integral point preserves cost and every prefix

**Proposition 4.** Native recovery from a verified profile witness returns
an original integer allocation satisfying the same scalar budget and the
PA target guarantee. Every lower-prefix inequality and the actual cost
comparison hold at this one point.

**Proof.** The supplied witness is checked against the augmented base
ranks and totals, actual budget, bin equalities and small utility rows.
For each augmented resource, form the complement rank in PA Section 6
using its original augmented singleton caps. The complement of the witness
is a base of that rank.

Order each selected player's big bins by decreasing lower endpoint,
followed by small coordinates in decreasing true value, with big groups
first at a tie. Add the ceiling cap for every complement prefix,
including the full prefix. These are the integral chain-polymatroid
constraints from PA Section 6. Disposal caps are already implied by each
complement resource's singleton bound. The intersection of the complement
resource direct sum and these independent chains is integral. Its
full-total face contains the fractional complement witness, and total
forces every individual complement resource to remain a base. Thus its
vertices are integral, without intersecting an integral polytope with an
extra budget halfspace.

Stream the active vertices of this face and minimize the negative of
actual assignment cost on the complement, with disposal coefficient zero.
An exact optimizer exists by boundedness. Complementing back gives no
more original assignment cost than the input witness, since the cap-cost
constant is unchanged. The original setup fee is unchanged as well.
Discard only disposal; unused original capacity remains optional.

The complement ceiling at each prefix is exactly a primal floor lower
bound. At big-bin boundary prefixes, the fractional counts are integers
by the verified bin equalities. The summation-by-parts proof in PA Section
7 therefore has zero big-boundary error. Only the small group loses at
most its largest value, bounded by the small threshold. PA Section 8 then
proves the full requested relative accuracy; a generic largest-original-
value charge would not prove it. Integral output need not keep individual
big-bin equalities. The native output verifier and actual utility check
are additional executable checks on the resulting original allocation.

## 5. Original-grid optimization and full theorem audit

**Theorem 5.** On every affordable original instance the native optimizer
returns a valid allocation of at least the requested relative fraction
of original integer optimum, with the finite LP cost below. Unaffordability
is detected even at zero utility.

**Proof.** Enumerating actual original bases and exactly the PA profiles,
Lemma 2 and Lemma 3 show that target failure excludes every original
integer full-target witness. Proposition 4 shows that success supplies
the relaxed original utility at that nominal target. The affordable
zero allocation initializes search. Use the rational gcd quantum of the
original positive pair values and the original total-value upper bound.
Every original integer minimum, including optimum, is on this grid.
The upper endpoint starts strictly above optimum and remains so after
every failure. At adjacent integer grid indices the saved nominal lower
endpoint is at least optimum, regardless of nonmonotone weak successes.
Keeping the best actual output preserves the requested guarantee. The
number of target calls is polynomial in the original binary value/rank
encoding, not the numerical upper endpoint. No extra accuracy division
is introduced by search.

The complete mathematical audit checks original integer capping, the
first-reaching count bound, exact occupied-bin ties, the joint original
resource LP, disposal and complement duality, integrality and one actual
cost objective, the zero-error big boundaries, and the final accuracy
inequality. It also checks the pruned profile tree, binary indices and
state counters, partition generating-function envelope, all-input failed
profile costs, and one-sided original-grid search. These match the
unrelated-value additive dependency's scalar-cost rounding construction.
That dependency's fractional comparator does not silently replace PA's
integer comparator. The ICALP 2025 cost-preserving-rounding primary source
is an antecedent, not an imported theorem asserted to provide this
recipient-polymatroid profile solver.

## 6. Actual reference costs and boundaries

The complete original rank tables are charged input. Validation scans all
original subset pairs; each augmented table has twice the original
number of entries. The exact LP accounting for a single call is

```text
q = original owner count (including named original loops)
m = original resource type count
ambient dimension = m*q       # one disposal owner eliminated per type
D = actual free dimension after exact fixed-coordinate substitutions
R = actual distinct nonconstant row count after those substitutions
D <= m*q
active systems examined <= binom(R,D)
```

There is polynomial exact Gaussian/row-check work per active system.
Feasibility may stop at its first vertex; cost recovery scans the active
systems to obtain an exact linear optimizer. Both are streamed, retaining
one active system, one candidate and the best point. No numeric integer-
count enumeration, resource-unit expansion or accuracy-sized table is
used. Determinant bounds give polynomial bit lengths for vertices and
objectives in the encoded input and target. The target grid also has
polynomial bit length.

Thus this reference adds its potentially exponential active-system
factor to the canonical actual-basis/profile enumeration. The mathematical
PA time envelopes assume named paid polynomial LP, rank/SFM and weighted
intersection primitives. Those mathematical constructions are complete;
the finite reference does not claim their fast primitive costs. It uses
polynomial rational workspace in the complete-table encoding and full
accuracy encoding. Multiple independent exact budgets, player-dependent
coupling constraints between resources and fractional basis selection are
outside both contracts. Internal review and exact finite checks are not
proof-assistant formalization or external peer review.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
