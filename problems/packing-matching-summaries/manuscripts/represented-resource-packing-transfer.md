# Quadratic matching summaries and a packing transfer of the failure-projection lift

**Abstract.** We combine exterior packing features with polynomial failure features and an optional represented resource matroid. A weighted basis of the product space preserves every feasible packing context, prescribed cardinality, and fixed linear cost under bounded failures. The replacement guarantee remains valid in arbitrary later extensions of the original resource matroid.

This note transfers the polynomial-failure projection to set packing with a represented resource matroid. Its most concrete consequence is an exact deterministic universal summary for general multigraph matching with

$$
r(h_e+1)\binom{2K+h_v}{2}
       =O\!\left(r(h_e+1)(K+h_v)^2\right)
 \tag{1}
$$

original edges, where r is the full positive-side resource-matroid rank, K is the maximum matching size of interest, and queries may fail at most h_v vertices and h_e original edge IDs. The summary also supports arbitrary later matroid extensions supplying a quota-free background, even if the later extension is not represented. The positive resource matroid must be explicitly represented at preprocessing.

Compared with W–UH's arbitrary-oracle graph bound O(r(h_e+1)(K+h_v+1)^3 log^3(r(h_e+1)(K+h_v+1)+2)), this removes one power of the matching/vertex-failure parameter and the logarithmic factors **under the stronger represented-resource input model**. It does not improve W–UH for arbitrary independence-oracle resources. Ordinary matching has no additional resource factor and gets (h_e+1) binomial(2K+h_v,2) retained edges.

The algebra is within the classical representative-family framework. The new contribution claimed for this manuscript is the specific universal failure/completion transfer and explicit comparison, subject to focused literature review. It is not a claim to invent the exterior-algebra representative-set method.

## 1. General model

There is an explicit item set E. Every item e carries a subset S_e of a packing universe U, with |S_e| at most p, where p is positive. Feasible positive choices contain at most K items and their packing sets are pairwise disjoint. Items have fixed arbitrary signed linear costs.

Optionally, E also carries a matroid M represented by columns v_e over the rationals or an explicit finite field. Its full, untruncated rank is r. Positive choices must be independent in M, or in a later matroid M+ on E disjoint union Z whose restriction to E is M when background elements are included.

Queries may specify:

- A set V_f contained in U of at most h_v failed packing-universe elements. An item meeting V_f fails.
- For each of s independent failure-label systems j, a set F_j of at most h_j labels. Item e has at most d_j labels Lambda_j(e), and fails if any Lambda_j(e) meets F_j.
- An arbitrary matroid extension M+ with M+ restricted to E equal to M, a fixed background choice Y contained in Z, and a desired positive cardinality at most K. Background elements do not consume packing-universe elements or carry the positive-item failure labels.

The ground, original representation, packing sets, positive costs, and label assignments remain fixed. Only the allowed failure sets and later extension/background are variable. Specified totals are preserved, never reset to the rank of a restriction.

The theorem is stated for explicit items. Before padding, replace an oversized bound p by max{1, max_e |S_e|}; this preserves the instance and can only improve the displayed upper bound. Thus the padding length is bounded by the explicit input.

If K=0, return the empty positive summary and leave any background-only feasibility or optimization to the query. If a required resource matroid has rank zero, no positive item can occur and the same conclusion applies. The nontrivial construction below assumes K and r are positive when the resource is present.

## 2. Main transfer theorem

With a represented resource matroid, there is a deterministic restriction H contained in E of size at most

$$
\min\left\{|E|,\;
      r\binom{pK+h_v}{p}
       \prod_{j=1}^{s}\binom{h_j+d_j}{d_j}
      \right\}
 \tag{2}
$$

having this original-context replacement property:

For every allowed query, every feasible independent context T in M+ whose positive items form a live packing of size at most K, and every positive item e in T, there is a live retained item f in H outside T minus e such that

$$
\begin{split}
 &(T-\{e\})\cup\{f\}\text{ is independent in }M^+,\\
 &\{S_a:a\in (T\cap E)-\{e\}+\{f\}\}\text{ is a packing},\\
 &c(f)\le c(e).
 \end{split}
 \tag{3}
$$

The whole background T intersect Z stays fixed. Replacing positive items outside H one at a time yields preservation of the minimum positive cost for every fixed background and every prescribed positive cardinality at most K. The guarantee also preserves feasibility and full total size.

Without a resource constraint, omit the factor r in (2) and the resource-independence statement in (3). Pairwise disjoint packing sets still ensure that the replacement does not duplicate an item already in the positive context.

The algorithm is uniform polynomial time in the explicit input: as in the companion failure-lift manuscript, it returns the input unchanged when the displayed dimension is at least |E|, and otherwise constructs a lifted matrix with fewer than |E| rows.

## 3. Packing vectors

Pad every packing set to exactly p elements with private dummy universe elements that occur in no other item and never fail. This preserves pairwise disjointness and is polynomial in the explicit input. Padding also handles initially empty packing sets without introducing a duplicate-item issue.

Set t=pK+h_v. Assign distinct field values to the enlarged packing universe and represent its elements by Vandermonde columns u_x in K^t. Every set of at most t distinct columns is independent. For an item e put

$$
a_e=\bigwedge_{x\in S_e}u_x
                   \in\bigwedge^p K^t.
 \tag{4}
$$

The packing-feature dimension is binomial(t,p). A fixed ordering of universe elements determines all signs.

Consider a protected e in a feasible packing and define

$$
C=V_f\cup\bigcup_{a\in(T\cap E)-\{e\}} S_a.
 \tag{5}
$$

Use a set union, so duplicate occurrences of a failed universe element cause no repeated wedge factors. Then |C| is at most p(K-1)+h_v, and the protected S_e is disjoint from C. Therefore

$$
a_e\wedge\bigwedge_{x\in C}u_x\ne0.
 \tag{6}
$$

Choose a coordinate functional psi on the target exterior power that is nonzero on (6), and define the linear functional

$$
L_C(a)=\psi\left(a\wedge\bigwedge_{x\in C}u_x\right).
 \tag{7}
$$

It is nonzero on a_e and is zero on every a_f whose packing set meets C. It need not be nonzero on every valid replacement; only the protected nonzero value and rejection of all conflicts are needed.

## 4. Failure features and the lifted greedy basis

For each label system j, use the coefficient construction of the companion failure-lift manuscript. It supplies a feature vector phi_j(e) of dimension binomial(h_j+d_j,d_j) and, for every allowed F_j, a linear functional ell_{F_j} such that

$$
\ell_{F_j}(\phi_j(e))=0
        \quad\Longleftrightarrow\quad
       \Lambda_j(e)\cap F_j\ne\varnothing.
 \tag{8}
$$

Explicitly, choose a never-failing dummy scalar a_0, pad the label-root polynomial g_{j,e}(X) to monic degree d_j, and take all coefficient monomials of total degree at most h_j. The query functional evaluates the polynomial product over lambda in F_j of g_{j,e}(a_lambda).

With a resource matroid define the lifted column

$$
z_e=v_e\otimes a_e\otimes
                       \bigotimes_{j=1}^{s}\phi_j(e).
 \tag{9}
$$

Without the resource matroid, omit v_e. Keep the cost-ordered greedy basis of these lifted columns. Its cardinality obeys (2), and for every protected e it supplies a relation

$$
z_e\in\mathrm{span}
                      \{z_f:f\in H,\ c(f)\le c(e)\}.
 \tag{10}
$$

Inside a cost tie, only predecessors in the fixed total order are needed when e is discarded.

## 5. The unknown extension does not need a representation

This is the main quantifier point. Let T be an independent context in an arbitrary later extension M+, and protect e in T intersect E. Define

$$
A=E\cap\mathrm{cl}_{M^+}(T-\{e\}).
 \tag{11}
$$

A is a flat of the original matroid M. Indeed, M+ restricted to E is M, and closure of A in M is contained in closure of T minus e in M+, intersected with E. Moreover e does not belong to A by independence of T.

Because M is represented, there exists a linear functional L_A on its representation space that vanishes on all v_f with f in A and is nonzero on v_e. This functional is used only for the proof; neither A nor a representation of M+ is needed by preprocessing.

Apply

$$
L_A\otimes L_C\otimes
                        \bigotimes_j\ell_{F_j}
 \tag{12}
$$

to (10). The protected left side is nonzero. Therefore at least one retained f on the right has all factors nonzero. For that f:

- L_A(v_f) nonzero implies f is outside closure of T minus e, so it preserves resource independence and is not already in T minus e.
- L_C(a_f) nonzero implies that S_f avoids the packing context and all failed universe elements.
- Every label functional is nonzero, so all label-failure tests are passed.
- Its cost is at most c(e) by (10).

This is (3). Omitting the resource factor proves the no-resource case; the private padding makes S_f intersect C whenever f already belongs to the positive context, so duplicating an item cannot be the nonzero witness.

Each replacement removes one positive item outside H and inserts an item of H. Thus repeated replacement terminates. No changing reduced resource, recomputed mandatory total, or access to future failure sets enters construction.

The same proof is local in the candidate pool. If only a pool Y contained in E is reduced, take a basis of the lifted columns indexed by Y; the protected e must lie in Y, but the other positive context items may lie anywhere in the original E. The size bound may use the dimension of span{v_e:e in Y}, while the proof's flat A and packing context are still defined in the original resource and original full ground. This is a reduction of candidates in Y, not permission to discard outside elements or truncate the original matroid.

## 6. General multigraph matching

Set p=2 and take S_e to be the two endpoints of each nonloop edge. Parallel edges are distinct original items, even when they have the same endpoint set. The exterior feature lives in dimension binomial(2K+h_v,2).

To tolerate h_e individual edge deletions, give each original edge its own label in one failure system with d_1=1 and h_1=h_e. Its feature dimension is h_e+1. Equation (2) gives exactly (1).

More generally, if an edge carries at most d risk labels and a query fails h labels, the size is

$$
r\binom{2K+h_v}{2}\binom{h+d}{d}.
 \tag{13}
$$

Independent budgets for individual edge IDs and whole risk classes can be handled by separate feature factors. For example, single-color risk groups with at most h_c failed colors, in addition to h_e individual edge failures, give

$$
r(h_e+1)(h_c+1)\binom{2K+h_v}{2}.
 \tag{14}
$$

Every formula applies to arbitrary undirected multigraphs and arbitrary signed fixed edge costs. There is no bipartiteness, bounded-degree, planarity, or bounded-color-class-size assumption. The extra resource M may be any represented matroid on the original edge IDs. The later extension/background can be arbitrary subject to preserving its restriction to those positive IDs.

Loops can be removed before construction since they are not eligible matching edges. Original edge IDs are retained; one must not merge parallel edges when individual-ID failures are allowed.

Without an extra resource constraint the factor r is omitted. Thus this also gives a deterministic exact kernel of original edges for minimum-cost matchings of every cardinality at most K under all allowed failures. It is a preprocessing-size result, not a new faster algorithm for unrestricted maximum matching and not an improvement to the original 4/5 exponent.

## 7. Construction cost, field model, and scope

Let D be the right side of (2) without the minimum with |E|. Compute D with saturation at |E|. If D is at least |E|, return all items. If D is smaller, every feature factor has dimension at most D and all of (9) can be explicitly constructed in polynomial time. The Vandermonde ambient dimension pK+h_v is polynomial in the explicit input after clipping K to |E| and h_v to |U|. Exterior coordinates are p by p minors, so straightforward determinant computation for each listed coordinate suffices. The Gaussian stage uses O(|E| D^2) field operations.

Use the rational or explicit finite-field construction from the companion manuscript to supply sufficiently many distinct scalars. Field extension preserves the original resource ranks. The proof does not rely on a randomized representation, randomized determinant evaluation, or polynomial identity testing. Cost comparisons are exact and separate from field arithmetic.

This manuscript does not assert an oracle implementation for a nonrepresented resource matroid, a binary-owner compression theorem, arbitrary positive recosting, or a runtime for optimizing over an unspecified later extension. It proves a uniform-polynomial preprocessing restriction and its pointwise exact replacement guarantee. Query-specific algorithmic improvements may use the existing W–QK interface when its hypotheses are satisfied.

### 7.1 Bit accounting and output representation

Let `D` denote the product dimension in (2) before taking the minimum with `|E|`. The dimension gate is applied using saturated integer arithmetic, so no tensor or exterior-coordinate list is materialized when `D >= |E|`. In the rational model, let `b_in` bound the bit length of resource entries, costs, and explicitly listed universe/label identifiers, and let `U'` be the padded packing-universe size. After row-wise denominator clearing, a conservative bound for one lifted matrix entry is

```text
B_mat = O(|E|*b_in + p*(p*K + h_v)*log(U' + 2)
                      + p*log(p + 2)
                      + sum_j h_j*d_j*log(L_j + 2)
                      + log(|E| + D + 2)),
```

where `L_j` is the number of labels in system `j`. The Vandermonde columns have coordinates through degree `p*K + h_v - 1`; the factor `p*(p*K + h_v)` bounds the total degree of a determinant term. Exterior coordinates are determinants of `p` by `p` Vandermonde submatrices, and the label factors are the coefficient monomials from the failure-lift construction. Fraction-free elimination therefore uses `O(|E|*D^2)` arithmetic operations and, with integer multiplication cost `M`, at most

```text
\widetilde O(|E|*D^2*M(D*B_mat + D*log(D + 2)))
```

bit operations, plus polynomial preprocessing for padding, determinant coordinates, feature generation, rank compression, and exact cost sorting. For an explicit finite-field representation, replace `B_mat` by the field-element representation length and the multiplication cost by the chosen field-arithmetic cost. The bound counts original item IDs in the output separately from the auxiliary tensor/elimination workspace.

## 8. Related work and scope

The exterior packing feature is classical representative-family machinery: repeated universe vectors force a zero wedge, and a weighted basis keeps a nonworse witness for every annihilating linear functional. Relevant primary antecedents are:

- Fomin, Lokshtanov, Panolan, Saurabh, *Efficient Computation of Representative Families with Applications in Parameterized and Exact Algorithms*: https://sites.cs.ucsb.edu/~daniello/papers/efficientRepSetJ.pdf
- van Bevern, Tsidulko, Zschoche, *Representative families for matroid intersections, with applications to location, packing, and covering problems*: https://arxiv.org/html/1806.11527v4

The construction specializes the representative-family framework to the stated product dimension and arbitrary-extension replacement guarantee. Its proof uses the flat in (11), the nonzero protected exterior product in (6), and exact original item identities. The resource representation is additional input; an arbitrary independence oracle is not a substitute.
