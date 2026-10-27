# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- <code class="math">\mathrm{FOPT}</code> chooses one actual common player basis with scenario-specific fractional assignments. A common setup vector contributes to each exact scenario budget.
- Intersected service regions have nonnegative support separators, and a fixed promised basis survives omissions and residual setup-cost changes.
- Exact reoptimization and separate scenario rounding retain the basis, budget and player-specific additive loss.
- The boundary constructions distinguish common selection from invalid common roles and from fractional dummy selection.

## Executable evidence

No result-specific executable check is supplied. The argument above is a mathematical proof, not an executable certificate or a complete solver.

## Model and verification boundaries

<code class="math">\mathrm{FOPT}</code> is the actual-basis fractional-assignment comparator, not a fractionally selected basis or an integer comparator. The guarantee retains scenario-specific additive errors; different setup vectors or a common heavy/light assignment are not automatic extensions.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
