# Independent audit of the joint-owner sharp-quality addendum

**25 October 2026. Audit passed.** The manuscript reviewed is
`joint_owner_sharp_quality_addendum.md`.

The independent set \(J_i\cup A_i\) has rank
\(k-s+a\), so eligible fractional mass is at least
\(w-a\). A proposed failed growth test with
\(y\le\gamma w\), \(a\le y\), and \(\gamma\le1/2\)
makes this mass strictly positive. The strict lower cover bound is
therefore applicable, including when the available-bundle guarantee
is approximate.

With \(L=T-B/\lambda\ge0\), the difference of lower and upper
cover bounds is at least

\[
 [L(1-\gamma)-C(\rho+\gamma)]w
   =[\Delta-\gamma(C+L)]w.
\]

Thus the stated \(\gamma\) gives a contradiction whenever
\(\Delta>0\). The failed certificate uses the actual independent
set \(J_i\cup A_i\), not the smaller old individual-eligibility
set. The companion joint-owner proof already shows that every retained
layer's joint eligibility and lower maximality survive an earliest
single exchange.

At the exact boundary, an empty stable new layer has both \(y=0\)
and \(a=0\): free candidates are handled immediately and never
stored as unblocked persistent centers. The strict lower bound then
contradicts \(s/w\le\rho\). This validates the same positive-
coordinate composition count and exact rank-exponential branch.

For the fat-wrapper uniform-error calculation, the previously audited
gap estimate gives \(\delta\ge a_0/8\), where
\(a_0=\min\{\eta,1\}\). Since \(\rho\le1\),

\[
 \frac{\delta}{2(1+\rho+\delta)}
   \ge\frac{a_0}{32+2a_0}\ge\frac{a_0}{34}.
\]

The choice \(\gamma=a_0/64\) is consequently conservative.
Replacing the original rank by a smaller derived rank decreases
\(\rho\); replacing \(\overline C\) by the actual smaller
star coefficient increases
\((L-\rho C)/(C+L)\). Hence the uniform bound is not lost in
the union reduction. The rank-zero and rank-one branches are handled
explicitly, and no extra inverse-\(\lambda\) enters the rank
exponent.

This verifies a stronger search invariant at the same quality/time
scale. It does not establish geometric early-layer collapse for a
joint free family. The structural examples and polynomial-time gate
in `joint_owner_layer_batching_gate.md` remain unchanged.

