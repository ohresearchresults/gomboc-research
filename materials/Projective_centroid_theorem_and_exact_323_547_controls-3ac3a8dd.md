# material-3ac3a8ddddb9

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Projective centroid reachability, without equilibrium preservation

This is a general mathematical mechanism plus two preserved exact non-record bodies, NOT an own110 construction. Dependencies: exact_audit.py from [internal-source-reference]; the literal W51 input and simple reference from [internal-source-reference]. The complete numerical source and both exact rational output bodies are supplied here. No original sandbox or optimizer replay is required to reconstruct the exact bodies.

## General theorem
Let K be any full-dimensional bounded convex polytope with0 strictly inside. For b in D={b:1+b.x>0 for every x in K}, define T_b(x)=x/(1+b.x). There is a UNIQUE b* in D for which the actual homogeneous centroid of T_b*(K) is0. An arbitrary original interior point p is handled by replacing K with K-p first.

Proof. The Jacobian determinant is (1+b.x)^(-4), so
V(b)=Vol(T_b K)=integral_K (1+b.x)^(-4) dx,
grad V(b)=-4 integral_K x(1+b.x)^(-5) dx=-4 M(T_b K),
Hessian V(b)=20 integral_K xx^T(1+b.x)^(-6) dx.
The Hessian is positive definite since K has nonzero volume. D=int(-K*) is a bounded open convex set. At any boundary approach, one vertex v has epsilon=1+b.v tending to0. A fixed interior tetrahedral cone at v, restricted to radius proportional to epsilon, has volume proportional to epsilon^3 and denominator bounded above by a constant times epsilon, so V(b) diverges at least proportionally to epsilon^-1. Thus V has a unique interior minimizer, with M=0. T_b has positive denominator, maps segments to segments, and preserves convex incidence. It does NOT preserve radial equilibria. Any subsequent nonsingular affine transformation preserves the zero homogeneous centroid and can be used to investigate the remaining metric freedom.

This separates centroid reachability from the real obstacle: preserving strict110 while changing the geometry. It is not a proof that the required own110 body exists in a fixed projective/affine orbit.

## Executed finite computation and exact controls
Starting from literal W51 at the exact free110 point p=(4/5,11/10,-3/20), Newton minimization reached b approximately(2.580481636278759,-23.20593243626263,-9.01645994532598). At iteration18, image volume was approximately .004438526682693827, centroid norm6.07586185441064e-17, and the minimum vertex denominator .4583882334227054. These are numerical discovery values, not exact algebraic b* coordinates.

The independently specified rational freeze W51_PROJECTIVE_CENTRED_G8 has V31/E87/F58,C174, OWN strict323, additional weak000, primitive000. Its exact sole P relative depth is approximately .9840938570143961; Q depths are .5819316435967637 and .36094143857532. Rounding was not assumed to preserve the centroid: the audit recomputes its true rational homogeneous mass.

A finite five-start,600-step-per-start ordered-escape affine metric search on that exact freeze gave W51_CENTRED_METRIC_G8, same31/87/58, OWN strict547, weak000, primitive000. P depths approximately .8541124505514216,.07154031413233151,.06432462024797647; Q .686302735306367,.12914205271905446,.12517203289466142,.00009236770144272108. This does not improve to110 and does NOT exclude the full SPD orbit. It is retained as an exact negative control and reusable method, not a record.

Environment actually reported by these new numerical runs: NumPy2.3.5, SciPy1.17.0 where used, Torch2.10.0+cpu, float64, OMP/BLAS/Torch threads1, Python3.13.5. Earlier coordinator summaries listing different library versions are not the environment receipt for these runs. Exact audits use the standard library only.

## Exact rational inputs
Save each compact JSON line with final LF.
projective_centroid/input.json:941bytes SHA0c1a1fa2ff689fcd1e8420f7699fb3879354faf550e6e5a8c128f455506e9f13.
```json
{"denominator":100000000,"name":"W51_PROJECTIVE_CENTRED_G8","points":[[-10299072,-6621255,3331356],[-11734164,-6186503,1840394],[-9547954,-5474541,618144],[-73082155,18325078,-54975233],[-2321555,-3163118,-3256626],[-3569693,-2250458,-5537962],[-3099405,-2713787,-4458709],[-13354693,-54620,-11743391],[-893007,-2146218,-4990333],[-550768,-3466324,-2067138],[245513,-3221245,-2401883],[651205,-2830748,-3127555],[1589575,-2357486,-3716688],[730259,-1150158,-5896840],[4113402,-2553146,-2218806],[75381432,-7054412,50993322],[6874359,-3291289,641918],[8869278,-4392404,4090728],[10632992,-5720364,8143574],[3193080,-3843292,173942],[10793394,-6908287,11205061],[9672839,-7735979,12858917],[7791625,-8244291,13425866],[5449806,-8460322,13099605],[3027002,-8428479,12138218],[832719,-8346785,11173132],[-1026796,-8132875,9999036],[-2567851,-7916946,8944798],[-3932199,-7709434,7983849],[-5323783,-7485817,6985959],[-6959536,-7211400,5798649]]}
```
centred_metric/input.json:1082bytes SHA fa754b5d1f6a7fd7872d6b25e4d005b1846b4137d9fd2e90cf8fa14d9ca56e79.
```json
{"denominator":100000000,"name":"W51_CENTRED_METRIC_G8","points":[[-86524850,-117027071,228054707],[-88690800,-116842998,219998873],[-64709180,-117178492,142534578],[-247011492,134042367,206106830],[13515996,-117636098,-108865381],[17039634,-113356518,-138562850],[14506110,-115893418,-122314088],[-23434934,-89866544,-77820319],[34195608,-112706303,-180254607],[20102551,-118506527,-116025260],[28099983,-117806815,-140887738],[35325594,-116131641,-166979240],[45593643,-112280339,-199373327],[50656787,-99816457,-229485478],[55695417,-109063619,-211845326],[261112619,131280265,-189782212],[59635550,-106743214,-194863555],[54371479,-105724893,-147527719],[43659729,-103674704,-79182670],[35201076,-115959003,-135433636],[26765994,-103666261,-3935335],[8559771,-105124764,61123775],[-8958994,-107269553,113803681],[-24688364,-109653199,153063431],[-37296990,-111849816,177832314],[-48202667,-113398977,198118498],[-55348548,-114589813,206239341],[-60809013,-115389681,211001636],[-65495682,-115944159,214605894],[-70185030,-116370203,217913852],[-75629316,-116704759,221538828]]}
```

Exact verification from these literals (no optimizer):
```sh
python -B -S exact_audit.py projective_centroid/input.json projective_centroid/CLI.audit.json
python -B -S exact_audit.py centred_metric/input.json centred_metric/CLI.audit.json
```
The CLI adds a name field. To reproduce the original program audit encodings exactly, use:
```python
from pathlib import Path
import json
from exact_audit import audit
for folder in ('projective_centroid','centred_metric'):
    p=Path(folder);d=json.loads((p/'input.json').read_text())
    (p/'audit.json').write_text(json.dumps(audit(d['points'],d['denominator']),sort_keys=True,separators=(',',':'))+'\n')
print('PROJECTIVE_AND_METRIC_EXACT_RECONSTRUCTION_PASS')
```
Expected original audits: projective_centroid/audit.json11862bytes SHA68dc20a46f222ad736a1064fa3dbb74cdd74a94d594b0cf155b056f3e2681207; centred_metric/audit.json14699bytes SHA14aaaefab7ee98f631880ca5287d9480aa407c0ed28d1be9cdf1149e3d11824f. CLI terminal counts are31 87 58 [3,2,3] and31 87 58 [5,4,7], respectively, all additional weak/primitive zeros0.

## Complete projective_centroid.py
2860bytes SHA b2862bda5f456f34ac0b521eab5edc44146a4e3ed5f9ca77596802c143967009.
Numerical producing command:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python projective_centroid.py W51_ROBUST_G3.json W51_free_reference_simple.json projective_centroid
```python
"""Unique centroid-fixing central projectivity by strictly convex volume minimization.
Any interior prescribed reference is sent to the homogeneous centroid, but equilibrium
class is NOT invariant. Float64 solve plus exact rational frozen-body audit required.
"""
from pathlib import Path
from fractions import Fraction
import json,sys
import numpy as np
import torch
from exact_audit import audit

def solve(data,reference,out):
    torch.set_num_threads(1);torch.set_default_dtype(torch.float64);out=Path(out);out.mkdir(parents=True,exist_ok=True)
    au=audit(data['points'],data['denominator']);c=np.array([float(Fraction(v)) for v in reference]);ids=au['vertices'];mp={v:i for i,v in enumerate(ids)};p=torch.tensor(np.array(data['points'],float)[ids]/data['denominator']-c);tri=[]
    for f in au['facets']:
        v=f['vertices']
        for i in range(1,len(v)-1):tri.append([mp[v[0]],mp[v[i]],mp[v[i+1]]])
    tri=np.array(tri);det=(p[tri[:,0]]*torch.linalg.cross(p[tri[:,1]],p[tri[:,2]])).sum(1);assert bool((det>0).all())
    def volume(b):
        den=1+p@b;return (det/(den[tri].prod(1))).sum()/6
    b=torch.zeros(3);history=[]
    for k in range(60):
        b=b.detach().requires_grad_(True);v=volume(b);g=torch.autograd.grad(v,b)[0];H=torch.autograd.functional.hessian(volume,b);step=-torch.linalg.solve(H,g);rec=dict(k=k,volume=float(v.detach()),gradient_norm=float(torch.linalg.vector_norm(g).detach()),centroid_norm=float(torch.linalg.vector_norm(g).detach()/(4*v.detach())),minimum_denominator=float((1+p@b).min().detach()));history.append(rec)
        if rec['centroid_norm']<1e-12:break
        t=1.
        for j in range(80):
            trial=(b+t*step).detach()
            if bool(((1+p@trial)>0).all()) and float(volume(trial))<=float(v.detach())+1e-4*t*float(g@step):break
            t*=.5
        else:raise RuntimeError('Newton line search failed')
        b=trial
    transformed=p.detach().numpy()/(1+p.detach().numpy()@b.detach().numpy())[:,None]
    np.save(out/'points.npy',transformed);np.save(out/'projective_vector.npy',b.detach().numpy());(out/'run.json').write_text(json.dumps(dict(reference=reference,projective_vector=b.detach().tolist(),history=history,numpy=np.__version__,torch=torch.__version__),sort_keys=True,indent=2)+'\n')
    frozen=dict(name='W51_PROJECTIVE_CENTRED_G8',denominator=10**8,points=np.rint(transformed*1e8).astype(np.int64).tolist());(out/'input.json').write_text(json.dumps(frozen,sort_keys=True,separators=(',',':'))+'\n');a=audit(frozen['points'],frozen['denominator']);(out/'audit.json').write_text(json.dumps(a,sort_keys=True,separators=(',',':'))+'\n');print('PROJECTIVE_CENTRE_FINITE',history[-1], 'exact frozen own',a['strict'],a['additional_weak'],a['primitive_zero'])
if __name__=='__main__':solve(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))['reference'],sys.argv[3])
```

## Complete centred_metric_search.py
3725bytes SHA a603c3ea312bdf9cb489d696841ba5b287654df3d4044f5bc1f1678ff4720b7c.
Numerical producing command:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python centred_metric_search.py --input projective_centroid/input.json --out centred_metric --steps 600 --restarts 5 --lr .004 --margin .00001 --seed 260925
```python
"""Finite ordered-escape SPD metric search on an exactly specified own-centred body.
No finite failure excludes the metric orbit. Only an exact final census can certify110.
"""
from pathlib import Path
from fractions import Fraction
import argparse,json,time
import numpy as np
import torch
from exact_audit import audit

def run(input,out,steps=600,restarts=5,lr=.004,margin=1e-5,seed=260925):
    torch.set_num_threads(1);torch.set_default_dtype(torch.float64);data=json.load(open(input));a=audit(data['points'],data['denominator']);p=np.array(data['points'],float)[a['vertices']]/data['denominator'];c=np.array([float(Fraction(x)) for x in a['centroid']]);x=p-c;n=np.array([f['normal'] for f in a['facets']],float);h=np.array([f['offset'] for f in a['facets']],float)/data['denominator']-n@c;q=n/h[:,None]
    eig,V=np.linalg.eigh(x.T@x/len(x));B=(V/np.sqrt(eig))@V.T;X=torch.tensor(x@B.T);Q=torch.tensor(q@np.linalg.inv(B));out=Path(out);out.mkdir(parents=True,exist_ok=True);rng=np.random.default_rng(seed);history=[];best=1e100
    def mat(v):
        z=v[0]*0;diag=v[:3]-v[:3].mean();return torch.stack((torch.stack((diag[0].exp(),z,z)),torch.stack((v[3],diag[1].exp(),z)),torch.stack((v[4],v[5],diag[2].exp()))))
    def loss(z):
        r=(z*z).sum(1);order=torch.argsort(r.detach(),stable=True);rank=torch.empty(len(z),dtype=torch.long);rank[order]=torch.arange(len(z));allowed=rank[None,:]>rank[:,None];M=z@z.T/r[:,None]-1;M=M.masked_fill(~allowed,-1e12);w=M.max(1).values;w=w[order[:-1]];return torch.relu(margin-w).square().sum(),w.min()
    for j in range(restarts):
        v=torch.tensor(np.zeros(6) if j==0 else rng.normal(0,.25,6),requires_grad=True);opt=torch.optim.Adam([v],lr=lr)
        for k in range(steps+1):
            A=mat(v);P=X@A.T;R=Q@torch.linalg.inv(A);lp,mp=loss(P);lq,mq=loss(R);L=lp+lq;val=float(L.detach())
            if val<best:
                best=val;matrix=A.detach().numpy()@B;points=x@matrix.T;np.save(out/'matrix.npy',matrix);np.save(out/'points.npy',points);rec=dict(restart=j,k=k,loss=val,minP=float(mp.detach()),minQ=float(mq.detach()),condition=float(np.linalg.cond(matrix)));(out/'best.json').write_text(json.dumps(rec,sort_keys=True,indent=2)+'\n')
            if k%300==0:print('CENTRED_METRIC',j,k,val,best,flush=True)
            if float(torch.minimum(mp,mq).detach())>margin/2:break
            if k==steps:break
            opt.zero_grad();(L+1e-5*torch.relu(v.abs()-3).square().sum()).backward();opt.step()
        history.append(dict(restart=j,last_step=k,best=best))
    frozen=dict(name='W51_CENTRED_METRIC_G8',denominator=10**8,points=np.rint(np.load(out/'points.npy')*1e8).astype(np.int64).tolist());(out/'input.json').write_text(json.dumps(frozen,sort_keys=True,separators=(',',':'))+'\n');au=audit(frozen['points'],frozen['denominator']);(out/'audit.json').write_text(json.dumps(au,sort_keys=True,separators=(',',':'))+'\n');(out/'run.json').write_text(json.dumps(dict(steps=steps,restarts=restarts,lr=lr,margin=margin,seed=seed,history=history,numpy=np.__version__,torch=torch.__version__),sort_keys=True,indent=2)+'\n');print('CENTRED_METRIC_FINITE_EXACT_FREEZE',au['strict'],au['additional_weak'],au['primitive_zero'],[b['depth_float'] for b in au['P']],[b['depth_float'] for b in au['Q']],flush=True)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='projective_centroid/input.json');ap.add_argument('--out',default='centred_metric');ap.add_argument('--steps',type=int,default=600);ap.add_argument('--restarts',type=int,default=5);ap.add_argument('--lr',type=float,default=.004);ap.add_argument('--margin',type=float,default=1e-5);ap.add_argument('--seed',type=int,default=260925);run(**vars(ap.parse_args()))
```

The original accepted C622 is unchanged. A finite unsuccessful centring-plus-metric search is not a proof that this mechanism cannot work on a deformed body or another reference cell.
