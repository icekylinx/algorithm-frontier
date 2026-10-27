# Realization and scoped review of the width-two unit gate

The [implementation](reference/README.md) realizes the main proof's exact
local gate. Original player-matroid rank and original scenario-unit tests
are paid callbacks. It supplies the polynomial matching terminal itself,
rather than substituting exponential endpoint enumeration. This note
separates that executable scope from the high-quota allocation corollary.

## Original-ground oracle interface

The explicit player IDs are `range(q)`, the original player rank is `r`,
and the omitted dual rank is `c=q-r`. For a set `D` already omitted,
dual independence is equivalent to `rank_M(P-D)=r`. Every independence
query in the implementation uses precisely this original-ground formula.
There is no need to materialize a dual representation or contract resource
ranks. If `D` is dual independent, then a disjoint set `S` is independent
in the dual contraction exactly when `D|S` is dual independent, where `|`
is set union in the program.

A scenario callback returns `None` exactly for infeasibility and otherwise
an actual integer one-unit witness under that original scenario's budget
and resource constraints. These families must be hereditary and contain
the empty set. Nonnegative assignment costs and disposable units justify
these properties in the allocation model. The implementation never
changes a callback's costs, resource ranks, budget or required unit value.
Paid polynomial exact unit tests therefore give the intended polynomial
node cost. A potentially exponential callback does not inherit that cost
assumption merely because it implements the same Boolean predicate.

## Implemented polynomial matroid intersection

For a common independent set `S`, initialize BFS at every outside element
whose addition preserves independence in the first matroid; terminal
outside elements are those addable in the second matroid. An arc from an
inside element to an outside element is present when the corresponding
exchange preserves the first matroid. The reverse type of arc is present
when its exchange preserves the second matroid. BFS explores exactly
these arcs, with fixed integer tie orders, and returns a shortest path
from the source set to the terminal set. Flip all its vertices by symmetric
difference. If no terminal is reachable, return the current set.

This is the standard augmenting matroid intersection theorem, with exact
orientation and shortest-path rule as stated in Bárász, Bérczi, Király,
Oki, Yamaguchi and Yokoi, *Matroid Intersection under Minimum Rank Oracle*,
[arXiv:2407.03229v2, Definition 2.2 and Algorithm 1](https://arxiv.org/html/2407.03229v2#S2).
The theorem supplies both independent augmentation and maximum cardinality
at exhaustion. This named published mathematical dependency is explicit;
no independence-exchange claim is inferred solely from finite examples.
Loops cause no extension of the theorem: a first-matroid loop is neither
a source nor reachable through a first-matroid exchange, and a second-
matroid loop is neither a terminal nor has an outgoing second-matroid
exchange. Removing such elements does not change the augmenting paths or
the optimum. The paper's loopless convention can thus be enforced
conceptually without changing the implementation.

Every successful flip increases the common cardinality by one. At most
`q` augmentations occur. Each BFS inspects at most `q` vertices, at most
`q` possible outgoing exchanges at each vertex, and polynomial set work.
Consequently it makes polynomially many independence calls, stores only
polynomially many vertex and predecessor records, and has polynomial work
in the explicit ground size and paid oracle work. BFS shortest paths,
rather than arbitrary exchange paths, are essential to this contract.

## Complete dual-cover search and reconstruction

Enumerate every original singleton and pair in each explicit scenario.
A rejected singleton forces that vertex into the dual basis; a rejected
pair creates an edge. Union these forced vertices with the caller's
forced omissions. A dependent forced union proves failure. Otherwise
start with that union as the current dual-independent omitted set.

At each processed state rebuild the uncovered graph by dropping edges
incident to omitted vertices. For a vertex of degree at least two,
attempt to append its singleton and its entire neighbor set, respectively.
Only dual-independent unions are pushed. Every covering dual basis either
contains the vertex or contains all its neighbors. Therefore at least one
child preserves any protected covering basis. The neighbor branch may
later also include the vertex, which only duplicates possible solutions.

If the remaining graph is a matching, restrict the current dual
contraction to its endpoints and intersect it with the partition matroid
of capacity one on each edge. A common independent set as large as the
matching picks one representative from every edge. Its existence is
necessary: choose one endpoint per edge from any independent cover, then
use heredity. It is sufficient: extend the representatives to a full dual
basis by greedily adding any remaining dual-independent elements. Basis
extension preserves coverage. The final basis may contain both endpoints
of an edge, which is permitted. The code never constrains its completed
basis to be independent in the representative partition matroid.

When a covering dual basis is found, its original-ground complement is
an original player basis avoiding the seed. Recheck that same basis in
every original scenario and return all actual unit witnesses if they
succeed. If a scenario rejects it, greedily remove players while rejection
persists. Heredity proves that the remaining set is inclusion-minimal
for the original family. No rejected singleton or pair can be contained
in this graph-independent selected basis, so the resulting set has size
at least three. Return the separate width-violation outcome immediately.

If every dual-cover state fails, no graph-compatible original basis
exists. Since every actual robust unit basis is graph-compatible, that
failure remains sound even outside the width promise. A width violation
might coexist with another feasible basis and is never treated as a
failed seed. On the promised class, every independent minimal failure
has size at most two, so the violation outcome is impossible.

## Runtime, forced seeds and workspace

Singleton/pair preprocessing, node reconstruction, rejected contraction
tests, matching intersection, basis extension and final certificate
shrinking all have polynomial cost under the stated paid oracles. A
successful branch reduces remaining dual rank by one or by the vertex's
degree, which is at least two. The main proof's Fibonacci weighted-leaf
argument therefore applies to every processed state, including terminal
failures; failed contraction attempts are charged at their parent.

The initial forced union contains the seed. Hence its residual dual rank
is at most `c-|forced|`, giving exactly the main proof's uniform extension
bound. A stack implements depth-first traversal and avoids a language
recursion-depth restriction. Each stack state is an explicit omitted
set, branching depth is at most the residual rank, and at most one
pending sibling per depth is stored. Thus workspace is polynomial.
Neither numerical capacities nor oracle rank values are expanded into
unit records.

The generic streamed block wrapper's local containment-cover inequality
applies at the fixed quadratic Fibonacci base. Exact comparisons reduce
to integer pairs representing powers in `Q(sqrt(5))`; the bit lengths are
polynomial in the block size and exponent. All forced-seed completeness,
all-input cost and width-violation propagation conditions have been checked
against the wrapper. This proves the displayed whole-ground unit bound
mathematically; that wrapper is not implemented in this reference.

## Review boundary

Internal review covers the complete exact unit gate, its original-rank
semantics, matching intersection and completion, Fibonacci accounting,
forced omissions, guarded outcomes and whole-ground conversion. On the
stated Boolean resource instances, every integer count is at most one,
so the exact unit gate also completely solves optimization.

The main proof's Section 8 high-quota factor tradeoffs have also been
checked against the complete bounded-certificate theorem. The original
player basis/rank and the same explicit scenario resources, costs and
budgets match exactly. Width two is used only by the exact one-time unit
gate; targets up to the fixed tradeoff use its saved witness, and larger
targets retain the original weighted quota gap and scenario-wise integral
recovery. The local costs add, so the combined base is their maximum.
Applying the global wrapper separately to the unit and positive-quota
interfaces gives the same maximum through monotonicity of its base map.
For fixed tradeoff, the quota constant has a fixed rational power and the
unit constant lies in the fixed quadratic field; each wrapper's comparisons
are exact with polynomial bit length. Comparing the constants, if needed,
reduces to raising positive values to the fixed power and using the
Fibonacci representation of quadratic powers. No arbitrary real oracle is
needed. The factor-two and factor-three quota constants both exceed the
unit constant, leaving their existing whole-ground bases unchanged.

General polymatroid/budget unit tests have the [certified weighted realization](../robust-bounded-certificates/reference-realization.md).
That native adapter can feed this local width-two gate directly, as checked
by its integration tests. Higher-quota LPs/recovery and the streamed wrapper
remain outside this executable backend, although their full mathematical
composition is now within review. No external peer review or proof-assistant
verification is claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
