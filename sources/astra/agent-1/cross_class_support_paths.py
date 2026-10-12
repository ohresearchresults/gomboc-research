"""Physical support paths between own211 and own121 bodies.

Both endpoints are centred by their true uniform volume centroid. Orthogonal
alignment and positive scaling preserve that fact only at endpoints; every
intermediate hull is integrated afresh. At most84 supplied support vectors
guarantee E<=246 for every genuine full dimensional bounded hull. Matching is
only a search parametrization, never an incidence or equilibrium certificate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,pathlib,json,time
import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.spatial.transform import Rotation
from fractions import Fraction
from geometry import halfspace_mesh,arrows,census
from persistence_search import pairs,polar_edges
from soft_forest_polish import run as polish

def load(p):
    p=pathlib.Path(p)
    if p.suffix=='.npz':Q=np.load(p)['Q']
    else:
        H=json.loads(p.read_text())['H'];Q=np.array([[float(Fraction(x,row[3])) for x in row[:3]] for row in H])
    m=halfspace_mesh(Q);R=np.sqrt(np.mean(np.sum((m['X']-m['g'])**2,axis=1)));Q=Q[m['active']]/(1-Q[m['active']]@m['g'])[:,None]*R;return Q

def frame(s,u):
    a=s/np.linalg.norm(s);b=u-a*(u@a);b/=np.linalg.norm(b);return np.stack([a,b,np.cross(a,b)],axis=1)

def record(Q):
    m=halfspace_mesh(Q);bars=[]
    for A,edges in [(m['X']-m['g'],m['edges']),(Q/(1-Q@m['g'])[:,None],polar_edges(m))]:
        pp,h=pairs(A,edges);bars.append((1-h[pp[:,1]]/(A[pp[:,0]]**2).sum(1)).tolist())
    return dict(P=bars[0],Q=bars[1],score=float(sum(.001*np.log1p(np.array(bs)/.001).sum() for bs in bars)),**census(m,0))

def run(a,b,out,orientations=72,seed=931209,repairs=10):
    out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);A=load(a);B=load(b);N=max(len(A),len(B));assert N<=84;ma,mb=halfspace_mesh(A),halfspace_mesh(B);sa=np.flatnonzero(arrows(A).max(1)<0);ua=np.flatnonzero(arrows(ma['X']-ma['g']).max(1)<0);sb=np.flatnonzero(arrows(B).max(1)<0);ub=np.flatnonzero(arrows(mb['X']-mb['g']).max(1)<0);assert len(sa)==2 and len(ua)==1 and len(sb)==1 and len(ub)==2
    A=np.r_[A,np.zeros((N-len(A),3))];B=np.r_[B,np.zeros((N-len(B),3))];np.savez(out/'endpoints.npz',A=A,B=B);rng=np.random.default_rng(seed);rows=[];candidates=[];best=1.;start=time.time();ts=np.unique(np.r_[np.linspace(.025,.975,39),1e-5,1e-4,.001,.005,.995,.999,.9999,.99999]);(out/'definition.json').write_text(json.dumps(dict(a=str(pathlib.Path(a).resolve()),b=str(pathlib.Path(b).resolve()),seed=seed,N=N,orientations=orientations,t=ts.tolist(),scope='Finite interpolated physical support bodies at their separately integrated uniform centroids'),indent=2))
    for k in range(orientations):
        i=sa[(k//2)%2];j=ub[k%2];R=frame(A[i],ma['X'][ua[0]]-ma['g'])@frame(B[sb[0]],mb['X'][j]-mb['g']).T
        if k>=4:
            axis=A[i]/np.linalg.norm(A[i]);angle=rng.uniform(-np.pi,np.pi);R=Rotation.from_rotvec(axis*angle).as_matrix()@R
            if k%3==0:R=Rotation.from_rotvec(rng.normal(size=3)*.4).as_matrix()@R
        if k%5==4:R=R@np.diag([1,1,-1])
        BB=B@R.T;na=np.linalg.norm(A,axis=1);nb=np.linalg.norm(BB,axis=1);cost=1-(A/np.maximum(na[:,None],1e-30))@(BB/np.maximum(nb[:,None],1e-30)).T+.07*(np.log(np.maximum(na,1e-6))[:,None]-np.log(np.maximum(nb,1e-6))[None,:])**2;ia,ib=linear_sum_assignment(cost);assert np.array_equal(ia,np.arange(N));BB=BB[ib]
        for t in ts:
            Q=(1-t)*A+t*BB
            try:
                r=record(Q);r.update(orientation=k,t=float(t));rows.append(r)
                if not 17<=r['E']<249:raise ValueError('support-count complexity invariant failed')
                if r['score']<best:
                    best=r['score'];np.savez(out/'best.npz',Q=Q);(out/'best.json').write_text(json.dumps(r,indent=2));print('CROSS_CLASS_BEST',json.dumps({x:r[x] for x in ['orientation','t','score','S','U','E']}),flush=True)
                if r['S']==r['U']==1 and min(r['min_primal_nonroot'],r['min_polar_nonroot'])>1e-9:
                    np.savez(out/'POTENTIAL_OWN110.npz',Q=Q);(out/'history.json').write_text(json.dumps(rows,indent=2));return
                if .05<t<.95:
                    candidates.append((r['score'],k,float(t),Q.copy(),r));candidates=sorted(candidates,key=lambda x:x[0])[:80]
            except (ValueError,RuntimeError,np.linalg.LinAlgError) as error:rows.append(dict(orientation=k,t=float(t),error=repr(error)))
        (out/'history.json').write_text(json.dumps(rows,indent=2));print('CROSS_CLASS_ORIENTATION',k,'best',best,'seconds',time.time()-start,flush=True)
    selected=[]
    for _,k,t,Q,r in candidates:
        if any(abs(t-u)<.12 and k==j for j,u in selected):continue
        selected.append((k,t));p=out/f'repair{len(selected)-1:02d}-orientation{k:03d}';p.mkdir();np.savez(p/'input.npz',Q=Q);(p/'input.json').write_text(json.dumps(r,indent=2))
        try:
            q=polish(Q,p/'actual110',nP=1,nQ=1,steps=140,apex=False);s=record(q);(p/'result.json').write_text(json.dumps(s,indent=2));np.savez(p/'final.npz',Q=q)
            if s['S']==s['U']==1 and min(s['min_primal_nonroot'],s['min_polar_nonroot'])>1e-9:
                np.savez(out/'POTENTIAL_OWN110.npz',Q=q);return
        except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as error:(p/'error.txt').write_text(repr(error))
        if len(selected)>=repairs:break

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--a',required=True);p.add_argument('--b',required=True);p.add_argument('--out',required=True);p.add_argument('--orientations',type=int,default=72);p.add_argument('--repairs',type=int,default=10);a=p.parse_args();run(a.a,a.b,a.out,a.orientations,repairs=a.repairs)
