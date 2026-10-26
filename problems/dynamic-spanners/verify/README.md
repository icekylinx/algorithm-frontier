# Verification and proof scope

The proof keeps the tracked-terminal four-fifths construction and
the full-horizon five-sixths construction separate. They have different
recourse contracts even when a headline stretch expression looks similar.

Flat projection, clipped reporting, finite horizons, restart charges and
published-edge changes are accounted for explicitly. The
[constructed APSP hierarchy](../../apsp-frontier/proof.md),
[flat witness family](../../../manuscripts/graph-backends/destructive-apsp-path-support-extractor.md)
and [clipped-reporting construction](../../../manuscripts/graph-backends/clipped-walk-queries-and-dynamic-spanner.md)
supply the generic lemmas' inputs, including update work and recourse.
Both complete theorem instantiations are ready for review. No executable
end-to-end dynamic spanner is supplied.

The zero-edge class extension is a local deterministic reduction ready
for review. It preserves zero-cost connectivity by current output
paths, processes zero-edge deletions before publication, and charges
the additional class's vertices, updates and recourse. It adds no
dynamic SCC dependency. Positive weighted classes still incur their
stated dyadic stretch factor.

Adaptive histories require providers that satisfy the same deterministic
history contract. Recourse counts actual published edge changes;
enumerating the whole current spanner separately costs its output size.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
