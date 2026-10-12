"""Reference110 physical volume expansion under a fixed farthest vertex.
Thales chords put every vertex strictly inside the root-radius ball. Therefore
volume maximization cannot be faked by scale growth. Actual-centroid penalty
and a retained physical volume floor counter collapse of centroid-only paths.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from thales_centroid_homotopy import Homotopy
from vertex_geometry import geometry
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def data(s,z,vol0,mu):
 eq,DE,v,J,X,info=s.calc(np.r_[z,0.]);X,DX=s.c.physical(z);g=geometry(X,False);T=g['T'];a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];da,db,dc=DX[T[:,0]],DX[T[:,1]],DX[T[:,2]];DV=(np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc)).sum(0)/6;V=g['V'];cent=g['g'];Dg=DE[:,:-1]*s.scale;f=-np.log(V)+mu*np.dot(cent,cent);grad=-DV/V+2*mu*cent@Dg;vv=np.r_[v,V/vol0-.8];JJ=np.vstack((J[:,:-1],DV/vol0));return f,grad,vv,JJ,X,dict(**info,volume=float(V),volume_ratio=float(V/vol0),objective=float(f))
def run(source,out,rounds,mu):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);X=X[geometry(X,False)['vertices']];X/=np.max(np.linalg.norm(X,axis=1));vol0=geometry(X,False)['V'];np.save(out/'initial.npy',X);(out/'mode.json').write_text(json.dumps(dict(mu=mu,initial_volume=vol0,volume_floor_fraction=.8,fixed_farthest_radius=1.,objective='-log(actual_volume)+mu*norm(actual_centroid)^2'),indent=2));hist=[];start=time.time()
 for outer in range(rounds):
  X=X[geometry(X,False)['vertices']];s=Homotopy(X,out/f'chart{outer:02d}',1e-8);z=s.c.z0.copy();trust=.01
  for it in range(700):
   f,grad,v,J,X,info=data(s,z,vol0,mu);row=dict(chart=outer,it=it,trust=trust,seconds=time.time()-start,**info);hist.append(row);np.save(out/'latest.npy',X);(out/'history.json').write_text(json.dumps(hist,indent=2));(out/'latest.json').write_text(json.dumps(row,indent=2))
   if it%20==0:print('REFERENCE_VOLUME_FLOW',out,{k:row[k] for k in ['chart','it','S','U','reference_S','reference_U','centroid_norm','volume','objective','trust']},flush=True)
   if info['S']==info['U']==1:np.save(out/'potential.npy',X);print('REFERENCE_VOLUME_POTENTIAL_OWN110_REQUIRES_EXACT',row,flush=True);return
   d=len(z);I=eye(d);sc=.001;A=vstack([hstack([-csr_matrix(J/sc),csr_matrix((len(v),d))]),hstack([I,-I]),hstack([-I,-I])],format='csr');b=np.r_[v/sc,np.zeros(2*d)];obj=np.r_[grad/np.linalg.norm(grad),np.full(d,1e-8)];sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*d,method='highs',options=OPT)
   if not sol.success:trust*=.4;continue
   dz=sol.x[:d];pred=-grad@dz;ok=False
   if pred>1e-14:
    for k in range(15):
     zz=z+2.**-k*dz
     try:ff,_,vv,_,XX,ii=data(s,zz,vol0,mu)
     except (ValueError,np.linalg.LinAlgError):continue
     if min(vv)>-1e-10 and ii['reference_S']==ii['reference_U']==1 and ff<f-1e-5*2.**-k*pred:
      z=zz;X=XX;ok=True;row['alpha']=2.**-k
      if k==0:trust=min(.1,trust*1.2)
      break
   if not ok:trust*=.4
   if trust<1e-9:break
  np.save(s.out/'accepted_final.npy',X)
 print('REFERENCE_VOLUME_DONE',out,hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--rounds',type=int,default=8);p.add_argument('--mu',type=float,default=10.);a=p.parse_args();run(a.input,a.out,a.rounds,a.mu)
