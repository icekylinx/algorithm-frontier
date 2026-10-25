# Verification note

**Curated source path:** `sources/checkpoint-q/current_checkpoint/matching_size_kernel_corollary.md`

The source audit follows.

# An exact matching-size kernel and the current time corollary

**Elementary matching-preserving reduction.** The kernel proof below
is independent of the OAI phase and the numerical backend. Composing
it with the current candidate gives

    O(n+m) + (min{m_s, nu(G)^2}+1)^(1+o(1)),

or, for each fixed epsilon>0,

    O(n+m) + O_epsilon((min{m_s, nu(G)^2}+1)^(1+epsilon)).

Here m_s is the number of distinct nonloop edges after cleanup. The
kernel itself is unconditional; the improved solve time retains the
proof status and dependencies in `uniform_general_maximum_matching.md`.
No publication-priority claim is made for this elementary reduction.

## 1. A linear-time quadratic edge kernel

First scan the input, discard loops and duplicate edge copies if needed,
and construct any deterministic maximal matching `F` by greedy edge
order. Retain original edge identifiers. Let

    C = V(F),     c = |C| = 2|F|,     U = V\C.

If `F` is empty, there are no useful edges. Otherwise `c>=2`. Maximality
implies that `U` is independent, so `C` is a vertex cover. Therefore

\[
                  |F|\le\nu\le c=2|F|\le2\nu.      \tag{2}
\]

Construct a subgraph `H` retaining:

1. every edge with both endpoints in `C`;
2. for each `u in C`, any `min(deg_U(u),c+1)` incident edges to distinct
   vertices of `U`.

All choices use fixed edge order. Scanning adjacency lists constructs
`H` in `O(n+m)` time. Its edge count `m_H` obeys

\[
 m_H\le \min\left\{m_s,\binom c2+c(c+1)\right\}
      =O(\min\{m_s,\nu^2\}).                        \tag{3}
\]

Delete isolated vertices of `H`; its remaining vertex count `n_H` is
at most `2m_H`.

### Exact matching preservation

Every matching has at most `c` edges, since `C` is a vertex cover. Take
any maximum matching `M` of the original graph. If an edge `uv` of `M`
was omitted from `H`, it must have `u in C` and `v in U`, because all
`C-C` edges were retained. The vertex `u` has `c+1` retained neighbors
in `U`. At most `c` vertices of `U` are matched by `M`, so one retained
neighbor `w` is unused. Replace `uv` by `uw`.

The replacement keeps the matching cardinality, creates no conflict,
and decreases the number of edges outside `H`. Repeat until no omitted
edge remains. This is an existence proof; the algorithm does not need
to know `M` or perform these replacements. Since `H` is a subgraph,
it follows that

\[
                            \nu(H)=\nu(G).         \tag{4}
\]

Every edge of the greedy matching `F` belongs to `H`, because its
endpoints lie in `C`. Thus all bounds in (2) remain valid for `H`.

## 2. Composition and independent acceptance

Build and compact H once. Its nonempty compact size is
q_H=n_H+m_H=Theta(m_H), and all retained edges carry original IDs.
Apply the exact odd-path degree reduction and optimum-gap driver in
`general_graph_gap_reduction.md`, using the persistent-carrier phase
and either complete numerical route. The fixed-parameter branch has
cost q_H^(1+O(1/a)+o_a(1)). No separate warm start or classical tail is
needed for this current composition.

Every branch of the uniform program shares the same read-only H.
Validate a proposed matching and search for an augmenting path in H.
Absence of an augmenting path proves optimality in H; the independent
identity nu(H)=nu(G) then proves optimality in G. The verifier need not
rescan the original graph on each proposal. Map the final matching's
edge IDs back once, after acceptance.

Choosing a sufficiently large fixed branch proves each fixed-epsilon
bound above. The separate instruction-interleaving proof in
`deterministic_uniformization_by_optimality_check.md` gives the same
single-program 1+o(1) envelope with q_H in place of the original compact
size. Cleanup, greedy construction, kernelization and final translation
are charged once in O(n+m).

If nu=0, the greedy scan finds no nonloop edge and returns the empty
matching. The added one in the displayed expressions handles this
case uniformly. No supplied value or estimate of nu is needed: c is
computed by the greedy matching and lies between nu and 2nu.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
