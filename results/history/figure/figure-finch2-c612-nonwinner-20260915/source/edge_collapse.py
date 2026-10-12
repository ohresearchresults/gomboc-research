"""Physical-abscissa regular collapse of the physical edge82--85: insert contact(16,55,94,118).
Retain all original multiple contacts; release precisely the two new incidences.
Floors inherited once from the exact FINCH_SEQUENTIAL seed, including basin146.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse,json,time,multiprocessing as mp
from pathlib import Path
import numpy as np
from scipy.optimize import minimize,linprog
from coupled import Model
from forest_search import metric

class Collapse(Model):
 def __init__(self,G,R):
  self.ready=False
  super().__init__(G,R,forced={82:85})
  self.axis=2;self.j=self.index[(16,2)];self.tri=np.array([55,94,118])
  self.delta0=self.X0[85,0]-self.X0[82,0]
  self.z0[self.j]=self.delta0;self.ready=True
  self.release=((self.geo_i==82)&(self.keep[self.geo_j]==16))|((self.geo_i==85)&(self.keep[self.geo_j]==118))
  assert self.release.sum()==2
  self.locked_v=self.select(self.eval(self.z0))[0]
  self.locked_f=self.select(self.eval(self.z0))[1]
  suc={int(self.vi[k]):int(self.vj[k]) for k in self.locked_v};suc[82]=85
  for v in range(len(self.X0)):
   seen=set()
   while v!=self.root:assert v not in seen;seen.add(v);v=suc[v]
 def chart(self,z,deriv=True):
  X,d=super().chart(z,deriv)
  if not self.ready:return X,d
  A=np.linalg.solve(X[self.tri],np.ones(3));R=np.cross(X[55],X[94]);r=R/R[0];B=A+z[self.j]*r;rest=[0,1];X[16,2]=(1-X[16,rest]@B[rest])/B[2]
  if deriv:
   da=-np.linalg.solve(X[self.tri],np.einsum('vkp,k->vp',d[self.tri],A))
   dR=np.cross(d[55].T,X[94]).T+np.cross(X[55],d[94].T).T
   dr=(dR-r[:,None]*dR[0])/R[0];db=da+z[self.j]*dr;db[:,self.j]+=r
   rhs=-np.einsum('k,kp->p',X[16],db)-B[rest]@d[16,rest];d[16,2]=rhs/B[2]
  return X,d
 def constr(self,a,vv=None,ff=None,deriv=False,geomask=None):
  if not self.ready:return super().constr(a,vv,ff,deriv,geomask)
  if vv is None:vv=self.locked_v;ff=self.locked_f
  if geomask is None:geomask=~self.release
  else:geomask=geomask&~self.release
  return super().constr(a,vv,ff,deriv,geomask)

def solveqp(A,b,E,h):
 K=A.shape[1];norm=np.maximum(np.linalg.norm(A,axis=1),1e-12);A=A/norm[:,None];b=b/norm
 en=np.linalg.norm(E,axis=1);E=E/en[:,None];h=h/en
 scale=max(b.max(),abs(h).max(),1e-4);bb=b/scale;hh=h/scale
 u=E.T@np.linalg.solve(E@E.T,hh)
 def worker(conn):
  try:
   sol=minimize(lambda x:.5*x@x,u,jac=lambda x:x,method='SLSQP',constraints=[{'type':'ineq','fun':lambda x:A@x-bb,'jac':lambda x:A},{'type':'eq','fun':lambda x:E@x-hh,'jac':lambda x:E}],options={'ftol':1e-10,'maxiter':10})
   conn.send((sol.x,sol.message,int(sol.nit)))
  finally:conn.close()
 ctx=mp.get_context('fork');a,c=ctx.Pipe(False);proc=ctx.Process(target=worker,args=(c,));proc.start();c.close();msg='QP-time-limit';nit=0;accepted=False
 if a.poll(4):
  v,msg,nit=a.recv()
  if (A@v-bb).min()>-1e-8 and abs(E@v-hh).max()<1e-8:u=v;accepted=True
 if proc.is_alive():proc.terminate()
 proc.join(timeout=1)
 if proc.is_alive():proc.kill();proc.join(timeout=1)
 a.close()
 if not accepted:return None,dict(qp=msg,nit=nit)
 return u*scale,dict(qp=msg,nit=nit,res=float((A@u-bb).min()*scale))

def correct(m,z,level,limit=12):
 trace=[]
 def merit(a,z):return float(np.linalg.norm(np.r_[np.minimum(0,m.constr(a)-2e-8),z[m.j]-level]))
 for it in range(limit):
  a=m.eval(z,True);c=m.constr(a)
  if c.min()>=0 and abs(z[m.j]-level)<1e-12 and a['min_det']>=-1e-14 and abs(a['allslack'][m.inc]).max()<1e-9:return z,a,True,trace
  c,J=m.constr(a,deriv=True,geomask=a['geo']<.04);T=metric(m,a)
  E=T[m.j:m.j+1];u,inf=solveqp(J@T,2e-8-c,E,np.array([level-z[m.j]]))
  if u is None:trace.append(inf);break
  dz=T@u;old=merit(a,z);alpha=1.;ok=False
  for ls in range(18):
   try:
    zz=z+alpha*dz;aa=m.eval(zz);new=merit(aa,zz)
    if new<old*(1-1e-4*alpha):ok=True;break
   except (np.linalg.LinAlgError,FloatingPointError):pass
   alpha*=.5
  tr=dict(inner=it,delta=float(z[m.j]),cmin=float(c.min()),unorm=float(np.linalg.norm(u)),alpha=alpha,merit=old,qp=inf);trace.append(tr)
  print('COR',json.dumps(tr),flush=True)
  if not ok or np.linalg.norm(alpha*u)>.4:break
  z=zz
 return z,m.eval(z),False,trace

def freeze(m,z,file,grid=10**13,closed=False):
 G=json.loads(json.dumps(m.gen));G['controls']=[[0,0,0] for _ in G['controls']];G['grid']=grid
 # Before closure, freeze original chart's free16z after computing the regular chart.
 X,_=m.chart(z,False)
 for i,k in m.free:G['controls'][i][k]=int(round(float(X[i,k])*grid))
 if closed:
  # 16 has no other multiple contacts. Reorder to solve the new merged point then16.
  assert next(d for i,d,ax in G['plan'] if i==16)==[]
  G['plan']=[row for row in G['plan'] if row[0]!=16];j=len(G['controls']);G['controls'].append([0,0,0]);G['groups'].append([16,55,94,118]);G['plan'] += [[j,[55,94,118],[0,1,2]],[16,[j],[2]]]
 Path(file).write_text(json.dumps(G,sort_keys=True,separators=(',',':')))

def main():
 p=argparse.ArgumentParser();p.add_argument('--start');p.add_argument('--steps',type=int,default=6);p.add_argument('--step',type=float,default=.002);p.add_argument('--tag',default='COLLAPSE');a=p.parse_args()
 G=json.load(open('FINCH_SEQUENTIAL_GENERATOR.json'));R=json.load(open('FINCH_SEQUENTIAL_A.json'));m=Collapse(G,R)
 z=m.z0.copy() if a.start is None else np.load(a.start);step=a.step;logs=[];t0=time.time()
 print('START',z[m.j],flush=True)
 for it in range(a.steps):
  level=max(0,float(z[m.j])-step);print('OUTER',it,level,flush=True)
  try:zz,b,ok,cor=correct(m,z,level)
  except (np.linalg.LinAlgError,FloatingPointError) as exc:ok=False;b=m.eval(z);cor=[str(exc)]
  log=dict(iteration=it,accepted=ok,step=step,level=level,delta=float(zz[m.j]),cmin=float(m.constr(b).min()),g=b['g'].tolist(),volume=float(b['volume']),inner=cor,elapsed=time.time()-t0)
  if ok:z=zz;step=min(.004,step*1.25);np.save(a.tag+'.npy',z);freeze(m,z,a.tag+'_GENERATOR.json',closed=level==0)
  else:step*=.5
  logs.append(log);Path(a.tag+'_TRACE.json').write_text(json.dumps(logs));print('OUTCOME',json.dumps({k:v for k,v in log.items() if k!='inner'}),flush=True)
  if ok and level==0:print('NUMERICAL_CLOSED_CONSTRUCTION',flush=True);break
  if step<1e-7:break
 print('PHASE_FINISHED',flush=True)
if __name__=='__main__':main()
