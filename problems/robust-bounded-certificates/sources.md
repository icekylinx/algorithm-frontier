# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Robust unit allocation with bounded minimal infeasibility certificates](proof.md)
- [Certified weighted unit intersection and the guarded robust basis gate](reference-realization.md)

## Mathematical dependencies

- [Exact factor two for one-value allocation with arbitrary assignment costs](../one-value-exact-two/proof.md), Sections 3 and 5: nonnegative support separation and integral maximum-total quota recovery.

- [Two exact scenario budgets already obstruct corank-FPT unit selection](../robust-two-scenario-hardness/proof.md)
- [A Fibonacci-base exact gate for width-two robust unit feasibility](../robust-width-two-allocation/proof.md)
- [A polynomial-space conversion from corank gaps to global exponential time](../whole-ground-allocation/global-conversion.md)
- [Faster global time for coarser integer-quota approximation](../whole-ground-allocation/integer-quotas.md)
- [Single-exponential corank time for weighted packing through first-violation prefixes](../whole-ground-allocation/selection.md)

## Primary reference

- [Bárász et al., Matroid Intersection under Minimum Rank Oracle, arXiv:2407.03229v2, Definition 2.2, Algorithm 2 and Lemma 2.5](https://arxiv.org/html/2407.03229v2#S2): standard weighted augmentation and its exchange-cycle characterization. The reference uses ordinary independence oracles; it does not rely on the paper's restricted minimum-rank machinery.

## Executable evidence

- [Certified weighted/unit/gate reference](reference/README.md) and [independent finite checker](verify/check_bounded.py).

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): Integer-quota arithmetic: <code class="math">d=2,\ldots,30</code> and every <code class="math">d&lt;K\le399</code> (11,107 cases) satisfy <code class="math">K/(K-\lceil K/d\rceil)\le(d+1)/(d-1)</code>; every <code class="math">1\le K\le d</code> satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed. Failure width and scenario feasibility are also outside the check.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
