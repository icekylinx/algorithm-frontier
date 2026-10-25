# Increment X-SS: Wider recursive lookups improve the deterministic Subset Sum exponent

**English rough draft for external review.** This is an incremental change to
the fast-time proof imported at Algorithm Frontier commit
`37b31138bf102a83d9efb2cbe44437eec45ae3c2`, specifically
`sources/subset-sum/combined-proof.md`, Part I. Its underlying Subset Sum
source commit is `1ecb2e2eb43963a6ca9a4a5f4c6a208990c3b22b`.

Attribution: Yilin Liu and GPT-6 Astra Pro.

## 1. Outcome and dependency boundary

The repository's deterministic general-input time exponent is

\[
 E_{\rm old}=\frac{149809813343531}{301754962128739}
 =0.496461805587\ldots.
\]

Changing two explicitly specified circuit families and rebalancing the full
input algorithm gives the smaller exponent

\[
 \boxed{E_{\rm new}=
 \frac{149809813343531}{301825962128739}
 =0.4963450204447026\ldots.}
 \tag{SS1}
\]

The decrease is approximately \(0.0001167851\) per input coordinate.

**Incremental theorem.** With the exact circuit compilation and deterministic
representation lemmas of the repository's Part I, there is a uniform
deterministic algorithm for Subset Sum on arbitrary signed binary integers
that decides every instance and returns an indexed witness on YES instances
in

\[
 C_{\rm new}+\operatorname{poly}(n,L)2^{E_{\rm new}n}
 \tag{SS2}
\]

bit operations. Here \(L\) is the full binary encoding length and
\(C_{\rm new}\) is a finite input-independent circuit-construction cost.
The polynomial degrees and constants are fixed. This theorem makes no
simultaneous small-space claim and does not inherit the separate low-space
algorithm's space exponent.

The new work changes the actual menu of exact signed circuits. The full
prefix-profile inequality and all input-dependent cost lines are checked
below. The earlier circuit identities, compiler, canonical-prefix selector,
collision-energy oracle, residue covers, exact-key semantics, and witness
recovery remain dependencies from the cited repository proof; this increment
does not independently reprove that entire manuscript or its historical
priority claims.

## 2. The two changes to the circuit menu

Keep the matching types

\[
 s=\frac{11}{100},\quad t=\frac9{20},\quad
 a=\frac{13}{250},\quad b=\frac{29}{500},\quad a+b=s.
 \tag{SS3}
\]

Write

\[
 H(c,x)=c\log_2c-x\log_2x-(c-x)\log_2(c-x),
\]

with the continuous endpoint conventions.

**Changed recursive family.** Set

\[
 \rho=\frac{13}{5},\qquad
 \gamma_1=\frac{13}{25}=0.52.
 \tag{SS4}
\]

The repository used \(\gamma_1=0.47\) for this value of \(\rho\).
The first inner lookup is now \(C_1=\gamma_1\beta\), where
\(\beta=a+\rho(m-a)\). Keep the second-level rule

\[
 C_2=\max\{C_1/2,C_1-w_1\}.
 \tag{SS5}
\]

Use the same exact two-orientation containment factorization and the same
pooled-trace coefficients as in Sections I.2.5–I.2.7 of the baseline.
No positive cover is substituted for a signed identity.

For every outer color, \(\beta-z\le C_1\): it is enough to check
\(z=m\), where the worst ratio occurs at \(m=s\), and
\(\beta(s)-s=0.0928<0.52\beta(s)=0.105456\). Thus the enlarged
lookup is valid over the entire required color domain, not just the
numerically active colors.

**Added direct family.** Add the ordinary signed outer lookup circuit with

\[
                            \rho=4.
 \tag{SS6}
\]

Here \(\beta\le a+4b=0.284<t<1-t\). The original direct occurrence
counting, distinct-query-gate bound, and rational correction therefore apply
on their stated full domains. This family improves the high-\(\tau\) tail
after the recursive central interval has improved.

Both choices are fixed rational parameters. The usual rounding to integer
lookup sizes contributes \(o(1)\) to the normalized profile. The finite
compiler may choose a larger fixed admissible seed and still use the same
total allowance \(\zeta=10^{-6}\).

## 3. New full-domain contact inequalities

For the changed recursive family, the complete colored profile has the
following contacts:

| Family | \(\tau\) | Certified upper profile |
|---|---:|---:|
| \(\rho=13/5,\gamma_1=13/25\), two levels with pooled traces | \(0.46\) | \(0.17266\) |
| The same exact family and the same routing | \(0.52\) | \(0.18388\) |
| Direct \(\rho=4\) | \(0.60\) | \(0.19414\) |
| The same direct family | \(0.76\) | \(0.20552\) |

Each decimal is an exact rational. The two contacts in one family concern
one fixed circuit construction, not circuits chosen separately for each
color after observing the input. Consequently convexity gives the straight
contact chord throughout the associated \(\tau\)-interval.

Here are the domains and expressions needed to reproduce the new
inequalities. Throughout,

\[
 a\le m\le s,\quad m\le z\le\beta,
 \qquad
 L_0=\max\{0,H(t,z)+H(1-t,\beta-z)
                       -H(1-m,\beta-m)\}.
 \tag{SS7}
\]

For the recursive family put

\[
 C_1=\gamma_1\beta,\quad Q_1=\beta-z,\quad D_1=C_1-Q_1,
\]

\[
 \max\{Q_1,C_1-m\}\le w_1\le\min\{\beta-m,C_1\}.
 \tag{SS8}
\]

The first inner occurrence exponent is

\[
 F_{1,\rm raw}=H(\beta-m,w_1)+H(m,C_1-w_1)-H(z,D_1).
 \tag{SS9}
\]

On the push branch \(w_1\le C_1/2\), use the upper expression

\[
 \tau L_0+(1-\tau)H(b,m-a)
 +(1-\tau)\max\{0,F_{1,\rm raw}\}
 +\tau H(D_1,w_1-Q_1).
 \tag{SS10}
\]

On the recursive branch, write

\[
 v=w_1-C_1/2\ge0,\quad C_2=C_1/2,\quad Q_2=C_2-v,
\]

\[
 \max\{0,\beta-z-C_2,C_2-m\}\le v
 \le\min\{C_2,\beta-m-C_2\},
 \tag{SS11}
\]

\[
 \max\{Q_2,C_2-Q_1\}\le w_2\le\min\{D_1,C_2\}.
 \tag{SS12}
\]

The second-level contributions are

\[
 F_2=\max\{0,H(D_1,w_2)+H(Q_1,C_2-w_2)-H(C_2+v,v)\},
 \qquad G_2=H(v,w_2-Q_2).
 \tag{SS13}
\]

The relevant profile is bounded by

\[
 \tau L_0+(1-\tau)H(b,m-a)
 +(1-\tau)\max\{0,F_{1,\rm raw}-\delta\}
 +\tau F_2+(1-\tau)G_2.
 \tag{SS14}
\]

Here the safe constant trace correction on a box is exactly the one from
the baseline. For a box
\([m_0,m_1]\times[z_0,z_1]\times[v_0,v_1]\), define

\[
 \begin{aligned}
 D_{\min}&=(1-\gamma_1/2)\beta(m_0)-m_0-v_1,\\
 D_{\max}&=(1-\gamma_1/2)\beta(m_1)-m_1-v_0,\\
 d_q&=m_0-a-C_2(m_0)+v_0,\\
 m_q&=m_0-C_2(m_0)+v_0,\\
 w_r&=C_2(m_0)+v_0-s+m_0,\\
 r_{\max}&=s-m_0,\qquad d_{\min}=m_0-a.
 \end{aligned}
 \tag{SS15}
\]

If \(\beta(m_0)\ge s\), all required factors are nonnegative, and

\[
 d_qw_r\ge r_{\max}D_{\max},\qquad
 r_{\max}m_1D_{\max}
 \le d_{\min}m_q(1-s-D_{\max}),
 \tag{SS16}
\]

take

\[
 \delta=\frac75\frac{(s-m_1)D_{\min}}{1-m_0}.
 \tag{SS17}
\]

Otherwise take \(\delta=0\). The subtraction remains inside the
nonnegative maximum. In particular, no branch is discarded merely because
its correction conditions fail.

For the direct family \(\rho=4\), the expression is

\[
 \tau L_0+(1-\tau)
 \left[H(b,m-a)+H(\beta-m,z-m)-\delta_{\rm dir}\right].
 \tag{SS18}
\]

On a rectangle with \(m_0>a\) and
\(\rho(m_0-a)^2\ge b(z_1-a)\), use
\(\delta_{\rm dir}=(7/5)(s-m_1)\max\{0,z_0-m_1\}\);
else use zero. This is the existing distinct-query-gate correction.

## 4. How the contact bounds were certified

The proof is the Gibbs-line and concavity method already used in the
baseline, with a fresh complete domain subdivision for the new parameters.
For any rational \(0<p<1\),

\[
 H(x,y)\le-y\log_2p-(x-y)\log_2(1-p).
 \tag{SS19}
\]

Use these affine upper bounds for every positive entropy. Use lower linear
chords or lower bilinear vertex interpolants for each negative entropy.
The latter are valid by joint concavity. If a relaxed box has an invalid
vertex for \(H(z,D_1)\), use the safe lower bound zero for that entire
negative entropy on the box, rather than evaluating outside its domain.

In the recursive branch, maximize the Gibbs affine expression in \(w_2\)
using a fixed globally valid endpoint from (SS12), selected according to
the sign of its coefficient. Handle both branches of the maximum defining
\(F_2\). In the push branch do the same for \(w_1\), imposing
\(w_1\le C_1/2\). The resulting upper functions are separately convex in
the remaining box coordinates. Their maxima occur at the four or eight
box vertices. Both branches of every nonnegative maximum are retained.

For the recursive region, start with

\[
 \begin{aligned}
 m&\in\left[\max\left\{a,
 \frac{(1-\gamma_1/2)a(\rho-1)}{(1-\gamma_1/2)\rho-1}\right\},s\right],\\
 z&\in[a,\beta(s)],\\
 v&\in[0,\min\{C_2(s),\beta(s)-s-C_2(s)\}].
 \end{aligned}
 \tag{SS20}
\]

Before evaluating a box, tighten its endpoints by the necessary inequalities
(SS11), as in baseline equation (118). Bisect the coordinate with greatest
value among \(3(m_1-m_0),z_1-z_0,2(v_1-v_0)\), using that tie order.
For the push branch and the direct family use the analogous two-coordinate
rule with \(3(m_1-m_0)\) and \(z_1-z_0\). Discard only empty boxes.

Rational Gibbs probabilities were selected as multiples of \(10^{-12}\),
clamped to \([10^{-9},1-10^{-9}]\). Approximate stationary points serve
only to propose these rationals; they are not used in accepting a box.
All acceptance comparisons use exact rational arithmetic and outward
logarithm enclosures. One explicit enclosure is obtained by normalizing
\(x\) into \([1,2]\), putting \(z=(x-1)/(x+1)\), and evaluating

\[
 \ln x=2\sum_{j=0}^{31}\frac{z^{2j+1}}{2j+1}+\mathcal R,
 \qquad 0\le\mathcal R<2^{-100}.
 \tag{SS21}
\]

The final bound follows from \(z\le1/3\). Each product and division can
be rounded outward on the \(2^{-120}\) grid. Divide by an independently
enclosed \(\ln2\), then round base-two logarithms outward to the
\(10^{-14}\) grid. These operations produce rational upper and lower
bounds throughout; no floating-point acceptance is used.

The complete terminating subdivisions had the following accepted nonempty
leaf counts:

| New family and contact | Push leaves | Recursive leaves | Direct leaves |
|---|---:|---:|---:|
| \((\rho,\gamma_1,\tau)=(2.6,.52,.46)\) | 47 | 16,718 | — |
| \((2.6,.52,.52)\) | 47 | 13,149 | — |
| \((\rho,\tau)=(4,.60)\) | — | — | 166 |
| \((4,.76)\) | — | — | 206 |

For orientation, the smallest accepted slack was greater than
\(1.2\cdot10^{-7}\) in the first recursive contact and greater than
\(4.5\cdot10^{-8}\) in the second. The push contacts had positive
slack as well. The leaf counts describe the performed calculation, not an
additional mathematical assumption or a substitute for the inequalities.

## 5. The complete replacement profile

Use the following chords. Entries marked “old” use certified baseline
contacts or a restriction of an old contact chord. The new circuit parameters
are fixed for the whole row.

| Interval | Exact family | Left bound | Right bound |
|---|---|---:|---:|
| \([.24,.40]\) | old \(\rho=1.3,\gamma_1=.47\) | .12004 | .16082 |
| \([.40,.45]\) | old \(\rho=1.7,\gamma_1=.47\) | .15966 | .17177 |
| \([.45,.46]\) | restriction of old \(\rho=2,\gamma_1=.47\) chord | .17078 | .173028 |
| \([.46,.52]\) | **new \(\rho=2.6,\gamma_1=.52\)** | **.17266** | **.18388** |
| \([.52,.54]\) | old \(\rho=2.8,\gamma_1=.50\) | .18347 | .18689 |
| \([.54,.57]\) | old \(\rho=3.1,\gamma_1=.54\) | .18616 | .19091 |
| \([.57,.60]\) | restriction of old direct \(\rho=3.3\) chord | .19179 | .195594 |
| \([.60,.76]\) | **new direct \(\rho=4\)** | **.19414** | **.20552** |

The value .173028 is the exact restriction of the old chord at .46.
The value .195594 rounds upward its old chord value at .60. For
\([0,.24]\) retain \(\tau d_{\rm push}\), with
\(d_{\rm push}\le.49973033201029\). For \([.76,1]\) retain
\((1-\tau)d_{\rm pull}\), with \(d_{\rm pull}\le.88282502240658\).
Retain both one-sided values at each junction.

Call this complete piecewise upper profile \(f\). Let

\[
 D_c=h(t)-h(s)-H(s,a),\qquad
 .38309469039628\le D_c\le.38309469039633,
 \qquad K=\frac{875}{3042}.
\]

For \(u=f(\tau),v=f(1-\tau)\), set

\[
 \Delta=(2\tau-1)D_c+u-v.
\]

The full scalar bound is

\[
 \boxed{u+v+K\Delta^2\le S_{\rm new},\qquad
 S_{\rm new}=.36049.}
 \tag{SS22}
\]

All chord values are below \(1/4\), so the expression is increasing in
each of \(u,v\) exactly as in the baseline. On a common refinement
interval it is convex in \(\tau\) and in \(D_c\). It is therefore
sufficient to check the rational endpoints

\[
 0,.24,.40,.43,.45,.46,.48,.52,.54,.55,.57,.60,.76,1,
 \tag{SS23}
\]

including all applicable one-sided values and both endpoints for \(D_c\).
There are 76 resulting rational comparisons. Their maximum is

\[
 \frac{24369014753102946965693821968703}
      {67600000000000000000000000000000}
 =.3604883839216412\ldots < .36049,
 \tag{SS24}
\]

with margin

\[
 \frac{109246897053034306178031297}
      {67600000000000000000000000000000}>1.6\cdot10^{-6}.
\]

The maximum occurs at the old direct-contact side of \(\tau=.57\),
or its reflection \(.43\). Thus the previously binding central contacts
have genuinely ceased to be the bottleneck.

## 6. Transfer through unequal cores and the compiler

Let \(R=h(t)\), \(Q=h(s)+H(s,a)\), and let \(q\) be the
row-oriented core fraction. For the mixed typed matrix the endpoint objective
is

\[
 \Phi(q,\tau)
 =q[\tau R+(1-\tau)Q+u]
 +(1-q)[(1-\tau)R+\tau Q+v].
\]

Writing \(x=q-1/2\), inequality (SS22) and completing the square give

\[
 \Phi(q,\tau)\le
 \frac{R+Q+S_{\rm new}}2
 +\frac{1521}{875}(q-1/2)^2.
 \tag{SS25}
\]

The same entropy curvature inequality as before gives

\[
 \frac{1521}{875}(q-1/2)^2
 \le1-h(s+(1-2s)q).
 \tag{SS26}
\]

Thus the complete unequal-core profile hypothesis of the repository compiler
holds with \(S_*\) replaced by \(S_{\rm new}\). Keep
\(\zeta=10^{-6}\). The signed first-level identities, coefficient
aggregation, tensor rebalancing, grouping, actual gate names, and
output-sensitive incidence enumeration all apply to the added finite menu.
In particular, the claim does not pass from a favorable isolated inner
state directly to Subset Sum.

## 7. New gain, block size, and every outer cost line

The canonical typed support exponent and the auxiliary scalar bounds remain

\[
 \begin{aligned}
 D&\le D_U=\frac{49809813343531}{10^{14}},\\
 \alpha&\le\alpha_U=\frac{138991595816454}{10^{14}},\\
 \eta&\le\eta_U=\frac{559334743723}{10^{14}},
 \qquad d_0=\frac1{50}.
 \end{aligned}
 \tag{SS27}
\]

The old safe gain lower bound was
\(g_{L,\rm old}=2135335441677/(2\cdot10^{14})\).
Only the term \(-S_*/2\) changes, so a new safe gain is

\[
 g_L=g_{L,\rm old}+rac{.3612-.36049}{2}
     =\frac{2206335441677}{200000000000000}.
 \tag{SS28}
\]

Choose

\[
 \mu=\frac1{2(1+D_U+g_L)}
     =\frac{100000000000000}{301825962128739},
 \qquad M=500\left\lfloor\frac{\mu n}{500}\right\rfloor.
 \tag{SS29}
\]

Then \(3\mu<1\), \(g_L<d_0\), and the two binding input-dependent
rates coincide:

\[
 \mu(1+D_U)=\frac12-\mu g_L=E_{\rm new}.
 \tag{SS30}
\]

The whole outer ledger, with decimals rounded upward, is:

| Operation | Rate per input coordinate |
|---|---:|
| Retained signed-circuit incidences and witness recovery | \(E_{\rm new}\) |
| Canonical outputs and complete residue-cover state | \(E_{\rm new}\) |
| All candidate-modulus energy evaluations | \(<.471560525\) |
| Selectors and shared witness preprocessing | \(<.339796266\) |
| Repeated prefix lookups | \(<.348275771\) |
| Repeated outside lookups | \(<.344674295\) |
| Direct cyclic convolution and common shifts | \(<.338536025\) |
| High-deficiency dictionary matching | \(<.493373665\) |
| Dictionary and canonical-layer preparation | \(<.331316761\) |

These follow by exact substitution into the baseline's complete cost
expressions:

\[
 \begin{gathered}
 \mu(1+D_U),\quad
 \mu(d_0+\eta_U+\alpha_U+D_U/64),\quad
 \mu(1+d_0+\eta_U),\\
 \mu[1+2(d_0+\eta_U)],\quad
 (1-\mu)/2+\mu(d_0+2\eta_U),\quad
 \mu(d_0+\eta_U+2D_U),\\
 1/2-d_0\mu,\quad 1/2-\mu g_L,\quad \mu.
 \end{gathered}
 \tag{SS31}
\]

The high-deficiency fallback, modulus candidates, local cover repetitions,
residue state, witness-trie preprocessing, actual integer keys, and
coefficient bit lengths have not been omitted. Rounding \(M\) changes
logarithmic costs by \(O(1)\). The fixed finite small-input range is
handled exhaustively, with polynomial dependence on \(L\). This proves
the stated incremental theorem under the same complete reduction and
uniformity contract as the original theorem.

## 8. Scope and immediate continuation

This is a general-input deterministic exponent improvement within the
repository's representation-and-circuit framework. It is not a practical
implementation claim: the original finite input-independent circuit search
remains, with no useful numerical bound on its startup constant supplied
here. The unrelated matching exponent \(4/5\) is not being changed.

The current binding profile junctions are now the old contacts near
\(\tau=.43,.46,.54,.57\), rather than the replaced central family. Further
improvement requires moving those junctions or proving additional contacts
and repeating the whole profile and outer ledger. A favorable numerical
contact alone is not a further theorem.
