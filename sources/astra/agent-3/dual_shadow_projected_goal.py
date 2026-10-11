"""Transfer a physical U1 point body into a bounded S1 support family.

Candidate inequalities come from the actual own-centroid physical facets.
Greedy deletion defines new circumscribed bodies until<=84 remain. Then a
positive-shadow radial construction defines new normals and the actual filled
intersection's centroid is restored. No formal polar mass is used.
"""
import argparse,json,time,hashlib
from pathlib import Path
import numpy as np
from vertex_geometry import geometry as vertex_geometry
from support_geometry import geometry,census
from dual_shadow_goal import run as goal

def run(source,out,steps):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);g=vertex_geometry(X,False);Q,inv=np.unique(g['H'],axis=0,return_inverse=True);root=int(np.argmax(np.linalg.norm(g['Z'],axis=1)));locked=set(map(int,inv[np.any(g['T']==root,axis=1)]));locked.add(int(np.argmax(np.linalg.norm(Q,axis=1))));ids=list(range(len(Q)));trace=[];start=time.time()
    (out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest(),initial_supports=len(Q),literal_identical_vectors_only_deduplicated=True,locked_supports=sorted(locked),scope='every deletion and radial adjustment defines a new physical body; no approximate facet merging or census relabelling'),indent=2));np.save(out/'initial_supports.npy',Q)
    while len(ids)>84:
        options=[]
        for i in ids:
            if i in locked:continue
            ss=[j for j in ids if j!=i]
            try:gg=geometry(Q[ss],False)
            except(ValueError,np.linalg.LinAlgError):continue
            options.append((float(gg['V']),i,gg))
        if not options:raise ValueError('no bounded physical support deletion available')
        volume,i,gg=min(options,key=lambda r:r[0]);ids.remove(i);cl=census(gg);row=dict(remaining=len(ids),removed=i,volume=volume,seconds=time.time()-start,**cl);trace.append(row)
        if len(ids)%10==0:print('DIRECT_NORMAL_BOUND',row,flush=True)
    np.save(out/'bounded_supports.npy',Q[ids]);(out/'deletions.json').write_text(json.dumps(trace,indent=2));(out/'retained_ids.json').write_text(json.dumps(ids))
    for k in range(4):goal(out/'bounded_supports.npy',out/f'goal{k:02d}',steps,None if k==0 else 865390+k,True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=1400);a=p.parse_args();run(a.source,a.out,a.steps)
