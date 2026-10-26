# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [Binary representation and the integer-comparator lemma](../representation.md)

## Mathematical evidence

- The representation companion proves the natural rank formula and compressed distinct-copy interpretation without expanding binary multiplicities.
- Availability tests whole blocks; the integer contraction-loss lemma applies to the actual reserved set, including dependent units.
- Current-prefix normalization survives block moves with a paid progress measure, and its saved rank unit is a current dependence.
- Separate configuration constructions establish the aggregate and full residual gaps.
- The [residual-capacity comparator](../../../manuscripts/allocation-and-scheduling/recipient-polymatroid-residual-configuration-relaxation.md) proves the stronger fractional lower cover, preservation under the fat reduction, and the integer-quota consequence.
- The [fractional weak optimizer](../../../manuscripts/allocation-and-scheduling/residual-configuration-bounded-support-xp-solver.md) supplies a separate algorithm for coordinate-box local families. Its support-parameter running time is XP; it does not apply to an arbitrary local downward-closed oracle.

## Executable evidence

No result-specific executable check is supplied. The argument above is a mathematical proof, not an executable certificate or a complete solver.

## Model and verification boundaries

The principal guarantee compares against integer optimum for arbitrary integral recipient polymatroids. The strengthened residual-capacity relaxation has its own explicit cuts and comparator theorem. A separately represented component configuration system retains stronger information than a merged aggregate relaxation. The fractional optimizer requires coordinate-box local families; it is not an integer approximation scheme or a general local-oracle implementation. Binary capacities are never expanded into individual units.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
