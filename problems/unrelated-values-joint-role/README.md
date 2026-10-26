# Unrelated-value allocation with shared resource roles and setup costs

**Guarantee**

For fixed rational $`R>1`$, returns an actual selected basis and utility at least $`(1-1/R)\mathrm{OPT}/2`$ under one exact combined setup and assignment budget. Arbitrary values also admit exact factor two in $`2^q\mathrm{poly}(H)`$. Compulsory pair values $`\{0,u,a\}`$ admit the sharper J2 endpoint.

**Objective and output**

Maximize minimum player-specific utility while light and heavy roles share the original resource capacities; return actual integer counts and selected players.

**Randomness**

Deterministic in the near-two, exhaustive exact-two, compulsory J2 and whole-ground variants, with paid exact optimization and rounding primitives.

**Time**

Let $`B(R)=2-1/\Gamma(R)`$. The near-two theorem takes $`B(R)^q E(q)\mathrm{poly}(H)`$; use $`R=(2+\eta)/\eta`$ for factor $`2+\eta`$. J2 takes $`(27/4)^{\nu_C}\mathrm{poly}(H)`$ or $`(50/27)^q E(q)\mathrm{poly}(H)`$.

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units.

**Parameters**

$`q`$ is the original nonloop candidate count. $`R>1`$ is fixed rational; $`\nu_C`$ is the largest affordable one-heavy-unit recipient set in the compulsory two-value model. $`\Gamma(R)=R^R/(R-1)^{R-1}`$ and $`E(q)=2^{O(q\log\log(q+2)/\log(q+2))}`$.

**Model and representation**

Arbitrary integral recipient polymatroids, arbitrary player-type values, nonnegative original setup and assignment costs, and one exact budget. Near-two and $`2^q`$ exact-two allow an optional player-matroid basis. The J2 and discrete factor-$`d`$ pair-value refinements require compulsory players.

**Lower-bound scope**

The arbitrary-oracle subclass has strict-below-two query barriers. Neither an optimal exponential base at factor two nor an optional-basis extension of J2 is proved.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

## Results and proofs

**$`2+\eta`$**

**Time.** $`B((2+\eta)/\eta)^q E(q)\mathrm{poly}(H)`$

**Scope and proof.** [Joint-resource roles](proof.md), and [shared setup budget](setup-budget.md) for optional paid selection

**Exact $`2`$ for arbitrary values**

**Time.** $`2^q\mathrm{poly}(H)`$

**Scope and proof.** [Exact endpoint](exact-two.md), including optional selection and shared setup

**Exact $`2`$ for player-specific $`\{0,u,a\}`$**

**Time.** $`(27/4)^{\nu_C}\mathrm{poly}(H)`$ or $`(50/27)^q E(q)\mathrm{poly}(H)`$

**Scope and proof.** [J2 proof](proof.md#9-compulsory-two-valued-unrelated-instances-exact-factor-two); compulsory players, one assignment budget

**Fixed integer factor $`d\ge2`$ for $`\{0,u,a\}`$**

**Time.** $`A_d^{\nu_C}\mathrm{poly}(H)`$ or $`(2-1/A_d)^q E(q)\mathrm{poly}(H)`$

**Scope and proof.** [Integer tradeoff](two-value-tradeoffs.md), $`A_d=\Gamma((d+1)/(d-1))`$

If an optimum has at most $`K`$ selected heavy recipients at threshold $`(1-1/R)\mathrm{OPT}/2`$, the near-two proof also gives $`\Gamma(R)^{q-r+K}\mathrm{poly}(H)`$. This is a threshold-dependent support condition. The signed dummy used for setup accounting is an internal construction; original costs remain nonnegative.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
