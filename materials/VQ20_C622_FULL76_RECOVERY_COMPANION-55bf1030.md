# material-55bf1030e3d0

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# VQ20 C622 FULL76 — scoped recovery companion

## Identity and provenance

The exact nine payloads are separately preserved in material **[internal-source-reference]**, VQ20_C622_FULL76_NINE_LITERAL_PARTS.md, 90000 UTF-8 bytes, SHA-256 6b2f26e1da41ca6bd760b96579f6030c7cfeed8bffb777a46fcbf6fd0f6d2a4a. This is the complete literal extraction [685615,775615) from archive [internal-source-reference], SHA-256 e468b08ac896d49c832f5716ebf5b0b7ab895b7ba81c0edb3fbb4ecdbf06be9f. The lead read that entire selected range in two contiguous pages before extraction. Intervening preserved-span headings are not payload bytes. There are exactly nine fenced text payloads, in original part order.

This preserves the accepted endpoint VQ20_C622_ROUTE88_118_G12 and the full original 76-source map. It is a source scoping operation, NOT a fresh geometric replay or a new construction. The old statement that its native result alone omitted a recovery capsule remains true, but later complete nine-part preservation and source-only cold replay closed that historical gap. The exact decoded source map, not a filename or a hash alone, is the dependency.

Normalized payload lengths: eight parts of10000 ASCII characters, then8685. Concatenated88685 ASCII bytes SHA-256 56bb46a476d35128b4743224c5f015d13f38d99d50e319f9bef871878350cd94. Python base85 decode followed by LZMA decompress gives312622 bytes SHA-256 617f94b82a54bf54cd7cce67fbf5d506cc3d2b9431a7c64b587984ea429992f6, a JSON filename-to-complete-UTF8-source map of76 entries. Its MANIFEST.json SHA-256 is d06bc3d5782b4ebf2449b4bd89e962ce88f08faca9d06ae068a5bfaf22af0c53.

## Complete original decoder

Save the following as RECOVER_C622_PARTS.py with UTF-8, LF and one final newline. Historical byte count1975 and SHA-256 f13d97720ad700653053845dfac2e5e449868990549740aa71966a39985761e8. Its nine inputs are the text inside the nine fences, named C622_CAPSULE_01.b85 through C622_CAPSULE_09.b85; whitespace may remain because normalization is explicit.

```python
"""Recover the complete VQ20 C622 FULL76 sources from nine journal payloads."""
import base64, hashlib, json, lzma, sys
from pathlib import Path
assert __debug__, 'Assertions must be enabled'
assert len(sys.argv)==3, 'Usage: RECOVER_C622_PARTS.py PARTS_DIRECTORY NEW_SOURCE_DIRECTORY'
root=Path(sys.argv[1]); out=Path(sys.argv[2])
expected=[
'e276a6a9de0724cc7f360be8f8c995db7af9c8b148435daa14d2335c984fb5ce',
'd28d6a47d0c76f30be99c0a925527609c31476e5dfe12e9b5be551ce7ca573df',
'59208221d1384a3f8cdd8aa3889348eb27f9d4749108be90c33c252006848f90',
'63443ee222ddc79a82c8d9980d1b21982302f9f5a3baac118ccf406eed8a10cf',
'018db45bc9e8dda0d6f7a1fc9bc7f2e8de0725143da1eeafa7f99ca00eb90d9e',
'351f37c4737f2dcfa6423f59983135b691fd30b80aee8a566e1783eefabae773',
'c4303b862425f6ba2a07e3803dd0c74ac2cd93adddeb75a68aa9391f3e1fc6f4',
'278d9841919cc9de242db8868715d20bec7ac1deabe95800dc610ae412bde2f5',
'83298c1cb9f692ad52da1da248904e27492c506f3a02687867f290d418b6b05b']
sha=lambda b:hashlib.sha256(b).hexdigest()
parts=[]
for i,h in enumerate(expected,1):
 s=''.join((root/f'C622_CAPSULE_{i:02d}.b85').read_text(encoding='ascii').split()).encode('ascii')
 assert len(s)==(10000 if i<9 else 8685) and sha(s)==h,(i,len(s),sha(s))
 parts.append(s)
encoded=b''.join(parts)
assert len(encoded)==88685 and sha(encoded)=='56bb46a476d35128b4743224c5f015d13f38d99d50e319f9bef871878350cd94'
data=lzma.decompress(base64.b85decode(encoded))
assert len(data)==312622 and sha(data)=='617f94b82a54bf54cd7cce67fbf5d506cc3d2b9431a7c64b587984ea429992f6'
files=json.loads(data);assert len(files)==76
assert sha(files['MANIFEST.json'].encode())=='d06bc3d5782b4ebf2449b4bd89e962ce88f08faca9d06ae068a5bfaf22af0c53'
assert not out.exists();out.mkdir(parents=True)
for name,text in files.items():
 rel=Path(name);assert not rel.is_absolute() and '..' not in rel.parts
 p=out/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode('utf-8'))
print('VQ20_C622_NINE_PART_FULL76_SOURCE_RECOVERY_PASS')
```

## Reconstruction and inherited verification

For deterministic extraction of the nine input files, read the literal-parts material as UTF-8, collect `re.findall(r'```text\s*\n(.*?)\n```', text, re.S)` in order, assert exactly9, and write each capture plus a newline to its numbered .b85 input. No source-coordinate row or parameter is omitted by this extraction. Do not use the headings as base85 characters.

Commands, with absent destination directories:

```sh
python -B -S RECOVER_C622_PARTS.py PARTS_DIRECTORY NEW_SOURCE_DIRECTORY
cd NEW_SOURCE_DIRECTORY
python -B -S REPLAY.py --out NEW_PROOF_DIRECTORY
```

The historical journal records observed markers VQ20_C622_NINE_PART_FULL76_SOURCE_RECOVERY_PASS and VQ20_C622_TWO_INDEPENDENT_EXACT_AUDITS_COLD_SOURCE_ONLY_PASS. The latter aggregate was68a6790514a48284af603bdacaf1d6cce63e141026a5abef7b0629acb1c03432; RECEIPT.json10859bytes. These are inherited completed observations, not claimed executions by the present coordinator. The source replay reconstructs the finite bodies and executes fresh independent A/B audits, third centred mass, contacts/stress/connectivity and negative fixtures rather than merely comparing cached output.

Original proof runtime: CPython3.13.5 standard library with assertions enabled. Numerical proposal runtime: NumPy2.3.5, SciPy1.17.0, one BLAS/OMP thread. p54's later stress discovery additionally used JAX0.9.0.1.

Accepted C622 generator11841bytes SHA-256 3cbd90d799189108f26b941800c8fa79a6f1c5abb17b2db614f0e54f57fffee7. Its independently identical A/B record311825bytes SHA-256 142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0. Actual176/311/137,own110/weak000,Sinput3,Urawlex94.

## Later continuation dependency

The fully read immutable worker result **figure-0380**, SHA-256 522bb3deeabb87145caf7dc68e421bddc9fcf832d99015b966781c85ca8df7aa, contains the complete later55-file delta, its decoder VQ20_E310_DELTA_RECOVER.py, all later finite inputs/checkpoints, and exact commands. It must be passed as an explicit parent for a descendant using that result, not replaced by this companion. The FULL76 sources above are the delta's unchanged BASE dependency.

The delta312? correction: its exact decoded55-source map is292419 bytes, SHA-256 458a5833199edaee4534a6f3368eefa49520b6edbcac2dc1ec8efbaa9cb3ea40; the normalized base85 length is67205, SHA-256 44d4d9ee47692c071086fce98e7dcf1fc88a6dcc46da8543067f1b0d5f867eb2. FULL76's312622-byte count must not be assigned to this delta.

The later C622_HOMOTOPY_POSITIVE is a distinct exact same-complex body with actual176/311/137 own110/weak000, target physical edge between owners(13,26,68) and(13,37,42,68) shortened but NOT removed. Its complete315 hex-parameter continuation checkpoint resides in the p54 delta. It is not a C<622 endpoint. The C614/C616 nonwinners use a different cleaned136-support index domain. Keep those identities separate.
