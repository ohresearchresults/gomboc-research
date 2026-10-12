# material-3790ec46859f

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J121 numerical producing methods — complete part 1 of 2

These complete numerical source units produced the J121 finite continuations and negative controls. They are not exact equilibrium certificates. All current homogeneous hulls and actual volume centroids are rebuilt, and all positive floating bars are retained in diagnostics, although the displayed census uses explicit floating floors. Exact classification of the three retained rational endpoints is separately preserved in [internal-source-reference] with the required exact115 source [internal-source-reference]. The exact source is one engine, not an independent pair of physics verifiers.

Environment actually used: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, torch 2.10.0+cpu. Set OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1. Save every code block with its final newline. Full initial inputs J119_FREEH_P_G6.txt (1179B, SHA08e3e6f45c673d60782ac16b7efdaf1ee154d43f5ddc3162416ded89276583d6) and J119_FREEH_Q_G6.txt (1162B, SHA6044d8c75d5fbf7e10345805e016b8f4aae5a8d46ad90efe868725ebb9d7b95c) are literal in [internal-source-reference]. That complete input dependency must be supplied for original-run reconstruction. Part2 preserves the finite relay/NLP source, the exact older-version patch, complete commands and observed limits. New floating checkpoints are separate input data, not substitutes for these source units.

## geometry121.py — 5112 bytes, SHA b64da8c4140fba3954b28323d603be3813b0643ed6aca18b195a2b62f2c44bf1
```python
"""Actual uniform-mass H-hull geometry for J121 numerical experiments.
Search only: floating signs are never absence certificates. Python 3.13.5,
NumPy 2.3.5, SciPy 1.17.0, torch 2.10.0+cpu. Input n_i.x <= 1.
Complete current facets/true edges are grouped, not counted as triangulation.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json
from pathlib import Path
import numpy as np
import torch
from scipy.spatial import ConvexHull, QhullError
from scipy.spatial.distance import pdist
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def read_h(path):
    if str(path).endswith('.json'):return np.asarray(json.loads(Path(path).read_text())['n'],float)
    lines=Path(path).read_text().splitlines();m,D=map(int,lines[0].split());r=np.array([list(map(int,l.split())) for l in lines[1:] if l.strip()],float)
    assert len(r)==m
    return r/D if D else r[:,:3]/r[:,3,None]

def geometry(n):
    n=np.asarray(n,float);h=ConvexHull(n)
    if h.equations[:,3].max()>=-1e-10:raise ValueError('origin not strictly inside polar')
    raw=-h.equations[:,:3]/h.equations[:,3,None]
    # Generic input fast path; nonsimple vertices are merged and distinguished.
    simple=len(raw)<2 or pdist(raw).min()>1e-9
    verts=[];groups=[];mp=[]
    for i,v in enumerate(raw):
        hits=[] if simple else [j for j,w in enumerate(verts) if np.linalg.norm(v-w)<1e-9]
        if hits:j=hits[0];groups[j].append(i)
        else:j=len(verts);verts.append(v);groups.append([i])
        mp.append(j)
    v=np.array(verts);tri=np.array([h.simplices[z[0]] for z in groups],int)
    faces={};tet=[];owners={}
    for f in sorted(h.vertices):
        ids=sorted({mp[k] for k,t in enumerate(h.simplices) if f in t});a=n[f]
        axis=np.eye(3)[np.argmin(abs(a))];e=np.cross(a,axis);e/=np.linalg.norm(e);ff=np.cross(a,e)
        delta=v[ids]-v[ids].mean(0);cy=np.array(ids)[np.argsort(np.arctan2(delta@ff,delta@e))].tolist()
        faces[int(f)]=cy
        for x,y in zip(cy,cy[1:]+cy[:1]):owners.setdefault(tuple(sorted((x,y))),[]).append(int(f))
        for b,c in zip(cy[1:-1],cy[2:]):tet.append([cy[0],b,c])
    assert all(len(a)==2 for a in owners.values())
    assert len(v)-len(owners)+len(faces)==2
    assert np.max(v@n.T-1)<1e-7
    tet=np.asarray(tet,int);w=np.linalg.det(v[tet])/6
    if w.min()<=0:raise ValueError('nonpositive tetrahedron')
    V=w.sum();g=(w[:,None]*v[tet].sum(1)/4).sum(0)/V
    active=np.array(sorted(faces),int);remap={f:i for i,f in enumerate(active)}
    pe=np.array(sorted(owners),int);qe=np.array([[remap[f] for f in owners[tuple(e)]] for e in pe],int)
    q=n[active]/(1-n[active]@g)[:,None];p=v-g
    return dict(n=n,v=v,p=p,q=q,pe=pe,qe=qe,faces=faces,active=active,tet=tet,triples=tri,g=g,volume=V,simple=simple)

def tensors(n,G):
    if not G['simple']:raise ValueError('free-H derivative requires simple current fan')
    v=torch.linalg.solve(n[G['triples']],torch.ones((len(G['v']),3,1))).squeeze(-1)
    tet=v[G['tet']];w=torch.linalg.det(tet)/6;V=w.sum();g=(w[:,None]*tet.sum(1)/4).sum(0)/V
    p=v-g;nn=n[G['active']];q=nn/(1-nn@g)[:,None]
    return p,q,g,V

def arrows(x,angular=True):
    d=x[None,:,:]-x[:,None,:];sq=(x*x).sum(1);num=np.einsum('ik,ijk->ij',x,d)
    if angular:
        den=np.sqrt(sq[:,None]*(d*d).sum(2));den[np.diag_indices(len(x))]=1
        a=num/den
    else:a=num/sq[:,None]
    a[np.diag_indices(len(x))]=-np.inf
    return a.max(1),a.argmax(1),a

def bars(x,edges):
    sq=(x*x).sum(1);d=x[edges[:,1]]-x[edges[:,0]];dd=(d*d).sum(1)
    t=np.clip(-np.einsum('ij,ij->i',x[edges[:,0]],d)/dd,0,1)
    z=x[edges[:,0]]+t[:,None]*d;lev=(z*z).sum(1)
    # Rounding-level errors are clipped only in this numerical diagnostic.
    lev=np.minimum(lev,np.minimum(sq[edges[:,0]],sq[edges[:,1]]))
    par=np.arange(len(x));out=[]
    def root(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return int(i)
    for k in sorted(range(len(edges)),key=lambda k:(-lev[k],tuple(edges[k]))):
        a,b=map(root,edges[k])
        if a==b:continue
        if (sq[a],-a)<(sq[b],-b):a,b=b,a
        depth=1-lev[k]/sq[b]
        if depth>0:out.append(dict(depth=float(depth),root=b,edge=edges[k].tolist(),birth=float(sq[b]),death=float(lev[k])))
        par[b]=a
    return sorted(out,key=lambda b:-b['depth'])

def describe(n):
    G=geometry(n);pa,pw,_=arrows(G['p']);qa,qw,_=arrows(G['q']);pr=int(np.argmax((G['p']**2).sum(1)));qr=int(np.argmax((G['q']**2).sum(1)))
    pidx=np.arange(len(pa))!=pr;qidx=np.arange(len(qa))!=qr
    P=bars(G['p'],G['pe']);Q=bars(G['q'],G['qe'])
    return dict(VEF=[len(G['v']),len(G['pe']),len(G['active'])],S=G['active'][qa<-1e-10].tolist(),U=np.where(pa<-1e-10)[0].tolist(),P=[b for b in P if b['depth']>1e-12],Q=[b for b in Q if b['depth']>1e-12],all_positive_float_P=P,all_positive_float_Q=Q,minp=float(pa[pidx].min()),minq=float(qa[qidx].min()),rho=float(min(pa[pidx].min(),qa[qidx].min())),volume=float(G['volume']),g=G['g'].tolist(),numerical_only=True)

def normalize(n):
    G=geometry(n);return n/(1-n@G['g'])[:,None]*G['volume']**(1/3)
```

## coforest121.py — 5004 bytes, SHA 5662a947b9bf9d0dc79f4138b3fc5c8e1fb716cb8ddde5bed3b21dbe3e4cb054
```python
"""J121 two-sided epigraph witness repair; numerical feasibility search only.
All active primal/polar nonroots are enforced individually, with dynamic global
witnesses. Duplicate constraints at a fan split cannot multiply a penalty.
Current actual uniform mass is differentiated and rebuilt at every finite trial.
No outgoing condition is relaxed by a solid-angle weight or a bar threshold.
"""
import sys,json,time
from pathlib import Path
import numpy as np,torch
from scipy.optimize import linprog
from scipy.spatial import QhullError
from geometry121 import geometry,tensors,read_h,arrows,describe,normalize

def model(n,angular=True):
    G=geometry(n);pa,pw,_=arrows(G['p'],angular);qa,qw,_=arrows(G['q'],angular)
    pr=int(np.argmax((G['p']**2).sum(1)));qr=int(np.argmax((G['q']**2).sum(1)))
    ip=np.array([i for i in range(len(pa)) if i!=pr]);iq=np.array([i for i in range(len(qa)) if i!=qr])
    def fn(flat):
        p,q,g,V=tensors(flat.reshape(n.shape),G);out=[]
        for x,idx,w in [(p,ip,pw[ip]),(q,iq,qw[iq])]:
            d=x[w]-x[idx];num=(x[idx]*d).sum(1)
            den=torch.sqrt((x[idx]*x[idx]).sum(1)*(d*d).sum(1)) if angular else (x[idx]*x[idx]).sum(1)
            out.append(num/den)
        return torch.cat(out+[g,torch.log(V)[None]])
    z=torch.tensor(n.ravel());values=fn(z).detach().numpy()
    J=torch.autograd.functional.jacobian(fn,z,vectorize=True).detach().numpy()
    return G,values[:-4],J[:-4],J[-4:],dict(pr=pr,qr=qr,ip=ip.tolist(),iq=iq.tolist(),pw=pw[ip].tolist(),qw=qw[iq].tolist())

def run(inp,prefix,maxiter=150,trust=.01,angular=True):
    n=read_h(inp);G=geometry(n);n=n[G['active']];n=normalize(n)
    prefix=Path(prefix);prefix.parent.mkdir(exist_ok=True,parents=True)
    hist=[];start=time.time();delta=trust;initial=n.copy();accepted=0;reason='iteration_limit'
    for it in range(maxiter):
        G,a,J,gauge,policy=model(n,angular);rho=float(a.min());dim=n.size
        scale=np.repeat(np.linalg.norm(n,axis=1),3)
        # Epigraph, not a sum over vertices. Four equalities merely fix the
        # similarity/translation coordinate gauges within this free-H chart.
        A=np.column_stack([-J*scale,np.ones(len(a))]);c=np.r_[np.zeros(dim),-1]
        eq=np.column_stack([gauge*scale,np.zeros(4)])
        lp=linprog(c,A_ub=A,b_ub=a,A_eq=eq,b_eq=np.zeros(4),bounds=[(-delta,delta)]*dim+[(rho,0.005)],method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
        if not lp.success:
            hist.append(dict(iteration=it,lp_status=int(lp.status),message=lp.message,rho=rho,trust=delta));reason='linear_solver_failure';break
        predicted=float(lp.x[-1]);step=(lp.x[:-1]*scale).reshape(n.shape);good=False;attempts=[]
        for k in range(16):
            alpha=2.**(-k)
            try:
                nn=n+alpha*step;gg=geometry(nn)
                if not gg['simple']:raise ValueError('nonsimple free-H wall')
                pc=arrows(gg['p'],angular)[0];qc=arrows(gg['q'],angular)[0]
                pr=int(np.argmax((gg['p']**2).sum(1)));qr=int(np.argmax((gg['q']**2).sum(1)))
                rr=float(min(np.delete(pc,pr).min(),np.delete(qc,qr).min()))
                ok=rr>=rho+max(1e-11,0.05*alpha*(predicted-rho))
                attempts.append(dict(alpha=alpha,rho=rr,accepted=ok,VEF=[len(gg['v']),len(gg['pe']),len(gg['active'])]))
                if ok:good=True;break
            except (ValueError,AssertionError,QhullError,np.linalg.LinAlgError) as ex:attempts.append(dict(alpha=alpha,error=str(ex)))
        rec=dict(iteration=it,rho=rho,predicted=predicted,trust=delta,accepted=good,attempts=attempts,policy=policy,duals=(-lp.ineqlin.marginals).tolist())
        if good:
            n=normalize(nn);accepted+=1;delta=min(.08,delta*(1.35 if k<=1 else .8))
            s=describe(n);rec['stats']=s
            Path(str(prefix)+'.last.json').write_text(json.dumps(dict(n=n.tolist(),stats=s,iteration=it,accepted=accepted),indent=2)+'\n')
            if s['rho']>1e-8:reason='NUMERICAL_ONE_ROOT_EACH_NEEDS_EXACT_AUDIT';hist.append(rec);break
        else:
            delta*=.25
            if delta<1e-8:reason='finite_policy_trust_stall';hist.append(rec);break
        hist.append(rec)
        if it%10==0 or not good:print('COFOREST121',it,'accepted',accepted,'rho',rho,'to',rec.get('stats',{}).get('rho'),'P/Q',len(rec.get('stats',{}).get('P',[])),len(rec.get('stats',{}).get('Q',[])),'trust',delta,flush=True)
    out=dict(n=n.tolist(),initial=initial.tolist(),stats=describe(n),reason=reason,accepted=accepted,maxiter=maxiter,initial_trust=trust,angular=angular,seconds=time.time()-start,history=hist)
    Path(str(prefix)+'.json').write_text(json.dumps(out,indent=2)+'\n');print('COFOREST121_DONE',reason,'accepted',accepted,'stats',out['stats'],flush=True)
    return out
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 150,float(sys.argv[4]) if len(sys.argv)>4 else .01,not(len(sys.argv)>5 and sys.argv[5]=='radial'))
```

## paired121.py — 5898 bytes, SHA 903d5ca44c69f8f60b598c9a9b328b7b7748194d3ac88bf4a11e3202d86baa36
```python
"""J121 paired persistence continuation with individual no-birth constraints.
This is a numerical producer, not an exact equilibrium or nonexistence proof.
All actual nonroot outgoing guards are protected, except the one current
positive-persistence root on each side. LP maximizes a common fractional
reduction of both complete sole bars. Current geometry/mass are re-integrated.
"""
import sys,json,time
from pathlib import Path
import numpy as np,torch
from scipy.optimize import linprog,minimize
from scipy.spatial import QhullError
from geometry121 import geometry,tensors,read_h,arrows,describe,normalize,bars

def model(n):
 G=geometry(n);pol=[];outs=[]
 for x,ed in [(G['p'],G['pe']),(G['q'],G['qe'])]:
  a,w,_=arrows(x);bb=bars(x,ed);pr=int(np.argmax((x*x).sum(1)));root=bb[0]['root'] if bb else pr
  ip=np.array([i for i in range(len(x)) if i not in {pr,root}],int)
  pol.append(dict(root=root,elder=pr,idx=ip.tolist(),witness=w[ip].tolist(),bar=bb[0] if bb else None))
 def fn(flat):
  p,q,g,V=tensors(flat.reshape(n.shape),G);guards=[];dep=[]
  for x,P in zip((p,q),pol):
   idx=P['idx'];w=P['witness'];d=x[w]-x[idx]
   guards.append((x[idx]*d).sum(1)/torch.sqrt((x[idx]*x[idx]).sum(1)*(d*d).sum(1)))
   if P['bar'] is None:dep.append(flat.sum()*0)
   else:
    u=P['root'];a,b=P['bar']['edge'];d=x[b]-x[a];t=torch.clamp(-(x[a]@d)/(d@d),0,1);z=x[a]+t*d;dep.append(1-(z@z)/(x[u]@x[u]))
  return torch.cat(guards+[torch.stack(dep),g,torch.log(V)[None]])
 z=torch.tensor(n.ravel());val=fn(z).detach().numpy();J=torch.autograd.functional.jacobian(fn,z,vectorize=True).detach().numpy()
 return G,val,J,pol

def run(inp,prefix,maxiter=160,trust=.01,tau=1e-6,qp=False,mode='both'):
 n=read_h(inp);n=n[geometry(n)['active']];n=normalize(n);initial=n.copy();hist=[];start=time.time();delta=trust;reason='iteration_limit';accepted=0
 for it in range(maxiter):
  G,v,J,pol=model(n);guards=v[:-6];D=v[-6:-4];ng=len(guards);dim=n.size;scale=np.repeat(np.linalg.norm(n,axis=1),3)
  if min(guards)<tau*.49:reason='initial_no_birth_margin_failure';break
  # Restore the fixed positive margin at each linear step; do not creep
  # along the lower finite-admission boundary.
  floor=np.full_like(guards,tau)
  Aub=[np.column_stack([-J[:ng]*scale,np.zeros(ng)])];bub=[guards-floor]
  gd=J[-6:-4]*scale
  target=np.maximum(D,1e-9)
  coeff=target if mode=='both' else np.array([target[0] if mode=='P' else 0.,target[1] if mode=='Q' else 0.])
  Aub.append(np.column_stack([gd,coeff]));bub.append(np.zeros(2))
  A=np.vstack(Aub);b=np.concatenate(bub);eq=np.column_stack([J[-4:]*scale,np.zeros(4)])
  lp=linprog(np.r_[np.zeros(dim),-1],A_ub=A,b_ub=b,A_eq=eq,b_eq=np.zeros(4),bounds=[(-delta,delta)]*dim+[(0,.2)],method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
  if not lp.success:reason='linear_solver_failure';hist.append(dict(iteration=it,rho=float(min(guards)),lp_status=int(lp.status),message=lp.message));break
  t=float(lp.x[-1]);z=lp.x[:-1]
  if t<1e-10:reason='linear_pareto_stall';hist.append(dict(iteration=it,t=t,D=D.tolist(),policy=pol,duals=(-lp.ineqlin.marginals).tolist()));break
  if qp:
   goal=.5*t;aa=A[:,:-1];bb=b-A[:,-1]*goal;ee=eq[:,:-1]
   res=minimize(lambda x:(.5*x@x,x),z*.5,jac=True,method='SLSQP',bounds=[(-delta,delta)]*dim,constraints=[dict(type='ineq',fun=lambda x:bb-aa@x,jac=lambda x:-aa),dict(type='eq',fun=lambda x:ee@x,jac=lambda x:ee)],options=dict(maxiter=80,ftol=1e-15))
   if res.success and (bb-aa@res.x).min()>-1e-9:z=res.x;t=goal
  step=(z*scale).reshape(n.shape);trials=[];good=False
  for k in range(18):
   alpha=2.**(-k)
   try:
    nn=n+alpha*step;gg=geometry(nn)
    if not gg['simple']:raise ValueError('nonsimple wall')
    nr=[];mn=[];deps=[]
    for xx,ed in [(gg['p'],gg['pe']),(gg['q'],gg['qe'])]:
     aa,ww,_=arrows(xx);bs=bars(xx,ed);pr=int(np.argmax((xx*xx).sum(1)));jr=bs[0]['root'] if bs else pr;idx=[i for i in range(len(xx)) if i not in {pr,jr}]
     nr.append(int(sum(aa<0)));mn.append(float(aa[idx].min()));deps.append(bs[0]['depth'] if bs else 0)
    gain=.05*alpha*t
    ok=min(mn)>=tau*.5 and all(deps[j]<=D[j]-gain*coeff[j]+2e-13 for j in range(2)) and (D-np.array(deps)).sum()>1e-12
    trials.append(dict(alpha=alpha,D=deps,roots=nr,min_guard=mn,accepted=bool(ok)))
    if ok:good=True;break
   except (ValueError,AssertionError,QhullError,np.linalg.LinAlgError) as ex:trials.append(dict(alpha=alpha,error=str(ex)))
  rec=dict(iteration=it,D=D.tolist(),t=t,trust=delta,accepted=good,trials=trials,policy=pol,duals=(-lp.ineqlin.marginals).tolist())
  if good:
   n=normalize(nn);accepted+=1;delta=min(.08,delta*(1.25 if k<2 else .85));rec['stats']=describe(n)
   Path(prefix+'.last.json').write_text(json.dumps(dict(n=n.tolist(),stats=rec['stats'],accepted=accepted),indent=2)+'\n')
   if rec['stats']['rho']>1e-8:reason='NUMERICAL_ONE_ROOT_EACH_NEEDS_EXACT_AUDIT';hist.append(rec);break
  else:
   delta*=.2
   if delta<1e-9:reason='finite_no_birth_stall';hist.append(rec);break
  hist.append(rec)
  if it%10==0 or not good:print('PAIRED121',mode,it,accepted,D,'=>',[b['depth'] for b in rec.get('stats',{}).get('P',[])],[b['depth'] for b in rec.get('stats',{}).get('Q',[])],min(guards),delta,flush=True)
 out=dict(n=n.tolist(),initial=initial.tolist(),stats=describe(n),reason=reason,accepted=accepted,maxiter=maxiter,trust=trust,tau=tau,qp=qp,mode=mode,seconds=time.time()-start,history=hist)
 Path(prefix+'.json').write_text(json.dumps(out,indent=2)+'\n');print('PAIRED121_DONE',mode,reason,accepted,[b['depth'] for b in out['stats']['P']],[b['depth'] for b in out['stats']['Q']],out['stats']['VEF'],flush=True);return out
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 160,float(sys.argv[4]) if len(sys.argv)>4 else .01,float(sys.argv[5]) if len(sys.argv)>5 else 1e-6,('qp' in sys.argv),sys.argv[-1] if sys.argv[-1] in ['P','Q'] else 'both')
```
