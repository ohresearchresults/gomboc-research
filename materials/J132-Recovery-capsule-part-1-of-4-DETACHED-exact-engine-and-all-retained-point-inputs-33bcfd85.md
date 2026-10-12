# material-33bcfd8523e5

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J132 recovery capsule part 1/4 — exact small-V constructions and reference cells

This part is self-contained for the retained DETACHED point inputs and their exact own/reference census. Parts2/4 preserve numerical producing methods; part3/4 preserves QW source methods; part4/4 preserves common-apex methods and rational parameters. They are different research objects, not four missing fragments of a coordinate array. This part supplies every coordinate needed for its own replay. The separate all-policy QW proof is [internal-source-reference].

## Findings and limits
The unchanged DETACHED_G6 body is47/135/90,C270, own211/weak000/primitive000, P empty and one Q about .46246611091319517. Actual V=4052900436758915819/6000000000000000000 and g approximately(.016816900677785785,.008952937838908213,-.03415340529918704). Its sorted-min-first oriented triangular face labels are S16/18,U6,H43--44; S16=(5,38,45),S18=(5,46,34). These labels are not silently interchangeable with earlier worker labels.
Two distinct exact reference110/weak000/primitive000 centres of this SAME body are c_margin=(6322656281/10^10,1113601609/5e9,-34613141/250000000), roots U6/S26, normalized centroid gap .7519956868801955; and c_near=(957161323/2500000000,117187677/312500000,-3436059199/10^10), U6/S88, gap .6873725479442003. They prove that J131's four-guard exclusion does NOT extend to all witness policies. They do not change the body's own211 class.
The margin MILP was TIME-LIMITED, status1,30seconds,23500nodes; its feasible auxiliary margin .04524232215753143 was not proved optimal. The near MILP returned numerical status0,8759nodes,L-infinity objective .3660476285501147 with eta1e-5; no exact all-policy optimization bound is claimed from that solver status.
A fixed-fan numerical physical continuation gives a new47/135/90,C270 body GUARDED132_near. Its exact own class is(15,20,33),P19/Q14,weak000/primitive000; exact reference110/weak000/primitive000 survives. Its normalized gap .6200119847875744 is smaller but own-equilibrium quality is worse.
An actual-fan continuation retires original point45 at iteration5 and46 at62. The retained FREEFAN132_margin is45/129/86,C258, exact own(14,10,22),P9/Q13,weak000/primitive000; exact reference110/weak000/primitive000. Gap .45219616228176684 is about39.867percent below its starting margin-centre gap, NOT a new own110 result. There were180 accepted numerical steps and46 changes in the actual sorted face list with persistent original point identities. No exact entire-path classification is claimed. Both bodies' complete rational coordinates are encoded below as literal IEEE binary64 hexadecimal values: Fraction(float.fromhex(token)), with no decimal re-rounding. This is the exact mathematical input, not an approximate display.

## Reconstruction and terminal outputs
Save each named fenced file verbatim with its final newline in one directory. Use Python3.13.5,NumPy2.3.5,SciPy1.17.0 (Qhull nominates triangular facets only; EVERY retained support sign, adjacency, filled-volume mass, all S/U/H, weak and primitive-zero signs, and every positive P/Q bar are rationally checked). Set OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. Run:
python geometry132.py
python replay132.py
python project132.py --mode near
python project132.py --mode margin
The replay writes minimal MIP132_near.json/MIP132_margin.json containing only their exact centres; it intentionally does not pretend to reproduce the floating MILP history. Exact terminal markers include J132_EXACT_SEED_REFERENCE110 margin [6] [26], near [6] [88], J132_RETAINED_ENDPOINT_PASS for the stated two bodies, and J132_ALL_DETACHED_RETAINED_INPUTS_PASS.
GUARDED132_near_REPLAY.json is48002 bytes,SHA f35e3211de392b603e5ac7d42ba4ae386234a5aa0b671699626ea398fa1156da. FREEFAN132_margin_REPLAY.json is33916 bytes,SHA 6c6e5500437ef6ff7f132855d54367c03fdca63b3b0297179b28febe88646cfe. Both were regenerated from the literal hex files.
The optional exact ONE-policy nearest-centre projections use eta1e-6. Near's active rows are P34->15,Q89->88,Q28->30, normalized gap about.667444971937. Margin's are Q22->23,Q39->41,P24->28, gap about.615315788776. These are nearest points in the selected closed positive-margin cells, NOT a global lower bound over all policies. The exact rational KKT multipliers, all feasibility inequalities and full reference census are checked by project132.py.

## File identities
geometry132.py6728 bytes/SHA1cc066496a3196e91ae4287f0b2733bd6a90a9cba972cd437c182c82c2a4c8ed; project132.py4437 bytes/SHAef9ec1a7f21f7a0f15baed70a3d37a0b04cd50e00e94b0072d45d8f3bf7c2271; DETACHED_G6.txt1034 bytes/SHAa5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50. The hex point files are3029/2906 bytes with hashes asserted in replay132.py. All sources here are complete runnable units, not isolated fragments.

## File: geometry132.py
```python
#!/usr/bin/env python3
"""J132 exact simplicial geometry and explicit own/reference equilibrium census.
Source adapted from the fully read J131 rational engine. Qhull nominates only;
every used supporting sign is rationally established. Never treats a selected
reference as the homogeneous centroid. No positive persistence cutoff.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import numpy as np
from scipy.spatial import ConvexHull
ROOT=Path(__file__).resolve().parent
O=F(0)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(s,a): return tuple(s*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),O)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def serial(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,np.generic): return x.item()
    if isinstance(x,np.ndarray): return serial(x.tolist())
    if isinstance(x,dict): return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [serial(v) for v in x]
    return x
def write(name,x):
    b=(json.dumps(serial(x),indent=2)+'\n').encode(); (ROOT/name).write_bytes(b)
    return dict(name=name,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def load():
    b=(ROOT/'DETACHED_G6.txt').read_bytes()
    assert len(b)==1034 and hashlib.sha256(b).hexdigest()=='a5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50'
    w=list(map(int,b.split())); n,D=w[:2]; assert len(w)==2+3*n
    return [tuple(F(t,D) for t in w[2+3*i:5+3*i]) for i in range(n)]
def hull(X):
    h=ConvexHull(np.array(X,float)); fs=[]
    for tt in h.simplices:
        t=list(map(int,tt)); a,b,c=[X[i] for i in t]; n=cross(sub(b,a),sub(c,a))
        sg=[dot(n,sub(p,a)) for p in X]
        if max(sg)>0:
            assert min(sg)>=0,'Qhull nominated nonsupport'; t[1],t[2]=t[2],t[1]
        j=t.index(min(t)); fs.append(tuple(t[j:]+t[:j]))
    fs=sorted(fs); assert len(fs)==len(set(fs)); planes=[]; edges={}; directions={}
    for fi,t in enumerate(fs):
        a,b,c=[X[i] for i in t]; n=cross(sub(b,a),sub(c,a)); hh=dot(n,a)
        sg=[dot(n,p)-hh for p in X]
        assert max(sg)==0 and sum(s==0 for s in sg)==3,'Not a strict simplicial hull'
        planes.append((n,hh))
        for j in range(3):
            a,b=t[j],t[(j+1)%3]; key=tuple(sorted((a,b)))
            edges.setdefault(key,[]).append(fi); directions.setdefault(key,[]).append((a,b))
    assert all(len(v)==2 for v in edges.values())
    assert all(v[0]==v[1][::-1] for v in directions.values())
    edges=dict(sorted(edges.items())); vs=sorted({i for t in fs for i in t})
    assert len(vs)-len(edges)+len(fs)==2
    seen={0}; todo=[0]
    while todo:
        i=todo.pop()
        for j in range(3):
            for f in edges[tuple(sorted((fs[i][j],fs[i][(j+1)%3])))]:
                if f not in seen: seen.add(f); todo.append(f)
    assert len(seen)==len(fs)
    return fs,planes,edges,vs
def mass(X,fs):
    V=O; M=(O,O,O)
    for i,j,k in fs:
        a,b,c=X[i],X[j],X[k]; d=det(a,b,c)
        V+=d/6; M=add(M,mul(d/24,add(add(a,b),c)))
    assert V>0
    return V,M,mul(1/V,M)
def persistence(X,edges):
    rad=[dot(p,p) for p in X]; par=list(range(len(X))); peak=rad[:]; links=[]; out=[]
    def root(i):
        while par[i]!=i: par[i]=par[par[i]]; i=par[i]
        return i
    for a,b in edges:
        d=sub(X[b],X[a]); t=max(O,min(F(1),-dot(X[a],d)/dot(d,d)))
        p=add(X[a],mul(t,d)); links.append((dot(p,p),a,b))
    for level,i,j in sorted(links,reverse=True):
        a,b=root(i),root(j)
        if a==b: continue
        if peak[a]<peak[b]: a,b=b,a
        q=1-level/peak[b]; assert q>=0
        if q>0: out.append(dict(root=b,edge=(i,j),birth=peak[b],death=level,depth=q))
        par[b]=a
    return sorted(out,key=lambda z:z['depth'],reverse=True)
def audit(X,reference=None,lattice=None):
    fs,planes,edges,vs=hull(X) if lattice is None else lattice
    V,M,g=mass(X,fs); c=g if reference is None else tuple(reference)
    Y=[sub(p,c) for p in X]; S=[]; U=[]; H=[]; weak=[[],[],[]]; zeros=[0,0,0]
    for f,(t,(n,h)) in enumerate(zip(fs,planes)):
        assert h-dot(n,c)>0,'Reference must be strictly interior'
        sig=[dot(n,cross(Y[t[j]],Y[t[(j+1)%3]])) for j in range(3)]
        zeros[0]+=sum(s==0 for s in sig)
        if min(sig)>0: S.append(f)
        elif min(sig)>=0: weak[0].append(f)
    nb=[[] for _ in X]
    for a,b in edges: nb[a].append(b); nb[b].append(a)
    for i in vs:
        sig=[dot(Y[i],sub(Y[j],Y[i])) for j in nb[i]]; zeros[1]+=sum(s==0 for s in sig)
        if max(sig)<0: U.append(i)
        elif max(sig)<=0: weak[1].append(i)
    for (a,b),(i,j) in edges.items():
        d=sub(Y[b],Y[a]); dd=dot(d,d); aa=-dot(Y[a],d); bb=dd-aa
        p=add(Y[a],mul(aa/dd,d)); n1,n2=planes[i][0],planes[j][0]
        g11,g12,g22=dot(n1,n1),dot(n1,n2),dot(n2,n2); D=g11*g22-g12*g12; assert D>0
        c1=dot(p,n1)*g22-dot(p,n2)*g12; c2=dot(p,n2)*g11-dot(p,n1)*g12
        assert mul(D,p)==add(mul(c1,n1),mul(c2,n2))
        sig=[aa,bb,c1,c2]; zeros[2]+=sum(s==0 for s in sig)
        if min(sig)>0: H.append((a,b))
        elif min(sig)>=0: weak[2].append((a,b))
    assert len(S)+len(U)-len(H)==2
    P=persistence(Y,edges); Q=persistence([mul(1/(h-dot(n,c)),n) for n,h in planes],edges.values())
    assert len(P)==len(U)-1 and len(Q)==len(S)-1
    vc=O; mc=(O,O,O)
    for i,j,k in fs:
        a,b,d=sub(X[i],g),sub(X[j],g),sub(X[k],g); z=det(a,b,d); assert z>0
        vc+=z/6; mc=add(mc,mul(z/24,add(add(a,b),d)))
    assert vc==V and mc==(O,O,O)
    return dict(V=len(vs),E=len(edges),F=len(fs),strict=[len(S),len(U),len(H)],weak=list(map(len,weak)),primitive_zero=zeros,S=S,S_cycles=[fs[i] for i in S],U=U,H=H,P=P,Q=Q,volume=V,moment=M,centroid=g,reference=c,is_own=(c==g))
def rows(X,planes,edges):
    """All true-edge directed escape forms, rationally distance-scaled by max |a|."""
    out=[]
    for a,b in edges:
        for i,j in [(a,b),(b,a)]:
            d=sub(X[j],X[i]); aa=mul(-1,d); bb=dot(X[i],d); w=max(map(abs,aa))
            out.append(dict(kind='P',i=i,j=j,a=aa,b=bb,w=w))
    for a,b in edges.values():
        for i,j in [(a,b),(b,a)]:
            n,h=planes[i]; m,k=planes[j]; nm=dot(n,m); nn=dot(n,n)
            aa=sub(mul(nn,m),mul(nm,n)); bb=nm*h-nn*k; w=max(map(abs,aa)); assert w>0
            out.append(dict(kind='Q',i=i,j=j,a=aa,b=bb,w=w))
    return out
if __name__=='__main__':
    X=load(); a=audit(X); print(write('BASE132.json',a)); print(a['strict'],a['S'],a['U'],[float(b['depth']) for b in a['Q']])
```
The one omitted comment before vc=O in this preserved copy is scientifically inert; the originally executed6728-byte source included the line `# Independent positive tetrahedron expansion at the ACTUAL centroid checks mass.` at that point. Restore that line with four leading spaces to match the stated original source hash exactly. All executable lines are literal. This comment-only difference does not change outputs.

## File: project132.py
```python
#!/usr/bin/env python3
"""Exact Euclidean projection into a positive-margin reference110 policy cell.
Floating minimization nominates active rows only; the KKT certificate and all
feasibility/strict equilibrium tests are rational. This is NOT a projection
onto the union of all policies or an all-geometry lower bound.
"""
from itertools import combinations
from fractions import Fraction as F
import argparse,json
import numpy as np
from scipy.optimize import minimize,LinearConstraint
import geometry132 as e
O=F(0)

def solve(A,b):
    n=len(A[0]);a=[list(row)+[rhs] for row,rhs in zip(A,b)];row=0;piv=[]
    for j in range(n):
        k=next((k for k in range(row,len(a)) if a[k][j]),None)
        if k is None:continue
        a[row],a[k]=a[k],a[row];z=a[row][j];a[row]=[x/z for x in a[row]]
        for k in range(len(a)):
            if k==row:continue
            z=a[k][j]
            if z:a[k]=[x-z*y for x,y in zip(a[k],a[row])]
        piv.append(j);row+=1
    if len(piv)!=n or any(not any(r[:-1]) and r[-1] for r in a):return None
    x=[O]*n
    for k,j in enumerate(piv):x[j]=a[k][-1]
    assert all(e.dot(row,x)==rhs for row,rhs in zip(A,b));return x

def make_cell(X,lat,c,eta):
    fs,H,E,vs=lat;aud=e.audit(X,c,lat);assert aud['strict']==[1,1,0] and aud['weak']==[0,0,0]
    roots={'P':aud['U'][0],'Q':aud['S'][0]};rs=e.rows(X,H,E);sel=[]
    for kind,N in [('P',len(X)),('Q',len(fs))]:
        for i in range(N):
            if i==roots[kind]:continue
            avail=[r for r in rs if r['kind']==kind and r['i']==i]
            best=max(avail,key=lambda r:(e.dot(r['a'],c)+r['b'])/r['w'])
            assert e.dot(best['a'],c)+best['b']>eta*best['w']
            sel.append(best)
    for i,(n,h) in enumerate(H):sel.append(dict(kind='I',i=i,j=-1,a=e.mul(-1,n),b=h,w=max(map(abs,n))))
    assert all(e.dot(r['a'],c)+r['b']>=eta*r['w'] for r in sel)
    return roots,sel

def certificate(rows,g,eta,ids):
    A=[e.mul(-1/r['w'],r['a']) for r in rows];b=[r['b']/r['w']-eta for r in rows]
    gram=[[e.dot(A[i],A[j]) for j in ids] for i in ids]
    lam=solve(gram,[e.dot(A[i],g)-b[i] for i in ids])
    if lam is None or min(lam)<0:return None
    x=g
    for i,l in zip(ids,lam):x=e.sub(x,e.mul(l,A[i]))
    if any(e.dot(a,x)>z for a,z in zip(A,b)):return None
    assert all(e.dot(A[i],x)==b[i] for i in ids)
    d=e.sub(g,x);normal=(O,O,O)
    for i,l in zip(ids,lam):normal=e.add(normal,e.mul(l,A[i]))
    assert d==normal
    return dict(point=x,active=ids,labels=[(rows[i]['kind'],rows[i]['i'],rows[i]['j']) for i in ids],multipliers=lam,distance2=e.dot(d,d),separator_normal=d,separator_offset=e.dot(d,x))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['near','margin'],default='near');args=ap.parse_args()
    X=e.load();lat=e.hull(X);V,M,g=e.mass(X,lat[0]);data=json.loads((e.ROOT/('MIP132_'+args.mode+'.json')).read_text());c=tuple(F(t) for t in data['centre_rational']);eta=F(1,10**6)
    roots,rows=make_cell(X,lat,c,eta)
    Af=np.array([e.mul(-1/r['w'],r['a']) for r in rows],float);bf=np.array([float(r['b']/r['w']-eta) for r in rows]);gf=np.array(g,float)
    res=minimize(lambda x:(.5*np.dot(x-gf,x-gf),x-gf),np.array(c,float),jac=True,method='SLSQP',constraints=[LinearConstraint(Af,-np.inf,bf)],options={'ftol':1e-14,'maxiter':500})
    nominated=list(map(int,np.argsort(abs(Af@res.x-bf))[:12]));cert=None
    for k in range(1,4):
        for ids in combinations(nominated,k):
            cert=certificate(rows,g,eta,list(ids))
            if cert is not None:break
        if cert is not None:break
    assert cert is not None,'No exact KKT found, no global projection claim'
    cert['normalized_gap_sixth']=cert['distance2']**3/V**2
    aud=e.audit(X,cert['point'],lat);assert aud['strict']==[1,1,0] and aud['weak']==[0,0,0]
    out=dict(mode=args.mode,seed=c,eta=eta,roots=roots,rows=rows,projection=cert,census=aud,float_nomination=dict(success=bool(res.success),point=res.x,nit=res.nit),scope='Exact nearest point to own centroid in this ONE closed positive-margin policy cell; not the all-policy union.')
    print(e.write('PROJECTION132_'+args.mode+'.json',out));print('J132_EXACT_REAL_CELL_PROJECTION_PASS',args.mode,cert['labels'],'point',list(map(float,cert['point'])),'distance',float(cert['distance2'])**.5,'normalized',float(cert['normalized_gap_sixth'])**(1/6),'lambda',list(map(float,cert['multipliers'])),flush=True)
if __name__=='__main__':main()
```

## File: replay132.py
```python
#!/usr/bin/env python3
"""Rebuild every retained DETACHED reference/end-point exact census."""
import sys,hashlib
from fractions import Fraction as F
import geometry132 as e
sys.set_int_max_str_digits(0)
CASES=[('GUARDED132_near',47,135,90,[15,20,33],19,14,'434480d50454edff6e81d1f5188b56f410ff593f0563f04fe708c0e705327b98'),('FREEFAN132_margin',45,129,86,[14,10,22],9,13,'efb59335dbdc5b6eff73a25f57af59ef133892326433de88567cfef66bce7b6c')]
def main():
 X=e.load();base=e.audit(X);assert base['strict']==[2,1,1] and base['weak']==[0,0,0]
 seeds={'margin':('6322656281/10000000000','1113601609/5000000000','-34613141/250000000'),'near':('957161323/2500000000','117187677/312500000','-3436059199/10000000000')}
 for name,c in seeds.items():
  z=e.audit(X,tuple(map(F,c)));assert z['strict']==[1,1,0] and z['weak']==[0,0,0] and z['primitive_zero']==[0,0,0];e.write('MIP132_'+name+'.json',dict(centre_rational=c));print('J132_EXACT_SEED_REFERENCE110',name,z['U'],z['S'])
 for name,v,ee,ff,cl,np,nq,sha in CASES:
  raw=(e.ROOT/(name+'_POINTS.hex.txt')).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
  X=[tuple(F(float.fromhex(t))for t in row.split())for row in raw.decode().splitlines()];c=tuple(F(float.fromhex(t))for t in (e.ROOT/(name+'_CENTRE.hex.txt')).read_text().split());lat=e.hull(X);assert len(lat[3])==len(X)
  own=e.audit(X,lattice=lat);ref=e.audit(X,c,lattice=lat);assert [own[k]for k in ['V','E','F']]==[v,ee,ff] and own['strict']==cl and len(own['P'])==np and len(own['Q'])==nq
  assert own['weak']==ref['weak']==own['primitive_zero']==ref['primitive_zero']==[0,0,0] and ref['strict']==[1,1,0]
  d=e.sub(c,own['centroid']);m6=e.dot(d,d)**3/own['volume']**2
  print(e.write(name+'_REPLAY.json',dict(own=own,reference=ref,gap_sixth=m6)));print('J132_RETAINED_ENDPOINT_PASS',name,[v,ee,ff],cl,np,nq,'reference110',float(m6)**(1/6))
 print('J132_ALL_DETACHED_RETAINED_INPUTS_PASS')
if __name__=='__main__':main()
```

## File: DETACHED_G6.txt
```text
47 1000000
-220660 -170809 739992
-470733 -252568 617724
-344429 -201140 695040
-827617 -345105 -7630
-804956 -306141 -196980
-617752 -310722 484546
-802871 -391980 208231
708441 212327 -26773
629324 353053 -32544
109721 -76616 760640
306556 -32243 700380
212446 -60072 735986
469379 -34257 598089
392685 -40271 652622
646907 -14969 394808
537342 -31849 536185
596588 -24705 468240
750839 45997 64966
-102855 -139962 763378
7557 -112190 768796
719082 11448 235222
687865 -2839 316832
740239 27161 150766
750330 69885 -21314
738230 84890 -114933
592447 240452 -366643
659702 196951 -280592
707333 140337 -199650
700973 -34829 -222306
-736323 -274563 -374807
228858 452552 -370941
60624 561672 -200802
142319 490402 -325534
566004 -68026 -372688
612214 -197888 -188679
464617 500011 -71398
-487325 -442504 -463527
552036 118367 -435356
-19326 554813 -63048
350712 442484 -390884
577522 340656 -272794
199735 530859 -305689
-532859 -303654 -567337
-484871 -149126 -645284
472985 292300 -459118
-416022 64364 111262
-193306 -303834 71494
```

## File: GUARDED132_near_CENTRE.hex.txt
```text
0x1.834241b573211p-2 0x1.833f4484016fdp-2 -0x1.412ed31b00dddp-2
```
## File: GUARDED132_near_POINTS.hex.txt
```text
-0x1.3d15c22d66db6p-2 -0x1.f36b8227a76e8p-3 0x1.afd1210864ab9p-1
-0x1.3077693ccd7ccp-1 -0x1.592843c234fbap-2 0x1.686af3352d7e9p-1
-0x1.cd879b0dd50c7p-2 -0x1.1d2360a254d59p-2 0x1.95889ba541842p-1
-0x1.ed95cc7c2c2f4p-1 -0x1.c5271538ec8f0p-2 -0x1.1f7fe9dac4655p-7
-0x1.ebeac10f114dcp-1 -0x1.97ae00ba730f0p-2 -0x1.cbee4e4dd0d6dp-3
-0x1.839869354512ap-1 -0x1.9b9ca665a8f5ap-2 0x1.1ab47c86957a1p-1
-0x1.e0321e6e70258p-1 -0x1.f5f18e0468f2cp-2 0x1.e5df6f71a0441p-3
0x1.90bf7b91a1417p-1 0x1.bf623e3bb9c45p-3 -0x1.a0e1e998d3f0ap-6
0x1.705eee28425a3p-1 0x1.ad3fa28dc7862p-2 0x1.13d1196f3a55cp-6
0x1.11f21aa0ab716p-4 -0x1.179fece919c89p-3 0x1.bbd019b9c8e84p-1
0x1.2af534b08cd4bp-2 -0x1.532b2cffb65acp-4 0x1.98a64f823e7cfp-1
0x1.78d38417932d7p-3 -0x1.e204c6f774d36p-4 0x1.ad6de2ae1b475p-1
0x1.eebe30452cff2p-2 -0x1.69824d3ea200ep-4 0x1.63d65ba21acfbp-1
0x1.90216bcd6464fp-2 -0x1.85956497fdcf4p-4 0x1.7cc819ccd2163p-1
0x1.5f9edacfd293cp-1 -0x1.0f77fbb82dd66p-4 0x1.ccd0b15debabdp-2
0x1.256e89a2000d5p-1 -0x1.59d028ffca582p-4 0x1.3d018c2f80c1ep-1
0x1.49536f997c395p-1 -0x1.3c67bf478b8d0p-4 0x1.11764821c1d4ap-1
0x1.9a024a3afa397p-1 0x1.a4418c864d996p-9 0x1.2ef4974c31e21p-4
-0x1.672b17f478b8ep-3 -0x1.ab752a068a39ep-3 0x1.bd6a9f7e39b60p-1
-0x1.95f4062d57710p-5 -0x1.6aa8756fdaf0dp-3 0x1.c2d5f3286d01cp-1
0x1.873a6c88d867ap-1 -0x1.22ace865d448dp-5 0x1.126faf27216b8p-2
0x1.76a5cfe5c3b50p-1 -0x1.adafcf39ddd84p-5 0x1.71ade5a77a181p-2
0x1.922a9f79a1dc2p-1 -0x1.2b3069604944ep-6 0x1.5fbe5f437320ap-3
0x1.980e0ab5a6106p-1 0x1.198cbd12ed2b4p-5 -0x1.8f44c3a5deb7bp-6
0x1.90fe8374341d3p-1 0x1.856309e96a6fcp-5 -0x1.0c6cc26bf39bep-3
0x1.3bed15587e91cp-1 0x1.cc71b9ee184ffp-3 -0x1.abf8858f9d1b6p-2
0x1.63d4eda09b110p-1 0x1.8a939e0d6fd2ap-3 -0x1.478b7e4f103a8p-2
0x1.7ef70aca92dd1p-1 0x1.c58803ba8688dp-4 -0x1.d229b607cac8bp-3
0x1.7dde284aed79bp-1 -0x1.6b8fd9f66e3bbp-4 -0x1.0385acfb9913ep-2
-0x1.baf4aca259df4p-1 -0x1.72d399e7c7306p-2 -0x1.a441d95cf7574p-2
0x1.9f0cfcbcb9727p-3 0x1.ddc0ec420a65ep-2 -0x1.b011f774f1783p-2
0x1.d636d6c3cecccp-6 0x1.334ffc386e9adp-1 -0x1.d4da10ce8a9dep-3
0x1.b4577fec6f0e9p-4 0x1.04f696dffcaeep-1 -0x1.7bf9ef45ecf40p-2
0x1.2c7ef634152f7p-1 -0x1.cf2b5732f1709p-4 -0x1.8d61d8e7403e2p-2
0x1.4b76bd68d4646p-1 -0x1.05e557004b67ap-2 -0x1.1c7a74d0b0d5cp-3
0x1.18f17836e91e9p-1 0x1.32858482f35c4p-1 -0x1.37c482e317b1fp-6
-0x1.3a25f734e1fe3p-1 -0x1.e8e9558a096a3p-2 -0x1.d3adc3056a007p-2
0x1.245863099fb11p-1 0x1.652c228ba8e83p-4 -0x1.f7a2974b43114p-2
-0x1.d266f675c5193p-5 0x1.416a47701ee5bp-1 0x1.aa8d17b3198cap-9
0x1.5dbc34af27b16p-2 0x1.eb462198f21b9p-2 -0x1.b5faab92931f7p-2
0x1.33f030e394e69p-1 0x1.82aa18992fbbap-2 -0x1.fcbc5f97248bap-3
0x1.5b131ec3d212ap-3 0x1.1edef448a1554p-1 -0x1.64d59956e3600p-2
-0x1.54b41bd9cdfddp-1 -0x1.7f91039fa8091p-2 -0x1.30daa72844652p-1
-0x1.2662abc452d94p-1 -0x1.b055dd6451ec4p-3 -0x1.6039977a0989dp-1
0x1.ec6f19bafb1acp-2 0x1.22bb3b4dd1f08p-2 -0x1.098f1ddd4eed2p-1
-0x1.108a8b720ad9fp-1 0x1.8b7eddbe1a196p-6 0x1.0baca4b15fe16p-3
-0x1.1d29571c70035p-2 -0x1.920cb5b97ff23p-2 0x1.52b0e96885ae7p-4
```
## File: FREEFAN132_margin_CENTRE.hex.txt
```text
0x1.cf0c82c15858ep-2 -0x1.12b219a7985aep-19 0x1.18688aad146e3p-19
```
## File: FREEFAN132_margin_POINTS.hex.txt
```text
-0x1.daef4c0d923a6p-2 -0x1.9a70c0fee2ba8p-2 0x1.442d7d391beacp-1
-0x1.588c0597a85c5p-1 -0x1.c31f78d7975a6p-2 0x1.f9d44bda63a4fp-2
-0x1.229167dfc6825p-1 -0x1.ad78b74383b8fp-2 0x1.29f40c6ff9cd9p-1
-0x1.22f22475ca91ap+0 -0x1.0fddd996bf302p-1 0x1.8cc27c05b6c01p-5
-0x1.f3a8d4c8a2c80p-1 -0x1.02a26221828f4p-1 -0x1.b33beac497b32p-3
-0x1.a9777e80ea0e8p-1 -0x1.e3589662d8e02p-2 0x1.5ecd62c757ff8p-2
-0x1.22d5b45e05d6bp+0 -0x1.10cff5ea370c1p-1 0x1.90c08a5a9e41bp-5
0x1.5fe66b8800d89p-1 0x1.d8f380a172dc5p-7 0x1.94cfb0a758ccfp-5
0x1.5b136fdfa0d42p-1 0x1.dbab30a37ce3fp-2 0x1.023e816f7ebd5p-3
-0x1.234ed3e21e4d3p-3 -0x1.1da2d492b0e43p-2 0x1.71f253da38eb1p-1
0x1.3567ab5971adep-3 -0x1.27a24842134d7p-5 0x1.796db2f1842e9p-1
0x1.cd48898be8bd1p-8 -0x1.2ce2bc74f1f1fp-2 0x1.6590a6838ff9dp-1
0x1.9106bae7ab019p-2 -0x1.139d9361f5b04p-2 0x1.493a1480eb551p-1
0x1.13f3e52321b7cp-2 -0x1.2572bff816e3fp-2 0x1.50dcd03e065e3p-1
0x1.2b0fbc58a417cp-1 -0x1.038b49acfd5cfp-2 0x1.5946cd046f7cfp-2
0x1.0655226465a15p-1 -0x1.85ff7ab645cbap-3 0x1.47abbd96e0e63p-1
0x1.0fd562008008dp-1 -0x1.0c0a00ce99959p-2 0x1.b098e89983811p-2
0x1.4230f6e0744e8p-1 -0x1.5d40023dfc5cep-3 -0x1.6f63019a8edd6p-4
-0x1.7ac7968b297b6p-2 -0x1.89a7058f11587p-2 0x1.573d007afef31p-1
-0x1.052e2bd2e3a6cp-2 -0x1.748bbcbbc0530p-2 0x1.6ebdc1d15e7d4p-1
0x1.416960e853f22p-1 -0x1.eeb11f194de47p-3 0x1.5566a8d4b6ed5p-3
0x1.373dc4bbba9c2p-1 -0x1.fd9f309d68dc9p-3 0x1.0706d742fb3eep-2
0x1.51e8b0d9bd40ep-1 -0x1.cc263c2c1e731p-3 0x1.2164ba1f156cdp-3
0x1.452c71423484bp-1 -0x1.0ccc163e069a9p-3 -0x1.65b9569f42973p-3
0x1.3bcdba061abb3p-1 -0x1.beaa3aee012f0p-4 -0x1.25f85b5532d47p-2
0x1.c36dd973a7488p-2 0x1.f77ddebd64593p-6 -0x1.4089628c39b52p-1
0x1.2296070c89e2ep-1 -0x1.6041e0e62c3f7p-7 -0x1.0cffe926734e3p-1
0x1.23cd0e6828d55p-1 -0x1.5dd0c980ba257p-4 -0x1.be2f3f0dce340p-2
0x1.185d9d7200478p-1 -0x1.248ac1c37105bp-3 -0x1.8f78ae57136e8p-2
-0x1.9e392dae4336cp-1 -0x1.eaef2b37026d3p-2 -0x1.cb18016e93abfp-2
0x1.1418b4d79d6f3p-4 0x1.6456dfc2ea6d3p-2 -0x1.3c94cbcdd0193p-1
-0x1.d973ae54ff814p-5 0x1.cb9ea4fc0f216p-2 -0x1.5a315d220b1a3p-2
-0x1.f964a89b46500p-6 0x1.3c52d85509ac5p-2 -0x1.288ffbaef5fe8p-1
0x1.823e49bec313fp-2 -0x1.44b94deb974eep-3 -0x1.cb90bf9eb9eb7p-2
0x1.ea02abf1810a2p-2 -0x1.285386a62da24p-2 -0x1.04e1154476603p-3
0x1.b85c765d4efcbp-2 0x1.2759d25b2e956p-1 0x1.3f2dc0dcd2b6fp-3
-0x1.9e7a2fbcf1b29p-1 -0x1.eb436b0f993c6p-2 -0x1.cabf36a86a2a2p-2
0x1.8df6019c55c7ap-2 0x1.180b214f37391p-7 -0x1.3fa7f6bdcb49fp-1
-0x1.a4b12d4fb8aafp-3 0x1.183dbf020605bp-1 0x1.65dfc4bf50d44p-3
0x1.580e15d432330p-2 0x1.ba4ea681637c9p-2 -0x1.38558b293c4ffp-1
0x1.189f7f77ea22bp-1 0x1.c2d9d8bc88e8ep-2 -0x1.09dd45d227f8bp-1
0x1.0224a27bac18fp-4 0x1.be4b22bc12ec6p-2 -0x1.1700ff9b00b19p-1
-0x1.94c646ed9f7bcp-1 -0x1.df570949c338ap-2 -0x1.d3d455eba4761p-2
-0x1.1f13b903dc42ep-1 -0x1.254b1e9d3545ep-2 -0x1.1ceddbb60b264p-1
0x1.2836b6a882610p-2 0x1.189d83a93bb01p-3 -0x1.6af9a2f70645ap-1
```
