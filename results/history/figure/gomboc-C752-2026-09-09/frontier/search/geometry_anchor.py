"""Floating discovery only; exact acceptance requires the separate rational auditors."""
import numpy as np
from scipy.spatial import ConvexHull
from collections import defaultdict

def geom(q, derivatives=False, anchor=None):
 q=np.asarray(q,dtype=float); n=len(q); hull=ConvexHull(q)
 if np.max(hull.equations[:,3]) >= -1e-10: raise ValueError('origin not strictly interior')
 roots=np.flatnonzero(q[:,2]==1.0); rs=set(roots.tolist()); tr=hull.simplices
 groups={}; owner=[]; source=[]
 for t in tr:
  key=('root',) if set(t).issubset(rs) else (('fixed',) if anchor is not None and set(t).issubset(set(anchor['rows'])) else tuple(sorted(t.tolist())))
  if key not in groups:groups[key]=len(source);source.append(key)
  owner.append(groups[key])
 V=len(source); X=np.zeros((V,3)); J=np.zeros((V,3,3*n)) if derivatives else None
 for k,key in enumerate(source):
  if key==('root',):X[k]=[0,0,1];continue
  if key==('fixed',):X[k]=anchor['point'];continue
  ids=np.array(key); inv=np.linalg.inv(q[ids]);X[k]=inv@np.ones(3)
  if derivatives:
   for s,i in enumerate(ids):J[k,:,3*i:3*i+3]=-np.outer(inv[:,s],X[k])
 eq=X@q.T-1
 if eq.max()>1e-7:raise ValueError(('support',eq.max()))
 te=defaultdict(list)
 for f,t in enumerate(tr):
  for a,b in zip(t,np.roll(t,-1)):te[tuple(sorted((int(a),int(b))))].append(owner[f])
 edges={}
 for (a,b),vs in te.items():
  assert len(vs)==2
  if vs[0]!=vs[1]:edges[tuple(sorted(vs))]=(a,b)
 faces={};T=[]
 for i in hull.vertices:
  adj=defaultdict(list)
  for (a,b),(j,k) in edges.items():
   if i==j or i==k:adj[a].append(b);adj[b].append(a)
  if not adj:raise ValueError('empty face')
  if not all(len(a)==2 for a in adj.values()):raise ValueError('broken face graph')
  a=min(adj);cy=[a];prev=-1
  while True:
   nxt=[v for v in adj[cy[-1]] if v!=prev][0]
   if nxt==a:break
   prev=cy[-1];cy.append(nxt)
   if len(cy)>len(adj):raise ValueError('cycle')
  if len(cy)!=len(adj):raise ValueError('disconnected facet')
  ar=np.sum(np.cross(X[cy],X[np.roll(cy,-1)]),axis=0)
  if ar@q[i]<0:cy=cy[::-1]
  faces[int(i)]=cy
  T += [(cy[0],cy[j],cy[j+1]) for j in range(1,len(cy)-1)]
 assert V-len(edges)+len(faces)==2
 T=np.array(T);a,b,c=X[T].transpose(1,0,2);cr=np.cross(b,c);d=np.einsum('ij,ij->i',a,cr);W=d.sum()
 if W<=0:raise ValueError('volume')
 sums=a+b+c; M=np.einsum('i,ij->j',d,sums);g=M/(4*W)
 if derivatives:
  da,db,dc=J[T].transpose(1,0,2,3)
  dw=np.einsum('ij,ijk->ik',cr,da)+np.einsum('ij,ijk->ik',np.cross(c,a),db)+np.einsum('ij,ijk->ik',np.cross(a,b),dc)
  dg=(np.einsum('ij,ik->jk',sums-4*g,dw)+np.einsum('i,ijk->jk',d,da+db+dc))/(4*W)
  JY=J-dg
 h=1-q@g
 if min(h)<=0:raise ValueError('centroid outside')
 Z=q/h[:,None];Y=X-g
 if derivatives:
  JZ=np.einsum('ij,k->ijk',np.eye(n).repeat(3,axis=1),np.zeros(1)) if False else np.zeros((n,3,3*n))
  for i in range(n):
   dh=-(q[i]@dg);dh[3*i:3*i+3]-=g
   JZ[i]=-np.outer(q[i]/h[i]**2,dh)
   JZ[i,:,3*i:3*i+3]+=np.eye(3)/h[i]
 def escapes(v):
  nn=np.sum(v*v,axis=1);A=(v@v.T)/nn[:,None]-1;np.fill_diagonal(A,-np.inf);return A,np.argmax(A,axis=1),A.max(axis=1)
 aU,pU,vU=escapes(Y);aS,pS,vS=escapes(Z)
 active=np.array(sorted(faces));S=active[vS[active]<-1e-11];U=np.flatnonzero(vU<-1e-11)
 H=[];r2s={};emin={};edgevals=[]
 for (i,j),(f,k) in edges.items():
  e=Y[j]-Y[i];ee=e@e;t=-Y[i]@e/ee;p=Y[i]+t*e;w=np.cross(q[f],q[k]);ww=w@w
  al=np.cross(p,q[k])@w/ww;be=np.cross(q[f],p)@w/ww
  if min(t,1-t,al,be)>1e-10:H.append((i,j))
  v=Y[i]+np.clip(t,0,1)*e;emin[i,j]=v@v;r2s[i,j]=p@p;edgevals.append([i,j,t,1-t,al,be])
 # Entire maximal-facet/ball sublevel graph. Zero bars are grouped by a numerical
 # tolerance for search only, never for an exact acceptance decision.
 birth={i: h[i]**2/(q[i]@q[i]) if i in S else min(emin[tuple(sorted(e))] for e in zip(cy,np.roll(cy,-1))) for i,cy in faces.items()}
 events=[(v,0,i) for i,v in birth.items()]+[(v,1,e) for e,v in emin.items()]
 par={i:i for i in faces};bars=[]
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 for v,kind,key in sorted(events):
  if kind==0:continue
  f,k=edges[key];u,w=root(f),root(k)
  if u==w:continue
  live,dead=sorted((u,w),key=lambda i:(birth[i],i));B=1-birth[dead]/v
  if B>1e-9:bars.append(dict(stable=dead,edge=key,B=B))
  par[dead]=live
 out=dict(q=q,X=X,Y=Y,Z=Z,g=g,V=V,E=len(edges),F=len(faces),volume=W/6,faces=faces,edges=edges,T=T,source=source,active=active,rootrows=roots,S=S,U=U,H=H,bars=bars,vertex_escape=vU,pole_escape=vS,pU=pU,pS=pS,h=h,edgevals=np.array(edgevals),A_U=aU,A_S=aS)
 if derivatives:out.update(JX=J,JY=JY,JZ=JZ,Jg=dg)
 return out

def escape_grad(v,J,parent,ids):
 ids=np.asarray(ids);j=parent[ids];a=v[ids];b=v[j];nn=np.sum(a*a,axis=1);ab=np.sum(a*b,axis=1)
 return np.einsum('ij,ijk->ik',b/nn[:,None]-2*a*(ab/nn**2)[:,None],J[ids])+np.einsum('ij,ijk->ik',a/nn[:,None],J[j])

def bar_grad(G,bar):
 i=bar['stable'];a,b=bar['edge'];q=G['q'];s=G['Z'][i];Js=G['JZ'][i];Y=G['Y'];J=G['JY'];e=Y[b]-Y[a];t=-Y[a]@e/(e@e);z=Y[a]+t*e
 rS=1/(s@s);rH=z@z
 ds=-2*s@Js/(s@s)**2;dh=2*z@((1-t)*J[a]+t*J[b])
 return -ds/rH+rS*dh/rH**2

def brief(G):
 return dict(VEF=[G[k] for k in ('V','E','F')],counts=[len(G[k]) for k in ('S','U','H')],S=G['S'].tolist(),U=[G['source'][i] for i in G['U']],H=[[G['source'][i],G['source'][j],G['edges'][tuple(sorted((i,j)))]] for i,j in G['H']],bars=G['bars'],g=G['g'].tolist(),volume=G['volume'])
