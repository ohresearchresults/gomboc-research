"""Exact dyadic certificates: two weakly unstable vertices on every edge slide.
Input is a complete exact hull/mass report from the independent parent audits.
Polynomial signs use integer Bernstein coefficients, never floating tolerances.
"""
import sys,json,math,hashlib,time
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def poly_add(a,b):
 z=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):z[i]+=x
 for i,x in enumerate(b):z[i]+=x
 return z

def poly_mul(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z

def integer_polynomial(p):
 while len(p)>1 and not p[-1]:p.pop()
 d=math.lcm(*(x.denominator for x in p));a=[int(x*d) for x in p];g=math.gcd(*a);return [x//g for x in a] if g else a

def bernstein_nonpositive(p,l,d):
 n=len(p)-1;q=1<<d;fac=math.factorial(n)
 coeff=[sum(p[k]*math.comb(k,j)*l**(k-j)*q**(n-k) for k in range(j,n+1)) for j in range(n+1)]
 B=[sum(coeff[j]*math.comb(i,j)*(fac//math.comb(n,j)) for j in range(i+1)) for i in range(n+1)]
 return max(B)<=0

def model(data,u,w):
 P=[[F(x) for x in row] for row in data['raw_vertices']];n=len(P);adj=[set() for _ in P]
 for a,b in data['edges']:adj[a].add(b);adj[b].add(a)
 assert len(adj[u])==3 and w in adj[u];a,b=sorted(adj[u]-{w});missing=[f for f,cy in enumerate(data['faces']) if u in cy and w not in cy];assert len(missing)==1 and len(data['faces'][missing[0]])>=4
 V=F(data['ordinary_volume']);M=[F(x) for x in data['raw_first_moments']];T=abs(dot(sub(P[a],P[u]),cross(sub(P[b],P[u]),sub(P[w],P[u]))))/6;assert 0<T<V
 e=sub(P[w],P[u]);r=[2*P[u][j]+P[a][j]+P[b][j] for j in range(3)];vol=[V,-T];mom=[[M[j],-T*r[j]/4,-T*e[j]/4] for j in range(3)]
 pos=[[[P[i][j],e[j] if i==u else F(0)] for j in range(3)] for i in range(n)]
 adj[a].add(b);adj[b].add(a)
 ps=[]
 for i in range(n):
  rows=[]
  for j in sorted(adj[i]):
   total=[F(0)]
   for axis in range(3):
    z=poly_add(poly_mul(pos[i][axis],vol),[-x for x in mom[axis]]);de=[pos[j][axis][k]-pos[i][axis][k] for k in range(2)];total=poly_add(total,poly_mul(z,de))
   rows.append((j,integer_polynomial(total)))
  ps.append(rows)
 return ps,dict(u=u,w=w,other_neighbors=[a,b],cut_face=missing[0],V=n,E=data['E']+1,F=data['F']+1,T=str(T),volume_at_1=str(V-T))

def prove(data,u,w,maxdepth=30):
 ps,info=model(data,u,w);pole=next(i for i,p in enumerate(data['raw_vertices']) if list(map(F,p))==[F(0),F(0),F(1)]);info['pole']=pole
 def unstable(i,l,d):return all(bernstein_nonpositive(p,l,d) for j,p in ps[i])
 assert unstable(pole,0,0),'fixed pole must be separately covered'
 candidates=[u]+sorted(set(j for j,p in ps[u]))+[i for i in range(data['V']) if i!=pole and i!=u and i not in {j for j,p in ps[u]}];tiles=[];todo=[(0,0)];fails=[]
 while todo:
  l,d=todo.pop();v=next((i for i in candidates if unstable(i,l,d)),None)
  if v is not None:tiles.append([l,d,v]);continue
  if d>=maxdepth:fails.append([l,d]);continue
  todo.extend([(2*l+1,d+1),(2*l,d+1)])
 info.update(tiles=tiles,unresolved=fails,maxdepth=max((d for l,d,v in tiles),default=0),status='EXACT_TWO_WEAK_UNSTABLE_COVER_PASS' if not fails else 'UNRESOLVED')
 # A second pass checks a sorted exact partition and every sign assertion.
 intervals=sorted((F(l,1<<d),F(l+1,1<<d),v,l,d) for l,d,v in tiles);cursor=F(0)
 if not fails:
  for aa,bb,v,l,d in intervals:assert aa==cursor and v!=pole and unstable(v,l,d);cursor=bb
  assert cursor==1
 return info

def main():
 report,out=sys.argv[1:];raw=Path(report).read_bytes();data=json.loads(raw);ans=[];clock=time.monotonic()
 for u in data['unstable_vertices']:
  adj=sorted({j if i==u else i for i,j in data['edges'] if u in (i,j)})
  if len(adj)!=3:continue
  for w in adj:
   rec=prove(data,u,w);ans.append(rec);print(rec['status'],u,w,'tiles',len(rec['tiles']),'depth',rec['maxdepth'],'unresolved',len(rec['unresolved']),'seconds',time.monotonic()-clock,flush=True)
 payload=dict(parent_sha256=hashlib.sha256(raw).hexdigest(),families=ans,claim='For every 0<s<1, each specified homogeneous convex edge-slide has at least two distinct weakly unstable vertices relative to its own exact volume centroid. Hence none has strict110 and weak000. Endpoint s=1 is not included.');Path(out).write_text(json.dumps(payload,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
