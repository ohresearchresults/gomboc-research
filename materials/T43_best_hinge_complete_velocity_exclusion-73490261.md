# material-7349026116fe

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# T43 best single-hinge plane: complete velocity-domain exclusion

## Scope and exact theorem
On the fixed INTEGER-coordinate plane n=(-325273,-698874,-240310), h=-45275161 of literal T43 all-G3, EVERY globally convex hinge F_v(x)=x+v max(0,n·x-h), n·v=0, retains original input vertices24 and29 as STRICT unstable equilibria at the actual homogeneous centroid. Thus this entire two-dimensional hinge-velocity family is excluded from own110. This is not an exclusion of other plane orientations, combined hinges, additional global affine metrics, free support changes, or T43 descendants generally.

The complete velocity polygon is exactly v=a*u+b*v with a>=0,b>=0,a+b<=1, where the two rational basis velocities are literal in the source below. Exact facet inequalities from the dependency establish all three corners feasible. Three nonempty groups of those same inequalities force a>=0,b>=0,a+b<=1; consequently there is no omitted region.

For each root i and every other candidate transformed original vertex or section-edge crossing j, the centred escape is an exact quadratic in a,b. The homogeneous centroid moves by beta*(a*u+b*v), beta=(n·Mplus-hVplus)/V, not by a virtual-centre parameter. The quadratic Hessian is a scalar multiple of the positive-definite Gram matrix of u,v. Its maximum on the triangle is attained at a vertex, an edge stationary maximum, or an interior stationary maximum when concave; the code enumerates all these possibilities exactly. ALL130 maxima are strictly negative. This both preserves the two roots and certifies that they remain extreme. The worst maximum is approximately -519294.48 in integer-coordinate squared units, not physical-coordinate units (divide by10^6).

## Dependency and recovery
This source requires the COMPLETE finite_hinge_exact.py unit from immutable material [internal-source-reference], T43_finite_hinge_exact_recovery.md, material SHA d62d046640d6365501698bb41185ba3e351e043f8935a5c0a02bd3654d2deb00. Select that material too for any computational successor; the ID alone does not supply its bytes. That dependency contains all43 T43 rows and every hull/moment helper, so neither FULL76 nor an old sandbox is needed.
Save the following exact block as hinge_triangle_exclusion.py:3652 bytes,SHA256 39bbafc5ff8bee7e2c3f21948666cefe2c02f6be6f7fc6e68c385280e9bb7e0a. Run python -B -S hinge_triangle_exclusion.py alongside finite_hinge_exact.py. Coordinator actually executed this under CPython3.13.5, standard library only. Expected marker HINGE_TRIANGLE_ROOT_MAXIMA 130 True. Full output hinge_triangle_exclusion.json:345278 bytes,SHA256 43e91650387e6fdc38da0010399295227db32030e8d4edab6e3424e1c87f4b0d. It includes every exact polynomial, maximizer, maximum and domain-forcing witness. This is exact rational computation, not proof-assistant verification.

```python
"""Exact all-velocity two-root check on the best T43 hinge plane.
Uses the complete finite_hinge_exact.py recovery unit. No interval sampling.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json,hashlib
from finite_hinge_exact import P,hull,moments,controls,dot,sub,add,scale,primitive_plane,complex_from_supports,integrate

def max_quadratic_triangle(q):
    # q=A+B a+C b+D a*a+E a*b+F b*b.
    A,B,C,D,E,FF=q
    def ev(p):
        a,b=p;return A+B*a+C*b+D*a*a+E*a*b+FF*b*b
    vertices=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
    candidates=[(ev(p),p,'vertex') for p in vertices]
    for p,r in zip(vertices,vertices[1:]+vertices[:1]):
        u,v=sub(r,p);a,b=p
        lin=B*u+C*v+2*D*a*u+E*(a*v+b*u)+2*FF*b*v
        quad=D*u*u+E*u*v+FF*v*v
        if quad<0:
            t=-lin/(2*quad)
            if 0<t<1:
                x=add(p,scale((u,v),t));candidates.append((ev(x),x,'edge'))
    disc=4*D*FF-E*E
    if D<0 and disc>0:
        a=(E*C-2*FF*B)/disc;b=(E*B-2*D*C)/disc
        if a>=0 and b>=0 and a+b<=1:candidates.append((ev((a,b)),(a,b),'interior'))
    # For this application the quadratic part is a scalar multiple of a SPD Gram matrix.
    assert disc>=0 and ((D>=0 and FF>=0) or (D<=0 and FF<=0))
    return max(candidates,key=lambda r:r[0])

def main():
    n=(-325273,-698874,-240310);h=-45275161
    u=scale((6558183650,-10897765265,22816215436),F(896003,43031309628659688161280))
    v=scale((9143958392,-13454834289,26752740547),F(896003,57272582292669275259520))
    faces,edges=hull(P);z,active,bounds=controls(P,faces,n,h)
    coeff=[(dot(m,u),dot(m,v),B) for (_,m,_),B in zip(faces,bounds)]
    assert all(a<=B and b<=B for a,b,B in coeff)
    forces_a=[i for i,(a,b,B) in enumerate(coeff) if B==0 and a<0 and b==0]
    forces_b=[i for i,(a,b,B) in enumerate(coeff) if B==0 and a==0 and b<0]
    forces_sum=[i for i,(a,b,B) in enumerate(coeff) if B>0 and a==b==B]
    assert forces_a and forces_b and forces_sum
    cp=[tuple(F(z[i]*P[j][k]-z[j]*P[i][k],z[i]-z[j]) for k in range(3)) for i,j in edges if z[i]*z[j]<0]
    upper=[tuple(map(F,p)) for p,zz in zip(P,z) if zz>=0]+cp
    planes=[primitive_plane(m,b) for ids,m,b in faces]+[primitive_plane(scale(n,-1),-h)]
    X,ff,pl,ee=complex_from_supports(upper,planes);vp,mp,cc=integrate(X,ff)
    V,c=moments(P,faces);beta=(dot(n,mp)-h*vp)/V
    cloud=list(P)+cp;zz=z+[0]*len(cp);roots=[24,29];records=[]
    for i in roots:
        xi=sub(P[i],c);si=max(z[i],0);alpha=si-beta
        for j,p in enumerate(cloud):
            if j==i:continue
            d=sub(p,P[i]);s=max(zz[j],0)-si;C=alpha*s
            L=add(scale(d,alpha),scale(xi,s))
            q=(dot(xi,d),dot(L,u),dot(L,v),C*dot(u,u),2*C*dot(u,v),C*dot(v,v))
            mx,pt,kind=max_quadratic_triangle(q)
            records.append(dict(root=i,witness=j,max=str(mx),argmax=list(map(str,pt)),kind=kind,coeff=list(map(str,q))))
    all_strict=all(F(r['max'])<0 for r in records)
    worst=sorted(records,key=lambda r:F(r['max']),reverse=True)[:10]
    output=dict(roots=roots,all_strict=all_strict,tests=len(records),domain_forcing=[forces_a,forces_b,forces_sum],
                worst=worst,records=records,beta=str(beta),velocity_basis=[list(map(str,u)),list(map(str,v))])
    raw=(json.dumps(output,sort_keys=True,separators=(',',':'))+'\n').encode();path=Path(__file__).with_name('hinge_triangle_exclusion.json');path.write_bytes(raw)
    print('HINGE_TRIANGLE_ROOT_MAXIMA',len(records),all_strict,[(r['root'],r['witness'],float(F(r['max'])),r['kind']) for r in worst[:3]],len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```
