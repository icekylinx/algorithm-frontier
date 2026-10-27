# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Two exact scenario budgets already obstruct corank-FPT unit selection](proof.md)

## Mathematical dependencies

The sole external hardness input is Abboud, Lewi and Williams,
*Losing Weight by Gaining Edges*, Definition 1.1 and Theorem 1.3.
Definition 1.1 uses nonnegative entries and a nonnegative target bounded
by `q^(2k)`, selected by exactly `k` indices. Section 4 gives the
deterministic hardness reduction. The present proof uses this bounded
source directly, rather than the paper's separate randomized range
reduction for arbitrary integers. Its W[1]-membership result is unnecessary.

All remaining steps are local: polynomial-time preprocessing of trivial
cardinality cases, binary encoding of the two cost lists, the identities
TS3--TS4, and preservation of corank `c=k`. The free Boolean ranks have
only coordinatewise unit capacities, so no rank-oracle, LP, integral
intersection, rounding or common-basis algorithm is assumed. A zero-count
allocation is always feasible; the reduction detects positive integer
service rather than ordinary feasibility.

## Primary references

- [Losing Weight by Gaining Edges](https://people.csail.mit.edu/rrw/ksum.pdf), author-hosted 12-page version: Definition 1.1 on page 1, Theorem 1.3 on page 2, and the deterministic hardness direction in Section 4 on page 10. Checked against the actual source on 2026-10-27.

## Executable evidence

- [verify_finite_reductions.py](../../tools/verify_finite_reductions.py): Exhaustive reduction identity for q=2,...,7, every vector in {0,1,2,3}^q, all 1<=k<q, every omitted k-subset and every integer target from zero through the total sum. It checks equivalence of the two budget inequalities and the target subset sum, not W[1]-hardness itself.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
