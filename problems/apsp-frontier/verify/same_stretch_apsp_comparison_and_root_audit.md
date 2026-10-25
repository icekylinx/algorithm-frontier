# Verification note

**Curated source path:** `sources/checkpoint-o/same_stretch_apsp_comparison_and_root_audit.md`

The source audit follows.

# A stronger public APSP comparison at exactly the same stretch scale

**Root mathematical and source audit, 25 October 2026.**

The public joint rederivation in **public_apsp_joint_retuning_audit.md**
changes the comparison with the numerical APSP construction. It is
stronger than simply retuning the fixed local theorem. This note
checks the separated budgets, records the conservative small-instance
implementation, and compares the two constructions at the same
asymptotic stretch scale.

## 1. Two distinct provider interfaces

Write \(U=\log(N+4)\) and \(h=\log(U+4)\). The reconstructed public
metric provider has a cut-player parameter \(r\) and a separate
expander-path depth \(q\). Its output quality and construction work
can be bounded by

\[
 g_{\rm pub}=O(qrh),\qquad
 f_{\rm pub}=O(U/q+U/r+r^2h+q^2rh).
 \tag{1}
\]

The last term is a conservative work allowance for small local
expander instances. It is not inserted into output path length.
The public ambient congestion factor still includes the length
of the input embedding.

The current research provider has the different interface

\[
 g_{\rm new}=O((p+r)h),\qquad
 f_{\rm new}=O(U/p+U/r+r^2h+(p+r)h).
 \tag{2}
\]

Its normalized ambient composition removes the input-path-length
multiplier. Neither of these two changes is silently attributed
to the public primitive.

## 2. Checks on the public reconstruction

I read the actual stage and path recurrences in CS21, Lemmas
3.10--3.11, rather than using its single packaged overhead
parameter. The work for one stage includes the terminal-expander
construction cost. The number of child stages depends on deleted
edges, embedding congestion, and pruning. Thus the construction
cost occurs once when stage work is multiplied by the stage count.
The path recurrence uses the embedding path length instead.

The conservative implementation activates the \(q\)-level structure
only when the local logarithmic size is at least \(Cq^2rh\).
Then the smallest nominal size gap is at least
\(\exp(Cqrh)\), which covers the cut-player cutoff, degree losses,
and positive deletion budgets. Smaller components use pruning
and direct BFS. Their path length still follows from expansion;
their larger search work is charged in \(f_{\rm pub}\). The two
static sparsifier passes make only an input-linear number of
path queries, times fixed powers of the output factors, so this
fallback does not turn a work factor into a quality factor.

The degree-band adapter must also be stated explicitly. The
literal artificial-self-loop version cannot simply be passed to
a loopless cut primitive or materialized at an \(n\Delta\) cost.
The actual-size loopless construction starts at average degree,
uses public decomposition and pruning, and moves a geometrically
shrinking residual to the next band. Weighted witnesses use
explicit ports of total size proportional to their total weight.
These elementary domain adapters are part of the reconstruction,
not a claim that the source pseudocode already supplies them.

I also checked CKL Section 5.1, Claims 5.7--5.8 and Lemma 5.9.
With the public ambient length factor retained, its repair
recurrences give path length \(\exp O(Kg_{\rm pub})\) and
congestion \(\exp O(K^2g_{\rm pub})\). The selected-edge output
count is controlled separately. A static work factor multiplying
one reconstruction job does not appear in its selected output.

The use of standard public deamortization is a work-budget
substitution: increase the computation allotted to a job by the
same factor as its work, retaining its logical update deadline
and catch-up schedule. Candidate outputs and their switch times
are not postponed to obtain the improved recourse bound. This
uses the public scheduler and its ordinary resumable-computation
model; it does not claim a worst-case update bound for the whole
APSP hierarchy.

The relevant primary sources are
[CS21](https://arxiv.org/abs/2009.08479),
[CKL22](https://arxiv.org/abs/2203.00671),
[the deterministic static replacement](https://arxiv.org/abs/2309.16629),
and [KMG](https://arxiv.org/abs/2311.06402).
The detailed reconstruction gives their exact theorem and
algorithm locations.

## 3. The public parameter balance

Using ordinary positive binary port trees at every recursive
boundary, the reconstructed public hierarchy has

\[
 \begin{aligned}
 B_{\rm pub}
   &=O\bigl(x+f_{\rm pub}+K^2g_{\rm pub}
                +d(U/K+g_{\rm pub}+h)+h\bigr),\\
 a_{\rm pub}
   &=O(dKg_{\rm pub}+dh).
 \end{aligned}
 \tag{3}
\]

Here \(B\) is logarithmic update overhead and \(a\) is logarithmic
stretch. Take

\[
 q=r=t,\quad K=t^2,\quad x=\Theta(U/t),\quad d=O(t).
\]

For the public provider this gives

\[
                 B_{\rm pub}=O(U/t+t^6h),
       \qquad a_{\rm pub}=O(t^5h).
 \tag{4}
\]

The conservative \(q^2rh=t^3h\) work term is smaller than the
displayed \(t^6h\) term. Taking \(t=\Theta((U/h)^{1/7})\)
therefore proves the derived point

\[
 B_{\rm pub}=O(U^{6/7}h^{1/7}),\qquad
 a_{\rm pub}=O(U^{5/7}h^{2/7}).
 \tag{5}
\]

This is a new reconstruction from public ingredients. It is
not the printed KMG theorem, and it replaces the previously
checked \(59/63\) composite as the stronger current comparator.

## 4. Matching that stretch with the research construction

The independently audited research hierarchy has

\[
                 B_{\rm new}=O(U/t+t^3h),
       \qquad a_{\rm new}=O(t^4h).
 \tag{6}
\]

Choose

\[
                         t=\Theta((U/h)^{5/28}).
\]

Then

\[
 a_{\rm new}=O(U^{5/7}h^{2/7}),
\]

the same asymptotic stretch scale as (5), while

\[
 \begin{aligned}
 U/t&=U^{23/28}h^{5/28},\\
 t^3h&=U^{15/28}h^{13/28}
           =o(U^{23/28}h^{5/28}).
 \end{aligned}
\]

The matched comparison is thus

| Construction | Amortized update overhead | Stretch |
|---|---|---|
| Reconstructed public composition | \(\exp O(U^{6/7}h^{1/7})\) | \(\exp O(U^{5/7}h^{2/7})\) |
| Research construction | \(\exp O(U^{23/28}h^{5/28})\) | \(\exp O(U^{5/7}h^{2/7})\) |

Both use arbitrary-degree undirected graphs, numerical distance
queries in polynomial logarithmic time, positive polynomial-range
external integer lengths, and amortized initialization/update
accounting. The constants hidden in the two stretch bounds
need not be identical; choosing the fixed parameter constants
against a specified allowed envelope gives a common scale.
No practical constant-factor performance comparison is implied.

## 5. A curve, not one isolated substitution

For a desired logarithmic stretch envelope \(A\), with
\(h\ll A=o(U)\), (4) can take

\[
 t_{\rm pub}=\Theta\!\left(
  \min\{(U/h)^{1/7},(A/h)^{1/5}\}\right).
\]

This gives the sufficient public work envelope

\[
 B_{\rm pub}=O\!\left(
       \max\{U^{6/7}h^{1/7},\,U(h/A)^{1/5}\}\right).
 \tag{7}
\]

Equation (6) instead takes \(t_{\rm new}=\Theta((A/h)^{1/4})\),
giving

\[
                       B_{\rm new}=O(U(h/A)^{1/4}).
 \tag{8}
\]

The construction and shrink guards have slack in these ranges.
These are upper envelopes for two specified constructions,
not claims of optimality among all public methods. Numerical
distance guarantees do not become exact matching or ordinary
output-sensitive path-reporting guarantees by this substitution.

The earlier \(11/14\) update point at logarithmic stretch
\(O(U^{6/7}h)\), and the \(3/4\) point with a larger
subpolynomial stretch, remain valid. This note adds a fair
comparison against a stronger reconstructed public interface
at its own smaller stretch scale. The unrestricted exact
general-graph maximum-matching exponent remains \(4/5\).

## 6. Nonuniform tuning inside the public positive-charge model

There is a useful algebraic check on (7). It is explicitly a statement
about optimizing the displayed accounting, not a lower bound on the
actual algorithm or on the APSP problem. An upper-bound expression
does not by itself prove that the implementation must incur that cost.

Consider the first part of a hypothetical nonuniform hierarchy while
the local logarithmic size \(u_i\) stays between \(U/2\) and \(U\).
Require its positive work budget \(B\) to dominate, up to fixed
constants, all the charged terms
\[
 x_i,\quad u_i/q_i,\quad u_i/r_i,\quad K_i^2q_ir_i h,
 \qquad\text{and}\qquad \sum_i u_i/K_i .
 \tag{9}
\]
Its logarithmic metric budget must dominate
\[
                 A_{\rm charge}=\sum_i K_iq_ir_i h.
 \tag{10}
\]
The nominal total shrink in this part is at least a constant times
\(U\). Since \(x_i\lesssim B\), it has
\(j\gtrsim U/B\) levels. Also
\[
 q_ir_i\gtrsim U^2/B^2,\qquad
 K_i\lesssim B^{3/2}/(U\sqrt h).
\]
Consequently (9) implies
\[
 B\gtrsim\sum_i u_i/K_i
   \gtrsim j\,U^2\sqrt h/B^{3/2}
   \gtrsim U^3\sqrt h/B^{5/2}.
\]
Thus
\[
                            B^7\gtrsim U^6h.              \tag{11}
\]

Independently, Cauchy's inequality and
\(\sum_i1/K_i\lesssim B/U\) give
\[
 \sum_iK_i\gtrsim j^2U/B\gtrsim U^3/B^3.
\]
Substituting into (10) yields
\[
             A_{\rm charge}\gtrsim U^5h/B^5.              \tag{12}
\]
If the same accounting is to certify \(A_{\rm charge}\lesssim A\),
then (11)--(12) require
\[
 B\gtrsim
     \max\{U^{6/7}h^{1/7},\,U(h/A)^{1/5}\}.
\]

This reproduces (7) inside the positive-charge model even when
parameters vary between levels. It does not certify global optimality:
a better provider, a different repair recurrence, a different
composition proof, or cancellation not captured by these charges can
change the conclusion. The analogous research-provider calculation
appears in **nonuniform_parameter_budget_frontiers.md**.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
