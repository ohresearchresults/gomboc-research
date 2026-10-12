from pathlib import Path
import json,time,numpy as np
from scipy.optimize import least_squares
from scipy.sparse import coo_matrix
from contact_chart import make_chart
from numeric import recover,mechanics
R=Path(__file__).parent;data=json.loads((R/'H249_RESTORATION.json').read_text());warm=np.load(R/'H249_FIT_W1000.npz')
q0=warm['q'];p0=warm['p'];n=len(q0);m=len(p0);N=n+m;root=n+data['root'];X0=np.vstack([q0,p0]);X0[root]=[0,0,1]
refs=np.array([[i,n+f] for f,cy in enumerate(data['polar_faces']) for i in cy],int)
inc=np.zeros((n,m),bool)
for i,j in refs:inc[i,j-n]=True
ni,nj=np.where(~inc);off=np.column_stack([ni,n+nj]);nr=len(refs);no=len(off)
scale=np.repeat(np.maximum(np.linalg.norm(X0,axis=1),0.1)[:,None],3,axis=1);free=np.ones((N,3),bool);free[root]=False;fi=np.flatnonzero(free.ravel());back=np.full(N*3,-1);back[fi]=np.arange(len(fi));y0=(X0/scale).ravel()[fi]
def decode(y):
 X=X0.copy();X.ravel()[fi]=y*scale.ravel()[fi];return X
counter=0;start=time.time()
def fun(y):
 global counter
 X=decode(y);z=np.einsum('ic,ic->i',X[refs[:,0]],X[refs[:,1]])-1;gap=1-np.einsum('ic,ic->i',X[off[:,0]],X[off[:,1]])
 counter+=1
 if counter%50==1:print('PROJ',counter,'time',time.time()-start,'inc',abs(z).max(),'mingap',gap.min(),flush=True)
 return np.r_[z,np.maximum(1e-10-gap,0)]
def jac(y):
 X=decode(y);act=np.einsum('ic,ic->i',X[off[:,0]],X[off[:,1]])>1-1e-10;rr=np.r_[np.arange(nr),nr+np.flatnonzero(act)];pp=np.vstack([refs,off[act]]);rows=[];cols=[];vals=[]
 for s in (0,1):
  ids=pp[:,s];other=pp[:,1-s]
  for k in range(3):
   j=back[3*ids+k];ok=j>=0;rows.extend(rr[ok]);cols.extend(j[ok]);vals.extend((X[other,k]*scale[ids,k])[ok])
 return coo_matrix((vals,(rows,cols)),shape=(nr+no,len(fi))).tocsr()
res=least_squares(fun,y0,jac=jac,x_scale='jac',method='trf',tr_solver='lsmr',max_nfev=1000,ftol=1e-14,xtol=1e-14,gtol=1e-14,tr_options={'atol':1e-13,'btol':1e-13,'maxiter':5000})
X=decode(res.x);np.savez(R/'H249_PROJECTED.npz',q=X[:n],p=X[n:],y=res.x);print('END_PROJ',res.message,'cost',res.cost,'nfev',res.nfev,'opt',res.optimality,flush=True)
order=[data['root']]+[i for i in range(m) if i!=data['root']];pp=X[n:][order];pp[0]=[0,0,1];groups=[data['polar_faces'][i] for i in order]
for pref in ['supports','points','degree']:
 for D in [10**12,10**15]:
  try:
   g,dep=make_chart(X[:n],pp,groups,grid=D,prefer=pref);qq=recover(g)[:n];r=mechanics(qq,data['primal_faces'],tol=1e-10)
   tag=f'H249_PROJECT_{pref}_D{D}';(R/(tag+'_GENERATOR.json')).write_text(json.dumps(g,sort_keys=True,separators=(',',':')));(R/(tag+'_numeric.json')).write_text(json.dumps(r,indent=2))
   print('CHART',pref,D,'depth',max(dep.values()),r,flush=True)
  except Exception as e:print('CHART_ERROR',pref,D,repr(e),flush=True)
