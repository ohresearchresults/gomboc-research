# material-c4546a4edecc

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# SHARP_FIVE_POLE_THREE_ARROWS_V1

Coordinator analytical theorem, not a global E17 exclusion or class110 construction.

## Exact statement
Let x,y,z be independent vectors in dimension three, s1,s2,t1,t2>0, v0=y+s1*x+t1*z, v1=y+s2*x+t2*z. Set D_uv=u^T N(v-u). There is an SPD N with D_yx>=0,D_xz>=0,v0^T N v1<=0 if and only if H>0 and Psi>0, where
A=1+s1+s2, B=s1-s2, C=t1+t2, D=t1-t2,
p=B^2+2*B*D,
L=A^2+2*A*C-p-1=2*(s1+s2+t1+t2)+4*(s1*s2+s1*t2+s2*t1),
K=L^2-4*p,
H=D^2-2*L*t1*t2,
Psi=D^4-4*L*t1*t2*D^2+16*p*(t1*t2)^2.
Whenever weak feasibility exists, strict feasibility exists. H=0 or Psi=0 never permits a full-rank weak realization. No sign hypothesis on B*D is required.
For actual poles a=-beta*v0,b-a=beta_prime*v1, beta,beta_prime>0, the third constraint is D_ab>=0. Equivalently a=-alpha*x-beta*y-c*z,b=m*x+n*y+ell*z, requiring alpha,beta,c,alpha+m,beta+n,c+ell>0. Then s1=alpha/beta,t1=c/beta,s2=(alpha+m)/(beta+n),t2=(c+ell)/(beta+n). Individual m,n,ell need not be positive.

## Complete proof
Absorb N into an invertible linear transformation, normalize ||z||=1, put r=||x||,s=x.z. Independence and D_xz>=0 require 0<r<1,r^2<=s<r. The first arrow is ||y-x/2||<=r/2. The third is
||y+((s1+s2)*x+(t1+t2)*z)/2|| <= ||(s1-s2)*x+(t1-t2)*z||/2.
Independent y exists precisely when these balls have interior overlap:
f(r,s)=r+sqrt(B^2*r^2+D^2+2*B*D*s)-sqrt(A^2*r^2+C^2+2*A*C*s)>0.
B=D=0 is the zero-radius impossible case, and has f<0.
For fixed r, f decreases strictly with s. For BD<=0 this is immediate. For BD>0 let U=B^2*r^2+D^2+2BDs,V=A^2*r^2+C^2+2ACs. Then
(AC)^2*U-(BD)^2*V=A^2*B^2*(C^2-D^2)*r^2+C^2*D^2*(A^2-B^2)+2*AC*BD*(AC-BD)*s>0,
because A>|B|,C>|D|,AC>|BD|. This proves the derivative comparison. Feasibility reduces to f(r,r^2)>0. Strict overlap allows slightly increasing s and choosing y outside span(x,z) in both interiors, hence all three arrows strict.
At s=r^2, V-r^2-U=L*r^2+4*t1*t2>0. Two valid squarings give
K*tau^2-4*H*tau+16*(t1*t2)^2<0,tau=r^2.
Writing S=s1+s2,T=t1+t2 gives L>2(S+T),p<=S^2+2ST, therefore K>4T^2>0. D^2<T^2. The quadratic has a negative value at positive tau exactly if H>0 and Psi>0; its discriminant is 16Psi and constant positive. Its vertex tau*=2H/K then lies in (0,1/2), so tau<1 is automatic. This proves the theorem and its no-SPD tangency boundary.

## Universal one-eighth SOS obstruction
The exact identity
 y.z+||z||^2/8=2||y-x/2+z/4||^2+2D_yx+D_xz/2
shows y.z>=-||z||^2/8 under the first two arrows.
If min(t1,t2)>=1/8, interchange v0,v1 if necessary to set a=t1<=b=t2. Set lambda=2(b-a)+s1+s2, mu=(b-a)/2+s1*b+s2*a. The identity
v0.v1-lambda*D_yx-mu*D_xz
=||y+a*z||^2+2(b-a)||y-x/2+z/4||^2+(b-a)(a-1/8)||z||^2
 +(s1+s2)||y||^2+(s1*b+s2*a+s1*s2)||x||^2
is positive definite in the independent triple, even when a=b=1/8: coefficients nonnegative, and x,y,y+a*z span three coordinates with positive coefficients. Thus Q=sym(v0*v1^T)-lambda*A_yx-mu*A_xz is SPD. For actual poles it is also -A_ab/(beta*beta_prime)-lambda*A_yx-mu*A_xz, contradicting three nonnegative arrows under SPD N. This excludes WEAK arrows, not only strict ones.
The constant 1/8 is sharp as a universal common lower threshold if t2 is unbounded and s1,s2 may approach zero. At s1=s2=0, feasibility reduces to (t1-t2)^2>8*t1*t2*(t1+t2). For every 0<t1<1/8 this holds for sufficiently large t2, and small positive s1,s2 preserve strict feasibility by continuity.

## Four-vector specialization and scope
When b=z, s1=s2=alpha/beta,t1=c/beta,t2=(c+1)/beta. The exact feasibility condition becomes
beta^2-4*c*(c+1)*[4*alpha*(alpha+beta+2*c+1)+2*beta*(2*c+1)]>0.
This proves the former four-vector conjecture in Source D of [internal-source-reference], including equality and rank behavior.
For FULL253's literal tree take x=q5,y=q6,z=q4,a=q2,b=q1, arrows 6->5,5->4,2->1. Actual centroid/facet geometry has NOT yet been shown to imply the coefficient positivity or min(t1,t2)>=1/8 universally. It must establish these, or exclude the complementary sharp feasible region. No global type/orbit count changes are claimed. Vector-only feasible controls are not convex-body/own-centroid controls.

## Complete runnable recovery source
Save the following block as positive_circuit_three_arrows.py, UTF-8, LF, final newline. Python 3 standard library only; no random inputs or non-default precision. Reconstruction and verification: python positive_circuit_three_arrows.py
Expected terminal marker: SHARP_POSITIVE_CIRCUIT_THREE_ARROWS_PASS 27.
Observed input: positive_circuit_three_arrows.py, 2864 bytes, SHA256 3299e834acdb6b411345303bfcbf3fe1b258d5f43ab71e0881b50f261ee7b0a3.
Observed output: positive_circuit_three_arrows_report.json, 9397 bytes, SHA256 3773e9835115dd96eaee5ea2095f8ab6312c421869c3923ecfdea7e98d177ff2.
The exact checker tests positive/tangent controls and 27 SOS identities/PD matrices. The universal proof is analytical, not inferred from these samples.

```python
"""SHARP_POSITIVE_CIRCUIT_THREE_ARROWS_V1. Python 3 stdlib, exact rationals."""
from fractions import Fraction as F
import json,hashlib
from pathlib import Path

def criterion(s1,s2,t1,t2):
    s1,s2,t1,t2=map(F,(s1,s2,t1,t2)); assert min(s1,s2,t1,t2)>0
    A,C=1+s1+s2,t1+t2; B,D=s1-s2,t1-t2
    p=B*B+2*B*D; L=A*A+2*A*C-p-1; K=L*L-4*p
    assert L==2*(s1+s2+t1+t2)+4*(s1*s2+s1*t2+s2*t1)
    assert K>4*(t1+t2)**2
    H=D*D-2*L*t1*t2; psi=D**4-4*L*t1*t2*D*D+16*p*(t1*t2)**2
    feasible=H>0 and psi>0
    if feasible:
        tau=2*H/K
        assert 0<tau<F(1,2) and K*tau*tau-4*H*tau+16*(t1*t2)**2<0
    return dict(s1=s1,s2=s2,t1=t1,t2=t2,A=A,B=B,C=C,D=D,p=p,L=L,K=K,H=H,psi=psi,feasible=feasible)

def outer(u,v): return [[(F(u[i])*F(v[j])+F(u[j])*F(v[i]))/2 for j in range(3)] for i in range(3)]
def plus(*terms): return [[sum(w*M[i][j] for w,M in terms) for j in range(3)] for i in range(3)]
def arrow(u,v): return outer(u,[v[i]-u[i] for i in range(3)])
def det(M):
    return sum(M[0][j]*(M[1][(j+1)%3]*M[2][(j+2)%3]-M[1][(j+2)%3]*M[2][(j+1)%3]) for j in range(3))
def corollary(s1,s2,a,b):
    s1,s2,a,b=map(F,(s1,s2,a,b)); assert s1>0 and s2>0 and F(1,8)<=a<=b
    x,y,z=tuple(map(F,(1,0,0))),tuple(map(F,(0,1,0))),tuple(map(F,(0,0,1)))
    v0=(s1,F(1),a); v1=(s2,F(1),b)
    lam=2*(b-a)+s1+s2; mu=(b-a)/2+s1*b+s2*a
    Q=plus((F(1),outer(v0,v1)),(-lam,arrow(y,x)),(-mu,arrow(x,z)))
    sos=plus((F(1),outer((0,1,a),(0,1,a))),
             (2*(b-a),outer((-F(1,2),1,F(1,4)),(-F(1,2),1,F(1,4)))),
             ((b-a)*(a-F(1,8)),outer(z,z)),((s1+s2),outer(y,y)),
             ((s1*b+s2*a+s1*s2),outer(x,x)))
    assert Q==sos
    assert Q[0][0]>0 and Q[0][0]*Q[1][1]-Q[0][1]**2>0 and det(Q)>0
    assert not criterion(s1,s2,a,b)['feasible']
    return dict(lambda_yx=lam,lambda_xz=mu,Q=Q)

def clean(v):
    if isinstance(v,F): return str(v)
    if isinstance(v,dict): return {k:clean(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)): return [clean(x) for x in v]
    return v

def main():
    positive=criterion(F(1,1000),F(3,1010),F(1,1000),F(100,101))
    assert positive['feasible']
    tangent=criterion(F(1,10),F(1,10),F(301,5400),F(301,600))
    assert tangent['psi']==0 and tangent['H']>0 and not tangent['feasible']
    cases=[]
    for s1 in (F(1,100),F(3,2),F(10)):
        for s2 in (F(1,100),F(3,2),F(10)):
            for a,b in ((F(1,8),F(1,8)),(F(1,8),F(1000)),(F(7,4),F(7,2))):
                cases.append(corollary(s1,s2,a,b))
    out=json.dumps(clean(dict(positive=positive,tangent=tangent,sos_cases=cases)),sort_keys=True,indent=2)+'\n'
    p=Path('positive_circuit_three_arrows_report.json');p.write_text(out)
    print('SHARP_POSITIVE_CIRCUIT_THREE_ARROWS_PASS',len(cases))
    for p in (Path(__file__),p):
        data=p.read_bytes();print(p.name,len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
```
