# material-068a3c55fa00

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# C426 replay: correction of descriptive numerical metadata

This corrects the empirical introduction to [internal-source-reference] and the C426 sections appended to common/branch memory. It does NOT modify the exact object, its capsule, or the complete runnable source units. Canonical own110 remainsC622. The two preserved C426 bodies remain exact nonwinners strict(1,31,30)/weak000.

## Exact source-only replay actually observed
Inputs: RECOVER_C508.py from [internal-source-reference], 14236bytes SHA25612c3e1fa064498a760c0c7eb5ef0d79d00276584b0053dab531b7c6cc5cb3838; RECOVER_FULL92_C426.py from [internal-source-reference], 6343bytes SHA2567dc0d7532809f333279827d3e09fed573c48c8e739d448cf9b5f937fa6824249. Command: OPENBLAS_NUM_THREADS=1 python RECOVER_FULL92_C426.py. Python3.13.5/NumPy2.3.5/SciPy1.17.0.
Both checkpoint and exact geometry files reproduced their capsule byte counts and SHA256 assertions, then full strict/weak census and separate three-axis projected volume/first-moment equality passed. Observed markers FULL92_C426_EXACT_NONWINNER_PASS FULL92_CYCLE6_G12 and FULL92_C426_EXACT_NONWINNER_PASS FULL92_CYCLE6_G6, then FULL92_C426_RECOVERY_COMPLETE. Exact body identity never depended on the erroneous descriptive floats below.

For both G12 and G6: V142,E213,F73,C426; strict[1,31,30],weak[0,0,0],zero real-edge primitives[0,0],stableinput[0]. Rooted polar maximum shortest depth is58, active inputs90 and91 attaining it, NOT49.
G12 volume_float=0.7920770593158468; actual centroid_float=[1.1225397524078577e-14,5.0572165298632435e-14,8.573881598132517e-14].
G6 volume_float=0.7920770286145373; actual centroid_float=[-3.4367417628884386e-08,3.360000004208299e-08,8.481331230109272e-08].
The earlier descriptive volumes0.7375283078/0.7375282567 and corresponding centroids were wrong. Discard them.
G12 checkpoint4094bytes SHA5aa97e57704f677ccbb94948894789582c2fba1d75221e7f51ac5330c89cb144; complete geometry75354bytes SHA0dcecd3a1d9dbe63109b138bf088975fc1b1e964cdbba54a86cda5b69311606c.
G6 checkpoint2431bytes SHA742851ad5f55a1b86c509e5273b3467188ffcb5c61a867bc3993ada58e4f3462; complete geometry37224bytes SHAca5cb5d4fca0f777e1a6ed06f2d53da882e7cf51f87fcab0e05c9de9075abda5.
The report's internal geometry_sha256 field hashes a different serialization; it is NOT the byte identity of the complete geometry file just specified.

## Actual finite numerical campaign receipts
All six full-active stages used bound0.2,eps1e-6,free volume,ftol1e-11,objective=sum,steps_requested1000. The source chain is exactly the six commands already provided in the immutable method material: initial FULL92_B02 has sourceNone; later CYCLE2 through6 read the preceding BEST.json. There is no required FULL92_1000 precursor. All six terminated with success=True and message Optimization terminated successfully. Their observed values are numerical search diagnostics, not independent exact certificates.

stage,evaluations,best normalized sum,C,S,U
FULL92_B02,267,0.3101460547510697,438,1,25
FULL92_CYCLE2,170,0.2387027751416521,420,1,24
FULL92_CYCLE3,319,0.19892562043902298,426,1,27
FULL92_CYCLE4,595,0.18136995245459414,426,1,29
FULL92_CYCLE5,334,0.17513410278539754,426,1,30
FULL92_CYCLE6,395,0.17199972402557598,426,1,31

The full-active numerical starting Model evaluates C508 with volume0.8204642690266892, value0.5801419188846952. This replaces the claimed starting0.561418. The final claimed0.174749014262139 was also wrong. The exact rounded final G12 capsule, passed through the same numerical geometry routine in a fresh process, gives normalized sum0.17199972402567162, volume0.7920770593158468. These are the numbers for THIS routine; do not silently overwrite an earlier exact persistence result with a differently defined numerical diagnostic.

Fixed84/variable60 CHAIN_PERSISTENCE_700 used bound1,eps5e-6,fixedvolumeTrue,steps_requested700; successTrue,247iterations286evaluations. Its best numerical C514,S1,U10 has value0.5107895030842462,volume0.8204642690261551.
CHAIN_FREEVOL_700 used the same parameters except fix_volumeFalse; successTrue,231iterations300evaluations. Its best numerical C532,S1,U13 has value0.5018706496311607,volume0.8589842781772647,minedge3.714018213403935e-7. The earlier claimed free-volume C514/S1/U8 was wrong. These fixed84 scouts were not promoted as exact new bodies.

## Recomputed short-chain seed geometry from the preserved G12 body
The dominant numerical physical persistence bar has peak101 at actual centered u=[0.08559123913198753,0.35171570792632406,0.6713521487458668], squared radius0.5817435070439568; death edge[86,87],deathheight0.4663806289501552,bar0.11536287809380164,45vertices in dying basin. The root normal remains[2.449607543282,-0.187079479902,-0.282636560527], norm2.472945465078236. Its angle to u is1.5951245105437042 radians. Earlier u=(-.34462154,-.02196149,.83381824),angle2.07346455,bar0.115659445872020 and associated deathheight/radius estimates were wrong; do not use them to seed a cut.
For q=alpha*u/(u.u), the equal-angle/equal-log-radius chain is root-escaping when norm(q)/norm(root)<cos(phi/N)^N. This is only a geometric candidate generator before true mass closure, not an accepted descendant.

## Complete fresh numeric diagnostic script
Save as REPLAY_C426_NUMERIC.py beside the two recovery sources and chain_persistence.py/full_active_persistence.py extracted completely from [internal-source-reference]. First run the exact reconstruction above, then run this script. It deliberately does NOT import RECOVER_FULL92_C426 into the model process, because that reconstruction module monkeypatches the auditor's original_planes to use a wholly new H-list.

```python
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import json
from pathlib import Path
import numpy as np
from full_active_persistence import FullActive
cp=json.loads(Path('FULL92_CYCLE6_G12.json').read_text())
N=np.array(cp['new_normals'],float)/cp['grid']
Path('CAPSULE92_NORMALS.json').write_text(json.dumps({'normals':N.tolist()}))
m=FullActive(source='CAPSULE92_NORMALS.json')
a=m.initial
b=max(a['bars'],key=lambda b:b['delta'])
u=a['points'][b['peak']]-a['centroid']
root=N[0]
phi=float(np.arccos(root@u/np.linalg.norm(root)/np.linalg.norm(u)))
print('FRESH_C426',{k:v for k,v in m.summary(m.start.ravel()).items() if k!='bars'})
print('DOMINANT',{'peak':b['peak'],'u':u.tolist(),'r2':float(u@u),
    'bar':b['delta'],'deathheight':float(u@u)-b['delta'],'edge':b['edge'],
    'basinvertices':len(b['basin']),'rootnorm':float(np.linalg.norm(root)),'phi':phi})
assert a['C']==426 and a['S']==1 and a['U']==31
print('C426_NUMERIC_REPLAY_PASS')
```
