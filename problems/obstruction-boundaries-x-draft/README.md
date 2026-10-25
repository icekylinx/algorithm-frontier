# Exact-separation and obstruction boundaries — checkpoint X draft

**Status: Draft checkpoint X.** Family-level review handle; not promoted.

| Field | Candidate statement |
|---|---|
| **Guarantee** | Exact membership in a specified binary compact-code partial-coloring body is claimed coNP-complete, while a seven-element non-Fano configuration gives exact value `15/128` where a proposed fixed-amplitude sign bound predicts `1/8`. |
| **Objective and output** | The first payload classifies membership in its feasibility body; the second computes the finite obstruction. Neither is a sparsifier or a general optimization algorithm. |
| **Time** | The separation statement is a complexity classification under bounded-arity binary reduction. The obstruction is constant-size exact rational enumeration. |
| **Space** | The reduction uses compact binary checks of arity at most two. The obstruction has seven elements and no asymptotic storage claim. |
| **Parameters** | The separation input is the compact check system and target body; the obstruction uses the listed seven-element incidences and fixed-amplitude sign objective. |
| **Model and representation** | Binary partial-coloring membership for payload 33 and the finite non-Fano sign-cone model for payload 38. |
| **Lower-bound scope** | coNP-completeness is a barrier for one separation route; `15/128` versus `1/8` refutes one conjectured inequality only. |
| **Review status** | Proof, algorithm, and source review are pending; formal verification is not claimed. |
| **Source** | Payloads `33` and `38` in the checkpoint-X source tree. |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
