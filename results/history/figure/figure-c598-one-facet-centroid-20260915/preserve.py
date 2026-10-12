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
    write(root/"archived-handoff.md",origin.encode())
    write(root/"recover_original.py",decoder.encode())
    receipt={"at":datetime.now(timezone.utc).isoformat(),"sourceFiles":len(sources),"capsuleBytes":len(encoded),"capsuleSha256":sha(encoded.encode()),"decodedBytes":len(data),"decodedSha256":sha(data),"sourceManifestPinsVerified":len(sources)-1,"localMathematicalOrNumericalReplay":False,"verification":"Exact canonical spans, complete payload/map/manifest pins, JSON/Python syntax and byte readbacks; original code not executed",**extra,"files":files}
    write(root/"integrity-receipt.json",(json.dumps(receipt,indent=2)+"\n").encode())
    print(json.dumps({k:v for k,v in receipt.items() if k!="files"}))


journal=JOURNAL.read_text();chunks=[]
for section in journal.split("### Unreviewed coordinator output (archived evidence)")[1:]:
    m=re.search(r"Source SHA-256: ([0-9a-f]+);.*?part: (\d+)/(\d+)",section)
    if not m or m.group(1)!="1e8d1af814f49f5e53263b9691fdd51852b642d6637617addd82e91db339d9a4":continue
    literal=section.split("The JSON string below preserves this portion exactly; concatenate decoded parts in order.\n\n",1)[1].split("\n\n## ",1)[0].strip()
    if m.group(3)!="6":raise ValueError("Archive count")
    chunks.append((int(m.group(2)),json.loads(literal)))
if [n for n,_ in chunks]!=list(range(1,7)):raise ValueError("Archive order")
raw="".join(t for _,t in chunks)
if sha(raw.encode())!="1e8d1af814f49f5e53263b9691fdd51852b642d6637617addd82e91db339d9a4":raise ValueError("Archive pin")
v=json.loads(raw);md=v["handoff_markdown"]
if set(v)!={"version","handoff_markdown"} or v["version"]!=1 or sha(md.encode())!="1378861cc19adcea523ae50c160dbb474d6801a2784baa311c158426a9923281":raise ValueError("Handoff pin")
payloads=re.findall("^"+tick+r"b85\n(.*?)^"+tick,md,re.M|re.S)
expected_parts=[(8000,"cecbdf88531f264e99ce0685ebc6446db7a8a087a6b6d97614ffb573d9321d9d"),(8000,"9ff25aef6181ef9ba8695111b50d63b37691bf0432fa1872bc36d9766e32a5ca"),(2505,"664169ec048a3cb6dc7b9600ada36c2224d1f25d1d1d2db94375c2d7040a37c6")]
if len(payloads)!=3:raise ValueError("Capsule parts")
for p,(n,pin) in zip(payloads,expected_parts):
    s="".join(p.split())
    if len(s)!=n or sha(s.encode())!=pin:raise ValueError("Capsule part pin")
encoded,data,sources=capsule("".join(payloads),18505,"4d1641e75f5203290850778adade56a2e69fe594d04a76860e3c39a9ba4e2590",46051,"1370cbde8a0dcfc72a736edbcd7c25cf0b9864749442ffa3a5eb4cb2c3a72872",9)
expect=json.loads(sources["EXPECTED.json"]);manifest=expect["sources"]
if set(manifest)!=set(sources)-{"EXPECTED.json"}:raise ValueError("Source manifest coverage")
for name,text in sources.items():
    if Path(name).name!=name or "\\" in name:raise ValueError("Unsafe source path")
    if name.endswith(".py"):ast.parse(text,filename=name)
    if name.endswith(".json"):json.loads(text)
    if name in manifest:
        b=text.encode();pin=manifest[name]
        if len(b)!=pin["bytes"] or sha(b)!=pin["sha256"]:raise ValueError("Source pin")
for name,pin in expect["core_sources"].items():
    b=(CORE/"source"/name).read_bytes()
    if len(b)!=pin["bytes"] or sha(b)!=pin["sha256"]:raise ValueError("Core input pin")
parent=BASE/"figure-c598-junction-endpoint-20260915"
parent_receipt=json.loads((parent/"integrity-receipt.json").read_text())
for name,pin in parent_receipt["files"].items():
    b=(parent/"source"/name).read_bytes()
    if len(b)!=pin["bytes"] or sha(b)!=pin["sha256"]:raise ValueError("Parent recovery source pin")
decoder=block(md,"python");ast.parse(decoder)
if len(decoder.encode())!=881 or sha(decoder.encode())!="164a08f1c5772f60e55a5d9155e28dfd97bdd96a0ddc551521738948ee92b9d1":raise ValueError("Decoder pin")
write(ROOT/"archived-handoff.json",raw.encode())
preserve(ROOT,sources,encoded,data,md,decoder,{"identity":"C598_ONE_FACET_CENTROID_PATCH","sourceChat":"6aa9667e-451c-83eb-9007-fdc0e643b5d3","sourceMessage":"3f9d9d25-c3af-47cc-99be-065aa9aea8d3","archivedAt":"2026-09-15T16:16:03.060Z","archiveSha256":sha(raw.encode()),"handoffSha256":sha(md.encode()),"standalone":False,"dependencies":{"core":str(CORE/"source"),"coreInputPins":len(expect["core_sources"]),"parentRecovery":str(parent/"source"),"parentSourceFiles":9,"c598RawExpected":expect["c598_raw"]},"completeRecoveryPreservedLocally":True,"scope":"Archived author proof: unique active cut moving onlysupport114 restores prescribed oldC602centroid, and hasatleast2stablewitnesses. NotglobalGombocminimum. Two rationalnonwinnersC612/C664; exact-centre isolatedcut isnotidentifiedwithnearbyrationalC664checkpoint.","bodyClaims":[{"C":612,"V":171,"E":306,"F":137,"own":[18,33,49],"weak":[0,0,0],"commonCentredDenominatorBits":79409},{"C":664,"V":201,"E":332,"F":133,"own":[5,6,9],"weak":[0,0,0],"commonCentredDenominatorBits":94807}]})
