# General-value near-two allocation with an arbitrary player matroid

**25 October 2026. New research manuscript; root and independent audits requested.**

This note extends the compulsory-player result in
`general_value_allocation_heavy_cover_near_two.md` to an arbitrary
original player-selection matroid. It uses the independently reviewed
additive workload algorithm and an explicit dual-union adapter. The
nonlinear parameter is the corank of the derived light-player matroid,
after deleting its loops. It is not generally the original player
matroid's corank alone.

For every positive rational eta, the result gives factor `2+eta` in
time `(O(1+eta^{-1}))^k poly(H)` when the derived corank at threshold
`OPT/(2+eta)` is at most k. The complete algorithm retains a public
constant-factor fallback without assuming that this condition holds.

## 1. Model and the derived parameter

Let M be a matroid of positive rank r on a finite set P of potential
players. A solution chooses a basis B of M. Each resource type j has
a positive rational intrinsic unit value v_j and an integral normalized
monotone submodular rank f_j on P. Its allocated integer count vector
belongs to P(f_j). The objective is

\[
                   \min_{p\in B}\sum_j v_j n_j(p).
 \tag{J1}
\]

Resource types have independent feasibility constraints. Unused units
are allowed; there is no additional local constraint coupling distinct
types. Integer coordinate bounds may already be incorporated into the
individual ranks. Values are common intrinsic values, not arbitrary
player-dependent values. Let OPT denote the integer optimum.

Delete all loops of the original M and restrict every resource rank to
the remaining ground. All original bases avoid those loops, and zero
extension preserves resource feasibility, so this preserves OPT. Rename
the new ground P and let q=|P|. Discard zero-value or zero-rank types.
If none remains, any basis with empty counts is optimal. Rank-zero
original instances return the empty basis separately, with no finite
minimum over an empty set asserted.

For a positive threshold theta, let heavy types have value at least
theta, and light types have value strictly below theta. Define

\[
 f^b_\theta=\sum_{j:v_j\ge\theta}f_j,
 \qquad N_\theta=\operatorname{Boolean}(f^b_\theta),
 \qquad U_\theta=M^*\vee N_\theta,
 \qquad K_\theta=U_\theta^*.
 \tag{J2}
\]

Here `Boolean(f)` is the matroid of player sets whose indicator lies
in P(f). It is the integral polymatroid intersected with the unit
coordinate box. Its independence means that each player can receive
one heavy unit. The aggregate independent count vector can be
decomposed among the original heavy types in polynomial oracle time.

Let Q_theta be the nonloop set of K_theta, and put

\[
          \delta(\theta)=r(K_\theta),
       \qquad c(\theta)=|Q_\theta|-\delta(\theta).
 \tag{J3}
\]

If delta=0 then Q_theta is empty and c(theta)=0. The parameter c(theta)
need not be monotone in theta; the algorithm below does not require
monotonicity.

Write nu(M,N) for the maximum cardinality of a common independent set.
The exact rank identity is

\[
                  \delta(\theta)=r-\nu(M,N_\theta).
 \tag{J4}
\]

Consequently

\[
       c(\theta)\le q-r+\nu(M,N_\theta)
                    \le(q-r)+r(N_\theta).
 \tag{J5}
\]

Thus the sum of the original corank and heavy-cover rank is a sufficient
upper parameter, while deleting derived loops can improve it. When M
is free, K=N*, and this specializes exactly to the compulsory-player
parameter `rank(N)-number_of_coloops(N)`.

All Boolean-cap, dual and union ranks, decompositions and extensions are
paid polynomial oracle operations. For example, the Boolean-cap rank
is `min_{A subseteq S} f^b(A)+|S\A|`; dual ranks use the usual complement
formula; union ranks use matroid union or submodular minimization. No
resource capacity is expanded into numerical unit copies.

## 2. The rank identity and a stronger completion fact

For completeness, (J4) can be proved constructively. If F is common
independent in M and N, extend it to an M-basis B. The disjoint union
`(P\B) union F` is independent in M* vee N and has size q-r+|F|.
Conversely, decompose a union basis into `C dot-union D`, with C
independent in M* and D independent in N. Extend C to an M*-basis
C'. At most q-r-|C| members of D are lost. The retained set D\C'
is independent in N and contained in the M-basis P\C', giving
the reverse inequality `rank(U)<=q-r+nu(M,N)`.

The following more precise fact is needed to preserve a particular
light-player set during output recovery.

**Union-basis spanning lemma.** Every basis S of U=M* vee N contains
a basis of M*. In fact, any independent M* component C of a union
decomposition `S=C dot-union D` can be extended to an M*-basis using
only members of S.

**Proof.** Suppose `r_(M*)(S)<r_(M*)(P)`. There is an element e outside
S with `r_(M*)(S+e)>r_(M*)(S)`. Such an e is outside the M*-closure of
every subset of S, including C. Thus `C+e` remains independent in
M*, and `(C+e) dot-union D=S+e` is independent in U, contradicting
that S is a U-basis. Hence S has full M* rank, and ordinary matroid
augmentation extends C within S to an M*-basis. Square.

**Completion corollary.** For every K-basis I, a basis B of the
original M containing I can be recovered so that B\I is independent
in N.

Indeed, S=P\I is a U-basis. Decompose it as above and extend C to
an M*-basis C' entirely inside S. Then

\[
                     B=P\setminus C',
               \qquad B\setminus I=S\setminus C'\subseteq D.
 \tag{J6}
\]

The first set is an M-basis, it contains I because C' avoids I, and
the second set is independent in N. This proves both the structural
fact and a polynomial construction. Extending C without restricting
it to S would not establish containment of I; the spanning lemma is
the step that makes the recovery precise.

The corollary also handles delta=0: take I empty and S=P, which is
a U-basis in this case. It returns a full M-basis independently
coverable by heavy units. Equivalently, (J4) says that M and N have
a common basis of size r. No minimum value over an empty light set
or a positive-rank inner quota problem is needed.

## 3. The optimum supplies a derived light-only basis

Fix any integer original allocation of value at least T on an M-basis
B*. Let R be the players in B* receiving at least one heavy unit.
Dropping to one such unit per player shows that R is independent in N.
Write L=B*\R for its light-only selected players.

The complement of L has the disjoint decomposition

\[
             P\setminus L=(P\setminus B^*)\mathbin{\dot\cup}R.
 \tag{J7}
\]

Its first component is an M*-basis and its second is N-independent.
It is therefore U-independent. Extend it to a U-basis S*. Its
complement I*=P\S* is a K-basis satisfying

\[
                                  I^*\subseteq L.
 \tag{J8}
\]

Every member of I* receives value at least T using only light types
in the original allocation. Restricting to these players preserves
the resource inequalities. Deleting K-loops also preserves this
witness because every K-basis avoids them.

This proof does not assume that all original selected players lacking
a heavy unit themselves form a K-basis. They need only contain one.
It also does not guess which heavy units or which players an optimum
uses. The union extension constructs the promise existentially from
any optimum, and the algorithm solves the derived instance directly.

## 4. The algorithm for one fixed heavy/light split

Fix rational `0<epsilon<1` and an integer budget k>=0. Enumerate all
distinct splits into a prefix of light value classes and a suffix of
heavy value classes, including either empty side. At most one more
than the number of distinct explicit values is needed.

For a fixed split construct N,U,K and its loop-deleted ground Q.
Write

\[
 a_H=\min_{j\text{ heavy}}v_j,
 \qquad u_L=\max_{j\text{ light}}v_j,
 \tag{J9}
\]

with a_H=infinity when there are no heavy types and u_L=0 when there
are no light types.

If rank(K)=0, use (J6) with I empty and give one heavy unit to every
member of the resulting M-basis. Record this legal candidate. The
positive original rank ensures that this branch cannot occur with
an empty heavy set. It is processed in polynomial time regardless
of the supplied budget.

If rank(K)>0 but c=|Q|-rank(K)>k, skip this split. A skip says nothing
about original feasibility or the original optimum.

For every other split, restrict the light resource ranks to Q and
run the additive algorithm of
`corank_arbitrary_value_additive_allocation.md` on player matroid K|Q.
If OPT_L denotes the integer light-only optimum over its bases, it
returns a K-basis I and original light counts with minimum value at
least

\[
                       \max\{0,(1-\epsilon)\mathrm{OPT}_L-u_L\}
 \tag{J10}
\]

in `Gamma(1/epsilon)^c poly(H)` time, where
`Gamma(R)=R^R/(R-1)^(R-1)<=eR`. Using u_L from before restriction
only weakens the paid rounding loss. If all restricted light ranks
are zero, an arbitrary K-basis with zero counts is the legitimate
output of this step.

Recover an original M-basis B containing I by (J6). Give every player
in B\I one heavy unit. Its indicator is in the heavy aggregate
polymatroid and is decomposed among the original types. Since heavy
and light types are disjoint, this cannot disturb the light counts.
Any counts outside B may be discarded. The candidate's actual value
is at least

\[
                 \min\{a_H,(1-\epsilon)\mathrm{OPT}_L-u_L\},
 \tag{J11}
\]

whenever the displayed expression is positive; the actual value is
always nonnegative. The final algorithm compares actual achieved
integer values, so a negative expression is never used as an objective.

For no heavy types, N is zero and K=M; the completion in (J6) leaves
B=I, and only the light value matters. For no light types with
positive derived rank, a zero-value candidate is valid but need not
improve the fallback. A zero-rank pure-heavy candidate is not asserted
to optimize the entire original instance; other splits may do better.

## 5. The target grid and integer rounding remain explicit

The invocation in Section 4 is a complete optimization algorithm,
not an oracle for an unimplemented value promise. Its exact numerical
interface can be summarized as follows. Choose an original value
quantum g with `v_j/g` integral and write `epsilon=e/d`, with
`0<e<d`. Put `Delta=g/d` and form the light workload rank

\[
                    F(S)=\sum_{j\text{ light}}(v_j/\Delta)f_j(S).
 \tag{J12}
\]

At target T=m g, the integer quotas are `t=md` and `b=m(d-e)`.
Their positive gap has exactly `t/(t-b)=1/epsilon`; this is valid
even at the smallest positive grid target. The omitted-player
branching parameter is the fixed c for this split, never the
original selection rank or a numerical resource supply.

Successful workload vectors are completed and decomposed on the
polynomial-size player-by-type ground. Division by their scaling
factors produces fractional original-resource bases. The reviewed
per-player lower-rounding lemma loses at most u_L. It does not
couple the light resources to the separately chosen heavy counts.

The original integer light-only optimum is a g-grid value. Its total
light value gives an external upper certificate for the one-sided
maximization search; success may occur above that optimum, while
failure is a sound full-target infeasibility statement. Thus the
routine returns (J10) without assuming monotone algorithmic success.
All input numbers, quotas and ranks stay binary encoded with
polynomial bit lengths. There is no original-unit granularity loss
in addition to the explicitly paid u_L.

## 6. Near-two guarantee at the optimum threshold

Define

\[
                          \theta^*={(1-\epsilon)\mathrm{OPT}\over2}.
 \tag{J13}
\]

Assume OPT>0 and c(theta*)<=k. The split at theta* appears among the
enumerated value-class splits, with equality assigned to the heavy
side. By Section 3, its derived light-only integer optimum satisfies
`OPT_L>=OPT` whenever its derived rank is positive. If its rank is
zero, the pure-heavy candidate already has value at least theta*.

Otherwise this split is processed, and its light output has value
at least

\[
        (1-\epsilon)\mathrm{OPT}-u_L
                   =2\theta^*-u_L>\theta^*.
 \tag{J14}
\]

Every heavy unit has value at least theta*. Completion by (J6)
therefore yields a full original M-basis of value at least theta*.
The use of the strict light inequality is essential at this step.

**Theorem J.** For every rational `0<epsilon<1` and supplied budget
k, a deterministic algorithm has running time

\[
                       \Gamma(1/\epsilon)^k\operatorname{poly}(H)
 \tag{J15}
\]

and polynomial workspace. If OPT>0 and `c((1-epsilon)OPT/2)<=k`, it
returns a legal allocation on a basis of the arbitrary original player
matroid with minimum value at least `(1-epsilon)OPT/2`. If OPT=0,
any legal basis allocation meets this bound, with no threshold or
parameter hypothesis; c(theta) need not be evaluated at theta=0.

The polynomial degree is independent of k and epsilon. The number
of splits, rank computations, reconstruction steps and target trials
only adds polynomial factors. The expression Gamma need not be
numerically evaluated by the algorithm.

For rational eta>0, choose `epsilon=eta/(2+eta)`. The guarantee becomes

\[
       \operatorname{value}\ge{\mathrm{OPT}\over2+\eta},
 \qquad
       c\left({\mathrm{OPT}\over2+\eta}\right)\le k,
 \tag{J16}
\]

with time

\[
       \Gamma\!\left({2+\eta\over\eta}\right)^k\operatorname{poly}(H)
             \le\left({e(2+\eta)\over\eta}\right)^k\operatorname{poly}(H).
 \tag{J17}
\]

The sufficient bound in (J5) gives the same conclusion when the
original corank plus the common heavy-cover rank is at most k,
or when the still simpler original corank plus rank(N_theta*) is
at most k. None of these statements replaces c(theta*) by original
corank alone without an additional instance condition.

## 7. A complete fallback for arbitrary original player selection

The algorithm returns the best actual value among all split candidates
and a polynomial constant-factor fallback. The public all-player
recipient-polymatroid `(8+zeta)` result, for fixed zeta>0, transfers to
the current original-M model by the following explicit construction.

Let V be the total value of the original resource ranks on P. Add one
dummy type of value V+g with recipient rank equal to the matroid rank
of M*. Make every player compulsory in this augmented instance.
First extend every original independent resource vector of an
optimal M-basis allocation to a full recipient base on P. This
does not lower any original selected player's value. Assign one
dummy unit to each member of the complementary M*-basis. The
result is a feasible all-player allocation of full resource bases
with minimum value at least OPT, matching the public theorem's
base model. Therefore its all-player integer optimum is at least OPT.

Run the public `(8+zeta)` algorithm. The players D receiving dummy
units form an M*-independent set, since that recipient resource is
itself a matroid and has singleton capacities at most one. Extend D
to an M*-basis D'. Its complement B=P\D' is an original M-basis
and none of its players received a dummy. Their entire guaranteed
value therefore comes from original resources. Remove the dummy
resource and discard original counts outside B. The value on B is
at least OPT/(8+zeta).

This fallback is polynomial for fixed zeta. It is valid even when
every split useful for (J16) exceeds the budget; no cap failure is
misclassified as infeasibility. Both the new split candidates and
the fallback are explicit legal original allocations, so returning
their best actual value preserves every applicable guarantee.

## 8. Comparison, dependencies and remaining boundaries

The public primary anchor is Bamas et al.,
[arXiv:2307.08453v1](https://arxiv.org/html/2307.08453v1), Theorem 4,
for the all-player arbitrary-value recipient-polymatroid factor
`8+zeta`, with the original-player-matroid transfer proved in Section
7. Its Theorem 21 supplies the known largest-unit additive rounding;
the binary-size per-player proof used here is recorded separately
in the additive manuscript. The present note does not claim that
rounding primitive as new.

The near-two result instead combines the new corank workload gap
with an explicit light-only basis promise and heavy completion.
The dual-union adapter is the same structural construction used in
`fat_deficiency_parameter_allocation.md`, but the exponent now depends
on the derived corank rather than its rank. Equations (J6)--(J8)
spell out the preservation steps needed for the different inner
algorithm. It is not an inference from a compulsory-player easy LP
branch to optional player selection.

This is an integer-OPT statement. It imposes no two-value restriction,
no small-unit assumption on the original instance, and no bound on
binary resource supplies. It retains common intrinsic values and
independent resource polymatroids, and it does not include local
constraints coupling different resource types. It does not set eta
to zero or claim exact factor two for arbitrary values.

Existing oracle lower bounds strictly below factor two in unit allocation
or two-value compulsory allocation remain valid within their stated
parameters. A lower bound for the specific threshold-derived
parameter c(OPT/(2+eta)) needs a separately aligned construction.
This note makes no matching lower-bound or optimal-exponential-base
claim for that parameter, and no exhaustive publication-priority
claim. Root and independent review remain requested for this new
extension.
