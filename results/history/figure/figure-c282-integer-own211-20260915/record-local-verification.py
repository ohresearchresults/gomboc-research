import hashlib,json,platform,sys
from datetime import datetime,timezone
from fractions import Fraction as F
from math import lcm
from pathlib import Path
ROOT=Path(__file__).parent;OUT=ROOT/"local-proof"
sha=lambda b:hashlib.sha256(b).hexdigest()
pins={"raw.json":(2483,"8254152f25df690b4da9ab394ab44c25041d449bfaa552272f5455c43b09c1e7"),"A.json":(10127,"374a1eda3378fbee5cb42d9fe11d52312215fa3a15b222768a2d5f8d2a16bbce"),"B.json":(10127,"374a1eda3378fbee5cb42d9fe11d52312215fa3a15b222768a2d5f8d2a16bbce"),"MASS.json":(216,"c84b76eda223c2c426545c4f51b602c0e6e4d0262a72be0f069a351576dcd2a0")}
for name,(size,pin)in pins.items():
    b=(OUT/name).read_bytes()
    if len(b)!=size or sha(b)!=pin:raise ValueError("Local output pin")
a=json.loads((OUT/"A.json").read_text());mass=json.loads((OUT/"MASS.json").read_text())
points=json.loads((ROOT/"POINTS49.json").read_text())["points"]
assert set(tuple(map(F,v))for v in a["raw_vertices"])==set(map(tuple,points))
assert [a[k]for k in["V","E","F"]]==[49,141,94]and a["counts"]==[2,1,1]and a["weak"]==[0,0,0]
assert all(len(f)==3 for f in a["faces"])
assert a["stable_face_ids"]==[28,93]and a["unstable_vertices"]==[21]and a["saddle_edges"]==[[14,34]]
assert a["centred_first_moments"]==[0,0,0]
assert all(a[k]==0 for k in["face_primitive_zero_count","vertex_max_zero_count","edge_primitive_zero_count"])
assert a["edge_primitive_count"]==564
g=tuple(map(F,a["raw_centroid"]))
assert g==(F(-181946001,670092982),F(335691589,1340185964),F(-100923148,335046491))
assert F(a["ordinary_volume"])==F(335046491,6)
h=lcm(*(v.denominator for v in g))
assert h==1340185964 and h.bit_length()==31
assert mass["tetrahedra"]==94 and mass["filled_first_moments"]==[0,0,0]
r={"at":datetime.now(timezone.utc).isoformat(),"status":"LOCAL_C282_INTEGER_HULL_TWO_EXACT_AUDITS_AND_THIRD_MASS_PASS","identity":"COORD_C282_OPPOSED_CHAIN_G1000_OWN211","V":49,"E":141,"F":94,"C":282,"own":[2,1,1],"weak":[0,0,0],"allMaximalFacetsTriangles":True,"inputIntegers":{"count":49,"min":-507,"max":643},"rawCentroid":a["raw_centroid"],"ordinaryVolume":a["ordinary_volume"],"commonCentredDenominator":h,"commonCentredDenominatorBits":31,"commonCentredDenominatorDecimalDigits":len(str(h)),"centredNumeratorMaxBits":mass["common_centred_integer_coordinate_max_bits"],"outputs":{n:{"bytes":v[0],"sha256":v[1]}for n,v in pins.items()},"python":sys.version,"platform":platform.platform(),"executedCommand":"nice -n 10 python3 -u -B -S c182_chain/exact_points.py POINTS49.json local-proof --core ../figure-finch3-c182-c592-nonwinners-20260915/source/core","freshComputation":"Supporting planes re-enumerated from49literalintegerpoints, both complete independent exactauditors run, thirdcentredmassrun, alloutputpinsmatch. Downloaded/precomputedgeometry wasnotaninput.","numericalDiscoveryReplayExecuted":False,"scope":"Locallyverifiedmonounstable/2stable nonwinner, notGömböc,not globalminimum. Acceptedown110recordC622 unchanged."}
with(OUT/"RECEIPT.json").open("x")as f:json.dump(r,f,indent=2)
print(json.dumps(r))
