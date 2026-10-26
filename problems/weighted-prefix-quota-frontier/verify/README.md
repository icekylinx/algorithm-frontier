# Verification and proof scope

The main proof establishes the quadratic laminar bound; companion
manuscripts establish one-order, two-order, bounded-family, sparse-row and
ground-reduction results. B, B0, Delta and p are local parameters, not aliases
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

Run the two focused deterministic checks from the repository root:

~~~sh
python3 -B problems/weighted-prefix-quota-frontier/verify/check_sharp_packing.py
python3 -B problems/weighted-prefix-quota-frontier/verify/check_laminar_reduction.py
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
at most $B$ retained lower rows.

These checks support the new local mechanisms. They do not verify all
asymptotic oracles, the universal-coloring family, the weighted Rado
completion theorem, or the lower-bound literature. The sharp packing
construction has explicit FPT preprocessing; it must not be described as
the uniform polynomial-time sunflower kernel. Its arbitrary-profit
polynomial endpoint requires saturated-row budget at most one.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
