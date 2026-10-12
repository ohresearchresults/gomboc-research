"""C598 joint old contact geometry / five exposed points / own mass chart.
All numerical topology is inherited from the exact seed. Exact endpoint audit is separate.
"""
import sys,json,itertools,os
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent

def dot(a,b,da,db):
 return np.sum(a*b,axis=-1),np.einsum('...ik,...i->...k',da,b)+np.einsum('...i,...ik->...k',a,db)
def cross(a,b,da,db):
 return np.cross(a,b),np.cross(da.swapaxes(-1,-2),b[...,None,:]).swapaxes(-1,-2)+np.cross(a[...,None,:],db.swapaxes(-1,-2)).swapaxes(-1,-2)
def norm(a,da):
 r=np.linalg.norm(a,axis=-1);return r,np.einsum('...i,...ik->...k',a,da)/r[...,None]
def divide(a,b,da,db):
 return a/b,(da-(a/b)[...,None]*db)/b[...,None]

def setup():
 if os.environ.get('MODEL_GENERATOR'):
  return json.load(open(os.environ['MODEL_GENERATOR'])),json.load(open(os.environ['MODEL_META']))
 G=json.load(open(HERE/'core/BQ13_C602.json'));par=json.load(open(HERE/'seed/PARENT_A.json'));seed=json.load(open(HERE/'seed/A.json'));cfg=json.load(open(HERE/'junction/SELECTORS.json'))
 P=[tuple(map(Q,r)) for r in par['raw_vertices']];N=np.array([[float(Q(z,d)) for z in row] for row,d in zip(par['normals'],par['offsets'])])
 owners=[[] for p in P]
 for f,cy in enumerate(par['faces']):
  for i in cy:owners[i].append(par['active_input_indices'][f])
 triples=[max(itertools.combinations(ow,3),key=lambda a:abs(np.linalg.det(N[list(a)]))) for ow in owners]
 new=[tuple(Q(z,cfg['grid']) for z in r) for r in cfg['new_raw_points']];allp=P+new;lab={p:i for i,p in enumerate(allp)}
 labels=[lab[tuple(map(Q,r))] for r in seed['raw_vertices']]
 meta={'triples':triples,'labels':labels,'faces':seed['faces'],'edges':seed['edges'],'selectors':cfg['selectors'],'reference':[str(z) for z in map(Q,par['raw_centroid'])]}
 return G,meta

class Model:
 def __init__(self,G=None,meta=None):
  if G is None:G,meta=setup()
  self.G=G;self.meta=meta;self.n=G['n_supports'];self.base=np.array(G['controls'],float)/G['grid'];self.base[self.n]=[0,0,1]
  self.free=[(i,a) for i,deps,axes in G['plan'] for a in range(3) if a not in axes]
  self.D=len(self.free)+15;self.z0=np.r_[[self.base[i,a] for i,a in self.free],(np.array(meta['new_points'],float).ravel() if 'new_points' in meta else np.array(json.load(open(HERE/'junction/SELECTORS.json'))['new_raw_points'],float).ravel()/1e12)]
  self.triples=np.array(meta['triples']);self.labels=np.array(meta['labels']);self.F=[list(cy) for cy in meta['faces']];self.E=np.array(meta['edges']);self.m=np.array([float(Q(z)) for z in meta['reference']]);self.root=int(np.flatnonzero(self.labels==85)[0]);self.stable=114
  self.tris=np.array([(cy[0],cy[j],cy[j+1]) for cy in self.F for j in range(1,len(cy)-1)])
  self.side=np.array([(f,i,j) for f,cy in enumerate(self.F) for i,j in zip(cy,cy[1:]+cy[:1])]);self.arrows=np.array([(i,j) for i,j in self.E for i,j in [(i,j),(j,i)]])
  self.u_indices=[np.flatnonzero(self.arrows[:,0]==i) for i in range(len(self.labels))];self.f_indices=[np.flatnonzero(self.side[:,0]==i) for i in range(len(self.F))]
  mask=np.ones((len(self.F),len(self.labels)),bool)
  for f,cy in enumerate(self.F):mask[f,cy]=False
  self.noninc=np.array(np.where(mask)).T
  self.latest=None
 def evaluate(self,z,theta=1.):
  lift=len(z)>self.D;K=self.D+3*lift;shapez=z[:self.D];X=self.base.copy();DX=np.zeros((*X.shape,K));
  for k,(i,a) in enumerate(self.free):X[i,a]=z[k];DX[i,a,k]=1
  for i,deps,axes in self.G['plan']:
   if not deps:continue
   rest=[a for a in range(3) if a not in axes];A=X[np.ix_(deps,axes)];DA=DX[deps][:,axes,:]
   b=np.ones(len(deps))-X[deps][:,rest]@X[i,rest]
   db=-np.einsum('iak,a->ik',DX[deps][:,rest,:],X[i,rest])-X[deps][:,rest]@DX[i,rest,:]
   y=np.linalg.solve(A,b);dy=np.linalg.solve(A,db-np.einsum('iak,a->ik',DA,y));X[i,axes]=y;DX[i,axes]=dy
  A=X[self.triples];DA=DX[self.triples];P=np.linalg.solve(A,np.ones((len(A),3,1)))[...,0];DP=np.linalg.solve(A,-np.einsum('niak,na->nik',DA,P))
  P=np.concatenate((P,np.asarray(shapez[-15:]).reshape(5,3)));Dn=np.zeros((5,3,K));Dn.reshape(15,K)[:,self.D-15:self.D]=np.eye(15);DP=np.concatenate((DP,Dn))
  oldids=[k for k,s in enumerate(self.meta['selectors']) if 'old' in s];newids=[k for k,s in enumerate(self.meta['selectors']) if 'tri' in s];olds=[self.meta['selectors'][k]['old'] for k in oldids];ts=np.array([self.meta['selectors'][k]['tri'] for k in newids])
  qs=np.zeros((len(self.F),3));Dq=np.zeros((len(self.F),3,K));qs[oldids]=X[olds];Dq[oldids]=DX[olds]
  A=P[ts];DA=DP[ts];v=np.linalg.solve(A,np.ones((len(A),3,1)))[...,0];dv=np.linalg.solve(A,-np.einsum('niak,na->nik',DA,v));qs[newids]=v;Dq[newids]=dv
  P=P[self.labels];DP=DP[self.labels];T=P[self.tris];DT=DP[self.tris]
  cr,dcr=cross(T[:,1],T[:,2],DT[:,1],DT[:,2]);det,ddet=dot(T[:,0],cr,DT[:,0],dcr);D=det.sum();dD=ddet.sum(axis=0)
  B=np.einsum('n,ni->i',det,T.sum(axis=1));dB=np.einsum('nk,ni->ik',ddet,T.sum(axis=1))+np.einsum('n,nik->ik',det,DT.sum(axis=1));g=B/(4*D);dg=(dB-4*g[:,None]*dD)/(4*D)
  centre=self.m*(1-theta)+theta*g;dc=theta*dg
  if lift:centre=z[-3:];dc=np.zeros((3,K));dc[:,-3:]=np.eye(3)
  Z=P-centre;DZ=DP-dc
  i,j=self.arrows.T;e=P[j]-P[i];de=DP[j]-DP[i];un,du=dot(Z[i],e,DZ[i],de);el,del_=norm(e,de);ul,dul=norm(Z[i],DZ[i]);usc=el*ul;dusc=del_*ul[:,None]+dul*el[:,None];u,du=divide(un,usc,du,dusc)
  f,i,j=self.side.T;ee=P[j]-P[i];dee=DP[j]-DP[i];cr,dcr=cross(Z[i],ee,DZ[i],dee);fn,df=dot(qs[f],cr,Dq[f],dcr);fn=-fn;df=-df
  ql,dql=norm(qs[f],Dq[f]);ell,dell=norm(ee,dee);zl,dzl=norm(Z[i],DZ[i]);fsc=ql*ell*zl;dfsc=dql*(ell*zl)[:,None]+dell*(ql*zl)[:,None]+dzl*(ql*ell)[:,None];fv,df=divide(fn,fsc,df,dfsc)
  f,vv=self.noninc.T;s=1-np.einsum('ni,ni->n',qs[f],P[vv]);ds=-np.einsum('nik,ni->nk',Dq[f],P[vv])-np.einsum('ni,nik->nk',qs[f],DP[vv])
  out={'q':qs,'dq':Dq,'P':P,'dP':DP,'g':g,'dg':dg,'volume':D/6,'dvolume':dD/6,'u':u,'du':du,'f':fv,'df':df,'s':s,'ds':ds,'det':det,'ddet':ddet,'centre':centre,'gap':centre-g,'dgap':dc-dg}
  return out
 def choices(self,R):
  ui=np.array([ix[np.argmax(R['u'][ix])] for ix in self.u_indices]);fi=np.array([ix[np.argmax(R['f'][ix])] for ix in self.f_indices]);return ui,fi
 def summary(self,R):
  ui,fi=self.choices(R);return {'U':np.flatnonzero(R['u'][ui]<0).tolist(),'S':np.flatnonzero(R['f'][fi]<0).tolist(),'worst_u':float(np.min(R['u'][ui[np.arange(len(ui))!=self.root]])),'worst_f':float(np.min(R['f'][fi[np.arange(len(fi))!=self.stable]])),'min_slack':float(R['s'].min()),'min_det':float(R['det'].min()),'g':R['g'].tolist(),'volume':float(R['volume'])}

if __name__=='__main__':
 M=Model();np.save(HERE/'start.npy',M.z0);(HERE/'META.json').write_text(json.dumps(M.meta,sort_keys=True,separators=(',',':')))
 for theta in [0,1]:
  R=M.evaluate(M.z0,theta);print(theta,json.dumps(M.summary(R)))
 rng=np.random.default_rng(31);d=rng.normal(size=M.D);d/=np.linalg.norm(d);h=1e-7
 R=M.evaluate(M.z0);R1=M.evaluate(M.z0+h*d);R2=M.evaluate(M.z0-h*d)
 print('variables',M.D)
 for k,jk in [('g','dg'),('u','du'),('f','df'),('s','ds')]:
  a=(R1[k]-R2[k])/(2*h);b=R[jk]@d;print(k,float(np.max(abs(a-b))),float(np.linalg.norm(a-b)/(1e-30+np.linalg.norm(a))))
