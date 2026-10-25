# Checkpoint X proof review: first pass

Status: internal review notes. These observations are not a priority or novelty claim. Promote a theorem only after the cited ingredients and the repaired statements have been checked against the source files. The low-risk wording repairs listed below have been applied directly to the current 01/03/05/09 drafts; the remaining items are still review gates.

## 01 — exact single-failure two-matroid/arborescence draft

The exchange-polytope argument is coherent, including the support argument and the minimum-hop update. The exposition should make the following points explicit before a theorem card is promoted:

1. **Two matching maps.** For a replacement (J), state the basis-exchange matching lemma in the exact form used: the bipartite graph on (B\setminus J) and (J\setminus B), with an edge (a e) whenever (B-a+e) is a basis, has a perfect matching. Apply it separately in (M_1) and (M_2). Invert both matchings by the common outside element (e), and define an arc (a_1(e)\to a_2(e)). This gives a permutation of (B\setminus J), whose cycles are the exchange cycles. The current paragraph says “orient ... in reverse” but does not show this common-(e) identification.
2. **Arborescence specialization.** Add the short implication: a common independent set of size (n-1) is an undirected forest with (n-1) edges and gives every nonroot exactly one incoming arc. A component not containing the root would then have indegree at least one at every vertex and hence a directed cycle, contradicting the underlying forest. Thus there is one root-spanning arborescence.
3. **Distance preserver assumptions.** The compressed graph can have negative arcs but no negative directed cycle. State whether the cited distance-preserver theorem permits this, or reweight with an explicitly computed lexicographic potential (Bellman–Ford on a super-source) before invoking a theorem requiring nonnegative weights. Keep the ordered-pair arithmetic for the secondary hop coordinate.
4. **Deterministic hitting proof.** The phase argument should be a named lemma with its path count, (L=\lceil N/\sqrt p\rceil), greedy coverage inequality, number of hubs, and exact record count. Explain how the fixed shortest paths and the in/out trees are stored and how a preserver path is reconstructed without an unproved uniqueness assumption.
5. **Bit complexity.** Parameterize rational arithmetic by the maximum input/value bit length (or explicitly state the finite-word model). “Rational arithmetic has polynomial bit complexity” is not enough when costs or oracle outputs are arbitrary rationals.

## 03 — correlated-failure boundary certificates

The incidence lift (T5)--(T12) is algebraically sound. Before promotion:

- Distinguish the feature dimension (q=\binom{h+d}{d}) from the finite-field size (currently both are written as (q) in Section 4). Use (Q) for the feature dimension and (|\mathbb F|) for field size.
- State in the theorem that one fixed column order is used. A filtration theorem uses filtration order; the cost-basis theorem uses the independent cost order. Do not combine the two bounds unless the orders coincide.
- In the persistence paragraph, explicitly identify the lower chain groups and boundary maps of (H_t-F_0) and (K_t-F_0) in the same coordinates; then the equal “image of ∂p” statement gives commuting persistence-module isomorphisms.
- In the one-color lower-bound example, replace “the top simplices ... are exactly the remaining simplices containing (j)” by “the surviving top simplices at filtration time (j) are exactly the (p)-simplices on the remaining vertices whose minimum vertex is (j).” The unique facet not containing (j) gives their independence.
- For the overlapping-label rank refinement (T21)--(T22), say explicitly that a rank-(s) basis of the feature-coordinate functions spans every query functional, and that the (z)-perturbation only proves rank at most (r) for each weighted block before stacking.

## 05 — colored graph/MSF certificates

The vertex-only activation lemma (G2)--(G9) is sound. The following are concrete repairs:

1. **Mixed vertex/edge features.** Section 6 cannot literally invoke Section 2 because the lifted block φ(v,e) depends on the edge (e), whereas (G3) assumes a vertex-only vector (z_v). State a generalized edge-dependent activation lemma: if each oriented edge (uv) has feature blocks φ(v,e), −φ(u,e), and every query functional evaluates each block to the corresponding endpoint/edge survival product, the row-map proof still preserves every ordered-prefix incidence span. The (nD) row bound is immediate; the symmetric-trilinear construction is an additional dependency family.
2. **Symmetric-cubic refinement.** Replace “the kernel consists exactly ...” by “the map from symmetric trilinear forms to row dependencies has kernel ... and therefore supplies at least ... independent dependencies.” A sparse input graph can have additional row dependencies; equality with the full matrix kernel is not established.
3. **Mixed lower bound.** In G18 the surviving graph still contains the all-surviving core clique, so it is not a tree. What is needed is only that every outer vertex has exactly one surviving incident edge, making that edge compulsory for connectivity. Correct the sentence and leave the lower-bound count unchanged.
4. The dynamic-MS​​F corollary should either cite a data-structure interface that reports forest exchanges or weaken “standard maintained-forest implementation exposes these exchanges” to an explicit implementation assumption.

## 09 — valuated matroid intersection

The valuated local-optimality, supporting-matroid, and exchange-matching arguments are valid with the stated minimization signs. Before promotion:

- In Lemma 2 and the reverse half of (V6), explicitly map each outside element (e\in J\setminus B) to its (M_1)-matched (a_1(e)) and (M_2)-matched (a_2(e)), then form arcs (a_1(e)\to a_2(e)). This makes the cycle decomposition and the sum of arc costs checkable.
- Remove the alternative “or by a sufficiently small rational perturbation” in Section 7. Unless a global rational gap bound is supplied, perturbation can change the ordering of paths; exact ordered-pair arithmetic is the safe implementation.
- The distance-preserver citation must state its weight assumptions. Arc lengths ℓ can be negative, although all directed cycles are nonnegative. Use a lexicographic potential/reweighting argument if the cited theorem requires nonnegative edge lengths.
- Add a valuation-output bit parameter to the complexity statement. Oracle call time alone does not bound the length of returned rational values or the number of bits in the (O(k^3)) comparisons.
- Preserve both coordinates of the lexicographic distances, not only the primary value; the minimum-hop lemma is what makes the reported cycle a literal update with distinct labels.

These items are proof repairs and scope clarifications, not evidence that the proposed results are novel. The drafts should remain marked as drafts until the repaired lemmas and the source assumptions are checked.
