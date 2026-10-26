# Player-local downward-closed allocation constraints

**25 October 2026. New exact-oracle extension; independent resource-side
audit completed.** See [item-matroid-allocation-public-scope-audit.md](item-matroid-allocation-public-scope-audit.md).

This note extends the audited current-blocker method to constraints on
each player's own bundle. The resource values remain common intrinsic
values. It does not extend the result to arbitrary player-specific
values or automatically to an arbitrary matroid constraining the
receiving players of each resource.

The algorithmic imports are
[matroid-allocation-current-blocker-quasipolynomial.md](matroid-allocation-current-blocker-quasipolynomial.md),
[matroid-allocation-sharp-star-rank-quality.md](matroid-allocation-sharp-star-rank-quality.md), and
[item matroid union proof](../../problems/item-matroid-union/proof.md). Their operations are kept;
the available-bundle search and its fractional certificate are changed
as specified below.

## 1. Model and the required oracle

There is a player matroid $M$ of rank $r$ on a set $P$ of
$q$ players, a finite explicit resource set $E$, and common
nonnegative intrinsic values $v_e$. Write $u=\max_e v_e$,
with $u=0$ when the resource set is empty.
Player $p$ may receive any bundle in a nonempty downward-closed
family $\mathcal F_p\subseteq2^E$. Resources are still indivisible
and may be allocated to at most one selected player. The selected
players must form a basis of $M$.

Rank zero is the trivial empty allocation. All formulas containing
$1/r$ below assume $r\ge1$.

For a currently available resource set $A\subseteq E$, assume
access to an oracle returning a bundle

$$
\mathcal O_p(A)\in\arg\max\{v(C): C\subseteq A,
                                      C\in\mathcal F_p\}.
 \tag{D1}
$$

Only the fixed common intrinsic objective and available-set
restrictions are needed. The theorem counts these oracle calls and
does not assume that an arbitrary downward-closed family has a
polynomial-time implementation of (D1).

The main explicit specialization is a separate item matroid $N_p$
for each player, with $\mathcal F_p=\mathcal I(N_p)$. Restricting
that matroid to $A$ and running weighted greedy implements (D1)
using $O(|E|)$ independence queries. Different players may have
different item matroids. Loops encode unacceptable resources.

## 2. The perspective relaxation

Use the following relaxation, denoted $L(T)$:

$$
\begin{split}
 &x\in P_{\mathcal B(M)},\\
 &y_p\in x_p\operatorname{conv}
          \{\mathbf1_C:C\in\mathcal F_p\}\quad(p\in P),\\
 &\sum_p y_{pe}\le1\quad(e\in E),\\
 &\sum_e v_e y_{pe}\ge T x_p\quad(p\in P).
 \end{split}
 \tag{D2}
$$

At $x_p=0$, the second line means $y_p=0$. The matroid
specialization uses a scaled matroid independence polytope. It implies
the individual bounds $0\le y_{pe}\le x_p$, but retains the
additional constraints needed for player-local bundle feasibility.

No feasible point of (D2) is needed as an input to the algorithm.

## 3. Candidate construction and maximality

The current matching, selected layers, blockers and player eligibility
are exactly as in the audited current-blocker algorithm. To search a
last layer with forbidden physical resource set $F$, run (D1) on
$E\setminus F$ for each eligible player.

If an oracle returns value at least $B$, remove resources while
the remaining value stays at least $B$. Every deletion preserves
membership in $\mathcal F_p$. A single deletion scan suffices,
because the remaining value only decreases. The resulting bundle is
inclusion-minimal above $B$ and is a legal bundle for this player.
If no eligible player succeeds, maximality means exactly

$$
\max\{v(C):C\subseteq E\setminus F,
                  C\in\mathcal F_p\}<B
                     \quad(p\text{ eligible}).
 \tag{D3}
$$

All matching and selected bundles remain individually feasible for
their owners. Repeated selected player names are permitted, just as
before; these are candidate alternatives, not simultaneous allocations
to one player.

## 4. The strict fractional outside-value bound

Fix a feasible point of (D2) and an eligible player with $x_p>0$.
Express $y_p/x_p$ as a convex combination of indicators of
feasible bundles. Intersect each bundle with $E\setminus F$.
By downward closure the intersection remains feasible for $p$.
Thus (D3) implies

$$
\sum_{e\notin F}v_e y_{pe}<Bx_p.
 \tag{D4}
$$

Assume $B\le T$, as in all guarantees below. The eligible
player mass is at least
$w=r-|I\setminus\operatorname{owners}(Y_{<i})|>0$.
Summing (D4), using the target constraints and physical resource
capacities, gives the same strict lower bound

$$
v(F)>(T-B)w.
 \tag{D5}
$$

Consequently an independent $J_0$, a physical resource set $F$,
oracle-verified inequalities (D3) outside $\operatorname{cl}(J_0)$,
and

$$
v(F)\le(T-B)(r-|J_0|)
 \tag{D6}
$$

certify infeasibility of (D2). Verification of the available-bundle
claims is relative to the stated exact oracle. For an item matroid,
weighted greedy supplies an explicit polynomial verification.

## 5. All exchange and star arguments survive

The earliest-circuit exchange only uses the player matroid $M$,
current physical disjointness and the feasibility of the one candidate
being inserted. The latter now follows from (D1) and downward closure.
It introduces no new blocker of a retained selected bundle, because
the candidate still avoids the same forbidden physical resource set.
The earlier player eligibility flats and lower forbidden sets remain
literally unchanged. Last-layer-only refresh and old-free-center
cascades therefore apply without modification.

Minimality supplies the same star estimates. Deleting a resource is
always legal, so a selected bundle has value below $B+u$, and a
blocker's value outside its unique selected center is below $B$.
The sharper singleton/non-singleton argument also remains valid:

$$
v(F)\le C(B,u)|Y|,
 \qquad C(B,u)=\max\{u,2B+\min(u,B)\}.
 \tag{D7}
$$

A singleton center with value at least $B$ has an identical
singleton matching blocker. The common intrinsic value is essential
here: the same physical resource has the same value in both bundles.
With unrelated player-specific values the resource-union and star
equalities used by this proof need not hold.

Therefore every guarantee in the sharp rank-quality note holds with
$Q(T)$ replaced by (D2). In particular

$$
B+\frac{r-1}{r}C(B,u)\le T
 \tag{D8}
$$

is sufficient for the exact rank-exponential algorithm. Positive
slack gives the same rank-quasipolynomial alternative.

## 6. Work and identity accounting

An available-bundle scan uses at most $q$ calls to (D1), in
addition to the player-matroid independence queries. Returned bundles
are explicit subsets of $E$, and pruning needs only a linear
value scan. Resource-owner tables, current blockers, selected-owner
pointers, phase resets and the finite integer signature are unchanged.

All ordinary work per charged microstate is polynomial in
$q,|E|,r$ and the rational input bit length. At most polynomially
many maximum-bundle oracle calls are used per state. The count of
charged states is

$$
\min\!\left\{2^{O(r)},
       (r+1)^{O(\varepsilon^{-1}\log(r+1))}\right\}
 \tag{D9}
$$

for positive slack, and $2^{O(r)}$ on the exact boundary. This
is a polynomial full-input multiplier, not an assertion that querying
$q$ unrelated item-matroid oracles is free or linear in a smaller
implicit description. The allocation wrapper uses polynomial space,
in addition to the workspace of its supplied or implemented oracles.

## 7. Arbitrary item sizes via the same matroid-union wrapper

Classify resources of value at least $\theta T$ as fat. Keep the
bipartite player-fat edge $(p,e)$ only if
$\{e\}\in\mathcal F_p$. This singleton condition follows
automatically from any feasible bundle containing $e$, but must
be enforced when constructing the fat transversal matroid $N$.
It can be tested by (D1) on $\{e\}$, or by an item-matroid
singleton query. Let $U=M^*\vee N$.

The forward optimum promise is unchanged: each fat-supplied optimum
player can keep one permitted fat singleton, and all other surviving
players keep their feasible all-small bundles. Complementing an
extended $U$-basis gives a feasible all-small allocation for a
$U^*$-basis. The derived rank is at most $r$.

The reverse construction returns either a small bundle in
$\mathcal F_p$ or a permitted fat singleton. Extending the dual
part may discard some supplied players. Downward closure and deleting
whole allocations preserve validity for every retained player.

With $\theta=1/(4-3/r)$, the special-case inner proof from the
fat-resource note uses only (D5), the star estimate and
$u<\theta T$. It therefore gives an exact factor
$4-3/r$ in rank-exponential time and factor
$4-3/r+\eta$ in rank-quasipolynomial time with the same dependence
on $\eta$. The target-grid binary search and all union/dual
oracle costs are paid as in that note. This is a guarantee relative
to integer optimum with arbitrary item sizes.

### 7.1 Configuration-LP comparison

The stronger comparator also extends. Let a configuration LP use
variables $z_{pC}$ for $C\in\mathcal F_p$ with
$v(C)\ge T$, physical item capacities, and player masses
$x_p=\sum_Cz_{pC}$ in the base polytope of $M$.
Choose one fat item from each fat-containing configuration. Their
fractional mass $f$ belongs to the valid-fat transversal matroid
polytope. The vector $1-x+f\le1$ belongs to the union polytope
and can be increased to a union-base vector. Complementing gives a
derived base vector $x'\le h=x-f$.

The marginals of all-small configurations, divided by $h_p$ when
positive, are a convex combination of feasible small bundles for
$p$. Multiplying those marginals by $x'_p/h_p$ preserves
physical capacities and gives exactly a point of (D2) for $U^*$.
When $h_p=0$, also $x'_p=0$, and the new marginal is zero.
Thus the fat wrapper can be compared to this configuration LP as
well, without receiving a feasible LP solution as input.

This does not extend the wrapper to an arbitrary feasible point of
the original unrestricted-size perspective relaxation (D2); the
configuration split uses configurations individually worth at least
$T$.

## 8. A concrete resource-side consequence: explicit transversal resources

Suppose resource $j$ has intrinsic value $v_j$ and may be
assigned once to each of a set of players independent in a resource-
specific transversal matroid $R_j$. Assume that $R_j$ is
given by an explicit bipartite representation: a slot set $L_j$
and edges from players to permitted slots. Different resources have
disjoint slot sets.

Replace every slot $s\in L_j$ by a physical item of value
$v_j$. For player $p$, allow only adjacent slots and impose
the partition-matroid condition

$$
|C\cap L_j|\le1\quad\text{for every }j.
 \tag{D10}
$$

This is an item matroid of the type already covered above. Any slot
allocation produces, for each $j$, a matching between its
receiving players and distinct slots, so the receiving set is
independent in $R_j$. Conversely every independent receiving set
has such a matching and hence an equivalent slot allocation. Values
are preserved exactly. The per-player condition (D10) is necessary:
omitting it would allow a player to count the same service repeatedly.

For the ordinary resource-matroid Santa Claus model, all players must
be supplied, so take the player-selection matroid to be free. If the
model requires each resource to be assigned to a full basis rather
than an independent receiving set, extend its receiving set to a basis
afterwards. All values are nonnegative and resource constraints are
independent across resources, so this only increases player values.

The result is a factor approaching four in quasipolynomial time for
arbitrary intrinsic values in this explicitly represented transversal-
resource subclass. Binary uniform capacities and partition-resource
matroids are special cases; the separate compressed-capacity note
avoids expansion when the ordinary copy multiplicities are very large.

For comparison, Bamas--Lindermayr--Megow--Rohwedder--Schl\"oter,
*Santa Claus meets Makespan and Matroids*, arXiv:2307.08453v1,
Theorem 4, states polynomial-time $8+\varepsilon$ for arbitrary
resource matroids/polymatroids and $4+\varepsilon$ for two values:
<https://arxiv.org/abs/2307.08453>.
The same-model comparison is recorded in
[item-matroid-allocation-public-scope-audit.md](item-matroid-allocation-public-scope-audit.md). In particular, the
all-player quasipolynomial factor approaching four also follows by
extending the public Polacek--Svensson algorithm
([arXiv:1205.1373v2](https://arxiv.org/abs/1205.1373v2)) to
downward-closed local families with the same available-set oracle.
Consequently the all-player slot consequence above is not an exclusive
improvement of the present method. The additional scope established
here is arbitrary player-selection matroids and the stated rank-only
search bound. No priority claim or improvement for arbitrary resource
matroids is inferred merely from this reduction.

## 9. The boundary of the extension

The local item-matroid constraints here act on one player's bundle.
General resource-matroid constraints act on the set of players receiving
one resource. These are different directions of coupling. Explicit
transversal slots convert the latter into physical item ownership plus
local partition constraints, but an arbitrary resource-matroid oracle
does not supply such slots.

In particular, a resource fundamental circuit is not an automatically
unique physical blocker. Its chosen exchanges may interact across
pending candidates and may create dependencies at a resource that was
previously free for a retained candidate. Extending the result to that
model requires an additional resource-span or reservation invariant,
not just the player-matroid earliest-span argument already proved here.
