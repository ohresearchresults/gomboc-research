# material-eb98472f555c

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# D2_FINITE_REFLECTION_20260923 — Recovery capsule part 3/3

Parts 1/2: [internal-source-reference] and [internal-source-reference]. They recover all five exact rational nonwinners without numerical dependencies. This part preserves complete reusable numerical methods, literal input seeds, final binary64 checkpoint and finite-run ledger. Environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, one OPENBLAS/OMP/MKL/Torch thread. Binary64 optimization and quadrature are exploratory, not exact feasibility/infeasibility or global convexity certificates. A future optimizer replay may differ between environments; the literal exact objects in part 2 remain independently reproducible.

## Commands, units and outcomes
Write each named code block with LF and one final newline:
* d2_core.py: 6656 bytes, SHA256 d7ddbf90311ed7caac8c9e38ca39b9c18b3440ac558e4d4646ac3af705bcf496.
* d2_rooted.py: 4082 bytes, SHA256 bc888cfe5e6496d350dbc373989b9ad4bd9410d87bf6cde3cc1dc8792473b4b5.
* dlv_mass.py: 979 bytes, SHA256 0f03572ecaaf38ebdbba73e9c527b3714ff5e793f3c072c411dda5ab4660fe69.

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python d2_core.py` reproduces the three reflection-exact numerical seeds. These are new geometries relative to the original unreflected finite-difference DLV scouts in [internal-source-reference]/[internal-source-reference]/[internal-source-reference]. Exact reflection can merge tiny symmetry-breaking carriers; never reuse the old scout topology or infer closeness from its tiny unrooted loss. The four rational baseline inputs in part 2 are formed by nearest-even rounding of representatives and bottom at denominators 10^4 and 10^6, then audited as new H bodies.

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python d2_rooted.py 0 0 400` was actually run. It starts from seed0 with its transverse anisotropy undone, no random perturbation in trial0, and all remaining settings are literal below. It stopped at the 400-iteration limit after 476 objective calls and 412 improving rows. Initial numerical V81/E136/F57,C272,S29/U25, volume4.1866824092221355,c_z0.2686344987594242, total loss3.5512023074780825 (U2.157673038280452,S1.3935283054838974). Final/best call476: V99/E166/F69,C332,S45/U47, volume4.288558466708964,c_z0.5134366417246847, loss0.6946655971811456 (U0.3040673038111757,S0.3905972101234639), minimum non-root angular values U=-0.1441743831227266,S=-0.07038034063216671. Thus this finite descent lowers the summed rooted barrier while increasing equilibrium count; it is not a solution and not a family exclusion. The G6 rationalized control is exact(45,47,90),weak000 in part 2. The complete exact control survives even if the numerical trace does not. No claim is made that every floating iteration has been preserved.

The complete-chord maximum spanning tree is oriented at the forced axial top/base roots. For an edge child u,parent v its squared radial minimum is A if B>=A, C if B>=C, otherwise (AC-B^2)/(A+C-2B), where A=u.u,B=u.v,C=v.v. The tree loss sums log(A/w) downhill gaps. Zero gap on all rooted edges gives nondecreasing radial paths; this does not replace positive strict margins or the full mixed-H/weak audit. A small root-norm penalty and coordinate regularizer are also present, so the total numerical loss must not be identified with an exact equilibrium theorem.

## d2_core.py
```python
"""Numerical, reflection-exact finite support geometry; no exact certificate claims."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
os.environ.setdefault('MKL_NUM_THREADS','1')
import numpy as np
from scipy.spatial import ConvexHull
from scipy.sparse.csgraph import minimum_spanning_tree
import torch

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
SIGNS=np.array([[1,1,1],[-1,1,1],[-1,-1,1],[1,-1,1]],float)
SEEDS=[
[.348924535735755,.430846292422864,.09177882694238823,1.1380793703098433,.919385164669734,.5366341588107586],
[.2286120132045184,.35184658419274134,-.05235369067970339,1.2729454408210938,.8947215520204572,.5461429524620107],
[.21075988583083555,.32866098715047964,-.06079203628228995,1.1026087116023102,.9851448939381748,.5456455760197303]]

def dlv_reps(params, nlat=9, nphi=8):
    c,d,shift,warp,cap,aspect=map(float,params)
    assert nphi%4==0
    def F(x):
        return (c*x*x+(1-c)*(1-x)**2*c*x/(c+x))/(c*x+(1-c)*(1-x)**2)
    def radius(th,ph):
        f=np.pi*F(th/np.pi+.5)-np.pi/2
        g=-np.pi*F(-th/np.pi+.5)+np.pi/2
        a=np.cos(ph)**2*np.cos(f)**2
        b=np.sin(ph)**2*np.cos(g)**2
        return 1+d*(a*np.sin(f)+b*np.sin(g))/(a+b)
    out=[]
    for s in np.linspace(-.9,.9,nlat):
        th=np.arcsin(np.tanh(warp*np.arctanh(s)))+shift*(1-s*s)
        for j in range(nphi//4):
            ph=(j+.5)*2*np.pi/nphi
            r=radius(th,ph); e=1e-5
            rt=(radius(th+e,ph)-radius(th-e,ph))/(2*e)
            rp=(radius(th,ph+e)-radius(th,ph-e))/(2*e)
            u=np.array([np.cos(th)*np.cos(ph),np.cos(th)*np.sin(ph),np.sin(th)])
            et=np.array([-np.sin(th)*np.cos(ph),-np.sin(th)*np.sin(ph),np.cos(th)])
            ep=np.array([-np.sin(ph),np.cos(ph),0])
            n=u-rt/r*et-rp/(r*np.cos(th))*ep
            n[0]/=aspect; n[1]*=aspect
            out.append(n/r)
    out.append(np.array([cap/np.sqrt(2)/aspect,cap/np.sqrt(2)*aspect,1])/(1+d))
    return np.array(out), 1/(1-d)

def expand(reps, bottom):
    return np.vstack([(reps[:,None,:]*SIGNS[None,:,:]).reshape(-1,3),[0.,0.,-bottom]])

def topology(q,tol=3e-8):
    """Return true maximal-complex topology from a numerical dual hull.
    Every primal vertex is represented by a nonsingular triple of its incident H rows.
    """
    h=ConvexHull(q)
    if np.max(h.equations[:,3])>=-1e-8: raise ValueError('unbounded or bad origin')
    candidates=h.equations[:,:3]/(-h.equations[:,3,None])
    groups=[]; vv=[]; triples=[]
    for v,tri in zip(candidates,h.simplices):
        hits=[i for i,w in enumerate(vv) if np.max(abs(w-v))<tol]
        if hits:
            groups[hits[0]].update(map(int,tri))
        else:
            vv.append(v); groups.append(set(map(int,tri))); triples.append(list(map(int,tri)))
    p=np.linalg.solve(q[np.array(triples)],np.ones((len(triples),3,1)))[...,0]
    if np.max(q@p.T-1)>tol*10: raise ValueError('invalid topology')
    faces=[]; active=[]
    for f in sorted(map(int,h.vertices)):
        ids=np.array([i for i,g in enumerate(groups) if f in g],int)
        if len(ids)<3: raise ValueError('facet degenerate')
        ctr=p[ids].mean(axis=0); n=q[f]/np.linalg.norm(q[f])
        e=p[ids[0]]-ctr; e/=np.linalg.norm(e); u=np.cross(n,e)
        ph=np.arctan2((p[ids]-ctr)@u,(p[ids]-ctr)@e)
        ids=ids[np.argsort(ph)]
        faces.append(ids.tolist()); active.append(f)
    edges={}
    tris=[]
    for f,ids in enumerate(faces):
        for a,b in zip(ids,ids[1:]+ids[:1]):
            key=tuple(sorted((a,b))); edges.setdefault(key,[]).append(f)
        for j in range(1,len(ids)-1): tris.append([ids[0],ids[j],ids[j+1]])
    if any(len(owners)!=2 for owners in edges.values()): raise ValueError('bad edge multiplicity')
    e=np.array(sorted(edges),int)
    dual=np.array([edges[tuple(t)] for t in e],int)
    if len(p)-len(e)+len(faces)!=2: raise ValueError('Euler')
    return dict(triples=np.array(triples),faces=faces,active=np.array(active),triangles=np.array(tris),edges=e,dual_edges=dual)

def coords(q,top):
    p=np.linalg.solve(q[top['triples']],np.ones((len(top['triples']),3,1)))[...,0]
    a,b,c=np.moveaxis(p[top['triangles']],1,0)
    vol6=np.einsum('ij,ij->i',a,np.cross(b,c))
    c0=(vol6[:,None]*(a+b+c)).sum(0)/(4*vol6.sum())
    return p,c0,vol6.sum()/6

def tensor_geometry(q,top):
    p=torch.linalg.solve(q[torch.as_tensor(top['triples'])],torch.ones((len(top['triples']),3)))
    abc=p[torch.as_tensor(top['triangles'])]; a,b,c=abc.unbind(1)
    vol6=(a*torch.linalg.cross(b,c)).sum(1)
    centroid=(vol6[:,None]*(a+b+c)).sum(0)/(4*vol6.sum())
    x=p-centroid
    qa=q[torch.as_tensor(top['active'])]
    polar=qa/(1-(qa*centroid).sum(1))[:,None]
    return x,polar,centroid,vol6.sum()/6

def directed_cos(x,e):
    a=np.r_[e[:,0],e[:,1]];b=np.r_[e[:,1],e[:,0]]
    d=x[b]-x[a]
    z=np.einsum('ij,ij->i',x[a],d)/np.sqrt(np.einsum('ij,ij->i',x[a],x[a])*np.einsum('ij,ij->i',d,d))
    ans=np.full(len(x),-np.inf)
    np.maximum.at(ans,a,z)
    return ans

def census(q,top=None):
    if top is None:top=topology(q)
    p,c,v=coords(q,top); x=p-c
    qa=q[top['active']]; polar=qa/(1-qa@c)[:,None]
    mu=directed_cos(x,top['edges']);ms=directed_cos(polar,top['dual_edges'])
    return dict(V=len(p),E=len(top['edges']),F=len(qa),C=2*len(top['edges']),S=int((ms<-1e-9).sum()),U=int((mu<-1e-9).sum()),centroid=c.tolist(),volume=v,
                S_ids=np.where(ms<-1e-9)[0].tolist(),U_ids=np.where(mu<-1e-9)[0].tolist(),rootU=int(np.argmax(p[:,2])),rootS=int(np.argmin(qa[:,2])), minU=float(np.sort(mu)[1]),minS=float(np.sort(ms)[1]))

def complete_tree(x,root):
    """Maximum spanning tree of exact-formula (floating) chord minima; orient at root."""
    a=np.einsum('ij,ij->i',x,x);b=x@x.T
    d=a[:,None]+a[None,:]-2*b
    w=np.where(b>=a[:,None],a[:,None],np.where(b>=a[None,:],a[None,:],(a[:,None]*a[None,:]-b*b)/np.maximum(d,1e-300)))
    np.fill_diagonal(w,0)
    # positive constant offset keeps all off-diagonal nonzero for csgraph.
    graph=minimum_spanning_tree(-(w+1)*(1-np.eye(len(x)))).tocoo()
    adj=[[] for _ in x]
    for i,j in zip(graph.row,graph.col):adj[i].append(j);adj[j].append(i)
    parent=np.full(len(x),-1,int);parent[root]=root;queue=[root]
    for u in queue:
        for v in adj[u]:
            if parent[v]<0:parent[v]=u;queue.append(v)
    ids=np.array([i for i in range(len(x)) if i!=root]);return ids,parent[ids]

if __name__=='__main__':
    import json
    for k,s in enumerate(SEEDS):
        reps,b=dlv_reps(s);q=expand(reps,b)
        print(k,json.dumps(census(q),sort_keys=True))
        np.savez(f'D2_SEED{k}.npz',reps=reps,bottom=b)
```

## d2_rooted.py
```python
"""Rooted chord-minimum descent in both physical and polar reflection-exact hulls."""
from d2_core import *
from scipy.optimize import minimize
import json, sys, time

def chart(reps,bottom):
    # Positive x/y representative normal components and bottom; free z components.
    if np.min(abs(reps[:,:2]))<=0: raise ValueError('nonzero quadrant chart required')
    a=reps.copy();a[:,:2]=np.log(abs(a[:,:2]));return np.r_[a.ravel(),np.log(bottom)]
def unchart(t):
    a=t[:-1].reshape(-1,3);r=np.c_[np.exp(a[:,:2]),a[:,2]];return r,np.exp(t[-1])
def tensor_q(t):
    a=t[:-1].reshape(-1,3);r=torch.cat((torch.exp(a[:,:2]),a[:,2:]),dim=1)
    q=(r[:,None,:]*torch.as_tensor(SIGNS)[None,:,:]).reshape(-1,3)
    return torch.cat((q,torch.stack((t[-1]*0,t[-1]*0,-torch.exp(t[-1])))[None,:]))

def tree_loss(x,root,pairs):
    i,j=pairs;u=x[torch.as_tensor(i)];v=x[torch.as_tensor(j)]
    a=(u*u).sum(1);b=(u*v).sum(1);c=(v*v).sum(1);d=a+c-2*b
    interior=(a*c-b*b)/torch.clamp(d,min=1e-24)
    w=torch.where(b>=a,a,torch.where(b>=c,c,interior))
    # Sum of logarithmic downhill losses; zero exactly characterizes rooted ascent.
    gap=torch.clamp(torch.log(a/torch.clamp(w,min=1e-24)),min=0)
    # A small positive margin on root norm dominance is a guard, not a census.
    norm=(x*x).sum(1);rootgap=torch.relu(torch.log(norm/norm[root])+1e-5)
    return gap.sum()+.1*rootgap.sum(),gap

class Objective:
    def __init__(self,tag,report=100):self.tag=tag;self.calls=0;self.best=np.inf;self.report=report;self.history=[]
    def __call__(self,z):
        self.calls+=1
        try:
            r,b=unchart(z);q=expand(r,b);top=topology(q)
            p,c,vol=coords(q,top)
            # Require the designed BASE and upper cap to remain genuine carriers.
            if len(q)-1 not in top['active']:raise ValueError('BASE inactive')
            up=int(np.argmax(p[:,2]));sp=int(np.where(top['active']==len(q)-1)[0][0])
            if np.linalg.norm(p[up,:2])>1e-6:raise ValueError('top not axial')
            qa=q[top['active']];xx=p-c;pp=qa/(1-qa@c)[:,None]
            pt=complete_tree(xx,up);st=complete_tree(pp,sp)
            t=torch.tensor(z,requires_grad=True);tq=tensor_q(t)
            x,polar,centroid,volume=tensor_geometry(tq,top)
            u,ug=tree_loss(x,up,pt);s,sg=tree_loss(polar,sp,st)
            # Do not drive coordinate magnitudes without bound by scale invariance.
            loss=u+s+1e-8*(t*t).sum()
            loss.backward();val=float(loss.detach());grad=t.grad.detach().numpy()
            if not np.isfinite(val) or not np.all(np.isfinite(grad)):raise ValueError('nonfinite')
            if val<self.best:
                self.best=val
                cs=census(q,top);row=dict(call=self.calls,loss=val,lossU=float(u.detach()),lossS=float(s.detach()),**cs)
                self.history.append(row)
                np.savez(self.tag+'_best.npz',z=z,reps=r,bottom=b)
                with open(self.tag+'_history.json','w') as f:json.dump(self.history,f,sort_keys=True,indent=2)
            if self.calls%self.report==0:print(self.tag,self.calls,'best',self.best,'current',val,flush=True)
            return val,grad
        except (ValueError,RuntimeError,np.linalg.LinAlgError) as e:
            return 1e6+1e-2*float(z@z),.02*z

def run(seed,trial,maxiter):
    r,b=dlv_reps(SEEDS[seed]);r[:,0]*=SEEDS[seed][-1];r[:,1]/=SEEDS[seed][-1] # undo harmful seed anisotropy
    rng=np.random.default_rng(2026092310+100*seed+trial)
    z=chart(r,b)
    if trial: z+=rng.normal(0,.015 if trial<4 else .05,size=len(z))
    tag=f'D2_ROOTED_{seed}_{trial}'
    ob=Objective(tag)
    bounds=[(-4,4) if k%3!=2 else (-5,5) for k in range(len(z)-1)]+[(-2,2)]
    res=minimize(ob,z,jac=True,method='L-BFGS-B',bounds=bounds,options={'maxiter':maxiter,'maxls':25,'ftol':1e-13,'gtol':1e-8,'maxcor':20})
    print(tag,'DONE',res.message,'calls',ob.calls,'best',ob.best,flush=True)
    if ob.history:print(json.dumps(ob.history[-1],sort_keys=True),flush=True)

if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]) if len(sys.argv)>3 else 600)
```

## Literal final binary64 checkpoint
Decode the following JSON and write `json.dumps(data,sort_keys=True,indent=2)+'\n'` as D2_ROOTED_0_0_checkpoint.json. Expected 3243 bytes, SHA256 93c01ff905a739cddbbbf3d698af3e2c978d6c185600c2c35b537513768bd48d. All z, representatives and bottom values are present. The representative array is canonical for the geometry; z is the saved optimization chart. Reconstruct its numerical hull with expand/census. Nearest-even rounding of reps*10^6 and bottom*10^6 gives the exact D2_ROOTED_00_G6 input in part 2.

```json
{"z":[-0.03493897981622713,-3.350082028350629,-2.258315075892187,-2.6054565511331043,-3.9999866023110435,-1.7000599302907913,0.29448942004749423,-2.4239135322552605,-1.2730868439716965,-1.483808600795635,-1.3107757649406135,-1.4964602257202235,0.33821842523797113,-2.5925301358493225,-0.7704120371934552,-1.4946947949863858,-0.2026360628438508,-0.7653694514102192,0.28475787741406045,-3.9099721025186,-0.28729957746289797,-0.8775099941586998,-0.13888399799976364,-0.39162925533468207,0.1750891307055802,-2.012747082257736,-0.03846457262153499,-0.7675026079967855,-0.18589760593203009,-0.09399774134272186,0.04838006710238549,-1.6345104290276191,0.15239844844043623,-0.6355625881940542,-0.3301910921231963,0.16564744311499574,-0.11193287195917319,-1.2346044122686968,0.29555999874965294,-0.46555656112893035,-0.5569569198614407,0.34357973398182545,-0.297844825981615,-1.0790223093679956,0.40778074428032385,-1.0607075707224725,-0.786360335781911,0.43441794499311404,-0.6508744043805459,-1.6679808164899435,0.5455116467112677,-1.9404812907937745,-1.3397241819213157,0.5259622496264619,-0.5104581034999063,-1.1094676952745253,0.5013331884031165,1.112858939272084],"reps":[[0.9656643394752531,0.0350814763071772,-2.258315075892187],[0.07386940433750212,0.01831588427761087,-1.7000599302907913],[1.3424407603351305,0.0885742999037826,-1.2730868439716965],[0.22677235620113909,0.26961082061405023,-1.4964602257202235],[1.4024467997286516,0.07483046911377461,-0.7704120371934552],[0.22431705697444773,0.8165753694721094,-0.7653694514102192],[1.3294401016749453,0.020041060148988158,-0.28729957746289797],[0.4158170104762642,0.870328982505537,-0.39162925533468207],[1.1913523979601035,0.1336211018654042,-0.03846457262153499],[0.46417083854672836,0.83035861442552,-0.09399774134272186],[1.049569486361825,0.19504783768804704,0.15239844844043623],[0.529637436716248,0.7187863658946336,0.16564744311499574],[0.8941042749541802,0.29094983579099737,0.29555999874965294],[0.627785606873986,0.5729499462849311,0.34357973398182545],[0.7424165345669059,0.3399277073680518,0.40778074428032385],[0.3462107550492325,0.4554996476709833,0.43441794499311404],[0.5215894971624826,0.18862755501916792,0.5455116467112677],[0.14363480303082699,0.2619179003104962,0.5259622496264619],[0.6002205526859591,0.3297344335657666,0.5013331884031165]],"bottom":3.043045853356578}
```

## dlv_mass.py and smooth-centre evidence boundary
`OPENBLAS_NUM_THREADS=1 python dlv_mass.py > dlv_mass_roots.jsonl` gives 11 rows (2107 bytes, SHA256 38134e0657c0a878cac72de4d88f853d324920ff2281f4caeaa5055991697bed in this environment). The c roots for d=.005,.02,.05,.1,.2,.3,.4,.5,.6,.7,.8 are respectively .05563073885406672,.055628158380543635,.05561373231448819,.0555625489803858,.05536296598287449,.05504762956361696,.05463919228130625,.05416383349243764,.0536477074672635,.053114229745419135,.05258250549008054. Fine actual-centre residuals use384 z and512 quadrant-phi nodes, from1.55e-14 to3.9643e-12. This is numerical quadrature convergence, not a rigorous enclosure. The smooth DLV existence theorem only guarantees convexity for sufficiently small d on a suitable compact c interval; it does not certify all these d values, nor finite sampled polyhedra. The substantial mismatch between c near.055 and prior scout c near.21-.35 suggests starting from genuine smooth mass balance rather than assuming the old scouts approximate an origin-centred smooth110 body.

```python
"""Numerical smooth DLV mass balancing; not a convexity certificate."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np
from scipy.special import roots_legendre
from scipy.optimize import brentq

def rho(theta,phi,c):
 def F(x):return (c*x*x+(1-c)*(1-x)**2*c*x/(c+x))/(c*x+(1-c)*(1-x)**2)
 f=np.pi*F(theta/np.pi+.5)-np.pi/2;g=-np.pi*F(-theta/np.pi+.5)+np.pi/2
 a=(np.cos(phi)*np.cos(f))**2;b=(np.sin(phi)*np.cos(g))**2
 return (a*np.sin(f)+b*np.sin(g))/(a+b)

def mass(c,d,n=192,m=256):
 z,w=roots_legendre(n);phi=(np.arange(m)+.5)*np.pi/(2*m)
 r=1+d*rho(np.arcsin(z[:,None]),phi[None,:],c)
 volume=(2*np.pi/3)*np.mean(r**3,axis=1)@w
 moment=(2*np.pi/4)*np.mean(r**4,axis=1)@(w*z)
 return volume,moment,moment/volume

if __name__=='__main__':
 import json
 for d in [.005,.02,.05,.1,.2,.3,.4,.5,.6,.7,.8]:
  c=brentq(lambda c:mass(c,d)[1],.0001,.999,xtol=1e-13)
  print(json.dumps(dict(d=d,c=c,coarse=mass(c,d),fine=mass(c,d,384,512))),flush=True)
```
