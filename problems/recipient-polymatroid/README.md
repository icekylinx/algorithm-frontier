# Allocation with arbitrary recipient polymatroids

**Guarantee**

Returns at least $\mathrm{OPT}/d$ with $d=4-3/r$ against integer optimum. With a certified local factor-$\lambda$ availability oracle, use $d=\lambda^{-1}+3-3/r$. The equal-unit core also returns $\lceil K/3\rceil$ units from a full quota-$K$ promise.

**Objective and output**

Select an actual player basis and legal integral recipient counts, maximizing common intrinsic value.

**Randomness**

Deterministic current-blocker search with paid exact primitives. A supplied factor-lambda availability oracle must satisfy its certified guarantee on every call.

**Time**

Factor $d$ and the equal-unit core take $2^{O(r)}\mathrm{poly}(H)$. Factor $d+\eta$ takes $\mathrm{poly}(H)\min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}$.

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units.

**Parameters**

$r\ge1$ is the player-matroid rank; $\eta>0$ is rational; optional $0<\lambda\le1$ is a certified local-oracle guarantee. $H$ includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

Common intrinsic values, arbitrary normalized monotone integral submodular recipient ranks, binary counts, and an arbitrary selected player basis. Optional local families are type-symmetric and downward closed. No assignment budget is added by this theorem.

**Lower-bound scope**

The [hidden-rank oracle barrier](../allocation-lower-bounds/proof.md) excludes deterministic factor strictly below two in rank-FPT oracle time. The [configuration gap](../allocation-lower-bounds/configuration-gaps.md) prevents replacing integer $\mathrm{OPT}$ by the simple aggregate configuration LP.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The [representation lemmas](representation.md) prove the compressed natural-matroid implementation, exact residual availability, distinct record bookkeeping, and the integer-comparator loss bound. A uniform near-three quasipolynomial equal-unit guarantee is not claimed at small quotas.

## Stronger comparators and fractional optimization

The aggregate configuration LP and the residual-capacity relaxation are
different comparators. Adding all stated residual cuts gives the following
additional results.

**[Residual-capacity comparator](../../manuscripts/allocation-and-scheduling/recipient-polymatroid-residual-configuration-relaxation.md)**

**Guarantee and cost.** Factor $4-3/r$ in $2^{O(r)}\mathrm{poly}(H)$ with exact local availability; factor $\lambda^{-1}+3-3/r$ with certified availability $\lambda$

**Scope.** Arbitrary recipient polymatroids; the allocation algorithm uses the LP as a comparator without solving it

**[Scaled recipient-matroid types](../../manuscripts/allocation-and-scheduling/scaled-recipient-matroids-binary-configuration-transfer.md)**

**Guarantee and cost.** The same approximation against the component configuration LP

**Scope.** Each supplied type has rank $f_j=c_jr_{R_j}$ with binary multiplicity; component constraints are retained

**[Fractional weak optimizer](../../manuscripts/allocation-and-scheduling/residual-configuration-bounded-support-xp-solver.md)**

**Guarantee and cost.** Target at least $(1-\epsilon)\mathrm{OPT}_{\rm LP}$ in $(q+1)^{O(s+1)}\mathrm{poly}(H,\epsilon^{-1})$ for support-$s$ cuts; the full LP takes $2^{O(q)}\mathrm{poly}(H,\epsilon^{-1})$

**Scope.** Coordinate-box local families; $s=2(r-1)$ is an XP rank bound, and the output is fractional

The residual-cut proof also transfers the exact integer-quota comparator.
It preserves the critical small-quota growth boundary and does not give a
new uniform quasipolynomial factor-three theorem.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
