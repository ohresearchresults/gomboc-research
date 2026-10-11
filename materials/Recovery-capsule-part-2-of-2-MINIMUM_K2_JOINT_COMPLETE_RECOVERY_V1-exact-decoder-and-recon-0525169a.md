# material-0525169aec89

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Recovery capsule part 2 of 2

Object identity: MINIMUM_K2_JOINT_COMPLETE_RECOVERY_V1.

Part 1 is the complete literal JSON-escaped Python source stored as [internal-source-reference], 61293 bytes, SHA256 9e0e6352f8a2c2276d15bc70a08e61bf6ba77fefa11eb1a1fd223c679443a4dd. It was extracted without retyping from UTF-16 interval [13145,74438) of the fully read coordinator archive [internal-source-reference] (82568 bytes; SHA256 22b06373925c7e7dee2014f9d43d229dee69c5c6af63bbc329115f70b387f3ca). Part 1 plus the complete decoder below recover all 18 literal source units without any originating sandbox. Archived mathematical conclusions still require substantive integration; preservation alone does not promote the claimed 550-position ledger.

Save Part 1's literal text as escaped_source.txt without adding a trailing newline or otherwise re-escaping it. Save the Python block below as extract_k2_capsule.py with LF and final LF: 2860 bytes; SHA256 9f54d868791b6398ea2b2ef176662789b3507fed210e3b65b3468f83539309ab. Run `python -S extract_k2_capsule.py escaped_source.txt minimum_recovery`. It safely extracts the DATA constant rather than executing unreviewed archived Python. Expected markers: MINIMUM_COMPLETE_LITERAL_SOURCE_CAPSULE_RECOVERED 18; K2_ESCAPED_CAPSULE_INPUT_AND_SOURCE_PINS_PASS.

Recovered original wrapper recover_minimum_handoff.py: 61268 bytes; SHA256 6935b6a7d86ca31d63234fea512cec9085a1b1372c40f4a027e2960625164c65. Compressed XZ: 45236 bytes; SHA256 0ca2533f3babe67404425cb7f9ec39d15f2488e1c427b7b4a40244093c47df9b. Source JSON: 189376 bytes; SHA256 d41d2b0ba4c5219e0302394a45edd60fca4dea1873b3769e354eebeb2eaa784a. recovery_manifest.json: 42819 bytes; SHA256 4f4f62fde6cd696266e3ba4856a04b02985f08d78f6505905618c612fceca78c. The manifest contains all 17 input and 136 output pins, exact parameters, inherited evidence authorities and reproduction environment.

Subsequent commands inside minimum_recovery: `python -S recovery_driver.py sources`; `python recovery_driver.py recover`; `python -S recovery_driver.py verify`; `python -S recovery_driver.py audit`; `python -S recovery_driver.py history`. Optional negative-run regeneration: `python recovery_driver.py reproduce-unknown`. The archived report's expected terminal markers are ALL_JOINT_CERTIFICATES_EXACT_VERIFIED 31 26920 269200; LOCAL_K2_EXACT_COVERAGE_PASS_NOT_CANONICAL_MUTATION 550 0 55 200 0; ALL_EXACT_PHYSICAL_AND_CIRCUIT_AUDITS_PASS 5; EXACT_NON_RECORD_HISTORY_REPRODUCED 2. These are expected markers, not a claim of a new replay merely from this storage action. Target recovery_plan.coverage.json: 25330 bytes; SHA256 476681d9159ba33c037d0f5e9329374351c1a72c38a9f48ac6a117af93b86b2a.

Pinned numerical regeneration environment from the archived report: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Linux x86_64/glibc2.41, OpenBLAS0.3.30 with exact manifest configuration; thread counts 1, OPENBLAS_CORETYPE=SkylakeX, PYTHONHASHSEED=0. Start is exactly zero; no random search; all nondefault solver parameters in recovered sources and manifest. The exact verifier is standard-library integer/rational code. Numerical regeneration is not interchangeable with exact certificate verification. The old supplementary ZIP is not an input dependency and need not exist.

```python
"""Recover the exact MINIMUM_K2_JOINT_COMPLETE_RECOVERY_V1 source capsule.
Usage: python -S extract_k2_capsule.py escaped_source.txt [output_directory]
Input is the complete literal text of immutable [internal-source-reference].
No numerical search is performed by this extractor.
"""
from pathlib import Path
import ast
import base64
import hashlib
import json
import lzma
import sys

INPUT = (61293, "9e0e6352f8a2c2276d15bc70a08e61bf6ba77fefa11eb1a1fd223c679443a4dd")
SOURCE = (61268, "6935b6a7d86ca31d63234fea512cec9085a1b1372c40f4a027e2960625164c65")
PACKED = (45236, "0ca2533f3babe67404425cb7f9ec39d15f2488e1c427b7b4a40244093c47df9b")
RAW = (189376, "d41d2b0ba4c5219e0302394a45edd60fca4dea1873b3769e354eebeb2eaa784a")
MANIFEST = (42819, "4f4f62fde6cd696266e3ba4856a04b02985f08d78f6505905618c612fceca78c")

def check(data, pin, label):
    observed = (len(data), hashlib.sha256(data).hexdigest())
    if observed != pin:
        raise ValueError(f"{label}: {observed!r} != {pin!r}")

def write_exact(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != data:
            raise ValueError(f"Refusing to replace different file: {path}")
    else:
        path.write_bytes(data)

def main():
    if len(sys.argv) not in (2, 3):
        raise SystemExit(__doc__)
    raw_input = Path(sys.argv[1]).read_bytes()
    check(raw_input, INPUT, "escaped source")
    source = json.loads('"' + raw_input.decode("utf-8") + '"').encode("utf-8")
    check(source, SOURCE, "original recovery source")
    assignments = [node for node in ast.parse(source).body
                   if isinstance(node, ast.Assign) and
                   any(isinstance(t, ast.Name) and t.id == "DATA" for t in node.targets)]
    if len(assignments) != 1:
        raise ValueError("Expected exactly one DATA assignment")
    encoded = ast.literal_eval(assignments[0].value)
    packed = base64.b64decode(encoded, validate=True)
    check(packed, PACKED, "XZ")
    unpacked = lzma.decompress(packed)
    check(unpacked, RAW, "source JSON")
    files = json.loads(unpacked)
    if not isinstance(files, dict) or len(files) != 18:
        raise ValueError("Expected exactly 18 source units")
    check(files["recovery_manifest.json"].encode("utf-8"), MANIFEST, "manifest")
    root = Path(sys.argv[2] if len(sys.argv) == 3 else "minimum_recovery")
    write_exact(root / "recover_minimum_handoff.py", source)
    for name, text in files.items():
        p = Path(name)
        if p.is_absolute() or ".." in p.parts or not isinstance(text, str):
            raise ValueError(f"Unsafe source unit {name!r}")
        write_exact(root / p, text.encode("utf-8"))
    print("MINIMUM_COMPLETE_LITERAL_SOURCE_CAPSULE_RECOVERED", len(files))
    print("K2_ESCAPED_CAPSULE_INPUT_AND_SOURCE_PINS_PASS")

if __name__ == "__main__":
    main()
```
