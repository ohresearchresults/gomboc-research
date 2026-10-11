# material-9cb6402b53c2

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# C114 own-centroid projective-affine numerical search — Recovery capsule part 4/4

Complete ordered capsule:
1. [internal-source-reference] — search.py, exact original grid and all projective/affine/solid-centroid formulas.
2. [internal-source-reference] — basin_search.py, complete fixed-graph radial merge-bar objective.
3. [internal-source-reference] — guarded_search.py, fixed-root U=1 constrained objective.
4. This material — complete recorded endpoints and reproducible numerical replay.

No new strict110 construction was found. The canonical C622 remains unchanged. These data preserve a method and bounded numerical negative result, not an exclusion of the eight-parameter projective-affine orbit. There are seven searched endpoints and one baseline. Endpoint S/U counts are numerical; weak equilibria and exact H were not certified. Exact rational grid geometry is inherited from the own211 C114 parent figure-0438, not promoted to own110 by transformation.

Extract the following two blocks verbatim, each ending with LF, into endpoints.json and replay.py alongside the three prior source files. Run python replay.py. Environment actually used: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0. Expected terminal marker: C114_ORBIT_ENDPOINT_REPLAY_PASS 8. This replay reconstructs geometry directly from stored binary64 endpoints and checks its actual solid centroid and numerical S/U; it does not rerun the optimizer. Floating output bytes may vary on different arithmetic platforms; the following hashes identify the output reproduced in the stated environment, not a universal mathematical certificate.

File manifest:
- endpoints.json: 1454 bytes; SHA-256 10e0a3a99c5d7c67787e22ae135c1a9bf7aae67b4b5428152bee23eeb7847367.
- replay.py: 2270 bytes; SHA-256 0db2b063e8a723eee88763159fbc41b853cc4f28327f6b707dcca2828dceb2c2.
- Reproduced replay_report.json: 21694 bytes; SHA-256 d07e9eb1dfef4f0d3a0b08ba28bfbc39cddfa2cc118e8c33ce7243bc0ca80f81.

Numerical findings reproduced from these literal endpoints: baseline S2/U1 with one polar birth-relative merge bar 0.9538258320653124 and no primal bar. Hinge starts gave S/U=(4,3),(3,3),(3,3). Joint full-bar starts gave (8,10),(10,11), with largest polar bars 0.46856806639440035 and 0.5801018866450024 respectively: lower objective but many extra basins. Both U=1-guarded starts gave S3/U1; largest polar bar 0.95033772035436 and a new bar 0.002258551706. Physical positive-escape margin is approximately 1e-7 at the active constraint. Denominators remain positive: guarded minimum about 0.9277543, condition(A) about 1.11668. All replayed solid-centroid residuals are below 3e-15. These statements use the actual stored source files and endpoint records, not provisional coordinator summaries.

## endpoints.json
```json
[{"S":2,"U":1,"id":"baseline","z":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]},{"S":4,"U":3,"id":"hinge_0","z":[0.01574826972712318,0.05338467762756262,-0.0713366655378851,0.14393291429494204,-0.1032750780605592,-0.059296028368209554,-0.019055034247974785,-0.3839859801388816]},{"S":3,"U":3,"id":"hinge_1","z":[-0.2517629132723839,-0.78683300710546,-0.1913572406095378,2.4543678055047544,-2.195121537899542,-0.06734973259714438,-1.2237149227350803,-0.033739180724381646]},{"S":3,"U":3,"id":"hinge_2","z":[0.9020754883819425,0.9815322696050942,-0.014096091910715031,1.0861345841620518,-1.6580532008363358,-0.7432589058007866,0.19300249902986516,0.704765443483473]},{"S":8,"U":10,"id":"joint_0","z":[-1.5596584925698043,-0.0054428343957209765,0.5478908975836221,-0.1327774273513826,0.3477389595700433,-0.22988072561039502,0.08091632589230197,0.3026537964408382]},{"S":10,"U":11,"id":"joint_1","z":[-1.3691175067946955,-0.1375019877897935,0.059813528474746074,-0.4074579974041119,0.03898961124909747,-0.08397347930570433,-0.5168702340023431,0.8073251693599494]},{"S":3,"U":1,"id":"guarded_0","z":[0.08310111101217517,-0.08561019778979494,-0.11008644301794863,-0.033077427054012516,0.03145902848806808,-0.037126279017090646,-0.03687286205052149,0.09033117494109853]},{"S":3,"U":1,"id":"guarded_1","z":[0.08310111101411899,-0.0856101977863207,-0.1100864430115948,-0.03307742705379974,0.03145902848750861,-0.037126279014041585,-0.03687286204747593,0.0903311749408249]}]
```

## replay.py
```python
"""Replay all recorded C114 orbit endpoints; numerical checks, not certification."""
import hashlib
import json
import platform
from pathlib import Path
import search as s
import basin_search as b
import guarded_search as guard
import numpy as np
import scipy

ROOT = Path(__file__).resolve().parent
SOURCES = {
    'search.py': '0cdbb78ed4f389add5a51accbba2f451a2b809071775ef0d7668468a974bfb11',
    'basin_search.py': '1c5195a120be35da6afec777621e9f471ce1ac1dcb1da617aeda3b183c4e9335',
    'guarded_search.py': '90c42fb56cdb73ff14dc2b67ff756e3a334ce9121cbc31af4d7d79915558cd13',
}

def main():
    for name, expected in SOURCES.items():
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f'Source hash mismatch: {name}')
    assert len(s.X0) == 21 and len(s.TRI) == 38 and len(b.EP) == 57
    records = json.loads((ROOT / 'endpoints.json').read_text())
    assert len(records) == 8
    report = []
    for item in records:
        z = np.array(item['z'], dtype=np.float64)
        geo = s.geometry(z)
        assert geo is not None, item['id']
        P, Q, g, A, den, cond = geo
        residual = float(np.linalg.norm(s.mass(P)))
        scale = float(np.linalg.norm(P, axis=1).max())
        assert residual < 1e-10 * scale, item['id']
        d = b.diagnostics(z)
        assert (d['S_float'], d['U_float']) == (item['S'], item['U']), item['id']
        d['id'] = item['id']
        d['centroid_residual'] = residual
        if item['id'].startswith('guarded'):
            d['guard_constraint_min'] = float(guard.constraints(z).min())
            assert d['guard_constraint_min'] > -1e-10
        report.append(d)
    payload = {'V': 21, 'E': 57, 'F': 38, 'C': 114,
               'evidence': 'floating endpoint replay; no exact class or exclusion certificate',
               'records': report}
    output = ROOT / 'replay_report.json'
    output.write_text(json.dumps(payload, sort_keys=True, indent=2) + '\n')
    print('Environment', platform.python_version(), np.__version__, scipy.__version__)
    print('C114_ORBIT_ENDPOINT_REPLAY_PASS', len(report),
          len(output.read_bytes()), hashlib.sha256(output.read_bytes()).hexdigest())

if __name__ == '__main__':
    main()
```
