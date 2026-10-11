"""Actual-complex numerical screen of single support deletions. No exact promotion."""
import sys,json,itertools,argparse
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'parent'));sys.path.insert(0,str(R/'parent/parent/mechanism/parent_sources'))
from numeric import recover,mechanics,topology

def hull(q):
 h=ConvexHull(q); assert np.max(h.equations[:,3])<0
 pts=h.equations[:,:3]/(-h.equations[:,3,None]);groups={}
 for p in pts:
  ids=tuple(np.where(abs(q@p-1)<1e-8)[0]);assert len(ids)>=3
  groups[ids]=p
 owners=sorted(groups);P=[]
 for ids in owners:
  tri=max(itertools.combinations(ids,3),key=lambda j:abs(np.linalg.det(q[list(j)])))
  P.append(np.linalg.solve(q[list(tri)],np.ones(3)))
 P=np.array(P);fs=[]
 for j,v in enumerate(q):
  ids=[i for i,o in enumerate(owners) if j in o];assert len(ids)>=3
  p=P[ids];n=v/np.linalg.norm(v);axis=np.eye(3)[np.argmin(abs(n))];e=np.cross(axis,n);e/=np.linalg.norm(e);b=np.cross(n,e);c=p.mean(0);a=np.arctan2((p-c)@b,(p-c)@e);fs.append(np.array(ids)[np.argsort(a)].tolist())
 topology(fs);return P,fs

def drop_chart(d,lost):
 lost=set(lost);assert not any(lost&set(deps) for i,deps,ax in d['plan'] if i not in lost)
 z=json.loads(json.dumps(d));kept=[i for i in range(len(d['controls'])) if i not in lost];mp={i:k for k,i in enumerate(kept)}
 z['n_supports']-=len(lost);z['controls']=[d['controls'][i] for i in kept];z['groups']=[[mp[i] for i in o if i not in lost] for o in d['groups']];z['plan']=[[mp[i],[mp[j] for j in ds],ax] for i,ds,ax in d['plan'] if i not in lost];return z

def run(a):
 d=json.loads((a.source/'GENERATOR.json').read_text());q=recover(d)[:d['n_supports']];out=a.out;out.mkdir(parents=True,exist_ok=False);rows=[]
 protected={3,17,49,57,73,88,134,135,136,71,94,109,116,119,126} if len(q)==137 else {3,16,48,56,72,87,133,134,135,70,93,108,115,118,125}
 for i in range(len(q)):
  if i in protected:continue
  qq=np.delete(q,i,axis=0)
  try:
   P,fs=hull(qq);z=mechanics(qq,fs,P=P,tol=1e-13)
   rec=dict(deleted=i,**z);rows.append(rec)
   if z['min_gap']>1e-8 and z['max_incidence_error']<1e-8:
    print(i,z['V'],z['E'],z['counts'],z['min_gap'],flush=True)
    try:dd=drop_chart(d,[i])
    except AssertionError:continue
    dr=out/f'DELETE{i}';dr.mkdir();(dr/'GENERATOR.json').write_text(json.dumps(dd,sort_keys=True,separators=(',',':')));(dr/'faces.json').write_text(json.dumps(fs,separators=(',',':')));(dr/'NUMERICAL.json').write_text(json.dumps(rec))
  except Exception as e:print('ERR',i,str(e),flush=True)
 (out/'SCREEN.json').write_text(json.dumps(rows,sort_keys=True,separators=(',',':')))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,default=R/'parent/BASIN69_96');p.add_argument('--out',type=Path,required=True);run(p.parse_args())
