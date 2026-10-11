"""Preserve the literal ATLAS56 capsule without running its research programs."""
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
raw = check((root / "result.json").read_bytes(), 48826, "ce3bc71c79e645777301fa6ac1adcb9a3e29cb148af68147797add570f1aa60d")
md = json.loads(raw)["result_markdown"]
if (root / "result.md").read_bytes() != md.encode("utf-8"):
    raise ValueError("Result markdown differs from immutable JSON")
blocks = re.findall(r"^```text\n(.*?)^```\s*$", md, re.M | re.S)
candidates = ["".join(block.split()).encode("ascii") for block in blocks if len("".join(block.split())) == 30810]
if len(candidates) != 1:
    raise ValueError("Ambiguous capsule block")
capsule = check(candidates[0], 30810, "4807ee686ca4052f1588bdc7d9356e212aaa5a34736e1b2e2688f756a30f35d4")
decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
decoded = decoder.decompress(base64.b85decode(capsule), max_length=93395)
if not decoder.eof or decoder.unused_data:
    raise ValueError("Unexpected compressed extent")
check(decoded, 93394, "35d4de0ce185e798c204c8a8c42cbadafe5d741ab590a435c54db24164017ab9")
files = json.loads(decoded)
if not isinstance(files, dict) or len(files) != 22:
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
if len(restore) != 1 or len(restore[0].encode("utf-8")) != 966:
    raise ValueError("Unexpected original restoration program")
ast.parse(restore[0])
payloads = {"source/" + name: text.encode("utf-8") for name, text in files.items()}
payloads.update({"restore.py": restore[0].encode("utf-8"), "SOURCE_CAPSULE.b85": capsule})
for name in payloads:
    if (root / name).exists():
        raise FileExistsError(root / name)
for name, data in payloads.items():
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)
    check(path.read_bytes(), len(data), sha(data))
receipt = {"at": datetime.now(timezone.utc).isoformat(), "sourceFiles": 22,
    "exactSourcePreservedLocally": True, "localMathematicalOrNumericalReplay": False,
    "verification": "Immutable result pin, base85 and decoded byte/hash pins, all21 manifest hashes, Python AST checks and byte-exact file readback passed. No research program executed.",
    "scope": "Three new author-verified own110/weak000 C626 arithmetic successors: D3_SMALL, D3_STRONG, ADAPT. Literal parent, frozen exact generators, exact witnesses, independent audits, mass and numerical reproposal sources and inputs retained.",
    "limitations": "Mathematical audits, cold replay and numerical byte-identical reproposal are author reports, not monitor replays. C624 remains the complexity record. Optional source-only and full output ZIPs were not downloaded.",
    "files": {name: {"bytes": len(data), "sha256": sha(data)} for name, data in payloads.items()}}
with (root / "integrity-receipt.json").open("x", encoding="utf-8") as stream:
    json.dump(receipt, stream, indent=2)
    stream.write("\n")
print(json.dumps({"status": "ATLAS56_SOURCE_INTEGRITY_PASS", "sourceFiles": len(files), "names": list(files), "localReplay": False}))
