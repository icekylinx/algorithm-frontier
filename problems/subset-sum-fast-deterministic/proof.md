# Deterministic Subset Sum through signed circuits and trace bounds

**Yilin Liu · GPT-6 Astra Pro**

## Abstract

We give an exact deterministic algorithm for Subset Sum on arbitrary signed binary integers, with indexed witness recovery. The refined running time is $C+\operatorname{poly}(n,L)2^{En}$, where $E=158153814247997/318927986919134<0.495892$ and $C$ is finite and independent of the input. Part I develops the signed-circuit compiler and reduction. Part II proves the trace and type refinement, and its continuous-domain checker certifies all 44 contact branches with exact rational arithmetic. A separate scalar checker reconstructs the reflected profile and the complete outer cost ledger. The refined theorem uses this new certificate directly; the older numerical menu is retained only as background with its explicit premise. No simultaneous space exponent is asserted for this algorithm.

## Theorem and proof structure

**Theorem F (refined deterministic algorithm).** On $n$ indexed signed integers of full binary encoding length $L$, the circuit and reduction constructions proved in Part I, with the parameter changes proved in Part II, decide feasibility and return an indexed witness in

$$
C+\operatorname{poly}(n,L)2^{En},\qquad
E=\frac{158153814247997}{318927986919134}.
$$

Here $C$ is the finite input-independent cost of constructing fixed circuit data, with no practical numerical bound claimed. All polynomial degrees are fixed and the complexity counts deterministic bit operations. The composition proof is Part II, Sections 2–7. The continuous-domain contact certificate in Part II, Section 4, and the scalar certificate in Section 9 discharge their separate numerical requirements. The circuit compiler and witness reduction are established by the mathematical arguments in the manuscript; the numerical programs are not a machine-checked formalization of those arguments.

**Theorem 1 (background conditional composition).** Assume the continuous-domain contact inequalities in Part I, Section I.4.2. The older baseline construction decides every signed binary Subset Sum instance and returns an indexed witness in

$$
C+\operatorname{poly}(n,L)2^{E_0n},
\qquad E_0=\frac{149809813343531}{301754962128739}<0.4964618056.
$$

Here $C$ is the finite input-independent cost of constructing fixed circuit data. The input-dependent term includes residue-cover construction. The imported baseline profile wrapper did not include the modules and receipt needed to replay its full-domain calculation; its reported leaf counts alone do not establish those contacts. This background theorem retains its explicit premise. Theorem F instead uses the reconstructed new menu and does not depend on the older numerical receipt. Both compositions use fixed polynomial degrees and the uniform deterministic bit model.

**Notation.** A witness is a binary vector `x` with `sum_i w_i x_i=t`. The input includes zero, negative and repeated weights. `L` includes every input bit. Logarithms are base two unless `ln` is written. Set `h(z)=-z log_2 z-(1-z) log_2(1-z)` with continuous endpoint values and `H(c,z)=c h(z/c)`.

The finite startup search builds fixed circuit data once; it is part of the running time, with no practical bound claimed here. Original indices remain attached to all representations and are recovered by the signed-circuit witness procedure.

## 2. Arithmetic primitives

Both algorithms use polynomial-time arithmetic on binary integers, the following prime bound, and exact array operations.

### 2.1. Prime density and enumeration

For real $x\geq1$, define

$$
\vartheta(x)=\sum_{p\leq x}\ln p,\qquad
\psi(x)=\sum_{p^j\leq x}\ln p,
$$

where $p$ ranges over primes and $j$ over positive integers. A prime power in $(\lceil n/2\rceil,n]$ contributes a factor of its underlying prime to $\binom n{\lfloor n/2\rfloor}$. This follows by subtracting the three factorial valuations; its contribution at this power is one and all other contributions are nonnegative. Consequently

$$
\psi(n)-\psi(\lceil n/2\rceil)
\leq\ln\binom n{\lfloor n/2\rfloor}\leq n\ln2.
$$

Induction gives $\psi(n)\leq4n$: for $n\geq2$, the induction bound is at most $2n+2+n\ln2\leq4n$, and the base case is immediate. Thus $\psi(x)\leq4x$ for real $x\geq1$.

Conversely, every prime valuation of $\binom{2m}m$ is at most the number of powers of that prime not exceeding $2m$. Since the central coefficient is the largest of the $2m+1$ coefficients whose sum is $2^{2m}$,

$$
\psi(2m)\geq\ln\binom{2m}m
\geq2m\ln2-\ln(2m+1).
$$

Put $m=\lfloor x/2\rfloor$. Integrating the tangent-line bound $1/u\geq4/3-4u/9$ on $[1,2]$ gives $\ln2\geq2/3$. Thus $\psi(x)\geq x/2$ for $x\geq64$: it suffices that $\ln(x+1)+4/3\leq x/6$, which holds at $64$ by $65<128$ and $\ln2<1$, and whose right side grows faster thereafter. The prime-power contribution beyond the first power is at most

$$
\psi(x)-\vartheta(x)
=\sum_{j=2}^{\lfloor\log_2x\rfloor}\vartheta(x^{1/j})
\leq4\sqrt{x}\log_2x.
$$

For $x\geq2^{20}$ the last bound is at most $x/4$ (the ratio $\log_2x/\sqrt x$ decreases in this range). We have proved

$$
x/4\leq\vartheta(x)\leq4x\qquad(x\geq2^{20}).
$$

It follows that, for $P\geq2^{20}$,

$$
\#\{p:P<p\leq32P\}
\geq\frac{\vartheta(32P)-\vartheta(P)}{\ln(32P)}
\geq\frac{4P}{\ln(32P)}.
$$

If a nonzero integer has absolute value less than $2^b$, at most $b\ln2/\ln P$ primes greater than $P$ divide it. The fraction of primes in this interval dividing that integer is therefore at most $2b/P$. This bound holds for all $P\geq2^{20}$. The interval ratio $32$ contributes a fixed factor.

All these primes can be generated deterministically in $P\operatorname{poly}(\log P)$ bit operations. Start with the integers through $\lfloor32P\rfloor$, and, for each unmarked integer starting at two, mark its proper multiples. A number remaining unmarked is prime: a composite has a smaller prime divisor, already processed. The number of marking iterations is at most $32P\sum_{d\leq32P}1/d=O(P\log P)$ even if all integers, rather than just primes, are charged. Index arithmetic has $O(\log P)$ bits.

### 2.2. Exact array and polynomial operations

For two length-$q$ arrays of integers of at most $b$ bits, compute cyclic convolution directly by

$$
c_r=\sum_{j=0}^{q-1}a_j b_{r-j\bmod q}.
$$

This uses $q^2$ multiplications and additions on integers of $O(b+\log(q+1))$ bits. The same bound applies to cyclic correlation. Both reductions charge this quadratic cost for their moduli.

In fixed dimension $d$, a polynomial of coordinatewise degree at most $M$ has at most $(M+1)^d$ coefficients. Store them in an array. Addition, monomial shifts, and multiplication by a fixed polynomial take polynomial time in the degree and coefficient bit length. Integer arithmetic computes binomial coefficients and factorials through order $M$. These operations support conditional-expectation arguments.


# Part I. A faster deterministic algorithm

This part proves the baseline compiler and reduction theorem used by Theorem F.

The reduction splits the coordinates into a prefix and two balanced outside
parts. A deterministic cover supplies binary–ternary representations of
each prefix; exact matching circuits join compatible records at equal
integer keys.

## I.1. Affine-majorant rebalancing

We develop the colored-circuit framework of Alman and Li [3] and Ye and Li [4], beginning with affine-majorant rebalancing.

### I.1.1. A finite rebalancing lemma

Let $\mathcal I$ and each $\mathcal J_i$ be nonempty finite sets, with positive real pairs

$$
(a_{ij},b_{ij}),\qquad i\in\mathcal I,\quad j\in\mathcal J_i.
$$

Fix real numbers $p,q$. Suppose that, for every parameter in the closed unit interval,

$$
\min_{i\in\mathcal I}\sum_{j\in\mathcal J_i}
       a_{ij}^{\tau}b_{ij}^{1-\tau}
\leq \exp\bigl(\tau p+(1-\tau)q\bigr),
\qquad 0\leq\tau\leq1.
\tag{1}
$$

For $\lambda>0$, define

$$
F_0(\lambda)=1+\lambda,
$$

$$
F_d(\lambda)=
\min_{i\in\mathcal I}\sum_{j\in\mathcal J_i}
a_{ij}F_{d-1}\!\left(\lambda\frac{b_{ij}}{a_{ij}}\right)
\qquad(d\geq1).
\tag{2}
$$

The finite minima are attained. Put

$$
A_{ij}=a_{ij}e^{-p},\qquad B_{ij}=b_{ij}e^{-q},\qquad
\delta_{ij}=\ln\frac{B_{ij}}{A_{ij}},\qquad
D=\max_{i,j}|\delta_{ij}|.
\tag{3}
$$

The constant $D$ is finite.

**Lemma I.1.1.** Under (1), every integer depth $d\geq1$ satisfies

$$
F_d\!\left(e^{(p-q)d}\right)
\leq
\exp\left(pd+K\ln2+\frac{D^2d}{8K}\right),
\qquad K=\lceil\sqrt d\rceil.
\tag{4}
$$

In particular,

$$
K\ln2+\frac{D^2d}{8K}
\leq
\left(\ln2+\frac{D^2}{8}\right)\sqrt d+\ln2
=o(d).
\tag{5}
$$

**Proof.** On nonnegative real functions define

$$
(Tf)(t)=
\min_{i\in\mathcal I}\sum_{j\in\mathcal J_i}
A_{ij}f(t+\delta_{ij}),\qquad t\in\mathbb R.
\tag{6}
$$

The operator is monotone and positively homogeneous:

$$
f\leq g\ \Longrightarrow\ Tf\leq Tg,
\qquad T(cf)=cTf\quad(c\geq0).
\tag{7}
$$

The normalized functions

$$
G_d(t)=e^{-pd}F_d\!\left(e^{(p-q)d+t}\right)
\tag{8}
$$

satisfy

$$
G_0(t)=1+e^t,\qquad G_d=TG_{d-1}.
\tag{9}
$$

Indeed, substituting (2) into (8) gives (6), because

$$
\delta_{ij}=\ln(b_{ij}/a_{ij})+p-q.
$$

For an integer $K\geq1$, put

$$
f_K(t)=\left(1+e^{t/K}\right)^K,
\qquad \phi_K(t)=\ln f_K(t).
\tag{10}
$$

The binomial theorem gives

$$
f_K(t)\geq1+e^t.
\tag{11}
$$

Direct differentiation yields

$$
\theta(t):=\phi_K'(t)
=\frac{e^{t/K}}{1+e^{t/K}}\in(0,1),
$$

$$
0\leq\phi_K''(t)
=\frac{e^{t/K}}{K(1+e^{t/K})^2}
\leq\frac1{4K}.
\tag{12}
$$

Taylor's theorem gives, for every real $\delta$,

$$
\phi_K(t+\delta)-\phi_K(t)
\leq\theta(t)\delta+\frac{\delta^2}{8K}.
\tag{13}
$$

Normalizing (1) gives

$$
\min_i\sum_j A_{ij}^{\tau}B_{ij}^{1-\tau}\leq1.
\tag{14}
$$

At each $t$, choose a minimizing list for $\tau=1-\theta(t)$. Equations (3), (13), and (14) give

$$
\begin{aligned}
(Tf_K)(t)
&\leq f_K(t)e^{D^2/(8K)}
       \min_i\sum_j A_{ij}e^{\theta(t)\delta_{ij}}\\
&= f_K(t)e^{D^2/(8K)}
       \min_i\sum_j A_{ij}^{1-\theta(t)}B_{ij}^{\theta(t)}\\
&\leq e^{D^2/(8K)}f_K(t).
\end{aligned}
\tag{15}
$$

The first inequality holds for each list before minimization, allowing the chosen list to depend on $t$ as in (2).

Keeping $K$ fixed, (7), (9), (11), and (15) imply by induction

$$
G_d(t)\leq (T^df_K)(t)
\leq e^{D^2d/(8K)}f_K(t).
\tag{16}
$$

Since $f_K(0)=2^K$, substituting $t=0$ into (8) and (16) proves (4). The inequalities $\sqrt d\leq K<\sqrt d+1$ and $d/K\leq\sqrt d$ give (5). $\square$

### I.1.2. Tensor circuits

An exact integer depth-two circuit for a finite integer matrix $M$ is a factorization into integer matrices. Its left and right degrees are the maximum nonzero counts in a row of the left factor and a column of the right factor, respectively. Exactness means integer matrix equality, with signed coefficients.

Suppose that every index in a nonempty finite menu supplies a colored circuit for this same matrix. Write its color decomposition as

$$
M=\sum_{j\in\mathcal J_i}M_{ij},
\qquad M_{ij}=U_{ij}V_{ij}.
\tag{17}
$$

Remove gates having a zero factor on either side and discard empty colors. Let the color degrees be the positive integers

$$
a_{ij}=\deg_L(U_{ij},V_{ij}),\qquad
b_{ij}=\deg_R(U_{ij},V_{ij}).
\tag{18}
$$

**Proposition I.1.2.** For every $d\geq0$ and $\lambda>0$, there is an exact integer circuit for $M^{\otimes d}$ satisfying

$$
\deg_L+\lambda\deg_R\leq F_d(\lambda),
\qquad M^{\otimes0}=(1).
\tag{19}
$$

**Proof.** The one-gate circuit for $(1)$ proves (19) at $d=0$.

For a positive depth, choose a menu index attaining (2). For each of its colors, apply the induction hypothesis at the smaller depth and the scaled weight

$$
\lambda_j=\lambda\frac{b_{ij}}{a_{ij}}.
$$

Let the resulting child degrees be $L_j,R_j$. Tensor that child circuit with the color circuit for $M_{ij}$, and concatenate the resulting circuits over all colors, using disjoint gate tags. The computed matrix is exactly

$$
\sum_j M_{ij}\otimes M^{\otimes(d-1)}
=M^{\otimes d}.
\tag{20}
$$

Tensor products bound endpoint degrees by products, and concatenation by sums; coefficients remain integral. Hence

$$
\begin{aligned}
\deg_L+\lambda\deg_R
&\leq\sum_j\bigl(a_{ij}L_j+\lambda b_{ij}R_j\bigr)\\
&=\sum_j a_{ij}\bigl(L_j+\lambda_jR_j\bigr)\\
&\leq\sum_j a_{ij}F_{d-1}(\lambda_j)
=F_d(\lambda).
\end{aligned}
\tag{21}
$$

This proves (19). $\square$

Apply the numerical lemma with weight $\lambda=e^{(p-q)d}$. Since the two degrees are nonnegative, (19) bounds them separately:

$$
\deg_L\leq\exp\bigl(pd+O(\sqrt d)\bigr),\qquad
\deg_R\leq\exp\bigl(qd+O(\sqrt d)\bigr).
\tag{22}
$$

The implicit constants depend only on the fixed menu and affine majorant.

## I.2. Biased partial-matching circuits and uniform enumeration

### I.2.1. Typed matrices and colored profiles

Fix

$$
s=\frac{11}{100},\qquad t=\frac9{20},\qquad
a=\frac{13}{250},\qquad b=\frac{29}{500},\qquad a+b=s.
$$

A length is admissible if it is a nonnegative multiple of 500. For an
admissible length $N$, let $T_N$ have binary rows of weight $tN$
and ternary columns with $aN$ specified ones, $bN$ specified zeros,
and $(1-s)N$ stars. Its entry is one precisely when the row agrees
with every specified column position. Set $T_0=(1)$. Every row and
column has a matching partner, since $a<t$ and $b<1-t$.

For $0\le x\le c$, write

$$
H(c,x)=c\log_2c-x\log_2x-(c-x)\log_2(c-x),
$$

with $0\log_20=0$. In particular $H(c,x)=c h(x/c)$ when $c>0$.
For a colored exact integer factorization, delete gates with a zero
factor and let $A_j,B_j$ be its positive left and right color degrees.
Its colored volume is

$$
\Upsilon(\tau)=\sum_j A_j^\tau B_j^{1-\tau},\qquad 0\le\tau\le1.
$$

Section I.1 applies to these exact integer color degrees.

Use the finite lookup menu

$$
\rho\in\{13/10,17/10,2,11/5,12/5,13/5,14/5,31/10,33/10\}.
$$

For each such $\rho$, put

$$
a\le m\le s,\qquad \beta=a+\rho(m-a),\qquad m\le z\le\beta.
\tag{23}
$$

Throughout this menu, $\beta\le .2434<t<1-t$. The two envelopes are

$$
L_\rho(m,z)=\max\{0,H(t,z)+H(1-t,\beta-z)-H(1-m,\beta-m)\},
$$

$$
R_{\rm old}(m,z)=H(b,m-a)+H(\beta-m,z-m).
\tag{24}
$$

We form the continuous envelope $R_{\rm new}$ from the two bounds and a
simpler certified envelope $\widehat R_\rho$.

### I.2.2. Exact lookup circuits with simultaneous concentration

The elementary binomial bounds

$$
\frac{2^{n h(j/n)}}{n+1}\le\binom nj\le2^{n h(j/n)}
\tag{25}
$$

follow from the largest term in the binomial distribution of parameter
$j/n$, with the endpoint values interpreted directly.

Fix an integer monomial size $m_0\in[aN,sN]$, and set

$$
B_0=\lfloor aN+\rho(m_0-aN)\rfloor,\qquad
T_{m_0}=\left\lceil N^2\binom N{m_0}/\binom{B_0}{m_0}\right\rceil.
$$

Choose $T_{m_0}$ independent uniform $B_0$-subsets, retaining an
occurrence label when the same subset is chosen more than once. A fixed
$m_0$-set is missed with probability at most $e^{-N^2}$.

Require two further bounds on the same lists. For every binary row $x$
and integer $z_0$, the number of occurrences intersecting
$\operatorname{supp}(x)$ in exactly $z_0$ positions is at most
$6\nu+3N$, where

$$
\nu=T_{m_0}\frac{\binom{|x|}{z_0}\binom{N-|x|}{B_0-z_0}}
 {\binom N{B_0}}.
\tag{26}
$$

For every typed query $y$, with specified sets $Y_1,Y_0$, and every
integer $j_0$, the number of occurrences satisfying
$Y_1\subseteq B$ and $|B\cap Y_0|=j_0$ is at most
$6\nu'+4N$, where

$$
\nu'=T_{m_0}
 \frac{\binom{bN}{j_0}\binom{(1-s)N}{B_0-aN-j_0}}
 {\binom N{B_0}}.
\tag{27}
$$

An out-of-domain binomial coefficient is zero. If $X$ is a sum of
independent indicators with mean $v$, then
$\mathbb E e^X\le e^{(e-1)v}$, and consequently
$\Pr(X>6v+dN)\le e^{-dN}\le2^{-dN}$.
There are at most $2^N\operatorname{poly}(N)$ row events,
$3^N\operatorname{poly}(N)$ query events, and
$2^N\operatorname{poly}(N)$ coverage events. A union bound proves
that all three requirements hold simultaneously at every sufficiently
large admissible $N$. The deterministic compiler below finds such fixed
finite circuits by exact search.

Assign every $m_0$-set $U$ to the first occurrence $B(U)$ containing
it. Gates have labels $g=(m_0,B,\sigma)$, where $B$ includes its
occurrence label and $\sigma\in\{0,1\}^{B}$. Define

$$
P[x,g]=[x|_B=\sigma],
$$

$$
Q[g,y]=(-1)^{m_0-aN}
 \#\{U:Y_1\subseteq U\subseteq Y_1\cup Y_0,\ |U|=m_0,
                \ B(U)=B,\ \sigma|_U=1\}.
\tag{28}
$$

Then $PQ=T_N$ exactly: expanding
$\prod_{i\in Y_1}x_i\prod_{i\in Y_0}(1-x_i)$ by inclusion-exclusion
gives precisely (28), with each monomial assigned once. Monomials
merged at a fixed gate have the same sign. Their combined coefficient
has magnitude at most $2^{bN}$.

Color a gate by $(m_0,z_0)=(m_0,|\sigma|)$. Gates with $z_0<m_0$
have no query neighbor and are removed. There are $O(N^2)$ colors.
Each row has at most the count (26) gates of a given color. Counting
each contributing monomial separately gives the right-degree bound

$$
\binom{bN}{m_0-aN}\binom{B_0-m_0}{z_0-m_0}.
\tag{29}
$$

Let $m=m_0/N,z=z_0/N,\beta'=B_0/N$. The identity

$$
\binom N{B_0}\binom{B_0}{m_0}
 =\binom N{m_0}\binom{N-m_0}{B_0-m_0}
$$

and (25) show that the left and right degrees are polynomial times
$2^{NL}$ and $2^{NR_{\rm old}}$, respectively, with $\beta'$
substituted for $\beta$ in (24). The ceiling in $T_{m_0}$ adds at
most one to each expected occurrence count and is absorbed in that
polynomial.

### I.2.3. Counting distinct query gates

Fix a query and a lookup occurrence counted in (27), and put
$j=j_0/N$. If its assignment has weight $zN$ and its gate is
nonzero at this query, it is one on $Y_1$ and has at least
$(m-a)N$ ones in $B\cap Y_0$. If the latter count is $uN$,
the number of assignments is

$$
\binom{jN}{uN}\binom{(\beta-a-j)N}{(z-a-u)N}.
$$

Here and in the following calculation $\beta$ may also denote the
actual rounded lookup density $\beta'$. Define

$$
C(j)=H(b,j)+H(1-s,\beta-a-j)-H(1-m,\beta-m),
$$

$$
S(j,u)=H(j,u)+H(\beta-a-j,z-a-u).
\tag{30}
$$

Property (27) and (25) bound the number of occurrences by polynomial
times $2^{N\max(C(j),0)}$. Therefore

$$
R_{\rm agg}(m,z)=\max_{j,u}\{\max(C(j),0)+S(j,u)\},\qquad
R_{\rm new}=\min(R_{\rm old},R_{\rm agg})
\tag{31}
$$

is a right-degree exponent. The maximum ranges over the binomial domain
and $u\ge m-a$. Each gate assignment is counted once, with harmless overcounting of
assignments lacking an assigned monomial. The integer $(j,u)$ pairs add
a polynomial factor to the degree bound of the same signed factorization.

For continuity and explicit evaluation, put

$$
v=m-a,\quad w=z-a,\quad B=\beta-a,\quad c=1-s.
$$

We have $0\le v\le b$, $v\le w\le B<c$. Let

$$
u_1=\max\{v,bw/(1-a)\},
$$

$$
F_1=H(b,u_1)+H(c,w-u_1)+H(1-z,\beta-z)
                         -H(1-m,\beta-m),
$$

$$
F_2=\begin{cases}
 H(B,w),&B\le b\ \text{or}\ v\le bw/B,\\
 H(b,v)+H(B-b,w-v),&B>b\ \text{and}\ v>bw/B.
\end{cases}
\tag{32}
$$

At $B=0$, take $F_2=0$. Then

$$
R_{\rm agg}=\max(F_1,F_2).
\tag{33}
$$

Indeed, $\max(\max(C,0)+S)=\max(\max(C+S),\max S)$.
The entropy chain identity and maximization over $j$ give

$$
\max_j(C+S)=H(b,u)+H(c,w-u)+H(1-z,\beta-z)
                            -H(1-m,\beta-m).
$$

For example, after selecting the $u$ ones from the first region and
$w-u$ ones from the second, the remaining $B-w$ lookup positions
are split optimally between regions of sizes $b-u$ and $c-w+u$;
their entropy is $H(b+c-w,B-w)=H(1-z,\beta-z)$.
The unconstrained optimum in $u$ is $bw/(1-a)$, so imposing
$u\ge v$ gives $F_1$. Its other feasibility constraints hold since
$B<c$ and $v\le\min(b,w)$.
For $S$ alone, the unconstrained split in a region of size $j$
has $u=jw/B$. It attains $H(B,w)$ in the first case of (32).
In the second case the optimum has $u=v$; the function
$H(j,v)+H(B-j,w-v)$ increases up to $j=vB/w>b$, and hence is
maximal at $j=b$. The same condition implies $w-v\le B-b$,
so the entropy arguments are valid. All formulas agree at branch
boundaries and extend continuously to their compact domain, including
$B=0$.

### I.2.4. A rational improvement used in the profile certificate

If $m>a$ and

$$
\rho(m-a)^2\ge b(z-a),
\tag{34}
$$

then $vB\ge bw$ for the unrounded density $B=\rho v$. Since
$w\ge v>0$, this implies $B\ge b$. Both maxima in (33)
occur at $u=v$. The entropy chain identity now gives

$$
F_1=R_{\rm old}-[H(1-m,z-m)-H(1-s,z-m)],
$$

$$
F_2=R_{\rm old}-[H(\beta-m,z-m)-H(\beta-s,z-m)].
$$

For $0\le d<x\le1$,

$$
\frac{\partial H(x,d)}{\partial x}
 =-\log_2(1-d/x)\ge \frac{d}{x\ln2}\ge\frac75d.
$$

The last inequality follows, for example, from $\ln2<5/7$.
Integration and continuity at the endpoints prove

$$
R_{\rm new}(m,z)\le
 R_{\rm old}(m,z)-\frac75(s-m)(z-m).
\tag{35}
$$

At $m=a$, condition (34) forces $z=a$, so the zero saving recovers
the old bound. On the feasible region, define the saving as follows:

$$
\Delta_\rho(m,z)=
\begin{cases}
\frac75(s-m)(z-m),&m>a\text{ and (34) holds},\\
0,&\text{otherwise},
\end{cases}
\qquad
\widehat R_\rho=R_{\rm old}-\Delta_\rho.
\tag{36}
$$

Thus $R_{\rm new}\le\widehat R_\rho$. On a rectangular box
$[m_0,m_1]\times[z_0,z_1]$ with $m_0>a$ and
$\rho(m_0-a)^2\ge b(z_1-a)$, the certified saving is at least

$$
\frac75(s-m_1)\max\{0,z_0-m_1\}.
\tag{37}
$$

This rational quantity is the only occurrence improvement needed in
the finite certificate of Section I.4.

### I.2.5. Recursive positive containment and two orientation swaps

Use the direct occurrence circuit on the last profile interval and
recursive circuits on the others. We first establish their exact integer
matrix identities.

For an outer occurrence $B$, its local matrix is
$I[\sigma,U]=[U\subseteq\sigma]$, where $|\sigma|=zN$ and $|U|=mN$.
Complementing both labels and transposing gives positive containment on
$\beta N$ coordinates, with row size $(\beta-m)N$ and query size
$(\beta-z)N$. Choose a fixed first inner lookup density $\gamma$ and put
$C=\gamma\beta$. All widths in the profile table below satisfy
$\beta-z\le C\le\beta$ throughout the outer color domain. Indeed it is
sufficient to check $z=m$, and $(\beta-m)/\beta$ increases with $m$.

Cover every positive query by labelled $CN$-subsets and assign it uniquely
to the first covering occurrence. For a row-intersection color $wN$,

$$
\max\{\beta-z,C-m\}\le w\le\min\{\beta-m,C\}.
\tag{38}
$$

The same sampling and binomial identities as in Section I.2.2 give the
uniform positive-containment degree exponents

$$
F=\max\{0,H(\beta-m,w)+H(m,C-w)-H(z,C-\beta+z)\},
\quad G=H(C-\beta+z,w-\beta+z).
\tag{39}
$$

Sample a polynomial times
$\binom{\beta N}{(\beta-z)N}/\binom{CN}{(\beta-z)N}$ labelled inner
lookups. The expected number with row intersection $wN$ is that sample
count times
$\binom{(\beta-m)N}{wN}\binom{mN}{(C-w)N}/\binom{\beta N}{CN}$.
Its entropy exponent is the expression inside $F$. A simultaneous
Chernoff bound adds a nonnegative floor and a polynomial factor. A
positive query assigned to one lookup has exactly
$\binom{(C-\beta+z)N}{(w-\beta+z)N}$ matching assignment gates, giving
$G$. Unique query assignment makes the factorization exact.

If $P^{\rm in}Q^{\rm in}$ denotes that positive factorization, then

$$
I[\sigma,U]=\sum_h Q^{\rm in}[h,B\setminus\sigma]
                         P^{\rm in}[B\setminus U,h].
\tag{40}
$$

For an original signed query $(Y_1,Y_0)$ the coefficient at the new
labelled gate $(m,B,z,h)$ is

$$
\sum_{\substack{U=Y_1\cup V,\ V\subseteq Y_0,\ |U|=mN\\B(U)=B}}
(-1)^{|V|}P^{\rm in}[B\setminus U,h].
\tag{41}
$$

Substitution in the inclusion–exclusion identity (28) proves exact
matrix equality. The two endpoint exponents are therefore

$$
L^{(1)}=L_\rho+G,\qquad R^{(1)}=H(b,m-a)+F.
\tag{42}
$$

The transpose places $G$ on the outer row side; (42) uses the
uncorrected outer occurrence bound.

Positive containment admits the same operation again. In general, on a
universe of size $n$, rows of size $Tn$ and positive queries of size $An$
are covered by lookups of size $\gamma n$. At row intersection $wn$ the
occurrence exponent is

$$
L_0=\max\{0,H(T,w)+H(1-T,\gamma-w)-H(1-A,\gamma-A)\}.
$$

The residual matrix, after complement and transpose, has types
$T'=(\gamma-A)/\gamma$, $A'=(\gamma-w)/\gamma$.
If its degrees per residual coordinate are $(L',R')$, substitution gives
$(L_0+\gamma R',\gamma L')$. This proves the orientation rule used next.

In units of the original $N$, put

$$
C_1=\gamma_1\beta,\quad Q_1=\beta-z,\quad D_1=C_1-Q_1,
\qquad
\max\{Q_1,C_1-m\}\le w_1\le\min\{\beta-m,C_1\},
$$

$$
F_{1,\mathrm{raw}}=H(\beta-m,w_1)+H(m,C_1-w_1)-H(z,D_1),
\qquad F_1=\max\{0,F_{1,\mathrm{raw}}\}.
\tag{43}
$$

For the second inner level choose the fixed rule

$$
Q_2=C_1-w_1,\quad C_2=\max\{C_1/2,Q_2\},\quad D_2=C_2-Q_2.
\tag{44}
$$

When $w_1<C_1/2$, the choice $C_2=Q_2$ is exactly the first-level
push implementation. Otherwise use the half lookup $C_2=C_1/2$.
This fixed routing has last color and degree contributions

$$
\max\{Q_2,C_2-Q_1\}\le w_2\le\min\{D_1,C_2\},
$$

$$
F_2=\max\{0,H(D_1,w_2)+H(Q_1,C_2-w_2)-H(w_1,D_2)\},
\qquad G_2=H(D_2,w_2-Q_2).
\tag{45}
$$

Two orientation swaps give

$$
L^{(2)}=L_\rho+F_2,\qquad
R^{(2)}=H(b,m-a)+F_1+G_2.
\tag{46}
$$

At $w_1=C_1/2$, one has $D_2=G_2=0$ and
$F_2=H(D_1,Q_2)$, so the unmerged formulas agree at the routing boundary.
All displayed entropies include their continuous boundary values.

### I.2.6. Exact trace aggregation and pooled occurrence counts

Fix an outer color $(m,z)$ and labelled occurrences $B$ and $C\subseteq B$
with $|B|=\beta N$, $|C|=cN$, $c=\gamma_1\beta$. The first inner row
is $B\setminus U$, whose intersection with $C$ is $W=C\setminus U$.
After the next complement and transpose, the residual query is
$K=C\setminus W=U\cap C$. Hence every descendant incidence and its
coefficient depends on $U$ only through $K$ for these fixed labels.
The coefficient may be summed first:

$$
(-1)^{(m-a)N}\#\{U:Y_1\subseteq U\subseteq Y_1\cup Y_0,
 |U|=mN,\ B(U)=B,\ U\cap C=K\}.
\tag{47}
$$

The aggregated coefficient preserves (41), has $O(N)$ bits, and retains
both occurrence labels in its gate.

Write $j=|B\cap Y_0|/N$, $e=|C\cap Y_1|/N$,
$f=|C\cap Y_0|/N$, and $q=|K|/N=c-w_1$ in this subsection only.
For a fixed pair of occurrences there are at most
$\binom{fN}{(q-e)N}$ possible traces. Their full feasibility domain is

$$
\begin{gathered}
0\le j\le b,\quad0\le\beta-a-j\le1-s,\quad
0\le e\le a,\quad0\le f\le j,\\
0\le c-e-f\le\beta-a-j,\quad0\le q-e\le f,\quad
0\le m-a-q+e\le j-f.
\end{gathered}
\tag{48}
$$

The last constraint ensures an outside completion; each feasible trace
is counted once regardless of its number of completions.

Choose independent outer samples in polynomial multiplicity times
$\binom N{mN}/\binom{\beta N}{mN}$, and independently for each labelled
outer occurrence choose inner samples in polynomial multiplicity times
$\binom{\beta N}{(\beta-z)N}/\binom{cN}{(\beta-z)N}$. Put

$$
C_0(j)=H(b,j)+H(1-s,\beta-a-j)-H(1-m,\beta-m),
$$

$$
C_1(j,e,f)=H(a,e)+H(j,f)+H(\beta-a-j,c-e-f)-H(z,c-\beta+z).
\tag{49}
$$

Here $C_1(j,e,f)$ denotes an exponent, distinct from the lookup width
$C_1$ in (43). The outer histogram has at most a polynomial times
$2^{N\max(0,C_0(j))}$ occurrences. Fix any outer family satisfying
these bounds, before conditioning on an inner event. Across all eligible
labelled outer occurrences, the inner histogram indicators are independent
Bernoulli variables with common probability

$$
\frac{\binom{aN}{eN}\binom{jN}{fN}
\binom{(\beta-a-j)N}{(c-e-f)N}}{\binom{\beta N}{cN}}.
$$

A single Chernoff bound on their pooled sum gives at most a polynomial
times

$$
2^{N\max\{0,C_1(j,e,f),C_0(j)+C_1(j,e,f)\}}
\tag{50}
$$

pairs. Polynomial oversampling makes every cover, row-degree, and
pooled-histogram failure probability $\exp(-\Omega(N^2))$. A union bound
over $\exp(O(N))$ queries and labelled families and polynomially many
colors proves their simultaneous existence. Independence is used in the
unconditioned pooled-histogram estimate.

Consequently the aggregated circuit has unchanged left degree and right
exponent at most both the old bound in (46) and

$$
G_2+\max_{j,e,f\text{ in }(48)}
\bigl[\max\{0,C_1(j,e,f),C_0(j)+C_1(j,e,f)\}+H(f,q-e)\bigr].
\tag{51}
$$

Both bounds apply to the same integer circuit.

### I.2.7. A closed trace correction

Put $d=m-a$, $r=s-m$, $w=w_1$, $q=c-w$ and
$D=\beta-m-w$. Suppose

$$
\beta\ge s,\quad D\ge0,\quad0\le q\le d,\quad w\ge r,
$$

$$
(b-q)w\ge r(\beta-a-q),\qquad
rmD\le d(m-q)(1-s-D).
\tag{52}
$$

Then, with $\Delta=H(1-m,D)-H(1-s,D)\ge0$, the right degree obeys

$$
R^{\rm trace}\le H(b,m-a)+\max\{0,F_{1,\mathrm{raw}}-\Delta\}+G_2.
\tag{53}
$$

We prove each branch of (51). Let $k=q-e$. Completion gives
$f\le j-d+k\le r+k$, so
$H(f,k)\le H(q+r,q)\le H(b,d)$, proving the zero branch.

For the $C_1$ branch, increasing $j$ to $b$ only enlarges the finite
set of pairs $(C,K)$: relabel neutral positions as prescribed zeros
without removing old traces. Put $g=f-k$, so $0\le g\le r$. The
expression to maximize becomes

$$
H(a,q-k)+H(b,k)+H(b-k,g)+H(\beta-s,w-g)-H(z,c-\beta+z).
$$

The unconstrained maximizer in $g$ is
$(b-k)w/(\beta-a-k)$. It is nonincreasing in $k$ because
$\beta\ge s$; the first inequality on the second line of (52)
puts it at least $r$ for $k\le q$. The constrained maximum is thus
at $g=r$. Vandermonde summation over $k$ bounds this branch by

$$
B_1=H(b,d)+H(m,q)+H(\beta-s,D)-H(z,c-\beta+z).
\tag{54}
$$

For the $C_0+C_1$ branch, set $u=j-f-(d-k)$. Then
$0\le u\le\min(r,D)$. Relax $k\le d$ to $k\le d+u$;
two Vandermonde summations over $k$ and $g$ give

$$
\begin{aligned}
J(u)={}&H(b,d+u)+H(m+u,q)+H(1-s,D-u)\\
&+H(1-m-D,w)-H(1-m,w+D)-H(z,c-\beta+z).
\end{aligned}
\tag{55}
$$

The three terms depending on $u$ are concave, and their derivative
at zero is $\log_2[rmD/(d(m-q)(1-s-D))]$. The last inequality
of (52) makes it nonpositive. If $r=0$ or $D=0$, the feasible
interval is already $\{0\}$; otherwise that inequality forces
$d>0$ and $1-s-D>0$, while $m-q\ge a>0$. This justifies the
derivative or covers its boundary exceptions. Thus the maximum is
at zero. The entropy chain identity gives

$$
B_2=J(0)=H(b,d)+F_{1,\mathrm{raw}}-\Delta.
$$

Finally,

$$
B_2-B_1=
[H(\beta-m,D)-H(\beta-s,D)]
-[H(1-m,D)-H(1-s,D)]\ge0.
$$

Both brackets integrate $\partial_xH(x,D)=\log_2[x/(x-D)]$
over intervals of length $s-m$, and the first interval lies to the
left, where this derivative is larger. The three branch bounds prove
(53).

For the rational certificate we use only

$$
\Delta\ge\frac75\frac{(s-m)D}{1-m}.
\tag{56}
$$

Indeed $\log_2[x/(x-D)]\ge D/(x\ln2)\ge(7/5)D/(1-m)$
throughout the integral. On a rectangle $m\in[m_0,m_1]$,
$v=w_1-C_1/2\in[v_0,v_1]$, whose feasible colors satisfy (52),
the safe constant subtraction is

$$
\delta=\frac75\frac{(s-m_1)D_{\min}}{1-m_0}.
\tag{57}
$$

The certificate verifies the region conditions throughout each rectangle.
Elsewhere set $\delta=0$ and use (46).

### I.2.8. Finite matrices, rounding and the compiler interface

All recursive families have fixed depth and polynomially many colors.
At a fixed finite base, exhaustive search finds outer and inner families
satisfying the simultaneous finite cover and histogram requirements.
Form the coefficients (47), merge equal traces, and store the resulting
nonzero finite adjacency lists. Exact multiplication verifies the matrix
identity. Each coefficient sums at most $2^{O(N)}$ bounded integer
contributions, and consequently has $O(N)$ bits.

Apply the rebalancing and three-count compiler of Sections I.2.10–I.2.16
to these aggregated finite matrices. At the input length, enumerate tensor
products of their stored adjacency lists. Inner colors preserve the
original row/query counts and each compatible pair's unique joint
count description.

For each fixed family the supremum of
$\tau L+(1-\tau)R$ over its colors is convex in $\tau$.
Take $R$ to be the minimum of the two valid bounds for that aggregated
circuit, with its fixed routing. Convexity gives the contact chords in
Section I.4.

Rounding lookup sizes changes normalized parameters by $O(1/N)$.
Use the full trace expression (51) and the old bound for this step.
Their entropy terms are continuous on compact feasible polyhedra, and
limits of rounded feasible colors remain feasible. The
maximum over colors therefore has upper error $o(1)$, uniformly in
$\tau$. The same conclusion holds at the fixed push/half boundary:
the unmerged degree formulas agree there and (51) is a valid bound
on either finite construction. Alternatively one can use the old bound
in a shrinking neighborhood of that boundary before passing to a
sufficiently large base. The color and histogram polynomial factors
also contribute $o(1)$ per coordinate.

Section I.2.16 absorbs these fixed polynomial losses into the total
compiler allowance $\zeta=10^{-6}$ by choosing a sufficiently large
fixed base. Preprocessing is independent of the Subset Sum instance;
variable-length coefficients and gate labels have $O(M)$ bits, with
polynomial work per emitted incidence.


### I.2.9. Direct profiles, endpoint circuits, and rounding

Define the direct upper lookup profile

$$
V_\rho(\tau)=\sup_{(m,z)\text{ in (23)}}
 \{\tau L_\rho(m,z)+(1-\tau)\widehat R_\rho(m,z)\}.
\tag{58}
$$

It is convex in $\tau$, being a supremum of affine functions.
For every fixed $\varepsilon>0$, the exact colored circuit above,
at every sufficiently large admissible $N$, satisfies uniformly
for $0\le\tau\le1$

$$
\Upsilon_{N,\rho}(\tau)\le2^{N(V_\rho(\tau)+\varepsilon)}.
\tag{59}
$$

For rounding, use the continuous actual profile $(L,R_{\rm new})$.
The change in $\beta$ is below $1/N$, so uniform continuity on the
compact domains in (24), (32), and (33) gives a uniform $o(1)$ exponent
error. Its unrounded value is bounded by (58); polynomial factors and
$O(N^2)$ colors add $O(\log N)/N$.

Two additional exact circuits use one gate for each query or one gate
for each row. Their profiles are, respectively,

$$
\tau d_{\rm push},\qquad (1-\tau)d_{\rm pull},\qquad
d_{\rm push}=H(t,a)+H(1-t,b),\quad
d_{\rm pull}=H(1-s,t-a).
\tag{60}
$$

For the first circuit a row meets
$\binom{tN}{aN}\binom{(1-t)N}{bN}$ query gates and each query
meets one; for the second, a query meets
$\binom{(1-s)N}{(t-a)N}$ row gates and each row meets one.
At a fixed base length, the direct and recursive circuits of Sections I.2.2–I.2.8 form an exact menu for $T_N$. Tensor products and transposes give the mixed menus below.

### I.2.10. Constructive simultaneous grouping of three counts

**Lemma I.2.1.** Given $kd$ integer vectors in $[0,k]^3$, one can
deterministically partition them into $d$ groups of exactly $k$
vectors such that every group sum differs in each coordinate by at
most $12k$ from $k$ times the global coordinate average. The
algorithm takes polynomial time and uses polynomial-bit rational
arithmetic in the explicit input size.

**Proof.** At a node containing $qk$ vectors, split the target number
of groups into $q_1=\lfloor q/2\rfloor$ and $q_2=q-q_1$, unless
$q=1$. Start with $x_i=q_1/q$; this solves

$$
\sum_i x_i=q_1k,\qquad
\sum_i x_i v_i=(q_1/q)\sum_i v_i,\qquad0\le x_i\le1.
$$

While more than four coordinates are fractional, choose five and a
nonzero integer null vector for their four constraint columns. Such
a vector has $O(\log(k+1))$-bit entries by fixed-dimensional minors
(or elimination at the actual rank). Move maximally in one direction
until a coordinate reaches zero or one. At most $qk$ moves suffice.
Maintaining a common denominator, each move multiplies it by at most
one of the bounded null-vector entries, so the total bit length is
polynomial. At the end at most four coordinates are fractional, and
their sum is an integer. Round exactly this many to one, the others
to zero. The cardinality stays exact and each vector sum changes by
at most $4k$. Recurse on the selected set and its complement, with
deterministic tie breaking throughout.

A node's error relative to its target number of final groups times
the global group average becomes $(q_i/q)\Delta+e$ in a child,
where $\|e\|_\infty\le4k$. For every nontrivial split
$q_i/q\le2/3$. Thus a leaf's error is at most
$4k\sum_{j\ge0}(2/3)^j=12k$. The recursion and all its rational
operations have polynomial total size. $\square$

### I.2.11. Matching dummy positions and exact joint descriptions

Take $k$ to be a multiple of 500, and put

$$
c_{\rm pad}=500k,\qquad N_0=k^2+c_{\rm pad}.
\tag{61}
$$

For a typed row-query pair of length $k^2d$, divide its coordinates
into $kd$ fixed consecutive blocks of length $k$. Its joint
description records in each block the triple (row ones, query ones,
query zeros). Apply Lemma I.2.1 to this sequence, with deterministic
tie breaking. Each resulting group contains $k^2$ real coordinates;
write its three counts as $(U,V,W)$. They differ from
$(tk^2,ak^2,bk^2)$ by at most $12k$ each.

Append $c_{\rm pad}$ dummy positions, with prescribed counts

$$
u'=tN_0-U,\qquad v'=aN_0-V,\qquad w'=bN_0-W.
\tag{62}
$$

These integers satisfy
$v',w'\ge0$, $v'\le u'$, and $w'\le c_{\rm pad}-u'$.
Indeed, the four sufficient inequalities are

$$
ac_{\rm pad}\ge12k,\quad bc_{\rm pad}\ge12k,\quad
(t-a)c_{\rm pad}\ge24k,\quad
(1-t-b)c_{\rm pad}\ge24k,
$$

and all hold for our constants. Put dummy row ones in the first
$u'$ positions, query ones in the first $v'$, and query zeros
in the last $w'$. Every dummy position matches. Each padded group
therefore belongs to $T_{N_0}$, and its matching value is exactly
the matching value of its real coordinates. The same construction
applies to a transposed core by interchanging the endpoint roles.

Joint descriptions preserve exact factorization as follows.
Take disjoint circuit copies indexed by all formal descriptions with
the required global totals. A row uses only copies with its actual
row-count sequence, while a query uses only copies with its actual
two query-count sequences. Exactly one description is consistent
with both members of any pair. Every other copy has an absent endpoint, so their sum computes the
original matrix at every pair.

Among at most $(k+1)^{3kd}$ descriptions, a row enumerates at most
$(k+1)^{2kd}$ and a query at most $(k+1)^{kd}$. Their per-coordinate
degree overheads are at most $2\log_2(k+1)/k$ and $\log_2(k+1)/k$;
use the larger for either mixed endpoint. Padding inflates length by
$1+500/k$. Both losses vanish as the fixed $k$ increases.

Any remaining admissible length can be padded to the next multiple
of $k^2$ using fewer than $k^2$ fixed positions of matching type
$(t,a,b)$. This is a bounded additive cost once $k$ is fixed;
the zero-length matrix is handled separately. These are the restrictions used in mixed-core compilation.

### I.2.12. A joint endpoint objective

Let $T_N$ be the typed matrix of Sections I.2.1--I.2.11, and write

$$
R=h(t),\quad Q=h(s)+H(s,a),\quad D=R-Q,
\quad c=1-2s,\quad S_* =\frac{903}{2500},\quad C_* =\frac{20}{7}c^2.
$$

Section I.4 certifies a piecewise affine function $f$ with the following property: for every fixed $\epsilon>0$, all sufficiently large admissible $N$ admit a finite menu of exact colored integer circuits for the same matrix $T_N$, such that the minimum volume at parameter $\tau$ is at most $2^{N(f(\tau)+\epsilon)}$. The menu includes the two exact endpoint circuits. Define

$$
\begin{aligned}
R_U(q)&=qR+(1-q)Q,& R_V(q)&=qQ+(1-q)R,\\
v(q)&=\frac{R+Q+S_*}{2}+C_*(q-1/2)^2,\\
\delta_U(q)&=v(q)-R_U(q),&
\delta_V(q)&=v(q)-R_V(q).
\end{aligned}
\tag{63}
$$

For the baseline parameters, the contact premise of Section I.4.2 and the
entropy-compensation argument of Section I.4 give the profile inequality

$$
qf(\tau)+(1-q)f(1-\tau)
\le\tau\delta_U(q)+(1-\tau)\delta_V(q)
\qquad(0\le q,\tau\le1).
\tag{64}
$$

**Theorem I.2.2 (compiler under the profile hypothesis).** Suppose (64) holds. Fix a positive rational allowance $\eta$. One terminating deterministic preprocessing program supplies common exact integer adjacency enumerators for

$$
T_{m_1}\otimes T_{m_2}^{\top}
$$

at every pair of lengths divisible by $500$. Put $M=m_1+m_2$ and $q=m_1/M$ when $M>0$. Their endpoint degrees are bounded by

$$
C_0\,2^{(\delta_U(q)+\eta)M},\qquad
C_0\,2^{(\delta_V(q)+\eta)M},
\tag{65}
$$

where $C_0$ is input-independent. Adjacency lists are generated within these bounds times a polynomial in $M$. Gate identifiers and integer coefficients have $O(M)$ bits, up to fixed constants. The zero-length matrix is handled separately. The preprocessing depends only on the fixed circuit data and $\eta$.

### I.2.13. Fixed exact mixed templates

Choose a fixed integer $B$ and a sufficiently large multiple $k$ of $500$. Put $N_0=k^2+500k$ and $q_j=j/B$. For every $0\le j\le B$, consider the fixed matrix

$$
\mathcal Q_j=T_{N_0}^{\otimes j}
\otimes(T_{N_0}^{\top})^{\otimes(B-j)}.
$$

Tensor independently chosen members of the typed menus. Every resulting menu member computes this same matrix. Transposition exchanges the two degree bounds, so the minimum volume is at most

$$
2^{BN_0[q_jf(\tau)+(1-q_j)f(1-\tau)+\epsilon]}.
$$

By (64) this has the affine majorant with endpoint exponents $\delta_U(q_j)+\epsilon$ and $\delta_V(q_j)+\epsilon$. Apply Lemma I.1.1 and Proposition I.1.2 to these finite color-degree lists. For every sufficiently large depth $d$, an exact circuit for $\mathcal Q_j^{\otimes d}$ has endpoint exponents arbitrarily close to the targets, measured per $BN_0d$ coordinates. All menu members factor the same exact matrix, with the stated maximum degrees.

There are finitely many grid points. Fix one sufficiently large common depth $d_0$ and store an exact circuit for each $\mathcal Q_j^{\otimes d_0}$. Use these stored circuits thereafter.

### I.2.14. Joint descriptions and three-count grouping

Pad each original core to length $k^2d_i$, with the bounded divisibility conditions specified below. The added lengths are multiples of $500$, so fixed matching row/query strings of types $t,a,b$ embed the original matrix as a restriction of the padded matrix.

Apply the grouping construction of Section I.2.11 separately to each core's row-one, query-one, and query-zero counts. It gives $d_i$ groups of $k^2$ real coordinates, each with discrepancies at most $12k$. Append $500k$ matching dummy positions to each group, yielding $T_{N_0}$ or its transpose.

The padding targets lie within $12k$ of $225k,26k,29k$. The integral query-one and query-zero counts therefore fit among the dummy row ones and zeros, respectively.

Tag each restricted grouped circuit by its joint description. The uniqueness argument of Section I.2.11 proves that their sum equals the original matrix.

In the first core, an endpoint on the row side knows its row-count vector and guesses two query-count vectors; an endpoint on the query side does the reverse. The roles are exchanged in the second core. Each endpoint guesses at most $2k(d_1+d_2)$ counts from $\{0,\ldots,k\}$. Hence its logarithmic description overhead is at most

$$
\frac{2\log_2(k+1)}k\,k^2(d_1+d_2).
\tag{66}
$$

The micro-padding multiplies the grouped length by $N_0/k^2=1+500/k$. These two overheads tend to zero as the single fixed $k$ increases.

### I.2.15. Exact adjacent-template mixing

Choose the initial bounded padding so that

$$
d_1\equiv d_2\equiv0\pmod{d_0},\qquad
d_1+d_2\equiv0\pmod{Bd_0}.
$$

Round each positive core upward to a multiple of $k^2d_0$, then increase one core by fewer than $Bd_0$ microgroup units to meet the final condition. Only $O(Bd_0k^2)$ coordinates are added. A zero core can remain zero by rounding in the other core. The case of two zero cores is scalar.

Put $T=(d_1+d_2)/(Bd_0)$ and $q'=d_1/(d_1+d_2)$. For $0<q'<1$, set $j=\lfloor Bq'\rfloor$ and

$$
x=(j+1)T-d_1/d_0,\qquad y=d_1/d_0-jT.
$$

These are nonnegative integers, $x+y=T$, and

$$
\begin{aligned}
d_1&=d_0[jx+(j+1)y],\\
d_2&=d_0[(B-j)x+(B-j-1)y].
\end{aligned}
$$

After a permutation, the grouped matrix is exactly

$$
(\mathcal Q_j^{\otimes d_0})^{\otimes x}
\otimes(\mathcal Q_{j+1}^{\otimes d_0})^{\otimes y}.
$$

At $q'=0,1$ use the corresponding endpoint template. Tensoring the stored circuits gives the interpolation of their endpoint exponents. The linear terms of $\delta_U,\delta_V$ interpolate exactly; their common quadratic term gives, for $\lambda=Bq'-j$,

$$
(1-\lambda)\delta_\bullet(q_j)+\lambda\delta_\bullet(q_{j+1})
\le\delta_\bullet(q')+\frac{C_*}{4B^2}.
\tag{67}
$$

The bounded initial padding changes the logarithmic target by only $O(1)$: the two functions in (63) have bounded derivatives, and both the total length and the first-core length changed by a bounded amount.

### I.2.16. Allowances, uniform search, and enumeration

For the stated parameters $C_*=1521/875$. Take $B=1000$. Then $C_*/(4B^2)<4.35\cdot10^{-7}$. For $\eta=10^{-6}$, allocate less than $2.5\cdot10^{-7}$ to stored-template errors, less than $2.5\cdot10^{-7}$ to (66) and the micro-padding inflation, and less than $5\cdot10^{-7}$ to (67), including its micro-padding factor. Choose $k$ sufficiently large, then the common depth $d_0$. All choices are fixed independently of the input. The same construction works for any prescribed positive rational allowance by first enlarging $B$.

The grid targets can be tested with rational bounds: writing $x=q-1/2$ gives $\delta_U=S_*/2-xD+C_*x^2$ and $\delta_V=S_*/2+xD+C_*x^2$. Refine a rational interval for $D$ to any fixed tolerance. Dovetail over $k,d_0$ and tuples of finite integer factorizations, checking exact matrix equality and rational-exponent degree caps by integer-power comparisons. The preceding existence argument proves that this finite preprocessing search terminates.

At the input length, enumerate an endpoint's missing count descriptions, discard invalid ones, and enumerate the corresponding products of stored adjacency lists. The number of descriptions is bounded by (66); valid padded endpoints have positive degree, so enumeration fits (65) up to a polynomial. Tag gates by the description, template choices, and local gate indices. Coefficients are products of fixed stored entries, with $O(M)$-bit lengths.

Compute integer histogram caps by multiplying stored maximum degrees by an integer upper bound on description counts. Their exponents satisfy (65), completing Theorem I.2.2.

## I.3. A uniform deterministic reduction

Let $z_1,\ldots,z_n,\tau$ be integers of total binary encoding length $L$. Fix

$$
\begin{gathered}
s=\frac{11}{100},\quad t=\frac9{20},\quad
a=\frac{13}{250},\quad b=\frac{29}{500}=s-a,\\
\mu=\frac{100000000000000}{301754962128739},\quad
H_0=500,\quad\zeta=10^{-6}.
\end{gathered}
\tag{68}
$$

Write $H(x,y)=xh(y/x)$ and put

$$
\begin{gathered}
R=h(t),\quad Q_{\rm ent}=h(s)+H(s,a),\quad
J=1-H(s,a)-H(1-s,t-a),\\
S_*=\frac{903}{2500},\qquad
v_0=\frac{R+Q_{\rm ent}+S_*}{2},\qquad
g_*=\frac12+h(s)-J-v_0-\zeta.
\end{gathered}
\tag{69}
$$

The mixed-core circuit theorem of Section I.2 supplies exact integer factorizations and output-sensitive adjacency enumeration with the following per-input degree bounds. If a fraction $q$ of the main coordinates has the row orientation on side $U$, define

$$
\begin{aligned}
R_U(q)&=qR+(1-q)Q_{\rm ent},&
R_V(q)&=qQ_{\rm ent}+(1-q)R,\\
v(q)&=v_0+\frac{1521}{875}(q-1/2)^2,&
\delta_U(q)&=v(q)-R_U(q),\quad
\delta_V(q)=v(q)-R_V(q).
\end{aligned}
\tag{70}
$$

On $M_0$ main coordinates the two degree caps are at most a fixed constant times $2^{[\delta_U(q)+\zeta]M_0}$ and $2^{[\delta_V(q)+\zeta]M_0}$, respectively. Enlarge these integer caps to at least one. All circuit constants are input-independent.

Put $M=H_0\lfloor\mu n/H_0\rfloor$. Handle the fixed finite range of smaller $n$ by exhaustive search, at cost a fixed multiple of $\operatorname{poly}(L)$. Assume henceforth that $M$ meets the stated core ranges.

### I.3.1. Three dictionaries and canonical layers

Choose three disjoint $M$-coordinate blocks. Construct each sorted distinct-sum dictionary by repeated merging of

$$
\Sigma(X\cup\{i\})=\Sigma(X)\cup(\Sigma(X)+z_i),
$$

retaining one binary mask per sum. This costs $2^M\operatorname{poly}(n,L)$. Let $P$ be a block with largest dictionary, let $N=|\Sigma(P)|$, and denote the other two blocks by $P_U,P_V$. For analysis write $N=2^{(1-d)M}$.

If the exact integer test $N^{50}\le2^{49M}$ holds, then $d\ge d_0=1/50$. Place two complete $M$-block dictionaries in opposite halves and divide the remaining coordinates equally. Each half has at most $N2^{(n-2M)/2+O(1)}$ entries. Exact complement matching, retaining the stored equal-sum witnesses, decides the instance in

$$
\operatorname{poly}(n,L)2^{n/2-dM+O(1)}
\le\operatorname{poly}(n,L)2^{(1/2-d_0\mu)n+O(1)}.
\tag{71}
$$

The unused third block may be split in this branch. Henceforth $d<d_0=.02$. Let $\mathcal A\subseteq\{0,1\}^P$ be the $N$ retained masks of the prefix dictionary; the sum map is injective on $\mathcal A$. For a binary prefix $c$, write $\bar c=1-c$ and define

$$
q_c(K)=\sum_{i\in K}(2c_i-1)z_i
=\sum_{i\in K\triangle\operatorname{supp}(\bar c)}z_i
-\sum_{i\in\operatorname{supp}(\bar c)}z_i.
\tag{72}
$$

Let $d_c(k)=|\{b\in\mathcal A:|b\oplus\bar c|=k\}|$. Assign $c$ to the least layer $k$ with $(M+1)d_c(k)\ge N$, and call its class $\mathcal C_k$. The classes partition the binary prefixes. For a nonempty class, put $B=\binom Mk$ and $\kappa=k/M$. Then

$$
B\ge\frac N{M+1},\qquad
h(\kappa)\ge1-d-\frac{\log_2(M+1)}M.
\tag{73}
$$

Since $h(1/5)<.74$, it follows that $1/5<\kappa<4/5$ for sufficiently large $M$.

All classes can be computed in $2^M\operatorname{poly}(M)$ integer operations. For functions on the binary cube define

$$
\widehat f(S)=\sum_xf(x)(-1)^{S\cdot x},\qquad
(f*_{\oplus}g)(x)=\sum_yf(y)g(x\oplus y).
$$

The identity $\sum_S(-1)^{S\cdot(x\oplus y)}=2^M1_{x=y}$ follows by multiplying $1+(-1)^{x_i+y_i}$ over the coordinates. It proves exact inverse Walsh division by $2^M$ and $\widehat{f*_{\oplus}g}=\widehat f\widehat g$. Splitting on one coordinate computes a transform with $M2^M$ additions. For $A=1_{\mathcal A}$ and $h_k(x)=1_{|x|=k}$,

$$
d_c(k)=(A*_{\oplus}h_k)(\bar c),\qquad
\widehat h_k(S)=\sum_j(-1)^j\binom{|S|}j\binom{M-|S|}{k-j}.
\tag{74}
$$

A polynomial-size binomial table, one transform of $A$, and one inverse transform per layer suffice. All intermediate integers have $O(M)$ bits.

### I.3.2. Integral cores, label flips, and original integer keys

Fix a nonempty class $\mathcal C_k$. Put $M_0=M-H_0$ and choose

$$
m_1=H_0\left\lceil
\frac{(1-s)M_0-k}{(1-2s)H_0}\right\rceil,
\qquad m_2=M_0-m_1,
\qquad u_0=k-sm_1-(1-s)m_2.
\tag{75}
$$

Then $u_0$ is an integer with $0\le u_0<(1-2s)H_0=390$. Both cores are positive for sufficiently large $M$, and their lengths are multiples of $500$, making all support, row, and query counts integral.

A round consists of a labeled partition $P=H_1\sqcup H_2\sqcup R_0$ of sizes $m_1,m_2,H_0$, together with a flip vector $f\in\{0,1\}^P$. The untyped support family is

$$
\mathcal D=\{K\subseteq P:
|K\cap H_1|=sm_1,\quad
|K\cap H_2|=(1-s)m_2,\quad
|K\cap R_0|=u_0\}.
$$

Its size is

$$
K_0=\binom{m_1}{sm_1}\binom{m_2}{sm_2}\binom{H_0}{u_0}
=2^{h(s)M}\operatorname{poly}(M)^{\pm1},
\tag{76}
$$

uniformly in the layer. This uses
$2^{mh(s)}/(m+1)\le\binom m{sm}\le2^{mh(s)}$ and the fixed boundary size. A uniform partition contains each weight-$k$ mask with probability $K_0/B$: all coordinates, including the boundary, are permuted, and coordinate permutations are transitive on that layer.

For a solution prefix $c$ put $e_i=2c_i-1$. On $H_1\cup R_0$, the $U$ contribution is $e_i1_{i\in K}$ and the $V$ contribution is $c_i-e_i1_{i\in K}$. On $H_2$, the $V$ contribution is $e_i1_{i\notin K}$ and the $U$ contribution is $c_i-e_i1_{i\notin K}$. The ternary and binary contributions sum to $c_i$. Relabel a ternary value $1,-1,0$ as the query symbol $0,1,*$, respectively. A ternary value and binary row value sum to a binary value exactly when the row matches its query.

Both core queries have support density $s$. The original $U$ prefix key is

$$
\operatorname{blockkey}_U=\gamma(c,\mathcal D)+q_c(K),
\qquad
\gamma(c,\mathcal D)=\sum_{i\in H_2}(1-c_i)z_i.
\tag{77}
$$

Indeed on $H_2$ its contribution is $(1-c_i)+(2c_i-1)1_{i\in K}$, and elsewhere the first orientation has no translation. For a fixed $c$ and partition, distinct canonical masks $b=K\oplus\bar c\in\mathcal A$ give distinct keys in (77), by (72).

A coordinate flip complements its binary row and every specified query bit, preserving the wildcard and compatibility. Retain only flipped rows of weight $tm_j$ and flipped queries with $am_j$ ones and $bm_j$ zeros in core $j$. The boundary has no type restriction. Undo flips before forming numerical records, so their contributions use the original weights, target, dictionaries, and key identity (77).

For any compatible row/query pair on a core of length $m$, a uniform flip makes its row uniformly binary. The probability of meeting both type constraints is exactly

$$
\theta_m=
\frac{\binom{sm}{am}\binom{(1-s)m}{(t-a)m}}{2^m}.
\qquad
\theta=\theta_{m_1}\theta_{m_2}
=2^{-JM}\operatorname{poly}(M)^{\pm1}.
\tag{78}
$$

This probability is independent of the original compatible labels.

The row-oriented proportion on side $U$ is

$$
q=\frac{m_2}{M_0},\qquad
\kappa_0=s+(1-2s)q,\qquad
\kappa=\kappa_0+O(1/M).
\tag{79}
$$

After reordering coordinates, the two-core matrix is $T_{m_2}\otimes T_{m_1}^{\top}$. Use (70) for this orientation, tensoring with an explicit fixed boundary compatibility matrix. This gives common gate names, exact integer coefficients, and degree caps $D_U,D_V\ge1$ with

$$
\log_2 D_U\le[\delta_U(q)+\zeta]M_0+O(\log M)+O_{H_0}(1),
\quad
\log_2 D_V\le[\delta_V(q)+\zeta]M_0+O(\log M)+O_{H_0}(1).
\tag{80}
$$

### I.3.3. An exact polynomial-tensor round selector

Let $\mathcal U\subseteq\mathcal C_k$ be the unserved prefixes. For a partition and flip, let $W_c$ count the canonical masks $b\in\mathcal A$ such that $K=b\oplus\bar c$ belongs to $\mathcal D$ and meets both flipped type constraints. Uniform partition and flip averaging gives

$$
\mathbb E\sum_{c\in\mathcal U}W_c
\ge |\mathcal U|T,
\qquad
T=\frac{NK_0\theta}{(M+1)B}.
\tag{81}
$$

A round attaining this mean and all its actual counts can be computed in $2^M\operatorname{poly}(n,L)$ bit operations. To see this, introduce ten formal variables: $X_j,Z_j$ for $j=0,1,2$, recording regional sizes and regional $K$ counts; and $Y_j,V_j$ for $j=1,2$, recording core row-one and specified-query-one counts.

For local bits $(c_i,b_i)$ put $k_i=1\oplus c_i\oplus b_i$. The binary row before flipping is $1-b_i$ on core 1 and $b_i$ on core 2. For a local region and flip $(j,f_i)$ use the following monomial as the corresponding entry of a $2$ by $2$ matrix indexed by $(c_i,b_i)$:

$$
\begin{array}{c|c}
j&\text{entry}\\ \hline
1&X_1Z_1^{k_i}Y_1^{e_i'}V_1^{k_i e_i'},
\quad e_i'=(1-b_i)\oplus f_i\\
2&X_2Z_2^{k_i}Y_2^{e_i'}V_2^{(1-k_i)e_i'},
\quad e_i'=b_i\oplus f_i\\
0&X_0Z_0^{k_i}.
\end{array}
\tag{82}
$$

At an assigned coordinate retain its chosen matrix; at an unassigned coordinate sum over the six possible region/flip labels. Call the resulting local matrix $T_i$. The polynomial

$$
F=\sum_{c\in\mathcal U}\sum_{b\in\mathcal A}
\prod_{i=1}^M T_i(c_i,b_i)
\tag{83}
$$

counts completions and their canonical witnesses. Extract the coefficient with regional sizes $(H_0,m_1,m_2)$, regional $K$ counts $(u_0,sm_1,(1-s)m_2)$, row-one counts $(tm_1,tm_2)$, and query-one counts $(am_1,am_2)$. The regional $K$ counts already force the global layer.

Compute (83) by applying the tensor product of the local matrices to the length-$2^M$ indicator vector of $\mathcal A$, and sum the indicated output entries. Each tensor stage combines pairs of vector entries. Since all exponents are nonnegative, they may be truncated at their target values. There are at most $(M+1)^{10}$ coefficients per polynomial and at most six monomials per local matrix entry. The full tensor computation costs $2^M\operatorname{poly}(M)$ operations. Its coefficients count at most $4^M6^M$ objects and have $O(M)$ bits.

Expose a coordinate's region and flip simultaneously. If $R'$ coordinates and regional capacities $R_0',R_1',R_2'$ remain, then the number of uniform completions is

$$
\frac{R'!}{R_0'!R_1'!R_2'!}\,2^{R'}.
\tag{84}
$$

The extracted coefficient divided by (84) is the exact conditional expected witness mass. A feasible child $(j,f_i)$ has probability $R_j'/(2R')$. The parent mean is the weighted average of the child means. Compute them by (83), compare by integer cross multiplication, and choose a maximizing child. Factorials and comparisons have polynomial bit length. Repeat over all coordinates and extract the terminal target coefficients to obtain all $W_c$ within the claimed cost, proving (81).

There is a uniform upper bound sharper than $K_0$. In a fixed round, let $c'=c\oplus f$ on one core. On the specified support, the transformed row is $1-c'$; elsewhere it is $c'$. A transformed query with $am$ ones and $bm$ zeros therefore chooses $am$ support coordinates among the zeros of $c'$ and $bm$ among its ones. The row-weight condition forces $|c'|=(t-a+b)m$. Put

$$
u=t-a+b=\frac{57}{125}=.456,
\qquad k_{\rm typed}=H(1-u,a)+H(u,b).
$$

On either core there are at most $\binom{(1-u)m}{am}\binom{um}{bm}$ such supports; on core 2 the support is the complement of $K$. Including the fixed boundary,

$$
W_c\le K_{\rm typed}\le\operatorname{poly}(M)2^{k_{\rm typed}M},
\qquad k_{\rm typed}<.4981.
\tag{85}
$$

Use the sharper bound for upper costs, retaining denominator $NK_0\theta$ in (81).

### I.3.4. Actual-width buckets, canonical extraction, and implicit energy

Bucket the positive terminal counts into intervals $[w,2w)$ with $w$ a power of two. Choose a bucket $G$ maximizing $|G|w$. Since there are at most $M+1$ buckets,

$$
|G|w\ge\frac{|\mathcal U|T}{2(M+1)},\qquad
w\ge\frac{T}{2(M+1)}.
\tag{86}
$$

Let $K$ be the exact size of the full typed support family of this round, including the boundary. It is independent of the pattern whenever its transformed regional weights are feasible; patterns with another weight have count zero. By (85), $K\le\operatorname{poly}(M)2^{DM}$, where

$$
D=H(1-u,a)+H(u,b),\qquad
\eta=1-h(u),\qquad \alpha=1+h(s)-s.
\tag{87}
$$

Expanding the entropy terms of the same four-cell joint distribution in the two orders gives

$$
h(u)+D=1+h(s)-J,\qquad
\frac KT\le\operatorname{poly}(M)
2^{[d+h(\kappa)-h(u)]M}
\le\operatorname{poly}(M)2^{(d+\eta)M}.
\tag{88}
$$

**Shared canonical extraction.** After the round is fixed, the relation between a pattern $c$ and an accepted canonical witness $b\in\mathcal A$ is a fixed number of nonnegative coordinate counts,

$$
\sum_{i=1}^M e_i(c_i,b_i)=\vec t,
\qquad T_i[c_i,b_i]=X^{e_i(c_i,b_i)}.
$$

The ten variables of (82) suffice. For every witness prefix $p$ of length $j$, apply
$T_{j+1}\otimes\cdots\otimes T_M$ to $1_{\mathcal A}(p,\cdot)$ and store
its polynomial vector $F_p$. The $2^j$ vectors each have length $2^{M-j}$;
all depths cost $2^M\operatorname{poly}(M)$ in time and storage. Degrees
are $O(M)$ in a fixed number of variables, and coefficients have $O(M)$
bits. Nonnegative exponents permit truncation above each target.

For fixed $c$ the number of extensions of $p$ is exactly

$$
\left[X^{\vec t-\sum_{i\le j}e_i(c_i,p_i)}\right]
F_p[c_{j+1},\ldots,c_M],
\tag{89}
$$

with a negative residual count interpreted as zero. Querying the zero child and comparing its count with a requested lexicographic rank unpacks one witness in polynomial time. Shared $2^M\operatorname{poly}(n,L)$ preprocessing thus reports $w$ witnesses for each of $G$ patterns in $|G|w\operatorname{poly}(n,L)$ additional time. Their integer keys are distinct by canonical injectivity.

**One-canonical collision energy.** We choose a modulus before reporting witnesses. In a fixed number of regions prescribe the pattern weight $U_j$ and the support counts $A_j,B_j$ on its zero and one positions. Write $\mathcal R_c$ for this full typed support family. After fixed complements and orientations, the witness has the form $b(R,c)=R\oplus(1-c)$ and its key is a known translation plus $\sum_i z_i b_i$. Sign changes in $z_i$ and the corresponding permutation of $\mathcal A$ handle both orientations. For a positive modulus $q$ define the ordered energy

$$
\begin{gathered}
E_q(c)=\sum_{R,R'\in\mathcal R_c}
1_{\mathcal A}(b(R,c))
[d(R,R',c)\ne0]\,[q\mid d(R,R',c)],\\
d(R,R',c)=\sum_i z_i\bigl(b(R,c)_i-b(R',c)_i\bigr).
\end{gathered}
\tag{90}
$$

The orientation change is explicit: on the cores set $c^*=c\oplus f$, $b^*=b\oplus f$ on $H_1$, and $b^*=b\oplus f\oplus1$ on $H_2$. Take $R=K$ on $H_1$ and $R=\overline K$ on $H_2$. Then $b^*=R\oplus(1-c^*)$. Replace $z_i$ by $z_i^*=(-1)^{f_i+1_{i\in H_2}}z_i$ in differences. The affine translation preserves equalities and canonical injectivity. Use this transformed notation below.

Only the first endpoint is canonical. For a bucket with $w\le W_c<2w$, the aggregate energy at modulus one is less than $2|G|wK$. The oracle below computes every $E_q(c)$ in $2^{\alpha M}\operatorname{poly}(n,L,\log q)$ bit operations, independently of the modulus magnitude apart from $\log q$.

Put $\delta_i=b_i-b_i'\in\{-1,0,1\}$. In each region both endpoints have weight $|H_j|-U_j-A_j+B_j$, so their positive and negative difference counts agree. Their support difference has size at most twice $k=\sum_j(A_j+B_j)$, giving at most $k$ negative differences. Fill the ternary array

$$
f_q(\delta)=\left[\sum_i z_i\delta_i\ne0\right]
\left[q\mid\sum_i z_i\delta_i\right]
$$

on vectors satisfying these budgets, and set it to zero elsewhere. Its input support has at most $\sum_{j\le2k}\binom Mj2^j$ entries. Use four count variables $x,y,x',y'$ per region. Direct enumeration of the local bits gives the matrices, with rows $c_i$ and columns $b_i$,

$$
T_0=\begin{pmatrix}xx'&1\\1&yy'\end{pmatrix},\quad
T_+=\begin{pmatrix}0&x'\\0&y\end{pmatrix},\quad
T_-=\begin{pmatrix}x&0\\y'&0\end{pmatrix}.
\tag{91}
$$

The coefficient of $\prod_jx_j^{A_j}y_j^{B_j}(x'_j)^{A_j}(y'_j)^{B_j}$ in
$F_c=\sum_{b,\delta}1_{\mathcal A}(b)f_q(\delta)\prod_iT_{\delta_i}[c_i,b_i]$
is (90) for patterns having the prescribed regional weights $U_j$; discard the other output entries. Each admissible local pair is counted once.

For a general $T_0=\left(\begin{smallmatrix}a_0&b_0\\c_0&d_0\end{smallmatrix}\right)$, $T_+=(p_0,q_0)^\top e_1^\top$, and $T_-=(r_0,s_0)^\top e_0^\top$, set

$$
\mathcal D=a_0q_0-c_0p_0,\quad
\mathcal H=a_0d_0-b_0c_0,\quad
\mathcal V=b_0q_0-d_0p_0.
$$

The identities $\mathcal Hp_0+a_0\mathcal V=b_0\mathcal D$ and $\mathcal Hq_0+c_0\mathcal V=d_0\mathcal D$ prove a polynomial rank-three decomposition

$$
\begin{gathered}
\mathcal D T_\delta[c,b]
=\sum_{j=1}^3 P[j,\delta]U[c,j]V[j,b],\\
P=\begin{pmatrix}\mathcal H&\mathcal D&0\\1&0&0\\0&0&\mathcal D\end{pmatrix},\quad
U=\begin{pmatrix}p_0&a_0&r_0\\q_0&c_0&s_0\end{pmatrix},\quad
V=\begin{pmatrix}0&1\\\mathcal D&\mathcal V\\1&0\end{pmatrix}.
\end{gathered}
\tag{92}
$$

Order the columns of $P$ by $0,+,-$, so channel three receives the
negative differences. Transform $f_q$ by $\bigotimes_iP_i$ and the
canonical indicator by $\bigotimes_iV_i$, multiply coordinatewise, then
contract by $\bigotimes_iU_i$ to obtain $(\prod_i\mathcal D_i)F$.
Keep strings with at most $k$ channel-three symbols. In the first
transform, processed channel-three symbols plus unprocessed negative
differences stay within $k$; in the other transforms, a prefix or suffix
exceeding $k$ contributes only to discarded final channels. Every stage
therefore has at most

$$
R_k=\sum_{j\le k}\binom Mj2^{M-j}.
\tag{93}
$$

For example, after $t$ coordinates of the canonical-input transform it is $2^{M-t}\sum_{j\le k}\binom tj2^{t-j}\le R_k$; the analogous output bound is $2^t\sum_{j\le k}\binom{M-t}j2^{M-t-j}\le R_k$. These are ordinary coordinatewise contractions with polynomial arrays. Here $k=sM+O(1)$ and $s<1/3$, so $R_k\le\operatorname{poly}(M)2^{[1+h(s)-s]M}$. The initial difference table is smaller because $h(2s)+2s<1<\alpha$.

For (91), $\mathcal D=x'(xy-1)$ is a nonzero formal polynomial. The common multiplier is $\prod_j(x'_j)^{m_j}(x_jy_j-1)^{m_j}$. Remove the monomial factors and multiply by the truncated series

$$
(1-x_jy_j)^{-m_j}
=\sum_{\ell\ge0}\binom{m_j+\ell-1}{\ell}(x_jy_j)^\ell
\tag{94}
$$

with the appropriate sign. Known divisibility gives the exact $F_c$. The computation uses formal polynomials of degree $O(M)$ in a fixed number of variables, with polynomial coefficient lengths.

Enumerate the pattern and two support masks on the fixed $H_0$-boundary.
Restrict the canonical indicator to the first boundary witness, add the exact boundary difference to the test for $f_q$, and sum the two-core transforms. These
constantly many computations preserve the core budgets, state exponent,
and complete zero-difference exclusion. The witness family uses the
original cores and boundary, proving the signed-key oracle.

**Fixed-factor modulus.** Choose a polynomial bit bound $B_0\ge1$ for all nonzero complete key differences. If $K=1$, take $Q=1$. Otherwise fix $r=64$, and set

$$
t_0=\lceil(4K)^{1/r}\rceil,\qquad
P_0=2^{32}(B_0+r+2)^2t_0.
\tag{95}
$$

Sieve the primes in $(P_0,32P_0]$. Section 2.1 gives at least $P_0/\log_2P_0$ candidates, more than $2r$. A nonzero $B_0$-bit difference has at most $B_0/\log_2P_0$ prime factors in the pool. At least half the pool remains unused at every stage; therefore at most a $2B_0/P_0\le1/(2t_0)$ fraction of the unused primes divide it. Starting at $m=1$, compute $\sum_{c\in G}E_{mp}(c)$ for each unused candidate and choose a minimum. Conditional averaging reduces the surviving aggregate by a factor at least $2t_0$ at each stage. The product $Q$ of the $r$ chosen distinct primes satisfies

$$
K\le Q\le K\operatorname{poly}(n,L),\qquad
\sum_{c\in G}E_Q(c)
\le\frac{2|G|wK}{(2t_0)^r}\le |G|w/2.
\tag{96}
$$

Indeed $Q>P_0^r\ge t_0^r\ge4K$ and $t_0\le2(4K)^{1/r}$; $r$ is fixed, so all factors other than $K$ in $(32P_0)^r$ are polynomial. The number of candidate oracle calls is at most $K^{1/64}\operatorname{poly}(n,L)$. Their total time per round is

$$
2^{(\alpha+D/64)M}\operatorname{poly}(n,L).
\tag{97}
$$

Prime sieving and the scan of each output energy vector are smaller. The conditional prime argument is an instance of the implicit-counting multi-prime method of Jin, Park, Saha, and Xu [9]; the oracle (90)–(94) and its costs are supplied here.

Serve the explicit patterns with $E_Q(c)\le2w$; at least half of $G$ qualify. Extract $w$ canonical witnesses per served pattern by (89). Their ordered modular collisions are a subset of (90). If $n_y$ are their residue multiplicities, then

$$
\sum_y n_y=w,\qquad
\sum_y n_y^2\le w+E_Q(c)\le3w,\qquad
|S_c|\ge w/3\ge w/5,
\tag{98}
$$

where $S_c$ is the deduplicated residue support. Cauchy–Schwarz gives this bound; use $w/5$ in the cover below.


### I.3.5. Complete local covers and harmonic charging

For this fixed round initialize $U_c=\mathbb Z_Q$ for every served pattern. A residue $\delta$ newly covers

$$
A_f(\delta)=\sum_c\sum_{s\in S_c}1_{U_c}(\delta-s),
\qquad
\frac1Q\sum_\delta A_f(\delta)
=\sum_c\frac{|U_c||S_c|}{Q}
\ge\frac{w}{5Q}\sum_c|U_c|.
\tag{99}
$$

Store uncovered indicators in binary range-sum trees. On a candidate
interval $I$, sum the counts on $I-s\pmod Q$ over the stored $S_c$;
each shifted interval splits into at most two ordinary intervals. Bisect
$I$, compare child means by cross multiplication, and retain a child
with at least the parent mean. After $O(\log(Q+1))$ steps, including odd
interval lengths, a singleton attains the original mean. Delete its
covered points and repeat.

If $H$ patterns are served, at most

$$
D_i\le\left\lceil\frac{5Q_i}{w_i}
\left(1+\lceil\log_2(HQ_i)\rceil\right)\right\rceil
\tag{100}
$$

choices suffice. Indeed each step multiplies the uncovered count by at most $1-w_i/(5Q_i)$; using $1-x\le e^{-x}$ makes the final integer count less than one. Initialization costs $|G_i|Q_i$, and each search and deletion pass costs $|G_i|w_i\operatorname{poly}(n,L)$. Thus all local covering work and state cost $|G_i|Q_i\operatorname{poly}(n,L)$, including the residue deduplication. For $w_i=Q_i=1$, use residue zero. In general,

$$
D_i\le\operatorname{poly}(n,L)K/w_i,\qquad
\frac{D_i}{Q_i}\le\frac{\operatorname{poly}(n,L)}{w_i}.
\tag{101}
$$

Remove the served patterns and repeat the selector and bucket construction. Write $C_i=|\mathcal U_i|$, let $G_i$ be the selected bucket, and let $H_i$ be its served subset, so $|H_i|\ge|G_i|/2$ and $C_{i+1}=C_i-|H_i|$. Equation (86) implies

$$
\frac1{w_i}\le\frac{4(M+1)}T\frac{|H_i|}{C_i}.
$$

For every nonfinal iteration $|H_i|/C_i\le\int_{C_{i+1}}^{C_i}dx/x$, and the final term is at most one. Since the served sets are disjoint,

$$
\begin{aligned}
\sum_i|G_i|&\le2|\mathcal C_k|,\\
\sum_i\frac1{w_i}&\le\frac{4(M+1)(1+\ln|\mathcal C_k|)}T
\le\operatorname{poly}(M)\frac{B}{NK_0\theta},\\
I&\le K\sum_i\frac1{w_i}
\le\operatorname{poly}(M)K/T
\le\operatorname{poly}(M)2^{(d+\eta)M}.
\end{aligned}
\tag{102}
$$

Combining (101) and (102) gives the full filtering rate

$$
\boxed{\sum_i\frac{D_i}{Q_i}
\le\operatorname{poly}(n,L)\frac{B}{NK_0\theta}.}
\tag{103}
$$

Every local residue repetition is included. Equations (86), (96), and (88) also give

$$
\max_iD_i\le\operatorname{poly}(n,L)K/T
\le\operatorname{poly}(n,L)2^{(d+\eta)M}.
$$

The total reported-witness and complete-cover costs are at most

$$
\sum_i|G_i|w_i+\sum_i|G_i|Q_i
\le 2^M K\operatorname{poly}(n,L).
\tag{104}
$$

Shared witness-table preprocessing and selectors cost $I2^M\operatorname{poly}(n,L)$. All candidate-prime oracle calls cost $I2^{(\alpha+D/64)M}\operatorname{poly}(n,L)$. These charges include the full-family modulus scale and its residue states, in addition to harmonic filtering.

Each assigned round covers every residue for every served prefix. A common shift of its local residue sequence preserves coverage by translating the residue to be covered oppositely. Choose the modulus and shift separately in each round.

### I.3.6. Cached outer lists and balanced incidence bounds

Split the coordinates outside $P$ into $O_U,O_V$ of sizes differing by at most one, containing the whole blocks $P_U,P_V$, respectively. This is feasible since $3M\le n$. Cache the two exact lists using each designated dictionary and all binary masks on the other coordinates of that side. Retain the corresponding witnesses. Their sizes are at most

$$
|\mathcal O_U|,|\mathcal O_V|
\le2^{(n-M)/2-dM+O(1)}.
\tag{105}
$$

For a selected round, let $\mathcal B_U,\mathcal B_V$ be its allowed typed prefix records, after undoing its flips. Their exact full keys are

$$
\operatorname{key}(u)=\operatorname{blockkey}(u)+\operatorname{outersum}(u),
\qquad
\operatorname{key}'(v)=\tau-\operatorname{blockkey}(v)-\operatorname{outersum}(v).
\tag{106}
$$

The binary row universe has size $\binom m{tm}\le2^{Rm}$ and the query universe has size $\binom m{sm}\binom{sm}{am}\le2^{Q_{\rm ent}m}$. Together with (80), each weighted prefix universe obeys

$$
D_U|\mathcal B_U|,\ D_V|\mathcal B_V|
\le\operatorname{poly}(M)2^{[v(q)+\zeta]M_0+O_{H_0}(1)}.
\tag{107}
$$

Since $h''(x)=-1/[\ln(2)x(1-x)]$ and $h'(1/2)=0$,

$$
1-h(1/2+x)\ge\frac2{\ln2}x^2\ge\frac{20}{7}x^2.
$$

The last inequality uses $\ln2<7/10$. Because $(20/7)(1-2s)^2=1521/875$, (79) gives

$$
\frac{1521}{875}(q-1/2)^2\le1-h(\kappa_0).
$$

The relevant layers stay in $(1/5,4/5)$ and $\kappa-\kappa_0=O(1/M)$, so $M|h(\kappa)-h(\kappa_0)|=O(1)$. Thus

$$
D_U|\mathcal B_U|,\ D_V|\mathcal B_V|
\le\operatorname{poly}(M)2^{[v_0+1-h(\kappa)+\zeta]M}.
\tag{108}
$$

For modulus $Q_i$, rebuild the cached outside residue buckets and histograms. Enumerate the raw prefix patterns to form prefix-key histograms, convolve them directly with the outside histograms, and reflect the $V$ sums around $\tau$. The resulting nonnegative weighted-load array is

$$
W_i(r)=D_U\#\{u:\operatorname{key}(u)\equiv r\}
+D_V\#\{v:\operatorname{key}'(v)\equiv r\}.
$$

For the local cover $\delta_{i,1},\ldots,\delta_{i,D_i}$, scan all common shifts and choose $\sigma_i$ minimizing $\sum_jW_i(\delta_{i,j}+\sigma_i)$. Its value is at most

$$
\frac{D_i}{Q_i}
\left(D_U|\mathcal B_U||\mathcal O_U|
+D_V|\mathcal B_V||\mathcal O_V|\right).
\tag{109}
$$

Direct cyclic convolution and shift evaluation cost $O(Q_i^2)$ and $O(Q_iD_i)\le Q_i^2\operatorname{poly}(n,L)$ integer operations, respectively.

For each chosen residue and each $U$ prefix key $x$, access only the outside bucket at $\delta_{i,j}+\sigma_i-x$. On side $V$ access the bucket at $\tau-x-\delta_{i,j}-\sigma_i$. Emit its entries and only then enumerate each retained record's circuit adjacency. Raw prefix enumeration and bucket lookups pay the overhead; (109) pays every emitted record because both degree caps are at least one.

Sum (109) and use (76), (78), (103), (105), (108), and $B\le2^{Mh(\kappa)}$. The logarithm of the retained incidence volume, up to polynomial factors, is at most

$$
\begin{aligned}
&(n-M)/2-dM+[v_0+1-h(\kappa)+\zeta]M\\
&\qquad+[h(\kappa)-(1-d)-h(s)+J]M
=n/2-g_*M.
\end{aligned}
\tag{110}
$$

Both the deficiency and the layer entropy cancel. The outside lists remain balanced for every layer.

### I.3.7. Exact counting and binary witnesses

For each selected round and each local residue occurrence, use the common exact integer compatibility circuit on the retained records. Gate tags include both that round and that residue occurrence, or these instances are processed separately. Sort incidences by their full integer key and gate, aggregate the coefficients on each side, and sum the products of the two aggregates. Circuit exactness gives the nonnegative integer

$$
\sum_{u,v}
1_{\operatorname{key}(u)=\operatorname{key}'(v)}
1_{\text{coordinatewise compatible}(u,v)}.
\tag{111}
$$

Accept when the completed count is positive. A compatible equal-key pair reconstructs a binary prefix and two stored outside witnesses with total sum $\tau$.

Conversely, fix a genuine solution with prefix $c$. Its assigned good layer eventually serves it. The selected canonical keys are actual representations meeting the typed domains, and remain distinct by (72), (77). Its assigned complete local cover applies to every outside residue, also after the common shift. Consequently a compatible representation has its $U$ key in a selected residue. The target-adjusted $V$ key is exactly equal. Replacing either designated outside block by its stored equal-sum witness preserves both keys. Undoing the flips before forming the keys preserves the original input sums. Hence this local instance has positive count. If every completed count is zero, no solution exists.

Recover a pair from a positive count by bisecting the retained $U$ list and recounting, keeping a positive part, until one record remains; then bisect the $V$ list. Restricted counts retain the nonnegative interpretation and sum to the preceding count. The polynomially many restrictions each reduce incidence volume, so sorting, aggregation, and recovery add polynomial factors to (110).

### I.3.8. All remaining costs and uniformity

The remaining operations have the following bounds up to $\operatorname{poly}(n,L)$ factors. Here $I\le2^{(d+\eta)M}\operatorname{poly}(n,L)$, $Q_i\le2^{DM}\operatorname{poly}(n,L)$, and $\max_iD_i\le2^{(d+\eta)M}\operatorname{poly}(n,L)$.

$$
\begin{array}{c|c}
\text{operation}&\text{exponent per }n\\ \hline
\text{dictionary and canonical-layer preparation}&\mu\\
\text{canonical witness output and complete cover state}&\mu(1+D)\\
\text{all candidate-modulus energy evaluations}&\mu(\alpha+D/64+d+\eta)\\
\text{selector and shared witness preprocessing}&\mu(1+d+\eta)\\
\text{repeated raw prefix lookups}&\mu[1+2(d+\eta)]\\
\text{repeated outside lookups}&(1-\mu)/2+\mu(d+2\eta)\\
\text{direct convolutions and common shifts}&\mu(d+\eta+2D)\\
\text{high-deficiency dictionary matching}&1/2-d_0\mu\\
\text{retained incidences and witness recovery}&1/2-\mu g_*.
\end{array}
\tag{112}
$$

A raw prefix list has at most $2^M$ times a fixed boundary factor, since $R\le1$ and $Q_{\rm ent}<1$. Enumerating it for every round and residue therefore gives the prefix-lookup line. Even scanning both outside lists once per residue costs at most $I\max_iD_i\,2^{(n-M)/2-dM+O(1)}$, giving the outside line. Histogram convolution and shift scans cost $I\max_iQ_i^2\operatorname{poly}(n,L)$. The energy row includes every candidate prime at all 64 stages; the prime sieve is smaller. Section I.4 certifies all these rates at $d<d_0$.

There are $M+1$ layers and fixed numbers of boundary coordinates,
count variables and prime factors. The counts have polynomial bit length
in $n,L$. Comparisons and covers are exact; zero-difference tests are
deterministic. Section I.2 supplies terminating input-independent
compilation. Since $M=\mu n+O(1)$, lattice rounding adds $O(1)$ to
logarithmic costs and gives uniformity for arbitrary binary input lengths.

## I.4. Baseline analytic tools and numerical specification

This section records the baseline entropy tools, numerical menu, and cost
calculation. The analytic inequalities are proved below. The contact values
and subdivision counts in Section I.4.2 are historical reports for the older
menu, whose full-domain replay is absent from the imported material. They
remain the explicit premise of the background Theorem 1. The refined
Theorem F uses the independently reconstructed certificate in Part II,
Section 4. All terminating decimals denote exact rationals.

### I.4.1. Entropy inequalities and rational logarithms

For $0<q,p<1$, the inequality $\ln y\le y-1$ gives

$$
q\ln\frac pq+(1-q)\ln\frac{1-p}{1-q}\le0.
$$

It follows that

$$
H(x,y)\le-y\log_2p-(x-y)\log_2(1-p).
$$

Endpoints follow by continuity. The function $H(x,y)=xh(y/x)$ is jointly concave: apply concavity of $h$ with weights proportional to the two first coordinates, then multiply by their sum. Its restriction to an affine segment is therefore above the chord joining its endpoint values. These facts justify the affine bounds used below.

For a rational $1\le v\le2$, put $z=(v-1)/(v+1)$. Integrating the geometric series for $1/(1-z^2)$ gives

$$
\ln v=2\sum_{j=0}^{31}\frac{z^{2j+1}}{2j+1}+\mathcal R,
\qquad
0\le\mathcal R\le\frac{2z^{65}}{65(1-z^2)}.
$$

The tail bound follows by replacing its denominators by $65$. Round each positive summand downward to a multiple of $2^{-120}$; add $32\cdot2^{-120}$ and the displayed tail to obtain an upper bound. Apply the same calculation to $v=2$. For any positive rational $x$, write $x=2^k v$ with $1\le v<2$ and use $\log_2x=k+\ln v/\ln2$. The normalized numerator is nonnegative, so division by the opposite positive endpoint of the interval for $\ln2$ is valid. For the profile calculation, round the resulting base-two logarithms outward to multiples of $10^{-14}$. The scalar calculations in Section I.4.4 can retain the finer rational endpoints before this final rounding.

Entropy enclosures follow by rational interval evaluation of

$$
H(x,y)=x\log_2x-y\log_2y-(x-y)\log_2(x-y),
$$

with $0\log_20=0$ and $H(x,0)=H(x,x)=0$. Also

$$
h'(u)=\log_2\frac{1-u}{u},\qquad
h''(u)=-\frac1{(\ln2)u(1-u)}.
$$

Integrating the second derivative from $1/2$, where $h'=0$, yields $1-h(1/2+x)\ge2x^2/\ln2$ on $|x|\le1/2$. The same logarithm enclosures give $\ln2<7/10$.

### I.4.2. Recursive and trace-aggregated lookup contacts

Every decimal in the following table denotes an exact rational number.
The first two rows use (42), the middle six use the trace-aggregated
construction (43)–(53), and the last uses the direct occurrence
circuit of Sections I.2.2–I.2.4. Within a row, both contacts concern one
fixed circuit and one fixed routing rule independent of $\tau$.

| $\rho$ | $\gamma_1$ | Left $\tau$ | Upper bound | Right $\tau$ | Upper bound |
|---:|---:|---:|---:|---:|---:|
| $1.3$ | $.47$ | $.24$ | $.12004$ | $.40$ | $.16082$ |
| $1.7$ | $.47$ | $.40$ | $.15966$ | $.45$ | $.17177$ |
| $2$ | $.47$ | $.45$ | $.17078$ | $.475$ | $.1764$ |
| $2.2$ | $.47$ | $.475$ | $.17585$ | $.49$ | $.17901$ |
| $2.4$ | $.47$ | $.49$ | $.1786$ | $.505$ | $.18154$ |
| $2.6$ | $.47$ | $.505$ | $.18122$ | $.52$ | $.18393$ |
| $2.8$ | $.50$ | $.52$ | $.18347$ | $.54$ | $.18689$ |
| $3.1$ | $.54$ | $.54$ | $.18616$ | $.57$ | $.19091$ |
| $3.3$ | direct | $.57$ | $.19179$ | $.76$ | $.21588$ |

The tails use

$$
d_{\rm push}\le .49973033201029,\qquad
 d_{\rm pull}\le .88282502240658.
\tag{113}
$$

The claimed baseline contacts concern their full color domains. The following
describes their reported certificate construction; it specifies acceptance
rules but does not supply an independent replay of the historical run.
For rational $0<p<1$, use the Gibbs supporting line

$$
H(x,y)\le -y\log_2p-(x-y)\log_2(1-p).
\tag{114}
$$

Both negative logarithms are enclosed outward on the $10^{-14}$ grid by
the rational logarithm procedure of Section I.4.1. Gibbs probabilities
are rational multiples of $10^{-12}$ clamped to
$[10^{-9},1-10^{-9}]$. Every such probability gives a valid supporting line. Near-stationary
proposals reduce subdivision; acceptance uses the rational bounds.

An outward-rounded implementation normalizes to $x\in[1,2]$, puts
$q=(x-1)/(x+1)$, and uses

$$
\ln x=2\sum_{j=0}^{31}\frac{q^{2j+1}}{2j+1}+\mathcal R,
\qquad0\le\mathcal R\le\frac{2q^{65}}{65(1-q^2)}.
\tag{115}
$$

Keep each lower and upper operation outward on the $2^{-120}$ grid,
including interval bounds on $q$ and its powers. The same formula at
$x=2$ encloses $\ln2$, and division gives rational bounds on $\log_2x$.
Expanding $H(x,y)=x\log_2x-y\log_2y-(x-y)\log_2(x-y)$ gives outward
entropy bounds, with the zero terms defined continuously.

For the first-level contacts use boxes $[m_0,m_1]\times[z_0,z_1]$,
starting from $[a,s]\times[a,\beta(s)]$ and tightening
$z_0\ge m_0$, $z_1\le\beta(m_1)$. Choose Gibbs lines at a feasible
center for the three positive inner entropies in
$(1-\tau)F_{\rm raw}+\tau G$. Their weighted sum is affine in $w$.
If its coefficient of $w$ is nonnegative, replace $w$ by either globally
valid affine upper bound $\beta-m$ or $C$; if it is negative, replace
it by one of $\beta-z,C-m,0$. Choose the tightest at the center, but
retain that same affine choice throughout the box. Each candidate
remains a valid one-sided inequality throughout the feasible region.

One rational proposal for the inner point uses 48 bisections on (38).
For $\tau=A/B$, the derivative sign is determined by the following
rational comparison:

$$
\left(\frac{(\beta-m-w)(C-w)}{w(m-C+w)}\right)^{B-A}
\left(\frac{C-w}{w-\beta+z}\right)^A.
\tag{116}
$$

Clear denominators before comparing integer powers; use the unique
endpoint when the interval is a singleton. This supplies the supporting-line parameters. In the branch $F=0$,
apply a Gibbs line directly to $G=H(C-\beta+z,w-\beta+z)$ and eliminate
$w$ with the same valid affine endpoints. Thus the two branches of
$\max(0,F_{\rm raw})$ are both covered.

The negative entropy $H(1-m,\beta-m)$ has a lower linear chord in $m$.
For $H(z,C-\beta+z)$, refine until
$z_0\ge(1-\gamma)\beta(m_1)$, so every box vertex lies in its entropy
domain. Its bilinear vertex interpolant is a lower bound by joint
concavity. After these replacements every branch is multiaffine in
$(m,z)$; maxima and nonnegative sums preserve separate convexity.
Its maximum on a rectangle therefore occurs at a vertex. Accept only
if all four rational vertex bounds are below the table contact;
otherwise bisect the larger of $3(m_1-m_0)$ and $z_1-z_0$, with the
first winning ties. This is the stated acceptance rule for the four first-level contacts.
The fixed push branch in the two-level families uses the same method
with $w_1\le C_1/2$, projected lower bound
$z\ge\max\{m,(1-\gamma_1/2)\beta\}$, and the additional globally
valid upper endpoint $w_1\le C_1/2$.

For the recursive branch set $v=w_1-C_1/2\ge0$ and
$C_2=\gamma_1\beta/2$. Its full domain is

$$
\max\{0,\beta-z-C_2,C_2-m\}\le v
 \le\min\{C_2,\beta-m-C_2\}.
\tag{117}
$$

Put $c=(1-\gamma_1/2)\rho-1>0$. Start from

$$
m\in\left[\max\left\{a,
\frac{(1-\gamma_1/2)a(\rho-1)}c\right\},s\right],\quad
z\in[a,\beta(s)],\quad
v\in[0,\min\{C_2(s),\beta(s)-s-C_2(s)\}].
$$

An empty range means that branch has no colors. On each box tighten

$$
\begin{aligned}
z_0&\leftarrow\max\{z_0,m_0,\beta(m_0)-C_2(m_0)-v_1\},\\
z_1&\leftarrow\min\{z_1,\beta(m_1)\},\\
v_0&\leftarrow\max\{v_0,0,\beta(m_0)-C_2(m_0)-z_1,C_2(m_1)-m_1\},\\
v_1&\leftarrow\min\{v_1,C_2(m_1),\beta(m_1)-m_1-C_2(m_1)\}.
\end{aligned}
\tag{118}
$$

All menu values have $\gamma_1\rho\le2$, which justifies these
monotone endpoint relaxations. Discard only empty boxes.

Choose Gibbs lines at a feasible center for the positive terms in
$\tau F_{2,\rm raw}+(1-\tau)G_2$. The weighted sum is affine in $w_2$.
Eliminate its coefficient using a valid affine upper endpoint $D_1$ or
$C_2$ when nonnegative, and a lower endpoint $Q_2,C_2-Q_1$, or $0$
when negative. A rational stationary-point proposal on (45) compares

$$
\left(\frac{(D_1-w_2)(C_2-w_2)}{w_2(Q_1-C_2+w_2)}\right)^A
\left(\frac{C_2-w_2}{w_2-Q_2}\right)^{B-A}
\gtreqless1
\tag{119}
$$

for $\tau=A/B$. In the $F_2=0$ branch, put $y=w_2-Q_2$;
then

$$
\max\{0,v-Q_1\}\le y\le\min\{v,w_1-Q_1\}.
$$

A Gibbs line for $H(v,y)$ and the appropriate signed affine endpoint
eliminate the last color.

Use a lower chord for $H(1-m,\beta-m)$, lower bilinear interpolants
for $H(z,D_1)$ and $H(C_2+v,v)$, and positive Gibbs lines for the
remaining entropies. Refine until
$z_0\ge(1-\gamma_1)\beta(m_1)$ to keep the first bilinear entropy
valid at every vertex. The second is always valid since $v\ge0$.
For the trace correction put

$$
\begin{aligned}
D_{\min}&=(1-\gamma_1/2)\beta(m_0)-m_0-v_1,\\
D_{\max}&=(1-\gamma_1/2)\beta(m_1)-m_1-v_0,\\
(d-q)_{\min}&=m_0-a-C_2(m_0)+v_0,\\
(m-q)_{\min}&=m_0-C_2(m_0)+v_0,\\
(w-r)_{\min}&=C_2(m_0)+v_0-s+m_0,\quad
r_{\max}=s-m_0,\quad d_{\min}=m_0-a.
\end{aligned}
\tag{120}
$$

Verify $\beta(m_0)\ge s$, nonnegativity of the factors, and

$$
(d-q)_{\min}(w-r)_{\min}\ge r_{\max}D_{\max},
$$

$$
r_{\max}m_1D_{\max}\le
 d_{\min}(m-q)_{\min}(1-s-D_{\max}).
\tag{121}
$$

These imply (52) for every feasible color in the box. Only on such
boxes replace $F_1$ by
$\max\{0,F_{1,\rm raw}-\delta\}$ with (57); otherwise set
$\delta=0$. The subtraction stays inside the nonnegative maximum.

The resulting upper expression is separately convex in $(m,z,v)$:
each branch is multiaffine, and all outer sums and maxima have
nonnegative weights. Evaluate every one of its eight vertices with
rational arithmetic. Accept precisely when all are at most the table
contact; otherwise bisect the coordinate with largest value among
$3(m_1-m_0),z_1-z_0,2(v_1-v_0)$, with that tie order. Evaluate affine extensions on the relaxed-box vertices, with all
negative entropy evaluations in their valid domains.

The baseline manuscript reported the following accepted nonempty leaf counts.
These are historical report values; the refined checker does not reproduce
or certify this older parameter menu.

| $\rho$ | Left contact: push + recursive | Right contact: push + recursive |
|---:|---:|---:|
| $2$ | $51+12447$ | $51+10699$ |
| $2.2$ | $50+15549$ | $50+14356$ |
| $2.4$ | $44+19271$ | $45+18263$ |
| $2.6$ | $46+21263$ | $45+21561$ |
| $2.8$ | $45+19175$ | $46+19509$ |
| $3.1$ | $55+15764$ | $55+16098$ |

The reported counts total $204538$ accepted leaves in these twelve contacts,
with positive trace corrections on $183117$ recursive leaves. The reported
four first-level counts are $176,139,143,137$. For the two direct contacts start with $[a,s]\times[a,\beta(s)]$,
tighten $z_0\ge m_0,z_1\le\beta(m_1)$, and use center-selected Gibbs
lines for all positive terms in (24) and a lower chord for
$H(1-m,\beta-m)$. If $m_0>a$ and
$\rho(m_0-a)^2\ge b(z_1-a)$, subtract the constant
$(7/5)(s-m_1)\max(0,z_0-m_1)$ from the right degree; otherwise
subtract zero. Evaluate both branches of $L_\rho$ at all four
vertices, accepting only below the contact. Bisect by the same
$3(m_1-m_0)$ versus $z_1-z_0$ rule. The reported direct-contact counts are
$175$ and $183$ accepted leaves. Their full-domain inequalities remain the
explicit numerical premise of the background Theorem 1; these counts alone
do not independently establish that premise. Finite cover factors and
rounding are accounted for separately by $\zeta$.

### I.4.3. Whole-prefix compensation

Join each row's two contacts by its chord. On $[0,.24]$ use
$\tau d_{\rm push}$ and on $[.76,1]$ use
$(1-\tau)d_{\rm pull}$. Denote this piecewise upper profile by $f$;
at a boundary retain both one-sided values. Convexity of each fixed
family's colored profile proves its chord throughout the interval.

Put

$$
R=h(t),\quad Q=h(s)+H(s,a),\quad D_c=R-Q,
\qquad .38309469039628\le D_c\le .38309469039633,
$$

$$
K=\frac{875}{3042},\qquad C=\frac1{2K}=\frac{1521}{875},
\qquad S_*=\frac{903}{2500}=.3612.
\tag{122}
$$

For $u=f(\tau)$, $v=f(1-\tau)$ and
$\Delta=(2\tau-1)D_c+u-v$, the finite rational comparison gives

$$
u+v+K\Delta^2\le S_*\qquad(0\le\tau\le1).
\tag{123}
$$

Here is the full reduction to the finite comparison. All chord values
are in $[0,1/4]$, so $|\Delta|\le .384+.25=.634$. The two
partial derivatives with respect to $u,v$ are positive because
$2K\cdot .634<1$. Thus both upper chords may be substituted
independently. The common refinement of their partitions has endpoints

$$
0,.24,.40,.43,.45,.46,.475,.48,.49,.495,
.505,.51,.52,.525,.54,.55,.57,.60,.76,1.
\tag{124}
$$

On each of its nineteen intervals the expression is convex in $\tau$;
it is also convex in $D_c$. Check both interval endpoints at both
rational endpoints for $D_c$. Thus there are thirty-eight one-sided
profile comparisons, or seventy-six scalar rational inequalities.
Their maximum is exactly

$$
\frac{1977604546193914547926593460805407}
{5475600000000000000000000000000000}<.361167,
$$

with margin below $S_*$ equal to

$$
\frac{182173806085452073406539194593}
{5475600000000000000000000000000000}>.000033.
\tag{125}
$$

For the row-oriented core fraction $q$, let

$$
\Phi(q,\tau)=q[\tau R+(1-\tau)Q+u]
 +(1-q)[(1-\tau)R+\tau Q+v].
$$

Writing $x=q-1/2$ gives
$\Phi=(R+Q+u+v)/2+x\Delta$. Completing the square in (123)
therefore proves

$$
\Phi(q,\tau)\le v_*(q):=\frac{R+Q+S_*}{2}+C(q-1/2)^2.
\tag{126}
$$

Indeed the difference is at most
$-\Delta^2/(4C)+x\Delta-Cx^2\le0$.
Since $\ln2<7/10$, entropy curvature gives
$1-h(1/2+y)\ge(20/7)y^2$. Apply this with
$y=(1-2s)(q-1/2)$ and use $C=(20/7)(1-2s)^2$ to obtain

$$
v_*(q)\le\frac{R+Q+S_*}{2}+1-h\bigl(s+(1-2s)q\bigr).
\tag{127}
$$

The reflected orientation has the same entropy. Bounded core rounding
changes the logarithmic cost only by a bounded quantity in the good-layer
range used by the reduction. The compiler of Section I.2 consequently
gives uniform endpoint degree caps with

$$
\delta_U(q)=v_*(q)-[qR+(1-q)Q],\qquad
\delta_V(q)=v_*(q)-[qQ+(1-q)R],
$$

$$
\deg_U\le O(1)2^{[\delta_U(q)+\zeta]M},\qquad
\deg_V\le O(1)2^{[\delta_V(q)+\zeta]M},\qquad\zeta=10^{-6}.
\tag{128}
$$

These give the per-endpoint enumeration bounds for the exact circuits.


### I.4.4. Exact gain and complete reduction costs

Use the matching types of Section I.3, $S_*=903/2500$, the full compilation allowance $\zeta=10^{-6}$, and $d_0=1/50$. With the definitions there,

$$
g_*=-\frac12+\frac12h(s)+\frac12H(s,a)
+H(1-s,t-a)-\frac12h(t)-\frac12S_*-\zeta.
$$

The rational logarithm series in Section I.4.1 proves the safe bounds

$$
\begin{gathered}
g_*\ge g_L=\frac{2135335441677}{200000000000000},\qquad
D\le D_U=\frac{49809813343531}{10^{14}},\\
\alpha\le\alpha_U=\frac{138991595816454}{10^{14}},\qquad
\eta\le\eta_U=\frac{559334743723}{10^{14}}.
\end{gathered}
\tag{129}
$$

For example, outward intervals obtained from the same series are

$$
\begin{aligned}
.49991595816452&<h(s)<.49991595816453,\\
.00741117216645&<J<.00741117216646,\\
.49809813343529&<D<.49809813343530,\\
.00559334743721&<\eta<.00559334743722.
\end{aligned}
\tag{130}
$$

Choose the rational balance

$$
\mu=\frac1{2(1+D_U+g_L)}
=\frac{100000000000000}{301754962128739}.
$$

Then

$$
\mu(1+D_U)=\frac12-\mu g_L
=E=\frac{149809813343531}{301754962128739}
<0.4964618056.
\tag{131}
$$

These rational upper bounds coincide. Their polynomially weighted sum has the same exponent. Also $3\mu<1$ and $g_L<d_0$, so the dictionaries fit and the high-deficiency branch is strictly cheaper.

The following rates substitute the rational bounds (129) into (112). Decimal entries are rounded upward.

| Operation | Upper rate per input coordinate |
|---|---:|
| Retained incidences and witness recovery | $E$ |
| Canonical output and complete residue-cover state | $E$ |
| All candidate-modulus energy evaluations | $.471671478$ |
| Selector and shared witness preprocessing | $.339876217$ |
| Repeated prefix lookups | $.348357717$ |
| Repeated outside lookups | $.344637748$ |
| Direct cyclic convolution and common shifts | $.338615680$ |
| High-deficiency dictionary matching | $.493372106$ |
| Dictionary and canonical-layer preparation | $.331394717$ |

Each auxiliary rate is strictly smaller than $E$ by exact rational comparison. The bound $h(1/5)<.74<1-d_0$ places every nonempty good layer in $(1/5,4/5)$ for sufficiently large $M$, as required by the core construction. The ledger includes local repetitions, modulus candidates, residue states, trie preprocessing, and witness recovery, with polynomial bit factors for all arithmetic.

## I.5. Proof of Theorem 1

Sections I.2 and I.4 give exact typed circuits and common adjacency
enumerators with total allowance $\zeta=10^{-6}$. Their terminating
input-independent compilation contributes $C$.

For an arbitrary integer instance, construct the dictionaries of Section
I.3. If $N^{50}\le2^{49M}$, use two-dictionary matching. Otherwise the
canonical layers, typed selector, energy oracle, and harmonic covers
serve every prefix, preserving actual representations at every outside
residue. The balanced outside lists retain equal-sum witnesses.

Form original integer keys after undoing label flips, keeping round and
residue-occurrence tags distinct. The signed circuit gives the
nonnegative count of compatible equal-key pairs. A positive count yields
a binary witness by bisection; if all counts vanish, completeness gives
NO. This applies to signed weights, repetitions, zeros, and coincidences.

The ledger and (131) bound input-dependent work by
$\operatorname{poly}(n,L)2^{En}$. Rounding and the boundary change only
constant factors; the finite small-input range is handled exhaustively
with a fixed polynomial coefficient. Adding $C$ proves the theorem. $\square$


# Part II. Trace refinement and improved parameter setting

This part applies the exact circuit compiler and reduction proved in Part I
to a stronger pooled-trace bound and a new rational parameter setting.
Its numerical requirements are discharged by the reconstructed
continuous-domain and scalar certificates described in Sections 4 and 9.
Source revisions and attribution are recorded in the [source map](sources.md).

## 1. Theorem and dependencies

The background conditional composition in Theorem 1 has exponent

$$
E_{\rm old}=\frac{149809813343531}{301754962128739}
 =.496461805587\ldots.
$$

The change below gives

$$
\boxed{E_{\rm new}=
 \frac{158153814247997}{318927986919134}
 =.4958919277538907\ldots < .495892.}
 \tag{XSS1}
$$

The exponent decreases by approximately `.0005698778` per input coordinate.
This result applies to arbitrary signed binary integers, with no promise
on density, multiplicities, target, or the existence of a solution.

**Theorem F, restated.** There is a uniform deterministic algorithm deciding Subset
Sum on `n` indexed signed binary integers of total encoding length `L`, and
returning an indexed witness on YES instances, using

$$
C_{\rm new}+\operatorname{poly}(n,L)2^{E_{\rm new}n}
 \tag{XSS2}
$$

bit operations. The startup cost `C_new` is finite and independent of the
input. All polynomial degrees are fixed. This is a time theorem; it makes
no simultaneous claim for the separate low-space algorithm.

The new argument changes three concrete ingredients: the pooled-trace
upper bound, the rational matching types used inside the reduction, and
the finite menu of recursive lookup widths. It then recomputes the entire
profile and every outer cost line. The exact signed identities, fixed-seed
compiler, canonical selection, energy evaluation, residue covers, exact
integer keys, and witness lifting are proved in Part I. The argument below
applies those constructions with the parameter changes justified in Section 6
and recomputes their cost in Section 7. It uses the new contact certificate
directly and does not assume the older numerical menu in Section I.4.2.

## 2. New types and the exact circuit families

Set

$$
s=\frac7{50}=.14,\quad t=\frac9{20}=.45,\quad
 a=\frac{13}{200}=.065,\quad b=\frac3{40}=.075,
 \qquad a+b=s.
 \tag{XSS3}
$$

Write `H(c,x)=c log_2 c-x log_2 x-(c-x)log_2(c-x)`, with its continuous
endpoint values. The outer color domain is

$$
a\le m\le s,\qquad \beta=a+\rho(m-a),\qquad m\le z\le\beta,
$$

$$
L_0=\max\{0,H(t,z)+H(1-t,\beta-z)-H(1-m,\beta-m)\}.
 \tag{XSS4}
$$

Use the following fixed recursive parameter pairs:

$$
(\rho,\gamma_1)\in
 \{(1.3,.47),(1.7,.47),(2.2,.50),(2.6,.54),
   (2.8,.58),(3,.60),(3.4,.62),(4,.65)\}.
 \tag{XSS5}
$$

All decimals in the mathematical specification are exact rationals.
For every family, `beta<=.365<t<1-t`. Its first inner lookup is
`c=gamma_1 beta`. The required containment condition `beta-z<=c`
holds on the full color domain: at the worst point `z=m=s`, the pairs
`(beta-s,c)` are respectively

$$
(.0225,.076375),\ (.0525,.090475),\ (.09,.115),\ (.12,.1404),
$$

$$
(.135,.1595),\ (.15,.174),\ (.18,.1984),\ (.225,.23725).
$$

The first inner color and occurrence exponent are

$$
Q_1=\beta-z,\quad D_1=c-Q_1,\qquad
 \max\{Q_1,c-m\}\le w_1\le\min\{\beta-m,c\},
$$

$$
F_{1,\rm raw}=H(\beta-m,w_1)+H(m,c-w_1)-H(z,D_1).
 \tag{XSS6}
$$

Keep the exact second-level routing

$$
Q_2=c-w_1,\qquad C_2=\max\{c/2,Q_2\},\qquad D_2=C_2-Q_2.
 \tag{XSS7}
$$

On the push branch `w_1<=c/2`, use the old valid profile upper bound

$$
P_{\rm push}=\tau L_0+(1-\tau)H(b,m-a)
 +(1-\tau)\max\{0,F_{1,\rm raw}\}
 +\tau H(D_1,w_1-Q_1).
 \tag{XSS8}
$$

On the recursive branch, write `v=w_1-c/2>=0`, so `C_2=c/2` and
`D_2=v`. The complete domain is

$$
\max\{0,\beta-z-c/2,c/2-m\}\le v
 \le\min\{c/2,\beta-m-c/2\},
$$

$$
\max\{Q_2,C_2-Q_1\}\le w_2\le\min\{D_1,C_2\}.
 \tag{XSS9}
$$

Put

$$
F_2=\max\{0,H(D_1,w_2)+H(Q_1,C_2-w_2)-H(w_1,D_2)\},
$$

$$
G_2=H(D_2,w_2-Q_2).
 \tag{XSS10}
$$

The new profile replaces the old first-level right contribution by the
trace bound proved next. The finite signed matrix is still the same exact
aggregated circuit from baseline (47); no positive cover substitutes for
a signed identity.

Also retain the ordinary direct signed lookup family `rho=4`. Its profile
is bounded by

$$
P_{\rm dir}=\tau L_0+(1-\tau)
 \{H(b,m-a)+H(\beta-m,z-m)-\delta_{\rm dir}\}.
 \tag{XSS11}
$$

On a rectangle where `m_0>a` and
`rho(m_0-a)^2>=b(z_1-a)`, use
`delta_dir=(7/5)(s-m_1) max(0,z_0-m_1)`; otherwise use zero.
This is the existing direct distinct-gate bound, applied at the new types.

## 3. The new pooled-trace lemma

Fix one outer and first-inner occurrence and write

$$
d=m-a,\quad r=s-m,\quad q=c-w_1,\quad D=\beta-m-w_1,
 \qquad B=H(b,d).
$$

The first-inner domain gives `0<=q<=m` and `D>=0`. When `beta>=s`, define

$$
A(g)=H(b,g)+H(s-g,q)+H(\beta-s,w_1-g)-H(z,D_1),
$$

$$
J(u)=H(b,d+u)+H(m+u,q)+H(1-s,D-u)
       +H(1-m-D,w_1)-H(1-m,w_1+D)-H(z,D_1).
 \tag{XSS12}
$$

Both functions are concave in their scalar argument. Their intervals are

$$
I_g=[\max\{0,w_1-(\beta-s)\},\min\{r,w_1\}],\qquad
 I_u=[0,\min\{r,D\}].
 \tag{XSS13}
$$

All entropy arguments are feasible. In particular, for this menu
`D<=beta<=.365<1-s=.86`. Put `A_*=max_{I_g}A` and `J_*=max_{I_u}J`.
Then the same exact aggregated circuit has a right-degree upper exponent

$$
R^{\rm trace}\le G_2+B_{\rm tr},
$$

$$
\boxed{B_{\rm tr}=
 \min\left\{B+\max\{0,F_{1,\rm raw}\},
             \max\{B,A_*,J_*\}\right\}.}
 \tag{XSS14}
$$

When `beta<s`, define `B_tr=B+max(0,F_{1,raw})`. Thus on every recursive
color the complete profile is bounded by

$$
P_{\rm rec}=\tau L_0+(1-\tau)B_{\rm tr}
              +\tau F_2+(1-\tau)G_2.
 \tag{XSS15}
$$

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

For the $C_1$ branch, fix the outer universe $B$ of size $\beta N$ and
its prescribed-one set $Y_1$ of size $aN$. Since $\beta\ge s$, choose nested
prescribed-zero sets $Z_j\subseteq Z_b\subseteq B\setminus Y_1$ of sizes $jN$ and $bN$.
A counted pair $(C,K)$ has $C\cap Y_1\subseteq K\subseteq C\cap(Y_1\cup Z_j)$,
$|K|=qN$, and a completion $U=Y_1\cup V$ with $V\subseteq Z_j$, $|V|=dN$,
and $U\cap C=K$. Enlarging $Z_j$ to $Z_b$ leaves $C,K,U$ unchanged, so
this is an injection into the union of the feasible histograms at $j=b$.
The restriction that $B$ owns $U$ was already relaxed in the histogram
upper bound; the injection need not preserve an ownership assignment.
The target union has only polynomially many values of the new zero
intersection count. Its largest entropy exponent therefore bounds the
original one, while the denominator $H(z,D_1)$ remains unchanged.
With $k=q-e$ and $g=f-k$, the exponent at $j=b$ is

$$
H(a,q-k)+H(b,k)+H(b-k,g)+H(\beta-s,w_1-g)-H(z,D_1).
$$

The entropy chain identity and Vandermonde give

$$
H(b,k)+H(b-k,g)=H(b,g)+H(b-g,k),
$$

$$
H(a,q-k)+H(b-g,k)\le H(s-g,q).
$$

Completion implies `0<=g<=r`, and the remaining entropy domains give
`I_g`. Thus this branch is at most `A_*`. The change from the earlier
argument is to sum over `k` before maximizing over `g`.

For the `C_0+C_1` branch set

$$
u=j-f-(d-k),\qquad j=d+u+g.
$$

Feasibility gives `0<=u<=min(r,D)`. The numerator exponent rewrites as

$$
H(b,d+u)+H(d+u,k)+H(a,q-k)
 +H(r-u,g)+H(1-s,D-u)+H(1-s-D+u,w_1-g).
$$

The two negative terms are `H(1-m,w_1+D)` and `H(z,D_1)`.
Vandermonde in `k` gives `H(m+u,q)`; independently, Vandermonde in `g`
gives `H(1-m-D,w_1)`. The resulting expression is `J(u)`. Maximize over
`I_u`, and combine the three branches. Polynomially many histogram
choices do not change normalized exponents. Taking the minimum with the
old bound for the same circuit proves (XSS14).

### A useful closed corollary

If, in addition, `0<=q<=d`, `w_1>=r`, and

$$
d(m-q)(w_1-r)\ge rmD,
 \tag{XSS16}
$$

then the same closed correction as before is valid:

$$
B_{\rm tr}\le B+\max\{0,F_{1,\rm raw}-\Delta\},\qquad
 \Delta=H(1-m,D)-H(1-s,D).
 \tag{XSS17}
$$

Indeed, for `rD>0`,

$$
A'(r)=\log_2\frac{d(m-q)(w_1-r)}{rmD}\ge0,
$$

so concavity gives `A_*=A(r)`. Also

$$
J'(0)=\log_2\frac{rmD}{d(m-q)(1-s-D)}\le0,
$$

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

$$
H(x,y)\le-y\log_2p-(x-y)\log_2(1-p).
 \tag{XSS18}
$$

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

$$
\delta=\frac75\frac{(s-m_1)D_{\min}}{1-m_0}
$$

inside the nonnegative maximum. Maximize each alternative bound over the
entire box's vertex set before taking the smaller resulting number. A
pointwise minimum of separately convex bounds need not be separately convex,
so taking a minimum independently at the vertices would not justify acceptance.
The push and direct branches use the analogous two-coordinate calculation.

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

$$
\min\{m_0-c(m_0)/2,m_1-c(m_1)/2\}+v_0.
 \tag{XSS19}
$$

This removes the old auxiliary restriction `gamma_1 rho<=2`; the exact
circuit construction itself never required that restriction.

Rational Gibbs probabilities can be proposed by approximate stationary
points, rounded to multiples of `10^{-12}` and clamped to
`[10^{-9},1-10^{-9}]`. Acceptance uses only exact rational comparisons
with outward logarithm enclosures. Normalize a positive rational into
`[1,2]`, put `z=(x-1)/(x+1)`, and use

$$
\ln x=2\sum_{j=0}^{31}\frac{z^{2j+1}}{2j+1}+\mathcal R,
 \qquad 0\le\mathcal R<2^{-100}.
 \tag{XSS20}
$$

The tail follows from `z<=1/3`. Products and divisions are rounded outward
on the `2^{-128}` grid. Divide by an independently enclosed `ln 2` and
round base-two logarithms outward to multiples of `10^{-14}`. Approximate
optimization chooses useful rational planes; it does not accept boxes.

The contact subdivisions are finite computations performed before the
input algorithm. Their scalar variables do not add an input-dependent
enumeration or optimization step.

The executable [continuous-domain checker](../../tools/verify_subset_sum_contacts.py)
completed all 42 push/recursive calculations and both direct calculations
with exact rational acceptance. Its [full-run receipt](verify/receipt.json)
records 188,227 accepted leaves, 376,414 subdivision nodes, two empty
recursive domains, and maximum depth 29. The accepted leaf counts are
given below in the same contact order as the preceding table. Each pair
is `(push leaves, recursive leaves)`; zero means an empty recursive domain.

| Family | Accepted leaf counts by contact |
|---|---|
| `(1.3,.47)` | `(177,0)`, `(25,0)` |
| `(1.7,.47)` | `(123,119)`, `(120,210)` |
| `(2.2,.50)` | `(80,17319)`, `(80,14139)` |
| `(2.6,.54)` | `(56,15591)`, `(59,13576)` |
| `(2.8,.58)` | `(52,11670)`, `(52,10663)` |
| `(3,.60)` | `(48,10249)`, `(48,9932)`, `(49,9562)`, `(49,9402)` |
| `(3.4,.62)` | `(48,9331)`, `(49,9163)`, `(49,9386)`, `(49,9580)` |
| `(4,.65)` | `(47,8278)`, `(53,8872)`, `(60,9427)` |
| Direct `rho=4` | `161`, `224` |

The smallest exact acceptance margin over all nonempty leaves is

$$
\frac{136285389119}{128000000000000000000}>10^{-9}.
$$

The receipt binds the complete contact menu to the checker's exact source
bytes. It is a record of the completed calculation; rerunning `--all`
reconstructs the entire continuous-domain proof. Approximate optimization
only proposes rational planes and never accepts or discards a box. The
[verification note](verify/README.md) proves the coverage and acceptance rules.

## 5. The whole reflected profile

Add the two exact endpoint circuits, valid for every `tau`:

$$
f_{\rm push}(\tau)=.58414212731239\,\tau,\qquad
 f_{\rm pull}(\tau)=.85319345691908\,(1-\tau).
 \tag{XSS21}
$$

The constants enclose `H(t,a)+H(1-t,b)` and `H(1-s,t-a)`, respectively.
Let `f` be the minimum of these lines and all eligible consecutive
contact chords from Section 4. A chord is eligible only inside its
certified interval. Retain both one-sided values at discontinuities.

Set

$$
D_c=h(t)-h(s)-H(s,a),\qquad
 .26905132960667\le D_c\le .26905132960673,
 \quad K=\frac{875}{2592},
$$

$$
U=f(\tau),\quad V=f(1-\tau),\qquad
 \Theta=(2\tau-1)D_c+U-V.
$$

Then the complete scalar inequality is

$$
\boxed{U+V+K\Theta^2\le S,\qquad S=.41113.}
 \tag{XSS22}
$$

All selected values are below `1/4`, so `|Theta|<.52` and the left side
is increasing in each of `U,V`. It is convex in `tau` on every common
affine refinement interval and is convex in `D_c`. The breakpoints of `f`
are exactly

$$
\left\{0,\frac{2425000000000}{9700570910413},\frac25,
 \frac{43}{100},\frac{3759}{8300},\frac{47}{100},\frac{12}{25},
 \frac{49}{100},\frac12,\frac{291}{580},\frac{51}{100},
 \frac{27}{50},\frac{11}{20},\frac35,\frac{5709}{9355},
 \frac{16693148922977}{22715773922977},1\right\}.
 \tag{XSS23}
$$

Adjoin their reflections and check the interval endpoints, both applicable
one-sided values, and both endpoints of the interval for `D_c`. The executable scalar certificate constructs the full common refinement and
checks 104 rational endpoint comparisons, retaining both one-sided values at
junctions. Their maximum is

$$
\frac{7169585626176460495449293952290503}
 {17438976000000000000000000000000000}
 =.4111242326485489\ldots < .41113,
 \tag{XSS24}
$$

attained at `tau=291/580` and its reflection `289/580`. The rational
margin is

$$
\frac{100576703539504550706047709497}
 {17438976000000000000000000000000000}>5.7\cdot10^{-6}.
$$

The numerical values of `S` for different matching types are not directly
comparable. The running-time comparison uses the rebalanced reduction
below, with all type-dependent entropy terms recomputed.

## 6. Unequal cores, rational types, and the finite compiler

Put `R=h(t)`, `Q=h(s)+H(s,a)`. For a fraction `lambda` of row-oriented
core coordinates, the endpoint objective is

$$
\Phi(\lambda,\tau)=
 \lambda[\tau R+(1-\tau)Q+U]
 +(1-\lambda)[(1-\tau)R+\tau Q+V].
$$

Completing the square using (XSS22) gives

$$
\Phi(\lambda,\tau)\le\frac{R+Q+S}{2}
 +\frac{1296}{875}(\lambda-1/2)^2.
 \tag{XSS25}
$$

The entropy curvature bound is valid for these types:

$$
\frac{1296}{875}(\lambda-1/2)^2
 =\frac{20}{7}(1-2s)^2(\lambda-1/2)^2
 \le1-h\bigl(s+(1-2s)\lambda\bigr).
 \tag{XSS26}
$$

This follows from `1-h(1/2+x)>=2x^2/ln 2>20x^2/7` on the whole binary
entropy domain. Thus the complete mixed-core profile hypothesis holds.

The new rational types require a divisibility change. Use `H_0=1000`,
take a sufficiently large fixed `k` divisible by `1000`, and use
microblocks of length

$$
N_0=k^2+1000k.
$$

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

$$
u=t-a+b=.46,\qquad
 D_{\rm can}=H(1-u,a)+H(u,b),
$$

$$
\eta=1-h(u),\quad \alpha=1+h(s)-s,\quad
 J=1-H(s,a)-H(1-s,t-a).
 \tag{XSS27}
$$

The canonical support bound, expectation identity, and `K/T` ratio are
the same binomial/entropy identities at these new rational arguments.
In particular,

$$
h(u)+D_{\rm can}=1+h(s)-J.
$$

The gain is recomputed from its full formula:

$$
g_*=-\frac12+\frac12h(s)+\frac12H(s,a)+H(1-s,t-a)
       -\frac12h(t)-\frac12S-\zeta.
 \tag{XSS28}
$$

Outward rational entropy evaluation as in (XSS20) proves

$$
\begin{aligned}
 D_{\rm can}&\le D_U=\frac{58153814247997}{10^{14}},\\
 \alpha&\le\alpha_U=\frac{144423881164287}{10^{14}},\\
 \eta&\le\eta_U=\frac{231078058989}{5\cdot10^{13}},\\
 g_*&\ge g_L=\frac{131017921157}{10^{13}}.
 \end{aligned}
 \tag{XSS29}
$$

Keep the dictionary-deficiency threshold `d_0=1/50`. Choose

$$
\mu=\frac1{2(1+D_U+g_L)}
 =\frac{50000000000000}{159463993459567},
$$

$$
M=1000\left\lfloor\frac{\mu n}{1000}\right\rfloor.
 \tag{XSS30}
$$

Then `3mu<1`, so the three dictionaries fit, and `g_L<d_0`. The two
binding input-dependent rates are exactly

$$
\mu(1+D_U)=\frac12-\mu g_L
 =\frac{158153814247997}{318927986919134}=E_{\rm new}.
 \tag{XSS31}
$$

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

$$
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
$$

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


## 9. Reproducible numerical certificates

[`verify_subset_sum_contacts.py`](../../tools/verify_subset_sum_contacts.py)
reconstructs the complete contact proof of Section 4. Run it with `--all`
to repeat all 44 branch calculations; `--jobs` only controls parallelism.
Every domain tightening and accepted vertex bound uses exact rational
arithmetic. The [receipt](verify/receipt.json) records the complete menu,
the accepted bounds and margins, and the source-code and menu fingerprints.
Receipt binding can be checked separately, without confusing that inexpensive
provenance check with a full recomputation.

[`verify_subset_sum_scalars.py`](../../tools/verify_subset_sum_scalars.py)
reconstructs the contact-chord lower envelope, proves its entropy enclosures
with rational logarithm series, checks all 104 one-sided reflected-profile
comparisons, and checks every operation in the outer ledger. It reproduces
the exact maximum (XSS24) and exponent (XSS31) without floating-point
acceptance. These two programs discharge the numerical requirements of
Theorem F. The circuit compiler, reduction, and witness recovery remain
the mathematical proofs given in this manuscript. The
[verification note](verify/README.md) gives the complete commands and
the separate scope of the finite energy-tensor check.

## References

1. Ellis Horowitz and Sartaj Sahni. Computing Partitions with Applications to the Knapsack Problem. *Journal of the ACM* 21(2):277–292, 1974. [doi:10.1145/321812.321823](https://doi.org/10.1145/321812.321823).
2. Tim Randolph and Karol Węgrzycki. Beating Meet-in-the-Middle for Subset Balancing Problems. *Proceedings of the 58th Annual ACM Symposium on Theory of Computing*, pp. 1314–1325. ACM, 2026. [doi:10.1145/3798129.3800841](https://doi.org/10.1145/3798129.3800841).
3. Josh Alman and Baitian Li. Kronecker Powers, Orthogonal Vectors, and the Asymptotic Spectrum. *arXiv:2509.14489v1*, 17 September 2025. [doi:10.48550/arXiv.2509.14489](https://arxiv.org/abs/2509.14489v1).
4. Lixi Ye and Baitian Li. Subset Sum via Partial Match. *arXiv:2610.10446v1*, 7 October 2026. [doi:10.48550/arXiv.2610.10446](https://arxiv.org/abs/2610.10446v1).
5. Swapnil Jain. Deterministic Subset Sum below meet-in-the-middle. Public GitHub preprint, commit `1daaf519f567dd7a65a00692b08b4ff54b252d24`, 11 October 2026. Theorem 5b-F in `proofs/stage5b.md`. [Versioned source](https://github.com/Swapnil-jain/subsetsum-derand/tree/1daaf519f567dd7a65a00692b08b4ff54b252d24).
6. OpenAI. Subset Sum in Time $O(2^{0.49n})$. *OpenAI Math Release preprint*, 4 October 2026. Repository commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`. [Versioned source](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026).

7. OpenAI. A Low-Space Algorithm for Worst-Case Subset Sum. *OpenAI Math Release preprint*, 26 September 2026; accessed 23 October 2026. [Source](https://github.com/openai/math/tree/main/preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026).
8. Richard Schroeppel and Adi Shamir. A $T=O(2^{n/2})$, $S=O(2^{n/4})$ Algorithm for Certain NP-Complete Problems. *SIAM Journal on Computing* 10(3):456–464, 1981. [doi:10.1137/0210033](https://doi.org/10.1137/0210033).
9. Ce Jin, Jaewoo Park, Barna Saha, and Yinzhan Xu. Deterministic Monotone Min-Plus Product and Convolution. *ICALP 2026*, LIPIcs 374, 119:1–119:23, 2026. [doi:10.4230/LIPIcs.ICALP.2026.119](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.119).
10. Mokshay Madiman, Adam W. Marcus, and Prasad Tetali. Entropy and Set Cardinality Inequalities for Partition-Determined Functions. *Random Structures & Algorithms* 40(4):399–424, 2012. [doi:10.1002/rsa.20385](https://doi.org/10.1002/rsa.20385).
