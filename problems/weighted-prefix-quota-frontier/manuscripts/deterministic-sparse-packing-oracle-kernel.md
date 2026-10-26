# Deterministic sparse packing kernels with an oracle matroid

**25 October 2026. Increment U. Complete manuscript-level proof with independent internal review.**

This note gives a deterministic polynomial-time reduction for item-set packing with one arbitrary independence-oracle matroid and sparse zero-one upper constraints. It retains a polynomial number of items when the column frequency is fixed, and has a strong replacement guarantee against every feasible context in the **original** instance.

The proof combines two established tools: the weighted one-matroid greedy replacement lemma and the constructive Erdős–Rado sunflower lemma. The key composition is a deletion rule using several disjoint greedy layers of one sunflower. It does not require linear matroid representations, randomized kernels, or a claim that three matroid intersections are integral.

“Kernel” below means an **oracle ground kernel**: a retained subset of original items with the original resource oracle and item weights still available. It is not a claim that arbitrary oracle descriptions or arbitrary rational weights have been compressed to a parameter-only number of bits.

## 1. Model and main theorem

Let $`E`$ be an explicit set of $`n`$ selectable items, and let $`M=(E,\mathcal I)`$ be one arbitrary matroid supplied by an independence oracle. Let $`c:E\to\mathbb Q`$ be rational item profits. Nonnegative profits suffice for the usual maximization problem; the proof also permits signed profits, with greedy scans continuing through negative items.

The explicitly supplied packing rows are sets $`A_j\subseteq E`$ with nonnegative integer capacities $`b_j`$. Feasible solutions satisfy

```math
S\in\mathcal I,\qquad |S|\le k,\qquad
                 |S\cap A_j|\le b_j\quad\text{for every }j.
\tag{SK1}
```

The resource is a matroid **on the selectable items**. For graph applications, it is a matroid on edges, not a matroid on their endpoint union.

Write $`\sigma(e)=\{j:e\in A_j\}`$ for an item's row support, and let

```math
\delta=\max_{e\in E}|\sigma(e)|.
\tag{SK2}
```

All rows may overlap arbitrarily; their capacities need not be one. The integer $`k`$ is an explicit cardinality limit, or a valid bound on the solution sizes of interest. Replace $`k`$ by $`\min\{k,n\}`$ without loss.

Let $`\mathcal F`$ denote the feasible family in SK1. A retained set $`R\subseteq E`$ has the deterministic single-replacement property if

```math
\begin{gathered}
 \text{for every }S\in\mathcal F\text{ and }e\in S,\text{ some }
 f\in R\setminus(S-e)\text{ satisfies}\\
             c_f\ge c_e,\qquad S-e+f\in\mathcal F.
 \end{gathered}
\tag{SK3}
```

**Theorem.** A set $`R`$ satisfying SK3 can be found in deterministic polynomial time and polynomial binary space. If $`k\ge1,\delta\ge1`$, one may guarantee

```math
|R|\le
 k\,\delta!\,[\,k(\delta(k-1)+1)\,]^\delta
                =(\delta k+2)^{O(\delta)}.
\tag{SK4}
```

For fixed $`\delta`$, this is $`O_\delta(k^{2\delta+1})`$. If the original real supports are pairwise distinct, the leading factor $`k`$ can be omitted:

```math
|R|\le\delta!\,[\,k(\delta(k-1)+1)\,]^\delta
                         =O_\delta(k^{2\delta}).
\tag{SK5}
```

At $`k=0`$, return the empty set. At $`\delta=0`$, one truncated greedy scan returns at most $`k`$ items with SK3. The case $`k=1`$ can also be solved directly by retaining a maximum-profit individually feasible item, or no item if none exists.

The polynomial construction time is uniform when the explicit frequency $`\delta`$ is part of the input. Only the output-size bound has exponent depending on $`\delta`$. The proof below gives a safe $`O(n^3+n)`$ independence-oracle query bound, in addition to polynomial explicit-set processing; no effort is made to optimize this implementation constant.

**Capacity-sensitive refinement.** If $`h`$ is any computable upper bound on
the number of packing rows saturated by a feasible context of at most
$`k-1`$ items, replace $`\delta(k-1)+1`$ in SK4--SK5 by $`h+1`$.
One can take $`h`$ to be the floor of the sum of the largest $`k-1`$ item
loads $`\sum_{j\in\sigma(e)}1/b_j`$, clipped to the number of rows, after
zero-capacity preparation. Section 6 only uses the number of saturated
rows, so its proof applies with exactly $`h+1`$ layers. The explicit load
proof appears in [the sharp FPT restriction](sharp-sparse-packing-fpt-restrictions.md#3-saturated-row-accounting-and-the-replacement-proof).

That companion also proves the different deterministic tradeoff
$`k\binom{\delta k}{\delta}=O_\delta(k^{\delta+1})`$ retained items for
unweighted original-context replacement, with
$`2^{O(\delta k\log(\delta k+2))}n^{O(1)}`$ preprocessing. An ordered
failure-summary variant gives at most $`e^\delta k^{\delta+1}`$ items
for arbitrary signed profits with the same FPT parameter dependence.
The exponential construction time keeps both variants distinct from the
uniformly polynomial arbitrary-profit theorem here.

## 2. Original-context replacement and composition

It is useful to state the local invariant before giving the reduction. For a current candidate set $`T\subseteq E`$, a reduction $`T\mapsto R_T\subseteq T`$ has the external-context property if

```math
\begin{gathered}
 \forall S\in\mathcal F,\ \forall e\in S\cap T,\quad
 \exists f\in R_T\setminus(S-e):\\
                   c_f\ge c_e,\quad S-e+f\in\mathcal F.
 \end{gathered}
\tag{SK6}
```

The context $`S-e`$ need not be contained in $`T`$. Both $`\mathcal F`$ and $`M`$ in this statement refer to the original instance.

These reductions compose. Fix an original feasible $`S`$ and $`e\in S`$, and set $`I=S-e`$. Suppose the current representative is $`e_i\in T_i`$, with $`I+e_i`$ feasible and $`c_{e_i}\ge c_e`$. Applying SK6 to $`I+e_i`$ yields $`e_{i+1}\in T_{i+1}\setminus I`$, with $`I+e_{i+1}`$ feasible and no smaller profit. The context $`I`$ stays exactly the same throughout. Thus the final retained ground satisfies SK3.

This is stronger than proving that every reduction preserves an optimum whose entire set lies in its current ground. That weaker assertion would not justify the external-context invariant used here.

## 3. The weighted greedy replacement lemma

For $`Y\subseteq E`$, let $`\mathrm{Greedy}(M,Y,k)`$ scan $`Y`$ in nonincreasing profit order, with fixed deterministic ties, adding an item when matroid independence is maintained and fewer than $`k`$ items have been retained.

**Greedy lemma.** If $`S\in\mathcal I`$, $`|S|\le k`$, and $`e\in S\cap Y`$, then this scan returns an $`f\notin S-e`$ with

```math
c_f\ge c_e,\qquad S-e+f\in\mathcal I.
\tag{SK7}
```

Here $`S-e`$ can contain items outside $`Y`$.

To prove it, let $`I=S-e`$, which has size at most $`k-1`$. If $`e`$ is retained, use $`f=e`$. If the scan has already retained $`k`$ items by the time it reaches $`e`$, these items form an independent set of rank $`k>|I|`$, so some retained item is outside $`\mathrm{cl}_M(I)`$. All were processed no later than $`e`$, and have profit at least $`c_e`$.

Otherwise the greedy prefix has fewer than $`k`$ retained items and rejected $`e`$ because that prefix spans $`e`$. Since $`e\notin\mathrm{cl}_M(I)`$, at least one member of the prefix lies outside $`\mathrm{cl}_M(I)`$; use it as $`f`$. Again its profit is at least $`c_e`$. In both cases an item outside the closure is outside $`I`$ and extends it independently.

This is the same one-matroid property stated as Lemma 2 in Huang, Kakimura, Kobayashi and Terao, *Polynomial Kernels with Reachability for Weighted d-Matroid Intersection* (2026). The proof above records the exact external-context quantifier required here. No packing feasibility is imposed on the greedy pool itself.

## 4. Preparation and duplicate supports

Remove matroid loops and items in any zero-capacity row. Such items appear in no feasible original solution, so this is safe even for SK6. Discard the resulting zero-capacity rows: neither an original feasible context nor any surviving candidate can use their removed items. Every remaining packing capacity is then at least one. Capacities at least $`k`$ may be discarded as redundant, or kept; either choice is safe. Support labels below always refer to the chosen fixed original row system.

For each class of items with the same **real row support**, retain only

```math
\mathrm{Greedy}(M,\text{class},k).
\tag{SK8}
```

There are at most $`k`$ retained items per support. This simultaneous reduction has SK6: for any protected $`e`$, the greedy lemma supplies a no-worse independent replacement in its own support class; identical supports preserve every packing row exactly. A replacement is outside the unchanged context.

Subsequent steps only delete items, so the at-most-$`k`$-per-support invariant remains true. It is not necessary to collapse these classes again after each deletion.

## 5. Constructive sunflowers on distinct supports

Set

```math
t=\delta(k-1)+1,\qquad L=kt+1.
\tag{SK9}
```

We will use a sunflower of $`L`$ **distinct** supports. Distinctness is not replaced by a count of items: many items may share one support.

For supports of size at most $`\delta`$, pad each distinct support to size exactly $`\delta`$ with private labels assigned to that support. A padding label is not a packing row and belongs to only that one padded support. This is an explicit construction of at most $`\delta`$ labels per support.

If the number of distinct padded supports exceeds

```math
\delta!(L-1)^\delta,
\tag{SK10}
```

the constructive Erdős–Rado lemma finds $`L`$ of them with a common intersection core and pairwise disjoint petals.

For completeness, the standard induction is algorithmic. On a family of distinct $`r`$-sets exceeding $`r!(L-1)^r`$, greedily find a maximal disjoint subfamily. If it has at least $`L`$ members, they form a sunflower with empty core. Otherwise its union has at most $`r(L-1)`$ labels and meets every set. Some label occurs in more than
```math
\frac{r!(L-1)^r}{r(L-1)}
                   =(r-1)!(L-1)^{r-1}
```
sets. Restrict to the sets containing it, delete that label, and recurse. The remaining sets stay distinct. Reinsert the label into the core of the returned flower. The singleton base case is immediate.

The recursion follows one popular-label branch, has depth at most $`r`$, and uses only polynomial-time scans of the explicit set family. It is polynomial also when $`\delta`$ is part of the input. The threshold can be computed or compared using $`O(\delta\log(\delta+1)+\delta\log(L+1))`$ bits.

Since $`L\ge2`$, no private padding label lies in the common core. On removing padding, the selected real supports have the same real core and disjoint real petals. Empty real petals cause no problem; distinct real supports allow at most one such petal.

## 6. Sunflower deletion by disjoint greedy layers

Choose one currently surviving item for each of the $`L`$ distinct supports of a found sunflower. Let $`V`$ be these $`L`$ chosen items, with real core $`C`$. Other items with the same supports are not included in this particular choice.

Construct $`t`$ disjoint greedy layers:

```math
\begin{split}
 V_1&=V,\\
 F_i&=\mathrm{Greedy}(M,V_i,k),\\
 V_{i+1}&=V_i\setminus F_i\qquad(1\le i\le t).
 \end{split}
\tag{SK11}
```

Let $`R_V=\bigcup_{i=1}^tF_i`$. It has size at most $`kt=L-1`$. Delete precisely the chosen items in $`V\setminus R_V`$, retaining $`R_V`$ and all current items outside $`V`$. At least one item is deleted.

**Deletion lemma.** This reduction satisfies SK6.

Let $`e`$ be a deleted item and fix any original feasible $`S`$ containing it. Put $`I=S-e`$. Since $`e`$ is in none of the layers, it remains available in every pool $`V_i`$. The greedy lemma gives, for each $`i`$, an item $`f_i\in F_i\setminus I`$ with
```math
c_{f_i}\ge c_e,\qquad I+f_i\in\mathcal I.
\tag{SK12}
```
The $`f_i`$ are distinct because the layers are disjoint. They come from distinct supports and therefore from distinct petals of the chosen flower.

A row $`j`$ can block adding an item to $`I`$ only if it is saturated there, $`|I\cap A_j|=b_j`$. Capacities are positive after preparation, so every such row contains some item of $`I`$. There are at most
```math
\delta|I|\le\delta(k-1)
\tag{SK13}
```
saturated rows, since each context item belongs to at most $`\delta`$ rows.

A saturated row cannot contain $`e`$, because $`I+e=S`$ was feasible. In particular no saturated row belongs to the flower core, which is contained in the support of $`e`$. Each saturated row therefore lies in at most one flower petal and can obstruct at most one of the distinct candidates $`f_i`$. There are $`t=\delta(k-1)+1`$ candidates and at most $`t-1`$ blocking rows. At least one $`f_i`$ violates no packing row.

That item has the required independent extension, cardinality, and profit. It lies in the retained $`R_V`$. Items not deleted can represent themselves, proving SK6 for the entire reduction.

The proof is unaffected by items of $`I`$ outside the current ground. They are counted in the original saturated rows, and the bound SK13 uses only their original frequency. It also does not require the greedy layers to be packing-feasible.

## 7. Algorithm, termination, and ground size

After the support collapse of Section 4, repeat:

- If the number of distinct real supports is at most SK10, stop.
- Otherwise construct a padded sunflower, choose one item per selected support, and perform Section 6's deletion.

Every iteration removes at least one current item. A support need not disappear in that iteration: other items of that support may remain. This does not affect termination, because the total number of items strictly decreases. There are at most $`n`$ deletion iterations.

At termination there are at most $`\delta!(L-1)^\delta`$ supports, each with at most $`k`$ retained items. Substituting $`L-1=k(\delta(k-1)+1)`$ gives SK4. If supports were pairwise distinct initially, deletion preserves that property and gives SK5.

Every deletion and the initial support collapse have the external-context property. Section 2's fixed-context composition therefore proves the final SK3, not merely preservation of an optimum.

If the explicit sunflower threshold is already at least the current support count, no flower search is attempted. All numerical comparison and factorial/product calculations have polynomial bit length.

## 8. Deterministic polynomial construction and space

Initial loop tests and support-class greedy scans use $`O(n)`$ independence queries. Rational profit comparisons are exact, and one global sorted order with fixed ties can be used in every later scan.

Whenever a sunflower deletion is invoked, its $`L`$ distinct supports belong to the current ground, so $`L\le n`$. Consequently $`t\le L\le n`$. Each greedy layer scans at most $`L`$ items and uses at most that many independence queries. A deletion costs at most $`tL\le n^2`$ queries, and at most $`n`$ deletions give the stated $`O(n^3+n)`$ bound.

The constructive sunflower routine uses at most $`\delta`$ levels and polynomial explicit set operations per level. It follows only one recursive subfamily. This is uniform polynomial computation in the explicit input; it is not an $`n^\delta`$ search over support tuples.

The current item set, its support table, padding labels, one recursive sunflower state, and the greedy layers all fit polynomial input space. There is no natural-matroid unit expansion or binary capacity expansion. The outputs retain original item identities and profits, and the resource oracle is still the original matroid restricted to those identities.

If desired, discard empty rows in the final restricted instance. At most $`\delta|R|`$ rows have a retained incidence. Capacities may be clipped to $`k`$. These facts bound the combinatorial support size, but not arbitrary original profit encodings or an oracle's program description. No classical parameter-only bit kernel is claimed.

## 9. Reachability and exact optimization consequences

SK3 gives deterministic element-by-element reachability. Given an original feasible
$`S=\{e_1,\ldots,e_s\}`$, process the original elements in that order. If the current set already contains $`e_i`$ in the retained ground, it can be kept; otherwise apply SK3 to replace it by a retained item of no smaller profit, outside all other current items. The resulting set remains feasible and has the same cardinality at every step. After at most $`s`$ proper replacements the entire set lies in $`R`$.

In particular, restricting to $`R`$ preserves maximum additive profit for every fixed cardinality up to $`k`$, and therefore for the size-at-most-$`k`$ optimization problem. Signed profits cause no difficulty, because no greedy layer was allowed to stop merely on reaching a negative profit.

Enumerating subsets of $`R`$ of size at most $`k`$ gives the standard exact time consequence
```math
2^{O(\delta k\log(\delta k+2))}
                         \mathrm{poly}(H).
\tag{SK14}
```
The exact FPT order itself is not the new comparison claimed here: sparse item-set packing already permits direct coloring/profile deductions. The stronger result of this note is the deterministic polynomial-time ground reduction with SK3.

The external-context statement also permits composing reductions of different candidate pools while retaining the original resource and row system. Any streaming or distributed use must maintain this original-context interpretation; no claim follows from restricting away the external context in the proof.

## 10. Concrete specializations

**One arbitrary matroid and several explicit partition matroids.** Suppose there are $`d-1`$ additional partition matroids, with arbitrary nonnegative integer capacities in their parts. Use one packing row per part, labelled by its partition. Each item occurs in at most $`d-1`$ rows. For fixed $`d\ge2`$, SK4 gives a deterministic reachable oracle ground of size
```math
O_d(k^{2d-1}).
\tag{SK15}
```
No simple-capacity-one assumption is required. If all part-incidence vectors are distinct, SK5 improves the exponent by one.

**Graph matching with a matroid on edges.** Give each vertex a capacity-one row and each edge its two endpoint incidences. For a loopless simple graph, supports are distinct and $`\delta=2`$, so
```math
|R|\le2[\,k(2k-1)\,]^2=O(k^4)
\tag{SK16}
```
edges suffice deterministically. This holds in nonbipartite graphs as well. With parallel edges, support collapse gives the general $`O(k^5)`$ edge bound. Vertex capacities above one give the corresponding edge-matroid-constrained $`b`$-matching ground reduction.

**Hyperedge selection with item independence.** A selectable hyperedge of size at most $`\delta`$ supplies the support of one item, and vertex capacities give the packing rows. SK4 applies to repeated hyperedge records and SK5 to distinct supports. The matroid is on hyperedge records. A matroid on the union of selected vertices is a different model and is not asserted.

## 11. Primary comparisons and attribution

The following primary statements were checked directly on 25 October 2026. They delimit the contribution and do not establish a publication-priority claim.

Huang, Kakimura, Kobayashi and Terao, *Polynomial Kernels with Reachability for Weighted d-Matroid Intersection*, arXiv:2603.17345v1, explicitly defines deterministic single exchangeability in Section 7. Its Lemma 2 is the greedy replacement lemma used here. Its Theorem 1 gives a randomized reachable ground of size $`\widetilde O(k^d)`$ for one arbitrary matroid and $`d-1`$ simple partition matroids; Corollary 2, via the transversal-matroid theorem, extends that same randomized size to arbitrary partition capacities. Theorem 5 gives $`\widetilde O(k^3)`$ for matching with an edge matroid. Theorem 6 is a deterministic result for two matroids, one $`g(k)`$-coverable. The current abstract page lists only that March 2026 version.

<https://arxiv.org/html/2603.17345v1>

<https://arxiv.org/abs/2603.17345>

The present reduction has a larger polynomial degree than those randomized bounds in their overlapping cases. Its guarantee is deterministic and applies to arbitrary sparse zero-one upper packing, including nonunit capacities. It does not claim to match the public size optimum or to improve the public theorem's broader graphic, cographic, or transversal cases.

Huang and Ward, *FPT-Algorithms for the ell-Matchoid Problem with a Coverage Objective*, already give deterministic representative kernels for general oracle matchoids. Their Theorems 3.6–3.7 provide the representative/kernel interface, with size exponential in the solution parameter for a fixed nontrivial matchoid frequency. The sparse uniform-row specialization here obtains a polynomial-size ground by a different deletion rule; the general matchoid problem is not claimed solved by this note.

<https://www.di.ens.fr/~cchuang/work/matchoid.pdf>

Disjoint greedy layers followed by a bounded-conflict pigeonhole argument also have a direct antecedent. Fomin, Golovach, Korhonen and Saurabh, *Stability in Graphs with Matroid Constraints*, SWAT 2024, Theorem 4, construct $`kD`$ disjoint greedy independent layers for a graph of maximum degree $`D`$, giving at most $`k^2D`$ retained vertices. Their proof obtains one resource-valid candidate from each layer and bounds the candidates obstructed by the remaining context. Section 6 uses this established mechanism inside a sunflower, where disjoint petals give the conflict bound despite an unbounded global conflict degree.

<https://drops.dagstuhl.de/storage/00lipics/lipics-vol294-swat2024/LIPIcs.SWAT.2024.22/LIPIcs.SWAT.2024.22.pdf>

The constructive support threshold is the classical Erdős–Rado sunflower bound. Their *Intersection Theorems for Systems of Sets*, Journal of the London Mathematical Society 35 (1960), pages 85–90, is available from the authors' institutional archive. Section 5 supplies the standard explicit induction so that no sunflower algorithm is hidden as an extra assumption.

<https://www.renyi.hu/~p_erdos/1960-04.pdf>

These comparisons support a concrete distinction: deterministic ground reduction with external-context reachability, at the displayed larger polynomial degree. They are not evidence for a first-ever deterministic kernel claim.

## 12. Limits of the theorem

The rows are zero-one **upper** packing rows. Arbitrary row-dependent integer coefficients, cover targets, and equality targets belong to the separate BF/HP exact-target theorems and do not inherit this polynomial kernel automatically. Same-support replacement would not preserve different numeric coefficients.

Only one arbitrary oracle matroid is imposed on the selectable items. The sunflower is formed on explicit row-ID supports, not on arbitrary matroid elements or vertex unions; no sunflower theorem for arbitrary matroids is assumed. A second unrelated arbitrary oracle matroid is outside the proof.

The retained ground may still have polynomial size larger than the input, in which case the algorithm simply returns the smaller current set. Numerical profits and the original oracle remain available. The theorem is therefore an oracle ground-kernel statement in the same sense as the cited reachable-kernel literature, not a compression of all input bits.
