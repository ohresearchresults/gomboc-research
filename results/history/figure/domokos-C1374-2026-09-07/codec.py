"""Deterministic PN03 recovery, exact rationals; no numerical selectors."""
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
from pathlib import Path
from collections import defaultdict
import sys,json
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def parse(raw):
 assert raw[:4]==b'PN03';it=iter(raw[4:])
 def u():
  z=s=0
  while True:
   a=next(it);z|=(a&127)<<s
   if a<128:return z
   s+=7
 def si():
  z=u();return z//2 if not z%2 else -(z//2)-1
 D0,N=u(),u();last=[0,0,0];J=[]
 for i in range(N):
  for k in range(3):last[k]+=si()
  J.append(tuple(last))
 ops=[]
 for _ in range(u()):
  t,m=u(),u();bases=[tuple(u()for k in range(3))for j in range(m)];dep=tuple(u()for j in range(m));ops.append((t,bases,dep))
 nt=u();lst=0;T=[]
 for _ in range(nt):
  tri=[]
  for k in range(3):lst+=si();tri.append(lst)
  T.append(tuple(tri))
 K,pr,po=u(),u(),u();wi=[]
 for _ in range(2):
  last=0;a=[]
  for j in range(u()):last+=si();a.append(last)
  wi.append(a)
 try:next(it);raise AssertionError('trailing data')
 except StopIteration:pass
 return D0,J,ops,T,K,pr,po,wi

def reconstruct(raw):
 D0,J,ops,T,K,pr,po,wi=parse(raw);R=[[F(j,D0)for j in row]for row in J]
 for t,bases,dep in ops:
  free=[i for i in range(3)if i not in dep];mat=[]
  for a,b,c in bases:
   n=cross(sub(R[b],R[a]),sub(R[c],R[a]));rhs=dot(n,R[a])-sum(n[k]*R[t][k]for k in free)
   mat.append([n[k]for k in dep]+[rhs])
  m=len(dep)
  for k in range(m):
   q=next(j for j in range(k,m)if mat[j][k]);mat[k],mat[q]=mat[q],mat[k];v=mat[k][k];mat[k]=[x/v for x in mat[k]]
   for j in range(m):
    if j!=k:
     v=mat[j][k];mat[j]=[x-v*y for x,y in zip(mat[j],mat[k])]
  for k,axis in enumerate(dep):R[t][axis]=mat[k][-1]
 for t,bases,dep in ops:
  for a,b,c in bases:assert det(sub(R[b],R[a]),sub(R[c],R[a]),sub(R[t],R[a]))==0
 D=lcm(*(r.denominator for row in R for r in row));I=[tuple(int(x*D)for x in row)for row in R]
 return I,D,T,(K,pr,po,wi)

def topology(I,T):
 faces={};tf=[];occ=defaultdict(list)
 for tri in T:
  a,b,c=[I[i]for i in tri];n=cross(sub(b,a),sub(c,a));h=dot(n,a);gg=reduce(gcd,(*n,h));p=tuple(x//gg for x in (*n,h));assert h>0
  f=faces.setdefault(p,len(faces));tf.append(f)
  for i,j in zip(tri,tri[1:]+tri[:1]):occ[tuple(sorted((i,j)))].append((f,i,j))
 bd=defaultdict(dict);edges=[]
 for v in occ.values():
  assert len(v)==2
  f,i,j=v[0];g,jj,ii=v[1];assert i==ii and j==jj
  if f!=g:bd[f][i]=j;bd[g][j]=i;edges.append((i,j,f,g))
 cycles=[]
 for f in range(len(faces)):
  b=bd[f];s=min(b);cy=[s];v=b[s]
  while v!=s:assert v not in cy;cy.append(v);v=b[v]
  assert len(cy)==len(b);cycles.append(cy)
 return list(faces),cycles,edges,tf

if __name__=='__main__':
 import numpy as np, time
 raw=Path(sys.argv[1]).read_bytes();t=time.time();I,D,T,extra=reconstruct(raw)
 print('recovered',len(I),len(T),len(str(D)),'seconds',time.time()-t,flush=True)
 planes,cycles,edges,tf=topology(I,T);W=sum(det(I[a],I[b],I[c])for a,b,c in T)
 M=[sum(det(I[a],I[b],I[c])*(I[a][k]+I[b][k]+I[c][k])for a,b,c in T)for k in range(3)]
 X=np.array([[float(F(x,D))for x in row]for row in I]);c=np.array([float(F(m,4*W*D))for m in M]);V=X-c
 np.savez(sys.argv[2],X=X,V=V,T=T,cycles=np.array(cycles,dtype=object),locks=np.array([cy for cy in cycles if len(cy)>3],dtype=object))
 print('VEF',len(I),len(edges),len(cycles),'centroid',c,'volume',float(F(W,6*D**3)), 'seconds',time.time()-t)
