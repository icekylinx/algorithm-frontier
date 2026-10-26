# The exact-factor-two endpoint for arbitrary unrelated allocation


The strictly-sub-two global bases in the near-two theorem require a
fixed positive approximation loss. At the endpoint, the same joint
resource LP and rounding give exact factor two in
2^q poly(H) time and polynomial space. This holds with an arbitrary
original player matroid, arbitrary player-type values, arbitrary
integral recipient polymatroids, and one exact combined budget for
nonnegative selected-player setup and assignment costs.

The result is a direct exponential enumeration bound. It makes no
claim that the base two is optimal at approximation factor two,
and is not obtained by substituting zero accuracy into a positive-gap
formula.

## 1. Fixed roles are polynomially optimizable

Use the model and notation of
[Unrelated-value allocation with one shared setup and assignment budget](setup-budget.md). With all setup fees zero,
this includes its ordinary exact-assignment-budget specialization.
First check minimum-setup basis feasibility and retain its legal
zero-resource allocation. Delete original player loops and let q
count the remaining candidate players.

For each mask of the positive original pair values and each nonempty
light-role set I subseteq P, fix Q=I in SD7--SD9. Keep the
zero-service dual-matroid dummy on all positions, including I.
Solve the exact rational LP

```math
\max t\quad\text{subject to }(x,y)\in X_I,\quad t\ge0,\quad
           \sum_j v_{pj}x_j(p)\ge t\quad(p\in I).
 \tag{X2-1}
```

An infeasible role LP is skipped. A feasible one has a finite maximum:
I is nonempty, real resource ranks are bounded and dummy service is
zero. All constraints, rank separators, coefficients and an exact
optimizing witness have polynomial binary complexity. A real
service upper bound is sum_j(max_p v_pj)f_j(P).

Apply the signed-cost count-floor and utility rounding of SD6 once
to its optimizing joint point. Extract an actual original M-basis
from the integer dummy-free players. The actual original setup and
assignment cost is at most C, and its value is at least

```math
\min\{a_H,t-u_L\}.
 \tag{X2-2}
```

Only legal integer original solutions are recorded. Their actual
minimum utility is computed exactly, and the best is returned.

For I empty, use the exact full-total all-heavy/dummy gate from SD8.
There is no light-service maximization or artificial infinite target
in this case.

## 2. An optimal original solution supplies one enumerated case

Discard zero-valued original assignments first; their nonnegative
original costs make this safe. The zero-service auxiliary dummy is
retained, including all of its negative setup credits.
Assume OPT>0 and choose the enumerated mask induced by
theta*=OPT/2, with equality on the heavy side. In an original integer
optimum on basis B*, let F* be its heavy recipients and
I*=B*\F* its light-only selected players. Put dummy units on the
dual basis P\B*. Keep one original heavy unit at every player in F*
and all original allocations on I*.

The resulting point respects the original shared resource ranks and
the affine setup budget; no negative dummy credit is lost. If I*
is nonempty, it is feasible in X_(I*) and supplies t=OPT in X2-1.
The computed optimum t is therefore at least OPT. Since
u_L<theta*<=a_H, X2-2 gives utility at least OPT/2.

If I* is empty, the original heavy cover and canonical dummy basis
are an affordable witness for the all-heavy/dummy gate, whose
recovered original basis has value at least theta*. Zero optimum
is covered by the initialized legal solution.

Thus the output is an exact factor-two approximation for every
feasible instance of the stated model, with the exact original
combined budget.

## 3. Time, space and comparison with the near-two algorithm

There are at most qm+1 pair-value masks and 2^q role sets. Each
case uses polynomial exact LP, rank-oracle, intersection, rounding
and basis-extraction work. Cases are streamed, keeping only one
current workspace and the best actual allocation. Total time is

```math
2^q\mathrm{poly}(H),
 \qquad\text{space }\mathrm{poly}(H).
 \tag{X2-3}
```

For any fixed rational eta>0, the accepted gap/global-cover
construction instead gives factor 2+eta in
B((2+eta)/eta)^(q+o(q)) poly(H), with B<2. It saves a fixed
exponential factor in q while keeping the original exact
constraints. The present endpoint removes the approximation slack
and returns to direct role enumeration.

The exact-two compulsory two-valued theorem remains stronger in
time: it attains base 50/27 by exact integer quota recovery.
There is no reason to replace that special theorem with X2-3.
No fixed base below two is proved here for exact factor two on
arbitrary unrelated values.

This is a same-model constructive endpoint and comparison baseline,
not an exhaustive public-priority claim. The actual joint-mask,
count-floor, signed-budget and dummy-free recovery proofs are the
reviewed prerequisites cited above.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
