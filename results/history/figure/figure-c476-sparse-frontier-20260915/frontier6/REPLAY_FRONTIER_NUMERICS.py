"""Full six-method finite replay, each process single-threaded.
Usage: python REPLAY_FRONTIER_NUMERICS.py OLD_NUMERIC_SOURCE AFFINE_SOURCE R12_A C602_A C476_BEFORE_A NEW_DIRECTORY
Restore inputs only from the already journaled CORE/C592/R12/AFFINE/DELETE capsules.
BEFORE_A is produced by CORE/check_A.py on the deletion replay's BEFORE/raw.json.
"""
import json,hashlib,os,sys,subprocess
from pathlib import Path
import numpy,scipy,torch
assert __debug__
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main(old,aff,r12,c602,before,out):
 here=Path(__file__).resolve().parent
 assert sys.version.split()[0]=='3.13.5' and numpy.__version__=='2.3.5' and scipy.__version__=='1.17.0' and torch.__version__=='2.10.0+cpu'
 for n,s in json.loads((here/'MANIFEST.json').read_bytes()).items():
  p=here/n;assert p.stat().st_size==s['bytes'] and sha(p)==s['sha256']
 for p,h in [(old/'projective_metric_screen.py','5b679e19c75a6fc0d5237b389e5ccf16254de97cbf88706d3fdf086b6249bb12'),(old/'primal334_delete_screen.py','b715d70309c91b2fd6c2ca3447276491b4d0f208fd85bcda8fb8c512a6e8c33d'),(aff/'REPLAY_AFFINE334.py','ec205eccb50fd705f71703f4ac35fc4d6f5f0ee13ee871b512652b8e42d3a359'),(r12,'8ee12742068e4246b3b7daf688703b3ce6f1c9803202a7d05f96e3ad8806ac21'),(c602,'2426da394eda9520bd30b2b8b3e1f00d043697353bb6bc73658f5983653c11ec'),(before,'9918f3cb6a779b46c3817cc8fdbb5d36a8e12e242f2e98f33c747e99bdfe2681')]:assert sha(p)==h
 out.mkdir(parents=True,exist_ok=False)
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONPATH=os.pathsep.join(map(str,[here,old.resolve(),aff.resolve()])))
 specs=[('metric476_screen',before),('critical476_primal_screen',before),('simplicial105_autodiff_screen',c602),('physical_triangle105_screen',c602),('budget105_delete_beam',r12),('facet105_delete_beam',c602)]
 running=[]
 for name,src in specs:
  log=(out/(name+'.log')).open('w');p=subprocess.Popen([sys.executable,str(here/(name+'.py')),str(src.resolve()),str((out/(name+'.json')).resolve())],stdout=log,stderr=subprocess.STDOUT,env=env);running.append((name,p,log));print('REPLAY_STARTED',name,flush=True)
 errors=[]
 for name,p,log in running:
  rc=p.wait();log.close()
  if rc:errors.append((name,rc))
 assert not errors,errors
 for n,s in json.loads((here/'EXPECTED.json').read_bytes()).items():
  p=out/n;assert p.stat().st_size==s['bytes'] and sha(p)==s['sha256'],n
 print('SIX_SPARSE_FRONTIER_NUMERICAL_METHODS_COLD_BITWISE_REPLAY_PASS',flush=True)
if __name__=='__main__':main(*map(Path,sys.argv[1:]))
