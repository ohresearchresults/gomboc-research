import ast, base64, hashlib, json, lzma, re
from datetime import datetime, timezone
from pathlib import Path
BASE=Path("/REDACTED_HOME/pro-research/output")
ROOT=Path(__file__).parent
CORE=BASE/"figure-four-frontiers-core-20260915"
JOURNAL=Path("/REDACTED_HOME/.pro-research/runs/run_-kjrDuYVMzeTQ9tyWn464e75/research-journal.md")
SNAPSHOT=BASE/"reconnect-figure-20260915-1423-nE7XkU/figure-heartbeat-1519.json"
sha=lambda b:hashlib.sha256(b).hexdigest()
tick=chr(96)*3
def block(text,lang):
    found=re.findall("^"+tick+re.escape(lang)+r"\n(.*?)^"+tick,text,re.M|re.S)
    if len(found)!=1:raise ValueError("Ambiguous "+lang+" source")
    return found[0]
def capsule(encoded,n,code_hash,size,data_hash,count):
    s="".join(encoded.split())
    if len(s)!=n or sha(s.encode())!=code_hash:raise ValueError("Encoded capsule pin")
    data=lzma.decompress(base64.b85decode(s))
    if len(data)!=size or sha(data)!=data_hash:raise ValueError("Decoded capsule pin")
    sources=json.loads(data)
    if len(sources)!=count:raise ValueError("Source count")
    return s,data,sources
def verify(sources,manifest_name):
    manifest=json.loads(sources[manifest_name])
    if set(manifest)!=set(sources)-{manifest_name}:raise ValueError("Manifest coverage")
    for name,text in sources.items():
        if Path(name).name!=name or "\\" in name or name in (".",".."):raise ValueError("Unsafe source path")
        if name.endswith(".py"):ast.parse(text,filename=name)
        if name.endswith(".json"):json.loads(text)
        if name in manifest:
            data=text.encode();m=manifest[name]
            if len(data)!=m["bytes"] or sha(data)!=m["sha256"]:raise ValueError("Source pin "+name)
    return manifest
def write(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("xb") as f:f.write(data)
    if path.read_bytes()!=data:raise ValueError("Readback failed")
def preserve(root,sources,encoded,data,origin,decoder,extra):
    if (root/"source").exists() or (root/"integrity-receipt.json").exists():raise FileExistsError("Existing preserved package")
    files={}
    for name,text in sources.items():
        b=text.encode();write(root/"source"/name,b);files[name]={"bytes":len(b),"sha256":sha(b)}
    write(root/"SOURCE_CAPSULE.b85",encoded.encode())
    write(root/"canonical-source.md",origin.encode())
    write(root/"recover_original.py",decoder.encode())
    receipt={"at":datetime.now(timezone.utc).isoformat(),"sourceFiles":len(sources),"capsuleBytes":len(encoded),"capsuleSha256":sha(encoded.encode()),"decodedBytes":len(data),"decodedSha256":sha(data),"sourceManifestPinsVerified":len(sources)-1,"localMathematicalOrNumericalReplay":False,"verification":"Exact canonical spans, complete payload/map/manifest pins, JSON/Python syntax and byte readbacks; original code not executed",**extra,"files":files}
    write(root/"integrity-receipt.json",(json.dumps(receipt,indent=2)+"\n").encode())
    print(json.dumps({k:v for k,v in receipt.items() if k!="files"}))


snapshot=BASE/"reconnect-figure-20260915-1423-nE7XkU/figure-heartbeat-1536.json"
delta=json.loads(snapshot.read_text())["journal"]["delta"]
sections=re.findall(r"^## Recovery capsule 1/1 — C598_JUNCTION91_AND_ALL_OLD_ENDPOINT_BOUND\n(.*?)(?=^## \d{4}-|\Z)",delta,re.M|re.S)
if len(sections)!=1:raise ValueError("C598 entry identity")
origin=sections[0]
encoded,data,sources=capsule(block(origin,"b85"),12685,"26908efcc8c8e339049eb136153ab50b65ee408ebc6e5d2520ebc150ec1356d2",30459,"31504bae5b7e5e19949e7657b05d385fbae1ed2ed4549019819d40045c57f2ee",9)
verify(sources,"SOURCE_MANIFEST.json")
decoder=block(origin,"python");ast.parse(decoder)
core_receipt=json.loads((CORE/"integrity-receipt.json").read_text())
if core_receipt["sourceFiles"]!=16 or core_receipt["decodedSha256"]!="50061fcdfeb6cc42de880bfe1805441e4ed8cf3df4a2c78d6cbd9cf079496d19":raise ValueError("Dependency identity")
for name,pin in core_receipt["files"].items():
    b=(CORE/"source"/name).read_bytes()
    if len(b)!=pin["bytes"] or sha(b)!=pin["sha256"]:raise ValueError("Dependency pin")
preserve(ROOT,sources,encoded,data,"## Recovery capsule 1/1 — C598_JUNCTION91_AND_ALL_OLD_ENDPOINT_BOUND\n"+origin,decoder,{"identity":"C598_JUNCTION91_AND_ALL_OLD_ENDPOINT_BOUND","bodyIdentity":"COORD_C602_TO91_CHAIN6_G1E12","journalEvent":1329,"journalAt":"2026-09-15T15:33:50.633Z","standalone":False,"dependency":{"directory":str(CORE/"source"),"files":16,"capsuleSha256":core_receipt["capsuleSha256"],"decodedSha256":core_receipt["decodedSha256"]},"completeRecoveryPreservedLocally":True,"body":{"V":164,"E":299,"F":137,"C":598,"own":[19,27,44],"reference":[3,1,2],"weak":[0,0,0],"commonCentredDenominatorBits":80232},"scope":"Exact author-reported C598 nonwinner; twelve numerical discovery cases, only C592/C598 fully audited; all unchanged-old-endpoint five-link bound is limited to frozen old geometry and old centroid, not actual new mass/affine changes/global C","decoderBytes":len(decoder.encode()),"decoderSha256":sha(decoder.encode())})
