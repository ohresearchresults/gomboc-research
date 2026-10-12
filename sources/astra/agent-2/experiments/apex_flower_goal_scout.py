"""Actual cap hulls across multiple apex facets, targeted at the last S root.
The added point lies strictly in the old unique apex's diameter ball. Whole
visible facets are replaced by the true horizon triangles; old polygon
facets stay polygons. Each body's uniform centroid and complete vertex/face
escape census are recomputed. Only a numerical110 is sent to exact freezing.
"""
import sys,json,time,hashlib
from pathlib import Path
from collections import defaultdict
import numpy as np
from scipy.spatial import QhullError
from apex_polygon_supports import ApexFamily
from geometry import mass,angular_scores
from support_persistence import ROOT

def run(src,out,m=44,trials=20000,seed=530712):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);q=np.load(src);s=ApexFamily(m,allow_top_retirement=True,edge_limit=249).state(q);X,H=s['X'],s['H'][s['A']];faces=s['faces'];U=X[0]
    if list(np.flatnonzero(s['uguards']<0))!=[0]:raise ValueError('actual source unique U must be the apex')
    stable=np.flatnonzero(s['sguards']<0);carrier=[i for i in stable if 0 in faces[i]]
    if len(carrier)!=1:raise ValueError('one extra stable apex carrier is required')
    carrier=carrier[0];normal=H[carrier];foot=normal/(normal@normal);adj=defaultdict(list)
    for i,f in enumerate(faces):
        for a,b in zip(f,f[1:]+f[:1]):adj[tuple(sorted((a,b)))].append(i)
    edges=np.array(list(adj),int);owners=np.array(list(adj.values()),int)
    if owners.shape[1]!=2:raise ValueError('source edge manifold fails')
    rng=np.random.default_rng(seed);rows=[];best=None;bestref=999;start=time.time();points=[]
    source=dict(path=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),apex_candidates=m,carrier=int(carrier),raw_owner=int(s['A'][carrier]),seed=seed,method=__doc__);(out/'source.json').write_text(json.dumps(source,indent=2)+'\n');np.save(out/'source_q.npy',q);np.save(out/'source_H.npy',s['H']);np.save(out/'source_R.npy',s['R'])
    def evaluate(p,index):
        side=H@p-1;visible=side>0
        if not visible[carrier] or np.min(abs(side))<1e-12:return None
        reference_escape=float(p@(U-p))
        if reference_escape<=1e-12:return None
        horizon=edges[visible[owners[:,0]]!=visible[owners[:,1]]];kept=np.flatnonzero(~visible);oldfaces=[faces[i] for i in kept];used=sorted(set(v for f in oldfaces for v in f));V=len(used)+1;F=len(kept)+len(horizon);E=V+F-2
        if not 17<=E<=249:return None
        mapping={a:i for i,a in enumerate(used)};P=np.r_[X[used],[p]];newfaces=[[mapping[v] for v in f] for f in oldfaces];newnormals=[]
        for a,b in horizon:
            f=[mapping[int(a)],mapping[int(b)],V-1];n=np.linalg.solve(P[f],np.ones(3))
            if np.cross(P[f[1]]-P[f[0]],P[f[2]]-P[f[0]])@n<0:f=f[::-1]
            newfaces.append(f);newnormals.append(n)
        normals=np.r_[H[kept],newnormals];T=np.array([[f[0],f[j],f[j+1]] for f in newfaces for j in range(1,len(f)-1)],int);vol,g=mass(P,T)
        if vol<=0 or np.min(1-normals@g)<=0:raise ValueError('invalid actual cap mass')
        Z=P-g;Y=normals/(1-normals@g)[:,None];ug=angular_scores(Z).max(1);sg=angular_scores(Y).max(1);refS=int((angular_scores(normals).max(1)<0).sum());S=int((sg<0).sum());UU=int((ug<0).sum());floor=float(min(np.sort(ug)[1],np.sort(sg)[1]));loss=float(np.maximum(1e-7-np.delete(ug,np.argmin(ug)),0).sum()+np.maximum(1e-7-np.delete(sg,np.argmin(sg)),0).sum())
        row=dict(index=index,V=V,E=E,F=F,S=S,U=UU,referenceS=refS,reference_newpoint_escape=reference_escape,visible_count=int(visible.sum()),horizon_count=len(horizon),loss=loss,floor=floor,centroid=g.tolist(),volume=float(vol),point=p.tolist())
        return row,P,normals,newfaces
    for k in range(trials):
        t=rng.uniform(.001,.995);base=(1-t)*foot+t*U
        # A tangential displacement explores the whole carrier and its fan.
        if k%3:
            tangent=X[faces[carrier][1]]-X[faces[carrier][0]];tangent-=normal*(tangent@normal)/(normal@normal);tangent/=np.linalg.norm(tangent);base+=rng.normal()*min(t,1-t)*.5*tangent
        d=foot;A=d@d;B=2*base@d-U@d;C=base@base-U@base;disc=B*B-4*A*C
        if C>=0 or disc<=0:continue
        limit=(-B+np.sqrt(disc))/(2*A);fraction=10.**rng.uniform(-6,0) if k%2 else rng.uniform(.001,.999);p=base+limit*fraction*d;points.append(p)
        try:r=evaluate(p,k)
        except (ValueError,np.linalg.LinAlgError):continue
        if r is None:continue
        row,P,N,ff=r;rows.append(row);key=(row['S']+row['U'],row['loss'])
        if best is None or key<best[0]:
            best=(key,row);np.save(out/'best_point.npy',p);np.save(out/'best_H.npy',N);(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('FLOWER_GOAL_SCOUT',row,flush=True)
        if row['referenceS']<bestref:bestref=row['referenceS'];(out/'best_reference.json').write_text(json.dumps(row,indent=2)+'\n')
        if row['S']==row['U']==1:
            np.save(out/'NUMERICAL_NOMINATION_point.npy',p);np.save(out/'NUMERICAL_NOMINATION_H.npy',N);(out/'NUMERICAL_NOMINATION.json').write_text(json.dumps(row,indent=2)+'\n');print('NUMERICAL_110_REQUIRES_EXACT_CAP_CONSTRUCTION',row,flush=True);break
    np.save(out/'all_points.npy',np.asarray(points));(out/'screen.json').write_text(json.dumps(dict(rows=rows,trials=trials,seconds=time.time()-start,goal_complete=False),indent=2)+'\n');return None if best is None else best[1]

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 44,int(sys.argv[4]) if len(sys.argv)>4 else 20000)
