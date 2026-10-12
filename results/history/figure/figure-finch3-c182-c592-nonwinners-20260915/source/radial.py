"""Complete rational coordinate atlas of a maximal polyhedral incidence graph.
All incident vertex/plane pairs are imposed exactly, with one vertex anchored.
"""
import json,sys,itertools
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
sys.set_int_max_str_digits(0)
def solve(A,b):
 M=[list(a)+[v] for a,v in zip(A,b)];n=len(M)
 for k in range(n):
  j=next(i for i in range(k,n) if M[i][k]);M[k],M[j]=M[j],M[k];p=M[k][k];M[k]=[x/p for x in M[k]]
  for i in range(n):
   if i!=k:
    t=M[i][k];M[i]=[x-t*y for x,y in zip(M[i],M[k])]
 return [r[-1] for r in M]
def reconstruct(G):
 n=G['n_supports'];D=G['grid'];X=[[F(x,D) for x in row] for row in G['controls']];X[n]=[F(0),F(0),F(1)];done={n};ed=set()
 for i,deps,axes in G['plan']:
  assert i not in done and set(deps)<=done and len(deps)==len(axes)<=3
  rest=[j for j in range(3) if j not in axes]
  if deps:
   v=solve([[X[j][k] for k in axes] for j in deps],[1-sum(X[j][k]*X[i][k] for k in rest) for j in deps])
   for k,x in zip(axes,v):X[i][k]=x
  for j in deps:
   assert sum(a*b for a,b in zip(X[i],X[j]))==1;ed.add(tuple(sorted((i,j))))
  done.add(i)
 expected={tuple(sorted((q,n+i))) for i,fs in enumerate(G['groups']) for q in fs};assert ed==expected and len(done)==len(X)
 H=[]
 for v in X[:n]:
  den=lcm(*(a.denominator for a in v));nums=[int(a*den) for a in v]+[den];d=gcd(*nums);H.append([x//d for x in nums])
 return {'H':H},X[n:]
def make(P,q,faces,root,grid=10**12,priority=None):
 import numpy as np
 n=len(q);perm=[root]+[i for i in range(len(P)) if i!=root];ind={i:k for k,i in enumerate(perm)};groups=[[] for i in P]
 for f,cy in enumerate(faces):
  for i in cy:groups[ind[i]].append(f)
 X=np.concatenate((q,P[perm]));graph=[set() for _ in X]
 for i,fs in enumerate(groups):
  for f in fs:graph[f].add(n+i);graph[n+i].add(f)
 remaining=set(range(len(X)));remaining.remove(n);todo=[]
 while remaining:
  choices=[]
  for i in sorted(remaining):
   ds=sorted(graph[i]);d=len(ds)
   if d>3:continue
   ax=max(itertools.combinations(range(3),d),key=lambda a:abs(np.linalg.det(X[np.ix_(ds,a)]))) if d else ()
   A=X[np.ix_(ds,ax)];score=1./np.linalg.cond(A) if d else 2.
   choices.append(((priority[i] if priority is not None else score),-d,-i,i,ds,list(ax)))
  assert choices,'radial graph ordering failed'
  _,_,_,i,ds,ax=max(choices);todo.append([i,ds,ax]);remaining.remove(i)
  for j in ds:graph[j].remove(i)
  graph[i].clear()
 plan=todo[::-1];C=np.rint(X*grid).astype(np.int64).tolist()
 for i,ds,ax in plan:
  for k in ax:C[i][k]=0
 C[n]=[0,0,grid]
 return {'n_supports':n,'grid':grid,'controls':C,'groups':groups,'plan':plan,'vertex_order':perm,'faces':[[ind[i] for i in cy] for cy in faces]}
if __name__=='__main__':
 G=json.load(open(sys.argv[1]));raw,P=reconstruct(G);Path(sys.argv[2]).write_text(json.dumps(raw,sort_keys=True,separators=(',',':')))
