# material-e887e6f905ca

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# RECIPROCAL_PAIR_CONVEX_HULL_V1
## Recovery capsule part 2/2: complete executable algebra and discovery units

Companion proof is [internal-source-reference]. Both parts form the complete capsule. All mathematical scope restrictions and all pins are in part1. These are algebraic/spectral controls, NOT new actual bodies. Save each fence literally with UTF8/LF and final newline.

## reciprocal_pair.py
6139 bytes, SHA2567071b25cdd1bcd3efde82d54fcb48aa959e1510f89a4fa37976e261aa7545980. Python>=3.10 stdlib; coordinator executed CPython3.13.5 build/check.
Commands: python -B -S reciprocal_pair.py build ; python -B -S reciprocal_pair.py check.
Expected marker: RECIPROCAL_PAIR_EXACT_PASS 1370 89424339a0b4208d0cac18e30e84ce85e9cc177e3582ba2c47592800a05d1a45
Output reciprocal_pair.json1370bytes with that SHA256.

```python
#!/usr/bin/env python3
"""Exact algebra for RECIPROCAL_PAIR_CONVEX_HULL_V1. Python >=3.10, stdlib."""
from __future__ import annotations
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib, itertools, json, sys

class P:
    """Rational polynomials in (k,x,y), with exact nonnegative exponents."""
    def __init__(self, value=0):
        if isinstance(value,P): self.c=dict(value.c)
        elif isinstance(value,dict): self.c={e:F(a) for e,a in value.items() if a}
        else: self.c={} if not value else {(0,0,0):F(value)}
    def __add__(self,other):
        q=P(other); out=dict(self.c)
        for e,a in q.c.items(): out[e]=out.get(e,F(0))+a
        return P(out)
    __radd__=__add__
    def __neg__(self): return P({e:-a for e,a in self.c.items()})
    def __sub__(self,other): return self+-P(other)
    def __rsub__(self,other): return P(other)+-self
    def __mul__(self,other):
        out={}
        for e,a in self.c.items():
            for f,b in P(other).c.items():
                g=tuple(e[i]+f[i] for i in range(3))
                out[g]=out.get(g,F(0))+a*b
        return P(out)
    __rmul__=__mul__
    def __truediv__(self,other): return self*F(1,other)
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        ans=P(1)
        for _ in range(n): ans=ans*self
        return ans
    def __eq__(self,other): return self.c==P(other).c
    def eval(self,k,x=0,y=0):
        return sum((a*F(k)**e[0]*F(x)**e[1]*F(y)**e[2] for e,a in self.c.items()),F(0))
    def coefficients_k(self):
        assert all(e[1:]==(0,0) for e in self.c)
        return [str(self.c.get((j,0,0),F(0))) for j in range(1+max((e[0] for e in self.c),default=0))]

def calculation():
    k=P({(1,0,0):1}); x=P({(0,1,0):1}); y=P({(0,0,1):1})
    d=k*k+k+1; u=1+(k-1)*x; v=1+(k-1)*y
    pp=u*v+u+1; qq=u*v+v+1
    ns=[d*(k*a*qq+b*pp)-k*(k+1)*pp*qq for a,b in [(u*v,1),(u,v),(1,u*v)]]
    tables=[
      [3*(k+1),(5*k*k+8*k+5)/2,(k+1)*(2*k*k+3*k+2),
       (4*k*k+7*k+4)/2,(k+1)*(7*k*k+8*k+7)/4,d*(3*k*k+5*k+3)/2,
       (k+1)**3,(k+1)**2*d,(k+1)*d*d],
      [3*(k+1),(k+2)*(2*k+1)/2,k*(k+1),
       (4*k*k+7*k+4)/2,(k+1)*(3*k*k+4*k+3)/4,k*d/2,
       (k+1)**3,d*d/2,P(0)],
      [3*(k+1),(k+2)*(2*k+1)/2,k*(k+1),
       (k*k+4*k+1)/2,(k+1)**3/4,P(0),
       k*(k+1),k*d/2,P(0)]]
    report=[]
    for n,tab in zip(ns,tables):
        reconstructed=P(0)
        for i,j in itertools.product(range(3),repeat=2):
            c=tab[3*i+j]
            assert all(e[1:]==(0,0) and a>0 for e,a in c.c.items())
            reconstructed += (k-1)**2*c*comb(2,i)*x**i*(1-x)**(2-i)*comb(2,j)*y**j*(1-y)**(2-j)
        assert reconstructed==n
        report.append([c.coefficients_k() for c in tab])
    # Check both rational scalar identities used for the universal sum cap.
    xx=x; yy=y; pq=(1+xx+yy)*(xx+yy+xx*yy)
    numer=(xx+yy+xx*yy)+xx*yy*(1+xx+yy)
    assert pq-numer==xx*xx+xx*yy+yy*yy
    # f(x,x^2)=(1+x^2)/(1+x+x^2).
    assert (1+xx*xx)*pq-numer*(1+xx*xx+xx)==(xx*xx-yy)**2
    assert (k*k+1)*(1+xx+xx*xx)-(1+xx*xx)*d==(k-xx)*(k*xx-1)
    # Exact formal spectral control; it is NOT a geometric body.
    kk=9; dd=91
    a=[F(1,40),F(8,40),F(31,40)]
    b=[F(10,40),F(26,40),F(4,40)]
    assert sum(a)==sum(b)==1
    for z in [a,b]:
        zz=sorted(z)
        assert zz[1]<kk*zz[0] and zz[2]<kk*zz[1]
        assert all(F(1,91)<q<F(81,91) for q in z)
    assert all(F(18,91)<a[i]+b[i]<F(82,91) for i in range(3))
    assert kk*a[0]+b[0]-F(90,91)==-F(1871,3640)
    h=[F(9)-F(45,91),-F(45,91),-F(45,91)]
    g=[F(1)-F(45,91),-F(45,91),-F(45,91)]
    ah=sum(a[i]*h[i] for i in range(3));bg=sum(b[i]*g[i] for i in range(3))
    assert ah<0 and bg<0 and ah+bg==-F(1871,3640)
    # All six labelled endpoint spectra and the inverse affine map.
    endpoint=[]
    for order in itertools.permutations(range(3)):
        aa=[None]*3;bb=[None]*3
        for j,i in enumerate(order): aa[i]=[F(81,91),F(9,91),F(1,91)][j];bb[i]=[F(1,91),F(9,91),F(81,91)][j]
        assert bb==[(1/z)/sum(1/t for t in aa) for z in aa]
        X=[(F(91,10)*(9*aa[i]+bb[i])-9)/64 for i in range(3)]
        Y=[(82-91*(aa[i]+bb[i]))/64 for i in range(3)]
        Z=[(F(91,10)*(aa[i]+9*bb[i])-9)/64 for i in range(3)]
        assert X[order[0]]==Y[order[1]]==Z[order[2]]==1
        assert sorted(X)==sorted(Y)==sorted(Z)==[0,0,1]
        endpoint.append([[str(z) for z in row] for row in [aa,bb,X,Y,Z]])
    # A strict convex-hull point which is not reciprocal: noncommuting pair.
    eye=[[F(i==j) for j in range(3)] for i in range(3)]
    w=[1,2,3]
    orth=[[eye[i][j]-F(w[i]*w[j],7) for j in range(3)] for i in range(3)]
    def mm(A,B):
        return [[sum(A[i][l]*B[l][j] for l in range(3)) for j in range(3)] for i in range(3)]
    assert mm(orth,orth)==eye
    def mix(vals):
        mat=[[vals[i] if i==j else F(0) for j in range(3)] for i in range(3)]
        rot=mm(mm(orth,mat),orth)
        return [[(mat[i][j]+rot[i][j])/4+eye[i][j]/6 for j in range(3)] for i in range(3)]
    mixa=mix([F(81,91),F(9,91),F(1,91)])
    mixb=mix([F(1,91),F(9,91),F(81,91)])
    ab=mm(mixa,mixb); ba=mm(mixb,mixa)
    assert ab[0][1]-ba[0][1]==F(5760,405769)
    return {'identity':'RECIPROCAL_PAIR_CONVEX_HULL_V1','interior_nonreciprocal_commutator01':str(ab[0][1]-ba[0][1]),'bernstein_quotient_tables':report,
      'symbolic_identity_count':6,'nonzero_bernstein_entries':sum(bool(c.c) for t in tables for c in t),
      'formal_control':{'A':list(map(str,a)),'B':list(map(str,b)),
        'AH':str(ah),'BG':str(bg),'new_gap':str(ah+bg)},'endpoint_checks':endpoint}

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('usage: python -B -S reciprocal_pair.py build|check')
    data=(json.dumps(calculation(),sort_keys=True,separators=(',',':'))+'\n').encode()
    pin=hashlib.sha256(data).hexdigest()
    path=Path('reciprocal_pair.json')
    if sys.argv[1]=='build': path.write_bytes(data)
    else: assert path.read_bytes()==data, 'report differs from exact reconstruction'
    print('RECIPROCAL_PAIR_EXACT_PASS',len(data),pin)
if __name__=='__main__': main()
```

## explore.py
651bytes SHAf82ebb39473a34f81bdc6a50b1d80692a27e9879fd86ef0a15fcc4327b1f8c11. Optional original exploration, SymPy1.14.0; python explore.py. The stdlib checker above supersedes this as the proof-execution dependency.

```python
import sympy as S
k,u,v,x,y,t=S.symbols('k u v x y t')
P=u*v+u+1; Q=u*v+v+1; d=k*k+k+1
N=[S.expand(d*(k*a*Q+b*P)-k*(k+1)*P*Q) for a,b in [(u*v,1),(u,v),(1,u*v)]]
for z,n in enumerate(N):
 print('N',z+1,S.factor(n))
 F=S.Poly(n.subs({u:1+(k-1)*x,v:1+(k-1)*y}),x,y)
 deg=F.degree_list(); print('degrees',deg)
 for i in range(deg[0]+1):
  for j in range(deg[1]+1):
   b=S.factor(sum(F.coeff_monomial(x**p*y**q)*S.binomial(i,p)/S.binomial(deg[0],p)*S.binomial(j,q)/S.binomial(deg[1],q) for p in range(i+1) for q in range(j+1)))
   coeff=S.Poly(S.expand(b.subs(k,1+t)),t).all_coeffs()
   print(i,j,S.factor(b),'POS' if all(c>=0 for c in coeff) else 'NEG')
```
