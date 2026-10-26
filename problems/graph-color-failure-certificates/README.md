# Exact graph certificates under color failures

One fixed edge set preserves every surviving ordered prefix and its canonical minimum spanning forest.

[Proof](proof.md) · [Sources](sources.md)

**Guarantee**

For vertex colors, retain at most <code class="math">\sum_C\left[n_Ck_C-\binom{k_C+1}{2}\right]</code> edges, where <code class="math">k_C=\min\{h+1,q_C\}</code>, and preserve exact connectivity and canonical MSF after every allowed color failure.

**Objective and output**

An original-edge certificate for the fixed signed weight/ID order. Mixed colors and overlapping lists use the separate formulas below.

**Randomness**

Deterministic preprocessing and exact queries. The near-linear single-color construction uses a deterministic dynamic-MSF backend with exchange reporting.

**Time**

Uniform deterministic polynomial preprocessing. A direct activation matrix uses <code class="math">O(mR^2)</code> field operations after sorting, where <code class="math">R=\sum_Cn_Ck_C</code>. For <code class="math">h=1</code>, a separate dynamic-MSF construction has the near-linear work bound below and requires exchange reporting.

**Space**

Displayed bounds count retained original edges. Direct elimination uses <code class="math">O(R^2)</code> field elements of workspace. Query output includes scanning the surviving certificate and Kruskal work.

**Parameters**

<code class="math">n_C,q_C</code> count original component vertices/colors; <code class="math">h</code> is failed-color budget; <code class="math">d_v,d_e</code> bound vertex/extra-edge list lengths; <code class="math">t</code> is actual vertex-feature rank when computed.

**Model and representation**

Undirected graphs with optional parallel edges, signed rational weights, and permanent edge IDs. Failures delete full color classes. The weight order stays fixed.

**Lower-bound scope**

The vertex-only envelope is sharp via the classical individual-vertex example. List and mixed models have matching leading coefficients in the stated simple-graph or multigraph regimes.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete proof](proof.md) and [canonical manuscript map](sources.md).

## Results

**One color per vertex**

<code class="math">\sum_C\left[n_Ck_C-\binom{k_C+1}{2}\right]</code>, <code class="math">k_C=\min\{h+1,q_C\}</code>

**Vertex lists of size <code class="math">d_v</code>, computed feature rank <code class="math">t</code>**

<code class="math">nt-\binom{t+1}{2}</code>, <code class="math">t\le\min\left\{n,\binom{h+d_v}{d_v}\right\}</code>

**Vertex and extra-edge lists, degrees <code class="math">d_v,d_e</code>**

<code class="math">\min\left\{m,n\binom{h+d_v+d_e}{d_v+d_e}\right\}</code>

**One color per vertex and per edge; at least <code class="math">h+1</code> vertex colors in a component**

<code class="math">n\binom{h+2}{2}-\binom{h+3}{3}</code>, componentwise

**General mixed-color rank refinement**

Subtract <code class="math">\binom{h+3}{3}-\binom{h-t+3}{3}</code> from <code class="math">n\binom{h+2}{2}</code>

**One failed color, near-linear construction**

<code class="math">O\!\left((m+A)[\log^4(n+2)+\log(m+2)]+ar\right)</code>, plus input organization; <code class="math">a=2d_v+d_e</code>, <code class="math">A\le am</code>, <code class="math">r=</code> MSF size

**One failed color, total difference lists**

<code class="math">\sum_c\lvert R_c\rvert\le ar</code>; indexed cost lookup <code class="math">O(1)</code>

When the list-feature dimension is gated out, the algorithm claims the parameter envelope at <code class="math">t=\min\left\{n,\binom{h+d_v}{d_v}\right\}</code>; the sharper actual-rank bound requires computing that rank.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
