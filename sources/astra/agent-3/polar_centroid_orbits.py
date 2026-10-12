"""Physical projective orbits with polarity and actual uniform-centroid recentering.
Each half step is a different homogeneous solid, not a transported density.
Canonical incidence is preserved projectively. A saved matrix P embeds either
the exact base K or its exact polar; supports transform by D P^{-T} D.
"""
import argparse,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from gmpy2 import mpq
from support_geometry import escape
from persistence_birth import bars_loss
D=np.diag([1.,1.,1.,-1.])
def mesh(points,faces):
 T=np.array([(f[0],f[k],f[k+1]) for f in faces for k in range(1,len(f)-1)]);owners={}
 for i,f in enumerate(faces):
  for j,k in zip(f,f[1:]+f[:1]):owners.setdefault(tuple(sorted((j,k))),[]).append(i)
 assert all(len(v)==2 for v in owners.values())
 return dict(points=points,faces=faces,T=T,edges=np.array(list(owners)),dual_edges=np.array(list(owners.values())))
def base(path):
 a=json.loads(Path(path).read_text());X=np.array([[float(mpq(v)) for v in row] for row in a['raw_vertices']]);Q=np.array([[float(mpq(v)/mpq(h)) for v in n] for n,h in zip(a['normals'],a['offsets'])]);M=mesh(X,a['faces']);ff=[]
 for i in range(len(X)):
  adjacent={f for f,cy in enumerate(a['faces']) if i in cy};links={f:[] for f in adjacent}
  for (u,v),(j,k) in zip(M['edges'],M['dual_edges']):
   if i in [u,v]:links[j].append(int(k));links[k].append(int(j))
  start=min(adjacent);cy=[start];prev=-1;current=start
  while True:
   choices=links[current];nxt=choices[0] if choices[0]!=prev else choices[1]
   if nxt==start:break
   assert nxt not in cy;cy.append(nxt);prev,current=current,nxt
  assert len(cy)==len(adjacent);pts=Q[cy];area=np.sum(np.cross(pts,np.roll(pts,-1,axis=0)),axis=0)
  if area@X[i]<0:cy.reverse()
  ff.append(cy)
 return [M,mesh(Q,ff)]
def mass(X,T):
 a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];v=np.einsum('ic,ic->i',a,np.cross(b,c));vol=v.sum()/6;assert vol>0;g=np.sum(v[:,None]*(a+b+c),axis=0)/(4*v.sum());return g,vol
def evaluate(bases,b,P):
 B=bases[b];C=bases[1-b];hom=np.column_stack((B['points'],np.ones(len(B['points']))))@P.T
 if min(hom[:,-1])<=0:raise ValueError('projective horizon intersects exact-base vertex proposal')
 X=hom[:,:3]/hom[:,-1,None];g,V=mass(X,B['T']);T=np.eye(4);T[:3,3]=-g;Pc=T@P;Pc/=Pc[3,3];X-=g;Pd=D@np.linalg.inv(Pc).T@D;qh=np.column_stack((C['points'],np.ones(len(C['points']))))@Pd.T
 if min(qh[:,-1])<=0:raise ValueError('centred polar horizon unresolved')
 Q=qh[:,:3]/qh[:,-1,None];su=escape(X)[0];ss=escape(Q)[0];U=int(np.sum(su<0));S=int(np.sum(ss<0));return Pc,Pd,X,Q,dict(S=S,U=U,V=len(X),E=len(B['edges']),F=len(Q),C=2*len(B['edges']),centroid_shift=g.tolist(),volume=float(V))
def run(paths,out,restarts,steps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);rng=np.random.default_rng(982851);summary=[];start=time.time()
 for source in paths:
  bases=base(source);tag=Path(source).parent.parent.name+'_'+hashlib.sha256(str(source).encode()).hexdigest()[:8];dest=out/tag;dest.mkdir();best=10000;hist=[];(dest/'source.json').write_text(json.dumps(dict(audit_path=str(Path(source).resolve()),audit_sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest()),indent=2))
  for run in range(restarts):
   P=np.eye(4);b=run%2;amp=[0.,.04,.12,.3][run%4]
   for it in range(steps):
    if amp:
     A=rng.normal(size=(3,3));A=(A+A.T)/2;A-=np.eye(3)*np.trace(A)/3;T=np.eye(4);T[:3,:3]=expm(amp*A);P=T@P
    P,Pd,X,Q,info=evaluate(bases,b,P);info.update(restart=run,step=it,dual=b,amplitude=amp);score=info['S']+info['U']
    if score<best:
     best=score;np.savez(dest/'best.npz',P=P,dual=b,X=X,Q=Q);(dest/'best.json').write_text(json.dumps(info,indent=2))
    if score<=4:
     pv=bars_loss(X,bases[b]['edges'])[2];qv=bars_loss(Q,bases[1-b]['edges'])[2];info.update(Pmax=max(pv,default=0.),Qmax=max(qv,default=0.))
    if info['S']==info['U']==1:
     p=dest/f'potential_r{run}_i{it}';p.mkdir();np.savez(p/'embedding.npz',P=P,dual=b);np.save(p/'vertices.npy',X);np.save(p/'supports.npy',Q);(p/'nomination.json').write_text(json.dumps(info,indent=2));(p/'source.json').write_text((dest/'source.json').read_text());print('POLAR_ORBIT_POTENTIAL_OWN110_REQUIRES_EXACT',p,info,flush=True)
    hist.append(info);P=Pd/Pd[3,3];b=1-b
  (dest/'history.json').write_text(json.dumps(hist,indent=2));row=dict(source=str(source),best_counts=best,seconds=time.time()-start,states=len(hist));summary.append(row);(out/'summary.json').write_text(json.dumps(summary,indent=2));print('POLAR_ORBIT_SOURCE',row,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('out');p.add_argument('sources',nargs='+');p.add_argument('--restarts',type=int,default=24);p.add_argument('--steps',type=int,default=32);a=p.parse_args();run(a.sources,a.out,a.restarts,a.steps)
