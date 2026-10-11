"""Minimize the actual volume-centroid distance while preserving reference110.
The fixed farthest vertex removes trivial scale collapse. Unlike the line
homotopy, the centroid may move in any direction. Exact own110 is still required.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from vertex_geometry import geometry
from thales_centroid_homotopy import Homotopy
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def run(source,out,rounds):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);X=X[geometry(X,False)['vertices']];X/=np.max(np.linalg.norm(X,axis=1));np.save(out/'initial.npy',X);history=[];start=time.time()
 for outer in range(rounds):
  X=X[geometry(X,False)['vertices']];s=Homotopy(X,out/f'chart{outer:02d}',1e-8);z=s.c.z0.copy();trust=.02
  for it in range(1000):
   w=np.r_[z,0.];e,DE,v,DV,X,info=s.calc(w);g=np.array(info['centroid']);Dg=DE[:,:-1]*s.scale;f=float(g@g);grad=2*g@Dg;row=dict(chart=outer,it=it,centroid_squared=f,centroid_norm=float(np.sqrt(f)),trust=trust,**{k:info[k] for k in ['S','U','reference_S','reference_U','min_guard','interior','V']},seconds=time.time()-start);history.append(row);np.save(out/'latest.npy',X);np.save(out/'latest_params.npy',z);(out/'history.json').write_text(json.dumps(history,indent=2));(out/'latest.json').write_text(json.dumps(row,indent=2))
   if info['S']==info['U']==1:
    np.save(out/'potential.npy',X);print('CENTER_DESCENT_POTENTIAL_OWN110_REQUIRES_EXACT',row,flush=True);return
   if it%20==0:print('CENTER_DESCENT',row,flush=True)
   d=len(z);J=DV[:,:-1];I=eye(d);scale=.001;A=vstack([hstack([-csr_matrix(J/scale),csr_matrix((len(v),d))]),hstack([I,-I]),hstack([-I,-I])],format='csr');b=np.r_[v/scale,np.zeros(2*d)];obj=np.r_[grad/max(np.linalg.norm(grad),1e-30),np.full(d,1e-8)]
   sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*d,method='highs',options=OPT)
   if not sol.success:trust*=.4;continue
   dz=sol.x[:d];pred=-grad@dz;accepted=False
   if pred>1e-14:
    for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625,.001953125]:
     zz=z+alpha*dz;_,_,vv,_,XX,ii=s.calc(np.r_[zz,0.]);ff=np.dot(ii['centroid'],ii['centroid'])
     if ii['V']>=12 and min(vv)>-s.eps*.01 and ii['reference_S']==ii['reference_U']==1 and ff<f-1e-5*alpha*pred:
      z=zz;X=XX;accepted=True;row['alpha']=alpha
      if alpha==1:trust=min(trust*1.2,.1)
      break
   if not accepted:trust*=.4
   if trust<1e-9:break
  np.save(s.out/'accepted_final.npy',X)
 print('CENTER_DESCENT_DONE',history[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--rounds',type=int,default=10);a=p.parse_args();run(a.input,a.out,a.rounds)
