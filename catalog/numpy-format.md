# NumPy cache representation

The released NumPy files contain no pickled object arrays. Load them with `allow_pickle=False`.

Twenty-five historical NPZ caches required conversion. Forty-eight arrays of scientific string labels (`primitive_keys`, `mode_meta`, `guard_keys`, `guard_kinds`) now use native fixed-width Unicode. Their shapes, ordering and exact strings are preserved. Numeric NPY members remain byte-identical.

In `sources/astra/agent-2/artifacts/baseline/numerical.npz`, the 137 ragged face lists are represented by two integer arrays instead of the old `faces` object array:

```python
with numpy.load(path, allow_pickle=False) as data:
    flat = data["faces_flat"]
    offsets = data["faces_offsets"]
    faces = [flat[a:b].tolist() for a, b in zip(offsets[:-1], offsets[1:])]
```

There are 622 vertex-index entries and 138 offsets. Historical scripts using the old `faces` key must read the new representation. The face lists are unchanged.

Another 36 NPZ containers retain their existing scalar Unicode scientific `kind` labels. Their numeric and Unicode member bytes are unchanged; only ZIP metadata is regenerated. [Conversion metadata](numpy-conversions.json) records all 61 files and the original/public hashes.

The conversion read a restricted literal format without executing pickle constructors.
