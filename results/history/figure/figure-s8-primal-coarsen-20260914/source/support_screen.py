"""Numerical support-deletion screen; not a rational certificate."""
import numpy as np,json,sys,os
from pathlib import Path
from scipy.spatial import HalfspaceIntersection,ConvexHull,cKDTree
sys.path.insert(0,str(Path(os.environ['S8_SOURCE'])/'parent/mechanism/parent_sources'))
from numeric import mechanics
from deletion import Model,canon

def hull(q):
 P=HalfspaceIntersection(np.c_[q,-np.ones(len(q))],np.zeros(3)).intersections
 # S8's separated physical vertices permit this proposer-only clustering threshold.
 pairs=cKDTree(P).query_pairs(1e-7);parent=list(range(len(P)))
 def root(i):
  while parent[i]!=i:i=parent[i]
  return i
 for i,j in pairs:parent[root(j)]=root(i)
 groups={}
 for i in range(len(P)):groups.setdefault(root(i),[]).append(i)
 P=np.array([P[g].mean(0) for g in groups.values()]);P=P[np.lexsort(P.T[::-1])]
 fs=[];active=[];gap=1-P@q.T
 for f,n in enumerate(q):
  ids=np.where(np.abs(gap[:,f])<1e-8)[0]
  if len(ids)<3:continue
  axes=[i for i in range(3)if i!=np.abs(n).argmax()];ix=ConvexHull(P[ids][:,axes]).vertices if len(ids)>3 else range(3);cy=ids[ix].tolist()
  if np.dot(n,np.cross(P[cy[1]]-P[cy[0]],P[cy[2]]-P[cy[0]]))<0:cy.reverse()
  fs.append(cy);active.append(f)
 return P,fs,active
if __name__=='__main__':
 from fractions import Fraction as F
 raw=json.loads(Path(sys.argv[1]).read_text());m=Model(raw);H=json.loads(Path(sys.argv[2]).read_text())['H'];new=m.plane([127,133,136]);H.append(new);q=np.array([[float(F(a,h[-1]))for a in h[:3]]for h in H]);out=Path(sys.argv[3]);out.mkdir(exist_ok=True);rows=[]
 for d in range(len(q)):
  idx=[i for i in range(len(q))if i!=d];qk=q[idx]
  try:
   P,faces,act=hull(qk);r=mechanics(qk[act],faces,P=P,tol=1e-13);r.update(deleted_support=d,active_original=[idx[i]for i in act]);r['C']=2*r['E'];rows.append(r)
   if sum(r['counts'])<=8:print(d,r['C'],r['counts'],r['U'],r['H'],flush=True)
  except Exception as e:rows.append(dict(deleted_support=d,error=repr(e)))
 (out/'D132_single_supports.json').write_text(canon(rows));print('D132_SINGLE_SUPPORT_SCREEN_DONE',len(rows),flush=True)
