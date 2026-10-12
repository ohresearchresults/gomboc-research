# material-54cef57d721e

AI research material

---

#!/usr/bin/env python3
"""Exact global-fold obstruction and original cubic rescue, one H5 tree.
Python >=3.11, standard library, assertions enabled. No parent files required.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib, json, sys
if not __debug__ or sys.version_info < (3, 11):
    raise RuntimeError('Python >=3.11 with assertions enabled is required')
class P:
    def __init__(self,a=0):
        if isinstance(a,P): self.d=a.d.copy()
        elif isinstance(a,dict): self.d={k:F(v) for k,v in a.items() if v}
        else: self.d={} if not a else {(0,0):F(a)}
    def __add__(self,o):
        o=P(o);d=self.d.copy()
        for k,v in o.d.items():d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.d.items()})
    def __sub__(self,o):return self+-P(o)
    def __rsub__(self,o):return P(o)+-self
    def __mul__(self,o):
        o=P(o);d={}
        for (a,b),u in self.d.items():
            for (c,e),v in o.d.items():
                k=(a+c,b+e);d[k]=d.get(k,F(0))+u*v
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,o):return self*(F(1)/F(o))
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        a=P(1)
        for _ in range(n):a=a*self
        return a
    def __eq__(self,o):return self.d==P(o).d
    def value(self,p,q):return sum((v*p**a*q**b for (a,b),v in self.d.items()),F(0))
    def bern(self,n,i,j):
        assert all(a+b<=n for a,b in self.d)
        return sum((v*F(comb(i,a)*comb(j,b),comb(n,a+b)*comb(a+b,a))
                    for (a,b),v in self.d.items() if a<=i and b<=j),F(0))
def sub(a,b):return tuple(a[i]-b[i] for i in range(3))
def dot(a,b):return sum(a[i]*b[i] for i in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sym(a,b):return [[(a[i]*b[j]+a[j]*b[i])/2 for j in range(3)]for i in range(3)]
def form(m,v):return sum(v[i]*m[i][j]*v[j]for i in range(3)for j in range(3))
def minors(m):
    return (m[0][0],m[0][0]*m[1][1]-m[0][1]*m[1][0],
            m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
def ev(m,p,q):return [[a.value(p,q) for a in row]for row in m]
def encode(a):
    if isinstance(a,F):return str(a)
    if isinstance(a,P):return {str(k):str(v)for k,v in sorted(a.d.items())}
    if isinstance(a,dict):return {str(k):encode(v)for k,v in a.items()}
    if isinstance(a,(tuple,list)):return [encode(v)for v in a]
    return a
x,r,l=F(63,64),F(1,3),F(1,256);s=1-l
p,q=P({(1,0):1}),P({(0,1):1})
f=(F(-1),F(1),F(0));ff=[[a*b for b in f]for a in f]
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
       (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=tuple(sorted({tuple(sorted((a,b))) for c in FACES
                   for a,b in zip(c,c[1:]+c[:1])}))
ARROWS=tuple((a,b) for e in EDGES for a,b in (e,e[::-1]))
assert len(EDGES)==17 and len(ARROWS)==34
T=((0,1),(1,2),(3,2),(4,3),(5,6),(6,0),(7,0),(8,2),(9,3))
assert all(e in ARROWS for e in T)
out=dict(T);assert set(out)==set(range(10))-{2}
for a in out:
    for _ in range(10):
        if a==2:break
        a=out[a]
    assert a==2
B=((P(F(1,4)),P(0)),(P(1-3*x/4),P(0)),(1-p,p),(q,1-q),
   (P(0),P(1-3*r/4)),(P(0),P(F(1,4))),(P(F(1,16)),P(F(1,16))))
z=[(s*a,s*b,P(0))for a,b in B]+[(P(0),P(0),P(1)),
    (P(l),P(0),P(1)),(P(0),P(l),P(1))]
area=(31-24*x*p-24*r*q)/64
bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
by=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
V=area*s*s/3+l/6
J=(s**3*bx/4+s*s*l*(1-3*x*p/4)/24+l*l/24,
   s**3*by/4+s*s*l*(1-3*r*q/4)/24+l*l/24,
   area*s*s/12+l/12+l*l/24)
FAN=((0,1,2,8),(0,9,8,2),(0,9,2,3),(0,9,3,4),
     (0,4,5,7),(0,4,7,9),(0,6,7,5),(0,7,8,9))
vfan=P(0);jfan=[P(0)for _ in range(3)];fanvolumes=[]
for ids in FAN:
    a,b,c,d=(z[i]for i in ids)
    v=dot(sub(b,a),cross(sub(c,a),sub(d,a)))/6
    fanvolumes.append(v);vfan+=v
    for k in range(3):jfan[k]+=v*sum(z[i][k]for i in ids)/4
assert vfan==V and all(jfan[k]==J[k]for k in range(3))
actual={};lower={};cubic_identities=0
for edge in ARROWS:
    i,j=edge;u=tuple(V*z[i][k]-J[k]for k in range(3));d=sub(z[j],z[i])
    G=[[-a for a in row]for row in sym(u,d)];actual[edge]=G
    get=lambda a,b:F(edge==(a,b))
    Ia=get(1,2)+get(8,2);Oa=get(2,1)+get(2,8)
    Ib=get(4,3)+get(9,3);Ob=get(3,4)+get(3,9)
    aa=get(2,3);bb=get(3,2)
    A=x*(Ia+3*Oa+3*aa+bb);D=r*(Ib+3*Ob+aa+3*bb)
    E=x*(Ob+3*aa+5*bb-Ib)+4*r*(Oa+aa)
    H=r*(Oa+5*aa+3*bb-Ia)+4*x*(Ob+bb)
    cub=s**4*(A*p**3+E*p*p*q+H*p*q*q+D*q**3)/32
    low=s**4*(A*p*p+D*q*q)/32
    m=[[G[i][j]+(cub-low)*ff[i][j] for j in range(3)]for i in range(3)]
    assert all(all(a+b<=2 for a,b in cell.d)for row in m for cell in row)
    for exp,t in (((3,0),A),((2,1),E),((1,2),H),((0,3),D)):
        for i in range(3):
            for j in range(3):assert G[i][j].d.get(exp,F(0))==-s**4*t*ff[i][j]/32
        cubic_identities+=1
    lower[edge]=m
assert cubic_identities==136
Lx=[[-s**4*x*p*q*ff[i][j]/32 for j in range(3)]for i in range(3)]
Lr=[[-s**4*r*p*q*ff[i][j]/32 for j in range(3)]for i in range(3)]
# Five rational positive rank-one tests, at three GENUINE interior bodies.
eps=F(1,65536)
pts=((F(1,2),eps),(F(1,2)-eps,F(1,2)-eps),(1-2*eps,eps))
raw=((39366201,(-512838,840056,176924),0),
     (46942882,(845464,-528447,-77035),1),
     (53699272,(-513477,839727,176637),0),
     (178511241,(845954,-527715,-76671),1),
     (681480403,(804746,563857,185606),2))
tests=[(F(a,10**9),tuple(F(v,10**6)for v in vv),pts[k])for a,vv,k in raw]
bodydata=[]
for pp,qq in pts:
    assert pp>0 and qq>0 and pp+qq<1
    zz=[tuple(a.value(pp,qq)for a in v)for v in z]
    vol=V.value(pp,qq);g=tuple(a.value(pp,qq)/vol for a in J)
    assert vol>0 and all(a.value(pp,qq)>0 for a in fanvolumes)
    for face in FACES:
        a,b,c=(zz[i]for i in face[:3]);n=cross(sub(b,a),sub(c,a));h=dot(n,a)
        assert any(n)
        for i in range(10):
            delta=h-dot(n,zz[i]);assert delta==0 if i in face else delta>0
        assert h-dot(n,g)>0
    bodydata.append({'p':pp,'q':qq,'vertices':zz,'volume':vol,'centroid':g})
coef=[F(0)]*11
for a,v,(pp,qq) in tests:
    for k,m in enumerate([lower[e]for e in T]+[Lx,Lr]):coef[k]+=a*form(ev(m,pp,qq),v)
Cx,Cr=-coef[9],-coef[10]
assert Cx>0 and Cr>0 and r*Cx==x*Cr
lo=max(F(0),(coef[2]-4*Cx)/3)
hi=min(Cr,-coef[1],-coef[7]);assert lo<hi
mu=(lo+hi)/2;assert 0<mu<Cr
K=coef[:9].copy();K[2]-=4*Cx+3*mu;K[1]+=mu;K[7]+=mu
assert all(k<-F(1,10**6) for k in K)
# Exact unfurled cubic: ONE constant stress rescues the ENTIRE closed triangle.
w=tuple(F(a,10**8) for a in (0,8324309,18456120,9753139,12482147,29902002,21082282,0,0))
W=sum(w);G=[[sum(wk*actual[e][i][j]for wk,e in zip(w,T))for j in range(3)]for i in range(3)]
shift=W/F(100000)
cert=[]
for i in range(4):
    for j in range(4-i):
        M=[[G[a][b].bern(3,i,j)for b in range(3)]for a in range(3)]
        N=[[M[a][b]-(shift if a==b else 0)for b in range(3)]for a in range(3)]
        mm=minors(N);assert all(t>0 for t in mm)
        cert.append({'index':(i,j),'matrix':M,'shifted_leading_minors':mm})
assert len(cert)==10
report=encode({'title':'H5_GLOBAL_FOLD_POINTWISE_OBSTRUCTION_AND_UNFOLDED_CUBIC_RESCUE_V1',
 'parameters':{'x':x,'r':r,'lambda':l},'tree_root':2,'tree':T,
 'facets':FACES,'edges':EDGES,'actual_moment_polynomials':{'V':V,'J':J},
 'cubic_identities':cubic_identities,'actual_bodies':bodydata,
 'pointwise_dual':{'tests':tests,'Cx':Cx,'Cr':Cr,'mu':mu,'coefficients':K,
                   'margin':-max(K),'uniform_lower_bound_on_margin':F(1,10**6)},
 'unfolded_rescue':{'weights':w,'W':W,'degree':3,'uniform_matrix_gap_per_W':F(1,100000),
                    'matrices':cert,'positive_shifted_minors':30},
 'scope':'One complete tree, full p/q triangle at stated fixed x/r/lambda; no new all-root domain or C bound.'})
data=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode()
outdir=Path(sys.argv[1]if len(sys.argv)>1 else '.');outdir.mkdir(parents=True,exist_ok=True)
(outdir/'h5_global_fold_loss.json').write_bytes(data)
print('H5_GLOBAL_FOLD_POINTWISE_OBSTRUCTION_AND_UNFOLDED_CUBIC_RESCUE_PASS',136,9,10,30)
print('REPORT_BYTES_SHA256',len(data),hashlib.sha256(data).hexdigest())
print('FOLD_DUAL_MARGIN',-max(K))
print('UNFOLDED_GAP_PER_WEIGHT',F(1,100000))
