# material-f084966c6444

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# BQ13_D100_COMPLETE33 — Recovery capsule part 4/4

Same exact object and ordering as part1 [internal-source-reference], part2 [internal-source-reference], part3 [internal-source-reference]. All four parts REQUIRED. This part contains base64 interval [50400,67736), stripped bytes17336, SHA256 d1c5b93562c2b758d008a14f9acfc6c8ea21a94504d66e8276a9b5e921d46137.

## Complete recovery and verification
Save the four literal base64 blocks in order as BQ13_D100_RECOVERY.b64, allowing whitespace. Save this complete decoder as RESTORE.py. It checks the exact input identities, reconstructs all33 source files without the originating sandbox, and invokes the source-only audit. Output directory must initially be absent.

```python
from pathlib import Path
import base64, hashlib, json, lzma, subprocess, sys
assert __debug__
def sha(b):
    return hashlib.sha256(b).hexdigest()
s = ''.join(Path(sys.argv[1]).read_text(encoding='ascii').split()).encode('ascii')
assert len(s) == 67736
assert sha(s) == 'bf0c31614bb0e90a3a309da3a1b4fb438d9ce9e270e549c465e34ae75a5f2567'
z = base64.b64decode(s, validate=True)
assert len(z) == 50800
assert sha(z) == '2dc01c8b11ed962b4720cb002c3006f7b4bb0730c8d350064da5dc8d0f5ede19'
b = lzma.decompress(z)
assert len(b) == 195516
assert sha(b) == 'b35a8a61b019e3d82770fed481a460b1b7a7840de1416aee246153b5732f54e4'
files = json.loads(b)
assert len(files) == 33
out = Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=False)
for name, text in files.items():
    p = Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    q = out / p
    q.parent.mkdir(parents=True, exist_ok=True)
    q.write_bytes(text.encode('utf8'))
subprocess.run([sys.executable, '-B', '-S', str(out / 'COLD_REPLAY.py')], check=True)
```

Command: `python -B -S RESTORE.py BQ13_D100_RECOVERY.b64 bq13-cold`.
Expected terminal markers:
```
EXACT_BARS_REFERENCE_U1_AND_INTERFACE_CERTIFICATES_PASS
BQ13_D100_SOURCE_ONLY_7_EXACT_NONWINNERS_AB_MASS_AND_CERTIFICATES_PASS
NO_OWN110_SUCCESSOR_CLAIMED
```
Original replay CPython3.13.5 standard library, assertions enabled. Numerical production NumPy2.3.5, SciPy1.17.0, PyTorch2.10.0+cpu float64, Torch threads1, OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1. Exact recovery does not rerun or depend on floating trajectories. README.md and EXPERIMENTS.json include every production command and non-default setting, FLOATS.json includes selected full IEEE-hex states. MANIFEST.json identifies allsource files; EXPECTED_NEW.json gives every new exact INPUT/H/A/B/MASS/SUMMARY filename, bytecount and SHA256; parent/EXPECTED.json gives parent output signatures. All are literal bytes inside this capsule, not missing external references.

Seven new nonwinners: exact_half5000 and exact_vol717 each V30/E84/F56 C168 own121; exact_sup5000 V98/E147/F51 C294 own121; exact_bridge V42/E120/F80 C240 own4/11/13; exact_bridge_cap V142/E213/F73 C426 own323; exact_release0 V84/E126/F44 C252 own345; exact_release_tilt V104/E156/F54 C312 own244. All weak000. Parent control V32/E90/F60 C180 own121. The exact_vol717 object is BQ13_D100_VOLUME_RECONSTRUCTION_D717, not the earlier unrounded C168 body.

Coordinator cold recovery from the hash-matching Library b64 was executed before preservation and reproduced the seven exact inputs/audits and certificates. That replay establishes source recovery, not an own110 improvement. CERTIFICATES.json output6536bytes SHA256 bb1c7f6b6320af0d4668af75dd9e5399bef3d18568aba9138c5da8a4d1aa8cca. Source capsules and the accepted parent result remain authoritative; accepted record C622 unchanged.


[Encoded source block omitted; the code in this passage is incomplete.]
