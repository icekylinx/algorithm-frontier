# Deterministic kernels with explicitly represented transversal matroids

**25 October 2026. Increment U. Complete manuscript-level proof with independent internal review.**

This note transfers the deterministic sparse-packing ground kernel of *deterministic_sparse_packing_oracle_kernel.md* (SK) to one arbitrary oracle matroid and several explicitly represented transversal matroids. The transfer preserves the strong replacement guarantee against every feasible context in the original ground.

The product-of-matching-witnesses reduction has a direct public antecedent in Huang–Kakimura–Kobayashi–Terao, Section 4. The additional implementation argument here first truncates every left neighborhood to the solution-size bound, and uses a return-the-whole-ground branch before forming the product. Consequently the construction is polynomial in the explicit input even when the number of transversal matroids is not a fixed constant.

## 1. Model and theorem

Let $E$ be an explicit item ground, $M_0$ an arbitrary matroid on $E$ supplied by an independence oracle, and $c_e\in\mathbb Q$ a possibly signed profit for each item. For $1\le i\le d$, a transversal matroid $M_i$ is supplied by an explicit bipartite graph

$$
G_i=(E,W_i;A_i).
\tag{TR1}
$$

A subset of $E$ is independent in $M_i$ exactly when it can be matched injectively into $W_i$. We seek solutions in

$$
\mathcal F=\{S\subseteq E:|S|\le k,\quad
                S\in\mathcal I(M_i)\text{ for }0\le i\le d\}.
\tag{TR2}
$$

Here $d$ counts the additional transversal matroids; the total number of matroids is $d+1$. The bipartite representations, rather than only independence oracles for these additional matroids, are part of the required input.

**Theorem.** A deterministic algorithm using polynomial time, a polynomial number of calls to the original $M_0$ oracle, and polynomial binary space returns $R\subseteq E$ with

$$
\begin{gathered}
 \forall S\in\mathcal F,\quad\forall e\in S,\quad
 \exists f\in R\setminus(S-e):\\
                    c_f\ge c_e,\qquad S-e+f\in\mathcal F.
 \end{gathered}
\tag{TR3}
$$

For $d\ge1$ and $k\ge1$, it satisfies

$$
|R|\le K(k,d):=
           k\,d!\,[\,k(d(k-1)+1)\,]^d.
\tag{TR4}
$$

Thus for each fixed $d$, the retained number of original items is
$O_d(k^{2d+1})$. Construction is uniformly polynomial in the full explicit input; this uniformity is stronger than allowing an input-size exponent depending on $d$.

The theorem preserves the maximum profit at every fixed cardinality at most $k$, including when some profits are negative. It also preserves exact feasibility at every such cardinality. Applying TR3 repeatedly replaces all elements of an original solution by distinct retained elements while never decreasing profit.

This is an **oracle ground kernel**. It does not compress an arbitrary program for $M_0$, or all rational profit bits, to a parameter-only number of bits. The additional bipartite representations can be reduced to at most $dk|R|$ incidences, as proved below.

## 2. Preliminary cases and deterministic neighborhood truncation

Delete every item that is a loop of $M_0$, or has no neighbor in at least one $G_i$. Such items occur in no original feasible set. Let $n$ be the number of remaining items, and replace $k$ by $\min\{k,n\}$. The feasible sets of interest are unchanged by these operations.

At $k=0$, return the empty ground. At $d=0$, one truncated weighted greedy scan in $M_0$ returns at most $k$ items with TR3, by the greedy lemma in SK. The case $k=1$ can alternatively be solved by retaining a maximum-profit individually feasible item. These scans continue through negative profits when a fixed cardinality is to be preserved.

For each remaining item $e$ and each $i$, fix an arbitrary deterministic subset

$$
N'_i(e)\subseteq N_i(e),\qquad
              |N'_i(e)|=\min\{k,|N_i(e)|\}.
\tag{TR5}
$$

Let $G'_i$ have these truncated neighborhoods.

**Truncation lemma.** For every $S\subseteq E$ with $|S|\le k$, the set $S$ has a matching into $W_i$ in $G_i$ if and only if it has one in $G'_i$.

One direction follows from $G'_i\subseteq G_i$. For the other, suppose $S$ has an original matching. By Hall's criterion, it suffices to verify

$$
\left|\bigcup_{e\in T}N'_i(e)\right|\ge|T|
                                  \quad\text{for every }T\subseteq S.
\tag{TR6}
$$

If $T$ contains any item with original degree at least $k$, that item's retained neighborhood already has $k\ge|T|$ distinct vertices, so TR6 holds. Otherwise every item's neighborhood in $T$ was left unchanged, and TR6 follows from the original matching. This proves the lemma simultaneously for all sets of size at most $k$; there is no guessed solution or randomized selection of neighbors.

In particular, after restricting to any returned ground $R$, the graphs $G'_i[R,W_i]$ still encode exactly the original independent sets on $R$ of size at most $k$. Delete isolated right vertices if desired. Their total edge count is at most

$$
dk|R|.
\tag{TR7}
$$

The cardinality limit remains part of the reduced instance: truncation is not asserted to preserve larger independent sets.

## 3. Avoiding a nonpolynomial witness product

Compute the integer $K=K(k,d)$ in TR4, or compare it with $n$ using capped integer arithmetic. If $n\le K$, return the entire remaining ground, together with the truncated bipartite representations. Property TR3 then holds by using $f=e$, and the size bound is immediate.

It remains to consider $n>K$. Since $d!\ge1$ and $d(k-1)+1\ge1$,

$$
K\ge k^{d+1},\qquad k^d<n.
\tag{TR8}
$$

Thus the following product, although exponential in $d$ as an unrestricted symbolic expression, has polynomial size in the branch where it is actually built:

$$
V=\{(e,r_1,\ldots,r_d): e\in E,\quad
                                  r_i\in N'_i(e)\text{ for every }i\}.
\tag{TR9}
$$

Writing $\pi(v)=e$ for the owner of a tuple gives

$$
|V|=\sum_{e\in E}\prod_{i=1}^d|N'_i(e)|
                         \le n k^d<n^2.
\tag{TR10}
$$

All tuples can therefore be enumerated explicitly using polynomial time and space, uniformly in the explicit integer $d$. Storing their coordinates costs a further factor polynomial in the explicit input. The bit length of the threshold is
$O(d\log(d+1)+d\log(k+1)+\log(k+1))$, or it can be capped as soon as it exceeds $n$.

This return-the-whole-ground branch is essential to the stated uniform implementation. It would not be justified to enumerate $n k^d$ tuples unconditionally and call that polynomial for variable $d$.

## 4. The parallel lift and packing constraints

Define a matroid $\widehat M_0$ on $V$ by

$$
T\in\mathcal I(\widehat M_0)
 \quad\Longleftrightarrow\quad
 |T|=|\pi(T)|\text{ and }\pi(T)\in\mathcal I(M_0).
\tag{TR11}
$$

This is the parallel extension of $M_0$ obtained by replacing each original item by its tuples. It is a matroid. For completeness, heredity is immediate. If $A,B$ satisfy TR11 and $|A|<|B|$, matroid augmentation in $M_0$ yields an owner in $\pi(B)\setminus\pi(A)$ extending $\pi(A)$; its unique tuple in $B$ augments $A$. One oracle call for $\widehat M_0$ is implemented by a distinct-owner check and at most one call to $M_0$.

For each pair $(i,r)$ with $r\in W_i$, impose the capacity-one packing row

$$
A_{i,r}=\{(e,r_1,\ldots,r_d)\in V:r_i=r\},
                        \qquad |T\cap A_{i,r}|\le1.
\tag{TR12}
$$

The row label includes $i$; equal names in different right domains are different rows. Every tuple lies in exactly $d$ rows. Give it profit $\widehat c_v=c_{\pi(v)}$, and retain the cardinality limit $k$.

The resulting instance is exactly an SK instance with one arbitrary resource matroid and column frequency $\delta=d$. It is also the intersection of $\widehat M_0$ with $d$ simple partition matroids, but the correctness proof does not rely on integrality of an intersection of three or more arbitrary matroids.

Apply SK to obtain $\widehat R\subseteq V$ of size at most $K(k,d)$ and with its full original-context replacement property. Return

$$
R=\pi(\widehat R).
\tag{TR13}
$$

Then $|R|\le|\widehat R|\le K(k,d)$.

## 5. Lifting solutions and projecting replacements

If $S\in\mathcal F$, choose a matching of $S$ into $W_i$ in each truncated graph $G'_i$; these exist by the truncation lemma. Combine the $d$ matching partners of each item into one tuple. The resulting $\widehat S\subseteq V$ has distinct owners and obeys every packing row in TR12, so it is feasible for the lifted SK instance. It has the same cardinality and profit as $S$.

Conversely, any lifted feasible set has distinct owners by TR11. For each $i$, its $i$-th coordinates give a matching of those owners in $G'_i$, by TR12. Its projection is therefore in $\mathcal F$, with the same cardinality and profit.

To prove the stronger TR3 rather than only preservation of an optimum, fix an arbitrary original $S\in\mathcal F$ and $e\in S$. Lift the entire $S$ using any of its truncated matching witnesses, and let $v_e$ be the tuple owned by $e$. The SK guarantee gives

$$
\widehat f\in\widehat R\setminus(\widehat S-v_e),\qquad
 \widehat c_{\widehat f}\ge\widehat c_{v_e},\qquad
             \widehat S-v_e+\widehat f\text{ is lifted-feasible}.
\tag{TR14}
$$

Set $f=\pi(\widehat f)$. The distinct-owner condition in TR11 forces
$f\notin S-e$, even when many tuples have the same owner. The lifted row conditions provide valid matchings after the replacement, while TR11 preserves the original resource independence. Thus

$$
c_f\ge c_e,\qquad S-e+f\in\mathcal F,
\tag{TR15}
$$

which proves TR3. The context $S-e$ is an arbitrary original context and need not be contained in $R$. If $f=e$, the conclusion is also valid, and means that another retained tuple has represented the same original item.

## 6. Complexity and useful interpretations

All preliminary operations are polynomial in the explicit bipartite graphs and rational input encoding. In the nontrivial branch, $|V|<n^2$. SK uses a safe cubic number of lifted independence queries, so a coarse bound for the original resource queries is

$$
O(n^6+n),
\tag{TR16}
$$

plus polynomial tuple processing; no effort is made to optimize this exponent. The exponent in this preprocessing bound is independent of $d$. All threshold tests, stored tuples, greedy layers, and set-family scans use polynomial binary space.

For example, suppose a selected collection of items must be assignable injectively to eligible resources in each of several different bipartite systems, and must also be independent in an arbitrary resource matroid. The theorem retains $O_d(k^{2d+1})$ original items while preserving the exact best signed profit at every selected cardinality at most $k$. Each assignment system in the returned instance needs only $k$ retained eligibility edges per retained item.

The theorem does not apply to an additional matroid merely because it is known abstractly to be transversal: the explicit bipartite representation is used to truncate and enumerate witnesses. It makes no claim that every laminar matroid has the representation required here. All original matroid and cardinality conditions remain part of the reduced problem.

## 7. Primary baseline and status of the increment

Huang, Kakimura, Kobayashi and Terao, *Polynomial Kernels with Reachability for Weighted d-Matroid Intersection*, arXiv:2603.17345v1, Theorem 3 and Section 4, gives a randomized reachable ground of size $\widetilde O(k^{d+1})$ when translated into this note's convention of $d$ additional transversal matroids. Its Section 4 lifts matching witnesses into a tuple ground with a parallel extension of the arbitrary resource matroid and simple partition constraints, then projects a kernel back to original items.

<https://arxiv.org/html/2603.17345v1>

That lift is an established ingredient, not a novelty claim of this note. The present deterministic consequence follows from SK, with the larger bound $O_d(k^{2d+1})$. The neighborhood truncation and size-threshold branch above make the explicit implementation uniform in $d$. This is a proved deterministic alternative with a larger output-size degree than the cited randomized construction; no first-ever or optimality assertion is made.

Dependencies: SK for deterministic sunflower thinning and the external-context greedy property; Hall's marriage criterion for TR6; ordinary matroid augmentation for TR11. The complete manuscript has undergone independent internal review, not formal verification or external peer review.
