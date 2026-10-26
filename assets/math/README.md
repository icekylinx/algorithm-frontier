# Standalone equation images

These SVG files are generated from the exact display source next to each
image in its manuscript. Every image includes its own glyph paths, an
accessible source title and a white background. There are no scripts,
external fonts or remote resources.

The first 24 hexadecimal characters of the formula's SHA-256 digest name its
image. `manifest.json` binds the complete source hash, SVG hash and renderer
version. The builder rejects a digest collision rather than overwriting a
different formula.

```sh
npm ci --prefix tools/math-renderer
python3 tools/build_math_assets.py
python3 tools/build_math_assets.py --check
```

The last command uses only Python. MathJax 3.2.2 is a pinned optional authoring
dependency, not a dependency of any algorithm or of reading the repository.
Edit a manuscript's `math-display` source comment and rebuild its image;
do not hand-edit a generated SVG. Mathematical statements and their review
scope remain in the problem pages and proof manuscripts.
