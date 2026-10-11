from pathlib import Path
import sys,subprocess,json,hashlib
assert not sys.flags.optimize
R=Path(__file__).resolve().parent
for folder,script in [('C650','REPLAY.py'),('PAIRS','RUN_PAIRS.py')]:
 subprocess.run([sys.executable,'-S',script],cwd=R/folder,check=True)
expected=json.loads((R/'FROZEN_ALL.json').read_text())
for name,(size,sha) in expected.items():
 b=(R/name).read_bytes();assert len(b)==size and hashlib.sha256(b).hexdigest()==sha,name
print('C650_AND_TWO_E323_NONWINNERS_SOURCE_ONLY_ALL_FIFTEEN_FROZEN_OUTPUTS_PASS',flush=True)
