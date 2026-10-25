# Independent audit of the global allocation, scheduling, and flow transfers

**25 October 2026. Full independent read of E1--E18 and all twelve
sections of `global_exponential_allocation_flow_transfers.md`.**

The complete application manuscript passes. The global conversion
removes the small-corank and heavy-support hypotheses from the stated
running-time guarantees, while preserving each original approximation,
budget, and output model. All displayed algorithms remain deterministic
and use polynomial space. The balanced hidden-set oracle barriers also
hold in their stated models.

The global conversion itself was independently rederived in
`polynomial_space_global_gap_second_audit.md`. This audit checks the
application interfaces and complete algorithms; it does not infer an
application merely from substituting a corank into the base formula.

## 1. What the global wrapper must preserve

The protected selected portion has a fixed positive cardinality s.
After a forced seed Z, its allowed ground is P\Z and its remaining
omission count is q-s-|Z|. Original resources, capacities, assignment
costs, routing constraints, and completion options retain their meanings.

For every application below, a full-target witness whose selected
portion avoids Z remains a full-target witness for the extension
call. Every extension success supplies a valid relaxed solution of
the original problem. The underlying weighted or unweighted corank
proof gives a uniform running-time bound on all seeds, including those
that destroy every full-target witness or even every feasible selection.
These are exactly the hypotheses needed by the global cover proof.

No target or approximation loss is applied successively across blocks.
Each streamed seed invokes one original gap with the same full and
relaxed targets. Polynomially many support sizes, value splits, and
outer search queries add only polynomial factors to the maximum
whole-ground bound.

## 2. One-value arbitrary-cost allocation satisfies the fixed-region interface

Restricting the original matroid's allowed player ground to Q preserves
its target rank r; if no original basis remains, the selector rejects.
The fractional count region keeps the original recipient constraints
and actual type-player costs. Service is requested only on Q. Counts
outside Q can be discarded because resource constraints are downward
and costs are nonnegative.

A full-K original basis avoiding a seed retains its original allocation,
so the quota gap has the required extension promise. Its remaining
deficit is (q-r)-|Z|. For every integer K>=2, the output quota
b=ceil(K/2) has K/(K-b)<=3. Since Gamma is increasing, A=27/4 is
a single rational bound valid across all target calls. Its logarithmic
derivative log(R/(R-1)) is positive, as stated.

The fractional output is converted to exactly b integer units per
selected player by minimizing actual cost on the integral full-total
direct-sum/partition intersection face. This costs no more than the
fractional witness and loses no units. It is polynomial work after
each successful gap, not an additional exponential selection step.

The exact K=1 coverage gate, zero initialization, external upper quota,
and one-sided integer search are unchanged. Every failure excludes the
full original quota, while a nominal success need only give its half
quota. At adjacent integer endpoints the saved nominal quota is at
least the integer optimum, yielding ceil(K*/2) units. The complete
factor-two bound is therefore T_(27/4)(q,H) for every positive original
rank. The original empty-selection convention handles rank zero
separately; no minimum over an empty selected set is needed.

## 3. Compulsory two-value allocation needs all heavy options after a seed

For fixed support cardinality k<q, the protected small set has size
q-k and its omission deficit is k. A forced seed is intended to remove
small candidates only. The minimum-heavy completion oracle therefore
keeps every original eligible heavy pair, including those owned by
players in the seed. Its actual chosen heavy support covers the
complement of its returned small set.

If the original full-target pair has small set I* and actual heavy
assignment H*, and I* avoids Z, then H* remains a permitted completion
at Q=P\Z. The minimum cost h_k(Q) is at most c(H*), so the original
small allocation remains feasible under the current residual budget
C-h_k(Q). The same fixed pair supplies this inequality at every
surviving recursive child. This proves the extension promise with
remaining deficit k-|Z|.

At success, the output uses the completion attaining h_k(Q). The small
allocation serves every member of Q before restriction, hence serves
that completion's small complement. Exact integer b-quota recovery
does not raise its cost. Adding the attaining H_Q preserves C exactly.
No affordable-rank hypothesis is needed once all k are enumerated.
Skipping a k whose minimum completion cost at P already exceeds C is
safe, because no full-target pair of that cardinality could be affordable.

The k=q case is direct full heavy coverage; it is not sent to a
positive-cardinality global quota wrapper. K=1 uses exact one-unit
coverage on the original instance, and T>=2a uses the fixed all-player
LP with cost-preserving largest-unit rounding. Equality T=2a is included
in this latter branch. All hard successes give at least T/2, and total
failure still excludes the full integer T.

The original value-grid maximization therefore remains valid. There
are only q+1 support sizes and polynomially many targets. The global
factor-two result is unconditional in h_C and has time
T_(27/4)(q,H), with the exact assignment budget unchanged.

## 4. General intrinsic allocation has no remaining support promise

For one value split and k<r, the protected light set has size r-k.
Its complement consists of k selected heavy recipients together with
the q-r unselected players. Thus its omission deficit is q-r+k, and
a forced seed may contain either kind of player. The completion oracle
uses the full original player matroid and all heavy pairs; only light
labels are forbidden at seeded positions.

This distinction preserves the original full pair I*,H*: if I* avoids
Z, its original heavy assignment is still feasible and bounds the
minimum h_k(P\Z). The original fractional full-T light allocation is
therefore feasible in the corresponding current residual budget.
The adaptive extension runtime is Gamma(R)^(q-r+k-|Z|), uniformly on
bad seeds as well as promised ones. No resource is contracted to the
allowed light ground.

Each split/k search retains its original fixed joint benchmark:
a genuine original basis, an integral one-unit heavy completion,
fractional common light service, and combined cost at most C. Failures
of the global gap exclude the full target for this same benchmark.
The original external light-value bound and one-sided grid search
consequently produce a saved nominal target at least the benchmark.
There is no search over a target-dependent family of separately priced
heavy completions.

For an integer optimum, let alpha=1-1/R and split at
theta*=alpha*OPT/2, with equality heavy. Dropping all but one originally
assigned heavy unit per heavy recipient gives a feasible joint witness
without increasing cost. Its support k is always processed because all
k<=r are now enumerated. The light-only recipients retain full OPT
utility. The corresponding optimized fractional light output gives
at least alpha*OPT; cost-preserving lower rounding loses at most
u_L<theta*. Heavy units have value at least theta*. Both sides therefore
give the stated minimum theta* while meeting C exactly.

If k=r, an affordable pure-heavy basis supplies the needed candidate
directly. Empty classes and zero benchmarks use the existing exits.
When OPT=0, a basis with zero counts is legal and the guarantee is
immediate. The algorithm never needs to know theta* or OPT: it enumerates
every distinct input value split, including the empty classes.

The old raw-corank additive fallback could exceed the new global time
bound. The application explicitly omits it, which is safe because all
support sizes are processed and the zero initialization is valid.
Alternatively its own extension can be globalized. This detail closes
the complete algorithm's time accounting, rather than bounding only
its principal new subroutine.

The resulting guarantee has no corank, support, price-diversity, or
proportional-cost hypothesis. It retains the intrinsic-value restriction:
light and heavy resource types are disjoint. A player-dependent split
of a single original resource is not justified by this proof. Only one
scalar assignment budget is preserved.

## 5. Scheduling uses the physical machine ground throughout duality

The scheduling easy cases remain polynomial. If there are no large
units, the single-size box-rank test solves the instance exactly. If
the Boolean large-job rank is smaller than the total large count h,
every schedule places two large units somewhere, implying OPT>=2a.
The public additive-largest-job rounding then gives factor three halves.
These cases are part of the theorem, not excluded by a hypothesis.

In the hard branch, q=|P^+| counts explicit eligible large positions,
while the small-job rank and its capped dual are defined on all q_0
physical machines. The retained-rank check precedes dualization. Its
success ensures that completing a dual base produces a full original
small-job base, so every job is scheduled.

For a forced seed Z in P^+, the player ground becomes P^+\Z and its
required rank remains h. The dual F_T itself is neither redefined nor
contracted. A target-T schedule whose large basis avoids Z still
supplies the full K_T-unit promise in this same recipient polymatroid.
The remaining deficit is |P^+|-h-|Z|. For K_T>=2 its half quota is
covered by A=27/4; K_T=1 retains the exact intersection gate.

The returned b_T-unit vector is zero-extended to the full physical
ground and completed to an integer dual base y. Setting
x_b=1_I and x_s=C_T*1-y gives full original count bases. This completion
may place small jobs at omitted large positions and at machines that
were never large eligible, as it must be allowed to do.

Writing delta_T=a+C_T*u-T, the selected-machine load is at most
T+delta_T-b_T*u. Since b_T>=K_T/2 and K_T*u>=delta_T, this is at most
T+delta_T/2<=3T/2. Other machines have load at most C_T*u<=T.
There is no additional small-unit rounding error.

The original minimization search still has a genuine feasible upper
target and a failed lower target. Sound failures imply that the final
successful grid target is no larger than OPT, giving the claimed exact
three-halves ratio. The time is T_(27/4)(|P^+|,H), and the coarser
q_0-machine bound follows from |P^+|<=q_0. This does not substitute
physical machine count for a binary-expanded slot universe.

## 6. Global flow gaps compose with exact rational-comparator recovery

Forced omissions change only which commodities may be selected. The
physical network, all edge capacities, and all routing-budget rows
remain fixed. The selected cardinality r stays fixed as well. A full
permitted routing avoiding Z survives in the same downward service
region, so the original weighted gap provides the required extension
with deficit q-r-|Z| and base Gamma(R).

The global wrapper consequently has the same target interface as the
old corank gap: every success returns an actual selected set and valid
alpha*T routing; every total failure puts the full optimum below T.
The family of permitted sets does not change with the outer target.

For each returned set, its original common-rate optimum remains a
bounded rational LP with a known uniform denominator bound. The
rational-comparator lemma uses that original LP, an externally bounded
fine target grid, and exact reoptimization of the saved set. It removes
only the search error and preserves the full alpha=1-1/R guarantee.
It does not require the wrapper itself to be an exact feasibility
procedure or to have monotone successes.

Thus globalization and rational recovery are different operations with
compatible interfaces: the former reduces the target-gap running time,
while the latter removes the final search loss. Their polynomial
numbers of calls and polynomial-space implementations compose without
an extra exponential factor or a second accuracy loss.

All routing-only rows remain exact because there is no integer flow
rounding. A supported selection-cost condition remains inside the fixed
restriction selector. The original empty-family and rank-zero checks
and zero-rate initialization remain valid.

## 7. Explicit robust scenarios and shared setup have the stated scopes

For explicit robust scenarios, membership in the common service region
means membership in every scenario's service region. A violated row
from any one scenario is valid for their intersection. Every full
witness consists of one selected set and its scenario-dependent
routings; all of them survive any seed avoiding that set. The explicit
scenario count contributes only to H, not to the omission dimension q.
The fixed-set combined LP still supplies the denominator bound needed
for rational recovery.

This does not impose oblivious routing or an unstated common path
distribution. It also does not supply separation for an exponentially
large implicit scenario family. These limits are explicit.

With a shared setup-plus-routing cap, the exact minimum-setup optimizer
returns both h(Q) and an attaining I_Q. A protected original set I*
satisfies h(Q)<=setup(I*), so its original full routing remains feasible
under routing budget C-h(Q). That invariant is preserved after a forced
seed and along the adaptive recursion. Success restricts the weak
routing to I_Q and adds its actual setup cost h(Q), meeting C exactly.

The affordable selected family is fixed across the outer target search.
Exact reoptimization of a specified I uses routing budget C-setup(I),
so rational recovery applies without changing its comparator. First
testing h(P)<=C is necessary: zero routing does not make an unaffordable
selected set legal. Additional fixed routing-only budgets remain safe.
The theorem correctly requires a stronger optimizer than a feasibility
selector and does not infer it for arbitrary extra selection budgets.

## 8. The fixed-accuracy constants and encodings check

The half-quota cases uniformly use A=27/4 and base 50/27. Their exact
factors two and three halves come from separate integer quota arguments;
they are not obtained by substituting R=3 into the generic light-unit
rounding formula.

The generic intrinsic guarantee is alpha*OPT/2, hence factor
2/alpha=2R/(R-1). Flow instead retains fraction alpha. The displayed
constant table is correct:

\[
 R=2:\ A=4,\ \text{base }7/4;\qquad
 R=3:\ A=27/4,\ \text{base }50/27;\qquad
 R=5:\ A=3125/256,\ \text{base }5994/3125.
\]

For fixed eta>0, R=(2+eta)/eta gives intrinsic factor 2+eta.
Choosing integer R>=1+2/eta gives a factor no larger than 2+eta.
The bases are strictly below two for fixed positive accuracy loss,
approaching two as that loss goes to zero.

For fixed rational R=a/b, the relation
Gamma(R)^b=a^a/(b^b*(a-b)^(a-b)) makes local comparisons exact by
raising positive quantities to the fixed power b. If R is an arbitrary
binary input, the manuscript uses a supplied polynomial-bit rational
bound, with A=3R as a safe default, rather than hiding huge numerical
powers in polynomial arithmetic. The explicit subexponential overhead
in T_A is retained; its q+o(q) shorthand is reserved for fixed A.

## 9. The balanced allocation oracle barriers are valid

Set q=2r>=4. In the one-value construction, the uniform player matroid
requires r selected players, the total resource rank is 2r, and hidden
A receives two units each. Its optimum is exactly two. Any factor
strictly below two must return integer utility at least two on every
selected player. Their total is at least 2r, so their selected set I
must satisfy f_A(I)>=2r. Among r-subsets this identifies I=A.

In the compulsory two-value construction, the heavy rank is r and
each heavy unit is worth two. The total available value is 4r=2q,
while the hidden allocation attains two everywhere. Thus the optimum
is exactly two. A strictly better-than-two factor forces integer
utility at least two at every player. There are at least r small-only
players and only 2r small units in total, so exactly r are small-only
and each gets two. Their set must be A. Costs and the assignment budget
are zero, so the same argument applies to the arbitrary-cost models.

Every rank answer except that on A is independent of the hidden set.
An unqueried exceptional set can still be the hidden set. If at least
two candidates remain, no single identifying output can be correct
for both. This proves the binomial-minus-one deterministic query bound.

## 10. The balanced scheduling dual barrier also identifies the hidden set

For q=2r, define g_A(S)=2|S|+f_A(P\S)-2r. The original f_A has
marginals between zero and two, so this complement rank is normalized,
monotone, integral, and submodular. Its total rank is 2r. Its bases are
the complements x_s=2*1-y of bases y of f_A.

The vector y=2*1_A is an f_A-base. Therefore x_s=2*1_(P\A) is a
g_A-base, and placing the r size-two units on A produces makespan two.
The total workload is 4r=2q, so no schedule can have smaller makespan.

A factor strictly below three halves produces integer makespan at most
two. Every large recipient then gets zero small units. There are r
large recipients and 2r small units, so every other machine must get
exactly two small units. Its dual vector is exactly twice the indicator
of the large-recipient set I. Base feasibility implies f_A(I)>=2r,
hence I=A. The hidden scheduling rank differs from its common baseline
only at P\A, so the same query-indistinguishability argument applies.

All q machines are eligible for a large unit, and q=2r>=r+2 because
r>=2. Thus the physical-ground count and the hypotheses of the accepted
dual construction agree exactly with this balanced instance.

Since the central binomial coefficient is at least 2^q/(q+1), these
lower bounds are 2^{q-O(log q)}. All numerical ranks, sizes, and explicit
matroid descriptions in the examples have polynomial encoding. For
any fixed delta>0, (2-delta)^q times a fixed polynomial is eventually
smaller. This excludes the claimed strictly better factors with that
time in the deterministic full rank-value-oracle model. Oracle queries
made inside optimization primitives are included in this accounting.

The barrier is qualitative at the approximation threshold. It does not
show that 50/27 is the optimal base at factor two or three halves, does
not establish the same hardness for explicit ordinary eligibility
lists, and does not imply a flow analogue. The manuscript keeps these
distinctions intact.

## 11. Complete-algorithm and provenance conclusion

Every counted ground is explicit: nonloop potential players for
optional allocation, compulsory players for its two-value specialization,
eligible physical positions for the scheduling hard branch, and
candidate commodities for flow. Numerical multiplicities are never
expanded. Polynomial per-target reconstruction, exact-budget recovery,
and the original one-sided or rational outer searches preserve the
stated whole-ground bounds and polynomial space.

The monotone-local-search base formula is correctly attributed to
Fomin, Gaspers, Lokshtanov and Saurabh. The separate conversion audit
checked their primary Theorem 1.2, permissive-extension discussion,
and stated space cost. The application manuscript makes no exhaustive
priority claim for these allocation, scheduling, or flow consequences.

All E1--E18 claims pass this independent review. The central conclusions
are unconditional whole-ground exponential-time upper bounds in the
stated models, together with the balanced deterministic value-oracle
thresholds. They are not polynomial-time approximation claims, and the
globalization does not relax any of the exact budgets or capacities.
