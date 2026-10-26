# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Two exact scenario budgets already obstruct corank-FPT unit selection](proof.md)

## Mathematical dependencies

The model-specific reductions and inequalities are proved in the canonical manuscripts. Standard rank-oracle, linear-programming and integral-intersection interfaces are stated where they are used; an internal review label is not an additional mathematical premise.

## Primary references

- [Losing Weight by Gaining Edges](https://people.csail.mit.edu/rrw/ksum.pdf)

## Executable evidence

- [verify_finite_reductions.py](../../tools/verify_finite_reductions.py): Exhaustive reduction identity for q=2,...,7, every vector in {0,1,2,3}^q, all 1<=k<q, every omitted k-subset and every integer target from zero through the total sum. It checks equivalence of the two budget inequalities and the target subset sum, not W[1]-hardness itself.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
