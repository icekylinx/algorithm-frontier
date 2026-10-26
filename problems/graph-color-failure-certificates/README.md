# Exact graph certificates under color failures

One fixed edge set preserves every surviving ordered prefix and its canonical minimum spanning forest.

[Proof](proof.md) · [Sources](sources.md)

| Field | Statement |
|---|---|
| **Guarantee** | For vertex colors, retain at most $\sum_C\left[n_Ck_C-\binom{k_C+1}{2}\right]$ edges, where $k_C=\min\{h+1,q_C\}$, and preserve exact connectivity and canonical MSF after every allowed color failure. |
| **Objective and output** | An original-edge certificate for the fixed signed weight/ID order. Mixed colors and overlapping lists use the separate formulas below. |
| **Time** | Uniform deterministic polynomial preprocessing. A direct activation matrix uses $O(mR^2)$ field operations after sorting, where $R=\sum_Cn_Ck_C$. For $h=1$, a separate dynamic-MSF construction has the near-linear work bound below and requires exchange reporting. |
| **Space** | Displayed bounds count retained original edges. Direct elimination uses $O(R^2)$ field elements of workspace. Query output includes scanning the surviving certificate and Kruskal work. |
| **Parameters** | $n_C,q_C$ count original component vertices/colors; $h$ is failed-color budget; $d_v,d_e$ bound vertex/extra-edge list lengths; $t$ is actual vertex-feature rank when computed. |
| **Model and representation** | Undirected graphs with optional parallel edges, signed rational weights, and permanent edge IDs. Failures delete full color classes. The weight order stays fixed. |
| **Lower-bound scope** | The vertex-only envelope is sharp via the classical individual-vertex example. List and mixed models have matching leading coefficients in the stated simple-graph or multigraph regimes. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Complete proof](proof.md) and [canonical manuscript map](sources.md). |

## Results

| Failure model / result | Retained edge bound or work |
|---|---|
| One color per vertex | $\sum_C\left[n_Ck_C-\binom{k_C+1}{2}\right]$, $k_C=\min\{h+1,q_C\}$ |
| Vertex lists of size $d_v$, computed feature rank $t$ | $nt-\binom{t+1}{2}$, $t\le\min\left\{n,\binom{h+d_v}{d_v}\right\}$ |
| Vertex and extra-edge lists, degrees $d_v,d_e$ | $\min\left\{m,n\binom{h+d_v+d_e}{d_v+d_e}\right\}$ |
| One color per vertex and per edge; at least $h+1$ vertex colors in a component | $n\binom{h+2}{2}-\binom{h+3}{3}$, componentwise |
| General mixed-color rank refinement | Subtract $\binom{h+3}{3}-\binom{h-t+3}{3}$ from $n\binom{h+2}{2}$ |
| One failed color, near-linear construction | $O\!\left((m+A)[\log^4(n+2)+\log(m+2)]+ar\right)$, plus input organization; $a=2d_v+d_e$, $A\le am$, $r=$ MSF size |
| One failed color, total difference lists | $\sum_c\lvert R_c\rvert\le ar$; indexed cost lookup $O(1)$ |

When the list-feature dimension is gated out, the algorithm claims the parameter envelope at $t=\min\left\{n,\binom{h+d_v}{d_v}\right\}$; the sharper actual-rank bound requires computing that rank.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
