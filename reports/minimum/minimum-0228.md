# minimum-0228

AI research report · 2026-09-24 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# FULL_MANIFOLD_PHYSICAL_CONTACT_SECTORS_AND_E17_EIGHT_REST_ESCAPE_V1

## 1. Main findings and scope

The full same-lattice problem admits a smaller and more faithful local formulation than independently perturbing vertex coordinates, facet poles and two metrics. I derive an exact actual-centroid tangent system, a complete physical-contact sector selection rule, a conormal stress alternative, a moment-based incidence-peeling sufficient condition, and a second-order escape alternative that includes the actual nonlinear centroid equations.

For an actual weak-inclusive S1U1 body on V10/E17/F9, the complete **strict first-jet** regularization question reduces to at most **256 strict linear systems, each with at most17 rows in16 effective variables**. These are physical-contact choices, not arbitrary zero primitives or selected spanning trees. Feasibility is proved sufficient for an actual analytic same-lattice regularization; it is not inferred from parameter counting. Infeasibility supplies an exact full-manifold stress, but does not by itself exclude higher-order regularization.

A new exact E17 control demonstrates a substantive difference from the projective-affine problem. It has **four simple VE/A contacts and four simple EF/B contacts**, all genuinely physical and mutually distinct. Its eight escape functions have **rank eight on the full actual-centroid realization manifold**. Consequently every one of the256 local sign chambers is genuinely realizable on the same lattice, with one fixed physical metric and its inverse. An explicit rational coordinate–metric path removes all eight contacts linearly for the entire interval0<t<=1/100, while preserving every original labelled strict equilibrium. Its four primal contacts nevertheless have a nonnegative first-order stress against **every projective-affine deformation**, including the correct projective centroid derivative.

The path is not merely a reparametrized projective example: for every t>0 it is not a labelled projective image of its starting body. A six-contact companion is also preserved, with a Euclidean rational-coordinate path and64 genuine local sign chambers.

**Neither control is S1U1.** Both start with strict(S,U,H)=(5,6,9), retain those counts along their positive paths, and become physicalweak000. Thus no proper110 attainer, universal proper110-density theorem, whole E17 exclusion or change to34<=C_min<=622 follows. What is settled is a full-manifold finite first-jet mechanism and an actual mixed-eight-contact escape beyond a projective-affine first-order obstruction.

## 2. Source authority and reading

I read both new supplied files consecutively through EOF before the research:

```
FIRST_LAYER_23_VARIABLE_CLOSED_ATLAS_AND_REALIZATION_REGULARITY_V1(1).md
19651 bytes
SHA256 dcf2cf5c0aa9fdcc106b5375502e4fe198b43833ae0b70405698f082e6bf770a

research-journal(20260924-144518).md
241324 bytes
SHA256 f4bb7e8bb95115fa1c74a572c65b36b0ca8245f88137ff148cef76b477f5e31b
```

The mathematical starting source is `[internal-source-reference]`. Its actual closed atlas and everywhere-full-rank incidence Jacobian are working premises, not an independent-replay task. In particular, it explicitly leaves mechanical strict feasibility unresolved; maximum-simplex ties are chart boundaries, not intrinsic restrictions on local physical motion. :contentReference[oaicite:0]{index=0}

The shared journal already records actual same-lattice regularization for all at-most-three physical weak points, along with narrower later special configurations. I do not relabel those as new results. The present mixed-eight example is different, and its entire exact construction below has no dependency on an earlier worker's source or sandbox. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

No missing exact dependency affects this handoff. The global S1U1 existence and proper110-density questions remain separate, as in the supplied branch memory. :contentReference[oaicite:3]{index=3}

## 3. Complete physical-contact sectors: VF requires two crossed escapes

Use true vertices x_i at the actual uniform centroid0, true same-origin poles q_f, and one physical pair M,N=M^-1. Define

```
D_ij=x_i^T M(x_j-x_i),
E_fg=q_f^T N(q_g-q_f).
```

A true edge ij incident to facets f,g has packet(D_ij,D_ji,E_fg,E_gf). Strict saddles have all four entries negative. Physical weak packets have all four nonpositive with a zero. A zero in a packet with another positive entry is harmless and must not automatically become a regularization constraint.

The complete local contact types are simple A, simple B and VF. A weak vertex exposes either one true edge, giving its unique simple A zero, or a true facet, giving VF. A weak facet foot lies either in the interior of a true edge, giving simple B, or at a vertex, giving VF. Opposite primitives cannot both vanish: D_ij+D_ji=-|x_j-x_i|_M^2<0, and similarly on the polar. A packet containing both a primal and a polar zero is VF: the edge projection is its endpoint, and the facet foot is the same uniquely determined edge projection.

At a VF point x_i on facet f, let the two edges of f at i be ij_1,ij_2, with other incident facets g_1,g_2. Write the four zero primitives

```
a=D_(i,j1), b=D_(i,j2), c=E_(f,g1), d=E_(f,g2).
```

All opposite packet primitives, all other outgoing primitives at i, and all other outgoing primitives at f are strictly negative at the VF point. In a sufficiently small neighborhood, preserving these strict signs, removal of this physical point **without adding a strict U, S or H** is equivalent to

```
(a>0 or b>0) and (c>0 or d>0)
and (a>0 or c>0) and (b>0 or d>0).
```

The first two clauses prevent a new vertex/facet equilibrium; the last two prevent either edge from becoming a saddle or remaining weak. Boolean simplification gives the exact two-sector rule

```
(a>0 and d>0) OR (b>0 and c>0).                    (3.1)
```

Thus one does not independently choose one arbitrary zero on each of the two VF edges. The choices must also remove the weak vertex and weak facet. Requiring all four zeros positive is sufficient but unnecessarily restrictive.

For simple A require its single zero D>0; for simple B require its single zero E>0. Apply(3.1) independently at each VF point. Preserve the old strict signs and one old positive escape wherever a feature was already excluded. This finite sector family is necessary and sufficient, locally, for retaining the original labelled strict S/U/H sets and removing all weak rests. Harmless zeros may remain.

There is also an intrinsic two-dimensional VF first-jet identity. In Euclidean physical coordinates put rho=|x_i|^2, so q_f=x_i/rho. For compatible vertex/pole velocities u_i,v_f let w=u_i-rho v_f. Linearized incidence gives

```
a'=e_1.w, b'=e_2.w,
c'=-(q_g1-q_f).w/rho,
d'=-(q_g2-q_f).w/rho.                              (3.2)
```

All four directions lie in x_i-perp, so these four covectors have rank two, not four. That rank is genuinely available: an infinitesimal symmetric physical metric change can prescribe the tangential part of w arbitrarily. This does not imply simultaneous feasibility at several contacts. At a right-angle facet corner, the two rows of an individual crossed sector may even be positive proportional rows; the sector formulation handles this without a false independence assertion.

For E17 with sole strict U and S, if there are k_A,k_B,k_C physical A,B,VF points, then

```
k_A+k_C<=9, k_B+k_C<=8,
k_A+k_B+2k_C<=17, k_C<=8.                          (3.3)
```

A weak vertex and a weak facet each support only one physical point. Hence there are at most2^8=256 crossed-sector choices, each with at most17 required positive primitive functions.

## 4. Full actual-centroid tangent and stress theorem

### 4.1 Absorb the common metric without losing its inverse

Locally choose an analytic B with B^T B=M and replace

```
x_i by B x_i, q_f by B^-T q_f.
```

Both mechanical primitive families are then Euclidean. This is an actual affine change of the uniformly filled body, carrying its actual centroid; it is not an independent recentering or filling of the polar. Time-dependent B also absorbs a varying physical metric. Thus the full11-shape-plus5-metric problem is equivalent to Euclidean own-centred realization space modulo rotations and homothety.

In the rest of the analytic derivation take M=N=I. The exact control uses an equivalent rational constant-M representation to avoid hiding its algebraic Euclidean scaling.

Let z=(x_i,q_f), and impose

```
q_f.x_i=1 on every true incidence,
J(x)=sum_T det(x_a,x_b,x_c)(x_a+x_b+x_c)=0,          (4.1)
D(x)=sum_T det(x_a,x_b,x_c)>0.
```

T is one outward triangulation of the true maximal facets. It is only an integration device. In the genuine same-lattice neighborhood, J/(4D) is the actual volume centroid. The incidence Jacobian has rank2E by the supplied theorem. The three centroid equations add rank three because translations preserve incidence and move the actual centroid arbitrarily. At E17 this gives57 variables,37 independent equations, a20-dimensional centred manifold, and16 dimensions after removing three rotations and one homothety. This quotient is the same physical16-dimensional space as the source's11+5 description, not extra shape freedom.

### 4.2 Actual facet second moments give the centroid derivative

At the centred body define

```
d_f=Area(F_f)/(Vol(P)*|q_f|),
T_f=mean_(F_f) xx^T,
C_f=d_f T_f.
```

Every C_f is SPD. A nonzero linear functional cannot vanish on a two-dimensional affine facet plane not through0.

For compatible pole velocities v_f, the normal velocity of the actual moving facet at x is -(v_f.x)/|q_f|. Integrating the true boundary layers gives

```
g'=-sum_f C_f v_f.                                 (4.2)
```

There is no free mass or independent triangle motion in this formula. In particular, the full tangent is exactly

```
q_f.u_i+x_i.v_f=0 on every incidence,
sum_f C_f v_f=0.                                   (4.3)
```

The identity sum_f C_f q_f q_f^T=I checks the translation response: v_f=-(q_f.a)q_f gives the second expression in(4.3) equal to-a.

All matrices are exactly reconstructible from the true fan. With D=6Vol and, for each facet triangle, delta=det(a,b,c), s=a+b+c,

```
C_f=(1/(4D))*sum_(triangles in f)
       delta*(s s^T+a a^T+b b^T+c c^T).             (4.4)
```

The verifier independently compares this surface-moment tangent with the direct derivative of the quartic J in(4.1).

### 4.3 Exact first-order escape alternative

Fix one of the physical sectors in Section3, with required zero functions f_l. Their covectors are

```
A i->j: (x_j-2x_i).u_i+x_i.u_j,
B f->g: (q_g-2q_f).v_f+q_f.v_g.                    (4.5)
```

Let K be the linear system(4.3), Z any basis of ker K, and R the matrix of(4.5) restricted to that basis. Then exactly one of the following holds:

```
ESCAPE: some w has Rw>0 in every row;
STRESS: some lambda>=0, lambda!=0 has R^T lambda=0. (4.6)
```

This is a finite exact linear alternative. One elementary proof separates0 from the convex hull of the row covectors: if0 is absent, its nearest point has strictly positive pairing with every row; if0 is present, its convex representation is the stress.

In the escape case, the analytic implicit-function theorem for(4.1) integrates Zw to an actual same-lattice own-centred curve. All selected functions become positive to first order. The finite old strict guards persist, so Section3 proves complete weak-rest removal with no added or lost labelled strict equilibria. If the starting body has strict S=U=1 and H=0, this gives a proper110 germ.

Conversely, any differentiable regularization with strictly positive first derivatives in this sector supplies the escape vector. The qualifier about first derivatives is essential: a higher-order or contact-preserving premove can succeed even when(4.6) returns a stress.

The covectors annihilate the four similarity directions, so they live in a16-dimensional space at E17. A minimal stress has at most17 selected rows. This is not an argument that17 or fewer inequalities are feasible; the exact signs in(4.6) decide it.

For rational actual coordinates and metric, the systems and alternatives are rational. A feasible strict cone contains a rational vector; an infeasible system has a rational normalized nonnegative dependence. A numerical near-nullspace is not a certificate.

### 4.4 Full reaction equations: what a genuine obstruction must contain

For contact weights lambda define vertex and pole forces

```
F_i^A=sum_(i->j) lambda_ij(x_j-2x_i)
                  +sum_(j->i) lambda_ji x_j,
F_f^B=sum_(f->g) lambda_fg(q_g-2q_f)
                  +sum_(g->f) lambda_gf q_g.
```

The stress in(4.6) is equivalent to existence of real incidence reactions omega_if and a vector c such that

```
F_i^A=sum_(f incident i) omega_if q_f,
F_f^B=sum_(i incident f) omega_if x_i+C_f c.          (4.7)
```

The reactions are not physical masses, and c is a multiplier, not a selectable false centroid. The same actual matrices C_f occur at every facet. These equations are the full-manifold obstruction; an affine contact-tensor dependence alone is weaker.

Testing(4.7) on genuine affine motions also gives the necessary common-metric balance

```
sum_A lambda sym[x_i(x_j-x_i)^T]
 =sum_B lambda sym[q_f(q_g-q_f)^T].                 (4.8)
```

Equation(4.8) alone omits the nonaffine reactions and actual centroid block and must not replace(4.7).

## 5. A moment–incidence peeling sufficient condition

Here is a structural consequence of(4.7) that can avoid a large tangent calculation. It applies to arbitrary genuine3-polytopes and mixed sectors, not only the control below.

Mark both vertex endpoints of every selected A row and both facet/pole endpoints of every selected B row. Start with the true bipartite vertex–facet incidence graph.

First delete all edges at any unmarked vertex node with at most three remaining neighbors. They carry zero omega in every possible stress, because that node has F_i^A=0 and any at most three incident poles are linearly independent. Let H be the remaining graph. For every unmarked facet node form

```
L_f=C_f^-1 span{x_i:(i,f) is an edge of H},
L=intersection_(unmarked f) L_f.                   (5.1)
```

An empty span is{0}; an intersection over no facets supplies no restriction. Equation(4.7) forces c in L. Therefore L={0} kills the centroid multiplier. This can happen by an intersection of several proper subspaces even when no single facet is isolated and no independently movable free facet has been assumed.

Once c=0, repeatedly delete edges at any unmarked vertex OR unmarked facet node with at most three remaining neighbors. Again the corresponding omega entries vanish, using the primal or polar three-vector independence. **If all edges are deleted, the selected sector has a strict first-order escape.**

Proof of the last step is not parameter counting. If a stress survived, all omega and c would now vanish, hence both force families would vanish. But a nonempty positive-weight A contact graph is acyclic: at a zero contact, |x_j|^2=|x_i|^2+|x_j-x_i|^2. Choose its greatest-radius participating target j. It has no outgoing positive-weight contact and at least one incoming contact, so

```
x_j.F_j^A=sum_(i->j) lambda_ij |x_i|^2>0.
```

Thus F_j^A cannot vanish. The identical argument on the actual poles handles a nonempty B graph. At least one graph is nonempty, contradicting(4.7). QED.

Failure of this peeling test is not an obstruction: the remaining reactions might still have no nonnegative contact weights. The exact alternative(4.6) remains decisive at first order. Conversely, any full stress must survive this actual-moment test through a nonzero allowed centroid multiplier or a nonempty remaining marked incidence subgraph. This distinguishes genuine full-manifold resistance from a tensor-only artifact.

## 6. Second-order escape with all actual nonlinear terms retained

Use the exact polynomial constraints F=(incidences,J) in(4.1), not a frozen version of C_f. Let A=DF(z0), and let G_l=df_l(z0). Choose a tangent v satisfying

```
Av=0, G_l v>=0.
```

Let I0 be the selected rows with G_l v=0. A sufficient and exact acceleration test for this v is

```
Aw=-D^2F[v,v],
G_l w+D^2f_l[v,v]>0 for l in I0.                   (6.1)
```

It is equivalent to the following stress-curvature condition: for EVERY nonzero lambda>=0 supported on I0 such that

```
sum_l lambda_l G_l=mu^T A,
```

one has

```
sum_l lambda_l D^2f_l[v,v]-mu^T D^2F[v,v]>0.        (6.2)
```

A has full row rank, so mu is uniquely determined by lambda. Normalize sum lambda=1; the possible weights form a compact polytope, and checking its extreme points is sufficient. With no such weights, the test is vacuous and an acceleration exists.

To prove equivalence, solve the first equation of(6.1), write all accelerations as w0+ker A, and apply the finite strict affine inequality alternative to the remaining rows. Multiplying by a stress eliminates the free acceleration and gives exactly(6.2), with its displayed sign.

Compatible v,w are the first two derivatives of a genuine analytic curve in F=0: use a local implicit chart and a quadratic path in its free coordinates. Rows outside I0 are already positive to first order; rows in I0 are positive to second order. The old guards persist as before.

The data in this test are completely explicit. For vertex/pole velocity components u_i,v_f,

```
D^2(q_f.x_i-1)[v,v]=2u_i.v_f,
D^2D_ij[v,v]=2u_i.(u_j-u_i),
D^2E_fg[v,v]=2v_f.(v_g-v_f).
```

Obtain D^2J[v,v] by expanding the actual quartic triangle sum in(4.1). This includes changing volume and centroid, not just fixed reference contacts. Working with actual reciprocal poles after the physical coordinate change includes the inverse-metric higher-order effects; q is not an independent second physical metric.

Failure for one v excludes only that acceleration direction. Failure of first-order escape is not a universal higher-order obstruction, and no claim is made that second order always suffices. The complete positive stress cone, rather than one convenient weighted Hessian, is required in(6.2).

## 7. Exact E17 mixed-eight construction

### 7.1 Coordinates, lattice and actual centroid

Use raw coordinates

```
Y0=(1,t,0)       Y1=(1,h,0)
Y2=(-t,1,0)      Y3=(-h,1,0)
Y4=(-1,-t,0)     Y5=(-1,-h,0)
Y6=(t,-1,0)      Y7=(h,-1,0)
Y8=(-1,0,z)      Y9=(1,0,z).
```

The outward maximal facets, in the permanent labels used everywhere below, are

```
F0=(0,7,6,5,4,3,2,1)
F1=(0,1,9)       F2=(0,9,7)       F3=(1,2,9)
F4=(2,3,8,9)     F5=(3,4,8)       F6=(4,5,8)
F7=(5,6,8)       F8=(6,7,9,8).
```

Their boundary cycles give the complete true edges

```
01,07,09,12,19,23,29,34,38,45,48,56,58,67,68,79,89.
```

There are16 face-fan integration triangles, not additional mechanical edges.

Put K=ht+h-t+2. Direct integration of this same uniformly filled solid gives

```
6Vol=4zK,
g=(0,0,z(K+1)/(4K)),
X_i=Y_i-g.                                        (7.1)
```

For the main eight-contact path choose

```
h=1/4, z=1-t, 0<=t<=1/100,
M=diag(1,1,36/17), N=diag(1,1,17/36).
```

Thus

```
Vol=(3-t)(1-t)/2,
g_z=(1-t)(13-3t)/(12(3-t)),
g_z(0)=13/36, g_z'(0)=-35/108.                     (7.2)
```

This is a rational coordinate–metric pair. Its literal Euclidean physical body is diag(1,1,6/sqrt(17))X_i, an exact algebraic body; I do not call that Euclidean coordinate array rational. The affine image remains uniformly filled and has actual centroid0. At t=1/100, the raw volume is29601/20000 and raw centroid height42801/119600.

### 7.2 All eight physical points at t=0

At t=0 there are exactly eight zero true-edge primitives:

```
A: D01=D23=D45=D67=0,
B: E12=E34=E65=E78=0.
```

All other60 primitives are strictly negative. The four A points are the actual vertices0,2,4,6. The four B feet, in centred coordinates, are

```
F1: (1,0,0),              edge09, fraction13/36 from0;
F3: (3/7,4/7,17/252),     edge29, fraction3/7 from2;
F6: (-1,0,0),             edge48, fraction13/36 from4;
F7: (-3/7,-4/7,17/252),   edge68, fraction3/7 from6.
```

They lie strictly inside their true edges. These are eight distinct physical points, four simple A and four simple B, with **no VF** and no harmless zero substituted for a contact.

The strict sets are

```
S={0,2,4,5,8},
U={1,3,5,7,8,9},
H={07,12,19,34,38,56,58,79,89}.                    (7.3)
```

### 7.3 Explicit linear removal on the entire interval

Along the actual-centroid path(7.2), all four A functions are

```
D01=D23=D45=D67=t(1/4-t).
```

The first pair of B functions is

```
E12=E65=t(23-9t)/(48+9t-7t^2).
```

The second pair is

```
E34=E78=
144t(3-t)^2(108t^4-420t^3+441t^2-122t+61)
/[(1-t)^2(23-9t)(131-22t-9t^2)^2].                 (7.4)
```

Their first derivatives, in the order A01,A23,A45,A67,B12,B34,B65,B78, are

```
(1/4,1/4,1/4,1/4,23/48,79056/394703,23/48,79056/394703).
```

Every entry is positive. The exact continuum certificate proves, throughout0<t<=1/100,

```
every one of the eight opened primitives >19t/100,
every original nonzero primitive has |value|>=3/50
and retains its original sign.                    (7.5)
```

All true supports, vertex extremality and strict polygon-cycle guards persist. Hence the entire path has exactly the strict sets(7.3), all68 primitives nonzero and physicalweak000. No generic perturbation or point sampling is used to certify this interval.

### 7.4 Full-manifold rank eight and all256 chambers

At t=0 the exact57-variable Jacobian of the34 incidences and three actual-J equations has rank37. Appending the eight rows in the order above gives rank45. In variable order

```
x0x,x0y,x0z,...,x9z,q0x,q0y,q0z,...,q8z,
```

a nonzero45-column minor uses columns0 through40 inclusive and42,45,47,51. Its exact determinant is

```
-77674658591966564719177771253760
/110097756446869307426503067797.                    (7.6)
```

Both SymPy's exact determinant and independent standard-library Fraction elimination reproduce(7.6). The code checks the actual moment-gradient rows against(4.2), not a freely specified centroid.

Therefore the eight contact functions are a submersion on the genuine20-dimensional centred manifold, and also on a16-dimensional physical similarity slice. Every sufficiently small prescribed eight-tuple of contact values is attained by an actual nearby same-lattice homogeneous body at its own centroid, at this same fixed M,N.

For a complete exact implicit reconstruction, freeze the twelve nonpivot variables at their displayed baseline values and solve

```
incidence equations=0,
J=0,
(eight contact functions)=epsilon*sigma,
sigma in{-1,+1}^8.
```

The nonsingular minor(7.6) selects the unique local analytic solution. Equivalently, write the45 pivot coordinates as z0+sum_(n>=1) z_n epsilon^n. The first coefficient solves the fixed45x45 Jacobian system with right side(0_37,sigma). At order n>1, substitute the earlier coefficients into the same37 polynomial constraints and eight contact functions, take the epsilon^n residual, and solve the same matrix against its negative. This is a deterministic rational Taylor reconstruction, convergent by the analytic implicit-function theorem. Its values need not be rational at rational epsilon.

If a of the four A signs and b of the four B signs are negative, the corresponding chamber has

```
(S,U,H)=(5+b,6+a,9+a+b), physicalweak000.            (7.7)
```

This gives all256 genuine local chambers. The executable enumerates their complete labelled sign/census table; actual realizability comes from the proved submersion, **not** from pretending those sign assignments are256 separately enumerated rational bodies. The common implicit neighborhood is not quantitatively evaluated. The explicit positive path already has the evaluated interval(7.5).

### 7.5 The projective-affine first-order obstruction is real but not structural

At the starting body let e_i be the four A displacements and x_i their sources. Exact identities are

```
sum e_i=0,
sum sym(x_i e_i^T)=0,
|x_i|_M^2=781/612 for all four,
sum |x_i|_M^2 e_i=0.                              (7.8)
```

A metric/affine first variation H contributes x_i^T H e_i, whose sum vanishes. For a genuine uniformly refilled projectivity x/(1+s p.x), at an actual centred body let L=5Sigma. At a zero A contact, the correct derivative is

```
D_i'=p^T L M e_i-|x_i|_M^2 p.e_i.
```

Its sum also vanishes by(7.8). Thus no projective-affine first jet can make all four A derivatives positive, even with the correct moving uniform centroid and arbitrary simultaneous metric variation. A frozen-centroid explanation is not involved.

The new path instead gives all four derivatives1/4, so its full nonaffine direction escapes this restriction. This does not rule out a higher-order projective-affine rescue by another path.

There is also exact finite geometric separation: vertices1,3,5,7 are fixed along the path and form a projective frame in the base plane. Any labelled projectivity between the starting and moving body fixes those four points and therefore acts as the identity on that plane. But vertex0 moves from(1,0,0) to(1,t,0). Consequently no such labelled projectivity exists for t>0. No unlabelled projective classification is claimed.

### 7.6 Preserved six-contact Euclidean rational companion

Set h=1/2,z=1,M=N=I in the same full generator. Then

```
Vol=(5-t)/3,
g_z=(7-t)/(4(5-t)),
g_z(0)=7/20, g_z'(0)=1/50.
```

At t=0 there are four physical A contacts01,23,45,67 and two physical B contacts12,65. The B feet are(1,0,0),(-1,0,0), at fraction7/20 on09 and48. All other62 primitives are nonzero. The strict sets remain(7.3).

The exact opening functions are

```
D_A=t(1/2-t),
E12=E65=t(13-3t)/(40+19t-5t^2).
```

The full interval0<t<=1/100 is again weak-free, with the same strict sets. The contact rank is six; a43-column augmented minor uses0 through39 inclusive and42,45,47 and equals

```
819200000000000/10388388653643.
```

All64 local sign chambers are therefore actual; formula(7.7) applies with b between0 and2. This companion is a rational Euclidean family, not just rational coordinates paired with a nonsquare rational metric. Its starting four-source squared radius is449/400, and the same projective-affine first-order and labelled-projective separation arguments apply.

## 8. What was tried, what the evidence decides, and what remains

I first separated genuine incidence integrability from mechanical sign feasibility, then derived the full conormal equations with the actual facet second moments. Physical VF bookkeeping reduced the apparent four independent zero choices to two crossed sectors and a rank-two local jet. The resulting criterion is exact at first order and has a genuine second-order continuation test rather than a genericity argument.

For a concrete stress test I constructed a centrally paired octagonal roof with cyclic basal A contacts. Its four-contact tensor identity creates a projective-affine first-order obstruction. Actual nonaffine basal motion and a coupled height motion nevertheless produce the eight explicit positive derivatives above. Full actual-centroid Jacobian rank, rather than a finite failed search or a proposed formal tensor configuration, establishes the surrounding eight-parameter contact unfolding. A preliminary six-contact companion is retained because it is a rational Euclidean construction with simpler formulas.

The following remain unresolved: whether EVERY actual E17 S1U1/H0 body has at least one successful physical sector; whether a full-manifold nonnegative stress can persist in all VF sectors; and whether every such first-order failure can be removed by higher-order or contact-preserving deformations. The peeling condition is sufficient, not a universal incidence classification. The second-order test is exact for its specified tangent, not a proof that two derivatives always suffice. The eight-contact example proves neither universal eight-contact regularization nor existence of any S1U1 body.

The most useful next step is to apply(4.7) and(5.1) to the actual physical contact sectors of a hypothetical first-layer joint candidate, retaining the true C_f. A remaining stress must survive both centroid-moment restrictions and incidence reactions; then(6.2) is the appropriate whole-stress-cone curvature test. Repeating an affine tensor obstruction alone cannot decide this full-manifold question.

## 9. Complete recovery and observed verification

The autonomous source below includes the literal vertices, facets, both metrics, actual moment and pole generation, exact full hull checks, all68 reciprocal primitives, physical weak feet, full Jacobians, determinant cross-checks, the two continuum proofs and all local sign tables. No parent source, numerical optimizer, omitted array or external input is required.

Executed environment: **CPython3.13.5, SymPy1.14.0, standard-library Fraction arithmetic, assertions enabled**. The continuum certificate contains452 strictly positive rational-function guards and2450 strictly positive Bernstein coefficients, with full coefficient-to-power reconstruction. Each of the two paths has226 guards. The eight-contact path has1357 coefficients; the six-contact path has1093.

Six exact full mechanical records are regenerated, at t=0,1/1000,1/100 on each path. They evaluate408 primitives:394 nonzero and14 physical zeros, all14 occurring in the two starting records. Two independent volume fans agree through second moments at every record. Whole-interval support and sign preservation are certified polynomially, not inferred from those six records.

Build/check completed, and both completed again from a fresh directory containing only the source; reports and stdout matched byte-for-byte. This is author-executed exact verification plus the analytic proofs above, not proof-assistant formalization or an independently authored whole geometric verifier.

Save the complete fence below as `full_shape_escape.py`, with final LF, then run

```sh
OPENBLAS_NUM_THREADS=1 python -B full_shape_escape.py build > build.stdout
OPENBLAS_NUM_THREADS=1 python -B full_shape_escape.py check > check.stdout
cmp build.stdout check.stdout
```

Do not disable assertions.

|Object|Bytes|SHA-256|
|---|---:|---|
|full_shape_escape.py|15244|87216eade62898ccba7324e150e6a603eb5bd20b5bb3a94cfad2e421d34d389b|
|full_shape_escape.json|850955|fd655aab19ce5ccfed67a89949946e2ce56312d29f89c2780b239daaa2169a58|
|identical build/check stdout|606|f823937c0f33646955d15ade4b72d04253cc2938b59a8eae1a82e0f08019bc59|

Expected terminal output:


[Encoded source block omitted; the code in this passage is incomplete.]


### Complete runnable source

```python
#!/usr/bin/env python3
"""Actual E17 full-manifold 4A+4B and 4A+2B regularization.
CPython 3.13.5, SymPy 1.14.0, assertions enabled. No external data/solver.
Run: python -B full_shape_escape.py build|check
"""
import sys, json, hashlib
from pathlib import Path
from itertools import combinations, product
from math import comb
from fractions import Fraction
import sympy as s
Q=s.Rational
FAC=((0,7,6,5,4,3,2,1),(0,1,9),(0,9,7),(1,2,9),(2,3,8,9),
     (3,4,8),(4,5,8),(5,6,8),(6,7,9,8))
TRI=tuple((f[0],f[j],f[j+1]) for f in FAC for j in range(1,len(f)-1))
ED={}
for f,cy in enumerate(FAC):
    for i,j in zip(cy,cy[1:]+cy[:1]): ED.setdefault(tuple(sorted((i,j))),[]).append(f)
ED=dict(sorted(ED.items()))
assert len(TRI)==16 and len(ED)==17 and all(len(fs)==2 for fs in ED.values())
AA=(('A',0,1),('A',2,3),('A',4,5),('A',6,7))
BB6=(('B',1,2),('B',6,5))
BB8=(('B',1,2),('B',3,4),('B',6,5),('B',7,8))
TMAX=Q(1,100)
t=s.symbols('t',real=True)
Z3=s.zeros(3,1)
def mat(v): return s.Matrix(v)
def simp(v): return v.applyfunc(s.factor) if isinstance(v,s.MatrixBase) else s.factor(v)
def det(a,b,c): return s.det(s.Matrix.hstack(a,b,c))
def raw(h,t,z):
    return list(map(mat,((1,t,0),(1,h,0),(-t,1,0),(-h,1,0),(-1,-t,0),
                         (-1,-h,0),(t,-1,0),(h,-1,0),(-1,0,z),(1,0,z))))
def moments(Y,o):
    D=0;J=s.zeros(3,1);W=s.zeros(3)
    for ids in TRI:
        a,b,c=[Y[i] for i in ids];d=det(a-o,b-o,c-o)
        vs=[o,a,b,c];v=sum(vs,s.zeros(3,1))
        D+=d;J+=d*v;W+=d*(v*v.T+sum((w*w.T for w in vs),s.zeros(3)))
    D=s.factor(D);J=simp(J);W=simp(W)
    return D,simp(J/(4*D)),simp(W/(20*D))
def geometry(Y):
    D,g,second=moments(Y,Z3); X=[simp(v-g) for v in Y]
    normals=[];heights=[];poles=[]
    for cy in FAC:
        a,b,c=[Y[i] for i in cy[:3]];n=simp((b-a).cross(c-a));r=s.factor(n.dot(a))
        normals.append(n);heights.append(r);poles.append(simp(n/(r-n.dot(g))))
    return D,g,second,X,normals,heights,poles
def primitives(X,P,M):
    N=M.inv();rr={}
    for (i,j),(f,g) in ED.items():
        for kind,a,b,vs,A in (('A',i,j,X,M),('A',j,i,X,M),('B',f,g,P,N),('B',g,f,P,N)):
            rr[kind,a,b]=s.factor(vs[a].dot(A*(vs[b]-vs[a])))
    assert len(rr)==68
    return rr

def certificate(expr,name):
    """Exact strictly-positive rational-function certificate on [0,1/100]."""
    num,den=s.fraction(s.cancel(expr))
    if den.subs(t,0)<0: num=-num;den=-den
    results=[]
    for p in (num,den):
        pp=s.Poly(p,t);degree=pp.degree()
        cc=[pp.nth(i)*TMAX**i for i in range(degree+1)]
        bb=[sum(cc[j]*Q(comb(i,j),comb(degree,j)) for j in range(i+1)) for i in range(degree+1)]
        assert min(bb)>0,(name,s.factor(p),bb)
        # Independent exact Bernstein-to-power reconstruction.
        for k in range(degree+1):
            recovered=sum(bb[i]*comb(degree,i)*comb(degree-i,k-i)*(-1)**(k-i) for i in range(k+1))
            assert s.expand(recovered-cc[k])==0
        results.append(dict(degree=degree,power=cc,bernstein=bb))
    return dict(name=name,polynomials=results)

def fraction_det(A):
    a=[[Fraction(int(v.p),int(v.q)) for v in row] for row in A.tolist()]
    d=Fraction(1);n=len(a)
    for j in range(n):
        k=next(i for i in range(j,n) if a[i][j])
        if k!=j:a[j],a[k]=a[k],a[j];d=-d
        q=a[j][j];d*=q
        for i in range(j+1,n):
            if a[i][j]:
                r=a[i][j]/q
                for k in range(j+1,n):a[i][k]-=r*a[j][k]
                a[i][j]=Fraction(0)
    return Q(d.numerator,d.denominator)

def census(rr):
    U=[i for i in range(10) if max(v for (k,a,b),v in rr.items() if k=='A' and a==i)<0]
    S=[i for i in range(9) if max(v for (k,a,b),v in rr.items() if k=='B' and a==i)<0]
    Uw=[i for i in range(10) if max(v for (k,a,b),v in rr.items() if k=='A' and a==i)==0]
    Sw=[i for i in range(9) if max(v for (k,a,b),v in rr.items() if k=='B' and a==i)==0]
    H=[];weak=[];packets=[]
    for (i,j),(f,g) in ED.items():
        vals=[rr['A',i,j],rr['A',j,i],rr['B',f,g],rr['B',g,f]]
        if max(vals)<0:H.append((i,j))
        elif max(vals)==0:weak.append((i,j))
        packets.append(dict(edge=(i,j),faces=(f,g),values=vals))
    return dict(S=S,U=U,H=H,weak_vertices=Uw,weak_facets=Sw,weak_edge_packets=weak,
                zeros=[k for k,v in rr.items() if v==0],packets=packets)

def exact_control(Y,M):
    D,g,W,X,ns,hs,ps=geometry(Y)
    inside=sum(Y,Z3)/10
    assert moments(Y,inside)==(D,g,W)
    # Supporting triple enumeration recovers exactly the nine declared maximal facets.
    actual=set()
    for i,j,k in combinations(range(10),3):
        n=(Y[j]-Y[i]).cross(Y[k]-Y[i])
        if n==Z3:continue
        sl=[n.dot(v-Y[i]) for v in Y]
        if max(sl)<=0 or min(sl)>=0: actual.add(tuple(a for a,z in enumerate(sl) if z==0))
    assert actual=={tuple(sorted(f)) for f in FAC}
    cc=census(primitives(X,ps,M))
    # These controls have no VF; zero sources are simple physical contacts.
    vf=[(i,f) for f,cy in enumerate(FAC) for i in cy if M*X[i]==ps[f]*X[i].dot(M*X[i])]
    assert not vf
    assert len(cc['weak_edge_packets'])==len(cc['weak_vertices'])+len(cc['weak_facets'])
    contacts=[]
    for kind,a,b in cc['zeros']:
        if kind=='A':
            assert a in cc['weak_vertices']
            contacts.append(dict(kind='VE',vertex=a,edge=tuple(sorted((a,b))),point=X[a]))
        else:
            assert a in cc['weak_facets']
            i,j=next(ij for ij,fg in ED.items() if set(fg)=={a,b})
            point=M.inv()*ps[a]/ps[a].dot(M.inv()*ps[a]);e=X[j]-X[i]
            fraction=s.factor((point-X[i]).dot(e)/e.dot(e))
            assert 0<fraction<1 and point==X[i]+fraction*e
            contacts.append(dict(kind='EF',facet=a,neighbor=b,edge=(i,j),point=point,fraction=fraction))
    assert len({tuple(q['point']) for q in contacts})==len(contacts)
    return dict(vertices=Y,volume=D/6,centroid=g,raw_second=W,centered=X,poles=ps,M=M,N=M.inv(),VF=vf,census=cc,physical_weak_contacts=contacts)

def tangent_data(X,P,M,zeros,path_X,path_P):
    nvar=57;inc=[];Jgrad=s.zeros(3,nvar)
    for f,cy in enumerate(FAC):
        for i in cy:
            r=s.zeros(1,nvar);r[0,3*i:3*i+3]=P[f].T;r[0,30+3*f:33+3*f]=X[i].T;inc.append(r)
    Inc=s.Matrix.vstack(*inc)
    # Exact derivative of the actual quartic boundary moment J, at centered X.
    D=0;J=s.zeros(3,1)
    for ids in TRI:
        a,b,c=[X[i] for i in ids];dd=det(a,b,c);v=a+b+c;D+=dd;J+=dd*v
        for i,ddgrad in zip(ids,(b.cross(c),c.cross(a),a.cross(b))):
            Jgrad[:,3*i:3*i+3]+=v*ddgrad.T+dd*s.eye(3)
    assert J==Z3 and D>0
    CF=[]
    for cy in FAC:
        A=s.zeros(3)
        for j in range(1,len(cy)-1):
            vs=[X[i] for i in (cy[0],cy[j],cy[j+1])];v=sum(vs,Z3)
            A+=det(*vs)*(v*v.T+sum((x*x.T for x in vs),s.zeros(3)))/12
        CF.append(3*A/D)
    assert all(min(A[:k,:k].det() for k in (1,2,3))>0 for A in CF)
    assert sum((A*p*p.T for A,p in zip(CF,P)),s.zeros(3))==s.eye(3)
    Crow=s.zeros(3,nvar)
    for f,A in enumerate(CF):Crow[:,30+3*f:33+3*f]=A
    K=Inc.col_join(Jgrad);KC=Inc.col_join(Crow)
    assert Inc.rank()==34 and K.rank()==KC.rank()==37
    assert K.col_join(KC).rank()==37
    Grow=[]
    for kind,a,b in zeros:
        vs,met,off=(X,M,0) if kind=='A' else (P,M.inv(),30)
        rr=s.zeros(1,nvar);rr[0,off+3*a:off+3*a+3]=(met*(vs[b]-2*vs[a])).T
        rr[0,off+3*b:off+3*b+3]=(met*vs[a]).T;Grow.append(rr)
    G=s.Matrix.vstack(*Grow);A=K.col_join(G)
    _,piv=A.rref(); minor=A[:,piv].det(method='domain-ge')
    assert len(piv)==37+len(zeros) and minor!=0
    assert fraction_det(A[:,piv])==minor
    vel=s.Matrix.vstack(*[simp(v.diff(t).subs(t,0)) for v in path_X+path_P])
    assert K*vel==s.zeros(37,1) and min(G*vel)>0
    # Four physical similarity directions lie in the kernel of all contact rows.
    symvel=[]
    for i,j in ((0,1),(0,2),(1,2)):
        H=s.zeros(3);H[i,j]=1;H[j,i]=-1;H=M.inv()*H
        symvel.append(s.Matrix.vstack(*([H*x for x in X]+[-H.T*p for p in P])))
    symvel.append(s.Matrix.vstack(*(X+[-p for p in P])))
    SS=s.Matrix.hstack(*symvel);assert SS.rank()==4 and A*SS==s.zeros(A.rows,4)
    # Projective-affine first-jet obstruction, INCLUDING arbitrary actual centroid motion.
    tensor=s.zeros(3);esum=Z3.copy();weighted=Z3.copy();norms=[]
    for _,i,j in AA:
        e=X[j]-X[i];tensor+=(X[i]*e.T+e*X[i].T)/2;esum+=e
        ni=X[i].dot(M*X[i]);norms.append(ni);weighted+=ni*e
    assert tensor==s.zeros(3) and esum==weighted==Z3 and len(set(norms))==1
    return dict(incidence_rank=34,incidence_centroid_rank=37,ambient_variables=57,
                centered_tangent_dimension=20,physical_mod_similarity_dimension=16,
                contacts=zeros,augmented_rank=A.rows,escape_rank=len(zeros),
                pivot_columns=list(piv),pivot_minor=minor,centroid_blocks=CF,
                explicit_path_velocity=vel,positive_first_derivatives=list(G*vel),
                primal_stress_tensor=tensor,edge_sum=esum,radius_weighted_edge_sum=weighted,
                source_radius_squared=norms[0])

def sign_chambers(base_rr,zeros):
    table=[]
    for signs in product((-1,1),repeat=len(zeros)):
        rr={k:s.sign(z) for k,z in base_rr.items()};rr.update(dict(zip(zeros,signs)))
        cc=census(rr);na=sum(v<0 for k,v in zip(zeros,signs) if k[0]=='A')
        nb=sum(v<0 for k,v in zip(zeros,signs) if k[0]=='B')
        assert (len(cc['S']),len(cc['U']),len(cc['H']))==(5+nb,6+na,9+na+nb)
        assert not(cc['zeros'] or cc['weak_edge_packets'] or cc['weak_vertices'] or cc['weak_facets'])
        table.append(dict(signs=signs,S=cc['S'],U=cc['U'],H=cc['H']))
    return table

def run_case(name,h,z,M,zeros):
    Y=raw(h,t,z);D,g,W,X,ns,hs,P=geometry(Y);K=h*t+h-t+2
    assert s.factor(D-4*z*K)==0
    assert simp(g-mat((0,0,z*(K+1)/(4*K))))==Z3
    certs=[]
    for f,cy in enumerate(FAC):
        n=ns[f];height=hs[f];certs.append(certificate(height-n.dot(g),f'{name}:height:{f}'))
        for i,y in enumerate(Y):
            slack=s.factor(height-n.dot(y))
            if i in cy:assert slack==0
            else:certs.append(certificate(slack,f'{name}:support:{f}:{i}'))
        # Every nonincident polygon vertex is on the strict interior side of every true edge.
        for a,b in zip(cy,cy[1:]+cy[:1]):
            for j in cy:
                if j not in (a,b):
                    certs.append(certificate(n.dot((Y[b]-Y[a]).cross(Y[j]-Y[a])),f'{name}:polygon:{f}:{a}:{b}:{j}'))
    for i in range(10):
        incident=[f for f,cy in enumerate(FAC) if i in cy]
        candidates=[(fs,s.factor(det(*[ns[f] for f in fs]))) for fs in combinations(incident,3)]
        fs,delta=next((fs,dd) for fs,dd in candidates if dd.subs(t,0)!=0)
        certs.append(certificate(s.sign(delta.subs(t,0))*delta,f'{name}:extreme:{i}:{fs}'))
    certs.append(certificate(D,f'{name}:volume'))
    rr=primitives(X,P,M);rr0={k:v.subs(t,0) for k,v in rr.items()}
    assert set(k for k,v in rr0.items() if v==0)==set(zeros)
    for key,value in rr.items():
        if key in zeros:check=s.cancel(value/t)
        else:check=s.sign(rr0[key])*value
        certs.append(certificate(check,f'{name}:primitive:{key}'))
    ratios={r['name'].split(':primitive:')[1]:
            min(r['polynomials'][0]['bernstein'])/max(r['polynomials'][1]['bernstein'])
            for r in certs if ':primitive:' in r['name']}
    assert all(ratios[str(k)]>Q(19,100) for k in zeros)
    assert all(ratios[str(k)]>=Q(3,50) for k in rr if k not in zeros)
    frame=[mat((Y[i][0],Y[i][1],1)) for i in (1,3,5,7)]
    frame_minors=[det(*vv) for vv in combinations(frame,3)]
    assert all(v!=0 and not v.has(t) for v in frame_minors)
    assert all(v==0 for v in Y[0]-raw(h,0,z)[0]-mat((0,t,0)))
    controls=[]
    for tv in (Q(0),Q(1,1000),TMAX):
        controls.append(exact_control([v.subs(t,tv) for v in Y],M))
    for i,cc in enumerate(controls):
        c=cc['census'];assert (len(c['S']),len(c['U']),len(c['H']))==(5,6,9)
        assert len(c['zeros'])==(len(zeros) if i==0 else 0)
        assert len(c['weak_vertices'])==(4 if i==0 else 0)
        assert len(c['weak_facets'])==(len(zeros)-4 if i==0 else 0)
    base=controls[0]
    tang=tangent_data(base['centered'],base['poles'],M,zeros,X,P)
    ch=sign_chambers(rr0,zeros)
    return dict(name=name,h=h,raw_height=str(z),closed_t_interval=(0,TMAX),
                D=s.factor(D),g=[s.factor(a) for a in g],M=M,N=M.inv(),
                all_arrow_formulas={str(k):str(v) for k,v in rr.items()},
                opening_formulas={str(k):str(rr[k]) for k in zeros},
                controls=controls,tangent=tang,certificates=certs,local_chambers=ch,
                opening_lower_bounds={str(k):ratios[str(k)] for k in zeros},
                old_nonzero_absolute_lower_bound=min(ratios[str(k)] for k in rr if k not in zeros),
                fixed_projective_frame_vertices=(1,3,5,7),frame_triangle_determinants=frame_minors,
                chamber_status='Exact sign table; actual local realizability follows from certified full differential rank and the analytic implicit-function theorem, not 256 separately enumerated rational bodies.')

def encode(x):
    if isinstance(x,s.MatrixBase):return [[encode(v) for v in row] for row in x.tolist()]
    if isinstance(x,s.Basic):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def main():
    assert __debug__ and s.__version__=='1.14.0'
    if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):raise SystemExit('python -B full_shape_escape.py build|check')
    six=run_case('E17_FOUR_A_TWO_B',Q(1,2),s.Integer(1),s.eye(3),AA+BB6)
    eight=run_case('E17_FOUR_A_FOUR_B',Q(1,4),1-t,s.diag(1,1,Q(36,17)),AA+BB8)
    coeffs=sum(len(p['bernstein']) for c in (six,eight) for r in c['certificates'] for p in r['polynomials'])
    guards=sum(len(c['certificates']) for c in (six,eight))
    result=dict(version=1,title='E17_FULL_MANIFOLD_EIGHT_CONTACT_ESCAPE_V1',faces=FAC,
                edges=ED,triangle_fan=TRI,positive_rational_function_guards=guards,
                positive_bernstein_coefficients=coeffs,cases=(six,eight),
                scope='Both actual families have strict S=5,U=6,H=9. No weak-inclusive S1U1 example or proper110 density/exclusion is asserted.')
    data=(json.dumps(encode(result),sort_keys=True,indent=2)+'\n').encode()
    out=Path('full_shape_escape.json')
    if sys.argv[1]=='build':out.write_bytes(data)
    else:assert out.read_bytes()==data
    print('ACTUAL_E17_SAME_LATTICE_FOUR_A_FOUR_B_ESCAPE_ALL_0_LT_T_LE_1_OVER_100_PASS')
    print('SIX_CONTACT_COMPANION_AND_ALL_TRUE_CENTROIDS_RECIPROCALS_PASS')
    print('EXACT_FULL_REALIZATION_CONTACT_RANKS_6_AND_8_PASS')
    print('LOCAL_64_AND_256_SIGN_CHAMBERS_IMPLICIT_REALIZATION_PASS')
    print('PROJECTIVE_AFFINE_FIRST_ORDER_OBSTRUCTION_FULL_SHAPE_LINEAR_ESCAPE_PASS')
    print('LABELLED_PROJECTIVE_NONEQUIVALENCE_AND_T_19_OVER_100_ESCAPE_MARGIN_PASS')
    print('POSITIVE_GUARDS_AND_BERNSTEIN_COEFFICIENTS',guards,coeffs)
    print('NO_S1U1_OR_110_BODY_NO_UNIVERSAL_REGULARIZATION_OR_GLOBAL_BOUND_CHANGE')
    print(out.name,len(data),hashlib.sha256(data).hexdigest())
if __name__=='__main__':main()
```

Convenience copies: [complete source](sandbox:/mnt/data/full_manifold_work/full_shape_escape.py), [exact generated report](sandbox:/mnt/data/full_manifold_work/full_shape_escape.json). The literal source above is sufficient without either link.
