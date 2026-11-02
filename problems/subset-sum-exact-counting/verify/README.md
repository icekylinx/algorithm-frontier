# Verification scope

Attribution: **icekylinx and GPT-6 Astra Pro**. Apache-2.0.

Run from the repository root with standard-library Python and assertions
enabled:

```sh
python3 -B problems/subset-sum-exact-counting/verify/check_trace_and_threshold.py
python3 -B problems/subset-sum-exact-counting/verify/check_weighted_trace.py
python3 -B problems/subset-sum-exact-counting/verify/check_activity_lifting.py
python3 -B problems/subset-sum-exact-counting/verify/check_improved_filter_certificate.py
```

The trace suite checks exact conjugate identities, noisy rounding controls,
CRT recovery, deterministic-tag bins, threshold recursions and disjoint
interval identities for every original subset in its tested cases. Negative
controls reject treating a trace as the total count or assuming isolation.

The weighted suite checks signed traces, finite-color extraction and exact
second moments by independent enumeration. The activity suite checks 2,800
prime-residue reductions and 400 signed weighted CRT reconstructions against
original subset sums and weights. These are genuine original-input tests;
they do not substitute an approximate answer for an exact count.

Some small conjugate/noise controls use floating-point complex arithmetic.
They are finite formula controls, not rigorous analytic error estimates.
The separate parameter checker uses exact `Fraction` intervals, rational
Taylor remainders and outward rounding. It verifies the changed outer
quadrature and complete exponent/cap ledger, accepting the named unchanged
analytic-strip and inner-quadrature bounds from the pinned source. Its
current report is written to `improved_filter_results.json`.

None of these programs implements the asymptotic checksum estimator, alias
extraction engine or full exponential-time algorithm. The mathematical
proof and explicit external source contracts supply those scopes. No
asymptotic theorem is established by finite enumeration, and no external
peer review or proof-assistant verification is claimed.
