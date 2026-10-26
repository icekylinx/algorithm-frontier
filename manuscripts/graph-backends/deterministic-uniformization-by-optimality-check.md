# Uniform deterministic optimization from independently checked branches

## 1. Uniformization theorem

Fix an explicit input representation of size $q\ge2$ and a deterministic physical computation model. Assume the following interfaces.

1. A deterministic verifier accepts exactly the valid optimum outputs and runs in $V(q)=q^{1+o(1)}$ time.
2. A single finite program accepts an integer branch index $t\ge1$. For every sufficiently large fixed $t$, it proposes an optimum on every sufficiently large input, uniformly over inputs of that size, in
   $$
T_t(q)\le c_t q^{1+\eta_t+\rho_t(q)},
   \qquad \eta_t\longrightarrow0,\quad \rho_t(q)\longrightarrow0.
$$
   Here $c_t$ and the convergence rate may depend on the fixed branch. All arithmetic, allocation, and output work is included.
3. A deterministic exact fallback has a fixed polynomial time bound in the same model.

Branches need not be sound on exceptional sizes. They may suspend, reject an internal precondition, or propose an incorrect answer; they cannot bypass the independent verifier. The eventual-performance assumption in item 2 is a hypothesis, not a consequence of output verification.

**Theorem 1.** Under these interfaces, one deterministic finite program always returns an optimum and has worst-case running time $q^{1+o(1)}$. It requires no computable table of the exceptional thresholds or the constants $c_t$.

**Proof.** Give each branch private mutable state and shared read-only input. A proposed output is copied or frozen before its verifier runs. Charge verification to that branch. Retire a branch after a rejected proposal or an explicit suspension. Branch zero runs the exact fallback and its verifier.

In round $j=0,1,\ldots$, give each unfinished branch $0\le t\le j$ at most $2^{j-t}$ elementary steps. Stop at the first accepted output. For a fixed branch needing $T$ steps, including verification, round
$$
J=t+\lceil\log_2\max\{1,T\}\rceil
$$
alone provides enough service unless an earlier accepted branch has already terminated the algorithm. The total allowances through that round satisfy
$$
\sum_{j=0}^{J}\sum_{u=0}^{j}2^{j-u}
<2^{J+2}
\le 8\cdot2^t\max\{1,T\}.
$$
Loop and coroutine bookkeeping introduce at most polynomial logarithmic overhead. In particular, for every fixed successful branch,
$$
T_{\mathrm{unif}}(q)
\le C_t\bigl(T_t(q)+V(q)+1\bigr)\mathrm{polylog}(q+2).
$$

Every accepted output is optimum. The fallback receives enough service to terminate on every input, so the program always terminates.

Fix $\epsilon>0$ in the analysis. Choose a sufficiently large fixed $t$ with $\eta_t<\epsilon/3$. For all sufficiently large $q$, the term $\rho_t(q)$, fixed constants, verifier cost, and simulation logarithms fit the remaining exponent slack. Thus the same program satisfies $T_{\mathrm{unif}}(q)\le q^{1+\epsilon}$ for all sufficiently large inputs. Since this holds for every $\epsilon>0$, its worst-case time is $q^{1+o(1)}$. The program never needs to determine which fixed branch proves a given exponent. ∎

One may define a nonincreasing exponent envelope by taking the supremum of the excess logarithmic worst-case exponent over all input sizes at least $q$. The polynomial fallback bounds that supremum, and the last paragraph makes it tend to zero. This gives no explicit practical convergence rate.

## 2. Charged implementation and one physical word constant

An elementary allotted step is a bounded physical instruction. A graph subroutine, large integer operation, memory reservation, or complete verifier call is not one atomic step.

Represent each branch by an instruction pointer and private state. Long integers are digit arrays; sparse logical address spaces are dictionaries of touched cells. Allocation and initialization write actual words one at a time. Every primitive loop is interruptible, including construction of a large parameter-dependent object.

If the fallback uses at most $q^C$ steps for a fixed $C$, it completes within $O(\log q)$ rounds. The total service, control work, and actual allocations before that completion are polynomial in $q$, independently of the other branches' indices. Therefore one fixed physical word-size constant suffices for actual addresses and counters. Larger logical values remain multiword objects. This argument does not assume that an arbitrarily large logical parameter fits in one word.

The fixed-branch hypothesis must already charge its own arithmetic. A conventional dictionary or persistent-memory simulation may add polynomial logarithmic factors; it cannot hide a parameter-dependent exponential operation as one step.

## 3. Maximum-matching verifier

For an undirected graph and a proposed matching $M$, first validate the edge identifiers and endpoint disjointness. Then run one deterministic augmenting-path search from $M$. By Berge's criterion, accept exactly when no augmenting path exists.

The [classical verifier manuscript](classical-matching-optimality-verifier.md) specifies the interface and initialization from an arbitrary supplied matching. Its primary inputs are Gabow, [The Weighted Matching Approach to Maximum Cardinality Matching](https://arxiv.org/abs/1703.03998v1), Sections 3 and 5, and Mehlhorn–Nobahari, [Gabow's Maximum Cardinality Matching Algorithm, Revisited](https://arxiv.org/pdf/2603.22909v2), Part I. The conservative bound is
$$
O(n+m\alpha(n)).
$$
This is one search relative to the proposed matching, not a complete solve from the empty matching.

The search is independent of the candidate's ledger, numerical certificates, and internal LOW decisions. Invalid data or a failed arithmetic precondition retires the candidate. The verifier itself remains an ordinary charged branch computation.

## 4. Fixed-parameter matching specialization

Suppose one finite implementation accepts $a=a_0+t$ and, for every sufficiently large fixed $a$, eventually returns an exact maximum matching in
$$
q^{1+O(1/a)+o_a(1)}
$$
time, with an absolute coefficient in $O(1/a)$. Its numerical parameters must be computed by finite arithmetic from $a$ and the input size. Neither a branch-dependent asymptotic constant nor an unknown exceptional-size cutoff is executable advice.

Theorem 1 then gives one deterministic $q^{1+o(1)}$ matching algorithm. For the carrier construction, the required fast-branch statement includes the complete raw-cycle realization, persistent ledger operations, exact projection, and phase accounting. The [current matching proof](../../problems/general-matching/proof.md), particularly its explicit Contract R, records that dependency. This uniformization theorem does not discharge it.

A flaw in every fast branch would leave the fallback's exactness and polynomial termination intact, but would invalidate the improved running-time conclusion.

## 5. Shared input cleanup and exact kernels

Read the original graph once. In the stated word-RAM representation, dense endpoint counting/radix sorting removes loops, coalesces parallel edges while retaining an original witness identifier, and discards isolated vertices in $O(n+m)$ time.

If $m_s$ distinct nonloop edges remain, the nonempty compact graph has at most $2m_s$ vertices and size $q=\Theta(m_s)$. Run every branch and verifier on this shared compact graph. Translate only the accepted matching back to original identifiers. The resulting conditional bound is
$$
O(n+m)+(m_s+1)^{1+o(1)}.
$$
The empty graph is settled during cleanup.

An exact witness-preserving kernel can likewise be computed once before the portfolio. Verification takes place on that trusted kernel, and its exact decoder lifts the accepted optimum. The kernel's own preprocessing is charged separately; uniformization does not improve it for free.
