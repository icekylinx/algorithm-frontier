# A direct Boolean-cap and one-unit gate proof

This note discharges the Boolean-cap matroid premise in
[Section 6 of the main theorem](proof.md#6-the-k1-gate-uses-minimum-cost-matroid-intersection).
The main theorem charges exact weighted matroid intersection, submodular
minimization and rational linear programming as paid polynomial primitives.
The construction below identifies their finite grounds and independence
oracles; it does not expand binary resource capacities into unit copies.

## Boolean caps are matroids

Let `f` be a normalized monotone integral submodular function on a finite
player ground `P`. Call a set `I` independent when its incidence vector
belongs to `P(f)`: equivalently, `|I intersect S| <= f(S)` for every subset
`S` of `P`. The empty set is independent, and every subset of an independent
set is independent.

For augmentation, fix independent sets `I,J` with `|I|<|J|`. Suppose that
no element of `J minus I` can be added to `I`. For every such element `e`,
integrality gives a set `S_e` containing `e` with `f(S_e)=|I intersect S_e|`:
a constraint violated after adding one unit had integral slack zero before
that addition. Sets tight for `I` are closed under union and intersection.
Indeed, submodularity bounds the sum of their ranks from below by the union
and intersection ranks, while feasibility bounds those ranks from below
by the corresponding incidence counts; modularity of incidence counts
forces equality throughout.

Their union `S` is therefore tight and contains `J minus I`. Independence
of `J` gives `|J intersect S| <= f(S)=|I intersect S|`. Outside `S`, every
element of `J` already belongs to `I`. Adding the inside and outside counts
gives `|J|<=|I|`, a contradiction. Thus augmentation holds and the Boolean
cap is a matroid.

An independence query is implemented by minimizing the submodular function
`f(S)-|I intersect S|` and checking that its minimum is nonnegative. Its
values have polynomial binary length relative to the supplied rank oracle
and explicit ground. No array is indexed by a numerical resource capacity.

## The assignment-pair gate

Create one pair `(p,j)` for each player and resource type with `f_j({p})>=1`.
For every type, lift its Boolean-cap matroid to those pairs; their direct
sum is a matroid `D`. A set is independent in `D` exactly when each type's
selected player set receives a legal incidence-vector allocation.

The second matroid is the parallel extension of the original player
matroid `M`: its independent sets contain at most one copy of each player,
and their projected player set is independent in `M`. Heredity is immediate.
For augmentation, project two independent pair sets of different sizes;
matroid augmentation in `M` supplies a player present only in the larger
projection. Adding that player's pair from the larger set preserves both
projection independence and the one-copy restriction.

Consequently a common independent set of size `rank(M)` supplies one unit
to every player of an actual original basis, with every resource constraint
satisfied. Conversely, any legal positive integer allocation on a basis can
be trimmed to one assigned unit per player. Downward resource constraints
and nonnegative costs preserve feasibility and do not increase its cost.
The retained units give exactly such a common independent pair set.

Give pair `(p,j)` its original assignment cost. Minimum-weight matroid
intersection at the prescribed cardinality therefore decides the one-unit
gate by comparing one minimum cost with the original budget. There are at
most the player count times the number of types pairs. Pair costs, rank
values and the original budget retain their binary encodings. The gate does
not assume that intersecting an integral polytope with a budget inequality
preserves integrality: it minimizes the budget objective first.

## Review boundary

Together with the main proof's nonnegative projection separator, weighted
[first-violation omission theorem](../whole-ground-allocation/selection.md),
no-loss fixed-quota recovery and one-sided integer target search, this closes
the main exact factor-two construction under its paid exact primitives.
The setup-budget companion and the separate whole-ground inclusion-cover
conversion require their own arguments. The finite
[gate checker](verify/check_one_unit_gate.py) tests the construction on named
small instances; it neither implements general weighted matroid intersection
nor proves the unbounded algorithm by enumeration.

**Attribution:** icekylinx and GPT-6 Astra Pro.
