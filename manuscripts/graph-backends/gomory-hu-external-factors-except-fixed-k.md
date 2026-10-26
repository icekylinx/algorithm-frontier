# Quantified outer Gomory--Hu factors and the fixed-k resolution

**Source-interface audit, 25 October 2026.** This note separates the
quantitative public imports from the constructive fixed-parameter
guide-tree mincut interface. The latter is now supplied by the new
global-max leaf adapter in
[deterministic-fixed-k-tree-mincut-adapter.md](deterministic-fixed-k-tree-mincut-adapter.md), with separate
independent audits. The historical filename is retained so existing
checkpoint links remain valid.

Put $U=\log(N+4)$, $h=\log(U+4)$. Every graph below has actual
size at most polynomial in the original input bound $N$. All work
bounds multiply actual sizes; the master parameter does not justify
padding a small recursive instance.

## 1. Hit-and-miss families have a fixed polynomial cost

Theorem 3.5 of
[AKL+, arXiv:2507.20354v1](https://arxiv.org/html/2507.20354v1)
states its precise dependency, citing CP24 Definition 4 and Theorem
3.1. For miss size $a$, hit size $b=O(1)$, and universe size
$n$, the family size is

$$
(a\log n)^{O(b)},
 \qquad\text{construction time }n(a\log n)^{O(b)}.
 \tag{1}
$$

The Section 6 calls always use $b=2$ and
$a=\widetilde O(\psi^{-1})$. Consequently their cost is a fixed
power of $\psi^{-1}$ and of $U$. There is no additional
unspecified subpolynomial factor from this component.

One can also replace this import by an elementary construction when
only a fixed hit size is needed. Enumerate sufficiently many small
primes $p$, and for every subset $R\subseteq\mathbb Z_p$ of
size at most $b$, use the function
$x\mapsto 1[x\bmod p\in R]$. For fixed disjoint sets $A,B$,
the nonzero integer

$$
\prod_{x\in A,y\in B}(x-y)
 \tag{2}
$$

has at most $ab\log_2 n$ distinct prime divisors. Among more than
that many primes, one makes every residue of $B$ distinct from
every residue of $A$. Choosing $R=B\bmod p$ separates them.
The standard polynomial bound on the first $O(ab\log n)$ primes,
and a deterministic sieve, give family size and time
$(a\log n)^{O(b+1)}$ and
$n(a\log n)^{O(b+1)}$, respectively. For $b=2$, these are still
the required fixed polynomial bounds. Empty hit sets are covered by
the zero function.

## 2. Weighted expander decomposition has a uniform parameter

AKL+ Appendix A quotes a fixed-constant accuracy statement and then
uses a vanishing accuracy. To avoid any uncertainty from that wording,
use the original uniform formulation of Li--Saranurak,
[arXiv:2106.01567](https://arxiv.org/pdf/2106.01567), Theorem 2.4 and
Corollary 2.5. The parameter $r\ge1$ is an explicit input. Its
weighted balanced-cut/prune quality is

$$
\log^{O(r^4)}N.
 \tag{3}
$$

The stated time is $m(mW)^{O(1/r)}$, up to logarithms. For a
conservative construction-level estimate, retain also the factors
visible in the proof: its spectral routine has
$\log^{O(r^2)}N$ overhead, and its recursive j-tree work has
$\log^{O(r)}(NW)$ overhead. Neither factor is iterated through a
second growing-depth application. A sufficient uniform bound is

$$
m\exp O\left(U/r+r^4h\right)
 \tag{4}
$$

for polynomial external weights and demands. The internal capacity
ratios may grow by $N^{O(r)}$, as explicitly bounded in the proof
of its Theorem 2.14. This uses $O(rU)$ numerical bits and only
polynomial logarithmic arithmetic factors, consistent with (4).

Take $r=\Theta((U/h)^{1/5})$, rounded to an integer. Both the
work factor and cut-quality factor are bounded by

$$
E_{\rm dec}=\exp O(U^{4/5}h^{1/5}).
 \tag{5}
$$

The weaker $\exp O(U^{4/5}h^{O(1)})$ envelope is enough for the
7/8 composition.

For completeness, arbitrary positive target expansion $\phi$ is
compatible with the primitive's normalization $\psi\le1$. Set
$\beta=\max\{1,\phi\}$, multiply every nonzero demand by
$\beta$, and use target $\psi=\phi/\beta$. The resulting
inequality is exactly the desired $\phi$-expansion for the original
demands. Recursively applying the balanced-cut/prune primitive gives
the needed decomposition with only a logarithmic factor in its quality
and total actual instance inventory. Demands and capacities remain
polynomially bounded at the external interface. This route does not
need to substitute a parameter outside the range of a fixed-constant
statement.

## 3. The flow-linked refinement in AKL+ Appendix A

The remainder of that appendix uses the preceding decomposition and
exact maxflow on linear-size graphs, followed by recursive calls on
vertex-disjoint induced graphs. Its recursion depth is
$O(\log(nW))$. Hence its total actual edge inventory is
$m\operatorname{poly}(U)$.

Choose all displayed approximation envelopes as powers of two. The
target $\phi$ used in Section 6 can also be chosen dyadic. The
auxiliary flow capacities have common factors such as
$1/(12\alpha)$ and $\phi/2$. Multiplication by one common
polynomially bounded denominator converts each flow call to positive
polynomially bounded integer capacities. There is no accumulation of
unrelated denominators across recursive calls.

With a deterministic exact-flow factor
$E_{\rm flow}=\exp O(U^{4/5}h^{O(1)})$, the refinement costs

$$
m\operatorname{poly}(U)
             \bigl(E_{\rm dec}+E_{\rm flow}\bigr),
 \tag{6}
$$

and its source/sink routing guarantee loses only an additional
polynomial logarithm. Both its work and its structural factor therefore
have leading logarithmic power at most $4/5$.

This paragraph uses the correctness of the public flow-linked
refinement as an imported lemma. The quantitative substitution has been
checked independently: it does not silently use a more expensive
maxflow black box or multiply construction work once per recursion
level in the exponent.

## 4. The terminal-selection loops have bounded fixed nesting

AKL+ Section 6 defines $\psi^{-1}$ as a fixed power of its
expander factor and logarithms. The displayed loops in DetectCC,
DecompFirstStep, and DecompSecondStep have counts polynomial in
$\psi^{-1}$ and $U$. Their hit-and-miss families are covered by
Section 1. Every isolating-cut invocation reduces to exact maxflow on
graphs of total size $m\operatorname{poly}(U)$.

Full SSMC makes $O(\log(nW))$ calls to partial SSMC. A call to
GHTreeStep performs a polynomial logarithmic number of the preceding
selection and decomposition operations. None of these levels has depth
growing as $\psi^{-1}$ with a recursively multiplied oracle work
factor. They are finite nested loops with fixed nesting depth.

Consequently, using the partial-SSMC implementation assembled from the
audited guide construction and the new fixed-k adapter, the complete
GHTreeStep work is

$$
m\operatorname{poly}(U)E^{O(1)}
       E_{\rm dec}^{O(1)}E_{\rm flow}^{O(1)}.
 \tag{7}
$$

## 5. The final recursive inventory

AKL+ Lemma 6.32 gives total vertex and edge inventories
$O(dn)$ and $O(dm+dn\log n)$, respectively, for recursion
depth $d$. The terminal sets shrink by a fixed fraction, so
$d=O(\log n)$. Combining this bound with (7), using actual local
sizes and a common monotone upper envelope for their factors, adds only
a polynomial logarithm.

The term $n\log n$ is harmless on a connected nontrivial input,
where $n\le m+1$. General inputs are first divided into connected
components and isolated vertices, so their additional processing and
output cost is $O(n+m)$.

## 6. Resolution of the fixed-parameter mincut interface

The fixed-parameter guide-tree mincut reduction connects the guide
family to partial SSMC. AKL+ Theorem 5.2 states a
deterministic almost-linear bound and refers its runtime analysis to
Zhang,
[arXiv:2112.01042](https://arxiv.org/pdf/2112.01042), Section 2.4.
Zhang's displayed recurrences give polylogarithmic aggregate maxflow
inventory for fixed respect parameter. However, the two papers' source
arm contractions are not identical. Some literal variants preserve
correctness but duplicate an uncovered Steiner region between two
same-parameter recursive calls; other literal variants restore the
inventory inequality while requiring an additional correctness
argument for a cut that separates the two ends of the source arm.

The audit therefore does not transfer the inventory bound by assertion.
Instead, [deterministic-fixed-k-tree-mincut-adapter.md](deterministic-fixed-k-tree-mincut-adapter.md) supplies a
modified construction. After all lower-k calls, its leaf routine
maximizes the candidate value over every non-source, non-centroid guide
target, including the source arm. A source-arm maximizer gets one full
child; an outside maximizer gets two children with disjoint
uncontracted regions. The proof establishes both the required cut
cases and $\sum_i(n_i-1)\le n-1$. Correct contracted-target
broadcasts and a set-mincut parameter-one base complete the interface.

The resulting aggregate maxflow input size is
$(m+n)\log^{O(k+1)}n$. For the fixed $k=16$, it multiplies
the exact-flow factor by only a fixed polynomial logarithm. This new
construction is independently checked in
[fixed-k-global-max-leaf-independent-audit.md](fixed-k-global-max-leaf-independent-audit.md). It closes the earlier
conditional boundary and, together with the preceding factors,
completes the explicit 7/8 Gomory--Hu proof assembly.
