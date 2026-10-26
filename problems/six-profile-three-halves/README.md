# Six-profile exact three-halves scheduling

| Field | Result |
|---|---|
| **Guarantee** | Returns an integer schedule with makespan at most $3\operatorname{OPT}/2$ while preserving every original job total and the exact assignment-cost budget. |
| **Objective and output** | Minimize maximum load for arbitrary machine-type processing times; output a full original schedule. |
| **Time** | $6^q\operatorname{poly}(H)$, with six profiles per physical machine. |
| **Space** | Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. |
| **Parameters** | $q$ is the physical-machine count. $H$ includes original processing times, costs, binary job totals, recipient-rank descriptions, and paid profile, LP, intersection, and rounding work. |
| **Model and representation** | Arbitrary nonnegative rational processing times and assignment costs, integral job polymatroids, eligibility masks, mandatory original bases, and one exact budget. |
| **Lower-bound scope** | No lower bound or optimality claim is made for the base six. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md). |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
