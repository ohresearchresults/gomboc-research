# material-9a9df583f7de

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# C330_ROOTFREE_G5: complete audit sources, recovery capsule part 2/2

Use with C330_ROOTFREE_G5_LITERAL_GEOMETRY.md, material [internal-source-reference]. All code below is literal and complete. No old sandbox, archive, numerical optimizer or external package is required. CPython3.13.5 standard library; assertions enabled. Extract each FILE block to the indicated relative filename, retaining its terminal newline. Extract the JSON line from part1 without a terminal newline to C330_ROOTFREE_G5_INPUT.json. Execute `python -B -S AUDIT_VH.py C330_ROOTFREE_G5_INPUT.json OUT` with a fresh OUT directory. Expected terminal marker begins EXACT_VH_AB_FILLED_MASS_PASS and includes VEF[57,165,110], strict[2,1,1], weak[0,0,0], primitive_zeros[0,0,0]. This is a NONWINNER, not own110. The generated RAW/A/B/MASS bytes and SHA256 are given in part1. A and B independently reconstruct the complete H-hull and maximal faces/true edges. Third integration uses positive centered integer tetrahedra and checks zero first moments. The complete source packet was cold-replayed before this preservation, including positive/weak/invalid controls. This two-part geometry/audit capsule does not contain the separate global cut and chain certificates.

Source identities: AUDIT_VH.py2047bytes SHA7f036e69a43492a747288d0e76e55cc00d30e84a678fe901b5187c8fc057726b; exact_source/check_A.py5483bytes SHAad72cc198140249c1e52a615513354036c04f4c718333a7beed64fba4b43d7f3; exact_source/check_B.py6351bytes SHAb0cb62d5486b32d020b60f717f3dfe9d07c6c9a978492928f54c3a38f396fc24; exact_source/centred_mass.py1328bytes SHAcc0ad7d58764902ca3d308539f7a133eec0f6fb2389361444808ca92694499a5. The independent A/B/mass units are unchanged inherited sources from the fully read SC83 result figure-0404. Transport integrity is separate from the mathematical predicates.

<!-- FILE AUDIT_VH.py -->
```python
"""Standalone exact bounded rational V/H hull, full mechanics and filled-mass audit.
Uses the three preserved independently written SC83 auditors in exact_source/.
Literal facet triples nominate planes only; exact A/B establish whole maximal hull.
"""
import sys,json,math,hashlib
from fractions import Fraction as Q
from pathlib import Path
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(Path(__file__).resolve().parent/'exact_source'))
import check_A as A,check_B as B,centred_mass as C
J=lambda v:json.dumps(v,sort_keys=True,separators=(',',':')).encode()
sha=lambda b:hashlib.sha256(b).hexdigest()
def audit(cfg,out):
 out=Path(out);out.mkdir(parents=True,exist_ok=False)
 den=int(cfg['grid']);assert den>0;P=[tuple(map(int,r)) for r in cfg['points']];X=[tuple(Q(v,den) for v in r) for r in P];H=[]
 for i,j,k in cfg['facet_triples']:
  n=A.cross(A.sub(P[j],P[i]),A.sub(P[k],P[i]));h=A.dot(n,P[i]);assert h
  if h<0:n=A.mul(-1,n);h=-h
  row=tuple(den*v for v in n)+(h,);d=math.gcd(*row);row=tuple(v//d for v in row)
  assert all(A.dot(row[:3],p)<=row[3]*den for p in P)
  H.append(row)
 raw=dict(H=sorted(set(H)));a=A.run(raw);b=B.run(raw);assert J(a)==J(b)
 vertices=[tuple(map(Q,r)) for r in a['raw_vertices']];assert set(vertices)==set(X),'Every supplied point must be exposed; both containments certify equality.'
 c=C.run(a);ids={}
 for name,v in [('RAW.json',raw),('A.json',a),('B.json',b),('MASS.json',c)]:
  bb=J(v);(out/name).write_bytes(bb);ids[name]=dict(bytes=len(bb),sha256=sha(bb))
 receipt=dict(name=cfg['name'],VEF=[a['V'],a['E'],a['F']],strict=a['counts'],weak=a['weak'],primitive_zeros=[a['face_primitive_zero_count'],a['vertex_max_zero_count'],a['edge_primitive_zero_count']],stable_face_ids=a['stable_face_ids'],unstable_vertices=a['unstable_vertices'],saddle_edges=a['saddle_edges'],mass=c,files=ids)
 (out/'RECEIPT.json').write_bytes(J(receipt));print('EXACT_VH_AB_FILLED_MASS_PASS',json.dumps(receipt),flush=True)
 return receipt
if __name__=='__main__':audit(json.loads(Path(sys.argv[1]).read_text()),sys.argv[2])
```

<!-- FILE exact_source/check_A.py -->
```python
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm
import sys,json
sys.set_int_max_str_digits(0)
Z=(0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(s,a):return tuple(s*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def sign(x):return (x>0)-(x<0)
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(tuple,list)):return [encode(v) for v in x]
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 return x

def polygon(X,ids,N):
 axis=max(range(3),key=lambda j:abs(N[j]));a,b=[j for j in range(3) if j!=axis];ids=sorted(ids,key=lambda i:(X[i][a],X[i][b]));lo=[];hi=[]
 def turn(i,j,k):return (X[j][a]-X[i][a])*(X[k][b]-X[i][b])-(X[j][b]-X[i][b])*(X[k][a]-X[i][a])
 for seq,out in [(ids,lo),(ids[::-1],hi)]:
  for i in seq:
   while len(out)>1 and turn(out[-2],out[-1],i)<=0:out.pop()
   out.append(i)
 cy=lo[:-1]+hi[:-1]
 if len(cy)<3:return []
 if dot(N,cross(sub(X[cy[1]],X[cy[0]]),sub(X[cy[2]],X[cy[0]])))<0:cy.reverse()
 k=cy.index(min(cy));return cy[k:]+cy[:k]

def run(raw):
 H=[tuple(map(int,r)) for r in raw['H']];assert len(H)>=4 and all(len(r)==4 and r[3]>0 for r in H);assert len(set(H))==len(H)
 N=[r[:3] for r in H];D=[r[3] for r in H];vertices=set();bounded=set()
 for i,j,k in combinations(range(len(H)),3):
  a,b,c=N[i],N[j],N[k];u=cross(b,c);v=cross(c,a);w=cross(a,b);dd=dot(a,u)
  if not dd:continue
  # Six explicit nonnegative cone decompositions certify boundedness.
  for axis in range(3):
   for s in [-1,1]:
    if all(s*t[axis]*dd>=0 for t in (u,v,w)):bounded.add((axis,s))
  p=add(add(mul(D[i],u),mul(D[j],v)),mul(D[k],w))
  if dd<0:p=mul(-1,p);dd=-dd
  if any(dot(n,p)>h*dd for n,h in zip(N,D)):continue
  gg=gcd(*p,dd);vertices.add(tuple(t//gg for t in p)+(dd//gg,))
 assert len(bounded)==6
 X=sorted(tuple(F(t,p[3]) for t in p[:3]) for p in vertices);assert len(X)>=4
 active=[];faces=[]
 for fi,(n,h) in enumerate(zip(N,D)):
  ids=[i for i,x in enumerate(X) if dot(n,x)==h];cy=polygon(X,ids,n) if len(ids)>=3 else []
  if cy:active.append(fi);faces.append(cy)
 normals=[N[i] for i in active];offsets=[D[i] for i in active];edges={};tris=[]
 for fi,cy in enumerate(faces):
  assert set(cy)=={i for i,x in enumerate(X) if dot(normals[fi],x)==offsets[fi]}
  for i,j in zip(cy,cy[1:]+cy[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append((fi,i,j))
  tris.extend((cy[0],cy[j],cy[j+1]) for j in range(1,len(cy)-1))
 assert len(X)-len(edges)+len(faces)==2 and all(len(v)==2 and v[0][1:]==v[1][1:][::-1] for v in edges.values())
 adjacency=[set() for _ in X]
 for i,j in edges:adjacency[i].add(j);adjacency[j].add(i)
 seen=set();todo=[0]
 while todo:
  i=todo.pop()
  if i not in seen:seen.add(i);todo.extend(adjacency[i]-seen)
 assert len(seen)==len(X)
 volume=F(0);moment=Z
 for i,j,k in tris:
  v=det(X[i],X[j],X[k])/6;assert v>0;volume+=v;moment=add(moment,mul(v/4,add(add(X[i],X[j]),X[k])))
 centre=mul(1/volume,moment);assert sub(moment,mul(volume,centre))==Z
 C=lcm(*(x.denominator for x in centre));M=tuple(int(x*C) for x in centre);bs=[lcm(*(v.denominator for v in x)) for x in X];aa=[tuple(int(v*b) for v in x) for x,b in zip(X,bs)];zz=[sub(mul(C,a),mul(b,M)) for a,b in zip(aa,bs)]
 def ed(i,j):return sub(mul(bs[i],aa[j]),mul(bs[j],aa[i]))
 SF=[];SW=[];UV=[];UW=[];EH=[];EW=[];fs=[];vs=[];es=[];fz=0;ez=0
 for fi,cy in enumerate(faces):
  vals=[dot(normals[fi],cross(zz[i],ed(i,j))) for i,j in zip(cy,cy[1:]+cy[:1])];sg=[sign(v) for v in vals];fs.append(sg);fz+=sg.count(0)
  if min(sg)>0:SF.append(fi)
  elif min(sg)>=0:SW.append(fi)
 for i in range(len(X)):
  js=[j for j in range(len(X)) if j!=i];j=js[0];best=dot(zz[i],ed(i,j))
  for k in js[1:]:
   val=dot(zz[i],ed(i,k));cmp=val*bs[j]-best*bs[k]
   if cmp>0 or (cmp==0 and k>j):j=k;best=val
  sg=sign(best);vs.append([j,sg])
  if sg<0:UV.append(i)
  elif sg==0:UW.append(i)
 for (i,j),pair in sorted(edges.items()):
  e=ed(i,j);ee=dot(e,e);ze=dot(zz[i],e);pn=sub(mul(ee,zz[i]),mul(ze,e));n,m=[normals[r[0]] for r in pair];nn=dot(n,n);mm=dot(m,m);nm=dot(n,m);delta=nn*mm-nm*nm;assert delta>0
  vals=[-ze*bs[j],C*ee+ze*bs[j],dot(pn,sub(mul(mm,n),mul(nm,m))),dot(pn,sub(mul(nn,m),mul(nm,n)))];sg=[sign(v) for v in vals];es.append([i,j,*sg]);ez+=sg.count(0)
  if min(sg)>0:EH.append([i,j])
  elif min(sg)>=0:EW.append([i,j])
 assert all(offsets[i]*C-dot(n,M)>0 for i,n in enumerate(normals))
 return encode(dict(V=len(X),E=len(edges),F=len(faces),active_input_indices=active,raw_vertices=X,faces=faces,edges=sorted(edges),normals=normals,offsets=offsets,ordinary_volume=volume,raw_first_moments=moment,raw_centroid=centre,centred_first_moments=Z,centred_centroid=Z,counts=[len(SF),len(UV),len(EH)],weak=[len(SW),len(UW),len(EW)],stable_face_ids=SF,unstable_vertices=UV,saddle_edges=EH,weak_faces=SW,weak_vertices=UW,weak_edges=EW,face_signs=fs,vertex_max_escape_signs=vs,edge_signs=es,face_primitive_zero_count=fz,vertex_max_zero_count=len(UW),edge_primitive_zero_count=ez,edge_primitive_count=4*len(edges),integration_triangle_count=len(tris)))
if __name__=='__main__':
 from pathlib import Path
 raw=json.loads(Path(sys.argv[1]).read_text());out=run(raw);Path(sys.argv[2]).write_text(json.dumps(out,sort_keys=True,separators=(',',':')))
 print('A',out['V'],out['E'],out['F'],out['counts'],out['weak'],flush=True)
```

<!-- FILE exact_source/check_B.py -->
```python
from fractions import Fraction as Q
from itertools import combinations
from math import lcm
import sys,json
sys.set_int_max_str_digits(0)
ZERO=(0,0,0)
def plus(a,b):return (a[0]+b[0],a[1]+b[1],a[2]+b[2])
def minus(a,b):return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def times(a,s):return tuple(x*s for x in a)
def inner(a,b):return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def outer(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def determinant(a,b,c):return inner(a,outer(b,c))
def sg(x):return 1 if x>0 else -1 if x<0 else 0
def encode(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,(tuple,list)):return [encode(v) for v in x]
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 return x

def run(raw):
 rows=[tuple(map(int,r)) for r in raw['H']];assert len(rows)>=4 and all(len(r)==4 and r[-1]>0 for r in rows);assert len(set(rows))==len(rows)
 normals=[r[:3] for r in rows];hs=[r[-1] for r in rows];points=set();lineedges=set()
 for a,b in combinations(range(len(rows)),2):
  n,m=normals[a],normals[b];d=outer(n,m);dd=inner(d,d)
  if not dd:continue
  p=plus(times(outer(m,d),hs[a]),times(outer(d,n),hs[b]));low=None;high=None;empty=False
  for nn,hh in zip(normals,hs):
   coeff=inner(nn,d);rhs=hh*dd-inner(nn,p)
   if coeff>0:
    t=Q(rhs,coeff);high=t if high is None or t<high else high
   elif coeff<0:
    t=Q(rhs,coeff);low=t if low is None or t>low else low
   elif rhs<0:empty=True;break
   if low is not None and high is not None and low>high:empty=True;break
  if empty:continue
  # An unbounded supporting line would be an unbounded edge/ray.
  assert low is not None and high is not None
  x=times(plus(p,times(d,low)),Q(1,dd));y=times(plus(p,times(d,high)),Q(1,dd));points.add(x);points.add(y)
  if low<high:lineedges.add(tuple(sorted((x,y))))
 X=sorted(points);assert len(X)>=4;index={p:i for i,p in enumerate(X)};pair_edges={tuple(sorted((index[x],index[y]))) for x,y in lineedges};faces=[];active=[]
 for fi,(normal,offset) in enumerate(zip(normals,hs)):
  ids=[i for i,p in enumerate(X) if inner(normal,p)==offset]
  if len(ids)<3:continue
  succ={}
  for a,b in combinations(ids,2):
   e=minus(X[b],X[a]);ee=inner(e,e);values={i:inner(normal,outer(e,minus(X[i],X[a]))) for i in ids};zero=[i for i in ids if values[i]==0];projections=[inner(e,minus(X[i],X[a])) for i in zero]
   if min(projections)<0 or max(projections)>ee:continue
   if min(values.values())>=0 and max(values.values())>0:succ[a]=b
   elif max(values.values())<=0 and min(values.values())<0:succ[b]=a
  if not succ:continue
  assert len(succ)>=3 and set(succ)==set(succ.values());start=min(succ);cycle=[start];b=succ[start]
  while b!=start:assert b not in cycle;cycle.append(b);b=succ[b]
  assert len(cycle)==len(succ)==len(ids);faces.append(cycle);active.append(fi)
 nrm=[normals[i] for i in active];off=[hs[i] for i in active];edges={};triangles=[];adj=[set() for _ in X]
 for fi,cy in enumerate(faces):
  for i,j in zip(cy,cy[1:]+cy[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append((fi,i,j));adj[i].add(j);adj[j].add(i)
  triangles.extend((cy[-1],cy[j],cy[j+1]) for j in range(len(cy)-2))
 assert set(edges)==pair_edges;assert len(X)-len(edges)+len(faces)==2;assert all(len(v)==2 and v[0][1:]==v[1][1:][::-1] for v in edges.values())
 visited=set();queue=[0]
 while queue:
  i=queue.pop()
  if i not in visited:visited.add(i);queue.extend(adj[i]-visited)
 assert len(visited)==len(X)
 rho=min(Q(h,100*(1+sum(map(abs,n)))) for n,h in zip(normals,hs));base=(rho,2*rho,3*rho);assert all(inner(n,base)<h for n,h in zip(normals,hs));Z=[minus(x,base) for x in X];volume=Q(0);localmoment=ZERO
 for a,b,c in triangles:
  v=determinant(Z[a],Z[b],Z[c])/6;assert v>0;volume+=v;localmoment=plus(localmoment,times(plus(plus(Z[a],Z[b]),Z[c]),v/4))
 centre=plus(base,times(localmoment,1/volume));moment=times(centre,volume);assert minus(moment,times(centre,volume))==ZERO
 C=lcm(*(v.denominator for v in centre));M=tuple(int(C*v) for v in centre);bs=[lcm(*(v.denominator for v in p)) for p in X];aa=[tuple(int(b*v) for v in p) for p,b in zip(X,bs)];zz=[minus(times(a,C),times(M,b)) for a,b in zip(aa,bs)]
 def edge(i,j):return minus(times(aa[j],bs[i]),times(aa[i],bs[j]))
 SF=[];SW=[];UV=[];UW=[];EH=[];EW=[];fs=[];vs=[];es=[];fz=0;ez=0
 for fi,cy in enumerate(faces):
  n=nrm[fi];hc=off[fi]*C-inner(n,M);nn=inner(n,n);assert hc>0;vals=[]
  for i,j in zip(cy,cy[1:]+cy[:1]):
   p=minus(times(n,bs[i]*hc),times(zz[i],nn));vals.append(inner(n,outer(edge(i,j),p)))
  signs=[sg(v) for v in vals];fs.append(signs);fz+=signs.count(0)
  if min(signs)>0:SF.append(fi)
  elif min(signs)>=0:SW.append(fi)
 for i in range(len(X)):
  largest=max(inner(zz[i],edge(i,j)) for j in adj[i]);classification=sg(largest)
  if classification<0:UV.append(i)
  elif classification==0:UW.append(i)
  best=None;jbest=None
  for j in range(len(X)):
   if j==i:continue
   value=inner(zz[i],edge(i,j))
   if best is None or value*bs[jbest]>=best*bs[j]:best=value;jbest=j
  assert sg(best)==classification;vs.append([jbest,sg(best)])
 for (i,j),pair in sorted(edges.items()):
  e=edge(i,j);ee=inner(e,e);ze=inner(zz[i],e);p=minus(times(zz[i],ee),times(e,ze));n,m=[nrm[v[0]] for v in pair];d=outer(n,m);assert inner(d,d)>0
  vals=[-ze*bs[j],C*ee+ze*bs[j],inner(outer(p,m),d),inner(outer(n,p),d)];signs=[sg(v) for v in vals];es.append([i,j,*signs]);ez+=signs.count(0)
  if min(signs)>0:EH.append([i,j])
  elif min(signs)>=0:EW.append([i,j])
 return encode(dict(V=len(X),E=len(edges),F=len(faces),active_input_indices=active,raw_vertices=X,faces=faces,edges=sorted(edges),normals=nrm,offsets=off,ordinary_volume=volume,raw_first_moments=moment,raw_centroid=centre,centred_first_moments=ZERO,centred_centroid=ZERO,counts=[len(SF),len(UV),len(EH)],weak=[len(SW),len(UW),len(EW)],stable_face_ids=SF,unstable_vertices=UV,saddle_edges=EH,weak_faces=SW,weak_vertices=UW,weak_edges=EW,face_signs=fs,vertex_max_escape_signs=vs,edge_signs=es,face_primitive_zero_count=fz,vertex_max_zero_count=len(UW),edge_primitive_zero_count=ez,edge_primitive_count=4*len(edges),integration_triangle_count=len(triangles)))
if __name__=='__main__':
 from pathlib import Path
 raw=json.loads(Path(sys.argv[1]).read_text());out=run(raw);Path(sys.argv[2]).write_text(json.dumps(out,sort_keys=True,separators=(',',':')));print('B',out['V'],out['E'],out['F'],out['counts'],out['weak'],flush=True)
```

<!-- FILE exact_source/centred_mass.py -->
```python
"""Third integration: integer tetrahedra based at the object's exact filled centroid."""
import sys,json,time,hashlib
from fractions import Fraction as F
from math import lcm
from pathlib import Path
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def run(a):
 p=[tuple(map(F,row)) for row in a['raw_vertices']];g=tuple(map(F,a['raw_centroid']));h=lcm(*(v.denominator for row in p for v in row),*(v.denominator for v in g))
 X=[tuple(int(h*(v-c)) for v,c in zip(row,g)) for row in p]
 V6=0;M24=[0,0,0];num=0
 for cy in a['faces']:
  cy=cy[2:]+cy[:2]
  for j in range(1,len(cy)-1):
   x,y,z=[X[i] for i in (cy[0],cy[j],cy[j+1])];d=dot(x,cross(y,z));assert d>0;V6+=d;num+=1
   for k in range(3):M24[k]+=d*(x[k]+y[k]+z[k])
 assert M24==[0,0,0]
 W=F(V6,6*h**3);assert W==F(a['ordinary_volume'])
 return {'status':'EXACT_CENTRED_INTEGER_TETRAHEDRA_PASS','tetrahedra':num,'common_centred_denominator_bits':h.bit_length(),'common_centred_integer_coordinate_max_bits':max(abs(v).bit_length() for row in X for v in row),'filled_first_moments':[0,0,0],'volume_agrees_with_A_and_B':True}
if __name__=='__main__':
 p=Path(sys.argv[1]);s=run(json.loads(p.read_text()));print(json.dumps(s,sort_keys=True,separators=(',',':')))
```

Optional extraction command, with both material texts saved under their displayed filenames, executed from their directory:
```python
import re,json,hashlib
from pathlib import Path
s=Path('C330_ROOTFREE_G5_COMPLETE_AUDIT_SOURCE.md').read_text()
for name,code in re.findall(r'<!-- FILE ([^\n]+) -->\n```python\n(.*?)```',s,re.S):
 p=Path(name);assert not p.is_absolute() and '..' not in p.parts;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(code)
g=Path('C330_ROOTFREE_G5_LITERAL_GEOMETRY.md').read_text();line=re.search(r'```json\n([^\n]+)\n```',g).group(1);b=line.encode();assert len(b)==2411 and hashlib.sha256(b).hexdigest()=='d2136dce7e42094ac636370e0726a1b829ad07235eb691e2036b36259e0517d7';Path('C330_ROOTFREE_G5_INPUT.json').write_bytes(b)
```
