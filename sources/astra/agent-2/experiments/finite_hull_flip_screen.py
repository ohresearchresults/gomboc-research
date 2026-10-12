"""Finite primal hull edge flips nominated by near-contact facet/vertex pairs.
Coordinates actually move across a supporting plane. The new convex hull and
actual mass/census are computed, not an integration triangulation relabeling.
"""
import sys,json,hashlib,time,numpy as np
from io import BytesIO
from pathlib import Path
from scipy.spatial import ConvexHull
from canonical_atlas import ROOT,Chart
from geometry import angular_scores,mass
sys.path.insert(0,str(ROOT/'sources'));from peer_agent3_persistence_birth import evaluate
folder=ROOT/sys.argv[1];src=folder/sys.argv[2];out=folder/sys.argv[3];out.mkdir(exist_ok=False);raw=src.read_bytes();(out/'source_q.npy').write_bytes(raw);c=Chart(folder);g=c.graph(np.load(BytesIO(raw)));X=g['X'];Y=g['Y'];assert len(X)<=84 and all(len(f)==3 for f in c.meta['faces']);np.save(out/'source_X.npy',X);original={tuple(sorted(face)) for face in c.meta['faces']};gaps=1-Y@X.T;fi,vi=np.where(~c.incidence);ix=np.argsort(gaps[fi,vi]);seen=set();rows=[];start=time.time()
for idx in ix:
 f,v=int(fi[idx]),int(vi[idx]);adjacent=[j for j,face in enumerate(c.meta['faces']) if v in face and len(set(face)&set(c.meta['faces'][f]))==2]
 if not adjacent:continue
 key=tuple(sorted(set(c.meta['faces'][f])|{v}))
 if key in seen:continue
 seen.add(key)
 for factor in [.1,1.,4.,16.,64.]:
  P=X.copy();P[v]+=(1+factor)*gaps[f,v]*Y[f]/(Y[f]@Y[f])
  try:
   h=ConvexHull(P);faces={tuple(sorted(face)) for face in h.simplices};removed=sorted(original-faces);added=sorted(faces-original)
   if not removed or not added:continue
   value,G,info=evaluate(P,.00001);Z=P-np.array(info['centroid']);H=-h.equations[:,:3]/(h.equations[:,3]+h.equations[:,:3]@np.array(info['centroid']))[:,None];U=int((angular_scores(Z[h.vertices]).max(1)<0).sum());S=int((angular_scores(H).max(1)<0).sum());row=dict(facet=f,vertex=v,neighbors=adjacent,gap=float(gaps[f,v]),factor=factor,V=len(h.vertices),E_upper=3*len(h.vertices)-6,S=S,U=U,Pmax=info['Pmax'],Qmax=info['Qmax'],loss=value,removed_facets=[list(x) for x in removed],added_facets=[list(map(int,x)) for x in added],max_displacement=float(np.linalg.norm(P-X,axis=1).max()));rows.append(row)
   if S==1 and U<=2:
    name=f'f{f}_v{v}_x{factor}';row['coordinates']=name+'.npy';np.save(out/row['coordinates'],P);print('PHYSICAL_FLIP121',row,flush=True)
  except (ValueError,AssertionError,np.linalg.LinAlgError):continue
 if len(seen)>=35:break
rows.sort(key=lambda r:(r['S']+r['U'],r['Pmax']+r['Qmax']));(out/'screen.json').write_text(json.dumps(dict(source=str(src),source_q_sha256=hashlib.sha256(raw).hexdigest(),elapsed=time.time()-start,rows=rows),indent=2)+'\n');print('FINITE_FLIP_SCREEN_DONE',len(rows),'seconds',time.time()-start,flush=True)
