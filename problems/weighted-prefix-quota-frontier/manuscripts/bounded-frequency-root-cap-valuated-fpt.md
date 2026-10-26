# Exact sparse numeric quotas with a root cap and arbitrary completion costs

**25 October 2026. Increment U. Complete manuscript-level proof with independent internal review.**

Rows may intersect arbitrarily and may have different nonnegative integer coefficients. A distinguished positive charge bounds the number of units that can participate in any numeric quota. The other structural parameter is column frequency, excluding that distinguished row. Neither the number of rows nor the number of distinct supports enters the exponential parameter.

Scalar coefficients on quota-free units are unrestricted. Their best completion cost is handled by the fixed-cardinality valuated-matroid interface established in *laminar_valuated_zero_completion_fpt.md* (VZ). A deterministic small-range hash catalogue replaces the laminar blocker recursion. Every actual resource optimization still uses one global integral polymatroid and one partition rank.

## 1. Model, parameters, and theorem

Let $F$ be a normalized monotone integral polymatroid rank on an explicit coordinate ground $E$. Counts, coordinate domains, and rank values are binary encoded. The resource requirement is either

$$
x\in P(F)\cap\mathbb Z_{\ge0}^{E},
 \qquad\hbox{or}\qquad
 x\in B(F)\cap\mathbb Z_{\ge0}^{E}.
\tag{BF1}
$$

In the base model the required original total is $R=F(E)$. Eligibility masks and box domains may be prepared into the rank, but a mandatory instance retains this original total and rejects if it cannot be attained.

There is a distinguished root cap

$$
\sum_{e\in E}w_ex_e\le B_0,
                   \qquad w_e\in\mathbb Z_{\ge0},
\tag{BF2}
$$

and an explicit collection of other rows

$$
l_j\le\sum_{e\in E}a_{je}x_e\le u_j,
                     \qquad a_{je}\in\mathbb Z_{\ge0}.
\tag{BF3}
$$

Missing lower bounds are zero; missing upper bounds are infinity. Finite targets are nonnegative integers. An equality is one interval row with equal targets. Coefficients need not factor into a common weight and set incidences.

The essential root-charge condition is

$$
w_e=0\quad\Longrightarrow\quad
                      a_{je}=0\quad\hbox{for every }j.
\tag{BF4}
$$

Thus every unit contributing to a nondistinguished numeric row consumes at least one integer root unit. Positive-root coordinates may have zero coefficients in all other rows.

Define

$$
\delta_0=\max_{e\in E}|\{j:a_{je}>0\}|,\qquad
 \Delta=\max\{1,\delta_0\},\qquad
 B=\max\{B_0,\text{all finite row targets}\}.
\tag{BF5}
$$

An empty maximum is zero. The root is excluded from frequency; an interval/equality row is counted once. Preparation may reduce actual frequency, and an upper bound on the original frequency remains valid.

The scalar $c\cdot x$ has arbitrary signed rational coefficients, including on root-zero coordinates, and is minimized or maximized exactly. A requested upper or lower bound on this same scalar can be decided by the corresponding optimum. This is not optimization of one scalar subject to a different independent scalar budget.

**Theorem.** If $B_0=0$, feasibility and scalar optimization are polynomial. If $B_0\ge1$, they have a deterministic algorithm with time

$$
2^{O(\Delta B_0\log(\Delta B_0B+2))}\operatorname{poly}(H)
 \ \le\
 2^{O(\Delta B\log(\Delta B+2))}\operatorname{poly}(H)
\tag{BF6}
$$

and uniform polynomial binary workspace. Here $H$ includes the explicit binary input and rank-oracle bit bounds. Exact SFM and weighted integral-polymatroid intersection are charged polynomially. The bound holds on all inputs, including infeasible instances and failed catalogue encodings.

For constant positive frequency, the worst-case order $2^{O(B\log B)}$ is sharp in the rank-oracle model. Section 12 retains the frequency-two zero-one baseline. The companion *disjoint_row_root_target_sharp_lower.md* strengthens the boundary to frequency one with disjoint weighted equalities, zero scalar, and pure feasibility in both resource domains.

The companion *sparse_root_quota_hash_profile_algorithm.md* gives a second, direct proof without unit expansion or valuated completion. *valuated_sparse_quota_sunflower_kernel.md* strengthens the preprocessing conclusion to a deterministic positive-capacity kernel; it does not reduce BF6's exponential order.

The convention $\Delta=\max\{1,\delta_0\}$ is deliberate: raw frequency zero leaves the root knapsack constraint and must not make the exponential factor disappear.

## 2. Safe preparation and integer lower capping

Negate the scalar for maximization. Discard vacuous rows and reject inconsistent intervals. Mask a positive-root coordinate if $w_e>B_0$, or if $a_{je}>u_j$ in any finite upper row. Such a coordinate cannot occur even once in an integer feasible allocation. Upper-zero rows therefore mask all their positive-coefficient coordinates. Resource loops may also be removed. Root-zero coordinates are not removed merely because their scalar is nonzero.

For optional resources use VZ's disposal lift: add a coordinate of numeric weight and scalar zero, and define $F^+(A)=F(A)$ when disposal is absent and $F^+(A)=R$ when it is present. Every optional vector extends to total $R$ by putting unused resource in disposal. Projection preserves all original rows and scalar. Mandatory resources receive no disposal. Subsequent masks keep required total $R$; rank loss is genuine mandatory infeasibility.

Write $P=\{e:w_e>0\}$, $Z=\{e:w_e=0\}$, including disposal in $Z$ when present. Every numeric row is zero on $Z$. Below $F$ denotes the prepared full-base rank.

For a positive lower row put

$$
\lambda_{je}=\min\{a_{je},l_j\},
                          \qquad l_j>0.
\tag{BF7}
$$

For nonnegative integer counts,

$$
\sum_ea_{je}x_e\ge l_j
       \quad\Longleftrightarrow\quad
       \sum_e\lambda_{je}x_e\ge l_j.
\tag{BF8}
$$

If a used coefficient is at least $l_j$, its first capped occurrence reaches the target. Otherwise capping changes none of the used coefficients. The reverse implication follows from $\lambda_{je}\le a_{je}$. This is integer feasibility equivalence, not equality of original totals or a fractional claim. Finite upper rows retain their original coefficients, which after individual eligibility lie in $\{0,\ldots,B\}$ on surviving coordinates.

## 3. Few positive lower rows and replacement classes

Each positive lower row needs a selected positive-root unit. There are at most $B_0$ such units, each occurring in at most $\Delta$ other rows. Therefore

$$
m_L:=|\{j:l_j>0\}|\le\Delta B_0
\tag{BF9}
$$

is necessary. Reject if it fails, or if a positive lower row has no remaining positive coefficient. This uses incidence counting, not a bound on the sum of targets: a large coefficient can meet a row with one unit.

Classify positive coordinates and their unit copies by

$$
(w_e,(\lambda_{je})_{j:l_j>0}).
\tag{BF10}
$$

The capped lower vector has at most $\Delta$ nonzero entries, each at most $B$. Thus the number $G$ of classes satisfies

$$
\begin{split}
 G&\le B_0\sum_{i=0}^{\min\{\Delta,m_L\}}\binom{m_L}{i}B^i\\
  &\le B_0(1+m_LB)^\Delta
   \le B_0(1+\Delta B_0B)^\Delta.
 \end{split}
\tag{BF11}
$$

The middle bound encodes each sparse vector by $\Delta$ slots, each empty or a row/value pair, in canonical order. Only input classes need be stored. Same-class replacement preserves root charge and all capped lower totals; BF8 preserves original lower feasibility. Equalities follow once original upper sides are also preserved.

## 4. The valued completion interface

Allow $b_e=\min\{F(\{e\}),\lfloor B_0/w_e\rfloor\}$ distinct copies $U_e$ of each $e\in P$, and set $U=\bigcup_eU_e$. Section 11 avoids constructing them when $B_0$ is large. Fix $0\le k\le\min\{B_0,R,|U|\}$.

For a $k$-set $S\subseteq U$, let $p_k(S)$ be the minimum true scalar of a full original-total resource base with positive units exactly $S$, allowing arbitrary compatible integer counts on $Z$. Set $p_k(S)=+\infty$ if no such completion exists.

VZ proves the following facts without using laminarity of any numeric row. When its finite domain is nonempty, $p_k$ is a minimum-cost valuated matroid: for domain bases $S,A$ and $e\in S\setminus A$, some $f\in A\setminus S$ satisfies

$$
p_k(S)+p_k(A)\ge p_k(S-e+f)+p_k(A-f+e).
\tag{BF12}
$$

The proof maps to the established weighted Rado-induction theorem. Conceptually take the full natural matroid of the prepared resource on the right. Every allowed positive copy on the left has only its private right edge; $R-k$ mandatory left dummies may match any right zero unit. Edge weights are minus true scalar. The R-minor valuation is $-p_k$. The right rank remains the original $R$, even with restricted left positives. This huge finite graph is a proof device only.

For any $Y\subseteq U$, an exact compressed oracle returns a domain basis $A$ first maximizing $|A\cap Y|$, then minimizing $p_k(A)$. On the actual ground $U\dot\cup Z$, one integral resource rank is

$$
G_F(D)=\min_{C\subseteq P}
 \left[F((D\cap Z)\cup C)+
                   \sum_{e\in P\setminus C}|D\cap U_e|\right].
\tag{BF13}
$$

It represents the shared original resource with cap one on each positive copy, and is evaluated by SFM on original coordinates. Intersect it with **one** partition rank of caps $k$ on $U$ and $R-k$ on $Z$, and require total $R$. This integral face forces both totals exactly.

Clear scalar denominators, put $C_{\max}=\max|\widetilde c_e|$ and $M=2RC_{\max}+1$, and minimize

$$
\widetilde c\cdot z
                       -M\sum_{u\in Y}z_u.
\tag{BF14}
$$

One overlap unit dominates all true-cost differences. Individual-copy rewards and caps are essential. Empty faces detect empty valuation domains. Fix deterministic ties for replay; VZ supplies a polynomial-bit tertiary subset score if desired.

No BF2–BF3 quota is imposed in this overlap oracle. Its basis need not be numerically feasible.

**Overlap replacement lemma.** For a domain basis $S$ and $e\in S\cap Y$, some emitted $f\in A\cap Y$ satisfies

$$
p_k(S-e+f)\le p_k(S).
\tag{BF15}
$$

If $e\in A$, use $f=e$. Otherwise use BF12. An exchanged $f\notin Y$ would increase the overlap of $A-f+e$, a contradiction. Thus $f\in Y$, and the second optimization criterion implies $p_k(A-f+e)\ge p_k(A)$. Cancellation proves BF15. A proper exchanged $f$ is outside $S$.

## 5. A deterministic small-range hash catalogue

Let $m_U$ be the number of remaining finite upper rows, excluding the root. If it is zero, use one unfiltered pool per replacement class and omit the hashing construction.

Otherwise label its rows by distinct binary polynomials of degree less than

$$
L=\max\{1,\lceil\log_2(m_U+1)\rceil\}.
$$

Set $K=\Delta(B_0+1)$, $D_0=\binom K2L$, and choose the smallest $d\ge2$ with

$$
q=2^d>4(D_0+1).
\tag{BF16}
$$

Then $q=O(K^2L)$. Enumerate the monic irreducible degree-$d$ polynomials $f\in\mathbb F_2[X]$. Each supplies a hash to the $q$ residues of degree less than $d$:

$$
h_f(j)=\operatorname{id}_j\bmod f.
\tag{BF17}
$$

**Hash lemma.** Every set $W$ of at most $K$ row IDs is injectively hashed by at least one catalogue member.

For completeness, let $I_d$ count degree-$d$ monic irreducibles. The factorization of $X^{2^d}-X$ gives $2^d=\sum_{r\mid d}rI_r$. Its roots form the field of $2^d$ elements; the minimal-polynomial degree divides $d$, every irreducible of a dividing degree occurs, and the derivative is one. Since $rI_r\le2^r$ and every proper divisor of $d$ is at most $d/2$,

$$
dI_d\ge2^d-\sum_{r=1}^{\lfloor d/2\rfloor}2^r
                  \ge2^{d-1}\qquad(d\ge2).
\tag{BF18}
$$

For fixed $W$, its pair-difference product
$D_W=\prod_{\{i,j\}\subseteq W}(\operatorname{id}_i-\operatorname{id}_j)$
is nonzero and has degree below $D_0$; the empty product is one. At most $D_0/d$ distinct degree-$d$ irreducibles divide it, whereas $I_d\ge q/(2d)>D_0/d$. Choose one not dividing the product. No two IDs then have equal remainders.

The catalogue is explicitly deterministic. Stream all $q$ monic degree-$d$ polynomials and retain exactly those for which

$$
\gcd(f,X^{2^j}-X)=1
                 \quad(1\le j\le\lfloor d/2\rfloor).
$$

A reducible polynomial has an irreducible factor of degree at most $d/2$, detected by one test; an irreducible degree-$d$ polynomial passes them all. Successive squaring modulo $f$ and binary-polynomial gcd are polynomial in $d$. No prime-density estimate, randomized construction, or large stored hash table is assumed.

## 6. Coefficient-labelled pools

For a copy $u$, let $I(u)=\{j:u_j<\infty,\ a_{j,u}>0\}$ be its nondistinguished finite-upper incidences, of size at most $\Delta$. Coefficients are inherited from its owner.

Fix a class $T$, a hash $h$, a palette $C$ of at most $\Delta$ residues, and thresholds $t_c\in\{1,\ldots,B\}$ for $c\in C$. Form

$$
Y(T,h,C,t)=
 \{u\in T:h(I(u))\subseteq C,\
       a_{j,u}\le t_{h(j)}\text{ for every }j\in I(u)\}.
\tag{BF19}
$$

The empty palette is allowed and gives the members with no upper incidence. For each pool run the overlap-first oracle and emit all of $A\cap Y$, at most $k$ copies.

For each hash, the palette/threshold count is at most

$$
\sum_{i=0}^{\min\{\Delta,q\}}\binom qiB^i
                     \le(\Delta+1)(qB+1)^\Delta.
\tag{BF20}
$$

Stream sorted palettes with binary threshold counters, or use padded slots and reject noncanonical encodings. The same bound, up to an inessential parameter factor, includes failed encodings. No subset of the full upper-row ground is directly guessed.

## 7. Every upper row survives a protected replacement

Fix a numerically feasible domain $k$-set $S$ and $e\in S$, and use its class $T$. Put

$$
W=\bigcup_{u\in S}I(u).
\tag{BF21}
$$

It has at most $\Delta k\le\Delta B_0<K$ rows. Choose a catalogue hash injective on all of $W$. Use palette and thresholds

$$
C=h(I(e)),\qquad
          t_{h(j)}=a_{j,e}\quad(j\in I(e)).
\tag{BF22}
$$

Injectivity makes thresholds well defined; individual eligibility places them in $\{1,\ldots,B\}$. This pool contains $e$.

Write $S^-=S-e$. Every candidate $f$ in this pool preserves every finite upper:

1. If row $j$ meets both $S^-$ and $e$, then $a_{j,f}\le a_{j,e}$ if $f$ enters it. Its total cannot increase.
2. If row $j$ meets $S^-$ but not $e$, it belongs to $W\setminus I(e)$. Its hash is outside the palette, so $f$ cannot enter.
3. If row $j$ does not meet $S^-$, the only new positive occurrence is $f$, and individual eligibility gives $a_{j,f}\le u_j$. This is safe even when its hash collides with a different palette row.

The third case includes rows that met only the removed $e$. Same-class membership preserves root charge and capped lower totals. Thus all original numeric predicates survive.

BF15 supplies an emitted candidate with no worse $p_k$. Its finite valuation domain preserves resource feasibility and full original-total completion. The whole oracle basis $A$ need not satisfy any numeric quota.

Hashing all upper incidences of $S$, rather than just a guessed overload list, is the reason this argument handles row-dependent coefficients. Collisions with rows untouched by $S^-$ are harmless because individual eligibility was enforced first.

## 8. Exact optimization from emitted positions

For each $1\le k\le\min\{B_0,R,|U|\}$, detect and skip empty valuation domains. Conceptually take the union of all emitted copies over classes and pools.

Starting from a numerically feasible domain basis, replace any selected copy outside that union using Section 7. It cannot itself have been emitted, so the replacement is proper: the new copy is in the union and outside the old selected set. Each step preserves numeric feasibility, does not increase $p_k$, and strictly increases the number of selected copies in the union. At most $k$ steps suffice.

Therefore an optimum at this cardinality lies in the emitted union. Enumerate $k$-tuples of emitted positions, reject repeated physical copies, test the original numeric rows, and evaluate exact $p_k(S)$. For this final query mask positives outside $S$ and use the same positive-total $k$/zero-total $R-k$ face. Unit caps force all copies of $S$, and the oracle returns an attaining zero vector or rejects.

Optimize $k=0$ separately on the zero ground, and choose the least true scalar over cardinalities. An original optimum can be assumed to use its own least-cost zero completion because all numeric rows vanish on $Z$, so it is exactly represented by $p_k$. Every returned solution is checked on the original resource and rows. Optional outputs discard only the designated disposal coordinate; no true zero-weight unit, scalar contribution, or mandatory resource is discarded.

## 9. All-input running time

Use $L=q=1$ for counting when $m_U=0$, without constructing hashes. The count of possible emitted positions for a fixed cardinality obeys

$$
K_k^{\rm pos}
 \le Gkq(\Delta+1)(qB+1)^\Delta
 \le(\Delta B_0B+2)^{O(\Delta)}L^{\Delta+1}.
\tag{BF23}
$$

The unfiltered no-upper case satisfies this without hashes. Constants are absolute. Empty pools, reducible polynomials, invalid palette encodings, absent output indices, and duplicate copies can all be charged within this bound.

Enumerating at most $B_0$ positions costs

$$
(\Delta B_0B+2)^{O(\Delta B_0)}
        L^{(\Delta+1)B_0}\operatorname{poly}(H).
\tag{BF24}
$$

The row-count factor does not introduce a parameter-dependent polynomial exponent. For $a\ge1$,

$$
(\log(m+2))^a\le(a/e)^a(m+2)
\tag{BF25}
$$

with natural logarithms, by maximizing $x^ae^{-x}$. A change of base costs a constant to power $a$. Take $a=(\Delta+1)B_0\le2\Delta B_0$, and absorb its factor into BF24. This proves BF6 with a uniform polynomial factor in $H$. The cardinality loop and zero case do not change it.

All catalogue calls are exact algorithms, not promise procedures. Failed positions and infeasible tuples are explicitly counted. The resource computations use only the two integral ranks from Section 4.

## 10. Best completion without expanding zeros

For a fixed positive resource-independent vector $x$, define on $Z$

$$
h_x(A)=\min_{C\subseteq P}
                              (F(A\cup C)-x(C)).
\tag{BF26}
$$

Positive independence gives normalization $h_x(\varnothing)=0$. Monotonicity follows from $F$. For submodularity choose minimizing $C_1,C_2$, apply submodularity to $A_1\cup C_1,A_2\cup C_2$, and use modularity of $x$; the resulting union/intersection bounds dominate the corresponding minima. Thus $h_x$ is a monotone integral rank.

Compatible zero vectors are exactly $P(h_x)$, since the full inequalities are $y(A)+x(C)\le F(A\cup C)$ for $A\subseteq Z,C\subseteq P$. Also $h_x(Z)\le R-x(P)$. Full completion exists exactly when equality holds. Then signed minimum-weight greedy base optimization on $h_x$ returns the best completion. Each rank evaluation is an SFM on original coordinates with a binary modular term.

## 11. Uniform polynomial binary space

Let $n=|P|$, and distinguish $B_0$ from the potentially much larger maximum target $B$.

If $B_0=0$ or $n=0$, all positive counts vanish. Reject positive lower rows, and optimize the scalar on the zero resource retaining required total $R$. This is polynomial even with nonuniform signed zero coefficients.

If $B_0\ge n\ge1$, avoid copies and hashes. Stream all positive vectors $0\le x_e\le\lfloor B_0/w_e\rfloor$. There are at most $(B_0+1)^n\le(B_0+1)^{B_0}$. Test numeric rows and positive resource independence; use Section 10 for exact best completion. Retain only $n$ counters, one best output, and polynomial oracle workspace. This branch lies within BF6.

If $1\le B_0<n$, build at most $nB_0<n^2$ positive copies and keep zero counts compressed. The hash range $q=O(\Delta^2(B_0+1)^2L)$ is polynomial in explicit input size because frequency is at most the number of rows. Each threshold up to binary-large $B$ needs only $O(\log(B+1))$ bits.

Do not store the emitted union. A position records its actual class, monic polynomial, padded palette/thresholds, and an index in sorted $A\cap Y$. Replay the deterministic oracle and reject failed encodings. Each position needs

$$
O(\log(n+1)+\log q+
       \Delta(\log(q+1)+\log(B+1))+\log(k+1))
$$

bits. A tuple has at most $k\le B_0<n$ positions. The tuple, one replayed oracle problem, and the best binary output fit polynomial space. The count in Section 9 already includes invalid positions.

Denominator clearing, the BF14 reward, and deterministic ties have polynomial bit length. The conceptual full natural matroid and Rado zero dummies are never built. Binary-large $R$, zero capacities, and target thresholds do not cause unit expansion.

## 12. Matching lower order at frequency two

Let $b\ge2$, with ground the $b^2$ edges of $K_{b,b}$. Every edge has root weight one, root cap $B_0=b$, and each vertex supplies the equality $\sum_{e\ni v}x_e=1$. Thus frequency is two, nondistinguished targets are one, $B=b$, coefficients are zero-one, and scalar is zero.

Let $\mathcal H$ be the $b!$ perfect matchings. Distinct members cannot differ by one exchange: their symmetric difference is a union of alternating cycles of length at least four. Their intersection therefore has size at most $b-2$.

Define rank-$b$ matroid $M_\varnothing$ with bases all $b$-sets outside $\mathcal H$. For each hidden $A\in\mathcal H$, add $A$ as a base to obtain $M_A$. These are matroids. For allowed bases $C,D$ and $e\in C\setminus D$, if $D\setminus C$ is a singleton its only exchange is $D$. Otherwise at least two exchanges share $b-1$ elements, so at most one belongs to the forbidden subfamily; an allowed exchange exists.

All smaller sets are independent: a $(b-1)$-set has several extensions, at most one forbidden. Every larger set contains a base: the $b$-subsets of a $(b+1)$-set pairwise differ by one exchange and cannot all be forbidden. Hence the oracles for $M_\varnothing$ and $M_A$ differ only on the single query set $A$.

The vertex equalities force a perfect matching, in either the optional or mandatory model. The reference is infeasible and the hidden instance has unique feasible allocation $A$. Deterministic exact decision needs $b!$ worst-case rank queries. Under promise-search, an unqueried final output can save at most one, giving $b!-1$.

For randomized decision, put mass one half on the reference and one half on a uniformly random hidden $A$. A deterministic strategy with at most $D$ queries discovers at most $D$ hidden choices along the reference transcript. Its success is at most $1/2+D/(2b!)$. Thus bounded error at most one third requires $D\ge b!/3$, also giving the randomized worst-case query bound.

Since $b!\ge(b/2)^{b/2}$, the lower order is

$$
2^{\Omega(B\log(B+1))}.
\tag{BF27}
$$

The explicit numeric data have polynomial size in $b$. The hidden choice is available only through the rank oracle, not inspectable source. No lower bound for graphic/linearly represented resources, and no ETH claim, is inferred.

## 13. Scope boundaries and earlier increments

The root-charge condition is necessary for this parameterization. In the same lower construction make every root coefficient zero and set root cap one, keeping vertex targets one and rank $b$. Then $B=1$ and frequency two for arbitrarily large $b$, while the $b!$-query obstruction remains. Dropping BF4 invalidates oracle FPT in $B,\Delta$.

Unbounded frequency is another real boundary. The full-prefix SetCover reduction in *row_dependent_full_prefix_target_boundary.md* may be given the explicit cardinality root cap $k$, already implied by its uniform resource. Its maximum target remains $k+1$, but every column meets every universe row. Its W[2]-hardness in the largest target is consistent with BF6 because frequency is unbounded.

Common-weight set rows are a special case $a_{je}=w_e\mathbf1[e\in A_j]$. Their targets above the root cap can be simplified, so one may take $B=B_0$. No laminarity is then needed at small frequency. Conversely a laminar tree may have large depth/frequency and VZ's structural bound can be preferable. Neither bound dominates all instances.

For row-dependent weights, $B_0$ controls selected positive units and protected incidences, whereas $B$ controls capped coefficient diversity and palette thresholds. BF6 keeps that distinction. Signed numeric coefficients, cancellation-based root charges, a second unrelated resource, or an additional independent scalar side constraint are not covered.

## 14. Checked primary comparisons

These bounded comparisons delimit the claim; they do not establish publication priority.

- Huang and Ward, *FPT-Algorithms for the ell-Matchoid Problem with a Coverage Objective*, give deterministic fixed-parameter linear optimization in the general independence-oracle setting. Their joint representative theorem and kernel statement are Theorems 3.6–3.7 in the author PDF. This is an antecedent for resource-aware replacement, not a justification for treating weighted numeric rows as matroids. The present rows may have arbitrary integer coefficients, and $p_k$ is an optimal completion value.

  <https://www.di.ens.fr/~cchuang/work/matchoid.pdf>

- Bansal, Korula, Nagarajan and Srinivasan, *On k-Column Sparse Packing Programs*, explicitly parameterize column sparsity and give an $(ek+o(k))$-approximation for packing integer programs. That approximation theorem for unrestricted solution sizes is different from exact mixed quotas under a root cap. No general dominance over sparse-packing approximation methods is claimed.

  <https://www.cs.umd.edu/~srin/PDF/2010/k-sparse-conf.pdf>

  <https://arxiv.org/abs/0908.2256>

- Eisenbrand, Rohwedder and Węgrzycki, *Sensitivity, Proximity and FPT Algorithms for Exact Matroid Problems*, arXiv:2404.03747v2, describe guessing counts of weight vectors followed by partition-matroid intersection. Here sparse incidence and a positive root cap yield a catalogue with no parameter-dependent polynomial exponent in the number of upper rows. This is not a first-use claim for partition recovery.

  <https://arxiv.org/html/2404.03747v2>

- Husić, Loho, Smith and Végh, *On complete classes of valuated matroids*, TheoretiCS 3 (2024), Definition 1.1 and Theorem 2.9, provide the weighted Rado/network-induction property. The mapping and binary compressed oracle are proved in VZ and recalled in Section 4. Negating their maximum-valued exchange convention gives BF12.

  <https://theoretics.episciences.org/14792/pdf>

The algorithm uses no three-rank intersection assertion: every recovery is a single resource rank intersected with one partition rank, or the explicit residual rank BF26.
