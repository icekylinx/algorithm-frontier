# Public parameter comparison for the weak-Haxell reanalysis

**Primary-source audit, 25 October 2026.**

This note records what has actually been checked for the parameter
comparison in [weak-haxell-current-blocker-growth.md](weak-haxell-current-blocker-growth.md). It does not
assert that every possible reanalysis of the public literature has
been optimized.

Throughout, an edge has one left vertex and `r-1` right resources,
`n` is the number of left vertices, and `0<epsilon<1`. The promise
being compared is

$$
\tau(E_S)>(2r-3+\epsilon)(|S|-1)
                  \quad\hbox{for every nonempty }S\subseteq A.
$$

## 1. Annamalai's matching algorithm and certifying theorem

The primary source is [Annamalai, arXiv:1509.07007v2](https://arxiv.org/html/1509.07007v2),
particularly Theorems 1.3 and 5.4, Sections 3--5, and the degree
parameters following Definition 2.4. Its
[arXiv history](https://arxiv.org/abs/1509.07007) lists v2 as the
latest version. The [journal record](https://link.springer.com/article/10.1007/s00493-017-3567-2)
is *Combinatorica* 38 (2018), 1285--1307.

The displayed theorem is polynomial time for each fixed `r` and
`epsilon`; its exponent is not given as a single uniform formula.
The certifying alternative already belongs to Theorem 5.4. Thus
neither the existence of a deterministic algorithm under the above
promise nor the qualitative certificate alternative is a new claim
of this research round.

The source's parameters are

$$
\mu=\epsilon^2/(10r^2),\quad Q=\lceil1/\mu\rceil,
 \delta_X=\epsilon/(5r^2).
$$

An immediate length-aware count of its existing nondecreasing
signature vectors gives the derived exponent

$$
O\!\left((r^2/\epsilon)\log(2+r/\epsilon)\right).
$$

The derivation is in [weak-haxell-uniform-lifetime-analysis.md](weak-haxell-uniform-lifetime-analysis.md).
This should be treated as a public-formula baseline, not as a bound
explicitly printed in the theorem. Counting arbitrary partitions
without using the signature's length gives a weaker uniform
dependence, so comparison only with that coarse count would
understate what the public proof already provides.

The internally audited improvement in [weak-haxell-current-blocker-growth.md](weak-haxell-current-blocker-growth.md)
adds a new proof that every surviving layer's **current** blocker
count exceeds `epsilon/(10r)` times the size of its lower prefix.
That reduces the exponent to

$$
O\!\left((r/\epsilon)\log(2+r/\epsilon)\right).
$$

Both a weighted lifetime count and a length-aware count of the
source signature then give this rate. The operation sequence on
promised inputs is the public algorithm's sequence; retained
historical certificates and stopping checks implement the explicit
certifying alternative.

## 2. Graf--Haxell is relevant under exactly the same promise

The later primary source is [Graf--Haxell,
*Finding Independent Transversals Efficiently*,
arXiv:1811.02687v2](https://arxiv.org/html/1811.02687v2),
Theorem 4, Definition 10, Lemmas 16--20, and Section 7.1.
Its [official history](https://arxiv.org/abs/1811.02687) identifies
v2 of February 2020 and the journal publication in
*Combinatorics, Probability and Computing* 29 (2020), 780--806.

Section 7.1 constructs the intersection graph on hyperedges and
applies the independent-transversal theorem with

$$
\epsilon'=\epsilon/(r-1).
$$

The graph is `r`-claw-free. Crucially, the returned dominating set
contains a constellation. Counting overlaps within its stars saves
one right resource per relevant leaf and recovers the coefficient
`2r-3`. A comparison that simply charges `r-1` resources to each
dominating vertex and concludes that this needs coefficient
`2r-2` would be incorrect. The theorem does cover the same promise.

The example feasible parameters in Definition 10 are

$$
\mu=\rho=\epsilon'/(10r),\qquad U=10r/\epsilon'.
$$

For the hypergraph application, `rho=Theta(epsilon/r^2)`.
Lemma 16 gives signature length
`L=O(rho^{-1} log(n+1))`. With logarithmic base
`b=U/(U-mu rho)`, Definition 17 and Lemma 20 give maximum
coordinate

$$
H=O\!\left(\rho^{-3}
       [L\log(1/\rho)+\log(n+1)]\right).
$$

A length-aware count is therefore

$$
\log\#\mathrm{signatures}
   =O(L\log(2+H/L))
   =O\!\left((r^2/\epsilon)\log(2+r/\epsilon)
                       \log(n+1)\right).
$$

This is again a derivation from named public formulas. The paper
itself explicitly does not optimize the parameter dependence. Its
per-iteration bound in the proof of Theorem 4 is polynomial in the
intersection-graph input size; the direct hypergraph implementation
in the present notes instead pays the explicit incidence volume.
Neither observation rules out better implementations or a stronger
new analysis of that public algorithm.

## 3. The 2026 almost-linear strong-Haxell result has a different promise

[Bucic--He--Huang--Saranurak, arXiv:2511.02214v1](https://arxiv.org/html/2511.02214v1)
(SODA 2026), Theorem 1.5, works with a strong condition of the
form `tau(E_S)>=Phi|S|` and `Phi>=d(r-1)^2`, `d>=4`,
after converting its right-rank convention to the present one.
The `(|S|-1)` weak-Haxell promise with coefficient close to `2r`
does not imply that condition. Its almost-linear theorem therefore
cannot be substituted into the near-threshold comparison above.

The research round's sharper quantitative reanalysis of that strong
condition is recorded separately. It also belongs to a public
algorithm reanalysis, and it should not be conflated with the
near-threshold result here.

## 4. Exact status of the comparison

| Item | Promise | Checked quantitative conclusion |
|---|---|---|
| Annamalai, Theorems 1.3/5.4 | Near-threshold weak Haxell | Printed polynomial time for fixed parameters; certifying formulation already known |
| Length-aware count of the existing Annamalai signature | Same promise | Derived exponent `O((r^2/epsilon) log(2+r/epsilon))` |
| Graf--Haxell, displayed parameters and Section 7.1 reduction | Same promise | Same rank-squared order from a length-aware signature count |
| Current-blocker lemma in this round, followed by either count | Same promise | Internally audited exponent `O((r/epsilon) log(2+r/epsilon))`; root and independent audits accompany the main note |
| BHHS, Theorem 1.5 | Stronger rank-squared expansion promise | Almost-linear result; not a substitute for the weak promise |

The source check has not identified a displayed near-threshold
uniform rate already implying the proposed rank-linear exponent.
This is not a claim that such a result is absent from the entire
literature. The safe attribution is a quantitative strengthening of
the named public algorithm and proof, with explicit parameter
accounting. Ordinary bipartite graph matching at `r=2` has far
better algorithms and is outside the claimed advantage.
