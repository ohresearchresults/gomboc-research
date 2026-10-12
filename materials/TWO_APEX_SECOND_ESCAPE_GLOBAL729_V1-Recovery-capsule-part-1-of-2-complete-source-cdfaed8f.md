# material-cdfaed8f37df

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""TWO_APEX_SECOND_ESCAPE_GLOBAL729_V1: exact finite algebra and controls.
CPython >=3.11, standard library, assertions enabled. No random input.
python -S two_apex_second_escape.py build
python -S two_apex_second_escape.py check
The analytic proof uses Berwald's inequality; this is not its formalization.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib, json, sys
assert __debug__
IDENTITY='TWO_APEX_SECOND_ESCAPE_GLOBAL729_V1'
def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items():out[e]=out.get(e,F(0))+c
    return {e:c for e,c in out.items() if c}
def scale(p,c):return {e:v*c for e,v in p.items() if v*c}
def mul(p,q):
    out={}
    for a,u in p.items():
        for b,v in q.items():
            e=tuple(x+y for x,y in zip(a,b));out[e]=out.get(e,F(0))+u*v
    return {e:c for e,c in out.items() if c}
def power(p,n):
    r={(0,)*len(next(iter(p))):F(1)}
    for _ in range(n):r=mul(r,p)
    return r
def variables(n):return [{tuple(int(i==j) for i in range(n)):F(1)} for j in range(n)]
one={(0,)*5:F(1)}
H,T,v,m,p=variables(5)
sq=lambda x:power(x,2)
u=add(sq(H),sq(T));h=sq(H);k2=add(sq(v),sq(m),sq(p))
I1=add(k2,scale(mul(H,v),-1),scale(mul(T,m),-1),scale(p,-1))
I2=add(one,h,scale(mul(H,v),-1),scale(p,-1))
rows=[]
for c,d,expected in [(1,2,F(8)),(3,4,F(78,5)),(2,5,F(119,5))]:
    centre=F(4-c*d,1+c*c)
    C=F(d*d+6)-F((4-c*d)**2,1+c*c)
    assert C==expected
    Q=add(k2,scale(sq(add(scale(p,c),scale(one,d))),-1))
    lhs=add(scale(I1,2),scale(I2,6),scale(Q,-1))
    rhs=add(sq(add(v,scale(H,-4))),sq(add(m,scale(T,-1))),
        scale(sq(add(p,scale(one,-centre))),1+c*c),scale(one,C),scale(u,-1),scale(h,-9))
    assert lhs==rhs
    rows.append({'c':c,'d':d,'centre':str(centre),'constant':str(C),'a_lower':str(64*C),'GJ_lower':str(64*C+1)})
# Complete one-variable certificate for a>64u+576h on 0<w<1/4.
w,=variables(1);o={(0,):F(1)}
D=add(o,w,scale(sq(w),7));L=add(o,scale(w,-4))
Q=add(o,scale(w,5),scale(sq(w),27),scale(power(w,3),-532),scale(power(w,4),2416))
lhs=add(D,scale(mul(power(w,3),add(D,scale(sq(L),9))),-64))
assert lhs==mul(L,Q)
a=[Q.get((j,),F(0))/4**j for j in range(5)]
b=[sum(a[j]*F(comb(i,j),comb(4,j)) for j in range(i+1)) for i in range(5)]
assert b==list(map(F,[1]))+[F(21,16),F(61,32),F(45,64),F(81,16)] and min(b)>0
# Elementary numerical constants in the analytic covariance/eigenvalue proof.
assert F(4**2,comb(5,3))==F(8,5)
assert F(1)/(F(8,5)-1)==F(5,3)
assert F(15)/F(5,3)==9
assert 9*9*9==729
assert F(4997,5)>729 and F(7621,5)>729
# Exact vector helpers and a genuine own-centroid two-apex polytope control.
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def times(a,t):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
X=[(-2,-1,0),(-3,0,0),(-2,1,0),(2,1,0),(3,F(1,2),0),(F(7,2),0,0),(3,F(-1,2),0),(2,-1,0),(-1,0,1),(1,0,1)]
X=[tuple(map(F,x)) for x in X]
faces=[(0,1,2,3,4,5,6,7),(0,1,8),(1,2,8),(3,4,9),(4,5,9),(5,6,9),(6,7,9),(2,3,9,8),(7,0,8,9)]
# All supporting triples give exactly these maximal faces, not triangulation faces.
found=set()
for i,j,l in combinations(range(len(X)),3):
    n=cross(sub(X[j],X[i]),sub(X[l],X[i]))
    if not any(n):continue
    vals=[dot(n,sub(x,X[i])) for x in X]
    if max(vals)<=0 or min(vals)>=0:found.add(tuple(t for t,a in enumerate(vals) if not a))
assert found=={tuple(sorted(f)) for f in faces}
inside=tuple(sum(x[j] for x in X)/len(X) for j in range(3))
V=F(0);moment=(F(0),)*3;oriented=[];planes=[]
for face in faces:
    cyc=list(face);a,bb,cc=[X[i] for i in cyc[:3]]
    n=cross(sub(bb,a),sub(cc,a))
    if dot(n,sub(inside,a))>0:cyc.reverse();a,bb,cc=[X[i] for i in cyc[:3]];n=cross(sub(bb,a),sub(cc,a))
    hh=dot(n,a)
    assert all(dot(n,x)<=hh for x in X)
    planes.append((n,hh));oriented.append(cyc)
    for j in range(1,len(cyc)-1):
        a,bb,cc=[X[i] for i in (cyc[0],cyc[j],cyc[j+1])]
        dv=det(a,bb,cc)/6
        V+=dv;moment=plus(moment,times(plus(plus(a,bb),cc),dv/4))
assert V==F(17,4)
c=times(moment,1/V);assert c==(F(19,136),F(0),F(59,204))
Y=[sub(x,c) for x in X];poles=[]
for n,hh in planes:
    off=hh-dot(n,c);assert off>0;poles.append(times(n,1/off))
edges={tuple(sorted((f[j],f[(j+1)%len(f)]))) for f in faces for j in range(len(f))}
assert len(edges)==17
adj={i:set() for i in range(10)}
for i,j in edges:adj[i].add(j);adj[j].add(i)
U=[i for i in range(10) if all(dot(Y[i],sub(Y[j],Y[i]))<0 for j in adj[i])]
S=[i for i in range(9) if all(dot(poles[i],sub(poles[j],poles[i]))<0 for j in range(9) if j!=i)]
Hs=[]
for i,j in sorted(edges):
    owners=[k for k,f in enumerate(faces) if i in f and j in f];assert len(owners)==2
    aa,bb=owners
    if dot(Y[i],sub(Y[j],Y[i]))<0 and dot(Y[j],sub(Y[i],Y[j]))<0 and dot(poles[aa],sub(poles[bb],poles[aa]))<0 and dot(poles[bb],sub(poles[aa],poles[bb]))<0:Hs.append([i,j])
assert S==[0,7,8] and U==[1,5] and Hs==[[0,7],[2,3],[8,9]]
p0=dot(poles[0],Y[8]);s0=dot(poles[0],Y[9]);delta=-p0-s0-2
assert p0==s0==F(-145,59) and delta==F(172,59)
lam=delta/(1-s0);assert lam==F(43,51)
assert p0+3==(1-lam)*(1-s0)>0
z_escape=[j for j in sorted(adj[9]) if dot(Y[9],sub(Y[j],Y[9]))>=0]
assert z_escape and any(j in faces[0] for j in z_escape)
maxroot=max(range(10),key=lambda i:dot(Y[i],Y[i]))
assert dot(Y[maxroot],Y[maxroot])>dot(Y[8],Y[8])
# Formal local/scalar control only. It deliberately is NOT one bounded actual body.
t=[(F(3),F(0))]
for _ in range(3):a0,b0=t[-1];t.append((a0-F(7,4)*b0,b0+F(7,4)*a0))
weights=[6305,16,16,768]
assert all(sum(weights[i]*t[i][j] for i in range(4))==0 for j in range(2))
assert all(dot(t[i],sub(t[i+1],t[i]))==0 for i in range(3))
q=[a+(F(1),) for a in t];x=(F(0),F(0),F(1));B=(F(29,10),F(-1,25),F(999,1000))
dvec=(F(1),F(-84),F(-3));y=plus(x,times(dvec,F(1,3263)))
assert dot(B,y)==1 and dot(y,sub(x,y))>0
assert dot(B,sub(q[0],B))>0
u0=dot(t[0],t[0]);a0=dot(t[3],t[3]);h0=F(9,7057)
assert 64*u0+576*h0<a0<728
assert F(8)<u0+9*h0<F(78,5)
s1=F(-3009,1000);z=times(B,s1/dot(B,B))
assert dot(z,z)<1 and dot(B,z)==s1 and -dot(B,x)-s1-2==F(1,100)
assert dot(z,sub(x,z))<0
# For EVERY point b of the formal base plane B.b=1, z.(b-z) is this negative constant.
base_escape=s1/dot(B,B)-dot(z,z);assert base_escape<0
assert dot(q[3],z)>1
report={
 'identity':IDENTITY,
 'proof_kind':'analytic geometric theorem plus exact finite algebra; not a proof-assistant formalization',
 'parent_assignment':'minimum-0086',
 'parent_sha256':'8123315ee22b6a0fc370e8f672f299bc19997f89ad023530404946c77f994f10',
 'sos_records':rows,
 'coupled_envelope_bernstein':[str(z) for z in b],
 'global_covariance_metric_product_upper_strict':729,
 'true_body_control':{'vertices':[[str(z) for z in x] for x in X], 'facets':[list(f) for f in faces], 'VEF':[10,17,9], 'volume':str(V),'centroid':[str(z) for z in c],'S':S,'U':U,'H_edges':Hs,'p':str(p0),'s':str(s0),'delta':str(delta),'lambda':str(lam),'second_apex_weak_targets':z_escape,'failed_hypothesis':'x=8 is not the maximum-radius vertex and is not the unique unstable root'},
 'formal_local_control':{'tangents':[[str(z) for z in r] for r in t],'positive_origin_weights':weights,'base_pole':[str(z) for z in B],'x':[str(z) for z in x],'y':[str(z) for z in y],'z':[str(z) for z in z],'u':str(u0),'a':str(a0),'h':str(h0),'mass_scalar_delta':'1/100','uniform_base_escape':str(base_escape),'last_pole_support_violation':str(dot(q[3],z)-1),'status':'partial local/scalar control only; no globally realizable common-support or own-volume-centroid body is claimed'},
 'scope':{'arbitrary_vertex_and_facet_counts':True,'closing_edge_other_endpoint_must_be_in_B':True,'closing_edge_x_z_case_closed_by_this_extension':False,'all_two_apex_bodies_excluded':False,'E17_census_changed':False,'global_C_lower_changed':False,'new_attainer':False}}
def encoded(o):return (json.dumps(o,sort_keys=True,indent=2,ensure_ascii=True)+'\n').encode('utf-8')
mode=sys.argv[1] if len(sys.argv)>1 else 'build';assert mode in ('build','check')
data=encoded(report);path=Path('two_apex_second_escape.json')
if mode=='build':path.write_bytes(data)
else:assert path.read_bytes()==data
print('TWO_APEX_SECOND_ESCAPE_SOS_78_5_AND_119_5_PASS')
print('COUPLED_TANGENT_ENVELOPE_AND_GLOBAL729_CONSTANTS_PASS')
print('GENUINE_10_17_9_CONTROL_AND_FORMAL_LOCAL_FAILURE_PASS')
print(path.name,len(data),hashlib.sha256(data).hexdigest())
print('TWO_APEX_SECOND_ESCAPE_GLOBAL729_RECOVERY_PASS')
