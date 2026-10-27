# Exact one-order mixed-prefix reference

[prefix.py](prefix.py) implements the bounded
[one-common-order theorem](../manuscripts/exact-weighted-prefix-quotas-max-target.md).
The [realization proof](../reference-prefix-realization.md) derives its original
resource LP and exact signed recovery. It does not implement the whole prefix,
laminar, sparse-row or kernel family.

`Prefix(rank, weights, costs, rows=(), mandatory=True, allowed=None, maximize=False)`
takes one complete original integral polymatroid rank table. Coordinates are
ordered by their original IDs, starting at zero. Weights are nonnegative
integers, scalar coefficients are exact signed `int`/`Fraction` values, and
each quota is `(prefix_length, relation, target)` with relation `<=`, `=` or
`>=` and a nonnegative integer target. Prefix length zero denotes the empty
prefix. Eligibility, when supplied, lists original coordinate IDs.

`solve()` returns `Solution(original_counts, exact_scalar)` attaining the
original optimum, or `None` for original infeasibility. The default minimizes
the scalar; `maximize=True` maximizes it. `verify(solution)` independently
checks every original rank, quota, eligibility, count and scalar identity.
Mandatory mode retains the original rank-table total, even after masking.
Optional mode adds one internal zero-cost disposal coordinate and drops it
from the output. All real zero-weight coordinates retain their actual costs.

The client performs actual upper/lower dominance, safe original upper masks,
shared active/passive copying, occupied support-and-weight profiles and exact
resource/partition recovery. `profiles()` streams binary class multiplicities
under the charged mass and count caps. `realize(profile)` validates such a
profile and computes its exact signed optimum or proves its face empty.
The shared copied resource is enforced by original-subset rows; no complete
rank table on the doubled ground is constructed.

`last_trace` records streamed profiles, failed numeric filters, empty integral
faces and actual recovered profiles. Its counters charge failures as well as
successes. The reference retains one current profile and one LP tableau,
with no rank-sized, target-sized or unit-copy array. The canonical iterative
occupied-profile iterator is reused after exact mass normalization.

The native LP is the canonical exact Bland simplex. Its potentially
exponential basis factor is separately charged from the mathematical theorem's
paid polynomial integral-polymatroid optimization. The native code still uses
polynomial workspace in the complete-table input and numeric bit lengths.
The one-order exponential profile bound depends on the largest numeric target;
it is not polynomial in that target's bit length. No additional independent
scalar budget or second resource polymatroid is supported.

```sh
python3 -B problems/weighted-prefix-quota-frontier/verify/check_prefix.py
```

The checker compares actual original count vectors and signed optima. Its
small enumeration is separate from the native solver, and its binary-large
fixtures do not enumerate counts or units.

**Attribution:** Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
