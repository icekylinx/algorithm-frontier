# A numerical client independent of the ledger radix

**Separate mathematical simplification, 24 October 2026.** The ledger
radix need not determine numerical accuracy or occurrence thresholds.
This note proves the numerical part of that separation. The structural
choice $a=s$, $B_{\rm ledger}=2$ is proved separately in
[the binary-ledger note](binary-ledger-hierarchy-and-decoupled-parameters.md).
Existing complete 14/15 and earlier frozen constructions are unchanged.

The explicit proofs used here are
[priced logarithmic steps](priced-logarithmic-steps-from-raw-cycles.md),
[near-feasible rounding and exact projection](near-feasible-rounding-and-exact-projection.md),
and [the degree-reset backend](distance-degree-reset-candidate.md).
The original numerical source is
[OAI Section 5](https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026).
We use its reconstructed proof with a different parameter interface;
we do not claim that its printed fixed-parameter statement already
contains the choices below.

## 1. A direct master-scale numerical contract

Fix $S=2^s$. Assume one deterministic raw backend, with master
parameter $U=2s$, has a computable cap $E=E_*(2s)\ge1$.
On every actual numerical root of size at most $S^2$, with
positive integral lengths and integral gradients of magnitude at most
$S^{1200}$, the cap bounds:

* initialization work per actual input record;
* amortized edits, queries and complete exposed representation logs;
* occurrence multiplicity, including isolated and dormant exposed copies;
* answer-piece count and inverse raw approximation quality;
* complete retirement and the required polynomial master histories.

The record lifetime, signed/absolute counter, query transaction and
real-loop interfaces remain those in the existing numerical proof.
A ratio-only oracle does not suffice. The cap is a proved performance
and quality hypothesis on a favorable branch, not a conclusion drawn
from its final matching verifier.

Define $\mathrm{pow2ceil}(x)$ to be the smallest power
of two at least $x$, and set

$$
D=\mathrm{pow2ceil}(\max\{16,4E\}),\qquad
 q=\frac1{16D}.
 \tag{1}
$$

Then $4E\le D\le16E$. Retain

$$
\delta=S^{-1000},\qquad\varepsilon=S^{-3000},\qquad
 H_{\rm price}=S^{100}.
 \tag{2}
$$

For a logical lifetime allowance $R$, choose simply

$$
M=\mathrm{pow2ceil}(16(R+2)).
 \tag{3}
$$

There is no divisibility-by-$2a^2$ requirement. The client keeps
its existing degree-three port paths: a logical endpoint insertion
uses a fresh port, while repricing retains its existing endpoint
ports. Thus actual resident records are bounded by this local
allowance; the choice of $M$ does not allocate $S$ or
$S^2$ records for a tiny local problem.

Check $M\le S^2$, $q\ge S^{-1}$, and $D\le S^2$,
as well as the unchanged descriptor, argument, grid, lifetime and
history guards. If $E=S^{o(1)}$, then (1) gives the last two
checks eventually. All parameters are exact integers or dyadic
rationals computed by finite integer arithmetic.

This parameter choice has no feedback loop. Compute the backend cap
from master $2s$, its fixed root-price bound, and the structural
local capacity before choosing $D,q$. Root prices are bounded
using the fixed $\delta,\varepsilon$ and argument envelopes,
independently of $q$. Numerical repricing retains endpoint slots,
so the additional notifications affect only the already declared
polynomial operation horizon, not the logical lifetime size $R$.
The guarded $D\le S^2$ still puts that enlarged history well
inside the backend's master lifespan. Nothing in the definition of
$E$ is silently enlarged after (1).

## 2. Generalized priced-step lemma

With the contract above, the priced client retains all of its
correctness properties:

1. LOW is impossible in the presence of a nonzero circulation
   $d$ with
   $g^Td\ge\tfrac12\sum_e\lambda_e|d_e|$.
2. An accepted step is an exact $\varepsilon$-grid circulation,
   preserves positivity through every partial application, has total
   relative absolute motion at most $q/100$, and increases
   the objective by $\Omega(q^2)$.
3. Settled registers have relative error at most $q/100$.
   Genuine refresh and disable reports number $O(D)$ per
   accepted step, apart from explicit client settings.

Here is why no old relationship between the ledger parameters and
$M,D,q$ is needed. The proof's numerical inequalities are

$$
0<q<1/100,\qquad q\ge S^{-1},\qquad D\le S^2,
 \qquad\frac1{4D}>2q.
 \tag{4}
$$

Equation (1) gives $q\le1/256$ and
$2q=1/(8D)<1/(4D)$. It also gives the required occurrence
bound $E\le D/4$, and raw quality at least $1/D$.

At an exact anchor, prices remain
$\ell_e=\lceil H_{\rm price}\lambda_e\rceil$ and
$\gamma_e=\mathrm{round}(H_{\rm price}g_e)$.
The same argument and weight bounds give
$\ell_e\ge S^{80}$ and prices below $S^{1122}$,
within the direct $S^{1200}$ backend limit. The old inequality
$S\le M^a$ was only a way to translate these prices into
the original local bound $M^{1200a}$. That translation is
unnecessary with the explicit master contract.

A logical circulation's degree-three port lift adds at most
$2M\sum_e|d_e|$ connector length. Since $M\le S^2$
and real prices are at least $S^{80}$, a strong logical
direction still has integer-priced lifted ratio above $1/4$.
The raw backend and (4) imply that it passes the unchanged threshold
$|\gamma^Tc|\ge2qV$.

Choose the step power of two from

$$
\frac q{400}\le\frac{\mu V}{H_{\rm price}}
 \le\frac q{200},
 \tag{5}
$$

and choose each coordinate's drift threshold from

$$
\frac{qH_{\rm price}}{800D\ell_e}
 \le\theta_e\le
 \frac{qH_{\rm price}}{400D\ell_e}.
 \tag{6}
$$

The raw traversal bound, rather than cancellation in the final
circulation, proves partial positivity and the $\Omega(q^2)$
progress. Threshold settlement gives error at most $q/200$.
All dormant copies and retirement buckets remain included. A report
consumes at least $q/(800D)$ units of raw priced motion, while
a step creates at most $q/200$; this proves the $O(D)$
report bound independently of the size of $q$.

The $\mu$- and $\theta_e$-grid proofs use only
$q\ge S^{-1}$, $D\le S^2$, and the unchanged price
and traversal bounds. They remain far above $\varepsilon$.
No coordinatewise rounding of a direction is introduced. Pad service,
boundary expansion locks and top positivity repairs use only the
fixed small relative margin $q/100$. Their tiny total violation
uses $\delta$ and the independent polynomial history guard.

Consequently $R+B\le S^{1+2/a}$,
$D=M^{10/a}$, and the old $2a^2$ nominal exponent
rounding have no independent role after (3)--(4) and the explicit
root-price limit are supplied. In particular this is a direct proof
with master caps, not an invocation of a fixed-$a$ asymptotic
statement at an unproved growing value of $a$.

## 3. Work before collapsing the step count into the request count

Let $J$ be accepted steps and let $Q$ count external
requests by the owning client, including failed/LOW queries and exact
point requests. Internal numerical refreshes are a separate
$O(DJ)$ category. The explicit cost is

$$
\begin{split}
 T_{\rm priced}
 &\le O((M+Q+DJ)E)\mathrm{poly}(s)\\
 &\quad+O((Q+DJ)D)\mathrm{poly}(s)\\
 &\quad+O(Qp_c+DJ)\mathrm{poly}(s)\\
 &\le O(MD+QD+D^2J)\mathrm{poly}(s).
\end{split}
\tag{7}
$$

The initial occurrence records, complete signed and absolute motion,
representation retirement, $D^2J$ full-copy sweeps, and raw
inspection of unsuccessful queries are all included. Maintaining
$J$ separately avoids the unnecessarily weaker bound
$(M+Q)D^2$. All arithmetic and dynamic-tree operations use
charged finite-word work; the fixed polynomial includes their
ordinary bit and identifier overhead.

## 4. Local and global exact recovery

For a local threshold test with parent debt $P$, the objective
range plus total insertion and lock losses is $O((P+1)s)$.
Equation (1) gives $q^{-2}=256D^2$, so

$$
J_{\rm loc}=O((P+1)D^2s)
 \tag{8}
$$

per threshold. Across $O(s)$ thresholds and their checked
recoveries, this is $(P+1)D^2\mathrm{poly}(s)$.
Client services per genuine numerical notification are constant in
number up to ordinary identifier work. Reanchoring cannot create new
absolute-motion credit. Thus

$$
Q_{\rm loc}=O(P+1+DJ_{\rm loc})\mathrm{poly}(s)
            =(P+1)D^3\mathrm{poly}(s).
 \tag{9}
$$

The local graph only grows during a test. Fewer than
$1000(P+1)$ ordinary arcs are born. An arc contributes one
logical edge, two endpoint insertions, and at most two new logical
vertices; the return arc and terminals add constant records.
Descriptor/lock changes do not create ports. Hence the explicit
allowance

$$
R_{\rm loc}=8192(P+1)
 \tag{10}
$$

covers the lifetime count, and (3) gives $M=O(P+1)$.
Substitute (8)--(10) into (7):

$$
T_{\rm projection}
             \le (P+1)D^4\mathrm{poly}(s).
 \tag{11}
$$

Near-feasible integral cycle rounding, exact reads, cut checks and
ordinary residual searches add only
$(P+1)D\mathrm{poly}(s)$. There is no new static
max-flow call. The fixed scale 16, return-weight comparison, total
violation below one and exact true-flow/optimistic-cut recovery are
unchanged. All residual searches omit the numerical return arc.

The all-expanded exchange graph has $O(N_0)$ records on an
input state of size $N_0$. Repeating the same reasoning gives

$$
T_{\rm global}
             \le (N_0+1)D^4\mathrm{poly}(s).
 \tag{12}
$$

The terminal preprocessing and magnitude assumptions of that theorem
remain in force. The matching use has only polynomial-master
capacities, so no separate general-capacity reduction is needed.

## 5. Top client and admissible lifetime sizes

For the binary-ledger choice $a=s$, structural objective losses
are $O(aSs^2)$, while each step gains $\Omega(D^{-2})$.
Thus

$$
J_{\rm top}=S D^2\mathrm{poly}(s),\qquad
 Q_{\rm top}=S D^3\mathrm{poly}(s).
 \tag{13}
$$

Top logical topology births and retargetings are
$O(aS\log S)$ by the physical movement bound. The fixed
allowance

$$
R_{\rm top}=S(s+1)^{10}
 \tag{14}
$$

covers them eventually and gives $M=S\mathrm{poly}(s)$
in (3). It is below $S^2$ eventually. Equation (7) therefore
gives

$$
T_{\rm top}=S D^4\mathrm{poly}(s).
 \tag{15}
$$

For higher projections the structural bound is
$P\le(s+3)b_{j-1}\le(s+3)S/2$, so (10) also gives
$M<S^2$ eventually. Level-one global recovery has only
$O(S)$ actual records. These are local capacities: no repeated
master-sized initialization is hidden in (11).

The former nominal-size condition would give only $4S$ when
$a=s$; (14) need not satisfy it. Its replacement is the
explicit $M\le S^2$ master interface, whose proof was given
above. This distinction is necessary and is not an omitted guard.

## 6. Complete conditional consequence and uniformity

The binary-ledger proof gives total higher-reset volume
$O(s^3S)$, $O(s)$ global resets per phase, polynomial
structural work in $s$, and $O(s^2)$ phases. Combining
these facts with (11), (12), and (15) yields

$$
T_{\rm complete}
              =S D^4\mathrm{poly}(s)
              =S E^4\mathrm{poly}(s).
 \tag{16}
$$

This includes final exact matching verification. The source-specific
favorable branch still needs its independent primitive, recurrence
and quality proofs. The first-failure argument retains the loose
polynomial magnitude/history guards; with $E=S^{o(1)}$, all
sharp counts in (8)--(16) are $S^{1+o(1)}$ and satisfy those
guards eventually. Polynomial floors such as $C=s+1$ keep
all client fields within the same $O(s)$-bit master envelope.

For the degree-reset construction, enumerate only its fixed backend
constants $(c_C,c_E)$. Compute $E_*$, then $D,q$
by (1). A further outer balancing constant $c_B$ is unnecessary.
Keep the fixed-share classical fallback and branch-local verification.
Every actual word operation, including computing a cap that is too
large, is interruptible and charged to its branch. Some fixed favorable
pair succeeds beyond one fixed threshold. Its share penalty is a
constant; scheduling contributes a further fixed polynomial in $s$,
already allowed in (16). Shared compact cleanup preserves the additive
$O(n+m)$ input term.

With the proved degree-reset cap

$$
E_*(2s)=\exp\!\left(O(s^{14/15}(\log(s+4))^{1/5})\right),
$$

(16) has the same 14/15 logarithmic exponent. For this explicit
family, $E_*$ eventually dominates every fixed polynomial in
$s$; after collecting all such factors, $SE_*^5$ is a
safe eventual complete allowance. The simplification removes the
outer radix/accuracy balance; it is not a claim of an exponent below
14/15.
