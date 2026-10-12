"""Actual finite C2 hulls seeded from saved numerical support guides.

Point mode samples x=s*n+grad(s). Support mode samples n/s, with the support
profile sign chosen so the family's fixed axial roots have the right roles.
The declared diamond truncation and apex scaling produce a fresh physical
polyhedron. No smooth-body mass or census is inherited by it.
"""
import sys,json,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import brentq,minimize
from c2_twisted_ladder import Search as PointSearch,NumericalGoal,ROOT
from c2_dual_morse import Search as SupportSearch

def initial(profile,side,n=40,phase=0.,base_depth=.006,apex_gain=0.):
    k=profile['k'];a=np.array(profile['coefficients']);degrees=np.array(profile['degrees']);A=a.sum()
    def point(u):
        x,y,z=u;co=np.cos(k*z);si=np.sin(k*z);g=x*co-y*si;ge=np.array([co,-si,-k*(x*si+y*co)]);gs=ge-u*(u@ge);f=float((g**degrees)@a);df=float((degrees*g**(degrees-1))@a)
        if side=='point':return ((1+f)*u+df*gs)/(1+A)/(1+apex_gain)
        return (1-A)*u/(1-f)/(1+apex_gain)
    xb=-(1-A)/(1+A)/(1+apex_gain)+base_depth
    def section(alpha,axis):
        u=np.array([-np.cos(alpha),np.sin(alpha) if axis==1 else 0.,np.sin(alpha) if axis==2 else 0.]);return point(u)
    br=[]
    for axis in [1,2]:
        grid=np.linspace(0,np.pi/2,500);vals=[section(t,axis)[0]-xb for t in grid];j=next(j for j in range(1,len(grid)) if vals[j]>=0 and vals[j-1]<0);alpha=brentq(lambda x:section(x,axis)[0]-xb,grid[j-1],grid[j]);br.append(abs(section(alpha,axis)[axis]))
    pts=[];adjusted=[];gold=np.pi*(3-np.sqrt(5))
    for i in range(n):
        x=-1+2*(i+.6)/(n+.2);phi=(gold*i+phase)%np.pi;r=np.sqrt(1-x*x);p=point(np.array([x,r*np.cos(phi),r*np.sin(phi)]))
        if p[0]<=xb:p[0]=xb+.003*(1-xb);adjusted.append(i)
        if p[0]>=1:p[0]=.999;adjusted.append(i)
        pts.append(p)
    pts=np.array(pts);t=(pts[:,0]-xb)/(1-xb);q=np.r_[np.log(-xb),np.log(br),np.c_[np.log(t/(1-t)),pts[:,1:]].ravel()]
    return q,dict(side=side,profile=profile,base_depth=base_depth,apex_gain=apex_gain,phase=phase,adjusted_points=adjusted,scope='fresh finite physical hull; smooth census and centroid not inherited')

def run(src,out,side='point',n=40):
    src=Path(src);raw=src.read_bytes();profiles=json.loads(raw);profiles=[p for p in profiles if p['success'] and p['amplitude']>.03 and p['minimum_curvature_eigenvalue']>.005];profiles=sorted(profiles,key=lambda p:-p['amplitude'])[:4];out=Path(out);out.mkdir(parents=True,exist_ok=False);(out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),side=side),indent=2)+'\n');bounds=[(-4,1),(-4,1),(-4,1)]+[b for _ in range(n) for b in [(-8,8),(-3,3),(-3,3)]]
    for seed,profile in enumerate(profiles):
        q,definition=initial(profile,side,n,phase=.31*seed,base_depth=.006,apex_gain=.025 if seed%2 else 0.);(out/f'seed{seed:02d}_definition.json').write_text(json.dumps(definition,indent=2)+'\n')
        for stage,tau in enumerate([-1.,.03,.003,.0003]):
            s=PointSearch(out/f'seed{seed:02d}_stage{stage}',n,tau) if side=='point' else SupportSearch(out/f'seed{seed:02d}_stage{stage}',tau)
            try:opt=minimize(s.eval,q,jac=True,method='L-BFGS-B',bounds=bounds,options=dict(maxiter=700,maxls=40,maxcor=15,ftol=1e-13,gtol=1e-10))
            except NumericalGoal:(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(dict(folder=str(s.out)),indent=2)+'\n');print('GUIDE_NUMERICAL_REQUIRES_EXACT',str(s.out),flush=True);return
            q=np.load(s.out/'best_q.npy');history=s.hist if side=='point' else s.history;(s.out/'history.json').write_text(json.dumps(history,indent=2)+'\n');print('GUIDE_STAGE_DONE',seed,stage,s.fewest,opt.message,flush=True)
    (out/'FINITE_SEARCH_END.json').write_text(json.dumps(dict(profiles=len(profiles),side=side,goal_complete=False),indent=2)+'\n')

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],sys.argv[3] if len(sys.argv)>3 else 'point')
