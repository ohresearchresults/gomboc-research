# material-541578176d7d

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# BRIDGE79 recovery capsule part 2/3 — exactly centred algebraic body

## Complete dependency and reconstruction
This part requires input.json and exact_bridge.py from BRIDGE79_recovery_part1of3.md, material [internal-source-reference], SHA-256 9a8772ff6ee0c2330d2ed846a4652c1051bbc2c13b4225c73b48a274da55c178. Those complete literal files are necessary, not replaced by the reference. The source below, together with part1, reconstructs the exact mathematical object and its full certificate. Part3 is needed only for the broader numerical searches, not for this proof.
Save the complete source below as interval_centre.py next to the part1 files. Command: `python -B -S interval_centre.py`. CPython3.13.5 standard library only. Source6629 bytes, SHA-256 7354a675bdef31a917f6a8949d9116ebe718e8e023f657fa7ba93513a71e559b. Expected output interval_centre_report.json3429 bytes, SHA-256 08d5c403d8d9f6a553d8695ebeaafa51ddac6ca45a4ee6c3a6fd234c9b904d4e. Expected terminal markers:
```
EXACT_PROJECTIVE_CENTRE_INTERVAL_PASS [79, 231, 154] [28, 21, 47] [0, 0, 0] 3429 08d5c403d8d9f6a553d8695ebeaafa51ddac6ca45a4ee6c3a6fd234c9b904d4e
NO_OWN110_CLAIM
```

## Exact object and theorem
Let K be the literal REFERENCE_BRIDGE79_G8 from parent figure-0549 and q its OLD primary-centroid reference point, exactly given in part1 input.json. Put L=K-q and T_b(x)=x/(1+b dot x). Define b* to be the unique zero of the actual filled-centroid map g(b)=centroid(T_b L) inside the rational box b0+[-10^-45,10^-45]^3, where
```
b0=(0.0516287086156190870476570674664976621516282281332439115,
   -0.2735806392234802083219774691541762748127396236111414059,
    0.0088622111843475384945097582566682574388621576613729747).
```
All displayed decimals here are exact rationals. The body T_b*L is therefore defined exactly by rational input plus an isolated algebraic root, not by a rounded floating point centre. Its exact homogeneous own centroid is(0,0,0), V/E/F=79/231/154, C462, strict own S/U/H=28/21/47, no additional weak equilibria and no zero primitive. This establishes failure of the unique positive-chart projective map that makes this nominated old reference point become the own centroid. It does NOT exclude other nominated points, affine metrics, modifications of the bridge, or the whole projective orbit.

Proof mechanism: write V(b)=integral_L (1+b dot x)^(-4)dx. Its derivative is grad V=-4Vg. Differentiating the centroid gives J=Dg=-5 Sigma-g g^T, where Sigma is the covariance of the uniformly filled IMAGE body. Also Hess V=20 integral xx^T(1+b dot x)^(-6)dx is positive definite on the positive-chart domain, so a zero of g there is unique. Every integration simplex is a positive tetrahedron from0 to an outward boundary triangle; its transformed volume equals its original volume divided by the three nontrivial vertex denominators. The exact formulas for first/second moments yield V,g,J used in the code.

A90-digit decimal Newton predictor merely chooses rational b0 and an exact decimal preconditioner C; it is NOT the proof. All subsequent interval arithmetic rounds every addition, multiplication and division outwards at70digits, with exact rational source coordinates bracketed by directed division. The program encloses J(B) and g(b0), verifies strict inclusion of K=b0-Cg(b0)+(I-CJ(B))(B-b0) into B and an infinity-norm contraction bound below1. Thus the map b->b-Cg(b) has a unique fixed point in B; the verified nonsingularity implicit in the contraction makes it a zero of g. Its maximum contraction-row enclosure is below2.956e-44. Every vertex denominator has lower bound greater than .830470524966192. The original maximal facets and true edges are proved by complete exact supporting-triple enumeration in part1; positive-chart projectivity preserves them.

The interval mechanics test is at the FIXED origin throughout B. This is the own centroid only at b*, not at every b in the box. Every facet side, all-vertex cone inequality and segment/normal-edge inequality excludes zero throughout B. At b*, these prove the complete own census. Primitive negative/zero/positive totals are respectively facet[138,0,324], vertex[6003,0,159], edge[212,0,712]. The actual image volume lies in
[1.600039820981135547750469317565816025710044289103168374052271876002697,
 1.600039820981135547750469317565816025710044301414412665941396603670776].
The generated report contains every stable face, unstable vertex and saddle edge, the Krawczyk image, full pole enclosure and residual brackets. No exact bar depths are asserted for this algebraic object; part1's distinct rational grid control has full exact bars.

## File: interval_centre.py
```python
"""Rigorous decimal-interval enclosure of the unique projective centering pole.
Pure Python standard library; all interval operations round outwards at PREC digits.
Proof uses an interval Krawczyk self-map and a full primitive-sign enclosure.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from fractions import Fraction as F
import json,sys,hashlib
from pathlib import Path
from exact_bridge import build,hull,dot,cross,sub,det
ROOT=Path(__file__).resolve().parent
PREC=70
DOWN=Context(prec=PREC,rounding=ROUND_FLOOR)
UP=Context(prec=PREC,rounding=ROUND_CEILING)

class Iv:
    __slots__=('lo','hi')
    def __init__(self,a,b=None):
        if isinstance(a,Iv):self.lo,self.hi=a.lo,a.hi;return
        if isinstance(a,F):
            self.lo=DOWN.divide(D(a.numerator),D(a.denominator));self.hi=UP.divide(D(a.numerator),D(a.denominator));return
        self.lo=D(a);self.hi=self.lo if b is None else D(b)
        assert self.lo<=self.hi
    def __add__(self,z):
        z=Iv(z);return Iv(DOWN.add(self.lo,z.lo),UP.add(self.hi,z.hi))
    __radd__=__add__
    def __neg__(self):return Iv(self.hi.copy_negate(),self.lo.copy_negate())
    def __sub__(self,z):return self+-Iv(z)
    def __rsub__(self,z):return Iv(z)+-self
    def __mul__(self,z):
        z=Iv(z)
        return Iv(min(DOWN.multiply(a,b) for a in (self.lo,self.hi) for b in (z.lo,z.hi)),max(UP.multiply(a,b) for a in (self.lo,self.hi) for b in (z.lo,z.hi)))
    __rmul__=__mul__
    def __truediv__(self,z):
        z=Iv(z);assert z.lo>0 or z.hi<0,'division interval contains zero'
        return self*Iv(DOWN.divide(D(1),z.hi),UP.divide(D(1),z.lo))
    def __rtruediv__(self,z):return Iv(z)/self
    def __repr__(self):return '[%s,%s]'%(self.lo,self.hi)
    def sign(self):
        if self.lo>0:return 1
        if self.hi<0:return -1
        raise ValueError('unresolved primitive sign '+repr(self))
    def record(self):return [str(self.lo),str(self.hi)]

def source():
    H,q=build('bridge');X,tri,planes,edges,active=hull(H)
    L=[sub(x,q) for x in X];w=[det(L[i],L[j],L[k])/6 for i,j,k in tri]
    assert min(w)>0
    return L,tri,edges,active,w

def image_mass(L,tri,w,b,convert):
    Z=[[convert(x) for x in row] for row in L];den=[1+dot(x,b) for x in Z]
    Y=[[x/d for x in row] for row,d in zip(Z,den)]
    W=[convert(t)/(den[i]*den[j]*den[k]) for t,(i,j,k) in zip(w,tri)]
    V=sum(W);ss=[[sum(Y[i][k] for i in f) for k in range(3)] for f in tri]
    g=[sum(t*s[k] for t,s in zip(W,ss))/(4*V) for k in range(3)]
    raw=[[sum(t*(s[k]*s[l]+sum(Y[i][k]*Y[i][l] for i in f)) for t,s,f in zip(W,ss,tri))/(20*V) for l in range(3)] for k in range(3)]
    cov=[[raw[k][l]-g[k]*g[l] for l in range(3)] for k in range(3)]
    J=[[-5*cov[k][l]-g[k]*g[l] for l in range(3)] for k in range(3)]
    return V,g,J,Y,den

def inverse(A):
    n=len(A);M=[list(row)+[D(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        p=max(range(k,n),key=lambda i:abs(M[i][k]));M[k],M[p]=M[p],M[k]
        v=M[k][k];assert v;M[k]=[x/v for x in M[k]]
        for i in range(n):
            if i!=k:
                v=M[i][k];M[i]=[a-v*b for a,b in zip(M[i],M[k])]
    return [r[n:] for r in M]

def primitive_census(Y,tri,edges,active):
    N=[cross(sub(Y[j],Y[i]),sub(Y[k],Y[i])) for i,j,k in tri]
    support=[dot(n,Y[f[0]]) for n,f in zip(N,tri)]
    assert all(x.sign()==1 for x in support)
    sr=[];ur=[];hr=[];S=[];U=[];H=[]
    for fi,(n,f) in enumerate(zip(N,tri)):
        z=[dot(n,cross(Y[f[k]],Y[f[(k+1)%3]])) for k in range(3)];sg=[v.sign() for v in z]
        sr.extend(sg)
        if min(sg)>0:S.append(fi)
    for i in active:
        z=[dot(Y[i],sub(Y[j],Y[i])) for j in active if j!=i];sg=[v.sign() for v in z];ur.extend(sg)
        if max(sg)<0:U.append(i)
    for (i,j),owners in sorted(edges.items()):
        a=Y[i];e=sub(Y[j],a);ee=dot(e,e);ae=dot(a,e);p=sub([ee*x for x in a],[ae*x for x in e])
        n1,n2=(N[k] for k in owners);aa=dot(n1,n1);ab=dot(n1,n2);bb=dot(n2,n2)
        gram=aa*bb-ab*ab;assert gram.sign()==1
        z=[-ae,ee+ae,bb*dot(p,n1)-ab*dot(p,n2),aa*dot(p,n2)-ab*dot(p,n1)]
        sg=[v.sign() for v in z];hr.extend(sg)
        if min(sg)>0:H.append([i,j])
    assert len(S)+len(U)-len(H)==2
    return {'SUH':[len(S),len(U),len(H)],'S_face_ids':S,'S_cycles':[tri[i] for i in S],'U_input_ids':U,'H_edges':H,'primitive_sign_counts':[[z.count(-1),0,z.count(1)] for z in (sr,ur,hr)],'additional_weak_counts':[0,0,0]}

def main():
    L,tri,edges,active,w=source()
    def dec(q):return D(q.numerator)/D(q.denominator)
    with localcontext() as ctx:
        ctx.prec=90
        b=[D('.051628708615618996'),D('-.27358063922348047'),D('.008862211184347577')]
        history=[]
        for it in range(12):
            V,g,J,_,den=image_mass(L,tri,w,b,dec);assert min(den)>0
            history.append(str(max(map(abs,g))))
            C=inverse(J);step=[dot(row,g) for row in C];b=[x-y for x,y in zip(b,step)]
            if max(map(abs,step))<D('1e-75'):break
        b0=[x.quantize(D('1e-55')) for x in b]
        rad=D('1e-45');B=[Iv(x-rad,x+rad) for x in b0]
        V0,g0,J0,_,_=image_mass(L,tri,w,[Iv(x) for x in b0],Iv)
        VI,gI,JI,YI,denI=image_mass(L,tri,w,B,Iv)
        _,_,J,_,_=image_mass(L,tri,w,b0,dec);C=inverse(J)
        # K=b0-C*g(b0)+(I-C*J(B))*(B-b0) is strictly interior to B.
        R=[[Iv(int(i==j))-sum(Iv(C[i][k])*JI[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        K=[Iv(b0[i])-sum(Iv(C[i][j])*g0[j] for j in range(3))+sum(R[i][j]*Iv(-rad,rad) for j in range(3)) for i in range(3)]
        assert all(B[i].lo<K[i].lo and K[i].hi<B[i].hi for i in range(3))
        rownorm=[sum(max(abs(x.lo),abs(x.hi)) for x in row) for row in R]
        assert max(rownorm)<1
        counts=primitive_census(YI,tri,edges,active)
        out={'precision':PREC,'b0':list(map(str,b0)),'radius':str(rad),'box':[x.record() for x in B],'krawczyk_image':[x.record() for x in K],'contraction_row_bounds':list(map(str,rownorm)),'residual_at_b0':[x.record() for x in g0],'volume_interval':VI.record(),'positive_chart_minimum_lower_bound':str(min(x.lo for x in denI)),'VEF':[len(active),len(edges),len(tri)],'exact_centroid':[0,0,0],'mechanics':counts,'newton_predictor_history':history}
    text=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n';(ROOT/'interval_centre_report.json').write_text(text)
    print('EXACT_PROJECTIVE_CENTRE_INTERVAL_PASS',out['VEF'],counts['SUH'],counts['additional_weak_counts'],len(text.encode()),hashlib.sha256(text.encode()).hexdigest())
    print('NO_OWN110_CLAIM')
if __name__=='__main__':main()
```
