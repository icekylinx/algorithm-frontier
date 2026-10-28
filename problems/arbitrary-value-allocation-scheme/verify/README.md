# Verification and scope

The [complete PA proof](../proof.md) and [native realization](../reference-realization.md)
provide the mathematical construction. The [reference API](../reference/README.md)
and exact finite checker provide a separate executable form.

## Mathematical review

Internal review covers the complete original optional-player theorem: an
actual player basis, arbitrary player/type values, eligibility, independent
recipient polymatroids, optional unused capacity, nonnegative setup and
assignment costs and one shared exact scalar budget. It checks the minimum
setup affordability gate, integer-target capping, first-reaching profile
witness, exact occupied-bin endpoints and actual joint original-resource LP.

Disposal completion, complement duality and all lower-prefix constraints
are enforced at one integral full-total intersection face. One actual cost
objective preserves assignment cost and the fixed setup fee. Integral
big-boundary prefixes eliminate the large-value rounding loss; only the
small group pays the stated loss. The full accuracy inequality, pruned
profile traversal, both state-count envelopes and all-input one-sided
original-value-grid optimization are checked. The integer comparator is
not replaced by the additive dependency's fractional comparator.

## Executable evidence

```sh
python3 problems/arbitrary-value-allocation-scheme/verify/check_scheme.py
```

The [independent checker](check_scheme.py) supplies:

- 42 original instances/accuracy choices, 168 target calls with 78 actual
  outputs and 90 independently checked sound failures, and 42 original-grid
  optimizations compared with exhaustive original integer allocations.
- 305 inspected profiles and 26 direct fractional/integer recoveries,
  checking every original rank, actual budget, simultaneous lower prefix
  and no-greater assignment cost.
- 39 independently enumerated occupied profiles; exact small/internal/last
  bin endpoints; very large capped values; and a direct example showing
  capping's failure to preserve fractional full-target feasibility.
- 18 comparisons with an independent uncompressed exact vertex enumerator,
  including fixed coordinates, lower-dimensional faces, exact cost optima
  and inconsistent scalar bounds.
- Two deliberate fractional cases with genuine small-service requirements
  and with two players sharing the same original unit resources. Actual
  joint cost optimization must select the cheaper legal original assignment.
- 101-bit supplies, 121-bit accuracy with huge absent-bin indices, a deep
  occupied iterator, original player loops, unaffordable setup gates,
  rank-zero and empty-type cases.
- A producer-disabled original output verifier, four forged outputs and
  eight malformed input/witness rejections.

The exhaustive integer comparator reads original bases, resource ranks,
eligibility, values, setup, costs and budget. It uses no backend binning,
profile, LP, rounding or target helper. The independent vertex comparator
uses the canonical uncompressed Gaussian/vertex primitive, not the native
fixed-coordinate substitution. Numeric count enumeration occurs only in
the tiny independent integer test oracle, never in the backend. Finite
checks do not prove the general theorem or its asymptotic state counts.

## Costs and remaining boundaries

Original complete rank tables are charged input. The native program really
streams occupied profiles and original-grid targets, with original output
recovery and no binary resource-unit expansion. Its LPs stream exact active
systems after fixed-coordinate substitution. Their potentially exponential
basis count is explicit and separate from PA's paid polynomial LP/SFM and
weighted-intersection primitives. Rational workspace and determinant-based
bit lengths are polynomial in the encoded input, targets and full accuracy.

Multiple exact independent budgets, fractional player selection and extra
constraints coupling resource types are outside this model. The named
polynomial primitives are mathematical dependencies; a finite reference
implementation with a larger time factor does not make the mathematical
interfaces unresolved. The ICALP 2025 cost-preserving-rounding paper is a
public antecedent, not a black-box theorem for this complete profile model.
Repository surface checks do not establish mathematical correctness;
proof-assistant formalization and external peer review are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
