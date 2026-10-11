import ast,hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).parent;BASE=ROOT.parent
s=json.loads((BASE/"reconnect-figure-20260915-1551-OoOtnw/figure-heartbeat-1711.json").read_text())["journal"]["delta"]
tick=chr(96)*3
blocks=re.findall("^"+tick+r"python\n(.*?)^"+tick,s,re.M|re.S)
sha=lambda b:hashlib.sha256(b).hexdigest()
if len(blocks)!=1:raise ValueError("Ambiguous source")
source=blocks[0].encode()
if len(source)!=3036 or sha(source)!="281d5dbba9510c39e85159eb969e421d7b5a9b3f96486ae4a2748880ac832f4c":raise ValueError("Source pin")
ast.parse(source)
parent=BASE/"figure-c598-projective-metric-20260915"
parent_src=(parent/"PM598_RECOVER.py").read_bytes()
if len(parent_src)!=3517 or sha(parent_src)!="ce93a45eda31171f603d17133a5c8de885cbdb24d5c5ef63b62195d3874c3276":raise ValueError("Parent recovery pin")
core=BASE/"figure-four-frontiers-core-20260915/source";cr=json.loads((core.parent/"integrity-receipt.json").read_text())
for name in ["check_A.py","check_B.py","centred_mass.py"]:
    b=(core/name).read_bytes();p=cr["files"][name]
    if len(b)!=p["bytes"]or sha(b)!=p["sha256"]:raise ValueError("Core dependency pin")
def write(n,b):
    with(ROOT/n).open("xb")as f:f.write(b)
    if(ROOT/n).read_bytes()!=b:raise ValueError("Readback mismatch")
write("PM580_RECOVER.py",source);write("canonical-entry.md",s.encode())
receipt={"at":datetime.now(timezone.utc).isoformat(),"identity":"COORD_PM598_DEL_3_5_6_C580_OWN222","event":1348,"journalAt":"2026-09-15T17:00:59.656Z","sourceFiles":1,"sourceBytes":len(source),"sourceSha256":sha(source),"dependencies":{"core":str(core),"pm598Recovery":str(parent/"PM598_RECOVER.py"),"requiredParentAudit":{"bytes":504653,"sha256":"d01383b4720b9615d019f4a229429b97a57f16755998b305033b5ff3506b2752","state":"Not materialized here; complete already preserved PM598 driver regenerates it from pinned C598 raw input"}},"completeRecoveryPreservedLocally":True,"localMathematicalOrNumericalReplay":False,"claimedBody":{"V":161,"E":290,"F":131,"C":580,"own":[2,2,2],"weak":[0,0,0],"commonCentredDenominatorBits":91696},"scope":"Three literal PM598 rawlex deletions3,5,6 plus21explicit supporting triples; author exactA/B/thirdmass and full driver cold replay reported. Not a Gomboc. Distinct from earlier unrealized C580 combinatorial proposal. Full64case discovery screen source/outcomes still pending."}
write("integrity-receipt.json",(json.dumps(receipt,indent=2)+"\n").encode())
print(json.dumps(receipt))
