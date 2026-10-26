# Exact two for compulsory two-value allocation with arbitrary assignment costs

Every player must be served, resource values have two positive
levels, recipient capacities are arbitrary integral polymatroids,
and every player-type assignment may have an arbitrary nonnegative
cost. One total assignment budget is preserved exactly. An adaptive
minimum-heavy-cost reservation gives an exact factor-two algorithm
without a price-diversity parameter or a common-small-cost condition.

The parameter can be the maximum number of distinct heavy recipients
affordable within the original budget. Its running time is
`(27/4)^h_C poly(H)`. A strict-below-two recipient-oracle lower bound
holds for the same parameter, even when every cost is zero.

## 1. Model and computable parameter

Let P have q>=1 compulsory players. Resource type j has positive
intrinsic value v_j, an integral normalized monotone submodular
recipient rank f_j, and arbitrary nonnegative rational costs c_pj.
Integer counts n_j belong to P(f_j); unused resource capacity is
allowed. The cost condition is

```math
\sum_{p,j}c_{pj}n_j(p)\le C,
                              \qquad C\ge0.
 \tag{C1}
```

After discarding zero-rank or zero-value types, assume two distinct
values 0<u<a, with small types J_s and large types J_b. Missing
classes are handled exactly in Section 9. Let OPT_C be the integer
maximum all-player minimum utility.

Let h_C be the maximum number of distinct players that can each
receive one feasible large unit with combined assignment cost at
most C. It is computed by minimum-cost matroid intersection on
eligible large player-type pairs: the direct sum of type Boolean
recipient matroids intersects the player partition matroid allowing
one pair per player. Minimum cost at cardinality k is nondecreasing
in k, so the largest affordable k can be found in polynomial time.

If N is the Boolean-cap matroid of the aggregate large recipient
rank, then h_C<=rank(N)<=q. h_C may be strictly smaller because
of the assignment costs. Every original budget-feasible allocation
has at most h_C recipients of large units: retain one of its
actual large assignments per recipient to witness that fact.

**Theorem C.** A deterministic algorithm returns an integer all-player
allocation satisfying (C1) exactly and giving each player utility
at least OPT_C/2. Its running time and workspace are

```math
(27/4)^{h_C}\mathrm{poly}(H),
                          \qquad\mathrm{poly}(H).
 \tag{C2}
```

H pays all original bits and the exact polynomial matroid, recipient,
LP, submodular-minimization and decomposition primitives. Resource
supplies and all quotas remain binary encoded.

## 2. Minimum large-completion cost at an omission node

Fix k in {0,...,h_C}. A candidate small set has size q-k and its
complement receives one large unit per player. At a current ground
Q subseteq P of allowed small recipients, define h_k(Q) as the
minimum actual cost of a feasible cardinality-k large assignment
whose recipient set F includes P\Q. Set it to infinity if none
exists. Return an attaining H_Q and I_Q=P\F subseteq Q.

This is the compulsory-player instance of the completion oracle
in [Arbitrary-cost allocation near factor two with an adaptive residual budget](../../manuscripts/allocation-and-scheduling/arbitrary-cost-residual-budget-near-two-allocation.md).
Explicitly, make zero-weight small copies for players in Q and
actual-cost large pairs for every eligible large assignment.
Intersect the partition matroid allowing at most one copy of each
player with the direct sum of the uniform small cap q-k and the
rank-k truncation of the large type-matroid direct sum. A common
independent set of size q necessarily covers all players, uses
q-k small copies and k large pairs, and its weight is exactly the
large assignment cost. Minimum-weight intersection computes the
required pair, including forced large coverage outside Q.

The large support is never extended beyond its fixed size k.
The costs of different large types at the same player are fully
retained in this oracle. The type-pair ground is polynomial and
does not expand numerical supply.

## 3. The residual small-count region

For D>=0 define the fractional small count region

```math
\mathcal U_s(D)=\left\{z\ge0:\exists x_j\in P(f_j)\ (j\in J_s),
       \ \sum_{j\in J_s}x_j(p)\ge z_p\ (p),
       \ \sum_{p,j\in J_s}c_{pj}x_j(p)\le D\right\}.
 \tag{C3}
```

This is a compact convex downward rational polytope. It has an
exact nonnegative packing separator and reconstruction LP from
the budgeted count proof in
[Exact factor two for one-value allocation with arbitrary assignment costs](../one-value-exact-two/proof.md), Sections 3--4.
Both small capacity and actual assignment cost remain coupled
inside this region. Aggregating small resource ranks while ignoring
their individual costs would not be sufficient.

At a node Q with h_k(Q)<=C, the algorithm uses the current budget
D_Q=C-h_k(Q). For full and output quotas t>b>0, it queries
b*1_Q in U_s(D_Q). A successful membership witness serves all of
Q at b. Restrict it to the attaining small set I_Q and retain H_Q;
their combined fractional cost is at most C.

If the query fails, use its nonnegative violated row in the
weighted prefix-free omission routine. The required selected
cardinality is q-k, so the omission budget starts at k.

## 4. Why the changing budget preserves completeness

Suppose there is a pair I*,H* with |I*|=q-k, one large assignment
on each complementary player, and a fractional small allocation
x* giving at least t units on I*, with total cost at most C.
Whenever I* subseteq Q, its original large assignment is a
permitted completion, and therefore

```math
h_k(Q)\le c(H^*),\qquad
           c(x^*)\le C-c(H^*)\le C-h_k(Q).
 \tag{C4}
```

The full t*1_(I*) is feasible in every current small-count region
along a branch that preserves I*. Thus every local violated row
supplies the same weighted omission certificate as in the fixed-
region theorem. One child preserves I*, and induction applies.
At success it is essential to use the *attaining* H_Q, because
the small allocation was charged against its exact cost.

The abstract adaptive theorem and prefix-free accounting are in
[Corank omission with a changing residual budget](../whole-ground-allocation/adaptive-selection.md). They give a gap routine
of time

```math
\Gamma(t/(t-b))^k\mathrm{poly}(H),
                         \qquad \Gamma(R)={R^R\over(R-1)^{R-1}},
 \tag{C5}
```

with polynomial space, including failed completion calls. All
current residual budgets have polynomial bit length because
h_k(Q) is a sum of original large assignment costs.

## 5. No-loss integer small-quota recovery

The output small quota b will be an integer. For a returned
I_Q and its fractional small allocation, discard counts outside
I_Q and trim each selected player's total to exactly b units.
This reduces cost and preserves every recipient constraint.

On I_Q times the small types, intersect the direct sum of the
restricted original recipient polymatroids with the partition
polymatroid allowing at most b total units per player. The
fractional point has total b*|I_Q|, which saturates the partition
rank. The resulting maximum-total face is nonempty and integral.
Minimize actual small assignment cost on this face and choose an
integer optimum. Its cost is no greater than that of the supplied
fractional point, and its total forces exactly b units at each
member of I_Q.

Thus the integer small allocation costs at most C-h_k(Q). Add
the same H_Q to meet the exact budget. There is no largest-small-
unit loss in this step. The one-value cost-recovery lemma supplies
an integral minimizer of a linear objective on an integral face;
it does not assume that intersecting a polytope with a cost budget
preserves integrality.

When k=q the small set is empty; test affordable all-large coverage
directly and omit this quota procedure.

## 6. Hard targets and the exact half quota

Fix 0<T<2a and put

```math
K=\lceil T/u\rceil,
                       \qquad b=\lceil K/2\rceil.
 \tag{C6}
```

For K>=2, use the adaptive count gap with t=K and this b, for
every k=0,...,h_C. The ratio satisfies

```math
K/(K-\lceil K/2\rceil)\le3,
                                \qquad \Gamma(3)=27/4.
 \tag{C7}
```

The maximum occurs at K=3. A success followed by Section 5 gives
small utility b*u>=T/2 and large utility a>T/2, at cost at most C.

To prove that a feasible original T cannot be rejected, let R be
the players receiving any large unit in an integer T-allocation.
Its cardinality k is at most h_C. Keep one of the original large
assignments at every member of R, preserving its type, and
discard other counts there. The complementary players I* had only
small resources, at least K units each. Retain their original
small allocation or trim it to K units per player. Costs only
decrease. This supplies the t=K pair in Section 4 for its true k.
That gap call cannot fail. No extra large recipient is added.

If all k calls fail, the original integer T is infeasible. A
success need only attain T/2 and is not an assertion of full-T
feasibility.

## 7. The exact one-unit gate and large targets

If K=1 then 0<T<=u. Every positive unit has value at least T.
A feasible original target exists exactly when one resource unit
can be assigned to every player at cost at most C: trim all
other units from an original allocation to prove the forward
direction.

Use all positive types in the minimum-cost one-unit coverage
intersection: their Boolean matroid direct sum versus the player
partition matroid, at cardinality q. Accept exactly when its
cost is at most C. A success gives utility at least u>=T, and
a failure soundly excludes the target. The gap theorem is not
invoked with t=b=1.

For T>=2a, solve the budgeted fractional all-player feasibility
LP with utility T and the original resource constraints. A
failure excludes the integer target. On success use the accepted
cost-preserving lower-rounding lemma, with free disposal and the
cost-optimal full-total dual face. Its largest unit value is a,
so the resulting integer utility is at least

```math
T-a\ge T/2,
 \tag{C8}
```

and its total assignment cost is at most C. This branch uses a
fixed compulsory player set, so no unknown-basis selection step
is hidden in the LP. Equality T=2a is assigned to this branch.

## 8. Complete one-sided optimization and complexity

Choose a positive rational grid g dividing u and a, and let
V=sum_j v_j f_j(P). Every integer minimum utility, including
OPT_C, lies on the g-grid and is at most V. Start with lower
target zero and the zero allocation, and external upper bound
V+g. Query middle grid targets by Sections 6--7. Save every
success and move the lower endpoint; move the upper only on
a sound failure.

All failures exclude the full original integer target, so the
upper endpoint stays strictly above OPT_C. At adjacent grid
points the saved lower target is at least OPT_C. Its actual
allocation gives at least half that lower target, proving the
factor-two guarantee. Successes may be nonmonotone and may
exceed the original optimum as nominal targets; the proof does
not interpret them as full-target witnesses.

There are polynomially many target calls in the binary length
of V/g. Each hard target enumerates at most h_C+1 support sizes
and uses (C5)--(C7); summing over them changes only a polynomial
factor. The exact gates and large-target LP are polynomial. This
proves (C2). All algorithms keep polynomially many coordinates
and binary counters, with depth-first omission search. Zero budget
and zero assignment costs are valid throughout.

## 9. Empty and one-value cases

If no positive resource remains, optimum is zero. With one value
v, a target of b integer units at every player can be tested by
minimum-cost integral polymatroid intersection: direct-sum
recipient constraints and the per-player b-unit partition cap,
on their maximum-total face of total bq. Feasibility and optimum
cost are integral. Comparing this cost with C is an exact target
test, and integer binary search finds the exact one-value optimum.

This is the fixed-player specialization of
[Exact factor two for one-value allocation with arbitrary assignment costs](../one-value-exact-two/proof.md). It does not
require equal assignment costs among types. Missing classes
therefore need no artificial heavy threshold, and no empty
selected set is sent to a positive quota core.

## 10. A matching strict-below-two oracle threshold

The zero-cost subclass already supplies the matching approximation
threshold. Fix q>r>=2, set h=q-r, take one small unit-valued
resource with hidden rank

```math
f_A(S)=\min\{2|S|,2r\}-{\bf1}[|S|=r]+{\bf1}[S=A],
                                  \qquad |A|=r,
 \tag{C9}
```

and a large resource of value two with recipient matroid U_(h,q).
Set all assignment costs and C to zero. The rank validity and
hidden-set property are proved in
[A value-oracle barrier below factor two for rank-parameterized allocation](../allocation-lower-bounds/proof.md).
The affordable large-recipient parameter h_C is exactly h.

The hidden allocation gives two small units to A and one large
unit to each player outside A, so optimum is at least two.
At most h players can receive large units, and the total small
rank is 2r, so optimum cannot exceed two. Any factor strictly
below two must give every player integer utility at least two.
Its small-only players number at least r, each need two small
units, and the total rank forces exactly r of them. Their set
I must satisfy f_A(I)>=2r, which holds only for I=A.

Thus such an output identifies the hidden set. The rank oracle
differs from a symmetric reference only at A, so a deterministic
algorithm needs at least binom(q,r)-1=binom(q,h_C)-1 queries in
the worst case. Fixing h_C larger than any proposed polynomial
degree and increasing q excludes every uniform F(h_C)*poly(H)
algorithm of factor strictly below two in this oracle model.

This is an approximation threshold for arbitrary recipient-rank
oracles. It does not prove the exponential base 27/4 optimal,
does not obstruct exact two, and does not establish ordinary
explicit-eligibility hardness.

## 11. Public comparison and relation to the broader theorem

The ordinary arbitrary-cost Budgeted Santa Claus result of
Rohwedder, Rouhani and Wennmann,
[*Cost Preserving Dependent Rounding for Allocation Problems*,
ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127), Theorem 3,
gives a randomized polynomial logarithmic guarantee. Its ordinary
cost-preserving additive rounding is established background.
The present factor two is deterministic with exponential dependence
on the affordable large-recipient parameter, and it permits
binary-supply recipient polymatroids. It is not a polynomial
factor-two claim when that parameter is unbounded.

The earlier common-small-charge exact-two theorem is a proper
subclass of this statement. The new residual budget replaces
its modular charge by the actual budgeted small-count projection.
The no-loss integer quota recovery is what retains exact two.

The arbitrary-value original-player theorem in
[Arbitrary-cost allocation near factor two with an adaptive residual budget](../../manuscripts/allocation-and-scheduling/arbitrary-cost-residual-budget-near-two-allocation.md) gives
2+eta using a positive fractional utility gap and a light-unit
loss. This compulsory two-value theorem uses a different fixed
value-class parameter and its exact large-target LP. Neither
scope nor parameter is silently substituted for the other.

Root and independent full review are requested for the adaptive
pair invariant, attaining completion at success, exact small
quota recovery, K=1 and T=2a interfaces, target optimization,
affordable parameter and matching oracle threshold.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
