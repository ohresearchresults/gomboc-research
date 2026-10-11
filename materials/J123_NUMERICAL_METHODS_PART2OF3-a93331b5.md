# material-a93331b5509c

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J123 numerical methods — Recovery capsule part 2/3

Same object identity and environment as part1, [internal-source-reference]. These five complete units require geometry123.py, jointwide123.py and safecap123.py from that part. Part3 contains literal binary64 checkpoints and the remaining failed controls. The independent exact-recovery PACKAGE (not an independent auditor implementation) is [internal-source-reference].

The fan bundle samples topology at scales1,.1,.01,.001 of each proposed step and differentiates the alternate boundary mass polynomial at the CURRENT coordinates. Reusing current P guard constants for all alternate charts is a heuristic model, NOT a simultaneous exact feasibility theorem. Every accepted finite shape instead recomputes its actual hull, true homogeneous mass and all positive physical-tree guards. Requiring every sampled chart at once can itself overrestrict the model; its failure does not exclude an actual sign-conditioned chart escape. bufferedcap adds1e-4 to the model P threshold while retaining actual tauP=1e-6. barflow substitutes max(Q)+weight*sum(Q), including all merge events, for angular capacity. fullbarflow also samples neighboring Q topology. surgery tries deterministic finite deletion and stellar families with actual mass and whole-Q ranking; surviving proposals are not presumed own110.

Observed trajectory in part1: bufferedD is numerical S3/U1; barE lowers its main Q to~.4505521 but reaches S9/U1; fullF reaches S10/U1 with mainQ~.4423292. The latter G8 exact endpoint is indeed own(10,1,9),not211. surgery's best finite point adds one vertex over triangle[31,2,13], equal barycentric weights and height.001. starH then has39 submitted points, numericalV39/E111/F74, S16/U1,P[],15 positive Q with largest~.410193858. starH is a floating checkpoint, not an exact audited body in this package. Its100 accepted steps ended at the requested limit, not a proved obstruction. Forty-six additional arbitrary material points remain under the sufficient N85 budget.

Source byte identities:
bundlecap123.py 3639 1ef36c9b5407f532305472ed205845467b1e257ad50ef2ff6c14093bab209daf
bufferedcap123.py 3675 1c28fffaccc713a6b1a41d03fd28963c0523e949bc1386a8a62564aa9e5b622f
barflow123.py 6280 9b296e1bbd5414f724322b4632cadd67137398dec9ae838baa25186517c6938c
fullbarflow123.py 6936 85bea7c1bee67fd1761348c3fb42f66ac2424c910c368bb147ab599abeac4a69
surgery123.py 2217 aeec8cab35103cdd54322909c6a6badd06d20d2f2d2b0aeefc6cd278822546b9

## bundlecap123.py
```python
"""Finite-hull safeguarded capacity continuation with neighboring mass-fan guards.
Same scope as safecap123, with extra P Jacobian rows sampled on actual adjacent
fans. The sampled shape is used ONLY to choose its oriented boundary; the
alternative integration polynomial is differentiated at the CURRENT shape.
"""
from __future__ import annotations
import json,sys,time
from pathlib import Path
import numpy as np,torch
from scipy.optimize import minimize
from safecap123 import values
from geometry123 import load_points,triangulate,live_values,reference_tree_guards,stats

def alternate_jac(x,ids,pr,pp,sample):
 tr,fa,_,_=triangulate(sample);base=torch.tensor(x);z=base[ids].reshape(-1).detach().requires_grad_()
 def f(t):
  xx=base.index_copy(0,torch.tensor(ids),t.reshape(-1,3));v,g,p,q=live_values(xx,tr,fa)
  return reference_tree_guards(p,pr,pp)
 return torch.autograd.functional.jacobian(f,z,vectorize=True).detach().numpy()

def run(inp,prefix,steps,trust,taup,ridge):
 x=load_points(inp);v0=values(x)['volume'];trace=[];frames=[];begin=time.monotonic();rejected=0
 for it in range(steps):
  a=values(x,True);m=len(a['p']);k=len(a['q']);J=a['jac'];n=J.shape[1];cap=a['capacity']
  A=np.zeros((m+k+1,n+1));A[:,:n]=J;A[m:m+k,n]=-1;b=np.r_[a['p']-taup,a['q']-cap,a['volume']-.05*v0]
  signatures={tuple(sorted(tuple(sorted(map(int,t))) for t in triangulate(x)[0]))};solves=[]
  for bi in range(8):
   sub=minimize(lambda y:(.5*ridge*(y[:-1]@y[:-1])-y[-1],np.r_[ridge*y[:-1],-1.]),np.zeros(n+1),jac=True,method='SLSQP',constraints=[{'type':'ineq','fun':lambda y:A@y+b,'jac':lambda y:A}],bounds=[(-trust,trust)]*n+[(-.01,.05)],options={'ftol':1e-12,'maxiter':200})
   d=sub.x[:-1].reshape(-1,3);new=0
   for alpha in [1,.1,.01,.001]:
    sample=x.copy();sample[a['ids']]+=alpha*d
    try:tr=triangulate(sample)[0]
    except Exception:continue
    sig=tuple(sorted(tuple(sorted(map(int,t))) for t in tr))
    if sig in signatures:continue
    signatures.add(sig);pj=alternate_jac(x,a['ids'],a['rootP'],a['parentsP'],sample)
    more=np.zeros((m,n+1));more[:,:n]=pj;A=np.vstack([A,more]);b=np.r_[b,a['p']-taup];new+=1
   solves.append({'status':int(sub.status),'gain':float(sub.x[-1]),'added_fans':new})
   if not new:break
  ok=False;gain=float(sub.x[-1])
  for ls in range(25):
   al=2.**(-ls);xx=x.copy();xx[a['ids']]+=al*d
   try:aa=values(xx)
   except Exception:rejected+=1;continue
   if min(aa['p'])>=taup-1e-11 and aa['volume']>=.05*v0 and aa['capacity']>cap+max(1e-11,1e-4*al*max(gain,0)):
    ok=True;break
   rejected+=1
  row={'iteration':it,'capacity':cap,'new_capacity':aa['capacity'] if ok else None,'minP':float(min(a['p'])),'accepted':ok,'alpha':al,'fans':len(signatures),'solves':solves}
  trace.append(row)
  if ok:x=xx;frames.append(x.tolist())
  if it%10==0 or not ok:print(json.dumps(row),flush=True)
  if not ok or aa['capacity']>0:break
 out={'points':x.tolist(),'input':str(inp),'parameters':{'steps':steps,'trust':trust,'tauP':taup,'ridge':ridge,'line_search_steps':25,'bundle_passes':8,'fan_sample_scales':[1,.1,.01,.001],'qp_maxiter':200,'qp_ftol':1e-12,'volume_floor_fraction':.05},'trace':trace,'frames':frames,'rejected':rejected,'seconds':time.monotonic()-begin,'stats':stats(x)}
 Path(prefix+'.json').write_text(json.dumps(out,indent=2)+'\n');s=out['stats'];print(json.dumps({'accepted':len(frames),'Q':[v['depth'] for v in s['Q']],'P':[v['depth'] for v in s['P']],'SU':[len(s['S']),len(s['U'])],'VEF':[s[z] for z in ['V','E','F']],'seconds':out['seconds']}),flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]))
```

## bufferedcap123.py
```python
"""Finite-hull safeguarded capacity continuation with neighboring mass-fan guards.
Same scope as safecap123, with extra P Jacobian rows sampled on actual adjacent
fans. The sampled shape is used ONLY to choose its oriented boundary; the
alternative integration polynomial is differentiated at the CURRENT shape.
"""
from __future__ import annotations
import json,sys,time
from pathlib import Path
import numpy as np,torch
from scipy.optimize import minimize
from safecap123 import values
from geometry123 import load_points,triangulate,live_values,reference_tree_guards,stats

def alternate_jac(x,ids,pr,pp,sample):
 tr,fa,_,_=triangulate(sample);base=torch.tensor(x);z=base[ids].reshape(-1).detach().requires_grad_()
 def f(t):
  xx=base.index_copy(0,torch.tensor(ids),t.reshape(-1,3));v,g,p,q=live_values(xx,tr,fa)
  return reference_tree_guards(p,pr,pp)
 return torch.autograd.functional.jacobian(f,z,vectorize=True).detach().numpy()

def run(inp,prefix,steps,trust,taup,ridge):
 x=load_points(inp);v0=values(x)['volume'];trace=[];frames=[];begin=time.monotonic();rejected=0
 for it in range(steps):
  a=values(x,True);m=len(a['p']);k=len(a['q']);J=a['jac'];n=J.shape[1];cap=a['capacity']
  A=np.zeros((m+k+1,n+1));A[:,:n]=J;A[m:m+k,n]=-1;b=np.r_[a['p']-(taup+1e-4),a['q']-cap,a['volume']-.05*v0]
  signatures={tuple(sorted(tuple(sorted(map(int,t))) for t in triangulate(x)[0]))};solves=[]
  for bi in range(8):
   sub=minimize(lambda y:(.5*ridge*(y[:-1]@y[:-1])-y[-1],np.r_[ridge*y[:-1],-1.]),np.zeros(n+1),jac=True,method='SLSQP',constraints=[{'type':'ineq','fun':lambda y:A@y+b,'jac':lambda y:A}],bounds=[(-trust,trust)]*n+[(-.01,.05)],options={'ftol':1e-12,'maxiter':200})
   d=sub.x[:-1].reshape(-1,3);new=0
   for alpha in [1,.1,.01,.001]:
    sample=x.copy();sample[a['ids']]+=alpha*d
    try:tr=triangulate(sample)[0]
    except Exception:continue
    sig=tuple(sorted(tuple(sorted(map(int,t))) for t in tr))
    if sig in signatures:continue
    signatures.add(sig);pj=alternate_jac(x,a['ids'],a['rootP'],a['parentsP'],sample)
    more=np.zeros((m,n+1));more[:,:n]=pj;A=np.vstack([A,more]);b=np.r_[b,a['p']-(taup+1e-4)];new+=1
   solves.append({'status':int(sub.status),'gain':float(sub.x[-1]),'added_fans':new})
   if not new:break
  ok=False;gain=float(sub.x[-1])
  for ls in range(25):
   al=2.**(-ls);xx=x.copy();xx[a['ids']]+=al*d
   try:aa=values(xx)
   except Exception:rejected+=1;continue
   if min(aa['p'])>=taup-1e-11 and aa['volume']>=.05*v0 and aa['capacity']>cap+max(1e-11,1e-4*al*max(gain,0)):
    ok=True;break
   rejected+=1
  row={'iteration':it,'capacity':cap,'new_capacity':aa['capacity'] if ok else None,'minP':float(min(a['p'])),'accepted':ok,'alpha':al,'fans':len(signatures),'solves':solves}
  trace.append(row)
  if ok:x=xx;frames.append(x.tolist())
  if it%10==0 or not ok:print(json.dumps(row),flush=True)
  if not ok or aa['capacity']>0:break
 out={'points':x.tolist(),'input':str(inp),'parameters':{'steps':steps,'trust':trust,'tauP':taup,'ridge':ridge,'line_search_steps':25,'model_P_buffer':1e-4,'bundle_passes':8,'fan_sample_scales':[1,.1,.01,.001],'qp_maxiter':200,'qp_ftol':1e-12,'volume_floor_fraction':.05},'trace':trace,'frames':frames,'rejected':rejected,'seconds':time.monotonic()-begin,'stats':stats(x)}
 Path(prefix+'.json').write_text(json.dumps(out,indent=2)+'\n');s=out['stats'];print(json.dumps({'accepted':len(frames),'Q':[v['depth'] for v in s['Q']],'P':[v['depth'] for v in s['P']],'SU':[len(s['S']),len(s['U'])],'VEF':[s[z] for z in ['V','E','F']],'seconds':out['seconds']}),flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]))
```

## barflow123.py
```python
"""Whole polar persistence flow under actual-centred physical-tree guards.
Finite hull/mass/complete-bar recomputation admits each step; derivatives are
local charts and sampled adjacent mass fans, not independent certificates.
"""
from __future__ import annotations
import json,sys,time
from pathlib import Path
import numpy as np,torch
from scipy.optimize import minimize
from geometry123 import load_points,triangulate,live_values,positive_tree,reference_tree_guards,stats
from bundlecap123 import alternate_jac

def dual_edges(hull):
    _,reps,inv=np.unique(np.round(hull.equations,10),axis=0,return_index=True,return_inverse=True)
    order=np.argsort(reps);rank=np.empty(len(reps),dtype=int);rank[order]=np.arange(len(reps));group=rank[inv]
    edgeowners={}
    for i,t in enumerate(hull.simplices):
        for u,v in [(t[0],t[1]),(t[0],t[2]),(t[1],t[2])]:edgeowners.setdefault(tuple(sorted((int(u),int(v)))),[]).append(int(group[i]))
    edges=set()
    for owners in edgeowners.values():
        assert len(owners)==2
        a,b=owners
        if a!=b:edges.add(tuple(sorted((a,b))))
    return np.array(sorted(edges),dtype=int)

def bar_structure(q,edges):
    q=np.asarray(q);r=(q*q).sum(axis=1);d=q[edges[:,1]]-q[edges[:,0]]
    t=np.clip(-np.einsum('ij,ij->i',q[edges[:,0]],d)/(d*d).sum(axis=1),0,1)
    z=q[edges[:,0]]+t[:,None]*d;levels=(z*z).sum(axis=1)
    par=np.arange(len(q));out=[]
    def find(a):
        while par[a]!=a:par[a]=par[par[a]];a=int(par[a])
        return a
    for ei in sorted(range(len(edges)),key=lambda i:(-levels[i],tuple(edges[i]))):
        i,j=edges[ei];a,b=find(int(i)),find(int(j))
        if a==b:continue
        if r[a]<r[b] or (r[a]==r[b] and a>b):a,b=b,a
        out.append((b,int(i),int(j)));par[b]=a
    assert len(out)==len(q)-1
    return np.array(out,dtype=int)

def depths(q,structure):
    birth=q[structure[:,0]];u=q[structure[:,1]];d=q[structure[:,2]]-u
    t=(-(u*d).sum(dim=1)/(d*d).sum(dim=1)).clamp(0,1)
    z=u+t[:,None]*d
    return torch.relu(1-(z*z).sum(dim=1)/(birth*birth).sum(dim=1))

def values(x,derivatives=False):
    tr,fa,_,hull=triangulate(x);xt=torch.tensor(x,requires_grad=True);v,g,p,q=live_values(xt,tr,fa)
    pr,pp=positive_tree(p.detach().numpy());st=bar_structure(q.detach().numpy(),dual_edges(hull));ids=np.array([i for i in range(len(x)) if i!=pr]);base=xt.detach()
    def guards(z):
        xx=base.index_copy(0,torch.tensor(ids),z.reshape(-1,3));vv,gg,px,qx=live_values(xx,tr,fa)
        return torch.cat((reference_tree_guards(px,pr,pp),depths(qx,st),vv.reshape(1)))
    z=base[ids].reshape(-1).requires_grad_();val=guards(z);m=len(x)-1
    out={'volume':float(v.detach()),'p':val[:m].detach().numpy(),'bars':val[m:-1].detach().numpy(),'ids':ids,'rootP':pr,'parentsP':pp,'faces':fa}
    if derivatives:out['jac']=torch.autograd.functional.jacobian(guards,z,vectorize=True).detach().numpy()
    return out

def run(inp,prefix,steps,trust,taup,ridge,buffer,weight):
    x=load_points(inp);v0=values(x)['volume'];trace=[];frames=[];begin=time.monotonic();rejected=0
    for it in range(steps):
        a=values(x,True);m=len(a['p']);k=len(a['bars']);J=a['jac'];n=J.shape[1];barmax=float(max(a['bars']));phi=barmax+weight*sum(a['bars'])
        A=np.zeros((m+k+1,n+1));A[:,:n]=J;A[m:m+k,:n]*=-1;A[m:m+k,n]=-1
        b=np.r_[a['p']-(taup+buffer),barmax-a['bars'],a['volume']-.05*v0]
        lin=weight*J[m:m+k].sum(axis=0)
        signatures={tuple(sorted(tuple(sorted(map(int,t))) for t in triangulate(x)[0]))};solves=[]
        for bi in range(8):
            sub=minimize(lambda y:(.5*ridge*(y[:-1]@y[:-1])+lin@y[:-1]-y[-1],np.r_[ridge*y[:-1]+lin,-1.]),np.zeros(n+1),jac=True,method='SLSQP',constraints=[{'type':'ineq','fun':lambda y:A@y+b,'jac':lambda y:A}],bounds=[(-trust,trust)]*n+[(-.01,.05)],options={'ftol':1e-12,'maxiter':200})
            d=sub.x[:-1].reshape(-1,3);new=0
            for alpha in [1,.1,.01,.001]:
                sample=x.copy();sample[a['ids']]+=alpha*d
                try:tr=triangulate(sample)[0]
                except Exception:continue
                sig=tuple(sorted(tuple(sorted(map(int,t))) for t in tr))
                if sig in signatures:continue
                signatures.add(sig);pj=alternate_jac(x,a['ids'],a['rootP'],a['parentsP'],sample)
                more=np.zeros((m,n+1));more[:,:n]=pj;A=np.vstack([A,more]);b=np.r_[b,a['p']-(taup+buffer)];new+=1
            solves.append({'status':int(sub.status),'gain':float(sub.x[-1]-lin@sub.x[:-1]),'added_fans':new})
            if not new:break
        ok=False;gain=float(sub.x[-1]-lin@sub.x[:-1])
        for ls in range(25):
            al=2.**(-ls);xx=x.copy();xx[a['ids']]+=al*d
            try:aa=values(xx)
            except Exception:rejected+=1;continue
            newphi=max(aa['bars'])+weight*sum(aa['bars'])
            if min(aa['p'])>=taup-1e-11 and aa['volume']>=.05*v0 and newphi<phi-max(1e-12,1e-4*al*max(gain,0)):
                ok=True;break
            rejected+=1
        row={'iteration':it,'maxQ':barmax,'sumQ':float(sum(a['bars'])),'new_maxQ':float(max(aa['bars'])) if ok else None,'new_sumQ':float(sum(aa['bars'])) if ok else None,'minP':float(min(a['p'])),'accepted':ok,'alpha':al,'fans':len(signatures),'solves':solves}
        trace.append(row)
        if ok:x=xx;frames.append(x.tolist())
        if it%10==0 or not ok:print(json.dumps(row),flush=True)
        if not ok or max(aa['bars'])<1e-14:break
    out={'points':x.tolist(),'input':str(inp),'parameters':{'steps':steps,'trust':trust,'tauP':taup,'ridge':ridge,'model_P_buffer':buffer,'sum_weight':weight,'line_search_steps':25,'bundle_passes':8,'fan_sample_scales':[1,.1,.01,.001],'qp_maxiter':200,'qp_ftol':1e-12,'volume_floor_fraction':.05},'trace':trace,'frames':frames,'rejected':rejected,'seconds':time.monotonic()-begin,'stats':stats(x)}
    Path(prefix+'.json').write_text(json.dumps(out,indent=2)+'\n');s=out['stats'];print(json.dumps({'accepted':len(frames),'Q':[v['depth'] for v in s['Q']],'P':[v['depth'] for v in s['P']],'SU':[len(s['S']),len(s['U'])],'VEF':[s[z] for z in ['V','E','F']],'seconds':out['seconds']}),flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]),float(sys.argv[8]))
```

## fullbarflow123.py
```python
"""Whole polar persistence flow under actual-centred physical-tree guards.
Finite hull/mass/complete-bar recomputation admits each step; derivatives are
local charts and sampled adjacent mass fans, not independent certificates.
"""
from __future__ import annotations
import json,sys,time
from pathlib import Path
import numpy as np,torch
from scipy.optimize import minimize
from geometry123 import load_points,triangulate,live_values,positive_tree,reference_tree_guards,stats
from bundlecap123 import alternate_jac

def dual_edges(hull):
    _,reps,inv=np.unique(np.round(hull.equations,10),axis=0,return_index=True,return_inverse=True)
    order=np.argsort(reps);rank=np.empty(len(reps),dtype=int);rank[order]=np.arange(len(reps));group=rank[inv]
    edgeowners={}
    for i,t in enumerate(hull.simplices):
        for u,v in [(t[0],t[1]),(t[0],t[2]),(t[1],t[2])]:edgeowners.setdefault(tuple(sorted((int(u),int(v)))),[]).append(int(group[i]))
    edges=set()
    for owners in edgeowners.values():
        assert len(owners)==2
        a,b=owners
        if a!=b:edges.add(tuple(sorted((a,b))))
    return np.array(sorted(edges),dtype=int)

def bar_structure(q,edges):
    q=np.asarray(q);r=(q*q).sum(axis=1);d=q[edges[:,1]]-q[edges[:,0]]
    t=np.clip(-np.einsum('ij,ij->i',q[edges[:,0]],d)/(d*d).sum(axis=1),0,1)
    z=q[edges[:,0]]+t[:,None]*d;levels=(z*z).sum(axis=1)
    par=np.arange(len(q));out=[]
    def find(a):
        while par[a]!=a:par[a]=par[par[a]];a=int(par[a])
        return a
    for ei in sorted(range(len(edges)),key=lambda i:(-levels[i],tuple(edges[i]))):
        i,j=edges[ei];a,b=find(int(i)),find(int(j))
        if a==b:continue
        if r[a]<r[b] or (r[a]==r[b] and a>b):a,b=b,a
        out.append((b,int(i),int(j)));par[b]=a
    assert len(out)==len(q)-1
    return np.array(out,dtype=int)

def depths(q,structure):
    birth=q[structure[:,0]];u=q[structure[:,1]];d=q[structure[:,2]]-u
    t=(-(u*d).sum(dim=1)/(d*d).sum(dim=1)).clamp(0,1)
    z=u+t[:,None]*d
    return torch.relu(1-(z*z).sum(dim=1)/(birth*birth).sum(dim=1))

def values(x,derivatives=False):
    tr,fa,_,hull=triangulate(x);xt=torch.tensor(x,requires_grad=True);v,g,p,q=live_values(xt,tr,fa)
    pr,pp=positive_tree(p.detach().numpy());st=bar_structure(q.detach().numpy(),dual_edges(hull));ids=np.array([i for i in range(len(x)) if i!=pr]);base=xt.detach()
    def guards(z):
        xx=base.index_copy(0,torch.tensor(ids),z.reshape(-1,3));vv,gg,px,qx=live_values(xx,tr,fa)
        return torch.cat((reference_tree_guards(px,pr,pp),depths(qx,st),vv.reshape(1)))
    z=base[ids].reshape(-1).requires_grad_();val=guards(z);m=len(x)-1
    out={'volume':float(v.detach()),'p':val[:m].detach().numpy(),'bars':val[m:-1].detach().numpy(),'ids':ids,'rootP':pr,'parentsP':pp,'faces':fa}
    if derivatives:out['jac']=torch.autograd.functional.jacobian(guards,z,vectorize=True).detach().numpy()
    return out

def alternate_full(x,ids,pr,pp,sample):
    tr,fa,_,hull=triangulate(sample)
    _,_,_,qs=live_values(torch.tensor(sample),tr,fa)
    st=bar_structure(qs.detach().numpy(),dual_edges(hull))
    base=torch.tensor(x);z=base[ids].reshape(-1).detach().requires_grad_()
    def f(t):
        xx=base.index_copy(0,torch.tensor(ids),t.reshape(-1,3));v,g,p,q=live_values(xx,tr,fa)
        return torch.cat((reference_tree_guards(p,pr,pp),depths(q,st)))
    val=f(z).detach().numpy();jac=torch.autograd.functional.jacobian(f,z,vectorize=True).detach().numpy()
    return val,jac

def run(inp,prefix,steps,trust,taup,ridge,buffer,weight):
    x=load_points(inp);v0=values(x)['volume'];trace=[];frames=[];begin=time.monotonic();rejected=0
    for it in range(steps):
        a=values(x,True);m=len(a['p']);k=len(a['bars']);J=a['jac'];n=J.shape[1];barmax=float(max(a['bars']));phi=barmax+weight*sum(a['bars'])
        A=np.zeros((m+k+1,n+1));A[:,:n]=J;A[m:m+k,:n]*=-1;A[m:m+k,n]=-1
        b=np.r_[a['p']-(taup+buffer),barmax-a['bars'],a['volume']-.05*v0]
        lin=weight*J[m:m+k].sum(axis=0)
        signatures={tuple(sorted(tuple(sorted(map(int,t))) for t in triangulate(x)[0]))};solves=[]
        for bi in range(8):
            sub=minimize(lambda y:(.5*ridge*(y[:-1]@y[:-1])+lin@y[:-1]-y[-1],np.r_[ridge*y[:-1]+lin,-1.]),np.zeros(n+1),jac=True,method='SLSQP',constraints=[{'type':'ineq','fun':lambda y:A@y+b,'jac':lambda y:A}],bounds=[(-trust,trust)]*n+[(-.01,.05)],options={'ftol':1e-12,'maxiter':200})
            d=sub.x[:-1].reshape(-1,3);new=0
            for alpha in [1,.1,.01,.001]:
                sample=x.copy();sample[a['ids']]+=alpha*d
                try:tr=triangulate(sample)[0]
                except Exception:continue
                sig=tuple(sorted(tuple(sorted(map(int,t))) for t in tr))
                if sig in signatures:continue
                signatures.add(sig);av,aj=alternate_full(x,a['ids'],a['rootP'],a['parentsP'],sample)
                more=np.zeros((len(av),n+1));more[:,:n]=aj;more[m:,:n]*=-1;more[m:,n]=-1
                A=np.vstack([A,more]);b=np.r_[b,a['p']-(taup+buffer),barmax-av[m:]];new+=1
            solves.append({'status':int(sub.status),'gain':float(sub.x[-1]-lin@sub.x[:-1]),'added_fans':new})
            if not new:break
        ok=False;gain=float(sub.x[-1]-lin@sub.x[:-1])
        for ls in range(25):
            al=2.**(-ls);xx=x.copy();xx[a['ids']]+=al*d
            try:aa=values(xx)
            except Exception:rejected+=1;continue
            newphi=max(aa['bars'])+weight*sum(aa['bars'])
            if min(aa['p'])>=taup-1e-11 and aa['volume']>=.05*v0 and newphi<phi-max(1e-12,1e-4*al*max(gain,0)):
                ok=True;break
            rejected+=1
        row={'iteration':it,'maxQ':barmax,'sumQ':float(sum(a['bars'])),'new_maxQ':float(max(aa['bars'])) if ok else None,'new_sumQ':float(sum(aa['bars'])) if ok else None,'minP':float(min(a['p'])),'accepted':ok,'alpha':al,'fans':len(signatures),'solves':solves}
        trace.append(row)
        if ok:x=xx;frames.append(x.tolist())
        if it%10==0 or not ok:print(json.dumps(row),flush=True)
        if not ok or max(aa['bars'])<1e-14:break
    out={'points':x.tolist(),'input':str(inp),'parameters':{'steps':steps,'trust':trust,'tauP':taup,'ridge':ridge,'model_P_buffer':buffer,'sum_weight':weight,'line_search_steps':25,'Q_bundle':True,'bundle_passes':8,'fan_sample_scales':[1,.1,.01,.001],'qp_maxiter':200,'qp_ftol':1e-12,'volume_floor_fraction':.05},'trace':trace,'frames':frames,'rejected':rejected,'seconds':time.monotonic()-begin,'stats':stats(x)}
    Path(prefix+'.json').write_text(json.dumps(out,indent=2)+'\n');s=out['stats'];print(json.dumps({'accepted':len(frames),'Q':[v['depth'] for v in s['Q']],'P':[v['depth'] for v in s['P']],'SU':[len(s['S']),len(s['U'])],'VEF':[s[z] for z in ['V','E','F']],'seconds':out['seconds']}),flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]),float(sys.argv[8]))
```

## surgery123.py
```python
"""Finite deletion and off-centre stellar nominations with actual mass/U1.
Every proposal recomputes all polar bars; no claim that deleting a carrier
cancels its basin. Deterministic small geometric family, not an exclusion.
"""
import json,sys,itertools
from pathlib import Path
import numpy as np,torch
from geometry123 import load_points,triangulate,live_values,angular,stats
from barflow123 import values

def run(inp,prefix):
 x=load_points(inp);a=values(x);base=max(a['bars'])+.1*sum(a['bars']);proposals=[];success=[]
 def test(xx,description):
  try:
   b=values(xx);mg=float(min(b['p']));score=float(max(b['bars'])+.1*sum(b['bars']))
   row={'description':description,'N':len(xx),'minP':mg,'maxQ':float(max(b['bars'])),'sumQ':float(sum(b['bars'])),'score':score}
   proposals.append(row)
   if mg>1e-6:success.append((score,xx.copy(),row))
  except Exception:proposals.append({'description':description,'N':len(xx),'admitted':False})
 for i in range(len(x)):
  if i==a['rootP']:continue
  test(np.delete(x,i,axis=0),{'operation':'delete','vertex':i})
 tr,fa,_,_=triangulate(x);_,g,p,q=live_values(torch.tensor(x),tr,fa);aq=angular(q).max(dim=1).values.numpy();roots=np.flatnonzero(aq<0)
 weights=[(1/3,1/3,1/3)]+sorted(set(itertools.permutations((.2,.2,.6))))+sorted(set(itertools.permutations((.1,.45,.45))))
 for f in roots:
  t=fa[f];aa,bb,cc=x[t];n=np.cross(bb-aa,cc-aa);n/=np.linalg.norm(n)
  for w in weights:
   z=np.array(w)@x[t]
   for h in [1e-4,.001,.005,.02,.05,.1,.2]:
    test(np.vstack([x,z+h*n]),{'operation':'stellar','face':t.tolist(),'weights':list(w),'height':h})
 success.sort(key=lambda r:r[0]);summary={'input':inp,'base_score':float(base),'proposal_count':len(proposals),'U1_admitted':len(success),'ranked':[r[2] for r in success],'proposals':proposals}
 Path(prefix+'.search.json').write_text(json.dumps(summary,indent=2)+'\n')
 for i,(score,xx,row) in enumerate(success[:5]):
  d={'points':xx.tolist(),'proposal':row,'stats':stats(xx)};Path(f'{prefix}.{i}.json').write_text(json.dumps(d,indent=2)+'\n')
 print(json.dumps({'base':base,'count':len(proposals),'admitted':len(success),'top':[r[2] for r in success[:8]]}),flush=True)
if __name__=='__main__':run(sys.argv[1],sys.argv[2])
```
