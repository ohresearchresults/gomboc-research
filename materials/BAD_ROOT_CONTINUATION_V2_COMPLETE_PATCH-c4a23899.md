# material-c4a23899ff7c

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# BAD_ROOT_CONTINUATION_V2 — complete exact patch and finite inputs

## Exact source closure
Decode the complete CONTACT_CONTINUATION_V1 source dictionary from BOTH [internal-source-reference] and [internal-source-reference]. Exclude malformed abandoned part2 [internal-source-reference]. The required original BAD_ROOT_CONTINUATION.py SHA256 is1de090b1361adb0b2d83d10aa112572b8100918d73570863f1e73e1cdde88520. All imported helpers are in the complete THREE CONDITION25 source materials [internal-source-reference],[internal-source-reference],[internal-source-reference]. Exact deletion reports and endpoints are reconstructed with [internal-source-reference] plus those same parents.

V2 corrects a numerical continuation buffer, not a geometric theorem. In V1, adding1%of the magnitude of the negative target makes the requested additional improvement about0.0003 even when the outer step has been reduced below0.000001. Consequently tiny adaptive outer steps still ask for large predictor movements. V2 instead buffers the negative target by1%of the requested incremental change, capped at1e-8 and floored at1e-13. Every other physical/polar escape and convexity guard remains unchanged. Actual stage acceptance still requires all values minus floors >−1e-12. This is a finite numerical search; no exact own110 result or obstruction follows from its residual alone.

## MAKE_BAD_ROOT_V2.py
This is the complete deterministic source patch; run beside decoded BAD_ROOT_CONTINUATION.py as `python -B -S MAKE_BAD_ROOT_V2.py`:
```python
from pathlib import Path
import hashlib
p=Path('BAD_ROOT_CONTINUATION.py');b=p.read_bytes()
assert hashlib.sha256(b).hexdigest()=='1de090b1361adb0b2d83d10aa112572b8100918d73570863f1e73e1cdde88520'
s=b.decode()
a='desired=s.floor+np.maximum(abs(s.floor)*.01,1e-13)'
c='desired=s.floor+np.maximum(abs(s.floor)*.01,1e-13)\n  desired[slot]=target+max(min(abs(target-float(s.evaluate(z0)[0][slot]))*.01,1e-8),1e-13)'
assert s.count(a)==1
s=s.replace(a,c).replace('BAD_ROOT_CONTINUATION_FINITE_DONE','BAD_ROOT_CONTINUATION_V2_FINITE_DONE')
b=s.encode();assert hashlib.sha256(b).hexdigest()=='28e4683524224c22c4bb87e19f6a871e5595096368b494b453482d27cb910ec5'
Path('BAD_ROOT_CONTINUATION_V2.py').write_bytes(b)
print('BAD_ROOT_CONTINUATION_V2_EXACT_PATCH_PASS')
```

## Actual finite campaigns
CPython3.13.5,NumPy2.3.5,SciPy1.17.0; OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1, also enforced by the source. Start from the exact original CONDITION25 support deletion, not a rounded V1 intermediate. After reconstructing the exact reports into del99_exact/A.json and del117_exact/A.json and the original24source files into source/:
`python -u BAD_ROOT_CONTINUATION_V2.py --source source --report del99_exact/A.json --delete 99 --out badv2_99 --stages 45 --inner 60`
`python -u BAD_ROOT_CONTINUATION_V2.py --source source --report del117_exact/A.json --delete 117 --out badv2_117 --stages 45 --inner 60`
All other defaults are explicitly preserved by the source: fraction0.05,gamma1e-8,trust0.1,qbound0.01,grid1e12,ties-to-even np.rint. Stage success multiplies requested step by1.3,capped at25%of the initial defect; failure halves it. Outer stop if step<1e-8, or the positive gamma target is accepted, or45attempted stages.

Expected terminal marker BAD_ROOT_CONTINUATION_V2_FINITE_DONE. Full STAGES.json includes actual nonlinear line searches and rejected proposals; INPUT_GENERATOR.json,CONFIG.json preserve the exact initial rational construction and parameters. ACCEPTED, LAST_TRIAL and FINAL generator/z-hex/measure files distinguish feasible accepted checkpoints from unsuccessful trial states. Any new body still requires source-frozen input, independent exact A/B incidence and equilibrium audits, and filled-centered integration before promotion. Successful source patching is not successful geometry.
