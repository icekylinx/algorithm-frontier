# Independent audit of the two-scenario unit-budget corank obstruction

**25 October 2026. Full independent read of
`two_scenario_unit_budget_corank_obstruction.md`, TS1–TS5 and all
four sections. Result: the reduction and stated complexity
consequence pass; no substantive correction requested.**

This review also directly checks the cited primary source. It is
separate from the audits of the many-scenario Hitting Set reduction
and the rank-oracle indistinguishability construction.

## 1. The primary hardness premise is the one actually used

Abboud, Lewi and Williams, *Losing Weight by Gaining Edges*,
[author-hosted primary paper](https://people.csail.mit.edu/rrw/ksum.pdf),
Definition 1.1 defines exact-cardinality k-SUM on nonnegative integers
bounded by n^(2k), with a nonnegative target. Theorem 1.3 states
W[1]-completeness for that definition. Both statements were read
directly in the paper.

Only this bounded-integer W[1]-hardness is needed. The reduction does
not appeal to a randomized compression of arbitrary integer ranges,
nor to membership of unrestricted k-SUM in W[1]. Thus the source
supports the deterministic FPT consequence as stated.

The construction remains polynomial in the full binary source
encoding. Even though the numerical range depends on k, those
integers are supplied in binary and no pseudo-polynomial enumeration
is performed.

## 2. Preprocessing, parameters, and nonnegative budgets

For a source list of length q, the degenerate cases are decided
directly: k=0 requires target zero, k=q requires the sum of the whole
list, and k>q is impossible. A target greater than the sum A of the
nonnegative input numbers is impossible. This leaves

    1<=k<q,       0<=T<=A.

Set r=q-k and L=A+1. Then r>=1, and the selected original player
matroid M=U_(r,q) has corank exactly

    q-r=k.

The resource in either scenario is the free Boolean recipient
matroid with rank f(S)=|S|. Thus its integer independent vectors are
exactly the coordinatewise zero-one count vectors. Unused resource
units are explicitly permitted; this is not a mandatory-base
allocation model.

Scenario 1 has coordinate cost a_i and budget C_1=A-T>=0. Scenario 2
has coordinate cost L-a_i and budget C_2=rL-A+T. Every second cost
is positive because a_i<=A<L. Also

    C_2>=L-A+T=1+T>0.

All setup fees are zero. Every M-basis with zero allocated counts is
therefore a legal robust solution, independently of the source
answer. This prevents a hidden feasibility promise from carrying
the hardness. The ranks, costs and budgets have explicit polynomial
representations; no information is hidden inside a rank oracle.

## 3. Independent derivation of the equivalence

Fix any common selected basis B, and put D=P minus B. Then |D|=k.
Because each coordinate has capacity one and every unit has value
one, positive integer minimum service on B in either scenario forces
the allocation to give exactly one unit to every i in B.

Allocating additional units outside B cannot help the objective and,
by nonnegative costs, cannot improve budget feasibility. Such units
may be removed. Hence the required scenario-1 cost is exactly

    sum_(i in B) a_i=A-sum_(i in D) a_i.

It is at most A-T if and only if sum_D a_i>=T.

The required scenario-2 cost is exactly

    sum_(i in B)(L-a_i)
       =rL-A+sum_(i in D) a_i.

It is at most rL-A+T if and only if sum_D a_i<=T. Satisfying both
scenarios is therefore equivalent to the single equality

    sum_(i in D) a_i=T.

Conversely, any source k-set with this sum gives its complementary
basis B and one-unit allocations with equality in both budgets.
The two allocations are allowed to adapt separately, but at a
positive integer target their coordinates on B are forced, so
adaptivity does not weaken either inequality.

Each selected player can receive at most one unit in either
scenario, while r>=1 ensures the minimum is over a nonempty basis.
Consequently the robust integer optimum is exactly one on YES
instances and exactly zero on NO instances. This establishes both
directions of TS5 without an approximation or numerical gap.

## 4. Finite-factor consequence and its limits

An always legal deterministic finite-factor multiplicative algorithm
must return positive objective when OPT=1. Its objective is an
integer, so positive means at least one. When OPT=0, no legal
positive allocation exists. Running such an algorithm and checking
its output therefore decides the source problem.

Since the constructed corank is exactly k and the explicit encoding
grows polynomially, running time F(c) poly(H) would give an FPT
algorithm for the source. The same holds for F(c,s) poly(H), since
the number s of scenarios is always two. Under FPT!=W[1], no such
unrestricted finite-factor guarantee is possible.

The argument uses exact scenario budgets and a common optional
selected basis. It does not establish hardness for a supplied common
basis or for a fixed compulsory player set. It does not transfer to
relaxed budgets merely by retaining the same construction. It also
does not yield a particular exponential lower base in q: that is a
separate rank-oracle result with a different input interface.

The conclusion is compatible with additive high-quota guarantees.
Here the largest unit value and the positive optimum are both one,
so a one-unit additive loss permits objective zero. It is likewise
compatible with single-scenario exact-budget results, since the two
opposing inequalities are essential to enforce the omitted-set sum.

The main note states all of these model boundaries correctly. The
full reduction and its claimed deterministic corank-FPT obstruction
are accepted by this independent review.
