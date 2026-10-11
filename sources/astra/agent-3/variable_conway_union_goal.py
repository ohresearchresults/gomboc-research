"""Direct own-centroid Figure search in three independently thickened spirals.

Three convex Conway-based pyramids share one radial root after physical
rotations and scaling. Their convex union is filled uniformly. Unequal apex
positions/heights and arbitrary inter-plane angles supply mass compensation;
no symmetry or inherited centroid is presumed. <=82 inputs gives E<=240.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from vertex_geometry import geometry
from support_geometry import escape
from shadow_mass_retracted_goal import bars as qbars
from dual_shadow_goal import bars as pbars
from goal_nomination import preserve

def construct(q,n=14):
    logits=np.r_[q[:n-1],0.];weights=np.exp(logits);alpha=np.pi*weights/weights.sum();eps=q[n-1];af=q[n:n+3];hf=q[n+3:n+6];angles=np.r_[0.,q[n+6:n+8]];theta=-np.pi/2+np.cumsum(alpha);factors=np.cos(alpha+eps)/np.cos(eps);r=np.r_[np.cumprod(factors[:0:-1])[::-1],1.];x=r*np.cos(theta);x[-1]=0.;y=r*np.sin(theta);base=np.column_stack((np.r_[x,-x[-2::-1]],np.r_[y,y[-2::-1]]));nxt=np.roll(base,-1,axis=0);cr=base[:,0]*nxt[:,1]-base[:,1]*nxt[:,0];A=cr.sum()/2;by=float(np.sum(cr*(base[:,1]+nxt[:,1]))/(6*A));bottom=float(min(base[:,1]));parts=[];gy=[]
    assert min(alpha)>eps and max(alpha+eps)<np.pi/2
    for a,h,t in zip(af,hf,angles):
        ay=bottom+a*(by-bottom);az=h*np.sqrt((by-ay)*(ay-bottom));g=np.array([0.,(3*by+ay)/4,az/4]);gy.append(g[1]);X=np.vstack((np.column_stack((base,np.zeros(len(base)))),[0.,ay,az]))-g;root=n-1;Rr=np.linalg.norm(X[root]);u=X[root]/Rr;e=np.array([1.,0.,0.]);R=np.array([e,np.cross(u,e),u]);X=X@R.T/Rr;X=np.delete(X,root,axis=0);c,s=np.cos(t),np.sin(t);rot=np.array([[c,-s,0.],[s,c,0.],[0.,0.,1.]]);parts.append(X@rot.T)
    return np.vstack((*parts,[[0.,0.,1.]])),np.array(gy)

def run(out,seeds=12,steps=450):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);n=14;dim=n+8;bounds=[(-1.,1.)]*(n-1)+[(1e-4,.01745)]+[(.01,.95)]*3+[(.05,.999)]*3+[(0.,2*np.pi)]*2;assert len(bounds)==dim;rng=np.random.default_rng(852370);allrows=[]
    (out/'method.json').write_text(json.dumps(dict(n=n,copies=3,maximum_points=82,maximum_edges=240,parameters='13 logarithmic angular weights, positive spiral angle excess, three apex fractions, three height fractions, two inter-copy angles',physical_definition='uniform filled convex hull of literal point copies; centroid integrated on every proposal; all own nonroot vertex escapes constrained'),indent=2))
    for seed in range(seeds):
        d=out/f'seed{seed:02d}';d.mkdir();q=np.r_[rng.normal(0,.05,n-1),.00349,[.28,.28,.28],[.98,.98,.98],[np.pi,np.pi+.03]]
        if seed:
            q[:n-1]=rng.uniform(-.25,.25,n-1);q[n:n+3]=rng.uniform(.1,.3,3);q[n+3:n+6]=rng.uniform(.6,.99,3);q[-2:]=[np.pi+rng.normal(0,.15),np.pi+rng.normal(0,.15)]
        np.save(d/'initial_parameters.npy',q);cache={};calls=0;trace=[];start=time.time();best=None
        def evaluate(q):
            nonlocal calls,best
            if 'q'in cache and np.array_equal(cache['q'],q):return cache['objective'],cache['constraints']
            X,gy=construct(q,n);g=geometry(X,False);uv,_=escape(g['Z'],angular=True);constraints=np.r_[uv[:-1]-1e-8,-gy-1e-6];Q=qbars(g,False)[0];qm=float(max(Q,default=0.));edges=set()
            for tri in g['T']:
                for i,j in zip(tri,np.roll(tri,-1)):edges.add(tuple(sorted((int(i),int(j)))))
            g['edges']=np.array(list(edges));P=pbars(g,False)[0];pm=float(max(P,default=0.));calls+=1;us=int(sum(uv[g['vertices']]<0));row=dict(call=calls,Qmax=qm,Pmax=pm,U=us,positive_Q=len(Q),minimum_nonroot_escape=float(min(uv[:-1])),pyramid_gy=gy.tolist(),actual_centroid=g['g'].tolist(),V=len(g['vertices']),seconds=time.time()-start);trace.append(row)
            if us==1 and(qm<1e-10):preserve(X,d/f'exact_nomination_{calls:06d}','variable three-Conway-pyramid physical union; numericalU1 and stable-bar nomination; strict exact maximal-facet census required')
            if us==1 and(best is None or qm<best[0]):best=(qm,q.copy(),X.copy(),row);np.save(d/'best_U1_points.npy',X);np.save(d/'best_U1_parameters.npy',q);(d/'best_U1.json').write_text(json.dumps(row,indent=2))
            if calls%100==0:np.save(d/'latest_parameters.npy',q);(d/'trace.json').write_text(json.dumps(trace,indent=2));print('VARIABLE_CONWAY_UNION',d,row,flush=True)
            cache.update(q=q.copy(),objective=qm,constraints=constraints);return qm,constraints
        sol=minimize(lambda z:evaluate(z)[0],q,method='SLSQP',bounds=bounds,constraints=[dict(type='ineq',fun=lambda z:evaluate(z)[1])],options=dict(maxiter=steps,ftol=1e-12,eps=1e-6,disp=False));X,gy=construct(sol.x,n);np.save(d/'endpoint_parameters.npy',sol.x);np.save(d/'endpoint_points.npy',X);row=dict(seed=seed,success=bool(sol.success),message=sol.message,objective=float(sol.fun),iterations=int(sol.nit),evaluations=calls,seconds=time.time()-start,best_actual_U1=best[3]if best else None);allrows.append(row);(d/'trace.json').write_text(json.dumps(trace,indent=2));(out/'results.json').write_text(json.dumps(allrows,indent=2));print('VARIABLE_CONWAY_UNION_FINITE_CASE',row,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('out');p.add_argument('--seeds',type=int,default=12);p.add_argument('--steps',type=int,default=450);a=p.parse_args();run(a.out,a.seeds,a.steps)
