"""Independent exact hull and outward-rounded moment verifier; standard library.
Usage: python -B -S verify_deletions.py S8_RAW_COMPLEX CERT.json REPORT.json
A finite exclusion of deleting one or two FIXED vertices only. No motion,
metric change, projective deformation, or larger deletion set is excluded.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from functools import cmp_to_key,lru_cache
from math import gcd,lcm
import hashlib,json,sys,time
if not __debug__:raise RuntimeError('Assertions must be enabled')
sys.set_int_max_str_digits(0)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def plane(ids):
 a,b,c=[X[i]for i in ids];n=cross(sub(b,a),sub(c,a));assert n!=(0,0,0);r=(*n,dot(n,a));D=lcm(*(z.denominator for z in r));r=tuple(int(z*D)for z in r);g=gcd(*r);r=tuple(z//g for z in r)
 if r[3]<0:r=tuple(-z for z in r)
 assert r[3]>0;return r

def signs(h):
 v=[dot(h[:3],p[:3])-h[3]*p[3]for p in HOM];return frozenset(i for i,a in enumerate(v)if a>0),frozenset(i for i,a in enumerate(v)if a==0)

def polygon(h,ids):
 ids=sorted(ids);assert len(ids)>=3;drop=max(range(3),key=lambda j:abs(h[j]));ax=[j for j in range(3)if j!=drop];cen=[sum(X[i][j]for i in ids)/len(ids)for j in ax];xy={i:(X[i][ax[0]]-cen[0],X[i][ax[1]]-cen[1])for i in ids}
 def half(a):return 0 if a[1]>0 or (a[1]==0 and a[0]>0)else 1
 def cmp(i,j):
  a,b=xy[i],xy[j];d=half(a)-half(b)
  if d:return d
  c=a[0]*b[1]-a[1]*b[0];assert c!=0 if i!=j else True
  return -1 if c>0 else 1 if c<0 else 0
 cy=sorted(ids,key=cmp_to_key(cmp))
 if dot(h[:3],cross(sub(X[cy[1]],X[cy[0]]),sub(X[cy[2]],X[cy[0]])))<0:cy.reverse()
 k=cy.index(min(cy));cy=tuple(cy[k:]+cy[:k])
 for i,j in zip(cy,cy[1:]+cy[:1]):
  for k in cy:
   if k not in (i,j):assert dot(h[:3],cross(sub(X[j],X[i]),sub(X[k],X[i])))>0
 return cy

def topology(faces,keep):
 edges={};owners={i:[]for i in keep}
 for f,cy in enumerate(faces):
  assert len(cy)>=3 and len(set(cy))==len(cy)
  for i in cy:owners[i].append(f)
  for i,j in zip(cy,cy[1:]+cy[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append((f,i,j))
 assert all(len(z)==2 and z[0][1:]==z[1][1:][::-1]for z in edges.values())
 assert all(len(o)>=3 for o in owners.values());assert len(keep)-len(edges)+len(faces)==2
 seen={0};todo=[0];neighbors=[[]for f in faces]
 for z in edges.values():a,b=z[0][0],z[1][0];neighbors[a].append(b);neighbors[b].append(a)
 while todo:
  f=todo.pop()
  for g in neighbors[f]:
   if g not in seen:seen.add(g);todo.append(g)
 assert len(seen)==len(faces)
 return len(edges),owners

rawbytes=Path(sys.argv[1]).read_bytes();data=json.loads(rawbytes);certbytes=Path(sys.argv[2]).read_bytes();cert=json.loads(certbytes);assert cert['version']==1 and cert['parent_sha256']==hashlib.sha256(rawbytes).hexdigest();assert cert['precision_bits']==128
X=[tuple(map(Q,p))for p in data['vertices']];N=len(X);assert N==177 and X==sorted(set(X));HOM=[]
for p in X:
 D=lcm(*(a.denominator for a in p));HOM.append(tuple(int(a*D)for a in p)+(D,))
oldH=[];oldF=[]
for cy in data['faces']:
 h=plane(cy[:3]);pos,zero=signs(h);assert not pos and zero==set(cy);oldH.append(h);oldF.append(polygon(h,zero))
assert len(oldH)==len(set(oldH))==137
E,owners=topology(oldF,set(range(N)));assert E==312
for i,ow in owners.items():assert any(dot(oldH[a][:3],cross(oldH[b][:3],oldH[c][:3]))!=0 for a,b,c in combinations(ow,3))
# Deleting any two vertices leaves affine dimension three: certify this
# already on a small fixed subset, independently of the proposed case meshes.
anchors=(0,30,60,90,120,150,176)
for omit in combinations(anchors,2):
 rest=[i for i in anchors if i not in omit]
 assert any(dot(sub(X[b],X[a]),cross(sub(X[c],X[a]),sub(X[d],X[a])))!=0 for a,b,c,d in combinations(rest,4))
new=[];allH=set(oldH)
for tri in cert['new_planes']:
 assert len(set(tri))==3;h=plane(tri);assert h not in allH;allH.add(h);pos,zero=signs(h);assert 1<=len(pos)<=2;cy=polygon(h,zero);new.append((h,pos,zero,cy))
# Every interval is an integer pair [lo,hi]/B. Multiplication rounds outwards.
B=1<<cert['precision_bits'];Z=(0,0)
def qI(a):return(a.numerator*B//a.denominator,-((-a.numerator*B)//a.denominator))
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def minus(a,b):return(a[0]-b[1],a[1]-b[0])
def times(a,b):
 t=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]);return(min(t)//B,-((-max(t))//B))
def divint(a,n):assert n>0;return(a[0]//n,-((-a[1])//n))
def isum(xs):
 a=Z
 for x in xs:a=plus(a,x)
 return a

def icross(a,b):return(minus(times(a[1],b[2]),times(a[2],b[1])),minus(times(a[2],b[0]),times(a[0],b[2])),minus(times(a[0],b[1]),times(a[1],b[0])))
def idot(a,b):return isum(times(x,y)for x,y in zip(a,b))
XI=[tuple(map(qI,p))for p in X]
@lru_cache(None)
def moments(cy):
 if len(cy)<3:return (Z,Z,Z,Z)
 ans=[Z,Z,Z,Z]
 for j in range(1,len(cy)-1):
  a,b,c=[XI[k]for k in (cy[0],cy[j],cy[j+1])];d=idot(a,icross(b,c));ans[0]=plus(ans[0],divint(d,6))
  for k in range(3):ans[k+1]=plus(ans[k+1],divint(times(d,plus(plus(a[k],b[k]),c[k])),24))
 return tuple(ans)
base=tuple(isum(moments(cy)[k]for cy in oldF)for k in range(4));assert base[0][0]>0
DIF=[[tuple(minus(a,b)for a,b in zip(XI[j],XI[i]))for j in range(N)]for i in range(N)]
K=[[idot(XI[i],DIF[i][j])for j in range(N)]for i in range(N)]
expected=[(i,)for i in range(N)]+list(combinations(range(N),2));assert len(cert['cases'])==len(expected)
small=0;above=0;byC={};minmargin=None;worst=None;beg=time.monotonic();used=set()
for serial,((deleted,extra,witness),want)in enumerate(zip(cert['cases'],expected)):
 assert tuple(deleted)==want and len(extra)==len(set(extra));ds=set(deleted);keep=set(range(N))-ds;faces=[];mo=list(base)
 for f,cy in enumerate(oldF):
  nc=tuple(i for i in cy if i not in ds)
  if len(nc)>=3:faces.append(nc)
  if nc!=cy:
   a,b=moments(nc),moments(cy)
   for k in range(4):mo[k]=plus(mo[k],minus(a[k],b[k]))
 for e in extra:
  used.add(e);h,pos,zero,cy=new[e];assert pos<=ds;nc=tuple(i for i in cy if i not in ds);assert set(nc)==zero-ds and len(nc)>=3;faces.append(nc)
  a=moments(nc)
  for k in range(4):mo[k]=plus(mo[k],a[k])
 edgecount,_=topology(faces,keep);C=2*edgecount;byC[C]=byC.get(C,0)+1;assert mo[0][0]>0
 if C>=624:above+=1;assert not witness;continue
 small+=1;assert len(set(witness))==2 and set(witness)<=keep
 for i in witness:
  for j in keep-{i}:
   # Exact expression V*x_i.(x_j-x_i)-M.(x_j-x_i) is strictly negative.
   iv=minus(times(mo[0],K[i][j]),idot(mo[1:],DIF[i][j]));assert iv[1]<0,('U check failed',deleted,i,j,iv)
   if minmargin is None or -iv[1]<minmargin:minmargin=-iv[1];worst=[deleted,i,j]
 if serial%1000==0:print('VERIFIED',serial,small,round(time.monotonic()-beg,2),flush=True)
assert used==set(range(len(new)))
report=dict(status='ALL_FIXED_S8_ONE_TWO_VERTEX_DELETIONS_C_LT_624_EXCLUDED',total=len(expected),under_budget=small,at_or_above_budget=above,complexity_histogram=byC,new_plane_count=len(new),strict_U_witnesses_per_under_budget_case=2,precision_bits=128,minimum_negative_numerator_bound=[str(minmargin),str(B)],tightest_witness=worst,parent_sha256=hashlib.sha256(rawbytes).hexdigest(),certificate_sha256=hashlib.sha256(certbytes).hexdigest(),scope='Only exact fixed S8 coordinates with one or two original raw-lex vertices deleted. No moving-coordinate, affine, projective or larger-subset exclusion.')
b=canonical(report);Path(sys.argv[3]).write_bytes(b);print(report['status'],len(b),hashlib.sha256(b).hexdigest(),flush=True)
