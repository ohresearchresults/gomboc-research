# material-035a7fef8c84

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact H5 four-defect moments and 180-block stress reduction.
Python >=3.11, standard library only, assertions enabled.
No inherited certificate/solver/code is required. Variables: x,y,q,l.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib, json, math, sys
if not __debug__ or sys.version_info < (3,11):
    raise RuntimeError('Python >=3.11 and assertions enabled required')
N=4
ZERO=(0,)*N

def clean(a): return {m:c for m,c in a.items() if c}
def p(c=0): return {} if not c else {ZERO:F(c)}
def var(i):
    e=[0]*N; e[i]=1; return {tuple(e):F(1)}
def add(a,b):
    r=a.copy()
    for m,c in b.items(): r[m]=r.get(m,F(0))+c
    return clean(r)
def neg(a): return {m:-c for m,c in a.items()}
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    r={}
    for m,c in a.items():
        for n,d in b.items():
            e=tuple(m[i]+n[i] for i in range(N))
            r[e]=r.get(e,F(0))+c*d
    return clean(r)
def sc(c,a): return clean({m:F(c)*v for m,v in a.items()})
def pw(a,k):
    r=p(1)
    for _ in range(k): r=mul(r,a)
    return r
def psum(seq):
    r=p()
    for a in seq:r=add(r,a)
    return r
def vec(a,b,c):return [a,b,c]
def va(a,b):return [add(a[i],b[i]) for i in range(3)]
def vs(a,b):return [sub(a[i],b[i]) for i in range(3)]
def vc(c,a):return [sc(c,t) for t in a]
def vm(c,a):return [mul(c,t) for t in a]
def cross(a,b):
    return [sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0]))]
def dot(a,b):return psum(mul(a[i],b[i]) for i in range(3))
def sym(a,b):return [[sc(F(1,2),add(mul(a[i],b[j]),mul(b[i],a[j]))) for j in range(3)] for i in range(3)]
def ma(a,b):return [[add(a[i][j],b[i][j]) for j in range(3)] for i in range(3)]
def ms(a,b):return [[sub(a[i][j],b[i][j]) for j in range(3)] for i in range(3)]
def mc(c,a):return [[sc(c,t) for t in row] for row in a]
def mm(c,a):return [[mul(c,t) for t in row] for row in a]
def degree(a,i):return max((m[i] for m in a),default=-1)
def md(a):return [max(degree(t,i) for row in a for t in row) for i in range(N)]
def evaluate(a,pt):
    return sum((c*math.prod(pt[i]**m[i] for i in range(N)) for m,c in a.items()),F(0))
def freeze(a,i,t):
    r={}
    for m,c in a.items():
        e=list(m); e[i]=0;e=tuple(e)
        r[e]=r.get(e,F(0))+c*t**m[i]
    return clean(r)
def coeff(a,i,k):
    r={}
    for m,c in a.items():
        if m[i]==k:
            e=list(m);e[i]=0;r[tuple(e)]=c
    return clean(r)
def serialize(a):return [[*m,str(c)] for m,c in sorted(a.items())]
def bernstein(a,degrees):
    from itertools import product
    assert all(degree(a,i)<=degrees[i] for i in range(N))
    out={}
    for k in product(*(range(n+1) for n in degrees)):
        out[k]=sum((c*math.prod(F(math.comb(k[i],m[i]),math.comb(degrees[i],m[i])) for i in range(N))
                    for m,c in a.items() if all(m[i]<=k[i] for i in range(N))),F(0))
    return out
def dump(obj):return (json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()

x,y,q,l=[var(i) for i in range(N)];one=p(1);s=sub(one,l);zero=p()
b=a=F(1,4);d=F(3,4);u=v=F(1,16)
c=sub(one,sc(1-b,x));pp=mul(sub(one,q),y)
B=[(p(b),zero),(c,zero),(sub(one,pp),pp),(q,sub(one,q)),(zero,p(d)),(zero,p(a)),(p(u),p(v))]
z=[vec(mul(s,bx),mul(s,by),zero) for bx,by in B]+[vec(zero,zero,one),vec(l,zero,one),vec(zero,l,one)]
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=((0,1),(0,6),(0,7),(1,2),(1,8),(2,3),(2,8),(3,4),(3,9),(4,5),(4,9),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9))
DIRECTED=tuple((i,j) for e in EDGES for i,j in (e,e[::-1]))
TETS=((0,1,2,8),(0,9,8,2),(0,9,2,3),(0,9,3,4),(0,4,5,7),(0,4,7,9),(0,6,7,5),(0,7,8,9))

def detvol(zz):return sc(F(1,6),dot(vs(zz[1],zz[0]),cross(vs(zz[2],zz[0]),vs(zz[3],zz[0]))))
def tetmom(zz):
    vol=detvol(zz); total=[psum(t[i] for t in zz) for i in range(3)]
    return vol,vm(sc(F(1,4),vol),total)

def main(dest):
    # Generic exact formulas specialized only after their geometric derivation.
    da=sc(F(1,2),mul(sub(one,c),pp)); dr=sc((1-d)/2,q)
    do0=F(b*v,2);do1=F(a*u,2)
    area=sub(p(F(1,2)-do0-do1),add(da,dr))
    bx=sub(p(F(1,6)-(do0*(b+u)+do1*u)/3),sc(F(1,3),add(mul(da,sub(add(p(2),c),pp)),mul(dr,q))))
    by=sub(p(F(1,6)-(do0*v+do1*(v+a))/3),sc(F(1,3),add(mul(da,pp),mul(dr,sub(p(2+d),q)))))
    V=add(sc(F(1,3),mul(area,pw(s,2))),sc(F(1,6),l))
    J=vec(add(add(sc(F(1,4),mul(pw(s,3),bx)),sc(F(1,24),mul(mul(pw(s,2),l),sub(one,sc(2,da))))),sc(F(1,24),pw(l,2))),
          add(add(sc(F(1,4),mul(pw(s,3),by)),sc(F(1,24),mul(mul(pw(s,2),l),sub(one,sc(2,dr))))),sc(F(1,24),pw(l,2))),
          add(add(sc(F(1,12),mul(area,pw(s,2))),sc(F(1,12),l)),sc(F(1,24),pw(l,2))))
    Vf=zero;Jf=[zero,zero,zero];vs_fan=[]
    sample=(F(1,2),)*4
    for ids in TETS:
        vol,jj=tetmom([z[i] for i in ids])
        # The listed fan has a fixed orientation on the genuine interior.
        sign=1 if evaluate(vol,sample)>0 else -1
        vol=sc(sign,vol);jj=vc(sign,jj)
        assert evaluate(vol,sample)>0
        vs_fan.append(vol);Vf=add(Vf,vol);Jf=va(Jf,jj)
    assert Vf==V and Jf==J
    fan_expected=[sc(F(1,8),mul(pw(s,2),mul(sub(one,q),mul(y,sub(one,x))))),
                  sc(F(1,8),mul(s,l)),
                  sc(F(1,8),mul(pw(s,2),mul(sub(one,q),sub(one,y)))),
                  sc(F(1,96),mul(pw(s,2),add(one,sc(8,q)))),
                  sc(F(1,48),pw(s,2)),sc(F(1,24),mul(s,l)),
                  sc(F(1,192),pw(s,2)),sc(F(1,6),pw(l,2))]
    assert vs_fan==fan_expected
    # The 34 incident flags vanish identically and all 56 other supports
    # are strictly inward on the four-dimensional open cube.
    flag_zero=flag_positive=0
    for face in FACES:
        n=cross(vs(z[face[1]],z[face[0]]),vs(z[face[2]],z[face[0]]))
        for j in range(10):
            h=dot(n,vs(z[face[0]],z[j]))
            if j in face:
                assert not h; flag_zero+=1
            else:
                deg=tuple(max(0,degree(h,i)) for i in range(N))
                bb=list(bernstein(h,deg).values())
                assert min(bb)>=0 and max(bb)>0,(face,j)
                flag_positive+=1
    assert (flag_zero,flag_positive)==(34,56)
    # Parent q-cube formulas are recovered identically at l=1/2.
    Vparent=sc(F(1,768),sub(sub(p(95),sc(8,q)),sc(24,mul(x,pp))))
    Jparent=vec(sub(add(sub(sc(F(1,98304),sub(p(2045),sc(128,pw(q,2)))),sc(F(1,64),mul(x,pp))),sc(F(3,1024),mul(pw(x,2),pp))),neg(sc(F(1,256),mul(x,pw(pp,2))))),
                 sub(sc(F(1,98304),add(sub(p(2045),sc(480,q)),sc(128,pw(q,2)))),sc(F(1,256),mul(x,pw(pp,2)))),
                 sc(F(1,3072),sub(sub(p(191),sc(8,q)),sc(24,mul(x,pp)))))
    assert freeze(V,3,F(1,2))==Vparent
    assert [freeze(t,3,F(1,2)) for t in J]==Jparent
    # Uniform nonvanishing volume, exhibited as positive polynomials on the cube.
    area_gap=sc(F(1,8),add(sc(3,mul(sub(one,q),sub(one,mul(x,y)))),sc(2,q)))
    assert area_gap==sub(area,p(F(7,64)))
    vg=add(sc(F(1,3),mul(area_gap,pw(s,2))),mul(l,add(p(F(3,32)),sc(F(7,192),l))))
    assert vg==sub(V,p(F(7,192)))
    vmax=add(sc(F(1,3),mul(sub(p(F(1,2)),area),pw(s,2))),sc(F(1,6),mul(s,l)))
    assert vmax==sub(p(F(1,6)),V)
    # z-centroid remains interior even at both positive-volume endpoints.
    assert sub(J[2],sc(F(1,4),V))==sc(F(1,24),mul(l,add(one,l)))
    assert sub(sc(F(3,4),V),J[2])==add(sc(F(1,6),mul(area,pw(s,2))),sc(F(1,24),mul(s,l)))
    assert freeze(V,3,F(0))==sc(F(1,3),area)
    assert freeze(V,3,F(1))==p(F(1,6))
    assert [freeze(t,3,F(1)) for t in J]==[p(F(1,24)),p(F(1,24)),p(F(1,8))]
    # Complete directed-edge stress basis; no tree/PSD feasibility is presumed.
    e=vec(sc(-(1-b),s),zero,zero)
    f=vec(neg(mul(s,sub(one,q))),mul(s,sub(one,q)),zero)
    k=sc((1-b)/6,mul(pw(s,2),sub(one,q)))
    out=[]
    for i,j in DIRECTED:
        G=mc(-1,sym(vs(vm(V,z[i]),J),vs(z[j],z[i])))
        t1=F(3*(i==1)+(j==1),4);t2=F(3*(i==2)+(j==2),4)
        B1=mm(sc(t1,k),sym(e,e));B2=mm(sc(t2,k),sym(f,f))
        factor1=mul(mul(y,pw(x,2)),sub(one,x))
        factor2=mul(mul(x,pw(y,2)),sub(one,y))
        R=ms(ms(G,mm(factor1,B1)),mm(factor2,B2))
        deg=md(R)
        assert all(v<=bound for v,bound in zip(deg,(2,2,3,4))), (i,j,deg)
        mixed=[[coeff(coeff(t,0,2),1,2) for t in row] for row in G]
        omega=F((i,j) in ((1,2),(2,1)))-F((j==1)-(i==1)+(j==2)-(i==2),4)
        expected=mm(sc(omega,k),sym(e,f))
        assert mixed==expected,(i,j)
        out.append({'edge':[i,j],'degree':deg,'residual':[[serialize(t) for t in row] for row in R]})
    # Exact tensor Bernstein representation and subdivision interpolation.
    # This identity is universal on degree n, not a finite point check of positivity.
    for n in (2,3,4):
        for power in range(n+1):
            rhs=zero
            for kk in range(power,n+1):
                rr=sc(F(math.comb(kk,power)*math.comb(n,kk),math.comb(n,power)),mul(pw(x,kk),pw(sub(one,x),n-kk)))
                rhs=add(rhs,rr)
            assert rhs==pw(x,power)
    report={'theorem':'H5_FOUR_DEFECT_RATIO_MOMENTS_180_BLOCK_REDUCTION_V1',
            'variables':['x','y','q','lambda'],
            'fixed':{'b':'1/4','a':'1/4','d':'3/4','u':'1/16','v':'1/16'},
            'domain':'[0,1]^4; genuine incidence only on (0,1)^4',
            'V_lower':'7/192','V_upper':'1/6','volume':serialize(V),
            'J':[serialize(t) for t in J],'fan_volumes':[serialize(t) for t in vs_fan],
            'edge_count':len(DIRECTED),'bernstein_blocks':180,
            'incidence_zero':flag_zero,'support_interior_positive':flag_positive,
            'residuals':out,
            'scope':'Exact moments/degree reduction only. NO all-root exclusion or feasibility finding.'}
    dest=Path(dest);dest.mkdir(parents=True,exist_ok=True)
    raw=dump(report);fn=dest/'h5_ratio_reduction.json';fn.write_bytes(raw)
    print('H5_FOUR_DEFECT_RATIO_MOMENTS_180_BLOCK_PASS',len(DIRECTED),180)
    print('REPORT_BYTES_SHA256',len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else '.')
