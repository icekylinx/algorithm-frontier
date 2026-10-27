# Complete-table realization of the two-size corank construction

The [reference client](reference/corank.py) executes the hard-target corank
construction of [Theorem D](proof.md), rather than selecting a schedule by
enumerating all original assignments. It shares the existing
[two-time high-target solver](../two-time-scheduling/reference/scheduling.py).
The two original recipient-rank tables use the same physical-machine subset
indices. Common sizes are positive exact rationals with the small size strictly
less than the large size. Original large and small mandatory totals are the
full ranks of those tables. The input validator reuses the canonical two-time
rank/data validator; the empty physical ground is handled directly.

## 1. Box restriction and full-ground duality

**Lemma 1.** The client's box tables, Boolean player matroid and hard-target
dual represent exactly the objects in Theorem D, including original totals and
machines that cannot receive any large unit.

**Proof.** `box_rank` evaluates the integral box formula by enumerating every
subset of its queried set. Thus it computes exactly the capped polymatroid
rank. The unit-cap table of the original large rank is the Boolean player
matroid. Its full rank is compared with the original mandatory large total;
its nonloops, determined from singleton ranks, define only the candidate
large-recipient ground. A loss of Boolean rank rules out every hard target
because such a target permits at most one large unit per machine.

For the original small rank, retain its original full total after imposing
the uniform target count cap. A rank loss rejects the target. Otherwise form
the dual with respect to that cap on the entire original physical ground,
before restricting any candidate large-recipient set. The fixed dual table
is then reused unchanged throughout recursion. Complementing an integer dual
base in the uniform cap gives exactly an original small base inside that box.
No target or recursive mask changes a mandatory full total. The main proof's
feasible-target argument supplies its full integer quota on the large-recipient
basis. <code class="math">\square</code>

## 2. The exact gate, actual batch recursion and binary completion

**Lemma 2.** At a hard target, the client either returns original bases
satisfying the integer-quota approximation or soundly rejects the original
full target. Its reached batch nodes include failed candidate rank tests.

**Proof.** For a full quota at most the fixed divisor, the weak quota is one.
Enumerate the subsets of eligible large positions of the original required
cardinality, testing independence in both the Boolean player matroid and the
dual unit box. This is an exact common-basis gate. A full-quota basis supplies
a one-unit basis, so failure is sound.

For larger quotas, `batch_gap` minimizes the weak-quota deficiency over all
subsets of the current candidate ground. If none is deficient, it returns
a player basis by matroid greedy; downward closure proves that the weak quota
on this basis is dual independent. Otherwise it computes the required omission
batch from the deficient-set cardinality and its full-quota capacity. If that
batch exceeds the current omission deficit, it rejects before enumerating
deletions. Every full-quota basis omits at least that many elements of the
deficient set, so the guard is sound and some enumerated batch preserves the
same original witness. Recurse on all candidate batches until one succeeds.
The first operation in every child is its original player-rank test, and the
child is counted even if that test rejects it. This is precisely the algorithm
and augmented node accounting in the
[batch theorem](../../manuscripts/allocation-and-scheduling/unit-quota-corank-batch-branching-improvement.md),
Sections 1–3. It does not contract or recompute the recipient dual.

The returned weak count vector is extended by zero to all physical machines.
`complete_base` first tests every original rank inequality. At each coordinate,
it adds the smallest slack among all sets containing that coordinate, as one
binary integer increment. All rank inequalities remain valid. That coordinate
is now saturated by a tight set and remains saturated when other counts grow.
After every coordinate has been processed, a nonbase independent vector would
have an augmentable coordinate by integral polymatroid augmentation, a
contradiction. Thus this procedure completes to an integer dual base and never
decreases a promised count. Complementing the base gives the mandatory original
small base. The large indicator is a Boolean independent vector of the original
required total, hence an original large base. Theorem D's load calculation and
the integer-quota extension give the asserted per-target factor without an
extra small-job unit. <code class="math">\square</code>

## 3. Other targets, shared high-target recovery and optimization

**Proposition 3.** For every validated complete-table instance and fixed
integer divisor at least two, `optimize` returns the corresponding integer-quota
makespan approximation with the original small and large bases exact.

**Proof.** When the large total is zero, uniform box restriction and binary
base completion decide the remaining one-size target exactly. With a positive
large total, a target below the large size is infeasible. Above the integer-quota
high-target cutoff, every machine is easy in the two-time theorem. The canonical
shared backend therefore executes only its joint load LP and upper-prefix
recovery, preserving the two original zero-cost resource bases. Its additive
largest-job bound is within the requested factor. In particular Boolean rank
loss is handled by this branch whenever an originally feasible target exists;
it is not excluded as an input promise. All other targets lie in the valid
one-large-unit regime and are covered by Lemmas 1–2.

Greedy binary augmentation supplies arbitrary original bases and a finite
initial schedule. Empty totals give the empty optimum. Otherwise zero is a
certified failed target because both sizes are positive. A common denominator
and integer gcd give an exact rational load grid. Binary search raises its
lower endpoint only on a sound full-target rejection and saves the actual
schedule at every weak upper success. Adjacent endpoints put the final upper
nominal target at most the optimum, so its saved output has the required factor.
Successful weak answers need not be monotone. This is the main proof's target
search, with polynomially many calls in the binary upper-grid index length.
<code class="math">\square</code>

## 4. Explicit implementation costs and verification boundaries

Let <code class="math">q_0</code> be the physical-machine count and
<code class="math">c</code> the eligible-position corank in the retained-rank
branch. Complete-table input validation checks all table pairs and takes
<code class="math">O(4^{q_0})</code> comparisons. Computing an entire box table
takes <code class="math">O(3^{q_0})</code> rank/bit operations. A deficient-set
scan visits at most <code class="math">2^{q_0}</code> table entries per batch
node, the exact gate visits at most that many subsets, and binary base completion
uses <code class="math">O(q_0^2 2^{q_0})</code> additions/comparisons. These are
polynomial costs in the complete-table representation, with polynomial-bit
arithmetic. The batch theorem's augmented node bound applies unchanged.
Table storage is exponential in the physical-machine count and is charged
as explicit input, not described as a compressed value-oracle implementation.

The shared high-target backend has its own explicitly charged LP-vertex and
numeric integer-count enumeration costs, and may store exponentially many
vertices. Those costs remain part of this executable client's bound. The hard
path and one-size path store binary counts and never iterate up to a count's
numeric magnitude. A forced-count test with an 81-bit count replaces the shared
high-target routine by an exception and checks hard-target output and grid
optimization, so this binary-hard-path claim is exercised independently of
the shared enumerator.

[check_corank.py](verify/check_corank.py) independently enumerates original
small and large bases and evaluates actual loads. Its oracle does not use
box ranks, duality or the batch recursion. Separate tests compare every tiny
box rank with a direct independent-vector maximum, check both directions of
the full-ground base complement, validate binary base completions and compare
the augmented node count with the exact algebraic batch bound. Nonloop
restrictions, rank-rejected candidate children, unpromised guards and the
one-unit exception are exercised explicitly.

This backend does not implement the distinct large-unit-rank local search,
private-slack contracted core or streamed whole-ground conversion. Their
mathematical proofs and running-time guarantees retain their own dependency
chains. Finite reference checks are not proof-assistant verification, external
peer review or a numerical proof of the general oracle theorem.

**Attribution:** Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
