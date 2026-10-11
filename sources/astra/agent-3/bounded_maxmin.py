"""Maximize the worst physical equilibrium escape margin within C<500 families."""
import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

from bounded_goal_search import support_guards, exact_support
from direct_face_polish import guards as vertex_guards
from goal_nomination import preserve
from support_geometry import geometry as sg
from vertex_geometry import geometry as vg


def gauge(X):
    n=len(X);Z=X-X.mean(0);A=np.zeros((7,n,3))
    for j in range(3):A[j,:,j]=1
    A[3]=Z
    A[4,:,1]=-Z[:,2];A[4,:,2]=Z[:,1]
    A[5,:,0]=Z[:,2];A[5,:,2]=-Z[:,0]
    A[6,:,0]=-Z[:,1];A[6,:,1]=Z[:,0]
    A=A.reshape(7,-1);A/=np.linalg.norm(A,axis=1)[:,None]
    return np.c_[A,np.zeros(7)]


def run(source,out,kind,steps,physical_angular=False):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);assert len(X)<=84
    geom=vg if kind=='vertices'else sg;guards=vertex_guards if kind=='vertices'else support_guards
    if physical_angular:
        from bounded_physical_guards import evaluate
        guards=lambda g,derivative=True:evaluate(g,kind,derivative)
    initial=X.copy();np.save(out/'initial.npy',X);trace=[];trust=.004;start=time.time()
    (out/'method.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),kind=kind,physical_angular=physical_angular,maximum_true_edges=246,objective='maximize smallest selected own-centroid escape margin; seven linear similarity gauges'),indent=2))
    def nominate(Q,path):
        if kind=='vertices':preserve(Q,path,'C<=492 bounded family numerical own110 during worst-margin continuation')
        else:exact_support(Q,path)
    for it in range(steps):
        g=geom(X);v,J,cl=guards(g);minimum=float(min(v));row=dict(it=it,minimum=minimum,deficit_sum=float(np.maximum(1e-9-v,0).sum()),trust=trust,seconds=time.time()-start,**cl)
        trace.append(row);np.save(out/'latest.npy',X);(out/'trace.json').write_text(json.dumps(trace,indent=2))
        if it%10==0:print('BOUNDED_MAXMIN',out,row,flush=True)
        if cl['S']==cl['U']==1:nominate(X,out/f'exact_nomination_it{it}')
        d=X.size
        A=np.c_[-J,np.ones(len(v))];E=gauge(X)
        r=linprog(np.r_[np.zeros(d),-1.],A_ub=A,b_ub=v,A_eq=E,b_eq=np.zeros(7),bounds=[(-trust,trust)]*d+[(None,None)],method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=10.))
        if not r.success:row['error']=r.message;trust*=.4
        else:
            dx=r.x[:d].reshape(X.shape);ok=False
            for k in range(16):
                xx=X+2.**-k*dx
                try:gg=geom(xx,False);vv,_,cc=guards(gg,False);m=float(min(vv))
                except(ValueError,np.linalg.LinAlgError):continue
                if cc['S']==cc['U']==1:nominate(xx,out/f'exact_nomination_it{it}_line{k}')
                if m>minimum+max(1e-13,abs(minimum)*1e-7):X=xx;ok=True;row['alpha']=2.**-k;break
            if ok and k==0:trust=min(.04,trust*1.3)
            if not ok:trust*=.4
        if trust<1e-11:break
    np.save(out/'endpoint.npy',X);print('BOUNDED_MAXMIN_FINITE_STOP',out,trace[-1],flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--kind',choices=['vertices','supports'],required=True);p.add_argument('--steps',type=int,default=1000);p.add_argument('--physical-angular',action='store_true');a=p.parse_args();run(a.source,a.out,a.kind,a.steps,a.physical_angular)
