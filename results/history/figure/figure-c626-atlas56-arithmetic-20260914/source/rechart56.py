"""A depth-three core-first contact chart of the literal doubly merged C626 body.
Six core supports are built from free points; their dependent points are chosen
among the one-core leaves, so no core support depends on another core support.
"""
import argparse,itertools,json
from pathlib import Path
from fractions import Fraction as F
from math import lcm
import numpy as np
from rational56 import points
from simplify56 import build,screen

def rechart(d,chosen=(142,151,164,174,175)):
 n=d['n_supports'];X=points(d);xf=np.array(X,float);M=len(X);groups=d['groups'];sowners=[[n+j for j,group in enumerate(groups) if i in group] for i in range(n)]
 core=[i for i,g in enumerate(sowners) if len(g)>3];assert core==[26,54,76,78,79,90]
 B=set(chosen)|{153,168,170};assert len(B)==8
 assert all(sum(v in sowners[i] for i in core)==1 for v in B)
 plan=[]
 for v in range(n+1,M-1):
  if v not in B:plan.append([v,[],[]])
 for i in core:
  deps=[v for v in sowners[i] if v not in B];assert len(deps)==3
  plan.append([i,deps,[0,1,2]])
 for v in sorted(B):
  i=next(i for i in core if v in sowners[i]);ax=int(np.argmax(np.abs(xf[i])));plan.append([v,[i],[ax]])
 for i in range(n):
  if i in core or i==18:continue
  deps=[v for v in sowners[i] if v!=179];assert len(deps)<=3
  axes=max(itertools.combinations(range(3),len(deps)),key=lambda ax:abs(np.linalg.det(xf[np.ix_(deps,ax)])) if deps else 1)
  plan.append([i,deps,list(axes)])
 plan.extend([[179,[16,71,94],[0,1,2]],[18,[179],[int(np.argmax(np.abs(xf[179])))]]])
 z=dict(n_supports=n,groups=groups,plan=plan,controls=[[0,0,0] for _ in X],denominators=[1]*M)
 z['controls'][n]=[0,0,1]
 for i,deps,axes in plan:
  rest=[k for k in range(3) if k not in axes];D=lcm(*(X[i][k].denominator for k in rest));z['denominators'][i]=D
  for k in rest:z['controls'][i][k]=int(X[i][k]*D)
 # This is an exactly identical reparametrization before any approximation.
 assert points(z)==X
 dep={n:0}
 for i,deps,axes in plan:dep[i]=1+max((dep[v] for v in deps),default=-1)
 assert max(dep.values())==3
 return z,xf
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',default='PARENT_G8.json');p.add_argument('--faces',default='FACES.json');p.add_argument('--chosen',type=int,nargs=5,default=[142,151,164,174,175]);p.add_argument('--eps',type=float,default=1e-8);p.add_argument('--out',required=True);a=p.parse_args();d=json.loads(Path(a.source).read_text());z,X=rechart(d,tuple(a.chosen));z=build(z,X,a.eps);out=Path(a.out);out.mkdir(parents=True,exist_ok=False);(out/'GENERATOR.json').write_text(json.dumps(z,sort_keys=True,separators=(',',':')));r=screen(z,json.loads(Path(a.faces).read_text()));(out/'NUMERICAL.json').write_text(json.dumps(r,sort_keys=True,separators=(',',':')));print('RECHART',a.chosen,a.eps,r,flush=True)
