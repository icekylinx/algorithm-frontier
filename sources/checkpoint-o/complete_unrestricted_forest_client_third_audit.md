# Third audit of the unrestricted-receiver forest client

**25 October 2026. Independent mathematical and accounting audit passed.**

This note checks `complete_unrestricted_forest_one_sided_client.md`.
The whole ambient ordinary allocation support must be a forest. The
result is not obtained by selecting a spanning forest from a cyclic
ambient support, and gives no general-graph maximum-matching exponent
improvement by itself.

## 1. Direct separation is complete on the ambient forest

Orient each allocation coordinate from its row to its bin, and each
slack coordinate from an auxiliary vertex \(z\) to its bin. A feasible
difference has zero divergence at rows and bins. Summing the row and
bin conservation equations also gives zero divergence at \(z\).
Choosing the sign-compatible residual direction of each nonzero
coordinate therefore gives a nonnegative circulation.

Simple-cycle decomposition uses only those chosen signs, so it
preserves both signed slack gain and the one-sided charge exactly.
It never inserts an opposite-direction copy of a coordinate as a
cancellation. A simple cycle containing \(z\) has exactly one entering
and one leaving slack arc. Its ordinary part is a simple bin-to-bin
path. In the ambient forest that path is precisely the unique ordinary
path queried by the dynamic program. Ordinary-only cycles have zero
slack gain and cannot provide a positive-ratio obstruction.

Consequently a feasible comparison of ratio greater than one half
contains an ordinary path of ratio greater than one half. The
conservative-price search detects every such path. An empty search
therefore gives the claimed direct LOW certificate, with no old-label
feasibility assumption. This is the essential completeness property
that would be false for a forest selected from a cyclic ambient graph.

## 2. Opening every receiver preserves the local data structure

The cluster join formulas represent simple underlying paths by joining
two disjoint child pieces at their unique common boundary. Allowing
both directions of a base incidence only makes two directional scores
finite; it does not create a permitted repeated-edge walk. Every
ordinary backtrack has positive donor cost and can be erased without
weakening a shortest-path offer.

The physical allocation coordinate still has one watcher owner. Its
forward directional buffer decreases by the transfer, while its
backward buffer increases by the transfer. This identity does not use
receiving-edge tightness. A register-price decrease after a receiving
step is a valid ordinary DP point update. No potential monotonicity is
needed for either lazy propagation or the hysteresis count.

## 3. The fixed numerical floor does not hide a third outcome

A passing path has source and target reciprocals satisfying
\(1/s_a>(5/3)/s_b\). With the admitted step normalization, the
source slack increases and the target slack remains above the old
source slack. Thus the global minimum slack never decreases on
numerical steps.

For each donor on an accepted path,

\[
                  1/(4x_e)\le\bar c_e/H<3/(4s_a),
                  \qquad x_e>s_a/3.
\]

In addition, the path normalization satisfies
\(V_{\rm up}\ge1/x_e\), so
\(\eta V_{\rm up}\le1/256\) implies
\(\eta\le x_e/256\). This is the inequality that justifies the
main note's stated post-step donor bound
\(x_e-\eta>(255/256)s_a/3\). Using only
\(\eta\le s_a/256\) would give a weaker constant, but the stronger
coordinate bound is available directly.

Therefore a donor cannot fall to an arbitrarily small scale below
the initial minimum slack. Coordinates already below that scale cannot
be donors and can only remain fixed or increase. Choosing declared
floors below the initial guarded range rules out permanent numerical
floor failure. A polynomial sufficiently fine common grid exists
because all reciprocal and path-sum bounds remain polynomial in the
declared word-scale parameter. Upper guards can be chosen strictly
above row totals and bin capacities.

## 4. Objective, register and structural work

Each accepted step gains an absolute positive constant in the
slack-log objective. Its finite width gives the stated numerical-step
bound. Every step has bounded total negative allocation log variation;
telescoping bounds positive variation by this plus the initial and
external-coordinate contributions. Hysteresis then charges all
register events. Nothing in this variation argument relies on a
fixed potential or a permanent donor/receiver role.

For a dynamic structural transcript, the accounting explicitly includes
every changed bin slack in \(A_s\), every external allocation record
in \(A_x\), and every topological record in \(A_T\). Retiring a
high-degree vertex must enumerate its incident cuts. Processing all
cuts before links makes every link an edge of the final settled forest
and allows ordinary connectivity checks. External feasibility and the
polynomial guarded range are assumptions of the supplied ledger
operation, not silently constructed by this client.

These counts justify the near-linear total bound in the explicit
transcript size. The optional implicit fresh potential at LOW is
valid, but its full materialization is not charged on every step.

No remaining local correctness, guard, or event-accounting obstruction
was found within the stated forest-support contract.
