# A deterministic Subset Sum bound

**Author:** Yilin Liu

**Abstract.** We give two uniform deterministic algorithms for Subset Sum on arbitrary signed binary integers. The first runs in $C+\operatorname{poly}(n,L)2^{En}$ bit operations, where $E<0.4964618056$ and $C$ is a finite input-independent startup cost. It uses recursive signed matching circuits, pooled trace coefficients, balancing over unequal cores, and an implicit canonical collision-energy oracle. The second runs in $\operatorname{poly}(n,L)2^{n/2}$ bit operations and uses $\operatorname{poly}(n,L)2^{E_Sn}$ writable bits, where $E_S<0.1826163578$. It uses nonlinear support extraction, canonical-distance ownership, support-dependent signings, and independently ordered parent streams. Both decide every instance exactly and return an indexed witness on YES instances.

## 1. Statement and notation

An instance consists of integers $z_1,\ldots,z_n,\tau$ with total binary encoding length $L$. A witness is a binary vector $c$ satisfying $\sum_i c_i z_i=\tau$. Time counts bit operations and space counts writable bits. Polynomial factors have fixed degrees and constants depending only on the numerical parameters. Logarithms have base two except where $\ln$ is written. We use the binary entropy function:

$$
h(t)=-t\log_2t-(1-t)\log_2(1-t),\qquad h(0)=h(1)=0.
$$

**Theorem 1.** There is a uniform deterministic algorithm which either returns a Subset Sum witness or correctly reports that none exists, and whose bit running time is bounded by

$$
C+\operatorname{poly}(n,L)\,2^{En},\qquad
E=\frac{149809813343531}{301754962128739}<0.4964618056.
$$

The constant $C$ is the finite cost of constructing the fixed circuit data. The stated input-dependent term includes construction of the residue covers.

**Theorem 2.** There is a uniform deterministic algorithm which either returns a Subset Sum witness or correctly reports that none exists, and whose bit running time and writable-bit space are bounded by

$$
\begin{gathered}
\operatorname{poly}(n,L)2^{n/2}\quad\text{bit operations},\qquad
\operatorname{poly}(n,L)2^{E_Sn}\quad\text{writable bits},\\
E_S=\frac{18261635770550353}{10^{17}}<0.1826163578.
\end{gathered}
$$

Part I proves Theorem 1 by exact matching circuits and a deterministic representation reduction. Part II proves Theorem 2 by support extraction and bounded-storage generation. The two algorithms share the notation and arithmetic of Sections 1–2. The circuit parameters appear in Section I.4; the low-space resource certificate is in Section II.8.

The proof uses elementary real calculus, finite probability, unique factorization, and exact integer and rational arithmetic. Concentration, entropy, prime-density, grouping, and circuit-rebalancing bounds are derived below.

### 1.1. Relation to prior work

Horowitz and Sahni's meet-in-the-middle algorithm solves Subset Sum in $2^{n/2}\operatorname{poly}(n,L)$ time [1]. Representation techniques for subset balancing were developed by Randolph and Węgrzycki [2]. The depth-two circuit framework of Alman and Li [3] and the partial-match construction of Ye and Li [4] provide the circuit methods used here.

Jain [5, Theorem 5b-F] gives deterministic time $\operatorname{poly}(n,L)2^{(0.4986298176+\epsilon)n}$ for each fixed positive $\epsilon$ in the common regime $L=2^{o(n)}$. Theorem 1 improves the exponent within that representation-and-circuit framework. Recursive containment and exact trace aggregation strengthen the matching profile; balancing, canonical covering, and implicit energy evaluation complete the deterministic reduction.

Schroeppel and Shamir [8] achieve half-exponential time with quarter-exponential space. OpenAI [7] gives a randomized algorithm at the same time exponent using $\operatorname{poly}(n+b)2^{.199n}$ words, hence ordinary $O(2^{.2n})$ word space under every fixed polynomial-bit convention. Here $b$ is the maximum input-integer bit length. Theorem 2 gives deterministic bit space with exponent $E_S<0.1826163578$ and polynomial factors in the full encoding length. Starting from the representation layout, modular streams, and separator entropy calculation of [7], Part II develops strict support extraction, deterministic covers, and interval processing. Fractional set-cardinality inequalities provide related context for proportional support extraction [10].

For randomized time bounds, Ye and Li [4] use partial matching, and OpenAI [6] gives $O(2^{.49n})$ word-RAM time for polynomial-bit inputs. The deterministic comparisons above use the stated bit-operation and input-length models.

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

This part proves Theorem 1.

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

The finite profile inequality proved in Section I.4 gives

$$
qf(\tau)+(1-q)f(1-\tau)
\le\tau\delta_U(q)+(1-\tau)\delta_V(q)
\qquad(0\le q,\tau\le1).
\tag{64}
$$

**Theorem I.2.2.** Fix a positive rational allowance $\eta$. One terminating deterministic preprocessing program supplies common exact integer adjacency enumerators for

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

## I.4. Finite rational certification

We certify the profile premise of Section I.2 and the costs of Section I.3. All terminating decimals denote exact rationals.

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

We certify the contacts over their full color domains.
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
first winning ties. This certifies the four first-level contacts.
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

The accepted nonempty leaf counts are:

| $\rho$ | Left contact: push + recursive | Right contact: push + recursive |
|---:|---:|---:|
| $2$ | $51+12447$ | $51+10699$ |
| $2.2$ | $50+15549$ | $50+14356$ |
| $2.4$ | $44+19271$ | $45+18263$ |
| $2.6$ | $46+21263$ | $45+21561$ |
| $2.8$ | $45+19175$ | $46+19509$ |
| $3.1$ | $55+15764$ | $55+16098$ |

There are $204538$ accepted leaves in these twelve contacts. Positive
trace corrections occur on $183117$ recursive leaves. The four
first-level counts are $176,139,143,137$. For the two direct contacts start with $[a,s]\times[a,\beta(s)]$,
tighten $z_0\ge m_0,z_1\le\beta(m_1)$, and use center-selected Gibbs
lines for all positive terms in (24) and a lower chord for
$H(1-m,\beta-m)$. If $m_0>a$ and
$\rho(m_0-a)^2\ge b(z_1-a)$, subtract the constant
$(7/5)(s-m_1)\max(0,z_0-m_1)$ from the right degree; otherwise
subtract zero. Evaluate both branches of $L_\rho$ at all four
vertices, accepting only below the contact. Bisect by the same
$3(m_1-m_0)$ versus $z_1-z_0$ rule. These direct contacts have
$175$ and $183$ accepted leaves. These are complete continuous-domain certificates;
finite cover factors and rounding are paid separately by $\zeta$.

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

# Part II. A deterministic low-space algorithm

This part proves Theorem 2. Write $O^*(f(n))$ for
$\operatorname{poly}(n,L)f(n)$, where $L$ is the full encoding length.
Masks refer to indexed coordinates. The weights are $w_1,\ldots,w_n$
and the target is $t$; parameters used below are local to this part.
The time and space bounds are

$$
\begin{gathered}
T=O^*(2^{n/2}),\qquad S=O^*(2^{E_Sn}),\\
E_S=\frac{18261635770550353}{10^{17}}<0.1826163578.
\end{gathered}
\tag{132}
$$

The construction starts from the representation layout, modular
streams and separators of [7]. Weighted canonical-distance ownership,
linear translate covers, biased top layers and bounded original-key
streams are combined below. We use $n=3m+O(1)$ with $8\mid m$;
bounded leftover coordinates are enumerated explicitly.

## II.1. Support counting and nonlinear core extraction

For a coordinate set $A$, let

$$
\Sigma(A)=\left\{\sum_{i\in D}w_i:D\subseteq A\right\},
\qquad N(A)=|\Sigma(A)|,\qquad d(A)=|A|-\log_2N(A).
\tag{133}
$$

All masks are indexed. Split $A$ into two nearly equal parts, sort their
raw subset-sum arrays, and heap-merge the rows of their pair sums in
increasing actual order. Counting each new value once computes $N(A)$
in $O^*(2^{|A|})$ time and $O^*(2^{|A|/2})$ space. The same stream fills
a distinct-value residue histogram with one additional modulus-length
array. Sums, comparisons, and counters have polynomial bit length in
$n,L$.

Choose the lexicographically least witness for every distinct sum of a
$q$-coordinate set, giving a family $\mathcal F$ of size $N$. Its
projection onto any coordinate set is sum-injective. If two projected
masks had the same sum, replacing the lexicographically larger one in
its full canonical witness would preserve the sum and decrease that
witness.

A cube family of size $N$ has at most $N\log_2N/2$ internal edges.
Induct on dimension: slices of sizes $a,b$ have at most
$(a\log_2a+b\log_2b)/2$ internal edges and at most $\min(a,b)$ crossing
edges. Concavity gives $h(p)\ge2\min(p,1-p)$, so the bound follows with
$p=a/(a+b)$. If $E_i$ counts edges in direction $i$, forgetting that
coordinate leaves exactly $N-E_i$ projected masks. Some deletion
therefore retains support at least $N(q+d_q)/(2q)$, and the maximum-support
deletion satisfies

$$
d_{q-1}\le d_q-\log_2(1+d_q/q).
\tag{134}
$$

The algorithm counts all one-coordinate deletions sequentially and takes
a largest support, with fixed tie breaking. The entire nested chain
costs $O^*(\sum_{q\le m}q2^{q-1})=O^*(2^m)$ time and
$O^*(2^{m/2})$ space. It retains polynomially many coordinate sets and
counts.

Since $\log_2(1+x)\ge x$ on $[0,1]$, deficiency density decreases along
the chain. If its initial density is at most $\kappa$, then
$\lambda=\log_2(1+\kappa)/\kappa$ gives
$d_{q-1}\le(1-\lambda/q)d_q$. For $q\ge2$ these factors are
nonnegative and at most $(1-1/q)^\lambda$. Thus

$$
d(C)\le(c/m)^\lambda d(B),\qquad |C|=c,\quad |B|=m.
\tag{135}
$$

The zero-deficiency and empty-core cases follow directly. We will also
use $\lambda=4/3$ when $\kappa\le1/6$, certified by $7^9>4\cdot6^9$.

The sharper certificate used in the resource policy is

$$
P_*=\frac{23}{26},\qquad
\Phi(\delta)=\frac{\delta^{52}}{(P_*-\delta)^{75}},
\qquad
\Psi(q,d)=\frac{d^{52}}{(P_*q-d)^{75}}.
\tag{136}
$$

For $\delta=d_q/q\le1/5$, put
$F(\delta)=\log_2(1+\delta)-\delta$ and
$R(\delta)=\delta(P_*-\delta)/(2+\delta)$.
The derivative of
$\ln(1+\delta)-2\delta/(2+\delta)$ is
$\delta^2/((1+\delta)(2+\delta)^2)\ge0$.
The positive atanh series gives
$\ln2<2/3+2/81+1/540=1123/1620<52/75$.
Consequently $F(\delta)\ge R(\delta)$, and
$R'(\delta)=(2P_*-4\delta-\delta^2)/(2+\delta)^2>0$ on $[0,1/5]$.
Writing $\delta'=d_{q-1}/(q-1)$, (134) gives
$\delta'\le\delta-R(\delta)/(q-1)$. Since
$(\ln\Phi)'=23/R$, integration yields

$$
\ln\Phi(\delta)-\ln\Phi(\delta')
\ge\frac{23(\delta-\delta')}{R(\delta)}
\ge\frac{23}{q-1}
\ge23\ln\frac q{q-1}.
\tag{137}
$$

A zero endpoint is immediate. Since
$\Phi(d/q)=q^{23}\Psi(q,d)$, multiplication along the chain proves
$\Psi(c,d(C))\le\Psi(m,d(B))$ exactly.

For an initial density upper bound $0<x\le1/5$ and retained fraction
$s\in(0,1]$, define $\beta(x,s)$ by

$$
\beta^{52}(P_*-x)^{75}=x^{52}(P_*s-\beta)^{75},
\quad 0<\beta\le sx.
\tag{138}
$$

The left-to-right ratio increases strictly with $\beta$, so the root is
unique. Equivalently,
$P_*s=xt+(P_*-x)t^{52/75}$ and $\beta=xt$.
The potential proves $d(C)\le m\beta(x,s)$.
At $x=0$ set $\beta=0$. Increasing $x$ enlarges the initial potential,
so $\beta$ is increasing in $x$; also $\beta(x,s)\le sx$.
Rational bisection of (138), with denominators cleared, supplies safe
$O(1/m)$ enclosures by fixed-power integer comparisons.
All requested sizes and deficiency proxies are selected before useful
layers. Exact support counts continue to define the actual histograms.

## II.2. Trace mass, support-dependent signings, and balanced cells

### II.2.1. An exact fixed-layer trace inequality

For integers $0\le k,r\le c$ and every $\mathcal F\subseteq\{0,1\}^c$ with $|\mathcal F|\ge2^k$,

$$
\sum_{|T|=r}|\pi_T\mathcal F|
\ge[z^r](1+2z)^k(1+z)^{c-k}
=\sum_j\binom kj\binom{c-k}{r-j}2^j.
\tag{139}
$$

We prove the rank comparison needed for this coefficient inequality.
For an integer interval $I$, let $W(I)$ be its multiset of binary
Hamming weights. Domination means that every upper-threshold count is
at least as large. We claim that, for $a\ge b\ge0$,

$$
W([a,a+b))\ \text{dominates}\ 1+W([0,b)).
\tag{140}
$$

The case $b=0$ is immediate. Use strong induction on $a+b$. A consequence available at smaller sums
is $W([u,u+v))$ dominating $W([0,v))$: apply (140) to
$\max(u,v),\min(u,v)$, weaken by removing the added one, then add and
cancel common prefix multisets in the threshold inequalities.
Let $H$ be the largest power of two at most $a$.
If $a+b\le2H$, remove the leading bit and apply this consequence to
$[a-H,a-H+b)$. If $a+b>2H$, put $D=2H=2^d$,
$u=D-a$, and $v=b-u>0$. Since $D-b\ge u$, the smaller instance
$(D-b,u)$ gives
$W([D-b,D-b+u))$ dominating $1+W([0,u))$.
Complementing the $d$ bits reverses domination and gives
$W([a,D))$ dominating $1+W([v,b))$.
The remaining interval has
$W([D,D+v))=1+W([0,v))$, proving (140).

If $B_j(N)$ counts integers below $N$ with Hamming weight at least $j$,
(140) says
$B_j(a)+B_{j-1}(b)\le B_j(a+b)$ for $a\ge b$.
Induction on dimension now shows that a downset $\mathcal D$ of size
$N$ has at most $B_j(N)$ members of rank at least $j$: its two slices
are downsets of sizes $N_0\ge N_1$, and the displayed inequality combines
their inductive bounds. Thus, for every nonnegative decreasing rank
weight $w$,

$$
\sum_{A\in\mathcal D}w(|A|)
\ge\sum_{j=0}^{N-1}w(\operatorname{wt}(j)).
\tag{141}
$$

This follows by expressing $w$ as a constant plus nonnegative multiples
of lower-rank threshold indicators.

Downward compression in a coordinate replaces sections
$\mathcal F_0,\mathcal F_1$ by their union and intersection.
It preserves cardinality and decreases every projection size:
projections omitting the coordinate are unchanged, while the sum of
the two projected section sizes bounds the corresponding union and
projected intersection. Compression preserves earlier downward closure,
so one pass through the coordinates yields a downset $\mathcal D$
with $|\pi_T\mathcal F|\ge|\pi_T\mathcal D|$ for every $T$.
For a downset,

$$
\sum_{|T|=r}|\pi_T\mathcal D|
=\sum_{A\in\mathcal D}\binom{c-|A|}{r-|A|}.
\tag{142}
$$

The rank weight on the right decreases, with consecutive ratio
$(r-j)/(c-j)$ until it becomes zero. When $|\mathcal D|=2^k$,
(141) compares it with the full $k$-cube and gives (139).
For a larger family, take any $2^k$ members first.

Apply (139) to the canonical full-support witnesses of a weighted
$c$-coordinate core. Their projections are sum-injective by Section II.1.
With $k=\lfloor\log_2N\rfloor$,

$$
S_r:=\sum_{|T|=r}N(T)
\ge[z^r](1+2z)^k(1+z)^{c-k}.
\tag{143}
$$

The right side is a polynomial-bit binomial sum. The canonical and
compressed families serve only in this proof.

### II.2.2. Finite trace-gain certificates

Let $N\ge2^{c-d}$, $\delta=d/c$, and
$r=\theta c+O(Q_{\rm grid})$, where $Q_{\rm grid}$ is a fixed multiple of four chosen before the input.
Retaining a binomial term in (143) gives

$$
\log_2S_r\ge c\max_\eta
\left\{(1-\delta)h\!\left(\frac{\theta-\eta\delta}{1-\delta}\right)
       +\delta h(\eta)+\theta-\eta\delta\right\}
-O(Q_{\rm grid}\log(c+1)).
\tag{144}
$$

The feasible $\eta$ make both entropy arguments valid. The finite
rectangles used below satisfy

$$
\log_2S_r\ge[h(\theta)+\theta]c-(\theta-g)d
              -O(Q_{\rm grid}\log(c+1)),
\tag{145}
$$

with $(\theta,\delta,g)$ in
$[.38,.46]\times[0,.2]\times\{1/16\}$,
$[.41,.46]\times[0,.05]\times\{3/40\}$, or
$[.44,.46]\times[0,.03]\times\{79/1000\}$.
Greedy extraction decreases deficiency density, so a rectangle chosen
from a full-block density upper bound also applies to its strict core.

Here is a complete rational certificate. For fixed rational $\eta$,
subtract $h(\theta)+\theta(1-\delta)$ from the expression in braces
in (144), calling the result $\Delta(\theta,\delta)$.
It is concave in $\delta$, with value zero at zero. For positive
$\delta$ it is also concave in $\theta$: writing
$z=(\theta-\eta\delta)/(1-\delta)$, its second derivative is
$(\ln2)^{-1}(1/(\theta(1-\theta))-1/((1-\delta)z(1-z)))<0$.
Indeed,
$\theta(1-\theta)=(1-\delta)z(1-z)+\delta\eta(1-\eta) +\delta(1-\delta)(z-\eta)^2$.
It therefore suffices to bound $\Delta/\delta$ at the two theta
endpoints and the upper density endpoint of each rectangle.

Define rational entropy enclosures by

$$
\begin{aligned}
\ell_-&=2\sum_{j=0}^{11}\frac1{(2j+1)3^{2j+1}},
&\ell_+&=\ell_-+\frac2{25\,3^{25}}\frac98,\\
S(z)&=\sum_{j=1}^{32}\frac{z^{2j}}{(2j)(2j-1)},
&R(z)&=\frac{z^{66}}{66\cdot65(1-z^2)},\\
h_-(p)&=1-\frac{S(|1-2p|)+R(|1-2p|)}{\ell_-},
&h_+(p)&=1-\frac{S(|1-2p|)}{\ell_+}.
\end{aligned}
\tag{146}
$$

The positive atanh series bounds $\ln2$ between $\ell_-,\ell_+$;
the positive entropy series and its geometric tail give
$h_-(p)\le h(p)\le h_+(p)$ at the interior arguments used here.
Substitution into

$$
G_-=
\frac{(1-\delta)h_-((\theta-\eta\delta)/(1-\delta))
             +\delta h_-(\eta)-h_+(\theta)}{\delta}
+\theta-\eta
\tag{147}
$$

gives the following strict rational lower comparisons:

| Theta interval | $\delta$ | $\eta$ | Left bound | Right bound |
|---|---:|---:|---:|---:|
| $[19/50,2/5]$ | $1/5$ | $13/50$ | $6253/10^5$ | $6309/10^5$ |
| $[2/5,43/100]$ | $1/5$ | $7/25$ | $6395/10^5$ | $6417/10^5$ |
| $[43/100,23/50]$ | $1/5$ | $3/10$ | $6597/10^5$ | $6439/10^5$ |
| $[41/100,43/100]$ | $1/20$ | $13/50$ | $7548/10^5$ | $7558/10^5$ |
| $[43/100,23/50]$ | $1/20$ | $7/25$ | $7714/10^5$ | $7676/10^5$ |
| $[11/25,23/50]$ | $3/100$ | $143/500$ | $3967/50000$ | $1593/20000$ |

Each entry is verified by (146)–(147) after clearing positive
denominators. The first three exceed $1/16$, the next two exceed $3/40$,
and the last exceeds $79/1000$. The two concavity reductions prove
(145) over all three rectangles, including zero density by continuity.

### II.2.3. Linear translate covers

Let $V=\mathbb F_2^c$, let $\varnothing\ne G\subseteq V$, and suppose membership in $G$ takes deterministic time $Q$ and workspace $W$. Write $N=2^c$ and $\alpha=|G|/N$. There is a deterministic algorithm returning a basis for a subspace $H\le V$ such that

$$
G+H=V,\qquad
K:=|H|\le\min\left\{2^c,\frac{2(1+c\ln2)}{\alpha}\right\}.
\tag{148}
$$

Its time is $O^*(2^cKQ)$ and its space is $O^*(W+\operatorname{poly}(c))$. A basis permits enumeration of all centers with polynomial delay and state. All arithmetic in the construction has polynomial bitlength.

Start with $H=\{0\}$ and let $U=V\setminus(G+H)$. Adding a vector $v$ to the basis replaces the uncovered set by $U\cap(U+v)$. The average translation intersection is

$$
\frac1N\sum_{v\in V}|U\cap(U+v)|=\frac{|U|^2}{N}.
\tag{149}
$$

Choose $v$ whose intersection size is no larger than this average. If $U\ne\varnothing$, then $0<|U|<N$. Such a choice strictly decreases $|U|$, and cannot lie in $H$, since $U$ is $H$-invariant. Consequently the subspace doubles at every successful step. After $d$ steps,

$$
|U_d|/N\le(1-\alpha)^{2^d}\le e^{-\alpha2^d}.
\tag{150}
$$

The first power of two at least $(1+c\ln2)/\alpha$ makes the integer $|U_d|$ smaller than one. Alternatively rank $c$ gives $H=V$. This proves (148). The algorithm stops by exact counting, without evaluating a real logarithm.

To choose $v$, fix its bits by conditional expectation. For a prefix length $j$, let $U_a$ be the number of uncovered vectors with prefix $a\in\mathbb F_2^j$. If $v$'s prefix is $P$, then

$$
\mathbb E[|U\cap(U+v)|\mid v|_{[j]}=P]
 =2^{-(c-j)}\sum_a U_aU_{a+P}.
\tag{151}
$$

For each uncovered $x$ with prefix $a$, its translated suffix is uniform in the suffix class with prefix $a+P$; this proves the formula. The two next-bit means average to the current mean. Choose the smaller, using their common-denominator integer numerators. The uncovered predicate remains unchanged until all bits of the new vector have been chosen.

Membership in $U$ is decided by enumerating the present $H$ and testing $x+h\notin G$ for every $h$. For one candidate prefix, enumerate each $a$, count $U_a$ and $U_{a+P}$ by scanning their suffix classes, multiply the two counts, then discard them. The suffix classes partition $V$, so this is at most two full passes, with time $O^*(N|H|Q)$ and space $W+\operatorname{poly}(c)$. The score has at most $2c+1$ bits. The $c$ bit choices add a polynomial factor. Across stages the current subspace sizes are $1,2,\ldots,K/2$, whose sum is less than $K$. Exact stopping tests, including a final full pass, obey the same bound. This proves the claimed time and space.

If $G$ lies in the cardinality layer $\binom{[c]}r$, test cardinality before the expensive predicate, whose time and state on this layer are $Q_r,W_r$. For each fixed $h$, exactly $\binom cr$ of the $N$ translated vectors in a full pass have cardinality $r$. The preceding proof therefore gives the sharper bound

$$
T=O^*\!\left(K\left[2^c+\binom cr Q_r\right]\right),
\qquad S=O^*(W_r+\operatorname{poly}(c)).
\tag{152}
$$

For a dyadic class defined by distinct subset-sum support, sorted half-sum streaming gives $Q_r=O^*(2^r)$, $W_r=O^*(2^{r/2})$. The cardinality test charges all failed masks; early successful membership tests only reduce the count.

### II.2.4. Support classes and signing costs

Partition the $r$-subsets into exact support classes
$\mathcal G_\ell=\{T:2^\ell\le N(T)<2^{\ell+1}\}$.
Count them by the support stream of Section II.1, and choose a nonempty
class maximizing $2^\ell g$, where $g=|\mathcal G_\ell|$.
There are at most $r+1$ classes, so $2^\ell g\ge S_r/(2(r+1))$.
Apply the linear translate cover to this class, and let $K$ be its
actual number of centers. Coverage gives $2^c\le Kg$, while the size
bound gives $Kg\le\operatorname{poly}(c)2^c$. Put
$\tau=1-h(\theta)$ and $\phi=\theta-\gamma$ for the applicable trace
gain $\gamma$. The resulting bounds are:

$$
\begin{aligned}
\ell-\log_2K&\ge(\theta-\tau)c-\phi d
                    -O(Q_{\rm grid}\log(c+1)),\\
\ell&\ge\theta c-\phi d-O(Q_{\rm grid}\log(c+1)),\\
\log_2K&\le\tau c+\phi d+O(Q_{\rm grid}\log(c+1)).
\end{aligned}
\tag{153}
$$

For the first line, use
$\ell+\log_2g\ge\log_2S_r-O(\log(c+1))$ and the upper bound on
$Kg$. The second also uses $g\le\binom cr$; the third follows from
the first and $\ell\le r$. All class choices and membership tests
use exact integers. Substituting the third line into the layer-aware
construction bound gives

$$
T=O^*\!\left(2^{(1+\theta)c+\phi d}\right),\qquad
S=O^*\!\left(2^{r/2}+\operatorname{poly}(c)\right).
\tag{154}
$$

Indeed, the expensive term is
$K\binom cr2^r\le O^*(2^{(1+\theta)c+\phi d})$;
the $K2^c$ term is smaller because $h(\theta)+\theta>1$ on the
active intervals. A center basis is stored once per unsigned core and
scalar configuration, before outer owners or top signings. Subsequent
per-center work retains the actual $K$ multiplicity.

For a center $D$, negate its weights and map a mask $S$ to
$S\mathbin\triangle D$. Its signed weight is the original weight
minus $\Delta_D=\sum_{i\in D}w_i$. On every fixed coordinate subset
$T$, the signed support is a translate of $\Sigma(T)$, so support-class
membership is independent of the center. Permitted fixed-cardinality
images are generated with their actual signed weights. Restoring
$\Delta_D$ recovers original local keys.

### II.2.5. Constructive balanced-cell families

We use a fixed number $Q_{\rm grid}$ of fine cells. For a core of size $b$
divisible by $Q_{\rm grid}$, fix a selected cardinality $r$ and smaller
cardinality $k$, with $Q_{\rm grid}\mid r,k$. A three-coloring
$(D,A\setminus D,B\setminus A)$ has totals $(k,r-k,b-r)$.
A uniform equipartition into $Q_{\rm grid}$ equal cells gives exactly
$1/Q_{\rm grid}$ of each color to each cell with probability at least

$$
p_b=(b+1)^{-3Q_{\rm grid}}.
\tag{155}
$$

For each color, its equally split multinomial coefficient is maximal
and at least $Q_{\rm grid}^{\,\text{color size}}/(b+1)^{Q_{\rm grid}}$.
Multiplying these three lower bounds and dividing by at most $Q_{\rm grid}^b$
equipartition labelings proves (155).

Construct a family covering every such coloring by greedy conditional
expectation. After some partitions are chosen, fix the labels of one
new partition coordinate by coordinate. For a coloring with remaining
color counts $r_a$, residual cell capacities $R_j$, and residual
target counts $t_{aj}$, its conditional coverage probability is

$$
\frac{\prod_a r_a!/\prod_{a,j}t_{aj}!}
     {(\sum_jR_j)!/\prod_jR_j!},
\tag{156}
$$

interpreted as zero for a negative target. Enumerate the uncovered
colorings, testing their status against the prior polynomial list,
and choose a next cell label at least as good as its capacity-weighted
mean. Each completed partition covers at least $p_b$ of the remaining
colorings. At most $p_b^{-1}(b\ln3+1)+1$ partitions suffice.
The factorials and score sums have polynomial bit length; the universe
is regenerated, and only the selected partition list is stored.

For an active strict local shell, $\theta=.45$, and the coloring count is
$\binom br\binom rk\le2^{[h(\theta)+\theta]b+O(Q_{\rm grid})}\le 2^{1.45m+O(Q_{\rm grid})}$.
For a top base of size at most $.9m$ it is at most
$3^{.9m+O(Q_{\rm grid})}<2^{1.427m+O(Q_{\rm grid})}$, and an oriented half uses at
most $3^{m/2}$. Multiplication by the fixed-degree polynomial factors
preserves these bounds. Thus this construction supplies all required
fine-cell families within the half-exponential budget using polynomial
state. The local families depend only on their fixed cores and cardinalities.
Construct them before the ownership and signing loops, then reuse them
throughout. Top-base families are likewise reused across their signings.

To align a useful smaller layer, remove fewer than $Q_{\rm grid}$ elements from
each of its distinct-sum witnesses. If the removed set is $R$, its
original sum is the trimmed sum plus $\sum_{i\in R}w_i$; one trimmed
sum accounts for at most $\binom b{|R|}$ original sums.
Thus trimming loses at most $b^{Q_{\rm grid}-1}$.
For each retained sum choose one trimmed witness. Every three-coloring
is balanced by some partition in the constructed family, so one
partition retains a reciprocal-polynomial fraction of the distinct sums.
The selected pattern occupies $r/Q_{\rm grid}$ positions per cell and its
smaller mask $k/Q_{\rm grid}$ positions. The total trimming, layer, and layout
loss is $O(Q_{\rm grid}\log(b+1))$ in its support logarithm.
Choose shell sizes divisible by $Q_{\rm grid}$ within $O(Q_{\rm grid})$ of $\theta b$;
this changes the finite trace estimates only by the same lower-order
term.

### II.2.6. Retained quarter layers

Consider a good selected shell of size
$r=\theta c+O(Q_{\rm grid})$ with $N(T)\ge2^\ell$ and
$\theta c-\ell\le\phi d+O(Q_{\rm grid}\log(m+1))$.
If the full-block deficiency density is at most $x$ and
$\phi x<\theta/8$ with a fixed positive gap, density monotonicity gives
$\ell/r>7/8$ after a fixed coordinate cutoff.
Pigeonhole distinct-sum witnesses by cardinality, complement within
$T$ if necessary, and trim fewer than $Q_{\rm grid}$ positions.
The resulting smaller layer $k\le r/2$ retains at least
$2^\ell/\operatorname{poly}(m)$ distinct sums. Since its cardinality
is at most $2^{r h(k/r)}$,

$$
h(k/r)\ge\ell/r-o(1)>7/8>h(1/4).
\tag{157}
$$

The last comparison follows from $3^9>2^{14}$, which gives
$h(1/4)<5/6$. Hence a useful layer has $k/r>1/4$ with a fixed margin.
We retain only $r/4\le k\le r/2$ before expensive processing.
The polynomial family of retained layers and layouts preserves a
representation of every original solution.

For the biased top, $\theta=21/50$, $x\le27/200$, and
$\phi\le143/400$. For a strict local core, $\theta=9/20$ and
$\phi\le31/80$. The requisite gaps are

$$
\frac{\theta}{8}-\phi x\ge
\begin{cases}
339/80000,&\theta=21/50,\\
63/16000,&\theta=9/20.
\end{cases}
\tag{158}
$$

Every retained top layer satisfies
$k/c\ge.105-o(1)>.1$ and $(r-k)/c\ge.21-o(1)>.2$.
The integer inequalities
$10^{20}>2^9 9^{18}$ and $5^{10}>2^{23}$ give
$h(.1)>9/20$ and $h(.2)>7/10$. Its actual mean mask entropy
therefore exceeds $23/40$ after the fixed cutoff.
For every retained strict local layer,
$k/c\ge9/80-o(1)>1/9$ and $(r-k)/c\le27/80+o(1)<7/20$.
The inequalities $9^6>2^{19}$ and
$20^{80}<2^{75}7^{28}13^{52}$ imply
$h(1/9)>1/2$ and $h(7/20)<15/16$. Thus

$$
h((r-k)/c)-h(k/c)<7/16.
\tag{159}
$$

These bounds apply to every processed layer. The fine-cell product
counts incur $O(Q_{\rm grid}\log(m+1))$ error. Concavity also gives
$h(k/c)+h((r-k)/c)\ge h(\theta)-o(1)$, which will bound the
unrestricted child domains.

### II.2.7. Shared local image scans

For fixed local layer, layout, and child roles, a center $D$ and good
selected set $T$ determine a permitted image $X_D(T)$.
In a candidate-prime scan, enumerate $T$ first and count its support
once. For good $T$ only, enumerate the centers and generate
$X_D(T)$. Since $K|\mathcal G_\ell|\le\operatorname{poly}(c)2^c$,

$$
O^*\!\left(\binom cr2^r+K|\mathcal G_\ell|2^r\right)
=O^*(2^{c+r})
\tag{160}
$$

bounds one complete scan. The support-class test is independent of
$D$, by the translation identity above. It is also independent of the
outer top label.

For one top seed, construct all local weighted residue covers in
lockstep. Keep each center's uncovered count, candidate interval,
polynomial seed list, and separate resource means. At every score
pass, put the good-set loop outside the center loop, generating one
image and its residue-prefix counts at a time. An image and its offsets
cost $O^*(2^r)$, since its modulus is $O^*(2^\ell)$ and $\ell\le r$.
Thus a simultaneous coverage-score pass costs $O^*(2^{c+r})$.
Regenerate each center's resource vector in a shared workspace and
compare its own two exact means. The histogram cost is separately

$$
O^*\!\left(K(P_{\max}^2+P_{\max}+2^{m-c})\right).
\tag{161}
$$

Only $O^*(K)$ scalar and seed state is cached. One image, histogram,
and complementary-support workspace is live at a time. Each cover
retains its own nonnegative cost normalizers; interleaving their score
passes preserves every conditional-expectation guarantee.

## II.3. Weighted ownership representations

Let a top core have size $a$, $N$ distinct subset sums and deficiency $d=a-\log N$. For the dense branch, use $a=.9m+O(1)$, $p=1/20$, and $d/a\le17/2000+O(1/m)$. The representation and checker constructions below have the following bounds:

$$
\begin{aligned}
T_{\rm owner}&=O^*(2^{3a/2+2d}),&
S_{\rm owner}&=O^*(2^{a/2}+2^d),\\
T_{\rm container}&=O^*(2^{.3825m}),&
S_{\rm construction}&=O^*(2^{.1275m}),\\
S_{\rm assignment/index}&=O^*(2^{.265185m}).
\end{aligned}
\tag{162}
$$

Every parent retains movable top/background logarithmic mass at least $m/2-O(\log m)$. Its upper mass is the central equal-rate budget, up to polynomial factors. Exact incidence is bounded by $2^{3m/2}$ times a polynomial whenever the original local full-block deficiency is at least $d$. The bounds hold for arbitrary indexed integer weights and every feasible fine profile.

### II.3.1. Direct coefficients and canonical distance

Let $H$ be the owner-right region of cardinality $b$. For an original top subset $S$ and variation mask $R$, use

$$
(\alpha_i,\beta_i)=
\begin{cases}
(S_i\oplus R_i,\ R_i(2S_i-1)),&i\notin H,\\
(R_i(2S_i-1),\ S_i\oplus R_i),&i\in H.
\end{cases}
\tag{163}
$$

The coordinate sum is $S_i$. The left top weight is
$w(S\setminus H)+w^{S\oplus H}(R)$, where $w_i^G=(-1)^{G_i}w_i$.
The parents store these original coefficient weights. A compatible pair is exactly one with binary coordinatewise sums.

Choose the smallest indexed full mask $X$ for each distinct original top sum, and denote this family by $\mathcal F$. For a given $S$, let $N_j(S)$ count its canonical witnesses at Hamming distance $j$. Fix integers $b,u,v$ with
$0\le u\le a-b$, $0\le v\le b$, and $j=b+u-v$. Set

$$
Q=\binom{a-b}u\binom bv,\qquad
c(S,H)=\#\{X\in\mathcal F:
 |(X\oplus S)\setminus H|=u,\quad |(X\oplus S)\cap H|=b-v\}.
\tag{164}
$$

For $R=X\oplus S\oplus H$, the required variation quotas are $u,v$.
For fixed $H$, its signed sum equals
$w(X)-w(S\oplus H)$, so canonical contributions remain distinct.
Consequently $c(S,H)$ is a lower bound on the actual signed quota-image size and $c(S,H)\le Q$.

Counting the same pairs $(Y,H)$, with $|Y|=j$, in two orders gives

$$
\binom aj\binom ju\binom{a-j}v=\binom ab Q,\qquad
\frac1{\binom ab}\sum_{|H|=b}c(S,H)
 =\frac{N_j(S)Q}{\binom aj}.
\tag{165}
$$

Choose a distance band $I$ by the integer condition
$\sum_{j\notin I}\binom aj\le N/2$.
For every $S$, some $j\in I$ then has
$N_j(S)\ge N/[2(a+1)]$. All distances in the band are enumerated.

### II.3.2. Weighted owner covers

For a fixed distance and quota configuration, put $C_0=2(a+1)$,

$$
\mathcal E=\{S:C_0N_j(S)\ge N\},\qquad
M=\frac{NQ}{C_0\binom aj},\qquad
L_Q=1+\lfloor\log Q\rfloor.
\tag{166}
$$

Configurations with $M>Q$ have empty eligible universe. Otherwise maintain pairs $(H_i,\ell_i)$, with $0\le\ell_i<L_Q$, and the implicit uncovered set
$\mathcal U=\{S\in\mathcal E:c(S,H_i)<2^{\ell_i}\text{ for all earlier }i\}$.
When $\mathcal U\ne\varnothing$, choose $H$ satisfying
$\sum_{S\in\mathcal U}c(S,H)\ge M|\mathcal U|$.
For $r_\ell=\#\{S\in\mathcal U:c(S,H)\ge2^\ell\}$, the inequality
$c\le\sum_{2^\ell\le c}2^\ell$ gives some threshold with
$2^\ell r_\ell\ge M|\mathcal U|/L_Q$. Choose a maximizing threshold and append that pair.

Charge $2^{-\ell}$ to the pair. If it removes $r$ of the $U$ current elements, its charge is at most $Lr/(MU)$. Summing this through successive removals is bounded by a harmonic sum:

$$
\sum_i2^{-\ell_i}\le\frac{L_Q H_{|\mathcal E|}}M
 \le\frac{L_Q(1+a\ln2)}M,\qquad
K:=\#\{i\}\le\operatorname{poly}(a)2^d.
\tag{167}
$$

The last inequality uses $2^{-\ell_i}\ge1/Q$ and
$\binom aj\le2^a$. Grouping pairs by threshold yields, for each group,

$$
\frac{K_\ell Q}{2^\ell}
 \le\operatorname{poly}(a)\frac{\binom aj}{N}.
\tag{168}
$$

Every eligible pattern succeeds in at least one of the enumerated groups.

Here is a low-state implementation of the owner choice. A prefix fixes owner-one coordinates $F_1$, owner-zero coordinates $F_0$, and leaves $W$ unfixed. It has
$B_P=\binom{|W|}{b-|F_1|}$ completions. For a mask $Y$, put
$z_1=|Y\cap F_1|$, $z_w=|Y\cap W|$. The number of these completions giving the prescribed quotas is zero unless $|Y|=j$, and otherwise equals

$$
k_P(Y)=
 \binom{z_w}{b-v-z_1}
 \binom{|W|-z_w}{b-|F_1|-(b-v-z_1)}.
\tag{169}
$$

Infeasible binomial arguments mean zero. The mean total trace over the prefix's completions is:

$$
A_P/B_P,\qquad
A_P=\sum_{S\in\mathcal U}\sum_{X\in\mathcal F}k_P(S\oplus X).
\tag{170}
$$

The current mean is the completion-count-weighted average of the feasible next-bit means. Exact cross multiplication therefore chooses a child with no smaller mean. Starting from (165), $a$ choices produce the required owner. The uncovered set is kept fixed throughout these prefix choices.

Partition coordinates computationally into halves of sizes $\lfloor a/2\rfloor,\lceil a/2\rceil$, independently of ownership. Write $S=(s,z)$, $X=(x,y)$. For fixed $s$, scan $\mathcal F$ and group its low masks $y$ by the three high-part counts of $x\oplus s$ in $F_1,F_0,W$. There are polynomially many arrays of length $2^{\lceil a/2\rceil}$. For each high-count triple, form the low kernel by inserting its counts and the low-mask counts into (169). Summing their XOR convolutions gives every value
$\sum_X k_P((s,z)\oplus X)$ for that $s$.

A Walsh transform computes each convolution exactly: apply the butterflies $(x,y)\mapsto(x+y,x-y)$, multiply the transforms pointwise, apply the transform again, and divide by its length. Character orthogonality proves exactness. The counts and intermediate values have polynomial bitlength. Grouping by high distance similarly computes $N_j((s,z))$; grouping by the two high quota counts computes $c((s,z),H_i)$ for any previous pair. Retain the eligibility/uncovered Boolean array for this $s$, and process previous pairs sequentially.

The canonical scan itself sorts the two half-subset occurrence lists and heap-merges their pair-sum rows. Process each equal-weight run completely, retaining only its smallest full mask. It costs $O^*(2^a)$ time and $O^*(2^{a/2})$ state per reset, including repeated and negative sums. For each $s$, its scan dominates the polynomially many low transforms. Enumerating all $s$, a prefix score, termination test or threshold count costs
$O^*(2^{3a/2}(1+K_{\rm old}))$ time and
$O^*(2^{a/2}+K_{\rm old})$ state.
Summing over the $K$ choices proves the first line of (162).

For each nonempty group and $t=j/a-1/2$, binomial upper bounds turn (168) into

$$
\log Q-\ell+\log K_\ell
 \le d-aD(t)+O(\log a),\qquad
D(t)=1-h(1/2+t).
\tag{171}
$$

The owner lists are constructed before the common-prime selection of Section II.4, which uses their actual signed quota images.

### II.3.3. Equal rates on unequal owner regions

Fix $p=1/20$. For an exact distance $j$, set

$$
t=j/a-1/2,\qquad z=\frac{t}{1-2p},\qquad
b=a(1/2+z),\qquad
u=p(a-b),\quad v=pb.
\tag{172}
$$

Then $b+u-v=j$, the total variation radius is $pa$, and the ideal natural quota entropy is $a h(p)$, independent of $t$.
Round $b$, round $u=p(a-b)$, and define $v=b+u-j$. This preserves the distance exactly and changes all counts by $O(1)$. On the active band $|t|\le.06$, both owner regions and both quota fractions have fixed positive interior margins, so rounding changes logarithmic estimates by $O(\log a)$. Thus

$$
\log Q=a h(p)+O(\log a),\qquad u+v=pa+O(1).
\tag{173}
$$

The band exists for every original pattern: strict extraction does not increase density, so $d/a\le.0085+O(1/m)$, whereas the positive entropy series and $\ln2<52/75$ give

$$
D(.06)\ge\frac{2(.06)^2}{52/75}
 =\frac{27}{2600}>\frac{17}{2000}.
\tag{174}
$$

The binomial tail outside the band is at most
$2(a+1)2^{a h(.56)+O(1)}$, hence is below $N/2$ after a fixed coordinate cutoff. The algorithm verifies the band by the exact integer tail comparison.

Write $n_-=a-b$ and $n_+=b$ for the exact owner-region sizes. Their ideal values are $a(1/2-z)$ and $a(1/2+z)$, respectively, with bounded rounding error.

### II.3.4. Physical profiles and background allocation

Choose each local useful cardinality layer, balanced layout and child role from its physical integer image before common-prime selection. Full selected-support size at least its Good threshold gives a useful physical layer/layout after a polynomial loss in the coordinate count alone; this gives the physical local-layer contrast of Section II.2. Include all such enumerated local images in the common-prime universe, together with the global exact-quota top images. Keep the selected local images and child roles fixed throughout the following top refinement. Once the common prime path makes the global top image good, retain one variation witness per occupied top residue; each witness belongs to a residual cyclic-layout branch from Section II.6.1. A polynomial pigeonhole leaves one branch with a reciprocal-polynomial fraction of these residues. Partition the top regions into a fixed number $Q_{\rm grid}$ of fine chunks and enumerate their support counts; repeat the same pigeonhole step for these profiles. The algorithm enumerates every branch, and the eligibility allowance includes these polynomial losses. Local images remain fixed.

For an actual top profile, put $P_-=\prod_{C\subseteq H^c}\binom{|C|}{u_C}$ and $P_+=\prod_{C\subseteq H}\binom{|C|}{v_C}$, where $C$ ranges over its fine chunks and fixed residual coordinates are singleton chunks. Write $h_-=\log P_-$, $h_+=\log P_+$, and $r=u+v$. The exact raw top-domain logarithms are

$$
L_L=n_-+h_++v,\qquad
L_R=n_++h_-+u,
\qquad
M_{\rm total}=m+h_-+h_++r.
\tag{175}
$$

These use actual products, including sparse profiles. Since
$P_-P_+\le Q$, take the exact upper cap

$$
M_{\rm cap}=\frac{m+\log Q+r}{2}.
\tag{176}
$$

Choose $M_j\in[\max(m/2,L_j),M_{\rm cap}]$ with sum $M_{\rm total}$. Then $z_j=M_j-L_j\ge0$ are background counts summing to $m-a$. The interval conditions follow as follows. The upper-sum condition is $M_{\rm total}\le2M_{\rm cap}$, from $P_-P_+\le Q$. The sum of the two lower bounds is handled by four cases. The both-$m/2$ case uses $M_{\rm total}\ge m$; the both-$L_j$ case uses $m\ge a$. The two mixed cases follow from
$m/2\ge(1-p)\max(n_-,n_+)$ up to bounded rounding. Each individual upper bound exceeds its raw lower bound when the following two inequalities hold with fixed slack:

$$
m-a\ge2|z|[1-h(p)-p]a,\qquad
m-a\ge[2|z|(1-p)-p]a.
\tag{177}
$$

The first proves $L_j\le M_{\rm cap}+O(\log a)$, using
$h_\pm\le n_\pm h(p)+O(\log a)$; the second proves the mixed lower-sum cases. Also $M_{\rm cap}\ge m/2$.
With $p=.05$, $|z|\le1/15$, $a=.9m+O(1)$, their right sides are respectively less than $.08m$ and at most $.069m$, whereas $m-a=.1m+O(1)$. Thus every profile has a feasible interval pair after a fixed cutoff.

Use exact integer products to choose the background counts. Binary-search the least integer $z_L\in[0,m-a]$ satisfying $z_L+L_L\ge m/2$ and $m-a-z_L+L_R\le M_{\rm cap}$, and put $z_R=m-a-z_L$. Real interval feasibility shows that the other two bounds are missed by at most one. Both tests are monotone; squaring the domain products compares them with the integers $2^m$ and $2^{m+r}Q$. Accordingly,

$$
M_j\ge m/2-O(1),\qquad
M_j\le\frac{m+a[h(p)+p]}2+O(\log a).
\tag{178}
$$

The fixed slack in (177) absorbs the binomial and quota-rounding corrections. Every one of the $m-a$ background coordinates is assigned.

Equation (178) supplies the actual movable mass required by the local atomic allocation in Section II.5; the local mask images and child roles remain fixed.

Substituting (173) and (178) into the child and restart resource formulas of Sections II.5 and II.7 gives the central top coefficients

$$
D_p=\frac{h(p)-p}{2},\qquad
A_p=\frac{h(p)-3p}{4},\qquad
f_p=\frac{h(p)+p}{8}.
\tag{179}
$$

Equation (171) subtracts $aD(t)$ from both central raw and restart exponents and preserves the leaf coefficient. The checker enlargement affects incidence and tuple state only. Each fine-chunk factor has logarithmic size at most twice its coordinate count. With $Q_{\rm grid}$ fixed before the input, all layout, count-profile and residue-pigeonhole families have fixed polynomial size. Their logarithmic losses are polynomial factors. The fine-factor packing in Section II.5 incurs $O(m/Q_{\rm grid}+Q_{\rm grid}\log(m+1))$ error. The fixed grid and cutoff in Section II.8 place this error within the certified margins.

## II.4. Common modular filters and weighted covers

Let $u=n+L+2$. Every integer difference below has fewer than $2u$
binary digits. A pattern means a permitted selected mask together with
its signing or ownership label. Its image is a set of distinct integer
sums. For a distinct image $X$, define

$$
C_q(X)=\sum_{z\bmod q}f_z(f_z-1),
\qquad f_z=|\{x\in X:x=z\bmod q\}|.
\tag{180}
$$

For $h\ge4$ there are at least $2^h/(4h)$ primes in
$[2^h/(4h),2^h)$. Indeed, for $x=2^h$ the central binomial
coefficient is at least $2^x/(x+1)$. Its valuation at each prime
$p$ is at most $\lfloor\log_px\rfloor$, by the factorial valuation
formula. Hence it is at most $x^{\pi(x)}$, so
$\pi(x)\ge(x-\log_2(x+1))/h$. Subtracting at most $x/(4h)$
smaller primes proves the claim; $x$ is composite.
A sieve constructs the pool. Conditioned on $q\mid x-y$, the condition
$qp\mid x-y$ is exactly $p\mid(x-y)/q$, including repeated prime
factors. The quotient has at most $2u$ distinct prime divisors. Thus a
uniform prime in this pool satisfies

$$
\mathbb E_p C_{qp}(X)\le8u^2 2^{-h}C_q(X).
\tag{181}
$$

Call $p$ bad for $X$ if $2^hC_{qp}(X)>80u^2C_q(X)$.
At most one tenth of the pool is bad. If $C_q(X)=0$, every prime is
good. Let $2^B$ bound the total number of individual patterns;
For example, encode mask labels and the indices of the fixed layout
families and take
$B=4n+100Q_{\rm grid}^2\lceil\log_2(n+1)\rceil+100Q_{\rm grid}^2$.
The constructive families above have polynomial degree linear in
$Q_{\rm grid}$, so this bounds every label length. At each fixed prefix $q$, select
$k=32(B+1)$ prime positions with repetition. If $b_A$ earlier positions
were bad for pattern $A$, choose the next prime minimizing

$$
\sum_A2^{b_A+1_{\{p\text{ bad for }A\}}}.
\tag{182}
$$

Its conditional mean is at most $11/10$ times the preceding sum.
After $k$ choices the sum is at most $2^B(11/10)^k<2^{k/4}$.
Each pattern is bad at fewer than $k/4$ positions. Every triple of
patterns therefore has a position good for all three.

Let $\ell_0,\ell_L,\ell_R$ be the natural image scales supplied by
the representations. Split the sorted scale increments into pieces
at most $\lceil\ell_{\max}/16\rceil$, retaining all three endpoints.
There are at most nineteen pieces. A piece smaller than four uses
factor one; every other piece uses (182). Branch over the selected
prime positions, stopping an image at its scale. This fixed-depth tree
has polynomial size. Every eligible triple has a path good at all
active stages. Its recorded moduli satisfy

$$
\frac{2^{\ell_i}}{\operatorname{poly}(u)}\le p_i\le2^{\ell_i},
\qquad
C_{p_i}(X_i)\le(80u^2)^{19}|X_i|^2/p_i.
\tag{183}
$$

They form a divisibility chain, with
$p_j/p_i\le2^{\ell_j-\ell_i}$ when $\ell_i\le\ell_j$.
Skipping short pieces loses a constant factor. Cauchy--Schwarz gives

$$
|X_i\bmod p_i|\ge
\frac{p_i}{p_i/|X_i|+(80u^2)^{19}}.
\tag{184}
$$

Eligibility means $|X_i|\ge2^{\ell_i}/\operatorname{poly}(u)$ with
a fixed polynomial. Fix an integer $E_{\rm img}$ larger than its degree and put
$\delta=u^{-(2E_{\rm img}+400)}$. After a fixed small-input cutoff every
eligible image on a common-good path has density at least $\delta$.

Process one image at a time, replaying the selected prime positions
to compute its bad count and accumulating (182). The physical
local-image scans in Section II.2.7 include all signing, layer and
layout labels, with Good-set membership tested outside the signing
loop. Their total cost per candidate is $O^*(2^{c+r})$.
Prime enumeration contributes $2^{\ell_{\max}/16+O(1)}$.
Ownership scans retain their actual owner count. Section II.8 bounds
all construction costs. The live arrays contain one image, its
residue frequencies and polynomially many prime positions; potential
values have polynomial bit length.

### II.4.1. A universal weighted translate cover

Suppose images $I_A\subseteq\mathbb Z/p\mathbb Z$ have density at
least $\delta$. Let $c(\rho)\ge0$ be an exact rational cost with
uniform mean $\mu$. If $Q$ pattern-offset pairs remain uncovered, let
$\operatorname{cov}(\rho)$ count those covered by $\rho$. Its mean
is at least $\delta Q$. When $\mu>0$, select a residue with score
at least the mean of

$$
\operatorname{cov}(\rho)-\frac{\delta Q}{2\mu}c(\rho).
\tag{185}
$$

That mean is at least $\delta Q/2$. The selected residue covers at
least $\delta Q/2$ pairs and costs at most $2\mu/\delta$, since
$\operatorname{cov}(\rho)\le Q$. If $\mu=0$, all costs vanish and
use coverage alone. Repeating for
$O(\delta^{-1}\log(Q+1))$ rounds gives a polynomial-size list
$\mathcal R$ satisfying

$$
\mathcal R\cap(I_A+v)\ne\varnothing\quad\text{for all }A,v,
\qquad
\sum_{\rho\in\mathcal R}c(\rho)
\le\operatorname{poly}(u)\mu.
\tag{186}
$$

For $s$ costs with positive means use the penalty
$\delta Q\sum_i c_i(\rho)/(2s\mu_i)$ in (185). This proves
(186) separately for each cost. Zero-mean terms are identically zero.

Find the residue by interval conditional expectation: bisect
$[0,p-1]$ and retain a child whose average score is at least its
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

$$
O^*\!\left(K(P_{\max}^2+2^{m-c}+P_{\max})\right)
\quad\text{time},\qquad
O^*(P_{\max}+K+2^{m-c})\quad\text{space}.
\tag{187}
$$

Construct the cover once for a fixed outer configuration and top
residue; reuse it in every interval query. It covers the solution's
translated local image at its actual parent lift.

## II.5. Top projection and atomic local generators

### II.5.1. Projecting a useful integer layer

Let a fixed signed top base have $b$ coordinates, selected set $T$ of
size $sb$, and a cardinality layer with $M$ distinct sums. Orient the
layer by complementation inside $T$ so its size is at most $sb/2$.
Trim to the fixed cell divisibility as in Section II.2, losing only
a polynomial factor, and recanonicalize each retained sum in the
complete trimmed layer of $T$.

The balanced-cell family gives a layout into $Q_{\rm grid}$ equal
cells and a subfamily $\mathcal F$ of at least
$M/\operatorname{poly}(b)$ canonical masks with equal selected and
layer counts in each cell. The family of distinct projected masks from $\mathcal F$
on any union of cells is sum-injective. Otherwise
replacing the larger equal-sum projection in its full witness would
preserve both its cardinality and sum while decreasing the canonical
witness.

For completeness, write $\operatorname{Ent}$ for binary Shannon
entropy. Factoring joint probabilities proves the chain rule;
concavity of $-\sum p_i\log_2p_i$ shows that additional conditioning
decreases conditional entropy. For uniform $D\in\mathcal F$, expand
$\operatorname{Ent}(D\cap U)$ in coordinate order, where $U$ is a
uniform union of $p$ cells. Replace conditioning on earlier coordinates
of $U$ by conditioning on all earlier coordinates. Each coordinate
belongs to $U$ with probability $p/Q_{\rm grid}$, so

$$
\mathbb E_U\operatorname{Ent}(D\cap U)
\ge\frac{p}{Q_{\rm grid}}\log_2|\mathcal F|.
\tag{188}
$$

Some union therefore has at least $|\mathcal F|^{p/Q_{\rm grid}}$
projected masks, all with distinct actual sums. Its size is
$a=pb/Q_{\rm grid}$, and the selected fraction and relative layer
cardinalities are unchanged. Thus a support threshold $2^\ell$ on
the base yields a projected permitted image of size at least

$$
2^{(a/b)\ell}/\operatorname{poly}(b).
\tag{189}
$$

Enumerate the layouts and all cell unions of the prescribed size.
The number is polynomial with fixed degree, since $Q_{\rm grid}$ is
fixed. Choose $p$ divisible by four; downward grid rounding changes
the ideal $a/m$ by at most $4/Q_{\rm grid}$. All these are integer
images selected before common-prime construction. The signed
coordinates outside the projection remain ordinary top background.
The entire base-signing offset is restored once after the final join.

Let $Q_L,Q_R$ be the actual products of the permitted top-mask
binomial counts, and let $F=m-a$ background coordinates remain.
Choose $z_L$ nearest to
$(F+\log_2Q_R-\log_2Q_L)/2$, and put $z_R=F-z_L$.
This is an exact integer search comparing $2^{2z_L}Q_L$ with
$2^FQ_R$. When the background-feasibility inequalities below have
their fixed reserve, both counts are nonnegative after the cutoff.
The ancestor products $A_j=2^{z_j}Q_j$ then satisfy

$$
\begin{gathered}
\log_2A_j\le\tfrac12(F+\log_2Q_L+\log_2Q_R)+1
\le\tfrac m2+(\overline H-\tfrac12)a+1,\\
\log_2A_j\ge\tfrac m2+(\overline H-\tfrac12)a
 -O(Q_{\rm grid}\log(m+1)),
\end{gathered}
\tag{190}
$$

where $\overline H$ is the actual mean of the two mask entropy rates.
The upper comparison uses exact product balancing and the binomial
upper bound. The lower comparison also uses the binomial lower bound
over the fixed number of cells. In particular
$\overline H\ge1/2$ supplies the movable-mass floor, while the upper
comparison gives incidence bounds with polynomial losses only.

### II.5.2. Biased top shells

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
\tag{191}
$$

Here $x_0$ bounds the full top-block deficiency density, and strict
extraction preserves this density bound. Let the linear translate
cover of this class have $K$ centers. It satisfies
$Kg\le\operatorname{poly}(m)2^b$. Put

$$
\delta=sb-\ell,\qquad \kappa=\log K,\qquad \tau_0=1-h(s).
\tag{192}
$$

Since $g\le\binom br\le\operatorname{poly}(m)2^{h(s)b}$,

$$
\delta+\kappa\le\tau_0b+\phi_0d+O(\log(m+1)),
\qquad \delta\le\phi_0d+O(\log(m+1)).
\tag{193}
$$

Each center is a separate outer signing. For any original witness,
one center makes its selected top set belong to the class. Negating
that center's coordinates translates the target once. Coordinates
later returned to the background retain their signed weights.

**Physical projection.**

Fix an outer center. Pigeonhole its selected-set support by
cardinality, orient the smaller layer and apply (189) before common
primes. Projection scales the physical deficit to $(a/b)\delta$;
the outer code cost remains $\kappa$.

Write $k\in[0,s/2]$ for the smaller-layer fraction on the base and set

$$
\begin{gathered}
H_-=h(k),\quad H_+=h(s-k),\quad
\overline H=(H_-+H_+)/2,\quad H_0=h(s/2),\\
L_0=H_0-\overline H,\quad \Delta=H_+-H_-,\quad
D_0'=\tfrac12+s-H_0,\quad p=D_0'-\delta/b.
\end{gathered}
\tag{194}
$$

The active density range makes $p>0$. Choose the ideal projected size

$$
a=\frac{pb}{p+L_0}.
\tag{195}
$$

It gives the exact raw-resource identity

$$
-(\tfrac12+s-\overline H)a+(a/b)\delta+\kappa
=-D_0'b+\delta+\kappa.
\tag{196}
$$

Thus the top raw contribution is at most
$-D_0b+\phi_0d+O(\log(m+1))$, with $D_0=D_0'-\tau_0$.
The corresponding restart contribution is also bounded by its central
base value. Its difference from that value is

$$
\frac{L_0a}{2p}(\delta/b-s)\le0.
\tag{197}
$$

The leaf contribution satisfies
$(\overline H/4-1/8)a\le(H_0/4-1/8)b$ whenever
$\overline H\ge1/2$, as proved below. Projection therefore preserves
the required central resource bounds without scaling the outer code.

**Background feasibility.**

Let $B=b/m$. Balancing the actual top-mask products requires
$a(1+\Delta)\le m$. A sufficient uniform condition is

$$
1-B\ge\frac{28}{25}pB^2.
\tag{198}
$$

For completeness, put $c=s/2$, $t=c-k$, and $v=pB$. The function

$$
F(t)=(\tfrac12+v)h(c+t)+(\tfrac12-v)h(c-t)
\tag{199}
$$

has $F(0)=H_0$ and $F'(0)=2v h'(c)$. On
$c\in[1/5,1/4]$, $0\le t<c$, $v\le1/5$,

$$
-F''(t)=
\frac{c(1-c)-t^2-2v(1-2c)t}
{(\ln2)(c^2-t^2)((1-c)^2-t^2)}\ge\frac5{\ln2}.
\tag{200}
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
\tag{201}
$$

Exact top-product balancing supplies at least
$m/2+(\overline H-1/2)a+O(\log m)$ movable logarithmic mass per
parent. The atomic-complement allocation therefore applies throughout
the enumerated layer range, rather than relying on eligibility for
each processed configuration.

**Incidence and resource bounds.**

For a full local block with deficiency $d_j$, the parent ambient
exponent, including the outer top code, is

$$
\frac{3m}{2}-d_j-(\tfrac12+s-\overline H)a
 +(a/b)\delta+\kappa.
\tag{202}
$$

Adding the separator degree $d_sa$, its difference from the central
bound $3m/2-d_j+\delta+\kappa-\tau_0b/2$ is exactly

$$
-\frac{L_0a d_s}{p}\le0.
\tag{203}
$$

Since $d_j\ge x_0m$ and $d\le m\beta(x_0,\rho)$, the central
incidence excess is at most

$$
I=\tfrac12\tau_0\rho+\phi_0\beta(x_0,\rho)-x_0.
\tag{204}
$$

Section II.8 proves $I<-1/1250$ on the active
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
\tag{205}
$$

The oriented-half local mode keeps its exact nonpositive compression
corrections. All definitions and inequalities here concern actual
integer images before modular reduction. Common primes are selected
only after those images are fixed. Universal local covers handle every
later background translation, and original-key signing unions retain
the full-block ambient bound without a local Cartesian code factor.

### II.5.3. The ordinary half-selected top

The high-tail mode uses a strict top base $V$ of size $b=\rho m$,
$\rho=18/25$. The prefix masks and their complements form a
polynomial signing family. Prefix flips take every original selected
cardinality from $|S|$ to $b-|S|$ in unit steps, so some signing gives
a half-selected set $T$. Its complementary signing gives $V\setminus T$.
Since $N(V)\le N(T)N(V\setminus T)$, one has support at least
$\sqrt{N(V)}$. Cardinality pigeonholing and (189) give a projected
permitted image at the exact inherited scale

$$
\ell_0=\left\lfloor\frac{a}{2b}\log_2N(V)\right\rfloor.
\tag{206}
$$

Let $N_0$ be the original full top-block support. Deficiency density
decreases during extraction, so

$$
\ell_0\ge\left\lfloor\frac{a}{2m}\log_2N_0\right\rfloor,
\qquad f_0:=a/2-\ell_0\le\frac{a}{2m}d_0+1.
\tag{207}
$$

Here $d_0=m-\log_2N_0$. These comparisons use the actual supports.

To choose the projected size uniformly over layers, set
$h_0=h(1/4)$ and $p_0=1-h_0-\xi/2$, where $\xi\le.203$ is the
nominal base-density bound. For a smaller-layer fraction
$k\in[0,1/4]$, put

$$
\overline H=\tfrac12[h(k)+h(1/2-k)],\quad
\Delta=h(1/2-k)-h(k),\quad
a_* =\frac{p_0\rho m}{p_0+h_0-\overline H}.
\tag{208}
$$

The following sufficient conditions hold in this mode:
$p_0>0$, $p_0\rho<1/5$, and
$1-\rho\ge(7/10)p_0\rho^2$. Indeed $h_0<.812$,
$\xi/2\le.1015$, $p_0<.19$, and $\rho=.72$.
They imply $a_*(1+\Delta)\le m$ as follows.
Write $t=1/4-k$, $r=p_0\rho$, and

$$
F(t)=(\tfrac12+r)h(1/4+t)+(\tfrac12-r)h(1/4-t).
\tag{209}
$$

Then $F(0)=h_0$, $F'(0)=2r\log_23$, and

$$
-(\ln2)F''(t)=
\frac{3/16-t^2-rt}{(1/16-t^2)(9/16-t^2)}\ge5.
\tag{210}
$$

Subtracting five times the denominator leaves at least
$3/256+(29/16)t^2-rt\ge3/256-4r^2/29>0$.
Completing the square gives
$F(t)\le h_0+2(\ln2)(\log_23)^2r^2/5<h_0+.7r^2$.
The last strict comparison follows from $\ln2<52/75$ and
$3^{200}<2^{317}$. Since $F=\overline H+r\Delta$, the reserve
condition proves

$$
h_0-\overline H\ge p_0[\rho\Delta-(1-\rho)].
\tag{211}
$$

This yields the asserted background feasibility and

$$
\begin{aligned}
(1-\overline H-\xi/2)a_*&=(1-h_0-\xi/2)\rho m,\\
(\overline H/2-1/4)a_*&\le(h_0/2-1/4)\rho m.
\end{aligned}
\tag{212}
$$

Here $1/2\le\overline H\le h_0$. Round down to an enumerated
four-cell multiple. The reserve is strict, so actual integer mask
products admit nonnegative background counts after the fixed cutoff.
Use the actual binomial products to balance those counts within one
bit, as in the biased-top construction.

The all-layer separator of Section II.6 at selected fraction $1/2$
has common degree $O^*(2^{(1-h_0)a})$. If $\Lambda_j$ is the original
parent ambient exponent, exact product balance and (207) give

$$
\begin{aligned}
\Lambda_j+(1-h_0)a
&\le\tfrac32m-d_j+f_0-(h_0-\overline H)a+O(\log(n+L))\\
&\le\tfrac32m-d_j+\frac{a}{2m}d_0+O(\log(n+L))
\le\tfrac32m+O(\log(n+L)).
\end{aligned}
\tag{213}
$$

The last step uses the least-deficient full top block, so $d_0\le d_j$.
Incidences retain this actual inherited scale separately from the
strict grid allowances used for raw and leaf resource bounds.

### II.5.4. Whole-complement supports and exact allocation

Fix a local core $C\subseteq B_j$ of size $c\ge m/2-O(Q_{\rm grid})$, chosen before
its signing and useful layer. Put $T=B_j\setminus C$. Store one indexed
witness per actual sum in $\Sigma(T)$, and write

$$
R_T=\log_2N(T)=m-c-d_T\le m/2+O(Q_{\rm grid}).
\tag{214}
$$

The sorted support stream constructs this array in $O^*(2^{m-c})$
time and $O^*(2^{m/2})$ space, including generation state. Reuse it
across local signings. These coordinates are exclusive to this parent:
replacing a subset of $T$ by its stored equal-sum witness preserves
every compatibility condition.

A fixed local layer and balanced layout give mask families of exact
sizes

$$
W_1=\binom{c/Q_{\rm grid}}{k/Q_{\rm grid}}^{Q_{\rm grid}},\qquad
W_2=\binom{c/Q_{\rm grid}}{(r-k)/Q_{\rm grid}}^{Q_{\rm grid}}.
\tag{215}
$$

Their images and child roles are fixed before top fine-profile
selection. Orient $W_1\le W_2$ and put $B_i=\log_2W_i$.
For every retained strict local layer, the quarter-layer lemma gives
$B_2-B_1<(7/16)c+O(Q_{\rm grid}\log(m+1))$.
The scalar policy gives $c>.53m$, so $R_T<.47m$.
The top allocation supplies movable ancestor factors of total
log-cardinality $M_j\ge m/2-O(Q_{\rm grid}\log(m+1))$ per parent.
These factors consist of allocated top-mask or coefficient choices and
ordinary background coordinates; the local image stays fixed.

Place the entire support array in child 1. Ideal balancing assigns the
movable masses $E_1,E_2$ as follows:

$$
E_1+E_2=M_j,\qquad E_1-E_2=B_2-B_1-R_T.
\tag{216}
$$

Feasibility is equivalent to $|R_T-(B_2-B_1)|\le M_j$.
For strict local cores both nonnegative terms on the left are at most
$.47m+O(Q_{\rm grid}\log(m+1))$, leaving a fixed $.03m$ reserve.
For the oriented-half mode below each is at most $m/2+O(Q_{\rm grid})$, so clamping
the ideal target to the available interval incurs only
$O(Q_{\rm grid}\log(m+1))$ error.

Every small ancestor factor has logarithmic size at most
$2m/Q_{\rm grid}+O(\log(m+1))$; a free coordinate is one factor of
size two. Order the factors and take an initial segment whose product
first crosses the target. The overshoot is at most one factor.
The target comparison is exact: compare the squares of the two
integer partial domain sizes against their fixed total product.
Only ancestor factors and top background move between children;
each local mask family remains in its prescribed child.
The resulting raw child logarithms differ by
$O(m/Q_{\rm grid}+Q_{\rm grid}\log(m+1))$ from

$$
\beta_j=\frac{M_j+R_T+B_1+B_2}{2}.
\tag{217}
$$

The ambient histogram always uses distinct sums of the entire
original full local block $B_j$. The support-array histogram counts
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
atomic factor has logarithmic size $R_T$ above half the child-domain
logarithm, put that factor alone in one leaf. Otherwise start with
that factor and add small factors until first crossing half. A child
without an atom starts with an empty first leaf. Thus the larger leaf
has logarithmic size at most

$$
F_j\le\max\{R_T,\beta_j/2\}
       +O(m/Q_{\rm grid}+Q_{\rm grid}\log(m+1)).
\tag{218}
$$

Enumerate each leaf explicitly and sort it with its full witness.
Repeated weights retain distinct occurrence IDs. The support atom is
the only factor deduplicated by weight at this stage.

Let $\overline\beta$ be the uncompressed central analytic upper
budget for one child. Across $K$ local signings, the filtered-child
budget is $\overline\beta-\ell+\log_2K$, and summed leaf starts have
budget $\max\{R_T,\overline\beta/2\}+\log_2K$.
The active policies satisfy
$\overline\beta-\ell>.56919m$ and
$\overline\beta/2-r>.05959m$ before the declared finite losses.
For strict local cores these follow from
$3/4-(.45+.5-h(.225))>.56919$ and
$3/8-(.45+.25-h(.225)/2)>.05959$;
the oriented-half bounds are larger.
Since $\ell\le r$, $R_T\le m/2+O(Q_{\rm grid})$, and the dictionary exponent is below
$.548m$, the filtered analytic budget pays capacity and both terms
of the summed leaf initialization. This includes empty pruned calls.

For lift accounting we also need the actual unrestricted child domains.
Concavity gives
$B_1+B_2\ge h(\theta)c-O(Q_{\rm grid}\log(m+1))$.
Moreover $N(B_j)\le2^cN(T)$, so $d_T\le d_j$.
Together with $M_j\ge m/2-O(Q_{\rm grid}\log(m+1))$ this yields

$$
2\beta_j\ge\frac{3m}{2}-[1-h(\theta)]c-d_T
                 -O(Q_{\rm grid}\log(m+1)).
\tag{219}
$$

For strict locals $\theta=.45$, and for the oriented-half mode
$\theta=.5$. In either case $1-h(\theta)<.015$ and
$d_T\le d_j\le.203m+O(1)$. Each unrestricted child therefore has
more than $2^{.64m}/\operatorname{poly}(n)$ occurrences after the fixed
cutoff. Interval and prefix restrictions use the upper initialization
budget above.

### II.5.6. Oriented local halves

The main algorithm takes $4\mid m$. Split a local full block into
two fixed equal halves and orient them as $A,T$ so that $N(A)\ge N(T)$.
Move fewer than $2Q_{\rm grid}$ coordinates from $A$ to $T$ so that
$c=|A|$ is a multiple of $2Q_{\rm grid}$.
Removing a coordinate decreases deficiency; adding one increases it.
Thus, writing $d_A,d_T$ for the resulting deficiencies and using
$N(B_j)\le N(A)N(T)$, we retain

$$
d_A\le d_T,\qquad d_A+d_T\le d_j.
\tag{220}
$$

Use the support array of $T$ as the atom. On $A$, enumerate each
prefix signing and its complement. For every original selected mask,
prefix flips change its cardinality by one at a time from its original
size to its complementary size; one attains $|A|/2$.
The selected half $S$ and its complement, in the signed weights, satisfy
$N(S)N(A\setminus S)\ge N(A)$. One of the two complementary signings
therefore gives a selected half with support at least $\sqrt{N(A)}$.
Its natural scale is
$\ell_A=\lfloor\log_2N(A)/2\rfloor$.
Pigeonholing, complementation inside this selected half, and the
balanced-cell construction give a useful smaller layer with only
polynomial support loss.

The two local mask families have total selected size $|A|/2$ and
mean entropy $1/2\le\overline H_A\le h(1/4)$. Their contrast is at
most $c=m/2-O(Q_{\rm grid})$, and $R_T\le m/2+O(Q_{\rm grid})$,
so the allocation above applies. Replacing $c$ by $m/2$ incurs only
$O(Q_{\rm grid})$ in the following resource formulas.
Compared with the uncompressed half-core formula, compression reduces
each balanced child exponent by $d_T/2$ and raw-parent work by $d_T$;
the local filter adds $d_A/2$. The resulting corrections are

$$
(d_A-d_T)/2\le0,\qquad d_A/2-d_T\le0.
\tag{221}
$$

For example, in an ordinary top representation let $a$ be the actual
top size, $\overline H_0$ its actual mean mask entropy, and
$f_0=r_0-\ell_0$ its physical image deficit, where $r_0$ is the
selected top size. Put $h=h(1/4)$ and $u=1-h$.
Before applying the top central-domination inequalities, the filtered
child and raw-parent budgets satisfy

$$
\begin{aligned}
\Gamma_{\rm half}
&\le\frac{3m}{4}+(\overline H_0/2-1/4)a-u\frac m2+O(Q_{\rm grid}),\\
J_{\rm half}
&\le\frac{3m}{2}-(1-\overline H_0)a
       +(2h-3/2)\frac m2+f_0,\\
\Lambda_j&\le\frac{3m}{2}-(1-\overline H_0)a-d_j+f_0.
\end{aligned}
\tag{222}
$$

For a biased selected top fraction $s$, replace the top raw term
$-(1-\overline H_0)a$ by
$-(1/2+s-\overline H_0)a$; the child coefficient stays unchanged.
An outer top-code logarithm is added once to each summed solve budget.
The actual top entropy is retained until its central-domination lemma
is applied. The ambient histogram still uses the original full local
block. The stored-leaf bound is
$\max\{m/2,(1/4+h/4)m+(h/4-1/8)a\}$ up to the declared finite
losses; it is below $.523m$ for $a\le.9m$.

### II.5.7. Fixed granularity and arithmetic

Choose $Q_{\rm grid}$ as a fixed multiple of four, independently of
the input. Required integer divisibilities and layer trimming change
$O(Q_{\rm grid})$ coordinates. Binomial estimates, fixed-power root
enclosures, and the fixed number of count refinements add
$O(Q_{\rm grid}\log(m+1))$ to exponent bounds. Every stored sum,
count, factorial and exact comparison has polynomial bit length in
$n,L$, with fixed constants depending on $Q_{\rm grid}$.

A union of a multiple of four cells approximates an ideal projected
top size within $4m/Q_{\rm grid}$. The small-factor packing above and
the subsequent leaf split each miss their targets by at most
$2m/Q_{\rm grid}+O(\log(m+1))$.
The relevant raw, child, restart and leaf coefficients have absolute
value at most one. Their combined charge is bounded by
$20m/Q_{\rm grid}+O(Q_{\rm grid}\log(m+1))$; the global certificate
uses the conservative allowance

$$
100m/Q_{\rm grid}+O(Q_{\rm grid}\log(m+1)).
\tag{223}
$$

Fix $Q_{\rm grid}=10^{12}$ and then a fixed coordinate cutoff as
specified in the resource certificate. Smaller instances are solved
directly. All factors polynomial in the arbitrary input length $L$
remain explicit polynomial factors. Incidence normalization uses
actual integer product counts.

## II.6. Compatibility and ordered generation

### II.6.1. Assignment containers

The following primitive is deterministic. A zero support uses one empty container. On $n$ coordinates, with ternary support size $k$ and container length $2k\le l\le n$, let
$N_k=\binom nk$, $A_k=\binom lk$, $p_k=A_k/N_k$. Choose

$$
\nu=\left\lceil16(n+1)/p_k\right\rceil,\qquad
L_k=\lceil4\nu p_k+8(n+1)\rceil.
\tag{224}
$$

A multiset of $\nu$ containers can cover every support while giving each support fewer than $L_k=O(n)$ containing indices. For independent random containers, the potential
$\#\{\text{uncovered supports}\}+\sum_B2^{\deg(B)-L_k}$
has expectation
$N_k(1-p_k)^\nu+N_k2^{-L_k}(1+p_k)^\nu<1$.
Indeed $N_k\le2^n$, $\nu p_k\ge16(n+1)$, $1-p_k\le e^{-p_k}$ and $\log_2(1+p_k)\le2p_k$ bound each term by less than $1/2$.
Fix one container at a time by minimizing its exact conditional expectation. The mean over candidates is the previous value, so the final potential remains below one, forcing complete coverage and every degree below $L_k$. After $i$ choices the conditional expectation is

$$
(1-p_k)^{\nu-i}U_i+
2^{-L_k}(1+p_k)^{\nu-i}\sum_B2^{d_i(B)}.
\tag{225}
$$

For a proposed next container and $s=\nu-i-1$, comparisons use the common-denominator integer score
$2^{L_k}(N_k-A_k)^sU_Y+(N_k+A_k)^s\sum_B2^{d_Y(B)}$.
Its bitlength is $O(n\nu)$. The central binomial bound gives
$N_k/A_k\le(2k+1)\binom nk4^{-k} \le(n+1)\sum_{j=0}^n\binom nj4^{-j}=(n+1)(5/4)^n$.
Schoolbook arithmetic, a scan of all supports for each candidate, and all rounds cost at most
$O^*(2^{2n}\nu^3)=O^*((125/16)^n)<O^*(2^{3n})$.
Support flags/degrees, selected containers and the large operands occupy $O^*(2^n)$ state.

For every selected container $Y$ and binary assignment $s$ on $Y$, use the rectangle consisting of binary $x$ with $x|_Y=s$, and ternary $y$ supported on a $k$-subset of $Y$ with $y_i=(-1)^{s_i}$ on that support. All pairs have binary sums, and every compatible pair is covered. Binary degree, ternary degree and tuple count are respectively

$$
O^*(N_k/A_k),\qquad O^*(2^{l-k}),\qquad O^*(N_k2^l/A_k).
\tag{226}
$$

Build a support-to-container index by enumerating each container's $k$-subsets. Its length is $\nu A_k=O^*(N_k)$, with polynomially many indices per support. A ternary query enumerates just these indices and the permitted assignment extensions. This realizes the degree bound as an actual query-time bound.

For the degree calculation take $t\ge0$; for $t<0$, interchange the two region names and parent roles. Write
$n_\pm=a(1/2\pm z)$, $k_\pm=pn_\pm$.
Set $h=h(p)$, $g=h-3p>0$. Initially use container length $2k_\pm$. The full right degree exceeds the left by $C=2zag$. Enlarge the plus-region container by $w$, keeping the minus-region length unchanged. Define

$$
E(l,k)=l[1-h(k/l)],\qquad
2w-E(2k_++w,k_+)=C.
\tag{227}
$$

The binary degree on the enlarged region decreases by $w-E$, while its ternary degree increases by $w$. Thus (227) equalizes the full parent degrees.

For $p=1/20$ and $|t|\le.06$,
$z\le1/15$. The rational entropy certificate in Section II.8 gives $h(.05)<.2864$, hence $g<7/50$, so

$$
\frac C{k_+}
 =\frac{2z}{1/2+z}\frac gp
 \le\frac4{17}\frac{14}5=\frac{56}{85}.
\tag{228}
$$

For $l\ge2k$, differentiation gives
$E(2k,k)=E_l(2k,k)=0$, $0\le E_l<1$, and
$E_{ll}=k/[(\ln2)l(l-k)]$.
Hence $E(2k+w,k)\le w^2/(4k\ln2)$.
The left side of (227) is strictly increasing with derivative greater than one. At $w=3C/4$,
$E\le63C/(680\ln2)<C/2$, using $\ln2>1/2$;
thus its value exceeds $C$. The unique root satisfies
$0\le w\le3C/4$, and its container fits with fixed slack:

$$
2k_++w\le(2+42/85)k_+=\frac{53}{425}n_+<n_+.
\tag{229}
$$

Both complete checker degrees and the global assignment table therefore have logarithmic bounds

$$
D_{\rm side}=\frac a2[h(p)-p]+\frac E2+O(\log a),
\qquad
\log N_{\rm tup}=a h(p)+E+O(\log a).
\tag{230}
$$

The positive binary-entropy series gives $D(t)\ge2t^2/\ln2$. Combining this with the curvature bound proves, for $t\ne0$,

$$
\frac{E}{2aD(t)}
 \le\frac{9g^2}{32p(1-2p)^2}
 \le\frac{49}{360}<\frac38.
\tag{231}
$$

At $t=0$, use the original containers and $E=0$.
Integer container lengths bracket the monotone degree crossing. Expanding entropy at rational arguments converts each sign test to a comparison of integer powers with polynomial bitlength. Rounding an interior length changes exponents by $O(\log a)$; actual polynomial load caps are retained.

### II.6.2. Support-balanced tensorization

Use four subregions for container construction. For a support $R$ on an $n$-coordinate owner region, remove a residual set $T$ containing $|R|\bmod4$ supported and $(n-|R|)\bmod4$ unsupported coordinates. It has at most six coordinates. Enumerate every such $T$ and its support pattern. The remaining total and support cardinalities are divisible by four.

For any ordered even-size coordinate set with an even support, consider every cyclic interval containing half the coordinates. Its support count changes by at most one when the interval advances by one position. The opposite interval has the complementary support count. Discrete intermediate value therefore gives an interval with exactly half the support. Apply this twice: first divide the remaining region into two equal coordinate/support halves, then divide each half likewise. The four regions have equal coordinate counts and equal support counts.

Enumerating all cyclic choices at these three nodes gives a polynomial family. Every support is balanced by some branch. The residual coordinates remain explicit in all coefficient vectors and actual sums. Their checker enumerates binary assignments, with ternary signs forced on the fixed residual support; its cost is constant.

Suppose the original container ratio is $\gamma=l/k$. In each regular subregion, set $l_i=\lceil\gamma k_i\rceil$. On the active range $k/n$ is bounded away from zero and $1/2$, $l/n$ is bounded below one, and $l/k$ is bounded. Thus all four lengths are feasible after a fixed cutoff. Removing finitely many coordinates and rounding four lengths gives

$$
\begin{aligned}
\sum_i l_i&=l+O(1),&
\sum_i k_i&=k+O(1),\\
\sum_i n_i h(k_i/n_i)&=n h(k/n)+O(\log n),&
\sum_i l_i h(k_i/l_i)&=l h(k/l)+O(\log n).
\end{aligned}
\tag{232}
$$

The tensor rectangles preserve (226) and (230) up to polynomial factors. Their support indices realize the same sided degrees. Construction runs on regions of size $n/4+O(1)$, so it takes
$O^*(2^{3n/4})$ time and $O^*(2^{n/4})$ construction state. The full assignment table, its initialization and clearing structure remain separately charged.

In the active band, $|z|\le1/15$, so the larger owner region has at most $.51m+O(1)$ coordinates. Construction therefore has exponents $.3825m$ and $.1275m$. The rational entropy enclosures from Section II.8,
$h(.05)<.28639696<.2864$ and $D(.06)<.011$, together with (231), give

$$
a h(p)+E
 < .9m[.2864+(3/4)(.011)]+O(\log m)
 =.265185m+O(\log m).
\tag{233}
$$

This includes the tuple table and support incidence indices.

### II.6.3. Exact sided incidence

Combining (176) with the actual-quota form of (230) gives
$M_j+D_{\rm side}\le m/2+\log Q+E/2+O(\log a)$.
For original local full-support deficiency $d_j$, the ambient count after the natural top modulus and summing the threshold group's owners therefore has exponent at most

$$
\frac32m-d_j+d-aD(t)+E/2+O(\log n)
 \le\frac32m-d_j+d-\frac58aD(t)+O(\log n).
\tag{234}
$$

Choosing a least-deficient original full block as top, and extracting without increasing absolute deficiency, gives $d\le d_j$. The independent sorted parent streams charge the two sided incidence counts separately. At a complementary actual weight, one representative per tensor rectangle is sufficient: every pair in that rectangle has binary coefficient sum. Each distinct parent key pays its own incidence degree once.

### II.6.4. All-layer ordinary separators

Let $0<s\le1/2$ be the selected top fraction. Group the retained
fine cells into four equal coarse regions. Their mask counts are
balanced independently of which raw child holds each factor.


For a cell of size $g$, let left and right counts be $kg$ and
$(s-k)g$. A separator must contain the left mask and avoid the right.
Set

$$
\alpha=1+\frac{\ln(2-s)}{\ln(1/(1-s))},\qquad
e(k)=\tfrac12+\alpha(k-s/2).
\tag{235}
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
\tag{236}
$$

The right exponent is $E_s(s-k)$. Put
$X=1-k$, $Y=e-k$, $Z=1-e$, $W=1-s-Y$ and
$G=(\ln2)E_s$. Direct differentiation gives

$$
G''=1/X-\alpha^2/Z+(\alpha-1)^2/W.
\tag{237}
$$

Since $Z/X\le1$ and
$Z/W\le(1+\alpha s)/(1-2s+\alpha s)$,

$$
ZG''\le
-\frac{2(1-s)(\alpha-1)}{1-2s+\alpha s}<0.
\tag{238}
$$

The chosen $\alpha$ makes $G'(s/2)=0$. Both sided degrees are thus
at most $O^*(2^{d_sa})$ after taking products over cells, where

$$
d_s=E_s(s/2)=s-h(s/2)+h(s)/2.
\tag{239}
$$

The family-size exponent is
$T_s(k)=h(e)-(1-s)h((e-k)/(1-s))$.
It is symmetric about $s/2$. Its second derivative has the sign of

$$
(1-s)[(\alpha-1)^2-\alpha^2(1-s)]/4
 +s\alpha^2(\alpha-1)^2(k-s/2)^2.
\tag{240}
$$

At $(k-s/2)^2=s^2/4$, four times this upper bound equals
$(1-\alpha s)P(\alpha)$, where

$$
P(A)=(1-s)-(1-s)(2-s)A-s(1-2s)A^2-s^2A^3.
\tag{241}
$$

For $0<s\le1/2$, $P(\alpha)\le P(1)=s-1<0$.
Hence $T_s$ is concave and $T_s(k)\le T_s(s/2)=s$.
The global tuple table has $O^*(2^{sa})$ entries.

For an integer region, write $c,d$ for its mask counts and $e$
for its separator size, and put

$$
B_g=\binom ge,\quad R_g=\binom{g-c-d}{e-c},\quad
H_L=\binom{g-c}{e-c},\quad H_R=\binom{g-d}e.
\tag{242}
$$

Choose $\nu=\lceil10(g+1)B_g/R_g\rceil$ separators and load caps
$K_j=\lceil2\nu H_j/B_g+4g+8\rceil$. The potential is the number
of uncovered disjoint pairs plus $\sum2^{\deg-K_j}$ over both mask
families. The uncovered-pair term is at most $3^g e^{-10(g+1)}$. Each of the
two degree sums is at most $2^{-3g-8}$ by $\log_2(1+p)\le2p$;
therefore the expected potential is below one.
After fixing some separators, with $r$ choices left, its exact
conditional expectation is

$$
U_i(1-R_g/B_g)^r+
2^{-K_L}A_i(1+H_L/B_g)^r+
2^{-K_R}B_i(1+H_R/B_g)^r,
\tag{243}
$$

where $A_i,B_i$ sum the current degree powers. Enumerate all next
separators and retain one no larger than the mean. A common positive
denominator makes every comparison integral. The final potential
below one gives complete coverage and both load bounds.

There are at most $2^g$ candidates per choice, $\operatorname{poly}(g)2^g$
choices, $3^g$ pair constraints and $2^{g+1}$ degree constraints.
Comparison integers have at most $\operatorname{poly}(g)2^g$ bits.
Schoolbook arithmetic gives $O^*(2^{6g})$ bit time and $O^*(2^{2g})$
state, including the support-to-separator indices. Four coarse regions
therefore cost $O^*(2^{3a/2})$ time and $O^*(2^{a/2})$ construction
state, in addition to the global tuple table $O^*(2^{sa})$.
The geometric families are reused under coordinate relabeling.

Store per-region compatible-index lists and enumerate their Cartesian
product for each parent label. A record pays its sided degree.
At a fixed complementary actual weight, retain one left witness per
tuple and query right witnesses through their compatible tuples.
Every pair in a tuple is disjoint. If a genuine pair shares a tuple,
any stored left representative has that weight and avoids the right
mask. Thus representative replacement preserves every match. Initialize
the table once per layout and clear touched entries by stamps; each
output key incurs one degree charge. At $s=1/2$, the bound is
$d_s=1-h(1/4)$, as used by the high-tail projection.

### II.6.5. Ordered child streams

Let $p\mid P_{\max}$, and impose a child residue modulo $p$. A pair of stored leaf arrays can be streamed in either order

$$
(w\bmod P_{\max},\ w\text{ increasing}),\qquad
((v-w)\bmod P_{\max},\ w\text{ decreasing}).
\tag{244}
$$

Sort the second leaf by its residue modulo $p$, then modulo $P_{\max}$, then actual weight and occurrence ID. For each first-leaf occurrence, find the complementary $p$-slice and regard its pair sums as a row. In the direct order, traverse its residue groups cyclically forward from the first residue crossing the modular pivot, and traverse each residue in increasing actual weight. In the complementary order, traverse cyclically backward from the last residue at the complementary pivot, with decreasing actual weight inside a residue. A heap merges these sorted rows. Begin each cyclic traversal at a whole residue-group boundary, so repeated residues remain contiguous. Empty slices are skipped by their stored indices.

Initialization, arrays and mutable row-heap state are linear in the stored leaf lengths up to polynomial factors. Each advance costs polynomial time. A complete state copy costs its full size and shares only immutable arrays. Occurrence IDs distinguish all repeated values. Mask or coefficient-prefix restrictions are imposed on their fine factors before leaf generation, so they can only decrease the domains.

### II.6.6. The interval band join

Suppose the first child is ordered by $(k,x\text{ increasing})$ and the second by $(k,y\text{ decreasing})$, with equal primary keys imposing the desired parent residue. For an actual-weight interval $[L,U]$, maintain two forward cursors in the second stream. At a first occurrence $(k,x)$, the start cursor is its first same-key occurrence of weight at most $U-x$, or the first later key. The end cursor is its first same-key occurrence of weight strictly below $L-x$, or the first later key. Skip earlier keys in both cursors. Their half-open occurrence-position interval is exactly the set of eligible partners, including tied weights and both interval endpoints. Both cursors move forward because $x$ increases and the thresholds decrease within a key.

Keep a circular buffer containing the last $B$ occurrences consumed by the end cursor. If the partner window has length at most $B$, it is precisely the corresponding suffix of this buffer. Otherwise copy the start state and replay the entire window, then discard the copy. If the mutable state size is $S_0$, there are at most $J_I/B$ such copies, where $J_I$ counts all potential reported pairs in the interval. Thus the join has time and space

$$
O^*(N_1+N_2+B+(S_0/B)J_I+J_I),\qquad
O^*(S_0+B),
\tag{245}
$$

in addition to original leaf initialization. The same upper bound applies to early termination, charging a final copy to its potential window. The buffer persists across primary keys and uses absolute occurrence positions; its full capacity is initialized only once per join. Set $B=C$, where $C$ is the dictionary capacity. The certified leaf bound gives $S_0=O^*(C)$, so each interval call costs
$O^*(F+G+C+J_I)$: $F$ pays leaves and initialization, $G=N_1+N_2$ counts filtered-child occurrences, and $J_I$ includes all raw parent pairs, including local overlaps rejected afterward.

### II.6.7. Original-weight unions over local signings

Fix one parent's outer layout, moduli, top residue and lift. For a local signing mask $D$, set $w_i^D=(-1)^{D_i}w_i$ and $\delta_D=w(D)$. Disjoint signed-core masks $A,B$ reconstruct the original subset $(A\cup B)\oplus D$, with

$$
w((A\cup B)\oplus D)=\delta_D+w^D(A)+w^D(B).
\tag{246}
$$

Use the parent-offset convention: a requested original interval $I$ and parent residue $v$ become $I-\delta_D$ and $v-\delta_D\pmod {P_{\max}}$ inside the signed child join. Restore $\delta_D$ exactly once before key insertion. The top label is unchanged: an indexed mask in ordinary mode or the complete coefficient vector in ownership mode. Any fixed outer top offset in ordinary mode is already included in the branch's target convention; ownership weights are direct original coefficient weights.

A capped query maintains one dictionary of original keys $(w,\text{top label})$. Sequentially enumerate local signings and their cached polynomial lists of residue seeds, run the restricted band join, reject invalid local overlaps, restore the original witness, and insert the key. Stop the whole query at $C+1$ distinct keys. Free a signing's child states before processing the next signing. If generation completes, retain any original witness per key: differing local witnesses use only exclusive coordinates, so top compatibility is unaffected.

Let $F_D$ include all initialization under the cached seeds of signing $D$, let $G_D(v)$ count its filtered-child scans, and let $J_D(I,\pi,v)$ count its raw labeled parent tuples in the requested interval and top-prefix cell. With the polynomial seed multiplicities included, the query costs

$$
O^*\!\left(C+\sum_D(F_D+G_D(v))
                 +\sum_DJ_D(I,\pi,v)\right),
\qquad
O^*\!\left(C+\max_DF_D\right)\text{ live generation space}.
\tag{247}
$$

The single dictionary is shared across all signings. Raw tuples keep their signing, seed and occurrence labels for charging; equal original output keys are deduplicated across those labels.

Every output uses an original subset of the entire exclusive full local block. Consequently its distinct-key histogram $U(v)$ is bounded by the ambient histogram $V(v)$ formed from original full-local distinct sums, allowed top labels and allocated ordinary top-background occurrences. This bound contains no signing multiplicity. Local image/cover preparation is completed before interval recursion; only polynomial seed lists and scalar states are cached per signing, while temporary image and histogram arrays are regenerated sequentially. Their separate preparation costs and cache space are included in the global resource accounting.

### II.6.8. Independent sorted streams

We prove a general conversion for a single parent. Let $U$ be the number of distinct valid original keys, $J$ the number of raw labeled occurrences, and suppose a restricted interval/prefix query has time
$O^*(K+J_{I,\pi})$ and state $S$, including after early termination. For (247),

$$
K=C+\sum_D(F_D+G_D),\qquad J=\sum_DJ_D.
\tag{248}
$$

Choose an integer interval containing all possible original actual weights, with polynomial-bit endpoints; the sum of absolute input weights gives such a bound, enlarged by a constant factor for raw coefficient ranges if necessary. Traverse a binary tree of key cells depth first. A cell is an actual-weight interval and, only at a singleton weight, a top-label prefix. Run its capped query. If it finishes with at most $C$ keys, close the raw generator, sort the completed dictionary, and expose its records. If it reaches $C+1$ keys, discard the dictionary and generator, then split a nonsingleton weight interval at its midpoint. At a singleton weight, split by the next top-label bit. A full label prefix contains at most one key and cannot overflow. For increasing output, visit lower weight intervals first; for decreasing output, visit upper intervals first. Prefix order within a weight may be fixed lexicographically.

Every valid key lies in a unique terminal cell, so it is emitted once. The weight order of cells and sorting within completed dictionaries make the stream globally ordered, with complete equal-weight groups contiguous. A paused stream holds only its completed dictionary and scalar traversal frames. Ancestors retain no dictionaries or raw generator state.

The tree depth $H$ is polynomial in $n+L$, from the endpoint bitlength and the $O(a)$-bit top label. At a fixed depth, overflowing cells are disjoint and each contains more than $C$ valid keys; hence there are at most $U/(C+1)$ such cells. The entire binary tree has $O(1+HU/C)$ nodes, including empty children. Every raw occurrence, valid or invalid, has a well-defined original weight and top label and lies in at most one cell per depth. Thus
$\sum_{\text{cells}}J_{I,\pi}\le O(HJ)$. Sorting completed dictionaries costs $O^*(U)$, giving the total stream bound

$$
O^*(K(1+U/C)+J)\text{ time},\qquad O^*(C+S)\text{ space}.
\tag{249}
$$

This is a total-time bound; it includes empty streams and all starts. Original-weight offsets merely translate a signing's query interval and do not change the unique cell used in the occurrence charging.

Construct the left stream in increasing actual weight and the right stream in decreasing actual weight. Compare a left weight $w_L$ with the increasing transformed right key $t'-w_R$. Advance the smaller key until they agree or a stream ends. At an agreement, consume the entire left weight group into the compatibility tuple table, then the entire complementary right group through that table. The fixed-weight representative argument proves soundness and completeness for ordinary separators or ownership rectangles. Both streams can be suspended during this process because each exposed dictionary was completed after closing its generator. A constant number of dictionaries and one active generation state suffice.

Let $D_L,D_R$ be the respective tuple degrees and $N_{\rm tup}$ the tuple-table size. Each distinct output key undergoes at most one incidence operation; raw duplicates have already been removed. With immutable incidence indices and once-only tuple initialization charged separately, the complete solve therefore satisfies

$$
\begin{aligned}
T=O^*\big(&K_L(1+U_L/C)+K_R(1+U_R/C)
          +J_L+J_R+U_LD_L+U_RD_R\big),\\
S&=O^*(C+S_L+S_R+N_{\rm tup}).
\end{aligned}
\tag{250}
$$

All restart products are sided. The two local signing unions are scanned independently, and the original full-block ambient bounds control their distinct output keys. Generation stamps or touched-entry clearing charge per-weight table reuse to the already counted left incidences. Exact original indexed witnesses are combined at a compatible match and verified in the input instance.

## II.7. Original keys and covers shared across residue lifts

Fix the top representation, a layout, useful local layers, and a
common-good modulus chain. Write $q_0$ for its top modulus, $p_j$ for
the local modulus on side $j$, and $P_{\max}$ for the largest recorded
modulus. All divide $P_{\max}$. Let $C=\lceil2^{q_*m}\rceil$ be the
dictionary capacity specified in Section II.8.

### II.7.1. Restoring keys before taking the union

The original-key identity (246) restores each local center before
deduplication. Ordinary top keys use an indexed mask in the fixed
outer signing; ownership keys use the complete original coefficient
vector. A fixed-key witness can be replaced because all differing
local coordinates are exclusive to that parent.

Let $V_j(v)$ count an ambient family by original parent residue modulo
$P_{\max}$. It consists of every allowed top label, its assigned top
background choices, and every distinct sum of the original full local
block $B_j$. This contains all restored parent keys. For their union,

$$
U_j(v)\le V_j(v),\qquad Z_j:=\sum_vV_j(v).
\tag{251}
$$

The same ambient bound serves every signing. Build its histogram from
the original support stream and the assigned top factors. Retained
keys and witnesses carry their exact indexed masks.

### II.7.2. Exact resource means

For one signing let raw child domains have sizes $L_1,L_2$, which
depend on the layout and permitted masks, not their signed weights.
Let $C_{D1},C_{D2}$ be occurrence histograms modulo $P_{\max}$;
raw occurrences include local overlaps and every generator label.
Fold them modulo $p=p_j$, obtaining $A_D,B_D$. Define

$$
\begin{aligned}
G_D(v,r)&=A_D[r]+B_D[v-\delta_D-r\bmod p],\\
J_D(v,r)&=\sum_{x\bmod P_{\max}:x=r\bmod p}
 C_{D1}[x]C_{D2}[v-\delta_D-x],\\
\mu&=(L_1+L_2)/p.
\end{aligned}
\tag{252}
$$

The mean of $G_D(v,r)$ over $r$ is exactly $\mu$ for every $v,D$.
The quantity $J_D$ counts raw pairs subject to both congruences;
local disjointness is checked after reporting them.

For a top residue $\eta$, put $H=P_{\max}/q_0$. The left lift set
is $\Omega_L=\{v:v=\eta\bmod q_0\}$; the right set consists of
the complementary residues $t'-v$. Here $t'$ includes the entire
fixed top-signing offset. In the ownership case it is the original
target. Put $Z_j(\eta)=\sum_{v\in\Omega_j}V_j(v)$.
For each signing construct a local cover with three costs

$$
\sum_{v\in\Omega_j}G_D(v,r),\qquad
\sum_{v\in\Omega_j}G_D(v,r)V_j(v),\qquad
\sum_{v\in\Omega_j}J_D(v,r).
\tag{253}
$$

Their means are $H\mu$, $\mu Z_j(\eta)$, and
$A_D^{(0)}(\eta_j-\delta_D)/p$, respectively, where
$A_D^{(0)}(s)$ counts unfiltered child pairs of signed total
$s\bmod q_0$, and $\eta_j$ is the prescribed side residue.
Apply (186) using separate normalizers. Summing over signings controls
the union query's scans, diagonal restart products, and raw pairs:

$$
\sum_{D,r\in\mathcal R_D,v\in\Omega_j}
G_D(v,r)U_j(v)
\le\operatorname{poly}(u)K\mu Z_j(\eta),
\tag{254}
$$

where $K$ is the actual local signing count. The cover meets every
translated eligible image, including its unknown solution lift.

For the top cover, first aggregate the integer counts

$$
A_j^{\rm agg}(\eta_j)=\sum_D A_D^{(0)}(\eta_j-\delta_D).
\tag{255}
$$

Use four costs $A_j^{\rm agg}(\eta_j)/p_j$ and $Z_j(\eta)$ for
$j=L,R$. Their uniform means are

$$
\overline J_j=\frac{K_jL_{j1}L_{j2}}{q_0p_j},
\qquad \overline Z_j=Z_j/q_0.
\tag{256}
$$

The top weighted cover bounds each cost by a polynomial times its
own mean and preserves every eligible top representation. Integer
aggregation precedes normalization, so intermediate numerators and
denominators have polynomial bit length. Each local cover uses only
three normalizers at a time.

### II.7.3. Summing the independently generated streams

Let $F_{jD}$ bound leaf initialization for signing $D$, and $d_j$ be
the side's checker degree bound. Section II.6 supplies an independent
ordered stream of distinct parent keys at cost

$$
O^*\!\left[
\left(C+\sum_D(F_{jD}+G_D(v))\right)
\left(1+\frac{U_j(v)}C\right)+\sum_DJ_D(v)
\right].
\tag{257}
$$

Merge the streams in opposite actual-weight order; their costs add.
Summing (257) over lifts and the local and top cover lists gives

$$
O^*\!\left[
\sum_{j=L,R}\left\{
H\left(C+\sum_DF_{jD}+K_j\mu_j\right)
+\left(C+\sum_DF_{jD}+K_j\mu_j\right)
\frac{\overline Z_j}{C}
+\overline J_j+\overline Z_jd_j
\right\}+N_{\rm tuple}\right].
\tag{258}
$$

Allocate the checker table of size $N_{\rm tuple}$ once for a fixed
layout; stamps clear only touched entries between weight groups.
Each distinct parent key incurs one checker-degree charge. The
ambient bound and independent stream construction give exactly the
diagonal restart products in (258).

To construct the costs, fold the ambient histogram on its lift coset
modulo $p$. The resulting seed counts satisfy:

$$
\sum_vG_D(v,r)V_j(v)
=A_D[r]\sum_sV_s+\sum_sV_sB_D[s-\delta_D-r].
\tag{259}
$$

A quadratic cyclic convolution gives the full seed vector. Folding
$C_{D2}$ modulo $q_0$ similarly gives

$$
\sum_{v\in\Omega_j}J_D(v,r)
=\sum_{x\bmod P_{\max}:x=r\bmod p}
C_{D1}[x]C_{D2}^{(q_0)}[\eta_j-\delta_D-x].
\tag{260}
$$

One $P_{\max}$-entry scan fills all seeds. Release one signing's
histograms before preparing the next; cache only its residue list.
Every interval restart reuses that list. Simultaneous state is
$O^*(C+\max_DF_{jD}+P_{\max}+K_L+K_R+N_{\rm tuple})$.

Every lift, including one with empty realized streams, incurs its
startup in (258). The identity

$$
H\mu_j=P_{\max}
\left(\frac1{L_{j1}}+\frac1{L_{j2}}\right)
\frac{L_{j1}L_{j2}}{q_0p_j}
\tag{261}
$$

pays lifted child scans by the raw-pair mean when the unrestricted
balanced child domains exceed $P_{\max}$ by a fixed exponential
factor. Section II.5 proves this for every useful local layer.
The uncompressed analytic child budget in Section II.8 dominates
$C+\sum_DF_{jD}$ in the restart products. The baseline itself is bounded directly in Section II.8, retaining
the local cache and outer-label factors. That bound covers empty
calls separately from the output-dependent restart products.

## II.8. Parameters and complete resource bounds

Normalize the three full blocks to size $m$. Let $x_0$ be the least
full-block deficiency proxy and let $x\ge x_0$ be either local proxy;
each side is analyzed at its own $x$. Use the potential $\beta$ of
Section II.1, with $P_*=23/26$ and $\alpha_*=52/75$. Fix

$$
q_{\rm circ}=\frac{137}{250},\qquad
X=\frac{17}{2000},\qquad T=\frac{27}{200},\qquad
B_{\max}=\frac{203}{1000}.
\tag{262}
$$

The core policies use the design anchor $q_{\rm circ}$. Their actual
dictionary capacity $2^{q_*m}$ is specified below. The scalar functions
$R,Q,F$ bound, respectively, raw-parent time in excess of $3m/2$,
the restart capacity threshold, and stored leaves. The independent-stream
bound of Section II.7 therefore has raw and restart exponents at most
$3/2+R$ and $3/2+Q-q_*$. All terminating decimals in this section are
exact rationals.

### II.8.1. Exact scalar certificates

For the entropy comparisons use

$$
\begin{aligned}
L_-&=2\sum_{j=0}^{23}\frac1{(2j+1)3^{2j+1}},&
L_+&=L_-+\frac{2}{49\,3^{49}}\frac98,\\
S(z)&=\sum_{j=1}^{128}\frac{z^{2j}}{(2j)(2j-1)},&
E(z)&=\frac{z^{258}}{258\cdot257(1-z^2)}.
\end{aligned}
\tag{263}
$$

For $u\in(0,1)$, put $z=|1-2u|$ in the logarithm and entropy bounds:

$$
1-\frac{S(z)+E(z)}{L_-}\le h(u)
\le1-\frac{S(z)}{L_+}.
\tag{264}
$$

These inequalities certify the entropy bounds below. The only implicit
roots needed are

$$
\begin{aligned}
\frac{859560838307}{10^{12}}
&<t(X,.9)<\frac{859560838308}{10^{12}},\\
\frac{515456646931}{10^{12}}
&<t(X,.6305)<\frac{515456646932}{10^{12}}.
\end{aligned}
\tag{265}
$$

At each listed interval endpoint $P_*z-xt>0$. Substitution gives
opposite signs in the increasing root equation
$xt+(P_*-x)t^{52/75}=P_*z$, equivalently in
$t^{52}(P_*-x)^{75}-(P_*z-xt)^{75}$. Thus (265), like
(264), is an integer comparison after clearing denominators.

### II.8.2. Ownership parameters

For $0\le x_0\le X$, put

$$
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
$$

For strict locals $x<T$, use $\phi=.371,.375,.3875$ on the
intervals cut at $.03,.05$. The ownership and local-allocation bounds
of Sections II.3 and II.5 give

$$
\begin{aligned}
R&=-D\rho+e\sigma+\beta(x_0,\rho)+\phi\beta(x,\sigma),\\
Q&=.75-A\rho-r\sigma-x+\beta(x_0,\rho)+\phi\beta(x,\sigma),\\
F&=\max\{1-\sigma,.375+f\rho+v\sigma/2\}.
\end{aligned}
\tag{267}
$$

Here $Q=q_{\rm circ}+R$ whenever $\sigma<1$. Set
$b_t=X(859560838308/10^{12})$. Monotonicity of the potential and
(265) give $\beta(x_0,.9)\le b_t$. Direct substitution gives

$$
.99998<\sigma(X)<1,\qquad \sigma(T)>.53006,
\qquad C-v=.00849648632975<X.
\tag{268}
$$

For $x\le X$, the bounds $\beta(x,\sigma)\le x$ and
$\sigma\le1$ give $R<-.00030765$. Also

$$
Q\le .75-A\rho-r\sigma(X)+\beta(x,\rho)-.629x
<.54769110.
\tag{269}
$$

Indeed $t(x,.9)$ increases with $x$: at fixed $t<1$, the defining
right side $xt+(P_*-x)t^{\alpha_*}$ decreases with $x$.
Thus $\beta(x,.9)\le(859560838308/10^{12})x$ on this interval,
and the affine upper bound in (269) is largest at $X$.
For $X\le x<T$, proportional extraction gives

$$
R\le-D\rho+b_t+\frac{(e+\phi x)(C-x)}v.
\tag{270}
$$

This is a concave quadratic, with critical point
$(\phi C-e)/(2\phi)$ clamped to the relevant interval. Its three
maxima satisfy:

| Interval | Maximum location | Strict upper bound |
|---|---|---:|
| $[X,.03]$ | $29646127739029/2968000000000000$ | $-.00030589$ |
| $[.03,.05]$ | $.03$ | $-.00074738$ |
| $[.05,T]$ | $.05$ | $-.00181446$ |

For example the first exact value is

$$
-\frac{1955191732793963624585813319}{6391714532250880000000000000000}.
\tag{271}
$$
Consequently $R<-.0003$, $Q<q_{\rm circ}-.0003$, and
$F\le.375+f\rho+v/2=.547441072186$; the complementary atom is
below $.47$.

For $T\le x\le B_{\max}$ use oriented halves. With
$h_0=374/461>h(1/4)$ and $U=1-h_0$, their bounds are

$$
\begin{aligned}
R_h&\le-D\rho+(2h_0-1.5)/2+b_t
=-\frac{8711179803779801}{230500000000000000}<-.03779,\\
Q_h&\le .75-A\rho-U/2-T+b_t
=\frac{57308853692168787}{115250000000000000}<.49726,\\
F_h&\le.5.
\end{aligned}
\tag{272}
$$

The inequality for $h_0$ also follows directly from
$3^{1383}>2^{2192}$.

### II.8.3. Biased middle parameters

For $X\le x_0\le T$, set

$$
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
$$

Take $\phi_0=.345$ for $x_0\le.05$ and $.3575$ afterward.
Use the preceding three local values of $\phi$ and, for $x<T$,
$\sigma=\min\{1,(b+C\rho-x)/v\}>.53$. The biased projection
and local allocation give

$$
\begin{aligned}
R&=-D\rho+e\sigma+\phi_0\beta(x_0,\rho)+\phi\beta(x,\sigma),\\
Q&=.75-A\rho-r\sigma-x+\phi_0\beta(x_0,\rho)+\phi\beta(x,\sigma),\\
F&=\max\{1-\sigma,.375+f\rho+v\sigma/2\}.
\end{aligned}
\tag{274}
$$

The top term includes the actual outer code multiplicity. Two useful
bounds on the potential are

$$
\beta(x,z)\le xz^{4/3}\quad(92x\le17P_*),\qquad
\beta(x,z)\le xz^{7/5}\quad(161x\le11P_*).
\tag{275}
$$

To prove the first, substitute $t=z^{4/3}$ and divide the defining
equation by $z$. For $w=z^{1/225}$ the resulting left side is
$xw^{75}+(P_*-x)w^{-17}$, which decreases to $P_*$ on $0<w\le1$
under the displayed hypothesis. The second uses
$xw^{150}+(P_*-x)w^{-11}$ and $w=z^{1/375}$.
Since $T<17P_*/92$ and $.85<.95^3$, the top term satisfies
$\beta(x_0,\rho)<.95x_0\rho$. Locally use
$\beta(x,\sigma)\le x\sigma$.

On the rising top define

$$
\begin{gathered}
B_0=b+.605C=.27504852882943,\quad k=3C=.362224109898,\\
a_c=B_0-v=.00585569981543,\quad
z_c=\frac{a_c}{1-k}=\frac{585569981543}{63777589010200}.
\end{gathered}
\tag{276}
$$

The uncapped domain is $x\ge a_c+kx_0$. There

$$
R\le\overline R=-D\rho+(e+\phi x)\frac{B_0+kx_0-x}v
                      +.95\phi_0x_0\rho.
\tag{277}
$$

At fixed $x$, its $x_0^2$ coefficient is $3(.95)\phi_0>0$.
On a diagonal edge it is
$3(.95)\phi_0+\phi(k-1)/v \ge35091383426981/538385658028000>0$; on the cap edge it is
$3(.95)\phi_0>0$. Hence maxima occur at boundary endpoints or
on a vertical boundary $x_0=z$. On such a boundary the only additional
candidate is $x_*=[b+C\rho(z)-e/\phi]/2$, clamped to that boundary.
Writing $c_X=a_c+kX$, the complete rising-domain certificate is:

| Top interval | Local interval | Vertices | Strict upper $\overline R$ |
|---|---|---|---:|
| $[X,.05]$ | $[X,.03]$ | $(X,c_X),(X,.03),(z_c,z_c),(.03,.03)$ | $-.0001771431$ |
| $[X,.05]$ | $[.03,.05]$ | $(X,.03),(X,.05),(.03,.03),(.05,.05)$ | $-.0006064236$ |
| $[X,.05]$ | $[.05,T]$ | $(X,.05),(X,T),(.05,.05),(.05,T)$ | $-.0016602729$ |
| $[.05,Z]$ | $[.03,.05]$ | $(.05,.05)$ | $-.0046558153$ |
| $[.05,Z]$ | $[.05,T]$ | $(.05,.05),(.05,T),(Z,Z),(Z,T)$ | $-.0040912578$ |

All entries follow by rational substitution at these candidates.
The first maximum occurs at
$x_0=X$, $x=7574073885281873/742000000000000000$.
On the plateau, $\overline R$ increases with $x_0$ at fixed $x$,
so maximize on $x_0=x$. This concave quadratic has critical point
$8011512564987923/62000000000000000$ and value below $-.0037421981$.
Thus the complete uncapped domain satisfies
$R<-1/6000$ and $Q=q_{\rm circ}+R<.5478228569$.

The cap has $X\le x_0\le z_c<.01$ and
$x_0\le x\le a_c+kx_0<.01$. Here $\rho<.64$,
$.01<11P_*/161$, and $.64^2<.84^5$, so (275) gives
$\beta(x_0,\rho)<.84x_0\rho$. Maximize raw work at
$x=a_c+kx_0$ and restart at $x=x_0$ to obtain

$$
\begin{aligned}
R_c&\le-D\rho+e+.84(.345)x_0\rho+.371(a_c+kx_0),\\
Q_c&\le .75-A\rho-r-.629x_0+.345\beta(x_0,\rho).
\end{aligned}
\tag{278}
$$

The first is convex, and substitution at $X,z_c$ gives
$R_c<-.0003827602$. Along $\rho=.605+3x_0$, implicit
differentiation gives

$$
\beta'=t+x_0\frac{t^{\alpha_*}-t+3P_*}
 {x_0+\alpha_*(P_*-x_0)t^{\alpha_*-1}}
\le.635+.01\frac{1+3P_*}{\alpha_*(P_*-.01)}<.7.
\tag{279}
$$

Here $t\le\rho\le.635$. Therefore $Q_c'\le-3A-.629+.345(.7)<0$.
Its maximum is at $X$; the second root bracket in (265) yields

$$
Q_c\le q_{\rm crit}:=\frac{54784907211651059}{10^{17}}.
\tag{280}
$$

Outside the cap the raw-leaf term is $.75-q_{\rm circ}/2+C\rho-x/2$.
It decreases along the rising diagonal; its capped value increases up
to $z_c$. Hence $F<.5477835481$, including the complementary atom
below $.47$.

The biased incidence excess is bounded by

$$
I\le(\tau_0/2)\rho+.95\phi_0x_0\rho-x_0<-.0008968462<-1/1250.
\tag{281}
$$

The expression is convex on each rising piece and decreases on the
plateau. Its endpoint tests are $X,.05,Z,T$, using both coefficients
at $.05$. For $x\ge T$, oriented halves instead give

$$
\begin{aligned}
R_h&\le-D\rho+(2H_Q-1.5)/2+\phi_0\beta(x_0,\rho)<-.0357253886,\\
Q_h&\le .75-A\rho-(1-H_Q)/2-x+\phi_0\beta(x_0,\rho)<.5262657137,\\
F_h&\le\max\{.5,.375+f\rho+(H_Q-.5)/4\}<.5041346134.
\end{aligned}
\tag{282}
$$

Replace the top potential by $.95x_0\rho$ and $x$ by $T$ in $Q_h$.
The rising pieces are convex and the plateau is affine, so the same
endpoint list proves all three bounds.

### II.8.4. Proportional high tail and actual capacity

For $T\le x_0\le x\le B_{\max}$, take $\rho_t=.72$ and use
oriented local halves. Proportional extraction bounds the top deficit
by $\rho_tx_0m$. With $h_0=374/461$, $U=1-h_0$ and
$A_0=1.25-1.5h_0$,

$$
\begin{aligned}
R_t&\le-U\rho_t+(2h_0-1.5)/2+\rho_tB_{\max}/2
=-\frac{17503}{11525000}<-.0015,\\
Q_t&\le .75-A_0\rho_t-U/2-T+\rho_tT/2
=\frac{628599}{1152500}<.54543,\\
F_t&\le\max\{.5,.375+(h_0-.5)(\rho_t+1)/4\}
=\frac{11729}{23050}<.50886.
\end{aligned}
\tag{283}
$$

The ordinary projection lemma applies throughout this closed domain:
$p_0=1-h(1/4)-\xi/2>0$, $p_0\rho_t<1/5$, and its sufficient
reserve $.7p_0\rho_t^2<1-\rho_t$ hold for $0\le\xi\le.203$.
For example $p_0<.19$, so the latter two inequalities follow already
from $.19(.72)<.2$ and $.7(.19)(.72)^2<.28$.

The largest resource threshold is (280). Choose

$$
\begin{gathered}
q_*=q_{\rm crit}+10^{-9}
=\frac{54784907311651059}{10^{17}},\\
B_*:=.75-q_*=\frac{20215092688348941}{10^{17}}<.203.
\end{gathered}
\tag{284}
$$

For a full-block support of size $N$, the integer test
$m-\lfloor\log_2N\rfloor\ge B_*m$ implies true deficiency
$d\ge B_*m-1$. The high-deficiency interval algorithm then has

$$
T=O^*(2^{n/2}+2^{n/4}U/C),\qquad
S=O^*(2^{n/8}+C),\qquad
U\le O^*(2^{n/2-d}),\quad C=\lceil2^{q_*m}\rceil.
\tag{285}
$$

The identity $q_*+B_*=3/4$ bounds its restart term by $O^*(2^{n/2})$.
Every remaining profile lies within the certified domain through
$B_{\max}$ after the fixed cutoff.

### II.8.5. Construction, startup, and state

The linear signing-code construction of Section II.2 has exponent
$(1+\theta)c+\phi d$ and is shared before outer top enumeration.
For strict locals, the uniform envelope

$$
\sigma\le\min\{1,(C_*-x)/v_*\},\qquad
C_*=.30463325,\qquad v_*=.26919
\tag{286}
$$

gives code cost at most $\sigma(1.45+.3875x)$. It increases to
$x_*=C_*-v_*=.03544325$ and decreases thereafter, with maximum
$1.45+.3875x_*<1.464$. The actual local and outer label rates obey

$$
\begin{gathered}
\kappa_j<.00723+.3875T=.0595425,\qquad
\kappa_0<.85(.01855+.3575T)=.056790625,\\
\kappa_{\rm owner}\le.9X=.00765.
\end{gathered}
\tag{287}
$$

Physical integer layers and layouts precede prime selection. For the
joint local universe $(D,\mathrm{Good}T,\text{layer},\text{layout})$,
test Good membership with the selected set outside the signing loop.
The inequality $K|\mathrm{Good}|\le\operatorname{poly}(n)2^c$
then bounds a candidate scan by $O^*(2^{c+r})$. Prime depth $16$
therefore gives exponent $1+.45+.45/16=1.478125$.
Both physical local images are fixed before allocating a top fine profile;
the owner-dependent work pays its actual outer multiplicity.

The retained layers also have uniform physical cardinality bounds.
For the biased top, $\delta/A\le.3575T+O(\log A/A)<s/8$;
for a strict local, $\delta/c\le.3875T+O(\log c/c)<.45/8$.
Every useful layer has entropy at least $7/8-o(1)$, whereas
$3^9>2^{14}$ gives $h(1/4)<5/6$. Orient the layer so that
$k\le r/2$ and retain $k\ge r/4$.
For top layers, $k>.1A$ and $r-k>.2A$. The exact inequalities
$10^{20}>2^9 9^{18}$ and $5^{10}>2^{23}$ give mean top entropy
above $23/40$. For strict locals, $k\ge(.1125-o(1))c>c/9$ and
$r-k\le(.3375+o(1))c<.35c$; the inequalities $9^6>2^{19}$ and
$20^{80}<2^{75}7^{28}13^{52}$ give contrast below $7/16$.
Together with $c>.53m$, this leaves at least $.03m$ reserve for
atomic allocation. These restrictions retain a representation of every
witness and depend on coordinate counts alone.

The remaining construction bounds, including their indicated label
multiplicities, are:

| Operation | Time exponent per $m$ |
|---|---:|
| Weighted ownership construction | $1.3653$ |
| Ownership top weighted covers | $<1.42317$ |
| Biased top linear code and top primes | $<1.293$ |
| Shared local linear codes | $<1.464$ |
| Shared physical-image local primes | $1.478125$ |
| Top-dependent local weighted covers | $<1.465$ |
| Signing histograms and full-support replay | $<1.057$ |
| Four-region tensorized containers | $.3825$ |
| Cached local and top layout families | $\le1.45$ |
| Ordinary high-tail separators | $1.08$ |
| Full-block counting and extraction | $1$ |

Here the ownership rows use, respectively,
$1.5(.9)+2(.9X)$ and $(1+2h(.05))(.9)+.9X$.
The biased top code costs at most $1.42(.85)+.3575(.85)T$;
its weighted covers cost at most $1.42(.85)+\kappa_0$, and adding
$.45/16$ bounds prime selection by $1.293$.
The local weighted-cover maximum is below
$1.45+.635(.01855+.3575(.01))=1.464049375$:
its diagonal core policy leaves the cap before $.01$, after which
the core-size derivative is below $-2.3$ and the conservative outer-rate
derivative below $.448$.
Histograms pay $K_0K_j(P_{\max}^2+P_{\max}+2^{m-c})$;
they are regenerated one signing at a time.
The layout family costs are at most $1.45$, $.85(317/200)=1.34725$,
and $.72(317/200)=1.1412$, using $3^{200}<2^{317}$.
The four-region ownership container has maximum region $.51m$,
giving preparation exponents $3(.51)/4=.3825$ in time and $.51/4=.1275$
in space.

For pure lift scans and starts, $\log_2P_{\max}\le.45m+O(\log(n+L))$
and the single-sign uncompressed child budget is below $1.122m$.
The local prime scales satisfy
$\log_2p_j\ge(.45-.3875T)(.53)m-O(\log(n+L)) =.210774375m-O(\log(n+L))$ for strict locals and
$\log_2p_j\ge(.25-B_{\max}/4)m-O(\log(n+L)) =.19925m-O(\log(n+L))$ for oriented halves.
The latter have local signing rate zero. Separating these modes gives

$$
\begin{aligned}
\text{strict:}\quad&.45+1.122-.210774375+.05955+.057
 =1.477775625,\\
\text{half:}\quad&.45+1.122-.19925+.057=1.42975,\\
\text{capacity and leaf starts:}\quad&.45+.548+.05955+.057
 =1.11455.
\end{aligned}
\tag{288}
$$

All three are strictly below $3/2$. In restart products
the declared analytic filtered budget exceeds $.56919m$ and its leaf-minus-shell gap exceeds
$.05959m$. They pay capacity and summed initialization even for empty
pruned streams. For completeness, the two comparisons follow from
$3/4-(.45+.5-h(.225))>.56919$ and
$3/8-(.45+.25-h(.225)/2)>.05959$.
The actual unrestricted child entropies exceed $.64m$, above
$\log_2P_{\max}$; hence the exact product identity of Section II.7
also charges every lift for every modulus ordering.

Additional state has exponent at most $.5$ for supports and atoms,
$.45$ for ownership traces and residue arrays, $.265185$ for ownership
tuples, $.357$ for biased tuples, $.36$ for high-tail tuples,
$.1275$ for tensor preparation, $.0595425$ for local caches, and
$.057$ for outer labels. For the ownership tuple bound use
$.9[h(.05)+.75D(.06)]<.265185$, where
$27/2600<D(.06)<.011$ follows from (264). Each parent keeps one
dictionary of capacity $2^{q_*m}$; constantly many simultaneous arrays
add their sizes.

Finally choose

$$
Q_{\rm grid}=10^{12},\qquad
\varepsilon_{\rm fin}=200/Q_{\rm grid}=2\cdot10^{-10}.
\tag{289}
$$

The fixed grid contributes at most $100m/Q_{\rm grid}$, and a fixed
coordinate cutoff bounds alignment, root-enclosure and combinatorial
losses by another $100m/Q_{\rm grid}$. This total is below
$q_*-q_{\rm crit}=10^{-9}$ and all other strict resource margins.
The preceding scalar bounds pay raw reports and restarts, while the
exact ownership and ordinary-half incidence normalizations give
$O^*(2^{3m/2})$ time. Biased incidence has the margin (281).
All construction costs and the scan/start bounds (288) are strictly
below $3/2$; their margins absorb the stated finite losses.
Thus all phases use time $O^*(2^{3m/2})$ and writable-bit space
$O^*(2^{q_*m})$, with the polynomial factors in the full input length
retained. Since $n=3m+O(1)$, the space exponent is exactly
$q_*/3=18261635770550353/10^{17}$.

## II.9. Complete algorithm and proof of Theorem 2

Enumerate at most twenty-three leftover coordinates so the remaining
instance has $3m$ coordinates with $8\mid m$. Its weights are still
arbitrary signed integers. A fixed small-coordinate range is handled
directly. Split the remaining coordinates into three full $m$-blocks,
and compute their exact supports $N_j$. Put
$\widehat d_j=m-\lfloor\log_2N_j\rfloor$, so
$d_j\le\widehat d_j<d_j+1$. Let $q_*,B_*,X,T$ be the exact
constants in Section II.8.

### II.9.1. A full block above the deficiency threshold

If some $\widehat d_j\ge B_*m$, place that entire block in a
coordinate half and fill the half arbitrarily. Its distinct support
has size $U\le2^{3m/2-d_j}$, with $d_j\ge B_*m-1$.
Use capacity $C=\lceil2^{q_*m}\rceil$.

Store raw eighth lists and generate each raw quarter as a sorted pair
stream. The band join of Section II.6 produces requested half-weight
intervals. Bisect an overflowing left interval, deduplicating by actual
weight; a singleton interval contains one key. For a fitting dictionary,
scan the complementary right interval and test exact membership.
The intervals on either side are disjoint at each recursion depth.

There are $O^*(1+U/C)$ starts, each scanning at most $2^{3m/4}$
quarter records, and at most $2^{3m/2}$ raw half pairs per depth.
Only the eighth lists and bounded dictionaries are stored. Therefore

$$
T=O^*\!\left(2^{3m/2}+2^{3m/4}U/C\right)
 =O^*(2^{3m/2}),\qquad
S=O^*(2^{3m/8}+C).
\tag{290}
$$

The equality uses $q_*+B_*=3/4$ and the one-bit threshold tolerance.
Store a mask with each retained weight to recover its witness.

### II.9.2. The low-deficiency cases

Otherwise choose a largest-support full block as top and let
$x_0=\widehat d_0/m$. Each local proxy $x$ lies in
$[x_0,B_*)$. Use the exhaustive policy

| Top proxy | Representation | Top-base fraction |
|---|---|---:|
| $0\le x_0\le X$ | Equal-rate variable ownership, $p=1/20$ | $.9$ |
| $X\le x_0\le T$ | Biased shell, $s=.42$ | $\min(.605+3x_0,.85)$ |
| $T\le x_0<B_*$ | Half-selected top | $.72$ |

At a shared boundary either mode is valid. Choose each strict base
before its useful layer, rounding its size down to the required fixed
multiple. On either local side, $x<T$ uses the strict shell
$\theta=.45$ and its own certified core fraction; $x\ge T$ uses
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
$O^*(2^{3m/2})$. Actual code and owner multiplicities are paid in
their respective loops. Only shared unsigned preparations are performed
once. The state bound includes every support atom, raw leaf, copied
heap, ring, residue array, cache, assignment index, tuple representative
and dictionary. Multiple simultaneous objects add their sizes.
The fixed grid and coordinate cutoff leave the stated positive reserve
above the critical capacity. All arithmetic, sorting, sieving and
conditional comparisons have the bit costs already charged; factors
polynomial in arbitrary full input length remain explicit.

Since $n=3m+O(1)$, the resulting bounds are

$$
\begin{gathered}
T=\operatorname{poly}(n,L)2^{n/2},\qquad
S=\operatorname{poly}(n,L)2^{E_Sn},\\
E_S=\frac{18261635770550353}{10^{17}}.
\end{gathered}
\tag{291}
$$

This proves Theorem 2, including indexed witness recovery.

## Acknowledgments

OpenAI Codex, including GPT-6 Astra, assisted with proof development, numerical certificates, verification code, literature review, and manuscript preparation.

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
