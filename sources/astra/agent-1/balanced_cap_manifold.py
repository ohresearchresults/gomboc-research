"""Nine free cap coordinates with three full-hull moment equations closed.

The three compensating cap feet may move inside their original facets. Their
heights are bounded by the old-vertex escape balls, not by one-facet visibility;
thus old vertices may retire from the new convex hull. Every body is integrated
and counted anew. Nothing about the actual centroid is inferred from polarity.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time,hashlib
import numpy as np
from scipy.spatial import QhullError
from scipy.optimize import minimize
from balanced_flower_caps import parent_data
from balanced_cap_optimize import mass,Found
from stable_face_augmentation import halfspaces
from basin_scout import score

def run(candidate,out,evaluations=4500,eta=1e-7):
    candidate=pathlib.Path(candidate);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);recipe=json.loads((candidate/'construction.json').read_text());parent=pathlib.Path(recipe['parent_audit']).parent;p=parent_data(parent);s0=json.loads((candidate/'summary-numerical.json').read_text());tri=np.array(s0['balancing_facets']);C=p['C'][tri];N=p['N'][tri];area=p['area'][tri];P=p['P'];Qold=p['Q'];points0=np.load(candidate/'body.npz')['added_points'];v0=points0[0];e1=[];e2=[];scale=[]
    for f,c,n in zip(tri,C,N):
        vertices=P[p['faces'][f]];axis=vertices[0]-c;axis/=np.linalg.norm(axis);e1.append(axis);e2.append(np.cross(n,axis));scale.append(np.sqrt(np.mean(np.sum((vertices-c)**2,axis=1))))
    e1=np.array(e1);e2=np.array(e2);scale=np.array(scale);moving=np.arange(len(P)+1,len(P)+4);offset=points0[1:]-C;params0=np.r_[v0,np.c_[np.sum(offset*e1,axis=1)/scale,np.sum(offset*e2,axis=1)/scale].ravel()];count=0;best=np.inf;strict_best=1.;history=[];start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(candidate=str(candidate.resolve()),parent=str(parent.resolve()),balancing_facets=tri.tolist(),eta=eta,evaluations=evaluations,parameterization='3 main point coordinates; 2 tangential coordinates per compensating facet; 3 normal heights solve full first moments',scope='Numerical actual-body search; exact physical audit required'),indent=2))
    def evaluate(z):
        nonlocal count,best,strict_best
        count+=1;v=z[:3];tt=z[3:].reshape(3,2);tangent=scale[:,None]*(tt[:,0,None]*e1+tt[:,1,None]*e2);feet=C+tangent
        if np.max(Qold@feet.T)>1+1e-10:return 1+float(np.maximum(Qold@feet.T-1,0).sum())
        if np.max(P@v-v@v)<=1e-9:return 1.
        limits=[]
        for foot,n in zip(feet,N):
            aa=P@foot-foot@foot;bb=2*foot@n-P@n;good=aa>1e-12
            if not good.any():return 1.
            roots=2*aa[good]/(bb[good]+np.sqrt(bb[good]**2+4*aa[good]));limits.append(.95*float(roots.max()))
        limits=np.array(limits)
        try:
            _,mainM,_=mass(np.r_[P,v[None]],[],[]);B=(area[:,None]*(C+tangent/4)/3).T;d=np.linalg.solve(B,-mainM)
            if not ((d>0)&(d<limits)).all():return 1+float(np.maximum(-d,0).sum()+np.maximum(d-limits,0).sum())
            for it in range(16):
                points=np.r_[v[None],feet+d[:,None]*N];X=np.r_[P,points];V,M,J=mass(X,moving,N)
                if np.linalg.norm(M)/V<1e-13:break
                step=np.linalg.solve(J,-M);accepted=False
                for bt in range(12):
                    dd=d+step*2**-bt
                    if not ((dd>0)&(dd<limits)).all():continue
                    XX=np.r_[P,v[None],feet+dd[:,None]*N];VV,MM,_=mass(XX,moving,N)
                    if np.linalg.norm(MM)<np.linalg.norm(M):d=dd;accepted=True;break
                if not accepted:return 1.
            if np.linalg.norm(M)/V>=1e-12:return 1.
            points=np.r_[v[None],feet+d[:,None]*N];Q=halfspaces(np.r_[P,points]);s=score(Q)
            if not 17<=s['E']<249:return 1+.01*max(s['E']-248,0)
            if s['U']!=1:return 1+max(s['P'],default=0)
            val=float(eta*np.log1p(np.array(s['Q'])/eta).sum());depth=max(s['Q'],default=0);winning=s['S']==1 and min(s['min_primal_nonroot'],s['min_polar_nonroot'])>1e-9;improved=s['S']==2 and depth<strict_best-1e-10
            if winning or val<best-max(1e-16,eta*1e-10) or improved:
                folder=out/f'evaluation{count:06d}';folder.mkdir();np.savez(folder/'body.npz',X=np.r_[P,points],Q=Q,added_points=points,parameters=z);record=dict(evaluation=count,balancing_facets=tri.tolist(),heights=d.tolist(),tangent_coordinates=tt.tolist(),centroid_norm=float(np.linalg.norm(M)/V),search_objective=val,eta=eta,seconds=time.time()-start,**s);(folder/'summary-numerical.json').write_text(json.dumps(record,indent=2));rr=dict(parent_audit=str((parent/'audit.json').resolve()),parent_audit_sha256=hashlib.sha256((parent/'audit.json').read_bytes()).hexdigest(),parent_frame='raw',parent_translation='None; use exact raw parent coordinates',added_points=[[str(x) for x in row] for row in points+p['centroid']],scope='New literal rational body in parent frame, pending independent full exact audit');(folder/'construction.json').write_text(json.dumps(rr,indent=2));history.append(dict(folder=str(folder.resolve()),**record));(out/'history.json').write_text(json.dumps(history,indent=2));print('BALANCED_MANIFOLD',json.dumps(record),flush=True);best=min(best,val)
                if improved:strict_best=depth;(out/'best-strict211.json').write_text(json.dumps(dict(folder=str(folder.resolve()),**record),indent=2))
                if winning:(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(construction=str((folder/'construction.json').resolve())),indent=2));raise Found()
            return val
        except (ValueError,QhullError,np.linalg.LinAlgError):return 2.
    step=np.r_[np.full(3,.001*np.sqrt(np.mean(np.sum(P*P,axis=1)))),np.full(6,.025)];simplex=np.r_[params0[None],params0[None]+np.diag(step)]
    try:
        evaluate(params0);res=minimize(evaluate,params0,method='Nelder-Mead',options={'maxfev':evaluations,'maxiter':evaluations,'initial_simplex':simplex,'adaptive':True,'xatol':1e-9,'fatol':min(1e-12,eta*1e-8)});(out/'finite-result.json').write_text(json.dumps(dict(message=str(res.message),success=bool(res.success),value=float(res.fun),parameters=res.x.tolist(),evaluations=count,best_strict_Q=strict_best),indent=2))
    except Found:print('POTENTIAL_MASS_BALANCED_OWN110_REQUIRES_EXACT',flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--candidate',required=True);ap.add_argument('--out',required=True);ap.add_argument('--evaluations',type=int,default=4500);ap.add_argument('--eta',type=float,default=1e-7);a=ap.parse_args();run(a.candidate,a.out,a.evaluations,a.eta)
