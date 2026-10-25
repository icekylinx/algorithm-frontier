# Proof note

This file is the curated proof record for the result in `README.md`. The original source note follows.

**Original source:** `sources/checkpoint-o/dynamic_msf_public_two_thirds_baseline.md`

# A public 2/3 worst-case MSF baseline and the new reduction's audit boundary

**Independent source and parameter audit, 25 October 2026.**

**Formal interface audit accepted.** The operative proof is
`dynamic_msf_formal_pruning_substitution_audit.md`, independently checked
in `dynamic_msf_public_baseline_root_audit.md`. The bound below is an
accepted derived-public baseline of this research. It uses NSW's actual
weighted certificate and formal worst-case reduction. CGLN's informal
residual-connectivity sketch, read in isolation, would not suffice.

A deterministic fully dynamic exact minimum spanning forest bound

\[
 \exp O\bigl(U^{2/3}h^{1/3}\bigr)
 \quad\text{per update in the worst case},\qquad
 U=\log(N+4),\quad h=\log(U+4),                            \tag{1}
\]

is already a derived consequence of the older public MSF reduction,
the public deterministic balanced-cut construction, and the 2025
worst-case pruning theorem. The October 2026 MSF reduction is not
needed to obtain this quantitative point. The derivation below is
new accounting of these sources; it is not claimed to be a displayed
theorem in any one of them.

Accordingly, the tagged-triangle route in
`dynamic_msf_tagged_triangles_research_candidate.md` must not be
presented as an improvement over this public quantitative baseline
merely for reaching (1). It may supply an alternative implementation
or an extension to another client, subject to its own remaining proof
obligations. It uses no special advantage of the research matching
router.

## 1. Primary sources and current versions

The following official sources were reopened during this audit.

| Source | Exact role |
|---|---|
| [CGLNPS, arXiv:1910.08025v2](https://arxiv.org/html/1910.08025v2), Corollary 6.1 and Section 6.2, equations (4)--(5) | Deterministic decomposition and a parameterized deterministic reading of the NSW MSF reduction |
| [NSW, arXiv:1708.03962v2](https://arxiv.org/pdf/1708.03962), Theorem 7.1, Section 9.3, especially Lemma 9.28 | Explicit worst-case batch-insertion/contraction reduction and its recursive time calculation |
| [MGS, arXiv:2504.00544v1](https://arxiv.org/html/2504.00544v1), Theorems 1.3 and 6.4 | Deterministic pruning with worst-case work and vertex recourse \(\widetilde O(\phi^{-2})\) |
| [MPG, arXiv:2510.08297v1](https://arxiv.org/html/2510.08297v1), Sections 3.5--3.7 | New connectivity framework; its deamortization discussion is brief |
| [MPGY, arXiv:2610.00491v1](https://arxiv.org/html/2610.00491v1), Sections 3, 4, and 6 | Recent randomized polylogarithmic worst-case MSF/2-edge-connectivity result with static decomposition as its only randomized ingredient |

The arXiv histories of 2504.00544, 2510.08297, and 2610.00491 each
show only the listed v1 as of the audit date. The latest randomized
result does not itself assert deterministic polylogarithmic worst-case
MSF. Deterministic polylogarithmic **amortized** MSF is a different,
classical guarantee and is not improved by (1).

## 2. The formal public reduction separates pruning from decomposition

Let \(\gamma>1\). The conservative weighted-decomposition adapter
in the formal audit constructs NSW's hierarchy in
\(n\operatorname{poly}(\gamma)\) time. It has depth
\(O(\gamma)\), total reweighted-edge inventory \(O(n/\gamma)\),
and conductance \(\phi_0=\Omega(\gamma^{-5})\) in every
non-root cluster requiring pruning. Let \(\pi\) bound worst-case
pruning work and publication. With a sufficiently short decremental
period, the resulting recurrence is

\[
 T(n)\le\widetilde O\bigl(\pi(\gamma)
                     \operatorname{poly}(\gamma)\bigr)
       +O(\log n)T\bigl(O(n/\gamma)\bigr).                \tag{2}
\]

NSW Theorem 5.1 asks for a monotone published set \(P\), initially
empty, and existence of \(P'\subseteq P\) whose complement induces
a connected graph. This applies only to **non-root large clusters**.
The root need not expand. The amount of new publication per deletion
and its computation time are bounded by \(\pi\).

This weak connectivity statement supports the actual weighted
certificate, not an arbitrary union of an initial MST and edges
incident to \(P\). Definition 9.5 additionally retains the three
compressed-cluster MSFs, original versions of reweighted edges, and
retired edges. Claims 9.18 and 9.19 use the hereditary child-MSF
invariant and contraction monotonicity to prove that this certificate
contains the exact MSF. Claim 9.19 also justifies publishing a
superset of the unknown witness \(P'\).

NSW Theorem 7.1 and Lemma 9.28 have fixed polynomial dependence on
batch size, preprocessing factor, and the finite update horizon.
Batch insertions contribute to the local charge, whereas only
logarithmically many recursive calls are made for a deletion. Thus
\(\pi\) is not raised to the number of recursion levels in (2).
CGLN's deterministic decomposition removes the randomized branch of
this named worst-case construction.

## 3. Modern pruning, isolated vertices, and a short supported period

MGS Theorems 1.3 and 6.4 deterministically maintain an increasing
vertex set \(A\). During its supported deletion interval, the
positive-volume remainder is a
\(\Omega(\phi/\log^4 m)\)-expander. Each deletion costs
\(\operatorname{polylog}(m)/\phi^2\) worst-case work and adds
at most that many vertices. Linear times a fixed polynomial in
\(1/\phi\) and \(U\) suffices as its initialization allowance.

Conductance conventions can ignore zero-volume vertices, so direct
connectivity is not inferred from that statement alone. In a native
degree-three cluster publish

\[
 P=A\cup N_{\rm initial}(A)
       \cup\{\text{endpoints of deleted edges}\}.
\]

This adds only a constant factor to vertex publication. These extra
vertices are **not** fed as deletions to the pruning algorithm.
Every newly isolated residual vertex lies in \(P\), and positive-
volume residual vertices form one connected component. If that
component exists, remove \(A\) and the residual isolates as the
existential witness. If all residual vertices are isolated, then
\(P=V\), and retain any singleton. Thus the literal NSW interface
holds even in this boundary case.

The MGS deletion horizon is at least \(c\phi_0m_C/Q\), for a
fixed polynomial \(Q=\operatorname{poly}(U)\). Every non-root
large cluster has \(m_C\ge n/(C\gamma)\), so its supported
period is at least \(c'n/(\gamma^6Q)\). Inflate the declared
publication/work factor to \(\pi=\gamma^{12}Q'\), and choose

\[
 T_{\rm period}(n)=
   \left\lfloor n/(C\pi d\gamma)\right\rfloor,
 \qquad d=\Theta(\gamma).                                \tag{3}
\]

Actual pruning costs only \(\gamma^{10}\operatorname{poly}(U)\).
The declared factor is still a fixed polynomial in \(\gamma\),
and (3) expires well before any local pruning horizon. No
whole-instance publication at the end of a horizon, or gradual
completion device, is needed. Actual-size polynomial bases handle
floors and zero-length periods. The total published inventory remains
\(T_{\rm period}\pi d=O(n/\gamma)\), exactly as used by
NSW's compressed certificate and recursive sparsification.

## 4. Deterministic decomposition with the required gamma

Use CGLNPS Corollary 6.1 with parameter \(r\) and crossing budget
\(\epsilon=\gamma^{-2}\). Its output expansion is at least

\[
 \frac{\gamma^{-2}}{\exp O(r^2h)},
\]

and its time, on an actual \(M\)-edge instance, is at most

\[
 M\exp O(U/r+r^2h)\gamma^4.                               \tag{4}
\]

Choose

\[
 r=\Theta((U/h)^{1/3}),\qquad
 \gamma=\exp\bigl(C(U/r+r^2h+h)\bigr)                     \tag{5}
\]

for a sufficiently large fixed \(C\). The contracted output
expansion is then at least \(\gamma^{-3}\), and (4) is
\(M\operatorname{poly}(\gamma)\). Expanding protected blocks
of size \(\Theta(\gamma)\) loses a further fixed power, giving
the safe native-cluster bound \(\phi_0=\Omega(\gamma^{-5})\).
Also

\[
                 \log\gamma=O(U^{2/3}h^{1/3}).             \tag{6}
\]

At each hierarchy step first remove the current weight band and then
decompose, while preserving the initial MSF block trees. This order
ensures that returned children have the stated expansion. NSW's
contraction lemma and the protected-tree weight argument give the
hereditary child-MSF property. The full construction, including
unbounded-degree contracted inputs and all actual-size cutoffs, is in
the operative formal audit.

Only this displayed, fully public decomposition interface is needed;
the slightly sharper Section 5.1 output-quality tradeoff is optional.
In particular the tagged-triangle demand gadget plays no role in this
baseline.

There is no master-size padding. Stop the dynamic recursion and use
an exact small-graph implementation once its actual size is at most
\(\gamma^{c_1}\) for a fixed constant \(c_1\). Its polynomial
cost is within \(\operatorname{poly}(\gamma)\). Above this
threshold, the source restriction \(r=O(\log M)\) holds with
room to spare. Alternatively use the local cutoff
\(r_M=\min\{r,c_2\log(M+2)\}\); the same global upper bound
in (4) follows. The usual bounded-degree reduction is already part
of the named MSF framework.

## 5. Solving the worst-case recurrence

Use one master upper bound \(\gamma\) from (5) in the recurrence;
the exact base handles the range in which \(n/\gamma\) is too
small for another reduction. There are
\(O(U/\log\gamma)\) nonbase levels. Equations (2) and (3) give

\[
 T(N)\le
   \operatorname{poly}(\gamma,U)\,
   \exp O\left(\frac{Uh}{\log\gamma}\right).              \tag{7}
\]

The second logarithmic term is
\(O(U^{1/3}h^{2/3})\), smaller than (6). Hence (7) proves (1),
using the named public worst-case reduction throughout. Exact MSF
edge changes are the output of that reduction. The result also
supports connectivity queries through the maintained forest.

For arbitrary tied weights, use deterministic lexicographic ordering
by weight and immutable edge identity. This selects one exact MSF
without changing the original minimum-weight objective. The time is in a
comparison-RAM model with constant-time weight comparisons, or with
weights having polynomially many bits in \(\log N\), whose arithmetic
cost is absorbed in \(\operatorname{poly}(U)\). Arbitrary
polynomial-in-\(N\) bit lengths do not have free comparison cost.

This is a **derived public-framework baseline**. It is not claimed
to optimize all public parameter choices or all dynamic MSF
algorithms. The primary-source search also located the October
2026 randomized polylogarithmic improvement; its randomness prevents
using it as a deterministic bound without a further construction.

## 6. What the October 2026 deamortization reference does and does not supply

The new 2610.00491 construction has a useful explicit amortized
parameter structure. With local monotone-publication bound \(\eta\)
and static factor \(F\), one deletion creates only one deletion
at any later level. New publications are forwarded as insertions,
so their multiplicity is additive across the hierarchy. Static
rebuild periods proportional to reduced size divided by
\(\eta\operatorname{poly}(U)\) yield amortized
\(F\eta\operatorname{poly}(U)\) work.

Its final Section 6.1 paragraph invokes background rebuilding and
refers to 2510.08297. Reopening that paper does not reveal a more
detailed parameterized theorem: Section 3.5 consists of a short
background-rebuilding and pointer-switching discussion. Section 3.6
then explains how query access to an implicit forest yields an
explicit spanning forest. It does not state a uniform theorem with
arbitrary growing \(F\) and \(\eta\).

Therefore a proof for the new tagged construction must still either
give a precise shadow-version/catch-up implementation with fixed
polynomial dependence on these factors, or name and verify a
sufficient external worst-case wrapper. An amortized substitution
alone does not establish its worst-case claim. Equation (1) above
avoids that outstanding issue by using NSW's explicit worst-case
reduction instead.

## 7. Consequences for further work

The outstanding new-reduction proof is now an alternative-proof or
2-edge-connectivity transfer question, rather than a route to a
new MSF exponent. A 2-edge-connectivity result is not asserted by
this note: the older MSF reduction by itself does not maintain all
bridge-cover information. Its modern client has additional
interfaces and must be audited separately.

No general graph maximum-matching exponent follows from this MSF
calculation. The general matching objective and the separate
strong-forest/Gomory--Hu research result retain their own stated
interfaces and bounds.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
