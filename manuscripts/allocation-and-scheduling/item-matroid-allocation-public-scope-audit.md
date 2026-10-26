# Player-local item constraints: independent audit and public comparison

**25 October 2026. Scope audit.** The player-local extension in
[player-local-downward-closed-allocation-extension.md](player-local-downward-closed-allocation-extension.md) passes the
mathematical checks below. Its ordinary, all-players version must be
compared with an elementary extension of the public
Polacek--Svensson algorithm. In particular, a quasipolynomial
$(4+\varepsilon)$ guarantee for heterogeneous item matroids with
common item weights is already a **derived-public baseline**. It is not
an exclusive consequence of the current-blocker construction.

The meaningful additional scope of the new construction is the
combination of an arbitrary player-selection matroid, player-local
bundle constraints, and a running-time exponent depending on the
selection rank. This note does not claim a complete classification of
all published algorithms or a first constant approximation for every
special case.

## 1. The model being compared

Let $P$ be the players, $E$ the physical items, and $v_e\ge0$
common intrinsic item values. Player $p$ has a downward-closed family
$\mathcal F_p\subseteq2^E$. Its value for an available set is

$$
f_p(A)=\max\{v(C):C\subseteq A,\ C\in\mathcal F_p\}.
 \tag{1}
$$

The oracle returns an attaining feasible subset, not merely an upper
bound on (1). For an item matroid $N_p$, weighted greedy on its
restriction to $A$ supplies this oracle. Different players may have
different item matroids. All running times count these oracle calls
and their implementation cost.

There are two distinct selection contracts:

* **Compulsory players:** every player receives a disjoint feasible
  bundle. This is the setting of the public algorithm used in Section 3.
* **Matroid selection:** the supplied players form a basis of an
  arbitrary player matroid $M$, of rank $r$, on all $q=|P|$
  candidate players. Here $r$ can be much smaller than $q$.

The common values in (1) are essential. Arbitrary player-specific
weights are outside this audit, even if each player's valuation
separately is a weighted matroid-rank valuation.

## 2. Audit of the new player-local extension

The operative manuscript is
[player-local-downward-closed-allocation-extension.md](player-local-downward-closed-allocation-extension.md). Its imported
player-matroid exchange invariant and signature analysis were audited
separately; the additional interfaces in that manuscript check out as
follows.

**Available-bundle search.** For a forbidden physical item set $F$,
an exact call to (1) on $E\setminus F$ decides whether a feasible
bundle of value at least $B$ exists. Deleting items while keeping
value at least $B$ returns a minimal feasible bundle. Downward
closure justifies every deletion; no item-matroid exchange is being
silently substituted for physical disjointness.

**The necessary fractional relaxation.** The correct local constraint
is the perspective condition

$$
y_p\in x_p\mathrm{conv}
             \{\mathbf1_C:C\in\mathcal F_p\},
 \tag{2}
$$

in addition to player-base constraints, physical capacities and
$v\cdot y_p\ge Tx_p$. Individual bounds $y_{pe}\le x_p$
alone are insufficient for arbitrary $\mathcal F_p$.
If every eligible player has $f_p(E\setminus F)<B$, intersecting
each feasible bundle in a convex decomposition of (2) with
$E\setminus F$ gives

$$
\sum_{e\notin F}v_e y_{pe}<Bx_p\qquad(x_p>0).
 \tag{3}
$$

Thus the original strict cover lower bound and infeasibility
certificate remain valid. The implementation need not receive or
compute that fractional solution.

**Star bounds.** Every proper subset of a minimal $B$-bundle is
feasible and has value below $B$. Consequently the outside part of
a blocker meeting its center has value below $B$. If a center is
a singleton $\{e\}$ with $v_e\ge B$, a minimal blocker
containing $e$ is the identical singleton, including when the two
owners have different feasible families. The sharp charge

$$
C(B,u)=\max\{u,\,2B+\min(u,B)\}
 \tag{4}
$$

therefore survives. A resource fundamental circuit is never used in
this argument: blockers are allocations sharing an actual item.

**Fat reduction.** The fat player--item graph must retain an edge
$(p,e)$ only when $\{e\}\in\mathcal F_p$. Any feasible
bundle containing a fat item contains such a feasible singleton by
downward closure. The forward and reverse player-matroid-union
reductions then preserve local feasibility. In the configuration-LP
comparison, all-small marginals lie in
$h_p\mathrm{conv}(\mathcal F_p)$, where $h_p$ is the
mass of small configurations. Scaling by $x'_p/h_p$, with the
zero convention when $h_p=0$, proves the new perspective
constraint. This does not assert a reduction from an arbitrary
unrestricted-size point of (2).

**Input and boundary costs.** A scan of all $q$ players and their
unrelated item oracles is charged. Explicit returned bundles and
physical-owner records have polynomial size. Rank zero uses the
trivial empty-basis convention and is excluded from formulas containing
$4-3/r$. Rank one is covered by the separate exact case of the
imported theorem.

## 3. A public quasipolynomial four-approximation extends to this model

### 3.1 Primary source and the precise derived statement

The source is L. Polacek and O. Svensson, *Quasi-Polynomial Local Search
for Restricted Max-Min Fair Allocation*,
[arXiv:1205.1373v2](https://arxiv.org/abs/1205.1373v2), revised
17 January 2014. The complete source used here is its 14-page v2:
[PDF](https://arxiv.org/pdf/1205.1373v2). The relevant portions are
Section 3.1 and Algorithm 1, Section 3.3 and Lemma 1, and the full proof
of Lemma 2 on pages 11--13. Section 5 acknowledges corrections to an
earlier algorithm description and signature. The corrected v2
fat/thin signature is the one used here.

**Derived-public proposition.** For compulsory players with the
families and oracle (1), common nonnegative rational item values, and
$0<\varepsilon\le1$, the public algorithm with the oracle
replacement below either finds feasible disjoint bundles of value
$T/(4+\varepsilon)$ for every player, or correctly certifies that
the corresponding feasible-configuration LP at target $T$ is
infeasible. Its work is

$$
\mathrm{poly}(|P|,|E|,\text{bit length},
                     \text{oracle cost})\,
 (|P|+1)^{O(\varepsilon^{-1}\log(|P|+1))}.
 \tag{5}
$$

This proposition is an explicitly reconstructed extension of the
public proof, not a verbatim claim in its theorem statement.

### 3.2 Feasible minimal hyperedges and exact addable-edge search

Set $\alpha=4+\varepsilon$ and $B=T/\alpha$. For each
player, the conceptual hyperedges are its inclusion-minimal feasible
bundles of value at least $B$. The algorithm never enumerates them.
A resource of value at least $B$ is fat. A minimal feasible bundle
containing a fat resource is a singleton; every other hyperedge is
thin. These assertions follow from common values and downward closure.

The source's alternating tree, physical addable-edge definition and
blocker definition need no change. Addable bundles avoid the resources
of the current adding and blocking edges and have a player already in
the tree. Test fat singletons first at the corresponding distance.
For thin candidates, evaluate (1) on the available nonfat resources
and trim an attaining bundle to minimality if it reaches $B$.
Among the resulting candidates choose one with minimum distance in
the source's zero-fat, unit-thin distance convention. Scanning the
currently eligible players is polynomial. Thus this implements the
literal shortest-addable-edge selection rather than substituting an
arbitrary greedy edge.

The exchange/collapse procedure is purely a procedure on this
hypergraph. Every allocation it inserts is individually feasible for
its owner. It never needs a union of two feasible bundles to remain
feasible.

### 3.3 The configuration-LP dual argument still applies

Use configurations $C\in\mathcal F_p$ with $v(C)\ge T$.
The source's truncated alternating tree, minimum-distance invariant
and dual variables are unchanged. A reached player has dual value
$(\alpha-1)/\alpha$. Reached fat resources have that same
dual value; the relevant reached thin resources have dual value
$v_e/T$.

Let $F$ be the support of those resource dual variables and take
a feasible target configuration $C$ of a reached player. If it
contains a positively charged fat resource, its dual constraint is
immediate. Otherwise, suppose its total charged thin value were below
$(\alpha-1)T/\alpha$. Then

$$
v(C\setminus F)>T/\alpha=B,
 \qquad C\setminus F\in\mathcal F_p.
 \tag{6}
$$

The second statement is exactly the additional step needed for a
player-local family. Trimming (6) gives an addable hyperedge in the
truncated tree, contradicting the assumed absence of such an edge.
Hence all dual constraints hold.

The dual objective estimate also survives. A thin center has value
below $2B$. Its matching blocker, after removing its intersection
with that center, has value below $B$, since this is a proper
feasible subset of the blocker. Each stable center has at least one
blocker, and the blockers belong to distinct players. Thus the
source's thin-resource charge is at most three times $B$ times
the number of thin blockers. Fat charges cancel against reached fat
players just as in the source. No unrestricted-subset assumption is
used elsewhere in this calculation.

Consequently the literal Lemma 2 inequality is retained:

$$
\frac{\alpha-4}{3}
       \sum_{i=1}^{D}|B_{2i}^{\rm thin}|
       <|B_{2D+2}^{\rm thin}|
 \tag{7}
$$

whenever there is no addable edge in the specified distance range and
the target LP is feasible. This gives depth
$O(\varepsilon^{-1}\log(|P|+1))$.

### 3.4 Termination, certification and the target search

The v2 signature separates the fat and thin center/blocker counts.
Its strict decrease after each source operation is a hypergraph
statement, so it does not depend on the particular local families.
Its coordinates are bounded by the number of players. This proves
(5) with the polynomial oracle implementation above.

When the bounded search fails, the same dual assignment proves
configuration-LP infeasibility. Rational finite precision and a search
over the target grid give a guarantee relative to the optimum of that
configuration LP. The feasibility of this LP is monotone in $T$,
and the algorithm need not solve it. As usual, a successful run above
the LP optimum does not invalidate the one-sided search guarantee.

### 3.5 Consequences that must be attributed to the public pipeline

For each player-specific item matroid, weighted greedy implements (1),
so (5) applies even when the matroids differ arbitrarily. More
generally it applies to any local downward-closed families for which
the required exact available-weight oracle is efficient.

The explicit-transversal-resource construction in Section 8 of the
new extension note replaces a resource by its explicit slots and
imposes a per-player partition constraint of at most one slot from
each original resource. This is a special case of (1). Therefore its
**all-player quasipolynomial $4+\varepsilon$ consequence also has
the derived-public proof above**. Neither that consequence nor the
local item-matroid oracle substitution is, by itself, evidence of a
new general constant approximation.

What this source does not supply is a replacement of its number of
compulsory players by the rank of an arbitrary player-selection
matroid on a much larger set of candidate players. Such a replacement
requires an exchange and retained-layer invariant beyond Algorithm 1.

## 4. Later public results and the exact model boundaries

The following primary sources were checked through their latest
available arXiv record or official proceedings version on 25 October
2026. These entries describe named comparison pipelines, not a claim
that all possible reanalyses have been exhausted.

| Source | Scope and guarantee relevant here | Why it is not the same general selection-rank theorem |
|---|---|---|
| Polacek--Svensson, v2; Section 3 above | Deterministic quasipolynomial $4+\varepsilon$, including the derived heterogeneous local-family extension | All players are compulsory; the signature uses their number |
| Davies--Rothvoss--Zhang v4 plus the local-oracle and fat-union adapters in Section 5 | Named derived-public polynomial $6+\eta$ for general player selection and local feasible families | It imports the published player-side exchange machinery; it does not give the new rank-only four-approximation tradeoff |
| Bamas--Garg--Rohwedder, ICALP 2021 | Polynomial $O(\log\log |E|)$ for $f_p(S)=f(S\cap\Gamma_p)$ with one common monotone submodular $f$ | Different arbitrary item matroids generally are not restrictions of one common function; all players are compulsory |
| Bamas--Morell--Rohwedder, SODA 2025 | General heterogeneous submodular valuations: polylogarithmic approximation in quasipolynomial time, and polynomial time for any fixed-power approximation | Covers weighted matroid-rank valuations as valuation functions, but gives a weaker general ratio and does not select a player-matroid basis |
| Chekuri--Kulkarni--Mehta--Vondrak, APPROX 2026 | Randomized polynomial additive guarantee $(1-1/e-\varepsilon)\mathrm{OPT}-\mathrm{Max}$, and a multiplicative $1-1/e-\varepsilon$ guarantee for a fixed total number of players | The additive loss matters for unrestricted item sizes; a fixed number of all players is not rank-only dependence when $q\gg r$ |
| Bamas--Lindermayr--Megow--Rohwedder--Schloeter, SODA 2024, Theorem 4 | Polynomial $8+\varepsilon$ for general resource matroids/polymatroids, $4+\varepsilon$ for two values | Constraints act on recipients of one resource, not on the items in one player's bundle; explicit transversal resources admit the separate slot reduction above |
| Boehmer, SWAT 2026 | Identical valuations, and a separate configuration-gap/estimation result when the same item-matroid constraints are imposed on all players | Does not state the heterogeneous local-family plus arbitrary player-selection contract |

Primary links:

1. Bamas--Garg--Rohwedder,
   [arXiv:2011.06939v1](https://arxiv.org/abs/2011.06939v1).
2. Bamas--Morell--Rohwedder,
   [arXiv:2407.04824v1](https://arxiv.org/abs/2407.04824v1),
   [full text](https://arxiv.org/html/2407.04824v1), Theorem 1.
3. Chekuri--Kulkarni--Mehta--Vondrak,
   [arXiv:2511.21099v1](https://arxiv.org/abs/2511.21099v1),
   [full text](https://arxiv.org/html/2511.21099v1), Theorems 4 and 5;
   [official APPROX 2026 record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2026.21).
4. Bamas--Lindermayr--Megow--Rohwedder--Schloeter,
   [arXiv:2307.08453v1](https://arxiv.org/abs/2307.08453v1),
   Theorem 4 and Section 5.
5. Boehmer,
   [official SWAT 2026 full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol370-swat2026/html/LIPIcs.SWAT.2026.8/LIPIcs.SWAT.2026.8.html),
   Theorem 1.5 and Section 4.3;
   [arXiv:2604.12417](https://arxiv.org/abs/2604.12417).

Unweighted matroid-rank allocation, agent-entitlement weights and Nash
social welfare are different comparison problems. A theorem for any
one of them does not establish a weighted max-min allocation guarantee
in the present model.

## 5. A named public six-approximation pipeline for general selection

The current public version is
[arXiv:1807.07189v4](https://arxiv.org/html/1807.07189v4).
Its displayed player-matroid theorem and the historical one-third
coefficient are recorded in
[matroid-allocation-public-comparison-and-version-audit.md](matroid-allocation-public-comparison-and-version-audit.md).
The following adapter was checked directly against Claim 7 and
Lemmas 8--10 of the v4 full text.

### 5.1 The exact resource-oracle substitution

Restrict its conceptual minimal $\alpha T$-edges and
$\beta T$-edges to the player's feasible family. Implement the
greedy expansion by the exact available-weight oracle, retaining the
source's joint player-matroid independence test.

In the proof of Lemma 8, let $W''$ denote the current forbidden
resources, including those of the freshly selected expansion edges.
Its one use of unrestricted additive neighborhoods is the implication
from greedy maximality to
$v(N(p)\setminus W'')<\alpha T$. Replace that statement by

$$
\max\{v(C): C\in\mathcal F_p,
                   C\cap W''=\varnothing\}<\alpha T.
 \tag{8}
$$

By (2) and downward closure, (8) implies
$\sum_{e\notin W''}v_e y_{pe}<\alpha T x_p$.
The same target-value and resource-capacity inequalities therefore
give the same cover lower bound and the same expansion coefficient
$\mu$. The player-side Strong Swapping Lemma is unchanged.

Claim 7 and Lemmas 9--10 use the value of the available part of an
already selected edge. Such a part is a feasible subset of that edge.
Consequently it contains a feasible minimal $\beta T$-bundle
exactly when its value reaches $\beta T$. Their minimal-edge
upper bounds, overlap charges and current-blocker counts are preserved
without a second approximation factor. The later signature and
layer-size calculations introduce no additional resource-family
operation. Thus the resource-side proof is a literal adapter of the
public one; the required new fractional premise is (2).

### 5.2 What public algorithmic machinery is imported

For a fair named-pipeline comparison, import the published DRZ v4
player-side exchange and termination guarantee and apply the resource
adapter above. This gives its displayed fifth-type value

$$
\left(\frac15-\varepsilon\right)T-\frac u5
 \tag{9}
$$

for the perspective relaxation, with polynomial work for fixed
$\varepsilon$ and polynomial exact local oracles. The fat wrapper
only needs the source's safe small-item range $u/T<1/6$; no
extrapolation of its printed parameter positivity outside that range
is needed here.

This source-level comparison does not purport to repair the literal
pseudocode's retained-layer repeated-owner contract. That separate
question is documented in
[public-matroid-repeated-owner-interface-gap.md](../mechanism-boundaries/public-matroid-repeated-owner-interface-gap.md). The precise scope is:
the resource adapter is verified here, and the published player-side
algorithm is an explicitly named import. A fully independent
reimplementation of all allowed pseudocode choices, or the stronger
square-curve reparameterization considered in that other note, remains
subject to its exchange-interface audit. Neither issue is concealed
by the oracle substitution.

### 5.3 Fat union and the resulting public ratio

For desired fixed $\eta>0$, set
$\theta=1/(6+\eta)$. Run the feasible-singleton fat graph and
player-matroid-union wrapper on items of value at least $\theta T$.
All remaining items satisfy $u/T<\theta<1/6$. Taking

$$
0<\varepsilon\le
             \frac{1-6\theta}{5}
             =\frac{\eta}{5(6+\eta)}
 \tag{10}
$$

in (9) gives at least $\theta T$ to every selected small-side
player. Fat-side players receive that value from a legal singleton.
The union and configuration-LP arguments are exactly those in
[configuration-comparator.md](../../problems/item-matroid-union/configuration-comparator.md), now using (2).

Accordingly **polynomial $6+\eta$ for arbitrary player selection
and efficient exact player-local families is a named derived-public
baseline**, with the imported player-side dependency just stated.
The new rank-parameterized four-type result is a stronger ratio with a
different time tradeoff and an independently proved retained-layer
invariant. The mere existence of a constant approximation in this
expanded model is not claimed as new.

## 6. Knapsack families also have direct public comparison pipelines

The oracle metatheorem in
[approximate-available-bundle-oracle-allocation.md](approximate-available-bundle-oracle-allocation.md) includes a
self-contained knapsack FPTAS implementation. Its independent audit is
[Approximate available-bundle oracles in current-blocker allocation](approximate-available-bundle-oracle-allocation.md).
The following comparison prevents interpreting that application as
the first constant approximation for player-local budgets.

### 6.1 Fixed common rounding, followed by exact available optimization

Fix a positive target $T$, let $m=|E|>0$, and choose
$0<\kappa<1$. Define the same new intrinsic value for an item
at every player by

$$
\widehat v_e=K\left\lfloor\frac{\min\{v_e,T\}}K\right\rfloor,
                  \qquad K=\kappa T/m.
 \tag{11}
$$

Every originally feasible configuration of value at least $T$
has capped value at least $T$: if it contains an item of value
at least $T$, that item alone contributes $T$ after
capping; otherwise its value is unchanged. Rounding then loses less
than $mK$. Consequently the same configuration has
$\widehat v$-value at least $(1-\kappa)T$. Its player-local
budget feasibility is unaffected.

For player-dependent knapsack costs and budgets, a dynamic program
can optimize $\widehat v$ exactly over every available set:
each integer profit is at most $m/\kappa$, and the total
integer profit range is $O(m^2/\kappa)$. Store the minimum
true cost for each attainable profit. This is polynomial in the
explicit input and $1/\kappa$, even when costs and budgets have
large binary magnitudes. All arithmetic uses the given rational costs
and the common rounded profits.

If the original configuration LP is feasible at $T$, the same
configuration variables are feasible for the rounded instance at
$(1-\kappa)T$. A rounded allocation also has at least its
rounded value under the original utilities. Thus exact-oracle public
algorithms apply with a controlled ratio loss.

### 6.2 The resulting named public bounds

For compulsory players, use Section 3 with
$\varepsilon=\eta/2$ and
$\kappa=\eta/[2(4+\eta)]$, for $0<\eta\le1$. Then

$$
\frac{4+\varepsilon}{1-\kappa}=4+\eta.
$$

This gives a deterministic quasipolynomial $4+\eta$
player-local knapsack allocation guarantee by a direct public
Polacek--Svensson pipeline. Its minimum-distance hyperedge search is
implemented exactly for the fixed rounded utilities.

For arbitrary player selection, use the named derived-public
$6+\eta/2$ pipeline of Section 5 with
$\kappa=\eta/[2(6+\eta)]$. The same calculation gives
$6+\eta$ in polynomial time for fixed $\eta$, with the
same explicitly named published player-side dependency. The comparator
is the original player-matroid configuration LP. The target search
need not assume success is monotone: feasibility at $T$ guarantees
success of the rounded run, while success directly certifies its
original-value allocation.

These are ratio/time comparisons, not global priority claims. The
new construction additionally supplies its rank-parameterized time,
finite-rank quality and fully stated retained-layer proof.

### 6.3 A distinction for arbitrary approximate-oracle black boxes

An approximate available oracle for one fixed objective need not
support exact optimization for rounded objectives. Furthermore it need
not detect the truly closest minimal $B$-edge in the public PS
distance order. Merely changing the dual player price to account for
an oracle loss does not justify that original truncation invariant.
The fixed-rounding knapsack argument supplies a genuine exact oracle,
so it does not have this gap. A general loss-$\lambda$ PS adapter
would need an additional prefix-search or distance-selection argument
and is not counted as established here.

