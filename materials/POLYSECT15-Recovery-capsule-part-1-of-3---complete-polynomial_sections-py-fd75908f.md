# material-fd75908f4473

AI research material

---

"""POLYSECT15 exact rational analytic body and optional finite controls.
Core verification: Python3.13.5 standard library only.
Optional finite audit: exact circle_family.py dependency from CIRCLE5 capsule;
NumPy2.3.5, SciPy1.17.0. No randomness, quadrature, optimization or rounding here.
Run python polynomial_sections.py --out polysect15
Optional: add --sample-m 5 (eight literal circle directions, all fixed-world).
"""
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction as Q
from pathlib import Path

def trim(p):
    p=list(map(Q,p))
    while len(p)>1 and not p[-1]: p.pop()
    return tuple(p)
def add(a,b): return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def neg(a): return trim([-v for v in a])
def sub(a,b): return add(a,neg(b))
def scale(a,s): return trim([Q(s)*v for v in a])
def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def power(a,n):
    c=(Q(1),)
    for _ in range(n): c=mul(c,a)
    return c
def derivative(a): return trim([i*a[i] for i in range(1,len(a))] or [Q(0)])
def evaluate(a,x):
    c=Q(0)
    for y in a[::-1]: c=c*x+y
    return c
def bernstein(p):
    n=len(p)-1
    return tuple(sum(p[j]*Q(math.comb(i,j),math.comb(n,j)) for j in range(i+1)) for i in range(n+1))
def split(b):
    layers=[list(b)]
    while len(layers[-1])>1:
        layers.append([(x+y)/2 for x,y in zip(layers[-1],layers[-1][1:])])
    return tuple(v[0] for v in layers),tuple(v[-1] for v in layers[::-1])
def positive_certificate(p,max_depth=40):
    leaves=[]; stack=[(Q(0),Q(1),bernstein(p),0)]
    while stack:
        l,r,b,d=stack.pop()
        if min(b)>0:
            leaves.append({'left':str(l),'right':str(r),'minimum_bernstein':str(min(b)),'coefficients':[str(v) for v in b]})
        elif max(b)<=0: raise ArithmeticError(f'nonpositive polynomial interval {l},{r}')
        elif d>=max_depth: raise ArithmeticError(f'unresolved interval {l},{r} at depth {d}')
        else:
            u,v=split(b); m=(l+r)/2
            stack.append((m,r,v,d+1)); stack.append((l,m,u,d+1))
    assert leaves[0]['left']=='0' and leaves[-1]['right']=='1'
    assert all(a['right']==b['left'] for a,b in zip(leaves,leaves[1:]))
    return {'power_coefficients':[str(v) for v in p],'degree':len(p)-1,'leaves':leaves,
        'global_positive_lower_bound':str(min(Q(t['minimum_bernstein']) for t in leaves))}

P=scale((1,Q(-43,6),Q(91,18)),Q(1,15))
QPOLY=scale((Q(39,10),Q(-70,9),Q(5,3)),Q(1,15))
Y=(Q(0),Q(1)); ONE=(Q(1),); O=(Q(1),Q(-1))

def proof():
    # p(x)=P(x^2), q(x)=x QPOLY(x^2). The exact normalized transverse
    # first moment is sum P_j / ((2j+1)(2j+3)); the omitted factor is4*pi.
    moment=sum(c/Q((2*j+1)*(2*j+3)) for j,c in enumerate(P)); assert moment==0
    D=add(mul(P,P),mul(Y,mul(QPOLY,QPOLY)))
    DD=derivative(D); T=sub(D,mul(O,DD)); R=mul(O,D)
    W=sub(mul(T,T),mul(R,mul(DD,DD)))
    N=add(scale(derivative(P),2),scale(mul(Y,derivative(derivative(P))),4))
    L=add(scale(derivative(QPOLY),6),scale(mul(Y,derivative(derivative(QPOLY))),4))
    K=sub(ONE,mul(power(O,3),add(mul(N,N),mul(Y,mul(L,L)))))
    certificates={name:positive_certificate(poly) for name,poly in [('D',D),('T',T),('W',W),('K',K)]}
    assert evaluate(P,0)==Q(1,15)
    assert evaluate(P,1)==Q(-2,27) and evaluate(QPOLY,1)==Q(-199,1350)
    return {'identity':'POLYSECT15_V1','P':[str(c) for c in P],'Q':[str(c) for c in QPOLY],
        'moment_without_4pi':str(moment),'volume':'4*pi/3','filled_centroid':['0','0','0'],
        'unstable':['0','16/15','0'],'stable':['0','-14/15','0'],
        'radial_min':'14/15','radial_max':'16/15','radial_ratio':'7/8',
        'positive_polynomials':certificates,
        'scope':'Analytic C-infinity strictly convex body, exactly one nondegenerate S and U. NOT a polyhedron; no finite C assigned.'}

def point(t,u):
    t=Q(t); u=tuple(map(Q,u)); assert -1<=t<=1 and sum(c*c for c in u)==1
    x=2*t/(1+t*t); rho=(1-t*t)/(1+t*t)
    return (x,evaluate(P,x*x)+rho*u[0],x*evaluate(QPOLY,x*x)+rho*u[1])
def tangent(p):
    x,y,z=map(Q,p); dy=y-evaluate(P,x*x); dz=z-x*evaluate(QPOLY,x*x)
    assert x*x+dy*dy+dz*dz==1
    pp=2*x*evaluate(derivative(P),x*x)
    qq=evaluate(QPOLY,x*x)+2*x*x*evaluate(derivative(QPOLY),x*x)
    n=(x-dy*pp-dz*qq,dy,dz)
    return n,sum(a*b for a,b in zip(n,p))
def samples(m):
    if m<2: raise ValueError('m must be >=2')
    directions=[(1,0),(Q(3,5),Q(4,5)),(0,1),(Q(-3,5),Q(4,5)),(-1,0),(Q(-3,5),Q(-4,5)),(0,-1),(Q(3,5),Q(-4,5))]
    pts=[]
    for j in range(-m,m+1):
        for u in (directions if abs(j)<m else [(1,0)]): pts.append(point(Q(j,m),u))
    return sorted(set(pts))
def serialize(x):
    if isinstance(x,Q): return str(x)
    if isinstance(x,(list,tuple)): return [serialize(v) for v in x]
    if isinstance(x,dict): return {str(k):serialize(v) for k,v in x.items()}
    return x

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--out',default='polysect15');pa.add_argument('--sample-m',type=int);args=pa.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    report=proof(); (out/'analytic_certificate.json').write_text(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n')
    for name,cert in report['positive_polynomials'].items(): print(name,cert['degree'],len(cert['leaves']),cert['global_positive_lower_bound'])
    print('POLYSECT15_ANALYTIC_EXACT_PASS')
    if args.sample_m is not None:
        from circle_family import census
        pts=samples(args.sample_m)
        for p in pts:
            n,h=tangent(p); assert all(sum(a*b for a,b in zip(n,q))<=h for q in pts)
        body=census(pts,landscape=True)
        data={'identity':f'POLYSECT15_FIXED_M{args.sample_m}', 'm':args.sample_m,'points':pts}
        (out/'finite_input.json').write_text(json.dumps(serialize(data),sort_keys=True,separators=(',',':'))+'\n')
        (out/'finite_audit.json').write_text(json.dumps(serialize(body),sort_keys=True,separators=(',',':'))+'\n')
        for key in ['V','E','F','C','strict','additional_weak','primitive_zeros','centroid']:print(key,body[key])
        print('POLYSECT15_FINITE_EXACT_PASS')
    for p in sorted(out.glob('*.json')):print(p.name,len(p.read_bytes()),hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
