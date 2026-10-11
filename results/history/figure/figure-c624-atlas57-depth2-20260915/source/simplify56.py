"""Simultaneous low-height rational approximation of each independent contact row.
The exact endpoint still requires two full exact audits and cold replay.
"""
import argparse,json,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from numeric import recover,mechanics

def common_approx(values,eps,limit=30000000):
 # First denominator whose nearest numerators are all inside their intervals.
 x=np.array(values,float)
 if len(x)==0:return [],1
 for lo in range(1,limit+1,50000):
  D=np.arange(lo,min(lo+50000,limit+1),dtype=np.int64)
  y=D[:,None]*x;N=np.rint(y)
  good=np.all(np.abs(N-y)<=eps*D[:,None],axis=1);ids=np.flatnonzero(good)
  if len(ids):
   j=int(ids[0]);q=int(D[j]);p=N[j].astype(np.int64).tolist()
   # Exact qualification against decimal centres and exact decimal tolerance.
   if all(abs(F(a,q)-F(str(b)))<=F(str(eps)) for a,b in zip(p,values)):return p,q
 # The fallback is complete, labelled, and never silently relaxes the tolerance.
 q=int(np.ceil(1/(2*eps)));p=np.rint(q*x).astype(np.int64).tolist();return p,q

def build(d,X,eps):
 z=json.loads(json.dumps(d));z.pop('grid',None);z['controls']=[[0,0,0] for _ in X];z['denominators']=[1]*len(X);z['controls'][d['n_supports']]=[0,0,1]
 for i,deps,axes in z['plan']:
  rest=[k for k in range(3) if k not in axes];p,q=common_approx([X[i,k] for k in rest],eps)
  for k,v in zip(rest,p):z['controls'][i][k]=v
  z['denominators'][i]=q
 return z

def screen(z,faces):
 X=np.array(z['controls'],float)/np.array(z['denominators'])[:,None]
 return mechanics(recover(z,X)[:z['n_supports']],faces,tol=1e-13)

def main():
 p=argparse.ArgumentParser();p.add_argument('--source',default='PARENT_G8.json');p.add_argument('--faces',default='FACES.json');p.add_argument('--npz');p.add_argument('--eps',type=float,required=True);p.add_argument('--out',required=True);a=p.parse_args()
 d=json.loads(Path(a.source).read_text());faces=json.loads(Path(a.faces).read_text());X=recover(d) if not a.npz else np.load(a.npz)['X'];t=time.monotonic();z=build(d,X,a.eps);out=Path(a.out);out.mkdir(parents=True,exist_ok=False);(out/'GENERATOR.json').write_text(json.dumps(z,sort_keys=True,separators=(',',':')));r=screen(z,faces);(out/'NUMERICAL.json').write_text(json.dumps(r,sort_keys=True,separators=(',',':')));print('END',a.eps,time.monotonic()-t,r,flush=True)
if __name__=='__main__':main()
