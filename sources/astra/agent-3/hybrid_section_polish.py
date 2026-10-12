"""Actual-mass hybrid section retraction with symbolic coplanar ownership.
Unreleased quad membership merges its integration triangles without an angular
tolerance. The changed local faces follow the actual current hull proposal.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
from rectangular_sections import RectFamily
from vertex_geometry import geometry
from support_geometry import escape
from section_polish import roots
from polish_121 import forest
from persistence_birth import bars_loss
OPT={'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10}

def physical(f,w,index):
 base=f.physical(w[:-3]);Y=base['X'].copy();Y[index]+=w[-3:];DY=np.zeros((len(Y),3,len(w)));DY[:,:,:-3]=base['DX'];DY[index,:,-3:]=np.eye(3);g=geometry(Y);T=g['T'];owner={}
 for k,face in enumerate(f.faces):
  for a in range(len(face)):
   for b in range(a+1,len(face)):
    for c in range(b+1,len(face)):
     tri=tuple(sorted([face[a],face[b],face[c]]))
     if index not in tri or np.all(w[-3:]==0):owner[tri]=('old',k)
 groups={};rep=[];tid=[]
 for k,t in enumerate(T):
  key=owner.get(tuple(sorted(t)),('new',*sorted(t)))
  if key not in groups:groups[key]=len(rep);rep.append(k)
  tid.append(groups[key])
 rep=np.array(rep);tid=np.array(tid);edges={}
 for k,t in enumerate(T):
  for a,b in zip(t,np.roll(t,-1)):edges.setdefault(tuple(sorted((a,b))),[]).append(int(tid[k]))
 pe=[];qe=[]
 for e,fs in edges.items():
  assert len(fs)==2
  if fs[0]!=fs[1]:pe.append(e);qe.append(fs)
 D=DY.reshape(Y.size,-1);DZ=np.einsum('ncp,pz->ncz',g['DZ'],D);DH=np.einsum('fcp,pz->fcz',g['DH'][rep],D);H=g['H'][rep];pe=np.array(pe);qe=np.array(qe)
 keep=np.array([i for i,fc in enumerate(f.faces) if index not in fc]);oldH=base['H'][keep];z=Y[index]-base['g'];ineq=1-oldH@z;dz=DY[index].copy();dz[:,:-3]-=base['Dg'];DI=-oldH@dz;DI[:,:-3]-=np.einsum('fcp,c->fp',base['DH'][keep],z)
 return dict(X=Y,Z=g['Z'],H=H,DZ=DZ,DH=DH,pe=pe,qe=qe,inequality=ineq,Dinequality=DI,construction=base['construction'],E=len(pe),V=len(g['vertices']),F=len(H),centroid=g['g'])

def guards(g,S,U):
 vals=[];Js=[];cl=[]
 for A,DA,ed,nroot in [(g['Z'],g['DZ'],g['pe'],U),(g['H'],g['DH'],g['qe'],S)]:
  rr=roots(A,ed,nroot);pp=forest(A,rr);sg=np.ones(len(A));sg[rr]=-1;v,_,J=escape(A,DA,angular=True,chosen=pp);vals.append(v*sg);Js.append(J*sg[:,None]);cl.append(int(np.sum(escape(A)[0]<0)))
 return np.r_[tuple(vals)],np.vstack(Js),cl

def run(f,source,out,index,S,U,steps,eps):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);w=np.load(source);trust=.005;hist=[];start=time.time();np.save(out/'initial_params.npy',w)
 for it in range(steps):
  g=physical(f,w,index);v,J,cl=guards(g,S,U);iv=g['inequality'];IJ=g['Dinequality'];merit=float(np.maximum(eps-v,0).sum()+np.maximum(-iv,0).sum());row=dict(it=it,S=cl[1],U=cl[0],V=g['V'],E=g['E'],F=g['F'],minimum=float(v.min()),unaffected=float(iv.min()),merit=merit,trust=trust,seconds=time.time()-start);hist.append(row);np.save(out/'latest_params.npy',w);np.savez(out/'latest_construction.npz',**g['construction'],released_vertex=index,released_offset=w[-3:]);(out/'history.json').write_text(json.dumps(hist,indent=2))
  if it%10==0:print('HYBRID_POLISH',out,row,flush=True)
  if min(v)>eps*.9 and min(iv)>0:
   np.save(out/'success_params.npy',w);np.savez(out/'success_construction.npz',**g['construction'],released_vertex=index,released_offset=w[-3:]);row['P']=bars_loss(g['Z'],g['pe'])[2];row['Q']=bars_loss(g['H'],g['qe'])[2];(out/'success.json').write_text(json.dumps(row,indent=2));print('HYBRID_STRICT_NOMINATION_REQUIRES_EXACT',row,flush=True);return
  d=len(w);m=len(v);I=eye(d);O=csr_matrix((d,m));scale=.001;A=vstack([hstack([-csr_matrix(J/scale),-eye(m),csr_matrix((m,d))]),hstack([-csr_matrix(IJ/scale),csr_matrix((len(iv),m+d))]),hstack([I,O,-I]),hstack([-I,O,-I])],format='csr');b=np.r_[(v-eps)/scale,iv*.9/scale,np.zeros(2*d)];obj=np.r_[np.zeros(d),np.ones(m),np.full(d,1e-5)];sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(-trust,trust)]*d+[(0,None)]*m+[(0,None)]*d,method='highs',options=OPT)
  if not sol.success:trust*=.5;continue
  dw=sol.x[:d];ok=False
  for alpha in [1.,.5,.25,.125,.0625,.03125,.015625,.0078125]:
   ww=w+alpha*dw;gg=physical(f,ww,index);vv,_,cc=guards(gg,S,U);mm=np.maximum(eps-vv,0).sum()+np.maximum(-gg['inequality'],0).sum()
   if np.isfinite(mm) and mm<merit*(1-1e-6):w=ww;ok=True;row['alpha']=alpha;break
  if ok and alpha==1:trust=min(.1,trust*1.3)
  if not ok:trust*=.4
  if trust<1e-11:break
 print('HYBRID_POLISH_NONWINNER',out,hist[-1],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('out');p.add_argument('--index',type=int,required=True);p.add_argument('--layers',type=int,default=30);p.add_argument('--S',type=int,default=1);p.add_argument('--U',type=int,default=2);p.add_argument('--steps',type=int,default=500);p.add_argument('--epsilon',type=float,default=1e-6);a=p.parse_args();run(RectFamily(a.layers),a.input,a.out,a.index,a.S,a.U,a.steps,a.epsilon)
