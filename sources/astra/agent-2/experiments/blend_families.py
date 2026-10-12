"""Physically consistent 85-support blends of exact own121 and own211 seeds.
The halfspace set always defines the physical body, and its own volume centroid
is recomputed. Matching and interpolation are discovery operations only.
"""
from pathlib import Path
from fractions import Fraction
import json,sys,numpy as np
from scipy.optimize import linear_sum_assignment
from support_persistence import ROOT,complex_for,points,edge_graphs,barcode
from geometry import angular_scores

def centered(Y):
 ds,xm,tr,tm,ym=complex_for(Y);Z,Q=points(Y,ds,tr,tm)
 a,b,c=Z[tr[:,0]],Z[tr[:,1]],Z[tr[:,2]];vol=np.sum(np.einsum('ij,ij->i',a,np.cross(b,c))*tm)/6
 return Q*vol**(1/3),Z/vol**(1/3)

def record(Y):
 ds,xm,tr,tm,ym=complex_for(Y);Z,Q=points(Y,ds,tr,tm);eu,es=edge_graphs(ds,xm);bu,wu,p=barcode(Z,xm,eu);bs,ws,q=barcode(Q,ym,es)
 p=np.array([v/np.dot(Z[r[0]],Z[r[0]]) for r,v in zip(bu,p)])
 q=np.array([v/np.dot(Q[r[0]],Q[r[0]]) for r,v in zip(bs,q)])
 u=angular_scores(Z);u[:,xm==0]=-np.inf;s=angular_scores(Q);s[:,ym==0]=-np.inf
 return {'S':int(np.sum((s.max(axis=1)<0)&(ym>0))),'U':int(np.sum((u.max(axis=1)<0)&(xm>0))),'V':int(xm.sum()),'F':int(ym.sum()),'Pmax':float(max(p)),'Qmax':float(max(q)),'soft_loss':float(np.log1p(p/.03).sum()+np.log1p(q/.03).sum())}

if __name__=='__main__':
 out=ROOT/'artifacts/blend_families';out.mkdir(exist_ok=True)
 A=np.load(ROOT/'artifacts/kf27d_expanded/F85_caps_g3.npy')
 H=json.loads((ROOT/'sources/peer_agent1_A1_C492_FLOW_G14/H.json').read_text())['H'];B=np.array([[float(Fraction(x,r[3])) for x in r[:3]] for r in H])
 ds,xm,tr,tm,ym=complex_for(B);Z,Q=points(B,ds,tr,tm);esc=angular_scores(Z).max(axis=1);i=int(np.argmax(esc));B=np.r_[B,((B[ds[i]].mean(axis=0))*(1+1e-5))[None,:]]
 A,XA=centered(A);B,XB=centered(B)
 # First align each strongest physical/polar radial extremum by one rotation.
 src=np.array([XB[np.argmax(np.linalg.norm(XB,axis=1))],B[np.argmax(np.linalg.norm(B,axis=1))]])
 dst=np.array([XA[np.argmax(np.linalg.norm(XA,axis=1))],A[np.argmax(np.linalg.norm(A,axis=1))]])
 src/=np.linalg.norm(src,axis=1)[:,None];dst/=np.linalg.norm(dst,axis=1)[:,None]
 u,s,vt=np.linalg.svd(src.T@dst);fix=np.eye(3);fix[2,2]=np.linalg.det(u@vt);R=u@fix@vt;B=B@R
 da=A/np.linalg.norm(A,axis=1)[:,None];db=B/np.linalg.norm(B,axis=1)[:,None]
 cost=1-da@db.T+.03*(np.log(np.linalg.norm(A,axis=1))[:,None]-np.log(np.linalg.norm(B,axis=1))[None,:])**2
 rows,cols=linear_sum_assignment(cost);assert np.array_equal(rows,np.arange(len(A)));B=B[cols]
 np.save(out/'A_own121.npy',A);np.save(out/'B_own211.npy',B)
 meta={'A_source':'artifacts/kf27d_expanded/F85_caps_g3_H.json','B_source':'sources/peer_agent1_A1_C492_FLOW_G14/H.json','B_added_support_from_triple':ds[i].tolist(),'B_cap_factor':'100001/100000','B_rotation':R.tolist(),'B_assignment':cols.tolist(),'A_record':record(A),'B_record':record(B)}
 (out/'construction.json').write_text(json.dumps(meta,indent=2)+'\n');print('ENDPOINTS',meta['A_record'],meta['B_record'],flush=True)
 logs=[]
 for k in range(101):
  t=k/100;Y=(1-t)*A+t*B
  try:r=record(Y)
  except ValueError:continue
  r['t']=t;logs.append(r)
  if k%10==0 or r['S']+r['U']<=3:print(r,flush=True)
  np.save(out/f't{k:03d}.npy',Y)
 (out/'screen.json').write_text(json.dumps(logs,indent=2)+'\n')
 print('best_interiors',sorted([r for r in logs if 0<r['t']<1],key=lambda a:a['soft_loss'])[:5],flush=True)
