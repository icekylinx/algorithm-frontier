# Scheduling by bottleneck commitments

**Guarantee**

With $`D_k=3-2/k`$ and $`\beta(D)=\max\{3/2,2-1/D\}`$, returns

```math
C_{\max}\le\min\{\mathrm{OPT}+a,\max\{\beta(D)\mathrm{OPT}+u,a+\lambda_k\}\}.
```

For two sizes, the bound improves to $`\max\{\alpha_k\mathrm{OPT},a+\lambda_k\}`$, where $`\alpha_k=3/2`$ for $`k\le2`$ and $`5/3`$ for $`k\ge3`$.

**Objective and output**

Commit a computable independent set of largest-job machines, solve the remaining rank-$`k`$ problem, and recover every original job base.

**Randomness**

Deterministic greedy commitment selection, residual unit search, exact decomposition and additive rounding.

**Time**

For $`D=D_k`$, time is $`2^{O(k)}\mathrm{poly}(H)`$. For $`D=D_k+\eta`$ with rational $`0<\eta\le1`$, time is $`\mathrm{poly}(H)\min\{2^{O(k)},(k+1)^{O((1+\eta^{-1})\log(k+1))}\}`$.

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units.

**Parameters**

$`a`$ is the largest positive size; $`u`$ is the largest smaller size; $`h`$ is the required largest-job total; $`1\le k\le h`$. For $`W_p=\sum_{j:p_j<a}p_j f_j(\{p\})`$, $`\lambda_k=\min\{z:\mathrm{rank}_M(\{p:W_p\le z\})\ge h-k\}`$, where $`M`$ is the rank-$`h`$ Boolean-cap largest-job matroid. Set $`\lambda_h=0`$.

**Model and representation**

Integral job polymatroids with common type sizes, binary ranks, mandatory original bases, and no additional assignment-cost budget. The Boolean-cap rank-loss case is handled by a polynomial $`3/2`$ branch.

**Lower-bound scope**

No lower bound is claimed for this algorithm.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The commitment term is a load bound, not an approximation ratio. The two-size rank-two result is a full $`3/2`$ approximation precisely when $`a+\lambda_2\le3\mathrm{OPT}/2`$. The $`k=0`$, empty-job, and one-size cases have separate routines.

## Further rank reductions and local-size certificates

These companion theorems use the same common-type job-polymatroid model
with mandatory original bases and no assignment or setup budget.

**[Full-marginal machine contraction](machine-contraction.md)**

A polynomial greedy pass computes a bottleneck $`\beta_k`$ and contracts every job polymatroid to residual large-job rank at most $`k`$. Every residual guarantee $`\alpha\mathrm{OPT}_F+e`$ becomes $`\max\{\beta_k,\alpha\mathrm{OPT}+e\}`$, because $`\mathrm{OPT}_F\le\mathrm{OPT}`$. Machines may absorb multiple large units and original $`h`$ may exceed $`q`$.

**Homogeneous-large residual scheduling**

Returns $`\min\{\mathrm{OPT}+a,\max\{\beta_k,(2-1/(3+\eta))\mathrm{OPT}+u\}\}`$ in $`\mathrm{poly}(H)\min\{2^{O(k)},(k+1)^{O((1+\eta^{-1})\log(k+1))}\}`$ time for rational $`0<\eta\le1`$. With exactly two positive sizes, the residual term improves to $`5\mathrm{OPT}/3`$ in $`2^{O(k)}\mathrm{poly}(H)`$ time.

**Zero residual large rank**

With exactly two positive sizes, $`\max\{\beta_0,\mathrm{OPT}\}`$; with arbitrary smaller sizes, $`\max\{\beta_0,\mathrm{OPT}+u\}`$. The original additive candidate $`\mathrm{OPT}+a`$ may also be retained.

**[Eligibility padding and collision thresholds](eligibility-padding.md)**

Given an aggregate-independent commitment $`F_0`$ of size $`h-k`$, returns $`\min\{\mathrm{OPT}+a_+,\max\{\beta_D(F_0)\mathrm{OPT}+u,B(F_0)\}\}`$. Here $`\beta_D=\max\{1+a_+/C_2,1+E_D/a_+\}`$, $`E_D=((D-1)A+H_{\mathrm{width}})/D`$, and $`B(F_0)=\max_{p\in F_0}(W_p+a_p)`$.

**Eligibility-sensitive hard-target bound**

If $`\mathrm{OPT}<C_2`$, the preceding construction gives $`\max\{\mathrm{OPT}+E_D+u,B(F_0)\}`$. The exact scalar refinement can replace $`E_D`$ by its smaller optimized padding certificate $`C_\star`$.

For eligibility padding, $`a_+`$ is the largest attained type size, $`C_2`$ is
the minimum possible load of two large units on one machine, and
$`a_+/\infty=0`$. On the nonloops of the contracted large-recipient
matroid, $`A=\max_p a_p`$ and $`H_{\mathrm{width}}=\max_p(a_p-\ell_p)`$, where $`[\ell_p,a_p]`$
is the range of large sizes eligible at $`p`$. With $`D=D_k=3-2/k`$ the
time is $`2^{O(k)}\mathrm{poly}(H)`$; with $`D=D_k+\eta`$, $`0<\eta\le1`$, it has the same
rank-quasipolynomial alternative as the table above. Boolean-rank loss
is handled by the separate additive collision branch. Every bottleneck
is a load certificate; no promise that it is small compared with $`\mathrm{OPT}`$
is implicit.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
