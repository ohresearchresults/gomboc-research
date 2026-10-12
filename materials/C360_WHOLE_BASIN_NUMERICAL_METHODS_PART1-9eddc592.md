# material-9eddc592e128

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# C360 whole-basin methods: complete runnable source and exact seed, part1/2

Numerical research evidence, not an exact own110 certificate. These are the complete materially executed source units for whole radial/polar persistence descent, constrained own-volume coordinate motion, and integer-grid repair. No hidden scout.py or sandbox helper is required. Part2 contains the distinct finite-cap and affine methods that depend on this base. Extract each FILE block with its terminal newline. The C360_POINTS.json block also has a terminal newline. Environment CPython3.13.5,NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu,float64,OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1,Torch1thread. Fresh output directories are required.

The exact seed is the physical point hull of the original ENERGY_VERTEX62_G5 recovered from [internal-source-reference]; the complete62 integer rows are repeated here under a smaller input filename. Its exact own121/weak000 status is separate existing evidence; the numerical routines below do not exhaust weak/SUH acceptance predicates. The union-find bar calculation uses squared radial superlevel merge heights on the actual physical and centered polar1-skeleta. Relative lifetime=(peak-saddle)/peak. Positive nonzero lifetimes represent secondary extrema; finite tolerances can miss very small positive bars. The numerical topology groups polar facet normals rounded to10 decimal digits; this is NOT exact maximal-face reconstruction, particularly after ill-conditioned cuts. Hard E<311 checks here are nomination filters, not exact complexity certificates.

## Executed finite runs and limitations
Commands, with input C360_POINTS.json and fresh directory names:
`python PEAK_MERGE_FLOW.py C360_POINTS.json flow1 --steps 160 --trust .02`:160 completed iterations,150 accepted; endpoint floating V44/E126/F84,largest U relative bar.09292755361282727 versus starting.6849764714802099;20 secondary U and29 secondary S bars above1e-10. Squared loss fell.4691927664814788→.022095274873355584 by fragmentation into many critical pairs, NOT progress in the own110 census.
`python PEAK_MERGE_LOG_FLOW.py C360_POINTS.json logflow1 --steps 200 --trust .02`:200 completed,161 accepted; endpoint V61/E177/F118,largest Ubar.6715127567898515,7 U bars above1e-10,0 S bars above1e-10 but actual smax9.973805610829415e-13. This last quantity prevents inferring exact S1 from the bar threshold. Log-loss4.221937463933409.
`python PEAK_GUARDED_SLP.py C360_POINTS.json guarded1 --steps 160 --trust .01`:149 completed,89 accepted,ended naturally at shrinking trust below1e-10. Floating S1/U2,V62/E180/F120,largest Ubar.6714189845668551. Positive directed escapes at original61→59 and59→41 approached roughly6.69e-17 and1.49e-16, so this is a weak-boundary nomination, not a robust improved exact body. It guards current selected arrows but accepts finite steps by direct numeric counts; the shrinking relative floor does not prevent approaching zero.
`python PEAK_FIXED_GUARD_SLP.py C360_POINTS.json guarded2 --steps 250 --trust .01 --margin .000001`:interrupted externally after207 fully saved iterations,143 accepted; NOT250 completed. Saved endpoint floating S1/U2,V62/E180/F120,largest Ubar.6716971348976005,positive-arrow acceptance floor.8e-6. To reproduce only the completed prefix use --steps207 with a separating space. This finite result is not an obstruction theorem.
`python INTEGER_GRID_SEARCH.py C360_POINTS.json grid4 --grid 10000 --steps 10`:stopped on success at step2; two accepted one-coordinate repairs relative to its binary64 rounded initial points. `python INTEGER_GRID_SEARCH.py C360_POINTS.json grid3 --grid 1000 --steps 30`:stopped on success at step9. These nominations were then passed to independent exact A/B/third-mass verification and preserved as separate rational bodies in [internal-source-reference] with audit dependency [internal-source-reference]. Grid quantization is the literal NumPy operation rint((float(P)/100000)*grid), NOT necessarily exact-rational ties-to-even. Exact rational rows in the accepted geometry capsule are authoritative. RepairedG3 differs from exact ties-to-even rounding by nine integer edits(13,1,+1),(22,1,-1),(34,1,+1),(52,2,+1),(54,0,+1),(54,2,+1),(55,0,+1),(55,1,-1),(61,0,-1). RepairedG4 differs from exact ties-to-even by four edits(44,1,-1),(54,0,+1),(56,1,+1),(59,0,+1), two arising already from binary64 tie displacement.
`python INTEGER_GRID_SEARCH.py C360_POINTS.json grid2 --grid 100 --steps 50` was externally interrupted. Last fully saved start-of-iteration checkpoint is step24, floating V58/E167/F111,S4/U2,not a complete50-step run and not an exact retained own121 body. No whole-grid exclusion is implied.

Hashes identify the complete source bytes, not mathematical verification. PEAK_MERGE_FLOW.py5007bytes SHA87e7e3057ace3c71b60a4328d4b0b92b142470c8f973af7c168c8f18bddf3b92; PEAK_GUARDED_SLP.py4936bytes SHA8966db54a29ec28c8de3fb3d06cc201b61cdc988cf98f97bc5450c83d72b629c; INTEGER_GRID_SEARCH.py2687bytes SHA436bb32af201d16a73a1f2ac8aa511dffabe546dbca7ed055f65f33c7de0909c. MAKE_METHOD_VARIANTS.py1527bytes SHA4f7f14ee72012341de200d414e34aec3e0f60fda8d4d93c7268f918742d1cae5 applies the complete exact patches; executing it produces PEAK_MERGE_LOG_FLOW.py5031bytes SHAc5979fa24389acc554c544a3355bbba74133536733e23f6c42bc7f7524d26f28 and PEAK_FIXED_GUARD_SLP.py5141bytes SHA3829bc70ff94b5c736bbd48fdb97e3175c77356cb1660d66f16c74e7cb53fe91. The variant reconstruction was executed and printed EXECUTED_VARIANT_SOURCE_HASHES_PASS. Exact coordinate recovery of the auditedG3/G4/C318 bodies does not require rerunning any numerical optimizer.

## FILE C360_POINTS.json (1345bytes,SHA0bcafeecc250eb2ae560197db620d5198940cc2ed63d2b4df582e3935711c037)
```json
{"grid":100000,"points":[[-68082,-20590,-139121],[-67857,-10679,-139614],[-63974,990,-138978],[-62926,-36863,-132919],[-62448,-38221,-132726],[-61652,5346,-137542],[-60917,9161,-134815],[-55497,14216,-129682],[-42831,-62596,-98188],[-34174,33251,-106828],[-32116,33751,112079],[-31481,21748,114186],[-30149,15405,112430],[-30419,37437,-89345],[-29415,46326,109793],[-27137,-68603,-81288],[-23883,34948,-99432],[-21791,60127,106594],[-18760,-3418,113474],[-18579,-8617,109871],[-11351,73413,102593],[-9135,-28027,84722],[-7936,41853,-73699],[-6136,75520,98608],[-3620,51732,-40448],[-2373,65676,23769],[3482,62034,-1919],[8401,-73224,-51309],[10649,70813,95323],[10919,-27914,85456],[14922,58602,-14066],[15165,-21196,95496],[14578,-11058,107664],[23410,-71489,-45388],[26749,56349,-13001],[27252,27552,-55060],[30460,-1535,103226],[31999,-52097,454],[43775,24802,-39434],[45883,58977,33307],[45900,-37869,17828],[48696,-52392,-40729],[47636,17151,-39756],[47916,33819,-27914],[49931,37675,-22200],[51642,9753,-39586],[51471,54051,2855],[51902,7547,-40296],[52659,41206,-15510],[53100,2851,-40556],[53981,-2298,-41201],[55952,-14031,-38831],[56077,46287,-5765],[59293,37557,-5674],[60782,30598,-7164],[61148,27171,-8147],[61387,9205,-15514],[61796,15417,-12138],[63559,12340,25960],[64194,-33571,-13506],[65998,-5490,33342],[67151,-21203,3670]]}
```

## FILE PEAK_MERGE_FLOW.py
```python
"""Numerical whole radial/polar persistence loss on actual filled convex hulls.
All trial geometry and ordinary filled moments are rebuilt; not an exact verifier.
No reference-center or nonuniform mass is substituted. Float64, one thread.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse, json, pathlib
from collections import defaultdict
import numpy as np
import torch
from scipy.spatial import ConvexHull
DT=torch.float64
torch.set_num_threads(1)

def geom(x, f, ids):
    v=x.reshape(-1,3);a,b,c=v[f[:,0]],v[f[:,1]],v[f[:,2]]
    d=(a*torch.linalg.cross(b,c)).sum(1);volume=d.sum()/6
    center=(d[:,None]*(a+b+c)).sum(0)/(4*d.sum())
    p=v-center;a,b,c=p[f[:,0]],p[f[:,1]],p[f[:,2]]
    n=torch.linalg.cross(b-a,c-a);q=n/(n*a).sum(1)[:,None]
    return p,q[ids],center,volume

def topology(v):
    h=ConvexHull(v);f=h.simplices.copy()
    n=np.cross(v[f[:,1]]-v[f[:,0]],v[f[:,2]]-v[f[:,0]])
    rev=(n*h.equations[:,:3]).sum(1)<0;f[rev]=f[rev][:,[0,2,1]]
    p,q,c,vol=geom(torch.tensor(v.reshape(-1),dtype=DT),torch.tensor(f),torch.arange(len(f)))
    p,q,c=p.numpy(),q.numpy(),c.numpy()
    _,ids,inv=np.unique(np.round(q,10),axis=0,return_index=True,return_inverse=True)
    owners=defaultdict(list)
    for k,tri in enumerate(f):
        for i,j in zip(tri,np.roll(tri,-1)):owners[tuple(sorted((int(i),int(j))))].append(int(inv[k]))
    pe=[];qe=[]
    for e,fs in sorted(owners.items()):
        assert len(fs)==2
        if fs[0]!=fs[1]:pe.append(e);qe.append(sorted(fs))
    return f,ids,np.array(pe,int),np.array(sorted(set(map(tuple,qe))),int),p,q[ids],c,float(vol)

def pairs(p,e):
    r=(p*p).sum(1);a=p[e[:,0]];dv=p[e[:,1]]-a
    t=np.clip(-(a*dv).sum(1)/(dv*dv).sum(1),0,1);w=((a+t[:,None]*dv)**2).sum(1)
    par=np.arange(len(p));peak=np.arange(len(p));out=[]
    def root(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for k in sorted(range(len(e)),key=lambda k:(-w[k],int(e[k,0]),int(e[k,1]))):
        i,j=map(root,e[k])
        if i==j:continue
        if (r[peak[i]],-peak[i])<(r[peak[j]],-peak[j]):i,j=j,i
        out.append((int(peak[j]),int(e[k,0]),int(e[k,1])))
        par[j]=i
    return np.array(out,int)

def bars_torch(v, pairing):
    pk=v[pairing[:,0]];a=v[pairing[:,1]];b=v[pairing[:,2]];dv=b-a
    t=torch.clamp(-(a*dv).sum(1)/(dv*dv).sum(1),0,1)
    h=((a+t[:,None]*dv)**2).sum(1);B=(pk*pk).sum(1)
    return torch.clamp((B-h)/B,min=0)

def inspect(x,gradient=False):
    f,ids,pe,qe,p,q,c,vol=topology(np.asarray(x).reshape(-1,3))
    pp=pairs(p,pe);qp=pairs(q,qe)
    t=torch.tensor(x,dtype=DT,requires_grad=gradient)
    a,b,ctr,vt=geom(t,torch.tensor(f),torch.tensor(ids))
    ub=bars_torch(a,torch.tensor(pp));sb=bars_torch(b,torch.tensor(qp))
    loss=(ub**2).sum()+(sb**2).sum()
    data=dict(V=len(np.unique(f)),E=len(pe),F=len(ids),volume=vol,centroid=c.tolist(),
       loss=float(loss.detach()),u_bar_count=int((ub.detach().numpy()>1e-10).sum()),s_bar_count=int((sb.detach().numpy()>1e-10).sum()),
       u_max=float(ub.max().detach()),s_max=float(sb.max().detach()),u_sum=float(ub.sum().detach()),s_sum=float(sb.sum().detach()))
    if gradient:
        loss.backward();return data,t.grad.numpy()
    return data

def run(inp,out,steps=300,trust=.02):
    obj=json.load(open(inp));v=np.array(obj.get('raw',obj.get('points')),float)
    if 'grid' in obj:v/=obj['grid']
    st=inspect(v.reshape(-1));v-=np.array(st['centroid']);target=st['volume'];x=v.reshape(-1)
    dest=pathlib.Path(out);dest.mkdir(parents=True,exist_ok=False)
    path=[];momentum=np.zeros_like(x)
    for it in range(steps):
        st,g=inspect(x,True);scale=target**(1/3)
        direction=-g/max(np.linalg.norm(g,np.inf),1e-30)*trust*scale
        accepted=False
        for alpha in (1.,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625):
            xx=x+alpha*direction
            try:
                nxt=inspect(xx)
                if nxt['E']>=311 or nxt['volume']<=0:continue
                xx=(xx.reshape(-1,3)-np.array(nxt['centroid']))*(target/nxt['volume'])**(1/3);xx=xx.reshape(-1)
                nxt=inspect(xx)
            except Exception:continue
            if nxt['loss']<st['loss']-max(1e-12,1e-5*alpha*trust*np.linalg.norm(g,1)):
                x=xx;accepted=True;break
        rec=dict(step=it,accepted=accepted,trust=trust,alpha=alpha,**(nxt if accepted else st));path.append(rec)
        print(json.dumps(rec),flush=True)
        (dest/'checkpoint.json').write_text(json.dumps(dict(raw=x.reshape(-1,3).tolist(),history=path),separators=(',',':')))
        if accepted:trust=min(.06,trust*1.2)
        else:trust*=.5
        if trust<1e-10 or rec['loss']<1e-16:break
    return x,path

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output');ap.add_argument('--steps',type=int,default=300);ap.add_argument('--trust',type=float,default=.02);a=ap.parse_args();run(a.input,a.output,a.steps,a.trust)
```

## FILE PEAK_GUARDED_SLP.py
```python
"""Numerical own-filled-centroid persistence descent with no-birth escape guards.
A finite all-vertex-coordinate SLP; all trial hulls and moments are rebuilt.
Not an exact verifier, nor a proof of nonexistence after a failed search.
Complete dependency: PEAK_MERGE_FLOW.py.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,json,pathlib
import numpy as np
import torch
from scipy.optimize import linprog
from PEAK_MERGE_FLOW import topology,geom,pairs,bars_torch,DT

def arrows(x,ed):
    aa=np.vstack((ed,ed[:,::-1]));i,j=aa[:,0],aa[:,1];d=x[j]-x[i]
    val=np.einsum('ij,ij->i',x[i],d)/(np.linalg.norm(x[i],axis=1)*np.linalg.norm(d,axis=1))
    vertices=np.unique(ed);out=[];best=[]
    for k in vertices:
        ix=np.flatnonzero(i==k);a=ix[np.argmax(val[ix])];out.append(aa[a]);best.append(val[a])
    return np.array(out),np.array(best)

def report(x):
    f,ids,pe,qe,p,q,c,vol=topology(x.reshape(-1,3));ua,um=arrows(p,pe);sa,sm=arrows(q,qe)
    pp=pairs(p,pe);qp=pairs(q,qe)
    u=bars_torch(torch.tensor(p),torch.tensor(pp)).numpy();s=bars_torch(torch.tensor(q),torch.tensor(qp)).numpy()
    st=dict(V=len(np.unique(f)),E=len(pe),F=len(ids),volume=vol,centroid=c.tolist(),S=int((sm<0).sum()),U=int((um<0).sum()),u_max=float(max(u)),s_max=float(max(s)),u_sum=float(sum(u)),s_sum=float(sum(s)),U_indices=ua[um<0,0].tolist(),S_indices=sa[sm<0,0].tolist())
    return st,(f,ids,pe,qe,p,q,ua,um,sa,sm,pp,qp,u,s)

def linearization(x,ctx,margin):
    f,ids,pe,qe,p,q,ua,um,sa,sm,pp,qp,u,s=ctx
    # The surviving roots and the single secondary maximum are allowed to move.
    pr=int(np.argmax((p*p).sum(1)));sr=int(np.argmax((q*q).sum(1)));bad=int(pp[np.argmax(u),0])
    ku=(ua[:,0]!=pr)&(ua[:,0]!=bad);ks=sa[:,0]!=sr
    au=torch.tensor(ua[ku]);ass=torch.tensor(sa[ks]);ft=torch.tensor(f);it=torch.tensor(ids);bpt=torch.tensor(pp[[int(np.argmax(u))]])
    old=np.r_[um[ku],sm[ks]];floor=np.minimum(old*.5,margin)
    def fun(xx):
        a,b,c,v=geom(xx,ft,it)
        def av(y,ar):
            d=y[ar[:,1]]-y[ar[:,0]];yy=y[ar[:,0]]
            return (yy*d).sum(1)/(torch.linalg.vector_norm(yy,dim=1)*torch.linalg.vector_norm(d,dim=1))
        return torch.cat((bars_torch(a,bpt),av(a,au),av(b,ass),c,torch.log(v).reshape(1)))
    xt=torch.tensor(x,dtype=DT,requires_grad=True);z=fun(xt).detach().numpy()
    J=torch.autograd.functional.jacobian(fun,xt,vectorize=True).detach().numpy()
    return z,J,floor

def run(inp,out,steps=200,trust=.01,margin=1e-5):
    obj=json.load(open(inp));v=np.array(obj.get('raw',obj.get('points')),float)
    if 'grid'in obj:v/=obj['grid']
    st,_=report(v.reshape(-1));v-=np.array(st['centroid']);target=st['volume'];x=v.reshape(-1)
    dst=pathlib.Path(out);dst.mkdir(exist_ok=False);history=[]
    for it in range(steps):
        st,ctx=report(x);z,J,floor=linearization(x,ctx,margin);m=len(floor);n=len(x)
        # Coordinate L1 regularization removes gratuitous null directions.
        obj=np.r_[J[0],np.full(n,1e-6)]
        A=np.vstack((np.c_[-J[1:1+m],np.zeros((m,n))],np.c_[np.eye(n),-np.eye(n)],np.c_[-np.eye(n),-np.eye(n)]))
        b=np.r_[z[1:1+m]-floor,np.zeros(2*n)]
        res=linprog(obj,A_ub=A,b_ub=b,A_eq=np.c_[J[-4:],np.zeros((4,n))],b_eq=np.zeros(4),bounds=[(-trust*target**(1/3),trust*target**(1/3))]*n+[(0,None)]*n,method='highs')
        accepted=False;why=str(res.message);alpha=0
        if res.success:
            dx=res.x[:n]
            for alpha in (1.,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625):
                xx=x+alpha*dx
                try:
                    ns,_=report(xx)
                    if ns['E']>=311 or ns['volume']<=0 or ns['S']>1 or ns['U']>2:continue
                    if ns['u_max']>=st['u_max']-max(1e-12,1e-4*alpha*max(0,-J[0]@dx)):continue
                    xx=(xx.reshape(-1,3)-np.array(ns['centroid']))*(target/ns['volume'])**(1/3);xx=xx.reshape(-1)
                    ns,_=report(xx)
                    if ns['S']>1 or ns['U']>2:continue
                    x=xx;accepted=True;break
                except Exception as e:why=type(e).__name__;continue
        rec=dict(step=it,accepted=accepted,trust=trust,alpha=alpha,lp_success=bool(res.success),why=why,**(ns if accepted else st));history.append(rec)
        print(json.dumps(rec),flush=True)
        (dst/'checkpoint.json').write_text(json.dumps(dict(raw=x.reshape(-1,3).tolist(),history=history),separators=(',',':')))
        if accepted:trust=min(.04,trust*1.3)
        else:trust*=.5
        if trust<1e-10 or rec['S']==rec['U']==1:break
    return x,history
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output');ap.add_argument('--steps',type=int,default=200);ap.add_argument('--trust',type=float,default=.01);ap.add_argument('--margin',type=float,default=1e-5);a=ap.parse_args();run(a.input,a.output,a.steps,a.trust,a.margin)
```

## FILE MAKE_METHOD_VARIANTS.py
```python
"""Recreate the two exactly executed variants, asserting their complete byte hashes."""
from pathlib import Path
from hashlib import sha256

def rewrite(source,target,replacements,expected):
    s=Path(source).read_text()
    for old,new in replacements:
        assert old in s
        s=s.replace(old,new)
    b=s.encode();assert sha256(b).hexdigest()==expected
    Path(target).write_bytes(b)

rewrite('PEAK_MERGE_FLOW.py','PEAK_MERGE_LOG_FLOW.py',[
('loss=(ub**2).sum()+(sb**2).sum()','loss=torch.log1p(ub/.01).sum()+torch.log1p(sb/.01).sum()')],
'c5979fa24389acc554c544a3355bbba74133536733e23f6c42bc7f7524d26f28')
rewrite('PEAK_GUARDED_SLP.py','PEAK_FIXED_GUARD_SLP.py',[
('Numerical own-filled-centroid persistence descent with no-birth escape guards.','Numerical own-filled-centroid persistence descent with FIXED positive escape guards.'),
('floor=np.minimum(old*.5,margin)','floor=np.full(len(old),margin)'),
('def run(inp,out,steps=200,trust=.01,margin=1e-5):','def run(inp,out,steps=200,trust=.01,margin=1e-6):'),
("if ns['S']>1 or ns['U']>2:continue\n                    x=xx", "if ns['S']>1 or ns['U']>2:continue\n                    _,ctxnext=report(xx)\n                    nua,num,nsa,nsm=ctxnext[6:10]\n                    if min(num[num>0],default=1.)<margin*.8 or min(nsm[nsm>0],default=1.)<margin*.8:continue\n                    x=xx"),
('type=float,default=1e-5','type=float,default=1e-6')],
'3829bc70ff94b5c736bbd48fdb97e3175c77356cb1660d66f16c74e7cb53fe91')
print('EXECUTED_VARIANT_SOURCE_HASHES_PASS')
```

## FILE INTEGER_GRID_SEARCH.py
```python
"""Finite integer-coordinate rounding and local repair of the physical C360 seed.
Float own S/U nominations only; independent exact full audits are separate.
Complete dependencies: PEAK_GUARDED_SLP.py and PEAK_MERGE_FLOW.py.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse,json,pathlib
import numpy as np
from PEAK_GUARDED_SLP import report

def fit(P,grid):
    s,c=report(P.astype(float).ravel()/grid);f,ids,pe,qe,p,q,ua,um,sa,sm,pp,qp,u,z=c
    # Preserve the two actual endpoint roots; score no surplus U and S.
    vals=np.r_[np.sort(um)[2:],np.sort(sm)[1:]]
    # Counts dominate, then repair small sign margins.
    loss=int((vals<0).sum())+np.maximum(1e-5-vals,0).sum()
    s['margin']=float(min(vals));return float(loss),s

def search(inp,out,grid=1000,steps=400,seed=19):
    obj=json.load(open(inp));raw=np.array(obj.get('raw',obj.get('points')),float)/obj.get('grid',1);P=np.rint(raw*grid).astype(int)
    dst=pathlib.Path(out);dst.mkdir(exist_ok=False);rng=np.random.default_rng(seed);loss,st=fit(P,grid);hist=[]
    for it in range(steps):
        rec=dict(step=it,loss=loss,**st);hist.append(rec)
        if it%10==0 or st['S']==1 and st['U']==2:print(json.dumps(rec),flush=True)
        (dst/'best.json').write_text(json.dumps(dict(grid=grid,points=P.tolist(),status=rec),separators=(',',':')))
        if st['S']==1 and st['U']==2 and st['margin']>1e-6:break
        best=None
        # Full coordinate-neighborhood, fixed seed controls tie selection only.
        order=rng.permutation(P.size)
        for k in order:
            i,j=divmod(int(k),3)
            for d in (-1,1):
                Q=P.copy();Q[i,j]+=d
                try:ll,ss=fit(Q,grid)
                except Exception:continue
                if best is None or ll<best[0]:best=(ll,Q,ss,(i,j,d))
        if best is None:break
        if best[0]>=loss:
            # Bounded two-coordinate perturbation, never accepted as a proof.
            Q=P.copy()
            for k in rng.choice(P.size,2,replace=False):
                i,j=divmod(int(k),3);Q[i,j]+=rng.choice([-1,1])
            try:ll,ss=fit(Q,grid)
            except Exception:continue
            if ll<loss+1e-6:P,loss,st=Q,ll,ss
        else:loss,P,st,_=best
    (dst/'history.json').write_text(json.dumps(hist,separators=(',',':')))
    return P,st
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('input');a.add_argument('output');a.add_argument('--grid',type=int,default=1000);a.add_argument('--steps',type=int,default=400);a.add_argument('--seed',type=int,default=19);o=a.parse_args();search(o.input,o.output,o.grid,o.steps,o.seed)
```
