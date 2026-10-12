"""Per-node common-denominator contact controls. Exact rational reconstruction."""
from fractions import Fraction as F
from math import gcd,lcm
from RECONSTRUCT import solve

def points(d):
 if 'denominators' in d:X=[[F(v,D) for v in row] for row,D in zip(d['controls'],d['denominators'])]
 else:X=[[F(v,d['grid']) for v in row] for row in d['controls']]
 n=d['n_supports'];X[n]=[F(0),F(0),F(1)];done={n};edges=set()
 for i,deps,axes in d['plan']:
  assert i not in done and set(deps)<=done and len(deps)==len(axes)<=3
  rest=[k for k in range(3) if k not in axes]
  if deps:
   ans=solve([[X[j][k] for k in axes] for j in deps],[F(1)-sum(X[j][k]*X[i][k] for k in rest) for j in deps])
   for k,v in zip(axes,ans):X[i][k]=v
  for j in deps:
   assert (i<n)!=(j<n) and sum(a*b for a,b in zip(X[i],X[j]))==1;edges.add(tuple(sorted((i,j))))
  done.add(i)
 assert done==set(range(len(X)))
 assert edges=={tuple(sorted((i,n+j))) for j,ids in enumerate(d['groups']) for i in ids}
 return X

def recover(d):
 X=points(d);H=[]
 for row in X[:d['n_supports']]:
  D=lcm(*(v.denominator for v in row));r=[int(v*D) for v in row]+[D];G=gcd(*r);H.append([v//G for v in r])
 assert len(set(map(tuple,H)))==len(H)
 return {'H':H}
