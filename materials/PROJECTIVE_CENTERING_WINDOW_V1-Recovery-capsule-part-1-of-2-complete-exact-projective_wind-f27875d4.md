# material-f27875d4eb6e

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact actual-body controls for PROJECTIVE_CENTERING_WINDOW_V1.
Standard library only; Python 3.13.5 used. No numerical locator or hidden input.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import argparse, hashlib, json

Z = F(0)
I = [[F(i == j) for j in range(3)] for i in range(3)]
def dot(a,b): return sum((x*y for x,y in zip(a,b)), Z)
def add(a,b): return [a[i]+b[i] for i in range(3)]
def sub(a,b): return [a[i]-b[i] for i in range(3)]
def scale(c,a): return [c*x for x in a]
def cross(a,b): return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def det(a): return dot(a[0],cross(a[1],a[2]))
def tr(a): return [list(z) for z in zip(*a)]
def mv(a,x): return [dot(r,x) for r in a]
def mm(a,b): return [[dot(r,c) for c in tr(b)] for r in a]
def outer(a,b): return [[x*y for y in b] for x in a]
def madd(a,b): return [[a[i][j]+b[i][j] for j in range(3)] for i in range(3)]
def msub(a,b): return [[a[i][j]-b[i][j] for j in range(3)] for i in range(3)]
def mscale(c,a): return [[c*x for x in r] for r in a]
def inv(a):
    d=det(a); assert d
    return mscale(1/d,tr([cross(a[1],a[2]),cross(a[2],a[0]),cross(a[0],a[1])]))
def spd(a):
    assert a==tr(a)
    assert a[0][0]>0 and a[0][0]*a[1][1]-a[0][1]**2>0 and det(a)>0

def geometry(points, cycles):
    """Check all actual maximal facets, every strict support, true edges/Euler."""
    q=[]; cc=[]
    for cyc in cycles:
        cyc=list(cyc)
        a,b,c=(points[k] for k in cyc[:3])
        normal=cross(sub(b,a),sub(c,a)); off=dot(normal,a)
        assert off != 0
        if off<0:
            cyc.reverse()
            a,b,c=(points[k] for k in cyc[:3])
            normal=cross(sub(b,a),sub(c,a)); off=dot(normal,a)
        pole=scale(1/off,normal)
        assert all(dot(pole,points[k])==1 for k in cyc)
        assert all(dot(pole,x)<1 for k,x in enumerate(points) if k not in cyc)
        for j in range(len(cyc)):
            aa,bb,dd=(points[cyc[t%len(cyc)]] for t in (j,j+1,j+2))
            assert dot(normal,cross(sub(bb,aa),sub(dd,bb)))>0
        q.append(pole); cc.append(cyc)
    found=set()
    for i,j,k in combinations(range(len(points)),3):
        normal=cross(sub(points[j],points[i]),sub(points[k],points[i]))
        if not any(normal): continue
        vals=[dot(normal,sub(x,points[i])) for x in points]
        if all(s>=0 for s in vals) or all(s<=0 for s in vals):
            found.add(tuple(t for t,s in enumerate(vals) if s==0))
    assert found=={tuple(sorted(c)) for c in cc}
    ef={}
    for f,cyc in enumerate(cc):
        for j in range(len(cyc)):
            edge=tuple(sorted((cyc[j],cyc[(j+1)%len(cyc)])))
            ef.setdefault(edge,[]).append(f)
    assert all(len(ff)==2 for ff in ef.values())
    assert len(points)-len(ef)+len(cc)==2
    assert all(sum(i in e for e in ef)>=3 for i in range(len(points)))
    return q,cc,dict(sorted(ef.items()))

def moments(points,cycles):
    vol=Z; first=[Z]*3; second=[[Z]*3 for _ in range(3)]
    for cyc in cycles:
        for j in range(1,len(cyc)-1):
            a,b,c=(points[k] for k in (cyc[0],cyc[j],cyc[j+1]))
            vv=det([a,b,c])/6; assert vv>0
            ss=add(add(a,b),c)
            vol+=vv; first=add(first,scale(vv/4,ss))
            zz=outer(ss,ss)
            for x in (a,b,c): zz=madd(zz,outer(x,x))
            second=madd(second,mscale(vv/20,zz))
    assert vol>0
    g=scale(1/vol,first); w=mscale(1/vol,second)
    return vol,g,w

def transformed(points,p):
    return [scale(1/(1+dot(p,x)),x) for x in points]

def census(points,cycles,M,own=True):
    q,cc,ef=geometry(points,cycles)
    V,g,W=moments(points,cc)
    ref=g if own else [Z]*3
    x=[sub(v,ref) for v in points]
    poles=[scale(1/(1-dot(a,ref)),a) for a in q]
    N=inv(M); spd(M); spd(N)
    vals=[]; va={i:[] for i in range(len(x))}; fa={i:[] for i in range(len(q))}
    hh=[]; weak=[]
    for (i,j),(a,b) in ef.items():
        u=dot(x[i],mv(M,sub(x[j],x[i])))
        v=dot(x[j],mv(M,sub(x[i],x[j])))
        s=dot(poles[a],mv(N,sub(poles[b],poles[a])))
        t=dot(poles[b],mv(N,sub(poles[a],poles[b])))
        packet=[u,v,s,t]
        va[i].append(u);va[j].append(v);fa[a].append(s);fa[b].append(t)
        vals.extend(packet)
        if all(z<0 for z in packet): hh.append([i,j])
        if all(z<=0 for z in packet) and any(z==0 for z in packet):weak.append([i,j])
    us=[i for i,z in va.items() if max(z)<0]
    ss=[i for i,z in fa.items() if max(z)<0]
    return {'V':V,'g':g,'W':W,'f_vector':[len(x),len(ef),len(q)],
            'S':ss,'U':us,'H':hh,'counts':[len(ss),len(us),len(hh)],
            'weak_edge_packets':weak,'all_primitives_nonzero':all(vals),
            'primitive_signs':[1 if z>0 else -1 if z<0 else 0 for z in vals],
            'min_abs_primitive':min(abs(z) for z in vals)}

def rows(points,cycles,M):
    q,cc,ef=geometry(points,cycles); N=inv(M); out=[]
    for (i,j),(a,b) in ef.items():
        for h,k in ((i,j),(j,i)):
            x,y=points[h],points[k]
            xy=dot(x,mv(M,y)); xx=dot(x,mv(M,x))
            out.append((f'P:{h}>{k}',xy-xx,sub(scale(xy,x),scale(xx,y))))
        for h,k in ((a,b),(b,a)):
            dd=mv(N,sub(q[k],q[h]))
            out.append((f'D:{h}>{k}',dot(q[h],dd),dd))
    return out

def window(points,cycles,M,R,Lbar):
    q,cc,ef=geometry(points,cycles); V,g,W=moments(points,cc); Wi=inv(W)
    L2=max(dot(x,mv(Wi,x)) for x in points)
    e2=dot(g,mv(Wi,g)); assert Lbar**2>=L2 and R*Lbar<1
    outward_gap=(5*R/(1+R*Lbar)**6)**2-e2
    assert outward_gap>0
    margins=[]
    for label,a,b in rows(points,cc,M):
        margin=a*a-R*R*dot(b,mv(Wi,b))
        assert a and margin>0
        margins.append([label,1 if a>0 else -1,margin])
    return {'R':R,'Lbar':Lbar,'L2':L2,'e2':e2,'outward_gap':outward_gap,
            'minimum_squared_row_margin':min(z[2] for z in margins),
            'sign_guards':margins}

def differentiate_g(points,cycles,p):
    """Direct exact derivative of the actual triangulated moments, not finite differences."""
    vv=transformed(points,p); V,g,W=moments(vv,cycles)
    dcols=[]
    for h in range(3):
        dx=[scale(-x[h],x) for x in vv]
        dV=Z; dJ=[Z]*3
        for cyc in cycles:
            for j in range(1,len(cyc)-1):
                ids=(cyc[0],cyc[j],cyc[j+1]); a,b,c=(vv[k] for k in ids)
                da,db,dc=(dx[k] for k in ids)
                vol=det([a,b,c])/6
                dv=(det([da,b,c])+det([a,db,c])+det([a,b,dc]))/6
                ss=add(add(a,b),c);ds=add(add(da,db),dc)
                dV+=dv;dJ=add(dJ,scale(F(1,4),add(scale(dv,ss),scale(vol,ds))))
        dcols.append(scale(1/V,sub(dJ,scale(dV,g))))
    Dg=tr(dcols); Sig=msub(W,outer(g,g)); spd(Sig)
    predicted=msub(mscale(-5,Sig),outer(g,g)); assert Dg==predicted
    d=1-dot(p,g);assert d>0
    r=scale(1/d,g)
    # Direct quotient differentiation and the closed rank-one/covariance identity.
    drcols=[]
    for h in range(3):
        col=[Dg[i][h] for i in range(3)]
        dd=-g[h]-dot(p,col)
        drcols.append(scale(1/d,sub(col,scale(dd,r))))
    Dr=tr(drcols)
    formula=mscale(-5/d,mm(madd(I,outer(r,p)),Sig))
    assert Dr==formula and det(Dr)==-125*det(Sig)/d**4
    return {'p':p,'V':V,'g':g,'covariance':Sig,'r':r,'Dg':Dg,'Dr':Dr,'det_Dr':det(Dr)}

def poly(t): return 1360268*t**3+47133*t**2+6733200*t-20000

def build():
    pts=[[F(x),F(y),F(z)] for x,y,z in product((F(-1),F(101,100)),(-1,1),(-1,1))]
    faces=[[0,1,3,2],[4,6,7,5],[0,4,5,1],[2,3,7,6],[0,2,6,4],[1,5,7,3]]
    q,cc,ef=geometry(pts,faces)
    M=[[F(2),F(1,4),F(1,5)],[F(1,4),F(3,2),F(1,7)],[F(1,5),F(1,7),F(1)]]
    spd(M)
    cert=window(pts,cc,M,F(1,400),F(301,100))
    assert all(z[1]==-1 for z in cert['sign_guards']) and len(cert['sign_guards'])==48
    at0=census(pts,cc,M,own=False); own0=census(pts,cc,M,own=True)
    assert at0['counts']==own0['counts']==[6,8,12]
    # The unique centering parameter is t*e1; it is genuinely irrational.
    assert all((1360268*t**3+47133*t**2+6733200*t-20000)%17 for t in range(17))
    assert 1360268%17
    lo,hi=F(29,10000),F(31,10000)
    assert poly(lo)<0<poly(hi)
    for _ in range(90):
        mid=(lo+hi)/2
        if poly(mid)<0: lo=mid
        else: hi=mid
    assert poly(lo)<0<poly(hi)
    assert hi**2*own0['W'][0][0]<F(1,400)**2
    # A rational nearby body is a separate actual object, centered by its OWN mass.
    mid=(lo+hi)/2
    near=census(transformed(pts,[mid,Z,Z]),cc,M,own=True)
    assert near['counts']==[6,8,12] and near['all_primitives_nonzero'] and not near['weak_edge_packets']
    jac=differentiate_g(pts,cc,[F(1,50),F(-1,100),F(1,150)])
    # Verify all affine-in-p row identities at a nonzero three-parameter point.
    pp=jac['p'];xx=transformed(pts,pp);rr=rows(pts,cc,M);N=inv(M)
    actual=[]
    for (i,j),(a,b) in ef.items():
        actual.append(dot(xx[i],mv(M,sub(xx[j],xx[i]))))
        actual.append(dot(xx[j],mv(M,sub(xx[i],xx[j]))))
        actual.append(dot(add(q[a],pp),mv(N,sub(q[b],q[a]))))
        actual.append(dot(add(q[b],pp),mv(N,sub(q[a],q[b]))))
    for (label,a,b),observed in zip(rr,actual):
        z=a+dot(b,pp)
        if label.startswith('P:'):
            i,j=map(int,label[2:].split('>'))
            z/=((1+dot(pp,pts[i]))**2*(1+dot(pp,pts[j])))
        assert z==observed
    # Wrong-reference and actual-own-COM mechanics really need not agree.
    badp=[F(3,4),Z,Z]; bp=transformed(pts,badp)
    false_reference=census(bp,cc,M,own=False)
    true_reference=census(bp,cc,M,own=True)
    assert false_reference['counts']==[6,7,11]
    assert true_reference['counts']==[5,6,9]
    assert false_reference['all_primitives_nonzero'] and true_reference['all_primitives_nonzero']
    assert not false_reference['weak_edge_packets'] and not true_reference['weak_edge_packets']
    for c in (near,false_reference,true_reference): c.pop('W');c.pop('primitive_signs')
    return {'identity':'PROJECTIVE_CENTERING_WINDOW_V1','points':pts,'facets':cc,'M':M,
            'actual_start':{k:own0[k] for k in ('V','g','W','f_vector','counts')},
            'window_certificate':cert,
            'centering_root':{'ascending_polynomial':[-20000,6733200,47133,1360268],
              'irreducibility_prime':17,'rational_isolation':[lo,hi],
              'rational_midpoint_control':near},
            'centroid_preimage_derivative_control':jac,
            'large_parameter_countercontrol':{'p':badp,'about_fixed_zero':false_reference,'about_own_centroid':true_reference}}

def clean(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [clean(v) for v in x]
    return x

def encoded():return (json.dumps(clean(build()),sort_keys=True,separators=(',',':'))+'\n').encode()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['build','check'])
    ap.add_argument('--output',default='window.json');ap.add_argument('--input',default='window.json');args=ap.parse_args()
    bb=encoded();sha=hashlib.sha256(bb).hexdigest()
    if args.command=='build':
        Path(args.output).write_bytes(bb);print('PROJECTIVE_WINDOW_BUILD_OK',len(bb),sha)
    else:
        assert Path(args.input).read_bytes()==bb
        print('PROJECTIVE_WINDOW_CHECK_OK',len(bb),sha)
if __name__=='__main__':main()
