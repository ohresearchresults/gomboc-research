"""Extract and hash-check a literal result capsule, without executing its code."""
import ast
import base64
from datetime import datetime, timezone
import hashlib
import json
import lzma
from pathlib import Path, PurePosixPath
import sqlite3

ROOT = Path(__file__).resolve().parent
ASSIGNMENT = "asg_RCec_cSHP9QT7MDzi-ldZ6Dy"
RUN = "run_-kjrDuYVMzeTQ9tyWn464e75"
EXPECTED_RESULT_SHA = "e4b02b73abe4b9f212844982334fd28adf447de9a106e47e30a205829a4d33c4"
def sha(data):
    return hashlib.sha256(data).hexdigest()
def checked(data, size, digest):
    if len(data) != size or sha(data) != digest:
        raise ValueError(f"Integrity mismatch: {len(data)} bytes, SHA {sha(data)}")
    return data

db = sqlite3.connect("file:/REDACTED_HOME/.pro-research/state/research.sqlite?mode=ro", uri=True)
row = db.execute("SELECT run_id,sha256,raw,created_at FROM results WHERE assignment_id=?", (ASSIGNMENT,)).fetchone()
db.close()
if not row or row[0] != RUN or row[1] != EXPECTED_RESULT_SHA:
    raise ValueError("Result ownership mismatch")
raw = checked(row[2].encode("utf-8"), 99064, EXPECTED_RESULT_SHA)
result = json.loads(raw)
if result["version"] != 2 or not isinstance(result["result_markdown"], str):
    raise ValueError("Unexpected result contract")
markdown = result["result_markdown"]
start, end = "\nBEGIN_BQ13_C626_CAPSULE\n", "\nEND_BQ13_C626_CAPSULE\n"
if markdown.count(start) != 1 or markdown.count(end) != 1:
    raise ValueError("Ambiguous capsule extent")
capsule = checked("".join(markdown.split(start)[1].split(end)[0].split()).encode("ascii"),
                  75845, "5205e8dba550c0462a40e9dc179a941bf96f9357ed3f92f0502bbb40d76bb341")
decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
decoded = decoder.decompress(base64.b85decode(capsule), max_length=229875)
if not decoder.eof or decoder.unused_data:
    raise ValueError("Unexpected compressed stream extent")
checked(decoded, 229874, "7c480e9fbdb117d52c5ab4a6116e7af1e34bf2bcbc1228f1360fd67d66f98398")
files = json.loads(decoded)
if not isinstance(files, dict) or len(files) != 45:
    raise ValueError("Unexpected source count")
for name, source in files.items():
    rel = PurePosixPath(name)
    if not isinstance(source, str) or rel.is_absolute() or ".." in rel.parts or "\\" in name or str(rel) != name:
        raise ValueError("Unsafe source map")
    if name.endswith(".py"):
        ast.parse(source, filename=name)
manifest = json.loads(files["SOURCE_MANIFEST.json"])
if set(manifest) != set(files) - {"SOURCE_MANIFEST.json"}:
    raise ValueError("Source manifest coverage mismatch")
for name, digest in manifest.items():
    if sha(files[name].encode("utf-8")) != digest:
        raise ValueError("Source hash mismatch: " + name)
payloads = {"source/" + name: source.encode("utf-8") for name, source in files.items()}
payloads["result.json"] = raw
payloads["result.md"] = markdown.encode("utf-8")
for name in payloads:
    if (ROOT / name).exists():
        raise FileExistsError(ROOT / name)
for name, data in payloads.items():
    target = ROOT / name
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as stream:
        stream.write(data)
    checked(target.read_bytes(), len(data), sha(data))
receipt = {
    "at": datetime.now(timezone.utc).isoformat(), "assignmentId": ASSIGNMENT, "runId": RUN,
    "resultAt": row[3], "resultSha256": EXPECTED_RESULT_SHA, "eventSeq": 1145,
    "workerClaim": "New distinct BQ13_C626_STABLE_CAP_VERTEX_68_96_OWN110; V178 E313 F137 strict110 weak000. Also exact C626 own121 and own34/71/103 nonwinners, finite numerical checkpoints and methods.",
    "researchRecordUnchanged": 626, "coordinatorAcceptanceOfThisVariant": "Not observed yet",
    "localVerification": "Original immutable result bytes/SHA, capsule bytes/SHA, decoded JSON bytes/SHA, all44 source hashes, Python AST syntax and byte-exact file readback verified. Full45-file source capsule preserved.",
    "localMathematicalReplay": False,
    "claimedWinnerCommonCentredDenominatorBits": 82260,
    "archiveBoundary": "Optional167-file sandbox bundle not downloaded; complete45-file literal source capsule, exact definitions, replay methods and retained critical checkpoints are preserved. Archive-only scratch controls are not claimed saved.",
    "files": {name: {"bytes": len(data), "sha256": sha(data)} for name, data in payloads.items()},
}
with (ROOT / "integrity-receipt.json").open("x", encoding="utf-8") as stream:
    json.dump(receipt, stream, indent=2)
    stream.write("\n")
print(json.dumps({"status": "SOURCE_INTEGRITY_PASS", "sourceFiles": len(files), "recordUnchanged": 626, "mathematicalReplay": False, "receipt": str(ROOT / "integrity-receipt.json")}))
