# Verification note

**Curated source path:** `sources/checkpoint-q/frozen_barrier_detector_independent_audit.md`

The source audit follows.

# Independent audit of the frozen auxiliary barrier detector

**25 October 2026.** This note audits `frozen_barrier_distance_detector.md` independently of its outer shortest-path recursion. The freeze accounting, comparison circulation, birth accounting, and sound LOW/termination implications pass the checks below. The result remains a research construction, with the stated raw-cycle interface and its quantitative implementation imported from the existing backend notes.

The central conclusion is substantive: deleting a positive barrier at retirement gives a cumulative frozen-unit bound

\[
 O(\alpha M (\log N)^2/\sigma)
\]

without an oracle approximation factor. The proof uses the complete potential budget, rather than the number of numerical steps. The running time still depends polynomially on the inverse oracle accuracy.

The public comparison is Liu, *Incremental Shortest Paths in Almost Linear Time via a Modified Interior Point Method*, arXiv:2506.19207v1, Sections 3.2--3.4, particularly Lemmas 3.4, 3.7, 3.10 and the detector proof. That source charges dangerous auxiliary edges through the number of numerical steps; the new retirement operation is absent there. Source: <https://arxiv.org/html/2506.19207v1>.

## 1. What retirement changes, and what it must preserve

Let an auxiliary edge `j=(s,v)` be frozen at its current value `z_j` with `0<z_j<1`. The full demand remains the count of all units ever born. The current active graph has demand reduced by the divergence of all frozen auxiliary values. The full cost remains

\[
 P=c^T f_{\rm ordinary}+\sum_{j\in J}a_jf_j+
   \sum_{j\notin J}a_jz_j.
\]

Removing the coordinate from the active graph is therefore not deletion of its already delivered commodity. Future numerical updates are circulations only on active edges. In particular they cannot alter a frozen value.

This distinction defeats the most immediate counterexample attempt. If frozen values were deleted from the full cost, or if future comparison flows could set them to zero, the global gap and comparison argument would change. The proposed definition does neither.

The existing exact flow register already supports this operation. In `current_checkpoint/priced_logarithmic_steps_from_raw_cycles.md`, Sections 8--9, a logical coordinate is

\[
 f_e={\rm base}_e+\sum_{q\mapsto e}h_q.
\]

An exact point read visits its complete current-copy list, including dormant copies. During deletion, every retiring copy transfers its signed register to the logical base and its absolute register to the drift bucket before the old image is invalidated. Thus the safe retirement transaction is:

1. Settle the preceding numerical transaction and read `z_j` exactly.
2. Record its immutable cost and divergence contribution.
3. Delete the active logical edge while retaining its old metadata through all real-copy callbacks.
4. Finish every signed and absolute transfer, then remove or mark stale its coordinate notification entries.
5. Permit the next query only after all affected-coordinate notifications settle.

These operations preserve every surviving logical value. There is no need to reroute the frozen flow through ordinary edges. The port-path construction in Section 3 of that same backend note maintains conservation of increments, and stores no primal flow on connector edges. It explicitly permits nonzero current logical divergence.

A new auxiliary unit can likewise be inserted with logical base value one. This is an external demand birth, paid separately, followed only by circulation increments. It is not an assertion that insertion at value one is itself a circulation.

## 2. The strong comparison survives every valid freeze

For each frozen unit retain `z_j`; for each active auxiliary unit take `min(f_j,1)`. Route each unit's remaining amount along a current ordinary shortest path. All remaining amounts are nonnegative. The result is a full feasible flow of the same demand and has cost at most `F`, because both its anchor and its ordinary shortest path cost at most that unit's anchor.

The difference from the current flow vanishes on every frozen coordinate. It is consequently a circulation in the remaining active graph. For an ordinary coordinate with slack `t=f_e+delta_e>0`, its comparison target is nonnegative, so

\[
 -\Delta_e/t\leq 2-|\Delta_e|/t.
\]

For an active auxiliary coordinate below one, the comparison leaves it unchanged. Above one, its barrier derivative is `-1/f_j`, and the same inequality applies. These statements do not require the ordinary current flow to be nonnegative; the allowed tiny negative excursion is sufficient.

With `A=1000`, there is therefore ample margin in

\[
 g^T\Delta\leq -\frac{AM(P-F)}{P-(1-\alpha)F}
                 +2M-\|W\Delta\|_1.
\]

When `P>(1+5 alpha)F`, this is at most `-||W Delta||_1`. A sound LOW result is impossible in that regime. This check uses only the number of active logical coordinates, bounded by `M`.

## 3. A remaining auxiliary unit certifies an unreported vertex

Circulation duality applied to a sound LOW result gives a potential whose ordinary reduced costs are positive. Scaling it by `r/(AM)` makes it a feasible lower-distance potential. All ordinary edges remain active, so deletion of auxiliary edges cannot remove a constraint needed to prove `phi(v)<=d(s,v)`.

For an unreported vertex there is at least one active auxiliary unit. After notifications settle it has weight below `2K`; otherwise it would be frozen. The auxiliary reduced-cost inequality and `r<=6 alpha F`, `F<=2M` give

\[
 a_j-d(s,v)\leq a_j-\phi(v)
 \leq O(\alpha K/A)<\sigma.
\]

Only this one remaining copy is needed. No inequality on any frozen coordinate is invoked. The same-anchor assumption for a vertex converts this to the desired certificate for that vertex's phase anchor.

This also explains why retirement of *all* its current units is required for a report. Reporting after just one of several degree units freezes would not pay the degree-volume charge used by the outer recursion.

## 4. Births inject only a harmonic amount of potential

The coefficient `AM` must be fixed for the lifetime. It is based on the announced local logical inventory allowance, not on the current number of active edges and not on the backend's larger flat representation.

After the first unit, every nonterminal settled state has `r>alpha F/4`. A new unit of anchor `a` changes the gap to `r+alpha a`, and adds `1/p` as its auxiliary barrier. Its positive injection is at most

\[
 4AM\,a/F+1/p.
\]

Since `a` is in `[1,2]` and `F` grows by precisely those anchors,

\[
 \sum_{\text{later births}}a/F_{\rm before}=O(\log(M+2)).
\]

The first unit initializes a separate nonempty lifetime state. Ordinary-edge births each add `O(log N)` to the potential. Thus all births together inject `O(M log N)`, even when degrees or the vertex set grow during a phase.

No oracle-loss factor is needed in this calculation. Inserting new units at already reported vertices can make future termination earlier, but does not invalidate this potential bound or require a second report of those vertices.

## 5. A direct lower bound that does not retain frozen barriers

Here is an explicit version of the polynomial-state argument, useful for avoiding circular reasoning. Assume the ordinary-slack guard `sum delta_e<=N^-20` and at least one unit. All positive costs are at least `N^-c`, so any nonnegative coordinate is at most `N^c(P+1)` after harmless changes to constants. The frozen positive cost does not weaken this upper bound.

Every ordinary negative logarithm and every auxiliary branch above one is bounded below by

\[
 -O(\log N)-\log(P+2).
\]

An auxiliary branch below one is positive and can be discarded for a lower bound. There are at most `M` such terms in total.

If `P<=4M+4`, all these negative terms have magnitude `O(M log N)`, while the nonterminal lower gap `r>alpha F/4` gives `AM log r>=-O(M log N)`. If `P>4M+4`, then `F<=2M` implies `r>P/2`, and

\[
 \Phi\geq (AM-M)\log P-O(M\log N).
\]

These two cases prove a uniform lower bound `Phi>=-O(M log N)`. Together with the upper bound from initialization and births they also prove `P<=N^C` for a fixed constant. The argument nowhere counts a barrier after it has been retired.

Moreover each remaining positive auxiliary barrier is at most `O(M log N)` after paying the other terms. Hence `f_j^-p` is polynomially bounded. This gives the required polynomial values of active weights, even though the integer exponent `p=Theta(log N)` requires longer temporary arithmetic.

## 6. The freeze bound is independent of the oracle

A valid freeze has true weight at least `K/2>1`, so its removed positive term equals

\[
 V_p(z_j)=\frac{w_j^{p/(p+1)}}p
         \geq \frac{(K/2)^{p/(p+1)}}p
         =\Omega(K/p).
\]

The final estimate uses `log K=O(p)`, which follows from the stated master-size parameter range. Summing the potential decreases due to freezes and discarding the other nonnegative decreases yields

\[
 \#\mathrm{freezes}\cdot\Omega(K/p)
 \leq \Phi_{\rm initial}+
       \sum\mathrm{positive\ injections}-\Phi_{\rm final}
 =O(M\log N).
\]

Substituting `p=Theta(log N)` and `K=Theta(sigma/alpha)` gives the stated count. This calculation concerns all retired auxiliary copies throughout the lifetime, including copies of already reported vertices, rather than only the set currently absent.

## 7. Numerical steps, the gap, and termination

For `x<=1`, the power barrier obeys

\[
 \frac{V_p''(x)}{(-V_p'(x))^2}=(p+1)x^p\leq p+1.
\]

For `x>=1` the same quotient is one. Although the second derivative jumps at one, the derivative is continuous, and a step with weighted motion `O(1/p)` stays in a constant-comparison neighborhood. The integrated Taylor remainder is therefore `O(p ||W h||_1^2)`, also across the join. The ordinary logarithms have the same bound with no extra factor `p`.

With the oracle's descent `g^Tz<=-beta R` and `eta R=Theta(beta/p)`, this gives decrease `Omega(beta^2/p)`. Concavity treats the global logarithm exactly to first order when its final gap is positive. If the proposed complete update instead crosses the stopping threshold, its coordinatewise feasibility still holds by raw absolute-motion control, and the algorithm uses that complete flow as an existence certificate.

The reduced-cost identity with a true shortest-path potential gives

\[
 P\geq\sum_v b_vd(v)-4\sum_e\delta_e.
\]

It remains valid for both active and frozen auxiliary values, since all such values are positive and their anchor reduced costs are nonnegative. Thus the stopping certificate is sound without an external fixed-demand flow instance.

For a decreasing-potential step, the positive relative gap increase is bounded by `O(beta/(Mp))`, since

\[
 AM\,\Delta r/r=g^Th+w^Th\leq\|Wh\|_1.
\]

Births add only `O(log N)` positive logarithmic gap variation. The polynomial upper/lower gap bounds then bound the negative variation too. This pays full repricings at relative gap changes of order `beta`; it does not require each individual accepted step to be cost-decreasing.

## 8. Finite arithmetic and the raw implementation boundary

The new detector uses polynomial-size real-coordinate values but may temporarily evaluate powers of `O(log N)`-bit rationals to exponent `O(log N)`. Their numerator/denominator bit lengths are `O((log N)^2)`, paid by polynomial logarithmic arithmetic per refresh. Rounded exported integer prices still have `O(log N)` bits.

The flow grid is selected only after bounding all integer raw denominators. Choosing each step as a power of two with weighted size `Theta(beta/p)` gives a uniform polynomial lower bound on step size. A sufficiently fine common dyadic grid then contains every initial value, step, slack offset, and frozen value. There is no independent coordinate rounding and therefore no conservation error.

An additional fixed-cost aggregate on raw forest paths, already supplied for the moving-box flow client, computes the complete proposed cost change before application. It is essential to keep this aggregate distinct from the stale gradient aggregate. Auxiliary retirement moves its exact cost to the immutable offset; it does not change the maintained full cost scalar.

The raw interface must process every operation at settled transaction boundaries. An intermediate forest path may have nonzero divergence and a negative affine gap. It may not be queried or logarithmically evaluated; the complete circulation is the object used by the proof.

Two minor clarifications are advisable:

* An ordinary edge born with slack `delta_0` lies below the example rearming threshold `5 delta_0/4`. Pay one initial rearm per birth, or initialize at a safe slack. Subsequent rearms are charged to separated weighted motion.
* The potential inventory `M` counts logical ordinary edges, auxiliary units, vertices, and at most `O(M)` port-path records. The backend's `M E^{O(1)}` flat occurrences are charged in time and space only. Including those copies in the coefficient `AM` would incorrectly reintroduce oracle loss into the reporting count.

## 9. Scope of this audit

The independent checks found no counterexample to the proposed single-lifetime freeze mechanism under its explicit interface. It remains necessary to supply the outer recursion's inventory, phase-restart, accuracy, and path-reporting accounting. In particular, the count here pays degree volume at a vertex's first report, while edges inserted later at that vertex require separate input-volume accounting. This note does not infer any global shortest-path exponent from the detector alone.

## 10. Subsequent audit of the explicit raw-cycle bridge

The later `raw_cycle_to_frozen_detector_bridge.md` supplies an explicit instantiation of the numerical interface. Its main constants and work dependencies pass the following independent calculation.

Write `beta=1/(256R)`, `xi=beta/10^5`, and `kappa=r/rhat`. The scaled-gradient identity and integer rounding give

\[
 |\gamma/H-\kappa g|\leq 3\xi w.
\]

The true logical weighted traversal length of a raw answer is at most `2V/H`. Acceptance requires

\[
 T/V\geq 1/(16R)=16\beta.
\]

Consequently its oriented circulation satisfies

\[
 -g^Tc\geq\frac{16\beta-6\xi}{1+\xi}\frac VH
          \geq7\beta V/H.
\]

With certified raw denominator `R_raw=2V/H`, this is stronger than the required descent. Conversely, a true ratio at most `-1/4` lifts through the port paths to an integer-priced comparison with absolute ratio at least `1/5`, because the connector cost is negligible at the chosen common scale. The backend must then return raw ratio at least `1/(5R)`, which is above the LOW threshold `1/(16R)`. Both directions use the before-cancellation denominator.

There is no circular repricing charge. The potential argument first proves

\[
 T=O(Mp\beta^{-2}U).
\]

The total positive logarithmic gap variation from numerical motion is then at most `O(T beta/(Mp))=O(beta^-1 U)`; births add `O(U)`. Endpoint polynomial bounds pay the negative variation. Refreshing the global gap at relative changes `Theta(beta)` therefore requires at most `O(beta^-2 U)` complete passes. Representation maintenance itself changes neither the true flow nor the full objective, so it cannot generate additional gap variation. Each pass may pay its full occurrence and callback cost under the imported envelope.

For the `S=N^C` label-master extension, choose an actual fixed polynomial event horizon first, then the slack exponent and exported-label scale, and finally a sufficiently large fixed `C`. The allowed backend horizon `S^100` is an upper allowance; it need not be used as the number of actual client events when selecting the slack exponent. Since `R(N^C)=N^{o(1)}` for every fixed `C`, this order leaves the potential, grid, and word-size choices acyclic and preserves the four-fifths logarithmic envelope.

The outer accounting has separately been audited in `frozen_sssp_outer_independent_audit.md`.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
