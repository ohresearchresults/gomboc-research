"""Three-dimensional actual-mass search with three compensating facet caps.
All caps remain within explicit old-vertex escape balls. Their three heights
solve the full convex hull's first moment, with an analytic derivative through
its current oriented boundary triangles. Exact acceptance is separate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,pathlib,time,hashlib
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize
from balanced_flower_caps import parent_data
from stable_face_augmentation import halfspaces
from geometry import halfspace_mesh,arrows
from basin_scout import score

class Found(Exception):pass

def mass(X,moving,N):
    h=ConvexHull(X);T=h.simplices.copy();a=X[T];flip=(np.cross(a[:,1]-a[:,0],a[:,2]-a[:,0])*h.equations[:,:3]).sum(1)<0;T[flip]=T[flip][:,[0,2,1]];a,b,c=np.moveaxis(X[T],1,0);det=np.einsum('ij,ij->i',a,np.cross(b,c));M=np.sum(det[:,None]*(a+b+c),axis=0)/24;V=det.sum()/6;J=[]
    for index,n in zip(moving,N):
        da=(T[:,0]==index)[:,None]*n;db=(T[:,1]==index)[:,None]*n;dc=(T[:,2]==index)[:,None]*n;dd=(da*np.cross(b,c)).sum(1)+(db*np.cross(c,a)).sum(1)+(dc*np.cross(a,b)).sum(1);J.append(np.sum(dd[:,None]*(a+b+c)+det[:,None]*(da+db+dc),axis=0)/24)
    return V,M,np.array(J).T

def run(candidate,out,iterations=1400,cap_fraction=.9,eta=.001,initial_step=.001):
    candidate=pathlib.Path(candidate);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);recipe=json.loads((candidate/'construction.json').read_text());parent=pathlib.Path(recipe['parent_audit']).parent;p=parent_data(parent,cap_fraction);s0=json.loads((candidate/'summary-numerical.json').read_text());tri=np.array(s0['balancing_facets']);C=p['C'][tri];N=p['N'][tri];area=p['area'][tri];limits=p['limits'][tri];P=p['P'];v0=np.load(candidate/'body.npz')['added_points'][0];baseline=score(p['Q']);u=P[np.argmax((P*P).sum(1))];moving=np.arange(len(P)+1,len(P)+4);B=(area[:,None]*C/3).T;BI=np.linalg.inv(B);best=1e9;best_strict=1.;history=[];start=time.time();counter=0
    (out/'definition.json').write_text(json.dumps(dict(candidate=str(candidate.resolve()),parent=str(parent.resolve()),balancing_facets=tri.tolist(),cap_fraction=cap_fraction,limits=limits.tolist(),iterations=iterations,eta=eta,initial_step=initial_step,scope='Floating full-body first-moment closure and actual-centroid census; exact audit required'),indent=2))
    def evaluate(v,save=True):
        nonlocal counter,best,best_strict
        counter+=1;v=np.asarray(v);escape=np.max(P@v-v@v)
        if escape<=1e-9:return 1+abs(escape)
        try:
            _,mainM,_=mass(np.r_[P,v[None]],[],[]);d=BI@(-mainM)
            if not ((d>0)&(d<limits)).all():return 1+float(np.maximum(-d,0).sum()+np.maximum(d-limits,0).sum())
            for iteration in range(14):
                caps=C+d[:,None]*N;X=np.r_[P,v[None],caps];V,M,J=mass(X,moving,N)
                if np.linalg.norm(M)/V<1e-13:break
                step=np.linalg.solve(J,-M);accepted=False
                for bt in range(12):
                    dd=d+step*2**-bt
                    if not ((dd>0)&(dd<limits)).all():continue
                    XX=np.r_[P,v[None],C+dd[:,None]*N];VV,MM,_=mass(XX,moving,N)
                    if np.linalg.norm(MM)<np.linalg.norm(M):d=dd;accepted=True;break
                if not accepted:return 1+float(np.linalg.norm(M)/V)
            if np.linalg.norm(M)/V>=1e-12:return 1+float(np.linalg.norm(M)/V)
            points=np.r_[v[None],C+d[:,None]*N];Q=halfspaces(np.r_[P,points]);s=score(Q)
            if not 17<=s['E']<249:return 1+max(s['E']-248,0)*.01
            if s['U']!=1:return 1+max(s['P'],default=0)
            val=float(eta*np.log1p(np.array(s['Q'])/eta).sum());record=dict(evaluation=counter,main_vertex=v.tolist(),heights=d.tolist(),moment_norm=float(np.linalg.norm(M)),mass_centroid_norm=float(np.linalg.norm(M)/V),search_objective=val,objective_eta=eta,seconds=time.time()-start,**s)
            winning=s['S']==1 and min(s['min_primal_nonroot'],s['min_polar_nonroot'])>1e-9
            improved_strict=s['S']==2 and max(s['Q'],default=0)<best_strict-1e-10
            if winning or val<best-1e-12 or improved_strict:
                folder=out/f'evaluation{counter:06d}';folder.mkdir();np.savez(folder/'body.npz',X=np.r_[P,points],Q=Q,added_points=points);rr=dict(parent_audit=str((parent/'audit.json').resolve()),parent_audit_sha256=hashlib.sha256((parent/'audit.json').read_bytes()).hexdigest(),parent_frame='raw',parent_translation='None; use the exact raw parent vertices',added_points=[[str(x) for x in row] for row in points+p['centroid']],scope='NEW exact rational body nominated by decimal added points in the unchanged exact parent frame; full audit required');(folder/'construction.json').write_text(json.dumps(rr,indent=2));(folder/'summary-numerical.json').write_text(json.dumps(dict(balancing_facets=tri.tolist(),**record),indent=2));history.append(dict(folder=str(folder.resolve()),**record));(out/'history.json').write_text(json.dumps(history,indent=2));print('BALANCED_CAP_OPTIMIZATION',json.dumps(record),flush=True)
                if val<best:best=val
                if improved_strict:best_strict=max(s['Q'],default=0);(out/'best-strict211.json').write_text(json.dumps(dict(folder=str(folder.resolve()),**record),indent=2))
                if winning:(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(construction=str((folder/'construction.json').resolve())),indent=2));raise Found()
            return val
        except (ValueError,QhullError,np.linalg.LinAlgError):return 2.
    # Check the mass derivative at a known physical cap configuration before
    # using it in the new local implicit-centroid construction.
    d=np.array(s0['heights']);X=np.r_[P,v0[None],C+d[:,None]*N];_,_,J=mass(X,moving,N);fd=[];h=1e-7
    for j in range(3):
        direction=np.zeros(3);direction[j]=h;fp=mass(np.r_[P,v0[None],C+(d+direction)[:,None]*N],moving,N)[1];fm=mass(np.r_[P,v0[None],C+(d-direction)[:,None]*N],moving,N)[1];fd.append((fp-fm)/(2*h))
    err=float(np.max(abs(np.array(fd).T-J)));(out/'mass-derivative-check.json').write_text(json.dumps(dict(max_absolute_error=err,step=h),indent=2));assert err<1e-8
    try:
        evaluate(v0);simplex=np.r_[v0[None],v0[None]+np.eye(3)*initial_step*np.linalg.norm(u)];result=minimize(evaluate,v0,method='Nelder-Mead',options={'maxfev':iterations,'maxiter':iterations,'xatol':1e-10,'fatol':min(1e-12,eta*1e-8),'initial_simplex':simplex});(out/'finite-result.json').write_text(json.dumps(dict(message=str(result.message),success=bool(result.success),value=float(result.fun),x=result.x.tolist(),evaluations=counter,best_strict_Q=best_strict),indent=2))
    except Found:print('POTENTIAL_BALANCED_OWN110_REQUIRES_EXACT',flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--candidate',required=True);ap.add_argument('--out',required=True);ap.add_argument('--iterations',type=int,default=1400);ap.add_argument('--cap-fraction',type=float,default=.9);ap.add_argument('--eta',type=float,default=.001);ap.add_argument('--initial-step',type=float,default=.001);a=ap.parse_args();run(a.candidate,a.out,a.iterations,a.cap_fraction,a.eta,a.initial_step)
