# material-8f2e17ae3d9e

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# Recovery capsule part 5/5 — COORD_IMPLICIT_CAP_SCOPED_DELTA16_V1

Final base64 characters [31200,38464). The ordered first four materials are [internal-source-reference], [internal-source-reference], [internal-source-reference], [internal-source-reference]. All five parts plus the four exact Bright COMPLETE33 dependency parts named in part1 are required. Canonical accepted own110 remains C622. These are four independent fully audited nonwinners and reusable methods, not an improved Gömböc.


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


## Literal decoder
Save the following exact code, with its final newline, as RECOVER_SCOPED_DELTA.py: 2048 bytes, SHA256 75bd18b490283ad8f41d85b9ca5ca7de6ef1ba309ed6c235bb9bce2fee54f979.

```python
#!/usr/bin/env python3
"""Recover scoped implicit-cap additions against the exact Bright COMPLETE33 source."""
import base64, hashlib, json, lzma, pathlib, re, sys

def checked(data, count, sha):
    assert len(data) == count, (len(data), count)
    assert hashlib.sha256(data).hexdigest() == sha
    return data

def main():
    assert len(sys.argv) == 8, 'Usage: python RECOVER_SCOPED_DELTA.py OUT BRIGHT_SOURCE PART1 PART2 PART3 PART4 PART5'
    out, bright = map(pathlib.Path, sys.argv[1:3])
    chunks = []
    for p in map(pathlib.Path, sys.argv[3:]):
        blocks = re.findall(r'```base64\s*\n(.*?)\n```', p.read_text(), flags=re.S)
        assert len(blocks) == 1
        chunks.append(re.sub(r'\s+', '', blocks[0]))
    text = checked(''.join(chunks).encode('ascii'), 38464, 'e32d8600c790c8434ec26a90ee9ce17cff22d9568f649d47f919e02667ce5e66')
    compressed = checked(base64.b64decode(text, validate=True), 28848, 'b70e6121aa669bb8dd1a22910bbbf42be60af98b985a19649adf37033c584574')
    raw = checked(lzma.decompress(compressed), 138613, 'de8058c7e18c3269a52d7e57046d267dd612e7040e9f3acb85af1be4ffcff211')
    files = json.loads(raw)
    assert len(files) == 16
    out.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        rel = pathlib.PurePosixPath(name)
        assert not rel.is_absolute() and '..' not in rel.parts
        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(content.encode('utf-8'))
    for name, meta in json.loads((out/'MANIFEST.json').read_text()).items():
        checked((out/name).read_bytes(), meta['bytes'], meta['sha256'])
    for name, meta in json.loads((out/'SOURCE_DEPENDENCIES.json').read_text()).items():
        data = checked((bright/name).read_bytes(), meta['bytes'], meta['sha256'])
        dest = out/'source'/name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    print('IMPLICIT_CAP_SCOPED_DELTA16_AND_SEVEN_BRIGHT_DEPENDENCIES_RECOVERED')

if __name__ == '__main__':
    main()
```

## Commands and terminal expectations
First reconstruct BQ13_D100_COMPLETE33 with the decoder in its part4. Then, with paths chosen by the operator:

```
python -B -S RECOVER_SCOPED_DELTA.py recovered_cap recovered_bright part1.md part2.md part3.md part4.md part5.md
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -S recovered_cap/joint/REPLAY_EXACT.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B recovered_cap/joint/REPLAY_NUMERIC_SCOPED.py
```

Recovery must print IMPLICIT_CAP_SCOPED_DELTA16_AND_SEVEN_BRIGHT_DEPENDENCIES_RECOVERED. Exact replay must end with EXACT_CAP_MASS_JACOBIAN_DIVERGENCE_AND_SPD_CONTROLS_PASS, EXACT_RECESSION_RAY_AND_SOURCE_FACET_MAPS_PASS, COORD_IMPLICIT_CAP_FOUR_EXACT_NONWINNERS_AB_MASS_JACOBIAN_COLD_PASS, NO_OWN110_AND_NO_ACCEPTED_RECORD_CHANGE. Numerical checkpoint/survey replay must end with IMPLICIT_CAP_SCOPED_HEX_AND_CORRECTED_SURVEY_PASS. Exact replay is Python standard library only. Numeric replay environment used: Python3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, one thread; production random seed17092026, complete per-stage non-default parameters in EXPERIMENTS_COORD.json and SELECTED_NUMERIC.json. This replays checkpoints and reports, not the optimizer's elapsed times or exact trajectory.

The four exact objects use prefix COORD_IMPLICIT_CAP_: TRIAL_TILT_PANEL_D10000 V104/E156/F54 C312 strict233; TRIAL_TILT_PANEL_D500 V100/E150/F52 C300 strict233; TRIAL_AXIS_PANEL_D300 V82/E123/F43 C246 strict233; TRIAL_TILT_D100 V18/E27/F11 C54 strict9,9,16. All weak000, no predicate zeros, A/B full real incidence and all-feature results agree, third positive centered integration agrees. Their common centered denominator/max centered coordinate bitlengths are respectively5044/5046,2487/2489,1919/1921,438/440. Positive centered tetrahedron counts204,196,160,32. Active supports respectively54/54,52/54,43/44,11/54; do not equate input rows with active facets.

Exact expected output filenames, byte counts and SHA256 values (all input,H,A,B,MASS,SUMMARY outputs) are literal in joint/EXACT_EXPECTED.json: 7468 bytes, SHA256 ee8c066a7b2570c1853edbd7b9f9007fead6fc80b1a11afbd4d613038f38a469. Derivative certificate: 1249 bytes, SHA256 4d1a1687762b290caf396bdf0dc2d2f473dc75df423b343edfc58383a9a4b3cb. Continuation labels2459 bytes SHA25638526e238d06b06ed7918d21527f35e42ed2f807df309a5226af04901f95214c. Corrected rounding bank61885 bytes SHA2567da35a00b5607afb37a3a24ec76c2205dcd02bde8d0ec80ee544903aa5622c9f; corrected survey31024 bytes SHA25601fc5f2dd208b9386f22318b7cc2c5a40cafbeaaecc08833ad7d419d34a3a5fd. Five numerical checkpoint .npy hashes and output names are in joint/NUMERIC_EXPECTED.json and are checked by replay. SCOPE.md records historical invalid raw-polar/triangulated survey as excluded; do not use v1 counts as mechanics evidence. The two below-floor C28 survey proposals are excluded before equilibrium analysis. The incomplete axis-protected numerical stage has a preserved checkpoint, not a terminal optimization result.
