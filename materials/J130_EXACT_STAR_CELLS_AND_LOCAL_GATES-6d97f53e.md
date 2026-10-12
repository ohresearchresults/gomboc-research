# material-6d97f53e2309

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# J130 exact star cells and local gates — complete standalone recovery

This is new coordinator research on the literal KF27I DETACHED_G6 input, obtained completely from [internal-source-reference] (SHA25695de5a8f64bdf3150125bc2fbccfdf66b1c2ebaad79a2f740cab16639642deaf). No worker workspace, C622 source, optimizer or earlier capsule is needed to reproduce these exact results. This material contains every required literal file. The numerical nomination methods are separately preserved; the frozen inputs here are sufficient to reconstruct both exact bodies and all certificates.

## Findings and limits

Two new distinct rational bodies have true V47/E135/F90,C270, own strict211, additionalweak000 and endpoint primitivezero000. Both have S triangles[5,38,45] and[5,46,34], U6, H43--44 and P[]. J130_EXACT_STAR47 has Q approximately.46086304181486154 and EXACTLY the parent's volume, first moment and centroid. Its eleven moved independent vertices are[38,42,21,11,22,28,30,40,16,12,46]. Every intermediate point of the whole affine segment has the same physical mass data, the same triangular incidence and own211/additionalweak000, certified by3960 exact all-point/face inequalities and exact quadratic extrema for a complete physical forest and every stable-face escape. Primitive zeros are NOT excluded at every intermediate parameter. J130_ADAPTIVE47_G10 is a separately rounded finite continuation with Q approximately.45705261300095035; its actual centroid is approximately(-9.67727211069674e-12,1.3614763927374472e-11,1.3319467070632891e-11), NOT exactly zero. No body is110. Coordinate fraction numerator/denominator maximum bits are604/606 for the exact star body and33/34 for the G10 body; centroid denominator maxima83 and137 respectively.

For an independent set of moving vertices, every triangle has at most one moving vertex. At star i with oriented incident faces(i,a,b), define K_i=sum(a cross b) and D_i=[sum det(p_i,a,b)]I+sum(a+b)(a cross b)^T. A displacement d_i changes its volume by K_i.d_i/6. Under K_i.d_i=0, its first-moment change is D_i d_i/24. Thus all star-volume planes plus sum D_i d_i=0 give a linear exact mass-neutral space of finite motions, not merely an infinitesimal nullspace. A selected physical exclusion p_i.(p_i-p_j)<0 is convex quadratic or affine when moving vertices are independent. For an oriented triangle(a,b,c), n=(b-a) cross(c-a), the stable-foot edge sign is n.(a cross b); it is at most quadratic, and affine when the moving vertex is opposite that edge. Hull signs are at most quadratic. Any symmetric quadratic Q may be upper-majorized by Q_+ or a certified rational PSD majorant, creating a convex INNER joint physical/polar/hull cell in the mass-neutral plane. This does not make the union of cells convex. The execution used floating spectral matrices only to nominate a step; the final exact segment certificate uses direct rational polynomial extrema, not floating spectral claims.

Six exact local inequalities explain limitations of chosen opposite-edge routes. Three zero-star-volume lower bounds for drivers5,38,45 are approximately.0031961252654800474,.012922971020866675,.00013054218194771878. More strongly, selected fixed-neighbor/physical-witness constraints imply positive lower bounds.0010139162155150842,.011499358683598233,.00009812774817843247 WITHOUT any local or global volume/moment restriction. These are raw oriented edge signs, not normalized persistence. They forbid only the indicated opposite-edge crossing at the FIXED parent centroid and named retained coordinates/planes/witnesses. They do NOT exclude cancellation via another edge, changed carrier geometry, changed witness, moving centre, or an arbitrary whole basin. The driver38 free-volume gate uses only convexity and its fixed neighbors plus root6. The source prints all exact coefficients, fixed labels and nonnegative dual multipliers. General volume exchange still gives affine endpoint mass closure for prescribed changes tau_i: K_i.d_i=6 tau_i and sum[(D_i+6 tau_i I)d_i+6 tau_i p_i]=0 with sum tau_i=0. An entire segment also needs sum tau_i d_i=0. These formulas do not certify feasibility of a selected exchange.

## Reconstruction and exact verification

Save the four fenced units under their literal filenames with one terminal newline. Execute:

OPENBLAS_NUM_THREADS=1 python exact130.py
OPENBLAS_NUM_THREADS=1 python gates130.py

Environment used: Python3.13.5, NumPy2.3.5, SciPy1.17.0. fractions.Fraction supplies exact arithmetic. Qhull only nominates triangles; every supporting sign, closed connected incidence, mass value, equilibrium and certificate comparison is rational. This is one newly authored exact producer/auditor, not a claim of two independent engines.

Input/source manifest:
- DETACHED_G6.txt1034B SHAa5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50
- NOMINATION130.json2386B SHA978b92df6b6b613f551b43a111868cccfcdc4ebfad7f7906aece0c61c55ea313
- exact130.py11014B SHAde17c6a60523a72cb46b889c4b2429d95e1ba50938df0c69f410f63150e9a9b5
- gates130.py3648B SHA5173483352541c6f1840824608de43bad655bd4e608f2146e2c4c825bc1d202a

Expected reproduced outputs:
- J130_EXACT_STAR47.json14283B SHA1f97fa6b2f1c9f07dd29720cc969fe6453535e0cfca5ff14e557d5334ab24f70
- J130_ADAPTIVE47_G10.json6349B SHAceb70d284a1785416c212a74959138ae193abd22522e09667b0ed1cdf1c3c232
- J130_EXACT_REPORT.json11043B SHA308da40033bb92b2ad8a7ee34a58ca45918159b53cf98a168f92476d5a26a73e
- J130_GATES_REPORT.json15413B SHAac1fbd153943bf061922c5bc218c1ab2920a548c7ba6ab534a04d72c16aeed88

Expected terminal markers include EXACT_STAR47 [2,1,1] COMMON_VOLUME_MOMENT_CENTROID; EXACT_ENTIRE_SEGMENT [2,1,1]3960 ADDITIONAL_WEAK000; EXACT_ADAPTIVE47_G10 [2,1,1]; J130_EXACT_PASS; six EXACT_LOCAL_GATE lines; J130_GATES_PASS.

## File: DETACHED_G6.txt
```text
47 1000000
-220660 -170809 739992
-470733 -252568 617724
-344429 -201140 695040
-827617 -345105 -7630
-804956 -306141 -196980
-617752 -310722 484546
-802871 -391980 208231
708441 212327 -26773
629324 353053 -32544
109721 -76616 760640
306556 -32243 700380
212446 -60072 735986
469379 -34257 598089
392685 -40271 652622
646907 -14969 394808
537342 -31849 536185
596588 -24705 468240
750839 45997 64966
-102855 -139962 763378
7557 -112190 768796
719082 11448 235222
687865 -2839 316832
740239 27161 150766
750330 69885 -21314
738230 84890 -114933
592447 240452 -366643
659702 196951 -280592
707333 140337 -199650
700973 -34829 -222306
-736323 -274563 -374807
228858 452552 -370941
60624 561672 -200802
142319 490402 -325534
566004 -68026 -372688
612214 -197888 -188679
464617 500011 -71398
-487325 -442504 -463527
552036 118367 -435356
-19326 554813 -63048
350712 442484 -390884
577522 340656 -272794
199735 530859 -305689
-532859 -303654 -567337
-484871 -149126 -645284
472985 292300 -459118
-416022 64364 111262
-193306 -303834 71494
```

## File: NOMINATION130.json
```json
{"star_step":{"selected":[38,42,21,11,22,28,30,40,16,12,46],"pivot_columns":[31,1,12,6,5,15,20,24,10,22,28,2,0,29],"free_columns":[3,4,7,8,9,11,13,14,16,17,18,19,21,23,25,26,27,30,32],"denominator":1000000000000,"scale":"19/20","free_numerators":[20087755701,47226930002,1667036763,6778883501,6267866132,-2475369599,-238511573,7071674500,2068275773,-903751932,31335065348,31169090785,-17134703423,1909301395,1791747927,6256896520,-2658556288,188488692402,-54085190936],"originating_nomination":"RUN_38_0_0p25; fixed-margins version, driver38 seed0 trust.25"},"adaptive_grid":{"denominator":10000000000,"numerators":[[-2371507882,-1796400922,7741910044],[-4875499007,-2615209378,6518774053],[-3587591806,-2091016249,7301661657],[-8451618750,-3554390412,255438939],[-8236890498,-3174562381,-1582367516],[-6373926935,-3192079081,5166655838],[-8196879007,-4009329378,2423844053],[6960125050,1955013544,-72980313],[6125070993,3441000622,16094053],[929002673,-855702179,7947946023],[2897390993,-411959378,7345334053],[2019259471,-682917097,7676524955],[4569080224,-434918899,6282307438],[3758677473,-492243456,6867749075],[6227703085,-200138000,4427446283],[5205368232,-408391453,5703478268],[5772417374,-324380529,5062252666],[7340220993,370440622,991194053],[-1193913746,-1488470214,7975649535],[-77403739,-1209505261,8027507581],[7022080789,54224928,2693159182],[6682844965,-100257276,3580796484],[7224641470,179707899,1918448802],[7336959421,623448554,161302236],[7214778810,756719526,-806007255],[5756300993,2314990622,-3324895947],[6422699249,1902537121,-2459465087],[6905161742,1313838383,-1654965202],[6842803143,-414365474,-1893388661],[-7520640040,-2830184386,-3422826808],[2436166522,4746676209,-3213197654],[437628974,5526915992,-1666713450],[1440668842,5202726084,-2634566374],[5615637768,-612331715,-3439100758],[5953970993,-2068409378,-1545255947],[4537813298,4886523941,-364940436],[-5041419007,-4514569378,-4293735947],[5351766413,1093961713,-4012176079],[-429662931,5401401312,-239306282],[3509898238,4249866019,-3603042841],[5435703959,3491811056,-2367312933],[2139704570,5096584477,-2881442634],[-5295490024,-2652878571,-5605286451],[-5016879007,-1580789378,-6111305947],[4631180848,2774881846,-4250533417],[-2758179281,2482492504,847657386],[-1420125134,-3310591667,-800787526]],"originating_nomination":"RUN_38_0_0p25 then current guarded adaptive rounds0..5; BEST_5"}}
```

## File: exact130.py
```python
#!/usr/bin/env python3
"""J130 exact finite independent-star deformation and whole-segment certificate.
Reconstructs from DETACHED_G6.txt and NOMINATION130.json only.
Qhull nominates oriented triangular hull facets; ALL supporting/incidence signs,
volume, moments, equilibria and segment extrema are rationally checked.
Python3.13.5 NumPy2.3.5 SciPy1.17.0; fractions.Fraction is the exact engine.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
import numpy as np
from scipy.spatial import ConvexHull
R=Path(__file__).resolve().parent
ZERO=F(0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),ZERO)
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def convert(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return{str(k):convert(v)for k,v in x.items()}
 if isinstance(x,(list,tuple)):return[convert(v)for v in x]
 if isinstance(x,np.integer):return int(x)
 return x

def write(name,x):
 b=(json.dumps(convert(x),indent=2)+'\n').encode();(R/name).write_bytes(b)
 return dict(name=name,bytes=len(b),sha256=sha256(b).hexdigest())

def hull(X):
 h=ConvexHull(np.array([[float(x)for x in p]for p in X]));fs=[];hs=[]
 for tt in h.simplices:
  t=list(map(int,tt));a,b,c=[X[i]for i in t];n=cross(sub(b,a),sub(c,a));hh=dot(n,a);s=[dot(n,x)-hh for x in X]
  if max(s)>0:
   assert min(s)>=0,'Numerical facet not exactly supporting'
   t[1],t[2]=t[2],t[1]
  # Canonical orientation: smallest vertex first, outward cyclic order.
  j=t.index(min(t));t=t[j:]+t[:j];fs.append(tuple(t))
 fs=sorted(fs);assert len(set(fs))==len(fs)
 es={}
 for fi,t in enumerate(fs):
  a,b,c=[X[i]for i in t];n=cross(sub(b,a),sub(c,a));hh=dot(n,a);s=[dot(n,x)-hh for x in X]
  assert max(s)==0 and sum(v==0 for v in s)==3,'Not a strict triangle hull'
  hs.append((n,hh))
  for j in range(3):es.setdefault(tuple(sorted((t[j],t[(j+1)%3]))),[]).append(fi)
 assert all(len(v)==2 for v in es.values())
 vs=sorted(set(i for t in fs for i in t));assert len(vs)-len(es)+len(fs)==2
 todo=[0];seen={0}
 while todo:
  i=todo.pop();t=fs[i]
  for j in range(3):
   for k in es[tuple(sorted((t[j],t[(j+1)%3])))]:
    if k not in seen:seen.add(k);todo.append(k)
 assert len(seen)==len(fs)
 # Supporting triangles constitute a connected closed full boundary, not a subset.
 return fs,hs,dict(sorted(es.items())),vs

def mass(X,fs):
 v=ZERO;m=(ZERO,ZERO,ZERO)
 for a,b,c in fs:
  d=det(X[a],X[b],X[c]);v+=d/6;m=add(m,mul(d/24,add(add(X[a],X[b]),X[c])))
 assert v>0
 return v,m,mul(1/v,m)

def persistence(P,es):
 rad=[dot(p,p)for p in P];par=list(range(len(P)));peak=rad[:];links=[];out=[]
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for i,j in es:
  d=sub(P[j],P[i]);tt=max(ZERO,min(F(1),-dot(P[i],d)/dot(d,d)));p=add(P[i],mul(tt,d));links.append((dot(p,p),i,j))
 for level,i,j in sorted(links,reverse=True):
  a,b=root(i),root(j)
  if a==b:continue
  if peak[a]<peak[b]:a,b=b,a
  depth=1-level/peak[b];assert depth>=0
  if depth>0:out.append(depth)
  par[b]=a
 return sorted(out,reverse=True)

def audit(X):
 fs,hs,es,vs=hull(X);v,m,g=mass(X,fs);Y=[sub(x,g)for x in X]
 S=[];U=[];H=[];weak=[[],[],[]];zeros=[0,0,0]
 for fi,(t,(n,hh))in enumerate(zip(fs,hs)):
  assert hh-dot(n,g)>0
  signs=[dot(n,cross(Y[t[j]],Y[t[(j+1)%3]]))for j in range(3)]
  zeros[0]+=sum(s==0 for s in signs)
  if min(signs)>0:S.append(fi)
  elif min(signs)>=0:weak[0].append(fi)
 neigh=[[]for _ in X]
 for i,j in es:neigh[i].append(j);neigh[j].append(i)
 for i in vs:
  signs=[dot(Y[i],sub(Y[j],Y[i]))for j in neigh[i]];zeros[1]+=sum(s==0 for s in signs)
  if max(signs)<0:U.append(i)
  elif max(signs)<=0:weak[1].append(i)
 for (i,j),(a,b)in es.items():
  d=sub(Y[j],Y[i]);dd=dot(d,d);aa=-dot(Y[i],d);bb=dd-aa;p=add(Y[i],mul(aa/dd,d))
  n1,n2=hs[a][0],hs[b][0];g11,g12,g22=dot(n1,n1),dot(n1,n2),dot(n2,n2);D=g11*g22-g12*g12;assert D>0
  c1=dot(p,n1)*g22-dot(p,n2)*g12;c2=dot(p,n2)*g11-dot(p,n1)*g12
  assert mul(D,p)==add(mul(c1,n1),mul(c2,n2))
  signs=[aa,bb,c1,c2];zeros[2]+=sum(s==0 for s in signs)
  if min(signs)>0:H.append((i,j))
  elif min(signs)>=0:weak[2].append((i,j))
 assert len(S)+len(U)-len(H)==2
 P=persistence(Y,list(es));Q=persistence([mul(1/(hh-dot(n,g)),n)for n,hh in hs],list(es.values()))
 assert len(P)==len(U)-1 and len(Q)==len(S)-1
 return dict(V=len(vs),E=len(es),F=len(fs),strict=[len(S),len(U),len(H)],weak=list(map(len,weak)),primitive_zero=zeros,S=[fs[i]for i in S],U=U,H=H,P=P,Q=Q,volume=v,moment=m,centroid=g),fs

def solve(A,b):
 n=len(A);a=[list(r)+[z]for r,z in zip(A,b)]
 for j in range(n):
  k=next(k for k in range(j,n)if a[k][j]);a[j],a[k]=a[k],a[j];z=a[j][j];a[j]=[v/z for v in a[j]]
  for k in range(n):
   if k==j:continue
   z=a[k][j]
   if z:a[k]=[x-z*y for x,y in zip(a[k],a[j])]
 return [a[k][-1]for k in range(n)]

def constraints(X,fs,ids):
 k=len(ids);C=[[ZERO]*(3*k)for _ in range(k+3)]
 for j,i in enumerate(ids):
  K=(ZERO,ZERO,ZERO);D=[[ZERO]*3 for _ in range(3)];dd=ZERO
  for t in fs:
   if i not in t:continue
   a=t.index(i);u,w=X[t[(a+1)%3]],X[t[(a+2)%3]];cc=cross(u,w);K=add(K,cc);dd+=dot(X[i],cc)
   for r in range(3):
    for c in range(3):D[r][c]+=(u[r]+w[r])*cc[c]
  for c in range(3):C[j][3*j+c]=K[c]
  for r in range(3):
   for c in range(3):C[k+r][3*j+c]=D[r][c]+(dd if r==c else 0)
 assert all(sum(i in t for i in ids)<=1 for t in fs),'Moving vertices are not independent'
 return C

def projected(X,fs,data):
 ids=data['selected'];C=constraints(X,fs,ids);piv=data['pivot_columns'];free=data['free_columns'];n=len(C)
 assert len(piv)==n and sorted(piv+free)==list(range(3*len(ids)))
 d=[ZERO]*(3*len(ids));den=data['denominator'];scale=F(data['scale'])
 for c,num in zip(free,data['free_numerators']):d[c]=F(num,den)*scale
 b=[-sum((r[c]*d[c]for c in free),ZERO)for r in C]
 sol=solve([[r[c]for c in piv]for r in C],b)
 for c,z in zip(piv,sol):d[c]=z
 assert all(dot(r,d)==0 for r in C)
 out=X[:]
 for j,i in enumerate(ids):out[i]=add(X[i],tuple(d[3*j:3*j+3]))
 return out

# A polynomial along a one-dimensional segment is reconstructed at 0,1,1/2.
# All uses below have degree <=2 by the independent-star hypothesis.
def coeff(values):
 c,y,m=values;a=2*(y+c-2*m);b=y-c-a;return c,b,a

def extrema(q):
 c,b,a=q;ts=[ZERO,F(1)]
 if a and 0<-b/(2*a)<1:ts.append(-b/(2*a))
 vals=[c+b*t+a*t*t for t in ts];return min(vals),max(vals)

def segment_certificate(X,Y,fs,g,ids):
 D=[sub(y,x)for x,y in zip(X,Y)];Xs=[[sub(add(x,mul(t,d)),g)for x,d in zip(X,D)]for t in [ZERO,F(1),F(1,2)]]
 planes=[]
 for XX in Xs:planes.append([(cross(sub(XX[b],XX[a]),sub(XX[c],XX[a])),XX[a])for a,b,c in fs])
 hull_margin=None;allhull=0
 for fi,t in enumerate(fs):
  for j in range(len(X)):
   if j in t:continue
   q=coeff([dot(planes[k][fi][0],sub(Xs[k][j],planes[k][fi][1]))for k in range(3)]);lo,hi=extrema(q);assert hi<0,('hull',fi,j,q)
   hull_margin=-hi if hull_margin is None else min(hull_margin,-hi);allhull+=1
 es=set()
 for t in fs:
  for j in range(3):es.add(tuple(sorted((t[j],t[(j+1)%3]))))
 neigh=[[]for _ in X]
 for a,b in es:neigh[a].append(b);neigh[b].append(a)
 roots=[];forest=[];umin=None
 for i in range(len(X)):
  initial=[(dot(Xs[0][i],sub(Xs[0][j],Xs[0][i])),j)for j in neigh[i]]
  best,j=max(initial)
  if best<0:
   roots.append(i)
   for jj in neigh[i]:
    hi=extrema(coeff([dot(XX[i],sub(XX[jj],XX[i]))for XX in Xs]))[1];assert hi<0
   continue
  q=coeff([dot(XX[i],sub(XX[j],XX[i]))for XX in Xs]);lo,hi=extrema(q);assert lo>0,('U',i,j)
  forest.append([i,j]);umin=lo if umin is None else min(umin,lo)
 assert len(roots)==1
 stable=[];escapes=[];smin=None
 for fi,t in enumerate(fs):
  qs=[coeff([dot(planes[k][fi][0],cross(Xs[k][t[j]],Xs[k][t[(j+1)%3]]))for k in range(3)])for j in range(3)]
  initial=[q[0]for q in qs]
  if min(initial)>0:
   assert all(extrema(q)[0]>0 for q in qs),('S retention',fi)
   stable.append(t)
  else:
   j=min(range(3),key=lambda j:initial[j]);hi=extrema(qs[j])[1];assert hi<0,('S escape',fi,j,hi)
   escapes.append([fi,j]);smin=-hi if smin is None else min(smin,-hi)
 assert len(stable)==2
 # In each edge's closed equilibrium conditions, a zero at an endpoint entails
 # a closed nonstrict U there; a zero cone coefficient entails a closed nonstrict
 # S on an incident facet. The strict root/escape certificates above exclude
 # both. Consequently no additional weak edge equilibrium exists along this
 # convex, fixed-incidence segment. Strict saddle count is then S+U-2=1.
 return dict(independent_vertices=ids,hull_comparisons=allhull,hull_min_raw_margin=hull_margin,physical_forest=forest,U_root=roots[0],physical_min_raw_margin=umin,S_roots=stable,stable_escape_edges=escapes,stable_escape_min_raw_margin=smin,whole_segment_strict=[2,1,1],whole_segment_additionalweak=[0,0,0],scope='Exact entire t in [0,1], fixed triangular incidence, common actual centroid; no primitive-zero-free claim for every t.')

def main():
 b=(R/'DETACHED_G6.txt').read_bytes();assert len(b)==1034 and sha256(b).hexdigest()=='a5b7cb7cd10de4a8ba08a997945ee3a932385cf03a5e259946be867954772a50'
 w=list(map(int,b.split()));N,D=w[:2];X=[tuple(F(t,D)for t in w[2+3*i:5+3*i])for i in range(N)]
 data=json.loads((R/'NOMINATION130.json').read_text());parent,fs=audit(X)
 Y=projected(X,fs,data['star_step']);endpoint,ys=audit(Y)
 assert parent['strict']==endpoint['strict']==[2,1,1] and parent['weak']==endpoint['weak']==[0,0,0]
 assert fs==ys and all(parent[k]==endpoint[k]for k in ['volume','moment','centroid'])
 cert=segment_certificate(X,Y,fs,parent['centroid'],data['star_step']['selected'])
 # Check actual common mass again at rational interior point without relying on endpoints.
 mid=[mul(F(1,2),add(x,y))for x,y in zip(X,Y)]
 assert mass(mid,fs)==(parent['volume'],parent['moment'],parent['centroid'])
 body=write('J130_EXACT_STAR47.json',dict(vertices=Y,audit=endpoint,segment_certificate=cert))
 frozen=data['adaptive_grid'];Z=[tuple(F(t,frozen['denominator'])for t in p)for p in frozen['numerators']];grid,gs=audit(Z)
 assert grid['strict']==[2,1,1] and grid['weak']==[0,0,0]
 coarse=write('J130_ADAPTIVE47_G10.json',dict(vertices=Z,audit=grid))
 report=dict(parent=parent,exact_star_endpoint=endpoint,exact_segment=cert,adaptive_grid=grid,outputs=[body,coarse],evidence='New exact producer/auditor, not a second independent verification of worker results. The numerical spectral/SLSQP process nominates inputs only.')
 receipt=write('J130_EXACT_REPORT.json',report)
 print('EXACT_STAR47',endpoint['strict'],[float(q)for q in endpoint['Q']],'COMMON_VOLUME_MOMENT_CENTROID',flush=True)
 print('EXACT_ENTIRE_SEGMENT',cert['whole_segment_strict'],cert['hull_comparisons'],'ADDITIONAL_WEAK000',flush=True)
 print('EXACT_ADAPTIVE47_G10',grid['strict'],[float(q)for q in grid['Q']],flush=True)
 print('J130_EXACT_PASS',json.dumps(receipt),flush=True)
if __name__=='__main__':main()
```

## File: gates130.py
```python
#!/usr/bin/env python3
"""Six exact local opposite-edge gates on DETACHED47, fixed actual centre.
Three require fixed local star volume; three stronger selected local gates
require no volume or moment restriction at all. These are NOT whole-S or
whole-body exclusions. Named neighboring coordinates/planes and the specified
physical witness must remain; joint carrier motion and new witnesses escape.
Depends only on exact130.py and its literal DETACHED_G6.txt input.
"""
from fractions import Fraction as F
import exact130 as e

SPECS={
 (5,'zero_star_volume'):[['hull',[1,5,34],46],['U',1,5]],
 (38,'zero_star_volume'):[['hull',[3,6,45],38],['U',38,31]],
 (45,'zero_star_volume'):[['hull',[1,38,5],45],['U',45,6]],
 (5,'free_volume'):[['hull',[3,6,45],5],['hull',[5,6,46],36],['U',1,5]],
 (38,'free_volume'):[['hull',[3,6,45],38],['hull',[9,10,38],35],['hull',[9,38,19],18]],
 (45,'free_volume'):[['hull',[1,38,5],45],['hull',[3,6,45],38],['U',45,6]]}

def main():
 w=list(map(int,(e.R/'DETACHED_G6.txt').read_bytes().split()));N,D=w[:2];raw=[tuple(F(t,D)for t in w[2+3*i:5+3*i])for i in range(N)]
 fs,hs,es,vs=e.hull(raw);V,M,g=e.mass(raw,fs);X=[e.sub(x,g)for x in raw];out=[]
 tri=next(t for t in fs if set(t)=={5,38,45})
 def shifted(driver,j):
  Y=X[:];p=list(Y[driver]);p[j]+=1;Y[driver]=tuple(p);return Y
 for (driver,kind),specs in SPECS.items():
  edge=next((tri[j],tri[(j+1)%3])for j in range(3)if driver not in(tri[j],tri[(j+1)%3]))
  def target(Y):
   a,b,c=[Y[i]for i in tri];return e.dot(e.cross(e.sub(b,a),e.sub(c,a)),e.cross(Y[edge[0]],Y[edge[1]]))
  c0=target(X);o=tuple(target(shifted(driver,j))-c0 for j in range(3));rows=[];bounds=[];fixed=set(tri)-{driver};policies=[]
  for sp in specs:
   if sp[0]=='hull':
    t,j=sp[1:];assert tuple(t)in fs
    def f(Y,t=t,j=j):
     a,b,c=[Y[i]for i in t];return e.dot(e.cross(e.sub(b,a),e.sub(c,a)),e.sub(Y[j],a))
    cc=f(X);a=tuple(f(shifted(driver,k))-cc for k in range(3));fixed|=(set(t)|{j})-{driver};policies.append(sp)
   else:
    i,j=sp[1:];cc=e.dot(X[i],e.sub(X[i],X[j]));assert cc<0
    if driver==i:a=e.sub(e.mul(F(2),X[i]),X[j]);remainder='|d|^2 >= 0'
    elif driver==j:a=e.mul(-1,X[i]);remainder='0'
    else:raise AssertionError('Witness does not involve driver')
    fixed|={i,j}-{driver};policies.append(dict(identity=sp,nonnegative_remainder=remainder))
   assert cc<0;rows.append(a);bounds.append(-cc)
  if kind=='zero_star_volume':
   K=(F(0),F(0),F(0));neighbors=set()
   for t in fs:
    if driver not in t:continue
    j=t.index(driver);a,b=t[(j+1)%3],t[(j+2)%3];K=e.add(K,e.cross(X[a],X[b]));neighbors|={a,b}
   fixed|=neighbors;rows.append(K);bounds.append(F(0))
  # o + sum(lambda_i a_i) = 0. Closed necessary inequalities give the bound;
  # strict valid geometry can only improve it. Equality multiplier is free.
  lam=e.solve([[rows[j][i]for j in range(3)]for i in range(3)],[-x for x in o])
  count=2 if kind=='zero_star_volume' else 3
  assert all(x>=0 for x in lam[:count])
  assert all(o[i]+sum(lam[j]*rows[j][i]for j in range(3))==0 for i in range(3))
  bd=c0-sum(lam[j]*bounds[j]for j in range(3));assert bd>0
  cert=dict(driver=driver,kind=kind,target_triangle=tri,opposite_edge=edge,fixed_coordinate_labels=sorted(fixed),fixed_centre=g,policies=policies,objective_constant=c0,objective_gradient=o,rows=rows,bounds=bounds,multipliers=lam,strict_positive_lower_bound=bd)
  if kind=='zero_star_volume':cert['volume_exchange_threshold']=bd/(6*lam[-1])
  out.append(cert);print('EXACT_LOCAL_GATE',driver,kind,float(bd),flush=True)
 receipt=e.write('J130_GATES_REPORT.json',out);print('J130_GATES_PASS',receipt,flush=True)
if __name__=='__main__':main()
```
