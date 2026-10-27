# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [A value-oracle barrier below factor two for rank-parameterized allocation](proof.md)
- [Two integrality gaps for recipient-polymatroid configuration relaxations](configuration-gaps.md)
- [The factor-two oracle obstruction persists at refined parameter zero](refined-parameter-barrier.md)

## Mathematical dependencies

The lower bounds do not depend on the correctness of the corresponding
allocation or scheduling upper-bound algorithms. The hidden rank is proved
submodular directly, its dual is checked directly, and the transcript
argument counts the remaining hidden sets without importing a matroid-parity
oracle theorem.

The configuration-gap proof derives the greedy vertex description of an
integral polymatroid and computes residual capacity using only feasibility,
tightness on its greedy support and submodularity. Convexity then proves
the equivalence of all reserve cuts and all subset cuts. This argument
uses no unit-copy construction, flow oracle or unproved allocation interface.
For the comparison with separately represented uniform-matroid components,
both displayed cardinality ranks have direct integer decompositions: allocate
one unit per positive coordinate to the free component and put the excess
in rank-one components, or put doubled coordinates in both uniform components
and split singleton coordinates within the remaining capacities. No general
integral polymatroid decomposition theorem is needed for these examples.

## Model definitions and comparisons

- [Recipient-polymatroid allocation](../recipient-polymatroid/proof.md): the integer comparator and its separate upper bound; not a premise of the lower bounds.
- [Two-size scheduling](../two-size-scheduling/rank-parameter.md): the full-base job-polymatroid model used by the dual construction; not a premise about that algorithm's performance.
- [Arbitrary-player heavy parameters](../intrinsic-values-near-two/player-selection.md#1-model-and-the-derived-parameter): the Boolean-cap matroid and loop-deleted corank convention. The refined-parameter proof uses a free Boolean cap, making the derived dual all loops.
- [Compulsory-player heavy parameters](../intrinsic-values-near-two/proof.md): the refined parameter is heavy-cover rank minus its number of coloops. A free heavy-cover matroid makes this zero, although its unrefined rank is the full ground size.

## Executable evidence

- [check_barriers.py](verify/check_barriers.py): independent finite hidden-rank axioms and quota comparisons, complementary scheduling ranks, balanced refined-zero instances, aggregate configuration rows, residual subset cuts, direct feasible-reserve cuts, and greedy residual identities. Exact instance ranges and totals are in the verification note. The adaptive-query argument and asymptotic separation are mathematical proofs, not outputs of this checker.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
