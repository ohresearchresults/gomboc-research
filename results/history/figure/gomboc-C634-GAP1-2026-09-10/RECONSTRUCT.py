"""Exact alternating contact atlas with explicit rational incidence right-side offsets.
The physical body is the intersection of its recovered support halfspaces.
Offset auxiliary nodes are not declared to be physical vertices; audit the real hull.
"""
import json,sys
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
sys.set_int_max_str_digits(0)

def solve(A,b):
 n=len(A);M=[list(a)+[v] for a,v in zip(A,b)]
 for k in range(n):
  p=next((j for j in range(k,n) if M[j][k]),None);assert p is not None,'singular contact minor'
  M[k],M[p]=M[p],M[k];d=M[k][k];M[k]=[x/d for x in M[k]]
  for j in range(n):
   if j!=k:
    d=M[j][k];M[j]=[x-d*y for x,y in zip(M[j],M[k])]
 return [row[-1] for row in M]

def recover(data):
 D=data['grid'];n=data['n_supports'];assert isinstance(D,int) and D>0
 X=[[F(v,D) for v in row] for row in data['controls']];assert 0<n<len(X)
 offsets={}
 for row in data.get('rhs_offsets',[]):
  assert len(row)==4 and all(isinstance(x,int) for x in row)
  i,j,num,den=row;assert 0<=i<len(X) and 0<=j<len(X) and i!=j and den>0
  key=tuple(sorted((i,j)));assert key not in offsets
  offsets[key]=F(num,den)
 X[n]=[F(0),F(0),F(1)];done={n};edges=set()
 for i,deps,axes in data['plan']:
  assert i not in done and set(deps)<=done and len(deps)==len(axes)<=3
  assert len(set(axes))==len(axes) and set(axes)<={0,1,2}
  if deps:
   rest=[k for k in range(3) if k not in axes];A=[[X[j][k] for k in axes] for j in deps];b=[F(1)-offsets.get(tuple(sorted((i,j))),F(0))-sum(X[j][k]*X[i][k] for k in rest) for j in deps];values=solve(A,b)
   for k,v in zip(axes,values):X[i][k]=v
  for j in deps:
   assert (i<n)!=(j<n);assert sum(a*b for a,b in zip(X[i],X[j]))==1-offsets.get(tuple(sorted((i,j))),F(0));edges.add(tuple(sorted((i,j))))
  done.add(i)
 assert done==set(range(len(X)))
 intended={tuple(sorted((i,n+j))) for j,ids in enumerate(data['groups']) for i in ids};assert edges==intended and set(offsets)<=intended
 H=[]
 for row in X[:n]:
  den=lcm(*(v.denominator for v in row));num=[int(v*den) for v in row];gg=gcd(*num,den);H.append([v//gg for v in num]+[den//gg])
 assert len(set(map(tuple,H)))==len(H)
 return {'H':H}
if __name__=='__main__':
 data=json.loads(Path(sys.argv[1]).read_text());Path(sys.argv[2]).write_text(json.dumps(recover(data),sort_keys=True,separators=(',',':')))
