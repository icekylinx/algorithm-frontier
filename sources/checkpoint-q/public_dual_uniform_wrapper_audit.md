# Independent audit of the parameterized public dual-flow baseline

**25 October 2026. Status: source-dependence audit, with an explicit reconstruction of the missing parameter substitution.**

This note supplements [the public dual reoptimization](public_dual_reoptimization.md). The conclusion is that the four-fifths specialization is supported by the public constructions. The printed five-sixths theorem is therefore an inadequate comparison baseline for a claim that a different static minimum-cost-flow algorithm at four fifths is a new asymptotic improvement.

The conclusion concerns the mathematical interfaces and their parameter dependence. As with the cited theorems, this note imports the existing refining-partition, vertex-split, self-loop, and numerical implementations; it does not claim a new implementation or a separate verification of every line of those papers.

## 1. Sources and the point being checked

Use the following primary sources.

1. Chuzhoy, Gao, Li, Nanongkai, Peng, and Saranurak (CGLNPS), *A Deterministic Algorithm for Balanced Cut with Applications to Dynamic Connectivity, Flows, and Beyond*, arXiv:1910.08025v2. [PDF](https://arxiv.org/pdf/1910.08025v2). The relevant results are Lemma 5.3, Theorem 5.1, Corollary 5.2, and Lemmas 6.12--6.13.
2. van den Brand, Chen, Kyng, Liu, Meierhans, Probst Gutenberg, and Sachdeva (FO24), *Almost-Linear Time Algorithms for Decremental Graphs: Min-Cost Flow and More via Duality*, arXiv:2407.10830v1. [HTML](https://arxiv.org/html/2407.10830v1). The relevant parts are Sections 4.1--4.4, the proof of Theorem 4.11, Claim 4.22, Theorem 5.8, and Sections 6--6.2.
3. Sulser and Probst Gutenberg (PS), *Near-Optimal Algorithm for Directed Expander Decompositions*, arXiv:2403.04542v2, 11 February 2025. [PDF](https://arxiv.org/pdf/2403.04542). The relevant parts are Definition 2.2, Theorem 4.1, and Appendices A.5--A.6. The unversioned URL currently resolves to v2; the version is printed on its first page.

Let

\[
 U=\log(M+4),\qquad h=\log(U+4),\qquad
 \chi=\exp(Cph),\qquad
 F=\exp C(U/p+p^2h),
\]

where `C` denotes a sufficiently large absolute constant, `p` is a positive integer in the admissible CGLNPS range, and all actual graphs have at most a fixed polynomial in the master size `M` records. Increasing the absolute constants permits the same envelopes at every invocation.

The question is whether FO24 Section 4.4 admits the uniform replacement

\[
 c_0,c_1\leq\chi^{O(1)},\qquad
 T_{\rm decomp}\leq M F\chi^{O(1)}\theta^{-O(1)},           \tag{1}
\]

with absolute exponents. The printed paper gives only the specialization `p` of order `U^(1/3)`. Crucially, `F` must not enter the output-quality constants `c0,c1`, nor be raised to a later hierarchy depth.

## 2. The static witness has a uniform linear quality exponent

CGLNPS Lemma 5.3 gives, on a bounded-degree graph, either a cut of sparsity at most a chosen `theta`, or an explicitly embedded spanning witness of expansion

\[
 \psi_p=\log^{-O(p)} M.
\]

The construction time is

\[
 \widetilde O\bigl(M^{1+O(1/p)}\log^{O(p^2)}M+M/\theta\bigr)
 \leq MF\theta^{-O(1)}.                                  \tag{2}
\]

The witness has maximum degree `O(log M)`, and its embedding congestion is `O(log M/theta)` after the standard bounded-degree reduction. Converting sparsity to conductance, making the degree comparison in PS Definition 2.2, and contracting the degree-reduction gadgets costs only fixed powers of `log M` and `psi_p^-1`. Consequently the interface can be written as a `(varphi,psi)` witness with

\[
 \psi^{-1}\leq\chi^{O(1)},\qquad
 \varphi\geq\theta\chi^{-O(1)}.                          \tag{3}
\]

These normalizations do not depend on `F`. CGLNPS Section 5.2 gives the deterministic degree reduction and canonical-cut conversion. Its Theorem 5.1 and Corollary 5.2 explicitly state the linear `O(p)` quality exponent, whereas the faster low-conductance theorem in the introduction has a different quadratic quality loss. The latter must not be substituted here.

### Fake edges do not introduce an inverse-conductance quality loss

The proof of CGLNPS Lemma 5.3 contains a useful stronger property than the bare congestion bound. Each missing matching pair receives its own fresh fake edge, and its witness embedding path consists of that one edge. All real routing calls in later rounds are still made on the original graph `G`, not on `G` augmented by earlier fake edges. Hence every fake-edge record is used by only its own witness path, up to the constant duplication used in the witness normalization:

\[
 |\Pi^{-1}(F_{\rm fake})|=O(|F_{\rm fake}|).               \tag{4}
\]

This statement follows directly from the partial matching and singleton-path construction on printed pages 34--35. It is stronger than bounding this quantity by the maximum congestion times the number of fake edges. The weaker estimate would introduce an unnecessary `theta^-1` into the balancing tolerance.

Set the unmatched-pair tolerance to

\[
 z=cM\psi^a/\log^b(M+4)
\]

for sufficiently large fixed `a,b` and sufficiently small fixed `c`. Since the number of cut-matching rounds is `O(log M)`, (4) gives

\[
 |\Pi^{-1}(F_{\rm fake})|\leq c'\psi^2M,
\]

with any desired fixed small `c'`. The alternative cut has both sides of volume at least `M chi^-O(1)`. This balance parameter depends on `psi`, and thus on the output quality, but not on the construction work `F` or on `theta^-1`.

## 3. The PS pruning framework has only fixed powers of witness quality

PS Definition 2.2 exposes both parameters rather than hiding them in a polylogarithmic specialization. A `(varphi,psi)` witness has congestion at most `psi/varphi` and degree comparison

\[
 \deg_G(v)\leq\deg_W(v)\leq\deg_G(v)/\psi.
\]

Its Theorem 4.1 is deterministic and, for an appropriate deletion set `D`, provides the following explicit bounds:

\[
 \begin{aligned}
 \text{new witness parameters}
   &=\left(\varphi\psi^6/32000,\ \psi^4/800\right),\\
 |E^r|&\leq(\varphi/4)\sum_{P\in\mathcal P}\operatorname{vol}_G(P),\\
 \sum_{P\in\mathcal P}\operatorname{vol}_W(P)
   &\leq(8/\psi)|\Pi^{-1}(D)|,\\
 \text{admissible deletion condition}
   &:\quad 200\psi^{-2}|\Pi^{-1}(D)|<|E(G)|.
 \end{aligned}                                           \tag{5}
\]

The time bound is `O(H |D|/(psi^2 varphi))`, where the label height is `H=O(log n/varphi)`. Thus it is bounded by

\[
 |D|\operatorname{polylog}M\,\psi^{-O(1)}\varphi^{-O(1)}. \tag{6}
\]

The hypotheses on fake edges in Section 2 satisfy the initialization deletion condition in (5). The retained component has the desired expansion at least `theta chi^-O(1)`.

The powers in (5) are incurred a fixed number of times for a newly initialized component. They are not iterated at every deletion: a pruning data structure continues to use its original witness. When the decomposition creates a new component that requires a fresh static call, that call starts again with (3). There is no sequence `psi -> psi^4 -> psi^16 -> ...` of input witnesses down the decomposition recursion.

## 4. Why the decomposition wrapper preserves (1)

PS Appendix A.5 builds a static decomposition by fresh cut/witness calls followed by pruning. There are two ways the recursion proceeds.

* A sparse cut removes a fraction at least `chi^-O(1)` of the local volume from either continuing branch.
* A witness return removes its fake edges and recurses on the pruned pieces. The admissibility threshold and the pruned-volume bound in (5) ensure a fixed-factor volume reduction for these pieces.

Therefore the sum of graph volumes over a recursion is at most

\[
 M\chi^{O(1)}\operatorname{polylog}M.                    \tag{7}
\]

Multiplying (7) by the cost of a fresh static call per unit volume gives `MF chi^O(1) theta^-O(1)`. The static subroutine is called afresh; its internal computation time is not used to choose the cut budget, the witness quality, or the recursion balance. Summing boundary edges through the same volume accounting yields a boundary coefficient `chi^O(1)`, with expansion `theta chi^-O(1)`.

Appendix A.6 maintains such decompositions using the same pruning routine and fresh static calls on pruned pieces. Its stated epoch length is a fixed constant times `varphi psi M`, and its run-time proof uses the total pruned volume `O(|D|/varphi)` and the bound (6). Reinitialization after an epoch adds only fixed powers of `varphi^-1` and `psi^-1`. Substituting (3) consequently has exactly the form (1).

One must retain the full FO24 Theorem 4.8 interface at this point. PS's displayed Theorem A.5 explicitly promises refinement for one epoch; citing only that theorem and silently merging clusters at a restart would not prove FO24's global refining interface. FO24 Sections 4.1 and 4.4 specify the refining, monotonically accumulating cut-set version and its vertex-split/self-loop extension. Its derandomization changes only the static cut/witness calls. In that wrapper, the volume and update charges above depend on the expansion, balance, witness congestion, and epoch thresholds, all of which are fixed powers of `chi` and `theta^-1`; they do not depend on `F`. Thus the same existing interface carries the uniform dependence (1).

The capacitated-to-uncapacitated conversion of FO24 Section 4.1 adds another fixed power of `theta^-1`. It also changes the size seen by a static call from `M` to at most `M theta^-O(1)`. For the later choice `log(theta^-1)=o(U)`, this has logarithm `O(U)`, so the global expressions for `chi` and `F` remain valid.

This is the needed parameter substitution. It does not use the new sequential routing construction or the moving-box flow client.

## 5. Independent confirmation that construction work is not recourse

FO24's proof of Theorem 4.11 establishes three separate properties for the expander hierarchy. Its Property 3 bounds the number of updates to each level graph by `M polylog M`: each partition is refining, each split has a permanent descendant relation, and every monotone cut-edge record causes at most two corresponding self-loop insertions. These counts are independent of the effort spent constructing the decomposition.

The exported tree has only `M polylog M` cluster records. Its capacities are rounded to powers of two and made monotonically decreasing. Polynomial capacity range therefore gives `polylog M` changes per tree edge. Allowing any polynomial number of hierarchy levels preserves this recourse bound.

Claim 4.22 then charges each fully dynamic core period once. If a level has a core of size `M_{i-1}` and rebuilds every `M_i` updates, its total construction contribution is

\[
 M_{i-1}F_{\rm dec}\frac{M}{M_i}
 =MF_{\rm dec}\exp O(U/L).
\]

It is incorrect to replace the exported recourse by the full internal work `M F_dec` and propagate that computational work through all `L` levels. The source's structural accounting avoids precisely that multiplication.

## 6. Later interfaces do not erase the four-fifths balance

For the parameters

\[
 t=(U/h)^{1/5},\quad p\asymp L\asymp t,\quad
 s=\log\theta^{-1}\asymp t^3h,
\]

the companion note proves that both the tree-cut quality and its amortized work have logarithm `O(t^4 h)`. There are two additional checks.

**Change detection.** FO24's dependency graph has depth `L+1` (or a harmless additional logarithmic factor under alternate bookkeeping), and in-degree `polylog M`. Theorem 5.8 therefore introduces at most `exp O(L h)` (conservatively `exp O(L h^2)`) copies and approximation loss. Both are smaller than `exp O(t^4 h)`.

**The numerical client.** Theorem 6.3 uses `~O(M kappa^2)` iterations. Its lazy slack updates, detection tolerance, global rebuilds, and initialization multiply fixed powers of the oracle quality, work, and detection loss. Even charging every detection multiplicity explicitly preserves a bound `M exp O(t^4 h)`. The source also bounds the magnitude range of the slacks quasipolynomially. Its numerical implementation is imported here; a magnitude bound alone is not a proof that exact rational denominators stay short. In particular, this source-parameter audit must not be presented as an independent common-grid arithmetic reconstruction.

Static flow extraction in Section 6.2 uses one constant-factor undirected minimum-congestion flow computation. To avoid treating its cited randomized nearly-linear implementation as deterministic, CGLNPS Lemmas 6.12--6.13 supply an explicit deterministic alternative:

\[
 M^{1+O(1/r)}\log^{O(r^3)}(MR),
\]

where `R` is the capacity ratio. For `log R=poly(U)`, setting `r` of order `(U/h)^(1/4)` bounds this by `M exp O(U^(3/4) h^(1/4))`, up to larger fixed logarithmic powers if one uses the paper's displayed, less tightly balanced specialization. In either form its leading logarithmic exponent is below `4/5`. Final binary search and integral flow rounding incur only polylogarithmic or nearly-linear overhead.

## 7. Consequence for comparison and attribution

The public framework, with its independent parameters retained, supports the comparison bound

\[
 M\exp O\bigl(U^{4/5}h^{1/5}\bigr).
\]

This is a derived specialization of public constructive ingredients. It is not the literal exponent displayed in FO24 Theorem 6.17, and should not be cited as if that theorem printed it. Conversely, the printed five-sixths specialization cannot justify claiming that a different four-fifths static min-cost-flow route surpasses the best bound obtainable by straightforward parameter reoptimization of these sources.

The new moving-box client remains an independent numerical construction, with explicit dyadic arithmetic, original-edge recovery, and exact final acceptance. Its potential applications to incremental flow, raw-cycle clients, or distance maintenance require their own comparisons; the static four-fifths exponent alone is no longer a separating result.
