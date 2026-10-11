"""Recover the exact S8 input from its complete six-part source capsule.
Usage: python -B -S REPLAY_INPUT.py S8_SOURCE S8_RAW_COMPLEX.json
No third-party modules. Assertions must be enabled.
"""
from pathlib import Path
import hashlib,json,sys
if not __debug__:
    raise RuntimeError('Assertions must be enabled')
sys.set_int_max_str_digits(0)
source=Path(sys.argv[1]).resolve()
out=Path(sys.argv[2])
if out.exists():
    raise FileExistsError(out)
sys.path.insert(0,str(source))
import REPLAY,RECONSTRUCT,check_A
REPLAY.sources()
a=check_A.run(RECONSTRUCT.recover(REPLAY.generator('S8')))
REPLAY.validate(a,'S8')
data=dict(vertices=a['raw_vertices'],faces=a['faces'],true_edges=a['edges'])
b=json.dumps(data,sort_keys=True,separators=(',',':')).encode()
assert len(b)==52119
assert hashlib.sha256(b).hexdigest()=='fa3affc96322660cd6409cb963bfbe2f4793c552b9e626f7463bb62f5bd26ab4'
out.write_bytes(b)
print('S8_EXACT_INPUT_FROM_SOURCE_PASS',len(b),hashlib.sha256(b).hexdigest(),flush=True)
