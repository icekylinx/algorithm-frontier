# Scheduling with two processing times per machine

**Guarantee**

For every fixed integer $d\ge2$, returns makespan at most $(2-1/d)\mathrm{OPT}$, including exact $3/2$ at $d=2$.

**Objective and output**

Assign every original type total when each machine has at most two positive processing times, preserving the exact assignment-cost budget.

**Randomness**

Deterministic quota search and original-total recovery, including the fixed-factor endpoints and deterministic whole-ground conversion.

**Time**

Put $R_d=(d+1)/(d-1)$, $A_d=\Gamma(R_d)$, and $B_d=2-1/A_d$. Time is $B_d^q E(q)\mathrm{poly}(H)$. Endpoints are

$$
(\text{factor},\text{base})=(3/2,50/27),(5/3,7/4),\bigl(7/4,2-(108/3125)^{1/3}\bigr).
$$

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units.

**Parameters**

$q$ is the physical-machine count; $d\ge2$ is a fixed integer; each machine has its own at most two positive times $u_p<a_p$. $\Gamma(R)=R^R/(R-1)^{R-1}$ and $E(q)=2^{O(q\log\log(q+2)/\log(q+2))}$. $H$ includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

Integral job polymatroids, mandatory original bases, machine-dependent two-time pairs, arbitrary nonnegative assignment costs, and one exact scalar budget. Zero-time pairs are permitted.

**Lower-bound scope**

No lower bound is claimed for this algorithm.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The positive time pair may differ from machine to machine. A rational noninteger $d$ is not included in the discrete quota proof.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
