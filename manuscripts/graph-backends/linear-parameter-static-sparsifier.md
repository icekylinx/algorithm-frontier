# A normalized static sparsifier with linear parameter dependence

**Research refinement, 24 October 2026.** Substitute the explicit
sequential router into the length-free ambient construction. The
returned normalized route table is part of the output. This is a
research proof assembly, not an externally verified implementation.
The delivered 5/6 threshold-router checkpoint is unchanged.

## 1. Contract

Let U>=2, h=ceil(log_2(U+4)), and 1<=p,r<=U with (p+r)h<=U.
The input is a loopless demand multigraph J and endpoint-annotated
ambient walks Pi(e) in H'. Preserve distinct native lifetime IDs.
Write m_J=|E(J)|, n_J=|V(J)|, Delta=Delta(J), L_0>=1 for maximum
ambient length, and C_0 for ambient vertex-occurrence congestion.
Endpoints and repeated occurrences count in C_0.

There are uniform factors
$$
\log\Gamma=O((p+r)h),\qquad
 \log F=O(U/p+U/r+r^2h+(p+r)h)                              \tag{1}
$$
such that the output is a table Pi', a subgraph J_tilde of J, and
endpoint-preserving routes R:J->J_tilde with
$$
\begin{aligned}
 |E(J_{\rm tilde})|&\leq n_J\Gamma\mathrm{poly}(U),\\
 L(R)&\leq\Gamma,\quad L(\Pi'\circ R)\leq\Gamma L_0,\\
 C(\Pi'\circ R)&\leq\Gamma(C_0+\Delta).
 \end{aligned}                                               \tag{2}
$$
Full work, plus actual vertex bookkeeping, is
$$
m_JF^{O(1)}\Gamma^{O(1)}(L_0+1)\mathrm{poly}(U).
                                                               \tag{3}
$$
F enters neither selected size nor congestion. Loops use the local
annotated empty-route convention of the distance client before this
nonloop primitive; isolates are processed at actual size.

## 2. Two distinct path normalizations

First erase closed subwalks of each Pi(e), using IMMEDIATE ambient
vertex IDs and lifetimes. This gives simple Pi'(e), with length
at most L_0 and congestion at most C_0. A stack and deterministic
position dictionary cost the supplied list length up to logarithms.
Distinct aliases with the same eventual physical image stay distinct.

Separately, project every returned token route from its incidence-port
graph to its immediate token HOST, then loop-erase using that host's
IDs. This supplies simple J_i paths before weighted ambient selection
and simple W_i paths for reverse routing. Both actual output-list
costs are charged.

The theorem concerns Pi', not an arbitrary unchanged Pi. Individual
route-image gradients need not be preserved. The distance-cycle
client uses e minus its NEW route as its correction circulation;
[normalized-route-cycle-comparison.md](normalized-route-cycle-comparison.md)
proves the exact identity and raw-lift compatibility.

## 3. Degree bands and weighted witnesses

Use
[separated-static-sparsifier-parameters.md](separated-static-sparsifier-parameters.md)
and [length-free-ambient-static-sparsifier.md](length-free-ambient-static-sparsifier.md).
Parameter r gives common conductance phi=exp(-O(rh)).
Partition J into J_0 with at most n_J edges and band graphs J_i.
Each nontrivial component has conductance at least phi and minimum
degree at least rho_i=phi 2^i. Decomposition work is
$$
m_J\exp O(U/r+r^2h+rh)\mathrm{poly}(U).  \tag{4}
$$
Its constant-conductance witness W_i has fresh edges of common
weight rho_i and, for an absolute D_w,
$$
\deg_{J_i}(v)\leq\rho_i\deg_{W_i}(v)\leq D_w\deg_{J_i}(v).
                                                               \tag{5}
$$
The established actual-inventory bounds are
$$
\begin{aligned}
 \sum_i|E(W_i)|&\leq O(n_J\phi^{-1}U),\\
 \sum_i|E(W_i)|&\leq O(m_J\phi^{-1}),\\
 \sum_i\rho_i|E(W_i)|&\leq O(m_J),\qquad \phi\leq\rho_i\leq\Delta.
 \end{aligned}                                               \tag{6}
$$
No master-sized graph is allocated.

An optional fully elementary replacement for the witness construction
is proved in
[hypercube-weighted-witness.md](hypercube-weighted-witness.md).
Its degree multiplier is explicitly D_w=O(U), and its conductance
is at least 1/O(U). Its Section 4 replaces the three inventories
in (6) by O(n_J phi^{-1} U^2), O(m_J phi^{-1} U), and O(m_J U),
respectively, and proves both full query volumes O(m_J U/phi).
These additional fixed polynomial-U factors are absorbed in (1)--(3).
When this alternative is used, D_w is not treated as an unchanged
absolute constant in the intermediate calculations below.

## 4. Pay the new router's full query volumes

[sequential-expander-routing-tradeoff.md](sequential-expander-routing-tradeoff.md)
preprocesses an m_H-edge expander once in
m_H exp O(U/p+ph+log(Phi_H^{-1})) poly(U) work. A query at
degree-proportional endpoint load D costs m_HD Q poly(U), returning
simple paths of length Q and edge congestion DQ.
Use a common Q=exp O((p+r)h).

Forward direction: for each witness edge make ceil(rho_i) token
copies through J_i. Endpoint multiplicity is at most
$$
\lceil\rho_i\rceil\deg_{W_i}(v)
                         \leq(2D_w/\phi)\deg_{J_i}(v).       \tag{7}
$$
Use D_1=ceil(2D_w/phi). Query volume sums to O(m_J/phi);
the real token inventory also sums to O(m_J/phi). All dummy
tokens required by the full router are thereby paid.

Reverse direction: route one token per J_i edge through W_i.
By (5) the load parameter is D_{2,i}=max(1,ceil(rho_i)), and
$$
\sum_i |E(W_i)|D_{2,i}
 \leq\sum_i(\rho_i+1)|E(W_i)|=O(m_J/\phi).                    \tag{8}
$$
Only query work multiplies this load. Each W_i and J_i component
is preprocessed once at its actual size, never once per load unit.

Combining both directions and (6), router work is
m_J exp O(U/p+(p+r)h) poly(U). Together with (4) this gives
the F envelope in (1), with all constants uniform in p,r.

## 5. Weighted path selection

Forward candidates have aggregate edge-occurrence congestion O(Q/phi)
on J. Band edge sets are disjoint. After composition with Pi', their
total unweighted occurrence count at a fixed ambient vertex is
O(Q C_0/phi). One candidate has at most Q host edges, each with a
SIMPLE ambient image; its count at that vertex is O(Q+1), independently
of L_0. In
[deterministic-weighted-path-selection.md](deterministic-weighted-path-selection.md),
$$
B=\max_{g,j,x}\lceil\rho_i\rceil a_{gjx}
                              \leq O((\Delta+1)(Q+1)).       \tag{9}
$$
Apply the deterministic sparse selection globally, keeping one P_g
per witness edge with weight rho_i. Weighted ambient congestion is
$$
O(Q C_0/\phi+Q(\Delta+1)\log(N_{\rm used}+2))
       \leq Q\phi^{-O(1)}\mathrm{poly}(U)(C_0+\Delta).   \tag{10}
$$
Only represented ambient vertices count; log N_used=O(U).
Residual J_0 adds at most C_0.

Sparse conditional expectations read every candidate occurrence list.
Their finite precision costs the total list size up to logarithms.
Expanding ambient images costs O(L_0) per routed host-edge occurrence.
This supplies L_0+1 in (3); it is absent only from congestion.

## 6. Select input edges and compose reverse routes

Select the genuine J-edge IDs used by the P_g, plus J_0:
$$
|E(J_{\rm tilde})|
 \leq |E(J_0)|+Q\sum_i|E(W_i)|
          \leq n_JQ\phi^{-O(1)}\mathrm{poly}(U).        \tag{11}
$$
Reverse W_i paths have occurrence load D_{2,i}Q per witness edge.
Relative to weight rho_i it is at most
$$
QD_{2,i}/\rho_i\leq2Q/\phi.         \tag{12}
$$
Replace each witness occurrence by P_g. The final length is at most
Q^2; ambient congestion is bounded by (12) times (10), plus residual
routes. Fixed powers of Q and phi^{-1} give Gamma=exp O((p+r)h).
Ambient length is at most Q^2 L_0, proving (2).

Support retains its central native J-edge ID even if normalization
removes that edge's geometric occurrence. A projected image uses
lower repair layers and at most its own central edge. Loop erasure
preserves this property. Adding the central ID is sufficient, and
harmless if unnecessary after erasure.

## 7. Dynamic and numerical composition

[normalized-projected-route-composition.md](normalized-projected-route-composition.md)
applies to this output type. Index ACTUAL normalized routes, their
native edge/vertex lifetimes, and separate central IDs. Recurrences are
$$
C_{j+1}\leq c\Gamma(C_j+\Delta_{\rm native}),\qquad
 L_{j+1}\leq c\Gamma L_j.                                    \tag{13}
$$
No old length multiplies the new congestion.

[normalized-route-cycle-comparison.md](normalized-route-cycle-comparison.md)
uses correction e-R(e). Normalization's gradient change is included
in that correction, with exact native boundary cancellation.
Coincident physical images never identify distinct native aliases.

Repair scheduling, central-only memberships, degree-reset ports,
raw lifts, exact flow projection, and general matching reduction
retain their contracts. The final exponent pays FULL depth
dK log Gamma; see
[quantitative-matching-4-5-composition.md](quantitative-matching-4-5-composition.md).

## 8. Claim status

This refinement uses the explicit sequential router, its repaired
half-matching entropy lemma, retained virtual hierarchy, and query
induction. Exact final verification protects accepted output but
does not prove the faster work bound. The delivered 5/6 checkpoint
retains its independent CS21 full-matching dependency path.
