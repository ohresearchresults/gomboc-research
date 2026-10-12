"""Convex hulls after a literal rank-one affine warp of a physical cap.

P(x)=x+a*max(0,n.x-d), followed by taking the convex hull of the resulting
points. Planes inside each affine piece remain planes; crossing facets may
split or disappear. These changes are not constrained to an old contact chart.
The true input-point hull, uniform centroid and both persistence graphs are
rebuilt at each trial. Numeric coplanar grouping is ONLY discovery; exact
rational source transforms and an independent hull audit are needed to accept.
"""
import sys,json,time,hashlib
from pathlib import Path
from collections import defaultdict
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import minimize
from gmpy2 import mpq
from selected_projective import load
from geometry import mass,angular_scores
from support_persistence import ROOT,barcode

def hull(points,tol=2e-8):
    h=ConvexHull(points);T=h.simplices.copy()
    a,b,c=points[T[:,0]],points[T[:,1]],points[T[:,2]]
    flip=np.einsum('ij,ij->i',np.cross(b-a,c-a),h.equations[:,:3])<0
    T[flip]=T[flip][:,[0,2,1]]
    vol,g=mass(points,T)
    if vol<=0:raise ValueError('nonpositive mass')
    offsets=-h.equations[:,3]-h.equations[:,:3]@g
    if min(offsets)<=0:raise ValueError('centroid not interior')
    Q=h.equations[:,:3]/offsets[:,None]
    # Record and later exactly audit this numerical grouping. Integration
    # triangles do not themselves contribute to the nominated facet count.
    groups=[];labels=[]
    for q in Q:
        k=next((j for j,p in enumerate(groups) if np.linalg.norm(q-p)<=tol*max(1,np.linalg.norm(q),np.linalg.norm(p))),None)
        if k is None:k=len(groups);groups.append(q)
        labels.append(k)
    adj=defaultdict(list)
    for k,t in enumerate(T):
        for i,j in zip(t,np.roll(t,-1)):adj[tuple(sorted((int(i),int(j))))].append(labels[k])
    assert all(len(v)==2 for v in adj.values())
    eu=np.array([e for e,ff in adj.items() if ff[0]!=ff[1]],int)
    es=np.array([ff for ff in adj.values() if ff[0]!=ff[1]],int)
    Q=np.array(groups);Z=points-g;mask=np.zeros(len(points));mask[h.vertices]=1
    # Euler is a guard against an inconsistent approximate grouping.
    if len(h.vertices)-len(eu)+len(Q)!=2:raise ValueError('coplanar grouping Euler failure')
    pp,pw,P=barcode(Z,mask,eu);qp,qw,B=barcode(Q,np.ones(len(Q)),es)
    P/=np.maximum(np.sum(Z[pp[:,0]]**2,axis=1),1e-30);B/=np.sum(Q[qp[:,0]]**2,axis=1)
    us=angular_scores(Z[h.vertices]).max(1);ss=angular_scores(Q).max(1)
    return dict(V=len(h.vertices),E=len(eu),F=len(Q),S=int((ss<0).sum()),U=int((us<0).sum()),Pmax=float(P.max()),Qmax=float(B.max()),loss=float(P@P+B@B),centroid=g.tolist(),volume=float(vol),minimum_nonroot=float(min(np.sort(us)[1],np.sort(ss)[1])),T=T,points=points,facet_representatives=Q,grouping_tolerance=tol)

class Search:
    def __init__(self,src,out):
        self.src=Path(src);self.out=Path(out);self.out.mkdir(parents=True,exist_ok=False)
        X,Y,tri,eu,es,r=load(self.src);self.center=np.array([float(mpq(x)) for x in r['raw_centroid']]);self.X=X-self.center
        Y=Y/(1-Y@self.center)[:,None];elder=int(np.argmax(np.sum(Y**2,1)));target=next(i for i in r['stable_face_ids'] if i!=elder)
        self.n=Y[target]/np.linalg.norm(Y[target]);e=np.eye(3)[np.argmin(abs(self.n))];self.a=np.cross(self.n,e);self.a/=np.linalg.norm(self.a);self.b=np.cross(self.n,self.a)
        self.radius=np.max(np.linalg.norm(self.X,axis=1));self.X/=self.radius
        self.best=np.inf;self.bestfew=(999,999);self.calls=0;self.history=[];self.goal=False;self.start=time.time()
        (self.out/'source.json').write_text(json.dumps(dict(source=str(self.src),sha256=hashlib.sha256(self.src.read_bytes()).hexdigest(),center=self.center.tolist(),radius=float(self.radius),target=target,n=self.n.tolist(),a=self.a.tolist(),b=self.b.tolist(),scope='all counts are numerical nominations; exact source affine transform is required'),indent=2)+'\n')
    def points(self,t):
        # Normal tilts remain declared physical parameters, not a polar metric.
        normal=self.n+t[4]*self.a+t[5]*self.b;normal/=np.linalg.norm(normal)
        return self.X+np.maximum(self.X@normal-t[3],0)[:,None]*np.array(t[:3])[None,:],normal
    def eval(self,t):
        self.calls+=1
        if abs(t[3])>1.5 or max(abs(np.array(t[:3])))>5 or max(abs(np.array(t[4:])))>2:return 100.
        X,n=self.points(t)
        try:s=hull(X)
        except (ValueError,QhullError,np.linalg.LinAlgError,AssertionError):return 100.
        value=s['loss']+1e-4*max(0,s['E']-248)**2
        row={k:v for k,v in s.items() if k not in ['T','points','facet_representatives']};row.update(t=list(map(float,t)),normal=n.tolist(),calls=self.calls,objective=value,seconds=time.time()-self.start)
        if value<self.best:
            self.best=value;np.save(self.out/'best.npy',X);np.save(self.out/'best_t.npy',t);(self.out/'best.json').write_text(json.dumps(row,indent=2)+'\n')
        few=(s['S']+s['U'],s['loss'])
        if s['E']<=248 and few<self.bestfew:
            self.bestfew=few;self.history.append(row);np.save(self.out/'fewest.npy',X);(self.out/'fewest.json').write_text(json.dumps(row,indent=2)+'\n');print('PATCH_FEWEST',row,flush=True)
        if s['E']<=248 and s['S']==s['U']==1:
            self.goal=True;np.save(self.out/'NUMERICAL_NOMINATION.npy',X);(self.out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');print('NUMERICAL_REQUIRES_EXACT',row,flush=True)
        if self.calls%500==0:(self.out/'history.json').write_text(json.dumps(self.history,indent=2)+'\n');print('PATCH_CALLS',self.calls,'best',self.best,'fewest',self.bestfew,flush=True)
        return value

def run(src,out,starts=12):
    import cma
    obj=Search(src,out);rng=np.random.default_rng(203941)
    projection=obj.X@obj.n
    obj.eval(np.r_[np.zeros(3),np.median(projection),np.zeros(2)])
    for seed in range(starts):
        if seed<6:
            t=np.r_[rng.normal(size=3)*.04,np.quantile(projection,[.1,.3,.5,.7,.85,.95][seed]),np.zeros(2)]
        else:
            t=np.load(obj.out/'best_t.npy')+rng.normal(size=6)*.1
        solver=cma.CMAEvolutionStrategy(t,.12,dict(seed=29381+seed,verbose=-9,popsize=14,maxiter=180,tolfun=1e-12,tolx=1e-8))
        while not solver.stop() and not obj.goal:
            xs=solver.ask();solver.tell(xs,[obj.eval(x) for x in xs])
        if obj.goal:break
        # A finite six-parameter local refinement. Objective still re-hulls.
        opt=minimize(obj.eval,solver.result.xbest,method='Powell',options=dict(maxiter=60,ftol=1e-9,xtol=1e-7))
        print('PATCH_SEED_DONE',seed,opt.fun,obj.best,flush=True)
    (obj.out/'history.json').write_text(json.dumps(obj.history,indent=2)+'\n');print('FINITE_PATCH_SEARCH_DONE',obj.calls,obj.bestfew,flush=True)

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 12)
