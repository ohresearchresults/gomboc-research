"""Return a true contact-event hull below budget before new Figure search."""
import argparse,json,time
from pathlib import Path
from literal_support_subset_goal import Source
from root_collar_expand_goal import save_proposal
from contact_physical_110 import realize
import numpy as np

def run(source,out,depth=3,width=3,steps=400):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);S=Source(source);ids=tuple(range(S.n));g=S.geometry(ids);beam=[(ids,g)];seen={ids};serial=0;hist=[];seeds=[];start=time.time()
    (out/'native_source_census.json').write_text(json.dumps({k:S.a[k]for k in ['V','E','F','counts','weak']},indent=2))
    for level in range(depth):
        pool=[]
        for ids,g in beam:
            for f in ids:
                ii=tuple(x for x in ids if x!=f)
                if ii in seen:continue
                seen.add(ii);serial+=1
                try:z=S.geometry(ii)
                except(ValueError,np.linalg.LinAlgError,ZeroDivisionError):continue
                row=dict(level=level,serial=serial,removed=f,retained=list(ii),**{k:z[k]for k in ['V','E','F','S','U','Pmax','Qmax','volume']})
                if z['E']<=248 and z['S']==z['U']==1:S.freeze(ii,out/f'exact_goal_{serial:06d}','literal exact support retirement after actual contact event; numeric own110')
                score=z['Pmax']+z['Qmax']+1e-6*(z['S']+z['U']);pool.append((score,ii,z,row))
        if not pool:break
        pool.sort(key=lambda p:p[0]);beam=[(i,g)for _,i,g,_ in pool[:width]];hist.append(dict(level=level,trials=serial,best=pool[0][3],seconds=time.time()-start));(out/'history.json').write_text(json.dumps(hist,indent=2));print('CONTACT_EVENT_BUDGET_RETIREMENT',hist[-1],flush=True)
        for k,(_,ii,z,row)in enumerate(pool[:width]):
            if z['E']>248:continue
            d=out/f'level{level:02d}_seed{k:02d}';c,gg=save_proposal(S,ii,z,d);(d/'screen.json').write_text(json.dumps(row,indent=2));seeds.append(d)
    for d in seeds:realize(d/'construction.json',d/'physical_110',steps,1e-8,angular_vertices=True)
    print('CONTACT_EVENT_BUDGET_FINITE_STOP',serial,len(seeds),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--depth',type=int,default=3);p.add_argument('--width',type=int,default=3);p.add_argument('--steps',type=int,default=400);a=p.parse_args();run(a.source,a.out,a.depth,a.width,a.steps)
