"""Re-run the three recorded numerical experiments; exact audit remains separate."""
import os,sys,json,hashlib,subprocess,argparse
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
r=Path(__file__).resolve().parent;o=a.out.resolve();o.mkdir(parents=True,exist_ok=False)
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
def run(args):
 subprocess.run([sys.executable,'-B',*map(str,args)],check=True,env=env)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
run([r/'make_double.py','--root',r/'BASIN69_96','--out',o/'seed','--axis',2])
assert sha(o/'seed/GENERATOR.json')=='8057e4030d563b580ee714754a0b27b27d94373c01745a2a838c089f522a135b'
expected={'inherited':'cfa90753ea7a681d2f040ba120830bc8811d9fbfe139cad638d91e4b210a3514','naive':'0ec1013048527ca98e71b843de7918e69e48c553b4ee8006ca2a2ad42ef9e180','relaxed':'99df9dc29f728350668bce153a5534b2db7fa4acdbc5e7b74f555256c2f95a7d'}
for name in ['inherited','naive','relaxed']:
 run([r/('repair_'+name+'.py'),'--source',o/'seed','--out',o/name,'--goal','1e-6','--trust','.03','--seconds',28,'--steps',50])
 h=sha(o/name/'GENERATOR.json');assert h==expected[name],(name,h)
print('C624_METHOD_THREE_REPROPOSALS_MATCH')
