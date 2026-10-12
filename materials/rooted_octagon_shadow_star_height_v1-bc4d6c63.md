# material-bc4d6c63a012

AI research material

---

# ROOTED_OCTAGON_ASYMMETRY_WITHOUT_VOLUME_CENTRED_LIFT_V1

## Statement and proof
This exact strictly convex octagon has 0 interior, strict -Q/3 containment, a strict true-boundary arborescence to corner0, and capped barycentric weights 0<=alpha_i<=1/4 summing to1 and giving projected mean0. Nevertheless NO full-dimensional uniformly filled convex polyhedron with exactly the eight vertices (q_i,z_i), one above each displayed corner, has projected centroid0, for ANY heights or true facet lattice. Extra vertices or repeated projections are outside this statement. This proves existence with eight corners for the planar strict relaxation; seven-corner existence remains unresolved, since the accepted obstruction excludes up to six. It is not a 3D U1 or110 construction and does not change 34<=Cmin<=622.

Cone a triangulation of the nonincident facets to a chosen vertex v. Every positive-volume tetrahedron contains v. Therefore the projected volume centroid belongs to conv{(q_v+q_i+q_j+q_k)/4: i,j,k distinct and different from v}. For v=0 and u=(7,5), the values 10000*u*q_i are 70000,61079,42788,18641,-4157,-20135,-26460,-4181. The three smallest nonroot values are at6,5,7, so u*(q0+qi+qj+qk)>=19224/10000=2403/1250. Thus u*g>=2403/5000>0 for every actual homogeneous lift. This is an analytic all-height exclusion, not an inference from failed optimization.

## Exact fixed-height-cone formulation
For fixed projected points and fixed upper/lower surface subdivisions, face coplanarity and supporting-plane inequalities are linear in heights. For a projected triangle abc of area A,
integral h=A(ha+hb+hc)/3,
integral (x,y)h=A*((2a+b+c)ha+(a+2b+c)hb+(a+b+2c)hc)/12.
Subtract lower from upper. Positive fixed volume and zero projected first moments are rational linear constraints. Vertical translation centres the remaining coordinate. Enforce strict supporting inequalities at nonincident vertices and coplanarity of each true face; integration diagonals are not mechanical edges. Corner-only projections automatically preserve all vertices; repeated/interior projected vertices require additional incidence and nondegeneracy checks. This is exact for a fixed projection and subdivisions, not an all-projection theorem.

## Complete source-only recovery
Save the fence as verify_shadow_star_v1.py, UTF-8/LF, then run with assertions enabled:
python -B -S verify_shadow_star_v1.py > verify.out
Observed environment CPython3.13.5, standard library only. No sandbox or search output is an input.

Pins:
verify_shadow_star_v1.py:4240 bytes; SHA256 38cbddb2adc6d8a3cf573b3f15fe6fbe6a60d6d051786c16eafe44c1d2d92624
shadow_star_height_v1.json:1361 bytes; SHA256 970da887818cc4e39c9d953fec02727e781ee8f3bcd6731eec7d002e2e0aff39
verify.out:35 bytes; SHA256 4fcfb60a521c367f68a739ce0ed90d3d77e5a2b8a9893cb9f389aa5e69e793b2

```python
#!/usr/bin/env python3
"""Exact rational shadow/rootedness/volume-centroid obstruction. Standard library."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

DEN = 10000
QINT = ((10000,0),(5172,4975),(1849,5969),(-1122,5299),
        (-3091,3496),(-3780,1265),(-3235,-763),(2462,-4283))
PARENT = (0,0,1,2,3,4,5,0)
ALPHA = tuple(map(F,('20348427/109895468','0','0','0',
                    '17276893/109895468','1/4','1/4','455853/2891986')))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def scale(a,t): return tuple(t*x for x in a)

def triangle_coefficients(q,tri):
    """Integral h and integral (x,y)h on a fixed projected triangle."""
    a,b,c=(q[i] for i in tri)
    area=abs(cross(sub(b,a),sub(c,a)))/2
    if not area: raise ValueError('Degenerate projected triangle')
    total=add(add(a,b),c)
    return area, tuple(area/3 for i in tri), tuple(scale(add(total,q[i]),area/12) for i in tri)

def verify():
    q=tuple(tuple(F(x,DEN) for x in p) for p in QINT)
    n=len(q); zero=(F(0),F(0))
    convex=[]; origin=[]; inclusion=[]
    for i in range(n):
        j=(i+1)%n; e=sub(q[j],q[i])
        origin.append(cross(e,sub(zero,q[i])))
        for k in range(n):
            if k not in (i,j): convex.append(cross(e,sub(q[k],q[i])))
            inclusion.append(cross(e,sub(scale(q[k],F(-1,3)),q[i])))
    arrows=[dot(q[i],sub(q[PARENT[i]],q[i])) for i in range(1,n)]
    assert min(convex)>0 and min(origin)>0 and min(inclusion)>0 and min(arrows)>0
    # A genuine polygon corner is a strict radial maximum exactly when both
    # incident outgoing primitives are negative. No weak boundary primitive occurs.
    primitive={(i,j):dot(q[i],sub(q[j],q[i])) for i in range(n)
               for j in ((i-1)%n,(i+1)%n)}
    assert all(v!=0 for v in primitive.values())
    maxima=[i for i in range(n) if all(primitive[i,j]<0 for j in ((i-1)%n,(i+1)%n))]
    assert maxima==[0]
    assert sum(ALPHA)==1 and all(0<=a<=F(1,4) for a in ALPHA)
    assert tuple(sum(ALPHA[i]*q[i][j] for i in range(n)) for j in range(2))==zero
    # Every tetrahedron of a star triangulation at vertex 0 has 0 and three
    # distinct other vertices. All of its projected centroids lie strictly on
    # the same side of a fixed line. Thus every homogeneous lift does too.
    direction=(7,5)
    triple_scores={t:dot(direction,add(q[0],add(add(q[t[0]],q[t[1]]),q[t[2]])))
                   for t in combinations(range(1,n),3)}
    star_min=min(triple_scores.values())
    assert star_min==F(2403,1250)>0
    assert sorted((dot(direction,q[i]),i) for i in range(1,n))[:3]==[
        (F(-1323,500),6),(F(-4027,2000),5),(F(-4181,10000),7)]
    # Integrals on a test triangle validate the exact height coefficients.
    test=((F(0),F(0)),(F(1),F(0)),(F(0),F(1)))
    A,v,m=triangle_coefficients(test,(0,1,2))
    assert A==F(1,2) and v==(F(1,6),)*3
    assert m==((F(1,24),F(1,24)),(F(1,12),F(1,24)),(F(1,24),F(1,12)))
    return {
        'identity':'ROOTED_OCTAGON_ASYMMETRY_WITHOUT_VOLUME_CENTRED_LIFT_V1',
        'coordinate_denominator':DEN,'q_integer':QINT,'parent':PARENT,
        'minimum_nonincident_edge_cross':str(min(convex)),
        'minimum_origin_edge_cross':str(min(origin)),
        'minimum_minus_third_inclusion_cross':str(min(inclusion)),
        'selected_arrow_numerators_denominator_100000000':[int(a*DEN*DEN) for a in arrows],
        'strict_radial_maxima':maxima,'zero_boundary_primitives':0,
        'capped_barycentric_weights':list(map(str,ALPHA)),
        'star_separator':[7,5], 'star_minimum':str(star_min),
        'all_homogeneous_lifts_centroid_dot_lower_bound':str(star_min/4),
        'minimum_triple':min(triple_scores,key=triple_scores.get),
        'true_3d_centred_lift_exists':False,
        'general_complexity_bound_improved':False,
        'terminal':'ALL_VERIFIED_SHADOW_STAR_HEIGHT_V1'
    }

if __name__=='__main__':
    report=verify()
    raw=(json.dumps(report,sort_keys=True,indent=2)+'\n').encode('utf-8')
    Path('shadow_star_height_v1.json').write_bytes(raw)
    print(report['terminal'])
```

The coordinator executed the exact certificate. The floating locator and all-8646-pair height-cone enumeration were exploratory only; neither is used to justify the all-height exclusion. Their complete reusable source is preserved separately.
