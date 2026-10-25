# Independent audit of compressed-slot corank scheduling

**25 October 2026. Fresh full review of S1--S28.**

This note independently reviews
`compressed_large_slots_corank_makespan.md`. The conditional
`(1+epsilon)OPT+u` guarantee, the single-exponential corank bound,
and the binary-capacity polynomial-space implementation pass the
checks below.

## 1. The parameter represents an actual natural-matroid corank

At target T, each largest-job count is bounded both by its original
singleton rank and by floor(T/a). The sum of those bounds is N(T).
The first box-rank check is indispensable: only after it retains
the full large rank h can N(T)-h be called a nonnegative corank.
The manuscript uses the budget predicate N(T)<=h+k before this
check and never applies a running-time formula to a negative value.

On a conceptual slot ground with s_p positions for machine p, the
natural matroid of the original large polymatroid has rank h exactly
when the box check passes. Individual positions need not be named or
expanded. Its independent sets and bases are determined by their
owner count vectors, which are the states used by the implementation.

## 2. The smaller-workload dual stays on the full machine set

The engineered quantum Delta makes the target cap C, the largest
quota t and the output quota b integral, with b=(1-epsilon)t exactly.
Aggregating the smaller workload gives an integral rank F. If the
coordinate cap at C loses total rank, no original target schedule
exists. If it retains total rank, the complement rank

    f_T(S)=C|S|+G(P\S)-F(P)

is normalized and monotone; its marginal is C minus a capped-rank
marginal. Its bases are exactly the complements of capped smaller-
workload bases. This construction uses every physical machine,
including machines with no largest-job slot.

An original target schedule has smaller workload w* and large
counts x*, so its complementary dual y* satisfies y*>=t x*.
Therefore t x* is an independent vector of the fixed f_T. The
manuscript correctly retains that same f_T after every count deletion.
Recomputing it on a reduced owner set would not preserve this argument.

The lift `f_T(owners(Z))` is submodular on conceptual positions:
owner unions are exact, owner intersections contain the owners of
position intersections, and monotonicity closes the latter inclusion.
Uniform t units on a chosen position basis are equivalent to t times
its owner-count vector being feasible in f_T. This validates the
conceptual explanation without requiring its expansion.

## 3. Compressed omission preserves a witness

At a node with remaining capacities n, a full-rank box has omission
budget d=n(P)-h. A negative minimizer of `f_T(S)-b n(S)` supplies a
set with m=n(S) and forced omission number

    ell=m-floor(f_T(S)/t).

Nonnegativity and strict violation imply 1<=ell<=m. Any promised
large base x* satisfies x*(S)<=floor(f_T(S)/t), so its unused counts
n-x* contain at least ell units on S. If ell>d, no such witness
can exist. Otherwise some bounded integer deletion pattern of total
ell fits inside those unused counts. That branch retains the same
x*, the same t-quota feasibility, and full large box rank.

Conversely, a successful leaf verifies b n in the resource polymatroid
and chooses an actual large base x<=n. Downward closure then verifies
b x. Thus every success is valid on unpromised targets as well.
Patterns are sufficient because all positions of one owner are
exchangeable in both relevant constraints.

## 4. All attempted patterns have the entropy bound

The strict violation gives ell>m/R for R=1/epsilon. A pattern maps
injectively to an ell-subset of conceptual positions by taking a
fixed initial segment of each owner's positions. Hence there are
at most binom(m,ell)<=Gamma(R)^ell patterns. The recursion charges
every attempted pattern, including those rejected immediately by
the large rank test, and decreases its budget by exactly ell.
The accepted batch induction therefore bounds the complete attempted
tree by (c+1)Gamma(R)^c.

The exact-sum generator is also important. At every coordinate,
its stated interval excludes choices that cannot be completed with
the remaining capacities. Every retained partial assignment extends
at least one pattern, so the traversal has polynomial overhead per
emitted pattern. A full rectangular enumeration at every small-corank
node would not justify the same bound; the manuscript avoids it.

## 5. The large-corank branch closes the space issue

Because c can be binary encoded, a recursion of depth c would not
by itself establish polynomial workspace. The split at c<q^2 solves
this. In that branch every stack has polynomial depth, and each
frame contains only physical count vectors and binary counters.

When c>=q^2, enumerating all q-coordinate deletion vectors of total
c, or even their containing rectangle, has at most (c+1)^q attempts.
I rechecked the numerical comparison:

    q log(c+1)<=c  whenever c>=q^2 and q>=1.

For fixed q, the difference c-q log(c+1) increases on this range.
At c=q^2 it is nonnegative because x-log(x^2+1) is increasing for
x>=1 and positive at one. Thus (c+1)^q<=e^c, including q=1.
For epsilon<=1/2, Gamma(1/epsilon)>=4>e. The enumeration therefore
fits the promised exponential factor and uses only q binary counters.

Every promised large base appears as x=s-z in this enumeration.
The tests that x is a large base and b x is dual-independent are
on physical-machine subsets. The large branch is therefore both
complete under the promise and sound on arbitrary input targets.

## 6. Reconstruction preserves all original jobs

Completing b x to a full dual base and complementing back gives a
base of the capped smaller-workload rank. Since the cap retained
the original total rank, it is also a base of F. The polynomial-size
sum decomposition gives fractional original smaller-job bases.
Upper prefix rounding increases each machine's smaller workload
by at most u while preserving every original resource base.

The largest-job counts remain x and can be decomposed among the
original equal-sized largest types. At each machine the final bound is

    T+(a-b Delta)x_p+u
      =T+epsilon a x_p+u
      <=(1+epsilon)T+u,

because x_p<=floor(T/a). This is valid with many largest units on
one machine. No hard-target condition T<2a is being used implicitly.

## 7. The budget prefix and minimization search are sound

N(T) is nondecreasing, so its budget predicate defines a prefix of
the original load grid. The largest in-budget grid target T_cap
between zero and the known feasible total workload V is well-defined
and computable in polynomial bit complexity.

If the optimum satisfies the supplied surplus budget, then T_cap
is at least OPT and the target routine must succeed there. Starting
from a genuine infeasible lower target zero and that saved success,
the one-sided minimization search maintains that every failed lower
endpoint is strictly below OPT. At adjacent endpoints the upper
endpoint is at most OPT, yielding the stated strong schedule.

This argument does not require algorithmic success to be monotone.
It also shows that a success at T_cap can yield the strong guarantee
even when the sufficient budget condition is not known to hold.
If T_cap is zero or fails, the public additive fallback is retained.
No target excluded only by the budget is called infeasible.

## 8. Boundaries and conclusion

Empty instances, one positive size, and the absence of a designated
largest class are handled separately. The main nontrivial branch
has h>0 and therefore OPT>=a>0. Its original load grid is exact for
all integral schedules, and all search ranges have polynomial
binary length.

The result keeps the explicit smaller-unit term u. Its small-unit
corollary is conditional, and its comparison to the exact two-size
three-halves theorem does not erase that different theorem's lack
of an additive loss. The public OPT+a fallback remains available
throughout.

I found no substantive proof, parameter, numerical, reconstruction
or space gap in S1--S28. This is an internal mathematical audit,
not an external novelty certification or formal verification.
