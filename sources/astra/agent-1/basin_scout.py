"""Finite whole-polar-basin deformations with physical projective mass closure."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,pathlib,json,time,argparse
from geometry import halfspace_mesh,census
from persistence_search import pairs,polar_edges
from selfpolar_search import mass

def balance(Q):
 m=halfspace_mesh(Q);X=m['X'];tri=m['triangles'];total=np.zeros(3)
 for i in range(25):
  V,g,M=mass(X,tri)
  if np.linalg.norm(g)<1e-11:break
  d=np.linalg.solve(5*M-4*np.outer(g,g),g);ok=False
  for k in range(20):
   db=d*2**-k;den=1+X@db
   if den.min()<.05:continue
   Y=X/den[:,None];_,gg,_=mass(Y,tri)
   if np.linalg.norm(gg)<np.linalg.norm(g):X=Y;total+=db;ok=True;break
  if not ok:raise ValueError('projective mass closure stalled')
 if np.linalg.norm(mass(X,tri)[1])>1e-9:raise ValueError('unclosed moment')
 return Q+total,total

def dying_component(Q):
 m=halfspace_mesh(Q);q=Q/(1-Q@m['g'])[:,None];edges=polar_edges(m);pp,h=pairs(q,edges);rr=(q*q).sum(1);de=1-h[pp[:,1]]/rr[pp[:,0]];pk=int(np.argmax(de));target=pp[pk,1]
 par=np.arange(len(Q));sets=[{i} for i in range(len(Q))]
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for k in np.argsort(-h,kind='stable'):
  i,j=edges[k];a,b=root(i),root(j)
  if a==b:continue
  if rr[a]<rr[b]:a,b=b,a
  if k==target:return np.array(sorted(sets[b]),int),edges[k],int(b),float(h[k])
  par[b]=a;sets[a]|=sets[b]
 raise ValueError('component missing')

def score(Q):
 m=halfspace_mesh(Q);p=m['X']-m['g'];q=Q/(1-Q@m['g'])[:,None];bs=[]
 for x,e in [(p,m['edges']),(q,polar_edges(m))]:
  pp,h=pairs(x,e);r=(x*x).sum(1);bs.append((1-h[pp[:,1]]/r[pp[:,0]]).tolist())
 value=sum(np.log1p(np.array(b)/.001).sum()*.001 for b in bs)
 return dict(score=float(value),P=bs[0],Q=bs[1],**census(m))

def run(input,out):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);Q=np.load(input)['Q'];m=halfspace_mesh(Q);Q=Q/(1-Q@m['g'])[:,None]
 comp,edge,root,h=dying_component(Q);print('COMPONENT',comp.tolist(),'edge',edge.tolist(),'root',root,'death',h,flush=True)
 a=Q[edge[0]];d=Q[edge[1]]-a;t=np.clip(-a@d/(d@d),0,1);foot=a+t*d
 targets={'foot':foot,'outside':Q[next(int(v) for v in edge if v not in comp)],'zero':np.zeros(3),'mean':Q[comp].mean(0)}
 records=[];best=1e9
 for mode,target in targets.items():
  for t in np.r_[np.linspace(0,.9,31),.93,.95,.97,.99,.999]:
   R=Q.copy();R[comp]=(1-t)*R[comp]+t*target
   try:
    R,b=balance(R);s=score(R);row=dict(mode=mode,t=float(t),projective_shift=b.tolist(),**s);records.append(row)
    if s['score']<best:
     best=s['score'];np.savez(out/'best.npz',Q=R);(out/'best.json').write_text(json.dumps(row,indent=2));print('BEST',mode,t,best,s['S'],s['U'],s['E'],flush=True)
    if s['S']==s['U']==1:np.savez(out/'NOMINATION110.npz',Q=R);print('NOMINATION110_REQUIRES_EXACT',flush=True);return
   except Exception as e:records.append(dict(mode=mode,t=float(t),error=str(e)))
  (out/'history.json').write_text(json.dumps(records,indent=2))
 (out/'component.json').write_text(json.dumps({'indices':comp.tolist(),'edge':edge.tolist(),'root':root,'death':h},indent=2))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);a=ap.parse_args();run(a.input,a.out)
