# Two obstructions to lifting one-scenario roles into robust allocation

The model has a common actual basis of an original player matroid and
an explicit list of scenarios. Resource counts may adapt to the
scenario. Values, recipient polymatroids and assignment costs may be
scenario dependent. Each scenario has its own exact budget, which may
include the setup cost of the common selected basis.

Two separate difficulties prevent an automatic extension of the
one-scenario joint-role proof. First, the same player can require a
heavy role in one scenario and a light role in another. Second, even
when every scenario uses exactly the same all-heavy role mask, a
shared fractional dummy cannot in general be rounded to one common
integer selection. The latter difficulty survives a zero role-
disagreement parameter.

These are counterexamples to specific lifting arguments. They are not
new lower bounds on a whole-ground exponential time base.

## 1. A common role set can fail with one compulsory player

Let P={p}, let the player matroid be the free rank-one matroid, and
give every assignment cost and setup fee value zero. There are two
scenarios, each with one modular recipient resource:

| Scenario | Singleton capacity | Value per unit |
|---|---:|---:|
| A | 1 | 2 |
| B | 3 | 3/4 |

The maximum utility is 2 in A and 9/4 in B. Because the one player
is compulsory and the allocations adapt to the scenario, the robust
integer optimum is exactly

$$
\mathrm{OPT}=2.
\tag{CR1}
$$

Use the exact-half threshold theta=OPT/2=1. Scenario A has only a
heavy eligible pair; scenario B has only a light eligible pair.
A single role set Q, interpreted as light inside Q and heavy
outside Q in every scenario, has only two possibilities. If Q={p},
scenario A has no allowed pair and cannot give positive light
service. If Q is empty, scenario B cannot satisfy the required
one-heavy-unit equality. Neither common role assignment represents
the original optimum, although both scenario allocations are
individually elementary.

The same example also works for the near-two threshold
theta=alpha*OPT/2 whenever 3/4<alpha<1. For any fixed 0<alpha<1,
replace scenario B's unit value by v=alpha/2 and its capacity by
ceil(2/v). Scenario B then still supplies at least two utility,
so robust OPT remains two, while v<theta=alpha. Changing the
capacity as well as the value is essential. The role is a property
of the scenario allocation, not just the selected player.

There is no complexity obstruction in this example. The selected
basis is already fixed and each scenario can be solved independently.
It only disproves a shared-role promise used without additional
justification.

## 2. A common fractional dummy does not supply a common integer basis

Let

$$
P=\{1,2,3,4\},\qquad M=U_{2,4}.
\tag{CR2}
$$

The dual player matroid is again U_{2,4}. There is one scenario for
each of the six pairs S in binom(P,2). In scenario S use one unit-
valued recipient resource with rank

$$
f_S(A)=|A\setminus S|+\min\{|A\cap S|,1\}.
\tag{CR3}
$$

Thus f_S is the direct sum of a free matroid on P\\S and a rank-one
uniform matroid on S. All original values are one. All assignment
costs, setup fees and budgets are zero. Choose any positive threshold
theta<=1, so every nonzero real pair is heavy in every scenario.
There are no light roles and no role disagreements.

Consider the natural proposed joint fractional all-heavy/dummy LP:
use one common dummy y in P(M*) and one real resource vector x^S in
P(f_S) per scenario, requiring

$$
x^S_p+y_p=1\qquad(p\in P).
\tag{CR4}
$$

It is feasible. Set

$$
y_p=1/2,\qquad x^S_p=1/2
                          \qquad(p\in P,\ S\in\tbinom P2).
\tag{CR5}
$$

The dummy has coordinates at most one and total two, so it belongs
to P(U_{2,4}). Each x^S satisfies the two singleton caps on S and
x^S(S)=1; outside S the matroid is free with singleton caps one.
Those conditions characterize P(f_S), proving real resource
feasibility. The equalities CR4 and all budgets hold exactly.

Nevertheless, the robust integer optimum is zero. An actual
M-basis B is some pair. In the scenario S=B, the total number of
units allocated to B is at most f_B(B)=1. Counts are integral, so
at least one of the two selected players has utility zero.
No actual basis works at positive service in every scenario.

The same conclusion can be stated directly in terms of the proposed
rounding. Suppose y' were a common integer dummy and every scenario
were rounded to integer x'^S satisfying the count floors in CR4.
Its support D would have size at most two. There would therefore
be two dummy-free players u,v. Scenario S={u,v} would require at
least one real unit at both of them, violating x'^S(S)<=1.
Thus no common integer rounded point with these simultaneous
properties exists.

Each scenario separately does have a feasible integral all-heavy/
dummy assignment, but the dummy support can change with the scenario.
Extracting a basis from each scenario's dummy-free ground therefore
does not prove that a single basis is available for all scenarios.
The one-scenario signed-cost rounding proof never supplied this
missing simultaneous dummy constraint.

## 3. Bounding role disagreements alone does not address selection

The preceding four-player example has zero disagreement: every real
unit is heavy in every scenario. More generally, every instance of
the explicit reduction in
[robust-unit-allocation-corank-obstruction.md](robust-unit-allocation-corank-obstruction.md) can be viewed at a
threshold at most one, with the same all-heavy mask in every scenario.
On every positive source instance all selected players receive a
heavy unit in every scenario.

That reduction has robust optimum exactly zero or one and preserves
corank c=k, where k is the Hitting Set parameter. Consequently, under
FPT!=W[2], no deterministic finite-multiplicative robust integer
guarantee in F(c,d)*poly(H) follows merely by adding a parameter d
that is zero on identical all-heavy role patterns. In particular,
a disagreement bound without another hypothesis does not remove
the difficult positive-unit common-selection gate.

The standard Hitting Set classification used here is recorded in
Jansen,
[*On Structural Parameterizations of Hitting Set*](https://arxiv.org/abs/1507.05890),
and in Section 1.1 of Inamdar et al.,
[*Fixed-Parameter Algorithms for Fair Hitting Set Problems*, MFCS 2023](https://drops.dagstuhl.de/storage/00lipics/lipics-vol272-mfcs2023/LIPIcs.MFCS.2023.55/LIPIcs.MFCS.2023.55.pdf).
The reduction and all model-specific implications are proved in
the companion obstruction and its independent audit.

This reasoning does not rule out parameterization by the number
of scenarios, a direct exact common-selection oracle, structural
restrictions on scenario resources, or an additive utility loss.
It also does not imply any specific base lower bound as a function
of q.

## 4. Scenario-specific setup vectors create an additional gate

There is a separate issue if setup fees themselves may vary
arbitrarily with the scenario. Even finding a legal common basis
with zero allocation can encode the same Hitting Set problem.
For each source set S, put

$$
\sigma^S_p=\mathbf1[p\in S],\qquad C_S=|S|-1,
                 \qquad M=U_{q-k,q}.
\tag{CR6}
$$

Give all real assignments zero utility and cost. A basis B meets
every setup budget exactly when

$$
|B\cap S|\le |S|-1
\tag{CR7}
$$

for every S, which says that P\\B is a hitting set. Use the same
empty-set and fresh-element preprocessing as in the companion
reduction. The reduction is explicit and again preserves c=k.

Thus independently minimizing each scenario's setup cost does not
give one attaining basis or a generic feasible zero initialization.
A theorem allowing arbitrary scenario setup vectors needs either
a separately proved common feasibility/optimization interface or
an explicit additional promise. One common nonnegative setup
vector, charged against each scenario's budget, avoids this
particular problem: a minimum-setup basis minimizes the same
quantity for every scenario.

## 5. Positive scopes that remain valid

When the selected basis B is fixed in advance, each scenario is an
independent one-budget allocation problem on B. Its setup fee is
then a fixed scalar, and one-scenario algorithms can be run
separately. The resulting allocations all serve that same B.
In particular, compulsory-player instances do not need a shared
role set at all; each scenario may use its own one-scenario
near-two procedure. An explicit scenario list contributes a
polynomial factor to the running time, not a product of all role
enumerations.

For optional common selection, the additive theorem in
[robust unrelated allocation proof](../../problems/robust-unrelated-allocation/proof.md) instead selects one
actual basis through intersected fractional utility regions and
only then rounds the scenarios separately. With one common setup
vector it gives `(1-epsilon)FOPT-u`, exact per-scenario budgets,
and the existing corank/global time bounds. It does not try to
preserve a shared fractional dummy during rounding.

The unit-valued companion
[robust-unit-allocation-additive-and-promised-two.md](../allocation-and-scheduling/robust-unit-allocation-additive-and-promised-two.md) has an exact
per-scenario quota recovery on a fixed returned basis. Its
unconditional floor(K*/2) bound and its promised factor two for
K*>=2 are compatible with the zero/one obstruction. These are
substantive positive regimes, but neither justifies an unrestricted
multiplicative robust extension of the joint-role theorem.

## 6. Public comparison and status

Robust recoverable matroid bases have an established literature,
but the allowed first-stage/second-stage choices must be compared
literally. Ito, Kakimura, Kamiyama, Kobayashi and Okamoto,
[*A parameterized view to the robust recoverable base problem of
matroids under structural uncertainty*, ORL 2022](https://api.lib.kyushu-u.ac.jp/opac_download_md/7161146/7161146.pdf),
study a recoverable basis model and a scenario-count parameter.
That model is not an automatic solver for the fixed common basis
with adaptive integer service considered here. A bounded primary-
source search did not establish an exact prior match for the
present formulation; no priority claim follows from that search.

The conclusion is a proof boundary, not a claim that all robust
related problems are exhausted. A common role partition is
insufficient even for representing the witness, and a common
fractional dummy is insufficient even after the role issue has
vanished. A valid further multiplicative result must supply a
common integer selection mechanism beyond those two shortcuts.
