import hashlib,json,math,sys
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
assert __debug__, 'Run without -O'
sys.set_int_max_str_digits(0)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(k,a): return tuple(k*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
rows=[tuple(map(int,l.split())) for l in Path(sys.argv[1]).read_text().splitlines() if l.strip()]
labels=[r[0] for r in rows]; N=[r[1:] for r in rows]; D=10**12
assert len(rows)==len(set(labels))==len(set(N))==93
raw=json.dumps(dict(D=D,I=N,scale=1),separators=(',',':')).encode()
assert hashlib.sha256(raw).hexdigest()=='6ee321f92968d1214e2ceda56a823b776b4563e26e861d2e363aa586b8e9aca5'
planes=set()
for a,b,c in combinations(N,3):
    n=cross(sub(b,a),sub(c,a))
    if not any(n): continue
    h=dot(n,a); pos=neg=False
    for x in N:
        d=dot(n,x)-h; pos|=d>0; neg|=d<0
        if pos and neg: break
    if pos and neg: continue
    assert pos or neg, 'Normals must span a 3D body'
    if pos: n=mul(-1,n); h=-h
    assert h>0, 'Origin must be strictly inside the polar hull'
    g=math.gcd(*n,h); planes.add(tuple(x//g for x in n)+(h//g,))
# Preserve parent indexing: lexicographic primitive POLAR support-plane tuples.
planes=sorted(planes)
X=[tuple(Q(D*x,p[3]) for x in p[:3]) for p in planes]
contact=[{v for v,x in enumerate(X) if dot(n,x)==D} for n in N]
assert len(X)==141 and all(len(s)>=3 for s in contact)
assert all(dot(n,x)<=D for n in N for x in X)
edgeowners={}
for f,g in combinations(range(93),2):
    s=contact[f]&contact[g]
    if len(s)>=2:
        assert len(s)==2
        e=tuple(sorted(s)); assert e not in edgeowners
        edgeowners[e]=(f,g)
E=sorted(edgeowners); adj=[set() for x in X]; F=[]
for i,j in E: adj[i].add(j); adj[j].add(i)
for f,vs in enumerate(contact):
    na={i:[] for i in vs}
    for (i,j),fg in edgeowners.items():
        if f in fg: na[i].append(j); na[j].append(i)
    assert all(len(v)==2 for v in na.values())
    first=min(vs); cy=[first]; prev=first; cur=min(na[first])
    while cur!=first:
        assert cur not in cy; cy.append(cur)
        nxt=next(v for v in na[cur] if v!=prev); prev,cur=cur,nxt
    assert set(cy)==vs
    if dot(N[f],cross(sub(X[cy[1]],X[cy[0]]),sub(X[cy[2]],X[cy[0]])))<0:
        cy=[cy[0]]+cy[:0:-1]
    assert all(dot(N[f],cross(sub(X[j],X[i]),sub(X[k],X[i])))>0
               for i,j in zip(cy,cy[1:]+cy[:1]) for k in cy if k not in (i,j))
    F.append(cy)
tri=[(c[0],c[j],c[j+1]) for c in F for j in range(1,len(c)-1)]
V=Q(0); M=(Q(0),)*3
for i,j,k in tri:
    w=dot(X[i],cross(X[j],X[k])); assert w>0
    V+=w/6; M=add(M,mul(w/24,add(add(X[i],X[j]),X[k])))
c=mul(1/V,M); assert all(dot(n,c)<D for n in N)
assert sub(M,mul(V,c))==(0,0,0)
q=math.lcm(*(z.denominator for z in c)); C=tuple(int(q*z) for z in c)
b=[math.lcm(*(z.denominator for z in x)) for x in X]
A=[tuple(int(t*z) for z in x) for t,x in zip(b,X)]
Z=[sub(mul(q,x),mul(t,C)) for t,x in zip(b,A)]
def edge(i,j): return sub(mul(b[i],A[j]),mul(b[j],A[i]))
def arrow(i,j): return dot(Z[i],edge(i,j))
S=[];U=[];H=[];weak=[[],[],[]];zero=0
for f,cy in enumerate(F):
    v=min(dot(N[f],cross(Z[i],edge(i,j))) for i,j in zip(cy,cy[1:]+cy[:1]))
    if v>0:S.append(f)
    elif v==0:weak[0].append(f)
for i in range(len(X)):
    v=max(arrow(i,j) for j in adj[i])
    if v<0:U.append(i)
    elif v==0:weak[1].append(i)
for i,j in E:
    e=edge(i,j); l=dot(e,e); d=dot(Z[i],e)
    n,m=(N[f] for f in edgeowners[i,j]); aa,bb,cc=dot(n,n),dot(n,m),dot(m,m)
    assert aa*cc-bb*bb>0
    p=sub(mul(l,Z[i]),mul(d,e))
    vals=(-d*b[j],q*l+d*b[j],dot(p,sub(mul(cc,n),mul(bb,m))),dot(p,sub(mul(aa,m),mul(bb,n))))
    zero+=sum(v==0 for v in vals)
    if min(vals)>0:H.append([i,j])
    elif min(vals)==0:weak[2].append([i,j])
assert (len(X),len(E),len(F))==(141,232,93)
assert (S,U,H,weak,zero)==([3],[1,65],[[1,132]],[[],[],[]],0)
assert X[65]==(0,0,1) and len(adj[65])==44 and all(len(adj[i])==3 for i in range(141) if i!=65)
def reach(root):
    seen={root}
    while True:
        new=seen|{i for i in range(141) if any(j in seen and arrow(i,j)>0 for j in adj[i])}
        if new==seen:return seen
        seen=new
R=reach(65); B=reach(1)
assert R.isdisjoint(B) and R|B==set(range(141)) and (len(R),len(B))==(26,115)
cut=[(i,j) for i,j in E if (i in B)!=(j in B)]
assert len(cut)==67 and all(arrow(i,j)<0 and arrow(j,i)<0 for i,j in cut)
assert set(j for i in B for j in adj[i] if arrow(i,j)>0)<=B
met=[labels[f] for f,s in enumerate(contact) if s&B]
assert set(labels)-set(met)=={103}
limits=[]
for j in sorted(adj[1]):
    e=edge(1,j); d=dot(Z[1],e); assert d<0
    owner=max(range(141),key=lambda k:Q(dot(Z[k],e),b[k]))
    t=Q(-d*b[owner],dot(Z[owner],e)*b[1]-d*b[owner])
    distance2=Q(d*d,q*q*b[1]*b[1]*dot(e,e))
    floor=t.numerator*10**12//t.denominator
    dfloor=math.isqrt(distance2.numerator*10**24//distance2.denominator)
    assert Q(floor,10**12)<t<Q(floor+1,10**12)
    assert Q(dfloor,10**12)**2<distance2<Q(dfloor+1,10**12)**2
    limits.append(dict(neighbor=j,projection_maximizer=owner,removed_fraction=str(t),fraction_floor_1e12=floor,centre_distance_squared=str(distance2),distance_floor_1e12=dfloor))
assert [(x['neighbor'],x['projection_maximizer'],x['fraction_floor_1e12']) for x in limits]==[(2,65,391430389220),(23,4,322407487982),(132,126,425471657696)]
o=dict(VEF=[141,232,93],strict=[1,2,1],weak=[0,0,0],edge_primitive_zeros=zero,
       labels=labels,raw_vertices=[[str(t) for t in x] for x in X],faces=F,edges=E,
       volume=str(V),raw_first_moments=list(map(str,M)),raw_centroid=list(map(str,c)),
       centred_first_moments=['0','0','0'],apex_basin=sorted(R),unwanted_basin=sorted(B),
       basin_cut=cut,basin_support_labels=met,subtractive_mass_bounds=limits)
Path(sys.argv[2]).write_text(json.dumps(o,sort_keys=True,separators=(',',':')))
print('NH72_EXACT_PARENT_BASIN_AND_SUBTRACTIVE_MASS_BOUND_PASS')
print('VEF',o['VEF'],'strict',o['strict'],'basins',len(R),len(B),'cut',len(cut))
print('minimum_removed_fraction > 322407487982/1000000000000')
