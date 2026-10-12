# material-a504413d17f7

AI research material

---

"""SPHERICAL_CLOSURE_PATH718_CUT_V1. Exact rational certificate and real control.
CPython 3.13.5, standard library only. No random input. UTF-8/LF.
Run: python -S angular_closure_exact.py > angular_closure_exact.json
The continuous spherical argument is in the accompanying complete proof.
"""
from fractions import Fraction as F
from itertools import combinations
from functools import cmp_to_key
from math import comb,gcd,lcm
import json

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a,b,c):return dot(a,cross(b,c))
def solve(A,b):
    A=[list(map(F,r))+[F(v)] for r,v in zip(A,b)];n=len(b)
    for k in range(n):
        j=next(j for j in range(k,n) if A[j][k]);A[k],A[j]=A[j],A[k]
        p=A[k][k];A[k]=[x/p for x in A[k]]
        for i in range(n):
            if i!=k:
                t=A[i][k];A[i]=[x-t*y for x,y in zip(A[i],A[k])]
    return [A[i][-1] for i in range(n)]
def rank(rows):
    A=[list(map(F,r)) for r in rows];r=0
    for k in range(3):
        jj=[i for i in range(r,len(A)) if A[i][k]]
        if not jj:continue
        j=jj[0];A[r],A[j]=A[j],A[r];p=A[r][k];A[r]=[x/p for x in A[r]]
        for i in range(r+1,len(A)):
            t=A[i][k];A[i]=[x-t*y for x,y in zip(A[i],A[r])]
        r+=1
    return r

def primitive(a):
    d=lcm(*(x.denominator for x in a));v=[int(x*d) for x in a];g=gcd(*v)
    return tuple(x//g for x in v)
def hull(P):
    planes={}
    for i,j,k in combinations(range(len(P)),3):
        n=cross(sub(P[j],P[i]),sub(P[k],P[i]));h=dot(n,P[i])
        if n==(0,0,0):continue
        vals=[dot(n,x)-h for x in P]
        if all(x<=0 for x in vals):pass
        elif all(x>=0 for x in vals):n=mul(-1,n);h=-h
        else:continue
        plane=primitive(n+(-h,));planes[plane]=[l for l,x in enumerate(P) if dot(plane[:3],x)+plane[3]==0]
    vertices=sorted(i for i in range(len(P)) if rank([k[:3] for k,v in planes.items() if i in v])==3)
    facets=[]
    for plane,inds in sorted(planes.items()):
        inds=sorted(set(inds)&set(vertices));assert len(inds)>=3
        center=mul(F(1,len(inds)),tuple(sum(P[i][j] for i in inds) for j in range(3)))
        n=plane[:3];u=sub(P[inds[0]],center);v=cross(n,u)
        coords={i:(dot(sub(P[i],center),u),dot(sub(P[i],center),v)) for i in inds}
        def cmp(i,j):
            a,b=coords[i],coords[j]
            ha=0 if a[1]>0 or(a[1]==0 and a[0]>=0) else 1
            hb=0 if b[1]>0 or(b[1]==0 and b[0]>=0) else 1
            if ha!=hb:return -1 if ha<hb else 1
            z=a[0]*b[1]-a[1]*b[0]
            return -1 if z>0 else(1 if z<0 else 0)
        cyc=sorted(inds,key=cmp_to_key(cmp));assert dot(cross(sub(P[cyc[1]],P[cyc[0]]),sub(P[cyc[2]],P[cyc[0]])),n)>0
        facets.append((plane,cyc))
    edges={}
    for f,(plane,cyc) in enumerate(facets):
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):edges.setdefault(tuple(sorted((a,b))),[]).append(f)
    assert all(len(fs)==2 for fs in edges.values())
    assert len(vertices)-len(edges)+len(facets)==2
    return vertices,facets,edges

def physical_control():
    P=[];x,y=F(1),F(0)
    for i in range(10):
        z=F(1,1000) if i==4 else(F(-1,1000) if i==5 else F(0))
        P.append((x,y,z));x,y=(F(54,65)*x-F(9,26)*y,F(9,26)*x+F(54,65)*y)
    chosen=(0,4,5,9)
    bary=solve([[P[i][j] for i in chosen] for j in range(3)]+[[1]*4],[0,0,0,1])
    assert min(bary)>0
    n=[dot(x,x) for x in P]
    D=[dot(P[i],sub(P[i-1],P[i])) for i in range(1,10)]
    assert min(D)>0 and 8*n[9]>=n[0]
    closure=32*dot(P[0],P[9])+5*n[0];assert closure<0
    vertices,facets,edges=hull(P)
    den=F(0);m=[F(0)]*3
    for plane,cyc in facets:
        assert plane[3]<0
        a=P[cyc[0]]
        for j in range(1,len(cyc)-1):
            b,c=P[cyc[j]],P[cyc[j+1]];w=det3(a,b,c);assert w>0
            den+=w
            for k in range(3):m[k]+=w*(a[k]+b[k]+c[k])
    centroid=tuple(v/(4*den) for v in m);assert centroid!=(0,0,0)
    X=[sub(x,centroid) for x in P];normals=[]
    for plane,cyc in facets:
        h=-plane[3]-dot(plane[:3],centroid);assert h>0
        normals.append(mul(1/h,plane[:3]))
    stable=[];unstable=[];saddles=[];degenerate=[]
    for i,q in enumerate(normals):
        foot=mul(1/dot(q,q),q);tests=[dot(r,foot)-1 for j,r in enumerate(normals) if j!=i]
        if max(tests)<0:stable.append(i)
        elif max(tests)==0:degenerate.append(['facet',i])
    for i in vertices:
        tests=[dot(X[i],sub(X[j],X[i])) for j in vertices if j!=i]
        if max(tests)<0:unstable.append(i)
        elif max(tests)==0:degenerate.append(['vertex',i])
    for (a,b),(f,g) in sorted(edges.items()):
        s=sub(X[b],X[a]);t=-dot(X[a],s)/dot(s,s)
        p,q=normals[f],normals[g];d=sub(q,p);v=-dot(p,d)/dot(d,d)
        if 0<t<1 and 0<v<1:saddles.append([a,b])
        elif 0<=t<=1 and 0<=v<=1 and (t in (0,1) or v in(0,1)):degenerate.append(['edge',a,b])
    assert not degenerate
    assert len(stable)+len(unstable)-len(saddles)==2
    assert (len(stable),len(unstable),len(saddles))!=(1,1,0)
    return {'points':P,'positive_origin_tetrahedron':chosen,'origin_barycentric':bary,'escape_margins_at_origin':D,'last_norm_ratio':n[9]/n[0],'closure_cut':closure,'true_vertices':vertices,'facets':[cyc for _,cyc in facets],'true_edges':[list(e) for e in sorted(edges)],'six_volume':den,'own_volume_centroid':centroid,'own_COM_signature_SUH':[len(stable),len(unstable),len(saddles)],'stable_facets':stable,'unstable_vertices':unstable,'saddle_edges':saddles,'degenerate':degenerate,'status':'actual_homogeneous_control_NOT_110; designated_origin_is_NOT_own_centroid'}

def main():
    a,b=F(793,1000),F(9,10)
    assert a**9<F(1,8) and a>F(3,4)
    assert F(1837,1944)==1-F(1,18)+F(1,1944)
    assert F(1837,1944)**2<b
    Q=[F(5),F(-80),F(336),F(-512),F(256)]
    power=[sum(Q[j]*comb(j,k)*a**(j-k)*(b-a)**k for j in range(k,5)) for k in range(5)]
    bern=[sum(power[k]*F(comb(j,k),comb(4,k)) for k in range(j+1)) for j in range(5)]
    expected=[-F(4820386699,3906250000),-F(101361819,78125000),-F(3752553,3125000),-F(13317,15625),-F(79,625)]
    assert bern==expected and max(bern)<0
    Fpoly=lambda z:256*z**9-576*z**8+432*z**7-120*z**6+9*z**5
    gap=Fpoly(a)+F(5,32)
    assert gap==-F(1961990342540345421157,3906250000000000000000000) and gap<0
    # c^9 T_9(c): Chebyshev recurrence, complete integer coefficient check.
    T0=[1];T1=[0,1]
    def minus(u,v):return [(u[i] if i<len(u) else 0)-(v[i] if i<len(v) else 0) for i in range(max(len(u),len(v)))]
    for _ in range(1,9):T0,T1=T1,minus([0]+[2*x for x in T1],T0)
    assert T1==[0,9,0,-120,0,432,0,-576,0,256]
    out={'identity':'SPHERICAL_CLOSURE_PATH718_CUT_V1','interval':[a,b],'Q_Bernstein':bern,'endpoint_gap':gap,'Chebyshev_T9':T1,'control':physical_control(),'terminal':'SPHERICAL_CLOSURE_PATH718_CUT_EXACT_RATIONAL_AND_REAL_CONTROL_PASS','global_bound_change':False}
    print(json.dumps(out,default=str,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
