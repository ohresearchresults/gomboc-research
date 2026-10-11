"""Exact rational physical-hull/mass audit with integer homogeneous contact signs.
The incidence oracle is numerical; every proposed vertex/facet/edge is checked
rationally. Closure as an oriented connected spherical boundary of supporting
facets certifies completeness. No floating tolerance decides an equilibrium.
"""
import json,sys,itertools,math,pathlib
import numpy as np
import gmpy2
from scipy.spatial import ConvexHull
R=gmpy2.mpq
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def sgn(a):return int(a>0)-int(a<0)
def encode(x):
 if isinstance(x,(gmpy2.mpq,gmpy2.mpz)):return str(x)
 if isinstance(x,(list,tuple)):return [encode(y) for y in x]
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 return x

def polygon(X,ids,n):
 axis=max(range(3),key=lambda k:abs(n[k]));a,b=[k for k in range(3) if k!=axis]
 ids=sorted(ids,key=lambda i:(X[i][a],X[i][b]));lo=[];hi=[]
 def turn(i,j,k):return (X[j][a]-X[i][a])*(X[k][b]-X[i][b])-(X[j][b]-X[i][b])*(X[k][a]-X[i][a])
 for seq,chain in [(ids,lo),(ids[::-1],hi)]:
  for i in seq:
   while len(chain)>1 and turn(chain[-2],chain[-1],i)<=0:chain.pop()
   chain.append(i)
 cy=lo[:-1]+hi[:-1]
 assert len(cy)>=3
 if dot(n,cross(sub(X[cy[1]],X[cy[0]]),sub(X[cy[2]],X[cy[0]])))<0:cy.reverse()
 k=cy.index(min(cy));return cy[k:]+cy[:k]

def run(H):
 H=[tuple(R(x) for x in row) for row in H];assert all(row[3]>0 for row in H)
 N=[r[:3] for r in H];D=[r[3] for r in H]
 q=np.array([[float(x/r[3]) for x in r[:3]] for r in H]);oracle=ConvexHull(q)
 assert np.max(oracle.equations[:,3])<0
 vertices=set();groups=[]
 for ids in oracle.simplices:
  i,j,k=map(int,ids);a,b,c=N[i],N[j],N[k];dd=det(a,b,c)
  assert dd
  p=mul(1/dd,add(add(mul(D[i],cross(b,c)),mul(D[j],cross(c,a))),mul(D[k],cross(a,b))))
  assert all(dot(n,p)<=d for n,d in zip(N,D)),('infeasible proposed vertex',ids)
  vertices.add(p)
 X=sorted(vertices);faces=[];active=[]
 for k,(n,d) in enumerate(zip(N,D)):
  ids=[i for i,v in enumerate(X) if dot(n,v)==d]
  if len(ids)<3:continue
  cy=polygon(X,ids,n);assert set(cy)==set(ids),'non-extreme row on a facet'
  faces.append(cy);active.append(k)
 edges={};tris=[]
 for fi,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append((fi,i,j))
  tris.extend((cy[0],cy[k],cy[k+1]) for k in range(1,len(cy)-1))
 assert len(X)-len(edges)+len(faces)==2
 assert all(len(e)==2 and e[0][1:]==e[1][1:][::-1] for e in edges.values()),'incomplete boundary'
 # Exact supporting facets + full cyclic vertex links certify a closed sphere.
 neighbors=[set() for _ in X]
 for i,j in edges:neighbors[i].add(j);neighbors[j].add(i)
 seen=set();todo=[0]
 while todo:
  i=todo.pop()
  if i not in seen:seen.add(i);todo.extend(neighbors[i]-seen)
 assert len(seen)==len(X)
 for v in range(len(X)):
  link={u:[] for u in neighbors[v]}
  for cy in faces:
   if v in cy:
    k=cy.index(v);u,w=cy[k-1],cy[(k+1)%len(cy)];link[u].append(w);link[w].append(u)
  assert all(len(a)==2 for a in link.values())
  ls=set();lt=[next(iter(link))]
  while lt:
   u=lt.pop()
   if u not in ls:ls.add(u);lt.extend(set(link[u])-ls)
  assert ls==set(link)
 volume=R(0);moment=(R(0),)*3
 for i,j,k in tris:
  dv=det(X[i],X[j],X[k])/6;assert dv>0
  volume+=dv;moment=add(moment,mul(dv/4,add(add(X[i],X[j]),X[k])))
 g=mul(1/volume,moment);Z=[sub(v,g) for v in X]
 assert all(d-dot(n,g)>0 for n,d in zip(N,D))
 # vi=Pi/di and g=G/D. Ai=Pi*D-G*di represents di*D*(vi-g).
 # Every discarded denominator below is strictly positive; signs are exact integers.
 def homogeneous(v):
  dd=math.lcm(*(int(x.denominator) for x in v));return tuple(gmpy2.mpz(x*dd) for x in v),gmpy2.mpz(dd)
 G,GD=homogeneous(g);PV=[homogeneous(v) for v in X];IV=[p for p,d in PV];VD=[d for p,d in PV];AZ=[sub(mul(GD,p),mul(d,G)) for p,d in PV];IN=[homogeneous(n)[0] for n in N]
 def direction(i,j):return sub(mul(VD[i],IV[j]),mul(VD[j],IV[i]))
 SF=[];SW=[];UV=[];UW=[];EH=[];EW=[];fs=[];vs=[];es=[]
 for fi,cy in enumerate(faces):
  n=IN[active[fi]]
  signs=[sgn(dot(n,cross(AZ[i],direction(i,j)))) for i,j in zip(cy,cy[1:]+cy[:1])]
  fs.append(signs)
  if min(signs)>0:SF.append(fi)
  elif min(signs)==0:SW.append(fi)
 for i,v in enumerate(AZ):
  signs=[sgn(dot(v,direction(i,j))) for j in range(len(X)) if j!=i];best=max(signs);vs.append(best)
  if best<0:UV.append(i)
  elif best==0:UW.append(i)
 for (i,j),ef in sorted(edges.items()):
  e=direction(i,j);ee=dot(e,e);ze=dot(AZ[i],e);p=sub(mul(ee,AZ[i]),mul(ze,e))
  n,m=(IN[active[r[0]]] for r in ef);nn=dot(n,n);mm=dot(m,m);nm=dot(n,m);assert nn*mm-nm*nm>0
  signs=list(map(sgn,[-ze,dot(AZ[j],e),dot(p,sub(mul(mm,n),mul(nm,m))),dot(p,sub(mul(nn,m),mul(nm,n)))]));es.append([i,j,*signs])
  if min(signs)>0:EH.append([i,j])
  elif min(signs)==0:EW.append([i,j])
 counts=[len(SF),len(UV),len(EH)];weak=[len(SW),len(UW),len(EW)]
 if weak==[0,0,0]:assert counts[0]+counts[1]-counts[2]==2
 return encode(dict(V=len(X),E=len(edges),F=len(faces),C=2*len(edges),counts=counts,weak=weak,primitive_zero=[sum(s.count(0) for s in fs),vs.count(0),sum(s[2:].count(0) for s in es)],raw_vertices=X,raw_halfspaces=H,faces=faces,active=active,edges=sorted(edges),volume=volume,moment=moment,centroid=g,stable_faces=SF,unstable_vertices=UV,saddle_edges=EH,weak_faces=SW,weak_vertices=UW,weak_edges=EW,face_signs=fs,vertex_max_signs=vs,edge_signs=es))
if __name__=='__main__':
 import argparse,time
 ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output');a=ap.parse_args();t=time.time()
 h=json.load(open(a.input));h=h['H'] if isinstance(h,dict) else h
 r=run(h);pathlib.Path(a.output).write_text(json.dumps(r,separators=(',',':')))
 print({k:r[k] for k in ['V','E','F','C','counts','weak','primitive_zero']},'seconds',time.time()-t)
