# Verification note

**Curated source path:** `sources/checkpoint-q/fully_dynamic_spanner_independent_audit.md`

The source audit follows.

# Independent audit of the full-horizon spanner transfer

**25 October 2026. Verdict: the batching assembly in
`fully_dynamic_spanner_five_sixths.md`, Sections 1--6, passes this audit,
conditional on its named numerical-provider imports.**

The public source is KMZ's published
[ICALP 2025 paper, Section 5](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.111/LIPIcs.ICALP.2025.111.html).
The checked assembly gives explicit integer clocks and inventory
accounting instead of relying on the abbreviated published indexing.
Its guarantee is amortized. This audit does not make it a worst-case
dynamic spanner.

## 1. Single-instance facts

For congestion threshold `K`, path cap `R`, `F` input insertions
including seeding, and `D0` input deletions, each deletion breaks at
most `K` currently stored routes. An edge of the output spanner has
its own identity route, so another already selected spanner edge
cannot be among the affected nontrivial rerouting requests.

Every saturated eligible edge is permanently ineligible for its
physical lifetime. Its load can decrease later, but never increase
after that retirement. Thus a blocked lifetime can be charged `K`
distinct installed route incidences, even when some earlier incidences
were subsequently removed. This proves the two first counts in (F2).

The eligible graph always has girth above the stated threshold: an
insertion occurs only when the true endpoint distance exceeds that
threshold, and every other eligible-graph change is a deletion. Its
size is `O(n)`. The full spanner consists of this graph and the
blocked lifetimes, and loses physical edges only upon input deletions.
Its total insertion count is therefore its maximum size plus at most
`D0`. The last line of (F2) correctly includes this term through
`R D0`.

The numerical oracle is updated on the eligible graph, not on the
dense instance input. Both initial vertex handles and every installed
route incidence are paid in (F3). Destroying a retired instance does
not introduce an extra dense initialization multiplier: its current
records are a subset of the records previously created and paid.

## 2. Why the nested deletion clocks are sufficient

The clocks are `t_i=n K^(s-i)`, so `t_(i-1)=K t_i`. A replacement
of any ancestor coincides with a replacement of all its descendants.
During one live instance of layer `i`, no ancestor is internally
replaced. Every removal from its parent input therefore traces to an
original external physical deletion. Saturation changes only the
parent's eligible graph and does not remove an edge from the parent's
output spanner.

Hence one live layer-`i` instance sees at most `t_i` input deletions;
over all its instances it sees at most `D`. Artificial destruction
deletions are not forwarded into replacement instances. This is
consistent with the settled-update interface: old internal structures
are retired, replacements are seeded from current parents, and only
the final output is published.

These facts also prove the exact initialization count

\[
 n(1+\lfloor D/t_i\rfloor)\le n+D,
\]

since every `t_i>=n`. The special case `s=1`, including `M<=n`,
has the same property. The ceiling in `s` only inflates a numerical
clock capacity; it does not allocate unused vertices or edges.

## 3. The current-size induction has no insertion-count assumption

For any chronological prefix of one live instance, let `F_life`
include its seed. Because the parent is not replaced in this interval,

\[
 F_{life}=|E(\text{current parent})|
                   +\#\text{parent deletions in the interval}.
\]

Thus (F6), `F_life<=V_(i-1)+t_i`, follows exactly. There is no
missing initial-size term and no assumption that insertions are
bounded by deletions. Applying the single-instance count gives the
claimed `V_i=(c0 R)^i M'/K^i`. This induction applies while actual
seed edges are being inserted as well as after subsequent updates.

## 4. Total work: check of (F9)--(F13)

Let `I*=m0+I`. At level 1 the first seed is counted by `m0`, while
each later seed of at most `M` edges is charged to a completed `t1`
deletion interval. Hence

\[
                     F_1\le I_*+DK.
\]

At level `i+1`, ordinary insertions are included in the parent's
total output insertion count `O_i`. The first seed is already covered
by the parent's initial output insertions. Every later seed costs at
most `V_i` and is charged to one of the `floor(D/t_(i+1))`
replacement boundaries. Therefore

\[
 F_{i+1}\le O_i+DK(c_0R)^i,
 \qquad O_i\le c[n+D+(R/K)F_i+RD].
\]

Simultaneous ancestor replacements may make this accounting charge
an edge twice, which is safe. They do not make it omit a seed. An
absolute enlargement of `c1` now gives

\[
 F_i\le(c_1R)^i(I_*+n+DK).
\]

The route-query term contributes `R(F_i+K D)`; the oracle update
term contributes `alpha[n+D+(R/K)F_i+RD]`. Summing over levels
is bounded by (F13). The `K` factor multiplying total deletions is
paid once, and the first initialization remains `m0`, rather than
the potentially much larger upper capacity `M`.

This also confirms the distinction from rebuilding a dense graph
after each `n` original deletions. That strategy would pay a density
factor; the nested construction charges different rebuilding levels
to appropriately separated clocks.

## 5. Output IDs, size, recourse, and weights

Each layer chooses only current physical input edges. Their identities
are preserved through all layers; inner binary-port edges are private
representations and are never output edges. Parallel input identities
are legal. Two parallel edges cannot both enter the current eligible
graph, because the later edge would already have an eligible route
of length one.

The last layer has clock exactly `n`. Between its replacements,
its ordinary insertions are at most its maximum size plus its physical
deletions. At a replacement, charging the union of the old and new
output sets bounds the published changes. This proves (F14),

\[
                 \operatorname{recourse}
                    \le(n+D)(c_3R)^s.
\]

Stretch multiplies across the `s` subgraph layers, and size is bounded
by (F7). Running the hierarchy independently in dyadic length classes
adds a polynomial logarithmic factor and a factor two to stretch.
Every clipping query then remains unweighted; there is no numerical
edge-length factor in route enumeration.

## 6. The new balanced point

The conservative numerical family imported by the assembly is

\[
 B=O(U/t+t^5h),\qquad A=O(t^4h).
\]

No normalized-repair improvement is needed for this substitution.
Set `t=Theta((U/h)^(1/6))`, `z=Theta(U/t)`, and `K=2^ceil(z)`.
Then `s=O(t)`, and all of `B`, `z`, and `s(A+h)` are
`O(U^(5/6) h^(1/6))`. The logarithms of all maintained integer
clocks and of all actual record counts are polynomial in `U`.
The ratio between the inner shrink and recourse has slack, so small
instances can terminate at their actual-size base without padding.

Together with Sections 1--5, this yields the claimed simultaneous
stretch, size, total-time, and total-recourse envelope in (F1).
The source/provider dependencies remain research assumptions as
classified in the companion notes; the new outer assembly itself has
no unresolved initialization or lifetime-counting gap found here.

## 7. Optimizing the public comparison, including a matched stretch

The public joint reconstruction has the one-parameter family

\[
 B_{pub}=O(U/t+t^6h),\qquad A_{pub}=O(t^5h).
\]

Taking `z=Theta(U/t)` in the same batching wrapper makes final
stretch/density log at most `O(t^6h)`, while its time log is at most
`O(U/t+t^6h)`. Thus the balanced public point is `6/7`, but this
is not the only fair comparison.

To match the new final stretch and density envelope
`S=U^(5/6)h^(1/6)`, choose

\[
 t=\Theta((U/h)^{5/36}),\qquad z=\Theta(U/t).
\]

Then the public time log is

\[
                     O(U^{31/36}h^{5/36}),              \tag{5}
\]

and its final stretch, density, and recourse logs are all `O(S)`.
This is an accepted upper-bound substitution into the same proved
outer wrapper. It is a derived public comparison, not a printed
theorem with those exponents.

There is also a useful positive-budget check, distinct from an
algorithmic lower bound. The public envelope already proved in
`same_stretch_apsp_comparison_and_root_audit.md`, Section 6, has

\[
 B^7\ge\Omega(U^6h),\qquad
             A_{charge}\ge\Omega(U^5h/B^5).
\]

In the dense-cap regime `log(M/n)=Theta(U)`, if the outer total time
charge is `Z`, its shrink logarithm is at most `Z`, so it needs
`Omega(U/Z)` layers. Every such numerical oracle still has `n`
vertex handles and the same order of master logarithm. Thus the
declared additive outer stretch charge is at least
`Omega(U^6h/Z^6)`. A declared final stretch budget `S` imposes

\[
 Z\ge\Omega\left(
       \max\{U^{6/7}h^{1/7},\ U(h/S)^{1/6}\}\right).    \tag{6}
\]

Nonuniform positive charges at different outer levels give the same
conclusion: each level has time at most `Z`, and the number of levels
required to cover the density logarithm is at least `Omega(U/Z)`.
Equation (5) matches (6) at the stated stretch scale. These are
obstructions for the **charged constructive envelope**. They do not
prove a lower bound on actual stretch, or rule out a different public
construction with more favorable accounting.

## 8. The elementary keep-the-input baseline must also be used

Suppose a promised current edge cap satisfies `M<=n Dens`, where
`n Dens` is the allowed output-size bound. Keeping `H=G` gives
stretch one and constant per-update graph maintenance. Since

\[
 m_0+I=|E(G_{final})|+D\le M+D,
\]

its total output recourse is at most `M+2D`, hence
`O((n+D)Dens)`. In this sparse-cap regime no dynamic sparsification
is required to obtain the allowed size and recourse.

Accordingly, the full-horizon theorem has nontrivial content for
general graphs whose current density can exceed its allowed output
overhead; polynomial density is an example. The same point matters
for the deletion-bounded comparison. With stretch/size log
`a=U^(5/7)h^(2/7)`, taking `m=Theta(n)` merely compares two
loose formulas on a problem already solved by keeping the input.
An illustrative nontrivial density window is instead
`m/n=exp(Theta(U^(3/4)))`, with at most `n` deletions. The input
then exceeds the common size cap, while the shared insertion term
is smaller than both declared APSP-maintenance terms. No global
optimality claim is inferred from this example.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
