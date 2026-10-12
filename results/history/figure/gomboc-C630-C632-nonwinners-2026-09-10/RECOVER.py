"""Recover exact nonwinner definitions from the complete saved journal capsule."""
from pathlib import Path
import base64, hashlib, json, lzma, re, shutil

root = Path(__file__).resolve().parent
note = root.parent/'research-results-2026-09-09/figure-C630-C632-nonwinners-20260910-0855.md'
blocks = re.findall(r'```[^\n]*\n(.*?)\n```', note.read_text(), re.S)
encoded = next(''.join(b.split()) for b in blocks if len(''.join(b.split())) == 9090)
assert hashlib.sha256(encoded.encode()).hexdigest() == 'de66c1f08e3730c3ef271177f022000c10c52c44fba24e0e79fede8ee2f018de'
raw = lzma.decompress(base64.b85decode(encoded))
assert len(raw) == 23752
assert hashlib.sha256(raw).hexdigest() == '7ca0ac9c66ac744a8590eb24fb0fab7c0394fd65c5079077063eb5fe60cfbf5b'
data = json.loads(raw)
expected = {
    'C630_COORD_NONWINNER_OWN121': (11889,'412543caed98f81b5a250301ecd5c44d779f084cb2a1dcea475a7e7ecd1d7e7b'),
    'C632_COORD_NONWINNER_OWN121': (11800,'fe60d84225c723c8d6f046602b01a082c414f44fa0744244edf27d4620f29a64'),
}
assert set(data) == set(expected)
assert not (root/'generators.json').exists(), 'Already recovered; do not overwrite'
for name,obj in data.items():
    blob = json.dumps(obj,sort_keys=True,separators=(',',':')).encode()
    size,sha = expected[name]
    assert len(blob) == size and hashlib.sha256(blob).hexdigest() == sha
    destination = root/name
    destination.mkdir()
    (destination/'GENERATOR.json').write_bytes(blob)
    print(name, size, sha, 'GENERATOR_AUTHENTICATED', flush=True)
(root/'generators.json').write_bytes(raw)
parent = root.parent/'gomboc-C634-2026-09-10/source-only/audit'
for filename in ['RECONSTRUCT.py','check_A.py','check_B.py']:
    shutil.copyfile(parent/filename,root/filename)
