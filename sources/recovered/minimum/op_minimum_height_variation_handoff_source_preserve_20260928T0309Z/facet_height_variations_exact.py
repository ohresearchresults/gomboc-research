"""Actual whole-facet height variations and an exact ridge countercontrol.
Python 3.13.5 / SymPy 1.14.0. No input files, seeds, numerical decisions or
checkpoints. Run with assertions enabled: python -B facet_height_variations_exact.py
The accompanying analytical proof supplies admissibility and global scope.
"""
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

Q=s.Rational
rt=s.sqrt(6)
def eq(a,b=0):
    assert s.cancel(s.expand(a-b))==0

def canon(a):
    return s.expand(s.radsimp(a))

def positive(a):
    """Exact sign in Q(sqrt(6)); no floating-point comparisons."""
    a=canon(a); b=a.coeff(rt); c=s.expand(a-b*rt)
    assert b.is_Rational and c.is_Rational
    if b==0:return bool(c>0)
    if c==0:return bool(b>0)
    if b>0 and c>0:return True
    if b<0 and c<0:return False
    return bool(6*b*b>c*c) if b>0 else bool(c*c>6*b*b)

r,u=s.symbols('r u',real=True)
S,T,U,K,V,J,I,B0,B1,B2,E0,E1,E2,tv,yv=s.symbols('S T U K V J I B0 B1 B2 E0 E1 E2 tv yv',nonzero=True)
eta=B1/B2
# Layer-cake over v+(1-r)(K-v), including its two-dimensional Jacobian.
M0=s.integrate((1-r)**2*S,(r,0,1))
Mt=s.integrate((1-r)**2*((1-r)*T+r*S*tv),(r,0,1))
My=s.integrate((1-r)**2*((1-r)*U+r*S*yv),(r,0,1))
M2=s.integrate((1-r)**2*((1-r)**2*K+2*r*(1-r)*U*yv+r*r*S*yv*yv),(r,0,1))
eq(M0,S/3);eq(Mt,T/4+S*tv/12);eq(My,U/4+S*yv/12)
eq(M2,K/5+U*yv/10+S*yv*yv/30)
H=s.expand(Mt/J-M0/V-M2/I-2*eta*My/V)
Phi=tv/J-1/V-yv*yv/I-2*eta*yv/V
D0=T/J-S/V-K/I-2*eta*U/V+E2/B2
identity=(K-2*U*yv+S*yv*yv)/(20*I)-E2/(4*B2)+S*Phi/12+D0/4
eq(H,identity)
f=J/V+(J/I)*yv*yv+(2*J*eta/V)*yv
eq(s.diff(H.subs(tv,f),yv,2),S/(10*I))
# A marked-edge apex has a one-dimensional tent trace.
Ce2=s.integrate((1-r)*((1-r)**2*E2+2*r*(1-r)*E1*yv+r*r*E0*yv*yv),(r,0,1))
eq(Ce2,E2/4+E1*yv/6+E0*yv*yv/12)
# Direct differentiation includes the ACTUAL moving centroid.
e,m0,mt,my,m2,c0,c1,c2=s.symbols('e m0 mt my m2 c0 c1 c2')
Ve=V+e*m0;Je=J+e*mt;ge=e*my/Ve
Ie=I+e*m2-e*e*my*my/Ve
Be=B2+e*c2-2*ge*(B1+e*c1)+ge*ge*(B0+e*c0)
Re=Je*Be/(Ve*Ie)
D=s.diff(Re,e).subs(e,0)/(J*B2/(V*I))
eq(D,mt/J-m0/V-m2/I-2*B1*my/(V*B2)+c2/B2)
# Weighted line rotations, with density values l0,l1 at the two endpoints.
l0,l1,d,A=s.symbols('l0 l1 d A',positive=True)
ld=l0+(l1-l0)*u
rot=s.factor(s.integrate(u*u*(1-u)*ld,(u,0,1))/s.integrate(u*(1-u)*ld,(u,0,1)))
eq(rot,(2*l0+3*l1)/(5*(l0+l1)))
line=(1-u)*(-rot+u)
weighted=s.factor(s.integrate(ld*line,(u,0,1)))
eq(weighted,-(3*l0*l0+6*l0*l1+l1*l1)/(60*(l0+l1)))
# After the true marked-endpoint stationarity equation, the leading inward
# graph-height hinge test on this flat side has this nonnegative square gap.
unweighted=s.integrate(line,(u,0,1))
flat_gap=s.factor(unweighted-weighted/l0)
eq(flat_gap,(l0-l1)**2/(60*l0*(l0+l1)))

# Exact actual control. K has vertices (0,-1),(0,1),(1,0), density 1+a*t+k*y.
# Its normal marginal is 2*(1-t)*(1+a*t), independent of k in [-1,1].
a,t,q=s.symbols('a t q',real=True)
vol=s.integrate(2*(1-t)*(1+a*t),(t,0,1))
first=s.integrate(2*t*(1-t)*(1+a*t),(t,0,1))
second=s.integrate(2*t*t*(1-t)*(1+a*t),(t,0,1))
h=s.factor(first/vol);ii=s.factor(second-first*first/vol)
ratio=s.factor(2*first**3/(vol**2*(vol*second-first**2)))
eq(ratio,15*(a+2)**3/((a+3)**2*(a*a+8*a+10)))
eq(s.diff(ratio,a),-15*(a+1)*(a+2)**2*(a*a+4*a-2)/((a+3)**3*(a*a+8*a+10)**2))
a0=rt-2
kappa=Q(243,25)-Q(171,50)*rt
eq(ratio.subs(a,a0),kappa)
subs={S:1,T:Q(1,3),U:Q(1,3)-h,K:Q(1,6)-2*h/3+h*h,V:vol,J:first,I:ii,B0:2,B1:-2*h,B2:2*h*h,tv:u,yv:u-h}
Ht=canon(H.subs(subs,simultaneous=True).subs(a,a0))
eq(Ht,-(u-1)**2/2)
# On the marked edge the extra direct edge term is 1/2, so its total is zero.
eq(Ht.subs(u,0)+Q(1,2),0)
# A ridge at t=q, rather than one apex, has the concave height G(t,q).
GM=[]
for power in range(3):
    GM.append(s.factor(s.integrate(2*(1-t)*t**power*t*(1-q),(t,0,q))+s.integrate(2*(1-t)*t**power*q*(1-t),(t,q,1))))
Vr=vol+e*GM[0];Jr=first+e*GM[1];Qr=second+e*GM[2]
Rridge=s.factor(2*Jr**3/(Vr**2*(Vr*Qr-Jr*Jr)))
Dr=canon((s.diff(Rridge,e).subs(e,0)/ratio).subs(a,a0))
eq(Dr,q*(1-q)**3*(3*q-2)/2)
eq(Dr.subs(q,Q(3,4)),Q(3,2048))
actual={a:a0,q:Q(3,4),e:Q(1,10)}
Rnew=canon(Rridge.subs(actual));delta=canon(Rnew-kappa)
assert positive(delta)
# Literal eight-vertex one-sided-ridge body. Its whole marked facet is unchanged.
qa=Q(3,4);eps=Q(1,10)
base=[(0,-1),(0,1),(1,0)]
pts=[]
for sign in [-1,1]:
    for x,y in base:pts.append(s.Matrix([x,y,sign*(1+a0*x)/2]))
zridge=(1+a0*qa)/2+eps*qa*(1-qa)
pts.extend([s.Matrix([qa,-(1-qa),zridge]),s.Matrix([qa,1-qa,zridge])])
faces=[(0,1,2),(0,1,4,3),(0,2,5,6,3),(1,2,5,7,4),(3,4,7,6),(5,6,7)]
# Recover every maximal support independently from all vertex triples.
supports=set()
for i,j,k in itertools.combinations(range(8),3):
    n=(pts[j]-pts[i]).cross(pts[k]-pts[i]);n=n.applyfunc(s.expand)
    if n==s.zeros(3,1):continue
    vals=[s.expand(n.dot(p-pts[i])) for p in pts]
    nz=[x for x in vals if x!=0]
    if all(positive(x) for x in nz) or all(positive(-x) for x in nz):
        supports.add(frozenset(i for i,x in enumerate(vals) if x==0))
assert supports==set(map(frozenset,faces))
edges={tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in faces for i in range(len(f))}
assert len(edges)==12
# Positive exact volume fan, with the true three-dimensional centroid and moment.
inside=sum(pts,s.zeros(3,1))/8
VV=s.Integer(0);MM=s.zeros(3,1);XX=s.zeros(3,3)
for face in faces:
    for j in range(1,len(face)-1):
        vs=[inside,pts[face[0]],pts[face[j]],pts[face[j+1]]]
        det=s.expand(s.Matrix.hstack(*(vs[k]-vs[0] for k in [1,2,3])).det())
        if not positive(det):det=-det
        assert positive(det)
        vv=det/6;ss=sum(vs,s.zeros(3,1));qq=sum((v*v.T for v in vs),s.zeros(3,3))
        VV+=vv;MM+=vv*ss/4;XX+=vv*(ss*ss.T+qq)/20
VV=s.expand(VV);MM=MM.applyfunc(s.expand);XX=XX.applyfunc(s.expand)
eq(VV,Vr.subs(actual));eq(MM[0],Jr.subs(actual));eq(XX[0,0],Qr.subs(actual))
centroid=(MM/VV).applyfunc(canon)
assert centroid[1]==0 and positive(centroid[2])
Rfan=canon(2*MM[0]**3/(VV**2*(VV*XX[0,0]-MM[0]**2)))
eq(Rfan,Rnew)
report={'identity':'ACTUAL_FACET_HEIGHT_VARIATIONS_AND_RIDGE_COUNTERCONTROL_V1',
 'weighted_rotation_ratio':str(rot),'flat_hinge_square_gap':str(flat_gap),
 'off_edge_tent_derivative':str(H),'strict_density_tent_identity':str(identity),
 'marked_edge_direct_term':str(Ce2),'stationary_a':str(a0),
 'stationary_normal_ratio':str(kappa),'all_single_apex_derivatives':str(Ht),
 'marked_edge_apex_derivative':'0','ridge_log_derivative':str(Dr),
 'ridge_q':'3/4','ridge_epsilon':'1/10','ridge_ratio':str(Rnew),
 'strict_ratio_increase':str(delta),'f_vector':[8,12,6],
 'vertices':[[str(canon(x)) for x in p] for p in pts],
 'maximal_facets':faces,'true_edges':sorted(edges),
 'volume':str(canon(VV)),'actual_centroid':list(map(str,centroid)),
 'actual_second_raw_moment':[[str(canon(XX[i,j])) for j in range(3)] for i in range(3)],
 'scope':'Moment variations only. Not a 110 construction, not a universal 3/2 proof, not an E17 exclusion.'}
b=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode()
Path(__file__).with_name('facet_height_variations_report.json').write_bytes(b)
print('ACTUAL_FACET_HEIGHT_VARIATIONS_EXACT_PASS',len(b),hashlib.sha256(b).hexdigest(),flush=True)
