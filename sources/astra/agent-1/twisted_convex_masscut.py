"""Direct convex hull and actual-mass-balanced truncation of twisted latitudes.
The half-turn symmetry reduces the actual centroid condition to g_z=0.
For each literal convex hull with negative g_z, a horizontal cut is solved
against its full polyhedral mass. The resulting body is independently counted.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import pathlib,json,time
import numpy as np
from scipy.spatial import QhullError
from scipy.optimize import brentq
from scipy.special import spherical_jn
from stable_face_augmentation import halfspaces
from geometry import halfspace_mesh,arrows,census


def points(m,epsilon,k,phase,apex_extra,power):
    w=-.99+1.98*(np.arange(m)+.5)/m;w=np.sign(w)*abs(w)**power
    phi=(np.arange(m)*np.pi*(3-np.sqrt(5))+phase)%np.pi
    u=np.sqrt(1-w*w)*np.cos(phi);v=np.sqrt(1-w*w)*np.sin(phi)
    co=np.cos(k*u);si=np.sin(k*u)
    n=np.c_[u,v*co+w*si,-v*si+w*co]
    x=(1+epsilon*w)[:,None]*n
    return np.r_[x,x*np.array([-1.,-1.,1.]),[[0.,0.,1+epsilon+apex_extra]]]


def clipped_mass(X,triangles,height):
    zcut=-height;tris=[];boundary=[]
    for ids in triangles:
        face=X[ids];poly=[]
        for a,b in zip(face,np.roll(face,-1,axis=0)):
            ina=a[2]>=zcut;inb=b[2]>=zcut
            if ina:poly.append(a)
            if ina!=inb:
                t=(zcut-a[2])/(b[2]-a[2]);v=a+t*(b-a);v[2]=zcut
                poly.append(v);boundary.append(v)
        for j in range(1,len(poly)-1):tris.append([poly[0],poly[j],poly[j+1]])
    if len(boundary)>=3:
        boundary=np.unique(np.round(boundary,14),axis=0)
        # This ordered cap is only used for numerical integration. Final hull
        # incidence is rebuilt from the literal supporting halfspaces.
        cy=boundary[np.argsort(-np.arctan2(boundary[:,1],boundary[:,0]))]
        for j in range(1,len(cy)-1):tris.append([cy[0],cy[j],cy[j+1]])
    t=np.asarray(tris);six=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2]))
    volume=six.sum()/6
    if volume<=0:raise ValueError('Clipped oriented volume is nonpositive')
    g=np.sum(six[:,None]*t.sum(1),axis=0)/(4*six.sum())
    return g,volume


def run(out,trials=1200,seed=473216):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);rng=np.random.default_rng(seed)
    history=[];best=999;best_merit=np.inf;start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(trials=trials,seed=seed,
        scope='Direct literal convex hull, horizontal mass-balanced cut, and complete own-centroid numerical census; exact verification reserved for own110'),indent=2))
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes())
    for it in range(trials):
        m=int(rng.choice([20,25,30,35,39]));eps=float(rng.uniform(.08,.95))
        equation=lambda k:4*spherical_jn(1,k)/k+12*eps*eps*spherical_jn(2,k)/k**2
        k=float(brentq(equation,4.,6.)+rng.uniform(-.6,.6));phase=float(rng.uniform(0,np.pi));extra=float(rng.uniform(0,.25));power=float(rng.uniform(.65,1.6))
        parameters=dict(m=m,epsilon=eps,k=k,phase=phase,apex_extra=extra,power=power)
        X=points(**parameters)
        try:
            H=halfspaces(X);body=halfspace_mesh(H)
            if abs(body['g'][:2]).max()>1e-8:raise ValueError('Parent half-turn centroid symmetry failed')
            if body['g'][2]>=-1e-8:
                row=dict(trial=it,parameters=parameters,uncut_centroid=body['g'].tolist(),scope='A lower cut cannot move this positive centroid to zero')
            else:
                high=-body['X'][:,2].min()+1e-6
                fun=lambda h:float(clipped_mass(body['X'],body['triangles'],h)[0][2])
                height=float(brentq(fun,1e-6,high,xtol=1e-12))
                Q=np.r_[H,[[0.,0.,-1/height]]];cut=halfspace_mesh(Q);st=census(cut,0)
                if abs(cut['g']).max()>2e-9:raise ValueError('Independent final hull mass does not close at the chosen cut')
                row=dict(trial=it,parameters=parameters,cut_height=height,uncut_centroid=body['g'].tolist(),seconds=time.time()-start,**st)
                if 17<=st['E']<249:
                    merit=max(0,-st['min_primal_nonroot'])+max(0,-st['min_polar_nonroot'])
                    if st['S']+st['U']<best or merit<best_merit:
                        p=out/f'trial{it:05d}';p.mkdir();np.savez(p/'body.npz',Q=Q,X=cut['X'],input_points=X)
                        row['folder']=str(p.resolve());(p/'summary.json').write_text(json.dumps(row,indent=2));best=min(best,st['S']+st['U']);best_merit=min(best_merit,merit)
                        print('TWISTED_MASSCUT_BEST',json.dumps({k:v for k,v in row.items() if k not in ['S_ids','U_ids']}),flush=True)
                    if st['S']==st['U']==1 and min(st['min_primal_nonroot'],st['min_polar_nonroot'])>1e-10:
                        np.savez(out/'POTENTIAL_OWN110.npz',Q=Q,X=cut['X'],input_points=X)
                        (out/'POTENTIAL_OWN110.json').write_text(json.dumps(row,indent=2));return
        except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as error:
            row=dict(trial=it,parameters=parameters,error=repr(error))
        history.append(row)
        if it%20==0:(out/'history.json').write_text(json.dumps(history,indent=2))
    (out/'history.json').write_text(json.dumps(history,indent=2))
