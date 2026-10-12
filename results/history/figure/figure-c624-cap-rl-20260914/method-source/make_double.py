"""BQ13 stable-cap C626 plus the distinct contact {16,18,71,94}; numerical proposals only.
Exact reconstruction through RECONSTRUCT is mandatory before any acceptance.
"""
import argparse,json,sys,copy,os
from pathlib import Path
import numpy as np
BASE=Path(__file__).resolve().parent
sys.path[:0]=[str(BASE/'parent/mechanism/parent_sources')]
from numeric import recover,merge_faces,mechanics

def build(root,out,axis=2,project=True):
 d=json.loads((root/'GENERATOR.json').read_text());fs=json.loads((root/'faces.json').read_text())
 X=recover(d);own=[[f for f,cy in enumerate(fs) if v in cy] for v in range(max(map(max,fs))+1)]
 a=next(i for i,o in enumerate(own) if o==[16,18,94]);b=next(i for i,o in enumerate(own) if o==[18,71,94])
 assert [i for i,deps,axes in d['plan'] if 18 in deps]==[]
 old=next(t for t in d['plan'] if t[0]==18);assert old[1:]==[[],[]]
 d['plan'].remove(old)
 p=np.linalg.solve(X[[16,71,94]],np.ones(3));q=X[18]
 if project:q=q+(1-q@p)/(p@p)*p
 idx=len(d['controls']);assert idx==d['n_supports']+len(d['groups'])
 d['controls'][18]=np.rint(q*d['grid']).astype(np.int64).tolist()
 d['controls'].append(np.rint(p*d['grid']).astype(np.int64).tolist());d['groups'].append([16,18,71,94])
 d['plan'] += [[idx,[16,71,94],[0,1,2]],[18,[idx],[axis]]]
 nf=merge_faces(fs,a,b)
 out.mkdir(exist_ok=False,parents=True)
 for f,o in [('GENERATOR.json',d),('faces.json',nf)]: (out/f).write_text(json.dumps(o,sort_keys=True,separators=(',',':')))
 XX=recover(d);r=mechanics(XX[:137],nf,tol=1e-12)
 (out/'NUMERICAL.json').write_text(json.dumps(r,indent=2))
 print(out.name,'p',p,'dq18',np.linalg.norm(XX[18]-X[18]),r,flush=True)
 return d,nf,r
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=BASE/'C628_WINNER');p.add_argument('--out',type=Path,required=True);p.add_argument('--axis',type=int,default=2);p.add_argument('--no-project',action='store_true');a=p.parse_args();build(a.root,a.out,a.axis,not a.no_project)
