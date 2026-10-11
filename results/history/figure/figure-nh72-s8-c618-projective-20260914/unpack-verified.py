"""Preserve a bounded literal source capsule without executing research code."""
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
raw = check((root / "result.json").read_bytes(), 73144, "c00d707b68ac1ed80be88960dad668969b21b25ef57afbd02f4bef9d22299ffb")
md = json.loads(raw)["result_markdown"]
if (root / "result.md").read_bytes() != md.encode("utf-8"):
    raise ValueError("Result markdown differs from immutable JSON")
start, end = "\nNH72_S8_B64_BEGIN\n", "\nNH72_S8_B64_END"
if md.count(start) != 1 or md.count(end) != 1:
    raise ValueError("Ambiguous source markers")
capsule = check("".join(md.split(start)[1].split(end)[0].split()).encode("ascii"), 44392, "90696271f17317024576b1d7b5ad4e9f094ed1577188abe28f4080e1c4263962")
decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
decoded = decoder.decompress(base64.b64decode(capsule, validate=True), max_length=118589)
if not decoder.eof or decoder.unused_data:
    raise ValueError("Unexpected compressed extent")
check(decoded, 118588, "3ac9a8a2ab883259d9e40753b5d48ba8ce544450d161ebbed5a85cd83a76fe53")
files = json.loads(decoded)
if not isinstance(files, dict) or len(files) != 28:
    raise ValueError("Unexpected source count")
for name, value in files.items():
    rel = PurePosixPath(name)
    if not isinstance(value, str) or not rel.parts or rel.is_absolute() or ".." in rel.parts or "\\" in name or str(rel) != name:
        raise ValueError("Unsafe source path")
    if name.endswith(".py"):
        ast.parse(value, filename=name)
manifest = json.loads(files["MANIFEST.json"])
if set(manifest) != set(files) - {"MANIFEST.json"}:
    raise ValueError("Incomplete manifest coverage")
for name, spec in manifest.items():
    check(files[name].encode("utf-8"), spec["bytes"], spec["sha256"])
restore = re.findall(r"^```python\n(.*?)^```\s*$", md, re.M | re.S)
if len(restore) != 1 or len(restore[0].encode("utf-8")) != 975:
    raise ValueError("Unexpected original restoration program")
ast.parse(restore[0])
payloads = {"source/" + name: value.encode("utf-8") for name, value in files.items()}
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
receipt = {"at": datetime.now(timezone.utc).isoformat(), "sourceFiles": 28,
    "exactSourcePreservedLocally": True, "localMathematicalOrNumericalReplay": False,
    "verification": "Immutable result hash; base64 and decoded byte/hash pins; all27 manifest hashes; Python AST checks and byte-exact file readback passed. Original restore.py preserved but not run because it launches a mathematical replay.",
    "scope": "Two NEW S8 C618 projective-metric own222/weak000 nonwinners, two already known own121 S8 deletions, bounded centroid-pullback coordinate theorem, full exact/numerical methods and frozen inputs.",
    "limitations": "Author reports exact audits and cold replay; monitor did not independently repeat mathematical audits, validate theorem proof, or establish literature novelty. Accepted construction record remains C624. Optional full sandbox ZIP not downloaded; capsule is standalone.",
    "files": {name: {"bytes": len(data), "sha256": sha(data)} for name, data in payloads.items()}}
with (root / "integrity-receipt.json").open("x", encoding="utf-8") as stream:
    json.dump(receipt, stream, indent=2)
    stream.write("\n")
print(json.dumps({"status": "NH72_S8_SOURCE_INTEGRITY_PASS", "sourceFiles": len(files), "names": list(files), "localReplay": False}))
