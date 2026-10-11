"""Replay the complete finite C486 numerical search suite, not an exact proof.
Usage: OPENBLAS_NUM_THREADS=1 python REPLAY_NUMERICS.py AFFINE_METHOD R12_A C592_A C602_A NEW
The exact input audits must be regenerated from the already preserved source-only capsules.
"""
import hashlib,json,os,subprocess,sys
from pathlib import Path
import numpy as np,scipy
assert __debug__
assert sys.version_info[:3]==(3,13,5) and np.__version__=='2.3.5' and scipy.__version__=='1.17.0'
assert os.environ.get('OPENBLAS_NUM_THREADS')=='1'
SHA=lambda b:hashlib.sha256(b).hexdigest()
def main():
 affine,r12,c592,c602,out=map(Path,sys.argv[1:]);here=Path(__file__).resolve().parent
 for n,v in json.loads((here/'MANIFEST.json').read_bytes()).items():
  b=(here/n).read_bytes();assert len(b)==v['bytes'] and SHA(b)==v['sha256']
 assert SHA((affine/'REPLAY_AFFINE334.py').read_bytes())=='ec205eccb50fd705f71703f4ac35fc4d6f5f0ee13ee871b512652b8e42d3a359'
 out.mkdir(parents=True,exist_ok=False)
 jobs=[('projective_metric_screen.py',[r12,out/'projective_metric_screen.json']),('augmented_metric_screen.py',[c592,r12,out/'projective_metric_screen.json',out/'augmented_metric_screen.json']),('spiral_bridge_screen.py',[c592,c602,out/'spiral_bridge_screen.json']),('centred_bridge_scan.py',[c592,c602,out/'centred_bridge_scan.json']),('primal334_delete_screen.py',[r12,out/'primal334_delete_screen.json'])]
 env=dict(os.environ,PYTHONPATH=str(affine.resolve()),OPENBLAS_NUM_THREADS='1')
 expected=json.loads((here/'EXPECTED.json').read_bytes())
 for name,args in jobs:
  subprocess.run([sys.executable,str(here/name),*map(str,args)],env=env,check=True)
  file=args[-1];b=file.read_bytes();v=expected[file.name]
  assert len(b)==v['bytes'] and SHA(b)==v['sha256'],(file.name,len(b),SHA(b),v)
  print('NUMERICAL_FINITE_SCREEN_OUTPUT_MATCH',file.name,flush=True)
 print('C486_FIVE_NUMERICAL_SCREENS_SOURCE_ONLY_BITWISE_REPLAY_PASS',flush=True)
if __name__=='__main__':main()
