# Matroid allocation: public comparison, version history, and a gated parameter optimization

**Primary-source audit, 25 October 2026.** This note is the comparison
companion to [matroid-allocation-current-blocker-quasipolynomial.md](matroid-allocation-current-blocker-quasipolynomial.md).
It separates three different statements: a theorem displayed in the
latest public manuscript, an earlier numerical claim that the authors
subsequently revised, and a new parameter calculation whose full
algorithmic interface has not been closed in this audit.

The initial accepted new construction has value

$$
(T-u)/3-\varepsilon T,
 \qquad u=\max_jv_j,
$$

for the player-basis relaxation `Q(T)`, with quasipolynomial running
time for fixed positive epsilon. The coefficient one third is not a
new numerical claim in the historical literature. The contribution
being checked is a fully specified current-blocker construction and
proof, including an explicit fractional-infeasibility alternative.

The subsequent audited refinement is recorded in
[matroid-allocation-sharp-star-rank-quality.md](matroid-allocation-sharp-star-rank-quality.md). If the player matroid
has rank r, write rho=(r-1)/r and

$$
C(B,u)=\max\{u,2B+\min(u,B)\}.
$$

Every positive B satisfying `B+rho C(B,u)<=T` is attained in
`mathcal P 2^{O(r)} poly(b+log mathcal P)` time, with an explicit
infeasibility alternative. Subtracting epsilon T from the largest
such B gives the minimum of this bound and the rank-quasipolynomial
bound. This statement includes the exact additive one-third boundary,
and improves it for finite rank and for certain larger-item ranges.
Its independent audit is
[Matroid union removes the largest-item penalty](../../problems/item-matroid-union/proof.md).

## 1. The exact public model

In Davies--Rothvoss--Zhang (DRZ), a matroid is given on the player set.
One must select a basis and give those players disjoint sets of liked
resources. Resource values are player-independent. The relaxation is

$$
x\in P_{\mathcal B(\mathcal M)},\qquad
 \sum_j v_j y_{pj}\ge Tx_p,\qquad
 \sum_p y_{pj}\le1,\qquad 0\le y_{pj}\le x_p.
 \tag{1}
$$

This is exactly the model of the new construction. The condition
`y_pj<=x_p` is used in its infeasibility proof. A guarantee against the
integral optimum of a broader allocation model does not automatically
imply a rounding or infeasibility theorem for (1).

Primary source: [DRZ v4, equation (1), Theorem 2, and Section 3](https://arxiv.org/html/1807.07189v4).

## 2. Version history: the largest-item coefficient matters

The dates below are from the [arXiv submission history](https://arxiv.org/abs/1807.07189).
Each row records the theorem stated in that version; it does not
independently certify every proof in a superseded version.

| Version | Displayed matroid guarantee from `Q(T)` | Ordinary restricted Santa Claus claim |
|---|---|---|
| [v1, 19 July 2018](https://arxiv.org/pdf/1807.07189v1), Theorems 2--5 | Theorem 2 makes `x` integral at `(1/3-epsilon)T` while permitting fractional `y`; Theorem 3 makes both integral at `(1/3-epsilon)T-u`. Theorem 5 treats unit resources separately. | `6+epsilon` |
| [v2, 7 May 2019](https://arxiv.org/pdf/1807.07189v2), Theorems 2--3 | Both integral at `(1/3-epsilon)T-u/3`. | `4+epsilon` |
| [v3, 27 July 2025](https://arxiv.org/html/1807.07189v3), Theorems 2--3 | Both integral at `(1/5-epsilon)T-u/5`. | `6+epsilon` |
| [v4, 4 January 2026](https://arxiv.org/html/1807.07189v4), Theorems 2--3 | Both integral at `(1/5-epsilon)T-u/5`. | `6+epsilon` |

All the displayed algorithms are stated as polynomial for a fixed
positive approximation slack, under polynomial-time independence
queries. The present new construction has a different running-time
tradeoff and is not a polynomial-time improvement over the latest
displayed theorem.

The SODA 2020 abstract and the corresponding chapter of
[Sami Davies's 2021 dissertation](https://digital.lib.washington.edu/researchworks/items/f2a80a99-1858-4670-9e0d-4857b24419e1)
belong to the earlier factor-four/one-third history. They should not
be counted as an additional current result independent of the version
revision. In particular, the dissertation is dated 2021, not a new
2025 or 2026 development.

DRZ v4 Section 4 identifies the authors' correction: a blocking-layer
growth inequality had been justified when a layer was born, but need
not survive later collapses. The revised procedure checks available
resources in existing layers, at the cost of a weaker stated
approximation. This audit does not infer any further reason for the
revision. It also does not silently preserve the old unit-resource
polynomial claim as an independently proved contemporary baseline:
the v1 growth argument uses the same birth-versus-current distinction.

## 3. A stronger symbolic parameter curve: algebra passes, interface pending

This section records a useful possible public-framework strengthening.
**It is not promoted to an algorithmic theorem.** The obstacle is in
Section 4, and is separate from the following exact calculations.

Normalize `delta=u/T`. Write the free parameters in DRZ Lemmas 8--12
as `alpha`, `beta`, and `kappa`, with

$$
\begin{split}
 \mu&=\frac{1-\alpha-\delta-(\alpha+\delta)
                    (\beta/(\alpha-\beta)+\kappa)}{1+\delta},\\
 \phi&=\frac{\alpha-\beta}{\alpha+\delta},\\
 c_{\rm grow}&=\frac{(\alpha-\beta)\mu}
                    {\beta+\delta+\kappa(\alpha-\beta)}.
 \end{split}
 \tag{2}
$$

For `0<=delta<1` and `0<eta<(1-delta)^2/4`, set

$$
\alpha=\frac{1-\delta}{2},\qquad
 \beta=\alpha^2-\eta,\qquad
 d=\alpha-\beta,\qquad
 \kappa=\frac{\eta}{2d(1-\alpha)}.
 \tag{3}
$$

Substitution gives

$$
\mu=\frac{\eta}{2d(1+\delta)}=\frac\kappa2,
 \qquad
 \phi=\frac d{1-\alpha},
 \qquad
 c_{\rm grow}=\frac{2\eta}{(1+\delta)^3-4\delta\eta}.
 \tag{4}
$$

All three are positive. For example, the domain implies
`mu>=eta`, `kappa>=2eta`, `phi>=alpha>sqrt(eta)`, and
`eta/4<=c_grow<1/2`. Thus no new vanishing parameter appears when
eta is fixed, even if delta varies within its allowed interval.

There is a second, elementary constant adjustment needed for a
literal use of the source's layer-concentration lemma. Its direct
free-edge branch supplies a swappable fraction `phi mu`; its inner
collapse branch supplies `kappa c_grow`. These need not be as large
as `c_grow` itself. A safe common parameter is

$$
c_* =\min\{c_{\rm grow},\phi\mu,\kappa c_{\rm grow},1/4\},
 \qquad
 \gamma=\frac{1}{2\bigl(\lceil\log(2/c_*)/
                                  \log(1+c_*)\rceil+1\bigr)}.
 \tag{5}
$$

The same concentration proof then has both its required growth and
fraction hypotheses. Conservatively, `c_*=Omega(eta^2)` and gamma
is a fixed positive function of eta. The corresponding shrink
fractions are positive functions of eta. This calculation supports
polynomial time for fixed eta **if** the historical exchange interface
is supplied correctly.

The resulting candidate value would be

$$
\left(\frac{(1-u/T)^2}{4}-\eta\right)T.
 \tag{6}
$$

In the limit of negligible largest resource it approaches `T/4`,
instead of the displayed `T/5`. At zero slack, it exceeds the
displayed one-fifth curve when `u/T<1/5`. It remains below the
new one-third curve for every `0<=u/T<1`.

Even the default source parameters should not be treated as an
independently checked all-delta proof simply by substitution: when
the source slack tends to zero, its displayed expression for mu
is positive only below `delta=1/6`. The source itself states some
uniform estimates in this restricted range. We preserve its Theorem
2 as a **displayed public theorem**, rather than asserting that this
audit has filled every parameter-domain detail of its proof.

## 4. The literal historical-exchange contract still needs clarification

The following is a specific interface question, not a declaration
that the public theorem is false. An additional selection rule,
historical invariant, or repair could conceivably resolve it. None
was identified in the source formulas checked for this parameter
transfer.

Algorithm 1 asks a new family `H` to be disjoint on resources from
all retained adding and blocking edges. It does not explicitly forbid
an owner in `H_X` from also owning an older retained adding edge.
After a swap, Algorithm 2 is applied again to old adding edges that
now have enough free resources. Its set-exchange premise must then
still imply a matching with distinct owners and the same rank.

A small stress test makes the missing obligation concrete. Use a
uniform rank-two matroid, independent set `S={s0,y}`, and matching
`M={M_y}`. Suppose the first retained adding layer consists of a
bundle owned by an outside player `p`, blocked by `M_y`.
A later free candidate can also be owned by `p`, while using
different resources. The printed choice conditions allow it to
replace `y`, retaining the earlier adding layer. Now

$$
S=\{s_0,p\},\qquad M=\{\text{new bundle of }p\},
 \qquad B_1=\varnothing,
$$

and the old adding bundle of `p` has become free. Applying Algorithm
2 to this old layer can select `C'={s0}` and `D'={p}`. The printed
conditions `|C'|=|D'|` and `S\C' union D'` independent hold as set
statements, but do not preserve cardinality: `p` was already in
`S\C'`. Adding the old bundle to `M` gives two bundles with the same
owner, not the required hypergraph matching.

This is also realizable at ordinary positive source parameters.
Take `T=1`, `delta=0.1`, source slack `0.01`, so
`alpha=0.355` and `beta=0.17`. Let `M_y` consist of two resources
of value `0.1`. The first adding bundle of `p` consists of these two
resources and resources of value `0.09` and `0.07`: it is minimal
for alpha and has free value `0.16<beta`. A later bundle of `p`
can use four new resources of value `0.09`, be minimal for alpha,
and avoid all old resources. Each chosen singleton family meets
the source's positive expansion-size requirement in this rank-two
example. Extra private resources can make `Q(1)` feasible without
changing these choices.

The immediate missing condition is disjointness of incoming owners
from retained matched owners, except those actually exchanged out.
More generally, one must establish the joint exchange eligibility of
every retained older candidate family after each intermediate swap.
Simply removing repeated-owner candidates would also require new
growth and resource accounting; it is not a free parameter change.

The new current-blocker construction avoids this particular problem
by using individual eligibility, a separate `p in I` case, and an
earliest-fundamental-circuit exchange rule. That rule preserves the
spans determining every retained lower layer, while higher layers
are discarded. This is part of its independently checked proof,
not an imported invariant from Algorithm 2.

Until this public interface question is settled, (6) is an **audited
algebraic candidate**, not a closed derived-public baseline.
The complete independent source-interface stress test, including an
execution from the preceding initialization phase, is recorded in
[public-matroid-repeated-owner-interface-gap.md](../mechanism-boundaries/public-matroid-repeated-owner-interface-gap.md).

## 5. Broader resource-matroid allocation is related but has a different comparator

[Bamas--Lindermayr--Megow--Rohwedder--Schloeter,
arXiv:2307.08453v1](https://arxiv.org/abs/2307.08453), Section 1 and
Theorem 4, permit each resource to be allocated to a basis of its own
resource-specific matroid or polymatroid. Their displayed polynomial
guarantees are `8+epsilon` in the general restricted setting and
`4+epsilon` for two values.

This model does contain the player-basis problem. Add one sufficiently
large resource whose matroid is the dual of the player matroid;
the players not served by that resource must form a basis of the
original matroid and receive ordinary small resources. Thus it would
be incorrect to dismiss the paper as a disjoint model.

The displayed approximation theorem, however, compares against the
integral allocation optimum. It does not, just from its headline,
give an allocation of `(T-u)/3-epsilon T` whenever the specific LP
(1) is feasible, nor the new algorithm's explicit certificate for
infeasibility of that LP. Their Section 4 provides a richer
polymatroid local-search and infeasibility framework; no stronger
matching guarantee for the precise interface (1) was verified in
this bounded source audit. The introduction's reference to DRZ's
factor four predates DRZ v3/v4 and must be read with that version
qualification.

Results imposing matroids on the **items received by each player**,
or assuming one identical valuation for all players, also require a
separate reduction. They are not interchangeable with a matroid on
the set of players selected for service.

There is a further elementary special-case comparison. BLMRS
Appendix E, Theorem 21, rounds a feasible assignment LP for a fixed
set of all players to value at least `T-u` in polynomial time, even
in its resource-polymatroid setting. Therefore when the player
matroid is free and every player is compulsory, the small-resource
LP alone already has a stronger rounding guarantee than the new
general-basis star formula. The new theorem's scope is the arbitrary
matroid choice of the served basis; it is not a new best statement
for that fixed-player LP special case.

### 5.1 Additional parameterized and 2026 primary-source checks

There are already strong parameterized approximation results for
ordinary Santa Claus. [Jansen--Maack, arXiv:1701.03263v2,
Theorem 1 and Section 4](https://arxiv.org/pdf/1701.03263v2)
give an approximation scheme with parameter the number K of player
valuation types, with time

$$
2^{O(K\log(2+K)\,\zeta^{-1}\log^4(2+1/\zeta))}
       +\mathrm{poly}(|I|).
$$

In particular, K is at most the total number of players. This also
explains the parameterized approximation scheme noted by Grandoni in
[Dagstuhl Seminar 23291, Section 5.3](https://drops.dagstuhl.de/storage/04dagstuhl-reports/volume13/issue07/23291/DagRep.13.7.96/DagRep.13.7.96.pdf).
Our new parameter is instead the rank r of a matroid on potentially
many more eligible players q. The algorithm must choose the served
basis while respecting that oracle matroid. Enumerating all r-player
subsets and invoking an ordinary allocation scheme would cost a power
of q depending on r, rather than a rank-only parameter factor.
Moreover, the ordinary approximation scheme has an integral-optimum
comparator, not the fractional guarantee (1).

Two recent nearby results were also checked directly:

| Primary source | Actual scope | Why the stated result does not supply the same interface |
|---|---|---|
| [Boehmer, SWAT 2026, Theorems 1.1 and 1.5](https://drops.dagstuhl.de/storage/00lipics/lipics-vol370-swat2026/html/LIPIcs.SWAT.2026.8/LIPIcs.SWAT.2026.8.html) | A `2/5` algorithm for identical submodular valuations; separate configuration-LP gap bounds with matroids on each allocated item set. | The players have a common valuation, and the matroids constrain items, rather than selecting a basis of players with arbitrary liking sets. The gap theorem is not a construction of the claimed allocation. |
| [Berczi--Liu--Reis--Tarnawski, arXiv:2608.13983v1, Theorem 1 and Sections 4--5](https://arxiv.org/html/2608.13983v1) | Weighted partitions into matroid bases, identical-valued fair division, and degree-bounded rounding with additive discrepancy depending on column sparsity. | It does not state the player-basis allocation theorem (1); the discrepancy guarantee cannot be substituted for that theorem without an additional reduction and its error bound. |

This extended search found no independently closed source covering
the new rank-parameterized guarantee
`mathcal P 2^{O(r)}` at the exact additive boundary `(T-u)/3`, or
the positive-slack rank-quasipolynomial bound. This is the result of
a bounded primary-source check, not a universal novelty assertion.
The older DRZ one-third statements remain part of the comparison
in Section 2.

## 6. Ordinary Santa Claus: the adapter returns to a known factor

The large-resource transversal-matroid reduction in DRZ Section 3
does apply to the new theorem. If resources at most `theta T` are
small, its two allocation alternatives have value at least

$$
\min\{\theta,(1-\theta)/3-\varepsilon\}T.
 \tag{7}
$$

Setting `theta=(1-3epsilon)/4` gives `(1-3epsilon)T/4`.
The proof that the compact Santa Claus LP induces (1) for the dual
transversal matroid is recorded in Section 8 of
[Current blocker growth for matroid max-min allocation](matroid-allocation-current-blocker-quasipolynomial.md).

This is not a below-four result, and not an improvement over the
polynomial `4+delta` allocation algorithm of
[Cheng--Mao, arXiv:1905.06084v1](https://arxiv.org/abs/1905.06084),
whose reference objective is the ordinary configuration LP.
The compact-LP and configuration-LP comparators must be named rather
than silently identified. Cheng--Mao's separate `99/26` gap bound,
and Haxell--Szabo's later `53/15` gap bound, do not by themselves
supply corresponding efficient allocation algorithms.

For perspective only, substituting the **unclosed** candidate (6)
into the same compact reduction would balance
`theta=(1-theta)^2/4` at `theta=3-2sqrt(2)`, giving a candidate
factor `3+2sqrt(2)+o(1)`. This is another way to see why (6), even
if repaired, would not improve the ordinary factor-four baseline.

### 6.1 Arbitrary player-matroid basis selection: a separate union wrapper

The ordinary all-player reduction has a useful extension to any
original player matroid M. For fat resources at threshold theta T,
let N be the player transversal matroid supplied by those resources,
and use the derived player matroid

$$
(M^*\vee N)^*.
$$

Its rank is at most rank(M)=r. An original integral basis allocation
at target T supplies an integral feasible small-resource solution
for this derived matroid: the original discarded players form an
M* basis, the fat-served players form an N-independent set, and
their disjoint union extends to a union basis. The complement is a
derived dual basis of entirely small-served players.

Conversely, a derived small basis leaves a union basis that can be
partitioned into M*-independent discarded players and fat-matchable
players. Extending the former to an M* basis and deleting the
allocations of newly discarded players gives a valid original basis.
The proof, paid oracle implementation, and one-sided rational-grid
target search are in [item matroid union proof](../../problems/item-matroid-union/proof.md).

This gives the following model-matched comparison. All guarantees in
this table are relative to the original **integral optimum**, with
arbitrary resource values and an arbitrary matroid on the served
players.

| Inner result and union wrapper | General player-basis guarantee | Running time and status |
|---|---|---|
| Latest displayed DRZ v4 one-fifth theorem | `6+eta` | Polynomial for fixed eta; a derived consequence of the displayed theorem and public matroid union, rather than a separately printed general-basis corollary. |
| Historical DRZ v2 one-third theorem | `4+eta` | Historical polynomial claim under the same wrapper. Its subsequent version correction must be retained in the comparison; it is not an independently closed current proof. |
| New sharp-star current-blocker construction | `d_r=4-3/r` | `poly(input) 2^{O(r)}`, including the exact endpoint. |
| New construction with positive error | `d_r+eta` | `poly(input,bits eta) min{2^{O(r)}, (r+1)^{O((1+eta^-1) log(r+1))}}`. |

The separate [configuration-comparator.md](../../problems/item-matroid-union/configuration-comparator.md) strengthens
all of these composed comparisons to the natural configuration LP
with the player marginal in the base polytope of M. It splits fat
and all-small configuration mass, extends a fractional union
independent point to a base, and scales the small marginals to the
derived dual basis. The algorithm does not enumerate or solve the
configuration LP. This stronger comparator is also different from
the unrestricted-item compact Q_M(T).

For the first row, take fat threshold T/6. The displayed inner
guarantee is at least `(1/6-epsilon)T`; choose
`epsilon=1/6-1/(6+eta)`. A displayed promise algorithm can be run
for its polynomial bound and its output validated, yielding a
one-sided target test. It need not supply the new theorem's explicit
infeasibility certificate. This row is a consequence of the displayed
public theorem and keeps the source-interface qualification in
Section 4; it is not presented as a newly repaired proof of DRZ.

For the new exact row take theta=1/d_r. Every small item has value
u<theta T, and the auxiliary rank r' is at most r. Hence

$$
\theta T+\rho_{r'}(2\theta T+u)
 \le\theta T(1+3\rho_r)=T.
$$

The inner exact solver supplies value theta T, as do the fat items.
The positive-error row uses epsilon=1/d_r-1/(d_r+eta), whose inverse
is `O(1+eta^-1)`. Union and dual queries have polynomial full-input
cost, so these wrapper bounds deliberately use a polynomial input
factor rather than the inner theorem's linear multiplier.

In particular, the `8+eta` broader-resource-matroid headline in
Section 5 is not the strongest composable public comparison for this
subclass: the displayed DRZ theorem plus this union wrapper gives
`6+eta`. Nor should the new row be advertised as the first historical
appearance of factor four, given the old DRZ one-third claim. The
rank-sensitive exact factor approaches four and is not a uniform
constant-below-four algorithm.

The ordinary Jansen--Maack parameterized scheme is also not eclipsed:
when every player is compulsory its parameter is at most the total
player count and it obtains ratios arbitrarily close to one. The new
wrapper allows q to be much larger than the selected basis rank r
without a q^r enumeration. No stronger independently closed primary
source for this precise rank-only, oracle-player-matroid interface
was identified in the bounded audit. This is not a global priority
claim.

## 7. Comparison language suitable for a checkpoint

The independently checked current-blocker theorem establishes a
rank-sensitive quality/time tradeoff for the exact DRZ player-basis
LP, with the sharp-star target stated above and an explicit
infeasibility alternative. The latest public manuscript displays a
polynomial one-fifth guarantee. The earlier one-third value was
already asserted in an older public version and was revised; it is
therefore inappropriate to claim the first historical appearance of
that coefficient.

The possible quadratic public curve has been algebraically checked
but remains gated by a specific historical-exchange interface. The
ordinary Santa Claus corollary returns to factor four and is an
application of the theorem, not another approximation breakthrough.
The separate arbitrary-player-matroid union wrapper gives the exact
finite-rank ratio `4-3/r` and a `4-3/r+eta` rank-quasipolynomial
guarantee relative to integral optimum. Its model-matched current
public comparison is the derived polynomial `6+eta` consequence,
with the historical factor-four claim stated explicitly.

