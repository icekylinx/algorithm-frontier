# Allocation with arbitrary recipient polymatroids

**Guarantee**

Returns at least <code class="math">\mathrm{OPT}/d</code> with <code class="math">d=4-3/r</code> against integer optimum. With a certified local factor-<code class="math">\lambda</code> availability oracle, use <code class="math">d=\lambda^{-1}+3-3/r</code>. The equal-unit core also returns <code class="math">\lceil K/3\rceil</code> units from a full quota-<code class="math">K</code> promise.

**Objective and output**

Select an actual player basis and legal integral recipient counts, maximizing common intrinsic value.

**Randomness**

Deterministic current-blocker search with paid exact primitives. A supplied factor-`lambda` availability oracle must satisfy its certified guarantee on every call.

**Time**

Factor <code class="math">d</code> and the equal-unit core take

<!-- math-display: f53c232e9b6631d4d9719b29
2^{O(r)}\mathrm{poly}(H)
-->
![Formula](../../assets/math/f53c232e9b6631d4d9719b29.svg)

Factor <code class="math">d+\eta</code> takes

<!-- math-display: 8ced10ea45fea6f141e8d448
\mathrm{poly}(H)\min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}
-->
![Formula](../../assets/math/8ced10ea45fea6f141e8d448.svg)

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units.

**Parameters**

<code class="math">r\ge1</code> is the player-matroid rank; <code class="math">\eta&gt;0</code> is rational; optional <code class="math">0&lt;\lambda\le1</code> is a certified local-oracle guarantee. <code class="math">H</code> includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

Common intrinsic values, arbitrary normalized monotone integral submodular recipient ranks, binary counts, and an arbitrary selected player basis. Optional local families are type-symmetric and downward closed. No assignment budget is added by this theorem.

**Lower-bound scope**

The [hidden-rank oracle barrier](../allocation-lower-bounds/proof.md) excludes deterministic factor strictly below two in rank-FPT oracle time. The [configuration gap](../allocation-lower-bounds/configuration-gaps.md) prevents replacing integer <code class="math">\mathrm{OPT}</code> by the simple aggregate configuration LP.

**Review status**

**Ready for review in the stated scope.** The complete canonical main integer-comparator theorem and binary representation: natural ranks, whole-owner contraction and availability, original-box integral comparator recovery, distinct-record realization, large-unit dual-union completion, ordered-prefix block additivity, current strong release and atomic earliest exchange, present rank charging, integer lower cover, exact and positive-slack signatures and target search, and the equal-unit rank-exponential endpoint. The native backend realizes count, availability, recovery and minimality interfaces.

**Dependencies and scope.** The mathematical theorem pays for exact rank/SFM, integral intersection and decomposition, and the supplied certified local-availability oracle. Binary multiplicities remain numerical. The native reference uses complete rank tables and explicit subset enumeration with separate bit costs. The residual-capacity and scaled-copy fractional comparators, bounded-support fractional optimizer and full weak fractional optimizer remain outside this review. Full player-layer software, selected-basis recovery and arbitrary local-availability oracle implementations are not supplied by the count backend. Independent finite original-input checks and mathematical interface proofs do not assert external peer review or proof-assistant verification.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The [representation lemmas](representation.md) prove the compressed natural-matroid implementation, exact residual availability, distinct record bookkeeping, and the integer-comparator loss bound. A uniform near-three quasipolynomial equal-unit guarantee is not claimed at small quotas.

## Stronger comparators and fractional optimization

The aggregate configuration LP and the residual-capacity relaxation are
different comparators. Adding all stated residual cuts gives the following
additional results.

**[Residual-capacity comparator](../../manuscripts/allocation-and-scheduling/recipient-polymatroid-residual-configuration-relaxation.md)**

**Guarantee and cost.** Factor <code class="math">4-3/r</code> in <code class="math">2^{O(r)}\mathrm{poly}(H)</code> with exact local availability; factor <code class="math">\lambda^{-1}+3-3/r</code> with certified availability <code class="math">\lambda</code>

**Scope.** Arbitrary recipient polymatroids; the allocation algorithm uses the LP as a comparator without solving it

**[Scaled recipient-matroid types](../../manuscripts/allocation-and-scheduling/scaled-recipient-matroids-binary-configuration-transfer.md)**

**Guarantee and cost.** The same approximation against the component configuration LP

**Scope.** Each supplied type has rank <code class="math">f_j=c_jr_{R_j}</code> with binary multiplicity; component constraints are retained

**[Fractional weak optimizer](../../manuscripts/allocation-and-scheduling/residual-configuration-bounded-support-xp-solver.md)**

**Guarantee and cost.** Target at least <code class="math">(1-\epsilon)\mathrm{OPT}_{\rm LP}</code> in <code class="math">(q+1)^{O(s+1)}\mathrm{poly}(H,\epsilon^{-1})</code> for support-<code class="math">s</code> cuts; the full LP takes <code class="math">2^{O(q)}\mathrm{poly}(H,\epsilon^{-1})</code>

**Scope.** Coordinate-box local families; <code class="math">s=2(r-1)</code> is an XP rank bound, and the output is fractional

The residual-cut proof also transfers the exact integer-quota comparator.
It preserves the critical small-quota growth boundary and does not give a
new uniform quasipolynomial factor-three theorem.

The [binary-count backend](reference/README.md) implements natural ranks, residual availability and integral comparator recovery with explicit-table costs; its [proof](reference-realization.md) and [independent checks](verify/README.md) separate those interfaces from the full allocation theorem.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
