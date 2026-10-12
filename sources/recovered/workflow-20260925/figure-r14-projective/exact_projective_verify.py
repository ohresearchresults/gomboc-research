#!/usr/bin/env python3
"""Exact Fraction verifier for rational projective/affine images of the source.
Python 3.11+ standard library only. Every barycentre is uniform-volume.
Input transform: raw coordinates x -> A*(x/(1+c dot x)); default identity.
All rational values are integer or 'numerator/denominator' strings.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse, hashlib, json, sys
if hasattr(sys,'set_int_max_str_digits'): sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
ZERO=Q(0)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),ZERO)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(k,a):return tuple(k*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def solve(rows,b):
 a,c,d=rows;D=det(a,c,d)
 if not D:raise ValueError('singular exact matrix')
 return mul(1/D,add(add(mul(b[0],cross(c,d)),mul(b[1],cross(d,a))),mul(b[2],cross(a,c))))
def matvec(A,x):return tuple(dot(row,x) for row in A)
def trans(A):return tuple(zip(*A))
def s(x):return str(x)
def vstr(v):return [s(x) for x in v]
def mass(X,faces,N):
 W=Q(0);mom=(Q(0),)*3;triangles=[]
 for fi,f in enumerate(faces):
  for k in range(1,len(f)-1):
   ids=[f[0],f[k],f[k+1]]
   if dot(cross(sub(X[ids[1]],X[ids[0]]),sub(X[ids[2]],X[ids[0]])),N[fi])<0:ids[1],ids[2]=ids[2],ids[1]
   a,b,c=(X[i] for i in ids);w=det(a,b,c)
   W+=w;mom=add(mom,mul(w,add(add(a,b),c)));triangles.append(ids)
 if W<=0:raise ValueError('nonpositive exact signed volume')
 return W/6,mul(1/(4*W),mom)
def verify(data, transform):
 N=[tuple(map(Q,n)) for n in data['normals']];H=[dot(n,n) for n in N]
 faces=[[i-1 for i in f] for f in data['faces']]
 triples=[[i-1 for i in t] for t in data['vertex_triples']]
 X=[solve([N[i] for i in t],[H[i] for i in t]) for t in triples]
 if transform.get('center_source',False):
  _,origin=mass(X,faces,N)
  X=[sub(x,origin) for x in X];H=[h-dot(n,origin) for n,h in zip(N,H)]
 c=tuple(map(Q,transform.get('c',[0,0,0])))
 A=[tuple(map(Q,r)) for r in transform.get('A',[[1,0,0],[0,1,0],[0,0,1]])]
 if det(*A)<=0:raise ValueError('orientation-preserving invertible A required')
 ell=[1+dot(c,x) for x in X]
 if min(ell)<=0:raise ValueError('projective pole intersects polytope')
 Y=[matvec(A,mul(1/l,x)) for x,l in zip(X,ell)]
 M=[solve(trans(A),add(n,mul(h,c))) for n,h in zip(N,H)]
 # Check the full supporting-plane incidence, not only triple intersections.
 for fi,(n,h,f) in enumerate(zip(M,H,faces)):
  for vi,y in enumerate(Y):
   val=dot(n,y)-h
   if vi in f:assert val==0,(fi,vi,'missing incidence')
   else:assert val<0,(fi,vi,'unexpected incidence or nonconvexity')
  for k in range(len(f)):
   e1=sub(Y[f[(k+1)%len(f)]],Y[f[k]])
   e2=sub(Y[f[(k+2)%len(f)]],Y[f[(k+1)%len(f)]])
   assert dot(cross(e1,e2),n)!=0,'flat polygon corner'
 edges={};neighbors=[set() for _ in Y]
 for fi,f in enumerate(faces):
  for a,b in zip(f,f[1:]+f[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(fi)
 assert len(Y)-len(edges)+len(faces)==2
 for (a,b),ff in edges.items():
  assert len(ff)==2
  neighbors[a].add(b);neighbors[b].add(a)
 V,g=mass(Y,faces,M);Z=[sub(y,g) for y in Y];h=[hh-dot(n,g) for n,hh in zip(M,H)]
 assert min(h)>0,'centroid not strictly interior'
 S=[];U=[];Hs=[];weak=[];face_witnesses=[];vertex_witnesses=[];edge_witnesses=[]
 for i,(n,hi) in enumerate(zip(M,h)):
  foot=mul(hi/dot(n,n),n)
  gates=[(j,dot(nj,foot)-hj) for j,(nj,hj) in enumerate(zip(M,h)) if j!=i]
  if max(z for j,z in gates)<=0:
   if max(z for j,z in gates)<0:S.append(i+1)
   else:weak.append({'feature':'face','id':i+1})
  else:
   j,z=max(gates,key=lambda a:a[1]);face_witnesses.append([i+1,j+1,s(z)])
 for i,z in enumerate(Z):
  gates=[(j,dot(z,sub(Z[j],z))) for j in sorted(neighbors[i])]
  if max(a for j,a in gates)<=0:
   if max(a for j,a in gates)<0:U.append(i+1)
   else:weak.append({'feature':'vertex','id':i+1})
  else:
   j,a=max(gates,key=lambda a:a[1]);vertex_witnesses.append([i+1,j+1,s(a)])
 for (ia,ib),(fi,fj) in sorted(edges.items()):
  a=Z[ia];d=sub(Z[ib],a);t=-dot(a,d)/dot(d,d);r=add(a,mul(t,d))
  n,m=M[fi],M[fj];nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);D=nn*mm-nm*nm
  assert D>0
  lam=(dot(r,n)*mm-dot(r,m)*nm)/D
  mu=(dot(r,m)*nn-dot(r,n)*nm)/D
  assert r==add(mul(lam,n),mul(mu,m))
  gates=[t,1-t,lam,mu]
  if min(gates)>=0:
   rec={'edge':[ia+1,ib+1],'faces':[fi+1,fj+1],'t':s(t),'lambda':s(lam),'mu':s(mu)}
   if min(gates)>0:Hs.append(rec)
   else:rec['feature']='edge';weak.append(rec)
  else:
   k=min(range(4),key=lambda k:gates[k]);edge_witnesses.append([ia+1,ib+1,k,s(gates[k])])
 if not weak:assert len(S)+len(U)-len(Hs)==2,'Euler equilibrium check'
 return dict(identity=data['identity'],transform=transform,counts={'V':len(Y),'E':len(edges),'F':len(faces),'C':2*len(edges)},
             volume=s(V),uniform_centroid=vstr(g),min_projective_denominator=s(min(ell)),
             S=S,U=U,H=Hs,weak_features=weak,
             non_equilibrium_witnesses={'faces':face_witnesses,'vertices':vertex_witnesses,'edges':edge_witnesses},
             evidence='Exact rational arithmetic; all supporting incidences and all closed feature equilibrium gates checked.',
             acceptance_class110=(len(S)==1 and len(U)==1 and len(Hs)==0 and not weak))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input',default=str(HERE/'reshetov14_input.json'))
 ap.add_argument('--transform');ap.add_argument('--out',default=str(HERE/'exact_result.json'))
 a=ap.parse_args();raw=Path(a.input).read_bytes();data=json.loads(raw)
 tf=json.loads(Path(a.transform).read_text()) if a.transform else {}
 r=verify(data,tf);r['input_sha256']=hashlib.sha256(raw).hexdigest()
 Path(a.out).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
 print('EXACT_GATE_CHECK_PASS')
 print(json.dumps({k:r[k] for k in ['counts','S','U','weak_features','acceptance_class110']}))
 print('H_EDGES',[(e['edge'],e['faces']) for e in r['H']])
if __name__=='__main__':main()
