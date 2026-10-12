# material-ef4c8cf0785a

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J85 dynamic-hull and stable-carrier methods: complete source units and exact lemma

## Evidence boundary after an observed working-container reset
The working directory /mnt/data/j85 disappeared during source publication; a subsequent listing showed /mnt/data empty. The already stored [internal-source-reference] remains the exact recovery capsule for J85_CLASS_FIRST_G8, its G6 control, and the angular-flattening control. The later dynamic/stellar bodies were executed and exactly audited before the reset, but their full literal coordinate files had not yet been stored. At publication of THIS source material those later files are lost locally, and their exact recovery is pending. Do not promote their numerical hashes or this statement as complete coordinate preservation.

This material preserves complete source units from the literal executed tool calls, plus the analytic lemma. It provides a regeneration route from already durable exact input. Optimization is a numerical producer, not a portable bit-for-bit theorem: check the listed coordinate hashes before treating regenerated checkpoints as the previously audited bodies. A differing result is a different nominee and needs its own identity and exact census. The two required source dependencies are [internal-source-reference] (exact84.py and its literal J82_S1_ROBUST_G6_INPUT.json) and [internal-source-reference] (J85_CLASS_FIRST_G8_INPUT.json and freeze85.py). No FULL76 is needed.

Executed environment before and after the observed reset: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, float64, one Torch thread, OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1.

## Executed chronology, not a claim of own110
From literal J85_CLASS_FIRST_G8, dynamic85.py ran ten accepted steps at initial radius .01. The frozen J85_DYNAMIC_A_G8/G10 each had V45/E129/F86, C258, own121/weak000, one positive P and no Q. P was .4552962231087733/.4552962200930236. Exactly18 old triangular facet sets were replaced by18 new ones. Stable facet {0,30,40}, U0/40 and H21--30 persisted. G8 sufficient S1 cube rho was3.0884500134885855e-7.
Two single-stellar exact endpoints from this G8 parent had V46/E132/F88, C264, own121/weak000. The new stable facet was {0,30,45}, excluding U40; U0/40 and H21--30 remained. The literal new D=1e12 rows for lambda1/2 and3/4, beta1e-6, are embedded in stellar_exact85.py. Their P depths were .45529621852998653/.4552962173466763. This is label/carrier detachment, not cancellation or whole-basin separation.
The lambda3/4 endpoint was continued for12 accepted steps, then14 completed accepted steps of a requested20-step run. The latter timed out after step13; no claim to the other six. Frozen J85_DETACHED_CONTINUED_B_G10/G12 had V46/E132/F88, C264, own121/weak000, P .44777264877820677/.447772648799477, no Q, stable {0,30,45}, U0/40, H21--30. S1 cube rho fell to2.7541408663612723e-8/2.7516604826672314e-8. Better depth is not unconditional improvement in robustness.
A second stellar addition instead started from the EARLIER lambda1/2 single-stellar body, not from the lower-depth continued B body. Exact J85_DOUBLE_STELLAR_L1D4_G12 and L1D2_G12 had V47/E135/F90, C270, own121/weak000, P .45529621853755453/.45529621854408525 and no Q. Stable facet {0,45,46} is disjoint from the exact strict-superlevel component above the finite P death: {22,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44}. Their S1 cube radii were3.1617028157621806e-7/3.161677682111101e-7. This is not the old J84 block28..44, and not a claim about every possible gradient-attractor basin. U0/40 and H21--30 remained. None is110; canonical own110 remains C622.

## Stable-triangle splitting lemma, with physical mass
Let a homogeneous convex polyhedron have no additional weak equilibria, and let F=conv(a,b,c) be a strictly stable maximal triangular facet. Let g be its own centroid, n=(b-a) cross(c-a) outward, h_g=n.(a-g)>0, and f=g+h_g*n/|n|^2. Choose0<lambda<1, put t=(1-lambda)f+lambda*c, and add w(beta)=t+beta*h_g*n/|n|^2. For all sufficiently small positive beta, the homogeneous hull retains the complete strict S/U/H census and has no weak equilibria, while F is replaced by three triangles and its stable carrier becomes conv(a,b,w), excluding c. V increases1, E increases3, F increases2, C increases6. An unstable equilibrium at c is not eliminated. This is a directly derived local method, not a claim of historical novelty for stellar subdivision.
Proof: t is in the relative interior of F, so small protrusion sees only F and retains the other facets and all old vertices/edges. Write f=alpha*a+eta*b+gamma*c with positive barycentric weights. With d=(1-lambda)gamma+lambda, f lies strictly inside conv(a,b,t), with t-weight gamma/d and a,b weights alpha*lambda/d, eta*lambda/d. The other subtriangles exclude f. The three normals and the true new centroid converge to the originals, giving exactly one stable subtriangle and preserving every other old facet's classification. Since t-f is nonzero and t is an interior convex combination, some old corner has a strictly positive radial chord from t; the new apex stays non-U for small beta. Every old non-U keeps an old positive witness. Every old U has a strictly negative score toward t, a nontrivial convex combination of old vertices, and remains strict after small centroid drift.
Old edge saddle/weak classifications persist by strict separation from the closed equilibrium conditions. No new edge's beta=0 closed segment contains f. If its orthogonal projection parameter lies outside the segment, it remains outside. Otherwise its radial vector has a nonzero tangential component, whereas its adjacent outward normals both converge to n; it cannot enter their positive cone for small beta. Thus the new edges add no H or weak equilibria. This proves a small interval, not arbitrary finite beta.
The added pyramid volume is v(beta)=beta*h_g/6, with centroid (a+b+c+w(beta))/4. The actual new filled centroid is [V*g+v(beta)*(a+b+c+w(beta))/4]/[V+v(beta)], a rational function with quadratic numerator. For another old support n_j.x<=h_j with n_j.n>0, first visibility contact occurs at beta_j=(h_j-n_j.t)*|n|^2/[h_g*(n_j.n)]. These explicit mass/visibility formulas can help bound a finite interval. The listed finite rounded endpoints still require the fresh exact census. The double-stellar construction uses the new stable triangle, target row30, beta1e-8, lambda1/4 or1/2 and ties-to-even D1e12 rounding only of the new row.

## Regeneration commands and exact identity checks
Save source blocks verbatim. With the two required source materials extracted alongside them:
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
python dynamic85.py --steps 10 --radius .01 --out DYNAMIC85_A.json
python freeze_dynamic85.py --input DYNAMIC85_A.json --prefix J85_DYNAMIC_A --grids 8 10
Before using any later literal recipe, require J85_DYNAMIC_A_G8_INPUT.json SHA1c45fe7c95d2454c29596c1ce6dd3ccaf39cefd465026bd1d2c10a97aae6f847 and G10 INPUT SHAec1c1f91d911177b4cd23e9d5e1fd6ea63303e7890bd4bc3c3e91572021331f2.
Then python stellar_exact85.py and python double_stellar85.py.
To recover the lower-depth continuation, run:
python dynamic_stellar85.py --input J85_STELLAR_L3D4_B1D1000000_G12_INPUT.json --steps 12 --radius .01 --out DYNAMIC_STELLAR85_A.json
python dynamic_stellar85.py --input DYNAMIC_STELLAR85_A.json --steps 14 --radius .0125 --out DYNAMIC_STELLAR85_B.json
python freeze_dynamic85.py --input DYNAMIC_STELLAR85_B.json --prefix J85_DETACHED_CONTINUED_B --grids 10 12
The14-step replay matches the actual completed prefix, not all20 requested steps. The wrapper preserves stored PD/QD on warm continuation; it does not lower the target by another factor10 at each restart. Desired G10 INPUT SHA b64ac54422ce18d54117685545d2f306ab29f15dc7473664941b71d2814f54c8, G12 INPUT SHAecb57f2d9acd94f1bf4fb0af01ba40f6596d13f081823ffb7c23332de4a36232.
Terminal markers are in the complete source units. These numerical regeneration commands have not yet been replayed after the reset at publication of this material.

## dynamic85.py
```python
"""Live-hull class-first continuation after J85. Nomination only, no exact claim.
Independent of old numerical helpers; exact84 is used only for ROOT. Qhull
nominates each current hull and torch differentiates its locally fixed faces.
"""
import os,argparse,json,time
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np,torch
from scipy.spatial import ConvexHull
from scipy.optimize import linprog
from exact84 import ROOT

torch.set_num_threads(1);torch.set_default_dtype(torch.float64)

def getfaces(X):
    h=ConvexHull(X);F=h.simplices.copy();a=X[F[:,0]];b=X[F[:,1]];c=X[F[:,2]]
    flip=(np.cross(b-a,c-a)*(a-X.mean(0))).sum(1)<0
    F[flip]=F[flip][:,[0,2,1]]
    return F

def guards(xx):
    d=xx[None,:,:]-xx[:,None,:];dd=torch.linalg.vector_norm(d,dim=2)
    score=(xx[:,None,:]*d).sum(2)/(torch.linalg.vector_norm(xx,dim=1)[:,None]*torch.clamp(dd,min=1e-30))
    return (score-torch.eye(len(xx))*4).max(1).values

def geom(X,F):
    tri=X[F];n=torch.linalg.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]);area=torch.linalg.vector_norm(n,dim=1)
    n=n/area[:,None];h=(n*tri[:,0]).sum(1);r=X.mean(0);xx=tri-r
    v=(xx[:,0]*torch.linalg.cross(xx[:,1],xx[:,2])).sum(1);V=v.sum()/6
    g=(v[:,None]*(tri.sum(1)+r)).sum(0)/(24*V);p=X-g;q=n/(h-n@g)[:,None]
    return p,q,area,V,g

class Model:
    def __init__(self,X):
        self.first=torch.tensor(X[0]);self.N=len(X);self.rp=[0,40]
        self.PD=1e-7;self.QD=1e-6;self.AREA=1e-7;self.SEP=.001
        F=getfaces(X)
        with torch.no_grad():p,q,a,V,g=geom(torch.tensor(X),torch.tensor(F))
        self.Vmin=float(V)*.2
    def full(self,x):return torch.cat((self.first[None],x.reshape(-1,3)))
    def setup(self,x):
        X=self.full(torch.tensor(x)).numpy();F=getfaces(X)
        with torch.no_grad():p,q,a,V,g=geom(torch.tensor(X),torch.tensor(F))
        rq=int(torch.argmax((q*q).sum(1)));mp=torch.tensor([i not in self.rp for i in range(self.N)])
        mq=torch.tensor([i!=rq for i in range(len(F))]);T=torch.tensor(F)
        def fun(w):
            Y=self.full(w);p,q,a,V,g=geom(Y,T);dist=torch.cdist(Y,Y)+torch.eye(self.N)*1e4
            return torch.cat((guards(p)[mp]-self.PD,guards(q)[mq]-self.QD,a-self.AREA,
                              dist.min(1).values-self.SEP,(V-self.Vmin)[None]))
        return fun,F
    def cj(self,x,jac=False):
        fun,F=self.setup(x);w=torch.tensor(x)
        v=fun(w).numpy()
        J=torch.func.jacrev(fun,chunk_size=16)(w).numpy() if jac else None
        return v,J,F

def barlist(X,F):
    with torch.no_grad():p,q,a,V,g=geom(torch.tensor(X),torch.tensor(F))
    pp=p.numpy();r=(pp*pp).sum(1);edges=sorted({tuple(sorted((int(a),int(b)))) for f in F for a,b in zip(f,np.roll(f,-1))})
    par=list(range(len(X)))
    def find(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    ev=[]
    for a,b in edges:
        d=pp[b]-pp[a];t=np.clip(-pp[a]@d/(d@d),0,1);z=pp[a]+t*d;ev.append((z@z,a,b))
    out=[]
    for v,a,b in sorted(ev,reverse=True):
        i,j=find(a),find(b)
        if i==j:continue
        if (r[i],-i)<(r[j],-j):i,j=j,i
        if r[j]>v:out.append((1-v/r[j],j,a,b))
        par[j]=i
    return sorted(out,reverse=True)

def objective_grad(m,x,F,bar):
    _,root,a,b=bar;w=torch.tensor(x,requires_grad=True);p,q,ar,V,g=geom(m.full(w),torch.tensor(F))
    d=p[b]-p[a];t=torch.clamp(-(p[a]*d).sum()/(d*d).sum(),0,1);z=p[a]+t*d
    obj=1-(z*z).sum()/(p[root]*p[root]).sum();obj.backward();return w.grad.numpy()

def restore(m,x,radius):
    for k in range(5):
        v,_,F=m.cj(x)
        if v.min()>=-1e-12:return x,True,k
        v,J,F=m.cj(x,True);N=len(x)
        A=np.vstack((np.c_[-J,np.zeros(len(v))],np.c_[np.eye(N),-np.ones(N)],np.c_[-np.eye(N),-np.ones(N)]))
        b=np.r_[v-1e-9,np.zeros(2*N)];obj=np.r_[np.zeros(N),1.]
        r=linprog(obj,A_ub=A,b_ub=b,bounds=[(-radius,radius)]*N+[(0,radius)],method='highs')
        if not r.success:return x,False,k
        x=x+r.x[:-1]
    v,_,F=m.cj(x);return x,bool(v.min()>=-1e-12),5

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='J85_CLASS_FIRST_G8_INPUT.json');ap.add_argument('--out',default='DYNAMIC85.json')
    ap.add_argument('--steps',type=int,default=12);ap.add_argument('--radius',type=float,default=.01);a=ap.parse_args()
    d=json.loads((ROOT/a.input).read_text());X=np.array(d['points'],float)/d.get('denominator',1)
    m=Model(X);x=X[1:].ravel();rad=a.radius;records=[];start=time.time();F0=getfaces(X)
    for k in range(a.steps):
        v,J,F=m.cj(x,True);BB=barlist(X,F)
        if not BB:break
        old=BB[0][0];grad=objective_grad(m,x,F,BB[0]);rr=linprog(grad,A_ub=-J,b_ub=v,bounds=[(-rad,rad)]*len(x),method='highs')
        accepted=False;alpha=1.;ns=0
        if rr.success:
            for j in range(12):
                try:
                    y,ok,ns=restore(m,x+alpha*rr.x,rad*alpha)
                    if ok:
                        Y=m.full(torch.tensor(y)).numpy();ff=getfaces(Y);bb=barlist(Y,ff);new=bb[0][0] if bb else 0.
                        if new<old-1e-10:accepted=True;X=Y;x=y;F=ff;break
                except (ValueError,RuntimeError):pass
                alpha*=.5
        if accepted and alpha>.99:rad=min(rad*1.25,.05)
        elif not accepted or alpha<.125:rad*=.5
        with torch.no_grad():p,q,ar,V,g=geom(torch.tensor(X),torch.tensor(F));gp=guards(p);gq=guards(q)
        bb=barlist(X,F);v,_,_=m.cj(x);topchange=len({tuple(sorted(f)) for f in F}^{tuple(sorted(f)) for f in F0})
        rec={'step':k,'accepted':accepted,'P':bb[0][0] if bb else 0.,'S':int((gq<0).sum()),'U':int((gp<0).sum()),
             'margin':float(v.min()),'changed_triangles':topchange,'radius_next':rad,'alpha':alpha,'restore_rounds':ns,'LP_status':rr.status}
        records.append(rec)
        out={'parameters':vars(a),'points':X.tolist(),'faces':F.tolist(),'records':records,'bars':bb,'volume':float(V),'centroid':g.numpy().tolist(),
             'elapsed':time.time()-start,'PD':m.PD,'QD':m.QD,'AREA':m.AREA,'SEP':m.SEP,'Vmin':m.Vmin,'status':'NUMERICAL_ONLY'}
        (ROOT/a.out).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');print(rec,flush=True)
        if rad<1e-8:break
    print('J85_DYNAMIC_HULL_CONTINUATION_DONE',len(records),sum(r['accepted'] for r in records),flush=True)
if __name__=='__main__':main()
```

## dynamic_stellar85.py
```python
"""Dynamic-hull continuation from an exactly S1/U2 stellar-detached body.
This wrapper only makes initial positive witness targets consistent with its
new facet normals. All subsequent hull/mass/bar/restoration logic is dynamic85.
"""
import argparse,json
import numpy as np,torch
import dynamic85 as d
OriginalModel=d.Model
parser=argparse.ArgumentParser(add_help=False)
parser.add_argument('--input',default='J85_CLASS_FIRST_G8_INPUT.json')
known,_=parser.parse_known_args()
source=json.loads((d.ROOT/known.input).read_text())
saved_targets=(source.get('PD'),source.get('QD'))
class Model(OriginalModel):
    def __init__(self,X):
        super().__init__(X)
        F=d.getfaces(X)
        with torch.no_grad():p,q,a,V,g=d.geom(torch.tensor(X),torch.tensor(F));gp=d.guards(p);gq=d.guards(q)
        rp=np.array([i not in self.rp for i in range(len(X))]);rq=int(torch.argmax((q*q).sum(1)));sq=np.arange(len(F))!=rq
        assert int((gp<0).sum())==2 and int((gq<0).sum())==1
        self.PD=min(1e-7,.1*float(gp[rp].min()));self.QD=min(1e-6,.1*float(gq[sq].min()))
        if saved_targets[0] is not None and saved_targets[1] is not None:
            self.PD=float(saved_targets[0]);self.QD=float(saved_targets[1])
        assert self.PD>0 and self.QD>0
        print('J85_STELLAR_INITIAL_FEASIBLE_TARGETS',self.PD,self.QD,flush=True)
d.Model=Model
if __name__=='__main__':d.main()
```

## freeze_dynamic85.py
```python
"""Exact fresh supporting hull for rationalized dynamic-hull checkpoints.
Requires exact84.py and freeze85.py; uses no Qhull for final supporting planes.
The saved INPUT includes all material rows; report maps true vertices back to rows.
"""
import argparse,json
from fractions import Fraction as R
from itertools import combinations
from exact84 import ROOT,cross,dot,sub,audit
from freeze85 import cube,dump

def exact_hull(rows,D):
    faces=[]
    for a,b,c in combinations(range(len(rows)),3):
        n=cross(sub(rows[b],rows[a]),sub(rows[c],rows[a]));h=dot(n,rows[a])
        if n==(0,0,0):continue
        scores=[dot(n,p)-h for p in rows]
        if min(scores)<0<max(scores):continue
        if sum(s==0 for s in scores)!=3:raise ValueError('Nonsimplicial rational endpoint requires a maximal-facet hull builder')
        faces.append([a,b,c] if max(scores)==0 else [a,c,b])
    ids=sorted({i for f in faces for i in f});idx={old:new for new,old in enumerate(ids)}
    P=[tuple(R(t,D) for t in rows[i]) for i in ids];F=[[idx[i] for i in f] for f in faces]
    # Every original material row was checked against every surviving support above.
    return P,F,ids

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='DYNAMIC85_A.json');ap.add_argument('--prefix',default='J85_DYNAMIC_A')
    ap.add_argument('--grids',type=int,nargs='+',default=[8,10]);a=ap.parse_args();j=json.loads((ROOT/a.input).read_text())
    for k in a.grids:
        D=10**k;rows=[[round(float(t)*D) for t in row] for row in j['points']];name=a.prefix+'_G'+str(k)
        dump(name+'_INPUT.json',{'name':name,'denominator':D,'points':rows});P,F,ids=exact_hull(rows,D)
        rep=audit(P,F);rep['name']=name;rep['material_rows']=ids;dump(name+'_EXACT.json',rep)
        cc=cube(P,F)
        if cc is not None:dump(name+'_CUBE.json',cc)
        print('J85_DYNAMIC_EXACT',name,len(rows),(rep['V'],rep['E'],rep['F']),rep['strict'],rep['weak'],
              [float(R(t['depth'])) for t in rep['P']],None if cc is None else cc['certificates']['adjacent']['rho_float'],flush=True)
    print('J85_DYNAMIC_FREEZE_DONE_NO_110_CLAIM',flush=True)
if __name__=='__main__':main()
```

## stellar_exact85.py
```python
"""Exact selected stable-carrier-detachment bodies; no optimizer for replay.
Required exact input: J85_DYNAMIC_A_G8_INPUT.json. Required source modules:
exact84.py, freeze85.py, freeze_dynamic85.py. New rows are literal integers.
"""
import json
from fractions import Fraction as R
from exact84 import ROOT,audit
from freeze85 import dump,cube
from freeze_dynamic85 import exact_hull
CASES={
 'J85_STELLAR_L1D2_B1D1000000_G12':[340833863051,-589347081200,-397577617925],
 'J85_STELLAR_L3D4_B1D1000000_G12':[591346646643,-522088413323,-448042290520],
}

def main():
    base=json.loads((ROOT/'J85_DYNAMIC_A_G8_INPUT.json').read_text());D=10**12
    for name,new in CASES.items():
        rows=[[t*(D//base['denominator']) for t in row] for row in base['points']]+[new]
        dump(name+'_INPUT.json',{'name':name,'denominator':D,'points':rows})
        P,F,ids=exact_hull(rows,D);rep=audit(P,F);rep['name']=name;rep['material_rows']=ids
        assert (rep['V'],rep['E'],rep['F'])==(46,132,88)
        assert rep['strict']==[1,2,1] and rep['weak']==[0,0,0]
        assert [ids[v] for v in rep['U']]==[0,40]
        sf={ids[v] for v in F[rep['S'][0]]};assert sf=={0,30,45}
        dump(name+'_EXACT.json',rep);cc=cube(P,F);dump(name+'_CUBE.json',cc)
        print('J85_OWN121_STABLE_CARRIER_DETACHMENT_EXACT_PASS',name,sf,
              float(R(rep['P'][0]['depth'])),cc['certificates']['adjacent']['rho_float'],flush=True)
    print('J85_STELLAR_TWO_EXACT_BODIES_NO_110',flush=True)
if __name__=='__main__':main()
```

## double_stellar85.py
```python
"""Detach the actual stable triangle from the finite-bar superlevel component.
Exact 47-vertex constructions, not own110. Builds on the exact lambda=1/2
single-stellar input, keeping its 46 rows literally unchanged on D=1e12.
"""
import json
from fractions import Fraction as R
from exact84 import ROOT,audit,sub,cross,dot,add,scale,topology
from freeze85 import dump,cube
from freeze_dynamic85 import exact_hull

def superlevel_component(P,F,g,root,death):
    pp=[sub(p,g) for p in P];edges,_=topology(P,F);adj=[[] for _ in P]
    for a,b in edges:
        d=sub(pp[b],pp[a]);t=max(R(0),min(R(1),-dot(pp[a],d)/dot(d,d)));r=add(pp[a],scale(d,t))
        if dot(r,r)>death:adj[a].append(b);adj[b].append(a)
    seen={root};stack=[root]
    while stack:
        for j in adj[stack.pop()]:
            if j not in seen:seen.add(j);stack.append(j)
    return sorted(seen)

def main():
    base=json.loads((ROOT/'J85_STELLAR_L1D2_B1D1000000_G12_INPUT.json').read_text());D=base['denominator']
    P,F,ids=exact_hull(base['points'],D);assert ids==list(range(46));rep=audit(P,F);g=tuple(map(R,rep['own_centroid']))
    f=F[rep['S'][0]];a,b,c=[P[i] for i in f];n=cross(sub(b,a),sub(c,a));nn=dot(n,n);h=dot(n,sub(a,g));foot=add(g,scale(n,h/nn))
    beta=R(1,10**8)
    for lam in [R(1,4),R(1,2)]:
        w=add(add(scale(foot,1-lam),scale(P[30],lam)),scale(n,beta*h/nn))
        rows=base['points']+[[round(v*D) for v in w]];name='J85_DOUBLE_STELLAR_L'+str(lam.numerator)+'D'+str(lam.denominator)+'_G12'
        dump(name+'_INPUT.json',{'name':name,'denominator':D,'points':rows});Q,G,qids=exact_hull(rows,D);r=audit(Q,G)
        r['name']=name;r['material_rows']=qids;sf={qids[i] for i in G[r['S'][0]]}
        assert (r['V'],r['E'],r['F'])==(47,135,90) and r['strict']==[1,2,1] and r['weak']==[0,0,0]
        assert sf=={0,45,46} and [qids[i] for i in r['U']]==[0,40]
        B=superlevel_component(Q,G,tuple(map(R,r['own_centroid'])),r['P'][0]['root'],R(r['P'][0]['death2']))
        assert sf.isdisjoint({qids[i] for i in B})
        r['finite_P_superlevel_component']=B;r['stable_facet_material_rows']=sorted(sf)
        r['scope']='Stable facet excludes every vertex of the strict superlevel component above the single finite P death; not a claim about all possible gradient basins.'
        dump(name+'_EXACT.json',r);cc=cube(Q,G);dump(name+'_CUBE.json',cc)
        print('J85_DOUBLE_STELLAR_FINITE_BAR_CARRIER_DETACHED_EXACT_PASS',name,B,float(R(r['P'][0]['depth'])),cc['certificates']['adjacent']['rho_float'],flush=True)
    print('J85_DOUBLE_STELLAR_TWO_OWN121_BODIES_NO_110',flush=True)
if __name__=='__main__':main()
```
