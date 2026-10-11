# material-913791c4e563

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# H5 conditioned packet discovery: complete optional sources

These are the exact numerical locator and rationalization sources materially used to discover the four-arrow conditioned certificate. They are NOT the acceptance or reconstruction dependency of the exact result. The exact theorem and source are [internal-source-reference] and [internal-source-reference]. In particular, floating optimizer failure is never a feasibility or exclusion verdict.

Save both code blocks with final LF as explore.py and rationalize.py in one directory. Stack: CPython3.13.5, SymPy1.14.0, NumPy2.3.5, SciPy1.17.0. Commands:

    OPENBLAS_NUM_THREADS=1 python explore.py
    OPENBLAS_NUM_THREADS=1 python rationalize.py

Source pins: explore.py 1969 bytes SHA25625672c3ee61983297bc2b2f47ebfac416c79809637be5b26e91cc0717b3d7452; rationalize.py1034 bytes SHA25631a55560de1933b096e2a3e7ec6334580c2a1c8d0ce79b8be3d61401d61637a0. Numerical explore.json observed2944 bytes SHA2563c31b4659c73814190c3da1731258f5573c110c2c12d2e390a8fbdf8bd863a56. Floating-byte reproducibility is not assumed on a different numerical stack.

The first source searches each deletion of the literal five-packet. It maximizes the covariance-conditioned dual support function at cap48 with four starting points, explicit seeds1,2,3 and the uniform start. Omissions0 and4 produced positive discovery scores; failures of the other three searches are not certified feasibility statements. The second source tests four small integer-weight proposals and rounds a negative-part matrix. Its accepted proposal omitting0 with weights(1,2,3,2) yields the rounded integer matrix [[229,-360,208],[-360,654,-439],[208,-439,330]] at denominator100000, augmented by actual Sigma/1000. The exact source then proves the stronger simple cap63 without any numerical input. The second accepted proportional weights(3,6,9,6) proposal is preserved by this generator but is not promoted as a distinct construction; it uses a separately rounded matrix, not an alias of the smaller exact certificate.

## explore.py
```python
import sympy as S
import numpy as np
from scipy.optimize import minimize
from pathlib import Path
import json
F=S.Rational
Z=tuple(S.Matrix(v) for v in [(F(7,40),0,0),(F(287,800),0,0),(F(7,50),F(14,25),0),(F(7,100),F(63,100),0),(0,F(49,160),0),(0,F(7,40),0),(F(7,160),F(7,160),0),(0,0,1),(F(3,10),0,1),(0,F(3,10),1)])
FACETS=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
D=F(0);K=S.zeros(3,1);J=S.zeros(3)
for f in FACETS:
    for k in range(1,len(f)-1):
        a,b,c=(Z[i] for i in (f[0],f[k],f[k+1]));d=a.dot(b.cross(c));t=a+b+c
        D+=d;K+=d*t/4;J+=d*(t*t.T+a*a.T+b*b.T+c*c.T)/20
G=K/D;C=J/D-G*G.T
PACKET=((0,6),(4,3),(5,7),(6,5),(9,4))
As=[]
for i,j in PACKET:
    a=Z[i]-G;b=Z[j]-Z[i];As.append((a*b.T+b*a.T)/2)
e,U=np.linalg.eigh(np.array(C,float));W=(U/np.sqrt(e))@U.T;V=(U*np.sqrt(e))@U.T
Bs=np.array([W@np.array(a,float)@W for a in As]);KK=48

def phi_grad(w,A):
    Q=-np.einsum('i,ijk->jk',w,A)
    d,R=np.linalg.eigh(Q);neg=d<0
    P=R[:,neg]@R[:,neg].T
    val=np.trace(Q)+(KK-1)*d[neg].sum()
    grad=-np.einsum('jk,ijk->i',np.eye(3)+(KK-1)*P,A)
    return -val,-grad
out=[]
for omit in range(5):
    ids=[i for i in range(5) if i!=omit];A=Bs[ids]
    best=None
    for seed in range(4):
        w=np.ones(4)/4 if seed==0 else np.random.default_rng(seed).dirichlet(np.ones(4))
        r=minimize(phi_grad,w,args=(A,),jac=True,bounds=[(0,1)]*4,constraints={'type':'eq','fun':lambda w: w.sum()-1,'jac':lambda w:np.ones(4)},method='SLSQP',options={'ftol':1e-12,'maxiter':1000})
        if best is None or r.fun<best.fun:best=r
    w=best.x;Q=-np.einsum('i,ijk->jk',w,A);ev,T=np.linalg.eigh(Q)
    print('omit',omit,'success',best.success,'phi',-best.fun,'w',w,'eig',ev,flush=True)
    Np=(T*np.maximum(-ev,0))@T.T
    N=V@Np@V
    out.append({'omit':omit,'ids':ids,'weights':w.tolist(),'phi':-float(best.fun),'N':N.tolist()})
Path('explore.json').write_text(json.dumps(out,indent=2)+'\n')
print('covariance',C)
```

## rationalize.py
```python
# Reuses literal actual-geometry calculations from explore.py, not its optimizer.
exec(open('explore.py').read().split('out=[]')[0])
for omit,ww in [(0,[1,2,3,2]),(0,[3,6,9,6]),(4,[3,1,1,6]),(4,[5,2,2,10])]:
 ids=[i for i in range(5) if i!=omit];AA=Bs[ids]
 val,_=phi_grad(np.array(ww),AA);print(omit,ww,'phi',-val)
 if val<0:
  Qs=-sum((w*As[i] for i,w in zip(ids,ww)),S.zeros(3))
  Qn=W@np.array(Qs,float)@W;ev,T=np.linalg.eigh(Qn)
  NP=(T*np.maximum(-ev,0))@T.T
  NN=V@NP@V
  for den in [10000,100000,1000000,10000000]:
   Nr=S.Matrix([[F(round(t*den),den) for t in row] for row in NN])
   # A small positive actual covariance shift controls rounding both sides.
   Nr+=F(1,1000)*C
   Pr=Qs+Nr
   pmins=[S.factor(Pr[:k,:k].det()) for k in (1,2,3)]
   nmins=[S.factor(Nr[:k,:k].det()) for k in (1,2,3)]
   gap=S.factor(S.trace(C.inv()*(Pr-48*Nr)))
   if min(pmins+nmins)>0 and gap>0:
    print('EXACT',den,'gap',float(gap),'Qdet',Qs.det(),'NROUND',[[round(float(t)*den) for t in row] for row in NN]);break
  else: print('NO EXACT')
```
