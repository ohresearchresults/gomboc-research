# material-a80b43b9b03e

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Recovery capsule part 2/2: complete producing method
Object identity SQP1_HARD_ESCAPE_V1. Part1 is [internal-source-reference], SQP1_RECOVERY_PART1_OF2_EXACT_CONTROLS.md5700B,SHA67aade110691f4aa1388cc5ec2818700ccf1bbab80a8b48e789c5d9560e68413. It preserves literal exact checkpoints and deterministic integer recovery for G6/G7/G8/G10, including exact negative coarse controls.

Required exact source input: [internal-source-reference], GROWTH_V2_THREE_EXACT_CONTROLS_211_222_413.md13762B,SHA4677b31400c27db8d56f58f5fd5fa01a121e726b2d0c37db72e661df0b93c1b3. Extract its COMPLETE G2_LOG_BEST_G8.json2590B SHA0a6617d3c9b5ef15e6054429a78d6e31357c277e70362cdb0c077c40e00c829b, not a renamed or averaged body. It contains83inputrows of which58 are extreme. Required exact audit unit: [internal-source-reference], JB_C168_OWN211_EXACT_RECOVERY_V1.md13684B SHA2b1c5045a6bac634a6858e76e723cf3820fe4185a0ef3253bb1a845d696b84e2; exact_poly.py6134B SHA898f77989193886996d6f2dc121ccdfdf611b8a9ac52fd3207557eac6a69c0c4. These owned source materials plus the two SQP1 parts are the complete dependency set.

Write following complete module as escape_sqp_v1.py, final LF, expected8708B SHA0d3a8b67d565cb35db3acde0b0f785e2b95d74c53d5f4e0c62c473fe9d8886d0. Original execution used identical bytes under escape_sqp.py. Observed environment for THIS execution: Python3.13.2,numpy2.1.3,scipy1.15.3,torch2.6.0+cpu. No RNG. Torchfloat64 and singlethread. Execute:
```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python escape_sqp_v1.py G2_LOG_BEST_G8.json sqp1 --steps 60 --record 10
python exact_poly.py sqp1_BEST.json
```
All other options defaults, explicitly: radius.002,maxradius.01,minradius1e-10,margin1e-7,feasible2e-9,drive1,repair-drift.002,digits8; record10 replaces25; steps60 replaces300. SLSQPftol1e-12,maxiter150,uniformslackpenalty100,initialpruneConvexHull.vertices. Trace first mainQ.4772196433841408,violation.0003069209574414454,S4U1; it10 mainQ.45031138451008523,S2U1; it60 mainQ.44768655913405125,violation1.4235997e-9,S2U1.60acceptedsteps. Expected terminal ESCAPE_SQP_FINISHED 61 60 best 0.44768655913405125. Floating optimization may be platform-sensitive; Part1 exact recovery is the platform-independent scientific endpoint, rather than an assertion that arbitrary library versions reproduce optimization bits.

Result sqp1_BEST.json1839B SHA354f11698c74a6e37d28f43c7934e86f9cc3500f6f42af9ce18f4feed9631719; audit6054B SHA9b36a9a21609216eaf96e1b0d30f2ed8251e8fc6451f80e84000edffff588819; EXACT_POLY_AUDIT_PASS. Exact own211/weak000/zero000 at C336, NOT110. This simultaneously eliminates two genuine tinyQ bars of the source and reduces the senior Qdepth to.44768656497521575. Part1 exactG10 control is derived from floating best rounded at1e10 then ties-even integer rescaling; reproducing this fine control does not require rerunning optimizer.

Method: rebuild true floating hull/incidence and integrate actual uniform volume centroid at each candidate; choose a positive radial escape witness for every nonallowed primal/polar vertex. Allow one P root and two Q roots (global and senior finite). SQP closest-step enforces linearized direct escape inequalities, followed by acceptance using recomputed actual geometry. Repair is prioritized over lowering senior barrier. Constraint witness switching and physical incidence changes are permitted. Tiny bars are real; the1e-14 forest filter is ONLY floating search guidance, never the exact certificate. E≤249 gate is physical simplicial hull edges. No frozen chosen center or nominal density. The accepted endpoint keeps a genuine senior Qbar and must not be advertised as110.

Observed methodological limit: simple line acceptance shrinks trust radius to about8.157e-6 while active nonlinear escape constraints become tangent. Next meaningful direction is a live nonlinear/second-order feasibility correction after an objective step, not merely increasing a scalar penalty or erasing small bars.

## escape_sqp_v1.py
```python
"""Live-own-centroid P/Q escape-constrained sequential quadratic search.
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

def run(args):
    raw=json.loads(Path(args.input).read_text());x=np.array(raw['points'],dtype=float)/raw['denominator']
    x=x[ConvexHull(x).vertices]
    prefix=Path(args.prefix);prefix.parent.mkdir(parents=True,exist_ok=True)
    trace=[];radius=args.radius;best=np.inf;accepted=0
    for it in range(args.steps+1):
        s=state(x,args.margin)
        rec=dict(iteration=it,V=s['V'],E=s['E'],F=s['F'],S=s['S'],U=s['U'],P=len(s['pb']),Q=len(s['qb']),depth=s['depth'],violation=s['violation'],radius=radius)
        if s['S']==2 and s['U']==1 and s['violation']<args.feasible and s['depth']<best:
            best=s['depth'];write_body(x,Path(str(prefix)+'_BEST.json'),args.digits)
            np.save(str(prefix)+'_BEST.npy',x)
        if it%args.record==0 or it==args.steps:
            print(json.dumps(rec),flush=True)
            write_body(x,Path(str(prefix)+f'_IT{it:04d}.json'),args.digits)
        trace.append(rec)
        if it==args.steps or (s['S']==1 and s['U']==1 and s['violation']<args.feasible):break
        objective,g,m,A=linearize(x,s)
        # Closest-step QP: repair first; when feasible follow the basin objective.
        repair=s['violation']>args.feasible
        gn=np.linalg.norm(g)
        target=np.zeros_like(g) if repair else -args.drive*radius*np.sqrt(len(g))*g/max(gn,1e-20)
        lb=args.margin-m
        opts=dict(ftol=1e-12,maxiter=150,disp=False)
        qp=minimize(lambda d:.5*np.dot(d-target,d-target),np.zeros_like(g),jac=lambda d:d-target,
            constraints=[LinearConstraint(A,lb,np.inf)],bounds=Bounds(-radius,radius),method='SLSQP',options=opts)
        if np.min(A@qp.x-lb)<-1e-7:
            # A minimax feasibility step, with nonnegative uniform slack.
            A2=np.c_[A,np.ones(len(m))]
            z0=np.r_[np.zeros_like(g),max(s['violation'],args.margin)]
            qp2=minimize(lambda z:.5*np.dot(z[:-1],z[:-1])+100*z[-1],z0,
                jac=lambda z:np.r_[z[:-1],100.],constraints=[LinearConstraint(A2,lb,np.inf)],
                bounds=Bounds(np.r_[np.full(len(g),-radius),0.],np.r_[np.full(len(g),radius),np.inf]),method='SLSQP',options=opts)
            step=qp2.x[:-1]
        else:step=qp.x
        okay=False
        for alpha in (1.,.5,.25,.125,.0625,.03125,.015625,.0078125):
            trial=x+alpha*step.reshape(x.shape)
            try:st=state(trial,args.margin)
            except (ValueError,AssertionError,RuntimeError):continue
            if st['E']>249:continue
            if repair:
                cond=(st['violation']<s['violation']*.995 or st['violation']<args.feasible) and st['depth']<s['depth']+args.repair_drift
            else:
                cond=st['violation']<args.feasible and st['depth']<s['depth']-1e-12
            if cond:
                x=trial;okay=True;accepted+=1
                radius=min(args.maxradius,radius*(1.1 if alpha>=.5 else .8));break
        trace[-1].update(accepted=okay,repair=repair,qp_success=bool(qp.success),stepnorm=float(np.linalg.norm(step)))
        if not okay:radius*=.5
        if radius<args.minradius:
            print('ESCAPE_SQP_LOCAL_STOP',it,s['depth'],s['violation'],flush=True);break
    write_body(x,Path(str(prefix)+'_FINAL.json'),args.digits)
    Path(str(prefix)+'_TRACE.json').write_text(json.dumps(trace,sort_keys=True,separators=(',',':'))+'\n')
    print('ESCAPE_SQP_FINISHED',len(trace),accepted,'best',best,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('prefix')
    p.add_argument('--steps',type=int,default=300);p.add_argument('--radius',type=float,default=.002)
    p.add_argument('--maxradius',type=float,default=.01);p.add_argument('--minradius',type=float,default=1e-10)
    p.add_argument('--margin',type=float,default=1e-7);p.add_argument('--feasible',type=float,default=2e-9)
    p.add_argument('--drive',type=float,default=1.);p.add_argument('--repair-drift',type=float,default=.002)
    p.add_argument('--digits',type=int,default=8);p.add_argument('--record',type=int,default=25)
    run(p.parse_args())
```
