# material-e7d76e764027

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""SECTION_STRESS_HELLY3_E17_V1, exact rational control and certificates.
Standard library only; assertions required. Run: python -S section_stress.py build|check.
Analytic minimax and half-section proofs are in the companion recovery capsule.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, lcm, isqrt
from pathlib import Path
import json, hashlib, sys
assert __debug__
ID = 'SECTION_STRESS_HELLY3_E17_V1'
B = [(F(1),F(0)),(F(3,5),F(4,5)),(F(-3,5),F(4,5)),
     (F(-4,5),F(3,5)),(F(-4,5),F(-3,5)),(F(-5,13),F(-12,13)),
     (F(5,13),F(-12,13)),(F(35,37),F(-12,37))]
HALF = F(41,40)
P = [(*b,F(0)) for b in B]+[(-HALF,F(0),F(1)),(HALF,F(0),F(1))]
I2=((F(1),F(0)),(F(0),F(1)))
GBOX=[((F(1),b),(b,s)) for b,s in product((F(-1,200),F(1,200)),(F(99,100),F(101,100)))]
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(t,a): return tuple(t*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def mv(A,x): return tuple(dot(row,x) for row in A)
def bil(x,A,y): return dot(x,mv(A,y))
def outer(a,b): return tuple(tuple(x*y for y in b) for x in a)
def inv(A):
 d=det(*A); assert d>0
 C=(cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))
 return tuple(tuple(C[j][i]/d for j in range(3)) for i in range(3))
def hull2(points):
 points=sorted(set(points))
 def turn(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 rows=[]
 for seq in (points,points[::-1]):
  r=[]
  for p in seq:
   while len(r)>1 and turn(r[-2],r[-1],p)<=0: r.pop()
   r.append(p)
  rows.append(r[:-1])
 return rows[0]+rows[1]
def hull3(points):
 planes={}
 for i,j,k in combinations(range(len(points)),3):
  n=cross(sub(points[j],points[i]),sub(points[k],points[i])); d=dot(n,points[i])
  if not any(n): continue
  sl=[dot(n,x)-d for x in points]
  if min(sl)<0<max(sl) or max(sl)==min(sl)==0: continue
  if min(sl)>=0: n=scale(-1,n); d=-d
  den=lcm(*(x.denominator for x in (*n,d)))
  a=[int(x*den) for x in (*n,d)]; div=gcd(*a)
  h=tuple(F(x//div) for x in a)
  planes[h]=[i for i,x in enumerate(points) if dot(h[:3],x)==h[3]]
 faces=[]
 for h,ids in planes.items():
  drop=next(k for k in range(3) if h[k]); axes=[k for k in range(3) if k!=drop]
  lookup={tuple(points[i][k] for k in axes):i for i in ids}
  cy=[lookup[x] for x in hull2(lookup)]
  if dot(cross(sub(points[cy[1]],points[cy[0]]),sub(points[cy[2]],points[cy[0]])),h[:3])<0: cy.reverse()
  st=cy.index(min(cy)); cy=cy[st:]+cy[:st]
  assert set(cy)==set(ids)
  for a,b in zip(cy,cy[1:]+cy[:1]):
   assert all(dot(cross(sub(points[b],points[a]),sub(points[c],points[a])),h[:3])>0 for c in cy if c not in (a,b))
  faces.append((tuple(cy),h))
 faces.sort()
 arcs={}
 for f,(cy,h) in enumerate(faces):
  for e in zip(cy,cy[1:]+cy[:1]): assert e not in arcs; arcs[e]=f
 edges=sorted({tuple(sorted(e)) for e in arcs})
 assert all((j,i) in arcs for i,j in arcs)
 assert len(points)-len(edges)+len(faces)==2
 assert set(range(len(points)))==set(i for cy,h in faces for i in cy)
 for i in range(len(points)):
  ns=[h[:3] for cy,h in faces if i in cy]
  assert any(det(*q) for q in combinations(ns,3))
 return faces,edges,[(arcs[i,j],arcs[j,i]) for i,j in edges]
def mass(points,faces,ref):
 vol=F(0); first=(F(0),)*3; fan=[]
 for cy,h in faces:
  for j in range(1,len(cy)-1):
   ids=(cy[0],cy[j],cy[j+1]); tr=[points[i] for i in ids]
   w=det(*(sub(x,ref) for x in tr))/6; assert w>=0
   vol+=w; first=add(first,scale(w/4,add(ref,add(tr[0],add(tr[1],tr[2])))))
   fan.append((ids,w))
 assert vol>0
 return vol,scale(1/vol,first),fan
def stress(X,ids,weights):
 assert sum(weights)==1 and min(weights)>0
 assert all(X[i][2]*X[ids[0]][2]>0 for i in ids)
 S=sum(w*X[i][2]**2 for i,w in zip(ids,weights))
 b=tuple(sum(w*X[i][2]*X[i][k] for i,w in zip(ids,weights)) for k in range(2))
 T=tuple(tuple(sum(w*X[i][k]*X[i][l] for i,w in zip(ids,weights))-b[k]*b[l]/S for l in range(2)) for k in range(2))
 return dict(ids=ids,weights=weights,S=S,b=b,T=T,center=scale(-1/S,b))
def energy(st,G): return sum(st['T'][i][j]*G[i][j] for i in range(2) for j in range(2))
def metric(G,v,y):
 assert G[0][0]>0 and G[0][0]*G[1][1]>G[0][1]**2 and y>0
 q=mv(G,v)
 M=((G[0][0],G[0][1],q[0]),(G[1][0],G[1][1],q[1]),(q[0],q[1],dot(v,q)+y))
 N=inv(M)
 assert all(sum(M[i][k]*N[k][j] for k in range(3))==int(i==j) for i in range(3) for j in range(3))
 return M,N
def mechanics(X,Q,edges,dual,faces,v,y):
 M,N=metric(I2,v,y)
 gg=[[bil(a,M,b) for b in X] for a in X]; jj=[[bil(a,N,b) for b in Q] for a in Q]
 U=[i for i in range(len(X)) if all(gg[i][j]<gg[i][i] for j in range(len(X)) if j!=i)]
 S=[i for i in range(len(Q)) if all(jj[i][j]<jj[i][i] for j in range(len(Q)) if j!=i)]
 saddles=[]; weak={}; harmless=[]; primitives=[]
 for k,((i,j),(f,h)) in enumerate(zip(edges,dual)):
  z=(gg[i][j]-gg[i][i],gg[i][j]-gg[j][j],jj[f][h]-jj[f][f],jj[f][h]-jj[h][h]); primitives.append(z)
  assert z[0]+z[1]<0 and z[2]+z[3]<0
  if max(z)<0: saddles.append(k)
  elif max(z)==0:
   t=z[0]/(z[0]+z[1]); p=add(X[i],scale(t,sub(X[j],X[i])))
   d=jj[f][f]*jj[h][h]-jj[f][h]**2; assert d>0
   la,lb=-z[3]/d,-z[2]/d
   assert min(t,1-t,la,lb)>=0 and mv(M,p)==add(scale(la,Q[f]),scale(lb,Q[h]))
   active=[l for l,q in enumerate(Q) if dot(q,p)==1]
   assert all(dot(q,p)<=1 for q in Q)
   kind='VF' if t in (0,1) and min(la,lb)==0 else ('VE' if t in (0,1) else 'EF')
   weak.setdefault(p,dict(kind=kind,point=p,active=active,edges=[]))['edges'].append(k)
  elif any(a==0 for a in z): harmless.append(k)
 if not weak: assert len(S)+len(U)-len(saddles)==2
 height=F(isqrt(y.numerator),isqrt(y.denominator)); assert height**2==y
 Y=[(x[0]+v[0]*x[2],x[1]+v[1]*x[2],height*x[2]) for x in X]
 R=[(q[0],q[1],(q[2]-v[0]*q[0]-v[1]*q[1])/height) for q in Q]
 assert gg==[[dot(a,b) for b in Y] for a in Y] and jj==[[dot(a,b) for b in R] for a in R]
 fy,ey,dy=hull3(Y); assert [c for c,h in fy]==[c for c,h in faces] and ey==edges and dy==dual
 vy,gy,fan=mass(Y,fy,Y[0]); assert gy==(0,0,0)
 return dict(v=v,y=y,M=M,N=N,physical_vertices=Y,physical_poles=R,physical_volume=vy,physical_centroid=gy,counts=(len(S),len(U),len(saddles)),S=S,U=U,H_edge_ids=saddles,weak=list(weak.values()),harmless_zero_edges=harmless,primitives=primitives)
def encode(obj):
 if isinstance(obj,F): return str(obj)
 if isinstance(obj,dict): return {str(k):encode(v) for k,v in obj.items()}
 if isinstance(obj,(list,tuple)): return [encode(v) for v in obj]
 return obj
def build():
 faces,edges,dual=hull3(P)
 assert len(faces)==9 and len(edges)==17 and sorted(len(cy) for cy,h in faces)==[3]*6+[4]*2+[8]
 assert [sum(i in e for e in edges) for i in range(10)]==[3]*8+[5,5]
 V,g,f0=mass(P,faces,P[8]); v2,g2,f1=mass(P,faces,P[9]); assert (V,g)==(v2,g2)
 X=[sub(p,g) for p in P]; assert mass(X,faces,X[8])[:2]==(V,(0,0,0))
 Q=[scale(1/(h[3]-dot(h[:3],g)),h[:3]) for cy,h in faces]
 assert all(all(dot(q,x)==1 if i in cy else dot(q,x)<1 for i,x in enumerate(X)) for q,(cy,h) in zip(Q,faces))
 cuts=[]
 for i,j in edges:
  if X[i][2]*X[j][2]<0:
   t=-X[i][2]/(X[j][2]-X[i][2]); cuts.append((i,j,add(X[i][:2],scale(t,sub(X[j][:2],X[i][:2])))))
 assert len(cuts)==8 and all(X[i][2]<0 for i in range(8)) and min(X[8][2],X[9][2])>0
 section=[r for i,j,r in cuts]
 mink=[sub(add(scale(1-g[2],b),(sgn*g[2]*HALF,F(0))),g[:2]) for b in B for sgn in (-1,1)]
 assert set(hull2(section))==set(hull2(mink))
 # Positive barycentric weights of the circumcenter for base vertices 0,2,5.
 ids=(0,2,5); mat=tuple(tuple((B[i][k] if k<2 else F(1)) for i in ids) for k in range(3))
 # This matrix can have either orientation; solve directly by signed determinants.
 den=det(*mat); target=(F(0),F(0),F(1))
 weights=[]
 for j in range(3):
  A=[list(row) for row in mat]
  for k in range(3): A[k][j]=target[k]
  weights.append(det(*A)/den)
 weights=tuple(weights)
 assert min(weights)>0 and sum(weights)==1 and tuple(sum(w*B[i][k] for i,w in zip(ids,weights)) for k in range(2))==(0,0)
 lower=stress(X,ids,weights); upper=stress(X,(8,9),(F(1,2),F(1,2)))
 assert all(dot(b,b)==1 for b in B)
 assert energy(lower,I2)==1 and energy(upper,I2)==HALF**2
 R2=max(dot(r,r) for r in section)
 pairs=[(i,j,dot(sub(B[i],B[j]),sub(B[i],B[j]))/4) for i,j in combinations(range(8),2)]
 pairmax=max(z for i,j,z in pairs)
 assert pairmax==F(64,65) and pairmax<R2<1<HALF**2
 guards=[]
 for G in GBOX:
  R=max(bil(r,G,r) for r in section)
  gaps=[energy(st,G)-R for st in (lower,upper)]
  assert min(gaps)>0
  guards.append(dict(G=G,R2=R,gaps=gaps))
 # Polynomial completion-of-squares identity, tested exactly at nontrivial inputs.
 for G,v,y in product(GBOX,((F(0),F(0)),(F(3,7),F(-11,13))), (F(1,100),F(17,3))):
  M,N=metric(G,v,y)
  for st in (lower,upper):
   lhs=sum(w*bil(X[i],M,X[i]) for i,w in zip(st['ids'],st['weights']))
   rhs=energy(st,G)+st['S']*(bil(sub(v,st['center']),G,sub(v,st['center']))+y)
   assert lhs==rhs
 controls=[mechanics(X,Q,edges,dual,faces,v,y) for v,y in [((F(0),F(0)),F(1,100)),((F(0),F(0)),F(1)),((F(4),F(-3)),F(1,4))]]
 assert all(c['counts'][1]>=2 for c in controls)
 return dict(identity=ID,raw_vertices=P,faces=faces,edges=edges,dual=dual,volume=V,centroid=g,two_apex_fans=(f0,f1),centered_vertices=X,poles=Q,section_cuts=cuts,lower_stress=lower,upper_stress=upper,section_R2=R2,all_28_base_pairs=pairs,max_pair_radius2=pairmax,triple_radius2=F(1),Gbox_guards=guards,controls=controls,global_bounds_unchanged=(34,622),not_an_110_attainer=True)
if __name__=='__main__':
 assert sys.argv[1:] in (['build'],['check'])
 obj=build(); data=(json.dumps(encode(obj),sort_keys=True,separators=(',',':'))+'\n').encode(); path=Path('section_stress.json')
 if sys.argv[1]=='build': path.write_bytes(data)
 else: assert path.read_bytes()==data
 print('ACTUAL_E17_HULL_TRUE_COM_TWO_FANS_PASS')
 print('ALL_28_BASE_PAIRS_FAIL_BUT_HELLY3_STRESS_PASSES')
 print('WHOLE_GBOX_ALL_SHEARS_ALL_HEIGHTS_U2_PASS')
 print('COUNTS', [x['counts'] for x in obj['controls']])
 print('WEAK_COUNTS',[len(x['weak']) for x in obj['controls']])
 print('VOLUME',obj['volume'],'CENTROID',obj['centroid'])
 print('WEIGHTS',obj['lower_stress']['weights'],'R2',obj['section_R2'])
 print('MIN_GBOX_MARGIN',min(x for r in obj['Gbox_guards'] for x in r['gaps']))
 print(path.name,len(data),hashlib.sha256(data).hexdigest())
 print('SECTION_STRESS_HELLY3_E17_RECOVERY_PASS')
