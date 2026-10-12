"""Direct physical face-foot correction on a complete exact contact family.

The unique unstable equilibrium is maintained at the actual filled centroid.
All stable-facet exclusions use signed projected-foot distances in the primal
body, avoiding inverse small dihedral angles. No facet is approximately merged.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from contact_numpy import Chart
from contact_quota_polish import metric
from contact_polynomial_flow import correct, OPT as CORRECTION_OPT
from direct_face_polish import cross_derivative
from support_geometry import escape
from exact_contact_audit import audit
from exact_barcode_report import report
from goal_nomination import ExactGoalCandidateFound

class PhysicalFeet:
 def __init__(self,c):
  self.c=c;self.f=np.concatenate([np.full(len(cy),f,int)for f,cy in enumerate(c.faces)]);self.a=np.concatenate([np.array(cy,int)for cy in c.faces]);self.b=np.concatenate([np.roll(np.array(cy,int),-1)for cy in c.faces]);self.starts=np.r_[0,np.cumsum([len(cy)for cy in c.faces])]
 def evaluate(self,g):
  R=np.sqrt(np.mean(np.sum(g['Z']**2,axis=1)));DR=np.mean(np.einsum('ic,icp->ip',g['Z'],g['DZ']),axis=0)/R;Y=g['Y'];DY=g['DY'];length=np.linalg.norm(Y,axis=1);n=Y/length[:,None];Dn=(DY-n[:,:,None]*np.einsum('ic,icp->ip',n,DY)[:,None,:])/length[:,None,None];e=g['X'][self.b]-g['X'][self.a];De=g['DX'][self.b]-g['DX'][self.a];ell=np.linalg.norm(e,axis=1);t=np.cross(n[self.f],e)/ell[:,None];Dt=cross_derivative(n[self.f],Dn[self.f],e,De)/ell[:,None,None]-t[:,:,None]*np.einsum('ic,icp->ip',e,De)[:,None,:]/ell[:,None,None]**2;v=np.einsum('ic,ic->i',t,g['Z'][self.a])/R;J=(np.einsum('icp,ic->ip',Dt,g['Z'][self.a])+np.einsum('ic,icp->ip',t,g['DZ'][self.a]))/R-v[:,None]*DR/R;chosen=np.array([int(l+np.argmax(v[l:r]))for l,r in zip(self.starts[:-1],self.starts[1:])]);vf=v[chosen];JF=J[chosen];stable=np.flatnonzero(vf<0)
  if not len(stable):raise ValueError('no strictly interior stable projected foot in the numerical contact realization')
  root=int(stable[np.argmax(np.sum(g['H'][stable]**2,axis=1))]);keep=np.arange(len(vf))!=root;vu,_,JU=escape(g['Z'],g['DZ'],angular=True);uroot=int(np.argmax(np.sum(g['Z']**2,axis=1)));umask=np.arange(len(vu))!=uroot;return vf[keep],JF[keep],vu[umask],JU[umask],dict(S=len(stable),U=int(sum(vu<0)),stable_root=root,unstable_root=uroot,foot_scores=vf)

def exact_nomination(c,q,out):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);np.save(out/'literal_controls.npy',q);grid=max(float(v).as_integer_ratio()[1]for v in q);a=audit(c.path,out/'literal_controls.npy',out/'exact_dyadic_controls',grid);report(out/'exact_dyadic_controls')
 if a['counts']==[1,1,0]and a['weak']==[0,0,0]and 34<=2*a['E']<500 and a['V']+a['E']+a['F']<500:raise ExactGoalCandidateFound('Exact direct-face contact Figure at '+str(out))
 return a

def run(source,out,steps,start_q=None):
 CORRECTION_OPT['time_limit']=10.
 c=Chart(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);feet=PhysicalFeet(c);q=c.q0.copy()if start_q is None else np.load(start_q);g=c.physical(q);v,J,u,JU,cl=feet.evaluate(g);assert cl['U']==1 and min(u)>0;epsU=min(1e-8,float(min(u))*.2);epsS=1e-8;gapfloor=min(1e-11,float(min(g['noncontact']))*.1);trust=.03;hist=[];start=time.time();(out/'source_construction.json').write_bytes(Path(source).read_bytes());np.save(out/'initial_q.npy',q);(out/'method.json').write_text(json.dumps(dict(epsilon_stable=epsS,epsilon_unstable=epsU,gapfloor=gapfloor,correction_lp_seconds=10.,start_q=None if start_q is None else str(Path(start_q).resolve()),scope='all accepted bodies have actual U1; direct physical facet-foot violations are reduced'),indent=2))
 for it in range(steps):
  g=c.physical(q);v,J,u,JU,cl=feet.evaluate(g);merit=float(np.maximum(epsS-v,0).sum());row=dict(it=it,S=cl['S'],U=cl['U'],merit=merit,minimum_face=float(min(v)),minimum_U=float(min(u)),gap=float(min(g['noncontact'])),trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest_q.npy',q);(out/'trace.json').write_text(json.dumps(hist,indent=2))
  if it%5==0:print('CONTACT_PHYSICAL_FACE_DESCENT',out,row,flush=True)
  if cl['S']==cl['U']==1:exact_nomination(c,q,out/f'goal_nomination_it{it}')
  W=metric(c,g);d=c.d;m=len(v);bound=trust/np.sqrt(d);gap=g['noncontact'];JG=g['Dgap'][~c.incidence]@W;rhs=gap-gapfloor;keep=rhs<=bound*np.sum(abs(JG),axis=1)+1e-10;I=eye(d);O=csr_matrix((d,m));sc=.001;hard=np.vstack((JG[keep],JU@W));hb=np.r_[rhs[keep],u-epsU];A=vstack([hstack([-csr_matrix(J@W/sc),-eye(m),csr_matrix((m,d))]),hstack([-csr_matrix(hard/sc),csr_matrix((len(hb),m+d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-epsS)/sc,hb/sc,np.zeros(2*d)];r=linprog(np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)],A_ub=A,b_ub=b,bounds=[(-bound,bound)]*d+[(0,None)]*(m+d),method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=20.))
  if not r.success:row['error']=r.message;trust*=.4
  else:
   dq=W@r.x[:d];rr=[[cl['unstable_root']],list(range(c.F))];ok=False
   for k in range(13):
    try:
     qq,good,n=correct(c,q+2.**-k*dq,W,rr,epsU,gapfloor)
     if not good:continue
     gg=c.physical(qq);vv,_,uu,_,cc=feet.evaluate(gg);mm=float(np.maximum(epsS-vv,0).sum())
    except(ValueError,np.linalg.LinAlgError):continue
    if cc['S']==cc['U']==1:exact_nomination(c,qq,out/f'goal_nomination_it{it}_line{k}')
    if cc['U']==1 and min(uu)>epsU*.85 and mm<merit-max(1e-12,merit*1e-7):q=qq;ok=True;row.update(alpha=2.**-k,corrections=n);break
   if ok and k==0:trust=min(.4,trust*1.3)
   if not ok:trust*=.4
  if trust<1e-10:break
 np.save(out/'endpoint_q.npy',q);a=audit(source,out/'endpoint_q.npy',out/'exact_endpoint_g15',10**15);report(out/'exact_endpoint_g15');print('CONTACT_FACE_ENDPOINT',{k:a[k]for k in ['V','E','F','counts','weak']},flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=500);p.add_argument('--start-q');a=p.parse_args();run(a.source,a.out,a.steps,a.start_q)
