import ast,base64,hashlib,json,lzma,re
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).parent;BASE=ROOT.parent
HP=BASE/"reconnect-figure-20260915-1551-OoOtnw/coord-arithmetic-completed-1829-history.json"
SNAP=BASE/"reconnect-figure-20260915-1551-OoOtnw/figure-heartbeat-1829.json"
wrapper=json.loads(HP.read_text());messages=wrapper["history"]["messages"]
delta=json.loads(SNAP.read_text())["journal"]["delta"]
sha=lambda b:hashlib.sha256(b).hexdigest()
def text(m):
    c=m["content"]
    return c.get("text") if isinstance(c.get("text"),str) else "\n".join(x for x in c.get("parts",[])if isinstance(x,str))
byid={m["id"]:m for m in messages}
def heredoc(mid,path):
    s=text(byid[mid]);marker="cat > "+path+" <<'PY'\n"
    if s.count(marker)!=1:raise ValueError("Heredoc identity")
    return s.split(marker,1)[1].split("\nPY",1)[0]+"\n"
def write(name,data):
    p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("xb")as f:f.write(data)
    if p.read_bytes()!=data:raise ValueError("Readback")
def blocks(body,lang):return re.findall("^"+chr(96)*3+re.escape(lang)+r"\n(.*?)^"+chr(96)*3,body,re.M|re.S)
def unmap(encoded,length,pin,size,data_pin,count):
    if len(encoded)!=length or sha(encoded.encode())!=pin:raise ValueError("Capsule pin")
    data=lzma.decompress(base64.b85decode(encoded))
    if len(data)!=size or sha(data)!=data_pin:raise ValueError("Map pin")
    files=json.loads(data)
    if len(files)!=count:raise ValueError("Map count")
    manifest=json.loads(files["MANIFEST.json"])
    if set(manifest)!=set(files)-{"MANIFEST.json"}:raise ValueError("Manifest coverage")
    for name,s in files.items():
        p=Path(name)
        if p.is_absolute()or".."in p.parts or"\\"in name:raise ValueError("Unsafe source path")
        if name.endswith(".py"):ast.parse(s,filename=name)
        if name.endswith(".json"):json.loads(s)
        if name in manifest:
            b=s.encode();m=manifest[name]
            if len(b)!=m["bytes"]or sha(b)!=m["sha256"]:raise ValueError("Source pin")
    return data,files
# Exact original files from actual command/output carriers, never guessed replacements.
g10=heredoc("41d25e96-0e27-4a22-aaf3-2a93248cb21a","/mnt/data/c622_arithmetic/RECOVER_G10.py")
factor=text(byid["05c55c12-83f5-4d76-b3ba-1f6335fd507c"]).split("\n--- MASS ---",1)[0]
dec26=heredoc("97b7ff86-eb81-4b79-aa2b-e14da3cb586a","/mnt/data/c622_arithmetic/RECOVER_METHODS.py")
polar=heredoc("0d5bf876-1911-47f8-8f0f-4b6465beb2aa","/mnt/data/lower_bound_gate/POLAR_CENTROID_COUNTEREXAMPLE.py")
if len(g10.encode())!=2609:raise ValueError("G10 source length")
if len(factor.encode())!=2541 or sha(factor.encode())!="9a248c400aa99ee7d89b6ddf6fbbe81cc6befe12ae247a6453a301f86794eac1":raise ValueError("Factor19 original pin")
for s in [g10,factor,dec26,polar]:ast.parse(s)
# Recover the missing first26-file part from an actual tool output by full exact pins.
part2_sections=re.findall(r"^## Recovery capsule part 2/2 — COORD_C622_ARITHMETIC_METHODS_13GRID_2MIP_SVD40\n(.*?)(?=^## 2026-|\Z)",delta,re.M|re.S)
if len(part2_sections)!=1:raise ValueError("Methods part2 identity")
pp=blocks(part2_sections[0],"text")
if len(pp)!=1:raise ValueError("Methods part2 span")
p2="".join(pp[0].split())
if len(p2)!=8460 or sha(p2.encode())!="29fa3aeea9e39fcd63e9ded230d879d4f8bf404ba39f5356cb59383fee26b31f":raise ValueError("Part2 pin")
matches={}
for m in messages:
    if m["author"]["role"]!="tool":continue
    s=text(m)
    for hit in re.finditer(re.escape("{Wp48"),s):
        candidate="".join(s[hit.start():].split())[:8500]
        if len(candidate)==8500 and sha(candidate.encode())=="bfc511d13e061def6efcd1936012dedb67316f9ae03da5d8ea7495a6e20a7421":
            matches.setdefault(candidate,[]).append(m["id"])
if len(matches)!=1:raise ValueError("Missing/ambiguous original part1")
p1,carriers=next(iter(matches.items()))
encoded26=p1+p2
map26,files26=unmap(encoded26,16960,"d39b8bad6d29b22591c97c018132352a132d2c35c638f281869a82ec8a69b0fb",48930,"ef1a7d9b1b74103a8c57b91b813138a59964d467f8ca4314df15e8bf501ac444",26)
parts47=re.findall(r"^## Recovery capsule part ([12])/2 — COORD_C622_FACTORED42_SCREEN\n(.*?)(?=^## 2026-|\Z)",delta,re.M|re.S)
if [n for n,_ in parts47]!=["1","2"]:raise ValueError("Factored part identities")
codes47=[]
for n,body in parts47:
    b=blocks(body,"text")
    if len(b)!=1:raise ValueError("Factored payload span")
    codes47.append("".join(b[0].split()))
encoded47="".join(codes47)
map47,files47=unmap(encoded47,13450,"dc9db9eadd523ddae4b808302c52e012f8dae64f0cc5ae6b4b5e0d0315f8d8f4",42238,"f70e75bcd87255d3b3566200013d180a6cac129761e98ebb93e3864adcad944c",47)
# Original47-file decoder is a literal in the recorded builder; no builder execution.
builder=text(byid["040219cc-b03c-4a4c-b265-00704528113a"])
code=builder.split("<<'PY'\n",1)[1].rsplit("\nPY",1)[0]
values=[ast.literal_eval(n.value)for n in ast.walk(ast.parse(code))if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=="s"for t in n.targets)and isinstance(n.value,ast.Constant)and isinstance(n.value.value,str)]
dec47=next(v for v in values if "Recover the complete finite 42" in v)
# Reproduce only the literal placeholder replacements shown in the recorded builder.
for i,payload in enumerate(codes47,1):dec47=dec47.replace("PART"+str(i),sha(payload.encode()))
if len(dec47.encode())!=1556 or sha(dec47.encode())!="3f1acfcc09b9463b8b2d0b04661c873e21a0376553e578ff8296ef4c3333d18d":raise ValueError("Observed original47decoder pin")
if "DECODER 1556 3f1acfcc09b9463b8b2d0b04661c873e21a0376553e578ff8296ef4c3333d18d" not in text(messages[207]):raise ValueError("Missing decoder measurement carrier")
ast.parse(dec47)
originals={"RECOVER_G10.py":g10,"RECOVER_FACTOR19.py":factor,"RECOVER_METHODS.py":dec26,"POLAR_CENTROID_COUNTEREXAMPLE.py":polar,"RECOVER_FACTORED_SCREEN.py":dec47}
literal_blocks=blocks(delta,"python")
variants=[]
for s in literal_blocks:
    key=next((n for n in originals if n in s or(n=="POLAR_CENTROID_COUNTEREXAMPLE.py"and"centroid counterexample" in s)),None)
    if key:
        orig=originals[key];variants.append({"file":key,"journalBytes":len(s.encode()),"journalSha256":sha(s.encode()),"originalBytes":len(orig.encode()),"originalSha256":sha(orig.encode()),"equal":s==orig})
        write("journal-variants/"+key,s.encode())
for n,s in originals.items():write(n,s.encode())
file_pins={}
for folder,files in [("methods26",files26),("factored47",files47)]:
    for n,s in files.items():
        b=s.encode();write(folder+"/"+n,b);file_pins[folder+"/"+n]={"bytes":len(b),"sha256":sha(b)}
write("METHODS_PART_1.b85",p1.encode());write("METHODS_PART_2.b85",p2.encode())
for i,s in enumerate(codes47,1):write("FACTORED_PART_"+str(i)+".b85",s.encode())
# Required original parent input layout, not a claim of a full parent batch directory.
parent=BASE/"figure-c622-route-20260915/local-endpoint-proof"
for name,pin in [("GENERATOR.json","3cbd90d799189108f26b941800c8fa79a6f1c5abb17b2db614f0e54f57fffee7"),("A.json","142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0")]:
    b=(parent/name).read_bytes()
    if sha(b)!=pin:raise ValueError("Parent input pin")
    write("parent-input/C622_ROUTED/"+name,b)
receipt={"at":datetime.now(timezone.utc).isoformat(),"sourceChat":wrapper["receipt"]["sourceChat"],"historySha256":wrapper["receipt"]["historySha256"],"methods26":{"files":26,"manifestPins":25,"decodedBytes":len(map26),"decodedSha256":sha(map26),"missingCanonicalPart1RecoveredFromMessages":carriers,"part1Sha256":sha(p1.encode()),"part2Sha256":sha(p2.encode())},"factored47":{"files":47,"manifestPins":46,"decodedBytes":len(map47),"decodedSha256":sha(map47)},"originalScripts":{n:{"bytes":len(s.encode()),"sha256":sha(s.encode())}for n,s in originals.items()},"journalVariants":variants,"incorrectProsePins":{"RECOVER_METHODS.py":{"bytes":1562,"sha256":"09509a9ed67ba454535648fd1713c380faed11af0b103bf216735ad945f7f9f6"},"POLAR_CENTROID_COUNTEREXAMPLE.py":{"bytes":2729,"sha256":"4168fe59d97c6de33566e235c765e59a61c9d92cfb1b2b74d71aac7fc8ed72ef"},"RECOVER_FACTORED_SCREEN.py":{"bytes":1613,"sha256":"16a661fc264b6fe98d8b898f9d7d1e4af1621664a24c37e5d9d93bf708b31b18"}},"localMathReplayExecuted":False,"canonicalGaps":["GRID10 exact construction entry absent from actual journal","Arithmetic methods26 part1 absent from actual journal"],"scope":"Recovered literal originals and missing exact source part from owned completed-chat code/output carriers, verified source maps and manifests. Canonical files were not edited. Documentation/source mismatches remain explicit; mathematical verification has its own receipt.","files":file_pins}
write("source-integrity-receipt.json",(json.dumps(receipt,indent=2)+"\n").encode())
print(json.dumps({k:v for k,v in receipt.items()if k!="files"}))
