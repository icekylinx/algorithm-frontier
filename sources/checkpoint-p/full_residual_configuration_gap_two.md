# An explicit factor-two gap survives every residual configuration cut

**25 October 2026. Root derivation with an independent internal mathematical review.**

The strengthened residual configuration relaxation repairs the
unbounded-rank gap of the simple aggregate LP, but it is not exact.
Even the **full** family of residual cuts has an integrality gap of
two on a single, explicitly described recipient polymatroid. The
polymatroid is a sum of two uniform-matroid rank functions. Keeping
those two components separate gives a strictly stronger configuration
relaxation on this example.

This is an integrality-gap statement about a particular comparator,
not a computational hardness result or an oracle-query lower bound.

## 1. The instance

Choose an integer r>=3, let q=2r, and let the player matroid be
M=U_(r,2r). There is one unit-valued resource with rank

\[
 f(S)=\min\{|S|,r-1\}+\min\{|S|,r+1\}.
 \tag{G1}
\]

This is normalized, monotone, integral and submodular as the sum of
two uniform-matroid ranks. It has singleton rank two and total rank
2r. Each player's local count box is consequently 0<=n<=2, with
no additional restriction. The explicit cardinality formula is a
polynomial-time rank-value representation.

An allocation selects an r-element player basis and gives integer
resource counts to its members. One unit at each selected player is
feasible: for every S, the required count is at most min(r,|S|),
which is no greater than f(S). Two units at every selected player
would require 2r units on that selected r-set I, but

\[
                         f(I)=2r-1.
 \tag{G2}
\]

Thus the integer max-min optimum is exactly one.

## 2. A target-two configuration point

For every player p, place mass 1/2 on its sole target-two
configuration n=2. Then

\[
                x_p=1/2,\qquad y_p=1.
 \tag{G3}
\]

The vector x belongs to B(U_(r,2r)): its coordinates lie in [0,1]
and sum to r. The aggregate y belongs to P(f), since |S|<=f(S)
for every S subset of the 2r players. It remains to check every
subset residual inequality, not merely the aggregate column.

## 3. Exhaustive symbolic verification of all subset cuts

For a subset S of size s, a player inside S has marginal zero.
Every outside player has the common marginal

\[
 m(s)=f(s+1)-f(s)
   =\begin{cases}
      2,&0\le s\le r-2,\\
      1,&s=r-1\text{ or }s=r,\\
      0,&r+1\le s<2r.
     \end{cases}
 \tag{G4}
\]

At s=2r there are no outside players. The full residual cut is

\[
 \sum_p x_p(2-m_p(S))_+\le f(S).
 \tag{G5}
\]

Its left side and right side depend only on s:

| Subset size s | Left side of (G5) | Right side f(S) | Reason it holds |
|---|---:|---:|---|
| 0<=s<=r-2 | s | 2s | Immediate, including the empty set |
| s=r-1 | (3r-1)/2 | 2r-2 | Equivalent to r>=3 |
| s=r | 3r/2 | 2r-1 | Equivalent to r>=2 |
| r+1<=s<=2r | 2r | 2r | Equality |

Thus every subset cut holds. The exact reserve/subset equivalence
in `recipient_polymatroid_subset_cut_compression.md` implies that
every feasible reserved-count cut holds as well, including reserves
with arbitrary support and arbitrarily large counts allowed by f.
This example is not exploiting a bounded-support truncation.

The relaxation has a feasible target-two point, and no target above
two is possible because every player has singleton capacity two.
Equivalently, its base mass is r and its total available value is
2r. Therefore

\[
 \boxed{\quad\mathrm{OPT}_{\mathrm{full\ residual\ LP}}=2,
       \qquad \mathrm{OPT}_{\mathrm{integer}}=1.\quad}
 \tag{G6}
\]

## 4. Separate component configurations retain more information

Represent the same recipient count polymatroid as the aggregate of
two one-service resource components with ranks U_(r-1,2r) and
U_(r+1,2r), both of unit value. Integral polymatroid decomposition
makes the feasible total count vectors exactly P(f)'s integer points.
The underlying integer allocation problem is unchanged.

In the **separate-component** configuration LP, however, a player
reaching value two must take one unit from each component. Any
player-basis configuration point has total player mass r, so it
requires expected total r from the first component. That component
has total rank only r-1. Target two is therefore infeasible.

Target one is feasible integrally, so the separate-component LP's
optimum is exactly one. The full residual LP of the merged rank has
not reconstructed all information carried by the separate component
configurations. Its valid cuts are useful but are not a complete
description of that stronger component relaxation.

## 5. Consequences and boundaries

No algorithm can guarantee a factor strictly below two **against
this full residual LP** on every instance, even with unlimited
computation, because the displayed integer optimum is only half
its LP target. This does not rule out a better algorithm against
integer OPT, nor does it establish that factor two is achievable.

The example also explains why improving the fractional solver does
not yield an integer approximation scheme. The solver may correctly
return a point arbitrarily close to target two, while every integral
solution has minimum value at most one.

The earlier unstrengthened aggregate LP had a gap growing with rank.
This example has a different purpose: it proves a remaining constant
gap after **all** the new residual cuts are imposed. The current
factor-four upper comparison, and the distinct component comparators
for matroid or scaled-matroid resources, remain consistent with it.

The rank construction is elementary; no formal verification or
external publication-priority claim is made. The full-family
calculation and component-merging distinction passed the independent
review in `full_residual_configuration_gap_two_independent_audit.md`.
