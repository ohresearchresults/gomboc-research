# material-ac364159cba0

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J85 recovered dynamic coordinates — literal exact inputs, no optimizer dependency

The J85 working directory was lost during this coordinator turn. Re-execution of the complete dynamic85.py from [internal-source-reference], starting from durable J85_CLASS_FIRST_G8 in [internal-source-reference], reproduced BOTH dynamic rational input hashes and all four exact report/cube hashes. This closes the former source gap for these two inputs. The literal bytes are now preserved below, so further recovery does NOT require numerical optimization. This is justified source recovery after a real reset, not an independently implemented verification engine.

Both bodies have V45/E129/F86,C258, own strict121, additionalweak000, one positive P and no Q. G8 has P .4552962231087733 and sufficient fixed-surface S1 cube rho3.0884500134885855e-7. G10 has P .4552962200930236 and rho3.112849668956749e-7. Material U0/40, S triangle{0,30,40}, saddle21--30. Compared with the literal parent J85_CLASS_FIRST_G8,18 triangular support sets disappear and18 new sets appear; this is not a claim of36 independent flips. The finite remaining basin is NOT cancelled. Canonical own110 remains C622; no own110 under500 is claimed.

For exact replay, extract the two JSON inputs and replay_recovered85.py below. Its complete required source dependencies are: exact84.py from [internal-source-reference]; freeze85.py from [internal-source-reference]; freeze_dynamic85.py from [internal-source-reference]. That last helper contains exhaustive rational supporting-triple reconstruction and explicitly rejects nonsimplicial endpoints. It does not call the numerical optimizer. These three materials plus this one also supply the complete inputs/code for the single- and double-stellar constructions in the latter source material. Their later continued-B coordinate gap remains separate until explicitly closed.

Save each block with its final LF. Run CPython3.13.5 standard library: python replay_recovered85.py. Observed marker: J85_DYNAMIC_TWO_LITERAL_COORDINATES_REPLAY_PASS_NO_110. Source replay_recovered85.py1397B/SHAacb2c4764bd987c4388e104023682d1f66f245f3a02f63baf0ef719a87bc82a9.

Manifest:
J85_DYNAMIC_A_G8_INPUT.json1432B/1c45fe7c95d2454c29596c1ce6dd3ccaf39cefd465026bd1d2c10a97aae6f847
J85_DYNAMIC_A_G10_INPUT.json1705B/ec1c1f91d911177b4cd23e9d5e1fd6ea63303e7890bd4bc3c3e91572021331f2
J85_DYNAMIC_A_G8_EXACT.json5081B/89c2df30c23aa633aee17856618b45c4d516063cd74b3d043de7874859f0e601
J85_DYNAMIC_A_G8_CUBE.json102262B/24ff7c50b0537c100f03d30a3255bd283b52f77dd294d679726d9c052abc91ef
J85_DYNAMIC_A_G10_EXACT.json5849B/bbe05ad650ebef59a3a488db2f840c6a57e77b7ec315d5abafba479b4aa6f888
J85_DYNAMIC_A_G10_CUBE.json126715B/2d2de8de29dd74c297ec051f23ccf2816d9fb160cb9bbc9cb1788fffcdb82c77

## J85_DYNAMIC_A_G8_INPUT.json
```json
{"denominator":100000000,"name":"J85_DYNAMIC_A_G8","points":[[-177249800,-122247600,44660000],[-110344644,-35425568,-75605216],[-96395427,-17813038,10945047],[-84770118,542150,1386945],[-81666556,8990167,-24769650],[-80500679,-23934149,-96753890],[-81254359,8911510,-35328030],[-64232300,-21120803,-104001236],[-65392701,23070599,-17102503],[-57400481,26227185,-46449417],[-48543074,-21263979,-107947896],[-38143269,-21382744,-109282000],[-42210660,25056016,13060655],[-34527632,48494196,-37923439],[-34334077,51608092,-23149963],[-28141555,-21105114,-109393145],[-23341302,44230341,-47970292],[-23223120,52822573,-6771477],[-18417532,-23835283,-108482949],[-17759958,-59910684,-69330127],[-14072693,32381474,-58713015],[-10619053,-25982462,-106957283],[-8519568,51546830,12829123],[-7435212,22681938,-66169111],[-2065552,47599572,18086576],[2019909,19752398,29952194],[6975619,45285692,22193018],[17222496,43179404,25397889],[40080610,37823391,29206546],[46639847,30356092,29992514],[50321082,-47414442,-88613043],[53862645,22988476,29569600],[60415486,14579200,27852759],[63771517,22103408,452452],[66321960,5694331,24718533],[71969391,-12419373,-66783008],[72343413,-3288047,19851901],[77810977,-859596,-40121128],[77359942,-12684523,13066016],[81282876,-21443741,4756455],[84185932,-45482928,-49850689],[85545042,-42382512,-31436203],[84166146,-29595354,-5441750],[85795085,-36791218,-17750700],[86686841,-35760790,-37118957]]}
```

## J85_DYNAMIC_A_G10_INPUT.json
```json
{"denominator":10000000000,"name":"J85_DYNAMIC_A_G10","points":[[-17724980000,-12224760000,4466000000],[-11034464362,-3542556753,-7560521595],[-9639542678,-1781303769,1094504733],[-8477011794,54215008,138694511],[-8166655552,899016652,-2476964965],[-8050067857,-2393414918,-9675388900],[-8125435863,891151013,-3532802970],[-6423230021,-2112080288,-10400123603],[-6539270070,2307059879,-1710250319],[-5740048127,2622718500,-4644941652],[-4854307360,-2126397944,-10794789585],[-3814326871,-2138274413,-10928199972],[-4221066025,2505601594,1306065503],[-3452763190,4849419576,-3792343943],[-3433407720,5160809162,-2314996317],[-2814155536,-2110511369,-10939314539],[-2334130183,4423034088,-4797029176],[-2322311978,5282257320,-677147726],[-1841753180,-2383528324,-10848294907],[-1775995812,-5991068427,-6933012700],[-1407269264,3238147352,-5871301466],[-1061905270,-2598246235,-10695728327],[-851956805,5154683031,1282912253],[-743521235,2268193823,-6616911138],[-206555187,4759957151,1808657572],[201990922,1975239841,2995219391],[697561920,4528569217,2219301850],[1722249639,4317940377,2539788937],[4008061012,3782339053,2920654607],[4663984683,3035609184,2999251416],[5032108222,-4741444210,-8861304296],[5386264535,2298847568,2956960035],[6041548550,1457919969,2785275896],[6377151707,2210340793,45245250],[6632196045,569433067,2471853347],[7196939088,-1241937281,-6678300787],[7234341350,-328804711,1985190087],[7781097741,-85959614,-4012112753],[7735994153,-1268452338,1306601599],[8128287600,-2144374081,475645464],[8418593208,-4548292793,-4985068931],[8554504232,-4238251189,-3143620347],[8416614608,-2959535394,-544175009],[8579508530,-3679121784,-1775070001],[8668684131,-3576079007,-3711895705]]}
```

## replay_recovered85.py
```python
"""Exact cold replay from the two literal recovered J85 dynamic inputs.
Dependencies: exact84.py, freeze85.py, freeze_dynamic85.py. No optimizer.
"""
import json,hashlib
from exact84 import ROOT,audit
from freeze85 import cube,dump
from freeze_dynamic85 import exact_hull
CASES={
 'J85_DYNAMIC_A_G8':('1c45fe7c95d2454c29596c1ce6dd3ccaf39cefd465026bd1d2c10a97aae6f847','89c2df30c23aa633aee17856618b45c4d516063cd74b3d043de7874859f0e601','24ff7c50b0537c100f03d30a3255bd283b52f77dd294d679726d9c052abc91ef'),
 'J85_DYNAMIC_A_G10':('ec1c1f91d911177b4cd23e9d5e1fd6ea63303e7890bd4bc3c3e91572021331f2','bbe05ad650ebef59a3a488db2f840c6a57e77b7ec315d5abafba479b4aa6f888','2d2de8de29dd74c297ec051f23ccf2816d9fb160cb9bbc9cb1788fffcdb82c77')}
for name,(si,se,sc) in CASES.items():
    raw=(ROOT/(name+'_INPUT.json')).read_bytes();assert hashlib.sha256(raw).hexdigest()==si
    j=json.loads(raw);P,F,ids=exact_hull(j['points'],j['denominator']);r=audit(P,F)
    r['name']=name;r['material_rows']=ids
    assert (r['V'],r['E'],r['F'])==(45,129,86) and r['strict']==[1,2,1] and r['weak']==[0,0,0]
    assert [ids[i] for i in r['U']]==[0,40] and {ids[i] for i in F[r['S'][0]]}=={0,30,40}
    assert len(r['P'])==1 and not r['Q']
    assert dump(name+'_EXACT.json',r)['sha256']==se
    assert dump(name+'_CUBE.json',cube(P,F))['sha256']==sc
print('J85_DYNAMIC_TWO_LITERAL_COORDINATES_REPLAY_PASS_NO_110',flush=True)
```
