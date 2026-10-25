# Uniform deterministic exactness through a final optimality check

**Status.** A standard algorithmic composition, conditional only on the
eventual fixed-parameter running-time/correctness theorem for the proposed
carrier algorithm. It removes the need to prove that every unfinished or
small-input parameter branch has a sound internal LOW outcome. It does
not repair a failure of eventual correctness or of the claimed fast
running time in those branches.

## 1. A near-linear verifier for a proposed maximum matching

Let `G` be an arbitrary undirected general graph and let `M` be a
proposed matching. First check its edge identifiers and disjointness
of endpoints. This costs `O(n+m)` on an explicit input, or `O(n+|M|)`
once the shared input records have been indexed. Reject an invalid
list immediately.

For a valid matching, run **one** deterministic general-graph
augmenting-path search to exhaustion. Accept `M` exactly when no
augmenting path exists. Berge's criterion makes this an exact
optimality check. This is not a complete maximum-matching computation
starting from the empty matching.

An independent pre-2026 primary source is Gabow, *The Weighted
Matching Approach to Maximum Cardinality Matching*,
arXiv:1703.03998v1 (2017), Figures 1–2 and Sections 3 and 5:

<https://arxiv.org/abs/1703.03998v1>.

Its Phase 1 starts from the supplied matching, puts weight two on
matched edges and zero on the others, and runs a single Edmonds
search. Figure 2 includes the no-augmenting-path outcome. Section 5
proves a linear bound for this search with Gabow–Tarjan's 1985
incremental-tree set-union structure. Ordinary union-find gives the
conservative `O(n+m alpha(n))` bound used here. The initialization,
unsuccessful-search cutoff and compact-input accounting are stated
in [the classical verifier note](classical_matching_optimality_verifier.md).

A second primary source explicitly supplying the same interface is
Mehlhorn and Nobahari, *Gabow's O(sqrt(n)m) Maximum Cardinality
Matching Algorithm, Revisited*, arXiv:2603.22909v2, April 2026:

<https://arxiv.org/pdf/2603.22909>.

Its Part I pseudocode (Figure 3, printed page 7) is expressly a
boolean procedure: it returns true if an augmenting path exists
and false otherwise. Section 2.3 explains exhaustive detection of
the no-augmenting-path case and, optionally, construction of an
optimality certificate. Section 4, printed page 18, gives
`O(m alpha(n))`, or `O(m)` with the stronger union-find implementation,
per iteration. Part I alone suffices here. Handle isolated vertices
in an initial linear scan, giving the conservative verifier cost

    O(n + m alpha(n)) = (n+m)^(1+o(1)).

Either search can start with any supplied valid matching. The
initialization of its search structures depends on the currently
free vertices, not on a history of previous augmentations.

No optimality certificate needs to be included in a user-facing
checkpoint. This is an internal algorithmic acceptance test.

## 2. The fixed-parameter family needed for uniformity

Let `p=n+m`. Suppose one finite program, given an integer parameter
`t>=1`, executes the proposed matching algorithm with

    a=a0+t,    eta=1/(C a),

where `a0` and `C` are fixed literal integers, for example the
already used `a0=1000` and `C=10^6` in the conservative backup
backend. The other numerical parameters are computed by finite
integer arithmetic as prescribed in the backend construction.
For example, with power-of-two nominal size `M`, take

    k=2^ceil(log2(M)/(C a)),
    D=ceil(2 C a)+2,
    K_sp=ceil(2^(4D) C a).

Rounding `k` upward to a power of two changes only a constant factor.
These formulas are computations, not advice. A larger fixed literal
`C` could be chosen once if the explicit backend bookkeeping uses a
larger envelope. The fixed-branch time constants `C_a` that appear
in the analysis are never queried or supplied to the program.
Assume the
proved fixed-parameter statement:

> For every sufficiently large fixed `t`, on every sufficiently
> large input, this branch avoids prerequisite suspension, returns
> a maximum matching, and takes
> `T_t(p)=p^(1+O(1/a)+o_a(1))` elementary implementation steps.

The coefficient of `1/a` is absolute. Constants and the `o_a(1)`
rate may depend on the fixed parameter. No computable table of
the sufficiently-large input thresholds is assumed.

For finite exceptional inputs, a branch may suspend, run for a long
time, or propose a nonmaximum matching because a prerequisite was
not established. Its final answer is never accepted directly. Run
the verifier in Section 1 on its proposal, and count that work as
part of the same branch. If verification fails, retire the branch
without an answer. Every branch thus has unconditional output
soundness, even though its eventual-performance proof is
asymptotic.

An invalid internal arithmetic operation can likewise reject that
branch. Branches have separate mutable storage and share only the
read-only input. The verifier reads its own copy or private view of
the proposed edge list, so a rejected branch cannot alter another
branch's computation or the original graph.

Add branch zero, an ordinary deterministic exact polynomial-time
general matching algorithm. It always terminates correctly. Its
output can pass through the same verifier for a uniform interface.

## 3. One finite program competing with all fixed branches

Use instruction-level weighted interleaving. At round `j=0,1,2,...`,
give each unfinished branch `t=0,...,j` up to `2^(j-t)` elementary
implementation steps. A rejected or suspended branch remains
inactive. Stop at the first branch whose proposal passes the
optimality check.

The interleaving is part of the mathematical algorithm; it is not an
external automation or a future scheduled task.

The parameter family is one executable interpreter with `a` supplied
as an integer, rather than a nonuniform list of separately advised
programs. For example, `eta=1/(C a)`, the constant recursion depth,
and any large fixed distance-oracle parameter such as `K_sp` are
computed by the same integer-arithmetic subroutines in every branch.
Every imported constructive primitive is likewise the same finite
algorithm with its numerical parameters as input. No per-`a` table
of exceptional size thresholds is embedded in the program.

For a fixed branch `t` requiring `T` total steps, including its final
check, round

    j=t+ceil(log2(max(1,T)))

alone supplies it enough cumulative service. Total allowances
through that round are less than a constant times `2^t(T+1)`.
Starting branches and loop/control overhead add only logarithmic
factors. Hence this one program competes with every fixed branch
with a fixed multiplicative factor depending on that branch index.
Writing `a=a0+t` and absorbing the fixed-branch arithmetic constants,
the comparison can be stated as

    T_uniform(p) <= C_a 2^(O(a))
                    (T_a(p)+p alpha(p)+1) polylog(p+2).

The branch's validation and augmenting-path verifier are performed
within its own allocated instruction slices; they are not an
uninterruptible global check that could delay all other branches.

Every accepted answer is maximum by the verifier, and branch zero
guarantees termination. There are no random bits, probabilistic
error events, or seed searches in this composition.

## 4. Charged arithmetic, memory, and one physical word constant

An allotted step is one bounded physical machine instruction, not a
whole graph subroutine, arbitrary-size integer operation, memory
reservation, or backend initialization. Store each branch as a
coroutine with an instruction pointer and its private state.

Long logical integers use charged digit arrays. Logical address
spaces are represented by dictionaries of touched memory cells.
Allocate and initialize actual words one at a time. Computing a
large fixed-parameter quantity, constructing its recursive structure,
or writing its output can be interrupted inside the corresponding
finite loop. No branch obtains an enormous allocation atomically.

The fallback has a fixed polynomial instruction bound `F(p)` under
this ordinary finite-word implementation. Unless a verified answer
has already stopped the program, branch zero receives `2^j` steps
in round `j`, so it completes within `O(log p)` rounds. The total
actual instructions and allocations before then are polynomial in
`p`, with constants independent of the varying parameter branches.

Choose a physical word-size constant once, large enough for that
polynomial number of real memory addresses, input indices and
control counters. Logical values larger than a word remain digit
arrays. Thus the implementation does not assume that all varying
parameter values fit one word, and it has one fixed physical
word-RAM model.

For each fixed branch, the added dictionary/digit-array costs are
polylogarithmic or already included in its word-arithmetic proof.
The persistent carrier's address-to-word simulation composes with
this wrapper with further polynomial-logarithmic overhead only.

## 5. The common near-linear exponent

Fix any `epsilon>0`. In the analysis, choose one sufficiently large
fixed branch index `t` so that its absolute `O(1/a)` exponent is
less than `epsilon/3`. For all sufficiently large `p`, its
`o_a(1)`, the verifier's inverse-Ackermann factor, fixed constants,
and all logarithmic overheads fit the remaining exponent slack.
The single interleaved program therefore has

    T(p)<=p^(1+epsilon)

for every sufficiently large input, uniformly over all graphs of
that size. The program itself does not choose `t` as a function of
the input based on an unknown asymptotic threshold.

Since the same program has this property for every positive
`epsilon`, its worst-case running time is `p^(1+o(1))`. A common
nonincreasing exponent envelope can be defined exactly as in the
OAI uniformization proof by taking the supremum of the excess
logarithmic running-time exponent over inputs of size at least
`p`. The polynomial fallback makes that supremum finite, and
competition with every fixed branch makes it tend to zero.

This is a uniform asymptotic conclusion, with no explicit practical
convergence rate. The fixed-epsilon version remains the cleaner
quantitative statement when a particular exponent is desired.

## 6. Shared cleanup and the additive input-reading bound

For an input with explicit integer vertex identifiers, read its
`n+m` records once, discard self-loops, merge parallel copies while
retaining one original edge witness, and remove isolated vertices.
Endpoint counting/radix sorting gives deterministic `O(n+m)` cleanup
under the stated word-RAM input model. Let the cleaned simple
nonisolated graph have `r` vertices and `m_s` edges. If `m_s=0`,
return the empty matching. Otherwise

    r<=2m_s,       q=r+m_s=Theta(m_s).

Renumber its vertices and edges densely and retain one shared
read-only mapping to original edge identifiers. Run the entire
portfolio, candidate validation and augmenting-path verification
on this cleaned graph. A candidate branch does not rescan all raw
isolates or duplicate input occurrences. Its verifier costs
`O(q alpha(q))`, and its successful fixed-parameter computation
uses the parameter `q` (or its linear-size subcubic reduction).

After a cleaned matching passes verification, map its edge IDs
back once. Removing loops, merging parallel edges and removing
isolates preserves maximum matching cardinality, and the retained
witness map preserves every selected original edge. Therefore the
overall bound sharpens to

    O(n+m) + m_s^(1+o(1)).

The case `m_s=0` is covered by the initial linear scan. Original
identifiers may require `O(log(n+m))` bits even when `q` is tiny;
they are used only in shared cleanup and final output mapping.
The branch graph itself has dense `O(log q)`-bit identifiers.

An exact witness-preserving kernel can likewise be computed once
before the portfolio, with its own separately proved preprocessing
bound. Run verification on the kernel graph and lift the accepted
matching through the kernel's exact decoder. Uniformization then
adds only the near-linear term in kernel size; it does not silently
make the kernel's own preprocessing free or linear.

## 7. What the verifier does not prove

The verifier prevents an incorrect finite branch from publishing an
incorrect maximum matching. It does **not** establish that the
carrier algorithm passes verification in near-linear time for
large inputs. That still requires the complete static/dynamic
carrier proof, source matching/projection invariants, deterministic
raw-cycle backend, and their fixed-parameter running-time bounds.

In particular, a hidden structural or backend error could make all
fast branches fail verification, leaving only the classical
polynomial fallback. The proposed improved time theorem must
continue to state its constructive theorem dependencies and its
research-draft status.
