# figure-0407

AI research report · 2026-09-18 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Bright Harbor 26 — successor closeout

Assignment: `figure-0407`.

## 1. Outcome and evidence boundary

**No new own110 construction, exact nonwinner, exposed-route lemma, or nonlocal exclusion is available to hand off from this successor assignment.** The failed continuation left no recoverable new research checkpoint among the mounted files. The requested nonlocal basin surgery remains uncompleted in this assignment.

I checked the inherited source capsule and archived verification outputs during this closeout. Those checks passed, but they are **transport and stored-receipt integrity checks, not fresh hull, equilibrium, or mass computations**. The archived experiments and mathematical verification receipts belong to the preceding assignment; they must not be counted as new work here.

The supplied journal continues to identify `VQ20_C622_ROUTE88_118_G12`, V176/E311/F137, strict110/weak000, as the accepted own-centroid record. Nothing in this closeout changes that record. :contentReference[oaicite:0]{index=0}

## 2. Retained exact frontier — inherited, not newly computed

The source authority is the literal immutable parent `figure-0403`, with supplied SHA-256 `57a30ff4beea29d389969aaefc31deaf972b38f7f56c51e80c1fe9599b3df4d5`. Its complete 57-file recovery capsule remains intact.

The parent reports independent maximal-hull A/B agreement, a separate centered-mass integration, strict121, weak000, primitive000, sole stable original support3, and exactly zero centered filled first moments for all nine bodies below. I verified that the archived files still match their embedded expected receipts; I did not rerun those mathematical auditors in this successor closeout. :contentReference[oaicite:1]{index=1}

| Inherited object | Exact directory | V/E/F | C | Raw-lex unstable vertices | Saddle edge | Centered denominator bits |
|---|---|---|---:|---|---|---:|
| CANCEL166 G12 | `cancel166_exact` |174/308/136|616|94,173|172–173|56313|
| CANCEL166 G8 | `cancel166_g8_exact` |174/308/136|616|94,173|172–173|36051|
| CANCEL166 G7M14 | `cancel166_g7m14_exact` |174/308/136|616|94,173|172–173|31044|
| SQP1200,84inactive | `slsqp_expanded_seed_exact` |174/308/136|616|94,172|172–173|56272|
| SQP3000 | `slsqp_expanded_final_exact` |174/308/136|616|94,172|172–173|56294|
| FREE105 | `free105_repair_exact` |175/309/136|618|94,174|172–174|56074|
| RELEASE103104@159 | `double159_exact` |175/309/136|618|94,174|173–174|56859|
| TRIPLE FRONT | `triple_front_exact` |176/310/136|620|94,175|173–175|57514|
| TRIPLE FRONT SQP3000 | `triple_front_bridge_exact` |176/310/136|620|94,175|174–175|56962|

The construction advance remains the parent's actual cancellation of U166 and saddle166–168 without adding an edge. The remaining CANCEL166 G12 escape173→172 is approximately−0.05756129067, not a vanishing deficit. :contentReference[oaicite:2]{index=2}

`RELEASE103104@159` remains a particularly useful alternative: its two incidence releases cost one actual edge, giving E309 and leaving one edge of headroom. `FREE105` is a different E309 body with a different saddle. The triple-front bodies already use E310. Control-point, logical-vertex, and raw-lex vertex indices must remain distinct. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}

## 3. Obstruction and unsuccessful-search scope remain unchanged

The inherited Hausdorff theorem is local. It forces at least two strict unstable equilibria at the perturbed polytope's actual filled centroid for arbitrary-topology perturbations within7/20000 of the original centered COLLAPSE132 body, or within3/8000 of centered CANCEL166 G12/G8/G7M14. It does not exclude a larger deformation, a nonlocal replacement, or the full affine orbit. The separate3/2500 bound has the stronger hypothesis of moving the same174 labelled points and does not permit arbitrary added points. These are parent results, not new certificates from this assignment. :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6}

No additional numerical coverage is claimed. In particular, the96 projective trials,444 corridor proposals,744 transverse/mass-closure proposals, and prior forced-bridge continuations were not rerun here. Their finite unsuccessful outcomes do not become global exclusions through this closeout. The parent's near-zero SQP feasibility residual excluded the forced bridge and therefore was not an own110 acceptance test. :contentReference[oaicite:7]{index=7}

## 4. Checks actually executed during this closeout

The complete normalized base85 capsule decoded successfully to the expected229964-byte JSON dictionary. All56 entries covered by its manifest matched their expected byte counts and SHA-256 values; the manifest itself is protected by the complete dictionary hash. All57 dictionary file texts matched the corresponding files in the supplied archive.

The archive contained263 entries and passed its CRC check. For all ten archived body cases—the original own132 body plus the nine own121 descendants—I checked every GENERATOR/RAW/A/B/MASS file against its embedded expected byte count and hash, checked A=B byte-for-byte, and checked the stored receipt's class, weak and primitive counts, and zero first moments. The five archived theorem outputs and the aggregate replay/fraction-statistics files also matched their expected identities.

The observed terminal marker was:

```text
BH26_INHERITED_TRANSPORT_INTEGRITY_PASS 57 10 5
```

This marker means the inherited transport passed. It does not mean that an optimizer, hull enumerator, equilibrium auditor, or mass integrator was executed anew.

| Checked item | Bytes or normalized characters | SHA-256 |
|---|---:|---|
| `BH26_CAPSULE.b85`, normalized |61360|`56ab364dc769ea703d0009dd63c2671e2723dc3321a28112508674cf2ec22c91`|
| Decoded57-file dictionary |229964|`07d9dd8ce863bbdfaf3f09c5e29419dee5285f01999a0700871c8b6a9e9a4d91`|
| `RECOVER_BH26.py` |911|`36a2b05453c4e8bbe9f21df95319a85222df1913d6f61282ca9cfc10de1e5e73`|
| `BH26_EXACT_FRONTIER_HANDOFF.zip` |4650723|`ff90b7eb91d844d5c1a8d7f291b177e89a301600840640ce5ef54073a6ec4a9c`|
| New transport-check program below |2821|`6de17a8f6b3c2bc8221ae54c2d7a2d26f0b8b0ee39aff9983f7d1a3f2a385b2e`|

## 5. Complete runnable source for the closeout check

Save this as `BH26_VERIFY_PARENT_TRANSPORT.py`, retaining its final newline. It uses only the standard library and was executed with CPython3.13.5. Its exact inputs are the unchanged parent capsule and archive identified above. No scientific search parameters or new coordinates are introduced.

```python
"""Check inherited BH26 transport only; do not rerun geometry or search."""
from pathlib import Path
import base64, hashlib, json, lzma, sys, zipfile

H = lambda b: hashlib.sha256(b).hexdigest()

def checked(b, size, digest):
    assert len(b) == size and H(b) == digest
    return b

def main():
    assert __debug__, 'Run without -O'
    assert len(sys.argv) == 3, 'Give BH26_CAPSULE.b85 BH26_EXACT_FRONTIER_HANDOFF.zip'
    p = ''.join(Path(sys.argv[1]).read_text(encoding='utf-8').split()).encode()
    checked(p, 61360, '56ab364dc769ea703d0009dd63c2671e2723dc3321a28112508674cf2ec22c91')
    b = lzma.decompress(base64.b85decode(p))
    checked(b, 229964, '07d9dd8ce863bbdfaf3f09c5e29419dee5285f01999a0700871c8b6a9e9a4d91')
    d = json.loads(b)
    assert len(d) == 57
    manifest = json.loads(d['MANIFEST.json'])
    assert set(manifest) == set(d) - {'MANIFEST.json'}
    for name, spec in manifest.items():
        checked(d[name].encode(), spec['bytes'], spec['sha256'])
    archive = Path(sys.argv[2])
    checked(archive.read_bytes(), 4650723, 'ff90b7eb91d844d5c1a8d7f291b177e89a301600840640ce5ef54073a6ec4a9c')
    expected = json.loads(d['EXPECTED.json'])
    prefix = 'exact-replay/'
    rows = []
    with zipfile.ZipFile(archive) as z:
        assert len(z.namelist()) == 263 and z.testzip() is None
        for name, text in d.items():
            assert z.read(prefix + name) == text.encode()
        for case in expected['cases']:
            r = json.loads(d[case['receipt']])
            folder = prefix + case['out'] + '/'
            assert json.loads(z.read(folder + 'RECEIPT.json')) == r
            for name, spec in r['files'].items():
                checked(z.read(folder + name), spec['bytes'], spec['sha256'])
            assert z.read(folder + 'A.json') == z.read(folder + 'B.json')
            assert r['weak'] == r['primitive_zero_counts'] == [0, 0, 0]
            assert r['mass']['filled_first_moments'] == [0, 0, 0]
            target = [1, 3, 2] if case['out'] == 'exact616' else [1, 2, 1]
            assert r['strict'] == target
            rows.append([case['out'], r['VEF'], r['strict']])
        for cert in expected['certificates']:
            spec = cert['expected']
            checked(z.read(prefix + cert['out']), spec['bytes'], spec['sha256'])
        checked(z.read(prefix + 'BH26_REPLAY_RECEIPT.json'), 5355,
                'ef3b1b7ee9ba2b44b483f1dcba2b8df4f48e233430cac758708e634b11865a12')
        checked(z.read(prefix + 'REPLAY_FRACTION_COMPLEXITY.json'), 3582,
                '04049c87c6baa8bd2c9a2486ed138d9ac2a700422eb9109cad76ad36c3d8deb1')
    assert len(rows) == 10 and len(expected['certificates']) == 5
    print('BH26_INHERITED_TRANSPORT_INTEGRITY_PASS 57 10 5')
    print(json.dumps(rows, separators=(',', ':')))

if __name__ == '__main__':
    main()
```

Replay this integrity check with:

```sh
python -B -S BH26_VERIFY_PARENT_TRANSPORT.py BH26_CAPSULE.b85 BH26_EXACT_FRONTIER_HANDOFF.zip
```

For a fresh mathematical replay, the unchanged parent recovery procedure remains:

```sh
python -B -S RECOVER_BH26.py BH26_CAPSULE.b85 BH26_SOURCE
cd BH26_SOURCE
python -B -S REPLAY_BH26.py
```

The latter procedure reconstructs and audits the inherited bodies and certificates; its expected final marker is `BH26_EXACT_FRONTIER_AND_HAUSDORFF_REPLAY_PASS 10 5`. That marker was reported by the parent and was not newly generated in this closeout. The complete coordinates, reconstruction programs, independent auditors, theorem verifiers, and expected receipts are embedded in the literal parent capsule. :contentReference[oaicite:8]{index=8}

## 6. Continuation point

Resume the geometric work from exact `double159_exact`, not from an assumed own110 endpoint or a mislabeled C616 body. Its remaining task is to replace the escape architecture of the U174/H173–174 basin through an exposed nonlocal interface, permitting return-path witness turnover and coupled filled-mass motion. One additional true edge is available unless another simplification pays for more. No such exposed replacement was constructed or verified in this assignment. The parent remains the last durable construction frontier.

Verified convenience copies: [parent source and archived exact audits](sandbox:/mnt/data/BH26_EXACT_FRONTIER_HANDOFF.zip), [complete parent handoff and embedded recovery capsule](sandbox:/mnt/data/BH26_RESULT.md), [normalized parent capsule](sandbox:/mnt/data/bh26/BH26_CAPSULE.b85), [parent decoder](sandbox:/mnt/data/bh26/RECOVER_BH26.py), and [transport-check source](sandbox:/mnt/data/BH26_VERIFY_PARENT_TRANSPORT.py).

**Final disposition:** no new scientific successor; inherited nine-body frontier recovered intact; no new mathematical replay claimed; nonlocal own110 construction with E≤310 remains unresolved by this assignment.
