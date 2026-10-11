"""Exact supporting-plane reconstruction from Qhull proposals, numerical mechanics screen.
Qhull is only a proposer: every new plane is checked against all retained exact
vertices and the assembled exact-plane complex must be closed and Eulerian.
Final equilibrium acceptance belongs to independent rational auditors, not here.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from itertools import combinations
import json,sys,time
import numpy as np
from scipy.spatial import ConvexHull
sys.set_int_max_str_digits(0)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(k,a):return tuple(k*x for x in a)
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
class Model:
 def __init__(self,raw):
  self.raw=raw;self.Xq=[tuple(F(a)for a in p)for p in raw['vertices']];self.X=np.array(self.Xq,float);self.owners=[set()for _ in self.X]
  for f,cy in enumerate(raw['faces']):
   for v in cy:self.owners[v].add(f)
  self.hom=[]
  for p in self.Xq:
   d=lcm(*(a.denominator for a in p));self.hom.append(tuple(int(a*d)for a in p)+(d,))
  self.planes={};self.cache={};self.newids={};self.originalplanes={}
  for f,cy in enumerate(raw['faces']):
   h=self.plane(cy[:3]);self.originalplanes[f]=h
 def plane(self,tri):
  tri=tuple(sorted(map(int,tri)))
  if tri in self.cache:return self.cache[tri]
  a,b,c=[self.hom[i]for i in tri]
  u=sub(mul(a[3],b[:3]),mul(b[3],a[:3]));v=sub(mul(a[3],c[:3]),mul(c[3],a[:3]));n=cross(u,v)
  if n==(0,0,0):raise ValueError('collinear proposal')
  h=(*mul(a[3],n),dot(n,a[:3]));g=gcd(*h);h=tuple(t//g for t in h)
  if h[3]<0:h=tuple(-t for t in h)
  assert h[3]>0,'origin lost'
  self.cache[tri]=h;return h
 def hull(self,deleted):
  keep=[i for i in range(len(self.X))if i not in deleted];P=self.X[keep];qh=ConvexHull(P);assert len(qh.vertices)==len(keep)
  groups={}
  for loc in qh.simplices:
   tri=tuple(keep[int(i)]for i in loc);common=self.owners[tri[0]]&self.owners[tri[1]]&self.owners[tri[2]]
   h=self.originalplanes[min(common)] if common else self.plane(tri)
   groups.setdefault(h,set()).update(tri)
  orig=set(self.originalplanes.values())
  for h in groups:
   if h not in orig:
    vals={i:dot(h[:3],self.hom[i][:3])-h[3]*self.hom[i][3]for i in keep}
    if max(vals.values())>0:raise ValueError('non-supporting Qhull triangle')
    assert groups[h]=={i for i in keep if vals[i]==0},'incomplete face'
  inv={g:i for i,g in enumerate(keep)};faces=[];H=[]
  for h,ids in sorted(groups.items()):
   # Qhull within a maximal exact plane gives only its polygon, not fan edges.
   ids=sorted(ids);n=np.array([float(F(z,h[3]))for z in h[:3]]);axis=int(np.argmax(np.abs(n)));axes=[j for j in range(3)if j!=axis]
   pts=self.X[ids][:,axes];cy=[ids[k]for k in ConvexHull(pts).vertices] if len(ids)>3 else ids
   assert set(cy)==set(ids)
   if np.dot(n,np.cross(self.X[cy[1]]-self.X[cy[0]],self.X[cy[2]]-self.X[cy[0]]))<0:cy.reverse()
   cy=[inv[i]for i in cy];k=cy.index(min(cy));cy=cy[k:]+cy[:k];faces.append(cy);H.append(h)
  ef={}
  for f,cy in enumerate(faces):
   for i,j in zip(cy,cy[1:]+cy[:1]):ef.setdefault(tuple(sorted((i,j))),[]).append((f,i,j))
  assert len(keep)-len(ef)+len(faces)==2
  assert all(len(p)==2 and p[0][1:]==p[1][1:][::-1] for p in ef.values())
  return keep,faces,H,ef
 def screen(self,deleted,detail=False):
  keep,faces,H,ef=self.hull(set(deleted));P=self.X[keep];tri=np.array([(cy[0],cy[j],cy[j+1])for cy in faces for j in range(1,len(cy)-1)])
  a,b,c=(P[tri[:,k]]for k in range(3));vols=np.einsum('ij,ij->i',a,np.cross(b,c))/6;assert vols.min()>0
  V=vols.sum();M=np.einsum('i,ij->j',vols,(a+b+c)/4);cent=M/V;x=P-cent
  q=np.array([[float(F(v,h[3]))for v in h[:3]]for h in H]);n=q/(1-q@cent)[:,None]
  ss=[]
  for fi,cy in enumerate(faces):
   ix=np.array(cy);jx=np.roll(ix,-1);ss.append(np.einsum('ij,j->i',np.cross(x[ix],x[jx]-x[ix]),n[fi]).min())
  uu=x@x.T-(x*x).sum(1)[:,None];np.fill_diagonal(uu,-np.inf);ums=uu.max(1)
  E=np.array(sorted(ef));pol=np.array([[z[0]for z in ef[tuple(e)]]for e in E]);aa=x[E[:,0]];dd=x[E[:,1]]-aa;ll=np.einsum('ij,ij->i',dd,dd);t=-np.einsum('ij,ij->i',aa,dd)/ll;z=aa+t[:,None]*dd
  ni=n[pol[:,0]];nj=n[pol[:,1]];an=np.einsum('ij,ij->i',ni,ni);bn=np.einsum('ij,ij->i',ni,nj);cn=np.einsum('ij,ij->i',nj,nj);r=np.einsum('ij,ij->i',z,ni);s=np.einsum('ij,ij->i',z,nj);D=an*cn-bn*bn
  assert D.min()>0
  ev=np.array([t,1-t,(r*cn-s*bn)/D,(s*an-r*bn)/D]).T
  sf=np.where(np.array(ss)>0)[0];uv=np.where(ums<0)[0];eh=np.where(ev.min(1)>0)[0]
  out=dict(deleted=sorted(map(int,deleted)),VEF=[len(keep),len(ef),len(faces)],C=2*len(ef),counts=[len(sf),len(uv),len(eh)],U=[keep[i]for i in uv],S=[sorted(keep[i]for i in faces[f])for f in sf],H=[[keep[i]for i in E[j]]for j in eh],centroid=cent.tolist(),volume=float(V),min_abs_U=float(np.abs(ums).min()),min_abs_S=float(np.abs(ss).min()),min_abs_edge=float(np.abs(ev).min()))
  if detail:out.update(keep=keep,faces=faces,Hrows=H,ef=ef,X=P,x=x,q=q,n=n,tri=tri,uu=uu,ss=ss,ev=ev)
  return out
if __name__=='__main__':
 model=Model(json.loads(Path(sys.argv[1]).read_text()));outdir=Path(sys.argv[2]);outdir.mkdir(parents=True,exist_ok=True);rows=[]
 for k in range(len(model.X)):
  try:r=model.screen([k]);rows.append(r)
  except Exception as e:rows.append(dict(deleted=[k],error=str(e)));continue
  if r['counts']==[1,1,0] or r['C']<624:print(r,flush=True)
 (outdir/'singles.json').write_text(canon(rows));print('SINGLE_SCREEN_DONE',len(rows),flush=True)
