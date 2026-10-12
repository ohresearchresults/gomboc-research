"""Exact physical realization of a saved Green-function section construction.
Saved binary64 parameters are interpreted as exact dyadic rationals, preserving
all planar side quadrilaterals. Complete hull/mass/equilibrium audit follows.
"""
import argparse,json,time,hashlib
from pathlib import Path
from math import lcm,gcd
import numpy as np
from gmpy2 import mpq
from exact_audit_vertices import check_B,cross,sub,dot
from triangular_sections import Family
from rectangular_sections import topology

def inv3(M):
 a,b,c=map(tuple,M);D=dot(a,cross(b,c));assert D!=0;cols=[cross(b,c),cross(c,a),cross(a,b)];return [[cols[j][i]/D for j in range(3)] for i in range(3)]
def audit(source,out):
 out=Path(out);out.mkdir(parents=True,exist_ok=False);start=time.time();data=np.load(source);Q=lambda v:mpq(float(v));z=list(map(Q,data['z']));L=len(z);isrect='kind' in data and str(data['kind'])=='independent_rectangle_curvatures';ispolygon='kind' in data and str(data['kind'])=='independent_polygon_curvatures';m=len(data['normals']) if ispolygon else 4 if isrect else 3;A=[list(map(Q,row)) for row in data['A']];tilt=list(map(Q,data['tilt']));assert A[0][0]*A[1][1]-A[0][1]*A[1][0]>0;assert -1<z[0] and z[-1]<1 and all(u<v for u,v in zip(z,z[1:]))
 if ispolygon:
  normals=[list(map(Q,row)) for row in data['normals']];h=[mpq(1)]*m;base=[]
 else:
  base=[list(map(Q,row)) for row in (np.array([[1.,-1.],[1.,1.],[-1.,1.],[-1.,-1.]]) if isrect else data['base'])];normals=[(base[(i+1)%m][1]-base[i][1],base[i][0]-base[(i+1)%m][0]) for i in range(m)];h=[sum(u*v for u,v in zip(n,b)) for n,b in zip(normals,base)];assert all(v>0 for v in h)
 M=[[hi,*ni] for hi,ni in zip(h,normals)]
 if not isrect and not ispolygon:MI=inv3(M)
 if 'W' in data:W=[list(map(Q,row)) for row in data['W']]
 else:
  k=list(map(Q,data['k']));a=[list(map(Q,row)) for row in data['a']];W=[[ki*(hi-sum(v*u for v,u in zip(n,ai))) for n,hi in zip(normals,h)] for ki,ai in zip(k,a)]
 assert all(v>0 for row in W for v in row),'nonpositive exact side curvature'
 r=[];mu=[];rectpoints=[]
 for zi in z:
  G=[(min(zi,zj)+1)*(1-max(zi,zj))/2 for zj in z];b=[sum(g*w[j] for g,w in zip(G,W)) for j in range(m)]
  if ispolygon:
   for j in range(m):
    u=normals[(j-1)%m];v=normals[j];a=b[(j-1)%m];bb=b[j];det=u[0]*v[1]-u[1]*v[0];assert det>0;xy=[(a*v[1]-u[1]*bb)/det,(u[0]*bb-a*v[0])/det];assert all(sum(n[k]*xy[k] for k in range(2))<=hh for n,hh in zip(normals,b));rectpoints.append(([xy[k]+(zi+1)*tilt[k]/2 for k in range(2)],zi))
  elif isrect:
   for ix,iy,sx,sy in [(0,3,1,-1),(0,1,1,1),(2,1,-1,1),(2,3,-1,-1)]:rectpoints.append(([sx*b[ix]+(zi+1)*tilt[0]/2,sy*b[iy]+(zi+1)*tilt[1]/2],zi))
  else:
   sec=[sum(v*u for v,u in zip(row,b)) for row in MI];r.append(sec[0]);mu.append([sec[j+1]+(zi+1)*tilt[j]/2 for j in range(2)])
 if not isrect and not ispolygon:assert all(v>0 for v in r)
 X=[(mpq(0),mpq(0),mpq(-1))]
 if isrect or ispolygon:
  for xy,zi in rectpoints:X.append(tuple(sum(v*u for v,u in zip(row,xy)) for row in A)+(zi,))
 else:
  for zi,ri,mi in zip(z,r,mu):
   for b in base:
    xy=[mi[j]+ri*b[j] for j in range(2)];X.append(tuple(sum(v*u for v,u in zip(row,xy)) for row in A)+(zi,))
 X.append(tuple(sum(v*u for v,u in zip(row,tilt)) for row in A)+(mpq(1),));mean=tuple(sum(p[j] for p in X)/len(X) for j in range(3));X=[tuple(v-mean[j] for j,v in enumerate(p)) for p in X];B=lambda x:json.dumps(x,default=str,sort_keys=True,separators=(',',':')).encode()
 meta=dict(source=str(source),source_sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest(),kind='independent_polygon_curvatures' if ispolygon else 'independent_rectangle_curvatures' if isrect else 'triangular_curvatures',interpretation='each saved floating parameter is its exact dyadic rational; reconstruct Green functions and exact section-plane solution',z=z,W=W,base=base,normals=normals,A=A,tilt=tilt,translation_mean=mean,density=1);(out/'construction.json').write_bytes(B(meta));(out/'coordinates.json').write_bytes(B(dict(points=X)))
 faces=topology(m,L)[0];rows=[]
 for f in faces:
  n=cross(sub(X[f[1]],X[f[0]]),sub(X[f[2]],X[f[0]]));hh=dot(n,X[f[0]]);assert hh>0;ss=[dot(n,p)-hh for p in X];assert all(v<=0 for v in ss);assert {i for i,v in enumerate(ss) if v==0}==set(f)
  den=lcm(*(int(v.denominator) for v in (*n,hh)));row=[int(v*den) for v in (*n,hh)];gg=gcd(*row);rows.append([v//gg for v in row])
 assert len({tuple(row) for row in rows})==len(rows);raw={'H':rows};(out/'raw.json').write_bytes(B(raw));(out/'construction_faces.json').write_bytes(B(faces));print('EXACT_SECTION_HULL_INPUT',L,len(X),len(rows),time.time()-start,flush=True)
 rep=check_B.run(raw);assert {tuple(mpq(v) for v in row) for row in rep['raw_vertices']}==set(X);assert [rep[k] for k in ['V','E','F']]==[m*L+2,m*(2*L+1),m*(L+1)];(out/'audit.json').write_bytes(B(rep));su={k:rep[k] for k in ['V','E','F','counts','weak','stable_face_ids','unstable_vertices','saddle_edges','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};su.update(C=2*rep['E'],seconds=time.time()-start,goal_met=rep['counts']==[1,1,0] and rep['weak']==[0,0,0] and 34<=2*rep['E']<500);su['files']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir()};(out/'summary.json').write_text(json.dumps(su,indent=2));print('EXACT_SECTION_CENSUS',out,{k:su[k] for k in ['V','E','F','C','counts','weak','goal_met','seconds']},flush=True)
 if su['goal_met']:(out/'GOAL_CANDIDATE_COMPLETE.json').write_text(json.dumps(su,indent=2))
 return rep
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');a=p.parse_args();audit(a.source,a.out)
