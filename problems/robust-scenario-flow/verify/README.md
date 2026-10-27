# Verification and scope

The [main proof](../proof.md) and [exact realization](../reference-realization.md)
separate the adaptive robust theorem from the executable reference baseline.

## Mathematical review

Internal review covers the complete scenario intersection construction,
its normalized nonnegative Farkas separator, original-coordinate omission
recursion and fixed-family rational comparator recovery. The combined
fixed-set LP retains all original scenario data, has polynomial dimension
and a uniform polynomial-bit denominator bound. The whole-ground sharp
base retains the fixed rational accuracy condition.

The exact-admission Hitting Set reduction has been checked in both
directions, including parameter preservation, forced bottleneck flow,
positive-capacity forests, the zero-capacity case and the absence of a
constant approximation gap. The primary source explicitly supplies the
solution-size `W[2]`-complete source problem. It proves no corresponding
lower bound for a fixed accuracy or a single-edge-failure-only family.

## Executable evidence

```sh
python3 problems/robust-scenario-flow/verify/check_scenarios.py
```

The [reference](../reference/README.md) reuses the canonical exact selected-flow
primitives. Its checker supplies:

- 48 robust selected-set optima against independently built native
  simple-path LPs solved by active-set enumeration, across distinct
  directed/undirected topologies, demands and scenario budget rows.
- 144 membership/boundary/strict-separation queries and independent native
  conservation, physical-capacity and budget checks on common-rate routings.
- 96 missing or mutated scenario-certificate rejections, two forged object
  type rejections, plus explicit
  common-choice versus independent-selection and adaptive-path fixtures.
- 59 exact Hitting Set network optima and positive-capacity forest checks
  for every nonempty blocked/selected pair on up to three elements.
- 922 exhaustive family/omitted-set admission identities on those grounds,
  six malformed input rejections and an optimizer-disabled verifier call.

The path LP and active-set solver are reused from the selected-flow
independent checker; they import no model builder or optimizer from the
scenario backend. The robust verifier shares the canonical native
formulation with its optimizer. Independent path and native routing
checks address that separate trusted translation. These finite checks
support the general proofs; they do not prove asymptotic complexity or
the external source problem's hardness.

## Model and implementation boundaries

Flows are rational, splittable and adaptive to an explicit scenario list;
selection alone is common. Exact capacities and all stated routing budgets
are preserved. The reference's Bland simplex and original-set enumeration
can take exponential time and do not implement the omission recursion,
rational target search or streamed global wrapper. Fixed-set optimality
has a search-free certificate; global optimality additionally relies on
complete enumeration and the paid fixed-family predicate.

The theorem retains paid polynomial exact rational LP, Farkas duality and
its exact restriction selector. Neither software absence nor the finite
simplex bound makes that mathematical theorem conditional on an unproved
flow interface. The [source map](../sources.md) records the dependencies.
Repository checks validate links, notation and generated surfaces rather
than mathematical correctness. External peer review and proof-assistant
verification are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
