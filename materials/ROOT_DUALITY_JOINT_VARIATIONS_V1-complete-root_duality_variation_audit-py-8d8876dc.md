# material-8d8876dc6f15

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Exact algebra audit for ROOT_DUALITY_JOINT_VARIATIONS_V1.
CPython 3.13.5, SymPy 1.14.0; no external inputs; assertions enabled.
Run: python root_duality_variation_audit.py
This checks algebra, not the analytic variational admissibility proofs.
The rational control is FORMAL MOMENT DATA, NOT a convex-body attainer.
"""
import sympy as S
assert __debug__
Q = S.Rational

def zero(x):
    if isinstance(x, S.MatrixBase):
        assert all(S.cancel(y) == 0 for y in x)
    else:
        assert S.cancel(x) == 0

a,b,c,d,u,v,z,t,q = S.symbols('a b c d u v z t q', nonzero=True)
p=u+v; s=a+b
point=S.Matrix([u,v,z]); w=S.Matrix([v/(3*p),u/(3*p),S.Rational(1,3)])
ell=lambda k: a+(d-a)*k[0]+(c-a)*k[1]+(b-a)*k[2]
n=lambda k: (s+c)*k[0]+(s+d)*k[1]
mu=ell(point); r=n(point)
zero(3*p*ell(w)-r)
TT=r/(t*mu); m=3*p/t
Rt=(TT*point-m*w)/(TT-m)
zero(ell(Rt))
zero(Rt-S.Matrix([TT*t*u-v,TT*t*v-u,TT*t*z-p])/(TT*t-3*p))
print('FIXED_BODY_ROOT_DUALITY_ALGEBRA_PASS')

# Root-plane stationarity: affine tests 1, coordinates, and G.
# Sroot = 6 V^2(T-m). For V=t/6, q=6VT=tT.
V=t/6; actual_q=r/mu; actual_T=actual_q/t
beta=S.Matrix([s+c+actual_q*(a-d),s+d+actual_q*(a-c),actual_q*(a-b)])
G=lambda k: n(k)-r-actual_q*ell(k)
zero(G(point)+r)
zero(G(w)+r+actual_q*r/(3*p)-n(w))
root_mass=6*V**2*(actual_T-m)
root_first=6*V**2*(actual_T*point-m*w)
zero(root_first/root_mass-Rt)
# h=G gives integral_F G^2/|grad ell|.
root_square=actual_q*V*G(point)-3*V*p*G(w)
zero(root_square-6*V**2*m*(r-n(w)))
zero(beta.dot(point)-actual_q*a)
print('ROOT_PLANE_FIRST_AND_SECOND_G_MOMENTS_PASS')

# Diagonal projectivity: infinitesimal coefficients of n after genuine
# uniform refilling. Its barycentric Jacobian derivative is sum(eta)-4phi.
x,y,zz,eps=S.symbols('x y zz eps')
eA,eB,eC,eD=S.symbols('eA eB eC eD')
phi=eA*(1-x-y-zz)+eB*zz+eC*y+eD*x
f=1+eps*phi
xp=(1+eps*eD)*x/f; yp=(1+eps*eC)*y/f
ap=a/(1+eps*eA); bp=b/(1+eps*eB)
cp=c/(1+eps*eC); dp=d/(1+eps*eD)
K=(eD*(s+c)-eA*a-eB*b-eC*c)*x+(eC*(s+d)-eA*a-eB*b-eD*d)*y
zero(S.diff((ap+bp+cp)*xp+(ap+bp+dp)*yp,eps).subs(eps,0)-K+((s+c)*x+(s+d)*y)*phi)

# Projective covariance equations. Substitute Ephi^2 through Sigma beta,
# using integral G phi/V = -r phi(g) + cov(G,phi).
# For eta_D,C,B respectively: 5 Sigma beta component = EK-r +4r Ephi.
Kmean=S.expand(K).subs({x:u,y:v,zz:z})
target5=S.Matrix([4*r*u-(s+2*d)*v,4*r*v-(s+2*c)*u,4*r*z-r-b*p])
for i,eta in enumerate((eD,eC,eB)):
    Ek=Kmean.subs({h:int(h==eta) for h in (eA,eB,eC,eD)})
    zero(target5[i]-(Ek-r+4*r*point[i]))
R=S.expand(S.Matrix([s+c+q*(a-d),s+d+q*(a-c),q*(a-b)]).dot(target5))
R_formula=2*q*((a*a+a*b+b*b)*p+s*c*u+s*d*v+c*c*u+d*d*v)-(s*s*p+s*(2*c*u+c*v+d*u+2*d*v)+2*c*d*p)
# These identities are on q*mu=r, not independent q.
zero((R-R_formula).subs(q,r/mu))
print('DIAGONAL_PROJECTIVE_COVARIANCE_IDENTITIES_PASS')

# Formal data obey all displayed first-moment caps and projective covariance
# equations with a PSD covariance dominating the forced tetrahedral part.
# They are deliberately NOT actual realizable high-trace body/root data.
aa,bb,cc,dd=Q(1),Q(1,2),Q(2,5),Q(2,5)
tt,trace=Q(5),Q(11,5)
g=S.Matrix([Q(3,4),Q(3,4),-Q(7,22)])
pp=g[0]+g[1]; ss=aa+bb
muu=aa+(dd-aa)*g[0]+(cc-aa)*g[1]+(bb-aa)*g[2]
rr=(ss+cc)*g[0]+(ss+dd)*g[1]; qq=rr/muu; mm=3*pp/tt
B=S.Matrix([ss+cc+qq*(aa-dd),ss+dd+qq*(aa-cc),qq*(aa-bb)])
g0=S.ones(3,1)/4; Sigma0=(4*S.eye(3)-S.ones(3,3))/80
Sigma_min=Sigma0/tt+(g-g0)*(g-g0).T/(tt-1)
T5=S.Matrix([4*rr*g[0]-(ss+2*dd)*g[1],4*rr*g[1]-(ss+2*cc)*g[0],4*rr*g[2]-rr-bb*pp])
yy=T5/5-Sigma_min*B; gap=B.dot(yy)
Sigma=Sigma_min+yy*yy.T/gap
assert (muu,rr,qq,mm)==(Q(57,220),Q(57,20),Q(11),Q(9,10))
assert qq==tt*trace and gap==Q(48323,6400)
zero(Sigma*B-T5/5)
assert all(Sigma[:i,:i].det()>0 for i in (1,2,3))
assert all(Sigma_min[:i,:i].det()>0 for i in (1,2,3))
assert all(e>0 and e<=4*muu for e in (aa,bb,cc,dd))
assert g[0]>=Q(1,4) and g[1]>=Q(1,4)
assert 4*g[0]<=tt and 4*g[1]<=tt and 4*pp==tt+1
assert 4*tt*muu>=cc*tt+ss+dd and 4*tt*muu>=dd*tt+ss+cc
assert min(aa,bb)>=4*muu*(trace-2)
assert trace<=1+ss/(4*muu) and tt<Q(45,7) and mm>Q(13,15)
ww=S.Matrix([g[1]/(3*pp),g[0]/(3*pp),Q(1,3)])
RR=(trace*g-mm*ww)/(trace-mm)
assert RR==S.Matrix([Q(15,13),Q(15,13),-Q(10,13)])
# The known exact equality-body theorem forces the fifth point R0 below:
R0=S.Matrix([Q(5,2),Q(5,2),-Q(25,11)])
assert (R0[0]*tt+R0[1])/(4*tt)==g[0]
assert (R0[1]*tt+R0[0])/(4*tt)==g[1]
assert (1+R0[2])/4==g[2]
bad_ell=aa+(dd-aa)*R0[0]+(cc-aa)*R0[1]+(bb-aa)*R0[2]
assert bad_ell==-Q(19,22)
print('FORMAL_COVARIANCE_CONTROL_PASS_NOT_AN_ACTUAL_BODY_ROOT_PAIR')
print('formal_covariance=',str(Sigma.tolist()))
print('covariance_gap=',gap)
print('forced_equality_vertex_ell=',bad_ell)
print('ROOT_DUALITY_JOINT_VARIATIONS_ALGEBRA_PASS')
