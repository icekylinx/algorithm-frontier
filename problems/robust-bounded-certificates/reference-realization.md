# Certified weighted unit intersection and the guarded robust basis gate

The [reference implementation](reference/README.md) completes the exact
one-unit testing and bounded-certificate extension interfaces used by the
main theorem and the width-two client. Its weighted primitive is polynomial
in paid independence-oracle work. The native complete-table adapter charges
the tables explicitly and never expands binary resource multiplicities.

## 1. Boolean caps are matroids on original owners

**Lemma 1.** For a normalized monotone integral submodular rank `f`, the
sets whose incidence vectors belong to `P(f)` form a matroid. A complete
rank table supplies exact independence tests in polynomial time in that
table's encoding.

**Proof.** The empty set is feasible and heredity follows from nonnegative
coordinate disposal. Let feasible owner sets `A,B` satisfy `|A|<|B|`.
Suppose no element of `B-A` can be added to `A`. For each such element
`e`, a violated rank row on `A+e`, monotonicity and integrality provide
a subset `S_e` of `A` with `f(S_e)=|S_e|` and
`f(S_e+e)=f(S_e)`. To obtain it, intersect the violated row with `A+e`;
monotonicity preserves violation. The row must contain `e`, because
`A` was feasible. Removing `e` gives a feasible lower bound one less
than its cardinality, forcing both equalities.

Tight subsets of the feasible set `A` are closed under union, by
submodularity and feasibility of their union and intersection. Hence
`S=union_e S_e` is tight. Diminishing returns implies that every element
of `B-A` has zero marginal rank after `S`, and therefore adding all of
them leaves rank `|S|`. Feasibility of `B` bounds the number of its
elements in `S union (B-A)` by `|S|`. Its other elements lie in `A-S`,
so `|B|<=|S|+|A-S|=|A|`, a contradiction. This proves augmentation.
The eligibility mask is simply a matroid restriction.

For the complete-table adapter, inspect every original subset row on the
incidence vector of the queried owner set. These are precisely all defining
inequalities, including rows extending outside that set. The work is
polynomial in the explicitly supplied table. No resource unit appears as
a new ground element. The validator checks every original rank pair for
monotonicity/submodularity and requires normalized nonnegative integer
values, so the lemma applies to every accepted table. A rank-oracle client
instead uses the main proof's paid submodular minimization construction.

## 2. Exact weighted augmentation and its certificate

**Proposition 2.** `minimum_cost` returns a minimum-cost common independent
set at the requested cardinality, or a certified maximum-cardinality smaller
set. Its rational arithmetic, oracle work and workspace are polynomial in
the explicit ground and encoded costs. The verifier checks this contract
without running an optimizer.

**Proof.** For current common independent set `I`, sources are outside
elements addable in the first matroid, and terminals are those addable in
the second. An inside-to-outside arc exchanges in the first matroid;
an outside-to-inside arc exchanges in the second. The vertex cost is the
original cost outside `I` and its negative inside. A path's sum is exactly
the cost change from flipping its vertices.

The exact external theorem is the standard weighted augmentation rule in
Bárász, Bérczi, Király, Oki, Yamaguchi and Yokoi,
[*Matroid Intersection under Minimum Rank Oracle*, arXiv:2407.03229v2,
Definition 2.2, Algorithm 2 and Lemma 2.5](https://arxiv.org/html/2407.03229v2#S2).
Apply its maximizing-weight convention to the negative of the input cost.
A minimum-cost cardinality-`k` common set has no negative-cost exchange
cycle. Flipping a minimum-cost source-to-terminal path, with shortest
length among cost ties, gives a minimum-cost cardinality-`k+1` common set.
Exhaustion gives maximum cardinality. These named mathematical dependencies
are not replaced by a finite-test assertion. Loops can be deleted: a
first-matroid loop has no incoming exchange or source status, and a second-
matroid loop has no outgoing exchange or terminal status. They occur in
neither relevant paths nor directed cycles, matching the source's loopless
convention without changing the code's outputs.

Start at the empty minimum-cost cardinality-zero set. Synchronous exact
Bellman--Ford relaxations compare total vertex cost, then length, then
integer path IDs for deterministic ties. With no negative cycles, a shortest
cheapest walk is simple; deleting any cycle either lowers its cost or
shortens it. At most the ground size minus one arc relaxations therefore
suffice. The implementation stores complete finite paths, avoiding reliance
on stale predecessor pointers. Induction by the augmentation theorem proves
the minimum-cost invariant and termination after at most the ground size
many augmentations, regardless of the numerical target or cost magnitude.

At return, compute all-source shortest exchange distances as potentials.
The machine-readable certificate contract is

```text
potential[v] <= potential[u] + signed_cost[v]  for every exchange arc u -> v.
signed_cost[i] = -cost[i] when i is chosen, and cost[i] otherwise.
```

Summing these inequalities around any directed cycle proves nonnegative
cycle cost. Lemma 2.5 then proves minimum cost at the returned cardinality.
The verifier reconstructs every original exchange through its paid oracles,
checks exact common independence and these inequalities, and performs no
shortest-path or negative-cycle search.

If a target is not reached, let `R` be the vertices reachable from the
source set and supply its complement as the cut. There is no reachable
terminal and no exchange leaves `R`. The no-augmentation theorem gives
that the first-matroid rank of the cut plus the second-matroid rank of `R`
equals the current cardinality. The verifier computes those two ranks by
ordinary independent-set greedy extension and checks the equality. Every
common independent set splits across the cut and its complement, so that
rank sum is an upper bound on its cardinality. Thus the checked cut proves
maximum cardinality without trusting the search history. An underfull
record with no cut is rejected.

A graph build makes at most quadratically many independence calls. There
are at most linearly many augmentation stages, and each shortest-path
computation uses linearly many relaxation rounds over that explicit graph.
Stored paths, potentials, sets and graph records occupy polynomial space.
Every distance is a sum of polynomially many original rational costs, so
its exact bit length is polynomial. The same holds for all comparisons and
certificate fields. No operation loops over a numerical cost or target.

## 3. Exact scenario budgets and original allocation witnesses

**Proposition 3.** Each `UnitScenario` callback realizes the main proof's
exact scenario-unit test. It supplies an actual allocation on success,
and its `optimize` record certifies the minimum-cost or resource-infeasible
outcome even when the budget test fails.

**Proof.** Form one explicit element for every eligible original owner/type
pair on the queried owner set. On this pair ground the first matroid is
the direct sum of Lemma 1's resource Boolean caps; the second is the owner
partition matroid with capacity one. A common set as large as the owner
set covers every owner exactly once and is exactly a legal one-unit
integer allocation. Every legal unit allocation conversely gives such
a common set. Original assignment costs are the pair weights.

Proposition 2 supplies the minimum cost at full coverage, or a cut proving
that full coverage is impossible. Comparing the true minimum cost to the
original nonnegative budget is therefore an exact feasibility test.
The original polymatroid inequalities remain unchanged; there is no cost
inequality inserted into an allegedly integral polytope. Empty coverage
has its zero-cost empty witness. Unused resource units and all counts at
outside owners are discarded, as permitted by the original model.

The native certificate records the queried original owners, the chosen
original pairs and Proposition 2's certificate. The verifier rebuilds the
pair correspondence, checks canonical record types and the intersection
certificate, and requires the assignment to equal exactly its selected
pairs. Thus neither a cheaper claimed cost nor a changed assignment can
replace the true certified optimum. The separate affordability predicate
assumes a produced or verified record, as its API states.

Nonnegative costs give heredity: deleting owners discards their units and
cannot raise cost. All callbacks retain the same original ranks, masks,
costs and budget, even during certificate shrinking or forced omissions.
The explicit pair ground is bounded by owners times types, independent of
binary capacities. The complete-table adapter is polynomial in its charged
tables; it does not claim polynomial rank-only input time by silently
materializing exponentially many subsets.

## 4. Guarded common-basis extension

**Proposition 4.** `gate` realizes the local exact extension algorithm of
the main proof's Sections 3–5, including sound three-outcome semantics,
forced omissions, its complete corank time bound and polynomial workspace.

**Proof.** Each stack state is an allowed original ground. Test its rank
against the original required rank, then greedily extend an independent
set to an actual original basis inside it. This is equivalent to requiring
the accumulated omissions to be independent in the original dual matroid;
the original rank and all scenario data stay fixed.

Test that same basis in every original scenario. If they all succeed,
return all actual witnesses. On the first failure greedily delete owners
while failure persists. Heredity proves that every single deletion from
the resulting set is feasible, and hence that it is inclusion-minimal in
the original scenario. It lies inside an original basis and is therefore
independent in the player matroid. A larger-than-supplied-width failure is
returned as a separate structural violation.

Otherwise branch on deleting each member of this minimal failed set.
Every protected robust basis omits at least one member, since it cannot
contain an infeasible hereditary subset. That child preserves the same
original robust basis and all its scenario allocations. At residual
corank zero the current basis is the entire allowed ground, so failure
there soundly exhausts the possibility. This proves completeness on the
width class and soundness of fully exhausted failure on arbitrary inputs.
A width violation can coexist with another feasible basis and is never
counted as a failed seed.

Every child decreases the allowed size by one while the required rank
remains fixed. A nonterminal node creates at most the supplied width many
children. The main proof's node recurrence therefore pays for every
processed state, including rank-rejected children. Shrinking and the
initial/final scenario tests are polynomial per node. Forced omissions
reduce the initial residual corank by their actual cardinality. The
iterative depth-first stack keeps only polynomially many pending sibling
sets; it does not store the search tree or an exponential cache. Rank
zero returns the empty basis under the stated convention.

The native budget tests from Proposition 3 also instantiate the callbacks
of the existing width-two Fibonacci gate. This discharges that software
interface with polynomial explicit-input work rather than merely adding
another test of abstract conflict graphs. Both gates retain the exact
same original unit scenarios.

## 5. Complete theorem audit and implementation boundary

The complete main theorem has been checked with its dependencies:

- The exact unit construction, original minimal failures and guarded
  extension satisfy the original-basis, forced-seed and all-input contracts.
- The scenario fractional regions use the nonnegative support separator
  in [one-value allocation, Section 3](../one-value-exact-two/proof.md#3-the-fixed-budgeted-count-service-region).
  Their intersection preserves one original common selected basis and
  separate adaptive witnesses.
- For larger integer quotas, the [integer quota ratio](../whole-ground-allocation/integer-quotas.md#2-the-integer-quota-ratio)
  gives the stated fixed-parameter omission bound. The complete
  [weighted first-crossing proof](../whole-ground-allocation/selection.md)
  pays for unpromised branches and its enumerator.
- Each successful scenario uses the [integral maximum-total resource/owner
  intersection](../one-value-exact-two/proof.md#5-no-loss-quota-recovery-with-the-exact-cost-budget).
  It attains its original integer owner quota with cost at most that
  scenario's fractional witness, without a cost-row integrality claim or
  numerical resource expansion.
- The small-target saved unit witness and all larger weak successes obey
  the one-sided integer-search invariant; every failed upper endpoint is
  strictly above the robust integer optimum. The total-count upper bound
  has polynomial binary encoding. The combined base is the maximum of
  the separately paid unit and positive-quota costs, rather than their
  product.
- The [streamed global wrapper](../whole-ground-allocation/global-conversion.md)
  applies to each forced-seed interface. Width one is already polynomial;
  the positive-quota base remains greater than one. Fixed tradeoff
  parameters allow exact constant-degree algebraic comparisons. Variable
  widths are clipped by the original basis rank, and binary-variable
  tradeoffs retain the separately stated rational upper-envelope option.

These arguments establish the full mathematical approximation theorem,
including exact scenario budgets and optimum one. Exact rational LP,
submodular minimization, integral polymatroid intersection and the named
weighted matroid theorem remain paid mathematical dependencies. None is
an unresolved interface solely because a particular software backend is
absent. The implementation supplied here realizes weighted intersection,
exact unit scenarios and the bounded local gate. It does not implement
higher-quota LP service, integral polymatroid recovery, integer target
search or the streamed global cover. Internal mathematical review and
finite executable checks are not external peer review or proof-assistant
verification.

**Attribution:** icekylinx and GPT-6 Astra Pro.
