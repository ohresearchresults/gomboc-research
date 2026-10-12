"""Reproduce scoped numerical forest findings and exact owner-label bijections."""
import json,sys,hashlib
from pathlib import Path
import numpy as np
from forest_repair import Atlas,paths
from active_repair import rooted
R=Path(__file__).resolve().parent

def owner_sets(faces):
 n=1+max(max(cy) for cy in faces);out=[set() for _ in range(n)]
 for f,cy in enumerate(faces):
  for v in cy:out[v].add(f)
 return [tuple(sorted(x)) for x in out]
def labels(reference,exact):
 aa=owner_sets(reference);bb=owner_sets(exact);assert len(set(aa))==len(aa) and set(aa)==set(bb)
 where={o:i for i,o in enumerate(bb)};mapping=[where[o] for o in aa]
 for cy,cz in zip(reference,exact):
  moved=[mapping[i] for i in cy];assert len(moved)==len(cz)
  assert any(moved==cz[k:]+cz[:k] for k in range(len(cz)))
 return mapping

def probe(inp):
 d=json.loads((inp/'GENERATOR.json').read_text());ref=inp/'TOPOLOGY.json'
 fs=json.loads(ref.read_text()) if ref.exists() else json.loads((inp/'A.json').read_text())['faces']
 m=Atlas(d,fs);s=m.state(m.u0,False);um=np.zeros((len(m.owners),len(m.owners)),bool);sm=np.zeros((m.nphys,m.nphys),bool)
 for (i,j),ff in m.ef.items():um[i,j]=um[j,i]=True;sm[tuple(ff)]=sm[tuple(ff[::-1])]=True
 result={}
 for name,cos,root,mask in [('primal',s['cu'],m.Uroot,um),('polar',s['cs'],m.Sroot,sm)]:
  z={}
  for strategy in ['widest','additive']:
   pa,dist=rooted(cos,root,mask) if strategy=='widest' else paths(cos,root,mask,np.full(len(mask),1e-7))
   co=cos[np.arange(len(mask)),pa];z[strategy]=dict(root=root,negative=[[i,int(pa[i]),float(co[i])] for i in range(len(mask)) if i!=root and co[i]<0],L2shortfall=float(np.linalg.norm(np.maximum(1e-7-np.delete(co,root),0))))
  result[name]=z
 result['positive_primal_outdegrees']={str(int(k)):int(v) for k,v in zip(*np.unique(np.sum(um&(s['cu']>0),axis=1),return_counts=True))}
 result['own_centroid']=s['c'].tolist();result['min_offincidence_gap']=float(s['gaps'][~m.inc].min())
 return result
if __name__=='__main__':
 p=Path(sys.argv[1]);print(json.dumps(probe(p),sort_keys=True,separators=(',',':')))
