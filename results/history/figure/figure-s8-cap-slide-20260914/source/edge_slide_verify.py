"""Independent exact check of a complete one-vertex edge-slide exclusion.
Rebuilds support/complex conditions on the whole open interval, computes mass by
boundary integration at four rational parameters, interpolates radial primitives,
and checks the saved dyadic cover with de Casteljau, not the producer's formula.
Usage: python -B -S edge_slide_verify.py PARENT_A.json COVER.json OUTPUT.json
"""
import sys,json,math,hashlib
from pathlib import Path
from fractions import Fraction as Q
sys.set_int_max_str_digits(0)
assert __debug__

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def minus(x,y):return tuple(a-b for a,b in zip(x,y))
def cross(x,y):return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def det(a,b,c):return dot(a,cross(b,c))
def pos(P,u,w,s):
 R=list(P);R[u]=tuple((1-s)*a+s*b for a,b in zip(P[u],P[w]));return R

def complex_and_geometry(data,rec):
 P=[tuple(map(Q,p)) for p in data['raw_vertices']];u,w=rec['u'],rec['w']
 oldedges=set(map(tuple,data['edges']));adj=[set() for _ in P]
 for a,b in oldedges:adj[a].add(b);adj[b].add(a)
 assert len(adj[u])==3 and w in adj[u]
 a,b=sorted(adj[u]-{w});assert [a,b]==rec['other_neighbors'] and (a,b) not in oldedges
 cy=[list(c) for c in data['faces']];cut=[i for i,c in enumerate(cy) if u in c and w not in c];assert cut==[rec['cut_face']] and len(cy[cut[0]])>=4
 cy[cut[0]].remove(u);T=abs(det(minus(P[a],P[u]),minus(P[b],P[u]),minus(P[w],P[u])))/6;assert T==Q(rec['T']) and T>0
 Rmid=pos(P,u,w,Q(1,2));tri=[a,b,u]
 if dot(cross(minus(Rmid[b],Rmid[a]),minus(Rmid[u],Rmid[a])),minus(P[u],Rmid[a]))<0:tri.reverse()
 cy.append(tri)
 ends=[pos(P,u,w,s) for s in [Q(0),Q(1)]];planes=[]
 for f,c in enumerate(cy):
  if f<data['F']:
   n=tuple(map(Q,data['normals'][f]));h=Q(data['offsets'][f]);planes.append([(n,h),(n,h)])
  else:
   planes.append([])
   for R in ends:
    x,y,z=(R[i] for i in c);n=cross(minus(y,x),minus(z,x));planes[-1].append((n,dot(n,x)))
  inside=set(c)
  for i in range(len(P)):
   vals=[h-dot(n,R[i]) for R,(n,h) in zip(ends,planes[f])]
   if i in inside:assert vals==[0,0]
   else:assert min(vals)>=0 and max(vals)>0,(f,i)
  # The only possibly quadratic support evaluation is identically zero:
  if f==data['F']:
   dn=minus(planes[f][1][0],planes[f][0][0]);assert dot(dn,minus(P[w],P[u]))==0
  else:
   # Every old polygon remains strictly convex throughout 0<s<1.
   for i in range(len(c)):
    vals=[]
    for R,(n,h) in zip(ends,planes[f]):
     x,y,z=[R[c[j%len(c)]] for j in [i,i+1,i+2]];vals.append(dot(n,cross(minus(y,x),minus(z,y))))
    assert min(vals)>=0 and max(vals)>0,(f,i,'nonconvex cycle')
 # Each labelled point remains an extreme point: incident-normal rank3,
 # certified by a linear determinant with one fixed sign on (0,1).
 from itertools import combinations
 owners=[[f for f,c in enumerate(cy) if i in c] for i in range(len(P))]
 for i,ow in enumerate(owners):
  found=False
  for f,g,h in combinations(ow,3):
   vals=[det(planes[f][j][0],planes[g][j][0],planes[h][j][0]) for j in [0,1]]
   if (min(vals)>=0 or max(vals)<=0) and any(vals):found=True;break
  assert found,('vertex rank',i)
 ed={}
 for f,c in enumerate(cy):
  for a,b in zip(c,c[1:]+c[:1]):ed.setdefault(tuple(sorted((a,b))),[]).append((f,a,b))
 assert set(ed)==oldedges|{tuple(rec['other_neighbors'])}
 assert all(len(v)==2 and v[0][1:]==v[1][1:][::-1] for v in ed.values())
 assert len(P)-len(ed)+len(cy)==2
 assert [len(P),len(ed),len(cy)]==[rec['V'],rec['E'],rec['F']]
 # No extra true edges from fan diagonals are counted.
 adj=[set() for _ in P]
 for a,b in ed:adj[a].add(b);adj[b].add(a)
 seen={0};todo=[0]
 while todo:
  for j in adj[todo.pop()]-seen:seen.add(j);todo.append(j)
 assert len(seen)==len(P)
 return P,cy,adj,ends,planes

def mass(P,faces):
 v=Q(0);m=[Q(0)]*3
 for c in faces:
  for k in range(1,len(c)-1):
   x,y,z=[P[i] for i in (c[0],c[k],c[k+1])];d=det(x,y,z);v+=d/6
   for j in range(3):m[j]+=d*(x[j]+y[j]+z[j])/24
 return v,tuple(m)

def interpolate(values):
 ts=[Q(0),Q(1,3),Q(2,3),Q(1)];out=[Q(0)]*4
 for i,v in enumerate(values):
  coeff=[Q(1)];den=Q(1)
  for j,t in enumerate(ts):
   if i==j:continue
   arr=[Q(0)]*(len(coeff)+1)
   for k,c in enumerate(coeff):arr[k]-=t*c;arr[k+1]+=c
   coeff=arr;den*=ts[i]-t
  for k,c in enumerate(coeff):out[k]+=v*c/den
 return out

def bernstein_on_cell(c,l,d):
 # Independent conversion to degree-three Bernstein, then exact midpoint cuts.
 b=[sum(c[j]*Q(math.comb(k,j),math.comb(3,j)) for j in range(k+1)) for k in range(4)]
 for bit in bin(l)[2:].zfill(d) if d else '':
  rows=[b]
  while len(rows[-1])>1:rows.append([(a+b)/2 for a,b in zip(rows[-1],rows[-1][1:])])
  b=[row[0] for row in rows] if bit=='0' else [row[-1] for row in rows[::-1]]
 return b

def verify(data,cover):
 recs=[]
 for rec in cover['families']:
  assert rec['status']=='EXACT_TWO_WEAK_UNSTABLE_COVER_PASS' and rec['unresolved']==[]
  P,faces,adj,ends,planes=complex_and_geometry(data,rec);u,w=rec['u'],rec['w'];T=Q(rec['T']);V0=Q(data['ordinary_volume']);M0=tuple(map(Q,data['raw_first_moments']));a,b=rec['other_neighbors'];e=minus(P[w],P[u]);snap=[]
  for s in [Q(0),Q(1,3),Q(2,3),Q(1)]:
   R=pos(P,u,w,s);v,m=mass(R,faces);assert v>0
   assert v==V0-s*T
   assert all(m[j]==M0[j]-s*T*(2*P[u][j]+P[a][j]+P[b][j]+s*e[j])/4 for j in range(3))
   snap.append((R,v,m))
  assert snap[-1][1]==Q(rec['volume_at_1'])
  pole=rec['pole'];assert P[pole]==(0,0,1) and pole!=u;cache={}
  def primitive(i,j):
   if (i,j) not in cache:
    vals=[dot(tuple(v*x-y for x,y in zip(R[i],m)),minus(R[j],R[i])) for R,v,m in snap]
    cache[i,j]=interpolate(vals)
   return cache[i,j]
  def weak(i,l,d):return all(max(bernstein_on_cell(primitive(i,j),l,d))<=0 for j in adj[i])
  assert weak(pole,0,0)
  tiles=sorted((Q(l,1<<d),Q(l+1,1<<d),i,l,d) for l,d,i in rec['tiles']);cursor=Q(0)
  for lo,hi,i,l,d in tiles:
   assert lo==cursor and hi>lo and i!=pole and weak(i,l,d);cursor=hi
  assert cursor==1
  recs.append(dict(u=u,w=w,V=rec['V'],E=rec['E'],F=rec['F'],tiles=len(tiles),witness_vertices=sorted({x[2] for x in tiles}),pole=pole,independent_polynomials=len(cache),geometry_on_open_unit_interval=True,mass_by_four_boundary_integrals=True,independent_de_casteljau_cover=True))
  print('INDEPENDENT_GEOMETRY_MASS_TWO_U_INTERVAL_PASS',u,w,flush=True)
 return dict(status='NINE_EDGE_SLIDES_SEPARATE_CHECKER_PASS',families=recs,conclusion='All listed families have two distinct weakly unstable true vertices at their own uniform-volume centroid for every 0<s<1. Endpoint s=1 is excluded.')

if __name__=='__main__':
 rp,cp,out=map(Path,sys.argv[1:]);rb=rp.read_bytes();cb=cp.read_bytes();cover=json.loads(cb);assert hashlib.sha256(rb).hexdigest()==cover['parent_sha256'];ans=verify(json.loads(rb),cover);ans['cover_sha256']=hashlib.sha256(cb).hexdigest();Path(out).write_text(json.dumps(ans,sort_keys=True,separators=(',',':')))
