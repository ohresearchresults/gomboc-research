"""Finite actual-mass retirement screen on an exact deformed selected hull.
All floating coplanarity counts/censuses are nominations, not exact certificates.
"""
import sys,json,time,numpy as np
from scipy.spatial import ConvexHull
from gmpy2 import mpq
from pathlib import Path
from geometry import angular_scores,mass
from support_persistence import ROOT
sys.set_int_max_str_digits(0)
def screen(X,ids):
 P=X[ids];h=ConvexHull(P);tr=h.simplices.copy();n=np.cross(P[tr[:,1]]-P[tr[:,0]],P[tr[:,2]]-P[tr[:,0]]);rev=np.einsum('ij,ij->i',n,h.equations[:,:3])<0;tr[rev]=tr[rev][:,[0,2,1]];v,c=mass(P,tr);Yraw=h.equations[:,:3]/(-h.equations[:,3,None]-h.equations[:,:3]@c[:,None]);Y=[]
 for y in Yraw:
  if not Y or min(np.linalg.norm(np.asarray(Y)-y,axis=1))>1e-7:Y.append(y)
 Y=np.asarray(Y);Z=P-c;ue=angular_scores(Z).max(1);se=angular_scores(Y).max(1)
 return dict(V=len(h.vertices),E=len(h.vertices)+len(Y)-2,F=len(Y),U=int((ue<0).sum()),S=int((se<0).sum()),centroid=c.tolist(),volume=float(v),u_min_nonroot=float(np.sort(ue)[1]),s_min_nonroot=float(np.sort(se)[1]))
if __name__=='__main__':
 source=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'artifacts/contact_atlas/centered_U1_regauged/exact_concave_checkpoint1/audit.json');r=json.loads(source.read_text());X=np.array([[float(mpq(v)) for v in p] for p in r['raw_vertices']]);c=np.array([float(mpq(v)) for v in r['raw_centroid']]);X-=c;u=r['unstable_vertices'][0];out=ROOT/'artifacts/retire_current'/source.parent.name;out.mkdir(parents=True,exist_ok=True);base=screen(X,list(range(len(X))));assert (base['V'],base['E'],base['F'])==(r['V'],r['E'],r['F']);rows=[]
 for i in range(len(X)):
  if i==u:continue
  ids=[j for j in range(len(X)) if j!=i];z=screen(X,ids);z.update(removed=[i],selected=ids,edges_saved=r['E']-z['E'],volume_removed=base['volume']-z['volume'],centroid_norm=float(np.linalg.norm(z['centroid'])));rows.append(z)
 rows.sort(key=lambda z:(z['U']!=1,z['E']>246,z['S'],z['centroid_norm']));(out/'single_screen.json').write_text(json.dumps(dict(source=str(source),baseline=base,rows=rows),indent=2)+'\n');print('SINGLES_BEST',[(z['removed'],z['E'],z['S'],z['U'],z['volume_removed'],z['centroid_norm']) for z in rows[:12]],flush=True)
 # Two-step nominations use actual re-hulled uniform mass at every pair.
 pairs=[];seen=set()
 for first in sorted(rows,key=lambda z:(z['U']!=1,z['centroid_norm']))[:12]:
  for j in first['selected']:
   if j==u:continue
   gone=tuple(sorted(first['removed']+[j]))
   if gone in seen:continue
   seen.add(gone);ids=[k for k in first['selected'] if k!=j];z=screen(X,ids)
   if z['E']>246:continue
   z.update(removed=list(gone),selected=ids,edges_saved=r['E']-z['E'],volume_removed=base['volume']-z['volume'],centroid_norm=float(np.linalg.norm(z['centroid'])));pairs.append(z)
 pairs.sort(key=lambda z:(z['U']!=1,z['S'],z['E']>245,z['centroid_norm']));(out/'pair_screen.json').write_text(json.dumps(dict(source=str(source),rows=pairs),indent=2)+'\n');print('PAIRS_BEST',[(z['removed'],z['E'],z['S'],z['U'],z['volume_removed'],z['centroid_norm']) for z in pairs[:12]],flush=True)
