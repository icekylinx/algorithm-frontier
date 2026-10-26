# Evidence for the restored static graph results

The four restored proof packages have scoped **ready for review** entries in
the [review registry](../../../reviews/README.md#supporting-manuscripts).
Their original source hashes are recorded at the end of each manuscript and
in the [checkpoint recovery index](../../../provenance/checkpoint-recovery.json).
These are complete written arguments with explicit dependencies. The finite
programs below provide additional evidence within their stated domains.

## Proof packages and dependencies

| Manuscript | Established scope | Remaining implementation or application boundary |
|---|---|---|
| [Exact demand trimming](../exact-demand-flow-trimming.md) | A coordinatewise subflow with exact positive nonsink demands; integral preservation and a near-linear arithmetic-operation ledger | The named deterministic dynamic-forest operations are a published data-structure dependency. There is no maximum-flow assumption. |
| [Selected-pair support balancing](../static-transportation-support-balancing.md) | Arbitrary row rank, a genuine pair per row, a new covering injection and strict component weight below twice the row total | The old injection may change. Dynamic maintenance of a separate private support is outside the static theorem. |
| [Confluent rounding and tails](../static-confluent-rounding-and-tail-bounds.md) | Near-linear simulation, completed-sink moments, load tails, a budget proportional to actual demand and a scoped local warm start | The exact published Conflt operations and dynamic-tree interface are named. Repeatedly reopening completed sinks needs separate dynamic accounting. |
| [Contact-rank odd crowns](../low-state-odd-crown.md) | Canonical contact envelope, min-cut certificate, exact optimum offset, LOW consequence and retained-mass counterexample | Ordinary bipartite matching suffices. The named almost-linear flow theorem is an optional faster implementation route. |

The current fast general-matching theorem has its own complete realization;
none of these independent static results is an unresolved premise of it.
All operation bounds charge physical input records and state their arithmetic
or word model. A small-instance program does not establish those asymptotic
data-structure bounds.

## Independent crown checks

From the repository root:

```sh
python3 manuscripts/graph-backends/verify/check_odd_crown.py
```

The program enumerates all row/bin incidence graphs with at most four bins
and three rows that admit a covering injection. It compares the construction
with an independent partial-matching enumeration and exhaustive captive-set
minimization. It checks 3,677 graphs, 56,249 contact sets and 138,470 optimal
injections. Every optimal injection must produce the same canonical envelope.

A second phase expands 615 seeded instances to physical graphs with singleton
or triangle bins, matched-remainder contacts, blockers and additional row
edges. An independent subset dynamic program computes the maximum matching
before and after crown removal on graphs through 18 vertices. It verifies
the exact offset without calling the repository's blossom solver.

The checker uses the Python standard library and rejects optimized Python
mode. Its scope excludes the numerical LOW interface, arbitrary-size proof,
factor-critical witness construction and imported almost-linear runtime.

## Independent flow and transportation checks

```sh
python3 manuscripts/graph-backends/verify/check_static_allocations.py
```

The flow phase covers 289 exhaustive and 1,000 fixed-seed integer instances,
including loops, parallel records, opposite arcs and outgoing sink flows.
It recomputes original-record divergences and checks exact target supplies,
integrality and coordinatewise domination after 3,262 cycle cancellations
and 4,103 path reductions.

The transportation phase covers 87 exhaustive and 1,500 fixed-seed instances.
It checks both original margins after 3,173 cycle cancellations, then
independently reconstructs the selected components, their native incidence
witnesses and the row-covering injection. The sample includes 625 cases with
row rank above three, maximum row rank nine, 940 cases with isolated bins
and 169 attaining the sharper integral top-row bound of twice the row total
minus two.

These reference routines explicitly list paths and cycles and may repeatedly
scan a graph. They are ordinary polynomial implementations for finite
verification. They use no matching implementation or dynamic-tree package,
and make no claim to implement the near-linear operation bounds. The script
uses the Python standard library and explicitly refuses optimized mode.

## Reading a verification result

Archive hashes establish the identity of recovered sources. A scoped review
entry records the theorem package that was inspected. An executable receipt
records a finite computation. These forms of evidence are kept separately so
that a reader can reproduce the relevant check and see what it establishes.
No external peer review or proof-assistant formalization is claimed.
