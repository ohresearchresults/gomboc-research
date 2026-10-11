import hashlib,json,platform,sys
from datetime import datetime,timezone
from fractions import Fraction as F
from math import lcm
from pathlib import Path
ROOT=Path(__file__).parent;OUT=ROOT/"local-proof"
sha=lambda b:hashlib.sha256(b).hexdigest()
pins={"raw.json":(1157,"5eb68c9a67409dd582d79df1fcdc764d057da979db0e53373c0a7c086221582f"),"A.json":(5169,"b8b614fec6f96fbc7844e1fe3ed3232d62587d1310fdb2c2b6e40f17ab1dabc0"),"B.json":(5169,"b8b614fec6f96fbc7844e1fe3ed3232d62587d1310fdb2c2b6e40f17ab1dabc0"),"MASS.json":(216,"82e54e84b880d4c233477d50b31af9df0772081d3800f6693f4727ebac3e90bf")}
for name,(size,pin)in pins.items():
    b=(OUT/name).read_bytes()
    if len(b)!=size or sha(b)!=pin:raise ValueError("Exact output pin")
a=json.loads((OUT/"A.json").read_text());m=json.loads((OUT/"MASS.json").read_text());P=json.loads((ROOT/"POINTS25.json").read_text())["points"]
assert set(tuple(map(F,r))for r in a["raw_vertices"])==set(map(tuple,P))
assert [a[k]for k in["V","E","F"]]==[25,69,46] and a["counts"]==[2,1,1]and a["weak"]==[0,0,0]
assert all(len(f)==3 for f in a["faces"])
assert a["stable_face_ids"]==[22,45]and a["unstable_vertices"]==[14]and a["saddle_edges"]==[[15,22]]
assert all(a[k]==0 for k in["face_primitive_zero_count","vertex_max_zero_count","edge_primitive_zero_count"])
assert a["centred_first_moments"]==[0,0,0]and m["tetrahedra"]==46
g=tuple(map(F,a["raw_centroid"]));assert g==(F(-1510919059,205647994),F(-1322990120,102823997),F(-1106176611,411295988))
assert F(a["ordinary_volume"])==F(102823997,6)
D=lcm(*(v.denominator for v in g));assert D==411295988 and D.bit_length()==29
r={"at":datetime.now(timezone.utc).isoformat(),"status":"LOCAL_C138_INTEGER_HULL_AB_AND_THIRD_MASS_PASS","identity":"COORD_C138_INTEGER_VERTEX25_OWN211","V":25,"E":69,"F":46,"C":138,"own":[2,1,1],"weak":[0,0,0],"allMaximalFacetsTriangular":True,"rawCentroid":a["raw_centroid"],"ordinaryVolume":a["ordinary_volume"],"commonCentredDenominator":D,"denominatorBits":29,"denominatorDecimalDigits":len(str(D)),"maxCentredIntegerBits":m["common_centred_integer_coordinate_max_bits"],"rawIntegerBounds":[min(v for p in P for v in p),max(v for p in P for v in p)],"outputs":{n:{"bytes":x[0],"sha256":x[1]}for n,x in pins.items()},"python":sys.version,"platform":platform.platform(),"method":"Fresh exactsupportingplane enumeration from25literalintegerpoints,bothfullindependentA/Bandthirdcentredmass,alloutputpinsmatched. No cachedgeometricreportinput.","numericalBeamOrDualChainReplayExecuted":False,"scope":"NonwinnerwithoneextraS/Hpair,notown110/globalminimum. C622recordunchanged."}
with(OUT/"RECEIPT.json").open("x")as f:json.dump(r,f,indent=2)
print(json.dumps(r))
