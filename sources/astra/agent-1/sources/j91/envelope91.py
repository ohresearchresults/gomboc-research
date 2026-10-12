"""U-safe, old-point diameter-ball outer-envelope experiments.
Numerical nomination only: maximal-facet grouping uses a stated tolerance.
All physical volume and centroid values are reintegrated on each actual hull.
"""
from pathlib import Path
import json,sys
import numpy as np
from scipy.spatial import ConvexHull
from j90 import geometry,report,score
from masscaps90 import poly
ROOT=Path(__file__).resolve().parent

def hullpoly(points,tol=2e-8):
 x=np.asarray(points,float);h=ConvexHull(x)
 if np.max(h.equations[:,3])>=0:raise ValueError('origin not interior')
 par=np.arange(len(h.simplices))
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for i,ns in enumerate(h.neighbors):
  for j in ns:
   if j>i and np.linalg.norm(h.equations[i]-h.equations[j])<tol:par[root(j)]=root(i)
 groups={}
 for i in range(len(par)):groups.setdefault(root(i),[]).append(i)
 faces=[]
 for ids in groups.values():
  es={}
  for k in ids:
   t=h.simplices[k]
   for a,b in zip(t,np.roll(t,-1)):
    e=tuple(sorted([int(a),int(b)]));es[e]=es.get(e,0)+1
  boundary=[e for e,v in es.items() if v==1];nb={}
  for a,b in boundary:nb.setdefault(a,[]).append(b);nb.setdefault(b,[]).append(a)
  if not all(len(v)==2 for v in nb.values()):raise ValueError('noncycle boundary')
  start=min(nb);cy=[start];prev=-1;cur=start
  while True:
   nxt=next(t for t in nb[cur] if t!=prev)
   if nxt==start:break
   cy.append(nxt);prev,cur=cur,nxt
   if len(cy)>len(nb):raise ValueError('cycle failure')
  if len(cy)!=len(nb):raise ValueError('disconnected face')
  n=h.equations[ids[0],:3]
  if np.cross(x[cy[1]]-x[cy[0]],x[cy[2]]-x[cy[0]])@n<0:cy.reverse()
  faces.append(cy)
 used=sorted(set(i for f in faces for i in f));mp={v:i for i,v in enumerate(used)}
 out=poly(x[used],[[mp[v] for v in f] for f in faces]);out['labels']=used
 return out

def ref(z):
 r=z.copy();r.update(p=z['x'],q=z['y'],g=np.zeros(3));return report(r)

def support_ball(old,n,slack=1e-4):
 n=np.array(n)/np.linalg.norm(n);r=np.linalg.norm(old,axis=1)
 vals=(old@n+r)/2;i=int(np.argmax(vals))
 w=old[i]/2+(1-slack)*r[i]*n/2
 return w,i,float(w@(old[i]-w)),float(vals[i])

def base():
 raw=np.loadtxt(ROOT/'J90_DETACHED_C390_G8.txt',skiprows=1)/1e8
 z=geometry(raw);return geometry(z['q']),z['g']

def main(mode='greedy',steps=20):
 z,g=base();old=z['x'].copy();points=old.copy();hist=[];best=None
 for k in range(steps):
  zz=hullpoly(points);rr=ref(zz);own=report(zz)
  print('STEP',k,'V/E/F',rr['V'],rr['E'],rr['F'],'referenceSU',len(rr['S']),len(rr['U']), 'Q', [b['depth'] for b in rr['Q']],'ownSU',len(own['S']),len(own['U']),'g',own['centroid'],flush=True)
  rec=dict(step=k,reference=rr,own=own)
  if len(rr['S'])==1:
   rec['note']='reference S1 only; physical centroid still must be repaired';hist.append(rec);break
  junior=rr['Q'][0]['root'];n=zz['y'][junior]
  if mode=='greedy':w,vi,guard,val=support_ball(old,n,1e-3)
  elif mode=='recursive':w,vi,guard,val=support_ball(points,n,1e-3)
  elif mode=='death':
   a,b=rr['Q'][0]['edge'];n=(zz['y'][a]+zz['y'][b])/2;w,vi,guard,val=support_ball(old,n,1e-3)
  else:raise ValueError('mode')
  if np.max(zz['y']@w)<1+1e-8:rec['note']='no strict outward support';hist.append(rec);break
  points=np.vstack([points,w]);rec.update(w=w.tolist(),witness=vi,guard=guard);hist.append(rec)
 (ROOT/f'J91_ENVELOPE_{mode}.json').write_text(json.dumps(dict(mode=mode,slack=.001,initial_shift=g.tolist(),points=points.tolist(),history=hist),indent=2)+'\n')
 print('J91_ENVELOPE_SCOUT_ONLY',mode,flush=True)
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'greedy',int(sys.argv[2]) if len(sys.argv)>2 else 20)
