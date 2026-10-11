"""Explicit mass-feasibility constrained optimization of the U1 shadow family.

The nonpositive initial axial centroid is an explicit inequality. This allows
the optimizer to move tangentially along that boundary rather than stalling at
the apex-closure kink. A base-height inequality preserves the genuine basal
quadrilateral and the <=248-edge input bound. Exact final audit is mandatory.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from c2_shadow_radial_goal import Family
from vertex_geometry import geometry
from goal_nomination import preserve

def run(source,out,steps,seed):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);original=np.load(source);F=Family(original,eta=.01,radial_costs=True);q=F.q.copy();q[-1]=0;X,_,_=F.construct(q);q[-1]=float(np.clip(1-(original[0,2]/original[-1,2])/X[0,2],1e-5,.6))
    bounds=[(-1.55,1.55),(-20,20)]*F.n+[(-1.55,-.05),(-20,20)]*2+[(1e-8,2.)]*F.n+[(1e-5,.6)]
    cache={};calls=0;best=np.inf;start=time.time();trace=[]
    def constraint(q):
        key=q.tobytes()
        if cache.get('key')==key:return cache['value'],cache['J']
        X,DX,_=F.construct(q);g=geometry(X);Jg=g['Dg']@DX.reshape(X.size,F.d);val=np.r_[-g['g'][2]-1e-9,X[4:-1,2]-X[0,2]-1e-5];J=np.vstack((-Jg[2],DX[4:-1,2]-DX[0,2]));cache.update(key=key,value=val,J=J);return val,J
    initial=constraint(q)[0];(out/'initial_constraints.json').write_text(json.dumps(dict(axial_mass=float(initial[0]),min_base_gap=float(min(initial[1:]))),indent=2));np.save(out/'initial_parameters.npy',q)
    rng=np.random.default_rng(seed);t=q.copy();t[F.ad:-1]=np.maximum(t[F.ad:-1],1e-4);d=rng.normal(size=len(q));d/=np.linalg.norm(d);h=2e-8;v,J=constraint(t);fd=(constraint(t+h*d)[0]-constraint(t-h*d)[0])/(2*h);err=float(max(abs(fd-J@d)));(out/'constraint_gradient_check.json').write_text(json.dumps(dict(max_error=err),indent=2));assert err<2e-5
    def objective(q):
        nonlocal calls,best
        calls+=1;v,J,X,row,meta=F.evaluate(q);c,_=constraint(q);feasible=min(c)>=-1e-10;row.update(calls=calls,constraint_min=float(min(c)),feasible=bool(feasible),seconds=time.time()-start)
        if feasible and v<best:
            best=v;trace.append(row);np.save(out/'best_parameters.npy',q);np.save(out/'best.npy',X);(out/'best.json').write_text(json.dumps(row,indent=2));(out/'construction.json').write_text(json.dumps(meta,indent=2))
        if row['closed']and row['base_valid']and row['reference_S']==row['actual_U']==1:
            preserve(X,out/f'exact_goal_{calls:06d}','C2 radial shadow construction with explicit physical mass feasibility and numerical actual110')
        if calls%100==1:print('C2_SHADOW_SQP_GOAL',out,row,flush=True)
        return v,J
    r=minimize(objective,q,jac=True,method='SLSQP',bounds=bounds,constraints=[dict(type='ineq',fun=lambda q:constraint(q)[0],jac=lambda q:constraint(q)[1])],options=dict(maxiter=steps,ftol=1e-11,disp=False))
    np.save(out/'endpoint_parameters.npy',r.x);(out/'trace.json').write_text(json.dumps(trace,indent=2));(out/'result.json').write_text(json.dumps(dict(message=str(r.message),iterations=int(r.nit),calls=calls,best_feasible=best if np.isfinite(best)else None,constraint_min=float(min(constraint(r.x)[0]))),indent=2));print('C2_SHADOW_SQP_FINITE_STOP',out,str(r.message),calls,best,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=700);p.add_argument('--seed',type=int,default=774051);a=p.parse_args();run(a.source,a.out,a.steps,a.seed)
