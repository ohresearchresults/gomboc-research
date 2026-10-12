from fractions import Fraction as F
from pathlib import Path
import json,sys,math,hashlib
import audit_A as H
sys.set_int_max_str_digits(0)
a=H.add;s=H.sub;m=H.scale;d=H.dot;c=H.cross;det=H.det
Z=(0,0,0)
def strings(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(tuple,list)):return [strings(v) for v in x]
 if isinstance(x,dict):return {str(k):strings(v) for k,v in x.items()}
 return x

def run(raw):
 I=[tuple(p) for p in raw['I']];D=raw['D'];scale=raw.get('scale',256)
 hh=H.exact_audit(I,D);assert hh['active_input_indices']==list(range(len(I)))
 X=[]
 for *N,b in hh['primitive_support_planes']:
  assert b>0;X.append(tuple(F(D*t,b) for t in N))
 faces=[]
 for i,N in enumerate(I):
  ids=[j for j,cy in enumerate(hh['maximal_faces']) if i in cy];faces.append(H.exact_polygon(X,ids,N))
 edges={};tris=[]
 for f,cy in enumerate(faces):
  for x,y in zip(cy,cy[1:]+cy[:1]):edges.setdefault(tuple(sorted((x,y))),[]).append((f,x,y))
  tris +=[(cy[0],cy[j],cy[j+1]) for j in range(1,len(cy)-1)]
 assert len(X)-len(edges)+len(faces)==2
 assert all(len(es)==2 and es[0][1:]==es[1][1:][::-1] for es in edges.values())
 for f,N in enumerate(I):
  cy=set(faces[f])
  assert all(d(N,x)==D if j in cy else d(N,x)<D for j,x in enumerate(X))
 vol=F(0);mom=Z
 for i,j,k in tris:
  v=det(X[i],X[j],X[k])/6;assert v>0;vol+=v;mom=a(mom,m(v/4,a(a(X[i],X[j]),X[k])))
 centre=m(1/vol,mom);Y=[m(scale,s(x,centre)) for x in X];hs=[scale*(D-d(n,centre)) for n in I]
 assert all(h>0 for h in hs)
 v2=scale**3*vol;m2=m(scale**4,s(mom,m(vol,centre)));assert m2==Z
 # Clear the common centroid denominator once; edge differences remain short.
 Dc=math.lcm(*(v.denominator for v in centre));Mc=tuple(int(v*Dc) for v in centre)
 bs=[math.lcm(*(z.denominator for z in p)) for p in X];aa=[tuple(int(z*bi) for z in p) for p,bi in zip(X,bs)];yi=[s(m(Dc,p),m(bi,Mc)) for p,bi in zip(aa,bs)]
 def edge(i,j):return s(m(bs[i],aa[j]),m(bs[j],aa[i]))
 S=[];SW=[];U=[];UW=[];SH=[];HW=[];fl=[];ul=[];el=[]
 for f,cy in enumerate(faces):
  N=I[f];vals=[d(N,c(yi[i],edge(i,j))) for i,j in zip(cy,cy[1:]+cy[:1])]
  if min(vals)>0:S.append(f)
  elif min(vals)>=0:SW.append(f)
  fl.append([int(v>0)-int(v<0) for v in vals])
 for i in range(len(Y)):
  jj=[j for j in range(len(Y)) if j!=i];j=jj[0];num=d(yi[i],edge(i,j))
  for k in jj[1:]:
   q=d(yi[i],edge(i,k));cmp=q*bs[j]-num*bs[k]
   if cmp>0 or (cmp==0 and k>j):num=q;j=k
  v=F(scale**2*num,bs[i]**2*bs[j]*Dc)
  if v<0:U.append(i)
  elif v==0:UW.append(i)
  ul.append([j,v])
 for (i,j),es in sorted(edges.items()):
  e=edge(i,j);ee=d(e,e);q=d(yi[i],e);t=F(-q*bs[j],Dc*ee);pn=s(m(ee,yi[i]),m(q,e));pd=bs[i]*Dc*ee
  N=I[es[0][0]];M=I[es[1][0]];nn=d(N,N);mm=d(M,M);nm=d(N,M);dd=nn*mm-nm*nm;assert dd>0
  alpha=F(scale*d(pn,s(m(mm,N),m(nm,M))),pd*dd);beta=F(scale*d(pn,s(m(nn,M),m(nm,N))),pd*dd)
  vals=[t,1-t,alpha,beta]
  if min(vals)>0:SH.append([i,j])
  elif min(vals)>=0:HW.append([i,j])
  el.append([[i,j],[es[0][0],es[1][0]],vals])
 active=set(range(len(Y)));adj={i:set() for i in active}
 for i,j in edges:adj[i].add(j);adj[j].add(i)
 todo=[0];seen=set()
 while todo:
  i=todo.pop()
  if i not in seen:seen.add(i);todo.extend(adj[i]-seen)
 assert seen==active
 return strings(dict(V=len(X),E=len(edges),F=len(faces),counts=[len(S),len(U),len(SH)],weak=[len(SW),len(UW),len(HW)],stable_face_ids=S,stable_faces=[faces[i] for i in S],unstable_vertices=U,saddle_edges=SH,weak_faces=SW,weak_vertices=UW,weak_edges=HW,faces=faces,edges=sorted(edges),vertices=Y,normals=I,supports=hs,raw_vertices=X,raw_volume=vol,raw_first_moments=mom,raw_centroid=centre,volume=v2,first_moments=m2,centroid=Z,face_signs=fl,vertex_max_escape=ul,edge_cone=el,triangles=tris,K_faces=hh['maximal_faces'],K_supports=hh['primitive_support_planes']))
if __name__=='__main__':
 R=Path(__file__).parent;o=run(json.loads(Path(sys.argv[1]).read_text()));bb=json.dumps(o,sort_keys=True,separators=(',',':')).encode();Path(sys.argv[2]).write_bytes(bb);print('DUAL_A',o['V'],o['E'],o['F'],o['counts'],o['weak'],len(bb),hashlib.sha256(bb).hexdigest(),flush=True)
