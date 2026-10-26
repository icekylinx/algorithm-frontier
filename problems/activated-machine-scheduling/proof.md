# Scheduling on an activated matroid basis with one shared budget

## 1. Model and results

Let $P$ be $q$ physical machines and let $M$ be a rank-$r$ matroid
on $P$. The activated set must be an actual basis $B$ of $M$.
Resource type $j$ has a normalized monotone integral submodular rank
$f_j$ and original mandatory count $n_j=f_j(P)$. A schedule consists
of integer vectors $x_j\in B(f_j)$ with $x_j(p)=0$ outside $B$.
Processing times $\ell_{pj}$, assignment costs $a_{pj}$, and machine
setup fees $\sigma_p$ are nonnegative rationals. Eligibility masks are
allowed. The original budget is

$$
\sigma(B)+\sum_{p,j}a_{pj}x_j(p)\le C,\qquad C\ge0. \tag{AS1}
$$

The original $n_j$ remains mandatory after every eligibility or
activation mask. Let OPT be the minimum makespan of a legal schedule.
The binary input size $H$ includes paid polynomial matroid, rank,
submodular-minimization, exact LP and polymatroid-intersection work.

For rational $0<\varepsilon\le1$, put

$$
\delta=\varepsilon/2,\quad K=\lfloor1/\delta\rfloor,\quad
 L_\delta=\left\lceil\frac{1-\delta}{\delta^2}\right\rceil,\quad
 C_\varepsilon=\binom{L_\delta+K}{K},\quad
 \Pi_\varepsilon=\min\{C_\varepsilon,\exp(3(K+1))\}. \tag{AS2}
$$

Also let $H_\varepsilon=H+\mathrm{size}(\varepsilon)$, including
the entire rational numerator and denominator.

**Theorem AS (activation adapter).** A deterministic algorithm detects
global budget infeasibility or returns a legal activated-basis schedule.
The following guarantee/time pairs are available, all with polynomial
workspace in the displayed input:

| Makespan guarantee | Time |
| --- | --- |
| $(1+\varepsilon)\mathrm{OPT}$ | $\binom qr\Pi_\varepsilon^r\mathrm{poly}(H_\varepsilon)$ |
| $\tfrac32\mathrm{OPT}$ | $\binom qr6^r\mathrm{poly}(H)$ |
| $\gamma_k\mathrm{OPT}$, $\gamma_k=(3\cdot2^k-1)/(2^{k+1}-1)$, integer $k\ge0$ | $\binom qr(k+1)^r\mathrm{poly}(H+k)$ |

In particular the first bound is
$2^{O(q+r/\varepsilon)}\mathrm{poly}(H_\varepsilon)$, hence
$2^{O(q/\varepsilon)}\mathrm{poly}(H_\varepsilon)$.
Every original job total and the single shared budget remain exact.

The rank-sensitive enumeration in the table fixes the active basis
before generating profiles. Summing over all possible cardinalities
recovers the coarser bounds $(1+\Pi_\varepsilon)^q$, $7^q$, and
$(k+2)^q$, respectively. For one given rank, the displayed binomial
bounds are at least as strong.

## 2. Initialization and the zero optimum

**Lemma 1 (exact feasibility).** Global feasibility with unbounded load,
and feasibility at makespan zero, can each be decided in
$\binom qr\mathrm{poly}(H)$ time and polynomial space.

**Proof.** Stream all $r$-subsets of $P$. Reject nonbases by a rank
test and bases with $\sigma(B)>C$. For each remaining basis, restrict
every original resource to eligible pairs on $B$, retaining total
$n_j=f_j(P)$. If a masked resource has smaller full rank, reject it.
Otherwise minimize assignment cost over the product of these original
resource bases. The product is integral, so its minimum has an integral
optimizer. Accept precisely when this cost is at most $C-\sigma(B)$.

Every accepted output is a legal original schedule. Conversely every
legal activated-basis schedule appears in one enumerated basis and
certifies that basis's cost test. This proves the unbounded-load test.
Adding the mask $\ell_{pj}=0$ proves the zero-load test. Both tests
stream one subset and one polynomial optimization workspace. $\square$

A minimum-setup basis alone is insufficient: it may lack recipient
capacity for the mandatory jobs. The lemma tests both costs and original
totals. If all job totals are zero, choose any affordable basis and return
zero load. Rank $r=0$ is feasible exactly when all mandatory totals are
zero, since no machine is active.

## 3. Fixed-basis profiles and joint integral recovery

Fix a positive target $T$, a genuine basis $B$, and its residual
assignment budget $C-\sigma(B)$. All coordinates outside $B$ are zero.

Use one of the following finite active-machine profile families:

1. The [arbitrary-processing scheme](../arbitrary-processing-scheduling/proof.md)
   has at most $\Pi_\varepsilon$ profiles per active machine and gives
   load at most $(1+\varepsilon)T$.
2. The [six-profile construction](../six-profile-three-halves/proof.md)
   has six profiles per active machine and gives load at most $3T/2$.
3. The [bucket construction](../processing-bucket-tradeoff/proof.md)
   has $k+1$ profiles per active machine and gives load at most
   $\gamma_kT$.

In each construction every full target-$T$ schedule supplies a valid
profile at each of its machines. Each fixed profile defines one rational
LP and one integral machine-cap polymatroid for rounding. Original
resource constraints continue to couple all active machines.

**Lemma 2 (activation preserves the profile guarantee).** A feasible
fixed-basis profile LP gives an integer schedule of the corresponding
load bound and total cost at most (AS1). If a full target-$T$ original
schedule exists on $B$, some enumerated profile LP is feasible.

**Proof.** The profile LP includes every original type total, the masked
resource ranks, the profile constraints, and budget $C-\sigma(B)$.
The profile construction supplies an integral machine-cap polymatroid
containing its fractional witness. Intersect it with the direct sum of
the masked resource polymatroids and require total $N=\sum_jn_j$.
Every resource total is at most its original $n_j$; therefore total
$N$ forces every original total separately. This is a maximum-total
face of an integral polymatroid intersection.

Minimize actual assignment cost on that face and choose an integral
optimizer. Its cost is no larger than the fractional witness's cost.
All profile load estimates apply to that same integer point. The basis
$B$ remains fixed, so adding its unchanged setup fee gives (AS1).

For completeness, the actual bin counts or labels of a full target
schedule provide one enumerated profile. The unchanged schedule
satisfies its joint LP, with the same resource totals and cost.
No resource is duplicated between profiles or machines. $\square$

There are at most $\binom qr$ tested basis candidates and at most
$\Pi_\varepsilon^r$, $6^r$, or $(k+1)^r$ joint profiles per basis.
Tests of nonbases and failed profiles cost polynomial work. The profile
families are generated only on occupied input bins and streamed as in
their proofs; an accuracy-sized table or unit-copy expansion is
unnecessary. Lemmas 1 and 2 therefore give the table's all-input bounds.

## 4. Exact target optimization

After Lemma 1 has supplied a feasible schedule and rejected target zero,
choose a rational grid $g>0$ dividing all positive processing times.
A common denominator followed by an integer gcd computes $g$ with
polynomial encoding. Every integer schedule load and OPT lies on the grid.

Initialize a failed lower target zero and an upper grid target equal
to the saved feasible schedule's makespan. At a grid midpoint $T$,
run the complete basis/profile search. Total failure implies OPT $>T$
by Lemma 2 and raises the lower endpoint. A success saves its actual
schedule and lowers the upper endpoint. If the approximation coefficient
is $\rho$, the saved schedule always has makespan at most $\rho U$.

When the endpoints are adjacent, $U=L+g$ and $L<\mathrm{OPT}$ imply
$U\le\mathrm{OPT}$. The saved schedule thus has makespan at most
$\rho\mathrm{OPT}$. This argument requires no monotonicity of relaxed
successes and incurs no extra accuracy loss. The initial upper load is
at most $(\sum_jn_j)\max_{p,j}\ell_{pj}$, so the number of target calls
and every target encoding are polynomial. This proves Theorem AS.
$\square$

The same proof applies to any fixed-cardinality activation family with
a polynomial membership test, replacing the matroid-basis test. Several
independent exact assignment budgets require a different recovery
argument: the integral-face step above minimizes one scalar objective.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
