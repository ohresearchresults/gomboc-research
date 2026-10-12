# material-9631366c62d3

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Positive-escape path energy and a retained-point C2 complexity/mass gate

New elementary necessary-condition theorem and exact applications, not a110 construction and not an exclusion of general C2/D2 geometry. Independent of an optimizer. The three exact physical objects used below are preserved in [internal-source-reference] plus its unchanged exact-auditor dependency [internal-source-reference]. This theorem complements, rather than replaces, QF71's retained-halfspace mass gate.

## Theorem: finite escape length forces a shifted containing ball
Let P be a full-dimensional convex polytope, origin interior, with one strict unstable vertex A and no additional weak vertex equilibria. At every other vertex v there is a TRUE adjacent w with v·(w-v)>0; otherwise the radial supporting plane makes v strict unstable or weak. For each such arrow,

|w|²-|v|² = 2v·(w-v)+|w-v|² > |w-v|².

Follow positive arrows. Radial norm strictly increases, so the path is acyclic and ends at A. If a path from v to A has k edges, telescoping and Cauchy give

k (|A|²-|v|²) > |A-v|².

If an orthogonal symmetry group fixes the origin and P has m vertex orbits, the path visits at most one vertex of each orbit, since orbit members have equal norms. Thus k<=m-1. More generally any known bound k<=M-1 implies every nonroot vertex lies strictly in

B(A/M, (M-1)|A|/M).

Indeed expanding the ball inequality gives (M-1)(|A|²-|v|²)>|A-v|². Root A lies on this ball's boundary. Convexity of the ball, and strict convexity except at A, imply EVERY point p of P other than A lies strictly inside it. Consequently the same inequality applies to a retained point even if it stops being a vertex in a descendant. This stronger point statement is not an assertion that a path begins at an interior point.

The identical argument applies to vertices of the polar about the SAME physical centre if P has sole strict stable facet and no additional weak facet equilibria. No own polar centroid is substituted. This does not by itself check mixed-edge equilibria or establish110.

## C2 axial architecture and the E<=249 limit
Assume homogeneous C2 symmetry with half-turn around z, one axial top A=(0,0,t), full horizontal bottom facet z=b<t, all other points between these heights. The actual centre is c=(0,0,gamma). The only symmetry-fixed extreme vertex is A; every other vertex orbit has size2 (or at least2 under a larger group). A unique unstable vertex must therefore be A. For E<=249, minimum vertex degree3 gives V<=166; the one fixed vertex forces V odd, hence V<=165 and at most83 C2 vertex orbits. The necessary inequality for every retained p=(w,y) !=A is therefore

82 [(t-y)(t+y-2gamma)-|w|²] > |w|²+(t-y)².

It remains valid when the old marked point becomes nonextreme. It is conditional on the same top, marked point, C2/axial/full-base architecture, own centroid and edge budget; arbitrary movement of p or A escapes this gate. The general nonsymmetric version can use V-1<=165 instead of82. A successful body need not have these symmetries.

The homogeneous centroid floor is gamma>=(t+3b)/4, obtained by coning boundary triangles to the top: each resulting tetrahedron has all three other vertices at heights>=b and centroid height>=(t+3b)/4. Positive volume averaging proves the floor. Since the radial gap in square brackets decreases with gamma, a violation even at this floor excludes ALL own masses for the fixed retained-point architecture and chosen orbit/edge bound. Otherwise the inequality imposes the strict upper bound

gamma < (t+y)/2 - [|w|²+(|w|²+(t-y)²)/82]/[2(t-y)].

These are necessary conditions, not sufficiency or a universal vertex lower bound for class110.

## Exact application to the new V21/E46 controls
Take t=1,b=-1 and the maximum-|y| lateral point, with y here denoting axial coordinate in the formula, not Cartesian second coordinate. G3 has p=(0,-1393/1000,-19/20), gamma=-120482561947/253055728800. Its positive root radial gap is182978607139/13179985875000, yet distance²/gap=605535893606763/1463828857112≈413.66577. Any U1 body retaining p,A and this same centre would require at least414 positive path edges,415 C2 vertex orbits,829 vertices and the elementary degree bound E>=1244. This is a conditional lower bound, NOT a proof that those values are attainable. At E<=249 it is necessary to move the actual centre below -156864767/319800000≈-.490508965 or move the marked point/top/architecture. Current centre≈-.476110786 is above this threshold.

G4/G6 analogous minimum path lengths399/400, elementary degree lower bounds1199/1202 (not claimed sharp; further parity may improve), and gamma thresholds≈-.490364361/-.490378305. All three mass floors equal-.5, which is BELOW these thresholds: the mass-floor+E249 gate alone does NOT exclude all descendants. However, preserving at most the present eight vertex orbits gives k<=7; its required gamma<-2330449/3412500≈-.682915 for G3 (and analogous G4/G6 thresholds) lies below-.5. Hence with the old top, bottom heights and marked lateral point, no homogeneous U1 descendant with at most eight orbits is possible, even if all other geometry and the point's extremality change. More orbits, moving p, changing top/bottom or symmetry can escape. This explains a limitation of shrinking the vertex optimizer to eight active orbits, not all small-body searches.

## Exact source and recovery
Write the following full unit as d2_path_energy.py,2035B,SHA81911b13e3f20785e5c0b3307dbbc47668234f2a2a65c169af4bd17648f219c5, LF+terminal newline. Required complete sources recover_d2_v21.py and d2_vertex_exact.py are in [internal-source-reference]; d2_exact.py is the exact dependency named there. Command `python -B -S d2_path_energy.py`. Expected terminal `D2_PATH_ENERGY_EXACT_CERTIFICATES_PASS 2317 19b59ef638016c51c1567d905ed8b799a682aa4957683c34e422f7a7813b3748`. Output D2_PATH_ENERGY.json2317B with that SHA was freshly reproduced, contains all exact margins, ratios, thresholds and lower bounds. Its field minimum_C2_edges means the elementary proved degree LOWER BOUND, not an attained optimum.

```python
"""Exact certificates for the conditional positive-escape path-energy gate.
Input dependency: the three minimal V21 controls via recover_d2_v21.py.
The general geometric theorem is proved in the companion material text.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from recover_d2_v21 import ROWS
from d2_vertex_exact import convert,raw

def main():
    rows=[]
    for g,points in ROWS.items():
        _,a=convert(dict(name=f'D2_V21_E46_G{g}',denominator=10**g,representatives=points))
        cen=F(a['centroid'][2]);vv=[tuple(F(x,v[3]) for x in v[:3]) for v in a['vertices']]
        p=max(vv,key=lambda v:abs(v[1]));t=F(1);b=F(-1);trans=p[0]**2+p[1]**2
        delta=(t-p[2])*(t+p[2]-2*cen)-trans;distance2=trans+(t-p[2])**2
        assert delta>0
        ratio=distance2/delta;kmin=ratio.numerator//ratio.denominator+1
        gamma82=(t+p[2])/2-(trans+distance2/82)/(2*(t-p[2]))
        gamma7=(t+p[2])/2-(trans+distance2/7)/(2*(t-p[2]))
        floor=(t+3*b)/4
        assert floor<gamma82<cen
        assert gamma7<floor
        margin=distance2-82*delta;assert margin>0
        mmin=kmin+1;vmin=2*mmin-1;emin=(3*vmin+1)//2
        def s(x):return str(x)
        rows.append(dict(name=a['name'],centroid=s(cen),point=list(map(s,p)),delta=s(delta),distance2=s(distance2),path_ratio=s(ratio),minimum_path_edges=kmin,minimum_C2_vertex_orbits=mmin,minimum_C2_vertices=vmin,minimum_C2_edges=emin,violation_82_margin=s(margin),necessary_gamma_upper_E249=s(gamma82),mass_floor=s(floor),necessary_gamma_upper_eight_orbits=s(gamma7)))
    report=dict(theorem='strict positive-escape path energy; conditional retained-point/axial C2 architecture',rows=rows)
    bs=raw(report);Path('D2_PATH_ENERGY.json').write_bytes(bs)
    print('D2_PATH_ENERGY_EXACT_CERTIFICATES_PASS',len(bs),hashlib.sha256(bs).hexdigest())
    for r in rows:print(r['name'],r['minimum_path_edges'],r['minimum_C2_edges'],r['necessary_gamma_upper_E249'],r['necessary_gamma_upper_eight_orbits'])
if __name__=='__main__':main()
```
