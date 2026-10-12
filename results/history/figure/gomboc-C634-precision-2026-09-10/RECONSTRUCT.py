"""Literal coordinator delta, exact integer rounding; no numerical search.
Run python3 -S RECONSTRUCT.py, then each variant's REPLAY.py.
The copied author auditors are the already authenticated C634 source capsule.
"""
from pathlib import Path
import hashlib, json, shutil

root = Path(__file__).resolve().parent
parent = root.parent / 'gomboc-C634-2026-09-10/source-only'
raw = (parent/'C634_SOC/GENERATOR.json').read_bytes()
assert hashlib.sha256(raw).hexdigest() == '09b77674fbf9877abcf35f5932d4d96fad25c855da1fefbcf1d71e7bd6d297c6'
source = json.loads(raw)
assert source['grid'] == 10**12
patches = [(158,0,1),(171,2,-1),(152,2,-1),(155,0,1),(155,2,1),(60,0,1)]
for name, grid, edits, expected, size in [
    ('C634_GRID9_COORD',10**9,[], 'f4b09033a0cee8f349a37fde3b605f257a3d534b066b4eb9e3f78b12361f6081',10103),
    ('C634_GRID8_MIP6_COORD',10**8,patches,'fcebe21a021047869a57c1d89f220c9ffd0c138f81e62cd8d9fd8841abff28bd',9567),
]:
    data = json.loads(raw)
    def nearest(v):
        q,r = divmod(v*grid,source['grid'])
        return q + int(2*r > source['grid'] or (2*r == source['grid'] and q%2 == 1))
    data['grid'] = grid
    data['controls'] = [[nearest(v) for v in row] for row in source['controls']]
    constrained = {i:set(axes) for i,deps,axes in data['plan']}
    for i,axis,delta in edits:
        assert axis not in constrained.get(i,set())
        data['controls'][i][axis] += delta
    blob = json.dumps(data,sort_keys=True,separators=(',',':')).encode()
    assert len(blob) == size and hashlib.sha256(blob).hexdigest() == expected
    destination = root/name
    assert not destination.exists(), 'Refusing to overwrite an existing variant'
    destination.mkdir()
    (destination/'GENERATOR.json').write_bytes(blob)
    meta = json.loads((parent/'C634_SOC/META.json').read_bytes())
    meta['tag'] = name
    (destination/'META.json').write_text(json.dumps(meta,sort_keys=True,separators=(',',':')))
    for filename in ['RECONSTRUCT.py','REPLAY.py','check_A.py','check_B.py','EXTRA.py']:
        shutil.copyfile(parent/'audit'/filename,destination/filename)
    print(name,size,expected, 'EXACT_GENERATOR_HASH_MATCH')
