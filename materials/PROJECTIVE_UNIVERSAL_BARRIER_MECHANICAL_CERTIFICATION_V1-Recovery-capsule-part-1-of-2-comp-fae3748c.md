# material-fae3748c00d7

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Rational universal-barrier centering and actual mechanical certificates.
Standard library only; exact Fractions throughout the proofs' finite controls.
Usage: python projective_barrier.py build --output barrier.json
       python projective_barrier.py check --input barrier.json
The analytic self-concordance premise is Lee--Yue, arXiv:1809.03011v4, Thm 2.
This file does not prove the analytic theorem by sampling or produce class 110.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import argparse
import hashlib
import json
import sys
from math import gcd, lcm


def vec(xs): return tuple(F(x) for x in xs)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def scale(a,x): return tuple(a*b for b in x)
def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def cross(x,y):
    return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def trans(A): return tuple(zip(*A))
def det(A): return dot(A[0],cross(A[1],A[2]))
def mv(A,x): return tuple(dot(a,x) for a in A)
def mm(A,B): return tuple(tuple(dot(a,b) for b in trans(B)) for a in A)
def outer(x,y): return tuple(tuple(a*b for b in y) for a in x)
def mscale(a,A): return tuple(scale(a,x) for x in A)
def madd(A,B): return tuple(add(a,b) for a,b in zip(A,B))
def msub(A,B): return tuple(sub(a,b) for a,b in zip(A,B))
def quad(A,x): return dot(x,mv(A,x))
def inv(A):
    d=det(A)
    if d==0: raise ValueError('Singular matrix')
    return mscale(1/d,trans((cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))))
def pd(A):
    return A==trans(A) and A[0][0]>0 and A[0][0]*A[1][1]-A[0][1]**2>0 and det(A)>0
Z=vec((0,0,0)); ZM=(Z,Z,Z)
I=tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
FACETS=((0,1,3,2),(4,6,7,5),(0,4,5,1),(2,3,7,6),(0,2,6,4),(1,5,7,3))


def validate(vertices, facets):
    fs=[]; poles=[]
    for ids in facets:
        ids=tuple(ids)
        a,b,c=(vertices[i] for i in ids[:3])
        n=cross(sub(b,a),sub(c,a)); h=dot(n,a)
        assert h!=0
        if h<0:
            ids=tuple(reversed(ids))
            a,b,c=(vertices[i] for i in ids[:3])
            n=cross(sub(b,a),sub(c,a)); h=dot(n,a)
        q=scale(1/h,n)
        assert all(dot(q,x)==1 if i in ids else dot(q,x)<1 for i,x in enumerate(vertices))
        for k in range(len(ids)):
            x,y,z=(vertices[ids[(k+j)%len(ids)]] for j in range(3))
            assert dot(n,cross(sub(y,x),sub(z,y)))>0
        fs.append(ids);poles.append(q)
    assert len(set(map(frozenset,fs)))==len(fs)
    actual=set()
    for i,j,k in combinations(range(len(vertices)),3):
        x,y,z=vertices[i],vertices[j],vertices[k]
        n=cross(sub(y,x),sub(z,x))
        if n==Z: continue
        h=dot(n,x); ds=[dot(n,v)-h for v in vertices]
        if all(t<=0 for t in ds) or all(t>=0 for t in ds):
            actual.add(frozenset(i for i,t in enumerate(ds) if t==0))
    assert actual==set(map(frozenset,fs))
    edges={}
    for f,ids in enumerate(fs):
        for i,j in zip(ids,ids[1:]+ids[:1]):
            edges.setdefault(tuple(sorted((i,j))),[]).append(f)
    assert all(len(v)==2 for v in edges.values())
    assert len(vertices)-len(edges)+len(fs)==2
    assert all(sum(i in e for e in edges)>=3 for i in range(len(vertices)))
    return tuple(fs),tuple(poles),tuple((e,tuple(edges[e])) for e in sorted(edges))


def moments(vertices, facets, velocities=None):
    V=F(0);J=Z; Q=ZM;dV=F(0);dJ=Z
    for ids in facets:
        for k in range(1,len(ids)-1):
            ii=(ids[0],ids[k],ids[k+1]);a,b,c=(vertices[i] for i in ii)
            v=dot(a,cross(b,c))/6
            assert v>0
            s=add(add(a,b),c)
            V+=v;J=add(J,scale(v/4,s))
            Q=madd(Q,mscale(v/20,madd(outer(s,s),madd(outer(a,a),madd(outer(b,b),outer(c,c))))))
            if velocities is not None:
                da,db,dc=(velocities[i] for i in ii)
                dv=(dot(da,cross(b,c))+dot(a,cross(db,c))+dot(a,cross(b,dc)))/6
                dV+=dv;dJ=add(dJ,add(scale(dv/4,s),scale(v/4,add(add(da,db),dc))))
    g=scale(1/V,J);W=mscale(1/V,Q)
    result=(V,g,W)
    if velocities is None: return result
    return result,(dV,scale(1/V,sub(dJ,scale(dV,g))))


def box(a): return tuple((x,y,z) for x,y,z in product((F(-1),F(a)),(F(-1),F(1)),(F(-1),F(1))))

def project(vertices, facets, p):
    ff=tuple(1+dot(p,x) for x in vertices)
    assert min(ff)>0
    y=tuple(scale(1/f,x) for x,f in zip(vertices,ff))
    fs,qq,ee=validate(y,facets)
    return y,fs,qq,ee


def rows(vertices,poles,edges,M):
    assert pd(M);N=inv(M);rr=[]
    for (i,j),(f,h) in edges:
        for a,b in ((i,j),(j,i)):
            x,y=vertices[a],vertices[b]
            rr.append(('V',a,b,dot(x,mv(M,sub(y,x))),sub(scale(dot(x,mv(M,y)),x),scale(quad(M,x),y))))
        for a,b in ((f,h),(h,f)):
            d=sub(poles[b],poles[a])
            rr.append(('F',a,b,dot(poles[a],mv(N,d)),mv(N,d)))
    return tuple(rr)


def census(vertices,poles,edges,M,center=Z):
    x=tuple(sub(v,center) for v in vertices)
    ds=tuple(1-dot(a,center) for a in poles)
    assert min(ds)>0
    q=tuple(scale(1/d,a) for a,d in zip(poles,ds));N=inv(M)
    ve=[[] for _ in x];fe=[[] for _ in q];hs=[];weak=[];values=[]
    for (i,j),(f,h) in edges:
        vv=(dot(x[i],mv(M,sub(x[j],x[i]))),dot(x[j],mv(M,sub(x[i],x[j]))),
            dot(q[f],mv(N,sub(q[h],q[f]))),dot(q[h],mv(N,sub(q[f],q[h]))))
        ve[i].append(vv[0]);ve[j].append(vv[1]);fe[f].append(vv[2]);fe[h].append(vv[3]);values.extend(vv)
        if max(vv)<0:hs.append((i,j))
        if max(vv)==0:weak.append((i,j))
    S=[i for i,v in enumerate(fe) if max(v)<0];U=[i for i,v in enumerate(ve) if max(v)<0]
    return {'SUH':[len(S),len(U),len(hs)],'S':S,'U':U,'H':hs,'weak_edges':weak,
            'zero_primitives':sum(v==0 for v in values),'signs':[1 if v>0 else -1 if v<0 else 0 for v in values]}


def barrier_state(vertices,facets,p):
    y,fs,qs,es=project(vertices,facets,p)
    V,g,W=moments(y,fs);Sigma=msub(W,outer(g,g));H=msub(mscale(20,W),mscale(16,outer(g,g)))
    assert pd(Sigma) and pd(H)
    Hi=inv(H);lambda2=16*quad(Hi,g)
    assert 0<=lambda2<=3
    return {'vertices':y,'facets':fs,'poles':qs,'edges':es,'V':V,'g':g,'W':W,'Sigma':Sigma,'H':H,'Hi':Hi,'lambda2':lambda2}


def mechanical_window(rr,p,H,lambda2,ell=None):
    if lambda2==0:
        ell=F(0)
    elif ell is None:
        if lambda2>F(1,4): return None
        ell=F(1,2)
        while lambda2<=(ell/2)**2:ell/=2
    ell=F(ell)
    assert 0<=ell<1 and lambda2<=ell**2
    R=ell/(1-ell);Hi=inv(H)
    margins=[];signs=[];norms=[]
    for kind,i,j,a,b in rr:
        aa=a+dot(b,p);nn=quad(Hi,b)
        margins.append(aa*aa-R*R*nn);norms.append(nn)
        signs.append(1 if aa>0 else -1 if aa<0 else 0)
    return {'ell':ell,'R':R,'margins':tuple(margins),'row_dual_norm_squares':tuple(norms),
            'signs':signs,'passes':min(margins)>0 and 0 not in signs,'minimum_margin':min(margins)}


def rounded_quarter_step(p,H,Hi,g,lambda2):
    assert lambda2>0
    target=add(p,mv(Hi,g))
    # Least dyadic precision whose ACTUAL H-norm error passes the rational test.
    bits=0
    while True:
        den=1<<bits
        q=tuple(F((v*den).numerator//(v*den).denominator,den) for v in target)
        error=sub(q,target);error2=quad(H,error)
        if error2<=lambda2/4096:break
        bits+=1
    step=sub(q,p);step2=quad(H,step)
    assert step2<1 and -4*dot(g,step)<0
    return q,{'bits':bits,'rounding_error_squared':error2,'allowed_error_squared':lambda2/4096,
              'step_norm_squared':step2,'linear_barrier_change':-4*dot(g,step)}


def local_control():
    vertices=box(F(3,2));fs,qs,es=validate(vertices,FACETS)
    s=barrier_state(vertices,fs,Z);rr=rows(vertices,qs,es,I)
    window=mechanical_window(rr,Z,s['H'],s['lambda2'],F(5,16))
    assert s['V']==10 and s['g']==vec((F(1,4),0,0))
    assert s['W']==(vec((F(7,12),0,0)),vec((0,F(1,3),0)),vec((0,0,F(1,3))))
    assert s['H']==(vec((F(32,3),0,0)),vec((0,F(20,3),0)),vec((0,0,F(20,3))))
    assert s['lambda2']==F(3,32) and window['R']==F(5,11) and window['passes']
    assert set(window['signs'])=={-1} and len(rr)==48
    Wi=inv(s['W']);e2=quad(Wi,s['g']);L2=max(quad(Wi,x) for x in vertices)
    old_gap=e2*L2-F(5,6)**12
    assert old_gap>0 # Rules out EVERY old radius R and EVERY permissible Lupper.
    cen=census(vertices,qs,es,I,s['g'])
    assert cen['SUH']==[6,8,12] and not cen['weak_edges'] and cen['zero_primitives']==0
    return {'a':F(3,2),'vertices':vertices,'facets':fs,'edges':es,'M':I,'N':I,
            'V':s['V'],'g':s['g'],'W':s['W'],'H':s['H'],'lambda2':s['lambda2'],
            'e2':e2,'L2':L2,'old_all_radius_failure_gap':old_gap,'new_window':window,
            'raw_own_COM_census':cen,'certified_centered_SUH':[6,8,12],'certified_centered_weak':0}


def global_control(a,p0,max_steps=100):
    vertices=box(a);fs,qs,es=validate(vertices,FACETS);rr=rows(vertices,qs,es,I)
    p=vec(p0);steps=[];initial=barrier_state(vertices,fs,p)
    initial_ref=census(initial['vertices'],initial['poles'],initial['edges'],I)
    initial_own=census(initial['vertices'],initial['poles'],initial['edges'],I,initial['g'])
    assert initial['lambda2']>1
    for iteration in range(max_steps+1):
        s=barrier_state(vertices,fs,p);w=mechanical_window(rr,p,s['H'],s['lambda2'])
        if w is not None and w['passes']:
            end_ref=census(s['vertices'],s['poles'],s['edges'],I)
            end_own=census(s['vertices'],s['poles'],s['edges'],I,s['g'])
            assert end_ref['signs']==w['signs'] and end_ref['SUH']==[6,8,12]
            assert end_own['SUH']==[6,8,12] and end_own['zero_primitives']==0 and not end_own['weak_edges']
            return {'a':F(a),'p0':vec(p0),'initial_lambda2':initial['lambda2'],
                    'initial_reference_census':initial_ref,'initial_own_COM_census':initial_own,
                    'steps':steps,'terminal_p':p,'terminal_V':s['V'],'terminal_g':s['g'],
                    'terminal_H':s['H'],'terminal_lambda2':s['lambda2'],'terminal_window':w,
                    'terminal_reference_census':end_ref,'terminal_rational_own_COM_census':end_own,
                    'certified_exact_centered_SUH':[6,8,12],'certified_exact_centered_weak':0}
        assert iteration<max_steps,'Control did not reach its strict-row certificate'
        q,rec=rounded_quarter_step(p,s['H'],s['Hi'],s['g'],s['lambda2'])
        ss=barrier_state(vertices,fs,q)
        rational_decrease=s['V']-ss['V']*(1+s['lambda2']/6)
        assert rational_decrease>0
        rec.update({'iteration':iteration,'p':p,'next_p':q,'V':s['V'],'lambda2':s['lambda2'],
                    'volume_ratio':ss['V']/s['V'],'rational_decrease_margin':rational_decrease})
        steps.append(rec);p=q
    raise AssertionError('Unreachable')


def identities_control():
    vertices=box(F(3,2));fs,qs,es=validate(vertices,FACETS)
    p=vec((F(1,5),F(-1,20),F(1,30)))
    M=(vec((2,F(1,4),F(1,5))),vec((F(1,4),F(3,2),F(1,7))),vec((F(1,5),F(1,7),1)))
    s=barrier_state(vertices,fs,p);y=s['vertices'];cols=[]
    for k in range(3):
        dy=tuple(scale(-v[k],v) for v in y)
        _,(dv,dg)=moments(y,s['facets'],dy)
        assert dv==-4*s['V']*s['g'][k]
        cols.append(scale(-4,dg))
    assert trans(tuple(cols))==s['H']
    original=rows(vertices,qs,es,M);new=rows(y,s['poles'],s['edges'],M)
    for (kind,i,j,a,b),(kk,ii,jj,aa,bb) in zip(original,new):
        assert (kind,i,j)==(kk,ii,jj)
        divisor=(1+dot(p,vertices[i]))**2*(1+dot(p,vertices[j])) if kind=='V' else F(1)
        assert aa==(a+dot(b,p))/divisor and bb==scale(1/divisor,b)
    # Explicit polar incidences for (D-p)^o = -T_p K.
    Dshift=tuple(scale(-1,add(q,p)) for q in qs)
    polar_vertices=tuple(scale(-1,v) for v in y)
    for i,v in enumerate(polar_vertices):
        assert all(dot(v,q)==1 if i in fs[f] else dot(v,q)<1 for f,q in enumerate(Dshift))
    Wi=inv(s['W']);e2=quad(Wi,s['g'])
    assert s['lambda2']==4*e2/(5-4*e2)
    return {'p':p,'M':M,'N':inv(M),'V':s['V'],'g':s['g'],'H':s['H'],'lambda2':s['lambda2'],
            'e2':e2,'differentiated_actual_moments_match_H':True,
            'all_48_original_and_rebased_rows_match':True,'polar_identity_full_incidences':True}


def axial_exact_center(a,lo,hi):
    a=F(a);lo=F(lo);hi=F(hi);d=a-1;c=a*a-a+1
    coeff=(-6*d,20*a-4*d*d,d*(15*a-c),4*a*c)
    den=lcm(*(v.denominator for v in coeff))
    integers=[int(v*den) for v in coeff]
    content=gcd(*integers);integers=[v//content for v in integers]
    def polynomial(t):return sum((F(v)*t**j for j,v in enumerate(integers)),F(0))
    assert F(-1,a)<lo<hi<1 and polynomial(lo)<0<polynomial(hi)
    modulus=next(p for p in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47)
                 if integers[-1]%p and all(sum(v*k**j for j,v in enumerate(integers))%p for k in range(p)))
    vertices=box(a);fs,qs,es=validate(vertices,FACETS)
    # Positive-refill fan differentiation checks the closed axial volume formula.
    test=F(1,50);s=barrier_state(vertices,fs,(test,F(0),F(0)))
    U=(1-test)*(1+a*test);N=3+3*d*test+c*test**2
    assert s['V']==4*(a+1)*N/(3*U**3)
    pp=sum((v*test**j for j,v in enumerate(coeff)),F(0))
    assert -4*s['V']*s['g'][0]==4*(a+1)*pp/(3*U**4)
    for _ in range(80):
        mid=(lo+hi)/2
        if polynomial(mid)<0:lo=mid
        else:hi=mid
    assert polynomial(lo)<0<polynomial(hi)
    mid=(lo+hi)/2;s=barrier_state(vertices,fs,(mid,F(0),F(0)))
    own=census(s['vertices'],s['poles'],s['edges'],I,s['g'])
    assert own['SUH']==[6,8,12] and not own['weak_edges'] and own['zero_primitives']==0
    return {'a':a,'primitive_polynomial_ascending':integers,'irreducible_modulus':modulus,
            'root_interval':[lo,hi],'bisections':80,'exact_centered_parameter':'(unique root in interval,0,0)',
            'different_rational_midpoint_body':{'p':(mid,F(0),F(0)),'V':s['V'],'own_g':s['g'],'own_census':own},
            'exact_axial_volume_and_gradient_identity_control':True}


def data():
    local=local_control();identities=identities_control()
    global_a=global_control(F(3,2),(F(4,5),F(1,100),F(-1,200)))
    global_b=global_control(F(10),(F(-9,100),F(1,100),F(-1,200)))
    assert global_a['initial_reference_census']['SUH']!=global_a['certified_exact_centered_SUH']
    return {'identity':'PROJECTIVE_UNIVERSAL_BARRIER_MECHANICAL_CERTIFICATION_V1',
            'analytic_source':{'author':'Yin Tat Lee and Man-Chung Yue','arxiv':'1809.03011v4','theorem':2},
            'controls_are_NOT_110':True,'local_stronger_window':local,'exact_identities':identities,
            'exact_centered_objects':[axial_exact_center(F(3,2),F(9,100),F(1,10)),
                                      axial_exact_center(F(10),F(1,5),F(1,3))],
            'global_rounded_quarter_newton':[global_a,global_b],
            'fixed_parameters':{'rounding_error_factor_squared':F(1,4096),'step_fraction':F(1,4),
                                'proved_barrier_decrease_coefficient':F(1,6),'maximum_control_steps':100}}


def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def output_bytes():return (json.dumps(encode(data()),sort_keys=True,separators=(',',':'))+'\n').encode()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('mode',choices=('build','check'))
    p.add_argument('--output',default='barrier.json');p.add_argument('--input',default='barrier.json')
    args=p.parse_args();raw=output_bytes()
    if args.mode=='build':Path(args.output).write_bytes(raw)
    else:assert Path(args.input).read_bytes()==raw,'Output differs from complete exact reconstruction'
    print('PROJECTIVE_BARRIER_'+args.mode.upper()+'_OK',len(raw),hashlib.sha256(raw).hexdigest())
    print('PROJECTIVE_UNIVERSAL_BARRIER_MECHANICAL_CERTIFICATION_PASS')

if __name__=='__main__':main()
