import ast,hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).parent;BASE=ROOT.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
text=(ROOT/"native-result.md").read_text()
blocks=re.findall("^"+chr(96)*3+r"python\n(.*?)^"+chr(96)*3,text,re.M|re.S)
if len(blocks)!=1:raise ValueError("Ambiguous method unit")
source=blocks[0].encode();ast.parse(source,filename="opposite_mass_gate.py")
deps=[]
for folder,files,decoded in [("figure-four-frontiers-core-20260915",16,"50061fcdfeb6cc42de880bfe1805441e4ed8cf3df4a2c78d6cbd9cf079496d19"),("figure-c592-exposed-chain-20260915",6,"57d0644b73858349341fad8f3f55fd83a00c4485efef5d0cdc49afb9b5a16320")]:
    p=BASE/folder;r=json.loads((p/"integrity-receipt.json").read_text())
    if r["sourceFiles"]!=files or r["decodedSha256"]!=decoded:raise ValueError("Dependency identity")
    for n,pin in r["files"].items():
        b=(p/"source"/n).read_bytes()
        if len(b)!=pin["bytes"]or sha(b)!=pin["sha256"]:raise ValueError("Dependency file pin")
    deps.append({"directory":str(p/"source"),"files":files,"decodedSha256":decoded})
out=ROOT/"opposite_mass_gate.py"
if out.exists()or(ROOT/"integrity-receipt.json").exists():raise FileExistsError("Already preserved")
with out.open("xb")as f:f.write(source)
if out.read_bytes()!=source:raise ValueError("Source readback")
r={"at":datetime.now(timezone.utc).isoformat(),"identity":"NH72_C592_OPPOSITE_POINT_MASS_GATE","sourceFiles":1,"sourceBytes":len(source),"sourceSha256":sha(source),"nativeResultSha256":"f6901be7929b0cb34c8692771c1aa8f8b7b5314cefccd0a208bef020b13520e8","dependencies":deps,"inputAuditPins":{"C592_A":"d200af2491ba532cd9307caceb4d780e9a661a4c9094da10e4e0c3562875204d","C602_A":"2426da394eda9520bd30b2b8b3e1f00d043697353bb6bc73658f5983653c11ec"},"localMathematicalOrMethodReplayExecuted":False,"authorFinalMethodReplayObserved":False,"scope":"Exact analytical augmentation/centroid-region obstruction plus rational visibility-chamber moment/Jacobian formulas. No new fully bound successor coordinates or census claimed. Final method source has no separate author SHA in prose; exact native-result pin binds its literal bytes, local SHA recorded.","completeAnalyticalMethodRecoveryPreserved":True,"unboundNumericalCandidateSourcesComplete":False}
with(ROOT/"integrity-receipt.json").open("x")as f:json.dump(r,f,indent=2)
print(json.dumps(r))
