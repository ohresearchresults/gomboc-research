"""Physical paths from strict121 to strict211 with <=51 moving input points.
Endpoint convex hulls are retained exactly up to rigid pose and global scale;
added correspondence points lie inside the second endpoint. All path bodies
are uniformly filled and their actual own centroids are recalculated.
"""
from pathlib import Path
import argparse,json,time
import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.spatial.transform import Rotation
from vertex_geometry import geometry
from support_geometry import escape
from persistence_birth import evaluate

def axes(g):
 u=np.flatnonzero(escape(g['Z'])[0]<0);s=np.flatnonzero(escape(g['H'])[0]<0);return u,s
def prepare(X):
 g=geometry(X,False);X=g['Z'][g['vertices']];X/=np.max(np.linalg.norm(X,axis=1));return X,geometry(X,False)
def align(B,A):
 U,_,V=np.linalg.svd(B.T@A);D=np.eye(3);D[-1,-1]=np.linalg.det(U@V);return U@D@V
def run(out,steps):
 out=Path(out);out.mkdir(exist_ok=False,parents=True);X,gx=prepare(np.load('artifacts/cap_flow_t0.25/latest.npy'));Y,gy=prepare(np.load('artifacts/thales_n40_1/polish211/success.npy'));ua,sa=axes(gx);ub,sb=axes(gy);assert len(sa)==len(ub)==1 and len(ua)==len(sb)==2
 rng=np.random.default_rng(550813);rows=[];start=time.time();best=np.inf
 for iu in ua:
  for js in sb:
   va=np.array([X[iu]/np.linalg.norm(X[iu]),gx['H'][sa[0]]/np.linalg.norm(gx['H'][sa[0]])]);vb=np.array([Y[ub[0]]/np.linalg.norm(Y[ub[0]]),gy['H'][js]/np.linalg.norm(gy['H'][js])]);R=align(vb,va)
   for twist in [-.6,-.3,-.1,0.,.1,.3,.6]:
    R2=Rotation.from_rotvec(twist*va[0]).as_matrix().T;YY=Y@R@R2;pad=len(X)-len(Y);T=gy['T'];cent=YY[T].mean(1);dirs=cent/np.linalg.norm(cent,axis=1)[:,None]
    # Literal interior convex combinations only; no density is moved to points.
    chosen=rng.choice(len(T),pad,replace=False);aux=cent[chosen]*.99;YY=np.vstack((YY,aux))
    cost=np.sum((X[:,None]-YY[None])**2,axis=2);cost[iu]=1e6;cost[:,ub[0]]=1e6;cost[iu,ub[0]]=0;ii,jj=linear_sum_assignment(cost);assert jj[iu]==ub[0];YY=YY[jj];path=out/f'u{iu}_s{js}_tw{twist:g}';path.mkdir();np.savez(path/'endpoints.npz',X=X,Y=YY,rotation=R@R2,permutation=jj,pad_triangles=chosen)
    pathrows=[]
    for k,t in enumerate(np.linspace(0,1,steps)):
     Z=(1-t)*X+t*YY;g=geometry(Z,False);nu=len(np.flatnonzero(escape(g['Z'])[0]<0));ns=len(np.flatnonzero(escape(g['H'])[0]<0));r=dict(t=float(t),S=ns,U=nu,V=len(g['vertices']))
     if ns+nu<=5:
      info=evaluate(Z)[2];r.update(P=info['Pmax'],Q=info['Qmax'],loss=info['loss'])
      if 0<t<1 and info['loss']<best:
       best=info['loss'];np.save(out/'best.npy',Z);(out/'best.json').write_text(json.dumps(dict(path=str(path),**r),indent=2))
     if ns==nu==1:
      np.save(path/f'potential_{k}.npy',Z);(path/f'potential_{k}.json').write_text(json.dumps(r));print('INTERPOLATION_POTENTIAL_NEEDS_EXACT',str(path),r,flush=True)
     pathrows.append(r)
    (path/'census.json').write_text(json.dumps(pathrows,indent=2));row=dict(path=str(path),min_equilibria=min(r['S']+r['U'] for r in pathrows[1:-1]),counts=sorted(set((r['S'],r['U']) for r in pathrows)),seconds=time.time()-start);rows.append(row);(out/'paths.json').write_text(json.dumps(rows,indent=2));print('INTERPOLATION_PATH',row,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('out');p.add_argument('--steps',type=int,default=501);a=p.parse_args();run(a.out,a.steps)
