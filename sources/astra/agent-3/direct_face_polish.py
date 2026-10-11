"""Own-centroid equilibrium correction using physical face-foot distances.

Stable exclusion is the signed distance of the centroid projection beyond a
true hull triangle edge. It has no inverse dihedral-angle factor. All proposed
point hulls are freshly integrated with uniform density. Exact auditing still
determines maximal faces, strict equilibria, weak contacts and complexity.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from vertex_geometry import geometry
from support_geometry import escape
from goal_nomination import preserve

def cross_derivative(a,da,b,db):
 return(np.cross(np.moveaxis(da,1,2),b[:,None,:])+np.cross(a[:,None,:],np.moveaxis(db,1,2))).transpose(0,2,1)

def face_scores(g,derivative=True):
 X=g['X'];T=g['T'];active=g['vertices'];R=np.sqrt(np.mean(np.sum(g['Z'][active]**2,axis=1)));a,b,c=X[T[:,0]],X[T[:,1]],X[T[:,2]];e=b-a;f=c-a;n0=np.cross(e,f);nn=np.linalg.norm(n0,axis=1);n=n0/nn[:,None]
 if derivative:
  DX=g['DX'];de=DX[T[:,1]]-DX[T[:,0]];df=DX[T[:,2]]-DX[T[:,0]];Dn0=cross_derivative(e,de,f,df);Dn=(Dn0-n[:,:,None]*np.einsum('ic,icp->ip',n,Dn0)[:,None,:])/nn[:,None,None];DR=np.mean(np.einsum('ic,icp->ip',g['Z'][active],g['DZ'][active]),axis=0)/R
 vals=[];Js=[]
 for k in range(3):
  ia=T[:,k];ib=T[:,(k+1)%3];ee=X[ib]-X[ia];ll=np.linalg.norm(ee,axis=1);t=np.cross(n,ee)/ll[:,None];v=np.einsum('ic,ic->i',t,g['Z'][ia])/R;vals.append(v)
  if derivative:
   Dee=DX[ib]-DX[ia];Dt=cross_derivative(n,Dn,ee,Dee)/ll[:,None,None]-t[:,:,None]*np.einsum('ic,icp->ip',ee,Dee)[:,None,:]/ll[:,None,None]**2;J=(np.einsum('icp,ic->ip',Dt,g['Z'][ia])+np.einsum('ic,icp->ip',t,g['DZ'][ia]))/R-v[:,None]*DR/R;Js.append(J)
 V=np.column_stack(vals);which=V.argmax(1);v=V[np.arange(len(T)),which];J=np.stack(Js,axis=1)[np.arange(len(T)),which]if derivative else None;return v,J,V

def guards(g,derivative=True):
 active=g['vertices'];A=g['Z'][active]
 if derivative:vp,_,JP=escape(A,g['DZ'][active],angular=False)
 else:vp,_=escape(A,angular=False);JP=None
 vf,JF,_=face_scores(g,derivative);stable=np.flatnonzero(vf<0)
 if not len(stable):raise ValueError('numerical triangulation has no strictly interior projected foot; cannot assert a stable root')
 sr=int(stable[np.argmax(np.sum(g['H'][stable]**2,axis=1))]);ur=int(np.argmax(np.sum(A*A,axis=1)));pm=np.arange(len(A))!=ur;fm=np.arange(len(vf))!=sr;v=np.r_[vp[pm],vf[fm]];J=np.vstack((JP[pm],JF[fm]))if derivative else None;return v,J,dict(S=int(sum(vf<0)),U=int(sum(vp<0)),V=len(active),F_triangles=len(g['T']),stable_root=sr,unstable_root=int(active[ur]))

def run(source,out,steps,eps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);X=np.load(source);np.save(out/'initial.npy',X);trace=[];trust=.002;start=time.time()
 for it in range(steps):
  g=geometry(X);v,J,cl=guards(g);merit=float(np.maximum(eps-v,0).sum());row=dict(it=it,merit=merit,minimum=float(min(v)),trust=trust,seconds=time.time()-start,**cl);trace.append(row);np.save(out/'latest.npy',X);(out/'trace.json').write_text(json.dumps(trace,indent=2))
  if it%10==0:print('DIRECT_FACE_REPAIR',out,row,flush=True)
  if cl['S']==cl['U']==1:
   np.save(out/'success.npy',X);(out/'success.json').write_text(json.dumps(row,indent=2))
   if 2*(cl['V']+cl['F_triangles']-2)<622:preserve(X,out/f'exact_nomination_it{it}','direct physical face-projection and own-centroid unstable census both1; complete exact hull needed')
   return X,row
  d=X.size;m=len(v);I=eye(d);O=csr_matrix((d,m));sc=.001;A=vstack([hstack([-csr_matrix(J/sc),-eye(m),csr_matrix((m,d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-eps)/sc,np.zeros(2*d)];r=linprog(np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)],A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*(m+d),method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=20.))
  if not r.success:row['error']=r.message;trust*=.4
  else:
   dx=r.x[:d].reshape(X.shape);ok=False
   for k in range(14):
    xx=X+2.**-k*dx
    try:gg=geometry(xx,False);vv,_,cc=guards(gg,False);mm=float(np.maximum(eps-vv,0).sum())
    except(ValueError,np.linalg.LinAlgError):continue
    if cc['S']==cc['U']==1:
     np.save(out/'success.npy',xx);rr=dict(it=it,alpha=2.**-k,merit=mm,**cc);(out/'success.json').write_text(json.dumps(rr,indent=2))
     if 2*(cc['V']+cc['F_triangles']-2)<622:preserve(xx,out/f'exact_nomination_it{it}_line{k}','direct physical face-foot census own110 in line trial')
     return xx,rr
    if np.isfinite(mm)and mm<merit-max(1e-13,merit*1e-7):X=xx;ok=True;row['alpha']=2.**-k;break
   if ok and k==0:trust=min(.04,trust*1.3)
   if not ok:trust*=.4
  if trust<1e-11:break
 print('DIRECT_FACE_FINITE_NONWINNER',out,trace[-1],flush=True);return None,None

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=350);p.add_argument('--epsilon',type=float,default=1e-8);a=p.parse_args();run(a.source,a.out,a.steps,a.epsilon)
