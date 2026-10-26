# Algorithm Frontier

Research manuscripts on deterministic algorithms, combinatorial optimization, dynamic graphs, and sparsification. The catalogue below lists every result family; each entry opens a precise statement, complete proofs, and its computational assumptions.

[![Repository checks](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml/badge.svg)](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml) [![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

**53 result families · 18 supporting results** · [Complete proof index](CONTENTS.md) · [Complexity conventions](docs/COMPLEXITY.md) · [Verification evidence](reviews/README.md) · [Citation](CITATION.cff)

## Results

[Subset Sum](#subset-sum) · [Numeric targets and quota geometry](#numeric-targets-and-quota-geometry) · [Graph algorithms](#graph-algorithms) · [Exact failures, persistence and compilation](#exact-failures-persistence-and-compilation) · [Spectral, group and quantum sparsification](#spectral-group-and-quantum-sparsification) · [Allocation and resource matroids](#allocation-and-resource-matroids) · [Selected flow and robust allocation](#selected-flow-and-robust-allocation) · [Scheduling](#scheduling) · [Matching certificates and oracle barriers](#matching-certificates-and-oracle-barriers) · [Supporting results](#supporting-results)

A displayed conditional composition includes its named backend hypotheses. Oracle bounds, explicit-input algorithms, support sizes, query costs, and existence theorems keep their distinct meanings. Exact rational constants and complete parameter ranges are stated on the linked cards.

### Subset Sum

Time counts deterministic bit operations; $L$ is the complete input length. The two rows are separate algorithms.

| Problem | Output or guarantee | Quantitative result | Model and scope |
|---|---|---|---|
| [Faster deterministic Subset Sum](problems/subset-sum-fast-deterministic/) | Exact decision and indexed witness | $C+\operatorname{poly}(n,L)2^{0.495891928n}$; exact rational exponent on the card | Exact rational certification of all 44 continuous contact branches; C is finite input-independent circuit precomputation; combinatorial compiler and bit-cost proofs are in the manuscript |
| [Low-space deterministic Subset Sum](problems/subset-sum-low-space-deterministic/) | Exact decision and indexed witness | Time $\operatorname{poly}(n,L)2^{n/2}$; writable bits $\operatorname{poly}(n,L)2^{0.18261635770550353n}$ | Also half-exponential time and $O^*(2^{n/6})$ space for the stated two-short-range input class |

### Numeric targets and quota geometry

Every bound includes polynomial work in the full encoded input. Binary resource counts remain compressed, and mandatory bases retain their original total.

| Problem | Output or guarantee | Quantitative result | Model and scope |
|---|---|---|---|
| [Numeric targets and support patterns](problems/numeric-target-frontier/) | Exact mixed targets and signed-scalar optimization | $2^{O(T\log(2+\min\{Q/T,T\}))}$; fixed dimension $\exp(O_d((T+1)^{d/(d+1)}))$; one-target decision $2^{O(\sqrt{T+1})}$ | $T,Q>0$ in the first formula; zero cases are polynomial. Also unequal targets, overlap/components, stars, seven accuracy schemes and aligned nonlinear transfers |
| [Prefix, laminar and sparse quotas](problems/weighted-prefix-quota-frontier/) | Exact quota algorithms and deterministic original-ground kernels | One order $2^{O(B)}$; two orders $2^{O(B\log(B+2))}$; $p$ weight families $2^{O(pB\log(p+2))}$; laminar $2^{O(B^2)}$ | Also support/family tradeoffs, sparse quotas, coverable/transversal kernels, and edge-matroid matching kernels |

### Graph algorithms

Use each result’s declared graph cap N, with $U=\log(N+4)$, $h=\log(U+4)$ and $\mathcal E_a=\exp(O(U^ah^{1-a}))$. The flow row instead displays its numerical cap S explicitly. Conditional compositions retain their named hierarchy, raw-cycle and lifetime interfaces; the MSF row is a derived public baseline.

| Problem | Output or guarantee | Quantitative result | Model and scope |
|---|---|---|---|
| [Maximum-cardinality matching](problems/general-matching/) | Exact matching with original edge identifiers | $O(n+m)+(m_s+1)\mathcal E_{4/5}$; optional $m_H=O(\nu(G)^2)$ kernel | Conditional on raw-backend Contract R and the named external primitives |
| [Degree-constrained subgraphs](problems/degree-constrained-subgraphs/) | Exact factors, interval degrees and cardinality optimization | $O(n+m)+(m+1)\mathcal E_{4/5}$ | Loopless multigraph; capacity one per explicit edge record; conditional matching backend |
| [Static and threshold min-cost flow](problems/min-cost-flow/) | Exact integral optimum or threshold witness | $O((N+1)E(S)^4\operatorname{polylog}S)$, $E(S)=\exp(O((\log S)^{4/5}(\log\log(S+4))^{1/5}))$ | Conditional raw-cycle lifetime and initialization interfaces; numerical cap S; full-flow output charged separately |
| [Incremental strongly connected components](problems/incremental-scc/) | Exact component labels | Total $(n+m)\mathcal E_{4/5}^{O(1)}\operatorname{poly}(U)$ | Conditional raw-cycle/retirement interface; total insertion work; component labels only |
| [Incremental directed SSSP](problems/incremental-sssp/) | $(1+\epsilon)$ distances and simple paths | Total $(n+m)\exp(O(U^{4/5}h^{1/5}+\sqrt{U(h+\log(1/\epsilon))}))$ | Conditional detector/retirement interface; positive polynomial-range lengths; $0<\epsilon\le1/2$, $\log(1/\epsilon)=O(U)$; $k$-edge output costs $(k+1)\operatorname{poly}(U)$ |
| [Fully dynamic APSP](problems/apsp-frontier/) | A family of update/stretch tradeoffs | Amortized factor $\exp(O(U/t+t^3h))$; stretch $\exp(O(t^4h))$; query $\operatorname{poly}(U)$ | Conditional metric hierarchy; $t\to\infty$, $t^2h=o(U)$; positive polynomial-range lengths; five explicit parameter points |
| [Dynamic spanners](problems/dynamic-spanners/) | Two distinct stretch/recourse regimes | Tracked terminals $\mathcal E_{4/5}$; full-horizon $\mathcal E_{5/6}$ with recourse $(n+D)\mathcal E_{5/6}$ | Conditional hierarchy interfaces; unweighted graph; amortized work includes initial inventory, insertions and deletions |
| [Dynamic minimum spanning forest](problems/dynamic-msf/) | Exact fully dynamic MSF | Worst-case update $\mathcal E_{2/3}$ | Derived public baseline using the stated decomposition and pruning results |
| [Strong forests and Gomory–Hu trees](problems/decremental-strong-forest/) | Decremental strong forest; exact cut-equivalent tree | $O(n+m)+(m+1)\mathcal E_{6/7}$ | Conditional forest/flow interfaces; bounded-degree native forest; arbitrary-degree cut-tree transfer with positive polynomial-range integer capacities |

### Exact failures, persistence and compilation

Support bounds count retained original objects. They are shown separately from preprocessing and query costs. Let $h$ be the failure budget and $d$ the maximum labels per item where applicable.

| Problem | Output or guarantee | Quantitative result | Model and scope |
|---|---|---|---|
| [Single-failure optimum preservers](problems/exact-failure-preservers/) | Weighted and valuated two-matroid intersection; rooted arborescences | Matroids: $O(k^{3/2})$ support/records, $O(k)$ reporting; arborescences: $O(n^{3/2})$, $O(n)$ | Deterministic polynomial preprocessing; arborescences $\widetilde O(mn)$ arithmetic work; effective-domain initialization for valuations |
| [Flow, matching and price sensitivity](problems/exact-flow-sensitivity/) | Unit-flow/path failures, general matching, two matroids and one-element prices | Flow $O(n^{3/2}\lambda^{1/4})$; matching $4\mu+2$ edges, or $6\mu+2$ for edge/vertex failure; matroids $2r+k\le3r$; prices $O(N+r\sqrt{\min\{N,r^2\}})$ | Flow exponent: simple unit-capacity digraph and nonnegative costs. Matching/matroid failures preserve cardinality; each reporting bound is model-specific |
| [Matroid and submodular failure summaries](problems/matroid-failure-summaries/) | Represented fixed-cost prefixes; oracle rank and integer-submodular value preservation | Rank: $r\binom{h+d}{d}$; integral submodular range $R$: $R\binom{h+d}{d}$; sharp marginal/entropy inequality | Support capped by original ground size; uniform polynomial represented construction; parameterized oracle construction; rank-only oracle model has no weighted-prefix claim |
| [Colored and vertex-failure graph certificates](problems/graph-color-failure-certificates/) | Exact surviving connectivity and canonical MSF | $\sum_C(n_Ck_C-\binom{k_C+1}{2})$, $k_C=\min\{h+1,q_C\}$ | Displayed bound: one color per vertex and a fixed weight order; overlapping vertex lists and additional edge labels have separate bounds |
| [Resource-constrained packing summaries](problems/packing-matching-summaries/) | Weighted universal completion after deletions and forbidden vertices | $\min\{N,r\binom{pK+h_v}{p}\prod_j\binom{h_j+d_j}{d_j}\}$ | Explicit packing sets and represented resource; omit r when absent; full-input gate precedes lift expansion |
| [Persistent-homology failure certificates](problems/persistence-failure-certificates/) | All surviving boundary spaces and lower-degree persistence modules | $\min\{N,r\binom{h+a+b}{a+b}\}$ retained top simplices | One fixed filtration over the stated field; full lower skeleton retained; homology degrees at most $p-1$ |
| [Boolean linear optimization compiler](problems/boolean-linear-compiler/) | Signed equalities, intervals, witnesses and lexicographic optimization | $\operatorname{poly}(L)(\prod_i p_i)2^{\alpha n+Q-(1-\alpha)B}$ | Supplied indexed-witness Subset Sum backend of exponent $\alpha$; $0\le B\le Q$; a space bound requires that same backend |

### Spectral, group and quantum sparsification

Support counts retained original items and is capped by input size. Construction models remain separate from existence. For correlated failures, $\Gamma(h,d)=(h+d)^{h+d}/(h^hd^d)$, with $\Gamma=1$ when hd=0; Q counts allowed label sets, K is feature dimension, and $\rho$ is effective dimension.

| Problem | Output or guarantee | Quantitative result | Model and scope |
|---|---|---|---|
| [Correlated spectral, regression and seminorm summaries](problems/correlated-spectral-regression/) | PSD forms, norms, weak convex losses, graded incidence and simplicial spectra | PSD: $O(\Gamma r\epsilon^{-2}\log(2rQ/\delta))$; weak regression: $O(\Gamma\rho\epsilon^{-1}\log(2(p+q)Q/\delta))$; seminorm existence: $O(rK/\epsilon^2)$ | Capped original-item support; one event covers all failures; regression penalties are nonnegative convex; constructive seminorm bounds require the lifted backend |
| [Label and whole-block cut sparsification](problems/label-block-cut/) | Exact incidence decoders, hyperedges, whole blocks and adaptive quotient resparsification | $O(\min\{m,R\log(2R/\epsilon)/\epsilon^2\})$, with $R=r\binom{h+k}{k}$ for incidence label deficit k | Compact randomized whole-item construction; full-input gate; graph deficit a+b, hyperedge and commuting-block variants keep their distinct ranks |
| [Finite groups, affine constraints and metrics](problems/group-metric-constraints/) | Cayley generators, subgroups/cosets, modular blocks and Hilbert metric sums | Cayley $O(\epsilon^{-2}\log^3(2\lvert G\rvert))$; subgroups $O(\epsilon^{-2}\log(2[G:\cap_eH_e]))$; cosets $O(\epsilon^{-2}\log(2\lvert G\rvert))$; transitive metrics $O(\epsilon^{-2}\log(2N))$ | Cayley construction uses explicit matrices; subgroup/coset/metric constructions use explicit query tables; compact modular construction has its separate logarithmic overhead |
| [Pauli, qudit and stabilizer blocks](problems/quantum-stabilizer/) | Whole-check sparsification and commuting energy witnesses | $R=\log_2(2D)$: support existence $O(\min\{m,R/\epsilon^2\})$; compact randomized $O(\min\{m,R\log(2R/\epsilon)/\epsilon^2\})$ | Whole internally commuting blocks; arbitrary cross-block noncommutation. Sharper prime-dimensional rows and separate $2+\sqrt2$ witness approximation are on the card; witness optimization is exponential |
| [Exact-separation and non-Fano boundaries](problems/obstruction-boundaries/) | Compact relative-error-body membership and a precise fixed-amplitude matroid obstruction | coNP-complete membership; non-Fano sign probability $15/128<1/8$ | Exact separation would decide the membership problem; the sign obstruction does not refute general sparsification |

### Allocation and resource matroids

Time entries suppress $\operatorname{poly}(H)$, or $\operatorname{poly}(H_\epsilon)$ for accuracy. Let $q$ be the candidate count, $r$ the selected rank, $c=q-r$, $\Gamma(R)=R^R/(R-1)^{R-1}$, and $E(q)=2^{O(q\log\log(q+2)/\log(q+2))}$.

| Problem | Output or guarantee | Quantitative result | Model and scope |
|---|---|---|---|
| [Arbitrary-value allocation scheme](problems/arbitrary-value-allocation-scheme/) | $(1-\epsilon)\mathrm{OPT}$ with exact setup and assignment budget | $\binom qr\exp(O(r/\epsilon))$ | Actual selected player basis; integer comparator |
| [Recipient polymatroids](problems/recipient-polymatroid/) | Factor $4-3/r$; approximate availability and equal-unit extensions | $2^{O(r)}$; relaxed factor has a rank-quasipolynomial alternative | Integer comparator; binary repeated resources |
| [Recipient-matroid configuration](problems/recipient-matroid-configuration/) | Factor $4-3/r$ against the configuration LP | $2^{O(r)}$; factor $\lambda^{-1}+3-3/r$ with a certified local $\lambda$ oracle | The configuration comparator is explicit |
| [Explicit-item matroid union](problems/item-matroid-union/) | Factor $4-3/r$ against the configuration LP | $2^{O(r)}$; relaxed factor has the stated rank-quasipolynomial bound | Explicit items and liking incidences |
| [One-value allocation](problems/one-value-exact-two/) | Exact factor two with setup and assignment budget | $(27/4)^c$ or $(50/27)^qE(q)$ | All fixed integer quota factors are included |
| [Intrinsic two-value allocation](problems/two-value-exact-two/) | Exact factor two for compulsory players | $(27/4)^{h_C}$ or $(50/27)^qE(q)$ | Exact assignment budget; intrinsic values shared by recipients |
| [Intrinsic values near factor two](problems/intrinsic-values-near-two/) | Factor $2+\eta$ | Near-two: $\Gamma(1/\epsilon)^k$, $\epsilon=\eta/(2+\eta)$; exact-two: XP $(q+1)^k$ or separated-light $\Gamma(1/\sigma)^k$ | Actual compulsory/optional bases; near-two and exact-two use their distinct threshold-derived coranks. Exact-two is polynomial at corank zero; the $\sigma$ branch requires a quantified light-value gap. No cost budget |
| [Unrelated-value additive allocation](problems/unrelated-values-additive/) | At player $p$: $\max\{0,(1-\epsilon)\mathrm{FOPT}-u_p\}$ | $\Gamma(1/\epsilon)^c$; whole-ground alternative $(2-1/\Gamma(1/\epsilon))^qE(q)$ | An actual permitted set with fractional assignments as comparator; exact assignment budget; whole-ground alternative for fixed accuracy |
| [Unrelated values with a joint role](problems/unrelated-values-joint-role/) | Factor $2+\eta$ with setup; exact two in $2^q$; player-specific two-value J2 endpoint | $(2-1/\Gamma(R))^qE(q)$; J2 $(27/4)^{\nu_C}$ or $(50/27)^qE(q)$ | Near-two uses fixed $R=(2+\eta)/\eta$ and permits an actual optional basis; J2 requires compulsory players with pair values $\{0,u,a\}$ |
| [Whole-ground selection and transfers](problems/whole-ground-allocation/) | Converts forced-omission extensions without changing comparator or exact constraints | $A^c\longmapsto(2-1/A)^qE(q)$ | Fixed A>1, all-input forced-seed extension and polynomial space; weighted/adaptive selection and rational optimization retained |

### Selected flow and robust allocation

Time entries suppress polynomial encoded-input work. Whole-ground alternatives use fixed accuracy/tradeoff parameters. Scenario lists are explicit; one permitted selected set is shared, while scenario routings or assignments may adapt.

| Problem | Output or guarantee | Quantitative result | Model and scope |
|---|---|---|---|
| [Selected concurrent flow](problems/selected-flow/) | $(1-\epsilon)$ of optimum common splittable rate | $\Gamma(1/\epsilon)^c$ or $(2-1/\Gamma(1/\epsilon))^qE(q)$ | Paid exact restriction selector; permitted commodity set and exact routing constraints; whole-ground alternative for fixed accuracy |
| [Flow with shared setup budget](problems/shared-setup-flow/) | $(1-\epsilon)$ of optimum common rate | $\Gamma(1/\epsilon)^c$ with the whole-ground alternative | Paid minimum-setup restriction optimizer; one combined setup/routing budget; routing-only budgets exact |
| [Robust selected flow](problems/robust-scenario-flow/) | One commodity set attains $(1-\epsilon)\mathrm{OPT}$ in every scenario | $\Gamma(1/\epsilon)^c$ with the whole-ground alternative | Paid exact restriction selector; separate exact scenario budgets and adaptive splittable routings |
| [Robust unrelated allocation](problems/robust-unrelated-allocation/) | At $(\omega,p)$: $\max\{0,(1-\epsilon)\mathrm{FOPT}-u_{\omega,p}\}$ | $\Gamma(1/\epsilon)^c$ with the whole-ground alternative | One actual basis; exact per-scenario setup/assignment budgets |
| [Robust bounded-width certificates](problems/robust-bounded-certificates/) | Fixed integer factor $d\ge2$ under failure width $w$ | $A^c$ or $(2-1/A)^qE(q)$, $A=\max\{w,\Gamma((d+1)/(d-1))\}$ | Width is a stated promise, not automatic |
| [Width-two robust unit allocation](problems/robust-width-two-allocation/) | Exact common-basis unit feasibility | $\varphi^c$ or $((5-\sqrt5)/2)^qE(q)$ | $\varphi=(1+\sqrt5)/2$; width two bounds minimal aggregate budget-feasible one-unit failures |
| [Two-scenario hardness](problems/robust-two-scenario-hardness/) | W[1]-hard exact positive service in corank $c$ | Parameter-preserving reduction with $c=k$ | Two explicit scenarios; Boolean recipient ranks are free, while nonnegative assignment costs and both exact budgets remain |

### Scheduling

Time entries suppress polynomial encoded-input work. Every positive approximation returns a complete integer schedule. Each card specifies whether a cost budget is present; all stated budgets and original job totals are retained.

| Problem | Output or guarantee | Quantitative result | Model and scope |
|---|---|---|---|
| [Arbitrary-processing scheme](problems/arbitrary-processing-scheduling/) | Factor $1+\epsilon$ | $\Pi_\epsilon^q=2^{O(q/\epsilon)}$ | Exact assignment budget for the scheme. Separate common-type/no-budget branch: $\min\{\mathrm{OPT}+a,(1+\epsilon)\mathrm{OPT}+u\}$ in $\Gamma(1/\epsilon)^k$ when $c_{\rm slot}(\mathrm{OPT})\le k$, $0<\epsilon\le1/2$ |
| [Activated-machine scheduling](problems/activated-machine-scheduling/) | Factors $1+\epsilon$, $3/2$, and the bucket curve | $\binom qr\Pi_\epsilon^r$; $\binom qr6^r$; $\binom qr(k+1)^r$ | Actual rank-$r$ activation bases |
| [Six-profile scheduling](problems/six-profile-three-halves/) | Exact factor $3/2$ | $6^q$ | Unrelated processing times; six profiles per machine |
| [Processing-bucket tradeoff](problems/processing-bucket-tradeoff/) | $\gamma_k=(3\cdot2^k-1)/(2^{k+1}-1)$ | $(k+1)^q\operatorname{poly}(H+k)$ | Approaches $3/2$ with increasing bucket depth |
| [Two-size scheduling](problems/two-size-scheduling/) | Exact $3/2$; separate $5/3$ small-large-count regime | $(27/4)^c$ or $(50/27)^qE(q)$; separate $2^{O(h)}$ branch | $c=q-h$ is surplus large positions; h is mandatory large-unit count; common type sizes and no assignment-cost budget |
| [Per-machine two-time scheduling](problems/two-time-scheduling/) | Factor $2-1/d$ for fixed integer $d\ge2$ | $(2-1/\Gamma((d+1)/(d-1)))^qE(q)$ | At most two positive times per machine; zero-time handling is explicit |
| [Many-size workload scheduling](problems/many-size-scheduling/) | $\min\{2\mathrm{OPT},(2-1/(3+\eta))\mathrm{OPT}+u\}$ | $\min\{2^{O(h)},(h+1)^{O((1+\eta^{-1})\log(h+1))}\}$ | $0<\eta\le1$; h counts mandatory largest-size units; common type sizes and no assignment-cost budget |
| [Commitment scheduling](problems/commitment-scheduling/) | Bottleneck/additive guarantee; two-size $3/2$ or $5/3$ endpoints | $2^{O(k)}$ with a rank-quasipolynomial relaxed alternative | Common type sizes without an assignment-cost budget; full-machine contraction permits more large units than machines, and eligibility-width/collision refinements have their own certificates |

### Matching certificates and oracle barriers

These records separate constructive certificates, promise conditions, and lower-bound models.

| Problem | Output or guarantee | Quantitative result | Model and scope |
|---|---|---|---|
| [Hypergraph matching and expander routing](problems/strong-haxell-matching/) | Left-perfect matching or an explicit deficient hitting-set certificate | $O(\lvert A\rvert+\lvert B\rvert)+p\exp(O(U\log(2+s)/s))$ | $\Delta\ge4$, right-resource rank r, $U=\log(p+4)$ and $s=\log\Delta$; also certified disjoint paths and density-conditioned spanning expander packing |
| [Independent transversals](problems/independent-transversal/) | Independent transversal or a dominating-set/constellation certificate | $P\min\{e^{O(q)},(q+1)^{O(\epsilon^{-1}\log(2+r/\epsilon))}\}$ | Explicit graph/partition; no vertex has r independent neighbours in distinct classes; full bit and rational-accuracy factors remain on the card |
| [Allocation and scheduling barriers](problems/allocation-lower-bounds/) | Below-two allocation and below-$3/2$ scheduling oracle barriers | $\binom qr-1$ deterministic recipient-rank queries | Also aggregate configuration gap approaching $r$, residual gap two, and a zero refined-parameter family |

## Supporting results

These additional algorithms, structural lemmas and scoped boundaries have their own complete manuscripts. Further refinements are listed with their parent result in the [proof index](CONTENTS.md).

| Result | Output or guarantee | Quantitative result | Model and scope |
|---|---|---|---|
| [Grouped choices under resource deletions](manuscripts/graph-backends/decremental-choice-recourse-lemma.md) | One live representative per group with bounded prefix recourse | $O((M\log R+Q)\log(M+2))$ representative changes | M groups, R resources and Q adaptive deletions; augmenting-path discovery work is separate |
| [Nonuniform sparse route rounding](manuscripts/graph-backends/nonuniform-fractional-path-selection.md) | Choose one supplied candidate per group while controlling every resource load | Load $\le2\mu_x+B\log(8(\lvert X\rvert+1))$; $S\operatorname{poly}(\log S,b)$ bit work | Explicit sparse occurrences, rational masses and weights; B bounds one weighted occurrence contribution |
| [Short path inventories from a shared DAG](manuscripts/graph-backends/compressed-fractional-path-extraction.md) | Retain at least half of the unit commodities on short candidate routes | $O(Z+P)$ arithmetic operations; route length $\le4H$ and fractional load at most doubled | Supplied DAG and rational masses with total weighted length at most MH; explicit expansion is output-charged |
| [Bounded-width lazy path client](manuscripts/graph-backends/bounded-interface-witness-pattern-updates.md) | Complete static numerical client with implicit physical-path updates | Time $(m+\nu)\exp(O(b^2))h\operatorname{polylog}S$; space $(m+\nu)\exp(O(b^2))$ | Supplied fixed edge-partition hierarchy of height h and boundary b; decomposition-input work is additional |
| [Forest-support numerical client](manuscripts/graph-backends/complete-unrestricted-forest-one-sided-client.md) | Complete threshold search with unrestricted receiving directions | $(m+\nu)\operatorname{polylog}S$ total fixed-ledger work | The entire ambient allocation support is a forest, with the stated polynomial-range guards |
| [Feedback-edge numerical client](manuscripts/graph-backends/feedback-edge-one-sided-client.md) | Complete threshold search with k nonforest incidences | $(m+\nu(k+1))\operatorname{polylog}S$ total work; $(k+1)\operatorname{polylog}S$ per query/update plus events | Fixed polynomial-range ledger; parameterized support theorem does not improve arbitrary-graph matching time |
| [Weak-Haxell certifying matching](manuscripts/matching-and-routing/weak-haxell-current-blocker-growth.md) | Left-perfect matching or an explicit violated hitting-set condition | $P(n+1)^{O((r/\epsilon)\log(2+r/\epsilon))}\operatorname{poly}(b_\epsilon+\log P)$ | Whole-edge rank $r\ge2$, $0<\epsilon<1$; matching under $\tau(E_S)>(2r-3+\epsilon)(\lvert S\rvert-1)$ |
| [Sparse-separator corank refinement](manuscripts/allocation-and-scheduling/attained-set-sparse-separator-gap.md) | Smaller extension and whole-ground bases when the returned separator is sparse | $\beta(R,w)^c$; $\beta(2,3)=(1+\sqrt5)/2$, $\beta(3,4)=1+\sqrt2$ | Actual separator width w; matching global bases $(5-\sqrt5)/2$ and $3-\sqrt2$ use the forced-omission wrapper |
| [Whole-ground robust allocation barrier](manuscripts/allocation-and-scheduling/robust-unit-allocation-whole-ground-oracle-barrier.md) | Every finite multiplicative guarantee requires near-exhaustive rank queries | At least $q^{-1}\binom qr-1$ deterministic queries; $2^{q-O(\log q)}$ for balanced rank | $2\le r<q$; q explicit scenarios, uniform player matroid and zero costs; separate attributed two-scenario implication |
| [Implicit minimal-bundle transversals](manuscripts/matching-and-routing/implicit-minimal-bundle-transversal-oracle.md) | Disjoint minimal bundles or an explicit domination/constellation certificate | $P(q+1)^{O(\epsilon^{-1}\log(2+q/\epsilon))}\operatorname{poly}(b+b_\epsilon+\log P)$ | No configuration enumeration or arbitrary-neighbour oracle; certificate class sets retain their distinct meanings |
| [Global free pool at the critical quota](manuscripts/allocation-and-scheduling/critical-unit-quota-global-free-pool.md) | Globally resource-free owners cover the current player-rank deficit | $r_M(F)\ge r-k$ when the full quota is $t=3b-2$ and each current record has b units | Fully normalized prefix invariant; eligible free owners admit a paid exchange; no faster critical-quota runtime follows |
| [Jointly independent layer owners](manuscripts/allocation-and-scheduling/joint-owner-sharp-quality-addendum.md) | Within-layer joint independence retains the sharp availability-dependent quality | Factor $\lambda^{-1}+3-3/r+\eta$ with the original rank-exponential or relaxed rank-quasipolynomial time | The stated current-blocker and paid availability model; joint independence alone does not supply a polynomial batching theorem |
| [Explicit laminar reservation interface](manuscripts/allocation-and-scheduling/laminar-resource-current-blocker-reservations.md) | Token reservations and antichain compact certificates for recipient constraints | No laminar-depth factor in the resource value certificate | Includes the stated local-family interfaces; its older base-model approximation is subsumed by the main recipient-polymatroid theorem |
| [Persistent path-hitting certificates](manuscripts/graph-backends/fixed-hitting-certificates-under-graph-updates.md) | One shared update set preserves all historical path-hitting certificates | $C\cup I$ hits current short paths; size at most $\lvert C\rvert+\lvert I\rvert$ | Deletions and length increases are safe; inserted/decreased edge lifetimes enter I; selected-path and layer repair are separate |
| [Fixed-potential tight-DAG repairs](manuscripts/graph-backends/fixed-potential-tight-dag-repair-lemma.md) | Maintain old-label shortest-path forests on tight-reachable vertices | $O(m+\nu)$ total graph work and supplied forest edits per fixed-potential interval | No ledger births or label changes inside the interval; potential-refresh work is outside the bound |
| [Slack-only directed matching reduction](manuscripts/graph-backends/slack-only-one-sided-matching-client.md) | Constant-ratio comparison and a finite-word static threshold oracle | Directed nonnegative SSSP reduction with monotone prices and a charged repricing budget | The dynamic path-reporting/update provider remains a separate unproved interface; no improved general-matching exponent |
| [Residual-capacity configuration comparator](manuscripts/allocation-and-scheduling/recipient-polymatroid-residual-configuration-relaxation.md) | Integral allocation with factor $4-3/r$ against the strengthened residual-capacity configuration LP | $2^{O(r)}\operatorname{poly}(H)$; the stated rank-quasipolynomial alternative allows additive accuracy in the factor | Arbitrary binary recipient polymatroids and exact local availability; certified factor-$\lambda$ availability changes the ratio to $\lambda^{-1}+3-3/r$. The algorithm does not solve the LP |
| [Fractional optimization of residual configuration relaxations](manuscripts/allocation-and-scheduling/residual-configuration-bounded-support-xp-solver.md) | A feasible fractional configuration point at target at least $(1-\epsilon)\mathrm{OPT}_{\rm LP}$ | Full LP: $2^{O(q)}\operatorname{poly}(H,\epsilon^{-1})$; support-s cuts: $(q+1)^{O(s+1)}\operatorname{poly}(H,\epsilon^{-1})$ | Coordinate-box local families and binary capacities; $s=2(r-1)$ gives an XP rank bound. This is optimization of the stated fractional comparator, with separate integer rounding |

## Reading and verification

Start with a result card, then read its `proof.md`. Longer derivations are linked as companion manuscripts. Shared graph interfaces, allocation lemmas, and explicit obstruction constructions are indexed in [Contents](CONTENTS.md#shared-manuscripts). The source map names the dependencies used by that result.

Each `verify/README.md` explains the available evidence and its limits. Exact finite certificates check specified identities, finite examples, or certified domains; they do not by themselves establish every asymptotic theorem. The repository does not claim proof-assistant verification or external peer review.

The [maintenance guide](CONTRIBUTING.md) gives the single local check command and the rules for updating statements, proof dependencies, and this generated catalogue.

## Citation and attribution

Yilin Liu and GPT-6 Astra Pro. *Algorithm Frontier* (2026). Cite the relevant problem path and commit; the [citation protocol](PROTOCOL.md) and [import provenance](provenance/README.md) retain the applicable licenses and notices.
