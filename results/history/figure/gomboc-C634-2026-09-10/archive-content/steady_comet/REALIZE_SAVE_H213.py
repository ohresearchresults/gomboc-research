from fractions import Fraction as F
from pathlib import Path
import hashlib,json,collections,sys
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent;N=137
H=[tuple(map(int,l.split())) for l in (ROOT/'H213_edges.txt').read_text().splitlines()]
rot={}
for line in (ROOT/'H213_rotation.txt').read_text().splitlines():
 i,s=line.split(':',1);rot[int(i)]=[int(x) for x in s.strip().split(',')]
seen=set();faces=[];dface={}
for u,v in sorted((u,v) for a,b in H for u,v in ((a,b),(b,a))):
 if (u,v) in seen: continue
 cyc=[];a,b=u,v;fid=len(faces)
 while (a,b) not in seen:
  seen.add((a,b));dface[(a,b)]=fid;cyc.append(a)
  rr=rot[b];k=rr.index(a);c=rr[(k-1)%len(rr)];a,b=b,c
 faces.append(cyc)
assert len(faces)==78 and len(seen)==426
xy={}
for line in (ROOT/'H213_tutte_xy_exact.txt').read_text().splitlines():
 v,x,y=line.split();xy[int(v)]=(F(x),F(y))
stress={e:F(1) for e in H}
stress[(1,6)]=F(-3975020208044236037132700849064167748613055,7409136625438368337108070963931321725078284)
stress[(1,11)]=F(-33678230867548844273631982400919490673199,1058448089348338333872581566275903103582612)
stress[(6,11)]=F(-320628155822873462371534760805344222354643,2116896178696676667745163132551806207165224)
outer_f=next(i for i,c in enumerate(faces) if set(c)=={1,6,11} and len(c)==3)
fadj=collections.defaultdict(list)
for u,v in H:
 a=dface[(u,v)];b=dface[(v,u)];fadj[a].append((b,u,v));fadj[b].append((a,v,u))
planes={outer_f:((F(0),F(0)),F(0))};dq=collections.deque([outer_f])
while dq:
 f=dq.popleft();(gx,gy),cc=planes[f]
 for g,u,v in fadj[f]:
  if g in planes: continue
  dx=xy[v][0]-xy[u][0];dy=xy[v][1]-xy[u][1];w=stress[tuple(sorted((u,v)))]
  dg=(-w*dy,w*dx);planes[g]=((gx+dg[0],gy+dg[1]),cc-dg[0]*xy[u][0]-dg[1]*xy[u][1]);dq.append(g)
assert len(planes)==78
for u,v in H:
 a=dface[(u,v)];b=dface[(v,u)]
 for t in (u,v):
  vals=[]
  for f in (a,b):
   (gx,gy),cc=planes[f];vals.append(gx*xy[t][0]+gy*xy[t][1]+cc)
  assert vals[0]==vals[1]
Q=[]
for v in range(N):
 vals=[]
 for f,c in enumerate(faces):
  if v in c:
   (gx,gy),cc=planes[f];vals.append(gx*xy[v][0]+gy*xy[v][1]+cc)
 assert vals and all(z==vals[0] for z in vals);Q.append((xy[v][0],xy[v][1],vals[0]))
s=tuple(sum(q[k] for q in Q)/N for k in range(3));q=[tuple(Q[i][k]-s[k] for k in range(3)) for i in range(N)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a,b,c):return dot(a,cross(b,c))
def solve3(A):
 d=det3(A[0],A[1],A[2]);assert d
 num=add(add(cross(A[1],A[2]),cross(A[2],A[0])),cross(A[0],A[1]));return mul(num,F(1,d))
P=[]
for cyc in faces:
 tri=None
 for i in range(len(cyc)-2):
  for j in range(i+1,len(cyc)-1):
   for k in range(j+1,len(cyc)):
    if det3(q[cyc[i]],q[cyc[j]],q[cyc[k]])!=0:tri=(cyc[i],cyc[j],cyc[k]);break
   if tri:break
  if tri:break
 p=solve3([q[i] for i in tri]);assert all(dot(q[i],p)==1 for i in cyc);P.append(p)
min_gap=None
for f,cyc in enumerate(faces):
 inc=set(cyc)
 for i in range(N):
  z=1-dot(q[i],P[f])
  if i in inc:assert z==0
  else:assert z>0;min_gap=z if min_gap is None or z<min_gap else min_gap
inc_faces=[]
for i in range(N):
 cyc=[dface[(i,j)] for j in rot[i]]
 if len(cyc)>=3:
  a,b,c=P[cyc[0]],P[cyc[1]],P[cyc[2]]
  if dot(cross(sub(b,a),sub(c,a)),q[i])<0:cyc=list(reversed(cyc))
 inc_faces.append(cyc)

def enc(o):
 if isinstance(o,F):return str(o)
 if isinstance(o,(list,tuple)):return [enc(z) for z in o]
 if isinstance(o,dict):return {str(k):enc(v) for k,v in o.items()}
 return o
(ROOT/'H213_geometry.json').write_text(json.dumps(enc(dict(Q=q,P=P,faces=faces,primal_faces=inc_faces)),sort_keys=True,separators=(',',':')))
print('H213_EXACT_GEOMETRY_SAVED',flush=True)
V=F(0);M=[F(0),F(0),F(0)];tri_count=0
for cyc in inc_faces:
 a=P[cyc[0]]
 for k in range(1,len(cyc)-1):
  b=P[cyc[k]];c=P[cyc[k+1]];d=det3(a,b,c);assert d>0;V+=d/F(6);tri_count+=1
  for j in range(3):M[j]+=d*(a[j]+b[j]+c[j])/F(24)
cent=tuple(x/V for x in M);X=[sub(p,cent) for p in P]
h=[F(1)-dot(qi,cent) for qi in q];assert min(h)>0;n=[mul(q[i],F(1,h[i])) for i in range(N)]
adj=[set() for _ in range(N)]
for u,v in H:adj[u].add(v);adj[v].add(u)
stable=[];weakS=[];face_zero=0
for i in range(N):
 vals=[dot(n[i],n[i])-dot(n[j],n[i]) for j in adj[i]]
 if all(z>0 for z in vals):stable.append(i)
 if all(z>=0 for z in vals):weakS.append(i)
 face_zero+=sum(z==0 for z in vals)
fneigh=[set() for _ in faces]
for u,v in H:
 a=dface[(u,v)];b=dface[(v,u)];fneigh[a].add(b);fneigh[b].add(a)
unstable=[];weakU=[];vertex_zero=0
for f,x in enumerate(X):
 vals=[-dot(x,sub(X[g],x)) for g in fneigh[f]]
 if all(z>0 for z in vals):unstable.append(f)
 if all(z>=0 for z in vals):weakU.append(f)
 vertex_zero+=sum(z==0 for z in vals)
saddles=[];weakH=[];edge_zero=0
for u,v in H:
 f=dface[(u,v)];g=dface[(v,u)];a=X[f];d=sub(X[g],X[f]);dd=dot(d,d);t=-dot(a,d)/dd;z=add(a,mul(d,t));ni=n[u];nj=n[v];aa=dot(ni,ni);bb=dot(ni,nj);cc=dot(nj,nj);rr=dot(z,ni);ss=dot(z,nj);D=aa*cc-bb*bb;assert D>0
 al=(rr*cc-ss*bb)/D;be=(ss*aa-rr*bb)/D;vals=(t,1-t,al,be);edge_zero+=sum(x==0 for x in vals)
 if all(x>0 for x in vals):saddles.append((u,v))
 if all(x>=0 for x in vals):weakH.append((u,v))
assert stable==[23,53] and unstable==[2,3] and saddles==[(1,11),(56,92)]
assert [len(weakS),len(weakU),len(weakH)]==[2,2,2] and [face_zero,vertex_zero,edge_zero]==[0,0,0]
assert min_gap==F(1382951671074730364861071489704561,66114220181725757804883126314811016274315)
print('EXACT H213 REALIZATION')
print('polar n,m,f',N,len(H),len(faces),'min noninc gap',min_gap)
print('volume',V,'centroid',cent,'triangulation',tri_count)
print('class',len(stable),len(unstable),len(saddles),'S',stable,'U',unstable,'H',saddles)
print('weak',len(weakS),len(weakU),len(weakH),'zeros',face_zero,vertex_zero,edge_zero)

(ROOT/'H213_exact.json').write_text(json.dumps(enc(dict(Q=q,P=P,X=X,centroid=cent,volume=V,moments=M,faces=faces,primal_faces=inc_faces)),sort_keys=True,separators=(',',':')))
