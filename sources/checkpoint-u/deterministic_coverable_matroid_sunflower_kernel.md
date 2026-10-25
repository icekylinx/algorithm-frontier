# Deterministic sunflower kernels for several coverable matroids

**25 October 2026. Increment U. Complete manuscript-level proof with independent internal review.**

This note transfers the external-context sunflower reduction of *deterministic_sparse_packing_oracle_kernel.md* (SK) to several additional matroids whose small independent sets span only a bounded number of parallel classes. The feature supports are now parallel-class IDs, rather than packing-row IDs.

The additional matroids are not replaced by partition feasibility constraints. Their full independence conditions remain in the original instance. Parallel-class features are used only to certify safe single replacements.

## 1. Input and closure-class assumption

Let \(M_0,M_1,\ldots,M_d\) be matroids on one explicit item ground \(E\), supplied by independence oracles. The first matroid \(M_0\) is unrestricted. There is a cardinality limit \(k\) and a rational additive profit \(c_e\), which may be signed as in SK. The original feasible family is

\[
 \mathcal F=\{S\subseteq E:|S|\le k,\
                     S\in\mathcal I(M_i)\text{ for every }0\le i\le d\}.
\tag{CK1}
\]

Here \(d\) counts **additional** matroids, so there are \(d+1\) matroids in total.

Delete elements that are loops in any matroid. In a loopless matroid, the span of a singleton is its parallel class, and every flat is a union of parallel classes. Assume that for each \(1\le i\le d\) a supplied integer \(g_i\ge0\) satisfies:

\[
 \text{if }I\in\mathcal I(M_i),\ |I|\le k-1,\text{ then }
 \operatorname{cl}_{M_i}(I)
 \text{ is a union of at most }g_i\text{ parallel classes.}
\tag{CK2}
\]

This is a semantic structural assumption, not a property the algorithm claims to verify for arbitrary oracle matroids. It is enough that the additional matroid is \(g_i(k)\)-coverable in the sense of Huang–Kakimura–Kobayashi–Terao; one may then use that certified bound. The proof needs only the context sizes in CK2.

The estimates may be capped at \(|E|\), because a loopless ground has at most that many parallel classes. We assume the capped estimates are supplied or computable in polynomial time. The concrete classes below have elementary polynomial estimates.

Set

\[
                            g=\sum_{i=1}^d g_i.
\tag{CK3}
\]

For \(d=0\), one greedy scan gives the usual at-most-\(k\) ground. For \(k=0\), return the empty set. As usual, replace \(k\) by \(\min\{k,|E|\}\).

## 2. The deterministic ground-kernel theorem

**Theorem.** There is a deterministic polynomial-time algorithm returning \(R\subseteq E\) such that, for every original \(S\in\mathcal F\) and every \(e\in S\), some \(f\in R\setminus(S-e)\) satisfies

\[
                    c_f\ge c_e,\qquad S-e+f\in\mathcal F.
\tag{CK4}
\]

For \(d\ge1,k\ge1\), its retained ground obeys

\[
                     |R|\le k\,d!\,[\,k(g+1)\,]^d.
\tag{CK5}
\]

If no two items have the same tuple of parallel classes in \(M_1,\ldots,M_d\), the factor \(k\) in front can be omitted.

Construction uses polynomial binary space and a polynomial number of oracle queries, uniformly in explicit \(d\). This is an **oracle ground kernel**, with the original matroid oracles and rational profits available. It is not a bound on an arbitrary oracle program's encoded size or on all weight bits.

The theorem preserves the best profit for every fixed cardinality up to \(k\), and gives deterministic element-by-element reachability. SK's fixed-original-context composition proves these consequences.

## 3. Computing the features

For each additional matroid, compute parallel classes by comparing each nonloop element with existing class representatives. Two distinct nonloops are parallel exactly when their pair is dependent. This uses at most \(O(d|E|^2)\) singleton/pair independence queries and polynomial storage.

Give item \(e\) the feature set

\[
              \sigma(e)=\{(i,\operatorname{class}_{M_i}(e)):
                                      1\le i\le d\}.
\tag{CK6}
\]

Every support has exactly \(d\) features. Features from different matroids are distinct even when their class labels happen to have the same numerical name.

Keep these original feature IDs throughout the reduction. Removing candidates does not change the oracle or silently replace an original closure by a closure in a different context.

For a fixed feasible context \(I\), let \(\mathcal B_i(I)\) be the feature classes contained in \(\operatorname{cl}_{M_i}(I)\). By CK2,

\[
       |\mathcal B(I)|:=
          \left|\bigcup_{i=1}^d\{(i,C):C\in\mathcal B_i(I)\}\right|
                                  \le g.
\tag{CK7}
\]

For an item \(f\notin I\), all additional matroid extensions \(I+f\) are independent exactly when \(\sigma(f)\) avoids this blocked-feature set. The equivalence holds because a matroid flat contains either all or none of each parallel class.

The algorithm does not need to compute these unknown context closures. They are only used in the correctness proof.

## 4. Identical feature tuples

Within each class of identical \(\sigma(e)\), keep only
\(\operatorname{Greedy}(M_0,\text{class},k)\), scanning in nonincreasing profit order and retaining independent elements until size \(k\).

For every original feasible \(I+e\), the SK greedy lemma returns a no-worse resource-valid replacement \(f\) in this retained set, outside \(I\). Because \(e,f\) are parallel in each additional matroid, \(e\notin\operatorname{cl}_{M_i}(I)\) implies \(f\notin\operatorname{cl}_{M_i}(I)\). Thus all additional constraints remain valid.

This is an external-context reduction: \(I\) need not lie in the current candidate set. Afterwards at most \(k\) items have any one feature tuple, and later deletions preserve that invariant.

## 5. Sunflower thinning with blocked parallel classes

Set

\[
                         t=g+1,\qquad L=kt+1.
\tag{CK8}
\]

If the current ground has more than \(d!(L-1)^d\) distinct feature supports, the constructive Erdős–Rado lemma from SK finds \(L\) distinct supports forming a sunflower. No padding is needed because all supports have size \(d\).

Choose one current item per sunflower support, and let \(V\) be these \(L\) items. Construct \(t\) disjoint layers

\[
 F_j=\operatorname{Greedy}
       \left(M_0,V\setminus\bigcup_{h<j}F_h,k\right),
                              \qquad 1\le j\le t.
\tag{CK9}
\]

Their union has size at most \(kt=L-1\). Delete only the chosen flower items outside this union. At least one item disappears; other items of the same feature tuple are left alone.

Fix a deleted \(e\), and any original feasible \(I+e\) with \(|I|\le k-1\). The item \(e\) survives in every layer's pool. The weighted greedy lemma gives distinct representatives \(f_j\in F_j\setminus I\) satisfying

\[
                   c_{f_j}\ge c_e,\qquad
                          I+f_j\in\mathcal I(M_0).
\tag{CK10}
\]

Every feature in the flower core belongs to \(\sigma(e)\). Such a feature is unblocked, since \(I+e\) is independent in every \(M_i\). All blocked features therefore occur only in petals. The petals are pairwise disjoint, so each blocked feature can obstruct at most one of the distinct \(f_j\).

There are at most \(g\) blocked features and \(g+1\) representatives. Some \(f_j\) avoids all blocked classes and is independent over \(I\) in every additional matroid. It is the required no-worse replacement.

Retained items represent themselves. Thus each flower reduction has the full original external-context property.

## 6. Iteration, size, and polynomial implementation

Repeat the preceding deletion while the distinct-support threshold is exceeded. Every iteration removes at least one item, even if its support still has other surviving copies. There are at most \(|E|\) iterations.

When the process stops there are at most \(d!(L-1)^d\) supports and at most \(k\) items per support. This is CK5. If tuples were initially distinct, they remain distinct, and the leading \(k\) is absent.

For an original \(S,e\), fix \(I=S-e\). Under each successive reduction, replace only the current representative of \(e\); the feasible set always has the form \(I+e_j\), and its profit never decreases. Hence the final result satisfies CK4 even though the unchanged context \(I\) may contain items removed from the candidate ground.

The sunflower construction follows one popular-feature branch at each of at most \(d\) levels. It uses polynomial explicit-set work. If a flower is requested, \(L\) cannot exceed the current number of distinct supports, so \(L\le |E|\) and the number of greedy layers actually executed is at most \(|E|\). Each deletion therefore makes at most \(|E|^2\) queries to \(M_0\), and at most \(|E|\) deletions give a safe cubic bound. Together with class computation, a safe oracle count is

\[
                         O(|E|^3+d|E|^2).
\tag{CK11}
\]

All large thresholds are tested using polynomial-bit integer arithmetic. If the threshold already exceeds the support count, no large sunflower or layer family is built. The original oracle IDs, tuple table, current ground, one recursion path, and one layer collection use polynomial space.

## 7. Graphic, cographic, and simple-partition consequences

For fixed \(d\), CK5 gives the following deterministic bounds.

| Additional matroids | Valid closure-class bound per matroid | Retained items |
|---|---:|---:|
| Simple partition matroids | \(g_i\le k\) | \(O_d(k^{2d+1})\) |
| Graphic matroids | \(g_i\le\binom{k+1}{2}\) | \(O_d(k^{3d+1})\) |
| Cographic matroids | \(g_i\le5k\) | \(O_d(k^{2d+1})\) |

Distinct feature tuples again remove one factor \(k\).

For a graphic matroid, an independent context is a forest. A spanned nonloop edge has its endpoints in one tree component. If the components contain \(r_1,\ldots,r_s\) forest edges, the number of spanned parallel classes is at most
\[
 \sum_j\binom{r_j+1}{2}
          \le\binom{1+\sum_jr_j}{2}
          \le\binom{k+1}{2}.
\tag{CK12}
\]
This safe elementary bound includes the one-edge case. Thus one arbitrary item matroid and \(d\) graphical interpretations of the same items admit the displayed kernel for selecting a common forest.

For cographic matroids, the public coverability proof gives a linear bound. A safe explicit constant follows by contracting original graph bridges, which deletes the corresponding cographic loops, and considering an independent deletion set \(I\). Contract the bridge-free components of the graph after deletion; the newly spanned edges form a tree of bridges in each original connected component. Every leaf of a nontrivial such tree is incident with a deleted edge, since otherwise its tree edge would already have been an original graph bridge. Mark the at-most-\(2|I|\) tree vertices incident with deleted edges and the at-most-\(2|I|\) branching vertices. Its maximal unmarked-internal paths number at most \(4|I|\); edges along each path are parallel in the original cographic matroid, because the path interior has no deleted-edge endpoint. Adding at most \(|I|\) classes for \(I\) itself gives \(5|I|\le5k\). Empty trees are handled directly. This yields a deterministic kernel for selecting deletable edges while preserving connectivity in each graphical interpretation, together with the arbitrary resource matroid.

The simple-partition case follows because an independent context occupies at most \(k\) parallel classes. Higher-capacity partition matroids are not automatically covered by this particular closure-class hypothesis; they are already covered directly by SK's sparse upper-packing theorem.

## 8. Public baseline and scope

Huang, Kakimura, Kobayashi and Terao, *Polynomial Kernels with Reachability for Weighted d-Matroid Intersection*, arXiv:2603.17345v1, Definition 2, introduces the \(g(k)\)-coverability condition used here. Its Theorem 2 gives a randomized reachable ground of size
\(\widetilde O(k\prod_i g_i(k))\). Lemmas 4–5 establish the graphic and cographic classes. Its deterministic Theorem 6 treats one arbitrary and one coverable matroid with size \(k^2(g(k)+1)\).

<https://arxiv.org/html/2603.17345v1>

The case \(d=1\) of CK5 has exactly that same deterministic size bound; it is not claimed as a new endpoint. With several additional matroids, the present reduction is deterministic but generally has a larger degree than the public randomized product bound. For example, with \(d\) graphic matroids the public randomized order is \(\widetilde O(k^{2d+1})\), whereas the deterministic bound here is \(O_d(k^{3d+1})\).

The greedy replacement, sunflower threshold, and layered bounded-conflict argument have the primary antecedents recorded in SK, including the greedy-layer kernel in Fomin–Golovach–Korhonen–Saurabh, SWAT 2024, Theorem 4. This note's proof composes those tools with the explicit parallel-class feature interface. No first-ever or size-optimality claim is made.

An arbitrary additional oracle matroid need not satisfy CK2 with any parameter-only bound. Uniform, transversal, and laminar classes require separate qualifications; their mere presence in the public broader paper does not justify applying this theorem to them. The additional resource conditions remain actual matroid independence, not an asserted integral intersection of all feature partitions. This remains a deterministic oracle ground reduction on selectable items.

