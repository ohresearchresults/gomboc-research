# material-46d7b0169c0a

AI research material

---

#!/usr/bin/env python3
"""Whole rational horizon path, exact coefficient domination. Requires SymPy.
Run: python -B cut_stack_horizon_interval.py
Reads only the complete sibling cut_stack_regular_horizon.py source.
The output records each rational guard and its exact interval sign certificate.
"""
from fractions import Fraction as F
import json
import sympy as sp
import cut_stack_regular_horizon as core

s=sp.Symbol('s')
R=sp.Rational

def rat(v):return R(v.numerator,v.denominator)
def cancel(x):return sp.cancel(x)
def vec(v):return tuple(rat(x) for x in v)
def clean(v):return tuple(cancel(x) for x in v)
def cmat(M):return tuple(clean(row) for row in M)

beta=rat(core.BETA); f=vec(core.FCUT); t=rat(core.STACK); w=vec(core.WEIGHTS); A=rat(core.LEFT_SCALE); c=vec(core.CWIDTH)
b=((0,-beta,0),(0,1-beta,0),(0,0,1)); r=s*A
p=sp.prod(f); q=sp.prod(1-s*x for x in c)
dl=1-(1-t)*p;D=cancel(r*dl+(1-r)*(1-q));delta=cancel(D/s)
assert cancel(A*dl+sum(c)-1)==0
bm=(-r,0,0);bp=(1-r,0,0)
l=tuple((-r*(1-z),z*v[1],z*v[2]) for z,v in zip(f,b))
n=tuple(((1-r)*s*z,(1-s*z)*v[1],(1-s*z)*v[2]) for z,v in zip(c,b))
u=core.add(core.scale(t,bm),core.scale(1-t,tuple(sum(w[j]*l[j][k] for j in range(3)) for k in range(3))))
raw=b+l+n+(u,)
V=tuple((cancel(v[0]/D),v[1],v[2]) for v in raw)

def vsum(rows):return tuple(sum(v[k] for v in rows) for k in range(3))
# Actual signed tetrahedral first moment numerator, with six-volume coefficients.
units=((r,(bm,)+b),(1-r,(bp,)+b),(-r*p,(bm,)+l),(-(1-r)*q,(bp,)+n),(r*t*p,l+(u,)))
J=clean(tuple(sum(co*vsum(tet)[k] for co,tet in units) for k in range(3)))
g=(cancel(J[0]/(4*D*D)),cancel(J[1]/(4*D)),cancel(J[2]/(4*D)))
assert tuple(x.subs(s,0) for x in g)==tuple(rat(x) for x in core.certify(F(0))['centroid'])
X=tuple(clean(core.sub(v,g)) for v in V)
M=tuple(vec(row) for row in core.METRIC); N=tuple(vec(row) for row in core.inverse(core.METRIC))
checks=[('delta',delta,1)];poles=[];incidence={};fanD=0;fanJ=(0,0,0)
for fi,cy in enumerate(core.CYCLES):
    va,vb,vc=(V[i] for i in cy[:3]); normal=clean(core.cross(core.sub(vb,va),core.sub(vc,va)));h=cancel(core.dot(normal,va))
    for i,v in enumerate(V):
        expr=cancel(h-core.dot(normal,v))
        if i in cy:assert expr==0
        else:checks.append((f'support_{fi}_{i}',expr,1))
    for j in range(len(cy)):
        i,k,lidx=cy[j],cy[(j+1)%len(cy)],cy[(j+2)%len(cy)]
        turn=cancel(core.dot(core.cross(core.sub(V[k],V[i]),core.sub(V[lidx],V[k])),normal))
        checks.append((f'turn_{fi}_{i}',turn,1))
        incidence.setdefault(tuple(sorted((i,k))),[]).append(fi)
    for j in range(1,len(cy)-1):
        a0,b0,c0=V[cy[0]],V[cy[j]],V[cy[j+1]]
        d0=cancel(core.dot(a0,core.cross(b0,c0)));sum0=core.add(core.add(a0,b0),c0)
        fanD+=d0;fanJ=core.add(fanJ,core.scale(d0,sum0))
    hc=cancel(h-core.dot(normal,g));checks.append((f'centred_support_{fi}',hc,1))
    poles.append(clean(core.scale(1/hc,normal)))
assert cancel(fanD-1)==0
assert all(cancel(fanJ[k]-4*g[k])==0 for k in range(3))
for (i,j),(f0,h0) in sorted(incidence.items()):
    for a,b0 in ((i,j),(j,i)):
        expr=cancel(core.dot(X[a],core.mv(M,core.sub(X[b0],X[a]))))
        sign=sp.sign(expr.subs(s,0));assert sign in (-1,1)
        checks.append((f'VE_{a}_{b0}',expr,int(sign)))
    for a,b0 in ((f0,h0),(h0,f0)):
        expr=cancel(core.dot(poles[a],core.mv(N,core.sub(poles[b0],poles[a]))))
        sign=sp.sign(expr.subs(s,0));assert sign in (-1,1)
        checks.append((f'EF_{a}_{b0}',expr,int(sign)))
assert len(checks)==168


def coefficients(poly):
    p=sp.Poly(poly,s,domain=sp.QQ)
    assert not p.is_zero
    return [p.nth(i) for i in range(p.degree()+1)]


def sign_certificate(co, radius):
    c0=co[0];assert c0!=0
    tail=sum(abs(x)*radius**i for i,x in enumerate(co[1:],1))
    gap=abs(c0)-tail
    return gap

prepared=[]
for name,expr,desired in checks:
    num,den=sp.fraction(expr);aa,bb=coefficients(num),coefficients(den)
    assert sp.sign(aa[0])*sp.sign(bb[0])==desired
    prepared.append((name,desired,aa,bb))
# An exact acceptance loop, not sampled interval feasibility.
radius=R(1,16)
while not all(sign_certificate(a,radius)>0 and sign_certificate(b,radius)>0 for _,_,a,b in prepared):
    radius/=2
    if radius<R(1,2**30):raise RuntimeError('No accepted interval within the prescribed exact bound')
rows=[]
for name,desired,a,b in prepared:
    rows.append({'name':name,'sign':desired,'numerator_coefficients':[str(x) for x in a],
      'denominator_coefficients':[str(x) for x in b],
      'numerator_gap':str(sign_certificate(a,radius)),'denominator_gap':str(sign_certificate(b,radius))})
ref=core.certify(F(0))
report={'identity':'CUT_STACK_ELEVEN_MODULI_REGULAR_RIGHT_HORIZON_V1','sympy_version':sp.__version__,
        'interval':['0',str(radius)],'actual_volume':'1/6','actual_centroid':[str(x) for x in g],
        'S':ref['S'],'U':ref['U'],'H':ref['H'],'weak':'000','guard_count':len(rows),
        'max_numerator_degree':max(len(a)-1 for _,_,a,b in prepared),
        'max_denominator_degree':max(len(b)-1 for _,_,a,b in prepared),
        'checks':rows,'marker':'CUT_STACK_REGULAR_HORIZON_WHOLE_PATH_EXACT_PASS'}
print(json.dumps(report,sort_keys=True,indent=2))
