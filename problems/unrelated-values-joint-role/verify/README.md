# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [The exact-factor-two endpoint for arbitrary unrelated allocation](../exact-two.md)
- [Unrelated-value allocation with one shared setup and assignment budget](../setup-budget.md)
- [Integer-quota time tradeoffs for compulsory unrelated two-value allocation](../two-value-tradeoffs.md)

## Mathematical evidence

- One masked polymatroid represents each original resource across light and heavy roles, preserving shared capacity.
- The changing role LP retains a protected original full allocation with uniform rational descriptions.
- The setup companion keeps one combined original budget on an actual selected basis; enumeration proves exact two in <code class="math">2^q</code> polynomial time.
- J2 and the discrete factor-<code class="math">d</code> companion prove their exact quota recovery for compulsory player-specific values in <code class="math">\{0,u,a\}</code>.
- The [native realization proof](../reference-realization.md) establishes the exact original resource LP, nonnegative support separator, signed lower-prefix face, persistent dual dummy and original-basis budget extraction. The canonical weighted omission, streamed cover, rational-grid and oracle lower-bound dependencies have been checked in their actual models.

## Executable evidence

[check_joint.py](check_joint.py) independently enumerates original feasible
integer allocations for 39 original inputs, comparing exact-half outputs
and 17 near-two calls. Five calls use actual streamed covers, including the
logarithmic-block branch on four owners. Twelve direct
signed-cost prefix roundings check cost and every prefix at the same
integer point; 301 compulsory quota targets compare sound failures and
relaxed outputs with the original integer optimum. Fixtures include shared
original capacities with opposite value orders, mixed light/heavy roles,
persistent dummy credit inside the light ground, original loops, empty
resources, rank zero, forced-role failures, early relaxed success retaining
all current light owners, and a 101-bit supply. A 121-bit
rational ratio checks the safe cover-base shortcut. The original verifier
is tested with its producer disabled; two forged records and six malformed
inputs are rejected.

[verify_profile_certificates.py](../../../tools/verify_profile_certificates.py) checks the following finite claim:

Integer-quota arithmetic: <code class="math">d=2,\ldots,30</code> and every <code class="math">d&lt;K\le399</code> (11,107 cases) satisfy <code class="math">K/(K-\lceil K/d\rceil)\le(d+1)/(d-1)</code>; every <code class="math">1\le K\le d</code> satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed. This applies only to the compulsory J2 and factor-<code class="math">d</code> quota arithmetic, not shared-resource or setup coupling.

Run from the repository root:

```sh
python3 tools/verify_profile_certificates.py
python3 problems/unrelated-values-joint-role/verify/check_joint.py
```

These finite checks do not establish the asymptotic proof. The native
backend executes the actual mask/LP/recursion/rounding construction, using
finite active-basis LP enumeration with separately charged time and
potentially exponential projected-support storage. It does not implement
the fast polynomial LP/intersection primitive costs or compute the
affordable-support cap used in the sharper compulsory theorem.

## Model and verification boundaries

Near-two and the <code class="math">2^q</code> exact-two endpoint allow optional player bases. The faster J2 and discrete pair-value tradeoffs require compulsory players. Adding a dummy value does not preserve the two-value premise; finite quota tests do not check shared-resource or setup constructions.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
