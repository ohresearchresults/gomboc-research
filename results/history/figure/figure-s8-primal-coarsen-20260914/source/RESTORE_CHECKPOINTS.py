"""Reconstruct exact normalized inputs; unused dependent controls are zero.
Usage: python -B -S RESTORE_CHECKPOINTS.py S8_SOURCE NEW_DIRECTORY
Only the 315 independent controls are stored. All dependent values are solved
exactly by the unchanged source plan. This changes generator bytes, not bodies.
"""
from pathlib import Path
import sys,json,hashlib
if not __debug__:raise RuntimeError('Assertions must be enabled')
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(Path(sys.argv[1]).resolve()))
import REPLAY,RECONSTRUCT
REPLAY.sources();out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
canon=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def meta(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
base=REPLAY.generator('S8');free=[(i,k)for i,deps,axes in base['plan']for k in range(3)if k not in axes];assert len(free)==315
(out/'S8_GENERATOR.json').write_bytes(canon(base));(out/'S8_H.json').write_bytes(canon(RECONSTRUCT.recover(base)))
data=json.loads((Path(__file__).parent/'CHECKPOINTS.json').read_text())
for name,spec in sorted(data.items()):
 g=json.loads(json.dumps(base));g['grid']=spec['grid'];g['controls']=[[0]*3 for row in g['controls']];assert len(spec['free_controls'])==len(free)
 for (i,k),v in zip(free,spec['free_controls']):g['controls'][i][k]=v
 b=canon(g);assert meta(b)==spec['normalized_generator'];raw=canon(RECONSTRUCT.recover(g));assert meta(raw)==spec['auxiliary_H']
 p=out/name;p.mkdir();(p/'GENERATOR.json').write_bytes(b);(p/'AUXILIARY_H.json').write_bytes(raw)
 for key,filename in [('config','CONFIG.json'),('incidence','INCIDENCE.json'),('expected_outputs','EXPECTED.json'),('exact_stats','EXACT_STATS.json'),('roundtrip','ROUNDTRIP.json'),('numerical','NUMERICAL.json')]:
  if key in spec:(p/filename).write_bytes(canon(spec[key]))
 print('EXACT_NORMALIZED_CHECKPOINT_RESTORED',name,meta(b),flush=True)
print('ALL_FIVE_EXACT_INPUTS_RESTORED',flush=True)
