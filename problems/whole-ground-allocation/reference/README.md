# Executable weighted omission and streamed global conversion

[selection.py](selection.py) implements the actual first-crossing DFS,
weighted omission recursion, logarithmic-block greedy covers and streamed
global wrapper. The [realization proof](../reference-realization.md) gives
its contracts, implementation accounting and complete transfer audit.
It uses exact `int`/`Fraction` arithmetic and no third-party packages.

`first_crossings(order, ratio, deficit, counts=None)` visits budget-pruned
binary prefix words. It yields `(deleted_ids, word)` at the first strict
density crossing and stops extending that word. The zero-count budget is
computed exactly, stored in binary, and bounded exploration always stops
at the actual order length. It does not enumerate all omitted subsets.

`gap(q, rank, full, weak, prepare, separate, forced=(), observe=None, counts=None)` runs iterative depth-first weighted omission on original IDs
`range(q)`. The selected cardinality is positive and fixed; targets satisfy
`full > weak > 0`. Its interfaces are:

- `prepare(allowed)` returns a canonical `Choice(selected, context)` with
  the required original selected cardinality, or `None` for no legal
  restricted choice. Adaptive clients must return an attaining completion.
- `separate(allowed, choice, rates)` returns a canonical nonnegative `Row`
  valid for the current region and strictly violated at `rates`, or `None`
  for membership. The vector always has every original coordinate and zero
  service outside `allowed`.
- Fixed-region clients require globally valid rows for one downward region.
  Adaptive clients additionally prove that the same full witness survives
  every current region while its selected set survives. The program checks
  local row shape and violation; it does not certify arbitrary external
  oracle correctness or that protected-witness hypothesis.

A `GapResult` retains the actual selected choice and reached-work counts.
Membership proves weak service for its selected subset; model-specific
witness recovery remains the caller's paid operation. `None` is a sound
full-target rejection under the stated interfaces. Rank-zero families use
the separate empty-selection convention outside this API. Failed selector
nodes, zero-deficit exits and unfinished prefix states are counted. The
optional observer's work and retained snapshots are additional user costs.

`explicit_separator(rows,q)` realizes a fixed original rational packing
system. `uniform_selector` attains minimum additive cost on unrestricted
fixed-size subsets, optionally with a fixed threshold.
`common_matroid_selector` reuses the canonical
[certified weighted matroid intersection](../../robust-bounded-certificates/reference/README.md)
on the original IDs with restricted-outside loops; it supports one fixed
selection-cost threshold. It does not add several unrelated constraints.

`local_cover(n,p,base)` chooses the exact minimizing seed size, then builds
the greedy containment cover with lexicographic subset ties.
`cover_seeds(q,corank,base)` stores only local logarithmic-block covers and
streams every admissible count profile and Cartesian-product seed.
`whole_ground(q,rank,base,extension)` invokes `extension(seed)` until a
non-`None` answer, or returns `None` after exhaustion. The callback must
return `None` on ordinary failure and a legal weak result otherwise, with
the declared uniform extension bound for the supplied rational `base > 1`.
A separate structural outcome, when a client has one, must be propagated
as such by that client rather than interpreted as an ordinary failed seed.

`rational_optimize(alpha, denominator_bound, upper, initial, gap_oracle, reoptimize)` implements the fixed-family rational grid search and original
fixed-set reoptimization. `initial` is a legal family member; `upper` and
the binary denominator bound are valid uniformly over the fixed family.
The gap oracle returns a choice or `None` under the one-sided promise.
`reoptimize(choice)` returns the original exact optimum and its witness.
The output retains the same full requested relative accuracy. Changing
family membership with the nominal target is outside the contract.

`flow_gap(network,rank,full,weak,budgets=(),setup=None,forced=(),selector=None)`
is a native integration with the canonical selected-flow Farkas separator
and fixed-set certificate recovery. It executes the real prefix recursion
with fixed routing rows or one adaptive shared setup/routing budget. The
default selector attains minimum setup on unrestricted fixed-size sets.
An external setup selector must attain its true minimum on its declared
fixed family; its actual returned setup is subtracted again at each node.
Original budget iterators are materialized before repeated calls.

The generic prefix and global engines have the proved bounds with their
paid selector/separator/extension interfaces. The native flow integration
uses the existing finite Bland simplex, whose potentially exponential LP
cost remains charged separately. This implementation does not supply a
polynomial-time simplex theorem, all allocation recovery backends, or
Gaussian/implicit uncertainty interfaces. Source is licensed under the
repository Apache-2.0 license.

**Attribution:** icekylinx and GPT-6 Astra Pro.
