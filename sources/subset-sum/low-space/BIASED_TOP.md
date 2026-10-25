# Biased top representations

Author: Yilin Liu. Assistance: OpenAI Codex, including GPT-6 Astra.

This module proves the positive-deficiency top representation used in
the general low-space bound. Its support counting, fixed-layer
trace inequality, canonical projections, balanced-cell families, and
original-key generators are the complete constructions in
[the manuscript](../../../problems/subset-sum-low-space-deterministic/proof.md), Sections II.1–II.2 and II.5–II.7.
The code construction is strengthened in [LINEAR_COVERS.md](LINEAR_COVERS.md).
All logarithms have base two.

## 1. The support class and its two costs

Choose a strict top base of size $b=\rho m$ before its useful layer.
Its full support has deficiency $d$. Let $s=21/50$. Round the base
to the required fixed multiple so the shell size is exactly $r=sb$. Partition its $r$-subsets by dyadic
support size. If $g$ is the cardinality of a class with threshold
$2^\ell$, maximize $2^\ell g$. The fixed-layer trace theorem and
the gain certificates at $s=.42$ give

$$
\ell+\log g\ge[h(s)+s]b-\phi_0d-O(\log(m+1)),
\qquad
\phi_0=\begin{cases}.345,&x_0\le.05,\\.3575,&x_0>.05.
\end{cases}
$$

Here $x_0$ bounds the full top-block deficiency density, and strict
extraction preserves this density bound. Let the linear translate
cover of this class have $K$ centers. It satisfies
$Kg\le\operatorname{poly}(m)2^b$. Put

$$
\delta=sb-\ell,\qquad \kappa=\log K,\qquad \tau_0=1-h(s).
$$

Since $g\le\binom br\le\operatorname{poly}(m)2^{h(s)b}$,

$$
\delta+\kappa\le\tau_0b+\phi_0d+O(\log(m+1)),
\qquad \delta\le\phi_0d+O(\log(m+1)).
$$

Each center is a separate outer signing. For any original witness,
one center makes its selected top set belong to the class. Negating
that center's coordinates translates the target once. Coordinates
later returned to the background retain their signed weights.

## 2. Projecting an actual integer layer

Fix an outer center. Partition the distinct sums of its selected
set by witness cardinality, complement the larger layer if needed,
trim a bounded number of coordinates, and recanonicalize in the
complete retained cardinality layer. The balanced-cell construction
and the canonical projection entropy argument give, for a suitable
union occupying fraction $a/b$ of the base, at least

$$
2^{(a/b)\ell}/\operatorname{poly}(m)
$$

distinct permitted integer sums. Enumerate the layers, layouts, and
projected cores before constructing common prime families. The code
cost remains $\kappa$; its physical deficit becomes $(a/b)\delta$.

Write $k\in[0,s/2]$ for the smaller-layer fraction on the base and set

$$
\begin{gathered}
H_-=h(k),\quad H_+=h(s-k),\quad
\overline H=(H_-+H_+)/2,\quad H_0=h(s/2),\\
L_0=H_0-\overline H,\quad \Delta=H_+-H_-,\quad
D_0'=\tfrac12+s-H_0,\quad p=D_0'-\delta/b.
\end{gathered}
$$

The active density range makes $p>0$. Choose the ideal projected size

$$
a=\frac{pb}{p+L_0}.
$$

It gives the exact raw-resource identity

$$
-(\tfrac12+s-\overline H)a+(a/b)\delta+\kappa
=-D_0'b+\delta+\kappa.
$$

Thus the top raw contribution is at most
$-D_0b+\phi_0d+O(\log(m+1))$, with $D_0=D_0'-\tau_0$.
The corresponding restart contribution is also bounded by its central
base value. Its difference from that value is

$$
\frac{L_0a}{2p}(\delta/b-s)\le0.
$$

The leaf contribution satisfies
$(\overline H/4-1/8)a\le(H_0/4-1/8)b$ whenever
$\overline H\ge1/2$, as proved below. Projection therefore preserves
the required central resource bounds without scaling the outer code.

## 3. Background coordinates for every useful layer

Let $B=b/m$. Balancing the actual top-mask products requires
$a(1+\Delta)\le m$. A sufficient uniform condition is

$$
1-B\ge\frac{28}{25}pB^2.
$$

For completeness, put $c=s/2$, $t=c-k$, and $v=pB$. The function

$$
F(t)=(\tfrac12+v)h(c+t)+(\tfrac12-v)h(c-t)
$$

has $F(0)=H_0$ and $F'(0)=2v h'(c)$. On
$c\in[1/5,1/4]$, $0\le t<c$, $v\le1/5$,

$$
-F''(t)=
\frac{c(1-c)-t^2-2v(1-2c)t}
{(\ln2)(c^2-t^2)((1-c)^2-t^2)}\ge\frac5{\ln2}.
$$

After subtracting five times the denominator without $\ln2$, the
numerator is at least
$3/256+(29/16)t^2-(6/5)vt\ge3/256-(144/725)v^2>0$.
Completing the square and using $h'(c)\le2$, $\ln2<7/10$, gives
$F(t)\le H_0+(28/25)v^2$. Therefore
$L_0\ge p[B\Delta-(1-B)]$, proving the sufficient condition.
Endpoint layers follow by continuity. The active choice $B\le.85$
satisfies it with a fixed margin, since $p\le D_0'<.179$ and
$(28/25)(.179)(.85)^2<.15$.

Retain only smaller layers with $r/4\le k b\le r/2$.
This retains a useful layer: the physical class bound gives
$\delta/b\le(143/400)T=3861/80000<s/8$, so its support entropy per
selected coordinate exceeds $7/8-o(1)$. A layer with relative
cardinality at most $1/4$ has entropy at most $h(1/4)<5/6$,
certified by $3^9>2^{14}$. The fixed gap absorbs layer, trimming,
and layout losses. Thus every original solution has a retained layer.

Every retained layer, useful or otherwise, satisfies $k\ge s/4>.1$
and $s-k\ge s/2>.2$. The exact integer comparisons
$10^{20}>2^9 9^{18}$ and $5^{10}>2^{23}$ give
$h(.1)>9/20$ and $h(.2)>7/10$. Hence

$$
\overline H>\frac{23}{40}>\frac12.
$$

Exact top-product balancing supplies at least
$m/2+(\overline H-1/2)a+O(\log m)$ movable logarithmic mass per
parent. The atomic-complement allocation therefore applies throughout
the enumerated layer range, rather than relying on eligibility for
each processed configuration.

## 4. Separators for every layer

For a cell of size $g$, let left and right counts be $kg$ and
$(s-k)g$. A separator must contain the left mask and avoid the right.
Set

$$
\alpha=1+\frac{\ln(2-s)}{\ln(1/(1-s))},\qquad
e(k)=\tfrac12+\alpha(k-s/2).
$$

The separator has $e(k)g+O(1)$ coordinates. Concavity of $\ln$ gives
$s\ln(2-s)<-(1-s)\ln(1-s)$, hence $1<\alpha<1/s$.
Consequently $k<e(k)<1-s+k$ throughout the layer interval.
Rational logarithm enclosures and integer rounding determine a
feasible size with only $O(\log g)$ exponent error.

The left degree exponent is

$$
E_s(k)=(1-k)h\!\left(\frac{e-k}{1-k}\right)
 -(1-s)h\!\left(\frac{e-k}{1-s}\right).
$$

The right exponent is $E_s(s-k)$. Put
$X=1-k$, $Y=e-k$, $Z=1-e$, $W=1-s-Y$ and
$G=(\ln2)E_s$. Direct differentiation gives

$$
G''=1/X-\alpha^2/Z+(\alpha-1)^2/W.
$$

Since $Z/X\le1$ and
$Z/W\le(1+\alpha s)/(1-2s+\alpha s)$,

$$
ZG''\le
-\frac{2(1-s)(\alpha-1)}{1-2s+\alpha s}<0.
$$

The chosen $\alpha$ makes $G'(s/2)=0$. Both sided degrees are thus
at most $O^*(2^{d_sa})$ after taking products over cells, where

$$
d_s=E_s(s/2)=s-h(s/2)+h(s)/2.
$$

The family-size exponent is
$T_s(k)=h(e)-(1-s)h((e-k)/(1-s))$.
It is symmetric about $s/2$. Its second derivative has the sign of

$$
(1-s)[(\alpha-1)^2-\alpha^2(1-s)]/4
 +s\alpha^2(\alpha-1)^2(k-s/2)^2.
$$

At $(k-s/2)^2=s^2/4$, four times this upper bound equals
$(1-\alpha s)P(\alpha)$, where

$$
P(A)=(1-s)-(1-s)(2-s)A-s(1-2s)A^2-s^2A^3.
$$

For $0<s\le1/2$, $P(\alpha)\le P(1)=s-1<0$.
Hence $T_s$ is concave and $T_s(k)\le T_s(s/2)=s$.
The global tuple table has $O^*(2^{sa})$ entries.

The deterministic bounded-load construction is the finite potential
argument in the manuscript, Section II.6.4, with general counts
$c,d$ satisfying $c+d=sg$:

$$
B_g=\binom ge,\quad R_g=\binom{g-c-d}{e-c},\quad
H_L=\binom{g-c}{e-c},\quad H_R=\binom{g-d}e.
$$

Take $\nu=\lceil10(g+1)B_g/R_g\rceil$ separators and degree caps
$K_j=\lceil2\nu H_j/B_g+4g+8\rceil$. The expected potential
consisting of uncovered pairs plus $\sum2^{\deg-K_j}$ is below one.
Its exact conditional expectation determines each separator by
enumerating candidates. The same integer-denominator proof costs
$O^*(2^{6g})$ bit time and $O^*(2^{2g})$ state, including incidence
indices. A fixed number of balanced cells pays construction and the
separate global tuple table. For equal-weight groups, one witness per
tuple preserves every disjoint match, and touched-entry clearing
charges each record only its degree.

## 5. Incidences and the outer signing cost

For a full local block with deficiency $d_j$, the parent ambient
exponent, including the outer top code, is

$$
\frac{3m}{2}-d_j-(\tfrac12+s-\overline H)a
 +(a/b)\delta+\kappa.
$$

Adding the separator degree $d_sa$, its difference from the central
bound $3m/2-d_j+\delta+\kappa-\tau_0b/2$ is exactly

$$
-\frac{L_0a d_s}{p}\le0.
$$

Since $d_j\ge x_0m$ and $d\le m\beta(x_0,\rho)$, the central
incidence excess is at most

$$
I=\tfrac12\tau_0\rho+\phi_0\beta(x_0,\rho)-x_0.
$$

[RESOURCES.md](RESOURCES.md) proves $I<-1/1250$ on the active
positive-deficiency interval. This margin pays fixed-grid projection
errors. The code rate is paid once in each outer solve, in its
preparation, and in every top-dependent residue cover; two outer
top signings are never combined by one compatibility checker.

For the local strict-core notation of the resource certificate, the
complete central upper bounds are

$$
\begin{aligned}
R&=-D_0\rho+e\sigma+\phi_0\beta(x_0,\rho)
                  +\phi\beta(x,\sigma),\\
Q&=\tfrac34-A_0\rho-r\sigma-x+\phi_0\beta(x_0,\rho)
                  +\phi\beta(x,\sigma),\\
F&=\max\{1-\sigma,\tfrac38+(H_0/4-1/8)\rho
                                  +(H-1/2)\sigma/2\},\\
A_0&=\tfrac34+s-\tfrac32H_0-\tau_0.
\end{aligned}
$$

The oriented-half local mode keeps its exact nonpositive compression
corrections. All definitions and inequalities here concern actual
integer images before modular reduction. Common primes are selected
only after those images are fixed. Universal local covers handle every
later background translation, and original-key signing unions retain
the full-block ambient bound without a local Cartesian code factor.
