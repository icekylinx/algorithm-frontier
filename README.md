# Algorithm Frontier

Research manuscripts on deterministic algorithms, combinatorial optimization, dynamic graphs, and sparsification. The catalogue below lists every result family; each entry opens a precise statement, complete proofs, and its computational assumptions.

[![Repository checks](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml/badge.svg)](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml) [![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

**53 result families · 18 supporting results** · [Complete proof index](CONTENTS.md) · [Complexity conventions](docs/COMPLEXITY.md) · [Verification evidence](reviews/README.md) · [Citation](CITATION.cff)

## Results

- [Subset Sum](#subset-sum)
- [Numeric targets and quota geometry](#numeric-targets-and-quota-geometry)
- [Graph algorithms](#graph-algorithms)
- [Exact failures, persistence and compilation](#exact-failures-persistence-and-compilation)
- [Spectral, group and quantum sparsification](#spectral-group-and-quantum-sparsification)
- [Allocation and resource matroids](#allocation-and-resource-matroids)
- [Selected flow and robust allocation](#selected-flow-and-robust-allocation)
- [Scheduling](#scheduling)
- [Matching certificates and oracle barriers](#matching-certificates-and-oracle-barriers)
- [Supporting results](#supporting-results)

A displayed conditional composition includes its named backend hypotheses. Oracle bounds, explicit-input algorithms, support sizes, query costs, and existence theorems keep their distinct meanings. Exact rational constants and complete parameter ranges are stated on the linked cards.

Every entry states its [randomness contract](docs/RANDOMNESS.md): deterministic, Monte Carlo, Las Vegas, or a separately identified existence theorem, structural result or lower bound. A supplied randomized backend must retain its own confidence and adversary assumptions.

### Subset Sum

Time counts deterministic bit operations; $L$ is the complete input length. The two entries describe separate algorithms.

#### [Faster deterministic Subset Sum](problems/subset-sum-fast-deterministic/)

Exact decision and indexed witness.

**Randomness.** Deterministic exact algorithm in the uniform bit model, including indexed-witness recovery and input-independent deterministic circuit construction; no probability of error.

**Quantitative result.**

$$
C+\mathrm{poly}(n,L)2^{0.495891928n}
$$

Exact rational exponent on the card.

**Model and scope.** Exact rational certification of all 44 continuous contact branches; C is finite input-independent circuit precomputation; combinatorial compiler and bit-cost proofs are in the manuscript.

#### [Low-space deterministic Subset Sum](problems/subset-sum-low-space-deterministic/)

Exact decision and indexed witness.

**Randomness.** Deterministic exact algorithm in the uniform bit model, including indexed-witness recovery; the writable-space and restricted-range variants have no probability of error.

**Quantitative result.**

Time $\mathrm{poly}(n,L)2^{n/2}$.

Writable bits:

$$
\mathrm{poly}(n,L)2^{0.18261635770550353n}
$$

**Model and scope.** Also half-exponential time and $O^*(2^{n/6})$ space for the stated two-short-range input class.

### Numeric targets and quota geometry

Every bound includes polynomial work in the full encoded input. Binary resource counts remain compressed, and mandatory bases retain their original total.

#### [Numeric targets and support patterns](problems/numeric-target-frontier/)

Exact mixed targets and signed-scalar optimization.

**Randomness.** Deterministic upper algorithms in the stated exact rank/optimization-oracle model. The success-probability-2/3 randomized statement is an oracle lower bound, not a randomized upper algorithm.

**Quantitative result.**

$$
2^{O(T\log(2+\min\{Q/T,T\}))}
$$

Fixed dimension $\exp(O_d((T+1)^{d/(d+1)}))$.

One-target decision $2^{O(\sqrt{T+1})}$.

**Model and scope.** $T,Q>0$ in the first formula; zero cases are polynomial. Also unequal targets, overlap/components, stars, seven accuracy schemes and aligned nonlinear transfers.

#### [Prefix, laminar and sparse quotas](problems/weighted-prefix-quota-frontier/)

Exact quota algorithms and deterministic original-ground kernels.

**Randomness.** Deterministic exact algorithms and deterministic original-ground reductions in the stated exact oracle model; universal colorings are explicitly enumerated rather than sampled.

**Quantitative result.**

One order $2^{O(B)}$.

Two orders $2^{O(B\log(B+2))}$.

$p$ weight families $2^{O(pB\log(p+2))}$.

Laminar $2^{O(B^2)}$.

**Model and scope.** Also support/family tradeoffs, sparse quotas, coverable/transversal kernels, and edge-matroid matching kernels.

### Graph algorithms

Use each result’s declared graph cap N, with $U=\log(N+4)$, $h=\log(U+4)$ and $\mathcal E_a=\exp(O(U^ah^{1-a}))$. The flow entry instead displays its numerical cap S explicitly. Conditional compositions retain their named hierarchy, raw-cycle and lifetime interfaces; the MSF entry is a derived public baseline.

#### [Maximum-cardinality matching](problems/general-matching/)

Exact matching with original edge identifiers.

**Randomness.** Deterministic conditional composition, requiring deterministic external primitives and a deterministic implementation of Contract R.

**Quantitative result.**

$$
O(n+m)+(m_s+1)\mathcal E_{4/5}
$$

Optional $m_H=O(\nu(G)^2)$ kernel.

**Model and scope.** Conditional on raw-backend Contract R and the named external primitives.

#### [Degree-constrained subgraphs](problems/degree-constrained-subgraphs/)

Exact factors, interval degrees and cardinality optimization.

**Randomness.** Deterministic reductions conditional on the deterministic matching backend, including Contract R and its external primitives.

**Quantitative result.**

$$
O(n+m)+(m+1)\mathcal E_{4/5}
$$

**Model and scope.** Loopless multigraph; capacity one per explicit edge record; conditional matching backend.

#### [Static and threshold min-cost flow](problems/min-cost-flow/)

Exact integral optimum or threshold witness.

**Randomness.** Deterministic exact numerical client conditional on the stated deterministic raw-cycle/lifetime backend, including its guarantees for adaptive polynomial-length histories.

**Quantitative result.**

$O((N+1)E(S)^4\mathrm{polylog}S)$.

$$
E(S)=\exp(O((\log S)^{4/5}(\log\log(S+4))^{1/5}))
$$

**Model and scope.** Conditional raw-cycle lifetime and initialization interfaces; numerical cap S; full-flow output charged separately.

#### [Incremental strongly connected components](problems/incremental-scc/)

Exact component labels.

**Randomness.** Deterministic conditional composition using the deterministic raw-cycle backend and exact nonzero-base, flow-maintenance and retirement interfaces; no randomized error allowance is stated.

**Quantitative result.**

Total:

$$
(n+m)\mathcal E_{4/5}^{O(1)}\mathrm{poly}(U)
$$

**Model and scope.** Conditional raw-cycle/retirement interface; total insertion work; component labels only.

#### [Incremental directed SSSP](problems/incremental-sssp/)

$(1+\epsilon)$ distances and simple paths.

**Randomness.** Deterministic conditional composition; its raw-cycle and retirement backend is explicitly required to be deterministic and to support adaptive updates.

**Quantitative result.**

Total:

$$
(n+m)\exp(O(U^{4/5}h^{1/5}+\sqrt{U(h+\log(1/\epsilon))}))
$$

**Model and scope.** Conditional detector/retirement interface; positive polynomial-range lengths; $0<\epsilon\le1/2$, $\log(1/\epsilon)=O(U)$; $k$-edge output costs $(k+1)\mathrm{poly}(U)$.

#### [Fully dynamic APSP](problems/apsp-frontier/)

A family of update/stretch tradeoffs.

**Randomness.** Deterministic conditional composition under the normalized deterministic metric-hierarchy contract, including its construction, update and query interfaces.

**Quantitative result.**

Amortized factor $\exp(O(U/t+t^3h))$.

Stretch $\exp(O(t^4h))$.

Query $\mathrm{poly}(U)$.

**Model and scope.** Conditional metric hierarchy; $t\to\infty$, $t^2h=o(U)$; positive polynomial-range lengths; five explicit parameter points.

#### [Dynamic spanners](problems/dynamic-spanners/)

Two distinct stretch/recourse regimes.

**Randomness.** Both displayed spanner constructions are deterministic conditional on the stated deterministic hierarchy and forest interfaces. Randomized public baselines are comparisons only.

**Quantitative result.**

Tracked terminals $\mathcal E_{4/5}$.

Full-horizon $\mathcal E_{5/6}$ with recourse $(n+D)\mathcal E_{5/6}$.

**Model and scope.** Conditional hierarchy interfaces; unweighted graph; amortized work includes initial inventory, insertions and deletions.

#### [Dynamic minimum spanning forest](problems/dynamic-msf/)

Exact fully dynamic MSF.

**Randomness.** Deterministic derived public baseline using deterministic decomposition and pruning in the stated worst-case MSF reduction.

**Quantitative result.**

Worst-case update $\mathcal E_{2/3}$.

**Model and scope.** Derived public baseline using the stated decomposition and pruning results.

#### [Strong forests and Gomory–Hu trees](problems/decremental-strong-forest/)

Decremental strong forest; exact cut-equivalent tree.

**Randomness.** Deterministic conditional composition; the strong forest and exact Gomory-Hu transfer require the named deterministic hierarchy, flow, skeleton and guide-tree interfaces.

**Quantitative result.**

$$
O(n+m)+(m+1)\mathcal E_{6/7}
$$

**Model and scope.** Conditional forest/flow interfaces; bounded-degree native forest; arbitrary-degree cut-tree transfer with positive polynomial-range integer capacities.

### Exact failures, persistence and compilation

Support bounds count retained original objects. They are shown separately from preprocessing and query costs. Let $h$ be the failure budget and $d$ the maximum labels per item where applicable.

#### [Single-failure optimum preservers](problems/exact-failure-preservers/)

Weighted and valuated two-matroid intersection; rooted arborescences.

**Randomness.** Deterministic preprocessing and reporting in the stated oracle model, including the valuated and arborescence variants. Randomness is not required by the distance-preserver reporting construction.

**Quantitative result.**

Matroids: $O(k^{3/2})$ support/records, $O(k)$ reporting.

Arborescences: $O(n^{3/2})$, $O(n)$.

**Model and scope.** Deterministic polynomial preprocessing; arborescences $\widetilde O(mn)$ arithmetic work; effective-domain initialization for valuations.

#### [Flow, matching and price sensitivity](problems/exact-flow-sensitivity/)

Unit-flow/path failures, general matching, two matroids and one-element prices.

**Randomness.** Deterministic preprocessing and queries in each stated flow, matching, matroid and price-sensitivity model; the required exact optimization and independence oracles retain their specified costs.

**Quantitative result.**

Flow $O(n^{3/2}\lambda^{1/4})$.

Matching $4\mu+2$ edges, or $6\mu+2$ for edge/vertex failure.

Matroids $2r+k\le3r$.

Prices $O(N+r\sqrt{\min\{N,r^2\}})$.

**Model and scope.** Flow exponent: simple unit-capacity digraph and nonnegative costs. Matching/matroid failures preserve cardinality; each reporting bound is model-specific.

#### [Matroid and submodular failure summaries](problems/matroid-failure-summaries/)

Represented fixed-cost prefixes; oracle rank and integer-submodular value preservation.

**Randomness.** Deterministic: represented weighted-prefix elimination, oracle-rank FPT/XP constructions and integer-submodular value-summary construction. Random label orderings occur only in the size-bound proof, not in these algorithms.

**Quantitative result.**

Rank: $r\binom{h+d}{d}$.

Integral submodular range $R$: $R\binom{h+d}{d}$.

Sharp marginal/entropy inequality.

**Model and scope.** Support capped by original ground size; uniform polynomial represented construction; parameterized oracle construction; rank-only oracle model has no weighted-prefix claim.

#### [Colored and vertex-failure graph certificates](problems/graph-color-failure-certificates/)

Exact surviving connectivity and canonical MSF.

**Randomness.** Deterministic preprocessing and exact queries. The near-linear single-color construction uses a deterministic dynamic-MSF backend with exchange reporting.

**Quantitative result.**

$\sum_C(n_Ck_C-\binom{k_C+1}{2})$, $k_C=\min\{h+1,q_C\}$.

**Model and scope.** Displayed bound: one color per vertex and a fixed weight order; overlapping vertex lists and additional edge labels have separate bounds.

#### [Resource-constrained packing summaries](problems/packing-matching-summaries/)

Weighted universal completion after deletions and forbidden vertices.

**Randomness.** Deterministic uniformly polynomial construction over the supplied rational or finite-field representation; no randomized representation, hashing or isolation step is assumed.

**Quantitative result.**

$$
\min\{N,r\binom{pK+h_v}{p}\prod_j\binom{h_j+d_j}{d_j}\}
$$

**Model and scope.** Explicit packing sets and represented resource; omit r when absent; full-input gate precedes lift expansion.

#### [Persistent-homology failure certificates](problems/persistence-failure-certificates/)

All surviving boundary spaces and lower-degree persistence modules.

**Randomness.** Deterministic uniformly polynomial construction for the explicit complex and supplied coefficient-field representation, valid simultaneously after every allowed failure.

**Quantitative result.**

$\min\{N,r\binom{h+a+b}{a+b}\}$ retained top simplices.

**Model and scope.** One fixed filtration over the stated field; full lower skeleton retained; homology degrees at most $p-1$.

#### [Boolean linear optimization compiler](problems/boolean-linear-compiler/)

Signed equalities, intervals, witnesses and lexicographic optimization.

**Randomness.** Deterministic compiler with a supplied deterministic indexed-witness Subset Sum backend; optimization, witnesses and the stated space transfer retain that same backend contract.

**Quantitative result.**

$$
\mathrm{poly}(L)(\prod_i p_i)2^{\alpha n+Q-(1-\alpha)B}
$$

**Model and scope.** Supplied indexed-witness Subset Sum backend of exponent $\alpha$; $0\le B\le Q$; a space bound requires that same backend.

### Spectral, group and quantum sparsification

Support counts retained original items and is capped by input size. Construction models remain separate from existence. For correlated failures, $\Gamma(h,d)=(h+d)^{h+d}/(h^hd^d)$, with $\Gamma=1$ when hd=0; Q counts allowed label sets, K is feature dimension, and $\rho$ is effective dimension.

#### [Correlated spectral, regression and seminorm summaries](problems/correlated-spectral-regression/)

PSD forms, norms, weak convex losses, graded incidence and simplicial spectra.

**Randomness.** Mixed. Importance pools are Monte Carlo with failure at most $\delta$; random-code variants have code failure at most $\zeta$, plus any ordinary sampler failure. One success event covers all allowed failures and later queries. Single-failure PSD/regression and coherence-code PSD alternatives are deterministic. Optimal arbitrary-seminorm support is existence only; its constructive alternative is Monte Carlo with the ordinary backend's high-probability guarantee and lifted-access assumptions.

**Quantitative result.**

PSD:

$$
O(\Gamma r\epsilon^{-2}\log(2rQ/\delta))
$$

Weak regression:

$$
O(\Gamma\rho\epsilon^{-1}\log(2(p+q)Q/\delta))
$$

Seminorm existence: $O(rK/\epsilon^2)$.

**Model and scope.** Capped original-item support; one event covers all failures; regression penalties are nonnegative convex; constructive seminorm bounds require the lifted backend.

#### [Label and whole-block cut sparsification](problems/label-block-cut/)

Exact incidence decoders, hyperedges, whole blocks and adaptive quotient resparsification.

**Randomness.** Monte Carlo randomized preprocessing, with success probability at least $2/3$ for one event covering every allowed failure and quotient/cut query. Queries and failed labels may be chosen after the summary is revealed. The exact label decoder and field-extension arithmetic are deterministic.

**Quantitative result.**

$$
O(\min\{m,R\log(2R/\epsilon)/\epsilon^2\})
$$

With $R=r\binom{h+k}{k}$ for incidence label deficit k.

**Model and scope.** Compact randomized whole-item construction; full-input gate; graph deficit a+b, hyperedge and commuting-block variants keep their distinct ranks.

#### [Finite groups, affine constraints and metrics](problems/group-metric-constraints/)

Cayley generators, subgroups/cosets, modular blocks and Hilbert metric sums.

**Randomness.** Mixed. Cayley matrix construction and rational-rank conversion are deterministic; the optional group-operations Cayley variant is Monte Carlo with failure at most $\delta$. Subgroup, coset and metric table constructions are Monte Carlo partial coloring with success at least $2/3$, using bounded fresh trials and certified table/separation checks under the stated precision contract. Compact modular blocks are Monte Carlo with success at least $2/3$. Optimal compact-input support and the unrestricted few-orbit seminorm branch are existence statements where no such construction is supplied.

**Quantitative result.**

Cayley:

$$
O(\epsilon^{-2}\log^3(2\lvert G\rvert))
$$

Subgroups:

$$
O(\epsilon^{-2}\log(2[G:\cap_eH_e]))
$$

Cosets:

$$
O(\epsilon^{-2}\log(2\lvert G\rvert))
$$

Transitive metrics $O(\epsilon^{-2}\log(2N))$.

**Model and scope.** Cayley construction uses explicit matrices; subgroup/coset/metric constructions use explicit query tables; compact modular construction has its separate logarithmic overhead.

#### [Pauli, qudit and stabilizer blocks](problems/quantum-stabilizer/)

Whole-check sparsification and commuting energy witnesses.

**Randomness.** Mixed. Compact and explicit-dimension whole-block sparsification are Monte Carlo with success at least $2/3$; correlated Pauli preprocessing succeeds with probability at least $1-\delta$ simultaneously for all allowed failures. Sharp support is existential in the compact-input model. Stabilizer-basis surrogate construction and the stated exponential exact witness enumeration are deterministic. All sampling is classical preprocessing randomness.

**Quantitative result.**

$R=\log_2(2D)$: support existence $O(\min\{m,R/\epsilon^2\})$.

Compact randomized:

$$
O(\min\{m,R\log(2R/\epsilon)/\epsilon^2\})
$$

**Model and scope.** Whole internally commuting blocks; arbitrary cross-block noncommutation. Sharper prime-dimensional bounds and separate $2+\sqrt2$ witness approximation are on the card; witness optimization is exponential.

#### [Exact-separation and non-Fano boundaries](problems/obstruction-boundaries/)

Compact relative-error-body membership and a precise fixed-amplitude matroid obstruction.

**Randomness.** Deterministic reductions, explicit constructions and exhaustive exact verification. The non-Fano sign probability describes a mathematical random-sign experiment, not a randomized algorithm or algorithm failure probability.

**Quantitative result.**

coNP-complete membership.

Non-Fano sign probability $15/128<1/8$.

**Model and scope.** Exact separation would decide the membership problem; the sign obstruction does not refute general sparsification.

### Allocation and resource matroids

Time entries suppress $\mathrm{poly}(H)$, or $\mathrm{poly}(H_\epsilon)$ for accuracy. Let $q$ be the candidate count, $r$ the selected rank, $c=q-r$, $\Gamma(R)=R^R/(R-1)^{R-1}$, and $E(q)=2^{O(q\log\log(q+2)/\log(q+2))}$.

#### [Arbitrary-value allocation scheme](problems/arbitrary-value-allocation-scheme/)

$(1-\epsilon)\mathrm{OPT}$ with exact setup and assignment budget.

**Randomness.** Deterministic profile and basis enumeration with paid exact rank, submodular-minimization, LP and intersection primitives.

**Quantitative result.**

$$
\binom qr\exp(O(r/\epsilon))
$$

**Model and scope.** Actual selected player basis; integer comparator.

#### [Recipient polymatroids](problems/recipient-polymatroid/)

Factor $4-3/r$; approximate availability and equal-unit extensions.

**Randomness.** Deterministic current-blocker search with paid exact primitives. A supplied factor-lambda availability oracle must satisfy its certified guarantee on every call.

**Quantitative result.**

$$
2^{O(r)}
$$

Relaxed factor has a rank-quasipolynomial alternative.

**Model and scope.** Integer comparator; binary repeated resources.

#### [Recipient-matroid configuration](problems/recipient-matroid-configuration/)

Factor $4-3/r$ against the configuration LP.

**Randomness.** Deterministic current-blocker search with exact paid primitives. The optional factor-lambda availability oracle requires a certified per-call guarantee.

**Quantitative result.**

$$
2^{O(r)}
$$

Factor $\lambda^{-1}+3-3/r$ with a certified local $\lambda$ oracle.

**Model and scope.** The configuration comparator is explicit.

#### [Explicit-item matroid union](problems/item-matroid-union/)

Factor $4-3/r$ against the configuration LP.

**Randomness.** Deterministic matroid-union reduction and current-blocker search, including both the exact rank-dependent factor and the relaxed quasipolynomial variant.

**Quantitative result.**

$$
2^{O(r)}
$$

Relaxed factor has the stated rank-quasipolynomial bound.

**Model and scope.** Explicit items and liking incidences.

#### [One-value allocation](problems/one-value-exact-two/)

Exact factor two with setup and assignment budget.

**Randomness.** Deterministic corank branching and exact-budget recovery; the whole-ground alternative uses deterministic inclusion covers.

**Quantitative result.**

$(27/4)^c$ or $(50/27)^qE(q)$.

**Model and scope.** All fixed integer quota factors are included.

#### [Intrinsic two-value allocation](problems/two-value-exact-two/)

Exact factor two for compulsory players.

**Randomness.** Deterministic in the exact-two and whole-ground variants, with paid exact completion, rank, LP and decomposition primitives.

**Quantitative result.**

$(27/4)^{h_C}$ or $(50/27)^qE(q)$.

**Model and scope.** Exact assignment budget; intrinsic values shared by recipients.

#### [Intrinsic values near factor two](problems/intrinsic-values-near-two/)

Factor $2+\eta$.

**Randomness.** Deterministic split enumeration, omission branching and integral recovery, including optional-player, exact-two and constructive local-search fallback variants.

**Quantitative result.**

Near-two: $\Gamma(1/\epsilon)^k$, $\epsilon=\eta/(2+\eta)$.

Exact-two: XP $(q+1)^k$ or separated-light $\Gamma(1/\sigma)^k$.

**Model and scope.** Actual compulsory/optional bases; near-two and exact-two use their distinct threshold-derived coranks. Exact-two is polynomial at corank zero; the $\sigma$ branch requires a quantified light-value gap. No cost budget.

#### [Unrelated-value additive allocation](problems/unrelated-values-additive/)

At player $p$: $\max\{0,(1-\epsilon)\mathrm{FOPT}-u_p\}$.

**Randomness.** Deterministic selection, rational optimization and additive-loss rounding with paid exact primitives; whole-ground selection uses deterministic covers.

**Quantitative result.**

$$
\Gamma(1/\epsilon)^c
$$

Whole-ground alternative $(2-1/\Gamma(1/\epsilon))^qE(q)$.

**Model and scope.** An actual permitted set with fractional assignments as comparator; exact assignment budget; whole-ground alternative for fixed accuracy.

#### [Unrelated values with a joint role](problems/unrelated-values-joint-role/)

Factor $2+\eta$ with setup; exact two in $2^q$; player-specific two-value J2 endpoint.

**Randomness.** Deterministic in the near-two, exhaustive exact-two, compulsory J2 and whole-ground variants, with paid exact optimization and rounding primitives.

**Quantitative result.**

$$
(2-1/\Gamma(R))^qE(q)
$$

J2 $(27/4)^{\nu_C}$ or $(50/27)^qE(q)$.

**Model and scope.** Near-two uses fixed $R=(2+\eta)/\eta$ and permits an actual optional basis; J2 requires compulsory players with pair values $\{0,u,a\}$.

#### [Whole-ground selection and transfers](problems/whole-ground-allocation/)

Converts forced-omission extensions without changing comparator or exact constraints.

**Randomness.** Deterministic streamed inclusion covers and fixed-order enumeration. Bernoulli measures in the analysis count branches; the procedure draws no random bits.

**Quantitative result.**

$$
A^c\longmapsto(2-1/A)^qE(q)
$$

**Model and scope.** Fixed A>1, all-input forced-seed extension and polynomial space; weighted/adaptive selection and rational optimization retained.

### Selected flow and robust allocation

Time entries suppress polynomial encoded-input work. Whole-ground alternatives use fixed accuracy/tradeoff parameters. Scenario lists are explicit; one permitted selected set is shared, while scenario routings or assignments may adapt.

#### [Selected concurrent flow](problems/selected-flow/)

$(1-\epsilon)$ of optimum common splittable rate.

**Randomness.** Deterministic branching and exact rational flow-LP optimization, conditional on the paid exact restriction selector; both time alternatives are deterministic.

**Quantitative result.**

$\Gamma(1/\epsilon)^c$ or $(2-1/\Gamma(1/\epsilon))^qE(q)$.

**Model and scope.** Paid exact restriction selector; permitted commodity set and exact routing constraints; whole-ground alternative for fixed accuracy.

#### [Flow with shared setup budget](problems/shared-setup-flow/)

$(1-\epsilon)$ of optimum common rate.

**Randomness.** Deterministic, conditional on the paid exact minimum-setup restriction optimizer and exact rational flow-LP primitives.

**Quantitative result.**

$\Gamma(1/\epsilon)^c$ with the whole-ground alternative.

**Model and scope.** Paid minimum-setup restriction optimizer; one combined setup/routing budget; routing-only budgets exact.

#### [Robust selected flow](problems/robust-scenario-flow/)

One commodity set attains $(1-\epsilon)\mathrm{OPT}$ in every scenario.

**Randomness.** Deterministic for the explicit scenario list, with a paid exact selector. Scenario-dependent routing is recourse after selection, rather than randomized or adversarial input.

**Quantitative result.**

$\Gamma(1/\epsilon)^c$ with the whole-ground alternative.

**Model and scope.** Paid exact restriction selector; separate exact scenario budgets and adaptive splittable routings.

#### [Robust unrelated allocation](problems/robust-unrelated-allocation/)

At $(\omega,p)$: $\max\{0,(1-\epsilon)\mathrm{FOPT}-u_{\omega,p}\}$.

**Randomness.** Deterministic common-basis selection and exact-budget rounding in each listed scenario; whole-ground selection also uses deterministic covers.

**Quantitative result.**

$\Gamma(1/\epsilon)^c$ with the whole-ground alternative.

**Model and scope.** One actual basis; exact per-scenario setup/assignment budgets.

#### [Robust bounded-width certificates](problems/robust-bounded-certificates/)

Fixed integer factor $d\ge2$ under failure width $w$.

**Randomness.** Deterministic width-guarded branching and exact unit tests. A width-violation certificate reports a failed promise, rather than a probabilistic failure.

**Quantitative result.**

$A^c$ or $(2-1/A)^qE(q)$, $A=\max\{w,\Gamma((d+1)/(d-1))\}$.

**Model and scope.** Width is a stated promise, not automatic.

#### [Width-two robust unit allocation](problems/robust-width-two-allocation/)

Exact common-basis unit feasibility.

**Randomness.** Deterministic conflict enumeration, graph-cover branching and exact matroid intersection; the whole-ground alternative uses deterministic covers.

**Quantitative result.**

$\varphi^c$ or $((5-\sqrt5)/2)^qE(q)$.

**Model and scope.** $\varphi=(1+\sqrt5)/2$; width two bounds minimal aggregate budget-feasible one-unit failures.

#### [Two-scenario hardness](problems/robust-two-scenario-hardness/)

W[1]-hard exact positive service in corank $c$.

**Randomness.** Deterministic parameter-preserving reduction from bounded-integer k-SUM. The stated hardness consequence concerns deterministic algorithms; no randomized reduction is needed.

**Quantitative result.**

Parameter-preserving reduction with $c=k$.

**Model and scope.** Two explicit scenarios; Boolean recipient ranks are free, while nonnegative assignment costs and both exact budgets remain.

### Scheduling

Time entries suppress polynomial encoded-input work. Every positive approximation returns a complete integer schedule. Each card specifies whether a cost budget is present; all stated budgets and original job totals are retained.

#### [Arbitrary-processing scheme](problems/arbitrary-processing-scheduling/)

Factor $1+\epsilon$.

**Randomness.** Deterministic profile enumeration and exact integral recovery, including the compressed-slot-surplus branch, with paid deterministic primitives.

**Quantitative result.**

$$
\Pi_\epsilon^q=2^{O(q/\epsilon)}
$$

**Model and scope.** Exact assignment budget for the scheme. Separate common-type/no-budget branch: $\min\{\mathrm{OPT}+a,(1+\epsilon)\mathrm{OPT}+u\}$ in $\Gamma(1/\epsilon)^k$ when $c_{\mathrm{slot}}(\mathrm{OPT})\le k$, $0<\epsilon\le1/2$.

#### [Activated-machine scheduling](problems/activated-machine-scheduling/)

Factors $1+\epsilon$, $3/2$, and the bucket curve.

**Randomness.** Deterministic enumeration of activation bases and profiles, followed by exact feasibility and recovery tests.

**Quantitative result.**

$$
\binom qr\Pi_\epsilon^r
$$

$$
\binom qr6^r
$$

$$
\binom qr(k+1)^r
$$

**Model and scope.** Actual rank-$r$ activation bases.

#### [Six-profile scheduling](problems/six-profile-three-halves/)

Exact factor $3/2$.

**Randomness.** Deterministic enumeration of six profiles per machine and exact cost-preserving integral recovery.

**Quantitative result.**

$$
6^q
$$

**Model and scope.** Unrelated processing times; six profiles per machine.

#### [Processing-bucket tradeoff](problems/processing-bucket-tradeoff/)

$\gamma_k=(3\cdot2^k-1)/(2^{k+1}-1)$.

**Randomness.** Deterministic bucket enumeration and exact minimum-cost recovery, for every stated integer bucket depth.

**Quantitative result.**

$$
(k+1)^q\mathrm{poly}(H+k)
$$

**Model and scope.** Approaches $3/2$ with increasing bucket depth.

#### [Two-size scheduling](problems/two-size-scheduling/)

Exact $3/2$; separate $5/3$ small-large-count regime.

**Randomness.** Deterministic rank tests, omission branching and job reconstruction; the independent large-count branch and whole-ground alternative are also deterministic.

**Quantitative result.**

$(27/4)^c$ or $(50/27)^qE(q)$.

Separate $2^{O(h)}$ branch.

**Model and scope.** $c=q-h$ is surplus large positions; h is mandatory large-unit count; common type sizes and no assignment-cost budget.

#### [Per-machine two-time scheduling](problems/two-time-scheduling/)

Factor $2-1/d$ for fixed integer $d\ge2$.

**Randomness.** Deterministic quota search and original-total recovery, including the fixed-factor endpoints and deterministic whole-ground conversion.

**Quantitative result.**

$$
(2-1/\Gamma((d+1)/(d-1)))^qE(q)
$$

**Model and scope.** At most two positive times per machine; zero-time handling is explicit.

#### [Many-size workload scheduling](problems/many-size-scheduling/)

$\min\{2\mathrm{OPT},(2-1/(3+\eta))\mathrm{OPT}+u\}$.

**Randomness.** Deterministic workload aggregation, rank-based unit search, decomposition and additive rounding in both approximation variants.

**Quantitative result.**

$$
\min\{2^{O(h)},(h+1)^{O((1+\eta^{-1})\log(h+1))}\}
$$

**Model and scope.** $0<\eta\le1$; h counts mandatory largest-size units; common type sizes and no assignment-cost budget.

#### [Commitment scheduling](problems/commitment-scheduling/)

Bottleneck/additive guarantee; two-size $3/2$ or $5/3$ endpoints.

**Randomness.** Deterministic greedy commitment selection, residual unit search, exact decomposition and additive rounding.

**Quantitative result.**

$2^{O(k)}$ with a rank-quasipolynomial relaxed alternative.

**Model and scope.** Common type sizes without an assignment-cost budget; full-machine contraction permits more large units than machines, and eligibility-width/collision refinements have their own certificates.

### Matching certificates and oracle barriers

These records separate constructive certificates, promise conditions, and lower-bound models.

#### [Hypergraph matching and expander routing](problems/strong-haxell-matching/)

Left-perfect matching or an explicit deficient hitting-set certificate.

**Randomness.** Deterministic certifying hypergraph matching. The routing and expander-packing transfers additionally require the supplied deterministic destructive-support distance interface.

**Quantitative result.**

$$
O(\lvert A\rvert+\lvert B\rvert)+p\exp(O(U\log(2+s)/s))
$$

**Model and scope.** $\Delta\ge4$, right-resource rank r, $U=\log(p+4)$ and $s=\log\Delta$; also certified disjoint paths and density-conditioned spanning expander packing.

#### [Independent transversals](problems/independent-transversal/)

Independent transversal or a dominating-set/constellation certificate.

**Randomness.** Deterministic certifying construction, including the elementary exponential fallback; arbitrary choices use fixed tie rules.

**Quantitative result.**

$$
P\min\{e^{O(q)},(q+1)^{O(\epsilon^{-1}\log(2+r/\epsilon))}\}
$$

**Model and scope.** Explicit graph/partition; no vertex has r independent neighbours in distinct classes; full bit and rational-accuracy factors remain on the card.

#### [Allocation and scheduling barriers](problems/allocation-lower-bounds/)

Below-two allocation and below-$3/2$ scheduling oracle barriers.

**Randomness.** Lower bounds for deterministic rank-query algorithms, together with explicit integrality-gap constructions. These query statements do not claim the same bound for randomized algorithms.

**Quantitative result.**

$\binom qr-1$ deterministic recipient-rank queries.

**Model and scope.** Also aggregate configuration gap approaching $r$, residual gap two, and a zero refined-parameter family.

## Supporting results

These additional algorithms, structural lemmas and scoped boundaries have their own complete manuscripts. Further refinements are listed with their parent result in the [proof index](CONTENTS.md).

### [Grouped choices under resource deletions](manuscripts/graph-backends/decremental-choice-recourse-lemma.md)

One live representative per group with bounded prefix recourse.

**Randomness.** Deterministic representative-maintenance rule, valid against an adaptive deletion order; the recourse bound does not assert near-linear total augmenting-path search time.

**Quantitative result.**

$O((M\log R+Q)\log(M+2))$ representative changes.

**Model and scope.** M groups, R resources and Q adaptive deletions; augmenting-path discovery work is separate.

### [Nonuniform sparse route rounding](manuscripts/graph-backends/nonuniform-fractional-path-selection.md)

Choose one supplied candidate per group while controlling every resource load.

**Randomness.** Deterministic sparse rounding by conditional averaging and guarded finite arithmetic. Candidate probabilities are mathematical weights; the implementation does not sample choices.

**Quantitative result.**

Load:

$$
\le2\mu_x+B\log(8(\lvert X\rvert+1))
$$

$S\mathrm{poly}(\log S,b)$ bit work.

**Model and scope.** Explicit sparse occurrences, rational masses and weights; B bounds one weighted occurrence contribution.

### [Short path inventories from a shared DAG](manuscripts/graph-backends/compressed-fractional-path-extraction.md)

Retain at least half of the unit commodities on short candidate routes.

**Randomness.** Deterministic extraction from a supplied exact shared DAG and rational flow records. The upstream flow-oracle construction and its randomness are outside this lemma.

**Quantitative result.**

$O(Z+P)$ arithmetic operations.

Route length $\le4H$ and fractional load at most doubled.

**Model and scope.** Supplied DAG and rational masses with total weighted length at most MH; explicit expansion is output-charged.

### [Bounded-width lazy path client](manuscripts/graph-backends/bounded-interface-witness-pattern-updates.md)

Complete static numerical client with implicit physical-path updates.

**Randomness.** Deterministic finite-interface numerical client with a supplied edge-partition/separator hierarchy; hierarchy-construction work is additional.

**Quantitative result.**

Time:

$$
(m+\nu)\exp(O(b^2))h\mathrm{polylog}S
$$

Space $(m+\nu)\exp(O(b^2))$.

**Model and scope.** Supplied fixed edge-partition hierarchy of height h and boundary b; decomposition-input work is additional.

### [Forest-support numerical client](manuscripts/graph-backends/complete-unrestricted-forest-one-sided-client.md)

Complete threshold search with unrestricted receiving directions.

**Randomness.** Deterministic numerical client under the stated ambient-support forest and finite-word contracts, using exact directed tree dynamic programming and lazy path updates.

**Quantitative result.**

$(m+\nu)\mathrm{polylog}S$ total fixed-ledger work.

**Model and scope.** The entire ambient allocation support is a forest, with the stated polynomial-range guards.

### [Feedback-edge numerical client](manuscripts/graph-backends/feedback-edge-one-sided-client.md)

Complete threshold search with k nonforest incidences.

**Randomness.** Deterministic numerical client under the stated feedback-edge and finite-word contracts, using exact forest queries and a small Dijkstra computation.

**Quantitative result.**

$(m+\nu(k+1))\mathrm{polylog}S$ total work.

$(k+1)\mathrm{polylog}S$ per query/update plus events.

**Model and scope.** Fixed polynomial-range ledger; parameterized support theorem does not improve arbitrary-graph matching time.

### [Weak-Haxell certifying matching](manuscripts/matching-and-routing/weak-haxell-current-blocker-growth.md)

Left-perfect matching or an explicit violated hitting-set condition.

**Randomness.** Deterministic certifying augmenting search on the explicit hypergraph; it returns a matching or the stated hitting-set certificate.

**Quantitative result.**

$$
P(n+1)^{O((r/\epsilon)\log(2+r/\epsilon))}\mathrm{poly}(b_\epsilon+\log P)
$$

**Model and scope.** Whole-edge rank $r\ge2$, $0<\epsilon<1$; matching under $\tau(E_S)>(2r-3+\epsilon)(\lvert S\rvert-1)$.

### [Sparse-separator corank refinement](manuscripts/allocation-and-scheduling/attained-set-sparse-separator-gap.md)

Smaller extension and whole-ground bases when the returned separator is sparse.

**Randomness.** Deterministic certificate enumeration, relative to the paid exact separator, selection and recovery interfaces. Bernoulli probabilities are used only to count branches.

**Quantitative result.**

$$
\beta(R,w)^c
$$

$\beta(2,3)=(1+\sqrt5)/2$, $\beta(3,4)=1+\sqrt2$.

**Model and scope.** Actual separator width w; matching global bases $(5-\sqrt5)/2$ and $3-\sqrt2$ use the forced-omission wrapper.

### [Whole-ground robust allocation barrier](manuscripts/allocation-and-scheduling/robust-unit-allocation-whole-ground-oracle-barrier.md)

Every finite multiplicative guarantee requires near-exhaustive rank queries.

**Randomness.** Lower bounds: the self-contained q-scenario oracle proof concerns deterministic algorithms; the attributed two-scenario consequence also excludes bounded-error randomized algorithms.

**Quantitative result.**

At least $q^{-1}\binom qr-1$ deterministic queries.

$2^{q-O(\log q)}$ for balanced rank.

**Model and scope.** $2\le r<q$; q explicit scenarios, uniform player matroid and zero costs; separate attributed two-scenario implication.

### [Implicit minimal-bundle transversals](manuscripts/matching-and-routing/implicit-minimal-bundle-transversal-oracle.md)

Disjoint minimal bundles or an explicit domination/constellation certificate.

**Randomness.** Deterministic implicit construction using fixed-order resource scans and the stated exact bundle operations.

**Quantitative result.**

$$
P(q+1)^{O(\epsilon^{-1}\log(2+q/\epsilon))}\mathrm{poly}(b+b_\epsilon+\log P)
$$

**Model and scope.** No configuration enumeration or arbitrary-neighbour oracle; certificate class sets retain their distinct meanings.

### [Global free pool at the critical quota](manuscripts/allocation-and-scheduling/critical-unit-quota-global-free-pool.md)

Globally resource-free owners cover the current player-rank deficit.

**Randomness.** Structural rank lemma and deterministic paid search acceleration with exact availability. No improved global running-time bound is asserted.

**Quantitative result.**

$r_M(F)\ge r-k$ when the full quota is $t=3b-2$ and each current record has b units.

**Model and scope.** Fully normalized prefix invariant; eligible free owners admit a paid exchange; no faster critical-quota runtime follows.

### [Jointly independent layer owners](manuscripts/allocation-and-scheduling/joint-owner-sharp-quality-addendum.md)

Within-layer joint independence retains the sharp availability-dependent quality.

**Randomness.** Structural guarantee for deterministic current-blocker search, conditional on an availability oracle satisfying its certified factor on every call.

**Quantitative result.**

Factor $\lambda^{-1}+3-3/r+\eta$ with the original rank-exponential or relaxed rank-quasipolynomial time.

**Model and scope.** The stated current-blocker and paid availability model; joint independence alone does not supply a polynomial batching theorem.

### [Explicit laminar reservation interface](manuscripts/allocation-and-scheduling/laminar-resource-current-blocker-reservations.md)

Token reservations and antichain compact certificates for recipient constraints.

**Randomness.** Deterministic explicit-token reservations and fixed-order current-blocker search for the supplied laminar matroids.

**Quantitative result.**

No laminar-depth factor in the resource value certificate.

**Model and scope.** Includes the stated local-family interfaces; its older base-model approximation is subsumed by the main recipient-polymatroid theorem.

### [Persistent path-hitting certificates](manuscripts/graph-backends/fixed-hitting-certificates-under-graph-updates.md)

One shared update set preserves all historical path-hitting certificates.

**Randomness.** Deterministic structural certificate transfer from supplied historical hitting sets; it does not establish a complete fully dynamic matching or disjoint-path algorithm.

**Quantitative result.**

$C\cup I$ hits current short paths.

Size at most $\lvert C\rvert+\lvert I\rvert$.

**Model and scope.** Deletions and length increases are safe; inserted/decreased edge lifetimes enter I; selected-path and layer repair are separate.

### [Fixed-potential tight-DAG repairs](manuscripts/graph-backends/fixed-potential-tight-dag-repair-lemma.md)

Maintain old-label shortest-path forests on tight-reachable vertices.

**Randomness.** Deterministic reachability and parent-repair algorithm within one supplied fixed-potential interval; no global bound across potential refreshes is established.

**Quantitative result.**

$O(m+\nu)$ total graph work and supplied forest edits per fixed-potential interval.

**Model and scope.** No ledger births or label changes inside the interval; potential-refresh work is outside the bound.

### [Slack-only directed matching reduction](manuscripts/graph-backends/slack-only-one-sided-matching-client.md)

Constant-ratio comparison and a finite-word static threshold oracle.

**Randomness.** Deterministic mathematical reduction and exact static threshold oracle. The required fast dynamic interface has not been constructed, so no complete faster dynamic algorithm is classified.

**Quantitative result.**

Directed nonnegative SSSP reduction with monotone prices and a charged repricing budget.

**Model and scope.** The dynamic path-reporting/update provider remains a separate unproved interface; no improved general-matching exponent.

### [Residual-capacity configuration comparator](manuscripts/allocation-and-scheduling/recipient-polymatroid-residual-configuration-relaxation.md)

Integral allocation with factor $4-3/r$ against the strengthened residual-capacity configuration LP.

**Randomness.** Deterministic current-blocker allocation relative to the stronger LP. A supplied factor-lambda availability oracle must meet its certified guarantee on every call.

**Quantitative result.**

$$
2^{O(r)}\mathrm{poly}(H)
$$

The stated rank-quasipolynomial alternative allows additive accuracy in the factor.

**Model and scope.** Arbitrary binary recipient polymatroids and exact local availability; certified factor-$\lambda$ availability changes the ratio to $\lambda^{-1}+3-3/r$. The algorithm does not solve the LP.

### [Fractional optimization of residual configuration relaxations](manuscripts/allocation-and-scheduling/residual-configuration-bounded-support-xp-solver.md)

A feasible fractional configuration point at target at least $(1-\epsilon)\mathrm{OPT}_{\mathrm{LP}}$.

**Randomness.** Deterministic rational ellipsoid optimization, exact-budget profit-scaling dynamic programming and finite primal LP extraction.

**Quantitative result.**

Full LP:

$$
2^{O(q)}\mathrm{poly}(H,\epsilon^{-1})
$$

Support-s cuts:

$$
(q+1)^{O(s+1)}\mathrm{poly}(H,\epsilon^{-1})
$$

**Model and scope.** Coordinate-box local families and binary capacities; $s=2(r-1)$ gives an XP rank bound. This is optimization of the stated fractional comparator, with separate integer rounding.

## Reading and verification

Start with a result card, then read its `proof.md`. Longer derivations are linked as companion manuscripts. Shared graph interfaces, allocation lemmas, and explicit obstruction constructions are indexed in [Contents](CONTENTS.md#shared-manuscripts). The source map names the dependencies used by that result.

Each `verify/README.md` explains the available evidence and its limits. Exact finite certificates check specified identities, finite examples, or certified domains; they do not by themselves establish every asymptotic theorem. The repository does not claim proof-assistant verification or external peer review.

The [maintenance guide](CONTRIBUTING.md) gives the single local check command and the rules for updating statements, proof dependencies, and this generated catalogue.

## Citation and attribution

Yilin Liu and GPT-6 Astra Pro. *Algorithm Frontier* (2026). Cite the relevant problem path and commit; the [citation protocol](PROTOCOL.md) and [import provenance](provenance/README.md) retain the applicable licenses and notices.
