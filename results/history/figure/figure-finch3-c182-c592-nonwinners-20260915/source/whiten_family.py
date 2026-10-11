"""Own-volume projective/metric search in a scale-conditioned body chart.
The whitening is a real affine material change, not an assigned centre.
Edge-projection fractions avoid the short-edge/cosine zero trap."""
import json,sys,argparse,numpy as np,radial
from fractions import Fraction as F
from pathlib import Path
import global_family as engine
from model import dot,cross,norm,divide,HERE
# Reuse the complete differentiable family with both denominators changed to edge squared.
src=Path(__file__).with_name('global_family.py').read_text()
head=src[src.index('class Global:'):src.index('\ndef run(')]
head=head.replace('u,du=divide(v,ll*rr,dv,dll*rr[:,None]+drr*ll[:,None])','u,du=divide(v,ll*ll,dv,2*dll*ll[:,None])')
head=head.replace('fv,df=divide(v,ll*rr,dv,dll*rr[:,None]+drr*ll[:,None])','fv,df=divide(v,ll*ll,dv,2*dll*ll[:,None])')
exec(compile(head,'eta_family_derived','exec'),globals())
class White(Global):
 def __init__(self,nodes=False):
  from quotient_global import Body
  import quotient_global
  quotient_global.SOURCE=SOURCE;B=Body();self.__dict__.update(B.__dict__)
  P=self.P;T=P[self.tris];dt=np.einsum('ni,ni->n',T[:,0],np.cross(T[:,1],T[:,2]));D=dt.sum();g=np.einsum('n,ni->i',dt,T.sum(axis=1))/(4*D)
  Z=P-g;C=Z.T@Z/len(Z);w,U=np.linalg.eigh(C);A=(U*(1/np.sqrt(w)))@U.T;A/=np.max(np.linalg.norm(Z@A.T,axis=1));self.P=Z@A.T;self.q=np.linalg.solve(A.T,(self.q/(1-self.q@g)[:,None]).T).T;self.last=None;self.reslast=None
  Path(TAG+'_WHITEN.json').write_text(json.dumps({'source':SOURCE,'A':A.tolist(),'old_centroid':g.tolist()},sort_keys=True,separators=(',',':')))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--start',default='QUOT_11_1_G6.json');p.add_argument('--tag',default='WHITE1');p.add_argument('--starts',type=int,default=35);p.add_argument('--seed',type=int,default=59283);p.add_argument('--maxeval',type=int,default=300);a=p.parse_args();SOURCE=a.start;TAG=a.tag;engine.Global=White;engine.run(TAG,a.starts,a.seed,a.maxeval,False,None)
