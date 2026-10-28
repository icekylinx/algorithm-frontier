# Verification and scope

The [main proof](../proof.md), [optional-player adapter](../player-selection.md),
[exact-half endpoints](../exact-two-boundaries.md) and
[reference realization](../reference-realization.md) have separate mathematical
and executable roles.

## Mathematical review

Internal review covers the complete canonical family: all value splits,
engineered workload and fixed-family fractional comparators, original
resource recovery and largest-light-unit loss, derived dual-union ranks,
union-basis spanning and original completion containing the retained light
basis. Forced loops and original resource restrictions are kept distinct;
no original resource is contracted after deleting light candidates.

The exact-half XP, zero-corank and quantified-margin endpoints use their
own half-optimum threshold. The unrestricted exact-half FPT question remains
unresolved. The two-unit nonmatroid example and its private-resource
strengthening, tiny numerical-slack limitation and modular-bonus limitation
have been checked. The refined-parameter-zero hidden ranks preserve the
near-two threshold convention and only prove deterministic oracle barriers
for strictly better than two, not exact two or explicit-input hardness.

The published fixed-slack compulsory-player fallback and the optional-player
dummy-dual transfer have matching original full-base models. Named paid
rank/SFM, exact LP, integral intersection/decomposition and public fallback
algorithms remain mathematical dependencies. The structural deficit
manuscript is not used to infer a different local-search theorem without
its own proof.

## Executable evidence

```sh
python3 problems/intrinsic-values-near-two/verify/check_intrinsic.py
```

The [native reference](../reference/README.md) executes actual weighted prefix
selection, certified union/heavy completion, exact original fractional
realization and joint complement-prefix lower rounding. Its checker supplies:

- 83 original-input rank geometries, independently reconstructed from
  original basis/one-heavy-assignment feasibility, including original loops
  and compulsory-player refined parameters.
- 112 completions of actual light bases, checking original basis containment,
  original type assignments and every original heavy resource inequality.
- 106 original allocation/parameter cases against independent exhaustive
  integer allocations; 212 near-two/quantified-margin calls and 106 XP or
  zero-corank exact-half calls, with each actual threshold promise computed
  from the original optimum.
- 41 direct original fractional/integer recovery checks, including all
  original totals, every rank row and every lower prefix, not just a final
  aggregate value check.
- Refined-zero hidden-rank and two-unit nonmatroid boundaries, 101-bit
  resource multiplicities, supplied-fallback retention, a producer-disabled
  original-output verifier, two forged output
  rejections and seven malformed inputs.

The exhaustive comparator uses original owner/type counts and original rank
inequalities. It imports no dual, union, workload, LP, omission or rounding
helper from the backend. The derived-basis comparator is reconstructed by
original heavy assignment and original player-basis completion, rather than
assuming the dual-union identity being tested. The output verifier checks
original feasibility without a producer or optimizer. Finite examples
support the general proofs; they do not prove asymptotic bounds, the public
fallback theorem or an oracle-query lower bound.

## Model and implementation boundaries

All values are common intrinsic values, resource polymatroids are independent,
and unused capacity is permitted. There is no assignment/setup budget or
extra coupling between types. The reference validates complete rank tables,
whose full encoding is charged; its table algorithms do not claim rank-only
input time by constructing those tables implicitly.

The native near-two method uses the actual shared prefix recursion and
full-accuracy fixed-family rational search. Light LP realization and joint
rounding stream active systems, so their potentially exponential basis count
is charged separately from the theorem's paid polynomial primitives. They
use polynomial rational workspace and never loop over binary capacities or
individual resource units. The XP method alone enumerates derived complements.

The default implementation returns a valid candidate on every input and
has the approximation under its stated threshold parameter promise. It does
not implement the public unconditional fixed-constant fallback. A supplied
fallback must have its own paid guarantee; the program checks feasibility
and compares actual values. This software boundary does not make the named
mathematical fallback or its explicit dummy transfer unresolved.

The [source map](../sources.md) identifies the exact dependencies. Repository
checks validate links, notation and generated surfaces rather than mathematical
correctness. External peer review and proof-assistant verification are not
claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
