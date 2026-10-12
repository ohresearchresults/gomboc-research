# material-fc31d4ddabed

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Finite polar/metric search by direct all-vertex escape inequalities.
Numerical discovery only; complete exact primitive audit remains necessary.
Required local source units: h44_lead_probe.py, h44_polar_orbit.py.
"""
import argparse,json,time,platform
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import minimize
from h44_polar_orbit import Q0,ED,DE,vertices,mesh,census,centroid

def escape(Y,E):
    d=Y[E[:,1]]-Y[E[:,0]]
    nr=np.linalg.norm(Y,axis=1);nd=np.linalg.norm(d,axis=1)
    s=np.einsum('ij,ij->i',Y[E[:,0]],d)/(nr[E[:,0]]*nd)
    t=-np.einsum('ij,ij->i',Y[E[:,1]],d)/(nr[E[:,1]]*nd)
    best=np.full(len(Y),-np.inf)
    np.maximum.at(best,E[:,0],s);np.maximum.at(best,E[:,1],t)
    # The furthest vertex is necessarily an unstable root.
    root=int(np.argmax(nr));return np.delete(best,root),root

def residual(x,margin=1e-4):
    V=vertices(x);_,g,Q,_,_=mesh(V)
    a,ra=escape(V-g,ED);b,rb=escape(Q,DE)
    # Smooth hinge except at changing witnesses and roots. No small-bar discard.
    return np.maximum(margin-np.r_[a,b],0),[ra,rb]

def loss(x,margin=1e-4,power=1):
    try:
        r,_=residual(x,margin)
        return float(np.sum(r**power))
    except (ValueError,FloatingPointError,np.linalg.LinAlgError):return 100.+float(np.linalg.norm(x))

def main():
    p=argparse.ArgumentParser();p.add_argument('--steps',type=int,default=12);p.add_argument('--seed',type=int,default=24092026);p.add_argument('--out',default='H44_polar_witness.json');p.add_argument('--margin',type=float,default=1e-4);p.add_argument('--power',type=float,default=1.);p.add_argument('--start');a=p.parse_args()
    rng=np.random.default_rng(a.seed);best=None;ledger=[];t0=time.monotonic()
    starts=[np.r_[centroid,np.zeros(5)],np.zeros(8),np.array([-.45270851603684054,-.27519232193358595,-.06095950845168827,0,0,0,0,0])]
    if a.start:starts.insert(0,np.array(json.loads(Path(a.start).read_text())['best']['x']))
    bounds=[(-2.,2.)]*3+[(-1.5,1.5)]*2+[(-2.,2.)]*3
    for i in range(a.steps):
        if i<len(starts):x=starts[i].copy()
        elif i%3==0:x=rng.normal(0,.5,8)
        else:x=np.array(best['x'])+rng.normal(0,.1 if i%2 else .35,8)
        mx=float(np.max(Q0@x[:3]));x[:3]/=max(1.,mx/.75)
        x=np.clip(x,np.array(bounds)[:,0],np.array(bounds)[:,1])
        r=minimize(lambda z:loss(z,a.margin,a.power),x,method='SLSQP',bounds=bounds,constraints=[{'type':'ineq','fun':lambda z:1-Q0@z[:3]-1e-3}],options={'ftol':1e-11,'maxiter':300,'eps':1e-6})
        try:
            au=census(vertices(r.x));counts=[len(au['S']),len(au['U']),len(au['H'])]
            rr,roots=residual(r.x,a.margin)
            entry={'index':i,'x':r.x.tolist(),'loss':float(r.fun),'counts':counts,'weak_counts':[len(w) for w in au['weak']],'max_residual':float(max(rr)),'residual_count':int(np.count_nonzero(rr)),'roots':roots,'nit':int(r.nit),'success':bool(r.success),'message':str(r.message),'P':len(au['P']),'Q':len(au['Q'])}
        except (ValueError,np.linalg.LinAlgError) as ex:
            ledger.append({'index':i,'invalid':str(ex)});continue
        ledger.append(entry)
        if best is None or r.fun<best['loss']:
            best={'x':r.x.tolist(),'loss':float(r.fun),'audit':au};print('POLAR_WITNESS_BEST',i,r.fun,counts,entry['residual_count'],flush=True)
        payload={'status':'numerical_not_exact','environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'seed':a.seed,'steps_requested':a.steps,'margin':a.margin,'power':a.power,'start_file':a.start,'ledger':ledger,'best':best,'elapsed_seconds':time.monotonic()-t0}
        Path(a.out).write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
        if counts==[1,1,0] and not any(au['weak']):print('NUMERICAL_OWN110_CANDIDATE_NOT_CERTIFIED',flush=True);break
if __name__=='__main__':main()
