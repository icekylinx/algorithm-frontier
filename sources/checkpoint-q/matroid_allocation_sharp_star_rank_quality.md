# Sharper star charging and rank-sensitive quality for matroid allocation

**25 October 2026. New proof refinement; independent and root mathematical reviews completed.**

The root review is **matroid_quality_and_union_root_audit.md**.

This note strengthens the guarantee of
`matroid_allocation_current_blocker_quasipolynomial.md`. It preserves
the one-at-a-time earliest-circuit exchanges, last-layer refresh,
current blocker ownership and integer signatures audited in
`matroid_allocation_current_blocker_second_audit.md`. Only the value
accounting, the numerical growth test and the final certificate
inequality are changed.

The resulting guarantee is rank-sensitive, includes the exact
zero-slack boundary, and has a sharp domain of positive guarantees
against the compact relaxation. The lower-bound examples at the end
distinguish limitations of this certificate from actual LP gaps.

## 1. Notation and the improved coefficient

Let \(M\) be a matroid of rank \(r\ge1\) on \(q\) players, given
by an independence oracle. Resources have intrinsic positive rational
values, explicit liking sets, and largest value \(u\). Let \(Q(T)\)
be the compact relaxation with a base-polytope player vector \(x\),
resource capacities one, and \(0\le y_{pj}\le x_p\).

For a target integral bundle value \(B>0\), define

\[
 C(B,u)=\max\{u,\;2B+\min(u,B)\},\qquad
 \rho_r=\frac{r-1}{r}.
 \tag{Q1}
\]

Every bundle stored in the matching or a selected layer is inclusion
minimal above \(B\). Every current matching blocker intersects a
unique selected center, and each stored selected center is blocked
outside the explicitly handled free cascade.

### Lemma 1: current star value

For a fully blocked prefix with current blocker set \(Y\) and
forbidden resource union \(F=R(X\cup Y)\),

\[
                         v(F)\le C(B,u)|Y|.
 \tag{Q2}
\]

**Proof.** Assign each matching blocker to its unique selected center.
Consider one center \(A\).

If \(A\) is a singleton \(\{e\}\), then \(v_e\ge B\).
Any inclusion-minimal \(B\)-bundle containing \(e\) must itself
equal \(\{e\}\): any other resource could be deleted while retaining
value at least \(B\). Since matching bundles are resource-disjoint,
this center has exactly one blocker. Its whole star has value
\(v_e\le u\).

If \(A\) is not a singleton, every resource in \(A\) has value
strictly less than \(B\). Removing any one of them leaves value below
\(B\), so

\[
                         v(A)<B+\min(u,B).
\]

Each of its \(t_A\ge1\) blockers has value less than \(B\)
outside \(A\), because removing one resource of its intersection
with \(A\) leaves a proper subset of a minimal bundle. Therefore

\[
 \begin{aligned}
 v\bigl(A\cup R(Y_A)\bigr)
 &<B+\min(u,B)+Bt_A\\
 &\le [2B+\min(u,B)]t_A.
 \end{aligned}
\]

Stars are resource-disjoint: centers are disjoint, matching blockers
are disjoint, and a blocker cannot meet another center. Summing their
bounds proves (Q2). The weak inequality is intentional, since a
singleton star can have value exactly \(u\). No restriction on repeated
selected player names is used. \(\square\)

When \(u\le B\), this recovers \(2B+u\). When \(u\ge B\), the
new coefficient is \(\max\{3B,u\}\), improving the former
\(2B+u\) bound.

## 2. A strict fractional lower bound

During an augmentation phase, write \(k=|I|<r\), and let a completed
last layer \(i\) have earlier blocker count \(s=|Y_{<i}|\). Define

\[
 J_0=I\setminus\operatorname{owners}(Y_{<i}),\qquad
 U=P\setminus\operatorname{cl}(J_0),\qquad
 w=r-|J_0|=r-k+s.
 \tag{Q3}
\]

Thus \(1\le w\le r\). The current maximality test is exactly

\[
                         v(L_p\setminus F_i)<B
                         \quad(p\in U).
 \tag{Q4}
\]

If \((x,y)\in Q(T)\), then \(x(U)\ge w>0\). For each
\(p\in U\) with \(x_p>0\), the individual inequalities
\(y_{pj}\le x_p\) and (Q4) give strictly less than \(Bx_p\)
fractional value outside \(F_i\). Therefore, for \(B\le T\),

\[
                    v(F_i)>(T-B)x(U)\ge(T-B)w.
 \tag{Q5}
\]

The first inequality is strict. There are finitely many players, and
their positive \(x_p\) mass in \(U\) is nonzero. This strictness
also holds when \(B=T\), in which case the right-hand side is zero.

Consequently the following is a valid oracle-checkable certificate of
infeasibility of \(Q(T)\): an independent \(J_0\), a resource set
\(F\), and

\[
 \begin{split}
 &v(L_p\setminus F)<B\quad
                         (p\notin\operatorname{cl}(J_0)),\\
 &v(F)\le(T-B)(r-|J_0|),\qquad r-|J_0|\ge1.
 \end{split}
 \tag{Q6}
\]

In contrast with the original sufficient certificate, the last
inequality is allowed to be an equality. Its validity is supplied by
the strict lower bound (Q5), rather than by a strict star upper bound.

## 3. The finite-rank factor

Since \(s\le k<r\),

\[
             \frac{s}{r-k+s}\le\frac{r-1}{r}=\rho_r.
 \tag{Q7}
\]

At a completed maximal layer with \(Y_i=\varnothing\), all its
prefix blockers are the \(s\) earlier blockers. Lemma 1 and (Q7)
give

\[
                         v(F_i)\le C(B,u)s
                             \le \rho_r C(B,u)w.
\]

It follows that the local-search algorithm, with the growth test simply
\(|Y_i|>0\), is valid whenever

\[
                       \boxed{B+\rho_r C(B,u)\le T.}
 \tag{Q8}
\]

Indeed a failed test then produces (Q6), while every successful layer
has at least one distinct current matching blocker. All exchanges,
refreshes and the integer micro-signature are unchanged. The total work
is therefore

\[
                    \mathcal P\,2^{O(r)}
                       \operatorname{poly}(b+\log\mathcal P),
 \tag{Q9}
\]

with polynomial space. The original player count \(q\) occurs in the
explicit-input factor \(\mathcal P\); it does not replace \(r\)
in the exponential factor. The complete per-microstate implementation
accounting is in Section 7.3 of the second independent audit.

## 4. Explicit optimal target for this coefficient

For \(r\ge2\), the function \(B+\rho_r C(B,u)\) is continuous
and strictly increasing in \(B\). It has a positive solution to
(Q8) exactly when

\[
                         0\le u<\frac{T}{\rho_r}.
 \tag{Q10}
\]

Let \(B_r^*(T,u)\) be its unique equality solution. Put
\(a_r=1+3\rho_r=4-3/r\). Then

\[
 B_r^*(T,u)=
 \begin{cases}
 \displaystyle\frac{T-\rho_r u}{1+2\rho_r},
       &u\le T/a_r,\\[6pt]
 \displaystyle T/a_r,
       &T/a_r\le u\le3T/a_r,\\[6pt]
 \displaystyle T-\rho_r u,
       &u\ge3T/a_r.
 \end{cases}
 \tag{Q11}
\]

Only the positive portion of the last line is included. Adjacent
formulas agree at their common endpoints. The first line is

\[
                    \frac{rT-(r-1)u}{3r-2}.
 \tag{Q12}
\]

For \(r=1\), simply take \(B_1^*(T,u)=T\), with no restriction
on \(u\). Rank one can also be solved directly: select a nonloop
player with maximum total liked-resource value. The one-layer
certificate above gives the same conclusion. Rank zero is vacuous.

As \(r\) grows, the guarantee tends to

\[
 B_\infty^*(T,u)=
 \begin{cases}
 (T-u)/3,&u\le T/4,\\
 T/4,&T/4\le u\le3T/4,\\
 T-u,&3T/4\le u<T.
 \end{cases}
 \tag{Q13}
\]

The middle and last branches improve the earlier additive bound for
moderate or large resources. The finite-rank first branch also improves
its leading constant: for negligible \(u\), it is
\(T/(3-2/r)\). These are guarantees against the same compact
relaxation, not against a stronger configuration LP.

## 5. Positive slack and quasipolynomial time

Let \(r\ge2\), assume (Q10), and choose a rational
\(0<\varepsilon<B_r^*(T,u)/T\). Set

\[
             B=B_r^*(T,u)-\varepsilon T,
             \qquad \eta=\varepsilon/4.
 \tag{Q14}
\]

Use the same greedy operations but test current growth by

\[
                    |Y_i|>\eta\,(r-k+|Y_{<i}|).
 \tag{Q15}
\]

The change from \(1+|Y_{<i}|\) to \(r-k+|Y_{<i}|\) is only a
stronger numerical use of the same eligibility flat. Within a phase
\(k\) is fixed. Earlier retained blocker sets remain unchanged by
the earliest-circuit exchange, so completed earlier growth statements
remain true exactly as before.

Monotonicity of \(C\) gives

\[
                        B+\rho_r C(B,u)\le T-\varepsilon T.
 \tag{Q16}
\]

Also \(B\le T\), \(u<T/\rho_r\le2T\), and hence
\(C(B,u)\le3T\). If (Q15) fails at a maximal layer, Lemma 1 yields

\[
 \begin{aligned}
 v(F_i)&\le C(B,u)(s+|Y_i|)\\
       &\le C(B,u)(\rho_r+\eta)w\\
       &\le (T-B-\varepsilon T+3\varepsilon T/4)w\\
       &<(T-B)w.
 \end{aligned}
 \tag{Q17}
\]

This is an infeasibility certificate. In a feasible instance every
completed layer satisfies (Q15), so the quantity
\(r-k+|Y_{\le i}|\) grows by a factor greater than \(1+\eta\)
per completed layer and never exceeds \(r\). The depth is
\(O(\varepsilon^{-1}\log(r+1))\). The unchanged micro-signature
therefore gives

\[
 \boxed{\quad
 \mathcal P\,
 \min\!\left\{2^{O(r)},
       (r+1)^{O(\varepsilon^{-1}\log(r+1))}\right\}
       \operatorname{poly}(b+\log\mathcal P).
 \quad}
 \tag{Q18}
\]

Rank one is handled by its direct scan, so no separate approximation
parameter is needed there. At \(\varepsilon=0\), use (Q9) rather
than the logarithmic-depth estimate.

## 6. The positive domain is sharp for this relaxation

For any \(r\ge2\), take the free matroid of rank \(r\) on exactly
\(r\) players. Give them \(r-1\) resources, all liked by every
player, each with value

\[
                         u_0=\frac{rT}{r-1}=\frac T{\rho_r}.
\]

The compact LP is feasible: set every player variable to one and
give each player fraction \(1/r\) of each resource. Each receives
fractional value exactly \(T\). Integrally, at least one of the
\(r\) players receives no resource at all. Thus no positive
allocation guarantee against \(Q(T)\) is possible at this endpoint.
Increasing the common resource value gives the same obstruction above
the endpoint.

This is an actual LP-gap example. It explains why a theorem against
integer optimum, such as the separate fat-resource reduction, has a
different scope from rounding an arbitrary feasible \(Q(T)\).

## 7. What the star mechanism cannot improve by itself

The improved coefficient is not uniformly reducible merely by invoking
minimality, current unique blocker ownership, or repeated player names.

### 7.1 Small resources: the additive item term can be approached

Let \(h\ge2\), take all resources in one star to have value \(a\),
and choose

\[
                       B=(h-1+\tau)a,\qquad0<\tau<1.
\]

A center of \(h\) resources and a matching blocker of \(h\)
resources, sharing exactly one resource, are both inclusion-minimal
above \(B\). The center has one blocker and the star union has value

\[
                    (2h-1)a=2B+a-2\tau a.
 \tag{Q19}
\]

Here \(u=a\le B\), and the right side approaches \(2B+u\)
as \(\tau\) tends to zero. Taking \(h\) large makes \(u/B\)
arbitrarily small. Thus a uniform replacement of the additive \(u\)
by \(o(u)\) does not follow from these local star hypotheses.

### 7.2 The other branches

If \(B\le u\le3B\), use a center and blocker with two resources
each, sharing one, all three resources of value \(B-\zeta\).
For sufficiently small positive \(\zeta\), both bundles are minimal
above \(B\), and the union approaches \(3B\). A separate singleton
star can realize an exact larger global item maximum without weakening
the asymptotic average over many such two-resource stars. If
\(u\ge3B\), a center and blocker equal to the same singleton of
value \(u\) attain the coefficient \(u\) exactly.

### 7.3 A maximal state can realize the same obstruction

Replicate the star of Section 7.1 \(t\) times, using disjoint
resources. Use the free matroid on \(t+1\) players. The current
matching gives one blocker bundle to each of \(t\) players; the
remaining player owns all \(t\) selected centers. Repeated selected
owners are allowed by the actual current-blocker interface.

Let every player like all star resources, and give each player its own
additional resources of total value \(a_0<B\), each individual value
at most \(a\). The first layer consisting of those \(t\) centers
and blockers is fully blocked. The next eligible set is the whole
ground set. Its available liked resources outside the forbidden union
are exactly a player's private set, of value below \(B\); hence the
next layer is maximal and empty.

Nevertheless the compact LP is feasible at

\[
                 T=a_0+\frac{t}{t+1}(2h-1)a,
 \tag{Q20}
\]

by allocating each private set to its owner and splitting every star
resource equally among the \(t+1\) players. As
\(a_0\uparrow B\), \(\tau\downarrow0\), and \(t/h\to\infty\),
this value approaches \(3B+u\) to within \(o(u)\).

This is a valid current-state and resource-certificate obstruction.
It is not a proof that the prescribed scan order from an empty matching
must reach that state. Nor is it an integrality-gap barrier at factor
three: distribute the star resources as evenly as possible and keep
the private assignments. This gives every player at least

\[
                  a_0+a\left\lfloor
                            \frac{t(2h-1)}{t+1}\right\rfloor,
\]

which differs from (Q20) by less than one resource value. A method
using the same final star certificate cannot simply erase its additive
item loss; a stronger algorithm or a different certificate may do so.

## 8. Consequence for the separately audited fat-resource reduction

The separate matroid-union reduction uses an original player matroid
of rank \(r\), classifies resources of value at least \(\theta T\)
as fat, and calls the small-resource solver on a derived player matroid
of rank at most \(r\). Its proof is independent of this note.

Take

\[
                         \theta=\frac1{4-3/r}.
 \tag{Q21}
\]

For the small instance, \(u<\theta T\). With \(B=\theta T\),
its coefficient is strictly less than \(3B\), and its rank factor
is at most \(\rho_r\). Therefore

\[
               B+\rho_{r'}C(B,u)\le B+3\rho_rB=T.
\]

Consequently the exact rank-exponential solver supplies all selected
small players with value at least \(\theta T\); retained fat players
also receive at least \(\theta T\). The separately audited reduction
therefore gives factor \(4-3/r\) against integer optimum in
\(2^{O(r)}\operatorname{poly}(\mathcal P,b)\) time. Rank one is
exact. This factor tends to four as rank grows and is not a uniform
constant-below-four result for unrestricted rank. Matroid-union oracle
overhead is polynomial in the full input and is not asserted to be
linear in \(\mathcal P\).
