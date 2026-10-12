# material-11fdb454563c

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact physical two-amplitude metric atlas on a rational own-centred body.
Python >=3.9, standard library only. Run python -B -S atlas.py.
No floating point, optimizer, random choice or external input is used.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd, lcm, isqrt
import json, hashlib, sys

PARENT='minimum-0279'
PARENT_SHA='d29ef38046c1ca99c02309710e454af21163746b81c7c780054e30b1f102b55a'
Y=tuple(tuple(map(F,r)) for r in (
 ('0','-1/15','0'),('0','1','0'),('0','0','1'),
 ('-6/25','-19/375','0'),('-63/100','37/100','0'),('-33/100','0','67/100'),
 ('39/50','-11/750','0'),('27/50','23/50','0'),('14/25','0','11/25'),
 ('-407/500','14849/450000','2077/30000')))
FACES=((0,3,4,1,7,6),(0,2,5,3),(0,6,8,2),(1,4,5,2),(1,2,8,7),(3,9,4),(3,5,9),(4,9,5),(6,7,8))
ZERO=((F(0),)*3,)*3

def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def scale(c,x): return tuple(c*a for a in x)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(A): return dot(A[0],cross(A[1],A[2]))
def mv(A,x): return tuple(dot(a,x) for a in A)
def outer(x,y): return tuple(tuple(a*b for b in y) for a in x)
def madd(A,B): return tuple(add(a,b) for a,b in zip(A,B))
def mscale(c,A): return tuple(scale(c,a) for a in A)
def inv(A):
 d=det(A); assert d>0
 return mscale(1/d,tuple(zip(cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))))
def quad(x,A,y): return dot(x,mv(A,y))
def primitive(v,canon=False):
 d=1
 for x in v:d=lcm(d,F(x).denominator)
 w=[int(F(x)*d) for x in v]; g=0
 for x in w:g=gcd(g,abs(x))
 if not g:return tuple(w)
 w=[x//g for x in w]
 if canon and next(x for x in reversed(w) if x)<0:w=[-x for x in w]
 return tuple(w)
def geometry():
 g=(F(305383217,94853338000),F(6871784228327,28456001400000),F(487569104171,1897066760000))
 X=tuple(sub(y,g) for y in Y); poles=[]; expected=set(map(frozenset,FACES)); found=set()
 for tri in combinations(range(10),3):
  a,b,c=(Y[i] for i in tri); n=cross(sub(b,a),sub(c,a))
  if not any(n):continue
  h=dot(n,a); vals=[h-dot(n,y) for y in Y]
  if max(vals)<=0:vals=[-v for v in vals]
  if min(vals)>=0: found.add(frozenset(i for i,v in enumerate(vals) if not v))
 assert found==expected
 edges=tuple(sorted({tuple(sorted((cy[j],cy[(j+1)%len(cy)]))) for cy in FACES for j in range(len(cy))}))
 assert len(edges)==17
 ef=tuple(tuple(f for f,cy in enumerate(FACES) if i in cy and j in cy) for i,j in edges)
 assert all(len(x)==2 for x in ef)
 V=F(0);J=(F(0),)*3;K=ZERO
 for cy in FACES:
  a,b,c=(X[i] for i in cy[:3]);n=cross(sub(b,a),sub(c,a));h=dot(n,a)
  assert h>0
  assert all((h-dot(n,x)==0) if i in cy else (h-dot(n,x)>0) for i,x in enumerate(X))
  poles.append(scale(1/h,n))
  for j in range(1,len(cy)-1):
   a,b,c=(X[i] for i in (cy[0],cy[j],cy[j+1])); d=det((a,b,c));assert d>0
   s=add(add(a,b),c);V+=d/6;J=add(J,scale(d/24,s))
   T=outer(s,s)
   for z in (a,b,c):T=madd(T,outer(z,z))
   K=madd(K,mscale(d/120,T))
 assert V==F(47426669,140625000) and J==(0,0,0)
 Sigma=mscale(1/V,K);assert det(Sigma)>0
 return X,tuple(poles),edges,ef,Sigma

def gram_frame(M,seeds):
 out=[]
 for w in seeds:
  w=tuple(map(F,w))
  for v in out:w=sub(w,scale(quad(v,M,w)/quad(v,M,v),v))
  assert any(w);out.append(w)
 assert all(quad(v,M,w)==0 for v,w in combinations(out,2))
 return tuple(out)

def rows(X,Q,edges,ef,N0,u,v):
 assert N0==tuple(zip(*N0)) and N0[0][0]>0 and N0[0][0]*N0[1][1]>N0[0][1]**2 and det(N0)>0
 M0=inv(N0); a=quad(u,M0,u);b=quad(v,M0,v);assert a>0 and b>0 and quad(u,M0,v)==0
 U=mscale(1/a,outer(mv(M0,u),mv(M0,u))); W=mscale(1/b,outer(mv(M0,v),mv(M0,v)))
 arr=[]
 # Numerators in order (1,p,q,pq). Denominators are positive.
 for (i,j),(f,h) in zip(edges,ef):
  for r,s in ((i,j),(j,i)):
   x,e=X[r],sub(X[s],X[r]);arr.append(primitive((quad(x,M0,e),-quad(x,U,e),-quad(x,W,e),0)))
  for r,s in ((f,h),(h,f)):
   x,e=Q[r],sub(Q[s],Q[r]); A=quad(x,N0,e);B=dot(x,u)*dot(e,u)/a;C=dot(x,v)*dot(e,v)/b
   arr.append(primitive((A,B-A,C-A,A-B-C)))
 return tuple(arr)

# Exact root catalog. Rational roots have key ('r',num,den); irreducible
# quadratic roots key ('q',a,b,c,sign), with a>0 and sqrt(b*b-4*a*c).
def roots(coeff):
 v=list(coeff)
 while v and not v[-1]:v.pop()
 if len(v)<2:return ()
 v=primitive(v,True)
 if len(v)==2:
  x=F(-v[0],v[1]);return (('r',x.numerator,x.denominator),)
 assert len(v)==3
 c,b,a=v;D=b*b-4*a*c
 if D<0:return ()
 s=isqrt(D)
 if s*s==D:
  rr={F(-b+s,2*a),F(-b-s,2*a)}
  return tuple(('r',x.numerator,x.denominator) for x in rr)
 return (('q',a,b,c,-1),('q',a,b,c,1))
def enclosure(key,bits):
 if key[0]=='r':
  x=F(key[1],key[2]);return x,x
 _,a,b,c,sg=key;D=b*b-4*a*c;den=1<<bits;k=isqrt(D*den*den)
 lo,hi=F(k,den),F(k+1,den)
 if sg<0:lo,hi=-hi,-lo
 return (F(-b)+lo)/(2*a),(F(-b)+hi)/(2*a)
def critical(arr):
 pol=set()
 def put(c):
  c=primitive(c,True)
  while c and not c[-1]:c=c[:-1]
  if len(c)>1:pol.add(c)
 for a,b,c,d in arr:
  put((a,b));put((c,d));put((a+c,b+d)) # q=0, poles, q=1
 for (a,b,c,d),(e,f,g,h) in combinations(arr,2):
  put((a*g-e*c,a*h+b*g-e*d-f*c,b*h-f*d))
 keys={('r',0,1),('r',1,1)}
 for c in pol:keys.update(roots(c))
 bits=16
 while True:
  keep=[];bad=False
  for k in keys:
   lo,hi=enclosure(k,bits)
   if hi<0 or lo>1:continue
   if (lo<0<hi) or (lo<1<hi):bad=True;break
   if lo>=0 and hi<=1:keep.append((lo,hi,k))
  if not bad:
   keep.sort(key=lambda x:(x[0],x[1]))
   if all(x[1]<y[0] for x,y in zip(keep,keep[1:])):return keep,bits,len(pol)
  bits*=2
  if bits>16384:raise RuntimeError('Root separation guard exceeded')

def census(signs,edges,ef):
 up=[True]*(1+max(max(e) for e in edges));st=[True]*(1+max(max(e) for e in ef));H=0;weak=[]
 for k,((i,j),(f,h)) in enumerate(zip(edges,ef)):
  a,b,c,d=signs[4*k:4*k+4]
  up[i]&=a<0;up[j]&=b<0;st[f]&=c<0;st[h]&=d<0
  if max(a,b,c,d)<0:H+=1
  elif max(a,b,c,d)<=0:weak.append(k)
 return (sum(st),sum(up),H,len(weak))

def atlas(arr,edges,ef):
 cuts,bits,npoly=critical(arr);signatures={};npoints=0
 for left,right in zip(cuts,cuts[1:]):
  p=(left[1]+right[0])/2;pn,pd=p.numerator,p.denominator
  ab=[(a*pd+b*pn,c*pd+d*pn) for a,b,c,d in arr]
  qs={F(0),F(1)}
  for A,B in ab:
   if B:
    q=F(-A,B)
    if 0<q<1:qs.add(q)
  qq=sorted(qs)
  for lo,hi in zip(qq,qq[1:]):
   q=(lo+hi)/2;qn,qd=q.numerator,q.denominator
   sig=tuple((z>0)-(z<0) for A,B in ab for z in (A*qd+B*qn,))
   if sig not in signatures:signatures[sig]=(p,q)
   npoints+=1
 counts={};witnesses={}
 for sig,(p,q) in signatures.items():
  c=census(sig,edges,ef);counts[c]=counts.get(c,0)+1
  if c not in witnesses:witnesses[c]=(p,q)
  if c[3]==0:assert c[0]+c[1]-c[2]==2
 digest=hashlib.sha256(('\n'.join(''.join('-0+'[x+1] for x in sig) for sig in sorted(signatures))+'\n').encode()).hexdigest()
 return {'critical_roots':len(cuts),'projection_polynomials':npoly,'root_isolation_bits':bits,'sample_points':npoints,
 'sign_vectors':len(signatures),'sign_sha256':digest,'census_sign_vector_counts':{str(k):v for k,v in sorted(counts.items())},
 'census_witnesses':{str(k):tuple(map(str,v)) for k,v in sorted(witnesses.items())},
 'has_proper110':(1,1,0,0) in counts,
 'min_strict_S_plus_U':min(c[0]+c[1] for c in counts if c[3]==0),
 'zero_rows':[k for k,r in enumerate(arr) if not any(r)]}


def clip(poly,row):
 a,b,c=row
 def val(x):return a+b*x[0]+c*x[1]
 out=[]
 for x,y in zip(poly,poly[1:]+poly[:1]):
  fx,fy=val(x),val(y)
  if fx<=0:out.append(x)
  if (fx<0<fy) or (fy<0<fx):
   t=fx/(fx-fy);out.append((x[0]+t*(y[0]-x[0]),x[1]+t*(y[1]-x[1])))
 clean=[]
 for x in out:
  if not clean or clean[-1]!=x:clean.append(x)
 if len(clean)>1 and clean[0]==clean[-1]:clean.pop()
 return clean

def feature_reduce(arr,edges,ef):
 up=[[] for _ in range(1+max(max(e) for e in edges))];st=[[] for _ in range(1+max(max(e) for e in ef))]
 for k,((i,j),(f,h)) in enumerate(zip(edges,ef)):
  up[i].append(4*k);up[j].append(4*k+1)
  st[f].append(4*k+2);st[h].append(4*k+3)
 records=[];active=set()
 for kind,features,domain in (
  ('U',up,[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]),
  ('S',st,[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))])):
  for label,ids in enumerate(features):
   poly=domain.copy()
   for ix in ids:
    a,b,c,d=arr[ix]
    assert (d==0) if kind=='U' else (a+b+c+d==0)
    if not any((a,b,c)):
     poly=[];break # this feature is NEVER a strict equilibrium
    poly=clip(poly,(a,b,c))
    if not poly:break
   area=sum((x[0]*y[1]-x[1]*y[0] for x,y in zip(poly,poly[1:]+poly[:1])),F(0))
   if area<=0:records.append((kind,label,None));continue
   selected=set()
   for x,y in zip(poly,poly[1:]+poly[:1]):
    if x==y:continue
    # Domain boundary supports are strictly inactive throughout the OPEN domain.
    if kind=='U':is_boundary=any(x[j]==y[j] and x[j] in (0,1) for j in (0,1))
    else:is_boundary=(x[0]==y[0]==0 or x[1]==y[1]==0 or sum(x)==sum(y)==1)
    if is_boundary:continue
    passing=[ix for ix in ids if all(arr[ix][0]+arr[ix][1]*z[0]+arr[ix][2]*z[1]==0 for z in (x,y))]
    assert passing;selected.add(min(passing))
   selected=tuple(sorted(selected));active.update(selected)
   records.append((kind,label,selected))
 return tuple(sorted(active)),tuple(records)

def reduced_atlas(arr,edges,ef):
 active,features=feature_reduce(arr,edges,ef)
 cuts,bits,npoly=critical(tuple(arr[i] for i in active));signatures={};counts=set();npoints=0
 assert all(any(row) for row in arr),'Generic-row reduced mode requires no identically zero primitive'
 for left,right in zip(cuts,cuts[1:]):
  # Avoid vertical zero components of OMITTED primitives without introducing
  # any additional projection cuts. There are only finitely many bad p values.
  k=1
  while True:
   p=(k*left[1]+right[0])/(k+1);pn,pd=p.numerator,p.denominator
   ab=[(a*pd+b*pn,c*pd+d*pn) for a,b,c,d in arr]
   if all(A or B for A,B in ab):break
   k+=1
  qs={F(0),F(1)}
  for ix in active:
   A,B=ab[ix]
   if B and 0<F(-A,B)<1:qs.add(F(-A,B))
  qq=sorted(qs)
  for lo,hi in zip(qq,qq[1:]):
   k=1
   while True:
    q=(k*lo+hi)/(k+1);qn,qd=q.numerator,q.denominator
    vals=[A*qd+B*qn for A,B in ab]
    if all(vals):break
    k+=1
   sig=tuple((z>0)-(z<0) for z in vals)
   reduced_sig=tuple(sig[ix] for ix in active)
   U=sum(kind=='U' and ids is not None and all(sig[ix]<0 for ix in ids) for kind,label,ids in features)
   S=sum(kind=='S' and ids is not None and all(sig[ix]<0 for ix in ids) for kind,label,ids in features)
   actual=census(sig,edges,ef)
   assert actual==(S,U,S+U-2,0)
   if reduced_sig not in signatures:signatures[reduced_sig]=(p,q,actual)
   counts.add(actual);npoints+=1
 return {'active_rows':active,'feature_active_rows':features,'projection_polynomials':npoly,
   'critical_roots':len(cuts),'root_isolation_bits':bits,'generic_samples':npoints,
   'reduced_sign_vectors':len(signatures),'censuses':sorted(counts),
   'census_witnesses':{str(c):tuple(map(str,next((p,q) for p,q,a in signatures.values() if a==c))) for c in sorted(counts)}}

def selftest():
 # Exact rational identity for the same inverse, including mixed amplitude.
 N0=((F(3),F(1),F(0)),(F(1),F(2),F(0)),(F(0),F(0),F(4)))
 M0=inv(N0);u,v,_=gram_frame(M0,((1,2,3),(2,-1,1),(0,0,1)));a=quad(u,M0,u);b=quad(v,M0,v)
 p,q=F(2,7),F(3,8)
 N=madd(madd(N0,mscale(p/((1-p)*a),outer(u,u))),mscale(q/((1-q)*b),outer(v,v)))
 M=madd(madd(M0,mscale(-p/a,outer(mv(M0,u),mv(M0,u)))),mscale(-q/b,outer(mv(M0,v),mv(M0,v))))
 assert inv(N)==M
 # Double rational root, irreducible quadratic, shared component, vertical line,
 # horizontal line, identically zero primitive, and out-of-square intersections.
 toy=((1,-2,0,0),(1,-1,-1,1),(1,0,-2,0),(0,0,0,0),(1,-3,2,4))
 cc,_,_=critical(toy); assert len(cc)>=4
 for l,r in zip(cc,cc[1:]):assert l[1]<r[0]
 assert roots((-1,0,1))==(('r',1,1),('r',-1,1)) or set(roots((-1,0,1)))=={('r',1,1),('r',-1,1)}
 assert len(roots((-2,0,1)))==2

def main():
 if not __debug__:raise RuntimeError('Assertions must be enabled')
 selftest();X,Q,edges,ef,Sigma=geometry();M0=inv(Sigma)
 frame=gram_frame(M0,((1,0,0),(0,1,0),(0,0,1)))
 reports=[]
 for i,j in ((0,1),(0,2),(1,2)):
  arr=rows(X,Q,edges,ef,Sigma,frame[i],frame[j]);r=atlas(arr,edges,ef)
  r['pair']=(i,j);r['rows']=arr;r['feature_reduced']=reduced_atlas(arr,edges,ef)
  assert set(r['census_sign_vector_counts'])==set(r['feature_reduced']['census_witnesses'])
  reports.append(r)
  print('completed frame pair',i,j,'sign vectors',r['sign_vectors'],'minimum S+U',r['min_strict_S_plus_U'],file=sys.stderr,flush=True)
 out={'marker':'EXACT_TWO_AMPLITUDE_PHYSICAL_FEATURE_ATLAS_V2 PASS','scope':'three entire fixed-frame two-amplitude squares; NOT all orientations or whole E17',
 'parent':PARENT,'parent_sha256':PARENT_SHA,'actual_covariance':[[str(v) for v in row] for row in Sigma],
 'rational_frame':[[str(v) for v in u] for u in frame],'reports':reports}
 print(json.dumps(out,sort_keys=True,indent=2))
if __name__=='__main__':main()
