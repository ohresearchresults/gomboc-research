"""Regenerate all three frozen generators. Discovery requires NumPy2.3.5/SciPy1.17.0.
Floating proposals are never automatically promoted; exact frozen inputs dominate.
"""
import argparse,os,subprocess,sys,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);p.add_argument('--stage',choices=['adapt','shallow','small','strong','finish','all'],default='all');a=p.parse_args();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
def run(file,*args):subprocess.run([sys.executable,'-B',str(ROOT/file),*map(str,args)],cwd=ROOT,env=env,check=True)
if a.stage in ['adapt','all']:run('simplify56.py','--source',ROOT/'PARENT_G8.json','--faces',ROOT/'FACES.json','--eps','1e-8','--out',out/'adapt')
if a.stage in ['shallow','all']:run('rechart56.py','--source',ROOT/'PARENT_G8.json','--faces',ROOT/'FACES.json','--chosen',142,151,164,174,175,'--eps','1e-8','--out',out/'shallow')
for key,floor in [('small','4e-7'),('strong','5.2e-7')]:
 if a.stage in [key,'all']:run('compress_chart56.py','--source',out/'shallow/GENERATOR.json','--faces',ROOT/'FACES.json','--floor',floor,'--rounds',3,'--trust','1e-5','--qmax',2000000,'--order','reverse','--out',out/key)
if a.stage in ['finish','all']:
 for name,key in [('ADAPT','adapt'),('D3_SMALL','small'),('D3_STRONG','strong')]:
  b=(out/key/'GENERATOR.json').read_bytes();assert b==(ROOT/name/'GENERATOR.json').read_bytes(),name
  print('IDENTICAL_GENERATOR',name,len(b),hashlib.sha256(b).hexdigest(),flush=True)
 print('ATLAS56_NUMERICAL_REPROPOSAL_BYTE_IDENTICAL',flush=True)
