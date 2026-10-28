# Two exact scenario budgets already obstruct corank-FPT unit selection

This is an explicit finite-input obstruction, separate from both the
many-scenario Hitting Set reduction and the rank-oracle lower bound.
With only two scenarios, free Boolean recipient resources, unit values
and no setup fees, selecting a common player basis with positive integer
service can encode k-SUM. Consequently an unrestricted finite-factor
corank-FPT theorem remains impossible under FPT!=W[1], even when the
number of scenarios is fixed at two and all recipient ranks are simple.

## 1. Source and preprocessing

Use k-SUM: nonnegative binary integers a_1,...,a_q and target T,
asking whether a subset D of exactly k indices has sum T. Its
parameter is k. Abboud, Lewi and Williams,
[Losing Weight by Gaining Edges](https://people.csail.mit.edu/rrw/ksum.pdf),
Definition 1.1 and Theorem 1.3, state W[1]-completeness for the
bounded-integer version already sufficient here. We only use its
W[1]-hardness; no randomized reduction from arbitrary integer ranges
or disputed membership statement for unbounded ranges is required.
Specifically, their Definition 1.1 permits both the entries and target
in <code class="math">[0,q^{2k}]</code>, and their Section 4 obtains hardness by a
deterministic reduction. This source range is already nonnegative,
so no sign conversion or random modulus is part of the present reduction.

Let A=sum_i a_i. The cases k=0, k>=q, and T>A can be decided directly
with their ordinary exact-cardinality conventions. Nontrivial source
instances may therefore be restricted to

    1<=k<q,   0<=T<=A.

Set r=q-k>=1 and L=A+1. All constructed data have polynomial binary
encoding in the source data.
Indeed, if the source entries and target have at most <code class="math">b</code> bits,
the sum <code class="math">A</code> and <code class="math">L</code> have at most
<code class="math">b+\lceil\log_2 q\rceil+1</code> bits, and all assignment costs and
budgets have <code class="math">O(b+\log q)</code> bits. Only two lists of
<code class="math">q</code> costs, two budgets and the uniform rank are required;
the construction never enumerates integer magnitudes or resource copies.

## 2. Two scenarios with modular unit costs

Use original player matroid M=U_(r,q). Each scenario has one resource
whose rank is the free Boolean matroid rank f(S)=|S|. Its counts are
therefore independently bounded by one at every player. Every unit
has value one. Unused units are allowed and all setup fees are zero.

Scenario 1 has assignment cost a_i at player i and budget

    C_1=A-T.                                                       (TS1)

Scenario 2 has assignment cost L-a_i at player i and budget

    C_2=rL-A+T.                                                    (TS2)

All costs are nonnegative: L>A>=a_i. Both budgets are nonnegative;
C_1>=0 and C_2>=L-A+T=1+T. Thus any original M-basis with zero
counts is a legal robust solution. There is no hidden zero-feasibility
problem and no negative-cost encoding.

Choose one common M-basis B. The two actual allocations may adapt
independently to their scenarios. Its complement D=P minus B has
exactly k elements.

## 3. Positive integer service is exactly the source equality

Because every player has resource cap one, positive integer service
on B requires exactly one unit at every member of B. It is feasible
in scenario 1 precisely when

    sum_(i in B)a_i<=A-T
          iff sum_(i in D)a_i>=T.                                (TS3)

In scenario 2 it is feasible precisely when

    sum_(i in B)(L-a_i)<=rL-A+T
          iff sum_(i in D)a_i<=T.                                (TS4)

Together, TS3--TS4 are equivalent to sum_(i in D)a_i=T. Conversely,
such a source subset gives B and one-unit allocations satisfying
both budgets with equality. Therefore the robust integer optimum is

    1 on positive k-SUM instances and 0 on negative instances.     (TS5)

Separate scenario allocations do not help at this target: their
positive-service coordinates are each forced to equal one on B.
The resource ranks, player matroid and all budgets are explicit,
polynomial-time evaluable data.

## 4. Parameter consequence and exact scope

The corank is c=q-r=k. Any deterministic algorithm that always
returns a legal robust integer allocation with a finite multiplicative
guarantee, in F(c) poly(H) time, would distinguish the two values in
TS5. A positive optimum demands strictly positive output, which is
integer and hence at least one. This would be an FPT algorithm for
the W[1]-hard source problem. Thus no such guarantee exists unless
FPT=W[1]. Parameterizing additionally by the scenario count does not
remove this example, since that count is always two.

This does not prove a whole-q exponential lower bound: an explicit
sum problem has different exponential algorithms from a general
rank-oracle intersection. It does not contradict the separate
unconditional near-2^q rank-oracle lower bound, the many-scenario
W[2] reduction, the high-quota additive guarantee, or the bounded
minimal-certificate positive results. In the present construction
the recipient matroids themselves are free; exact budget feasibility
can nevertheless create large minimal infeasible recipient sets.

Nor is this an impossibility result for two exact assignment costs
on a fixed compulsory set, for relaxed budgets, or for a supplied
common selected basis. The hard decision is the same optional
common basis under two scenario budgets. No publication-priority,
formal-verification or external-review claim is made.

---

**Attribution:** icekylinx and GPT-6 Astra Pro.
