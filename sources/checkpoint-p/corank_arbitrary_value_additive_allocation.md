# Corank-parameterized additive approximation for arbitrary resource values

**25 October 2026. New research manuscript; independent and root audits requested.**

The batched omission algorithm gives an additive approximation for
arbitrary nonnegative intrinsic resource values and arbitrary integral
recipient polymatroids. The selected players must form a basis of a
given matroid. The nonlinear parameter is its corank after deleting
loops. The proof combines exact workload scaling with polynomial-size
polymatroid intersection and a per-player additive rounding lemma.

The result is an additive theorem, not an unconditional approximation
scheme for integer max-min allocation. In particular, the largest
resource value remains an additive loss. A small-item hypothesis
turns it into a multiplicative approximation scheme.

## 1. Model and guarantee

Let M be a player matroid of positive rank r on a finite set P.
For each resource type j, let f_j be a normalized, monotone,
integer-valued submodular function on P, and let v_j>=0 be its
common intrinsic value. Counts of type j form an integer vector
in P(f_j). A solution chooses a basis I of M and maximizes

\[
                  \min_{p\in I}\sum_j v_j n_j(p).
 \tag{V1}
\]

Unassigned resources are permitted. Counts outside I may be
discarded. There are no additional local constraints coupling
different resource types. Fixed per-player, per-type integer upper
bounds may be incorporated into f_j before running the algorithm;
Section 8 explains this point precisely. Values and numerical
capacities are rational or integer numbers encoded in binary.

Delete all player-matroid loops and restrict every f_j to the
remaining ground. Rename that fixed ground P, put q=|P|, and let
c=q-r. Every original basis avoids the deleted loops. Restricting
any allocation preserves its value on that basis, and zero extension
of a feasible restricted vector is feasible on the original ground.
Thus this preprocessing preserves the integer optimum OPT.

Discard zero-value types and types of rank f_j(P)=0. If none remains,
OPT=0 and any player basis with zero counts is optimal. Otherwise
write

\[
                              u=\max_j v_j>0.
 \tag{V2}
\]

The maximum is over the remaining positive-rank types. Keeping the
larger maximum from before loop deletion is also a valid, weaker
additive bound. Rank-zero player instances return the empty basis
separately; no finite minimum over an empty basis is asserted.

Let 0<epsilon<1 be rational, and define
Gamma(R)=R^R/(R-1)^(R-1) for R>1.

**Theorem V.** There is a deterministic algorithm returning an
integer allocation and an M-basis I with value at least

\[
                    \max\{0,(1-\epsilon)\mathrm{OPT}-u\}
 \tag{V3}
\]

in time

\[
             \Gamma(1/\epsilon)^c\operatorname{poly}(H)
                 \le(e/\epsilon)^c\operatorname{poly}(H),
 \tag{V4}
\]

and polynomial workspace. H includes the original input bits,
the rational accuracy parameter, oracle-answer bit lengths and the
paid deterministic rank, submodular-minimization, and integral
polymatroid-intersection primitives. The algorithm expands neither
binary supplies nor conceptual workload units into individual copies.

## 2. Exact workload units engineer a genuine quota gap

Write 1-epsilon=B/A with integers A>B>=1. Choose a positive rational
g dividing every value, so v_j/g is a positive integer. For example,
the reciprocal of the product of the value denominators suffices;
its binary length is polynomial in the original input length. Set

\[
       \Delta=g/A,\qquad m_j=v_j/\Delta=A(v_j/g),
       \qquad F(S)=\sum_j m_j f_j(S).
 \tag{V5}
\]

Every m_j is a positive integer. Hence F is an integral monotone
polymatroid rank on the fixed loop-deleted ground P. Its value
oracle uses one original value query per type and binary arithmetic.

For a positive target T=kg, where k is an integer, use the quota pair

\[
          t=T/\Delta=Ak,\qquad b=Bk,
          \qquad \frac{t}{t-b}=\frac{A}{A-B}=1/\epsilon.
 \tag{V6}
\]

Both quotas are positive integers and b<t for every queried positive
target. In particular, this construction never attempts to apply
the gap theorem at t=b. No exceptional one-unit branch is needed.

Suppose an original integer allocation gives value at least T on
a basis I*. Its workload vector

\[
                            w_p^*=\sum_j m_j n_j(p)

\]

belongs to P(F): every subset inequality follows by summing the
corresponding original resource inequalities. On I* it is at least
t, so downward closure gives

\[
                               t\mathbf1_{I^*}\in P(F).
 \tag{V7}
\]

Apply the fully audited batch theorem from
`unit_quota_corank_batch_branching_improvement.md` to M and F.
Its runtime is Gamma(1/epsilon)^c poly(H). If it fails, (V7) proves
that no original integer target-T allocation exists. If it succeeds,
it returns a basis I with b*1_I in P(F).

During the batch recursion, F is only restricted to the current
player ground. It is always the same function (V5). No resource
contraction, reweighting, or recomputation on a smaller ground is
performed. Successful counts are zero-extended to the fixed P before
the reconstruction below.

## 3. An explicit binary-capacity decomposition

Start with w^0=b*1_I in P(F) and extend it to an integer base
w in B(F) with w>=w^0. Integral polymatroid augmentation permits
this. It can be implemented by at most q coordinate saturations,
each using submodular minimization to find the maximum permitted
integer increment; it does not add units one at a time. Once a
coordinate is saturated it remains saturated as other coordinates
increase, and a maximal independent vector of a polymatroid is a
base.

We now give a constructive decomposition into the scaled original
types. This makes explicit that a numerical multiplier m_j need
not be represented by m_j copies. On the polynomial-size ground
E=P times J, define

\[
 \mathcal A(S)=\sum_j m_j f_j(S_j),
       \qquad S_j=\{p:(p,j)\in S\},
 \tag{V8}
\]

and the per-player capacity polymatroid

\[
 \mathcal B(S)=\sum_{p:\,S\cap(\{p\}\times J)\ne\varnothing}w_p.
 \tag{V9}
\]

Both ranks are normalized, monotone, integral and submodular.
Their total ranks both equal w(P)=F(P). For any S subseteq E,
put R=intersection_j S_j. Then

\[
 \begin{split}
 \mathcal B(E\setminus S)&=w(P)-w(R),\\
 \mathcal A(S)&\ge\sum_jm_j f_j(R)=F(R)\ge w(R).
 \end{split}
 \tag{V10}
\]

The integral polymatroid-intersection min-max theorem therefore
gives a common independent integer vector of total w(P). Write
its component vectors as z_j. Since every type total is at most
m_j f_j(P), attaining the sum of those totals forces
z_j in B(m_j f_j) for every j. Likewise, the per-player capacities
in (V9), together with total equality, force sum_j z_j(p)=w_p.

Consequently

\[
                x_j=z_j/m_j\in B(f_j),
       \qquad \sum_jv_jx_j(p)=\Delta\sum_jz_j(p)=\Delta w_p.
 \tag{V11}
\]

For every selected player p in I, its fractional original value is
at least Delta*b=(1-epsilon)T. The z_j need not be divisible by
m_j. That is why (V11) is a fractional allocation of original
resources and needs a separate integer rounding step.

## 4. Per-player lower rounding through complement duality

The following lemma is valid for arbitrary nonnegative intrinsic
values and arbitrary fractional bases x_j in B(f_j).

**Lower-rounding lemma.** An integer base x'_j in B(f_j) can be
found for every resource, in polynomial oracle time, such that
every player p satisfies

\[
                    \sum_jv_jx'_j(p)\ge\sum_jv_jx_j(p)-u.
 \tag{V12}
\]

Here is a full derivation of the interface. Put a_j(p)=f_j({p}) and
define the complement rank

\[
       f_j^{\#}(S)
          =a_j(S)+f_j(P\setminus S)-f_j(P).
 \tag{V13}
\]

It is normalized, integral, and submodular. Its marginal on adding
p is a_j(p) minus a marginal of f_j, which is nonnegative by
submodularity and f_j(empty)=0. Thus it is monotone. Moreover,
f_j^{#}({p})<=a_j(p).

The affine complement map y_j=a_j-x_j takes B(f_j) exactly to
B(f_j^{#}). To verify the inverse, let y be a dual base and set
x=a_j-y. Since y(p)<=f_j^{#}({p})<=a_j(p), x is nonnegative.
Its total is f_j(P), and for every S the base equality and
complement-rank inequality give

\[
 y(S)\ge f_j^{\#}(P)-f_j^{\#}(P\setminus S)
           =a_j(S)-f_j(S),

\]

so x(S)<=f_j(S). The forward direction follows by the same
complement inequalities. In particular, it is not necessary for
the singleton-cap vector a_j itself to be a feasible base.

For completeness, upper rounding the dual bases has a polynomial-size
construction. Order the types so v_1>=...>=v_m>0 and put v_(m+1)=0.
At each player define

\[
             C_{p,k}=\left\lceil\sum_{j=1}^{k}y_j(p)\right\rceil,
       \qquad C_{p,0}=0.
 \tag{V14}
\]

Intersect the direct sum of the dual polymatroids on P times J
with the integral polymatroid of prefix constraints
sum_(j<=k) y'_j(p)<=C_(p,k). The latter's rank on a set S is
sum_p max{C_(p,k):(p,k) in S}, with an empty maximum equal to zero.
Its rank is submodular because a maximum of nonnegative element
weights is submodular; monotonicity of the C_(p,k) makes these
rank inequalities equivalent to the stated prefix constraints.

The starting fractional y belongs to this intersection and has
total sum_j f_j^{#}(P). Integral polymatroid intersection therefore
finds an integer vector with the same total. The direct-sum total
bound forces each component y'_j to be a dual base. Telescoping
the prefix constraints gives, separately at each player,

\[
 \begin{split}
 \sum_jv_jy'_j(p)
   &\le\sum_{k=1}^{m}(v_k-v_{k+1})C_{p,k}\\
   &\le\sum_jv_jy_j(p)+v_1
     =\sum_jv_jy_j(p)+u.
 \end{split}
 \tag{V15}
\]

Each y'_j is coordinatewise at most a_j. Complementing back gives
nonnegative integer bases x'_j=a_j-y'_j in B(f_j). Equation (V15)
is exactly the lower bound (V12). All coordinate caps and prefix
ceilings have polynomial binary length; both intersections use only
|P| times |J| ground elements.

This lemma is also the additive allocation guarantee in Bamas,
Lindermayr, Megow, Rohwedder and Schloeter,
[arXiv:2307.08453v1, Theorem 21](https://arxiv.org/html/2307.08453v1).
The direct argument above records the per-player statement and its
binary-capacity implementation. It makes no use of the local-search
results in the public paper or the ordered-layer core in this project.

## 5. The resulting one-sided target procedure

On a success of the quota step, use Sections 3--4 to reconstruct
integer original-resource bases. For every selected player,

\[
                      \sum_jv_jx'_j(p)\ge(1-\epsilon)T-u.
 \tag{V16}
\]

Discard all counts assigned outside I. The remaining resource
vectors are integer and independent by downward closure, and every
selected player's value is unchanged. Nonnegative values also give
the trivial lower bound zero. Thus every success returns a genuine
allocation meeting max{0,(1-epsilon)T-u}.

Every failure of the quota step proves OPT<T by (V7). All later
steps are guaranteed to succeed on its valid output. Thus the
target procedure returns a constructive additive approximation or
a sound original-target infeasibility conclusion. It can succeed
when T>OPT; the search below uses no converse implication.

Keeping all the rounded bases, instead of discarding outside I,
also gives the same objective guarantee in a variant that allows
unselected players to receive leftover resources. The proof does
not claim that full resource bases can always be assigned only to I.
The main theorem uses independent resource vectors and permits waste.

## 6. Exact target search needs only an external upper certificate

Every original integer utility is a multiple of g, and so is the
finite integer optimum. Let

\[
                         V=\sum_j v_j f_j(P).
 \tag{V17}
\]

Since r>=1, every minimum selected-player value is at most V.
Initialize lower target zero with an arbitrary player basis and
zero resource counts. Initialize upper target V+g as certified
infeasible from the total-value bound. Both are on the g-grid.
There is no need to run the weaker quota algorithm at that upper
endpoint or demand that it return failure there.

Maintain a successful lower grid target L with a saved allocation,
and an upper target U known to satisfy U>OPT. At a midpoint, save
the output and increase L after a target success; after a failure,
decrease U using its sound original-target infeasibility. When the
indices are adjacent, U=L+g. As OPT is a grid value strictly below
U, one has L>=OPT. The saved allocation then satisfies (V3).

The number of target trials is O(log(V/g+1)), including the usual
constant-size boundary handling. It is polynomial in the input bit
length. This proof does not assume monotonicity of algorithmic
success or identify a successful target with exact original
feasibility.

## 7. All numerical and oracle costs remain binary polynomial

The rational numbers g, Delta and epsilon have polynomial encodings.
All weights m_j and all target quotas Ak,Bk have polynomial binary
length, even when their numerical values are very large. The value
oracle for F uses polynomially many original queries. Its output
length is polynomial because it sums polynomially many products of
polynomial-bit integers.

Every batch node uses deterministic submodular minimization on the
current restriction of F and player-rank tests. The accepted batch
bound counts every attempted deletion, including those failing a
rank test, on both promised and unpromised targets. Its number of
attempted computation nodes is at most
(c+1)Gamma(1/epsilon)^c. The factor c+1 and all target-search
iterations are absorbed into poly(H).

Base extension, the decomposition intersection, and the lower-rounding
intersection are polynomial oracle computations. Their ground size is
polynomial in q and the number of types. Dividing z_j by m_j and
computing the exact prefix ceilings only uses rational arithmetic
of polynomial bit length. Large numerators or denominators do not
cause a loop indexed by their numerical magnitude.

Depth-first batch search uses at most c+1 stack levels. Together
with the paid polynomial-space deterministic oracle primitives,
all reconstruction and search operations use polynomial workspace.
The analytic expression Gamma(1/epsilon) is never evaluated by the
algorithm.

## 8. Coordinate bounds and the exact scope of the theorem

A prescribed integer cap h_j(p)>=0 on the count of type j at
player p can be absorbed into the recipient rank by

\[
 \widehat f_j(S)=\min_{A\subseteq S}
                   \{f_j(A)+h_j(S\setminus A)\}.
 \tag{V18}
\]

This is the integral polymatroid for P(f_j) intersected with the
coordinate box 0<=x<=h_j. Its oracle is computed by submodular
minimization. Apply the theorem to these capped ranks, so both
workload decomposition and final rounding preserve the caps.

Constraints coupling different resource types at one player, such
as a total item limit or an arbitrary downward-closed bundle family,
are not represented by (V18). Rounding and extending to bases can
violate such constraints. They are therefore outside this theorem.
Likewise, common intrinsic values are required for the workload
identity (V11); no player-dependent-value extension is claimed.

## 9. Consequence when individual units are small

For 0<eta<1/2, run the theorem with epsilon=eta. If the instance
satisfies u<=eta OPT, then

\[
                      \operatorname{value}(I)
                           \ge(1-2\eta)\mathrm{OPT}
 \tag{V19}
\]

in time Gamma(1/eta)^c poly(H). The algorithm need not know OPT
or verify this instance condition for its additive theorem to hold.

Equivalently, for a rational approximation parameter delta>0,
choose eta=delta/(2(1+delta)). Under u<=eta OPT, the returned
value is at least OPT/(1+delta), with time
(O(1+delta^-1))^c poly(H). This is a multiplicative consequence
under an explicit small-unit condition, not an unconditional
fixed-parameter approximation scheme for arbitrary integer inputs.

For example, the hidden unit-resource instances with OPT=2 and u=1
in `recipient_polymatroid_below_two_oracle_barrier.md` do not satisfy
an arbitrarily small-unit condition. The additive lower bound
2(1-epsilon)-1 does not force their hidden two-unit basis. Thus the
new theorem is consistent with the strict-below-two oracle barrier.

## 10. Public comparison and provenance boundaries

The primary public anchor is
[Bamas et al., arXiv:2307.08453v1](https://arxiv.org/html/2307.08453v1).
Its Theorem 21 gives the largest-unit additive rounding for a
fractional all-player allocation. Its Theorem 4 states a polynomial
8+epsilon guarantee for arbitrary resource values and 4+epsilon
for two values in the compulsory-player resource-polymatroid model.
Those statements were checked directly in the primary manuscript
on 25 October 2026.

The additive rounding itself is not claimed new. In particular,
when every player is compulsory, a fractional assignment LP followed
by the public rounding already gives the stronger guarantee
OPT-u in polynomial time. The role of the present batch theorem
is to select a basis among optional players with nonlinear time
depending on the number of omitted players, while losing only
epsilon OPT before rounding.

Targeted primary-source searches for corank-parameterized Santa
Claus allocation and polymatroid additive approximation did not
identify a checked statement of the precise theorem above. This
limited comparison is not a proof of publication priority or an
exhaustive literature review. The positive statement is presented
with its complete argument and with the exact oracle model and
additive loss kept visible.

The theorem depends on the separately audited batch omission
algorithm and standard integral polymatroid intersection. It is
independent of the project's ordered-prefix allocation theorem
and of the corrected public DRZ local-search argument.
