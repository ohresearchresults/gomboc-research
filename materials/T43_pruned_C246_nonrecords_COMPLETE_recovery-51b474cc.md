# material-51b474ccdfb5

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Complete recovery of two exact pruned T43 nonrecords

This immutable capsule preserves the exact local source whose earlier material link [internal-source-reference] returned not-owned. It is a new accessible recovery record, not a claimed alias of that failed source ID. It includes all literal input and every code dependency; no previous sandbox, attachment, numerical library, or FULL76 is required. These bodies remain own222, NOT own110. Canonical own110 remainsC622 and the goal C<500 is unmet.

For integer T43 rows p/1000 define p'=[L p+(n cross w)max(0,n.p-H)]/(1000L), then take the convex hull of ONLY these43 moved old vertices. No section vertices are inserted. This is not the full filled hinge image; its own uniform filled mass is recomputed, not obtained from the full-hinge affine moment law. Every full-dimensional member has<=43 vertices, hence E<=123,C<=246.

Exact controls, both V43/E123/F82,C246,own strict222,additionalweak000,primitivezero000:
- T43_PRUNED_HINGE_5196: n=(-3,-1,-2),w=(6,-3,-17),H2878,L280. P=.5212151179484401,Q=.6357933975335549, both below baseline(.5341742685943558,.655896727661406). Exactly21 old triangular facets are replaced, with no complexity increase. Coordinates require at most19bits in reduced numerator/denominator and COM denominator60bits. Old U24/29 and stable material triangles[6,24,29],[15,29,21] still touching elder29 remain; current H0--6,29--41. P24->29 component10/cut33,path24,5,3,2,1,0,6,29; Q component40/cut26. No pair cancellation or stable-root detachment.
- T43_PRUNED_HINGE_14875: n=(-3,1,0),w=(-20,5,-1),H-1091,L200. P=.5154382278722822,Q=.6508451157368185; compared with5196, P is lower but Q higher. Coordinates at most18bits,COM denominator59bits. Old triangles(27,35,37),(27,36,37) become(27,35,36),(35,36,37). Same U and stable material triangles remain; H0--4,29--41; P component10/cut33,Q45/cut27. This is a true interface diagonal flip, not a goal body.

The exact source enumerates every supporting triple and requires all maximal facets triangular, every input point used and each actual edge to have two owners. It recomputes uniform filled volume/first moment and crosschecks another tetrahedral coning origin, not a second hull engine. All strict and closed S/U/H signs are exact in integer own-centred coordinates, including both edge-foot bounds and both cone coefficients. Every positive true-edge primal and polar bar is retained with complete components, cuts and attaining paths. No threshold is used. Euler and barcode/count identities are postchecks rather than the source of the census. This is a simplicial-body auditor, not a general nonsimplicial one. The top-level n:null legacy field is unused; recipe.normal and integer_points define each exact body.

Save the sole code block as pruned_hinge_recovery.py including final newline:7239bytes SHA256 f3377e7fff88927175d1784ba7e78dcaf02e6bc7993a307b01b1b33ab3d57eb4. Execute `python -B -S pruned_hinge_recovery.py` under standard-library CPython3.13.5. Expect PRUNED_HINGE_EXACT_PASS for baseline and both named controls, each [43,123,82],[2,2,2],[0,0,0]. Reproduced files:
T43_BASE.json6782bytes SHAab025042b19daba26735c702cd3dffeae54b063a644bd5422ca7626ca10b9c13;
T43_PRUNED_HINGE_5196.json7733bytes SHA56a11ba40f585c09f8a1e1098316ed3ef95f025ec19d20687df08ab0cbbcf383;
T43_PRUNED_HINGE_14875.json8049bytes SHA96c1326660a5822ed604a8b8bf2e383c47509fccf224c6cc206111c0ae752802.

```python
"""New finite-hinge atlas implementation; literal T43 input from immutable recovery."""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
import math,json
P0=[[-1131,-380,23],[-1127,-283,-218],[-1086,-225,-391],[-1013,-181,-547],[-945,-683,646],[-931,-156,-666],[-871,-801,885],[-869,-137,-738],[-780,-129,-818],[-668,-131,-892],[-635,202,-115],[-589,230,-7],[-559,224,54],[-528,217,107],[-496,331,-186],[-445,199,212],[-382,425,-214],[-366,407,-88],[-316,410,9],[-307,448,-285],[-230,462,-332],[-215,439,46],[-128,476,-366],[-30,481,-367],[-2,-201,-1240],[126,415,143],[140,485,-321],[295,502,-44],[325,457,97],[385,-951,2433],[389,393,124],[432,342,135],[462,305,132],[491,268,127],[517,230,121],[553,-80,-600],[564,161,93],[602,94,61],[633,24,23],[657,-49,-23],[674,-125,-78],[675,-281,-220],[681,-203,-143]]
P=[tuple(x) for x in P0]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,t):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def primitive(a):
 g=math.gcd(*a);return tuple(x//g for x in a)
def hull(X):
 faces=[]; edges=defaultdict(list)
 for ids in combinations(range(len(X)),3):
  a,b,c=[X[i] for i in ids];m=cross(sub(b,a),sub(c,a))
  if not any(m):continue
  h=dot(m,a);s=[dot(m,p)-h for p in X]
  if min(s)<0<max(s) or min(s)==max(s):continue
  if max(s)>0:m=mul(m,-1);ids=(ids[0],ids[2],ids[1])
  assert s.count(0)==3
  m=primitive(m);h=dot(m,a);fi=len(faces);faces.append((ids,m,h))
  for e in combinations(ids,2):edges[tuple(sorted(e))].append(fi)
 assert all(len(x)==2 for x in edges.values()); assert len(X)-len(edges)+len(faces)==2
 return faces,dict(edges)
faces,edges=hull(P)

"""Exact recovery/audit of complexity-safe pruned T43 hinges. Standard library.
No numerical hull, no tolerance, no suppressed positive radial bars.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
from pathlib import Path
import json,math,hashlib,sys
BASE=P

def chord(a,b):
 A=dot(a,a);B=dot(a,b);C=dot(b,b)
 if B>=A:return A
 if B>=C:return C
 return F(A*C-B*B,A+C-2*B)

def bars(X,EE):
 rr=[dot(x,x) for x in X];ed=sorted([(chord(X[i],X[j]),i,j) for i,j in EE],key=lambda a:(-a[0],a[1],a[2]))
 par=list(range(len(X)));peaks=par.copy();out=[]
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for death,u,v in ed:
  i,j=root(u),root(v)
  if i==j:continue
  if (rr[peaks[i]],-peaks[i])<(rr[peaks[j]],-peaks[j]):i,j=j,i
  birth=rr[peaks[j]]
  if birth>death:out.append({'root':peaks[j],'elder':peaks[i],'birth':birth,'death':death,'depth':F(birth-death,birth)})
  par[j]=i
 for o in out:
  adj=defaultdict(list);inc=defaultdict(list)
  for val,u,v in ed:
   if val>o['death']:adj[u].append(v);adj[v].append(u)
   if val>=o['death']:inc[u].append(v);inc[v].append(u)
  comp={o['root']};stack=[o['root']]
  for u in stack:
   for v in adj[u]:
    if v not in comp:comp.add(v);stack.append(v)
  cut=[(val,u,v) for val,u,v in ed if (u in comp)!=(v in comp)]
  assert max(val for val,u,v in cut)==o['death']
  stack=[o['root']];prev={o['root']:None}
  for u in stack:
   if u==o['elder']:break
   for v in sorted(inc[u]):
    if v not in prev:prev[v]=u;stack.append(v)
  assert o['elder'] in prev
  path=[o['elder']]
  while path[-1]!=o['root']:path.append(prev[path[-1]])
  path.reverse()
  assert min(chord(X[i],X[j]) for i,j in zip(path,path[1:]))==o['death']
  o.update(component=sorted(comp),cut=sorted([i,j] for val,i,j in cut),attaining=sorted([i,j] for val,i,j in cut if val==o['death']),path=path)
 return sorted(out,key=lambda b:(-b['depth'],b['root']))

def freeze(n,w,H,L):
 c=cross(n,w)
 return [add(mul(p,L),mul(c,max(0,dot(n,p)-H))) for p in BASE],1000*L

def exact(name,n=None,w=None,H=None,L=None):
 X,D=(BASE,1000) if n is None else freeze(n,w,H,L)
 fa,ed=hull(X);assert set(i for f,m,h in fa for i in f)==set(range(len(X)));W=sum(det(*(X[i] for i in f)) for f,m,h in fa)
 T=tuple(sum(det(*(X[i] for i in f))*sum(X[i][k] for i in f) for f,m,h in fa) for k in range(3))
 assert W>0;Z=[sub(mul(x,4*W),T) for x in X];den=4*W*D
 # Independent exact volume/COM calculation coned from mean of all material points.
 q=tuple(F(sum(x[k] for x in X),len(X)) for k in range(3));vv=F(0);mm=(F(0),)*3
 for f,m,h in fa:
  a,b,c=(X[i] for i in f);v=F(det(sub(a,q),sub(b,q),sub(c,q)),6);assert v>0
  vv+=v;mm=add(mm,mul(add(add(a,b),add(c,q)),v/4))
 assert vv==F(W,6) and mm==tuple(F(t,24) for t in T)
 strict=[[],[],[]];weak=[[],[],[]];signs={s:[0,0,0] for s in ('U','S','H')}
 def classify(slot,label,vals):
  for x in vals:signs['SUH'[slot]][(x>0)-(x<0)+1]+=1
  if min(vals)>=0:(strict if min(vals)>0 else weak)[slot].append(label)
 for i,z in enumerate(Z):classify(1,i,[-dot(z,sub(t,z)) for j,t in enumerate(Z) if j!=i])
 for f,(ids,n,h) in enumerate(fa):
  assert 4*W*h-dot(n,T)>0
  vals=[dot(n,cross(Z[a],Z[b])) for a,b in zip(ids,ids[1:]+ids[:1])]
  classify(0,f,vals)
 for (i,j),(f,g) in sorted(ed.items()):
  a=Z[i];d=sub(Z[j],a);d2=dot(d,d);tn=-dot(a,d);q=add(mul(a,d2),mul(d,tn))
  n,m=fa[f][1],fa[g][1];aa=dot(n,n);bb=dot(n,m);cc=dot(m,m);ds=aa*cc-bb*bb;assert ds>0
  ln=cc*dot(q,n)-bb*dot(q,m);mn=aa*dot(q,m)-bb*dot(q,n)
  assert mul(q,ds)==add(mul(n,ln),mul(m,mn))
  classify(2,[i,j],[tn,d2-tn,ln,mn])
 Q=[tuple(F(u,4*W*h-dot(n,T)) for u in n) for ids,n,h in fa]
 pp=bars(Z,sorted(ed));qq=bars(Q,sorted(tuple(sorted(x)) for x in ed.values()))
 if not any(weak):
  assert len(strict[0])+len(strict[1])-len(strict[2])==2
  assert len(pp)==len(strict[1])-1 and len(qq)==len(strict[0])-1
 return dict(name=name,n=n if False else None,VEF=[len(X),len(ed),len(fa)],C=2*len(ed),denominator=D,integer_points=X,
 volume=F(W,6*D**3),moment=tuple(F(t,24*D**4) for t in T),centroid=tuple(F(t,den) for t in T),
 facets=[f[0] for f in fa],support_planes=[list(n)+[h] for f,n,h in fa],edges=sorted(ed),strict=strict,additional_weak=weak,
 strict_counts=list(map(len,strict)),weak_counts=list(map(len,weak)),primitive_sign_counts=signs,P=pp,Q=qq,
 radial_frame='P=4W*integer_points-T; Q=n/(n.P_f), common positive scaling of own-centred physical primal and polar')

def serialize(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):serialize(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [serialize(v) for v in x]
 return x
if __name__=='__main__':
 cases=[('T43_BASE',None,None,None,None),('T43_PRUNED_HINGE_5196',(-3,-1,-2),(6,-3,-17),2878,280),('T43_PRUNED_HINGE_14875',(-3,1,0),(-20,5,-1),-1091,200)]
 for name,n,w,h,l in cases:
  out=exact(name,n,w,h,l);out['recipe']={'normal':n,'cross_partner':w,'raw_offset':h,'velocity_denominator':l}
  raw=(json.dumps(serialize(out),sort_keys=True,separators=(',',':'))+'\n').encode();path=Path(__file__).with_name(name+'.json');path.write_bytes(raw)
  print('PRUNED_HINGE_EXACT_PASS',name,out['VEF'],out['strict_counts'],out['weak_counts'],out['primitive_sign_counts'],[float(b['depth']) for b in out['P']],[float(b['depth']) for b in out['Q']],len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
```
