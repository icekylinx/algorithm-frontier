# Why arbitrary many exact assignment budgets cannot be added for free

**25 October 2026. Explicit reduction and elementary relaxation gap;
root and independent review requested.**

The single exact assignment-budget restriction in the allocation
theorems is substantive. With an input-size collection of independent
hard assignment budgets, one compulsory player and unit-valued
rank-one resource types already express Maximum Independent Set.
There is also an unbounded integrality gap for the natural fractional
count relaxation, even on this one-player subclass.

This note concerns integer resource allocation. It does not contradict
the selected splittable-flow theorems, which may retain many routing-only
budget rows because their returned routing is continuous and unrounded.

## 1. The proposed larger model

For each type j and player p, let x_pj be the integer allocated count,
subject to the original integral recipient-polymatroid constraints.
Replace one nonnegative assignment-cost row by d independently supplied
rows

\[
                  \sum_{p,j}c^{(\ell)}_{pj}x_{pj}
                         \le C_\ell
                   \qquad(1\le\ell\le d),
 \tag{B1}
\]

where all costs and right sides are nonnegative and all d rows must hold
exactly. The number d is part of the input. No budget augmentation or
violation is allowed.

The selected players still form a genuine basis of the original player
matroid. The obstruction below has exactly one player p, with M=U_(1,1),
so its rank and ground size are one and its corank is zero. There is no
combinatorial choice of player, recipient eligibility ambiguity, hidden
value oracle, or binary expansion in the construction.

## 2. An exact encoding of every graph independent set

Let G=(V,E) be any finite simple graph with n>=1 vertices. For each vertex
v create a resource type j_v of intrinsic value one and recipient rank

\[
                     f_{j_v}(\varnothing)=0,
                         \qquad f_{j_v}(\{p\})=1.
 \tag{B2}
\]

Each resource is just one explicit unit that may be allocated to the
sole player or left unused. Its integer variable is x_v in {0,1}.
For each edge e={u,v} create a separate assignment budget with right
side one, coefficient one on its two endpoint types, and coefficient
zero on every other type. Its row is

\[
                                x_u+x_v\le1.
 \tag{B3}
\]

All numerical data are zero or one. There are n types and d=|E| rows;
the explicit dense or sparse encoding is polynomial in the graph size.

Given an integer allocation, let S={v:x_v=1}. Rows B3 hold exactly when
no graph edge has both endpoints in S, which is exactly the definition
of an independent set. Conversely every independent set gives a legal
allocation. The sole player's utility is

\[
                             \sum_{v\in V}x_v=|S|.
 \tag{B4}
\]

Therefore the optimum allocation utility equals alpha(G), and the
reduction preserves every multiplicative approximation ratio exactly.
It is an equality of feasible solutions and objective values, not just
a decision implication. Zero allocation is always feasible.

## 3. The precise complexity consequence and its primary source

Zuckerman's primary paper
[*Linear Degree Extractors and the Inapproximability of Max Clique and
Chromatic Number*, Theory of Computing 3 (2007), Theorem 1.1](https://theoryofcomputing.org/articles/v003a006/v003a006.pdf)
proves NP-hardness of approximating Maximum Clique within n^(1-epsilon)
for every fixed epsilon>0. Graph complementation preserves n and changes
a clique into an independent set of the same cardinality. The same
inapproximability therefore applies to Maximum Independent Set and,
through B2--B4, to this allocation subclass.

Consequently, unless P=NP, no deterministic polynomial-time algorithm for this
many-budget allocation model attains an n^(1-epsilon) approximation
for any fixed epsilon>0, where n here is the number of resource types.
In particular there is no fixed constant-factor deterministic polynomial-time
approximation. To infer the latter from the cited growing-factor
hardness, handle the finitely many small n below the constant threshold
by exact enumeration; a constant-factor algorithm on the remaining
instances would be stronger than the prohibited n^(1-epsilon) ratio.

This also rules out a deterministic fixed-constant approximation in time
`F(q) poly(H)`, `F(r) poly(H)` or `F(c) poly(H)` with a fixed polynomial
degree, because the reduction has q=r=1 and c=0. The same obstruction
applies to any claimed whole-player bound `A^q poly(H)` for a fixed A.
At one player such a bound is polynomial in the original graph encoding.

The reduction alone proves exact computational equivalence with
Independent Set on this subclass. Its quantitative inapproximability
uses the explicitly cited theorem and the stated P!=NP assumption.
It is not an unconditional oracle-query lower bound. It makes no
subexponential-time claim in the number of graph vertices or budgets.

## 4. An unconditional large fractional gap at one player

For the complete graph G=K_n with n>=3, the natural fractional count
relaxation is

\[
            0\le x_v\le1,
              \qquad x_u+x_v\le1\quad(u\ne v).
 \tag{B5}
\]

The vector x_v=1/2 for every v is feasible and has utility n/2. Summing
all pair constraints yields

\[
                     (n-1)\sum_v x_v
                            \le\frac{n(n-1)}2,
 \tag{B6}
\]

so the fractional optimum is exactly n/2. The integer optimum is one,
since an independent set in a complete graph has at most one vertex.
Thus this count relaxation has integrality gap n/2, while the largest
individual unit value remains one.

For every fixed epsilon in (0,1), an asserted simultaneous-budget
rounding guarantee

\[
                     \text{integer value}
                           \ge(1-\epsilon)\mathrm{FOPT}-1
 \tag{B7}
\]

is false for sufficiently large n, regardless of running time. The
right side exceeds the integer optimum once n>4/(1-epsilon).
There is only one genuine selected basis, so this gap is unrelated to
fractional mixtures of player-selection bases.

This example pinpoints an obstruction to replacing the one-cost
rounding objective by an assertion that all assignment budget rows can
be preserved simultaneously at the same largest-unit additive loss.
The fractional budgeted region remains downward and separable by an LP;
the failure is in integer recovery with all rows exact.

## 5. Even an integer-comparator additive extension would be too strong

Suppose, for example, that a deterministic polynomial algorithm in this larger model
guaranteed value at least OPT/2-1, with OPT the integer optimum. This
does not contradict the fractional example directly, but it would
still imply a constant-factor approximation for Independent Set.

Run it and also enumerate every independent set of size at most four.
Return the larger resulting value. If OPT<4, the enumeration is exact.
If OPT>=4, the additive algorithm gives at least OPT/4. Enumeration
requires only polynomial time because its size bound is constant.
The combined algorithm would be a four-approximation, contradicting
Section 3 unless P=NP.

More generally a fixed fractional multiplicative retention and fixed
additive loss, independent of the input graph, can be converted into
a constant-factor approximation by bounded-size enumeration. Thus
switching the comparator from fractional to integer does not justify
an unrestricted many-budget additive theorem at q=1.

## 6. Boundaries and public context

The number of independent assignment budgets in this reduction grows
with the input. It does not prove that two fixed budgets forbid every
constant approximation, nor that a fixed number of budgets cannot be
handled by algorithms with additional parameter or accuracy dependence.
It also does not exclude algorithms allowing explicit budget violation,
or algorithms whose exponential parameter counts the resource types,
budget dimensions or an additional appropriate structure.

The 2026 primary paper
[*On the PTAS Complexity of Multidimensional Knapsack*](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/LIPIcs.ITCS.2026.50/LIPIcs.ITCS.2026.50.pdf)
by Doron-Arad, Kulik and Manurangsi separately discusses the known
Independent-Set obstruction when the number of dimensions is input-sized,
and distinguishes it from fixed-dimension approximation questions. The
present elementary specialization is recorded as a boundary for this
project's allocation theorems, not as a new knapsack hardness discovery.

The positive single-budget theorems and the continuous multi-budget flow
theorems retain exactly their stated scopes. The simple graph encoding
explains why those two scopes cannot be combined into an integer
allocation theorem merely by adding more rows to the fractional LP.
