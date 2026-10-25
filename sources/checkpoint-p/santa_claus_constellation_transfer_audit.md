# Santa Claus: public baselines and the constellation transfer boundary

**Primary-source audit, 25 October 2026.** This note does not claim an
algorithm with approximation factor below four for general restricted
Santa Claus. It records the usable local inequalities, a concrete
obstruction to applying the independent-transversal certificate as a
black box, and the separate matroid-allocation direction.

## 1. Current public comparison

Here a factor `a` means an allocation of value at least the reference
optimum divided by `a`. An integrality-gap bound or an efficient estimate
of the optimum is not an algorithm producing that allocation.

| Primary source | Scope and displayed result | Relevant limitation |
|---|---|---|
| [Jansen--Rohwedder, arXiv:1807.03626v1](https://arxiv.org/abs/1807.03626v1), Theorem 3 / Claim 2 | Restricted Santa Claus configuration-LP gap at most `23/6` | Their local-search iteration bound is exponential in the number of matched players. |
| [Cheng--Mao, arXiv:1905.06084v1](https://arxiv.org/abs/1905.06084v1), Theorems 1--2 and Appendix C | Polynomial-time `4+delta` allocation; separately, configuration-LP gap `99/26` | The smaller constant is not accompanied by polynomial or quasipolynomial running time. |
| [Cheng--Mao, Algorithmica 84 (2022), 1835--1874](https://doi.org/10.1007/s00453-022-00942-y) | The journal abstract retains both results above | Detailed lemma numbers below refer to the accessible full 2019 manuscript, not an asserted page-for-page identity with the journal proof. |
| [Haxell--Szabo, arXiv:2202.01143v3](https://arxiv.org/html/2202.01143v3), Theorem 1.1 and Section 8 | Configuration-LP gap `53/15` | The paper explicitly does not bound the running time of its constructive procedure. Its topological connectivity criterion is not a total-domination promise. |
| [Davies--Rothvoss--Zhang, arXiv:1807.07189v4](https://arxiv.org/html/1807.07189v4), Theorems 2--3 | For the player-matroid LP `Q(T)`, integral value `(1/5-epsilon)T-u/5`, in polynomial time for fixed epsilon; restricted Santa Claus `6+epsilon` | This is the corrected version dated 4 January 2026. |
| [Bamas--Lindermayr--Megow--Rohwedder--Schloter, arXiv:2307.08453v1](https://arxiv.org/abs/2307.08453v1), Theorem 4 | Polynomial `8+epsilon` for resource-matroid Santa Claus; `4+epsilon` in its two-value case | This more general model allows a resource to serve a basis of its own matroid. It contains the DRZ setting, but the displayed theorem does not give the same `(T-u)/3` LP guarantee. |

The contemporary source check found no general restricted-Santa-Claus
allocation algorithm below four in quasipolynomial time. This is a
bounded literature audit, not a proof that no such result exists.
The known `(3+4 eta)` quasipolynomial result for the `(1,eta)` two-value
special case is not a result for arbitrary restricted valuations;
Haxell--Szabo discuss this distinction in their introduction.

### 1.1 A version correction that changes the comparison

The SODA 2020 DRZ abstract, some later papers, and Sami Davies's
[2021 University of Washington dissertation](https://digital.lib.washington.edu/researchworks/items/f2a80a99-1858-4670-9e0d-4857b24419e1)
repeat the earlier factor-four claim and its one-third matroid
coefficient. These are historical claims, not a separate recent
improvement over DRZ v4.

DRZ v4 Section 4 explains the change: an earlier blocking-growth
invariant was established at layer creation but could fail after
collapses. The corrected algorithm checks newly available resources in
old layers; its theorem has the one-fifth coefficient. We use that
corrected theorem as the named polynomial baseline, and do not infer a
separate reason for the revision. Cheng--Mao still supplies the
polynomial factor-four baseline for ordinary restricted Santa Claus.

The independently checked candidate
`matroid_allocation_current_blocker_quasipolynomial.md` is a new proof
of a quasipolynomial one-third guarantee. It should not be described as
the first appearance of the numerical coefficient one third in public
literature.

The exact largest-item term also changed historically. DRZ v1
(19 July 2018) states a one-third result with fractional resource
assignments, followed by an integral guarantee
`(1/3-epsilon)T-u`; its unit-resource theorem is separate. DRZ v2
(7 May 2019) states the integral term `-u/3`. Versions v3 and v4
state `-u/5`. A detailed version table and the precise model comparison
are in `matroid_allocation_public_comparison_and_version_audit.md`.
That note also records an algebraically promising quadratic public
parameter curve, whose historical exchange interface is still
unclosed; it is not used as an established algorithmic baseline.

## 2. The exact local part of the 23/6 proof is transferable

Let the configuration-LP target be `T`, set `B=T/(23/6)`, and let every
selected bundle be inclusion-minimal with value at least `B`.
Resources of value at least `B` are fat. Write

\[
 z(r)=\begin{cases}
 1,&v_r\ge B,\\
 \min\{1/3,(2/5)v_r/B\},&v_r<B.
 \end{cases}
\]

Only resources in the proposed certificate support receive a positive
price. The following is an elementary strengthening of the local
calculation in JR Claim 2.

**Star lemma.** For a nontrivial star of minimal bundles, with one
centre and `b>=1` pairwise resource-disjoint leaves, its resource price
is at most `b`. It is also at most `(b+1)/2`.

For a fat centre, all incident minimal bundles use that same singleton
resource. Disjoint leaves force `b=1`, giving both bounds.

For a thin centre `C`, its total price is at most `2/3`. To see this,
if it has two resources use the cap `1/3` on each. If it has `k>=3`
resources, minimality and the least resource value imply

\[
 v(C)<\frac{k}{k-1}B,
 \qquad z(C)<\frac25\frac{k}{k-1}\le\frac35.
\]

Every leaf has value less than `B` outside `C`. Thus for `b>=2`,

\[
 z(C\cup\text{leaves})<\frac23+\frac25 b
 \le\frac{b+1}{2}\le b.
\]

For one leaf, let `a` be the smallest resource value in the two
bundles. If `a<=B/2`, their union has value less than `2B+a`, hence
price at most one. If `a>B/2`, each bundle has exactly two resources,
and their intersecting union has at most three resources, again giving
price at most one. This also covers identical bundles with different
owners; it does not require three nonempty set differences.

Consequently a constellation `K` made of such stars satisfies

\[
 z(R(K))\le\#\operatorname{leaves}(K),
 \qquad z(R(K))\le |V(K)|/2.
\]

Cross-star overlap can only decrease the price of the union, so summing
the individual upper bounds is safe. These bounds use no rule choosing
the fewest blockers, and no optimization among candidate bundle values.
The public local search itself is allowed to choose an arbitrary
available minimal bundle.

The missing step in a black-box transfer is global: which players have
all their target configurations covered, and how does their number
compare with the leaves or vertices charged above?

## 3. What the 99/26 proof adds

Use `B=26T/99` and normalized resource size `t=v_r/B`. For thin
resources the CM Appendix C price, divided by `B`, is

\[
 \psi(t)=\begin{cases}
 3t/(2+t),&0<t<1/2,\\
 3t/(3-t),&1/2\le t<3/4,\\
 1,&3/4\le t<1.
 \end{cases}
\]

The precise imported local inequality is CM Claim 32:

\[
 \sum_{r\in C}\psi(v_r/B)
 \le\frac32+\frac12\psi(v_a/B)
 \quad\text{for every minimal thin bundle }C
 \text{ and every }a\in C.
\]

Splitting the price of a shared resource equally between its incident
centre and leaf shows that any such star costs at most `3/2` times its
number of vertices. This is the only local charging property needed
in CM Claim 31. It does not require a specially chosen minimal bundle.

The global mechanism in Appendix C is more specific. A maximum
matching of players to fat resources is maintained separately. A player
is eligible for a thin candidate when it is reachable by an alternating
fat path from an exposed or thin-blocking player. For the entire
reachable closure `P+` and its reachable fat resources `F+`, matching
maximality gives

\[
 |P^+|-|F^+|\ge 1+\#\{\text{thin blocking players}}.
\]

That inequality cancels the dual cost of fat resources. It is not
provided by the ordinary independent-transversal certificate.

There is also no uniform slack in the cost of a one-leaf thin star:
two intersecting minimal two-resource bundles can have a union of
three resources, each with size close to `B`; its normalized price is
exactly three. Enlarging the target ratio slightly while keeping it
below four does not remove this clipped-price equality. A proof that
merely multiplies the cardinality bound `2+epsilon` by the per-vertex
star charge therefore does not establish a below-four algorithm.

## 4. A concrete black-box obstruction, even with no extras

Fix `0<epsilon<1`, and choose an integer `W>1+2/epsilon`.
There are players `p_0,...,p_W` and resources
`r_1,...,r_W,g`, all of value `T`. Their desired sets are

\[
 L_{p_0}=\{r_1\},\qquad
 L_{p_i}=\{r_i,r_{i+1}\}\ (1\le i<W),\qquad
 L_{p_W}=\{r_W,g\}.
\]

The integral target `T` is feasible: assign `r_(i+1)` to `p_i` for
`0<=i<W`, and give `g` to `p_W`.

In the minimal-bundle allocation graph, form one star edge for each
`j=1,...,W` between the vertices

\[
 \{r_j\}^{p_{j-1}}\quad\text{and}\quad\{r_j\}^{p_j}.
\]

These `W` edges are an induced disjoint union of nontrivial stars.
Taking the second endpoint as the leaf gives a partial independent
transversal of `p_1,...,p_W`. Thus `K` is a constellation for all
`W+1` classes. Set

\[
 S=\{p_0,...,p_{W-1}\},\qquad D=V(K).
\]

Every bundle vertex in every class of `S` has its opposite-owner
singleton as a neighbour in `D`. Hence `D` totally dominates `S`.
Nevertheless,

\[
 |D|=2W<(2+\epsilon)(W-1)
       =(2+\epsilon)(|S|-1),
 \qquad D\setminus V(K)=\emptyset.
\]

This is a fully legal independent-transversal failure certificate in an
instance that already has an optimal integral allocation. It disproves
the inference that a small clean constellation certificate by itself
contradicts configuration-LP feasibility. It is not a counterexample to
the new matroid-layer algorithm: maximum fat matching solves this
example immediately.

For an actual current-blocker prefix, the same bookkeeping issue is
visible in the identities

\[
 |S|=W=1+|Y_{<i}|,
 \qquad |S_0|-1=|Y_{\le i}|=W-1+|Y_i|.
\]

Integer choices of the transversal parameters can remove free selected
vertices and candidate extras. They do not make `S=S_0` at a nonempty
current-blocker stopping layer.

## 5. The constructive matroid direction and its precise consequence

The independently checked construction works directly with DRZ's player
matroid and compact LP

\[
 x\in P_{\mathcal B(\mathcal M)},\quad
 \sum_{r\in L_p}v_r y_{pr}\ge T x_p,\quad
 \sum_p y_{pr}\le1,\quad 0\le y_{pr}\le x_p.
\]

Its guarantee is

\[
 B=(T-u)/3-\epsilon T,
 \qquad u=\max_r v_r,
\]

in input-polynomial times
`(q+1)^{O(epsilon^{-1} log(q+1))}` oracle time. Its earliest-circuit
exchange preserves the lower-layer matroid closures after a single
free-bundle swap; a fresh maximal extension then bounds the *current*
layer depth. The independent audits are recorded separately in
`matroid_allocation_current_blocker_independent_audit.md` and
`matroid_allocation_current_blocker_second_audit.md`.

This improves the numerical guarantee of the named corrected DRZ v4
theorem while allowing quasipolynomial time. It is not a polynomial
algorithm and is not a new global bound for maximum matching.

For ordinary restricted Santa Claus, separating items at `theta T`
and using the dual of the large-item matching matroid gives the value

\[
 \min\{\theta,(1-\theta)/3-\epsilon\}T.
\]

Balancing the terms gives `theta=(1-3epsilon)/4`, hence a factor
arbitrarily close to four from above. Ordinary restricted Santa Claus
already has a polynomial `4+delta` algorithm from Cheng--Mao. The new
matroid statement concerns a more general player-basis model and the
specific compact LP; this corollary must not be advertised as beating
the ordinary factor-four baseline.

## 6. Remaining avenues

Two ingredients are available without a new combinatorial selection
rule: the JR/CM star inequalities, and polynomial access to a minimal
bundle in a currently available resource set. The open below-four
bridge is a stronger stopping or exchange argument that pays the
terminal layer's extra blockers after fat cancellation. The constant
`53/15` cannot be substituted for that bridge merely because the
allocation graph is the same: its proof uses a different topological
certificate.

The separate implicit-oracle note handles the distinction between
finding a minimal available bundle and finding an arbitrary neighbour
of a specified minimal bundle. The latter can hide a subset-sum
constraint. None of the claims here assumes that enumerating all
minimal configurations or a minimum-blocking configuration is free.

