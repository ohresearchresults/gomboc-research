"""Exact all-s exclusion with perfect old-centroid closure and arbitrary cap shape.
Unlike the old unconstrained-volume slides, the fixed centre here is a CONDITION
on the actual modified body's volume centroid. No unmodified mass formula is used.
"""
import sys,json,math
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
sys.set_int_max_str_digits(0)
CAPS={99:[([0,2],[1,3,10,95]),([83,85,87,91,93,96,98,102,105,110,113],[79,90,95,116])],117:[([0,2],[1,3,10,93]),([82,83,85,89,91,94,96,100,103,108,111],[79,88,93,114])]}
CAPS[84]=CAPS[99]
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def ipoly(p):
 while len(p)>1 and not p[-1]:p.pop()
 den=math.lcm(*(x.denominator for x in p));q=[int(x*den) for x in p];gg=math.gcd(*q)
 return [v//gg for v in q] if gg else q

def nonpositive(p,l,d):
 n=len(p)-1;q=1<<d;fac=math.factorial(n)
 coeff=[sum(p[k]*math.comb(k,j)*l**(k-j)*q**(n-k) for k in range(j,n+1)) for j in range(n+1)]
 bern=[sum(coeff[j]*math.comb(i,j)*(fac//math.comb(n,j)) for j in range(i+1)) for i in range(n+1)]
 return max(bern)<=0

def proof(a,deleted):
 P=[tuple(map(Q,p)) for p in a['raw_vertices']];g=tuple(map(Q,a['raw_centroid']));n=len(P)
 adj=[set() for p in P]
 for i,j in a['edges']:adj[i].add(j);adj[j].add(i)
 apex=next(i for i,p in enumerate(P) if p==(0,0,1));u=next(i for i in a['unstable_vertices'] if i!=apex)
 moving=set(i for cap,sep in CAPS[deleted] for i in cap)
 unchanged=[f for f,cy in enumerate(a['faces']) if not set(cy)&moving]
 goodapex=[f for f in unchanged if apex in a['faces'][f]];z=sub(P[apex],g);certificate=None
 for ii in combinations(goodapex,3):
  n1,n2,n3=[a['normals'][i] for i in ii];den=det(n1,n2,n3)
  if not den:continue
  weights=[Q(dot(z,cross(n2,n3)),den),Q(dot(n1,cross(z,n3)),den),Q(dot(n1,cross(n2,z)),den)]
  if min(weights)>0:
   assert all(sum(weights[k]*a['normals'][ii[k]][j] for k in range(3))==z[j] for j in range(3))
   certificate=dict(faces=list(ii),weights=list(map(str,weights)));break
 assert certificate is not None
 safe=[i for i in range(n) if i!=apex and all(f in unchanged for f,cy in enumerate(a['faces']) if i in cy)]
 families=[]
 for w in sorted(adj[u]):
  aa,bb=sorted(adj[u]-{w});neighbors=[set(z) for z in adj];neighbors[aa].add(bb);neighbors[bb].add(aa);e=sub(P[w],P[u]);vel=[e if i==u else (Q(0),)*3 for i in range(n)];polys={}
  for i in safe:
   assert not neighbors[i]&moving
   rows=[]
   for j in sorted(neighbors[i]):
    pi=sub(P[i],g);de=sub(P[j],P[i]);dv=sub(vel[j],vel[i])
    rows.append((j,ipoly([dot(pi,de),dot(pi,dv)+dot(vel[i],de),dot(vel[i],dv)])))
   polys[i]=rows
  def unstable(i,l,d):return all(nonpositive(p,l,d) for j,p in polys[i])
  todo=[(0,0)];tiles=[];failed=[];candidates=[u]+[i for i in safe if i!=u]
  while todo:
   l,d=todo.pop();v=next((i for i in candidates if unstable(i,l,d)),None)
   if v is not None:tiles.append([l,d,v]);continue
   if d==30:failed.append([l,d]);continue
   todo.extend([(2*l+1,d+1),(2*l,d+1)])
  assert not failed
  partition=sorted((Q(l,1<<d),Q(l+1,1<<d),v,l,d) for l,d,v in tiles);last=Q(0)
  for left,right,v,l,d in partition:assert left==last and unstable(v,l,d);last=right
  assert last==1
  families.append(dict(u=u,w=w,tiles=tiles,degree=max(len(p)-1 for rows in polys.values() for _,p in rows)))
  print('PERFECT_CENTROID_TWO_CAP_EXCLUSION',deleted,u,w,'tiles',len(tiles),tiles,flush=True)
 return dict(status='ALL_REAL_ADMISSIBLE_TWO_CAP_SHAPES_AT_PERFECT_CENTROID_SLIDE_EXCLUDED',deleted_support=deleted,caps=[{'vertices':x,'boundary':y} for x,y in CAPS[deleted]],apex=apex,apex_certificate=certificate,families=families,scope='For 0<s<1, all compatible convex realizations of the planned edge slide with either cap changed by any boundary-fixing projectivity, and ACTUAL volume centroid exactly equal to the original centroid. At least two weak unstable vertices. Unchanged old support planes and planned local stars remain true. No assertion about a different centroid, different local surgery, or metric.')
if __name__=='__main__':
 p,j,out=sys.argv[1:];data=json.loads(Path(p).read_text());r=proof(data,int(j));Path(out).write_text(json.dumps(r,sort_keys=True,separators=(',',':')))
