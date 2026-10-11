"""One-coordinate integer-grid repairs, screened by the full filled-mass Jacobian.
The numerical screen does not certify the exact endpoint.
Usage: integer_patch.py BQ_SOURCE source_dir fresh_output
"""
from pathlib import Path
import json,sys,math
import numpy as np
base,src,out=map(lambda s:Path(s).resolve(),sys.argv[1:]);sys.path[:0]=[str(base/'parent/mechanism/parent_sources')]
from atlas_opt import Atlas
from numeric import recover,mechanics
pd=json.loads((base/'BASIN69_96/GENERATOR.json').read_text());pf=json.loads((base/'BASIN69_96/faces.json').read_text());pm=Atlas(pd,pf);ps=pm.state(pm.u0,False);pa=ps['cu'].argmax(1);a=pm.owners.index([16,18,94]);b=pm.owners.index([18,71,94]);alias=lambda i:(a if i==b else i)-(i>b);pp=[]
for i in range(len(pa)):
 if i==b:continue
 j=int(pa[i]);seen={i}
 while j in (a,b):
  assert j not in seen;seen.add(j);j=int(pa[j])
 pp.append(alias(j))
d=json.loads((src/'GENERATOR.json').read_text());fs=json.loads((src/'faces.json').read_text());m=Atlas(d,fs);m.uparent=np.array(pp);m.sparent=ps['cs'].argmax(1);s=m.state(m.u0);J=s['J']/(d['grid']*m.scale)[None,:]
print('BEFORE',s['vals'].min(),'free',m.np,flush=True);proposals=[]
for goal in [3e-8,1e-8,1e-9]:
 rhs=goal-s['vals']
 for j in range(m.np):
  v=J[:,j];pos=v>1e-20;neg=v<-1e-20
  if np.any(rhs[~(pos|neg)]>0):continue
  low=max(-1000.,float(np.max(rhs[pos]/v[pos])) if pos.any() else -1000.)
  high=min(1000.,float(np.min(rhs[neg]/v[neg])) if neg.any() else 1000.)
  lo,hi=math.ceil(low),math.floor(high)
  if lo>hi:continue
  x=lo if lo>0 else hi if hi<0 else 0
  proposals.append((abs(x),-goal,j,x))
proposals.sort();print('LINEAR_FEASIBLE',len(proposals),proposals[:8],flush=True)
for _,ng,j,delta in proposals:
 z=json.loads(json.dumps(d));i,k=map(int,m.free[j]);z['controls'][i][k]+=delta
 X=recover(z);report=mechanics(X[:m.n],fs,tol=1e-13)
 if report['counts']!=[1,1,0] or report['min_gap']<=0 or report['max_incidence_error']>1e-10:continue
 out.mkdir(parents=True,exist_ok=False)
 (out/'GENERATOR.json').write_text(json.dumps(z,sort_keys=True,separators=(',',':')));(out/'faces.json').write_text(json.dumps(fs,separators=(',',':')))
 (out/'NUMERICAL.json').write_text(json.dumps(report,indent=2));patch=dict(grid=d['grid'],control=i,axis=k,integer_delta=delta,linear_goal=-ng)
 (out/'PATCH.json').write_text(json.dumps(patch,sort_keys=True,separators=(',',':')));print('INTEGER_PATCH_NUMERICAL_OWN110',patch,report,flush=True);break
else: print('NO_ONE_COORDINATE_PATCH_IN_FINITE_SCREEN',flush=True)
