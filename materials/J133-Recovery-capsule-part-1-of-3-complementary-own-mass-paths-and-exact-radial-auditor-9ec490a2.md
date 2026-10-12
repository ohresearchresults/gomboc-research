# material-9ec490a2d5be

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J133 Recovery capsule part 1 of 3

Object family: J133 complementary own121/own211 interpolation; reusable exact simplicial auditor also used by part3. This part is autonomous for its interpolation experiment. Parts2/3 concern canonical C622 contraction and deletion experiments and explicitly name their additional immutable dependencies. Nothing here is an own110 construction.

The four complete source/input units below are UTF-8 with one final LF. Extract each fenced block to its named file in one directory. INPUT_A.txt is the literal J82_S1_ROBUST_G6 point body from fully read [internal-source-reference], not a new body. INPUT_B46.txt is the literal J132 own211 grid-six 46-point body from fully read [internal-source-reference]; remove zero-indexed point32 as instructed below to obtain J132_DELETE_45. It is NOT the unrelated J132_FREEFAN reference110 body.

## Reproduction and observed evidence
Python3.13.5, NumPy2.3.5, SciPy1.17.0; OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. Generate INPUT_B.txt by the exact command below, then run geom133.py, connect133.py build, and connect133.py paths --start 0 --count 80 --steps 40. No randomness. Qhull nominates triangular hull faces; the exact audit checks all support signs, strict triangularity, closed oriented incidence, connectedness/Euler, actual uniform volume and centroid, all strict and weak face/vertex/edge equilibria, all positive physical and polar persistence, and a second centred volume/moment identity. One adapted Fraction implementation, not independently written engines. Numerical persistence suppresses depths <=1e-13 ONLY for nomination; exact persistence has no threshold.

A is45/129/86 own121/weak000/primitive000, P approximately .5678697406886946, Q[]. B is45/129/86 own211/weak000/primitive000, P[], Q approximately .45607066704761967. The algorithm normalizes each actual own-centred body to volume1, aligns either A unstable root0 or40 with B root6, tests two reflections and72 rotations, and uses two Hungarian matching costs. It stores575 unique alignments. Only the FIRST80 were traversed, each at41 parameters i/40:3280 numerical hull evaluations. None had S1/U1; the best strictly interior sampled S+U was19. This is a bounded unsuccessful search, not an exclusion of all correspondences, paths or deformations. Every interpolated hull has at most45 vertices and E<=129; the centroid is recomputed, never linearly interpolated.

Expected files: INPUT_A.txt1013B SHA9aa811a7347db08e9da84af77772c965e78f9466c540192ef8ce651a4bee07ad; INPUT_B46.txt1009B SHA58f19272473ba118a1043990bc9734c6906001c622af17f36b1e5269b30500c7; generated INPUT_B.txt987B SHA483e07060670572890f5a3e0289fab944e94b41402503c5c6c08bbe237dddbe9; geom133.py7273B SHAf5222266a0a5e8f2e71266907dac25df087f8e650a08cdae56a69a0c1c256ac7; connect133.py3771B SHA81dd05285d41616a9e17d0e7c5ac2cbff77715bffe6508daf22014b14e0ad507. Audits: A2055B SHAb2033b0e967dc6672eab8c9b6d3aca882461e0a2770d40cde4c672b1a32c545f; B2116B SHA3a08df7a29d6c1075cd4eecf3c4da800b0462a109c96ce113dc10ec77a6128b4. PATHS133_0_80_40.json134250B SHA5f3f1147fe7c35bcfe1850cc140f7afabffc4185365029432a1a175504aa4fc1. Floating output bytes can depend on the named numerical environment; exact input and census claims do not depend on those nomination hashes.

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
python - <<'PY'
from pathlib import Path
w=Path('INPUT_B46.txt').read_text().splitlines()
assert w[0]=='46 1000000' and len(w)==47
Path('INPUT_B.txt').write_text('45 1000000\n'+'\n'.join(w[1:33]+w[34:])+'\n')
PY
python geom133.py
python connect133.py build
python connect133.py paths --start 0 --count 80 --steps 40
```

## File: INPUT_A.txt
```text
45 1000000
-1772498 -1222476 446600
-1039299 -313302 -700462
-1003288 -275901 132016
-809479 -13170 17208
-790129 68868 -233475
-774789 -231542 -897502
-797981 62277 -350742
-635384 -210168 -961663
-609466 221337 -171601
-525729 253449 -484224
-489649 -200686 -996078
-374946 -195685 -1011378
-366813 246691 105757
-316429 451849 -418573
-295644 503340 -233141
-275629 -186981 -1011480
-229896 416128 -495865
-194308 509959 -88421
-195520 -211846 -1005706
-187899 -558943 -768752
-134126 305378 -589651
-126147 -264851 -992981
-49174 491813 93901
-35621 178251 -677618
-10288 436303 144281
28080 186153 253802
64850 412231 179729
185379 412442 205366
400273 357835 238447
436566 275260 247302
489402 -473343 -873790
533167 226150 240322
619725 163301 221898
662701 219162 -3537
666794 75353 193396
728134 -96722 -608110
740107 2105 147220
797950 1378 -368423
797491 -77809 85715
835835 -160959 8618
877002 -392469 -517165
833841 -381745 -334567
864938 -239770 -88025
882247 -308985 -203874
889527 -317124 -393548
```

## File: INPUT_B46.txt
```text
46 1000000
-271637 -204592 881573
-556457 -297245 741996
-410998 -240432 830371
-961339 -404505 29170
-935513 -360099 -185472
-724210 -363271 592139
-935179 -456403 277228
787730 232662 9402
697154 393184 2825
106921 -98499 904926
331080 -47944 836071
223944 -78652 876776
516272 -48191 719610
428006 -55045 782518
717861 -26834 488551
592342 -45447 650490
660090 -37305 572916
836304 41224 112080
-136146 -169441 908388
-10763 -137106 914668
800127 1849 306578
764801 -13645 398951
824311 19766 209703
835610 70497 15624
821913 87432 -91233
656829 262862 -378146
732489 215311 -279869
786787 150633 -187629
779542 -50110 -213441
-857294 -324110 -388122
240649 506012 -384886
50966 630587 -188934
144066 547831 -331105
626934 -88725 -385576
679599 -236725 -177166
511386 558701 -41957
-573529 -515362 -490396
610752 123705 -458011
-42200 623157 -31939
379523 493143 -405565
640061 377044 -272036
209507 594400 -308486
-625411 -355216 -608231
-572769 -181153 -695498
519072 321929 -483330
-494304 64205 166717
```

## File: geom133.py
```python
#!/usr/bin/env python3
"""Numerical finite-hull nomination and exact simplicial audit.
Exact predicates are adapted from the fully read geometry132.py, not an
independent physics implementation. Numerical counters are nominations only.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
import numpy as np
from scipy.spatial import ConvexHull
R=Path(__file__).resolve().parent
O=F(0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),O)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def load(name):
 w=list(map(int,(R/name).read_text().split()));N,D=w[:2];assert len(w)==3*N+2
 return [tuple(F(t,D)for t in w[2+3*i:5+3*i])for i in range(N)]
def serial(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,np.ndarray):return serial(x.tolist())
 if isinstance(x,np.generic):return x.item()
 if isinstance(x,dict):return {str(k):serial(v)for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [serial(v)for v in x]
 return x
def write(name,obj):
 b=(json.dumps(serial(obj),sort_keys=True,separators=(',',':'))+'\n').encode();(R/name).write_bytes(b)
 return dict(name=name,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def numeric(X,full=False):
 X=np.asarray(X,float);h=ConvexHull(X);fs=h.simplices.copy()
 n=np.cross(X[fs[:,1]]-X[fs[:,0]],X[fs[:,2]]-X[fs[:,0]])
 flip=(n*h.equations[:,:3]).sum(1)<0;fs[flip]=fs[flip][:,[0,2,1]]
 d=np.einsum('ij,ij->i',X[fs[:,0]],np.cross(X[fs[:,1]],X[fs[:,2]]));V=d.sum()/6
 assert V>1e-12
 g=(d[:,None]*X[fs].sum(1)).sum(0)/(24*V);Y=X-g
 n=np.cross(Y[fs[:,1]]-Y[fs[:,0]],Y[fs[:,2]]-Y[fs[:,0]]);nn=np.linalg.norm(n,axis=1)
 area=nn/2;hh=np.einsum('ij,ij->i',n,Y[fs[:,0]]);assert min(hh)>0
 sg=np.column_stack([np.einsum('ij,ij->i',n,np.cross(Y[fs[:,k]],Y[fs[:,(k+1)%3]]))/(nn*np.linalg.norm(Y[fs[:,(k+1)%3]]-Y[fs[:,k]],axis=1))for k in range(3)])
 sv=np.min(sg,axis=1);S=np.flatnonzero(sv>0)
 E={}
 for i,t in enumerate(fs):
  for a,b in zip(t,np.roll(t,-1)):E.setdefault(tuple(sorted((int(a),int(b)))),[]).append(i)
 ee=np.array(list(E),int);i,j=ee[:,0],ee[:,1];dd=Y[j]-Y[i];length=np.linalg.norm(dd,axis=1)
 sc0=np.einsum('ij,ij->i',Y[i],dd)/length/np.linalg.norm(Y[i],axis=1)
 sc1=-np.einsum('ij,ij->i',Y[j],dd)/length/np.linalg.norm(Y[j],axis=1)
 uv=np.full(len(X),-np.inf);np.maximum.at(uv,i,sc0);np.maximum.at(uv,j,sc1)
 U=np.flatnonzero(np.isfinite(uv)&(uv<0))
 out=dict(V=len(h.vertices),E=len(E),F=len(fs),S=len(S),U=len(U),S_indices=S,U_indices=U,volume=V,centroid=g,faces=fs,edges=ee,dual=np.array(list(E.values()),int),S_guard=sv,U_guard=uv,area=area,planes=np.c_[n,hh+np.einsum('ij,j->i',n,g)],Y=Y,Q=n/hh[:,None])
 if full:
  out['P']=bars(Y,ee);out['Qbars']=bars(out['Q'],out['dual'])
 return out

def bars(X,E):
 r=np.einsum('ij,ij->i',X,X);par=np.arange(len(X));peak=r.copy();out=[]
 def rt(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 i,j=E[:,0],E[:,1];d=X[j]-X[i];tt=np.clip(-np.einsum('ij,ij->i',X[i],d)/np.einsum('ij,ij->i',d,d),0,1);p=X[i]+tt[:,None]*d
 levels=np.minimum(np.minimum(r[i],r[j]),np.einsum('ij,ij->i',p,p))
 for k in np.argsort(-levels,kind='stable'):
  a,b=rt(i[k]),rt(j[k])
  if a==b:continue
  if peak[a]<peak[b]:a,b=b,a
  depth=1-levels[k]/peak[b]
  if depth>1e-13:out.append(dict(root=int(b),edge=E[k].tolist(),depth=float(depth)))
  par[b]=a
 return sorted(out,key=lambda x:-x['depth'])

def exact_hull(X):
 h=ConvexHull(np.array(X,float));fs=[]
 for tt in h.simplices:
  t=list(map(int,tt));a,b,c=[X[i]for i in t];n=cross(sub(b,a),sub(c,a));sg=[dot(n,sub(p,a))for p in X]
  if max(sg)>0:
   assert min(sg)>=0,'Nomination is nonsupport';t[1],t[2]=t[2],t[1]
  j=t.index(min(t));fs.append(tuple(t[j:]+t[:j]))
 fs=sorted(fs);assert len(fs)==len(set(fs));planes=[];E={};oriented={}
 for f,t in enumerate(fs):
  a,b,c=[X[i]for i in t];n=cross(sub(b,a),sub(c,a));hh=dot(n,a);sg=[dot(n,p)-hh for p in X]
  assert max(sg)==0 and sum(z==0 for z in sg)==3,'Nonsimplicial endpoint unsupported'
  planes.append((n,hh))
  for k in range(3):
   a,b=t[k],t[(k+1)%3];key=tuple(sorted((a,b)));E.setdefault(key,[]).append(f);oriented.setdefault(key,[]).append((a,b))
 assert all(len(z)==2 for z in E.values()) and all(z[0]==z[1][::-1]for z in oriented.values())
 E=dict(sorted(E.items()));vs=sorted({i for t in fs for i in t});assert len(vs)-len(E)+len(fs)==2
 seen={0};todo=[0]
 while todo:
  i=todo.pop()
  for k in range(3):
   for f in E[tuple(sorted((fs[i][k],fs[i][(k+1)%3])))]:
    if f not in seen:seen.add(f);todo.append(f)
 assert len(seen)==len(fs)
 return fs,planes,E,vs

def exact_bars(X,E):
 r=[dot(p,p)for p in X];par=list(range(len(X)));peak=r[:];events=[];out=[]
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for a,b in E:
  d=sub(X[b],X[a]);t=max(O,min(F(1),-dot(X[a],d)/dot(d,d)));p=add(X[a],mul(t,d));events.append((dot(p,p),a,b))
 for z,i,j in sorted(events,reverse=True):
  a,b=root(i),root(j)
  if a==b:continue
  if peak[a]<peak[b]:a,b=b,a
  q=1-z/peak[b];assert q>=0
  if q>0:out.append(dict(root=b,edge=(i,j),birth=peak[b],death=z,depth=q))
  par[b]=a
 return sorted(out,key=lambda z:z['depth'],reverse=True)

def exact(X,reference=None):
 fs,H,E,vs=exact_hull(X);V=O;M=(O,O,O)
 for i,j,k in fs:
  a,b,c=X[i],X[j],X[k];z=dot(a,cross(b,c));V+=z/6;M=add(M,mul(z/24,add(add(a,b),c)))
 assert V>0;g=mul(1/V,M);c=g if reference is None else reference;Y=[sub(p,c)for p in X]
 S=[];U=[];saddle=[];weak=[[],[],[]];zero=[0,0,0]
 for i,(t,(n,h))in enumerate(zip(fs,H)):
  assert h-dot(n,c)>0
  sig=[dot(n,cross(Y[t[k]],Y[t[(k+1)%3]]))for k in range(3)];zero[0]+=sum(z==0 for z in sig)
  if min(sig)>0:S.append(i)
  elif min(sig)>=0:weak[0].append(i)
 nb=[[]for p in X]
 for a,b in E:nb[a].append(b);nb[b].append(a)
 for i in vs:
  sig=[dot(Y[i],sub(Y[j],Y[i]))for j in nb[i]];zero[1]+=sum(z==0 for z in sig)
  if max(sig)<0:U.append(i)
  elif max(sig)<=0:weak[1].append(i)
 for (a,b),(i,j)in E.items():
  d=sub(Y[b],Y[a]);dd=dot(d,d);aa=-dot(Y[a],d);bb=dd-aa;p=add(Y[a],mul(aa/dd,d));n,m=H[i][0],H[j][0]
  nn,nm,mm=dot(n,n),dot(n,m),dot(m,m);D=nn*mm-nm*nm;assert D>0
  x=dot(p,n)*mm-dot(p,m)*nm;y=dot(p,m)*nn-dot(p,n)*nm;assert mul(D,p)==add(mul(x,n),mul(y,m))
  sig=[aa,bb,x,y];zero[2]+=sum(z==0 for z in sig)
  if min(sig)>0:saddle.append((a,b))
  elif min(sig)>=0:weak[2].append((a,b))
 assert len(S)+len(U)-len(saddle)==2
 P=exact_bars(Y,E);Q=exact_bars([mul(1/(h-dot(n,c)),n)for n,h in H],E.values());assert len(P)==len(U)-1 and len(Q)==len(S)-1
 vc=O;mc=(O,O,O)
 for i,j,k in fs:
  a,b,d=sub(X[i],g),sub(X[j],g),sub(X[k],g);z=dot(a,cross(b,d));assert z>0;vc+=z/6;mc=add(mc,mul(z/24,add(add(a,b),d)))
 assert vc==V and mc==(O,O,O)
 return dict(V=len(vs),E=len(E),F=len(fs),strict=[len(S),len(U),len(saddle)],weak=list(map(len,weak)),primitive_zero=zero,S=S,S_cycles=[fs[i]for i in S],U=U,H=saddle,P=P,Q=Q,volume=V,moment=M,centroid=g,reference=c,is_own=c==g,faces=fs)
if __name__=='__main__':
 for name in ['INPUT_A.txt','INPUT_B.txt']:
  X=load(name);a=exact(X);print(name,a['strict'],a['weak'],a['primitive_zero'],[float(x['depth'])for x in a['P']],[float(x['depth'])for x in a['Q']],write(name+'.audit.json',a),flush=True)
```

## File: connect133.py
```python
#!/usr/bin/env python3
"""Finite own-mass paths between literal own121 and own211 point hulls.
Only nominations; every interpolated hull has at most45 vertices and E<=129.
Use independently rebuilt mass and all current S/U, not interpolated centroids.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
from itertools import permutations
import json,hashlib,argparse
import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.spatial.transform import Rotation
import geom133 as e

def normalize(X):
 z=e.numeric(X);return (np.asarray(X,float)-z['centroid'])/z['volume']**(1/3)
def align_vector(b,a):
 b=b/np.linalg.norm(b);a=a/np.linalg.norm(a);k=np.cross(b,a);s=np.linalg.norm(k);c=b@a
 if s<1e-14:
  if c>0:return np.eye(3)
  k=np.cross(b,[1,0,0]if abs(b[0])<.8 else[0,1,0]);k/=np.linalg.norm(k);return Rotation.from_rotvec(k*np.pi).as_matrix()
 return Rotation.from_rotvec(k/s*np.arctan2(s,c)).as_matrix()
def matching(A,B,fix,mode):
 r=np.linalg.norm(A,axis=1);s=np.linalg.norm(B,axis=1)
 if mode==0:C=((A[:,None,:]-B[None,:,:])**2).sum(2)
 elif mode==1:C=((A/r[:,None])[:,None,:]-(B/s[:,None])[None,:,:])**2;C=C.sum(2)+.2*(r[:,None]-s[None,:])**2
 else:
  C=((A[:,None,:]-B[None,:,:])**2).sum(2);wa=e.numeric(A)['area'];wb=e.numeric(B)['area']
 for i,j in fix:
  C[i,:]=1e6;C[:,j]=1e6;C[i,j]=0
 rows,cols=linear_sum_assignment(C);assert np.array_equal(rows,np.arange(len(A)))
 return cols,float(C[rows,cols].sum())
def build():
 A=normalize(e.load('INPUT_A.txt'));B=normalize(e.load('INPUT_B.txt'));out=[];seen=set()
 # Both possible surviving A roots, reflections, and72 rotations around that root.
 for root in [0,40]:
  for reflect in [1,-1]:
   B0=B@np.diag([1,1,reflect]);base=align_vector(B0[6],A[root])
   for yaw in range(72):
    rot=Rotation.from_rotvec(A[root]/np.linalg.norm(A[root])*yaw*np.pi/36).as_matrix()@base
    Y=B0@rot.T
    for mode in [0,1]:
     idx,cost=matching(A,Y,[(root,6)],mode);key=(root,reflect,yaw,tuple(idx))
     if key in seen:continue
     seen.add(key);out.append(dict(root=root,reflect=reflect,yaw=yaw,mode=mode,perm=idx.tolist(),rotation=rot.tolist(),cost=cost))
 # Keep diverse rotations; no quality filtering that uses unobserved endpoint class.
 e.write('ALIGNMENTS133.json',out);e.write('NORMALIZED133.json',dict(A=A,B=B));return A,B,out

def paths(start,count,steps):
 data=json.loads((e.R/'NORMALIZED133.json').read_text());A=np.array(data['A']);B=np.array(data['B']);al=json.loads((e.R/'ALIGNMENTS133.json').read_text());records=[]
 for k in range(start,min(start+count,len(al))):
  x=al[k];Y=(B@np.diag([1,1,x['reflect']])@np.array(x['rotation']).T)[x['perm']];seq=[]
  for i in range(steps+1):
   t=i/steps;Z=(1-t)*A+t*Y;z=e.numeric(Z)
   S,U=int(z['S']),int(z['U']);margin=min(abs(z['S_guard']).min(),abs(z['U_guard'][np.isfinite(z['U_guard'])]).min())
   seq.append([i,S,U,z['V'],z['E'],float(margin)])
   if S==U==1:
    fname=f'PATH133_A{k}_T{i}D{steps}.json';print('NUMERICAL110',fname,flush=True);e.write(fname,dict(X=Z,alignment=k,t=t));
  interior=min((s[1]+s[2]for s in seq[1:-1]),default=0)
  records.append(dict(alignment=k,steps=steps,sequence=seq,min_interior=interior))
 print(e.write(f'PATHS133_{start}_{count}_{steps}.json',records),flush=True)
 print('batch',start,count,'best interior',min(z['min_interior']for z in records),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('mode',choices=['build','paths']);p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=40);p.add_argument('--steps',type=int,default=40);a=p.parse_args()
 if a.mode=='build':A,B,out=build();print('ALIGNMENTS',len(out))
 else:paths(a.start,a.count,a.steps)
```
