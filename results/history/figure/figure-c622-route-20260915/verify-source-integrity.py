import ast,base64,hashlib,json,lzma,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).parent
sha=lambda b:hashlib.sha256(b).hexdigest()
B=lambda x:json.dumps(x,sort_keys=True,separators=(",",":")).encode()
prog=(ROOT/"VQ20_C622_RECOVER.py").read_bytes()
if len(prog)!=90523 or sha(prog)!="7a5303c972ed90f1563add95829c4c6c2d23be78d9e6e3a17739f526081e75dd":raise ValueError("Program pin")
tree=ast.parse(prog);values=[ast.literal_eval(n.value)for n in tree.body if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=="CAPSULE"for t in n.targets)]
if len(values)!=1:raise ValueError("Ambiguous capsule")
encoded="".join(values[0].split())
if len(encoded)!=88685 or sha(encoded.encode())!="56bb46a476d35128b4743224c5f015d13f38d99d50e319f9bef871878350cd94":raise ValueError("Capsule pin")
data=lzma.decompress(base64.b85decode(encoded))
if len(data)!=312622 or sha(data)!="617f94b82a54bf54cd7cce67fbf5d506cc3d2b9431a7c64b587984ea429992f6":raise ValueError("Map pin")
files=json.loads(data)
if len(files)!=76:raise ValueError("Source count")
manifest=json.loads(files["MANIFEST.json"])
if sha(files["MANIFEST.json"].encode())!="d06bc3d5782b4ebf2449b4bd89e962ce88f08faca9d06ae068a5bfaf22af0c53":raise ValueError("Manifest pin")
if set(manifest)!=set(files)-{"MANIFEST.json"}:raise ValueError("Manifest coverage")
pins={}
for name,text in files.items():
    p=Path(name)
    if p.is_absolute()or".."in p.parts or "\\"in name:raise ValueError("Unsafe path")
    b=text.encode()
    if name in manifest and sha(b)!=manifest[name]:raise ValueError("File pin")
    if name.endswith(".json"):json.loads(b)
    if name.endswith(".py"):ast.parse(b,filename=name)
    if (ROOT/"source"/name).read_bytes()!=b:raise ValueError("Restored source mismatch")
    pins[name]={"bytes":len(b),"sha256":sha(b)}
sys.path.insert(0,str(ROOT/"source/methods"))
import G_FREE_CODEC
expected=json.loads(files["EXPECTED.json"])
generators={}
for name,want in expected["cases"].items():
    g=G_FREE_CODEC.decode(json.loads(files["inputs/"+name+".json"]));b=B(g)
    if sha(b)!=want["generator_sha256"]:raise ValueError("Restored generator pin")
    generators[name]={"bytes":len(b),"sha256":sha(b),"claimedVEF":want["VEF"],"claimedCounts":want["counts"]}
    if name=="C622_ROUTED"and b!=(ROOT/"GENERATOR.json").read_bytes():raise ValueError("Downloaded endpoint generator mismatch")
a=(ROOT/"ENDPOINT_A.json").read_bytes();b=(ROOT/"ENDPOINT_B.json").read_bytes()
if a!=b or len(a)!=311825 or sha(a)!="142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0":raise ValueError("Author audit pin")
r=json.loads(a)
if [r[k]for k in["V","E","F"]]!=[176,311,137]or r["counts"]!=[1,1,0]or r["weak"]!=[0,0,0]:raise ValueError("Author endpoint record mismatch")
receipt={"at":datetime.now(timezone.utc).isoformat(),"identity":"VQ20_C622_ROUTE88_118_G12","sourceFiles":76,"manifestPayloads":len(manifest),"capsuleChars":len(encoded),"capsuleSha256":sha(encoded.encode()),"decodedBytes":len(data),"decodedSha256":sha(data),"programBytes":len(prog),"programSha256":sha(prog),"sourceManifestSha256":sha(files["MANIFEST.json"].encode()),"standalone":True,"completeSourcePreservedLocally":True,"literalHandoffGapResolvedLocally":True,"authorEndpointReports":{"bytes":len(a),"sha256":sha(a),"V":176,"E":311,"F":137,"C":622,"own":[1,1,0],"weak":[0,0,0]},"generatorCases":generators,"fullTenCaseAuditBatchCompleted":False,"verificationBoundary":"All76literal files,75manifest pins,program/payload/map pins,JSON/Python syntax and restored-byte equality verified. All10original generator byte identities decoded. Author endpoint A/B downloads match. Separate local endpoint verification receipt, if completed, is authoritative for rerun status; no full ten-case aggregate claim.","files":pins}
with(ROOT/"source-integrity-receipt.json").open("x")as f:json.dump(receipt,f,indent=2)
print(json.dumps({k:v for k,v in receipt.items()if k!="files"}))
