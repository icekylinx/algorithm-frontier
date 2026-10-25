# Allocation and scheduling oracle barriers

This is a boundary record for value-oracle lower bounds and configuration
obstructions.

| Field | Curated statement |
|---|---|
| **Guarantee** | In the stated hidden-rank value-oracle models, strictly below factor two allocation and strictly below factor three-halves two-size scheduling are blocked by the named query barriers. |
| **Objective and output** | Distinguish what an oracle transcript can identify from what a configuration relaxation can represent; the record outputs a lower-bound or gap statement rather than an allocation algorithm. |
| **Time** | The hidden-rank oracle barrier requires at least `binom(q,r) - 1` deterministic rank-oracle queries for any factor below two; configuration-gap rows retain their own bases. |
| **Space** | Not an algorithmic resource claim; the record is a query lower bound and representation boundary. |
| **Parameters** | `q` is the potential-player count; `r` is the hidden basis rank; `c=q-r` is the scheduling-transfer corank; the approximation factor and comparator are row-specific. |
| **Model and representation** | Full rank-value-oracle models and the exact aggregate configuration relaxations named by each source. No explicit-input hardness or universal optimal-base claim is inferred. |
| **Lower-bound scope** | This page is itself a lower-bound record. Oracle-query, configuration-gap, deterministic-ETH, and explicit-input claims remain separate and are never merged. |
| **Review status** | Internal display and model review; proof and scope follow-up remains in the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). Finite audits are not formal verification. |
| **Source** | [Recipient-polymatroid oracle barrier](../../sources/checkpoint-o/recipient_polymatroid_below_two_oracle_barrier.md), its [proof map](proof.md), and `verify/`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
