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
