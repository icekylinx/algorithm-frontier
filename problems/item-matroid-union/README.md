# Explicit-item allocation on a selected matroid basis

**Guarantee**

Returns value at least $T_{\mathrm{conf}}/(4-3/r)$ against the player-matroid configuration LP, hence also against integer optimum. An alternative gives factor $4-3/r+\eta$.

**Objective and output**

Select an actual player-matroid basis and disjoint liked-item bundles with large minimum intrinsic value.

**Randomness**

Deterministic matroid-union reduction and current-blocker search, including both the exact rank-dependent factor and the relaxed quasipolynomial variant.

**Time**

Factor $d=4-3/r$ takes $2^{O(r)}\mathrm{poly}(H)$. Factor $d+\eta$ takes $\mathrm{poly}(H)\min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}$.

**Space**

Polynomial in the explicit item and liking-incidence input, rational encodings, and paid matroid workspace.

**Parameters**

$r\ge1$ is the player-matroid rank; $\eta>0$ is rational; $T_{\mathrm{conf}}$ is the configuration optimum. All matroid-union and original-oracle costs are paid in $H$.

**Model and representation**

Explicit indivisible items with intrinsic values and explicit liking incidences; an arbitrary player matroid. Configurations and an LP solution are not supplied or enumerated.

**Lower-bound scope**

No lower bound is claimed for this algorithm.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The [configuration-comparator proof](configuration-comparator.md) establishes the stronger comparator without changing the algorithm. Rank one is exact. The factor tends to four as rank grows; no fixed improvement below four for all ranks is asserted.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
