"""Fresh-directory exact replay; Python 3.11+, standard library, no optimization."""
import datetime, hashlib, json, shutil, subprocess, sys, time
from pathlib import Path

root = Path(__file__).resolve().parent
name = sys.argv[1] if len(sys.argv) > 1 else 'replay-1'
assert Path(name).name == name and name not in ('.', '..', 'source')
assert not sys.flags.optimize
manifest = json.loads((root/'source-manifest.json').read_text())
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
for filename, pin in manifest.items():
    assert Path(filename).name == filename
    p = root/'source'/filename
    assert p.stat().st_size == pin['bytes'] and sha(p) == pin['sha256'], filename
destination = root/name
shutil.copytree(root/'source', destination)
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
clock = time.monotonic()
print('START',name,started,flush=True)
with (destination/'verification.log').open('w') as log:
    result = subprocess.run([sys.executable,'-u','-S','REPLAY.py'],cwd=destination,stdout=log,stderr=subprocess.STDOUT)
elapsed = time.monotonic()-clock
expected = {
    'A.json': (36881582,'387353545245a0c6373863d50c0d326ece350aab7a9e035fb52c308157006fe2'),
    'B.json': (36881691,'5a804794121cf33ecc6930b1d2d3e236d61b5b37c9ea96ed267cffccaceddc7d'),
    'EXTRA.json': (7549613,'ce80422cf0eb306c5878e629d4affd51bf86068d2b69731e278e59d14877e48e'),
    'CONTROLS.json': (238,'479674e5f16dbcc973c77f202c6f054ec63da9c248aea5a93f2ae47c0d219fc0'),
    'SUMMARY.json': (939,'273ca2def67c9e6402d157767b76cf375e473e3657846feb7c3f5c1e77acb9cc'),
}
receipt = {'startedAt':started,'finishedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'elapsedSeconds':elapsed,'exitCode':result.returncode,'python':sys.version,'outputs':{},'accepted':False}
for filename,(size,digest) in expected.items():
    p=destination/filename
    receipt['outputs'][filename] = None if not p.exists() else {'bytes':p.stat().st_size,'sha256':sha(p),
        'matchesAuthor':p.stat().st_size==size and sha(p)==digest}
marker='COORD_H141_C752_D1000000_TWO_INDEPENDENT_FULL_AUDITS_SUBLEVELS_FORESTS_CONTROLS_COLD_GOMBOC_PASS'
receipt['terminalMarkerPresent']=marker in (destination/'verification.log').read_text()
receipt['sourcesUnchanged']=all(sha(destination/f)==p['sha256'] for f,p in manifest.items())
receipt['accepted']=(result.returncode==0 and receipt['terminalMarkerPresent'] and receipt['sourcesUnchanged']
    and all(v and v['matchesAuthor'] for v in receipt['outputs'].values()))
(destination/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2),flush=True)
assert receipt['accepted'], 'Replay failed; inspect verification.log and receipt.json'
