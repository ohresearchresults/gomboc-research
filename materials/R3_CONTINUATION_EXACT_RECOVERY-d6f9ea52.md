# material-d6f9ea52c4d7

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# R3_CONTINUATION: exact recovery and method provenance
R3_BEST is a non-target homogeneous convex rational body V58/E168/F112,C336, own211, no additional weak equilibria, no primitive zeros. Complete exact P landscape has zero positive bars; Q has one positive bar of normalized depth 0.3682015269855614. R3_G8 and R3_G7 preserve own211/weak000/zero000/P0Q1, depths .3682015230877156 and .3682015858035583. R3_G6 is a meaningful coarse-grid failure: own12/20/30,weak000,zero000,P19Q11,seniorQdepth .3682013015397365; tiny positive bars are real, not tolerance-zero. None meets110. Canonical accepted own110/C622 is unchanged.

## Exact dependencies
Endpoint recovery needs only literal R3_BEST below and recover_r3.py below. For full geometry/mass/equilibria/bar reconstruction use exact_poly.py6134B SHA898f77989193886996d6f2dc121ccdfdf611b8a9ac52fd3207557eac6a69c0c4 in immutable material [internal-source-reference] (JB_C168_OWN211_EXACT_RECOVERY_V1.md13684B SHA2b1c5045a6bac634a6858e76e723cf3820fe4185a0ef3253bb1a845d696b84e2). The complete stdlib auditor enumerates exact supporting triples, rejects nontriangular maximalfacets, computes filledvolume/moments and actual COM, strict and closedweak S/U/H, primitivezeros and complete rational P/Q forests. One exact hull engine, not an independently doubled engine. All four controls truly simplicial.
Producing method is the complete source escape_core_v2.py4657B SHA1e363702f3e1bb4310426ca40f02d1ad705c9ba9314e9690358ce6d20bd55f4b and escape_retract_v2.py5256B SHA106228465cf7665ed066ebff8f17e85c59f8db616c320edfac05cb6fb5afdc32 in [internal-source-reference] (R2_RECOVERY_PART2_OF2_COMPLETE_METHOD.md14041B SHAc929e095798756965803ca9abac292ae3ee1bed0691092e087680f5ac99a0aba). Complete exact input R2_BEST.json2179B SHA119fa76fbc2ee00387cba4d488be9a5876484e64f78f734448674ac59a327bb4 is in [internal-source-reference] (R2_RECOVERY_PART1_OF2_EXACT_CONTROLS.md5993B SHAca3ccf961d925f03a8bd39769587eb3967434dd8dd501a9b8d888a1ef1664a97). R3 does not require reconstructing the earlier SQP1 optimizer input: its full literal R2 input is available.

## Production and exact verification
Observed environment CPython3.13.5,numpy2.3.5,scipy1.17.0,torch2.10.0+cpu CPUfloat64,torchthreads1. No RNG. Numerical command:
```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python escape_retract_v2.py R2_BEST.json R3 --steps 300 --record 20
```
All other parameters explicitly: radius.002,maxradius.01,minradius1e-9,margin1e-7,feasible2e-9,corrections8,repair_radius.005,drive1,digits10,improve1e-11. This source reselects live hull/COM/witnesses after every trial and nonlinear correction. Float forest depths≤1e-14 are diagnostic only; exact audit never discards exact positive bars. 301 trace states,300 acceptedsteps; RETRACT_FINISHED 301 300 0.3682015269436045. Depths at iterations0/100/200/300 were .3860491795645385/.3718693288295628/.3692872962124038/.3682015269436045. All recorded states remainedS2U1/P0Q1/E168. Radius reached.01 at20 and remainedthere. Diminishing descent is an observation, not a proof of a local minimum or impossibility. There is no claim that a floating optimizer replays byte-identically across dependency versions. The preserved rational endpoint is independent of such replay.
R3_TRACE.json observed156129B SHAe9d40728fa0b7e01b3afdd46d3c0a092c1b09369504be604780745ffddbe02c6;R3_RUN.log2519B SHA93099b1dacf49cd92ae2f0f47c29a7fea9ed22e8a6ca3a230cce19958182ecce. These trace receipts are not substitutes for data: complete producing source,input,parameters and exact terminal coordinates are preserved above/below; full transient trace is not an endpoint dependency.

Write both following blocks verbatim with final LF. R3_BEST.json2177B SHA43d6adb06bc3a027dac4257de57455692b3fb964e1ef4e872c6e16d32d965a2b;recover_r3.py1908B SHA7eb6a2bced8ef6295637b79ae2880a0af36944d22ee38ac5fa7a7e77e01f173f. Commands:
```
python -B -S recover_r3.py
python -B -S exact_poly.py R3_BEST.json
python -B -S exact_poly.py R3_G8.json
python -B -S exact_poly.py R3_G7.json
python -B -S exact_poly.py R3_G6.json
python -B -S recover_r3.py --audits
```
Observed four EXACT_POLY_AUDIT_PASS lines with classes above, four R3_AUDIT_RECEIPT_PASS and R3_RECOVERY_PASS. Complete reproducible audit file byte/hash checks are in recover_r3.py. Geometry indices refer to the auditor's sorted exact vertices and sorted oriented facets, not input row order or previous R2 labels. Fine R3 S=[52,105],U=[57],H=[[38,57]]. Qjunior105,elder52,component33/cut21,attainingedge[89,90],attainingpath[105,107,108,109,106,110,101,103,104,102,94,96,97,95,87,89,90,88,98,75,76,72,83,82,81,52]. Complete component/cut/mass/birth/death fractions regenerate in audit.

## R3_BEST.json
```json
{"denominator":10000000000,"name":"R3_BEST","points":[[-9986162735,-668926505,1078173628],[-9754484205,-594155033,3142712316],[-9832200805,-658773005,-934650426],[-9822830943,-1743754645,1752197048],[-9366786675,-148081766,-2733405915],[-9312935043,290396516,4678262463],[-9587692793,-2865631587,401023285],[-9271032131,-816944371,-2898530289],[-8544918874,1096951252,6200315836],[-8782366843,1008535552,-3865878756],[-9083627217,-3876655459,-926919480],[-8268533166,953808257,-4846317833],[-8547772429,-3762270191,-2872490252],[-8299645096,-867419467,-4760979506],[-7438004919,1706736318,7687585673],[-8313856781,-4785743239,-2190207381],[-7047233814,-557877137,-6332447120],[-7546995723,-5071550603,-3588796010],[-6157588305,1994248238,-6695241457],[-6126946722,-6872778809,-2440085021],[-6087992743,2318945829,8937555527],[-6575240850,-5261716603,-4858861015],[-6097343317,-6375412372,-3985317161],[-5214914294,282062086,-7702865778],[-3352862417,-8233307746,-2405070573],[-5494161493,-4910647820,-6221752125],[-4472150313,2978244041,9956981936],[-4456532481,-3822366198,-7489916360],[-4922815167,-6395886562,-5248365256],[-2734686375,1760287392,-8379597758],[-376480818,-8722448288,-1398267969],[-2854208393,-2773482458,-8492262232],[-3844256631,-5083643712,-7147311727],[-2617200318,3676644544,10680239280],[-3019943757,-7104589521,-5603283812],[-1925689612,-5006739091,-7829774347],[-372188837,-2070648657,-8929480749],[2040137247,-8135602487,531127799],[476528176,-4516955865,-8142340863],[-913147656,-7530434132,-5612161805],[-347425138,4415938476,11101568527],[571978577,69276097,-7973143542],[1714848719,-7313461513,-5359235878],[2246172135,5238477533,10994250413],[5643330344,559221128,-5383641006],[5767519915,-1743341414,-4623214415],[6945176038,3635324399,-4370970080],[5446363411,6145498483,10091203630],[9266065656,6944115166,7799527944],[15568415967,7455638944,472738961],[-1154747918,3594426864,-6479577124],[5189953368,815719144,5852152955],[-260605724,-36309925,7451872789],[1493912657,-1246370227,6147557723],[3082638329,-7336097607,-2050349413],[1579673877,1651956462,-7040821451],[7313556205,-1937498330,-2342400736],[8616607677,897877731,-3200534991]]}
```

## recover_r3.py
```python
"""Recover the exact rational R3 endpoint and three coarser controls."""
import json,hashlib,sys
from pathlib import Path
p=Path('R3_BEST.json');b=p.read_bytes()
assert len(b)==2177 and hashlib.sha256(b).hexdigest()=='43d6adb06bc3a027dac4257de57455692b3fb964e1ef4e872c6e16d32d965a2b'
x=json.loads(b)
checks={8:(1825,'455f29d7a353c2576c810dbc1153c7a1a471fc7bed4352c7670a57e563eceaa6'),7:(1650,'5f27af1e90ff237534cb455eb580d161329a01ef495e143133e7c3cbabd9619e'),6:(1475,'2d205e280da24430e1910cbe037cb7de37caa985e0245f63f7495cfd277e8e59')}
for k,(size,sha) in checks.items():
    def rnd(a):
        b=10**(10-k);q,r=divmod(a,b)
        return q+int(2*r>b or(2*r==b and q%2))
    z=dict(denominator=10**k,name=f'R3_G{k}',points=[[rnd(v) for v in p] for p in x['points']])
    data=(json.dumps(z,separators=(',',':'))+'\n').encode()
    assert len(data)==size and hashlib.sha256(data).hexdigest()==sha
    Path(z['name']+'.json').write_bytes(data)
    print('R3_RECOVER_INPUT_PASS',z['name'],size,sha)
if '--audits' in sys.argv:
    audits={'R3_BEST':(6631,'4ebb493fd0d11a0a2d4d166841586969e24d78c34f5a1cb1feaad0a0e9cbc3d5',[2,1,1],0,1),'R3_G8':(6055,'406e9d462407b5374870fb2d4789a544f3318aa37ee4593dcd4149b0ee4c55cf',[2,1,1],0,1),'R3_G7':(5786,'c3157fb9e986be96fb9c76e5477a81b5ca0933471f47bad3c5f3941e02dde721',[2,1,1],0,1),'R3_G6':(20547,'edfbca43b92b20f9be04c37e24a49032159e8e96e9692434058a01eab951befe',[12,20,30],19,11)}
    for name,(size,sha,cls,pn,qn) in audits.items():
        b=Path(name+'_AUDIT.json').read_bytes();assert len(b)==size and hashlib.sha256(b).hexdigest()==sha
        d=json.loads(b)
        assert [d['V'],d['E'],d['F'],d['C']]==[58,168,112,336]
        assert d['strict']==d['weak']==cls and d['additional_weak']==d['primitive_zero']==[0,0,0]
        assert len(d['P_bars'])==pn and len(d['Q_bars'])==qn
        print('R3_AUDIT_RECEIPT_PASS',name,cls,pn,qn)
print('R3_RECOVERY_PASS')
```
