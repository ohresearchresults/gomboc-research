"""Full exact physical audit of complete contact-plan coordinates and free controls."""
import argparse,json,hashlib,time
from pathlib import Path
from math import gcd,lcm
import numpy as np
from gmpy2 import mpq
from exact_projective_audit import inverse,apply
from exact_audit_vertices import check_B,dot,cross,sub

def audit(source,params,out,grid):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);meta=json.loads(Path(source).read_text());q=np.load(params);controls=[int(round(float(v)*grid)) for v in q];meta.update(free_controls=controls,grid=grid,source_q_path=str(Path(params).resolve()),source_q_sha256=hashlib.sha256(Path(params).read_bytes()).hexdigest());A=[(mpq(0),)*3 for _ in range(meta['nodes'])];t=time.time()
 for p in meta['plan']:
  x=[mpq(0)]*3
  for axis,v in p['fixed'].items():x[int(axis)]=mpq(v)
  for axis,i in zip(p['free_axes'],p['free_indices']):x[axis]=mpq(controls[i],grid)
  if p['deps']:
   M=[[A[j][axis] for axis in p['axes']] for j in p['deps']];b=[1-dot(A[j],x) for j in p['deps']];sol=apply(inverse(M),b)
   for axis,v in zip(p['axes'],sol):x[axis]=v
  A[p['node']]=tuple(x)
 F=meta['F'];Y=A[:F];X=A[F:];inc=[set(fc) for fc in meta['faces']]
 for f,n in enumerate(Y):
  for i,x in enumerate(X):
   gap=1-dot(n,x)
   if i in inc[f]:assert gap==0
   else:assert gap>0,'literal reconstruction is outside its strict contact chart'
  fc=meta['faces'][f]
  for k in range(1,len(fc)-1):assert dot(cross(sub(X[fc[k]],X[fc[0]]),sub(X[fc[k+1]],X[fc[0]])),n)>0
 B=lambda x:json.dumps(x,default=str,sort_keys=True,separators=(',',':')).encode();(out/'construction.json').write_bytes(B(meta));(out/'coordinates.json').write_bytes(B(dict(points=X,primal_supports=Y,density=1)));rows=[]
 for n in Y:
  den=lcm(*(int(v.denominator) for v in n));r=[int(v*den) for v in n]+[den];gg=gcd(*r);rows.append([v//gg for v in r])
 raw={'H':rows};(out/'raw.json').write_bytes(B(raw));rep=check_B.run(raw);assert {tuple(mpq(v) for v in row) for row in rep['raw_vertices']}==set(X);assert [rep[k] for k in ['V','E','F']]==[meta[k] for k in ['V','E','F']];(out/'audit.json').write_bytes(B(rep));su={k:rep[k] for k in ['V','E','F','counts','weak','stable_face_ids','unstable_vertices','saddle_edges','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};su.update(C_2E=2*rep['E'],VplusEplusF=rep['V']+rep['E']+rep['F'],seconds=time.time()-t,goal_met=rep['counts']==[1,1,0] and rep['weak']==[0,0,0] and 34<=2*rep['E']<500 and rep['V']+rep['E']+rep['F']<500);su['files']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir()};(out/'summary.json').write_text(json.dumps(su,indent=2));print('EXACT_CONTACT',out,{k:su[k] for k in ['V','E','F','C_2E','VplusEplusF','counts','weak','goal_met','seconds']},flush=True)
 if su['goal_met']:(out/'GOAL_CANDIDATE_COMPLETE.json').write_text(json.dumps(su,indent=2))
 return rep
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('construction');p.add_argument('params');p.add_argument('out');p.add_argument('--grid',type=int,default=10**14);a=p.parse_args();audit(a.construction,a.params,a.out,a.grid)
