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
    'A.json': (50575948,'a97d9952ef724f77b0fcaa3ba77bbb0fecad670266c35cd4d55092e172c65050'),
    'B.json': (50576039,'6cec8ed480cfb2582a1e75d984eacda90939b218bcee78ea384fa46eec24ff6f'),
    'EXTRA.json': (10329194,'088b31fa099638a1d1faf11bbdd229d6de66cb1cd9f0f3a907bae22944d7ee61'),
    'CONTROLS.json': (238,'479674e5f16dbcc973c77f202c6f054ec63da9c248aea5a93f2ae47c0d219fc0'),
    'SUMMARY.json': (937,'c776847c3c0b9ca66a3cb394a4be86ee9bc61daed63734f955e09149f1ce9d42'),
}
receipt = {'startedAt':started,'finishedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'elapsedSeconds':elapsed,'exitCode':result.returncode,'python':sys.version,'outputs':{},'accepted':False}
for filename,(size,digest) in expected.items():
    p=destination/filename
    receipt['outputs'][filename] = None if not p.exists() else {'bytes':p.stat().st_size,'sha256':sha(p),
        'matchesAuthor':p.stat().st_size==size and sha(p)==digest}
marker='COORD_FLOW_H140_C746_D100000000_TWO_INDEPENDENT_FULL_AUDITS_SUBLEVELS_FORESTS_CONTROLS_COLD_GOMBOC_PASS'
receipt['terminalMarkerPresent']=marker in (destination/'verification.log').read_text()
receipt['sourcesUnchanged']=all(sha(destination/f)==p['sha256'] for f,p in manifest.items())
receipt['accepted']=(result.returncode==0 and receipt['terminalMarkerPresent'] and receipt['sourcesUnchanged']
    and all(v and v['matchesAuthor'] for v in receipt['outputs'].values()))
(destination/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2),flush=True)
assert receipt['accepted'], 'Replay failed; inspect verification.log and receipt.json'
