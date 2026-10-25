# Publishing and maintenance

`algorithm-frontier` is a public GitHub repository. The public branch is `main`; all public claims must remain source-linked and must preserve their license boundaries.

## Before pushing

Run:

```bash
python3 tools/validate_curation.py
python3 tools/check_latex_delimiters.py
python3 tools/verify_incremental_sources.py
git diff --check
```

GitHub Actions repeats these checks for pushes and pull requests through `.github/workflows/curation.yml`.

## Adding a checkpoint

1. Keep the archive hash and the original checkpoint manifest.
2. Add the increment under `sources/checkpoint-<letter>/` without flattening its payload.
3. Record the parent checkpoint, parent archive hash, exclusions, and review scope.
4. Update the provenance manifests and delta summary.
5. Link the checkpoint from the relevant complexity or problem index.

## Public release discipline

Keep imported manuscripts, notices, and licenses in their source boundary. A curated README may summarize a result, but it must not silently strengthen the source claim. Use the commit SHA in citations and identify any changed curation layer.
