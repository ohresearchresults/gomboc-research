"""Direct five-dimensional physical affine search, at the uniform centroid.
Each matrix is invertible with determinant one. Primal X maps to AX and dual
Q to A^{-T}Q; the actual uniform centroid transforms by that SAME map. A
numerical qualifying nomination is rehulled and reintegrated before saving.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.optimize import differential_evolution,minimize
from geometry import halfspace_mesh,arrows,census
from persistence_search import pairs,polar_edges


class Found(Exception):pass


def run(input,out,mode='bar',seed=615417,maxiter=800):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);a=np.load(input)
    raw=a['normals']/a['offs'][:,None];mesh=halfspace_mesh(raw);X=mesh['X']-mesh['g'];Q=raw/(1-raw@mesh['g'])[:,None]
    # A similarity keeps the finite parameter range in ordinary physical units.
    radius=np.sqrt(np.mean(np.sum(X*X,axis=1)));X/=radius;Q*=radius;ep=mesh['edges'];eq=polar_edges(mesh)
    np.savez(out/'physical_parent.npz',X=X,Q=Q,edges=ep,polar_edges=eq)
    (out/'definition.json').write_text(json.dumps(dict(input=str(pathlib.Path(input).resolve()),mode=mode,seed=seed,maxiter=maxiter,
        condition_number_limit=1e5,scope='Physical common affine embedding, same uniform centroid; formal metric residual is never a Figure'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());calls=0;best=np.inf;start=time.time();history=[]
    def transform(z):
        a,b,c,d,e=z
        A=np.array([[np.exp(a),c,d],[0.,np.exp(b),e],[0.,0.,np.exp(-a-b)]])
        return A,X@A.T,np.linalg.solve(A.T,Q.T).T
    def loss(z):
        nonlocal calls,best
        calls+=1;A,P,R=transform(z);condition=np.linalg.cond(A)
        if condition>1e5:return 10+np.log(condition/1e5)
        guards=[];counts=[];barsets=[]
        for points,edges in [(P,ep),(R,eq)]:
            W=arrows(points).max(1);root=int(np.argmax((points*points).sum(1)));non=np.delete(W,root)
            guards.append(float(non.min()));counts.append(int(np.sum(W<0)))
            if mode=='bar':
                pp,h=pairs(points,edges);barsets.append(np.maximum(0,1-h[pp[:,1]]/(points[pp[:,0]]**2).sum(1)))
        if mode=='bar':score=float(sum(np.sqrt(b).sum() for b in barsets))
        else:
            score=0.
            for points in (P,R):
                W=arrows(points).max(1);root=int(np.argmax((points*points).sum(1)));non=np.delete(W,root);score+=np.maximum(-non,0).sum()
        if counts==[1,1] and min(guards)>1e-9:
            actual=halfspace_mesh(R);st=census(actual,0)
            if st['S']==st['U']==1 and 17<=st['E']<250 and min(st['min_primal_nonroot'],st['min_polar_nonroot'])>1e-9:
                np.savez(out/'POTENTIAL_OWN110.npz',Q=R,X=actual['X'],A=A,parameters=z)
                (out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(calls=calls,condition=condition,**st),indent=2));raise Found()
        if score<best:
            best=score;row=dict(calls=calls,score=score,S=counts[1],U=counts[0],condition=condition,guards=guards,parameters=np.asarray(z).tolist(),seconds=time.time()-start)
            np.savez(out/'best.npz',A=A,X=P,Q=R,parameters=z);history.append(row);(out/'improvements.json').write_text(json.dumps(history,indent=2))
            print('AFFINE_DIRECT',json.dumps(row),flush=True)
        return score
    bounds=[(-3.,3.),(-3.,3.),(-5.,5.),(-5.,5.),(-5.,5.)]
    try:
        loss(np.zeros(5))
        result=differential_evolution(loss,bounds,seed=seed,popsize=20,maxiter=maxiter,tol=1e-9,atol=1e-10,
                                      polish=False,updating='immediate',workers=1)
        minimize(loss,result.x,method='Nelder-Mead',bounds=bounds,options={'maxiter':2500,'xatol':1e-10,'fatol':1e-12})
    except Found:return
    (out/'FINITE_END.json').write_text(json.dumps(dict(calls=calls,best=best,seconds=time.time()-start,scope='Finite affine search found no qualifying body; no family exclusion'),indent=2))
