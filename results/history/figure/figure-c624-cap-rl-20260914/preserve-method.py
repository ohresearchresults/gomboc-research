"""Verify all three literal method parts before preserving the source package."""
import ast
import base64
from datetime import datetime, timezone
import hashlib
import json
import lzma
from pathlib import Path, PurePosixPath
import re

ROOT = Path(__file__).resolve().parent
OBS = ROOT.parent / "journal-materials-rollout-20260914-gye91I/figure-heartbeat-0244.json"
def sha(data):
    return hashlib.sha256(data).hexdigest()
def check(data, size, digest):
    if len(data) != size or sha(data) != digest:
        raise ValueError(f"Integrity mismatch: {len(data)} bytes, {sha(data)}")
    return data

obs_bytes = OBS.read_bytes()
delta = json.loads(obs_bytes)["journal"]["delta"]
canonical = Path("/REDACTED_HOME/.pro-research/runs/run_-kjrDuYVMzeTQ9tyWn464e75/research-journal.md")
if not delta or delta not in canonical.read_text(encoding="utf-8"):
    raise ValueError("Canonical journal provenance mismatch")
parts = re.findall(r"^```text\n(.*?)^```\s*$", delta, re.M | re.S)
specs = [(9360, "22c07b987203ecfc9d00fb07fdce8739f330eca4accb353662451fea4aef204d"),
         (9360, "bd8b9156006ba091262c32010693769a91b0c5b8589fb74164d8ecf337ba9520"),
         (8780, "218af253bac92004536c802f567d5d7fa712501a6de571f08bfda08093930b13")]
if len(parts) != 3:
    raise ValueError("Incomplete method capsule")
parts = [check("".join(part.split()).encode("ascii"), *spec) for part, spec in zip(parts, specs)]
capsule = check(b"".join(parts), 27500, "54410efa57199a39e8061f22c5097cc66b224b5c4b7869c749cadbaf1be5985b")
decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
decoded = decoder.decompress(base64.b85decode(capsule), max_length=74278)
if not decoder.eof or decoder.unused_data:
    raise ValueError("Unexpected compressed extent")
check(decoded, 74277, "0f168fd265ce4ed15626ec13105c0b8ec4ff58517b8c4897e61ee02911157d96")
files = json.loads(decoded)
if not isinstance(files, dict) or len(files) != 16:
    raise ValueError("Unexpected source count")
for name, source in files.items():
    path = PurePosixPath(name)
    if not isinstance(source, str) or path.is_absolute() or ".." in path.parts or "\\" in name or str(path) != name:
        raise ValueError("Unsafe source map")
    if name.endswith(".py"):
        ast.parse(source, filename=name)
manifest = json.loads(files["MANIFEST.json"])
if set(manifest) != set(files) - {"MANIFEST.json"}:
    raise ValueError("Manifest does not cover all payloads")
for name, spec in manifest.items():
    check(files[name].encode("utf-8"), spec["bytes"], spec["sha256"])
unpack = re.findall(r"^```python\n(.*?)^```\s*$", delta, re.M | re.S)
if len(unpack) != 1:
    raise ValueError("Unexpected decoder count")
unpack_bytes = check(unpack[0].encode("utf-8"), 1211, "6ec1ceb78232fbfdbbace2b8abb64b6d164d0d1902b460bc5881e709d6cb7d3f")
ast.parse(unpack_bytes)
payloads = {"method-source/" + name: source.encode("utf-8") for name, source in files.items()}
payloads.update({"method-journal-entries.md": delta.encode("utf-8"), "method-capsule.b85": capsule,
                 "UNPACK_C624_METHOD.py": unpack_bytes})
for name in payloads:
    if (ROOT / name).exists():
        raise FileExistsError(ROOT / name)
for name, data in payloads.items():
    target = ROOT / name
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as stream:
        stream.write(data)
    check(target.read_bytes(), len(data), sha(data))
receipt = {
    "at": datetime.now(timezone.utc).isoformat(), "observation": str(OBS), "observationSha256": sha(obs_bytes),
    "journalEvents": [1153, 1154, 1155, 1156], "sourceFiles": 16,
    "localVerification": "All3 part length/SHA pins, joined capsule and decoded JSON pins, all15 payload manifest pins, decoder pin, Python AST syntax and exact readback passed.",
    "localNumericalOrMathematicalReplay": False,
    "coordinatorClaim": "Cold numerical reproposal reproduced inherited positive G14 and both naive/relaxed failed finite generators byte-identically. These two failed proposals have numerical censuses, not full independent exact audits.",
    "scope": "Completes preservation of the already-notified C624 discovery method; not a new lower record or proof of global minimum. Exact body verification remains in the separate nine-file capsule.",
    "proseCorrection": "Later journal1156 explicitly corrects the duplicated27d seed hash to8057e4030d563b580ee714754a0b27b27d94373c01745a2a838c089f522a135b. Preserve both original entries; no payload normalization or guessed correction.",
    "files": {name: {"bytes": len(data), "sha256": sha(data)} for name, data in payloads.items()},
}
with (ROOT / "method-integrity-receipt.json").open("x", encoding="utf-8") as stream:
    json.dump(receipt, stream, indent=2)
    stream.write("\n")
print(json.dumps({"status": "METHOD_SOURCE_INTEGRITY_PASS", "sourceFiles": len(files), "names": list(files), "localReplay": False}))
