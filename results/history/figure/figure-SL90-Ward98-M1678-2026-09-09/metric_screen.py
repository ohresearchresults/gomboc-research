# Frozen finite discovery screen; exact promotion is separate.
import json,sys,random,math
import numpy as np
from fractions import Fraction as Q
from pathlib import Path
sys.set_int_max_str_digits(0)
a=json.loads(Path('A.json').read_bytes());raw=json.loads(Path('RAW.json').read_bytes())
p=np.array([[float(Q(x)) for x in v] for v in a['vertices']]);g=np.array([float(Q(x)) for x in a['centroid']]);p-=g
q=np.array(raw['I'],dtype=float)/float(raw['D']);z=q/(1-q@g)[:,None]
e=np.array([r[:2] for r in a['edges']],int);ep=np.array([r[2:] for r in a['edges']],int)
def directed(edges):
 out=np.concatenate([edges,edges[:,::-1]]);return out[np.lexsort((out[:,1],out[:,0]))]
eu=directed(e);es=directed(ep)
def primitives(X,edges,M):
 i,j=edges.T; r=X[i];d=X[i]-X[j]
 val=np.einsum('ij,ij->i',r@M,d)
 den=np.sqrt(np.einsum('ij,ij->i',r@M,r)*np.einsum('ij,ij->i',d@M,d))
 y=val/den
 starts=np.r_[0,np.where(np.diff(i))[0]+1]
 return np.minimum.reduceat(y,starts),float(np.min(np.abs(y)))
def score(B):
 M=B.T@B;N=np.linalg.inv(M)
 u,um=primitives(p,eu,M);s,sm=primitives(z,es,N)
 S=int(np.sum(s>1e-12));U=int(np.sum(u>1e-12))
 # Exclude the largest-radius physical/polar root for the deficit tie-break.
 ru=int(np.argmax(np.einsum('ij,ij->i',p@M,p)));rs=int(np.argmax(np.einsum('ij,ij->i',z@N,z)))
 fu=np.maximum(np.delete(u,ru)+1e-4,0);fs=np.maximum(np.delete(s,rs)+1e-4,0)
 loss=float(np.sum(fu*fu)+np.sum(fs*fs))
 return (S+U,max(S,U),loss),S,U,min(sm,um)
rng=random.Random(90990);best=None
for k in range(10001):
 A=np.eye(3,dtype=int) if k==0 else np.array([[rng.randrange(-32,33) for j in range(3)] for i in range(3)],int)
 aa=A.tolist();det=(aa[0][0]*(aa[1][1]*aa[2][2]-aa[1][2]*aa[2][1])-aa[0][1]*(aa[1][0]*aa[2][2]-aa[1][2]*aa[2][0])+aa[0][2]*(aa[1][0]*aa[2][1]-aa[1][1]*aa[2][0]))
 if not det:continue
 key,S,U,margin=score(A.astype(float))
 if margin<=1e-12 or S<1 or U<1:continue
 if best is None or key<best[0]:
  best=(key,aa,k,S,U,margin)
  print('BEST',best,flush=True)
  Path('metric_best.json').write_text(json.dumps(best,separators=(',',':')))
  if S==U==1: break
print('FINITE_SCREEN_COMPLETE',flush=True)
