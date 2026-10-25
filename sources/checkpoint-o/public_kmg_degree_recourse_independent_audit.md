# Public KMG degree versus recourse: independent audit

**25 October 2026.** This is a targeted audit of the degree and edit
inventory needed in the public strong-forest joint retuning. It does
not independently reprove every subsequent strong-SSSP wrapper.

Primary source: Kyng--Meierhans--Probst Gutenberg,
[*A Dynamic Shortest Paths Toolbox*, arXiv:2311.06402v1](https://arxiv.org/pdf/2311.06402v1),
Claims 3.17--3.18, proof of Theorem 3.1 on pages 27--29, and
Lemma 3.21 / Algorithm 5 on pages 30--32.

## 1. The degree recurrence is linear in the input degree

Let \(\Delta\ge1\) bound the native input degree. Let \(P\) be a
sufficiently large uniform quality/selected-recourse allowance with

\[
                       \log P=O(U/K+g+h).
\]

The source's Claim 3.18 gives, before identification of the core copies,

\[
 \deg(\widetilde H)
   \le\widetilde O(\Delta m^{2/K}\gamma_\ell^2),
 \qquad
 \#\{\text{core-forest and selected-graph edits}}
   \le\widetilde O(\Delta m^{2/K}\gamma_\ell^2)
\]

per native edit. Choose \(P\) to absorb
\(m^{2/K}\gamma_\ell^2\) and its polynomial logarithms, or their
retuned counterparts. There are only \(O(\log m)\) core copies of
one native vertex. Their zero-length identifications therefore yield

\[
                         \deg(H)\le\Delta P.             \tag{1}
\]

This follows directly from the proved Claim 3.18. It does not use the
coarser advertised relation \(\deg(H)\le\Delta\gamma_{\rm recVS}\).
That advertised relation is true when its recourse parameter is enlarged,
but is too weak to use as the recursive degree recurrence.

## 2. The second degree factor belongs to the elementary edit transcript

The proof of Theorem 3.1 explicitly simulates a vertex split in
\(\widetilde H\) by elementary edge edits. A split can affect all
incident selected edges. Multiplying the number of split/graph events
by the maximum degree gives the safe bound

\[
                  R(\Delta)\le\Delta^2P^2               \tag{2}
\]

after enlarging \(P\) by a fixed factor. The \(\Delta^2\) is present
in the source proof, even though some displayed theorem notation does
not expose it.

Equation (2) bounds a transcript length. It does not state that the
resulting graph has degree \(\Delta^2P^2\). Equation (1) continues
to bound its actual degree. In particular, inserting the squared
factor from (2) into the degree recurrence would artificially create
an exponential-in-depth loss that is not required by the construction.

The static construction factor \(F\) also does not enter (1) or (2).
As checked in `public_apsp_joint_retuning_independent_audit.md`, the
cleanup potential counts selected edges; increasing the computation
needed to find them only enlarges the time charge.

## 3. Iterating the two different bounds

Starting from degree three and using a master \(P\) valid at every
level, (1) gives

\[
                         \Delta_i\le3P^i.
\]

The elementary edit multiplier at level \(i\) obeys

\[
                  R_i\le 9P^{2i+2}.
\]

Consequently over \(d\) levels,

\[
 \log\prod_{i<d}R_i
    \le O(d)+\sum_{i<d}(2i+2)\log P
    =O(d^2\log P).                                      \tag{3}
\]

The same conclusion holds if a local auxiliary operation has any fixed
polynomial dependence \(\Delta_i^{O(1)}P^{O(1)}\). This is the
justified public \(d^2\) envelope. There is no need to prove that the
local transcript is independent of input degree.

## 4. Conservative forest-mapping accounting

Algorithm 5 in Lemma 3.21 explicitly copies the core trees. Its copy
allowance depends on input forest edge congestion \(c\) and the
selected degree of \(H\). A safe allowance is
\(c(\deg(H)+1)\), up to polynomial logarithms, for the incident
forest nodes and the source interface's designated terminal copy.
Unneeded isolated nonterminal records must not be counted as incident
nodes using edge congestion; they may be kept separately and charged
to their own explicit vertex-edit inventory.

For the copied **edge records**, congestion is bounded by
\(c\Delta^{O(1)}P^{O(1)}\). Each native edit makes only
\(\Delta P\) core/selected events before copying. Charging their
propagation to every affected copy, and charging root merging by its
native incident-edge bound, still gives

\[
              c\Delta^{O(1)}P^{O(1)}
\]

work and recourse, in addition to the incoming forest-edit transcript.
Thus this conservative accounting remains within (3).

One should **not** reuse the source's abbreviated initialization bound
without charging its displayed copies. Initializing all copies can cost
the actual native inventory multiplied by the copy allowance; it is
safely paid by the same \(c\Delta^{O(1)}P^{O(1)}\) envelope. Likewise,
there is no need to rely on a missing or suppressed fixed power of the
recourse parameter in the source's short recourse calculation. Fixed
powers only alter the constant in (3).

The resulting safe public local/recursive work envelope is therefore
consistent with

\[
 B_0=O\bigl(x+f+K^2g+d^2(U/K+g+h)\bigr),
\]

where \(f=\log F\). This targeted audit approves the separation
needed for that envelope; it does not by itself certify any claimed
final strong-forest exponent without the remaining outer-wrapper
calculation.

