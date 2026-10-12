# material-41105eaa7aaf

AI research material

---

"""Exact two-cap cone charts: three degree-seven E17 controls.
Python >=3.10 standard library. No numerical inputs, random seeds or external files.
Run: python -S twocap.py --output twocap.json
Assertions must be enabled. All output rationals are reduced p/q strings.
"""
from fractions import Fraction as F
from itertools import combinations
from functools import cmp_to_key
from pathlib import Path
import argparse, hashlib, json, sys

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(c,a): return tuple(c*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)), F(0))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def outer(a,b): return tuple(tuple(x*y for y in b) for x in a)
def madd(A,B): return tuple(add(a,b) for a,b in zip(A,B))
def mscale(c,A): return tuple(mul(c,a) for a in A)
def mv(A,v): return tuple(dot(a,v) for a in A)
def transpose(A): return tuple(zip(*A))
def inverse(A):
    d=det(*A); assert d
    return tuple(mul(1/d,r) for r in transpose((cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))))
def positive(A):
    assert A==transpose(A)
    assert A[0][0]>0 and A[0][0]*A[1][1]-A[0][1]**2>0 and det(*A)>0

def polygon_cycle(ids, X, normal):
    """Exact angular order in a nonsingular coordinate projection."""
    drop=next(i for i in range(3) if normal[i])
    ax=[i for i in range(3) if i!=drop]
    ctr=tuple(sum((X[i][a] for i in ids),F(0))/len(ids) for a in ax)
    points={i:(X[i][ax[0]]-ctr[0],X[i][ax[1]]-ctr[1]) for i in ids}
    def half(v): return 0 if v[1]>0 or (v[1]==0 and v[0]>=0) else 1
    def cmp(i,j):
        a,b=points[i],points[j]
        if half(a)!=half(b): return -1 if half(a)<half(b) else 1
        c=a[0]*b[1]-a[1]*b[0]
        assert c!=0
        return -1 if c>0 else 1
    out=sorted(ids,key=cmp_to_key(cmp))
    if dot(cross(sub(X[out[1]],X[out[0]]),sub(X[out[2]],X[out[1]])),normal)<0:
        out.reverse()
    for i in range(len(out)):
        assert dot(cross(sub(X[out[(i+1)%len(out)]],X[out[i]]),sub(X[out[(i+2)%len(out)]],X[out[(i+1)%len(out)]])),normal)>0
    j=out.index(min(out)); return tuple(out[j:]+out[:j])

def hull(X):
    found={}
    for a,b,c in combinations(range(len(X)),3):
        n=cross(sub(X[b],X[a]),sub(X[c],X[a]));
        if n==(0,0,0): continue
        h=dot(n,X[a]); vals=[dot(n,x)-h for x in X]
        if all(v<=0 for v in vals): pass
        elif all(v>=0 for v in vals): n=mul(-1,n);h=-h;vals=[-v for v in vals]
        else: continue
        ids=tuple(i for i,v in enumerate(vals) if v==0)
        assert any(v<0 for v in vals)
        if ids not in found: found[ids]=(polygon_cycle(ids,X,n),n,h)
    return [found[q] for q in sorted(found)]

def moments(X, facets, apex):
    zero=(F(0),)*3; Z=((F(0),)*3,)*3
    D=F(0); first=zero; second=Z; cells=[]
    for cyc,n,h in facets:
        for j in range(1,len(cyc)-1):
            ids=(cyc[0],cyc[j],cyc[j+1]); tri=[X[i] for i in ids]
            q=det(*[sub(x,apex) for x in tri]); assert q>=0
            if not q: continue
            verts=[apex]+tri; S=tuple(sum((v[a] for v in verts),F(0)) for a in range(3))
            SS=outer(S,S)
            for v in verts: SS=madd(SS,outer(v,v))
            D+=q;first=add(first,mul(q,S));second=madd(second,mscale(q,SS));cells.append((ids,q))
    assert D>0
    return D/6,mul(1/(4*D),first),mscale(1/(20*D),second),cells

def chart(cut, theta):
    assert 0<theta<1
    B=[(F(j)-cut,F(j*j),F(1)) for j in range(-3,4)]
    # Strict convexity of the seven-vertex parabola chain and closing chord.
    for i in range(7):
        a,b,c=B[i],B[(i+1)%7],B[(i+2)%7]
        assert cross(sub(b,a),sub(c,b))[2]>0
    assert all(b[0]!=0 for b in B) and min(b[0] for b in B)<0<max(b[0] for b in B)
    W=[]
    for i,b in enumerate(B):
        c=B[(i+1)%7]
        if b[0]*c[0]<0:
            u=-b[0]/(c[0]-b[0]);W.append(add(b,mul(u,sub(c,b))))
    assert len(W)==2 and all(w[0]==0 for w in W)
    R=[1/(1+(1-theta)*b[0]) if b[0]>0 else 1/(1-theta*b[0]) for b in B]
    X=[(F(0),)*3]+[mul(r,b) for b,r in zip(B,R)]+W
    return B,R,W,X

def split_polygon(B, sign):
    out=[]
    for i,a in enumerate(B):
        b=B[(i+1)%len(B)]
        if sign*a[0]>0: out.append(a)
        if a[0]*b[0]<0:
            u=-a[0]/(b[0]-a[0]);out.append(add(a,mul(u,sub(b,a))))
    assert len(out)>=3
    return out

def integral_chart(B,theta):
    Z=F(0); first=(F(0),)*3; second=((F(0),)*3,)*3; records=[]
    for sign in (1,-1):
        C=split_polygon(B,sign); a=1-theta if sign==1 else -theta
        zpart=F(0);fpart=(F(0),)*3
        for j in range(1,len(C)-1):
            tri=(C[0],C[j],C[j+1]); area=det(*tri)/2; assert area>0
            l=[1+a*v[0] for v in tri]; assert min(l)>=1
            w=[mul(1/d,v) for v,d in zip(tri,l)]
            mass=area/(l[0]*l[1]*l[2]); S=tuple(sum((v[i] for v in w),F(0)) for i in range(3))
            SS=outer(S,S)
            for v in w:SS=madd(SS,outer(v,v))
            Z+=mass; zpart+=mass
            first=add(first,mul(mass/3,S)); fpart=add(fpart,mul(mass/3,S))
            second=madd(second,mscale(mass/12,SS))
        records.append({'sign':sign,'cone_volume':zpart/3,'cap_centroid':mul(1/zpart,fpart)})
    return Z/3,mul(F(3,4)/Z,first),mscale(F(3,5)/Z,second),records

def control(cut):
    theta=F(1,2);B,R,W,X=chart(cut,theta); facets=hull(X)
    edges={}
    for f,(cyc,n,h) in enumerate(facets):
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(f)
    assert len(X)==10 and len(edges)==17 and len(facets)==9
    assert all(len(fs)==2 for fs in edges.values())
    degrees=[sum(i in edge for edge in edges) for i in range(10)]
    assert degrees==[7]+[3]*9
    caps=[i for i,(cyc,_,_) in enumerate(facets) if 0 not in cyc]
    lateral=[i for i in range(9) if i not in caps]
    assert len(caps)==2 and sorted(len(facets[i][0]) for i in lateral)==[3]*5+[4]*2
    kcount=sum(b[0]<0 for b in B)
    assert sorted(len(facets[i][0]) for i in caps)==sorted((kcount+2,9-kcount))
    v,g,sec,cells=moments(X,facets,X[0])
    qapex=tuple(sum((x[i] for x in X),F(0))/10 for i in range(3))
    v2,g2,sec2,_=moments(X,facets,qapex)
    vi,gi,seci,capmom=integral_chart(B,theta)
    assert (v,g,sec)==(v2,g2,sec2)==(vi,gi,seci)
    weighted=(F(0),)*3
    for q in capmom:weighted=add(weighted,mul(q['cone_volume']/v,q['cap_centroid']))
    assert g==mul(F(3,4),weighted)
    M=tuple(tuple(map(F,r)) for r in ((13,2,1),(2,11,3),(1,3,17)))
    positive(M);N=inverse(M);positive(N)
    centered=[sub(x,g) for x in X]
    Q=[mul(1/(h-dot(n,g)),n) for cyc,n,h in facets]
    P={};T={};packets={}
    for (a,b),(f,h) in sorted(edges.items()):
        P[a,b]=dot(centered[a],mv(M,sub(centered[b],centered[a])))
        P[b,a]=dot(centered[b],mv(M,sub(centered[a],centered[b])))
        T[f,h]=dot(Q[f],mv(N,sub(Q[h],Q[f])))
        T[h,f]=dot(Q[h],mv(N,sub(Q[f],Q[h])))
        vals=(P[a,b],P[b,a],T[f,h],T[h,f]);assert all(vals)
        packets[f'{a}-{b}']={'facets':(f,h),'primitives':vals}
    unstable=[a for a in range(10) if all(v<0 for (i,j),v in P.items() if i==a)]
    stable=[a for a in range(9) if all(v<0 for (i,j),v in T.items() if i==a)]
    saddle=[edge for edge,packet in packets.items() if all(v<0 for v in packet['primitives'])]
    assert len(stable)+len(unstable)-len(saddle)==2
    assert not (len(stable)==len(unstable)==1 and not saddle)
    return {'cut':cut,'theta':theta,'chart_polygon':B,'ray_scales':R,'seam':W,'vertices':X,
      'facets':[q[0] for q in facets],'edge_incidence':{f'{a}-{b}':fs for (a,b),fs in sorted(edges.items())},
      'degree_sequence':degrees,'cap_facet_indices':caps,'cap_sizes':sorted(len(facets[i][0]) for i in caps),
      'volume':v,'centroid':g,'raw_second_moment':sec,'cap_moments':capmom,
      'M':M,'N':N,'strict_stable':stable,'strict_unstable':unstable,'strict_saddle':saddle,
      'weak_counts':[0,0,0],'nonzero_primitives':68,'edge_packets':packets}

def encode(x):
    if isinstance(x,F):return f'{x.numerator}/{x.denominator}'
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(a) for a in x]
    return x

def main():
    assert __debug__ and sys.version_info>=(3,10)
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='twocap.json');args=ap.parse_args()
    results=[control(F(a,2)) for a in (-5,-3,-1)]
    assert [r['cap_sizes'] for r in results]==[[3,8],[4,7],[5,6]]
    raw=(json.dumps(encode({'version':1,'controls':results}),sort_keys=True,indent=2)+'\n').encode()
    Path(args.output).write_bytes(raw)
    for r in results:print('CONTROL',r['cut'],r['cap_sizes'],len(r['strict_stable']),len(r['strict_unstable']),len(r['strict_saddle']))
    print('DEGREE7_TWO_CAP_THREE_TYPES_EXACT_MOMENTS_AND_MECHANICS_PASS',len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
