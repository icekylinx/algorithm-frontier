# One-value allocation with exact quotas and setup costs

**Guarantee**

Returns at least $\lceil K_\star/2\rceil$ units to every player of an actual selected basis, preserving the exact combined setup and assignment budget. More generally, fixed integer $d\ge2$ gives $\lceil K_\star/d\rceil$.

**Objective and output**

Maximize the common minimum count of equal-value units; output a selected basis and integral resource counts.

**Randomness**

Deterministic corank branching and exact-budget recovery; the whole-ground alternative uses deterministic inclusion covers.

**Time**

For fixed integer $d\ge2$ set $R_d=(d+1)/(d-1)$, $A_d=\Gamma(R_d)$, and $B_d=2-1/A_d$. Time is $A_d^c\mathrm{poly}(H)$ or $B_d^q E(q)\mathrm{poly}(H)$. Exact factor two has $A_2=27/4$ and $B_2=50/27$; factor three has $A_3=4$ and $B_3=7/4$.

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units.

**Parameters**

$q$ is the nonloop player count; $r\ge1$ is its matroid rank; $c=q-r$; $K_\star$ is the integer optimum count; each unit has value $v>0$. $\Gamma(R)=R^R/(R-1)^{R-1}$ and $E(q)=2^{O(q\log\log(q+2)/\log(q+2))}$. $H$ includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

Arbitrary integral recipient polymatroids, an original player-matroid basis, nonnegative setup and assignment costs, one shared exact budget, and unused resources allowed.

**Lower-bound scope**

The [strict-below-two oracle barrier](../allocation-lower-bounds/proof.md) applies to an included zero-cost subclass; it does not prove these exponential bases optimal.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The [base proof](proof.md) treats assignment costs; the [setup and full quota tradeoff](setup-tradeoffs.md) proves the stronger shared-budget statement. With $c=0$, exact count optimization is polynomial after subtracting the fixed setup cost.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
