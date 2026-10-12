"""Refine a twisted radial hull by explicit geometric escape witnesses.
The reference-centre stage is only a construction device. A final horizontal
cut is integrated independently at the body's own centroid before nomination.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np,torch
from scipy.optimize import minimize,brentq
from scipy.spatial import QhullError
from scipy.special import spherical_jn
from twisted_convex_masscut import points,clipped_mass
from stable_face_augmentation import halfspaces
from geometry import halfspace_mesh,arrows,census

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)


def witness(p,epsilon,k):
    direction=p/np.linalg.norm(p);x,y,z=direction;co=np.cos(k*x);si=np.sin(k*x)
    start=np.array([np.arcsin(np.clip(y*si+z*co,-1,1)),np.arctan2(y*co-z*si,x)])
    pp=torch.tensor(p)
    def coordinate(a):
        t,phi=a;w=torch.sin(t);u=torch.cos(t)*torch.cos(phi);v=torch.cos(t)*torch.sin(phi)
        co=torch.cos(k*u);si=torch.sin(k*u)
        return (1+epsilon*w)*torch.stack([u,v*co+w*si,-v*si+w*co])
    def loss(a):
        aa=torch.tensor(a,requires_grad=True);value=-(pp*coordinate(aa)).sum()
        return float(value.detach()),torch.autograd.grad(value,aa)[0].detach().numpy()
    result=minimize(loss,start,jac=True,method='L-BFGS-B',bounds=[(-np.pi/2,np.pi/2),(start[1]-np.pi,start[1]+np.pi)],
                    options={'maxiter':100,'ftol':1e-14,'gtol':1e-11})
    q=coordinate(torch.tensor(result.x)).detach().numpy()
    return q,float(p@(q-p))


def mass_cut(H,m):
    if m['g'][2]>=-1e-9:return None
    upper=-m['X'][:,2].min()+1e-6
    height=brentq(lambda h:float(clipped_mass(m['X'],m['triangles'],h)[0][2]),1e-6,upper,xtol=1e-12)
    Q=np.r_[H,[[0.,0.,-1/height]]];body=halfspace_mesh(Q)
    if abs(body['g']).max()>2e-9:raise ValueError('Final independent mass-cut closure failed')
    return Q,body,float(height)


def run(out,trials=48,rounds=32,seed=573312):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);rng=np.random.default_rng(seed);history=[];start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(trials=trials,rounds=rounds,seed=seed,
        scope='Explicit reference escape witnesses followed by actual homogeneous mass closure and full census; no reference-centre success claim'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    for trial in range(trials):
        eps=float(rng.uniform(.18,.94));k=float(brentq(lambda a:4*spherical_jn(1,a)/a+12*eps**2*spherical_jn(2,a)/a**2,4,6)+rng.uniform(-.4,.4))
        pars=dict(m=int(rng.choice([12,16,20])),epsilon=eps,k=k,phase=float(rng.uniform(0,np.pi)),apex_extra=float(rng.uniform(.08,.35)),power=float(rng.uniform(.7,1.4)))
        X=points(**pars);p=out/f'trial{trial:03d}';p.mkdir();(p/'parameters.json').write_text(json.dumps(pars,indent=2));records=[]
        for iteration in range(rounds):
            try:
                H=halfspaces(X);body=halfspace_mesh(H);X=body['X'];W=arrows(X);roots=np.flatnonzero(W.max(1)<0);elder=int(np.argmax((X*X).sum(1)))
                refS=int(np.sum(arrows(H).max(1)<0));own=census(body,0)
                row=dict(iteration=iteration,referenceS=refS,referenceU=len(roots),seconds=time.time()-start,**own)
                records.append(row);np.savez(p/'latest.npz',X=X,Q=H);(p/'history.json').write_text(json.dumps(records,indent=2))
                if not 17<=len(body['edges'])<249:row['stop']='edge budget';break
                if own['S']==own['U']==1:
                    np.savez(out/'POTENTIAL_OWN110.npz',X=X,Q=H);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(trial=trial,uncut=True,**row),indent=2));return
                if len(roots)<=3 or iteration%5==0:
                    cut=mass_cut(H,body)
                    if cut is not None:
                        Q,m,height=cut;st=census(m,0);row['cut']=dict(height=height,**st)
                        np.savez(p/'latest-mass-closed.npz',Q=Q,X=m['X'])
                        if 17<=st['E']<249 and st['S']==st['U']==1:
                            np.savez(out/'POTENTIAL_OWN110.npz',Q=Q,X=m['X']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(trial=trial,iteration=iteration,height=height,**st),indent=2));return
                if len(roots)==1:row['stop']='reference U closed; actual candidate checked';break
                additions=[];witnesses=[]
                for i in roots:
                    if i==elder:continue
                    q,margin=witness(X[i],eps,k)
                    if margin>1e-10:
                        additions.append(q);witnesses.append(dict(old_vertex=int(i),point=q.tolist(),escape_margin=margin))
                row['new_witnesses']=witnesses
                if not additions:row['stop']='no strict finite witness found';break
                # Literal half-turn pairs preserve the one-dimensional mass
                # equation independently of optimization roundoff.
                additions=np.array(additions);X=np.r_[X,additions,additions*np.array([-1.,-1.,1.])]
            except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as error:
                records.append(dict(iteration=iteration,error=repr(error)));break
        (p/'history.json').write_text(json.dumps(records,indent=2));result=dict(trial=trial,parameters=pars,endpoint=records[-1]);history.append(result)
        (out/'history.json').write_text(json.dumps(history,indent=2));print('SUPPORT_CLOSURE_TRIAL',json.dumps({k:v for k,v in records[-1].items() if k not in ['S_ids','U_ids','new_witnesses']}),flush=True)
