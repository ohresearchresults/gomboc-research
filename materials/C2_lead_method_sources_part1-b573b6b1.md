# material-b573b6b17421

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# C2 actual-mass finite search method — complete source part1

Complete numerical source units lead_c2.py and free_c2.py. This is a reusable finite search method, NOT an exact certificate and NOT a general exclusion. Part2 supplies the guarded/chart continuation, part3 exact numerical checkpoints/campaign settings. Exact geometric endpoints ROOTC71_G6 and CHART40_G8 have separate literal recovery capsules and do not depend on optimizer reproducibility. All source inputs, including the historical CH95_MASS_RECON71_G6 geometry, are literal below. Scientific historical parent is the complete immutable result figure-0508 SHA1496e2f4f33663ee3e62b53fbf258925e93cb8b632498a247eeec8598c3fd5e6; any successor scientifically derived from it should also select that literal parent.

Versions CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, float64, one OpenBLAS/OMP/MKL/Torch thread. The source hashes identify literal UTF-8/LF files with one final newline: lead_c2.py6367B SHA4d5c61021253015a0c04b07658da8f52b755fadd2ab5cf235a3ad2fe8f280e88; free_c2.py5835B SHAadfd5041d08e288a0acf1645d1a6f375ef64dc92f294bc3ec7b7a69e56c3f2eb. No other non-default settings are implicit. The maximal floating hull is regrouped using1e-9 plane tolerance; all accepted bodies require the separate exact integer hull/centroid/weak-state auditor. Do not infer exact class or weak000 from this floating census.

Save this first source as lead_c2.py:
```python
"""New lead numerical methods, CH95 G6 literal parent. Not an exact verifier.
CPython 3.13.5 / numpy 2.3.5 / scipy 1.17.0 / torch 2.10.0+cpu.
Fixed-incidence axial-projective/affine chart and free C2 vertex chart.
"""
import os
for _k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:
    os.environ[_k]='1'
import json, sys, hashlib, time
from pathlib import Path
import numpy as np
import scipy
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
import torch
torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
HALF_G6 = [[457549,-476424,4200],[455928,-469860,142701],[431226,-462724,253058],[414594,-463893,367648],[342861,-451364,453247],[275617,-453498,545481],[183681,-430269,611203],[73045,-412691,657589],[-41899,-373148,694522],[-166799,-352874,697732],[-290990,-325449,681518],[-406235,-348320,621819],[-514129,-298397,578415],[-606553,-271337,509729],[-684329,-236186,435162],[-745583,-199370,358049],[-792094,-167522,278140],[-824011,-120466,213821],[-845480,-77645,153092],[-857900,-32400,104215],[-864721,797,54958],[-866363,46447,19231],[-863907,92273,-6964],[-857982,140669,-25189],[-848740,190767,-38786],[-835913,242739,-49462],[-818986,296589,-59337],[-797253,352444,-69836],[-769751,410523,-81558],[-735330,470471,-96530],[-692399,533138,-113400],[-638137,599783,-125527],[-569013,670355,-133493],[-479812,745976,-130336],[-347680,832991,-133654]]
TAIL_G6 = [223168,-570002,405531]
SOURCE_ID='figure-0508'
SOURCE_SHA='1496e2f4f33663ee3e62b53fbf258925e93cb8b632498a247eeec8598c3fd5e6'
def literal():
    a=np.asarray(HALF_G6,dtype=float)/1e6
    s,b,c=np.asarray(TAIL_G6,dtype=float)/1e6
    return np.vstack([a,a*np.array([-1,1,-1]),[0,1,0],[[s,b,c],[-s,b,c],[-s,b,-c],[s,b,-c]]])
def topology(x):
    h=ConvexHull(x)
    tri=h.simplices.copy()
    p=x[tri]; n=np.cross(p[:,1]-p[:,0],p[:,2]-p[:,0])
    flip=np.einsum('ij,ij->i',n,h.equations[:,:3])<0
    tri[flip]=tri[flip][:,[0,2,1]]
    # One representative from each maximal face. The triangulation remains for volume.
    reps=[]
    for i,e in enumerate(h.equations):
        if not any(np.max(np.abs(e-h.equations[j]))<1e-9 for j in reps):reps.append(i)
    ft=tri[reps]
    base=np.flatnonzero(np.all(ft>=71,axis=1))
    assert len(base)==1
    edges=set()
    for i,j in enumerate(h.neighbors):
        for z in j:
            if z<i:continue
            if np.max(np.abs(h.equations[i]-h.equations[z]))<1e-9:continue
            edges.add(tuple(sorted(set(tri[i]).intersection(tri[z]))))
    return tri,ft,np.asarray(h.vertices),int(base[0]),np.asarray(sorted(edges))
def mechanics(x,tri,ft,verts):
    p=x[tri]
    v6=torch.einsum('ij,ij->i',p[:,0],torch.linalg.cross(p[:,1],p[:,2]))
    vol=v6.sum()/6
    c=(v6[:,None]*p.sum(dim=1)).sum(dim=0)/(4*v6.sum())
    xx=x-c
    f=xx[ft]
    n=torch.linalg.cross(f[:,1]-f[:,0],f[:,2]-f[:,0])
    hh=torch.einsum('ij,ij->i',n,f[:,0])
    q=n/hh[:,None]
    return xx[verts],q,c,vol

def best_cos(x):
    d=x[None,:,:]-x[:,None,:]
    den=torch.sqrt(torch.clamp((x*x).sum(1)[:,None]*(d*d).sum(2),min=1e-30))
    cos=(x[:,None,:]*d).sum(2)/den
    cos=cos-torch.eye(len(x))*1e4
    return cos.max(dim=1).values

def census(x):
    tri,ft,v,b,e=topology(np.asarray(x))
    p,q,c,vol=mechanics(torch.tensor(x),torch.tensor(tri),torch.tensor(ft),torch.tensor(v))
    bp=best_cos(p).numpy(); bq=best_cos(q).numpy()
    ui=np.flatnonzero(bp<=0); si=np.flatnonzero(bq<=0)
    return dict(V=len(v),E=len(e),F=len(ft),C=2*len(e),S=len(si),U=len(ui),S_rows=ft[si].tolist(),U_sources=v[ui].tolist(),centroid=c.numpy().tolist(),volume=float(vol),minPnonTop=float(np.delete(bp,np.flatnonzero(v==70)).min()),minQnonBase=float(np.delete(bq,b).min()),base_q_index=b,base_to_inradius=float(torch.linalg.vector_norm(q,dim=1).max()/torch.linalg.vector_norm(q[b])))

class Projective:
    def __init__(self):
        self.x0=torch.tensor(literal()); self.topo=topology(literal());tri,ft,v,b,e=self.topo
        self.tri=torch.tensor(tri);self.ft=torch.tensor(ft);self.v=torch.tensor(v);self.b=b
        self.pr=int(np.flatnonzero(v==70)[0]);self.calls=0
    def build(self,z):
        # denominator is positive over the bounded search chart.
        a,b,c,p=z
        xx=self.x0/(1+p*self.x0[:,1,None])
        return torch.stack([torch.exp(a)*xx[:,0]+b*xx[:,2],xx[:,1],torch.exp(c)*xx[:,2]],dim=1)
    def eval(self,z,wp=100.,target=1e-4,mode='cos'):
        z=torch.tensor(z,requires_grad=True);x=self.build(z)
        p,q,c,vol=mechanics(x,self.tri,self.ft,self.v)
        bp=best_cos(p);bq=best_cos(q)
        ap=torch.cat([bp[:self.pr],bp[self.pr+1:]])
        aq=torch.cat([bq[:self.b],bq[self.b+1:]])
        loss=wp*torch.relu(target-ap).square().sum()+torch.relu(target-aq).square().sum()
        loss=loss+1e-10*z.square().sum()
        loss.backward();self.calls+=1
        return float(loss.detach()),z.grad.numpy()

def projective_campaign(out,seed=230923,nstarts=20,maxiter=500):
    out=Path(out);out.mkdir(exist_ok=True,parents=True)
    rng=np.random.default_rng(seed);p=Projective();ledger=[]
    for j in range(nstarts):
        x0=np.zeros(4) if j==0 else np.array([rng.normal(0,.25),rng.normal(0,.15),rng.normal(0,.25),rng.uniform(-.65,1.2)])
        w=[100.,10.,1.,1000.][j%4]
        t=time.monotonic();before=p.calls
        r=minimize(lambda z:p.eval(z,wp=w),x0,jac=True,method='L-BFGS-B',bounds=[(-1.5,1.5),(-2,2),(-1.5,1.5),(-.8,1.6)],options={'maxiter':maxiter,'maxls':40,'ftol':1e-15,'gtol':1e-10})
        x=p.build(torch.tensor(r.x)).detach().numpy();stats=census(x)
        item=dict(j=j,weight=w,seed=seed,start=x0.tolist(),end=r.x.tolist(),end_hex=[float(t).hex() for t in r.x],loss=float(r.fun),nit=int(r.nit),nfev=int(r.nfev),success=bool(r.success),message=str(r.message),seconds=time.monotonic()-t,stats=stats)
        ledger.append(item);(out/'projective_ledger.json').write_text(json.dumps(ledger,sort_keys=True,indent=2)+'\n')
        print(j,w,r.fun,stats,flush=True)
        if stats['S']==1 and stats['U']==1:
            np.save(out/'candidate.npy',x);break
    return ledger

if __name__=='__main__':
    if sys.argv[1]=='census': print(json.dumps(census(literal()),indent=2))
    elif sys.argv[1]=='projective':projective_campaign(sys.argv[2],nstarts=int(sys.argv[3]) if len(sys.argv)>3 else 20,maxiter=int(sys.argv[4]) if len(sys.argv)>4 else 500)
```

Save this second source as free_c2.py:
```python
"""Free finite C2 geometry at its filled centroid: whole root-directed bottlenecks.
Numerical scout only. This is a new method, not a replay of CH95 flowA/B/C.
"""
import sys,json,time
from pathlib import Path
import numpy as np
import torch
from scipy.optimize import minimize
from scipy.spatial import ConvexHull,QhullError
from lead_c2 import literal,topology,mechanics,best_cos,census,Projective

def unpack(z):
    h=z[:105].reshape(35,3);a,b,c=z[105:]
    corners=torch.stack([torch.stack([a,b,c]),torch.stack([-a,b,c]),torch.stack([-a,b,-c]),torch.stack([a,b,-c])])
    return torch.cat([h,h*torch.tensor([-1.,1.,-1.]),torch.tensor([[0.,1.,0.]]),corners])
def pack(x):
    return np.concatenate([x[:35].ravel(),x[71]])
def bottleneck_edges(x,root):
    """Max-min directed paths to the specified root. Dense Dijkstra, no cycles.
    Scores need not be positive. Returns each nonroot's attaining bottleneck edge.
    """
    d=x[None,:,:]-x[:,None,:]
    s=(x[:,None,:]*d).sum(2)/torch.sqrt(torch.clamp((x*x).sum(1)[:,None]*(d*d).sum(2),min=1e-30))
    a=s.detach().numpy().copy();np.fill_diagonal(a,-np.inf)
    n=len(x);val=np.full(n,-np.inf);val[root]=np.inf
    ends=np.full((n,2),-1,dtype=int);done=np.zeros(n,bool)
    for _ in range(n):
        v=int(np.argmax(np.where(done,-np.inf,val)));done[v]=True
        cand=np.minimum(a[:,v],val[v]);take=(~done)&(cand>val)
        ids=np.flatnonzero(take);edgefirst=a[ids,v]<=val[v]
        ends[ids[edgefirst],0]=ids[edgefirst];ends[ids[edgefirst],1]=v
        ends[ids[~edgefirst]]=ends[v]
        val[ids]=cand[ids]
    ids=np.delete(np.arange(n),root);ee=ends[ids]
    assert np.all(ee>=0)
    return s[ee[:,0],ee[:,1]],ee

class Free:
    def __init__(self,start=None,wp=100.,wroot=0.,mode='root',target=1e-4):
        self.start=pack(literal()) if start is None else np.array(start)
        self.wp=wp;self.wroot=wroot;self.mode=mode;self.target=target
        self.calls=0;self.last=None
    def eval(self,z):
        z=torch.tensor(z,requires_grad=True);x=unpack(z)
        # Rebuild true floating hull on every actual geometry change.
        xx=x.detach().numpy()
        try:
            tri,ft,vs,base,e=topology(xx)
        except (QhullError,AssertionError,ValueError):
            # Stable base or unique top chart invalid. Positive finite penalty.
            dz=z-torch.tensor(self.start)
            loss=1e3+1e3*dz.square().sum();loss.backward()
            return float(loss.detach()),z.grad.numpy()
        if not np.any(vs==70):
            dz=z-torch.tensor(self.start);loss=1e3+1e3*dz.square().sum();loss.backward()
            return float(loss.detach()),z.grad.numpy()
        pr=int(np.flatnonzero(vs==70)[0]);p,q,c,vol=mechanics(x,torch.tensor(tri),torch.tensor(ft),torch.tensor(vs))
        bp=best_cos(p);ap=torch.cat([bp[:pr],bp[pr+1:]])
        qn=torch.linalg.vector_norm(q,dim=1);qratio=qn/qn[base]
        rr=torch.cat([qratio[:base],qratio[base+1:]])
        rootloss=torch.relu(rr-1+1e-4).square().sum()
        if self.mode=='root':qloss=rootloss
        elif self.mode=='cos':
            bq=best_cos(q);aq=torch.cat([bq[:base],bq[base+1:]])
            qloss=torch.relu(self.target-aq).square().sum()
        elif self.mode=='bottleneck':
            aq,ee=bottleneck_edges(q,base)
            qloss=torch.relu(self.target-aq).square().mean()
        else:raise ValueError(self.mode)
        h=z[:105].reshape(35,3);a,b,cc=z[105:]
        # Guard the finite architecture while permitting the side hull to change.
        geom=torch.relu(b+1e-4-h[:,1]).square().sum()+torch.relu(h[:,1]-1+1e-4).square().sum()+torch.relu(1e-3-a).square()+torch.relu(1e-3-cc).square()
        loss=self.wp*torch.relu(self.target-ap).square().sum()+qloss+self.wroot*rootloss+1e4*geom+1e-9*(z-torch.tensor(self.start)).square().sum()
        loss.backward();self.calls+=1
        self.last=dict(loss=float(loss.detach()),ploss=float(torch.relu(self.target-ap).square().sum().detach()),qloss=float(qloss.detach()),rootloss=float(rootloss.detach()),S=int((best_cos(q)<=0).sum()),U=int((bp<=0).sum()),base_ratio=float(qratio.max().detach()))
        return float(loss.detach()),z.grad.numpy()

def run(out,mode,wp,maxiter=500,startfile=None,wroot=0.,target=1e-4):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    if startfile:
        z0=np.array([float.fromhex(t) for t in json.loads(Path(startfile).read_text())['end_hex']])
    else:z0=pack(literal())
    obj=Free(z0,wp=wp,wroot=wroot,mode=mode,target=target);trace=[];t=time.monotonic()
    def callback(z):
        trace.append(dict(iter=len(trace)+1,**(obj.last or {})))
        if len(trace)%50==0:print(mode,wp,len(trace),trace[-1],flush=True)
        (out/'last.json').write_text(json.dumps(dict(end_hex=[float(u).hex() for u in z],iter=len(trace),last=obj.last),sort_keys=True)+'\n')
    result=minimize(obj.eval,z0,jac=True,method='L-BFGS-B',callback=callback,options=dict(maxiter=maxiter,maxls=40,ftol=1e-15,gtol=1e-9,maxcor=30))
    xx=unpack(torch.tensor(result.x)).detach().numpy()
    stats=census(xx)
    rec=dict(mode=mode,wp=wp,wroot=wroot,target=target,maxiter=maxiter,startfile=startfile,start_hex=[float(u).hex() for u in z0],end_hex=[float(u).hex() for u in result.x],loss=float(result.fun),nit=int(result.nit),nfev=int(result.nfev),success=bool(result.success),message=str(result.message),seconds=time.monotonic()-t,stats=stats,trace=trace)
    (out/'result.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in rec.items() if k not in ['trace','start_hex','end_hex']},indent=2),flush=True)
    return rec
if __name__=='__main__':
    run(sys.argv[1],sys.argv[2],float(sys.argv[3]),maxiter=int(sys.argv[4]),startfile=None if len(sys.argv)<6 or sys.argv[5]=='-' else sys.argv[5],wroot=float(sys.argv[6]) if len(sys.argv)>6 else 0.)
```
