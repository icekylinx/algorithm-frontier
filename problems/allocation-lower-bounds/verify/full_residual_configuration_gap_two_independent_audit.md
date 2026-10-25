# Verification note

**Curated source path:** `sources/checkpoint-p/full_residual_configuration_gap_two_independent_audit.md`

The source audit follows.

# Independent audit of the full residual-configuration gap of two

**25 October 2026. Review of G1--G6 and the component comparison.**

The construction in `full_residual_configuration_gap_two.md` passes.
It is an explicit integrality-gap example for the full strengthened
relaxation, with no oracle representation issue and no truncation of
the residual-cut family. The separate-component configuration LP is
strictly stronger on this same integer allocation problem.

## 1. Integer feasibility and the aggregate point

For r>=3 and q=2r, the cardinality rank function

`f(S)=min(|S|,r-1)+min(|S|,r+1)`

is a sum of two integral matroid rank functions. Its marginal sequence
is two for the first r-1 elements, one for the next two, and zero
afterwards. It is therefore also directly a normalized monotone
submodular rank function, with singleton rank two and total rank 2r.

Every chosen r-set admits one unit per member. For two units per
member, the inequality on that very r-set fails: its requested count
is 2r and its rank is 2r-1. Since all count values are integral and
the unit value is one, the integer max-min optimum is exactly one.
Giving additional counts to nonselected players cannot remedy this
violated restriction.

The proposed configuration point puts mass one half on count two at
every player. Its player mass is r, and all coordinates are in [0,1],
so it belongs to the uniform player-base polytope. Its aggregate
recipient vector is the all-ones vector. For 0<=s<=2r one has
f(s)>=s: for s<=r-1 this is 2s>=s; for s=r or r+1 it follows from
the displayed ranks; for larger s it is 2r>=s. Thus all aggregate
recipient constraints hold.

## 2. All residual cuts are included

For a subset S of size s, inside players contribute s in total to
the hinge left side. Every outside player contributes
`(2-m(s))_+/2`, where m(s) is the next rank increment. Hence the
exact left side is

`L(s)=s+(2r-s)(2-m(s))_+/2`.

There are only four cases, covering every subset:

| Range | Rank increment outside S | L(s) | f(s)-L(s) |
|---|---:|---:|---:|
| 0<=s<=r-2 | 2 | s | s |
| s=r-1 | 1 | (3r-1)/2 | (r-3)/2 |
| s=r | 1 | 3r/2 | (r-2)/2 |
| r+1<=s<=2r | 0, or no outside player | 2r | 0 |

All slacks are nonnegative for r>=3. At r=3 the first middle case
is tight; this is permitted. The restriction r>=3 is material:
r=2 would give a negative slack at s=r-1, so the example is not
being asserted in that case. At s=0 both sides are zero, and at
s=2r the last case holds without assigning an artificial outside
marginal to a nonexistent player.

The prior reserve/subset equivalence applies to this integral
polymatroid and these nonnegative configuration masses. Therefore
the verified subset inequalities imply every feasible reserved-count
inequality. No bound on support is used in this inference.

The target-two point is feasible for the full residual LP. A higher
target has no allowed local configuration because the singleton
capacity is two. Thus its LP optimum is exactly two, and the ratio
to the integer optimum is exactly two.

## 3. Merging changes the relaxation but not integer feasibility

The two unit-valued components have independent count vectors in
`P(U_(r-1,2r))` and `P(U_(r+1,2r))`. Integral polymatroid sum
decomposition shows that their achievable summed integer vectors
are exactly the integer points in P(f). Consequently this comparison
keeps the underlying integer problem fixed.

In separate-component configurations, one player receives at most
one unit from each component. Reaching any target strictly above
one therefore requires both units. Every configuration carrying
positive mass at such a target uses the lower-rank component once.
The base-polytope total player mass r forces expected lower-component
usage r, violating its total rank r-1. This excludes every target
above one, not just the single target two. Target one is feasible
integrally using the higher-rank component alone. The separate-
component configuration optimum is therefore exactly one.

This strict inequality does not contradict a statement that component
configurations imply the merged residual cuts. It refutes the reverse
implication for arbitrary sums of different matroid ranks. The example
does not assert anything different about a single supplied scaled
matroid component.

## 4. Exact implication and limitations

The gap rules out an approximation factor below two against this
particular full residual LP, regardless of computational time. It
does not establish integer-OPT hardness, an oracle lower bound, or
an achievable factor-two algorithm. It also does not weaken the
separate theorem bounding the same LP by the current factor-four
allocation guarantee.

All substantive claims G1--G6 and the component-merging distinction
are correct. This is an independent internal mathematical audit;
it is not a claim of implementation, formal verification, external
peer review, or exhaustive publication priority.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
