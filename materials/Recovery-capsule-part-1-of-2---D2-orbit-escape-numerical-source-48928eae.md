# material-48928eaea0dc

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 1/2: D2_ORBIT_ESCAPE_FINITE_20260923
This capsule preserves a numerical method and finite nonwinning experiments, not an exact class110 certificate. Part1 contains the complete original direct-edge module. Part2 supplies complete exact transformations to the orbit-exterior and BASE-active charts, drivers, frozen checkpoint data and the finite ledger. Do not treat part1 alone as a new computed endpoint. Analytic foundation is the independent complete proof [internal-source-reference].

Save the sole Python block below as d2_direct.py, preserving its terminal newline. It has9803 UTF-8 bytes, SHA256 d219e9058e548f269ed278ff616fad2af0bd5091bbf302dba54991e68e79d523. Original numerical environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, binary64, one numerical thread. No randomness for trial0; trial seeds and perturbation sizes are fully specified in the code. Source/checkpoint recovery is exact; bit-identical optimizer histories across other environments are not claimed.

Example original command: python d2_direct.py 1 0 150 .001 .0001. This is the old DIRECT objective: it permits same-orbit negative edges as the maximizer and is preserved to reproduce the diagnosed orbit-contraction failure. Geometry is uniformly filled, actual-volume-centred, and the polar uses the SAME physical centre. Floating maximal-plane merging, strict S/U arrow counts and tolerances are not a complete weak/mixed-edge certificate.

```python
"""D2_DIRECT_EDGE_20260923: numerical search, not an exact certificate.
Two vertical reflections, independent supporting-plane representatives, true
maximal-edge outward escapes at the actual homogeneous volume centroid.
All constants, inputs and evaluation code are self-contained.
"""
import os
for s in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[s]='1'
import json, sys
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
import torch

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
SIGNS=np.array([[1,1,1],[-1,1,1],[-1,-1,1],[1,-1,1]],float)
SEEDS=np.array([
[.348924535735755,.430846292422864,.09177882694238823,1.1380793703098433,.919385164669734,.5366341588107586],
[.2286120132045184,.35184658419274134,-.05235369067970339,1.2729454408210938,.8947215520204572,.5461429524620107],
[.21075988583083555,.32866098715047964,-.06079203628228995,1.1026087116023102,.9851448939381748,.5456455760197303]])

def reps_seed(params,nlat=9,nphi=8):
    c,d,shift,warp,cap,aspect=map(float,params)
    def F(x):
        return (c*x*x+(1-c)*(1-x)**2*c*x/(c+x))/(c*x+(1-c)*(1-x)**2)
    def radius(th,ph):
        f=np.pi*F(th/np.pi+.5)-np.pi/2
        g=-np.pi*F(-th/np.pi+.5)+np.pi/2
        a=np.cos(ph)**2*np.cos(f)**2;b=np.sin(ph)**2*np.cos(g)**2
        return 1+d*(a*np.sin(f)+b*np.sin(g))/(a+b)
    ans=[]
    for s in np.linspace(-.9,.9,nlat):
        th=np.arcsin(np.tanh(warp*np.arctanh(s)))+shift*(1-s*s)
        for j in range(nphi//4):
            ph=(j+.5)*2*np.pi/nphi;r=radius(th,ph);e=1e-5
            rt=(radius(th+e,ph)-radius(th-e,ph))/(2*e)
            rp=(radius(th,ph+e)-radius(th,ph-e))/(2*e)
            u=np.array([np.cos(th)*np.cos(ph),np.cos(th)*np.sin(ph),np.sin(th)])
            et=np.array([-np.sin(th)*np.cos(ph),-np.sin(th)*np.sin(ph),np.cos(th)])
            ep=np.array([-np.sin(ph),np.cos(ph),0.])
            n=u-rt/r*et-rp/(r*np.cos(th))*ep;n[0]/=aspect;n[1]*=aspect
            ans.append(n/r)
    ans.append(np.array([cap/np.sqrt(2)/aspect,cap/np.sqrt(2)*aspect,1])/(1+d))
    return np.array(ans),1/(1-d)

def chart(r,b):
    a=r.copy();a[:,:2]=np.log(abs(a[:,:2]));return np.r_[a.ravel(),np.log(b)]
def unchart(z):
    a=z[:-1].reshape(-1,3);r=np.c_[np.exp(a[:,:2]),a[:,2]];return r,np.exp(z[-1])
def expand(r,b):
    return np.vstack([(r[:,None,:]*SIGNS[None,:,:]).reshape(-1,3),[0.,0.,-b]])
def tensor_q(z):
    a=z[:-1].reshape(-1,3);r=torch.cat((torch.exp(a[:,:2]),a[:,2:]),dim=1)
    q=(r[:,None,:]*torch.as_tensor(SIGNS)[None,:,:]).reshape(-1,3)
    return torch.cat((q,torch.stack((z[-1]*0,z[-1]*0,-torch.exp(z[-1])))[None,:]))

def topology(q,tol=3e-8):
    h=ConvexHull(q)
    if np.max(h.equations[:,3])>=-1e-8:raise ValueError('unbounded')
    candidates=h.equations[:,:3]/(-h.equations[:,3,None]);groups=[];vv=[];triples=[]
    for v,tri in zip(candidates,h.simplices):
        hits=[i for i,w in enumerate(vv) if np.max(abs(w-v))<tol]
        if hits:groups[hits[0]].update(map(int,tri))
        else:vv.append(v);groups.append(set(map(int,tri)));triples.append(list(map(int,tri)))
    p=np.linalg.solve(q[np.array(triples)],np.ones((len(triples),3,1)))[...,0]
    if np.max(q@p.T-1)>tol*10:raise ValueError('global support')
    faces=[];active=[]
    for f in sorted(map(int,h.vertices)):
        ids=np.array([i for i,g in enumerate(groups) if f in g],int)
        if len(ids)<3:raise ValueError('degenerate facet')
        ctr=p[ids].mean(0);n=q[f]/np.linalg.norm(q[f]);e=p[ids[0]]-ctr;e/=np.linalg.norm(e);u=np.cross(n,e)
        ph=np.arctan2((p[ids]-ctr)@u,(p[ids]-ctr)@e)
        faces.append(ids[np.argsort(ph)].tolist());active.append(f)
    edges={};tris=[]
    for f,ids in enumerate(faces):
        for a,b in zip(ids,ids[1:]+ids[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(f)
        for j in range(1,len(ids)-1):tris.append([ids[0],ids[j],ids[j+1]])
    if any(len(owners)!=2 for owners in edges.values()):raise ValueError('edge owners')
    e=np.array(sorted(edges),int);de=np.array([edges[tuple(t)] for t in e],int)
    if len(p)-len(e)+len(faces)!=2:raise ValueError('Euler')
    return dict(triples=np.array(triples),faces=faces,active=np.array(active),triangles=np.array(tris),edges=e,dual_edges=de)

def coords(q,t):
    p=np.linalg.solve(q[t['triples']],np.ones((len(t['triples']),3,1)))[...,0]
    a,b,c=np.moveaxis(p[t['triangles']],1,0);v6=np.einsum('ij,ij->i',a,np.cross(b,c))
    c0=(v6[:,None]*(a+b+c)).sum(0)/(4*v6.sum())
    return p,c0,v6.sum()/6

def tensor_geometry(q,t):
    p=torch.linalg.solve(q[torch.as_tensor(t['triples'])],torch.ones((len(t['triples']),3)))
    a,b,c=p[torch.as_tensor(t['triangles'])].unbind(1);v6=(a*torch.linalg.cross(b,c)).sum(1)
    c0=(v6[:,None]*(a+b+c)).sum(0)/(4*v6.sum())
    qa=q[torch.as_tensor(t['active'])];polar=qa/(1-(qa*c0).sum(1))[:,None]
    return p-c0,polar,c0,v6.sum()/6

def arrows(x,e):
    i=torch.as_tensor(np.r_[e[:,0],e[:,1]]);j=torch.as_tensor(np.r_[e[:,1],e[:,0]])
    d=x[j]-x[i];dot=(x[i]*d).sum(1)
    scale=torch.sqrt(torch.clamp((x[i]*x[i]).sum(1)*(d*d).sum(1),min=1e-24))
    scores=dot/scale
    best=torch.full((len(x),),-float('inf')).scatter_reduce(0,i,scores,reduce='amax',include_self=True)
    return best

def census(q,t=None):
    if t is None:t=topology(q)
    with torch.no_grad():
        x,y,c,v=tensor_geometry(torch.as_tensor(q),t)
        u=arrows(x,t['edges']).numpy();s=arrows(y,t['dual_edges']).numpy()
    p=x.numpy()+c.numpy();qa=q[t['active']]
    rootU=int(np.argmax(p[:,2]));rootS=int(np.where(t['active']==len(q)-1)[0][0])
    mu=np.delete(u,rootU);ms=np.delete(s,rootS)
    return dict(V=len(p),E=len(t['edges']),F=len(qa),C=2*len(t['edges']),S=int((s<-1e-9).sum()),U=int((u<-1e-9).sum()),
      centroid=c.numpy().tolist(),volume=float(v),rootU=rootU,rootS=rootS,minU=float(mu.min()),minS=float(ms.min()),
      S_ids=np.where(s<-1e-9)[0].tolist(),U_ids=np.where(u<-1e-9)[0].tolist())

class Objective:
    def __init__(self,tag,weight,margin,z0):
        self.tag=tag;self.weight=weight;self.margin=margin;self.z0=z0;self.calls=0;self.best=np.inf;self.rows=[];self.countbest=(999,999)
    def __call__(self,z):
        self.calls+=1
        try:
            r,b=unchart(z);q=expand(r,b);top=topology(q);p,c,v=coords(q,top)
            if len(q)-1 not in top['active']:raise ValueError('base inactive')
            rootU=int(np.argmax(p[:,2]));rootS=int(np.where(top['active']==len(q)-1)[0][0])
            if np.linalg.norm(p[rootU,:2])>1e-6:raise ValueError('top nonaxial')
            zz=torch.tensor(z,requires_grad=True);x,y,cc,vv=tensor_geometry(tensor_q(zz),top)
            u=arrows(x,top['edges']);s=arrows(y,top['dual_edges'])
            iu=np.delete(np.arange(len(x)),rootU);is_=np.delete(np.arange(len(y)),rootS)
            # Topology-local escape score: a positive outgoing true edge for EVERY nonroot.
            # It is not a sum of all rooted-tree segment chord losses.
            ul=torch.relu(self.margin-u[iu]).square().sum();sl=torch.relu(self.margin-s[is_]).square().sum()
            reg=1e-10*(zz-torch.as_tensor(self.z0)).square().sum()
            loss=self.weight*ul+sl+reg;loss.backward();val=float(loss.detach());g=zz.grad.numpy()
            if not np.isfinite(val) or not np.all(np.isfinite(g)):raise ValueError('nonfinite')
            cs=census(q,top);key=(cs['S']+cs['U'],max(cs['S'],cs['U']))
            if val<self.best or key<self.countbest:
                row=dict(call=self.calls,loss=val,lossU=float(ul.detach()),lossS=float(sl.detach()),**cs)
                self.rows.append(row)
                if key<self.countbest:
                    self.countbest=key
                    out=dict(reps=r.tolist(),bottom=b,z=z.tolist(),**row)
                    with open(self.tag+'_countbest.json','w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
                    print(self.tag,'COUNT',key,'loss',val,'S/U',cs['S'],cs['U'],'C',cs['C'],flush=True)
                if val<self.best:
                    self.best=val
                    out=dict(reps=r.tolist(),bottom=b,z=z.tolist(),**row)
                    with open(self.tag+'_best.json','w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
                with open(self.tag+'_history.json','w') as f:json.dump(self.rows,f,sort_keys=True,indent=2);f.write('\n')
            if self.calls%100==0:print(self.tag,'calls',self.calls,'best',self.best,'counts',self.countbest,flush=True)
            return val,g
        except (ValueError,RuntimeError,np.linalg.LinAlgError) as exc:
            if self.calls<=3:print(self.tag,'INVALID',type(exc).__name__,str(exc),flush=True)
            return 1e3+1e-3*float((z-self.z0)@(z-self.z0)),.002*(z-self.z0)

def run(seed,trial,maxiter,weight=1.,margin=.001,checkpoint=None):
    if checkpoint:
        data=json.load(open(checkpoint));r=np.array(data['reps']);b=data['bottom']
    else:r,b=reps_seed(SEEDS[seed])
    z=chart(r,b);rng=np.random.default_rng(202609230600+100*seed+trial)
    if trial:z+=rng.normal(0,.015 if trial<4 else .05,size=len(z))
    tag=f'D2_DIRECT_R2_{seed}_{trial}_w{weight:g}_m{margin:g}'
    ob=Objective(tag,weight,margin,z.copy())
    bounds=[(-14,4) if k%3!=2 else (-6,6) for k in range(len(z)-1)]+[(-2,3)]
    res=minimize(ob,z,jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':maxiter,'maxls':25,'ftol':1e-15,'gtol':1e-9,'maxcor':20})
    print(tag,'DONE',res.message,'calls',ob.calls,'best',ob.best,'counts',ob.countbest,flush=True)
    return ob

if __name__=='__main__':
    seed=int(sys.argv[1]);trial=int(sys.argv[2]);maxiter=int(sys.argv[3])
    w=float(sys.argv[4]) if len(sys.argv)>4 else 1.
    m=float(sys.argv[5]) if len(sys.argv)>5 else .001
    run(seed,trial,maxiter,w,m,sys.argv[6] if len(sys.argv)>6 else None)
```
