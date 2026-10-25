# Smaller explicit powers in the priced matching client

**Separate mathematical refinement, 24 October 2026.** This note leaves
the complete 14/15 composition and all frozen checkpoints unchanged.
It changes only the client's conservative accuracy and occurrence caps,
while retaining the already proved backend cap. It does not improve
the logarithmic exponent 14/15.

The proof uses the explicit inequalities in
[priced logarithmic steps](priced_logarithmic_steps_from_raw_cycles.md),
[near-feasible rounding and exact projection](near_feasible_rounding_and_exact_projection.md),
and [the 14/15 composition](quantitative_matching_14_15_composition.md).
The original client source is
[OAI Section 5](https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026).
The new choices below are justified by the reconstructed client proof;
they are not asserted to be the parameter values printed in that source.

## 1. Statement and parameters

Keep the master parameters and every numerical-backend construction
from the 14/15 composition. In particular, let

\[
 S=2^s,\qquad v=\lceil s/a\rceil,\qquad B=2^v,
 \qquad E_*\le B/4.
 \tag{1}
\]

The cap \(E_*\) bounds backend initialization per input record,
amortized updates and queries, exposed logs, occurrence multiplicity,
pieces, and inverse raw quality, with the complete lifetime interface.
Replace the old client choices by

\[
                 D_*=B,\qquad q=B^{-2}.
 \tag{2}
\]

Keep

\[
 \delta=S^{-1000},\qquad \varepsilon=S^{-3000},
 \qquad H_{\rm price}=S^{100}.
 \tag{3}
\]

Require \(B>8\). Since \(B\) is a power of two, this means
\(B\ge16\). Retain the existing magnitude, history, bit-length,
nominal-size and transaction guards. In particular retain
\(q\ge S^{-1}\) and \(D_*\le S^2\).

For every favorable fixed constant tuple in the 14/15 composition,
these choices eventually support the following conservative bounds:

\[
 \begin{split}
 T_{\rm projection}&\le (P+B)B^{10},\\
 T_{\rm top}&\le SB^{10},\\
 T_{\rm phase}&\le SB^{13},\\
 T_{\rm favorable\ branch}&\le SB^{15}.
 \end{split}
 \tag{4}
\]

Here the local projection parameter \(P\) is its input parent debt.
The same global recovery bound is \((M+B)B^{10}\) for an
all-expanded exchange graph with \(M\) records. Including the
fixed-share portfolio and its charged scheduling and verification,
\(O(SB^{20})\) is a safe complete allowance. All bounds are
eventual upper bounds for the same mathematical construction, not
finite-size runtime certificates derived from a guard alone.

## 2. Exactly which inequalities use the two parameters

The client proof uses the following conditions on \(q,D_*\):

\[
 0<q<1/100,\qquad q\ge S^{-1},\qquad
 D_*\le S^2,\qquad \frac1{4D_*}>2q.
 \tag{5}
\]

Its occurrence hypothesis is at most \(D_*/4\) vertices per
physical input slot, counting isolated and dormant exposed copies.
It needs inverse raw quality at most \(D_*\), and it can use
backend time, logs, and pieces at most \(D_*\). Equation (1)
supplies all these conditions with slack. No substitution into a
bare ratio oracle is being made: the complete occurrence, raw-length,
precision and lifetime interface remains necessary.

With (2), the nontrivial quality inequality in (5) is precisely

\[
                       \frac1{4B}>\frac2{B^2},
\]

which holds for \(B>8\). Also \(q\le1/256<1/100\).
The other guards hold eventually because \(v=o(s)\). For example
the retained guard \(B\le S^{1/20}\) already implies
\(q\ge S^{-1/10}\ge S^{-1}\).

There is no further use of the particular power 100 in the local
argument:

* Integer pricing uses \(q\ge S^{-1}\) to dominate its rounding
  error. The original \(H_{\rm price}\), price magnitudes and
  stale-price comparison remain valid.
* Strong-direction detection uses the last inequality in (5).
  A strong logical direction still has integer-priced port-lift ratio
  above \(1/4\); the raw answer therefore passes the unchanged
  acceptance threshold \(2q\).
* The dyadic step satisfies
  \(q/400\le\mu V/H_{\rm price}\le q/200\).
  It gives exact grid conservation, relative absolute motion below
  \(q/100\), and objective progress \(\Omega(q^2)\).
  Larger \(q\) within (5) does not invalidate positivity.
* Coordinate thresholds remain dyadic powers in
  \([qH_{\rm price}/(800D_*\ell_e),
     qH_{\rm price}/(400D_*\ell_e)]\).
  The stale-register estimate is still at most \(q/200\).
  Both signed and absolute counters, including dormant copies and
  retirement buckets, are treated exactly as before.
* Grid compatibility uses only \(q\ge S^{-1}\),
  \(D_*\le S^2\), and the unchanged price/traversal bounds.
  Thus \(\mu\) and the thresholds still exceed
  \(\varepsilon\) and are exact multiples of that grid.
* Pad service, boundary locks and top positivity repair use only
  the small relative tolerance \(q/100\). Their existing fixed
  margins remain valid. The tiny total pad violation follows from
  the independent polynomial history guard and \(\delta\),
  not from a factor \(B^{-100}\).

The source's original relation \(D=M^{10/a}\) served to instantiate
an occurrence/quality cap from its original backend. It is not used
algebraically by the drift, counter or positivity proof. Here it is
replaced by the explicit master cap (2), justified by (1). The old
nominal-size grid may be retained without changing this observation.

## 3. Priced-engine work with the smaller cap

Let \(J\) count accepted steps and let \(Q\) count requests
made by the owning client, including failed and LOW queries. Then
\(J\le Q\). Genuine numerical refresh and disable notifications
number \(O(D_*J)=O(BJ)\); they are not fresh uncharged motion.

Apply the explicit accounting from Section 12 of the priced-step note:

\[
\begin{split}
 T_{\rm priced}
 &\le O((M+Q+D_*J)E_*)\operatorname{poly}(s)\\
 &\quad+O((Q+D_*J)D_*)\operatorname{poly}(s)\\
 &\quad+O(Qp_c+D_*J)\operatorname{poly}(s)\\
 &\le (M+Q)B^2\operatorname{poly}(s).
\end{split}
\tag{6}
\]

The unspecified fixed polynomial factors also cover charged
multiword arithmetic and ordinary tree operations. In particular,
the full \(D_*^2J=B^2J\) copy-sweep term is retained. The
\(Qp_c\) term includes inspection of answers that return LOW.
No report or copy sweep has been declared constant-time.

## 4. Local projection and all-expanded recovery

The local objective range and its total insertion/lock losses remain
\(O((P+1)s)\) per threshold. Only the progress denominator changes.
Thus

\[
 J_{\rm loc}=O((P+1)B^4s)
 \tag{7}
\]

per threshold. At most \(O(s)\) thresholds and their exact
recovery calls add fixed polynomial factors in \(s\). Each genuine
notification causes constantly many client services. Such services
may discard old absolute-motion credit but do not create new credit.
Consequently, for the complete local call,

\[
 Q_{\rm loc}\le (P+1)B^5\operatorname{poly}(s).
 \tag{8}
\]

This is the same external-request versus motion-notification separation
as in the complete composition. It is not a circular inequality in
which every client service creates another factor \(D_*Q\).

The rounded nominal size is
\(M\le O((P+B)2^{2a^2})\). Substitution into (6) gives

\[
 T_{\rm numerical,loc}
 \le (P+B)2^{2a^2}B^7\operatorname{poly}(s).
 \tag{9}
\]

The near-feasible integral rounding, exact coordinate reads, final
ordinary residual searches and deduplicated union cost only
\((P+1)\operatorname{poly}(s)\) across these thresholds.
They invoke no additional exact-flow algorithm. Their correctness
proof uses total violation below one, the fixed scale 16 and the
strong-direction exclusion, all unchanged by (2).

For the 14/15 parameter choice, \(a^2=o(v)\), and every fixed
polynomial in \(a,s\) is \(2^{o(v)}\). Hence
\(2^{2a^2}\operatorname{poly}(a,s)=B^{o(1)}\).
Equation (9), all recovery work and constant factors therefore fit
the safe projection allowance \((P+B)B^{10}\).
The all-expanded construction has the identical proof with its
\(O(M)\)-record input in place of the local region. Its allowance
is \((M+B)B^{10}\).

## 5. Top work, additive reset sum and the gap driver

The structural objective-loss argument gives

\[
 J_{\rm top}=O(aSB^4s^2),\qquad
 Q_{\rm top}\le(aSs+B J_{\rm top})\operatorname{poly}(s).
 \tag{10}
\]

Using the old top lifetime allowance \(R_{\rm top}=SB\), its
rounded nominal size, and (6), all top initialization, steps, refreshes,
exact residual access and the final LOW query fit \(SB^{10}\).

The unchanged physical/debt proof gives \(\tau=O(aS)\) and

\[
 \sum_{j=2}^{a}\frac{\tau}{b_j}
       [(C+2)b_{j-1}+B]=O(a^3SB),
 \qquad b_j=B^{a-j},\quad C=a+1.
 \tag{11}
\]

Multiplying (11) once by the new projection factor \(B^{10}\)
gives \(O(a^3SB^{11})\), eventually at most \(SB^{12}\).
Sparse support application and persistent carrier normalization are
included. These costs are added across ledger levels, not exponentiated
through that hierarchy.

At level one there are \(O(aB+1)\) all-expanded resets. Their
total cost is

\[
 O(aB+1)(S+B)B^{10}\le SB^{12}
 \tag{12}
\]

eventually. Top work, the two reset categories, structural work,
initialization and final materialization together fit \(SB^{13}\)
per phase. The direct general-graph gap driver uses \(O(a\log S)\)
phases. That factor is \(B^{o(1)}\), so \(SB^{15}\) is a
safe complete favorable-branch allowance, including its final exact
matching verifier.

The same first-failure proof applies: the improved sharp counts are
smaller, while the positivity and nominal-region arguments still use
the old independent loose polynomial guards. Resource and source
quality hypotheses must be established on a favorable branch; the
final verifier does not supply its fast-time proof.

## 6. Uniform program and unchanged exponent

Keep the same enumeration of fixed constants and the same shared
compact original input. A fixed favorable branch still has a fixed
positive instruction share. Scheduling overhead is polynomial in the
logarithm of the executed instruction count and is absorbed into
\(SB^{20}\). Tiny graphs, malformed branches, and finite exceptional
sizes retain the classical fallback and exact acceptance verifier.

The resulting expression remains

\[
 O(n+m)+(m_s+1)\exp\!\left(
 O\!\left((\log(m_s+2))^{14/15}
          (\log\log(m_s+4))^{1/5}\right)\right).
\]

The optional exact matching-size kernel is unchanged. This refinement
reduces explicit conservative powers of \(B\) in the assembled
client proof; it supplies no additional exponent claim or new public
primitive.
