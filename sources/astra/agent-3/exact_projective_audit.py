"""Exact physical embedding audit for polarity/projective-orbit nominations.
P maps homogeneous primal coordinates. The opposite support coordinates use
D P^{-T} D, D=diag(1,1,1,-1). Uniform mass is integrated after the map.
"""
import argparse,json,time,hashlib
from pathlib import Path
from math import lcm,gcd
import numpy as np
from gmpy2 import mpq
from exact_audit_vertices import check_B,dot

def inverse(A):
 n=len(A);B=[list(row)+[mpq(i==j) for j in range(n)] for i,row in enumerate(A)]
 for j in range(n):
  pivot=next((i for i in range(j,n) if B[i][j]!=0),None);assert pivot is not None,'singular literal embedding';B[j],B[pivot]=B[pivot],B[j];v=B[j][j];B[j]=[x/v for x in B[j]]
  for i in range(n):
   if i!=j:
    v=B[i][j];B[i]=[x-v*y for x,y in zip(B[i],B[j])]
 return [row[n:] for row in B]
def apply(A,v):return tuple(sum(x*y for x,y in zip(row,v)) for row in A)
def audit(folder,out):
 folder=Path(folder);out=Path(out);out.mkdir(parents=True,exist_ok=False);meta=json.loads((folder/'source.json').read_text());raw=Path(meta['audit_path']).read_bytes();assert hashlib.sha256(raw).hexdigest()==meta['audit_sha256'];a=json.loads(raw);e=np.load(folder/'embedding.npz');P=[[mpq(float(v)) for v in row] for row in e['P']];b=int(e['dual']);assert b in [0,1];X=[tuple(mpq(v) for v in row) for row in a['raw_vertices']];Q=[tuple(mpq(v)/mpq(h) for v in row) for row,h in zip(a['normals'],a['offsets'])]
 if b:X,Q=Q,X
 I=inverse(P);sg=[1,1,1,-1];PD=[[sg[i]*I[j][i]*sg[j] for j in range(4)] for i in range(4)];xx=[apply(P,(*v,mpq(1))) for v in X];qq=[apply(PD,(*v,mpq(1))) for v in Q];assert all(v[-1]>0 for v in xx+qq);Y=[tuple(t/v[-1] for t in v[:3]) for v in xx];rows=[]
 for v in qq:
  den=lcm(*(int(t.denominator) for t in v));row=[int(t*den) for t in v];d=gcd(*row);rows.append([t//d for t in row])
 assert all(dot(row[:3],y)<=row[3] for row in rows for y in Y)
 B=lambda v:json.dumps(v,default=str,sort_keys=True,separators=(',',':')).encode();(out/'base_audit.json').write_bytes(raw);(out/'embedding.json').write_bytes(B(dict(P=P,dual=b,D=sg,relationship='physical vertices=P*[x,1] divided by fourth coordinate; support coordinates=D*P^(-T)*D*[q,1]',density='uniform in this single physical embedding')));(out/'coordinates.json').write_bytes(B(dict(points=Y)));H={'H':rows};(out/'raw.json').write_bytes(B(H));t=time.time();rep=check_B.run(H);assert {tuple(mpq(v) for v in v) for v in rep['raw_vertices']}==set(Y);assert rep['E']==a['E'];assert rep['V']==(a['F'] if b else a['V']);assert rep['F']==(a['V'] if b else a['F']);(out/'audit.json').write_bytes(B(rep));su={k:rep[k] for k in ['V','E','F','counts','weak','stable_face_ids','unstable_vertices','saddle_edges','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};su.update(C=2*rep['E'],seconds=time.time()-t,goal_met=rep['counts']==[1,1,0] and rep['weak']==[0,0,0] and 34<=2*rep['E']<500);su['files']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir()};(out/'summary.json').write_text(json.dumps(su,indent=2))
 su['C_2E']=2*rep['E'];su['VplusEplusF']=rep['V']+rep['E']+rep['F'];su['goal_met']=su['goal_met']and su['VplusEplusF']<500
 (out/'summary.json').write_text(json.dumps(su,indent=2))
 print('EXACT_PROJECTIVE',out,{k:su[k]for k in ['V','E','F','C_2E','VplusEplusF','counts','weak','goal_met']},flush=True)
 if su['goal_met']:(out/'GOAL_CANDIDATE_COMPLETE.json').write_text(json.dumps(su,indent=2))
 return rep
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');a=p.parse_args();audit(a.input,a.out)
