# material-bc9634899fb8

AI research material

---

#!/usr/bin/env python3
"""ASYMMETRIC_RECIPROCAL_EDGE_HULL_V1: exact symbolic and rational checks.
CPython 3.13.5 / SymPy 1.14.0. No inputs, optimizer, seed or parent imports.
The real 3x3 matrix-partition lemma is proved in the companion text.
"""
from pathlib import Path
import hashlib
import json
import sys
import sympy as S

F=S.Rational
p,q,u,v,x,a,b=S.symbols('p q u v x a b', real=True)
I=S.eye(3)


def enc(t):
    if isinstance(t,S.MatrixBase):
        return [[str(t[i,j]) for j in range(t.cols)] for i in range(t.rows)]
    if isinstance(t,S.Basic):return str(t)
    if isinstance(t,dict):return {str(k):enc(v) for k,v in t.items()}
    if isinstance(t,(list,tuple)):return [enc(v) for v in t]
    return t


def pair(uu,vv):
    P=uu*vv+uu+1;Q=uu*vv+vv+1
    return S.diag(uu*vv,uu,1)/P,S.diag(1,vv,uu*vv)/Q


def partition(A,B,pp,qq):
    P=pp*qq+qq+1;Q=pp*qq+pp+1
    X=(pp*P*A+Q*B-pp*(qq+1)*I)/((pp-1)*(pp*qq-1))
    Y=((pp*qq+1)*I-P*A-Q*B)/((pp-1)*(qq-1))
    Z=(P*A+qq*Q*B-qq*(pp+1)*I)/((qq-1)*(pp*qq-1))
    return tuple(T.applyfunc(S.factor) for T in (X,Y,Z))


def symbolic_certificate():
    # Exact inverse affine map of the three endpoint eigenvalue pairs.
    P0=p*q+q+1;Q0=p*q+p+1
    AA,BB=pair(q,p);ep=partition(AA,BB,p,q)
    assert ep==(S.diag(1,0,0),S.diag(0,1,0),S.diag(0,0,1))
    A,B=pair(u,v);XYZ=partition(A,B,p,q)
    assert (sum(XYZ,S.zeros(3))-I).applyfunc(S.factor)==S.zeros(3)
    assert all(S.factor(S.trace(T)-1)==0 for T in XYZ)
    assert (A-(p*q*XYZ[0]+q*XYZ[1]+XYZ[2])/P0).applyfunc(S.factor)==S.zeros(3)
    assert (B-(XYZ[0]+p*XYZ[1]+p*q*XYZ[2])/Q0).applyfunc(S.factor)==S.zeros(3)
    # For p>q, u=q and q<v<p give two strictly negative endpoint-hull coordinates.
    den=(q*v+q+1)*(q*v+v+1)
    negZ=q*(p-v)*(q+1)*(q-v)/((q-1)*(p*q-1)*den)
    negY=q*(p-v)*(q-v)/((p-1)*(q-1)*den)
    assert S.factor(XYZ[2][0,0].subs(u,q)-negZ)==0
    assert S.factor(XYZ[1][2,2].subs(u,q)-negY)==0
    # Fixed upper ratio v=p: all 27 degree-two Bernstein coefficients are
    # nonnegative polynomials under q=2+a, p=q+b, a,b>=0.
    denominators=((p-1)*(p*q-1),(p-1)*(q-1),(q-1)*(p*q-1))
    records=[];nonzero=0;terms=0
    for row in range(3):
        for eig in range(3):
            N=S.factor(XYZ[row][eig,eig].subs(v,p)*denominators[row]*(u*p+u+1)*(u*p+p+1))
            N=S.Poly(S.expand(N.subs(u,1+(q-1)*x)),x)
            assert N.degree()<=2
            coeff=[]
            for k in range(3):
                beta=S.factor(sum(N.nth(j)*F(S.binomial(k,j),S.binomial(2,j)) for j in range(k+1)))
                shifted=S.Poly(S.expand(beta.subs(p,q+b).subs(q,2+a)),a,b)
                literal=tuple((i,j,c) for (i,j),c in shifted.terms() if c)
                assert all(c>0 for i,j,c in literal)
                if literal:nonzero+=1
                terms+=len(literal)
                coeff.append(beta)
                records.append({'partition':row,'eigen_index':eig,'bernstein_index':k,
                                'coefficient_p_q':beta,'positive_shift_terms':literal})
            reconstructed=sum(coeff[k]*S.binomial(2,k)*x**k*(1-x)**(2-k) for k in range(3))
            assert S.expand(reconstructed-N.as_expr())==0
    assert len(records)==27
    return {'negative_endpoint_coordinate_Z00':negZ,
            'negative_endpoint_coordinate_Y22':negY,
            'fixed_upper_ratio_bernstein_coefficients':records,
            'nonzero_bernstein_coefficients':nonzero,'positive_shift_monomials':terms}


def rational_control():
    pp=F(7024915,1000000);qq=F(6832329,1000000)
    uu=qq-F(1,1000000);vv=(pp+qq)/2
    assert 2<uu<qq<vv<pp
    A,B=pair(uu,vv);X,Y,Z=partition(A,B,pp,qq)
    assert S.trace(A)==S.trace(B)==1
    assert B==A.inv()/S.trace(A.inv())
    assert X+Y+Z==I and all(S.trace(T)==1 for T in (X,Y,Z))
    assert Y[2,2]<0 and Z[0,0]<0
    kk=F(281,40);d=kk*kk+kk+1
    guards=(((kk*kk+1)/d)*I-A-B,
            kk*A+B-kk*(kk+1)/d*I,
            A+kk*B-kk*(kk+1)/d*I)
    diagonal_guards=tuple(tuple(T[i,i] for i in range(3)) for T in guards)
    assert all(t>0 for row in diagonal_guards for t in row)
    # The correct one-parameter boundary representation at t=vv has PSD parts.
    edgeparts=partition(A,B,vv,qq)
    assert all(T[i,i]>0 for T in edgeparts for i in range(3))
    assert (vv*qq*edgeparts[0]+qq*edgeparts[1]+edgeparts[2])/(vv*qq+qq+1)==A
    assert (edgeparts[0]+vv*edgeparts[1]+vv*qq*edgeparts[2])/(vv*qq+vv+1)==B
    return {'upper_adjacent_cap_p':pp,'lower_adjacent_cap_q':qq,
            'actual_lower_ratio_u':uu,'actual_upper_ratio_v':vv,
            'A':A,'B':B,'wrong_single_endpoint_partition':(X,Y,Z),
            'violated_Z00':Z[0,0],'violated_Y22':Y[2,2],
            'accepted_common_cap_k':kk,'common_cap_strict_diagonal_guards':diagonal_guards,
            'correct_boundary_parameter_t':vv,'correct_boundary_partition':edgeparts,
            'scope':'FORMAL exact reciprocal spectral pair; not a realized homogeneous body, arrow packet, U1/S1 witness, or minimum-bound change.'}


def main():
    symbolic=symbolic_certificate();control=rational_control()
    report={'identity':'ASYMMETRIC_RECIPROCAL_EDGE_HULL_V1',
            'python':sys.version.split()[0],'sympy':S.__version__,
            'symbolic':symbolic,'rational_control':control,
            'scope':'Closed reciprocal-pair hull for p>=q>=2 is generated by endpoint orbits with spectra (q*t,q,1), q<=t<=p. The single endpoint orbit fails for p!=q. Analytic matrix-partition and convex-hull proof is in the companion text.',
            'status':'PASS'}
    raw=(json.dumps(enc(report),sort_keys=True,indent=2)+'\n').encode()
    dest=Path('asymmetric_reciprocal_report.json');dest.write_bytes(raw)
    print(dest.name,len(raw),hashlib.sha256(raw).hexdigest())
    print('BERNSTEIN_NONZERO',symbolic['nonzero_bernstein_coefficients'],
          'POSITIVE_MONOMIALS',symbolic['positive_shift_monomials'])
    print('FORMAL_STRICT_COUNTERCONTROL_NEGATIVE_Z_AND_Y')
    print('ASYMMETRIC_RECIPROCAL_EDGE_HULL_V1_PASS')


if __name__=='__main__':main()
