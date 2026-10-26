# Direct-spanner parameter budget and the next recourse obstacles

**Internal continuation note, 25 October 2026.**

This note concerns the specific certificate and accounting in
[dynamic spanners proof](../../problems/dynamic-spanners/proof.md). It proves no lower
bound on graph spanners, distance oracles, or dynamic algorithms.
The positive terms below are the ones that the current proof charges,
not necessary costs of every execution or every alternative algorithm.

## 1. Nonuniform parameters do not improve this certificate budget

Let `B` be the logarithmic work allowance of the normalized APSP/flat
forest hierarchy and `A` its charged logarithmic metric stretch.
Sections 1--2 of [nonuniform-parameter-budget-frontiers.md](../graph-backends/nonuniform-parameter-budget-frontiers.md) consider
the initial nominal size range whose logarithms are comparable to `U`.
They allow different routing, repair, and shrink parameters at every
level and prove the positive-budget inequality

```math
A\gtrsim U^4h/B^4.        \tag{R1}
```

For completeness, the model charges `x_i` and `u_i/p_i` to `B`,
and charges `sum_i u_i/K_i` to `B`. A total nominal shrink
`sum_i x_i=Omega(U)` forces at least `Omega(U/B)` levels, and
`p_i=Omega(U/B)`. Cauchy's inequality gives
`sum_i K_i=Omega(U^3/B^3)`. The metric charge
`h sum_i K_i p_i` is therefore at least the right side of (R1).
An actual graph that shrinks much faster is not asserted to attain
this ledger.

The direct spanner exposes a changed short compressed record by
listing at most `R=exp O(A)` physical occurrences. Its certified
time overhead is `exp O(B+A)`. Thus a common positive budget `Z`
for this proof must cover both `B` and `A`. Substituting into (R1),

```math
Z^5\gtrsim U^4h.               \tag{R2}
```

The four-fifths choice attains this displayed envelope. Nonuniform
inner parameters or fewer current marks alone do not remove (R2):
fewer marks improve the current output-size bound, while the present
per-changed-record analysis still pays `R`.

Equation (R2) ceases to apply if a new proof avoids that `R` charge,
improves the metric/work relation, or uses a different certificate.
It is explicitly an obstruction to retuning this positive upper-bound
formula, not evidence of an algorithmic lower bound.

## 2. A real obstruction for exact short-path-union maintenance

An unrestricted marked-forest interface cannot report the **exact**
current short-path union with constant update output independent of
`R`. Take an ordinary path with `r` physical edges, each of length
one, and set `R=r`. With both endpoints marked, its one compressed
edge is short and its full path belongs to the exact union. Remove
one endpoint mark: the minimal marked subtree is now a single vertex,
and all `r` output edges disappear. Reinsert that mark: all `r`
edges reappear. The forest itself did not change.

This example proves `Omega(R)` output changes for the particular
exact-union selection rule. It does **not** prove such a cost for a
spanner algorithm: keeping the whole path is already an excellent
spanner, and a different certificate may retain those edges. It also
does not show that the abstract alternating mark sequence is generated
by the actual numerical hierarchy. It is a warning against claiming
that a better dynamic-tree iterator alone removes the charge.

The cached-list implementation can avoid needless reference-count
churn on special operations. For instance, splitting an already short
compressed path into short pieces leaves its physical union unchanged.
That optimization is valid but does not resolve the example above
or the general output selection problem.

## 3. Why keeping all historical output edges is insufficient

Retaining an old output edge until its original physical deletion
would remove artificial output deletions and is attractive for the
insertion-independent recourse goal. However, the current size proof
counts only **current** marked compressed paths. It gives no bound
on the union of their supports over many obsolete forest generations
or active-source changes. Keeping all those historical supports can
grow to the dense original graph.

There is a valid but limited monotonic observation: after an original
edge insertion, an old spanner remains valid for all old input edges,
and adding that one new original edge restores the same stretch for
the new graph. This costs one output insertion. Repeatedly doing so
eventually violates the sparse size cap unless another sparsification
operation is paid. Upon an original deletion, an old spanner path can
break, so this insertion argument does not supply repairs.

One can rebuild from the current direct certificate after sufficiently
many insertions, paying its actual sparse output size. Rebuilding after
every harmful deletion can instead cost that size per deletion and
does not prove the desired fast arbitrary-deletion theorem. No such
unpaid rebuild is included in the proved four-fifths result.

## 4. Concrete remaining avenues

The following are open construction questions, not established
improvements:

1. **A persistent sparse support.** Keep enough obsolete paths to
   avoid large output changes from a mere certificate replacement,
   while proving a current `n exp O(Z)` size bound. Its proof must
   control historical supports, not only present mark count.
2. **A weaker repair certificate.** On an original deletion, find
   only the edges needed to repair the current spanner instead of
   installing the entire current short-path union. It must avoid
   scanning the dense original graph on each deletion.
3. **A structural restriction on real trace changes.** Derive an
   amortization specific to the actual `S_i` source traces and stable
   forest lifetimes, stronger than arbitrary marked-forest updates.
   The preceding path example does not rule this out.
4. **An implicit route/counter interface.** Congestion-based greedy
   sparsification would benefit from updating and invalidating stored
   query routes without enumerating their full walks. A valid interface
   must account for repeated original IDs, old-version lifetimes, and
   reporting all affected stored routes when a physical edge dies.
   A distance estimate or one implicit path alone does not provide it.

The five-sixths batching construction already proves
`(n+D) exp O(U^(5/6)h^(1/6))` output recourse for arbitrary histories.
The direct four-fifths construction proves the faster ordinary-recourse
statement. This note does not combine their advantages without an
additional argument.
