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

Run the independent original-count checker:

```sh
python3 -B problems/recipient-polymatroid/verify/check_counts.py
```

The [binary-count reference](../reference/README.md) and its
[realization proof](../reference-realization.md) cover natural ranks,
whole-block contraction, residual availability, integral comparator recovery
and one-pass minimal bundles. The checker covers 87 complete rank tables,
813 reserved ranks, 4,075 coordinate-increment availability identities,
9,127 original comparator recoveries, 438 minimal bundles and 10 malformed
inputs. It independently enumerates allocations satisfying original subset
inequalities, including nonseparable shared-feature ranks. Four additional
100-digit-capacity assertions exercise rank, availability, recovery and bulk
minimality without unit expansion.

The executable realizes these representation interfaces. It does not run
the complete player-layer algorithm or any fractional configuration solver;
the explicit-table enumeration costs remain separate from the theorem's
paid oracle costs.

## Model and verification boundaries

The principal guarantee compares against integer optimum for arbitrary integral recipient polymatroids. The strengthened residual-capacity relaxation has its own explicit cuts and comparator theorem. A separately represented component configuration system retains stronger information than a merged aggregate relaxation. The fractional optimizer requires coordinate-box local families; it is not an integer approximation scheme or a general local-oracle implementation. Binary capacities are never expanded into individual units.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
