# material-2b2ce5534688

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# FREE_FIRST_G8_EXACT_MATERIAL_CHECKPOINT_V1

## Accepted object and limits
FREE_FIRST_G8 is the convex hull of the complete31 integer rows below divided by100000000. Its exact maximal hull has V30/E84/F56/C168; strict own817=(8,1,7), weak817, additionalweak000, primitivezero000. No own110 claim. Actual mass and centroid are rationally integrated. The complete P landscape has zero positive bars. Seven Q bars have birth-relative depths approximately0.0002116565141,0.0001836693801,0.0011844703623,0.0030908832522,0.0045499276786,0.0012253181306,0.6206680020792; the total is about0.631114. The parent RESERVE31's singleQ depth is0.8220302331638814 to shown precision; this is a useful reduction of the total barrier, but at the cost of six additional stable equilibria. Counts cannot be replaced by a small barrier objective.

Origin: hull-aware free movement of31 parent extreme input points with SLSQP at actual mass, bound radius1 in per-axis parent standard-deviation units, required complete-input physical escape cosine1e-5 for every original input except root30, negative maximum escape at root30, volume at least0.05 times parent. The exact input below is binary64 independent ties-to-even freezing at1e8 of the saved first successful feasible checkpoint at call202. The search later encountered a float coplanar-group ownership error; no finished first-run ledger is claimed. The literal freeze is authoritative, not that interrupted optimizer. Full numerical source is to be archived separately; it is NOT needed to recover these coordinates.

## Exact source dependency and reconstruction
The object itself is completely represented below. For the audit, obtain complete exact_ref.py from immutable material [internal-source-reference], RESERVE31_REFERENCE110_AND_INNER_CENTROID_BOUND_V1.md, SHA256 dc6d8d69f00d801023c9cd0305395cf7fc5dacaec4f49c36e52c56426438991c. A worker using this checkpoint must receive BOTH materials. The source module SHA256 is ecd35ed2829159f7a513de38f5a936a649ee00e84d2c173dac37ab291d7e2abb,7364bytes. No body data are omitted in that dependency.

Save the one-line JSON with one final newline as FREE_FIRST_G8_INPUT.json. Save this complete audit invocation as audit_free_first.py and run `python audit_free_first.py`. Python3.13.5 standard library only. It calls the preserved exhaustive rational hull/mass/equilibrium/complete radial-graph auditor without changing it.

```python
from pathlib import Path
import json,hashlib
from exact_ref import complex_from_integer,audit
root=Path(__file__).parent
raw=(root/'FREE_FIRST_G8_INPUT.json').read_bytes()
assert len(raw)==979 and hashlib.sha256(raw).hexdigest()=='5b9b38f861e605bbc6db102e000cdd1325cfb2fde88de70a43542fed385348f3'
x=json.loads(raw)
P,F,E,V,M,c=complex_from_integer(x['points'],x['denominator'])
a=audit(P,F,E,V,M,c,c)
assert (len(P),len(E),len(F))==(30,84,56)
assert a['strict']==[8,1,7] and a['additional_weak']==[0,0,0] and a['primitive_zero']==[0,0,0]
assert len(a['P_bars'])==0 and len(a['Q_bars'])==7
text=json.dumps(a,sort_keys=True,separators=(',',':'))+'\n'
assert len(text.encode())==9792 and hashlib.sha256(text.encode()).hexdigest()=='655e4f47e3703fd9ae70585ba03a9dec6d8a0db9e9d45157531841bebd3779a4'
(root/'FREE_FIRST_G8_EXACT.json').write_text(text)
print('FREE_FIRST_G8_EXACT_817_WEAK000_PASS')
```

Underlying exact computation and output hash were observed before preservation. This convenience invocation adds equivalent assertions; its new marker is not a separately observed independent run. Verification: `sha256sum FREE_FIRST_G8_INPUT.json FREE_FIRST_G8_EXACT.json`; expected979 and9792bytes, hashes as asserted.

## FREE_FIRST_G8_INPUT.json
```json
{"denominator":100000000,"points":[[-95260360,-1031143,23122621],[-94051163,-3631501,44688613],[-92098354,1829731,2204422],[-90126324,6200326,61133417],[-93282642,-17915257,29827987],[-88995027,-30085790,14180771],[-82707326,16016101,76813837],[-84730193,2225550,-17634420],[-81303438,-39993476,-1560819],[-73109097,5452578,-35522284],[-71659396,24390306,91830663],[-70180241,-47829975,-16568043],[-58715231,-1635930,-49926838],[-57055870,30623867,105810681],[-55206767,-54833734,-29131646],[-38747466,36569140,117625676],[-35993761,3533446,-62705456],[-33022028,-74373373,-11059792],[-36458014,-53959408,-44010339],[-16752533,42827950,126021305],[-13985731,-49334939,-54616748],[13311135,-59682474,-42621834],[9238871,-77251057,4011284],[9209500,49287790,129842478],[10411129,-28362145,-62041104],[423737,-47060997,-44543750],[38211993,55466778,127303534],[64493858,37122344,-32124346],[69081104,60828548,116628598],[103051400,65034009,93758298],[163824235,67195737,17657236]]}
```
