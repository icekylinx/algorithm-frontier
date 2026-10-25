# Increment X-SS: Vandermonde trace bounds and retyped circuits for deterministic Subset Sum

**English rough draft for external review.**

Baseline repository: `icekylinx/algorithm-frontier`, commit
`37b31138bf102a83d9efb2cbe44437eec45ae3c2`,
`sources/subset-sum/combined-proof.md`, Part I. The imported Subset Sum
source commit is `1ecb2e2eb43963a6ca9a4a5f4c6a208990c3b22b`.

Attribution: Yilin Liu and GPT-6 Astra Pro.

## 1. The incremental theorem

The repository's deterministic general-input exponent is

\[
 E_{\rm old}=\frac{149809813343531}{301754962128739}
 =.496461805587\ldots.
\]

The change below gives

\[
 \boxed{E_{\rm new}=
 \frac{158153814247997}{318927986919134}
 =.4958919277538907\ldots < .495892.}
 \tag{XSS1}
\]

The exponent decreases by approximately `.0005698778` per input coordinate.
This result applies to arbitrary signed binary integers, with no promise
on density, multiplicities, target, or the existence of a solution.

**Theorem, with the repository's exact circuit and reduction lemmas as
dependencies.** There is a uniform deterministic algorithm deciding Subset
Sum on `n` indexed signed binary integers of total encoding length `L`, and
returning an indexed witness on YES instances, using

\[
 C_{\rm new}+\operatorname{poly}(n,L)2^{E_{\rm new}n}
 \tag{XSS2}
\]

bit operations. The startup cost `C_new` is finite and independent of the
input. All polynomial degrees are fixed. This is a time theorem; it makes
no simultaneous claim for the separate low-space algorithm.

The new argument changes three concrete ingredients: the pooled-trace
upper bound, the rational matching types used inside the reduction, and
the finite menu of recursive lookup widths. It then recomputes the entire
profile and every outer cost line. The exact signed identities, fixed-seed
compiler, canonical selection, energy evaluation, residue covers, exact
integer keys, and witness lifting remain dependencies of the repository
proof. This increment does not claim an independent reproof or external
review of that full earlier manuscript.

## 2. New types and the exact circuit families

Set

\[
 s=\frac7{50}=.14,\quad t=\frac9{20}=.45,\quad
 a=\frac{13}{200}=.065,\quad b=\frac3{40}=.075,
 \qquad a+b=s.
 \tag{XSS3}
\]

Write `H(c,x)=c log_2 c-x log_2 x-(c-x)log_2(c-x)`, with its continuous
endpoint values. The outer color domain is

\[
 a\le m\le s,\qquad \beta=a+\rho(m-a),\qquad m\le z\le\beta,
\]

\[
 L_0=\max\{0,H(t,z)+H(1-t,\beta-z)-H(1-m,\beta-m)\}.
 \tag{XSS4}
\]

Use the following fixed recursive parameter pairs:

\[
 (\rho,\gamma_1)\in
 \{(1.3,.47),(1.7,.47),(2.2,.50),(2.6,.54),
   (2.8,.58),(3,.60),(3.4,.62),(4,.65)\}.
 \tag{XSS5}
\]

All decimals in the mathematical specification are exact rationals.
For every family, `beta<=.365<t<1-t`. Its first inner lookup is
`c=gamma_1 beta`. The required containment condition `beta-z<=c`
holds on the full color domain: at the worst point `z=m=s`, the pairs
`(beta-s,c)` are respectively

\[
 (.0225,.076375),\ (.0525,.090475),\ (.09,.115),\ (.12,.1404),
\]

\[
 (.135,.1595),\ (.15,.174),\ (.18,.1984),\ (.225,.23725).
\]

The first inner color and occurrence exponent are

\[
 Q_1=\beta-z,\quad D_1=c-Q_1,\qquad
 \max\{Q_1,c-m\}\le w_1\le\min\{\beta-m,c\},
\]

\[
 F_{1,\rm raw}=H(\beta-m,w_1)+H(m,c-w_1)-H(z,D_1).
 \tag{XSS6}
\]

Keep the exact second-level routing

\[
 Q_2=c-w_1,\qquad C_2=\max\{c/2,Q_2\},\qquad D_2=C_2-Q_2.
 \tag{XSS7}
\]

On the push branch `w_1<=c/2`, use the old valid profile upper bound

\[
 P_{\rm push}=\tau L_0+(1-\tau)H(b,m-a)
 +(1-\tau)\max\{0,F_{1,\rm raw}\}
 +\tau H(D_1,w_1-Q_1).
 \tag{XSS8}
\]

On the recursive branch, write `v=w_1-c/2>=0`, so `C_2=c/2` and
`D_2=v`. The complete domain is

\[
 \max\{0,\beta-z-c/2,c/2-m\}\le v
 \le\min\{c/2,\beta-m-c/2\},
\]

\[
 \max\{Q_2,C_2-Q_1\}\le w_2\le\min\{D_1,C_2\}.
 \tag{XSS9}
\]

Put

\[
 F_2=\max\{0,H(D_1,w_2)+H(Q_1,C_2-w_2)-H(w_1,D_2)\},
\]

\[
 G_2=H(D_2,w_2-Q_2).
 \tag{XSS10}
\]

The new profile replaces the old first-level right contribution by the
trace bound proved next. The finite signed matrix is still the same exact
aggregated circuit from baseline (47); no positive cover substitutes for
a signed identity.

Also retain the ordinary direct signed lookup family `rho=4`. Its profile
is bounded by

\[
 P_{\rm dir}=\tau L_0+(1-\tau)
 \{H(b,m-a)+H(\beta-m,z-m)-\delta_{\rm dir}\}.
 \tag{XSS11}
\]

On a rectangle where `m_0>a` and
`rho(m_0-a)^2>=b(z_1-a)`, use
`delta_dir=(7/5)(s-m_1) max(0,z_0-m_1)`; otherwise use zero.
This is the existing direct distinct-gate bound, applied at the new types.

## 3. The new pooled-trace lemma

Fix one outer and first-inner occurrence and write

\[
 d=m-a,\quad r=s-m,\quad q=c-w_1,\quad D=\beta-m-w_1,
 \qquad B=H(b,d).
\]

The first-inner domain gives `0<=q<=m` and `D>=0`. When `beta>=s`, define

\[
 A(g)=H(b,g)+H(s-g,q)+H(\beta-s,w_1-g)-H(z,D_1),
\]

\[
 J(u)=H(b,d+u)+H(m+u,q)+H(1-s,D-u)
       +H(1-m-D,w_1)-H(1-m,w_1+D)-H(z,D_1).
 \tag{XSS12}
\]

Both functions are concave in their scalar argument. Their intervals are

\[
 I_g=[\max\{0,w_1-(\beta-s)\},\min\{r,w_1\}],\qquad
 I_u=[0,\min\{r,D\}].
 \tag{XSS13}
\]

All entropy arguments are feasible. In particular, for this menu
`D<=beta<=.365<1-s=.86`. Put `A_*=max_{I_g}A` and `J_*=max_{I_u}J`.
Then the same exact aggregated circuit has a right-degree upper exponent

\[
 R^{\rm trace}\le G_2+B_{\rm tr},
\]

\[
 \boxed{B_{\rm tr}=
 \min\left\{B+\max\{0,F_{1,\rm raw}\},
             \max\{B,A_*,J_*\}\right\}.}
 \tag{XSS14}
\]

When `beta<s`, define `B_tr=B+max(0,F_{1,raw})`. Thus on every recursive
color the complete profile is bounded by

\[
 P_{\rm rec}=\tau L_0+(1-\tau)B_{\rm tr}
              +\tau F_2+(1-\tau)G_2.
 \tag{XSS15}
\]

### Proof of the trace lemma

Use the exact pooled-histogram expression (51) in the baseline. Its
histogram coordinates are `j,e,f`. Set `k=q-e` and `g=f-k`. The three
branches of the pooled count are `0,C_1,C_0+C_1`.

For the zero branch, every feasible trace `K` has at least one completion
`U=Y_1 union V`, where `V` has `dN` elements of `Y_0`. Select one
completion for each trace. Distinct traces have different `U cap C`, and
therefore different completions. Hence there are at most `binom(bN,dN)`
traces, giving exponent `B`. Equivalently, the feasibility constraints
give `0<=k<=d` and `0<=d-k<=j-f`; a fixed outside completion injects the
`binom(fN,kN)` trace choices into the `binom(bN,dN)` original choices.
This argument does not require `q<=d`.

For the `C_1` branch, increasing `j` to `b` only enlarges the finite set
of pairs `(C,K)`: move prescribed zeros from outside the outer occurrence
to previously neutral positions inside it. Every old trace and its
completion remains valid. The exponent at `j=b` is

\[
 H(a,q-k)+H(b,k)+H(b-k,g)+H(\beta-s,w_1-g)-H(z,D_1).
\]

The entropy chain identity and Vandermonde give

\[
 H(b,k)+H(b-k,g)=H(b,g)+H(b-g,k),
\]

\[
 H(a,q-k)+H(b-g,k)\le H(s-g,q).
\]

Completion implies `0<=g<=r`, and the remaining entropy domains give
`I_g`. Thus this branch is at most `A_*`. The change from the earlier
argument is to sum over `k` before maximizing over `g`.

For the `C_0+C_1` branch set

\[
 u=j-f-(d-k),\qquad j=d+u+g.
\]

Feasibility gives `0<=u<=min(r,D)`. The numerator exponent rewrites as

\[
 H(b,d+u)+H(d+u,k)+H(a,q-k)
 +H(r-u,g)+H(1-s,D-u)+H(1-s-D+u,w_1-g).
\]

The two negative terms are `H(1-m,w_1+D)` and `H(z,D_1)`.
Vandermonde in `k` gives `H(m+u,q)`; independently, Vandermonde in `g`
gives `H(1-m-D,w_1)`. The resulting expression is `J(u)`. Maximize over
`I_u`, and combine the three branches. Polynomially many histogram
choices do not change normalized exponents. Taking the minimum with the
old bound for the same circuit proves (XSS14).

### A useful closed corollary

If, in addition, `0<=q<=d`, `w_1>=r`, and

\[
 d(m-q)(w_1-r)\ge rmD,
 \tag{XSS16}
\]

then the same closed correction as before is valid:

\[
 B_{\rm tr}\le B+\max\{0,F_{1,\rm raw}-\Delta\},\qquad
 \Delta=H(1-m,D)-H(1-s,D).
 \tag{XSS17}
\]

Indeed, for `rD>0`,

\[
 A'(r)=\log_2\frac{d(m-q)(w_1-r)}{rmD}\ge0,
\]

so concavity gives `A_*=A(r)`. Also

\[
 J'(0)=\log_2\frac{rmD}{d(m-q)(1-s-D)}\le0,
\]

because `(1-s-D)-(w_1-r)=1-beta>=0`. Thus
`J_*=J(0)=B+F_{1,raw}-Delta`. The entropy-integral comparison in the
baseline gives `J(0)>=A(r)`. If `r=0` or `D=0`, the interval is a
singleton or `Delta=0`, and the old bound handles the boundary directly.

This guard is weaker than the old first guard:
`(b-q)w_1>=r(beta-a-q)` is equivalent to
`(d-q)(w_1-r)>=rD`; multiply by `m` and use
`d(m-q)-m(d-q)=aq>=0` to obtain (XSS16). The old second guard follows
automatically. The continuous bound (XSS14) remains available even when
the closed guard fails.

## 4. Full-domain contacts

The following bounds concern one fixed exact family in each row. Every
push branch, recursive branch, nonnegative maximum, and legal color is
included. A pair `(tau,U)` means that the full normalized colored profile
at `tau` is at most the exact rational `U`.

| Exact family | Certified contacts `(tau,U)` |
|---|---|
| Recursive `(rho,gamma_1)=(1.3,.47)` | `(.24,.14310)`, `(.40,.19000)` |
| Recursive `(1.7,.47)` | `(.40,.18545)`, `(.44,.19560)` |
| Recursive `(2.2,.50)` | `(.43,.19229)`, `(.46,.19877)` |
| Recursive `(2.6,.54)` | `(.45,.19669)`, `(.48,.20234)` |
| Recursive `(2.8,.58)` | `(.47,.20032)`, `(.49,.20396)` |
| Recursive `(3,.60)` | `(.48,.20214)`, `(.49,.20384)`, `(.50,.20556)`, `(.51,.20730)` |
| Recursive `(3.4,.62)` | `(.50,.20561)`, `(.51,.20706)`, `(.54,.21148)`, `(.58,.21758)` |
| Recursive `(4,.65)` | `(.55,.21218)`, `(.60,.21801)`, `(.65,.22429)` |
| Direct `rho=4` | `(.60,.21873)`, `(.76,.22760)` |

For one fixed family, the supremum of `tau L+(1-tau)R` over its colors
is convex in `tau`. The trace bound is independent of `tau`. Hence a
chord between consecutive contacts bounds the same family's whole
intervening interval. No chord joins unrelated circuit families.

### Rational proof method for the contacts

Use the baseline Gibbs inequality, for any rational `0<p<1`,

\[
 H(x,y)\le-y\log_2p-(x-y)\log_2(1-p).
 \tag{XSS18}
\]

Positive entropies are replaced by these affine majorants. Negative
entropies use lower linear or multilinear vertex interpolants, valid by
concavity. If a relaxed box has an invalid corner for `H(z,D_1)`, use
the safe lower bound zero for that entire negative term on that box.

For (XSS14), apply the positive-entropy Gibbs bounds separately to `A(g)`
and `J(u)`. Each resulting expression is affine in its extra scalar.
According to its coefficient's sign, substitute any one globally valid
upper or lower interval endpoint from (XSS13). This removes `g` and `u`
without adding a subdivision dimension. The negative terms remain the
same `H(z,D_1)` and `H(1-m,beta-m)` already handled by interpolation.

Similarly eliminate `w_2` using (XSS9), treating both branches of `F_2`.
The resulting functions are separately convex in `(m,z,v)`, so their
maxima are attained at the eight box vertices. The old trace guard or
the stronger guard (XSS16) may also be used on an entire box, with safe
constant subtraction

\[
 \delta=\frac75\frac{(s-m_1)D_{\min}}{1-m_0}
\]

inside the nonnegative maximum. Take the better of these valid upper
bounds. The push and direct branches use the analogous two-coordinate
calculation.

Start from the whole domains in (XSS4), (XSS6), and (XSS9), tighten only
by necessary affine inequalities, and discard only empty boxes. For
recursive boxes, bisect the coordinate maximizing
`3(m_1-m_0), z_1-z_0, 2(v_1-v_0)`, in that tie order. For two-coordinate
boxes omit the third entry. The family `(1.3,.47)` has an empty recursive
branch; its complete domain is handled by the push calculation.

The two largest families have `gamma_1 rho>2`. Therefore the sign of
the affine function `c/2-m` is not copied from the old certificate.
Every affine interval extremum is evaluated at both relevant endpoints.
For example, the lower bound for `m-q=m-c/2+v` is

\[
 \min\{m_0-c(m_0)/2,m_1-c(m_1)/2\}+v_0.
 \tag{XSS19}
\]

This removes the old auxiliary restriction `gamma_1 rho<=2`; the exact
circuit construction itself never required that restriction.

Rational Gibbs probabilities can be proposed by approximate stationary
points, rounded to multiples of `10^{-12}` and clamped to
`[10^{-9},1-10^{-9}]`. Acceptance uses only exact rational comparisons
with outward logarithm enclosures. Normalize a positive rational into
`[1,2]`, put `z=(x-1)/(x+1)`, and use

\[
 \ln x=2\sum_{j=0}^{31}\frac{z^{2j+1}}{2j+1}+\mathcal R,
 \qquad 0\le\mathcal R<2^{-100}.
 \tag{XSS20}
\]

The tail follows from `z<=1/3`. Products and divisions are rounded outward
on the `2^{-120}` grid. Divide by an independently enclosed `ln 2` and
round base-two logarithms outward to multiples of `10^{-14}`. Approximate
optimization chooses useful rational planes; it does not accept boxes.

The contact subdivisions are finite computations performed before the
input algorithm. Their scalar variables do not add an input-dependent
enumeration or optimization step.

All 42 push/recursive branch calculations and both direct calculations
terminated with exact rational acceptance. The accepted leaf counts are
given below in the same contact order as the preceding table. Each pair
is `(push leaves, recursive leaves)`; zero means an empty recursive domain.

| Family | Accepted leaf counts by contact |
|---|---|
| `(1.3,.47)` | `(312,0)`, `(25,0)` |
| `(1.7,.47)` | `(120,114)`, `(117,200)` |
| `(2.2,.50)` | `(72,15257)`, `(69,12963)` |
| `(2.6,.54)` | `(51,14967)`, `(52,12777)` |
| `(2.8,.58)` | `(45,10518)`, `(46,9848)` |
| `(3,.60)` | `(41,9577)`, `(41,9210)`, `(42,8710)`, `(42,8529)` |
| `(3.4,.62)` | `(51,9117)`, `(53,8901)`, `(69,9168)`, `(75,9562)` |
| `(4,.65)` | `(59,9168)`, `(78,9961)`, `(80,10667)` |
| Direct `rho=4` | `184`, `250` |

These counts report the completed calculation; the mathematical claims
are the whole-domain inequalities and exact rational acceptance rules,
not the use of numerical optimization to propose planes.

## 5. The whole reflected profile

Add the two exact endpoint circuits, valid for every `tau`:

\[
 f_{\rm push}(\tau)=.58414212731239\,\tau,\qquad
 f_{\rm pull}(\tau)=.85319345691908\,(1-\tau).
 \tag{XSS21}
\]

The constants enclose `H(t,a)+H(1-t,b)` and `H(1-s,t-a)`, respectively.
Let `f` be the minimum of these lines and all eligible consecutive
contact chords from Section 4. A chord is eligible only inside its
certified interval. Retain both one-sided values at discontinuities.

Set

\[
 D_c=h(t)-h(s)-H(s,a),\qquad
 .26905132960667\le D_c\le .26905132960673,
 \quad K=\frac{875}{2592},
\]

\[
 U=f(\tau),\quad V=f(1-\tau),\qquad
 \Theta=(2\tau-1)D_c+U-V.
\]

Then the complete scalar inequality is

\[
 \boxed{U+V+K\Theta^2\le S,\qquad S=.41113.}
 \tag{XSS22}
\]

All selected values are below `1/4`, so `|Theta|<.52` and the left side
is increasing in each of `U,V`. It is convex in `tau` on every common
affine refinement interval and is convex in `D_c`. The breakpoints of `f`
are exactly

\[
 \left\{0,\frac{2425000000000}{9700570910413},\frac25,
 \frac{43}{100},\frac{3759}{8300},\frac{47}{100},\frac{12}{25},
 \frac{49}{100},\frac12,\frac{291}{580},\frac{51}{100},
 \frac{27}{50},\frac{11}{20},\frac35,\frac{5709}{9355},
 \frac{16693148922977}{22715773922977},1\right\}.
 \tag{XSS23}
\]

Adjoin their reflections and check the interval endpoints, both applicable
one-sided values, and both endpoints of the interval for `D_c`. There are
124 rational comparisons, including harmless duplicates at continuous
junctions. Their maximum is

\[
 \frac{7169585626176460495449293952290503}
 {17438976000000000000000000000000000}
 =.4111242326485489\ldots < .41113,
 \tag{XSS24}
\]

attained at `tau=291/580` and its reflection `289/580`. The rational
margin is

\[
 \frac{100576703539504550706047709497}
 {17438976000000000000000000000000000}>5.7\cdot10^{-6}.
\]

The numerical values of `S` for different matching types are not directly
comparable. The running-time comparison uses the rebalanced reduction
below, with all type-dependent entropy terms recomputed.

## 6. Unequal cores, rational types, and the finite compiler

Put `R=h(t)`, `Q=h(s)+H(s,a)`. For a fraction `lambda` of row-oriented
core coordinates, the endpoint objective is

\[
 \Phi(\lambda,\tau)=
 \lambda[\tau R+(1-\tau)Q+U]
 +(1-\lambda)[(1-\tau)R+\tau Q+V].
\]

Completing the square using (XSS22) gives

\[
 \Phi(\lambda,\tau)\le\frac{R+Q+S}{2}
 +\frac{1296}{875}(\lambda-1/2)^2.
 \tag{XSS25}
\]

The entropy curvature bound is valid for these types:

\[
 \frac{1296}{875}(\lambda-1/2)^2
 =\frac{20}{7}(1-2s)^2(\lambda-1/2)^2
 \le1-h\bigl(s+(1-2s)\lambda\bigr).
 \tag{XSS26}
\]

This follows from `1-h(1/2+x)>=2x^2/ln 2>20x^2/7` on the whole binary
entropy domain. Thus the complete mixed-core profile hypothesis holds.

The new rational types require a divisibility change. Use `H_0=1000`,
take a sufficiently large fixed `k` divisible by `1000`, and use
microblocks of length

\[
 N_0=k^2+1000k.
\]

The grouping discrepancies are still at most `12k`. The added matching
dummy positions have target row-one, query-one, and query-zero counts
`450k,65k,75k`, respectively. These have ample slack for the discrepancies
and for fitting query ones and zeros into the corresponding row symbols.
Both the description overhead `2 log_2(k+1)/k` and the new padding factor
`1+1000/k` have the same limiting behavior required by the compiler.

Keep the core-fraction grid size `1000`. Its quadratic interpolation loss
is now at most `(1296/875)/(4*1000^2)<3.71*10^{-7}`, below the earlier
allowance. Increase the fixed seed and amplification depth as necessary
to retain the complete compilation allowance `zeta=10^{-6}`. Every exact
cover, aggregation identity, grouping restriction, and stored finite
adjacency list remains valid. Dovetailing over these finite data and
checking exact integer matrix equality gives a terminating uniform
startup search. The startup bound supplied here is finite, not practical.

At input length, use the same count descriptions, tensor products of
stored adjacency lists, actual gate names, and output-sensitive incidence
enumeration. The additional scalar entropy optimizations in the proof
are absent from this input-time implementation.

## 7. Retyping the reduction and the full outer ledger

The three-dictionary reduction is unchanged except for its rational types
and block scale. Its low-deficiency canonical layers satisfy
`1/5<k/M<4/5` exactly as before. Since the new `s=.14<1/5`, both integral
cores remain positive in the required range. Replacing `H_0=500` by
`1000` gives integral counts for all new types and only a fixed boundary
overhead.

The canonical transformed pattern density and type-dependent constants
are

\[
 u=t-a+b=.46,\qquad
 D_{\rm can}=H(1-u,a)+H(u,b),
\]

\[
 \eta=1-h(u),\quad \alpha=1+h(s)-s,\quad
 J=1-H(s,a)-H(1-s,t-a).
 \tag{XSS27}
\]

The canonical support bound, expectation identity, and `K/T` ratio are
the same binomial/entropy identities at these new rational arguments.
In particular,

\[
 h(u)+D_{\rm can}=1+h(s)-J.
\]

The gain is recomputed from its full formula:

\[
 g_*=-\frac12+\frac12h(s)+\frac12H(s,a)+H(1-s,t-a)
       -\frac12h(t)-\frac12S-\zeta.
 \tag{XSS28}
\]

Outward rational entropy evaluation as in (XSS20) proves

\[
 \begin{aligned}
 D_{\rm can}&\le D_U=\frac{58153814247997}{10^{14}},\\
 \alpha&\le\alpha_U=\frac{144423881164287}{10^{14}},\\
 \eta&\le\eta_U=\frac{231078058989}{5\cdot10^{13}},\\
 g_*&\ge g_L=\frac{131017921157}{10^{13}}.
 \end{aligned}
 \tag{XSS29}
\]

Keep the dictionary-deficiency threshold `d_0=1/50`. Choose

\[
 \mu=\frac1{2(1+D_U+g_L)}
 =\frac{50000000000000}{159463993459567},
\]

\[
 M=1000\left\lfloor\frac{\mu n}{1000}\right\rfloor.
 \tag{XSS30}
\]

Then `3mu<1`, so the three dictionaries fit, and `g_L<d_0`. The two
binding input-dependent rates are exactly

\[
 \mu(1+D_U)=\frac12-\mu g_L
 =\frac{158153814247997}{318927986919134}=E_{\rm new}.
 \tag{XSS31}
\]

Here is the complete ledger, with all displayed decimal caps rounded
upward:

| Operation | Rate per original input coordinate |
|---|---:|
| Retained signed-circuit incidences and witness recovery | `E_new` |
| Canonical outputs and complete residue-cover state | `E_new` |
| All candidate-modulus energy evaluations | `<.463410854` |
| Selectors and shared witness preprocessing | `<.321270508` |
| Repeated prefix lookups | `<.328990608` |
| Repeated outside lookups | `<.352393990` |
| Direct cyclic convolution and common shifts | `<.372403143` |
| High-deficiency dictionary matching | `<.493728992` |
| Dictionary and canonical-layer preparation | `<.313550407` |

These are exact substitutions into, respectively, the full existing
input-cost expressions

\[
 \begin{gathered}
 \mu(1+D_U),\quad
 \mu(d_0+\eta_U+\alpha_U+D_U/64),\quad
 \mu(1+d_0+\eta_U),\\
 \mu[1+2(d_0+\eta_U)],\quad
 (1-\mu)/2+\mu(d_0+2\eta_U),\quad
 \mu(d_0+\eta_U+2D_U),\\
 1/2-d_0\mu,\quad 1/2-\mu g_L,\quad \mu.
 \end{gathered}
 \tag{XSS32}
\]

The modulus candidates, full residue state, repetitions of the local
covers, outside scans, canonical witnesses, integer-key bit lengths, and
large-deficiency fallback are included. The change in `H_0` contributes
only fixed padding and rounding costs. Handle the fixed finite small-input
range exhaustively, with polynomial dependence on `L`. This yields (XSS2)
under the same uniformity and exact-witness contract as the baseline.

## 8. Scope

The main new lemma replaces a constrained three-histogram maximization by
two concave scalar upper bounds and weakens the old closed-correction
guard. Retyping and the enlarged circuit menu convert that local change
into the stated general deterministic time exponent. The claim is not
restricted to a favorable class of instances or to a single active color.

The startup search remains a large input-independent constant, with no
practical numerical bound supplied here. The result does not combine this
time exponent with the repository's separate small-space exponent, and it
does not change the unrelated matching exponent `4/5`.
