"""Exact filled raw/central moments through order two, with two tetrahedralizations.
The monomial() function is also a finite exact recovery formula for any raw moment.
No surface masses or vertex-mass surrogate are used.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json,sys,hashlib
sys.set_int_max_str_digits(0)
def det(a,b,c):return a[0]*(b[1]*c[2]-b[2]*c[1])+a[1]*(b[2]*c[0]-b[0]*c[2])+a[2]*(b[0]*c[1]-b[1]*c[0])
def moments(P,faces,base,reverse_anchor=False):
 V=Q(0);M=[Q(0)]*3;T=[[Q(0)]*3 for _ in range(3)]
 for cy in faces:
  if reverse_anchor:cy=cy[-1:]+cy[:-1]
  for k in range(1,len(cy)-1):
   vv=[[P[v][j]-base[j] for j in range(3)] for v in [cy[0],cy[k],cy[k+1]]]
   d=det(*vv);assert d>0;s=[sum(p[j] for p in vv) for j in range(3)]
   V+=d/6
   for i in range(3):
    M[i]+=d*s[i]/24
    for j in range(3):T[i][j]+=d*(s[i]*s[j]+sum(p[i]*p[j] for p in vv))/120
 rawM=[M[j]+V*base[j] for j in range(3)]
 rawT=[[T[i][j]+base[i]*M[j]+M[i]*base[j]+V*base[i]*base[j] for j in range(3)] for i in range(3)]
 return V,rawM,rawT

def monomial(P,faces,powers):
 """Integral x^p y^q z^r over the filled polyhedron, origin interior.
 Complete expansion on each standard simplex; any nonnegative integer powers.
 This function is not a claim that infinitely many evaluations were executed.
 """
 assert len(powers)==3 and all(isinstance(v,int) and v>=0 for v in powers)
 ans=Q(0)
 for cy in faces:
  for j in range(1,len(cy)-1):
   a,b,c=[P[v] for v in [cy[0],cy[j],cy[j+1]]];terms={(0,0,0):Q(1)}
   for axis,n in enumerate(powers):
    for _ in range(n):
     nxt={}
     for e,w in terms.items():
      for k,pt in enumerate([a,b,c]):
       f=list(e);f[k]+=1;f=tuple(f);nxt[f]=nxt.get(f,Q(0))+w*pt[axis]
     terms=nxt
   z=sum(w*factorial(e[0])*factorial(e[1])*factorial(e[2]) for e,w in terms.items())/factorial(sum(powers)+3)
   ans+=det(a,b,c)*z
 return ans

def run(folder):
 R=Path(folder);a=json.loads((R/'A.json').read_text());P=[list(map(Q,p)) for p in a['raw_vertices']];faces=a['faces']
 rho=min(Q(h,100*(1+sum(abs(t) for t in n))) for n,h in zip(a['normals'],a['offsets']));base=[rho,2*rho,3*rho]
 V,M,T=moments(P,faces,[Q(0)]*3);W,N,U=moments(P,faces,base,True);assert (V,M,T)==(W,N,U)
 assert V==Q(a['ordinary_volume']) and M==list(map(Q,a['raw_first_moments']))
 c=[m/V for m in M];assert c==list(map(Q,a['raw_centroid']))
 C=[[T[i][j]-M[i]*M[j]/V for j in range(3)] for i in range(3)]
 assert C[0][0]>0 and C[0][0]*C[1][1]-C[0][1]**2>0 and det(*C)>0
 # Execute and cross-check the general circuit for every monomial of degree<=2.
 exponents=[(0,0,0)]+[tuple(int(j==i) for j in range(3)) for i in range(3)]
 exponents += [tuple(int(k==i)+int(k==j) for k in range(3)) for i in range(3) for j in range(i,3)]
 values=[]
 for e in exponents:
  val=monomial(P,faces,e);degree=sum(e)
  expected=V if degree==0 else M[e.index(1)] if degree==1 else T[[i for i in range(3) if e[i]][0]][[i for i in range(3) if e[i]][-1]]
  assert val==expected;values.append([list(e),str(val)])
 out=dict(volume=str(V),first_moments=list(map(str,M)),centroid=list(map(str,c)),raw_second_moments=[[str(x) for x in row] for row in T],centred_second_moments=[[str(x) for x in row] for row in C],centred_first_moments=['0','0','0'],general_circuit_checked_exponents=[list(e) for e in exponents],two_exact_tetrahedralizations_agree=True)
 blob=json.dumps(out,sort_keys=True,separators=(',',':')).encode();(R/'MASS_MOMENTS.json').write_bytes(blob)
 print(R.name,'EXACT_FILLED_MOMENTS_THROUGH_ORDER_TWO_TWO_TETRAHEDRALIZATIONS_PASS',len(blob),hashlib.sha256(blob).hexdigest(),flush=True)
 return out
if __name__=='__main__':
 for folder in sys.argv[1:]:run(folder)
