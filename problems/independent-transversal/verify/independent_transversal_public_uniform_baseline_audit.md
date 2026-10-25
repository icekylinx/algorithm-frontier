# Verification note

**Curated source path:** `sources/checkpoint-o/independent_transversal_public_uniform_baseline_audit.md`

The source audit follows.

# Public uniform baselines for the full independent-transversal certificate

**Primary-source comparison, 25 October 2026.**

This note accompanies the internally audited research construction
`independent_transversal_current_blocker_growth.md`. It does not change
checkpoint G or its accepted weak-Haxell and spanner statements. The
comparison below is with named constructions and their verified input
and output contracts; it is not a claim that every possible public
reanalysis has been optimized.

## 1. The contract being compared

Let a loopless graph have `q` nonempty vertex classes and explicit input
size `P=|V|+|E|+q+2`. The partition-relative claw parameter `r` means that
no vertex has `r` independent neighbours in distinct classes. For
`0<epsilon<1`, the full certifying task returns either an independent
transversal (IT), or a class set `S`, a total dominating set `D` for all
vertices in those classes, and a constellation `K` on a class set
`S_0` containing `S`, such that

\[
 |D|<(2+\epsilon)(|S|-1),\qquad
 V(K)\subseteq D,\qquad
 |D\setminus V(K)|<\epsilon(|S|-1).
\]

The constellation is induced in `G_(S_0)`: first restrict to the
classes in `S_0`, then delete all within-class edges, as in the
source's Definition 3. It need not be induced in the original graph
before those edges are deleted. The constellation condition is part of
the comparison. It is needed,
for example, to recover the near-`2r-3` hypergraph matching threshold
from the intersection-graph reduction. A generic approximate dominating
set is not an interchangeable output. The failure alternative does not
assert that no IT exists.

## 2. Named general baseline and uniform reanalysis

[Graf--Haxell, arXiv:1811.02687v2](https://arxiv.org/html/1811.02687v2),
Theorem 4, gives the full certifying task. Its published theorem states
polynomial time for fixed `r` and `epsilon`; Section 8 explicitly leaves
the parameter dependence unoptimized. The source's feasibility,
depth, and signature interfaces are Definition 10, Lemma 16,
Definition 17, and Lemmas 18--20. The public latest arXiv version is
v2, dated 27 February 2020.

Here is a useful stronger quantitative baseline derived directly from
those interfaces. Choose uniformly feasible parameters

\[
 \mu=\rho=\epsilon/(100r),\qquad Q=\lceil1/\mu\rceil,
\]

where `Q` denotes the paper's cap parameter `U`. Put
`z=r/epsilon`. The original birth-growth argument gives

\[
 L_0=O(z\log(q+1)).
\]

The signature base is `b=Q/(Q-mu rho)`, so `log b=Theta(z^{-3})`.
At a continuing boundary, noncollapsibility implies
`|X_i|<=|Y_i|/(1-mu)<=2q`. Consequently the largest finite
absolute signature coordinate is at most

\[
 H_0=O\!\left(z^3[L_0\log(2+z)+\log(q+1)]\right).
\]

There are at most `2L_0` finite coordinates and their absolute values
are nonnegative nondecreasing integers. A count by length and height,
using weakly increasing lists rather than arbitrary subsets of the
height range, therefore yields

\[
 \log\#\mathrm{signatures}
   =O\!\left(L_0\log(2+H_0/L_0)\right)
   =O\!\left(z\log(2+z)\log(q+1)\right).
\]

Thus a fair named **derived-public** baseline for the same contract is

\[
 P\,(q+1)^{
            O((r/\epsilon)\log(2+r/\epsilon))}.
\]

This is a derivation in the present notes, not a displayed rate in the
paper. It already improves a literal use of the paper's coarse height
count and should be used instead of that coarse bound. The linear
input multiplier uses the common implementation proved in
`independent_transversal_input_linear_iteration_implementation.md`
and independently audited in Section 8 of
`independent_transversal_current_blocker_independent_audit.md`.
The paper itself retains a coarse `O(|V|^4)` per-iteration bound.
No new stopping condition is needed for this baseline. Both rates
also have the common rational-input bit factor displayed below.

The current-blocker construction retains the signature's height-to-length
ratio but adds a certifying stop that forces
`L=O(epsilon^{-1} log(q+1))`. Its audited rate is consequently

\[
 P\,(q+1)^{O(\epsilon^{-1}\log(2+r/\epsilon))}
       \operatorname{poly}(b_\epsilon+\log P).
\]

The improvement is the factor `r` in the exponent on the class count.
Since `r` can be replaced by `min(r,q+1)`, its arbitrary-graph
specialization is polynomial in explicit graph input and
quasipolynomial in `q` for fixed `epsilon`. This statement uses an
additional valid certificate stop; it is not attributed verbatim to
the source algorithm on arbitrary inputs.

### 2.1 A parameter-independent elementary fallback

The original single-vertex proof sketch in Section 2 of the same
primary source gives another baseline. At a stable state its
blocker-count signature is a positive integer list whose sum is at
most `q-1`. There are only `2^{q-1}` such lists, including the
empty list. A free-centre cascade can be processed before counting
the next stable state, and takes at most `q` swaps. An explicit
adjacency-list implementation therefore takes `P exp(O(q))` time.
At a certificate exit it returns a totally dominating constellation
itself, so `D=V(K)` and `|D|<=2(|S|-1)`. This is a stronger
failure guarantee for every positive slack.

The self-contained operation, induced-star, and complexity argument
is in `independent_transversal_elementary_exponential_fallback.md`.
It is a derived public baseline, not an independent new result.
Thus the fair combined public bound is

\[
 P\min\left\{\exp(O(q)),\,
 (q+1)^{O((r/\epsilon)\log(2+r/\epsilon))}\right\}
 \operatorname{poly}(b_\epsilon+\log P).
\]

The current-blocker algorithm also takes the minimum with the same
fallback, replacing only the second exponent's outer `r/epsilon`
by `1/epsilon`. In particular, the arbitrary-graph comparison at
fixed slack is against an already available exponential-in-`q`
algorithm, not an artificially larger `q^{O(q log q)}` bound.

## 3. Stronger algorithms under different promises

The following results must not be omitted merely because they have a
different output contract.

| Primary source | Verified scope and guarantee | Relevance to the present comparison |
|---|---|---|
| Graf--Harris--Haxell, [1907.00033v8](https://arxiv.org/pdf/1907.00033), Theorem 5 and Corollary 6 | Randomized expected polynomial time for fixed positive slack, with block size at least `(2+slack) Delta`; also supplies a weighted IT guarantee for equal block sizes | Much faster than the candidate on this degree/block-size promise; does not state a full arbitrary-partition domination/constellation oracle |
| Harris, [1909.08065v6](https://arxiv.org/pdf/1909.08065), Theorem 1.5(1), Section 7 | **Deterministic** polynomial time for fixed positive slack and blocks of size at least `(2+slack) Delta`, including the weighted guarantee | The preceding special-case result must not be described as only randomized. Its derandomization does not furnish the general certificate contract |
| Chakraborti--Tran, [2402.02815v2](https://arxiv.org/abs/2402.02815) | Approximately packs ITs under a local-degree sparsity hypothesis and maximum degree below the common block size | A different structural promise and packing conclusion; not a comparison of uniform claw dependence in `FindITorBD` |
| Dai--Gan, [2610.28468v1](https://arxiv.org/abs/2610.28468), Theorem 1.1 | Packs almost all possible ITs in rank-at-least-three hypergraphs with average-degree and codegree hypotheses | A new October 2026 existence result for a different object and promise; not a full certifying algorithm for arbitrary partitioned graphs |

The weighted paper's latest arXiv version is v8 (21 August 2021).
Harris's latest version is v6 (1 February 2023; journal publication in
*Random Structures & Algorithms* 63(3), 716--752, 2023). Harris's
Theorem 1.5(2) also gives a parallel result under the stronger
`(4+slack) Delta` condition. Neither theorem treats a growing claw
parameter through the arbitrary-partition certifying interface above.

The deterministic degree/block-size method repeatedly restricts the
vertex set while preserving block sizes, degrees, and weight. Its
Section 7 reduction stops at a slack-dependent constant block size.
This reduction uses the degree/block-size hypothesis: arbitrary
induced sampling does not preserve the general no-small-domination
promise or automatically lift a failed sampled certificate to the
original graph. Therefore it cannot simply be inserted as a
black-box replacement for the full `FindITorBD` contract.

## 4. Search boundary and claims permitted by this audit

The primary sources above, the latest versions of the original
Graf--Haxell and weighted papers, their cited derandomization, and
recent 2024--October 2026 IT literature were checked. No verified
primary theorem located in this audit states the full domination plus
constellation contract with the candidate's logarithmic dependence on
`r`. This is a bounded literature-search finding, not proof of a
global priority or optimality claim.

The conclusion supported by the completed mathematical and source audits is:

> The current-blocker certificate sharpens the uniform quantitative
> bound obtained from the named Graf--Haxell construction, reducing the
> claw parameter's dependence in the class-count exponent from linear
> times logarithmic to logarithmic, while preserving the full
> domination/constellation alternative.

It is not a faster algorithm for unrestricted exact IT decision,
not an improvement over the deterministic polynomial algorithms on
their degree/block-size domain, and not a new general-graph maximum
matching bound. Its weak-Haxell specialization belongs to the same
mechanism as the already accepted direct hypergraph improvement.



---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
