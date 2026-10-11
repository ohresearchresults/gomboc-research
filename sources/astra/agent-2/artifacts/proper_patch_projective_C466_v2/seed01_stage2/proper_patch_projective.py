"""A proper physical patch, followed by explicit projective and affine maps.

The cutting plane is always an interior quantile of the old vertex projections,
so both pieces are represented. All operations act on the SAME physical point
set and the final homogeneous centroid is integrated after every transformation.
No independent primal/polar metric is used. Numeric nominations only.
"""
import sys,json,time,hashlib
from pathlib import Path
import numpy as np
import cma
from gmpy2 import mpq
from selected_projective import load
from piecewise_affine_patch import hull
from support_persistence import ROOT

class Search:
    def __init__(self,src,out,tau=-1):
        self.src=Path(src);self.out=Path(out);self.out.mkdir(parents=True,exist_ok=False)
        X,Y,tri,eu,es,r=load(self.src);self.center=np.array([float(mpq(x)) for x in r['raw_centroid']]);X-=self.center;Y/= (1-Y@self.center)[:,None]
        self.radius=np.max(np.linalg.norm(X,axis=1));self.X=X/self.radius
        sr=int(np.argmax((Y*Y).sum(1)));target=next(i for i in r['stable_face_ids'] if i!=sr);self.n=Y[target]/np.linalg.norm(Y[target]);e=np.eye(3)[np.argmin(abs(self.n))];self.a=np.cross(self.n,e);self.a/=np.linalg.norm(self.a);self.b=np.cross(self.n,self.a)
        self.tau=tau;self.best=np.inf;self.fewest=(999,np.inf);self.goal=False;self.calls=0;self.start=time.time();self.hist=[]
        meta=dict(source=str(src),source_sha256=hashlib.sha256(self.src.read_bytes()).hexdigest(),center=self.center.tolist(),radius=float(self.radius),n=self.n.tolist(),a=self.a.tolist(),b=self.b.tolist(),target=target,tau=tau,scope='complete physical transform; discovery coplanarity grouping only, requires exact physical audit')
        (self.out/'source.json').write_text(json.dumps(meta,indent=2)+'\n')
        for name in ['proper_patch_projective.py','piecewise_affine_patch.py']:
            p=Path(__file__).with_name(name);(self.out/name).write_bytes(p.read_bytes())

    def transform(self,t):
        t=np.asarray(t)
        if max(abs(t[:3]))>4 or abs(t[3])>6 or max(abs(t[4:6]))>2 or max(abs(t[6:9]))>1.5 or max(abs(t[9:]))>1.5:raise ValueError('outside parameter box')
        n=self.n+t[4]*self.a+t[5]*self.b;n/=np.linalg.norm(n)
        fraction=.08+.84/(1+np.exp(-t[3]));d=float(np.quantile(self.X@n,fraction));height=np.maximum(self.X@n-d,0)
        assert (height>0).any() and (height==0).any()
        P=self.X+height[:,None]*t[:3];B=t[6:9];den=1+P@B
        if den.min()<=.15:raise ValueError('projective denominator too small')
        L=np.array([[np.exp(t[9]),0,0],[t[11],np.exp(t[10]),0],[t[12],t[13],np.exp(-t[9]-t[10])]])
        return (P/den[:,None])@L,dict(normal=n.tolist(),cut_offset=d,patch_vector=t[:3].tolist(),projective_B=B.tolist(),affine_L=L.tolist(),warped=int((height>0).sum()),unwarped=int((height==0).sum()),cut_fraction=float(fraction),minimum_denominator=float(den.min()))

    def eval(self,t):
        self.calls+=1
        try:X,transform=self.transform(t);s=hull(X,full=True)
        except (ValueError,np.linalg.LinAlgError,AssertionError):return 1e3
        P,Q=s['P_bars'],s['Q_bars']
        value=s['loss'] if self.tau<0 else float(np.log1p(P/self.tau).sum()+np.log1p(Q/self.tau).sum())
        penalty=(1e-4 if self.tau<0 else .05)*max(0,s['E']-248)**2
        value+=penalty
        row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','loss','centroid','volume','minimum_nonroot','grouping_tolerance']};row.update(t=list(map(float,t)),transform=transform,objective=value,tau=self.tau,calls=self.calls,seconds=time.time()-self.start)
        if value<self.best:
            self.best=value;np.save(self.out/'best.npy',X);np.save(self.out/'best_t.npy',t);(self.out/'best.json').write_text(json.dumps(row,indent=2)+'\n')
        few=(s['S']+s['U'],s['loss'])
        if s['E']<=248 and few<self.fewest:
            self.fewest=few;self.hist.append(row);np.save(self.out/'fewest.npy',X);(self.out/'fewest.json').write_text(json.dumps(row,indent=2)+'\n');print('PROPER_PATCH_FEWEST',row,flush=True)
        if s['E']<=248 and s['S']==s['U']==1:
            self.goal=True;np.save(self.out/'NUMERICAL_NOMINATION.npy',X);(self.out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');print('NUMERICAL_REQUIRES_EXACT',row,flush=True)
        if self.calls%500==0:print('PROPER_PATCH_CALLS',self.calls,'best',self.best,'fewest',self.fewest,flush=True)
        return value

def run(src,out,starts=4):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);rng=np.random.default_rng(829102)
    for seed in range(starts):
        t=np.zeros(14);t[3]=[-2,-.5,.5,2][seed%4];t+=rng.normal(size=14)*.015
        for stage,tau in enumerate([-1,.02,.002]):
            s=Search(src,out/f'seed{seed:02d}_stage{stage}',tau)
            solver=cma.CMAEvolutionStrategy(t,.06 if stage==0 else .015,dict(seed=18333+31*seed+stage,popsize=18,maxiter=130,verbose=-9,tolfun=1e-12,tolx=1e-8))
            while not solver.stop() and not s.goal:
                xx=solver.ask();solver.tell(xx,[s.eval(x) for x in xx])
            (s.out/'history.json').write_text(json.dumps(s.hist,indent=2)+'\n')
            if s.goal:
                (out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(dict(stage=str(s.out)),indent=2)+'\n');return
            t=np.load(s.out/'best_t.npy');print('PROPER_PATCH_STAGE_DONE',seed,stage,s.best,s.fewest,flush=True)
    (out/'FINITE_SEARCH_END.json').write_text(json.dumps(dict(starts=starts,goal_complete=False),indent=2)+'\n')

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 4)
