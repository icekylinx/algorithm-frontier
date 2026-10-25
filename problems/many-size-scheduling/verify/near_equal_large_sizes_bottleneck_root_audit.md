# Verification note

**Curated source path:** `sources/checkpoint-o/near_equal_large_sizes_bottleneck_root_audit.md`

The source audit follows.

# Root audit: heterogeneous large bands and bottleneck commitments

**25 October 2026. Internal mathematical review.**

The root reviewer read the full H1--H16 manuscript in
`near_equal_large_sizes_bottleneck_makespan_draft.md`. Its filename is
historical; the construction passes this review after explicitly
defining the band endpoints as the actual extrema of positive-rank
large types. The endpoint convention justifies both target rejection
below a_+ and the rational workload-grid identities.

## 1. Aggregation fixes positions, not premature type assignments

The sum of the large-type ranks has an integral base decomposition.
Under the unit box, any full-rank basis gives h distinct recipient
machines and can be decomposed into all original large-type bases.
The commitment F0 is only an independent set of this aggregate
matroid. No particular type is committed there before the final basis
is completed; doing so could invalidate the spanning argument.

If the Boolean rank drops below h, no schedule with target below
2 a_- can exist. The public additive algorithm then gives
`OPT+a_+ <= (1+R/2) OPT`. This branch needs no bottleneck profile.

## 2. The residual promise and output bounds use opposite endpoints

At a hard feasible target, every selected large-job machine has
small workload at most `T-a_-`, regardless of its actual large type.
The dual therefore provides the common quota `K=a_-/Delta` on the
original large-recipient basis. Arbitrary independent commitments
preserve this quota on a basis of the player contraction.

The final residual large assignment is bounded above by a_+.
Consequently the noncommitted selected machines have load at most
`T+a_+-a_-/D+u`. With `T>=a_+` and `D>=1`, this is at most
`(2-1/(DR)) T+u`. The easy branch contributes `1+R/2`.
Both endpoint uses and their directions are correct.

## 3. The stronger machine bottleneck remains valid after rounding

For any machine receiving one large unit, its assigned type has
positive singleton rank there and hence size at most a_p. Every
final smaller component obeys its original singleton bound, so
the machine's load is at most `W_p+a_p`. This conclusion holds
after smaller-job rounding and incurs no additional +u.

Sorting these costs and applying matroid greedy gives an independent
set of each required cardinality with minimum bottleneck. Loops are
never selected even if their nominal cost is small. A single greedy
order supplies the whole profile B_k. The empty commitment at k=h
has bottleneck zero.

## 4. Exact quotas and target search

Writing rational D=A/B and choosing `Delta=g/A` makes both K and
`b=K/D` integral. All actual sizes lie on the original g-grid, so
every target and output needed for the refined-grid search has
polynomial encoding length. D need not be expanded numerically.

At rank k, `D_k b <= Db=K` gives strict feasibility of the unit
quota condition. With `D=D_k+eta`, the relative cover margin is
greater than eta/2. The proof does not borrow a large-original-unit
promise; it engineers the equality in the fractional workload model
and later pays the +u integrality cost.

Only genuine infeasibility rejections remain. Grid binary search
therefore gives a successful target at most OPT, even if the success
set is not monotone. The bound `max(beta T+u,B_k)` is monotone in T.
Thus the displayed theorem is against the original OPT, without a
private-slack cap threshold.

## 5. Zero residual rank and band enumeration

For k=0, commit a full bottleneck large basis and balance the smaller
workload independently. Its fractional optimum is at most OPT.
After original-type decomposition and rounding, the committed machines
are bounded by B0 and the remaining machines by `OPT+u`. This proves
the polynomial endpoint `max(OPT+u,B0)` without using a nonexistent
formula D0. The argument also works when the smaller band is empty.

Trying all distinct top-size suffixes is polynomially many choices.
For each band its h, u, extrema, Boolean matroid and bottleneck profile
must be recomputed. Running the allowed rank budgets and returning the
best actual schedule proves the envelope of their bounds; it does
not require knowing OPT to select the best theoretical band.

## 6. Coefficient arithmetic and public comparison

For `R<=1+tau`, the hard coefficient satisfies

\[
 2-\frac1{(3+\eta)(1+\tau)}
 \le\frac53+\frac\eta9+\frac\tau3.
\]

This follows by separating the loss from eta and tau, respectively
bounded by eta/9 and tau/3. For `0<=tau<=1`, the easy coefficient
`3/2+tau/2` is at most `5/3+tau/3`. The k=3 exact coefficient is
below 5/3 for `R<9/7`; the easy branch is also below 5/3 throughout
that range. The additive u and commitment term still have to be paid.

The root directly opened the primary Jansen--Rohwedder full version
at <https://arxiv.org/html/1701.07208v2>. Its constructive 11/6-plus-error
quasipolynomial result concerns ordinary restricted assignment without
the size-band promise. The new theorem trades that unconditional scope
for its stated size parameters and general job-polymatroid model; it
does not dominate the public theorem on every instance. Enumerating
all h large placements gives a separate `q^{O(h)}` quality baseline
and must not be described as fixed-parameter time in h.

## Verdict

The heterogeneous-band transfer, computed bottleneck profile,
finite-rank coefficient, zero-budget endpoint and one-sided search
are accepted within their explicit model. This is internal proof
review, not formal verification, external peer review or exhaustive
publication-priority certification.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
