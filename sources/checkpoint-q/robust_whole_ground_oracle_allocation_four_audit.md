# Independent audit of the robust whole-ground oracle barrier

**25 October 2026. Reviewer: allocation_four. Full fresh read of
robust_unit_allocation_whole_ground_oracle_barrier.md, RO1--RO12 and
all eight sections, with a fresh read of the cited primary theorem.**

## Verdict

The self-contained deterministic q-scenario construction passes.
For a uniform rank-r original player matroid it forces the unique
positive robust integer basis to be a hidden member of a residue
class of size at least binom(q,r)/q. The lower bound
|H_h|-1 rank queries, and its balanced-rank consequence
2^(q-O(log q)), are justified in the stated black-box oracle model.

The separately attributed two-scenario consequence of the public
three-matroid-intersection theorem also passes. It is not a claim
that the q-scenario construction itself has constant scenario count.

## 1. The forbidden-family rank is valid everywhere

If two distinct forbidden r-sets have intersection at most r-2,
define independence by all sets of size at most r-1 and all
nonforbidden r-sets. Heredity is immediate.

For augmentation, the only nontrivial case is an independent
(r-1)-set I and an independent r-set J. If J minus I has one
element, adding it produces J. Otherwise two candidates I+a and
I+b share r-1 elements, so at most one can be forbidden. One
augmentation succeeds. This proves the matroid axioms.

Because q>r, an (r-1)-set has two possible outside extensions, so
the rank is actually r. Every set of size above r contains such
an allowed extension. Consequently the stated function

    min(|S|,r) - 1[|S|=r and S is forbidden]

is the rank on all sets, not just on r-sets. Removing one forbidden
r-set preserves validity and changes precisely its one rank answer.
Singleton ranks equal one because r>=2.

## 2. Residue classes and their size are correctly encoded

If two r-sets differ in one exchanged element a,b, their label
sums modulo q differ by a-b. Distinct labels in 0,...,q-1 have
nonzero difference modulo q. Hence every equal-residue class has
the required intersection property.

The q classes partition all r-subsets, so a largest class has
size at least binom(q,r)/q. The stated dynamic program chooses
its residue in polynomial bit time. Each counter has at most
q+1 bits, there are polynomially many states, and two consecutive
ground-prefix layers suffice for polynomial space. The hidden
class need not be listed explicitly.

## 3. Exactly one basis has positive integer service

Every selected basis has size r. Each scenario has Boolean
singleton caps, so positive integer service at every selected
player forces its unit incidence vector to be independent.

A basis in a residue class other than h is forbidden by that
class's known scenario. A basis in H_h other than A is forbidden
by the hidden scenario. A itself is allowed by every scenario.
Thus OPT=1 and a positive output must select exactly A.

Resource allocations may vary by scenario; this does not change
the necessary unit vector on the common selected basis. Allowing
unused units, zero assignments, zero costs and zero setup fees
does not weaken the conclusion.

## 4. The transcript proof includes the promised-positive case

The hidden oracle differs from the baseline only on A itself.
Queries to any other set or known scenario cannot distinguish
the possible hidden candidates.

A finite positive approximation factor on optimum one requires
strictly positive utility. Since the output is integral and at
most one, it must be one. Therefore it identifies A.

If two candidates are unqueried, the same transcript is compatible
with both, and one deterministic selected basis cannot be correct
for both. The |H_h|-1 lower bound is the correct conservative
statement: a promised-positive algorithm may infer and output the
last unqueried candidate. The proof does not assume that such an
algorithm must solve the baseline no-instance.

If the baseline transcript does not terminate early, its first
|H_h|-1 distinct candidate queries are still shared by a suitable
hidden positive instance. Thus the adversarial running-time argument
does not rely on termination on an out-of-promise baseline.

## 5. Encoding, central rank and parameterized scope

The known input consists of polynomially many bits and q scenario
handles. Every rank answer is O(log q) bits. A is private inside
the hidden oracle; it is not supplied as inspectable program source
or an explicit forbidden-set list.

At central rank, binom(q,floor(q/2))>=2^q/(q+1). Division by q
gives the stated lower bound 2^q/[q(q+1)]-1. For any fixed base
strictly below two, no polynomial factor in the known input can
bridge this exponential difference.

For fixed corank c, binom(q,c)/q is Omega(q^(c-1)). A uniform
F(c)*poly(H) claim has one polynomial degree independent of c;
choosing a sufficiently large fixed c contradicts the bound as
q grows. The same argument works for fixed rank. The growing
scenario count is essential to this parameterized conclusion.
It must not be silently attributed to the two-scenario reduction.

This is an information bound for oracle matroids, distinct from
the conditional explicit Hitting Set reduction.

## 6. Fresh verification of the public three-matroid theorem

I opened the current cited version directly:

Doron-Arad, Kulik and Shachnai, *You (Almost) Can't Beat Brute
Force for 3-Matroid Intersection*, arXiv:2412.02217v2:
https://arxiv.org/html/2412.02217v2

Theorem 1.1 states the membership-oracle lower bound
2^(q-5*sqrt(q)*log(q)) for three matroids when q>=4 is a square.
It covers the paper's randomized decision model and therefore
deterministic algorithms. The source distinguishes oracle
matroids from explicitly represented matroids.

This verifies the version, oracle interface and numerical exponent
used in Section 8 of the manuscript. No older abstract or secondary
summary is substituted for the theorem.

## 7. Two scenarios and rank-query simulation

For three equal-positive-rank matroids M1,M2,M3, use M1 as the
original player matroid and M2,M3 as the two unit-recipient
scenario resources. A selected M1-basis of size r has positive
service in both scenarios exactly when it is a basis of all three.
Thus robust integer optimum is one in a yes-instance and zero
otherwise. Unequal ranks have no common basis, and the rank-zero
case is trivial preprocessing.

A query for the rank of S in an independence-oracle matroid is
simulated by scanning S and greedily adding an element whenever
independence is retained. This uses at most |S|<=q independence
queries and ends in a maximal independent subset, hence a basis
of the restriction and its correct rank. Rank computations for
the original player matroid are handled in the same way.

A hypothetical robust allocation algorithm using a fixed exponential
base below two would therefore decide the source problem with only
a polynomial overhead in independence queries. Its final positive
output is checked by ordinary independence tests. This contradicts
the primary bound along the infinite square-q sequence.

The resulting two-scenario statement has an arbitrary original
player matroid and a subexponential-factor loss. The self-contained
q-scenario statement instead has a uniform original player matroid
and a polynomial-factor loss. The manuscript keeps those differences.

## 8. Compatibility and limitations

The obstruction is for one common selected basis and positive
integer utility. It does not transfer to continuous splittable
flow or to a compulsory fixed player set. All units can be heavy
under the same threshold in every scenario, so merely counting
light/heavy disagreements does not remove the obstruction.

An additive guarantee that may output zero at optimum one is
consistent with the theorem. A supplied actual robust unit witness
reveals the missing selected basis and is substantial extra input.

The proof establishes no ordinary explicit eligibility-list
lower bound and no impossibility of all q-exponential algorithms.
It excludes fixed bases below two in the stated unrestricted
robust oracle model. Both the mathematical construction and the
public attribution pass without a substantive correction.
