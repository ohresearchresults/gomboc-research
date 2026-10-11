"""Preserve and integrity-check literal source transport; execute no research code."""
import ast
import base64
from datetime import datetime, timezone
import hashlib
import json
import lzma
from pathlib import Path, PurePosixPath
import re

root = Path(__file__).resolve().parent
parent = root.parent / 'figure-c624-s8-20260914'
d12 = root.parent / 'figure-s8-fixed-d12-exclusion-20260914'
def sha(data):
    return hashlib.sha256(data).hexdigest()
def check(data, size, digest):
    if len(data) != size or sha(data) != digest:
        raise ValueError('Source pin differs')
    return data
def decode(data, size, digest):
    dec = lzma.LZMADecompressor(memlimit=134217728)
    raw = dec.decompress(base64.b85decode(data), max_length=size + 1)
    if not dec.eof or dec.unused_data:
        raise ValueError('Unexpected compressed extent')
    return json.loads(check(raw, size, digest))
def verify_map(files, count, manifest_name):
    if not isinstance(files, dict) or len(files) != count:
        raise ValueError('Wrong source count')
    for name, text in files.items():
        rel = PurePosixPath(name)
        if not isinstance(text, str) or not rel.parts or rel.is_absolute() or '..' in rel.parts or '\\' in name or str(rel) != name:
            raise ValueError('Unsafe source path')
        if name.endswith('.py'):
            ast.parse(text, filename=name)
        elif name.endswith('.json'):
            json.loads(text)
    manifest = json.loads(files[manifest_name])
    if set(manifest) != set(files) - {manifest_name}:
        raise ValueError('Incomplete manifest')
    for name, pin in manifest.items():
        check(files[name].encode(), pin['bytes'], pin['sha256'])

observation = json.loads((root.parent / 'journal-materials-rollout-20260914-gye91I/figure-heartbeat-0829.json').read_text())
journal = Path('/REDACTED_HOME/.pro-research/runs/run_-kjrDuYVMzeTQ9tyWn464e75/research-journal.md').read_bytes()
snap = observation['journal']
if not snap['prefixPreserved'] or sha(journal[:snap['bytes']]) != snap['sha256']:
    raise ValueError('Canonical snapshot changed')
delta = snap['delta'].encode()
start = snap['bytes'] - len(delta)
if journal[start:snap['bytes']] != delta:
    raise ValueError('Journal delta differs')
sections = re.split(r'(?=^## Recovery capsule part \d/6 — COORD_S8_PRIMAL_COARSEN_METHODS_AND_NONWINNERS)', snap['delta'], flags=re.M)
sections = [s for s in sections if s.startswith('## Recovery capsule part')]
if len(sections) != 6:
    raise ValueError('Incomplete or duplicated parts')
digests = ['b87e8a75ff69eb4a3f4af5192ce33ac1ccae4d53a1e6a828b0835afd13229185', '4cc12e9dd252b9fa6a7e582307058f35edf111855ed4ec7bdb77ea8e015b254e', '89a009fa5a74a58ba254c57fddc69984474bbfe5999072c0522919b6b30860d8', 'dc32a1e5a68a9c82c5d6276cb1d6be4651ebb47371e020097d9b8a72f62e1441', 'b7e94d9d8af67fde5afeefefeca84fd26389eb538625d173c882f3a68c309a6b', '812c287ae02e8a01b5ab1e9b4a6e580e3d087498f4a929c02a162bbf56584b26']
chunks = []
for i, section in enumerate(sections, 1):
    if not section.startswith(f'## Recovery capsule part {i}/6 —'):
        raise ValueError('Part ordering differs')
    blocks = re.findall(r'^```text\n(.*?)^```\s*$', section, re.M | re.S)
    if len(blocks) != 1 or digests[i - 1] not in section:
        raise ValueError('Missing part pin or ambiguous block')
    chunks.append(check(''.join(blocks[0].split()).encode(), 8000 if i < 6 else 3065, digests[i - 1]))
capsule = check(b''.join(chunks), 43065, 'be898099f142dc8a7a5121ffdfb973db41dbc6004f32ba7561019361f50f2daa')
files = decode(capsule, 150446, 'd5aceb473245065e1b15f98fc0217dab2ed9549275e055558ccb68d4f50534a8')
verify_map(files, 22, 'MANIFEST.json')
decoders = re.findall(r'^```python\n(.*?)^```\s*$', sections[-1], re.M | re.S)
if len(decoders) != 1:
    raise ValueError('Ambiguous original decoder')
ast.parse(decoders[0], filename='restore_original.py')
parent_capsule = check((parent / 'SOURCE_CAPSULE.b85').read_bytes(), 59100, 'e3c07742531ebe37a1a3332748807c7154f5d7a9c669b57bb78612041dbd1c00')
dependencies = decode(parent_capsule, 170010, '44319c99762df191373664c4e89bbeb7fb70db771c7c38e0a19e4e0ea2645fd3')
verify_map(dependencies, 30, 'SOURCE_MANIFEST.json')
for name, text in dependencies.items():
    if (parent / 'source' / name).read_bytes() != text.encode():
        raise ValueError('Prior S8 dependency differs')
check((d12 / 'source/REPLAY_INPUT.py').read_bytes(), 990, '024c75cea48170dd77822f1647344849c60f909a0db1499f0d2e39c920fcda43')
payloads = {'journal-entries.md': delta, 'METHOD_CAPSULE.b85': capsule, 'restore_original.py': decoders[0].encode()}
payloads.update({'source/' + name: text.encode() for name, text in files.items()})
for name in [*payloads, 'integrity-receipt.json']:
    if (root / name).exists():
        raise FileExistsError(root / name)
for name, data in payloads.items():
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)
    check(path.read_bytes(), len(data), sha(data))
receipt = {
    'at': datetime.now(timezone.utc).isoformat(), 'identity': 'COORD_S8_PRIMAL_COARSEN_METHODS_AND_NONWINNERS',
    'events': [1223, 1224, 1225, 1226, 1227, 1228], 'completeSourcePreservedLocally': True,
    'journal': {'startByte': start, 'endByte': snap['bytes'], 'bytes': len(delta), 'sha256': sha(delta)},
    'capsule': {'base85Chars': len(capsule), 'base85Sha256': sha(capsule), 'decodedBytes': 150446, 'decodedSha256': 'd5aceb473245065e1b15f98fc0217dab2ed9549275e055558ccb68d4f50534a8'},
    'newSourceFiles': 22, 'parentSourceFiles': 30, 'parentDirectory': str(parent / 'source'), 'additionalDependency': str(d12 / 'source/REPLAY_INPUT.py'),
    'verification': 'All6 ordered parts, encoded/decoded pins, all21 new and29 old manifest pins, JSON parse/Python AST, exact30 parent file readbacks and990-byte D12 input-replay dependency checked. New archive readback passed. No research source executed or parent archive duplicated.',
    'localMathematicalOrNumericalReplay': False,
    'scope': 'Complete finite deletion proposer/full-case verifier,315-control actual-primal chart and optimizer versions, five exact rational checkpoint definitions. Author fully audited three C622 nonwinners: elastic2_D176 own65/64/127, elastic3_D147 own121, elastic3_D176 own121, allweak000. elastic2_D147 and elastic2_D84 have only numerical classifications. No lower-C Gomboc.',
    'limitations': 'Numerical discovery is time-limited/platform-dependent, not claimed bitwise reproducible. Literal rational endpoints are recoverable without optimizer replay. Legacy int64-overflow outputs excluded; legacy source retained to document failure. Smaller residual alone is not mechanical progress.',
    'files': {name: {'bytes': len(data), 'sha256': sha(data)} for name, data in payloads.items()},
}
with (root / 'integrity-receipt.json').open('x', encoding='utf-8') as stream:
    json.dump(receipt, stream, indent=2)
    stream.write('\n')
print(json.dumps({k: v for k, v in receipt.items() if k != 'files'}))
