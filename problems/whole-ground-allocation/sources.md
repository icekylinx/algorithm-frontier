# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Global exponential-time allocation, scheduling and selected-flow transfers](proof.md)
- [Corank omission with a changing residual budget](adaptive-selection.md)
- [A polynomial-space conversion from corank gaps to global exponential time](global-conversion.md)
- [Faster global time for coarser integer-quota approximation](integer-quotas.md)
- [Rational comparator recovery without splitting the approximation error](rational-optimization.md)
- [Single-exponential corank time for weighted packing through first-violation prefixes](selection.md)

## Mathematical dependencies

- [Arbitrary-cost allocation near factor two with an adaptive residual budget](../../manuscripts/allocation-and-scheduling/arbitrary-cost-residual-budget-near-two-allocation.md)
- [Minimum-cost common bases with degree capacities: a corank augmentation scheme](../../manuscripts/allocation-and-scheduling/corank-degree-bounded-common-bases.md)
- [The exact corank-sensitive time curve of the block gap conversion](../../manuscripts/allocation-and-scheduling/global-gap-corank-profile-bound.md)
- [Exact factor two for one-value allocation with arbitrary assignment costs](../one-value-exact-two/proof.md)
- [Adaptive selected flow under explicit network scenarios](../robust-scenario-flow/proof.md)
- [Near-optimal concurrent flow with few rejected commodities and exact selection constraints](../selected-flow/proof.md)
- [Selected concurrent flow with one shared setup and routing budget](../shared-setup-flow/proof.md)
- [A three-halves algorithm for two-size polymatroid scheduling in the corank parameter](../two-size-scheduling/proof.md)
- [Exact two for compulsory two-value allocation with arbitrary assignment costs](../two-value-exact-two/proof.md)

## Related bounds and model comparisons

- [A value-oracle barrier below factor two for rank-parameterized allocation](../allocation-lower-bounds/proof.md)

## Primary references

- [*Exact Algorithms via Monotone Local Search*](https://arxiv.org/abs/1512.01621)
- [Bamas et al., arXiv:2307.08453v1](https://arxiv.org/html/2307.08453v1)
- [*Cost Preserving Dependent Rounding for Allocation Problems*, ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127)
- [author journal manuscript](https://sites.cs.ucsb.edu/~daniello/papers/monotoneLocalSearch19.pdf)

## Executable evidence

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): Integer-quota arithmetic: <code class="math">d=2,\ldots,30</code> and every <code class="math">d&lt;K\le399</code> (11,107 cases) satisfy <code class="math">K/(K-\lceil K/d\rceil)\le(d+1)/(d-1)</code>; every <code class="math">1\le K\le d</code> satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed. Only the integer-quotas companion is covered; no global-conversion check is claimed.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
