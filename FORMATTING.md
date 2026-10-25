# Document formatting

The repository has two presentation layers:

- `README.md`, `OVERVIEW.md`, `CONTENTS.md`, and `problems/*/README.md` are display-first surfaces;
- `proof.md`, `verify/`, and `sources/` carry proof maps, audit boundaries, and imported detail.

## Mathematical display

- Use fenced code blocks for executable snippets.
- Use code spans for displayed complexity on GitHub-facing pages: `2^(...)`, `exp(...)`, `poly(...)`, `eps`, `OPT`, and `Gamma(...)`.
- Do not add TeX math delimiters to a display-first page.
- Keep one bound per table cell and label time, space, update, query, and approximation resources separately.
- Preserve source notation inside `sources/`; display normalization is not a mathematical edit to imported text.

## Result tables

Problem READMEs use this order whenever the model supports it:

1. Guarantee
2. Objective
3. Time
4. Space
5. Parameters
6. Representation and model
7. Lower-bound type
8. Status

If a field is not claimed, say so explicitly. Do not infer a space bound from a time bound or turn a conditional backend into an implementation claim.

## Linking and filenames

Use relative links from the file that owns the claim. Checkpoint files keep their original names and remain under their checkpoint directory. Source maps name the exact source path and any parent checkpoint dependency.

New curation files use lowercase hyphenated problem directories and stable filenames: `README.md`, `proof.md`, `sources.md`, and at least two focused files under `verify/`.
