# Algorithm Frontier

**Stable repository:** `algorithm-frontier`  
**Attribution:** Yilin Liu  · **AI contribution identifier:** GPT-6 Astra Pro  
**License:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)  
**Citation rules:** [`PROTOCOL.md`](PROTOCOL.md) · [`CITATION.cff`](CITATION.cff)

This repository curates the strongest supported result for each distinct
problem found in the supplied `aaa` research archives. Each problem has a
stable directory with:

- `README.md`: exact model, headline bound, parameter, and status;
- `proof.md`: proof map and the assumptions needed for the bound;
- `verify/`: several independent or root audit notes;
- `sources/`: the source-note paths used for the curation.

“Strongest” means the best non-dominated guarantee **within the same stated
model and parameter scope**. Incomparable parameterizations remain separate.
Superseded bounds are moved to `history/` or retained only in provenance; they
are not presented as current results. Conditional constructions say exactly
which external primitive or internal contract is assumed.

## Citation

> Yilin Liu and GPT-6 Astra Pro. *Algorithm Frontier*, version 2026.10.25
> (2026). CC BY-SA 4.0.

For a particular result, cite the repository record and the problem path, for
example `problems/general-matching/`. Keep the attribution names exactly as
written, link the canonical license URL, and state whether the cited files were
changed. Adapted versions must remain under CC BY-SA 4.0. The full stable
protocol is in [`PROTOCOL.md`](PROTOCOL.md).

## Status vocabulary

- **Reviewed research:** root and independent audits are present; this is not a
  claim of peer review or formal machine verification.
- **Conditional:** the theorem explicitly assumes named external primitives or
  an internal implementation contract.
- **Historical:** retained for traceability but superseded in the same scope.
- **Negative result:** a lower bound or obstruction with its exact model; it is
  not an algorithmic guarantee.

The full latest supplied source snapshot is preserved under
`sources/checkpoint-o/`; the general-matching manuscript package is under
`sources/matching-manuscript/`. `provenance/archive-manifest.json` records the
SHA-256 hashes of all original archives in the input directory.

## License boundary

Original curation material is CC BY-SA 4.0. Source notes may contain quoted or
third-party material under different terms; follow their local attribution and
license statements. The license does not grant patent, trademark, privacy, or
other rights that are not held by the licensor.
