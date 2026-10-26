# General resource matroids with all remaining bundles as conservative blockers

**25 October 2026. Internal root, exchange and source audits completed.**

The all-subsets invariant in
general_resource_matroid_subset_reservations.md can be maintained
without enumerating subsets. For a newly found candidate, designate
every currently unmarked matching bundle as its blocker. Some of
these bundles may receive no resource in the candidate. They are
nevertheless valid conservative blockers by the simultaneous
reservation proof below, and their values are paid in the coarse
cover inequality.

For player-selection rank $r\ge1$, the main guarantee is

$$
\boxed{\begin{gathered}
 \text{factor }5-4/r\text{ in }2^{O(r)}\mathrm{poly}(H),\\
 \text{factor }5-4/r+\eta\text{ in }
 \mathrm{poly}(H)
 \min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}.
 \end{gathered}}
 \tag{A1}
$$

Here $H$ includes the full explicit input and numerical encoding,
and all oracle work is paid. The quasipolynomial branch has no
resource-rank or subset-enumeration factor. This is a new construction,
not a statement printed in a public source. Primary-source comparison
remains separate from mathematical validation.

## 1. Model and imported player-side operations

There is a player-selection matroid $M$ of rank $r$ on an
explicit set $P$. Resource $j$ has common intrinsic nonnegative
rational value $v_j$ and an arbitrary recipient matroid $R_j$
on $P$. Its receiving-player set must be independent in $R_j$.
For each pair (player, resource), at most one service is supplied. Loops encode
unacceptable recipients.

The output supplies players forming a basis of $M$, each receiving
a set of resources with additive intrinsic utility. One resource may
serve several players when its recipient matroid permits it. Unused
capacity is allowed. In the compulsory-player model, receiving sets
may afterwards be extended to resource bases; nonnegative values only
increase. A requirement for a resource basis restricted to an
arbitrarily chosen player subset is not asserted.

Rank zero is the empty allocation. For rank one and exact
unrestricted availability, choose a nonloop player with maximum total
value of individually permitted resources; this is exact.

We import the audited player-side operations from
matroid_allocation_current_blocker_quasipolynomial.md and
matroid_allocation_current_blocker_second_audit.md: earliest
one-at-a-time fundamental-circuit exchanges, last-layer refresh,
immediate old-free-center cascades and the integer micro-signature.
The new resource invariants are proved here. They do not assume
physical item intersections.

For target $T$, the small-resource relaxation is

$$
\begin{split}
 &x\in P_{\mathcal B(M)},\qquad
   y_{\cdot j}\in P_{\mathcal I(R_j)}\quad(j\text{ a resource}),\\
 &0\le y_{pj}\le x_p,\qquad
   \sum_jv_jy_{pj}\ge Tx_p\quad(p\in P).
 \end{split}
 \tag{A2}
$$

No feasible point is required as input.
The search below is for positive rational T and B. At target zero,
any player basis with empty bundles is feasible, by downward closure
and the empty independent receiving sets. This also initializes the
one-sided target search and handles a zero optimum.

## 2. State, availability, and all-remaining completion

In a phase, the current matching has independent owner set $I$,
$|I|=k<r$. Each matching bundle has a current record ID and one
owner. All matching and selected bundles are minimal above a fixed
threshold $B>0$.

Each selected center $c$ has a designated group $D(c)$ of
current matching records. Groups are disjoint. Let $X$ be the
selected centers and $Y$ the union of their groups. Every stable
group is nonempty; an empty group is handled immediately. “Blocker”
and “free” refer to this reservation structure, not to actual physical
intersections.

For resource $j$, write

$$
X_j=\{p(c):c\in X,\ j\in c\},\qquad
 Y_j=\{p(b):b\in Y,\ j\in b\},\qquad
 M_j=\{p(b):b\text{ currently matched},\ j\in b\}.
$$

A last-layer scan treats $j$ as available to $p$ precisely when

$$
p\notin\mathrm{cl}_{R_j}(X_j\cup Y_j).
 \tag{A3}
$$

At layer $i$, player eligibility is outside
$\mathrm{cl}_M(I\setminus\mathrm{owners}(Y_{<i}))$.
For an earlier layer use its own selected and blocker prefixes in
(A3). Each resource closure is determined by at most $2r$ names.

An eligible player with available total at least $B$ supplies a
minimal $B$-bundle $c$, by choosing available resources and
pruning. Define

$$
\boxed{\quad D=\{\text{all current matching records outside }Y\}.\quad}
 \tag{A4}
$$

If $D\ne\varnothing$, add $c$ to the last layer, assign
$D(c)=D$, and mark those previously unmarked records with that
center. If $D=\varnothing$, process $c$ as a fresh free
candidate. There are no subset tests or recipient-circuit searches
in this completion operation.

A designated blocker need not share a resource with its center.
Accordingly we use only the coarse coefficient $2(B+u)$, proved
below. We do not import the preceding manuscript's sharper singleton
charge, which relied on shared resources.

## 3. An all-subsets invariant without subset enumeration

For $Z\subseteq X$, let $D(Z)$ be the union of its designated
groups and $X_j(Z)$ its selected recipients at $j$. Maintain

$$
Q_j(Z)=
 \bigl(M_j\setminus\mathrm{owners}(D(Z))\bigr)
       \mathbin{\dot\cup}X_j(Z)\in\mathcal I(R_j)
       \qquad\text{for every }Z,j.
 \tag{A5}
$$

The dotted union means distinct receiving names. More explicitly,
selected centers using one resource have distinct owners and
$X_j\cap M_j=\varnothing$. Services to the same player-resource
pair are never silently identified by a set union.

Initially $X=\varnothing$, so the invariant is just actual matching
feasibility. It is a mathematical statement about all subsets; the
algorithm does not store or enumerate them.

### Lemma 1: completion establishes every new reservation

Let $c$ have owner $p$, be selected using (A3), and let $D$
be (A4). For every old $Z$ and each $j\in c$, the prospective
reservation is

$$
\Bigl(M_j\setminus\mathrm{owners}(D(Z)\cup D)\Bigr)
       \mathbin{\dot\cup}X_j(Z)\mathbin{\dot\cup}\{p\}.
 \tag{A6}
$$

Its part before $p$ is independent, being a deletion from
$Q_j(Z)$. Deleting all unmarked matching records leaves matching
names only in $Y_j$. The whole part before $p$ is therefore
contained in $X_j\cup Y_j$. By (A3), $p$ lies outside its
span, and adding it preserves independence. At resources outside
$c$, the prospective reservation only deletes old elements.

For distinctness, (A3) excludes $p$ from $X_j$ and $Y_j$.
If $p\in I$, player eligibility implies that its own matching
bundle lies in the earlier blocker prefix. Every resource of that
old bundle is therefore unavailable to $p$. Thus $p\notin M_j$
for every newly chosen resource. All new reservations and the stronger
distinctness invariant follow; old subsets are unchanged. $\square$

This proof is valid even if most of $D$ has no resource in $c$.
Those records are removed in every new reservation and later charged
as complete matching bundles, not as fictional intersections.

## 4. Fresh and stored free candidates

When a fresh candidate has $D=\varnothing$, Lemma 1 proves joint
feasibility with every old selected subset. The empty subset in
particular proves feasibility against the actual matching.

When a stored center $c$ loses its last designated blocker, (A5)
for $Z\cup\{c\}$ proves the same joint feasibility for every
subset $Z$ of the other centers. Thus an empty group certifies a
legal free center. The converse is unnecessary: a center that is
already feasible may continue to carry conservative blockers.

Use the accepted player-side rule. An owner outside
$\mathrm{cl}_M(I)$ augments and ends the phase. Otherwise
remove its own matching bundle if already matched; for a new spanned
owner remove a bundle in the earliest layer met by its fundamental
circuit. This is strictly earlier than the free center's search layer.
Truncate higher layers and remove the deleted record from its unique
designated group.

### Lemma 2: the exchange preserves retained reservations

For any retained $Z$, its new reservation is a subset of the old
reservation together with the incoming center's service. Deleting
the old matching record either removes an element already present,
or removes a blocker that had already excluded that same element.
The incoming service is jointly independent by Lemma 1 or by the
old invariant for $Z\cup\{c\}$. The new reservation is therefore
independent. The empty subset proves actual matching feasibility.

A fresh candidate excluded every retained occurrence of its owner
by (A3). A stored center already had a distinct owner from the other
centers using each of its resources. Its own old matching allocation,
if present, is removed. Consequently the matching remains disjoint
in player-resource pairs from retained selected centers. No receiving
names collapse in the dotted unions. $\square$

Only the one group losing the deleted record can become empty.
Process its center immediately. Each cascade moves to an earlier
layer, and uses the same stored resource bundle; it does not replace
that bundle after discarding its record.

Truncation releases designated groups without deleting their matching
allocations. Those records become unmarked and enter (A4) at a later
completion. Removing unrelated selected records does not change the
reservation for any retained $Z$.

## 5. Old maximality survives literally

Below the earliest exchange layer, selected bundles and designated
blocker bundles are the same record objects as before. None is the
deleted matching record, and the new matching record is not marked
in those lower layers. Their $X_j,Y_j$ sets and resource closures
(A3) remain identical.

The player-side earliest-circuit lemma preserves their eligibility
flats. Thus earlier completed availability inequalities remain true
on the identical domain and available lists. They do not depend on
current actual recipient circuits or on minimality of the designated
groups.

Only the last retained layer is refreshed. New blocked candidates are
adopted, free candidates are processed immediately, and each completed
growth test follows a full scan at an unchanged state. These are the
conditions used by the accepted signature analysis.

## 6. A coarse current-rank cover is sufficient

At a completed layer, let $J_0$ be the player independent set
after removing earlier blockers and $w=r-|J_0|>0$. Define

$$
\Phi(X,Y)=\sum_jv_jr_{R_j}(X_j\cup Y_j).
 \tag{A7}
$$

Every unavailable recipient of $j$ lies in that resource closure.
Its total fractional receiving mass is bounded by the rank in (A7).
A completed failed scan gives strictly less than $Bx_p$ fractional
available value for each positive eligible player coordinate. Hence,
for $B\le T$, feasibility of (A2) requires

$$
\Phi(X,Y)>(T-B)w.
 \tag{A8}
$$

Conversely,

$$
\begin{split}
 \Phi(X,Y)&\le\sum_{c\in X}v(c)+\sum_{b\in Y}v(b)\\
          &\le2(B+u)|Y|.
 \end{split}
 \tag{A9}
$$

Rank is at most cardinality, every stored bundle has value below
$B+u$, and nonempty disjoint designated groups give $|X|\le|Y|$.
No common resource between a center and blocker is used.

For matching size $k<r$, earlier blocker count $s$ and current
blocker count $y$, let $w=r-k+s$. Then
$s/w\le\rho_r=(r-1)/r$. An empty new layer produces a valid
infeasibility certificate whenever

$$
B+2\rho_r(B+u)\le T.
 \tag{A10}
$$

The certificate comprises the player flat, explicit selected and
designated bundles, their rank cover (A7), and the complete availability
scan. Its soundness uses strict (A8), so a weak upper cover inequality
is sufficient, including equality and rank one.

## 7. All actual operations have polynomial cost

The state stores only current matching bundles, selected bundles,
their group pointers, resource owner sets and layer data. There are
at most $r-1$ matching bundles during a phase, and at most $r$
selected records including a transient free center. Every bundle is
an explicit subset of the input resources.

A complete scan uses polynomially many resource independence queries
on sets of $O(r)$ names and the usual player-matroid queries.
Pruning is a value scan. Rule (A4) marks at most $r-1$ records.
An exchange changes one matching record and one group membership,
then releases higher-layer groups. Even whole-state scans per action
cost only a polynomial in $H,r$ and oracle work.

No operation tests (A5) by enumeration. Lemmas 1--2 maintain it
inductively. The preceding explicit-subset algorithm remains a valid
alternative with different blocker choices, but its exponential
work is absent here.

A blocked insertion increases the last selected count. A free
exchange decreases the earliest retained blocker count before later
coordinates matter. Layer appends follow the accepted infinity-sentinel
convention. The same micro-signature therefore strictly decreases at
every charged action. This proof uses designated group ownership and
changes, not actual resource intersections or minimal blocker sets.

At the exact boundary every successful completed layer has a blocker.
The rank-bounded composition count gives $2^{O(r)}$ states per
phase. Under growth $y>\gamma w$, it also gives
$(r+1)^{O(\gamma^{-1}\log(r+1))}$ states. There are at most $r$
phases. Wrapper storage is polynomial, plus oracle workspace.

## 8. Arbitrary sizes: factor $5-4/r$ and positive error

Set

$$
\rho=(r-1)/r,\qquad d=1+4\rho=5-4/r,\qquad B_0=T/d.
 \tag{A11}
$$

A resource is fat if $v_j\ge B_0$. Let $N$ be the union of
the fat recipient matroids and $U=M^*\vee N$. Matroid union and
decomposition are polynomial oracle operations. Independence in $N$
means a partition among fat resources, each part recipient-independent,
so each player can receive one legal fat service.

The audited dual-union complement argument gives an all-small promise
for a $U^*$-basis whenever the original target is feasible. Its
rank $r'\le r$, and its largest small resource is $u<B_0$.
At $B=B_0$,

$$
B_0+2\rho_{r'}(B_0+u)
                          \le(1+4\rho)B_0=T.
$$

Thus the rank-exponential algorithm applies. If $r'=0$, there
is no inner search. After success, decompose the complementary
$U$-basis, allocate the fat part, extend the dual part to an
$M^*$-basis, and discard allocations of the added players. The
remaining original basis retains legal small or fat allocations.
Deleting recipients preserves every resource's independence.

For $\eta>0$, keep fat threshold $B_0$ but use

$$
B=T/(d+\eta),\qquad
 \varepsilon=(B_0-B)/T=\frac{\eta}{d(d+\eta)}.
$$

The coarse coefficient is at most
$\overline C=2(B+B_0)\le4T/d$, and

$$
T-B-\rho\overline C
                          =(1+2\rho)(B_0-B).
 \tag{A12}
$$

Since $1+2\rho\ge d/2$ and $d\ge1$, the gap divided by
$\overline C$ is at least $\min\{\eta,1\}/16$. Use
$\gamma=\min\{\eta,1\}/64$. Failure of a completed growth test
yields the cover certificate; passing layers have multiplicative
growth. This proves (A1), with polynomial work per charged state and
no dependence on recipient rank in the quasipolynomial exponent.

## 9. Configuration comparator and target search

The configuration LP uses player-feasible resource subsets of value
at least $T$, player masses in $P_{\mathcal B(M)}$, and
recipient marginals in $P_{\mathcal I(R_j)}$. Choose one fat
resource from each fat-containing configuration. Its fractional
recipient vector is coordinatewise bounded by the original resource
column and remains in that resource's independent-set polytope.
Their sum $f\le x$ belongs to the union polytope of $N$.

As in the audited configuration addendum, $1-x+f$ lies in
$P_{\mathcal I(U)}$, has a dominating base vector, and yields a
complementary derived base vector $x'\le h=x-f$. Scale each
player's all-small marginals by $x'_p/h_p$, taking zero when
$h_p=0$. Resource columns only decrease, and target values become
at least $Tx'_p$. This proves inner failure soundness against the
configuration LP without computing its variables.

All configuration values lie on the common rational value grid.
The total possible delivered utility is bounded by
$V=\sum_jv_jr(R_j)$. Initialize a failed grid target above
$(d+\eta)V$, or the exact-ratio counterpart. The established
one-sided binary search only uses that failure excludes that target
and larger feasible targets; success need not mean feasibility of the
full target. It returns the stated ratio against the optimal
configuration target with polynomially many trials.

## 10. Local families and approximate available oracles

For a player-local downward-closed resource family, invoke its oracle
on the resource list (A3). A factor-$\lambda$ feasible oracle,
$0<\lambda\le1$, and a complete failed scan at an unchanged state
give true available optimum below $B/\lambda$. The row perspective
constraint and downward closure replace (A8) by

$$
\Phi(X,Y)>(T-B/\lambda)w,\qquad B\le\lambda T.
 \tag{A13}
$$

Minimality, conservative completion and the coarse cover are unchanged.
Use fresh scans; do not assume monotonicity of approximate witnesses.
The sufficient condition is $B/\lambda+2\rho(B+u)\le T$.

Restrict each fat recipient matroid to players whose singleton service
is locally feasible. A positive-factor feasible oracle decides this
on a singleton input. The restriction is a matroid. The fat and
configuration proofs preserve the local perspective constraints.

With $\tau=\lambda^{-1}$, replace (A11) by

$$
d=\tau+4\rho.
 \tag{A14}
$$

The exact factor is $d$, and the positive-error factor is $d+\eta$.
Formula (A12) has $1+2\rho$ replaced by $\tau+2\rho\ge d/2$.
The same $\gamma=\min\{\eta,1\}/64$ works uniformly in $\lambda$.
The rank exponent in (A1) is unchanged; oracle accuracy, work and
workspace are paid. Rank-one exact optimization is not claimed when
the available oracle is approximate.

## 11. Public comparison and limits

The named public Bamas--Lindermayr--Megow--Rohwedder--Schloeter
Theorem 4 gives polynomial $8+\varepsilon$ for general resource
matroids/polymatroids and $4+\varepsilon$ for two values; see
[arXiv:2307.08453v1](https://arxiv.org/abs/2307.08453v1).
Those polynomial times and the two-value special case must be retained
in comparisons. This construction changes the approximation/time
tradeoff and has a rank-dependent search bound. Same-model
primary-source comparisons are being audited before any priority claim.

The recipient objects proved here are matroids: one service is one
ground-set element. Integer polymatroids permit repeated units to
a player and require another availability and numerical-reservation
argument. They are not included silently.

Finally, the sharper compact-relaxation coefficient in the preceding
explicit-subset manuscript does not transfer automatically. It used
a shared resource between every center and blocker. Conservative
completion gives up that fact and uses the coarse inequality (A9).
That inequality is sufficient for the stated arbitrary-size factors
and for their general quasipolynomial branch.

