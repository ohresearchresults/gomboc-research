"""Physical multi-facet caps in the union of ALL old-vertex escape balls.

The reference U1 lemma is only a proposal constraint. Every nominated body has
its own uniform mass integrated. Reference S1 alone is explicitly not success.
Numerical hull incidence is inherited from an exact convex parent and a strict
visible-facet/horizon decomposition; final acceptance is a separate exact audit.
"""
import sys,json,time,hashlib
from pathlib import Path
from collections import defaultdict
import numpy as np
from gmpy2 import mpq
from selected_projective import load
from geometry import mass,angular_scores
from support_persistence import ROOT,barcode

class Cap:
    def __init__(self,src):
        self.src=Path(src)
        X,Y,tri,eu,es,r=load(self.src)
        self.c=np.array([float(mpq(x)) for x in r['raw_centroid']])
        self.X=X-self.c;self.Y=Y/(1-Y@self.c)[:,None]
        self.r=r;self.faces=r['faces'];self.eu=eu;self.es=es
        self.u=int(np.argmax(np.sum(self.X**2,1)))
        self.sr=int(np.argmax(np.sum(self.Y**2,1)))
        targets=[int(f) for f in r['stable_face_ids'] if f!=self.sr]
        assert len(targets)==1 and r['counts']==[2,1,1]
        self.target=targets[0]
        self.n=self.Y[self.target]/np.linalg.norm(self.Y[self.target])
        self.h=1/np.linalg.norm(self.Y[self.target])
        e=np.eye(3)[np.argmin(abs(self.n))]
        self.a=np.cross(self.n,e);self.a/=np.linalg.norm(self.a)
        self.b=np.cross(self.n,self.a)
        self.top=(self.X@self.n+np.linalg.norm(self.X,axis=1))/2
        self.witnesses=np.flatnonzero(self.top>self.h+1e-10)

    def body(self,p,maxedges=248):
        X,Y=self.X,self.Y
        gap=1-Y@p
        if np.min(abs(gap))<1e-12:return None
        visible=gap<0
        if not visible[self.target]:return None
        horizon=self.eu[visible[self.es[:,0]]!=visible[self.es[:,1]]]
        ff=[list(f) for i,f in enumerate(self.faces) if not visible[i]]
        newp=len(X);P=np.vstack([X,p]);N=[y for i,y in enumerate(Y) if not visible[i]]
        for i,j in horizon:
            norm=np.cross(X[j]-X[i],p-X[i]);h=norm@X[i]
            if h<0:i,j=j,i;norm=-norm;h=-h
            if h<=0:return None
            ff.append([int(i),int(j),newp]);N.append(norm/h)
        ids=np.array(sorted({v for f in ff for v in f}));V=len(ids);F=len(ff);E=V+F-2
        if E>maxedges:return None
        N=np.array(N);tri=np.array([[f[0],f[k],f[k+1]] for f in ff for k in range(1,len(f)-1)])
        vol,g=mass(P,tri)
        if vol<=0 or min(1-N@g)<=0:raise ValueError('invalid mass')
        if (N@P.T-1).max()>1e-7:raise ValueError('horizon containment fails')
        adj=defaultdict(list)
        for f,vs in enumerate(ff):
            for i,j in zip(vs,vs[1:]+vs[:1]):adj[tuple(sorted((i,j)))].append(f)
        if len(adj)!=E or not all(len(fs)==2 for fs in adj.values()):raise ValueError('horizon incidence fails')
        return dict(P=P,N=N,faces=ff,ids=ids,tri=tri,vol=vol,g=g,V=V,E=E,F=F,adj=adj,visible=np.flatnonzero(visible).tolist())

def maxima(A):
    G=A@A.T-np.sum(A*A,axis=1)[:,None]
    np.fill_diagonal(G,-np.inf)
    return G.max(1)

def run(src,out,samples=30000,seed=9319):
    src=Path(src);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    cap=Cap(src);X,Y,n=cap.X,cap.Y,cap.n;rng=np.random.default_rng(seed)
    meta=dict(source=str(src),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),samples=samples,seed=seed,target=cap.target,witnesses=cap.witnesses.tolist(),point_frame='source exact own centroid subtracted',scope='reference110 is not own110; all counts here numerical')
    (out/'source.json').write_text(json.dumps(meta,indent=2)+'\n')
    rows=[];bestref=(999,np.inf);bestown=(999,np.inf);start=time.time()
    for k in range(samples):
        w=int(rng.choice(cap.witnesses));center=X[w]/2;R=np.linalg.norm(center);d=cap.h-n@center
        fraction=10**rng.uniform(-7,-.0001) if k%3==0 else rng.uniform(.00001,.99999)
        z=d+(R-d)*fraction;rho=np.sqrt(max(R*R-z*z,0))*np.sqrt(rng.uniform(0,.999999));theta=rng.uniform(0,2*np.pi)
        p=center+n*z+rho*(np.cos(theta)*cap.a+np.sin(theta)*cap.b)
        body=cap.body(p)
        if body is None:continue
        g=body['g'];P=body['P'][body['ids']];N=body['N'];Z=P-g;M=N/(1-N@g)[:,None]
        S=int((maxima(M)<0).sum());U=int((maxima(Z)<0).sum());rS=int((maxima(N)<0).sum());rU=int((maxima(P)<0).sum())
        if rU!=1:raise ValueError('reference U1 lemma disagrees with numeric census')
        row=dict(sample=k,point=p.tolist(),old_witness=w,old_witness_chord=float(p@(X[w]-p)),visible=body['visible'],V=body['V'],E=body['E'],F=body['F'],S=S,U=U,reference_S=rS,reference_U=rU,centroid=g.tolist(),centroid_distance=float(np.linalg.norm(g)),volume=float(body['vol']))
        if S+U<=5 or rS<=2:
            qp,qw,bars=barcode(M,np.ones(len(M)),np.array(list(body['adj'].values())));bars/=np.sum(M[qp[:,0]]**2,1)
            row['Qmax']=float(bars.max())
        keyref=(rS,row['centroid_distance']);keyown=(S+U,row.get('Qmax',np.inf))
        if keyref<bestref:
            bestref=keyref;(out/'best_reference.json').write_text(json.dumps(row,indent=2)+'\n');print('FLOWER_REFERENCE_BEST',row,flush=True)
        if keyown<bestown:
            bestown=keyown;(out/'best_own.json').write_text(json.dumps(row,indent=2)+'\n');print('FLOWER_OWN_BEST',row,flush=True)
        if rS==1:
            row['reference_margin']=float(np.sort(angular_scores(N).max(1))[1]);(out/f'REFERENCE110_NOT_GOAL_{k}.json').write_text(json.dumps(row,indent=2)+'\n')
        if S==U==1:
            row['own_margin']=float(min(np.sort(angular_scores(M).max(1))[1],np.sort(angular_scores(Z).max(1))[1]));(out/f'NUMERICAL_NOMINATION_{k}.json').write_text(json.dumps(row,indent=2)+'\n');print('NUMERICAL_REQUIRES_EXACT',row,flush=True)
        rows.append(row)
        if k%1000==0:(out/'screen.json').write_text(json.dumps(dict(source=meta,rows=rows,seconds=time.time()-start),indent=2)+'\n')
    rows.sort(key=lambda r:(r['reference_S'],r['centroid_distance']));(out/'screen.json').write_text(json.dumps(dict(source=meta,rows=rows,seconds=time.time()-start),indent=2)+'\n');print('FLOWER_SCREEN_DONE',len(rows),bestref,bestown,time.time()-start,flush=True)

if __name__=='__main__':run(ROOT/sys.argv[1],ROOT/sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 30000)
