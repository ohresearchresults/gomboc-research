"""Differentiable rational-contact atlas; numerical discovery only.
Exact definitions and acceptance use RECONSTRUCT.py and both independent audits.
"""
import json, sys, numpy as np
from pathlib import Path
from fractions import Fraction
from scipy.linalg import svd
from scipy.optimize import linprog
class Model:
 def __init__(self,gen,top):
  self.gen=gen;self.n=gen['n_supports'];self.base=np.array(gen['controls'],dtype=float)/gen['grid'];self.plan=gen['plan'];self.groups=gen['groups']
  self.free=[(i,k) for i,deps,axes in self.plan for k in range(3) if k not in axes]
  self.k=len(self.free);self.x0=np.array([self.base[i,k] for i,k in self.free]);self.fidx={p:t for t,p in enumerate(self.free)}
  self.owners=top['owners'];self.faces=top['faces'];self.edges=top['edges'];self.stable=gen.get('stable',3)
  if not isinstance(self.stable,int):self.stable=3
  self.tris=np.array([(c[0],c[j],c[j+1]) for c in self.faces for j in range(1,len(c)-1)])
  groupdict={tuple(sorted(g)):self.n+j for j,g in enumerate(self.groups)}
  self.vspec=[('node',groupdict[tuple(sorted(o))]) if tuple(sorted(o)) in groupdict else ('solve',list(o)[:3]) for o in self.owners]
  self.root=next(i for i,o in enumerate(self.owners) if tuple(sorted(o))==tuple(sorted(self.groups[0])))
  self.mask=np.ones((len(self.owners),self.n),dtype=bool)
  for i,o in enumerate(self.owners):self.mask[i,o]=False
  self.vi=np.array([i for i in range(len(self.owners)) if i!=self.root]);self.qi=np.array([i for i in range(self.n) if i!=self.stable])
 def nodes(self,x,der=True):
  X=self.base.copy();X[self.n]=[0,0,1];J=np.zeros((len(X),3,self.k)) if der else None
  for t,(i,k) in enumerate(self.free):
   X[i,k]=x[t]
   if der:J[i,k,t]=1
  for i,deps,axes in self.plan:
   if not deps:continue
   rest=[k for k in range(3) if k not in axes];A=X[np.ix_(deps,axes)];b=1-X[np.ix_(deps,rest)]@X[i,rest]
   X[i,axes]=np.linalg.solve(A,b)
   if der:
    rhs=-np.einsum('rkp,k->rp',J[deps],X[i])-X[np.ix_(deps,rest)]@J[i,rest]
    J[i,axes]=np.linalg.solve(A,rhs)
  return X,J
 def geom(self,x,der=True):
  X,J=self.nodes(x,der);q=X[:self.n];P=[];PJ=[]
  for kind,data in self.vspec:
   if kind=='node':
    P.append(X[data]);
    if der:PJ.append(J[data])
   else:
    A=q[data];p=np.linalg.solve(A,np.ones(3));P.append(p)
    if der:PJ.append(np.linalg.solve(A,-np.einsum('ikp,k->ip',J[data],p)))
  P=np.array(P);PJ=np.array(PJ) if der else None
  a,b,c=(P[self.tris[:,i]] for i in range(3));cross=np.cross(b,c);det=np.einsum('ij,ij->i',a,cross);W=det.sum();ss=a+b+c;moment=np.einsum('i,ij->j',det,ss);g=moment/(4*W)
  if der:
   A,B,C=(PJ[self.tris[:,i]] for i in range(3));dw=np.einsum('ijk,ij->ik',A,cross)+np.einsum('ijk,ij->ik',B,np.cross(c,a))+np.einsum('ijk,ij->ik',C,np.cross(a,b));dW=dw.sum(0)
   dm=np.einsum('ik,ij->jk',dw,ss)+np.einsum('i,ijk->jk',det,A+B+C);dg=(dm-4*g[:,None]*dW)/(4*W)
   R=P-g;RJ=PJ-dg;h=1-q@g;dh=-np.einsum('ijk,j->ik',J[:self.n],g)-q@dg
   Q=q/h[:,None];QJ=J[:self.n]/h[:,None,None]-q[:,:,None]*dh[:,None,:]/h[:,None,None]**2
   return dict(X=X,J=J,P=P,PJ=PJ,q=q,qJ=J[:self.n],R=R,RJ=RJ,Q=Q,QJ=QJ,g=g,dg=dg,V=W/6)
  h=1-q@g
  return dict(X=X,P=P,q=q,R=P-g,Q=q/h[:,None],g=g,V=W/6)
 @staticmethod
 def allcos(R):
  delta=R[None,:,:]-R[:,None,:];dd=np.linalg.norm(delta,axis=2);rr=np.linalg.norm(R,axis=1)
  ans=np.einsum('ik,ijk->ij',R,delta)/np.maximum(rr[:,None]*dd,1e-150);np.fill_diagonal(ans,-np.inf);return ans
 @staticmethod
 def selected(R,J,ii,jj):
  r=R[ii];d=R[jj]-r;rn=np.linalg.norm(r,axis=1);dn=np.linalg.norm(d,axis=1);den=rn*dn;c=np.einsum('ij,ij->i',r,d)/den
  if J is None:return c,None
  rj=J[ii];dj=J[jj]-rj
  cj=(np.einsum('ikp,ik->ip',rj,d)+np.einsum('ikp,ik->ip',dj,r))/den[:,None]-c[:,None]*(np.einsum('ikp,ik->ip',rj,r)/rn[:,None]**2+np.einsum('ikp,ik->ip',dj,d)/dn[:,None]**2)
  return c,cj
 def stat(self,G):
  va=self.allcos(G['R']).max(1);vb=self.allcos(G['Q']).max(1);sl=1-G['P']@G['q'].T
  return {'V':float(G['V']),'g':G['g'].tolist(),'U':int(sum(va<0)),'S':int(sum(vb<0)),'min_escape':float(min(va[self.vi].min(),vb[self.qi].min())),'slack':float(sl[self.mask].min()),'shortest':float(min(np.linalg.norm(G['P'][i]-G['P'][j]) for i,j in self.edges))}
 def witness(self,G):
  ca=self.allcos(G['R']);cb=self.allcos(G['Q']);ja=ca[self.vi].argmax(1);jb=cb[self.qi].argmax(1)
  a,A=self.selected(G['R'],G.get('RJ'),self.vi,ja);b,B=self.selected(G['Q'],G.get('QJ'),self.qi,jb)
  return np.r_[a,b],np.vstack([A,B]) if A is not None else None,(ja,jb)
 def save(self,x,path,grid=10**12):
  G=self.geom(x,False);d=json.loads(json.dumps(self.gen));d['grid']=int(grid);d['controls']=np.rint(G['X']*grid).astype(np.int64).tolist();Path(path).write_text(json.dumps(d,separators=(',',':'),sort_keys=True))
def source_top(path):
 a=json.loads(Path(path).read_text());owners=[[] for _ in a['raw_vertices']]
 for i,c in enumerate(a['faces']):
  for v in c:owners[v].append(a['active_input_indices'][i])
 return dict(owners=owners,faces=a['faces'],edges=a['edges'])
def add36(gen,top):
 gen=json.loads(json.dumps(gen));top=json.loads(json.dumps(top));n=gen['n_supports'];idx=len(gen['controls']);assert idx==172
 model=Model(gen,top);X,_=model.nodes(model.x0);node=np.linalg.solve(X[[26,65,82]],np.ones(3));gen['controls'].append(np.rint(node*gen['grid']).astype(np.int64).tolist())
 assert [27,[137],[2]] in gen['plan'];gen['plan'].remove([27,[137],[2]]);gen['plan'] += [[172,[26,65,82],[0,1,2]],[27,[137,172],[1,2]]];gen['groups'].append([26,27,65,82]);gen['labels']='COORD_REBUILT_CONTACT36_H137'
 u=top['owners'].index(sorted([26,65,82]));v=top['owners'].index(sorted([26,27,82]));print('merge physical',u,v,flush=True)
 keep=min(u,v);drop=max(u,v);top['owners'][keep]=[26,27,65,82];top['owners'].pop(drop)
 mapping={i:(keep if i==drop else (i-1 if i>drop else i)) for i in range(len(top['owners'])+1)};faces=[];edges=set()
 for c in top['faces']:
  cy=[]
  for i in c:
   j=mapping[i]
   if not cy or cy[-1]!=j:cy.append(j)
  if cy[0]==cy[-1]:cy.pop()
  assert len(cy)>=3 and len(cy)==len(set(cy));faces.append(cy);edges.update(tuple(sorted((i,j))) for i,j in zip(cy,cy[1:]+cy[:1]))
 top['faces']=faces;top['edges']=sorted(edges);return gen,top
if __name__=='__main__':
 base=Path(__file__).resolve().parent/'BASE650';g=json.loads((base/'GENERATOR.json').read_text());t=source_top(base/'A.json');m=Model(g,t);print('base',m.k,m.stat(m.geom(m.x0)),flush=True)
 g,t=add36(g,t);m=Model(g,t);G=m.geom(m.x0);print('contact',m.k,m.stat(G),flush=True)
 Path('TOP36.json').write_text(json.dumps(t,separators=(',',':')));m.save(m.x0,'SEED36.json');np.save('x36.npy',m.x0)
 rng=np.random.default_rng(17);d=rng.normal(size=m.k);d/=np.linalg.norm(d);h=1e-7
 for name,jname in [('P','PJ'),('g','dg'),('Q','QJ')]:
  a=m.geom(m.x0+h*d,False)[name];b=m.geom(m.x0-h*d,False)[name];fd=(a-b)/(2*h);an=G[jname]@d;print('diff',name,float(np.linalg.norm(fd-an)/max(np.linalg.norm(an),1e-12)),flush=True)
