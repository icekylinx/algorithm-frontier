# Unit-quota allocation by corank-bounded deficient-set branching

**25 October 2026. Internally reviewed corank theorem; the batch refinement is
the principal algorithm. See the independent and root audits.**

This note gives a deterministic gap algorithm for an arbitrary player
matroid and an arbitrary integral recipient polymatroid. The parameter
is the **corank of the player matroid after deleting its loops**. The
algorithm is independent of the earlier ordered-layer local search.
In particular, it resolves the four-unit-promise/two-unit-output
problem in time 4^c poly(H) for this complementary parameter.
The self-contained batch analysis is in
[unit-quota-corank-batch-branching-improvement.md](unit-quota-corank-batch-branching-improvement.md); Sections 2--5
below retain the simpler one-deletion argument as a pedagogical
predecessor. All headline runtimes and optimization statements use
the stronger batch algorithm.

The resulting factor-two algorithm for integer unit-value allocation
has a matching strict-below-two obstruction in the value-oracle model.
Neither the positive theorem nor its lower bound is asserted to be a
new result in the literature; a dedicated public comparison is still
required. All positive statements below have complete proofs.

## 1. Model and statement

Let M be a matroid of rank r on a finite set P. Let f be a normalized,
monotone, integer-valued submodular function on P, and write

$$
P(f)=\{z\in\mathbb R_{\ge0}^{P}: z(S)\le f(S)
                         \text{ for every }S\subseteq P\}.
 \tag{C1}
$$

The player matroid is supplied by rank or independence queries, and
f is supplied by value queries. Numerical ranks and quotas are binary
encoded. Every oracle operation, deterministic submodular
minimization, and numerical bit operation is charged to the running
time. Let H denote the full input length and the polynomially bounded
bit lengths of oracle answers.

Delete every loop of M, and restrict f to the remaining ground set.
Call the resulting loopless ground set P again, put q=|P|, and define

$$
c=q-r.
 \tag{C2}
$$

Loop deletion is harmless: every basis already avoids these elements;
an independent vector on the restricted resource extends by zero to
an independent vector on the original ground. The input size H still
includes the original ground set and the work needed for this
preprocessing.

For integers t>b>=1, a **t-unit basis** means an M-basis I with
t*1_I in P(f). A gap algorithm must either return an M-basis I with
b*1_I in P(f), or certify that no t-unit basis exists. It may succeed
even on an input without a t-unit basis.

**Theorem C.** Write Gamma(R)=R^R/(R-1)^(R-1) for R>1. Such a
deterministic gap algorithm exists with at most

$$
(c+1)\Gamma\!\left(\frac{t}{t-b}\right)^c
 \tag{C3}
$$

computation nodes, counting even candidate deletions rejected by a
rank test. Each node uses polynomially many input-oracle operations and
polynomial-bit arithmetic. Consequently its running time is

$$
\Gamma\!\left(\frac{t}{t-b}\right)^c\mathrm{poly}(H)
       \le\left(\frac{et}{t-b}\right)^c\mathrm{poly}(H),
 \tag{C4}
$$

and it can use polynomial workspace. For t=4 and b=2 this is

$$
4^c\mathrm{poly}(H).
 \tag{C5}
$$

The principal batch procedure and the complete proof of (C3)--(C5)
are in the batch-refinement note. It sets
ell=|S|-floor(f(S)/t), rejects ell>current corank, and branches over
all ell-subsets of necessarily omitted elements. The case r=0 returns
the empty basis immediately. If r>0, c=0 is covered directly by either
procedure. Retaining the immediate r=0 exit only improves the bound.

## 2. A deficient-set bound under the stronger promise

Consider any restricted ground set Q subseteq P for which M|Q still
has rank r, and put d=|Q|-r. The recipient resource is always the
restriction f|Q of the same original function. It is not a
contraction of f.

Suppose S subseteq Q violates the b-unit assignment to every element
of Q:

$$
f(S)<b|S|.
 \tag{C6}
$$

If I* subseteq Q is a t-unit M-basis, then

$$
|S\setminus I^*|\le |Q\setminus I^*|=d,
 \qquad
 t(|S|-d)\le t|S\cap I^*|\le f(S)<b|S|.
 \tag{C7}
$$

Therefore every deficient set on a promised instance satisfies

$$
(t-b)|S|<td,
 \qquad
 |S|\le\left\lceil\frac{td}{t-b}\right\rceil-1.
 \tag{C8}
$$

The inequality is strict, which matters at the boundary. For t=4,
b=2 the bound is |S|<=2d-1. For b=ceil(t/2) and t>=2, it is at most
3d-1 because t/(t-b)<=3.

A second elementary fact gives the branching rule. Every t-unit
basis I* omits at least one element of S. Otherwise S subseteq I*
would imply f(S)>=t|S|>b|S|, contradicting (C6). Deleting an omitted
element preserves both I* and the player rank r.

## 3. A pedagogical one-deletion recursion

The procedure receives Q subseteq P. Its invariant is that rank(M|Q)
is r. It executes the following steps.

1. Minimize the integer-valued submodular function
   S -> f(S)-b|S| over S subseteq Q by deterministic submodular
   minimization.
2. If its minimum is nonnegative, b*1_Q belongs to P(f|Q).
   Find any basis I of M|Q and return I. Downward closure and zero
   extension imply b*1_I in P(f) on the original ground.
3. Otherwise let S be a returned deficient set, and put d=|Q|-r.
   If (t-b)|S|>=td, return FAILURE.
4. Otherwise, for each p in S in a fixed deterministic order, test
   the rank of M|(Q\{p}). Skip the branch if its rank is below r.
   Recurse on every other Q\{p}, returning the first successful
   basis. If every branch fails, return FAILURE.

The guard in step 3 is essential. Without it, an unpromised input
could produce a large deficient set and invalidate the claimed
fixed-parameter bound. The algorithm never branches on such a set.

Only the player ground is reduced. The resource rank query at every
node is still f(S) for a subset S of the original ground. In an
application where f was itself obtained by dualizing another
polymatroid, the dual is formed once before this recursion. It must
not be recomputed on Q.

## 4. Correctness, including every failure branch

A returned basis is always a basis of the original matroid: all
recursive restrictions retain rank r, and restriction independence
is original independence. Step 2 verifies that b*1_Q is resource
independent, hence so is its subvector b*1_I. If the original input
had deleted loops or the recursion deleted other elements, zero
extension is valid because for any original set A,

$$
b|I\cap A|=b|I\cap(A\cap Q)|
                  \le f(A\cap Q)\le f(A).
 \tag{C9}
$$

It remains to prove that FAILURE is a sound certificate against the
t-unit promise. We prove this by induction on d.

If the guard in step 3 rejects, (C7) would force (C8) for any t-unit
basis, contradicting the guard. The rejection is therefore sound.
In particular, when d=0 every nonempty deficient set triggers this
guard: the only rank-r basis contained in Q is Q itself, and it
cannot be t-unit feasible.

Otherwise suppose a t-unit basis I* is contained in Q. The preceding
section supplies p in S\I*. Its deletion leaves I* inside Q\{p}, so
the rank test cannot skip this branch. The branch has corank d-1 and
still contains a t-unit basis. By induction it cannot fail. Hence a
parent node with a t-unit basis cannot report that all branches
failed. This proves soundness of every FAILURE and completes the
correctness proof.

No monotonicity of algorithmic success in t is asserted. A success
only supplies the promised b-unit output; a failure proves the
stronger target t impossible.

## 5. Oracle cost, numerical size, and workspace

At corank d, the guard permits at most

$$
B_d=\left\lceil\frac{td}{t-b}\right\rceil-1
 \tag{C10}
$$

children, and every child has corank d-1. If r>0 and d>=1, B_d>=1.
The total number of nodes is at most

$$
1+B_c+B_cB_{c-1}+\cdots+\prod_{i=1}^{c}B_i
                   \le(c+1)\prod_{i=1}^{c}B_i.
 \tag{C11}
$$

Writing R=t/(t-b)>1, one has B_i<Ri, so this one-deletion product is
at most R^c c!. In the critical four-to-two case it is the odd double
factorial (2c-1)!!. The batch refinement replaces this weaker bound
by the single-exponential headline bound (C3)--(C4).

The submodular objective f(S)-b|S| has polynomial-bit oracle values:
the additional arithmetic uses only log b+log q bits. The guard is
tested by cross-multiplying the integers (t-b)|S| and td, without
floating-point division. A rank query on a restriction can be
implemented from an independence oracle by ordinary matroid greedy
augmentation. Each node therefore has polynomial cost in H. Large
numerical resource capacities are not expanded into copies.

A depth-first traversal stores the current deletion set, the
deficient set and next branch index at each of at most c+1 levels,
plus polynomial workspace for the oracle subroutines. It does not
store the full search tree. Its workspace is polynomial in the
original input and oracle-answer bit lengths.

An optional preprocessing step for a fixed target t deletes any
player p with f({p})<t. Such a player cannot belong to a t-unit basis.
If this deletion drops the player rank, failure is sound; otherwise
it can only reduce the corank and improve the above bound. This
optimization is not required for the theorem.

## 6. The exact polynomial one-unit case

For completeness, an output quota of one can be handled without the
gap recursion. The integral polytope

$$
P(f)\cap[0,1]^P
 \tag{C12}
$$

is a matroid independence polytope, with rank function

$$
r_f(S)=\min_{A\subseteq S}\{f(A)+|S\setminus A|\}.
 \tag{C13}
$$

Its rank and independence queries are implemented by paid
deterministic submodular minimization. Matroid intersection with M
finds a common independent set of size r, or proves that none
exists. Thus a one-unit basis is found exactly in polynomial time.
In particular, the case t=b=1, which lies outside t>b in Theorem C,
is fully covered. The statement is about integer unit counts; no
continuous rounding is hidden here.

## 7. A factor-two optimization theorem

Assume r>=1 and define

$$
K^*=\max\{K\in\mathbb Z_{\ge0}:\text{an M-basis }I
                                     \text{ has }K1_I\in P(f)\}.
 \tag{C14}
$$

At target K>=2, invoke Theorem C with

$$
t=K,\qquad b=\lceil K/2\rceil.
 \tag{C15}
$$

The denominator K-b=floor(K/2) is positive and

$$
\frac{K}{K-b}\le3.
 \tag{C16}
$$

At K=1 use the exact one-unit algorithm. Use the batch version of
Theorem C at all larger targets. Since Gamma is increasing and
Gamma(3)=27/4, each target query
returns a basis with value at least ceil(K/2), or proves K>K*,
in time (27/4)^c poly(H).

To optimize, note the explicit upper bound

$$
K^*\le U_0=\lfloor f(P)/r\rfloor.
 \tag{C17}
$$

Keep an integer lower index L=0 with an arbitrary basis of value
zero, and an upper index U=U_0+1 certified to exceed K*. Query an
integer midpoint. On success set L to that midpoint and retain its
basis; on failure set U to that midpoint. The invariants are that U
exceeds K* and L has a recorded successful output. When U=L+1,
integrality gives L>=K*. This search does not assume that success is
monotone. Its output therefore has value at least

$$
\lceil K^*/2\rceil.
 \tag{C18}
$$

The number of queries is O(log(U_0+2)), which is polynomial in H.
If K*=0, the zero-quota basis is an adequate output. The r=0 problem
is vacuous and returns the empty basis separately rather than
assigning a finite value to a minimum over no selected players.

**Corollary C2.** Unit-value allocation with arbitrary player matroid
and arbitrary integral recipient polymatroid has a deterministic
factor-two algorithm in

$$
(27/4)^c\mathrm{poly}(H)
                          =2^{O(c)}\mathrm{poly}(H)
 \tag{C19}
$$

time and polynomial workspace, where c is the loop-deleted player
corank. Several unit-value resource types may first be aggregated
by summing their rank functions; integral polymatroid decomposition
recovers a feasible allocation to the original types without
expanding binary multiplicities.

## 8. Scope and the matching oracle threshold

Section 6 of [allocation lower bounds proof](../../problems/allocation-lower-bounds/proof.md)
reparameterizes its self-contained hidden-basis construction by
c=q-r. It requires at least binom(q,c)-1 resource queries for every
deterministic approximation factor strictly below two. For any
putative runtime F(c)q^C with fixed C, choose a fixed integer c>C
and let q grow. Therefore no strictly better uniform approximation
factor has fixed-parameter oracle runtime in c in this full model.

This lower bound matches the approximation threshold of Corollary
C2. It does not imply that the single-exponential time is optimal,
and it is not a hardness result for explicit restricted-assignment
instances or special succinct polymatroid representations.

The corank theorem also does not close the earlier rank-r
quasipolynomial four-to-two question when c is unbounded. The two
parameters describe different regimes. The existing rank-based
factor-three theorem and the new corank-based factor-two theorem
can both be run, with the best resulting feasible allocation kept.
No effort to lower the general-matching 4/5 exponent is used here.

For the original allocation/scheduling polymatroid framework and its
standard aggregation, box restriction and decomposition primitives,
see Bamas et al., *Santa Claus Meets Makespan and Matroids*,
arXiv:2307.08453v1:
<https://arxiv.org/html/2307.08453v1>.
The deficient-set branching proof above is self-contained.
