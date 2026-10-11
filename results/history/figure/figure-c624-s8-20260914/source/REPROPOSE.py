"""Replay the finite numerical discovery; exact acceptance is REPLAY.py, not this.
Dependencies used: CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, one BLAS thread.
"""
import argparse,hashlib,json,os,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parent
import REPLAY
p=argparse.ArgumentParser();p.add_argument('--out',required=True,type=Path);a=p.parse_args();out=a.out.resolve();out.mkdir(parents=True,exist_ok=False)
REPLAY.sources()
env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONHASHSEED='0')
def call(name,*args):
 with (out/(name+'.log')).open('w') as f:subprocess.run([sys.executable,'-B',str(R/name),*map(str,args)],stdout=f,stderr=subprocess.STDOUT,env=env,check=True,timeout=90)
def check(path,expected):
 b=path.read_bytes();assert REPLAY.meta(b)==expected,(str(path),REPLAY.meta(b),expected)
call('combine.py',R,out/'seed',2)
call('repair_parent.py',R,out/'seed',out/'G14',5e-8,.03,40,30)
check(out/'G14/GENERATOR.json',REPLAY.meta((R/'G14_GENERATOR.json').read_bytes()))
call('repair_stronger.py',R,out/'seed',out/'STRONG_G14',1e-6,.03,40,30)
check(out/'STRONG_G14/GENERATOR.json',REPLAY.meta((R/'STRONG_G14_GENERATOR.json').read_bytes()))
(out/'G9').mkdir();(out/'G9/GENERATOR.json').write_bytes(REPLAY.canon(REPLAY.generator('G9')));(out/'G9/faces.json').write_bytes((out/'seed/faces.json').read_bytes())
call('integer_patch.py',R,out/'G9',out/'G9P')
expected=json.loads((R/'EXPECTED.json').read_text())
check(out/'G9P/GENERATOR.json',expected['G9P']['files']['GENERATOR.json'])
assert REPLAY.meta(REPLAY.canon(REPLAY.generator('S8')))==expected['S8']['files']['GENERATOR.json']
rec={'status':'C624_NUMERICAL_SOURCE_REPROPOSAL_IDENTICAL','G14':REPLAY.meta((out/'G14/GENERATOR.json').read_bytes()),'STRONG_G14':REPLAY.meta((out/'STRONG_G14/GENERATOR.json').read_bytes()),'G9P':REPLAY.meta((out/'G9P/GENERATOR.json').read_bytes()),'S8':expected['S8']['files']['GENERATOR.json'],'exact_acceptance':'Run REPLAY.py separately; this numerical receipt is not a certificate.'}
(out/'REPROPOSAL_RECEIPT.json').write_bytes(REPLAY.canon(rec));print(rec['status'])
