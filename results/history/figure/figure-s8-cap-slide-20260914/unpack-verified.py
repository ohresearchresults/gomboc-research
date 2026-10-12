"""Verify and preserve a canonical source capsule; do not execute research code."""
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
raw = (root / "journal-entries.md").read_bytes()
provenance = json.loads((root / "journal-preservation-receipt.json").read_text())
check(raw, provenance["bytes"], provenance["sha256"])
md = raw.decode("utf-8")
parts = re.findall(r"^CAP_SLIDE_B64_([1-4])_BEGIN\n([A-Za-z0-9+/=\n]+)\nCAP_SLIDE_B64_\1_END$", md, re.M)
if [i for i, _ in parts] != list("1234"):
    raise ValueError("Incomplete or reordered source capsule")
capsule = check("".join("".join(value.split()) for _, value in parts).encode("ascii"), 47960, "e749e6b45436636c172a725c058b729a098c4ef5213a1d2371c40282fe6d0417")
compressed = check(base64.b64decode(capsule, validate=True), 35968, "c96bee088ebad0e41c85ea44f1bb55e580ce1a65cd0b9379075581f9e10df021")
decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
decoded = decoder.decompress(compressed, max_length=121553)
if not decoder.eof or decoder.unused_data:
    raise ValueError("Unexpected compressed extent")
check(decoded, 121552, "ef0a76e229b1b640b2b186d8792bb5f2ac81093f54f7440ede5dddf40e34b117")
files = json.loads(decoded)
if not isinstance(files, dict) or len(files) != 27:
    raise ValueError("Unexpected source count")
for name, value in files.items():
    rel = PurePosixPath(name)
    if not isinstance(value, str) or not rel.parts or rel.is_absolute() or ".." in rel.parts or "\\" in name or str(rel) != name:
        raise ValueError("Unsafe source path")
    if name.endswith(".py"):
        ast.parse(value, filename=name)
if sum(len(value.encode("utf-8")) for value in files.values()) != 118787:
    raise ValueError("Source byte count differs")
manifest = json.loads(files["MANIFEST.json"])
if set(manifest) != set(files) - {"MANIFEST.json"}:
    raise ValueError("Incomplete source manifest")
for name, spec in manifest.items():
    check(files[name].encode("utf-8"), spec["bytes"], spec["sha256"])
restore = re.findall(r"^```python\n(.*?)^```\s*$", md, re.M | re.S)
if len(restore) != 1:
    raise ValueError("Ambiguous original decoder")
ast.parse(restore[0])
payloads = {"source/" + name: value.encode("utf-8") for name, value in files.items()}
payloads.update({"UNPACK_CAP_SLIDE.py": restore[0].encode("utf-8"), "SOURCE_CAPSULE.b64": capsule})
for name in payloads:
    if (root / name).exists():
        raise FileExistsError(root / name)
for name, data in payloads.items():
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)
    check(path.read_bytes(), len(data), sha(data))
receipt = {"at": datetime.now(timezone.utc).isoformat(), "sourceFiles": 27,
    "completeSourcePreservedLocally": True, "localMathematicalOrNumericalReplay": False,
    "verification": "Canonical journal byte readback; four ordered complete parts; whole base64, compressed and decoded pins; all26 source manifest pins; Python AST and byte-exact file readback passed. No research code executed.",
    "scope": "Author's nine exact continuous one-vertex-slide exclusions, three separately audited finite nonwinner endpoints, local rank3 filled-centroid control by two physical projective caps, numerical methods and finite inputs.",
    "limitations": "Mathematical checks and proofs are author-reported, not independently replayed by monitor. No global lower bound, no entire projective-family exclusion, no C<624 winner and no quantitative manufacturing tolerance implied. Later cold-replay observation requires its own evidence.",
    "files": {name: {"bytes": len(data), "sha256": sha(data)} for name, data in payloads.items()}}
with (root / "integrity-receipt.json").open("x", encoding="utf-8") as stream:
    json.dump(receipt, stream, indent=2)
    stream.write("\n")
print(json.dumps({"status": "CAP_SLIDE_SOURCE_INTEGRITY_PASS", "sourceFiles": len(files), "names": list(files), "localReplay": False}))
