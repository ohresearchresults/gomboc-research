"""Literal halfspace clips across the junior unstable basin of an exact body.

The original maximal faces remain in their original planes. Clipped triangles
can become true quads; the cap is one maximal face. A candidate is not charged
for its integration triangulation. No angular coplanarity merging is used.
"""
import argparse,json,time,hashlib
from pathlib import Path
from gmpy2 import mpq as Fraction
import numpy as np
from scipy.optimize import differential_evolution,minimize
from persistence_birth import bars_loss
from support_geometry import escape

class Clip:
 def __init__(self,source):
  self.source=Path(source);self.a=json.loads((self.source/'audit.json').read_text());a=self.a;X=np.array([[float(Fraction(t)) for t in row] for row in a['raw_vertices']]);self.center=np.array([float(Fraction(t)) for t in a['raw_centroid']]);X-=self.center;self.scale=float(np.max(np.linalg.norm(X,axis=1)));self.X=X/self.scale;self.faces=a['faces'];self.edges=np.array(a['edges']);bars=json.loads((self.source/'exact_bars.json').read_text());assert len(bars['P'])==1 and not bars['Q'];self.junior=int(bars['P'][0]['peak']);u=self.X[self.junior];self.n0=u/np.linalg.norm(u);v=np.eye(3)[np.argmin(abs(self.n0))];v-=self.n0*(v@self.n0);v/=np.linalg.norm(v);self.B=np.column_stack((v,np.cross(self.n0,v)));normal_rows=[tuple(map(Fraction,n))for n in a['normals']];self.N=np.array([[float(v/max(map(abs,n)))for v in n]for n in normal_rows]);self.N/=np.linalg.norm(self.N,axis=1)[:,None]
  for f,n in zip(self.faces,self.N):assert np.sum(np.cross(self.X[f],np.roll(self.X[f],-1,axis=0)),axis=0)@n>0
 def body(self,t):
  n=self.n0+self.B@t[:2];n/=np.linalg.norm(n);h=float(t[2]*(n@self.X[self.junior]));assert h>0;d=self.X@n-h;inside=d<=0;old=np.flatnonzero(inside);lookup={int(i):k for k,i in enumerate(old)};pts=list(self.X[old]);crossings={};cap=[lookup[int(i)] for i in np.flatnonzero(d==0)]
  for i,j in self.edges:
   if d[i]*d[j]<0:
    k=len(pts);crossings[(int(i),int(j))]=k;cap.append(k);pts.append(self.X[i]+d[i]/(d[i]-d[j])*(self.X[j]-self.X[i]))
  faces=[];normals=[]
  for f,nf in zip(self.faces,self.N):
   cyc=[]
   for i,j in zip(f,f[1:]+f[:1]):
    if inside[i]:cyc.append(lookup[i])
    key=tuple(sorted((i,j)))
    if key in crossings:cyc.append(crossings[key])
   if len(cyc)>=3:faces.append(cyc);normals.append(nf)
  X=np.array(pts);v=np.eye(3)[np.argmin(abs(n))];v-=n*(v@n);v/=np.linalg.norm(v);w=np.cross(n,v);middle=X[cap].mean(0);aa=np.arctan2((X[cap]-middle)@w,(X[cap]-middle)@v);cap=[cap[k] for k in np.argsort(aa)];faces.append(cap);normals.append(n);normals=np.array(normals);T=np.array([(f[0],f[k],f[k+1]) for f in faces for k in range(1,len(f)-1)]);a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));vol=v6.sum()/6;assert vol>0;g=np.sum(v6[:,None]*(a+b+c),axis=0)/(4*v6.sum());Z=X-g;offset=np.array([normal@X[f[0]] for normal,f in zip(normals,faces)]);hh=offset-normals@g;assert min(hh)>0;H=normals/hh[:,None];owners={}
  for i,f in enumerate(faces):
   for j,k in zip(f,f[1:]+f[:1]):owners.setdefault(tuple(sorted((j,k))),[]).append(i)
  assert all(len(v)==2 for v in owners.values());E=len(owners);assert len(X)-E+len(faces)==2;pe=np.array(list(owners));qe=np.array(list(owners.values()));return dict(X=X,Z=Z,H=H,faces=faces,pe=pe,qe=qe,centroid=g,volume=vol,n=n,h=h,V=len(X),E=E,F=len(faces))
 def score(self,t,eta=.03):
  g=self.body(t);lp,_,P=bars_loss(g['Z'],g['pe'],eta);lq,_,Q=bars_loss(g['H'],g['qe'],eta);cl=dict(S=int(np.sum(escape(g['H'])[0]<0)),U=int(np.sum(escape(g['Z'])[0]<0)));info=dict(**cl,V=g['V'],E=g['E'],F=g['F'],C_2E=2*g['E'],VplusEplusF=g['V']+g['E']+g['F'],P=P,Q=Q,Pmax=max(P,default=0.),Qmax=max(Q,default=0.),loss=lp+lq);return lp+lq,g,info

def run(source,out,seed,iterations):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);c=Clip(source);(out/'definition.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),audit_sha256=hashlib.sha256((Path(source)/'audit.json').read_bytes()).hexdigest(),scale=c.scale,center=c.center.tolist(),junior=c.junior,seed=seed,formula='base exact body intersect {n dot ((x-own_centroid)/scale) <= h}',parameter_normal='normalize(junior_unit_direction + tangent_basis @ t[:2])',parameter_offset='t[2] * n dot normalized_junior_vertex'),indent=2));np.save(out/'basis.npy',c.B);np.save(out/'n0.npy',c.n0);best=np.inf;calls=0;start=time.time();bestclass={}
 def fun(t):
  nonlocal best,calls
  calls+=1;v,g,info=c.score(t);admissible=34<=2*g['E']<500 and g['V']+g['E']+g['F']<500
  if not admissible:v+=100+max(0,2*g['E']-498)
  def save(stem):
   np.save(out/(stem+'.npy'),g['X']);np.save(out/(stem+'_controls.npy'),t);(out/(stem+'.json')).write_text(json.dumps(dict(info,controls=np.array(t).tolist(),normal=g['n'].tolist(),offset=g['h'],calls=calls,seconds=time.time()-start),indent=2))
  if admissible and v<best:best=v;save('best')
  if admissible and info['S']<=2 and info['U']<=2:
   key=f'S{info["S"]}U{info["U"]}'
   if v<bestclass.get(key,np.inf):bestclass[key]=v;save('best_'+key)
  if admissible and info['S']==info['U']==1:save('potential'+str(calls));print('CAP_CLIP_POTENTIAL_REQUIRES_EXACT',out,info,flush=True)
  if calls%5000==0:print('CAP_CLIP',out,calls,best,bestclass,flush=True)
  return v
 rng=np.random.default_rng(seed);pop=np.column_stack((rng.uniform(-2,2,size=(72,2)),rng.uniform(.1,.9999,size=72)));pop[0]=[0,0,.99];bounds=[(-3.,3.),(-3.,3.),(.03,.999999)];de=differential_evolution(fun,bounds,seed=seed,init=pop,maxiter=iterations,polish=False,tol=1e-10,recombination=.8,mutation=(.4,1.2));r=minimize(fun,np.load(out/'best_controls.npy'),method='Nelder-Mead',bounds=bounds,options=dict(maxiter=3000,xatol=1e-10,fatol=1e-11));(out/'termination.json').write_text(json.dumps(dict(global_message=de.message,local_message=r.message,calls=calls,seconds=time.time()-start,bestclass=bestclass),indent=2));print('CAP_CLIP_DONE',out,best,bestclass,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--seed',type=int,default=75800);p.add_argument('--iterations',type=int,default=700);a=p.parse_args();run(a.input,a.out,a.seed,a.iterations)
