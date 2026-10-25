# A uniform deterministic near-linear general-matching candidate

**Research theorem assembly, 24 October 2026.** This note strengthens the
fixed-exponent carrier composition using an independent final optimality
check and a uniform interleaving of parameter branches. The structural
and numerical proof dependencies remain explicit; this is not a claim
of external verification or an implemented performance result.

## 1. Proposed theorem

There is a proposed single deterministic word-RAM program that outputs
an explicit exact maximum-cardinality matching of an arbitrary
undirected general graph with running time

\[
 O(n+m)+(m_s+1)^{1+o(1)},                                         \tag{1}
\]

where `m_s` is the number of distinct nonloop edges and `n,m` are the
original vertex and listed-edge counts. The empty cleaned graph is
handled by the initial input scan. The subpolynomial factor is uniform
over all graphs of the relevant size, although this proof supplies no
useful practical convergence rate. A separate, more explicit candidate
envelope with logarithmic exponent `4/5` is assembled in
`quantitative_matching_4_5_composition.md`, using
`sequential_expander_routing_tradeoff.md` and
`linear_parameter_static_sparsifier.md`. The independent `5/6`
envelope is assembled in
`quantitative_matching_5_6_composition.md`, using the normalized-route
primitive in `length_free_ambient_static_sparsifier.md`.
The preceding `6/7` envelope is retained in
`conditional_matching_6_7_composition.md`, using the reconstructed
static interface in `separated_static_sparsifier_parameters.md` and
the explicit amortized update construction in
`amortized_static_base_distance_sparsifier.md`.
The earlier `14/15` envelope remains independently assembled in
`quantitative_matching_14_15_composition.md`. These use the simpler
outer parameterization in
`binary_ledger_hierarchy_and_decoupled_parameters.md`.
The independent Route A and earlier quantitative calculations remain
available. The present note retains the independent fixed-parameter
portfolio argument.

The optional matching-size-sensitive bound is

\[
 O(n+m)+\bigl(\min\{m_s,\nu(G)^2\}+1\bigr)^{1+o(1)}.              \tag{2}
\]

For a simple input this is also `O(n+m)+(m+1)^(1+o(1))`, and hence
`(n+m)^(1+o(1))`. It includes disconnected graphs, odd-order graphs,
arbitrary densities, and graphs with no perfect matching.

The fixed-exponent theorem in `persistent_carrier_general_matching.md`
remains an alternative quantitative formulation: for every chosen
constant `epsilon>0`, a fixed parameter gives
`O(n+m)+O_epsilon((m_s+1)^(1+epsilon))`.

## 2. The fast branch theorem being used

The carrier construction proves, subject to its named imports, an
eventual fixed-parameter statement. For every sufficiently large fixed
integer `a`, the corresponding finite parameterized algorithm, on every
sufficiently large cleaned input, returns an exact maximum matching in

\[
                 q^{1+O(1/a)+o_a(1)},                            \tag{3}
\]

where `q` is its compact input size. The coefficient in `O(1/a)` is
absolute; the constants and convergence threshold may depend on the
fixed parameter. The graph reductions, direct optimum-gap driver,
carrier operations, materialization and numerical bookkeeping are all
included in (3).

This statement uses the following explicit dependencies:

* the September 2026 OAI row/bin framework, with reconstructed
  factor-critical, ledger, projection, priced-client and complete
  phase-cost proofs in the current notes catalogued by
  `oai_baseline_and_imports.md`;
* one complete deterministic raw-cycle construction from
  `numerical_backend_choices.md`: either the degree-three routing,
  legal portal aliases and geometric Steiner bridge, or the explicitly
  degree-sensitive distance-sparsifier integration;
* the appropriate disconnected-component wrapper, including local
  small-component treatment, counted resident recursive slots and
  the required native-split conventions;
* the new persistent actual-ledger representation and canonical
  selected forests in `persistent_integral_ledger_carrier.md`;
* the deterministic local tight-set detector and two-tree exchange;
* the exact odd-path optimum-offset reduction and direct gap driver.

The directed exact-flow subroutine used by the projections is the
deterministic almost-linear minimum-cost-flow theorem of van den Brand
et al., arXiv:2309.16629v1, with the explicitly charged capacity-scaling
specialization described in the backend dependency note. Each numerical
route supplies stable vertex occurrences, explicit representation edits
and literal raw-length certificates. The alternative distance route
does not require the arbitrary-degree routing interface of the 2023
incremental-graphs paper. The routing route now has a separate geometric
reconstruction of that boundary.

The full constructions are not replaced by a generic minimum-ratio
oracle. In particular, a net-circulation score by itself would not
bound the literal traversal charged by the OAI numerical client.

The OAI source is model-produced, unformalized research with varying
verification status. The present reconstructions do not amount to
external certification. A mathematical defect in
one of these fast-branch dependencies would invalidate the improved
time proof, even though the final-check wrapper below would still
protect accepted answers.

## 3. An independent near-linear acceptance test

For a proposed explicit matching `M`, first validate its edge IDs and
the disjointness of its endpoints. Then run one ordinary deterministic
general-graph augmenting-path search relative to `M`.

* If an augmenting path exists, reject the proposal.
* If none exists, accept `M`.

Berge's criterion makes acceptance equivalent to maximum cardinality.
The search is performed on the graph itself and does not consult the
proposer's numerical certificates, ledger state, forest records, or
internal LOW decisions.

The required conservative time is `O(q alpha(q))`. A primary explicit
interface appears in Mehlhorn--Nobahari,
*Gabow's O(sqrt(n)m) Maximum Cardinality Matching Algorithm, Revisited*,
arXiv:2603.22909v2, Figure 3 (Part I), Sections 2.3 and 4:

<https://arxiv.org/pdf/2603.22909v2>.

This is one augmenting-path search from the supplied valid matching,
not a complete classical solve starting from the empty matching. The
implementation and primary-source details are recorded in
`deterministic_maximum_matching_verifier.md`.

The acceptance test makes finite branch outputs sound even if a small
parameter branch prematurely proposes a nonmaximum matching. It does
not prove that a fast branch succeeds within its claimed time. That
performance obligation is exactly (3).

## 4. One parameterized program and one bounded physical model

Use one finite implementation with an integer parameter `a`, not an
advised collection of unrelated programs. Its reduction factor,
recursion depth, arithmetic precision and other fixed-parameter
quantities are computed by the same explicit integer procedures.
Analytical constants such as `C_a` and unknown exceptional-size
thresholds are never supplied to that implementation as advice.

For branch index `t>=1`, choose `a=a_0+t`. Run that branch until it
proposes a matching, suspends, or fails a prerequisite. If it proposes
a matching, run the independent acceptance test as part of that same
branch. An invalid or nonmaximum proposal retires the branch. A
suspended or internally invalid branch cannot supply an answer.

Include branch zero, a classical deterministic exact polynomial-time
matching algorithm, with the same final acceptance interface. It
ensures termination for every finite input.

Each branch is an interruptible computation with private mutable
storage and a shared read-only compact input. All primitive loops,
memory initialization, output validation, large-integer arithmetic,
and the final verifier are charged to its own elementary steps.
No whole backend call or large allocation is an atomic free operation.

The classical branch has a fixed polynomial bound. This bounds the
total rounds and all actual memory allocated before some verified
answer is found by a fixed polynomial in `q`. One physical word-size
constant therefore suffices for real addresses and counters. Larger
logical integers use charged multiword arrays; logical address spaces
use dictionaries of touched cells. For each fixed branch, this
simulation adds only polynomial-logarithmic factors to (3).

## 5. Interleaving and the common exponent

At round `j=0,1,2,...`, give every unfinished branch `t<=j` up to
`2^(j-t)` elementary steps. Stop at the first independently accepted
answer. This is internal execution of one algorithm, not a recurring
or future external task.

Fix any branch `t` that needs `T_t(q)` steps including its final
verification. By round

\[
             j=t+\lceil\log_2\max\{1,T_t(q)\}\rceil
\]

it has received enough time. The sum of all branch allowances through
that round is at most a constant times `2^t(T_t(q)+1)`. Loop and
simulation overheads add only logarithmic factors. Thus the one
program competes with every fixed branch:

\[
 T(q)\le C_a 2^{O(a)}
      \bigl(q^{1+O(1/a)+o_a(1)}+q\alpha(q)+1\bigr)
      \operatorname{polylog}(q+2).                               \tag{4}
\]

All final-check work is already inside the interleaved branch budget.
A bad branch cannot block the other branches by requesting a long
global verification run.

For any fixed `epsilon>0`, choose in the analysis a sufficiently
large **fixed** branch so its absolute `O(1/a)` exponent is less than
`epsilon/3`. For every sufficiently large `q`, its `o_a(1)`, constants,
and all simulation logarithms fit the remaining exponent slack.
The same program consequently satisfies `T(q)<=q^(1+epsilon)` for
all sufficiently large inputs, for every positive epsilon.

This proves a common `q^(1+o(1))` envelope. If desired, take the
supremum of the excess logarithmic worst-case exponent over all
sizes at least `q` to obtain a nonincreasing envelope tending to
zero. The polynomial fallback makes that supremum finite. The
program never needs to compute or consult that envelope.

The full instruction, digit and memory accounting is in
`deterministic_uniformization_by_optimality_check.md`.

## 6. One cleanup preserves the additive input term

Read the input once, remove loops, coalesce parallel copies while
retaining one original edge ID, delete isolates, and compactly relabel
the surviving vertices and edges. This costs `O(n+m)` in the standard
word-RAM representation.

For a nonempty cleaned graph, `r<=2m_s`, so its compact size
`q=r+m_s` is `Theta(m_s)`. Run every parameter branch and every
acceptance test on this shared compact graph. Map the accepted edge
IDs back to original IDs once, after acceptance. This proves (1).
Repeated verification on the raw graph, with all its isolates and
duplicate copies, is unnecessary and would obscure the stronger
additive-input formulation.

The physical word length is chosen from the ORIGINAL input size,
as usual for that input's word-RAM model. Compact branch addresses
and arithmetic use only polynomially many words in `q`; original
edge IDs are passive single-word labels retained by the cleanup.
The possibly much larger raw input therefore does not introduce
repeated `log(n+m)`-factor work into the compact computation. An
original label is read or copied in one physical word operation;
branch dictionaries are charged by their compact record counts.

For (2), perform the elementary exact matching-size kernel first.
A maximal greedy matching gives a vertex cover `C` of size
`nu<=|C|<=2nu`. Keep all edges inside `C` and at most `|C|+1`
distinct outside neighbors per vertex of `C`. The replacement
argument in `matching_size_kernel_corollary.md` proves that this
kernel has exactly the original optimum and only
`O(min{m_s,nu^2})` edges. Compact it, run the portfolio and acceptance
test on that trusted exact-preserving kernel, and then map edge IDs
back. The kernel proof is independent of the fast numerical branch.

## 7. Scope of the conclusion

The candidate eliminates a fixed polynomial overhead in the
deterministic general-graph problem, rather than improving only a
regular, bipartite, approximate, or communication variant. Its
uniform exponent reaches the input-reading scale. A smaller fixed
polynomial exponent than one in the input size is unavailable for
an explicit worst-case input-reading task; remaining quantitative
improvements concern the subpolynomial factor, constants, and
implementation.

The final verifier guarantees correctness of an accepted output.
It cannot by itself certify the improved running time. If a hidden
error caused every fast branch to fail, the classical branch would
still return a maximum matching, but only its classical time bound
would remain justified. The near-linear claim must therefore be
read together with the complete carrier proof and all named
numerical/OAI dependencies, at the stated research-draft status.
