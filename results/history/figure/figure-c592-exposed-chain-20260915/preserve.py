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

journal=JOURNAL.read_text()
parts=re.findall(r"^## Recovery capsule part ([123])/3 — FOUR_FRONTIERS_EXACT_CORE_20260915\n(.*?)(?=^## \d{4}-|\Z)",journal,re.M|re.S)
if len(parts)!=3 or [n for n,_ in parts]!=["1","2","3"]:raise ValueError("Core part identity")
expected=[(9000,"88cff44e5a41e7c22f598f95c30931dbb1e5e82d07591c88b775d51153c3de40"),(9000,"8e48a54bcc1064dc48e4104575541d68db4acd8f779f8fa936e8da6e44ed1480"),(7865,"e725a89e0390cfd54c35fa45463a57862372871fcdca4d1ad2202febccee2651")]
payloads=[]
for (_,body),(n,pin) in zip(parts,expected):
    s="".join(block(body,"b85").split())
    if len(s)!=n or sha(s.encode())!=pin:raise ValueError("Core part pin")
    payloads.append(s)
cs,cb,cf=capsule("".join(payloads),25865,"ec0ad716235628338a7c3c6d371de170e30bd6184ae039c9b13eff096984c929",71405,"50061fcdfeb6cc42de880bfe1805441e4ed8cf3df4a2c78d6cbd9cf079496d19",16)
verify(cf,"CORE_MANIFEST.json")
core_decoder=block(parts[0][1],"python")
if len(core_decoder.encode())!=818 or sha(core_decoder.encode())!="169643b049eda7a23db0692610b483c6c4bb6018131da66fcf3fe78513b148e4":raise ValueError("Core decoder pin")
delta=json.loads(SNAPSHOT.read_text())["journal"]["delta"]
sections=re.findall(r"^## Recovery capsule 1/1 — COORD_C602_EXPOSED_CHAIN5_G1E12: exact C592 exposed-chain nonwinner\n(.*?)(?=^## \d{4}-|\Z)",delta,re.M|re.S)
if len(sections)!=1:raise ValueError("C592 identity")
body=sections[0]
ss,sb,sf=capsule(block(body,"b85"),7095,"f9ee5fc1060be31f8694da3c1bab3ef93c24ee992f2a2149db65a2ebce758c26",15925,"57d0644b73858349341fad8f3f55fd83a00c4485efef5d0cdc49afb9b5a16320",6)
verify(sf,"MANIFEST.json")
decoder=block(body,"python");ast.parse(decoder)
if (CORE/"source").exists() or (ROOT/"source").exists():raise FileExistsError("Do not duplicate preserved sources")
preserve(CORE,cf,cs,cb,"\n".join("## Recovery capsule part "+n+"/3 — FOUR_FRONTIERS_EXACT_CORE_20260915\n"+b for n,b in parts),core_decoder,{"identity":"FOUR_FRONTIERS_EXACT_CORE_20260915","standalone":True,"journalEvents":[1317,1318,1319],"scope":"Four previously reported exact bodies only; not all numerical/discovery/nonwinner histories"})
preserve(ROOT,sf,ss,sb,"## Recovery capsule 1/1 — COORD_C602_EXPOSED_CHAIN5_G1E12: exact C592 exposed-chain nonwinner\n"+body,decoder,{"identity":"COORD_C602_EXPOSED_CHAIN5_G1E12","journalEvent":1325,"journalAt":"2026-09-15T15:13:05.937Z","standalone":False,"dependency":{"directory":str(CORE/"source"),"files":16,"capsuleSha256":sha(cs.encode()),"decodedSha256":sha(cb)},"completeRecoveryPreservedLocally":True,"body":{"V":163,"E":296,"F":135,"C":592,"own":[17,26,41],"reference":[5,1,4],"weak":[0,0,0],"commonCentredDenominatorBits":80232},"scope":"Author-reported exact exposed five-link hull; neither own110 nor reference110; lower complexity does not improve accepted C624 winner"})
