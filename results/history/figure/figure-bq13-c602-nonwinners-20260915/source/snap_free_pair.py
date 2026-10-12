"""Finite stratum replacement for a vanishing free-point edge.
Removes collapsed maximal facets instead of preserving their old triangles.
"""
import sys,json,itertools,argparse
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'parent'))
from blowup_edge import Model
from numeric import mechanics,topology
from atlas_opt import Atlas

def construct(data,fs,an,bn,u):
 m=Model(data,fs,an,bn);X=m.chart(u,False);X[bn]=X[an];av=m.ai;bv=m.bi
 va=lambda i:(av if i==bv else i)-((av if i==bv else i)>bv)
 ff=[];removed=[]
 for fi,cy in enumerate(fs):
  cc=[]
  for v in cy:
   v=va(v)
   if not cc or cc[-1]!=v:cc.append(v)
  if cc[0]==cc[-1]:cc.pop()
  if len(cc)<3:removed.append(fi)
  else:assert len(set(cc))==len(cc);ff.append(cc)
 for i in removed:assert not any(i in deps for j,deps,axes in data['plan'])
 removed_nodes=set(removed)|{bn};kept=[i for i in range(len(X)) if i not in removed_nodes];ix={i:j for j,i in enumerate(kept)};ix[bn]=ix[an]
 d=json.loads(json.dumps(data));d['n_supports']-=len(removed);d['controls']=np.rint(X[kept]*d['grid']).astype(np.int64).tolist()
 groups=[]
 for j,ids in enumerate(data['groups']):
  i=data['n_supports']+j
  if i==bn:continue
  if i==an:ids=sorted(set(ids)|set(data['groups'][bn-data['n_supports']]))
  groups.append([ix[k] for k in ids if k not in removed])
 d['groups']=groups;plan=[]
 for i,deps,axes in data['plan']:
  if i in removed_nodes:continue
  ds=list(dict.fromkeys(an if j==bn else j for j in deps));assert not set(ds)&set(removed)
  if len(ds)!=len(deps):axes=list(max(itertools.combinations(range(3),len(ds)),key=lambda ax:abs(np.linalg.det(X[np.ix_(ds,ax)]))))
  plan.append([ix[i],[ix[j] for j in ds],axes])
 d['plan']=plan;topology(ff)
 return d,ff,dict(pair_construction=[av,bv],pair_aux=[an,bn],discarded_input_supports=removed,input_support_to_new={i:ix[i] for i in range(data['n_supports']) if i not in removed},epsilon=float(m.epsilon(u)))
def main(a):
 d=json.loads((a.source/'GENERATOR.json').read_text());fs=json.loads((a.source/'faces.json').read_text());u=np.load(a.checkpoint)['u'];dd,ff,info=construct(d,fs,a.an,a.bn,u);a.out.mkdir(parents=True,exist_ok=False)
 for n,o in [('GENERATOR.json',dd),('faces.json',ff),('CHANGE.json',info),('CHECKPOINT.json',dict(u_hex=[float(v).hex() for v in u],an=a.an,bn=a.bn))]: (a.out/n).write_text(json.dumps(o,sort_keys=True,separators=(',',':')))
 m=Atlas(dd,ff);s=m.state(m.u0,False);rep=mechanics(s['q'],ff,P=s['P'],tol=1e-13);(a.out/'NUMERICAL.json').write_text(json.dumps(rep));print('FINITE',info,rep,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,default=R/'parent/BASIN69_96');p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--an',type=int,required=True);p.add_argument('--bn',type=int,required=True);p.add_argument('--out',type=Path,required=True);main(p.parse_args())
