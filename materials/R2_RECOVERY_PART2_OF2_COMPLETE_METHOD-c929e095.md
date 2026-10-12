# material-c929e0957987

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 2/2: R2_NONLINEAR_ESCAPE_RETRACTION complete executed source
Part1 [internal-source-reference],5993B,SHAca3ccf961d925f03a8bd39769587eb3967434dd8dd501a9b8d888a1ef1664a97 preserves four literal rational endpoint controls independently of optimizer reproducibility. Fine/G8/G7 own211 weak000,C336;G6 own11/14/23. No110. The method reduces the normalized sole Q-bar depth (birth-death)/birth, not the unnormalized difference.

## Dependencies and observations
Exact numerical input: SQP1_G10.json2188B SHA923be5aff0bdd96b9fd9a654c7e445817708a039f0a6ff0de582ffdfb48444f8 from complete recover_sqp1.py3205B SHA08be2f33043aa6a882618c07c11105cf48c395ddf27214635be25b383ec76bdb in [internal-source-reference],SQP1_RECOVERY_PART1_OF2_EXACT_CONTROLS.md5700B SHA67aade110691f4aa1388cc5ec2818700ccf1bbab80a8b48e789c5d9560e68413. Exact endpoint auditor: exact_poly.py6134B SHA898f77989193886996d6f2dc121ccdfdf611b8a9ac52fd3207557eac6a69c0c4 in [internal-source-reference],13684B SHA2b1c5045a6bac634a6858e76e723cf3820fe4185a0ef3253bb1a845d696b84e2. These dependencies and both R2 parts close the recovery capsule. No omitted helpers or old optimizer module needed: complete geometric core and optimizer below.
CPython3.13.5,numpy2.3.3,scipy1.16.1,torch2.8.0+cu128 CPUfloat64,torchthreads1. No RNG. OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1. All defaults explicitly recorded in source. --steps60 is nondefault, --record10 explicitdefault. Sorted livehull faces/edges, actual filled volume centroid, live P/Q witness reselection and normalized escape (x_i·(x_j−x_i))/||x_i||². At each proposed objective step up to8 nonlinear correction QPs reselect hull/centre/witnesses. QP ftol1e-13,maxiter100,rownormalization,minnorm objective. Positive1e-7 escape target,2e-9 feasible tolerance, radius.002→.01 max,repair_radius.005. Trial retraction may exceed single raw step radius; observed actual infinitymoves .0015016027897294692 to .006735090801944409. The earlier tangent-only SQP1 did not have this retraction.

Write source blocks verbatim with LF final newline. escape_core_v2.py4657B SHA1e363702f3e1bb4310426ca40f02d1ad705c9ba9314e9690358ce6d20bd55f4b; escape_retract_v2.py5256B SHA106228465cf7665ed066ebff8f17e85c59f8db616c320edfac05cb6fb5afdc32. Commands:
```
python -B -S recover_sqp1.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python escape_retract_v2.py SQP1_G10.json R2 --steps 60 --record 10
python -B -S exact_poly.py R2_BEST.json
python -B -S recover_r2.py
python -B -S exact_poly.py R2_G8.json
python -B -S exact_poly.py R2_G7.json
python -B -S exact_poly.py R2_G6.json
```
Observed: 61 trace states,60acceptedsteps comprising1initialrepair+59objective steps, allobjectivealpha1. Float RETRACT_FINISHED 61 60 0.3860491795207218; exact fineQdepth0.3860491795645384 versus exactinput0.44768655918729555. No proof of global convergence or elimination of remaining finite Q basin. R2_BEST.json2179B SHA119fa76fbc2ee00387cba4d488be9a5876484e64f78f734448674ac59a327bb4; R2_TRACE.json35895B SHAc7c15f9a008cd7b6e03d4a3784cece3c779977b25a9e415adefb51a1f487898b. Exactaudit and allcoarsefile receipts inpart1. Initial execution imported same geometry from full oldmodule; extracted complete core below, changed import and replayed identical60steps withprefixR2R. Observed all58rationalpointrows identical and samefloatterminalmarker. PrefixR2R changes bodyname/traceprefix but not coordinates. Source and actual trace were read from runtime before immutable preservation, not inferred from a remembered hash. No claim of byteidentity with old SQP1 optimizer.
Float forest suppresses diagnostic depths≤1e-14 only for proposal guidance. Exact_poly retains every exactpositive bar and censuses strict versus closed weak equilibria and primitivezeros. Core ConvexHull triangulates its numeric input; exact_poly rejects nontriangular maximalfacets rather than certifying a fake simplicial complex. All four observed R2 controls truly simplicial. Exact verification uses one full exacthull engine; do not call it two independent hull checks.

## escape_core_v2.py
```python
"""Live own-centroid core for nonlinear escape retraction, numerical only.
Float search only. Every candidate needs exact_poly.py rational audit.
Deterministic with numpy/scipy/torch thread count 1; no RNG is used.
"""
import argparse,json,os,sys,time
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize, LinearConstraint, Bounds
import torch

torch.set_default_dtype(torch.float64)
torch.set_num_threads(1)

def complex_of(x):
    hull=ConvexHull(x)
    fs=[]
    for f,eq in zip(hull.simplices,hull.equations):
        f=sorted(map(int,f))
        if np.dot(np.cross(x[f[1]]-x[f[0]],x[f[2]]-x[f[0]]),eq[:3])<0:f[1],f[2]=f[2],f[1]
        fs.append(f)
    fs.sort(key=lambda f:sorted(f))
    edges={}
    for k,f in enumerate(fs):
        for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(k)
    assert all(len(v)==2 for v in edges.values())
    pe=sorted(edges);qe=[tuple(edges[e]) for e in pe]
    active=sorted(set(i for e in pe for i in e))
    assert len(active)-len(pe)+len(fs)==2
    return np.array(fs),np.array(pe),np.array(qe),np.array(active)

def geometry(x,fs):
    tri=x[fs];a,b,c=tri[:,0],tri[:,1],tri[:,2]
    ds=(a*torch.linalg.cross(b,c)).sum(1);W=ds.sum()
    center=(ds[:,None]*(a+b+c)).sum(0)/(4*W)
    P=x-center
    n=torch.linalg.cross(b-a,c-a)
    height=(n*(a-center)).sum(1)
    Q=n/height[:,None]
    return P,Q,center,W/6

def forest(X,edges):
    R=(X*X).sum(1);ds=X[edges[:,1]]-X[edges[:,0]]
    den=(ds*ds).sum(1)
    t=np.clip(-(X[edges[:,0]]*ds).sum(1)/den,0,1)
    gate=((X[edges[:,0]]+t[:,None]*ds)**2).sum(1)
    par=list(range(len(X)));peak=par[:];members=[{i} for i in par];bars=[]
    def find(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    for k in sorted(range(len(edges)),key=lambda k:(-gate[k],*edges[k])):
        a,b=map(int,edges[k]);u,v=find(a),find(b)
        if u==v:continue
        if (R[peak[u]],peak[u])<(R[peak[v]],peak[v]):u,v=v,u
        birth=R[peak[v]];depth=(birth-gate[k])/birth
        if depth>1e-14:bars.append(dict(peak=peak[v],elder=peak[u],edge=k,depth=float(depth),component=sorted(members[v])))
        par[v]=u;members[u]|=members[v]
    return sorted(bars,key=lambda b:-b['depth'])

def witnesses(X,edges,allowed,active=None):
    nb=[[] for _ in X]
    for a,b in edges:nb[a].append(b);nb[b].append(a)
    if active is None:active=range(len(X))
    rr=(X*X).sum(1);pairs=[];margins=[];roots=[]
    for i in active:
        js=sorted(nb[i])
        v=np.array([np.dot(X[i],X[j]-X[i])/rr[i] for j in js])
        j=js[int(np.argmax(v))]
        if max(v)<0:roots.append(int(i))
        if i not in allowed:pairs.append([int(i),int(j)]);margins.append(max(v))
    return np.array(pairs,dtype=int).reshape(-1,2),np.array(margins),roots

def state(x,margin):
    fs,pe,qe,active=complex_of(x)
    with torch.no_grad():
        P,Q,c,vol=geometry(torch.tensor(x),torch.tensor(fs));P=P.numpy();Q=Q.numpy()
    pb=forest(P,pe);qb=forest(Q,qe)
    pr=int(active[np.argmax((P[active]**2).sum(1))]);qr=int(np.argmax((Q**2).sum(1)))
    allowed=[qr]+([qb[0]['peak']] if qb else [])
    wp,mp,ur=witnesses(P,pe,[pr],active)
    wq,mq,sr=witnesses(Q,qe,allowed)
    m=np.r_[mp,mq]
    return dict(fs=fs,pe=pe,qe=qe,active=active,P=P,Q=Q,center=c.numpy(),volume=float(vol),pb=pb,qb=qb,pr=pr,qr=qr,allowed=allowed,wp=wp,wq=wq,m=m,S=len(sr),U=len(ur),Sids=sr,Uids=ur,objective=sum(b['depth'] for b in qb),depth=qb[0]['depth'] if qb else 0.,violation=max(0.,float(margin-m.min())),E=len(pe),V=len(active),F=len(fs))

def tensor_values(flat,shape,s):
    P,Q,_,_=geometry(flat.reshape(shape),torch.tensor(s['fs']))
    values=[]
    for X,pair in ((P,s['wp']),(Q,s['wq'])):
        a=X[pair[:,0]];b=X[pair[:,1]]
        values.append((a*(b-a)).sum(1)/(a*a).sum(1))
    if s['qb']:
        b=s['qb'][0];a0,a1=s['qe'][b['edge']];a,d=Q[a0],Q[a1]-Q[a0]
        t=torch.clamp(-(a*d).sum()/(d*d).sum(),0,1);death=((a+t*d)**2).sum();birth=(Q[b['peak']]**2).sum()
        objective=1-death/birth
    else:objective=P.sum()*0
    return torch.cat((objective.reshape(1),*values))

def linearize(x,s):
    z=torch.tensor(x.reshape(-1),requires_grad=True)
    fun=lambda z:tensor_values(z,x.shape,s)
    values=fun(z).detach().numpy()
    J=torch.autograd.functional.jacobian(fun,z,vectorize=True).detach().numpy()
    assert np.isfinite(J).all()
    return values[0],J[0],values[1:],J[1:]

def write_body(x,path,digits):
    d=10**digits
    raw=dict(denominator=d,name=path.stem,points=np.rint(x*d).astype(np.int64).tolist())
    path.write_text(json.dumps(raw,separators=(',',':'))+'\n')
```

## escape_retract_v2.py
```python
"""Own-mass escape SQP with live nonlinear feasibility retraction.
Requires escape_core_v2.py; numerical nominees need exact audit.
"""
import argparse,json,hashlib,os,sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize,LinearConstraint,Bounds
import escape_core_v2 as v

def qp(target,A,lb,radius):
    scale=np.maximum(np.linalg.norm(A,axis=1),1e-12)
    AA=A/scale[:,None];bb=lb/scale
    ans=minimize(lambda d:.5*np.dot(d-target,d-target),np.zeros_like(target),jac=lambda d:d-target,
        constraints=[LinearConstraint(AA,bb,np.inf)],bounds=Bounds(-radius,radius),
        method='SLSQP',options=dict(ftol=1e-13,maxiter=100,disp=False))
    return ans.x,bool(ans.success),float(np.min(A@ans.x-lb))

def retract(y,args,radius):
    """Reselect hull/centroid/witnesses; minimum corrections, live violation descent."""
    z=y.copy();log=[]
    for k in range(args.corrections+1):
        try:s=v.state(z,args.margin)
        except (ValueError,AssertionError,RuntimeError):return None,log
        log.append(dict(k=k,violation=s['violation'],depth=s['depth'],E=s['E']))
        if s['E']>249:return None,log
        if s['violation']<=args.feasible:return z,log
        if k==args.corrections:break
        _,g,m,A=v.linearize(z,s)
        d,ok,slack=qp(np.zeros_like(g),A,args.margin-m,min(radius,args.repair_radius))
        log[-1].update(qp=ok,slack=slack,norm=float(np.linalg.norm(d)))
        if slack < -1e-7:return None,log
        accepted=False
        for alpha in (1.,.5,.25,.125,.0625):
            trial=z+alpha*d.reshape(z.shape)
            try:t=v.state(trial,args.margin)
            except (ValueError,AssertionError,RuntimeError):continue
            if t['E']<=249 and (t['violation']<s['violation']*.8 or t['violation']<=args.feasible):
                z=trial;accepted=True;break
        if not accepted:break
    return None,log

def run(args):
    raw=json.loads(Path(args.input).read_text());x=np.array(raw['points'],float)/raw['denominator']
    x=x[v.ConvexHull(x).vertices]
    prefix=Path(args.prefix);prefix.parent.mkdir(parents=True,exist_ok=True)
    radius=args.radius;trace=[];attempts=[];accepted=0;best=float('inf')
    def save(x,tag):
        v.write_body(x,Path(str(prefix)+'_'+tag+'.json'),args.digits)
        Path(str(prefix)+'_'+tag+'_HEX.json').write_text(json.dumps([[float(a).hex() for a in row] for row in x],separators=(',',':'))+'\n')
    for it in range(args.steps+1):
        s=v.state(x,args.margin)
        rec=dict(it=it,V=s['V'],E=s['E'],F=s['F'],S=s['S'],U=s['U'],P=len(s['pb']),Q=len(s['qb']),depth=s['depth'],violation=s['violation'],radius=radius)
        trace.append(rec)
        if s['violation']<=args.feasible and s['S']<=2 and s['U']==1 and s['depth']<best:
            best=s['depth'];save(x,'BEST')
        if it%args.record==0 or it==args.steps:print(json.dumps(rec),flush=True);save(x,f'IT{it:04d}')
        if it==args.steps or (s['S']==1 and s['U']==1 and s['violation']<=args.feasible):break
        if s['violation']>args.feasible:
            z,logs=retract(x,args,radius)
            attempts.append(dict(it=it,kind='initial_repair',logs=logs))
            if z is not None:x=z;accepted+=1;continue
            radius*=.5;continue
        _,g,m,A=v.linearize(x,s)
        target=-args.drive*radius*np.sqrt(len(g))*g/max(np.linalg.norm(g),1e-30)
        step,ok,slack=qp(target,A,args.margin-m,radius)
        okay=False
        for alpha in (1.,.5,.25,.125):
            y=x+alpha*step.reshape(x.shape)
            z,logs=retract(y,args,radius*alpha)
            item=dict(it=it,alpha=alpha,qp=ok,slack=slack,logs=logs,accepted=False)
            attempts.append(item)
            if z is None:continue
            t=v.state(z,args.margin)
            if t['depth']<s['depth']-args.improve and t['S']<=2 and t['U']==1:
                x=z;okay=True;accepted+=1;item['accepted']=True
                rec['accepted_alpha']=alpha;rec['move_inf']=float(np.max(np.abs(x-y+alpha*step.reshape(x.shape))))
                radius=min(args.maxradius,radius*(1.15 if alpha>=.5 else .7));break
        rec['accepted']=okay
        if not okay:radius*=.5
        if radius<args.minradius:
            print('RETRACT_LOCAL_STOP',it,flush=True);break
    save(x,'FINAL')
    Path(str(prefix)+'_TRACE.json').write_text(json.dumps(dict(args=vars(args),trace=trace,attempts=attempts),sort_keys=True,separators=(',',':'))+'\n')
    print('RETRACT_FINISHED',len(trace),accepted,best,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('prefix')
    p.add_argument('--steps',type=int,default=100);p.add_argument('--radius',type=float,default=.002)
    p.add_argument('--maxradius',type=float,default=.01);p.add_argument('--minradius',type=float,default=1e-9)
    p.add_argument('--margin',type=float,default=1e-7);p.add_argument('--feasible',type=float,default=2e-9)
    p.add_argument('--corrections',type=int,default=8);p.add_argument('--repair-radius',type=float,default=.005)
    p.add_argument('--drive',type=float,default=1.);p.add_argument('--digits',type=int,default=10)
    p.add_argument('--record',type=int,default=10);p.add_argument('--improve',type=float,default=1e-11)
    run(p.parse_args())
```
