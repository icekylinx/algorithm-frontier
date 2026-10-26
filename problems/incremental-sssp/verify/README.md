# Verification and proof scope

The proof separates the frozen shortest-path detector, barrier
updates, epoch accounting and path-reporting interface. The stated graph
model uses **positive polynomial-range integer lengths**. It does not silently
include zero or arbitrary real lengths.

The quantitative composition retains its named hierarchy and routing
interfaces, charged initialization and finite update cap. Source-root
handling, current distances and output-sensitive simple path reporting have
separate obligations. The source map records the supporting arguments;
there is no runnable implementation of the complete dynamic data structure.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
