# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Prefix normalization gives factor four for arbitrary recipient polymatroids](proof.md)
- [Binary representation and the integer-comparator lemma](representation.md)

## Mathematical dependencies

- [Prefix rank additivity and eager release for resource matroids](../recipient-matroid-configuration/proof.md)

## Related bounds and model comparisons

- [Two integrality gaps for recipient-polymatroid configuration relaxations](../allocation-lower-bounds/configuration-gaps.md)

## Executable evidence

- [Binary-count backend](reference/README.md) and [realization proof](reference-realization.md): natural rank, whole-block contraction, integral comparator recovery and threshold minimality using numerical counts.
- [Independent original-count checker](verify/check_counts.py): exhaustive original-subset feasibility and maximum recovery on small rank tables, plus 100-digit-capacity guards. Full allocation layers and fractional optimizers remain outside this implementation.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

## Strengthened comparators and their optimization

- [Residual-capacity configuration relaxation](../../manuscripts/allocation-and-scheduling/recipient-polymatroid-residual-configuration-relaxation.md)
- [Scaled recipient-matroid configuration transfer](../../manuscripts/allocation-and-scheduling/scaled-recipient-matroids-binary-configuration-transfer.md)
- [Bounded-support fractional optimizer](../../manuscripts/allocation-and-scheduling/residual-configuration-bounded-support-xp-solver.md)
- [Count-box pricing and full fractional optimization](../../manuscripts/allocation-and-scheduling/residual-configuration-box-pricing-and-weak-solver.md)

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
