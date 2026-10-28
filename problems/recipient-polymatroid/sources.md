# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Prefix normalization gives factor four for arbitrary recipient polymatroids](proof.md)
- [Binary representation and the integer-comparator lemma](representation.md)
- [Binary pricing and original residual-configuration realization](fractional-realization.md)

## Mathematical dependencies

- [Prefix rank additivity and eager release for resource matroids](../recipient-matroid-configuration/proof.md)

## Related bounds and model comparisons

- [Two integrality gaps for recipient-polymatroid configuration relaxations](../allocation-lower-bounds/configuration-gaps.md)

## Executable evidence

- [Binary-count backend](reference/README.md) and [realization proof](reference-realization.md): natural rank, whole-block contraction, integral comparator recovery and threshold minimality using numerical counts.
- [Independent original-count checker](verify/check_counts.py): exhaustive original-subset feasibility and maximum recovery on small rank tables, plus 100-digit-capacity guards. Full allocation layers remain outside this implementation.
- [Fractional/pricing backend](reference/fractional.py) and [independent original-box checker](verify/check_fractional.py): signed convex-cost pricing, strict rational-grid weak separation, subset/reserve and scaled loss identities, signed aggregate support, actual normalized-Farkas column generation and original-grid fractional optimization. Finite generation/storage and exact Bland pivot costs remain separate from the mathematical ellipsoid bounds.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

## Strengthened comparators and their optimization

- [Residual-capacity configuration relaxation](../../manuscripts/allocation-and-scheduling/recipient-polymatroid-residual-configuration-relaxation.md)
- [Exact subset-cut compression](../../manuscripts/allocation-and-scheduling/recipient-polymatroid-subset-cut-compression.md)
- [Scaled recipient-matroid configuration transfer](../../manuscripts/allocation-and-scheduling/scaled-recipient-matroids-binary-configuration-transfer.md)
- [Bounded-support fractional optimizer](../../manuscripts/allocation-and-scheduling/residual-configuration-bounded-support-xp-solver.md)
- [Count-box pricing and full fractional optimization](../../manuscripts/allocation-and-scheduling/residual-configuration-box-pricing-and-weak-solver.md)

The [fractional realization](fractional-realization.md) audits all these
interfaces and the configuration-gap boundaries. The optimizer restriction
to coordinate boxes and its fractional-only unrelated-value corollary are
distinct from the allocation comparator's certified availability-oracle
model. Classical ellipsoid containment/volume and knapsack scaling are
identified in those companions; their model-specific strict-price,
positive-direction and finite-primal extraction proofs are explicit.

**Attribution:** icekylinx and GPT-6 Astra Pro.
