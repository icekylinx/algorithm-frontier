# Verification note

**Curated source path:** `sources/checkpoint-o/recipient_polymatroid_aggregate_configuration_gap.md`

The source audit follows.

# An aggregate recipient-polymatroid configuration LP has a rank-sized gap

**25 October 2026. Explicit finite construction; independent audit requested.**

This note identifies a necessary comparator distinction. It does not rule out
a constant approximation to the integer allocation problem. In particular,
the new integer-optimum argument in
`general_recipient_polymatroid_integer_optimum_transfer.md` does not use the
relaxation refuted here.

## 1. Model of the relaxation being tested

Let a player-selection matroid have rank r. For each player p, put mass x_p
on feasible integral count-vector configurations of value at least T, with
x in the player-basis polytope. For resource j, let y_pj be the expected
number of its units in the configurations of p. The aggregate recipient
constraint is

\[
                         y_{\cdot j}\in P(f_j),
\]

where f_j is an integral polymatroid rank function on the players. This is
the direct count-vector analogue of the recipient-matroid configuration
relaxation. It omits information about any separately supplied decomposition
of f_j into physical resource types or recipient-matroid copies.

## 2. Construction

Fix integers r>=2 and D>=r. There are q=Dr players and the selection
matroid is the uniform matroid U_(r,q). There is one resource, every unit
has value one, and its rank function is

\[
 f(\varnothing)=0,\qquad f(S)=|S|+D\quad(S\ne\varnothing).
 \tag{G1}
\]

This function is normalized, monotone, integral and submodular. Indeed it
is the sum of the free-matroid rank |S| and D copies of the rank-one
uniform-matroid rank min(1,|S|). No difficult or nondecomposable polymatroid
is needed.

For each player, D+1 units form a feasible singleton-player configuration
of value T=D+1, since f({p})=D+1. Give that configuration mass

\[
                     x_p=1/D,\qquad y_p=(D+1)/D.
 \tag{G2}
\]

Every coordinate of x is at most one and sum_p x_p=q/D=r, so x lies in
the uniform-matroid basis polytope. For a nonempty set S of size s,

\[
 y(S)=s+s/D\le s+D=f(S),
\]

because s<=q=Dr<=D^2. Hence (G2) is feasible in P(f), and the aggregate
configuration target D+1 is feasible.

## 3. Exact integer optimum

An integral allocation selects exactly r players. For their set I, the
resource bound is n(I)<=r+D. Therefore its least supplied selected player
has at most

\[
                         1+\lfloor D/r\rfloor
\]

units. This bound is attained: give each selected player exactly that
many units. For every subset A of selected players,

\[
 n(A)=|A|+|A|\lfloor D/r\rfloor\le |A|+D.
\]

Sets containing unselected players have a no smaller rank bound and no
additional allocation, so all polymatroid inequalities hold. Thus

\[
 \mathrm{OPT}_{\rm int}=1+\lfloor D/r\rfloor,
 \qquad
 \frac{T_{\rm aggregate\,config}}{\mathrm{OPT}_{\rm int}}
 \ge\frac{D+1}{1+\lfloor D/r\rfloor}.
 \tag{G3}
\]

Taking D=rL and letting L grow makes this ratio tend to r. Consequently
no rank-independent constant guarantee against this aggregate relaxation
can hold for arbitrary integral recipient polymatroids and arbitrary
player selection. For example r=6 and sufficiently large D already
exclude a universal factor-five assertion against this comparator.

## 4. Why a supplied decomposition has a stronger comparator

The integer resource in (G1) can also be presented as two resource types
of unit value: one free-recipient matroid copy and D rank-one recipient
matroid copies. The integer feasible count vectors are identical after
forgetting which type supplied a unit.

Their component-level configuration relaxation is different. A
configuration of D+1 units for a player must use its one free-recipient
service and all D rank-one copies. Under (G2), the expected usage of the
rank-one type is D x_p=1 per player, so its total expected usage is
q=Dr>D. That violates the supplied rank-one type's capacity. The bogus
configuration point cannot be lifted to the component-level relaxation.

Therefore a theorem for binary multiplicities of supplied recipient
matroids may safely use its separate per-type columns and count-vector
configurations. It must not merge components with different recipient
matroids into one aggregate polymatroid and claim preservation of the
same configuration comparator.

## 5. Public scope

Bamas, Lindermayr, Megow, Rohwedder and Schloeter,
[*Santa Claus meets Makespan and Matroids: Algorithms and Reductions*,
arXiv:2307.08453v1](https://arxiv.org/html/2307.08453v1), give an
8+epsilon polynomial approximation for their general recipient
matroid/polymatroid allocation problem, and 4+epsilon for two values.
Those are guarantees against integer optimum, and the displayed model
makes all players compulsory. The dual dummy-resource reduction discussed
in the checkpoint transfers their integer guarantee to arbitrary player
selection. Nothing in (G1)--(G3) contradicts that public result.

The construction only refutes the specified aggregate configuration
comparator. It is not a computational hardness lower bound, an
approximation lower bound against integer optimum, or a claim that every
possible strengthened polymatroid relaxation has this gap.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
