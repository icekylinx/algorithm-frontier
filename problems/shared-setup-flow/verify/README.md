# Verification and scope

The [main proof](../proof.md) and shared
[reference realization](../../selected-flow/reference-realization.md) have separate
theorem and executable scopes.

## Mathematical review

The review covers the attained minimum-setup restriction oracle, fresh residual
routing budget at every omission node, one unchanged protected full-rate set
and routing, nonnegative finite Farkas separation, exact returned-set
reoptimization, and the sharp fixed-accuracy whole-ground conversion.
The weighted prefix, adaptive residual-region and rational comparator proofs
were read as part of this dependency chain.

A feasibility-only selector does not supply the required minimum-setup
optimizer. Several fixed routing-only budgets remain valid, but unrelated
extra selection budgets do not automatically admit the same selector.
The original capacities and allowed family remain fixed. Exact polynomial
rational LP and the stated exact minimum-setup oracle are paid mathematical
dependencies. Internal review does not claim external peer review or formal
verification.

## Executable evidence

```sh
python3 problems/selected-flow/verify/check_concurrent.py
```

The common [exact reference backend](../../selected-flow/reference/README.md)
subtracts the actual selected set's setup cost before each fixed-set LP.
The checker includes 16 setup-budget profiles with independent path-LP
comparisons, the manuscript's optimum rate-twenty example, forbidden permitted
sets, and completely unaffordable families. The companion
[evidence note](../../selected-flow/verify/README.md) records the full primitive,
flow, separator and hostile-certificate test counts.

A fixed-set result has a search-free primal/dual certificate against the
actual residual budget. Exact global selected-set optimization is supplied by
explicit enumeration and a fixed-family predicate. It does not implement the
faster adaptive omission recursion or the polynomial-time minimum-setup
matroid-intersection oracle. Its finite simplex and enumeration bounds are
stated separately from the research approximation theorem.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
