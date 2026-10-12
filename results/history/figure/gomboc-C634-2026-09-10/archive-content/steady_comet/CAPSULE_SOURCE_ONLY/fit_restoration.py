"""C650-coordinate-driven restoration and simultaneous incidence fitting.
This is physical shape fitting, not minimum-edge optimization.
"""
from pathlib import Path
from fractions import Fraction as F
import json,itertools,time,sys
import numpy as np
from scipy.optimize import least_squares
from scipy.sparse import coo_matrix
from numeric import topology,mechanics
from contact_chart import make_chart

def embedded_faces(edges,rotation):
    E=set(edges);rot={i:[j for j in rotation[i] if tuple(sorted((i,j))) in E] for i in rotation}
    seen=set();faces=[];dface={}
    for u,v in sorted((u,v) for a,b in edges for u,v in ((a,b),(b,a))):
        if (u,v) in seen:continue
        a,b=u,v;cy=[];fid=len(faces)
        while (a,b) not in seen:
            seen.add((a,b));dface[a,b]=fid;cy.append(a);r=rot[b];a,b=b,r[(r.index(a)-1)%len(r)]
        faces.append(cy)
    return faces,rot,dface

def build(target=249):
    R=Path(__file__).parent; A=json.loads((R/'parent650/C650/A.json').read_text());raw=json.loads((R/'parent650/C650/RAW.json').read_text())
    q=np.array([[x/h[3] for x in h[:3]] for h in raw['H']]);P=np.array([[float(F(v)) for v in p] for p in A['raw_vertices']]);owners,ef=topology(A['faces'])
    polar_to_primal={tuple(sorted(v)):k for k,v in ef.items()}
    rotation={int(k):v for k,v in json.loads((R/'C650_rotation.json').read_text()).items()}
    H=set(tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines());G=set(polar_to_primal)
    selected=H|{e for e in G if 3 in e}
    def cost(S):
        fs,_,_=embedded_faces(sorted(S),rotation);out=0.
        for cy in fs:
            if len(cy)<=3:continue
            p=np.linalg.lstsq(q[cy],np.ones(len(cy)),rcond=None)[0]
            out+=np.sum((q[cy]@p-1)**2)/(p@p)
        return out
    print('START_RESTORATION',len(selected),cost(selected),flush=True)
    for ne in range(len(selected),target):
        score,e=min((cost(selected|{e}),e) for e in sorted(G-selected))
        selected.add(e);print('RESTORE',len(selected),e,'cost',score,flush=True)
    fs,rot,df=embedded_faces(sorted(selected),rotation)
    # Components of the actual primal contraction forest determine physical initial points.
    par=list(range(len(P)))
    def find(a):
        while par[a]!=a:par[a]=par[par[a]];a=par[a]
        return a
    for e in G-selected:
        a,b=polar_to_primal[e];par[find(a)]=find(b)
    comps={}
    for i in range(len(P)):comps.setdefault(find(i),[]).append(i)
    keyed={tuple(sorted(set().union(*(set(owners[i]) for i in cc)))):cc for cc in comps.values()}
    assert len(keyed)==len(fs)
    PP=np.array([P[keyed[tuple(sorted(cy))]].mean(0) for cy in fs])
    primal=[]
    for i in range(137):
        cy=[df[i,j] for j in rot[i]]
        if np.dot(np.cross(PP[cy[1]]-PP[cy[0]],PP[cy[2]]-PP[cy[0]]),q[i])<0:cy=cy[::-1]
        primal.append(cy)
    root=next(i for i,cy in enumerate(fs) if set(cy)==set(owners[101]))
    data=dict(edges=sorted(selected),added_edges=sorted(selected-H),polar_faces=fs,primal_faces=primal,root=root,initial_q=q.tolist(),initial_p=PP.tolist())
    (R/f'H{target}_RESTORATION.json').write_text(json.dumps(data,separators=(',',':')))
    return data

def fit(data,outname):
    R=Path(__file__).parent;n=len(data['initial_q']);m=len(data['initial_p']);N=n+m
    q0=np.array(data['initial_q']);p0=np.array(data['initial_p']);X0=np.vstack([q0,p0]);root=n+data['root'];X0[root]=[0,0,1]
    refs=np.array([[i,n+f] for f,cy in enumerate(data['polar_faces']) for i in cy],int)
    incid=np.zeros((n,m),bool)
    for i,j in refs:incid[i,j-n]=True
    ni,nj=np.where(~incid);off=np.column_stack([ni,n+nj]);nr=len(refs);no=len(off)
    # Variable scale: dual coordinates have reciprocal units, row normalization improves LSMR.
    scale=np.maximum(np.linalg.norm(X0,axis=1),0.1)[:,None]*np.ones((1,3))
    free=np.ones((N,3),bool);free[root]=False;fi=np.flatnonzero(free.ravel());back=np.full(3*N,-1);back[fi]=np.arange(len(fi))
    y0=(X0/scale).ravel()[fi]
    anchor=X0.copy();reg=np.ones(N);reg[n:]=0.1
    # Deliberately protect the stable support and its actual neighboring supports in proximity.
    original_neighbors=set()
    for e in data['edges']:
        if 3 in e:original_neighbors.update(e)
    for i in original_neighbors:reg[i]=3
    weights=np.repeat(reg,3)[fi]
    def decode(y):
        X=anchor.copy();X.ravel()[fi]=(y*scale.ravel()[fi]);return X
    def residual(y,w):
        X=decode(y)
        z=np.einsum('ic,ic->i',X[refs[:,0]],X[refs[:,1]])-1
        h=np.maximum(np.einsum('ic,ic->i',X[off[:,0]],X[off[:,1]])-1+1e-5,0)
        return np.r_[w*z,w*h,weights*(y-y0)]
    def jac(y,w):
        X=decode(y);active=np.einsum('ic,ic->i',X[off[:,0]],X[off[:,1]])>1-1e-5
        rr=np.r_[np.arange(nr),nr+np.flatnonzero(active)];pairs=np.vstack([refs,off[active]])
        row=[];col=[];vals=[]
        for side in (0,1):
            ids=pairs[:,side];other=pairs[:,1-side]
            for k in range(3):
                jj=back[3*ids+k];ok=jj>=0
                row.extend(rr[ok]);col.extend(jj[ok]);vals.extend((w*X[other,k]*scale[ids,k])[ok])
        row.extend(nr+no+np.arange(len(fi)));col.extend(np.arange(len(fi)));vals.extend(weights)
        return coo_matrix((vals,(row,col)),shape=(nr+no+len(fi),len(fi))).tocsr()
    y=y0;start=time.time()
    for w in [10.,100.,1000.,10000.,100000.]:
        print('FIT_STAGE',w,'start',time.time()-start,flush=True)
        res=least_squares(residual,y,jac=jac,args=(w,),method='trf',tr_solver='lsmr',x_scale='jac',max_nfev=250,ftol=1e-10,xtol=1e-11,gtol=1e-10,verbose=0,tr_options={'atol':1e-9,'btol':1e-9,'maxiter':1500})
        y=res.x;X=decode(y);z=np.einsum('ic,ic->i',X[refs[:,0]],X[refs[:,1]])-1;g=1-X[:n]@X[n:].T
        print('FIT_END',w,'nfev',res.nfev,'cost',res.cost,'optimality',res.optimality,'incmax',abs(z).max(),'mingap',g[~incid].min(),'dq',np.linalg.norm(X[:n]-q0),flush=True)
        np.savez(R/(outname+f'_W{int(w)}.npz'),q=X[:n],p=X[n:],y=y,refq=q0,refp=p0)
    rootidx=data['root'];order=[rootidx]+[i for i in range(m) if i!=rootidx];pp=X[n:][order];pp[0]=[0,0,1]
    groups=[data['polar_faces'][i] for i in order]
    gen,depth=make_chart(X[:n],pp,groups,grid=10**12,prefer='points')
    (R/(outname+'_GENERATOR.json')).write_text(json.dumps(gen,sort_keys=True,separators=(',',':')))
    from numeric import recover
    qq=recover(gen)[:n];audit=mechanics(qq,data['primal_faces'],tol=1e-9)
    print('FITTED_CHART',max(depth.values()),audit,flush=True)
    (R/(outname+'_numeric.json')).write_text(json.dumps(audit,indent=2))

if __name__=='__main__':
    target=int(sys.argv[1]) if len(sys.argv)>1 else 249
    data=build(target);fit(data,f'H{target}_FIT')
