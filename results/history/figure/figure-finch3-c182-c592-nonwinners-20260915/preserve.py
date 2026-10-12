import ast,base64,hashlib,json,lzma,re
from fractions import Fraction as F
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).parent
BASE=Path("/REDACTED_HOME/pro-research/output/reconnect-figure-20260915-1551-OoOtnw")
md=(BASE/"finch-completed-2001.md").read_text()
raw=(BASE/"finch-completed-2001.json").read_bytes()
sha=lambda b:hashlib.sha256(b).hexdigest()
code=re.findall("^"+chr(96)*3+r"python\n(.*?)^"+chr(96)*3,md,re.M|re.S)
if len(code)!=1:raise ValueError("Recovery source count")
tree=ast.parse(code[0]);values=[ast.literal_eval(n.value)for n in tree.body if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=="CAPSULE"for t in n.targets)]
if len(values)!=1:raise ValueError("Literal capsule count")
s="".join(values[0].split())
if len(s)!=59545 or sha(s.encode())!="776bd3a4fa0abe64ede23fde3078f938a7df8d58117e320df8504ce428c6bccc":raise ValueError("Capsule pin")
b=lzma.decompress(base64.b85decode(s))
if len(b)!=210036 or sha(b)!="0ba9975c3b9c374c8b2b51f6cba4c2ec0328752136a1e93813fb6dd20eb26ad6":raise ValueError("Source map pin")
p=json.loads(b);d=p["files"]
# Exact literal integer-delta/quantization recipe from the preserved recovery program.
for r in p["recipes"]:
    B=json.loads(d[r["base"]]);G=json.loads(d[r["base"]]);D=B["grid"]
    if "quantize"in r:
        G["grid"]=r["quantize"]
        G["controls"]=[[round(F(v*G["grid"],D))for v in row]for row in B["controls"]]
    else:
        for k in r["remove"]:G.pop(k)
        G.update(r["updates"])
        G["controls"]=[[round(F(B["controls"][k][j]*G["grid"],D))+v for j,v in enumerate(ds)]for k,*ds in r["deltas"]]
    d[r["name"]]=json.dumps(G,sort_keys=True,separators=(",",":"))
if len(d)!=44 or set(d)!=set(p["expected"]):raise ValueError("Source set mismatch")
for name,text in d.items():
    q=Path(name)
    if q.is_absolute()or".."in q.parts or"\\"in name:raise ValueError("Unsafe path")
    bb=text.encode();e=p["expected"][name]
    if len(bb)!=e["bytes"]or sha(bb)!=e["sha256"]:raise ValueError("Source pin "+name)
    if name.endswith(".py"):ast.parse(text,filename=name)
    if name.endswith(".json"):json.loads(text)
if(ROOT/"source").exists():raise FileExistsError("Sources already preserved")
def write(name,bb):
    path=ROOT/name;path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("xb")as f:f.write(bb)
    if path.read_bytes()!=bb:raise ValueError("Readback")
for name,text in d.items():write("source/"+name,text.encode())
write("backend-result.json",raw);write("result.md",md.encode());write("RECOVER_ORIGINAL.py",code[0].encode());write("SOURCE_CAPSULE.b85",s.encode())
receipt={"at":datetime.now(timezone.utc).isoformat(),"identity":"FINCH3_COUPLED_QUOTIENTS_AND_TWO_PLANE_MATERIAL_SURGERY","assignmentId":"asg_9_3jUNaB9fDmUrfQOxs-5B7l","sourceFinal":"513ce564-6f35-413b-81dc-7081b74d4e26","backendPayloadSha256":sha(raw),"sourceFiles":44,"sourcePinsChecked":len(p["expected"]),"capsuleChars":len(s),"capsuleSha256":sha(s.encode()),"decodedBytes":len(b),"decodedSha256":sha(b),"standalone":True,"completeRecoveryPreservedLocally":True,"localMathematicalOrNumericalReplay":False,"verification":"Literal capsule and encoded map pins, exact recorded delta/quantization restoration,all44originalbytepins,JSON/PythonAST and source readbacks; no scientific code executed","primaryClaims":[{"name":"C592_OWN222_GRID6","V":162,"E":296,"F":136,"C":592,"own":[2,2,2],"weak":[0,0,0],"denominatorBits":27013},{"name":"C450_TWO_PLANE222","V":135,"E":225,"F":92,"C":450,"own":[2,2,2],"weak":[0,0,0],"denominatorBits":26625},{"name":"C182_TWO_PLANE222","V":54,"E":91,"F":39,"C":182,"own":[2,2,2],"weak":[0,0,0],"denominatorBits":8853}],"scope":"TenauthorfullA/B+thirdmasscases,selectedcoldreplaysandnumericalproductionreported; allnonwinners. C592 distinctfrompreviouscoordinatorC592; C182's39activefacetsnot136inputinequalities. CurrentC622winnerrecordunchanged.","files":p["expected"]}
write("integrity-receipt.json",(json.dumps(receipt,indent=2)+"\n").encode())
print(json.dumps({k:v for k,v in receipt.items()if k!="files"}))
