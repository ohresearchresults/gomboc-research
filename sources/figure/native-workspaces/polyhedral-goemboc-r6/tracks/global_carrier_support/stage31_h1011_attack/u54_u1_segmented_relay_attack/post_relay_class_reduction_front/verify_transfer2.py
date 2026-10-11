#!/usr/bin/env python3
"""Stdlib-only clean-room exact verifier for ordered transfer epoch 2."""
from __future__ import annotations
import csv, hashlib, json, math, sys
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path

sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
SOURCE=HERE/"transfer1_far.csv"; ENDPOINT=HERE/"transfer2_far.csv"
CERTIFICATE=HERE/"transfer2_certificate.json"
FACES=HERE.parent.parent/"continuation"/"main"/"exact_full_control_chain_post_faces.json"
SOURCE_SHA="1e77e096ea1285457aa4427ecc1772a82289dbcabb6a0d186651d98cc4471191"
ENDPOINT_SHA="3e15e92981bf9437e76578feeec3d5b512505a11017878b0c453fd5ed104c253"
FACES_SHA="c1d74d638df21a0492645aa39e4d3943b8401ed0732393505c838ec2f1c0ed77"
FAR=Q(27,1000); WIDTH=Q(1,10**30)
ALIASES={"edge:(9, 10):one_minus_t","vertex:10:9"}
BASE=frozenset(range(17))|{54}; PRIMARY=(7,8,245)
ACTIVE=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,54,69,72,73,88,198,224,228,
229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,
249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264]
BEFORE={"class":[2,3,3],"stable_faces":[sorted(BASE),list(PRIMARY)],"unstable_vertices":[1,8,54],
        "saddle_edges":[[1,54],[5,6],[10,11]]}
AFTER={"class":[2,4,4],"stable_faces":[sorted(BASE),list(PRIMARY)],"unstable_vertices":[1,8,10,54],
       "saddle_edges":[[1,54],[5,6],[9,10],[10,11]]}
DANGER={(frozenset((198,230,231)),229),(frozenset((198,229,230)),231)}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def qs(x): return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def qlog(x): return -math.inf if not x else math.log10(abs(x.numerator))-math.log10(x.denominator)
def canonical(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

@dataclass(frozen=True)
class P:
 c:tuple
 def __post_init__(self):
  c=tuple(Q(x) for x in self.c)
  while len(c)>1 and c[-1]==0:c=c[:-1]
  object.__setattr__(self,"c",c or (Q(0),))
 @staticmethod
 def zero():return P((0,))
 @staticmethod
 def coerce(x):return x if isinstance(x,P) else P((Q(x),))
 @property
 def degree(self):return len(self.c)-1
 def __add__(self,o):
  o=P.coerce(o);n=max(len(self.c),len(o.c));return P(tuple((self.c[i] if i<len(self.c) else 0)+(o.c[i] if i<len(o.c) else 0) for i in range(n)))
 __radd__=__add__
 def __neg__(self):return P(tuple(-x for x in self.c))
 def __sub__(self,o):return self+(-P.coerce(o))
 def __rsub__(self,o):return P.coerce(o)-self
 def __mul__(self,o):
  o=P.coerce(o);out=[Q(0)]*(len(self.c)+len(o.c)-1)
  for i,x in enumerate(self.c):
   for j,y in enumerate(o.c):out[i+j]+=x*y
  return P(tuple(out))
 __rmul__=__mul__
 def __truediv__(self,s):return P(tuple(x/Q(s) for x in self.c))
 def derivative(self):return P.zero() if len(self.c)==1 else P(tuple(i*self.c[i] for i in range(1,len(self.c))))
 def eval(self,x):
  out=Q(0)
  for a in reversed(self.c):out=out*Q(x)+a
  return out
 def affine(self,a,b):
  z=P((Q(a),Q(b)-Q(a)));out=P.zero()
  for v in reversed(self.c):out=out*z+v
  return out
 def exact(self):return [qs(x) for x in self.c]

def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,s):return tuple(x*s for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),P.zero() if isinstance(a[0],P) or isinstance(b[0],P) else Q(0))
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a,b,c):return dot(a,cross(b,c))
def norm2(a):return dot(a,a)
def bcoeff(p):
 n=p.degree;return tuple(sum((p.c[k]*Q(math.comb(i,k),math.comb(n,k)) for k in range(i+1)),Q(0)) for i in range(n+1))
def bsign(p,a,b,depth=60):
 stack=[(Q(a),Q(b),0)];expected=None;leaves=0;worst=None
 while stack:
  lo,hi,d=stack.pop();c=bcoeff(p.affine(lo,hi));s=1 if all(x>0 for x in c) else(-1 if all(x<0 for x in c) else 0)
  if not s:
   if d>=depth:raise AssertionError(("Bernstein",p.degree,qs(lo),qs(hi)))
   m=(lo+hi)/2;stack.extend(((m,hi,d+1),(lo,m,d+1)));continue
  if expected is None:expected=s
  elif s!=expected:raise AssertionError("sign change")
  leaves+=1;v=min(abs(x) for x in c);worst=qlog(v) if worst is None else min(worst,qlog(v))
 return expected,leaves,worst
def isolate(p,lo,hi):
 lo,hi=Q(lo),Q(hi);flo,fhi=p.eval(lo),p.eval(hi)
 if not flo or not fhi or(flo>0)==(fhi>0):raise AssertionError("root bracket")
 ds,dl,_=bsign(p.derivative(),lo,hi)
 while hi-lo>WIDTH:
  m=(lo+hi)/2;fm=p.eval(m)
  if not fm:lo=hi=m;flo=fhi=fm;break
  if(fm>0)==(flo>0):lo,flo=m,fm
  else:hi,fhi=m,fm
 return{"lo":lo,"hi":hi,"value_lo":flo,"value_hi":fhi,"derivative_sign":ds,"derivative_bernstein_leaves":dl}
def read_rows(p):
 out={}
 with p.open(newline="") as h:
  for r in csv.DictReader(h):out[int(r["source_id"])]=tuple(Q(r[k]) for k in("x","y","z"))
 return out
def normal(cycle,points):
 a=points[cycle[0]]
 for j in range(1,len(cycle)-1):
  n=cross(sub(points[cycle[j]],a),sub(points[cycle[j+1]],a))
  if any(x!=0 for x in n):return n
 raise AssertionError("flat face")
def centroid_num(points,faces):
 poly=isinstance(next(iter(points.values()))[0],P);d=P.zero() if poly else Q(0);m=[P.zero() if poly else Q(0) for _ in range(3)]
 for c in faces:
  for j in range(1,len(c)-1):
   a,b,z=points[c[0]],points[c[j]],points[c[j+1]];v=det3(a,b,z);d+=v
   for k in range(3):m[k]+=v*(a[k]+b[k]+z[k])
 return d,tuple(m)
def edges_of(faces):
 inc={};neighbors={}
 for fi,c in enumerate(faces):
  for a,b in zip(c,c[1:]+c[:1]):
   e=tuple(sorted((a,b)));inc.setdefault(e,[]).append(fi);neighbors.setdefault(a,set()).add(b);neighbors.setdefault(b,set()).add(a)
 if any(len(v)!=2 for v in inc.values()):raise AssertionError("nonmanifold")
 return inc,{i:sorted(v) for i,v in neighbors.items()}
def mechanics(points,faces):
 d,m=centroid_num(points,faces);scale=4*d;center={i:tuple(scale*points[i][k]-m[k] for k in range(3)) for i in points}
 inc,neighbors=edges_of(faces);face={};refs={}
 for fi,c in enumerate(faces):
  n=normal(c,points);nn=norm2(n);zero=P.zero() if isinstance(points[c[0]][0],P) else Q(0)
  rp=tuple(sum((points[i][k] for i in c),zero)/len(c) for k in range(3));key=tuple(sorted(c));face[key]={};refs[key]={}
  for a,b in zip(c,c[1:]+c[:1]):
   e=tuple(sorted((a,b)));direction=sub(points[b],points[a]);h=dot(n,center[a])
   face[key][e]=dot(cross(direction,sub(mul(n,h),mul(center[a],nn))),n)
   refs[key][e]=dot(cross(direction,sub(rp,points[a])),n)
 vertex={i:{j:-dot(center[i],sub(points[j],points[i])) for j in neighbors[i]} for i in neighbors};edge={}
 for e,owners in inc.items():
  i,j=e;direction=sub(points[j],points[i]);dd=norm2(direction);t=-dot(center[i],direction)
  n1,n2=normal(faces[owners[0]],points),normal(faces[owners[1]],points);aa,ab,cc=norm2(n1),dot(n1,n2),norm2(n2)
  r1,r2=dot(center[i],n1),dot(center[i],n2)
  edge[e]={"direction_norm2":dd,"gram":aa*cc-ab*ab,"t":t,"one_minus_t":scale*dd-t,
           "beta1":r1*cc-r2*ab,"beta2":r2*aa-r1*ab}
 return{"d6":d,"face":face,"reference":refs,"vertex":vertex,"edge":edge}
def supports(points,faces):
 labels=set(points)
 for fi,c in enumerate(faces):
  n=normal(c,points);a=points[c[0]]
  for i in c[1:]:
   if dot(n,sub(points[i],a))!=P.zero():raise AssertionError(("coplanarity",fi,i))
  for w in sorted(labels-set(c)):yield fi,w,dot(n,sub(points[w],a))
def primitives(points,faces):
 l=mechanics(points,faces);yield"volume_d6",l["d6"],"mechanics_denominator"
 for fi,w,p in supports(points,faces):yield f"support:f{fi}:w{w}",p,"support"
 for fi,c in enumerate(faces):
  if len(c)<=3:continue
  n=normal(c,points)
  for k,v in enumerate(c):yield f"in_face_turn:f{fi}:v{v}",dot(cross(sub(points[v],points[c[k-1]]),sub(points[c[(k+1)%len(c)]],points[v])),n),"in_face_turn"
 for key,vals in sorted(l["reference"].items()):
  for e,p in sorted(vals.items()):yield f"face_reference:{key}:{e}",p,"mechanics_denominator"
 for key,vals in sorted(l["face"].items()):
  for e,p in sorted(vals.items()):yield f"face_raw:{key}:{e}",p,"face_component"
 for v,vals in sorted(l["vertex"].items()):
  for w,p in sorted(vals.items()):yield f"vertex:{v}:{w}",p,"vertex_component"
 for e,vals in sorted(l["edge"].items()):
  for k in("direction_norm2","gram","t","one_minus_t","beta1","beta2"):yield f"edge:{e}:{k}",vals[k],"edge_component"
def classify(points,faces):
 l=mechanics(points,faces);stable=[]
 if l["d6"]<=0:raise AssertionError("volume")
 for key,vals in l["face"].items():
  signed=[]
  for e,raw in vals.items():
   ref=l["reference"][key][e]
   if not ref:raise AssertionError("reference")
   signed.append((1 if ref>0 else-1)*raw)
  if all(v>0 for v in signed):stable.append(key)
 unstable=[i for i,v in l["vertex"].items() if all(x>0 for x in v.values())];saddles=[]
 for e,v in l["edge"].items():
  if v["gram"]<=0 or v["direction_norm2"]<=0:raise AssertionError("denominator")
  if all(v[k]>0 for k in("t","one_minus_t","beta1","beta2")):saddles.append(e)
 return l,{"class":[len(stable),len(unstable),len(saddles)],"stable_faces":[list(x) for x in sorted(stable)],
           "unstable_vertices":sorted(unstable),"saddle_edges":[list(x) for x in sorted(saddles)]}
def hull(points,faces):
 labels=set(points);inc,_=edges_of(faces);strict=0
 for c in faces:
  n=normal(c,points);a=points[c[0]]
  for i in c[1:]:
   if dot(n,sub(points[i],a))!=0:raise AssertionError("face member")
  vals=[dot(n,sub(points[w],a)) for w in sorted(labels-set(c))]
  if any(v==0 for v in vals) or any((v>0)!=(vals[0]>0) for v in vals):raise AssertionError("support")
  strict+=len(vals)
 active=sorted(set().union(*(set(c) for c in faces)))
 return{"f_vector":[len(active),len(inc),len(faces)],"euler":len(active)-len(inc)+len(faces),"active_labels":active,
        "strict_support_count":strict,"edges":sorted(inc)}
def rails():
 out=set()
 for route in([228]+list(range(229,247))+[8],[228]+list(range(247,265))+[8]):out.update(tuple(sorted(e)) for e in zip(route,route[1:]))
 out.remove((228,229));return out
def row230(points,faces):
 out={}
 for c in faces:
  n=normal(c,points);a=points[c[0]]
  for w in sorted(set(points)-set(c)):
   fam=(frozenset(c),w)
   if fam in DANGER:
    v=dot(n,sub(points[w],a));out[f"{sorted(fam[0])}|{w}"]=v*v/norm2(n)
 if len(out)!=2 or any(v<=0 for v in out.values()):raise AssertionError("row230")
 return{k:qs(v) for k,v in out.items()}
def evaluate(path,t):return{i:tuple(p.eval(t) for p in xyz) for i,xyz in path.items()}

def main():
 if(sha(SOURCE),sha(ENDPOINT),sha(FACES))!=(SOURCE_SHA,ENDPOINT_SHA,FACES_SHA):raise AssertionError("frozen hashes")
 frozen={str(p):sha(p) for p in(SOURCE,FACES,CERTIFICATE,ENDPOINT)}
 source,endpoint=read_rows(SOURCE),read_rows(ENDPOINT);faces=json.loads(FACES.read_text());cert=json.loads(CERTIFICATE.read_text())
 if cert.get("verdict")!="EXACT_ORDERED_TRANSFER2_H910_EPOCH_PASS":raise AssertionError("primary verdict")
 velocity={i:tuple((endpoint[i][k]-source[i][k])/FAR for k in range(3)) for i in source}
 path={i:tuple(P((source[i][k],velocity[i][k])) for k in range(3)) for i in source}
 if evaluate(path,FAR)!=endpoint:raise AssertionError("endpoint reconstruction")
 rows=list(primitives(path,faces))
 if len(rows)!=7922:raise AssertionError(("primitive count",len(rows)))
 lookup={n:p for n,p,_ in rows};target=lookup["edge:(9, 10):one_minus_t"];aliases={n for n,p,_ in rows if p==target}
 if aliases!=ALIASES:raise AssertionError(("zero family",aliases))
 claim=cert["exact_root"]
 if canonical(target.exact())!=claim["polynomial_digest"]:raise AssertionError("target digest")
 lo,hi=Q(claim["lo"]),Q(claim["hi"]);root=isolate(target,lo,hi)
 if root["lo"]!=lo or root["hi"]!=hi or target.eval(0)>=0 or target.eval(FAR)<=0:raise AssertionError("root/orientation")
 if(bsign(target,0,lo)[0],bsign(target,hi,FAR)[0])!=(-1,1):raise AssertionError("open signs")
 digest=hashlib.sha256();leaves=0;worst=None;counts={};count=0
 for index,(name,p,family) in enumerate(rows):
  counts[family]=counts.get(family,0)+1
  if name in aliases:continue
  value=p.eval(0);expected=(value>0)-(value<0);sign,l,m=bsign(p,0,FAR)
  if sign!=expected:raise AssertionError(("non-target",name,expected,sign))
  count+=1;leaves+=l;worst=m if worst is None else min(worst,m);digest.update(f"{name}|{family}|{sign}|{'|'.join(p.exact())}\n".encode())
  if index and index%1000==0:print(json.dumps({"phase":"transfer2_clean_room_strict_audit","completed":index,"total":len(rows)}),flush=True)
 strict={"primitive_count":len(rows),"family_counts":counts,"strict_other_primitive_count":count,
         "strict_other_bernstein_leaf_count":leaves,"strict_other_minimum_bernstein_log10_abs":worst,
         "strict_other_primitive_digest":digest.hexdigest()}
 if strict!=cert["exhaustive_strict_other_primitives"]:raise AssertionError("strict receipt")
 pre=evaluate(path,lo/2);post=evaluate(path,(hi+FAR)/2)
 sl,ss=classify(source,faces);pl,ps=classify(pre,faces);ql,qsig=classify(post,faces);el,es=classify(endpoint,faces)
 if ss!=BEFORE or ps!=BEFORE or qsig!=AFTER or es!=AFTER:raise AssertionError(("signatures",ss,ps,qsig,es))
 hs,he=hull(source,faces),hull(endpoint,faces)
 for packet in(hs,he):
  if packet["f_vector"]!=[61,162,103] or packet["euler"]!=2 or packet["active_labels"]!=ACTIVE:raise AssertionError("hull contract")
  if not rails().issubset(set(packet["edges"])):raise AssertionError("rails")
 d,m=centroid_num(endpoint,faces);centroid=[qs(v/(4*d)) for v in m]
 h910={k:(el["edge"][(9,10)][k]>0)-(el["edge"][(9,10)][k]<0) for k in("t","one_minus_t","beta1","beta2")}
 if set(h910.values())!={1}:raise AssertionError(("H910 alive",h910))
 d_alias={"edge":(lookup["edge:(1, 54):one_minus_t"].eval(FAR)>0)-(lookup["edge:(1, 54):one_minus_t"].eval(FAR)<0),
          "vertex":(lookup["vertex:54:1"].eval(FAR)>0)-(lookup["vertex:54:1"].eval(FAR)<0)}
 if d_alias!={"edge":1,"vertex":1}:raise AssertionError(("D aliases",d_alias))
 coordinate_hash=canonical({str(i):[globals()["qs"](v) for v in endpoint[i]] for i in sorted(endpoint)})
 if coordinate_hash!=cert["far_checkpoint"]["coordinate_hash"]:raise AssertionError("coordinate hash")
 result={"version":1,"clean_room_contract":{"stdlib_only_exact_proof":True,"local_owner_imports":[],"frozen_inputs":frozen,
         "reconstruction":"transfer1 FAR plus transfer2 endpoint-derived exact affine velocity"},
         "complete_zero_family":sorted(aliases),"exact_root":{k:(globals()["qs"](v) if isinstance(v,Q) else v) for k,v in root.items()},
         "target_polynomial_digest":canonical(target.exact()),"exhaustive_strict_other_primitives":strict,
         "open_side_signatures":{"source":ss,"pre":ps,"post":qsig,"endpoint":es},
         "hull":{"source":{k:v for k,v in hs.items() if k!="edges"},"endpoint":{k:v for k,v in he.items() if k!="edges"}},
         "centroid_endpoint":centroid,"forced_rail_count":len(rails()),"row230":{"source":row230(source,faces),"endpoint":row230(endpoint,faces)},
         "h910_alive":h910,"D_aliases_positive":d_alias,"source_hashes":{str(Path(__file__).resolve()):sha(Path(__file__)),**frozen},
         "verdict":"INDEPENDENT_CLEAN_ROOM_EXACT_ORDERED_TRANSFER2_H910_VERIFICATION_PASS"}
 (HERE/"transfer2_verification.json").write_text(json.dumps(result,indent=2)+"\n")
 print(json.dumps({"verdict":result["verdict"],"strict_other":count,"class_transition":[ss["class"],es["class"]],
                   "endpoint_sha256":sha(ENDPOINT)},indent=2),flush=True)
if __name__=="__main__":main()
