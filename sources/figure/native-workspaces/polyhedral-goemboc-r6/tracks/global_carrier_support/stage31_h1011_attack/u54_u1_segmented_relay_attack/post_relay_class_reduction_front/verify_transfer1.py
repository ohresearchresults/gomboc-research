#!/usr/bin/env python3
"""Stdlib-only clean-room exact verifier for ordered transfer epoch 1.

No local geometry, proposal, certificate, or exact-arithmetic owner is imported.
The certificate supplies a claimed interval; all geometry and interval proofs
are reconstructed here from the frozen CSV endpoints and face ledger.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path


sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "far_u1.csv"
ENDPOINT = HERE / "transfer1_far.csv"
CERTIFICATE = HERE / "transfer1_certificate.json"
FACES = HERE.parent.parent / "continuation" / "main" / "exact_full_control_chain_post_faces.json"
SOURCE_SHA = "9f6c84382c05502766a17feb0cb9346bd44ec9f889e566e3e102d3d63a29ed77"
ENDPOINT_SHA = "1e77e096ea1285457aa4427ecc1772a82289dbcabb6a0d186651d98cc4471191"
FACES_SHA = "c1d74d638df21a0492645aa39e4d3943b8401ed0732393505c838ec2f1c0ed77"
FAR_PARAMETER = Q(1, 100)
ROOT_WIDTH = Q(1, 10**30)
ALIASES = {"edge:(1, 54):one_minus_t", "vertex:54:1"}
BASE = frozenset(range(17)) | {54}
PRIMARY = (7, 8, 245)
ACTIVE = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,54,69,72,73,88,198,224,228,
          229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,
          247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264]
BEFORE = {"class":[2,2,2], "stable_faces":[sorted(BASE),list(PRIMARY)],
          "unstable_vertices":[1,8], "saddle_edges":[[5,6],[10,11]]}
AFTER = {"class":[2,3,3], "stable_faces":[sorted(BASE),list(PRIMARY)],
         "unstable_vertices":[1,8,54], "saddle_edges":[[1,54],[5,6],[10,11]]}
DANGER = {(frozenset((198,230,231)),229),(frozenset((198,229,230)),231)}


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def qs(x): return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
def qlog(x): return -math.inf if not x else math.log10(abs(x.numerator))-math.log10(x.denominator)
def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()


@dataclass(frozen=True)
class P:
    c: tuple
    def __post_init__(self):
        c=tuple(Q(x) for x in self.c)
        while len(c)>1 and c[-1]==0: c=c[:-1]
        object.__setattr__(self,"c",c or (Q(0),))
    @staticmethod
    def zero(): return P((0,))
    @staticmethod
    def coerce(x): return x if isinstance(x,P) else P((Q(x),))
    @property
    def degree(self): return len(self.c)-1
    def __add__(self,o):
        o=P.coerce(o); n=max(len(self.c),len(o.c))
        return P(tuple((self.c[i] if i<len(self.c) else 0)+(o.c[i] if i<len(o.c) else 0) for i in range(n)))
    __radd__=__add__
    def __neg__(self): return P(tuple(-x for x in self.c))
    def __sub__(self,o): return self+(-P.coerce(o))
    def __rsub__(self,o): return P.coerce(o)-self
    def __mul__(self,o):
        o=P.coerce(o); out=[Q(0)]*(len(self.c)+len(o.c)-1)
        for i,x in enumerate(self.c):
            for j,y in enumerate(o.c): out[i+j]+=x*y
        return P(tuple(out))
    __rmul__=__mul__
    def __truediv__(self,s): return P(tuple(x/Q(s) for x in self.c))
    def derivative(self): return P.zero() if len(self.c)==1 else P(tuple(i*self.c[i] for i in range(1,len(self.c))))
    def eval(self,x):
        out=Q(0)
        for a in reversed(self.c): out=out*Q(x)+a
        return out
    def affine(self,a,b):
        z=P((Q(a),Q(b)-Q(a))); out=P.zero()
        for coefficient in reversed(self.c): out=out*z+coefficient
        return out
    def exact(self): return [qs(x) for x in self.c]


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,s): return tuple(x*s for x in a)
def dot(a,b):
    zero=P.zero() if isinstance(a[0],P) or isinstance(b[0],P) else Q(0)
    return sum((x*y for x,y in zip(a,b)),zero)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a,b,c): return dot(a,cross(b,c))
def norm2(a): return dot(a,a)


def bernstein_coefficients(poly):
    n=poly.degree
    return tuple(sum((poly.c[k]*Q(math.comb(i,k),math.comb(n,k)) for k in range(i+1)),Q(0)) for i in range(n+1))


def bernstein_sign(poly,a,b,max_depth=60):
    stack=[(Q(a),Q(b),0)]; expected=None; leaves=0; worst=None
    while stack:
        lo,hi,depth=stack.pop(); coefficients=bernstein_coefficients(poly.affine(lo,hi))
        sign=1 if all(x>0 for x in coefficients) else (-1 if all(x<0 for x in coefficients) else 0)
        if not sign:
            if depth>=max_depth: raise AssertionError(("Bernstein sign not isolated",poly.degree,qs(lo),qs(hi)))
            middle=(lo+hi)/2; stack.extend(((middle,hi,depth+1),(lo,middle,depth+1))); continue
        if expected is None: expected=sign
        elif sign!=expected: raise AssertionError("polynomial changes sign")
        leaves+=1; magnitude=min(abs(x) for x in coefficients)
        worst=qlog(magnitude) if worst is None else min(worst,qlog(magnitude))
    return expected,leaves,worst


def isolate(poly,lo,hi,width):
    lo,hi=Q(lo),Q(hi); flo,fhi=poly.eval(lo),poly.eval(hi)
    if not flo or not fhi or (flo>0)==(fhi>0): raise AssertionError("bad root bracket")
    derivative_sign,derivative_leaves,_=bernstein_sign(poly.derivative(),lo,hi)
    while hi-lo>width:
        middle=(lo+hi)/2; fm=poly.eval(middle)
        if not fm: lo=hi=middle; flo=fhi=fm; break
        if (fm>0)==(flo>0): lo,flo=middle,fm
        else: hi,fhi=middle,fm
    return {"lo":lo,"hi":hi,"value_lo":flo,"value_hi":fhi,
            "derivative_sign":derivative_sign,"derivative_bernstein_leaves":derivative_leaves}


def read_rows(path):
    out={}
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle): out[int(row["source_id"])]=tuple(Q(row[k]) for k in ("x","y","z"))
    return out


def cycle_normal(cycle,points):
    a=points[cycle[0]]
    for j in range(1,len(cycle)-1):
        normal=cross(sub(points[cycle[j]],a),sub(points[cycle[j+1]],a))
        if any(x!=0 for x in normal): return normal
    raise AssertionError(("flat face",cycle))


def centroid_numerators(points,faces):
    polynomial=isinstance(next(iter(points.values()))[0],P)
    d6=P.zero() if polynomial else Q(0); m=[P.zero() if polynomial else Q(0) for _ in range(3)]
    for cycle in faces:
        for j in range(1,len(cycle)-1):
            a,b,c=points[cycle[0]],points[cycle[j]],points[cycle[j+1]]; volume=det3(a,b,c); d6+=volume
            for k in range(3): m[k]+=volume*(a[k]+b[k]+c[k])
    return d6,tuple(m)


def edge_data(faces):
    incidence={}; neighbors={}
    for fi,cycle in enumerate(faces):
        for a,b in zip(cycle,cycle[1:]+cycle[:1]):
            edge=tuple(sorted((a,b))); incidence.setdefault(edge,[]).append(fi)
            neighbors.setdefault(a,set()).add(b); neighbors.setdefault(b,set()).add(a)
    if any(len(v)!=2 for v in incidence.values()): raise AssertionError("nonmanifold ledger")
    return incidence,{i:sorted(v) for i,v in neighbors.items()}


def mechanics(points,faces):
    d6,m24=centroid_numerators(points,faces); scale=4*d6
    centered={i:tuple(scale*points[i][k]-m24[k] for k in range(3)) for i in points}
    incidence,neighbors=edge_data(faces); face={}; reference={}
    for fi,cycle in enumerate(faces):
        normal=cycle_normal(cycle,points); nn=norm2(normal)
        zero=P.zero() if isinstance(points[cycle[0]][0],P) else Q(0)
        refpoint=tuple(sum((points[i][k] for i in cycle),zero)/len(cycle) for k in range(3))
        fkey=tuple(sorted(cycle)); face[fkey]={}; reference[fkey]={}
        for a,b in zip(cycle,cycle[1:]+cycle[:1]):
            edge=tuple(sorted((a,b))); direction=sub(points[b],points[a]); hbar=dot(normal,centered[a])
            face[fkey][edge]=dot(cross(direction,sub(mul(normal,hbar),mul(centered[a],nn))),normal)
            reference[fkey][edge]=dot(cross(direction,sub(refpoint,points[a])),normal)
    vertex={i:{j:-dot(centered[i],sub(points[j],points[i])) for j in neighbors[i]} for i in neighbors}
    edges={}
    for edge,owners in incidence.items():
        i,j=edge; direction=sub(points[j],points[i]); dd=norm2(direction); t=-dot(centered[i],direction)
        n1=cycle_normal(faces[owners[0]],points); n2=cycle_normal(faces[owners[1]],points)
        aa,ab,cc=norm2(n1),dot(n1,n2),norm2(n2); r1,r2=dot(centered[i],n1),dot(centered[i],n2)
        edges[edge]={"direction_norm2":dd,"gram":aa*cc-ab*ab,"t":t,
                     "one_minus_t":scale*dd-t,"beta1":r1*cc-r2*ab,"beta2":r2*aa-r1*ab}
    return {"d6":d6,"face":face,"reference":reference,"vertex":vertex,"edge":edges}


def support_rows(points,faces):
    labels=set(points)
    for fi,cycle in enumerate(faces):
        normal=cycle_normal(cycle,points); anchor=points[cycle[0]]
        for member in cycle[1:]:
            if dot(normal,sub(points[member],anchor))!=P.zero(): raise AssertionError(("moving coplanarity",fi,member))
        for witness in sorted(labels-set(cycle)):
            yield fi,witness,dot(normal,sub(points[witness],anchor))


def primitive_rows(points,faces):
    ledger=mechanics(points,faces); yield "volume_d6",ledger["d6"],"mechanics_denominator"
    for fi,witness,poly in support_rows(points,faces): yield f"support:f{fi}:w{witness}",poly,"support"
    for fi,cycle in enumerate(faces):
        if len(cycle)<=3: continue
        normal=cycle_normal(cycle,points)
        for offset,current in enumerate(cycle):
            previous=cycle[offset-1]; following=cycle[(offset+1)%len(cycle)]
            turn=dot(cross(sub(points[current],points[previous]),sub(points[following],points[current])),normal)
            yield f"in_face_turn:f{fi}:v{current}",turn,"in_face_turn"
    for key,values in sorted(ledger["reference"].items()):
        for edge,poly in sorted(values.items()): yield f"face_reference:{key}:{edge}",poly,"mechanics_denominator"
    for key,values in sorted(ledger["face"].items()):
        for edge,poly in sorted(values.items()): yield f"face_raw:{key}:{edge}",poly,"face_component"
    for vertex,values in sorted(ledger["vertex"].items()):
        for neighbor,poly in sorted(values.items()): yield f"vertex:{vertex}:{neighbor}",poly,"vertex_component"
    for edge,values in sorted(ledger["edge"].items()):
        for component in ("direction_norm2","gram","t","one_minus_t","beta1","beta2"):
            yield f"edge:{edge}:{component}",values[component],"edge_component"


def classify(points,faces):
    ledger=mechanics(points,faces); stable=[]
    if ledger["d6"]<=0: raise AssertionError("nonpositive volume")
    for key,values in ledger["face"].items():
        signed=[]
        for edge,raw in values.items():
            ref=ledger["reference"][key][edge]
            if not ref: raise AssertionError(("zero face reference",key,edge))
            signed.append((1 if ref>0 else -1)*raw)
        if all(x>0 for x in signed): stable.append(key)
    unstable=[i for i,values in ledger["vertex"].items() if all(x>0 for x in values.values())]
    saddles=[]
    for edge,values in ledger["edge"].items():
        if values["gram"]<=0 or values["direction_norm2"]<=0: raise AssertionError(("edge denominator",edge))
        if all(values[k]>0 for k in ("t","one_minus_t","beta1","beta2")): saddles.append(edge)
    return ledger,{"class":[len(stable),len(unstable),len(saddles)],
                   "stable_faces":[list(x) for x in sorted(stable)],
                   "unstable_vertices":sorted(unstable),"saddle_edges":[list(x) for x in sorted(saddles)]}


def hull_readback(points,faces):
    labels=set(points); incidence,_=edge_data(faces); strict=0
    for cycle in faces:
        normal=cycle_normal(cycle,points); anchor=points[cycle[0]]
        for member in cycle[1:]:
            if dot(normal,sub(points[member],anchor))!=0: raise AssertionError(("face not coplanar",cycle,member))
        values=[dot(normal,sub(points[w],anchor)) for w in sorted(labels-set(cycle))]
        if any(v==0 for v in values): raise AssertionError(("unexpected zero support",cycle))
        sign=values[0]>0
        if any((v>0)!=sign for v in values): raise AssertionError(("mixed support",cycle))
        strict+=len(values)
    active=sorted(set().union(*(set(cycle) for cycle in faces)))
    return {"f_vector":[len(active),len(incidence),len(faces)],"euler":len(active)-len(incidence)+len(faces),
            "active_labels":active,"strict_support_count":strict,"edges":sorted(incidence)}


def forced_rails():
    rails=set()
    for route in ([228]+list(range(229,247))+[8],[228]+list(range(247,265))+[8]):
        rails.update(tuple(sorted(edge)) for edge in zip(route,route[1:]))
    rails.remove((228,229)); return rails


def row230(points,faces):
    found={}
    for fi,cycle in enumerate(faces):
        normal=cycle_normal(cycle,points); anchor=points[cycle[0]]
        for witness in sorted(set(points)-set(cycle)):
            family=(frozenset(cycle),witness)
            if family in DANGER:
                value=dot(normal,sub(points[witness],anchor)); found[f"{sorted(family[0])}|{witness}"]=value*value/norm2(normal)
    if len(found)!=2 or any(v<=0 for v in found.values()): raise AssertionError(("row230",found))
    return {k:qs(v) for k,v in found.items()}


def evaluate_path(path,t): return {i:tuple(poly.eval(t) for poly in xyz) for i,xyz in path.items()}


def main():
    if sha(SOURCE)!=SOURCE_SHA or sha(ENDPOINT)!=ENDPOINT_SHA or sha(FACES)!=FACES_SHA:
        raise AssertionError(("frozen input hash",sha(SOURCE),sha(ENDPOINT),sha(FACES)))
    frozen={str(path):sha(path) for path in (SOURCE,FACES,CERTIFICATE,ENDPOINT)}
    source=read_rows(SOURCE); endpoint=read_rows(ENDPOINT); faces=json.loads(FACES.read_text()); certificate=json.loads(CERTIFICATE.read_text())
    if certificate.get("verdict")!="EXACT_ORDERED_TRANSFER1_D_EPOCH_PASS": raise AssertionError("primary verdict")
    velocity={i:tuple((endpoint[i][k]-source[i][k])/FAR_PARAMETER for k in range(3)) for i in source}
    path={i:tuple(P((source[i][k],velocity[i][k])) for k in range(3)) for i in source}
    if evaluate_path(path,FAR_PARAMETER)!=endpoint: raise AssertionError("endpoint reconstruction")
    rows=list(primitive_rows(path,faces))
    if len(rows)!=7922: raise AssertionError(("primitive count",len(rows)))
    lookup={name:poly for name,poly,_ in rows}; target=lookup["edge:(1, 54):one_minus_t"]
    aliases={name for name,poly,_ in rows if poly==target}
    if aliases!=ALIASES: raise AssertionError(("complete zero family",aliases))
    claim=certificate["exact_root"]
    if canonical(target.exact())!=claim["polynomial_digest"]: raise AssertionError("polynomial digest")
    lo,hi=Q(claim["lo"]),Q(claim["hi"]); root=isolate(target,lo,hi,ROOT_WIDTH)
    if root["lo"]!=lo or root["hi"]!=hi: raise AssertionError("noncanonical root interval")
    if target.eval(0)>=0 or target.eval(FAR_PARAMETER)<=0: raise AssertionError("target orientation")
    pre=bernstein_sign(target,Q(0),lo); post=bernstein_sign(target,hi,FAR_PARAMETER)
    if (pre[0],post[0])!=(-1,1): raise AssertionError("open target signs")
    digest=hashlib.sha256(); leaves=0; worst=None; counts={}; strict_count=0
    for index,(name,poly,family) in enumerate(rows):
        counts[family]=counts.get(family,0)+1
        if name in aliases: continue
        source_value=poly.eval(0); expected=(source_value>0)-(source_value<0)
        sign,row_leaves,margin=bernstein_sign(poly,Q(0),FAR_PARAMETER)
        if sign!=expected: raise AssertionError(("non-target sign",name,expected,sign))
        strict_count+=1; leaves+=row_leaves; worst=margin if worst is None else min(worst,margin)
        digest.update(f"{name}|{family}|{sign}|{'|'.join(poly.exact())}\n".encode())
        if index and index%1000==0: print(json.dumps({"phase":"clean_room_strict_audit","completed":index,"total":len(rows)}),flush=True)
    strict={"primitive_count":len(rows),"family_counts":counts,"strict_other_primitive_count":strict_count,
            "strict_other_bernstein_leaf_count":leaves,"strict_other_minimum_bernstein_log10_abs":worst,
            "strict_other_primitive_digest":digest.hexdigest()}
    if strict!=certificate["exhaustive_strict_other_primitives"]: raise AssertionError("primary strict receipt mismatch")
    pre_points=evaluate_path(path,lo/2); post_points=evaluate_path(path,(hi+FAR_PARAMETER)/2)
    source_ledger,source_sig=classify(source,faces); pre_ledger,pre_sig=classify(pre_points,faces)
    post_ledger,post_sig=classify(post_points,faces); endpoint_ledger,endpoint_sig=classify(endpoint,faces)
    if source_sig!=BEFORE or pre_sig!=BEFORE or post_sig!=AFTER or endpoint_sig!=AFTER:
        raise AssertionError(("open-side signatures",source_sig,pre_sig,post_sig,endpoint_sig))
    hull_source=hull_readback(source,faces); hull_endpoint=hull_readback(endpoint,faces)
    for packet in (hull_source,hull_endpoint):
        if packet["f_vector"]!=[61,162,103] or packet["euler"]!=2 or packet["active_labels"]!=ACTIVE:
            raise AssertionError(("hull contract",packet))
        if not forced_rails().issubset(set(packet["edges"])): raise AssertionError("missing forced rail")
    d6,m24=centroid_numerators(endpoint,faces); centroid=[qs(v/(4*d6)) for v in m24]
    h910={name:(value>0)-(value<0) for name,value in (("edge",endpoint_ledger["edge"][(9,10)]["one_minus_t"]),
                                                        ("vertex",endpoint_ledger["vertex"][10][9]))}
    if h910!={"edge":-1,"vertex":-1}: raise AssertionError(("H910 nonresurrection",h910))
    coordinate_hash=canonical({str(i):[qs(v) for v in endpoint[i]] for i in sorted(endpoint)})
    if coordinate_hash!=certificate["far_checkpoint"]["coordinate_hash"]: raise AssertionError("coordinate hash")
    result={
        "version":1,"clean_room_contract":{"stdlib_only_exact_proof":True,"local_owner_imports":[],
        "frozen_inputs":frozen,"reconstruction":"source plus endpoint-derived exact affine velocity"},
        "complete_zero_family":sorted(aliases),"exact_root":{k:(qs(v) if isinstance(v,Q) else v) for k,v in root.items()},
        "target_polynomial_digest":canonical(target.exact()),"exhaustive_strict_other_primitives":strict,
        "open_side_signatures":{"source":source_sig,"pre":pre_sig,"post":post_sig,"endpoint":endpoint_sig},
        "hull":{"source":{k:v for k,v in hull_source.items() if k!="edges"},
                "endpoint":{k:v for k,v in hull_endpoint.items() if k!="edges"}},
        "centroid_endpoint":centroid,"forced_rail_count":len(forced_rails()),"row230":{"source":row230(source,faces),"endpoint":row230(endpoint,faces)},
        "h910_nonresurrection":h910,"source_hashes":{str(Path(__file__).resolve()):sha(Path(__file__)),**frozen},
        "verdict":"INDEPENDENT_CLEAN_ROOM_EXACT_ORDERED_TRANSFER1_D_VERIFICATION_PASS"}
    (HERE/"transfer1_verification.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"verdict":result["verdict"],"strict_other":strict_count,"class_transition":[source_sig["class"],endpoint_sig["class"]],
                      "endpoint_sha256":sha(ENDPOINT)},indent=2),flush=True)


if __name__=="__main__": main()
