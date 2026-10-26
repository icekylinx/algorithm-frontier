# A polynomial-work energy cut player

This note gives a deterministic replacement for the exhaustive local search
in Appendix B.1 of [Chang--Huang--Su, arXiv:2405.03908v1](https://arxiv.org/abs/2405.03908).
The replacement proves the energy separation needed by the shuffler with
an $`O(\log t)`$ loss, where $`t`$ is the number of clusters. Its arithmetic
work is polynomial in $`t`$ and in the input bit size. The extra logarithm
in the number of shuffler rounds is harmless for the source's
$`\log^{O(1/\epsilon)}n`$ routing envelope.

The proof is independent of the projection-dependent expectation
calculation in the printed proof of Lemma B.2. It does not assert the
printed constant $`1/720`$. It also does not supply the matching-embedding
or hierarchical-decomposition algorithms used elsewhere in that source.

## 1. The vector separation problem

Let $`t\geq16`$, and let $`R_1,\ldots,R_t`$ be rational vectors in
$`\mathbb Q^t`$. Put
```math
\overline R=\frac1t\sum_iR_i,\qquad
 v_i=R_i-\overline R,\qquad
 \Phi=\sum_i\|v_i\|_2^2.
```
Assume $`\Phi>0`$. Define the integer
```math
h=\left\lceil\log_4(8t^3)\right\rceil.
 \tag{1}
```
There is a deterministic polynomial-work algorithm returning disjoint
sets $`S,S'\subseteq[t]`$ such that
```math
|S|\leq t/8,\qquad |S'|\geq t/2,
 \tag{2}
```
and, for every map $`\sigma:S\longrightarrow S'`$, including
noninjective maps,
```math
\sum_{i\in S}\|R_i-R_{\sigma(i)}\|_2^2
       \geq \frac{\Phi}{512h}.
 \tag{3}
```
The same sets work for every map; the map is not fixed before the sets
are chosen.

### 1.1 A sign projection with simultaneous control of every pair

For a sign vector $`r\in\{-1,1\}^t`$, write
```math
E(r)=\sum_i\langle v_i,r\rangle^2.
```
For each unordered pair $`i<j`$ with $`d_{ij}=v_i-v_j\ne0`$, put
```math
H_{ij}(r)=
   \left(\frac{\langle d_{ij},r\rangle^2}
                    {8h\|d_{ij}\|_2^2}\right)^h.
```
Use the potential
```math
\Psi(r)=E(r)-t\Phi\sum_{i<j:\,d_{ij}\ne0}H_{ij}(r).
 \tag{4}
```
If the signs are independent and uniform, then
$`\mathbb E E=\Phi`$. Expanding the even moment, or comparing its
nonnegative even-monomial expansion with the Gaussian moment, gives
```math
\mathbb E\langle d,r\rangle^{2h}
 \leq (2h-1)!!\,\|d\|_2^{2h}
 \leq (2h)^h\|d\|_2^{2h}.
 \tag{5}
```
Consequently $`\mathbb E H_{ij}\leq4^{-h}`$. There are fewer than
$`t^2`$ pairs, so (1) implies
```math
\mathbb E\Psi\geq
 \Phi-t^3\Phi\,4^{-h}\geq\frac78\Phi.
 \tag{6}
```

Fix the coordinates of $`r`$ in order. At each step compute the exact
conditional expectation of (4) for each of the two choices, and retain
the larger one, breaking ties by a fixed rule. Section 4 proves that
these computations take polynomial work and polynomially many bits.
The resulting vector satisfies $`\Psi(r)\geq7\Phi/8`$. Therefore
```math
E(r)\geq7\Phi/8.
 \tag{7}
```
Moreover Cauchy--Schwarz gives $`E(r)\leq t\Phi`$. If any pair had
$`H_{ij}(r)\geq1`$, (4) would give $`\Psi(r)\leq0`$, contradicting
(6). Thus, simultaneously for every pair,
```math
|\langle R_i-R_j,r\rangle|^2
       \leq 8h\,\|R_i-R_j\|_2^2.
 \tag{8}
```
The inequality is also true when $`R_i=R_j`$.

### 1.2 A median and two extreme tails

Set $`\mu_i=\langle R_i,r\rangle`$, and sort these values with index
tie-breaking. Let $`m`$ be the value in position $`\lceil t/2\rceil`$,
and put $`a=\lfloor t/8\rfloor`$. Take the bottom $`a`$ and top $`a`$
positions. Their union contains the $`a`$ largest values of
$`|\mu_i-m|`$. Hence the sum of squared distances to $`m`$ on that
union is at least
```math
\frac at\sum_i(\mu_i-m)^2.
 \tag{9}
```
Choose as $`S`$ whichever of the two tails has the larger sum in (9).
Because $`t\geq16`$, $`a\geq t/16`$, and therefore
```math
\sum_{i\in S}(\mu_i-m)^2
       \geq\frac1{32}\sum_i(\mu_i-m)^2
       \geq\frac1{32}\sum_i(\mu_i-\overline\mu)^2
       =\frac{E(r)}{32}.
 \tag{10}
```
If $`S`$ is the top tail, let $`S'`$ be the bottom
$`\lceil t/2\rceil`$ positions. If $`S`$ is the bottom tail, take the
top $`\lceil t/2\rceil`$ positions. These sets are disjoint, including
when values tie, and satisfy (2). Their scalar values lie on opposite
sides of $`m`$. Thus for every map $`\sigma:S\to S'`$,
```math
|\mu_i-\mu_{\sigma(i)}|\geq|\mu_i-m|.
 \tag{11}
```
Combining (7), (8), (10), and (11) proves
```math
\sum_{i\in S}\|R_i-R_{\sigma(i)}\|_2^2
 \geq \frac{7\Phi}{2048h}
 \geq \frac{\Phi}{512h}.
 \tag{12}
```
No search over the $`3^t`$ possible pairs of disjoint sets occurs.

## 2. Physical cluster sizes and a saturated fractional matching

For the CHS application, $`R`$ is the current doubly stochastic
walk matrix, and its row mean is $`\mathbf1/t`$. Let cluster $`i`$
have $`c_i`$ physical vertices. Property 3.1 supplies
```math
\frac23(\tau-1)\leq c_i\leq2(\tau+1)
 \tag{13}
```
for a common $`\tau`$, as well as
```math
\frac{|X|}{3k}\leq c_i\leq\frac{6|X|}{k}.
 \tag{14}
```
Assume $`\tau>7`$. For the sets just constructed,
```math
|S_X|\leq\frac{(\tau+1)t}{4}
       <\frac{(\tau-1)t}{3}
       \leq |S'_X|.
 \tag{15}
```
Thus the source's matching-embedding primitive can be called with
sources $`S_X`$ and sinks $`S'_X`$. In a host whose sparsity is
strictly greater than the primitive's cut threshold, its cut alternative
is impossible, and its matching saturates all of $`S_X`$.

Let $`c_{ij}`$ count the matched pairs between clusters $`i`$ and $`j`$,
and retain the source's literal normalization
```math
n'=\frac{6|X|}{k},\qquad m_{ij}=\frac{c_{ij}}{n'}.
 \tag{16}
```
This is not a change to normalization by the largest cluster.
Equation (14) implies that $`M=(m_{ij})`$ is a symmetric fractional
matching: every fractional degree is at most one. For every
$`i\in S`$, saturation and (14) imply
```math
\sum_{j\in S'}m_{ij}=\frac{c_i}{n'}\geq\frac1{18}.
 \tag{17}
```

To apply (3) to these fractional weights, for each $`i\in S`$ choose
a $`j_i\in S'`$ minimizing $`\|R_i-R_j\|^2`$. Then
```math
\sum_{i\in S,j\in S'}m_{ij}\|R_i-R_j\|^2
 \geq\frac1{18}\sum_{i\in S}\|R_i-R_{j_i}\|^2
 \geq\frac{\Phi}{9216h}.
 \tag{18}
```
This argument uses no rounding of $`n'/18`$ and no asserted integer
number of cluster matchings.

## 3. Exact potential decrease and the revised shuffler length

Complete $`M`$ to a symmetric stochastic matrix $`M^*`$ with diagonal
entries $`1-\sum_{j\ne i}m_{ij}`$, and let
```math
Q=\frac12(I+M^*),\qquad R_{\rm new}=QR.
 \tag{19}
```
This is the CHS lazy fractional-matching update. Both matrices are
doubly stochastic, so the row mean remains $`\mathbf1/t`$. Applied
to the centered row vectors, Jensen's inequality gives
```math
\Phi-\Phi_{\rm new}
 \geq\frac14\sum_{i,j}m^*_{ij}\|v_i-v_j\|^2
 =\frac12\sum_{i\in S,j\in S'}m_{ij}\|R_i-R_j\|^2.
 \tag{20}
```
For completeness, write $`w_i=\sum_jm^*_{ij}v_j`$.
The identity
```math
\|v_i\|^2-\left\|\frac{v_i+w_i}{2}\right\|^2
 =\frac14(\|v_i\|^2-\|w_i\|^2)
          +\frac12\langle v_i,v_i-w_i\rangle
```
and Jensen's inequality show that the sum of the first terms is
nonnegative. Symmetry of $`M^*`$ converts the sum of the second
terms into the Dirichlet form in (20).
Equivalently $`I-Q^2=(I-M^*)(3I+M^*)/4\succeq(I-M^*)/2`$,
since the eigenvalues of the symmetric stochastic $`M^*`$ lie in
$`[-1,1]`$. The quadratic-form identity
$`\langle v,(I-M^*)v\rangle =\tfrac12\sum_{ij}m^*_{ij}\|v_i-v_j\|^2`$
then gives (20).

Combining (18) and (20),
```math
\Phi_{\rm new}\leq
 \left(1-\frac1{18432h}\right)\Phi.
 \tag{21}
```
Starting from $`R=I`$, the initial potential is $`t-1`$. For
$`t\leq n`$, a sufficiently large absolute constant in
```math
\lambda=O\!\left(h\log(n+2)\right)
          =O\!\left(\log(t+2)\log(n+2)\right)
 \tag{22}
```
ensures $`\Phi\leq1/(9n^3)`$, the unchanged stopping condition.
The stopping test can also be made by exact rational arithmetic.

### 3.1 The source's later integer-token error bounds

The following is a compatibility calculation for the source's original
integer-token architecture. The PRIMARY sequential provider instead
uses the actual-size leaf threshold and integer guards in
[sequential-expander-routing-tradeoff.md](sequential-expander-routing-tradeoff.md),
Section 3, together with the direct query induction in
[conditional-full-router-from-shufflers.md](conditional-full-router-from-shufflers.md).
That provider does not require the additional clipping or condition
(23) below. This distinction prevents a historical sufficient condition
from being mistaken for a restriction on its growing parameter p.

The only change here is that the shuffler has $`\lambda`$ as in
(22), rather than $`O(\log n)`$. The source's Section 6.1 accumulates
at most $`\lambda t`$ error for each token class, and Section 6.5
uses $`q^2/k`$ in its load bound after $`q\leq\lambda`$ shuffler
steps. Its leaf trimming ensures $`|X|\geq k^4`$ for an internal
node and $`t\leq k`$. Thus the same inequalities hold after
requiring
```math
k\geq c_1\lambda
 \tag{23}
```
for a sufficiently large absolute constant: in particular
$`|X|/(10t^2)\geq k^2/10\geq t\lambda`$, and
the maximum load is $`O(L\lambda)`$ for $`L\geq1`$.

The actual-size clipping used in
[degree-split-token-routing-interface.md](degree-split-token-routing-interface.md)
has
```math
p_{\rm loc}\leq c\sqrt{\log(n+2)/\log\log(n+4)},\qquad
 k=n^{1/p_{\rm loc}}.
```
It makes $`k`$ exceed every fixed power of $`\log n`$ eventually.
Therefore (23) holds without altering the proposed output envelope.
An executable implementation checks the elementary size inequalities;
the finitely many remaining actual host sizes are handled directly.
The larger $`\lambda`$ contributes fixed logarithmic factors to
recursive costs and hence remains within
$`\log^{O(p_{\rm loc})}n`$. It does not insert a polynomial factor
in $`k`$ into output path length or congestion.

The assumptions $`t\geq16`$ and $`\tau>7`$ can likewise be enforced
by a fixed increase of the leaf/small-host thresholds. A node with
$`\tau\leq7`$ has $`|X|=O(k)`$, so it is a permissible
polynomial-$`k`$ leaf. Once the global host has $`k\geq24`$,
Property 3.1's $`t\geq2k/3`$ gives $`t\geq16`$.

## 4. An exact finite-word implementation

Assume first that all $`v_i`$ have a common positive denominator $`D`$,
and that the integer coordinates $`D v_i`$ have at most $`b`$ bits.
One may multiply the entire potential by $`D^2`$, so only these
integer coordinates and rational pair-normalization factors are
needed. Different explicitly represented denominators can instead
be cleared by their product; its bit size is polynomial in the
stated input encoding.

After some signs have been fixed, a pair projection has the form
```math
a+\sum_{\ell\in I}d_\ell r_\ell .
 \tag{24}
```
Its moments through order $`2h`$ are computed by a short dynamic
program. Start with $`M_j=a^j`$. When incorporating one remaining
coefficient $`d`$, replace the list by
```math
M'_j=\sum_{\substack{0\leq z\leq j\\z\ {\rm even}}}
                 {j\choose z}d^z M_{j-z}.
 \tag{25}
```
The absence of odd terms is exactly the average over the two signs.
All entries are integers. At the end $`M_{2h}`$ is the conditional
moment appearing in (4). The conditional expectation of $`E(r)`$
is even simpler: for each row it is the square of the fixed partial
sum plus the sum of the remaining coefficient squares.

A pair moment has $`O(h(b+\log(t+2)))`$ bits. Its denominator in
(4) is
```math
(8h)^h\left(\sum_\ell d_\ell^2\right)^h,
 \tag{26}
```
with $`O(h(b+\log(t+2)+\log(h+2)))`$ bits. Summing the fewer than
$`t^2`$ rational pair terms using the product of their denominators
therefore requires only polynomially many bits. Computing both
candidate expectations from scratch at each of the $`t`$ sign
choices uses, for example,
```math
O(t^4h^2)
 \tag{27}
```
integer arithmetic operations on polynomial-bit integers. This
deliberately loose bound suffices: no operation hides an
exponential search in $`t`$.

In the CHS application $`k`$ is rounded to an integer. The
entries of each update (19) have a common denominator dividing
$`12|X|`$. After $`i`$ shuffler steps, a common denominator for
the centered rows divides
```math
t(12|X|)^i.
 \tag{28}
```
Because $`i=O(\log t\log n)`$, these input coordinate bit lengths
are $`O((\log(n+2))^3)`$. The larger integers used privately in
the exact conditional-expectation comparison occupy polynomially
many $`k`$-words and are charged to preprocessing work. They are
not assumed to fit in one CONGEST message or one machine word.
Only the resulting cluster sets, matching counts, and existing
routing labels need the source's short-message representation.

For $`t\leq k`$, the full cut-player preprocessing at a node is
therefore polynomial in $`k`$ and $`\log n`$, with fixed degree.
Summing over at most $`n`$ hierarchy nodes gives the safe work
bound
```math
n\,\mathrm{poly}(k,\log n).
 \tag{29}
```
This is compatible with the intended
$`n\exp O((\log n)/p+p\log\log(n+2)+\log\psi^{-1})`$
sequential preprocessing envelope. The hierarchy and
matching-embedding work remain separately accounted obligations.

## 5. Precise interface supplied

The routine supplies explicit sets satisfying physical source/sink
size feasibility and the all-mappings energy inequality (3). It
supplies an exact finite rational algorithm and proves the revised
potential contraction (21), including fractional matching weights.
Together with the source's matching-embedding primitive it constructs
a valid shuffler in the number of rounds (22).

The note does not deduce sequential complexity merely from CONGEST
rounds. The other necessary pieces are the constructive leaf routing
procedure and explicit hierarchy/matching-primitive work accounting,
as separated in
[sequential-leaf-routing-and-chs-work.md](sequential-leaf-routing-and-chs-work.md).
It establishes no new matching running-time theorem by itself.
