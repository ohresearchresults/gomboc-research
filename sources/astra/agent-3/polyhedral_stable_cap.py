"""Literal point additions to a general exact polyhedron with maximal faces.
Visible old facets disappear; horizon edges receive triangles. Kept polygon
facets stay intact. All new filled volume and its actual centroid are included.
"""
import argparse,json,time,hashlib
from pathlib import Path
from gmpy2 import mpq as Fraction
import numpy as np
from persistence_birth import bars_loss
from support_geometry import escape

class Cap:
 def __init__(self,source,target='stable'):
  self.source=Path(source);a=json.loads((self.source/'audit.json').read_text());self.a=a;self.g0=np.array([float(Fraction(v))for v in a['raw_centroid']]);X=np.array([[float(Fraction(v))for v in x]for x in a['raw_vertices']]);X-=self.g0;self.scale=float(np.max(np.linalg.norm(X,axis=1)));self.X=X/self.scale;self.faces=a['faces'];N=np.array([[float(Fraction(v)/Fraction(h))for v in n]for n,h in zip(a['normals'],a['offsets'])]);N/=np.linalg.norm(N,axis=1)[:,None];self.N=N;self.h=np.array([n@self.X[f[0]]for n,f in zip(N,self.faces)]);self.owners={tuple(e):[]for e in a['edges']}
  for f,cy in enumerate(self.faces):
   for i,j in zip(cy,cy[1:]+cy[:1]):self.owners[tuple(sorted((i,j)))].append(f)
  if target=='stable':
   H=N/self.h[:,None];s=a['stable_face_ids'];assert len(s)==2;self.junior=int(s[np.argmin(np.sum(H[s]**2,axis=1))]);self.normal=N[self.junior];self.foot=self.normal*self.h[self.junior];v=np.eye(3)[np.argmin(abs(self.normal))];v-=self.normal*(v@self.normal);v/=np.linalg.norm(v)
  else:
   assert len(a['saddle_edges'])==1;i,j=a['saddle_edges'][0];v=self.X[j]-self.X[i];t=-self.X[i]@v/(v@v);assert 0<t<1;self.foot=self.X[i]+t*v;self.normal=self.foot/np.linalg.norm(self.foot);v/=np.linalg.norm(v)
  self.B=np.column_stack((v,np.cross(self.normal,v),self.foot))
 def body(self,t):
  p=self.foot+self.B@t;visible=self.N@p>self.h;points=np.vstack((self.X,p));k=len(self.X);faces=[cy.copy()for f,cy in enumerate(self.faces)if not visible[f]];face_sources=[dict(type='old',index=f)for f in range(len(self.faces))if not visible[f]]
  for (i,j),adj in self.owners.items():
   if visible[adj[0]]==visible[adj[1]]:continue
   tri=[i,j,k];n=np.cross(points[j]-points[i],p-points[i])
   if n@points[i]<0:tri.reverse()
   faces.append(tri);face_sources.append(dict(type='cap',edge=[i,j]))
  active=sorted({i for f in faces for i in f});mapping={a:b for b,a in enumerate(active)};X=points[active];faces=[[mapping[i]for i in f]for f in faces];T=np.array([(f[0],f[j],f[j+1])for f in faces for j in range(1,len(f)-1)]);a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));V=v6.sum()/6;assert V>0;g=np.sum(v6[:,None]*(a+b+c),axis=0)/(4*v6.sum());Z=X-g;N=np.array([np.cross(X[f[1]]-X[f[0]],X[f[2]]-X[f[0]])for f in faces]);h=np.array([n@Z[f[0]]for n,f in zip(N,faces)]);assert min(h)>0;H=N/h[:,None];own={}
  for f,cy in enumerate(faces):
   for i,j in zip(cy,cy[1:]+cy[:1]):own.setdefault(tuple(sorted((i,j))),[]).append(f)
  assert all(len(v)==2 for v in own.values());E=len(own);assert len(X)-E+len(faces)==2;pe=np.array(list(own));qe=np.array(list(own.values()));return dict(X=X,Z=Z,H=H,faces=faces,face_sources=face_sources,active_point_ids=active,pe=pe,qe=qe,volume=V,centroid=g,point=p,visible=np.flatnonzero(visible),V=len(X),E=E,F=len(faces))
 def score(self,t):
  g=self.body(t);lp,_,P=bars_loss(g['Z'],g['pe'],.03);lq,_,Q=bars_loss(g['H'],g['qe'],.03);info=dict(Pmax=max(P,default=0.),Qmax=max(Q,default=0.),P_count=len(P),Q_count=len(Q),S=int(np.sum(escape(g['H'])[0]<0)),U=int(np.sum(escape(g['Z'])[0]<0)),V=g['V'],E=g['E'],F=g['F'],C_2E=2*g['E'],VplusEplusF=g['V']+g['E']+g['F'],loss=lp+lq);return g,info

def run(source,out,seed,trials,target='stable'):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);c=Cap(source,target);rng=np.random.default_rng(seed);rows=[];best={};start=time.time();(out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),audit_sha256=hashlib.sha256((Path(source)/'audit.json').read_bytes()).hexdigest(),scale=c.scale,centroid=c.g0.tolist(),foot=c.foot.tolist(),basis=c.B.tolist(),seed=seed,target=target,formula='convex hull(original exact body union {exact_centroid + scale * saved_normalized_point})'),indent=2));guard='Pmax'if target=='stable'else'Qmax';objective='Qmax'if target=='stable'else'Pmax';prefix='P'if target=='stable'else'Q'
 for it in range(trials):
  t=np.r_[rng.normal(size=2)*rng.choice([.01,.05,.15,.5]),np.exp(rng.uniform(np.log(1e-5),np.log(3.)))];g,info=c.score(t)
  if info['VplusEplusF']>=500:continue
  row=dict(it=it,controls=t.tolist(),point=g['point'].tolist(),visible_facets=g['visible'].tolist(),**info);rows.append(row)
  for lim in [1e-10,1e-7,1e-5,.001,.01,.1,1.]:
   if info[guard]<=lim:
    key=f'{prefix}{lim:g}'
    if info[objective]<best.get(key,{objective:np.inf})[objective]:best[key]=row;(out/('best_'+key+'.json')).write_text(json.dumps(row,indent=2))
  if info['S']==info['U']==1:(out/f'potential{it}.json').write_text(json.dumps(row,indent=2));print('GENERAL_CAP_POTENTIAL_REQUIRES_EXACT',row,flush=True)
  if it%1000==0:print('GENERAL_CAP',it,{k:(v['Pmax'],v['Qmax'],v['E'])for k,v in best.items()},flush=True)
 (out/'trials.json').write_text(json.dumps(rows,indent=2));(out/f'best_by_{prefix}.json').write_text(json.dumps(best,indent=2));print('GENERAL_CAP_DONE',out,len(rows),time.time()-start,{k:(v['Pmax'],v['Qmax'],v['E'])for k,v in best.items()},flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--seed',type=int,default=80201);p.add_argument('--trials',type=int,default=6000);p.add_argument('--target',choices=['stable','saddle'],default='stable');a=p.parse_args();run(a.source,a.out,a.seed,a.trials,a.target)
