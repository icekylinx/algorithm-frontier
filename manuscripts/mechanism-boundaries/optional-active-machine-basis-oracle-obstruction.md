# Optional active machine bases: an oracle obstruction before approximation

**25 October 2026. Complete obstruction manuscript; internal review requested.**

The weighted prefix-free corank packing theorem does not automatically
extend to choosing an active machine basis on which all mandatory jobs
must be scheduled. In the full recipient-polymatroid value-oracle model,
this natural extension is impossible in fixed-parameter corank time:
finding any feasible schedule already identifies a hidden subset.

The obstruction uses one unit-size job type, identical processing times,
zero assignment costs and a uniform active-machine matroid. It therefore
applies in particular to unrelated processing times with a single exact
assignment-cost budget. It does not assert hardness for explicitly
represented ordinary eligibility lists.

## 1. The model that is ruled out

Let P be q candidate machines and let M be a rank-r matroid on P. The
algorithm must select an actual M-basis I. Only machines in I may run
jobs; every machine outside I receives zero jobs. A job type j has an
integral normalized monotone submodular recipient rank f_j. A complete
integer schedule is a vector x_j in the base polytope B(f_j):

$$
x_j(S)\le f_j(S)\quad(S\subseteq P),\qquad
 x_j(P)=f_j(P),\qquad x_j\in\mathbb Z_{\ge0}^{P}.
 \tag{A1}
$$

It must additionally satisfy x_j(p)=0 for p outside I. Its machine loads
are sum_j p_pj x_j(p), for nonnegative rational machine-dependent
processing times. A single assignment budget may require
sum_(p,j) c_pj x_j(p)<=C. Define the selection corank c=q-r, after any
valid deletion of original machine-matroid loops.

The theorem below rules out a uniform deterministic running time
F(c) poly(H) even for returning a feasible schedule on promised-feasible
instances. Consequently no finite multiplicative or additive makespan
guarantee in such time can hold for this whole oracle model.

The support requirement and mandatory base equalities in (A1) are
essential. In allocation, unused resources can be discarded and the
chosen players only need adequate service. Here all job units must be
assigned on the selected support.

## 2. A hidden integral polymatroid

Fix integers c>=2 and q>=c+2, and put r=q-c. For every hidden r-element
set A subseteq P, define

$$
f_0(S)=\min\{2|S|,2r\}-{\bf1}[|S|=r],
 \tag{A2}
$$

$$
f_A(S)=f_0(S)+{\bf1}[S=A].
 \tag{A3}
$$

These are the rank functions used in the earlier self-contained
[allocation lower bounds proof](../../problems/allocation-lower-bounds/proof.md). Their complete
validity check is repeated here because the present obstruction has a
different interpretation and does not depend on an approximation
threshold.

For f_0, the cardinality increments are r-1 increments of two, followed
by one, one, and then zeros. They are nonnegative and nonincreasing.
Thus f_0 is normalized, monotone, integral and submodular.

Raising f_0(A) by one preserves monotonicity: a proper subset of A has
value at most 2r-2, whereas every strict superset of A has value 2r.
For submodularity, only raising a term on the right side of
f(X)+f(Y)>=f(X union Y)+f(X intersection Y) can cause difficulty.
If X union Y=A and neither X nor Y equals A, both sets are smaller
than r and their original slack is exactly one. If X intersection Y=A
and neither set equals A, both are strict supersets and their original
slack is again one. The increase consumes that slack. In a nested case
the same raised term appears on both sides; a raised left-side term
cannot hurt. This covers all cases.

Every oracle value has O(log q) bits. In particular,

$$
f_A(P)=2r,
 \qquad
 f_A(I)=
 \begin{cases}
 2r,&I=A,\\
 2r-1,&|I|=r,\ I\ne A.
 \end{cases}
 \tag{A4}
$$

All singleton values equal two because r>=2. There are no ineligible
individual machines that reveal the hidden set during preprocessing.

## 3. Feasibility uniquely identifies the active basis

Let the active-machine matroid be the uniform matroid U_(r,q). There
is one job type with recipient rank f_A and processing time one on
every machine. Thus precisely 2r unit jobs must be assigned. Set all
assignment costs to zero and C=0.

For any active basis I and any complete schedule supported on I,

$$
2r=x(P)=x(I)\le f_A(I).
 \tag{A5}
$$

Equation (A4) forces I=A. This implication holds even if the algorithm
is allowed arbitrarily large makespan: additional load on the selected
machines cannot create an extra unit of recipient rank.

Conversely, x=2*1_A is a feasible base. If |S|<r, its count is at most
2|S|=f_A(S). If S=A, equality holds at 2r. If |S|=r and S is not A,
the count is at most 2r-2<2r-1=f_A(S). If |S|>r, its count is at
most 2r=f_A(S). These are all subsets.

Hence every constructed instance is feasible, its unique feasible
active basis is A, and its optimal makespan equals two. The equality
also follows from 2r mandatory unit jobs on r active machines. Its
assignment cost is zero, satisfying the single budget exactly.

The lower bound therefore persists even if the algorithm is given
the optimum makespan two in advance and is promised feasibility.

## 4. The deterministic query lower bound

For every A, the value oracle f_A differs from f_0 at exactly the
query S=A. Answer all queries by f_0 until the algorithm asks the
hidden set. Queries of other cardinalities reveal nothing about A.

If at least two r-sets remain unqueried, the entire transcript is
consistent with either being the hidden set. A deterministic
algorithm has the same output after that transcript, but a legal
active basis must equal the hidden set. A single output cannot be
correct in both instances. Returning infeasibility is also invalid,
because both instances are promised feasible.

It follows that the worst-case number of recipient-value queries is

$$
{q\choose r}-1={q\choose c}-1.
 \tag{A6}
$$

This is a bound on producing any valid schedule, not just on choosing
an optimal one. No computational assumption such as P!=NP or a
parameterized complexity conjecture is needed.

To see why (A6) excludes a uniform F(c) poly(H) algorithm, suppose its
polynomial degree in the explicit ground size and numerical bit
lengths is a fixed constant D. Choose a fixed integer c>D (or a
larger fixed c if a particular encoding adds a constant polynomial
factor). Let q tend to infinity. The explicit input here consists
of the uniform-matroid parameters, q unit processing times and zero
costs; rank answers have O(log q) bits. The claimed bound is therefore
F(c) q^D polylog(q), up to a fixed polynomial encoding adjustment,
whereas binom(q,c) grows as q^c/c!. The latter eventually exceeds it.

Equivalently, for any proposed constant polynomial degree, choose a
larger fixed corank and then a sufficiently large ground. Dependence
hidden in F(c) cannot absorb a larger power of the unbounded q.

## 5. Why complementing the selected machines does not repair the route

For a fixed available machine set Q, the condition that job type j
can be assigned wholly within Q is

$$
f_j(Q)=f_j(P).
 \tag{A7}
$$

Adding available machines can only help (A7). A current set Q that
contains a promised active basis may therefore support all jobs even
when no useful capacity-violation witness identifies which machines
to delete. In the example, P supports all jobs, but only one of its
rank-r subsets continues to do so.

One may encode the deleted set D=P\I and regard preserving full
recipient rank as a downward condition on D. That changes the
selection family to bases of the dual matroid M*, whose rank is c.
The omission theorem's parameter is then q-c=r, not c. The symmetry
of binom(q,c)=binom(q,r) is consistent with this change; it does not
turn the lower bound into an FPT algorithm for the original corank.

More generally, a service projection with nonnegative packing rows
must be defined and proved to represent the intended output. Treating
active-machine availability as if it were lower service, dropping the
base totals, or allowing jobs outside the selected basis changes the
problem. The present example detects all three substitutions.

## 6. Fixed machines have a different, classical additive baseline

If all physical machines remain available, a fractional schedule of
load at most T_p and assignment cost at most C can be rounded with
one largest-unit additive load per machine while preserving that one
cost bound. For ordinary unrelated jobs, this is the classical
Shmoys--Tardos guarantee: [*An approximation algorithm for the
generalized assignment problem*, Mathematical Programming 62
(1993), Theorem 2.1 and the following multiplicity remark](https://www.cs.cornell.edu/~eva/Approx.Algorithm.Generalized.Assignment.Prob.pdf).
It is a public baseline, not a corank-selection breakthrough.

For completeness, the same prefix-intersection interface used by the
present project gives its job-polymatroid version. Let x_j be the
fractional job bases and, independently at each machine p, order types
by decreasing p_pj. Set the prefix bound

$$
C_{p,k}=\left\lceil\sum_{\ell\le k}x_{j_p(\ell)}(p)\right\rceil.
 \tag{A8}
$$

On the q times number-of-types coordinates, intersect the direct sum
of the original resource polymatroids with the prefix polymatroid
whose rank is the sum, over machines, of the largest included prefix
bound. The fractional x lies in this intersection and has the full
sum of resource ranks. Its maximum-total face is integral. Minimize
the one assignment-cost objective on that face. An integer minimizer
has cost no larger than x and retains every job type's full base total.
Prefix telescoping bounds its load at p by

$$
\sum_j p_{pj}x_j(p)+\max_{j:\, f_j(\{p\})>0}p_{pj}.
 \tag{A9}
$$

The construction uses polynomially many coordinates and binary
counts. No job-unit expansion is necessary. It is the upper-load
counterpart of the existing cost-preserving lower-utility rounding.

This rounding presupposes that the allowed support is already fixed
and a fractional full-job assignment exists there. It does not choose
a feasible active basis; applying it after such a choice cannot avoid
(A6). In particular, a parameter-free fixed-machine additive guarantee
must not be advertised as a new optional-machine selection theorem.

## 7. Scope and remaining meaningful directions

The obstruction applies to arbitrary recipient-polymatroid value
oracles and exact selected-support feasibility. It does not establish
hardness for ordinary explicit machine-job eligibility, explicit
network or laminar ranks, or other representations that may expose
additional structure. It also does not rule out relaxing the number
of active machines, allowing jobs outside the selected set, dropping
some jobs, or parameterizing by a different structural measure.

The existing large-job-slot corank results keep all physical machines
available and select placements of particular job units. They do not
make the active-machine commitment in Section 1 and are not contradicted
by this construction. Likewise, the weighted prefix-free theorem for
nonnegative packing remains valid; the failure here is the proposed
model reduction, not its counting argument.

No publication-priority claim is made for this hidden-subset
construction. The purpose is to close a proposed general extension
with an explicit oracle proof and to preserve the distinction between
fixed-machine rounding and active-machine-basis selection.
