"""Preserve a literal bounded source capsule without executing research code."""
import ast
import base64
from datetime import datetime, timezone
import hashlib
import json
import lzma
from pathlib import Path, PurePosixPath
import re

root = Path(__file__).resolve().parent
def sha(data):
    return hashlib.sha256(data).hexdigest()
def check(data, size, digest):
    if len(data) != size or sha(data) != digest:
        raise ValueError("Source integrity mismatch")
    return data
raw = check((root / "result.json").read_bytes(), 61554, "c5ea8fda8761454dd25eacd0b1140dd5c53332e513b4b4c09f64617ad11f33d3")
md = json.loads(raw)["result_markdown"]
if (root / "result.md").read_bytes() != md.encode("utf-8"):
    raise ValueError("Result markdown differs from immutable JSON")
start, end = "\nNH72_PM_B64_BEGIN\n", "\nNH72_PM_B64_END"
if md.count(start) != 1 or md.count(end) != 1:
    raise ValueError("Ambiguous source markers")
capsule = check("".join(md.split(start)[1].split(end)[0].split()).encode("ascii"), 36464, "d06b4813e87a33dc14ed53897732882781874b3c22da71fe8ed9fbb2c36d395a")
decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
decoded = decoder.decompress(base64.b64decode(capsule, validate=True), max_length=83136)
if not decoder.eof or decoder.unused_data:
    raise ValueError("Unexpected compressed extent")
check(decoded, 83135, "c3e1c908a17fb25744fb37323df081ec2d61cfc2b556489c341c8b94dc9a8017")
files = json.loads(decoded)
if not isinstance(files, dict) or len(files) != 23:
    raise ValueError("Unexpected source count")
for name, text in files.items():
    rel = PurePosixPath(name)
    if not isinstance(text, str) or not rel.parts or rel.is_absolute() or ".." in rel.parts or "\\" in name or str(rel) != name:
        raise ValueError("Unsafe source path")
    if name.endswith(".py"):
        ast.parse(text, filename=name)
manifest = json.loads(files["MANIFEST.json"])
if set(manifest) != set(files) - {"MANIFEST.json"}:
    raise ValueError("Incomplete manifest coverage")
for name, spec in manifest.items():
    check(files[name].encode("utf-8"), spec["bytes"], spec["sha256"])
restore = re.findall(r"^```python\n(.*?)^```\s*$", md, re.M | re.S)
if len(restore) != 1 or len(restore[0].encode("utf-8")) != 974:
    raise ValueError("Unexpected original restoration program")
ast.parse(restore[0])
payloads = {"source/" + name: text.encode("utf-8") for name, text in files.items()}
payloads.update({"restore.py": restore[0].encode("utf-8"), "SOURCE_CAPSULE.b64": capsule})
for name in payloads:
    if (root / name).exists():
        raise FileExistsError(root / name)
for name, data in payloads.items():
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)
    check(path.read_bytes(), len(data), sha(data))
receipt = {"at": datetime.now(timezone.utc).isoformat(), "sourceFiles": 23,
    "exactSourcePreservedLocally": True, "localMathematicalOrNumericalReplay": False,
    "verification": "Immutable result hash; base64 and decoded byte/hash pins; all22 manifest hashes; Python AST checks and byte-exact file readback passed. Original restore.py preserved but not run because it launches a mathematical replay.",
    "scope": "Two own222/weak000 C624 projective-metric nonwinners, complete exact audit and physical centroid/basin reconstruction, analytic centroid-map method, numerical search code and saved finite inputs.",
    "limitations": "Author reports exact audits and cold replay; monitor did not independently repeat them or prove theorem novelty. The result's C626 incumbent sentence is stale: current accepted incumbent is C624. Optional full sandbox ZIP not downloaded.",
    "files": {name: {"bytes": len(data), "sha256": sha(data)} for name, data in payloads.items()}}
with (root / "integrity-receipt.json").open("x", encoding="utf-8") as stream:
    json.dump(receipt, stream, indent=2)
    stream.write("\n")
print(json.dumps({"status": "NH72_SOURCE_INTEGRITY_PASS", "sourceFiles": len(files), "names": list(files), "localReplay": False}))
