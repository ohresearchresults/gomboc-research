import ast,hashlib,json,subprocess,sys,time
from datetime import datetime,timezone
from fractions import Fraction as F
from math import lcm
from pathlib import Path
ROOT=Path(__file__).resolve().parent
FULL=ROOT.parent/"figure-c622-route-20260915/source"
sha=lambda b:hashlib.sha256(b).hexdigest()
B=lambda x:json.dumps(x,sort_keys=True,separators=(",",":")).encode()
sources=json.loads((ROOT/"source-integrity-receipt.json").read_text())
for name,pin in sources["originalScripts"].items():
    b=(ROOT/name).read_bytes()
    if len(b)!=pin["bytes"]or sha(b)!=pin["sha256"]:raise ValueError("Original source mismatch")
ast.parse((ROOT/"POLAR_CENTROID_COUNTEREXAMPLE.py").read_bytes())
start=time.monotonic();results=[]
for tag,script,expected_hash,bits in [
 ("g10","RECOVER_G10.py","b397575230d5af70de7cf0743b150dd69257455b4ae5c9685c6992724563910d",46717),
 ("factor19","RECOVER_FACTOR19.py","9bf939cc259034e320ea0d662fb73dc7e429767ca343363262ab560fe2892774",45344)]:
    out=ROOT/("local-proof-"+tag)
    if out.exists():raise FileExistsError(out)
    print("START_LOCAL_"+tag.upper(),flush=True)
    subprocess.run([sys.executable,"-u","-B","-S",str(ROOT/script),str(FULL),str(ROOT/"parent-input"),str(out)],check=True)
    a=(out/"A.json").read_bytes();b=(out/"B.json").read_bytes()
    if a!=b or sha(a)!=expected_hash:raise ValueError("New exact A/B identity")
    report=json.loads(a);mass=json.loads((out/"MASS.json").read_text())
    if [report[k]for k in["V","E","F"]]!=[176,311,137]or report["counts"]!=[1,1,0]or report["weak"]!=[0,0,0]:raise ValueError("Endpoint classification")
    if mass["tetrahedra"]!=348 or mass["filled_first_moments"]!=[0,0,0]or mass["common_centred_denominator_bits"]!=bits:raise ValueError("Third mass result")
    sys.set_int_max_str_digits(0)
    p=[tuple(map(F,r))for r in report["raw_vertices"]];g=tuple(map(F,report["raw_centroid"]));d=lcm(*(v.denominator for r in p for v in r),*(v.denominator for v in g))
    if d.bit_length()!=bits:raise ValueError("Denominator reconstruction")
    outputs={n:{"bytes":len((out/n).read_bytes()),"sha256":sha((out/n).read_bytes())}for n in["GENERATOR.json","raw.json","A.json","B.json","MASS.json","RECEIPT.json"]}
    rec={"tag":tag,"completedAt":datetime.now(timezone.utc).isoformat(),"C":622,"V":176,"E":311,"F":137,"own":[1,1,0],"weak":[0,0,0],"commonCentredDenominatorBits":bits,"commonCentredDenominatorDecimalDigits":len(str(d)),"outputs":outputs}
    results.append(rec);print(json.dumps(rec),flush=True)
polar=ROOT/"local-polarity-report.json"
if polar.exists():raise FileExistsError(polar)
subprocess.run([sys.executable,"-B","-S",str(ROOT/"POLAR_CENTROID_COUNTEREXAMPLE.py"),str(polar)],check=True)
pdata=polar.read_bytes();pr=json.loads(pdata)
if pr["K_centroid"]!=["0","0","0"]or pr["polar_centroid"]!=["0","27/1120","0"]:raise ValueError("Polarity exact result")
receipt={"at":datetime.now(timezone.utc).isoformat(),"elapsedSeconds":round(time.monotonic()-start,3),"python":sys.version,"results":results,"polarity":{"bytes":len(pdata),"sha256":sha(pdata),"centroid":pr["K_centroid"],"polarCentroid":pr["polar_centroid"],"matchesDeclaredReport":len(pdata)==602 and sha(pdata)=="85daf6f3258a190c3e083c8e6cd7f2c1b63d5040ca5f1f1284a918ca7f0d8991"},"numericalScreensRerun":False,"fullTenCaseBatchRerun":False,"scope":"Fresh exact G10 andFactor19 A/B+thirdmass from verified G12 parent inputs; tiny exact polarity counterexample. No broader lower-bound proof or new edge record. Canonical documentation gaps are not silently modified."}
with(ROOT/"local-verification-receipt.json").open("x")as f:json.dump(receipt,f,indent=2)
print("LOCAL_C622_ARITHMETIC_COMPANIONS_AND_POLARITY_PASS",flush=True)
