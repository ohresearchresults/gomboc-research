# material-8a7d43cbd500

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# JOINT75 affine/projective numerical methods — complete recovery source

Literal geometry is R62J_JOINT75_G7_TRUE75 from figure-0549 (SHA f996fa67a06c542cbe559aadce39ce5f7b2f06b81a609a4a55dd3f03d9291605). These coordinator computations produced no own110 and no new exact construction. Affine images transport the filled centroid exactly; projective images reintegrate it. This is finite floating evidence, not an all-affine/projective exclusion. The event-ray screen uses floating quadratic roots, not certified real-root isolation. The bar reporter discards depths <=1e-14 for numerical diagnostics; it is NOT a final strict/weak certificate. Full-pair strict vertex predicates are separately reported without that bar tolerance. Exact moderate-affine exclusion is in [internal-source-reference], not derived from these numerical searches.

## Environment correction
The live execution environment is CPython3.13.5 (GCC14.2.0), NumPy2.3.5, SciPy1.17.0, float64 and OPENBLAS_NUM_THREADS=1. An earlier recovery summary incorrectly identified3.11.8/1.24.0/1.14.1. The exact angular capsule's annotation 'tested CPython3.11.8' is therefore corrected to 'tested CPython3.13.5'; its integer/rational source and output hashes remain those stored, with no mathematical change. Older provisional floating summary values are superseded by the observations below and their regenerators.

## Reconstruct and replay
Save each complete file block below under its stated filename, preserving the last newline. Coordinates are integer rows divided by10000000. No other source dependency or checkpoint is needed. Run in that directory:

```
export OPENBLAS_NUM_THREADS=1
python -B orbit.py
python -B orbit.py 3 2581 5
python -B constrained.py 5 100
python -B constrained.py 8 100
python -B escape.py 8 9421 3 0.0001
python -B rays.py 0 180
python -B metric_milp.py P 6 10 3
```

The baseline is P=[.10155678447201522], Q=[.0677140016997031], U=[6,62], S=[1,97] in SciPy's temporary face order, E219. Those S IDs are NOT the canonical parent face IDs3,62. The numerical source's reference uses actual parent COM, not a nominated centre.

Observed source manifest (bytes SHA256):
primary.json 2044 72ab95b77af39a8a87444c47e05a1e24b78c0bc88a70281f365715f30d502fde
orbit.py 3786 4ddf500002323a1105af89ee3b0c5cd1e0e3e4d46b77c3c20867a5e5308cc574
constrained.py 2876 73cccc686ea62de8addd1cf81ee974fcc2a95b2f2419050333c973956de36286
escape.py 1512 d93c69d1e911214cb3e11610dd0f2bd0534a43d7353e299928e82962a9b78242
rays.py 3056 2580fa94596b8327650a9cb0f291a3f63ef88e30aca4f1102ee87230e1abb732
metric_milp.py 2619 455c3f2d69492b6e7b051d711f1200562d60d3cad4b7d3d72858ca94756e3105

Observed output manifest (regenerable; floating optimizers and time-limited MILP need not be bit-identical on other platforms):
search_d5_s2581.json 10006 1e579ab9d278342b5db7a99cee09e42930baab8e07c7412f05a8d0526587a1bc
constrained_d5.json 7681 6ffcd3a60a24c51e9a582b9edcc6efa359fc953561e6407fee56170cb9f572f1
constrained_d8.json 4688 6a123d2e00618b4aae3c6893293bc40c0f41f6402703cee07652caeea7ab622e
escape_d8_s9421_t0.0001.json 8497 3c33d993464ec8125a15bc2265223df52ce00de0b205f5a77afd870459914356
rays_0_180.json 369055 6688ed190fffb9351124c88b82b7b1addd240f9428e78d5bcecee6e42b8f0dac
milp_P_6.json 142 80bf523deeb29806ead75317f63fd941ecdc2e737d96b1732a55e4c7a34ce99a

Observed findings: three Nelder-Mead runs ended at (S,U)=(5,3),(13,18),(10,18), with sumP/sumQ respectively .10155920520869122/.06770440451638737, .152402759275305/.2543719982670304, .13162160787547195/.2688506209056303. They fragmented, not improved to110.
Class-preserving affine descent accepted11 small steps, final p=[-5.0184926780954236e-6,3.404547245879331e-6,-2.3995228115869865e-6,-1.3321636406717267e-6,-2.812034108957382e-6], P=.1015533431686102,Q=.06771069307953748. Projective-plus-affine descent accepted5 steps, p=[-4.139565320614072e-6,5.189867011072356e-6,-1.1133610967395452e-6,3.255952736770119e-6,-4.338749072877985e-6,-1.807607084678147e-6,-3.910477968071674e-6,4.23640064526541e-6], P=.10154780104947436,Q=.06771131073834358. Both remained numerically222, not exact promoted endpoints.
The three8D escape-loss runs ended (S,U)=(8,13),(8,13),(2,4), with sumP/sumQ=.10796274829978691/.09658269092175331, .10796281139480002/.09658379039620568, .9156874252236255/.8904000352698115. The last small local loss1.695371319081461e-6 hides DEEP genuine bars, not negligible defects. Other losses8.753185181323444e-5 and8.753185181782663e-5.
All180 deterministic gate rays contained121097 computed sign-change events. Across all sampled open event cells minU2,minS2,min(S+U)4. This does not exclude all affine metrics, omitted zero-boundary cells, or roots lost by floating near-coincidence.
The P-root6 metric MILP hit its10-second limit without an incumbent: [{'status':1,'message':'Time limit reached. (HiGHS Status 13: model_status is Time limit reached; primal_status is None)'}]. No infeasibility or feasibility conclusion. Binary metric search is only an outer PSD-cut relaxation until a positive definite candidate is checked.

## File: primary.json
```json
[[-11310213,-3802031,232661],[-11269293,-2834032,-2182730],[-10855182,-2246500,-3911998],[-10128821,-1814868,-5467871],[-9452382,-6834502,6456555],[-9308206,-1555414,-6662777],[-8712882,-8006246,8846843],[-8693078,-1373304,-7380329],[-7797905,-1286403,-8181129],[-6681453,-1307873,-8916622],[-6352338,2020313,-1146993],[-5892536,2295258,-71116],[-5592263,2241235,541206],[-5425338,-1474781,-9487378],[-5280741,2171200,1073969],[-4959361,3312877,-1863739],[-4453446,1994305,2115702],[-4311479,345947,4048866],[-4305575,1694912,2608464],[-4237167,1203950,3206121],[-3820955,4252385,-2139686],[-3661038,4074852,-884602],[-3623465,-1644023,-10021566],[-3190033,811977,3827673],[-3155609,4102561,85230],[-3074935,4483432,-2851622],[-2953571,-1851896,-10161171],[-2718323,668005,3934224],[-2651732,122199,4295157],[-2302445,4621821,-3324860],[-2248430,-2037367,-10247983],[-2145336,4388373,461753],[-1938256,3964861,1093487],[-1561887,3760992,1454978],[-1502148,-2223378,-10275715],[-1278721,4758931,-3663608],[-1049751,3727821,1606020],[-740759,-2457388,-10231458],[-298044,4806779,-3669461],[-159770,3872224,1576892],[-121991,838112,3483867],[39249,-2666243,-10115526],[91753,589879,3521150],[725989,729286,3291554],[822613,-2865673,-9923443],[847151,1601384,2948252],[1257541,4150503,1429262],[1400720,4852019,-3212547],[1599055,-3043575,-9655675],[2331916,-2317243,-9420429],[2351892,-3267823,-9302290],[2947803,5018418,-438633],[3091632,-3449326,-8871363],[3252567,4572542,973174],[3518927,-4445832,-8207140],[3801752,-3598386,-8365506],[3886092,3932529,1241770],[4317265,3420766,1352627],[4466143,-3720508,-7791824],[4524082,-5334292,-6695320],[4622668,3053371,1323427],[4905967,2678528,1274548],[5061533,-3853293,-7158199],[5166891,2298083,1206990],[5506198,-4926808,-5369878],[5525767,-801605,-6004784],[5644371,1606910,926729],[6018142,937609,612094],[6137534,-4326615,-4182924],[6330239,239389,230320],[6547165,-3582767,-3087182],[6574260,-489010,-228500],[6738672,-1246564,-776981],[6751376,-2814918,-2197016],[6805726,-2026966,-1429050]]
```

## File: orbit.py
```python
import json, numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from pathlib import Path
I=np.array(json.loads((Path(__file__).parent/'primary.json').read_text()),dtype=np.int64)
V=I/1e7
G0=np.array([-53286920506055854442174018051,-42633799180986064597953397917,-43819041531080084398689329023],dtype=float)/301728380651199510841280000000
X=V-G0
H=ConvexHull(X)
F=H.simplices.copy()
E=np.array(sorted(set(tuple(sorted((int(f[k]),int(f[(k+1)%3])))) for f in F for k in range(3))))
DE=np.array(sorted(set(tuple(sorted((i,int(j)))) for i,ns in enumerate(H.neighbors) for j in ns)))
Y=H.equations[:,:3]/(-H.equations[:,3,None])

def matrix(p):
    # determinant-one lower triangular affine map, G=A^T A
    a,b,c,d,e=p[:5]
    return np.array([[np.exp(a),0,0],[c,np.exp(b),0],[d,e,np.exp(-a-b)]])

def project(p):
    if len(p)<8: return X,Y
    den=1+X@np.asarray(p[5:8]);
    if den.min()<=.02: raise ValueError('projective pole')
    v=X/den[:,None]
    # exact combinatorial orientation inherited; fill volumes with signed tetrahedra
    fs=F.copy(); vv=v[fs]; d=np.linalg.det(vv)
    # original scipy simplices have mixed orientation; outward det signs inherited
    ori=np.sign(np.linalg.det(X[fs])); w=d*ori
    cent=(w[:,None]*vv.sum(axis=1)).sum(axis=0)/(4*w.sum())
    v=v-cent
    n=np.cross(v[fs[:,1]]-v[fs[:,0]],v[fs[:,2]]-v[fs[:,0]])
    hh=np.einsum('ij,ij->i',n,v[fs[:,0]])
    return v,n/hh[:,None]

def bars(v,edges):
    r=(v*v).sum(axis=1)
    vv=v[edges[:,0]]; dd=v[edges[:,1]]-vv
    t=np.clip(-np.einsum('ij,ij->i',vv,dd)/np.einsum('ij,ij->i',dd,dd),0,1)
    z=vv+t[:,None]*dd; h=(z*z).sum(axis=1)
    order=np.argsort(-h,kind='stable'); root=np.arange(len(v)); peak=root.copy();out=[]
    def find(i):
        while root[i]!=i:
            root[i]=root[root[i]];i=root[i]
        return i
    for k in order:
        a,b=map(find,edges[k])
        if a==b:continue
        if (r[peak[a]],-peak[a])<(r[peak[b]],-peak[b]):a,b=b,a
        dep=max(0.,1-h[k]/r[peak[b]])
        if dep>1e-14:out.append((dep,int(peak[b]),int(k),float(r[peak[b]]),float(h[k])))
        root[b]=a
    return sorted(out,reverse=True)

def scores(p,full=False):
    a=matrix(p)
    try:x,y=project(p)
    except ValueError:return None
    x=x@a.T;y=y@np.linalg.inv(a)
    bp=bars(x,E);bq=bars(y,DE)
    if full:
        def roots(v):
            gram=v@v.T; rr=np.diag(gram);z=gram-rr[:,None];np.fill_diagonal(z,-np.inf)
            return np.where(z.max(axis=1)<0)[0].tolist()
        return dict(p=list(map(float,p)),P=bp,Q=bq,U=roots(x),S=roots(y),E=len(E),A=a.tolist())
    return sum(b[0]**.5 for b in bp),sum(b[0]**.5 for b in bq)

def objective(p,kind='sum'):
    s=scores(p)
    if s is None:return 1e4+sum(np.array(p)**2)
    if kind=='sum':return sum(s)
    if kind=='max':return max(s)+.05*min(s)
    if kind=='sq':return sum(z*z for z in s)
    return s[0]*float(kind)+s[1]
if __name__=='__main__':
    import sys
    if len(sys.argv)==1:
        print(json.dumps(scores(np.zeros(5),True),indent=2));quit()
    n=int(sys.argv[1]);seed=int(sys.argv[2]);dim=int(sys.argv[3]) if len(sys.argv)>3 else 5
    rng=np.random.default_rng(seed);out=[]
    for i in range(n):
        z=np.zeros(dim) if i==0 else rng.normal(size=dim)*(.03 if i%3 else .15)
        kind=['sum','max','sq'][i%3]
        res=minimize(lambda p:objective(p,kind),z,method='Nelder-Mead',options={'maxiter':1500,'xatol':1e-10,'fatol':1e-10})
        d=scores(res.x,True);d.update(value=float(res.fun),kind=kind,seed=seed,start=z.tolist(),nit=int(res.nit));out.append(d)
        print(i,kind,res.fun, len(d['S']),len(d['U']),[b[0] for b in d['P']], [b[0] for b in d['Q']],flush=True)
        (Path(__file__).parent/f'search_d{dim}_s{seed}.json').write_text(json.dumps(out,indent=2))
```

## File: constrained.py
```python
from orbit import *
from scipy.optimize import linprog

def shape(p):
    a=matrix(p);x,y=project(p)
    return x@a.T,y@np.linalg.inv(a)

def make_features(p):
    vv=shape(p); assignments=[];signatures=[]
    for v,edges in zip(vv,[E,DE]):
        gram=v@v.T;r=np.diag(gram)
        sc=gram/r[:,None]-1;np.fill_diagonal(sc,-np.inf)
        jj=np.argmax(sc,axis=1); ii=np.where(sc.max(axis=1)>0)[0]
        assignments.append((ii,jj[ii]))
        bp=bars(v,edges)
        if len(bp)!=1: raise ValueError(('not two roots',len(bp)))
        b=bp[0]; signatures.append((b[1],edges[b[2]]))
    return assignments,signatures

def features(p,ass,sig):
    vv=shape(p);out=[];depth=[]
    for v,(ii,jj),(birth,(a,b)) in zip(vv,ass,sig):
        out.extend((np.einsum('ij,ij->i',v[ii],v[jj]-v[ii])/np.einsum('ij,ij->i',v[ii],v[ii])).tolist())
        d=v[b]-v[a];t=-(v[a]*d).sum()/(d*d).sum();z=v[a]+t*d
        depth.append(np.log((v[birth]*v[birth]).sum()/(z*z).sum()))
    return np.array(out+depth)

def go(dim=5,n=100,eps=1e-12):
    p=np.zeros(dim); history=[]
    for it in range(n):
        ass,sig=make_features(p); f=features(p,ass,sig)
        jac=np.array([np.imag(features(p.astype(complex)+1j*1e-24*np.eye(dim)[k],ass,sig))/1e-24 for k in range(dim)]).T
        scale=np.linalg.norm(jac,axis=1);scale[scale<1e-12]=1
        w=-f[:-2]*.8
        best=None
        # own-class preserving trust region with simultaneous log-bar nonincrease
        for trust in [1e-2,1e-3,1e-4,1e-5]:
            AA=np.r_[-jac[:-2]/scale[:-2,None],jac[-2:]/scale[-2:,None]]
            bb=np.r_[-w/scale[:-2], [0.,0.]]
            r=linprog(jac[-2:].sum(axis=0),A_ub=AA,b_ub=bb,bounds=[(-trust,trust)]*dim,method='highs')
            if not r.success:continue
            for alpha in [1,.5,.25,.125,.0625,.03125]:
                q=p+alpha*r.x
                try: ss=scores(q,True)
                except (ValueError,np.linalg.LinAlgError):continue
                if len(ss['U'])!=2 or len(ss['S'])!=2:continue
                new=np.array([sum(np.log(b[3]/b[4]) for b in ss[k]) for k in ['P','Q']])
                if (new<=f[-2:]+1e-12).all() and new.sum()<f[-2:].sum()-1e-13:
                    best=(q,ss,trust,alpha,r.fun);break
            if best:break
        if best is None:
            print('STOP',it,'p',p,'logs',f[-2:],'minmargin',f[:-2].min(),flush=True);break
        p,ss,trust,alpha,cost=best
        history.append(dict(it=it,p=p.tolist(),P=ss['P'],Q=ss['Q'],trust=trust,alpha=alpha,cost=cost))
        if it%10==0:print(dim,it,[z[0] for z in ss['P']],[z[0] for z in ss['Q']],trust,alpha,flush=True)
    (Path(__file__).parent/f'constrained_d{dim}.json').write_text(json.dumps(dict(p=p.tolist(),history=history,final=scores(p,True)),indent=2))
    return p
if __name__=='__main__':
    import sys
    go(int(sys.argv[1]),int(sys.argv[2]) if len(sys.argv)>2 else 100)
```

## File: escape.py
```python
from constrained import *

def esc(p,tau=1e-4):
    try:vvs=shape(p)
    except ValueError:return 1e4+sum(p*p),2*p
    labs=[];ms=[]
    for v in vvs:
        rr=(v*v).sum(1);g=v@v.T/rr[:,None]-1;np.fill_diagonal(g,-np.inf)
        ri=int(rr.argmax());ii=np.arange(len(v));ii=ii[ii!=ri];jj=g.argmax(1)[ii]
        labs.append((ii,jj));ms.extend(g[ii,jj])
    ms=np.array(ms);bad=np.maximum(tau-ms,0)
    cost=float(bad@bad)
    grads=[]
    for k in range(len(p)):
        q=p.astype(complex);q[k]+=1j*1e-24
        gr=[]
        for v,(ii,jj) in zip(shape(q),labs):
            gr.extend(np.imag((v[ii]*(v[jj]-v[ii])).sum(1)/(v[ii]*v[ii]).sum(1))/1e-24)
        grads.append(-2*np.dot(bad,gr))
    return cost,np.array(grads)
if __name__=='__main__':
    import sys
    dim=int(sys.argv[1]);seed=int(sys.argv[2]);n=int(sys.argv[3]);tau=float(sys.argv[4])
    rng=np.random.default_rng(seed);out=[]
    for i in range(n):
        z=np.zeros(dim) if i==0 else rng.normal(0,.06,dim)
        r=minimize(lambda p:esc(p,tau),z,jac=True,method='L-BFGS-B',bounds=[(-1,1)]*5+[(-.25,.25)]*(dim-5),options={'maxiter':800,'ftol':1e-15,'gtol':1e-12,'maxls':50})
        d=scores(r.x,True); d.update(loss=float(r.fun),tau=tau,start=z.tolist(),nit=int(r.nit),success=bool(r.success));out.append(d)
        print(i,dim,r.fun,len(d['S']),len(d['U']),'P',sum(b[0] for b in d['P']),'Q',sum(b[0] for b in d['Q']),flush=True)
        (Path(__file__).parent/f'escape_d{dim}_s{seed}_t{tau}.json').write_text(json.dumps(out,indent=2))
```

## File: rays.py
```python
from orbit import *
from scipy.sparse import csr_matrix
B=np.array([[[1,0,0],[0,0,0],[0,0,-1]],[[0,0,0],[0,1,0],[0,0,-1]],[[0,1,0],[1,0,0],[0,0,0]],[[0,0,1],[0,0,0],[1,0,0]],[[0,0,0],[0,0,1],[0,1,0]]],float)
DIRS=[];INC=[]
for Z,ee in [(X,E),(Y,DE)]:
 ij=np.r_[ee,ee[:,::-1]];DIRS.append(ij)
 INC.append(csr_matrix((np.ones(len(ij)),(ij[:,0],np.arange(len(ij)))),shape=(len(Z),len(ij))))

def sym(x,d):return (np.outer(x,d)+np.outer(d,x))/2

def gate_directions():
 rows=[]
 roots=[(6,1),(6,97),(62,1),(62,97)]
 metric=np.einsum('aij,bij->ab',B,B); inv=np.linalg.inv(metric)
 for u,s in roots:
  un=sorted(set(E[E[:,0]==u,1])|set(E[E[:,1]==u,0]));sn=sorted(set(DE[DE[:,0]==s,1])|set(DE[DE[:,1]==s,0]))
  for j in un:
   for k in sn:
    cp=sym(X[u],X[j]-X[u]);cq=-sym(Y[s],Y[k]-Y[s]);aa=np.array([np.einsum('ij,aij->a',cp,B),np.einsum('ij,aij->a',cq,B)])
    rhs=-np.array([X[u]@(X[j]-X[u]),Y[s]@(Y[k]-Y[s])])
    co=inv@aa.T@np.linalg.solve(aa@inv@aa.T,rhs);d=np.einsum('a,aij->ij',co,B)
    di=np.rint(d*1e8).astype(np.int64);di[2,2]=-di[0,0]-di[1,1]
    rows.append((dict(u=u,j=int(j),s=s,k=int(k)),di))
 return rows

def polys(d):
 pp=[]
 # exact formula is adj(I+tD) = I+t(tr(D)I-D)+t^2 adj(D)
 adj=d@d-np.trace(d)*d+((np.trace(d)**2-np.trace(d@d))/2)*np.eye(3)
 for z,ij,dd,ee in [(X,DIRS[0],d,np.zeros((3,3))),(Y,DIRS[1],np.trace(d)*np.eye(3)-d,adj)]:
  v=z[ij[:,0]];w=z[ij[:,1]]-v
  pp.append(np.array([np.einsum('ij,ij->i',v,w),np.einsum('ij,jk,ik->i',v,dd,w),np.einsum('ij,jk,ik->i',v,ee,w)]).T)
 return pp

def ray(di):
 d=di/1e8;lam=np.linalg.eigvalsh(d);lo=max(-1/v for v in lam if v>0);hi=min(-1/v for v in lam if v<0)
 pp=polys(d);rr=[]
 for p in pp:
  for c,b,a in p:
   if abs(a)<1e-22:
    if b!=0:rr.append(-c/b)
   else:
    disc=b*b-4*a*c
    if disc>0:
     sq=np.sqrt(disc);q=-.5*(b+np.copysign(sq,b));rr.extend([q/a,c/q])
 cuts=np.unique(np.r_[lo,np.array(rr)[(np.array(rr)>lo)&(np.array(rr)<hi)],hi]);mid=(cuts[1:]+cuts[:-1])/2
 counts=[];margins=[]
 for pol,inc in zip(pp,INC):
  val=pol[:,0,None]+pol[:,1,None]*mid+pol[:,2,None]*mid**2
  ctr=inc@(val>0);counts.append((ctr==0).sum(axis=0))
  margins.append(np.min(abs(val),axis=0))
 su=counts[0]+counts[1];ii=np.where(su==su.min())[0]
 # Retain up to twelve of the widest intervals at best count; all target intervals retained.
 jj=np.where(su==2)[0] if (su==2).any() else ii[np.argsort(-(cuts[ii+1]-cuts[ii]))[:12]]
 return dict(lo=float(lo),hi=float(hi),events=len(cuts)-2,minSU=int(su.min()),minU=int(counts[0].min()),minS=int(counts[1].min()),best=[dict(t=float(mid[k]),bounds=cuts[k:k+2].tolist(),U=int(counts[0][k]),S=int(counts[1][k]),raw_margin=[float(m[k]) for m in margins]) for k in jj])
if __name__=='__main__':
 import sys
 a=int(sys.argv[1]);b=int(sys.argv[2]);out=[]
 for it,(gate,di) in enumerate(gate_directions()[a:b],a):
  q=ray(di);q.update(i=it,gate=gate,Dint=di.tolist());out.append(q)
  print(it,q['minSU'],[(b['S'],b['U']) for b in q['best'][:3]],q['events'],flush=True)
  (Path(__file__).parent/f'rays_{a}_{b}.json').write_text(json.dumps(out,indent=2))
```

## File: metric_milp.py
```python
from orbit import *
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix

def coef(x,d):return np.array([x[0]*d[0],x[1]*d[1],x[2]*d[2],x[0]*d[1]+x[1]*d[0],x[0]*d[2]+x[2]*d[0],x[1]*d[2]+x[2]*d[1]])
def mat(v):return np.array([[v[0],v[3],v[4]],[v[3],v[1],v[5]],[v[4],v[5],v[2]]])
def run(which='P',root=6,seconds=12,rounds=2):
 z,ee=(X,E) if which=='P' else (Y,DE);ij=np.r_[ee,ee[:,::-1]];nn=len(ij); nv=7+nn
 lo=np.r_[[0,0,0,-.5,-.5,-.5,0],np.zeros(nn)];hi=np.r_[[1,1,1,.5,.5,.5,.2],np.ones(nn)]
 integ=np.r_[np.zeros(7),np.ones(nn)];cc=np.zeros(nv);cc[6]=-1
 rows=[];rl=[];rh=[]
 def add(c,l=-np.inf,h=np.inf):rows.append(c);rl.append(l);rh.append(h)
 add({0:1,1:1,2:1},1,1)
 for k,(i,j) in enumerate(ij):
  d=z[j]-z[i];cf=coef(z[i],d); sym=(np.outer(z[i],d)+np.outer(d,z[i]))/2;M=.2-np.linalg.eigvalsh(sym)[0]
  row={i:float(t) for i,t in enumerate(cf)};row[6]=-1;row[7+k]=-M;add(row,-M,np.inf)
 for i in range(len(z)):
  if i==root:continue
  add({7+k:1 for k in np.where(ij[:,0]==i)[0]},1,np.inf)
  cf=coef(z[root],z[root])-coef(z[i],z[i]);add({k:float(t) for k,t in enumerate(cf)},0,np.inf)
 rng=np.random.default_rng(180219)
 for vec in np.r_[np.eye(3),rng.normal(size=(32,3))]:
  vec/=np.linalg.norm(vec);cf=coef(vec,vec);add({k:float(t) for k,t in enumerate(cf)},1e-8,np.inf)
 out=[]
 for it in range(rounds):
  a=lil_matrix((len(rows),nv))
  for i,row in enumerate(rows):
   for k,v in row.items():a[i,k]=v
  res=milp(cc,integrality=integ,bounds=Bounds(lo,hi),constraints=LinearConstraint(a.tocsr(),rl,rh),options={'time_limit':seconds,'mip_rel_gap':1e-6})
  print(which,root,it,res.message,'fun',res.fun,'bound',getattr(res,'mip_dual_bound',None),flush=True)
  if res.x is None:out.append(dict(status=int(res.status),message=res.message));break
  g=mat(res.x[:6]);ev,q=np.linalg.eigh(g);m=np.array([z[i]@g@(z[j]-z[i]) for i,j in ij]);cnt=np.array([m[ij[:,0]==i].max() for i in range(len(z))]);
  d=dict(status=int(res.status),message=res.message,root=int(root),G=g.tolist(),tau=float(res.x[6]),eigen=ev.tolist(),roots=np.where(cnt<0)[0].tolist(),minescape=float(np.delete(cnt,root).min()),bound=float(getattr(res,'mip_dual_bound',float('nan'))))
  print('tau/eigen/roots',d['tau'],d['eigen'],d['roots'],'margin',d['minescape'],flush=True);out.append(d)
  if ev.min()>=0:break
  for v in q[:,ev<0].T:
   cf=coef(v,v);add({k:float(t) for k,t in enumerate(cf)},1e-8,np.inf)
 (Path(__file__).parent/f'milp_{which}_{root}.json').write_text(json.dumps(out,indent=2))
if __name__=='__main__':
 import sys
 run(sys.argv[1],int(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]))
```
