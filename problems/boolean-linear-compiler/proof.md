# Exact Boolean optimization by interval and slack compilation

The strongest local refinement is the [cardinality and coefficient-normalized compiler](manuscripts/cardinality-and-modal-interval-compilation.md). For each nonconstant row, subtract a most frequent coefficient on each exact cardinality layer. If <code class="math">d_i</code> is the resulting support, put <code class="math">\bar\kappa_i=\min\{W_i+1,d_i,\lfloor n/2\rfloor\}</code> and <code class="math">\bar Q=\sum_i\lceil\log_2\bar\kappa_i\rceil</code>. For <code class="math">0\le B\le\bar Q</code>, its time is

<!-- math-display: e3ef6f5197ea5deb5290743c
\mathrm{poly}(L)P_{\rm card}
2^{\alpha n+\bar Q-(1-\alpha)B},
-->
![Formula](../../assets/math/e3ef6f5197ea5deb5290743c.svg)

with the same backend space bound at <code class="math">n+B</code> variables. Here <code class="math">P_{\rm card}</code> is the maximum of one and the actual catalogue product over nontrivial cardinality layers. Original variables and rows are explicit, so their counts are at most <code class="math">L</code>. The original support-sized argument below remains an independent unconditioned lemma.

## 1. Unconditioned compiler theorem

The input has <code class="math">n</code> Boolean variables, signed binary integer equalities, and interval rows <code class="math">\ell_i\le a_i^\top x\le u_i</code>. Let <code class="math">L</code> be its binary length, <code class="math">s_i=&#124;\mathrm{supp}(a_i)&#124;</code>, and <code class="math">W_i=u_i-\ell_i</code>. Normalize one-sided rows against their attainable ranges and handle empty intervals and zero rows directly. Put
<!-- math-display: 972de2e59f303d81dcb6e4b2
\kappa_i=\min\{W_i+1,s_i\},\quad q_i=\lceil\log_2\kappa_i\rceil,\quad Q=\sum_iq_i.
-->
![Formula](../../assets/math/972de2e59f303d81dcb6e4b2.svg)
Assume a deterministic Subset Sum backend returns indexed witnesses in time <code class="math">\mathrm{poly}(L')2^{\alpha N}</code>, and, if supplied, writable space <code class="math">\mathrm{poly}(L')2^{\sigma N}</code>. For any integer <code class="math">0\le B\le Q</code>, the compiler gives
<!-- math-display: d10cc014ca3dc9c461ad85d1
T_B\le\mathrm{poly}(L)\left(\prod_i p_i\right)
2^{\alpha n+Q-(1-\alpha)B},\qquad
S_B\le\mathrm{poly}(L)2^{\sigma(n+B)},
-->
![Formula](../../assets/math/d10cc014ca3dc9c461ad85d1.svg)
where <code class="math">p_i\le2\lceil\log_2(W_i+1)\rceil+1</code>, and <code class="math">p_i=1</code> if <code class="math">W_i+1\le s_i</code>. Exact equalities contribute no slack parameter. Feasibility, indexed witnesses, linear optimization, and explicitly listed polynomial-size lexicographic optimization are supported.

## 2. Signed interval lemma

For a nonzero row with original support <code class="math">s\ge1</code>, stop when the current interval contains at most <code class="math">s</code> integers. Otherwise let <code class="math">t</code> be the number of odd current coefficients, set <code class="math">a'_j=\lfloor a_j/2\rfloor</code>, and put

<!-- math-display: 4ba1528586485df26fc79322
\ell'=\lceil\ell/2\rceil,\qquad u'=\lfloor(u-t)/2\rfloor.
-->
![Formula](../../assets/math/4ba1528586485df26fc79322.svg)

Emit the nonempty intervals

<!-- math-display: 44c54b36a771196f9a13db93
[\ell,\min\{u,2\ell'+t-2\}],\qquad
[\max\{\ell,2u'+2\},u]
-->
![Formula](../../assets/math/44c54b36a771196f9a13db93.svg)

using the current coefficient row. Recurse once with <code class="math">a'</code> on <code class="math">[\ell',u']</code> if it is nonempty. For every Boolean assignment, including for signed coefficients,

<!-- math-display: f977bde887a07ce20726ee7d
a^\top x=2(a')^\top x+\delta(x),\qquad
\delta(x)=\sum_{j:a_j\text{ odd}}x_j\in[0,t].
-->
![Formula](../../assets/math/f977bde887a07ce20726ee7d.svg)

Thus a recursive acceptance has original value between <code class="math">2\ell'\ge\ell</code> and <code class="math">2u'+t\le u</code>. Conversely, if a parent-feasible assignment has rounded sum below <code class="math">\ell'</code>, its original sum is at most <code class="math">2\ell'+t-2</code> and falls in the lower boundary. A rounded sum above <code class="math">u'</code> has original sum at least <code class="math">2u'+2</code> and falls in the upper boundary. When <code class="math">\ell'&gt;u'</code>, these two cases cover every assignment and no recursion is needed. Clipping keeps boundary acceptances inside the parent interval.

The lower boundary has at most <code class="math">2\ell'-\ell+t-1\le t</code> values; the upper has at most <code class="math">u-2u'-1\le t</code> values. When <code class="math">t=0</code>, both are empty. Every emitted interval therefore contains at most <code class="math">s</code> values, or at most <code class="math">W+1</code> if the initial row is already short. A recursive width is at most half its parent's width, so at most two emissions per halving and one terminal emission prove <code class="math">p_i\le2\lceil\log_2(W_i+1)\rceil+1</code>. The depth and all intermediate bit lengths are polynomial in the binary input size. A zero row is checked directly and removed before defining <code class="math">q_i</code>; a reversed interval is infeasible.

This proves exact disjunction for each original Boolean assignment. Boundary overlaps are harmless: they are counted among the catalogue's actual tests, and the construction has only one recursive child. The [complete proof](manuscripts/boolean-linear-optimization-compiler.md#2-signed-short-interval-catalogue) treats the empty-child and negative-floor cases explicitly. The [independent checker](verify/check_interval_compiler.py) also compares full compiled solution sets with the original systems.

## 3. Slack and branch count

Choose <code class="math">0\le b_i\le q_i</code> summing to <code class="math">B</code>. Split each catalogue interval into chunks of at most <code class="math">2^{b_i}</code> values. There are at most <code class="math">2^{q_i-b_i}</code> chunks, so the number of branch tuples is at most
<!-- math-display: c0c667f51df16b6635ad4f06
\left(\prod_i p_i\right)2^{Q-B}.
-->
![Formula](../../assets/math/c0c667f51df16b6635ad4f06.svg)
For a positive-width chunk <code class="math">[l,u]</code>, put <code class="math">w=u-l</code>, <code class="math">q=\lceil\log_2(w+1)\rceil\le b_i</code>. The <code class="math">q</code> weights
<!-- math-display: ea3f8367f7eff3b76c93ae6a
1,2,\ldots,2^{q-2},\quad w-(2^{q-1}-1)
-->
![Formula](../../assets/math/ea3f8367f7eff3b76c93ae6a.svg)
have subset sums exactly <code class="math">0,\ldots,w</code>. For <code class="math">q=1</code>, the initial list is empty. The powers cover the initial interval; the final shift overlaps or abuts it and ends at <code class="math">w</code>. Thus the chunk becomes one equality with at most <code class="math">b_i</code> Boolean slack variables. Different rows use different variables; width zero needs none. This is a witness reduction, not a parsimonious counting reduction.

## 4. Signed radix packing

For a branch with equations <code class="math">c_j^\top y=t_j</code> on <code class="math">N\le n+B</code> variables, use
<!-- math-display: c9e513a8905c5b3b78b246df
R=1+\max_j\left(\sum_k|c_{jk}|+|t_j|\right),\qquad
A_k=\sum_jc_{jk}R^j,\qquad T=\sum_jt_jR^j.
-->
![Formula](../../assets/math/c9e513a8905c5b3b78b246df.svg)
Handle the all-zero system directly; otherwise <code class="math">R\ge2</code>. The packed equation <code class="math">\sum_kA_ky_k=T</code> is equivalent to all branch equations. Indeed <code class="math">d_j=c_j^\top y-t_j</code> satisfies <code class="math">&#124;d_j&#124;&lt;R</code>. Reducing <code class="math">\sum_jd_jR^j=0</code> modulo <code class="math">R</code> forces <code class="math">d_0=0</code>; divide and repeat. This proof permits signed digits.

The packed bit length is polynomial in <code class="math">L</code>. Multiplying the branch bound by the backend cost at <code class="math">n+B</code> proves the time formula. Branches run sequentially with one backend workspace, proving the space formula. A witness is restricted to its original <code class="math">n</code> coordinates.

## 5. Optimization and backend conditions

Binary search over the polynomial-bit objective range uses polynomially many feasibility queries. Completely enumerate the short-target catalogue for the one added threshold row; its cost is polynomial and it adds no slack variables. Fix an optimum as an exact equality before treating the next lexicographic objective.

For a fixed number of interval rows, <code class="math">Q=O(\log n)</code> and <code class="math">\prod_i p_i</code> is polynomial in <code class="math">L</code>, so the backend's separate time and space interfaces transfer up to polynomial factors. A time-only backend supplies no new simultaneous space bound. Numerical runtimes use the full theorem and indexed-witness scope of the chosen backend; scalar exponent checks alone do not establish that separate theorem.

## 6. Cardinality and common-coefficient refinement

On the retained equality <code class="math">\sum_{j=1}^n x_j=k</code>, subtract a most frequent row coefficient <code class="math">c_i</code> and shift both endpoints by <code class="math">c_i k</code>. The transformed support is <code class="math">d_i=n-\max_c&#124;\{j:a_{ij}=c\}&#124;\le s_i</code>, and the interval width is unchanged. A constant row becomes the direct test <code class="math">\ell_i\le c_i k\le u_i</code>, without a logarithmic parameter.

If a current row has <code class="math">t</code> odd coefficients, signed floor gives a remainder in

<!-- math-display: ed191fb97c67de64773589d1
[A,D]=[\max\{0,k+t-n\},\min\{k,t\}],
\qquad D-A=\min\{k,n-k,t,n-t\}.
-->
![Formula](../../assets/math/ed191fb97c67de64773589d1.svg)

The safe child is <code class="math">[\lceil(\ell-A)/2\rceil,\lfloor(u-D)/2\rfloor]</code>. Its two clipped boundary intervals have at most <code class="math">D-A</code> values. Recursing only on that child yields the cap <code class="math">\kappa_i(k)=\min\{W_i+1,d_i,k,n-k\}</code> and the same logarithmic catalogue count. The [companion proof, Sections 2–4](manuscripts/cardinality-and-modal-interval-compilation.md#2-exact-coefficient-normalization-within-a-layer), includes empty children, negative common coefficients, constant parity remainders, overlapping boundaries and polynomial bit lengths.

Keep the cardinality equality on original variables, with zero slack coefficients, in the signed radix system. Set <code class="math">Q_k=\sum_i\lceil\log_2\kappa_i(k)\rceil</code> and <code class="math">B_k=\min\{B,Q_k\}</code>. Then <code class="math">Q_k-B_k\le\bar Q-B</code> and <code class="math">B_k\le B</code>, proving the displayed uniform time/space bound even when <code class="math">B&gt;Q_k</code> or <code class="math">\alpha&gt;1</code>. The layers <code class="math">k=0,n</code> and <code class="math">n\le1</code> are direct cases. Original equalities and objective values retain their original meaning; an objective threshold is centered only under the same guard and its short tests are enumerated with no additional slack variables.

## Complete proofs

[Unconditioned interval compiler, numerical instantiations, and primary source comparison](manuscripts/boolean-linear-optimization-compiler.md). The general signed interval-rounding method is inherited from Nederlof–van Leeuwen–van der Zwaan and Bansal–Garg–Nederlof–Vyas. The manuscript gives the complete support-sized boundary refinement and the short-interval/slack interpolation; it requires no further external theorem for either local step.

[Complete guarded and normalized compiler](manuscripts/cardinality-and-modal-interval-compilation.md), including its independent exact checks.

**Attribution:** icekylinx and GPT-6 Astra Pro.
