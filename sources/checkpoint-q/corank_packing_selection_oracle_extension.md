# Corank gap branching for selection oracles and set-packing capacities

**25 October 2026. General consequence of the batch theorem; independent audit requested.**

The proof in `unit_quota_corank_batch_branching_improvement.md` uses
less structure than a player matroid and a recipient polymatroid.
This note isolates the two oracle requirements and derives a
resource-augmentation scheme. It is a scope extension of the same
bounded search tree, not a separate claim of a new literature result.

## 1. The two oracle interfaces

Let P have q elements. Fix an integer r, and let B be any family of
r-element subsets of P. Assume a **restriction selection oracle**:
on input Q subseteq P, it either returns a member I of B contained
in Q, or certifies that no such member exists. The oracle runs in
polynomial time and is charged to the algorithm.

The resource system has a possibly implicit family A of subsets of
P and nonnegative rational capacities u_A for A in A. Its packing
region is

\[
 \mathcal P(u)=\{z\in\mathbb R_{\ge0}^{P}:
                              z(A)\le u_A\text{ for every }A\in\mathcal A\}.
 \tag{E1}
\]

Assume a polynomial **packing separation oracle** on the queried
vectors: it either certifies feasibility or returns a violated row
A together with its capacity u_A. We only need to query vectors
b*1_Q. Returned rows and capacities have polynomial-bit
representations. The family A need not contain every subset and
need not be associated with a submodular function.

All arithmetic, input bits, and both oracle costs are included in H.
Put c=q-r. If the selector reports that B is empty, all target
promises immediately fail; otherwise q>=r. Elements known to belong
to no member of B may be deleted first, but detecting them is not
assumed as part of the generic oracle interface.

## 2. Gap theorem for rational quotas

Let t>b>0 be rational numbers of polynomial bit length. The promise
is that some I* in B satisfies t*1_(I*) in P(u). The requested output
is an I in B satisfying b*1_I in P(u). These quotas need not be
integers for this abstract packing problem.

At a current ground Q, first call the selector. If no member remains,
return FAILURE. Otherwise retain the returned member for possible
use. Let d=|Q|-r, and separate b*1_Q against the **original full
packing system** (E1). If it is feasible, return the retained member
I subseteq Q; downward closure makes b*1_I feasible.

If the separator returns A, put S=A intersect Q, m=|S|, and

\[
                  \ell=m-\left\lfloor\frac{u_A}{t}\right\rfloor.
 \tag{E2}
\]

The violated inequality is u_A<bm. Nonnegative capacities and t>b
imply 1<=ell<=m. Every promised I* contained in Q has

\[
              t|I^*\cap S|=t|I^*\cap A|\le u_A,
                       \qquad |S\setminus I^*|\ge\ell.
 \tag{E3}
\]

If ell>d, failure is sound. Otherwise enumerate all ell-subsets D
of S and recurse on Q\D. One enumerated D is contained in
S\I*, so the promised I* survives that branch. The restriction
selector reports nonemptiness there. Induction proves that a
promised input cannot fail and that every returned set is valid.

For R=t/(t-b)>1, the strict violation gives

\[
                    \ell\ge m-u_A/t>m/R.
 \tag{E4}
\]

Therefore binom(m,ell)<=Gamma(R)^ell, with
Gamma(R)=R^R/(R-1)^(R-1). Every attempted deletion subset is counted
as a child, including those rejected immediately by the selector.
The full augmented computation tree has at most
(c+1)Gamma(R)^c nodes by the proof of B7--B8 in the batch note.

**Theorem E.** The rational t-versus-b promise problem has a
deterministic algorithm of running time

\[
                     \Gamma\!\left(\frac{t}{t-b}\right)^c
                                      \operatorname{poly}(H)
                \le\left(\frac{et}{t-b}\right)^c\operatorname{poly}(H),
 \tag{E5}
\]

using polynomial workspace. It either returns the requested b-unit
set or certifies absence of a t-unit set. For r=0, the selector first
checks whether the empty set is permitted; if so it is always
resource feasible because every capacity is nonnegative. For c=0,
the single possible r-element set is tested directly.

Keeping the full resource system in every separation call matters.
If its capacities do not come from a monotone submodular function,
restricting the list of resource rows to subsets of Q could omit a
relevant original inequality. Using S=A intersect Q only in the
branching calculation avoids that issue.

## 3. A fixed-parameter resource-augmentation scheme

Suppose the desired integral selection is I in B with

\[
                              |I\cap A|\le u_A
                                \quad\text{for every }A\in\mathcal A.
 \tag{E6}
\]

Fix rational epsilon>0. Inflate the capacities to
u'_A=(1+epsilon)u_A, and run Theorem E with

\[
                             t=1+\epsilon,\qquad b=1.
 \tag{E7}
\]

Any set satisfying (E6) satisfies the stronger promise
(1+epsilon)*1_I in P(u'). A successful output satisfies

\[
                          |I\cap A|\le(1+\epsilon)u_A
                                      \quad\text{for every }A\in\mathcal A.
 \tag{E8}
\]

A failure proves that no set satisfies the original capacities.
The running time is

\[
           \left(\frac{e(1+\epsilon)}{\epsilon}\right)^c
                        \operatorname{poly}(H)
                 =\bigl(O(1+\epsilon^{-1})\bigr)^c\operatorname{poly}(H).
 \tag{E9}
\]

Here H includes the bit representation of epsilon, not its numerical
inverse. The explicit exponential factor contains the full
dependence on the accuracy parameter. Rational floor calculations
in (E2) use exact integer numerator/denominator arithmetic.

This is a resource-augmentation statement. The output is an exact
member of B and an integer incidence vector; only the capacity
guarantee is relaxed. No exact t=b feasibility algorithm is invoked.

## 4. Concrete selection and resource examples

For one player matroid, the restriction selector is ordinary rank
and basis computation. For two player matroids of rank r, it is
ordinary matroid intersection on the restricted ground, seeking a
common independent set of size r. Thus Theorem E gives the four-unit
promise/two-unit output and other positive-gap theorems for common
bases of two arbitrary oracle matroids as well.

The resource system may consist of an explicit list of subset
capacities. More generally, for a nonnegative rational submodular
rank f, the full polymatroid rows u_A=f(A) are separated at b*1_Q
by minimizing f(A)-b|A intersect Q| over the original ground. This
uses deterministic submodular minimization. Positive rational
capacity scaling in Section 3 preserves this property.

Consequently two arbitrary player matroids, plus an arbitrary
recipient polymatroid, admit the resource-augmentation scheme
(E8)--(E9) in the corank parameter. This statement requires no
linear representation of the player matroids and no expansion of
binary resource counts.

## 5. The one-unit optimization gate does not disappear

Only the positive-gap theorem transfers automatically to a general
selector. The factor-two **integer unit-value optimization** wrapper
in the original corank note also used an exact one-unit feasibility
algorithm. That extra ingredient was matroid intersection between
one player matroid and the recipient Boolean-cap matroid.

With two player matroids, exact one-unit feasibility additionally
requires intersecting their common-basis condition with the third
recipient Boolean matroid. The restriction selector supplied above
does not solve that problem. We therefore do not infer the original
factor-two integer optimization guarantee for two-player-matroid
selection from Theorem E alone.

The resource-augmentation formulation avoids this gate because its
promise has rational t=1+epsilon>b=1. A very small epsilon can make
the augmented integer capacities effectively exact, but then the
explicit epsilon dependence in (E9) must be retained; no uniform
exact-feasibility fixed-parameter claim follows.
