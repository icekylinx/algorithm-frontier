# From the raw-cycle backend to the frozen-barrier detector

**25 October 2026. Independent interface reconstruction.**

This note supplies the numerical interface assumed by
[frozen-barrier-distance-detector.md](frozen-barrier-distance-detector.md). It uses the raw, before-cancellation
cycle certificate, complete occurrence lifetimes, and implicit exact flow
registers of the previous checkpoint. It does not infer a flow-maintaining
oracle from an approximate optimum value alone.

The construction below is conditional on the previously stated raw backend.
Its purpose is to show that the new detector needs no additional asymptotic
oracle guarantee. In particular, a positive frozen flow is retired without
discarding its cost or divergence, and the growing power in the barrier is
paid in local arithmetic rather than exported label magnitude.

## 1. Imported contract and master sizes

Let the global graph master be a power of two `N=2^U`. A detector lifetime
has at most `M<=N` logical ordinary-edge records, auxiliary units, and
vertex records, up to a fixed constant in this allowance. A port path at
each logical vertex uses `O(M)` additional records. Neither the potential
coefficient `AM` nor the reporting bound counts the backend's expanded
occurrences.

Choose one envelope `R=N^o(1)` that bounds, by increasing a fixed power of
the existing envelope if necessary:

* the inverse approximation quality of the raw cycle query;
* its number of signed physical-edge/forest-path pieces;
* complete current and dormant copy multiplicity;
* initialization, updates, queries, and exposed-forest callback costs.

All guarantees apply to the actual adaptive operation sequence and its
polynomial horizon. The flat forest has at most `M R^O(1)` records.

The raw backend accepts positive integer lengths and signed integer
gradients on a graph of maximum degree three. A returned object consists
of unit signed pieces whose physical projection `c` is a circulation.
Its denominator `V` sums the physical lengths of **all traversals before
cancellation**. If the maximum absolute circulation ratio is `OPT>0`,
the returned object has `V>0` and

$$
|\gamma^T c|/V\geq \mathrm{OPT}/R.                 \tag{1}
$$

The actual oriented numerator is computed from the same retained edge
lifetimes. Only physically empty images are null. A real loop or an edge
with zero current gradient is still a real record. Old endpoints, prices,
and logical identities remain available until their last retirement
callback completes.

If a previous formulation permits labels only up to `S^1200`, set its
numerical master to `S=N^C` for one sufficiently large fixed integer `C`.
All exponents below are fixed once the input weight envelope and primitive
constants are fixed. This change preserves

$$
\exp O\bigl((\log S)^{4/5}(\log\log S)^{1/5}\bigr)
 =\exp O\bigl(U^{4/5}(\log(U+4))^{1/5}\bigr).
$$

No local detector is padded to size `N` or `S`; these are precision and
parameter masters. Work and inventory still scale with its actual local
allowance `M`.

## 2. Exact flow registers and the extra cost aggregate

For every logical coordinate use the existing representation

$$
f_e=\operatorname{base}_e+\sum_{q\mapsto e}h_q.       \tag{2}
$$

The sum includes every live and dormant occurrence. The registers `h_q`
are maintained by signed path additions; independent absolute-motion
registers and logical drift buckets maintain the refresh invariant.
Retirement transfers the signed register to the base and the absolute
register to its bucket before invalidating the old mapping.

Maintain one additional immutable label on a real logical edge: its cost
in the detector's normalized ordinary graph, or its auxiliary anchor
cost. All costs have a common dyadic denominator. Store signed path sums
of this label in the exposed forest, alongside the existing length and
gradient sums. This adds a fixed number of fields to the dynamic-tree
operations. It does not enumerate an implicitly represented long path.
Connectors and true null edges carry cost zero.

Consequently a raw answer supplies three different quantities:

1. `V`, its positive before-cancellation integer length;
2. `gamma^T c`, its signed current-price numerator;
3. `c_cost^T c`, its signed **fixed-cost** change.

The third quantity cannot be replaced by the stale gradient numerator.
It allows the complete proposed objective change to be tested before the
flow update is applied. Cancellation is legitimate in this affine cost
sum, but not in the motion denominator.

## 3. Stale prices and the global logarithm

Use the notation of the detector: its gap is `r=P-(1-alpha)F>0`, its
gradient is `g=AM c_cost/r-w`, and `w` is the positive magnitude of the
derivative of the coordinate barrier. Let

$$
\beta=1/(256R),\qquad \xi=\beta/10^5.
$$

Increasing the fixed envelope to a power of two makes this numerical
choice dyadic. Maintain an anchor `rhat` and coordinate anchors such that

$$
|r/rhat-1|\leq\xi,\qquad
 |what_e/w_e-1|\leq\xi.                              \tag{3}
$$

At the anchors define `ghat=AM c_cost/rhat-what`. If `kappa=r/rhat`,
then the cost terms cancel exactly:

$$
\widehat g-\kappa g=\kappa w-\widehat w.             \tag{4}
$$

Thus `|ghat-kappa g|<=2 xi w`, regardless of the magnitude or cancellation
of the individual cost-gradient terms. This is why an additive
coordinate bound on `g` relative to `w` is unnecessary.

For a coordinate anchor it suffices to maintain

$$
\widehat w_e |f_e-\widehat f_e|
 \leq \xi/(C(p+1)),                                 \tag{5}
$$

for a large absolute `C`. For the ordinary logarithm this is stronger
than necessary. For the auxiliary branch below one,
`w=f^(-p-1)` and `w>=1/f`; its logarithmic derivative has magnitude
`(p+1)/f`. The branch above one has `w=1/f`. Integrating these inequalities,
including across the continuously differentiable join at one, proves
the second part of (3) from (5).

All anchors are read at settled exact grid values. Neither (3) nor a
LOW decision is tested midway through an unfinished raw transaction.

## 4. Integer labels and a sound LOW threshold

The detector's potential and slack guards imply polynomial bounds in `N`
on `w`, `1/w`, `|g|`, coordinate values, and `1/r`. Fix one common scale
`H=N^C_H`, large enough that for all logical edges

$$
H w_e\geq N^3/\beta
$$

and that rounding errors are below `xi w_e`. Export

$$
\ell_e=\lceil H\widehat w_e\rceil,\qquad
 \gamma_e=\operatorname{round}(H\widehat g_e).          \tag{6}
$$

The integers have `O(U)` bits. The degree-three lift replaces each logical
vertex by a private path of ports, with length-one, zero-gradient
connectors. A logical circulation `d` lifts by routing its incidence
imbalances along the paths. If there are `P_0=O(M)` port records, its
connector length is at most

$$
2P_0\sum_e|d_e|.                                    \tag{7}
$$

The scale choice makes (7) negligible relative to `H sum w_e|d_e|`.
Thus if the true logical circulation ratio is at most `-1/4`, the
corresponding integer-priced lifted circulation has absolute ratio
at least `1/5`, after a harmless further increase in fixed constants.
This statement concerns a comparison direction, not the returned raw
answer, and uses the full connector cost of that direction.

Orient a raw answer so that `T=-gamma^T c>=0`. Return LOW only if the
backend supplies no positive certificate or its valid certificate has

$$
T/V<1/(16R).                                        \tag{8}
$$

Equation (1) and the preceding `1/5` comparison prove that (8) is
impossible if any true logical circulation has ratio at most `-1/4`.
Therefore LOW has the soundness required by circulation duality in the
detector. A primitive error, failed guard, unfinished callback, or
invalid representation is never interpreted as LOW.

For an accepted answer, (4)--(6), cancellation only in signed sums,
and the raw length bound give

$$
-g^T c\geq 7\beta V/H.                              \tag{9}
$$

The true weighted absolute motion of the full raw traversal list is
at most `2V/H`. Define the certified raw denominator for the numerical
step to be

$$
R_{\rm raw}=2V/H.
$$

Then (9) implies `g^T c<=-3 beta R_raw`. In particular it supplies the
weaker `-beta R_raw` descent guarantee used in the detector. There is
no reliance on the norm of the projected circulation after cancellation.

## 5. Dyadic steps, positivity, and objective tests

Choose a power of two `eta` by integer comparisons so that

$$
\frac{\beta}{C_1p}\leq\eta R_{\rm raw}
 \leq\frac{2\beta}{C_1p}.                            \tag{10}
$$

Such a power of two always exists. The output contains unit signed
pieces, so `eta c` is an exact common-grid circulation. Every partial
coordinate change while applying its pieces is bounded by the left
coordinate's share of the full raw motion in (10). The ordinary slacks
and auxiliary coordinates therefore remain strictly positive at every
intermediate state, for sufficiently large fixed `C_1`.

The fixed-cost aggregate computes the proposed complete `P'` before
application. If it satisfies the detector's stopping inequality, use
that complete flow as the sound stopping witness and do not apply the
update. Otherwise the final gap remains above `alpha F/4`. Apply every
piece as one atomic numerical transaction, then settle all stale-price,
freeze, and representation callbacks before another query.

A prefix of a raw forest-path list need not be a circulation and may
have a negative affine cost gap. No logarithm, LOW decision, or flow
objective assertion is made about such a prefix. The proof of potential
decrease uses the straight segment between the two complete flows. Its
gap is positive because the two endpoint gaps are positive.

The local barrier Hessian obeys the integrated bound
`O(p ||W h||_1^2)`, while the global logarithm is concave. Together with
(9)--(10), this gives the claimed decrease `Omega(beta^2/p)`.

## 6. Freezing is an exact retirement transaction

When a refreshed auxiliary weight crosses its threshold, read its exact
current value `z_j`. If its true weight is at least `K/2`, then
`0<z_j<1`. Retire it as follows.

1. Preserve its immutable exact value `z_j`, cost `a_j z_j`, and
   incidence/divergence contribution.
2. Remove its active logical edge using the ordinary complete-copy
   deletion interface. Old images and prices remain valid until all
   transfers required by (2) finish.
3. Delete its positive coordinate barrier. Add its cost to the frozen
   offset, and remove it from the variable part of the cost sum.
4. Settle affected refresh lists before allowing another cycle query.

Full flow, full demand, and full cost are unchanged by this transaction.
The active graph's residual demand changes by the already recorded
divergence. Future increments are circulations on the remaining active
edges. Port connectors impose conservation of these increments; they
never stored the original primal flow. No ordinary-flow rerouting is
needed to retire the auxiliary edge.

Similarly, a new auxiliary unit sets its logical base to one and adds
its demand, anchor cost, and barrier. This is a separately accounted
external demand change, followed by circulation increments. It is not
misdescribed as a circulation at insertion.

An ordinary edge may start at zero with slack `delta_0`; pay a constant
number of initial rearming operations per birth, or initialize it at the
safe reset slack. Every subsequent rearm is separated by a fixed amount
of weighted motion. Neither rearming nor freezing creates new logical
ports for a retained edge identity.

## 7. Work and refresh accounting

The detector proves a total of

$$
T=O(Mp\beta^{-2}U)
$$

accepted steps. Their total raw weighted motion is `O(T beta/p)`.
Use the old absolute-drift scheme with per-copy threshold smaller than
the right-hand side of (5) by the complete copy-multiplicity bound.
The resulting number of genuine coordinate refresh reports is at most
`T R^O(1) poly(U)`, apart from explicitly paid births and resets.

This statement includes dormant copies, pre-existing logical buckets,
and retirement transfers. Representation changes may reveal old drift,
but cannot charge that same drift repeatedly as fresh numerical motion.
Complete replacement and callback work is charged under the imported
lifetime contract.

Full repricing is also bounded. For an accepted negative-gradient step,

$$
AM\,\Delta r/r=g^T h+w^T h\leq\|Wh\|_1
                  =O(\beta/p).
$$

Positive logarithmic gap variation due to numerical steps is at most
`O(T beta/(Mp))`; auxiliary births add `O(U)`. Since the gap remains
between fixed powers of `N`, negative logarithmic variation is bounded
by this positive variation plus `O(U)`. Repricing at relative changes
of order `xi=Theta(beta)` consequently costs at most
`R^O(1) poly(U)` complete passes. Each pass reads and reprices `O(M)`
logical coordinates, with its actual occurrence work included.

The entire detector lifetime therefore costs

$$
M R^{O(1)}\operatorname{poly}(U).                    \tag{11}
$$

This factor is computational work. It is not included in `AM` and is
not multiplied into the potential charge for a retired barrier. The
cumulative frozen-unit count remains `O(alpha M U^2/sigma)`.

## 8. Finite precision is a value-and-denominator argument

The polynomial state bounds alone are not enough to control rational
denominators. The step choice (10) supplies the missing denominator
argument.

Every forest path has at most its flat inventory in edges. There are
at most `R^O(1)` pieces and each exported integer root label is at most
a fixed power of `N`. Hence `1<=V<=N^C_V`. Since `beta>=N^-1/100`
eventually and `p=O(U)`, (10) gives a fixed polynomial lower bound on
`eta`. Choose one common dyadic flow grid fine enough to contain all
such power-of-two steps, the initial values, input costs, and all
ordinary slack offsets. Accepted flow updates never round coordinates
independently.

Each coordinate, frozen value, cost offset, and affine gap then has
`O(U)` bits on its respective fixed grid. Evaluating `f^(-p)` exactly
may create `O(U^2)`-bit temporary integers, because `p=O(U)`. This is
polynomial logarithmic arithmetic paid at a refresh. Rounding (6)
exports only polynomial-valued `O(U)`-bit integer labels. No product
over all graph-coordinate denominators is formed.

## 9. Consequence and limits

The raw backend already retained for general matching supplies the
frozen detector's required LOW/step, exact-cost, finite-grid, and
retirement operations with a fixed-power overhead. In particular its
four-fifths envelope remains four fifths. Combining this bridge with
the detector potential proof and the separately audited outer recursion
gives the incremental directed distance theorem stated there.

This is a mathematical proof assembly with explicitly imported
constructive interfaces. It is not an implementation benchmark or an
external verification. It makes no claim that static output checking
alone validates online LOW decisions, and it does not replace the
named raw backend by an unspecified numerical oracle.

### Supporting files and primary starting points

* [quantitative-matching-4-5-composition.md](quantitative-matching-4-5-composition.md) and
  [uniform-source-interfaces-for-4-5.md](uniform-source-interfaces-for-4-5.md) for the
  quantitative raw backend and its source scope.
* [priced-logarithmic-steps-from-raw-cycles.md](priced-logarithmic-steps-from-raw-cycles.md),
  especially its degree-three ports and signed/absolute retirement
  registers, and [numerical-backend-lifetime-and-loops.md](numerical-backend-lifetime-and-loops.md).
* [min cost flow proof](../../problems/min-cost-flow/proof.md) for the independent fixed-cost path
  aggregate and atomic objective-test construction.
* Liu, *Incremental Shortest Paths in Almost Linear Time via a Modified
  Interior Point Method*, <https://arxiv.org/html/2506.19207v1>.
* Chen, Kyng, Liu, Meierhans, and Probst Gutenberg, *Almost-Linear Time
  Algorithms for Incremental Graphs: Cycle Detection, SCCs, s-t Shortest
  Path, and Minimum-Cost Flow*, <https://arxiv.org/html/2311.18295v1>.
