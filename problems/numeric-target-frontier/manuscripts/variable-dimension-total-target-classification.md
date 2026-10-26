# A tight total-target classification for arbitrarily many mixed rows

**25 October 2026. Complete theorem and proof; two independent
internal full reviews passed.** The number of numeric constraints is part of the
input. This increment removes the fixed-dimension restriction from
polynomial workspace and gives a matching total-target time exponent.

## 1. Main result

Let F be one normalized monotone integral submodular rank on an
explicit ground E. Integer resource vectors lie in P(F) or B(F).
Rank values, coordinate capacities and all counts are encoded in
binary. Original eligibility restrictions are allowed.

There are d explicitly listed linear target rows

```math
a^j x\ \rho_j\ T_j,\qquad j=1,\ldots,d,
       \quad \rho_j\in\{\le,=,\ge\},
       \quad a^j_e,T_j\in\mathbb Z_{\ge0}.
 \tag{VT1}
```

Rows may overlap arbitrarily, and d is unrestricted. Set
T=sum_j T_j. Given an arbitrary rational scalar objective c,
one can detect infeasibility and compute its exact minimum or
maximum over the integer feasible family in

```math
\boxed{
  2^{O((T+1)\log(T+2))}\mathrm{poly}(H)
 }
 \tag{VT2}
```

time and polynomial binary workspace, uniformly in d.
Here H is the complete binary encoding, with polynomially
implemented rank, SFM and weighted polymatroid-intersection
operations charged. No input of numeric length T or resource
rank R is materialized.

The order T log T is necessary in the rank-oracle model:
for infinitely many T, exact feasibility already requires

```math
2^{\Omega(T\log T)}
 \tag{VT3}
```

rank queries. This lower bound holds for bounded-error randomized
decision with success at least 2/3, and already for ordinary
matroids, 0/1 row coefficients, and every nonzero target equal
to one. It holds separately for pure covering rows over
independent sets or bases, and pure upper-budget rows over
bases. Exact scalar maximization over independent sets with
pure upper rows has the same lower bound.

As elsewhere, an additional upper or lower bound on the same
scalar c can be decided by its appropriate exact extremum.
The statement does not simultaneously impose a different
unbounded scalar row while optimizing c.

## 2. Base representation, masks and effective row count

For optional P(F), represent every vector as a full base using
a free disposal coordinate 0 of zero coefficient in every
row and zero scalar cost. If R=F(E), its rank is F(S) when
0 is absent and R when 0 is present. An optional x extends
by x_0=R-x(E), and projecting such bases gives precisely
P(F). The rank is normalized, monotone, integral and
submodular. This operation preserves all target rows and c.

An original mandatory base receives no free disposal.
Every later mask retains the same required total R.

Delete all covering rows with target zero. For every upper
or equality row, forbid coordinates whose coefficient
exceeds its target; this is necessary for any feasible
integer point. In particular, at target zero, all positive
coefficients in that row are forbidden. After that mask,
remove this now identically zero row. A mandatory rank loss
below R certifies infeasibility. These statements also hold
in the legitimate optional-to-base representation.

All surviving rows have positive integer targets. Their
number d' satisfies

```math
d'\le T.
 \tag{VT4}
```

If none survives, optimize c on the original-total masked
base in polynomial time. This includes T=0 without a
singular logarithm or an empty covering interval.

Let C be the surviving covering rows, and put s=|C|.
For an upper or equality row the auxiliary upper cap is
U_j=T_j; for a covering row it is U_j=2T_j-1. Thus

```math
U=\sum_jU_j\le2T,\qquad s\le T.
 \tag{VT5}
```

## 3. Common-order stopping prefixes need only chain copies

Enumerate the s! permutations pi of the covering rows.
For one permutation define the decreasing chain of subsets

```math
S_0=C,\qquad
 S_i=C\setminus\{\pi(1),\ldots,\pi(i)\},
                      \quad i=1,\ldots,s.
 \tag{VT6}
```

For each eligible original coordinate e, create s+1 copies
(e,i), one per S_i. Their shared resource rank is
F_0(image(Y)), where F_0 is the masked original rank and
image forgets the chain index. All copies keep scalar cost
c_e. This rank is an integral polymatroid rank, and
aggregation x_e=sum_i z_(e,i) gives an exact equivalence
of independent regions and of full bases. Complete inverse
images prove one direction; the inequality
z(Y)<=x(image(Y)) proves the other. Full totals and scalar
values agree.

Upper and equality rows retain their original coefficients
on every copy. In a covering row j, the copy receives
auxiliary coefficient min(a^j_e,T_j) if j belongs to S_i,
and coefficient zero otherwise.

### Why enumerating chains is complete

Take any original feasible integer base. Conceptually order
all of its R units in one common order. This is an existence
argument; the algorithm does not construct the unit list.
For each covering row, cap its values at T_j and stop at
the first unit where its prefix sum reaches T_j. Such a
stopping position exists. Its auxiliary sum W_j satisfies

```math
T_j\le W_j\le2T_j-1.
 \tag{VT7}
```

Zero-valued units within a prefix cause no difficulty.
Sort the covering rows by stopping position, breaking ties
arbitrarily, and choose that enumerated permutation.
At any unit, the rows that still count it form one of
the chain subsets S_i. Rows stopping at that unit all
count the unit; their deletions occur immediately after
it. Intermediate chain layers among tied stops have
zero units. Assign each unit the corresponding chain
copy of its original coordinate.

This constructs a lifted integer base retaining every
original resource unit and scalar cost, with all covering
auxiliary totals in VT7. Upper and equality totals are
unchanged. Conversely, any lifted base whose upper,
equality and covering auxiliary totals meet the stated
ranges projects to a legal original integer base.
Original covering values dominate credited values.

Thus the union over s! chains represents all original
feasible integer vectors with their exact scalar values.
Each individual chain uses only (s+1)|E| coordinates.
This replaces a simultaneous 2^s-subset lift by streamed
chain choices, which is essential for uniform polynomial
workspace.

## 4. Exact vector profiles and integral scalar optimization

For a fixed chain, group coordinates by their complete
auxiliary vector b in Z^{d'}_{\ge0}. Enumerate nonnegative
integer counts h_b for the occupied nonzero vectors, with

```math
m=\sum_{b\ne0}h_b\le R,\qquad
       W_j=\sum_{b\ne0}b_j h_b\le U_j
                          \quad\hbox{for every }j.
 \tag{VT8}
```

Set the one global zero-vector count to h_0=R-m.
At a completed profile, require W_j<=T_j for an upper
row, W_j=T_j for an equality row, and
T_j<=W_j<=2T_j-1 for a covering row.

The prescribed group capacities h_b, including h_0,
sum to R. Intersect the shared resource polymatroid
with this integral partition-count polymatroid and
require total R. Two-polymatroid intersection is
integral, and its nonempty total-R face is integral.
Every group capacity is tight on that face because
their sum is R. Hence the complete vector profile
is enforced exactly.

Minimize or maximize c on that face by weighted
polymatroid intersection. Its integral optimum
projects to an actual legal original vector.
Taking the best over all profiles and chains is
exact by Section 3. No additional scalar halfspace
is presumed to preserve integrality.

## 5. A token-partition bound independent of dimension

The following counting lemma controls every component-capped
profile, including profiles that subsequently fail a row
filter or resource test.

For each j, imagine U_j distinct tokens of color j,
and one additional distinguished marker. There are U+1
tokens in all. Given a multiset of nonzero vectors b
with component totals bounded by U_j, order the vectors
canonically, retaining their multiplicities. For each
vector allocate the next b_j unused tokens of color j
to its block, for every j. Each such block is nonempty.
Put all unused tokens in the block containing the marker.

This maps profiles injectively into set partitions of
the U+1 tokens. Indeed, from any image partition,
discard its marker block and read the color-count
vectors of all remaining blocks. Their multiset is
exactly the original vector profile. Thus distinct
profiles cannot have the same image.

Writing Bell for the number of set partitions gives

```math
\#\{\text{profiles satisfying VT8}\}
                 \le \mathrm{Bell}(U+1)
                 \le (U+1)^{U+1}.
 \tag{VT9}
```

The last inequality follows by encoding a set partition
by the function sending each token to the least-labeled
token in its block. The tokens, their partitions, and
the canonical map are only counting devices. None is
constructed by the algorithm.

## 6. All-input time and uniform polynomial workspace

The algorithm stores only coefficient vectors present
among the current chain's explicit coordinates. When
the next vector is b, its count is bounded during
generation by

```math
\min\left\{R-m,\
       \min_{j:b_j>0}
         \left\lfloor\frac{U_j-W_j}{b_j}\right\rfloor
       \right\}.
 \tag{VT10}
```

This componentwise pruning is necessary for applying
VT9 to the entire traversal. A bound only on the total
l1 weight followed by component tests at the end would
not establish the same dimension-free count.

Every visited partial profile has a zero completion
within all component caps and the resource count cap.
Distinct prefixes at the same depth give distinct
complete profiles. The total number of generated
nodes is therefore at most a polynomial factor more
than the count in VT9. All failed profiles and
infeasible input instances are charged.

The resulting explicit bound is

```math
s!\,(U+1)^{U+1}\mathrm{poly}(H)
        \le
          2^{O((T+1)\log(T+2))}\mathrm{poly}(H).
 \tag{VT11}
```

For one permutation the ground has at most
(d+1)(|E|+1) coordinates, each with at most d
integer coefficient entries. Its encoding is polynomial
in H. The permutation, current profile, component
totals and count registers all have polynomial binary
length. The depth is at most the number of occupied
vectors, not U. Resource optimizations and chains
are processed one at a time. These facts prove
polynomial workspace uniformly in d and the binary
resource rank.

For fixed d, the sharper multivariate partition bound
from the companion mixed-target theorem can replace
VT9. In particular, with
K(U)=max_nonempty_S (product_(j in S) U_j)^(1/(|S|+1)),
the same chain implementation gives
s! exp(O_d(K(U))) poly(H). The total-target-only
fixed-dimensional exponent is d/(d+1).

## 7. A matching oracle lower bound with unit targets

Let d>=4 be even. The ground E consists of the
n=binomial(d,2) unordered pairs of vertices of the
complete graph on d labeled vertices. Give each pair
e its 0/1 endpoint-incidence vector a_e in {0,1}^d.
Set r=d/2, and put T_j=1 for every row, so T=d.

Let H be the family of all perfect matchings of this
complete graph, regarded only as r-element subsets
of E. There are

```math
N=(d-1)!!
                      =2^{\Theta(d\log d)}
 \tag{VT12}
```

such sets. The recurrence follows by choosing the
partner of one vertex and recursing. For an elementary
lower estimate, along multiples of four at least d/4
factors in the product (d-1)(d-3)...1 are at least d/2.
Thus N>=(d/2)^{d/4}; the bound N<=d^{d/2} is immediate.

No two distinct members of H differ by a single
element exchange, because their vector sums are both
the all-ones vector and all element labels are distinct.

Define the reference rank-r matroid M_0 by making
all subsets smaller than r independent and all
r-subsets outside H bases. For A in H, the hidden
matroid M_A additionally makes A a basis. These
are matroids: for an independent (r-1)-set and a
larger independent r-set, either the sole available
augmentation is that larger set or there are at
least two one-exchange-neighbor candidates; at most
one can be forbidden. All other augmentation
cases are immediate.

Their rank oracles differ only at the set A.
Every larger set contains two adjacent r-subsets,
at least one of which is a visible reference base.
All smaller sets are independent. An r-set loses
one rank precisely when it is a forbidden member
of H. The condition d>=4 ensures a nonempty
reference base family.

With equality targets a^j x=1, the reference has
no feasible basis and the hidden matroid has
exactly its hidden A as a feasible basis. All
scalar costs can be zero.

This also establishes the following stronger
orientations.

- With pure covering rows a^j x>=1 and either
  independent sets or bases, a feasible set has
  at most r elements and therefore total incidence
  at most 2r=d. All d covering constraints force
  total incidence at least d. Equality holds,
  every vertex has incidence one, and the set is
  a full perfect matching. Only hidden A is feasible.
- With pure upper rows a^j x<=1 on bases, every
  base has total incidence 2r=d. All upper bounds
  must be tight, so again only hidden A is feasible.
- With pure upper rows on independent sets,
  maximize the scalar cardinality c_e=1. The hidden
  optimum is r. The reference optimum is r-1:
  no full perfect matching is independent there,
  whereas an (r-1)-edge partial matching is
  independent. Thus exact optimization distinguishes
  the same oracle family even with a feasible
  reference instance.

On the reference transcript, Q rank queries hit
at most Q hidden candidates. Under the distribution
placing half its probability on the reference and
half uniformly on hidden instances, any randomized
algorithm with worst-case Q queries has average
decision success at most 1/2+Q/(2N). Success at
least 2/3 on every instance requires Q>=N/3.
This proves VT3. For exact optimization in the
last orientation, inspect the returned cardinality
to make the same decision.

The explicit coefficient matrix has O(d^3) bits
and every target is one. All non-oracle input
data are therefore polynomial in T. A factor
polynomial in H cannot absorb the query lower
bound. The graph supplies labels for an oracle
matroid construction; the resource family is
not the ordinary graph-matching feasible family.

## 8. Consequences and limits of the classification

The theorem gives exact algorithms for arbitrarily
many overlapping integer resource budgets, covering
requirements and equality targets under one global
integral polymatroid, while optimizing one arbitrary
rational scalar cost. It includes binary-large
capacities and maintains every original mandatory
resource unit.

The upper/lower comparison is tight in total-target
exponent order in the general oracle model. It does
not imply a lower bound for an explicitly represented
graphic, linear or laminar matroid. Those classes
may admit faster methods.

Nonnegative integer row coefficients are essential
to the bounded token count. Signed cancellations
are outside the theorem. An unrelated second
resource rank would turn the exact-profile
subproblem into an intersection of three ranks,
for which the integral recovery proof does not
apply.

The result does not change an approximation
accuracy exponent: T is the original integer
target sum, not 1/epsilon. The fixed-dimensional
and anisotropic formulas remain the sharper
choice in their regimes.

Count-vector intersection has established public
antecedents, explicitly described in Eisenbrand,
Rohwedder and Wegrzycki,
*Sensitivity, Proximity and FPT Algorithms for
Exact Matroid Problems*, arXiv:2404.03747v2:
<https://arxiv.org/html/2404.03747v2>.
The present proof supplies the total-target
counting, mixed-cover chain representation,
uniform polynomial-space implementation and
matching target-exponent construction.
No publication-priority claim is made.
