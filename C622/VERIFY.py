import ast,hashlib,json,os,sys,time
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SRC=ROOT/"source"
OUT=ROOT/(sys.argv[1] if len(sys.argv)>1 else "fresh-proof")
B=lambda x:json.dumps(x,sort_keys=True,separators=(",",":")).encode()
H=lambda b:hashlib.sha256(b).hexdigest()
if not __debug__:raise RuntimeError("Assertions required")
manifest_bytes=(SRC/"MANIFEST.json").read_bytes()
assert H(manifest_bytes)=="d06bc3d5782b4ebf2449b4bd89e962ce88f08faca9d06ae068a5bfaf22af0c53"
manifest=json.loads(manifest_bytes)
for name,pin in manifest.items():
    p=SRC/name;assert not Path(name).is_absolute() and ".." not in Path(name).parts
    data=p.read_bytes();assert H(data)==pin,name
    if name.endswith(".py"):ast.parse(data,filename=name)
    if name.endswith(".json"):json.loads(data)
OUT.mkdir(exist_ok=False)
started=datetime.now(timezone.utc).isoformat();start=time.monotonic()
def put(name,value):
    data=B(value);p=OUT/name
    with p.open("xb")as f:f.write(data)
    assert p.read_bytes()==data
    return {"bytes":len(data),"sha256":H(data)}
put("START.json",{"at":started,"pid":os.getpid(),"scope":"Only C622_ROUTED endpoint plus tiny rejection/weak fixtures; not full ten-case batch"})
sys.path[:0]=[str(SRC/"methods"),str(SRC/"methods/parent")]
import G_FREE_CODEC,RECONSTRUCT,check_A,check_B,centred_mass
g=G_FREE_CODEC.decode(json.loads((SRC/"inputs/C622_ROUTED.json").read_text()))
assert B(g)==(ROOT/"GENERATOR.json").read_bytes()
assert H(B(g))=="3cbd90d799189108f26b941800c8fa79a6f1c5abb17b2db614f0e54f57fffee7"
put("GENERATOR.json",g);raw=RECONSTRUCT.recover(g)
assert len(B(raw))==15437 and H(B(raw))=="ac01d1625274b64f336a715e1f5462f40686f647f0b7d1a4d90a5ee21765adb5"
raw_pin=put("raw.json",raw);reports={};pins={}
for label,fn in [("A",check_A.run),("B",check_B.run)]:
    print(json.dumps({"phase":"START_"+label,"elapsedSeconds":round(time.monotonic()-start,3)}),flush=True)
    a=fn(raw)
    assert [a[k]for k in("V","E","F")]==[176,311,137]
    assert a["counts"]==[1,1,0] and a["weak"]==[0,0,0]
    assert a["active_input_indices"]==list(range(137))
    assert a["centred_first_moments"]==[0,0,0]
    assert all(a[k]==0 for k in ["face_primitive_zero_count","vertex_max_zero_count","edge_primitive_zero_count"])
    assert a["edge_primitive_count"]==1244 and a["integration_triangle_count"]==348
    data=B(a);assert len(data)==311825 and H(data)=="142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0"
    assert data==(ROOT/("ENDPOINT_"+label+".json")).read_bytes()
    pins[label]=put(label+".json",a);reports[label]=a
    print(json.dumps({"phase":"COMPLETE_"+label,"elapsedSeconds":round(time.monotonic()-start,3),"V_E_F":[a[k]for k in("V","E","F")],"own":a["counts"],"weak":a["weak"],"sha256":H(data)}),flush=True)
assert reports["A"]==reports["B"]
print("START_THIRD_MASS",flush=True)
mass=centred_mass.run(reports["A"])
assert mass["tetrahedra"]==348 and mass["filled_first_moments"]==[0,0,0]
assert mass["common_centred_denominator_bits"]==56802 and mass["volume_agrees_with_A_and_B"]is True
mass_pin=put("CENTRED_MASS.json",mass)
fixtures=[]
for hh,c,w in [([[-1,-1,-1,1],[-1,1,1,1],[1,-1,1,1],[1,1,-1,1]],[4,4,6],[0,0,0]),([[1,0,0,1],[-2,3,0,1],[1,-3,0,1],[0,0,1,1],[0,0,-1,1]],[4,4,6],[1,2,3])]:
    a=check_A.run({"H":hh});b=check_B.run({"H":hh});assert a==b and a["counts"]==c and a["weak"]==w
    fixtures.append({"counts":c,"weak":w})
for hh in ([[1,0,0,-1]]*4,[[1,0,0,1]]*4,[[1,0,0,1],[-1,0,0,1],[0,1,0,1],[0,-1,0,1]]):
    for fn in [check_A.run,check_B.run]:
        try:fn({"H":hh})
        except (AssertionError,ValueError):pass
        else:raise AssertionError("Malformed or unbounded fixture accepted")
receipt={"status":"LOCAL_C622_ENDPOINT_TWO_EXACT_AUDITS_AND_THIRD_MASS_PASS","startedAt":started,"completedAt":datetime.now(timezone.utc).isoformat(),"elapsedSeconds":round(time.monotonic()-start,3),"sourceManifestEntriesChecked":len(manifest),"generatorSha256":H(B(g)),"raw":raw_pin,"reports":pins,"V":176,"E":311,"F":137,"C":622,"strict":[1,1,0],"weak":[0,0,0],"mass":mass,"massFile":mass_pin,"fixtures":fixtures,"malformedFixturesRejected":True,"fullTenCaseBatchExecuted":False,"stressAtlasNumericalReplayExecuted":False,"scope":"Local fresh source-only endpoint reconstruction and both supplied independent exact algorithms plus third mass/fixtures; no global minimum or external peer-review claim"}
put("RECEIPT.json",receipt)
print(json.dumps(receipt),flush=True)
