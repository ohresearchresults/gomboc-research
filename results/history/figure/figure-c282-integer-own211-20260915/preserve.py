import ast,hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).parent;BASE=ROOT.parent
snap=BASE/"reconnect-figure-20260915-1551-OoOtnw/figure-heartbeat-2108.json"
entry=json.loads(snap.read_text())["journal"]["delta"]
blocks=re.findall("^"+chr(96)*3+r"([^\n]*)\n(.*?)^"+chr(96)*3,entry,re.M|re.S)
specs=[
 ("POINTS49.json","json",776,"c01c8c5eb79a099250ea9f2c8cf8d85a17546abe7ab2b58129a78a6df3e1aaa7"),
 ("c182_chain/exact_points.py","python",2031,"e0cd67ba8ee150996c387c03cb91629dea8ce5fb1252fb1af832018cdac980db"),
 ("c182_affine/affine_search.py","python",4858,"e162a2c480f6ba6185460b858343db844f172199f8ac7c5339181acd330455a4"),
 ("c182_affine/metric_milp.py","python",4476,"3e338a0bffc721778a3356fc27e119aa3b6c1705e5f4c6343e361ff9e993d966"),
 ("c182_affine/metric_milp2.py","python",6250,"fc984d98253a2c756e7748cd43dc211a6422cf3e9b78c2e287c796ddb58c2443"),
 ("c182_affine/CUTS.json","json",869,"6445be4d8103d0409f34238510d5f9f04584e86ade306f099439ada869cb681a"),
 ("c182_chain/chain_search2.py","python",4090,"bfdf1c1ff606b69df6888aa56d836d56e03842a155ba9dc24e8bafd9a7ad47e1"),
 ("c182_chain/produce282.py","python",1748,"a9b3f3f3d0be38227a5ff34197547488954f54d7f3303ae12dc25214c5ae88e7")]
sha=lambda b:hashlib.sha256(b).hexdigest()
if len(blocks)!=len(specs):raise ValueError("Source block count")
files={}
for (lang,text),(name,kind,length,pin)in zip(blocks,specs):
    if lang!=kind:raise ValueError("Source order")
    if kind=="json":
        if not text.endswith("\n"):raise ValueError("Missing Markdown separator newline")
        text=text[:-1] # Author explicitly specifies no final newline for both JSON files.
        json.loads(text)
    else:ast.parse(text,filename=name)
    b=text.encode()
    if len(b)!=length or sha(b)!=pin:raise ValueError("Literal pin "+name)
    files[name]=b
parent=BASE/"figure-finch3-c182-c592-nonwinners-20260915"
pr=json.loads((parent/"integrity-receipt.json").read_text())
for name,pin in pr["files"].items():
    b=(parent/"source"/name).read_bytes()
    if len(b)!=pin["bytes"]or sha(b)!=pin["sha256"]:raise ValueError("Parent source pin")
points=json.loads(files["POINTS49.json"])["points"]
if len(points)!=49 or len(set(map(tuple,points)))!=49 or not all(isinstance(c,int)for p in points for c in p):raise ValueError("Point identity")
def write(name,b):
    p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("xb")as f:f.write(b)
    if p.read_bytes()!=b:raise ValueError("Readback")
for name,b in files.items():write(name,b)
write("canonical-entries.md",entry.encode())
r={"at":datetime.now(timezone.utc).isoformat(),"identity":"COORD_C282_OPPOSED_CHAIN_G1000_OWN211","journalEvents":[1413,1414],"sourceAndInputFiles":len(files),"rawPointCount":49,"rawCoordinates":"Integer convex hull; defining final body is translated by its exact own filled centroid","dependency":{"directory":str(parent/"source"),"verifiedFiles":44,"exactCore":str(parent/"source/core"),"canonicalCaveat":"Intactimmutableparent/operator44sourcepackage used; Finch six-partjournal copyknowncorrupt andunrepaired"},"localMathematicalReplayExecuted":False,"verification":"All8literal source/input pins, explicit JSON no-final-newline convention, PythonAST/JSON and44upstreamsourcepins verified. Fresh local exact replay has separate receipt.","completeRecoveryPreservedLocally":True,"files":{name:{"bytes":len(b),"sha256":sha(b)}for name,b in files.items()}}
write("source-integrity-receipt.json",(json.dumps(r,indent=2)+"\n").encode())
print(json.dumps(r))
