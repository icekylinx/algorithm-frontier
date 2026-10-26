# Arbitrary unrelated processing times: a bucket-label scheduling tradeoff

Processing times here are arbitrary nonnegative rationals. All original
job-polymatroid bases remain mandatory, and one assignment-cost budget
is exact. The algorithm includes factor 5/3 in 2^q polynomial time,
where q counts physical machines. This is an exponential-time theorem,
not a polynomial-time improvement for general unrelated scheduling.

## 1. Model and theorem

Let P be q>=1 machines. Each type j has a normalized monotone integral
submodular recipient rank f_j, with mandatory original count

$$
n_j=f_j(P),\qquad N=\sum_jn_j.
 \tag{AB1}
$$

A schedule has integer x_j in B(f_j). Each eligible pair (p,j) has
arbitrary nonnegative rational processing time ell_pj and assignment
cost c_pj. A supplied additional eligibility mask never reduces n_j.
The budget is

$$
\sum_{p,j}c_{pj}x_j(p)\le C,\qquad C\ge0.
 \tag{AB2}
$$

OPT is the minimum maximum machine load over these schedules. H
includes binary data and paid polynomial rank, SFM, LP and intersection
work. No unit of a binary count is expanded.

For integer k>=0 define

$$
\gamma_k=\frac{3\cdot2^k-1}{2^{k+1}-1}=\frac32+\frac1{2(2^{k+1}-1)}.
 \tag{AB3}
$$

**Theorem AB.** A deterministic algorithm either detects infeasibility
even without a load bound, or returns a legal schedule of makespan at
most gamma_k*OPT, with all original totals and the budget exact, in

$$
(k+1)^q\operatorname{poly}(H+k)\text{ time},\qquad \operatorname{poly}(H+k)\text{ space}.
 \tag{AB4}
$$

| k | Approximation | Exponential time factor |
| --- | --- | --- |
| 0 | 2 | 1 |
| 1 | 5/3 | 2^q |
| 2 | 11/7 | 3^q |
| 3 | 23/15 | 4^q |
| 4 | 47/31 | 5^q |

For rational epsilon>0, choosing k with the last term of AB3 at most
epsilon gives factor 3/2+epsilon in

$$
\bigl[O(1+\log(1+\varepsilon^{-1}))\bigr]^q\operatorname{poly}(H_\varepsilon).
 \tag{AB5}
$$

where H_epsilon=H+size(epsilon) includes the complete binary numerator
and denominator of the supplied rational accuracy. A rational close
to one can have a long encoding even when log(1+1/epsilon) is small.

The explicit AB3--AB4 tradeoff is primary. No finite k is asserted to
attain exact factor three halves by this construction.

## 2. One full-total minimum-cost recovery

Use one coordinate per eligible machine-type pair. The direct sum of
the resource polymatroids is integral. After any pair mask, type j has
rank at most n_j, but we still require

$$
\sum_{p,j}x_j(p)=N.
 \tag{AB6}
$$

Thus every type attains its own original n_j. One type cannot compensate
for another type's missing mandatory units.

Intersect this resource direct sum with an integral machine-cap
polymatroid. The intersection is integral, and its maximum-total face
at N is integral. A fractional point of total N and cost at most C
therefore guarantees an integer point of no larger cost: minimize the
actual scalar assignment cost on that face. We do not add a budget row
to an integral polytope and assume its intersection remains integral.
All rank and cap values are kept in binary.

## 3. Upper-prefix rounding inside a group

For one machine group G, order pair coordinates e_1,...,e_m by
nonincreasing time v_1>=...>=v_m>=0. Given a fractional x, put

$$
X_h=\sum_{i\le h}x(e_i),\qquad U_h=\lceil X_h\rceil.
 \tag{AB7}
$$

The integer prefix caps x'(e_1,...,e_h)<=U_h, including the full
prefix, define an integral chain polymatroid. Its explicit rank is

$$
r_G(S)=\max\{U_h:e_h\in S\},\qquad r_G(\varnothing)=0.
 \tag{AB8}
$$

The U_h are nondecreasing. If h is the largest index in S, the prefix
cap bounds its count by U_h; conversely prefix sets are among the rank
constraints. The maximum-weight rank in AB8 is normalized, monotone
and submodular, with a polynomial rank oracle and no slot expansion.

With v_(m+1)=0, summation by parts gives

$$
\begin{aligned}
 \sum_iv_ix'(e_i)
 &=\sum_h(v_h-v_{h+1})x'(\{e_1,\ldots,e_h\})\\
 &\le\sum_h(v_h-v_{h+1})\lceil X_h\rceil\\
 &\le\sum_iv_ix(e_i)+v_1.
 \end{aligned}
 \tag{AB9}
$$

Empty groups contribute zero. Zero processing times also cause no
problem: their coefficient differences vanish, while AB6 still
preserves their mandatory counts. Disjoint chains and big-job cap
groups will be combined in one machine direct sum.

## 4. Exact labels and thresholds

Fix T>0 and k>=1. Write D=2^(k+1)-1 and set

$$
\ell_i=\frac{2^k+2^i-1}{2^{k+1}-1},\qquad 0\le i\le k.
 \tag{AB10}
$$

These O(k)-bit rationals satisfy

$$
\frac12<\ell_0=\gamma_k-1<\ell_1<\cdots<\ell_k=1,\qquad
 \ell_i+2(1-\ell_{i-1})=\gamma_k\quad(1\le i\le k).
 \tag{AB11}
$$

Give each machine one label in {0,1,...,k}.

Label zero permits only pairs with ell_pj<=l_0*T, and its fractional
total load is capped at T.

Label i>=1 permits only two disjoint groups:

- Big: l_(i-1)*T < ell_pj <= l_i*T, with total count at most one.
- Small: 0<=ell_pj<=(1-l_(i-1))*T, with fractional load at most
  (1-l_(i-1))*T.

Every other pair is forbidden. The groups are disjoint because
l_(i-1)>1/2. In particular every retained big pair has ell_pj<=T;
this upper bound is essential. At k=0 there is only label zero,
l_0=1, and the usual LP load bound T on pairs of time at most T.

## 5. Fixed-label LP and its legal integer output

For a fixed label vector, mask each original resource rank to its
allowed pairs, retaining original equalities x_j(P)=n_j. Add AB2 and
the machine constraints of Section 4. Solve this bounded rational LP
exactly. Empty LPs are skipped. Masked rank loss below n_j, insufficient
capacity, and insufficient budget cannot reduce mandatory counts.

Counts are bounded by original resource ranks. Exact rank separation
uses paid submodular minimization; all rows, labels, extreme-point
witnesses and LP operations have polynomial bit complexity in H+k.

For a feasible x, construct the machine polymatroid as follows. A
label-zero machine gets an upper-prefix chain on all allowed pairs.
A positive-label machine gets a count cap one on its big group and
a separate upper-prefix chain on its small group. These groups are
disjoint, so their direct sum is integral. The fractional x belongs
to it and to the single resource direct sum at total N.

The full-total minimum-cost primitive returns integer x' with all
original totals and cost at most C. By AB9, label-zero load is at most

$$
T+\ell_0T=\gamma_kT.
 \tag{AB12}
$$

At a label-i machine the big contribution is at most l_i*T. The small
fractional load and maximum allowed small processing time are each at
most (1-l_(i-1))*T. Its integral total load is therefore at most

$$
[\ell_i+2(1-\ell_{i-1})]T=\gamma_kT.
 \tag{AB13}
$$

No lower bound of one on big count is required: an empty big group
only improves load. All jobs are rounded jointly, no resource is
duplicated, and no mandatory assignment is discarded.

## 6. Every full target schedule supplies a label vector

Suppose an original integer schedule has makespan at most T and cost
at most C. Each machine either has no job above l_0*T or has exactly
one such job, since l_0>1/2. In the first case choose label zero.
In the second case its unique large job belongs to one of the intervals
(l_(i-1)*T,l_i*T], which partition (l_0*T,T]. Choose that label.

Every other job, and their total load, is at most T minus the actual
large processing time, strictly below (1-l_(i-1))*T. Those jobs all
belong to the small group, and the original large unit obeys cap one.
Thus the unchanged complete original schedule is feasible for one
enumerated LP, with identical resource bases and cost.

Enumeration of all (k+1)^q label vectors therefore succeeds with
makespan at most gamma_k*T whenever the full target T is feasible.
Total failure implies OPT>T. A weak success need not certify full
target-T feasibility, and no such claim is made.

## 7. Initialization, zero processing and exact target optimization

First minimize assignment cost over the original resource bases on
eligible pairs, keeping every n_j. If full totals are infeasible or
their minimum cost exceeds C, the original instance is infeasible
even with unbounded makespan. Otherwise retain the integral minimum-
cost schedule. It gives a finite feasible upper load. When N=0 the
empty schedule is optimal under C>=0.

Test target zero exactly by restricting to zero-time pairs and using
the same original full-total minimum-cost optimization. On success,
return a load-zero schedule. On failure, OPT>0, so zero is a certified
failed lower endpoint. This step is necessary when zero times occur.

Choose a positive rational g dividing every positive finite input
processing time, for example by a common denominator and an integer
gcd of scaled numerators. Its bit length is polynomial in H. Every
integer schedule load and OPT lie on g times the nonnegative integers.
If there are no positive times, the zero test has already resolved
the feasible instance.

The retained schedule gives an upper grid target U and a saved legal
output; zero gives L=0. At grid midpoints run full label enumeration.
Failure raises L; weak success lowers U and saves its actual schedule.
Every failure implies its target is strictly below OPT, so L<OPT
throughout. At adjacent endpoints U=L+g, grid integrality implies
U<=OPT. The saved schedule has makespan at most gamma_k*U and hence
at most gamma_k*OPT. No monotonicity of weak successes is assumed.

The initial upper load is at most N times the maximum finite eligible
processing time. Consequently the number of target calls is polynomial
in binary encoding length, with no numeric expansion of N or 1/g.
There is no extra approximation loss from this search.

## 8. Complete time, space and the limiting curve

Each label vector uses polynomial LP, chain construction, polymatroid
intersection and scalar cost work. Coefficients have O(k) bits.
Labels are streamed with a radix-(k+1) counter; only the current
workspace and best schedule are stored. Polynomially many target
calls prove AB4 and polynomial space. The case k=0 is polynomial.

AB3 gives k=O(1+log(1+1/epsilon)) for the requested excess epsilon,
proving AB5. A finite number of these labels does not attain the
limiting factor three halves.

There is also an exact scope-limited optimality observation. Within
this contiguous one-big-group template, if the only recovery bounds
are 1+l_0 and l_i+2(1-l_(i-1)), a common bound gamma requires

    l_0<=gamma-1,   l_i<=2l_(i-1)+gamma-2.

Induction yields

    l_k<=(2^(k+1)-1)gamma-(3*2^k-2).

Covering all large sizes up to one requires l_k>=1, so gamma>=gamma_k.
AB10 attains equality. This is optimality of the stated template and
analysis only, not a lower bound on scheduling algorithms.

## 9. Scope, public background and limitations

The theorem allows arbitrary pair-dependent processing, arbitrary
job-polymatroid bases, binary job counts, eligibility masks, and one
exact assignment budget. It does not allow an input-sized list of
independent exact costs on the same assignment, optional discarded
jobs, or arbitrary common-scenario assignment constraints.

The two-size and per-machine two-size results are stronger on their
special inputs: they attain exact three halves with a global base
below two. AB gives the broader arbitrary-time model and a separate
time/quality curve. The inherited full-oracle lower bound from a
two-size zero-cost subclass gives 2^{q-O(log q)} queries on balanced
instances for factors strictly below three halves. It constrains
the whole-ground exponential base; it does not exclude an
F(q)*poly(H) approximation scheme, and it does not prove AB's bases
optimal at or above that factor.

Cost-preserving additive upper rounding for ordinary unrelated jobs
is public background, particularly [Shmoys and Tardos, *An approximation algorithm for the generalized assignment problem* (1993)](https://link.springer.com/article/10.1007/BF01585178), Theorem 2.1.
Ordinary unbudgeted scheduling has established parameterized
approximation schemes. This is not a first machine-parameterized
constant-approximation claim. The exact full-oracle model and explicit
bucket curve are internally derived here; publication priority needs
a separate exhaustive literature audit. No formal or external
verification claim is made.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
