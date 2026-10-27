# Exact original-input realization of shared resource roles

The [native backend](reference/joint.py) executes the changing joint-role LP,
the actual weighted first-crossing recursion and streamed covers, signed-cost
integer recovery, the arbitrary-value exact-two endpoint, and the compulsory
two-value target gaps. This note proves those operations on original rank
tables. Its finite LP implementation has a separate cost from the polynomial
LP and intersection primitives in the [main theorem](proof.md).

## 1. Original data and output

`Joint(player_rank, resource_ranks, values, costs, budget, setup=None)` accepts
complete original rank tables on binary subset masks. Values and costs are
type-major, so `values[j][p]` is player-specific. All numeric input is an exact
integer or `Fraction`; rank entries are nonnegative integers. The constructor
checks normalization, monotonicity and submodularity of every original table,
and the cardinality bound for the player matroid. Original values, costs,
setup fees and the budget are nonnegative. A resource may be unused.

`Allocation(basis, counts)` contains original owner IDs and original
type-major integer count vectors. The verifier checks an actual full-rank
player basis, every original resource inequality, zero assignments outside
that basis, and its actual setup plus assignment budget. It does not call a
role, LP, omission or rounding producer. Canonical record and integer types
are required. `zero()` returns a minimum-setup basis with zero counts, or
`None` when even that basis exceeds the budget. Rank zero has an empty basis
and minimum utility `None`.

The reference keeps original owner labels, including loops, rather than
renumbering them. The theorem may delete original loops before counting its
nonloop parameter. The software's finite bounds count all supplied labels.

## 2. Exact finite LP primitive and separators

**Lemma 1.** Every `Region` method computes its declared bounded original
resource LP exactly.

**Proof.** An active coordinate is one allowed original type-owner pair with
positive singleton rank. All other coordinates are identically zero. The
remaining inequalities are nonnegativity, every original rank row, one
possibly signed affine cost row, and any forced count-one equalities as two
inequalities. Original rank rows bound every coordinate. Because all subset
rows are present, zeroing forbidden coordinates is exactly the masked rank
polytope, even though the code retains original table entries.

`vertices` tries every set of as many rows as active variables and solves its
rational square system. A feasible vertex has an independent active basis,
including on lower-dimensional faces; every yielded point satisfies every
row. The zero-dimensional case explicitly tests all scalar inequalities.
Every nonempty bounded polytope has a vertex, and a bounded linear objective
attains an optimum there. Thus feasibility and optimization are exact.
Repeated active bases may yield the same vertex; this does not alter extrema.

`optimum(players)` adds one nonnegative target coordinate and service rows
for a nonempty owner set. Resource bounds also bound this target, so the same
argument applies. `feasible(service)` adds the requested lower service rows.
Positive pairs whose full-unit cost exceeds the budget remain available.

For separation, first reconstruct service membership directly. If it fails,
enumerate the distinct projected utility vectors of the underlying region's
vertices. The outer LP uses a nonnegative normal summing to one, and a support
height at least its scalar product with every such vector. The last normal
coordinate is eliminated exactly. Maximizing query minus height gives the
normalized support-gap LP from Section 4 of the main proof. The height need
not have an explicit upper cap: its objective coefficient is negative,
and an optimum uses the finite support height. The normal simplex is compact
and the resulting pointed epigraph has an optimizing vertex. A nonempty
downward utility region has zero service, so its support height is
nonnegative. The main proof's positive-part separation argument guarantees a
strictly positive gap for an external nonnegative query. The returned
`Row` is therefore nonnegative, valid for the whole region, and strictly
violated. An empty underlying region is rejected before this outer LP.
The zero-query-interior case is handled by membership, not by assuming that
the optimized gap must be exactly zero. This proves the lemma.

## 3. Integer lower-prefix recovery and signed objectives

**Lemma 2.** `round_counts` preserves each original resource and every
owner's cumulative count floor in its nonincreasing value order, without
increasing the supplied signed linear cost.

**Proof.** Start from its feasible fractional independent vectors. Add one
zero-cost disposal coordinate to each masked resource, completing it to a
base as in the [unrelated additive rounding proof](../unrelated-values-additive/proof.md#5-one-integral-rounding-preserves-every-prefix-and-the-cost).
Complement the base using integral singleton caps. At each real owner, put an
upper ceiling on every prefix of this complement vector; disposal coordinates
receive their caps. These are the chain-polymatroid and disposal constraints
from that proof. Their intersection with the direct sum of complement
resources is integral, and its maximum-total face contains the fractional
complement. Full total fixes every resource to its own base.

Each disposal variable is uniquely determined by its real independent vector.
After eliminating it and complementing back, this face is exactly the
original masked resource product with a lower floor on every real-owner
prefix. Conversely any real vector satisfying those original rank and prefix
rows has the required unique disposal extension and complement. This is an
affine bijection preserving integer points, not a relaxation. Consequently
every vertex of the reduced polytope enumerated by `round_counts` is integral.

The fractional input satisfies all its floor rows. Minimizing the supplied
linear cost therefore gives an integer point of no larger cost. Signed
coefficients do not affect boundedness or this comparison. The budget row is
removed before this optimization: intersecting an integral face with an
arbitrary rational budget halfspace would not justify integrality.

The full prefix preserves at least the floor of the total count. Telescoping
the other prefix floors gives each owner's original fractional utility less
at most its largest allowed unit value. Orders can differ at different
owners. No resource copy, conceptual unit expansion or numeric count loop is
used. This proves the lemma.

## 4. Persistent setup credit and actual basis extraction

For original player matroid `M`, the extra resource has rank `M*`, value zero
and cost `-setup[p]`. Its capacity remains available at every owner, including
inside the current light ground. The affine budget is the original budget
less the sum of all setup fees. The dummy is a device for signed accounting;
the original model still has nonnegative costs.

`role_region(theta,Q)` retains positive real pairs below `theta` inside `Q`
and positive real pairs at least `theta` outside `Q`. Every outside owner
has total real-plus-dummy count exactly one. All those coordinates use one
rank table for each original resource, across both roles.

**Lemma 3.** `recover` produces an original feasible allocation from any
feasible role witness. Inside the light ground it loses at most the largest
light unit; every selected owner outside receives a real heavy unit.

**Proof.** Apply Lemma 2 to the joint real-plus-dummy product with its signed
objective. Its full-prefix floor preserves at least one total unit outside
`Q`. The integer dummy support is independent in `M*`; its complement spans
`M`. Greedy basis extraction inside that dummy-free complement therefore
returns an actual original basis. Such an outside selected owner has dummy
count zero, so its preserved full-prefix count includes a real heavy unit.
Inside `Q`, the zero-valued dummy does not affect the light utility bound.

The signed affine budget holds before extraction. Setup on the extracted
basis is at most total setup on dummy-free owners. Restricting real counts to
that basis can only reduce nonnegative original assignment costs. Hence the
original combined budget holds exactly. No dummy is removed before its credit
has been converted in this way. This proves the lemma.

The pure gate imposes one total unit at every owner and minimizes the signed
objective on the full-total resource/partition intersection. It removes the
budget row before optimization, tests the optimum against that budget, and
then applies Lemma 3. This integral all-heavy/dummy gate handles an empty
light ground without introducing an unbounded service target.

## 5. Actual omission, target search and exact-half endpoint

`gap(theta,k,full,weak)` calls the canonical weighted prefix DFS with promised
light cardinality `q-k`. Its metadata selector names that many members of the
current ground, while its context retains the entire ground and joint
witness. A success keeps light service for every member of that ground;
recovery never discards the additional light counts merely because they were
absent from metadata.

A protected original role witness survives at every containing ground by
keeping all its dummy counts, real light counts on the protected set, and
forced heavy counts outside the current ground. Only nonnegative real costs
are discarded. Thus every returned support row protects the same full
witness even as masks and equalities change. Empty LP gates cannot reject a
protected node. The omitted-mass inequality, first-crossing completeness and
Kraft bound are exactly those proved in Sections 4–5 of
[the setup companion](setup-budget.md). The code calls that actual canonical
enumerator; it does not replace its children by all subsets. A supplied
`global_base` is checked by the exact rational power identity for `Gamma` and
uses the canonical streamed block covers. Supplying accuracy with enormous
binary numerator may make this direct power comparison expensive; those
integer-power operations are part of the reference cost. The safe rational
envelope `global_base>=3*full/(full-weak)` is checked first and performs no
such powers, so binary-accuracy callers can use the uniform bound. Fixed rational
accuracy has the sharp analytical comparison stated in the main theorem.

`near` searches a common original value grid separately for every finite
mask/cardinality benchmark. Its legal nominal-zero initializer need not be a
role witness. Failure alone excludes a full grid target; weak successes may
be nonmonotone. The upper endpoint remains above that benchmark, so adjacent
endpoints save a nominal target at least its value. Section 7 of the setup
companion then proves the near-two guarantee. `heavy_budget` is a cap on
total omitted light roles, including original corank; for the support promise
it must cover original corank plus the optimum's selected heavy recipients.
The unconditional default processes every cardinality.

`exact_two` streams every nonempty light set for every mask, optimizes its
original role target, and recovers it, alongside the pure gate. An optimum's
mask at half its value and its actual light-only selected owners are among
these cases. The persistent canonical dummy on its original unselected
owners supplies the protected witness. Hence [the exact-two proof](exact-two.md)
applies without substituting zero into a positive-gap parameter.

## 6. Compulsory quota gaps

`quota_target(T,d)` accepts compulsory players, no setup, at most two positive
pair values, a positive target and integer factor at least two. In the high
branch it solves the original fractional target and uses Lemma 2. In the
one-unit branch it minimizes actual cost on the integral positive-unit
coverage face. In the middle branch it uses the actual joint count gap with
full quota `ceil(T/u)` and weak quota `ceil(ceil(T/u)/d)`, including the pure
all-heavy gate. Its recovery imposes the integral heterogeneous owner quotas
exactly and minimizes cost on that resource/partition full-total face. The
budget is checked after optimizing this integral face. These are the three
branches of [the integer-quota proof](two-value-tradeoffs.md), so a success is
an original allocation of value at least `T/d` and a failure excludes every
integer full-`T` allocation.

The software loops over all heavy cardinalities. It does not compute the
minimum-cost affordable heavy-support cap `nu_C`, although the mathematical
proof supplies that polynomial weighted-intersection gate. Nor does it add
the two-value premise to optional selection by a value-changing dummy.

## 7. Exact finite reference cost

For an LP with `d` active variables and `N` distinct rows, the vertex stream
tries at most `binom(N,d)` square systems. Utility maximization adds one
variable. Separator construction temporarily stores all distinct projected
service vertices; their number can be exponential. It then enumerates the
outer support LP's active bases. Integral recovery has the same finite
active-basis bound after adding prefix or quota rows. Rational Gaussian work,
row storage, duplicate projected vectors, exact power comparisons and output
bits are all charged. Counts remain binary even for very large supplies.

Thus this reference realizes the original LP, oracle and recovery interfaces,
while its local enumeration cost is separate from the proved paid-polynomial
LP/SFM/intersection implementation. In particular the reference does not
claim the theorem's polynomial workspace: its temporary support list may be
exponential. The outer weighted DFS and block-cover mechanisms retain their
proved bounds with this separately charged local cost.

**Attribution:** Yilin Liu and GPT-6 Astra Pro. **License:** Apache-2.0.
