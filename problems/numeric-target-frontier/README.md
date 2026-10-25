# Numeric-target and support-sensitive frontier

This is a Tier A record for exact target feasibility, scalar optimization, and support-sensitive refinements in a globally coupled integral polymatroid.

| Field | Curated statement |
|---|---|
| **Guarantee** | Exact target decision and exact scalar optimization, with deterministic approximation and support-sensitive variants. |
| **Objective and output** | Upper-target, equality-target, and covering rows return an exact decision or an exact signed scalar optimum. Approximation rows state their direction and accuracy separately. |
| **Time** | The arbitrary-row envelope is exponential in the target budget times a polynomial factor. Fixed row dimension gives the sharper stretched-exponential envelope. The support-sensitive row replaces the arity restriction with the number of distinct eligible-column support patterns. |
| **Space** | Polynomial binary workspace in the named rank-oracle or readable-program model. Binary counts are never expanded into unit-size arrays. |
| **Parameters** | **T** is the numeric target budget; **Q** is the number of distinct nonempty eligible-column support patterns; **d** is fixed row dimension; **H** covers the complete binary input and paid polynomial primitive work; **epsilon** is the approximation accuracy. |
| **Approximation refinement** | For the stated target family, the reviewed accuracy factor is one over epsilon times exp of 141 divided by 50 epsilon plus 7, multiplied by a polynomial in H-epsilon. Single-matroid rows also retain separate square-root-of-T and square-root-of-OPT variants. |
| **Representation** | R and S cover independent regions or original-total bases of one arbitrary integral polymatroid. The source for each row names mandatory totals, exact budgets, and the rank representation. |
| **Lower-bound scope** | R records matching-order rank-oracle boundaries. S records a two-parameter query classification and separate deterministic-ETH consequences for readable rank programs or circuits. These claims do not automatically transfer to explicit matroids or ordinary graph matching. |
| **Review status** | Internal proof, algorithm, and source review is tracked in the [headline review report](../../reviews/headline/numeric-target-frontier.md). Finite replay checks are evidence for the listed statements; they are not formal verification. |

Read the [proof map](proof.md), [source map](sources.md), [complexity guide](../../docs/COMPLEXITY.md), and [complete index](../../CONTENTS.md) for the detailed rows and provenance.

**Sources.** [Checkpoint R](../../sources/checkpoint-r/CHECKPOINT_R_INCREMENT.md) and [Checkpoint S](../../sources/checkpoint-s/CHECKPOINT_S_INCREMENT.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
