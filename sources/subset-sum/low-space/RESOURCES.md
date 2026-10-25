# Complete resource certificate with a fixed design anchor

Author: Yilin Liu. Assistance: OpenAI Codex, including GPT-6 Astra.

All logarithms are binary. Every terminating decimal below is an exact
rational. Let

$$
q=137/250,
\quad X=17/2000,
\quad T=27/200,
\quad B_{\max}=203/1000,
\quad P=23/26,
\quad \alpha=52/75.
$$

Here $q$ is the fixed design anchor used in the core policies. The
actual dictionary exponent $q_*$ is determined below from the full
resource envelope. The certified low-density domain is
$0\le x_0\le x\le B_{\max}$, where $x_0$
is the least full-block deficiency proxy and $x$ is either local proxy.
The two local sides use their own $x$ throughout. For the strict-core
potential write

$$
\beta(x,z)=xt,
\qquad Pz=xt+(P-x)t^\alpha,
\qquad 0<t\le1.
$$

Its strict-extraction interpretation is used only for $x\le1/5$.
All larger local densities use oriented halves. The high-tail top uses
the general proportional deficiency bound.

## Exact entropy and root arithmetic

Define the rational numbers

$$
L_-=2\sum_{j=0}^{23}\frac1{(2j+1)3^{2j+1}},
\qquad L_+=L_-+\frac{2}{49\,3^{49}}\frac98,
$$

and

$$
S(z)=\sum_{j=1}^{128}\frac{z^{2j}}{(2j)(2j-1)},
\qquad E(z)=\frac{z^{258}}{258\cdot257(1-z^2)}.
$$

The positive logarithm and entropy series give, for $z=|1-2u|<1$,

$$
1-\frac{S(z)+E(z)}{L_-}
\le h(u)\le1-\frac{S(z)}{L_+}.
$$

All entropy bounds below follow by substitution in these rational
expressions. For a proposed root bracket, use opposite signs of

$$
J(x,z,t)=t^{52}(P-x)^{75}-(Pz-xt)^{75}.
$$

The second base is positive at all listed endpoints. Clearing
denominators makes every root test an integer comparison.

## The ownership branch

For $0\le x_0\le X$, put

$$
\begin{gathered}
p=.05,\quad \rho=.9,\quad
h_L=.28639695711<h(p)<h_U=.28639695712,\\
H=.76919282902>h(.225),\quad
\tau=.00722554602>1-h(.45),\\
D=(h_L-p)/2,\quad A=(h_L-3p)/4,\quad f_U=(h_U+p)/8,\\
v=H-1/2,\quad e=2H-1-.45+\tau,\quad
r=.95-H-\tau,\quad C=.75-q+(D-A)\rho.
\end{gathered}
$$

For $x<T$, choose $\sigma=\min(1,(C-x)/v)$. Let
$\phi=.371,.375,.3875$ on the intervals cut by $x=.03,.05$,
respectively. The resource functions are

$$
\begin{aligned}
R&=-D\rho+e\sigma+\beta(x_0,\rho)+\phi\beta(x,\sigma),\\
Q&=.75-A\rho-r\sigma-x+\beta(x_0,\rho)+\phi\beta(x,\sigma),\\
F&=\max(1-\sigma,.375+f_U\rho+v\sigma/2).
\end{aligned}
$$

The $R$ and $Q$ functions include the actual top ownership multiplicity.
On the uncapped domain $Q=q+R$. The local cap is handled directly.

The top root has the exact bracket
$859560838307/10^{12}<t<859560838308/10^{12}$ at $(X,\rho)$.
Set $b_t=X(859560838308/10^{12})$. Monotonicity makes $b_t$ an
upper bound on every top potential in this branch. Also

$$
.99998<\sigma(X)<1,
\qquad \sigma(T)>.53006,
\qquad C-v=.00849648632975<X.
$$

For $0\le x\le X$, use $\beta(x_0,\rho)\le b_t$,
$\beta(x,\sigma)\le x$, and $\sigma\le1$. This gives
$R<-.00030765$. For restart, use

$$
Q\le .75-A\rho-r\sigma(X)+\beta(x,\rho)-.629x.
$$

At fixed size, the root increases with density: its defining right
side decreases with $x$ at fixed $t<1$. Thus
$\beta(x,\rho)\le(859560838308/10^{12})x$ on this interval.
The resulting affine restart bound is largest at $X$, giving
$Q<.54769110<q-.0003$.

For $X\le x<T$, replace the top term by $b_t$ and set
$R_+(x)=-D\rho+e(C-x)/v+b_t+\phi\beta(x,(C-x)/v)$.
Use the proportional bound $\beta(x,\sigma)\le x\sigma$. The
entire interval is bounded by the concave rational quadratic

$$
R_+(x)\le-D\rho+b_t+\frac{(e+\phi x)(C-x)}v.
$$

Its critical point is $x_*=(\phi C-e)/(2\phi)$, clamped to the
corresponding interval. The three exact maxima are:

| Interval | $\phi$ | Maximum location | Strict upper bound |
|---|---:|---|---:|
| $[X,.03]$ | $.371$ | $29646127739029/2968000000000000$ | $-.00030589$ |
| $[.03,.05]$ | $.375$ | $.03$ | $-.00074738$ |
| $[.05,T]$ | $.3875$ | $.05$ | $-.00181446$ |

The first value before rounding is
$-1955191732793963624585813319/6391714532250880000000000000000$.
These rational comparisons prove $R<-.0003$ and $Q<q-.0003$ for
every strict local side. The state bound is

$$
F\le .375+f_U\rho+v/2=.547441072186<q-.00055,
$$

since the complementary atom has exponent below $.47$.

For $T\le x\le B_{\max}$, the oriented-half option gives, with
$h_0=374/461$ and $U=1-h_0$,

$$
\begin{aligned}
R_{\rm half}&\le-D\rho+(2h_0-3/2)/2+b_t
 =-8711179803779801/230500000000000000<-.03779,\\
Q_{\rm half}&\le .75-A\rho-U/2-T+b_t
 =57308853692168787/115250000000000000<.49726,\\
F_{\rm half}&\le1/2.
\end{aligned}
$$

These formulas use no local potential beyond its domain.

## The biased middle branch

For $X\le x_0\le T$, set

$$
\begin{gathered}
s=.42,\quad H_0=.741482739932>h(.21),\quad
\tau_0=.018546104967>1-h(.42),\\
H=.769192829014>h(.225),\quad
\tau=.007225546013>1-h(.45),\quad H_Q=.811278124460>h(.25),\\
D=.5+s-H_0-\tau_0=.159971155101,\\
A=.75+s-1.5H_0-\tau_0=.039229785135,\\
C=D-A=.120741369966,\quad f=H_0/4-.125=C/2,\\
v=H-.5,\quad e=2H-1-.45+\tau,\quad r=.95-H-\tau,\\
r_0=.605,\quad Z=49/600,\quad
\rho=\min(r_0+3x_0,.85),\quad b=.75-q=.202.
\end{gathered}
$$

Use $\phi_0=.345$ for $x_0\le.05$ and $.3575$ afterward, and the
same three local coefficients as above. For $x<T$, choose
$\sigma=\min(1,(b+C\rho-x)/v)$. Its minimum is greater than $.53$.
The resource functions are

$$
\begin{aligned}
R&=-D\rho+e\sigma+\phi_0\beta(x_0,\rho)+\phi\beta(x,\sigma),\\
Q&=.75-A\rho-r\sigma-x+\phi_0\beta(x_0,\rho)+\phi\beta(x,\sigma),\\
F&=\max(1-\sigma,.375+f\rho+v\sigma/2).
\end{aligned}
$$

The top credit includes the full outer code rate. Only the physical
image deficit scales in the preceding projection construction.

Two elementary consequences of the potential suffice:

$$
\beta(x,z)\le xz^{4/3}\quad(92x\le17P),
\qquad
\beta(x,z)\le xz^{7/5}\quad(161x\le11P).
$$

For the first, substitute $t=z^{4/3}$ in the root equation, divide
by $z$, and put $w=z^{1/225}$. The resulting expression
$xw^{75}+(P-x)w^{-17}$ decreases up to $w=1$, where its value is
$P$. The second follows identically from
$xw^{150}+(P-x)w^{-11}$ with $w=z^{1/375}$.
Since $x_0\le T<17P/92$ and $.85<.95^3$, we obtain
$\beta(x_0,\rho)<.95x_0\rho$. Locally use
$\beta(x,\sigma)\le x\sigma$.

### Complete uncapped mixed-domain reduction

On the rising top put

$$
B_0=b+Cr_0=.27504852882943,\quad k=3C=.362224109898,
\quad a_c=B_0-v=.00585569981543,
\quad z_c=\frac{a_c}{1-k}
 =\frac{585569981543}{63777589010200}.
$$

The uncapped region has $x\ge a_c+kx_0$. Partition the rising top
at $.05$ and $Z$, and the local interval at $.03$ and $.05$.
On each resulting polygon the upper function is the rational quadratic

$$
\overline R=-D\rho+e\sigma+.95\phi_0x_0\rho+\phi x\sigma,
\qquad \sigma=(B_0+kx_0-x)/v.
$$

Its coefficient of $x_0^2$ at fixed $x$ is $3(.95)\phi_0>0$.
On a diagonal edge the quadratic coefficient is
$3(.95)\phi_0+\phi(k-1)/v \ge35091383426981/538385658028000>0$.
On the cap edge it is $3(.95)\phi_0>0$.
Every nonvertical boundary therefore attains its maximum at an
endpoint. At a vertical boundary $x_0=z$, check the clamped critical
point $x_*=[b+C\rho(z)-e/\phi]/2$ on that boundary's interval.
Writing $c_X=a_c+kX$, the complete polygon list is:

| Top interval | Local interval | Vertices | Strict upper $\overline R$ |
|---|---|---|---:|
| $[X,.05]$ | $[X,.03]$ | $(X,c_X),(X,.03),(z_c,z_c),(.03,.03)$ | $-.0001771431$ |
| $[X,.05]$ | $[.03,.05]$ | $(X,.03),(X,.05),(.03,.03),(.05,.05)$ | $-.0006064236$ |
| $[X,.05]$ | $[.05,T]$ | $(X,.05),(X,T),(.05,.05),(.05,T)$ | $-.0016602729$ |
| $[.05,Z]$ | $[.03,.05]$ | $(.05,.05)$ | $-.0046558153$ |
| $[.05,Z]$ | $[.05,T]$ | $(.05,.05),(.05,T),(Z,Z),(Z,T)$ | $-.0040912578$ |

Each entry is obtained by rational substitution at the vertices and
the clamped vertical critical points. The first maximum is at
$x_0=X$, $x=7574073885281873/742000000000000000$.
On the plateau $\rho=.85$, the upper function increases with $x_0$
at fixed $x$, so its maximum is on $x_0=x$. That concave quadratic
has critical point $8011512564987923/62000000000000000$ and value
below $-.0037421981$. Thus $R<-1/6000$ and $Q=q+R<q-1/6000$
on the complete uncapped strict domain.

### The cap, state, incidence, and half sides

The cap satisfies $X\le x_0\le z_c<.01$ and
$x_0\le x\le a_c+kx_0<.01$. Here $\rho<.64$,
$.01<11P/161$, and $.64^2<.84^5$.
The stronger potential bound gives $\beta(x_0,\rho)<.84x_0\rho$.
For raw work maximize in $x$ at $a_c+kx_0$; for restart maximize
at $x=x_0$. The resulting upper bounds are

$$
\begin{aligned}
R_c&=-D\rho+e+.84(.345)x_0\rho+.371(a_c+kx_0),\\
Q_c&=.75-A\rho-r+(.371-1)x_0+.345\beta(x_0,\rho).
\end{aligned}
$$

The rational raw bound at $X,z_c$ gives $R_c<-.0003827602$.
For restart use the actual top potential. Its derivative along
$\rho=.605+3x_0$ is at most

$$
\beta'\le .635+.01\frac{1+3P}{\alpha(P-.01)}<.7.
$$

Indeed $t\le\rho\le.635$, $t^\alpha-t\le1$, and the implicit
denominator is at least $\alpha(P-.01)$ throughout the cap.
Consequently $Q_c'\le-3A-.629+.345(.7)<0$, so its maximum is at
$x_0=X$. The exact root bracket there is

$$
515456646931/10^{12}<t(X,.6305)<515456646932/10^{12}.
$$

Substituting its upper endpoint gives

$$
Q_c\le q_{\rm crit}
 :=54784907211651059/10^{17}.
$$
The raw-leaf term outside the cap equals $.75-q/2+C\rho-x/2$.
It decreases along the rising diagonal, while its capped value
increases up to $z_c$. Hence its global maximum is
$F<.5477835481<q-1/5000$. The complementary atom is below $.47$.

The incidence upper bound is

$$
I\le(\tau_0/2)\rho+.95\phi_0x_0\rho-x_0.
$$

It is convex on the two rising top intervals and decreases on the
plateau. Checking $X,.05,Z,T$, with both coefficients at $.05$,
gives $I<-.0008968462<-1/1250$.

For local $x\ge T$, oriented halves give

$$
\begin{aligned}
R_h&=-D\rho+(2H_Q-3/2)/2+\phi_0\beta(x_0,\rho),\\
Q_h&=.75-A\rho-(1-H_Q)/2-x+\phi_0\beta(x_0,\rho),\\
F_h&=\max(.5,.375+f\rho+(H_Q-.5)/4).
\end{aligned}
$$

Substitute $.95x_0\rho$ for the top potential and $T$ for $x$ in
restart. The two rising pieces are convex and the plateau is affine.
Their endpoint maxima give
$R_h<-.0357253886$, $Q_h<.5262657137$, and $F_h<.5041346134$.

## The ordinary high tail and fallback

For $T\le x_0\le x\le B_{\max}$, use top ratio $\rho_t=.72$ and
oriented local halves. Proportional extraction gives top deficiency
at most $\rho_tx_0m$, including $x_0>1/5$. With
$h_0=374/461$, $U=1-h_0$, and $A_0=1.25-1.5h_0$, the bounds are

$$
\begin{aligned}
R_t&\le-U\rho_t+(2h_0-1.5)/2+\rho_tB_{\max}/2
 =-17503/11525000<-.0015,\\
Q_t&\le .75-A_0\rho_t-U/2-T+\rho_tT/2
 =628599/1152500<.54543,\\
F_t&\le\max(.5,.375+(h_0-.5)\rho_t/4+(h_0-.5)/4)
 =11729/23050<.50886.
\end{aligned}
$$

The ordinary projection proof applies with
$p_0=1-h(1/4)-\xi/2>0$ and $p_0\rho_t<1/5$ for
$\xi\le B_{\max}=.203$. Its sufficient reserve condition has large slack
at $\rho_t=.72$. This use requires proportional extraction, not the
nonlinear potential outside its proved range.

## The critical dictionary exponent and fallback threshold

The cap restart is the largest complete threshold. The uncapped
restart maximum is below $.5478228569$, the ownership restart maximum
is below $.5477$, the biased leaf maximum is below $.5477835481$,
and the high-tail restart is below $.54543$. Thus choose

$$
q_*=q_{\rm crit}+10^{-9}
 =54784907311651059/10^{17},
\qquad B_*:=.75-q_*
 =20215092688348941/10^{17}<.203.
$$

All core policies retain their design anchor $q=.548$; their sizes,
image scales, and scalar functions are unchanged. Only dictionary
capacity and the high-deficiency trigger use $q_*,B_*$.

For a full block with deficiency $d\ge B_*m-O(1)$, the exact interval
fallback has time $O^*(2^{n/2}+2^{n/4}U/C)$ and space
$O^*(2^{n/8}+C)$, where $U\le O^*(2^{n/2-d})$ and
$C=\lceil2^{q_*m}\rceil$. The identity $q_*+B_*=3/4$ pays its
restart term at time exponent $n/2$. The trigger has only bounded
threshold error. Every remaining low-density profile lies in the
certified domain through $B_{\max}$.

## Preparation, initialization, and active state

The new linear-subspace signing cover has code-construction exponent
$(1+\theta)c+\phi d$, and it is built once per unsigned local core.
For $\theta=.45$, use the envelope

$$
\sigma\le\min\left(1,\frac{C_*-x}{v_*}\right),
\quad C_*=.30463325,\quad v_*=.26919.
$$

The upper code cost $\sigma(1.45+.3875x)$ increases up to
$x_*=C_*-v_*=.03544325$ and decreases afterward.
Its maximum is $1.45+.3875x_*<1.464$.
This construction is shared across outer top configurations.

The actual local cache rate is below
$.00723+.3875T=.0595425$; the outer biased top rate is below
$.85(.01855+.3575T)=.056790625$.
Owner labels have rate at most $.9X=.00765$.
The following rational envelopes include the indicated multiplicities:

| Operation | Time exponent per $m$ |
|---|---:|
| Weighted canonical-trace owner construction | $1.3653$ |
| Owner top weighted covers | $<1.42317$ |
| Biased top linear code | $<1.249$ |
| Shared local linear codes | $<1.464$ |
| Shared physical-image local prime preparation, depth $16$ | $1.478125$ |
| Biased top prime preparation, including top code | $<1.293$ |
| Top-dependent local coverage scans | $<1.465$ |
| Regenerated signing histograms | $<1.017$ |
| Original full-support histogram replay | $<1.057$ |
| Tensorized container preparation | $.3825$ |
| Cached biased top balanced-cell families | $1.34725$ |
| Pure lift scans and starts, including both code rates | $<1.49355$ |

Select physical integer useful layers and layouts before the primes.
The joint local universe contains a signing, a Good selected set, and
polynomially many layer/layout choices. Test the Good predicate with
the selected set outside the signing loop. Since
$K|\mathrm{Good}|\le\operatorname{poly}(n)2^c$, a candidate scan has
time $O^*(2^{c+r})$. Adding the depth-sixteen prime increment gives
$1+.45+.45/16=1.478125<1.5$. The same local Good-set test is not
repeated under top labels. All actual top labels remain in the top
prime universe. Both physical local images stay fixed before allocating
the post-prime top fine profile.

The active layer restrictions admit a short integer proof. The physical
top deficit satisfies $\delta/A\le.3575(.135)+O(\log A/A)<s/8$.
A useful top layer therefore has entropy at least $7/8-o(1)$.
The inequality $3^9>2^{14}$ gives $h(1/4)<5/6<7/8$, so after the
fixed cutoff it has $k\ge r/4$. Retain these top layers. They satisfy
$k>.1A$ and $r-k>.2A$; the inequalities
$10^{20}>2^9 9^{18}$ and $5^{10}>2^{23}$ give
$h(.1)>.45$, $h(.2)>.7$, and mean top entropy above $23/40$.
The same quarter-layer rule applies to strict locals because
$.3875T<.45/8$. Retain $k\ge r/4$ there as well.
Then $k\ge.1125c>c/9$ and $r-k\le.3375c<.35c$.
The exact comparisons $9^6>2^{19}$ and
$20^{80}<2^{75}7^{28}13^{52}$ give
$h(1/9)>1/2$, $h(.35)<15/16$, and local contrast below $7/16$.
Together with $c>.53m$, the atomic complement and this contrast are
at least $.03m$ below the movable mass $m/2$.
These physical cardinality restrictions are independent of the integer
bit length $L$ and retain a representation of every witness.

For weighted local coverage, the worst outer-code-inclusive scan is
less than $1.45+.635(.01855+.3575(.01))=1.464049375$.
This follows because its diagonal core policy leaves the upper cap
before $.01$, then the core-size derivative is below $-2.3$ while
the conservative outer-code derivative is below $.448$.
Signing histograms pay the separate factor
$K_{\rm outer}K_j(P_{\max}^2+P_{\max}+2^{m-c})$.
One shared residue workspace is regenerated; only scalar states and
polynomial seed lists are retained per signing.

The largest modulus scale is $.45m$. The uncompressed single-sign
child budget is below $1.122m$, and the natural local scale exceeds
$.195m$. For strict cores the latter follows from
$\sigma>.53$ and
$\ell/m\ge(.45-.3875T)\sigma-O(\log m/m)$.
For oriented halves, $d_A\le d_T$ and $d_A+d_T\le Bm$ give
$\ell/m\ge.25-B_{\max}/4-O(1/m)=.19925-O(1/m)$.
Thus the pure lift loop has exponent bounded by

$$
.45+.927+.05955+.057=1.49355<1.5.
$$

This includes the actual two family rates. The smaller leaf/capacity
start bound replaces $.927$ by $.548$.
Restart products use the declared analytic upper budget: its filtered
part exceeds $.56919m$, and its leaf-minus-shell gap exceeds $.05959m$.
These comparisons pay capacity and summed atomic/leaf starts even for
empty pruned streams. Actual unrestricted children have entropy above
$.64m$ and also satisfy the exact arbitrary-lift accounting identity.

All additional state has exponent at most $.5$ for support counting
and complementary atoms, $.45$ for canonical ownership traces and
residue arrays, $.265185$ for ownership tuples, $.357$ for biased
top tuples, $.36$ for high-tail tuples, $.0595425$ for local caches,
and $.057$ for outer labels. Constantly many simultaneous arrays add
their sizes. The actual leaves satisfy the strict scalar bounds above,
and each parent uses one capacity-$2^{q_*m}$ dictionary.

Use fixed grid $Q_{\rm grid}=10^{12}$, giving linear charge at most
$100m/Q_{\rm grid}=10^{-10}m$. A fixed coordinate cutoff bounds the
remaining combinatorial losses by another $10^{-10}m$.
The allowance coefficient $2\cdot10^{-10}$ is below the critical
capacity margin $q_*-q_{\rm crit}=10^{-9}$ and every other resource
margin. Owner and
ordinary-half incidence uses exact product normalization with polynomial
losses; biased-top incidence retains its separate strict margin.
Polynomial factors in arbitrary full input length remain explicit.

Consequently the complete resource system has uniform deterministic
time $\operatorname{poly}(n,L)2^{n/2}$ and writable-bit space
$\operatorname{poly}(n,L)2^{.18261635770550353n}$.
