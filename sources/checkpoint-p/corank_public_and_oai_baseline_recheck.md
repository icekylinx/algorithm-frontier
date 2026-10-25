# Public and OpenAI baseline check for the corank transfers

**25 October 2026. Bounded current-source audit, not a publication-priority certificate.**

The active research direction is allocation, scheduling and related
selection problems. The original general-graph matching 4/5 bound
is historical and unchanged. This note records the comparisons
needed for the new corank results.

## 1. Public polymatroid baseline and imported primitives

The primary full text is Bamas, Lindermayr, Megow, Rohwedder and
Schloeter, *Santa Claus Meets Makespan and Matroids: Algorithms and
Reductions*, arXiv:2307.08453v1:
<https://arxiv.org/html/2307.08453v1>.

Theorem 4 states polynomial approximation factors 8+epsilon in
general and 4+epsilon for two resource values. Corollary 5 states
7/4+epsilon for two-size job-matroid makespan. The paper's
polymatroid formulation, aggregation and integral decomposition
are the common input framework. Theorem 21 gives all-player
allocation loss at most the largest resource value from a feasible
fractional assignment. Theorem 23 gives makespan increase at most
the largest job size; its proof explicitly works with the job
polymatroids. These additive ingredients are the public imports
used in the easy branches of the new proofs.

The new exact factors two and three halves have a different time
regime: their polynomial input degree is independent of the stated
corank parameter, but an exponential parameter factor is paid.
They do not constitute a uniform polynomial improvement when
that parameter is unbounded.

## 2. Other public comparisons remain distinct

The earlier checkpoint records the two-size five-thirds estimation
and configuration-LP results, and distinguishes them from an actual
construction with its complete running time. It also records the
ordinary restricted-assignment quasipolynomial construction. Their
parameters and resource representations are not substituted for
the new arbitrary-polymatroid oracle model.

The current DRZ version correction and the separate Cheng--Mao
ordinary restricted Santa Claus result remain in
`current_public_version_and_dependency_recheck.md`. No superseded
local-search coefficient is imported into the corank branching
argument, which has its own self-contained proof.

Targeted searches using corank, unused eligible machines, parameterized
restricted assignment, and polymatroid allocation did not verify a
primary theorem with the exact new combination of model, parameter,
factor and runtime. This is a bounded search outcome. Terminology
can differ and a general approximation-search theorem may already
subsume the branching mechanism. No first-ever claim follows.

## 3. OpenAI collection: a limited index comparison

The official collection index was reopened:
<https://raw.githubusercontent.com/openai/math/main/CONTENTS.md>.
The retrieved index describes result 114 as randomized approximate
counting of common integer bases of two integral polymatroids with
binary capacities. Result 124 concerns unit jobs with precedences
on three identical machines. Those stated models do not directly
supply the corank quota or two-size assignment algorithms here.
The index search found no occurrences of the strings "Santa",
"allocation", or "matroid parity". This is not an exhaustive audit
of every constituent manuscript, nor a correctness endorsement of
unreviewed collection results.

There is a specific reduction boundary. A t-quota indicator t*1_I
for a player basis I belongs to the integer points of B(t r_M),
but arbitrary integer points of that scaled base polytope may have
coordinates strictly between zero and t. Counting or finding
general common integer bases therefore does not impose the
all-or-nothing quota condition. An additional valid argument would
be required before such a counting result could replace the
branching algorithm. No such replacement is assumed.

The original matching paper and its imported state interfaces retain
their separately documented provenance in
`current_checkpoint/oai_baseline_and_imports.md`. This checkpoint
does not revise or attempt to lower that original matching exponent.

## 4. What is established by the checkpoint

The checkpoint contains complete internally reviewed deterministic
algorithms and self-contained oracle lower bounds. It establishes
their mathematical statements subject to the explicitly named
standard oracle primitives. The lower bounds match approximation
thresholds in the full value-oracle models. They do not establish
publication priority, the optimal exponential base, or hardness for
explicit ordinary restricted-assignment representations.
