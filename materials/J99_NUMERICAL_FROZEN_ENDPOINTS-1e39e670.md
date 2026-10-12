# material-1e39e6704fbe

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J99 complete frozen numerical failure endpoints and replay

Dependencies: exact old R82 input in material [internal-source-reference], and complete geom99.py/joint99.py in [internal-source-reference]. No originating sandbox is required. These are three completed numerical experiments and TWO distinct geometric endpoints: case2 and case6 have identical coordinates, with different inactive elder-ceiling settings. None is an exact own110 nomination or a family exclusion. Case1 ended without a frozen endpoint and is described, not fabricated, in the methods material.

Each body is the convex hull of all160 original R82 vertices and ALL displayed new points. new_points_raw are in the original R82 chart. new_points_centered are in the chart translated by the original numerically integrated centroid. The own.g and reference.g fields BOTH record the actual filled-hull centroid in that old-centred chart; reference equilibrium counts were evaluated at chart zero, while own equilibrium counts used that actual mass. Thus reference.g is not a claim that the reference evaluation centre equals the actual centroid. Raw coordinates are provided as well to make the physical construction unambiguous.

All decimal literals round-trip their frozen float64 inputs. The numerical routine uses plane grouping2e-9, root threshold1e-10 and P/Q nomination floor1e-13. The replay regenerates all numerically retained bars and does not certify exact signs or small omitted tails. Exact rational acceptance is separate and was not run on these failed over-budget bodies. The displacement reduction to.00831644 did not eliminate cover holes or excess own equilibria.

## Recovery and replay
Save each FILE fence unchanged, ending with one newline, beside the dependencies. Execute:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python nominate_frozen99.py
```

Observed markers:
`J99_FROZEN_NUMERICAL_NOMINATION_REPLAY_NOT_EXACT 0 139 250 113 18 28 6`
`J99_FROZEN_NUMERICAL_NOMINATION_REPLAY_NOT_EXACT 2 134 300 168 8 36 5`
`J99_FROZEN_NUMERICAL_NOMINATION_REPLAY_NOT_EXACT 6 134 300 168 8 36 5`.
They encode case,V,E,F,ownS,ownU,remaining numerical component holes. The actual frozen-input replay was executed successfully in the same CPython3.13.5/NumPy2.3.5/SciPy1.17.0 environment. It is not an independent exact audit.

Input identities: J99_JOINT_0_FROZEN.json1982B SHA9d54a6296d07bc5770920435d44dcadd337a95f6e6a289702fb6d4787cb80371; J99_JOINT_2_FROZEN.json2500B SHAa6916136f423f085196d700431320fd7471b7e76f62e977828fa7bdd4c311a30; J99_JOINT_6_FROZEN.json2497B SHA9892b98abe41d4dd90b6825d94c5c7ece5e4a36222295a70b15c01def4b3c1f8. nominate_frozen99.py1577B SHA0769f210227f144bc328ae2c06a5018ac0d59ce2fa4bfa158bad2dbff60b556f. Regenerated J99_FROZEN_DIAGNOSTICS.json38929B SHA62d3ce833620c1e3ae88a7c0f1d904b21ddde33b3adab553b84a927ee5d37ee4 includes full numerical own/reference P/Q lists. Floating output hash portability is not assumed; exact recovery inputs remain literal.

## FILE J99_JOINT_0_FROZEN.json
```json
{"calls":111,"centroid_norm":0.019161958011424833,"evidence":"NUMERICAL_NOMINATION_ONLY_NO_EXACT_CENSUS","identity":"J99_JOINT_COVER_0","minimum_old_witness":9.99999998052748e-09,"new_points_centered":[[-0.3658847632467498,0.41624365497670646,0.4079688032649771],[0.00961445891461495,0.246846015548774,0.7102946504714409],[-0.3063079986077734,0.537595463240373,0.14384561391985762],[-0.49809534398085287,0.4741370181387343,-0.09681426680134936]],"new_points_raw":[[-0.3409218204961407,0.4194600019842249,0.4011860651428002],[0.034577401665223995,0.25006236255629244,0.703511912349264],[-0.28134505585716435,0.5408118102478915,0.1370628757976807],[-0.4731324012302438,0.47735336514614625276,-0.10359700492352628]],"numerical_component_holes":6,"old_witness_indices":[15,20,148,6],"own":{"E":250,"F":113,"S":[0,2,5,15,28,29,32,44,73,79,80,83,87,93,96,97,98,105],"U":[1,5,6,7,15,25,26,27,28,29,30,31,32,33,34,35,37,38,45,46,47,78,79,80,82,84,105,148],"V":139,"g":[-0.010215858619712404,0.008200979562718855,0.013984305549633983],"volume":1.7784217233949509},"reference":{"E":250,"F":113,"S":[0,2,5,15,28,29,32,44,96],"U":[15],"V":139,"g":[-0.010215858619712404,0.008200979562718855,0.013984305549633983],"volume":1.7784217233949509},"settings":{"ball_margin":1e-08,"elder_ceiling":0.6339,"level":0.63391,"maxiter":120,"ncontrol":0,"outer_limit":3,"sphere_samples":16000},"trace":[{"calls":70,"centroid_norm":0.018945129660529438,"constraint_min":-5.4567461660326444e-14,"holes":10,"iterations":63,"message":"Optimization terminated successfully","outer":0,"status":0,"success":true},{"calls":15,"centroid_norm":0.019474346773607754,"constraint_min":-7.566169912820442e-14,"holes":7,"iterations":15,"message":"Optimization terminated successfully","outer":1,"status":0,"success":true},{"calls":26,"centroid_norm":0.019161958011424833,"constraint_min":-2.7755575615628914e-17,"holes":6,"iterations":25,"message":"Optimization terminated successfully","outer":2,"status":0,"success":true}]}
```

## FILE J99_JOINT_2_FROZEN.json
```json
{"calls":356,"centroid_norm":0.00831644384301899,"evidence":"NUMERICAL_NOMINATION_ONLY_NO_EXACT_CENSUS","identity":"J99_JOINT_COVER_2","minimum_old_witness":9.999984225572181e-09,"new_points_centered":[[-0.3139381836024436,0.4038128211422286,0.6311343566958805],[0.27859177777577016,-0.22793725865769174,0.6924251530304015],[-0.3300700305232476,0.5455475851008326,0.07435909433304873],[-0.47806678443028383,0.4763827818832096,-0.11324306136187418],[0.5488643807222467,-0.5794341287402288,-0.3355022092505904],[0.010294789864676131,0.31142205238776677,-0.8319639235248029],[0.3704155592466507,0.13722046250721892,-0.8221193093582666],[0.8418118210891311,-0.07920141696350871,-0.37677528868829374]],"new_points_raw":[[-0.2889752408518345,0.40702916814974704,0.6243516185737036],[0.3035547205263792,-0.2247209116501733,0.6856424149082246],[-0.30510708777263856,0.5487639321083511,0.06757635621087181],[-0.45310384167967477,0.47959912889072803,-0.1200257994840511],[0.5738273234728558,-0.5762177817327103,-0.34228494737276727],[0.03525773261528518,0.3146383993952852,-0.8387466616469798],[0.39537850199725977,0.14043680951473736,-0.8289020474804435],[0.8667747638397402,-0.07598506995599028,-0.38355802681047063]],"numerical_component_holes":5,"old_witness_indices":[15,20,148,6,87,29,45,101],"own":{"E":300,"F":168,"S":[5,9,31,55,56,76,109,113],"U":[1,5,6,7,15,25,26,27,28,29,30,31,32,33,34,35,37,38,45,46,47,78,79,80,82,83,84,103,106,107,109,120,121,165,166,167],"V":134,"g":[-0.007513284284649151,0.00017028432637013975,0.003561572784645181],"volume":1.929112810851431},"reference":{"E":300,"F":168,"S":[5,9,31,55,56,76,107,113],"U":[15],"V":134,"g":[-0.007513284284649151,0.00017028432637013975,0.003561572784645181],"volume":1.929112810851431},"settings":{"ball_margin":1e-08,"elder_ceiling":0.6339,"level":0.63391,"maxiter":250,"ncontrol":4,"outer_limit":3,"sphere_samples":16000},"trace":[{"calls":175,"centroid_norm":0.007693972323745833,"constraint_min":-1.740274591099933e-14,"holes":6,"iterations":174,"message":"Optimization terminated successfully","outer":0,"status":0,"success":true},{"calls":90,"centroid_norm":0.008358432773938733,"constraint_min":-4.0245584642661925e-15,"holes":5,"iterations":89,"message":"Optimization terminated successfully","outer":1,"status":0,"success":true},{"calls":91,"centroid_norm":0.00831644384301899,"constraint_min":-1.5792922525292852e-14,"holes":5,"iterations":90,"message":"Optimization terminated successfully","outer":2,"status":0,"success":true}]}
```

## FILE J99_JOINT_6_FROZEN.json
```json
{"calls":356,"centroid_norm":0.00831644384301899,"evidence":"NUMERICAL_NOMINATION_ONLY_NO_EXACT_CENSUS","identity":"J99_JOINT_COVER_6","minimum_old_witness":9.999984225572181e-09,"new_points_centered":[[-0.3139381836024436,0.4038128211422286,0.6311343566958805],[0.27859177777577016,-0.22793725865769174,0.6924251530304015],[-0.3300700305232476,0.5455475851008326,0.07435909433304873],[-0.47806678443028383,0.4763827818832096,-0.11324306136187418],[0.5488643807222467,-0.5794341287402288,-0.3355022092505904],[0.010294789864676131,0.31142205238776677,-0.8319639235248029],[0.3704155592466507,0.13722046250721892,-0.8221193093582666],[0.8418118210891311,-0.07920141696350871,-0.37677528868829374]],"new_points_raw":[[-0.2889752408518345,0.40702916814974704,0.6243516185737036],[0.3035547205263792,-0.2247209116501733,0.6856424149082246],[-0.30510708777263856,0.5487639321083511,0.06757635621087181],[-0.45310384167967477,0.47959912889072803,-0.1200257994840511],[0.5738273234728558,-0.5762177817327103,-0.34228494737276727],[0.03525773261528518,0.3146383993952852,-0.8387466616469798],[0.39537850199725977,0.14043680951473736,-0.8289020474804435],[0.8667747638397402,-0.07598506995599028,-0.38355802681047063]],"numerical_component_holes":5,"old_witness_indices":[15,20,148,6,87,29,45,101],"own":{"E":300,"F":168,"S":[5,9,31,55,56,76,109,113],"U":[1,5,6,7,15,25,26,27,28,29,30,31,32,33,34,35,37,38,45,46,47,78,79,80,82,83,84,103,106,107,109,120,121,165,166,167],"V":134,"g":[-0.007513284284649151,0.00017028432637013975,0.003561572784645181],"volume":1.929112810851431},"reference":{"E":300,"F":168,"S":[5,9,31,55,56,76,107,113],"U":[15],"V":134,"g":[-0.007513284284649151,0.00017028432637013975,0.003561572784645181],"volume":1.929112810851431},"settings":{"ball_margin":1e-08,"elder_ceiling":0.8,"level":0.63391,"maxiter":250,"ncontrol":4,"outer_limit":3,"sphere_samples":16000},"trace":[{"calls":175,"centroid_norm":0.007693972323745833,"constraint_min":-1.740274591099933e-14,"holes":6,"iterations":174,"message":"Optimization terminated successfully","outer":0,"status":0,"success":true},{"calls":90,"centroid_norm":0.008358432773938733,"constraint_min":-4.0245584642661925e-15,"holes":5,"iterations":89,"message":"Optimization terminated successfully","outer":1,"status":0,"success":true},{"calls":91,"centroid_norm":0.00831644384301899,"constraint_min":-1.5792922525292852e-14,"holes":5,"iterations":90,"message":"Optimization terminated successfully","outer":2,"status":0,"success":true}]}
```

## FILE nominate_frozen99.py
```python
"""Replay complete frozen numerical nominations; this is not an exact certificate."""
from pathlib import Path
import hashlib,json
import numpy as np
from geom99 import load,hull,summary
from joint99 import holes
root=Path(__file__).parent;base=load();records=[]
expected={0:'9d54a6296d07bc5770920435d44dcadd337a95f6e6a289702fb6d4787cb80371',
          2:'a6916136f423f085196d700431320fd7471b7e76f62e977828fa7bdd4c311a30',
          6:'9892b98abe41d4dd90b6825d94c5c7ece5e4a36222295a70b15c01def4b3c1f8'}
for case,sha in expected.items():
    raw=(root/f'J99_JOINT_{case}_FROZEN.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()==sha
    f=json.loads(raw);A=np.array(f['new_points_centered']);b,ii,_=holes(base,A)
    own=summary(b);reference=summary(b,np.zeros(3))
    for name,r in [('own',own),('reference',reference)]:
        old=f[name]
        assert [r[k] for k in ['V','E','F']]==[old[k] for k in ['V','E','F']]
        assert len(r['S'])==len(old['S']) and len(r['U'])==len(old['U'])
        assert np.max(abs(np.array(r['g'])-old['g']))<1e-12
        assert abs(r['volume']-old['volume'])<1e-12
    assert len(ii)==f['numerical_component_holes']
    records.append(dict(identity=f['identity'],own=own,reference=reference,holes=len(ii)))
    print('J99_FROZEN_NUMERICAL_NOMINATION_REPLAY_NOT_EXACT',case,own['V'],own['E'],own['F'],len(own['S']),len(own['U']),len(ii))
text=json.dumps(records,indent=2)+'\n';dest=root/'J99_FROZEN_DIAGNOSTICS.json';dest.write_text(text)
print('OUTPUT',dest.name,len(text.encode()),hashlib.sha256(text.encode()).hexdigest())
```
