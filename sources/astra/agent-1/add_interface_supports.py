"""Allocate up to four formerly inactive supports at the live Q-death interface."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,pathlib,argparse
from geometry import halfspace_mesh,census,arrows
from persistence_search import pairs,polar_edges

def add(input,out,count=4):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);Q=np.load(input)['Q'];m=halfspace_mesh(Q);Q=Q[m['active']];m=halfspace_mesh(Q);P=m['X']-m['g'];R=Q/(1-Q@m['g'])[:,None];eq=polar_edges(m);pp,h=pairs(R,eq);rr=(R*R).sum(1);j=int(np.argmax(1-h[pp[:,1]]/rr[pp[:,0]]));qedge=set(eq[pp[j,1]].tolist());inc={}
 for f,cy in zip(m['active'],m['faces']):
  for u,v in zip(cy,cy[1:]+cy[:1]):inc.setdefault(tuple(sorted((u,v))),[]).append(int(f))
 edge=next(e for e,ff in inc.items() if set(ff)==qedge);candidates=list(edge)
 for v in edge:
  candidates.extend(j if i==v else i for i,j in m['edges'] if i==v or j==v)
 candidates=list(dict.fromkeys(candidates));U=set(np.flatnonzero(arrows(P).max(1)<0));candidates=[v for v in candidates if v not in U];targets=m['X'][candidates].copy();history=[]
 for target in targets:
  if len(history)>=count:break
  m=halfspace_mesh(Q);v=int(np.argmin(np.linalg.norm(m['X']-target,axis=1)))
  if np.linalg.norm(m['X'][v]-target)>1e-7:continue
  owners=np.flatnonzero(abs(Q@target-1)<1e-8);q=Q[owners].mean(0);vals=m['X']@q;others=np.delete(vals,v);pos=others[others>0];bound=float(np.min(1/pos-1));assert bound>0
  for rate in [0.1,0.03,0.01,0.003,0.001,0.0003,0.0001,0.00003]:
   candidate=np.vstack([Q,q*(1+rate*bound)])
   try:mm=halfspace_mesh(candidate);st=census(mm)
   except Exception:continue
   if st['S']==2 and st['U']==1:
    Q=candidate;history.append(dict(target=target.tolist(),owners=owners.tolist(),relative_plane_change=rate*bound,rate=rate,**st));print('ADDED',len(history),st['V'],st['E'],st['F'],rate*bound,flush=True);break
 np.savez(out/'seed.npz',Q=Q);(out/'history.json').write_text(json.dumps(history,indent=2));(out/'SOURCE.json').write_text(json.dumps({'input':str(pathlib.Path(input).resolve()),'Qdeath_edge':list(qedge),'physical_death_edge':list(edge),'requested':count,'added':len(history)},indent=2));print('FINAL',census(halfspace_mesh(Q)),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--input',required=True);ap.add_argument('--out',required=True);ap.add_argument('--count',type=int,default=4);a=ap.parse_args();add(a.input,a.out,a.count)
