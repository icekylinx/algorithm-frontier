# Verification and scope

The [main proof](../proof.md) and [reference realization](../reference-realization.md)
separate the corank approximation theorem from the executable exact baseline.

## Mathematical review

The complete selected-flow argument has been read with its weighted
first-crossing omission proof, rational comparator recovery and streamed
whole-ground conversion. The review covers the normalized finite Farkas
separator, nonnegative terminal-gap repair, exact routing budgets, singleton
zero-rate test, polynomial-bit denominator bounds, actual fixed-set
reoptimization, and one shared undirected capacity per physical edge.
The whole-ground sharp base retains its fixed rational accuracy condition.

Exact polynomial rational LP and the paid restriction selector remain
specified theorem dependencies. The reference simplex uses a different
finite worst-case bound. This is internal mathematical review, not external
peer review or proof-assistant verification.

## Executable evidence

```sh
python3 problems/selected-flow/verify/check_concurrent.py
```

The dependency-free [reference backend](../reference/README.md) supplies fixed-set
exact optimization, primal/dual certificates, normalized nonnegative Farkas
separation, and exact permitted-set enumeration. The checker covers:

- 120 small rational LPs against independent active-set vertex enumeration.
- 175 native flow optima against independently constructed simple-path LPs,
  including all 64 directed simple graphs on three vertices with and without
  a routing budget, 27 opposite-direction shared-capacity cases, and 20 seeded
  two-commodity budgeted instances.
- 16 setup-budget profiles and the manuscript's rate-twenty versus rate-one
  example; forbidden families and unaffordable families return `None`.
- 411 normalized Farkas queries, checking boundary membership, strict
  separation, nonnegative coefficients and original potential inequalities.
- 256 mutated primal/dual certificates, eight malformed inputs and a verifier
  call with the optimizer disabled.

All comparisons use exact rational arithmetic. Native path enumeration and
active-set solving import no optimization routines or matrix builder from the
backend. The fixed-set certificate verifier itself shares the model builder
with the solver; the native path comparisons address that separate trusted
translation. These finite tests support the written general proofs; they
are not an asymptotic benchmark or a proof of every possible instance.

## Implementation boundary

The simplex pivot count can be exponential. Explicit combination enumeration
can also be exponential. Neither implements the faster omission recursion or
the rational target search. The independent optimality certificate covers
one fixed set; global optimality also relies on complete enumeration and the
fixed-family predicate. The model is splittable rational flow, with no
unsplittable or integral multicommodity guarantee.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
