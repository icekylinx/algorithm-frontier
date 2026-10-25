# Sharp root-target lower bounds with disjoint weighted quota rows

**25 October 2026. Increment U. Complete manuscript-level proof with independent internal review.** It sharpens the constant-frequency endpoint of the sparse theorem to one nonroot row per coordinate. The hidden sparse-paving / SAT-decoder mechanism has public antecedents cited below; no priority claim is made for that mechanism.

## 1. Statement

Even with all of the following restrictions, exact feasibility requires
\[
2^{\Omega(B\log(B+2))}
\]
rank-oracle queries in the worst case:

- the resource is one ordinary matroid;
- the root row has unit weights and cap \(B_0\);
- every other quota row is an equality, the rows have disjoint supports, and each coordinate occurs in exactly one of them;
- coefficients and targets are nonnegative integers at most \(B\), with \(B=B_0+1\);
- there are no zero-root coordinates and the scalar objective is identically zero.

The result holds for mandatory bases and for optional independent sets. No objective or extra cardinality equality is needed in the optional case. The column frequency \(\Delta=1\) counts an original equality as one row; splitting equalities into upper and lower inequalities doubles it to two and leaves the conclusion unchanged.

The same family has polynomially encoded, polynomial-time evaluable rank programs. Under deterministic ETH there is no deterministic
\[
2^{o(B\log(B+2))}\operatorname{poly}(H)
\]
algorithm on that promised representation class. Randomized ETH is required separately for the corresponding randomized statement.

## 2. Explicit disjoint-row instance

Let \(d\ge2\) be an integer and put \(k=2d\). The ground set is
\[
E=\{(j,i):j\in[d],\ i\in[k]\}.
\]
Thus \(|E|=dk=2d^2\). The root inequality is
\[
\sum_{e\in E}x_e\le k.                                           \tag{DR1}
\]
For every block \(j\), impose
\[
\sum_{i=1}^{k} i\,x_{j,i}=k+1.                                  \tag{DR2}
\]
These \(d\) nonroot rows are disjoint. Every column has root weight one and exactly one nonroot incidence. The maximum target is \(B=k+1\), while \(B_0=k\).

For each \(j\), the \(d\) complementary pairs are
\[
P_{j,t}=\{(j,t),(j,k+1-t)\},\qquad t\in[d].
\]
Let
\[
\mathcal H=
\left\{\bigcup_{j=1}^{d}P_{j,t_j}:
                     (t_1,\ldots,t_d)\in[d]^d\right\}.           \tag{DR3}
\]
Then
\[
|\mathcal H|=d^d=(k/2)^{k/2}.                                   \tag{DR4}
\]

Any ordinary-matroid independent-set incidence vector satisfying DR1–DR2 uses at least two elements in each block, since one coefficient is at most \(k<k+1\). There are \(d\) blocks and the root cap is \(2d\), so it uses exactly two per block and exactly \(k\) elements overall. Equality DR2 makes those two coefficients complementary. Consequently the sets satisfying the numeric rows are **exactly** \(\mathcal H\), whether the resource domain is a base or an optional independent set.

This argument uses the equality in DR2. Replacing it only by a covering inequality could admit overshooting pairs; no such pure-cover claim is made.

## 3. The resource is a valid sparse-paving matroid

Distinct members of \(\mathcal H\) cannot differ by one exchange. Indeed, a cross-block exchange changes a positive block sum, and an exchange within one block changes its sum because all its coefficients are distinct. Equivalently,
\[
A,A'\in\mathcal H,\ A\ne A'
 \quad\Longrightarrow\quad |A\cap A'|\le k-2.                    \tag{DR5}
\]

For an arbitrary subfamily \(\mathcal G\subseteq\mathcal H\), define allowed bases to be
\[
\mathcal B_{\mathcal G}
 =\{S\subseteq E:|S|=k,\ S\notin\mathcal H\setminus\mathcal G\}.
                                                                    \tag{DR6}
\]
These are the bases of a rank-\(k\) matroid \(M_{\mathcal G}\).

Here is a direct verification. For allowed bases \(X,Y\) and \(e\in X\setminus Y\), if \(|Y\setminus X|=1\), the only exchange produces \(Y\), which is allowed. Otherwise there are at least two candidates \(X-e+f\), \(f\in Y\setminus X\). Any two share \(k-1\) elements, so by DR5 at most one is forbidden. A valid exchange therefore exists. There are allowed \(k\)-sets, and every set of size less than \(k\) extends to one: for a \((k-1)\)-set, among its at least two one-element extensions at most one is forbidden; smaller sets first extend arbitrarily to size \(k-1\).

Its full rank function, for every query size, is
\[
r_{\mathcal G}(S)=
\begin{cases}
 |S|,&|S|<k,\\
 k-1,&|S|=k,\ S\in\mathcal H\setminus\mathcal G,\\
 k,&\text{otherwise}.
\end{cases}                                                     \tag{DR7}
\]
For \(|S|>k\), an arbitrary \((k+1)\)-subset contains several mutually adjacent \(k\)-subsets, at most one forbidden; hence its rank is \(k\), as asserted.

Since ordinary matroid singleton ranks are at most one, all integer resource vectors are zero-one. Combining Section 2 with DR6 gives
\[
\text{numeric-resource feasibility}\quad\Longleftrightarrow\quad
\mathcal G\ne\varnothing.                                      \tag{DR8}
\]

## 4. Oracle lower bound

Take the reference \(\mathcal G=\varnothing\), and for every \(A\in\mathcal H\) the hidden instance \(\mathcal G=\{A\}\). The two rank oracles differ on exactly the set \(A\), and on no other subset of \(E\).

A deterministic decision algorithm must query every member of \(\mathcal H\) along the reference transcript to certify infeasibility. On the promise that one hidden feasible set exists, an algorithm finding a feasible set requires at least \(|\mathcal H|-1\) queries in the worst case.

For a bounded-error decision algorithm, consider the distribution that is reference with probability \(1/2\), and otherwise has a uniformly random hidden \(A\). With at most \(Q\) queries, a deterministic algorithm encounters that distinguished set with probability at most \(Q/|\mathcal H|\) on the hidden half. Its average success is therefore at most
\[
\frac12+\frac{Q}{2|\mathcal H|}.
\]
Yao's principle yields \(Q\ge|\mathcal H|/3\) for worst-case success at least \(2/3\). Thus the oracle lower is
\[
|\mathcal H|=2^{d\log_2 d}
            =2^{\Omega(B\log(B+2))}.                            \tag{DR9}
\]

All explicit row data have size polynomial in \(B\). For arbitrary sufficiently large budget upper bounds \(b\), choose the largest even \(k\le b-1\); the same construction has \(B\le b\) and exponent \(\Omega(b\log b)\). This is a worst-case statement over instances bounded by \(b\), not a requirement that every input have that complexity.

## 5. A readable rank program and ETH calibration

Let \(\varphi\) be a 3-CNF formula with \(\nu\) variables. Choose the least \(d\ge2\) for which
\[
d^d\ge2^\nu.                                                    \tag{DR10}
\]
Set \(k=2d\) and construct DR1–DR2.

Rank a tuple \((t_1,\ldots,t_d)\in[d]^d\) lexicographically using
\[
J(t_1,\ldots,t_d)
 =\sum_{j=1}^{d}(t_j-1)d^{d-j}\in[0,d^d-1].                     \tag{DR11}
\]
Define \(\mathcal G_\varphi\subseteq\mathcal H\) by admitting its tuple if
\(J<2^\nu\) and the \(\nu\)-bit binary expansion of \(J\) satisfies \(\varphi\). Every \(\nu\)-bit assignment occurs among these ranks. Therefore
\[
\mathcal G_\varphi\ne\varnothing
       \quad\Longleftrightarrow\quad \varphi\text{ is satisfiable}. \tag{DR12}
\]

The rank program evaluates DR7. For a queried \(k\)-set, it recognizes membership in \(\mathcal H\) by checking the two complementary elements of each block. On such a set it computes DR11 and evaluates \(\varphi\); on all other query sizes or nonmembers of \(\mathcal H\), DR7 has an immediate answer. Each operation takes time polynomial in the input and formula length. The program always describes a matroid because Section 3 applies to every subfamily \(\mathcal G_\varphi\). Its computation can also be unrolled to a polynomial-size Boolean rank circuit, with the formula included in the representation.

Minimality gives, for \(d>2\),
\[
(d-1)\log_2(d-1)<\nu\le d\log_2 d.
\]
Furthermore
\[
\frac{d^d}{(d-1)^{d-1}}
 =d\left(1+\frac1{d-1}\right)^{d-1}\le ed,
\]
so
\[
\nu\le d\log_2 d<\nu+\log_2(ed).
\]
The finitely many small \(\nu\) are harmless. In particular
\[
B\log(B+2)=\Theta(\nu),\qquad d=O(\nu),                           \tag{DR13}
\]
and the complete encoded target/resource instance has size polynomial in \(|\varphi|+\nu\).

A deterministic \(2^{o(B\log B)}\operatorname{poly}(H)\) algorithm for this encoded problem would decide 3-SAT in \(2^{o(\nu)}\operatorname{poly}(|\varphi|)\) time, contradicting deterministic ETH. The corresponding randomized conclusion requires randomized ETH, not deterministic ETH alone.

## 6. Relation to the upper bound and source credit

For fixed \(\Delta=1\), the direct sparse algorithm's bound
\[
2^{O(B\log(B+2))}\operatorname{poly}(H)
\]
has the correct exponent order in the oracle model, even though all nonroot rows have disjoint supports. The numeric coefficients create the obstruction; the lower should not be interpreted as a lower for the unit-coefficient disjoint-partition case, which has a different structure.

The construction is a disjoint-block specialization of the hidden exact-sum / sparse-paving technique used in earlier working notes. The public antecedents are substantive:

- Fomin, Golovach, Korhonen and Saurabh, [*Stability in Graphs with Matroid Constraints*, SWAT 2024](https://drops.dagstuhl.de/storage/00lipics/lipics-vol294-swat2024/LIPIcs.SWAT.2024.22/LIPIcs.SWAT.2024.22.pdf), Theorem 2, use a product of complement-pair choices in disjoint graph blocks and hide one rank-\(2p\) stable set among \(q^p\) candidates. Their underlying hidden family is precisely the pair-product family used here when \(p=q=d\). The present numeric rows encode those choices by disjoint weighted equalities and calibrate the root and maximum target.
- Doron-Arad, Kulik and Shachnai, [*Lower Bounds for Matroid Optimization Problems with a Linear Constraint*, arXiv:2307.07773v2](https://arxiv.org/html/2307.07773v2), develops exact-sum hidden families and, in Definitions 4.4–4.5 and Lemma 4.6, polynomially encoded SAT-matroid decoders.
- Their [*You (Almost) Can't Beat Brute Force for 3-Matroid Intersection*, arXiv:2412.02217v2](https://arxiv.org/html/2412.02217v2), Section 3, gives the general G-matroid margin construction.
- The ETH convention and sparsification framework are from Impagliazzo, Paturi and Zane, [*Which Problems Have Strongly Exponential Complexity?*, JCSS 63 (2001)](https://courses.cs.washington.edu/courses/cse599i/24sp/papers/ImpagliazzoPaturiZane_2001_jcss.pdf).

The new statement here is the explicit \(\Delta=1\), root-cap / maximum-target calibration, including optional pure feasibility and the readable-program exponent. It is proved in full rather than inferred as a priority claim from a literature gap.

