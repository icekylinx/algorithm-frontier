# Exact prefix, laminar and sparse quotas

The algorithms in this family optimize one signed rational scalar exactly while preserving mixed nonnegative integer quotas, a single global integral polymatroid, and every original mandatory resource total. Their complexity parameters describe quota geometry; they are separate from numeric-target sums.

| Theorem | Time apart from $\operatorname{poly}(H)$ | Complete proof |
|---|---|---|
| One common order and common weights | $2^{O(B)}$ | [Prefix theorem](manuscripts/exact-weighted-prefix-quotas-max-target.md) |
| Two common orders | $2^{O(B\log(B+2))}$ | [Two-order theorem](manuscripts/two-order-weighted-prefix-target-classification.md) |
| $C$ support patterns, one order | $2^{O(\sqrt{B\min\{C,B\}})}$ | [Support tradeoffs](manuscripts/weighted-prefix-support-budget-tradeoffs.md) |
| $C$ support patterns, two orders | $2^{O(\min\{\sqrt{BC},B\log(2+\min\{C/B,B\})\})}$ | [Support tradeoffs](manuscripts/weighted-prefix-support-budget-tradeoffs.md) |
| $p$ shared weight families | $2^{O(pB\log(p+2))}$ | [Family algorithm](manuscripts/few-weight-families-prefix-target-scheme.md), [joint lower calibration](manuscripts/few-weight-prefix-joint-lower-bounds.md) |
| Common-weight laminar quotas, root cap $B$ | $2^{4B^2+O(B\log(B+1))}$ | Theorem and complete proof below |
| Sparse root-bounded mixed quotas | $2^{O((\Delta+1)B_0\log((\Delta+1)B_0(B+2)+2))}$ | [Direct hash-and-profile proof](manuscripts/sparse-root-quota-hash-profile-algorithm.md) |

Here $B$ bounds the finite targets, $B_0\le B$ is the root cap, and $\Delta$ counts positive nonroot incidences per coordinate. In the sparse theorem a zero-root coordinate is zero in every numeric row, but can have an arbitrary scalar cost. All algorithms use uniform polynomial binary workspace.

The following reductions return a retained ground with the original oracle and weights. They are not running-time exponents or parameter-only encodings of an arbitrary oracle.

| Deterministic polynomial-time reduction | Retained-ground bound | Complete proof |
|---|---|---|
| Sparse packing with one item matroid, frequency $\delta$, solution size at most $k$ | $k\delta![k(\delta(k-1)+1)]^\delta=O_\delta(k^{2\delta+1})$ | [Sparse packing](manuscripts/deterministic-sparse-packing-oracle-kernel.md) |
| One arbitrary and $d$ additional coverable matroids | $k\,d![k(1+\sum_i g_i)]^d$ | [Coverable matroids](manuscripts/deterministic-coverable-matroid-sunflower-kernel.md) |
| One arbitrary and $d$ explicit transversal matroids | $O_d(k^{2d+1})$ | [Transversal transfer](manuscripts/deterministic-transversal-matroid-kernel-transfer.md) |
| Graph matching with a matroid on edges | $O(k^4)$ for a simple graph; $O(k^5)$ with parallel edges | [Graph corollaries](manuscripts/deterministic-sparse-packing-oracle-kernel.md) |
| Sparse numeric quotas with valuated completion | Parameter-bounded positive capacity; original zero-coordinate completion retained | [Coefficient-consistent sunflower proof](manuscripts/valuated-sparse-quota-sunflower-kernel.md) |

The lower bounds distinguish rank queries from computation with an explicitly readable rank program. In particular, [disjoint nonroot equality rows](manuscripts/disjoint-row-root-target-sharp-lower.md) already force $2^{\Omega(B\log(B+2))}$ rank queries at frequency one; [row-dependent weights](manuscripts/row-dependent-full-prefix-target-boundary.md) cross a separate W[2]-hard boundary. The laminar theorem below has a $2^{\Omega(B)}$ oracle lower bound and does not close that exponent gap.

## Main theorem: the quadratic laminar exponent

The arbitrary-cost laminar theorem in [laminar-valuated-zero-completion-fpt.md](manuscripts/laminar-valuated-zero-completion-fpt.md) (VZ) has time $2^{O(B^2\log(B+1))}\operatorname{poly}(H)$. This note replaces its recursive upper-blocker representatives by deterministic universal colorings. The resulting time is

$$
2^{O(B^2)}\operatorname{poly}(H),
\tag{LC1}
$$

with the same exact numeric constraints, arbitrary signed scalar costs, original resource totals, and uniform polynomial binary space. In particular, real zero-weight coordinates keep their arbitrary costs and binary counts.

Universal sets, small-bias constructions, and weighted Rado induction are established tools. The new composition here is the short two-color certificate supplied by laminar blockers, together with the completed-cost overlap oracle. A self-contained elementary coloring construction is included so that no exponential-space catalogue is assumed.

## 1. Model and theorem

Let $F$ be a normalized monotone integral polymatroid rank on an explicit coordinate ground $E$. Resource vectors are integer vectors in $P(F)$, or in its original-total base of total $R=F(E)$. Eligibility restrictions and binary domains can be absorbed by the same preparation as in VZ; a mandatory problem always retains its original required total.

An explicit laminar family $\mathcal L$ has common nonnegative integer coordinate weights $w$ and mixed quotas

$$
l_A\le \sum_{e\in A} w_e x_e\le u_A.
\tag{LC2}
$$

A root row imposes $w\cdot x\le B$, with nonnegative integer $B$. Missing directional bounds are allowed. The scalar $c\cdot x$, with arbitrary signed rational coefficients, is minimized or maximized exactly. Testing a bound on this same scalar is included; a second independent scalar constraint is not asserted.

**Theorem.** This problem admits a deterministic exact algorithm of time LC1 and workspace polynomial in the complete binary input length $H$. Polynomial rank-oracle bit bounds and standard exact submodular minimization and integral polymatroid intersection are included in the computational model.

More explicitly, the construction below gives a bound of the form

$$
2^{4B^2+O(B\log(B+1))}\operatorname{poly}(H)
                    \qquad (B\ge1).
\tag{LC3}
$$

The coefficient in LC3 is only an accounting bound for this construction, not an optimized constant. The existing $2^{\Omega(B)}$ oracle lower family remains applicable and leaves an exponent gap.

## 2. Prepared geometry and the completed-cost oracle

We restate the exact prerequisites from VZ, whose detailed proofs remain separate companion proofs.

An optional resource can be converted to a full base by one new zero-weight, zero-cost disposal coordinate. Its rank is $F(A)$ on sets without disposal and $R$ on sets with disposal. An optional vector extends by its missing mass, and projection preserves all original constraints and the scalar. A mandatory resource receives no disposal. All real zero-weight coordinates are retained.

Remove positive coordinates individually prohibited by an upper row, and perform the safe upper/lower dominance reductions. The retained upper capacities are positive integers that strictly increase up a containing chain. Their depth $D$ is therefore at most $B$. The number $m$ of upper rows may be arbitrarily large.

Retained positive lower targets strictly decrease down a containing chain. Their minimal sets are disjoint; if their targets sum to more than $B$, reject. Otherwise at most $B$ leaves and depth at most $B$ imply at most $B^2$ retained lower nodes and at most $B^2+1$ lower-membership patterns.

Write $P$ for positive-weight coordinates and $Z$ for zero-weight coordinates after preparation, including disposal if applicable. A positive coordinate $e$ needs at most

$$
b_e=\min\{F(\{e\}),\lfloor B/w_e\rfloor\}
\tag{LC4}
$$

unit copies. Their explicit ground, when constructed, is $U=\dot\bigcup_{e\in P}U_e$. Copies inherit their owner's weight, scalar, and numeric memberships. A class $T\subseteq U$ fixes the positive weight and the full retained lower-membership pattern. There are at most

$$
G\le B(B^2+1)
\tag{LC5}
$$

nonempty classes.

For a fixed $k$, let $p_k(S)$ be the minimum true scalar of a full resource base whose positive copy set is exactly $S\in\binom Uk$, with arbitrary compatible zero counts; set its value to $+\infty$ when no such completion exists. If its finite domain is nonempty, $p_k$ is a minimum-cost valuated matroid. One proof uses the full natural matroid of $F$, private edges for positive copies, and $R-k$ compulsory left dummy vertices adjacent to zero units. Matching edge weights are the negatives of their true scalar coefficients. Public weighted Rado induction then gives the valuation; the large conceptual matching ground is never constructed.

The needed oracle, given $Y\subseteq U$, returns a finite basis $A$ maximizing $|A\cap Y|$, then minimizing $p_k(A)$. It is polynomial on the compressed ground $U\dot\cup Z$. Its first rank is the box-truncated shared resource

$$
G(V)=\min_{C\subseteq P}
       \left[F((V\cap Z)\cup C)
                  +\sum_{e\in P\setminus C}|V\cap U_e|\right].
\tag{LC6}
$$

The second is one partition rank with positive-group cap $k$ and zero-group cap $R-k$. Requiring total $R$ makes both caps tight on an integral face. Guard $0\le k\le\min\{R,|U|\}$, and skip an empty face. After clearing scalar denominators, $M=2R\max_e|c_e|+1$ makes minimizing true cost minus $M$ times positive-copy overlap exactly the required lexicographic optimization. Here the displayed $c$ in this reward formula denotes the cleared integer coefficients. A polynomial-bit tertiary subset score can fix the returned positive set deterministically.

Thus individual-copy rewards, unrestricted zero costs, and the original total use exactly two integral ranks. The numeric laminar rows are not imposed on this oracle. They are preserved by replacements below.

For completeness, the overlap replacement consequence is short. Given a finite basis $S$ and $e\in S\cap Y$, if $e\in A$, keep it. Otherwise valuated exchange supplies $f\in A\setminus S$ with

$$
p_k(S)+p_k(A)\ge p_k(S-e+f)+p_k(A-f+e).
\tag{LC7}
$$

Maximum overlap forces $f\in Y$. On that same overlap face, minimum value gives $p_k(A-f+e)\ge p_k(A)$. Hence

$$
f\in A\cap Y,\qquad p_k(S-e+f)\le p_k(S).
\tag{LC8}
$$

If the replacement is proper, $f\notin S$.

## 3. A short red/green certificate for laminar replacement

Fix a numerically feasible finite basis $S$, an element $e\in S$, and its class $T$. Put $S^-=S-e$ and $w=w_e$. Let $\mathcal A(e)$ be the retained upper nodes containing $e$. Then

$$
|\mathcal A(e)|\le D\le B.
\tag{LC9}
$$

An upper node that blocks an equal-weight replacement satisfies

$$
u_A\ge w,\qquad w(S^-\cap U_A)+w>u_A.
\tag{LC10}
$$

Nodes with capacity below $w$ contain no eligible candidate of this class. A node in LC10 contains at least one unit of $S^-$, and cannot contain $e$: if it did, the left side would be exactly the original feasible total of $S$ in that node.

Let $\mathcal X$ be the inclusion-maximal nodes in LC10. Laminarity makes these nodes disjoint, and each contains a unit of $S^-$. Therefore

$$
|\mathcal X|\le k-1,
                 \qquad \mathcal X\cap\mathcal A(e)=\varnothing.
\tag{LC11}
$$

Every blocking node lies inside a member of $\mathcal X$.

A coloring of the upper-node IDs is suitable if every node in $\mathcal A(e)$ is green and every node in $\mathcal X$ is red. Only

$$
D+k-1\le2B-1
\tag{LC12}
$$

IDs have prescribed colors. For any coloring $\chi$, define the class pool

$$
Y(T,\chi)=\{f\in T:\text{every retained upper node containing }f
                                      \text{ is green}\}.
\tag{LC13}
$$

For a suitable coloring, $e\in Y(T,\chi)$, and no member of the pool lies in any maximal blocker. Apply LC8 to the overlap-optimal basis for this pool. The resulting same-class replacement avoids all upper blockers, preserves every lower total, preserves root weight, and does not worsen completed scalar cost.

This reduces representative construction to a binary coloring family realizing every prescription on at most $2B-1$ upper IDs. It does not require identifying the protected basis or its blockers algorithmically.

## 4. An elementary injective hash family

Assume $m\ge1$, and put

$$
K=\min\{m,2B-1\},\qquad
 L=\max\{1,\lceil\log_2(m+1)\rceil\},\qquad
 D_0=\binom K2L.
\tag{LC14}
$$

Represent distinct upper-row IDs by their distinct binary polynomials $a_j(X)$ of degree less than $L$. Let $d\ge2$ be the least integer such that

$$
q=2^d>4(D_0+1).
\tag{LC15}
$$

Then $q\le8(D_0+1)=O(K^2L)$. Enumerate all monic degree-$d$ polynomials over $\mathbb F_2$, retain the irreducible ones, and use

$$
h_f(j)=a_j(X)\bmod f(X)
\tag{LC16}
$$

as a hash value in $\{0,\ldots,q-1\}$, using the binary coefficient encoding of the remainder.

Every set $W$ of at most $K$ IDs is injective under at least one such hash. Indeed, the nonzero pair-difference product

$$
P_W(X)=\prod_{i<j,\ i,j\in W}(a_i(X)-a_j(X))
\tag{LC17}
$$

has degree at most $D_0$. At most $D_0/d$ different monic irreducibles of degree $d$ divide it. The number $I_d$ of monic irreducibles of that degree satisfies

$$
I_d\ge\frac{2^d}{2d}
                                      >\frac{D_0}{d}.
\tag{LC18}
$$

The standard elementary factorization of $X^{2^d}-X$ gives
$dI_d=2^d-\sum_{j\mid d,\,j<d}jI_j$.
Every proper divisor is at most $d/2$, and $jI_j\le2^j$. Summing $2^j$ for $1\le j\le\lfloor d/2\rfloor$, with $d=2,3$ checked directly, proves the first inequality in LC18. Thus some enumerated irreducible does not divide LC17 and causes no collision on $W$. The empty product for $|W|\le1$ causes no exception.

Irreducibility is testable using polynomial binary workspace: for every $1\le j\le\lfloor d/2\rfloor$, compute
$\gcd(f,X^{2^j}-X)$ by repeated squaring modulo $f$. A reducible degree-$d$ polynomial has an irreducible factor of degree at most $d/2$, and that factor is detected at its degree. An irreducible degree-$d$ polynomial passes all these tests. Thus enumeration and each test use polynomial work per candidate; there are at most $q$ candidates.

The product LC17 is a proof device and is not constructed.

## 5. Explicit small-bias colorings after hashing

Let

$$
t=d+K+2,\qquad Q=2^t=q\,2^{K+2}.
\tag{LC19}
$$

Construct a field $\mathbb F_Q$ by finding one monic irreducible degree-$t$ binary polynomial. Enumerating at most $Q$ candidates and using the preceding irreducibility test suffices. Only a degree-$t$ polynomial and polynomial-size arithmetic state are retained.

For every $(\alpha,\beta)\in\mathbb F_Q^2$, color hashed position $i\in\{0,\ldots,q-1\}$ by

$$
\gamma_{\alpha,\beta}(i)
                             =\operatorname{Tr}(\alpha\beta^i)
                                 \in\mathbb F_2.
\tag{LC20}
$$

Color one is green and color zero is red. The convention $\beta^0=1$ includes $\beta=0$.

Here $\operatorname{Tr}(z)=\sum_{a=0}^{t-1}z^{2^a}$. This is a nonzero $\mathbb F_2$-linear map to $\mathbb F_2$: squaring leaves its value unchanged, and its defining nonzero polynomial has degree $2^{t-1}<Q$, so it cannot vanish on all of $\mathbb F_Q$. Consequently its values are equally split between zero and one. Multiplication by any nonzero field element preserves that balance.

For a nonempty position set $J$, let $P_J(Y)=\sum_{i\in J}Y^i$. It is a nonzero polynomial of degree at most $q-1$. Averaging first over $\alpha$ gives

$$
\mathbb E_{\alpha,\beta}
     (-1)^{\sum_{i\in J}\gamma_{\alpha,\beta}(i)}
       =\Pr_\beta[P_J(\beta)=0]
       \le\frac{q-1}{Q}<\frac qQ.
\tag{LC21}
$$

The absolute value has the same bound; the displayed expectation is nonnegative. For $s\le K$ distinct positions and any prescribed bits $b_1,\ldots,b_s$, expand the product of their indicator functions. The empty term is one, and each nonempty term has absolute expectation below $q/Q$. Therefore

$$
\Pr[\gamma(i_a)=b_a\text{ for every }a]
   \ge 2^{-s}\left(1-(2^s-1)\frac qQ\right)
   >\frac34\,2^{-s}>0.
\tag{LC22}
$$

Every prescribed pattern on at most $K$ hashed positions is realized by an enumerated seed.

Compose LC20 with all hashes LC16. On every set of at most $K$ original IDs, first choose an injective hash and then a seed realizing the desired pattern. This gives a deterministic universal family $\mathcal C$ with

$$
|\mathcal C|\le qQ^2
                =q^3\,2^{2K+4}
                \le 2^{4B+O(\log(B+1))}\,L^3.
\tag{LC23}
$$

Duplicates are harmless. No coloring list or field table is stored. Given a row ID and a seed, its color is evaluated by polynomial division, binary powering and repeated squaring for the trace. If $m=0$, use the single empty coloring instead and omit Sections 4–5.

## 6. Representatives and exact recovery

For each nonempty weight/lower-pattern class $T$, each valid cardinality $1\le k\le B$ with nonempty completion domain, and each $\chi\in\mathcal C$, call the overlap oracle on LC13. Emit its at-most-$k$ elements in $A\cap Y(T,\chi)$.

For every numerically feasible finite basis $S$ and selected $e$, the universal family contains the red/green certificate of Section 3. That call supplies a no-worse feasible replacement. Repeatedly replace a selected element outside the emitted union. Every proper replacement inserts a representative not already selected, so the count of selected representatives strictly increases. Numeric feasibility, original completion and true scalar value are preserved or improved. Hence a fixed-cardinality optimum is represented.

The number of emitted positions for cardinality $k$ is at most

$$
N_k\le Gk\,qQ^2
                       \le 2^{4B+O(\log(B+1))}\,L^3.
\tag{LC24}
$$

Enumerate $k$-tuples of position descriptions, reject repeats, test every original numeric row, and evaluate $p_k(S)$ by the compressed full-completion oracle. An empty or impossible position is rejected. For a fixed positive set, masking all other positive copies, keeping positive total $k$ and zero total $R-k$, and minimizing the true scalar returns its exact best completion.

Every emitted union need not itself be materialized. Nor is any upper or lower numeric row added to the overlap query. Those rows are checked on final sets, and Section 3 proves that a represented optimum is among them.

Take the best attaining solution over all cardinalities, including the separate zero-positive solution if feasible. Since every returned solution is original-feasible and some represented solution has optimum scalar, the algorithm is exact.

## 7. All-input time and uniform polynomial space

Use the same two implementation branches as VZ. Let $n=|P|$.

If $B=0$ or $n=0$, positive counts vanish. Test the lower rows and optimize the signed scalar on the remaining zero-weight resource, retaining the required total. This is polynomial, including the rank-zero case.

If $B\ge n\ge1$, stream original positive count vectors
$0\le x_e\le\lfloor B/w_e\rfloor$.
There are at most $(B+1)^n\le(B+1)^B$. Test numeric rows and positive-resource feasibility. For a surviving vector, the exact zero-completion rank is

$$
h_x(A)=\min_{C\subseteq P}\{F(A\cup C)-x(C)\},\qquad A\subseteq Z.
\tag{LC25}
$$

Its full rank is at most $R-x(P)$, and equality is necessary and sufficient for a full completion. Signed-cost greedy optimization on this residual base recovers the best zero vector. This branch keeps only input-many binary counters and polynomial oracle state. Its time fits LC3, and no large copy ground is built.

In the remaining branch $1\le B<n$, $|U|\le nB<n^2$. Also $m$ is explicit-input size, $K\le2B-1$, $d=O(\log(B+1)+\log(L+1))$, and
$t=O(B+\log(L+1))$.
The hash range $q=O(B^2L)$ is polynomial in $H$. The larger field has $Q=2^{O(B)}\operatorname{poly}(B,L)$ elements, but a field element is stored in only $t$ bits. A defining irreducible polynomial can be found in $Q\operatorname{poly}(t)$ time and polynomial space, once and for all.

A representative position consists of a class index, a degree-$d$ polynomial, two degree-$t$ field elements, and an output index in $[k]$. Its deterministic oracle call can be recomputed from that description. Invalid irreducibles, empty pools and missing output indices are rejected, so counting all such position descriptions only enlarges LC24. At most $B$ descriptions are stored at once, along with the current $k$-set and one compressed recovery problem. Their total bit length is polynomial in $H$.

The enumeration time is bounded on every input by

$$
\sum_{k=1}^{B}(N_k+1)^k\operatorname{poly}(H)
       \le 2^{4B^2+O(B\log(B+1))}\,L^{3B}
                                                 \operatorname{poly}(H).
\tag{LC26}
$$

This includes failed tuples, invalid positions, rejected numeric rows and empty completion faces. The construction of the field and hash family is smaller than this bound. Every replayed oracle computation has polynomial cost on the current branch's polynomial-size ground.

The remaining logarithmic input factor is absorbed with a fixed-degree polynomial, not with an input exponent depending on $B$. For every $a>0$, maximizing $x^a e^{-x}$ over $x\ge0$ gives

$$
(\log(m+2))^a\le(a/e)^a(m+2).
\tag{LC27}
$$

Since $L=O(\log(m+2))$, taking $a=3B$ shows that $L^{3B}$ contributes only $2^{O(B\log(B+1))}(m+2)$. This proves LC3 and hence LC1, uniformly. The direct count-vector branch has the same space guarantee when $B$ is binary-large. No probability, successful-instance promise, or stored exponential family is used by the algorithm.

## 8. Sources, improvement, and remaining gap

The power/linear-functional small-bias method is classical. Alon, Goldreich, Håstad and Peralta's [*Simple Constructions of Almost k-wise Independent Random Variables*](https://www.cs.tau.ac.il/~nogaa/PDFS/aghp4.pdf), Section 5, Construction 3, uses finite-field powers paired with a binary linear functional. The trace formulation above gives the same family up to an invertible change of the linear-functional seed. Their Lemma 1 and Appendix A give the small-bias-to-pattern conversion. The present proof states the elementary polynomial-root and indicator-expansion arguments explicitly; it does not claim a new small-bias family.

Naor, Schulman and Srinivasan's [*Splitters and near-optimal derandomization*](https://www.wisdom.weizmann.ac.il/~naor/PAPERS/splitters.pdf) supplies the established universal-set and splitter context. Neither universal sets nor their use to derandomize bounded prescriptions is a novelty claim here. Our deliberately elementary family is sufficient for the quadratic exponent and exposes its polynomial-space evaluation directly.

The completed-cost valuated oracle is the accepted VZ dependency; its public weighted Rado source is Husić, Loho, Smith and Végh's [*On complete classes of valuated matroids*](https://theoretics.episciences.org/14792/pdf), Definition 1.1 and the cited induction/exchange statements. The original global resource, all mandatory units, and all signed zero costs remain unchanged in this refinement.

The proved gain is the replacement of VZ's $2^{O(B\log B)}$-size recursive candidate catalogue by $2^{O(B)}\operatorname{poly}(B,\log m)$ emitted positions. Its $B$-set recovery reduces the exponent from $B^2\log B$ to $B^2$. This does not close the gap to the existing $2^{\Omega(B)}$ lower bound, nor assert an optimal exponent or publication priority.

No frozen T proof is edited. The complete new coloring, replacement, time and space arguments have undergone independent internal review. This is not formal verification or external peer review.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
