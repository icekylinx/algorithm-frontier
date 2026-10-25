# Checkpoint X — incremental TCS research drafts

English rough drafts for external review. Attribution: Yilin Liu and GPT-6 Astra Pro.

This bundle contains new material from the current continuation. The reference repository is [Algorithm Frontier](https://github.com/icekylinx/algorithm-frontier), inspected at commit `37b31138bf102a83d9efb2cbe44437eec45ae3c2`. The repository itself was not modified. The original general-matching exponent 4/5 is not being revisited.

## Suggested reading order

### 1. Exact single-failure optimization in directed graphs and matroid intersection

The main new candidate is an exact sensitivity preserver for the minimum-cost common independent set of two arbitrary matroids. For a prescribed feasible cardinality k, it retains O(k^(3/2)) original elements. A reporting structure of the same number of word records returns an exact optimal size-k solution after any one element failure in O(k) time, without further matroid-oracle calls. Combining cardinalities r and r−1 handles minimum-cost maximum-cardinality solutions and rank drops.

For arbitrary directed graphs this gives an exact minimum-cost spanning-arborescence preserver with O(n^(3/2)) original arcs, deterministic preprocessing in soft-O(mn) arithmetic operations, and O(n) time to report a surviving optimal arborescence. The polynomial bit cost of rational arithmetic is additional to these arithmetic-operation counts. The word space includes original element identifiers and exact numerical quantities where needed.

The reduction uses a compressed exchange graph, integrality of the common-base polytope, minimum-cost minimum-hop cycles, and the classical directed pairwise distance-preserver bound. The path-reporting variant stores short paths and shortest-path trees with multiplicity; the space statement is not inferred merely from the size of their union.

The direct public comparator is Dey–Kavitha, *Low-Cost Arborescence Under Edge Faults*, May 2026, Theorem 1.1 and Section 5: O(n^(3/2)) arcs for factor-two approximation, with sparse exact preservation explicitly posed as an open problem. This is a claim of a new proof-bearing draft answering that question, subject to the external review requested by the user. A broader priority claim is not assumed.

The same draft includes an equivalence with directed distance preservation for linearly many demands in the general two-matroid/bipartite matching setting, an inherited lower bound, and a simple quadratic obstruction for **two** failures. Those lower bounds are not automatically lower bounds for rooted arborescences.

A companion draft extends the O(k^(3/2)) retained-size and O(k) reporting guarantee to the sum of two arbitrary rank-k valuated matroids, with value-oracle preprocessing. It proves the needed joint convex-decomposition and valued exchange-matching lemmas. This is a fixed-rank, fixed-valuation, single-original-element-failure theorem; smaller-rank objectives and correlated failures are not inferred from it.

### 2. A strict deterministic Subset Sum exponent improvement

The current closed increment changes actual recursive/direct circuit families in the repository's fast-time framework. Its full-input exponent is

    149809813343531 / 301825962128739 ≈ 0.4963450204447026...

compared with the repository baseline

    149809813343531 / 301754962128739 = 0.496461805587...

The theorem is incremental: it relies on the repository's circuit compiler, representation reduction, and complete cost accounting. It keeps the same uniform bit-algorithm interpretation for arbitrary signed binary inputs, indexed witness recovery, and a finite input-independent startup constant. It does not combine the fast-time bound with the separate low-space bound. The draft specifies the new parameter families, contact inequalities, full piecewise profile, and every outer cost line.

### 3. Correlated failures in boundary matrices and persistent homology

An incidence-sensitive lift gives a restriction of at most

    r * binomial(h + a + b, a + b)

top-dimensional simplices, where r is boundary-matrix rank, each vertex has at most a failure labels, and each top simplex has at most b additional labels. All failures of at most h labels and all prefixes of one fixed filtration are handled by the same restriction. The entire lower skeleton is retained. Boundary spaces, homology in lower dimensions, and the associated persistent modules are preserved over a specified field.

For one vertex color and no top-cell labels, the sharper envelope is

    min{N, k*r, binomial(n,p+1) − binomial(n−k,p+1)},
    k = min{h+1, number of colors}.

The fixed-n envelope and the leading general binomial coefficient have matching constructions in the stated original-cell model. Ordinary no-failure spanning forests, exterior-rank identities, and the exact ordinary-vertex graph bound are attributed to their existing sources. The proposed increments concern correlated failures and their simultaneous query/filtration interpretation.

### 4. Sharp binomial summaries for matroids, graphs, packing, and submodular information

For an explicitly represented rank-r matroid with at most d failure labels per item, a deterministic uniform polynomial-time construction retains at most

    min{|E|, r * binomial(h+d,d)}

items while preserving every surviving prefix span in a fixed cost order. Consequently it preserves exact minimum-cost bases, including rank drops. The binomial bound is sharp. In edge-colored graphs, d=1 gives (h+1)r edges, removing the logarithmic size loss in the polynomial construction quoted by Petruschka–Sapir–Tzalik's April 2026 connectivity-labeling paper.

The separate vertex-color lift yields O(hn) edges for arbitrary correlated vertex-color classes, with sharper rank envelopes, and O(h^2 n) for mixed one-vertex-color/one-edge-color failures. Color lists are allowed in the broader parameterized statement. Existing spanner constructions already imply weighted-prefix/MSF preservation when processed in weight order; that capability alone is not claimed as new.

Without a linear representation, the exact r*binomial(h+d,d) size bound still holds for **rank-only** summaries of arbitrary matroids. The supplied construction is deterministic FPT in r+h+d, rather than unrestricted polynomial time. A circuit-blocking permutation inequality extends to monotone submodular functions and gives a sharp bound on total worst-case marginal sensitivity. The associated entropy corollary is stated with exact correlated-erasure semantics. The arbitrary-oracle weighted binomial bound is not inferred from this unweighted argument.

The packing note gives a represented-resource improvement through a tensor/exterior representative construction. Its representation assumption must be retained when comparing with the previous arbitrary-oracle bounds. The Boolean linear optimization compiler is a secondary consequence of a supplied Subset Sum backend, with earlier interval-shrinking work explicitly credited; it is not a new best bound for unrestricted high-dimensional integer programming.

## Baseline scope

The current OpenAI public catalogue was checked at repository HEAD `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, using its [overview](https://github.com/openai/math/blob/main/overview.tex) and the relevant entries. The catalogue check did not locate an arborescence/fault-preserver entry. This is a bounded catalogue check, not a review of all manuscripts.

OpenAI catalogue entry 138 states a randomized O(2^(0.49n)) Subset Sum algorithm. The deterministic exponent above is numerically larger than 0.49 and is not advertised as beating that randomized running time. The improvement claimed here is over the pinned deterministic repository baseline. Entry 114 concerns approximate counting of common integer polymatroid bases and is a different task from exact sensitivity preservation.

The individual drafts give primary references and distinguish inherited ingredients from proposed contributions. They are intended for mathematical review and organization, with no claim of formal verification or exhaustive priority clearance. No old checkpoint bodies, proof-assistant files, PDFs, experimental programs, or internal review logs are bundled.
