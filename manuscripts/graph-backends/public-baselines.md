# Public baseline audit: deterministic exact general-graph matching

Audit date: 24 October 2026. Scope: explicit maximum-cardinality matching in an arbitrary simple undirected graph, with `n` vertices and `m` edges. All vertices, including isolates, count in the input. This note is an intermediate research record, not a claim of a new algorithm.

## Verified benchmark

The strongest unrestricted deterministic bound verified in this search is the Goldberg–Karzanov refinement

```math
O\!\left(m\sqrt n\,\frac{\log(n^2/m)}{\log n}\right),
```

under the usual nontrivial-input convention `n = O(m)`. Read and remove isolates in `O(n+m)` time to apply this to arbitrary adjacency-list inputs. The simpler classical benchmark is `O(m sqrt(n))`, achieved by the Micali–Vazirani, Gabow–Tarjan, and Gabow frameworks. At fixed polynomial densities `m = Theta(n^a)`, `1 <= a < 2`, the exponent is `a+1/2`; at density `Theta(n^2)` the refinement gives `O(n^(5/2)/log n)`. Thus a claimed `n^(5/2)` deterministic dense algorithm or a logarithmic improvement cannot be called a new polynomial-exponent breakthrough.

The source for the refinement is Goldberg and Karzanov, *Maximum skew-symmetric flows and matchings*, Mathematical Programming 100 (2004), 537–568, Theorem 10.3. The method is a deterministic extension of Feder–Motwani clique compression to skew-symmetric matching networks. Its preprocessing is itself charged in the displayed bound.

Primary sources:

- https://arxiv.org/html/math/0304290v2 — Section 10, Theorem 10.3.
- https://arxiv.org/abs/math/0304290v2 — abstract, submission history, journal metadata.
- https://www.microsoft.com/en-us/research/publication/maximum-skew-symmetric-flows-and-matchings/ — author/institution publication record.
- https://arxiv.org/abs/2409.14849 — Ansaripour, Danaei, Mehlhorn, *Gabow's Cardinality Matching Algorithm in General Graphs: Implementation and Experiments* (2024).

The last two classic bounds are not assertions of a matching lower bound. An algorithm faster than them could exist. The literature search did not reveal a later verified unrestricted deterministic polynomial-exponent improvement.

## Results that must not be substituted for this target

| Result | Guarantee | Why it does not settle this task |
|---|---|---|
| Harvey / Mucha–Sankowski algebraic matching | Randomized `O(n^omega)` arithmetic-operation algorithm; explicit output | Randomization is essential to the stated theorem. |
| Dani–Hayes–Pettie, September 2026 | Deterministic `O(n^2)` on `d`-regular graphs; `O((Delta+1-d)n^2)` if all degrees lie in `[d,Delta]` | Regularity/degree spread is a genuine hypothesis. It is not an arbitrary-graph exponent improvement. |
| Deterministic almost-linear integral flow | Solves directed integral flows and hence bipartite matching | Odd-set/blossom constraints remain in nonbipartite matching. |
| 2026 dynamic maximal matching | Maintains a maximal matching with sublinear amortized updates | Maximal is not maximum, and updates are not static exact solution time. |
| July 2026 communication protocol | `O~(n^(3/2))` communicated bits | Local computation is uncharged. It is not a sequential running-time bound. |
| October 2026 linear matroid parity | Deterministic `O(N r^2)` after fast matrix multiplication | More general problem, different parameters; specializing does not improve the above matching benchmark. |
| Izumi–Kitamura–Yamaguchi, November 2025, arXiv:2511.08210 | A simpler sequential exact augmentation framework; deterministic distributed and semi-streaming approximation improvements | The primary abstract explicitly describes the sequential algorithm as slower than MV. The improved distributed/semi-streaming results are `(1-epsilon)` approximations, not a faster sequential exact general-matching bound. |
| Mehlhorn–Nobahari, March/April 2026, arXiv:2603.22909 | Revisited analysis and implementation of Gabow's `O(m sqrt(n))` general-graph algorithm | A useful primary account of blocking phases, not a new polynomial exponent. |

Primary sources:

- https://people.csail.mit.edu/nickh/Publications/AlgebraicMatching/AlgebraicMatching.pdf — Harvey, *Algebraic Structures and Algorithms for Matching and Matroid Problems*, Sections 1.4 and 3. Its stated general matching algorithm is randomized.
- https://arxiv.org/html/2609.14126v1 — Dani, Hayes, Pettie, *Maximum Matching on Regular Nonbipartite Graphs*, Theorem 6 and Appendix B. Its introduction explicitly lists the longstanding unrestricted `O(m sqrt(n))` and `O(n^omega)` bounds (suppressing the former's known logarithmic refinement).
- https://arxiv.org/html/2607.05751v1 — Cheng, Jiang, Sawettamalya, Yu, *On the Communication Complexity of Maximum Matching and Negative-Weight Shortest Paths*, Theorem 1.1.
- https://arxiv.org/abs/2610.03030 — Hamada, Iwata, *A Shortest Augmenting Path Algorithm for Linear Matroid Parity*.
- https://arxiv.org/abs/2511.08210 — Izumi, Kitamura, Yamaguchi, *Forgetting Alternation and Blossoms: A New Framework for Fast Matching Augmentation and Its Applications to Sequential/Distributed/Streaming Computation*, submitted 11 November 2025; the sequential/distributed distinction is explicit in the abstract.
- https://arxiv.org/pdf/2603.22909 — Mehlhorn, Nobahari, *Gabow's O(sqrt(n)m) Maximum Cardinality Matching Algorithm, Revisited*, April 2026 revision, especially Section 4.

Geelen's deterministic algebraic substitution algorithm is also not a fast-`n^omega` deterministic matching algorithm. The original paper expressly describes its implementation as computationally unattractive and not competitive with augmenting-path matching. Source: https://www.math.uwaterloo.ca/~jfgeelen/Publications/matching.pdf , pp. 62–63.

## OAI baseline identification

The relevant source is OpenAI's manuscript *Almost-Linear-Time Maximum-Cardinality Matching in General Graphs*, dated 24 September 2026. It is family 120 in the release; the mirror PDF identifier 239 is unrelated to the family number. Its official directory contains the historical word `Sparse`, but Theorem 1.1 states the result for arbitrary simple graphs, measured in `p=n+m`.

Theorem 1.1 is randomized: one uniform word-RAM program uses at most `C p^(1+eta(p))` instructions on every random computation path, with `eta(p)->0`, and returns an explicit optimum with probability at least `2/3`. This is a worst-case runtime cap over random paths, not a deterministic success guarantee. Edmonds' deterministic polynomial fallback and deterministic checking of sampled structures do not change that distinction.

Official sources:

- https://github.com/openai/math/blob/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/main.pdf
- https://github.com/openai/math/blob/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/build/sections/01-introduction.tex
- https://github.com/openai/math — README describes the varying verification status of the model-produced manuscripts.

Convenient mirror (the manuscript itself, not the generated explanation): https://www.emergentmind.com/openai-math-explorer/papers/239.pdf?v=adc7f12

This audit identifies the statement, provenance, and randomization status. It is not a full independent verification of its 86-page proof. Derandomizing its components requires proving the replacement's construction cost and its compatibility with adaptive states; verifying a candidate sample alone does not provide an efficient deterministic search for it.

## Late-October primary-source refresh

A further primary-source search through **24 October 2026** did not find
an unrestricted deterministic sequential exact-matching theorem that
changes the verified benchmark above. This is a report of what was
located and checked, not a proof that no such result exists.

Two newly checked October results should not be mistaken for such a theorem:

- **Tatsuya Terao, 15 October 2026**, *Improved Pass Complexity for
  Semi-Streaming Matching in General Graphs via Budgeted Price Approach*,
  [arXiv:2610.22718v1](https://arxiv.org/html/2610.22718v1), Theorem 1:
  deterministic `(1-epsilon)` approximation in `O(1/epsilon^2)` passes
  and `O(n/epsilon^2)` words. Its Section 3.3 enumerates a grid of price
  vectors, and Section 4 explicitly says that the running time of the
  presented algorithm is exponential in `n` and `1/epsilon`. A future
  polynomial-time version is announced without its proof in this version.
  Thus the pass theorem is neither a fast sequential exact algorithm nor
  a verified additive-input-time warm-start primitive.
- **Quanlong Niu and Riheng Jia, 20 October 2026**,
  [arXiv:2610.27833](https://arxiv.org/abs/2610.27833): a `2/3`
  approximation in `O(n^5)` time for the *residual* maximum-matching
  objective, which chooses a maximum matching whose deletion leaves a
  large matching number. Its objective and running time do not supply
  a faster ordinary exact maximum-cardinality algorithm.

The **15 October v2** of Hamada--Iwata,
[arXiv:2610.03030](https://arxiv.org/abs/2610.03030), still states
`O(n r^2 log r)` deterministic linear-matroid-parity time, reduced to
`O(n r^2)` with fast matrix multiplication. This does not change the
general-graph matching comparison already recorded. The September
regular-graph result still requires its degree conditions; its
`O(n^2)` conclusion cannot be transferred to arbitrary inputs without
paying for a valid reduction.

The official current OAI introduction was reopened. It explicitly
allows disconnected graphs and isolates, makes no perfect-matching
promise, and claims the bound in `p=n+m` for every simple undirected
unweighted input. The historical directory word `Sparse` remains
irrelevant to that final theorem's scope. The material restriction for
this project remains **randomized success probability at least 2/3**,
even though its time cap holds on every random computation path. Its
stated word-RAM includes fixed-word multiplication, integer division,
and charged multiword work. It does not claim a deterministic exact
theorem or a weighted-matching extension in Theorem 1.1. Handling
parallel records and loops in our input guarantee is the separately
proved cardinality-preserving cleanup, not an additional assumption
silently read into the OAI statement.

Official source:
[current introduction](https://github.com/openai/math/blob/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/build/sections/01-introduction.tex).
The [repository README](https://github.com/openai/math) continues to
describe a collection at different stages of verification and the
possibility of issues in unformalized results; it is not evidence that
this particular proof assembly has been externally certified.
