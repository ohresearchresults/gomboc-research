# material-a008566eabc4

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact degree-seven two-cap seam localization controls and certificates.
Python >=3.10, standard library. `python -S twocap_seam.py` recomputes all
actual moments, facets, reciprocal equilibria and rational stress certificates.
Discovery is not used by verification. All literal inputs appear below.
"""
from fractions import Fraction as F
from itertools import combinations
from functools import cmp_to_key
from pathlib import Path
import json,hashlib,sys
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(t,a):return tuple(t*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def tr(A):return sum(A[i][i] for i in range(3))
def mt(A):return tuple(zip(*A))
def ms(t,A):return tuple(scale(t,r) for r in A)
def ma(A,B):return tuple(add(a,b) for a,b in zip(A,B))
def outer(a,b):return tuple(tuple(x*y for y in b) for x in a)
def sym(a,b):return ms(F(1,2),ma(outer(a,b),outer(b,a)))
def mv(A,v):return tuple(dot(r,v) for r in A)
def contract(A,B):return sum(dot(a,b) for a,b in zip(A,B))
def inv(A):
 d=det(*A);assert d
 return tuple(scale(1/d,r) for r in mt((cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))))
def minors(A):return (A[0][0],A[0][0]*A[1][1]-A[0][1]**2,det(*A))
def pd(A):assert A==mt(A) and min(minors(A))>0
def cycle(ids,Y,n):
 drop=next(i for i in range(3) if n[i]);axes=[i for i in range(3) if i!=drop]
 c=tuple(sum(Y[i][a] for i in ids)/len(ids) for a in axes)
 p={i:tuple(Y[i][a]-c[k] for k,a in enumerate(axes)) for i in ids}
 def half(v):return 0 if v[1]>0 or v[1]==0 and v[0]>=0 else 1
 def cmp(i,j):
  a,b=p[i],p[j]
  if half(a)!=half(b):return -1 if half(a)<half(b) else 1
  q=a[0]*b[1]-a[1]*b[0];assert q
  return -1 if q>0 else 1
 out=sorted(ids,key=cmp_to_key(cmp))
 if dot(cross(sub(Y[out[1]],Y[out[0]]),sub(Y[out[2]],Y[out[1]])),n)<0:out.reverse()
 for i in range(len(out)):
  assert dot(cross(sub(Y[out[(i+1)%len(out)]],Y[out[i]]),sub(Y[out[(i+2)%len(out)]],Y[out[(i+1)%len(out)]])),n)>0
 k=out.index(min(out));return tuple(out[k:]+out[:k])
def hull(Y):
 found={}
 for a,b,c in combinations(range(len(Y)),3):
  n=cross(sub(Y[b],Y[a]),sub(Y[c],Y[a]))
  if not any(n):continue
  h=dot(n,Y[a]);v=[dot(n,y)-h for y in Y]
  if all(x<=0 for x in v):pass
  elif all(x>=0 for x in v):n=scale(-1,n);h=-h;v=[-x for x in v]
  else:continue
  ids=tuple(i for i,x in enumerate(v) if x==0)
  assert any(x<0 for x in v)
  if ids not in found:found[ids]=(cycle(ids,Y,n),n,h)
 return [found[k] for k in sorted(found)]
def moments(Y,faces,o):
 D=F(0);L=(F(0),)*3
 for cyc,n,h in faces:
  for k in range(1,len(cyc)-1):
   a,b,c=[Y[j] for j in (cyc[0],cyc[k],cyc[k+1])]
   d=det(sub(a,o),sub(b,o),sub(c,o));assert d>=0
   D+=d;L=add(L,scale(d,add(add(o,a),add(b,c))))
 assert D>0
 return D,scale(1/(4*D),L)
def facecenter(Y,face):
 cyc,n,h=face;S=(F(0),)*3;area=F(0);triangles=[]
 for k in range(1,len(cyc)-1):
  ids=(cyc[0],cyc[k],cyc[k+1]);a,b,c=[Y[j] for j in ids]
  q=dot(n,cross(sub(b,a),sub(c,a)));assert q>0
  area+=q;S=add(S,scale(q,add(add(a,b),c)));triangles.append((ids,q))
 return scale(1/(3*area),S)
def geometry(cut,theta=F(1,2)):
 B=[(F(j)-cut,F(j*j),F(1)) for j in range(-3,4)]
 W=[];crossed=[]
 for i,a in enumerate(B):
  j=(i+1)%7;b=B[j]
  if a[0]*b[0]<0:
   W.append(add(a,scale(-a[0]/(b[0]-a[0]),sub(b,a))))
   crossed.append({a[0]>0:i+1,b[0]>0:j+1})
 assert len(W)==2
 Y=[(F(0),)*3]+[scale(1/(1+(1-theta)*b[0] if b[0]>0 else 1-theta*b[0]),b) for b in B]+W
 faces=hull(Y);edges={}
 for f,(cyc,n,h) in enumerate(faces):
  for a,b in zip(cyc,cyc[1:]+cyc[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(f)
 assert len(faces)==9 and len(edges)==17 and all(len(fs)==2 for fs in edges.values())
 assert [sum(i in e for e in edges) for i in range(10)]==[7]+[3]*9
 D,g=moments(Y,faces,Y[0]);o=scale(F(1,10),tuple(sum(y[j] for y in Y) for j in range(3)))
 assert moments(Y,faces,o)==(D,g)
 X=[sub(y,g) for y in Y];caps={}
 for f,face in enumerate(faces):
  if 0 not in face[0]:
   s=next(B[i-1][0]>0 for i in face[0] if 1<=i<=7);caps[s]=f
 assert len(caps)==2
 lam={};cent={}
 for s,f in caps.items():
  cf=facecenter(Y,faces[f]);cent[s]=sub(cf,g)
  dc,_=moments(Y,[faces[f]],Y[0]);lam[s]=dc/D
 assert sum(lam.values())==1
 assert add(X[0],scale(3,add(scale(lam[False],cent[False]),scale(lam[True],cent[True]))))==(0,0,0)
 return dict(cut=cut,theta=theta,Y=Y,X=X,faces=faces,edges=edges,D=D,g=g,caps=caps,crossed=crossed,lam=lam,cent=cent)
def constraints(G,neg,w,v):
 X=G['X'];fp=G['faces'][G['caps'][not neg]][0];fn=G['faces'][G['caps'][neg]][0]
 out=G['crossed'][w-8][not neg];A=[];names=[]
 for j in fn:
  if j!=w:A.append(ma(outer(X[w],X[w]),ms(-1,outer(X[j],X[j]))));names.append(('negmax',w,j))
 for j in fp:
  if j!=v:A.append(ma(outer(X[v],X[v]),ms(-1,outer(X[j],X[j]))));names.append(('posmax',v,j))
 A +=[sym(X[v],sub(X[0],X[v])),sym(X[w],sub(X[out],X[w])),
      ms(-1,ma(outer(X[0],X[0]),ms(3,sym(X[0],G['cent'][neg]))))]
 names += [('escape',v,0),('escape',w,out),('negative_balance',neg)]
 return A,names
def census(G,M):
 pd(M);N=inv(M);pd(N);X=G['X'];g=G['g']
 poles=[scale(1/(h-dot(n,g)),n) for cyc,n,h in G['faces']]
 primal={};dual={};pack=[]
 for (a,b),(f,k) in sorted(G['edges'].items()):
  ab=dot(X[a],mv(M,sub(X[b],X[a])));ba=dot(X[b],mv(M,sub(X[a],X[b])))
  fk=dot(poles[f],mv(N,sub(poles[k],poles[f])));kf=dot(poles[k],mv(N,sub(poles[f],poles[k])))
  primal[a,b]=ab;primal[b,a]=ba;dual[f,k]=fk;dual[k,f]=kf
  assert all(q!=0 for q in (ab,ba,fk,kf))
  pack.append((a,b,f,k,ab,ba,fk,kf))
 U=[i for i in range(10) if all(q<0 for (a,b),q in primal.items() if a==i)]
 S=[i for i in range(9) if all(q<0 for (a,b),q in dual.items() if a==i)]
 H=[(a,b) for a,b,f,k,*q in pack if all(x<0 for x in q)]
 assert len(S)+len(U)-len(H)==2
 return dict(M=M,N=N,S=S,U=U,H=H,weak=(0,0,0),packets=pack)
def encode(x):
 if isinstance(x,F):return str(x.numerator)+'/'+str(x.denominator)
 if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [encode(v) for v in x]
 return x

class IV:
 """Closed rational intervals, rounded OUTWARD to the fixed grid 10^-30."""
 GRID=10**30
 __slots__=('lo','hi')
 def __init__(self,a,b=None):
  if isinstance(a,IV):self.lo,self.hi=a.lo,a.hi
  else:self.lo,self.hi=F(a),F(a if b is None else b)
  assert self.lo<=self.hi
  lo=self.lo*self.GRID;hi=self.hi*self.GRID
  self.lo=F(lo.numerator//lo.denominator,self.GRID)
  self.hi=F(-((-hi.numerator)//hi.denominator),self.GRID)
 def __add__(a,b):
  b=IV(b);return IV(a.lo+b.lo,a.hi+b.hi)
 __radd__=__add__
 def __neg__(a):return IV(-a.hi,-a.lo)
 def __sub__(a,b):return a+-IV(b)
 def __rsub__(a,b):return IV(b)+-a
 def __mul__(a,b):
  b=IV(b);v=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi)
  return IV(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(a,b):
  b=IV(b);assert b.lo>0 or b.hi<0
  return a*IV(1/b.hi,1/b.lo)
 def __rtruediv__(a,b):return IV(b)/a
 def __pow__(a,n):
  assert n==2
  lo=0 if a.lo<=0<=a.hi else min(a.lo*a.lo,a.hi*a.hi)
  return IV(lo,max(a.lo*a.lo,a.hi*a.hi))
 def __repr__(a):return 'IV('+str(a.lo)+','+str(a.hi)+')'
def interval_family(G,gi,eps):
 cut=G['cut'];th=IV(F(1,2)-eps,F(1,2)+eps)
 B=[(IV(F(j)-cut-eps,F(j)-cut+eps),IV(F(j*j)-eps,F(j*j)+eps),IV(1))
    for j in range(-3,4)]
 guards=[]
 assert th.lo>0 and th.hi<1
 signs=[b[0].lo>0 for b in B]
 for b,s in zip(B,signs):assert b[0].lo>0 if s else b[0].hi<0
 # Every nonincident vertex lies strictly to the left of each polygon edge.
 for i in range(7):
  j=(i+1)%7
  for k in range(7):
   if k not in (i,j):
    q=cross(sub(B[j],B[i]),sub(B[k],B[i]))[2]
    assert q.lo>0;guards.append(q.lo)
 W=[]
 for i,a in enumerate(B):
  j=(i+1)%7;b=B[j]
  if signs[i]!=signs[j]:W.append(add(a,scale(-a[0]/(b[0]-a[0]),sub(b,a))))
 assert len(W)==2
 Y=[(IV(0),)*3]+[scale(1/(1+(1-th)*b[0] if s else 1-th*b[0]),b) for b,s in zip(B,signs)]+W
 D=IV(0);L=(IV(0),)*3;rawcent={}
 for s,f in G['caps'].items():
  cyc=G['faces'][f][0];area=IV(0);areaL=(IV(0),)*3
  for k in range(1,len(cyc)-1):
   a,b,c=[Y[j] for j in (cyc[0],cyc[k],cyc[k+1])]
   d=det(a,b,c);assert d.lo>0
   D+=d;L=add(L,scale(d,add(add(a,b),c)))
   area2=cross(sub(b,a),sub(c,a))[2];assert area2.lo>0
   area+=area2;areaL=add(areaL,scale(area2,add(add(a,b),c)))
  rawcent[s]=scale(1/(3*area),areaL)
 assert D.lo>0
 g=scale(1/(4*D),L)
 H=dict(G);H['X']=[sub(y,g) for y in Y];H['cent']={s:sub(c,g) for s,c in rawcent.items()}
 checks=[]
 for j,neg,w,v,weights in STRESSES:
  if j!=gi:continue
  AA,names=constraints(H,bool(neg),w,v)
  Q=((IV(0),)*3,)*3
  for weight,a in zip(weights,AA):Q=ma(Q,ms(-weight,a))
  mm=minors(Q);assert all(t.lo>0 for t in mm)
  checks.append(dict(neg=neg,w=w,v=v,lower_minors=[t.lo for t in mm]))
 assert len(checks)==14
 return dict(geometry=gi,radius=eps,free_parameters=15,polygon_guards=guards,
             D=[D.lo,D.hi],centroid=[[t.lo,t.hi] for t in g],certificates=checks)

STRESSES = [(0, 0, 8, 2, [0, 47, 0, 0, 0, 0, 7, 0, 0, 100, 0, 33]), (0, 0, 8, 3, [0, 48, 100, 0, 0, 0, 4, 0, 0, 62, 0, 9]), (0, 0, 8, 4, [17, 0, 0, 100, 0, 0, 3, 0, 27, 30, 23, 0]), (0, 0, 8, 5, [97, 0, 90, 17, 2, 0, 0, 0, 100, 64, 0, 0]), (0, 0, 8, 6, [443, 0, 0, 0, 0, 0, 471, 0, 1000, 0, 136, 298]), (0, 0, 8, 7, [0, 0, 254, 0, 0, 0, 0, 0, 1000, 823, 0, 268]), (0, 0, 9, 2, [0, 0, 0, 0, 0, 0, 69, 10, 0, 100, 0, 0]), (0, 0, 9, 3, [0, 0, 0, 0, 0, 0, 13, 50, 0, 100, 0, 24]), (0, 0, 9, 4, [0, 0, 0, 1000, 0, 0, 81, 0, 142, 331, 105, 0]), (0, 0, 9, 5, [22, 0, 0, 100, 0, 0, 15, 0, 68, 62, 13, 0]), (0, 0, 9, 6, [473, 0, 0, 621, 0, 0, 519, 0, 1000, 601, 65, 0]), (0, 0, 9, 7, [0, 52, 100, 25, 0, 0, 0, 0, 0, 82, 33, 0]), (0, 1, 8, 1, [11, 0, 0, 15, 27, 0, 0, 0, 0, 21, 100, 0]), (0, 1, 9, 1, [0, 276, 381, 0, 0, 27, 308, 0, 0, 485, 1000, 0]), (1, 0, 8, 3, [0, 0, 0, 0, 0, 0, 10, 26, 66, 100, 0, 11]), (1, 0, 8, 4, [0, 0, 0, 17, 0, 0, 0, 20, 30, 71, 100, 0]), (1, 0, 8, 5, [27, 0, 0, 0, 64, 0, 0, 0, 20, 6, 100, 0]), (1, 0, 8, 6, [18, 0, 0, 32, 0, 0, 0, 0, 4, 11, 100, 0]), (1, 0, 8, 7, [27, 0, 0, 8, 0, 0, 0, 0, 50, 32, 100, 0]), (1, 0, 9, 3, [0, 0, 0, 0, 0, 0, 10, 26, 66, 100, 0, 11]), (1, 0, 9, 4, [0, 0, 51, 49, 0, 0, 0, 0, 83, 33, 100, 79]), (1, 0, 9, 5, [42, 0, 0, 0, 0, 13, 0, 0, 100, 4, 71, 47]), (1, 0, 9, 6, [0, 100, 0, 0, 0, 0, 19, 46, 25, 0, 75, 55]), (1, 0, 9, 7, [0, 0, 49, 0, 0, 0, 0, 0, 100, 85, 50, 0]), (1, 1, 8, 1, [0, 0, 0, 259, 115, 3, 278, 0, 0, 0, 1000, 0]), (1, 1, 8, 2, [0, 0, 0, 0, 38, 0, 0, 100, 1, 0, 0, 0]), (1, 1, 9, 1, [0, 831, 177, 0, 0, 0, 0, 0, 0, 4, 885, 1000]), (1, 1, 9, 2, [0, 0, 60, 0, 0, 0, 18, 100, 0, 53, 67, 0]), (2, 0, 8, 4, [0, 0, 0, 0, 86, 0, 0, 19, 100, 68, 0, 0]), (2, 0, 8, 5, [85, 0, 0, 62, 0, 0, 0, 0, 0, 236, 1000, 0]), (2, 0, 8, 6, [13, 5, 0, 1, 0, 45, 0, 0, 0, 0, 100, 1]), (2, 0, 8, 7, [16, 0, 0, 0, 0, 0, 19, 3, 11, 6, 100, 0]), (2, 0, 9, 4, [0, 0, 0, 41, 53, 0, 0, 0, 100, 0, 54, 64]), (2, 0, 9, 5, [0, 100, 0, 0, 0, 0, 0, 34, 61, 0, 76, 26]), (2, 0, 9, 6, [0, 1000, 53, 0, 0, 0, 23, 634, 153, 0, 434, 0]), (2, 0, 9, 7, [0, 8, 76, 0, 0, 0, 0, 3, 0, 0, 85, 100]), (2, 1, 8, 1, [11, 0, 6, 12, 1, 34, 0, 0, 0, 0, 100, 0]), (2, 1, 8, 2, [0, 0, 0, 39, 3, 0, 22, 0, 0, 0, 100, 0]), (2, 1, 8, 3, [0, 0, 0, 0, 13, 0, 60, 0, 0, 100, 0, 7]), (2, 1, 9, 1, [455, 522, 0, 0, 0, 0, 0, 0, 0, 53, 904, 1000]), (2, 1, 9, 2, [0, 100, 0, 0, 0, 0, 0, 26, 5, 0, 89, 75]), (2, 1, 9, 3, [0, 0, 0, 0, 64, 0, 91, 62, 0, 0, 69, 100])]
METRICS = [(1, 1, [[430, 31, 490], [31, 5, 35], [490, 35, 565]], 1000), (2, 1, [[68, -6, 246], [-6, 3, -21], [246, -21, 930]], 1000)]
def main():
 assert __debug__ and sys.version_info>=(3,10)
 gs=[geometry(F(k,2)) for k in (-5,-3,-1)]
 proofs=[]
 for gi,neg,w,v,weights in STRESSES:
  A,names=constraints(gs[gi],bool(neg),w,v);assert len(weights)==len(A)
  assert min(weights)>=0 and max(weights)>0
  Q=((F(0),)*3,)*3
  for weight,a in zip(weights,A):Q=ma(Q,ms(-weight,a))
  pd(Q);proofs.append(dict(geometry=gi,neg=neg,w=w,v=v,weights=weights,names=names,Q=Q,minors=minors(Q)))
 assert len(proofs)==42
 for gi,g in enumerate(gs):
  wanted={(neg,w,v) for neg in (False,True) for w in (8,9)
    for v in g['faces'][g['caps'][not neg]][0] if v not in (8,9)}
  got={(bool(z['neg']),z['w'],z['v']) for z in proofs if z['geometry']==gi}
  assert len(wanted)==14 and wanted==got
 controls=[]
 for gi,i,ints,den in METRICS:
  M=tuple(tuple(F(q,den) for q in row) for row in ints);G=gs[gi]
  rec=census(G,M);X=G['X'];norm=[dot(x,mv(M,x)) for x in X]
  assert norm[0]>norm[i]>max(norm[j] for j in range(1,10) if j!=i)
  assert dot(X[i],mv(M,sub(X[0],X[i])))>0
  rec.update(geometry=gi,highest_nonroot=i,norms=norm)
  controls.append(rec)
 assert len(controls)==2
 neighborhoods=[interval_family(g,gi,F(1,100000000)) for gi,g in enumerate(gs)]
 record=dict(version=1,geometries=gs,certificates=proofs,highest_nonroot_countercontrols=controls,
             actual_shape_neighborhoods=neighborhoods)
 raw=(json.dumps(encode(record),sort_keys=True,indent=2)+'\n').encode()
 Path('twocap_seam.json').write_bytes(raw)
 print('TWO_CAP_ALL_THREE_CONTROLS_ROOT0_U1_EMPTY_42_EXACT_SEAM_CERTIFICATES_PASS')
 print('THREE_FULL_15_PARAMETER_ACTUAL_SHAPE_BOXES_RADIUS_1E_MINUS8_126_INTERVAL_MINORS_PASS')
 for c in controls:print('COUNTERCONTROL',c['geometry'],c['highest_nonroot'],len(c['S']),len(c['U']),len(c['H']))
 print('TWOCAP_SEAM_EXACT_PASS',len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
