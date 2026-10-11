"""Lossless compact encoding of rational contact generators.
Only free controls define the body. Small stored corrections to rounded dependent
coordinates recover the ORIGINAL complete generator bytes as well, not an alias.
"""
import json,sys,copy,hashlib
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def solve(A,b):
 M=[list(a)+[v] for a,v in zip(A,b)];n=len(A)
 for k in range(n):
  p=next(j for j in range(k,n) if M[j][k]);M[k],M[p]=M[p],M[k];d=M[k][k];M[k]=[v/d for v in M[k]]
  for j in range(n):
   if j!=k:
    d=M[j][k];M[j]=[v-d*w for v,w in zip(M[j],M[k])]
 return [r[-1] for r in M]
def free_indices(G):
 n=G['n_supports'];ax={i:a for i,d,a in G['plan']};return [(i,k) for i in range(n+len(G['groups'])) if i!=n for k in range(3) if k not in ax[i]]
def rounded(G):
 D=G['grid'];n=G['n_supports'];Y=[[F(x,D) for x in r] for r in G['controls']];Y[n]=[F(0),F(0),F(1)];done={n}
 for i,deps,axes in G['plan']:
  assert i not in done and set(deps)<=done;rest=[k for k in range(3) if k not in axes]
  if deps:
   M=[[Y[j][k] for k in axes] for j in deps];rhs=[1-sum(Y[j][k]*Y[i][k] for k in rest) for j in deps]
   for k,v in zip(axes,solve(M,rhs)):Y[i][k]=v
  done.add(i)
 assert len(done)==len(Y)
 return [[round(v*D) for v in row] for row in Y]
def encode(G):
 orig=B(G);meta={k:v for k,v in G.items() if k!='controls'};free=free_indices(G);base=rounded(G);cor=[[i,k,x-base[i][k]] for i,row in enumerate(G['controls']) for k,x in enumerate(row) if x!=base[i][k]];return dict(meta=meta,free=[G['controls'][i][k] for i,k in free],dependent_corrections=cor,original_bytes=len(orig),original_sha256=hashlib.sha256(orig).hexdigest())
def decode(data):
 G=copy.deepcopy(data['meta']);n=G['n_supports'];G['controls']=[[0,0,0] for _ in range(n+len(G['groups']))];G['controls'][n]=[0,0,G['grid']];free=free_indices(G);assert len(free)==len(data['free'])
 for (i,k),v in zip(free,data['free']):G['controls'][i][k]=v
 G['controls']=rounded(G)
 for i,k,d in data['dependent_corrections']:G['controls'][i][k]+=d
 b=B(G);assert len(b)==data['original_bytes'] and hashlib.sha256(b).hexdigest()==data['original_sha256'];return G
if __name__=='__main__':
 from pathlib import Path
 data=json.loads(Path(sys.argv[1]).read_text());G=decode(data);Path(sys.argv[2]).write_bytes(B(G));print('EXACT_ORIGINAL_GENERATOR_RECOVERED',data['original_sha256'])
