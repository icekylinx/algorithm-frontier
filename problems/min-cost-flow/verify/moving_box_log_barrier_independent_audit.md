# Verification note

**Curated source path:** `sources/checkpoint-o/moving_box_log_barrier_independent_audit.md`

The source audit follows.

# Independent audit of the moving-box logarithmic flow client

**Research note, 25 October 2026.** This audits the proposed numerical client, conditional on the already reconstructed deterministic raw minimum-ratio-cycle engine. It does not import a generic min-cost-flow reduction without checking its numerical interface. The reviewed scope here is static integral minimum-cost flow with polynomially bounded numerical data.

## 1. A useful exact inequality

For one coordinate let `a <= 0 <= u <= b`, let `a < x < b`, and put

\[
 b'(x)=\frac1{x-a}-\frac1{b-x},\qquad
 \lambda(x)=\frac1{x-a}+\frac1{b-x}.
\]

For every `y in [0,u]`,

\[
 b'(x)(y-x)\geq\lambda(x)|y-x|-2.                 \tag{1}
\]

If `y>=x`, the difference between the right and left weighted terms is `2(y-x)/(b-x)<=2`. If `y<=x`, it is `2(x-y)/(x-a)<=2`. This proof remains valid when the current coordinate is slightly outside its original box, because the comparison point lies inside the original box and hence inside the expanded box.

Let the original flow instance have `N` coordinates, integral costs `c`, conservation matrix `B`, and an integral threshold `F`. For an expanded-box feasible current flow `f` with exact conservation and positive gap `z=c^T f-F`, define

\[
 \Psi(f)=-W\log z+
   \sum_e[\log(f_e-a_e)+\log(b_e-f_e)],\qquad W=40N. 
                                                               \tag{2}
\]

If a true box-feasible flow `f*` of cost at most `F` exists, `d=f*-f` is an exact circulation, and (1) implies

\[
 \nabla\Psi(f)^Td
 \geq \|\lambda(f)d\|_1+38N.                    \tag{3}
\]

Indeed `-c^T d/z>=1`, so the cost term contributes at least `40N`. Thus a correctly implemented sufficiently accurate LOW answer cannot occur while the gap is above the stopping threshold and such a comparison flow exists.

## 2. Frozen cost anchors do not require coordinatewise control of the cost term

Let `r>0` be a stored cost-gap anchor and `fhat` the coordinatewise barrier anchors. Write

\[
 G=-Wc/r+b'(\widehat f),\qquad \alpha=r/z.
\]

The exact identity is

\[
 \nabla\Psi(f)=\alpha G+
       [b'(f)-\alpha b'(\widehat f)].             \tag{4}
\]

Consequently, if `r/z=1+O(eps)` and every current reciprocal barrier argument is within `1+O(eps)` of its anchor, then

\[
 |[\nabla\Psi(f)-\alpha G]_e|
       \leq O(\epsilon)\widehat\lambda_e.        \tag{5}
\]

There is no requirement that `|c_e|/r` be controlled by a local barrier length. Its potentially large value cancels exactly in (4). Taking `eps` to be a sufficiently small fixed multiple of the accepted cycle quality `q` makes the gradient error small compared with the accepted numerator. Integer price rounding must receive an additional allocation of this same error budget.

## 3. Step normalization and progress

Use an accepted compressed raw circulation `h`. Let `V` be its raw weighted traversal, so `||lambdahat h||_1 <= V`, and let

\[
 A=G^Th>0,\qquad A\geq 2qV.                     \tag{6}
\]

Choose a positive common-grid step `mu` such that

\[
 q^2/400\leq\mu A\leq q^2/200.                 \tag{7}
\]

Then `mu V<=q/400`. Under (5), the true first-order gain is a fixed fraction of `mu A`. The sum of the ordinary barrier Taylor errors is bounded by a fixed multiple of `(mu V)^2`.

The cost-gap relative motion also obeys

\[
 \frac{\mu|c^Th|}{r}
 \leq\frac{\mu A+\mu |b'(\widehat f)^Th|}{W}
 \leq\frac{\mu A+\mu V}{40N}=O(q/N).             \tag{8}
\]

Its Taylor error in the first term of (2) is therefore `O(q^2/N)`, with constants made smaller by the slack in (7). Every accepted step gains `Omega(q^2)` in `Psi`. The bound (8) also keeps the gap strictly positive, so stopping at a small positive gap never evaluates the logarithm at a nonpositive argument.

A full cost-anchor rebase after a relative `Theta(q)` change requires `Omega(N)` accepted steps. All `N` labels may therefore be refreshed at a rebase with total full-refresh volume `O(J)` over `J` accepted steps, apart from the initial `O(N)` work. Pointwise barrier refreshes are charged by the usual raw-relative-motion notifications; they must not be recomputed by a complete graph scan after each step.

## 4. Moving pads and finite arithmetic

Initially take each lower and upper pad to be `8 delta`. On an exact coordinate refresh, if a barrier slack is at most `4 delta`, move that corresponding bound outward by `8 delta`, and reprice immediately. Both kinds of outward moves increase (2). They do not consume the progress budget.

If the declared complete history has at most `S^100` pad changes and `delta=S^-1000`, then the sum of all original-box violations is at most a fixed multiple of `S^-900`. A coordinate is always strictly inside its expanded box. The initial and final possible potential values differ by `O(N log S)`, since all numerical magnitudes and the inverse stopping gap are polynomially bounded in `S`. Hence

\[
 J=O(Nq^{-2}\log S).                              \tag{9}
\]

This argument uses an upper bound on the potential even after every pad move; it does not incorrectly subtract pad gains. The history guard must be proved inactive on the favorable parameter branch.

Use a power-of-two master bound `S` that bounds the augmented instance's record count and polynomially bounded numeric data. A sufficiently fine fixed dyadic grid keeps every flow update exactly conservative. The interval in (7) has inverse-polynomial width because the unscaled prices and the raw direction coefficients have polynomial bounds under the established raw-lift guard. A fixed finer dyadic grid therefore contains an allowed positive step. Logarithms are only used in the analysis; all executable comparisons use exact rational arithmetic, integer cross multiplication, or integer-rounded price labels.

The root bit bound is `O(log S)` with fixed constants; temporary local arithmetic inside the tree primitive is accounted for separately by the existing backend. A statement for arbitrary unbounded-bit costs requires a new explicit numeric-size parameter and is not asserted here.

## 5. Exact recovery from a near-feasible threshold point

Suppose the numerical phase stops with

\[
 c^Tf\leq F+\tau,\qquad \tau<1/4,
\]

and original-box violation small enough that

\[
 P\sum_e\bigl[(-f_e)_++(f_e-u_e)_+\bigr]<1/4.    \tag{10}
\]

Take the integer convex piecewise-affine penalty

\[
 L(f)=c^Tf+P\sum_e\bigl[(-f_e)_++(f_e-u_e)_+\bigr].
                                                               \tag{11}
\]

On any open integral cell, (11) is affine. While fractional coordinates remain, their support contains an undirected cycle: otherwise a leaf in the fractional-support forest would contradict integral vertex divergence and integral contributions from all other edges. Move along either orientation of such a cycle, choosing one with nonpositive slope for (11), until the first coordinate reaches an integer. Already integral coordinates never move again. Thus the process terminates after at most `N` pivots and does not increase (11).

Every final coordinate lies between the floor and ceiling of its initial value, hence between `-1` and `u_e+1` once the total violation is below one. Consequently its cost is at least `-N C(U+1)`. Choosing an integer

\[
 P>2NC(U+1)+|F|+2                              \tag{12}
\]

ensures that any final integer point outside the original box has penalty larger than `F+1/2`, impossible by (10). The final point is box feasible and its integer cost is below `F+1/2`, hence at most `F`.

The pivots can use the existing fractional-support dynamic-forest rounding implementation: maintain the sum of the fixed cell slopes and the minimum admissible increase/decrease on a tree path, settle one pending non-tree edge, and remove the edges that become integral. Each pivot settles at least one fractional coordinate and the total topology work is `O(N)` up to logarithmic factors. No generic static max-flow call is needed for this final rounding.

## 6. Two outer interfaces that must be stated explicitly

### 6.1 A second exact linear functional

The general flow client needs exact values of `c^T f` and `c^T h` to detect termination, enforce cost-anchor thresholds, and perform (8). The old matching client has special return-arc objectives, so this capability should not be silently assumed.

A sufficient implementation extends every dynamic-forest/raw-lift record with one additional fixed linear label for `c`, alongside the priced gradient label. It supports the same exact signed path sums and point updates. All alias/lifetime accounting is unchanged. Frozen contraction potentials for the extra label are independent of those of the current gradient. Fixed-degree port scaling must use the exact raw pullback, with any powers of two tracked explicitly. The same raw-traversal envelope bounds its exported label size. Since only a constant number of labels is added, the asymptotic work changes by a fixed factor.

This is an implementation obligation, not permission to expand every raw path or scan the entire graph at every numerical step. A proof of this extra-label interface should be included in the main construction.

### 6.2 Always-feasible augmentation and accepted-output validation

For arbitrary integral demands of total zero, add a hub and one artificial arc per nonzero demand, oriented to carry that demand. The original arcs carry zero initially, and the artificial arcs carry the absolute demand, so the augmented instance has a known exactly conservative box-feasible initial flow. Let `B0=mCU` bound the absolute cost of every original box-feasible flow and assign every artificial arc cost `P_art>2B0`. Artificial capacities can equal their initial absolute flows.

A true original feasible flow extends with zero artificial flow. Every integer augmented flow using at least one artificial unit has cost at least `P_art-B0>B0`, whereas an original feasible flow has cost at most `B0`. Therefore an exact augmented optimum uses no artificial arc if and only if the original instance is feasible. If it uses none, it is an exact original optimum.

For a guarded parameter portfolio, solve the always-feasible augmented optimization problem over its ENTIRE augmented integer cost range. Do not stop after LOW on every threshold in only the original cost range: that would leave an unverified infeasibility answer. Every worker should finish with a candidate augmented optimum. A fast deterministic residual negative-weight shortest-path routine supplies potential labels for a valid optimum; checking all residual inequalities and the primal flow takes linear time. Incorrect candidates cannot pass those checks. On an infeasible original input, the validated augmented optimum with cost greater than `B0` then certifies infeasibility as well.

The source for the independently reported near-linear deterministic negative-weight SSSP verifier is Haeupler--Jiang--Saranurak, arXiv:2511.08551v1, Theorem 1.1. Its exact interface and run-time assumptions must be retained in the baseline/import audit. The numeric client above does not rely on a verifier to prove its own progress bound.

## 7. Audit disposition

The barrier comparison, frozen-gap identity, step normalization, moving-pad accounting, and exact rounding admit the proofs above. Subject to the exact linear-functional extension and the already reconstructed raw engine, there is no remaining numerical obstruction identified in this audit to using the four-fifths envelope for static polynomially bounded min-cost flow. This is a conditional proof review, not an implementation or external mathematical certification.

For incremental maintenance, accepting each intermediate LOW answer without a complete residual verification is a different issue. It requires a fixed proved parameter tuple or an efficiently maintained exact dual certificate; the static final-output portfolio argument alone does not establish that online interface.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
