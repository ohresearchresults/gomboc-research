# material-7c89e962c8d3

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

#!/usr/bin/env python3
"""Exact local EF/target-VE centroid-cone identities; no global body asserted.
Requires Python >=3.10 and SymPy 1.14.0. Run: python target_pair_centroid_cone.py
"""
from __future__ import annotations
import json
import platform
import sympy as S

def zero(v: S.Matrix | S.Expr) -> None:
    entries = list(v) if isinstance(v, S.MatrixBase) else [v]
    for x in entries:
        assert S.factor(x) == 0, str(x)

def main() -> None:
    H,j,u,mu,la,t,nu = S.symbols('H j u mu la t nu', positive=True)
    de = H*t*(mu+la)+j*((1-H)*mu+la)
    beta,psi = H*t/de,j/de
    a,b,c = S.eye(3).columnspace()
    r,q,s = S.Matrix([1,1,1]),S.Matrix([1-H,1,1]),S.Matrix([1,1,1-j])
    e=S.Matrix([-j*u/H,1+u+(1-H)*j*u/H,-u])
    aa=mu/H+mu*t/j
    N0=S.Matrix([[aa,mu-aa,0],[mu-aa,la-mu+aa,0],[0,0,0]])
    zvec=S.Matrix([-t,t-1,1]); N=N0+(nu/j)*zvec*zvec.T
    zero(N*r-S.Matrix([mu,la,0]))
    zero(beta*N*s+psi*N*q-b)
    zero(S.det(N0[:2,:2])-mu*de/(H*j))
    zero(S.det(N)-mu*nu*de/(H*j*j))
    ell=S.Matrix([-j*u/mu,0,-j*u/nu-j*t*u/mu])
    zero(N*ell-(e-b))
    x,y,X,Z=S.symbols('x y X Z')
    w=S.Matrix([0,x,y]); v=S.Matrix([0,X,((1+u+(1-H)*j*u/H)*X-Z)/u])
    bp=S.Matrix([-x/H,-x+x/H-(X-x)/j,(X-x)/j])
    zero(q.dot(bp));zero(r.dot(bp)+x);zero(s.dot(bp)+X)
    L=j*u/(mu*H); A=u/nu+u*t/mu+L
    Q=S.Matrix([[-la-nu*(t-1),-nu,la,0]])
    P=S.Matrix([[A,0,beta-A+L,-beta]])
    vec=S.Matrix([x,y,X,Z])
    zero((Q*vec)[0]-(w.dot(N*(s-2*r))+r.dot(N*v)))
    zero((P*vec)[0]-(bp.dot(ell)+beta*(X-Z)))
    W=S.Matrix.hstack(a+2*b+c,a+b+2*c,u*(a+2*b+e),u*(a+b+2*e))
    k=S.Matrix([2*u,-u,-2,1])
    zero(W*k)
    zero(S.det(W[:,:3])-j*u*u*(H-4)/H)
    qk=u*nu*(3-2*t)-2*la*(u+1)
    pk=2*(u+1)*A-2*L-3*beta
    zero((Q*k)[0]-qk);zero((P*k)[0]-pk)
    z1,z2,z3=S.symbols('z1 z2 z3')
    z4=-2*u*z1+u*z2+2*z3
    dn=(z2-z1)/j;bn=(z4-z3)/(j*u*u);kn=2*z1-z2
    an=(kn+4*(bn+dn))/(4-H)
    normal=an*q-bn*r-dn*s
    zero(W.T*normal-S.Matrix([z1,z2,z3,z4]))
    pars={H:S.Rational(1,2),j:S.Rational(1,2),u:S.Rational(1,2),
          mu:S.Rational(1,2),la:S.Rational(1,2),t:S.Integer(3),nu:S.Rational(1,2)}
    nc=N.subs(pars);mc=nc.inv();wc=W.subs(pars);qc=Q.subs(pars);pc=P.subs(pars)
    qkc=qk.subs(pars);pkc=pk.subs(pars);assert qkc<0<pkc
    zr=abs(pkc)*qc+abs(qkc)*pc
    dc=S.factor((zr[1]-zr[0])/pars[j])
    bc=S.factor((zr[3]-zr[2])/(pars[j]*pars[u]**2))
    kc=2*zr[0]-zr[1]; ac=S.factor((kc+4*(bc+dc))/(4-pars[H]))
    nn=ac*q.subs(pars)-bc*r-dc*s.subs(pars)
    zero(wc.T*nn-zr.T)
    assert all(mc[:i,:i].det()>0 for i in [1,2,3])
    assert ac==S.Rational(-12,7) and bc==S.Rational(4,5) and dc==S.Rational(-13,10)
    assert nn.dot(a)==S.Rational(-5,14)<0
    # The unique orientation with a positive q coefficient has B<0 and n(a)>0.
    assert -bc<0 and (-nn).dot(a)>0
    assert all(0<val<4 for val in [pars[H],pars[j],pars[j]*pars[u]])
    def mat(m):return [[str(v) for v in list(m.row(i))] for i in range(m.rows)]
    out={
      'scope':'Local physical contact and moment-map algebra only; not an actual uniform-centred 10/17/9 body.',
      'python':platform.python_version(),'sympy':S.__version__,
      'parameters':{str(key):str(value) for key,value in pars.items()},
      'N':mat(nc),'M':mat(mc),'M_leading_minors':[str(mc[:i,:i].det()) for i in [1,2,3]],
      'e':mat(e.subs(pars)),'beta':str(beta.subs(pars)),'psi':str(psi.subs(pars)),
      'Q':mat(qc),'P':mat(pc),'Qk':str(qkc),'Pk':str(pkc),'positive_combination_z':mat(zr),
      'A_B_D':[str(ac),str(bc),str(dc)],'normal':mat(nn),
      'normal_at_a_b_c_e':[str(nn.dot(v.subs(pars))) for v in [a,b,c,e]],
      'symbolic_checks':'N SPD Schur form, EF/VE incidence, edge covector, physical derivatives, moment kernel and conormal identities',
      'terminal_markers':['TARGET_VE_CENTROID_CONE_IDENTITIES_PASS','LOCAL_TARGET_CONORMAL_ESV_SIGN_EXTENSION_FAILS_PASS']
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
