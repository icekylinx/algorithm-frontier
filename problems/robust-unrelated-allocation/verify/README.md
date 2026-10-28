# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- <code class="math">\mathrm{FOPT}</code> chooses one actual common player basis with scenario-specific fractional assignments. A common setup vector contributes to each exact scenario budget.
- Intersected service regions have nonnegative support separators, and a fixed promised basis survives omissions and residual setup-cost changes.
- Exact reoptimization and separate scenario rounding retain the basis, budget and player-specific additive loss.
- The boundary constructions distinguish common selection from invalid common roles and from fractional dummy selection.
- The [native realization proof](../reference-realization.md) checks the minimum attained common setup, original physical ranks, all-scenario protected witness, rational denominator bound and fixed-basis scenario recovery. The weighted prefix, streamed cover and original scalar-cost rounding dependencies match the theorem's literal input and output.

## Executable evidence

[check_robust.py](check_robust.py) independently rebuilds eight original
fixed-basis fractional LPs and verifies their original integer recoveries;
45 forced/common-basis gaps check sound failures and relaxed successes,
including a four-owner logarithmic-block cover failure;
five full-accuracy rational/global-cover optimizations check the original
fractional comparator. A separate exact rational Gaussian solver rebuilds
the original comparator independently of the producer. Fixtures retain
fractional use of whole-unit-expensive pairs, common setup with changing
attaining bases, zero/empty regions, one scenario-role disagreement,
six bases of the zero/one robust common-selection obstruction and a
101-bit supply. Original output verification is tested with a producer
disabled, two forged records and four malformed inputs.

Run from the repository root:

```sh
python3 problems/robust-unrelated-allocation/verify/check_robust.py
```

The [native API](../reference/README.md) executes actual weighted omission,
streamed covers, original fixed-basis reoptimization and scenario rounding.
Its local active-basis LP enumeration and temporary projected-support list
can have exponential time and memory, separately from the paid polynomial
primitives in the mathematical theorem. Finite checks do not prove its
asymptotic guarantees or remove the additive-loss boundary.

## Model and verification boundaries

<code class="math">\mathrm{FOPT}</code> is the actual-basis fractional-assignment comparator, not a fractionally selected basis or an integer comparator. The guarantee retains scenario-specific additive errors; different setup vectors or a common heavy/light assignment are not automatic extensions.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
