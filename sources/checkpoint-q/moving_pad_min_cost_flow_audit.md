# Independent audit of the moving-pad logarithmic flow client

**Positive proof audit, 25 October 2026.** This note checks the proposed
transfer from the raw-cycle engine to exact minimum-cost circulation.
It is independent of the power-barrier IPM and does not use the literal
numerical formulas of Section 8 of arXiv:2311.18295v1.

The assembled primary statement is
[A moving-box logarithmic client for exact minimum-cost flow](moving_box_log_barrier_flow.md).
That statement also handles positive thresholds, nonzero integral
divergence, and artificial feasible initialization. The simpler
zero-divergence, negative-threshold convention below isolates the
independent checks; it does not restrict the primary theorem.

The structural input is the existing deterministic raw-cycle backend,
including its full lifetime, before-cancellation motion, and finite-word
interfaces. The client developed here is a new extension of the matching
client: it allows the nonseparable cost-gap logarithm, freezes its global
scale between rebuilds, and preserves short root labels by moving the
barrier bounds outward.

## 1. Problem, margins, and the potential

Consider a directed multigraph with `m >= 1` nonzero-capacity arcs,
integral capacities `u_e >= 1`, and integral costs `c_e`. Reference
orientations are the actual arc orientations. A circulation always
satisfies `B^T f = 0` exactly. Let `C=max(1,max |c_e|)` and
`U_c=max(1,max u_e)`. Initially `f=0`.

For an integral target `F<0`, write

\[
 z=c^Tf-F,\qquad
 \Psi(f)= -A\log z+
       \sum_e\bigl(\log(f_e-l_e)+\log(u'_e-f_e)\bigr),
 \qquad A=40m.                                             \tag{1}
\]

The maintained bounds satisfy `l_e <= 0` and `u'_e >= u_e`.
Initialize `l_e=-8 delta` and `u'_e=u_e+8 delta`.
At an exact coordinate anchor, if a lower slack is at most `4 delta`,
decrease `l_e` by `8 delta`; if an upper slack is at most `4 delta`,
increase `u'_e` by `8 delta`. Then recompute the anchored price.
The coordinate value is unchanged by either descriptor change.

All data magnitudes are bounded by a polynomial master `S`. Use a
dyadic `delta=S^(-1000)` and a strictly finer common flow grid, for
example `S^(-3000)`, after choosing `S` to be a power of two. The
history guard limits the total number of completed anchor and descriptor
operations to a fixed polynomial in `S` whose exponent is well below
1000. Thus the total outward movement of every bound, and their total
over all coordinates, is tiny. The favorable-branch runtime below lies
strictly within that guard for large enough `S`.

This is an acyclic use of the history guard: under the guard, bounds
and prices fit declared polynomial magnitudes; that establishes the
per-step and global-work estimates; those estimates then imply that
the guard does not fail on the favorable branch. The guard itself is
not an infeasibility certificate.

## 2. A constant-strength comparison direction

Let

\[
 s^-_e=f_e-l_e,\quad s^+_e=u'_e-f_e,\quad
 b_e=(s^-_e)^{-1}-(s^+_e)^{-1},\quad
 \lambda_e=(s^-_e)^{-1}+(s^+_e)^{-1},\quad
 g=-Ac/z+b.                                                \tag{2}
\]

Suppose a circulation `f*` exists in the ORIGINAL box
`0 <= f*_e <= u_e` with `c^T f* <= F`. Put `d=f*-f`.

If `d_e >= 0`, then `d_e <= s^+_e`, and

\[
 b_ed_e=\lambda_e|d_e|-2d_e/s^+_e
                                  \ge \lambda_e|d_e|-2.
\]

If `d_e < 0`, then `|d_e| <= s^-_e`, and the identical inequality
follows using the lower slack. Summing gives

\[
 b^Td\ge\|\Lambda d\|_1-2m.
\]

Moreover `c^T d <= -z`. Therefore

\[
          g^Td\ge A+\|\Lambda d\|_1-2m
                  =\|\Lambda d\|_1+38m.                    \tag{3}
\]

This proves the strong-direction guarantee without a centrality
invariant, a hidden stable witness, or a small current cost gap.
The only comparison vector used is an original feasible circulation.
Every outward pad update preserves the assumptions behind (3).

## 3. Frozen cost scale and coordinatewise stale prices

At the beginning of an epoch, set the reference `r=z`. Maintain exact
coordinate anchors `fhat_e`, updating an anchor only when its notified
relative drift is large. Store

\[
                 G_e=-Ac_e/r+b_e(\widehat f_e).             \tag{4}
\]

For a small parameter `q`, ensure at every settled query that

\[
 \widehat\lambda_e|f_e-\widehat f_e|\le \tau,
 \qquad |z/r-1|\le\eta,
 \qquad \tau,\eta\le q/10^4.                               \tag{5}
\]

Descriptor changes are immediately anchored; thus both slacks in
`b(fhat)` refer to their CURRENT bounds. The basic reciprocal estimate
then gives

\[
 (1-O(\tau))\widehat\lambda_e
       \le\lambda_e\le(1+O(\tau))\widehat\lambda_e,
 \qquad
 |b_e(f_e)-b_e(\widehat f_e)|\le 3\tau\widehat\lambda_e.
\]

Define `a_r=r/z`. Since `a_r=1+O(eta)`,

\[
                 g=a_r G+e,\qquad
 |e_e|\le(3\tau+2\eta)\widehat\lambda_e.                    \tag{6}
\]

Only the infinity norm in (5)--(6) is needed. No claim that a sum of
coordinate errors is at most `tau` is made. A dot product with an
arbitrary circulation is bounded by its weighted one-norm, which is
exactly the norm used by the raw-cycle backend.

The global scalar `a_r` need not be applied to every stored edge.
It changes no maximizing cycle for (4), and its known value is used
only in the analysis. The next full rebuild begins when the cost gap
leaves the window in (5).

## 4. Integer pricing and the safe step normalization

At an anchor, round `H lambda_hat_e` upward and `H G_e` to the nearest
integer, using a sufficiently large fixed polynomial price scale `H`.
For example, the same `H=S^100` as in the matching client suffices
under its declared polynomial envelopes. Every real length is then
at least `S^Omega(1)`. The degree-three port-path connectors have
length one and gradient zero; their extra length is negligible for
the lifted comparison direction. Integer rounding adds a negligible
multiple of the raw denominator to (6).

The raw backend yields a signed physical circulation `c` represented
by a list of forest paths and explicit edge occurrences. Let `N>0`
be its integer-priced numerator after choosing its orientation, and
let `V>0` be its integer-priced RAW denominator, counting all
occurrences before cancellation. Accept only when

\[
                              N\ge 2qV.                    \tag{7}
\]

Equation (3), (6), and the backend quality imply that a sufficiently
small fixed multiple `q` of the inverse backend envelope makes LOW
impossible when an original feasible target solution exists.

The numerical step must be normalized by `N`, not by `V` alone.
The global cost term in (4) means `|G_e| <= lambda_e` is generally
false. Choose a dyadic `mu > 0` with

\[
          q^2/400\le\mu N/H\le q^2/200.                    \tag{8}
\]

This is possible by selecting a power of two. The polynomial price,
raw occurrence, and input magnitude guards make `mu` far above the
common flow-grid spacing. Because the circulation uses integer
coefficients, `h=mu c` remains on that grid exactly, without
coordinatewise rounding.

By (7)--(8), the total raw anchored motion is at most `q/400`, up to
the negligible integer-pricing margin. Equations (6)--(8) give

\[
            g^Th\ge c_1 q^2,\qquad
            \sum_e\lambda_e|h_e|\le c_2q                   \tag{9}
\]

for fixed positive constants, with `c_1` larger than the second-order
barrier loss after increasing the fixed denominators in (8) if needed.
The existing matching-client Taylor estimate applies to the two
coordinate logarithms. The extra term `-A log z` is convex on the
positive-cost-gap domain and lies above its tangent. Hence

\[
                         \Psi(f+h)-\Psi(f)\ge c_3q^2.       \tag{10}
\]

### The global cost gap is an atomic quantity

From (4),

\[
 \frac{|c^Th|}{r}
   \le\frac{|G^Th|+|b(\widehat f)^Th|}{A}
   \le O(q/m).                                             \tag{11}
\]

Therefore the FINAL cost gap remains positive, and so does its value
on the straight line `f+t h`, `0 <= t <= 1`, used by the proof.

Actual application of the path list may temporarily change divergence
or move the scalar cost gap outside this interval before all pieces
are applied. In particular, a gradient gauge can make its intermediate
signed cost very large. The complete circulation is therefore one
atomic transaction: no pricing, LOW decision, descriptor change, or
logarithm evaluation occurs between its pieces. The signed cost
accumulator may have either sign during that transaction. Coordinate
barriers DO remain positive throughout every partial path application,
because their changes are bounded by the full raw motion. Settlement
and any global rebuild happen only after the complete transaction.

## 5. Pad updates and the potential ledger

Before an anchor is refreshed, (5) keeps its current slack within a
small relative factor of its anchored slack. Immediately after a
pad operation the affected anchored slack is greater than `8 delta`.
An unchanged anchored slack is greater than `4 delta`. Combined
with the partial raw-motion bound, this leaves a strict margin above
`3 delta` before the next settlement. Thus the tested pad operation
never attempts to repair a nonpositive argument after the fact.

Decreasing `l_e` or increasing `u'_e` increases a positive slack
while leaving `f` and `z` unchanged. Hence each pad operation
increases `Psi`. There is no negative potential charge associated
with an outward pad.

While the stopping test has not succeeded, assume
`z >= tau_stop`, where `tau_stop` is an inverse polynomial chosen
well below one. Under the cumulative pad guard, each coordinate
slack is at most `U_c+o(1)`. It follows that

\[
                         \Psi(f)\le O(m\log S).             \tag{12}
\]

Initially `Psi(f) >= -O(m log S)`. If edges are inserted, one new
zero-flow edge loses only `O(log S)` potential; there are at most
`m` such losses. Global rebuilds and representation changes do not
change any objective value. Equations (10)--(12) therefore imply

\[
                         J=O(mq^{-2}\log S)                \tag{13}
\]

successful steps in a threshold instance, also in the incremental
setting up to its first YES answer.

Equation (11) bounds the relative change of `z` in one step by
`O(q/m)`. A global epoch has width `eta=Theta(q)`, so every
completed epoch contains `Omega(m)` successful steps (with fixed
constants chosen in the correct order). Thus there are
`O(1+J/m)` full cost-scale rebuilds, and their combined actual-record
volume is `O(m+J)`. Inserting an edge with flow zero changes no cost.

The raw-motion detector consumes `Omega(q/A_occ)` charged motion per
coordinate report, where `A_occ` bounds exposed copies. A step creates
`O(q)` motion. The matching client's complete-copy and retirement
accounting therefore gives `O(A_occ)` reports per step, including
the necessary descriptor repricing. Old dormant counters are never
silently reset. A global rebuild is charged separately by its full
actual record volume, not disguised as a free collection of reports.

Consequently, if all structural costs and copy counts are bounded by
`E`, the total time is `m E^O(1) poly(log S)`. Choosing
`E=exp O((log m)^(4/5)(loglog m)^(1/5))` retains that exponent.

## 6. Exact original-box recovery

Suppose the stopping rule finds an exact circulation `f` satisfying

\[
                     c^Tf\le F+\tau_{\rm stop},
 \qquad
 V(f):=\sum_e\bigl(\max\{-f_e,0\}+\max\{f_e-u_e,0\}\bigr)
                 \le\nu_{\rm pad}.                         \tag{14}
\]

The lifetime pad budget makes `nu_pad` arbitrarily small compared
with any declared input polynomial. In particular, arrange
`tau_stop + P nu_pad < 1/4`, for an integer penalty

\[
                 P> 4m C(U_c+1)+4.                         \tag{15}
\]

Round within each ORIGINAL unit interval `[floor f_e,ceil f_e]`.
On that interval `c_e x + P(max{-x,0}+max{x-u_e,0})` is affine,
because all its breakpoints are integral. Use its affine slope as
the cycle-cancellation cost. Standard deterministic fractional-cycle
rounding preserves divergence, stays inside these unit intervals,
and does not increase

\[
                           Q(x)=c^Tx+P V(x).                \tag{16}
\]

It ends at an integral circulation `x`. The fractional support cannot
be a nonempty forest: a leaf would have a nonintegral divergence
after all other incident integral coordinates are subtracted.
Thus a fractional cycle always exists until the procedure finishes.
Each cancellation fixes an additional coordinate to an integer;
the dynamic-tree implementation uses near-linear bit work.

The pad bounds also ensure `floor f_e >= -1` and
`ceil f_e <= u_e+1`. If an integral output violated the original
box, `V(x) >= 1`, and

\[
                     Q(x)\ge P-mC(U_c+1)>1.
\]

On the other hand, since `F<0`, (14)--(16) give
`Q(x) <= Q(f) < F+1/4 < 1`. This contradiction proves that `x`
lies in the original box. Its cost is an integer and
`c^T x < F+1`, so `c^T x <= F` exactly.

This recovery uses no new max-flow or min-cost-flow call. It also
does not require a sequence of separate repairs of negative and
over-capacity coordinates.

## 7. Finite arithmetic and declared master bounds

The potential itself need not be evaluated by the implementation.
Only rational derivatives, the exact cost gap, and integer comparison
tests are used. Suppose the input size and all original magnitudes
are within `S^20`, and take the stopping threshold to be, for example,
`tau_stop=S^(-50)`. Choose the history exponent below 100 and enlarge
the fixed master size convention if necessary. Then:

* current slacks are at least `3 delta` at settled states and at most
  `S^20+o(1)`;
* inverse slacks and both logarithmic derivatives are at most a fixed
  multiple of `S^1000`;
* the cost term `A c_e/r` has a smaller fixed polynomial bound,
  since every priced epoch begins above the stopping threshold;
* `H=S^100` therefore puts the rounded root prices below `S^1200`,
  while every real integer length is at least `S^80`;
* the raw numerator and denominator are sums over polynomially many
  traversals in the favorable envelope, so their bit widths remain
  `O(log S)` with an explicit fixed coefficient.

All values and bounds are on the common `S^(-3000)` dyadic grid.
The reference gap `r=c^T f-F` is on that grid as well. Computing
`-A c_e/r + 1/s^-_e - 1/s^+_e` exactly for one coordinate uses at
most three local denominators, each of `O(log S)` bits. Their product
still has `O(log S)` bits. This is not a least-common-multiple operation
over the graph.

For `q>=S^(-1)` and the preceding raw bounds, the power of two chosen
in (8) is much larger than `S^(-3000)`. Thus every complete step
preserves the grid literally. The per-copy motion thresholds can also
be chosen as powers of two on that grid, using the matching client's
complete-copy detector construction. Prices may be recomputed by
exact integer division and rounding, without evaluating a logarithm,
an exponential, or a fractional power.

The exact signed cost accumulator is stored with a polynomial
transaction envelope. Its intermediate magnitude can be larger than
the cost of any settled feasible state, but remains bounded by the
explicit raw traversal count times the maximum input cost times the
step size. A separate fixed polynomial guard covers that quantity;
it is never used as a logarithm argument until the transaction closes.

Consequently the primary pure-log transfer uses the EXISTING
`O(log S)`-bit numerical root interface. The wider polynomial-bit
extension in the companion note is useful for the independent
power-barrier route, but is not a dependency of this transfer.

## 8. Scope of what has been checked

The following mathematical client boundaries are now explicit:

* the comparison direction uses an original feasible circulation;
* only coordinatewise stale-price accuracy is required;
* numerator-normalized dyadic steps control the nonseparable cost term;
* complete circulation application is atomic for the global logarithm;
* outward pads have the favorable potential sign;
* all global scans are charged by completed epoch progress;
* exact affine-penalty rounding returns an original-box integral flow.

The remaining shared dependency is the prior raw-cycle construction
and its complete occurrence/lifetime interface. This audit does not
independently certify that structural construction. The numerical
guards alone do not prove the time bound or validate a LOW answer.
