import hashlib,json,stat,zipfile
from datetime import datetime,timezone
from pathlib import Path,PurePosixPath
ROOT=Path(__file__).parent
sha=lambda b:hashlib.sha256(b).hexdigest()
e=json.loads((ROOT/"source/EXPECTED.json").read_text())
caps=(ROOT/"SOURCE_CAPSULE.b85").read_bytes()
decoder=(ROOT/"recover_original.py").read_bytes()
receipts=[]
for filename in ["C598_ONE_FACET_SOURCE_ONLY.zip","C598_ONE_FACET_VERIFIED_FULL.zip"]:
    with zipfile.ZipFile(ROOT/filename) as z:
        names=z.namelist()
        if len(names)!=len(set(names)):raise ValueError("Duplicate ZIP path")
        for i in z.infolist():
            p=PurePosixPath(i.filename)
            if p.is_absolute() or ".." in p.parts or "\\" in i.filename or stat.S_ISLNK(i.external_attr>>16) or i.file_size>20_000_000:raise ValueError("Unsafe ZIP")
        if z.testzip() is not None:raise ValueError("ZIP CRC")
        for name in (ROOT/"source").iterdir():
            if z.read("source/"+name.name)!=name.read_bytes():raise ValueError("Patch/source ZIP mismatch")
        for name,pin in e["core_sources"].items():
            b=z.read("core/"+name)
            if len(b)!=pin["bytes"] or sha(b)!=pin["sha256"]:raise ValueError("Core dependency ZIP pin")
        raw=z.read("C598_raw.json")
        if len(raw)!=e["c598_raw"]["bytes"] or sha(raw)!=e["c598_raw"]["sha256"]:raise ValueError("Raw input pin")
        if b"".join(z.read("ONE_FACET_PATCH.b85").split())!=caps or z.read("RECOVER_ONE_FACET.py")!=decoder:raise ValueError("Decoder/capsule ZIP mismatch")
        proof_names=[n for n in names if n.startswith("proof/") and not n.endswith("/")]
        verified_outputs=[]
        for name in proof_names:
            key=name.removeprefix("proof/")
            if key not in e["outputs"]:raise ValueError("Unpinned proof output")
            b=z.read(name);pin=e["outputs"][key]
            if len(b)!=pin["bytes"] or sha(b)!=pin["sha256"]:raise ValueError("Proof output pin")
            if name.endswith(".json"):json.loads(b)
            verified_outputs.append(key)
        if filename.endswith("VERIFIED_FULL.zip") and set(verified_outputs)!=set(e["outputs"]):raise ValueError("Missing proof outputs")
        receipts.append({"file":filename,"entries":len(names),"sourceFilesByteEqual":9,"coreDependencyPins":len(e["core_sources"]),"proofOutputPins":len(verified_outputs),"rawInputBytes":len(raw),"rawInputSha256":sha(raw),"note":"No archive-wide per-file manifest was supplied; full ZIP hash plus included EXPECTED source/core/output pins checked."})
raw_path=ROOT/"C598_raw.json"
if raw_path.exists():raise FileExistsError(raw_path)
with raw_path.open("xb") as f:f.write(raw)
if raw_path.read_bytes()!=raw:raise ValueError("Raw input readback")
receipt={"at":datetime.now(timezone.utc).isoformat(),"archives":receipts,"rawInputMaterialized":str(raw_path),"localMathematicalOrNumericalReplay":False,"verification":"Read-only archive CRC, fixed paths, literal source equality and original source/core/output pins; no source executed"}
with (ROOT/"archive-integrity-receipt.json").open("x") as f:json.dump(receipt,f,indent=2)
print(json.dumps(receipt))
