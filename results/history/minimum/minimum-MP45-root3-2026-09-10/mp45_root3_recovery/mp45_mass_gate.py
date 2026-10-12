from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm
from pathlib import Path
import json,hashlib

FS=tuple(tuple(map(int,s)) for s in
 '014 021 032 043 125 154 235 347 365 376 458 487 568 678'.split())
X=[[5,2,-6],[5,5,-6],[2,5,-6],[0,0,0],[12,0,0],[0,12,0],
   [2,5,6],[5,2,6],[5,5,6]]

def reduce(A):
    a=[list(map(F,row)) for row in A]
    n=len(a[0]);r=0;piv=[];order=list(range(len(a)))
    for j in range(n):
        k=next((i for i in range(r,len(a)) if a[i][j]),None)
        if k is None:
            continue
        a[r],a[k]=a[k],a[r]
        order[r],order[k]=order[k],order[r]
        d=a[r][j];a[r]=[v/d for v in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][j]:
                d=a[i][j];a[i]=[u-d*v for u,v in zip(a[i],a[r])]
        piv.append(j);r+=1
        if r==len(a):
            break
    return a,piv,order[:r]

def nullspace(A):
    a,piv,unused=reduce(A);n=len(A[0]);out=[]
    for j in range(n):
        if j in piv:
            continue
        v=[F(0)]*n;v[j]=F(1)
        for i,k in enumerate(piv):
            v[k]=-a[i][j]
        den=lcm(*(x.denominator for x in v))
        w=[int(x*den) for x in v];gg=gcd(*w);w=[x//gg for x in w]
        if next(x for x in w if x)<0:
            w=[-x for x in w]
        assert all(sum(x*y for x,y in zip(row,w))==0 for row in A)
        out.append(w)
    return out

def det3(a,b,c):
    return sum(a[i]*(b[(i+1)%3]*c[(i+2)%3]-b[(i+2)%3]*c[(i+1)%3])
               for i in range(3))

def sub(a,b):
    return [u-v for u,v in zip(a,b)]

def tet(points,t):
    a,b,c,d=(points[i] for i in t)
    return det3(sub(b,a),sub(c,a),sub(d,a))

def detn(A):
    a=[row[:] for row in A];n=len(a);old=1;sgn=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if a[i][k]),None)
        if p is None:
            return 0
        if p!=k:
            a[k],a[p]=a[p],a[k];sgn=-sgn
        d=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=d*a[i][j]-a[i][k]*a[k][j]
                assert v%old==0
                a[i][j]=v//old
        for i in range(k+1,n):
            a[i][k]=0
        old=d
    return sgn*a[-1][-1]

def geometry():
    fans=[[(a,)+f for f in FS if a not in f] for a in range(9)]
    cells=sorted({tuple(sorted(t)) for fan in fans for t in fan})
    sig={}
    for fan in fans:
        for t in fan:
            s=(-1)**sum(t[i]>t[j] for i in range(4) for j in range(i+1,4))
            key=tuple(sorted(t))
            assert key not in sig or sig[key]==s
            sig[key]=s
    triples=list(combinations(range(9),3));index={t:i for i,t in enumerate(triples)}
    R=[[0]*len(cells) for t in triples]
    for j,t in enumerate(cells):
        for k in range(4):
            R[index[t[:k]+t[k+1:]]][j]=sig[t]*(-1)**k
    beta=nullspace(R)
    assert len(cells)==63 and len(beta)==10 and len(reduce(R)[1])==53
    f0=[int(t in {tuple(sorted(q)) for q in fans[3]}) for t in cells]
    return cells,R,beta,f0

def moments(points,cells,beta):
    rows=[];labels=[]
    for k,b in enumerate(beta):
        rows.append(b[:]);labels.append([k,0])
        for a in range(3):
            rows.append([b[j]*sum(points[i][a] for i in t) for j,t in enumerate(cells)])
            labels.append([k,1,a])
        for a in range(3):
            for c in range(a,3):
                rows.append([b[j]*(sum(points[i][a] for i in t)*sum(points[i][c] for i in t)
                                  +sum(points[i][a]*points[i][c] for i in t))
                             for j,t in enumerate(cells)])
                labels.append([k,2,a,c])
    return rows,labels

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def main():
    for f in FS:
        assert min(tet(X,(a,)+f) for a in range(9) if a not in f)>0
    cells,R,beta,f0=geometry()
    d=[abs(tet(X,t)) for t in cells]
    assert min(d)>0
    L,labels=moments(X,cells,beta)
    assert len(L)==100 and all(dot(row,d)==0 for row in L)
    unused,cols,rr=reduce(L)
    assert len(cols)==62 and len(rr)==62
    minor=[[L[i][j] for j in cols] for i in rr]
    delta=detn(minor)
    assert delta!=0

    D=dot(f0,d)
    centre=[sum(f0[j]*d[j]*sum(X[i][a] for i in t)
                for j,t in enumerate(cells))/(F(4)*D) for a in range(3)]
    Y=[[F(X[i][a])-centre[a] for a in range(3)] for i in range(9)]
    LY,unused=moments(Y,cells,beta)
    assert len(reduce(LY)[1])==62
    A=[]
    for k in range(10):
        A.extend(LY[10*k:10*k+4])
        A.append([LY[10*k+4][j]+LY[10*k+7][j]+LY[10*k+9][j] for j in range(63)])
    A.append(f0[:])
    for a in range(3):
        A.append([f0[j]*sum(Y[i][a] for i in t) for j,t in enumerate(cells)])
    traces=[sum(sum(Y[i][a] for i in t)**2 for a in range(3))
            +sum(Y[i][a]**2 for i in t for a in range(3)) for t in cells]
    A.append([f0[j]*traces[j] for j in range(63)])
    assert len(A)==55
    H=nullspace(A)
    assert len(H)>=8
    h=H[0]
    eps=min(F(d[i],2*abs(h[i])) for i in range(63) if h[i])
    fake=[F(d[i])+eps*h[i] for i in range(63)]
    assert min(fake)>0 and fake!=list(map(F,d))
    assert all(dot(row,h)==0 for row in A)
    assert dot(f0,fake)==D
    for a in range(3):
        assert sum(f0[j]*fake[j]*sum(Y[i][a] for i in t)
                   for j,t in enumerate(cells))==0
    assert sum(f0[j]*fake[j]*traces[j] for j in range(63))==sum(f0[j]*d[j]*traces[j] for j in range(63))
    violations=[(i,dot(row,fake)) for i,row in enumerate(LY) if dot(row,fake)!=0]
    assert violations
    obj=dict(identity='NOVA54_MP45_FULL_TENSOR_MASS_RIGIDITY_V1',facets=FS,fixture=X,
             cells=cells,boundary_cycles=beta,actual_six_volumes=d,
             minor_rows=rr,minor_columns=cols,minor_row_labels=[labels[i] for i in rr],
             minor_determinant=delta,actual_centroid=[str(x) for x in centre],
             scalar_control_kernel_dimension=len(H),perturbation=h,epsilon=str(eps),
             counterfeit_six_volumes=[str(x) for x in fake],
             failed_full_tensor_rows=[[i,str(v)] for i,v in violations])
    raw=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('mp45_mass_gate.json').write_bytes(raw)
    print('NOVA54_MP45_MASS_RIGIDITY_63_53_10_100_62_PASS')
    print('POSITIVE_SCALAR_COUNTERFEIT_FAILS_FULL_TENSOR_MOMENTS_PASS')
    print('mp45_mass_gate.json',len(raw),hashlib.sha256(raw).hexdigest())

if __name__=='__main__':
    main()
