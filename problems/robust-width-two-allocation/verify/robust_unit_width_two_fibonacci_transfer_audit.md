# Verification note

**Curated source path:** `sources/checkpoint-q/robust_unit_width_two_fibonacci_transfer_audit.md`

The source audit follows.

# Independent review of the width-two Fibonacci unit gate

**25 October 2026. Reviewer: transfer_frontier. Full review of
`robust_unit_width_two_fibonacci_gate.md`, WF1--WF9: PASS.**

This review covers the exact singleton/pair reduction, dual-basis
branching, matching terminal solver, guarded all-input implementation,
and the global conversion. It is an internal mathematical review.

## 1. Exact conflict information in the original unit families

The fixed-set unit oracle includes each scenario's original aggregate
resource constraints and its scalar assignment budget. Its feasible
sets are hereditary because assignments and nonnegative costs can be
discarded on removed players.

Every actual robust unit basis avoids every failed singleton and every
failed pair. Conversely, an original M-independent set avoiding those
conflicts cannot fail under the width-two promise: an inclusion-minimal
failed subset would still be M-independent and would have size at least
three. Thus the weaker promise only on M-independent minimal failures
is sufficient. Testing pairs that happen to be M-dependent causes no
problem; no actual M-basis contains such a pair anyway.

The graph contains aggregate budgeted failures. It is not inferred from
individual matroid circuits or from the number of variables in one
packing row. Constructing all singleton and pair tests is polynomial in
the explicit scenario input size.

## 2. Dual complements and forced omissions

For N=M*, an original basis I is exactly the complement of an N-basis
D. Avoiding failed singleton vertices F means F is contained in D;
avoiding each failed pair means D covers that graph edge. Requiring an
extension to omit Z means Z is also contained in D.

If F union Z is dependent in N, no protected dual basis can contain it.
Otherwise contracting it reduces the rank by its cardinality, deletes
only already covered graph edges, and leaves the exact residual task.
Its rank is at most c-|Z|, which is the uniform seed parameter required
by the global conversion. Loops, coloops, and rank-zero residual cases
are covered by the same independence and contraction tests.

## 3. The matching terminal case is complete

When every residual degree is at most one, its edges are disjoint. A
common independent set of cardinality equal to the number of edges in
the current dual matroid and the one-per-edge partition matroid chooses
exactly one independent representative of each edge. It can then be
extended to any full basis of the current dual matroid, using isolated
vertices and possibly additional endpoints. This extension preserves
coverage and restores the required original dual-basis cardinality.

Conversely, any independent cover contains an independent subset with
one representative from each matching edge. If the intersection test
fails, no independent cover or covering basis exists. The proof does
not require the final basis to contain exactly one endpoint per edge;
that restriction is imposed only on the representative subset. This
distinction is necessary and correctly handled.

For an empty matching, the empty set extends to a basis. If the rank is
too small to represent all edges, intersection fails. Rank zero with an
uncovered edge therefore fails and rank zero without edges succeeds.

## 4. Branches preserve arbitrary matroid constraints

At a vertex v of degree a>=2, every covering basis contains v or all
of its neighbors. In the first case the singleton is independent and
can be contracted; in the second case the neighbor set is independent
and can be contracted. Contracting a subset of a protected basis leaves
its remainder as a basis of the contraction. Thus at least one child
preserves every protected solution.

An attempted selected set larger than the current rank, or containing
a loop or dependence, is rejected before recursion. The second child
does not need to forbid v later. Allowing v in a later extension only
causes overlap between branches and cannot invalidate a covering basis.
No unconstrained vertex-cover leaf dominance is assumed.

## 5. The Fibonacci bound includes all work

Successful recursive decrements are one and a>=2. For
phi=(1+sqrt(5))/2,

    phi^(-1)+phi^(-a) <= phi^(-1)+phi^(-2)=1.

Assign a leaf the product of the inverse-base weights along its path.
The total weight of recursively reached leaves is at most one, and
each leaf has weight at least phi^(-h) when the initial residual rank
is h. There are therefore at most phi^h leaves and at most
(h+1)phi^h processed nodes. Each node pays for both attempted
independence tests, including rejected branches; these attempts do not
create an unaccounted exponential term. Matching intersections, basis
extensions, graph updates, and final unit tests are polynomial work.

Depth-first execution uses polynomial space. The bound holds uniformly
for every seed, including seeds with no possible covering basis, and
is at most phi^(c-|Z|) times polynomial work. Exact comparison for the
fixed quadratic base can use arithmetic in Q(sqrt(5)); the Fibonacci
power identity gives polynomial-bit representations. Thus the stated
streamed conversion has whole-ground base

    2-1/phi=(5-sqrt(5))/2.

## 6. Guard semantics and higher quotas

If no graph-covering dual basis exists, no actual robust unit basis
exists even outside the promise, by the always-valid forward direction
of the conflict reduction. If a covering basis is returned but fails an
actual scenario test, shrink it in that original scenario. It contains
no failed singleton or pair, so the resulting original minimal failure
has size at least three. Returning that set as WIDTH VIOLATION is sound.
It must not be turned into target infeasibility or a failed global seed;
the manuscript explicitly preserves this third outcome.

On promised inputs the guard cannot occur at any seed. This proves both
the unconditional running-time bound of the guarded implementation and
the exact promised correctness of the global algorithm.

The higher-quota theorem changes only its once-run exact unit gate.
Its positive-gap base remains A_d, so the combined corank base is
max{phi,A_d}, not their product. The usual factor-two and factor-three
positive quotas still dominate that maximum. The direct numerical gain
is the exact unit decision, the Boolean-resource zero-or-one
optimization case, and the coarse-tradeoff gate term. The stated scope
does not claim fastest known graph algorithms or a general dense-row
improvement.

## 7. Verdict

The entire refinement passes. No substantive correction is requested.
Its improvement follows from a valid polynomial terminal solver and a
complete matroid-aware Fibonacci branching argument, with the original
budgets and the all-input width guard retained.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
