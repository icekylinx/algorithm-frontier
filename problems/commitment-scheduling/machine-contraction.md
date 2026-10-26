# Safe machine contraction and residual large-job rank

This is a preprocessing theorem for the job-polymatroid makespan model.
It commits whole machines at a certified load, contracts their full
contribution in every job polymatroid, and never increases the optimum
of the residual instance. The remaining large-job rank can be much
smaller than the original rank, even when that original rank exceeds
the number of machines.

The reduction is different from committing one large position in a
Boolean recipient basis. Removed machines may absorb many units of
many sizes. A greedy threshold closure computes the best certificate
within this full-marginal absorption rule in polynomial time. No
claim is made that it finds the best possible set of machines to
preassign under a load bound.

## 1. Scheduling model and marginal load

For each job type j, its size p_j is a positive rational and its
rank f_j is an integral normalized monotone submodular function on
the machine set P. Each schedule chooses an integer base x_j of
every f_j. Job capacities and ranks have binary representations.
Zero-size or zero-rank types can be handled separately and removed.

For a set F of already removed machines, define the residual
singleton load of a machine p outside F by

```math
c_p(F)=\sum_j p_j\bigl[f_j(F\cup\{p\})-f_j(F)\bigr].
 \tag{S1}
```

This is the load of assigning to p the entire currently available
singleton marginal of every type. It is computed directly from
rank-value queries and binary arithmetic. If F grows while p stays
outside, c_p(F) never increases, by submodularity of every f_j.

Fix a nonempty distinguished set of large job types. Define

```math
h=\sum_{j\text{ large}}f_j(P),\qquad
 \kappa(F)=\sum_{j\text{ large}}
                    [f_j(P)-f_j(F)].
 \tag{S2}
```

The preprocessing itself does not require a size gap or a common
large size. Such assumptions enter only through whichever residual
scheduling theorem is applied afterwards. There is no setup cost or
assignment-cost budget in this model.

## 2. Lemma: greedy absorption records legal restricted bases

Start with F empty. When a machine p is absorbed, assign

```math
x_j(p)=f_j(F\cup\{p\})-f_j(F)
                         \quad\text{for every type }j,
 \tag{S3}
```

and replace F by F union {p}. The assigned counts are nonnegative
integers, and their actual load is exactly c_p(F) with F before
the addition. If every absorbed marginal load is at most B, every
removed machine has load at most B.

For each type, these assigned counts are the greedy rank increments
along the absorption order. On the final F they form a base of
the restricted polymatroid f_j|F. In particular, their total count
is f_j(F). The residual job rank on Q=P\F is

```math
f_j^F(S)=f_j(F\cup S)-f_j(F),\qquad S\subseteq Q.
 \tag{S4}
```

This is an integral polymatroid with total rank f_j(P)-f_j(F).
There is no requirement that F be independent in a player matroid
or that the counts absorbed at one machine be at most one.

## 3. Lemma: restriction and contraction bases combine

Let a be any base of f|F and let b be any base of f/F on Q.
For a subset A of P, put U=A intersection F and V=A intersection Q.
Then

```math
\begin{split}
 a(U)+b(V)
 &\le f(U)+f(F\cup V)-f(F)\\
 &\le f(U\cup V)=f(A).
 \end{split}
 \tag{S5}
```

The second step is submodularity for F and U union V. The total
count is f(F)+f(P)-f(F)=f(P). Thus a union b is a full base of f.
This holds for every pair of the two bases, not just a specially
coupled decomposition.

Applying (S5) independently to every job type shows that any legal
residual schedule combines with the already recorded assignments.
The makespan of the combined schedule is the maximum of B and
the residual makespan.

## 4. Lemma: a contracted base dominated by any original base

The essential comparison is the following exact lemma.

**Lemma.** If x is an integer base of f on P, then f/F has an
integer base z on Q=P\F with z<=x|Q coordinatewise.

Write g=f/F. For every A subset of Q, original feasibility gives

```math
x(Q\setminus A)=f(P)-x(F\cup A)
                     \ge f(P)-f(F\cup A).
```

Consequently

```math
g(A)+x(Q\setminus A)\ge f(P)-f(F)=g(Q).
 \tag{S6}
```

The maximum total of an independent vector in P(g) bounded by x|Q
is `min_A[g(A)+x(Q\A)]`, which equals g(Q) by (S6) and A=Q.
Its integrality proves the lemma.

There is also a direct tight-set proof of the needed maximum
statement. Choose an integer independent z<=x|Q with maximum
total. Every coordinate not at its upper bound lies in a tight
set of g, since otherwise it could be increased by one. The union
of those tight sets is tight, by submodularity and feasibility.
Call it A. All coordinates outside A are at their upper bounds,
so z(Q)=g(A)+x(Q\A)>=g(Q). Feasibility gives the reverse inequality.
The empty-union case is included because g(empty)=0.

Now fix an optimal original schedule and apply this lemma separately
to each type. At every remaining machine, every residual type count
can be chosen no greater than its original count. All sizes are
nonnegative. Therefore the residual instance satisfies

```math
\mathrm{OPT}_F\le\mathrm{OPT}.
 \tag{S7}
```

The committed greedy bases need not agree with the original optimum
on F. Lemma (S5) ensures that they still combine with the dominated
residual bases from this comparison. The algorithm need not know
the optimum or these dominated vectors.

## 5. Theorem: the threshold closure is unique and monotone

For a threshold B>=0, repeatedly absorb any p with c_p(F)<=B until
none remains. Denote the final set by F*(B). The load assignments
in (S3) certify makespan at most B on that set.

The final set is independent of the choices. To prove this, compare
one legal absorption sequence with any final closed set G obtained
by another sequence. Inductively suppose its current prefix F lies
in G. If its next selected p were outside G, diminishing marginal
loads would give c_p(G)<=c_p(F)<=B, contradicting closure of G.
Thus every member of the first sequence belongs to G. Reversing
the roles proves equality of the final sets.

The same induction shows monotonicity:

```math
B\le B'\quad\Longrightarrow\quad F^*(B)\subseteq F^*(B').
 \tag{S8}
```

This is an exact statement for the specified greedy full-marginal
absorption rule. Other feasible preassignments could split type
counts more carefully and remove more machines at the same load;
they are not claimed to be described by F*(B).

## 6. Theorem: one greedy order computes every closure

Construct a full order p1,...,pq by repeatedly choosing a machine
of minimum current c_p(F), with deterministic tie breaking. Let
Fi={p1,...,pi}, let l_i=c_(p_i)(F_(i-1)), and set

```math
B_i=\max_{1\le t\le i}l_t,\qquad B_0=0,
             \kappa_i=\kappa(F_i).
 \tag{S9}
```

The individual l_i can decrease after an absorption. The prefix
bottleneck B_i is the quantity that is nondecreasing.

For a threshold B, stop just before the first l_i>B, or at the end
if there is no such index. Every earlier absorption is legal at B.
At that stopping point l_i is the minimum current marginal load,
so no remaining machine is legal. Thus the stopped prefix is exactly
F*(B). Equivalently, it is the longest prefix with B_i<=B, with
zero-cost initial machines included when B=0.

Every marginal computation uses t job-rank queries, where t is the
number of types. The naive full implementation uses O(q^2 t)
rank-value queries, plus polynomial binary arithmetic. It records
the greedy count assignments as part of the certificate. It needs
neither a numerical-capacity expansion nor an enumeration of all
possible sets F.

## 7. A computable bottleneck for a desired residual rank

For an integer budget k>=0, define

```math
\beta_k=\min\{B\ge0:
             \kappa(F^*(B))\le k\}.
 \tag{S10}
```

For k>=h this is zero. For k<h, take the first greedy prefix Fi
with kappa_i<=k; then beta_k=B_i. Extend through every further
prefix with the same bottleneck B_i. Its final set is F*(beta_k),
and its residual rank is at most k.

The proof follows directly from the threshold-prefix equivalence:
a smaller threshold stops before any prefix whose residual rank
has reached k. Since Fq=P has residual rank zero, the minimum
always exists and is attained. The possible positive beta_k values
are among the q computed prefix bottlenecks. Thus all distinct
rank-budget certificates are obtained in one polynomial run even
when h is a large binary-encoded number.

The bound is optimal only among the threshold closures specified
above. The notation beta_k does not denote the minimum makespan
needed to assign h-k arbitrary large units, nor the optimum of a
general scheduling subproblem.

## 8. Theorem: composition with any residual scheduling algorithm

Apply the reduction with F=F*(beta_k), keeping the recorded integer
assignments on F. Suppose a residual scheduling algorithm has a
guarantee

`C_res <= alpha_F OPT_F + e_F`,

where alpha_F>=0 and e_F>=0 are its stated parameters. Equations
(S5) and (S7) give the actual combined schedule bound

```math
\boxed{C_{\max}\le
          \max\{\beta_k,\ \alpha_F\mathrm{OPT}+e_F\}.}
 \tag{S11}
```

The residual algorithm receives the explicit contracted ranks (S4),
with one original rank query per contracted query. Singleton ranks
can only decrease. Its nonlinear running-time parameter is the
actual residual large rank kappa(F)<=k.

This can be combined with a further independent-set commitment
inside the residual Boolean matroid, or with [local-eligibility padding and collision thresholds](eligibility-padding.md). In such a composition, the final
maximum also includes the residual commitment's certified bottleneck.
All contractions and promise statements remain on their respective
grounds; the safe-machine reduction itself does not need a Boolean
large-job matroid of full original rank.

## 9. Concrete homogeneous-large consequences

Suppose all distinguished large types have the same size a, and
all remaining sizes are at most u<a. Then the [workload scheduling theorem](../many-size-scheduling/proof.md)
on the contracted instance gives, for rational 0<eta<=1,

```math
C_{\max}\le
  \max\left\{\beta_k,
        \left(2-{1\over3+\eta}\right)\mathrm{OPT}+u\right\}
 \tag{S12}
```

in

`poly(mathcal H) min{2^{O(k)},
 (k+1)^{O((1+eta^{-1}) log(k+1))}}`

time, with the zero-rank residual case handled directly. The
contracted small maximum may be less than u; using u is a valid
uniform bound. Thus the original large rank h may be enormous
while this nonlinear time depends only on the residual budget k.
For a requested eta>1, run the theorem with eta0=1. Its guarantee
is stronger than the displayed bound for that request, and its
runtime still has the stated O(1+eta^(-1)) dependence up to an
absolute constant factor in the exponent.

For exactly two original positive sizes, the [integral two-size rank theorem](../two-size-scheduling/rank-parameter.md)
instead yields

`C_max <= max{beta_k,(5/3)OPT}`

in 2^{O(k)} poly(mathcal H) time. If the contracted large rank is
zero, the remaining single-size instance can be solved exactly by
polymatroid capping and total-rank testing, giving

`C_max <= max{beta_0,OPT}`.

For arbitrary small
sizes and residual large rank zero, fractional scheduling followed
by small-job rounding gives the sharper

`C_max <= max{beta_0,OPT+u}`.

Running the public original-instance additive approximation as well
permits the minimum with OPT+a, and hence with 2OPT. The bottleneck
term is essential: no assertion that beta_k is automatically below
these OPT terms is made.

## 10. Structural and public-scope boundaries

The safe-machine parameter can be strictly different from the
one-large-position rank budget. A removed machine may contribute
many large units, and original h may exceed q. Conversely, the
full-marginal load requirement may be expensive, so the position
commitment can be better on other instances. Returning the best
actual schedule from both constructions is valid.

There is a relevant numerical baseline when the distinguished
large size is homogeneous: original h>q already forces two large
units on some machine and hence OPT>=2a. The ordinary public
additive bound then gives 3OPT/2. In that regime, merely reporting
the five-thirds residual formula is not a quality improvement.
The contraction remains useful for a smaller effective parameter,
for its zero-large-rank or near-exact residual cases, and in the
broader local-eligibility/collision transfers. The original additive
algorithm must remain among the returned candidate schedules.

This preprocessing does not improve the worst-case approximation
factor without a favorable certificate beta_k. It changes the
parameter on which the nonlinear part of the algorithm depends.
Its closure characterization is exact for its own deterministic
absorption rule; it is not a hardness or optimality result for
arbitrary ways of scheduling the removed machines.

The underlying polymatroid contraction, greedy bases, and box
restriction principles are classical. The public general makespan
additive baseline is Bamas et al.,
[arXiv:2307.08453v1, Theorem 23](https://arxiv.org/html/2307.08453v1).
The residual guarantees used in Section 9 are proved in the linked
workload and two-size manuscripts. The contraction and closure proofs
above require only integral polymatroid bases and their rank oracles.
The result asserts neither optimality over arbitrary commitments nor a
worst-case approximation improvement without a favorable bottleneck.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
