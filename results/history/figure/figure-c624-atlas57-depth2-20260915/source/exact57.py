"""S8 source-only exact recharts, finite leaf contraction and primal-star events.
All geometry definitions in this unit use only rational standard-library arithmetic.
"""
import itertools,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from math import lcm,gcd
import rational56
from RECONSTRUCT import solve
ROOT=Path(__file__).resolve().parent
PARENT_SHA='bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2'
def enc(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def det(rows):
 if not rows:return F(1)
 if len(rows)==1:return rows[0][0]
 return sum((-1)**i*rows[0][i]*det([r[:i]+r[i+1:] for r in rows[1:]]) for i in range(len(rows)))
def axes(X,deps):return list(max(itertools.combinations(range(3),len(deps)),key=lambda ax:abs(det([[X[j][k] for k in ax] for j in deps]))))
def owners(fs):return [[i for i,cy in enumerate(fs) if v in cy] for v in range(1+max(map(max,fs)))]
def physical(q,fs):
 P=[]
 for oo in owners(fs):
  dd=next(t for t in itertools.combinations(oo,3) if det([q[i] for i in t]))
  p=solve([q[i] for i in dd],[F(1)]*3)
  assert all(dot(q[i],p)==1 for i in oo)
  assert all(dot(r,p)<1 for i,r in enumerate(q) if i not in oo)
  P.append(p)
 assert len(set(map(tuple,P)))==len(P)
 return P
def encode(X,groups,plan,n=137):
 z=dict(n_supports=n,groups=groups,plan=plan,controls=[[0]*3 for _ in X],denominators=[1]*len(X));z['controls'][n]=[0,0,1]
 for i,deps,aa in plan:
  rest=[k for k in range(3) if k not in aa];D=lcm(*(X[i][k].denominator for k in rest));z['denominators'][i]=D
  for k in rest:z['controls'][i][k]=int(D*X[i][k])
 return z
def complexity(d):
 dep={d['n_supports']:0}
 for i,dd,aa in d['plan']:dep[i]=1+max((dep[j] for j in dd),default=-1)
 return dict(nodes=len(d['controls']),groups=len(d['groups']),free=sum(3-len(aa) for i,dd,aa in d['plan']),depth=max(dep.values()))
def source():
 b=(ROOT/'PARENT_S8.json').read_bytes();assert hashlib.sha256(b).hexdigest()==PARENT_SHA
 d=json.loads(b);fs=json.loads((ROOT/'FACES_S8.json').read_bytes());return d,fs
CORE=[26,54,76,78,79,90]
B8={142,151,153,163,167,169,173,174}
B4={145,158,161,173}
def manual(d):
 X=rational56.points(d);n=d['n_supports'];assert n==137 and len(X)==179
 so=[[n+j for j,o in enumerate(d['groups']) if i in o] for i in range(n)]
 assert [i for i,o in enumerate(so) if len(o)>3]==CORE
 plan=[[v,[],[]] for v in range(138,178) if v not in B8]
 for i in CORE:
  dd=[v for v in so[i] if v not in B8];assert len(dd)==3;plan.append([i,dd,[0,1,2]])
 for v in sorted(B8):
  dd=[i for i in CORE if v in so[i]];assert len(dd)==1;plan.append([v,dd,axes(X,dd)])
 for i in range(n):
  if i in CORE or i==18:continue
  dd=[v for v in so[i] if v!=178];assert len(dd)<=3;plan.append([i,dd,axes(X,dd)])
 plan.extend([[178,[16,71,94],[0,1,2]],[18,[178],axes(X,[178])]])
 z=encode(X,d['groups'],plan);assert rational56.points(z)==X
 assert complexity(z)['free']==complexity(d)['free']==315 and complexity(z)['depth']==3
 return z

def general(d,fs):
 q=rational56.points(d)[:137];P=physical(q,fs);ow=owners(fs);r=P.index([0,0,1]);ids=[r]+[i for i,o in enumerate(ow) if i!=r and len(o)>3];groups=[ow[i] for i in ids];X=q+[P[i] for i in ids];n=137
 so=[[n+j for j,o in enumerate(groups) if i in o] for i in range(n)];core=[i for i,o in enumerate(so) if len(o)>3];assert core==CORE
 assert all(sum(v in B4 for v in so[i])==len(so[i])-3 for i in core)
 plan=[[v,[],[]] for v in range(n+1,len(X)) if v not in B4]
 for i in core:
  dd=[v for v in so[i] if v not in B4];assert len(dd)==3;assert det([X[v] for v in dd]);plan.append([i,dd,[0,1,2]])
 for v in sorted(B4):
  dd=[i for i in core if v in so[i]];assert 1<=len(dd)<=3;plan.append([v,dd,axes(X,dd)])
 for i in range(n):
  if i in core:continue
  dd=so[i];assert len(dd)<=3;plan.append([i,dd,axes(X,dd)])
 z=encode(X,groups,plan);assert rational56.points(z)==X
 assert complexity(z)['free']==complexity(d)['free'] and complexity(z)['depth']==3
 return z

def core_free(d):
 X=rational56.points(d);n=d['n_supports'];groups=d['groups'];so=[[n+j for j,o in enumerate(groups) if i in o] for i in range(n)];core=[i for i,dd in enumerate(so) if len(dd)>3]
 assert not set(core)&set(groups[0]);assert max(len(set(o)&set(core)) for o in groups)<=3
 plan=[[i,[],[]] for i in core]
 for v,o in enumerate(groups[1:],n+1):
  dd=[i for i in o if i in core];aa=axes(X,dd);assert det([[X[i][k] for k in aa] for i in dd]);plan.append([v,dd,aa])
 for i in range(n):
  if i in core:continue
  dd=so[i];aa=axes(X,dd);assert len(dd)<=3 and det([[X[j][k] for k in aa] for j in dd]);plan.append([i,dd,aa])
 z=encode(X,groups,plan,n);assert rational56.points(z)==X
 assert complexity(z)['free']==complexity(d)['free'] and complexity(z)['depth']==2
 return z

def round_core_free(d,grid):
 z=core_free(d);X=rational56.points(z);z.pop('denominators');z['grid']=grid;z['controls']=[[0]*3 for _ in X];z['controls'][z['n_supports']]=[0,0,grid]
 for i,deps,aa in z['plan']:
  for k in range(3):
   if k not in aa:z['controls'][i][k]=round(grid*X[i][k])
 return z

def quotient_cycles(fs,a,b):
 keep=[i for i in range(1+max(map(max,fs))) if i!=b];mp={i:j for j,i in enumerate(keep)};mp[b]=mp[a];out=[]
 for cy in fs:
  cc=[]
  for i in cy:
   if not cc or cc[-1]!=mp[i]:cc.append(mp[i])
  if cc[-1]==cc[0]:cc.pop()
  assert len(set(cc))==len(cc)>=3;out.append(cc)
 return out

def leaf622(d,fs):
 z=manual(d);X=rational56.points(z);n=137;p=solve([X[i] for i in [101,102,121]],[F(1)]*3);t=(1-dot(X[120],p))/dot(p,p);X[120]=[v+t*w for v,w in zip(X[120],p)];X.append(p);groups=z['groups']+[[101,102,120,121]]
 so=[[n+j for j,o in enumerate(groups) if i in o] for i in range(n)]
 plan=[[v,[],[]] for v in list(range(138,178))+[179] if v not in B8]
 for i in CORE:
  dd=[v for v in so[i] if v not in B8];assert len(dd)==3;plan.append([i,dd,[0,1,2]])
 for v in sorted(B8):
  dd=[i for i in CORE if v in so[i]];plan.append([v,dd,axes(X,dd)])
 for i in range(n):
  if i in CORE or i==18:continue
  dd=[v for v in so[i] if v!=178];assert len(dd)<=3;plan.append([i,dd,axes(X,dd)])
 plan.extend([[178,[16,71,94],[0,1,2]],[18,[178],axes(X,[178])]])
 out=encode(X,groups,plan);assert rational56.points(out)==X and complexity(out)['free']==314
 return out,quotient_cycles(fs,162,164)

def plane(P,cy):
 a,b,c=[P[i] for i in cy[:3]];n=cross(sub(b,a),sub(c,a));return n,dot(n,a)
def star(d,fs,v,side):
 q=rational56.points(d)[:137];P=physical(q,fs);own=[f for f,cy in enumerate(fs) if v in cy];tri=[f for f in own if len(fs[f])==3];other=[f for f in own if len(fs[f])>3];assert len(own)==3 and len(tri)==2 and len(other)==1
 cy=fs[other[0]];k=cy.index(v);a,b=cy[k-1],cy[(k+1)%len(cy)];dr=sub(P[b],P[a]);constraints=[]
 for f in range(len(fs)):
  if f not in tri:constraints.append((1-dot(q[f],P[v]),-dot(q[f],dr)))
 PP=[p[:] for p in P];PP[v]=[x+y for x,y in zip(P[v],dr)]
 for f in tri:
  n,h=plane(P,fs[f]);nn,hh=plane(PP,fs[f]);dn=sub(nn,n);dh=hh-h;constraints.append((h,dh))
  for j,p in enumerate(P):
   if j!=v:constraints.append((h-dot(n,p),dh-dot(dn,p)))
 assert all(g>=0 for g,dt in constraints)
 ends=[max(-g/dt for g,dt in constraints if dt>0),min(-g/dt for g,dt in constraints if dt<0)];t=ends[side];PP[v]=[x+t*y for x,y in zip(P[v],dr)];rows=[]
 for cy in fs:
  n,h=plane(PP,cy)
  if h==0:continue
  assert h>0 and all(dot(n,p)<=h for p in PP)
  vv=n+[h];D=lcm(*(x.denominator for x in vv));row=[int(x*D) for x in vv];G=gcd(*row);row=[x//G for x in row]
  if row not in rows:rows.append(row)
 # Independently compute exact full filled mass on both boundary chains.
 def mass(P):
  D=F(0);L=[F(0)]*3
  for cy in fs:
   for k in range(1,len(cy)-1):
    aa,bb,cc=[P[i] for i in [cy[0],cy[k],cy[k+1]]];dd=dot(aa,cross(bb,cc));assert dd>=0;D+=dd;L=[x+dd*(i+j+k) for x,i,j,k in zip(L,aa,bb,cc)]
  return D/6,[x/24 for x in L]
 V,M=mass(P);VV,MM=mass(PP);c=next(i for i in set(j for f in tri for j in fs[f]) if i not in [a,b,v]);w=abs(dot(sub(P[a],P[c]),cross(sub(P[v],P[c]),sub(P[b],P[c]))))/6
 assert V==VV and sub(MM,M)==[w*t*x/4 for x in dr]
 return {'H':rows},dict(vertex=v,side=side,t=str(t),direction=list(map(str,dr)),volume_preserved=True,first_moment_change=list(map(str,sub(MM,M))),tetrahedron_volume=str(w))

def equality():
 d,fs=source();m=manual(d);g=general(d,fs);leaf,lf=leaf622(d,fs)
 return {'source':PARENT_SHA,'source_complexity':complexity(d),'manual':complexity(m),'core4':complexity(g),'core_free':complexity(core_free(g)),'core4_sacrificed_auxiliaries':sorted(B4),'manual_sacrificed_auxiliaries':sorted(B8),'all_source_supports_exactly_equal':True,'all_retained_source_vertices_exactly_equal':True,'leaf_seed_complexity':complexity(leaf),'leaf_projection_rechart_exactly_equal':True}
if __name__=='__main__':print(enc(equality()).decode())
