# material-c4a0ef05c360

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# COORD_C622_CANONICAL_SCOPED16_V1 — Recovery capsule part 2/2

Companion part 1 is [internal-source-reference], 15305 UTF-8 bytes, SHA256 d5846089dd79e70e4aa35f67d5d66b8480c3dd72bca1de45359a281931f632aa. This second normalized payload is 13864 ASCII base64 characters, SHA256 a07c9401e26a450fd7fdeb65f99ac82ebee2c88830a1310f0d35844c3c6e570e. Both parts reconstruct canonical VQ20_C622_ROUTE88_118_G12 exactly, not C622_HOMOTOPY_POSITIVE and not a new smaller body.


[Encoded source block omitted; the code in this passage is incomplete.]


## Complete decoder
Save the following exactly as RECOVER_C622_SCOPED16.py, UTF-8/LF with one final newline:2053 bytes, SHA256 cf90d8a2240f4b7154a902bc6ff558dbd2f3157683adadda1485a882cfd17d28. This decoder was executed successfully against both ordered payloads in an initially absent destination.

```python
"""Recover COORD_C622_CANONICAL_SCOPED16_V1 from its two ordered materials."""
import base64, hashlib, json, lzma, re, sys
from pathlib import Path
assert __debug__, 'Assertions must be enabled'
assert len(sys.argv) == 4, 'Usage: RECOVER_C622_SCOPED16.py NEW_DIRECTORY PART1.md PART2.md'
sha = lambda b: hashlib.sha256(b).hexdigest()
expected = [(14000, '79523072502560ef2e44d7b6e8f24f0ce566868e396e7cb65e8f4536ea693e19'),
            (13864, 'a07c9401e26a450fd7fdeb65f99ac82ebee2c88830a1310f0d35844c3c6e570e')]
parts = []
for name, (size, digest) in zip(sys.argv[2:], expected):
    blocks = re.findall(r'```base64\s*\n(.*?)\n```', Path(name).read_text(encoding='utf-8'), re.S)
    assert len(blocks) == 1, (name, len(blocks))
    b = ''.join(blocks[0].split()).encode('ascii')
    assert len(b) == size and sha(b) == digest, (name, len(b), sha(b))
    parts.append(b)
b = b''.join(parts)
assert len(b) == 27864 and sha(b) == '6a7d42eeabc1365c9dc122a9e62e6127e779db025765c6cbb37107cb31788638'
z = base64.b64decode(b, validate=True)
assert len(z) == 20896 and sha(z) == '74dfffa9c2c4972bf1d4b99c269e3c3df99eaa01549548b858c542b431fa3597'
r = lzma.decompress(z)
assert len(r) == 68603 and sha(r) == '63b9a7de970fa8fb01f43ce10bec573441e5afeebe4ef2d3b7031ea6fb64c9ca'
files = json.loads(r)
assert len(files) == 16
manifest = json.loads(files['MANIFEST.json'])
assert sha(files['MANIFEST.json'].encode()) == '0ba857a7d98fa85ad04ac1800886a9c450a5dc4c25e02177832adf9e0275d6af'
assert len(manifest) == 15
for name, rec in manifest.items():
    data = files[name].encode('utf-8')
    assert len(data) == rec['bytes'] and sha(data) == rec['sha256'], (name, rec)
out = Path(sys.argv[1])
assert not out.exists(), 'Destination must not exist'
for name in files:
    rel = Path(name)
    assert not rel.is_absolute() and '..' not in rel.parts
out.mkdir(parents=True)
for name, text in files.items():
    p = out / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(text.encode('utf-8'))
print('COORD_C622_CANONICAL_SCOPED16_SOURCE_RECOVERY_PASS')
```

## Reconstruction and checks

```sh
python -B -S RECOVER_C622_SCOPED16.py NEW_SOURCE PART1.md PART2.md
python -B -S NEW_SOURCE/REPLAY_SCOPED.py NEW_PROOF
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B NEW_SOURCE/SMOKE_NUMERIC.py NEW_PROOF
```

Observed markers: COORD_C622_CANONICAL_SCOPED16_SOURCE_RECOVERY_PASS; SCOPED_EXACT_A_PASS; SCOPED_EXACT_B_PASS; COORD_C622_SCOPED_CANONICAL_AB_MASS_CONTROLS_PASS; COORD_C622_SCOPED_NUMERIC_ENTRY_PASS. Exact runtime CPython3.13.5 standard library with assertions enabled; numerical runtime NumPy2.3.5,SciPy1.17.0,float64,one BLAS/OMP thread. The exact replay and numerical entry test both ran; the newly added generic rooted_correct driver has not been claimed to produce any new child. Finite optimizer failure is not an infeasibility theorem.

The decoded16files are COMPACT_INPUT.json,GENERATOR.json,README.md,REPLAY_SCOPED.py,SMOKE_NUMERIC.py,MANIFEST.json,core/RECONSTRUCT.py,core/check_A.py,core/check_B.py,core/centred_mass.py,methods/G_FREE_CODEC.py,methods/contact.py,methods/flexible.py,methods/SVD_CORRECT.py,methods/minnorm_qp.py,methods/scope.py. MANIFEST.json1673bytes SHA2560ba857a7d98fa85ad04ac1800886a9c450a5dc4c25e02177832adf9e0275d6af contains exact byte counts/hashes for every other decoded file. The source map is68603bytes SHA25663b9a7de970fa8fb01f43ce10bec573441e5afeebe4ef2d3b7031ea6fb64c9ca. All literal coordinates, contact plan, free controls and non-default parameters are included, not replaced by hashes.

The four core exact modules and methods contact/flexible/SVD_CORRECT/minnorm_qp/G_FREE_CODEC are unchanged FULL76 sources. scope.py retains complete atlas_generator/quotient from ANY_UNION.py, arrows from TREE_REPAIR.py and routing from ROOTED_ROUTING.py, with standalone imports and new load/rooted_correct entry points. It excludes unrelated historical bodies rather than required helpers. Canonical parent figure-0373 was read completely, SHA2568a9f5de8374e75eb2e09766c3546f750afd74102ae1fc3bddef86c4da45dc68d. Descendants must name that literal result as parent. FULL76 recovered dictionary312622bytes SHA256617f94b82a54bf54cd7cce67fbf5d506cc3d2b9431a7c64b587984ea429992f6 supplies provenance, not an additional decoding dependency.

Exact replay first reconstructs GENERATOR.json from lossless COMPACT_INPUT.json and checks byte identity; runs independent A/B hull/true-incidence/filled-mass/all-feature pipelines; verifies348positive centered tetrahedra and exact zero first moments. Both auditors correctly classify regular tetrahedron446/weak000 and deliberately weak prism446/weak123 and reject them as winners; each rejects three invalid fixtures.

Expected outputs: GENERATOR.json11841bytes SHA2563cbd90d799189108f26b941800c8fa79a6f1c5abb17b2db614f0e54f57fffee7; raw.json15437bytes SHA256ac01d1625274b64f336a715e1f5462f40686f647f0b7d1a4d90a5ee21765adb5; A.json and B.json311825bytes each SHA256142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0; RECEIPT.json681bytes SHA2566ca0671aace64125886235d1060235f93290915c512bd7e9ac1e0789d7ec3f8a. True176/311/137,strict110/weak000,all137supports active,1244edge primitives and zero degeneracy counters,Sinput3/Urawlex94. Separate mass348positive tets,common centered denominator/maxinteger56802bits. This is the scoped canonical replay, NOT a claim to repeat the historical ten-case aggregate.

Observed numerical smoke:314freecoordinates; minimum fullpoint escape including roots1.069843689360149e-8; minimum nonowner slack0.0008816302267673493; maximum physical-vertex discrepancy6.564193633096238e-15; centroid discrepancy7.632783294297951e-17. This proves a usable starting numerical entry, not smaller complexity. Any numerical child still needs exact reconstruction, actual maximal incidence, independent full checks and complete new recovery preservation.
