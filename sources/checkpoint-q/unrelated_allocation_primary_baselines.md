# Primary baseline audit for unrelated-value budgeted allocation

**25 October 2026. Bounded current-source check; no exhaustive priority claim.**

The new joint-role theorem concerns arbitrary nonnegative player-type
values, arbitrary integral recipient-polymatroid value oracles, an
optional original player-matroid basis, and one exact assignment
budget. Its shared-setup extension additionally pays the selected
players' nonnegative setup fees from that same budget. Its main time
parameter is the explicit number q of candidate players, with
polynomial dependence on all other input and oracle data.

The comparison must distinguish this from ordinary explicit items,
polynomial-time approximation, parameterized approximation schemes,
and algorithms that augment the budget. The following primary sources
were opened and their relevant statements checked directly.

## 1. General unrelated ordinary items: polynomial and quasipolynomial time

Chakrabarty, Chuzhoy and Khanna,
[On Allocating Goods to Maximize Fairness, author full version](https://home.ttic.edu/~cjulia/papers/max-min-allocation-full.pdf),
dated 24 February 2012, gives the classical general additive
max-min-allocation tradeoff: a roughly n^epsilon approximation in
n^(O(1/epsilon)) time, with the stated lower restriction on epsilon,
and a polylogarithmic approximation in quasipolynomial time.
Here n counts items in that paper. It also gives factor two for
the special case where each item has positive value to at most
two agents.

This ordinary-item paper does not assert the full recipient-polymatroid
or exact assignment-budget theorem developed here. The comparison is
not that the new exponential-time algorithm dominates its polynomial
or quasipolynomial time. It provides a different point on the quality,
time and input-model spectrum.

## 2. A public parameterized approximation scheme already exists

Jansen and Maack,
[An EPTAS for Scheduling on Unrelated Machines of Few Different Types](https://arxiv.org/abs/1701.03263),
arXiv v2, with
[full primary text](https://arxiv.org/pdf/1701.03263),
states in Theorem 1 the same approximation-scheme running time for
ordinary Santa Claus and makespan:

\[
 2^{O(K\log K\,\epsilon^{-1}\log^4(1/\epsilon))}
       +\operatorname{poly}(|I|),
\]

where K is the number of distinct player or machine types.
Taking K<=q gives a parameterized approximation scheme for ordinary
unbudgeted unrelated allocation by number of players. For fixed
accuracy, the displayed upper bound is of order 2^(O(q log q))
plus a polynomial, and its approximation can approach one.

The authors themselves explicitly discuss the parameterized
interpretation. Grandoni's contribution to
[Dagstuhl Seminar 23291, Section 5.3](https://drops.dagstuhl.de/storage/04dagstuhl-reports/volume13/issue07/23291/DagRep.13.7.96/DagRep.13.7.96.pdf)
also records this implication.

Therefore the new result must not be advertised as the first
constant-factor FPT approximation by number of players. Its relevant
distinctions are the explicit strictly-sub-two exponential base at a
coarser approximation, arbitrary recipient ranks, exact arbitrary
assignment cost, and the separately proved player-selection and setup
extensions. The public scheme has stronger accuracy in its own model.
Neither theorem is an unconditional dominance statement over the other.

## 3. Exact-budget intrinsic values in polynomial time

Rohwedder, Rouhani and Wennmann,
[Cost Preserving Dependent Rounding for Allocation Problems, ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127),
[full proceedings text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.127/LIPIcs.ICALP.2025.127.html),
Theorem 3, gives a randomized polynomial O(log n) approximation for
ordinary Budgeted Santa Claus. Its budget is exact, and the stated
model has intrinsic item values with recipient-dependent costs.
The paper's earlier additive-rounding discussion also allows unrelated
values in its ordinary assignment setting.

These public rounding ingredients are explicitly credited by the
project. The new joint-role theorem is not a claim that cost-preserving
additive rounding was invented here. Its full recipient-polymatroid
implementation and its use with changing light/heavy pair masks have
separate complete proofs.

## 4. A newer arbitrary-value budgeted baseline is bicriteria

Bamas, Li and Rohwedder,
[Randomized Rounding over Dynamic Programs](https://arxiv.org/abs/2511.03490),
arXiv v1 dated 5 November 2025, appears in STOC 2026. The primary
[Theorem 1.8 and Section 7.2](https://arxiv.org/html/2511.03490v1)
handle ordinary arbitrary-value Budgeted Santa Claus.
In time n^(O(1/epsilon)), their displayed guarantee gives every
player value at least V/(n^epsilon polylog(n)), while permitting
assignment cost B n^epsilon polylog(n), from a witness of value V
and cost B.

Thus this is a bicriteria approximation: its cost can exceed the
original budget. The project theorem keeps that budget exact but
uses exponential time in q. It does not improve the public theorem's
polynomial-time ratio at the same time bound.

The paper's general dynamic-programming theorem can preserve a
linear objective while relaxing added packing rows; that fact should
not be substituted for the explicit Santa Claus application's
bicriteria statement. The comparison above uses the application's
own theorem and variables.

## 5. A simple same-model exponential benchmark

For the project's one-budget unrelated allocation model, enumerate
all compulsory light/heavy role sets at each pair-value threshold.
For a fixed role set, the joint fractional LP is polynomially
solvable, and the reviewed cost-preserving count-floor rounding
recovers its weak guarantee. The optional player matroid has the
same-ground dummy adapter. This gives a direct 2^q times polynomial
role-enumeration benchmark. Exact fixed-role optimization, with the
mask at OPT/2, actually gives exact factor two, including the reviewed
setup extension; the complete endpoint proof is in
exact_two_global_enumeration_unrelated_allocation.md.

For the coarser factor 2R/(R-1), the weighted gap extension and global
cover replace that enumeration by B(R)^(q+o(q)) poly(H), where
B(R)=2-1/Gamma(R)<2 for fixed R.
This is a self-contained comparison within one exact model, not an
unsupported assertion about the best known published exponential
base. It also explains why the explicit q matters: q is players,
not the number of binary resource units or LP variables.

The accepted full-oracle hidden-subset lower bound rules out a
strictly smaller-than-two global base for approximation strictly
below two in the specified superclass. That oracle statement does
not rule out the ordinary-item parameterized schemes in Section 2,
whose resource representation is more informative.

## 6. Public OpenAI index scope

The public
[OpenAI mathematics index](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md)
was reopened and searched for the relevant terms. The visible index
contains no text match for Santa or allocation. Its entry 114
describes randomized approximate counting of common integer
polymatroid bases with binary capacities; entry 124 concerns
three identical machines with unit jobs and precedence constraints.
They are different stated tasks from this unrelated-value,
exact-budget max-min allocation theorem.

This is an index-level scope check only. It does not validate the
indexed manuscripts, assert that no reduction from them could exist,
or supply access to a private OpenAI baseline. The project uses the
ordinary deterministic optimization primitives stated in its proofs,
not an unexamined counting claim.

## 7. How the current claims should be reported

The supported claim is a completed internally reviewed derivation
of a deterministic near-two algorithm in explicit sub-two-base
exponential time, for the precisely stated full recipient-polymatroid
and exact-budget model, with an optional player matroid and the
reviewed setup extension. Compulsory unrelated two-valued pairs
have the stronger exact-two and integer-quota tradeoffs.

The source search is not exhaustive. No first-publication claim,
polynomial-time constant approximation claim, or universal
improvement over all ordinary-item algorithms is made. The current
results improve the project's previous intrinsic-value scope and
its same-model 2^q role-enumeration benchmark.
