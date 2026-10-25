# Root audit of the derived public two-thirds MSF envelope

**Independent mathematical and primary-source audit, 25 October 2026.**

The public-framework construction in
`dynamic_msf_formal_pruning_substitution_audit.md` passes this root audit.
It supports a deterministic fully dynamic exact minimum spanning forest
algorithm with worst-case update envelope

\[
 \exp O(U^{2/3}h^{1/3}),\qquad
 U=\log(N+4),\quad h=\log(U+4),
\]

under the comparison-RAM assumptions of the named public reduction.
Initialization is input-linear times a fixed power of this factor.
For an explicit bit model, input-weight comparison costs must also be
paid; word-size or polynomial-logarithmic-bit weights preserve the
displayed envelope. All additional ranks and hierarchy thresholds have
polynomial-logarithmic bit length.

This is a derived public baseline. It is neither a printed theorem with
this exact exponent nor a distinct improvement obtained from the research
matching router. In particular, reaching the same exponent through the
tagged-triangle candidate would not beat this comparator.

## 1. Primary source locations actually read

The root directly read the following parts of
[NSW, arXiv:1708.03962v2](https://arxiv.org/html/1708.03962v2):

* Theorem 7.1 and its exact batch-insertion/deletion cost formula;
* Theorem 8.3, Lemma 8.8, Algorithm 8.1, and Proposition 8.11;
* Section 9.1.1, including the exclusion of the root cluster from pruning;
* Claims 9.18 and 9.19, including their contraction and publication proofs;
* Lemma 9.20, Proposition 9.13 as used in Lemma 9.27, and the full
  preprocessing/update recurrences in Lemmas 9.24 and 9.28.

The root also checked the decomposition and pruning interfaces in
[CGLNPS, arXiv:1910.08025v2](https://arxiv.org/html/1910.08025v2),
Corollary 6.1 and Section 6.2, and
[MGS, arXiv:2504.00544v1](https://arxiv.org/html/2504.00544v1),
Theorems 1.3 and 6.4. The formal companion note is the operative proof.
The earlier informal baseline sketch is not an independent justification.

## 2. The pruning contract really is weak, but the certificate is not

An initially expanding non-root large cluster needs a monotone published
set P and an existential subset W of P whose removal leaves a connected
induced graph. Neither a boundary bound on P nor an algorithm finding W
is required by the correctness proof in Section 9.2.

This does not justify using only the original MSF and edges incident to P.
The four-vertex path counterexample in the companion note invalidates
that simplified certificate. The actual NSW construction also maintains
MSFs of its three types of compressed child-cluster graphs, original
versions of reweighted edges, and retained retired edges.

The weighted hierarchical property is essential: each child-cluster MSF
is contained in its parent's MSF after every physical deletion set.
It permits Claim 9.18 to process child forests before parent-owned edges.
The residual set V(child) minus W belongs to one current child component.
Contracting all current child components is therefore a further
contraction of the intermediate graph used in that claim. Its MSF edges
are contained in the earlier MSF, by the usual contraction property.

Claim 9.19 then permits W to be replaced by a larger published P. All
additional removed parent-owned edges are explicitly included in the
certificate. The elementary inclusion

\[
 \operatorname{MSF}(X\cup D)\subseteq\operatorname{MSF}(X)\cup D
\]

is applied separately to the three compressed graphs. This is the exact
reason that conservative extra publication is allowed.

The root cluster is never supplied to the expander pruner. Its large
children are pruned, and their published sets define the root's
compressed graphs. No expansion promise on an arbitrary original input
is being introduced.

## 3. The deterministic weighted hierarchy has the needed properties

The companion construction protects connected blocks of the initial MSF,
of size between a constant times gamma and gamma. Protected edges are
never reweighted or put in a weight band. At each level, remove the
current highest remaining nonprotected band **before** decomposition.
Contract the protected blocks and apply deterministic decomposition to
the resulting actual multigraph, with crossing budget c/gamma squared.

This order is an explicit implementation choice. The displayed order in
NSW Algorithm 8.1 does not by itself prove that expansion survives a
later arbitrary band deletion. Performing the deletion first avoids
that inference while preserving all of the following properties:

1. The protected blocks remain connected and wholly contained in each
   decomposition part.
2. The child graph is an actual decomposition output after uncontracting,
   and so has the claimed conductance.
3. The current band and inter-part edges become parent-owned. Only the
   lower-band crossing edges need their weights increased.
4. These increases separate parent-owned nonprotected weights from all
   child nonprotected weights. Surviving protected initial-MSF edges
   remain safe under deletions and increases of other weights. Kruskal's
   rule therefore proves the required child-MSF inclusion under every
   deletion set.
5. At one depth, owned band edges total O(n/gamma), and crossing edges
   total O(n/gamma squared). Over O(gamma) depths only O(n/gamma) edges
   are reweighted. Each leaf still contains an entire protected block.

The contracted graph need not have bounded degree. CGLNPS's general
decomposition interface is used there, not its bounded-degree corollary.
Its edge inventory is still O(n) per depth because the uncontracted
native graph has degree three. A conductance guarantee of order
gamma to the minus three on a nontrivial contracted component implies
at least that edge expansion. NSW Lemma 8.8 loses only the square of
the protected-block size and the original constant degree. Thus the
uncontracted child conductance is at least order gamma to the minus five.
An isolated contracted vertex corresponds to one connected protected
block and satisfies this weaker bound directly.

Each static call uses its actual size. If its local size is too small
for the master r, use the local clipped r from the companion note.
Its quality can only improve, and its work remains actual size times
a fixed polynomial in gamma. Singleton cases are handled directly.
No exponentially expensive small-instance search or master-size padding
is needed.

## 4. Literal connectivity, finite horizons, and real publication

Positive conductance can leave degree-zero vertices unspecified. The
companion note therefore publishes

\[
 P=A\cup N_{C_0}(A)\cup\{\text{endpoints of deleted edges}\},
\]

where A is the modern pruner's own set. Initial degree three makes the
extra work and publication a constant factor. Every residual isolate
lies in P. After additionally removing those isolates in the existential
analysis, the positive-volume residual is connected. If it is empty,
all vertices have been published and a singleton can be left. The
algorithm need not compute the existential set.

At child conductance of order gamma to the minus five, the MGS work and
publication cost is a fixed polynomial in gamma and U. Allowing
pi = gamma to the twelfth power times a sufficiently large fixed
polynomial in U is conservative. Use a decremental period

\[
 T(n)=\left\lfloor n/(C\pi d\gamma)\right\rfloor,
 \qquad d=\Theta(\gamma).
\]

Every pruned cluster has initially at least order n/gamma edges, so
this global period ends before any local modern-pruning horizon. There
is no final bulk-publication operation. Actual-size base cases handle
the range where this period would be shorter than one update.

Across one period, total publication is at most T pi d = O(n/gamma).
All additional incident edges fit the public sketch-size accounting.
This is the finite-horizon version used for the accepted baseline; a
separate gradual-completion construction is unnecessary.

## 5. Worst-case time is a direct public recurrence

The retained-edge rule ensures that a physical deletion creates at most
two sketch deletions. Publications create O(pi d) insertions, which the
explicit public batch-insertion interface handles. They do not create
O(pi d) recursive decremental update calls.

Write k=O(n/gamma) and let b=O(pi d) be the insertion batch bound.
NSW Theorem 7.1 charges

\[
 O\left(
  {b\log k\over k}\,t_{\mathrm{pre}}(O(k))
  +b\log^2 n+{k\log k\over T(k)}
  +\log k\,t_u(O(k))
 \right).
\]

The preprocessing recurrence has an additive n times polynomial in
gamma term, and O(gamma) calls on size O(n/gamma). After normalizing by
size its branching loss is a fixed constant per level. This costs at
most an additional exp O(U/log gamma) factor. The update recurrence has
only an O(log n) recursive multiplier. It follows that

\[
 \log t_u(N)=O\left(\log\gamma+{Uh\over\log\gamma}+h\right).
\]

This is worst-case time through the named public contraction/background
rebuilding reduction. It is not an inferred deamortization of a separate
amortized candidate. Deterministic primitive substitutions remove the
random branches without changing that reduction's scheduling.

Choose r of order (U/h) to the one-third power and

\[
 \log\gamma=C(U/r+r^2h+h)
             =\Theta(U^{2/3}h^{1/3}).
\]

The static decomposition cost is actual size times a fixed polynomial
in gamma, its quality meets the stated threshold, and the recursive
term Uh/log gamma is smaller. This yields the asserted exponent.

## 6. Status and consequence for the research agenda

The root's earlier gate on the public two-thirds comparison is closed
by the formal weighted construction and the source checks above. The
earlier standalone residual-connectivity sketch remains rejected.
The modern tagged-triangle construction remains a separate candidate
whose worst-case wrapper and any two-edge-connectivity application need
their own proofs. This MSF result changes no exact matching exponent
and makes no deterministic polynomial-logarithmic worst-case claim.

