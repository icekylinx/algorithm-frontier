# Randomness contracts

The [result catalogue](../README.md) and every problem card state the
randomness of the displayed method. Different variants within one family may
have different contracts. An exact output, a deterministic verifier, or a
probabilistic existence proof does not alone classify the construction.

## Algorithm labels

- **Deterministic.** The procedure draws no random bits. Its guarantee holds
  for every input satisfying its stated assumptions. Fixed tie rules resolve
  arbitrary choices. A deterministic oracle algorithm retains its paid
  oracle assumptions; it does not supply an unproved backend implementation.
- **Monte Carlo.** A bounded run can fail to produce an output satisfying the
  approximation or support guarantee. The result states its success event
  and probability, such as at least <code class="math">2/3</code> or <code class="math">1-\delta</code>. Feasibility of a
  returned object alone need not certify all its approximation guarantees.
- **Las Vegas.** Every returned output satisfies the guarantee, while the
  running time is random and must be stated in expectation or with a tail
  bound. Repetition warrants this label only when an adequate success
  verifier and a bound on the expected number of attempts are proved.
- **Mixed.** The family contains different contracts. The entry identifies
  the deterministic and randomized variants separately.

Existence theorems, structural lemmas, deterministic reductions and oracle
lower bounds are labeled as such. An existential support bound does not
promise a construction with that support in the compact input size.

## Confidence and adaptive choices

For randomized preprocessing, distinguish a guarantee for one fixed query
from one success event covering every allowed query or failure. In the
second case, queries can be chosen after observing the summary because the
event already quantifies over all of them. This alone does not prove that a
randomized update structure tolerates an adaptive update adversary.

The [label/block construction](../problems/label-block-cut/proof.md), for
example, has one all-failure, all-query event of probability at least <code class="math">2/3</code>.
The [correlated spectral pools](../problems/correlated-spectral-regression/proof.md)
instead expose their failure parameter <code class="math">\delta</code>. A separate random-code
construction also has its own code failure parameter <code class="math">\zeta</code>; all applicable
failure events must be counted.

A probabilistically failing local oracle requires an error budget over its
actual calls. Replacing an exact or certified deterministic oracle by such an
oracle does not automatically preserve the theorem. The graph compositions
use the deterministic interfaces and local realizations named in their
statements. Published prerequisites, supplied oracle models and unresolved
mathematical assumptions are recorded separately.

## Probability used only in a proof

The [omission search](../problems/whole-ground-allocation/selection.md) uses
Bernoulli probabilities to bound the number of branches, but enumerates its
certificates deterministically. The
[sparse route rounding](../manuscripts/graph-backends/nonuniform-fractional-path-selection.md)
derandomizes its weighted choices by conditional averaging. The
[Cayley construction](../problems/group-metric-constraints/manuscripts/arbitrary-group-cayley-sparsification.md)
derandomizes a concentration experiment. These constructions are
deterministic despite the probability calculations in their proofs.

Likewise, the [non-Fano probability](../problems/obstruction-boundaries/proof.md)
is the exact probability of a specified random-sign experiment, rather than
the error probability of an algorithm.

## Lower bounds

State whether the adversary argument concerns deterministic algorithms or
also bounded-error randomized algorithms, and in the latter case state the
success and query-budget convention. The
[numeric-target lower bound](../problems/numeric-target-frontier/proof.md)
covers success at least <code class="math">2/3</code> with a bounded worst-case number of rank queries.
The elementary [allocation barriers](../problems/allocation-lower-bounds/proof.md)
are stated for deterministic algorithms. These scopes should be retained
when comparing them with algorithmic upper bounds.

## Maintaining the labels

`catalogue.json` owns the concise randomness contracts for all main and
supporting entries. `python3 tools/build_catalogue.py` updates the compact
homepage and the **Randomness** paragraph on each problem card. The three
featured methods are deterministic; their detailed contracts remain on
their cards. The standard repository check rejects missing or stale card
labels. A changed backend, success probability, or adversary model requires
a corresponding proof and source update.
