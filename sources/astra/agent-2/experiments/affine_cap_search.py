"""Search actual affine embeddings of a fixed homogeneous capped body.
If x'=A(x-g), the filled-volume centroid is zero and dual normals transform
as y'=A^{-T}y. This uses one consistent physical map, and preserves the true
hull combinatorics. Complete primal and dual persistence bars are included.
"""
import json,sys,time,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution,minimize
from physical_multiple_cap_family import MultipleCapFamily
from support_persistence import barcode
from geometry import angular_scores

def matrix(q):
    return np.array([[np.exp(q[0]),0.,0.],[q[2],np.exp(q[1]),0.],[q[3],q[4],np.exp(-q[0]-q[1])]])

def run(src,out,m=40,points=1,generations=500):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    raw=src.read_bytes();(out/'source_z.npy').write_bytes(raw);z=np.load(out/'source_z.npy');s=MultipleCapFamily(m,points,249).state(z)
    np.save(out/'source_X.npy',s['X']);np.save(out/'source_Y.npy',s['Y'])
    (out/'source.json').write_text(json.dumps(dict(path=str(src),sha256=hashlib.sha256(raw).hexdigest(),m=m,points=points,counts={k:s[k] for k in ['V','E','F','S','U']},centroid=s['g'].tolist(),method=__doc__),indent=2)+'\n')
    best=np.inf;calls=0;history=[];start=time.time()
    class Found(Exception):pass
    def fun(q):
        nonlocal best,calls
        A=matrix(q);Z=s['Z']@A.T;Y=s['Y']@np.linalg.inv(A)
        p,_,P=barcode(Z,np.ones(len(Z)),s['eu']);r,_,Q=barcode(Y,np.ones(len(Y)),s['es'])
        P/=np.sum(Z[p[:,0]]**2,1);Q/=np.sum(Y[r[:,0]]**2,1)
        value=float(max(P.max(),Q.max())+.1*(P.mean()+Q.mean()));calls+=1
        if value<best:
            best=value;S=int((angular_scores(Y).max(1)<0).sum());U=int((angular_scores(Z).max(1)<0).sum())
            row=dict(evaluations=calls,seconds=time.time()-start,S=S,U=U,Pmax=float(P.max()),Qmax=float(Q.max()),objective=value,E=s['E'],condition=float(np.linalg.cond(A)),matrix=A.tolist())
            history.append(row);np.save(out/'best_affine.npy',A);np.save(out/'best_physical_X.npy',Z);(out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
            if calls==1 or S+U<=4:print('AFFINE_ACTUAL_BODY',row,flush=True)
            if S==U==1:
                # Independently integrate the transformed filled body.
                T=np.array([[f[0],f[i],f[i+1]] for f in s['faces'] for i in range(1,len(f)-1)],int)
                a,b,c=Z[T[:,0]],Z[T[:,1]],Z[T[:,2]];six=np.sum(a*np.cross(b,c),1);g=np.sum(six[:,None]*(a+b+c),0)/(4*six.sum())
                if abs(g).max()>1e-9:raise ValueError('physical affine mass identity failed')
                row.update(independent_centroid=g.tolist(),volume=float(six.sum()/6));np.save(out/'NUMERICAL_NOMINATION_affine.npy',A);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');raise Found()
        return value
    try:
        fun(np.zeros(5))
        for radius in [.04,.15,.5,1.5]:
            result=differential_evolution(fun,[(-radius,radius)]*5,x0=np.zeros(5),popsize=12,maxiter=generations,polish=False,tol=1e-9,seed=int(radius*1000)+811,updating='immediate')
            minimize(fun,result.x,method='Nelder-Mead',options=dict(maxiter=1200,xatol=1e-11,fatol=1e-13))
    except Found:return
    (out/'FINITE_BRANCH_END.json').write_text(json.dumps(dict(evaluations=calls,best_objective=best,goal_complete=False),indent=2)+'\n')

if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 40,int(sys.argv[4]) if len(sys.argv)>4 else 1,int(sys.argv[5]) if len(sys.argv)>5 else 500)
