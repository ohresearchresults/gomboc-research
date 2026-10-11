"""Preserve the complete literal C624 capsule; do not execute research code."""
import ast
import base64
from datetime import datetime, timezone
import hashlib
import json
import lzma
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
OBSERVATION = ROOT.parent / "journal-materials-rollout-20260914-gye91I/figure-heartbeat-0228.json"
CANONICAL = Path("/REDACTED_HOME/.pro-research/runs/run_-kjrDuYVMzeTQ9tyWn464e75/research-journal.md")
def sha(data):
    return hashlib.sha256(data).hexdigest()
def checked(data, size, digest):
    if len(data) != size or sha(data) != digest:
        raise ValueError(f"Integrity mismatch: {len(data)} bytes, SHA {sha(data)}")
    return data

observation_bytes = OBSERVATION.read_bytes()
observation = json.loads(observation_bytes)
delta = observation["journal"]["delta"]
if not delta or delta not in CANONICAL.read_text(encoding="utf-8"):
    raise ValueError("Journal source mismatch")
start, end = "\nBEGIN_COORD_CAP_RL_C624_EXACT_CAPSULE\n", "\nEND_COORD_CAP_RL_C624_EXACT_CAPSULE\n"
if delta.count(start) != 1 or delta.count(end) != 1:
    raise ValueError("Ambiguous capsule extent")
capsule = checked("".join(delta.split(start)[1].split(end)[0].split()).encode("ascii"), 15935,
                  "e494943aec3ecc12589b2c900a3b1d09ae61fd2edf58670df37a47adfc969730")
decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
decoded = decoder.decompress(base64.b85decode(capsule), max_length=37490)
if not decoder.eof or decoder.unused_data:
    raise ValueError("Unexpected compressed stream extent")
checked(decoded, 37489, "481ab0d864b0fc208b0e97f98e2678018a6956b7ae86b8504bf0b97ba1ee628d")
files = json.loads(decoded)
allowed = {"GENERATOR_G14.json", "ROUND.py", "RECONSTRUCT.py", "check_A.py", "check_B.py",
           "centred_mass.py", "REPLAY.py", "EXPECTED.json", "MANIFEST.json"}
if set(files) != allowed or not all(isinstance(value, str) for value in files.values()):
    raise ValueError("Unexpected source map")
manifest = json.loads(files["MANIFEST.json"])
if set(manifest) != allowed - {"MANIFEST.json"}:
    raise ValueError("Manifest coverage mismatch")
for name, spec in manifest.items():
    checked(files[name].encode("utf-8"), spec["bytes"], spec["sha256"])
blocks = re.findall(r"^```python\n(.*?)^```\s*$", delta, re.M | re.S)
if len(blocks) != 1:
    raise ValueError("Unexpected decoder source count")
unpack = checked(blocks[0].encode("utf-8"), 832, "47e5b13321754e19d29bcdcb1407ea23f4f37cedaf64393635a1edbf0fa73f92")
payloads = {"source/" + name: value.encode("utf-8") for name, value in files.items()}
payloads.update({"UNPACK_C624.py": unpack, "source-journal-entries.md": delta.encode("utf-8"),
                 "C624_EXACT_CAPSULE.b85": capsule, "decoded-source-map.json": decoded})
for name, data in payloads.items():
    if name.endswith(".py"):
        ast.parse(data, filename=name)
    if (ROOT / name).exists():
        raise FileExistsError(ROOT / name)
for name, data in payloads.items():
    target = ROOT / name
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as stream:
        stream.write(data)
    checked(target.read_bytes(), len(data), sha(data))
receipt = {
    "at": datetime.now(timezone.utc).isoformat(), "canonicalJournal": str(CANONICAL),
    "observation": str(OBSERVATION), "observationSha256": sha(observation_bytes), "journalEvents": [1151, 1152],
    "coordinatorAcceptanceAt": "2026-09-14T02:27:09.018Z", "complexity": 624,
    "preferred": "COORD_CAP_RL_C624_INHERITED_G9", "alsoPreserved": ["G14", "G8_NONWINNER"],
    "coordinatorClaim": "G9/G14 V177 E312 F137 strict110 weak000; G8_NONWINNER exact121. Reports complete independent A/B audits, third mass, negative fixtures and source-only cold replay for all3 objects.",
    "localVerification": "Capsule and decoded JSON bytes/SHA, all8 source-manifest pins, literal832-byte decoder pin, Python AST syntax and byte-exact file readback passed. Exact G9/G14/G8 definitions and all replay dependencies preserved.",
    "localMathematicalReplay": False, "globalMinimumProven": False,
    "arithmetic": "Coordinator reports G9 common denominator51085bits, implying15378 or15379 decimal digits, approximately15.4thousand. This is denominator size, not decimal precision or manufacturing tolerance.",
    "methodDependency": "Exact final objects are standalone. Discovery used immutable parent asg_RCec_cSHP9QT7MDzi-ldZ6Dy, preserved separately in figure-c626-bq13-stable-cap-20260914. Full new numerical discovery source capsule is still pending.",
    "files": {name: {"bytes": len(data), "sha256": sha(data)} for name, data in payloads.items()},
}
with (ROOT / "integrity-receipt.json").open("x", encoding="utf-8") as stream:
    json.dump(receipt, stream, indent=2)
    stream.write("\n")
print(json.dumps({"status": "SOURCE_INTEGRITY_PASS", "sourceFiles": len(files), "complexity": 624,
                  "localMathematicalReplay": False, "receipt": str(ROOT / "integrity-receipt.json")}))
