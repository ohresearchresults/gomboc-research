# material-edc129c7ed2d

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J85 detached-B exact coordinates and closed source recovery

Both previously executed lower-depth endpoints have now been recovered after the actual working-container reset, with their original input, exact report, and S1 cube hashes all reproduced. This supersedes the pending-coordinate status for detached-B in [internal-source-reference]. The literal G12 checkpoint below also reproduces the exact G10 input by rational ties-to-even rounding; this was executed and hash-matched, not assumed from proximity. Future exact reconstruction needs no optimizer or originating sandbox.

J85_DETACHED_CONTINUED_B_G10 and G12 are two distinct homogeneous polyhedra, both V46/E132/F88,C264, OWN strict(S,U,H)=(1,2,1), additionalweak000, one positive P and no Q. G10 P=.44777264877820677; G12 P=.447772648799477. Stable triangle{0,30,45} excludes the remaining unwanted U40; U0/40 and saddle21--30 persist in the exact material ordering. This is not110. The sufficient unchanged-surface S1 infinity-cube radii are2.7541408663612723e-8 and2.7516604826672314e-8, smaller than the parent certificates. A smaller remaining bar is not unconditional progress in robustness and does not certify basin cancellation. Primitivezero000 is not claimed.

Numerical producing path is completely preserved in [internal-source-reference]:12 accepted dynamic_stellar85.py steps from the lambda3/4 single-stellar exact input, then14 actual accepted steps of the originally20-step requested warm continuation. The latter original process timed out after step13. The14-step re-execution reproduced the endpoint exactly. The wrapper retains original stored PD/QD targets on warm restart. The separately preserved two double-stellar bodies do NOT derive from this B endpoint; they derive from the earlier lambda1/2 single-stellar body and have P near.45529622.

## Exact recovery
Extract this JSON and replay_detached85.py with their final LF. Required complete source dependencies: exact84.py from [internal-source-reference]; freeze85.py from [internal-source-reference]; freeze_dynamic85.py from [internal-source-reference]. Run CPython3.13.5 standard library: python replay_detached85.py. No numerical package is used by this replay. It rebuilds exact supporting facets/edges, closed oriented topology, positive-tetrahedron own mass, full S/U/H and weak census, all positive bars and sufficient S1 centre-cube policies. This is source recovery and replay through the same exact implementation, not a second independent verification engine.
Observed terminal: J85_DETACHED_B_TWO_LITERAL_BODIES_REPLAY_PASS_NO_110.
replay_detached85.py1766B/SHA66e295c543b9733d5ec6b8980fb7a635c14230e6c4b8b7ee357cc4df90876a19.

Expected inputs and outputs:
J85_DETACHED_CONTINUED_B_G10_INPUT.json1751B/b64ac54422ce18d54117685545d2f306ab29f15dc7473664941b71d2814f54c8
J85_DETACHED_CONTINUED_B_G12_INPUT.json2029B/ecb57f2d9acd94f1bf4fb0af01ba40f6596d13f081823ffb7c23332de4a36232
J85_DETACHED_CONTINUED_B_G10_EXACT.json5966B/9e40d19b4f96431bc15b31a13269bb9e434eb0537e03fa26de8b67534c5df3c0
J85_DETACHED_CONTINUED_B_G10_CUBE.json129346B/ad5a6e4e3b0e8e0ff3c587cab18e6dd67d771da31504dc6a2f6d93ccf132ed82
J85_DETACHED_CONTINUED_B_G12_EXACT.json6727B/b2164541ccc34d5ea6975236223cb993427a9a890f5f868a3b9baff6de8342b3
J85_DETACHED_CONTINUED_B_G12_CUBE.json153987B/0882a7fc3ecda6a5a8b5c6cb46c60771bdc0eb4a703897a67bed3441a129c1f9

## J85_DETACHED_CONTINUED_B_G12_INPUT.json
```json
{"denominator":1000000000000,"name":"J85_DETACHED_CONTINUED_B_G12","points":[[-1772498000000,-1222476000000,446600000000],[-1114825171136,-362420582659,-764275268089],[-937414935610,-156439584150,111940971245],[-846929305303,7740273984,14941002879],[-827890937311,83664468718,-250667225448],[-805795051794,-244662404527,-983672712828],[-820809682771,85832360429,-358695711345],[-639048578765,-214787724522,-1057463051979],[-650844699246,237894226905,-171817604448],[-564382555659,275341641101,-470586050855],[-482887523507,-215255494557,-1096774398455],[-378554338543,-215770260681,-1110307511209],[-419001264354,256992754003,130613766564],[-343103487620,493410917688,-383319919083],[-340652807914,525092186525,-232480977752],[-279220305795,-212667151931,-1111853626959],[-231775653078,453659180701,-480532135827],[-229772118541,537084742224,-69182218574],[-180419078971,-237251862777,-1102865285705],[-191793733595,-615405253595,-662910922409],[-142816954340,340178473781,-585148370424],[-86193835131,-251558313295,-1083376776587],[-82574938097,523243125660,128087643774],[-78953630474,247573112158,-658443045985],[-24501276608,476437815832,182667836486],[19323855021,198324063255,302495412790],[68203474580,456839481846,223334498145],[178282705640,438263076447,256456996311],[408032443728,380533065297,295841934395],[495796586941,315564651686,302344528048],[509745728429,-473567666872,-888930395316],[563607196452,231802330328,297389483564],[626640072826,144746592115,279173991533],[641929696619,243464264072,52692404402],[688480264179,52492339493,244872046833],[726958909250,-117953015690,-671368533347],[743495175499,-40061409701,194944075967],[790684285301,-68936168,-392670325043],[792443371725,-133565311131,126106318531],[830133766807,-219845124533,43422857763],[859256399618,-459993881792,-484748882668],[873127405777,-425951528753,-310609706728],[857763363096,-300204112216,-57414930542],[873162838925,-370993323627,-177421949467],[882679884176,-357633352181,-364656570644],[564202459618,-545890236035,-504935589578]]}
```

## replay_detached85.py
```python
"""Reconstruct both exact J85 detached-B bodies from one literal G12 checkpoint.
Dependencies: exact84.py, freeze85.py, freeze_dynamic85.py. Standard library only.
"""
import json,hashlib
from fractions import Fraction as R
from exact84 import ROOT,audit
from freeze85 import cube,dump
from freeze_dynamic85 import exact_hull
base=json.loads((ROOT/'J85_DETACHED_CONTINUED_B_G12_INPUT.json').read_text())
CASES={
 10:('b64ac54422ce18d54117685545d2f306ab29f15dc7473664941b71d2814f54c8','9e40d19b4f96431bc15b31a13269bb9e434eb0537e03fa26de8b67534c5df3c0','ad5a6e4e3b0e8e0ff3c587cab18e6dd67d771da31504dc6a2f6d93ccf132ed82'),
 12:('ecb57f2d9acd94f1bf4fb0af01ba40f6596d13f081823ffb7c23332de4a36232','b2164541ccc34d5ea6975236223cb993427a9a890f5f868a3b9baff6de8342b3','0882a7fc3ecda6a5a8b5c6cb46c60771bdc0eb4a703897a67bed3441a129c1f9')}
assert base['denominator']==10**12 and len(base['points'])==46
for k,(si,se,sc) in CASES.items():
    D=10**k;rows=[[round(R(x*D,10**12)) for x in row] for row in base['points']]
    name='J85_DETACHED_CONTINUED_B_G'+str(k);data={'denominator':D,'name':name,'points':rows}
    raw=(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n').encode()
    assert hashlib.sha256(raw).hexdigest()==si
    (ROOT/(name+'_INPUT.json')).write_bytes(raw)
    P,F,ids=exact_hull(rows,D);r=audit(P,F);r['name']=name;r['material_rows']=ids
    assert (r['V'],r['E'],r['F'])==(46,132,88) and r['strict']==[1,2,1] and r['weak']==[0,0,0]
    assert [ids[i] for i in r['U']]==[0,40] and {ids[i] for i in F[r['S'][0]]}=={0,30,45}
    assert len(r['P'])==1 and not r['Q']
    assert dump(name+'_EXACT.json',r)['sha256']==se
    assert dump(name+'_CUBE.json',cube(P,F))['sha256']==sc
print('J85_DETACHED_B_TWO_LITERAL_BODIES_REPLAY_PASS_NO_110',flush=True)
```
