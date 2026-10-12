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
