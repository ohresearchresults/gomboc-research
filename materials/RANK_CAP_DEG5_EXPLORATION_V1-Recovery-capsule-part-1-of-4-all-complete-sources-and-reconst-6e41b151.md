# material-6e41b1510a9b

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# RANK_CAP_DEG5_EXPLORATION_V1 — Recovery capsule part1/4

## Scope and evidence status

These are the complete numerical locators and symbolic discovery programs used before TWO_APEX_RANK_CAP_DEG5_546_V1. The floating optimizers are **NUMERIC_NONPROOF**, not exclusions, polyhedra or attaining examples. Small negative slacks and negative numerical matrix eigenvalues remain explicitly present in the exact observed JSON checkpoints. A success flag is not positive-definiteness or feasibility proof. The unproved symmetric ansatz was exploratory only and is not a premise of the accepted theorem.

The accepted exact proof is separate: source [internal-source-reference] and continuous proof [internal-source-reference]. It uses only the rational multipliers, exact positive principal minors, Bernstein identities and actual geometric hypotheses. It needs none of these floating-point files at runtime.

This four-part recovery object consists of:
1. this complete source/recovery document;
2. complete literal rank_cap_locator.compact.json,24 rows and the recorded selected row;
3. complete literal weighted_cap_locator.compact.json,24 rows and the recorded selected row;
4. complete literal gram_locator.compact.json,all5 slope cases — material [internal-source-reference].

All JSON rows are retained, without rounding, omitted coordinates, omitted failure rows or threshold-based filtering of the archive. The compact JSON is ordinary literal JSON, not encoded data. The reconstruction script below expands it to the exact originally observed reports, including failed optimization status messages. The complete original reports are not needed as additional inputs.

Observed numerical environment: CPython3.13.5,NumPy2.3.5,SciPy1.17.0,SymPy1.14.0. Exact reconstruction uses only CPython standard library. A new floating optimizer run can depend on platform linear algebra; the preserved literal checkpoints, not a fresh run, are authoritative for the old numeric observations.

Save all code blocks as the named files with UTF-8/LF and one final LF. Save parts2,3,4 literally as their compact JSON filenames. Run:

python -S reconstruct_locators.py build
python -S reconstruct_locators.py check

Both were executed successfully. Expected final marker:

RANK_CAP_DEG5_EXPLORATION_RECONSTRUCTION_PASS

Expected full output is:

rank_cap_locator.json 17700 809382ec03245084502692114e99956fd8d33d6a615165e0654463faa9939b87
weighted_cap_locator.json 20413 c319410e832eae53b33b5cd99ca8ac5d1cd0a76b22dcad28ad4923c2e79a602c
gram_locator.json 7309 90035444863f3d9ee7632c35f7599320f0fac04207ba31dbfd760000749e6089
RANK_CAP_DEG5_EXPLORATION_RECONSTRUCTION_PASS

Compact input pins:
rank_cap_locator.compact.json:12146bytes,SHA256 ee0479104b84d812c1983d5b66610013a0e66d99373d9a171ae91ac000f050ac.
weighted_cap_locator.compact.json:14236bytes,SHA256 2381f4b3ba54a7b76d8d105da428fc88f1fa5666ca3cd202d2f9bba5b08f068e.
gram_locator.compact.json:4350bytes,SHA256 1e5e377a582941708e637ba25e78092af03418367328f5d1e37ef9fd7c315b2f.

Source pins:
explore_rank_cap.py:1733bytes,SHA256 4400bf8291b37bc81e61f027602a698fbd746e643466d7aa5d1f247f30aebdcd.
explore_weighted_cap.py:1907bytes,SHA256 4b17a6b625f93b045dfc028765147e8aa9bd880140dd7597cacc5ae2cd51b358.
locate_gram_certificate.py:1417bytes,SHA256 25b09ba13eb8b5d9ca1db3d5decbf1a296e207594184defb631b0423c359f24e.
rationalize_gram.py:1042bytes,SHA256 725ac95208e187d25c7e24b2ea9cb7ede6b1fff19428dca87d27fc9774d10d87.
derive_envelope.py:306bytes,SHA256 308272e6478cb573f185c6e69e0258feed0d3a6ccdcd3c4ba73cd50edb4668ef.
derive_pentagon_exact.py:1107bytes,SHA256 3cadcb75bbaa0ade33351c1b45fd349309b8dc93f2c15d3bba1b8dcc86464394.
symmetric_cap_algebra.py:401bytes,SHA256 9c2336ae3fcb4c75fb4b7263c6d1a126c99c04283484ae829cf1139a2815d435.
reconstruct_locators.py:1376bytes,SHA256 0966f387a10c6e5b34ac484fd41fe47041773545a9e3bd3678d419583b582d96.

To repeat the numerical methods independently, run the named scripts in a new directory after installing exactly the listed dependencies. No command claims a mathematical proof. The rationalization script, run against the preserved gram_locator.json, prints PASS100, mix1/1000, L1351/100 and the exact multipliers used by the accepted source. The denominator and mixing loops, seeds, bounds, tolerances, starting coordinates and all nondefault optimizer parameters appear in full below. No hidden helpers or external checkpoint paths are needed.

## reconstruct_locators.py
```python
"""Recover exact observed NONPROOF reports from the complete literal JSON inputs.
python -S reconstruct_locators.py build
python -S reconstruct_locators.py check
"""
from pathlib import Path
import hashlib,json,sys
assert __debug__
PINS={
 'rank_cap_locator':(12146,'ee0479104b84d812c1983d5b66610013a0e66d99373d9a171ae91ac000f050ac',17700,'809382ec03245084502692114e99956fd8d33d6a615165e0654463faa9939b87'),
 'weighted_cap_locator':(14236,'2381f4b3ba54a7b76d8d105da428fc88f1fa5666ca3cd202d2f9bba5b08f068e',20413,'c319410e832eae53b33b5cd99ca8ac5d1cd0a76b22dcad28ad4923c2e79a602c'),
 'gram_locator':(4350,'1e5e377a582941708e637ba25e78092af03418367328f5d1e37ef9fd7c315b2f',7309,'90035444863f3d9ee7632c35f7599320f0fac04207ba31dbfd760000749e6089')}
if sys.argv[1:] not in (['build'],['check']):raise SystemExit('Usage: build|check')
for stem,(ni,hi,no,ho) in PINS.items():
 b=Path(stem+'.compact.json').read_bytes()
 assert len(b)==ni and hashlib.sha256(b).hexdigest()==hi
 data=(json.dumps(json.loads(b),sort_keys=True,indent=2)+'\n').encode()
 assert len(data)==no and hashlib.sha256(data).hexdigest()==ho
 out=Path(stem+'.json')
 if sys.argv[1]=='build':
  if out.exists():assert out.read_bytes()==data
  out.write_bytes(data)
 else:assert out.read_bytes()==data
 print(out.name,len(data),hashlib.sha256(data).hexdigest())
print('RANK_CAP_DEG5_EXPLORATION_RECONSTRUCTION_PASS')
```

## explore_rank_cap.py
```python
"""Nonproof floating exploration of two-apex shared cap with radius order.
python explore_rank_cap.py; seed and all parameters below.
"""
import json, platform
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import minimize
SEED=190926; STARTS=24
rng=np.random.default_rng(SEED)
def eq(y):
 a,w,v,p,*rest=y; b=np.array(rest[:3]);z=np.array(rest[3:]);q=np.array([w,v,p]);q0=np.array([a,0,1.])
 return np.array([q0@z-1,q@b-1,q@z+p+2])
def ine(y):
 a,w,v,p,*rest=y;b=np.array(rest[:3]);z=np.array(rest[3:]);q=np.array([w,v,p]);q0=np.array([a,0,1.])
 return np.array([b[2]-b@b,z[2]-z@z,q@q0-q@q,1-q0@b,b@b-z@z])
a=np.sqrt(20);base=np.array([a,56/(9*np.sqrt(5)),56/(3*np.sqrt(105)),-7/9,8*np.sqrt(5)/105,4*np.sqrt(105)/105,5/21,2*np.sqrt(5)/105,-4*np.sqrt(105)/105,17/21])
rows=[]
for i in range(STARTS):
 y=base.copy() if i==0 else base+rng.normal(0,.3,size=10)
 y[0]=max(.1,y[0])
 r=minimize(lambda y:y[0]**2,y,method='SLSQP',bounds=[(.1,100),(-100,100),(-100,100),(-3,1)]+[(-1,1)]*6,constraints=[{'type':'eq','fun':eq},{'type':'ineq','fun':ine}],options={'maxiter':3000,'ftol':1e-12})
 rows.append({'i':i,'success':bool(r.success),'u':float(r.fun),'eqmax':float(abs(eq(r.x)).max()),'minslack':float(ine(r.x).min()),'x':r.x.tolist(),'ine':ine(r.x).tolist(),'message':str(r.message)})
valid=[r for r in rows if r['eqmax']<1e-7 and r['minslack']>-1e-7]
res={'scope':'NUMERIC_NONPROOF_NOT_A_BODY','seed':SEED,'starts':STARTS,'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'all_rows':rows,'best':min(valid,key=lambda x:x['u']) if valid else None}
Path('rank_cap_locator.json').write_text(json.dumps(res,sort_keys=True,indent=2)+'\n')
print(json.dumps(res['best'],indent=2))
```

## explore_weighted_cap.py
```python
"""Standalone floating locator, not proof. All starts and parameters explicit."""
from pathlib import Path
import json, platform
import numpy as np, scipy
from scipy.optimize import minimize
SEED=190927;STARTS=24; WEIGHT=180.
rng=np.random.default_rng(SEED)
def parts(y):
 a,w,v,p,*rest=y;return a,np.array([w,v,p]),np.array([a,0.,1.]),np.array(rest[:3]),np.array(rest[3:])
def eq(y):
 a,q,q0,b,z=parts(y);return np.array([q0@z-1,q@b-1,q@z+q[2]+2])
def ine(y):
 a,q,q0,b,z=parts(y);return np.array([b[2]-b@b,z[2]-z@z,q@q0-q@q,1-q0@b,b@b-z@z,z[0]**2+z[1]**2-1e-10])
def objective(y):
 a,q,q0,b,z=parts(y);d=z[0]**2+z[1]**2
 return 16*a*a+WEIGHT*(1-z[2])**2/max(d,1e-10)
base=np.array([5.108369010611363,2.663687191174205,2.2404358786696275,-0.819967697522137,0.1065251837300998,0.48651968200320955,0.4558300525834766,0.10652518373010116,-0.4865196820032146,0.45583005258346954])
rows=[]
for i in range(STARTS):
 y=base.copy() if i==0 else base+rng.normal(0,.15,10);y[0]=max(.1,y[0])
 r=minimize(objective,y,method='SLSQP',bounds=[(.1,100),(-100,100),(-100,100),(-3,1)]+[(-1,1)]*6,constraints=[{'type':'eq','fun':eq},{'type':'ineq','fun':ine}],options={'maxiter':3000,'ftol':1e-10})
 a,q,q0,b,z=parts(r.x);h=(1-z[2])**2/(z[0]**2+z[1]**2)
 rows.append({'i':i,'success':bool(r.success),'objective':float(r.fun),'u':a*a,'h':h,'eqmax':float(abs(eq(r.x)).max()),'minslack':float(ine(r.x).min()),'x':r.x.tolist(),'ine':ine(r.x).tolist(),'message':str(r.message)})
valid=[r for r in rows if r['eqmax']<1e-6 and r['minslack']>-1e-6]
out={'scope':'NUMERIC_NONPROOF_NOT_A_BODY','seed':SEED,'starts':STARTS,'weight':WEIGHT,'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'all_rows':rows,'best':min(valid,key=lambda r:r['objective']) if valid else None}
Path('weighted_cap_locator.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');print(json.dumps(out['best'],indent=2))
```

## locate_gram_certificate.py
```python
"""SDP dual locator via SLSQP eigenvalue constraints. Not an exact proof."""
import json, platform
from pathlib import Path
import numpy as np, scipy
from scipy.optimize import minimize

def D(i,j):
 A=np.zeros((5,5));A[i,j]=1 if i==j else .5;A[j,i]=A[i,j];return A
# vectors: x,b,z,Q,B
E=np.array([D(0,0),D(0,3),D(2,3),D(1,4)])
I=np.array([D(0,4)+D(2,4),D(4,4)-D(3,4),D(1,3),D(1,1)-D(0,1),D(2,2)-D(0,2),D(2,2)-D(1,1)])
Z=np.concatenate([-E,I]);ell=np.array([1.,1.,1.,1.,2.,0.,-1.,0.,0.,0.])
rows=[]
for B in (0.,16.,24.,32.,40.):
 C=D(3,3)-B*D(2,2)
 def mat(y):return C+np.einsum('i,ijk->jk',y,Z)
 def eigen(y):return np.linalg.eigvalsh(mat(y))
 def jac(y):
  w,v=np.linalg.eigh(mat(y));return np.array([np.einsum('i,kij,j->k',v[:,i],Z,v[:,i]) for i in range(5)])
 y0=np.array([-1000.,0.,0.,0.,.1,1.,.1,100.,100.,.1])
 res=minimize(lambda y:-ell@y,y0,jac=lambda y:-ell,method='SLSQP',bounds=[(None,None)]*4+[(0,None)]*6,constraints=[{'type':'ineq','fun':eigen,'jac':jac}],options={'ftol':1e-10,'maxiter':3000})
 r={'B':B,'L':float(ell@res.x),'success':bool(res.success),'message':str(res.message),'x':res.x.tolist(),'eigen':eigen(res.x).tolist(),'matrix':mat(res.x).tolist()};rows.append(r);print(json.dumps(r))
Path('gram_locator.json').write_text(json.dumps({'scope':'NUMERIC_NONPROOF','python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'rows':rows},indent=2,sort_keys=True)+'\n')
```

## rationalize_gram.py
```python
"""Deterministic rational certificate locator; exact minors printed for inspection."""
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as s
rows=json.loads(Path('gram_locator.json').read_text())['rows']
y0=list(map(F,[-1000,0,0,0]))+[F(1,10),F(1),F(1,10),F(100),F(100),F(1,10)]
def D(i,j):
 m=s.zeros(5);m[i,j]=m[j,i]=1 if i==j else s.Rational(1,2);return m
E=[D(0,0),D(0,3),D(2,3),D(1,4)]
I=[D(0,4)+D(2,4),D(4,4)-D(3,4),D(1,3),D(1,1)-D(0,1),D(2,2)-D(0,2),D(2,2)-D(1,1)]
Z=[-a for a in E]+I
C=D(3,3)-24*D(2,2)
for den in [100,1000,10000,100000,1000000]:
 for mix in [F(1,4000),F(1,2000),F(1,1000)]:
  yf=rows[2]['x']; y=[F(round(den*((1-float(mix))*a+float(mix)*float(b))),den) for a,b in zip(yf,y0)]
  M=C+sum((s.Rational(v.numerator,v.denominator)*A for v,A in zip(y,Z)),s.zeros(5))
  minors=[M[:i,:i].det() for i in range(1,6)]
  L=sum(y[:4])+2*y[4]-y[6]
  if min(minors)>0 and L>13:
   print('PASS',den,mix,'L',L,'Y',list(map(str,y)),'minors',minors)
   print(M)
   raise SystemExit
print('NO PASS')
```

## derive_envelope.py
```python
import sympy as s
from scipy.optimize import minimize_scalar
v=s.symbols('v'); c=8*v*v-8*v+1
f=s.factor(v**4*(1-c*c)/(1+v**4-2*v*v*c))
b=s.factor((1-16*v**4)/f)
print(f,b)
fn=s.lambdify(v,b,'numpy');res=minimize_scalar(fn,bounds=(.147,.49999),method='bounded',options={'xatol':1e-14})
print(res.x,res.fun)
```

## derive_pentagon_exact.py
```python
"""Exact symbolic angular-envelope derivation; proposed continuous scope in proof."""
import sympy as s
v=s.symbols('v')
c=8*v*v-8*v+1
N=s.factor(v**4*(1-c*c));D=s.factor(1+v**4-2*v*v*c)
F=s.factor(N/D)
K=s.factor((1-16*v**4)*D-180*N)
print('N',N,'D',D,'F',F,'Kraw',K)
N2,D2=s.fraction(F)
K2=s.Poly(s.expand((1-16*v**4)*D2-180*N2),v)
print('K2',K2.as_expr(),s.factor(K2.as_expr()))
# Factor zero at v=1/2; give positive residual Bernstein on [0,1/2] and [1/4,1/2].
R=s.factor(K2.as_expr()/(1-2*v));print('R',R)
for a,b in [(s.Rational(0),s.Rational(1,2)),(s.Rational(1,4),s.Rational(1,2))]:
 t=s.symbols('t');P=s.Poly(s.expand(R.subs(v,a+(b-a)*t)),t);n=P.degree()
 bs=[s.factor(sum(P.nth(j)*s.binomial(i,j)/s.binomial(n,j) for j in range(i+1))) for i in range(n+1)]
 print('Bernstein',a,b,n,bs)
 if not all(x>0 for x in bs):
  for a2,b2 in [(a,(a+b)/2),((a+b)/2,b)]:
   P=s.Poly(s.expand(R.subs(v,a2+(b2-a2)*t)),t)
   bs=[s.factor(sum(P.nth(j)*s.binomial(i,j)/s.binomial(n,j) for j in range(i+1))) for i in range(n+1)]
   print('split',a2,b2,bs)
print('aux square',s.expand(180*(1+v)**2 + 384 - 500*(1+v)))
```

## symmetric_cap_algebra.py
```python
import sympy as S
p,u,h=S.symbols('p u h',real=True)
t=1/(1+h);alpha2=(1-t)**2/u;c2=t*(1-t)-alpha2
w2=(p*(1+2*t)+1)**2/(4*alpha2);aw= -u*(p*(1+2*t)+1)/(2*(1-t))
v2=(p+3)**2/(4*c2)
f=S.factor(w2+v2+p*p-aw-p)
print('f=',f)
fnum=S.fraction(f)[0];A=fnum.coeff(p,2)
poly=S.Poly(fnum,p);A,B,C=poly.all_coeffs();disc=S.factor(B*B-4*A*C)
print('A=',S.factor(A),'B=',S.factor(B),'C=',S.factor(C),'disc=',disc)
```
