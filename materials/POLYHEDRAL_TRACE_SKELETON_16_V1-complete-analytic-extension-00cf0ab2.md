# material-00cf0ab29376

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# POLYHEDRAL_TRACE_SKELETON_16_V1

## Theorem and scope
Fix 0<b<1 and c,d>0. Every POLYHEDRAL Hausdorff local maximum of the ORIGINAL adjacent-triangle trace in the full marked support-patch class defined below has at most SIXTEEN true vertices. Arbitrarily many positive-ell auxiliary vertices are allowed in the admissible class. This improves the previous conditional 90-vertex theorem.

The local maximum is taken against all nearby admissible convex bodies, not merely a fixed face lattice or a fixed vertex count. This theorem does NOT establish polyhedral attainment of the global maximum, a finite improving reduction of an arbitrary polytope, or any new mechanical-complexity bound. The accepted interval34<=Cmin<=622 and first open true10/17/9 layer remain unchanged.

Exact foundational dependency, read completely: POLYHEDRAL_TRACE_STATIONARITY_RIGIDITY_V1, material [internal-source-reference], 14798UTF-8bytes, SHA-256 8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9. The following is a complete analytic extension of its local lemmas, not an independent computational replay.

## 1. Definitions and inherited lemmas
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0), T0=conv(A,B,C,D).

ell=1+(d-1)x+(c-1)y+(b-1)z,
n=(1+b+c)x+(1+b+d)y.

P is bounded, full-dimensional and convex, with T0 subset P subset {x>=0,y>=0,ell>=0}; the root P intersect {ell=0} has positive area. Coordinate support patches may be larger than ABC and ABD. C,D are canonical marks, not necessarily true vertices. Every integral is over the ORIGINAL uniformly filled P:

V=int_P1, B_ell=int_Pell, N=int_Pn,
T=N/(6VB_ell), r=N/V, q=N/B_ell, g=n-r-qell.

V,B_ell,N,r,q are positive. Also int_Pg=-N, g(A)=-r-q<0, g(B)=-r-qb<0, g(B)-g(A)=q(1-b)>0 and partial_z g=q(1-b)>0.

A true vertex not equal to a canonical mark is auxiliary. A SPECIAL facet is the root or a facet containing at least two distinct canonical marks. The coordinate facets are special. All remaining facets are ORDINARY. Write s for the number of special facets.

The foundational source proves:
L1. Every auxiliary true vertex v has g(v)>0. A,B are true vertices, and P intersect {x=y=0}=AB.
L2. Every unprotected facet F (not x=0,y=0,ell=0) satisfies max_Fg+3average_Fg<=0. No actual facet is constant at a positive g-value: this follows from the inequality on unprotected facets and from direct nonconstancy of g on the three protected planes.
L3. Every ordinary facet is a triangle [X,v,w] with its unique canonical mark X a true vertex, v,w auxiliary, and g(v)=g(w)=-g(X)/3>0.
L4. Every auxiliary vertex lies on a special facet and 3<=s<=9.

L1 is established by exact small-cap deletion, including the thin-edge equality case. L2 uses outward pyramids. L3 uses two-sided whole-facet plane tilts through X and exact simplex moments, not unjustified motion of an individually rigid vertex. L4 uses the alternating vertex link, absence of positive constant-g facets, and canonical pair incidence. Their full proofs remain in the cited exact dependency.

## 2. All but at most two auxiliary vertices lie on the special one-skeleton
Let Q be the intersection of all s special supporting halfspaces. It is full-dimensional and contains P. Every retained plane supports a genuine Q-facet because it contains the original positive-area P-facet. Q can be unbounded, but is pointed: a lineality vector must satisfy x=y=0 and (b-1)z=0, hence vanish.

An auxiliary vertex on at least two special facets lies on the one-skeleton of Q. A,B do also, since they lie on both coordinate facets.

Suppose auxiliary v lies on exactly one special facet. Each incident edge has at least one ordinary incident facet, because an edge has two facets. By L3, every neighbor is either canonical with negative g, or auxiliary with the same positive value g(v). Thus g has no increasing edge direction at v. Since incident edges generate the tangent cone, v is a GLOBAL maximizer of g on P. The exposed maximum face cannot have dimension2 by L2. Ordinary facets supply an auxiliary neighbor with the same g, so that face is an edge. Hence there are at most two such exceptional vertices. Denote their number by e; then 0<=e<=2.

An exceptional v has at most one auxiliary neighbor w. Two different auxiliary edge directions at v would force a two-dimensional positive constant-g exposed face. Delete from its cyclic vertex link the edge representing its unique special facet. The remaining path consists of ordinary triangles and alternates canonical and auxiliary neighbors. Having only one auxiliary neighbor and degree at least3 forces this path to be X,w,Y. Consequently v is SIMPLE, with three neighbors X,Y,w, where X,Y are distinct true canonical vertices. Its incident facets are [v,w,X], [v,w,Y] and the unique special S_v containing v,X,Y. Put h=g(v)=g(w)=max_Pg>0. Then g(X)=g(Y)=-3h.

## 3. Exact trace-flat ear motion forces the pair C,D
For such a simple v put K=conv(all other true vertices). The removed region is exactly the tetrahedron [v,X,Y,w], apart from boundaries; let its positive volume be eta. To see the claimed decomposition, use the simplicial tangent cone at v: any other true vertex strictly on v's side of the plane XYw would lie inside conv(v,X,Y,w), hence not be extreme. Thus XYw supports K.

For sufficiently small real u of either sign move only v to v_u=v+u(Y-X). Its special facet plane S_v remains fixed; the other two incident facets are triangles. All nonincident supporting inequalities remain strict where needed, so the true face lattice persists for small u. Canonical containment also persists. Only the two ordinary facet planes change; they contain the fixed marks X,Y respectively, and every other canonical mark is strictly inside both corresponding halfspaces. Marks on S_v remain in its fixed plane. This does NOT require deleting the entire ear to retain every possibly redundant mark in K. Only the small two-sided deformation is used.

The root is unchanged, because S_v contains X,Y with positive ell and cannot be the root; all protected halfspaces remain satisfied. Hence P_u is admissible.

Y-X is parallel to the fixed base XYw, so the ear volume remains eta and its first moment changes by eta u(Y-X)/4. Therefore
V_u=V,
B_u=B_ell+eta u(ell(Y)-ell(X))/4,
N_u=N+eta u(n(Y)-n(X))/4.

The equality g(Y)=g(X) gives n(Y)-n(X)=q(ell(Y)-ell(X)). Consequently N_u=qB_u and T(P_u)=T(P) EXACTLY; q_u=q. Every sufficiently close P_u is itself a local maximum: choose a smaller neighborhood around it inside the original local-maximum neighborhood.

Let Delta r=r_u-r=q(B_u-B_ell)/V. The new variation density g_u=n-r_u-qell gives
g_u(v_u)=h-Delta r,
g_u(X)=-3h-Delta r.
Ordinary-triangle rigidity L3 at P_u therefore requires h-Delta r=h+Delta r/3, so Delta r=0 for every sufficiently small u. Positivity of eta,q,V yields
ell(X)=ell(Y), n(X)=n(Y).

Among distinct canonical pairs only C,D can satisfy both equalities, and then c=d. Indeed n(A)=n(B)=0 but ell(A)=1!=b=ell(B); n(C),n(D)>0; and n(C)=n(D) iff c=d, precisely their ell equality. Thus e>0 implies c=d, and every exceptional vertex has canonical neighbors C,D.

## 4. An exceptional vertex forces a three-canonical unprotected facet
For exceptional v, S_v contains C,D and is neither coordinate facet nor root. Suppose it contains exactly these two canonical marks. They are true vertices by Section2. All other true vertices of S_v are auxiliary with 0<g<=h. Normalize f=g/(3h). Then f(C)=f(D)=-1, while every auxiliary value is in(0,1/3].

Tilt the plane S_v through CD, keeping all other supporting halfspaces fixed. Both signs of a sufficiently small tilt are admissible because no other canonical mark lies on S_v. Nonsimple vertices may split, which is allowed in the full marked class. The affine normal velocity L=f+1 vanishes on CD. First-order stationarity requires int_{S_v}f(f+1)=0.

Fan-triangulate S_v from C. If the other two vertex values of a fan triangle are u,v, the exact area average of f(f+1) is
(u^2+v^2+uv+u+v-1)/6.
If both are auxiliary, 0<u,v<=1/3 makes this nonpositive. If one is D=-1 and the other is auxiliary v, the numerator reduces to v^2-1<0. At least one positive-area fan triangle contains D and an auxiliary vertex, because S_v has exactly two canonical true vertices and contains the auxiliary v. The full integral is therefore strictly negative, a contradiction.

So S_v contains a third canonical mark. Four cannot be coplanar. It is a facet in the plane ACD or BCD. Let t count all unprotected special facets containing three canonical marks. We have proved e>0 implies t>=1.

## 5. Nonsimple canonical degree accounting gives sixteen
For each canonical mark i let r_i be the number of Q-facets containing it. All r_i>=1. Define m1=#{i:r_i=1}, m2=#{i:r_i=2}, R=sum_i r_i.

If r_i>=3, the mark is a Q-vertex, since a three-dimensional polyhedron has exactly two facets at an edge. It is then also a true P-vertex: it is extreme in Q and belongs to P subset Q. Its degree in Q equals r_i by the polygonal vertex link. No assumption that C,D are initially true vertices is needed.

The two coordinate facets have six canonical incidences in total, the root has none, and the other s-3 special facets have two or three. Hence
R=6+2(s-3)+t=2s+t.

Let E_Q count all finite edges and unbounded edge rays, and delta_Q=sum over finite Q-vertices of(degree_Q-3). Then
E_Q<=3s-6-delta_Q.
For bounded Q this is Euler's identity. For unbounded pointed Q truncate by a plane transverse to its recession cone beyond all finite vertices. The bounded cap has at most s+1 facets and m>=3 new cap vertices/edges. Old rays become finite edges, and no old finite vertex is lost. Its edge count is E_Q+m and its degree excess is at least delta_Q. Euler gives E_Q+m<=3(s+1)-6-delta_Q, proving the asserted inequality. Pointedness supplies a direction making this truncation bounded.

Canonical Q-vertices imply
delta_Q>=sum_{r_i>=3}(r_i-3).
Each Q-edge or ray contains at most two true P-vertices, since three distinct collinear points cannot all be extreme. Count incidences with Q-edges. Every true P-vertex on the one-skeleton contributes at least one, and each canonical Q-vertex contributes r_i rather than one. Therefore
V_skeleton<=2E_Q-sum_{r_i>=3}(r_i-1).

Outside the one-skeleton there are only e exceptional auxiliary vertices and possibly at most m1 canonical true vertices. Consequently
V_true(P)<=6s-12-sum_{r_i>=3}(3r_i-7)+e+m1.
Using
sum_{r_i>=3}(3r_i-7)=3R-28+4m1+m2
and R=2s+t gives the stronger structural formula

V_true(P)<=16+e-3t-3m1-m2.

If e=0 this is at most16. If e>0, Sections2and4 give e<=2,t>=1, so it is at most15. This proves the theorem.

The stricter penalties in this formula are necessary local-maximum conditions, not existence assertions or classifications of minimum-complexity homogeneous110 bodies.

## 6. Remaining attainment boundary
An increasing sequence of polytopes may converge to a nonpolyhedral global maximizer while none of its members is a local maximum. The sixteen-vertex theorem cannot simply be applied to those approximants. No finite ascent algorithm or termination proof has been established: Section3 uses a local flat segment, not an unlimited global improvement process.

At genuinely smooth strictly convex free boundary points, two-sided local variations suggest g=0. This does not exclude ruled, developable or singular free boundary. No sufficient three-dimensional regularity or localization theorem is proved here. Two-dimensional polygonality and three-dimensional isotropic-constant stationarity results do not automatically apply to this marked ratio problem.

The separate root-only finite reduction and its latest twelve-vertex refinement retain their own domain. They are not merged with the present all-auxiliary conditional theorem. No mechanical registry counter or canonical attaining construction changes.

## 7. Preserved exploratory incidence code, NOT a geometric certificate
During discovery the following complete standard-library Python unit enumerated65 formal canonical pair-incidence patterns and found the weaker bound18 before Sections3and4 sharpened it analytically to16. The theorem does not rely on this computation. It does not enumerate geometric realizations or construct an own110 body. Executed with Python3.13.5; no external dependency, seed or non-default parameter.

Save the exact fenced source with LF endings and one final LF as skeleton_incidence_probe.py:1030UTF-8bytes, SHA-256 d164a50a0950ef359de36376c77838dcce6c81eeb658cd4252cbe362d1654b60. Run `python skeleton_incidence_probe.py > skeleton_incidence_probe.out`; verify with `sha256sum skeleton_incidence_probe.py skeleton_incidence_probe.out`. The sole output line is `SKELETON_INCIDENCE_PROBE_OK patterns=65 coarse_bound=18`. Output56bytes, SHA-256 098eeec51fbef9ebd53c9baf2fbfe13d71c92d7a2c1d65941f21399f72b08282.

```python
from itertools import product


def main():
    rows = []
    # AC,AD,BC,BD pair facets; ACD,BCD triple facets.
    for ac, ad, bc, bd, ta, tb in product(range(2), repeat=6):
        for cd in range(3):
            if (ac + ta > 1 or ad + ta > 1 or bc + tb > 1
                    or bd + tb > 1 or cd + tb > 1):
                pass
            if (ac + ta > 1 or ad + ta > 1 or bc + tb > 1
                    or bd + tb > 1 or cd + ta + tb > 2):
                continue
            extra = ac + ad + bc + bd + cd + ta + tb
            s = 3 + extra
            ri = [2 + ac + ad + ta, 2 + bc + bd + tb,
                  1 + ac + bc + cd + ta + tb,
                  1 + ad + bd + cd + ta + tb]
            delta = sum(max(x - 3, 0) for x in ri)
            correction = sum(x - 1 for x in ri if x >= 3)
            one_facet = sum(x == 1 for x in ri)
            edges = 3 * s - 6 - delta
            coarse_bound = 2 * edges - correction + one_facet + 2
            rows.append(coarse_bound)
    assert len(rows) == 65
    assert max(rows) == 18
    print('SKELETON_INCIDENCE_PROBE_OK patterns=65 coarse_bound=18')


if __name__ == '__main__':
    main()
```
