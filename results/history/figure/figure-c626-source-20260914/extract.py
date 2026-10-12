"""Preserve literal journal sources; validate hashes, never execute payload code."""
import ast
import base64
import hashlib
import json
import lzma
from pathlib import Path
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
OBSERVATION = ROOT.parent / "journal-materials-rollout-20260914-gye91I/figure-heartbeat-0104.json"
JOURNAL = Path("/REDACTED_HOME/.pro-research/runs/run_-kjrDuYVMzeTQ9tyWn464e75/research-journal.md")

def sha(data):
    return hashlib.sha256(data).hexdigest()

def checked(data, size, digest):
    if len(data) != size or sha(data) != digest:
        raise ValueError(f"Integrity mismatch: bytes={len(data)}, sha256={sha(data)}")
    return data

observation_bytes = OBSERVATION.read_bytes()
observation = json.loads(observation_bytes)
delta = observation["journal"]["delta"]
if not delta or delta not in JOURNAL.read_text(encoding="utf-8"):
    raise ValueError("Captured journal delta is not present in canonical journal")
exact_entry, method_entry = delta.split("## 2026-09-14T01:02:40.613Z", 1)
if "Recovery capsule part 1/1" not in exact_entry:
    raise ValueError("Unexpected source entry")
blocks = re.findall(r"^```text\n(.*?)^```\s*$", exact_entry, re.M | re.S)
if len(blocks) != 1:
    raise ValueError("Expected exactly one source capsule")
capsule = checked("".join(blocks[0].split()).encode("ascii"), 16990,
                  "45d554b84112aad09df18700626eba7f43fe0fab11ba9fff304a99a28866ba6d")
decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
decoded = decoder.decompress(base64.b85decode(capsule), max_length=45414)
if not decoder.eof or decoder.unused_data:
    raise ValueError("Unexpected compressed stream extent")
checked(decoded, 45413, "d8a1e7da95dfef6262bc260e454e3cdc281d2be155e62b6ec26f698f01319403")
files = json.loads(decoded)
allowed = {"RECONSTRUCT.py", "check_A.py", "check_B.py", "centred_mass.py",
           "G8/GENERATOR.json", "G14/GENERATOR.json", "EXPECTED.json", "REPLAY.py", "MANIFEST.json"}
if set(files) != allowed or not all(isinstance(value, str) for value in files.values()):
    raise ValueError("Unexpected source map")
manifest = json.loads(files["MANIFEST.json"])
if set(manifest) != allowed - {"MANIFEST.json"}:
    raise ValueError("Unexpected manifest entries")
for name, spec in manifest.items():
    checked(files[name].encode("utf-8"), spec["bytes"], spec["sha256"])
payloads = {"exact/" + name: value.encode("utf-8") for name, value in files.items()}
method_specs = {
    "make_double.py": (1974, "ae57361adcf41586f04efe10223243cd4bc987dd59d854a10dff53d7acc638b9"),
    "coarsen.py": (1083, "14e7570cdc0f485d690d16a78c99a368c8ce75059f97e5cdfd63453e9741b895"),
    "reproposal.py": (1482, "bacf6cc1a448831c88f0799f66cc6f2e8b67256a98a62d5cab3bf76d4d21da5a"),
}
for name, (size, digest) in method_specs.items():
    matches = re.findall(r"^" + re.escape(name) + r"[^\n]*\n```python\n(.*?)^```\s*$", method_entry, re.M | re.S)
    if len(matches) != 1:
        raise ValueError(f"Expected one literal method source: {name}")
    payloads["method/" + name] = checked(matches[0].encode("utf-8"), size, digest)
for name, data in payloads.items():
    if name.endswith(".py"):
        ast.parse(data, filename=name)
payloads["C626_EXACT_CAPSULE.txt"] = capsule
payloads["source-journal-entries.md"] = delta.encode("utf-8")
payloads["decoded-source-map.json"] = decoded
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
    "at": datetime.now(timezone.utc).isoformat(),
    "canonicalJournal": str(JOURNAL), "journalObservationAt": observation["at"],
    "observation": str(OBSERVATION), "observationSha256": sha(observation_bytes),
    "journalEvents": [1137, 1138],
    "claim": "Coordinator accepted C626 G8 and G14: V178 E313 F137 strict110 weak000, with two full exact audits and third mass integration reported.",
    "localVerification": "Capsule and decoded JSON pins, all 8 manifest file pins, 3 method file pins, Python AST syntax and byte-exact written-file readback passed. No mathematical replay executed by this extractor.",
    "mathematicalReplay": False,
    "methodDependency": "Literal unchanged BQ13 27-file parent in result asg_zSkJefQuEkGHd3_fzUFMGE19 SHA5f57852087082e58a87bf09e4674cddc11627f384f7ac9124c0c8102d12d1d29. Required for search-method replay, not for exact G8/G14 replay.",
    "files": {name: {"bytes": len(data), "sha256": sha(data)} for name, data in payloads.items()},
}
with (ROOT / "integrity-receipt.json").open("x", encoding="utf-8") as stream:
    json.dump(receipt, stream, ensure_ascii=False, indent=2)
    stream.write("\n")
print(json.dumps({"status": "SOURCE_INTEGRITY_PASS", "files": len(payloads), "receipt": str(ROOT / "integrity-receipt.json"), "mathematicalReplay": False}))
