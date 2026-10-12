# material-d4c753c4f64d

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact fixed-tangential-metric shear-cell decision for strict-escape H5 U1.
Standard library; rational arithmetic, exact quadratic-real ordering.
No claim of all-G, all-shape or weak-only U1 coverage.
"""
from fractions import Fraction as F
from functools import cmp_to_key, reduce
from math import gcd, isqrt, lcm
from itertools import combinations
from pathlib import Path
import json, hashlib, sys, time
FACETS=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=tuple(sorted({tuple(sorted((f[k],f[(k+1)%len(f)]))) for f in FACETS for k in range(len(f))}))
ARROWS=tuple(sorted((i,j) for a,b in EDGES for i,j in ((a,b),(b,a))))
ADJ=tuple(tuple(k for k,(i,j) in enumerate(ARROWS) if i==u) for u in range(10))
def dot(a,b): return sum((x*y for x,y in zip(a,b)), F(0))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def bil(a,G,b): return sum((a[i]*G[i][j]*b[j] for i in range(2) for j in range(2)),F(0))
def enc(x):
 if isinstance(x,F): return str(x)
 if isinstance(x,dict): return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)): return [enc(v) for v in x]
 return x

def geometry(theta):
 x,r,p,q,la=map(F,theta)
 assert 0<x<1 and 0<r<1 and p>0 and q>0 and p+q<1 and 0<la<1
 s=1-la
 B=((F(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),(0,1-3*r/4),(0,F(1,4)),(F(1,16),F(1,16)))
 z=tuple((s*a,s*b,F(0)) for a,b in B)+((F(0),F(0),F(1)),(la,F(0),F(1)),(F(0),la,F(1)))
 D=F(0); K=[F(0)]*3
 for f in FACETS:
  n=cross(sub(z[f[1]],z[f[0]]),sub(z[f[2]],z[f[0]]));h=dot(n,z[f[0]])
  assert n!=(0,0,0)
  for j in range(10): assert dot(n,z[j])==h if j in f else dot(n,z[j])<h
  for k in range(1,len(f)-1):
   a,b,c=(z[j] for j in (f[0],f[k],f[k+1]));d=dot(a,cross(b,c));D+=d
   for i in range(3):K[i]+=d*(a[i]+b[i]+c[i])/4
 assert D>0
 g=tuple(a/D for a in K); assert F(1,4)<g[2]<F(3,4)
 return z,g,D/6

def enclosure(z,g,G):
 # If U1 occurs, a same-layer norm-maximal nonroot has a cross exit.
 # For that oriented spoke D_ij/c_i = rho^2 - ||v-m||_G^2 - eta.
 # Hence ||v||_G^2+eta <= ||r_i||_G^2+||d_ij||_G^2.
 H=F(0);eta_cap=F(0)
 for i,j in ARROWS:
  sig=z[j][2]-z[i][2]
  if not sig:continue
  h=z[i][2]-g[2];ai=sub(z[i][:2],g[:2]);delta=sub(z[j][:2],z[i][:2])
  ri=tuple(-a/h for a in ai);dij=tuple(-a/sig for a in delta)
  H=max(H,bil(ri,G,ri)+bil(dij,G,dij))
  rd=sub(ri,dij);eta_cap=max(eta_cap,bil(rd,G,rd)/4)
 return H,eta_cap

def primitive(coeff):
 den=lcm(*(x.denominator for x in coeff));a=tuple(int(x*den) for x in coeff)
 div=reduce(gcd,map(abs,a)); assert div
 return tuple(x//div for x in a)

class QR:
 """A rational or an irrational root of a primitive integer quadratic."""
 __slots__=('key','a','b','disc','sgn','r')
 def __init__(self,key,a=0,b=0,disc=0,sgn=0,r=None):
  self.key,self.a,self.b,self.disc,self.sgn,self.r=key,a,b,disc,sgn,r
 def bounds(self,bits):
  if self.r is not None:return self.r,self.r
  den=1<<bits;k=isqrt(self.disc*den*den)
  lo,hi=F(k,den),F(k+1,den)
  if self.sgn<0:lo,hi=-hi,-lo
  return (lo-self.b)/(2*self.a),(hi-self.b)/(2*self.a)
 def __hash__(self):return hash(self.key)
 def __eq__(self,o):return isinstance(o,QR) and self.key==o.key

def rat(r):
 r=F(r);return QR(('r',r.numerator,r.denominator),r=r)
def roots(a,b,c):
 a,b,c=map(F,(a,b,c))
 if not a:return [] if not b else [rat(-c/b)]
 aa,bb,cc=primitive((a,b,c))
 if aa<0:aa,bb,cc=-aa,-bb,-cc
 disc=bb*bb-4*aa*cc
 if disc<0:return []
 k=isqrt(disc)
 if k*k==disc:return list({rat(F(-bb-k,2*aa)),rat(F(-bb+k,2*aa))})
 return [QR(('q',aa,bb,cc,s),aa,bb,disc,s) for s in (-1,1)]
def compare(a,b):
 if a==b:return 0
 bits=8
 while True:
  al,ah=a.bounds(bits);bl,bh=b.bounds(bits)
  if ah<bl:return -1
  if bh<al:return 1
  bits*=2
  if bits>16384:raise ArithmeticError('quadratic-real ordering failed')
def sorted_roots(seq):return sorted(set(seq),key=cmp_to_key(compare))
def between(a,b):
 assert compare(a,b)<0
 bits=8
 while True:
  al,ah=a.bounds(bits);bl,bh=b.bounds(bits)
  if ah<bl:return (ah+bl)/2
  bits*=2

def polys(z,g,G):
 """Rows: a*x^2 + b*x*y + c*y^2 + d*x + e*y + f.
 Cross rows divided by positive c_i; all have common quadratic -G.
 """
 out=[]
 for i,j in ARROWS:
  ai=sub(z[i][:2],g[:2]);delta=sub(z[j][:2],z[i][:2]);h=z[i][2]-g[2];sig=z[j][2]-z[i][2]
  qa=h*sig*G[0][0];qb=2*h*sig*G[0][1];qc=h*sig*G[1][1]
  lin=tuple(sig*ai[k]+h*delta[k] for k in range(2))
  d=dot(lin,(G[0][0],G[1][0]));e=dot(lin,(G[0][1],G[1][1]));f=bil(ai,G,delta)
  row=(qa,qb,qc,d,e,f)
  if sig:
   ci=-h*sig;assert ci>0
   row=tuple(a/ci for a in row)
   # Exact diameter-ellipse factorization, including constants.
   ri=tuple(-a/h for a in ai);dij=tuple(-a/sig for a in delta)
   assert row[:3]==(-G[0][0],-2*G[0][1],-G[1][1])
   assert row[3]==dot(tuple(ri[k]+dij[k] for k in range(2)),(G[0][0],G[1][0]))
   assert row[4]==dot(tuple(ri[k]+dij[k] for k in range(2)),(G[0][1],G[1][1]))
   assert row[5]==-bil(ri,G,dij)
  out.append(row)
 assert sum(bool(r[0]) for r in out)==14
 return tuple(out)

def line_circle_abscissae(line,circ):
 A,B,C=line; a,b,c,d,e,f=circ
 if B:
  # Substitute y=-(A*x+C)/B; clear B^2, preserving every intersection.
  return roots(a*B*B-b*A*B+c*A*A,d*B*B-b*C*B+2*c*A*C-e*A*B,c*C*C-e*C*B+f*B*B)
 if A:return [rat(-C/A)] # harmless extra event when no actual intersection
 return []

def critical_x(rows,B):
 # Events: vertical lines, vertical tangencies, intersections, box crossings.
 lines=[r[3:] for r in rows if not r[0]]+[(F(0),F(1),-F(B)),(F(0),F(1),F(B))]
 circles=list({r for r in rows if r[0]})
 events=[rat(-B),rat(B)]
 for A,BB,C in lines:
  if not BB and A:events.append(rat(-C/A))
 for a,b,c,d,e,f in circles:
  events+=roots(b*b-4*c*a,2*b*e-4*c*d,e*e-4*c*f)
 for l1,l2 in combinations(lines,2):
  A,B1,C=l1;D,E,F1=l2;det=A*E-B1*D
  if det:events.append(rat((B1*F1-C*E)/det))
 for l in lines:
  for c in circles:events+=line_circle_abscissae(l,c)
 for c1,c2 in combinations(circles,2):
  assert c1[:3]==c2[:3]
  line=tuple(c1[i]-c2[i] for i in (3,4,5))
  if line[0] or line[1]:events+=line_circle_abscissae(line,c1)
 lo,hi=rat(-B),rat(B)
 return sorted_roots(t for t in events if compare(lo,t)<=0 and compare(t,hi)<=0)

def int_fiber(row,x):
 a,b,c,d,e,f=row
 return primitive((c,b*x+e,a*x*x+d*x+f))
def sign_at(row,y):
 a,b,c=row;n,d=y.numerator,y.denominator
 value=a*n*n+b*n*d+c*d*d
 return (value>0)-(value<0)

def decision(theta,G):
 start=time.monotonic();G=tuple(tuple(map(F,r)) for r in G)
 assert G[0][1]==G[1][0] and G[0][0]>0
 tr=G[0][0]+G[1][1];G=tuple(tuple(a/tr for a in r) for r in G)
 det=G[0][0]*G[1][1]-G[0][1]**2;assert det>0
 z,g,vol=geometry(theta);rows=polys(z,g,G)
 # Exact body-specific necessary M_zz <= H; lambda_min(G)>=det(G).
 H,eta_cap=enclosure(z,g,G)
 B=1
 while B*B*det<=H:B+=1
 xs=critical_x(rows,B);stats={'critical_abscissae':len(xs),'x_slabs':len(xs)-1,'sampled_open_fiber_intervals':0,'sink_histogram':{}}
 witness=None
 for xa,xb in zip(xs,xs[1:]):
  x=between(xa,xb);fib=[int_fiber(r,x) for r in rows]
  ys=[rat(-B),rat(B)]
  for rr in fib:ys+=roots(*rr)
  lo,hi=rat(-B),rat(B);ys=sorted_roots(y for y in ys if compare(lo,y)<=0 and compare(y,hi)<=0)
  for ya,yb in zip(ys,ys[1:]):
   y=between(ya,yb);sg=[sign_at(rr,y) for rr in fib];assert 0 not in sg
   sinks=[i for i in range(10) if all(sg[k]<0 for k in ADJ[i])]
   assert sinks
   stats['sampled_open_fiber_intervals']+=1;stats['sink_histogram'][len(sinks)]=stats['sink_histogram'].get(len(sinks),0)+1
   if len(sinks)==1:
    v=(x,y);tree=[];caps=[]
    for i in range(10):
     if i==sinks[0]:continue
     k=next(k for k in ADJ[i] if sg[k]>0);_,j=ARROWS[k];tree.append((i,j))
     if z[i][2]!=z[j][2]:
      a,b,c,d,e,f=rows[k];caps.append(a*x*x+b*x*y+c*y*y+d*x+e*y+f)
    assert caps and min(caps)>0
    eta=min(caps)/2
    # Direct true-centroid full SPD arrow check, independent of polynomial sign evaluation.
    Y=[tuple(z[i][k]-g[k]+(z[i][2]-g[2])*v[k] for k in range(2)) for i in range(10)]
    D={}
    for i,j in ARROWS:D[i,j]=bil(Y[i],G,sub(Y[j],Y[i]))+(z[i][2]-g[2])*(z[j][2]-z[i][2])*eta
    assert all(D[e]>0 for e in tree)
    assert [i for i in range(10) if all(D[ARROWS[k]]<0 for k in ADJ[i])]==sinks
    par=dict(tree)
    for i in range(10):
     cur=i;seen=set()
     while cur!=sinks[0]:assert cur not in seen;seen.add(cur);cur=par[cur]
    witness={'shear':v,'eta':eta,'root':sinks[0],'strict_tree':tree};break
  if witness:break
 stats['elapsed_seconds']=round(time.monotonic()-start,3)
 return {'identity':'H5_FIXED_G_COMPLETE_OPEN_SHEAR_CELLS_V1','theta':theta,'normalized_G':G,'volume':vol,'centroid':g,'rational_shear_box':B,'necessary_Mzz_upper':H,'necessary_eta_upper':eta_cap,'verdict':'STRICT_ESCAPE_U1_WITNESS' if witness else 'NO_STRICT_ESCAPE_U1_AT_ANY_SHEAR_OR_POSITIVE_ETA','scope':'Fixed exact shape and G only; every real shear and eta>0 for strict-escape U1. Weak-only U1 is not decided. Proper110 is a subset of strict-escape U1. No all-G or whole-H5 claim.','stats':stats,'witness':witness}

CONTROLS={
 'A':(('13/20','3/4','4/5','1/10','3/10'),(('1','0'),('0','1'))),
 'B':(('1/5','2/5','2/3','1/4','1/5'),(('1','1/2'),('1/2','2'))),
 'C':(('9/10','1/10','7/8','1/16','1/10'),(('2','-1'),('-1','1'))),
}
def main():
 key=sys.argv[1] if len(sys.argv)>1 else 'A';theta,G=CONTROLS[key];out=decision(theta,G)
 # Run time is not part of deterministic exact report bytes.
 elapsed=out['stats'].pop('elapsed_seconds');raw=(json.dumps(enc(out),sort_keys=True,indent=2)+'\n').encode()
 path=Path('h5_shear_'+key+'.json');path.write_bytes(raw)
 print(raw.decode());print('ELAPSED',elapsed);print('OUTPUT',path.name,len(raw),hashlib.sha256(raw).hexdigest());print('H5_FIXED_G_SHEAR_CELLS_EXACT_PASS')
if __name__=='__main__':main()
