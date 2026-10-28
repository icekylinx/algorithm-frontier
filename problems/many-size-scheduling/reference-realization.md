# Native binary workload realization and its finite solver costs

The [reference implementation](reference/workload.py) realizes the workload,
decomposition and per-machine rounding interfaces of the [main theorem](proof.md)
and the [private-slack finite-rank refinement](../../manuscripts/allocation-and-scheduling/many-small-sizes-private-slack-deficiency.md).
It accepts arbitrary complete integral job-rank tables, positive rational common
type sizes and their full mandatory totals. Empty systems, zero-rank types and
the empty physical ground are included. No assignment-cost budget is admitted.

## 1. Binary scaled-base decomposition on the original pair ground

**Lemma 1.** `decompose` returns integer bases of the binary-scaled original
type ranks whose sum equals the supplied aggregate workload, without constructing
copies of the multipliers or individual jobs.

**Proof.** The routine validates the original rank tables, positive integer
multipliers and the supplied nonnegative integer workload base of their sum.
It uses one variable per original type/machine coordinate. The imported
`BaseLP` represents a base of each scaled original rank, eliminating its last
coordinate using that type's scaled full total. Add one integral partition
count cap at each physical machine, equal to the supplied workload there.

The two ranks are the direct sum of the scaled original recipient polymatroids
and the partition machine polymatroid. Their intersection is integral.
The original scaled type totals sum to the supplied workload total. Therefore
the nonempty full-total face forces every machine cap to be tight as well.
Nonemptiness is the scaled polymatroid-sum decomposition statement, or directly
the pair-ground min-max proof in
[the binary workload lemma](../arbitrary-processing-scheduling/slot-surplus.md#8-reconstructing-every-original-job-and-bounding-the-load).
For a pair subset, intersect its typewise machine subsets. The resource-side
rank is at least the aggregate rank on that intersection, hence at least the
workload there, while the complementary partition rank supplies the remainder.
This proves the min-max lower bound at the full required total.

Exact active-system enumeration returns a vertex of this integral face, so
its scaled coordinates are integers. The program checks integrality, every
scaled original base and every original machine total before returning.
Dividing each component by its own binary multiplier produces a fractional
base of the original type with exactly the intended physical workload.
The variable ground has no expanded multiplier copies. <code class="math">\square</code>

## 2. Native upper-prefix restoration of every original type

**Lemma 2.** `upper_round` returns integer original job bases and increases
each machine's load by at most the largest size among the nonzero-rank input
types. It preserves original types jointly rather than rounding them separately.

**Proof.** Validate the fractional original type bases. At each machine, order
active types by decreasing original common size and impose the ceiling of every
cumulative fractional count, including the full prefix. These integer caps
define the chain polymatroid from the main proof, Section 2. Its direct sum
over machines contains the same fractional point as the original resource
direct sum. Their integral maximum-total face therefore has an integer vertex
with every original mandatory total.

The routine uses the same streamed exact active-system solver on this face
and checks the returned integer original bases. Summation by parts of these
upper prefixes proves the main proof's per-machine additive inequality.
Zero-rank types have identically zero original counts and are excluded from
the size order, so a large but unused size cannot enlarge the additive bound.
There is no allocation disposal, lower rounding or assignment-cost claim in
this construction. <code class="math">\square</code>

## 3. Full-machine dual, original recovery and the weak selector

**Lemma 3.** Every successful native hard target reconstructs original integer
job bases with the stated workload load bound, and its full failure is sound.
The private mode preserves its separate cap semantics.

**Proof.** Aggregate the original equal-largest-size ranks and form their
Boolean cap. Scale only the smaller positive-rank types, in binary, by the
chosen common quantum. Uniform workload box restriction must retain its
original full total. Construct the complement dual on the full physical
machine set. The imported box formula and binary coordinatewise augmentation
are exactly those in the already proved two-size corank construction.

The reference weak selector enumerates subsets of the original required
cardinality and tests the actual Boolean player rank and every dual resource
inequality. In private mode it contracts only an independently chosen private
player set: each candidate residual set must complete that fixed set to an
original player basis, and its dual quota is supported off the committed set.
It never contracts or recomputes the recipient dual. This exhaustive weak
selector is a finite reference implementation, not the main theorem's
rank-dependent normalized-prefix local search.

A full original target supplies the integer full-workload quota in the main
proof, and therefore a weak-quota basis. In private mode the spanning argument
supplies a full-quota basis of the contracted player matroid. Thus no weak basis
can be absent on a protected full target. After a private success, certified
private marginals permit insertion of the requested quota at the committed
coordinates. The program then extends that full-machine independent lower
vector to a dual base.

Complementing the dual base gives an integer original aggregate workload base.
Lemma 1 decomposes it among the original scaled smaller types; division gives
their original fractional bases. Lemma 2 restores their integrality with the
explicit largest-smaller-job additive term. The largest assignment remains
fixed throughout and is split among its original equal-sized types by Lemma 1
with unit multipliers. All originally zero-rank types retain zero vectors.
This proves every original type base and the main proof's target load estimate.

Private mode uses the companion's exact engineered quota, with no ceiling loss,
and inserts only actual private coordinates. Its computed closed-form threshold
is the companion's attained threshold. A cap rejection is returned distinctly
from original infeasibility and is never used to claim the original target
impossible. The reconstruction API itself also allows any independent lower
vector, including zero on a separately committed set; its original-load bounds
then belong to that caller's separate proof. <code class="math">\square</code>

## 4. Easy branches, the fallback and exact target search

**Proposition 4.** The native reference gives the main approximation with its
explicit additive term and the private refinement with its capped comparator.
Its separate actual fallback also retains the additive-largest-job guarantee.

**Proof.** One positive size is solved exactly by a capped aggregate base and
unit-multiplier decomposition. Below the largest active size, a nonempty job
system is infeasible. Above twice that size, the original all-job fractional
LP and Lemma 2 return an additive-largest-job schedule, within the easy-branch
coefficient. Both LP and rounding retain every original base. Empty systems
return their original zero counts.

The fallback uses this original all-job LP and upper rounding at every target.
An integer full target always supplies a feasible fractional point, so its
failure is sound, and every success has makespan at most its target plus the
largest active size. A one-sided search on the original load grid therefore
gives the fallback bound against the original optimum. Since that size is at
most the positive optimum, it also gives the main factor-two fallback.

The main workload search has genuine original failures and saves actual weak
upper outputs. The private search works on its engineered finer grid, whose
loads include the original optimum and cap threshold. Genuine infeasibility
and cap failure both exclude the capped comparator below the failed endpoint,
so the final upper endpoint is at most that comparator. Neither search assumes
monotonicity of successes. Positive off-grid target queries are rounded down
to their working grid: every original integer schedule load and private cap
threshold is on that grid, so this changes neither full-target feasibility
nor the cap decision and only improves a weak upper load estimate. Returning
the better actual schedule preserves both the workload and fallback bounds.
<code class="math">\square</code>

## 5. Actual reference time, binary space and evidence

The module imports only the intrinsic reference's generic mandatory-base
`BaseLP` and streamed `vertex` operations; its optional allocation, lower-
rounding and disposal adapters are not used. Exact rational elimination is
the canonical scheduling implementation. Rank validation, subset box queries
and binary base completion are reused from canonical complete-table primitives.

For physical-machine count <code class="math">q</code> and <code class="math">m</code>
original types, a base LP has dimension <code class="math">m(q-1)</code> when
the ground is nonempty, and dimension zero on the empty ground. With
<code class="math">L</code> actual rows, its streamed solver tests at most
<code class="math">\binom{L}{m(q-1)}</code> active systems in the nonempty case,
doing polynomial rational work and row tests per system. The weak selector
tests at most <code class="math">\binom{q}{h}</code> candidate original subsets;
private contraction changes this to the corresponding residual combination
count. These costs remain separate from the fast theorem's rank-local-search
and paid polynomial LP/intersection primitives.

Only the current active system, candidate set, full rank tables and current
output are retained. All scaled ranks, counts, multipliers, cap values and
rational vertices have polynomial bit length by exact determinant bounds.
Enumeration does not range over a count, denominator or artificial multiplier's
numerical magnitude. Thus the reference has polynomial rational workspace in
its complete explicit input and parameter encoding even though its local time
can be exponential. It stores no full vertex family or expanded service ground.

[check_workload.py](verify/check_workload.py) independently enumerates original
job bases and actual loads. Separate exact comparisons test scaled-base sums
and upper-prefix caps without using the workload or LP helpers in the oracle.
The suite covers original equal-largest-type recovery, large-job loops, zero
rank and empty grounds, Boolean-rank loss, rational sizes, private rank budgets
and genuine cap failures at originally feasible targets. Binary tests include
81-bit original counts, 81-bit scaled multipliers, fractional intermediate
original bases and an 81-bit accuracy denominator. They execute actual native
decomposition, rounding and target/optimization paths rather than a unit-copy
or numeric count-enumeration substitute. Finite evidence is not a proof by
enumeration, formal verification or external peer review.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0.
