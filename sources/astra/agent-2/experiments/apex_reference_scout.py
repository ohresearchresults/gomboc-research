"""Reference-centre diagnostic for literal physical apex additions in a source-U diameter ball.
Use the exact parent's facet and edge incidence to construct the changed hull.
The old-centre ball is only a proposal distribution; every candidate's actual
uniform centroid and all angular exclusion scores are recomputed separately.
Maximal old facets are retained, new facets are horizon triangles; no mesh count.
"""
import sys,json,time,hashlib
from pathlib import Path
from collections import defaultdict
import numpy as np
from gmpy2 import mpq
from selected_projective import load
from geometry import mass,angular_scores
from support_persistence import ROOT,barcode

def run(src,out,samples=12000,seed=9294):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    X,Y,tri,eu,es,r=load(src);c=np.array([float(mpq(x)) for x in r['raw_centroid']]);X=X-c;Y=Y/(1-Y@c)[:,None]
    u=int(np.argmax(np.sum(X*X,1)));sr=int(np.argmax(np.sum(Y*Y,1)))
    targets=[int(f) for f in r['stable_face_ids'] if f!=sr];assert len(targets)==1
    target=targets[0];faces=r['faces'];rng=np.random.default_rng(seed);center=X[u]/2;R=np.linalg.norm(center);n=Y[target]/np.linalg.norm(Y[target]);d=(1-Y[target]@center)/np.linalg.norm(Y[target]);e=np.eye(3)[np.argmin(abs(n))];a=np.cross(n,e);a/=np.linalg.norm(a);b=np.cross(n,a)
    meta=dict(source=str(src),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),seed=seed,samples=samples,U=u,main_stable=sr,target_stable=target,target_degree=len(faces[target]),ball_plane_distance=d,ball_radius=R,minimum_plane_score=1.,point_frame='source exact own centroid subtracted',nomination_only=True)
    (out/'source.json').write_text(json.dumps(meta,indent=2)+'\n')
    if d>=R:
        (out/'NO_BALL_INTERSECTION.json').write_text(json.dumps(meta,indent=2)+'\n');return
    old_edge_faces={tuple(e):tuple(f) for e,f in zip(eu,es)};rows=[];best=(999,np.inf);start=time.time()
    for k in range(samples):
        fraction=10**rng.uniform(-8,0) if k%2==0 else rng.random()
        z=d+(R-d)*fraction;rho=np.sqrt(max(R*R-z*z,0))*np.sqrt(rng.uniform(0,.999));theta=rng.uniform(0,2*np.pi)
        p=center+n*z+rho*(np.cos(theta)*a+np.sin(theta)*b)
        gap=1-Y@p
        if np.min(abs(gap))<1e-12:continue
        visible=gap<0
        if not visible[target]:continue
        horizon=[edge for edge,ff in old_edge_faces.items() if visible[ff[0]]!=visible[ff[1]]]
        ff=[list(f) for i,f in enumerate(faces) if not visible[i]]
        newp=len(X);Q=np.vstack([X,p]);normals=[y for i,y in enumerate(Y) if not visible[i]]
        for i,j in horizon:
            norm=np.cross(X[j]-X[i],p-X[i]);h=norm@X[i]
            if h<0:i,j=j,i;norm=-norm;h=-h
            ff.append([int(i),int(j),newp]);normals.append(norm/h)
        ids=np.array(sorted({v for f in ff for v in f}));V=len(ids);F=len(ff);E=V+F-2
        if E>248:continue
        M=np.array(normals);tt=np.array([[f[0],f[i],f[i+1]] for f in ff for i in range(1,len(f)-1)]);vol,g=mass(Q,tt)
        if vol<=0 or min(1-M@g)<=0:raise ValueError('invalid mass in nominated hull')
        if (M@Q.T-1).max()>1e-7:raise ValueError('nominated cone hull fails physical containment')
        Z=Q-g;N=M/(1-M@g)[:,None];Us=angular_scores(Z[ids]);Ss=angular_scores(N);U=int((Us.max(1)<0).sum());S=int((Ss.max(1)<0).sum())
        adj=defaultdict(list)
        for f,vs in enumerate(ff):
            for i,j in zip(vs,vs[1:]+vs[:1]):adj[tuple(sorted((i,j)))].append(f)
        assert len(adj)==E and all(len(fs)==2 for fs in adj.values())
        qp,qw,bars=barcode(N,np.ones(F),np.array(list(adj.values())));bars/=np.sum(N[qp[:,0]]**2,axis=1)
        ref_scores=angular_scores(M).max(1);refS=int((ref_scores<0).sum())
        row=dict(reference_S=refS,reference_U_theorem=1,reference_nonroot_margin=float(np.sort(ref_scores)[1]),centroid_distance=float(np.linalg.norm(g)),sample=k,point=p.tolist(),visible=np.flatnonzero(visible).tolist(),V=V,E=E,F=F,S=S,U=U,Qmax=float(bars.max()),centroid=g.tolist(),source_U_chord=float(p@(X[u]-p)))
        rows.append(row);key=(refS,float(np.linalg.norm(g)))
        if key<best:
            best=key;(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('APEX_SCOUT',row,flush=True)
        if refS==1:
            (out/f'REFERENCE110_NOT_GOAL_{k}.json').write_text(json.dumps(row,indent=2)+'\n');print('REFERENCE110_OWN_MASS_REQUIRED',row,flush=True)
        if k%500==0:(out/'screen.json').write_text(json.dumps(dict(source=meta,rows=rows,seconds=time.time()-start),indent=2)+'\n')
    rows.sort(key=lambda r:(r['reference_S'],r['centroid_distance']));(out/'screen.json').write_text(json.dumps(dict(source=meta,rows=rows,seconds=time.time()-start),indent=2)+'\n');print('APEX_SCREEN_DONE',len(rows),time.time()-start,flush=True)

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 12000)
