import ast,hashlib,json,re,zipfile
from datetime import datetime,timezone
from fractions import Fraction as F
from math import gcd,lcm
from pathlib import Path
ROOT=Path(__file__).parent
BASE=ROOT.parent
SNAP=BASE/"reconnect-figure-20260915-1551-OoOtnw/figure-heartbeat-1652.json"
delta=json.loads(SNAP.read_text())["journal"]["delta"]
tick=chr(96)*3
blocks=re.findall("^"+tick+r"python\n(.*?)^"+tick,delta,re.M|re.S)
sha=lambda b:hashlib.sha256(b).hexdigest()
if len(blocks)!=1:raise ValueError("Ambiguous recovery source")
source=blocks[0];source_bytes=source.encode()
if len(source_bytes)!=3517 or sha(source_bytes)!="ce93a45eda31171f603d17133a5c8de885cbdb24d5c5ef63b62195d3874c3276":raise ValueError("Source pin")
ast.parse(source,filename="PM598_RECOVER.py")
parent=BASE/"figure-c598-one-facet-centroid-20260915/C598_raw.json"
raw=parent.read_bytes()
if len(raw)!=28264 or sha(raw)!="1286c05904d1aee57346b1bbeb200d8998b1656b0319d2cf56b2bfbb071c3599":raise ValueError("Parent pin")
core=BASE/"figure-four-frontiers-core-20260915/source"
core_receipt=json.loads((core.parent/"integrity-receipt.json").read_text())
dependencies={}
for name in ["check_A.py","check_B.py","centred_mass.py"]:
    bb=(core/name).read_bytes();pin=core_receipt["files"][name]
    if len(bb)!=pin["bytes"] or sha(bb)!=pin["sha256"]:raise ValueError("Core dependency pin")
    dependencies[name]=pin
D=10**12
bints=[231165476175,-287690514274,-722193871745]
lints=[[6195174799506,0,0],[-1419836775816,189361598103,0],[-4331762107070,485380338385,852421755373]]
b=tuple(F(v,D)for v in bints)
L=tuple(tuple(F(v,D)for v in row)for row in lints)
if not all(L[i][i]>0 for i in range(3)):raise ValueError("Singular affine map")
H=[]
for n0,n1,n2,d in json.loads(raw)["H"]:
    rhs=[F(n,d)+c for n,c in zip((n0,n1,n2),b)];z=[]
    for i in range(3):z.append((rhs[i]-sum(L[i][j]*z[j]for j in range(i)))/L[i][i])
    k=lcm(*(v.denominator for v in z));row=[int(v*k)for v in z]+[k];g=gcd(*row);row=[v//g for v in row]
    if row[3]<=0:raise ValueError("Bad primitive row")
    H.append(row)
if len(H)!=137 or len(set(map(tuple,H)))!=137:raise ValueError("Transformed support count")
transformed=json.dumps({"H":H},sort_keys=True,separators=(",",":")).encode()
if len(transformed)!=42455 or sha(transformed)!="df60591a327f8d36f1c1e66f7d7d4db48cf14433a3bb59e4bd9a668c88c79fcd":raise ValueError("Transformed H pin")
with zipfile.ZipFile(BASE/"figure-c598-one-facet-centroid-20260915/C598_ONE_FACET_VERIFIED_FULL.zip")as z:
    parent_a=z.read("proof/C598_A.json")
if len(parent_a)!=435251 or sha(parent_a)!="97e6687a0fd4a47515153da6efe8ed9168ea0e2b5ec603b2e1ef7c6b8bf230b9":raise ValueError("Parent audit data pin")
den=[]
for row in json.loads(parent_a)["raw_vertices"]:
    point=tuple(map(F,row));den.append(1+sum(x*y for x,y in zip(point,b)))
if len(den)!=164 or min(den)!=F(55561225651,200000000000) or min(den)<=0:raise ValueError("Projective denominator check")
def write(name,data):
    p=ROOT/name
    with p.open("xb")as f:f.write(data)
    if p.read_bytes()!=data:raise ValueError("Readback")
for n in ["PM598_RECOVER.py","raw.json","canonical-entries.md","parameters.json","integrity-receipt.json"]:
    if (ROOT/n).exists():raise FileExistsError("Already preserved")
write("PM598_RECOVER.py",source_bytes);write("raw.json",transformed);write("canonical-entries.md",delta.encode())
write("parameters.json",(json.dumps({"denominator":D,"b_numerators":bints,"L_numerators":lints,"map":"y=L^T*x/(1+b.x); defining body is then translated by its actual filled centroid","parent_raw":str(parent)},indent=2)+"\n").encode())
receipt={"at":datetime.now(timezone.utc).isoformat(),"identity":"COORD_C598_PROJECTIVE_METRIC_OWN334_G1E12","journalEvents":[1346,1347],"journalAt":"2026-09-15T16:48:11.005Z","sourceFiles":1,"sourceBytes":len(source_bytes),"sourceSha256":sha(source_bytes),"parentRaw":{"path":str(parent),"bytes":len(raw),"sha256":sha(raw)},"core":{"directory":str(core),"files":dependencies},"raw":{"file":"raw.json","bytes":len(transformed),"sha256":sha(transformed)},"localRationalTransformVerified":True,"localProjectiveDenominatorVerified":{"parentVertices":164,"minimum":[55561225651,200000000000]},"fullLocalGeometricOrEquilibriumAuditExecuted":False,"originalCombinedDriverExecutedByOperator":False,"combinedDriverAuthorColdReplay":"Pending in journal1347; uncombined complete cold run reported finished","claimedBody":{"V":164,"E":299,"F":137,"C":598,"own":[3,3,4],"weak":[0,0,0],"commonCentredDenominatorBits":92094},"verificationBoundary":"Pinned source/parent/core bytes, Python AST, independently calculated exact rational H transformation and positive projective denominators match published pins. The 3517-byte original driver was not run; whole-complex/own-census/mass tests remain author evidence.","completeRecoveryPreservedLocally":True}
write("integrity-receipt.json",(json.dumps(receipt,indent=2)+"\n").encode())
print(json.dumps(receipt))
