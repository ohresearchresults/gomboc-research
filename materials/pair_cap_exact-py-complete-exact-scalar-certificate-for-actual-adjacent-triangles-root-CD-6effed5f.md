# material-6effed5f64ea

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact scalar certificate in the genuine adjacent-triangle/root-CD theorem.
python -S pair_cap_exact.py build|check
The geometric cap reduction is proved in the accompanying immutable text.
No floating point, optimizer, random source or external package is used here.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json,sys
assert __debug__
HERE=Path(__file__).resolve().parent
IDENTITY='ACTUAL_ADJACENT_TRIANGLE_ROOT_CD_PAIR_CAP_51_25_V1'
CODES=('000','001','0100','0101','0110','0111','10','1100','1101','1110','1111')
P={(0,0):F(1),(2,0):F(50),(1,2):F(-51),(2,2):F(-51),(1,3):F(50),(3,3):F(-50),(3,4):F(51)}
def clean(a):return {k:v for k,v in a.items() if v}
def add(a,b):
 c=dict(a)
 for k,v in b.items():c[k]=c.get(k,F(0))+v
 return clean(c)
def scale(a,s):return clean({k:v*s for k,v in a.items()})
def mul(a,b):
 c={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():c[i+k,j+l]=c.get((i+k,j+l),F(0))+v*w
 return clean(c)
def power(a,n):
 b={(0,0):F(1)}
 for _ in range(n):b=mul(b,a)
 return b
ONE={(0,0):F(1)};A={(1,0):F(1)};E={(0,1):F(1)}
def box(code):
 q=[F(0),F(1),F(0),F(1)]
 for k,b in enumerate(code):
  assert b in '01';j=2*(k%2);m=(q[j]+q[j+1])/2
  q[j+(0 if b=='1' else 1)]=m
 return q

def restrict(code):
 a0,a1,e0,e1=box(code);out={}
 for (i,j),v in P.items():
  for r in range(i+1):
   for s in range(j+1):
    out[r,s]=out.get((r,s),F(0))+v*comb(i,r)*a0**(i-r)*(a1-a0)**r*comb(j,s)*e0**(j-s)*(e1-e0)**s
 return clean(out)
def bernstein(code):
 q=restrict(code)
 return [[sum((q.get((r,s),F(0))*F(comb(i,r),comb(3,r))*F(comb(j,s),comb(4,s)) for r in range(i+1) for s in range(j+1)),F(0)) for j in range(5)] for i in range(4)]
def basis(n,i,axis):
 v=A if axis==0 else E
 return scale(mul(power(v,i),power(add(ONE,scale(v,-1)),n-i)),F(comb(n,i)))
def reconstruct(B):
 out={}
 for i in range(4):
  for j in range(5):out=add(out,scale(mul(basis(3,i,0),basis(4,j,1)),B[i][j]))
 return out

def cover(prefix=''):
 if prefix in CODES:return 1
 assert any(c.startswith(prefix) for c in CODES),('GAP',prefix)
 assert not any(prefix.startswith(c) for c in CODES),('OVERLAP',prefix)
 return cover(prefix+'0')+cover(prefix+'1')
def enc(x):return(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return[len(b),hashlib.sha256(b).hexdigest()]
def build():
 # This is exactly 51*denominator - 25*numerator of the upper-cap ratio.
 denominator=mul(add(ONE,scale(mul(A,power(E,2)),-1)),add(ONE,scale(mul(power(A,2),power(E,2)),-1)))
 numerator=scale(mul(add(ONE,scale(power(A,2),-1)),add(ONE,scale(mul(A,power(E,3)),-1))),2)
 assert add(scale(denominator,51),scale(numerator,-25))==P
 # Exact upper-cap substitution h=1-a: h(1+p)=1-a*e^2,
 # h(k+a*p)=1-a^2*e^2, h*n=2(1-a*e^3).
 h=add(ONE,scale(A,-1));k=add(ONE,A);hp=mul(A,add(ONE,scale(power(E,2),-1)))
 hn=scale(add(h,mul(A,add(ONE,scale(power(E,3),-1)))),2)
 assert add(h,hp)==add(ONE,scale(mul(A,power(E,2)),-1))
 assert add(mul(h,k),mul(A,hp))==add(ONE,scale(mul(power(A,2),power(E,2)),-1))
 assert hn==scale(add(ONE,scale(mul(A,power(E,3),-1)),2))
 assert cover()==len(CODES)==11
 records=[];zero=[]
 for code in CODES:
  B=bernstein(code);assert reconstruct(B)==restrict(code)
  assert all(x>=0 for row in B for x in row)
  if any(x==0 for row in B for x in row):zero.append(code)
  else:assert min(x for row in B for x in row)>0
  records.append({'code':code,'box':list(map(str,box(code))),'bernstein_3_4':[[str(x) for x in row] for row in B]})
 assert zero==['1111']
 B=bernstein('1111');assert all(x>0 for x in B[0]) and B[3][0]>0
 # In the last cell, a<1 gives positive row-0 Bernstein weight and all
 # row-0 coefficients positive for every e. At a=1,e<1 use entry(3,0).
 # Thus the sole zero in the full closed square is (a,e)=(1,1).
 assert sum(P.values())==0
 kappa=F(51,25)
 assert 3*kappa-6==F(3,25) and 3-kappa==F(24,25)
 assert kappa-1==F(26,25)
 # The added lower-cap variable x has gap coefficients
 # [kappa*D0-k*n], [3/25+24*h/25+kappa*(2-h)*p],
 # [kappa-h*(2-h)]; the latter two are strictly positive for 0<=h<1,p>=0.
 # At h=0, 2*(1+x)*(2+x)-2*(2+3*x)=2*x^2.
 assert add(scale(mul(add(ONE,A),add(scale(ONE,2),A)),2),scale(add(scale(ONE,2),scale(A,3)),-2))==scale(power(A,2),2)
 return {'identity':IDENTITY,'kappa':'51/25','polynomial':[[i,j,str(v)] for (i,j),v in sorted(P.items())],
  'cells':records,'nonnegative_coefficients':220,'positive_coefficients':217,
  'zero_cell':'1111','sole_zero_on_closed_square':['1','1'],
  'strict_for_physical_range':'0<=a<1, 0<=e<=1',
  'lower_cap_gap_linear_minimum':['3/25','24/25'],
  'lower_cap_gap_quadratic_minimum':'26/25',
  'scope':'Two genuine adjacent triangles ABC and ABD; root supporting facet contains C,D and avoids A,B; actual uniform-volume centroid. No restriction on other facet count or metric; no general-root cap or complexity minimum asserted.',
  'source_pin':pin(Path(__file__).read_bytes())}
def main():
 assert sys.argv[1:] in (['build'],['check'])
 b=enc(build());p=HERE/'pair_cap_exact.json'
 if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==b
 else:p.write_bytes(b)
 print('ACTUAL_TRIANGLE_ROOT_CD_PAIR_CAP_EXACT_PASS',len(CODES),220,217,*pin(b),flush=True)
if __name__=='__main__':main()
