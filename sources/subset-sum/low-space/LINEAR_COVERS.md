# Linear translate covers with a paid geometric replay bound

Author: Yilin Liu. Assistance: OpenAI Codex, including GPT-6 Astra.

The final trace-mass consequence uses the inequality proved in [the manuscript](../../../proof.md), Sections II.2.1–II.2.2. The translate-cover theorem and its construction below are independent of that premise.

Let $V=\mathbb F_2^c$, let $\varnothing\ne G\subseteq V$, and suppose membership in $G$ takes deterministic time $Q$ and workspace $W$. Write $N=2^c$ and $\alpha=|G|/N$. There is a deterministic algorithm returning a basis for a subspace $H\le V$ such that

$$
G+H=V,\qquad
K:=|H|\le\min\left\{2^c,\frac{2(1+c\ln2)}{\alpha}\right\}.
\tag{LCV-1}
$$

Its time is $O^*(2^cKQ)$ and its space is $O^*(W+\operatorname{poly}(c))$. A basis permits enumeration of all centers with polynomial delay and state. All arithmetic in the construction has polynomial bitlength.

Start with $H=\{0\}$ and let $U=V\setminus(G+H)$. Adding a vector $v$ to the basis replaces the uncovered set by $U\cap(U+v)$. Counting ordered pairs in $U^2$ gives

$$
\frac1N\sum_{v\in V}|U\cap(U+v)|=\frac{|U|^2}{N}.
\tag{LCV-2}
$$

Choose $v$ whose intersection size is no larger than this average. If $U\ne\varnothing$, then $0<|U|<N$. Such a choice strictly decreases $|U|$, and cannot lie in $H$, since $U$ is $H$-invariant. Consequently the subspace doubles at every successful step. After $d$ steps,

$$
|U_d|/N\le(1-\alpha)^{2^d}\le e^{-\alpha2^d}.
\tag{LCV-3}
$$

The first power of two at least $(1+c\ln2)/\alpha$ makes the integer $|U_d|$ smaller than one. Alternatively rank $c$ gives $H=V$. This proves (LCV-1). The algorithm stops by exact counting, without evaluating a real logarithm.

To choose $v$, fix its bits by conditional expectation. For a prefix length $j$, let $U_a$ be the number of uncovered vectors with prefix $a\in\mathbb F_2^j$. If $v$'s prefix is $P$, then

$$
\mathbb E[|U\cap(U+v)|\mid v|_{[j]}=P]
 =2^{-(c-j)}\sum_a U_aU_{a+P}.
\tag{LCV-4}
$$

For each uncovered $x$ with prefix $a$, its translated suffix is uniform in the suffix class with prefix $a+P$; this proves the formula. The two next-bit means average to the current mean. Choose the smaller, using their common-denominator integer numerators. The uncovered predicate remains unchanged until all bits of the new vector have been chosen.

Membership in $U$ is decided by enumerating the present $H$ and testing $x+h\notin G$ for every $h$. For one candidate prefix, enumerate each $a$, count $U_a$ and $U_{a+P}$ by scanning their suffix classes, multiply the two counts, then discard them. The suffix classes partition $V$, so this is at most two full passes, with time $O^*(N|H|Q)$ and space $W+\operatorname{poly}(c)$. The score has at most $2c+1$ bits. The $c$ bit choices add a polynomial factor. Across stages the current subspace sizes are $1,2,\ldots,K/2$, whose sum is less than $K$. Exact stopping tests, including a final full pass, obey the same bound. This proves the claimed time and space.

If $G$ lies in the cardinality layer $\binom{[c]}r$, test cardinality before the expensive predicate, whose time and state on this layer are $Q_r,W_r$. For each fixed $h$, exactly $\binom cr$ of the $N$ translated vectors in a full pass have cardinality $r$. The preceding proof therefore gives the sharper bound

$$
T=O^*\!\left(K\left[2^c+\binom cr Q_r\right]\right),
\qquad S=O^*(W_r+\operatorname{poly}(c)).
\tag{LCV-5}
$$

For a dyadic class defined by distinct subset-sum support, sorted half-sum streaming gives $Q_r=O^*(2^r)$, $W_r=O^*(2^{r/2})$. The cardinality test charges all failed masks; early successful membership tests only reduce the count.

For completeness, suppose the fixed-layer trace mass is
$T_r=\sum_{|T|=r}N(T)$, and a class
$G_\ell=\{T:|T|=r,\ 2^\ell\le N(T)<2^{\ell+1}\}$
satisfies
$\ell+\log|G_\ell|\ge\log T_r-O(\log c)$.
The cover gives
$K|G_\ell|\le\operatorname{poly}(c)2^c$, hence

$$
\ell-\log K\ge\log T_r-c-O(\log c).
\tag{LCV-6}
$$

If $r=\theta c+O(1)$ and an independently proved trace inequality gives

$$
\log T_r\ge h(\theta)c+\theta c-(\theta-\gamma)d-O(\log c),
$$

then $\ell\le r$ implies
$\log K\le[1-h(\theta)]c+(\theta-\gamma)d+O(\log c)$.
When $h(\theta)+\theta>1$, substitution in (LCV-5) gives

$$
T=O^*\!\left(2^{(1+\theta)c+(\theta-\gamma)d}\right),
\qquad
S=O^*(2^{\theta c/2}+\operatorname{poly}(c)).
\tag{LCV-7}
$$

The trace inequality is an explicit premise of this last consequence; the translate-cover theorem itself requires only a decidable nonempty set. Its basis representation compresses the center description, while subsequent per-center histograms, seed caches and generator scans retain their actual $K$ multiplicity.
