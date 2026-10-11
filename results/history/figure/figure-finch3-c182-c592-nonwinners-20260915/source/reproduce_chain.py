"""Numerical re-proposal from the literal chosen global8-coordinate checkpoint.
Exact frozen generators are authoritative if floating-library details differ."""
import os,sys,json,subprocess,hashlib
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parent;os.chdir(ROOT);os.environ['OPENBLAS_NUM_THREADS']='1'

def command(args,env=None):
 print('RUN',args,flush=True);subprocess.run([sys.executable,*args],check=True,env=env)
def quantize(src,dst,grid):
 G=json.load(open(src));D=G['grid'];G['grid']=grid;G['controls']=[[round(F(v*grid,D)) for v in p] for p in G['controls']];Path(dst).write_text(json.dumps(G,sort_keys=True,separators=(',',':')));return G
if __name__=='__main__':
 command(['-B','-S','prepare_input.py']);command(['model.py']);command(['rechart.py','GLOBAL_ROW102.json','ATLAS1','--row','0']);env=dict(os.environ,MODEL_GENERATOR=str(ROOT/'ATLAS1_GENERATOR.json'),MODEL_META=str(ROOT/'ATLAS1_META.json'));command(['regularize.py','--tag','GREG1','--floor','1e-7','--steps','12'],env);command(['make_radial.py','RADIAL_GLOBAL','--start','GREG1.npy'],env);command(['implicit.py','--tag','IMPGLOBAL','--start','RADIAL_GLOBAL.json','--steps','50','--mu','1e-11']);G=quantize('IMPGLOBAL_GENERATOR.json','IMPGLOBAL_GENERATOR_G6.json',10**6)
 import quotient
 H=quotient.build(G,True,True,.5);Path('QUOT_11_1.json').write_text(json.dumps(H,sort_keys=True,separators=(',',':')));quantize('QUOT_11_1.json','QUOT_11_1_G6.json',10**6)
 expected=json.load(open('CASES.json'));want=expected['C592_OWN222_GRID6']['generator_info']['sha256'];got=hashlib.sha256(Path('QUOT_11_1_G6.json').read_bytes()).hexdigest();print('NUMERICAL_REPROPOSAL_HASH',got,'expected',want,'identical',got==want,flush=True)
