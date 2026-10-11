"""Materialize the authenticated C746 journal capsule, without executing its contents."""
import base64, hashlib, json, lzma, re
from pathlib import Path
root = Path(__file__).resolve().parent
journal = Path('/REDACTED_HOME/.pro-research/runs/run_-kjrDuYVMzeTQ9tyWn464e75/research-journal.md').read_text()
entry = journal[journal.index('## 2026-09-09T05:20:55.894Z'):].split('\n## 2026-', 1)[0]
blocks = re.findall(r'^\x60\x60\x60text\n(.*?)^\x60\x60\x60\s*$', entry, re.M | re.S)
assert len(blocks) == 1
blob = lzma.decompress(base64.b85decode(''.join(blocks[0].split())))
assert len(blob) == 36076 and hashlib.sha256(blob).hexdigest() == '53d5b7225c08d603f5067d62086f597726c7b3a80a531b2235511b503f11d55e'
parts = json.loads(blob)
assert parts == json.loads((root/'source-map.json').read_text())
assert set(parts) == {'RAW.json','REPLAY.py','audit_A.py','audit_B.py','dual_A.py','dual_B.py','exact_extra.py'}
(root/'source').mkdir()
pins = {}
for name, text in parts.items():
    assert Path(name).name == name
    data = text.encode('utf-8')
    with (root/'source'/name).open('xb') as f: f.write(data)
    pins[name] = {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
with (root/'source-manifest.json').open('x') as f: f.write(json.dumps(pins, indent=2)+'\n')
with (root/'COORDINATOR_HANDOFF.md').open('x') as f: f.write(entry)
with (root/'capsule-original.json').open('xb') as f: f.write(blob)
raw = json.loads(parts['RAW.json'])
assert raw['D'] == 100000000 and len(raw['I']) == 140 and raw['scale'] == 1
print(json.dumps({'sourcePins':pins,'D':raw['D'],'normals':len(raw['I']),'scale':raw['scale']},indent=2))
