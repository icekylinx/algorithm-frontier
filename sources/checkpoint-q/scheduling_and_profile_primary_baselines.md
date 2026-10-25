# Primary-source baseline audit for the profile schemes

**25 October 2026. Bounded public-source audit, not a priority certificate.**

The comparisons below distinguish input representations, parameters,
accuracy dependence and exact versus relaxed costs. The internal PS,
PA, AB, SX and HT proofs stand on their own. Public sources establish
antecedents and comparison points; they do not certify the new proofs.

## 1. Cost-preserving ordinary scheduling is established background

David Shmoys and Eva Tardos, *An approximation algorithm for the
generalized assignment problem*, Mathematical Programming 62 (1993),
461--474, [primary full text](https://www.columbia.edu/~cs2035/courses/ieor6400.F07/st.pdf).

Theorem 2.1 gives ordinary unrelated-job rounding with no cost increase
and additive load at most the largest eligible processing time. The
remark on page 466 explicitly treats type multiplicities: assign the
integer part first, leaving fewer than machine-count times type-count
units for the remaining rounding. Thus exact assignment-cost preservation
and compressed ordinary multiplicities are not new claims here.

Our comparisons must instead specify the original recipient-polymatroid
bases, the deterministic exponential profile bounds, and the complete
full-total recovery after every mask. A job-polymatroid resource is not
automatically an independent ordinary job list.

## 2. Ordinary approximation schemes already exist

Klaus Jansen and Lorant Porkolab, *Improved Approximation Schemes for
Scheduling Unrelated Parallel Machines*, Mathematics of Operations
Research 26(2), 324--338 (2001),
[publisher abstract](https://pubsonline.informs.org/doi/abs/10.1287/moor.26.2.324.10559).
The abstract gives fixed-machine approximation schemes and an extension
with both makespan and cost allowed a factor 1+epsilon. That extension
is a bicriteria statement, not the strict-budget guarantee proved here.
This audit uses the verified abstract scope rather than claiming a
complete proof audit of that paper.

Klaus Jansen and Monaldo Mastrolilli, *Scheduling unrelated parallel
machines: linear programming strikes back*, Technical Report 1004,
March 2010,
[primary report](https://d-nb.info/1020285699/34).
Its displayed ordinary scheduling bound is O(n)+2^{O(q log(q/epsilon))}.
The simplification to O(n)+(1/epsilon)^{O(q)} is explicitly conditioned
on sufficiently small epsilon, for example epsilon<=1/q. Section 3's
cost extension relaxes both cost and makespan by 1+epsilon.

Klaus Jansen and Marten Maack, *An EPTAS for Scheduling on Unrelated
Machines of Few Different Types*,
[primary full text, December 2017 version](https://arxiv.org/pdf/1701.03263).
Theorem 1 covers both ordinary makespan and Santa Claus, parameterized
by the number K of machine types, with displayed dependence
2^{O(K log(K) epsilon^{-1} log^4(1/epsilon))}+poly(|I|).
Taking K no larger than q already supplies ordinary machine-parameterized
approximation schemes. The checkpoint therefore makes no first-scheme
claim. The type parameter can be much smaller than the physical machine
count, so comparing exponents requires stating which parameter is used.

The current PS and PA curves have linear q/epsilon in the exponent and
a polynomial factor for exact oracle work. This is a different tradeoff;
it is not uniform dominance of every preceding scheme as all parameters
vary. A faster dependence on q at fixed accuracy can coexist with a
worse dependence on very small epsilon or on explicit ordinary input.
No exhaustive latest-best result is inferred from these references.

## 3. Allocation/scheduling reductions do not preserve every parameter

Etienne Bamas, Alexander Lindermayr, Nicole Megow, Lars Rohwedder and
Jens Schloter, *Santa Claus meets Makespan and Matroids: Algorithms and
Reductions*, [primary text](https://arxiv.org/html/2307.08453v1).

The two-value allocation/scheduling relation maps approximation alpha
to 2-1/alpha. Appendix C.1 introduces players associated with both
original machines and jobs. Therefore an exponential algorithm in its
new player count does not directly give the checkpoint's exponent in
only physical machines. The paper also provides intrinsic matroid and
polymatroid scheduling results. Those settings and guarantees must be
compared with the unrelated pair times and exact assignment budget
stated by US, HT, AB, SX and PS.

The direct full-target witness in the new scheduling proofs stays on
the original machines. This point, rather than the public ratio map
alone, is what supports the physical-ground complexity claim.

## 4. Cost-preserving allocation rounding has public antecedents

Lars Rohwedder, Ashkan Norouzi Rouhani and Leo Wennmann,
*Cost Preserving Dependent Rounding for Allocation Problems*,
ICALP 2025,
[primary full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.127/LIPIcs.ICALP.2025.127.html).
The paper studies exact-cost allocation rounding; its Budgeted Santa
Claus theorem gives a randomized polynomial-time logarithmic guarantee
in the stated ordinary setting. Cost preservation itself is established
background. PA proves its particular simultaneous prefix-floor
construction and its deterministic profile bound for the full model.

Etienne Bamas, Shi Li and Lars Rohwedder, *Randomized Rounding over
Dynamic Programs*, [primary text](https://arxiv.org/html/2511.03490v1).
Theorem 1.8's ordinary Budgeted Santa Claus application has both a
utility approximation and a multiplicative budget increase. Its
application-specific statement should not be replaced by a stronger
exact-budget assertion inferred from a general theorem elsewhere in
the paper. Its polynomial-time regime is also distinct from PA's
accuracy-dependent exponential regime.

## 5. Robust common-basis boundaries have different input meanings

Ilan Doron-Arad, Ariel Kulik and Hadas Shachnai,
*You (Almost) Can't Beat Brute Force for 3-Matroid Intersection*,
[primary v2 text](https://arxiv.org/html/2412.02217v2).
Theorem 1.1 gives a near-2^q membership-query lower bound for three
matroids on the admissible square-size subsequence. Taking one as the
player matroid and two as unit-resource scenarios is a direct inference
giving a robust positivity obstruction. Rank queries are simulated by
at most q independence queries. This attributed implication is distinct
from RO's self-contained q-scenario, uniform-player-matroid construction.

Amir Abboud, Kevin Lewi and Ryan Williams, *Losing Weight by Gaining
Edges*, ESA 2014,
[primary full text](https://people.csail.mit.edu/rrw/ksum.pdf).
Definition 1.1 and Theorem 1.3 support the bounded nonnegative k-SUM
hardness used in TS. The two exact scenario budgets are proved in the
checkpoint to force the omitted subset's sum to equal the target.
That conditional explicit-input corank boundary is not an oracle
query lower bound or a general whole-ground base lower bound.

Chien-Chung Huang and Francois Sellier,
*Matroid-Constrained Vertex Cover*,
[primary abstract](https://arxiv.org/abs/2306.04342).
Its objective maximizes covered edge weight under a matroid constraint.
WF concerns the exact all-edges-covered target, followed by basis
extension. This relationship does not establish that the checkpoint's
Fibonacci branching is the fastest known graph algorithm or improves
the paper's approximation ratios.

## 6. Global base conversion is a public framework

Fedor Fomin, Serge Gaspers, Daniel Lokshtanov and Saket Saurabh,
*Exact Algorithms via Monotone Local Search*,
[primary journal text](https://sites.cs.ucsb.edu/~daniello/papers/monotoneLocalSearch19.pdf).
The base conversion 2-1/A from an A^c extension algorithm is public
background. The checkpoint relies on its separately proved streamed
block implementation when claiming polynomial space and an explicit
subexponential overhead. Neither the generic base formula nor monotone
local search is claimed as invented in this project.

## 7. Public OpenAI comparison is limited to visible indexed material

The [public OpenAI math index](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md)
was checked again on 25 October 2026. Entry 114 describes randomized
approximate counting of common integer polymatroid bases with binary
capacities. Entry 124 describes exact unit-job precedence scheduling
on three identical machines. These indexed descriptions concern
different objectives and inputs from the present deterministic
allocation/scheduling profile schemes.

This is an index-level comparison. It does not independently verify
those indexed proofs, search unpublished work, or prove that no related
OpenAI result exists. In particular, no indexed counting statement is
used as a black-box algorithm for the checkpoint's optimization proofs.

## 8. What may safely be claimed

The manuscripts establish their displayed algorithms within their
explicit exact oracle/bit model. They improve the project's own
previous general-case approximation guarantees and supply useful
explicit time/accuracy tradeoffs in broader budgeted inputs.

The supported public comparison is narrower: the listed antecedents
have the precise models and costs recorded above. Calling a result
the first public scheme, uniformly fastest, or a new polynomial-time
breakthrough would require additional evidence and is not done here.
Fresh extensions or newer exact-input leads remain research work until
their full proof and source comparison have been completed.
