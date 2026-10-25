# Boolean linear optimisation compiler — checkpoint X draft

**Status: Draft checkpoint X.** This card records a parameterised compiler bound conditional on a supplied deterministic Subset Sum backend.

| Field | Candidate statement |
|---|---|
| **Guarantee** | For `n` Boolean variables, any number of signed equalities, and `m` signed interval rows, the source constructs an exact interval/slack compiler with a tunable parameter `B` and a catalogue of short interval tests. |
| **Objective and output** | Decide exact feasibility, recover indexed Boolean witnesses, and support explicitly listed polynomial-size linear objectives through the same backend interface. |
| **Time** | `T_B <= poly(L) * (product_i p_i) * 2^(alpha*n + Q - (1-alpha)*B)`, where `p_i <= 4*ceil(log2(W_i + 1)) + 1`, `Q = sum_i ceil(log2(min(W_i + 1, 5*s_i + 1)))`, `0 <= B <= Q`, and `alpha` is the supplied Subset Sum exponent. The branch count is exactly `(product_i p_i) * 2^(Q-B)`. |
| **Space** | If the backend exposes writable space `poly(L') * 2^(sigma*N)`, the compiler uses `S_B <= poly(L) * 2^(sigma*(n + B))`. No unconditional backend space bound is added here. |
| **Parameters** | `L` is full input length; `s_i` is row support; `W_i = u_i - ell_i`; `m` is the number of interval rows; `p_i` is the short-interval catalogue size; `Q` is total slack-bit count; `B` lies in `[0,Q]`. Exact equalities are charged to `L`, not `Q`. |
| **Model and representation** | Boolean variables, signed binary coefficients and endpoints, and a deterministic indexed-witness Subset Sum backend. One-sided inequalities and exact rows are normalized as specified in the source. |
| **Lower-bound scope** | No lower bound or universal dominance claim is made. The interval-rounding mechanism is credited to prior work; the incremental observation is the support-sensitive slack interpolation and its accounting. |
| **Review status** | Draft checkpoint X. Verify interval exactness, backend composition, and source attribution before promotion; formal verification is not claimed. |
| **Source** | [Boolean compiler draft](../../sources/checkpoint-x/08_boolean_linear_optimization_compiler.md). |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
