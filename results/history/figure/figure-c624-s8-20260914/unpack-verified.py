"""Extract the downloaded literal source capsule with bounded decompression."""
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
        raise ValueError(f"Integrity mismatch: {len(data)} bytes, {sha(data)}")
    return data
md = check((root / "RECOVERY_CAPSULE.md").read_bytes(), 63772, "b6973b557f3c9deb735587ad183899d09ce355ecfe94d260f7c04618dc2e0e70").decode("utf-8")
start = "\nBEGIN_COORD_C624_STRONG_G8_COMPLETE_SOURCE\n"
end = "\nEND_COORD_C624_STRONG_G8_COMPLETE_SOURCE\n"
if md.count(start) != 1 or md.count(end) != 1:
    raise ValueError("Ambiguous capsule markers")
capsule = check("".join(md.split(start)[1].split(end)[0].split()).encode("ascii"), 59100, "e3c07742531ebe37a1a3332748807c7154f5d7a9c669b57bb78612041dbd1c00")
decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
decoded = decoder.decompress(base64.b85decode(capsule), max_length=170011)
if not decoder.eof or decoder.unused_data:
    raise ValueError("Unexpected compressed extent")
check(decoded, 170010, "44319c99762df191373664c4e89bbeb7fb70db771c7c38e0a19e4e0ea2645fd3")
files = json.loads(decoded)
if not isinstance(files, dict) or len(files) != 30:
    raise ValueError("Unexpected file count")
for name, text in files.items():
    rel = PurePosixPath(name)
    if not isinstance(text, str) or rel.is_absolute() or ".." in rel.parts or "\\" in name or str(rel) != name:
        raise ValueError("Unsafe source map")
    if name.endswith(".py"):
        ast.parse(text, filename=name)
manifest = json.loads(files["SOURCE_MANIFEST.json"])
if set(manifest) != set(files) - {"SOURCE_MANIFEST.json"}:
    raise ValueError("Source manifest coverage mismatch")
for name, spec in manifest.items():
    check(files[name].encode("utf-8"), spec["bytes"], spec["sha256"])
unpack = re.findall(r"^```python\n(.*?)^```\s*$", md, re.M | re.S)
if len(unpack) != 1:
    raise ValueError("Unexpected decoder count")
unpack = check(unpack[0].encode("utf-8"), 989, "5774531aeecf01cb48889472489c1d106cd3654d2a0213a3136b18b614ad4420")
ast.parse(unpack)
payloads = {"source/" + name: text.encode("utf-8") for name, text in files.items()}
payloads.update({"UNPACK.py": unpack, "SOURCE_CAPSULE.b85": capsule})
for name in payloads:
    if (root / name).exists():
        raise FileExistsError(root / name)
for name, data in payloads.items():
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)
    check(path.read_bytes(), len(data), sha(data))
receipt = {"at": datetime.now(timezone.utc).isoformat(), "sourceFiles": 30,
    "exactSourcePreservedLocally": True, "localMathematicalOrNumericalReplay": False,
    "verification": "Authenticated downloaded capsule pin, base85/decoded byte and SHA pins, all29 source pins,989-byte decoder pin, Python syntax and byte-exact file readback passed. No generated research code executed.",
    "scope": "S8 C624 arithmetic candidate plus G14/G10/G9P positive variants and G9 nonwinner with all critical source/method inputs; scientific results remain author-reported until separately replayed.",
    "supersedes": "handoff-preservation-receipt.json exactSourcePreservedLocally=false is historical; full30-file capsule is now locally preserved. Separate COMPLETE_HANDOFF JSON and optional full audit ZIP were not downloaded.",
    "files": {name: {"bytes": len(data), "sha256": sha(data)} for name, data in payloads.items()}}
with (root / "source-integrity-receipt.json").open("x", encoding="utf-8") as stream:
    json.dump(receipt, stream, indent=2)
    stream.write("\n")
print(json.dumps({"status": "S8_SOURCE_INTEGRITY_PASS", "sourceFiles": len(files), "names": list(files), "localReplay": False}))
