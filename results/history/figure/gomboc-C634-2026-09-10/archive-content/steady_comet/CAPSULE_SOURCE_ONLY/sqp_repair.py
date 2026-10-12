from pathlib import Path
import json,time,numpy as np
from scipy.optimize import minimize
from atlas_opt import Atlas
from numeric import *
from tree_repair import assign_trees

def sqp_repair(gen,faces,outbase,tree=True,steps=250,goal=3e-5,radius=.05):
    m=Atlas(gen,faces)
    if tree:
        trees=assign_trees(m);Path(str(outbase)+'_TREES.json').write_text(json.dumps({k:[int(t) for t in v] if isinstance(v,list) else v for k,v in trees.items()},separators=(',',':')))
    st0=m.state(m.u0);vi,qi=np.where((st0['gaps']<.25)&(~m.inc));print('SQP_BEGIN','np',m.np,'geo',len(vi),'min',st0['vals'].min(),'tree',tree,flush=True)
    cached_u=None;cached=None;count=0;start=time.time();best=m.u0.copy();bestval=-np.inf
    def state(u):
        nonlocal cached_u,cached
        if cached_u is None or not np.array_equal(cached_u,u):cached=m.state(u);cached_u=u.copy()
        return cached
    def obj(u):d=u-m.u0;return 0.5*np.dot(d,d)
    def oj(u):return u-m.u0
    def co(u):
        s=state(u);return np.r_[s['vals']-goal,s['gaps'][vi,qi]-1e-7]
    def cj(u):
        s=state(u);return np.vstack([s['J'],m.gap_jac(s,vi,qi)])
    def cb(u):
        nonlocal count,best,bestval
        count+=1;s=state(u);mng=s['gaps'][~m.inc].min();v=s['vals'].min()
        if mng>0 and s['det'].min()>0 and v>bestval:bestval=v;best=u.copy()
        if count%5==0:print('SQP',count,'time',time.time()-start,'esc',v,'gap',mng,'obj',obj(u),flush=True)
    res=minimize(obj,m.u0,jac=oj,method='SLSQP',bounds=list(zip(m.u0-radius,m.u0+radius)),constraints=[{'type':'ineq','fun':co,'jac':cj}],callback=cb,options={'maxiter':steps,'ftol':1e-12,'disp':True})
    for label,u in [('final',res.x),('best',best)]:
        z=m.save(u,str(outbase)+'_'+label+'_GENERATOR.json');Path(str(outbase)+'_'+label+'_faces.json').write_text(json.dumps(faces,separators=(',',':')))
        rr=mechanics(recover(z)[:z['n_supports']],faces,tol=1e-10);print('SQP_RESULT',label,res.message,rr,flush=True)
        Path(str(outbase)+'_'+label+'_numeric.json').write_text(json.dumps(rr,indent=2))

if __name__=='__main__':
    R=Path(__file__).parent;g=json.loads((R/'C642_CONTACT_69_71_GENERATOR.json').read_text());fs=json.loads((R/'C642_CONTACT_69_71_faces.json').read_text())
    for a,b,moved in [(118,121,17),(173,175,123),(111,115,21)]:
        z,ff=snapped(g,fs,a,b,moved)
        sqp_repair(z,ff,R/f'SQP_E320_{a}_{b}_q{moved}',tree=True,steps=150,goal=3e-5,radius=.05)
