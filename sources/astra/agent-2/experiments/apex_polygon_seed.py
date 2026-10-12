"""Declared support selections from an exact body, preserving its apex star.
Dropping a plane is a physical change, followed by actual uniform mass
integration. Generic releases are explicit new normal coordinates. No census
or centroid is inherited from the source, and no exact preservation is claimed.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull,HalfspaceIntersection,QhullError
from gmpy2 import mpq
from selected_projective import load
from apex_polygon_supports import ApexFamily
from support_persistence import ROOT

def mass(H):
    X=HalfspaceIntersection(np.c_[H,-np.ones(len(H))],np.zeros(3)).intersections;h=ConvexHull(X);T=h.simplices.copy();a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]]
    flip=np.sum(np.cross(b-a,c-a)*h.equations[:,:3],1)<0;T[flip]=T[flip][:,[0,2,1]];a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];six=np.sum(a*np.cross(b,c),1);return six.sum()/6,np.sum(six[:,None]*(a+b+c),0)/(4*six.sum())

def run(src,out):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);X,H,T,eu,es,r=load(src);g=np.array([float(mpq(v)) for v in r['raw_centroid']]);X-=g;H/= (1-H@g)[:,None]
    if len(r['unstable_vertices'])!=1:raise ValueError('exact source must have unique U')
    root=r['unstable_vertices'][0];star=[i for i,f in enumerate(r['faces']) if root in f];m=len(star);family=ApexFamily(m);needed=family.maxF-m;others=[i for i in range(len(H)) if i not in star]
    radius=np.linalg.norm(X[root]);ez=X[root]/radius;e=np.eye(3)[np.argmin(abs(ez))];ex=e-ez*(e@ez);ex/=np.linalg.norm(ex);ey=np.cross(ez,ex);rot=np.column_stack([ex,ey,ez]);H=H@rot*radius;X=X@rot/radius;H[star,2]=1.
    source=dict(path=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),star=star,m=m,maxF=family.maxF,radius=float(radius),centroid=g.tolist(),rotation=rot.tolist(),scope=__doc__)
    (out/'source.json').write_text(json.dumps(source,indent=2)+'\n');selections={}
    area=[]
    for f in r['faces']:
        P=X[f];area.append(np.linalg.norm(np.sum(np.cross(P,np.roll(P,-1,axis=0)),axis=0))/2)
    selections['large_areas']=sorted(others,key=lambda i:-area[i])[:needed]
    dirs=H/np.linalg.norm(H,axis=1)[:,None];chosen=star.copy()
    for _ in range(needed):
        unseen=[i for i in others if i not in chosen];chosen.append(max(unseen,key=lambda i:np.min(np.linalg.norm(dirs[chosen]-dirs[i],axis=1))))
    selections['normal_cover']=[i for i in chosen if i not in star]
    initialV,_=mass(H)
    for alpha in [0.,10.,100.]:
        keep=list(range(len(H)));hist=[]
        while len(keep)>family.maxF:
            best=None
            for i in keep:
                if i in star:continue
                trial=[j for j in keep if j!=i]
                try:v,c=mass(H[trial]);value=v/initialV+alpha*float(c@c)
                except (ValueError,QhullError,np.linalg.LinAlgError):continue
                if best is None or value<best[0]:best=(value,i,v,c)
            if best is None:raise ValueError('no bounded plane retirement')
            _,i,v,c=best;keep.remove(i);hist.append(dict(removed=i,F=len(keep),volume=float(v),centroid=c.tolist(),selection_objective=float(best[0])))
        name=f'greedy_mass_{alpha:g}';selections[name]=[i for i in keep if i not in star];(out/(name+'_retirements.json')).write_text(json.dumps(hist,indent=2)+'\n')
    rng=np.random.default_rng(78142);rows=[]
    for name,extra in selections.items():
        selected=star+extra;raw=H[selected];np.save(out/(name+'_unreleased_H.npy'),raw);(out/(name+'_indices.json')).write_text(json.dumps(selected)+'\n')
        for exp in [7,6,5,4]:
            for repeat in range(2):
                HH=raw.copy();HH[m:]+=rng.normal(size=HH[m:].shape)*10.**(-exp);q=family.pack(HH);label=f'{name}_e{exp}_r{repeat}';np.save(out/(label+'_q.npy'),q)
                try:
                    s=family.state(q);row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,apex=m,centroid=s['g'].tolist(),volume=s['volume']);np.save(out/(label+'_H.npy'),s['H']);print('APEX_POLYGON_SEED',row,flush=True)
                except (ValueError,QhullError,AssertionError,np.linalg.LinAlgError) as e:row=dict(label=label,error=repr(e))
                rows.append(row)
    (out/'screen.json').write_text(json.dumps(rows,indent=2)+'\n')
    return rows

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2])
