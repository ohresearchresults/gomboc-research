"""Linear-disjunctive search for actual reference110 cells of a fixed body.
All S/U root choices and exclusion witnesses are free. Big-M bounds are derived
from physical vertex extrema, since c is constrained inside the actual hull.
Numerical MILP infeasibility is not promoted to a mathematical exclusion.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import milp,LinearConstraint,Bounds
from scipy.sparse import lil_matrix,csr_matrix
from gmpy2 import mpq
from sources.N40.N40_RECOVER import affine_guards,census

def run(source,out,seconds):
 source=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);a=json.loads(source.read_text());X=[tuple(mpq(v) for v in r) for r in a['raw_vertices']];c0=np.array([float(mpq(v)) for v in a['raw_centroid']]);XF=np.array(X,float);edges=a['edges'];owners={tuple(e):[] for e in edges}
 for f,cy in enumerate(a['faces']):
  for i,j in zip(cy,cy[1:]+cy[:1]):owners[tuple(sorted((i,j)))].append(f)
 K=dict(points=X,faces=a['faces'],edges=edges,edge_faces=list(owners.values()));groups=affine_guards(K)[:2];rows=[];rootcols=[];witnesscols=[];count=4;normalgroups=[];eps=1e-8*np.linalg.norm(np.ptp(XF,axis=0))
 for group in groups:
  roots=list(range(count,count+len(group)));count+=len(group);rootcols.append(roots);ng=[];wg=[]
  for fc in group:
   M=np.array([[float(v) for v in ar] for ar,b in fc]);b=np.array([float(v) for ar,v in fc]);sc=np.linalg.norm(M,axis=1);M/=sc[:,None];b/=sc;ng.append((M,b));ws=list(range(count,count+len(fc)));count+=len(fc);wg.append(ws)
  normalgroups.append(ng);witnesscols.append(wg)
 A=[];lb=[];ub=[]
 def add(coeff,low=-np.inf,high=np.inf):A.append(coeff);lb.append(low);ub.append(high)
 for roots,wg,ng in zip(rootcols,witnesscols,normalgroups):
  add({r:1 for r in roots},1,1)
  for r,ws,(M,b) in zip(roots,wg,ng):
   add({**{w:1 for w in ws},r:1},1,np.inf)
   for j,w in enumerate(ws):
    val=b[j]-XF@M[j];lower=float(val.min());upper=float(val.max());big=max(upper+eps,eps-lower)+1e-9
    # root r implies b-Mc>=eps; witness w implies b-Mc<=-eps.
    add({0:M[j,0],1:M[j,1],2:M[j,2],r:big},high=b[j]-eps+big)
    add({0:-M[j,0],1:-M[j,1],2:-M[j,2],w:big},high=-b[j]-eps+big)
 for n,h in zip(a['normals'],a['offsets']):
  n=np.array([float(mpq(v)) for v in n]);sc=np.linalg.norm(n);add({0:n[0]/sc,1:n[1]/sc,2:n[2]/sc},high=float(mpq(h))/sc-eps)
 for j in range(3):add({j:1,3:-1},high=c0[j]);add({j:-1,3:-1},high=-c0[j])
 AA=lil_matrix((len(A),count))
 for i,row in enumerate(A):
  for j,v in row.items():AA[i,j]=v
 low=np.r_[XF.min(0),0.,np.zeros(count-4)];high=np.r_[XF.max(0),np.inf,np.ones(count-4)];obj=np.zeros(count);obj[3]=1;integral=np.r_[np.zeros(4),np.ones(count-4)];t=time.time();res=milp(obj,integrality=integral,bounds=Bounds(low,high),constraints=LinearConstraint(csr_matrix(AA),lb,ub),options=dict(time_limit=seconds,mip_rel_gap=1e-6,presolve=True));report=dict(source=str(source.resolve()),status=int(res.status),message=str(res.message),variables=count,binaries=count-4,constraints=len(A),epsilon=eps,seconds=time.time()-t)
 if res.x is not None:
  c=res.x[:3];rc=tuple(mpq(int(round(v*1e13)),10**13) for v in c);ce=census(K,rc);report.update(reference_census=ce,reference_center=list(map(str,rc)),own_center=a['raw_centroid'],distance=float(np.linalg.norm(c-c0)),linf=float(res.x[3]));np.save(out/'reference_points.npy',XF-np.array(rc,float));print('MILP_REFERENCE_CENSUS',ce['strict'],ce['weak'],'own_distance',report['distance'],flush=True)
 (out/'result.json').write_text(json.dumps(report,indent=2));print('REFERENCE_MILP_DONE',report,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--seconds',type=float,default=60);a=p.parse_args();run(a.input,a.out,a.seconds)
