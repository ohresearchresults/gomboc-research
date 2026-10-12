# material-090523011387

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Four-corner clustering with an actual uniform centroid: all-metric U2

## Status, source and purpose

Coordinator analytic theorem, derived from the complete four-matrix regular-tetrahedron certificate in fully read immutable result minimum-0282, SHA-256 0410e1bb8930d18137452b69d75755227faa0c5673c9a4352205a44c4c8fa80e. The argument below is self-contained: it repeats the four small exact matrices and supplies the new multi-cluster perturbation and actual-centroid estimates. No code, numerical experiment or unobserved executable is a premise.

This extends the parent's ONE perturbed basal cluster criterion to simultaneous perturbations of all four corner clusters. It is not a stronger numerical bound for the parent's particular W wedge. It gives a uniform all-metric collar criterion for vertexwise four-corner collapse in the new flag charts, without integrating a separate centroid polynomial on every cell. A limiting hull being tetrahedral is NOT by itself enough: surviving labelled vertices might limit to edge or face interiors rather than to its four corners.

No C600 application, new full-incidence exclusion or complexity improvement is claimed. Canonical C622 and 34<=Cmin<=622 are unchanged.

## Theorem

Let
R0=(1,1,1), R1=(1,-1,-1), R2=(-1,1,-1), R3=(-1,-1,1),
and T=conv(R0,R1,R2,R3). Let P be an actual uniformly filled convex three-polytope such that T is contained in P and every true vertex of P lies within Euclidean distance delta of at least one R_i, where

0<=delta<=1/512.

Let g be the actual uniform volume centroid of P. For every nonzero positive semidefinite matrix M, the actual centred true-edge system has NO weak rooted spanning tree. More quantitatively, for every hypothetical such tree, three of its true arrows can be selected so that

sum_selected (v-g)^T M(w-v) < -(15083/65536) tr(M) < -tr(M)/5.

In particular P, centered at its actual uniform centroid, has at least two strict unstable equilibria for EVERY SPD metric, even if other physical weak equilibria occur. The conclusion is affine invariant when the stated geometric hypotheses and metric are transported together.

## 1. Exact containment bounds determine the actual centroid

The regular tetrahedron has facet inequalities

-R_i dot x <= 1, i=0,1,2,3.

If a vertex v has distance at most delta from some R_j, then each inequality satisfies

-R_i dot v <= 1+||R_i|| delta < 1+2delta

when delta>0. Consequently

T subset P subset sT, s=1+2delta.

The tetrahedron T has centroid zero and every point of sT has norm at most sqrt(3)s<2s. Uniform volume is essential here. Writing V for volume and using the integral over P minus T gives

||g|| <= 2s [V(P)-V(T)]/V(P)
       <= 2s(s^3-1)
       =12delta+48delta^2+64delta^3+32delta^4
       <=13delta.

The final inequality follows for delta<=1/512 from

12+48/512+64/512^2+32/512^3
=12+3/32+1/4096+1/4194304 <13.

For delta=0, P=T and g=0 directly. No freely chosen origin or vertex mass distribution appears. The estimate remains valid when some of the four specified R_i are merely contained points rather than extreme vertices.

Partition the true vertices into the four disjoint corner clusters. They are disjoint because the mutual corner distance is sqrt(8)>2delta. Every cluster is nonempty: otherwise, in the direction of its missing corner R_i, all true vertices would have dot product at most -1+sqrt(3)delta<3, contradicting the containment R_i in P. Write a clustered vertex as

v=R_i+d_v, ||d_v||<=delta,

and its actual centred position as X_v=R_i+d_v-g. Thus all vertices share one centroid error, not four independent origins.

## 2. Complete regular-tetrahedron rooted-tree certificate

For a rooted tree on the four regular corners, define

P0=-sum_(i->j) sym(R_i(R_j-R_i)^T),
where sym(A)=(A+A^T)/2.

There are 64 labelled rooted trees. Orthogonal permutations of the regular tetrahedron reduce them to four rooted forms, with orbit sizes 4,12,24,24. Complete representatives are:

1. Star rooted at its centre, arrows 1->0,2->0,3->0:
P0=((4,0,0),(0,4,0),(0,0,4)).

2. Star rooted at a leaf, arrows 1->0,2->1,3->1:
P0=((4,-2,-2),(-2,4,0),(-2,0,4)).

3. Path rooted at an endpoint, arrows 1->0,2->1,3->2:
P0=((2,-2,-1),(-2,6,-1),(-1,-1,4)).

4. Path rooted internally, arrows 0->1,2->1,3->2:
P0=((2,0,1),(0,6,-1),(1,-1,4)).

The leading principal minors of P0-I/2 are, respectively,

(7/2,49/4,343/8),
(7/2,33/4,119/8),
(3/2,17/4,31/8),
(3/2,33/4,175/8).

All are positive. Hence P0>I/2 for every four-corner rooted tree. Rooted-tree topology and these exact matrices are the entire finite certificate; no unlisted input is needed.

## 3. Simultaneous perturbations of all clusters

Select one actual arrow v->w between distinct groups i,j, put E=R_j-R_i, and write d=d_v, d'=d_w and eta=g. Its actual negative arrow matrix is

P_vw=-sym((R_i+d-eta)(E+d'-d)^T).

Subtract its regular-corner term -sym(R_i E^T). The difference equals

-sym((d-eta)E^T)-sym((R_i+d-eta)(d'-d)^T).

For vectors a,b, the operator norm of sym(ab^T) is at most ||a||||b||. Using ||R_i||<2, ||E||<3, ||d||,||d'||<=delta, and ||eta||<=e, its norm is at most

3(delta+e)+2delta(2+delta+e)
=7delta+3e+2delta^2+2e delta.

Different selected arrows may use different actual endpoints in the same cluster; the estimate never identifies those endpoints. For the three arrows of a four-group rooted tree,

P=sum P_vw
 > [1/2-21delta-9e-6delta^2-6e delta] I.

The actual-centroid bound e<=13delta therefore gives

P > [1/2-138delta-84delta^2] I
  >= [1/2-138/512-84/512^2] I
  = (15083/65536) I
  > I/5.

Every displayed constant is rational and the quadratic loss is increasing for delta>=0. This is the new reusable simultaneous-four-cluster estimate.

## 4. Quotient trees are genuine mechanical obligations

A weak rooted spanning tree on the actual true graph has arrows v->w satisfying

(v-g)^T M(w-v)>=0.

Contract all vertices in each of the four clusters. Every group can reach the root group in the quotient directed graph. It therefore contains a rooted arborescence on the four groups: for example, choose one outgoing edge per nonroot group along a shortest directed route to the root. Select one original true arrow realizing each of its three edges.

For these actual arrows the preceding matrix inequality gives

sum_selected (v-g)^T M(w-v)
=-tr(MP)<-(15083/65536)tr(M)<0

for every nonzero PSD M, contradicting all three weak arrow inequalities. No triangulation diagonal, artificial edge or unrestricted choice of masses has entered the argument.

For SPD M, whenever an actual true edge has a nonnegative outgoing primitive,

||w-g||_M^2-||v-g||_M^2
=2(v-g)^T M(w-v)+||w-v||_M^2>0.

Thus outgoing nonnegative arrows cannot cycle. Every vertex that is not strict U has one such true-edge escape, and any hypothetical unique strict U would generate a weak rooted spanning tree. Its exclusion proves at least two strict U. This makes no assumption about stable equilibria or about absence of other weak contacts. We do not assign equilibrium counts to a singular metric.

## 5. Application boundary for the flag compactification

The source result supplies closed rational flag charts of a fixed polytope's positive-projective orbit, each fixing four independent vertex labels to a standard tetrahedron. A fixed affine map sends that tetrahedron to the R_i above. If EVERY true vertex is shown, on a closed parameter cell, to lie within 1/512 of one of those four fixed corners, this theorem excludes all weak rooted trees on that cell uniformly over nonzero PSD metrics.

For a boundary stratum on which every labelled point is exactly one of those corners, continuity supplies local collars; compact subsets admit a finite union of them. An explicit global collar still requires a verified parameter-to-vertex bound. Merely knowing that the limiting HULL is a tetrahedron is insufficient if some labels land in its edge or face interiors. No new flag-cell coverage count or numeric parameter collar is claimed here.

The full-E17 regular face theta0=0, theta1,theta2,theta3>0 identified by the source does not meet the four-corner-collapse hypothesis merely because raw coordinates approach a plane. It remains an actual mechanical target, not a lower-vertex case removed by this theorem.
