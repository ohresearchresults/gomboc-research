"""Literal support deletion with exact inherited/new contact identities.

Qhull nominates the dual triangulation. Old coplanarity is looked up by exact
source incidence; new intersections and contacts use rational arithmetic.
Every reference110 nomination is independently re-hulled and audited exactly.
The old mass centroid is only a reference point for this screen.
"""
import argparse,json,itertools,time,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from gmpy2 import mpq
from exact_projective_audit import inverse,apply
from exact_audit_vertices import check_B,dot
from support_geometry import escape
from persistence_birth import bars_loss

def run(source,out):
 source=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=False);a=json.loads((source/'audit.json').read_text());raw=json.loads((source/'raw.json').read_text());P=[tuple(map(mpq,x))for x in a['raw_vertices']];norms=[tuple(map(mpq,x))for x in a['normals']];offs=list(map(mpq,a['offsets']));g0=list(map(mpq,a['raw_centroid']));Y=np.array([[float(v/(h-dot(n,g0)))for v in n]for n,h in zip(norms,offs)]);oldtriples={};incs=[set()for _ in P]
 for f,cy in enumerate(a['faces']):
  for i in cy:incs[i].add(f)
 for i,inc in enumerate(incs):
  for tri in itertools.combinations(sorted(inc),3):oldtriples[tri]=i
 records=[];start=time.time()
 for gone in range(a['F']):
  keep=np.array([i for i in range(a['F'])if i!=gone]);YY=Y[keep];refS=int(np.sum(escape(YY)[0]<0));row=dict(deleted=gone,reference_S=refS)
  if refS!=1:records.append(row);continue
  try:
   hull=ConvexHull(YY);assert max(hull.equations[:,3])<0,'unbounded support deletion';points={};pointincs={}
   for tt in keep[hull.simplices]:
    tri=tuple(sorted(map(int,tt)))
    if tri in oldtriples:
     i=oldtriples[tri];p=P[i];inc=incs[i]-{gone}
    else:
     p=tuple(apply(inverse([norms[i]for i in tri]),[offs[i]for i in tri]));slack=[offs[i]-dot(norms[i],p)for i in keep];assert min(slack)>=0,'nominated new intersection not exactly feasible';inc={int(i)for i,s in zip(keep,slack)if s==0}
    points[p]=p;pointincs[p]=inc
   PP=list(points);X=np.array([[float(v-cc)for v,cc in zip(p,g0)]for p in PP]);refU=int(np.sum(escape(X)[0]<0));row.update(reference_U=refU,V=len(X),F=len(keep),E=len(X)+len(keep)-2)
   if refU!=1:records.append(row);continue
   faces=[]
   for f,y in zip(keep,YY):
    ids=[i for i,p in enumerate(PP)if f in pointincs[p]];assert len(ids)>=3;cent=X[ids].mean(0);normal=y/np.linalg.norm(y);e=X[ids[0]]-cent;e/=np.linalg.norm(e);b=np.cross(normal,e);ang=np.arctan2((X[ids]-cent)@b,(X[ids]-cent)@e);faces.append([ids[i]for i in np.argsort(ang)])
   ed=sorted({tuple(sorted((i,j)))for cy in faces for i,j in zip(cy,cy[1:]+cy[:1])});assert len(ed)==row['E'];T=np.array([(cy[0],cy[k],cy[k+1])for cy in faces for k in range(1,len(cy)-1)]);u,v,w=X[T[:,0]],X[T[:,1]],X[T[:,2]];v6=np.einsum('ic,ic->i',u,np.cross(v,w));cent=np.sum(v6[:,None]*(u+v+w),axis=0)/(4*sum(v6));Z=X-cent;H=YY/(1-YY@cent)[:,None];row.update(own_S=int(np.sum(escape(H)[0]<0)),own_U=int(np.sum(escape(Z)[0]<0)),mass=cent.tolist(),mass_norm=float(np.linalg.norm(cent)),gain=a['E']-row['E']);d=out/f'delete{gone}';d.mkdir();np.savez(d/'reference_geometry.npz',X=X,Y=YY);proposal=dict(raw_vertices=X.tolist(),raw_halfspaces=[list(y)+[1.]for y in YY],V=len(X),F=len(YY),E=len(ed),faces=faces,edges=ed,active=list(range(len(YY))),source=str(source.resolve()),source_audit_sha256=hashlib.sha256((source/'audit.json').read_bytes()).hexdigest(),deleted=gone,source_reference_centroid=list(map(str,g0)),scope='exact incidence, numerical geometry in the old exact centroid frame; own-centroid audit separate');(d/'reference_proposal.json').write_text(json.dumps(proposal,indent=2));literal={'H':[list(map(str,(*n,h)))for i,(n,h)in enumerate(zip(norms,offs))if i!=gone]};(d/'raw.json').write_text(json.dumps(literal,sort_keys=True,separators=(',',':')));B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode();aa=check_B.run(literal);(d/'audit.json').write_bytes(B(aa));row.update(exact_counts=aa['counts'],exact_weak=aa['weak'],exact_VEF=[aa[k]for k in ['V','E','F']],audit_sha256=hashlib.sha256((d/'audit.json').read_bytes()).hexdigest(),path=str(d));assert [row[k]for k in ['V','E','F']]==row['exact_VEF'];print('REFERENCE110_LITERAL_DELETION',row,flush=True)
  except(ValueError,AssertionError,np.linalg.LinAlgError)as err:row.update(error=repr(err))
  records.append(row);(out/'screen.json').write_text(json.dumps(records,indent=2))
 (out/'screen.json').write_text(json.dumps(records,indent=2));print('REFERENCE110_DELETION_DONE',dict(seconds=time.time()-start,total=len(records),reference110=sum('exact_counts'in r for r in records)),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');a=p.parse_args();run(a.source,a.out)
