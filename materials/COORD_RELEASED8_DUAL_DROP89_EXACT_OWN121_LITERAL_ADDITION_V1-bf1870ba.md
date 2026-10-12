# material-bf1870ba6a97

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 1/1 — COORD_RELEASED8_DUAL_DROP89_EXACT_OWN121_LITERAL_ADDITION_V1

## Result and complete dependencies

New exact uniformly FILLED own-volume-centred nonwinner: COORD_RELEASED8_DUAL_DROP89_EXACT_OWN121, true V117/E177/F62,C354,strict(S,U,H)=(1,2,1),weak000. NOT a Gömböc or a replacement of accepted C622. Delete RAW-LEX vertex89 from COORD_RELEASED8_CENTRED_DUAL_EXACT_V1 by adding the plane through its three neighbors[82,86,90]. Every other parent vertex satisfies the plane; old89 strictly violates it. The new actual raw vertices are exactly the old raw vertices except89. New Sface60,U87/89,H[1,4]; new89=old90. This is a genuine finite cancellation of old U89 and H[89,90], after recomputing the actual filled centroid. No cancellation of the remaining U/H pair is claimed.

All exact dependencies are immutable: **[internal-source-reference]**,12622B,SHA97cc3483438972b9ea41766423b5b70d23050c920426d5db71c63b5cf3066418; **[internal-source-reference]**,20558B,SHAd746f9bc13c7ba70d8ead4b72438fcaae9badbc25a08757f5a94e99222d6cf1d. Both read fully in this coordinator turn. Together they reconstruct the complete seven-source RELEASED8 parent and exact dual_gate.py plus recover_addition.py. This addition includes BOTH complete new runnable files below, not fragments. No old sandbox, Library item, numerical checkpoint, seed or coordinate rounding is necessary.

From the two dependencies extract RELEASED8.b64, DUAL_GATE_ADDITION.b64 and recover_addition.py exactly as instructed there. Run `python -B -S recover_addition.py RELEASED8.b64 DUAL_GATE_ADDITION.b64 parent-recovered` with absent destination. It reconstructs selected/ and dual-proof/. Save the two literal source blocks below as check_A.py and drop_dual_vertex.py in one directory. Then run `python -B -S drop_dual_vertex.py parent-recovered/dual-proof parent-recovered/selected drop89-proof 89` with absent destination. CPython3.13.5 standard library only, assertions enabled; no random parameters. Expected and OBSERVED terminal **RELEASED8_DUAL_ONE_UH_PAIR_EXACT_CANCELLED_AB_MASS_PASS**.

check_A.py5483B SHAad72cc198140249c1e52a615513354036c04f4c718333a7beed64fba4b43d7f3. drop_dual_vertex.py3005B SHAdecff0e866e528fb77fac3d274e515f9c63c8fb92a81d176108f3a8d037ecd5a. Input parent DUAL_A.json177936B SHAca239966a94f3fb8fbe391f78f36dc0bcd42328dc20ecf93fc49a376ef52a2d3 and DUAL_H.json8444B SHA8d69c52cc0c9ccfd87670ac6f273f114a508a25001e3046160bad140e71bffc0 are checked by the script. New INPUT.json8745B SHAc1289aa66933f28f2db8c63ed1e59321014a1b2898060398eee3755a24358736. New A.json=B.json187132B SHAcc78876896038fdf42c617a779e3ab868407a8bf57ac9a635941de778d582f24. MASS.json223B SHA3fe211cfad5a47b76eddf21e0c3d240a3be52d7557fc95526eac23e7c22ac819. RECEIPT.json records all these observed output sizes and hashes.

A enumerates every plane triple, certifies boundedness, rebuilds maximal polygons and true edges, integrates from0 and classifies every feature. B from immutable core7 independently clips each plane-pair line by all halfspaces, reconstructs polygon boundaries and integrates from a different interior point. A=B bytewise, including ALL geometry/mass/mechanical fields. Third integration from the actual exact centroid uses230 positive integer tetrahedra, yields exactly zero first moments and the same volume. Weak-only000 and all three primitive-zero counters0. Common centred denominator34493bits; largest centred integer coordinate34495bits. Exact coordinates are each reproduced raw_vertex minus reproduced raw_centroid; no rounding. The source-only six-file auxiliary replay also passed both exact tetrahedron strict446/weak000 and triangular-prism strict446/weak123 controls, but this capsule relies only on the complete two-source addition and two immutable dependencies above, not on that auxiliary archive.

## check_A.py — complete source
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

## drop_dual_vertex.py — complete source
```python
"""Exact vertex deletion by the plane through its three neighbors.
Usage: python -B -S drop_dual_vertex.py dual-proof-dir core7-source-dir output-dir [vertex]
Inputs must be reproduced by the two immutable RELEASED8 source materials.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd,lcm
import sys,json,hashlib
sys.set_int_max_str_digits(0)
assert __debug__
def pack(v):return json.dumps(v,sort_keys=True,separators=(',',':')).encode()
def write(p,v):p.write_bytes(pack(v))
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def cross(x,y):return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def main():
 proof,src,out=map(Path,sys.argv[1:4]);v=int(sys.argv[4]) if len(sys.argv)>4 else 89
 raw=(proof/'DUAL_A.json').read_bytes();assert hashlib.sha256(raw).hexdigest()=='ca239966a94f3fb8fbe391f78f36dc0bcd42328dc20ecf93fc49a376ef52a2d3'
 hb=(proof/'DUAL_H.json').read_bytes();assert hashlib.sha256(hb).hexdigest()=='8d69c52cc0c9ccfd87670ac6f273f114a508a25001e3046160bad140e71bffc0'
 a=json.loads(raw);X=[tuple(map(Q,x)) for x in a['raw_vertices']];H=json.loads(hb)['H']
 adj=sorted({j if i==v else i for i,j in a['edges'] if v in (i,j)});assert len(adj)==3
 x,y,z=[X[i] for i in adj];n=cross(sub(y,x),sub(z,x));h=dot(n,x)
 if h<0:n=tuple(-t for t in n);h=-h
 den=lcm(*(t.denominator for t in (*n,h)));row=[int(t*den) for t in (*n,h)];gg=gcd(*row);row=[t//gg for t in row]
 assert row[3]>0 and dot(row[:3],X[v])>row[3]
 assert all(dot(row[:3],x)<=row[3] for i,x in enumerate(X) if i!=v)
 data={'H':H+[row]};out.mkdir(parents=True,exist_ok=False);write(out/'INPUT.json',data)
 import check_A
 sys.path.insert(0,str(src/'upstream/core'));import check_B,centred_mass
 aa=check_A.run(data);write(out/'A.json',aa);print('A',aa['V'],aa['E'],aa['F'],aa['counts'],aa['weak'],flush=True)
 bb=check_B.run(data);write(out/'B.json',bb);assert aa==bb
 assert aa['raw_vertices']==[x for i,x in enumerate(a['raw_vertices']) if i!=v]
 assert (aa['V'],aa['E'],aa['F'])==(117,177,62)
 assert aa['counts']==[1,2,1] and aa['weak']==[0,0,0]
 mm=centred_mass.run(aa);write(out/'MASS.json',mm)
 rec={'object':'COORD_RELEASED8_DUAL_DROP'+str(v)+'_EXACT_OWN121','parent_deleted_rawlex_vertex':v,'parent_neighbor_rawlex_vertices':adj,'counts':aa['counts'],'weak':aa['weak'],'V':aa['V'],'E':aa['E'],'F':aa['F'],'C':2*aa['E'],'stable_face_ids':aa['stable_face_ids'],'unstable_vertices':aa['unstable_vertices'],'saddle_edges':aa['saddle_edges'],'zero_primitives':[aa['face_primitive_zero_count'],aa['vertex_max_zero_count'],aa['edge_primitive_zero_count']],'mass':mm,'outputs':{}}
 for name in ['INPUT.json','A.json','B.json','MASS.json']:
  b=(out/name).read_bytes();rec['outputs'][name]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
 write(out/'RECEIPT.json',rec);print(json.dumps(rec,sort_keys=True),flush=True)
 print('RELEASED8_DUAL_ONE_UH_PAIR_EXACT_CANCELLED_AB_MASS_PASS',flush=True)
if __name__=='__main__':main()
```
