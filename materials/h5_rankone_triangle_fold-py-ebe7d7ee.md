# material-ebe7d7eecfda

AI research material

---

#!/usr/bin/env python3
"""Exact H5 rank-one triangle degree reduction, with a local strict stress control.
Run: python h5_rankone_triangle_fold.py [report.json]
Python >=3.11, SymPy; no numerical solver, random choices or external inputs.
This is a certificate reduction, NOT an all-root free-d exclusion.
"""
import hashlib, json, sys
from pathlib import Path
import sympy as S

Q=S.Rational
x,r,p,q,l=S.symbols('x r p q l')
s=1-l
f=S.Matrix([-1,1,0]); ff=f*f.T
EDGES=((0,1),(0,6),(0,7),(1,2),(1,8),(2,3),(2,8),(3,4),(3,9),(4,5),(4,9),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9))
ARROWS=tuple(a for e in EDGES for a in (e,e[::-1]))
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
BASE=[S.Matrix(v) for v in ((Q(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),(0,1-3*r/4),(0,Q(1,4)),(Q(1,16),Q(1,16))) ]
Z=[S.Matrix([s*b[0],s*b[1],0]) for b in BASE]+[S.Matrix(v) for v in ((0,0,1),(l,0,1),(0,l,1))]
AB=(31-24*x*p-24*q*r)/64
BX=p*p*x/8+3*p*x*x/32-3*p*x/8-q*q*r/8+Q(509,3072)
BY=-p*p*x/8+q*q*r/8+3*q*r*r/32-3*q*r/8+Q(509,3072)
V=AB*s*s/3+l/6
J=S.Matrix([s**3*BX/4+s*s*l*(1-3*x*p/4)/24+l*l/24,s**3*BY/4+s*s*l*(1-3*q*r/4)/24+l*l/24,AB*s*s/12+l/12+l*l/24])

def expanded(a):return a.applyfunc(S.expand) if isinstance(a,S.MatrixBase) else S.expand(a)
def zero(a):return expanded(a)==S.zeros(*a.shape) if isinstance(a,S.MatrixBase) else expanded(a)==0
def stress(i,j):
 a=V*Z[i]-J;b=Z[j]-Z[i]
 return expanded(-(a*b.T+b*a.T)/2)
def hom3(a,u=p,v=q):
 return a.applyfunc(lambda t:S.expand(sum(c*u**i*v**j for (i,j),c in S.Poly(t,u,v).terms() if i+j==3)))
def group(w):
 return (w.get((1,2),0)+w.get((8,2),0), w.get((2,1),0)+w.get((2,8),0),
         w.get((4,3),0)+w.get((9,3),0), w.get((3,4),0)+w.get((3,9),0),
         w.get((2,3),0),w.get((3,2),0))
def six_coeff(w):
 ia,oa,ib,ob,a,b=group(w)
 A=x*(ia+3*oa+3*a+b)
 D=r*(ib+3*ob+a+3*b)
 E=x*(ob+3*a+5*b-ib)+4*r*(oa+a)
 F=r*(oa+5*a+3*b-ia)+4*x*(ob+b)
 Lx=max(ob+3*a+5*b-ib,4*(ob+b))
 Lr=max(4*(oa+a),oa+5*a+3*b-ia)
 return A,D,E,F,x*Lx+r*Lr,Lx,Lr

def triangle_coeff(expr,u,v,n):
 poly=S.Poly(S.expand(expr),u,v)
 assert poly.total_degree()<=n
 return [S.expand(sum(c*S.binomial(k,i)*S.binomial(j,h)/(S.binomial(n,i)*S.binomial(n-i,h))
   for (i,h),c in poly.terms() if i<=k and h<=j))
   for k in range(n+1) for j in range(n+1-k)]
def minors(m):return [S.factor(m[:i,:i].det()) for i in (1,2,3)]
def matrix_strings(m):return [[str(t) for t in row] for row in m.tolist()]

def main(dest):
 # Independent actual polygon and tetrahedral volume/first-moment identities.
 aa=0;jj=S.zeros(2,1)
 for a,b in zip(BASE,BASE[1:]+BASE[:1]):
  d=S.det(S.Matrix.hstack(a,b));aa+=d/2;jj+=d*(a+b)/6
 assert zero(aa-AB) and zero(jj-S.Matrix([BX,BY]))
 tets=((0,1,2,8),(0,9,8,2),(0,9,2,3),(0,9,3,4),(0,4,5,7),(0,4,7,9),(0,6,7,5),(0,7,8,9))
 vv=0;jv=S.zeros(3,1);fan=[]
 for inds in tets:
  a,b,c,d=(Z[i] for i in inds)
  # Listed oriented apex-0 cells have negative determinant; sign fixed once.
  vol=S.factor(S.det(S.Matrix.hstack(b-a,c-a,d-a))/6)
  vals={x:Q(1,2),r:Q(1,3),p:Q(3,8),q:Q(1,4),l:Q(1,2)}
  if vol.subs(vals)<0:vol=-vol
  fan.append(str(S.factor(vol)));vv+=vol;jv+=vol*(a+b+c+d)/4
 assert zero(vv-V) and zero(jv-J)
 # The new triangle cubic formulas and globally valid degree-lowered matrices.
 Gs={};Rs={};bounds=[];cubic_table={}
 for i,j in ARROWS:
  w={(i,j):1};g=stress(i,j);Gs[i,j]=g
  A,D,E,F,L,Lx,Lr=six_coeff(w)
  cubic=(s**4/32)*(-A*p**3-E*p*p*q-F*p*q*q-D*q**3)*ff
  assert zero(hom3(g)-cubic)
  # These six nonnegative factors prove the triangle correction is PSD.
  assert S.Poly(L-E,x,r).coeffs() and all(t>=0 for t in S.Poly(L-E,x,r).coeffs())
  assert S.Poly(L-F,x,r).coeffs() and all(t>=0 for t in S.Poly(L-F,x,r).coeffs())
  assert Lx>=0 and Lr>=0
  correction=(s**4/32)*(A*p*p*(1-p)+D*q*q*(1-q)+p*q*(L*(1-p-q)+(L-E)*p+(L-F)*q))*ff
  low=(s**4/32)*(-A*p*p-D*q*q-L*p*q)*ff
  assert zero(cubic-low-correction)
  ex=S.Matrix([-3*s/4,0,0]);er=S.Matrix([0,-3*s/4,0])
  bx=s*s*p*(3*(i==1)+(j==1))*ex*ex.T/32
  br=s*s*q*(3*(i==4)+(j==4))*er*er.T/32
  R=expanded(g-x*x*(1-x)*bx-r*r*(1-r)*br-correction)
  assert zero(g-R-x*x*(1-x)*bx-r*r*(1-r)*br-correction)
  for e in R:
   pp=S.Poly(e,x,r,p,q,l)
   assert pp.degree(x)<=2 and pp.degree(r)<=2 and pp.degree(l)<=4
   assert all(deg[2]+deg[3]<=2 for deg,co in pp.terms())
  Rs[i,j]=R
  if cubic!=S.zeros(3):cubic_table[f'{i}->{j}']=[str(S.factor(t)) for t in (A,D,E,F,L)]
  bounds.append([i,j,Lx,Lr])
 # Exact degree-two triangle Bernstein basis, all six monomial identities.
 u,v=S.symbols('u v'); inds=[(k,j) for k in range(3) for j in range(3-k)]
 for a in range(3):
  for b in range(3-a):
   co=triangle_coeff(u**a*v**b,u,v,2)
   rebuilt=sum(c*S.factorial(2)/(S.factorial(k)*S.factorial(j)*S.factorial(2-k-j))*u**k*v**j*(1-u-v)**(2-k-j) for c,(k,j) in zip(co,inds))
   assert zero(rebuilt-u**a*v**b)
 # Positive three-arrow control on an actual physical local triangle.
 # It is a stress control, not a full-tree/all-root certificate.
 chosen=((7,0),(8,2),(9,4))
 H=sum((Gs[a] for a in chosen),S.zeros(3)).subs({x:Q(1,2),r:Q(1,3),l:Q(1,2)})
 anchor={p:Q(3,8),q:Q(1,4)}
 central=H.subs(anchor);assert all(t>0 for t in minors(central))
 tested=[];control=None
 for n in range(2,21):
  delta=Q(1,2**n)
  h=expanded(H.subs({p:anchor[p]+delta*u,q:anchor[q]+delta*v}))
  h3=hom3(h,u,v);assert zero(h3-h3[0,0]*ff)
  c=S.Poly(h3[0,0],u,v)
  c30=c.coeff_monomial(u**3);c03=c.coeff_monomial(v**3)
  c21=c.coeff_monomial(u*u*v);c12=c.coeff_monomial(u*v*v)
  ac=max(0,-c30);dc=max(0,-c03);lc=max(0,-c21,-c12)
  rr=expanded(h-h3+(-ac*u*u-dc*v*v-lc*u*v)*ff)
  cs=[triangle_coeff(rr[a,b],u,v,2) for a,b in ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))]
  matrices=[];mm=[]
  for k in range(6):
   a,b,c0,d,e,f0=[z[k] for z in cs];mat=S.Matrix([[a,b,c0],[b,d,e],[c0,e,f0]])
   matrices.append(mat);mm.append(minors(mat))
  passed=all(t>0 for row in mm for t in row);tested.append([n,passed])
  if passed:
   control={'delta':str(delta),'p0':str(anchor[p]),'q0':str(anchor[q]),'triangle_coefficients':[matrix_strings(m) for m in matrices], 'leading_minors':[[str(t) for t in row] for row in mm], 'A_D_L':[str(t) for t in (ac,dc,lc)],'central_G':matrix_strings(central)}
   break
 assert control is not None
 report={'claim':'H5_RANKONE_TRIANGLE_QUADRATIC_90_270_REDUCTION_V1','scope':'exact reduction, not all-root free-d exclusion','arrows':34,'fixed_d_blocks':90,'free_d_blocks':270,'triangle_monomial_identities':6,'fan_volumes':fan,'arrow_fold_envelopes':bounds,'cubic_table':cubic_table,'local_stress_arrows':[list(t) for t in chosen], 'local_attempts':tested,'local_control':control}
 blob=(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode()
 Path(dest).write_bytes(blob)
 print('H5_RANKONE_TRIANGLE_QUADRATIC_90_270_REDUCTION_PASS',len(ARROWS),90,270)
 print('LOCAL_THREE_ARROW_SIX_BERNSTEIN_PD_PASS',control['delta'],18)
 print('REPORT_BYTES_SHA256',len(blob),hashlib.sha256(blob).hexdigest())
 print('PYTHON_SYMPY',sys.version.split()[0],S.__version__)
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'h5_rankone_triangle_fold.json')
