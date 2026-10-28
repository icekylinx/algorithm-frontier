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

The count executable realizes these representation interfaces. It does not
run the complete player-layer algorithm. Its explicit-table enumeration
costs remain separate from the theorem's paid oracle costs.

The separate [fractional reference](../reference/fractional.py) and
[realization proof](../fractional-realization.md) supply actual signed
coordinate-box pricing, subset cuts, aggregate support, normalized Farkas
generation and original-grid weak fractional optimization. Run:

```sh
python3 -B problems/recipient-polymatroid/verify/check_fractional.py
```

This checker independently enumerates original small box vectors for
200 signed convex-price cases and 400 strict weak-price tests; it checks
70 dependent reserve bases, 63 reserve/subset comparisons, 608 scaled
fractional loss inequalities and 81 signed aggregate maxima. A separate
rational Gaussian original-LP comparator covers nine instances, 36 weak
targets and nine optimizations, retaining every original aggregate rank
row. An additional actual generated point has genuinely fractional masses
and multiple aggregate vertices while retaining all aggregate rows in a
support-zero relaxation. It includes both configuration gaps, binary 101-bit supply, 121-bit
accuracy encoding, empty/rank-zero conventions, a producer-disabled
original fractional verifier, four forged outputs and eight malformed
inputs. The independent comparators do not use the native pricing,
column, aggregate-greedy, Farkas or LP producer.

The native finite generation may store exponentially many configurations
and aggregate vertices. Each local pricing call uses binary segments and
a profit-scaled exact-budget DP; each normalized LP uses separately
charged finite Bland pivots. This is executable evidence for the original
interfaces, with no fast ellipsoid implementation or integer allocation
claim attached to fractional output.

## Model and verification boundaries

The principal guarantee compares against integer optimum for arbitrary integral recipient polymatroids. The strengthened residual-capacity relaxation has its own explicit cuts and comparator theorem. A separately represented component configuration system retains stronger information than a merged aggregate relaxation. The fractional optimizer requires coordinate-box local families; it is not an integer approximation scheme or a general local-oracle implementation. Binary capacities are never expanded into individual units.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
