"""Replace the complete quadrilateral beside the residual saddle by a 3-link arc.
The two new points remain on the adjoining maximal facet; only true faces count.
"""
import sys,json,itertools,numpy as np
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path[:0]=[str(R),str(R/'parent_sources')]
from numeric import recover,mechanics,vertices,topology
from live_hull import census

def construct(q,P,fs,c,t1=1/3,t2=2/3,rboost=(0.,0.)):
 N=len(P);u,v=103,114;flat=72;removed=18;support=q[flat];nn=support/np.linalg.norm(support);hd=(1-support@c)/np.linalg.norm(support);foot=nn*hd;z=P-c;aa=z[u]-foot;bb=z[v]-foot;r0=np.linalg.norm(aa);r1=np.linalg.norm(bb);e=aa/r0;ca=np.clip(aa@bb/(r0*r1),-1,1);ang=np.arccos(ca);ee=(bb/r1-ca*e)/np.sin(ang)
 ws=[]
 for t,b in zip([t1,t2],rboost):
  rho=np.exp((1-t)*np.log(r0)+t*np.log(r1)+b);w=c+foot+rho*(np.cos(ang*t)*e+np.sin(ang*t)*ee);j=int(np.argmax(abs(support)));w[j]=(1-np.delete(support,j)@np.delete(w,j))/support[j];ws.append(w)
 pp=np.vstack([P,ws]);base=[];qq=[]
 for i,f in enumerate(fs):
  if i==removed:continue
  if i==flat:
   nf=[]
   for a,b in zip(f,f[1:]+f[:1]):
    nf.append(a)
    if a==u and b==v:nf.extend([N,N+1])
    if a==v and b==u:nf.extend([N+1,N])
   f=nf
  base.append(f);qq.append(q[i])
 choices=[[[u,69,N],[69,97,N],[97,N+1,N],[97,v,N+1]],[[u,69,N],[69,N+1,N],[69,97,N+1],[97,v,N+1]]]
 results=[]
 for new in choices:
  ff=[f.copy() for f in base];qn=list(qq)
  for f in new:
   if np.linalg.det(pp[f])<0:f=f[::-1]
   ff.append(f);qn.append(np.linalg.solve(pp[f],np.ones(3)))
  qn=np.array(qn);gaps=1-pp@qn.T
  try:rr=mechanics(qn,ff,P=pp,tol=1e-12);ref=census(qn,pp,ff,c)
  except Exception as e:continue
  results.append((rr,ref,qn,pp,ff))
 best=max(results,key=lambda t:t[0]['min_gap']);return best,{'angle':ang,'rho':[r0,r1],'growth3':(r1/r0)**(1/3)*np.cos(ang/3)-1,'chain_eta':[float((pp[a]-c)@(pp[b]-pp[a])/np.sum((pp[b]-pp[a])**2)) for a,b in [(u,N),(N,N+1),(N+1,v)]]}

if __name__=='__main__':
 from REPROPOSE import main
 main()
