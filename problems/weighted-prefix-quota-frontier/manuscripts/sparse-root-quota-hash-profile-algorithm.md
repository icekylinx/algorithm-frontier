# A direct hash-and-profile algorithm for sparse exact root-bounded quotas

**25 October 2026. Increment U. Complete manuscript-level proof with independent internal review.** This is a separate direct proof of the sparse model treated by [bounded-frequency-root-cap-valuated-fpt.md](bounded-frequency-root-cap-valuated-fpt.md). It does not invoke a representative catalogue, a valuated-matroid completion theorem, or an expansion into resource units.

## 1. Exact model and theorem

Let $F:2^E\to\mathbb Z_{\ge0}$ be an integral, normalized, monotone submodular function supplied by a value oracle. Write
$$
P(F)=\{x\in\mathbb R_{\ge0}^E:x(A)\le F(A)\ \forall A\subseteq E\},
\qquad R=F(E).
$$
The domain is either the integer points of $P(F)$, or the integer points of its base face $x(E)=R$. All counts, ranks, coefficients and targets are binary encoded.

A distinguished row is
$$
\sum_{e\in E} w_e x_e\le B_0,                                      \tag{HP1}
$$
where $w_e$ is a nonnegative integer. Every other row has nonnegative integer coefficients and one of the relations
$$
a^j x\le u_j,\qquad a^j x=\tau_j,\qquad a^j x\ge\ell_j.              \tag{HP2}
$$
All finite targets are nonnegative and at most $B$, where $B\ge B_0$. Each coordinate appears with a positive coefficient in at most $\Delta$ nonroot rows. We require
$$
w_e=0\ \Longrightarrow\ a^j_e=0\quad\hbox{for every nonroot row }j.  \tag{HP3}
$$
The scalar objective is one arbitrary signed rational linear functional $c^\top x$, minimized exactly. Maximization is obtained by replacing $c$ with $-c$. One further upper or lower threshold on this same scalar is consequently tested exactly; no simultaneous optimization of several arbitrary scalar objectives is asserted.

Let $H$ include the entire explicit row and coefficient encoding, the scalar encoding, and the bit lengths of rank values. There is a deterministic exact algorithm, with uniform polynomial binary space, taking
$$
2^{\,O((\Delta+1)B_0
 \log((\Delta+1)B_0(B+2)+2))}\mathrm{poly}(H)                 \tag{HP4}
$$
time and oracle calls when $B_0\ge1$. In particular, for $\Delta\ge1$ and $B_0\le B$, this is
$$
2^{O(\Delta B\log(\Delta B+2))}\mathrm{poly}(H).               \tag{HP5}
$$
The case $B_0=0$ is polynomial time.

The result is exact feasibility and exact scalar optimization. There is no quota violation, budget augmentation, or rounding error.

The companion *disjoint_row_root_target_sharp_lower.md* proves the sharp constant-frequency $B\log B$ boundary already for disjoint weighted equality rows of frequency one. The separate *valuated_sparse_quota_sunflower_kernel.md* supplies deterministic positive-capacity preprocessing for this same root-charged model.

## 2. Optional-to-base conversion and preprocessing

Optional resource use can be converted to a mandatory base without altering any real assignment or scalar cost. Add a disposal coordinate $z$, with all quota coefficients and scalar coefficient zero, and define
$$
F^+(A)=
\begin{cases}
 F(A),&z\notin A,\\
 R,&z\in A.
\end{cases}                                                     \tag{HP6}
$$
This is an integral polymatroid rank. Its integer bases are exactly
$(x,R-x(E))$ for integer $x\in P(F)$. Thus it suffices to solve the base problem, keeping the original total $R$. The disposal coordinate is included among the zero-root coordinates below. Mandatory inputs do not receive this disposal coordinate. From this point, $E,F$ denote the resulting base instance, with disposal included when needed.

Split each equality into an upper and a lower inequality. Let $\delta\le2\Delta$ bound the resulting number of nonroot positive incidences per coordinate. Delete zero lower targets. A zero upper target forbids every coordinate on which that row is positive. Also forbid a positive-root coordinate with $w_e>B_0$, or one individually exceeding an upper target. These operations impose coordinate bounds $x_e=0$; they do **not** reduce the required original total $R$.

For a positive lower target $\ell_j$, replace its coefficient by
$$
\bar a^j_e=\min\{a^j_e,\ell_j\}.                                  \tag{HP7}
$$
This is equivalent on integer nonnegative counts. Indeed, if a used coordinate has original coefficient at least $\ell_j$, one integer unit already meets the row; otherwise every used coefficient is unchanged. We use this equivalence only for integer witnesses and integer outputs, not as a claim about unchanged fractional feasible regions.

Let $P=\{e:w_e>0\}$ after permanent masks and let $Z$ contain the remaining zero-root coordinates. Every feasible solution uses
$$
k=x(P)\le B_0.                                                   \tag{HP8}
$$
Every positive lower row needs at least one used coordinate with positive coefficient. Consequently the number $m_L$ of positive lower rows must satisfy
$$
m_L\le\delta B_0.                                                \tag{HP9}
$$
If this fails, or a positive lower row has no permitted coordinate, the instance is infeasible. Empty upper rows can be deleted.

If $B_0=0$, every positive-root coordinate is forbidden. Positive lower requirements then make the instance infeasible; otherwise the remaining problem is exact signed linear optimization on the original-total resource face restricted to $Z$, a polynomial-time problem. This handles $R=0$ as well.

From now on $B_0\ge1$. No allocation of an array of length $B_0$, $B$, or $R$ is used.

## 3. A polynomial-size family of hashes for used upper rows

Let $m_U$ be the number of remaining upper rows. A feasible solution touches at most
$$
K=\min\{\delta B_0,m_U\}                                        \tag{HP10}
$$
different upper rows. If $m_U=0$, omit hashing and all upper-color data.

For $m_U\ge1$, encode the upper-row IDs as distinct binary polynomials of degree less than
$$
L=\lceil\log_2(m_U+1)\rceil.
$$
Choose a power of two $q=2^d$ satisfying
$$
4(K+1)^2(L+1)\le q<8(K+1)^2(L+1).
$$
For every monic binary polynomial $g$ of degree $d$, define
$$
h_g(j)=j(X)\bmod g(X),                                          \tag{HP11}
$$
regarded as a $d$-bit color.

This family has $q$ hashes. For every set of at most $K$ upper-row IDs, one hash is injective on it.

To prove the last statement, it is enough to consider the irreducible polynomials among the enumerated moduli. There are at least $2^{d-1}/d$ monic irreducibles of degree $d$. Each nonzero difference of two row-ID polynomials, of degree less than $L$, has fewer than $L/d$ irreducible degree-$d$ divisors. At most
$\binom K2 L/d$ irreducibles can therefore cause a collision on the prescribed set. The displayed choice of $q$ leaves an irreducible that causes none.

For completeness, the standard count used here follows from
$2^d=\sum_{s\mid d}sN_s$, with $N_s$ the number of monic degree-$s$ irreducibles, and $sN_s\le2^s$. The sum for proper divisors is bounded by
$\sum_{s=1}^{\lfloor d/2\rfloor}2^s\le2^{d-1}$; the few smallest degrees satisfy the same inequality directly.

**Implementation precision.** Irreducibility need not be tested. We enumerate all monic degree-$d$ polynomials, since polynomial remainder is defined for every such modulus and the existence proof guarantees a good irreducible somewhere in the list. Moreover $K\le m_U$, so $q$ is polynomial in the explicit row input, even when $B_0$ is numerically enormous. Only colors actually occupied by input rows are stored.

## 4. Guessing used colors and their capacities

Fix one hash $h$. Enumerate every palette $\mathcal C$ of at most $K$ actually occupied colors, and every map
$$
\beta:\mathcal C\to\{1,\ldots,B\}.                               \tag{HP12}
$$
A positive coordinate $e$ is retained in this iteration only if:

1. every upper row incident with $e$ has its color in $\mathcal C$;
2. for every incident upper row $j$, $u_j\ge\beta_{h(j)}$.

For a retained coordinate, form its hashed coefficient vector
$$
b_{e,t}=\sum_{\substack{j\text{ upper}\\h(j)=t}}a^j_e
 \qquad(t\in\mathcal C).                                        \tag{HP13}
$$
If $b_{e,t}>\beta_t$ for some $t$, mask $e$ in this iteration as well.

The sum in HP13 is essential. When several actual upper rows collide, using the maximum coefficient or retaining one arbitrary row would not justify the soundness proof below.

Each remaining positive coordinate has a type
$$
\mathrm{type}(e)=
\left(w_e,\;(\bar a^j_e)_{j\text{ lower}},\;
                (b_{e,t})_{t\in\mathcal C}\right).               \tag{HP14}
$$
Group the **actual input coordinates** by these types. The zero-root coordinates form one separate group. All their nonroot coefficients are zero by HP3.

## 5. Exact profiles and one integral recovery problem

Let the actual positive type groups be $E_1,\ldots,E_M$. Enumerate nonnegative integer counts $n_1,\ldots,n_M$ with total
$k=\sum_i n_i\le\min\{B_0,R\}$. Keep a profile only if:

- its root-weight sum is at most $B_0$;
- its capped lower coefficient sum meets every lower target;
- for every palette color $t$, its hashed coefficient sum is at most $\beta_t$.

For each kept profile impose group upper bounds
$$
x(E_i)\le n_i\quad(1\le i\le M),\qquad x(Z)\le R-k,               \tag{HP15}
$$
and forbid all coordinates masked in this iteration. Intersect these partition bounds with the original resource polymatroid and require
$$
x(E)=R.                                                        \tag{HP16}
$$
The caps in HP15 sum to $R$; therefore HP16 forces every group bound to equality. This remains correct if a prescribed group is empty, if $Z$ is empty, or if restriction has lowered the available resource rank: the intersection then correctly reports infeasibility where necessary.

Both the resource rank and the partition rank are integral polymatroids. Their intersection is integral. Linear optimization on its maximum-total face, using the signed objective $c^\top x$, is polynomial time with the usual rank/submodular-minimization oracles and rational linear optimization. Thus a successful profile returns an actual integer point of exact minimum scalar value on that profile.

This is the only recovery operation. It jointly determines positive counts and all zero-root completion, pays all their true scalar contributions, and preserves the original required base total. No auxiliary scalar objective is optimized in place of the true one.

## 6. Soundness, completeness and exact optimization

### Soundness

Take an output of a successful profile. Its root and lower rows hold by the profile checks and the integer equivalence HP7.

Consider an actual upper row $j$. If no permitted coordinate touches it, its load is zero. Otherwise $h(j)\in\mathcal C$, and every selected incident coordinate passed the guard $u_j\ge\beta_{h(j)}$. Its total actual row load satisfies
$$
\sum_e a^j_e x_e
 \le\sum_e b_{e,h(j)}x_e
 \le\beta_{h(j)}
 \le u_j.                                                       \tag{HP17}
$$
The first inequality follows from nonnegativity and HP13. It remains valid when many unrelated actual rows collide. Both halves of each original equality therefore hold.

Resource feasibility, original total and actual scalar cost are guaranteed by HP15–HP16. Optional inputs are recovered by dropping disposal only.

### Completeness

Fix any feasible original integer witness $x^*$, not necessarily one of optimal scalar value. Let $J^*$ be its touched upper rows. By HP8–HP10, $|J^*|\le K$. Select a hash injective on $J^*$, let
$\mathcal C=h(J^*)$, and set
$$
\beta_{h(j)}=u_j \quad(j\in J^*).                                \tag{HP18}
$$
These choices are among the enumerated iterations.

Every used positive coordinate passes the incident-row capacity guards, and its hashed coefficients at used colors equal its actual coefficient on the unique corresponding touched upper row. In particular it passes the individual hashed-capacity masks. Its actual type counts satisfy all profile checks. The original witness, including its zero-root coordinates and disposal if present, belongs to HP15–HP16 for that profile.

### Scalar optimum

Apply completeness to a scalar-optimal original witness. The exact optimizer for its profile has objective at most that witness's value. Every output is feasible for the original problem, so taking the best output gives precisely the original optimum. If every profile fails, no feasible witness exists.

The proof therefore establishes an exact algorithm, rather than only a promise oracle or a one-sided gap procedure.

## 7. Time bound, including unsuccessful iterations

For a fixed hash, the number of palette/cap choices is at most
$$
\sum_{h=0}^{K}\binom{q}{h}B^h\le(qB+1)^K,                       \tag{HP19}
$$
with the usual value $1$ when $K=0$. Counting only occupied colors can only reduce this number.

Each type has root weight in $[B_0]$, at most $\delta$ nonzero lower entries, and at most $\delta$ nonzero upper-color entries; all these entries are at most $B$ after the guards. Also $m_L,|\mathcal C|\le\delta B_0$. A convenient upper bound for the total possible type count is
$$
M_{\max}\le
 B_0(1+\delta B_0B)^{2\delta}.                                   \tag{HP20}
$$
For $\delta=0$, interpret the right side as $B_0$.

The number of all type-count profiles of total at most $B_0$, including profiles that fail numerical checks or fail resource recovery, is at most
$$
\binom{M_{\max}+B_0}{B_0}
 \le\left(\frac{e(M_{\max}+B_0)}{B_0}\right)^{B_0}.                \tag{HP21}
$$
We use the actual $M\le |E|$ groups to enumerate. A depth-first traversal with partial total at most $B_0$ has at most $M+1$ times the number of final count vectors: every partial vector extends by zeros, so each fixed-depth prefix has an injective zero-extension into the final vectors. Numerical pruning only decreases the work. This charges unsuccessful profiles and all partial enumeration work.

Using $q=O((K+1)^2\log(m_U+2))$, HP19–HP21 give an exponential contribution bounded by HP4, apart from a factor
$(\log(m_U+2))^{O(K+1)}$. This is absorbed into the same parameter dependence and a fixed polynomial in the explicit input. For $a\ge1$ and $y\ge1$,
$$
y^a\le(a/e)^a e^y;
$$
apply it with $y=\ln(m_U+2)$ and adjust constants for the logarithm base. The exponent of the final polynomial in $H$ is independent of $\Delta,B_0,B$.

The $q$ hashes and every rank/optimization call have the already charged polynomial factors. Since $\delta\le2\Delta$, this proves HP4–HP5.

## 8. Uniform polynomial binary space

The algorithm does not materialize the possible-type bound HP20, a hash-range array of length $q$, or any natural-matroid unit expansion.

- A hash is stored as its degree-$d$ modulus. Row hashes are polynomial remainders of binary row IDs.
- Palettes are subsets of the actually occupied row colors, at most $m_U$ in number. Their capacities are binary counters.
- Actual types are computed from at most $|E|$ input coordinates, using the explicit lower rows and occupied palette.
- Count enumeration has depth at most $|E|$, with binary counters of $O(\log(B_0+1))$ bits.
- The full resource total $R$ appears only in binary arithmetic and in the original-total face. Zero-root multiplicity is not expanded.
- Integral-polymatroid intersection and rational linear optimization use polynomial input/oracle working space.

Thus the space is polynomial in the original input encoding even when $B_0,B,R$ greatly exceed the number of coordinates. No separate large-$B_0$ enumeration fallback is needed for this direct algorithm.

## 9. Public antecedents and the appropriate comparison

This proof uses standard color coding / separating hashes, exact count profiles, and weighted integral-polymatroid intersection. It should not be described as a new representative-family paradigm.

A close deterministic framework antecedent is van Bevern, Tsidulko and Zschoche, *Representative families for matroid intersections, with applications to location, packing, and covering problems*, Discrete Applied Mathematics 298 (2021). Their Section 5 uses perfect hash families, color-partition enumeration, and matroid intersection with arbitrary oracle facility matroids; their general set-packing theorem separately requires linear representations. See [the primary full version](https://arxiv.org/html/1806.11527v4), Proposition 5.9, Lemma 5.7 and Proposition 5.12.

Huang, Kakimura, Kobayashi and Terao, *Polynomial Kernels with Reachability for Weighted d-Matroid Intersection* (2026), already prove a randomized $O(k^3\log k)$ reachable kernel for weighted matching subject to one arbitrary matroid on the edges. Enumerating its $k$-subsets gives a $2^{O(k\log k)}$ exact parameterized algorithm. Their [primary Section 6](https://arxiv.org/html/2603.17345v1) is an important existing special case; the present theorem does not first establish that endpoint.

For arbitrary weighted two-row-incidence demands, Ahmadian and Friggstad's [ICALP 2017 paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2017.55) already studies generalized demand matching under an arbitrary oracle matroid, with approximation and bicriteria guarantees. That model is a direct antecedent for weighted sparse packing, while the guarantee and parameterization differ.

Finally, the $\Delta=2$, unit-upper-capacity subclass already contains matroid-constrained bipartite matching. The grid/G-matroid construction in Doron-Arad, Kulik and Shachnai, [*You (Almost) Can't Beat Brute Force for 3-Matroid Intersection*](https://arxiv.org/html/2412.02217v2), specializes to the hidden perfect-matching family of size $k!$. It yields the $2^{\Omega(B_0\log B_0)}$ oracle obstruction on that subclass. No new lower-bound priority is claimed here.

The present proof's explicit additional scope is the simultaneous combination of row-dependent bounded integer coefficients, mixed exact relations, a bounded positive root mass, arbitrary many rows, a binary integral-polymatroid resource with original base totals, and arbitrary signed scalar costs on zero-root completion. This is a verified internal theorem with identified antecedents; this bounded source check is not an exhaustive novelty determination.

## 10. What this proof does not claim

- Root-zero coordinates may not occur positively in other quota rows.
- The frequency bound is on nonzero **column** incidences, not on the number of coordinates inside a row.
- Arbitrary large nonnegative coefficients are allowed in the input, but upper-ineligible coordinates are masked and lower coefficients are capped against the integer target before type enumeration.
- The exact scalar is one functional. Several independent arbitrary rational budgets are not covered by this scalar optimization statement.
- The theorem does not replace its parameterized exponential time by polynomial time.
- The direct proof is independent of the valued exchange proof; agreement of their bounds is an internal cross-check, not evidence of external priority.
