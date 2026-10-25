# Verification note

**Curated source path:** `sources/checkpoint-o/public_apsp_joint_retuning_independent_audit.md`

The source audit follows.

# Independent source audit of the public APSP joint retuning

**Audit date:** 25 October 2026.  
**Object:** `public_apsp_joint_retuning_audit.md`, including its conservative
\(q^2rh\) small-instance work allowance and its explicit work-budget
substitution for the public batching scheduler.

## 1. Conclusion and scope

The joint public construction supports the following **derived public
baseline**:

\[
\begin{aligned}
 \text{amortized update factor}
   &\le \exp O(U^{6/7}h^{1/7}),\\
 \log(\text{distance stretch})
   &\le O(U^{5/7}h^{2/7}),\\
 \text{numerical distance query time}&\le \operatorname{poly}(U),
 \qquad U=\log(N+4),\quad h=\Theta(\log(U+4)).
\end{aligned}
\]

This is a recomposition and reanalysis of named public algorithms, not a
printed theorem with these parameters. It retains the public provider's
ambient-path-length loss. The audit does not claim a globally optimal
public APSP tradeoff, an output-sensitive arbitrary-path oracle, or
worst-case update time for the full recursive construction.

The principal potentially dangerous substitution is valid: the work used
to construct a deterministic static sparsifier can be charged once as
\(F\), while its output length, selected-edge inventory, and selected-edge
recourse are controlled by a separate \(\Gamma\). The two quantities must
not be identified again inside the recursion.

## 2. Source-level checks

The following checks use the original primary sources.

| Interface | Source inspected | Finding |
|---|---|---|
| Parameterized deterministic cut player / balanced cut | [CGLNPS20, arXiv:1910.08025v2](https://arxiv.org/html/1910.08025v2), Theorems 1.6 and 5.1 | The \(r^2h\) loss is construction work. The conductance/cut quality has only \(rh\). Small inputs require the stated parameter cutoff or a smaller effective \(r\). |
| Decremental expander path hierarchy | [CS21, arXiv:2009.08479v1](https://arxiv.org/html/2009.08479v1), Theorem 3.9, Algorithms 1--3, Lemmas 3.10--3.11 | The theorem permits arbitrary \(q>1\). Construction work enters one stage cost. The number of child stages is controlled by deletions, pruning, and embedding congestion; it does not depend on the construction work. |
| Deterministic static metric sparsifier | [vdB et al.23, arXiv:2309.16629v1](https://arxiv.org/html/2309.16629v1), Algorithm 4, Claims 8.7 and 8.9, proof of Theorem 8.1 | Both routing passes have only logarithmically many rounds. Each successful path call embeds a previously unembedded edge. Neither the round count nor path-call count includes construction work. |
| Touched-set repair | [CKL et al.22, arXiv:2203.00671v1](https://arxiv.org/pdf/2203.00671v1), Algorithm 1, Claims 5.7--5.8, Lemma 5.9 | Projected demand inventory depends on touched vertices and previous congestion; selected output inventory depends on touched vertices and static sparsity. The static construction work is not itself an inventory. |
| Local selected-degree cleanup | [KMG23, arXiv:2311.06402v1](https://arxiv.org/pdf/2311.06402v1), Claims 3.17--3.18 and proof of Theorem 3.1 | The cleanup potential and pile-splitting charge use the number of selected-edge changes. Replacing static construction work by a larger bound changes the paid time per cleanup call, not the amount of potential added by that call. |
| Public scheduler and richer edits | KMG23, paragraphs immediately before Theorem 3.7 | The source explicitly imports batching deamortization, forwarded vertex splits, direct retention of insertions, and length bucketing. The retuning uses this named scheduler interface, with its work budget rescaled along with the provider work. |
| Recursive numerical queries | KMG23, Algorithm 6 and Claim 4.4 | One pair descends per level. The base answer is a table lookup after base maintenance has been paid, not a shortest-path computation during the query. |

## 3. Growing parameters in the CS hierarchy

Put

\[
 \phi^{-1}=2^{O(rh)},\qquad
 F_r=2^{O(U/r+r^2h)}.
\]

CS Lemma 3.10 separates a level-\(i\) stage into construction of its
embedded terminal expander, incidence-list construction, ES-tree
maintenance, pruning, and deletion callbacks. The work of the first
item can be enlarged to \(F_r\) without changing the objects produced
by the other items. Thus a stage costs

\[
 m^{(i+1)/q}F_r 2^{O(rh)}.
\]

The child-stage ratio in the same proof is bounded by the parent deletion
allowance multiplied by embedding congestion and pruning loss, divided
by the child deletion allowance. It is

\[
 m^{1/q}2^{O(rh)},
\]

independently of \(F_r\). Multiplication down the \(q\) levels therefore
gives

\[
 m\,2^{O(U/q+U/r+r^2h+qrh)}.
\]

CS Lemma 3.11 separately gives

\[
 L_i\le O(U/\phi)(1+L_{i-1}),
 \qquad L_q\le 2^{O(qrh)}.
\]

There is no hidden constant-\(q\) restriction in this multiplication.
Factors polynomial in \(q\le U\) are covered by polynomial logarithms.

### Local cutoff and fallback

Using the hierarchy only when

\[
 \log(m+2)\ge Cq^2rh
\]

is conservative and sufficient. The consecutive-size ratio
\(m^{1/q}\) then dominates the primitive quality losses and the minimum
terminal size required by the cut player. In particular it pays for
rounding deletion allowances to positive integers and leaves enough
surviving intermediate terminals. This is an actual-local-size test;
small graphs are not padded to the global inventory.

For smaller calls, a direct BFS on the surviving pruned expander has
path length \(O(U/\phi)\), although its work can be
\(2^{O(q^2rh)}\). It is legitimate to charge the latter to construction
work because the static client below makes only a bounded number of
path calls. A generation can retire all remaining vertices once its
deletion count reaches the pruning theorem's permitted fraction of its
initial edge count: the entire original volume is then
\(O(t/\phi)\). Thus no claim of persistent expansion beyond that
theorem's deletion range is needed.

The settled-root and bottom-pruning completions in the main note are
necessary when reading CS Algorithms 1--3 literally. They add only root
deletions, already charged pruning deletions, and constant generation
bookkeeping. They do not introduce a faster routing primitive.

### Loopless degree bands and weighted witnesses

The subsequent loopless implementation in Section 2.3 of the main note
also passes. At band \(i\), each explicitly chosen low-degree vertex
causes fewer than \(\phi2^i/C_b\) requests and is chosen at most once.
Thus \(t_i<(\phi2^i/C_b)n\). Expander pruning, including retirement
on the first excess request, moves at most \(O(t_i/\phi)\) initial
edges to the residual graph. Together with the quarter-budget initial
crossing edges, this halves the edge-inventory bound. Starting at an
average-degree scale gives \(\sum_i2^in=O(m)\); it does not allocate
\(n\Delta\) artificial loops. This is an explicit implementation of
the degree-band interface, using public decomposition and pruning,
rather than a literal invocation of Appendix B's loop-adding pseudocode.

For the port witness, the loopless component gives
\(w_v\le\sum_{u\ne v}w_u\). Rounding preserves the needed half-port
inequality:

\[
 \lceil w_v\rceil
 \le\Bigl\lceil\sum_{u\ne v}w_u\Bigr\rceil
 \le\sum_{u\ne v}\lceil w_u\rceil.
\]

Each fiber consequently has at most half the ports. Constant edge
expansion of the bounded-degree port graph supplies a degree lower
bound for each contracted fiber and a cut lower bound for every union
of fibers. Quotient degree is at most the original port degree, so
discarding internal edges preserves constant conductance after the
fixed rescaling. The resulting degrees are between \(w_v\) and
\(O(w_v)\), and construction uses \(O(\sum_vw_v)\) ports. No
maximum-degree padding or higher output-quality exponent is introduced.

## 4. Why the static client pays the fallback only once

In vdB Algorithm 4, the first routing pass calls `GetPath` only for a
witness edge whose embedding is still empty; afterwards that edge is
permanently embedded. The second pass has the same property for demand
edges. Hence the number of successful queries is at most

\[
 |E(W)|+|E(J)|
   \le |E(J)|\,2^{O(rh)}\operatorname{poly}(U),
\]

after removing isolated vertices. Claims 8.7 and 8.9 show that only
\(O(U)\) fresh path structures are needed per component. The proofs
charge weighted volume and congestion; they never charge the time used
to construct those structures. Their input volume, witness volume, and
inverse conductance are polynomially bounded in the master inventory,
so the logarithmic number of rounds remains \(O(U)\).

The first pass explicitly enumerates ambient paths. That contributes
the factor \(L_0+1\), as in the main note, but introduces no power of
\(F_r\). These observations establish the safe separated provider

\[
 \log\Gamma=O(qrh),\qquad
 \log F=O(U/q+U/r+r^2h+q^2rh).
\]

The source's composed ambient congestion bound is
\(\Gamma L_0(C_0+\Delta(J))\). Its \(L_0\) is retained throughout
this audit.

## 5. Repair, selected recourse, and the work budget

CKL Algorithm 1 projects affected demands to a touched set \(S\).
The old surviving legs contribute the previous length and congestion;
the new middle uses the static provider. Keeping its ambient length
factor gives

\[
 \mathcal L_j\le\Gamma^{O(j+1)},\qquad
 \mathcal C_j\le\Delta\Gamma^{O((j+1)^2)}.
\]

The projected demand count is at most \(O(|S|\mathcal C_{j-1})\),
whereas selected output count is only
\(|S|\Gamma\operatorname{poly}(U)\). Therefore a complete repair job
costs at most

\[
 |S|\Delta F\Gamma^{O(K^2)}\operatorname{poly}(U),
\]

and the selected-edge recourse per native edit is
\(2^{O(U/K)}\Gamma\operatorname{poly}(U)\). The larger construction
bound is not multiplied once per repair level: each repair job calls
the static provider once, on its actual projected demand inventory.

The printed restriction involving \(1/6\) accompanies the fixed source
choice of \(\Gamma\). The proofs just inspected allow a different
uniform quality bound, provided its entire work, length, and congestion
envelope is paid. The retuning uses \(K^2\log\Gamma=o(U)\) at the
chosen point and a clock whose effective depth never exceeds the
actual logarithmic instance size by more than an endpoint convention.

For KMG's selected-degree cleanup, the potential increase is proportional
to newly selected edges, not the computation that found them. Its
initialization bound must be enlarged if necessary to pay every cleanup
operation using the new work envelope. The main note does this; it does
not reuse the source's smaller printed initialization expression.

The scheduler requires special care. The legitimate substitution is to
multiply **both** each static job's construction budget and the amount
of work assigned to it per logical edit by \(F\). Then the same logical
deadline and catchup lag are valid. Intermediate construction records
remain private; only selected output is published. Slowing the routine
while retaining the old budget would not justify the recourse claim.
This audit imports the public scheduler assertion immediately preceding
KMG Theorem 3.7; it does not assert a new scheduler theorem from a
black-box amortized-time guarantee alone.

## 6. Final balance and fair comparison

After standard degree reduction at each recursive boundary, the local
child inventory/edit factor satisfies

\[
 \log P=O(U/K+g+h),\qquad g=\log\Gamma.
\]

For \(x=\log k\) sufficiently larger than \(\log P\), the recursive
depth is \(d=O(U/x)\). Paying full child initialization and retirement
in the native phase charge yields

\[
 B_{\rm pub}=O(x+f+K^2g+d(U/K+g+h)+h),
 \qquad a_{\rm pub}=O(dKg+dh).
\]

Set \(q=r=t\), \(K=t^2\), \(x=\Theta(U/t)\), and
\(t=\Theta((U/h)^{1/7})\). Then

\[
 g=O(t^2h),\quad f=O(U/t+t^3h),\quad
 K^2g=O(t^6h)=O(U/t),\quad dKg=O(t^5h).
\]

The extra fallback term \(q^2rh=t^3h\) is below the dominant
\(U/t=t^6h\). This proves the displayed \(6/7\) work and \(5/7\)
stretch exponents.

For an equal-stretch comparison, the checkpoint's separated provider
has \(B=O(U/t+t^3h)\) and \(a=O(t^4h)\). Taking
\(t=\Theta((U/h)^{5/28})\) gives

\[
 B=O(U^{23/28}h^{5/28}),\qquad
 a=O(U^{5/7}h^{2/7}).
\]

Thus its advantage over this newly strengthened public baseline is
\(23/28\) versus \(6/7=24/28\) at the same displayed stretch scale.
The older \(11/14\) point remains valid at its larger displayed stretch;
neither numerical-APSP rate is a general-graph matching rate.

## 7. Nonuniform positive-budget check

Section 6 of `same_stretch_apsp_comparison_and_root_audit.md` also
passes as an optimization statement about its explicitly defined
positive-charge model. On the initial size range
\(u_i\in[U/2,U]\), its assumptions imply
\(j=\Omega(U/B)\), \(q_ir_i=\Omega(U^2/B^2)\), and
\(K_i=O(B^{3/2}/(U\sqrt h))\). Inserting these into
\(\sum_i u_i/K_i\lesssim B\) gives
\(B^7=\Omega(U^6h)\). Cauchy's inequality independently gives
\(\sum_iK_i=\Omega(j^2U/B)=\Omega(U^3/B^3)\); hence the
charged metric sum obeys
\(A_{\rm charge}=\Omega(U^5h/B^5)\).

The nominal-shrink assumption is necessary and is stated in that
section: a hierarchy whose total initial-range nominal shrink is
\(\Omega(U)\), with every \(x_i=O(B)\), has the required number
of levels. If \(B\) is already a constant fraction of \(U\), the
sublinear regime of interest has been left and the work floor is
immediate. For the intended range the calculation yields

\[
 B\gtrsim\max\{U^{6/7}h^{1/7},\ U(h/A)^{1/5}\}.
\]

This conclusion requires the model to charge the displayed provider,
repair, and metric terms as positive amounts. An implementation might
admit a different analysis or avoid a charge, so this is neither an
APSP lower bound nor an algorithmic lower bound inferred from an
upper-bound formula.



---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
