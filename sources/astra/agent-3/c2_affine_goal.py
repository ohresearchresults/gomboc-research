"""Consistent physical affine search of C2 mass-closed bodies.

Every trial is the uniformly filled A*P, whose volume centroid is A*g(P).
Physical vertices and dual normals use the same invertible map. Numerical110
triggers literal dyadic physical-coordinate preservation and complete exact audit.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution,minimize
from vertex_geometry import geometry
from direct_face_polish import face_scores
from support_geometry import escape
from goal_nomination import preserve

def run(source,out,generations,seed):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);initial=geometry(X,False);root=int(np.argmax(X[:,2]));ids=initial['vertices'];mask=~np.all(initial['T']<4,axis=1);um=ids!=root
    calls=0;best=np.inf;start=time.time();trace=[]
    def compute(p,save=True):
        nonlocal calls,best
        calls+=1;A=np.array([[np.exp(p[0]),p[1],0],[0,np.exp(p[2]),0],[0,0,1.]])
        Y=X@A.T;g=dict(initial,X=Y,Z=initial['Z']@A.T,g=A@initial['g'],H=initial['H']@np.linalg.inv(A))
        f,_,_=face_scores(g,False);u,_=escape(g['Z'][ids],angular=True);v=np.r_[f[mask],u[um]]
        # Every strictly positive escape is retained. Epsilon only asks for a
        # positive numerical safety margin; it never removes extra equilibria.
        apex_radius=np.linalg.norm(g['Z'][root]);base_distance=abs(g['Z'][0,2])
        radial=1-np.linalg.norm(g['Z'][ids[um]],axis=1)/apex_radius
        support=1/np.linalg.norm(g['H'][mask],axis=1)/base_distance-1
        value=float(np.maximum(1e-7-v,0).sum()+np.maximum(1e-7-radial,0).sum()+np.maximum(1e-7-support,0).sum());S=1+int(sum(f[mask]<0));U=int(sum(u<0))
        if S==U==1:
            d=out/f'exact_goal_call{calls:07d}';preserve(Y,d,'consistent physical C2 affine map, actual volume centroid transformed by the same A, numerical own110')
        if save and value<best:
            best=value;row=dict(calls=calls,value=value,S=S,U=U,min_face=float(min(f[mask])),min_escape=float(min(u[um])),parameters=p.tolist(),matrix=A.tolist(),seconds=time.time()-start);trace.append(row);np.save(out/'best.npy',Y);(out/'best.json').write_text(json.dumps(row,indent=2))
            if len(trace)%20==1:print('C2_AFFINE_GOAL',out,row,flush=True)
        return value
    bounds=[(-3.,3.),(-8.,8.),(-3.,3.)]
    compute(np.zeros(3));de=differential_evolution(compute,bounds,popsize=15,maxiter=generations,tol=1e-10,atol=0,seed=seed,polish=False,updating='immediate')
    for eta in [None]:
        r=minimize(compute,de.x,method='Nelder-Mead',bounds=bounds,options=dict(maxiter=3000,xatol=1e-12,fatol=1e-13))
    (out/'trace.json').write_text(json.dumps(trace,indent=2));print('C2_AFFINE_FINITE_STOP',out,dict(calls=calls,best=best,seconds=time.time()-start),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--generations',type=int,default=600);p.add_argument('--seed',type=int,default=16402);a=p.parse_args();run(a.source,a.out,a.generations,a.seed)
