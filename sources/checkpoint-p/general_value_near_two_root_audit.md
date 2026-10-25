# Root audit: arbitrary intrinsic values and near-two player-matroid allocation

**25 October 2026. Complete internal mathematical review.**

Reviewed and accepted:

* `corank_arbitrary_value_additive_allocation.md`, V1--V19;
* `general_value_allocation_heavy_cover_near_two.md`, A1--A14;
* `general_value_matroid_selection_near_two.md`, J1--J17;
* `near_two_refined_parameter_zero_oracle_barrier.md`, Z1--Z7.

The additive and near-two algorithms retain arbitrary integral
recipient polymatroids and binary capacities. Values are common
intrinsic values in this group of manuscripts. Optional selected
players may form a basis of an arbitrary original matroid. The
near-two parameter is a derived corank, not in general the original
player corank alone. All stated optima are integer optima.

## 1. Exact quota engineering and compressed decomposition

For 1-epsilon=B/A and a common rational value grid g, choose
Delta=g/A. At a positive original-grid target T=kg, the workload
rank F=sum_j(v_j/Delta)f_j is integral and the quota pair t=Ak,
b=Bk has exactly t/(t-b)=1/epsilon. This avoids both a rounding
loss in the quota and an unjustified t=b invocation at a small
target. An original target allocation aggregates to a vector in
P(F) dominating t on its selected basis.

The returned b-quota vector is completed to an integer F-base.
The explicit decomposition proof is valid: on player-type pairs,
intersect the direct sum of (v_j/Delta)f_j with the per-player
capacity polymatroid of the completed workload. For a subset S
of pairs, putting R=intersection_j S_j gives

    A(S)>=F(R)>=w(R),       B(E minus S)=w(P)-w(R).

The integral intersection min-max theorem supplies full total
w(P). Equality of the aggregate upper bounds forces every type
component to be a scaled base and every player total to equal
w_p. Division by its numerical multiplier gives fractional
original bases with exactly the required workload. No supply or
multiplier is expanded into copies.

## 2. Lower rounding and the additive guarantee

For each resource let a_j(p)=f_j({p}) and
f_j#(S)=a_j(S)+f_j(P minus S)-f_j(P). Each marginal is a singleton
upper bound minus an original marginal, so the complement rank
is monotone, integral and submodular. Complementing gives an
exact bijection between original and dual base polytopes.

Upper rounding the fractional dual bases by type-value prefix
ceilings increases every player's dual value by at most the
largest unit value u. The prefix-cap system has integral rank
given by a sum of maximum prefix capacities on the player-type
ground. Intersecting it with the direct sum of dual resources
at full total rank yields integer dual bases. Complementing back
loses at most u per player. The capped-coordinate variant is also
valid because the caps are absorbed into the individual resource
ranks before all these operations.

This proves max(0,(1-epsilon)OPT-u) in Gamma(1/epsilon)^c poly(H)
time, with c the loop-deleted original player corank. Arbitrary
local constraints coupling resource types are not preserved by
this reconstruction and are correctly excluded. Unselected
allocations may be discarded by downward closure.

The maximization search uses an original value grid and an external
total-value upper certificate. The upper endpoint need not be
queried. Failed targets exceed OPT; adjacent endpoints force the
saved successful lower target at least OPT. Algorithmic success
need not be monotone. All grids and targets have polynomial bit
length. The small-unit multiplicative corollary explicitly retains
the hypothesis u<=eta OPT.

## 3. The compulsory heavy-complement promise is exact

For a fixed heavy/light split, let N be the Boolean cap of the
heavy aggregate. In an optimum, the support R of heavy-receiving
players is N-independent after retaining one unit per player.
Extend R to an N-basis F. Its complementary N*-basis consists
entirely of light-only players, so it retains the full original
target using light types. Derived loops are forced-heavy players;
removing them reduces corank from rank N to rank N minus its
number of coloops without harming this promise.

The fixed-split workload optimization and lower rounding provide
light value (1-epsilon)OPT-u_L on the selected complement. Its
heavy complement receives one unit per player, of value at least
a_H. At theta=(1-epsilon)OPT/2, strict light values give

    (1-epsilon)OPT-u_L=2 theta-u_L>theta,

while every heavy unit is worth at least theta. The resulting
allocation serves all players with at least theta. Rank-zero
derived instances use the direct pure-heavy branch.

Enumerating distinct value-class splits is polynomial in the
explicit type count. A split exceeding the parameter budget is
skipped without any original-infeasibility claim. All inner
searches concern one fixed split, so no false monotonicity of
the refined corank is used. The public constant fallback retains
a legal guarantee on all other instances.

## 4. The arbitrary original player matroid adapter is fully proved

For original M and heavy Boolean N, define U=M* vee N and K=U*.
The rank identity r(K)=r(M)-nu(M,N) follows from matroid union
and intersection, and is also proved by explicit decompositions.
Its nonloop corank is at most the original corank plus nu(M,N).

The important output-recovery point is stronger than that identity:
every U-basis S spans M*. If it did not, an element outside the
M*-closure of S could augment the M* component of a union
decomposition of S, contradicting that S is a U-basis. Therefore
for S=P minus I, where I is any K-basis, the M* component C can
be extended to a full M*-basis C' entirely within S. Then

    B=P minus C' contains I,
    B minus I=S minus C' is contained in the N-independent component.

Thus B is an original M-basis, I keeps its light allocation, and
the remaining selected players can each receive one heavy unit.
Extending C outside S would not suffice; the manuscript correctly
proves and uses the within-S extension.

Conversely, in an original target allocation on B*, let R be its
heavy-receiving selected players and L=B* minus R. The complement
P minus L is a disjoint union of an M*-basis and an N-independent
set, so is U-independent. Extending it to a U-basis proves that
L contains a K-basis. This supplies a genuine integer light-only
promise. It does not assume L itself has exactly the derived rank.

The additive theorem on K, followed by the within-S completion,
therefore proves factor 2+eta at

    theta=OPT/(2+eta),
    k >= c(theta)=number of K_theta nonloops minus rank K_theta,

in Gamma((2+eta)/eta)^k poly(H) time. The derived rank-zero case
is a polynomial pure-heavy construction. OPT=0 is handled without
evaluating a positive-threshold parameter at zero.

## 5. The fallback and model boundaries remain valid

To transfer the public compulsory-player fallback to original M,
add a dummy resource on M* with a value above total original value.
An original optimum can be extended to bases and supplemented on
its complementary M*-basis, giving a feasible compulsory-player
comparison. In the returned allocation, dummy recipients are
M*-independent. Extend them to an M*-basis and retain its
complementary original M-basis, whose guaranteed value uses only
original resources. Dropping the dummy and unused outside counts
preserves feasibility. All numerical dummy values have polynomial
bit length.

This supplies a complete polynomial fallback without pretending
that a budget-skipped split is infeasible. The guarantee is not
uniformly near two in polynomial time when the derived parameter
is unbounded. Nor is its parameter simply original corank. The
heavy/light types are disjoint because values are intrinsic; a
resource whose value varies with the player requires a different
argument and is not covered by this near-two proof.

## 6. The lower bound is correctly aligned to the refined parameter

Fix eta>0 in the same threshold OPT/(2+eta). On q=2r players,
the hidden rank

    f_A(S)=min(2|S|,2r)-1[|S|=r]+1[S=A]

is a valid integral polymatroid, and f_A(S)>=|S| for every S.
Its Boolean cap is therefore free. For original player matroid
U_(r,2r) and one unit-value resource, OPT=2 and every unit is
heavy at the chosen threshold. The derived K has rank zero and
loop-deleted corank zero. Yet any factor below two forces two
integer units per selected player and identifies the hidden A.

For compulsory players, add a value-two uniform resource of rank
r. OPT remains two, every type is again heavy at this fixed
threshold, and the aggregate Boolean matroid is free. Its rank
minus coloop count is zero. Any below-two output identifies A as
the r players receiving no large unit. The total small rank forces
this identification even when unused resources are permitted.

Only the oracle query at A distinguishes its hidden rank from
the reference. Therefore binom(2r,r)-1 queries are needed in the
worst case, even at refined parameter zero. This proves a
below-two FPT-oracle obstruction under this exact threshold
convention. It does not apply at constant unrefined heavy-cover
rank, does not exclude exact factor two, and does not establish
hardness for explicit restricted-assignment encodings.

All four accepted compositions have their parameter, comparator,
integer rounding, and original-basis reconstruction obligations
closed. Exact factor two for arbitrary intrinsic values remains
a separate open positive-algorithm gate in this research record.
