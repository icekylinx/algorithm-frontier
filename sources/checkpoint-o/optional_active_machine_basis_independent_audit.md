# Independent audit: optional active machine bases

**25 October 2026. Fresh full read of
`optional_active_machine_basis_oracle_obstruction.md`, Sections 1--7.**

The feasibility obstruction is correct in the stated arbitrary
recipient-rank oracle model. It does not depend on a makespan
approximation factor or on assignment costs. The distinction from the
project's placement-selection scheduling theorems is essential and
is maintained in the manuscript.

## 1. Rank validity and the hidden information

Write r=q-c with c>=2 and r>=2. The cardinality rank
`min(2|S|,2r)-1[|S|=r]` has successive increments
2,...,2,1,1,0,...,0, so it is normalized, monotone and submodular.
Adding one only at a chosen r-set A preserves monotonicity.

For submodularity, a newly increased right-hand term can only be
the union A or the intersection A. If the compared sets are not
nested, their old inequality has exactly one unit of slack in either
case. If they are nested, the same term occurs on both sides. Thus
the asserted hidden f_A is a valid integral rank. In particular,
all machines have singleton rank two; neither singleton eligibility
nor player-matroid loop preprocessing reveals the hidden basis.

## 2. Mandatory jobs force the exact active support

The one job type has total rank 2r. Any complete schedule supported
on an active r-set I must satisfy

    2r = x(P) = x(I) <= f_A(I).

The right side is 2r only for I=A, and 2r-1 for every other r-set.
Consequently any legal schedule, however unbalanced, chooses A.
The explicit vector 2*1_A is feasible on every subset: proper
subsets of size below r use the 2|S| bound, different r-sets
intersect A in at most r-1 positions, and larger subsets use the
total bound 2r. Its load is two everywhere on A. The average load
lower bound on r active machines proves optimum makespan exactly two.
Zero assignment costs satisfy budget zero without further assumptions.

## 3. The query and parameter lower bounds follow

Until queried at A, the value oracle answers exactly as the fixed
cardinality reference. With two candidate r-sets still unqueried,
the same deterministic transcript is consistent with two feasible
instances having different uniquely permissible active bases. No
single output can be valid for both. This yields the stated worst-
case lower bound binom(q,r)-1=binom(q,c)-1.

For every proposed fixed polynomial degree D, choose a fixed
c>D after accounting for the explicit encoding convention. As q
grows, q^c/c! exceeds F(c)*q^D*polylog(q). The rank values retain
O(log q) bits. Thus a uniform deterministic F(c)*poly(H) algorithm
cannot even find a feasible schedule on these promised-feasible
instances. The argument is an information bound and does not
invoke an unproved computational complexity assumption.

## 4. The attempted reduction has the wrong monotonicity

Availability on Q satisfies f_j(Q)=f_j(P), an upward condition in
Q. Treating active machines as coordinates of a downward lower-
service packing region would therefore change the output problem.
Taking deleted machines as coordinates repairs monotonicity but
turns the selector into the dual rank-c matroid, whose omission
corank is r. This does not give the ruled-out corank-c algorithm.

The fixed-machine cost-preserving rounding paragraph is also
consistent: the full-total prefix-intersection face is integral,
minimum assignment cost on that face is at most the supplied
fractional cost, and machine-specific decreasing processing-time
orders give the stated largest-unit upper error. That step assumes
the permitted support is already fixed and fractionally feasible;
it cannot solve the preceding hidden-support selection problem.

No substantive gap was found. This is independent internal
mathematical review. It does not establish a lower bound for ordinary
explicit eligibility lists, for the previously accepted large-job
placement parameterizations, or for randomized algorithms without
a separately stated distributional argument.
