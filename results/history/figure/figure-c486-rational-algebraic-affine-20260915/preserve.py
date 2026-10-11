import ast,base64,hashlib,json,re,zlib
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).parent;BASE=ROOT.parent
SNAP=BASE/"reconnect-figure-20260915-1551-OoOtnw/figure-heartbeat-1915.json"
entry=json.loads(SNAP.read_text())["journal"]["delta"]
sha=lambda b:hashlib.sha256(b).hexdigest()
payloads=["".join(b.split())for b in re.findall("^"+chr(96)*3+r"b85\n(.*?)^"+chr(96)*3,entry,re.M|re.S)]
if len(payloads)!=4:raise ValueError("Unexpected capsule spans")
def decode(enc,n,pin,size,data_pin,count):
    if len(enc)!=n or sha(enc.encode())!=pin:raise ValueError("Encoded source pin")
    data=zlib.decompress(base64.b85decode(enc))
    if len(data)!=size or sha(data)!=data_pin:raise ValueError("Decoded source pin")
    files=json.loads(data)
    if len(files)!=count:raise ValueError("Source file count")
    for name,text in files.items():
        p=Path(name)
        if p.is_absolute()or".."in p.parts or"\\"in name:raise ValueError("Unsafe source path")
        if name.endswith(".py"):ast.parse(text,filename=name)
        if name.endswith(".json"):json.loads(text)
    manifest=json.loads(files["MANIFEST.json"])if"MANIFEST.json"in files else{}
    if manifest:
        if set(manifest)!=set(files)-{"MANIFEST.json"}:raise ValueError("Manifest coverage")
        for name,spec in manifest.items():
            b=files[name].encode()
            if isinstance(spec,str):
                if sha(b)!=spec:raise ValueError("Source hash")
            elif len(b)!=spec["bytes"]or sha(b)!=spec["sha256"]:raise ValueError("Source byte/hash pin")
    return data,files,manifest
rdata,rfiles,rm=decode(payloads[0],4789,"8dc2c75d0693e77ce8f9111605e1bb9629d2ad217bd03e20a7b1e8811db404df",9117,"4e9465a537e3f9d19d1da9b44fd5f91317b206b50b9a77d89587a58d4e4e6c36",5)
for p,n,pin in [(payloads[1],7200,"2bcace8eff917f80c274b3fa2426d39be3388f82fe0c00289abdc06954d9ad66"),(payloads[2],7174,"c746ca828d29e3413633d61e2bac5114380463476cda64664245bb708105994c")]:
    if len(p)!=n or sha(p.encode())!=pin:raise ValueError("Algebraic part pin")
adata,afiles,am=decode(payloads[1]+payloads[2],14374,"719d9f2c5b9eb068bb3c7be9f0a987717397667ba17c0dd4c4815cdb9c9df1ff",29649,"57ca2d325f2ae5d50a0857321d32bfc71216977c6ddbd9cb33259ff973508f6d",8)
fdata,ffiles,fm=decode(payloads[3],2893,"e383723795821cab7ddd27f5d21b10a32208d081f8a3174893383f3eac801319",4878,"294769b003d462f1c076c49643ccb2cd4d45aa552717423c0016ad1fdeb3fd47",1)
assert list(ffiles)==["REPLAY_AFFINE334.py"]
assert len(ffiles["REPLAY_AFFINE334.py"].encode())==4783 and sha(ffiles["REPLAY_AFFINE334.py"].encode())=="ec205eccb50fd705f71703f4ac35fc4d6f5f0ee13ee871b512652b8e42d3a359"
assert rfiles["augment_exact.py"]==afiles["augment_exact.py"]
dependencies=[]
for folder,count,pin in [("figure-four-frontiers-core-20260915",16,"50061fcdfeb6cc42de880bfe1805441e4ed8cf3df4a2c78d6cbd9cf079496d19"),("figure-c592-exposed-chain-20260915",6,"57d0644b73858349341fad8f3f55fd83a00c4485efef5d0cdc49afb9b5a16320")]:
    root=BASE/folder;r=json.loads((root/"integrity-receipt.json").read_text())
    if r["sourceFiles"]!=count or r["decodedSha256"]!=pin:raise ValueError("Dependency identity")
    for name,spec in r["files"].items():
        b=(root/"source"/name).read_bytes()
        if len(b)!=spec["bytes"]or sha(b)!=spec["sha256"]:raise ValueError("Dependency bytes")
    dependencies.append({"directory":str(root/"source"),"files":count,"decodedSha256":pin})
def write(name,b):
    p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("xb")as f:f.write(b)
    if p.read_bytes()!=b:raise ValueError("Readback")
pins={}
for folder,files in [("rational",rfiles),("algebraic",afiles),("affine",ffiles)]:
    if (ROOT/folder).exists():raise FileExistsError("Package exists")
    for name,text in files.items():
        b=text.encode();key=folder+"/"+name;write(key,b);pins[key]={"bytes":len(b),"sha256":sha(b)}
for name,data in [("R12_CAPSULE.b85",payloads[0]),("MASS_PART1.b85",payloads[1]),("MASS_PART2.b85",payloads[2]),("AFFINE_CAPSULE.b85",payloads[3]),("canonical-entries.md",entry)]:write(name,data.encode())
decoder=re.findall("^"+chr(96)*3+r"python\n(.*?)^"+chr(96)*3,entry,re.M|re.S)
if len(decoder)!=1:raise ValueError("Mass decoder count")
ast.parse(decoder[0]);write("decode_mass_capsule_original.py",decoder[0].encode())
receipt={"at":datetime.now(timezone.utc).isoformat(),"sourceFiles":14,"uniqueSourceFileContents":len(set(v["sha256"]for v in pins.values())),"dependencies":dependencies,"rational":{"identity":"COORD_C592_OPPOSITE_POINT_R12","event":1380,"files":5,"manifestPins":len(rm),"decodedBytes":len(rdata),"decodedSha256":sha(rdata),"body":{"V":118,"E":243,"F":127,"C":486,"own":[7,2,7],"weak":[0,0,0]},"authorCombinedColdReplay":"Reported complete in1381"},"algebraic":{"identity":"COORD_C592_OPPOSITE_ALGEBRAIC_MASS_C486","events":[1381,1382,1383],"files":8,"manifestPins":len(am),"decodedBytes":len(adata),"decodedSha256":sha(adata),"body":{"V":118,"E":243,"F":127,"C":486,"own":[7,2,7],"weak":[0,0,0]},"authorCombinedColdReplay":"Reported complete in1383","scope":"Distinct isolated degree<=4 point; exactoldC602centroid; allfourrealquarticroots classified, exactlyoneinthis41facetvisibilitychamber, no globalall-chamber exclusion"},"affine":{"identity":"COORD_C486_PROJECTIVE_AFFINE_R12_OWN334","event":1385,"files":1,"manifestPins":0,"decodedBytes":len(fdata),"decodedSha256":sha(fdata),"body":{"V":118,"E":243,"F":127,"C":486,"own":[3,3,4],"weak":[0,0,0],"commonCentredDenominatorBits":63728},"authorCombinedColdReplay":"Pending in1385; warmfullA/B+thirdmass+bijection reported complete","scope":"RationalimageoftheR12body, notthealgebraicbody; trueedgecountunchanged but owncensusimproved"},"localMathematicalOrNumericalReplay":False,"verification":"All encoded/map/manifest pins, literal affine source pin, JSON/Python syntax,22upstreamdependencyfiles and exactoutputreadbacks checked. No sourceexecuted; scientificcountsandSturm/censusproof remainauthor evidence.","completeRecoveryPreservedLocally":True,"files":pins}
write("integrity-receipt.json",(json.dumps(receipt,indent=2)+"\n").encode())
print(json.dumps({k:v for k,v in receipt.items()if k!="files"}))
