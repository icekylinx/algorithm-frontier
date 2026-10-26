# Relevant remaining blockers recover the sharper resource coefficient

**25 October 2026. Addendum to the independently reviewed
general_resource_all_remaining_blockers.md.** The primary theorem and
its A1--A14 proof remain unchanged. This note gives a strictly more
selective completion rule with the same implicit reservation proof,
and recovers the sharp compact-relaxation coefficient without any
subset enumeration.

## 1. Select only unmarked matching bundles sharing a resource

For a newly found minimal candidate $c$, replace completion A4 by

$$
D_{\rm rel}(c)=\{b:\ b\text{ is a current matching record outside }Y,
                              \quad b\cap c\ne\varnothing\}.
 \tag{R1}
$$

The intersection here is between resource-index sets, not between
physical units. Different players may legally receive the same
resource under its recipient matroid.

Scanning at most $r-1$ explicit matching bundles computes (R1)
in polynomial time. If the group is nonempty, assign it to $c$.
If it is empty, process $c$ as a fresh free candidate. The groups
remain disjoint. Existing search, release and exchange rules are
unchanged.

## 2. The all-subsets induction remains valid

For any old selected subset $Z$ and resource $j\in c$,
every unmarked matching recipient at $j$ belongs to a record in
(R1). Consequently

$$
M_j\setminus\mathrm{owners}(D(Z)\cup D_{\rm rel}(c))
                           \subseteq Y_j.
 \tag{R2}
$$

The new reservation before adding the owner $p(c)$ is an
independent deletion from the old $Q_j(Z)$, and is contained
in $X_j\cup Y_j$. Availability places $p(c)$ outside that
span. Adding it preserves independence. At $j\notin c$, there
is only a deletion from an old independent reservation.

Thus every new all-subsets reservation is established by exactly the
same induction as in the primary proof. The algorithm does not test
any of them. Distinct receiving names, fresh and stored free centers,
earliest exchanges, group retirement and earlier maximality inherit
their existing proofs verbatim.

In particular, an empty relevant group is sufficient even when
unrelated unmarked matching bundles remain. Such bundles receive
none of $c$'s resources and hence cannot appear in the affected
resource reservations.

## 3. Every designated blocker now has a shared resource

Unlike the deliberately coarse primary completion, (R1) guarantees
that each blocker assigned to $c$ receives some resource in $c$.
This is enough for the sharper value charge; physical unit identities
are still unnecessary.

Charge the current cover to each center and its designated blockers.
If the center is a singleton resource of value at least $B$, every
assigned minimal blocker contains that same resource and is itself
a singleton. For $t\ge1$ blockers the total value of the star is
at most $(t+1)u\le2tu$.

If the center is not a singleton, each of its resources is below
$B$. Each blocker shares one such resource. A minimal blocker
containing that resource cannot also contain any resource worth at
least $B$, so it too is nonsingleton. Each bundle in this star
has value below $B+\min(u,B)$, and the number of bundles is
$t+1\le2t$.

The rank cover is bounded by the sum of center and blocker service
values, as in A9 of the primary manuscript. Therefore

$$
\Phi(X,Y)\le C_R(B,u)|Y|,
 \qquad C_R(B,u)=\max\{2u,\ 2B+2\min(u,B)\}.
 \tag{R3}
$$

The star partition is by assigned group records. It does not require
different stars to use disjoint resource indices. The same resource
may supply many distinct recipients.

## 4. Compact-relaxation guarantees and time

Let $\rho=(r-1)/r$, and let $\tau=\lambda^{-1}$ for a
certified available-bundle oracle, with $\tau=1$ in the exact case.
The strict lower cover inequality from the primary proof gives the
sufficient condition

$$
\tau B+\rho C_R(B,u)\le T.
 \tag{R4}
$$

An empty completed new blocker layer is then certified infeasible.
The rank-exponential composition count applies at equality. If

$$
\Delta=T-\tau B-\rho C_R(B,u)>0,
$$

then growth $|Y_i|>\gamma(r-k+|Y_{<i}|)$, with

$$
\gamma=\min\{1/2,\Delta/(2C_R(B,u))\},
$$

gives the usual rank-quasipolynomial count. Every actual operation
has polynomial cost. There is no $2^{\kappa}$ resource-rank factor
and no explicit $2^{|X|}$ subset cost.

For reference, put $d=\tau+4\rho$. For $r\ge2$, the largest
positive equality solution of (R4) is

$$
B^*=
 \begin{cases}
 (T-2\rho u)/(\tau+2\rho), & u\le T/d,\\
 T/d, & T/d\le u\le2T/d,\\
 \lambda(T-2\rho u), & 2T/d\le u<T/(2\rho).
 \end{cases}
 \tag{R5}
$$

Adjacent formulas agree. For rank one use $B^*=\lambda T$.
The positive domain here is that of this sufficient coefficient;
no matching LP lower bound or problem hardness is asserted at its
endpoint.

## 5. Arbitrary sizes and what this refinement changes

The fat threshold $B_0=T/d$ leaves $u<B_0$, so
$C_R(B_0,u)\le4B_0$. Thus the arbitrary-size ratios remain
$\lambda^{-1}+4-4/r$ exactly in rank-exponential time and that
quantity plus $\eta$ in the primary rank-quasipolynomial time.
The original $5-4/r$ exact-oracle theorem is unchanged.

The improvement is the selective blocker group and the sharper
compact-relaxation curve, including its positive-gap time bound.
The common-resource hypothesis is restored explicitly by (R1);
it is not attributed retroactively to the primary all-remaining
completion.

