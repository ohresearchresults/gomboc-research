"""Direct physical clips with spare complexity and canonical mass centering.

The exact38-facet simple source has72vertices. A single new halfspace has at
most74vertices, so its literal floating point hull still has E<=216 even if
rounding breaks all original coplanar faces. Final success uses exact dyadic
coordinates, actual uniform mass, true facets and a complete weak audit.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution
from unstable_cap_clip import Clip
from support_geometry import escape
from canonical_projective_mass import normalize
from radial_power_projective_goal import screen
from goal_nomination import preserve

def run(source,out,trials=18000,iterations=350):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);C=Clip(source);assert C.a['F']<=38 and C.a['V']==2*C.a['F']-4;rng=np.random.default_rng(590302);calls=0;rows=[];refs=[];best=None;start=time.time();(out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),maximum_cut_facets=C.a['F']+1,maximum_literal_points=2*(C.a['F']+1)-4,physical_definition='literal float coordinates from a geometric half-space clip then a physical projective map solving uniform mass centroid; final dyadic point hull is the candidate, complete exact auditing required'),indent=2))
    log=(out/'trials.jsonl').open('w')
    def fun(t):
        nonlocal calls,best
        calls+=1;row=dict(call=calls,controls=np.asarray(t).tolist())
        try:
            c=C.body(t);assert 11<=len(c['X'])<=74;H0=c['H']/(1+c['H']@c['centroid'])[:,None];rs=int(sum(escape(H0)[0]<0));ru=int(sum(escape(c['X'])[0]<0));row['reference']=[rs,ru]
            g,p,hist,cl=screen(c['X']);value=cl['Pmax']+cl['Qmax'];row.update(projective_p=p.tolist(),**cl)
            if cl['U']==1 and(cl['S']==1 or cl['Qmax']<1e-10):preserve(g['X'],out/f'exact_goal_{calls:07d}','physical low-facet clip after canonical uniform mass normalization; <=74literal points; all strict and weak contacts require exact native audit')
            if best is None or value<best[0]:best=(value,t.copy(),g['X'].copy(),row);np.save(out/'best.npy',g['X']);np.save(out/'best_controls.npy',t);(out/'best.json').write_text(json.dumps(row,indent=2))
            if rs==ru==1:
                refs.append(row);np.save(out/f'reference110_{calls:07d}.npy',c['X']);(out/'reference110.json').write_text(json.dumps(refs,indent=2))
        except(ValueError,AssertionError,np.linalg.LinAlgError)as e:row.update(rejected=str(e),scope='invalid/failed finite physical proposal, never admitted');value=100.
        log.write(json.dumps(row)+'\n')
        if calls%1000==0:log.flush();print('LOW_FACET_PROJECTIVE_CLIP',calls,'best',best[3]if best else None,'reference110',len(refs),'seconds',time.time()-start,flush=True)
        return value
    for i in range(trials):
        scale=float(rng.choice([.08,.25,.7,2.,6.]));t=np.r_[rng.normal(0,scale,2),rng.uniform(.02,.999)];fun(t)
    bounds=[(-8.,8.),(-8.,8.),(.02,.99999)];pop=np.column_stack((rng.uniform(-3,3,(60,2)),rng.uniform(.05,.99,60)))
    if best is not None:pop[0]=np.clip(best[1],[-8,-8,.02],[8,8,.99999])
    de=differential_evolution(fun,bounds,init=pop,maxiter=iterations,polish=False,seed=914351,tol=1e-10,mutation=(.3,1.3),recombination=.85);log.close();(out/'termination.json').write_text(json.dumps(dict(calls=calls,message=de.message,seconds=time.time()-start,best=best[3]if best else None,reference110=len(refs)),indent=2));print('LOW_FACET_PROJECTIVE_CLIP_FINITE_STOP',calls,'best',best[3]if best else None,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--trials',type=int,default=18000);p.add_argument('--iterations',type=int,default=350);a=p.parse_args();run(a.source,a.out,a.trials,a.iterations)
