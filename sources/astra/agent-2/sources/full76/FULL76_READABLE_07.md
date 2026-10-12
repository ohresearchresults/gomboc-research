# FULL76 exact readable source, part 7/8
# Each FILE header gives the exact following UTF-8 byte count and SHA-256.
# The newline after each payload is a framing separator, not a source byte.

FILE methods/chart.py 3838 e2a29b606ce3f98143aa786751cd78f6fd1ebde1387ed5458950824afa879814
"""Exact projective Schlegel stress chart for the literal GRID7 polar graph."""
import json,sys,hashlib
from pathlib import Path
from fractions import Fraction as F
from math import lcm,gcd
from collections import defaultdict,deque
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(Path(__file__).parent/'parent'))
from check_A import dot,cross,add,sub,mul,det,polygon,encode

def inv3(A,b):
 d=det(*A); assert d
 return mul(1/d,add(add(mul(b[0],cross(A[1],A[2])),mul(b[1],cross(A[2],A[0]))),mul(b[2],cross(A[0],A[1]))))
def load(root=None):
 root=Path(root) if root is not None else Path(__file__).parent
 raw=json.loads((root/'baseline/raw.json').read_text());rep=json.loads((root/'baseline/A.json').read_text())
 Q=[tuple(F(v,row[3]) for v in row[:3]) for row in raw['H']]
 X=[tuple(map(F,row)) for row in rep['raw_vertices']]
 faces=[polygon(Q,[f for f,cy in enumerate(rep['faces']) if v in cy],x) for v,x in enumerate(X)]
 return Q,X,faces

def recover(outer=None,root=None):
 Q,X,faces=load(root)
 if outer is None:
  # The largest squared area triangular polar face, tie broken by index.
  outer=max((dot(cross(sub(Q[cy[1]],Q[cy[0]]),sub(Q[cy[2]],Q[cy[0]])),cross(sub(Q[cy[1]],Q[cy[0]]),sub(Q[cy[2]],Q[cy[0]]))),i) for i,cy in enumerate(faces) if len(cy)==3)[1]
 cy=faces[outer]; assert len(cy)==3
 c=mul(F(1,3),add(add(Q[cy[0]],Q[cy[1]]),Q[cy[2]]));a=sub(Q[cy[1]],Q[cy[0]]);b=sub(Q[cy[2]],Q[cy[0]]);d=c
 limit=min((1-dot(x,c))/dot(x,d) for i,x in enumerate(X) if i!=outer and dot(x,d)>0)
 delta=limit*F(3,4);assert delta>0
 # basis inverse by reciprocal vectors
 D=det(a,b,d);assert D>0
 rows=[mul(1/D,cross(b,d)),mul(1/D,cross(d,a)),mul(1/D,cross(a,b))]
 R=[]
 for q in Q:
  p=tuple(dot(row,sub(q,c)) for row in rows);den=1-p[2]/delta;assert den>0
  R.append(mul(1/den,p))
 planes=[]
 for i,x in enumerate(X):
  if i==outer:planes.append((F(0),)*3);continue
  k=dot(x,d)+(dot(x,c)-1)/delta;assert k<0
  planes.append(tuple(-v/k for v in (dot(x,a),dot(x,b),dot(x,c)-1)))
 # CCW bounded planar faces, CW outer face: reverse outward dual orientation.
 f2=[list(reversed(cy)) for cy in faces]
 left={}
 for fi,cy in enumerate(f2):
  for i,j in zip(cy,cy[1:]+cy[:1]):assert (i,j) not in left;left[i,j]=fi
 edges=sorted({tuple(sorted(e)) for e in left});weights=[]
 for i,j in edges:
  e=sub(R[j][:2],R[i][:2]);J=(-e[1],e[0]);diff=sub(planes[left[i,j]][:2],planes[left[j,i]][:2]);w=dot(diff,J)/dot(e,e)
  assert diff==mul(w,J)
  assert planes[left[i,j]][2]-planes[left[j,i]][2]==-w*dot(J,R[i][:2])
  assert (w<0)==(outer in (left[i,j],left[j,i]));weights.append(w)
 # Full equilibrium, including the recovered negative boundary stresses.
 forces=[[F(0),F(0)] for q in Q]
 for (i,j),w in zip(edges,weights):
  for k in range(2):forces[i][k]+=w*(R[j][k]-R[i][k]);forces[j][k]-=w*(R[j][k]-R[i][k])
 assert all(v==[0,0] for v in forces)
 for q,r in zip(Q,R):
  den=1+r[2]/delta;assert den>0
  assert q==add(c,mul(1/den,add(add(mul(r[0],a),mul(r[1],b)),mul(r[2],d))))
  for fi,cy in enumerate(f2):
   if Q.index(q) in cy:assert r[2]==dot(planes[fi],(r[0],r[1],F(1)))
 out=dict(outer=outer,boundary=faces[outer],Q=Q,X=X,faces=f2,edges=edges,weights=weights,R=R,planes=planes,c=c,a=a,b=b,d=d,delta=delta)
 return out

if __name__=='__main__':
 out=recover(int(sys.argv[1]) if len(sys.argv)>1 else None);path=Path(__file__).with_name('chart_exact.json');path.write_text(json.dumps(encode(out),sort_keys=True,separators=(',',':')))
 w=[v for v in out['weights'] if v>0]
 bits=lambda a:max(max(abs(F(x).numerator).bit_length(),F(x).denominator.bit_length()) for x in a)
 print('EXACT_PROJECTIVE_STRESS_RECOVERY_PASS',out['outer'],out['boundary'],'delta',float(out['delta']),'w',float(min(w)),float(max(w)),'weightbits',bits(out['weights']),'Rbits',bits(sum((list(p) for p in out['R']),[])),'sha',hashlib.sha256(path.read_bytes()).hexdigest())

END FILE methods/chart.py

FILE methods/chart_audit.py 5051 aadc679f483288ceb36a934c745e46aa2caab0e85481dace5c48a413144b16f4
"""Exact common-boundary projective chart, full self-stress and Maxwell round trips.
Only finite H generators and exact auditors are authoritative inputs.
"""
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from collections import deque,defaultdict
sys.path.insert(0,str(Path(__file__).parent/'parent'))
from check_A import dot,cross,add,sub,mul,det,encode
from chart import load,recover,inv3
sys.set_int_max_str_digits(0)

def stats(values):
 vals=[]
 def rec(x):
  if isinstance(x,(tuple,list)):
   for v in x:rec(v)
  else:vals.append(F(x))
 rec(values)
 return dict(numerator=max(abs(v.numerator).bit_length() for v in vals),denominator=max(v.denominator.bit_length() for v in vals))

def verify_geometry(Q,seed,calibrate=True):
 faces=seed['faces'];outer=seed['outer'];boundary=seed['boundary'];Q0=seed['Q']
 # Unique origin-fixing linear calibration of the three outer vertices.
 T=[inv3([Q[i] for i in boundary],[Q0[i][k] for i in boundary]) for k in range(3)] if calibrate else [(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]
 QQ=[tuple(dot(row,q) for row in T) for q in Q]
 assert all(QQ[i]==Q0[i] for i in boundary)
 # Preserve the parent's fixed Schlegel map, including its delta.
 a,b,c,d,delta=[seed[k] for k in ('a','b','c','d','delta')];D=det(a,b,d)
 rows=[mul(1/D,cross(b,d)),mul(1/D,cross(d,a)),mul(1/D,cross(a,b))]
 R=[];planes=[];X=[]
 for q in QQ:
  p=tuple(dot(row,sub(q,c)) for row in rows);de=1-p[2]/delta;assert de>0;R.append(mul(1/de,p))
 for f,cy in enumerate(faces):
  x=inv3([QQ[i] for i in cy[:3]],[F(1)]*3);X.append(x)
  assert all(dot(x,QQ[i])==1 for i in cy)
  assert all(dot(x,q)<=1 for q in QQ)
  if f==outer:planes.append((F(0),)*3);continue
  k=dot(x,d)+(dot(x,c)-1)/delta;assert k<0,'viewpoint no longer Schlegel'
  planes.append(tuple(-v/k for v in (dot(x,a),dot(x,b),dot(x,c)-1)))
 left={}
 for f,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):left[i,j]=f
 edges=seed['edges'];W=[];zero=[];outer_edges=[];forces=[[F(0),F(0)] for _ in Q]
 for e,(i,j) in enumerate(edges):
  v=sub(R[j][:2],R[i][:2]);J=(-v[1],v[0]);L,H=left[i,j],left[j,i]
  diff=sub(planes[L][:2],planes[H][:2]);w=dot(diff,J)/dot(v,v);W.append(w)
  assert diff==mul(w,J) and planes[L][2]-planes[H][2]==-w*dot(J,R[i][:2])
  if outer in (L,H):assert w<0;outer_edges.append(e)
  else:assert w>=0
  if w==0:zero.append(e)
  for k in range(2):forces[i][k]+=w*(R[j][k]-R[i][k]);forces[j][k]-=w*(R[j][k]-R[i][k])
 assert all(f==[0,0] for f in forces)
 # The positive-edge Dirichlet graph reaches the boundary, so harmonic positions are unique.
 adj=defaultdict(list)
 for (i,j),w in zip(edges,W):
  if w>0:adj[i].append(j);adj[j].append(i)
 seen=set(boundary);todo=list(boundary)
 while todo:
  i=todo.pop()
  for j in adj[i]:
   if j not in seen:seen.add(j);todo.append(j)
 assert len(seen)==len(Q)
 # Independently integrate the face-gradient/intercept cocycle from a zero root plane.
 dual=defaultdict(list)
 for e,(i,j) in enumerate(edges):
  L,H=left[i,j],left[j,i]
  if outer in (L,H):continue
  v=sub(R[j][:2],R[i][:2]);J=(-v[1],v[0]);jump=mul(W[e],(J[0],J[1],-dot(J,R[i][:2])))
  dual[H].append((L,jump));dual[L].append((H,mul(-1,jump)))
 root=next(f for f in range(len(faces)) if f!=outer);p={root:(F(0),)*3};dq=deque([root])
 while dq:
  f=dq.popleft()
  for g,jump in dual[f]:
   if g not in p:p[g]=add(p[f],jump);dq.append(g)
   else:assert p[g]==add(p[f],jump)
 assert len(p)==len(faces)-1
 h=[]
 for i in range(len(Q)):
  vals=[dot(p[f],(*R[i][:2],F(1))) for f,cy in enumerate(faces) if i in cy and f!=outer]
  assert len(set(vals))==1;h.append(vals[0])
 affine=inv3([(*R[i][:2],F(1)) for i in boundary],[h[i] for i in boundary])
 h=[v-dot(affine,(*R[i][:2],F(1))) for i,v in enumerate(h)]
 assert h==[r[2] for r in R]
 for q,qhat,r in zip(Q,QQ,R):
  de=1+r[2]/delta;assert de>0
  back=add(c,mul(1/de,add(add(mul(r[0],a),mul(r[1],b)),mul(r[2],d))))
  assert back==qhat and inv3(T,back)==q
 result=dict(outer_panel=outer,boundary=boundary,old_edges=edges,zero_edges=zero,zero_endpoint_pairs=[edges[e] for e in zero],negative_outer_edges=outer_edges,positive_interior_count=sum(w>0 for w in W),calibration=T,weights=W,projected=R,face_planes=planes,delta=delta,a=a,b=b,c=c,d=d,weight_bits=stats(W),projection_bits=stats(R),calibration_bits=stats(T),exact_equilibrium_residual_zero=True,positive_dirichlet_connected=True,exact_maxwell_roundtrip=True,exact_inverse_roundtrip=True)
 return encode(result)

if __name__=='__main__':
 root=Path(__file__).parent;folder=root/(sys.argv[1] if len(sys.argv)>1 else 'exact10000000000');seed=recover();raw=json.loads((folder/'raw.json').read_text());Q=[tuple(F(v,row[3]) for v in row[:3]) for row in raw['H']]
 out=verify_geometry(Q,seed);data=json.dumps(out,sort_keys=True,separators=(',',':')).encode();(folder/'STRESS.json').write_bytes(data)
 print('COMMON_CHART_EXACT_HARMONIC_MAXWELL_INVERSE_PASS',out['zero_endpoint_pairs'],out['positive_interior_count'],out['weight_bits'],'bytes',len(data),'sha',hashlib.sha256(data).hexdigest(),flush=True)

END FILE methods/chart_audit.py

FILE methods/contact.py 4391 689d8219dfe04529948100f8ac118d2cc97a9b83dd2826c6243aaed8cdf9077c
"""Full contact equations and analytic own-filled-mass derivatives; no fixed drawing."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np,json,copy
import sys
sys.set_int_max_str_digits(0)
from pathlib import Path
from scipy.optimize import least_squares
ROOT=Path(__file__).parent

def contact(data,coordinates,free,derivatives=True):
 Y=np.array(data['controls'],float)/data['grid'];n=len(free);DY=np.zeros((len(Y),3,n));Y[data['n_supports']]=[0,0,1]
 for k,(i,a) in enumerate(free):Y[i,a]=coordinates[k];DY[i,a,k]=1
 for i,deps,axes in data['plan']:
  if not deps:continue
  rest=[k for k in range(3) if k not in axes];A=Y[np.ix_(deps,axes)]
  Y[i,axes]=np.linalg.solve(A,1-Y[np.ix_(deps,rest)]@Y[i,rest])
  if derivatives:
   rhs=-np.einsum('c,acp->ap',Y[i],DY[deps])
   if rest:rhs-=Y[np.ix_(deps,rest)]@DY[i,rest]
   DY[i,axes]=np.linalg.solve(A,rhs)
 return Y,DY

import itertools

class Atlas:
 def escape(self,A,DA,forced=None,blocked=()):
  e=A[None,:,:]-A[:,None,:];aa=np.sum(A*A,axis=1);ee=np.sum(e*e,axis=2);den=np.sqrt(np.maximum(aa[:,None]*ee,1e-40));vals=np.einsum('ik,ijk->ij',A,e)/den;np.fill_diagonal(vals,-1e10)
  for i,j in blocked:vals[i,j]=-1e10
  js=np.argmax(vals,axis=1)
  for ii,jj in (forced or {}).items():js[ii]=jj
  i=np.arange(len(A));v=vals[i,js];d=A[js]-A;dd=np.sum(d*d,axis=1);de=DA[js]-DA;den=np.sqrt(np.maximum(aa*dd,1e-40))
  Dv=(np.einsum('ic,icp->ip',d,DA)+np.einsum('ic,icp->ip',A,de))/den[:,None]-v[:,None]*(np.einsum('ic,icp->ip',A,DA)/aa[:,None]+np.einsum('ic,icp->ip',d,de)/np.maximum(dd[:,None],1e-40))
  return v,Dv
 def evaluate(self,z,refresh=False):
  if not refresh and self.last is not None and np.array_equal(z,self.last[0]):return self.last[1:]
  Y,DY=contact(self.G,self.base+self.scale*z,self.free);DY=DY*self.scale[None,None,:];Q=Y[:self.nq];DQ=DY[:self.nq]
  X=np.empty((self.nv,3));DX=np.empty((self.nv,3,self.n));ix=self.direct>=0;X[ix]=Y[self.direct[ix]];DX[ix]=DY[self.direct[ix]]
  As=Q[self.trip];X[self.simple]=np.linalg.solve(As,np.ones((len(self.simple),3,1)))[:,:,0]
  DX[self.simple]=np.linalg.solve(As,-np.einsum('nc,nacp->nap',X[self.simple],DQ[self.trip]))
  a,b,c=X[self.tris[:,0]],X[self.tris[:,1]],X[self.tris[:,2]];da,db,dc=DX[self.tris[:,0]],DX[self.tris[:,1]],DX[self.tris[:,2]]
  v6=np.einsum('ic,ic->i',a,np.cross(b,c));dv6=np.einsum('ic,icp->ip',np.cross(b,c),da)+np.einsum('ic,icp->ip',np.cross(c,a),db)+np.einsum('ic,icp->ip',np.cross(a,b),dc)
  V=v6.sum()/6;DV=dv6.sum(axis=0)/6;M=(v6[:,None]*(a+b+c)).sum(axis=0)/24;DM=(np.einsum('ip,ic->cp',dv6,a+b+c)+np.einsum('i,icp->cp',v6,da+db+dc))/24;g=M/V;Dg=(DM-g[:,None]*DV)/V
  Z=X-g;DZ=DX-Dg;h=1-Q@g;Dh=-np.einsum('icp,c->ip',DQ,g)-Q@Dg;H=Q/h[:,None];DH=DQ/h[:,None,None]-Q[:,:,None]*Dh[:,None,:]/h[:,None,None]**2
  ep,dep=self.escape(Z,DZ,self.forcedp,getattr(self,'blockedp',()));eq,deq=self.escape(H,DH,self.forcedq,getattr(self,'blockedq',()))
  mech=np.r_[ep[self.keptp],eq[self.keptq],-ep[self.U],-eq[getattr(self,'S',3)]];dmech=np.vstack((dep[self.keptp],deq[self.keptq],-dep[self.U],-deq[getattr(self,'S',3)]))
  slack=1-Q@X.T;masked=np.where(self.mask,slack,np.inf);arg=masked.argmin(axis=1);cs=slack[np.arange(self.nq),arg];dcs=-np.einsum('icp,ic->ip',DQ,X[arg])-np.einsum('ic,icp->ip',Q,DX[arg])
  val=np.r_[mech,cs,v6/self.tscale,h,V];jac=np.vstack((dmech,dcs,dv6/self.tscale[:,None],Dh,DV))
  geo=dict(Q=Q,X=X,V=V,g=g,M=M,v6=v6,slack=masked,Y=Y,DQ=DQ,DX=DX,Dg=Dg,DY=DY)
  self.last=(np.array(z).copy(),val,jac,geo);return val,jac,geo
 def residual(self,z):
  v,J,g=self.evaluate(z);active=v<self.floor
  return np.maximum(self.floor-v,0)/self.rescale
 def derivative(self,z):
  v,J,g=self.evaluate(z);return -J/self.rescale[:,None]*(v<self.floor)[:,None]


def install(s,Q):
 def point(ids):
  tri=max(itertools.combinations(ids,3),key=lambda p:abs(np.linalg.det(Q[list(p)])))
  return np.linalg.solve(Q[list(tri)],np.ones(3))
 shift=np.array([0.,0.,1.])-point(s.G['groups'][0]);Q=Q/(1+Q@shift)[:,None]
 X=np.array([point(g) for g in s.G['groups']]);Y=np.vstack((Q,X));s.base=np.array([Y[i,a] for i,a in s.free]);s.last=None
 YY,DY=contact(s.G,s.base,s.free);s.scale=1/np.maximum(1.,np.linalg.norm(DY[:s.nq].reshape(-1,s.n),axis=0));s.tscale=np.ones(len(s.tris));s.last=None
 v,J,g=s.evaluate(np.zeros(s.n));s.tscale=np.maximum(abs(g['v6']),1e-10);s.last=None
 return Y


END FILE methods/contact.py

FILE methods/flexible.py 3258 50801763e1109ae271004866896206613b96b3f7fd4e17c4785b83228a278ef5
"""Generic full contact atlas on an independently reconstructed physical complex."""
from contact import *
from fractions import Fraction as F
class FlexibleAtlas(Atlas):
 def __init__(self,G,rep,Qinit,S=3,root_floors=None):
  self.G=copy.deepcopy(G);self.parents=rep;self.forcedp={};self.forcedq={};self.nq=G['n_supports'];self.S=S
  assert rep['active_input_indices']==list(range(self.nq))
  axes={i:ax for i,deps,ax in G['plan']};self.free=[(i,k) for i in range(len(G['controls'])) if i!=self.nq for k in range(3) if k not in axes[i]];self.n=len(self.free)
  self.base=np.array([G['controls'][i][a]/G['grid'] for i,a in self.free]);self.scale=np.ones(self.n);self.nv=rep['V'];self.mechlen=self.nv+self.nq
  self.owners=[[f for f,cy in enumerate(rep['faces']) if v in cy] for v in range(self.nv)]
  self.U=next(v for v,row in enumerate(rep['raw_vertices']) if list(map(F,row))==[0,0,1])
  self.faces=rep['faces'];self.tris=np.array([(cy[0],cy[k],cy[k+1]) for cy in self.faces for k in range(1,len(cy)-1)])
  groups={frozenset(g):self.nq+k for k,g in enumerate(G['groups'])};self.direct=np.array([groups.get(frozenset(o),-1) for o in self.owners]);self.simple=np.where(self.direct<0)[0];assert all(len(self.owners[v])==3 for v in self.simple)
  self.trip=np.array([self.owners[v] for v in self.simple]);self.mask=np.ones((self.nq,self.nv),bool)
  for v,own in enumerate(self.owners):self.mask[own,v]=False
  self.keptp=np.array([i for i in range(self.nv) if i!=self.U]);self.keptq=np.array([i for i in range(self.nq) if i!=S]);self.last=None;self.tscale=np.ones(len(self.tris));install(self,Qinit)
  v,J,g=self.evaluate(np.zeros(self.n));self.floor=np.zeros(len(v));self.floor[:self.mechlen-2]=3e-7
  self.floor[self.mechlen-2:self.mechlen]=np.maximum(v[self.mechlen-2:self.mechlen]*.5,1e-7) if root_floors is None else root_floors
  self.floor[self.mechlen:self.mechlen+self.nq]=1e-7;self.floor[self.mechlen+self.nq:self.mechlen+self.nq+len(self.tris)]=.001;self.floor[-self.nq-1:-1]=.001;self.floor[-1]=.02
  self.rescale=np.ones(len(v));self.rescale[:self.mechlen]=1e-3;self.rescale[self.mechlen:self.mechlen+self.nq]=1e-3

def delete_generator(G,target,Q):
 """Remove one support and its contacts; free one coordinate in affected point solves."""
 G=copy.deepcopy(G);n=G['n_supports'];assert 0<=target<n
 Y=np.vstack((Q,[np.linalg.solve(Q[list(max(itertools.combinations(ids,3),key=lambda a:abs(np.linalg.det(Q[list(a)]))))],np.ones(3)) for ids in G['groups']]))
 mapping={i:i-(i>target) for i in range(len(G['controls'])) if i!=target};plan=[];changed=[]
 for i,deps,axes in G['plan']:
  if i==target:continue
  dd=[v for v in deps if v!=target];aa=axes
  if len(dd)!=len(deps):
   aa=list(max(itertools.combinations(axes,len(dd)),key=lambda ax:abs(np.linalg.det(Y[np.ix_(dd,ax)])) if dd else 1.));changed.append([i,deps,axes,dd,aa])
  plan.append([mapping[i],[mapping[v] for v in dd],aa])
 G['controls']=[row for i,row in enumerate(G['controls']) if i!=target];G['n_supports']=n-1;G['groups']=[[mapping[i] for i in ids if i!=target] for ids in G['groups']];G['plan']=plan
 assert all(len(g)>=3 for g in G['groups']);return G,dict(deleted_original_support=target,old_to_new={str(i):j for i,j in mapping.items()},changed_plan_before_reindexing=changed)

END FILE methods/flexible.py

FILE methods/general_atlas.py 4142 5c9de823cc692105d765953aaed7c22261dac6726056f82e944e61b0b5a3801a
"""A full rational contact atlas for any eligible second triangle-panel union."""
from contact import *
import itertools
class GeneralAtlas(Atlas):
 def __init__(self,edge,Qinit):
  self.G=G=json.loads((ROOT/'parent/GENERATOR.json').read_text());rep=json.loads((ROOT/'baseline/A.json').read_text());chart=json.loads((ROOT/'chart_exact.json').read_text());self.parents=rep;self.forcedp={};self.forcedq={};self.edge=edge;root=rep['unstable_vertices'][0];assert len(rep['unstable_vertices'])==1
  pair=chart['edges'][edge];owners=[[f for f,cy in enumerate(rep['faces']) if v in cy] for v in range(rep['V'])];ends=[i for i,o in enumerate(owners) if all(q in o for q in pair)];assert len(ends)==2 and all(len(owners[i])==3 for i in ends) and root not in ends
  gone,keep=sorted(ends);union=sorted(set(owners[gone]+owners[keep]));assert len(union)==4
  plan={i:(deps,axes) for i,deps,axes in G['plan']};used={d for _,deps,_ in G['plan'] for d in deps};eligible=[i for i in pair if not plan[i][0] and i not in used];assert eligible,'No unused free endpoint for this contact atlas'
  def pt(ids):
   tri=max(itertools.combinations(ids,3),key=lambda a:abs(np.linalg.det(Qinit[list(a)])))
   return np.linalg.solve(Qinit[list(tri)],np.ones(3))
  shift=np.array([0.,0.,1.])-pt(G['groups'][0]);Qinit=Qinit/(1+Qinit@shift)[:,None];x=pt(union)
  chosen=max(eligible,key=lambda v:abs(np.linalg.det(Qinit[[q for q in union if q!=v]])));axis=int(np.argmax(abs(x)));new=len(G['controls'])
  G['controls'].append(np.rint(x*G['grid']).astype(np.int64).tolist());G['groups'].append(union);G['plan']=[r for r in G['plan'] if r[0]!=chosen]+[[new,[q for q in union if q!=chosen],[0,1,2]],[chosen,[new],[axis]]]
  self.patch=dict(edge=edge,pair=pair,gone=gone,keep=keep,union=union,new_node=new,solved_support=chosen,axis=axis)
  axes={i:ax for i,deps,ax in G['plan']};self.free=[(i,k) for i in range(len(G['controls'])) if i!=137 for k in range(3) if k not in axes[i]];self.n=len(self.free);self.base=np.array([G['controls'][i][a]/G['grid'] for i,a in self.free]);self.scale=np.ones(self.n)
  old=[i for i in range(rep['V']) if i!=gone];mapping={v:i for i,v in enumerate(old)};mapping[gone]=mapping[keep];owners[keep]=union;self.owners=[owners[i] for i in old];self.oldids=old;self.U=mapping[root];self.nv=len(old);self.nq=137;self.mechlen=self.nv+self.nq;self.merged=mapping[keep]
  faces=[]
  for cy in rep['faces']:
   cc=[mapping[i] for i in cy];out=[]
   for v in cc:
    if not out or v!=out[-1]:out.append(v)
   if out[0]==out[-1]:out.pop()
   assert len(set(out))==len(out) and len(out)>=3;faces.append(out)
  self.faces=faces;self.tris=np.array([(cy[0],cy[k],cy[k+1]) for cy in faces for k in range(1,len(cy)-1)])
  groups={frozenset(g):137+k for k,g in enumerate(G['groups'])};self.direct=np.array([groups.get(frozenset(o),-1) for o in self.owners]);self.simple=np.where(self.direct<0)[0];assert all(len(self.owners[v])==3 for v in self.simple);self.trip=np.array([self.owners[v] for v in self.simple]);self.mask=np.ones((137,self.nv),bool)
  for v,own in enumerate(self.owners):self.mask[own,v]=False
  self.keptp=np.array([i for i in range(self.nv) if i!=self.U]);self.keptq=np.array([i for i in range(137) if i!=3]);self.last=None;self.tscale=np.ones(len(self.tris));install(self,Qinit)
  val,jac,geo=self.evaluate(np.zeros(self.n));self.floor=np.zeros(len(val));self.floor[:self.mechlen-2]=3e-7
  from fractions import Fraction as F
  Xp=np.array([[float(F(v)) for v in row] for row in rep['raw_vertices']]);g=np.array([float(F(v)) for v in rep['raw_centroid']]);raw=json.loads((ROOT/'baseline/raw.json').read_text())['H'];qq=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw]);hh=qq/(1-qq@g)[:,None]
  ep,_=self.escape(Xp-g,np.zeros((*Xp.shape,self.n)));eq,_=self.escape(hh,np.zeros((*hh.shape,self.n)));self.floor[self.mechlen-2:self.mechlen]=[-ep[root]*.5,-eq[3]*.5]
  self.floor[self.mechlen:self.mechlen+137]=1e-7;self.floor[self.mechlen+137:self.mechlen+137+len(self.tris)]=.001;self.floor[-138:-1]=.001;self.floor[-1]=.02
  self.rescale=np.ones(len(val));self.rescale[:self.mechlen]=1e-3;self.rescale[self.mechlen:self.mechlen+137]=1e-3

END FILE methods/general_atlas.py

FILE methods/minnorm_qp.py 2459 0839c57dadcb51883760b1eac9c7f5c8a3a52566c59873e5de74fb73cb722301
"""Dual active-set minimum-norm halfspace projection, with equality elimination.
Numerical proposal solver. All returned inequalities are checked in original scale.
"""
import time
import numpy as np
from scipy.linalg import qr,solve_triangular

def solve(A,b,E=None,r=None,bound=.02,tol=2e-9,seconds=8,maxsteps=2000):
 t0=time.monotonic();A=np.asarray(A,float);b=np.asarray(b,float);n=A.shape[1]
 if E is None or len(E)==0:x0=np.zeros(n);P=np.eye(n)
 else:
  E=np.asarray(E,float);r=np.asarray(r,float);Q,R=qr(E.T,mode='economic',check_finite=False);x0=Q@solve_triangular(R.T,r,lower=True,check_finite=False);P=np.eye(n)-Q@Q.T
 if bound is not None:A=np.r_[A,np.eye(n),-np.eye(n)];b=np.r_[b,-np.ones(n)*bound,-np.ones(n)*bound]
 B=A@P;d=b-A@x0;sc=np.linalg.norm(B,axis=1);zero=sc<1e-13
 if np.any(d[zero]>tol):return None,{'why':'zero-row','steps':0}
 sc=np.maximum(sc,1e-13);B=B/sc[:,None];d=d/sc
 y=np.zeros(n);W=[];lam=np.empty(0);removes=0;inner=0
 for it in range(maxsteps):
  v=B@y-d;i=int(np.argmin(v));vmin=v[i]
  if vmin>=-tol:
   x=x0+y
   if np.min((A@x-b)/np.maximum(np.linalg.norm(A,axis=1),1e-13))<-5*tol:return None,{'why':'postguard','steps':it}
   return x,{'why':'pass','steps':it,'active':len(W),'removes':removes,'sec':time.monotonic()-t0,'min':float(vmin)}
  if time.monotonic()-t0>seconds:return None,{'why':'time','steps':it,'active':len(W),'sec':time.monotonic()-t0,'min':float(vmin)}
  if i in W:return None,{'why':'working-error','min':float(vmin),'steps':it}
  ln=0.
  while True:
   inner+=1
   if inner>maxsteps*5:return None,{'why':'inner-budget','steps':it}
   if W:
    Q,R=qr(B[W].T,mode='economic',check_finite=False)
    try:rr=solve_triangular(R,Q.T@B[i],check_finite=False)
    except Exception:return None,{'why':'singular','steps':it}
    z=B[i]-Q@(Q.T@B[i])
   else:rr=np.empty(0);z=B[i].copy()
   zz=float(z@z);full=(d[i]-B[i]@y)/zz if zz>1e-20 else np.inf
   rates=np.divide(lam,rr,out=np.full_like(lam,np.inf),where=rr>1e-11);j=int(np.argmin(rates)) if len(rates) else -1;part=rates[j] if j>=0 else np.inf
   if full< -tol:return None,{'why':'overshot','steps':it,'full':full}
   t=min(full,part)
   if not np.isfinite(t) or t>1e15:return None,{'why':'infeasible-or-illconditioned','steps':it,'zz':zz}
   t=max(t,0.);y+=t*z;lam-=t*rr;ln+=t
   if full<=part:
    W.append(i);lam=np.r_[lam,ln];break
   else:
    W.pop(j);lam=np.delete(lam,j);removes+=1
 return None,{'why':'budget','steps':maxsteps,'active':len(W)}

END FILE methods/minnorm_qp.py

FILE methods/numeric.py 6623 53aec445d2ec1ace09dc69708c4f30dd9e4a2c12b83e4dbad6a4a849259ec199
"""Numerical proposals only: faithful stress solve, Maxwell lift, inverse map and filled mass."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');os.environ.setdefault('OMP_NUM_THREADS','1')
import json
from fractions import Fraction
from pathlib import Path
import numpy as np
import scipy.linalg as la
from collections import defaultdict,deque
from scipy.spatial import ConvexHull

class Chart:
 def __init__(self,root=None):
  directory=Path(root) if root is not None else Path(__file__).parent
  data=json.loads((directory/'chart_exact.json').read_text())
  def arr(k):return np.array(data[k],dtype=object).astype(str)
  def num(x):return float(Fraction(x))
  def nums(x):return np.vectorize(num)(np.array(x,dtype=object))
  self.data=data;self.Q=nums(data['Q']);self.X=nums(data['X']);self.R=nums(data['R']);self.w=nums(data['weights']);self.faces=data['faces'];self.edges=np.array(data['edges'],int);self.outer=data['outer'];self.boundary=np.array(data['boundary'],int)
  self.delta=num(data['delta']);self.c=nums(data['c']);self.basis=np.array([nums(data[k]) for k in ('a','b','d')]);self.n=len(self.Q);self.nf=len(self.faces)
  self.left={}
  for f,cy in enumerate(self.faces):
   for i,j in zip(cy,cy[1:]+cy[:1]):self.left[i,j]=f
  self.ef=np.array([[self.left[i,j],self.left[j,i]] for i,j in self.edges]);self.inner=np.array([i for i in range(self.n) if i not in self.boundary]);self.ie=np.where(np.all(self.ef!=self.outer,axis=1))[0]
  inc=np.zeros((self.n,len(self.edges)))
  for k,(i,j) in enumerate(self.edges):inc[i,k]=1;inc[j,k]=-1
  self.Bi=inc[self.inner][:,self.ie];self.Bb=inc[self.boundary][:,self.ie]
  self.rb=self.R[self.boundary,:2];self.Ainv=np.linalg.inv(np.column_stack((self.rb,np.ones(3))))
  links=defaultdict(list)
  for k,(L,R) in enumerate(self.ef):
   if self.outer not in (L,R):links[R].append((L,k,1));links[L].append((R,k,-1))
  root=next(f for f in range(self.nf) if f!=self.outer);seen={root};dq=deque([root]);T=np.zeros((self.nf,len(self.edges)))
  while dq:
   f=dq.popleft()
   for g,e,s in links[f]:
    if g not in seen:T[g]=T[f];T[g,e]+=s;seen.add(g);dq.append(g)
  assert len(seen)==self.nf-1
  self.T=T[:,self.ie];self.vf=np.array([next(f for f,cy in enumerate(self.faces) if v in cy and f!=self.outer) for v in range(self.n)])
  self.physical_faces=json.loads((directory/'baseline/A.json').read_text())['faces']
  self.triples=np.array([f[:3] for f in self.faces]);self.ptris=np.array([(cy[0],cy[k],cy[k+1]) for cy in self.physical_faces for k in range(1,len(cy)-1)])
  self.parent_pedges=np.array(json.loads((directory/'baseline/A.json').read_text())['edges'])
 def solve(self,w,normalize=True):
  wi=w[self.ie];L=(self.Bi*wi)@self.Bi.T;rhs=-((self.Bi*wi)@self.Bb.T)@self.rb
  r=np.empty((self.n,2));r[self.boundary]=self.rb;r[self.inner]=la.solve(L,rhs,assume_a='pos',check_finite=False)
  e=r[self.edges[self.ie,1]]-r[self.edges[self.ie,0]];J=e[:,::-1]*[-1,1];off=-np.einsum('ij,ij->i',J,r[self.edges[self.ie,0]])
  planes=self.T@(wi[:,None]*np.column_stack((J,off)))
  h=np.einsum('ij,ij->i',planes[self.vf],np.column_stack((r,np.ones(self.n))))
  h-=np.column_stack((r,np.ones(self.n)))@(self.Ainv@h[self.boundary]);h[self.boundary]=0
  if normalize: h*=self.R[:,2].sum()/h.sum()
  den=1+h/self.delta
  if den.min()<=0:raise ValueError('inverse pole')
  Q=self.c+(np.column_stack((r,h))@self.basis)/den[:,None]
  return Q, r,h
 def fixed(self,Q):
  X=np.linalg.solve(Q[self.triples],np.ones((self.nf,3,1)))[:,:,0]
  tr=X[self.ptris];vol6=np.einsum('ij,ij->i',tr[:,0],np.cross(tr[:,1],tr[:,2]));V=vol6.sum()/6
  c=(vol6[:,None]*tr.sum(axis=1)).sum(axis=0)/(24*V)
  return X,V,c
 def actual(self,Q,tol=1e-9):
  hull=ConvexHull(Q)
  # plane equations provide vertices of P; merge planar Q triangles only for numeric screening.
  pq=-hull.equations[:,:3]/hull.equations[:,3,None]
  X=[];owners=[]
  for v in pq:
   if not any(np.linalg.norm(v-x)<tol for x in X):
    X.append(v);owners.append(np.where(np.abs(Q@v-1)<tol)[0].tolist())
  X=np.array(X);faces=[];normals=[];labels=[];edges=defaultdict(list);tris=[]
  for f,q in enumerate(Q):
   ids=np.where(np.abs(X@q-1)<tol)[0]
   if len(ids)<3:continue
   centre=X[ids].mean(axis=0);u=X[ids[0]]-centre;u/=np.linalg.norm(u);v=np.cross(q,u);v/=np.linalg.norm(v)
   cy=ids[np.argsort(np.arctan2((X[ids]-centre)@v,(X[ids]-centre)@u))].tolist()
   # discard collinear numerical points
   changed=True
   while changed and len(cy)>3:
    changed=False
    for k in range(len(cy)):
     if np.linalg.norm(np.cross(X[cy[k]]-X[cy[k-1]],X[cy[(k+1)%len(cy)]]-X[cy[k]]))<1e-12:
      del cy[k];changed=True;break
   fi=len(faces);faces.append(cy);normals.append(q);labels.append(f)
   for i,j in zip(cy,cy[1:]+cy[:1]):edges[tuple(sorted((i,j)))].append(fi)
   tris.extend((cy[0],cy[k],cy[k+1]) for k in range(1,len(cy)-1))
  if not all(len(fs)==2 for fs in edges.values()):raise ValueError('numeric incidence')
  tr=X[np.array(tris)];v6=np.einsum('ij,ij->i',tr[:,0],np.cross(tr[:,1],tr[:,2]));V=v6.sum()/6;c=(v6[:,None]*tr.sum(axis=1)).sum(axis=0)/(24*V)
  if V<=0 or np.min(1-Q@c)<=0:raise ValueError('noninterior mass')
  Z=X-c;H=Q/(1-Q@c)[:,None]
  qdots=H@H.T;fs=qdots.diagonal()-qdots.max(axis=1) # always <=0 incl self
  S=np.where(np.all(qdots<=qdots.diagonal()[:,None]+1e-12,axis=1))[0].tolist()
  pmax=(Z@Z.T-np.sum(Z*Z,axis=1)[:,None]);np.fill_diagonal(pmax,-np.inf);U=np.where(pmax.max(axis=1)<1e-11)[0].tolist()
  E=[]
  for (i,j),ff in edges.items():
   e=Z[j]-Z[i];ee=e@e;t=-Z[i]@e/ee
   if not 0<t<1:continue
   n,m=np.array(normals)[ff];p=Z[i]+t*e;aa=n@n;bb=n@m;cc=m@m;rr=p@n;ss=p@m
   if min(rr*cc-ss*bb,ss*aa-rr*bb)>1e-12:E.append((i,j))
  return dict(V=len(X),E=len(edges),F=len(faces),counts=[len(S),len(U),len(E)],volume=V,centroid=c.tolist(),S=S,U=[owners[i] for i in U],H=E,Q=Q.tolist())

if __name__=='__main__':
 c=Chart();Q,r,h=c.solve(c.w);X,V,g=c.fixed(Q)
 print('NUMERICAL_FAITHFUL_CHART',np.max(np.abs(Q-c.Q)),np.max(np.abs(r-c.R[:,:2])),np.max(np.abs(h-c.R[:,2])),V,g)
 a=c.actual(Q);a.pop('Q');print(a)
 if '--screen' in __import__('sys').argv:
  results=[]
  for k in c.ie:
   w=c.w.copy();w[k]=0
   try:
    Q,_,_=c.solve(w);a=c.actual(Q);a.update(edge=int(k),endpoints=c.edges[k].tolist(),weight=float(c.w[k]));a.pop('Q')
   except Exception as e:a=dict(edge=int(k),endpoints=c.edges[k].tolist(),error=str(e))
   results.append(a)
  Path(__file__).with_name('screen.json').write_text(json.dumps(results,indent=2))
  good=[a for a in results if 'counts' in a];good.sort(key=lambda a:(sum(a['counts']),a['E']))
  print('SCREEN',len(results),len(good));print(json.dumps(good[:15],indent=2))

END FILE methods/numeric.py

FILE methods/parent/RECONSTRUCT.py 1801 2a8c5685baa64c8a2e6998f898c889172b7c7f92fbf07ae9cf1d8b8d37e695fd
"""Exact finite reconstruction of an alternating point/support contact atlas."""
import json,sys
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
sys.set_int_max_str_digits(0)

def solve(A,b):
 n=len(A);M=[list(a)+[v] for a,v in zip(A,b)]
 for k in range(n):
  p=next((j for j in range(k,n) if M[j][k]),None);assert p is not None,'singular contact minor'
  M[k],M[p]=M[p],M[k];d=M[k][k];M[k]=[x/d for x in M[k]]
  for j in range(n):
   if j!=k:
    d=M[j][k];M[j]=[x-d*y for x,y in zip(M[j],M[k])]
 return [row[-1] for row in M]

def recover(data):
 D=data['grid'];n=data['n_supports'];assert isinstance(D,int) and D>0
 X=[[F(v,D) for v in row] for row in data['controls']];assert 0<n<len(X)
 X[n]=[F(0),F(0),F(1)];done={n};edges=set()
 for i,deps,axes in data['plan']:
  assert i not in done and set(deps)<=done and len(deps)==len(axes)<=3
  assert len(set(axes))==len(axes) and set(axes)<={0,1,2}
  if deps:
   rest=[k for k in range(3) if k not in axes];A=[[X[j][k] for k in axes] for j in deps];b=[F(1)-sum(X[j][k]*X[i][k] for k in rest) for j in deps];values=solve(A,b)
   for k,v in zip(axes,values):X[i][k]=v
  for j in deps:
   assert (i<n)!=(j<n);assert sum(a*b for a,b in zip(X[i],X[j]))==1;edges.add(tuple(sorted((i,j))))
  done.add(i)
 assert done==set(range(len(X)))
 intended={tuple(sorted((i,n+j))) for j,ids in enumerate(data['groups']) for i in ids};assert edges==intended
 H=[]
 for row in X[:n]:
  den=lcm(*(v.denominator for v in row));num=[int(v*den) for v in row];gg=gcd(*num,den);H.append([v//gg for v in num]+[den//gg])
 assert len(set(map(tuple,H)))==len(H)
 return {'H':H}
if __name__=='__main__':
 data=json.loads(Path(sys.argv[1]).read_text());Path(sys.argv[2]).write_text(json.dumps(recover(data),sort_keys=True,separators=(',',':')))

END FILE methods/parent/RECONSTRUCT.py

FILE methods/parent/centred_mass.py 1328 cc0ad7d58764902ca3d308539f7a133eec0f6fb2389361444808ca92694499a5
"""Third integration: integer tetrahedra based at the object's exact filled centroid."""
import sys,json,time,hashlib
from fractions import Fraction as F
from math import lcm
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def run(a):
 p=[tuple(map(F,row)) for row in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));h=lcm(*(v.denominator for row in p for v in row),*(v.denominator for v in g))
 X=[tuple(int(h*(v-c)) for v,c in zip(row,g)) for row in p]
 V6=0;M24=[0,0,0];num=0
 for cy in a['faces']:
  cy=cy[2:]+cy[:2]
  for j in range(1,len(cy)-1):
   x,y,z=[X[i] for i in (cy[0],cy[j],cy[j+1])];d=dot(x,cross(y,z));assert d>0;V6+=d;num+=1
   for k in range(3):M24[k]+=d*(x[k]+y[k]+z[k])
 assert M24==[0,0,0]
 W=F(V6,6*h**3);assert W==F(a['ordinary_volume'])
 return {'status':'EXACT_CENTRED_INTEGER_TETRAHEDRA_PASS','tetrahedra':num,'common_centred_denominator_bits':h.bit_length(),'common_centred_integer_coordinate_max_bits':max(abs(v).bit_length() for row in X for v in row),'filled_first_moments':[0,0,0],'volume_agrees_with_A_and_B':True}
if __name__=='__main__':
 p=Path(sys.argv[1]);s=run(json.loads(p.read_text()));print(json.dumps(s,sort_keys=True,separators=(',',':')))

END FILE methods/parent/centred_mass.py

FILE methods/parent/check_A.py 5483 ad72cc198140249c1e52a615513354036c04f4c718333a7beed64fba4b43d7f3
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm
import sys,json
sys.set_int_max_str_digits(0)
Z=(0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def sign(x):return (x>0)-(x<0)
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(tuple,list)):return [encode(v) for v in x]
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 return x

def polygon(X,ids,N):
 axis=max(range(3),key=lambda j:abs(N[j]));a,b=[j for j in range(3) if j!=axis];ids=sorted(ids,key=lambda i:(X[i][a],X[i][b]));lo=[];hi=[]
 def turn(i,j,k):return (X[j][a]-X[i][a])*(X[k][b]-X[i][b])-(X[j][b]-X[i][b])*(X[k][a]-X[i][a])
 for seq,out in [(ids,lo),(ids[::-1],hi)]:
  for i in seq:
   while len(out)>1 and turn(out[-2],out[-1],i)<=0:out.pop()
   out.append(i)
 cy=lo[:-1]+hi[:-1]
 if len(cy)<3:return []
 if dot(N,cross(sub(X[cy[1]],X[cy[0]]),sub(X[cy[2]],X[cy[0]])))<0:cy.reverse()
 k=cy.index(min(cy));return cy[k:]+cy[:k]

def run(raw):
 H=[tuple(map(int,r)) for r in raw['H']];assert len(H)>=4 and all(len(r)==4 and r[3]>0 for r in H);assert len(set(H))==len(H)
 N=[r[:3] for r in H];D=[r[3] for r in H];vertices=set();bounded=set()
 for i,j,k in combinations(range(len(H)),3):
  a,b,c=N[i],N[j],N[k];u=cross(b,c);v=cross(c,a);w=cross(a,b);dd=dot(a,u)
  if not dd:continue
  # Six explicit nonnegative cone decompositions certify boundedness.
  for axis in range(3):
   for s in [-1,1]:
    if all(s*t[axis]*dd>=0 for t in (u,v,w)):bounded.add((axis,s))
  p=add(add(mul(D[i],u),mul(D[j],v)),mul(D[k],w))
  if dd<0:p=mul(-1,p);dd=-dd
  if any(dot(n,p)>h*dd for n,h in zip(N,D)):continue
  gg=gcd(*p,dd);vertices.add(tuple(t//gg for t in p)+(dd//gg,))
 assert len(bounded)==6
 X=sorted(tuple(F(t,p[3]) for t in p[:3]) for p in vertices);assert len(X)>=4
 active=[];faces=[]
 for fi,(n,h) in enumerate(zip(N,D)):
  ids=[i for i,x in enumerate(X) if dot(n,x)==h];cy=polygon(X,ids,n) if len(ids)>=3 else []
  if cy:active.append(fi);faces.append(cy)
 normals=[N[i] for i in active];offsets=[D[i] for i in active];edges={};tris=[]
 for fi,cy in enumerate(faces):
  assert set(cy)=={i for i,x in enumerate(X) if dot(normals[fi],x)==offsets[fi]}
  for i,j in zip(cy,cy[1:]+cy[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append((fi,i,j))
  tris.extend((cy[0],cy[j],cy[j+1]) for j in range(1,len(cy)-1))
 assert len(X)-len(edges)+len(faces)==2 and all(len(v)==2 and v[0][1:]==v[1][1:][::-1] for v in edges.values())
 adjacency=[set() for _ in X]
 for i,j in edges:adjacency[i].add(j);adjacency[j].add(i)
 seen=set();todo=[0]
 while todo:
  i=todo.pop()
  if i not in seen:seen.add(i);todo.extend(adjacency[i]-seen)
 assert len(seen)==len(X)
 volume=F(0);moment=Z
 for i,j,k in tris:
  v=det(X[i],X[j],X[k])/6;assert v>0;volume+=v;moment=add(moment,mul(v/4,add(add(X[i],X[j]),X[k])))
 centre=mul(1/volume,moment);assert sub(moment,mul(volume,centre))==Z
 C=lcm(*(x.denominator for x in centre));M=tuple(int(x*C) for x in centre);bs=[lcm(*(v.denominator for v in x)) for x in X];aa=[tuple(int(v*b) for v in x) for x,b in zip(X,bs)];zz=[sub(mul(C,a),mul(b,M)) for a,b in zip(aa,bs)]
 def ed(i,j):return sub(mul(bs[i],aa[j]),mul(bs[j],aa[i]))
 SF=[];SW=[];UV=[];UW=[];EH=[];EW=[];fs=[];vs=[];es=[];fz=0;ez=0
 for fi,cy in enumerate(faces):
  vals=[dot(normals[fi],cross(zz[i],ed(i,j))) for i,j in zip(cy,cy[1:]+cy[:1])];sg=[sign(v) for v in vals];fs.append(sg);fz+=sg.count(0)
  if min(sg)>0:SF.append(fi)
  elif min(sg)>=0:SW.append(fi)
 for i in range(len(X)):
  js=[j for j in range(len(X)) if j!=i];j=js[0];best=dot(zz[i],ed(i,j))
  for k in js[1:]:
   val=dot(zz[i],ed(i,k));cmp=val*bs[j]-best*bs[k]
   if cmp>0 or (cmp==0 and k>j):j=k;best=val
  sg=sign(best);vs.append([j,sg])
  if sg<0:UV.append(i)
  elif sg==0:UW.append(i)
 for (i,j),pair in sorted(edges.items()):
  e=ed(i,j);ee=dot(e,e);ze=dot(zz[i],e);pn=sub(mul(ee,zz[i]),mul(ze,e));n,m=[normals[r[0]] for r in pair];nn=dot(n,n);mm=dot(m,m);nm=dot(n,m);delta=nn*mm-nm*nm;assert delta>0
  vals=[-ze*bs[j],C*ee+ze*bs[j],dot(pn,sub(mul(mm,n),mul(nm,m))),dot(pn,sub(mul(nn,m),mul(nm,n)))];sg=[sign(v) for v in vals];es.append([i,j,*sg]);ez+=sg.count(0)
  if min(sg)>0:EH.append([i,j])
  elif min(sg)>=0:EW.append([i,j])
 assert all(offsets[i]*C-dot(n,M)>0 for i,n in enumerate(normals))
 return encode(dict(V=len(X),E=len(edges),F=len(faces),active_input_indices=active,raw_vertices=X,faces=faces,edges=sorted(edges),normals=normals,offsets=offsets,ordinary_volume=volume,raw_first_moments=moment,raw_centroid=centre,centred_first_moments=Z,centred_centroid=Z,counts=[len(SF),len(UV),len(EH)],weak=[len(SW),len(UW),len(EW)],stable_face_ids=SF,unstable_vertices=UV,saddle_edges=EH,weak_faces=SW,weak_vertices=UW,weak_edges=EW,face_signs=fs,vertex_max_escape_signs=vs,edge_signs=es,face_primitive_zero_count=fz,vertex_max_zero_count=len(UW),edge_primitive_zero_count=ez,edge_primitive_count=4*len(edges),integration_triangle_count=len(tris)))
if __name__=='__main__':
 from pathlib import Path
 raw=json.loads(Path(sys.argv[1]).read_text());out=run(raw);Path(sys.argv[2]).write_text(json.dumps(out,sort_keys=True,separators=(',',':')))
 print('A',out['V'],out['E'],out['F'],out['counts'],out['weak'],flush=True)

END FILE methods/parent/check_A.py

