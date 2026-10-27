# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Matroid union removes the largest-item penalty](proof.md)
- [Configuration-LP comparison for the player-matroid union reduction](configuration-comparator.md)

## Mathematical dependencies

- [Sharper star charging and rank-sensitive quality for matroid allocation](../../manuscripts/allocation-and-scheduling/matroid-allocation-sharp-star-rank-quality.md)
- [Current blocker growth for matroid max-min allocation](../../manuscripts/allocation-and-scheduling/matroid-allocation-current-blocker-quasipolynomial.md), Sections 2–8: individual eligibility, earliest circuit exchange, last-layer refresh and the finite signature count. The physical-item theorem does not require the more general recipient-matroid extension.

## Primary references

- [DRZ v4, Lemma 14](https://arxiv.org/html/1807.07189v4)
- [Terao, ICALP 2023](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2023.104)

## Executable evidence

The [finite union-reduction checker](verify/check_union_reduction.py)
independently enumerates small union decompositions, rank minimizations,
dual-basis recovery and exact rational fractional rank constraints. It is
finite evidence, not the polynomial matroid-union algorithm or full allocator.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
