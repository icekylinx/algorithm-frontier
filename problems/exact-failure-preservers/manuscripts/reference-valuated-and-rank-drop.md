# Certified valuated baselines and ordinary rank-drop reporting

The [native interface](../reference/README.md) adds two realizations to the
existing reporter: fixed-rank valuated intersection from a supplied common
basis whose optimality is independently certified, and initialized ordinary
minimum-cost maximum-cardinality intersection under one deletion. Valuations
remain fixed between independent queries. No smaller-rank valuation objective
or native valuated initializer is inferred.

## 1. Oracle model and certificate contract

The original ground is the explicitly listed integer IDs `range(N)`. Two
callbacks represent valid rational minimization-convention valuated matroids
of the same stated rank. A basis has an exact `int`/`Fraction` value; `None`
means it is outside the effective domain. Validity of the valuated exchange
axiom is part of the oracle model, like validity of ordinary matroid
independence callbacks. The backend does not enumerate all bases to validate
that axiom.

A supplied baseline must be a common finite-valued basis. Its optimality is
checked rather than assumed. `certify` returns its exact sum of valuations
and an original-ground price vector. `verify_optimality` re-evaluates the
original baseline and each single exchange and checks only the priced local
inequalities. It uses no graph, optimizer, shortest path or certificate
producer. A malformed certificate or a failed inequality is rejected.
A common but nonoptimal supplied baseline is rejected by construction; this
is not an infeasibility claim for the original intersection problem.

## 2. A split-price certificate from the compressed graph

**Proposition 1.** A common finite-valued baseline is optimal exactly when
the compressed valued exchange graph has no negative directed cycle.
In that case the native procedure constructs polynomial-bit split prices
certifying optimality through original local exchanges.

**Proof.** Use the increments and ordered-pair lengths of V4 in
[the valuated companion](valuated-matroid-intersection.md). Its joint
convex-decomposition argument shows that an optimal baseline has no negative
cycle. Conversely, suppose no negative cycle exists. Give every baseline
vertex a zero-cost edge from a super-source and compute exact Bellman--Ford
potentials. These are baseline prices satisfying the following copyable
certificate conditions; an outside element imposes one interval:

```text
gamma_i(a,e) = omega_i(B-a+e) - omega_i(B), when finite
p_b - p_a <= gamma_1(a,e) + gamma_2(b,e)
lower_e = max_b (p_b - gamma_2(b,e))
upper_e = min_a (p_a + gamma_1(a,e))
lower_e <= p_e <= upper_e
```

The first inequality holds for every finite pair, since the stored arc is
its minimum over original outside labels. It makes the last interval
nonempty whenever both sides exist. If only an upper side exists, choose
its minimum; if only a lower side exists, choose its maximum; if neither
exists, choose zero. No local constraint is needed on a missing effective-
domain exchange.

These original prices give, for every finite single exchange,

```text
omega_1(B-a+e)-omega_1(B) >= p_e-p_a
omega_2(B-b+e)-omega_2(B) >= p_b-p_e
```

Thus the baseline is locally optimal for the first valuation minus prices
and the second valuation plus prices. The local-to-global lemma proved from
the valuated exchange axiom makes it globally optimal for each priced
valuation. Prices cancel on every common basis, proving global optimality
of their sum. This also proves that every nonoptimal supplied baseline has
a negative compressed cycle.

The native Bellman--Ford procedure starts all baseline potentials at zero,
relaxes every compressed arc for at most the baseline rank passes, and
rejects a change on the last pass. This is precisely the super-source
negative-cycle test. At rank zero there are no exchanges or cycles; the
empty basis is the unique rank-zero basis and retains both valuation
constants.

Potentials are sums along at most rank-many arcs when no negative cycle
exists. Each interval endpoint is a potential plus one original exchange
increment. Exact numerator/denominator lengths are therefore polynomial in
the original finite-value answer lengths and the rank. The signs above are
the standard valuated-intersection price criterion; no novelty is claimed
for that optimality principle. This proves the proposition.

## 3. Compact fixed-rank valued reporting

**Theorem 2.** After certifying a supplied common baseline, the native
valuated backend returns the existing compact exact fixed-rank deletion
reporter, with no valuation, independence or price calls during queries.

**Proof.** The builder evaluates both original valuations on every baseline
exchange. For each ordered baseline pair it retains the outside label
minimizing the sum of its two increments, breaking ties by original label.
Unlike ordinary linear-cost compression, the cheapest label may depend on
both endpoints.

The complete [valuated proof](valuated-matroid-intersection.md) supplies the
needed cycle identity and literal decoding. Its joint convex-decomposition
lemma uses the two supporting initial matroids and ordinary intersection
integrality. Its valued matching lemma follows from assignment duality and
local-to-global optimality on a contracted/deleted valuation. Their cycle
argument allows repeated labels before the minimum-hop step, and does not
assume simultaneous exchange for an arbitrary matching.

For an optimal baseline, the minimum cycle through a failed baseline element
has cost exactly its replacement gap. Among minimum-cost cycles, choosing
the fewest labeled arcs forces all outside labels distinct and the literal
remove/add update to be an optimal common basis. This follows by applying
the matching direction to a supported optimal replacement: any repeated
label would give a shorter optimal cycle. No query-time basis optimizer is
needed.

Split each baseline vertex into minus/plus nodes, with zero split arcs and
one-hop exchange arcs. The generic exact distance/hub builder uses the
original primary cost and exchange-hop tie coordinate. Negative original
arcs are allowed; all directed cycles are lexicographically positive.
An explicit short path or a tight hub-tree concatenation is therefore simple
and reports a minimum-hop optimal cycle. The existing literal decoder
returns original basis IDs and its stored sum-of-valuations optimum.
Unreachable baseline demands report fixed-rank infeasibility; a deletion
outside the baseline leaves it optimal.

The returned object is exactly the existing compact `Oracle`. Original
callbacks, the full exchange tables and the original-ground split-price
certificate are preprocessing temporaries and are discarded before return.
Certificate callers may separately retain a certificate if desired; that
optional evidence has original-ground size and is not part of the compact
reporting bound. This proves the theorem.

## 4. Ordinary maximum cardinality after a rank drop

**Theorem 3.** The ordinary wrapper reports an exact minimum-cost
maximum-cardinality common independent set after one deletion, with the
sum of the two consecutive-rank support/reporting bounds and no query-time
original oracle calls.

**Proof.** Invoke the canonical certified ordinary weighted-intersection
initializer with requested cardinality equal to the original ground size.
Its certificate proves maximum possible common cardinality and minimum
signed linear cost at that cardinality. Verify the original certificate,
then construct that fixed-rank compact reporter from its baseline. If its
rank is positive, separately initialize and construct the reporter at one
smaller rank. All original linear costs have a specified meaning at both
ranks, so this objective is well defined.

Deleting one element lowers maximum common rank by at most one: remove that
element from any original maximum common set. If the top-rank query remains
feasible, its reported minimum cost is the correct maximum-cardinality
answer. Otherwise the next-rank reporter must be feasible and gives exactly
the appropriate minimum cost. Stored feasibility values choose the reporter
before any path traversal. At rank zero the single empty reporter suffices.
The retained union and records have the same asymptotic order as the original
rank reporter; query work is linear in that original maximum rank.

The wrapper retains neither costs nor original independence callbacks or
initializer certificates. Unknown original IDs have the same no-effect
semantics as the existing compact reporter. This proves the theorem.

This argument applies to ordinary linear costs only. An arbitrary fixed-rank
valuation is not assigned a value on a smaller independent set. Separate
valuations and initialization at two ranks would be an additional explicit
input, not an implied interface here.

## 5. Audited primary baseline and actual costs

The entire fixed-rank valuated companion is reviewed in this increment:
exchange signs and initialization convention, local-to-global and initial
matroids, joint decomposition, valued matching bound, cycle value identity,
minimum-hop literal update, phased support/reporting, signed distances and
actual rational lengths. The ordinary rank-drop corollary is reviewed against
the original maximum-cardinality and consecutive-rank objectives.

Iwamasa and Takazawa, [arXiv:2003.02424v3](https://arxiv.org/pdf/2003.02424),
Lemma 7 on printed page 9, states the classical valuated-intersection
baseline runtime recorded in the companion. Its primary text and common-
basis minimization definition were checked directly. Effective-domain
initialization remains essential: a bare oracle hiding its sole finite
basis does not supply one. The complete mathematical theorem pays this
classical initializer and any domain-basis initialization. The native
valuated backend here does not search for a common baseline. Its supplied
common basis is independently certified and rejected if nonoptimal.

For the valued construction, there are two baseline evaluations and at most
twice ground-size times rank exchange evaluations. Minimum-label compression
uses at most ground-size times rank-squared comparisons. The baseline price
test and the existing dense distance/reporting construction add at most
cubic rank arithmetic work. Original value-evaluation costs and all returned
rational bit lengths are paid separately. The independently callable
certificate verifier makes the same linear-in-exchange-table number of
original evaluations but performs no graph search.

Ordinary maximum-cardinality initialization is the same conservative
polynomial weighted-intersection implementation already documented for the
[ordinary reference](reference-ordinary-matroid-reporting.md), followed by
one smaller-rank initializer. Its temporary original-ground certificates
are discarded. Its preprocessing is not the manuscript's faster specialized
graph preprocessing.

Both final reporters retain only their canonical support, baselines, paths,
hub trees and exact optimum values. The original-ground price certificate
is explicitly outside that retained-record count. Lower-bound transfers,
simultaneous failures, later-changing costs or valuations and other deletion
objectives are outside this incremental review. Internal mathematical review,
finite exact checks and original certificate verification are not external
peer review or proof-assistant formalization.

**Attribution:** icekylinx and GPT-6 Astra Pro.
