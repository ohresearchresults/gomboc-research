"""Physical own-centroid correction with literal support offsets and one apex.

The centroid is recomputed, not constrained to a prechosen reference point.
The exact cap freezer preserves every existing nontriangular facet contact.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.linalg import svd
from scipy.sparse import csr_matrix,eye,hstack,vstack
from safe_offset_cap_mass import SafeCap,freeze,close
from polyhedral_stable_cap import Cap
from section_polish import roots
from polish_121 import forest
from support_geometry import escape
from persistence_birth import bars_loss

def physical(c,q):
 g=c.physical(q);h=1-g['Y']@g['g'];dh=-np.einsum('fcp,c->fp',g['DY'],g['g'])-g['Y']@g['Dg'];g.update(Z=g['X']-g['g'],DZ=c.DX-g['Dg'],H=g['Y']/h[:,None],DH=g['DY']/h[:,None,None]-g['Y'][:,:,None]*dh[:,None,:]/h[:,None,None]**2);return g

def guards(c,g,quota):
 vals=[];Js=[]
 for A,DA,edges,n in [(g['Z'],g['DZ'],c.base['pe'],1),(g['H'],g['DH'],c.base['qe'],quota)]:
  rr=roots(A,edges,n);pp=forest(A,rr);sg=np.ones(len(A));sg[rr]=-1;v,_,J=escape(A,DA,angular=True,chosen=pp);vals.append(v*sg);Js.append(J*sg[:,None])
 return np.r_[tuple(vals)],np.vstack(Js)

def metric(c,g):
 M=np.vstack((g['DZ'].reshape(-1,c.d)/np.sqrt(np.mean(g['Z']**2)),g['DH'].reshape(-1,c.d)/np.sqrt(np.mean(g['H']**2)),.01*np.eye(c.d)));_,s,V=svd(M,full_matrices=False,check_finite=False);return V.T/s

def repair(c,q,out,steps=180,eps=1e-7):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);trace=[];trust=.02;start=time.time();quota=2
 for it in range(steps):
  g=physical(c,q);quota=min(quota,g['S']) if g['S']>0 else quota;v,J=guards(c,g,quota);merit=float(np.maximum(eps-v,0).sum());row=dict(it=it,S=g['S'],U=g['U'],Q=g['Q'],P=g['P'],guard=float(min(v)),gap=float(min(g['noncontact'])),mass=g['g'].tolist(),merit=merit,trust=trust,seconds=time.time()-start);trace.append(row);np.save(out/'latest_q.npy',q);(out/'trace.json').write_text(json.dumps(trace,indent=2))
  if it%10==0:print('OWN_SAFE_OFFSET_REPAIR',out,row,flush=True)
  if g['S']==g['U']==1:freeze(c,q,out/f'exact_goal_it{it}')
  if min(v)>.85*eps:
   np.save(out/'success_q.npy',q);return q,g
  W=metric(c,g);d=c.d;m=len(v);bnd=trust/np.sqrt(d);gap=g['noncontact'];Jgap=g['Dgap']@W;rhs=gap-np.minimum(.9*gap,1e-9);keep=rhs<=bnd*np.sum(abs(Jgap),axis=1)+1e-9;I=eye(d);zero=csr_matrix((d,m));A=vstack([hstack([-csr_matrix(J@W/.001),-eye(m),csr_matrix((m,d))]),hstack([-csr_matrix(Jgap[keep]),csr_matrix((int(sum(keep)),m+d))]),hstack([I,zero,-I]),hstack([-I,zero,-I])],format='csr');b=np.r_[(v-eps)/.001,rhs[keep],np.zeros(2*d)];r=linprog(np.r_[np.zeros(d),np.ones(m),np.full(d,1e-6)],A_ub=A,b_ub=b,bounds=[(-bnd,bnd)]*d+[(0,None)]*(m+d),method='highs',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10,time_limit=20.))
  if not r.success:row['error']=r.message;trust*=.4
  else:
   dq=W@r.x[:d];ok=False
   for k in range(18):
    qq=q+dq*2.**-k
    try:gg=physical(c,qq);vv,_=guards(c,gg,quota)
    except(ValueError,np.linalg.LinAlgError,AssertionError):continue
    if gg['S']==gg['U']==1:freeze(c,qq,out/f'exact_goal_it{it}_line{k}')
    if np.maximum(eps-vv,0).sum()<merit*(1-1e-6):q=qq;ok=True;row['alpha']=2.**-k;break
   if ok and k==0:trust=min(.4,trust*1.3)
   if not ok:trust*=.4
  if trust<1e-10:break
 return None,None

def run(scout,out,number,mode):
 scout=Path(scout);out=Path(out);out.mkdir(parents=True,exist_ok=False);de=json.loads((scout/'definition.json').read_text());cap=Cap(de['source']);rows=json.loads((scout/'screen.json').read_text());selected=sorted((r for r in rows if 1<=r['reference_S']<=2),key=lambda r:r['reference_Q'])[:number];records=[]
 for row in selected:
  c=SafeCap(cap,cap.body(row['controls']));d=out/f"case{row['it']}";d.mkdir();(d/'nomination.json').write_text(json.dumps(row,indent=2));rec=dict(case=row['it'],mode=mode,reference_Q=row['reference_Q'])
  try:
   q,g=close(c,d/'closure',150,True) if mode=='move-apex-closure' else repair(c,c.q0.copy(),d/'repair')
   if q is None:rec['result']='finite experiment failed'
   else:
    s=freeze(c,q,d/'exact');rec.update(result='exact body audited',summary=s,Q=g['Q'],P=g['P'])
  except (ValueError,AssertionError,np.linalg.LinAlgError)as err:rec.update(result='explicit physical or numerical failure',error=repr(err))
  records.append(rec);(out/'results.json').write_text(json.dumps(records,indent=2));print('OWN_SAFE_OFFSET_RESULT',rec,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('scout');p.add_argument('out');p.add_argument('--number',type=int,default=8);p.add_argument('--mode',choices=['move-apex-closure','own-centroid'],default='own-centroid');a=p.parse_args();run(a.scout,a.out,a.number,a.mode)
