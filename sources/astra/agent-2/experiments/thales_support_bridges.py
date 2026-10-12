"""Explicit support-normal chains that cancel the extra reference stable root.

Each new polar point p_j escapes to its predecessor: p_j.(p_{j-1}-p_j)>0.
The last point gives the old junior root a positive escape. Original nonroots
retain old witnesses. This proves reference S1 on the exact inequalities only;
the actual homogeneous centroid and primal U are separately evaluated below.
"""
import sys,json,time,hashlib
from pathlib import Path
from collections import defaultdict
import numpy as np
from scipy.optimize import root
from flower_reference_caps import Cap
from geometry import hull_from_supports,mass,angular_scores
from support_persistence import ROOT,barcode

def score(Y):
    X,N,faces,tri,E,ids=hull_from_supports(Y,tol=1e-10);vol,g=mass(X,tri);Z=X-g;Q=N/(1-N@g)[:,None]
    adj=defaultdict(list)
    for k,f in enumerate(faces):
        for i,j in zip(f,f[1:]+f[:1]):adj[tuple(sorted((i,j)))].append(k)
    pp,pw,P=barcode(Z,np.ones(len(Z)),np.array(list(adj)));qp,qw,B=barcode(Q,np.ones(len(Q)),np.array(list(adj.values())));P/=np.sum(Z[pp[:,0]]**2,1);B/=np.sum(Q[qp[:,0]]**2,1)
    return dict(V=len(X),E=E,F=len(N),S=int((angular_scores(Q).max(1)<0).sum()),U=int((angular_scores(Z).max(1)<0).sum()),reference_S=int((angular_scores(N).max(1)<0).sum()),reference_U=int((angular_scores(X).max(1)<0).sum()),centroid=g.tolist(),volume=float(vol),Pmax=float(P.max()),Qmax=float(B.max()),loss=float(P@P+B@B)),(X,N,faces,tri,ids)

def run(src,out):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False);c=Cap(src);Y=c.Y;r=Y[c.target];R=np.linalg.norm(r);elder=c.sr
    arrows=Y@Y.T-(Y*Y).sum(1)[:,None];np.fill_diagonal(arrows,-np.inf);reach={elder}
    while True:
        nxt=reach|set(map(int,np.flatnonzero((arrows[:,list(reach)]>0).any(1))))
        if nxt==reach:break
        reach=nxt
    (out/'source.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),reference_center=c.c.tolist(),target=c.target,elder=elder,scope='reference S1 construction; own uniform mass separately evaluated; all current counts numerical'),indent=2)+'\n')
    rows=[];best=(999,np.inf);k=0;start=time.time()
    for u in sorted(reach):
        g=Y[u];G=np.linalg.norm(g)
        if G<=R*1.001:continue
        v=g/G;e=r/R;theta=np.arccos(np.clip(v@e,-1,1));w=e-v*(e@v);w/=np.linalg.norm(w)
        def chain(angle,m):
            delta=angle/(m+1);ratio=np.cos(delta)*(1-1e-5)
            if ratio<=0:return None
            new=np.array([G*ratio**j*(v*np.cos(j*delta)+w*np.sin(j*delta)) for j in range(1,m+1)])
            prev=np.r_[g[None],new[:-1]]
            if np.min(np.sum(new*(prev-new),1))<=0 or r@(new[-1]-r)<=0:return None
            return new
        options=[]
        for side,angle in [('short',theta),('long',theta-2*np.pi)]:
            feasible=[(m,chain(angle,m)) for m in range(3,51)]
            feasible=[(m,p) for m,p in feasible if p is not None]
            if not feasible:continue
            for ix in [0,1,2,4,7]:
                if ix<len(feasible):m,p=feasible[ix];options.append((side,m,p))
        pairs=[(label,m,new) for label,m,new in options]
        shorts=[x for x in options if x[0]=='short'];longs=[x for x in options if x[0]=='long']
        pairs += [('both', [a[1],b[1]],np.r_[a[2],b[2]]) for a in shorts[:3] for b in longs[:3]]
        for label,m,new in pairs:
            try:
                summary,mesh=score(np.r_[Y,new])
                assert summary['reference_S']==1,'reference chain failed its promised polar census'
                row=dict(sample=k,witness_start=u,paths=label,chain_lengths=m,new_normals=new.tolist(),**summary,seconds=time.time()-start)
                rows.append(row)
                if summary['E']<=248:
                    key=(summary['S']+summary['U'],summary['loss'])
                    if key<best:best=key;(out/'best.json').write_text(json.dumps(row,indent=2)+'\n');print('THALES_BRIDGE_BEST', {k:v for k,v in row.items() if k!='new_normals'},flush=True)
                    if summary['S']==summary['U']==1:(out/f'NUMERICAL_NOMINATION_{k}.json').write_text(json.dumps(row,indent=2)+'\n')
            except (ValueError,AssertionError,np.linalg.LinAlgError) as e:
                rows.append(dict(sample=k,witness_start=u,paths=label,chain_lengths=m,error=repr(e)))
            k+=1
    (out/'screen.json').write_text(json.dumps(dict(rows=rows,source=str(src),seconds=time.time()-start),indent=2)+'\n');print('THALES_BRIDGE_SCREEN_DONE',len(rows),best,flush=True)

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2])
