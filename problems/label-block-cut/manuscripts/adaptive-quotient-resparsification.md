# Adaptive resparsification removes the ambient ground-set logarithm

**Abstract.** Adaptive repeated application of quotient sparsification removes the original ground-set size from the support logarithm. The proof controls restriction, accumulated multiplicative error, conditional failure probability, and the bit length of repeated rational reweightings.

## Theorem

**Theorem 1 (adaptive quotient resparsification).** Let $f:2^E\to\mathbb R_{\ge0}$ be normalized, monotone, and submodular, with every positive marginal at least one and total rank $r=f(E)$. For nonnegative rational item weights and $0<\varepsilon<1$, a randomized algorithm preserves the weight of every quotient within $1\pm\varepsilon$, simultaneously, on

$$
O\!\left(\min\left\{|E|,\frac{r\log(2r/\varepsilon)}{\varepsilon^2}\right\}\right)
$$

original items, with probability at least $2/3$. It uses $O(\log\log(2|E|))$ calls to Quanrud's quotient-sparsification backend and polynomially many additional oracle operations. The zero-rank case returns the empty summary. For an exact rational rank oracle with a fixed common denominator polynomial in the rank, the construction has polynomial bit complexity under the value-oracle contract in QB4.

**Proof.** QB1 states the external backend with its required confidence. QB2 proves that every original query remains a quotient after restriction. QB3 supplies error parameters whose sum is independent of the input ground-set size. QB4 bounds the total failure probability and accumulated rational encoding length. These steps prove the theorem. The support improvement is an adaptive consequence of the existing quotient theorem.

## QB1. The public backend

Let $f:2^E\to\mathbb R_{\ge0}$ be normalized and monotone submodular. Suppose every nonzero marginal value is at least one, let $r=f(E)$, and let the elements have arbitrary nonnegative weights. A set is closed if it contains every element with zero marginal relative to it. A quotient is the complement of a closed set.

Quanrud's SODA 2024 theorem gives, in randomized polynomial time with an evaluation oracle for $f$, a nonnegative reweighting supported on
$$
O\!\left(\frac{r\log(mr)}{\eta^2}\right),\qquad m=|E|,
$$
that preserves the weight of every quotient to relative error $\eta$. The source is:

- Kent Quanrud, *Quotient sparsification for submodular functions*, Theorem 1.1 and Section 3: <https://kentq.s3.amazonaws.com/submodular-sparsification.pdf>.

We use the following conventional quantified form of that theorem. For one absolute constant $A$, a call at error $\eta\in(0,1)$ has both the desired quotient guarantee and support at most
$$
A r\eta^{-2}\log(2mr)
 \tag{QB1}
$$
except with probability at most $(2m)^{-4}$. Increasing the absolute sampling constant supplies this form. This is directly justified by the proof of Lemma 3.3: its failure bound is $(mr)^{-c_3}$, and its footnote explicitly permits arbitrarily large fixed exponents by decreasing the threshold constant. Lemma 3.4 takes a union bound over at most $m$ strength levels, and the concluding Chernoff bound also controls the support. No variable confidence parameter is needed below.

The cases $r=0$, an empty support, and a support of size at most one can be handled exactly.

## QB2. Restrictions preserve the old query family

Let $S$ be closed for $f$, and let $T\subseteq E$ be an arbitrary retained support. Then $S\cap T$ is closed for the restriction $f|_T$.

Indeed, if $e\in T\setminus S$, closedness gives
$$
f(e\mid S)>0.
$$
Since $S\cap T\subseteq S$, submodularity gives
$$
f(e\mid S\cap T)\ge f(e\mid S)>0.
$$
Every element already in $S\cap T$ has zero marginal to that set. Thus its closure inside $T$ is exactly $S\cap T$. Consequently, if $Q$ is an original quotient, then $Q\cap T$ is a quotient of the restricted function.

This is also the restriction property recorded in Quanrud's Lemma 2.1. Therefore quotient approximations compose through arbitrary successive supports. The rank can only decrease; using the original $r$ as an upper bound is harmless. The lower bound of one on nonzero marginals is inherited by restriction.

## QB3. Adaptive error allocation

Here and below logarithms are natural. Fix $\varepsilon\in(0,1)$. Increase the absolute constant $A$ in (QB1) if necessary so that $A\ge1$, and define
$$
Z=\frac{65536 A r}{\varepsilon^2},\qquad
 \beta=8\log(2Z),\qquad B=e^\beta=(2Z)^8.
 \tag{QB2}
$$

Maintain the current weighted restriction, with current support size $m_i$.

While $m_i>B$, write $t_i=\log m_i$, and invoke the backend with an error parameter $\eta_i$ satisfying
$$
\frac{\varepsilon}{128}\sqrt{\frac{\beta}{t_i}}
 \ \le\ \eta_i\ \le\
 \frac{\varepsilon}{64}\sqrt{\frac{\beta}{t_i}}.
 \tag{QB3}
$$
A dyadic rational in this interval suffices. Keep the returned support and weights. If the backend exceeds its stated support cap, terminate with a failure flag; this event is already included in its failure budget.

Once $m_i\le B$, perform one final backend call with error $\varepsilon/4$.

The preliminary calls shrink the logarithm of the support by at least a factor of two. To see this, $m_i>B$ implies $m_i\ge r$, so
$$
\log(2m_i r)\le 2t_i+\log 2\le 3t_i.
$$
Using (QB1) and the lower bound in (QB3), the new support satisfies
$$
m_{i+1}\le \frac{Zt_i^2}{\beta}.
 \tag{QB4}
$$
For $t\ge\beta$, one has
$$
\log Z+2\log t-\log\beta\le t/2.
 \tag{QB5}
$$
For completeness, the difference between the right and left sides has derivative $1/2-2/t\ge0$ on this range. At $t=\beta$, the needed inequality is $\log Z+\log\beta\le\beta/2$, which follows from $\beta=8\log(2Z)$ and $Z\ge1$. Hence
$$
m_{i+1}\le\sqrt{m_i},\qquad
 t_{i+1}\le t_i/2.
 \tag{QB6}
$$
There are $O(\log\log(2m))$ preliminary calls.

Even though the number of calls depends on the original ground-set size, their error sum does not. If $s$ preliminary calls are made, repeated use of (QB6) gives
$$
\sum_{i=0}^{s-1}\eta_i
 \le \frac{\varepsilon}{64}
       \sum_{j\ge0}2^{-j/2}
 =\frac{\varepsilon}{64(1-2^{-1/2})}
 <0.054\varepsilon.
 \tag{QB7}
$$
Adding the final error $\varepsilon/4$ makes the sum less than $0.304\varepsilon$. For every original quotient, the total lower multiplicative factor is at least one minus this sum, and the upper factor is at most the exponential of this sum. Since $0<\varepsilon<1$, both bounds lie within $1\pm\varepsilon$.

The final support is at most
$$
O\!\left(
 \frac{r\log(2Br)}{\varepsilon^2}
 \right)
 =
 O\!\left(
 \frac{r\log(2r/\varepsilon)}{\varepsilon^2}
 \right).
 \tag{QB8}
$$
As usual, return the input itself if it is already smaller than the claimed target.

## QB4. Probability and computation

Use fresh randomness at every call, conditionally on the current restriction and its current weights. The source theorem applies to each such instance. The size checks ensure (QB6) along every nonterminated execution, independently of whether some quotient guarantee has silently failed.

Read the preliminary sizes backward from the last one. They are bounded below by $B,B^2,B^4,\ldots$. Therefore the sum of their conditional failure budgets is at most
$$
\sum_{j\ge0}(2B^{2^j})^{-4}<1/100.
 \tag{QB9}
$$
This pathwise bound also bounds the expectation of the sum of conditional failure probabilities. The final call has failure probability at most $1/100$ after a fixed adjustment to the sampling constant; tiny supports are treated exactly. Thus success probability $2/3$, or any other fixed constant below one, follows without inserting a logarithm of the number of calls into the support.

The requested inverse errors are at most
$$
O\!\left(\varepsilon^{-1}\sqrt{\log(2m)}\right).
$$
All restrictions use the original evaluation oracle on subsets of original element identifiers. The number of calls and arithmetic operations is polynomial in the original input size and $\varepsilon^{-1}$.

For explicit integer-valued polymatroids and rational weights, the repeated calls also admit a standard polynomial-bit implementation; it is unnecessary to treat a sequence of arbitrary polynomial-time black boxes as automatically bit efficient. Use the exact strength decomposition in Quanrud's Section 3, and replace its logarithmic threshold multiplier by a dyadic rational within a fixed constant factor. Every output weight is an integer multiple of a threshold
$$
\tau=\theta\,\frac{w(U)-w(V)}{f(U)-f(V)},
$$
where $\theta$ has polynomially many bits and the positive denominator $f(U)-f(V)$ is an integer at most $r$. If the current weights have a common denominator, one pass enlarges a common denominator by only the product of at most $m_i$ such integer rank gaps and the dyadic denominator. Its bit length increases by $O(m_i\log(2r))$ plus the parameter precision. Also $\tau\le O(W_i)$, where $W_i$ is current total weight, so the total-weight bit length grows by at most $O(\log(2m_i))$ in that pass. Across the stated number of passes these increases remain polynomial in the initial description. Exact sampling of rational probabilities, or bounded-bit sampling with an additional fixed failure budget, is therefore sufficient.

**Fixed rational rank denominator.** The same ledger applies if all rank values have a fixed common denominator $\Delta=\operatorname{poly}(r)$, while every positive marginal is still at least one. Write $f(U)-f(V)=a/\Delta$, with $1\le a\le r\Delta$. Then $\tau=\theta\Delta(w(U)-w(V))/a$, so $\Delta$ appears only in the numerator, and one pass enlarges a common weight denominator by the product of at most $m_i$ integers bounded by $r\Delta$, together with the dyadic parameter denominator. The additional bit length is $O(m_i\log(2r\Delta))$ plus parameter precision. Keep the same function and common denominator throughout the restrictions. Quanrud's theorem accepts these rational values directly; multiplying $\Delta$ into the rank for the support analysis would introduce an unnecessary loss. The companion [../../group-metric-constraints/manuscripts/rational-quotient-ranks-from-weak-oracles.md](../../group-metric-constraints/manuscripts/rational-quotient-ranks-from-weak-oracles.md) constructs precisely such a rational rank, with $\Delta=O(r)$, from logarithmic subgroup ranks without requiring integer factorization.

## QB5. Applications

1. **Finite-field scalar codes.** Given weighted vectors $v_e\in\mathbb F_q^D$, take $f(T)=\dim\operatorname{span}\{v_e:e\in T\}$. For every query $y$, the zero set $\{e:\langle v_e,y\rangle=0\}$ is closed. Thus one reweighting on $O(D\log(2D/\varepsilon)/\varepsilon^2)$ original vectors preserves every weighted nonzero-coordinate count, with no support dependence on $q$.

2. **Finite-field block codes.** Given row spaces $S_e\subseteq\mathbb F_q^D$, take $f(T)=\dim\sum_{e\in T}S_e$. The blocks annihilating any fixed query again form a closed set. The same support bound preserves all weighted whole-block nonzero counts. No bound on individual block rank is needed.

3. **Polynomial fault lifts.** If an exact fault/query compiler maps the desired zero pattern to a scalar code of dimension $D=r\binom{h+k}{k}$, this observation gives
   $$
O\!\left(
   \frac{r\binom{h+k}{k}}{\varepsilon^2}
   \log\frac{2r\binom{h+k}{k}}{\varepsilon}
   \right)
$$
   retained original items. Neither a $\log\log q$ term nor a catalogue-enumeration argument is needed.

These applications use the same original-item identities throughout successive restrictions. The fault-dependent decoder and the quantum decomposition are proved in their companion manuscripts. $\square$
