# Shared mathematical manuscripts

These manuscripts supply lemmas, interfaces and scoped counterexamples used
by several result families. Start from the relevant
[result card](../README.md#results) and its `sources.md</BT>; the
[complete proof index](../CONTENTS.md#shared-manuscripts) lists every shared
manuscript.

| Directory | Mathematical role |
|---|---|
| [Graph backends](graph-backends/) | Routing, sparsification, dynamic hierarchies, numerical clients, path reporting and explicit update contracts |
| [Allocation and scheduling](allocation-and-scheduling/) | Resource polymatroids, allocation invariants, quota extensions, exact budgets, scheduling transfers and their comparators |
| [Matching and routing](matching-and-routing/) | Haxell-type matching, independent transversals and implicit path or bundle interfaces |
| [Mechanism boundaries](mechanism-boundaries/) | Explicit counterexamples to specified carriers, monotonicity rules or update mechanisms |

## Reading a dependency

A proved interface lemma establishes its stated contract under its own input
assumptions. A conditional composition assumes the named provider contract;
an implementation of a related static primitive need not satisfy dynamic
initialization, notifications, retirement, recourse or output accounting.
Those obligations stay visible where the interface is used.

A counterexample to one mechanism is scoped to that mechanism. It does not
establish a lower bound for every algorithm solving the parent problem.
Likewise, a source comparison can explain which external theorem supplies a
primitive without establishing a new qualitative algorithm.

The [complexity guide](../docs/COMPLEXITY.md) defines the representation and
cost conventions. [Provenance](../provenance/README.md) maps historical
filenames to current manuscripts.
