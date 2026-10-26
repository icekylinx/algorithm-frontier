# Exact deterministic Subset Sum with low writable space

**Yilin Liu · GPT-6 Astra Pro**

## Abstract and theorem

**Theorem 2.** For arbitrary indexed binary integers `w_1,...,w_n,t` of total encoding length `L`, a uniform deterministic algorithm returns an indexed witness or correctly returns NO using

```math
T=\mathrm{poly}(n,L)2^{n/2},\qquad
S=\mathrm{poly}(n,L)2^{E_S n},\qquad
E_S=\frac{18261635770550353}{10^{17}}.
```

Time counts bit operations and space counts all simultaneously retained writable bits. The polynomial degrees are absolute constants. The proof includes signed and repeated weights, zero values, mixed density regimes, exact original-key recovery, and the high-deficiency fallback. This is a separate algorithm from the faster-time construction.

**Notation.** Logarithms are base two unless `ln` is written. The binary entropy is `h(z)=-z log_2 z-(1-z) log_2(1-z)` with continuous endpoint values. Masks always refer to indexed original coordinates.

## 2. Arithmetic primitives

Both algorithms use polynomial-time arithmetic on binary integers, the following prime bound, and exact array operations.

### 2.1. Prime density and enumeration

For real $`x\geq1`$, define

```math
\vartheta(x)=\sum_{p\leq x}\ln p,\qquad
\psi(x)=\sum_{p^j\leq x}\ln p,
```

where $`p`$ ranges over primes and $`j`$ over positive integers. A prime power in $`(\lceil n/2\rceil,n]`$ contributes a factor of its underlying prime to $`\binom n{\lfloor n/2\rfloor}`$. This follows by subtracting the three factorial valuations; its contribution at this power is one and all other contributions are nonnegative. Consequently

```math
\psi(n)-\psi(\lceil n/2\rceil)
\leq\ln\binom n{\lfloor n/2\rfloor}\leq n\ln2.
```

Induction gives $`\psi(n)\leq4n`$: for $`n\geq2`$, the induction bound is at most $`2n+2+n\ln2\leq4n`$, and the base case is immediate. Thus $`\psi(x)\leq4x`$ for real $`x\geq1`$.

Conversely, every prime valuation of $`\binom{2m}m`$ is at most the number of powers of that prime not exceeding $`2m`$. Since the central coefficient is the largest of the $`2m+1`$ coefficients whose sum is $`2^{2m}`$,

```math
\psi(2m)\geq\ln\binom{2m}m
\geq2m\ln2-\ln(2m+1).
```

Put $`m=\lfloor x/2\rfloor`$. Integrating the tangent-line bound $`1/u\geq4/3-4u/9`$ on $`[1,2]`$ gives $`\ln2\geq2/3`$. Thus $`\psi(x)\geq x/2`$ for $`x\geq64`$: it suffices that $`\ln(x+1)+4/3\leq x/6`$, which holds at $`64`$ by $`65<128`$ and $`\ln2<1`$, and whose right side grows faster thereafter. The prime-power contribution beyond the first power is at most

```math
\psi(x)-\vartheta(x)
=\sum_{j=2}^{\lfloor\log_2x\rfloor}\vartheta(x^{1/j})
\leq4\sqrt{x}\log_2x.
```

For $`x\geq2^{20}`$ the last bound is at most $`x/4`$ (the ratio $`\log_2x/\sqrt x`$ decreases in this range). We have proved

```math
x/4\leq\vartheta(x)\leq4x\qquad(x\geq2^{20}).
```

It follows that, for $`P\geq2^{20}`$,

```math
\#\{p:P<p\leq32P\}
\geq\frac{\vartheta(32P)-\vartheta(P)}{\ln(32P)}
\geq\frac{4P}{\ln(32P)}.
```

If a nonzero integer has absolute value less than $`2^b`$, at most $`b\ln2/\ln P`$ primes greater than $`P`$ divide it. The fraction of primes in this interval dividing that integer is therefore at most $`2b/P`$. This bound holds for all $`P\geq2^{20}`$. The interval ratio $`32`$ contributes a fixed factor.

All these primes can be generated deterministically in $`P\mathrm{poly}(\log P)`$ bit operations. Start with the integers through $`\lfloor32P\rfloor`$, and, for each unmarked integer starting at two, mark its proper multiples. A number remaining unmarked is prime: a composite has a smaller prime divisor, already processed. The number of marking iterations is at most $`32P\sum_{d\leq32P}1/d=O(P\log P)`$ even if all integers, rather than just primes, are charged. Index arithmetic has $`O(\log P)`$ bits.

### 2.2. Exact array and polynomial operations

For two length-$`q`$ arrays of integers of at most $`b`$ bits, compute cyclic convolution directly by

```math
c_r=\sum_{j=0}^{q-1}a_j b_{r-j\bmod q}.
```

This uses $`q^2`$ multiplications and additions on integers of $`O(b+\log(q+1))`$ bits. The same bound applies to cyclic correlation. Both reductions charge this quadratic cost for their moduli.

In fixed dimension $`d`$, a polynomial of coordinatewise degree at most $`M`$ has at most $`(M+1)^d`$ coefficients. Store them in an array. Addition, monomial shifts, and multiplication by a fixed polynomial take polynomial time in the degree and coefficient bit length. Integer arithmetic computes binomial coefficients and factorials through order $`M`$. These operations support conditional-expectation arguments.


# Part II. A deterministic low-space algorithm

This part proves Theorem 2. Write $`O^*(f(n))`$ for
$`\mathrm{poly}(n,L)f(n)`$, where $`L`$ is the full encoding length.
Masks refer to indexed coordinates. The weights are $`w_1,\ldots,w_n`$
and the target is $`t`$; parameters used below are local to this part.
The time and space bounds are

```math
\begin{gathered}
T=O^*(2^{n/2}),\qquad S=O^*(2^{E_Sn}),\\
E_S=\frac{18261635770550353}{10^{17}}<0.1826163578.
\end{gathered}
\tag{132}
```

The construction starts from the representation layout, modular
streams and separators of [7]. Weighted canonical-distance ownership,
linear translate covers, biased top layers and bounded original-key
streams are combined below. We use $`n=3m+O(1)`$ with $`8\mid m`$;
bounded leftover coordinates are enumerated explicitly.

## II.1. Support counting and nonlinear core extraction

For a coordinate set $`A`$, let

```math
\Sigma(A)=\left\{\sum_{i\in D}w_i:D\subseteq A\right\},
\qquad N(A)=|\Sigma(A)|,\qquad d(A)=|A|-\log_2N(A).
\tag{133}
```

All masks are indexed. Split $`A`$ into two nearly equal parts, sort their
raw subset-sum arrays, and heap-merge the rows of their pair sums in
increasing actual order. Counting each new value once computes $`N(A)`$
in $`O^*(2^{|A|})`$ time and $`O^*(2^{|A|/2})`$ space. The same stream fills
a distinct-value residue histogram with one additional modulus-length
array. Sums, comparisons, and counters have polynomial bit length in
$`n,L`$.

Choose the lexicographically least witness for every distinct sum of a
$`q`$-coordinate set, giving a family $`\mathcal F`$ of size $`N`$. Its
projection onto any coordinate set is sum-injective. If two projected
masks had the same sum, replacing the lexicographically larger one in
its full canonical witness would preserve the sum and decrease that
witness.

A cube family of size $`N`$ has at most $`N\log_2N/2`$ internal edges.
Induct on dimension: slices of sizes $`a,b`$ have at most
$`(a\log_2a+b\log_2b)/2`$ internal edges and at most $`\min(a,b)`$ crossing
edges. Concavity gives $`h(p)\ge2\min(p,1-p)`$, so the bound follows with
$`p=a/(a+b)`$. If $`E_i`$ counts edges in direction $`i`$, forgetting that
coordinate leaves exactly $`N-E_i`$ projected masks. Some deletion
therefore retains support at least $`N(q+d_q)/(2q)`$, and the maximum-support
deletion satisfies

```math
d_{q-1}\le d_q-\log_2(1+d_q/q).
\tag{134}
```

The algorithm counts all one-coordinate deletions sequentially and takes
a largest support, with fixed tie breaking. The entire nested chain
costs $`O^*(\sum_{q\le m}q2^{q-1})=O^*(2^m)`$ time and
$`O^*(2^{m/2})`$ space. It retains polynomially many coordinate sets and
counts.

Since $`\log_2(1+x)\ge x`$ on $`[0,1]`$, deficiency density decreases along
the chain. If its initial density is at most $`\kappa`$, then
$`\lambda=\log_2(1+\kappa)/\kappa`$ gives
$`d_{q-1}\le(1-\lambda/q)d_q`$. For $`q\ge2`$ these factors are
nonnegative and at most $`(1-1/q)^\lambda`$. Thus

```math
d(C)\le(c/m)^\lambda d(B),\qquad |C|=c,\quad |B|=m.
\tag{135}
```

The zero-deficiency and empty-core cases follow directly. We will also
use $`\lambda=4/3`$ when $`\kappa\le1/6`$, certified by $`7^9>4\cdot6^9`$.

The sharper certificate used in the resource policy is

```math
P_*=\frac{23}{26},\qquad
\Phi(\delta)=\frac{\delta^{52}}{(P_*-\delta)^{75}},
\qquad
\Psi(q,d)=\frac{d^{52}}{(P_*q-d)^{75}}.
\tag{136}
```

For $`\delta=d_q/q\le1/5`$, put
$`F(\delta)=\log_2(1+\delta)-\delta`$ and
$`R(\delta)=\delta(P_*-\delta)/(2+\delta)`$.
The derivative of
$`\ln(1+\delta)-2\delta/(2+\delta)`$ is
$`\delta^2/((1+\delta)(2+\delta)^2)\ge0`$.
The positive atanh series gives
$`\ln2<2/3+2/81+1/540=1123/1620<52/75`$.
Consequently $`F(\delta)\ge R(\delta)`$, and
$`R'(\delta)=(2P_*-4\delta-\delta^2)/(2+\delta)^2>0`$ on $`[0,1/5]`$.
Writing $`\delta'=d_{q-1}/(q-1)`$, (134) gives
$`\delta'\le\delta-R(\delta)/(q-1)`$. Since
$`(\ln\Phi)'=23/R`$, integration yields

```math
\ln\Phi(\delta)-\ln\Phi(\delta')
\ge\frac{23(\delta-\delta')}{R(\delta)}
\ge\frac{23}{q-1}
\ge23\ln\frac q{q-1}.
\tag{137}
```

A zero endpoint is immediate. Since
$`\Phi(d/q)=q^{23}\Psi(q,d)`$, multiplication along the chain proves
$`\Psi(c,d(C))\le\Psi(m,d(B))`$ exactly.

For an initial density upper bound $`0<x\le1/5`$ and retained fraction
$`s\in(0,1]`$, define $`\beta(x,s)`$ by

```math
\beta^{52}(P_*-x)^{75}=x^{52}(P_*s-\beta)^{75},
\quad 0<\beta\le sx.
\tag{138}
```

The left-to-right ratio increases strictly with $`\beta`$, so the root is
unique. Equivalently,
$`P_*s=xt+(P_*-x)t^{52/75}`$ and $`\beta=xt`$.
The potential proves $`d(C)\le m\beta(x,s)`$.
At $`x=0`$ set $`\beta=0`$. Increasing $`x`$ enlarges the initial potential,
so $`\beta`$ is increasing in $`x`$; also $`\beta(x,s)\le sx`$.
Rational bisection of (138), with denominators cleared, supplies safe
$`O(1/m)`$ enclosures by fixed-power integer comparisons.
All requested sizes and deficiency proxies are selected before useful
layers. Exact support counts continue to define the actual histograms.

## II.2. Trace mass, support-dependent signings, and balanced cells

### II.2.1. An exact fixed-layer trace inequality

For integers $`0\le k,r\le c`$ and every $`\mathcal F\subseteq\{0,1\}^c`$ with $`|\mathcal F|\ge2^k`$,

```math
\sum_{|T|=r}|\pi_T\mathcal F|
\ge[z^r](1+2z)^k(1+z)^{c-k}
=\sum_j\binom kj\binom{c-k}{r-j}2^j.
\tag{139}
```

We prove the rank comparison needed for this coefficient inequality.
For an integer interval $`I`$, let $`W(I)`$ be its multiset of binary
Hamming weights. Domination means that every upper-threshold count is
at least as large. We claim that, for $`a\ge b\ge0`$,

```math
W([a,a+b))\ \text{dominates}\ 1+W([0,b)).
\tag{140}
```

The case $`b=0`$ is immediate. Use strong induction on $`a+b`$. A consequence available at smaller sums
is $`W([u,u+v))`$ dominating $`W([0,v))`$: apply (140) to
$`\max(u,v),\min(u,v)`$, weaken by removing the added one, then add and
cancel common prefix multisets in the threshold inequalities.
Let $`H`$ be the largest power of two at most $`a`$.
If $`a+b\le2H`$, remove the leading bit and apply this consequence to
$`[a-H,a-H+b)`$. If $`a+b>2H`$, put $`D=2H=2^d`$,
$`u=D-a`$, and $`v=b-u>0`$. Since $`D-b\ge u`$, the smaller instance
$`(D-b,u)`$ gives
$`W([D-b,D-b+u))`$ dominating $`1+W([0,u))`$.
Complementing the $`d`$ bits reverses domination and gives
$`W([a,D))`$ dominating $`1+W([v,b))`$.
The remaining interval has
$`W([D,D+v))=1+W([0,v))`$, proving (140).

If $`B_j(N)`$ counts integers below $`N`$ with Hamming weight at least $`j`$,
(140) says
$`B_j(a)+B_{j-1}(b)\le B_j(a+b)`$ for $`a\ge b`$.
Induction on dimension now shows that a downset $`\mathcal D`$ of size
$`N`$ has at most $`B_j(N)`$ members of rank at least $`j`$: its two slices
are downsets of sizes $`N_0\ge N_1`$, and the displayed inequality combines
their inductive bounds. Thus, for every nonnegative decreasing rank
weight $`w`$,

```math
\sum_{A\in\mathcal D}w(|A|)
\ge\sum_{j=0}^{N-1}w(\mathrm{wt}(j)).
\tag{141}
```

This follows by expressing $`w`$ as a constant plus nonnegative multiples
of lower-rank threshold indicators.

Downward compression in a coordinate replaces sections
$`\mathcal F_0,\mathcal F_1`$ by their union and intersection.
It preserves cardinality and decreases every projection size:
projections omitting the coordinate are unchanged, while the sum of
the two projected section sizes bounds the corresponding union and
projected intersection. Compression preserves earlier downward closure,
so one pass through the coordinates yields a downset $`\mathcal D`$
with $`|\pi_T\mathcal F|\ge|\pi_T\mathcal D|`$ for every $`T`$.
For a downset,

```math
\sum_{|T|=r}|\pi_T\mathcal D|
=\sum_{A\in\mathcal D}\binom{c-|A|}{r-|A|}.
\tag{142}
```

The rank weight on the right decreases, with consecutive ratio
$`(r-j)/(c-j)`$ until it becomes zero. When $`|\mathcal D|=2^k`$,
(141) compares it with the full $`k`$-cube and gives (139).
For a larger family, take any $`2^k`$ members first.

Apply (139) to the canonical full-support witnesses of a weighted
$`c`$-coordinate core. Their projections are sum-injective by Section II.1.
With $`k=\lfloor\log_2N\rfloor`$,

```math
S_r:=\sum_{|T|=r}N(T)
\ge[z^r](1+2z)^k(1+z)^{c-k}.
\tag{143}
```

The right side is a polynomial-bit binomial sum. The canonical and
compressed families serve only in this proof.

### II.2.2. Finite trace-gain certificates

Let $`N\ge2^{c-d}`$, $`\delta=d/c`$, and
$`r=\theta c+O(Q_{\rm grid})`$, where $`Q_{\rm grid}`$ is a fixed multiple of four chosen before the input.
Retaining a binomial term in (143) gives

```math
\log_2S_r\ge c\max_\eta
\left\{(1-\delta)h\!\left(\frac{\theta-\eta\delta}{1-\delta}\right)
       +\delta h(\eta)+\theta-\eta\delta\right\}
-O(Q_{\rm grid}\log(c+1)).
\tag{144}
```

The feasible $`\eta`$ make both entropy arguments valid. The finite
rectangles used below satisfy

```math
\log_2S_r\ge[h(\theta)+\theta]c-(\theta-g)d
              -O(Q_{\rm grid}\log(c+1)),
\tag{145}
```

with $`(\theta,\delta,g)`$ in
$`[.38,.46]\times[0,.2]\times\{1/16\}`$,
$`[.41,.46]\times[0,.05]\times\{3/40\}`$, or
$`[.44,.46]\times[0,.03]\times\{79/1000\}`$.
Greedy extraction decreases deficiency density, so a rectangle chosen
from a full-block density upper bound also applies to its strict core.

Here is a complete rational certificate. For fixed rational $`\eta`$,
subtract $`h(\theta)+\theta(1-\delta)`$ from the expression in braces
in (144), calling the result $`\Delta(\theta,\delta)`$.
It is concave in $`\delta`$, with value zero at zero. For positive
$`\delta`$ it is also concave in $`\theta`$: writing
$`z=(\theta-\eta\delta)/(1-\delta)`$, its second derivative is
$`(\ln2)^{-1}(1/(\theta(1-\theta))-1/((1-\delta)z(1-z)))<0`$.
Indeed,
$`\theta(1-\theta)=(1-\delta)z(1-z)+\delta\eta(1-\eta) +\delta(1-\delta)(z-\eta)^2`$.
It therefore suffices to bound $`\Delta/\delta`$ at the two theta
endpoints and the upper density endpoint of each rectangle.

Define rational entropy enclosures by

```math
\begin{aligned}
\ell_-&=2\sum_{j=0}^{11}\frac1{(2j+1)3^{2j+1}},
&\ell_+&=\ell_-+\frac2{25\,3^{25}}\frac98,\\
S(z)&=\sum_{j=1}^{32}\frac{z^{2j}}{(2j)(2j-1)},
&R(z)&=\frac{z^{66}}{66\cdot65(1-z^2)},\\
h_-(p)&=1-\frac{S(|1-2p|)+R(|1-2p|)}{\ell_-},
&h_+(p)&=1-\frac{S(|1-2p|)}{\ell_+}.
\end{aligned}
\tag{146}
```

The positive atanh series bounds $`\ln2`$ between $`\ell_-,\ell_+`$;
the positive entropy series and its geometric tail give
$`h_-(p)\le h(p)\le h_+(p)`$ at the interior arguments used here.
Substitution into

```math
G_-=
\frac{(1-\delta)h_-((\theta-\eta\delta)/(1-\delta))
             +\delta h_-(\eta)-h_+(\theta)}{\delta}
+\theta-\eta
\tag{147}
```

gives the following strict rational lower comparisons:

| Theta interval | $`\delta`$ | $`\eta`$ | Left bound | Right bound |
|---|---:|---:|---:|---:|
| $`[19/50,2/5]`$ | $`1/5`$ | $`13/50`$ | $`6253/10^5`$ | $`6309/10^5`$ |
| $`[2/5,43/100]`$ | $`1/5`$ | $`7/25`$ | $`6395/10^5`$ | $`6417/10^5`$ |
| $`[43/100,23/50]`$ | $`1/5`$ | $`3/10`$ | $`6597/10^5`$ | $`6439/10^5`$ |
| $`[41/100,43/100]`$ | $`1/20`$ | $`13/50`$ | $`7548/10^5`$ | $`7558/10^5`$ |
| $`[43/100,23/50]`$ | $`1/20`$ | $`7/25`$ | $`7714/10^5`$ | $`7676/10^5`$ |
| $`[11/25,23/50]`$ | $`3/100`$ | $`143/500`$ | $`3967/50000`$ | $`1593/20000`$ |

Each entry is verified by (146)–(147) after clearing positive
denominators. The first three exceed $`1/16`$, the next two exceed $`3/40`$,
and the last exceeds $`79/1000`$. The two concavity reductions prove
(145) over all three rectangles, including zero density by continuity.

### II.2.3. Linear translate covers

Let $`V=\mathbb F_2^c`$, let $`\varnothing\ne G\subseteq V`$, and suppose membership in $`G`$ takes deterministic time $`Q`$ and workspace $`W`$. Write $`N=2^c`$ and $`\alpha=|G|/N`$. There is a deterministic algorithm returning a basis for a subspace $`H\le V`$ such that

```math
G+H=V,\qquad
K:=|H|\le\min\left\{2^c,\frac{2(1+c\ln2)}{\alpha}\right\}.
\tag{148}
```

Its time is $`O^*(2^cKQ)`$ and its space is $`O^*(W+\mathrm{poly}(c))`$. A basis permits enumeration of all centers with polynomial delay and state. All arithmetic in the construction has polynomial bitlength.

Start with $`H=\{0\}`$ and let $`U=V\setminus(G+H)`$. Adding a vector $`v`$ to the basis replaces the uncovered set by $`U\cap(U+v)`$. The average translation intersection is

```math
\frac1N\sum_{v\in V}|U\cap(U+v)|=\frac{|U|^2}{N}.
\tag{149}
```

Choose $`v`$ whose intersection size is no larger than this average. If $`U\ne\varnothing`$, then $`0<|U|<N`$. Such a choice strictly decreases $`|U|`$, and cannot lie in $`H`$, since $`U`$ is $`H`$-invariant. Consequently the subspace doubles at every successful step. After $`d`$ steps,

```math
|U_d|/N\le(1-\alpha)^{2^d}\le e^{-\alpha2^d}.
\tag{150}
```

The first power of two at least $`(1+c\ln2)/\alpha`$ makes the integer $`|U_d|`$ smaller than one. Alternatively rank $`c`$ gives $`H=V`$. This proves (148). The algorithm stops by exact counting, without evaluating a real logarithm.

To choose $`v`$, fix its bits by conditional expectation. For a prefix length $`j`$, let $`U_a`$ be the number of uncovered vectors with prefix $`a\in\mathbb F_2^j`$. If $`v`$'s prefix is $`P`$, then

```math
\mathbb E[|U\cap(U+v)|\mid v|_{[j]}=P]
 =2^{-(c-j)}\sum_a U_aU_{a+P}.
\tag{151}
```

For each uncovered $`x`$ with prefix $`a`$, its translated suffix is uniform in the suffix class with prefix $`a+P`$; this proves the formula. The two next-bit means average to the current mean. Choose the smaller, using their common-denominator integer numerators. The uncovered predicate remains unchanged until all bits of the new vector have been chosen.

Membership in $`U`$ is decided by enumerating the present $`H`$ and testing $`x+h\notin G`$ for every $`h`$. For one candidate prefix, enumerate each $`a`$, count $`U_a`$ and $`U_{a+P}`$ by scanning their suffix classes, multiply the two counts, then discard them. The suffix classes partition $`V`$, so this is at most two full passes, with time $`O^*(N|H|Q)`$ and space $`W+\mathrm{poly}(c)`$. The score has at most $`2c+1`$ bits. The $`c`$ bit choices add a polynomial factor. Across stages the current subspace sizes are $`1,2,\ldots,K/2`$, whose sum is less than $`K`$. Exact stopping tests, including a final full pass, obey the same bound. This proves the claimed time and space.

If $`G`$ lies in the cardinality layer $`\binom{[c]}r`$, test cardinality before the expensive predicate, whose time and state on this layer are $`Q_r,W_r`$. For each fixed $`h`$, exactly $`\binom cr`$ of the $`N`$ translated vectors in a full pass have cardinality $`r`$. The preceding proof therefore gives the sharper bound

```math
T=O^*\!\left(K\left[2^c+\binom cr Q_r\right]\right),
\qquad S=O^*(W_r+\mathrm{poly}(c)).
\tag{152}
```

For a dyadic class defined by distinct subset-sum support, sorted half-sum streaming gives $`Q_r=O^*(2^r)`$, $`W_r=O^*(2^{r/2})`$. The cardinality test charges all failed masks; early successful membership tests only reduce the count.

### II.2.4. Support classes and signing costs

Partition the $`r`$-subsets into exact support classes
$`\mathcal G_\ell=\{T:2^\ell\le N(T)<2^{\ell+1}\}`$.
Count them by the support stream of Section II.1, and choose a nonempty
class maximizing $`2^\ell g`$, where $`g=|\mathcal G_\ell|`$.
There are at most $`r+1`$ classes, so $`2^\ell g\ge S_r/(2(r+1))`$.
Apply the linear translate cover to this class, and let $`K`$ be its
actual number of centers. Coverage gives $`2^c\le Kg`$, while the size
bound gives $`Kg\le\mathrm{poly}(c)2^c`$. Put
$`\tau=1-h(\theta)`$ and $`\phi=\theta-\gamma`$ for the applicable trace
gain $`\gamma`$. The resulting bounds are:

```math
\begin{aligned}
\ell-\log_2K&\ge(\theta-\tau)c-\phi d
                    -O(Q_{\rm grid}\log(c+1)),\\
\ell&\ge\theta c-\phi d-O(Q_{\rm grid}\log(c+1)),\\
\log_2K&\le\tau c+\phi d+O(Q_{\rm grid}\log(c+1)).
\end{aligned}
\tag{153}
```

For the first line, use
$`\ell+\log_2g\ge\log_2S_r-O(\log(c+1))`$ and the upper bound on
$`Kg`$. The second also uses $`g\le\binom cr`$; the third follows from
the first and $`\ell\le r`$. All class choices and membership tests
use exact integers. Substituting the third line into the layer-aware
construction bound gives

```math
T=O^*\!\left(2^{(1+\theta)c+\phi d}\right),\qquad
S=O^*\!\left(2^{r/2}+\mathrm{poly}(c)\right).
\tag{154}
```

Indeed, the expensive term is
$`K\binom cr2^r\le O^*(2^{(1+\theta)c+\phi d})`$;
the $`K2^c`$ term is smaller because $`h(\theta)+\theta>1`$ on the
active intervals. A center basis is stored once per unsigned core and
scalar configuration, before outer owners or top signings. Subsequent
per-center work retains the actual $`K`$ multiplicity.

For a center $`D`$, negate its weights and map a mask $`S`$ to
$`S\mathbin\triangle D`$. Its signed weight is the original weight
minus $`\Delta_D=\sum_{i\in D}w_i`$. On every fixed coordinate subset
$`T`$, the signed support is a translate of $`\Sigma(T)`$, so support-class
membership is independent of the center. Permitted fixed-cardinality
images are generated with their actual signed weights. Restoring
$`\Delta_D`$ recovers original local keys.

### II.2.5. Constructive balanced-cell families

We use a fixed number $`Q_{\rm grid}`$ of fine cells. For a core of size $`b`$
divisible by $`Q_{\rm grid}`$, fix a selected cardinality $`r`$ and smaller
cardinality $`k`$, with $`Q_{\rm grid}\mid r,k`$. A three-coloring
$`(D,A\setminus D,B\setminus A)`$ has totals $`(k,r-k,b-r)`$.
A uniform equipartition into $`Q_{\rm grid}`$ equal cells gives exactly
$`1/Q_{\rm grid}`$ of each color to each cell with probability at least

```math
p_b=(b+1)^{-3Q_{\rm grid}}.
\tag{155}
```

For each color, its equally split multinomial coefficient is maximal
and at least $`Q_{\rm grid}^{\,\text{color size}}/(b+1)^{Q_{\rm grid}}`$.
Multiplying these three lower bounds and dividing by at most $`Q_{\rm grid}^b`$
equipartition labelings proves (155).

Construct a family covering every such coloring by greedy conditional
expectation. After some partitions are chosen, fix the labels of one
new partition coordinate by coordinate. For a coloring with remaining
color counts $`r_a`$, residual cell capacities $`R_j`$, and residual
target counts $`t_{aj}`$, its conditional coverage probability is

```math
\frac{\prod_a r_a!/\prod_{a,j}t_{aj}!}
     {(\sum_jR_j)!/\prod_jR_j!},
\tag{156}
```

interpreted as zero for a negative target. Enumerate the uncovered
colorings, testing their status against the prior polynomial list,
and choose a next cell label at least as good as its capacity-weighted
mean. Each completed partition covers at least $`p_b`$ of the remaining
colorings. At most $`p_b^{-1}(b\ln3+1)+1`$ partitions suffice.
The factorials and score sums have polynomial bit length; the universe
is regenerated, and only the selected partition list is stored.

For an active strict local shell, $`\theta=.45`$, and the coloring count is
$`\binom br\binom rk\le2^{[h(\theta)+\theta]b+O(Q_{\rm grid})}\le 2^{1.45m+O(Q_{\rm grid})}`$.
For a top base of size at most $`.9m`$ it is at most
$`3^{.9m+O(Q_{\rm grid})}<2^{1.427m+O(Q_{\rm grid})}`$, and an oriented half uses at
most $`3^{m/2}`$. Multiplication by the fixed-degree polynomial factors
preserves these bounds. Thus this construction supplies all required
fine-cell families within the half-exponential budget using polynomial
state. The local families depend only on their fixed cores and cardinalities.
Construct them before the ownership and signing loops, then reuse them
throughout. Top-base families are likewise reused across their signings.

To align a useful smaller layer, remove fewer than $`Q_{\rm grid}`$ elements from
each of its distinct-sum witnesses. If the removed set is $`R`$, its
original sum is the trimmed sum plus $`\sum_{i\in R}w_i`$; one trimmed
sum accounts for at most $`\binom b{|R|}`$ original sums.
Thus trimming loses at most $`b^{Q_{\rm grid}-1}`$.
For each retained sum choose one trimmed witness. Every three-coloring
is balanced by some partition in the constructed family, so one
partition retains a reciprocal-polynomial fraction of the distinct sums.
The selected pattern occupies $`r/Q_{\rm grid}`$ positions per cell and its
smaller mask $`k/Q_{\rm grid}`$ positions. The total trimming, layer, and layout
loss is $`O(Q_{\rm grid}\log(b+1))`$ in its support logarithm.
Choose shell sizes divisible by $`Q_{\rm grid}`$ within $`O(Q_{\rm grid})`$ of $`\theta b`$;
this changes the finite trace estimates only by the same lower-order
term.

### II.2.6. Retained quarter layers

Consider a good selected shell of size
$`r=\theta c+O(Q_{\rm grid})`$ with $`N(T)\ge2^\ell`$ and
$`\theta c-\ell\le\phi d+O(Q_{\rm grid}\log(m+1))`$.
If the full-block deficiency density is at most $`x`$ and
$`\phi x<\theta/8`$ with a fixed positive gap, density monotonicity gives
$`\ell/r>7/8`$ after a fixed coordinate cutoff.
Pigeonhole distinct-sum witnesses by cardinality, complement within
$`T`$ if necessary, and trim fewer than $`Q_{\rm grid}`$ positions.
The resulting smaller layer $`k\le r/2`$ retains at least
$`2^\ell/\mathrm{poly}(m)`$ distinct sums. Since its cardinality
is at most $`2^{r h(k/r)}`$,

```math
h(k/r)\ge\ell/r-o(1)>7/8>h(1/4).
\tag{157}
```

The last comparison follows from $`3^9>2^{14}`$, which gives
$`h(1/4)<5/6`$. Hence a useful layer has $`k/r>1/4`$ with a fixed margin.
We retain only $`r/4\le k\le r/2`$ before expensive processing.
The polynomial family of retained layers and layouts preserves a
representation of every original solution.

For the biased top, $`\theta=21/50`$, $`x\le27/200`$, and
$`\phi\le143/400`$. For a strict local core, $`\theta=9/20`$ and
$`\phi\le31/80`$. The requisite gaps are

```math
\frac{\theta}{8}-\phi x\ge
\begin{cases}
339/80000,&\theta=21/50,\\
63/16000,&\theta=9/20.
\end{cases}
\tag{158}
```

Every retained top layer satisfies
$`k/c\ge.105-o(1)>.1`$ and $`(r-k)/c\ge.21-o(1)>.2`$.
The integer inequalities
$`10^{20}>2^9 9^{18}`$ and $`5^{10}>2^{23}`$ give
$`h(.1)>9/20`$ and $`h(.2)>7/10`$. Its actual mean mask entropy
therefore exceeds $`23/40`$ after the fixed cutoff.
For every retained strict local layer,
$`k/c\ge9/80-o(1)>1/9`$ and $`(r-k)/c\le27/80+o(1)<7/20`$.
The inequalities $`9^6>2^{19}`$ and
$`20^{80}<2^{75}7^{28}13^{52}`$ imply
$`h(1/9)>1/2`$ and $`h(7/20)<15/16`$. Thus

```math
h((r-k)/c)-h(k/c)<7/16.
\tag{159}
```

These bounds apply to every processed layer. The fine-cell product
counts incur $`O(Q_{\rm grid}\log(m+1))`$ error. Concavity also gives
$`h(k/c)+h((r-k)/c)\ge h(\theta)-o(1)`$, which will bound the
unrestricted child domains.

### II.2.7. Shared local image scans

For fixed local layer, layout, and child roles, a center $`D`$ and good
selected set $`T`$ determine a permitted image $`X_D(T)`$.
In a candidate-prime scan, enumerate $`T`$ first and count its support
once. For good $`T`$ only, enumerate the centers and generate
$`X_D(T)`$. Since $`K|\mathcal G_\ell|\le\mathrm{poly}(c)2^c`$,

```math
O^*\!\left(\binom cr2^r+K|\mathcal G_\ell|2^r\right)
=O^*(2^{c+r})
\tag{160}
```

bounds one complete scan. The support-class test is independent of
$`D`$, by the translation identity above. It is also independent of the
outer top label.

For one top seed, construct all local weighted residue covers in
lockstep. Keep each center's uncovered count, candidate interval,
polynomial seed list, and separate resource means. At every score
pass, put the good-set loop outside the center loop, generating one
image and its residue-prefix counts at a time. An image and its offsets
cost $`O^*(2^r)`$, since its modulus is $`O^*(2^\ell)`$ and $`\ell\le r`$.
Thus a simultaneous coverage-score pass costs $`O^*(2^{c+r})`$.
Regenerate each center's resource vector in a shared workspace and
compare its own two exact means. The histogram cost is separately

```math
O^*\!\left(K(P_{\max}^2+P_{\max}+2^{m-c})\right).
\tag{161}
```

Only $`O^*(K)`$ scalar and seed state is cached. One image, histogram,
and complementary-support workspace is live at a time. Each cover
retains its own nonnegative cost normalizers; interleaving their score
passes preserves every conditional-expectation guarantee.

## II.3. Weighted ownership representations

Let a top core have size $`a`$, $`N`$ distinct subset sums and deficiency $`d=a-\log N`$. For the dense branch, use $`a=.9m+O(1)`$, $`p=1/20`$, and $`d/a\le17/2000+O(1/m)`$. The representation and checker constructions below have the following bounds:

```math
\begin{aligned}
T_{\rm owner}&=O^*(2^{3a/2+2d}),&
S_{\rm owner}&=O^*(2^{a/2}+2^d),\\
T_{\rm container}&=O^*(2^{.3825m}),&
S_{\rm construction}&=O^*(2^{.1275m}),\\
S_{\rm assignment/index}&=O^*(2^{.265185m}).
\end{aligned}
\tag{162}
```

Every parent retains movable top/background logarithmic mass at least $`m/2-O(\log m)`$. Its upper mass is the central equal-rate budget, up to polynomial factors. Exact incidence is bounded by $`2^{3m/2}`$ times a polynomial whenever the original local full-block deficiency is at least $`d`$. The bounds hold for arbitrary indexed integer weights and every feasible fine profile.

### II.3.1. Direct coefficients and canonical distance

Let $`H`$ be the owner-right region of cardinality $`b`$. For an original top subset $`S`$ and variation mask $`R`$, use

```math
(\alpha_i,\beta_i)=
\begin{cases}
(S_i\oplus R_i,\ R_i(2S_i-1)),&i\notin H,\\
(R_i(2S_i-1),\ S_i\oplus R_i),&i\in H.
\end{cases}
\tag{163}
```

The coordinate sum is $`S_i`$. The left top weight is
$`w(S\setminus H)+w^{S\oplus H}(R)`$, where $`w_i^G=(-1)^{G_i}w_i`$.
The parents store these original coefficient weights. A compatible pair is exactly one with binary coordinatewise sums.

Choose the smallest indexed full mask $`X`$ for each distinct original top sum, and denote this family by $`\mathcal F`$. For a given $`S`$, let $`N_j(S)`$ count its canonical witnesses at Hamming distance $`j`$. Fix integers $`b,u,v`$ with
$`0\le u\le a-b`$, $`0\le v\le b`$, and $`j=b+u-v`$. Set

```math
Q=\binom{a-b}u\binom bv,\qquad
c(S,H)=\#\{X\in\mathcal F:
 |(X\oplus S)\setminus H|=u,\quad |(X\oplus S)\cap H|=b-v\}.
\tag{164}
```

For $`R=X\oplus S\oplus H`$, the required variation quotas are $`u,v`$.
For fixed $`H`$, its signed sum equals
$`w(X)-w(S\oplus H)`$, so canonical contributions remain distinct.
Consequently $`c(S,H)`$ is a lower bound on the actual signed quota-image size and $`c(S,H)\le Q`$.

Counting the same pairs $`(Y,H)`$, with $`|Y|=j`$, in two orders gives

```math
\binom aj\binom ju\binom{a-j}v=\binom ab Q,\qquad
\frac1{\binom ab}\sum_{|H|=b}c(S,H)
 =\frac{N_j(S)Q}{\binom aj}.
\tag{165}
```

Choose a distance band $`I`$ by the integer condition
$`\sum_{j\notin I}\binom aj\le N/2`$.
For every $`S`$, some $`j\in I`$ then has
$`N_j(S)\ge N/[2(a+1)]`$. All distances in the band are enumerated.

### II.3.2. Weighted owner covers

For a fixed distance and quota configuration, put $`C_0=2(a+1)`$,

```math
\mathcal E=\{S:C_0N_j(S)\ge N\},\qquad
M=\frac{NQ}{C_0\binom aj},\qquad
L_Q=1+\lfloor\log Q\rfloor.
\tag{166}
```

Configurations with $`M>Q`$ have empty eligible universe. Otherwise maintain pairs $`(H_i,\ell_i)`$, with $`0\le\ell_i<L_Q`$, and the implicit uncovered set
$`\mathcal U=\{S\in\mathcal E:c(S,H_i)<2^{\ell_i}\text{ for all earlier }i\}`$.
When $`\mathcal U\ne\varnothing`$, choose $`H`$ satisfying
$`\sum_{S\in\mathcal U}c(S,H)\ge M|\mathcal U|`$.
For $`r_\ell=\#\{S\in\mathcal U:c(S,H)\ge2^\ell\}`$, the inequality
$`c\le\sum_{2^\ell\le c}2^\ell`$ gives some threshold with
$`2^\ell r_\ell\ge M|\mathcal U|/L_Q`$. Choose a maximizing threshold and append that pair.

Charge $`2^{-\ell}`$ to the pair. If it removes $`r`$ of the $`U`$ current elements, its charge is at most $`Lr/(MU)`$. Summing this through successive removals is bounded by a harmonic sum:

```math
\sum_i2^{-\ell_i}\le\frac{L_Q H_{|\mathcal E|}}M
 \le\frac{L_Q(1+a\ln2)}M,\qquad
K:=\#\{i\}\le\mathrm{poly}(a)2^d.
\tag{167}
```

The last inequality uses $`2^{-\ell_i}\ge1/Q`$ and
$`\binom aj\le2^a`$. Grouping pairs by threshold yields, for each group,

```math
\frac{K_\ell Q}{2^\ell}
 \le\mathrm{poly}(a)\frac{\binom aj}{N}.
\tag{168}
```

Every eligible pattern succeeds in at least one of the enumerated groups.

Here is a low-state implementation of the owner choice. A prefix fixes owner-one coordinates $`F_1`$, owner-zero coordinates $`F_0`$, and leaves $`W`$ unfixed. It has
$`B_P=\binom{|W|}{b-|F_1|}`$ completions. For a mask $`Y`$, put
$`z_1=|Y\cap F_1|`$, $`z_w=|Y\cap W|`$. The number of these completions giving the prescribed quotas is zero unless $`|Y|=j`$, and otherwise equals

```math
k_P(Y)=
 \binom{z_w}{b-v-z_1}
 \binom{|W|-z_w}{b-|F_1|-(b-v-z_1)}.
\tag{169}
```

Infeasible binomial arguments mean zero. The mean total trace over the prefix's completions is:

```math
A_P/B_P,\qquad
A_P=\sum_{S\in\mathcal U}\sum_{X\in\mathcal F}k_P(S\oplus X).
\tag{170}
```

The current mean is the completion-count-weighted average of the feasible next-bit means. Exact cross multiplication therefore chooses a child with no smaller mean. Starting from (165), $`a`$ choices produce the required owner. The uncovered set is kept fixed throughout these prefix choices.

Partition coordinates computationally into halves of sizes $`\lfloor a/2\rfloor,\lceil a/2\rceil`$, independently of ownership. Write $`S=(s,z)`$, $`X=(x,y)`$. For fixed $`s`$, scan $`\mathcal F`$ and group its low masks $`y`$ by the three high-part counts of $`x\oplus s`$ in $`F_1,F_0,W`$. There are polynomially many arrays of length $`2^{\lceil a/2\rceil}`$. For each high-count triple, form the low kernel by inserting its counts and the low-mask counts into (169). Summing their XOR convolutions gives every value
$`\sum_X k_P((s,z)\oplus X)`$ for that $`s`$.

A Walsh transform computes each convolution exactly: apply the butterflies $`(x,y)\mapsto(x+y,x-y)`$, multiply the transforms pointwise, apply the transform again, and divide by its length. Character orthogonality proves exactness. The counts and intermediate values have polynomial bitlength. Grouping by high distance similarly computes $`N_j((s,z))`$; grouping by the two high quota counts computes $`c((s,z),H_i)`$ for any previous pair. Retain the eligibility/uncovered Boolean array for this $`s`$, and process previous pairs sequentially.

The canonical scan itself sorts the two half-subset occurrence lists and heap-merges their pair-sum rows. Process each equal-weight run completely, retaining only its smallest full mask. It costs $`O^*(2^a)`$ time and $`O^*(2^{a/2})`$ state per reset, including repeated and negative sums. For each $`s`$, its scan dominates the polynomially many low transforms. Enumerating all $`s`$, a prefix score, termination test or threshold count costs
$`O^*(2^{3a/2}(1+K_{\rm old}))`$ time and
$`O^*(2^{a/2}+K_{\rm old})`$ state.
Summing over the $`K`$ choices proves the first line of (162).

For each nonempty group and $`t=j/a-1/2`$, binomial upper bounds turn (168) into

```math
\log Q-\ell+\log K_\ell
 \le d-aD(t)+O(\log a),\qquad
D(t)=1-h(1/2+t).
\tag{171}
```

The owner lists are constructed before the common-prime selection of Section II.4, which uses their actual signed quota images.

### II.3.3. Equal rates on unequal owner regions

Fix $`p=1/20`$. For an exact distance $`j`$, set

```math
t=j/a-1/2,\qquad z=\frac{t}{1-2p},\qquad
b=a(1/2+z),\qquad
u=p(a-b),\quad v=pb.
\tag{172}
```

Then $`b+u-v=j`$, the total variation radius is $`pa`$, and the ideal natural quota entropy is $`a h(p)`$, independent of $`t`$.
Round $`b`$, round $`u=p(a-b)`$, and define $`v=b+u-j`$. This preserves the distance exactly and changes all counts by $`O(1)`$. On the active band $`|t|\le.06`$, both owner regions and both quota fractions have fixed positive interior margins, so rounding changes logarithmic estimates by $`O(\log a)`$. Thus

```math
\log Q=a h(p)+O(\log a),\qquad u+v=pa+O(1).
\tag{173}
```

The band exists for every original pattern: strict extraction does not increase density, so $`d/a\le.0085+O(1/m)`$, whereas the positive entropy series and $`\ln2<52/75`$ give

```math
D(.06)\ge\frac{2(.06)^2}{52/75}
 =\frac{27}{2600}>\frac{17}{2000}.
\tag{174}
```

The binomial tail outside the band is at most
$`2(a+1)2^{a h(.56)+O(1)}`$, hence is below $`N/2`$ after a fixed coordinate cutoff. The algorithm verifies the band by the exact integer tail comparison.

Write $`n_-=a-b`$ and $`n_+=b`$ for the exact owner-region sizes. Their ideal values are $`a(1/2-z)`$ and $`a(1/2+z)`$, respectively, with bounded rounding error.

### II.3.4. Physical profiles and background allocation

Choose each local useful cardinality layer, balanced layout and child role from its physical integer image before common-prime selection. Full selected-support size at least its Good threshold gives a useful physical layer/layout after a polynomial loss in the coordinate count alone; this gives the physical local-layer contrast of Section II.2. Include all such enumerated local images in the common-prime universe, together with the global exact-quota top images. Keep the selected local images and child roles fixed throughout the following top refinement. Once the common prime path makes the global top image good, retain one variation witness per occupied top residue; each witness belongs to a residual cyclic-layout branch from Section II.6.1. A polynomial pigeonhole leaves one branch with a reciprocal-polynomial fraction of these residues. Partition the top regions into a fixed number $`Q_{\rm grid}`$ of fine chunks and enumerate their support counts; repeat the same pigeonhole step for these profiles. The algorithm enumerates every branch, and the eligibility allowance includes these polynomial losses. Local images remain fixed.

For an actual top profile, put $`P_-=\prod_{C\subseteq H^c}\binom{|C|}{u_C}`$ and $`P_+=\prod_{C\subseteq H}\binom{|C|}{v_C}`$, where $`C`$ ranges over its fine chunks and fixed residual coordinates are singleton chunks. Write $`h_-=\log P_-`$, $`h_+=\log P_+`$, and $`r=u+v`$. The exact raw top-domain logarithms are

```math
L_L=n_-+h_++v,\qquad
L_R=n_++h_-+u,
\qquad
M_{\rm total}=m+h_-+h_++r.
\tag{175}
```

These use actual products, including sparse profiles. Since
$`P_-P_+\le Q`$, take the exact upper cap

```math
M_{\rm cap}=\frac{m+\log Q+r}{2}.
\tag{176}
```

Choose $`M_j\in[\max(m/2,L_j),M_{\rm cap}]`$ with sum $`M_{\rm total}`$. Then $`z_j=M_j-L_j\ge0`$ are background counts summing to $`m-a`$. The interval conditions follow as follows. The upper-sum condition is $`M_{\rm total}\le2M_{\rm cap}`$, from $`P_-P_+\le Q`$. The sum of the two lower bounds is handled by four cases. The both-$`m/2`$ case uses $`M_{\rm total}\ge m`$; the both-$`L_j`$ case uses $`m\ge a`$. The two mixed cases follow from
$`m/2\ge(1-p)\max(n_-,n_+)`$ up to bounded rounding. Each individual upper bound exceeds its raw lower bound when the following two inequalities hold with fixed slack:

```math
m-a\ge2|z|[1-h(p)-p]a,\qquad
m-a\ge[2|z|(1-p)-p]a.
\tag{177}
```

The first proves $`L_j\le M_{\rm cap}+O(\log a)`$, using
$`h_\pm\le n_\pm h(p)+O(\log a)`$; the second proves the mixed lower-sum cases. Also $`M_{\rm cap}\ge m/2`$.
With $`p=.05`$, $`|z|\le1/15`$, $`a=.9m+O(1)`$, their right sides are respectively less than $`.08m`$ and at most $`.069m`$, whereas $`m-a=.1m+O(1)`$. Thus every profile has a feasible interval pair after a fixed cutoff.

Use exact integer products to choose the background counts. Binary-search the least integer $`z_L\in[0,m-a]`$ satisfying $`z_L+L_L\ge m/2`$ and $`m-a-z_L+L_R\le M_{\rm cap}`$, and put $`z_R=m-a-z_L`$. Real interval feasibility shows that the other two bounds are missed by at most one. Both tests are monotone; squaring the domain products compares them with the integers $`2^m`$ and $`2^{m+r}Q`$. Accordingly,

```math
M_j\ge m/2-O(1),\qquad
M_j\le\frac{m+a[h(p)+p]}2+O(\log a).
\tag{178}
```

The fixed slack in (177) absorbs the binomial and quota-rounding corrections. Every one of the $`m-a`$ background coordinates is assigned.

Equation (178) supplies the actual movable mass required by the local atomic allocation in Section II.5; the local mask images and child roles remain fixed.

Substituting (173) and (178) into the child and restart resource formulas of Sections II.5 and II.7 gives the central top coefficients

```math
D_p=\frac{h(p)-p}{2},\qquad
A_p=\frac{h(p)-3p}{4},\qquad
f_p=\frac{h(p)+p}{8}.
\tag{179}
```

Equation (171) subtracts $`aD(t)`$ from both central raw and restart exponents and preserves the leaf coefficient. The checker enlargement affects incidence and tuple state only. Each fine-chunk factor has logarithmic size at most twice its coordinate count. With $`Q_{\rm grid}`$ fixed before the input, all layout, count-profile and residue-pigeonhole families have fixed polynomial size. Their logarithmic losses are polynomial factors. The fine-factor packing in Section II.5 incurs $`O(m/Q_{\rm grid}+Q_{\rm grid}\log(m+1))`$ error. The fixed grid and cutoff in Section II.8 place this error within the certified margins.

## II.4. Common modular filters and weighted covers

Let $`u=n+L+2`$. Every integer difference below has fewer than $`2u`$
binary digits. A pattern means a permitted selected mask together with
its signing or ownership label. Its image is a set of distinct integer
sums. For a distinct image $`X`$, define

```math
C_q(X)=\sum_{z\bmod q}f_z(f_z-1),
\qquad f_z=|\{x\in X:x=z\bmod q\}|.
\tag{180}
```

For $`h\ge4`$ there are at least $`2^h/(4h)`$ primes in
$`[2^h/(4h),2^h)`$. Indeed, for $`x=2^h`$ the central binomial
coefficient is at least $`2^x/(x+1)`$. Its valuation at each prime
$`p`$ is at most $`\lfloor\log_px\rfloor`$, by the factorial valuation
formula. Hence it is at most $`x^{\pi(x)}`$, so
$`\pi(x)\ge(x-\log_2(x+1))/h`$. Subtracting at most $`x/(4h)`$
smaller primes proves the claim; $`x`$ is composite.
A sieve constructs the pool. Conditioned on $`q\mid x-y`$, the condition
$`qp\mid x-y`$ is exactly $`p\mid(x-y)/q`$, including repeated prime
factors. The quotient has at most $`2u`$ distinct prime divisors. Thus a
uniform prime in this pool satisfies

```math
\mathbb E_p C_{qp}(X)\le8u^2 2^{-h}C_q(X).
\tag{181}
```

Call $`p`$ bad for $`X`$ if $`2^hC_{qp}(X)>80u^2C_q(X)`$.
At most one tenth of the pool is bad. If $`C_q(X)=0`$, every prime is
good. Let $`2^B`$ bound the total number of individual patterns;
For example, encode mask labels and the indices of the fixed layout
families and take
$`B=4n+100Q_{\rm grid}^2\lceil\log_2(n+1)\rceil+100Q_{\rm grid}^2`$.
The constructive families above have polynomial degree linear in
$`Q_{\rm grid}`$, so this bounds every label length. At each fixed prefix $`q`$, select
$`k=32(B+1)`$ prime positions with repetition. If $`b_A`$ earlier positions
were bad for pattern $`A`$, choose the next prime minimizing

```math
\sum_A2^{b_A+1_{\{p\text{ bad for }A\}}}.
\tag{182}
```

Its conditional mean is at most $`11/10`$ times the preceding sum.
After $`k`$ choices the sum is at most $`2^B(11/10)^k<2^{k/4}`$.
Each pattern is bad at fewer than $`k/4`$ positions. Every triple of
patterns therefore has a position good for all three.

Let $`\ell_0,\ell_L,\ell_R`$ be the natural image scales supplied by
the representations. Split the sorted scale increments into pieces
at most $`\lceil\ell_{\max}/16\rceil`$, retaining all three endpoints.
There are at most nineteen pieces. A piece smaller than four uses
factor one; every other piece uses (182). Branch over the selected
prime positions, stopping an image at its scale. This fixed-depth tree
has polynomial size. Every eligible triple has a path good at all
active stages. Its recorded moduli satisfy

```math
\frac{2^{\ell_i}}{\mathrm{poly}(u)}\le p_i\le2^{\ell_i},
\qquad
C_{p_i}(X_i)\le(80u^2)^{19}|X_i|^2/p_i.
\tag{183}
```

They form a divisibility chain, with
$`p_j/p_i\le2^{\ell_j-\ell_i}`$ when $`\ell_i\le\ell_j`$.
Skipping short pieces loses a constant factor. Cauchy--Schwarz gives

```math
|X_i\bmod p_i|\ge
\frac{p_i}{p_i/|X_i|+(80u^2)^{19}}.
\tag{184}
```

Eligibility means $`|X_i|\ge2^{\ell_i}/\mathrm{poly}(u)`$ with
a fixed polynomial. Fix an integer $`E_{\rm img}`$ larger than its degree and put
$`\delta=u^{-(2E_{\rm img}+400)}`$. After a fixed small-input cutoff every
eligible image on a common-good path has density at least $`\delta`$.

Process one image at a time, replaying the selected prime positions
to compute its bad count and accumulating (182). The physical
local-image scans in Section II.2.7 include all signing, layer and
layout labels, with Good-set membership tested outside the signing
loop. Their total cost per candidate is $`O^*(2^{c+r})`$.
Prime enumeration contributes $`2^{\ell_{\max}/16+O(1)}`$.
Ownership scans retain their actual owner count. Section II.8 bounds
all construction costs. The live arrays contain one image, its
residue frequencies and polynomially many prime positions; potential
values have polynomial bit length.

### II.4.1. A universal weighted translate cover

Suppose images $`I_A\subseteq\mathbb Z/p\mathbb Z`$ have density at
least $`\delta`$. Let $`c(\rho)\ge0`$ be an exact rational cost with
uniform mean $`\mu`$. If $`Q`$ pattern-offset pairs remain uncovered, let
$`\mathrm{cov}(\rho)`$ count those covered by $`\rho`$. Its mean
is at least $`\delta Q`$. When $`\mu>0`$, select a residue with score
at least the mean of

```math
\mathrm{cov}(\rho)-\frac{\delta Q}{2\mu}c(\rho).
\tag{185}
```

That mean is at least $`\delta Q/2`$. The selected residue covers at
least $`\delta Q/2`$ pairs and costs at most $`2\mu/\delta`$, since
$`\mathrm{cov}(\rho)\le Q`$. If $`\mu=0`$, all costs vanish and
use coverage alone. Repeating for
$`O(\delta^{-1}\log(Q+1))`$ rounds gives a polynomial-size list
$`\mathcal R`$ satisfying

```math
\mathcal R\cap(I_A+v)\ne\varnothing\quad\text{for all }A,v,
\qquad
\sum_{\rho\in\mathcal R}c(\rho)
\le\mathrm{poly}(u)\mu.
\tag{186}
```

For $`s`$ costs with positive means use the penalty
$`\delta Q\sum_i c_i(\rho)/(2s\mu_i)`$ in (185). This proves
(186) separately for each cost. Zero-mean terms are identically zero.

Find the residue by interval conditional expectation: bisect
$`[0,p-1]`$ and retain a child whose average score is at least its
parent's average. To sum coverage on an interval, generate one image
and its prefix-count array. Enumerate offsets, testing uncoveredness
by replaying the preceding residue list. A translated interval needs
at most two prefix queries. Cost prefix sums supply the other terms.
No pattern-offset table is retained.

For local covers, each signing retains its residue list, uncovered
count, current interval, and fixed normalizers. During one shared
selected-set scan visit every compatible signing and accumulate its
conditional scores. Generate its cost arrays in one reusable workspace.
Thus (160) pays support tests and image scans, while the remaining
cost and cache work is

```math
O^*\!\left(K(P_{\max}^2+2^{m-c}+P_{\max})\right)
\quad\text{time},\qquad
O^*(P_{\max}+K+2^{m-c})\quad\text{space}.
\tag{187}
```

Construct the cover once for a fixed outer configuration and top
residue; reuse it in every interval query. It covers the solution's
translated local image at its actual parent lift.

## II.5. Top projection and atomic local generators

### II.5.1. Projecting a useful integer layer

Let a fixed signed top base have $`b`$ coordinates, selected set $`T`$ of
size $`sb`$, and a cardinality layer with $`M`$ distinct sums. Orient the
layer by complementation inside $`T`$ so its size is at most $`sb/2`$.
Trim to the fixed cell divisibility as in Section II.2, losing only
a polynomial factor, and recanonicalize each retained sum in the
complete trimmed layer of $`T`$.

The balanced-cell family gives a layout into $`Q_{\rm grid}`$ equal
cells and a subfamily $`\mathcal F`$ of at least
$`M/\mathrm{poly}(b)`$ canonical masks with equal selected and
layer counts in each cell. The family of distinct projected masks from $`\mathcal F`$
on any union of cells is sum-injective. Otherwise
replacing the larger equal-sum projection in its full witness would
preserve both its cardinality and sum while decreasing the canonical
witness.

For completeness, write $`\mathrm{Ent}`$ for binary Shannon
entropy. Factoring joint probabilities proves the chain rule;
concavity of $`-\sum p_i\log_2p_i`$ shows that additional conditioning
decreases conditional entropy. For uniform $`D\in\mathcal F`$, expand
$`\mathrm{Ent}(D\cap U)`$ in coordinate order, where $`U`$ is a
uniform union of $`p`$ cells. Replace conditioning on earlier coordinates
of $`U`$ by conditioning on all earlier coordinates. Each coordinate
belongs to $`U`$ with probability $`p/Q_{\rm grid}`$, so

```math
\mathbb E_U\mathrm{Ent}(D\cap U)
\ge\frac{p}{Q_{\rm grid}}\log_2|\mathcal F|.
\tag{188}
```

Some union therefore has at least $`|\mathcal F|^{p/Q_{\rm grid}}`$
projected masks, all with distinct actual sums. Its size is
$`a=pb/Q_{\rm grid}`$, and the selected fraction and relative layer
cardinalities are unchanged. Thus a support threshold $`2^\ell`$ on
the base yields a projected permitted image of size at least

```math
2^{(a/b)\ell}/\mathrm{poly}(b).
\tag{189}
```

Enumerate the layouts and all cell unions of the prescribed size.
The number is polynomial with fixed degree, since $`Q_{\rm grid}`$ is
fixed. Choose $`p`$ divisible by four; downward grid rounding changes
the ideal $`a/m`$ by at most $`4/Q_{\rm grid}`$. All these are integer
images selected before common-prime construction. The signed
coordinates outside the projection remain ordinary top background.
The entire base-signing offset is restored once after the final join.

Let $`Q_L,Q_R`$ be the actual products of the permitted top-mask
binomial counts, and let $`F=m-a`$ background coordinates remain.
Choose $`z_L`$ nearest to
$`(F+\log_2Q_R-\log_2Q_L)/2`$, and put $`z_R=F-z_L`$.
This is an exact integer search comparing $`2^{2z_L}Q_L`$ with
$`2^FQ_R`$. When the background-feasibility inequalities below have
their fixed reserve, both counts are nonnegative after the cutoff.
The ancestor products $`A_j=2^{z_j}Q_j`$ then satisfy

```math
\begin{gathered}
\log_2A_j\le\tfrac12(F+\log_2Q_L+\log_2Q_R)+1
\le\tfrac m2+(\overline H-\tfrac12)a+1,\\
\log_2A_j\ge\tfrac m2+(\overline H-\tfrac12)a
 -O(Q_{\rm grid}\log(m+1)),
\end{gathered}
\tag{190}
```

where $`\overline H`$ is the actual mean of the two mask entropy rates.
The upper comparison uses exact product balancing and the binomial
upper bound. The lower comparison also uses the binomial lower bound
over the fixed number of cells. In particular
$`\overline H\ge1/2`$ supplies the movable-mass floor, while the upper
comparison gives incidence bounds with polynomial losses only.

### II.5.2. Biased top shells

Choose a strict top base of size $`b=\rho m`$ before its useful layer.
Its full support has deficiency $`d`$. Let $`s=21/50`$. Round the base
to the required fixed multiple so the shell size is exactly $`r=sb`$. Partition its $`r`$-subsets by dyadic
support size. If $`g`$ is the cardinality of a class with threshold
$`2^\ell`$, maximize $`2^\ell g`$. The fixed-layer trace theorem and
the gain certificates at $`s=.42`$ give

```math
\ell+\log g\ge[h(s)+s]b-\phi_0d-O(\log(m+1)),
\qquad
\phi_0=\begin{cases}.345,&x_0\le.05,\\.3575,&x_0>.05.
\end{cases}
\tag{191}
```

Here $`x_0`$ bounds the full top-block deficiency density, and strict
extraction preserves this density bound. Let the linear translate
cover of this class have $`K`$ centers. It satisfies
$`Kg\le\mathrm{poly}(m)2^b`$. Put

```math
\delta=sb-\ell,\qquad \kappa=\log K,\qquad \tau_0=1-h(s).
\tag{192}
```

Since $`g\le\binom br\le\mathrm{poly}(m)2^{h(s)b}`$,

```math
\delta+\kappa\le\tau_0b+\phi_0d+O(\log(m+1)),
\qquad \delta\le\phi_0d+O(\log(m+1)).
\tag{193}
```

Each center is a separate outer signing. For any original witness,
one center makes its selected top set belong to the class. Negating
that center's coordinates translates the target once. Coordinates
later returned to the background retain their signed weights.

**Physical projection.**

Fix an outer center. Pigeonhole its selected-set support by
cardinality, orient the smaller layer and apply (189) before common
primes. Projection scales the physical deficit to $`(a/b)\delta`$;
the outer code cost remains $`\kappa`$.

Write $`k\in[0,s/2]`$ for the smaller-layer fraction on the base and set

```math
\begin{gathered}
H_-=h(k),\quad H_+=h(s-k),\quad
\overline H=(H_-+H_+)/2,\quad H_0=h(s/2),\\
L_0=H_0-\overline H,\quad \Delta=H_+-H_-,\quad
D_0'=\tfrac12+s-H_0,\quad p=D_0'-\delta/b.
\end{gathered}
\tag{194}
```

The active density range makes $`p>0`$. Choose the ideal projected size

```math
a=\frac{pb}{p+L_0}.
\tag{195}
```

It gives the exact raw-resource identity

```math
-(\tfrac12+s-\overline H)a+(a/b)\delta+\kappa
=-D_0'b+\delta+\kappa.
\tag{196}
```

Thus the top raw contribution is at most
$`-D_0b+\phi_0d+O(\log(m+1))`$, with $`D_0=D_0'-\tau_0`$.
The corresponding restart contribution is also bounded by its central
base value. Its difference from that value is

```math
\frac{L_0a}{2p}(\delta/b-s)\le0.
\tag{197}
```

The leaf contribution satisfies
$`(\overline H/4-1/8)a\le(H_0/4-1/8)b`$ whenever
$`\overline H\ge1/2`$, as proved below. Projection therefore preserves
the required central resource bounds without scaling the outer code.

**Background feasibility.**

Let $`B=b/m`$. Balancing the actual top-mask products requires
$`a(1+\Delta)\le m`$. A sufficient uniform condition is

```math
1-B\ge\frac{28}{25}pB^2.
\tag{198}
```

For completeness, put $`c=s/2`$, $`t=c-k`$, and $`v=pB`$. The function

```math
F(t)=(\tfrac12+v)h(c+t)+(\tfrac12-v)h(c-t)
\tag{199}
```

has $`F(0)=H_0`$ and $`F'(0)=2v h'(c)`$. On
$`c\in[1/5,1/4]`$, $`0\le t<c`$, $`v\le1/5`$,

```math
-F''(t)=
\frac{c(1-c)-t^2-2v(1-2c)t}
{(\ln2)(c^2-t^2)((1-c)^2-t^2)}\ge\frac5{\ln2}.
\tag{200}
```

After subtracting five times the denominator without $`\ln2`$, the
numerator is at least
$`3/256+(29/16)t^2-(6/5)vt\ge3/256-(144/725)v^2>0`$.
Completing the square and using $`h'(c)\le2`$, $`\ln2<7/10`$, gives
$`F(t)\le H_0+(28/25)v^2`$. Therefore
$`L_0\ge p[B\Delta-(1-B)]`$, proving the sufficient condition.
Endpoint layers follow by continuity. The active choice $`B\le.85`$
satisfies it with a fixed margin, since $`p\le D_0'<.179`$ and
$`(28/25)(.179)(.85)^2<.15`$.

Retain only smaller layers with $`r/4\le k b\le r/2`$.
This retains a useful layer: the physical class bound gives
$`\delta/b\le(143/400)T=3861/80000<s/8`$, so its support entropy per
selected coordinate exceeds $`7/8-o(1)`$. A layer with relative
cardinality at most $`1/4`$ has entropy at most $`h(1/4)<5/6`$,
certified by $`3^9>2^{14}`$. The fixed gap absorbs layer, trimming,
and layout losses. Thus every original solution has a retained layer.

Every retained layer, useful or otherwise, satisfies $`k\ge s/4>.1`$
and $`s-k\ge s/2>.2`$. The exact integer comparisons
$`10^{20}>2^9 9^{18}`$ and $`5^{10}>2^{23}`$ give
$`h(.1)>9/20`$ and $`h(.2)>7/10`$. Hence

```math
\overline H>\frac{23}{40}>\frac12.
\tag{201}
```

Exact top-product balancing supplies at least
$`m/2+(\overline H-1/2)a+O(\log m)`$ movable logarithmic mass per
parent. The atomic-complement allocation therefore applies throughout
the enumerated layer range, rather than relying on eligibility for
each processed configuration.

**Incidence and resource bounds.**

For a full local block with deficiency $`d_j`$, the parent ambient
exponent, including the outer top code, is

```math
\frac{3m}{2}-d_j-(\tfrac12+s-\overline H)a
 +(a/b)\delta+\kappa.
\tag{202}
```

Adding the separator degree $`d_sa`$, its difference from the central
bound $`3m/2-d_j+\delta+\kappa-\tau_0b/2`$ is exactly

```math
-\frac{L_0a d_s}{p}\le0.
\tag{203}
```

The integer proxies satisfy $`d_j\ge x_0m-1`$ and
$`d\le m\beta(x_0,\rho)`$. Thus the central incidence excess per
coordinate is at most $`I+1/m`$, where

```math
I=\tfrac12\tau_0\rho+\phi_0\beta(x_0,\rho)-x_0.
\tag{204}
```

The additional one bit in the unnormalized exponent is a factor of two,
included in the polynomial factor. Section II.8 proves $`I<-1/1250`$ on the active
positive-deficiency interval. This margin pays fixed-grid projection
errors. The code rate is paid once in each outer solve, in its
preparation, and in every top-dependent residue cover; two outer
top signings are never combined by one compatibility checker.

For the local strict-core notation of the resource certificate, the
complete central upper bounds are

```math
\begin{aligned}
R&=-D_0\rho+e\sigma+\phi_0\beta(x_0,\rho)
                  +\phi\beta(x,\sigma),\\
Q&=\tfrac34-A_0\rho-r\sigma-x+\phi_0\beta(x_0,\rho)
                  +\phi\beta(x,\sigma),\\
F&=\max\{1-\sigma,\tfrac38+(H_0/4-1/8)\rho
                                  +(H-1/2)\sigma/2\},\\
A_0&=\tfrac34+s-\tfrac32H_0-\tau_0.
\end{aligned}
\tag{205}
```

The oriented-half local mode keeps its exact nonpositive compression
corrections. All definitions and inequalities here concern actual
integer images before modular reduction. Common primes are selected
only after those images are fixed. Universal local covers handle every
later background translation, and original-key signing unions retain
the full-block ambient bound without a local Cartesian code factor.

### II.5.3. The ordinary half-selected top

The high-tail mode uses a strict top base $`V`$ of size $`b=\rho m`$,
$`\rho=18/25`$. The prefix masks and their complements form a
polynomial signing family. Prefix flips take every original selected
cardinality from $`|S|`$ to $`b-|S|`$ in unit steps, so some signing gives
a half-selected set $`T`$. Its complementary signing gives $`V\setminus T`$.
Since $`N(V)\le N(T)N(V\setminus T)`$, one has support at least
$`\sqrt{N(V)}`$. Cardinality pigeonholing and (189) give a projected
permitted image at the exact inherited scale

```math
\ell_0=\left\lfloor\frac{a}{2b}\log_2N(V)\right\rfloor.
\tag{206}
```

Let $`N_0`$ be the original full top-block support. Deficiency density
decreases during extraction, so

```math
\ell_0\ge\left\lfloor\frac{a}{2m}\log_2N_0\right\rfloor,
\qquad f_0:=a/2-\ell_0\le\frac{a}{2m}d_0+1.
\tag{207}
```

Here $`d_0=m-\log_2N_0`$. These comparisons use the actual supports.

To choose the projected size uniformly over layers, set
$`h_0=h(1/4)`$ and $`p_0=1-h_0-\xi/2`$, where $`\xi\le.203`$ is the
nominal base-density bound. For a smaller-layer fraction
$`k\in[0,1/4]`$, put

```math
\overline H=\tfrac12[h(k)+h(1/2-k)],\quad
\Delta=h(1/2-k)-h(k),\quad
a_* =\frac{p_0\rho m}{p_0+h_0-\overline H}.
\tag{208}
```

The following sufficient conditions hold in this mode:
$`p_0>0`$, $`p_0\rho<1/5`$, and
$`1-\rho\ge(7/10)p_0\rho^2`$. Indeed $`h_0<.812`$,
$`\xi/2\le.1015`$, $`p_0<.19`$, and $`\rho=.72`$.
They imply $`a_*(1+\Delta)\le m`$ as follows.
Write $`t=1/4-k`$, $`r=p_0\rho`$, and

```math
F(t)=(\tfrac12+r)h(1/4+t)+(\tfrac12-r)h(1/4-t).
\tag{209}
```

Then $`F(0)=h_0`$, $`F'(0)=2r\log_23`$, and

```math
-(\ln2)F''(t)=
\frac{3/16-t^2-rt}{(1/16-t^2)(9/16-t^2)}\ge5.
\tag{210}
```

Subtracting five times the denominator leaves at least
$`3/256+(29/16)t^2-rt\ge3/256-4r^2/29>0`$.
Completing the square gives
$`F(t)\le h_0+2(\ln2)(\log_23)^2r^2/5<h_0+.7r^2`$.
The last strict comparison follows from $`\ln2<52/75`$ and
$`3^{200}<2^{317}`$. Since $`F=\overline H+r\Delta`$, the reserve
condition proves

```math
h_0-\overline H\ge p_0[\rho\Delta-(1-\rho)].
\tag{211}
```

This yields the asserted background feasibility and

```math
\begin{aligned}
(1-\overline H-\xi/2)a_*&=(1-h_0-\xi/2)\rho m,\\
(\overline H/2-1/4)a_*&\le(h_0/2-1/4)\rho m.
\end{aligned}
\tag{212}
```

Here $`1/2\le\overline H\le h_0`$. Round down to an enumerated
four-cell multiple. The reserve is strict, so actual integer mask
products admit nonnegative background counts after the fixed cutoff.
Use the actual binomial products to balance those counts within one
bit, as in the biased-top construction.

The all-layer separator of Section II.6 at selected fraction $`1/2`$
has common degree $`O^*(2^{(1-h_0)a})`$. If $`\Lambda_j`$ is the original
parent ambient exponent, exact product balance and (207) give

```math
\begin{aligned}
\Lambda_j+(1-h_0)a
&\le\tfrac32m-d_j+f_0-(h_0-\overline H)a+O(\log(n+L))\\
&\le\tfrac32m-d_j+\frac{a}{2m}d_0+O(\log(n+L))
\le\tfrac32m+O(\log(n+L)).
\end{aligned}
\tag{213}
```

The last step uses the least-deficient full top block, so $`d_0\le d_j`$.
Incidences retain this actual inherited scale separately from the
strict grid allowances used for raw and leaf resource bounds.

### II.5.4. Whole-complement supports and exact allocation

Fix a local core $`C\subseteq B_j`$ of size $`c\ge m/2-O(Q_{\rm grid})`$, chosen before
its signing and useful layer. Put $`T=B_j\setminus C`$. Store one indexed
witness per actual sum in $`\Sigma(T)`$, and write

```math
R_T=\log_2N(T)=m-c-d_T\le m/2+O(Q_{\rm grid}).
\tag{214}
```

The sorted support stream constructs this array in $`O^*(2^{m-c})`$
time and $`O^*(2^{m/2})`$ space, including generation state. Reuse it
across local signings. These coordinates are exclusive to this parent:
replacing a subset of $`T`$ by its stored equal-sum witness preserves
every compatibility condition.

A fixed local layer and balanced layout give mask families of exact
sizes

```math
W_1=\binom{c/Q_{\rm grid}}{k/Q_{\rm grid}}^{Q_{\rm grid}},\qquad
W_2=\binom{c/Q_{\rm grid}}{(r-k)/Q_{\rm grid}}^{Q_{\rm grid}}.
\tag{215}
```

Their images and child roles are fixed before top fine-profile
selection. Orient $`W_1\le W_2`$ and put $`B_i=\log_2W_i`$.
For every retained strict local layer, the quarter-layer lemma gives
$`B_2-B_1<(7/16)c+O(Q_{\rm grid}\log(m+1))`$.
The scalar policy gives $`c>.53m`$, so $`R_T<.47m`$.
The top allocation supplies movable ancestor factors of total
log-cardinality $`M_j\ge m/2-O(Q_{\rm grid}\log(m+1))`$ per parent.
These factors consist of allocated top-mask or coefficient choices and
ordinary background coordinates; the local image stays fixed.

Place the entire support array in child 1. Ideal balancing assigns the
movable masses $`E_1,E_2`$ as follows:

```math
E_1+E_2=M_j,\qquad E_1-E_2=B_2-B_1-R_T.
\tag{216}
```

Feasibility is equivalent to $`|R_T-(B_2-B_1)|\le M_j`$.
For strict local cores both nonnegative terms on the left are at most
$`.47m+O(Q_{\rm grid}\log(m+1))`$, leaving a fixed $`.03m`$ reserve.
For the oriented-half mode below each is at most $`m/2+O(Q_{\rm grid})`$, so clamping
the ideal target to the available interval incurs only
$`O(Q_{\rm grid}\log(m+1))`$ error.

Every small ancestor factor has logarithmic size at most
$`2m/Q_{\rm grid}+O(\log(m+1))`$; a free coordinate is one factor of
size two. Order the factors and take an initial segment whose product
first crosses the target. The overshoot is at most one factor.
The target comparison is exact: compare the squares of the two
integer partial domain sizes against their fixed total product.
Only ancestor factors and top background move between children;
each local mask family remains in its prescribed child.
The resulting raw child logarithms differ by
$`O(m/Q_{\rm grid}+Q_{\rm grid}\log(m+1))`$ from

```math
\beta_j=\frac{M_j+R_T+B_1+B_2}{2}.
\tag{217}
```

The ambient histogram always uses distinct sums of the entire
original full local block $`B_j`$. The support-array histogram counts
its distinct entries once; all mask factors retain their indexed raw
labels. In particular, compression does not add another independent
copy of the complement to the ambient domain.

### II.5.5. Raw factors and atomic leaves

A raw child domain is the Cartesian product of its assigned ancestor
factors, one prescribed local mask family, its assigned free coordinates,
and possibly the one atomic support array. Each mask factor specifies
an exact coordinate cell and cardinality. Each coefficient factor
specifies its allowed assignments on its cell. A raw record contains
its exact signed weight and all indexed mask or coefficient choices;
a support entry includes its stored original witness.
These factor records determine every later overlap and compatibility
test. Allowed top-label prefixes are imposed on their corresponding
factors before constructing the leaves.

Split a child's small factors between two stored raw leaves. If its
atomic factor has logarithmic size $`R_T`$ above half the child-domain
logarithm, put that factor alone in one leaf. Otherwise start with
that factor and add small factors until first crossing half. A child
without an atom starts with an empty first leaf. Thus the larger leaf
has logarithmic size at most

```math
F_j\le\max\{R_T,\beta_j/2\}
       +O(m/Q_{\rm grid}+Q_{\rm grid}\log(m+1)).
\tag{218}
```

Enumerate each leaf explicitly and sort it with its full witness.
Repeated weights retain distinct occurrence IDs. The support atom is
the only factor deduplicated by weight at this stage.

Let $`\overline\beta`$ be the uncompressed central analytic upper
budget for one child. Across $`K`$ local signings, the filtered-child
budget is $`\overline\beta-\ell+\log_2K`$, and summed leaf starts have
budget $`\max\{R_T,\overline\beta/2\}+\log_2K`$.
The active policies satisfy
$`\overline\beta-\ell>.56919m`$ and
$`\overline\beta/2-r>.05959m`$ before the declared finite losses.
For strict local cores these follow from
$`3/4-(.45+.5-h(.225))>.56919`$ and
$`3/8-(.45+.25-h(.225)/2)>.05959`$;
the oriented-half bounds are larger.
Since $`\ell\le r`$, $`R_T\le m/2+O(Q_{\rm grid})`$, and the dictionary exponent is below
$`.548m`$, the filtered analytic budget pays capacity and both terms
of the summed leaf initialization. This includes empty pruned calls.

For lift accounting we also need the actual unrestricted child domains.
Concavity gives
$`B_1+B_2\ge h(\theta)c-O(Q_{\rm grid}\log(m+1))`$.
Moreover $`N(B_j)\le2^cN(T)`$, so $`d_T\le d_j`$.
Together with $`M_j\ge m/2-O(Q_{\rm grid}\log(m+1))`$ this yields

```math
2\beta_j\ge\frac{3m}{2}-[1-h(\theta)]c-d_T
                 -O(Q_{\rm grid}\log(m+1)).
\tag{219}
```

For strict locals $`\theta=.45`$, and for the oriented-half mode
$`\theta=.5`$. In either case $`1-h(\theta)<.015`$ and
$`d_T\le d_j\le.203m+O(1)`$. Each unrestricted child therefore has
more than $`2^{.64m}/\mathrm{poly}(n)`$ occurrences after the fixed
cutoff. Interval and prefix restrictions use the upper initialization
budget above.

### II.5.6. Oriented local halves

The main algorithm takes $`4\mid m`$. Split a local full block into
two fixed equal halves and orient them as $`A,T`$ so that $`N(A)\ge N(T)`$.
Move fewer than $`2Q_{\rm grid}`$ coordinates from $`A`$ to $`T`$ so that
$`c=|A|`$ is a multiple of $`2Q_{\rm grid}`$.
Removing a coordinate decreases deficiency; adding one increases it.
Thus, writing $`d_A,d_T`$ for the resulting deficiencies and using
$`N(B_j)\le N(A)N(T)`$, we retain

```math
d_A\le d_T,\qquad d_A+d_T\le d_j.
\tag{220}
```

Use the support array of $`T`$ as the atom. On $`A`$, enumerate each
prefix signing and its complement. For every original selected mask,
prefix flips change its cardinality by one at a time from its original
size to its complementary size; one attains $`|A|/2`$.
The selected half $`S`$ and its complement, in the signed weights, satisfy
$`N(S)N(A\setminus S)\ge N(A)`$. One of the two complementary signings
therefore gives a selected half with support at least $`\sqrt{N(A)}`$.
Its natural scale is
$`\ell_A=\lfloor\log_2N(A)/2\rfloor`$.
Pigeonholing, complementation inside this selected half, and the
balanced-cell construction give a useful smaller layer with only
polynomial support loss.

The two local mask families have total selected size $`|A|/2`$ and
mean entropy $`1/2\le\overline H_A\le h(1/4)`$. Their contrast is at
most $`c=m/2-O(Q_{\rm grid})`$, and $`R_T\le m/2+O(Q_{\rm grid})`$,
so the allocation above applies. Replacing $`c`$ by $`m/2`$ incurs only
$`O(Q_{\rm grid})`$ in the following resource formulas.
Compared with the uncompressed half-core formula, compression reduces
each balanced child exponent by $`d_T/2`$ and raw-parent work by $`d_T`$;
the local filter adds $`d_A/2`$. The resulting corrections are

```math
(d_A-d_T)/2\le0,\qquad d_A/2-d_T\le0.
\tag{221}
```

For example, in an ordinary top representation let $`a`$ be the actual
top size, $`\overline H_0`$ its actual mean mask entropy, and
$`f_0=r_0-\ell_0`$ its physical image deficit, where $`r_0`$ is the
selected top size. Put $`h=h(1/4)`$ and $`u=1-h`$.
Before applying the top central-domination inequalities, the filtered
child and raw-parent budgets satisfy

```math
\begin{aligned}
\Gamma_{\rm half}
&\le\frac{3m}{4}+(\overline H_0/2-1/4)a-u\frac m2+O(Q_{\rm grid}),\\
J_{\rm half}
&\le\frac{3m}{2}-(1-\overline H_0)a
       +(2h-3/2)\frac m2+f_0,\\
\Lambda_j&\le\frac{3m}{2}-(1-\overline H_0)a-d_j+f_0.
\end{aligned}
\tag{222}
```

For a biased selected top fraction $`s`$, replace the top raw term
$`-(1-\overline H_0)a`$ by
$`-(1/2+s-\overline H_0)a`$; the child coefficient stays unchanged.
An outer top-code logarithm is added once to each summed solve budget.
The actual top entropy is retained until its central-domination lemma
is applied. The ambient histogram still uses the original full local
block. The stored-leaf bound is
$`\max\{m/2,(1/4+h/4)m+(h/4-1/8)a\}`$ up to the declared finite
losses; it is below $`.523m`$ for $`a\le.9m`$.

### II.5.7. Fixed granularity and arithmetic

Choose $`Q_{\rm grid}`$ as a fixed multiple of four, independently of
the input. Required integer divisibilities and layer trimming change
$`O(Q_{\rm grid})`$ coordinates. Binomial estimates, fixed-power root
enclosures, and the fixed number of count refinements add
$`O(Q_{\rm grid}\log(m+1))`$ to exponent bounds. Every stored sum,
count, factorial and exact comparison has polynomial bit length in
$`n,L`$, with fixed constants depending on $`Q_{\rm grid}`$.

A union of a multiple of four cells approximates an ideal projected
top size within $`4m/Q_{\rm grid}`$. The small-factor packing above and
the subsequent leaf split each miss their targets by at most
$`2m/Q_{\rm grid}+O(\log(m+1))`$.
The relevant raw, child, restart and leaf coefficients have absolute
value at most one. Their combined charge is bounded by
$`20m/Q_{\rm grid}+O(Q_{\rm grid}\log(m+1))`$; the global certificate
uses the conservative allowance

```math
100m/Q_{\rm grid}+O(Q_{\rm grid}\log(m+1)).
\tag{223}
```

Fix $`Q_{\rm grid}=10^{12}`$ and then a fixed coordinate cutoff as
specified in the resource certificate. Smaller instances are solved
directly. All factors polynomial in the arbitrary input length $`L`$
remain explicit polynomial factors. Incidence normalization uses
actual integer product counts.

## II.6. Compatibility and ordered generation

### II.6.1. Assignment containers

The following primitive is deterministic. A zero support uses one empty container. On $`n`$ coordinates, with ternary support size $`k`$ and container length $`2k\le l\le n`$, let
$`N_k=\binom nk`$, $`A_k=\binom lk`$, $`p_k=A_k/N_k`$. Choose

```math
\nu=\left\lceil16(n+1)/p_k\right\rceil,\qquad
L_k=\lceil4\nu p_k+8(n+1)\rceil.
\tag{224}
```

A multiset of $`\nu`$ containers can cover every support while giving each support fewer than $`L_k=O(n)`$ containing indices. For independent random containers, the potential
$`\#\{\text{uncovered supports}\}+\sum_B2^{\deg(B)-L_k}`$
has expectation
$`N_k(1-p_k)^\nu+N_k2^{-L_k}(1+p_k)^\nu<1`$.
Indeed $`N_k\le2^n`$, $`\nu p_k\ge16(n+1)`$, $`1-p_k\le e^{-p_k}`$ and $`\log_2(1+p_k)\le2p_k`$ bound each term by less than $`1/2`$.
Fix one container at a time by minimizing its exact conditional expectation. The mean over candidates is the previous value, so the final potential remains below one, forcing complete coverage and every degree below $`L_k`$. After $`i`$ choices the conditional expectation is

```math
(1-p_k)^{\nu-i}U_i+
2^{-L_k}(1+p_k)^{\nu-i}\sum_B2^{d_i(B)}.
\tag{225}
```

For a proposed next container and $`s=\nu-i-1`$, comparisons use the common-denominator integer score
$`2^{L_k}(N_k-A_k)^sU_Y+(N_k+A_k)^s\sum_B2^{d_Y(B)}`$.
Its bitlength is $`O(n\nu)`$. The central binomial bound gives
$`N_k/A_k\le(2k+1)\binom nk4^{-k} \le(n+1)\sum_{j=0}^n\binom nj4^{-j}=(n+1)(5/4)^n`$.
Schoolbook arithmetic, a scan of all supports for each candidate, and all rounds cost at most
$`O^*(2^{2n}\nu^3)=O^*((125/16)^n)<O^*(2^{3n})`$.
Support flags/degrees, selected containers and the large operands occupy $`O^*(2^n)`$ state.

For every selected container $`Y`$ and binary assignment $`s`$ on $`Y`$, use the rectangle consisting of binary $`x`$ with $`x|_Y=s`$, and ternary $`y`$ supported on a $`k`$-subset of $`Y`$ with $`y_i=(-1)^{s_i}`$ on that support. All pairs have binary sums, and every compatible pair is covered. Binary degree, ternary degree and tuple count are respectively

```math
O^*(N_k/A_k),\qquad O^*(2^{l-k}),\qquad O^*(N_k2^l/A_k).
\tag{226}
```

Build a support-to-container index by enumerating each container's $`k`$-subsets. Its length is $`\nu A_k=O^*(N_k)`$, with polynomially many indices per support. A ternary query enumerates just these indices and the permitted assignment extensions. This realizes the degree bound as an actual query-time bound.

For the degree calculation take $`t\ge0`$; for $`t<0`$, interchange the two region names and parent roles. Write
$`n_\pm=a(1/2\pm z)`$, $`k_\pm=pn_\pm`$.
Set $`h=h(p)`$, $`g=h-3p>0`$. Initially use container length $`2k_\pm`$. The full right degree exceeds the left by $`C=2zag`$. Enlarge the plus-region container by $`w`$, keeping the minus-region length unchanged. Define

```math
E(l,k)=l[1-h(k/l)],\qquad
2w-E(2k_++w,k_+)=C.
\tag{227}
```

The binary degree on the enlarged region decreases by $`w-E`$, while its ternary degree increases by $`w`$. Thus (227) equalizes the full parent degrees.

For $`p=1/20`$ and $`|t|\le.06`$,
$`z\le1/15`$. The rational entropy certificate in Section II.8 gives $`h(.05)<.2864`$, hence $`g<7/50`$, so

```math
\frac C{k_+}
 =\frac{2z}{1/2+z}\frac gp
 \le\frac4{17}\frac{14}5=\frac{56}{85}.
\tag{228}
```

For $`l\ge2k`$, differentiation gives
$`E(2k,k)=E_l(2k,k)=0`$, $`0\le E_l<1`$, and
$`E_{ll}=k/[(\ln2)l(l-k)]`$.
Hence $`E(2k+w,k)\le w^2/(4k\ln2)`$.
The left side of (227) is strictly increasing with derivative greater than one. At $`w=3C/4`$,
$`E\le63C/(680\ln2)<C/2`$, using $`\ln2>1/2`$;
thus its value exceeds $`C`$. The unique root satisfies
$`0\le w\le3C/4`$, and its container fits with fixed slack:

```math
2k_++w\le(2+42/85)k_+=\frac{53}{425}n_+<n_+.
\tag{229}
```

Both complete checker degrees and the global assignment table therefore have logarithmic bounds

```math
D_{\rm side}=\frac a2[h(p)-p]+\frac E2+O(\log a),
\qquad
\log N_{\rm tup}=a h(p)+E+O(\log a).
\tag{230}
```

The positive binary-entropy series gives $`D(t)\ge2t^2/\ln2`$. Combining this with the curvature bound proves, for $`t\ne0`$,

```math
\frac{E}{2aD(t)}
 \le\frac{9g^2}{32p(1-2p)^2}
 \le\frac{49}{360}<\frac38.
\tag{231}
```

At $`t=0`$, use the original containers and $`E=0`$.
Integer container lengths bracket the monotone degree crossing. Expanding entropy at rational arguments converts each sign test to a comparison of integer powers with polynomial bitlength. Rounding an interior length changes exponents by $`O(\log a)`$; actual polynomial load caps are retained.

### II.6.2. Support-balanced tensorization

Use four subregions for container construction. For a support $`R`$ on an $`n`$-coordinate owner region, remove a residual set $`T`$ containing $`|R|\bmod4`$ supported and $`(n-|R|)\bmod4`$ unsupported coordinates. It has at most six coordinates. Enumerate every such $`T`$ and its support pattern. The remaining total and support cardinalities are divisible by four.

For any ordered even-size coordinate set with an even support, consider every cyclic interval containing half the coordinates. Its support count changes by at most one when the interval advances by one position. The opposite interval has the complementary support count. Discrete intermediate value therefore gives an interval with exactly half the support. Apply this twice: first divide the remaining region into two equal coordinate/support halves, then divide each half likewise. The four regions have equal coordinate counts and equal support counts.

Enumerating all cyclic choices at these three nodes gives a polynomial family. Every support is balanced by some branch. The residual coordinates remain explicit in all coefficient vectors and actual sums. Their checker enumerates binary assignments, with ternary signs forced on the fixed residual support; its cost is constant.

Suppose the original container ratio is $`\gamma=l/k`$. In each regular subregion, set $`l_i=\lceil\gamma k_i\rceil`$. On the active range $`k/n`$ is bounded away from zero and $`1/2`$, $`l/n`$ is bounded below one, and $`l/k`$ is bounded. Thus all four lengths are feasible after a fixed cutoff. Removing finitely many coordinates and rounding four lengths gives

```math
\begin{aligned}
\sum_i l_i&=l+O(1),&
\sum_i k_i&=k+O(1),\\
\sum_i n_i h(k_i/n_i)&=n h(k/n)+O(\log n),&
\sum_i l_i h(k_i/l_i)&=l h(k/l)+O(\log n).
\end{aligned}
\tag{232}
```

The tensor rectangles preserve (226) and (230) up to polynomial factors. Their support indices realize the same sided degrees. Construction runs on regions of size $`n/4+O(1)`$, so it takes
$`O^*(2^{3n/4})`$ time and $`O^*(2^{n/4})`$ construction state. The full assignment table, its initialization and clearing structure remain separately charged.

In the active band, $`|z|\le1/15`$, so the larger owner region has at most $`.51m+O(1)`$ coordinates. Construction therefore has exponents $`.3825m`$ and $`.1275m`$. The rational entropy enclosures from Section II.8,
$`h(.05)<.28639696<.2864`$ and $`D(.06)<.011`$, together with (231), give

```math
a h(p)+E
 < .9m[.2864+(3/4)(.011)]+O(\log m)
 =.265185m+O(\log m).
\tag{233}
```

This includes the tuple table and support incidence indices.

### II.6.3. Exact sided incidence

Combining (176) with the actual-quota form of (230) gives
$`M_j+D_{\rm side}\le m/2+\log Q+E/2+O(\log a)`$.
For original local full-support deficiency $`d_j`$, the ambient count after the natural top modulus and summing the threshold group's owners therefore has exponent at most

```math
\frac32m-d_j+d-aD(t)+E/2+O(\log n)
 \le\frac32m-d_j+d-\frac58aD(t)+O(\log n).
\tag{234}
```

Choosing a least-deficient original full block as top, and extracting without increasing absolute deficiency, gives $`d\le d_j`$. The independent sorted parent streams charge the two sided incidence counts separately. At a complementary actual weight, one representative per tensor rectangle is sufficient: every pair in that rectangle has binary coefficient sum. Each distinct parent key pays its own incidence degree once.

### II.6.4. All-layer ordinary separators

Let $`0<s\le1/2`$ be the selected top fraction. Group the retained
fine cells into four equal coarse regions. Their mask counts are
balanced independently of which raw child holds each factor.


For a cell of size $`g`$, let left and right counts be $`kg`$ and
$`(s-k)g`$. A separator must contain the left mask and avoid the right.
Set

```math
\alpha=1+\frac{\ln(2-s)}{\ln(1/(1-s))},\qquad
e(k)=\tfrac12+\alpha(k-s/2).
\tag{235}
```

The separator has $`e(k)g+O(1)`$ coordinates. Concavity of $`\ln`$ gives
$`s\ln(2-s)<-(1-s)\ln(1-s)`$, hence $`1<\alpha<1/s`$.
Consequently $`k<e(k)<1-s+k`$ throughout the layer interval.
Rational logarithm enclosures and integer rounding determine a
feasible size with only $`O(\log g)`$ exponent error.

The left degree exponent is

```math
E_s(k)=(1-k)h\!\left(\frac{e-k}{1-k}\right)
 -(1-s)h\!\left(\frac{e-k}{1-s}\right).
\tag{236}
```

The right exponent is $`E_s(s-k)`$. Put
$`X=1-k`$, $`Y=e-k`$, $`Z=1-e`$, $`W=1-s-Y`$ and
$`G=(\ln2)E_s`$. Direct differentiation gives

```math
G''=1/X-\alpha^2/Z+(\alpha-1)^2/W.
\tag{237}
```

Since $`Z/X\le1`$ and
$`Z/W\le(1+\alpha s)/(1-2s+\alpha s)`$,

```math
ZG''\le
-\frac{2(1-s)(\alpha-1)}{1-2s+\alpha s}<0.
\tag{238}
```

The chosen $`\alpha`$ makes $`G'(s/2)=0`$. Both sided degrees are thus
at most $`O^*(2^{d_sa})`$ after taking products over cells, where

```math
d_s=E_s(s/2)=s-h(s/2)+h(s)/2.
\tag{239}
```

The family-size exponent is
$`T_s(k)=h(e)-(1-s)h((e-k)/(1-s))`$.
It is symmetric about $`s/2`$. Its second derivative has the sign of

```math
(1-s)[(\alpha-1)^2-\alpha^2(1-s)]/4
 +s\alpha^2(\alpha-1)^2(k-s/2)^2.
\tag{240}
```

At $`(k-s/2)^2=s^2/4`$, four times this upper bound equals
$`(1-\alpha s)P(\alpha)`$, where

```math
P(A)=(1-s)-(1-s)(2-s)A-s(1-2s)A^2-s^2A^3.
\tag{241}
```

For $`0<s\le1/2`$, $`P(\alpha)\le P(1)=s-1<0`$.
Hence $`T_s`$ is concave and $`T_s(k)\le T_s(s/2)=s`$.
The global tuple table has $`O^*(2^{sa})`$ entries.

For an integer region, write $`c,d`$ for its mask counts and $`e`$
for its separator size, and put

```math
B_g=\binom ge,\quad R_g=\binom{g-c-d}{e-c},\quad
H_L=\binom{g-c}{e-c},\quad H_R=\binom{g-d}e.
\tag{242}
```

Choose $`\nu=\lceil10(g+1)B_g/R_g\rceil`$ separators and load caps
$`K_j=\lceil2\nu H_j/B_g+4g+8\rceil`$. The potential is the number
of uncovered disjoint pairs plus $`\sum2^{\deg-K_j}`$ over both mask
families. The uncovered-pair term is at most $`3^g e^{-10(g+1)}`$. Each of the
two degree sums is at most $`2^{-3g-8}`$ by $`\log_2(1+p)\le2p`$;
therefore the expected potential is below one.
After fixing some separators, with $`r`$ choices left, its exact
conditional expectation is

```math
U_i(1-R_g/B_g)^r+
2^{-K_L}A_i(1+H_L/B_g)^r+
2^{-K_R}B_i(1+H_R/B_g)^r,
\tag{243}
```

where $`A_i,B_i`$ sum the current degree powers. Enumerate all next
separators and retain one no larger than the mean. A common positive
denominator makes every comparison integral. The final potential
below one gives complete coverage and both load bounds.

There are at most $`2^g`$ candidates per choice, $`\mathrm{poly}(g)2^g`$
choices, $`3^g`$ pair constraints and $`2^{g+1}`$ degree constraints.
Comparison integers have at most $`\mathrm{poly}(g)2^g`$ bits.
Schoolbook arithmetic gives $`O^*(2^{6g})`$ bit time and $`O^*(2^{2g})`$
state, including the support-to-separator indices. Four coarse regions
therefore cost $`O^*(2^{3a/2})`$ time and $`O^*(2^{a/2})`$ construction
state, in addition to the global tuple table $`O^*(2^{sa})`$.
The geometric families are reused under coordinate relabeling.

Store per-region compatible-index lists and enumerate their Cartesian
product for each parent label. A record pays its sided degree.
At a fixed complementary actual weight, retain one left witness per
tuple and query right witnesses through their compatible tuples.
Every pair in a tuple is disjoint. If a genuine pair shares a tuple,
any stored left representative has that weight and avoids the right
mask. Thus representative replacement preserves every match. Initialize
the table once per layout and clear touched entries by stamps; each
output key incurs one degree charge. At $`s=1/2`$, the bound is
$`d_s=1-h(1/4)`$, as used by the high-tail projection.

### II.6.5. Ordered child streams

Let $`p\mid P_{\max}`$, and impose a child residue modulo $`p`$. A pair of stored leaf arrays can be streamed in either order

```math
(w\bmod P_{\max},\ w\text{ increasing}),\qquad
((v-w)\bmod P_{\max},\ w\text{ decreasing}).
\tag{244}
```

Sort the second leaf by its residue modulo $`p`$, then modulo $`P_{\max}`$, then actual weight and occurrence ID. For each first-leaf occurrence, find the complementary $`p`$-slice and regard its pair sums as a row. In the direct order, traverse its residue groups cyclically forward from the first residue crossing the modular pivot, and traverse each residue in increasing actual weight. In the complementary order, traverse cyclically backward from the last residue at the complementary pivot, with decreasing actual weight inside a residue. A heap merges these sorted rows. Begin each cyclic traversal at a whole residue-group boundary, so repeated residues remain contiguous. Empty slices are skipped by their stored indices.

Initialization, arrays and mutable row-heap state are linear in the stored leaf lengths up to polynomial factors. Each advance costs polynomial time. A complete state copy costs its full size and shares only immutable arrays. Occurrence IDs distinguish all repeated values. Mask or coefficient-prefix restrictions are imposed on their fine factors before leaf generation, so they can only decrease the domains.

### II.6.6. The interval band join

Suppose the first child is ordered by $`(k,x\text{ increasing})`$ and the second by $`(k,y\text{ decreasing})`$, with equal primary keys imposing the desired parent residue. For an actual-weight interval $`[L,U]`$, maintain two forward cursors in the second stream. At a first occurrence $`(k,x)`$, the start cursor is its first same-key occurrence of weight at most $`U-x`$, or the first later key. The end cursor is its first same-key occurrence of weight strictly below $`L-x`$, or the first later key. Skip earlier keys in both cursors. Their half-open occurrence-position interval is exactly the set of eligible partners, including tied weights and both interval endpoints. Both cursors move forward because $`x`$ increases and the thresholds decrease within a key.

Keep a circular buffer containing the last $`B`$ occurrences consumed by the end cursor. If the partner window has length at most $`B`$, it is precisely the corresponding suffix of this buffer. Otherwise copy the start state and replay the entire window, then discard the copy. If the mutable state size is $`S_0`$, there are at most $`J_I/B`$ such copies, where $`J_I`$ counts all potential reported pairs in the interval. Thus the join has time and space

```math
O^*(N_1+N_2+B+(S_0/B)J_I+J_I),\qquad
O^*(S_0+B),
\tag{245}
```

in addition to original leaf initialization. The same upper bound applies to early termination, charging a final copy to its potential window. The buffer persists across primary keys and uses absolute occurrence positions; its full capacity is initialized only once per join. Set $`B=C`$, where $`C`$ is the dictionary capacity. The certified leaf bound gives $`S_0=O^*(C)`$, so each interval call costs
$`O^*(F+G+C+J_I)`$: $`F`$ pays leaves and initialization, $`G=N_1+N_2`$ counts filtered-child occurrences, and $`J_I`$ includes all raw parent pairs, including local overlaps rejected afterward.

### II.6.7. Original-weight unions over local signings

Fix one parent's outer layout, moduli, top residue and lift. For a local signing mask $`D`$, set $`w_i^D=(-1)^{D_i}w_i`$ and $`\delta_D=w(D)`$. Disjoint signed-core masks $`A,B`$ reconstruct the original subset $`(A\cup B)\oplus D`$, with

```math
w((A\cup B)\oplus D)=\delta_D+w^D(A)+w^D(B).
\tag{246}
```

Use the parent-offset convention: a requested original interval $`I`$ and parent residue $`v`$ become $`I-\delta_D`$ and $`v-\delta_D\pmod {P_{\max}}`$ inside the signed child join. Restore $`\delta_D`$ exactly once before key insertion. The top label is unchanged: an indexed mask in ordinary mode or the complete coefficient vector in ownership mode. Any fixed outer top offset in ordinary mode is already included in the branch's target convention; ownership weights are direct original coefficient weights.

A capped query maintains one dictionary of original keys $`(w,\text{top label})`$. Sequentially enumerate local signings and their cached polynomial lists of residue seeds, run the restricted band join, reject invalid local overlaps, restore the original witness, and insert the key. Stop the whole query at $`C+1`$ distinct keys. Free a signing's child states before processing the next signing. If generation completes, retain any original witness per key: differing local witnesses use only exclusive coordinates, so top compatibility is unaffected.

Let $`F_D`$ include all initialization under the cached seeds of signing $`D`$, let $`G_D(v)`$ count its filtered-child scans, and let $`J_D(I,\pi,v)`$ count its raw labeled parent tuples in the requested interval and top-prefix cell. With the polynomial seed multiplicities included, the query costs

```math
O^*\!\left(C+\sum_D(F_D+G_D(v))
                 +\sum_DJ_D(I,\pi,v)\right),
\qquad
O^*\!\left(C+\max_DF_D\right)\text{ live generation space}.
\tag{247}
```

The single dictionary is shared across all signings. Raw tuples keep their signing, seed and occurrence labels for charging; equal original output keys are deduplicated across those labels.

Every output uses an original subset of the entire exclusive full local block. Consequently its distinct-key histogram $`U(v)`$ is bounded by the ambient histogram $`V(v)`$ formed from original full-local distinct sums, allowed top labels and allocated ordinary top-background occurrences. This bound contains no signing multiplicity. Local image/cover preparation is completed before interval recursion; only polynomial seed lists and scalar states are cached per signing, while temporary image and histogram arrays are regenerated sequentially. Their separate preparation costs and cache space are included in the global resource accounting.

### II.6.8. Independent sorted streams

We prove a general conversion for a single parent. Let $`U`$ be the number of distinct valid original keys, $`J`$ the number of raw labeled occurrences, and suppose a restricted interval/prefix query has time
$`O^*(K+J_{I,\pi})`$ and state $`S`$, including after early termination. For (247),

```math
K=C+\sum_D(F_D+G_D),\qquad J=\sum_DJ_D.
\tag{248}
```

Choose an integer interval containing all possible original actual weights, with polynomial-bit endpoints; the sum of absolute input weights gives such a bound, enlarged by a constant factor for raw coefficient ranges if necessary. Traverse a binary tree of key cells depth first. A cell is an actual-weight interval and, only at a singleton weight, a top-label prefix. Run its capped query. If it finishes with at most $`C`$ keys, close the raw generator, sort the completed dictionary, and expose its records. If it reaches $`C+1`$ keys, discard the dictionary and generator, then split a nonsingleton weight interval at its midpoint. At a singleton weight, split by the next top-label bit. A full label prefix contains at most one key and cannot overflow. For increasing output, visit lower weight intervals first; for decreasing output, visit upper intervals first. Prefix order within a weight may be fixed lexicographically.

Every valid key lies in a unique terminal cell, so it is emitted once. The weight order of cells and sorting within completed dictionaries make the stream globally ordered, with complete equal-weight groups contiguous. A paused stream holds only its completed dictionary and scalar traversal frames. Ancestors retain no dictionaries or raw generator state.

The tree depth $`H`$ is polynomial in $`n+L`$, from the endpoint bitlength and the $`O(a)`$-bit top label. At a fixed depth, overflowing cells are disjoint and each contains more than $`C`$ valid keys; hence there are at most $`U/(C+1)`$ such cells. The entire binary tree has $`O(1+HU/C)`$ nodes, including empty children. Every raw occurrence, valid or invalid, has a well-defined original weight and top label and lies in at most one cell per depth. Thus
$`\sum_{\text{cells}}J_{I,\pi}\le O(HJ)`$. Sorting completed dictionaries costs $`O^*(U)`$, giving the total stream bound

```math
O^*(K(1+U/C)+J)\text{ time},\qquad O^*(C+S)\text{ space}.
\tag{249}
```

This is a total-time bound; it includes empty streams and all starts. Original-weight offsets merely translate a signing's query interval and do not change the unique cell used in the occurrence charging.

Construct the left stream in increasing actual weight and the right stream in decreasing actual weight. Compare a left weight $`w_L`$ with the increasing transformed right key $`t'-w_R`$. Advance the smaller key until they agree or a stream ends. At an agreement, consume the entire left weight group into the compatibility tuple table, then the entire complementary right group through that table. The fixed-weight representative argument proves soundness and completeness for ordinary separators or ownership rectangles. Both streams can be suspended during this process because each exposed dictionary was completed after closing its generator. A constant number of dictionaries and one active generation state suffice.

Let $`D_L,D_R`$ be the respective tuple degrees and $`N_{\rm tup}`$ the tuple-table size. Each distinct output key undergoes at most one incidence operation; raw duplicates have already been removed. With immutable incidence indices and once-only tuple initialization charged separately, the complete solve therefore satisfies

```math
\begin{aligned}
T=O^*\big(&K_L(1+U_L/C)+K_R(1+U_R/C)
          +J_L+J_R+U_LD_L+U_RD_R\big),\\
S&=O^*(C+S_L+S_R+N_{\rm tup}).
\end{aligned}
\tag{250}
```

All restart products are sided. The two local signing unions are scanned independently, and the original full-block ambient bounds control their distinct output keys. Generation stamps or touched-entry clearing charge per-weight table reuse to the already counted left incidences. Exact original indexed witnesses are combined at a compatible match and verified in the input instance.

## II.7. Original keys and covers shared across residue lifts

Fix the top representation, a layout, useful local layers, and a
common-good modulus chain. Write $`q_0`$ for its top modulus, $`p_j`$ for
the local modulus on side $`j`$, and $`P_{\max}`$ for the largest recorded
modulus. All divide $`P_{\max}`$. Let $`C=\lceil2^{q_*m}\rceil`$ be the
dictionary capacity specified in Section II.8.

### II.7.1. Restoring keys before taking the union

The original-key identity (246) restores each local center before
deduplication. Ordinary top keys use an indexed mask in the fixed
outer signing; ownership keys use the complete original coefficient
vector. A fixed-key witness can be replaced because all differing
local coordinates are exclusive to that parent.

Let $`V_j(v)`$ count an ambient family by original parent residue modulo
$`P_{\max}`$. It consists of every allowed top label, its assigned top
background choices, and every distinct sum of the original full local
block $`B_j`$. This contains all restored parent keys. For their union,

```math
U_j(v)\le V_j(v),\qquad Z_j:=\sum_vV_j(v).
\tag{251}
```

The same ambient bound serves every signing. Build its histogram from
the original support stream and the assigned top factors. Retained
keys and witnesses carry their exact indexed masks.

### II.7.2. Exact resource means

For one signing let raw child domains have sizes $`L_1,L_2`$, which
depend on the layout and permitted masks, not their signed weights.
Let $`C_{D1},C_{D2}`$ be occurrence histograms modulo $`P_{\max}`$;
raw occurrences include local overlaps and every generator label.
Fold them modulo $`p=p_j`$, obtaining $`A_D,B_D`$. Define

```math
\begin{aligned}
G_D(v,r)&=A_D[r]+B_D[v-\delta_D-r\bmod p],\\
J_D(v,r)&=\sum_{x\bmod P_{\max}:x=r\bmod p}
 C_{D1}[x]C_{D2}[v-\delta_D-x],\\
\mu&=(L_1+L_2)/p.
\end{aligned}
\tag{252}
```

The mean of $`G_D(v,r)`$ over $`r`$ is exactly $`\mu`$ for every $`v,D`$.
The quantity $`J_D`$ counts raw pairs subject to both congruences;
local disjointness is checked after reporting them.

For a top residue $`\eta`$, put $`H=P_{\max}/q_0`$. The left lift set
is $`\Omega_L=\{v:v=\eta\bmod q_0\}`$; the right set consists of
the complementary residues $`t'-v`$. Here $`t'`$ includes the entire
fixed top-signing offset. In the ownership case it is the original
target. Put $`Z_j(\eta)=\sum_{v\in\Omega_j}V_j(v)`$.
For each signing construct a local cover with three costs

```math
\sum_{v\in\Omega_j}G_D(v,r),\qquad
\sum_{v\in\Omega_j}G_D(v,r)V_j(v),\qquad
\sum_{v\in\Omega_j}J_D(v,r).
\tag{253}
```

Their means are $`H\mu`$, $`\mu Z_j(\eta)`$, and
$`A_D^{(0)}(\eta_j-\delta_D)/p`$, respectively, where
$`A_D^{(0)}(s)`$ counts unfiltered child pairs of signed total
$`s\bmod q_0`$, and $`\eta_j`$ is the prescribed side residue.
Apply (186) using separate normalizers. Summing over signings controls
the union query's scans, diagonal restart products, and raw pairs:

```math
\sum_{D,r\in\mathcal R_D,v\in\Omega_j}
G_D(v,r)U_j(v)
\le\mathrm{poly}(u)K\mu Z_j(\eta),
\tag{254}
```

where $`K`$ is the actual local signing count. The cover meets every
translated eligible image, including its unknown solution lift.

For the top cover, first aggregate the integer counts

```math
A_j^{\rm agg}(\eta_j)=\sum_D A_D^{(0)}(\eta_j-\delta_D).
\tag{255}
```

Use four costs $`A_j^{\rm agg}(\eta_j)/p_j`$ and $`Z_j(\eta)`$ for
$`j=L,R`$. Their uniform means are

```math
\overline J_j=\frac{K_jL_{j1}L_{j2}}{q_0p_j},
\qquad \overline Z_j=Z_j/q_0.
\tag{256}
```

The top weighted cover bounds each cost by a polynomial times its
own mean and preserves every eligible top representation. Integer
aggregation precedes normalization, so intermediate numerators and
denominators have polynomial bit length. Each local cover uses only
three normalizers at a time.

### II.7.3. Summing the independently generated streams

Let $`F_{jD}`$ bound leaf initialization for signing $`D`$, and $`d_j`$ be
the side's checker degree bound. Section II.6 supplies an independent
ordered stream of distinct parent keys at cost

```math
O^*\!\left[
\left(C+\sum_D(F_{jD}+G_D(v))\right)
\left(1+\frac{U_j(v)}C\right)+\sum_DJ_D(v)
\right].
\tag{257}
```

Merge the streams in opposite actual-weight order; their costs add.
Summing (257) over lifts and the local and top cover lists gives

```math
O^*\!\left[
\sum_{j=L,R}\left\{
H\left(C+\sum_DF_{jD}+K_j\mu_j\right)
+\left(C+\sum_DF_{jD}+K_j\mu_j\right)
\frac{\overline Z_j}{C}
+\overline J_j+\overline Z_jd_j
\right\}+N_{\rm tuple}\right].
\tag{258}
```

Allocate the checker table of size $`N_{\rm tuple}`$ once for a fixed
layout; stamps clear only touched entries between weight groups.
Each distinct parent key incurs one checker-degree charge. The
ambient bound and independent stream construction give exactly the
diagonal restart products in (258).

To construct the costs, fold the ambient histogram on its lift coset
modulo $`p`$. The resulting seed counts satisfy:

```math
\sum_vG_D(v,r)V_j(v)
=A_D[r]\sum_sV_s+\sum_sV_sB_D[s-\delta_D-r].
\tag{259}
```

A quadratic cyclic convolution gives the full seed vector. Folding
$`C_{D2}`$ modulo $`q_0`$ similarly gives

```math
\sum_{v\in\Omega_j}J_D(v,r)
=\sum_{x\bmod P_{\max}:x=r\bmod p}
C_{D1}[x]C_{D2}^{(q_0)}[\eta_j-\delta_D-x].
\tag{260}
```

One $`P_{\max}`$-entry scan fills all seeds. Release one signing's
histograms before preparing the next; cache only its residue list.
Every interval restart reuses that list. Simultaneous state is
$`O^*(C+\max_DF_{jD}+P_{\max}+K_L+K_R+N_{\rm tuple})`$.

Every lift, including one with empty realized streams, incurs its
startup in (258). The identity

```math
H\mu_j=P_{\max}
\left(\frac1{L_{j1}}+\frac1{L_{j2}}\right)
\frac{L_{j1}L_{j2}}{q_0p_j}
\tag{261}
```

pays lifted child scans by the raw-pair mean when the unrestricted
balanced child domains exceed $`P_{\max}`$ by a fixed exponential
factor. Section II.5 proves this for every useful local layer.
The uncompressed analytic child budget in Section II.8 dominates
$`C+\sum_DF_{jD}`$ in the restart products. The baseline itself is bounded directly in Section II.8, retaining
the local cache and outer-label factors. That bound covers empty
calls separately from the output-dependent restart products.

## II.8. Parameters and complete resource bounds

Normalize the three full blocks to size $`m`$. Let $`x_0`$ be the least
full-block deficiency proxy and let $`x\ge x_0`$ be either local proxy;
each side is analyzed at its own $`x`$. More precisely, for actual
deficiency $`d_j=m-\log_2N_j`$, use
$`x_j=(m-\lfloor\log_2N_j\rfloor)/m`$, so
$`x_jm-1<d_j\le x_jm`$. A positive deficiency term may therefore
use the proxy as an upper bound; a saving $`-d_j`$ becomes at most
$`-x_jm+1`$. Every displayed normalized ledger below suppresses this
bounded one-bit correction inside its polynomial factor. Extraction
uses monotonicity of $`\beta`$ for the upper proxy, while ambient support
and restart savings retain the one-bit allowance. The strict margins
and exact incidence estimates are consequently unchanged.

Use the potential $`\beta`$ of
Section II.1, with $`P_*=23/26`$ and $`\alpha_*=52/75`$. Fix

```math
q_{\rm circ}=\frac{137}{250},\qquad
X=\frac{17}{2000},\qquad T=\frac{27}{200},\qquad
B_{\max}=\frac{203}{1000}.
\tag{262}
```

The core policies use the design anchor $`q_{\rm circ}`$. Their actual
dictionary capacity $`2^{q_*m}`$ is specified below. The scalar functions
$`R,Q,F`$ bound, respectively, raw-parent time in excess of $`3m/2`$,
the restart capacity threshold, and stored leaves. The independent-stream
bound of Section II.7 therefore has raw and restart exponents at most
$`3/2+R`$ and $`3/2+Q-q_*`$. All terminating decimals in this section are
exact rationals.

### II.8.1. Exact scalar certificates

For the entropy comparisons use

```math
\begin{aligned}
L_-&=2\sum_{j=0}^{23}\frac1{(2j+1)3^{2j+1}},&
L_+&=L_-+\frac{2}{49\,3^{49}}\frac98,\\
S(z)&=\sum_{j=1}^{128}\frac{z^{2j}}{(2j)(2j-1)},&
E(z)&=\frac{z^{258}}{258\cdot257(1-z^2)}.
\end{aligned}
\tag{263}
```

For $`u\in(0,1)`$, put $`z=|1-2u|`$ in the logarithm and entropy bounds:

```math
1-\frac{S(z)+E(z)}{L_-}\le h(u)
\le1-\frac{S(z)}{L_+}.
\tag{264}
```

These inequalities certify the entropy bounds below. The only implicit
roots needed are

```math
\begin{aligned}
\frac{859560838307}{10^{12}}
&<t(X,.9)<\frac{859560838308}{10^{12}},\\
\frac{515456646931}{10^{12}}
&<t(X,.6305)<\frac{515456646932}{10^{12}}.
\end{aligned}
\tag{265}
```

At each listed interval endpoint $`P_*z-xt>0`$. Substitution gives
opposite signs in the increasing root equation
$`xt+(P_*-x)t^{52/75}=P_*z`$, equivalently in
$`t^{52}(P_*-x)^{75}-(P_*z-xt)^{75}`$. Thus (265), like
(264), is an integer comparison after clearing denominators.

### II.8.2. Ownership parameters

For $`0\le x_0\le X`$, put

```math
\begin{gathered}
p=.05,\quad \rho=.9,\quad
h_L=.28639695711<h(p)<h_U=.28639695712,\\
H=.76919282902>h(.225),\qquad
\tau=.00722554602>1-h(.45),\\
D=(h_L-p)/2,\quad A=(h_L-3p)/4,\quad f=(h_U+p)/8,\\
v=H-.5,\quad e=2H-1-.45+\tau,\quad r=.95-H-\tau,\\
C=.75-q_{\rm circ}+(D-A)\rho,\qquad
\sigma=\min\{1,(C-x)/v\}.
\end{gathered}
\tag{266}
```

For strict locals $`x<T`$, use $`\phi=.371,.375,.3875`$ on the
intervals cut at $`.03,.05`$. The ownership and local-allocation bounds
of Sections II.3 and II.5 give

```math
\begin{aligned}
R&=-D\rho+e\sigma+\beta(x_0,\rho)+\phi\beta(x,\sigma),\\
Q&=.75-A\rho-r\sigma-x+\beta(x_0,\rho)+\phi\beta(x,\sigma),\\
F&=\max\{1-\sigma,.375+f\rho+v\sigma/2\}.
\end{aligned}
\tag{267}
```

Here $`Q=q_{\rm circ}+R`$ whenever $`\sigma<1`$. Set
$`b_t=X(859560838308/10^{12})`$. Monotonicity of the potential and
(265) give $`\beta(x_0,.9)\le b_t`$. Direct substitution gives

```math
.99998<\sigma(X)<1,\qquad \sigma(T)>.53006,
\qquad C-v=.00849648632975<X.
\tag{268}
```

For $`x\le X`$, the bounds $`\beta(x,\sigma)\le x`$ and
$`\sigma\le1`$ give $`R<-.00030765`$. Also

```math
Q\le .75-A\rho-r\sigma(X)+\beta(x,\rho)-.629x
<.54769110.
\tag{269}
```

Indeed $`t(x,.9)`$ increases with $`x`$: at fixed $`t<1`$, the defining
right side $`xt+(P_*-x)t^{\alpha_*}`$ decreases with $`x`$.
Thus $`\beta(x,.9)\le(859560838308/10^{12})x`$ on this interval,
and the affine upper bound in (269) is largest at $`X`$.
For $`X\le x<T`$, proportional extraction gives

```math
R\le-D\rho+b_t+\frac{(e+\phi x)(C-x)}v.
\tag{270}
```

This is a concave quadratic, with critical point
$`(\phi C-e)/(2\phi)`$ clamped to the relevant interval. Its three
maxima satisfy:

| Interval | Maximum location | Strict upper bound |
|---|---|---:|
| $`[X,.03]`$ | $`29646127739029/2968000000000000`$ | $`-.00030589`$ |
| $`[.03,.05]`$ | $`.03`$ | $`-.00074738`$ |
| $`[.05,T]`$ | $`.05`$ | $`-.00181446`$ |

For example the first exact value is

```math
-\frac{1955191732793963624585813319}{6391714532250880000000000000000}.
\tag{271}
```
Consequently $`R<-.0003`$, $`Q<q_{\rm circ}-.0003`$, and
$`F\le.375+f\rho+v/2=.547441072186`$; the complementary atom is
below $`.47`$.

For $`T\le x\le B_{\max}`$ use oriented halves. With
$`h_0=374/461>h(1/4)`$ and $`U=1-h_0`$, their bounds are

```math
\begin{aligned}
R_h&\le-D\rho+(2h_0-1.5)/2+b_t
=-\frac{8711179803779801}{230500000000000000}<-.03779,\\
Q_h&\le .75-A\rho-U/2-T+b_t
=\frac{57308853692168787}{115250000000000000}<.49726,\\
F_h&\le.5.
\end{aligned}
\tag{272}
```

The inequality for $`h_0`$ also follows directly from
$`3^{1383}>2^{2192}`$.

### II.8.3. Biased middle parameters

For $`X\le x_0\le T`$, set

```math
\begin{gathered}
s=.42,\quad H_0=.741482739932>h(.21),\quad
\tau_0=.018546104967>1-h(.42),\\
H=.769192829014>h(.225),\quad
\tau=.007225546013>1-h(.45),\\
H_Q=.811278124460>h(.25),\\
D=.5+s-H_0-\tau_0=.159971155101,\\
A=.75+s-1.5H_0-\tau_0=.039229785135,\\
C=D-A=.120741369966,\quad f=H_0/4-.125=C/2,\\
v=H-.5,\quad e=2H-1-.45+\tau,\quad r=.95-H-\tau,\\
\rho=\min\{.605+3x_0,.85\},\quad Z=49/600,\quad
b=.75-q_{\rm circ}=.202.
\end{gathered}
\tag{273}
```

Take $`\phi_0=.345`$ for $`x_0\le.05`$ and $`.3575`$ afterward.
Use the preceding three local values of $`\phi`$ and, for $`x<T`$,
$`\sigma=\min\{1,(b+C\rho-x)/v\}>.53`$. The biased projection
and local allocation give

```math
\begin{aligned}
R&=-D\rho+e\sigma+\phi_0\beta(x_0,\rho)+\phi\beta(x,\sigma),\\
Q&=.75-A\rho-r\sigma-x+\phi_0\beta(x_0,\rho)+\phi\beta(x,\sigma),\\
F&=\max\{1-\sigma,.375+f\rho+v\sigma/2\}.
\end{aligned}
\tag{274}
```

The top term includes the actual outer code multiplicity. Two useful
bounds on the potential are

```math
\beta(x,z)\le xz^{4/3}\quad(92x\le17P_*),\qquad
\beta(x,z)\le xz^{7/5}\quad(161x\le11P_*).
\tag{275}
```

To prove the first, substitute $`t=z^{4/3}`$ and divide the defining
equation by $`z`$. For $`w=z^{1/225}`$ the resulting left side is
$`xw^{75}+(P_*-x)w^{-17}`$, which decreases to $`P_*`$ on $`0<w\le1`$
under the displayed hypothesis. The second uses
$`xw^{150}+(P_*-x)w^{-11}`$ and $`w=z^{1/375}`$.
Since $`T<17P_*/92`$ and $`.85<.95^3`$, the top term satisfies
$`\beta(x_0,\rho)<.95x_0\rho`$. Locally use
$`\beta(x,\sigma)\le x\sigma`$.

On the rising top define

```math
\begin{gathered}
B_0=b+.605C=.27504852882943,\quad k=3C=.362224109898,\\
a_c=B_0-v=.00585569981543,\quad
z_c=\frac{a_c}{1-k}=\frac{585569981543}{63777589010200}.
\end{gathered}
\tag{276}
```

The uncapped domain is $`x\ge a_c+kx_0`$. There

```math
R\le\overline R=-D\rho+(e+\phi x)\frac{B_0+kx_0-x}v
                      +.95\phi_0x_0\rho.
\tag{277}
```

At fixed $`x`$, its $`x_0^2`$ coefficient is $`3(.95)\phi_0>0`$.
On a diagonal edge it is
$`3(.95)\phi_0+\phi(k-1)/v \ge35091383426981/538385658028000>0`$; on the cap edge it is
$`3(.95)\phi_0>0`$. Hence maxima occur at boundary endpoints or
on a vertical boundary $`x_0=z`$. On such a boundary the only additional
candidate is $`x_*=[b+C\rho(z)-e/\phi]/2`$, clamped to that boundary.
Writing $`c_X=a_c+kX`$, the complete rising-domain certificate is:

| Top interval | Local interval | Vertices | Strict upper $`\overline R`$ |
|---|---|---|---:|
| $`[X,.05]`$ | $`[X,.03]`$ | $`(X,c_X),(X,.03),(z_c,z_c),(.03,.03)`$ | $`-.0001771431`$ |
| $`[X,.05]`$ | $`[.03,.05]`$ | $`(X,.03),(X,.05),(.03,.03),(.05,.05)`$ | $`-.0006064236`$ |
| $`[X,.05]`$ | $`[.05,T]`$ | $`(X,.05),(X,T),(.05,.05),(.05,T)`$ | $`-.0016602729`$ |
| $`[.05,Z]`$ | $`[.03,.05]`$ | $`(.05,.05)`$ | $`-.0046558153`$ |
| $`[.05,Z]`$ | $`[.05,T]`$ | $`(.05,.05),(.05,T),(Z,Z),(Z,T)`$ | $`-.0040912578`$ |

All entries follow by rational substitution at these candidates.
The first maximum occurs at
$`x_0=X`$, $`x=7574073885281873/742000000000000000`$.
On the plateau, $`\overline R`$ increases with $`x_0`$ at fixed $`x`$,
so maximize on $`x_0=x`$. This concave quadratic has critical point
$`8011512564987923/62000000000000000`$ and value below $`-.0037421981`$.
Thus the complete uncapped domain satisfies
$`R<-1/6000`$ and $`Q=q_{\rm circ}+R<.5478228569`$.

The cap has $`X\le x_0\le z_c<.01`$ and
$`x_0\le x\le a_c+kx_0<.01`$. Here $`\rho<.64`$,
$`.01<11P_*/161`$, and $`.64^2<.84^5`$, so (275) gives
$`\beta(x_0,\rho)<.84x_0\rho`$. Maximize raw work at
$`x=a_c+kx_0`$ and restart at $`x=x_0`$ to obtain

```math
\begin{aligned}
R_c&\le-D\rho+e+.84(.345)x_0\rho+.371(a_c+kx_0),\\
Q_c&\le .75-A\rho-r-.629x_0+.345\beta(x_0,\rho).
\end{aligned}
\tag{278}
```

The first is convex, and substitution at $`X,z_c`$ gives
$`R_c<-.0003827602`$. Along $`\rho=.605+3x_0`$, implicit
differentiation gives

```math
\beta'=t+x_0\frac{t^{\alpha_*}-t+3P_*}
 {x_0+\alpha_*(P_*-x_0)t^{\alpha_*-1}}
\le.635+.01\frac{1+3P_*}{\alpha_*(P_*-.01)}<.7.
\tag{279}
```

Here $`t\le\rho\le.635`$. Therefore $`Q_c'\le-3A-.629+.345(.7)<0`$.
Its maximum is at $`X`$; the second root bracket in (265) yields

```math
Q_c\le q_{\rm crit}:=\frac{54784907211651059}{10^{17}}.
\tag{280}
```

Outside the cap the raw-leaf term is $`.75-q_{\rm circ}/2+C\rho-x/2`$.
It decreases along the rising diagonal; its capped value increases up
to $`z_c`$. Hence $`F<.5477835481`$, including the complementary atom
below $`.47`$.

The biased incidence excess is bounded by

```math
I\le(\tau_0/2)\rho+.95\phi_0x_0\rho-x_0<-.0008968462<-1/1250.
\tag{281}
```

The expression is convex on each rising piece and decreases on the
plateau. Its endpoint tests are $`X,.05,Z,T`$, using both coefficients
at $`.05`$. For $`x\ge T`$, oriented halves instead give

```math
\begin{aligned}
R_h&\le-D\rho+(2H_Q-1.5)/2+\phi_0\beta(x_0,\rho)<-.0357253886,\\
Q_h&\le .75-A\rho-(1-H_Q)/2-x+\phi_0\beta(x_0,\rho)<.5262657137,\\
F_h&\le\max\{.5,.375+f\rho+(H_Q-.5)/4\}<.5041346134.
\end{aligned}
\tag{282}
```

Replace the top potential by $`.95x_0\rho`$ and $`x`$ by $`T`$ in $`Q_h`$.
The rising pieces are convex and the plateau is affine, so the same
endpoint list proves all three bounds.

### II.8.4. Proportional high tail and actual capacity

For $`T\le x_0\le x\le B_{\max}`$, take $`\rho_t=.72`$ and use
oriented local halves. Proportional extraction bounds the top deficit
by $`\rho_tx_0m`$. With $`h_0=374/461`$, $`U=1-h_0`$ and
$`A_0=1.25-1.5h_0`$,

```math
\begin{aligned}
R_t&\le-U\rho_t+(2h_0-1.5)/2+\rho_tB_{\max}/2
=-\frac{17503}{11525000}<-.0015,\\
Q_t&\le .75-A_0\rho_t-U/2-T+\rho_tT/2
=\frac{628599}{1152500}<.54543,\\
F_t&\le\max\{.5,.375+(h_0-.5)(\rho_t+1)/4\}
=\frac{11729}{23050}<.50886.
\end{aligned}
\tag{283}
```

The ordinary projection lemma applies throughout this closed domain:
$`p_0=1-h(1/4)-\xi/2>0`$, $`p_0\rho_t<1/5`$, and its sufficient
reserve $`.7p_0\rho_t^2<1-\rho_t`$ hold for $`0\le\xi\le.203`$.
For example $`p_0<.19`$, so the latter two inequalities follow already
from $`.19(.72)<.2`$ and $`.7(.19)(.72)^2<.28`$.

The largest resource threshold is (280). Choose

```math
\begin{gathered}
q_*=q_{\rm crit}+10^{-9}
=\frac{54784907311651059}{10^{17}},\\
B_*:=.75-q_*=\frac{20215092688348941}{10^{17}}<.203.
\end{gathered}
\tag{284}
```

For a full-block support of size $`N`$, the integer test
$`m-\lfloor\log_2N\rfloor\ge B_*m`$ implies true deficiency
$`d\ge B_*m-1`$. The high-deficiency interval algorithm then has

```math
T=O^*(2^{n/2}+2^{n/4}U/C),\qquad
S=O^*(2^{n/8}+C),\qquad
U\le O^*(2^{n/2-d}),\quad C=\lceil2^{q_*m}\rceil.
\tag{285}
```

The identity $`q_*+B_*=3/4`$ bounds its restart term by $`O^*(2^{n/2})`$.
Every remaining profile lies within the certified domain through
$`B_{\max}`$ after the fixed cutoff.

### II.8.5. Construction, startup, and state

The linear signing-code construction of Section II.2 has exponent
$`(1+\theta)c+\phi d`$ and is shared before outer top enumeration.
For strict locals, the uniform envelope

```math
\sigma\le\min\{1,(C_*-x)/v_*\},\qquad
C_*=.30463325,\qquad v_*=.26919
\tag{286}
```

gives code cost at most $`\sigma(1.45+.3875x)`$. It increases to
$`x_*=C_*-v_*=.03544325`$ and decreases thereafter, with maximum
$`1.45+.3875x_*<1.464`$. The actual local and outer label rates obey

```math
\begin{gathered}
\kappa_j<.00723+.3875T=.0595425,\qquad
\kappa_0<.85(.01855+.3575T)=.056790625,\\
\kappa_{\rm owner}\le.9X=.00765.
\end{gathered}
\tag{287}
```

Physical integer layers and layouts precede prime selection. For the
joint local universe $`(D,\mathrm{Good}T,\text{layer},\text{layout})`$,
test Good membership with the selected set outside the signing loop.
The inequality $`K|\mathrm{Good}|\le\mathrm{poly}(n)2^c`$
then bounds a candidate scan by $`O^*(2^{c+r})`$. Prime depth $`16`$
therefore gives exponent $`1+.45+.45/16=1.478125`$.
Both physical local images are fixed before allocating a top fine profile;
the owner-dependent work pays its actual outer multiplicity.

The retained layers also have uniform physical cardinality bounds.
For the biased top, $`\delta/A\le.3575T+O(\log A/A)<s/8`$;
for a strict local, $`\delta/c\le.3875T+O(\log c/c)<.45/8`$.
Every useful layer has entropy at least $`7/8-o(1)`$, whereas
$`3^9>2^{14}`$ gives $`h(1/4)<5/6`$. Orient the layer so that
$`k\le r/2`$ and retain $`k\ge r/4`$.
For top layers, $`k>.1A`$ and $`r-k>.2A`$. The exact inequalities
$`10^{20}>2^9 9^{18}`$ and $`5^{10}>2^{23}`$ give mean top entropy
above $`23/40`$. For strict locals, $`k\ge(.1125-o(1))c>c/9`$ and
$`r-k\le(.3375+o(1))c<.35c`$; the inequalities $`9^6>2^{19}`$ and
$`20^{80}<2^{75}7^{28}13^{52}`$ give contrast below $`7/16`$.
Together with $`c>.53m`$, this leaves at least $`.03m`$ reserve for
atomic allocation. These restrictions retain a representation of every
witness and depend on coordinate counts alone.

The remaining construction bounds, including their indicated label
multiplicities, are:

| Operation | Time exponent per $`m`$ |
|---|---:|
| Weighted ownership construction | $`1.3653`$ |
| Ownership top weighted covers | $`<1.42317`$ |
| Biased top linear code and top primes | $`<1.293`$ |
| Shared local linear codes | $`<1.464`$ |
| Shared physical-image local primes | $`1.478125`$ |
| Top-dependent local weighted covers | $`<1.465`$ |
| Signing histograms and full-support replay | $`<1.057`$ |
| Four-region tensorized containers | $`.3825`$ |
| Cached local and top layout families | $`\le1.45`$ |
| Ordinary high-tail separators | $`1.08`$ |
| Full-block counting and extraction | $`1`$ |

Here the ownership rows use, respectively,
$`1.5(.9)+2(.9X)`$ and $`(1+2h(.05))(.9)+.9X`$.
The biased top code costs at most $`1.42(.85)+.3575(.85)T`$;
its weighted covers cost at most $`1.42(.85)+\kappa_0`$, and adding
$`.45/16`$ bounds prime selection by $`1.293`$.
The local weighted-cover maximum is below
$`1.45+.635(.01855+.3575(.01))=1.464049375`$:
its diagonal core policy leaves the cap before $`.01`$, after which
the core-size derivative is below $`-2.3`$ and the conservative outer-rate
derivative below $`.448`$.
Histograms pay $`K_0K_j(P_{\max}^2+P_{\max}+2^{m-c})`$;
they are regenerated one signing at a time.
The layout family costs are at most $`1.45`$, $`.85(317/200)=1.34725`$,
and $`.72(317/200)=1.1412`$, using $`3^{200}<2^{317}`$.
The four-region ownership container has maximum region $`.51m`$,
giving preparation exponents $`3(.51)/4=.3825`$ in time and $`.51/4=.1275`$
in space.

For pure lift scans and starts, $`\log_2P_{\max}\le.45m+O(\log(n+L))`$
and the single-sign uncompressed child budget is below $`1.122m`$.
The local prime scales satisfy
$`\log_2p_j\ge(.45-.3875T)(.53)m-O(\log(n+L)) =.210774375m-O(\log(n+L))`$ for strict locals and
$`\log_2p_j\ge(.25-B_{\max}/4)m-O(\log(n+L)) =.19925m-O(\log(n+L))`$ for oriented halves.
The latter have local signing rate zero. Separating these modes gives

```math
\begin{aligned}
\text{strict:}\quad&.45+1.122-.210774375+.05955+.057
 =1.477775625,\\
\text{half:}\quad&.45+1.122-.19925+.057=1.42975,\\
\text{capacity and leaf starts:}\quad&.45+.548+.05955+.057
 =1.11455.
\end{aligned}
\tag{288}
```

All three are strictly below $`3/2`$. In restart products
the declared analytic filtered budget exceeds $`.56919m`$ and its leaf-minus-shell gap exceeds
$`.05959m`$. They pay capacity and summed initialization even for empty
pruned streams. For completeness, the two comparisons follow from
$`3/4-(.45+.5-h(.225))>.56919`$ and
$`3/8-(.45+.25-h(.225)/2)>.05959`$.
The actual unrestricted child entropies exceed $`.64m`$, above
$`\log_2P_{\max}`$; hence the exact product identity of Section II.7
also charges every lift for every modulus ordering.

Additional state has exponent at most $`.5`$ for supports and atoms,
$`.45`$ for ownership traces and residue arrays, $`.265185`$ for ownership
tuples, $`.357`$ for biased tuples, $`.36`$ for high-tail tuples,
$`.1275`$ for tensor preparation, $`.0595425`$ for local caches, and
$`.057`$ for outer labels. For the ownership tuple bound use
$`.9[h(.05)+.75D(.06)]<.265185`$, where
$`27/2600<D(.06)<.011`$ follows from (264). Each parent keeps one
dictionary of capacity $`2^{q_*m}`$; constantly many simultaneous arrays
add their sizes.

Finally choose

```math
Q_{\rm grid}=10^{12},\qquad
\varepsilon_{\rm fin}=200/Q_{\rm grid}=2\cdot10^{-10}.
\tag{289}
```

The fixed grid contributes at most $`100m/Q_{\rm grid}`$, and a fixed
coordinate cutoff bounds alignment, root-enclosure and combinatorial
losses by another $`100m/Q_{\rm grid}`$. This total is below
$`q_*-q_{\rm crit}=10^{-9}`$ and all other strict resource margins.
The preceding scalar bounds pay raw reports and restarts, while the
exact ownership and ordinary-half incidence normalizations give
$`O^*(2^{3m/2})`$ time. Biased incidence has the margin (281).
All construction costs and the scan/start bounds (288) are strictly
below $`3/2`$; their margins absorb the stated finite losses.
Thus all phases use time $`O^*(2^{3m/2})`$ and writable-bit space
$`O^*(2^{q_*m})`$, with the polynomial factors in the full input length
retained. Since $`n=3m+O(1)`$, the space exponent is exactly
$`q_*/3=18261635770550353/10^{17}`$.

## II.9. Complete algorithm and proof of Theorem 2

Enumerate at most twenty-three leftover coordinates so the remaining
instance has $`3m`$ coordinates with $`8\mid m`$. Its weights are still
arbitrary signed integers. A fixed small-coordinate range is handled
directly. Split the remaining coordinates into three full $`m`$-blocks,
and compute their exact supports $`N_j`$. Put
$`\widehat d_j=m-\lfloor\log_2N_j\rfloor`$, so
$`d_j\le\widehat d_j<d_j+1`$. Let $`q_*,B_*,X,T`$ be the exact
constants in Section II.8.

### II.9.1. A full block above the deficiency threshold

If some $`\widehat d_j\ge B_*m`$, place that entire block in a
coordinate half and fill the half arbitrarily. Its distinct support
has size $`U\le2^{3m/2-d_j}`$, with $`d_j\ge B_*m-1`$.
Use capacity $`C=\lceil2^{q_*m}\rceil`$.

Store raw eighth lists and generate each raw quarter as a sorted pair
stream. The band join of Section II.6 produces requested half-weight
intervals. Bisect an overflowing left interval, deduplicating by actual
weight; a singleton interval contains one key. For a fitting dictionary,
scan the complementary right interval and test exact membership.
The intervals on either side are disjoint at each recursion depth.

There are $`O^*(1+U/C)`$ starts, each scanning at most $`2^{3m/4}`$
quarter records, and at most $`2^{3m/2}`$ raw half pairs per depth.
Only the eighth lists and bounded dictionaries are stored. Therefore

```math
T=O^*\!\left(2^{3m/2}+2^{3m/4}U/C\right)
 =O^*(2^{3m/2}),\qquad
S=O^*(2^{3m/8}+C).
\tag{290}
```

The equality uses $`q_*+B_*=3/4`$ and the one-bit threshold tolerance.
Store a mask with each retained weight to recover its witness.

### II.9.2. The low-deficiency cases

Otherwise choose a largest-support full block as top and let
$`x_0=\widehat d_0/m`$. Each local proxy $`x`$ lies in
$`[x_0,B_*)`$. Use the exhaustive policy

| Top proxy | Representation | Top-base fraction |
|---|---|---:|
| $`0\le x_0\le X`$ | Equal-rate variable ownership, $`p=1/20`$ | $`.9`$ |
| $`X\le x_0\le T`$ | Biased shell, $`s=.42`$ | $`\min(.605+3x_0,.85)`$ |
| $`T\le x_0<B_*`$ | Half-selected top | $`.72`$ |

At a shared boundary either mode is valid. Choose each strict base
before its useful layer, rounding its size down to the required fixed
multiple. On either local side, $`x<T`$ uses the strict shell
$`\theta=.45`$ and its own certified core fraction; $`x\ge T`$ uses
the oriented-half construction. Thus mixed strict/half pairs are
included. Build balanced-cell families and unsigned local codes once
before the outer top-label loop.

In the ownership mode enumerate distances in the useful band,
owner/threshold groups and global top quota images. Fix the physical
local layers, layouts and child roles before common-prime selection.
After a common path makes the global top image dense, enumerate the
residual tensor layouts and fine profiles that retain its modular
witnesses. Their actual coefficient products determine the background
allocation. Every profile satisfies the clamp bound of Section II.3.

For either ordinary mode first enumerate the top signing, useful
integer layer, balanced layout and projected core. The biased mode
retains its full outer code count while projecting only physical image
loss. The half-selected mode retains its exact inherited support scale.
Construct common primes for these actual top and local images, then
allocate ancestor factors using their exact products. Whole local
complements remain indivisible support arrays.

For each common path and configuration construct the weighted top
residue cover. For each selected top residue, construct and cache the
per-signing local covers shared by every parent lift. Use one reusable
histogram workspace. At each lift generate the two independent streams
of restored original keys, and merge complementary actual weights
through the compatibility table. Release the branch data before
processing the next top residue.

### II.9.3. Correctness and complete resources

For any genuine witness, the linear local codes give two useful
selected sets. Their physical cardinality layers and layouts preserve
a reciprocal-polynomial fraction of their support, and the retained
quarter rule includes the winning strict layers. The ownership cover
or ordinary top signing supplies a useful top representation. In the
ordinary modes its projected integer image exists by Section II.5;
in the ownership mode a retained modular top profile exists by
Section II.3.

The common-prime family has a path good for this triple. The weighted
top cover retains its actual translated top contribution. Each universal
local cover retains its actual parent lift and ancestor offset. The
bounded original-key streams therefore emit a compatible pair at the
required actual weights. Representative replacement at a fixed key or
compatibility tuple preserves such a pair.

An accepted ownership pair has binary coordinatewise coefficient sums.
An accepted ordinary pair has disjoint indexed masks in its common
signed top instance. Local overlaps are checked before insertion into
the original-key dictionaries. Restore each exclusive local signing
once, and restore the whole ordinary top signing once, including the
coordinates returned to background. The retained masks then form an
original witness of target weight. Every configuration family is finite;
exhaustion therefore gives the correct NO decision.

Section II.8 bounds all raw reports, diagonal restarts, incidences,
construction, genuine lift loops and empty-call starts by
$`O^*(2^{3m/2})`$. Actual code and owner multiplicities are paid in
their respective loops. Only shared unsigned preparations are performed
once. The state bound includes every support atom, raw leaf, copied
heap, ring, residue array, cache, assignment index, tuple representative
and dictionary. Multiple simultaneous objects add their sizes.
The fixed grid and coordinate cutoff leave the stated positive reserve
above the critical capacity. All arithmetic, sorting, sieving and
conditional comparisons have the bit costs already charged; factors
polynomial in arbitrary full input length remain explicit.

Since $`n=3m+O(1)`$, the resulting bounds are

```math
\begin{gathered}
T=\mathrm{poly}(n,L)2^{n/2},\qquad
S=\mathrm{poly}(n,L)2^{E_Sn},\\
E_S=\frac{18261635770550353}{10^{17}}.
\end{gathered}
\tag{291}
```

This proves Theorem 2, including indexed witness recovery.


## References

1. Ellis Horowitz and Sartaj Sahni. Computing Partitions with Applications to the Knapsack Problem. *Journal of the ACM* 21(2):277–292, 1974. [doi:10.1145/321812.321823](https://doi.org/10.1145/321812.321823).
2. Tim Randolph and Karol Węgrzycki. Beating Meet-in-the-Middle for Subset Balancing Problems. *Proceedings of the 58th Annual ACM Symposium on Theory of Computing*, pp. 1314–1325. ACM, 2026. [doi:10.1145/3798129.3800841](https://doi.org/10.1145/3798129.3800841).
3. Josh Alman and Baitian Li. Kronecker Powers, Orthogonal Vectors, and the Asymptotic Spectrum. *arXiv:2509.14489v1*, 17 September 2025. [doi:10.48550/arXiv.2509.14489](https://arxiv.org/abs/2509.14489v1).
4. Lixi Ye and Baitian Li. Subset Sum via Partial Match. *arXiv:2610.10446v1*, 7 October 2026. [doi:10.48550/arXiv.2610.10446](https://arxiv.org/abs/2610.10446v1).
5. Swapnil Jain. Deterministic Subset Sum below meet-in-the-middle. Public GitHub preprint, commit `1daaf519f567dd7a65a00692b08b4ff54b252d24`, 11 October 2026. Theorem 5b-F in `proofs/stage5b.md`. [Versioned source](https://github.com/Swapnil-jain/subsetsum-derand/tree/1daaf519f567dd7a65a00692b08b4ff54b252d24).
6. OpenAI. Subset Sum in Time $`O(2^{0.49n})`$. *OpenAI Math Release preprint*, 4 October 2026. Repository commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`. [Versioned source](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026).

7. OpenAI. A Low-Space Algorithm for Worst-Case Subset Sum. *OpenAI Math Release preprint*, 26 September 2026; accessed 23 October 2026. [Source](https://github.com/openai/math/tree/main/preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026).
8. Richard Schroeppel and Adi Shamir. A $`T=O(2^{n/2})`$, $`S=O(2^{n/4})`$ Algorithm for Certain NP-Complete Problems. *SIAM Journal on Computing* 10(3):456–464, 1981. [doi:10.1137/0210033](https://doi.org/10.1137/0210033).
9. Ce Jin, Jaewoo Park, Barna Saha, and Yinzhan Xu. Deterministic Monotone Min-Plus Product and Convolution. *ICALP 2026*, LIPIcs 374, 119:1–119:23, 2026. [doi:10.4230/LIPIcs.ICALP.2026.119](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.119).
10. Mokshay Madiman, Adam W. Marcus, and Prasad Tetali. Entropy and Set Cardinality Inequalities for Partition-Determined Functions. *Random Structures & Algorithms* 40(4):399–424, 2012. [doi:10.1002/rsa.20385](https://doi.org/10.1002/rsa.20385).
