"""Physical second-vertex coalescence and explicit support selection.
Selected polar points are moved onto one new exposed plane; all actual mass,
incidence and equilibria are recalculated. No source census is inherited.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from scipy.spatial import QhullError
from selected_projective import load
from two_apex_supports import TwoApexFamily

def run(src,out):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=src.read_bytes();(out/'source_exact.json').write_bytes(raw)
    X,H,T,eu,es,r=load(src);g=np.array([float(mpq(x)) for x in r['raw_centroid']]);X-=g;H/=(1-H@g)[:,None];root=r['unstable_vertices'][0]
    ez=X[root]/np.linalg.norm(X[root]);e=np.eye(3)[np.argmin(abs(ez))];ex=e-ez*(e@ez);ex/=np.linalg.norm(ex);ey=np.cross(ez,ex);rot=np.column_stack([ex,ey,ez]);radius=np.linalg.norm(X[root]);H=H@rot*radius;X=X@rot/radius
    star=[i for i,f in enumerate(r['faces']) if root in f];other=[i for i in range(len(H)) if i not in star];m=len(star);H[star,2]=1
    escape=X@X[root]-np.sum(X*X,1);pool=np.flatnonzero((np.arange(len(X))!=root)&(abs(X[:,2])>.08));chosen=[]
    if len(pool):chosen=[int(pool[np.argmax(escape[pool])])]
    while len(chosen)<min(30,len(pool)):
        unseen=[int(i) for i in pool if int(i) not in chosen];chosen.append(max(unseen,key=lambda i:np.min(np.linalg.norm(X[chosen]-X[i],axis=1))))
    area=[]
    for f in r['faces']:
        P=X[f];area.append(np.linalg.norm(np.sum(np.cross(P,np.roll(P,-1,axis=0)),axis=0))/2)
    dirs=H/np.linalg.norm(H,axis=1)[:,None];rng=np.random.default_rng(706532);rows=[];best=None;start=time.time()
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(raw).hexdigest(),root=root,first_star=star,canonical_rotation=rot.tolist(),radius=float(radius),second_vertex_pool=chosen,method=__doc__),indent=2)+'\n')
    for n in [12,20,32,44,60]:
        fam=TwoApexFamily(m,n);N=min(fam.maxF,len(H));extra=N-m-n
        if extra<0:continue
        for vi in chosen:
            for inward in [.0001,.01,.08]:
                v=(1-inward)*X[vi];dots=H@v;available=[i for i in other if dots[i]>.05 and H[i,2]/dots[i]<1-1e-8]
                if len(available)<n:continue
                second=sorted(available,key=lambda i:-dots[i])[:n];left=[i for i in other if i not in second]
                selections=[sorted(left,key=lambda i:-area[i])[:extra]]
                cover=star+second
                for _ in range(extra):
                    unseen=[i for i in left if i not in cover];cover.append(max(unseen,key=lambda i:np.min(np.linalg.norm(dirs[cover]-dirs[i],axis=1))))
                selections.append(cover[len(star)+len(second):])
                for mode,rest in enumerate(selections):
                    HH=np.r_[H[star],H[second]/dots[second,None],H[rest]];HH[m+n:]+=rng.normal(size=HH[m+n:].shape)*1e-7
                    label=f'n{n}_v{vi:03d}_in{inward:g}_select{mode}';q=fam.pack(HH,v)
                    try:s=fam.state(q)
                    except (ValueError,QhullError,np.linalg.LinAlgError,AssertionError) as e:rows.append(dict(label=label,error=repr(e)));continue
                    row={k:s[k] for k in ['V','E','F','S','U','Pmax','Qmax','minimum_noncontact']};row.update(label=label,m=m,n=n,original_second_vertex=vi,inward=inward,selector=mode,actual_second_degree=sum(1 in f for f in s['faces']),apex_degree=sum(0 in f for f in s['faces']));rows.append(row)
                    key=(s['S']+s['U'],max(s['Pmax'],s['Qmax']))
                    if best is None or key<best[0]:
                        best=key,row;np.save(out/'fewest_q.npy',q);(out/'fewest.json').write_text(json.dumps(row,indent=2)+'\n');print('TWO_GENUINE_APEX_SEED',row,flush=True)
                    np.save(out/(label+'_q.npy'),q)
                    if s['S']==s['U']==1:
                        np.save(out/'NUMERICAL_NOMINATION_q.npy',q);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');return
                (out/'screen.json').write_text(json.dumps(dict(rows=rows,seconds=time.time()-start,goal_complete=False),indent=2)+'\n')
    return None if best is None else best[1]

if __name__=='__main__':run(sys.argv[1],sys.argv[2])
