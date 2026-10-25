# A common retained-quarter lemma

Author: Yilin Liu. Assistance: OpenAI Codex, including GPT-6 Astra.

Let a strict core have size c and deficiency d, extracted from a full
block of density at most x. Greedy deletion gives d/c <= x.
Let r=theta*c+O(Q_grid) be its aligned selected-shell size and let the
chosen support class have threshold 2^ell. Suppose its physical support
deficit satisfies

$$
\theta c-\ell\le\phi d+O(Q_{\rm grid}\log(m+1)),
\qquad \phi x<\theta/8
$$

with a fixed positive gap. After a fixed coordinate cutoff,
ell/r > 7/8 with a fixed gap. Cardinality pigeonholing, complementation,
and bounded trimming retain a smaller layer of size k <= r/2 with

$$
h(k/r)\ge\ell/r-o(1)>7/8>h(1/4).
$$

Here h(1/4)<5/6 follows from 3^9>2^14.
Thus a useful layer has k/r > 1/4 with a fixed margin, and all layers
with k < r/4 can be omitted before expensive processing.
The polynomially many layer/layout choices still preserve every
solution's successful representation. The restriction only reduces
the generated universes and costs.

## Biased top

The active top has theta=s=21/50, x_0 <= 27/200 and phi_0 <= 143/400.
The exact comparison is

$$
\phi_0x_0\le\frac{3861}{80000}
<\frac{s}{8},\qquad
\frac{s}{8}-\frac{3861}{80000}=\frac{339}{80000}.
$$

Retain only r/4 <= k <= r/2.
For all retained configurations, after alignment,

$$
k/b\ge.105-o(1)>.1,\qquad
(r-k)/b\ge.21-o(1)>.2.
$$

Both arguments remain below one half. The exact integer inequalities

$$
10^{20}>2^9\,9^{18},\qquad 5^{10}>2^{23}
$$

give h(1/10)>9/20 and h(1/5)>7/10. Therefore every retained top layer,
including an unsuccessful one, satisfies

$$
\overline H
=\tfrac12[h(k/b)+h((r-k)/b)]>\frac{23}{40}.
$$

Exact top-product balance supplies at least m/2 movable logarithmic
mass per parent after the fixed cutoff. Its positive linear reserve
absorbs the fixed-cell binomial losses.

## Strict local cores

The active strict local mode has theta=9/20, x<27/200 and
phi <= 31/80. The corresponding exact comparison is

$$
\phi x\le\frac{837}{16000}<\frac{\theta}{8},
\qquad
\frac{\theta}{8}-\frac{837}{16000}=\frac{63}{16000}.
$$

Again retain only r/4 <= k <= r/2. For all retained layers,

$$
k/c\ge9/80-o(1)>1/9,\qquad
(r-k)/c\le27/80+o(1)<7/20.
$$

The exact comparisons

$$
9^6>2^{19},\qquad
20^{80}<2^{75}7^{28}13^{52}
$$

give h(1/9)>1/2 and h(7/20)<15/16. Consequently

$$
h((r-k)/c)-h(k/c)<7/16<.49.
$$

When the scalar policy also certifies c>53m/100, the atomic
complement entropy satisfies R_T <= m-c < .47m.
Together with movable entropy at least m/2, both possible sides of
the allocation imbalance have reserve at least .03m.
This is a stronger uniform packing reserve than the generic
one-half contrast test.

The inequalities are asserted after one fixed coordinate cutoff;
Q_grid is fixed independently of the input. All input-bit-length
factors remain polynomial and are kept outside this cutoff.

## One owner root and three quadratic comparisons

The owner scalar proof can use one outward fixed-power root enclosure
and three rational quadratic comparisons over its whole interval.
This replaces repeated endpoint root calculations and derivative
casework. The independent replay establishes the same complete owner
resource inequalities with design anchor q_circ=137/250.
The actual smaller dictionary capacity is derived separately in RESOURCES.md.

This is a simplification of the certificate proof. It does not change
the selected geometry, support threshold, owner cover, or cost model.

## Active-range assignment containers

Only p=1/20 and |t|<=.06 are needed. With z=t/(1-2p), reflection gives
0<=z<=1/15. Write g=h(p)-3p and use the certified h(.05)<.2864,
so g<7/50. If C=2zag and k_+=pa(1/2+z), then

$$
\frac{C}{k_+}\le\frac{56}{85}.
$$

For E(l,k)=l[1-h(k/l)], the increasing degree-crossing equation is
2w-E(2k_++w,k_+)=C. Its curvature bound gives
E(2k+w,k)<=w^2/(4k ln2). At w=3C/4 this is at most
63C/(680 ln2)<C/2. Hence the unique crossing satisfies
w<=3C/4 and

$$
2k_++w\le\frac{53}{425}n_+<n_+.
$$

With D(t)=1-h(1/2+t), the same curvature estimate and
D(t)>=2t^2/ln2 give

$$
\frac{E}{2aD(t)}
\le\frac{9g^2}{32p(1-2p)^2}
\le\frac{49}{360}<\frac38.
$$

At t=0 take E=0. This proves the needed active container fit and
incidence budget directly. The unused larger parameter range and its
additional entropy certificates are omitted. Complete construction,
support indexing, tensorization, and exact-bit costs remain in
OWNERSHIP.md.

## A decreasing tiny-cap envelope

On the middle upper cap, the local fraction is one, so the local
deficiency term is exact. The top implicit root obeys t<=rho.
Along rho=.605+3x with x<.01, implicit differentiation gives

$$
\beta'\le.635+\frac{.01(1+3P)}{\alpha(P-.01)}<.7.
$$

The cap restart derivative is therefore negative. Its maximum is
at the single left endpoint x=X. One outward root enclosure there
replaces an additional root enclosure and a convexity reduction.
Together with the owner simplification, only two implicit root
certificates remain in the complete scalar proof.

## Tight capacity with a fixed design

Core-size policies keep their original design anchor .548. The actual
dictionary exponent is the certified maximum restart envelope plus
10^-9. The fixed granularity and coordinate cutoff cost at most
2*10^-10. The high-deficiency threshold is adjusted simultaneously
so that q_actual+B=3/4 exactly.

A uniform weaker top coefficient is a valid shorter proof of the
received 137/750 bound, but increases the binding restart estimate.
The final tight certificate retains the two top coefficients and
their five rational regions. This avoids sacrificing the result
merely to remove a case.
