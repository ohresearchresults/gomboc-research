# material-7406fc9387ad

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J142 numerical producers and frozen cap recovery

## Evidence boundary
No new exact own110 body, optimizer-optimality claim, or entire-family exclusion is made by these numerical routines. Exact finite root-retaining contraction and volume-dual certificates are separately in [internal-source-reference], using the exact three-file dependency [internal-source-reference]. The latter includes all LOW62 input data, exact all-path reconstruction and integer hull/mass code. The six complete files below preserve every materially used numerical method and all twelve selected cap geometries without needing the originating optimizer checkpoint or sandbox.

Observed environment: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, binary64, one OPENBLAS/OMP thread. Numerical facets are grouped at1e-9; all positive floating P/Q are retained, including possible roundoff-size values. The diagnostic fields ending1e10 actually use the code's threshold1e-10; their names are historical, not a different tolerance. No weak/primitive exact census is inferred. BFGS precision-loss statuses are preserved rather than recast as optimality or infeasibility. The exact rational proofs do not depend on these statuses.

## Reconstruction and execution
First save all three FILE blocks in [internal-source-reference]. Save the six FILE blocks below, preserving their final newlines, in the same directory. Run with assertions enabled:

python -B -S exact142.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python numeric142.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python core142.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python caps142.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python replaycaps142.py

The frozen replay does not run an optimizer. Its complete lambda/depth-slack recipes and exact142-derived rays reconstruct all twelve original binary64 point arrays, authenticate their recorded hashes, and emit all floating positive bars. On a different numerical-library environment, an asserted point-array hash mismatch is a portability failure, not a false exact mechanical result. The original producing runs and the final frozen replay were executed; the exact witnesses remain valid independently of numerical replay.

Input/source manifest:
input142.py2491B/SHA256bc799e56b9c7f19e088e9872144860b8fbf272c5518a5b3e4380f7b3f04deb36.
numeric142.py3559B/SHA256f85d4433f52dafe615c2362a584cf401012e46d6601b157911457aa20df9aead.
caps142.py5478B/SHA25685309f3da3f5b9358f66f7ec521b19d7e6551513b850906baa3d619cf07822ba.
core142.py2775B/SHA256a9f7e57574cd626b1f3e4e4df5e05a71993636fa612a770cd44a824e68b0e9d4.
replaycaps142.py2106B/SHA256ede4e035729eb80c8492e7b7f99cf01f8757dc8454d4c269c251460b994f9377.
CAPS142_PARAMETERS.json5322B/SHA25682f35ef85e8107164d284f00f525bbfe4746f2aab5507c7309a477c9e486874f.

Observed outputs:
NOMINATE142.json26497B/SHA25649591d4eb666d7d8647d2f5610d729778adb5129515bf270eaac0e6227db522e.
CORE142_NOMINATIONS.json47527B/SHA256ddaa33651b2632e2bcf323d3338608b75f6080dfef39c7e731bcc90d63da985e.
CAPS142_NUMERICAL.json209320B/SHA25623c002201dd2db965b34f4048cc589cff194a00cd2c25030fa43201fef714ca9.
CAPS142_REPLAY.json115574B/SHA25655156d7c107ff041e16f501f24cf5fc37be8083a5ec05818b37621ccdf07cbc4.
Executed frozen marker: J142_TWELVE_FROZEN_CAPS_REPLAY_ALL_FLOAT_POSITIVE_BARS_NO_EXACT_CLASS.

## What the finite cap experiment found
The cap family uses H_i=p_i R_i exp(-slack*depth_i) and H intersect {1+lambda.x>=0}, with slack0,.001,.003,.01,.03,.1. Maximizing retained mass subject to centre0 is the J75 convex positive-affine integral principle, reused here. The actual numerical caps have tiny nonzero centre residuals and discard the designated old root. Consequently they are not root-retaining solutions of the J142 fixed-root family even before their many P/Q defects are counted.

For raw root9, the six numerical(V/E/F;Pcount,Qcount;retained volume fraction) are:
72/174/104;11,15;.6079658252200355.
71/171/102;8,13;.6005947453275262.
72/172/102;9,10;.586063859384819.
72/167/97;8,8;.5368573384143653.
70/157/89;7,4;.413929447789243.
56/119/65;8,1;.15700258371276204.
For root45:
61/132/73;12,14;.5371511638265212.
57/122/67;7,11;.5311473225275865.
55/117/64;8,10;.5192202860473275.
52/110/60;7,6;.4774112861370519.
47/102/57;8,3;.3654001362897385.
38/77/41;4,2;.1160420800020902.
These are twelve actually executed tests, not a proved obstruction to every centroid-balanced cut or a certified exact class ledger. No positive bar was deleted to claim110. The root-retaining-core search also sampled reflection -B/3; it selected the same fixed integer normals/alphas in these two instances, which is not a theorem that reflection never helps.

## FILE input142.py
```python
from pathlib import Path
import hashlib,json
ROWS=[
[-653160200,-396049270,-281044390],[-635901120,-348735520,-114703370],[-573485370,-312096030,59433110],[-403851850,-274801310,333222890],[-628942740,-465851940,-479051720],[-298369900,-270988410,445608910],[-294004040,145261700,-277025530],[-227641470,174563440,-397890660],[-205616870,175558830,52613520],[-166419230,-864228870,-1684987750],[-159639480,-279904570,546701640],[-127070280,274153810,-149434510],[-121431580,232514050,-433105560],[-64253580,188186610,-573157110],[-61840320,48778390,-768887040],[-41547760,287804810,5312940],[-29845790,163437240,-627608200],[99900,-45390120,-874628490],[5559340,-304900310,621173960],[8318690,-777643830,-875588880],[21079870,317858320,-407617870],[32249280,209952060,183953630],[35691350,401777180,-198295560],[143526670,299058790,155509180],[167157090,336773360,123310730],[189220990,-314610540,663403040],[214862400,-113330470,-923187470],[281708130,-144015970,-906872580],[292611180,361490930,-462968400],[298261210,78683760,-725758550],[316173700,495336860,-305926610],[330358080,-672965550,-524978670],[380482910,-290962420,671095610],[386072830,-647953450,-486309890],[419532220,375270360,-409491510],[884356620,279779640,-154148160],[453499290,-113904820,-752292560],[911839560,76557340,-160274860],[474798190,-564668400,-560385730],[957240240,-75942940,-56852760],[524292760,-463132620,-621603750],[568515370,-264590000,639235000],[663024440,-544756110,473622630],[670107650,446931130,-241056530],[691422270,462164000,-26560520],[742534800,-242797950,570713920],[742815290,197050420,387780860],[754773010,333161360,219979510],[773316910,405326120,-199527750],[838672450,-157875350,483863520],[874122860,-21297470,412343550],[878258330,193058660,-187178160],[886599130,-414301780,340615460],[963831750,31793390,253159880],[967688420,-9467480,-64248670],[973362910,208028950,-67041890],[990960090,-260302030,206973360],[1018719710,94253200,-4759060],[1042461050,-76072250,102176640],[100843014,-554476498,-80803471],[54576523,-557100114,-132222383],[147109506,-596760201,-171977242]
]
NAME='QW49J_LOW62_G9_INPUT.json'
DATA=dict(name='QW49J_LOW62_G9',kind='V',denominator=10**9,rows=ROWS,source='QW49J_LOW62_B20_AUDIT.json',rounding='rational ties-to-even')
raw=(json.dumps(DATA,sort_keys=True,separators=(',',':'))+'\n').encode()
assert len(raw)==2182 and hashlib.sha256(raw).hexdigest()=='90cc88f1a89396ed5cbe20e84cb4fc8265ae1b4170cc2d5bf245c024d4c4662e'
Path(NAME).write_bytes(raw)
```

## FILE numeric142.py
```python
"""Numerical nomination only: homothetic-shell first-moment separators.
Run from the directory containing input142.py. No mechanical class is inferred.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import json,heapq
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from input142 import ROWS

def geometry(X):
    X=np.asarray(X,float)
    h=ConvexHull(X)
    F=h.simplices.copy()
    c=X.mean(0)
    for t in F:
        a,b,d=X[t]
        if np.dot(np.cross(b-a,d-a),a-c)<0:t[1],t[2]=t[2],t[1]
    A=X[F[:,0]];B=X[F[:,1]];C=X[F[:,2]]
    det=np.einsum('ij,ij->i',A,np.cross(B,C))
    V=det.sum()/6
    M=(det[:,None]*(A+B+C)).sum(0)/24
    return F,V,M

def raytree(R,root):
    unit=R/np.linalg.norm(R,axis=1)[:,None]
    cosine=unit@unit.T
    cost=np.full_like(cosine,np.inf)
    np.log(np.clip(cosine,1e-300,1),out=cost,where=cosine>0)
    cost=-cost
    cost[cosine<=0]=np.inf
    np.fill_diagonal(cost,np.inf)
    n=len(R);dist=np.full(n,np.inf);dist[root]=0
    parent=np.full(n,-1,dtype=int);q=[(0.,root)]
    while q:
        d,j=heapq.heappop(q)
        if d!=dist[j]:continue
        for i in range(n):
            v=d+cost[i,j]
            if v<dist[i]:
                dist[i]=v;parent[i]=j;heapq.heappush(q,(v,i))
    p=np.empty(n);p[root]=1
    for i in np.argsort(dist):
        if i!=root:
            j=parent[i];assert j>=0
            p[i]=np.dot(R[i],R[j])/np.dot(R[i],R[i])*p[j]
    return p,parent,dist

def positive_moment(n,X,F):
    """Integral max(n.x,0) over a hull containing zero; positive origin tetrahedra."""
    T=X[F]
    det=np.einsum('ij,ij->i',T[:,0],np.cross(T[:,1],T[:,2]))
    assert det.min()>-1e-12
    hs=np.sort(T@n,axis=1)
    a,b,c=hs.T # a<=b<=c
    vals=np.zeros(len(F))
    full=a>=0
    vals[full]=a[full]+b[full]+c[full]
    one=(c>0)&(b<=0)
    vals[one]=c[one]**3/((c[one]-a[one])*(c[one]-b[one]))
    two=(b>0)&(a<0)
    aa=b[two];bb=c[two];cc=a[two]
    vals[two]=(aa*bb*(aa+bb)-cc*(aa*aa+aa*bb+bb*bb))/((aa-cc)*(bb-cc))
    return np.dot(det,vals)/24

def separator(X,F,V,M):
    n0=M/np.linalg.norm(M)
    seed=np.eye(3)[np.argmin(abs(n0))]
    e1=np.cross(n0,seed);e1/=np.linalg.norm(e1)
    e2=np.cross(n0,e1);basis=np.array([e1,e2]).T
    def fun(z):return positive_moment(n0+basis@z,X,F)
    o=minimize(fun,[0.,0.],method='BFGS',jac='3-point',options=dict(gtol=1e-11,maxiter=500))
    n=n0+basis@o.x;n/=np.linalg.norm(n)
    ni=np.round(n*10**6).astype(int)
    Jp=positive_moment(ni/1e6,X,F);Jm=Jp-np.dot(ni/1e6,M)
    alpha=(Jm/Jp)**.25
    return dict(n=ni.tolist(),alpha=alpha,epsilon=1-alpha,Jplus=Jp,Jminus=Jm,
                status=int(o.status),success=bool(o.success),jac=o.jac.tolist(),
                z=o.x.tolist(),message=str(o.message))

def main():
    X=np.array(ROWS,float)/1e9
    F,V,M=geometry(X);g=M/V;R=X-g
    rec=dict(parent_faces=F.tolist(),parent_centroid=g.tolist(),parent_volume=V,roots={})
    for root in [9,45]:
        p,parent,dist=raytree(R,root);H=p[:,None]*R
        FH,VH,MH=geometry(H)
        s=separator(H,FH,VH,MH)
        d=dict(parent=parent.tolist(),p=p.tolist(),V=VH,g=(MH/VH).tolist(),separator=s,
               approx_faces=FH.tolist(),pmin=float(min(p)),pmax=float(max(p)))
        rec['roots'][str(root)]=d
        print(root,json.dumps({k:v for k,v in d.items() if k not in ['p','parent','approx_faces']}),flush=True)
    Path('NOMINATE142.json').write_text(json.dumps(rec,sort_keys=True,indent=2)+'\n')
if __name__=='__main__':main()
```

## FILE caps142.py
```python
"""Finite maximum-volume centroid-balanced cap experiments; numerical only.
Dependencies: exact142.py output, literal LOW62 input, numeric142.py.
Each frozen endpoint stores all raw binary64 points. No mechanical acceptance
or global family exclusion is inferred from any optimizer status or count.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
from fractions import Fraction as Q
import json
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from numeric142 import geometry

def edges_of(F):
    return np.unique(np.sort(np.concatenate([F[:,[0,1]],F[:,[1,2]],F[:,[2,0]]]),axis=1),axis=0)

def clipped(X,F,lam):
    X=np.asarray(X,float);E=edges_of(F);h=1+X@lam
    cross=E[h[E[:,0]]*h[E[:,1]]<0]
    C=X[cross[:,0]]+(h[cross[:,0]]/(h[cross[:,0]]-h[cross[:,1]]))[:,None]*(X[cross[:,1]]-X[cross[:,0]])
    Y=np.vstack([X[h>=0],C]);FY,V,M=geometry(Y)
    return Y,FY,V,M

def capcentre(X,initial=None):
    F,V,M=geometry(X)
    cache={}
    def calc(lam):
        key=tuple(lam)
        if key not in cache:
            Y,FY,v,m=clipped(X,F,lam)
            cache.clear();cache[key]=(float(v+lam@m),m,Y,FY,v)
        return cache[key]
    def obj(lam):return calc(lam)[:2]
    if initial is None:initial=np.zeros(3)
    o=minimize(obj,initial,jac=True,method='BFGS',options=dict(gtol=1e-12,maxiter=500))
    f,m,Y,FY,v=calc(o.x)
    return o,Y,FY,v,m,float(V),float(f)

def persistence(X,edges):
    X=np.asarray(X,float);r=np.einsum('ij,ij->i',X,X)
    events=[(float(h),1,i,-1)for i,h in enumerate(r)]
    for i,j in edges:
        d=X[j]-X[i];dd=d@d
        if dd<=0:continue
        s=-X[i]@d/dd
        if s<=0:h=r[i]
        elif s>=1:h=r[j]
        else:
            f=X[i]+s*d;h=min(float(f@f),r[i],r[j])
        events.append((float(h),0,int(i),int(j)))
    events.sort(reverse=True);parent=list(range(len(X)));birth=r.copy();owner=list(range(len(X)));bars=[]
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for h,kind,i,j in events:
        if kind:continue
        a=find(i);b=find(j)
        if a==b:continue
        if (birth[a],-owner[a])<(birth[b],-owner[b]):a,b=b,a
        if birth[b]>h:
            bars.append(dict(depth=float((birth[b]-h)/birth[b]),birth=float(birth[b]),death=h,root=int(owner[b]),edge=[i,j]))
        parent[b]=a
    return sorted(bars,key=lambda b:-b['depth'])

def diagnosis(X):
    X=np.asarray(X,float);h=ConvexHull(X);F,V,M=geometry(X);g=M/V;P=X-g
    groups=[];ids=[]
    for eq in h.equations:
        ind=next((k for k,q in enumerate(groups)if np.max(abs(eq-q))<1e-9),None)
        if ind is None:ind=len(groups);groups.append(eq.copy())
        ids.append(ind)
    owners={}
    for fi,t in enumerate(h.simplices):
        for a,b in zip(t,np.roll(t,-1)):
            owners.setdefault(tuple(sorted((int(a),int(b)))),set()).add(ids[fi])
    true=[e for e,o in owners.items()if len(o)==2];active=sorted({i for e in true for i in e})
    dual=sorted({tuple(sorted(owners[e]))for e in true})
    Qp=np.array([q[:3]/(-q[3]-q[:3]@g)for q in groups])
    def roots(Z):
        c=Z@Z.T-np.einsum('ij,ij->i',Z,Z)[:,None]
        np.fill_diagonal(c,-np.inf);s=c.max(1)
        return dict(strict_below_minus_1e10=np.flatnonzero(s < -1e-10).tolist(),
                    nearzero_abs_1e10=np.flatnonzero(abs(s)<=1e-10).tolist(),max_scores=s.tolist())
    pp=persistence(P[active],[(active.index(i),active.index(j))for i,j in true]);qq=persistence(Qp,dual)
    return dict(V=len(active),E=len(true),F=len(groups),volume=float(V),centroid=g.tolist(),
                P=pp,Q=qq,primal=roots(P[active]),polar=roots(Qp),group_tolerance=1e-9,
                P_count=len(pp),Q_count=len(qq),active_input_indices=active)

def main():
    data=json.loads(Path('EXACT142.json').read_text());raw=json.loads(Path('QW49J_LOW62_G9_INPUT.json').read_text())
    g=np.array([float(Q(t))for t in data['parent_centroid']]);R=np.array(raw['rows'],float)/raw['denominator']-g
    rec={}
    recipe=json.loads(Path('RECIPE142.json').read_text())
    for root in [9,45]:
        p=np.array([float(Q(t))for t in data['roots'][str(root)]['p']]);parent=recipe['roots'][str(root)]['parent'];depth=np.zeros(len(p),int)
        def dep(i):
            if i==root:return 0
            if depth[i]:return int(depth[i])
            depth[i]=dep(parent[i])+1;return int(depth[i])
        for i in range(len(p)):dep(i)
        for slack in [0.,.001,.003,.01,.03,.1]:
            H=R*(p*np.exp(-slack*depth))[:,None]
            o,Y,F,V,M,VH,obj=capcentre(H)
            d=diagnosis(Y)
            tag=f'ROOT{root}_SLACK{slack:g}'
            v=dict(root=root,slack=slack,depths=depth.tolist(),lambda_=o.x.tolist(),status=int(o.status),
                   success=bool(o.success),message=str(o.message),iterations=int(o.nit),old_volume=VH,
                   cap_volume=V,volume_ratio=V/VH,objective=obj,centroid=(M/V).tolist(),
                   old_root_cap_value=float(1+o.x@H[root]),points=Y.tolist(),diagnosis=d)
            rec[tag]=v
            Path('CAPS142_NUMERICAL.json').write_text(json.dumps(rec,sort_keys=True,indent=2)+'\n')
            print(tag,'maxdepth',max(depth),'V/E/F',d['V'],d['E'],d['F'],'P/Q',d['P_count'],d['Q_count'],
                  'g',float(np.linalg.norm(M/V)),'fraction',V/VH,'rootvalue',v['old_root_cap_value'],'status',o.status,flush=True)
if __name__=='__main__':main()
```

## FILE core142.py
```python
"""Nominate root-and-centroid-reflection core moment exclusions. Numerical only.
The exact companion must check any proposed fixed alpha and integer normal.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
from fractions import Fraction as Q
import json
import numpy as np
from scipy.optimize import minimize
from numeric142 import geometry,positive_moment

def core(H,root,alpha,reflection=True):
    blocks=[alpha*H,H[[root]]]
    if reflection:blocks.extend([-alpha*H/3,-H[[root]]/3])
    return np.vstack(blocks)

def bestgap(H,FH,MH,B,initial=None):
    FB,VB,MB=geometry(B)
    n0=MH/np.linalg.norm(MH);seed=np.eye(3)[np.argmin(abs(n0))]
    e1=np.cross(n0,seed);e1/=np.linalg.norm(e1);e2=np.cross(n0,e1);E=np.array([e1,e2]).T
    def fun(z):
        n=n0+E@z
        return positive_moment(n,H,FH)-positive_moment(n,B,FB)
    o=minimize(fun,np.zeros(2)if initial is None else initial,method='BFGS',jac='3-point',options=dict(gtol=2e-10,maxiter=250))
    n=n0+E@o.x
    gap=(n@MH-o.fun)/np.linalg.norm(n)
    return gap,n/np.linalg.norm(n),o,dict(core_volume=VB,core_centroid=(MB/VB).tolist(),core_faces=len(FB))

def main():
    data=json.loads(Path('EXACT142.json').read_text());raw=json.loads(Path('QW49J_LOW62_G9_INPUT.json').read_text())
    g=np.array([float(Q(t))for t in data['parent_centroid']]);R=np.array(raw['rows'],float)/raw['denominator']-g
    out={}
    for root in [9,45]:
        p=np.array([float(Q(t))for t in data['roots'][str(root)]['p']]);H=p[:,None]*R;FH,VH,MH=geometry(H)
        for reflection in [False,True]:
            lo=.02;hi=.9;initial=None;trace=[]
            for iteration in range(22):
                a=(lo+hi)/2;B=core(H,root,a,reflection)
                gap,n,o,info=bestgap(H,FH,MH,B,initial);initial=o.x
                trace.append(dict(alpha=a,gap=float(gap),n=n.tolist(),status=int(o.status),jac=o.jac.tolist(),**info))
                if gap>0:hi=a
                else:lo=a
            key=f'{root}_{reflection}'
            a=np.ceil(hi*1e6)/1e6
            B=core(H,root,a,reflection);gap,n,o,info=bestgap(H,FH,MH,B,initial)
            nint=np.round(n*1e6).astype(int)
            FH,_,MH=geometry(H);FB,_,_=geometry(B)
            fixedgap=positive_moment(nint/1e6,B,FB)-positive_moment(-nint/1e6,H,FH)
            out[key]=dict(root=root,reflection=reflection,alpha_numerator=int(round(a*1e6)),alpha_denominator=10**6,n=nint.tolist(),
                          gap=float(fixedgap),status=int(o.status),trace=trace,**info)
            print(key,'alpha',a,'epsilon',1-a,'gap',fixedgap,'n',nint.tolist(),info,flush=True)
            Path('CORE142_NOMINATIONS.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
if __name__=='__main__':main()
```

## FILE replaycaps142.py
```python
"""Recover all twelve numerical cap geometries from frozen affine cuts.
No optimizer is run. The exact142 three-file recovery and numerical142/caps142
sources plus CAPS142_PARAMETERS.json are required. Numerical diagnostics are
not an exact equilibrium audit, especially for roundoff-size positive bars.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib
import numpy as np
from numeric142 import geometry
from caps142 import clipped,diagnosis

def main():
    raw=json.loads(Path('QW49J_LOW62_G9_INPUT.json').read_text());exact=json.loads(Path('EXACT142.json').read_text())
    rec=json.loads(Path('RECIPE142.json').read_text());pars=json.loads(Path('CAPS142_PARAMETERS.json').read_text())
    g=np.array([float(Q(v))for v in exact['parent_centroid']]);R=np.array(raw['rows'],float)/raw['denominator']-g
    out={}
    for key,x in pars.items():
        root=x['root'];p=np.array([float(Q(v))for v in exact['roots'][str(root)]['p']]);parent=rec['roots'][str(root)]['parent'];depth=np.zeros(len(p),int)
        def dep(i):
            if i==root:return 0
            if depth[i]:return int(depth[i])
            depth[i]=1+dep(parent[i]);return int(depth[i])
        for i in range(len(p)):dep(i)
        H=R*(p*np.exp(-x['slack']*depth))[:,None];F,_,_=geometry(H)
        Y,FY,V,M=clipped(H,F,np.array(x['lambda_']))
        h=hashlib.sha256((json.dumps(Y.tolist(),separators=(',',':'))+'\n').encode()).hexdigest()
        assert h==x['points_sha256'],(key,'floating geometry changed',h)
        diag=diagnosis(Y);assert [diag[k]for k in ['V','E','F']]==x['V_E_F']
        assert [diag['P_count'],diag['Q_count']]==x['positive_bar_counts']
        out[key]=dict(points=Y.tolist(),diagnosis=diag,parameters=x)
    b=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();Path('CAPS142_REPLAY.json').write_bytes(b)
    print('J142_TWELVE_FROZEN_CAPS_REPLAY_ALL_FLOAT_POSITIVE_BARS_NO_EXACT_CLASS',len(b),hashlib.sha256(b).hexdigest(),flush=True)
if __name__=='__main__':main()
```

## FILE CAPS142_PARAMETERS.json
```json
{"ROOT45_SLACK0":{"V_E_F":[61,132,73],"centroid":[4.377111239823406e-12,-1.2142390953282626e-12,1.7695358355082763e-12],"iterations":21,"lambda_":[0.21476051794302892,-3.086913222978693,-2.993440654036092],"old_root_cap_value":-1.1820493287829947,"points_sha256":"313f27f330be606e20d8fcf38d4f445527f4c4a6a8586e630cba0ac54ceff74e","positive_bar_counts":[12,14],"root":45,"slack":0.0,"status":2,"success":false,"volume_ratio":0.5371511638265212},"ROOT45_SLACK0.001":{"V_E_F":[57,122,67],"centroid":[1.8967912653549764e-10,-5.4094587357859416e-11,5.915289978242076e-11],"iterations":21,"lambda_":[0.21061888656686897,-3.1086699752628864,-3.0553838152531303],"old_root_cap_value":-1.2338152529235913,"points_sha256":"5360885268b26cde62f1c1b7d3cf9996667d9924de53c6f67d88ca13691f45ea","positive_bar_counts":[7,11],"root":45,"slack":0.001,"status":2,"success":false,"volume_ratio":0.5311473225275865},"ROOT45_SLACK0.003":{"V_E_F":[55,117,64],"centroid":[-5.807021863976527e-12,7.988662447529098e-13,-3.2864315506810555e-12],"iterations":22,"lambda_":[0.2022814517482632,-3.1509839634976338,-3.1812682876560916],"old_root_cap_value":-1.3390672018950749,"points_sha256":"e79b43287bd42f513de845b884f66e6e3f462472e5b44800b152bf0aa53e552f","positive_bar_counts":[8,10],"root":45,"slack":0.003,"status":2,"success":false,"volume_ratio":0.5192202860473275},"ROOT45_SLACK0.01":{"V_E_F":[52,110,60],"centroid":[-2.8541840862197555e-10,1.324696821002064e-10,-2.0833050546160366e-10],"iterations":20,"lambda_":[0.17180769663135137,-3.30375489197369,-3.647878511664347],"old_root_cap_value":-1.7291691329147842,"points_sha256":"3c968bd011517c54586f0b3431aa8bca86875524b3adb40926f4a07478346f93","positive_bar_counts":[7,6],"root":45,"slack":0.01,"status":2,"success":false,"volume_ratio":0.4774112861370519},"ROOT45_SLACK0.03":{"V_E_F":[47,102,57],"centroid":[-1.2165663082114165e-09,6.219619728735381e-10,3.0621138570520853e-10],"iterations":23,"lambda_":[0.0638643010441048,-3.762913548302912,-5.227345621738693],"old_root_cap_value":-3.0550229599101213,"points_sha256":"c1711857ea8d023e854f946a68d3b6633de80382d8d57755fb3cafff6bba3d16","positive_bar_counts":[8,3],"root":45,"slack":0.03,"status":2,"success":false,"volume_ratio":0.3654001362897385},"ROOT45_SLACK0.1":{"V_E_F":[38,77,41],"centroid":[1.1475702433866695e-11,2.6267349030644936e-11,-3.180933641690365e-12],"iterations":46,"lambda_":[-0.5592559387390353,-5.593073592884077,-14.487563693873636],"old_root_cap_value":-10.86507593893634,"points_sha256":"86cfab5a22447c035f6f5d76bdb637fb76c5291990bb99db0364e5f2060149be","positive_bar_counts":[4,2],"root":45,"slack":0.1,"status":0,"success":true,"volume_ratio":0.1160420800020902},"ROOT9_SLACK0":{"V_E_F":[72,174,104],"centroid":[-7.224214594829401e-11,-6.264822308093154e-11,8.053259464874468e-11],"iterations":17,"lambda_":[0.6437510297016359,-0.2232287291176843,2.126335292571933],"old_root_cap_value":-2.151987197889405,"points_sha256":"27138d1b8fad044269faf37df0b6fa01e3443133e2380136fcd118a45dc1f338","positive_bar_counts":[11,15],"root":9,"slack":0.0,"status":2,"success":false,"volume_ratio":0.6079658252200355},"ROOT9_SLACK0.001":{"V_E_F":[71,171,102],"centroid":[-1.219379073517932e-11,-1.997435694915681e-11,3.59812886995835e-11],"iterations":17,"lambda_":[0.6799718596840908,-0.2143971832129086,2.155392368331494],"old_root_cap_value":-2.2133697738389135,"points_sha256":"651b3beb53beb3e72f888a16fa352a43e75a8dbf9d2d20aabbd459175c1e7334","positive_bar_counts":[8,13],"root":9,"slack":0.001,"status":2,"success":false,"volume_ratio":0.6005947453275262},"ROOT9_SLACK0.003":{"V_E_F":[72,172,102],"centroid":[-2.5921757662374025e-11,-3.340840951747221e-11,-4.528709986130624e-11],"iterations":15,"lambda_":[0.7517839054895299,-0.19643634147706057,2.213474959675756],"old_root_cap_value":-2.3360514656573623,"points_sha256":"4c686b5c2d80763e21d27bf6fdf250362bfc6c62d1a8393cc08147a6633c7445","positive_bar_counts":[9,10],"root":9,"slack":0.003,"status":2,"success":false,"volume_ratio":0.586063859384819},"ROOT9_SLACK0.01":{"V_E_F":[72,167,97],"centroid":[3.993560057267938e-13,-2.4324391614816944e-13,-4.654300739005094e-14],"iterations":19,"lambda_":[0.9993227091764506,-0.13382147717411363,2.4220377813704586],"old_root_cap_value":-2.771422128126839,"points_sha256":"b3c64ed13964d1b597c0d96239fc3ed594e5969f97f06494ab169ffdd14240c7","positive_bar_counts":[8,8],"root":9,"slack":0.01,"status":0,"success":true,"volume_ratio":0.5368573384143653},"ROOT9_SLACK0.03":{"V_E_F":[70,157,89],"centroid":[7.37067507395258e-12,9.940086896912187e-12,1.6869440647864586e-11],"iterations":19,"lambda_":[1.7330728752681803,0.04080030578518593,3.0853090170832878],"old_root_cap_value":-4.119389904037878,"points_sha256":"2ce6687f49505dea55eb503e64ac30e18b0c701d2ef459399dceac2775e7e14a","positive_bar_counts":[7,4],"root":9,"slack":0.03,"status":2,"success":false,"volume_ratio":0.413929447789243},"ROOT9_SLACK0.1":{"V_E_F":[56,119,65],"centroid":[6.904649476552366e-13,-9.482427997921408e-13,-4.804105945307276e-13],"iterations":29,"lambda_":[5.1603654941348305,0.8404433881548704,6.544581561186777],"old_root_cap_value":-10.924471840766383,"points_sha256":"aa410c65ac53bf2ef49752d0ba8e7ff9a42fb79f6f61fea6a18a94316ec0fec9","positive_bar_counts":[8,1],"root":9,"slack":0.1,"status":0,"success":true,"volume_ratio":0.15700258371276204}}
```
