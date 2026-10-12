"""Direct Figure scout: radial powers followed by true projective mass closure."""
import json,argparse,time
from pathlib import Path
import numpy as np
from canonical_projective_mass import normalize
from unrestricted_shadow_goal import census
from vertex_geometry import geometry
from shadow_mass_retracted_goal import bars
from dual_shadow_goal import bars as primal_bars
from goal_nomination import preserve

def screen(X):
    g,p,h=normalize(X);cl=census(g);Q=bars(g,False)[0];owners=set()
    for tri in g['T']:
        for i,j in zip(tri,np.roll(tri,-1)):owners.add(tuple(sorted((int(i),int(j)))))
    g['edges']=np.array(list(owners));P=primal_bars(g,False)[0];return g,p,h,dict(Pmax=float(max(P,default=0.)),Qmax=float(max(Q,default=0.)),**cl)

def run(sources,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);rows=[];start=time.time();serial=0;best=[]
    powers=np.unique(np.r_[np.linspace(.1,1,61),np.linspace(1,3,201),np.geomspace(3,20,121)])
    for source in sources:
        X=np.load(source);assert len(X)<=84;r=np.linalg.norm(X,axis=1);r/=max(r)
        for power in powers:
            serial+=1;Y=X*r[:,None]**(power-1)
            try:g,p,h,cl=screen(Y)
            except(ValueError,np.linalg.LinAlgError)as err:rows.append(dict(source=source,power=float(power),error=str(err)));continue
            row=dict(source=source,power=float(power),serial=serial,projective_parameter=p.tolist(),normalization_iterations=len(h),**cl);rows.append(row)
            if cl['S']==cl['U']==1:preserve(g['X'],out/f'exact_goal_{serial:06d}','radial power then literal physical projective centroid normalization; <=84 vertices; actual numerical110')
            score=cl['Pmax']+cl['Qmax'];best.append((score,serial,g['X'],row));best.sort(key=lambda z:z[0]);best=best[:12]
            if serial%30==0:(out/'screen.json').write_text(json.dumps(rows,indent=2));print('RADIAL_PROJECTIVE_GOAL',serial,row,'seconds',time.time()-start,flush=True)
    (out/'screen.json').write_text(json.dumps(rows,indent=2))
    total_trials=serial
    for k,(score,serial,X,row)in enumerate(best):
        np.save(out/f'best{k:02d}.npy',X);(out/f'best{k:02d}.json').write_text(json.dumps(row,indent=2))
    print('RADIAL_PROJECTIVE_FINITE_STOP',total_trials,[r[3]for r in best[:3]],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('out');p.add_argument('sources',nargs='+');a=p.parse_args();run(a.sources,a.out)
