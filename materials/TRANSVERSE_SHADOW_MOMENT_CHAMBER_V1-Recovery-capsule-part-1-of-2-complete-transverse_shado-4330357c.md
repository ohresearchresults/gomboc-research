# material-4330357c9b5b

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

#!/usr/bin/env python3
"""TRANSVERSE_SHADOW_MOMENT_CHAMBER_V1. Exact stdlib reconstruction.
Run: python -S transverse_shadow.py build
     python -S transverse_shadow.py check
No scipy, symbolic algebra package, input downloads or omitted data are used.
Fractions represent every coordinate, coefficient and centroid exactly.
"""
from pathlib import Path
import hashlib
from itertools import product
from math import comb
from fractions import Fraction as F
from itertools import combinations
from functools import reduce
from math import gcd,lcm
import json,sys

def q(x): return x if isinstance(x,F) else F(x)
def vec(v):return tuple(map(q,v))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def plane(a,b,c,d):return det(sub(b,a),sub(c,a),sub(d,a))
def area2(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def cyclic(X,ids,n):
    k=next(k for k in range(3) if n[k]); axes=[j for j in range(3) if j!=k]
    pt={i:tuple(X[i][j] for j in axes) for i in ids}
    ordered=sorted(ids,key=lambda i:pt[i]);lo=[];hi=[]
    for i in ordered:
        while len(lo)>1 and area2(pt[lo[-2]],pt[lo[-1]],pt[i])<=0:lo.pop()
        lo.append(i)
    for i in ordered[::-1]:
        while len(hi)>1 and area2(pt[hi[-2]],pt[hi[-1]],pt[i])<=0:hi.pop()
        hi.append(i)
    r=lo[:-1]+hi[:-1]
    assert len(r)>=3
    if dot(cross(sub(X[r[1]],X[r[0]]),sub(X[r[2]],X[r[0]])),n)<0:r.reverse()
    k=r.index(min(r));return tuple(r[k:]+r[:k])

def hull(X):
    found={}
    for i,j,k in combinations(range(len(X)),3):
        n=cross(sub(X[j],X[i]),sub(X[k],X[i]))
        if not any(n):continue
        d=[dot(n,sub(x,X[i])) for x in X]
        if max(d)>0 and min(d)<0:continue
        if max(d)>0:n=mul(n,-1);d=[-t for t in d]
        if not min(d)<0:continue
        ids=tuple(l for l,t in enumerate(d) if t==0)
        found[ids]=cyclic(X,ids,n)
    faces=sorted(set(found.values()))
    vertices=sorted(set(i for f in faces for i in f))
    edges=sorted(set(tuple(sorted((f[j],f[(j+1)%len(f)]))) for f in faces for j in range(len(f))))
    assert len(vertices)-len(edges)+len(faces)==2
    return faces,vertices,edges

def tris(faces,reverse=False):
    for f in faces:
        f=f[1:]+f[:1] if reverse else f
        for j in range(1,len(f)-1):yield (f[0],f[j],f[j+1])

def mass(X,faces,ell,n,rotate=False):
    o=vec((F(1,4),)*3); V=F(0);J=vec((0,0,0));B=F(0);N=F(0)
    for i,j,k in tris(faces,rotate):
        v=det(sub(X[i],o),sub(X[j],o),sub(X[k],o))/6
        assert v>=0
        pts=[o,X[i],X[j],X[k]];V+=v
        J=add(J,mul(tuple(sum(p[c] for p in pts) for c in range(3)),v/4))
        B+=v*sum(ell[0]+dot(ell[1:],p) for p in pts)/4
        N+=v*sum(dot(n,p) for p in pts)/4
    return V,J,B,N,N/(6*V*B)

def rref(rows,m):
    A=[list(r) for r in rows if any(r)];piv=[];i=0
    for j in range(m):
        k=next((k for k in range(i,len(A)) if A[k][j]),None)
        if k is None:continue
        A[i],A[k]=A[k],A[i];z=A[i][j];A[i]=[x/z for x in A[i]]
        for k in range(len(A)):
            if k!=i and A[k][j]:
                z=A[k][j];A[k]=[x-z*y for x,y in zip(A[k],A[i])]
        piv.append(j);i+=1
        if i==len(A):break
    return A[:i],piv

def kernel(rows,m):
    A,piv=rref(rows,m);out=[]
    for j in range(m):
        if j in piv:continue
        v=[F(0)]*m;v[j]=1
        for row,k in zip(A,piv):v[k]=-row[j]
        out.append(tuple(v))
    return out

def boundary_polynomial_mass(X,faces,ell,n):
    V=F(0);B=F(0);N=F(0)
    for i,j,k in tris(faces):
        z=det(X[i],X[j],X[k]);V+=z/6
        B+=z*(4*ell[0]+sum(dot(ell[1:],X[a]) for a in (i,j,k)))/24
        N+=z*sum(dot(n,X[a]) for a in (i,j,k))/24
    return V,B,N

def shifted(X,ids,u,s):
    Y=X[:]
    for i,t in zip(ids,s):Y[i]=add(Y[i],mul(u,t))
    return Y

def chart(X,ids,u,ell,n):
    assert dot(ell[1:],u)==dot(n,u)==0
    faces,vs,es=hull(X);m=len(ids);zero=(F(0),)*m
    shifts=[shifted(X,ids,u,tuple(F(j==k) for j in range(m))) for k in range(m)]
    eq=[];ineq=[]
    def addrow(fun,tag):
        c=fun(X);a=tuple(fun(Y)-c for Y in shifts)
        assert c>=0,(tag,c)
        if c==0:
            if any(a):eq.append(a)
        elif any(a):ineq.append((c,a,tag))
    for i,j,k in tris(faces):
        for l in range(len(X)):
            addrow(lambda Z,i=i,j=j,k=k,l=l:-plane(Z[i],Z[j],Z[k],Z[l]),('support',i,j,k,l))
        o=vec((F(1,4),)*3)
        addrow(lambda Z,i=i,j=j,k=k:det(sub(Z[i],o),sub(Z[j],o),sub(Z[k],o)),('fan',i,j,k))
    for f in faces:
        norm=cross(sub(X[f[1]],X[f[0]]),sub(X[f[2]],X[f[0]]))
        if dot(norm,u)==0:
            for j in range(len(f)):
                a,b=f[j],f[(j+1)%len(f)]
                for k in f:
                    addrow(lambda Z,a=a,b=b,k=k,norm=norm:dot(cross(sub(Z[b],Z[a]),sub(Z[k],Z[a])),norm),('cycle',a,b,k))
    for i in ids:
        for c in (0,1):addrow(lambda Z,i=i,c=c:Z[i][c],('coordinate',i,c))
    v,b,nn=boundary_polynomial_mass(X,faces,ell,n)
    derivatives=[tuple(z-w for z,w in zip(boundary_polynomial_mass(Y,faces,ell,n),(v,b,nn))) for Y in shifts]
    av=tuple(z[0] for z in derivatives);ab=tuple(z[1] for z in derivatives);an=tuple(z[2] for z in derivatives)
    H=kernel(eq+[av],m)
    return faces,eq,ineq,(v,b,nn),(av,ab,an),H

def rigid_parent(delta=F(1,1000)):
    b=F(1,8);c=d=F(67,1000)
    X=[vec(v) for v in ((0,0,0),(0,0,1),(0,1,0),(1,0,0))]
    for s,w in ((F(13,16),0),(F(1),0),(F(107,100),delta)):
        z=(1-(1-c)*s-w)/(1-b)
        X.extend((vec((F(1,20000),s-F(1,20000),z)),vec((s-F(1,20000),F(1,20000),z))))
    return X,(F(1),d-1,c-1,b-1),(1+b+c,1+b+d,F(0))

# Two-variable exact sparse polynomials, with box parameters in [0,1].
def po(c):return {} if c==0 else {(0,0):F(c)}
def pa(a,b):
    o=a.copy()
    for k,v in b.items():o[k]=o.get(k,F(0))+v
    return {k:v for k,v in o.items() if v}
def pn(a):return {k:-v for k,v in a.items()}
def ps(a,b):return pa(a,pn(b))
def pm(a,b):
    o={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():o[i+k,j+l]=o.get((i+k,j+l),F(0))+v*w
    return {k:v for k,v in o.items() if v}
def pd(a,b):
    v={}
    for x,y in zip(a,b):v=pa(v,pm(x,y))
    return v
def pvsub(a,b):return tuple(ps(x,y) for x,y in zip(a,b))
def pc(a,b):return (ps(pm(a[1],b[2]),pm(a[2],b[1])),ps(pm(a[2],b[0]),pm(a[0],b[2])),ps(pm(a[0],b[1]),pm(a[1],b[0])))
def pe(a,x):return sum(v*x[0]**i*x[1]**j for (i,j),v in a.items())
def bern(a,m=3,n=3):
    assert all(i<=m and j<=n for i,j in a)
    return tuple(sum(a.get((k,l),0)*F(comb(i,k),comb(m,k))*F(comb(j,l),comb(n,l)) for k in range(i+1) for l in range(j+1)) for i in range(m+1) for j in range(n+1))
def sol(A,b):
    R,p=rref([list(a)+[v] for a,v in zip(A,b)],3);assert p==[0,1,2]
    return tuple(t[-1] for t in R)

def signed_first_moment(X,faces):
    J=vec((0,0,0))
    for i,j,k in tris(faces):
        z=det(X[i],X[j],X[k])/24
        J=add(J,mul(add(add(X[i],X[j]),X[k]),z))
    return J

def root_area_xy(X,face):
    return sum(X[i][0]*X[j][1]-X[j][0]*X[i][1]
               for i,j in zip(face,face[1:]+face[:1]))/2

def mechanics(X,faces,g):
    Z=[sub(x,g) for x in X];Q=[];inc={}
    for fi,f in enumerate(faces):
        n=cross(sub(X[f[1]],X[f[0]]),sub(X[f[2]],X[f[0]]))
        h=dot(n,Z[f[0]]);assert h>0
        Q.append(mul(n,1/h))
        for i,j in zip(f,f[1:]+f[:1]):
            inc.setdefault(tuple(sorted((i,j))),[]).append(fi)
    U={i:True for f in faces for i in f};S=[True]*len(faces)
    H=[];weak={};records=[]
    for (i,j),(f,k) in sorted(inc.items()):
        e=sub(Z[j],Z[i]);d=sub(Q[k],Q[f])
        a,b=dot(Z[i],e),dot(Z[j],mul(e,-1))
        c,d=dot(Q[f],d),dot(Q[k],mul(d,-1))
        R=(a,b,c,d)
        U[i]&=a<0;U[j]&=b<0;S[f]&=c<0;S[k]&=d<0
        if max(R)<0:H.append((i,j))
        if max(R)<=0 and 0 in R:
            t=-a/dot(e,e);w=add(Z[i],mul(e,t))
            weak.setdefault(w,[]).append((i,j))
        records.append({'edge':(i,j),'facets':(f,k),'signs':tuple((v>0)-(v<0) for v in R)})
    return {'U':[i for i in U if U[i]],'S':[faces[i] for i in range(len(S)) if S[i]],
            'H':H,'weak':[{'point':w,'edges':es} for w,es in sorted(weak.items())],
            'census_SUH':(sum(S),sum(U.values()),len(H)),
            'zero_primitive_count':sum(r['signs'].count(0) for r in records),'edge_signs':records}

def jsonable(o):
    if isinstance(o,F):return str(o)
    if isinstance(o,dict):return {str(k):jsonable(v) for k,v in o.items()}
    if isinstance(o,(tuple,list)):return [jsonable(v) for v in o]
    return o

def signed_bernstein_record(P):
    at=pe(P,(F(1,2),F(1,2)));sgn=(at>0)-(at<0);assert sgn
    coeff=tuple(sgn*b for b in bern(P));assert min(coeff)>=0
    # Bernstein coefficients are in lexicographic bidegree-(3,3) order.
    zero=tuple((i,j) for i in range(4) for j in range(4) if coeff[4*i+j]==0)
    if zero:
        assert len(zero)==4
        assert zero in (tuple((0,j) for j in range(4)),tuple((3,j) for j in range(4)),
                        tuple((i,0) for i in range(4)),tuple((i,3) for i in range(4)))
    return {'sign':sgn,'terms':[(i,j,v) for (i,j),v in sorted(P.items())],
            'signed_bernstein':coeff,'zero_indices':zero}

def exact_report():
    X,ell,n=rigid_parent();u=vec((1,-1,0));ids=tuple(range(4,10))
    faces,eq,ineq,base,der,H=chart(X,ids,u,ell,n)
    assert not eq
    V0,B0,N0=base
    assert base==(F(4263470123,21000000000),F(4553794654013,84000000000000),
                  F(184904985954453,1400000000000000))
    T0=N0/(6*V0*B0)
    assert T0==F(38830047050435130000000,19414967453661547553599)
    assert 2<T0<F(51,25)
    centers=lambda p:shifted(X,ids,u,tuple(t for t in p for _ in range(2)))
    center_basis=[tuple(F(i//2==k) for i in range(6)) for k in range(3)]
    assert kernel(list(der),6)==center_basis
    width_det=det(*[tuple(row[2*k] for k in range(3)) for row in der]);assert width_det
    J0=signed_first_moment(X,faces);g0=mul(J0,1/V0)
    root=next(f for f in faces if all(ell[0]+dot(ell[1:],X[i])==0 for i in f))
    A0=root_area_xy(X,root);assert A0==F(54369,320000)
    R=tuple(sub(signed_first_moment(centers(tuple(F(j==k) for j in range(3))),faces),J0)
            for k in range(3))
    rho=tuple(row[0] for row in R)
    assert rho==(F(7998131,672000000),F(19136473,6000000000),F(924533,1000000000))
    assert R==tuple((r,-r,F(0)) for r in rho)
    # J has degree at most two. These exact evaluations kill EVERY quadratic coefficient.
    for i in range(3):
        p=tuple(F(2 if i==j else 0) for j in range(3))
        assert signed_first_moment(centers(p),faces)==add(J0,mul(R[i],2))
        for j in range(i):
            p=tuple(F(k in (i,j)) for k in range(3))
            assert signed_first_moment(centers(p),faces)==add(J0,add(R[i],R[j]))
    # Every support/cycle/fan constraint is affine. Gather its reduced center row.
    rows=sorted({tuple((a[2*j]+a[2*j+1])/c for j in range(3)) for c,a,tag in ineq
                 if any(a[2*j]+a[2*j+1] for j in range(3))})
    assert len(rows)==38
    L=(vec((20000,0,0)),vec((F(-10720000,87),F(12460000,87),0)),
       vec((F(-1500800,3),F(5460800,3),-1340000)))
    # Six slab rows occur among the original necessary conditions. Conversely,
    # every original affine row is nonnegative at all eight slab corners.
    for a in L:
        assert a in rows and mul(a,-1) in rows
    box_corners=tuple(sol(L,vec(t)) for t in product((-1,1),repeat=3))
    assert len(set(box_corners))==8
    assert all(1+dot(a,p)>=0 for a in rows for p in box_corners)
    report={'object':'TRANSVERSE_SHADOW_MOMENT_CHAMBER_V1','literal_parent_assignment':
            'minimum-0123','ell':ell,'n':n,'direction':u,
            'initial_vertices':X,'initial_faces':faces,'VBN':base,'T':T0,'J':J0,'g':g0,
            'root_area_xy':A0,'moment_derivatives':der,'width_determinant':width_det,
            'moment_neutral_basis':center_basis,'centroid_coefficient':rho,
            'slab_rows':L,'all_38_rows':rows}
    def audit(p):
        Y=centers(p);ff,vv,ee=hull(Y)
        mm=mass(Y,ff,ell,n);assert mm==mass(Y,ff,ell,n,True)
        assert (mm[0],mm[2],mm[3])==base
        assert mm[1]==add(J0,mul(u,dot(rho,p)))
        rf=next(f for f in ff if all(ell[0]+dot(ell[1:],Y[i])==0 for i in f))
        assert root_area_xy(Y,rf)==A0
        true33=all(set(f) in [set(k) for k in ff] for f in ((0,1,2),(0,1,3)))
        census=mechanics(Y,ff,mul(mm[1],1/mm[0]))
        return {'parameters':p,'vertices':Y,'facets':ff,'edges':ee,'VEF':(len(vv),len(ee),len(ff)),
                'VBN':(mm[0],mm[2],mm[3]),'J':mm[1],'g':mul(mm[1],1/mm[0]),
                'T':mm[4],'true_coordinate_triangles':true33,'mechanics':census}
    report['strata']=[]
    for t in product((-1,0,1),repeat=3):
        p=sol(L,vec(t));a=audit(p)
        assert a['VEF']==(10,18+t.count(0),10+t.count(0))
        assert a['true_coordinate_triangles']==(t[0]==0)
        report['strata'].append({'box_face_representative':t,'body':a})
    # Original individually volume-rigid auxiliary pair, now moved jointly.
    lo=max(-c/a[2] for c,a in [(F(1),r) for r in rows] if a[2]>0)
    hi=min(-c/a[2] for c,a in [(F(1),r) for r in rows] if a[2]<0)
    assert (lo,hi)==(F(-1,1340000),F(1,1340000))
    report['auxiliary_pair_interval']=(lo,hi)
    report['auxiliary_pair_endpoints']=[audit(vec((0,0,t))) for t in (lo,hi)]
    for a in report['auxiliary_pair_endpoints']:
        assert a['VEF']==(10,20,12) and a['true_coordinate_triangles']
    # Exact whole own-centroid section. L2,L3 independently span [-1,1].
    mat=(rho,L[1],L[2])
    p00=sol(mat,vec((0,-1,-1)));p10=sol(mat,vec((0,1,-1)));p01=sol(mat,vec((0,-1,1)))
    p11=sol(mat,vec((0,1,1)))
    assert p11==sub(add(p10,p01),p00)
    assert max(abs(dot(L[0],p)) for p in (p00,p10,p01,p11))<1
    report['centroid_slice_corners']=[audit(p) for p in (p00,p10,p01,p11)]
    report['centroid_slice_strata']=[]
    for r,s in product((F(0),F(1,2),F(1)),repeat=2):
        p=add(p00,add(mul(sub(p10,p00),r),mul(sub(p01,p00),s)))
        a=audit(p);assert a['J']==J0 and a['true_coordinate_triangles']
        k=(r==F(1,2))+(s==F(1,2));assert a['VEF']==(10,19+k,11+k)
        assert a['mechanics']['census_SUH']==(4,4,6)
        assert a['mechanics']['weak']==[] and a['mechanics']['zero_primitive_count']==0
        report['centroid_slice_strata'].append({'box_face_representative':(r,s),'body':a})
    # Full continuous common-Euclidean-metric certificate, not sampled mechanics.
    PP=[]
    for i,x in enumerate(X):
        P=tuple(po(v) for v in x)
        if i>=4:
            k=(i-4)//2;t={(0,0):p00[k],(1,0):p10[k]-p00[k],(0,1):p01[k]-p00[k]}
            P=(pa(P[0],t),ps(P[1],t),P[2])
        PP.append(P)
    Z=[tuple(ps(x,po(c)) for x,c in zip(P,g0)) for P in PP]
    NN=[];HH=[];ef={};support_records=[]
    for k,f in enumerate(faces):
        nn=pc(pvsub(PP[f[1]],PP[f[0]]),pvsub(PP[f[2]],PP[f[0]]));h=pd(nn,Z[f[0]])
        assert min(bern(h))>0
        assert all(sum(t)<=1 for p in nn for t in p) and all(sum(t)<=1 for t in h)
        NN.append(nn);HH.append(h);support_records.append(signed_bernstein_record(h))
        for a,b in zip(f,f[1:]+f[:1]):ef.setdefault(tuple(sorted((a,b))),[]).append(k)
    cert=[];nonstrict=[]
    for (i,j),(f,k) in sorted(ef.items()):
        dp=(pd(Z[i],pvsub(Z[j],Z[i])),pd(Z[j],pvsub(Z[i],Z[j])))
        dq=(pd(NN[f],tuple(ps(pm(HH[f],v),pm(HH[k],w)) for v,w in zip(NN[k],NN[f]))),
            pd(NN[k],tuple(ps(pm(HH[k],v),pm(HH[f],w)) for v,w in zip(NN[f],NN[k]))))
        rec=[signed_bernstein_record(P) for P in dp+dq]
        assert all(not r['zero_indices'] for r in rec[:2])
        for j0,r in enumerate(rec):
            if r['zero_indices']:nonstrict.append(((i,j),j0))
        cert.append({'edge':(i,j),'old_facets':(f,k),'primitive_polynomials':rec})
    assert len(cert)==21 and len(nonstrict)==8
    assert {e for e,j in nonstrict}=={(2,4),(2,6),(3,5),(3,7)}
    assert all(j in (2,3) for e,j in nonstrict)
    report['continuous_446_certificate']={'degree_elevation':(3,3),'support_heights':support_records,
                                         'old_edge_primitives':cert,'boundary_zero_rows':nonstrict}
    return report

def report_bytes():
    return (json.dumps(jsonable(exact_report()),sort_keys=True,indent=2,ensure_ascii=True)+'\n').encode('ascii')

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):
        raise SystemExit('usage: python -S transverse_shadow.py build|check')
    raw=report_bytes();out=Path('transverse_shadow_report.json')
    if sys.argv[1]=='build':out.write_bytes(raw)
    else:
        if not out.is_file() or out.read_bytes()!=raw:raise SystemExit('REPORT_BYTES_MISMATCH')
    print('TRANSVERSE_SHADOW_MOMENT_CHAMBER_V1 PASS')
    print('FULL_MOMENT_NEUTRAL_CHAMBER 3D 38_ROWS 6_SLABS 27_STRATA MIN_E18')
    print('TRUE_TRIANGLE_PAIR_AND_OWN_CENTROID_SECTION 2D 9_STRATA MIN_E19')
    print('CONTINUOUS_446_WEAK000 84_POLYNOMIALS 1344_BERNSTEIN_COEFFICIENTS PASS')
    print(out.name,len(raw),hashlib.sha256(raw).hexdigest())

if __name__=='__main__':main()
