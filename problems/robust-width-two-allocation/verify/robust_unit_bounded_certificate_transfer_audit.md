# Verification note

**Curated source path:** `sources/checkpoint-q/robust_unit_bounded_certificate_transfer_audit.md`

The source audit follows.

# Independent review of robust unit allocation with bounded failure certificates

**25 October 2026. Reviewer: transfer_frontier. Full mathematical review of
`robust_unit_bounded_certificate_exact_tradeoffs.md`, BW1--BW16: PASS.**

This review covers the entire manuscript, including the all-input guarded
algorithm, the global exponential conversion, and the concrete examples.
It is an independent mathematical review, not a formal verification or a
claim of publication priority.

## 1. The width condition has the right scope

For each explicit scenario, let its unit-feasible family consist of the
player subsets that can receive one unit each using that scenario's
original recipient polymatroids and its exact assignment budget. This
family is hereditary: assignments to players removed from a subset can
be discarded because all assignment costs are nonnegative.

The manuscript bounds the size of an inclusion-minimal failure in this
**aggregate, budget-inclusive family**. It does not confuse that condition
with a circuit bound for an individual resource. It is enough to impose
the bound on player-matroid independent sets, because every certificate
the algorithm constructs lies in an actual basis of the original player
matroid. The original scenario resources are never contracted when
player candidates are omitted.

The one-unit feasibility test is exact. On a fixed player subset, Boolean
caps of the resource polymatroids form one direct-sum matroid, and the
at-most-one-unit-per-player condition forms a second matroid. Minimum-cost
intersection of the required cardinality tests both coverage and the
actual scalar budget. The original player matroid is not a third
constraint in this fixed-subset test.

## 2. One scan really finds a minimal original failure

Start from a failed basis and retain a set C that is still infeasible.
When testing an element p, delete it if C without p is infeasible. If p is
retained, its removal was feasible at that moment. Later deletions only
shrink that feasible removal set; heredity therefore implies that the
final C without p is feasible. Thus a single scan gives an
inclusion-minimal failure, rather than merely a set minimal relative to
the particular deletion order.

The empty set is feasible, so the final certificate is nonempty. Its
infeasibility and the feasibility of every single-element deletion can
be checked by the same exact unit oracle. In particular, the certificate
includes assignment-budget infeasibility when that is the cause of
failure; it is not just a resource-rank witness.

## 3. Branch correctness and the third outcome

At a surviving candidate set Q, the algorithm first finds an original
player-matroid basis I_Q. If it is unit-feasible in every scenario, the
actual scenario assignments certify success. Otherwise it finds a
minimal failed C contained in I_Q. Every promised robust unit-feasible
basis must omit an element of C, so branching on the deletion of each
element of C preserves a promised basis in at least one child.

The WIDTH VIOLATION output is essential. A certificate larger than the
supplied bound w is neither target infeasibility nor a failed global
seed. Propagating it as a separate outcome makes the algorithm's
all-input running-time bound valid. On an input satisfying the width
hypothesis, no recursive node or forced seed can trigger the guard:
the constructed C is always an original, player-independent minimal
failure to which the hypothesis applies.

At zero remaining corank, Q has exactly the rank number of elements.
It is then the only possible basis, so a failed test is a sound terminal
failure. With remaining corank h, all attempted children, including
children rejected by a player-rank test, fit the bound

    1 + w + ... + w^h <= (h+1) w^h.

Forced omissions Z simply initialize Q as the complement of Z and
reduce the remaining budget to c-|Z|. This supplies the uniform
extension interface needed by the global conversion. The case w=1
is already polynomial and does not require applying an exponential
conversion theorem at base one.

## 4. Higher quotas and exact per-scenario recovery

For K>d, the weak quota b=ceil(K/d) has

    K/(K-b) <= (d+1)/(d-1).

The intersection of the scenario budgeted fractional count regions is
downward closed. A failed scenario supplies a nonnegative packing row
valid for the whole intersection. The same protected original basis
works for every such row, even if different nodes use different
scenarios. Hence the weighted omission argument has the stated base
A_d=Gamma((d+1)/(d-1)).

For a returned basis, fractional counts can be trimmed to b at each
selected player separately in every scenario. Intersect that scenario's
resource product with integral player quota caps and take the full-total
face of value b times the player rank. Minimum actual assignment cost on
this integral face gives an integer b-unit allocation of cost no greater
than the fractional witness. The same selected basis is retained across
scenarios. The budgets can differ because the allocations themselves
are adaptive and different; no simultaneous multi-budget rounding of a
single assignment vector is asserted.

The exact unit gate is run once. Its saved witness supplies the weak
quota one for all K<=d. A sound unit failure implies integer optimum
zero. The one-sided integer maximization search has an external finite
upper bound, treats only genuine full-target failures as failures, and
returns at least ceil(K*/d). It does not assume that weak successes are
monotone. Binary bounds give polynomially many target calls.

## 5. The combined bases and global bounds are correct

The unit gate and positive-gap algorithm are run as separate procedures,
so their time factors add. They are bounded by a polynomial times

    max{w,A_d}^c,

not by the product of those bases. Global conversion can likewise be
applied separately, giving the maximum of the two transformed bases.
The guarded outcome must continue to propagate through that conversion.
Under the width promise every seed remains within the bound, so the
complete seed-generation and failed-seed costs are covered.

The special constants check: d=2 has A_d=27/4 and global base 50/27;
integer width at most six does not increase that base. For d=3,
A_d=4 and width at most four retains global base 7/4. The proof does not
claim these are optimal bases. Clipping a vacuous width bound to the
player rank and the manuscript's fixed-d versus variable-d arithmetic
qualifications are consistent with its input and space bounds.

## 6. Concrete examples and their limitations

With zero costs or a redundant unit budget, the scenario unit family is
the independent-set family of the union of the resource Boolean-cap
matroids. Its aggregate circuits are the relevant certificates. For
example, many rank-one uniform resources have individual circuit size
two, whereas their union can have much larger circuits; the manuscript
correctly excludes that invalid inference.

In the graph specialization, one Boolean partition resource per
scenario makes feasible unit sets avoid the forced loop vertices and
contain no parallel-class pair. After forced vertices are checked and
contracted in the dual player matroid, the omitted set is a dual basis
covering the remaining graph edges. The maximum unit value is genuinely
zero or one in this specialization, so the gate alone solves its
optimization problem exactly. No arbitrary graph independence system
is presented as a single matroid.

For disjoint capacity pools, the width statement explicitly requires
zero assignment costs or a redundant unit budget. A binding pool of
capacity b has a minimal unit obstruction of size b+1; a nonbinding pool
has none. Large nonbinding binary capacities may still matter to higher
quotas and do not invalidate the unit-width argument.

For nonnegative integral modular unit prices and a scenario budget at
most U, a minimal budget failure independent in the aggregate matroid
contains no zero-price player. Removing one player leaves at most U
positive integral prices, so the certificate has size at most U+1.
Resource-dependent minimal failures are aggregate circuits. Therefore
the stated maximum of the circuit bound and U+1 is valid, without a
constant-width claim for arbitrary binary budgets or arbitrary pair
costs.

## 7. Verdict

The theorem, its guarded implementation, and the stated applications
pass this full review. The width assumption is a substantive restriction
on original aggregate budgeted failures, and the manuscript preserves
that restriction throughout its claims. It is consistent with the
unrestricted robust unit-feasibility obstruction and does not claim an
unconditional finite-factor robust allocation algorithm.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
