#!/usr/bin/env python3
"""Verify the files supplied in the Git checkout; this is not a math proof."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'MANIFEST.json').read_text())
failures = []
for row in manifest['files']:
    path = ROOT / row['path']
    if not path.is_file():
        failures.append('missing: ' + row['path'])
        continue
    with path.open('rb') as f:
        sha = hashlib.file_digest(f, 'sha256').hexdigest()
    if sha != row['sha256'] or path.stat().st_size != row['bytes']:
        failures.append('changed: ' + row['path'])
known = {row['path'] for row in manifest['files']} | {'MANIFEST.json'}
optional_data = {row['path'] for row in (json.loads(line) for line in (ROOT / 'catalog/files.jsonl').read_text().splitlines())}
for path in ROOT.rglob('*'):
    rel = path.relative_to(ROOT)
    if not path.is_file() or rel.parts[0] in {'.git', '_work', '_downloads'} or '__pycache__' in rel.parts or path.suffix == '.pyc' or path.name == '.DS_Store':
        continue
    if len(rel.parts) > 1 and rel.parts[0] == 'C622' and rel.parts[1].startswith('fresh-proof'):
        continue
    name = rel.as_posix()
    if name not in known and name not in optional_data:
        failures.append('unmanifested: ' + name)
if failures:
    raise SystemExit('\n'.join(failures))
print(len(manifest['files']), 'release files match the manifest.')
