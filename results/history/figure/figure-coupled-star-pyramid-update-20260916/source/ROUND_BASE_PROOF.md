# Round-base homogeneous-pyramid obstruction

## Statement and scope

Let B be a full-dimensional convex polygon in a plane, with its **area centroid** at the origin in that plane. Suppose that the closed disk of radius R is contained in B and B is contained in the closed disk of radius Q, both disks being centred at that same centroid. Assume R>0 and 20R>=13Q.

For EVERY apex outside the base plane, the filled homogeneous pyramid conv(B,apex), with equilibria measured about its actual volume centroid, has either at least two stable equilibria or at least two unstable equilibria. It therefore cannot have strict (S,U,H)=(1,1,0) and weak-only000.

This is a sufficient obstruction on the base geometry, not an exclusion of all pyramids, all deformations, or an entire affine/projective orbit. Arbitrary loading is outside its hypotheses. Changing a fixed base only by an isometry or uniform scaling preserves the conclusion; a general affine map need not preserve its disk ratio.

## Proof

Use coordinates in which the base plane is z=0, its area centroid is 0, and the apex is A=(a,h), a in R^2 and h>0. Reflection in the base plane covers the other side. The volume centroid is g=(a/4,h/4): the cross-section at height z is (1-z/h)B+(z/h)a, its area scales by (1-z/h)^2, and integrating its first moments gives this formula. Write t=|a| and c=13/20.

### Low height: 0<h<R

The section of the pyramid through g parallel to its base is, after translation by -g, (3/4)B at height0. Hence the centred body contains an equatorial disk of radius3R/4. Its extent in the two normal directions is3h/4 and h/4. For its support function s on the unit sphere, all equatorial values are at least3R/4, whereas both normal-pole values are strictly smaller. The minimum on each closed hemisphere is therefore attained in that hemisphere's interior. These are two distinct stable equilibria.

For completeness, a local minimum of the support function of a full-dimensional polytope containing0 in its interior is a stable face equilibrium. If the exposed face had dimension below2, rotate the normal infinitesimally while remaining perpendicular to the affine differences of that face; other vertices remain strictly below the support plane. All exposed points have a common derivative beta in this direction. Choose the sign of the direction so that beta<=0. The support value is then s(u)cos(theta)+beta*sin(theta)<s(u), contradicting the minimum. If the exposed face is a facet but the orthogonal foot is not in its relative interior, there is a tangent direction d for which max_{x in facet} x.d<=0. Under the corresponding small spherical rotation its support is s(u)cos(theta)+max(x.d)sin(theta)<s(u), again a contradiction. Thus the perpendicular foot is in the relative interior of a maximal facet. Both hemisphere minima give strict stable equilibria. Possible additional weak equilibria elsewhere do not remove these two.

### High height: h>=R

A centred base vertex and the centred apex are respectively

    v=(b-a/4,-h/4),    u=(3a/4,3h/4).

For every b in B,

    u.(v-u)=(3/4)(a.b-t^2-h^2)
             <=(3/4)(Qt-t^2-h^2)
             <=(3/4)(Q^2/4-R^2)<0,

because R>=13Q/20>Q/2. Hence the apex is strictly unstable.

Choose a base vertex b maximizing r=|b-a/4| over B. Such a vertex exists because B is a finite convex hull. For every other base vertex b', the corresponding centred vertices satisfy

    2v.(v'-v)=|v'|^2-|v|^2-|v'-v|^2<0.

To prove that b is also strictly unstable it remains only to prove v.(u-v)<0. Define

    f=4v.(u-v)=5a.b-4|b|^2-t^2-h^2.

Every base vertex satisfies R<=|b|<=Q.

If 0<t<=cR, then

    f<=5tQ-t^2-5R^2
      <=5R(cQ-R)-t^2<0,

as cQ<=R. At t=0 the original expression is -4|b|^2-h^2<0.

If t>=cR, the point -Ra/t belongs to the inner disk, hence belongs to B. By the choice of b,

    r^2=|b-a/4|^2 >= (R+t/4)^2.

Using a.b=2|b|^2+t^2/8-2r^2 yields

    f=6|b|^2-(3/8)t^2-10r^2-h^2
      <=6Q^2-11R^2-5Rt-t^2
      <=6Q^2-(11+5c+c^2)R^2
      =6Q^2-(5869/400)R^2
      <=-(31861/160000)Q^2<0.

The final inequality uses R^2>=169Q^2/400. Thus b and the apex are two different strictly unstable vertices. Low and high heights exhaust all noncoplanar apex choices. QED.

## Exact applications executed in this turn

`round_base_gate.py` computes the actual area centroid by an anchored polygon triangulation, confirms coplanarity and convex cyclic order, and proves squared distances to all supporting edge lines exceed R^2 and all vertex squared distances are below Q^2. The certificate uses full Euclidean distances in the base plane, not distances in a non-isometric 2D projection.

- C80_BASE20: R=66612792, Q=100852489; 20R-13Q=21173483>0. The exact high-height margin 5869R^2-2400Q^2 is1631363866620674016>0.
- C96_BASE24: R=58972, Q=78849; 20R-13Q=154403>0. The exact high-height margin is5489406902896>0.

C80_BASE20 is the base of the journal's literal21-point C80 own211 body. C96_BASE24 is the projection of the literal C13825-point integer cloud excluding index15 onto n=(4,11,0)^perp by Y=137p-(n.p)n. The apex point is irrelevant to the fixed-base theorem. The journal's subsequent common translation is also irrelevant. Both conclusions cover **all apex tangent positions and all nonzero heights** on the respective fixed base.

The independently audited C80 forced-reference-centroid example is a concrete illustration, not the proof: replacing its apex by4*g_ref-3*b_base gives exact actual centroid g_ref=(7695683,168054,-75622586), but its signature is222/weak000, not110. The exact all-apex obstruction is stronger than this one negative test.

## Evidence status

This is a coordinator-derived mathematical proof and two executed rational hypothesis certificates. No assertion of historical novelty is made. It is not a worker result or a claimed new winner. It has not been appended to the canonical journal through a mutation tool in this read-only turn; preserve the complete proof, scripts, inputs, and receipts before treating it as canonical continuation state.
