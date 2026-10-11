import ast,hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).parent;BASE=ROOT.parent
s=json.loads((BASE/"reconnect-figure-20260915-1551-OoOtnw/figure-heartbeat-2138.json").read_text())["journal"]["delta"]
blocks=re.findall("^"+chr(96)*3+r"([^\n]*)\n(.*?)^"+chr(96)*3,s,re.M|re.S)
specs=[("dual_chain.py","python",5008,"d0677e0070d5475b75039a26c3d90f9bdd56b025d79c3fed3e4729c042b55e7b"),("POINTS25.json","json",425,"1be5293390fbabf8b86b02805771d0fed82fddd2c61678b58d36c7bab9f93cd8"),("vertexbeam282.py","python",2137,"2f82f8938825723be9d531a09e4025199fead8e6d175eb8eadf99f49eade3e5a")]
sha=lambda b:hashlib.sha256(b).hexdigest()
if len(blocks)!=3:raise ValueError("Source count")
data={}
for (lang,text),(name,expected_lang,size,pin)in zip(blocks,specs):
    if lang!=expected_lang:raise ValueError("Source order")
    if lang=="json":
        if not text.endswith("\n"):raise ValueError("JSON separator")
        text=text[:-1];json.loads(text)
    else:ast.parse(text,filename=name)
    b=text.encode()
    if len(b)!=size or sha(b)!=pin:raise ValueError("Source pin "+name)
    data[name]=b
parent=BASE/"figure-c282-integer-own211-20260915"
old=(parent/"POINTS49.json").read_bytes()
if len(old)!=776 or sha(old)!="c01c8c5eb79a099250ea9f2c8cf8d85a17546abe7ab2b58129a78a6df3e1aaa7":raise ValueError("Parent points")
ids=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,21,28,35,37,39,41,43,45,46,47,48]
points=json.loads(data["POINTS25.json"])["points"]
if points!=[json.loads(old)["points"][i]for i in ids]:raise ValueError("Exact subset mismatch")
exact=(parent/"c182_chain/exact_points.py").read_bytes()
if len(exact)!=2031 or sha(exact)!="e0cd67ba8ee150996c387c03cb91629dea8ce5fb1252fb1af832018cdac980db":raise ValueError("Existing verifier pin")
core=BASE/"figure-finch3-c182-c592-nonwinners-20260915/source/core"
pins={"check_A.py":"ad72cc198140249c1e52a615513354036c04f4c718333a7beed64fba4b43d7f3","check_B.py":"b0cb62d5486b32d020b60f717f3dfe9d07c6c9a978492928f54c3a38f396fc24","centred_mass.py":"5f1afafa0432436bfe953a94d94ca1027c12549504f9452491f0287c2a29d1a8"}
for name,pin in pins.items():
    if sha((core/name).read_bytes())!=pin:raise ValueError("Core pin")
def write(name,b):
    p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("xb")as f:f.write(b)
    if p.read_bytes()!=b:raise ValueError("Readback")
for name,b in data.items():write(name,b)
write("POINTS49.json",old)
for name,size,pin in [("raw.json",2483,"8254152f25df690b4da9ab394ab44c25041d449bfaa552272f5455c43b09c1e7"),("A.json",10127,"374a1eda3378fbee5cb42d9fe11d52312215fa3a15b222768a2d5f8d2a16bbce")]:
    b=(parent/"local-proof"/name).read_bytes()
    if len(b)!=size or sha(b)!=pin:raise ValueError("Numerical parent input pin")
    write("recovered282/"+name,b)
write("canonical-entries.md",s.encode())
r={"at":datetime.now(timezone.utc).isoformat(),"identity":"COORD_C138_INTEGER_VERTEX25_OWN211","journalEvents":[1419,1420],"sourceAndInputFiles":3,"parentInputCopies":3,"literalRetainedParentIds":ids,"dependency":{"verifier":str(parent/"c182_chain/exact_points.py"),"verifierSha256":sha(exact),"core":str(core),"corePins":pins},"localMathematicalReplayExecuted":False,"numericalSearchRerun":False,"verification":"Three new source/inputpins, exact25-pointsubsetidentity, existing exactauditor dependencies and3required unmodified-numerical-inputcopies checked. JSON terminalnewline omittedexactlyasauthorrequires, no coordinatechange.","files":{n:{"bytes":len(b),"sha256":sha(b)}for n,b in data.items()}}
write("source-integrity-receipt.json",(json.dumps(r,indent=2)+"\n").encode())
print(json.dumps(r))
