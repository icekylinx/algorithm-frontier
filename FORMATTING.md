# Document formatting

The repository has two presentation layers:

- `README.md`, `OVERVIEW.md`, and `problems/*/README.md` are display-first surfaces;
- `proof.md`, `verify/`, and `sources/` carry proof maps, audit boundaries, and imported detail.

## Mathematical display

- Use fenced code blocks for executable snippets.
- Use `$$ ... $$` for displayed LaTeX in authored curation documents.
- Keep one displayed expression per logical bound and name every parameter used by it.
- Do not mix an approximation factor, a time exponent, and a space exponent in one unlabeled cell.
- Preserve source notation inside `sources/`; formatting normalization is not a mathematical edit to imported text.

## Result tables

Problem READMEs use this order whenever the model supports it:

1. Guarantee
2. Objective
3. Time
4. Space
5. Parameters
6. Model
7. Lower bound
8. Status

If a field is not claimed, write that explicitly. In particular, do not infer a space bound from a time bound or treat a conditional backend as an implementation result.

## Linking and filenames

Use relative links from the file that owns the claim. Checkpoint files keep their original names and remain under their checkpoint directory. Source maps should name the exact source path and any parent checkpoint dependency.

New curation files use lowercase hyphenated problem directories and stable filenames: `README.md`, `proof.md`, `sources.md`, and at least two focused files under `verify/`.
