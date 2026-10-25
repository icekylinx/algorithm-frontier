# Robust integer unit allocation has a corank-parameter obstruction

**25 October 2026. Complete explicit Hitting Set reduction; root and independent full reviews passed.**

This note identifies a boundary of the robust fractional-flow transfer.
With an input list of scenarios and one common selected player basis,
even positive integer unit service in every scenario is W[2]-hard in
corank. The hardness holds with one explicitly represented Boolean
recipient resource per scenario, identical unit values, zero assignment
costs, and a uniform player matroid. Scenario allocations may adapt after
the scenario is revealed.

The consequence is conditional on the standard assumption FPT != W[2].
It is not an information-theoretic rank-oracle lower bound or a lower
bound on a whole-q exponential base.

## 1. The robust allocation model

Let P be an explicit q-player ground and M a rank-r player matroid.
Choose one actual M-basis I before the scenario is known. For each
explicit scenario sigma, choose an integer allocation separately, subject
to that scenario's recipient resources and budget. The robust utility is

\[
 \min_{\sigma}\ \min_{p\in I}
                \text{utility of p in scenario sigma}.
\tag{H1}
\]

The same I is used in all scenarios; the allocations need not be the
same. Unused resource capacity is permitted. The parameter is c=q-r.
The zero allocation is always legal, so an instance with optimum zero
remains a feasible optimization instance.

## 2. Source problem and harmless preprocessing

An instance of Hitting Set consists of a finite universe U, an explicit
family of sets S_1,...,S_m, and a budget k. The question is whether some
D of size at most k intersects every S_i. Hitting Set parameterized by
k is W[2]-complete. A primary research source stating this standard
baseline is Bart M. P. Jansen,
[*On Structural Parameterizations of Hitting Set: Hitting Paths in Graphs Using 2-SAT*](https://arxiv.org/abs/1507.05890).
It is also explicitly recorded in Section 1.1 of Inamdar et al.,
[*Fixed-Parameter Algorithms for Fair Hitting Set Problems*, MFCS 2023](https://drops.dagstuhl.de/storage/00lipics/lipics-vol272-mfcs2023/LIPIcs.MFCS.2023.55/LIPIcs.MFCS.2023.55.pdf).

Empty sets are immediately negative instances, and an empty family is
immediately positive. Values k>|U| are also trivial after the empty-set
test. With a nonempty family of nonempty sets, k=0 is immediately
negative. Thus the nontrivial reduction may assume a nonempty family of
nonempty sets and 1<=k<=|U|. Add one fresh element outside every S_i and
call the resulting ground P. Then q=|P|>k, so r=q-k>=1. This changes no
hitting-set answer. A hitting set of size at most k can be padded to
exactly k using arbitrary unused ground elements.

## 3. One explicit matroid resource per scenario

Use the uniform player matroid

\[
                            M=U_{q-k,q}.
\tag{H2}
\]

For each set S=S_i create one scenario with one unit-valued resource
whose recipient rank is

\[
 f_S(A)=|A\setminus S|+
                 \min\{|A\cap S|,\ |S|-1\}
                         \qquad(A\subseteq P).
\tag{H3}
\]

This is the rank of the direct sum of the free matroid on P\S and
the uniform matroid U_(|S|-1,S). Therefore it is normalized, monotone,
integral, and submodular. When |S|=1, the one element of S is simply
a loop, which is valid. Every singleton rank is at most one.

The representation is explicit: store S and its cardinality. A rank
query uses intersections and cardinalities in polynomial time. Every
rank lies between zero and q-1, so its binary length is O(log q).
Set every assignment cost and every scenario budget to zero. Every
nonzero allocated unit has value one, identically across players and
scenarios. There are m scenarios, so the total instance size is
polynomial in the Hitting Set input size.

## 4. Positive integer service is exactly a hitting set

Let I be any M-basis, and let D=P\I. Then |D|=k. Since every scenario
resource has singleton caps at most one, positive integer utility at a
selected player means exactly one allocated unit there.

The vector 1_I is feasible in scenario S exactly when

\[
                 |I\cap S|\le|S|-1
       \quad\Longleftrightarrow\quad S\not\subseteq I
       \quad\Longleftrightarrow\quad D\cap S\ne\varnothing.
\tag{H4}
\]

If D intersects every set, use x^S=1_I in every scenario. It is legal
and gives robust value one. Conversely, any scenario allocation giving
positive integer utility to every member of I must contain 1_I; by
downward feasibility, that vector must itself obey the scenario rank.
Equation H4 therefore forces D to hit every source set.

Consequently

\[
 \mathrm{OPT}_{\mathrm{robust}}=
 \begin{cases}
 1,&\text{the Hitting Set instance is positive},\\
 0,&\text{the Hitting Set instance is negative}.
 \end{cases}
\tag{H5}
\]

Allowing adaptive scenario allocations does not help: target one forces
the same necessary unit vector on the common selected set in every
scenario. The allocation outside I may always be discarded.

## 5. Every finite multiplicative guarantee decides the source instance

Suppose a deterministic algorithm returned a legal robust integer
allocation with any finite multiplicative factor alpha, in time
F(c)*poly(H), where the polynomial degree is independent of c. On an
instance with optimum one it must return value at least 1/alpha>0.
The returned value is integral, so it must actually equal one.
On an instance with optimum zero no legal output can have positive
value. Checking the output therefore decides Hitting Set.

The reduction preserves c=q-r=k. It follows that, unless FPT=W[2],
there is no such corank-FPT algorithm with any finite multiplicative
integer guarantee for this robust model. The factor need not be a
fixed constant: any finite positive guarantee on the optimum-one
instances forces the same decision. The statement concerns algorithms
whose claimed running-time form is uniform in the input and corank.

This obstruction already holds in the simple explicit subclass above.
It does not rely on hidden rank queries, large numerical supplies,
assignment costs, or a complicated selection matroid. It concerns an
unbounded input number of explicit scenarios, not a fixed scenario count.

## 6. Why robust fractional service is different

Intersecting finitely many downward fractional service regions still
admits the usual scenario-by-scenario separation. That fact does not
solve the integer one-unit positivity gate. In a single scenario, the
one-unit gate is a two-matroid intersection; across many scenarios it
requires the same selected set to avoid all scenario circuits S_i.
Here that requirement is exactly Hitting Set on its complement.

The integrality issue is visible without any large numbers. If all
source sets have size at least two, then for every I the vector
(1/2)*1_I is feasible in every scenario H3: at most |S|/2 units are
assigned inside S, and |S|/2<=|S|-1. Thus fractional robust service can
remain positive when integer robust optimum is zero. For example,
take source sets {1,2}, {2,3}, {1,3}, budget k=1, and a fresh fourth
element. No one-element hitting set exists, so integer optimum is zero;
one-half fractional service on every selected three-set is feasible in
all three scenarios.

The robust fractional-flow theorem therefore remains consistent with
this obstruction. Its continuous positive rate is not rounded upward
to a mandatory integer unit in every scenario. A largest-unit additive
rounding statement may legitimately return zero in this example and
does not give a finite multiplicative integer guarantee.

## 7. Exact scope of the conclusion

The result rules out an unrestricted robust integer extension in
F(c)*poly(H) time under FPT!=W[2]. It leaves open positive results with
additional structure, a fixed or parameterized scenario count, additive
loss, or a relaxed first-stage selection requirement.

No 2^(q-o(q)) lower bound, no particular whole-q exponential base, and
no unconditional oracle-query lower bound is inferred from this
reduction. Enumerating rejected k-sets gives the expected XP approach
for this explicit subclass. Stronger whole-ground time claims would
need their own complexity assumption and reduction.
