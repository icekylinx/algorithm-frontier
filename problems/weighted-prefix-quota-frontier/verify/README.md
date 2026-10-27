# Verification and proof scope

The main proof establishes the basic quadratic laminar catalogue. The
[recovery companion](../manuscripts/laminar-dominant-weight-recovery.md) improves
the elementary quadratic coefficient from `4` to `10/9`, or to `5/9` plus a
vanishing term with the specifically cited local universal-set theorem,
and proves a polynomial
one-positive-weight endpoint. Other companion
manuscripts establish one-order, two-order, bounded-family, sparse-row and
ground-reduction results. `B`, `B0`, `Delta` and `p` are local parameters, not aliases
for encoded input length.

Common-order and bounded-family theorems do not extend to arbitrary
row-dependent weights. The sparse theorem requires positive root charge on
every quota-active coordinate and retains its original completion oracle.
Weighted optimization is not inferred from a rank-only completion statement.

The kernels bound the retained selectable ground. They retain access to the
original oracle and weights and are not automatically parameter-only bit
kernels or construction-time bounds. Oracle-query lower bounds and
deterministic-ETH consequences keep their separate representations and
assumptions; the quadratic laminar upper bound retains an explicit lower-bound
gap. A general implementation of the numeric-target, completion, or
coloring algorithms is not supplied.

## New local executable evidence

Run the five focused deterministic checks from the repository root:

~~~sh
python3 -B problems/weighted-prefix-quota-frontier/verify/check_sharp_packing.py
python3 -B problems/weighted-prefix-quota-frontier/verify/check_laminar_reduction.py
python3 -B problems/weighted-prefix-quota-frontier/verify/check_laminar_recovery.py
python3 -B problems/weighted-prefix-quota-frontier/verify/check_two_weight_lower.py
python3 -B problems/weighted-prefix-quota-frontier/verify/check_quota_extensions.py
~~~

The packing check enumerates all 68 labeled matroids on four elements,
all two-row incidence patterns, the stated capacity choices, and three
signed profit profiles, including a profile with four distinct values.
It independently tests every original feasible
set and every protected item against literal matroid independence and
packing feasibility. Both exactly equal-profit class replacements and
arbitrary-profit ordered replacements are tested, as is the optimum at
every cardinality. It also checks higher-capacity examples, the
one-failure weighted endpoint, and the exact forcing construction through
rank four and support degree three. The reduction is tested as an oracle
procedure; no linear representation is assumed.

The [weighted-prefix checker](../../matroid-failure-summaries/verify/check_weighted_prefix.py)
additionally checks the ordered primitive over complete rank tables for
all labeled matroids on at most four elements and 26 fixed orders of the
13-item nonrepresentable obstruction. It checks original prefix ranks,
necessity witnesses, exact canonical-basis unions and the explicit
oracle-query bound.

The laminar check compares the original lower inequalities with the
aggregate-reduced inequalities on five laminar topologies, every lower
assignment through root cap three, and every nonnegative integral mass
vector under the cap. It covers 21,658 lower assignments and 696,490 mass
comparisons, and separately tests the telescoping charge identity giving
at most <code class="math">B</code> retained lower rows.

The new recovery check independently compares interval extendability,
grouped-copy greedy rank access, and the exact two-rank completion with
literal finite feasible allocations. It covers 77,438 laminar count
systems, 1,480,360 extension comparisons, 200,256 rank comparisons,
319,624 comparisons of rank bases with original count constraints, and
14,938 ordinary unit-copy basis-exchange conditions. A binary-large
fixture uses capacities up to <code class="math">2^{45}</code> and checks all 16 coordinate ranks
against a separate partition formula without expanding units.

It also checks 194,016 weight histograms and 600 seeded integer-polymatroid
recovery instances. The latter compare exact signed optima, including
nonuniform and negative zero costs, infeasibility, and root budget zero.
For this check, all original prepared positive copies replace the earlier
representative union. The test therefore isolates the new contraction,
count-rank correspondence and recovery; it does not implement the earlier
catalogue. The companion records the complete counts and exact scope.
The same checker also verifies the cardinality-sensitive exception
inequality and the exact integer exponent maximum against direct
finite enumeration: 590,480 cardinality/depth/budget cases and 6,321
actual-weight maxima. The stronger universal-set theorem is a named
mathematical dependency, not something these finite checks implement.

The two-positive-weight lower checker independently enumerates allowed
bases, all ranks, the exact numeric family, and mandatory/optional
outcomes for 20 sparse-paving matroids. It checks 20,569,302 ordinary
basis exchanges, 37,120 full rank entries, 26,240 reference/one-restored
rank comparisons, and 276 complete decoder truth tables. The [boundary
proof](../manuscripts/two-positive-weight-laminar-boundary.md) supplies the
asymptotic oracle and separately scoped ETH arguments. Its optional
instances demonstrate optimization hardness, not feasibility hardness.
The combined extension checker verifies projected coloring certificates
against every original upper row and checks that lower totals are exactly
preserved. Its 1,500 seeded instances give 25,797 certificates and 32,473
replacement comparisons; 1,368,168 weighted histogram profiles validate
the refined accounting. It separately enumerates all 2,629 compatible-cut
families on at most four elements, checks 10,441 anchor orientations, and
compares 819,576 fixed-mass numeric vectors with their rewritten laminar
constraints. This checks the new numeric correspondence, not a resource
optimization backend. The one-weight polynomial claim for compatible
cuts requires a prescribed or forced total numeric mass.
All five scripts refuse execution with assertions disabled.

These checks support the new local mechanisms. They do not verify all
asymptotic oracles, the universal-coloring family, weighted Rado induction,
the general weighted intersection implementation, or the lower-bound
literature. The recovery companion names the specific classical
polymatroid optimization and submodular minimization references it uses. The sharp packing
construction has explicit FPT preprocessing; it must not be described as
the uniform polynomial-time sunflower kernel. Its arbitrary-profit
polynomial endpoint requires saturated-row budget at most one.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
