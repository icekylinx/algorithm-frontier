# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- The reduction uses two explicit scenarios, the common basis rank <code class="math">q-k</code>, free Boolean resources and nonnegative assignment costs.
- Both budgets hold exactly when the omitted <code class="math">k</code>-set has the prescribed sum. Positive common service is the encoded decision event.
- The proof imports the identified parameterized <code class="math">k</code>-SUM hardness result and retains <code class="math">c=k</code>; the whole-ground rank-oracle obstruction has a different representation and conclusion.

An internal audit on 2026-10-27 read the canonical reduction and its
actual primary source, checking Definition 1.1, Theorem 1.3 and Section 4
of *Losing Weight by Gaining Edges*. The source already supplies
nonnegative bounded inputs and deterministic <code class="math">\mathrm{W}[1]</code>-hardness. The audit
reconstructed both budget identities, positivity versus feasibility,
nonnegative budgets, the `c=k` correspondence and binary-size bounds.
No unresolved algorithmic interface remains in this reduction. The family
is ready for manuscript review, conditional on the named published
source-hardness theorem and the stated complexity assumption.

## Executable evidence

[verify_finite_reductions.py](../../../tools/verify_finite_reductions.py) checks the following finite claim:

Exhaustive reduction identity for <code class="math">q=2,\ldots,7</code>, every vector in <code class="math">\{0,1,2,3\}^q</code>, all <code class="math">1\le k&lt;q</code>, every omitted <code class="math">k</code>-subset and every integer target from zero through the total sum. It checks equivalence of the two budget inequalities and the target subset sum, not <code class="math">\mathrm{W}[1]</code>-hardness itself.

Run from the repository root:

```sh
python3 tools/verify_finite_reductions.py
```

This checker implements the finite reduction identities, rather than
an allocation algorithm or a proof of source hardness. Its comparisons
are exact integer arithmetic. It does not establish the asymptotic
parameterized-complexity consequence.

## Model and verification boundaries

Exhaustive small instances test the exact reduction identity, not <code class="math">\mathrm{W}[1]</code>-hardness itself. The complexity conclusion depends on the cited source problem and parameter-preserving proof. No ETH bound or optimal whole-ground base follows from this finite check.

The impossibility concerns deterministic finite-factor algorithms under
`FPT != W[1]`, with exact budgets, integral service and one optional
common basis. It does not extend this assumption to randomized algorithms,
relaxed budgets or fractional service. The two scenario allocations may
adapt independently; the proof uses their shared selected basis only.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
