# Native shared-budget count allocation and exact quota recovery

The [reference client](reference/README.md) realizes the one-value
[main theorem](proof.md) and the shared-setup and integer-quota contracts of
the [setup companion](setup-tradeoffs.md) on complete original rank tables.
This note proves the local LP interfaces rather than replacing the omission
or inclusion-cover proofs with finite enumeration. The original
[one-unit gate note](one-unit-gate.md) supplies its pair-matroid proof.

## 1. Original finite input and output

The original player rank is an ordinary matroid rank. Resource ranks are
normalized, monotone, integral and submodular, with one complete table on the
same original ground for each type. Assignment costs and setup fees are
nonnegative rational numbers. There is one exact combined budget and one
positive common resource value. Recipient vectors are independent vectors;
unused resources are permitted. No mandatory resource-base equality is added.

The native output consists of an actual original player basis and integer
original type-major counts, zero outside that basis. Its verifier checks all
original subset inequalities, nonnegativity, support and actual combined cost.
Player loops are removed only from the omission ground, using an explicit map
back to original IDs. All resource LPs retain the original physical ground.
The empty-rank output has an empty basis and zero counts; no finite minimum
utility is assigned to the empty selection. An unaffordable minimum-setup
basis is reported as zero-service infeasibility, distinct from zero optimum.

## 2. A capped-service primal/dual certificate

Fix a nonnegative original service vector `z` and a nonnegative remaining
assignment budget `D`. Create one nonnegative variable for each original
type-player coordinate with positive singleton resource capacity. Every other
coordinate is forced to zero by its original rank. Use all original resource
subset rows, the one actual assignment-cost row and one service cap per player.
The exact native LP has the following machine contract:

```text
maximize    sum_(j,p) x[j,p]
subject to  sum_(p in S) x[j,p] <= f[j,S]       for every original j,S
            sum_(j,p) cost[j,p]*x[j,p] <= D
            sum_j x[j,p] <= z[p]               for every original p
            x >= 0.
```

The origin is feasible, every service cap is nonnegative and resource
singleton bounds make the feasible region bounded. Therefore the canonical
exact origin-feasible simplex applies, including zero budget, zero supply,
zero demand and an empty coordinate ground. The client verifies the returned
primal and dual certificate by direct rational inequalities and objective
equality.

Membership in the lower count-service projection is equivalent to attaining
the sum of all caps. Indeed, any projection witness can be reduced separately
at each player until its total equals the requested cap. Downward resource
constraints and nonnegative costs preserve feasibility. Conversely, all
service caps are tight whenever their summed upper bound is attained.
The primal vector then gives an actual fractional allocation.

For strict nonmembership let `y[j,S]`, `lambda` and `t[p]` be the returned
nonnegative dual prices of resource rows, budget and service caps. The
certificate identities and the native returned row are:

```text
sum_(S containing p) y[j,S] + lambda*cost[j,p] + t[p] >= 1
optimum = sum_(j,S) f[j,S]*y[j,S] + D*lambda + sum_p z[p]*t[p]
optimum < sum_p z[p]
a[p] = max(0, 1-t[p])
U = sum_(j,S) f[j,S]*y[j,S] + D*lambda.
```

All resource prices, the budget price and the capacity `U` are nonnegative.
The dual coordinate inequality bounds `a[p]` by the resource-plus-cost price:
when `1-t[p]` is negative, replacing it by zero is safe because the latter
price is nonnegative. Multiplying by any feasible nonnegative original
allocation and summing proves the returned packing row. Its capacity is valid
for every allocation under the remaining assignment budget, without imposing
the query's service caps. Omitted singleton-zero coordinates are identically
zero in all such allocations and do not affect this argument.

The strict dual objective gap proves strict separation: positive-part clipping
can only increase the queried scalar product, whose unclipped value exceeds
`U`. Thus the client returns a valid strict nonnegative original-ground row.
It does not enumerate or store the vertices of the budgeted region or run an
outer support LP. The row has polynomial encoding by the usual rational basic
solution determinant bound. Normalizing the row is unnecessary for the
weighted omission interface; exact nonnegative separation suffices.

## 3. Exact fixed-quota recovery without a budget intersection

Fix an actual original player basis `I` and an integer quota `b >= 0`.
Set all counts outside `I` to zero and impose the original resource ranks
and the partition upper cap `b` at every member of `I`. Remove the budget row.
This is the intersection of the integral resource direct-sum polymatroid and
the integral player partition polymatroid. The intersection is integral by
the same polymatroid intersection theorem used in Section 5 of the main proof.
Its explicit LP constraints are all packing constraints and the origin is
feasible. Every vertex returned by simplex therefore has integral counts.

The implementation uses this exact lexicographic scalarization:

```text
total_cap = b*rank(M)
cmax = maximum original assignment cost on the retained coordinates, or zero
M = total_cap*cmax + 1
maximize sum_(j,p) (M-cost[j,p])*x[j,p].
```

Every feasible count vector has assignment cost between zero and
`total_cap*cmax`. If two integral vertices have different totals, one extra
unit of total dominates their entire possible cost difference. Consequently
an optimal vertex has maximum total and, among all maximum-total points,
minimum actual assignment cost. Integrality of the polytope ensures that this
vertex comparison proves optimality against all fractional points as well.
The scalar has polynomial binary encoding; no loop is indexed by its numerical
value or by the quota. Zero quota and an empty resource ground are included.

If the attained total is below `total_cap`, the quota is infeasible. Otherwise
the player caps are all tight. Compare the actual minimum assignment cost plus
the fixed original setup fee of `I` with the combined budget. This is an exact
fixed-basis quota test. Given a fractional witness of the same quota and the
paired remaining assignment budget, the integral minimum costs no more, so
the recovery succeeds without a unit loss or a budget violation.

This argument minimizes cost over an integral face. It does not assume that
the budget inequality itself preserves integrality. Binary search with the
original total-capacity upper bound gives exact prescribed-basis optimization.
Optional-basis approximation and prescribed-basis exact optimization remain
distinct interfaces.

## 4. Actual one-unit gate and protected setup witness

For small positive full targets the client constructs eligible original
player-type pairs and calls the canonical minimum-weight matroid intersection
implementation. The matroids are the parallel extension of the original
player matroid and the direct sum of the resource Boolean caps. Each pair's
cost is its original assignment cost plus its owner's setup fee. A cardinality
equal to the original player rank pays each selected setup exactly once.
The returned intersection certificate is independently checked before output.
No resource multiplicity is expanded, and forced omissions delete only player
pairs. The one-unit gate is exact for positive coverage, while a larger nominal
small target receives only its promised one-unit weak output.

At a positive-gap node, original matroid greedy returns an attaining
minimum-setup basis in the currently allowed original player set. The client
rejects a lost-rank or unaffordable node. Otherwise it calls the count-service
LP with the combined budget minus that very basis's setup cost. On membership
it recovers on the same basis. It never pairs a setup minimum with a different,
more expensive basis.

For completeness, fix any original full-target basis and its allocation.
At a node still containing that basis, the attained setup cost is no larger
than the protected basis's setup cost. Its original assignment remains
feasible under the current residual budget. The strict row therefore supplies
the same weighted first-crossing omission certificate proved in the setup
companion. One child preserves the protected basis. The canonical iterator
charges dead ends, first crossings, rejected selectors and all recursive calls
on arbitrary inputs. Adaptive setup budgets do not require one unchanged
packing polytope; the protected original witness is the invariant.

## 5. Whole-ground conversion and integer search

The native adapter calls the canonical streamed containment-cover wrapper.
Each seed omits original selection candidates only. The protected full basis
survives every seed avoiding it, with all resource ranks, setup costs and
assignment costs unchanged. The omission call has exactly the residual corank
required by the conversion theorem. There is one original full/weak pair per
call and no repeated approximation across blocks.

For integer factor `d >= 2`, small targets through `d` use the one-unit gate;
larger targets use integer weak quota `ceil(K/d)`. The quota-ratio proof bounds
the worst omission ratio by `(d+1)/(d-1)`. Native rational covers use the sharp
default `27/4` for factor two and `4` for factor three. For other integer
factors, the supplied rational-cover implementation uses the binary-safe
upper envelope `3*(d+1)/(d-1)`. The sharp fixed-factor algebraic cover theorem
remains supported by its exact fixed-exponent comparisons in the
[global conversion proof](../whole-ground-allocation/global-conversion.md);
those comparisons are not implemented in this rational-only adapter.

The optimizer initializes an actual affordable minimum-setup basis with zero
counts and an external impossible integer target one above the resource-total
bound. Only a genuine full-target failure reduces the upper endpoint. A
success saves its actual weak allocation and advances the nominal lower
endpoint; success need not be monotone or certify its nominal full quota.
At adjacent integer endpoints the saved nominal target is at least the
original integer optimum. Its ceiling weak quota gives the stated guarantee.
No rational-utility approximation error is introduced: the positive common
value merely scales the exact integer count.

## 6. Representation, finite reference time and proof audit

Write `N` for the number of retained original type-player variables and `R`
for the number of explicit resource, budget and service-cap rows in an LP.
There are at most `q*m` variables and `m*2**q + q + 1` rows. Complete rank
validation is polynomial in the supplied table length. The native Bland
simplex uses a tableau of polynomial size, with at most
`binom(N+R, R)` feasible bases and polynomial exact work per pivot. Its
potentially exponential finite LP factor is separately charged; it is not the
paid polynomial-time rational LP primitive of the asymptotic theorem. Basic
tableau entries have polynomial bit length by determinant bounds, including
large binary quotas, capacities and dominant recovery coefficients.

The actual prefix recursion, local covers and weighted pair intersection use
their canonical implementations and stated native grounds. They retain
polynomial workspace. The complete-table cost is distinct from the theorem's
oracle complexity, the rational native cover envelope is distinct from the
sharp fixed-factor cover bound, and no numerical capacity or integer quota is
expanded into unit copies. The native reference has no additional player
matroid, several separate budgets or mandatory-resource extension.

The proof audit covers the full main theorem, direct Boolean-cap gate, setup
companion, exact integer-factor quotient argument, protected-witness omission
interface, streamed whole-ground conversion and prescribed-basis endpoint.
The inherited strict-below-two lower bound concerns deterministic recipient
value-oracle approximation with optional bases, even at zero cost. It does
not establish optimality of the exponential bases, does not apply to the
prescribed-basis exact subproblem and is not asserted for explicit recipient
lists. Finite native checks support these proofs without replacing them.

**Attribution:** Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
