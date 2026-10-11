from fractions import Fraction as Q
from pathlib import Path
import json,sys,hashlib,math
import audit_B as H
sys.set_int_max_str_digits(0)
plus=H.plus;minus=H.minus;mul=H.mul;inner=H.inner;outer=H.outer;determinant=H.determinant
ZERO=(0,0,0)
def encode(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,(tuple,list)):return [encode(v) for v in x]
 if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
 return x

def run(raw):
 I=[tuple(v) for v in raw['I']];D=raw['D'];sc=raw.get('scale',256);kh=H.audit(I,D)
 assert kh['active_input_indices']==list(range(len(I)))
 # Independent exact Cramer reconstruction from each maximal K-facet's contacts.
 X=[]
 for cy in kh['maximal_faces']:
  ia,ib,ic=cy[:3];a,b,c=I[ia],I[ib],I[ic];dd=determinant(a,b,c);assert dd!=0
  pt=mul(plus(plus(outer(b,c),outer(c,a)),outer(a,b)),Q(D,dd));X.append(pt)
  assert all(inner(I[i],pt)==D if i in cy else inner(I[i],pt)<D for i in range(len(I)))
 faces=[]
 for n in I:
  ids=[j for j,p in enumerate(X) if inner(n,p)==D];succ={}
  from itertools import combinations
  for a,b in combinations(ids,2):
   e=minus(X[b],X[a]);l=inner(e,e);vv={i:inner(n,outer(e,minus(X[i],X[a]))) for i in ids};zeros=[i for i in ids if vv[i]==0];pro=[inner(e,minus(X[i],X[a])) for i in zeros]
   if min(pro)<0 or max(pro)>l:continue
   if min(vv.values())>=0:succ[a]=b
   elif max(vv.values())<=0:succ[b]=a
  assert len(succ)>=3 and set(succ)==set(succ.values());a=min(succ);cy=[a];b=succ[a]
  while b!=a:assert b not in cy;cy.append(b);b=succ[b]
  assert len(cy)==len(succ);faces.append(cy)
 edges={};tri=[]
 for f,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append((f,i,j))
  tri +=[(cy[-1],cy[j],cy[j+1]) for j in range(len(cy)-2)]
 adj={j:set() for j in range(len(X))}
 for (i,j),rr in edges.items():assert len(rr)==2 and rr[0][1:]==rr[1][1:][::-1];adj[i].add(j);adj[j].add(i)
 assert len(X)-len(edges)+len(faces)==2;seen=set();todo=[0]
 while todo:
  j=todo.pop()
  if j not in seen:seen.add(j);todo.extend(adj[j]-seen)
 assert len(seen)==len(X)
 # Different interior reference and last-vertex fans.
 rho=Q(D,100*(1+max(sum(map(abs,n)) for n in I)));B=(rho,2*rho,3*rho);assert all(inner(n,B)<D for n in I);Z=[minus(p,B) for p in X];vol=Q(0);mom=ZERO
 for i,j,k in tri:
  v=determinant(Z[i],Z[j],Z[k])/6;assert v>0;vol+=v;mom=plus(mom,mul(plus(plus(Z[i],Z[j]),Z[k]),v/4))
 centre=plus(B,mul(mom,1/vol));first=mul(centre,vol);Y=[mul(minus(p,centre),sc) for p in X];hs=[sc*(D-inner(n,centre)) for n in I];assert min(hs)>0
 vv=vol*sc**3;mm=mul(minus(first,mul(centre,vol)),sc**4);assert mm==ZERO
 Dc=math.lcm(*(v.denominator for v in centre));Mc=tuple(int(v*Dc) for v in centre);bs=[math.lcm(*(v.denominator for v in p)) for p in X];aa=[tuple(int(v*b) for v in p) for p,b in zip(X,bs)];zi=[minus(mul(p,Dc),mul(Mc,b)) for p,b in zip(aa,bs)]
 def edge(i,j):return minus(mul(aa[j],bs[i]),mul(aa[i],bs[j]))
 st=[];sw=[];un=[];uw=[];sa=[];hw=[];fl=[];ul=[];el=[]
 for fi,cy in enumerate(faces):
  n=I[fi];hc=D*Dc-inner(n,Mc);nn=inner(n,n);vals=[]
  for i,j in zip(cy,cy[1:]+cy[:1]):
   proj=minus(mul(n,bs[i]*hc),mul(zi[i],nn));vals.append(inner(n,outer(edge(i,j),proj)))
  if min(vals)>0:st.append(fi)
  elif min(vals)>=0:sw.append(fi)
  fl.append([int(v>0)-int(v<0) for v in vals])
 for i,p in enumerate(Y):
  v=max(inner(zi[i],edge(i,j)) for j in adj[i])
  if v<0:un.append(i)
  elif v==0:uw.append(i)
  jj=[j for j in range(len(Y)) if j!=i];j=jj[0];num=inner(zi[i],edge(i,j))
  for k in jj[1:]:
   nu=inner(zi[i],edge(i,k));cmp=nu*bs[j]-num*bs[k]
   if cmp>0 or (cmp==0 and k>j):num=nu;j=k
  ul.append([j,Q(sc**2*num,bs[i]**2*bs[j]*Dc)])
 for (i,j),rr in sorted(edges.items()):
  e=edge(i,j);ee=inner(e,e);pa=inner(zi[i],e);t=Q(-pa*bs[j],Dc*ee);p=minus(mul(zi[i],ee),mul(e,pa));pd=bs[i]*Dc*ee
  n=I[rr[0][0]];nn=I[rr[1][0]];cc=outer(n,nn);den=inner(cc,cc);assert den>0
  alpha=Q(sc*inner(outer(p,nn),cc),pd*den);beta=Q(sc*inner(outer(n,p),cc),pd*den);vals=[t,1-t,alpha,beta]
  if min(vals)>0:sa.append([i,j])
  elif min(vals)>=0:hw.append([i,j])
  el.append([[i,j],[rr[0][0],rr[1][0]],vals])
 return encode(dict(V=len(X),E=len(edges),F=len(faces),counts=[len(st),len(un),len(sa)],weak=[len(sw),len(uw),len(hw)],stable_face_ids=st,stable_faces=[faces[i] for i in st],unstable_vertices=un,saddle_edges=sa,weak_faces=sw,weak_vertices=uw,weak_edges=hw,faces=faces,edges=sorted(edges),vertices=Y,normals=I,supports=hs,raw_vertices=X,raw_volume=vol,raw_first_moments=first,raw_centroid=centre,volume=vv,first_moments=mm,centroid=ZERO,face_signs=fl,vertex_max_escape=ul,edge_cone=el,triangles=tri,K_faces=kh['maximal_faces'],K_supports=kh['primitive_support_planes']))
if __name__=='__main__':
 o=run(json.loads(Path(sys.argv[1]).read_text()));bb=json.dumps(o,sort_keys=True,separators=(',',':')).encode();Path(sys.argv[2]).write_bytes(bb);print('DUAL_B',o['V'],o['E'],o['F'],o['counts'],o['weak'],len(bb),hashlib.sha256(bb).hexdigest(),flush=True)
 if len(sys.argv)>3:
  A=json.loads(Path(sys.argv[3]).read_text())
  for k in o:
   if k!='triangles':assert o[k]==A[k],k
  print('DUAL_ALL_COMMON_FIELDS_EQUAL',flush=True)
