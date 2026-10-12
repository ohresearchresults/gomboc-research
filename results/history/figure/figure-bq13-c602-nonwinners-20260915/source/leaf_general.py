"""Leaf contact with arbitrary nonsimple keeper and existing linear contacts.
Only finite exact rational rechart, not epsilon size, removes strata.
"""
import sys,json,itertools,argparse
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent
sys.path[:0]=[str(R/'parent/parent/mechanism'),str(R/'parent/parent/mechanism/parent_sources')]
from atlas_opt import Atlas
from numeric import recover,topology,mechanics
from leaf_contract import Leaf as OldLeaf,run,dump
PRESERVE_DROP=False

def finite(data,fs,keep,drop,moved,X):
 d=json.loads(json.dumps(data));d['controls']=np.rint(X*d['grid']).astype(np.int64).tolist();n=d['n_supports'];owners,ef=topology(fs)
 assert tuple(sorted([keep,drop])) in ef
 assert set(owners[drop])-set(owners[keep])=={moved}
 assert not any(moved in deps for i,deps,ax in d['plan'])
 union=sorted(set(owners[keep])|set(owners[drop]));found=[n+i for i,g in enumerate(d['groups']) if set(g)==set(owners[keep])]
 assert not any(set(g)==set(owners[drop]) for g in d['groups']), 'a represented disappearing point needs an explicit alias'
 if found:pidx=found[0];d['groups'][pidx-n]=union
 else:
  assert len(owners[keep])==3;pidx=len(X);p=np.linalg.solve(X[owners[keep]],np.ones(3));X=np.vstack([X,p]);d['controls'].append(np.rint(p*d['grid']).astype(np.int64).tolist());d['groups'].append(union);d['plan'].append([pidx,owners[keep],[0,1,2]])
 st=next(z for z in d['plan'] if z[0]==moved);d['plan'].remove(st);deps=st[1]+[pidx];ax=list(max(itertools.combinations(range(3),len(deps)),key=lambda a:abs(np.linalg.det(X[np.ix_(deps,a)]))));d['plan'].append([moved,deps,ax])
 vid={i:k for k,i in enumerate(i for i in range(len(owners)) if i!=drop)};vid[drop]=vid[keep];ff=[];lost=[]
 for fi,cy in enumerate(fs):
  cc=[]
  for i in cy:
   v=vid[i]
   if not cc or cc[-1]!=v:cc.append(v)
  if len(cc)>1 and cc[-1]==cc[0]:cc.pop()
  if len(cc)<3:lost.append(fi)
  else:assert len(set(cc))==len(cc);ff.append(cc)
 assert 3 not in lost
 ix={i:k for k,i in enumerate(i for i in range(len(X)) if i not in lost)}
 d['n_supports']-=len(lost);d['controls']=[v for i,v in enumerate(d['controls']) if i not in lost]
 d['groups']=[[ix[i] for i in g if i not in lost]for g in d['groups']];pp=[]
 for i,deps,ax in d['plan']:
  if i in lost:continue
  ds=[j for j in deps if j not in lost]
  if len(ds)!=len(deps):ax=list(max(itertools.combinations(range(3),len(ds)),key=lambda a:abs(np.linalg.det(X[np.ix_(ds,a)])))) if ds else []
  pp.append([ix[i],[ix[j]for j in ds],ax])
 d['plan']=pp;topology(ff);return d,ff

class Leaf(OldLeaf):
 def __init__(self,d,fs,keep=26,drop=19,moved=113,release=False):
  self.ready=False;Atlas.__init__(self,d,fs);self.keep=keep;self.drop=drop;self.moved=moved
  assert not any(moved in deps for i,deps,ax in d['plan'])
  old=next(t for t in d['plan'] if t[0]==moved);self.olddeps=old[1];oldax=old[2];assert len(oldax)<3
  assert set(self.owners[drop])-set(self.owners[keep])=={moved}
  X=recover(d);self.full_supports=np.array(self.owners[keep]);self.supports=np.array(max(itertools.combinations(self.owners[keep],3),key=lambda z:abs(np.linalg.det(X[list(z)]))))
  p=np.linalg.solve(X[self.supports],np.ones(3));rows=np.vstack([X[self.olddeps],p]);options=[j for j in range(3)if j not in oldax]
  self.axis=max(options,key=lambda k:abs(np.linalg.det(rows[:,oldax+[k]])));self.solveaxes=oldax+[self.axis];self.rest=[k for k in range(3)if k not in self.solveaxes]
  assert abs(np.linalg.det(rows[:,self.solveaxes]))>1e-12
  self.epindex=next(j for j,(i,k) in enumerate(self.free) if i==moved and k==self.axis);delta=1-X[moved]@p;self.u0[self.epindex]=delta/self.scale[self.epindex];self.ready=True
  self.guard=~self.inc.copy();self.guard[drop,self.full_supports]=False;self.guard[keep,moved]=False
  self.vanish=np.array([keep in t and drop in t for t in self.tri])
  if release:self.ui=np.array([i for i in self.ui if i not in ([keep] if PRESERVE_DROP else [keep,drop])])
  s=self.state(self.u0,False);self.floor=np.maximum(5e-8,np.minimum(1e-5,s['vals']*.5));assert np.all(s['vals']>self.floor)
  self.geofloor=np.maximum(1e-9,np.minimum(1e-6,s['gaps']*.01));self.release=release
 def chart(self,u,jac=True):
  if not self.ready:return Atlas.chart(self,u,jac)
  if jac:X,DX=Atlas.chart(self,u,True)
  else:X=Atlas.chart(self,u,False)
  p=np.linalg.solve(X[self.supports],np.ones(3));V=np.vstack([X[self.olddeps],p]);rhs=np.ones(len(V));rhs[-1]-=self.epsilon(u);i=self.moved;ax=self.solveaxes;rest=self.rest
  X[i,ax]=np.linalg.solve(V[:,ax],rhs-V[:,rest]@X[i,rest])
  if jac:
   dp=np.linalg.solve(X[self.supports],-np.einsum('rcp,c->rp',DX[self.supports],p));DV=np.concatenate([DX[self.olddeps],dp[None,:,:]],axis=0);rr=-np.einsum('rcp,c->rp',DV,X[i]);rr[-1,self.epindex]-=self.scale[self.epindex]
   if rest:rr-=V[:,rest]@DX[i,rest]
   DX[i,ax]=np.linalg.solve(V[:,ax],rr);return X,DX
  return X
 def state(self,u,jac=True):
  if not self.ready or not PRESERVE_DROP:return Atlas.state(self,u,jac)
  if hasattr(self,'uparent'):del self.uparent
  pre=Atlas.state(self,u,False);up=pre['cu'].argmax(1);row=pre['cu'][self.drop].copy();row[self.keep]=-np.inf;up[self.drop]=row.argmax();self.uparent=up
  return Atlas.state(self,u,jac)
 def endpoint(self,u):return finite(self.data,self.faces,self.keep,self.drop,self.moved,self.chart(u,False))

if __name__=='__main__':
 import leaf_contract
 leaf_contract.Leaf=Leaf
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--keep',type=int,required=True);p.add_argument('--drop',type=int,required=True);p.add_argument('--moved',type=int,required=True);p.add_argument('--release',action='store_true');p.add_argument('--steps',type=int,default=80);p.add_argument('--preserve-drop',action='store_true');a=p.parse_args();PRESERVE_DROP=a.preserve_drop;run(a)
