# Coarse directed paths suffice for the slack-only matching comparison

**Research lemma, 25 October 2026.** The directed path interface exposed
by **slack_only_one_sided_matching_client.md** does not require
near-exact distances merely to obtain a useful numerical direction.
A coarse multiplicative factor \(\Gamma\) yields an inverse-\(\Gamma\)
one-sided ratio. This is a reduction of an oracle requirement, not a
construction of the required dynamic directed path provider.

## 1. The exact path ratio and the strong comparison

Write \(\alpha_d=1/s_d\). The ordinary directed allocation graph has
receiving arcs \(r\to d\) of length zero and donor arcs \(d\to r\)
of length \(1/x_{rd}\). For a directed path from bin \(a\) to bin
\(b\), its slack-only ratio is

\[
       \frac{\alpha_a-\alpha_b}
            {\alpha_a+\alpha_b+\operatorname{len}(a\leadsto b)}.
                                                               \tag{1}
\]

The actual matching comparison has ratio greater than \(1/2\).
Decomposing it into directed simple cycles supplies a path satisfying

\[
           \alpha_a>3\alpha_b+\operatorname{len}(a\leadsto b).
                                                               \tag{2}
\]

This reduction uses the actual matching comparison theorem. It does
not rely on an arbitrary positive-ratio cycle in a matching-optimal
state.

## 2. Dyadic source buckets

For each dyadic threshold \(T\), define

\[
 A_T=\{a:T\le\alpha_a<2T\},\qquad
 B_T=\{b:\alpha_b<2T/3\}.                                    \tag{3}
\]

The guarded polynomial slack range requires only \(O(\log S)\)
nonempty source buckets. Take the bucket containing the source
of (2). Then

\[
                  b\in B_T,\qquad
                  \operatorname{dist}(A_T,b)<2T.             \tag{4}
\]

Suppose a directed multisource provider has upper distance estimates
within a factor \(\Gamma\ge1\), with current path witnesses whose
actual lengths are no larger than those upper estimates. It can
therefore certify a path from some \(a'\in A_T\) to this target
with length less than \(2\Gamma T\).

More generally, accept any current path from a source in \(A_T\)
to a target in \(B_T\) with length at most \(2\Gamma T\).
Equation (3) gives

\[
 \alpha_{a'}-\alpha_b>T/3,\qquad
 \alpha_{a'}+\alpha_b+\operatorname{len}(a'\leadsto b)
          <(8/3+2\Gamma)T.
\]

Its ratio is consequently greater than

\[
                   \frac{1}{8+6\Gamma}
                         \ge\frac{1}{14\Gamma}.             \tag{5}
\]

Thus the strong comparison is always detected in at least one bucket,
and every accepted bucket answer is safe for the one-sided progress
lemma. The path may start at a different bucket source from the
original comparison; all sources in the bucket satisfy the same
inequalities.

The path cannot be a zero-edge self-path, since the two price ranges
are disjoint. If the provider supplies a walk, charging donor
traversals before cancellation gives the same raw-ratio bound. Loop
erasure can only reduce its nonnegative ordinary length.

## 3. What the required query must actually return

For the intended running time, one needs a set-to-set threshold
operation: find a target in \(B_T\) with a sufficiently short
source path, or certify the absence of a path of length less than
the strong threshold. Merely exposing numerical estimates for all
vertices does not make a full scan of all targets free.

One can state the provider contract as:

* current source set \(A_T\) and target set \(B_T\);
* detection whenever their true directed distance is below \(2T\);
* a current witness of length at most \(2\Gamma T\) when a path
  is returned;
* support for the actual donor-price updates and source/target
  membership changes.

Separate instances for the \(O(\log S)\) buckets add a logarithmic
factor. This does not remove the need to pay for weight updates,
threshold discovery, path reporting, or structural record lifetimes.
The current undirected APSP machinery does not meet this directed
contract.

## 4. Old-potential feasibility is an additional requirement

The monotonicity result in **slack_potential_semantic_certificate.md**
preserves a feasible old potential when receiving arcs on the chosen
path are tight in that potential. A general coarse path has no such
guarantee. Increasing a receiving allocation lowers the reverse
donor price, which can invalidate an old potential inequality.

More explicitly, for an old potential satisfying
\[
                 0\le\pi_d-\pi_r\le\beta/x_{rd},
\]
increasing \(x_{rd}\) to \(x_{rd}+\eta\) is safe only if
\[
                 \pi_d-\pi_r\le\beta/(x_{rd}+\eta).        \tag{6}
\]
If the receiving arc is tight, \(\pi_d=\pi_r\), this holds for
any positive new donor price. Otherwise a strictly positive step
can exhaust the margin in (6), and a tight donor inequality can
leave zero admissible increase under the frozen potential.

Consequently (5) cannot be combined with the exact-SPT monotonicity
lemma without proving a compatible path/potential guarantee.
Restricting paths to potential-tight receiving arcs is a legitimate
possible interface, but its ability to detect the full matching
comparison is currently unproved.

Row normalization
\[
                      \pi_r=\min_{d\sim r}\pi_d
\]
provides at least one tight receiving exit per row. It does not
prove that every needed endpoint is reachable using only those
exits. It also does not make their directed donor metric symmetric.

## 5. Current consequence

The accuracy requirement for a future directed provider is weaker
than a \(1+\varepsilon\) distance guarantee: a factor \(\Gamma\)
can produce progress of order \(1/\Gamma^2\) per safe normalized
step. The unresolved interface is simultaneous coarse path
discovery, one-sided update support, and either feasible-potential
preservation or a charged potential refresh mechanism. No running
time below the existing matching \(4/5\) bound follows yet.

