"""Verify canonical multipart source transport; do not execute research code."""
import ast
import base64
from datetime import datetime, timezone
import hashlib
import json
import lzma
from pathlib import Path, PurePosixPath
import re

root = Path(__file__).resolve().parent
parent = root.parent / "figure-c624-s8-20260914"
def sha(data):
    return hashlib.sha256(data).hexdigest()
def check(data, size, digest):
    if len(data) != size or sha(data) != digest:
        raise ValueError("Source integrity mismatch")
    return data
def decode(data, size, digest):
    dec = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
    raw = dec.decompress(base64.b85decode(data), max_length=size + 1)
    if not dec.eof or dec.unused_data:
        raise ValueError("Unexpected compressed extent")
    return json.loads(check(raw, size, digest))
def verify_map(files, count, manifest_name):
    if not isinstance(files, dict) or len(files) != count:
        raise ValueError("Unexpected source count")
    for name, text in files.items():
        rel = PurePosixPath(name)
        if not isinstance(text, str) or not rel.parts or rel.is_absolute() or ".." in rel.parts or "\\" in name or str(rel) != name:
            raise ValueError("Unsafe source path")
        if name.endswith(".py"):
            ast.parse(text, filename=name)
    manifest = json.loads(files[manifest_name])
    if set(manifest) != set(files) - {manifest_name}:
        raise ValueError("Incomplete manifest")
    for name, spec in manifest.items():
        check(files[name].encode("utf-8"), spec["bytes"], spec["sha256"])

md = (root / "journal-entries.md").read_text(encoding="utf-8")
sections = re.split(r"(?=^## Recovery capsule part \d+/11 — S8_PC_SIX_NONWINNERS_AND_METHODS)", md, flags=re.M)
sections = [s for s in sections if s.startswith("## Recovery capsule part")]
if len(sections) != 11:
    raise ValueError("Source capsule still incomplete or duplicated")
chunks, pins = [], []
for i, section in enumerate(sections, 1):
    if int(re.match(r"## Recovery capsule part (\d+)/11", section).group(1)) != i:
        raise ValueError("Part ordering differs")
    pin = re.search(r"chars\[(\d+),(\d+)\)[^\n]*?SHA256\s*([0-9a-f]{64})", section)
    if not pin:
        raise ValueError("Missing part pin")
    start, end = int(pin[1]), int(pin[2])
    if start != (i - 1) * 6000 or end != (i * 6000 if i < 11 else 64470):
        raise ValueError("Part offsets differ")
    blocks = re.findall(r"^```text\n(.*?)^```\s*$", section, re.M | re.S)
    candidates = ["".join(block.split()).encode("ascii") for block in blocks if len("".join(block.split())) == end - start]
    if len(candidates) != 1:
        raise ValueError("Ambiguous encoded part")
    chunks.append(check(candidates[0], end - start, pin[3]))
    pins.append({"part": i, "start": start, "end": end, "sha256": pin[3]})
capsule = check(b"".join(chunks), 64470, "e182149c7c1c850dcecf423563b6d8815d391ca8cf4c52160fe04c19ebbebafd")
files = decode(capsule, 300482, "91f5a9f8a543ea9d03481fc781618ddd35fc75b0f3f7836e8287a64ab92371c4")
verify_map(files, 73, "NEW_MANIFEST.json")
restore = re.findall(r"^```python\n(.*?)^```\s*$", sections[0], re.M | re.S)
if len(restore) != 1:
    raise ValueError("Ambiguous restoration program")
check(restore[0].encode("utf-8"), 976, "c50c55d13a5421492201631923d026eec924e3901556934e19a706cbf6dbdd17")
ast.parse(restore[0])
parent_capsule = check((parent / "SOURCE_CAPSULE.b85").read_bytes(), 59100, "e3c07742531ebe37a1a3332748807c7154f5d7a9c669b57bb78612041dbd1c00")
parent_files = decode(parent_capsule, 170010, "44319c99762df191373664c4e89bbeb7fb70db771c7c38e0a19e4e0ea2645fd3")
verify_map(parent_files, 30, "SOURCE_MANIFEST.json")
for name, text in parent_files.items():
    data = text.encode("utf-8")
    if (parent / "source" / name).read_bytes() != data:
        raise ValueError("Prior S8 source readback differs")
payloads = {"new-source/" + name: text.encode("utf-8") for name, text in files.items()}
payloads.update({"restore_new.py": restore[0].encode("utf-8"), "NEW_CAPSULE.b85": capsule})
for name in payloads:
    if (root / name).exists():
        raise FileExistsError(root / name)
for name, data in payloads.items():
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)
    check(path.read_bytes(), len(data), sha(data))
receipt = {"at": datetime.now(timezone.utc).isoformat(), "completeSourcePreservedLocally": True,
    "newSourceFiles": 73, "priorDependencyFiles": 30, "parts": pins,
    "priorDependencyDirectory": str(parent / "source"),
    "verification": "Canonical journal byte readback, all11 part pins/offsets, whole64470-char base85 and300482-byte decoded pins, all72 new and29 old manifest pins, Python AST and exact written-file readback passed. Old30-file S8 dependency verified without duplicating its archive.",
    "localMathematicalOrNumericalReplay": False,
    "scope": "Six own121/weak000 C618/C620/C622 nonwinners, full predictor-corrector and earlier failed numerical methods, exact finite endpoints and expected output checksums. All mathematical and cold replay checks remain author-reported.",
    "supersedes": "s8-pc-partial-0507.json is a historical9/11 snapshot, not current missing-source status.",
    "files": {name: {"bytes": len(data), "sha256": sha(data)} for name, data in payloads.items()}}
with (root / "integrity-receipt.json").open("x", encoding="utf-8") as stream:
    json.dump(receipt, stream, indent=2)
    stream.write("\n")
print(json.dumps({"status": "S8_PC_FULL_SOURCE_INTEGRITY_PASS", "newFiles": len(files), "oldFiles": len(parent_files), "names": list(files), "localReplay": False}))
