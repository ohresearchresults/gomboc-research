# material-93a3ce5f03d5

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Complete numerical producer sources for the COORD_V20 finite experiments

These five complete source units materially produced the twenty-one exact frozen polyhedra in recovery capsule [internal-source-reference]. They are numerical search methods, not proofs of strict class or completeness. All hulls use their actual uniformly filled centroid, recomputed at every call. No network, variable density, free reference center, or fixed escape-tree chamber is used. Dependencies: CPython3.13.5,NumPy2.3.5,SciPy1.17.0,PyTorch2.10.0+cpu; torch float64 and one thread. Use OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. The exact checker is the separate concatenation of [internal-source-reference] and the Python block in [internal-source-reference].

Executed commands in an empty working directory were `python radial_flow.py --mode log --weight 1 --steps 180 --maxfun 2000 --out log1`, `python batch_flow.py`, the default `python escape_flow.py --out escape_w10_m1e-4 --weight 10 --margin .0001`, `python batch_escape.py`, and `python -B -S freeze_selected.py`. The two batch scripts can resume completed summaries; all24 cases in each batch completed. Selected exact numerical starting pins and finite coverage are preserved separately. Re-running an optimizer need not reproduce byte-identical floating results on another platform; the exact body capsule bypasses optimization using the original binary64 pins.

Byte counts and SHA256 of the literal code blocks, retaining their final newline:
radial_flow.py7537,c51ddbd0814b1e333be8350196e1b38426a30f1833ad501e6a280ac6a26e1220;
batch_flow.py1076,ba3672810e27dfbdc9668b61421405181d649b3d983ccec0b11c8afbdceb1dc6;
escape_flow.py4857,6c98e3a66233199f8d08b5608913b41a6b8a82f5bbe745bfea55462cc355c30d;
batch_escape.py987,91742c49f943e797c21ebc1d44c0baa5cf88f34479beca69f917ea1155f54dd1;
freeze_selected.py1786,019b80b21d64d223f157a5001bc4904eac1fb7821bf1263149cddc74c84641dc.

## radial_flow.py
```python
#!/usr/bin/env python3
"""Finite 20-vertex own-centroid radial-H0 experiments (numerical, not an exact certificate).
Re-run: python radial_flow.py --mode log --weight 1 --steps 180 --out log1
Requires CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, PyTorch 2.10.0+cpu.
The literal integer input is NW00_V20_COMP_G3; its immutable source is
figure-0449. All mass calculations use the physical convex hull.
"""
import argparse, json, os, sys, time
import numpy as np
from scipy.spatial import ConvexHull, QhullError
from scipy.optimize import minimize
import torch

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
INPUT = np.array([[-3553,371,-301],[-2340,-999,1069],[-1643,-1405,1459],[-1370,1438,-1360],[-1053,-1585,1657],[-446,-1662,1735],[-76,1421,-1439],[337,-1579,1653],[743,901,-1057],[809,-1477,1497],[1214,-1303,1288],[1456,509,-684],[1614,-969,941],[1765,481,-427],[1823,-524,376],[1828,-705,584],[1848,334,-252],[1877,-628,494],[1903,162,-81],[1943,-156,190]], dtype=np.int64)

def geometry(x):
    """Oriented QHull triangles; actual volume and centroid; physical-centered polar."""
    xn = x.detach().numpy()
    hull = ConvexHull(xn)
    tri = hull.simplices.copy()
    cr = np.cross(xn[tri[:,1]]-xn[tri[:,0]],xn[tri[:,2]]-xn[tri[:,0]])
    flip = np.einsum('ij,ij->i', cr,hull.equations[:,:3]) < 0
    tri[flip] = tri[flip][:,[0,2,1]]
    a,b,c = (x[tri[:,i]] for i in range(3))
    d = torch.sum(a*torch.linalg.cross(b,c),dim=1)
    D = d.sum()
    volume = D/6
    center = torch.sum(d[:,None]*(a+b+c),dim=0)/(4*D)
    p = x-center
    n = torch.linalg.cross(b-a,c-a)
    offsets = torch.sum(n*(a-center),dim=1)
    q = n/offsets[:,None]
    return p,q,volume,center,tri,hull

def barcode(x):
    """Complete graph weighted by exact-form chord minimum, floats here.
    Every vertex is born at norm^2. Descending-edge Kruskal with elder root
    gives the positive H0 bars, including zero bars in the returned tensor.
    """
    n=len(x)
    i,j=np.triu_indices(n,1)
    u,v=x[i],x[j]
    d=v-u
    den=(d*d).sum(1)
    safe=torch.where(den>0,den,torch.ones_like(den))
    t=(-(u*d).sum(1)/safe).clamp(0,1)
    foot=u+t[:,None]*d
    w=(foot*foot).sum(1)
    a=(x*x).sum(1)
    an=a.detach().numpy(); wn=w.detach().numpy()
    par=list(range(n)); peak=list(range(n))
    def root(k):
        while par[k]!=k:
            par[k]=par[par[k]]; k=par[k]
        return k
    pairs=[]
    for k in np.argsort(-wn,kind='stable'):
        r,s=root(int(i[k])),root(int(j[k]))
        if r==s: continue
        if (an[peak[r]],-peak[r]) < (an[peak[s]],-peak[s]): r,s=s,r
        pairs.append((peak[s],int(k),int(i[k]),int(j[k]),peak[r]))
        par[s]=r
        if len(pairs)==n-1: break
    births=a[[z[0] for z in pairs]]
    deaths=w[[z[1] for z in pairs]]
    gaps=(births-deaths).clamp(min=0)
    return births,deaths,gaps,pairs

def diagnostics(x, mode='log', weight=1., reg=0.):
    p,q,vol,center,tri,hull=geometry(x)
    if float(vol.detach())<=1e-15 or not bool(torch.isfinite(q).all()):
        raise ValueError('degenerate physical hull')
    bp,dp,gp,pp=barcode(p); bq,dq,gq,pq=barcode(q)
    if mode=='log':
        ep=torch.log1p(gp/dp.clamp(min=1e-30)).sum()
        eq=torch.log1p(gq/dq.clamp(min=1e-30)).sum()
    elif mode=='relative':
        ep=(gp/bp.clamp(min=1e-30)).sum(); eq=(gq/bq.clamp(min=1e-30)).sum()
    elif mode=='volume':
        ep=gp.sum()/vol.pow(2/3); eq=gq.sum()*vol.pow(2/3)
    else: raise ValueError(mode)
    R=torch.linalg.vector_norm(p,dim=1).max()
    r=1/torch.linalg.vector_norm(q,dim=1).max()
    penalty=reg*torch.relu(torch.log(.03*R/r)).square()
    loss=weight*ep+eq+penalty
    def bars(b,d,g,pairs):
        bn,dn,gn=(z.detach().numpy() for z in (b,d,g))
        scale=max(float(np.max(bn)),1e-300)
        # Relative significance is a diagnostic tolerance, not an exact zero claim.
        ids=[k for k,v in enumerate(gn) if v>1e-10*scale]
        return [dict(peak=pairs[k][0],edge=pairs[k][2:4],elder=pairs[k][4],birth=float(bn[k]),death=float(dn[k]),gap=float(gn[k])) for k in ids]
    pb=bars(bp,dp,gp,pp); qb=bars(bq,dq,gq,pq)
    met=dict(loss=float(loss.detach()),ep=float(ep.detach()),eq=float(eq.detach()),TP=float((gp.sum()/vol.pow(2/3)).detach()),TQ=float((gq.sum()*vol.pow(2/3)).detach()),volume=float(vol.detach()),centroid=center.detach().tolist(),rR=float((r/R).detach()),V=len(hull.vertices),E=len(hull.simplices)*3//2,F=len(hull.simplices),Pbars=pb,Qbars=qb,U_radial=1+len(pb),S_radial=1+len(qb))
    return loss,met

def run(args):
    out=args.out; os.makedirs(out,exist_ok=True)
    if args.start:
        start=np.array(json.load(open(args.start))['points'],float)
    else:
        start=INPUT.astype(float)/1000
        tx=torch.tensor(start)
        p,_,_,_,_,_=geometry(tx)
        start=p.numpy(); start/=np.linalg.norm(start,axis=1).max()
    rng=np.random.default_rng(args.seed)
    if args.noise:
        start=start+args.noise*rng.normal(size=start.shape)
    records=[]; best=[float('inf'),None]; calls=[0]; stamp=time.monotonic()
    def fun(y):
        calls[0]+=1
        x=torch.tensor(y.reshape(-1,3),requires_grad=True)
        try:
            loss,met=diagnostics(x,args.mode,args.weight,args.reg)
            loss.backward(); grad=x.grad.detach().numpy().ravel()
            value=float(loss.detach())
            if not np.isfinite(value) or not np.isfinite(grad).all(): raise ValueError('nonfinite')
        except (QhullError,ValueError,RuntimeError,FloatingPointError) as exc:
            records.append(dict(call=calls[0],error=str(exc)[:200]))
            return 1e12,np.zeros_like(y)
        if calls[0]==1 or value<best[0]:
            met.update(call=calls[0],points=x.detach().tolist(),mode=args.mode,weight=args.weight,reg=args.reg)
            best[:]=[value,met]
            json.dump(met,open(os.path.join(out,'best.json'),'w'),separators=(',',':'))
        if calls[0]==1 or calls[0]%100==0:
            records.append(dict(call=calls[0],loss=value,U=met['U_radial'],S=met['S_radial'],TP=met['TP'],TQ=met['TQ'],rR=met['rR']))
        return value,grad
    result=minimize(fun,start.ravel(),jac=True,method='L-BFGS-B',options=dict(maxiter=args.steps,maxfun=args.maxfun,maxls=30,ftol=1e-14,gtol=1e-9,maxcor=20))
    _,terminal=diagnostics(torch.tensor(result.x.reshape(-1,3)),args.mode,args.weight,args.reg)
    terminal['points']=result.x.reshape(-1,3).tolist()
    json.dump(terminal,open(os.path.join(out,'terminal.json'),'w'),separators=(',',':'))
    summary=dict(args=vars(args),iterations=int(result.nit),evaluations=int(result.nfev),calls=calls[0],message=str(result.message),success=bool(result.success),elapsed=time.monotonic()-stamp,best={k:v for k,v in best[1].items() if k not in ('points','Pbars','Qbars')},terminal={k:v for k,v in terminal.items() if k not in ('points','Pbars','Qbars')},records=records)
    json.dump(summary,open(os.path.join(out,'summary.json'),'w'),separators=(',',':'))
    print(json.dumps(summary,separators=(',',':')))

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); ap.add_argument('--mode',choices=['log','relative','volume'],default='log'); ap.add_argument('--weight',type=float,default=1.); ap.add_argument('--reg',type=float,default=0.); ap.add_argument('--steps',type=int,default=180); ap.add_argument('--maxfun',type=int,default=3000); ap.add_argument('--start'); ap.add_argument('--noise',type=float,default=0.); ap.add_argument('--seed',type=int,default=21092603)
    run(ap.parse_args())
```

## batch_flow.py
```python
#!/usr/bin/env python3
import argparse, contextlib, io, json, os
from radial_flow import run
cases=[]
for mode in ['log','relative','volume']:
    for weight in [3.,10.,30.,100.,300.,1000.]:
        cases.append(dict(mode=mode,weight=weight,start=None,tag=f'{mode}_w{int(weight)}'))
for weight in [3.,10.,30.,100.,300.,1000.]:
    cases.append(dict(mode='log',weight=weight,start='log1/best.json',tag=f'log1_cont_w{int(weight)}'))
rows=[]
for k,c in enumerate(cases):
    args=argparse.Namespace(out=c['tag'],mode=c['mode'],weight=c['weight'],reg=0.,steps=300,maxfun=3000,start=c['start'],noise=0.,seed=21092603)
    if not os.path.exists(c['tag']+'/summary.json'):
        with contextlib.redirect_stdout(io.StringIO()): run(args)
    a=json.load(open(c['tag']+'/summary.json')); b=a['best']
    row=dict(tag=c['tag'],nfev=a['evaluations'],nit=a['iterations'],loss=b['loss'],TP=b['TP'],TQ=b['TQ'],U=b['U_radial'],S=b['S_radial'],V=b['V'],rR=b['rR'])
    rows.append(row); print(json.dumps(row),flush=True)
    json.dump(rows,open('BATCH_FLOW.json','w'),separators=(',',':'))
```

## escape_flow.py
```python
#!/usr/bin/env python3
"""Finite all-pair escape-margin flow on a free V20 physical hull.
Numerical only; actual filled centroid differentiated through every current hull.
Self and coincident witnesses are excluded. The excepted root is dynamically the
largest-radius point; witness choice may change, so no fixed escape tree is held.
Run: python escape_flow.py --out escape_w10_m1e-4 --weight 10 --margin .0001
"""
import argparse,json,os,time
import numpy as np
import torch
from scipy.optimize import minimize
from scipy.spatial import QhullError
from radial_flow import INPUT,geometry,diagnostics

def escape(x,margin,form):
    n=len(x)
    if n<2: raise ValueError('insufficient points')
    norm=torch.linalg.vector_norm(x,dim=1)
    delta=x[None,:,:]-x[:,None,:]
    length=torch.linalg.vector_norm(delta,dim=2)
    dot=(x[:,None,:]*delta).sum(2)
    if form=='cos':
        scale=norm[:,None]*length
    elif form=='radial':
        scale=norm[:,None].square().expand(n,n)
    else: raise ValueError(form)
    valid=length>1e-12*norm.max().detach()
    scores=torch.where(valid,dot/scale.clamp(min=1e-30),torch.full_like(dot,-1e6))
    score,witness=scores.max(1)
    root=int(torch.argmax(norm).detach())
    keep=torch.arange(n)!=root
    deficit=torch.relu(margin-score[keep])
    # Squared penalty avoids a hard fixed-tree chamber; all witness alternatives remain.
    cost=deficit.square().sum()
    vals=score[keep].detach().numpy()
    return cost,dict(root=root,nonroot_min=float(vals.min()),nonroot_bad=int((vals<=0).sum()),nonroot_below_margin=int((vals<margin).sum()),witness=witness.detach().tolist())

def measure(x,weight,margin,form):
    p,q,v,c,t,h=geometry(x)
    ep,mp=escape(p[h.vertices],margin,form)
    eq,mq=escape(q,margin,form)
    loss=weight*ep+eq
    met=dict(loss=float(loss.detach()),EP=float(ep.detach()),EQ=float(eq.detach()),P=mp,Q=mq,volume=float(v.detach()),centroid=c.detach().tolist(),V=len(h.vertices),E=3*len(h.simplices)//2,F=len(h.simplices))
    return loss,met

def run(args):
    os.makedirs(args.out,exist_ok=True)
    if args.start: x=np.asarray(json.load(open(args.start))['points'],float)
    else:
        p,*_=geometry(torch.tensor(INPUT.astype(float)/1000));x=p.numpy();x/=np.linalg.norm(x,axis=1).max()
    rng=np.random.default_rng(args.seed)
    x=x+args.noise*rng.normal(size=x.shape)
    best=[float('inf'),None];calls=[0];records=[];st=time.monotonic()
    def fun(y):
        calls[0]+=1
        a=torch.tensor(y.reshape(-1,3),requires_grad=True)
        try:
            loss,met=measure(a,args.weight,args.margin,args.form)
            loss.backward();g=a.grad.detach().numpy().ravel();f=float(loss.detach())
            if not np.isfinite(f) or not np.isfinite(g).all():raise ValueError('nonfinite')
        except (ValueError,QhullError,RuntimeError,FloatingPointError) as e:
            records.append(dict(call=calls[0],error=str(e)[:200]));return 1e12,np.zeros_like(y)
        if f<best[0]:
            met.update(points=a.detach().tolist(),call=calls[0]);best[:]=[f,met]
            json.dump(met,open(args.out+'/best.json','w'),separators=(',',':'))
        if calls[0]==1 or calls[0]%200==0:
            records.append(dict(call=calls[0],loss=f,U=1+met['P']['nonroot_bad'],S=1+met['Q']['nonroot_bad'],EP=met['EP'],EQ=met['EQ']))
        return f,g
    res=minimize(fun,x.ravel(),jac=True,method='L-BFGS-B',options=dict(maxiter=args.steps,maxfun=args.maxfun,maxls=40,maxcor=20,ftol=1e-16,gtol=1e-11))
    _,term=measure(torch.tensor(res.x.reshape(-1,3)),args.weight,args.margin,args.form);term['points']=res.x.reshape(-1,3).tolist()
    json.dump(term,open(args.out+'/terminal.json','w'),separators=(',',':'))
    _,rad=diagnostics(torch.tensor(best[1]['points']))
    summary=dict(args=vars(args),iterations=int(res.nit),evaluations=int(res.nfev),calls=calls[0],success=bool(res.success),message=str(res.message),elapsed=time.monotonic()-st,best={k:v for k,v in best[1].items() if k!='points'},radial=rad,records=records)
    json.dump(summary,open(args.out+'/summary.json','w'),separators=(',',':'))
    print(json.dumps(dict(out=args.out,nit=res.nit,nfev=res.nfev,loss=best[0],U=1+best[1]['P']['nonroot_bad'],S=1+best[1]['Q']['nonroot_bad'],TP=rad['TP'],TQ=rad['TQ'],rR=rad['rR'],minP=best[1]['P']['nonroot_min'],minQ=best[1]['Q']['nonroot_min'])),flush=True)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--weight',type=float,default=10.);ap.add_argument('--margin',type=float,default=.0001);ap.add_argument('--form',choices=['cos','radial'],default='cos');ap.add_argument('--steps',type=int,default=600);ap.add_argument('--maxfun',type=int,default=4000);ap.add_argument('--start');ap.add_argument('--seed',type=int,default=21092604);ap.add_argument('--noise',type=float,default=0.)
    run(ap.parse_args())
```

## batch_escape.py
```python
#!/usr/bin/env python3
import argparse,contextlib,io,json,os
from escape_flow import run
cases=[]
for start,label in [(None,'input'),('log1/best.json','log1'),('relative_w1000/best.json','rp1000')]:
 for form in ['cos','radial']:
  for weight in [.1,1.,10.,100.]:
   tag=f'esc_{label}_{form}_w{weight:g}'
   cases.append(dict(out=tag,weight=weight,margin=.0001,form=form,steps=800,maxfun=4000,start=start,seed=21092604,noise=0.))
rows=[]
for c in cases:
 if not os.path.exists(c['out']+'/summary.json'):
  with contextlib.redirect_stdout(io.StringIO()):run(argparse.Namespace(**c))
 a=json.load(open(c['out']+'/summary.json'));b=a['best'];r=a['radial']
 z=dict(out=c['out'],nfev=a['evaluations'],nit=a['iterations'],loss=b['loss'],U=1+b['P']['nonroot_bad'],S=1+b['Q']['nonroot_bad'],TP=r['TP'],TQ=r['TQ'],rR=r['rR'],minP=b['P']['nonroot_min'],minQ=b['Q']['nonroot_min'])
 rows.append(z);print(json.dumps(z),flush=True)
 json.dump(rows,open('BATCH_ESCAPE.json','w'),separators=(',',':'))
```

## freeze_selected.py
```python
#!/usr/bin/env python3
"""Independent ties-to-even freezing of the pinned finite-flow outputs; no grid-to-grid rounding."""
import json,os,math
from fractions import Fraction as F
from exact_poly import audit,dot,sub,mul
os.makedirs('exact',exist_ok=True)
rows=[]
for label,source in [('cos100','esc_rp1000_cos_w100/best.json'),('cos10','esc_rp1000_cos_w10/best.json'),('rad100','esc_rp1000_radial_w100/best.json')]:
 pin=json.load(open(source))['points']
 for k in [3,4,5,6,7,8,9]:
  name=f'COORD_V20_{label.upper()}_G{k}';d=10**k
  data=dict(name=name,denominator=d,points=[[round(F(x)*d) for x in p] for p in pin])
  path='exact/'+name
  json.dump(data,open(path+'.json','w'),sort_keys=True,separators=(',',':'))
  try:r=audit(data)
  except (AssertionError,ValueError) as exc:
   z=dict(name=name,error=repr(exc));rows.append(z);print(z,flush=True);continue
  json.dump(r,open(path+'_REPORT.json','w'),sort_keys=True,separators=(',',':'))
  v=F(r['volume']);center=tuple(map(F,r['centroid']));p=[sub(tuple(F(x,r['denominator']) for x in q),center) for q in r['vertices']]
  R2=max(dot(x,x) for x in p);r2=min((F(q[3],r['denominator'])-dot(q[:3],center))**2/dot(q[:3],q[:3]) for q in r['planes'])
  tp=sum(F(b['gap']) for b in r['Pbars']);tq=sum(F(b['gap']) for b in r['Qbars'])
  eta=max((1/math.sqrt(float(F(b['death'])))-1/math.sqrt(float(F(b['birth']))))/2 for b in r['Qbars']) if r['Qbars'] else 0
  z={x:r[x] for x in ['name','V','E','F','C','strict','weak','primitive_zero','common_centered_denominator_bits']}
  z.update(TP=float(tp)/float(v)**(2/3),TQ=float(tq)*float(v)**(2/3),etaHat=eta/float(v)**(1/3),rR=math.sqrt(float(r2/R2)))
  rows.append(z);print(json.dumps(z),flush=True)
  json.dump(rows,open('EXACT_FREEZE_SUMMARY.json','w'),sort_keys=True,separators=(',',':'))
```

## Mathematical and numerical limits
The radial graph uses all input points, including possible interior points, and QHull's triangulated-facet normals. Exact complete-chord H0 theory tolerates redundant points, but floating near-coincidence and cancellation still matter. Displayed V/E/F from these scripts are numerical, not the maximal-incidence certificate. Numerical bar significance threshold1e-10 is not an exact-zero predicate. Escape flow suppresses self/near-coincident choices at length1e-12 times the maximum norm; it can artificially make a near-duplicate negative witness nearly zero, especially in the radial normalization. A penalty near2e-8 therefore does not mean own110; observed cases retained a deep Q basin. The exact independent-grid freeze and full face/edge/vertex inequalities, not small numerical energy, establish the retained own211 constructions.
