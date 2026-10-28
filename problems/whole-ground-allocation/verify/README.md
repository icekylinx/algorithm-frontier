# Verification and scope

The [main proof](../proof.md) and [reference realization](../reference-realization.md)
cover the transfer family and its six canonical components: weighted selection,
adaptive residual budgets, streamed global conversion, rational comparator
recovery, integer quotas and the model-specific transfers.

## Mathematical review

Internal review covers the complete shared family, including exact first-
crossing words and unfinished states, paid selector failures, unchanged
protected completions under adaptive budgets, local cover construction,
count profiles/product streaming, polynomial workspace, fixed-family
rational reoptimization and every small-quota endpoint. The corank-profile
and selector-cost companion proofs have matching oracle/grid/comparator
interfaces. Sharp Gamma-based global displays retain fixed rational
tradeoff parameters; variable binary inputs use the stated supplied
rational upper-bound alternative.

Actual model-specific proofs have been checked for one-value budgeted
allocation, compulsory two-value budgeted allocation, arbitrary intrinsic
values with residual heavy completion, two-size scheduling, splittable
selected flow, explicit adaptive scenarios and the shared setup/routing
budget. Their original ranks, exact scalar budgets, mandatory totals,
resource separation and fixed benchmarks are retained. Disposal/complement-
prefix rounding preserves one true cost objective. The balanced hidden-
subset lower bounds preserve valid ranks and force the hidden set only
for the stated strictly better factors in the deterministic oracle model.
No optimal exponential base or explicit-eligibility hardness follows.

## Executable evidence

```sh
python3 problems/whole-ground-allocation/verify/check_selection.py
python3 tools/verify_profile_certificates.py
```

The [reference backend](../reference/README.md) executes actual prefix-free
omission, streamed greedy block covers and exact rational search. The
independent checker supplies:

- 180 complete first-crossing languages against all finite binary prefixes,
  checking prefix-freeness, exact Bernoulli mass and unfinished-state bounds.
- 240 original weighted packing gaps against exhaustive original selected
  sets, including 120 calls with certified weighted two-matroid selectors.
  Exact algebraic-power comparisons check node and prefix-state accounting.
- 108 local greedy containment covers with exact minimizing seed sizes,
  coverage and size/weighted inequalities; 78 full streamed seed families
  covering every omitted set on grounds up to twelve elements.
- 80 rational-comparator recoveries with deliberately nonmonotone weak
  answers, plus zero optimum and a binary-large denominator bound.
- 24 native shared-setup/routing-budget flow gaps, compared with independently
  computed original set rates on private-edge networks. These use the actual
  Farkas separator, prefix recursion and exact primal/dual recovery.
- Explicit failed selector and zero-deficit counts, an actual two-element
  prefix deletion, huge binary ratio counters, and seven malformed inputs.

The checker enumerates selected sets and all finite binary words only as
independent comparators. The backend itself uses the actual budget-pruned
prefix DFS. It stores local covers and streams profiles/products, rather
than storing an exponential global seed family. The native flow comparator
uses original capacity, fee and charge data directly. These finite checks
do not prove the asymptotic transfer or validate arbitrary external oracles.

The existing profile checker separately checks integer-quota arithmetic
for `d=2,...,30` and every `d<K<=399` (11,107 cases), including small-target
one-unit identities. It does not execute allocation recovery or replace
the new global-conversion checks.

## Model and implementation boundaries

Generic runtime claims include the declared selector, separator and
extension work, their bit lengths and witness recovery. The native flow
adapter uses the existing finite Bland simplex, with its separate
potentially exponential pivot bound. It executes actual omission but does
not supply a polynomial LP implementation. The generic wrapper accepts a
supplied rational admissible base; arbitrary algebraic-input manipulation
is not implemented.

The reference does not implement every allocation/scheduling rounding and
recovery algorithm. Those retain their complete mathematical constructions
and named paid LP/SFM/intersection/decomposition dependencies. Original
model distinctions remain essential: adaptive versus common routing,
compulsory versus selected players, one scalar budget versus several,
intrinsic versus unrelated value classes, binary multiplicities versus
explicit grounds. Independent intrinsic-value family companions are not
certified merely by their shared terminology.

The [source map](../sources.md) records the dependencies and attribution.
Repository checks validate links, notation and generated surfaces rather
than mathematical correctness. External peer review and proof-assistant
verification are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
