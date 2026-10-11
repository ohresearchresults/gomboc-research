"""Compact exact data: per-node denominators and 314-coordinate frozen vectors.
Every recovered positive control is exactly nearest to its literal S8 rechart value.
Search is not rerun to define these finite rational bodies.
"""
import json
from pathlib import Path
import exact57,rational56
ROOT=Path(__file__).resolve().parent
def from_free(plan_source,spec):
 z=json.loads(json.dumps(plan_source));z.pop('denominators',None);z['grid']=spec['grid'];z['controls']=[[0]*3 for _ in z['controls']];z['controls'][z['n_supports']]=[0,0,z['grid']];it=iter(spec['free_controls'])
 for i,dd,aa in z['plan']:
  for k in range(3):
   if k not in aa:z['controls'][i][k]=next(it)
 assert next(it,None) is None
 return z
def denominators(z,Ds):
 X=rational56.points(z);assert len(Ds)==len(X) and all(isinstance(D,int) and D>0 for D in Ds);z=json.loads(json.dumps(z));z.pop('grid',None);z['denominators']=Ds;z['controls']=[[0]*3 for _ in X];z['controls'][z['n_supports']]=[0,0,1]
 for i,dd,aa in z['plan']:
  for k in range(3):
   if k not in aa:z['controls'][i][k]=round(Ds[i]*X[i][k])
 return z
def generator(name):
 d,fs=exact57.source();D=json.loads((ROOT/'CONTROL_DATA.json').read_bytes())
 if name=='S8_D3':return denominators(exact57.manual(d),D[name]['denominators'])
 if name in ['S8_CORE4','S8_D2']:
  z=exact57.general(d,fs)
  if name=='S8_D2':z=exact57.core_free(z)
  return denominators(z,D[name]['denominators'])
 leaf,lf=exact57.leaf622(d,fs)
 if name=='C622_SEED':return leaf
 if name=='PRE_RECHART':return from_free(leaf,D[name])
 # The same general chart order and axes apply at the seed and frozen endpoint.
 z=from_free(exact57.general(leaf,lf),D['C622_IMPROVED'])
 if name=='C622_IMPROVED':return z
 if name in ['C622_D2_G9','C622_D2_G10']:return exact57.round_core_free(z,10**(9 if name.endswith('G9') else 10))
 if name=='C622_D2_ADAPT':return denominators(exact57.core_free(z),D[name]['denominators'])
 raise KeyError(name)
