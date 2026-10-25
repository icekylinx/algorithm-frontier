# Independent audit of approximate available-bundle allocation

**25 October 2026. Mathematical audit passed.** The manuscript audited
is `approximate_available_bundle_oracle_allocation.md`. This review
covers the new oracle, numerical-quality and precision interfaces;
the audited player-matroid exchanges and integer-signature count
remain named imports.

## 1. The strict certificate and fresh scans

An oracle satisfying (A1) and returning value below \(B\) certifies
the available optimum strictly below \(B/\lambda\). Restricting
each feasible set in a convex decomposition of the perspective variable
to available items preserves feasibility and proves (A4).

Multiplying the eligible-mass lower bound by \(T-B/\lambda\)
requires nonnegativity; the manuscript explicitly assumes
\(B\le\lambda T\). Strictness at equality is still valid because
eligible mass is positive and the outside-value bound is strict for
every positive-coordinate eligible player. Thus the oracle-relative
certificate is sound, including the exact boundary.

Restarting the player scan after a state-changing microstep is
necessary and included. Approximate returned values need not be
monotone under deleting available items. Earlier layers retain their
mathematical availability inequalities because their forbidden sets
and eligible player sets stay unchanged; no monotonicity of returned
witnesses is assumed.

## 2. The quality curve and uniform rank exponent

Physical minimal bundles and blockers are unchanged, so the sharp
coefficient is still \(C(B,u)=\max\{u,2B+\min(u,B)\}\).
For \(\tau=1/\lambda\) and \(\rho=(r-1)/r\), solving
\(\tau B+\rho C(B,u)=T\) in the three regimes
\(u\le B\), \(B\le u\le3B\), and \(u\ge3B\)
gives exactly (A11). Its boundaries agree at
\(u=T/(\tau+3\rho)\) and
\(u=3T/(\tau+3\rho)\). For \(r\ge2\) a positive
solution exists precisely when \(u<T/\rho\). For rank one the
answer is \(\lambda T\), without an item-size restriction, as
appropriate for an approximate one-player optimization problem.

On a positive singleton, a feasible \(\lambda>0\) oracle must
return that singleton if it is permitted. The fat graph is therefore
constructed exactly. The previous matroid-union and configuration-LP
arguments remain valid.

For \(d=\tau+3\rho\), \(B_0=T/d\), and
\(B=T/(d+\eta)\), the coefficient \(\overline C=2B+B_0\)
bounds the sharp coefficient on the small instance. Direct subtraction
gives

\[
 T-\tau B-\rho\overline C=(\tau+2\rho)(B_0-B).
\]

Since \(\tau\ge1\ge\rho\),
\(\tau+2\rho\ge3d/4\). Also
\(\overline C\le3T/d\). The gap divided by
\(\overline C\) is therefore at least
\(\eta d/[4(d+\eta)]\ge\min\{\eta,1\}/8\).
Thus \(\gamma=\min\{\eta,1\}/16\) is valid uniformly in
\(\lambda\), and a smaller derived matroid rank only helps.
There is no additional inverse-\(\lambda\) factor hidden in the
rank exponent. The oracle cost and numerical parameter bits remain
explicitly paid.

## 3. The knapsack implementation and workspace

After singleton-infeasible items are removed, \(V_{\max}\) is a
lower bound on the available optimum. Rounding profits at scale
\(K=\kappa V_{\max}/m\) loses less than
\(mK\le\kappa\mathrm{OPT}\) from an optimal feasible
bundle. Minimum true cost for each rounded profit therefore yields
the stated \((1-\kappa)\) guarantee. The integer profit range,
conservative time bound, rational arithmetic, and reconstruction in
the manuscript are valid. The empty-positive-item case and zero costs
are handled by its singleton feasibility check.

The chosen \(\kappa\) gives
\(\lambda^{-1}-1\le\zeta/2\), and
\(\eta=\zeta/2\) supplies the requested
\(4-3/r+\zeta\) ratio. Exact rank-one knapsack is not being
solved in polynomial time. Ordinary allocation storage is polynomial;
total storage includes the oracle workspace. The profit DP uses space
polynomial in input and \(1/\zeta\), not necessarily in the
encoding length of an arbitrarily tiny accuracy parameter alone.

## 4. Public comparison

The oracle metatheorem is not a first-approximation claim for each of
its applications. `item_matroid_allocation_public_scope_audit.md`
records public knapsack comparisons obtained by fixed common profit
rounding and exact dynamic programming for the rounded objective.
That method preserves the truly minimum-distance hyperedge interface
of the original Polacek--Svensson search. Merely inserting a generic
approximate oracle into that search would not automatically preserve
its truncation invariant.

