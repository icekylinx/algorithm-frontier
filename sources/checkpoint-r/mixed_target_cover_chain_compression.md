# Covering-row chain compression for exact mixed numeric targets

**25 October 2026. Complete new reduction and proof; full root and independent internal reviews passed.**

This note replaces the `2^s` subset-copy ground used for `s` covering rows by a streamed enumeration of `s!` chains, each containing only `s+1` copies per original coordinate. The resource capacities, mandatory total, and one arbitrary scalar functional remain exact. The reduction permits a polynomial binary workspace bound even when the number of target rows is part of the input.

Companion manuscripts: `fixed_dimensional_mixed_numeric_targets.md` and its variable-dimensional continuation. This note proves the chain reduction and the profile-count interface independently; it does not assert publication priority.

## 1. Model and preprocessing

Let `F` be one normalized monotone integral polymatroid rank on an explicit ground `E`. The resource vector is integral and belongs either to `P(F)` or to `B(F)`. Rank values and counts are binary encoded. There are `d` rows with nonnegative integer coefficients `a^j_e`, nonnegative integer targets `T_j`, and independently chosen relations from `{<=, =, >=}`. The scalar functional `w x` is arbitrary rational and is to be minimized or maximized exactly.

Set

\[
T=\sum_{j=1}^d T_j.
\tag{CC1}
\]

An optional independent-vector problem can be represented by a base using one disposal coordinate with zero row and scalar coefficients. If the original rank is `R`, its lifted rank is `F(S)` for sets not containing disposal and `R` for sets containing it. Projection and completion by the missing total give an exact correspondence. An original mandatory base receives no such disposal coordinate.

From this point, keep the required original base total `R`. Remove zero-target covering rows. For every upper or equality row, mask coordinates with coefficient exceeding its target; a positive integer use of such a coordinate would be infeasible. Retain the original `R` after these masks and reject rank loss. A zero upper or equality target therefore leaves only zero coefficients in that row and can then be removed.

Let `C` be the remaining covering rows and `s=|C|`. Every one has positive integer target, so

\[
s\le T.
\tag{CC2}
\]

Let `F0` be the remaining rank on the eligible ground `E0`. Whenever preprocessing succeeds, `F0(E0)=R`. Its ground includes the legitimate disposal coordinate only in the optional model. All subsequent constructions use binary counts; conceptual individual resource units appear only in existence proofs.

## 2. One chain and its shared-copy rank

Enumerate every permutation

\[
\pi=(\pi_1,\ldots,\pi_s)
\tag{CC3}
\]

of the covering rows. For this permutation define the decreasing chain

\[
C_i=C\setminus\{\pi_1,\ldots,\pi_i\},
\qquad 0\le i\le s.
\tag{CC4}
\]

Thus `C_0=C` and `C_s` is empty. Create the coordinates `(e,i)` for `e in E0` and `0<=i<=s`. Let `pr` forget the second coordinate and define

\[
F_\pi^\uparrow(Y)=F0(\operatorname{pr}(Y)).
\tag{CC5}
\]

This is an integral polymatroid rank. If `x_e=sum_i z_(e,i)`, then

\[
z\in P(F_\pi^\uparrow)\iff x\in P(F0),
\qquad
z\in B(F_\pi^\uparrow)\iff x\in B(F0).
\tag{CC6}
\]

For the forward implication, query the full preimage of each original set. For the reverse implication, the sum on any copied set is bounded by the aggregate on its projection. The base equivalence follows by total mass. Projection preserves unions and maps intersections into intersections, which proves submodularity together with monotonicity of `F0`.

Every copy retains the original scalar coefficient `w_e`. Resource capacities are shared, and no original scalar contribution is discarded.

For an upper or equality row set `b^j_(e,i)=a^j_e`. For a covering row set

\[
b^j_{(e,i)}=
\begin{cases}
\min\{a^j_e,T_j\},&j\in C_i,\\
0,&j\notin C_i.
\end{cases}
\tag{CC7}
\]

The chain instance asks for the auxiliary row totals in the intervals

\[
\begin{array}{c|c}
\rho_j&\text{allowed auxiliary total}\\ \hline
\le&[0,T_j]\\
=&\{T_j\}\\
\ge&[T_j,2T_j-1].
\end{array}
\tag{CC8}
\]

All bounds and coefficients in this representation are integers.

## 3. Soundness of every chain

Take any lifted integer base satisfying CC8. Its projection is an original integer base by CC6. Upper and equality rows agree exactly with their original contributions. A covering row receives credit only from selected copies, and each credited coefficient is at most the original coefficient. Therefore the true covering total is at least the auxiliary total and hence at least its target.

The original scalar is unchanged, including when some scalar coefficients are negative. This proves soundness for every permutation without requiring that the recovered integer vector follow any chronological order of its units. The order is needed only for the completeness proof.

## 4. Completeness by one common order of units

Fix any feasible original integer base `x`. Conceptually list its `R` individual units in one arbitrary common order

\[
e_1,e_2,\ldots,e_R,
\tag{CC9}
\]

where coordinate `e` appears `x_e` times. No algorithm constructs this list.

For every remaining covering row `j`, let

\[
c_{jt}=\min\{a^j_{e_t},T_j\},
\qquad
\tau_j=\min\left\{u:\sum_{t=1}^u c_{jt}\ge T_j\right\}.
\tag{CC10}
\]

This first-reaching position exists. Indeed, if an original unit already has coefficient at least `T_j`, its capped contribution alone reaches the target; otherwise no coefficient changes under capping. In either case the full capped sum reaches `T_j`.

Mark the entire common-order prefix through position `tau_j` in row `j`. Zero-contribution units may be included in this prefix and do not affect the argument. The previous prefix has integer sum at most `T_j-1`, and the last contribution is at most `T_j`. Consequently

\[
T_j\le\sum_{t=1}^{\tau_j}c_{jt}\le2T_j-1.
\tag{CC11}
\]

Choose a permutation `pi` that sorts the positions `tau_j` nondecreasingly, breaking ties arbitrarily. For a unit in position `t`, put

\[
i(t)=|\{j\in C:\tau_j<t\}|.
\tag{CC12}
\]

The rows that mark this unit are exactly those with `tau_j>=t`, which form the chain suffix `C_(i(t))`. Assign the unit to copy `(e_t,i(t))`. Aggregating these assignments produces binary-encoded counts `z_(e,i)` with the same original projection `x`.

Tied stopping positions cause no difficulty. Their common last unit is marked in every tied row. All those rows disappear before the next unit, so intermediate chain layers have zero assigned units. A permutation may therefore describe a chain with empty layers. Zero original row entries are equally harmless: marking a unit with zero entry does not alter its row's credited sum.

By CC6, this is a lifted base. By CC11, every covering total has its required bounded value. All other rows and the scalar agree with their original values. Thus every feasible original integer vector, including every scalar optimum, appears in at least one enumerated chain with exactly the same scalar value.

Together with soundness, this proves exact equivalence after optimizing over all `s!` chains.

## 5. Exact profile subproblem and uniform binary space

Within one chain, group coordinates by their complete auxiliary coefficient vector. For each occupied nonzero vector `b`, guess its count `h_b`. Let `m=sum_b h_b`, reject `m>R`, and assign the one global zero-vector group count `R-m`.

Impose these counts as upper caps of a partition-count polymatroid. Its intersection with `Fup` is integral. On the total-`R` face every cap is tight because their prescribed sum is `R`. Exact scalar optimization on this face therefore returns an integer resource vector with the desired count profile, or proves this profile infeasible. If a positive zero remainder has no zero-vector coordinate, the face is simply empty.

For each surviving row let

\[
U_j=\begin{cases}
T_j,&\rho_j\in\{\le,=\},\\
2T_j-1,&\rho_j=\ge.
\end{cases}
\qquad
U=\sum_j U_j\le2T.
\tag{CC13}
\]

Rows with zero cap have already been removed after their masks. Enumerate nonzero profile counts by depth-first search, enforcing every component upper cap and the total count bound. The next count is bounded by the remaining rank and by `(U_j-W_j)/b_j` in every positive component. Lower and equality filters are applied at complete profiles.

Every partial profile has a zero completion satisfying these upper caps. Consequently all traversal nodes, including eventual row-filter and resource failures, are bounded by occupied depth times the number of complete upper-cap profiles.

For a fixed chain there are only `(s+1)|E0|` copied coordinates and at most that many occupied vector classes. This is polynomial in the full explicit input encoding even when `d` is variable. A permutation, its suffix masks, one profile, the component totals, and the exact intersection workspace all have polynomial binary size. Counters are bounded by the original binary rank or by binary target quantities. A next-permutation routine streams all chains without storing them simultaneously.

Therefore the complete algorithm uses polynomial binary workspace uniformly in the full input. Its running time is

\[
s!\;\mathcal P(U_1,\ldots,U_{d'})\;\operatorname{poly}(H),
\tag{CC14}
\]

where `mathcal P` counts nonzero vector profiles respecting the component upper caps; occupied-depth factors are absorbed in the polynomial. All oracle and exact-intersection costs are paid in that polynomial. No unit list, target-sized coefficient universe, or exponentially large subset-copy ground is stored.

For fixed dimension, applying the colored-partition estimate from MD recovers its target exponent. Applying its unequal-cap estimate gives the same anisotropic factor, multiplied by the constant `s!`. These are alternative bounds on the same profile traversal.

## 6. A dimension-free counting interface

The following elementary counting bound is useful when the number of rows is not fixed:

\[
\mathcal P(U_1,\ldots,U_{d'})
\le \operatorname{Bell}(U+1)
\le (U+1)^{U+1}.
\tag{CC15}
\]

For the first inequality, imagine `U_j` distinguished tokens of color `j`, together with one distinguished star. Order the nonzero vectors of a profile canonically, and order repeated copies arbitrarily by their occurrence number. For each vector occurrence `b`, form a block by taking the next `b_j` unused tokens of color `j` for every component. The cap constraints guarantee enough tokens. Each such block is nonempty because `b` is nonzero. Put all remaining tokens and the star into one final block.

This is a partition of `U+1` distinguished tokens. Decoding the color-count vectors of the blocks that do not contain the star recovers exactly the original profile. Thus two different profiles cannot produce the same partition. The star distinguishes unused capacity even when there is no unused token. The zero-vector resource group is not encoded separately: its count is fixed by the profile and the original rank.

For the second inequality, label the `U+1` tokens and map each token to the smallest label in its partition block. This map uniquely determines the partition and has at most `(U+1)^(U+1)` possible values.

The tokens are solely a counting device. In particular, CC15 does not require `U` workspace, and the implementation remains the occupied-class traversal from Section 5.

Using `s<=T` and `U<=2T` in CC14–CC15 gives the uniform consequence

\[
2^{O((T+1)\log(T+2))}\operatorname{poly}(H)
\tag{CC16}
\]

with polynomial binary space. When `T=0`, preprocessing leaves only the original base and scalar optimization, which is polynomial. The companion variable-dimensional theorem supplies the matching target-order oracle lower bound; this note's main purpose is the exact chain representation that makes the uniform workspace statement possible.

## 7. Scope

The construction retains arbitrary mixtures of nonnegative integer upper, equality, and covering rows and one exact scalar optimization. It retains all original mandatory resource mass and does not assume nonnegative scalar coefficients. Its `s!` factor is explicit; chain compression is a space improvement in variable dimension and does not improve the fixed-dimensional target exponent.

The result uses one resource polymatroid and an additional partition-count polymatroid per profile. It makes no analogous integrality claim for a third unrelated resource rank. Signed target coefficients, cancellation-based row representations, and a second unrelated scalar optimization under an extra side constraint require different arguments.
