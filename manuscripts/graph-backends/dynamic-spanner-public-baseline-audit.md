# Deterministic dynamic spanners: current public baselines and admissible comparisons

**Primary-source audit, 25 October 2026.**

This note audits the comparison for
[clipped-walk-queries-and-dynamic-spanner.md](clipped-walk-queries-and-dynamic-spanner.md). A dynamic spanner is an
explicit subgraph of an undirected input graph. Numerical APSP estimates
alone are not that output. Randomized adaptive algorithms, deterministic
algorithms, worst-case update time, amortized update time, and total
recourse are kept as distinct guarantees below.

The defensible comparison is with named, quantitatively audited public
constructions. This audit does not establish that the best possible
retuning of every public spanner framework has been found.

## 1. Source and version ledger

| Source | Audited guarantee and scope | Qualification for this project |
|---|---|---|
| Kyng--Meierhans--Zoecklein (KMZ), *A Simple Dynamic Spanner via APSP*, ICALP 2025, Lemma 11, Corollary 10, Theorem 12 | Unweighted undirected graphs, initially empty, fixed vertex set; a path-reporting APSP reduction with a separate insertion-query term and spanner-maintenance term | Its formal publication contains a new Section 5 beyond arXiv:2408.11368v1. The arbitrary-deletion batching must be compared too. |
| KMZ, published Section 5, Lemma 13 and Theorem 18 | Fully dynamic spanners via batching; stretch, density, and time all depend on the number of sparsification layers | One must pay initialization and deletion clocks at every layer. A one-layer few-deletion bound is not already this guarantee. |
| Chuzhoy--Parter (CP), arXiv:2601.20718v1, Theorem 1.1 | Deterministic, simple undirected graphs, polynomially bounded positive integer lengths, worst-case updates and recourse | The growing-parameter restrictions are material; see Section 4. |
| Meierhans--Probst Gutenberg--Saranurak (MGS), arXiv:2504.00544v1, Theorem 1.4 | Randomized adaptive maintenance of distance/cut/spectral sparsifiers, with polynomial logarithmic approximation, size overhead, worst-case update time and recourse | The expander pruner is deterministic, but the sparsifier client also samples edges. Replacing static decomposition alone does not derandomize this theorem. |
| Bernstein et al., *Fully-Dynamic Graph Sparsifiers Against an Adaptive Adversary*, arXiv:2004.08432v3, Section 10.1 | Randomized adaptive spanners; Theorems 10.1 and 10.2 distinguish amortized and worst-case updates | Their local sparsifier from Section 9 is independently randomized. |
| Bhattacharya--Saranurak--Sukprasert, arXiv:2207.04954v1 | Near-optimal deterministic recourse for greedy spanners; a separate efficient adaptive 3-spanner result | A recourse theorem without a suitable running-time bound is not a faster deterministic implementation of the present target. |

Primary links:

* [KMZ ICALP 2025 publication](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.111),
  [published HTML](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.111/LIPIcs.ICALP.2025.111.html),
  and [arXiv history](https://arxiv.org/abs/2408.11368).
* [CP current full version](https://arxiv.org/html/2601.20718v1) and
  [version history](https://arxiv.org/abs/2601.20718).
* [MGS current full version](https://arxiv.org/html/2504.00544v1) and
  [version history](https://arxiv.org/abs/2504.00544).
* [Bernstein et al. current full version](https://arxiv.org/html/2004.08432v3).
* [Bhattacharya et al. full version](https://arxiv.org/pdf/2207.04954).

The arXiv histories checked on the audit date list only v1 for KMZ's
simple-spanner preprint, CP, and MGS. This does **not** make KMZ's arXiv
v1 the most informative version: its official conference publication
adds the lower-stretch and arbitrary-deletion material.

## 2. The precise few-deletion ledger

Use the notation `gamma` for an APSP approximation bound, `alpha` for
its amortized update cost, and `beta` for numerical-query overhead.
KMZ's actual implementation asks for a path only when its stored upper
distance estimate is at most

```math
R=2\gamma\log n.
```

Consequently an interface returning a simple path in
`O((R+1) beta)` time for an accepted estimate suffices. The stronger
Definition 5 promise of time proportional to the final simple path
length is unnecessary for this application. This is a direct reading
of the cost proof of published Lemma 11, not a replacement of the
APSP definition for unrelated clients.

For at most `m >= n` insertions and at most `n` deletions, the bound is

```math
T=O\bigl(m\gamma\beta\log n+
               n\gamma\alpha\log n\bigr),             \tag{1}
```

with stretch `2 gamma log n`, size `O(n gamma log n)`, and total
recourse `O(n gamma log n)`. For the last assertion use published
Corollary 10 with `K=m/n`. Theorem 12's displayed recourse includes
an extra `alpha`; Corollary 10 and the preceding inventory proof give
the sharper bound independently of APSP processing cost.

Equation (1) has two different causes. Every input insertion may ask
for a witness and enumerate a bounded-length route. Only the smaller
spanner transcript is sent to the dynamic APSP structure. Faster APSP
updates improve the second term; they do not erase the first.

For polynomial-length histories under a declared master `N`, set
`U=log(N+4)` and `h=log(U+4)`. At the already audited common stretch
scale

```math
a=U^{5/7}h^{2/7},
```

the project has the following comparison of certified upper envelopes:

| APSP implementation | Logarithm of update overhead | Few-deletion total work |
|---|---:|---:|
| Jointly retuned public construction | `O(U^(6/7) h^(1/7))` | `m exp O(a) + n exp O(a + U^(6/7) h^(1/7))` |
| Separated research construction | `O(U^(23/28) h^(5/28))` | `m exp O(a) + n exp O(a + U^(23/28) h^(5/28))` |

Polynomial logarithmic factors are included in these expressions.
The public row has a legitimate clipped-walk implementation, as
checked in Section 3. These are the same asymptotic stretch scale,
not an equality between unspecified constants in two `O` terms.

The elementary baseline `H=G` must also be applied. If a current edge
cap `M` is at most the allowed spanner size, this gives stretch one
and linear total work. Its recourse is at most `M+2D`, since
`m0+I=|E(G_final)|+D`. Thus `m=Theta(n)` is not a meaningful
competitive improvement example for the table above.

A nontrivial comparison window is instead
`m/n=exp(Theta(U^(3/4)))` with at most `n` deletions: the input
can exceed the common size cap, while the shared insertion term is
smaller than both displayed maintenance terms. At polynomial density
`m/n=n^c` for a fixed positive constant `c`, that shared insertion
term can dominate both bounds. The table then does not establish a
leading-order total-time improvement. The structural advantage of
low recourse when insertions greatly outnumber deletions already
belongs to KMZ's reduction.

## 3. The public numerical baseline also supports clipped reporting

It would be unfair to treat the public `6/7` numerical hierarchy as
ineligible merely because the audit of its numerical theorem did not
state a general simple-path API. Retain its local ball shortest-path
trees, nearest-pivot paths, and core-edge witnesses. These are the
actual constructive objects in the public hierarchy. Their local
maintenance is included in its fixed-polynomial local work allowance.

For its positive binary-port adapter, let `H_i=poly(U)` be the
per-boundary scaling of real edge lengths, and write

```math
\sigma_j=\prod_{i\le j} H_i
                       \le \exp O(dh).
```

Connectors have positive integral length. Their image in the previous
physical graph can be empty, but they are still charged as native
occurrences in their own graph. All other native edges have stored
parent walks whose lengths are bounded by the edge's declared metric
length after the prescribed scaling.

A root query upper estimate `Q` is the sum of nonnegative local-leg
contributions in normalized units. Expanding its witness to level `j`
therefore gives total native length at most `sigma_j Q`, including
the legs entering at intermediate levels. Positivity bounds the
number of native edge occurrences at that level by the same quantity.
Enumerating all levels and then erasing cycles consequently costs

```math
(Q+1)\exp O(dh)\mathrm{poly}(U).  \tag{2}
```

In the public `6/7` point, `dh=O(U^(1/7)h^(6/7))=o(a)`. Thus the
extra factor in (2) does not change either exponent in Section 2.
One can declare a common output envelope that dominates each
implementation's actual approximation times its clipped-query
overhead. The algorithm can still use its actual approximation for
the admission threshold; inflating the declared output envelope does
not require increasing that threshold a second time.

This argument makes no claim of output-sensitive running time in the
length of the **final** loop-erased path. It pays for the accepted
length budget. It also uses only public positive port scaling and
constructive witnesses; it does not import the research full-pool
forest lift into the public baseline.

## 4. CP's legal parameter range

CP Theorem 1.1 permits

```math
512\le k\le (\log n)^{1/49},\qquad
             1/k\le\delta\le1/400,
```

and supplies stretch `poly(k) 2^(O(delta^-6))`, size
`O(n^(1+O(1/k)))`, worst-case update cost `n^(O(delta))`, and
recourse `n^(O(1/k))`.

At the fastest displayed asymptotic parameter choice,
`k=Theta((log n)^(1/49))` and `delta=Theta(1/k)`, these give

```math
\begin{split}
 \log(\text{update envelope})&=O((\log n)^{48/49}),\\
 \log(\text{size}/n)&=O((\log n)^{48/49}),\\
 \log(\text{stretch})&=O((\log n)^{6/49}+\log\log n).
\end{split}                                                    \tag{3}
```

This is a different tradeoff: much smaller stretch, and a larger
certified time and size envelope. A substitution such as
`k=(log n)^(2/7)` is outside the stated theorem. Conversely, (3) is
not a runtime lower bound for CP's algorithm; it is what its
displayed uniform parameter domain certifies. It does not certify
domination of the research `23/28` few-deletion point or the audited
`5/6` fully dynamic balanced point.

The research spanner statement remains amortized. It does not replace
CP's worst-case guarantee. CP's simple-graph and integer-length scope
also remains explicit.

## 5. Why the randomized pruning application is not a deterministic baseline

MGS Theorem 1.3 is a deterministic expander-pruning theorem. Its
Theorem 1.4, by contrast, explicitly states a randomized algorithm
for the sparsifier applications. This distinction cannot be removed
by substituting CGLN's deterministic static decomposition alone.

In Bernstein et al. Section 9, Algorithm 9.6 samples incident edges
independently, and Algorithm 9.8 refreshes those random samples after
updates. Theorem 9.38 is the resulting local expander sparsifier.
Section 10.1 invokes it in the spanner construction, while the
worst-case variant uses Lemma 9.39. That source of randomness is
separate from finding the initial expander decomposition.

Thus the very strong polynomial logarithmic adaptive results belong
in the comparison table, but they do not already prove a
deterministic `2/3` or polynomial logarithmic dynamic spanner through
the one-line replacement suggested above. A new deterministic local
expander-sparsifier implementation could change this assessment; no
such implementation is being assumed here.

## 6. Other public APSP and recourse routes

The numerical APSP source audit is
[apsp-public-parameter-and-query-audit.md](apsp-public-parameter-and-query-audit.md). It covers KMG, KMZ's
bootstrapped APSP, Haeupler--Long--Saranurak (HLS), and Chuzhoy--Zhang
(CZ), with their update, query, and growing-parameter ranges.

In particular, [HLS arXiv:2402.18541v2](https://arxiv.org/abs/2402.18541)
allows `epsilon >= log^(-c)n` for a sufficiently small constant `c`,
has approximation `2^(poly(1/epsilon))`, and gives worst-case update
time `O(n^epsilon)`. KMZ's published Theorems 19--20 retain that
restriction when obtaining low-stretch fully dynamic spanners.
Writing `epsilon=(log n)^(-1/6)` or `epsilon=(log n)^(-3/14)` without
checking that range and its uniform internal costs is not a verified
comparison. The HLS construction has not been fully reoptimized here;
we do not infer a lower bound for it from this restriction.

The legal KMZ APSP retuning already recorded in the source audit has
update log-envelope `O(U log(h+4)/h)`, with a choice of any fixed
positive power `U^a0` as a stretch-log upper bound. This is useful
for other approximation regimes but is asymptotically larger than
the fixed-power time envelopes discussed here.

Greedy spanners already admit very strong recourse guarantees without
the efficient path search used here. In particular, ignoring running
time, the elementary deletion-repair greedy construction maintains
high girth and total recourse proportional to its size plus deletions.
The new application cannot be advertised as the first low-recourse
spanner, nor as an improvement to the optimal size--stretch relation.

The current-source search also checked 2026 publications and authors'
public lists. It found no additional primary theorem that clearly
dominates the stated deterministic point in the same time, stretch,
size, and recourse regime. This is a bounded literature audit, not a
claim that no different public-framework derivation can exist.

## 7. Arbitrary deletions: audited comparison

Published KMZ Section 5 is an applicable second outer reduction. If
an APSP core has update log-cost `B` and approximation log `A`, and
the outer batching shrink is `K=exp(z)`, its audited quantitative
ledger is

```math
Z=O\bigl(B+z+(U/z)(A+h)\bigr),\qquad
  \log(\text{stretch}),\ \log(\text{size}/n)
        =O\bigl((U/z)(A+h)\bigr),                       \tag{4}
```

using `kappa=Theta(U)` and at least one actual outer layer. The
initialization clocks and current-inventory implementation are proved
in [dynamic spanners proof](../../problems/dynamic-spanners/proof.md) and independently checked
in [A direct dynamic spanner from tracked terminal forests](../../problems/dynamic-spanners/proof.md). The latter audit
checks actual initial size, cumulative insertions, original deletion
clocks, physical edge lifetimes, and output recourse.

The public joint point `B=O(U^(6/7)h^(1/7))`,
`A=O(U^(5/7)h^(2/7))`, and `z=Theta(U^(6/7)h^(1/7))` make every
term in (4) at most the `6/7` scale. The research family instead
allows a balanced `5/6` scale under the same outer accounting.
This is an improvement of the audited public pipeline in the
simultaneous time/stretch/density envelope, conditional on the
research-provider imports. It is not an unqualified theorem about
every possible dynamic-spanner algorithm.

There is also a comparison at the **same final** stretch and density
log `S=U^(5/6)h^(1/6)`. The public family
`B=O(U/t+t^6h), A=O(t^5h)` with
`t=Theta((U/h)^(5/36))` and `z=Theta(U/t)` has time log
`O(U^(31/36)h^(5/36))`, while its final stretch, density, and
recourse logs are all `O(S)`. The research wrapper has time log
`O(S)` at that same output envelope.

The companion audit also optimizes variable public parameters in the
named positive-charge model. In the dense-cap regime it gives the
necessary budget inequalities
`B^7=Omega(U^6h)`, `A_charge=Omega(U^5h/B^5)`, and
`Z=Omega(max(U^(6/7)h^(1/7),U(h/S)^(1/6)))`.
These describe the constructive accounting model, not lower bounds
for dynamic spanners or their actual stretch. They do not exclude a
different public framework or a sharper analysis outside that model.

The deletion-bounded conclusion (1) also remains independently valid.
