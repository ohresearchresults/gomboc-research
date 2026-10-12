# material-a7f923bbc865

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J134 Recovery capsule part 1 of 4 — exact C2 nonwinners

Object family: J134_C2_SHORT_G4/G10, J134_C2_WIDE_G4/G10, J134_C2_TWIST_G4/G10. These are SIX distinct rational homogeneous own132 bodies, not own110 and not canonical records. Part1 plus part2 reconstruct all six endpoints without any old sandbox. Parts3 and4 preserve producing searches and the scale-census method. The parent is the literal J133_C2_CAPROOT_G8 from coordinator material [internal-source-reference]; the exact mechanics extend geom133.py from [internal-source-reference]. All necessary literal parent data are repeated here as the small generator, not merely linked. This is one inherited Fraction implementation with exact identities, not two independent audits.

Environment actually used: Python3.13.5, NumPy2.3.5, SciPy1.17.0, Linux; OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. Save each fenced unit under its heading. Part2 supplies the six *.input.json files and EXPECTED134.json. Reconstruction/verification command: `python replay134.py`. Expected terminal marker: `J134_SIX_OWN132_RECOVERY_PASS_NO_110`. Endpoint input/point/audit hashes are in EXPECTED134.json. A failed assertion or missing dependency is not a pass. Qhull only nominates: every candidate is checked against all exact halfspaces, every hull facet is matched to an input halfspace, and the entire reconstructed polytope is thereby proved equal to the H intersection.

## input134.py — 2487 bytes; SHA256 74e39be39c1c5513467df36cc6ab7c59d2fe753bfa4501459b0f015598f45743
```python
from pathlib import Path
from fractions import Fraction
import json, hashlib
P = [[511468580, 25097891, -9555418254], [835083705, -439940695, -8591203661], [1422353202, 54022401, -8773704405], [1445101924, 119659634, -9785041435], [2504117446, 269500908, -9500104504], [3265730980, 263085077, -9230829355], [3672055717, 292920706, -9065265276], [4163936909, 604276879, -8811459077], [4610168206, 803116114, -8552229919], [5025705834, 1013078261, -8274112762], [5516773493, 1278595762, -7887595358], [5926740802, 1478889336, -7525342623], [6200673683, 1637088772, -7255527835], [6476595502, 1809438817, -6953675311], [6815078146, 2060731469, -6520466168], [7048385697, 2249286268, -6186061418], [7362360563, 2527261493, -5652842061], [7648446960, 2859081665, -5029089022], [7876075804, 3232064737, -4337869861], [8057034135, 3589466882, -3570119278], [8205285505, 3914585272, -2620044624], [8211306332, 4275369021, -1662367975], [8093991934, 4617732471, -587506704], [7767842751, 5042067514, 399178635], [7423633992, 5222760302, 1484624736], [6978189797, 5298486011, 2547335060], [5646797937, 6105915440, 3325533447], [4045034094, 7012014746, 3362862013], [2126934463, 7607996289, 3221750547], [-635326644, 7586661867, 2611761549], [-1645839615, 7072687993, 3223508486], [-3257096813, 5667597632, 4143302846], [-2633386080, 6644733529, 3297005387], [-4709779532, 4689791325, 3498342739], [-6413764484, 2307019068, 2929973705], [-6839848146, -1313659287, 4848223644], [-7332989774, -2927222448, 3715311271], [-4742308501, -5102527081, 5151878692], [-950461477, -6647675941, 4788443817], [968745720, -5671098782, 5152625190], [3768906278, -3782722385, 5152625190]]
def make(k=8,compact=True):
 D=10**k; half=[[round(Fraction(t*D,10**10))for t in p]for p in P]
 if compact:half=half[3:]
 X=[[0,0,-D]]+half+[[-x,-y,z]for x,y,z in half]
 return {'scale':D,'points':X}
if __name__=='__main__':
 for k,sha in [(6,'e71416393d9e05f209694755810843664a5b82118a8de8d4eb2ccff931419e0c'),(8,'f33aaa557d8f40b5e8cadf6f7cdbe675f506ed0af990e1e9266f764016c15196'),(10,'df06e390aec1dbf83401df8ba98785881559a06ee2d494791a6ae16dd0dc5c27')]:
  d=make(k,False);d['name']='J133_C2_CAPROOT_G'+str(k)
  b=(json.dumps(d,sort_keys=True,separators=(',',':'))+'\n').encode()
  assert hashlib.sha256(b).hexdigest()==sha
  Path(d['name']+'.json').write_bytes(b)
 Path('C2_COMPACT_G8.json').write_text(json.dumps(make(),sort_keys=True,separators=(',',':'))+'\n')
 print('C2_ORIGINAL_INPUT_IDENTITIES_AND_COMPACTION_PASS')
```

## geom134.py — 8412 bytes; SHA256 771ab593a8c56e039853f4913fb1a07f7f5e98f01c17dbf9213d5ecf8140328c
```python
"""Actual homogeneous geometry; numerical nominations and exact maximal-facet audit.
The exact mechanics and persistence adapt geom133.py (J133 source part1).
New: merges coplanar nominated triangles into exact maximal facets.
One inherited rational implementation, not a second independent auditor.
"""
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import numpy as np
from scipy.spatial import ConvexHull
import json
Z=F(0)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Z)
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def serial(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,np.ndarray):return serial(x.tolist())
 if isinstance(x,np.generic):return x.item()
 if isinstance(x,dict):return {str(k):serial(v)for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [serial(y)for y in x]
 return x

def chords(Y):
 D=Y[None,:,:]-Y[:,None,:];l=np.linalg.norm(D,axis=2)
 with np.errstate(divide='ignore',invalid='ignore'):
  A=np.einsum('ik,ijk->ij',Y,D)/(np.linalg.norm(Y,axis=1)[:,None]*l)
 np.fill_diagonal(A,-np.inf)
 return A

def widest(A,root):
 """Maximum bottleneck paths i->root, valid even for negative edge weights."""
 n=len(A);v=np.full(n,-np.inf);v[root]=np.inf;seen=np.zeros(n,bool);parent=np.full(n,-1,int)
 for _ in range(n):
  j=np.argmax(np.where(seen,-np.inf,v));seen[j]=True
  c=np.minimum(v[j],A[:,j]);take=(~seen)&(c>v);v[take]=c[take];parent[take]=j
 return v,parent

def persistence(X,E,exact=False):
 if exact:
  r=[dot(x,x)for x in X]
 else:r=np.einsum('ij,ij->i',X,X)
 par=list(range(len(X)));peak=list(r);out=[];events=[]
 def rt(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for a,b in E:
  if exact:
   d=sub(X[b],X[a]);t=max(Z,min(F(1),-dot(X[a],d)/dot(d,d)));p=add(X[a],mul(t,d));level=dot(p,p)
  else:
   d=X[b]-X[a];t=np.clip(-X[a]@d/(d@d),0,1);p=X[a]+t*d;level=p@p
  events.append((level,int(a),int(b)))
 for level,i,j in sorted(events,reverse=True):
  a,b=rt(i),rt(j)
  if a==b:continue
  if peak[a]<peak[b]:a,b=b,a
  depth=1-level/peak[b]
  if depth>(0 if exact else 1e-12):out.append(dict(root=b,edge=(i,j),birth=peak[b],death=level,depth=depth))
  par[b]=a
 return sorted(out,key=lambda q:-q['depth'])

def numeric(X,full=False):
 X=np.asarray(X,float);h=ConvexHull(X);tri=h.simplices.copy()
 n=np.cross(X[tri[:,1]]-X[tri[:,0]],X[tri[:,2]]-X[tri[:,0]])
 flip=np.einsum('ij,ij->i',n,h.equations[:,:3])<0;tri[flip]=tri[flip][:,[0,2,1]]
 d=np.einsum('ij,ij->i',X[tri[:,0]],np.cross(X[tri[:,1]],X[tri[:,2]]));V=d.sum()/6
 assert V>1e-12;g=(d[:,None]*X[tri].sum(1)).sum(0)/(24*V);Y=X-g
 # For nomination only. Exact endpoints use rational coplanarity below.
 group={};reps=[];which=[]
 for i,eq in enumerate(h.equations):
  key=tuple(np.round(eq,11));j=group.get(key)
  if j is None:j=len(reps);group[key]=j;reps.append(i)
  which.append(j)
 E0={}
 for i,t in enumerate(tri):
  for a,b in zip(t,np.roll(t,-1)):E0.setdefault(tuple(sorted((int(a),int(b)))),[]).append(which[i])
 E={k:v for k,v in E0.items()if len(set(v))==2};ee=np.array(list(E),int);dual=np.array(list(E.values()),int)
 fs=tri[reps];n=np.cross(Y[fs[:,1]]-Y[fs[:,0]],Y[fs[:,2]]-Y[fs[:,0]]);hh=np.einsum('ij,ij->i',n,Y[fs[:,0]]);assert hh.min()>0
 Q=n/hh[:,None];active=np.array(sorted(h.vertices));p=chords(Y[active]);q=chords(Q)
 u=active[np.flatnonzero(p.max(1)<0)];s=np.flatnonzero(q.max(1)<0)
 root=int(np.argmax((Q*Q).sum(1)));w,pa=widest(q,root)
 z=dict(V=len(active),E=len(E),F=len(fs),S=len(s),U=len(u),S_indices=s,U_indices=u,volume=V,centroid=g,Y=Y,Q=Q,tri=tri,representatives=fs,edges=ee,dual=dual,active=active,A=p,B=q,root=root,capacity=w,parent=pa)
 if full:z.update(P=persistence(Y,ee),Qbars=persistence(Q,dual))
 return z

def prim(v):
 D=lcm(*(x.denominator for x in v));w=[int(x*D)for x in v];g=reduce(gcd,w);return tuple(t//g for t in w)

def exact(X,reference=None):
 X=[tuple(F(x)for x in p)for p in X];h=ConvexHull(np.array(X,float));groups={}
 for tt in h.simplices:
  t=list(map(int,tt));a,b,c=[X[i]for i in t];n=cross(sub(b,a),sub(c,a));hh=dot(n,a)
  sg=[dot(n,p)-hh for p in X]
  if max(sg)>0:
   assert min(sg)>=0,'Nonsupport nomination';n=mul(-1,n);hh=-hh;t[1],t[2]=t[2],t[1]
  key=prim((*n,hh));groups.setdefault(key,[]).append(tuple(t))
 fs=[];planes=[];tris=[]
 for key,tt in sorted(groups.items()):
  n=tuple(F(v)for v in key[:3]);hh=F(key[3]);assert max(dot(n,p)-hh for p in X)==0
  # A supporting facet's triangulation boundary is its exact convex cycle.
  edges={}
  for t in tt:
   for a,b in zip(t,t[1:]+t[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append((a,b))
  bd={v[0][0]:v[0][1]for v in edges.values()if len(v)==1};assert len(bd)>=3
  start=min(bd);cyc=[start];i=bd[start]
  while i!=start:cyc.append(i);i=bd[i];assert len(cyc)<=len(bd)
  assert len(cyc)==len(bd)
  # Collinear boundary points are not true vertices; remove them exactly.
  changed=True
  while changed:
   changed=False
   for j in range(len(cyc)):
    if cross(sub(X[cyc[j]],X[cyc[j-1]]),sub(X[cyc[(j+1)%len(cyc)]],X[cyc[j]]))==(Z,Z,Z):
     cyc.pop(j);changed=True;break
  assert all(dot(n,cross(sub(X[cyc[(j+1)%len(cyc)]],X[cyc[j]]),sub(X[cyc[(j+2)%len(cyc)]],X[cyc[(j+1)%len(cyc)]])))>0 for j in range(len(cyc)))
  fs.append(tuple(cyc));planes.append((n,hh));tris.extend((cyc[0],cyc[j],cyc[j+1])for j in range(1,len(cyc)-1))
 E={};ori={}
 for f,t in enumerate(fs):
  for a,b in zip(t,t[1:]+t[:1]):key=tuple(sorted((a,b)));E.setdefault(key,[]).append(f);ori.setdefault(key,[]).append((a,b))
 assert all(len(v)==2 for v in E.values());assert all(v[0]==v[1][::-1]for v in ori.values())
 vs=sorted({i for t in fs for i in t});assert len(vs)-len(E)+len(fs)==2
 seen={0};todo=[0]
 while todo:
  f=todo.pop()
  for a,b in zip(fs[f],fs[f][1:]+fs[f][:1]):
   for k in E[tuple(sorted((a,b)))]:
    if k not in seen:seen.add(k);todo.append(k)
 assert len(seen)==len(fs)
 V=Z;M=(Z,Z,Z)
 for i,j,k in tris:
  a,b,c=X[i],X[j],X[k];d=dot(a,cross(b,c));V+=d/6;M=add(M,mul(d/24,add(add(a,b),c)))
 assert V>0;g=mul(1/V,M);c=g if reference is None else tuple(F(x)for x in reference);Y=[sub(p,c)for p in X]
 S=[];U=[];H=[];weak=[[],[],[]];zero=[0,0,0];Q=[]
 for i,(t,(n,hh))in enumerate(zip(fs,planes)):
  hh-=dot(n,c);assert hh>0;Q.append(mul(1/hh,n));sig=[dot(n,cross(Y[a],Y[b]))for a,b in zip(t,t[1:]+t[:1])];zero[0]+=sum(v==0 for v in sig)
  if min(sig)>0:S.append(i)
  elif min(sig)>=0:weak[0].append(i)
 nb={i:[]for i in vs}
 for a,b in E:nb[a].append(b);nb[b].append(a)
 for i in vs:
  sig=[dot(Y[i],sub(Y[j],Y[i]))for j in nb[i]];zero[1]+=sum(v==0 for v in sig)
  if max(sig)<0:U.append(i)
  elif max(sig)<=0:weak[1].append(i)
 for (a,b),(i,j)in sorted(E.items()):
  d=sub(Y[b],Y[a]);dd=dot(d,d);aa=-dot(Y[a],d);bb=dd-aa;p=add(Y[a],mul(aa/dd,d));n,m=planes[i][0],planes[j][0]
  nn,nm,mm=dot(n,n),dot(n,m),dot(m,m);D=nn*mm-nm*nm;assert D>0
  x=dot(p,n)*mm-dot(p,m)*nm;y=dot(p,m)*nn-dot(p,n)*nm;assert mul(D,p)==add(mul(x,n),mul(y,m))
  sig=[aa,bb,x,y];zero[2]+=sum(v==0 for v in sig)
  if min(sig)>0:H.append((a,b))
  elif min(sig)>=0:weak[2].append((a,b))
 assert len(S)+len(U)-len(H)==2
 P=persistence(Y,E,True);qb=persistence(Q,E.values(),True);assert len(P)==len(U)-1 and len(qb)==len(S)-1
 # Independent identities inside this inherited implementation, not another engine.
 vc=Z;mc=(Z,Z,Z)
 for i,j,k in tris:
  a,b,d=sub(X[i],g),sub(X[j],g),sub(X[k],g);z=dot(a,cross(b,d));assert z>0;vc+=z/6;mc=add(mc,mul(z/24,add(add(a,b),d)))
 assert vc==V and mc==(Z,Z,Z)
 polarU=[i for i,p in enumerate(Q)if all(dot(p,sub(q,p))<0 for j,q in enumerate(Q)if i!=j)];assert polarU==S
 return dict(V=len(vs),E=len(E),F=len(fs),strict=[len(S),len(U),len(H)],weak=list(map(len,weak)),primitive_zero=zero,S=S,U=U,H=H,S_cycles=[fs[i]for i in S],faces=fs,active=vs,volume=V,moment=M,centroid=g,reference=c,is_own=c==g,P=P,Q=qb)

if __name__=='__main__':
 import sys
 from pathlib import Path
 d=json.loads(Path(sys.argv[1]).read_text());X=[tuple(F(t,d['scale'])for t in p)for p in d['points']];z=exact(X)
 b=json.dumps(serial(z),sort_keys=True,separators=(',',':'))+'\n';Path(sys.argv[1]+'.audit.json').write_text(b)
 print(z['V'],z['E'],z['F'],z['strict'],z['weak'],z['primitive_zero'],[float(x['depth'])for x in z['P']],[float(x['depth'])for x in z['Q']],flush=True)
```

## freeze134.py — 4648 bytes; SHA256 5a2decd2b79714a054c963f256a11cf544ab72fe47aea3d9e4ff277cc1648d5c
```python
"""Freeze polar-chain halfspaces, reconstruct exact vertices, prove equality.
Original maximal supports are recovered from the literal rational parent.
Only new polar rows are rounded ties-to-even to the stated rational grid;
paired rows, the through-apex head, and the axial cap are imposed exactly.
Qhull nominates intersections; each accepted vertex obeys ALL exact supports.
Every exact hull facet is then matched to an input support. This proves that
the recovered hull equals the entire bounded H intersection, not merely a
subset of nominated vertices. The actual filled-volume centroid is audited.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json,hashlib,argparse,sys,numpy as np
sys.set_int_max_str_digits(0)
from scipy.spatial import ConvexHull,HalfspaceIntersection
import geom134 as e
from input134 import make

def baseline():
 d=make(8);X=[tuple(F(t,d['scale'])for t in p)for p in d['points']];nf=ConvexHull(np.array(X,float));planes=set()
 for tt in nf.simplices:
  a,b,c=[X[int(i)]for i in tt];n=e.cross(e.sub(b,a),e.sub(c,a));hh=e.dot(n,a)
  sg=[e.dot(n,p)-hh for p in X]
  if max(sg)>0:
   assert min(sg)>=0;n=e.mul(-1,n);hh=-hh
  assert hh>0;planes.add(e.prim((*n,hh)))
 return X,[tuple(F(x)for x in row)for row in sorted(planes)]

def solve(rows):
 a,b,c=[tuple(x[:3])for x in rows];D=e.dot(a,e.cross(b,c))
 if not D:return None
 return e.mul(1/D,e.add(e.add(e.mul(rows[0][3],e.cross(b,c)),e.mul(rows[1][3],e.cross(c,a))),e.mul(rows[2][3],e.cross(a,b))))

def recover(H,c):
 HF=np.array([[float(t)for t in r[:3]]+[-float(r[3])]for r in H]);HF/=np.linalg.norm(HF[:,:3],axis=1)[:,None]
 obj=HalfspaceIntersection(HF,np.array([0.,0.,float(c)]));good=set();tried=set();bad=0
 for point,active in zip(obj.intersections,obj.dual_facets):
  near=np.flatnonzero(np.abs(HF[:,:3]@point+HF[:,3])<1e-9)
  ids=sorted(set(active)|set(map(int,near)))
  for t in combinations(ids,3):
   if t in tried:continue
   tried.add(t);v=solve([H[i]for i in t])
   if v is not None:
    if all(e.dot(r[:3],v)<=r[3]for r in H):good.add(v)
    else:bad+=1
 X=sorted(good);assert len(X)>=4
 audit=e.exact(X)
 keys=set(e.prim(row)for row in H)
 for face in audit['faces']:
  a,b,c0=[X[i]for i in face[:3]];n=e.cross(e.sub(b,a),e.sub(c0,a));hh=e.dot(n,a)
  assert e.prim((*n,hh))in keys,'Missing supporting facet: nominated hull is incomplete'
 return X,audit,dict(nominated=len(obj.intersections),triples=len(tried),rejected_infeasible=bad,exact_vertices=len(X),all_hull_facets_are_input_supports=True)

def write(name,obj):
 s=(json.dumps(e.serial(obj),sort_keys=True,separators=(',',':'))+'\n').encode();Path(name).write_bytes(s);return dict(name=name,bytes=len(s),sha256=hashlib.sha256(s).hexdigest())

def freeze(record,name,grid=10):
 X0,H=baseline();c=F(str(record['c']));D=10**grid;raw=record['H'];n=record['n'];extra=raw[-(2*n+1):]
 qs=[]
 for i in range(n):
  q=[F(round(F(float(t))*D),D)for t in extra[2*i][:3]]
  if i==0:q[2]=-1/(1+c)
  qs.extend([tuple(q),(-q[0],-q[1],q[2])])
 qs.append((F(0),F(0),F(round(F(float(extra[-1][2]))*D),D)))
 newH=[(*q,1+q[2]*c)for q in qs];H+=newH
 inp=dict(name=name,parent='J133_C2_CAPROOT_G8 compact exact77',new_polar_rows=qs,reference_c=c,grid=grid,producing_parameters={k:record[k]for k in ['c','n','tau','mode','kappa']if k in record})
 a=write(name+'.input.json',inp);X,z,rec=recover(H,c);b=write(name+'.points.json',dict(points=X));cc=write(name+'.audit.json',z)
 out=dict(name=name,VEF=[z['V'],z['E'],z['F']],strict=z['strict'],weak=z['weak'],primitive=z['primitive_zero'],P=[float(x['depth'])for x in z['P']],Q=[float(x['depth'])for x in z['Q']],g=[float(x)for x in z['centroid']],g_minus_reference=float(z['centroid'][2]-c),volume=float(z['volume']),reconstruction=rec,receipts=[a,b,cc])
 print(json.dumps(out),flush=True);write(name+'.summary.json',out);return out

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay');p.add_argument('--grid',type=int,default=10);a=p.parse_args()
 if a.replay:
  d=json.load(open(a.replay));_,H=baseline();c=F(d['reference_c']);H += [(*[F(t)for t in q],1+F(q[2])*c)for q in d['new_polar_rows']]
  X,z,rec=recover(H,c);print(z['V'],z['E'],z['F'],z['strict'],z['weak'],z['primitive_zero'],rec,flush=True)
 else:
  src=json.load(open('TWIST134_FINE.json'));out=[]
  for c,n,tau,tag in [(-.98,12,0.,'SHORT'),(-.95,16,0.,'WIDE'),(-.98,20,-.05,'TWIST')]:
   r=next(x for x in src if x['c']==c and x['n']==n and x['tau']==tau);out.append(freeze(r,f'J134_C2_{tag}_G{a.grid}',a.grid))
  write(f'FREEZE134_G{a.grid}.json',out)
```

## replay134.py — 1236 bytes; SHA256 e5d5cbf3e80287b23623528dd534d2e555dc582f9763652a534069d2c9a4b024
```python
"""Cold replay of six distinct rational nonwinners, not independent engines."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import freeze134 as f

def main():
 expected=json.loads(Path('EXPECTED134.json').read_text())
 for name,rec in expected['inputs'].items():
  b=Path(name).read_bytes();assert len(b)==rec['bytes'] and hashlib.sha256(b).hexdigest()==rec['sha256']
  d=json.loads(b);_,H=f.baseline();c=F(d['reference_c']);H.extend((*[F(x)for x in q],1+F(q[2])*c)for q in d['new_polar_rows'])
  X,a,rr=f.recover(H,c);assert a['strict']==[1,3,2] and a['weak']==[0,0,0] and a['primitive_zero']==[0,0,0] and a['is_own'] and len(a['P'])==2 and not a['Q']
  prefix=d['name'];assert [a[k]for k in ['V','E','F']]==expected['objects'][prefix]
  for path,obj in [(prefix+'.points.json',dict(points=X)),(prefix+'.audit.json',a)]:
   out=f.write(path,obj);target=expected['outputs'][path];assert out['bytes']==target['bytes'] and out['sha256']==target['sha256']
  print(prefix,a['strict'],a['weak'],rr,flush=True)
 print('J134_SIX_OWN132_RECOVERY_PASS_NO_110',flush=True)
if __name__=='__main__':main()
```
