import ast,base64,hashlib,json,re,zlib
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).parent;BASE=ROOT.parent
SNAP=BASE/"reconnect-figure-20260915-1551-OoOtnw/figure-heartbeat-1956.json"
snapshot=json.loads(SNAP.read_text());entry=snapshot["journal"]["delta"]
sha=lambda b:hashlib.sha256(b).hexdigest()
parts=["".join(s.split())for s in re.findall("^"+chr(96)*3+r"b85\n(.*?)^"+chr(96)*3,entry,re.M|re.S)]
part_pins=[(3985,"5f39eee46e274f4bdf04e2863f69ce0c54ad6a0c90a3bad8669ef95dd5644cef"),(6000,"fe144ca2348feadeb430fa3fb5b95df5cb055f91c1ddae4a7a54b92e72262951"),(5245,"0f5b599bd6085ceaf8ea563479786166567cff47beb34ea37edfa1f8132dc5f5"),(4649,"f339b8dc8db699d26c41e0c54d2ddb648362254bb98b06122e32a7aaad71a984"),(7000,"1667051db41d89ca12606daadfd167d6cec87221b8854555d22bd65ce240f46f"),(6547,"8397a3f8fdd197b86ea107f57ef8d8a7ed79d6b0bb377d3f76d5655b4eb11f04")]
if len(parts)!=6:raise ValueError("Capsule part count")
for p,(n,h)in zip(parts,part_pins):
    if len(p)!=n or sha(p.encode())!=h:raise ValueError("Part pin")
specs=[
 ("deletion",parts[0],7554,"4d4c10f2c10ed04c2a3a220b175256725e7c964a7525d5be95844445775a0ca6",4),
 ("numerics5",parts[1]+parts[2],26991,"6dadf267a44460486f4866074a5a38e5828042ccb300a15eb644cb67d4da341f",8),
 ("slab",parts[3],7491,"3cec9e81bbe3ca723c9b54e9885fbe1efa63083b53787f4957a598bf8fa7a361",3),
 ("frontier6",parts[4]+parts[5],34902,"48510ea22862b63e83be7085b4a6cb031c10b5d90eb35a4a57b42fe43b70264b",10)]
decoded=[]
for name,payload,size,pin,count in specs:
    raw=zlib.decompress(base64.b85decode(payload))
    if len(raw)!=size or sha(raw)!=pin:raise ValueError("Map pin "+name)
    files=json.loads(raw)
    if len(files)!=count:raise ValueError("File count "+name)
    m=json.loads(files["MANIFEST.json"])
    if set(m)!=set(files)-{"MANIFEST.json"}:raise ValueError("Manifest coverage "+name)
    for file,text in files.items():
        p=Path(file)
        if p.is_absolute()or".."in p.parts or"\\"in file:raise ValueError("Unsafe file")
        if file.endswith(".py"):ast.parse(text,filename=file)
        if file.endswith(".json"):json.loads(text)
        if file in m:
            bb=text.encode();v=m[file]
            if isinstance(v,str):
                if sha(bb)!=v:raise ValueError("Source hash "+file)
            elif len(bb)!=v["bytes"]or sha(bb)!=v["sha256"]:raise ValueError("Source pin "+file)
    decoded.append((name,payload,raw,files,m))
dependencies=[]
for folder,prefix in [("figure-four-frontiers-core-20260915","source"),("figure-c592-exposed-chain-20260915","source"),("figure-c486-rational-algebraic-affine-20260915","")]:
    root=BASE/folder;r=json.loads((root/"integrity-receipt.json").read_text())
    for file,pin in r["files"].items():
        bb=(root/prefix/file).read_bytes()
        if len(bb)!=pin["bytes"]or sha(bb)!=pin["sha256"]:raise ValueError("Dependency pin")
    dependencies.append({"directory":str(root),"verifiedFiles":len(r["files"])})
for name,_,_,_,_ in decoded:
    if (ROOT/name).exists():raise FileExistsError("Package already saved")
def write(name,b):
    p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("xb")as f:f.write(b)
    if p.read_bytes()!=b:raise ValueError("Readback")
filepins={};capsules=[]
for name,payload,raw,files,m in decoded:
    for file,text in files.items():
        bb=text.encode();write(name+"/"+file,bb);filepins[name+"/"+file]={"bytes":len(bb),"sha256":sha(bb)}
    write(name+"/CAPSULE.b85",payload.encode())
    capsules.append({"name":name,"sourceFiles":len(files),"manifestPayloads":len(m),"encodedChars":len(payload),"encodedSha256":sha(payload.encode()),"decodedBytes":len(raw),"decodedSha256":sha(raw)})
write("canonical-entries.md",entry.encode())
receipt={"at":datetime.now(timezone.utc).isoformat(),"sourceFiles":25,"capsules":capsules,"dependencies":dependencies,"body":{"identity":"COORD_C476_AFFINE_DELETE42_63_83_OWN222","V":115,"E":238,"F":125,"C":476,"own":[2,2,2],"weak":[0,0,0],"originalR12DeletedVertexIds":[42,63,83]},"slabClaim":{"normal":[19,-98,-8],"normalSquared":10029,"diskRadius":"1/3","slabHalfHeight":"1/12","scope":"At least2strictstableequilibria for bodies containingthiscentraldiskandcontainedinthisslab abouttheirowncentre; notallC476 orallCbudgets"},"authorColdReplay":{"affineC486":"Reported completed at1386","C476":"Reported completed at1387","fiveNumericMethods":"Reported completed at1387","sixFrontierMethods":"Combined terminal pending at1392; original6executions completed"},"localMathematicalOrNumericalReplay":False,"completeSourceRecoveryPreserved":True,"verification":"All6parts,4decodedsource maps,21manifestpayloads,PythonAST/JSON and36existingdependencyfiles checked;25source entries byte-readback verified. No external scientificcode executed.","files":filepins}
write("integrity-receipt.json",(json.dumps(receipt,indent=2)+"\n").encode())
print(json.dumps({k:v for k,v in receipt.items()if k!="files"}))
