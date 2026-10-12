"""Reproduce the three positive rational proposals and the controlled C622 method.
Source-only exact body replay is independent of all numerical stages.
"""
import argparse,json,os,subprocess,sys
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import exact57,rational56,simplify56,compress_chart56,factory57
ROOT=Path(__file__).resolve().parent

def enc(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def put(path,d,fs,meta=None):
 path.mkdir(parents=True,exist_ok=False);(path/'GENERATOR.json').write_bytes(enc(d));(path/'faces.json').write_bytes(enc(fs))
 if meta is not None:(path/'META.json').write_bytes(enc(meta))
def identical(path,name):
 d=json.loads(path.read_bytes());want=factory57.generator(name);assert rational56.points(d)==rational56.points(want)
 if name!='C622_IMPROVED':assert enc(d)==enc(want)
 print('NUMERICAL_REPROPOSAL_IDENTICAL_GEOMETRY',name,flush=True)
def run(stage,out):
 out.mkdir(parents=True,exist_ok=True);d,fs=exact57.source()
 if stage in ['S8_D3','S8_CORE4','S8_D2']:
  z=exact57.manual(d) if stage=='S8_D3' else exact57.general(d,fs)
  if stage=='S8_D2':z=exact57.core_free(z)
  seed=simplify56.build(z,np.array(rational56.points(z),float),1e-9);sp=out/(stage+'_seed');put(sp,seed,fs);op=out/stage
  compress_chart56.run(SimpleNamespace(source=sp/'GENERATOR.json',faces=sp/'faces.json',out=op,rounds=3,floor=6e-7,trust=1e-5,qmax=2000000,order='reverse'));identical(op/'GENERATOR.json',stage)
 elif stage in ['PREFIX7','CORRECT4','CORRECT6','FINAL4']:
  leaf,lf=exact57.leaf622(d,fs);meta=json.loads((ROOT/'C622_SEED/META.json').read_bytes());guard=out/'guard'
  if not guard.exists():put(guard,leaf,lf,meta)
  if stage=='PREFIX7':source=leaf;steps=7;trust=.003
  elif stage=='CORRECT4':source=json.loads((out/'PREFIX7/GENERATOR.json').read_bytes());steps=4;trust=.001
  elif stage=='CORRECT6':source=json.loads((out/'CORRECT4/GENERATOR.json').read_bytes());steps=6;trust=.001
  else:
   source=exact57.general(factory57.generator('PRE_RECHART'),lf);steps=4;trust=.001
  sp=out/(stage+'_source');put(sp,source,lf,meta);op=out/stage
  cmd=[sys.executable,'-B',str(ROOT/'corrected57.py'),'--src',str(sp),'--out',str(op),'--steps',str(steps),'--trust',str(trust)]
  if stage=='PREFIX7':cmd+=['--halvings','8','--correctors','10','--qp-seconds','2','--qp-steps','3000']
  else:cmd+=['--guard',str(guard)]
  subprocess.run(cmd,check=True,env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'))
  key={'PREFIX7':'C622_CORRECTED','CORRECT4':'C622_CORRECTED2','CORRECT6':'C622_CORRECTED3','FINAL4':'C622_RECHART_R'}[stage];e=json.loads((ROOT/'CHECKPOINT_HASHES.json').read_bytes())[key];b=(op/'GENERATOR.json').read_bytes()
  if stage=='FINAL4':identical(op/'GENERATOR.json','C622_IMPROVED')
  else:assert len(b)==e['bytes'] and exact57.hashlib.sha256(b).hexdigest()==e['sha256']
 elif stage=='ADAPT622':
  z=exact57.core_free(factory57.generator('C622_IMPROVED'));X=np.array(rational56.points(z),float);zz=json.loads(json.dumps(z));zz['controls']=[[0]*3 for _ in X];zz['denominators']=[1]*len(X);zz['controls'][137]=[0,0,1]
  for i,deps,aa in zz['plan']:
   rest=[k for k in range(3) if k not in aa];pp,D=simplify56.common_approx([X[i,k] for k in rest],1e-10,limit=1000000);zz['denominators'][i]=D
   for k,v in zip(rest,pp):zz['controls'][i][k]=v
  op=out/stage;put(op,zz,json.loads((ROOT/'FACES_C622.json').read_bytes()));identical(op/'GENERATOR.json','C622_D2_ADAPT')
 elif stage=='ROUND622':
  for k in [8,9,10]:
   z=exact57.round_core_free(factory57.generator('C622_IMPROVED'),10**k);op=out/('C622_D2_G'+str(k));put(op,z,json.loads((ROOT/'FACES_C622.json').read_bytes()))
   if k>8:identical(op/'GENERATOR.json','C622_D2_G'+str(k))
   else:
    from numeric import mechanics
    print('G8_NUMERICAL_NONWINNER',mechanics(np.array(rational56.points(z),float)[:137],json.loads((ROOT/'FACES_C622.json').read_bytes()),tol=1e-13)['counts'],flush=True)
 print('ATLAS57_NUMERICAL_STAGE_COMPLETE',stage,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--stage',choices=['S8_D3','S8_CORE4','S8_D2','PREFIX7','CORRECT4','CORRECT6','FINAL4','ADAPT622','ROUND622'],required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();run(a.stage,a.out)
