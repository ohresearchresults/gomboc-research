"""Replay the exact successful BQ13-to-double-contact numerical construction.
Usage: reproposal.py BQ13_SOURCE C626_EXACT_SOURCE fresh_output
BQ13_SOURCE is the literal 27-file parent capsule's extracted directory.
"""
import hashlib,json,os,subprocess,sys
from pathlib import Path
base,exact,out=map(lambda s:Path(s).resolve(),sys.argv[1:])
out.mkdir(parents=True,exist_ok=False)
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',BQ13_SOURCE=str(base))
# New helper sources accompany this unit; unchanged numerical engines are parent sources.
for name in ['make_double.py','coarsen.py']:
 text=(Path(__file__).resolve().parent/name).read_text()
 (out/name).write_text(text)
def run(*args):subprocess.run([sys.executable,'-B',*map(str,args)],env=env,check=True)
run(out/'make_double.py','--root',base/'C628_WINNER','--out',out/'seed','--axis','2')
run(base/'repair_fixed.py','--source',out/'seed','--out',out/'repair','--goal','1e-6','--trust','.03','--seconds','30','--steps','40')
run(out/'coarsen.py',out/'repair',out/'coarse')
for key,p in [('G14',out/'repair/GENERATOR.json'),('G8',out/'coarse/G8/GENERATOR.json')]:
 b=p.read_bytes();want=(exact/key/'GENERATOR.json').read_bytes()
 if b!=want:raise RuntimeError('Numerical replay differs from certified exact '+key+'; do not accept without new exact audits')
 print('NUMERICAL_REPROPOSAL_IDENTICAL',key,len(b),hashlib.sha256(b).hexdigest(),flush=True)
print('C626_NUMERICAL_PARENT_TO_IDENTICAL_G14_AND_G8_PASS')
