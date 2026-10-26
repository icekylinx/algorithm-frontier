# A whole-ground oracle barrier for robust positive integer allocation

**25 October 2026. Root and independent full mathematical reviews completed; the public two-scenario implication remains separately attributed.**

Even with identical unit values, zero costs, zero setup fees, one
Boolean recipient matroid per scenario and a uniform original player
matroid, an unrestricted finite multiplicative robust guarantee
requires essentially 2^q value queries in the worst case. The
self-contained construction uses q explicit scenarios on q players.
It rules out every fixed exponential base below two in this oracle
model. It also rules out a uniform corank-FPT finite-factor guarantee
when the number of scenarios is part of the input.

The construction uses the standard sparse-paving mechanism, proved
directly below. No publication-priority claim is made. In particular,
the public near-brute-force lower bound for three-matroid intersection
already implies a no-fixed-base-below-two consequence with only two
scenarios; Section 8 separates that established implication from the
elementary q-scenario construction.

## 1. Model and theorem

Choose one actual basis I of an original player matroid M before
the scenario is known. In every scenario omega, integer independent
resource counts may be allocated adaptively. The robust utility is

$$
\min_\omega\min_{p\in I}x^\omega(p).
\tag{RO1}
$$

There will be one unit-valued recipient matroid resource per
scenario. Unused capacity is allowed; all costs, setup fees and
budgets are zero. Thus any actual player basis together with zero
allocations is always a legal output, even when the optimum is zero.

**Theorem RO.** For integers q and r with 2<=r<q, there is a family
of robust allocation instances with q players, M=U_(r,q), exactly
q explicitly listed scenarios and optimum one such that any
deterministic algorithm attaining any finite positive multiplicative
factor on every instance needs at least

$$
\frac1q\binom qr-1
\tag{RO2}
$$

rank-value queries in the worst case. More precisely the bound is
|H_h|-1 for an explicitly chosen class H_h with
|H_h|>=binom(q,r)/q. Only one scenario oracle depends on the hidden
instance. All non-oracle input data have polynomial size in q,
and all rank answers have O(log q) bits.

For r=floor(q/2) and q>=4, the bound is

$$
2^{q-O(\log q)}.
\tag{RO3}
$$

Therefore no deterministic algorithm with running time
(2-eta)^q*poly(H) for any fixed eta>0 can give a finite
multiplicative guarantee on this full robust oracle model. The
factor may depend on the instance provided it is always finite.
This is an unconditional oracle-query conclusion, not a
complexity assumption about explicitly represented matroids.

## 2. A direct rank proof for forbidden r-set families

Let H be a family of r-subsets of P, |P|=q>r, satisfying

$$
|A\cap B|\le r-2
                         \qquad(A,B\in H,\ A\ne B).
\tag{RO4}
$$

Define independent sets to be every set of size at most r-1,
together with the r-sets not in H. There are no larger independent
sets. This is a rank-r matroid, as can be checked without assuming
a sparse-paving theorem.

The empty-set and hereditary axioms are immediate. For augmentation,
let I,J be independent and |I|<|J|. If |I|<=r-2, any element of
J\\I can be added to I. The remaining case is |I|=r-1 and |J|=r.
If |J\\I|=1, adding its unique element produces J, which is
independent. Otherwise choose two distinct elements a,b in J\\I.
The two candidate r-sets I+a and I+b intersect in r-1 elements,
so RO4 permits at most one to belong to H. At least one augments
I independently.

The rank is actually r: start with any (r-1)-set and two distinct
outside elements, possible because q>r, and use the same argument.
Its rank function is exactly

$$
f_H(S)=\min\{|S|,r\}
                     -\mathbf1[|S|=r\text{ and }S\in H].
\tag{RO5}
$$

For |S|<r this follows from independence. A forbidden r-set has
rank r-1 because all its proper subsets are independent. An
allowed r-set has rank r. Finally, every set larger than r
contains an (r-1)-set and two outside elements, one of which
gives an independent r-subset. Thus RO5 holds in every case.
As a matroid rank it is normalized, monotone, integral and
submodular. Every singleton has rank one because r>=2.

Any subfamily of H also satisfies RO4. In particular, removing
one forbidden r-set leaves a valid rank-r matroid and changes
RO5 at exactly that one r-set.

## 3. Residue classes and a polynomial largest-class computation

Label P by the distinct residues 0,1,...,q-1. For each r-set S
define

$$
\chi(S)=\sum_{p\in S}p\pmod q,
                 \qquad H_t=\{S:|S|=r,\ \chi(S)=t\}.
\tag{RO6}
$$

Every H_t satisfies RO4. Indeed, if two distinct r-sets shared
r-1 elements, they would differ by exchanging distinct labels
a,b. Equal residues would imply a-b=0 modulo q, impossible for
distinct members of {0,...,q-1}.

The q residue classes partition all r-subsets. Choose a largest
class H_h, with a deterministic tie rule. Pigeonhole counting gives

$$
|H_h|\ge\binom qr/q.
\tag{RO7}
$$

Choosing h does not require enumerating the r-subsets. Define
D(i,k,t) as the number of k-subsets of {0,...,i-1} with residue t.
Initialize D(0,0,0)=1 and all other entries zero. For i=0,...,q-1
use

$$
D(i+1,k,t)=D(i,k,t)+D(i,k-1,t-i\bmod q),
\tag{RO8}
$$

where out-of-range k terms are zero and k need not exceed r.
The values D(q,r,t) are precisely the class sizes. There are
O(q^2*r) arithmetic operations, and each counter is at most
2^q and has O(q) bits. Retaining two i-layers uses polynomial
space. Thus h and |H_h| are computable in polynomial bit time,
without listing the members of H_h.

Membership of a proposed set S in H_t only requires its cardinality
and its label sum modulo q. This also gives an explicit polynomial
rank algorithm for each f_(H_t).

## 4. The q scenarios and the unique positive common basis

The original player matroid is M=U_(r,q). For every residue t!=h,
make one scenario whose single recipient matroid has rank f_(H_t).
There are q-1 such known scenarios.

Choose a hidden A in H_h. The final scenario has recipient rank

$$
f_A=f_{H_h\setminus\{A\}}.
\tag{RO9}
$$

It is valid by Section 2. All scenarios give value one for one
allocated unit, and have zero costs and budgets. Their resource
counts are independent vectors, so unused units are permitted.

For any actual player basis I, |I|=r. Singleton caps are one.
Consequently positive integer utility at every member of I
requires exactly one unit there. Such service in a scenario is
possible if and only if I is independent in that recipient
matroid: the necessary vector 1_I must be independent, and if
it is, that vector is a sufficient allocation.

If chi(I)!=h, the known scenario for residue chi(I) declares I
a forbidden r-set, so positive robust utility is impossible.
If chi(I)=h but I!=A, the hidden scenario forbids I. The only
remaining possibility is I=A. That set is allowed by every
known scenario and was removed from the hidden forbidden family,
so assigning 1_A in every scenario is legal.

We have proved

$$
\mathrm{OPT}=1,\qquad
 I\text{ has positive robust integer service}\iff I=A.
\tag{RO10}
$$

The scenarios may allocate independently; the conclusion uses
only the same selected I and each scenario's necessary unit
vector. Adaptivity does not permit changing the selected basis.

## 5. The oracle transcript and the minus-one bound

Use the baseline hidden oracle f_0=f_(H_h), in which no member
of H_h is relaxed. This is also a valid matroid. For every
possible hidden A,

$$
f_A(S)=f_0(S)+\mathbf1[S=A].
\tag{RO11}
$$

All other scenario oracles are independent of A. Until the
algorithm queries the hidden scenario on its particular hidden
set A, its entire transcript agrees with the baseline transcript.
Queries at non-r-sets, at other residue classes, or to known
scenarios reveal no information about A.

A finite multiplicative guarantee on OPT=1 requires output
value at least 1/alpha>0. The output is integral and at most
one, so it must have value one. By RO10, its actual selected
basis must be A.

If at least two sets of H_h remain unqueried in the hidden
scenario, choose either of them as A. Both choices give the
same transcript, but a deterministic output basis can equal at
most one of them. Hence no correct algorithm may terminate on
that transcript while two candidates remain. The worst case
requires at least |H_h|-1 queries.

The subtraction of one is deliberate: after ruling out all but
one candidate on a promised-positive instance, an algorithm may
output that last candidate without querying it. No stronger
query count is silently inferred. This proves RO2 even when the
algorithm is promised that the robust optimum equals one.

## 6. Encoding, asymptotics and corank

The explicitly listed scenario set has size q. Known scenario
descriptions contain their residue, the shared ground labels and
rank r; zero cost arrays and unit values have polynomial total
encoding. Every rank answer is at most r and has O(log q) bits.
The final scenario is accessed only through its rank-value oracle.
The private A used to implement that oracle is not supplied as
inspectable input, program source or an explicit circuit list.
Giving away that representation would invalidate this oracle
lower bound, just as in other hidden-set constructions.

For r=floor(q/2), the central binomial coefficient is at least
2^q/(q+1), because it is a largest term among the q+1 terms
whose sum is 2^q. Therefore the query bound is at least

$$
\frac{2^q}{q(q+1)}-1.
\tag{RO12}
$$

A fixed base 2-eta times any polynomial in the known input is
eventually smaller than RO12. Polynomial cost for evaluating a
rank query cannot remove this contradiction.

The general formula also gives a corank statement. Fix c=q-r
and let q grow. Then |H_h|>=binom(q,c)/q grows as
Omega(q^(c-1)) for fixed c. If a deterministic algorithm had
time F(c)*poly(H) with polynomial degree independent of c, the
known input size is a fixed polynomial in q. Choosing a fixed c
larger than that resulting polynomial degree plus one contradicts
RO2 as q grows. Thus unrestricted finite-factor robust allocation
is not corank-FPT in this oracle model. The analogous conclusion
holds for a rank-only F(r)*poly(H) bound by fixing r instead.

This is different from the companion explicit Hitting Set
reduction: that reduction gives conditional parameterized
hardness for explicit simple ranks; the present statement is an
unconditional information bound with a hidden rank oracle.

## 7. Compatibility with the positive robust theorems

Every nonzero unit is heavy at any threshold in (0,1]. Hence all
scenarios have the same all-heavy role pattern. A parameter
counting light/heavy disagreements is zero on this construction.
The obstacle is the common integer basis, not the description of
scenario roles.

For a fixed proposed basis, integer unit feasibility in every
scenario can be checked by one rank query per scenario. Full
enumeration of the player bases therefore gives a 2^q*poly(q)
upper bound for the zero/one subclass. The lower bound identifies
the exponential-base obstruction rather than a difficulty in
writing or checking one candidate allocation.

The positive guarantee in
[robust-unit-allocation-additive-and-promised-two.md](robust-unit-allocation-additive-and-promised-two.md) may return
zero when K*=1. Likewise
[robust unrelated allocation proof](../../problems/robust-unrelated-allocation/proof.md) loses the largest unit,
which is one here. Those guarantees do not have to identify A
and remain consistent with the lower bound. An externally supplied
one-unit robust witness would itself reveal the missing selected
basis on these instances; that certificate is not free information
provided by a fractional projection.

This construction does not establish the same bound for an
ordinary explicit eligibility-list model, for a compulsory fixed
player basis, or for continuous splittable flow. It also does
not by itself give a constant-scenario construction; that
separate implication follows from the public theorem below.

## 8. Existing primary theorem already gives a two-scenario boundary

Doron-Arad, Kulik and Shachnai,
[*You (Almost) Can't Beat Brute Force for 3-Matroid Intersection*,
arXiv:2412.02217v2](https://arxiv.org/html/2412.02217v2),
Theorem 1.1, exclude fewer than
2^(q-5*sqrt(q)*log(q)) membership queries for three-matroid common
basis, for infinitely many square q. Their result permits
randomization, and in particular applies to deterministic
algorithms.

For equal positive rank, take the first matroid as the original
player matroid and the other two as unit-recipient scenarios.
Robust integer optimum is one exactly when the three matroids
have a common basis, and zero otherwise. Unequal ranks or rank
zero are elementary preprocessing cases. A rank query can be
simulated by greedy using at most q independence queries, so
polynomial oracle overhead preserves the prohibition of every
fixed exponential base below two. Thus that prohibition already
holds for two scenarios. This is an attributed consequence of
their theorem, not a new three-matroid-intersection lower bound.

The self-contained q-scenario proof above has a sharper
polynomial-factor loss and a uniform original player matroid;
it uses more scenarios. These distinctions should be retained
when comparing the two statements. The residue-class and
sparse-paving ingredients, and hidden-oracle lower bounds more
broadly, are not claimed as novel techniques.
