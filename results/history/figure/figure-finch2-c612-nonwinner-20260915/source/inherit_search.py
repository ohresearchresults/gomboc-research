"""Transfer the full exact-parent escape forest through contraction82--85.
Only the merged pre-existing defect remains a target; the old146 pair stays guarded.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse,json,time
from pathlib import Path
import numpy as np
from coupled import Model
from stratum_search import correct
from forest_search import freeze

def build(gen,report):
 P=Model(json.load(open('FINCH_SEQUENTIAL_GENERATOR.json')),json.load(open('FINCH_SEQUENTIAL_A.json')),forced={82:85});ap=P.eval(P.z0);pv,pf=P.select(ap)
 report=json.loads(json.dumps(report));report['stable_face_ids']=[report['active_input_indices'].index(3)]
 m=Model(gen,report,forced={})
 def owners(md):return [tuple(md.keep[np.where(row)[0]]) for row in md.inc]
 old=owners(P);new=owners(m);which={o:i for i,o in enumerate(new)};merge=which[tuple(sorted(set(old[82])|set(old[85])))];mapping={i:(merge if i in [82,85] else which[o]) for i,o in enumerate(old)}
 suc={int(P.vi[k]):int(P.vj[k]) for k in pv};suc[82]=85
 # Map each retained directed witness, skipping the disappearing arrow82->85.
 ids=[];floors={};ti=None
 for u,v in suc.items():
  if u==82:continue
  i,j=mapping[u],mapping[v];k=np.where((m.vi==i)&(m.vj==j))[0];assert len(k)==1;k=int(k[0])
  if i==merge:ti=k
  else:ids.append(k);floors[i]=float(P.vfloor[u])
 assert ti is not None;assert len(ids)==len(m.X0)-2
 m.targetU=[merge];m.target_idx=np.array([ti]);m.locked_v=np.array(ids)
 for i,v in floors.items():m.vfloor[i]=v
 orig_face={int(P.keep[P.normid[f]]):f for f in range(len(P.faces))}
 for f in range(len(m.faces)):
  i=orig_face[int(m.keep[m.normid[f]])]
  if f!=m.sface:m.ffloor[f]=P.ffloor[i]
 succ={int(m.vi[k]):int(m.vj[k]) for k in [*ids,ti]};m.basin=[]
 for v in range(len(m.X0)):
  seen=set();i=v;inbasin=False
  while i!=m.root:
   assert i not in seen;seen.add(i);inbasin|=i==merge;i=succ[i]
  if inbasin:m.basin.append(v)
 m.protected_old146=(mapping[146],mapping[147]);return m,mapping

def main():
 p=argparse.ArgumentParser();p.add_argument('--gen',default='CLOSED_EDGE1_GENERATOR.json');p.add_argument('--report',default='CLOSED_EDGE1_A.json');p.add_argument('--tag',default='INHERIT');p.add_argument('--start');p.add_argument('--steps',type=int,default=3);p.add_argument('--step',type=float,default=.002);p.add_argument('--beta',type=float,default=0);a=p.parse_args()
 m,mapping=build(json.load(open(a.gen)),json.load(open(a.report)));z=m.z0.copy() if a.start is None else np.load(a.start);step=a.step;logs=[];t0=time.time();e=m.eval(z)
 print('ENTRY',m.census(e),'target',m.targetU,e['vert'][m.target_idx], 'guardmin',m.constr(e).min(),'old146',m.protected_old146,flush=True)
 Path(a.tag+'_MAP.json').write_text(json.dumps(mapping,sort_keys=True))
 for it in range(a.steps):
  old=m.eval(z);level=np.minimum(2e-6,old['vert'][m.target_idx]+step)
  try:zz,b,ok,cor=correct(m,z,level,a.beta,limit=20)
  except (np.linalg.LinAlgError,FloatingPointError) as ex:ok=False;b=old;cor=[str(ex)]
  log=dict(iteration=it,accepted=ok,step=step,level=level.tolist(),target=b['vert'][m.target_idx].tolist(),cmin=float(m.constr(b).min()),g=b['g'].tolist(),volume=float(b['volume']),inner=cor,elapsed=time.time()-t0)
  if ok:z=zz;step=min(.006,step*1.25);np.save(a.tag+'.npy',z);freeze(m,z,a.tag+'_GENERATOR.json')
  else:step*=.5
  logs.append(log);Path(a.tag+'_TRACE.json').write_text(json.dumps(logs));print(json.dumps({k:v for k,v in log.items() if k!='inner'}),flush=True)
  if ok and b['vert'][m.target_idx].min()>1e-8:print('NUMERICAL_POSITIVE',m.census(b),flush=True);break
 print('FINISHED',m.census(m.eval(z)),flush=True)
if __name__=='__main__':main()
