# material-4b4d8deb6b3a

AI research material

---

"""Exact uniform-H5 reference-ellipsoid hybrid certificate, Python stdlib only.
All five parameters vary; coefficients use t_i in [-1,1]. Assertions required.
No floating arithmetic, external files, or randomized choices are used.
"""
from fractions import Fraction as F
from itertools import combinations
import hashlib,json,sys
from pathlib import Path
DIM=5;Z=(0,)*DIM
class P:
    def __init__(self,a=0):
        if isinstance(a,P): self.d=a.d
        elif isinstance(a,dict):self.d={e:F(c) for e,c in a.items() if c}
        else:self.d={Z:F(a)} if a else {}
    def __add__(self,b):
        b=P(b);o=dict(self.d)
        for e,c in b.d.items():o[e]=o.get(e,0)+c
        return P(o)
    __radd__=__add__
    def __neg__(self):return P({e:-c for e,c in self.d.items()})
    def __sub__(self,b):return self+-P(b)
    def __rsub__(self,b):return P(b)+-self
    def __mul__(self,b):
        b=P(b);o={}
        for e,c in self.d.items():
            for f,d in b.d.items():
                g=tuple(e[i]+f[i] for i in range(DIM));o[g]=o.get(g,0)+c*d
        return P(o)
    __rmul__=__mul__
    def __truediv__(self,b):return self* (1/F(b))
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        a=self;o=P(1)
        while n:
            if n&1:o=o*a
            n//=2
            if n:a=a*a
        return o
    def bound(self):
        c=self.d.get(Z,F(0));r=sum(abs(v) for e,v in self.d.items() if e!=Z)
        return c-r,c+r
    def zero(self):return not self.d

def dot(a,b):return sum((x*y for x,y in zip(a,b)),P(0))
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def mul(s,a):return [s*x for x in a]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def det(a):return dot(a[0],cross(a[1],a[2]))
def quad(v,A):return dot(v,[dot(row,v) for row in A])
def rat(x):return str(F(x))
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
C=[[296,-103,-122],[-103,271,-112],[-122,-112,422]]
ADJ=[[C[1][1]*C[2][2]-C[1][2]*C[2][1],C[0][2]*C[2][1]-C[0][1]*C[2][2],C[0][1]*C[1][2]-C[0][2]*C[1][1]],
     [C[1][2]*C[2][0]-C[1][0]*C[2][2],C[0][0]*C[2][2]-C[0][2]*C[2][0],C[0][2]*C[1][0]-C[0][0]*C[1][2]],
     [C[1][0]*C[2][1]-C[1][1]*C[2][0],C[0][1]*C[2][0]-C[0][0]*C[2][1],C[0][0]*C[1][1]-C[0][1]*C[1][0]]]
DC=sum(C[0][i]*ADJ[i][0] for i in range(3))
assert C[0][0]>0 and C[0][0]*C[1][1]-C[0][1]**2>0 and DC>0
assert [[sum(C[i][k]*ADJ[k][j] for k in range(3)) for j in range(3)] for i in range(3)]==[[DC*int(i==j) for j in range(3)] for i in range(3)]

# Each endpoint is exact. t_i in [-1,1] is the complete physical box.
BOX=[(F(149,1000),F(151,1000))]*3+[(F(449,1000),F(451,1000)),(F(41,500),F(87,1000))]
ALPHA=F(251,500);GAMMA_UP=F(2783,10000);GAMMA_C_UP=F(73,10);CHI_UP=F(1,80)
K_UP=F(16,27)*GAMMA_C_UP**2
L_UP=F(21,2)
GUARDS=[]

def build(box):
    par=[]
    for i,(l,h) in enumerate(box):
        e=tuple(int(j==i) for j in range(DIM));par.append(P({Z:(l+h)/2,e:(h-l)/2}))
    x,r,p,q,lam=par;s=1-lam
    b=[[P(F(1,4)),P(0)],[1-3*x/4,P(0)],[1-p,p],[q,1-q],[P(0),1-3*r/4],[P(0),P(F(1,4))],[P(F(1,16)),P(F(1,16))]]
    z=[[(1-lam)*v[0],(1-lam)*v[1],P(0)] for v in b]+[[P(0),P(0),P(1)],[lam,P(0),P(1)],[P(0),lam,P(1)]]
    # Literal signed boundary tetrahedral volume D=6Vol and K=D*centroid.
    D=P(0);K=[P(0)]*3
    for face in FACES:
        a=z[face[0]]
        for j in range(1,len(face)-1):
            bb,cc=z[face[j]],z[face[j+1]];d=dot(a,cross(bb,cc))
            D=D+d;K=add(K,mul(d/4,add(add(a,bb),cc)))
    area=(31-24*x*p-24*r*q)/64
    bx=F(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
    by=F(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
    assert (D-(lam+2*area*s*s)).zero()
    kk=[3*s**3*bx/2+s*s*lam*(1-3*x*p/4)/4+lam*lam/4,
        3*s**3*by/2+s*s*lam*(1-3*r*q/4)/4+lam*lam/4,
        area*s*s/2+lam/2+lam*lam/4]
    assert all((a-b).zero() for a,b in zip(K,kk))
    # Seven true basal edge supports, with top support t.
    planar=[([P(0),P(-1)],P(0),P(0),1),
            ([p,p-3*x/4],s*p*(1-3*x/4),lam*p,3),
            ([P(1),P(1)],s,lam,4),
            ([q-3*r/4,q],s*q*(1-3*r/4),lam*q,5),
            ([P(-1),P(0)],P(0),P(0),6),
            ([P(-3),P(-1)],-s/4,P(0),7),
            ([P(-1),P(-3)],-s/4,P(0),2)]
    normals=[None]*9;hs=[None]*9
    normals[0]=[P(0),P(0),P(-1)];hs[0]=P(0)
    normals[8]=[P(0),P(0),P(1)];hs[8]=P(1)
    for n,h,t,f in planar:normals[f]=n+[h-t];hs[f]=h
    H=[D*h-dot(n,K) for n,h in zip(normals,hs)]
    V=[sub(mul(D,v),K) for v in z]
    return par,z,D,K,planar,normals,hs,H,V

def guards(box):
    par,z,D,K,planar,ns,hs,H,V=build(box)
    g=[('volume',D),('gamma_positive',K[2]),('gamma_below_half',D/2-K[2]),('gamma_upper',GAMMA_UP*D-K[2]),
       ('alpha_at_least_1_minus_2gamma',2*K[2]-(1-ALPHA)*D),('alpha_squared_below_gamma',K[2]-ALPHA**2*D)]
    # R turn requirement r=gamma(1+alpha)/(alpha(1-gamma))<3/2;
    # (3/2)*(cos(pi/7))^7<1 follows from cos(pi/7)^7<1/2.
    g.append(('turn_r_below_three_halves',F(3,2)*ALPHA*(D-K[2])-(1+ALPHA)*K[2]))
    for f,(n,h,ff) in enumerate(zip(ns,hs,FACES)):
        g.append((f'positive_support_{f}',H[f]))
        for i in range(10):
            sl=h-dot(n,z[i])
            if i in ff:assert sl.zero(),(f,i)
            else:g.append((f'nonincident_support_{f}_{i}',sl))
    # At each vertex three incident planes have nonzero determinant: true vertices.
    for i in range(10):
        inc=[f for f in range(9) if i in FACES[f]]
        chosen=None
        for triple in combinations(inc,3):
            d=det([ns[f] for f in triple]);lo,hi=d.bound()
            if lo>0:chosen=(triple,d);break
            if hi<0:chosen=(triple,-d);break
        assert chosen is not None,('vertex-rank',i)
        g.append((f'vertex_rank_{i}_{chosen[0]}',chosen[1]))
    for k,(n,h,t,f) in enumerate(planar):
        for i in range(7):
            for j in range(7,10):
                a=z[j][:2];b=z[i][:2]
                rr=(D-K[2])*h-(1+ALPHA)*dot(n,K[:2])+ALPHA*(D-K[2])*dot(n,b)+(1+ALPHA)*K[2]*dot(n,a)
                g.append((f'R_{k}_{i}_{j}',rr))
        for j in range(7,10):
            g.append((f'A_{k}_{j}',2*H[f]-D*(t-dot(n,z[j][:2]))))
    rr=[quad(v,ADJ) for v in V];ll=[quad(n,C) for n in ns]
    for i in range(10):
        for f in range(9):
            g.append((f'Gamma_{i}_{f}',GAMMA_C_UP*DC*H[f]**2-rr[i]*ll[f]))
    for i in range(7,10):
        g.append((f'chi_{i}',(1+CHI_UP)*DC*(D-K[2])**2-C[2][2]*rr[i]))
    return g

def main():
    out={'version':1,'C':C,'detC':DC,'box':[[rat(x) for x in b] for b in BOX],
         'alpha':rat(ALPHA),'gamma_up':rat(GAMMA_UP),'Gamma_up':rat(GAMMA_C_UP),'chi_up':rat(CHI_UP),
         'K_up':rat(K_UP),'L_up':rat(L_UP),'guards':[]}
    # Machin identity and alternating rational bounds give pi>333/106.
    pi_lo=16*sum(((-1)**k*F(1,5)**(2*k+1)/F(2*k+1) for k in range(6)),F(0))-4*F(1,239)
    assert pi_lo>F(333,106)
    cos_up=lambda t:1-t*t/2+t**4/24
    assert cos_up(F(333,106)/7)<F(901,1000)
    assert F(901,1000)**7<F(1,2)
    assert cos_up(F(333,106)/20)**20*cos_up(F(333,106)/18)**18<F(16,27)
    # Exact root-free matrix-product bound at the bounding constants.
    a=K_UP+1;b=K_UP-1
    load=4*K_UP*L_UP-a*a*(1+CHI_UP)-b*b*CHI_UP
    discriminant=load*load-4*a*a*b*b*CHI_UP*(1+CHI_UP)
    assert load>0 and discriminant>0
    margin=ALPHA**2-GAMMA_UP*(1-1/L_UP)
    assert margin>0
    out.update(product_load=rat(load),product_discriminant=rat(discriminant),hybrid_margin=rat(margin))
    gg=guards(BOX);bad=[]
    for name,p in gg:
        lo,hi=p.bound();entry={'name':name,'terms':len(p.d),'lower':rat(lo),'upper':rat(hi)}
        out['guards'].append(entry)
        if lo<=0:bad.append((name,float(lo),float(hi),len(p.d)))
    out['guard_count']=len(gg);out['coefficient_count']=sum(len(p.d) for n,p in gg)
    out['all_positive']=not bad
    path=Path(sys.argv[1] if len(sys.argv)>1 else 'HYBRID_EXACT_REGION.json')
    data=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode();path.write_bytes(data)
    print('GUARDS',len(gg),'COEFFICIENTS',out['coefficient_count'],'BAD',len(bad),flush=True)
    if bad:print(bad,flush=True)
    print(path.name,len(data),hashlib.sha256(data).hexdigest(),flush=True)
    assert not bad,'Positive certificate did not close the whole physical box'
    print('H5_TRUE_CENTROID_REFERENCE_ELLIPSOID_HYBRID_WHOLE_BOX_PASS')
if __name__=='__main__':main()
