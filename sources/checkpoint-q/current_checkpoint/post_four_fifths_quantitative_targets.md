# Quantitative targets after the 4/5 checkpoint

**Conditional accounting, 24 October 2026.** These are interfaces that
would improve the current candidate, not established new matching
bounds. The accepted research envelope remains 4/5.

## 1. Separate route quality from maintenance work

Write U for the master size logarithm, h=Theta(log(U+4)), x=log k,
d=Theta(U/x), and g=(p+r)h. Static work contains U/p+U/r+r^2h.
Retain selected recourse U/K+g. Suppose a NEW provider had local work
exponent K^a g and local raw-quality exponent K^b g, for fixed a,b>=0.
The current provider has a=b=1. All lifetime and notification
interfaces would have to be preserved separately.

A total logarithmic budget A pays
\[
 x,\ U/p,\ U/r,\ r^2h,\ K^ag,\ (U/x)(U/K),\ (U/x)K^bg.        \tag{1}
\]
Thus p,r=Omega(U/A), K=Omega(U^2/A^2), and x=O(A), giving
\[
 \begin{aligned}
 A&=\Omega(U^{2/3}h^{1/3}),\\
 A&=\Omega(U^{(2a+1)/(2a+2)}h^{1/(2a+2)}),\\
 A&=\Omega(U^{(2b+2)/(2b+3)}h^{1/(2b+3)}).
 \end{aligned}                                               \tag{2}
\]
These optimize charged upper expressions, not actual algorithm
lower bounds. A mechanism changing (1) can evade them.

## 2. The conditional 3/4 target

If local work remains K g but raw-quality growth is independent of K,
then a=1,b=0 gives A=U^{3/4}h^{1/4}. Choose
\[
 t=\Theta((U/h)^{1/4}),\quad p=r=t,\quad K=t^2,\quad
 x=\Theta(U/t),\quad d=\Theta(t).
\]
Local K g=t^3h=Theta(U/t), propagated dU/K=Theta(U/t),
while full quality d g=t^2h and construction r^2h are smaller.
Even b=1/2 with a=1 gives this same target, because
d sqrt(K)g=t^3h.

An improved cumulative-length invariant is therefore useful even
if the old larger local congestion work remains. Exact telescoping
alone does not provide that invariant; see
[recursive_cycle_quality_obstruction.md](recursive_cycle_quality_obstruction.md).
Ordinary repair-window reparenting also does not provide it; see
[repair_window_depth_tradeoff.md](repair_window_depth_tradeoff.md).

## 3. The conditional 2/3 target

If a<=1/2 and b=0, the dominant expression in (2) is
A=U^{2/3}h^{1/3}. Choose t=Theta((U/h)^{1/3}), p=r=t,
K=t^2, x=Theta(U/t). Then U/t=t^2h, local sqrt(K)g=t^2h,
full quality d g=t^2h, and propagated dU/K=U/t all fit.

A short-route provider whose selected recourse has logarithm O(g),
avoiding U/K entirely, would also allow constant repair depth and
reach this conditional balance. Static degree-band work itself has
U/r+r^2h>=Omega(U^{2/3}h^{1/3}); further improvement would require
changing that currently charged construction too.

The stored-label guard would still fit: b_*=O(Ut), x=Theta(U/t),
and b_*/x^2=O(t^3/U)=O(1/h) in the 2/3 case. This only checks one
necessary quantitative condition; it does not supply the missing
dynamic algorithm.

## 4. Current partial progress

[central_greedy_recoursing_under_splits.md](central_greedy_recoursing_under_splits.md)
proves small central-ID recourse and short distances via exact greedy
girth repair. It lacks the fast distance tests, maintained route
congestion, and notifications; its tree example isolates that gap.

[congested_greedy_support_and_dynamic_boundary.md](congested_greedy_support_and_dynamic_boundary.md)
adds bounded native edge congestion, but exhibits a polynomial
violation of the additive ambient contract even with degree-three
selected and ambient graphs. The stronger example in
[projected_central_provenance_congestion_obstruction.md](projected_central_provenance_congestion_obstruction.md)
realizes literal first-touched prefixes and each demand's own genuine
central edge through legal native splits. It remains an obstruction
to the unchanged greedy selection, not to every possible initializer
or ambient-aware maintenance algorithm.

[initial_route_projection_updates.md](initial_route_projection_updates.md)
keeps preliminary paths short using one fixed initial table and
pays the local anchor scans. Its projected updates involve
multiple-origin incidence extraction, beyond ordinary native splits.

[nonuniform_fractional_path_selection.md](nonuniform_fractional_path_selection.md)
and [compressed_fractional_path_extraction.md](compressed_fractional_path_extraction.md)
supply deterministic fractional-route selection and short-inventory
extraction. The quantitative fractional-flow provider is still required.

[potential_bypass_limits_in_matching_clients.md](potential_bypass_limits_in_matching_clients.md)
checks a different possible improvement. A shortest-path shortcut is
valid for a supplied nearly conservative ordinary gradient, but the
current exchange client violates that hypothesis at its literal
initialization. A legal top state also has persistent large potential
defect. A new charged centrality invariant would therefore be required.

None of these partial statements proves a 3/4 or 2/3 matching
algorithm. They identify exact proof obligations for continuing
the unrestricted general-graph objective.
