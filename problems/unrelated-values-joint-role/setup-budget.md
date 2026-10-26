# Unrelated-value allocation with one shared setup and assignment budget


This extension charges a nonnegative setup fee only for players in the
returned original matroid basis, and combines those fees with all actual
assignment costs in one exact budget. It permits arbitrary nonnegative
player-type values and arbitrary integral recipient polymatroids.

The main mechanism is a zero-utility dual-matroid dummy resource which
is available in every omission node, including at candidate light
players. Its negative auxiliary cost represents an unselected player's
setup credit. The original problem still has nonnegative costs. A
signed linear objective is used only inside a bounded integral rounding
face, and all discarded original assignments retain nonnegative costs.

## 1. The original model and theorem

Let M be a matroid of rank r>=1 on q nonloop players P. An actual basis
B of M must be selected. Each resource type j has normalized monotone
integral submodular recipient rank f_j. Its integer counts are independent
in P(f_j), unused units are allowed, and type-player values v_pj and
assignment costs c_pj are arbitrary nonnegative rationals. Player p has
nonnegative setup fee sigma_p. The returned solution must satisfy

```math
\sum_{p\in B}\sigma_p+
 \sum_{p\in B,j}c_{pj}x_j(p)\le C.
 \tag{SD1}
```

The objective is the minimum original utility over B. Write OPT for its
integer optimum, c=q-r, and H for the full binary input and the paid
polynomial rank-oracle and optimization work. Original player loops
may first be deleted; they are never selected and nonnegative-cost
assignments to them are unnecessary.

First compute a minimum-setup M-basis. If its setup cost exceeds C,
there is no feasible original solution, even with zero utility.
Otherwise save it with zero resource counts as a legal value-zero
output. Rank zero is handled separately by the chosen empty-set
convention.

**Theorem SD.** For every fixed rational R>1, put

```math
\alpha=1-1/R,\qquad
 \Gamma(R)=\frac{R^R}{(R-1)^{R-1}},\qquad
 B(R)=2-1/\Gamma(R).
 \tag{SD2}
```

For every feasible original instance, a deterministic algorithm returns
an actual M-basis and an integer allocation of value at least
alpha*OPT/2, respecting SD1 exactly, in

```math
B(R)^q\,
 2^{O(q\log\log(q+2)/\log(q+2))}
 \mathrm{poly}(H)
 \tag{SD3}
```

time and polynomial workspace. No intrinsic-value, support-size or
price-diversity assumption is required. For fixed rational eta>0,
R=(2+eta)/eta gives factor 2+eta. If some optimum has at most K
selected heavy recipients at alpha*OPT/2, the corresponding conditional
parameterized time is Gamma(R)^(c+K) poly(H).

## 2. A persistent dummy and its affine budget

Add an auxiliary resource with recipient rank M*, the dual of M.
Its fractional count vector is y in P(M*). Write
S_sigma=sum_(p in P) sigma_p. The internal affine budget is

```math
\sum_{p,j}c_{pj}x_j(p)+S_\sigma-\sum_p\sigma_p y_p\le C.
 \tag{SD4}
```

Thus a dummy unit at p has auxiliary linear cost -sigma_p. Its total
utility in the light service objective is zero. This is not the
large-valued dummy construction used to equate integer optima in
the basic unrelated-value theorem; the present proof uses a
protected original optimum directly.

An integer dummy vector has entries zero or one. If its support is D,
then D is M*-independent and the dual rank identity implies

```math
r_M(P\setminus D)=r.
 \tag{SD5}
```

Hence the dummy-free players contain an original M-basis B. For any
integer point satisfying SD4, restricting its real allocations to B
gives

```math
\begin{aligned}
 \sum_{p\in B}\sigma_p+\sum_{p\in B,j}c_{pj}x_j(p)
 &\le \sum_{p\notin D}\sigma_p+\sum_{p,j}c_{pj}x_j(p)\\
 &=S_\sigma-\sum_p\sigma_p y_p+\sum_{p,j}c_{pj}x_j(p)
 \le C.
 \end{aligned}
 \tag{SD6}
```

The inequalities use nonnegativity of the original fees and assignment
costs. The internal negative dummy coefficients are not discarded
before this conversion. This is how the exact original budget is
recovered.

## 3. The joint region at each light-role node

Fix a mask of the positive original pairs, with light pairs of value
less than theta and heavy pairs of value at least theta. Let u_L be
the largest light value, or zero, and a_H the smallest heavy value,
or infinity when no such pair exists. All distinct masks are enumerated
by the finitely many positive pair values. Equality belongs to heavy.

At Q subseteq P, use the original real-resource masks

```math
A_j(Q)=\{p\in Q:0<v_{pj}<\theta\}
          \cup\{p\notin Q:v_{pj}\ge\theta\},\qquad
 f_j^Q(S)=f_j(S\cap A_j(Q)).
 \tag{SD7}
```

Crucially, do not restrict the dummy resource to P\Q. It remains
available on all P. Let X_Q contain all fractional x,y satisfying

```math
\begin{aligned}
 x_j&\in P(f_j^Q),\qquad y\in P(M^*),\\
 y_p+\sum_jx_j(p)&=1 &&(p\notin Q),\\
 \sum_{p,j}c_{pj}x_j(p)-\sum_p\sigma_p y_p
     &\le C-S_\sigma.
 \end{aligned}
 \tag{SD8}
```

Outside Q a player has exactly one unit in total, either real heavy
or dummy, fractionally. At a player in Q the dummy may coexist with
light real counts, but contributes zero light utility. Define

```math
U_Q=\{z\in\mathbb R_+^Q:\exists(x,y)\in X_Q,\,
                 z_p\le\sum_jv_{pj}x_j(p)\ (p\in Q)\}.
 \tag{SD9}
```

Test X_Q for emptiness first. If nonempty, U_Q is compact, convex,
contains zero and is downward in its service coordinates. The right
side C-S_sigma may be negative; this causes no difficulty for its
bounded rational feasibility LP. The auxiliary signed objective
does not imply signed coefficients in a service separator.

For a nonnegative normal a, compute the support of U_Q by an exact
linear program over SD8. The normalized outer support LP of J9--J10
then returns either membership or a nonnegative valid row a*z<=U
with U>=0. Choose extreme optimizers for support cuts by exact
lexicographic refinement. Rank inequalities, the dummy matroid rank,
equalities and affine budget all have uniform polynomial bit length.
Thus separation and reconstruction are polynomial in H over every Q.

The support bound can be
V=sum_j(max_p v_pj)f_j(P), because dummy utility is zero on Q.
The special empty-Q case is the all-heavy/dummy gate below.

## 4. The original optimum survives all protected restrictions

Let an original optimal solution have selected basis B*. Extend its
complement D*=P\B* to the canonical dummy vector 1_(D*); it already
is an M*-basis. Let F* subseteq B* consist of the selected players
who originally receive at least one heavy pair, and let

```math
I^*=B^*\setminus F^*,\qquad
 k=|P\setminus I^*|=c+|F^*|.
 \tag{SD10}
```

Keep every original allocation on I*, keep one original heavy unit
at each member of F*, and keep the dummy vector on all D*.
At a node Q containing I*, drop the retained real heavy units on
F* intersect Q. Keep the dummy unchanged even on D* intersect Q.

All real retained pairs satisfy SD7. Every player outside Q is
either in F* or D*, so it still has exactly one real heavy or dummy
unit. The dummy credit in SD4 is unchanged:

```math
S_\sigma-\sum_{p\in D^*}\sigma_p=\sum_{p\in B^*}\sigma_p.
 \tag{SD11}
```

Only nonnegative real assignment costs have been discarded. Therefore
SD8 remains feasible, and the original full utility on I* survives:

```math
\mathrm{OPT}\,1_{I^*}\in U_Q.
 \tag{SD12}
```

This is the reason the dummy must remain available inside Q.
Deleting a dummy on an unselected player there would remove its
negative cost credit and could destroy exact-budget feasibility.

The same reasoning works for every fixed full-role witness defined
on an exact light set I: it may have dummy counts on I as well.
Retain all its dummy counts, retain real counts on I and P\Q, and
discard real counts on Q\I. Heavy equalities outside Q survive,
resource vectors decrease only in nonnegative real coordinates,
and the affine budget cannot increase.

## 5. Gap recursion and all-input time

Fix an exact promised light cardinality s=q-k>=1. A full-role witness
is a joint point of X_I for some s-set I, giving original light service
at least t to every member of I. Dummy counts are allowed everywhere.
For every Q containing that I, the final paragraph of Section 4
implies t*1_I in U_Q.

Query b*1_Q with b=alpha*t. When a nonnegative row separates it,

```math
t\,a(I)\le U<b\,a(Q)
 \quad\Longrightarrow\quad
 a(Q\setminus I)>\frac1R a(Q).
 \tag{SD13}
```

The weighted first-crossing certificates therefore include a deletion
inside Q\I. Repeating the surviving-witness argument after each such
deletion proves completeness. At zero deficit Q=I, the full witness
directly satisfies the weak query.

Starting after a forced omission seed Z, the all-input cost is
Gamma(R)^(k-|Z|) poly(H), with every empty-region check, failed
support query and failed branch included. No fixed or nested U_Q
assumption is used. The prefix-free counting depends only on R and
the remaining deficit. A success may occur early, with |Q|>s;
the recovery below still produces an original feasible basis solution.

## 6. Rounding with the signed auxiliary objective

The complement-prefix rounding proof works for any signed linear
cost objective on its bounded face. In detail, add a zero-cost free
disposal coordinate to each real and dummy resource so the given
fractional independent vector becomes a base at unchanged affine
cost. Form integral complement ranks and every per-player ceiling
prefix constraint. On their integral maximum-total intersection face,
maximize the given signed cost coefficients applied to the complement
vector. The original fractional complement lies on that same face.
Complementing the maximizing integer point back therefore never
increases the original signed linear objective.

Nonnegativity of the objective coefficients is not used in this
comparison; it was needed in the original additive theorem only for
discarding selected-out assignments. Here no dummy support is discarded
until it is converted by SD6. The disposal coordinates have cost zero.

At a player p in Q, order real types by their true light values and
give the dummy value zero for this ordering. The largest eligible
positive value is at most u_L. Prefix telescoping gives original
light utility at least b-u_L. At p outside Q, use any nonnegative
ordering of its allowed real heavy types and dummy. The full-prefix
count-floor guarantee gives

```math
y'_p+\sum_jx'_j(p)\ge
                       \left\lfloor y_p+\sum_jx_j(p)\right\rfloor=1.
 \tag{SD14}
```

Both the light utility and SD14 hold at the same integer
cost-preserving point. Masked real ranks prevent forbidden pairs
from reappearing. The dummy vector is an integer M*-independent
vector, so its entries are zero or one.

Let D be its actual dummy support and choose an M-basis B in P\D.
For p in B outside Q, SD14 and y'_p=0 imply at least one original
heavy unit, hence utility at least a_H. For p in B intersect Q,
the light utility is at least b-u_L. Restrict original resources
to B. Equation SD6 proves the exact original combined budget, and
the achieved minimum utility is at least

```math
\min\{a_H,b-u_L\}.
 \tag{SD15}
```

It is unnecessary to trim the auxiliary heavy counts to one before
extracting B. Such a trim must not arbitrarily remove a negative-cost
dummy credit. This proof avoids that operation entirely.

## 7. Finite target searches without a zero-role feasibility oracle

Use a common rational grid g dividing all original pair values.
For a fixed mask and k<q, define X as the largest g-grid light target
admitting a full-role witness from Section 5, with zero adjoined to
the possible benchmark values if the role family is empty.
For nonempty roles, feasibility is downward in the light target.
In every case 0<=X<=V and V lies on the same grid.

Initialize nominal target zero using the globally affordable
minimum-setup basis and zero original allocations from Section 1.
This original legal output need not be a witness for the particular
mask/k role family. Its utility zero is nevertheless at least
min{a_H,-u_L}, the required weak output bound at nominal target zero.
Thus no unproved exact minimum-cost optimizer over unknown role
sets is needed to initialize these searches.

Use external upper target V+g. At each positive interior grid target,
run the complete gap. Failure certifies T>X; a success is rounded
and its actual original basis solution is saved with its nominal T.
The invariant U>X persists. When endpoints become adjacent, the
saved lower target L satisfies L>=X. This includes an empty role
family or X=0, and does not require success monotonicity.

All target data have polynomial binary length. If all eligible
original values are zero, the initialized minimum-setup basis is
already optimal and no positive threshold is considered.

## 8. The all-heavy/dummy gate

When k=q there is no light set and its light benchmark would be
unbounded. Handle it directly. Use the heavy real-pair masks,
retain the dummy matroid on all players, and ask for an integral
allocation with exactly one total real-heavy-or-dummy unit at
each player. The product resource polymatroid intersected with
the partition caps one has a full-total integral face of total q
whenever its fractional counterpart is feasible.

Minimize the signed linear objective
sum c_pj x_j(p)-sum sigma_p y_p on that face and add S_sigma.
If the optimum exceeds C, or total q is infeasible, reject this
gate. Otherwise take an integer optimum and recover an original
M-basis from its dummy-free players by SD5--SD6. Every selected
player has one original heavy unit, so the value is at least a_H.

This is a polynomial weighted integral-intersection computation.
Its objective is bounded, its right-hand side may have either sign,
and no binary unit expansion is involved. If the protected optimum
has all r selected players heavy, its real heavy cover plus the
canonical dummy basis is an affordable witness for this gate.

## 9. Approximation, globalization and scope

For OPT>0 choose the enumerated mask induced by theta*=alpha*OPT/2.
Then u_L<theta*<=a_H. If the protected optimum has at least one
small-only selected player, SD10 gives k<q and its original
allocation supplies a full-role witness at target OPT. Thus X>=OPT,
the saved fractional target is at least alpha*OPT, and SD15 gives
value at least theta*. If it has none, Section 8 gives the same
guarantee. OPT=0 is covered by the initialized legal basis.

For a supplied support cap K, process every needed exact cardinality
k<=min{c+K,q-1}, and the pure gate when c+K>=q. The protected
optimum then gives the stated conditional corank-plus-support bound.
For all-instance time, process every exact k<q and the pure gate.
Apply the polynomial-space global cover to the forced-omission
interface in Section 5 for every finite target. Its returned
solution is the actual basis allocation from Section 6. An early
success with fewer forced roles is a legal relaxed output.

There are polynomially many pair masks, cardinalities and target
calls. Globalization gives SD3 and polynomial workspace. For fixed
rational R the sharp constant comparisons are exact algebraic
comparisons as proved in the global conversion. For varying binary
accuracy, the supplied rational A=3R gives the stated safe uniform
base version, with all accuracy bits paid.

This theorem has one combined budget and one original player
matroid. It does not assert a result for arbitrary negative original
assignment costs, several independent setup objectives, or several
exact integer assignment budgets. The signed dummy credit is valid
because its original meaning, its persistence at protected nodes,
and the final integer complement extraction are all proved.

The numerical global conversion is established public monotone local
search; the shared-role and complement rounding ingredients are proved
in [Unrelated-value allocation near two through a joint light/heavy LP](proof.md) and its accepted
dependencies. No external peer review or publication-priority claim
is made. The new contribution of this note is the exact affine setup
accounting and its compatibility with the changing joint-role LP.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
