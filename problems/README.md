# Curated problems

The catalogue is organised by [problem family](../docs/FAMILIES.md). Each result directory is a compact record with the same core fields:

- `README.md`: problem, output, model, guarantee, time, space, parameters, comparator, and claim status;
- `proof.md`: a short proof map when the record has one;
- `verify/`: executable or finite checks when available;
- `sources.md`: exact source paths, checkpoint provenance, and attribution.

A numerical bound is compared only after its model, parameterisation, representation, assumptions, and comparator have been matched. The [review registry](../reviews/README.md) records which parts have received proof, algorithm, source, and finite-check review.
