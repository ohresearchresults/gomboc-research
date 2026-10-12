import ast,hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).parent
BASE=ROOT.parent
entry=json.loads((BASE/"reconnect-figure-20260915-1551-OoOtnw/figure-heartbeat-2053.json").read_text())["journal"]["delta"]
code=re.findall("^"+chr(96)*3+r"python\n(.*?)^"+chr(96)*3,entry,re.M|re.S)
if len(code)!=2:raise ValueError("Unexpected source blocks")
sha=lambda b:hashlib.sha256(b).hexdigest()
if len(code[0].encode())!=3640 or sha(code[0].encode())!="27463970240605c6afbdbb739b8fb62e090d2f1beb98b2a60c5e9ed6c9f90c50":raise ValueError("Exact source pin")
for text in code:ast.parse(text)
parent=BASE/"figure-finch3-c182-c592-nonwinners-20260915"
receipt=json.loads((parent/"integrity-receipt.json").read_text())
for name,pin in receipt["files"].items():
    b=(parent/"source"/name).read_bytes()
    if len(b)!=pin["bytes"]or sha(b)!=pin["sha256"]:raise ValueError("Parent source pin")
def write(name,b):
    with(ROOT/name).open("xb")as f:f.write(b)
    if(ROOT/name).read_bytes()!=b:raise ValueError("Readback")
for n,b in [("check_shape.py",code[0].encode()),("c182_section_search.py",code[1].encode()),("canonical-entry.md",entry.encode())]:write(n,b)
r={"at":datetime.now(timezone.utc).isoformat(),"identity":"FINCH_C182_TWO_PLANE222_SECTION_CERTIFICATE","event":1412,"journalAt":"2026-09-15T20:43:37.741Z","sourceFiles":2,"files":{n:{"bytes":len(b),"sha256":sha(b)}for n,b in[("check_shape.py",code[0].encode()),("c182_section_search.py",code[1].encode())]},"dependency":{"directory":str(parent/"source"),"verifiedSourceFiles":44,"capsuleSha256":"776bd3a4fa0abe64ede23fde3078f938a7df8d58117e320df8504ce428c6bccc","canonicalBoundary":"Use original44sourcefiles alreadylocallypreserved/immutableparent. Six-partjournalcopyhasknownpart6corruption, notanintactdependencyuntilcorrected."},"authorExactCertificate":{"diskNormal":[8,3,0],"diskRadius":"31/400","slabHalfWidth":"7/400","segmentAxis":[-7,12,100],"segmentHalfLength":"363/1000","cylinderRadius":"121/1000","allSuppliedRows":136,"allVertices":54,"affineConditionBoundStable":"31/7","affineConditionBoundUnstable":"3","reportBytes":1163,"reportSha256":"2b42ab3272257aa104fbb33619e7dd90b7321755a18b019610a7e42d5c10da83"},"localMathematicalOrNumericalReplay":False,"scope":"Authorexactshapeinclusionsandproof forliteralC182own222; excludes onlyaffineimageswithspecifiedcondition-numberbounds. Notentireaffineorbit,non-affineredesignorallC182bodies/globalminimum.","numericalSourceBoundary":"Exactliteral1317bytediscoveryprogramretained withitsabsolute/mnt/data/c182 inputs. Inputsreconstructiblefromthe44-sourceparent; no seed orcross-platformnumericreplicationguarantee invented. Numericaldirectionsarenotglobaloptima.","verification":"Exactcheckerpin, bothPythonASTs, all44parentbytepins and written source/readbacks. No scientific code executed.","completeRecoveryPreservedLocally":True}
write("integrity-receipt.json",(json.dumps(r,indent=2)+"\n").encode())
print(json.dumps(r))
