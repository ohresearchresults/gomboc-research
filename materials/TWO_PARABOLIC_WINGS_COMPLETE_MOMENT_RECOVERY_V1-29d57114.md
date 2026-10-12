# material-29d5711452b4

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Complete two-sided parabolic-wing moment classes

## The actual theorem
For every a,b>0 define

    U(y)=(b-a)y+a+b+ab,
    K={(t,y):-1-a<=y<=1+b, max(0,y^2-1)<=t<=U(y)},
    e={(0,y):-1<=y<=1}.

The lower graph is convex, the upper graph affine, and the upper line joins the two endpoint values of the parabola. It lies above the parabola and above0 throughout the given interval. Thus K is a genuine compact full-dimensional convex support with the entire marked edge e. This is not a polygonal surrogate for the curved support.

For EACH of the two affine densities ell=1 and ell=U(y)-t, use its actual weighted barycentre, covariance Sigma and edge second moment T about that SAME barycentre. Let V=int_K ell, Jt=int_K t ell, B0=int_e ell, alpha=Jt B0/V^2. Then

    alpha T < (3/2) Sigma

as a horizontal2x2 positive-definite difference throughout the entire positive a,b quadrant. The second density is positive in the interior and vanishes on the full opposite upper edge. It is not an independent assignment of density moments.

For the actual uniform lift P={(t,y,z):(t,y) in K, |z|<=ell(t,y)/2}, the horizontal/z mixed covariance and facet mixed moments vanish by symmetry. The complete transverse theorem in the fully read parent minimum-0290 bounds the other block by10-5sqrt(3)<3/2. Hence the full actual3D whole lateral-facet matrix bound also follows. These are moment theorems, NOT equilibrium exclusions, NOT a classification of all conic extrema and NOT an improved C minimum.

## Exact polynomial proof
The complete source below integrates the actual support as the upper-line region minus its two lower parabolic pieces. It forms every raw moment of order at most2, the exact moving barycentre, Sigma, T and G=(3/2)Sigma-alpha T. It then proves the two leading Sylvester quantities G00 and det G positive.

The rational G00 and determinant are invariant under reflection y->-y, a<->b; the source proves that identity algebraically. Consequently it suffices to use a=b+c0 with b>0,c0>=0. In these variables the numerator and denominator coefficients of both quantities are all nonnegative, with positive terms even when c0=0. Hence both are strictly positive, not just numerically sampled.

For constant density the unshifted G00 numerator has132 terms and18 negative coefficients, degree16; its determinant has289 terms and11 negatives, degree24. Those negative coefficients were a failed sufficient test, not a counterexample. The reflected-half-quadrant polynomials have128 and285 terms, all nonnegative.
For the upper-zero density the unshifted G00 has269 terms and7 negative coefficients, degree24; the determinant has598 terms and no negative coefficient, degree36. Reflection likewise proves the complete half quadrant and its mirror. The exact full numerator/denominator polynomials are regenerated in the two reports.

## Complete durable recovery
Standalone source, no inputs/checkpoints/seeds. Environment Python3.13.5, SymPy1.14.0. Assertions must remain enabled. Save the literal source with LF newlines and one final newline as two_parabolic_wings.py. Both commands reconstruct and verify their exact complete class:

    python -B two_parabolic_wings.py uniform
    python -B two_parabolic_wings.py upper

Expected markers:
TWO_PARABOLIC_WINGS_UNIFORM_EXACT_PASS
TWO_PARABOLIC_WINGS_UPPER_EXACT_PASS

Input:
two_parabolic_wings.py2887B SHA2562dd425eac888d6dd5459a923d858721497a151502c2110a1ba8c655502207003
Outputs:
two_wings_uniform_report.json11503B SHA2563f52eb70b248f8a8bcb35236642d31da62e0fd76fc435a25b6f5cb5e3f708132
two_wings_upper_report.json27807B SHA256b46f71160fdb7b0e6cc1b22f254b56bd761b6d913b98e56a2a575b8921d41c70
Both normal runs and fresh source-only runs completed with byte-identical reports. The acceptance is exact symbolic algebra and coefficient positivity, not proof-assistant formalization.

## Complete source

```python
"""Exact centered facet-moment matrix for two parabolic wings.
Python3.13.5 SymPy1.14.0. Complete polynomial moment integration, no inputs.
K: -1-a<=y<=1+b, max(0,y*y-1)<=t<=U(y).
Densities 1 and U-t; whole marked edge t=0,-1<=y<=1.
"""
import sympy as s,json,hashlib,argparse
from pathlib import Path
a,b,y,c0=s.symbols('a b y c0',nonnegative=True)
U=(b-a)*y+a+b+a*b;W=y*y-1

def integral(p,lo,hi):
    P=s.Poly(s.expand(p),y)
    return s.expand(sum(c*(hi**(i+1)-lo**(i+1))/s.Integer(i+1) for (i,),c in P.terms()))

def moment(i,j,kind):
    def f(v):
        base=v**(i+1)/s.Integer(i+1)
        return y**j*(base if kind=='uniform' else U*base-v**(i+2)/s.Integer(i+2))
    return s.factor(integral(f(U),-1-a,1+b)-integral(f(W),-1-a,-1)-integral(f(W),1,1+b))

def run(kind):
    V=moment(0,0,kind);J=s.Matrix([moment(1,0,kind),moment(0,1,kind)])
    K=s.Matrix([[moment(2,0,kind),moment(1,1,kind)],[moment(1,1,kind),moment(0,2,kind)]])
    Bj=[s.factor(integral(y**j*(1 if kind=='uniform' else U),-1,1)) for j in range(3)]
    print(kind,'V',V,'J',list(J),'Bj',Bj,flush=True)
    g=J/V;c=s.Matrix([0,Bj[1]/Bj[0]]);alpha=s.factor(J[0]*Bj[0]/V**2)
    T=s.diag(0,Bj[2]/Bj[0])-g*c.T-c*g.T+g*g.T
    Sig=K/V-g*g.T;G=(s.Rational(3,2)*Sig-alpha*T).applyfunc(s.factor)
    records=[]
    for name,f in [('G00',G[0,0]),('det',s.factor(G.det()))]:
        num,den=s.fraction(f);P=s.Poly(s.expand(num),a,b);N=s.Poly(s.expand(den),a,b)
        original_negative=sum(bool(x<0) for x in P.coeffs())
        # Reflection y -> -y exchanges a,b; normalize the half quadrant a>=b.
        assert s.expand(num*den.xreplace({a:b,b:a})-num.xreplace({a:b,b:a})*den)==0
        PP=s.Poly(s.expand(num.subs(a,b+c0)),b,c0);NN=s.Poly(s.expand(den.subs(a,b+c0)),b,c0)
        ok=all(x>=0 for x in PP.coeffs()) and all(x>=0 for x in NN.coeffs())
        print(kind,name,'terms',len(P.terms()),'neg',sum(bool(c<0) for c in P.coeffs()),'degree',P.total_degree(),'positive',ok,flush=True)
        records.append({'name':name,'numerator':str(num),'denominator':str(den),'power_positive':ok,'terms':len(P.terms()),'degree':P.total_degree(),'original_negative':original_negative,'reflection_half_terms':len(PP.terms())})
    report={'identity':'TWO_PARABOLIC_WINGS_'+kind.upper()+'_V1','volume':str(V),'first_moment':list(map(str,J)),'second_moment':list(map(str,K)),'edge_moments':list(map(str,Bj)),'alpha':str(alpha),'certificates':records}
    data=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode();out=Path(__file__).with_name('two_wings_'+kind+'_report.json');out.write_bytes(data)
    assert all(c['power_positive'] for c in records)
    print('TWO_PARABOLIC_WINGS_'+kind.upper()+'_EXACT_PASS',len(data),hashlib.sha256(data).hexdigest(),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('density',choices=['uniform','upper']);args=ap.parse_args();run(args.density)
```
