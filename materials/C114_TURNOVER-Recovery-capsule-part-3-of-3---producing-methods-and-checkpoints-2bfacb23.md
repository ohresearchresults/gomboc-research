# material-2bfacb230259

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# C114_TURNOVER Recovery capsule part 3 of 3

This completes the same three-part object capsule. Part1 is [internal-source-reference] (exact_turnover.py, 11252 bytes, SHA256 c9ef4681d976faa810ea3e27631a5ad686ac904fb18ba2bd8a38e5435ad36f1d). Part2 is [internal-source-reference] (replay_turnover.py, 5781 bytes, SHA256 3681a5d342895f7a2c5c199b573f39f912cae9b6cdfb11d167de0b29d818a7b2). Save those literal texts as the indicated .py filenames. `python -B -S replay_turnover.py OUTPUT_DIRECTORY` reconstructs all four exact inputs, all four complete rational audits and exact comparisons without NumPy/SciPy/Torch. The eight output byte counts and SHA256 values are literal in part2. Its four expected terminal markers are TURNOVER_EXACT_TETRA446_PRISM446_WEAK123_CONTROLS_PASS; C114_TURNOVER_THREE_EXACT_OWN211_NO_WEAK_FREEZES_PASS; C114_TURNOVER_EIGHT_SOURCE_ONLY_OUTPUT_HASHES_PASS; C114_TURNOVER_GLOBAL_POLAR_TQ_RATIO_BELOW_0_42_PASS. Fresh source-only replay passed all four. These are non-record own211/weak000 bodies, NOT own110. Incumbent own110 C622 is unchanged.

The four complete numerical producing sources below preserve how finite physical root0->20 turnover was discovered and repaired. Sources have all helpers. Observed environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu. CPU/BLAS/Torch threads1. All non-default optimizer parameters are in code and commands. No numerical optimizer is part of the definition or exact reconstruction of the final bodies; part2 fixes all63 endpoint binary64 coordinates by exact hex strings and Fraction-based ties-to-even grid freezing. Numerical runs may depend on platform/library defaults; they are not exact exclusions or proofs of a continuous path.

Extract each complete fenced source to its heading filename, preserving its final newline. Source receipts: kernel_search.py 6448 bytes SHA256 4754f774883b332eca02bfa72d41d4869101e827353e524e9039f6ee29eb13cc; replace_search.py3291 bytes d234dddc97fd3cbb6a160e7e40a0c0500a12fd24da98014261f16bfc274770a9; turnover_repair.py5303 bytes 5deeeeb7dec3f8fd3c6eaebcfe84cd8ac795374a7de7863c6e9a9da8f7ca30e3; cancel_minor.py1036 bytes 3ff32305c154598889138e1972b7a1084056d65b28bf50df0b482df7e0cd29b7. If this complete material is saved as METHODS.md, extraction command: `python -c "import re,pathlib; t=pathlib.Path('METHODS.md').read_text(); [(pathlib.Path(n).write_text(s+'\n')) for n,s in re.findall(r'## File: ([^\n]+)\n```python\n(.*?)\n```',t,re.S)]"`.

Run commands, in the source directory: `python kernel_search.py SEGMENT_W30 2 30 1.25 60 8 520921`; `python replace_search.py APEX_W300 0 300 2 60 8 520922`; `python turnover_repair.py`; `python cancel_minor.py`. Segment scouting visited1464 shapes,0 rejects,no U1/no S1; best numerical S9/U26, TP about0.2790236,TQ about7.767909. Apex replacement visited1724 shapes,0rejects; best S3/U15,TP about0.011394581873246722,TQ about24.85146834438059. Only U1 visit was unchanged parent. Best apex displacement was [0.8247902896302414,-0.11665843533918274,0.48418916254818867]. These negative finite samples are not exclusions of all Minkowski sums or apex changes.

Physical repair moves all63 coordinates and the actual filled centroid, rebuilding hull/elder data each call. It selects new farthest input20, gamma0.003, alpha stages1e4/1e6/1e8,220 L-BFGS-B iterations each; observed343/363/328 evaluations. This reached numerical S3/U1 with TQ around14.45. Minor cancellation starts from the last stage's BEST checkpoint, not necessarily its terminal iterate; root20,gamma0.002,alpha1e6,two_roots mode,400iterations,2017evaluations. It reached S2/U1. Again final grid freezes use MINOR_CANCEL bestx, NOT necessarily result_x. Both state distinction and exact selected endpoint are preserved.

Pinned stage inputs can be recreated by `python pinned_inputs.py`: it writes the exact apex seed required by turnover_repair.py and the exact 63-coordinate pre-minor checkpoint consumed by cancel_minor.py, independent of rerunning optimizers. For independent minor-stage continuation run pinned_inputs.py then cancel_minor.py (without overwriting its TURNOVER_REPAIR.json by a new optimization). For full repair rerun pinned_inputs.py then turnover_repair.py then cancel_minor.py. To obtain exactly the preserved final bodies, use the standard-library replay in part2, not a claim of bitwise optimizer determinism. Exact audits use one full mechanical implementation plus independent boundary-volume/first-moment formulas, not two independent full mechanical implementations.

## File: kernel_search.py
```python
"""C114 physical Minkowski-kernel scouting. Full filled centroid and both elder forests.
Numerical exploration only; exact endpoint auditing is separate.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'): os.environ[k]='1'
import json, sys, hashlib, platform, time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull, QhullError
from scipy.optimize import differential_evolution
BASE=np.array([[-13513,10001,-9032],[7585,971,-5336],[9215,2535,-2766],[9859,3065,-261],[10414,1455,1511],[10533,-561,2627],[10245,-2747,3309],[9489,-4870,3884],[8292,-6612,4622],[6777,-7643,5870],[4984,-8225,7187],[2841,-8790,8032],[556,-8903,8725],[-1868,-8784,9006],[-4342,-8346,8933],[-6808,-7570,8472],[-9197,-6461,7561],[-11427,-4979,6139],[-13362,-2964,4209],[-14798,-281,1613],[-15515,3415,-2186]],dtype=np.int64)
def source_points(): return BASE/10000.
def body(kernel):
    return np.unique((source_points()[:,None,:]+np.asarray(kernel)[None,:,:]).reshape(-1,3),axis=0)
def geom(v):
    hull=ConvexHull(v)
    simp=hull.simplices.copy(); a,b,c=np.moveaxis(v[simp],1,0)
    sg=np.einsum('ij,ij->i',np.cross(b-a,c-a),hull.equations[:,:3])<0
    simp[sg]=simp[sg][:,[0,2,1]]
    anchor=v[hull.vertices].mean(axis=0)
    a,b,c=np.moveaxis(v[simp]-anchor,1,0)
    d=np.einsum('ij,ij->i',a,np.cross(b,c)); vol=d.sum()/6
    centroid=anchor+np.einsum('i,ij->j',d,a+b+c)/(4*d.sum())
    w=v-centroid
    # Normalized supporting equations; merge Qhull's coplanar subdivisions.
    groups={}
    for it, eq in enumerate(hull.equations):
        key=tuple(np.round(eq,9))
        groups.setdefault(key,[]).append(it)
    faces=[]; pe={}; q=[]
    for inds in groups.values():
        ei={}
        for t in simp[inds]:
            for j in range(3):
                ed=tuple(sorted((int(t[j]),int(t[(j+1)%3])))); ei[ed]=ei.get(ed,0)+1
        boundary=[e for e,k in ei.items() if k==1]
        fi=len(faces); fs=sorted(set(i for e in boundary for i in e)); faces.append(fs)
        for e in boundary: pe.setdefault(e,[]).append(fi)
        eq=hull.equations[inds[0]]; height=-(eq[3]+eq[:3]@centroid)
        if height<=0: raise ValueError('nonpositive centered height')
        q.append(eq[:3]/height)
    assert all(len(ff)==2 for ff in pe.values())
    used=sorted(hull.vertices.tolist()); remap={p:i for i,p in enumerate(used)}
    edges=np.array([(remap[a],remap[b]) for a,b in pe],dtype=int)
    qe=np.array([ff for ff in pe.values()],dtype=int)
    assert len(used)-len(pe)+len(faces)==2
    return dict(p=w[used],q=np.array(q),edges=edges,qedges=qe,volume=vol,centroid=centroid,
                V=len(used),E=len(pe),F=len(faces),input_indices=used,faces=faces)
def bars(p,edges):
    r=np.einsum('ij,ij->i',p,p); n=len(p)
    a,b=p[edges[:,0]],p[edges[:,1]]; d=b-a
    den=np.einsum('ij,ij->i',d,d)
    t=np.clip(-np.einsum('ij,ij->i',a,d)/den,0,1)
    x=a+t[:,None]*d; lev=np.einsum('ij,ij->i',x,x)
    par=list(range(n)); birth=list(range(n)); out=[]
    def root(i):
        while par[i]!=i: par[i]=par[par[i]]; i=par[i]
        return i
    for k in np.argsort(-lev,kind='stable'):
        i,j=map(int,edges[k]); u,z=root(i),root(j)
        if u==z: continue
        if (r[birth[u]],-birth[u]) < (r[birth[z]],-birth[z]): u,z=z,u
        delta=r[birth[z]]-lev[k]
        if delta>1e-12*max(r): out.append((birth[z],birth[u],int(k),float(delta)))
        par[z]=u
    return out

def diagnose(v):
    g=geom(v); pb=bars(g['p'],g['edges']); qb=bars(g['q'],g['qedges'])
    def unstable(p):
        vals=p@p.T-np.sum(p*p,axis=1)[:,None]
        np.fill_diagonal(vals,-np.inf)
        return np.flatnonzero(vals.max(axis=1)<0).tolist()
    ui=unstable(g['p']); si=unstable(g['q'])
    factor=g['volume']**(2/3)
    tp=sum(x[3] for x in pb)/factor; tq=sum(x[3] for x in qb)*factor
    return dict(V=g['V'],E=g['E'],F=g['F'],S=len(si),U=len(ui),S_labels=si,U_labels=ui,
                TP=tp,TQ=tq,Pbars=pb,Qbars=qb,volume=g['volume'],centroid=g['centroid'].tolist())

class Objective:
    def __init__(self,nk,weight):
        self.nk=nk; self.weight=weight; self.evals=0; self.rejects=0; self.best=1e100
        self.table={}; self.bestx=None; self.bestdiag=None; self.bestu1=None; self.bests1=None
    def __call__(self,x):
        self.evals+=1
        try:
            kernel=np.vstack((np.zeros(3),np.array(x).reshape(-1,3)))
            d=diagnose(body(kernel)); key=str((d['S'],d['U'])); self.table[key]=self.table.get(key,0)+1
            # Complete positive elder bars, not a local-escape surrogate.
            val=d['TQ']+self.weight*d['TP']
            if d['E']>310: val+=1e4*(d['E']-310)
            if val<self.best: self.best=val;self.bestx=x.tolist();self.bestdiag=d
            if d['U']==1 and (self.bestu1 is None or d['TQ']<self.bestu1['diagnosis']['TQ']):
                self.bestu1={'x':x.tolist(),'diagnosis':d}
            if d['S']==1 and (self.bests1 is None or d['TP']<self.bests1['diagnosis']['TP']):
                self.bests1={'x':x.tolist(),'diagnosis':d}
            return val
        except (QhullError,ValueError,AssertionError,FloatingPointError):
            self.rejects+=1;return 1e8

def run(label,nk,weight,bound,maxiter,popsize,seed):
    ob=Objective(nk,weight); settings=dict(label=label,nk=nk,weight=weight,bound=bound,maxiter=maxiter,popsize=popsize,seed=seed,polish=False,workers=1,updating='immediate',tol=0,atol=0)
    t=time.time(); res=differential_evolution(ob,[(-bound,bound)]*(3*(nk-1)),maxiter=maxiter,popsize=popsize,seed=seed,polish=False,workers=1,updating='immediate',tol=0,atol=0)
    out=dict(settings=settings,evaluations=ob.evals,rejects=ob.rejects,census_table=ob.table,best=ob.best,bestx=ob.bestx,bestdiag=ob.bestdiag,bestu1=ob.bestu1,bests1=ob.bests1,
             final_x=res.x.tolist(),final_fun=float(res.fun),message=str(res.message),iterations=int(res.nit),elapsed_seconds=time.time()-t,
             versions={'python':platform.python_version(),'numpy':np.__version__,'scipy':__import__('scipy').__version__})
    Path(label+'.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    print(label,ob.evals,'best',ob.bestdiag,'u1',ob.bestu1,'s1',ob.bests1,flush=True)
if __name__=='__main__':
    if len(sys.argv)==1: print(json.dumps(diagnose(source_points()),indent=2))
    else: run(sys.argv[1],int(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]))
```

## File: replace_search.py
```python
"""Finite root/interface turnover on C114: physical controls move, no fixed center/root."""
from kernel_search import *
from scipy.optimize import minimize

class Replacement(Objective):
    def __init__(self, controls, weight, reserve_weight=300):
        super().__init__(len(controls),weight); self.controls=controls; self.reserve_weight=reserve_weight
    def __call__(self,x):
        self.evals+=1
        try:
            v=source_points(); v[self.controls]+=np.array(x).reshape(-1,3)
            d=diagnose(v);g=geom(v);r=np.linalg.norm(g['p'],axis=1).max()
            rin=1/np.linalg.norm(g['q'],axis=1).max()
            es=np.linalg.norm(g['p'][g['edges'][:,0]]-g['p'][g['edges'][:,1]],axis=1).min()/r
            vr=d['volume']/r**3
            penalty=self.reserve_weight*(max(0,.035-rin/r)**2+max(0,.035-es)**2+max(0,.06-vr)**2)
            d.update(inradius_ratio=rin/r,minedge_ratio=es,volume_ratio=vr,reserve_penalty=penalty)
            key=str((d['S'],d['U']));self.table[key]=self.table.get(key,0)+1
            val=d['TQ']+self.weight*d['TP']+penalty
            if val<self.best: self.best=val;self.bestx=x.tolist();self.bestdiag=d
            if d['U']==1 and penalty==0 and (self.bestu1 is None or d['TQ']<self.bestu1['diagnosis']['TQ']):self.bestu1={'x':x.tolist(),'diagnosis':d}
            if d['S']==1 and penalty==0 and (self.bests1 is None or d['TP']<self.bests1['diagnosis']['TP']):self.bests1={'x':x.tolist(),'diagnosis':d}
            return val
        except (QhullError,ValueError,AssertionError,FloatingPointError):
            self.rejects+=1;return 1e8

def replace(label,controls,weight,bound,niter,popsize,seed):
    o=Replacement(controls,weight);nv=3*len(controls);bounds=[(-bound,bound)]*nv
    o(np.zeros(nv)); settings=dict(controls=controls,weight=weight,bound=bound,maxiter=niter,popsize=popsize,seed=seed,
                                polish=False,workers=1,updating='immediate',tol=0,atol=0,x0=[0.]*nv,reserve_weight=300)
    t=time.time();res=differential_evolution(o,bounds,maxiter=niter,popsize=popsize,seed=seed,polish=False,workers=1,updating='immediate',tol=0,atol=0,x0=np.zeros(nv))
    de=dict(x=res.x.tolist(),fun=float(res.fun),nit=int(res.nit),nfev=int(res.nfev),message=str(res.message))
    r=minimize(o,np.array(o.bestx),method='Nelder-Mead',bounds=bounds,options=dict(maxiter=400,xatol=1e-9,fatol=1e-9,adaptive=True))
    out=dict(settings=settings,evaluations=o.evals,rejects=o.rejects,census_table=o.table,best=o.best,bestx=o.bestx,bestdiag=o.bestdiag,bestu1=o.bestu1,bests1=o.bests1,de=de,
             polish=dict(method='Nelder-Mead',maxiter=400,xatol=1e-9,fatol=1e-9,adaptive=True,x=r.x.tolist(),fun=float(r.fun),nit=int(r.nit),nfev=int(r.nfev),message=str(r.message)),
             elapsed_seconds=time.time()-t,versions={'python':platform.python_version(),'numpy':np.__version__,'scipy':__import__('scipy').__version__})
    Path(label+'.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    for k in ('bestdiag','bestu1','bests1'): print(label,k,out[k],flush=True)
    print('evals',o.evals,'rejects',o.rejects)
if __name__=='__main__':replace(sys.argv[1],[int(x) for x in sys.argv[2].split(',')],float(sys.argv[3]),float(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]))
```

## File: turnover_repair.py
```python
"""C114 finite apex turnover followed by coupled all-coordinate physical repair.
Differentiates the actual filled centroid; hull and elder combinatorics rebuilt every call.
"""
from kernel_search import *
from scipy.optimize import minimize
import torch
torch.set_num_threads(1); torch.set_default_dtype(torch.float64)
class Repair:
    def __init__(self,root,gamma,alpha,mode="full"):
        self.mode=mode;self.root=root;self.gamma=gamma;self.alpha=alpha;self.evals=0;self.table={};self.bestu1=None;self.best=1e100;self.bestx=None;self.bestdiag=None
    def value_grad(self,x):
        self.evals+=1;v=np.asarray(x).reshape(-1,3)
        try:
            g=geom(v); d=diagnose(v); self.table[str((d['S'],d['U']))]=self.table.get(str((d['S'],d['U'])),0)+1
            if d['U']==1 and (self.bestu1 is None or d['TQ']<self.bestu1['diagnosis']['TQ']): self.bestu1={'points':v.tolist(),'diagnosis':d}
            h=ConvexHull(v);t=h.simplices.copy();a,b,c=np.moveaxis(v[t],1,0)
            rev=np.einsum('ij,ij->i',np.cross(b-a,c-a),h.equations[:,:3])<0;t[rev]=t[rev][:,[0,2,1]]
            vt=torch.tensor(v,requires_grad=True);tt=torch.tensor(t)
            a,b,c=vt[tt[:,0]],vt[tt[:,1]],vt[tt[:,2]]
            det=(a*torch.linalg.cross(b,c)).sum(1);vol=det.sum()/6
            center=(det[:,None]*(a+b+c)).sum(0)/(4*det.sum());p=vt-center
            fs=torch.tensor([ff[:3] for ff in g['faces']]);aa,bb,cc=vt[fs[:,0]],vt[fs[:,1]],vt[fs[:,2]]
            nn=torch.linalg.cross(bb-aa,cc-aa);hh=(nn*(aa-center)).sum(1);q=nn/hh[:,None]
            diff=p[None,:,:]-p[:,None,:];den=torch.linalg.vector_norm(p,dim=1)[:,None]*torch.linalg.vector_norm(diff,dim=2)
            cos=(p[:,None,:]*diff).sum(2)/(den+torch.eye(len(v)))
            cos=cos-10*torch.eye(len(v));best=cos.max(dim=1).values
            keep=torch.arange(len(v))!=self.root
            esc=torch.relu(self.gamma-best[keep]);physical=(esc*esc).sum()
            qb=bars(g['q'],g['qedges']);qloss=torch.tensor(0.)
            for peak,elder,ei,delta in qb:
                i,j=g['qedges'][ei];qa=q[i];qd=q[j]-qa
                tmin=torch.clamp(-(qa*qd).sum()/(qd*qd).sum(),0,1)
                qz=qa+tmin*qd
                qloss=qloss+(q[peak]*q[peak]).sum()-(qz*qz).sum()
            qloss=qloss*vol**(2/3)
            if self.mode=="two_roots":
                roots={int(np.argmax(np.sum(g['q']**2,axis=1)))}
                if qb: roots.add(max(qb,key=lambda row:row[3])[0])
                qdiff=q[None,:,:]-q[:,None,:]
                qden=torch.linalg.vector_norm(q,dim=1)[:,None]*torch.linalg.vector_norm(qdiff,dim=2)
                qcos=(q[:,None,:]*qdiff).sum(2)/(qden+torch.eye(len(q)))-10*torch.eye(len(q))
                qkeep=torch.tensor([i not in roots for i in range(len(q))])
                qesc=torch.relu(.0002-qcos.max(dim=1).values[qkeep])
                qloss=.001*qloss+1e6*(qesc*qesc).sum()
            radius=torch.linalg.vector_norm(p,dim=1).max();inner=1/torch.linalg.vector_norm(q,dim=1).max()
            pe=torch.tensor(g['edges']);ep=p[torch.tensor(g['input_indices'])]
            emin=torch.linalg.vector_norm(ep[pe[:,0]]-ep[pe[:,1]],dim=1).min()/radius
            guards=1e4*(torch.relu(.03-inner/radius)**2+torch.relu(.035-emin)**2+torch.relu(.06-vol/radius**3)**2)
            loss=qloss+self.alpha*physical+guards
            z=float(loss.detach());loss.backward();grad=vt.grad.detach().numpy().reshape(-1)
            if z<self.best:self.best=z;self.bestx=x.tolist();self.bestdiag=d
            return z,grad
        except (QhullError,ValueError,AssertionError,FloatingPointError): return 1e10,np.zeros_like(x)

def run():
    z=json.loads(Path('APEX_W300.json').read_text());v=source_points();v[0]+=np.array(z['bestx'])
    root=int(np.argmax(np.linalg.norm(v-np.array(diagnose(v)['centroid']),axis=1)))
    settings={'root':root,'gamma':.003,'alphas':[10000,1000000,100000000],'maxiter':220,'ftol':1e-13,'gtol':1e-10,'maxls':40,'maxfun':30000,'bounds':None}
    initial=v.copy();history=[];bestu=None;x=v.reshape(-1)
    for alpha in settings['alphas']:
        ob=Repair(root,settings['gamma'],alpha);t=time.time()
        res=minimize(ob.value_grad,x,jac=True,method='L-BFGS-B',options={k:settings[k] for k in ['maxiter','ftol','gtol','maxls','maxfun']})
        rec={'alpha':alpha,'evals':ob.evals,'table':ob.table,'best':ob.best,'bestx':ob.bestx,'bestdiag':ob.bestdiag,'bestu1':ob.bestu1,'result_x':res.x.tolist(),'nit':int(res.nit),'nfev':int(res.nfev),'message':str(res.message),'elapsed_seconds':time.time()-t}
        history.append(rec);x=res.x.copy()
        if ob.bestu1 is not None and (bestu is None or ob.bestu1['diagnosis']['TQ']<bestu['diagnosis']['TQ']):bestu=ob.bestu1
        print('alpha',alpha,'iters',res.nit,'evals',ob.evals,'bestclass',ob.bestdiag['S'],ob.bestdiag['U'],'TQ',ob.bestdiag['TQ'],'u1',None if ob.bestu1 is None else {k:ob.bestu1['diagnosis'][k] for k in ['V','E','F','S','U','TP','TQ']},flush=True)
        Path('TURNOVER_REPAIR.json').write_text(json.dumps({'settings':settings,'initial':initial.tolist(),'history':history,'bestu1':bestu,'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':__import__('scipy').__version__,'torch':torch.__version__}},sort_keys=True,separators=(',',':'))+'\n')
if __name__=='__main__':run()
```

## File: cancel_minor.py
```python
from turnover_repair import *
def run_cancel():
    parent=json.loads(Path('TURNOVER_REPAIR.json').read_text());x=np.array(parent['history'][-1]['bestx'])
    settings={'root':20,'gamma':.002,'alpha':1000000,'mode':'two_roots','maxiter':400,'ftol':1e-16,'gtol':1e-12,'maxls':40,'maxfun':50000,'bounds':None}
    ob=Repair(settings['root'],settings['gamma'],settings['alpha'],settings['mode']);t=time.time()
    r=minimize(ob.value_grad,x,jac=True,method='L-BFGS-B',options={k:settings[k] for k in ['maxiter','ftol','gtol','maxls','maxfun']})
    out=dict(settings=settings,initial=x.tolist(),best=ob.best,bestx=ob.bestx,bestdiag=ob.bestdiag,bestu1=ob.bestu1,table=ob.table,evals=ob.evals,elapsed_seconds=time.time()-t,
             result_x=r.x.tolist(),message=str(r.message),nit=int(r.nit),nfev=int(r.nfev))
    Path('MINOR_CANCEL.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    print('evals',ob.evals,'nit',r.nit,'message',r.message,'best',ob.bestdiag,flush=True)
if __name__=='__main__':run_cancel()
```

## File: pinned_inputs.py
```python
import json
from pathlib import Path
APEX_DELTA=[0.8247902896302414,-0.11665843533918274,0.48418916254818867]
MINOR_INITIAL_HEX=['-0x1.f5b4785474b6dp-2', '0x1.df558b96057adp-1', '-0x1.e202eb0aa726ep-2', '0x1.49bf01075ee45p-1', '-0x1.b8c4a542e0cfap-9', '-0x1.0e927adbbf578p-1', '0x1.b00419df84bb1p-1', '0x1.03d84cde920e2p-2', '-0x1.36de32d662277p-2', '0x1.e1cb9eb0928e5p-1', '0x1.3decbaad9a108p-2', '-0x1.103465e93e94fp-5', '0x1.01e47c0976c79p+0', '0x1.6f0522490757bp-3', '0x1.62d51fcec43b0p-3', '0x1.0c1e1919bc5f5p+0', '-0x1.cc7f5b4f88d10p-5', '0x1.ee8240070835cp-3', '0x1.08f0861f0a41ep+0', '-0x1.2b29ca79f782ep-2', '0x1.15265e4049da4p-2', '0x1.ec6aa3ca96bb6p-1', '-0x1.ebbf46c4344fep-2', '0x1.88f8e2191dc78p-2', '0x1.b1c631361732bp-1', '-0x1.4394a6631a892p-1', '0x1.0224a57b00947p-1', '0x1.6784974969a9ap-1', '-0x1.71fa112ea8930p-1', '0x1.4d879369cd167p-1', '0x1.0a8cc93f08e9ap-1', '-0x1.98d9b45417ac7p-1', '0x1.8bd7e7e476ba8p-1', '0x1.3a92b1d1c9dfep-2', '-0x1.bb62520452348p-1', '0x1.b46475eac1a90p-1', '0x1.282f746caabc7p-4', '-0x1.cd3e2e265433fp-1', '0x1.ce958137fac6cp-1', '-0x1.644e1cb225d45p-3', '-0x1.d20414317a8fbp-1', '0x1.d345a51b3ed88p-1', '-0x1.b64ae6ea8769cp-2', '-0x1.c6b18b7b8850cp-1', '0x1.c397c9364c976p-1', '-0x1.5c06476f94b6ap-1', '-0x1.a4e6ad3c6daeap-1', '0x1.a35c913027b11p-1', '-0x1.d7fd3728369c6p-1', '-0x1.6aa54dfbdbef4p-1', '0x1.71502c1696bd7p-1', '-0x1.247f88dbef63ep+0', '-0x1.16f6f946a80f8p-1', '0x1.2aad9a1b4aaafp-1', '-0x1.52f28f66c7107p+0', '-0x1.48f0e18f92a40p-2', '0x1.a65a4f43ccb81p-2', '-0x1.744fb8526cf8cp+0', '-0x1.6620d15d575c9p-6', '0x1.783f63d7b1b7bp-3', '-0x1.7e96bb4be20eep+0', '0x1.15eb8390c184bp-1', '-0x1.e3b0e6d8ec8c2p-3']
assert len(MINOR_INITIAL_HEX)==63
Path('APEX_W300.json').write_text(json.dumps({'bestx':APEX_DELTA},separators=(',',':'))+'\n')
Path('TURNOVER_REPAIR.json').write_text(json.dumps({'history':[{'bestx':[float.fromhex(h) for h in MINOR_INITIAL_HEX]}]},separators=(',',':'))+'\n')
print('C114_TURNOVER_PINNED_STAGE_INPUTS_READY')
```
