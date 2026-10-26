# Robust unrelated allocation with a common setup objective and additive loss

One actual player basis is selected for an explicit list of scenarios.
Assignments adapt to the scenario, values are unrelated, and every
scenario has one exact budget combining the selected basis's setup
fees with its own assignment costs. The setup vector is common to
all scenarios. An intersected fractional service query and a current
minimum-setup basis yield the same corank omission gap as in the
one-scenario theorem. Only after the common basis has been fixed do
we round each scenario separately.

The guarantee is additive: `(1-epsilon)FOPT-u`. In particular, it
does not solve the zero/one robust selection obstruction and is not
an unrestricted multiplicative robust theorem.

## 1. Model, comparator and theorem

Let M be a rank-r matroid on q nonloop players P, where r>=1, and
write c=q-r. The scenario set Omega is nonempty and explicitly
listed. Scenario omega has finitely many resource types j, normalized
monotone integral recipient ranks f_(omega,j), arbitrary nonnegative
rational values v_(omega,p,j), and nonnegative rational assignment
costs a_(omega,p,j). Integer independent count vectors are allocated;
unused capacity is permitted. Let sigma_p>=0 be one setup vector,
the same in every scenario, and C_omega>=0 the scenario budget.

Select one actual M-basis I. Scenario allocations x^omega may
differ, but all budgets must satisfy

$$
\sigma(I)+\sum_{p\in I,j}a_{\omega,p,j}x^\omega_j(p)
                   \le C_\omega\qquad(\omega\in\Omega).
\tag{RA1}
$$

The objective is the minimum utility over all pairs (omega,p)
with p in I. Let OPT be its integer optimum. Define FOPT by
choosing one genuine common M-basis and relaxing only each
scenario's resource counts to real independent vectors under RA1.
The selected basis is not mixed fractionally and does not change
with the scenario.

Put

$$
u_{\omega,p}=\max\bigl(\{v_{\omega,p,j}:
                      f_{\omega,j}(\{p\})\ge1\}\cup\{0\}\bigr),
 \qquad u=\max_{\omega,p}u_{\omega,p}.
\tag{RA2}
$$

Only original zero-singleton coordinates are irrelevant to this
maximum. A positive-cost pair is not removed just because one
whole unit exceeds a residual budget: fractional usage may affect
the stated comparator. H includes the complete scenario list,
all binary data, and the paid polynomial rank, LP and intersection
work.

For 0<epsilon<1 set

$$
R=1/\varepsilon,\quad \alpha=1-\varepsilon,\quad
 A=\Gamma(R)=\frac{R^R}{(R-1)^{R-1}},\quad\beta=2-1/A.
\tag{RA3}
$$

**Theorem RA.** Feasibility of the original zero-utility problem
is decidable in polynomial time. On every feasible instance, a
deterministic algorithm returns one actual M-basis I and explicit
integer scenario allocations satisfying RA1 exactly, with

$$
\sum_jv_{\omega,p,j}x^\omega_j(p)
      \ge \max\{0,\alpha\mathrm{FOPT}-u_{\omega,p}\}
                   \qquad(\omega\in\Omega,\ p\in I).
\tag{RA4}
$$

It uses polynomial workspace and either time

$$
A^c\mathrm{poly}(H)
\tag{RA5}
$$

or, for fixed rational epsilon, time

$$
\beta^q\,
  2^{O(q\log\log(q+2)/\log(q+2))}\mathrm{poly}(H).
\tag{RA6}
$$

The polynomial factors include accuracy and rational-query encoding.
For varying binary accuracy, the global construction may use the
safe rational upper bound 3R in place of Gamma(R), giving base
2-1/(3R) with the same explicit subexponential overhead. The sharp
constant in RA6 is a fixed-accuracy statement.

In particular the robust integer value is at least
max{0,alpha*FOPT-u}, hence at least max{0,alpha*OPT-u}. The number
of scenarios affects H, not the exponential parameter.

## 2. A common setup vector supplies a genuine zero initialization

Compute a minimum-sigma M-basis I_0 by weighted matroid optimization.
Write h_0=sigma(I_0). A feasible common basis exists if and only if

$$
h_0\le\min_\omega C_\omega.
\tag{RA7}
$$

Necessity follows because every basis costs at least h_0 and real
assignment costs are nonnegative. Sufficiency follows by assigning
zero units to I_0 in every scenario. This initializes a legal actual
basis even when FOPT=0. Original player loops may first be deleted:
they are never selected and nonnegative-cost assignments outside
the selected basis can be discarded.

Rank zero and an empty scenario list have convention-dependent
empty-objective meanings and are excluded from the nontrivial
statement. If every scenario has zero total possible positive
utility, or even one scenario has none, then FOPT=0 and I_0 with
zero allocations is already sufficient.

## 3. Exact nonnegative separators for each scenario

For a residual budget B>=0, let

$$
\begin{split}
 U_{\omega,B}=\{z\ge0:\ &\exists x_j\in P(f_{\omega,j}),\quad
             \sum_{p,j}a_{\omega,p,j}x_j(p)\le B,\\
             &z_p\le\sum_jv_{\omega,p,j}x_j(p)
                                      \quad(p\in P)\}.
 \end{split}
\tag{RA8}
$$

This is a compact convex downward region containing zero. It is
monotone in B. Exact membership and polynomial-bit reconstruction
use the direct fractional allocation LP. A strict nonnegative
separating row is available through the nested support LP proved
in [Unrelated-value allocation with an exact budget and a fractional comparator](../unrelated-values-additive/proof.md):
optimize the support for a>=0 using the scenario's resource and
cost LP, then optimize a normalized support-gap problem with
a(P)=1. If a query is outside U_(omega,B), this returns

$$
a\cdot z'\le w,\qquad a\ge0,\quad w\ge0,
\tag{RA9}
$$

strictly violated by the query. If the exact support gap is
nonpositive, reconstruct a fractional allocation for the query.
The positive-part reduction of a signed separator is valid for
a downward region, including lower-dimensional regions.

Resource inequalities have zero-one coefficients and encoded
integer right sides. The only other inner coefficients are original
rational values, costs and a current residual budget. Extreme
support optimizers have a uniform polynomial bit bound by the
usual active-row determinant argument. Their utility vectors give
polynomial-bit inequalities to the outer support LP. Thus all
calls use polynomial oracle time and space, including zero budgets.

No resource is contracted when a player is omitted from the
candidate set. RA8 always uses the original physical ground.

## 4. Current minimum setup and the intersected region

At a node with allowed player set Q, compute an actual minimum-
sigma M-basis I_Q contained in Q, or reject if M restricted to Q
has rank less than r. Put

$$
h(Q)=\sigma(I_Q).
\tag{RA10}
$$

Reject if h(Q)>C_omega for any scenario. Otherwise define

$$
U_Q=\bigcap_{\omega\in\Omega}
                           U_{\omega,C_\omega-h(Q)}.
\tag{RA11}
$$

Membership is tested in all scenarios. If one rejects, its row
RA9 is a valid separating row for U_Q. If all accept, retain or
reconstruct a scenario witness for each one. The explicit scenario
list keeps this polynomial in H.

Given full target t>0 and weak target b=alpha*t, test b*1_Q,
with zeros on P\\Q. If it belongs to U_Q, fix the attained basis
I_Q and discard every real count outside it in every scenario.
Each retained scenario gives service at least b on I_Q and costs
at most C_omega-h(Q). Its common setup charge is exactly h(Q),
not a lower bound obtained from a different basis. Consequently
the fractional original budgets RA1 hold simultaneously.

One may instead use the separately proved attained-set separator
variant to test b*1_(I_Q). The simpler full-Q query is sufficient
for the theorem and avoids any need for that refinement.

## 5. The same protected basis survives every scenario and omission

Fix a genuine common basis I* and fractional scenario allocations
providing full service t and satisfying RA1. Suppose I* is still
contained in Q. Minimum setup gives

$$
h(Q)\le\sigma(I^*),\qquad
             C_\omega-h(Q)\ge C_\omega-\sigma(I^*)\ge0.
\tag{RA12}
$$

The original scenario allocation for I* is therefore feasible in
every current residual region. Hence

$$
t\,1_{I^*}\in U_Q.
\tag{RA13}
$$

If b*1_Q violates a returned row a*z<=w, then

$$
t\,a(I^*)\le w<b\,a(Q),\qquad
        a(Q\setminus I^*)>\varepsilon a(Q)=a(Q)/R.
\tag{RA14}
$$

The weighted first-crossing enumeration supplies a deletion
certificate wholly inside Q\\I*. Delete those players and repeat.
At the new node, recompute h and all queried residual regions;
RA12--RA13 follow again from the same original I*. Different
failed queries may come from different scenarios. Each is valid
for that same protected full service vector.

At zero deficit Q=I*, downward closure makes the weak query
feasible. No protected branch can be rejected by a rank or setup
gate, either. Thus complete failure excludes every common
fractional full-t basis. An early success returns an actual common
basis with fractional service at least b in every scenario.

This is the adaptive residual-budget proof with several residual
budgets driven by one scalar h(Q). It does not minimize independent
scenario setup coordinates separately. All those budgets are
attained by the same I_Q because every one subtracts the identical
setup charge.

## 6. All-input corank time and global conversion

The deficit at Q is d=|Q|-r. The first-crossing certificate family
has the same Kraft-type inequality and deterministic enumeration
bound as in [Single-exponential corank time for weighted packing through first-violation prefixes](../whole-ground-allocation/selection.md):

$$
\sum_D\Gamma(R)^{-|D|}\le1.
\tag{RA15}
$$

All rank tests, minimum-setup computations, scenario separators,
failed candidates and reconstruction work have a uniform polynomial
bound. The recursion therefore costs Gamma(R)^c*poly(H) on all
inputs, including complete failures. Its depth is at most c<=q
and all numerical quantities are recomputed from original data,
so it uses polynomial workspace.

Starting after forced omissions Z costs Gamma(R)^(c-|Z|)*poly(H).
If a full witness I* avoids Z, RA12--RA14 remain valid. The
polynomial-space global conversion therefore supplies RA6 for
each rational target. Bad forced seeds and their failure work are
charged by the same uniform bound. No small-corank, support or
scenario-role promise is needed for RA6.

## 7. A fixed-basis rational comparator removes target-search loss

Let F be the fixed nonempty family of M-bases I satisfying
sigma(I)<=min_omega C_omega. For any specified I in F, optimize
the exact LP

$$
\begin{array}{ll}
 \text{maximize}&\lambda,\\
 \text{subject to}&x^\omega_j\in P(f_{\omega,j})\quad(\omega,j),\\
 &x^\omega_j(p)=0\quad(p\notin I),\\
 &\sum_j v_{\omega,p,j}x^\omega_j(p)\ge\lambda
                       \quad(\omega,\ p\in I),\\
 &\sum_{p,j}a_{\omega,p,j}x^\omega_j(p)
                       \le C_\omega-\sigma(I)\quad(\omega),\\
 &0\le\lambda\le V,
 \end{array}
\tag{RA16}
$$

where

$$
V=\min_\omega\sum_j
                     (\max_p v_{\omega,p,j})f_{\omega,j}(P).
\tag{RA17}
$$

The LP is bounded and nonempty, since zero counts are feasible.
Its optimum lambda_I is computable in polynomial oracle time,
and max_(I in F) lambda_I is exactly FOPT. Both this family and
RA16 are independent of the target queried by the gap routine.

For clarity, the uniform rational denominator bound is obtained
from RA16 itself, not from whatever separators a search happens
to query. There are at most
n=1+q*sum_omega(number of types in omega) variables. All resource
rows have entries zero or one and right sides at most the queried
full rank. Values, costs and C_omega are original encoded rationals;
sigma(I) is a sum of at most q original fees, with a known uniform
polynomial bit bound. The bound V is explicitly computed. Thus one
can compute an integer L of polynomial size such that every
coefficient and right side, uniformly over I, has numerator and
denominator of magnitude at most 2^L.

After rowwise denominator clearing, entries are bounded by
W=2^((n+2)L). A safe denominator bound for every optimum lambda_I
is

$$
D=n!W^n.
\tag{RA18}
$$

It has polynomial bit length; exponentially many rank rows do not
change the number of active rows needed at a vertex. Zero-fixed
variables or lower-dimensional faces do not prevent this bound.

Apply [Rational comparator recovery without splitting the approximation error](../whole-ground-allocation/rational-optimization.md) with alpha=A_0/B_0
in lowest terms and grid delta=1/(2*B_0*D^2). Initialize with I_0
and zero service; use an external upper grid point strictly
larger than V. Success records an actual returned basis, while
failure is sound for the fixed full comparator by Section 5.
At adjacent endpoints the saved lower target is greater than
FOPT-delta. Reoptimize RA16 on the saved basis. Rational separation
of denominators at most D then gives

$$
\lambda_I\ge\alpha\mathrm{FOPT}.
\tag{RA19}
$$

The number of calls and all query encodings are polynomial in H
and the accuracy encoding. In particular, no positive fractional
lower scale and no division of epsilon into two losses are needed.

## 8. Fix the common basis before rounding every scenario

Take the exact RA16 witnesses of the saved actual basis I. For
each scenario independently apply the accepted unrelated-value
lower-rounding lemma with its one assignment-cost objective.
Its free-disposal extension converts independent resource counts
to bases without adding real cost. Complement ranks and all
per-player value-prefix ceilings give an integral maximum-total
polymatroid-intersection face. Maximizing the scenario's cost on
the complement face returns original integer assignments of no
greater cost and utility at least

$$
\lambda_I-u_{\omega,p}
                                           \quad(p\in I).
\tag{RA20}
$$

Discard disposal and all real counts outside I. Nonnegative
original costs make that safe; selected utilities do not change.
Because the scenario's cost remains at most
C_omega-sigma(I), RA1 still holds exactly. Repeat for every
scenario using the same fixed I. This proves RA4.

The count vectors need not be equal across scenarios. No dummy
selection is rounded separately in different scenarios, and no
one integer assignment must preserve several cost objectives.
Each scenario has its own one-objective rounding problem, after
the common discrete selection has already been made.

Only polynomially many count entries are output, each in binary.
The total output size and the simultaneous stored scenario
witnesses are polynomial in H. They can also be reconstructed
and written one scenario at a time.

## 9. Interpretation, limits and primary public background

If u<=rho*FOPT for a specified rho<alpha, the returned robust
value is at least (alpha-rho)*FOPT. Without such a small-unit
condition the additive loss may absorb the comparator entirely.
On the robust unit zero/one obstruction, u=1 and this is exactly
what permits a legal zero guarantee. The theorem therefore does
not contradict [Robust integer unit allocation has a corank-parameter obstruction](../../manuscripts/mechanism-boundaries/robust-unit-allocation-corank-obstruction.md).

The common setup vector is a real restriction. Arbitrary scenario
setup vectors can already encode common-basis feasibility via
Hitting Set, as shown in
[Two obstructions to lifting one-scenario roles into robust allocation](../../manuscripts/mechanism-boundaries/robust-unrelated-common-role-obstructions.md). More generally the
argument extends to several residual budgets only when their
completion charges are monotone functions of one exactly
minimized scalar cost and the same optimizer attains them all;
that extra interface must be proved for any proposed application.

Cost-preserving additive allocation rounding is public background;
see Rohwedder, Rouhani and Wennmann,
[*Cost Preserving Dependent Rounding for Allocation Problems*,
ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127).
The explicit recipient-polymatroid, disposal and value-prefix
implementation used here is supplied by the project's accepted
unrelated budgeted rounding notes. The exponential base conversion
is public monotone-local-search background from Fomin, Gaspers,
Lokshtanov and Saurabh,
[*Exact Algorithms via Monotone Local Search*](https://arxiv.org/abs/1512.01621),
with the separately proved streamed polynomial-space implementation.

The theorem's content is the common-basis robust composition with
an attained common setup charge, a true selected-basis fractional
comparator, and independent exact-budget scenario recovery. A
bounded primary-source comparison is not an exhaustive priority
search. This manuscript makes no claim of external review, formal
verification, or a new general-purpose rounding theorem.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
