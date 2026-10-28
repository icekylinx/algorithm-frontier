# Exact occupied-profile and joint recovery realization

The [reference module](reference/profiles.py) implements the semantic profile
construction of [Theorem PS](proof.md), with a reusable joint machine-plan
interface for the [bucket theorem](../processing-bucket-tradeoff/proof.md).
The input is a complete rank table for every original job type on a finite
physical-machine ground, arbitrary nonnegative rational machine/type times and
costs, eligibility masks, one nonnegative rational budget, and exact rational
accuracy in the theorem's domain. Original full ranks remain mandatory.

## 1. A general data adapter and one joint finite solver

**Lemma 1.** `JointBackend.fixed_vertices` represents exactly its supplied
fixed plan and original mandatory bases. `recover` gives original integer
bases of cost no greater than its successful fractional witness, preserving
every integer group cap and the upper-prefix bounds of every load group.

**Proof.** The data adapter invokes the canonical two-time validator on the
same rank tables, costs and budget, with zero processing times on precisely
the original eligible pairs. This validates dimensions and complete integral
rank tables without imposing a two-positive-times limitation. It then checks
every actual processing time separately for exact nonnegative type and value.
The unchanged actual times are passed to the shared resource/LP backend.
No processing value in the scheduling model is replaced by the proxy.

A plan's count and load groups are checked to partition its allowed original
pair coordinates, without overlaps; each group belongs to one physical machine.
Count caps must be nonnegative integers. The LP consists of all original subset
rank constraints, all coordinate nonnegativity constraints, zeros on forbidden
pairs, the plan's count/load rows, and the original scalar cost row. The shared
coordinate elimination uses each type's original full rank, rather than any
masked rank. Thus every original mandatory amount remains exact and a masked
rank loss is a real infeasibility. All coordinates are bounded by original
singleton ranks, so exact rational active-set enumeration lists every vertex
even on lower-dimensional faces, by the
[canonical vertex proof](../two-time-scheduling/reference-realization.md#1-exact-lp-and-mandatory-totals).

At recovery retain the same allowed pairs and original resources, the integer
partition count caps, and the full descending-time prefix ceilings of each load
group. Zero-time coordinates remain in those prefixes and their original bases.
These disjoint partition and chain components form one integral machine
polymatroid. The fractional witness belongs to it and to the original resource
direct sum at the original total. Their maximum-total intersection face is
integral, so an integer minimum-cost point has cost no greater than the witness.
The reference enumerates the bounded integer reduced vectors and chooses that
minimum. The budget inequality is omitted from this integer optimization;
the budget is preserved through cost comparison, not by assuming a budget-cut
polytope is integral. All types are recovered jointly. <code class="math">\square</code>

## 2. Exact occupied-bin profiles and binary iteration

**Lemma 2.** `ProfileBackend.plans` streams exactly all profiles on its occupied
bins that satisfy Theorem PS's count and lower-load inequalities. It stores no
unoccupied bins, accuracy-indexed table or numerical job-unit copies.

**Proof.** Pairs above the target are forbidden. Pairs at the small threshold
are small. For each remaining big pair, `bin_index` evaluates the exact ceiling
index of Theorem PS, Equation PS10; the open-left/closed-right convention places
an internal upper endpoint in the preceding bin and the target in the final
bin. Grouping uses only indices occurring on actual input pairs.

For the next occupied bin, `profile_counts` enumerates exactly the nonnegative
counts bounded by both the unused integer count budget and the floor of the
unused lower-load budget divided by that bin's positive lower endpoint.
Consequently every partial state is valid and extends to a full profile by
zeros. Conversely every valid profile follows these choices, so none is lost
or repeated. Theorem PS's distinct-zero-completion argument charges the entire
tree by polynomial overhead per emitted profile, including unsuccessful LP
attempts. A separate explicit stack of paused machine iterators applies the
same argument globally and never materializes a family for a Cartesian-product
pool. The occupied-bin iterator itself also uses explicit DFS frames. Neither
stack consumes one Python call frame per input coordinate or physical machine,
so legal large explicit inputs do not encounter an interpreter recursion limit.

The count budget, bin indices and endpoints are exact binary values. The number
of stored counters is the number of actual occupied bins; their bit lengths
depend on the accuracy encoding, not its reciprocal in unary. The proved
composition and partition bounds on emitted profiles therefore apply to this
iterator itself. <code class="math">\square</code>

## 3. Quality, optimization and actual implementation costs

**Proposition 3.** The profile client returns the approximation and exact-budget
output of Theorem PS on every accepted complete-table input, or detects original
infeasibility. It has the reference solver costs below, independently of the
fast theorem's oracle implementation.

**Proof.** Every original full-target schedule supplies its actual big-bin
counts as a profile. Those counts meet the count budget and lower-load
inequality, and leave the schedule's small load within the corresponding
residual. The unchanged full schedule therefore witnesses one enumerated LP.
Total failure is sound. Lemma 1 returns original integer bases at no greater
cost. Theorem PS, Section 6, bounds their big load by the profile's lower load
plus one small-threshold allowance, and their rounded small load by the residual
plus that allowance. This is precisely the requested per-target factor.

Initialization, the exact zero-target gate and one-sided rational-grid search
reuse the canonical backend unchanged. That search only requires sound full
failures and saved actual weak upper outputs; its internal dispatch argument
does not set the profile approximation factor. The subclass's positive-target
contract supplies that factor. No monotonicity of successes is assumed. Thus
adjacent grid endpoints give the optimization guarantee. <code class="math">\square</code>

Let <code class="math">q</code> and <code class="math">m</code> be the physical-machine and type counts,
and <code class="math">D=m(q-1)</code> the reduced LP dimension. An LP with
<code class="math">L</code> rows inspects at most <code class="math">\binom{L}{D}</code>
active systems and does polynomial rational work and row checks for each.
An integer minimum-cost step inspects at most
<code class="math">\prod_j(n_j+1)^{q-1}</code> reduced vectors. Rank validation
uses <code class="math">O(m4^q)</code> table comparisons. These bounds are multiplied
by the actual streamed profile attempts and polynomially many target calls.
The profile-count bounds apply to the enumeration factor, but these local solver
costs are not substituted for polynomial oracle primitives. Storing all LP
vertices can use exponential space, and numeric integer enumeration is not
polynomial in binary multiplicities. The complete-table representation is also
charged explicitly. The client makes no claim to implement the slot-surplus
companion or its different common-size/no-budget model.

## 4. Independent finite evidence

[check_profiles.py](verify/check_profiles.py) compares outputs and target failures
with an independent original-count oracle that imports no backend helpers and
checks every original rank, mandatory total, assignment cost and load. Separate
rectangular enumeration checks every valid profile in small occupied-bin
families, including the pruning constraints. Boundary checks cover the exact
ceiling bin convention. Fixed-plan vertices are recovered and checked against
the original integer schedules, including fractional cost/load vertices,
zero-time assignments and more than two positive times on one machine.

An accuracy with an 81-bit denominator produces a formal bin count larger than
a 150-bit power of two. The test consumes only three profiles of a single
occupied bin with a numerically huge count budget, then checks a complete
tiny-accuracy target and optimization with one occupied bin. This exercises the
actual binary iterator, rather than allocating an accuracy-sized universe.
Four further streaming checks use 1,100 occupied coordinates with zero/one count
budgets and 1,100 physical machines, including a complete fixed-target solve.
They exercise explicit stack traversal beyond ordinary language recursion depth.
Finite evidence and complete mathematical proof have separate scopes; neither
formal verification nor external peer review is claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0.
