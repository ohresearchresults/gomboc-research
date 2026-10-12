# minimum-0225

AI research report · 2026-09-24 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# HEPTAGON_TRIANGLE_FULL_AFFINE_CHART_AND_EXPANSION7_U2_V1

## 1. Result and disposition

I obtain a genuine enlarged-family theorem, not another test inside the old four-cut domain.

**Every labelled heptagon–triangle prismatoid of the specified incidence has a unique nine-parameter affine normal form. Eight parameters describe its bottom polygon; the ninth is a relative triangle scale rho>0. For ALL eight admissible bottom parameters and ALL rho>=7, the actual uniformly filled body has at least TWO strict unstable vertices under EVERY SPD metric.** In fact its complete vertex-arrow graph admits no weak rooted spanning tree under any nonzero PSD matrix. No conditioning, stable-root, or saddle hypothesis is used.

The new proof transfers beyond this incidence: it applies to any finite bottom polygon and triangular top when the top triangle's area is at least49 times the area of the bottom's circumscribed triangle with those three supporting directions. A quantitative actual-centred tube of radius1/1024, in the explicit normalization below, also has U2 for every SPD; its proof does not require the perturbed true graph to remain unchanged.

I also give a **complete eleven-parameter labelled affine realization chart for the entire incidence**, including nonparallel heptagon and triangle planes. This is a realization chart, NOT an all-incidence mechanical exclusion. The eight basal parameters are complete projective moduli; positive projective denominators supply three further affine moduli, with the new uniform centroid explicitly recoverable.

A retained actual countercontrol shows why the old shadow reduction cannot be extended unchanged: an axial uniformly refilled projective image of the OLD fixed-slope shape has **TEN distinct true shadow corners**, not at most eight. Its physical census is6711, not U1. Three new genuinely changed-cut shapes have complete same-inverse **222, weak000** metric families with unbounded conditioning. No attaining example, whole-incidence count change, or change to34<=C_min<=622 follows.

## 2. Source identity and reading

The entire new research-journal(20260924-075628).md was read consecutively through EOF, including the literal parent and its complete recovery. The full18250-byte successor source supplied below imports no parent code or certificate data.

The direct mathematical anchor is

    minimum-0224
    SHA256 d4c4b2cbdc44607097e175a09d64c0181f19cd95da40fbce5fdb52974bff3e3a
    PRISMATOID_FOUR_CUT_FULL_DOMAIN_U2_V1.

Its fixed-slope family, all48790 rooted trees and actual-centred2^-22 tube remain closed. I did not reopen its320 systems or independently replay its large certificate. The old family is used for identity and comparison; the new quotient-tree certificate is independent. The parent's complete true-tree coverage and tube have their stated narrower scope. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## 3. Complete nine-modulus prismatoid chart

### 3.1. Domain, coordinates and true lattice

Write

    theta=(b,c,p,q,a,d,u,v), rho>0,
    0<b<c<1, 0<a<d<1,
    p>0, q>0, p+q<1,
    u>0, v>0, u/b+v/a<1.                            (1)

Use bottom plane z=0 and top plane z=1. The ten vertices, with the UNCHANGED labels, are

    Y0=(b,0,0),        Y1=(c,0,0),
    Y2=(1-p,p,0),      Y3=(q,1-q,0),
    Y4=(0,d,0),        Y5=(0,a,0),
    Y6=(u,v,0),
    Y7=(0,0,1),        Y8=(rho,0,1),       Y9=(0,rho,1). (2)

The maximal outward facet cycles F0,...,F8 are exactly

    (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0),
    (1,2,8), (9,8,2,3), (9,3,4),
    (4,5,7,9), (6,7,5), (7,8,9).

The true edges remain

    01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.

For direct reconstruction, the corresponding nine inequalities are

    F0: -z<=0,
    F1: -y<=0,
    F2: -v*x+(u-b)*y-b*v*z<=-b*v,
    F3: p*x+(c+p-1)*y+p*(c-rho)*z<=p*c,
    F4: x+y+(1-rho)*z<=1,
    F5: (d+q-1)*x+q*y+q*(d-rho)*z<=q*d,
    F6: -x<=0,
    F7: (v-a)*x-u*y-a*u*z<=-a*u,
    F8: z<=1.                                       (3)

All nine are genuine maximal facets under(1). No integration diagonal is a mechanical edge. Equality in a strict shape condition can merge features; such boundary objects are not reported as10/17/9 members.

Let Delta=conv((0,0),(1,0),(0,1)). The bottom B is the heptagon in(2). It is obtained from Delta by removing three corner regions: a two-edge region at0, one triangular region at(1,0), and one triangular region at(0,1). The origin-region corner is(u,v); the strict last inequality in(1) is exactly the positive turn at that corner. Its two cut lines meet the axes before(b,0) and(0,a), respectively. The other cuts are separated by b<c, a<d and p+q<1. This proves convexity and the genuine seven-edge order of B. At height s, the solid section is(1-s)B+s*rho*Delta. Its normal fan gives precisely the three side quadrilaterals and four side triangles in(3), for every rho>0.

### 3.2. Completeness and uniqueness under AFFINE normalization

In ANY prismatoid realization of these labelled facets, the opposite edges of F1,F4,F6 lie in parallel planes. Therefore

    01 || 78,    23 || 89,    45 || 97.

The three supporting lines of bottom edges01,23,45 form a nondegenerate circumscribed triangle Delta_B. Their outward directions are the three outward directions of the top triangle. An affine map sends Delta_B to Delta and the two levels to0,1. A shear fixing z=0 places vertex7 at(0,0,1). The top then has vertices(0,0),(rho,0),(0,rho) at height1 for one rho>0. The remaining bottom vertices have exactly form(2), and true incidences force every strict condition in(1).

This normalization is unique with the labels fixed. A further affine transformation between two such normal forms fixes the three virtual bottom triangle corners, hence fixes the bottom plane pointwise. Fixing top7 then removes its remaining two shear parameters and its height scaling. Thus it is the identity, and all nine parameters agree.

In particular rho is a genuine AFFINE modulus: rho^2 is the area of the top triangle divided by the area of Delta_B. The eight bottom coordinates independently range over an open subset of R8. This is not nine names for four old freedoms.

The only nontrivial unlabelled lattice symmetry is

    (0,1,2,3,4,5,6,7,8,9) -> (5,4,3,2,1,0,6,7,9,8),

which acts as

    (b,c,p,q,a,d,u,v,rho) -> (a,d,q,p,b,c,v,u,rho).

The source checks all14 bottom dihedral permutations and all6 top permutations, retaining exactly this symmetry and the identity.

The old parent is the FOUR-dimensional slice

    c=1-p, d=1-q, u=2a-b, v=b-a, rho=1.              (4)

Thus four independent cut-direction restrictions and the relative-scale restriction have now been released. For example, the normal to edge12 is(p,c+p-1), not necessarily(p,0); the normal to edge34 is(d+q-1,q), not necessarily(0,q). The two origin-cut normals(v,b-u) and(a-v,u) are likewise free.

## 4. Eight projective moduli and a complete eleven-modulus affine chart

This section concerns REALIZATION COVERAGE; it does not assert projective invariance of own-centred mechanics.

### 4.1. Why the eight basal moduli cannot be removed projectively

A labelled projectivity between two parallel-level normal forms preserves the intersection of their two facet planes: the horizontal line at infinity. Its restriction to the bottom plane is therefore affine. It sends each of the three virtual bottom support lines to its counterpart, so that restriction is the identity after normalization. Consequently the only remaining labelled projectivity between parallel-level normal forms is

    T_beta(x,y,z)=(x,y,(1+beta)z)/(1+beta*z), beta>-1,
    rho' = rho/(1+beta).                             (5)

It fixes the entire bottom polygon. Conversely(5) realizes every positive change of rho. Thus the eight bottom parameters are complete labelled PROJECTIVE moduli. The ninth parameter is projectively removable but is not mechanically removable under uniform refill.

### 4.2. Every realization, including nonparallel facet planes

In an arbitrary genuine realization of this incidence, F0 and F8 are disjoint facets and together contain all vertices. Let f0,f8 be their inward affine slacks. The function ell=f0+f8 is strictly positive on the whole body. Complete ell and f0 to a basis of four homogeneous affine forms. Dividing the other three forms by ell, with z'=f0/ell, gives an invertible positive projectivity taking the two facets to z'=0 and z'=1. It preserves the actual convex lattice. Apply the affine normalization above and then(5) to set rho=1.

Let Y_i(theta,1) be this canonical source, let g0 be its ACTUAL uniform centroid, and put X_i=Y_i-g0. Every realization of the incidence is, up to an affine map, represented by

    Z_i = X_i/(1+pi.X_i),
    pi in R3, 1+pi.X_i>0 for ALL ten i.              (6)

This yields eight basal parameters plus three denominator parameters: a complete eleven-dimensional labelled affine chart. There is no continuous redundancy. Indeed a labelled projectivity fixing the rho=1 source is the identity by(5). If two different pi values in(6) were affinely equivalent with the labels fixed, their composition would give such a nontrivial stabilizer.

An arbitrary positive projectivity factors into(6) followed by an affine transformation: writing its numerator A X+b and denominator1+pi.X gives b+(A-b*pi^T)X/(1+pi.X). The matrix A-b*pi^T is invertible. This proves coverage without pretending that a transported old centroid is the new centroid.

### 4.3. Exact uniform-refill centroid and reciprocal poles on the entire chart

Triangulate each TRUE facet cycle from its first vertex. For each triangle tau=(i,j,k), let

    w_tau=det(X_i,X_j,X_k)/6>0,
    d_i=1+pi.X_i.

The image tetrahedra with apex0 form a genuine disjoint fan. Hence

    V(pi)=sum_tau w_tau/(d_i*d_j*d_k),
    J(pi)=(1/4)sum_tau [w_tau/(d_i*d_j*d_k)]
                          *(X_i/d_i+X_j/d_j+X_k/d_k),
    g(pi)=J(pi)/V(pi).                               (7)

The physical centred vertices are Z_i-g(pi), not Z_i and not Z_i-T_pi(0). If q_f is a source pole at the actual source centroid, the new centred pole is

    q_f(pi)=(q_f+pi)/(1-(q_f+pi).g(pi)).              (8)

Use ONE SPD M and N=M^-1 at this same new origin. Equations(6)-(8), the strict domain and the literal face cycles are a full rational reconstruction recipe for every rational chart input. The executable independently checks(7) against a different image apex fan and checks(8) against actual face-plane solves.

For the parallel-level subclass, pi_x=pi_y=0. Starting from rho=1, beta=1/rho-1 in(5) corresponds to

    pi_z=beta/(1+beta*g0_z).

The new whole-sector exclusion rho>=7 therefore translates exactly to

    -1/(1-g0_z) < pi_z <= -6/(7-6*g0_z),
    pi_x=pi_y=0,                                    (9)

for EVERY admissible basal theta. The lower endpoint is a projective horizon, not a finite body. The upper endpoint is included.

**Important:** choosing beta to make rho large changes the uniformly refilled body. It cannot convert this tail theorem into an exclusion of an entire projective class or of all eleven chart parameters.

## 5. Actual solid moments for all nine prismatoid moduli

Let A0,A1,A2 be the actual areas of the three missing bottom corner regions, and K0,K1,K2 their first moments in the original bottom coordinates. They are

    A0=(b*v+a*u)/2, A1=(1-c)*p/2, A2=q*(1-d)/2,
    K0=((b*v*(b+u)+a*u^2)/6,
        (b*v^2+a*u*(a+v))/6),
    K1=A1*((2+c-p)/3,p/3),
    K2=A2*(q/3,(2+d-q)/3).

Set R=A0+A1+A2 and K=K0+K1+K2. For height one,

    V=(1+rho+rho^2-2R)/6,
    J_x=(1+rho+rho^2+rho^3)/24-K_x/4-rho*A1/12,
    J_y=(1+rho+rho^2+rho^3)/24-K_y/4-rho*A2/12,
    J_z=(1+2rho+3rho^2-2R)/24,
    g=J/V.                                          (10)

These are actual UNIFORM SOLID moments. The source verifies their entire polynomial identities in all nine variables with complete apex fans from0 and9, not only at the controls.

For the analytic derivation, at height s the ambient triangle is d(s)Delta, d(s)=1-s+rho*s. Each missing corner region is scaled by1-s and translated by rho*s times its triangle corner. Thus

    area(section)=d(s)^2/2-(1-s)^2R,
    first_xy(section)=d(s)^3*(1,1)/6
                     -(1-s)^3K-rho*s*(1-s)^2*(A1,A2).

Integrating these functions, and s times the area, proves(10). In particular

    0<=R<=1/2, 0<=A1,A2<=R,
    0<=K_x,K_y<=1/6.                                 (11)

The same formulas and bounds apply to ANY finite convex bottom polygon B contained in Delta and meeting its three supporting lines. First take positive-length side contacts: between consecutive triangle normal directions, Minkowski addition translates the corresponding bottom boundary chain by the relevant top vertex, giving exactly the same three missing regions. Point-contact cases follow by B_eta=(B+eta*Delta)/(1+eta) and continuity of the actual area and first moments. The final strict obstruction below is applied AFTER obtaining the closed moment bounds; it is not inferred by taking a limit of strict U counts.

This makes the tail mechanism independent of the number of bottom corners or the particular heptagon cuts.

## 6. The actual centroid supplies a much tighter four-group model

Put h=1/rho. Normalize horizontally by1/rho, leaving height one. Let g_h=(g_x/rho,g_y/rho,g_z), and let

    g_T=(1/4,1/4,3/4)

be the centroid of T=conv(000,001,101,011). Set k=1-2R and D_h=1+h+k*h^2. From(10), EXACTLY,

    g_h,x-1/4 = [2(R-A1)h^2+(1-6K_x)h^3]/(4D_h),
    g_h,y-1/4 = [2(R-A2)h^2+(1-6K_y)h^3]/(4D_h),
    3/4-g_h,z = [h+2k*h^2]/(4D_h).                  (12)

Consequently

    0<=dx,dy<=h^2/4,
    0<=zeta<=h(1+h)/4,                               (13)

where dx=g_h,x-1/4,dy=g_h,y-1/4,zeta=3/4-g_h,z. For the last bound, multiply by4D_h and use

    (1+h)D_h-(1+2k*h)
        =2(1-k)h+(1+k)h^2+k*h^3>=0.

The horizontal error is of order h^2, not order h. It comes from the synchronized actual corner areas AND first moments; it is not a free reference adjustment.

Use the invertible linear map

    L=((-2,-2,0),(2,0,-2),(0,2,-2))

and the four regular-tetrahedron vectors

    R0=(1,1,1), R1=(1,-1,-1),
    R2=(-1,1,-1), R3=(-1,-1,1).

In the new actual-centred coordinates, all bottom vertices and the three top vertices are respectively

    bottom: R0+h*L(x,y,0)-eta, (x,y) in B subset Delta,
    top i: Ri-eta, i=1,2,3,
    eta=L(dx,dy,-zeta).                              (14)

The three top labels1,2,3 here mean ORIGINAL vertices7,8,9. Group0 contains ALL original bottom vertices0,...,6. These four group names are not new physical vertices.

The proof now uses only(13)-(14). Thus it is valid even on the larger relaxation in which every bottom endpoint lies independently in Delta while the SAME eta belongs to the common box(13).

## 7. Complete nonzero-PSD obstruction for h<=1/7

### 7.1. Contract an actual rooted tree, without deleting escape obligations

Suppose a weak rooted tree exists on the actual vertex set, under a nonzero PSD M. This is an assumed TREE, not a singular strict-U count. Contract all bottom vertices to group0. Every quotient group can reach the root group, so the quotient directed graph contains a rooted tree on the four groups. Select one actual arrow realizing each of its three edges.

There are exactly64 possible rooted trees on the complete four-group graph. A quotient tree has at most one arrow sourced in group0. Different arrows entering group0 may end at different actual bottom vertices. The proof retains these endpoints separately. It does not replace all bottom vertices by one point or discard their original tree obligations.

### 7.2. Exact lower matrix and a retained positive square

For a quotient edge i->j put E=Rj-Ri. Let d=h*L(x,y,0) denote its bottom endpoint displacement when it has one. Its negative arrow matrix is -sym(X_source*(X_target-X_source)^T), where sym(A)=(A+A^T)/2.

Relative to -sym(Ri*E^T), its corrections are

    top -> top:    sym(eta*E^T),
    top -> bottom: sym(eta*E^T)-sym(Ri*d^T)+sym(eta*d^T),
    bottom -> top: sym(eta*E^T)+sym(d*(2R0-Rj)^T)
                                  -sym(eta*d^T)+d*d^T. (15)

All weights are ONE. These matrices are not the parent's volume-scaled arrow matrices; no old multiplier is transferred.

For the possible bottom-source arrow, put

    a_star=L(1/3,1/3,0)=(-4/3,2/3,2/3).

Write d=h*v. Retain the affine tangent of its square:

    d*d^T = h^2*(v*a_star^T+a_star*v^T-a_star*a_star^T)
            +h^2*(v-a_star)*(v-a_star)^T.             (16)

The last term is PSD. Let P(h) be the sum of(15) after replacing its one possible d*d^T term by the first term of(16). Therefore

    -sum_three sym(X_source*edge^T) >= P(h).          (17)

### 7.3. Finite exact certificate, with a complete continuous domain

Parameterize the common centroid box by

    eta=h*c1+h^2*c2,
    c1=L(0,0,-gamma/4),
    c2=L(alpha/4,beta/4,-gamma/4),
    alpha,beta,gamma in[0,1].

Each bottom endpoint has v in conv(000,(-2,2,0),(-2,0,2)). The matrix P is affine in each endpoint separately and affine in the common centroid parameters; the products are only common-centroid/endpoint products. Thus its entire domain is the convex hull of the EIGHT common centroid-box corners and the THREE choices per incident bottom endpoint.

For all64 quotient trees this gives exactly

    4*8*(9*3+6*9+1*27)=3456 corner configurations.

Here the16 undirected four-vertex trees have bottom-group degree1,2,3 in9,6,1 cases, respectively. These are quotient proof cases, not E17 incidence counts.

For each configuration P(h) has degree at most3. The source constructs its four exact matrix Bernstein coefficients on the CLOSED interval[0,1/7], reconstructs every power coefficient independently, and verifies

    every Bernstein coefficient - I/32 is SPD.       (18)

Actual executed totals:

    13824 shifted SPD matrices,
    41472 strictly positive leading principal minors.

The smallest first, second and third leading minors, respectively, are

    16711/14112,
    425973791/154893312,
    97178893181/566702997504.

Each determinant is also checked through a separate fraction-free LDL/Bareiss identity. The complete shifted-matrix stream SHA256 is

    1d56b60716d97c3ec62ace979f256b269f2789a2ab9a987c1d7bc57783ed20cb.

The stream hash is only an audit pin: every matrix is reconstructed by the complete source, not supplied by hash alone. No numerical solver or omitted multiplier table is needed.

The scalar Bernstein weights and the geometric convex-combination weights are nonnegative and sum to one. Consequently P(h)>I/32 throughout the full closed domain. From(17), for EVERY nonzero PSD M,

    sum_three D_ij(M) < -tr(M)/32 <0,                 (19)

contradicting the three selected weak arrows. The selected finite wall h=1/7 and the entire unbounded rho tail are covered. The h=0 endpoint is retained in the polynomial proof; it is the tetrahedral normalized limit, not an extra E17 member.

This rules out weak rooted trees even in the COMPLETE arrow graph. It does not declare its nonedges to be true mechanical edges: the complete graph is a stronger relaxation of the actual true-edge obligation. For SPD, a sole strict U would supply a true weak rooted tree by strict norm growth on every nonzero selected edge. Thus every actual member has at least two strict U, including all incidental physical weak contacts.

### 7.4. General geometric statement

Let P be ANY uniformly filled prismatoid whose top is a nondegenerate triangle T and whose bottom is a finite full-dimensional convex polygon B. In the bottom plane take the three actual supporting lines parallel to T's edges, forming Delta_B. Remove the relative translation by a shear. If

    Area(T) >=49*Area(Delta_B),                      (20)

then rho>=7 in the preceding normalization, and P has U>=2 under every SPD. The proof uses neither the number of bottom vertices nor the particular four-cut graph. It is NOT an exclusion of every triangular-top prismatoid; the complementary expansion ratios remain separate.

## 8. A larger true-COM tube, with no fixed-incidence assumption

In the normalized frame(14), h<=1/7 and(13) give

    ||eta||^2 <=h^2*(1/2+2h+3h^2)<h^2.

Hence every vertex has norm<5/2 and every pair difference has norm<7/2. Suppose another actual uniformly filled body has the same number of true labelled vertices, and AFTER centring at its OWN volume centroid, in this SAME linear normalization,

    max_i ||X'_i-X_i|| <=epsilon=1/1024.              (21)

Its maximal facets/true edges may differ. For any nonzero PSD M,

    |D'_ij-D_ij| <=tr(M)*[(17/2)epsilon+2epsilon^2]
                  <9epsilon*tr(M).

Any hypothesized new rooted tree still contracts to a four-group tree. Applying(19) to its three corresponding endpoint pairs gives

    sum_three D'_ij <(-1/32+27/1024)tr(M)
                     =-(5/1024)tr(M)<0.

Thus(21) excludes every SPD U1 body in this tube, including genuine nonparallel-level deformations whenever they meet the actual-centroid comparison. This is not the old2^-22 fixed-family tube, and it does not mean that arbitrary raw vertex perturbations preserve the incidence or the centroid.

## 9. Exact retained controls and a failed shortcut

### 9.1. Genuinely changed cut directions, boundary rho7 and an unbounded metric tail

For each rho in{7,8,64}, use

    (b,c,p,q,a,d,u,v)
      =(2/5,4/5,1/3,1/4,1/5,7/10,1/10,1/20).        (22)

All four old cut-direction restrictions fail. These are not affine or positive-projective relabellings of an old fixed-slope member: their eight projective basal invariants differ, also after the sole lattice reflection.

Actual volume/centroid pins are

    rho7:
      V=34091/3600,
      g=(14376173/8181840,14373469/8181840,97091/136364);
    rho8:
      V=43691/3600,
      g=(21033773/10485840,21030769/10485840,125291/174764);
    rho64:
      V=2496491/3600,
      g=(9586819373/599157840,9586799569/599157840,7450091/9985964).

Let S_rho=diag(1/rho,1/rho,1), and let

    U=(1,2,-1), V=(7,-4,-1), W=(1,1,3).

For EVERY ell>=16384 use the same reciprocal pair

    M_ell=S_rho*(ell^2 U U^T+ell V V^T+W W^T)*S_rho,
    N_ell=S_rho^-1*[U U^T/(36ell^2)
                       +V V^T/(4356ell)+W W^T/121]*S_rho^-1.

Each of these THREE actual geometries has throughout that whole interval

    strict S={0,8}, U={7,9}, H={79,89}, weak000.

All68 true-edge primitives remain NONZERO. The source expands each primal row and each ell^2-multiplied reciprocal row as a quadratic in ell-16384: its constant has the required strict sign, and the other coefficients have that sign or are zero. This proves the entire tail, not just the finite calibration point. In the horizontal1/rho frame, the metric spectrum is(6ell^2,66ell,11), so conditioning is unbounded. None of these222 bodies is an attainer.

### 9.2. A true TEN-corner shadow beyond the old eight-corner theorem

Use

    (b,c,p,q,a,d,u,v,rho)
      =(3/8,3/4,1/4,1/3,1/4,2/3,1/8,1/8,16/25).

This keeps the old cut slopes but changes its affine modulus rho. Its actual moments are

    V=647231/2160000,
    g=(221520227/776677200,420804829/1553354400,1172543/2588924).

Project along kernel(-3/10,-3/100,1), always using Y-g. The exact counterclockwise shadow cycle is

    (5,6,7,0,1,8,2,3,9,4).

ALL ten vertices are distinct true corners; every cycle edge is a true original edge. The minimum nonincident support determinant is1/900>0, and the actual origin is strictly interior. All20 boundary primitives at planar metric I are nonzero; the strict radial maxima are{0,4,5,7,8}, so this is NOT a rooted shadow.

For the genuine positive normal-height lift G=I,delta=1, set w=(-3/10,-3/100):

    M=((1,0,-w_x),(0,1,-w_y),(-w_x,-w_y,1+w_x^2+w_y^2)),
    N=((1+w_x^2,w_x*w_y,w_x),
       (w_x*w_y,1+w_y^2,w_y),(w_x,w_y,1)).

The complete physical census is

    S={0,1,2,4,6,8}, U={0,1,4,5,7,8,9},
    H={01,06,07,18,23,45,49,57,78,79,89}, weak000.

All68 primitives are nonzero. The old mask list and320 systems therefore cannot be reused outside their source geometry.

This body is exactly the uniformly refilled image of the old rho1 shape under(5) with beta=9/16. Transporting that source's old centroid gives instead

    (102764/393333,99434/393333,82775/131111),

which differs substantially from the actual centroid above. This is an actual same-incidence countercontrol to centroid transport, not merely a formal density calculation.

### 9.3. A nonparallel-level control in the full eleven-modulus chart

Take the basal parameters(22), source rho1, and source-own-centred projectivity

    pi=(1/5,-1/7,1/9).

Use(6)-(8), refill uniformly and recenter. At

    M=((3,1,0),(1,2,1),(0,1,2)), N=M^-1,

the body retains the literal10/17/9 incidence, its heptagon and triangle planes are genuinely nonparallel, and it has

    S={0,1,4,5,6,8}, U={1,3,6,7,8,9},
    H={01,18,23,34,39,49,57,78,79,89}, weak000.

All68 primitives are nonzero. Its larger rational coordinates, NEW actual centroid, poles and every primitive are regenerated exactly from the small input above. It is a realization/control, not a claimed point inside the U2 tail theorem or its quantitative tube.

### 9.4. Why dropping the source square was insufficient

At h=1/7, quotient arrows(3->2,0->3,1->0), common centroid-box corner(alpha,beta,gamma)=(0,0,1), and bottom choices(1,0) in the literal three-vertex order, the lower matrix obtained by simply DROPPING d*d^T is

    [[8/7,662/343,-416/343],
     [662/343,2400/343,416/343],
     [-416/343,416/343,4]].

Its determinant is -66448/117649. Restoring the actual source square at those formal endpoint choices gives leading minors

    60/49,617804/117649,394544/117649,

all positive. The tangent identity(16) repairs the ENTIRE rho>=7 domain without assuming that corner is a body.

The displayed centroid-box corner is NOT actual homogeneous geometry: actual full-dimensional B has integral_B x>0 and integral_B y>0, so(12) has strictly positive dx,dy for h>0. The negative determinant is therefore a precise failure of a dropped-term sufficient certificate, NOT failure of U2, actual moment realizability, or the full mechanical implication. This negative control is retained in the executable.

## 10. Remaining complement and useful continuation

The entire nine-modulus parallel-plane region rho>=7 is closed, as is the actual-centred tube(21). All roots, all selected weak-arrow walls, arbitrary metric conditioning, the finite rho7 wall and unbounded rho approaches are included. The result is not confined to a fixed base polygon or a small perturbation of old slopes.

The parallel-plane complement NOT decided here is the open domain(1) with0<rho<7, after removing the parent's fixed-slope rho1 family/its accepted tube and any overlap with(21). There is no reason to restrict its rank-two search to eight corners: the exact ten-corner control proves otherwise. The inherited prismatoid normal retraction remains applicable, but it now leads to the actual-centroid9/10-corner problem as well.

For all realizations, the complete domain is(1) for the eight basal parameters plus all pi satisfying(6). Nonparallel members have(pi_x,pi_y)!=(0,0). Outside the explicitly covered actual-centred tubes, those general positive projective directions are not excluded here; their physical centroid is(7), not a transported one. No all-incidence U1/110 theorem follows from choosing a convenient rho within a projective class.

The useful next step is to use the full eleven-modulus chart and its exact moment fan on this residual, or to strengthen the common-centroid/retained-square bound so it reaches smaller rho. No further search inside the old320 systems is needed. Finite local optimization undertaken during exploration did not supply a certified U1 body and contributes no exclusion premise.

## 11. Exact recovery and observed execution

The following complete standard-library source reconstructs all3456 cubic matrix configurations and13824 shifted SPD coefficients from the displayed exact rules, checks both whole-nine-variable apex-fan moment identities, reconstructs all five actual controls, checks all true hulls and the SAME inverse-metric censuses, verifies the three unbounded metric intervals, and retains the failed dropped-square control. It does not import an old catalogue, multiplier array, parent implementation, numerical solver, RNG or network source.

Observed environment: CPython3.13.5, assertions enabled. Build and check completed with identical stdout. A source-only recovery in a fresh directory regenerated the exact frozen source, ran build AND check, and matched the report bytes. These are author executions of this implementation, not a proof-assistant formalization or a separately authored audit.

Save the full source below as heptagon_triangle_moduli.py, UTF-8/LF with its final newline, and run

    python -B -S heptagon_triangle_moduli.py build > build.out
    python -B -S heptagon_triangle_moduli.py check > check.out
    cmp build.out check.out

Pins:

    heptagon_triangle_moduli.py:18250 bytes
    SHA256 276b9a9011d7e15642b21083268a9534af018231bdd8a630818290c481fcec90
    heptagon_triangle_moduli.json:191888 bytes
    SHA256 ba1e61f8916f2bc9a42debc31715ffd5af501667e6e9f30dce6f62793ad6ed8d
    identical build/check stdout:480 bytes
    SHA256 f50ce7f0629f51c375e968eec309fce856d1bec30156e980c15e6ba08e18bd0a

Expected terminal markers:

    WHOLE_NINE_MODULI_ACTUAL_VOLUME_TWO_FANS_PASS
    ALL_64_QUOTIENT_TREES_COMMON_CENTROID_BOX_EXACT_TAIL_PASS 3456 13824 41472
    EIGHT_FREE_BASAL_MODULI_R_GE7_ALL_NONZERO_PSD_ROOTED_EXCLUSION_PASS
    ACTUAL_TEN_CORNER_SHADOW_AND_FIVE_SAME_INVERSE_CONTROLS_PASS [(2, 2, 2), (2, 2, 2), (2, 2, 2), (6, 7, 11), (6, 6, 10)]
    THREE_NEW_SHAPES_ALL_L_GE16384_SAME_INVERSE_222_WEAK000_PASS
    HEPTAGON_TRIANGLE_MODULI_RECOVERY_PASS 191888 ba1e61f8916f2bc9a42debc31715ffd5af501667e6e9f30dce6f62793ad6ed8d

Supplementary copies: [source](sandbox:/mnt/data/prism_moduli/heptagon_triangle_moduli.py), [full exact report](sandbox:/mnt/data/prism_moduli/heptagon_triangle_moduli.json), [complete bundle](sandbox:/mnt/data/HEPTAGON_TRIANGLE_MODULI_EXPANSION7_bundle.zip). The literal source below is sufficient without those files.

### Complete runnable source

```python
#!/usr/bin/env python3
"""HEPTAGON_TRIANGLE_NINE_MODULI_AND_FULL_EXPANSION_TAIL_V1.
Python >=3.11 standard library; assertions enabled; no external input.
python -B -S heptagon_triangle_moduli.py build|check
The continuous proof is in the accompanying handoff.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path
import hashlib,json,sys
assert __debug__ and sys.version_info>=(3,11)
PARENT=('minimum-0224','d4c4b2cbdc44607097e175a09d64c0181f19cd95da40fbce5fdb52974bff3e3a')
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),(9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES=tuple(sorted({tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in FACES for i in range(len(f))}))
ARROWS=tuple(sorted((i,j) for a,b in EDGES for i,j in((a,b),(b,a))))
EF={e:tuple(i for i,f in enumerate(FACES) if set(e)<=set(f)) for e in EDGES}
R=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
L=((-2,-2,0),(2,0,-2),(0,2,-2))
HMAX=F(1,7);SHIFT=F(1,32)
PACK=((0,0),(1,1),(2,2),(0,1),(0,2),(1,2))

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(c,a):return tuple(c*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def mv(A,x):return tuple(dot(row,x) for row in A)
def syq(a,b):return tuple(F(a[i]*b[j]+a[j]*b[i],2) for i,j in PACK)
def matrix(v):return ((v[0],v[3],v[4]),(v[3],v[1],v[5]),(v[4],v[5],v[2]))
def minors(v):
 a,b,c,d,e,f=v
 return a,a*b-d*d,a*b*c+2*d*e*f-a*f*f-b*e*e-c*d*d

def solve(A,b):
 n=len(A);Q=[[F(x) for x in row]+[F(y)] for row,y in zip(A,b)]
 for k in range(n):
  j=next((i for i in range(k,n) if Q[i][k]),None)
  assert j is not None
  Q[k],Q[j]=Q[j],Q[k];d=Q[k][k];Q[k]=[z/d for z in Q[k]]
  for i in range(n):
   if i!=k:
    d=Q[i][k];Q[i]=[x-d*y for x,y in zip(Q[i],Q[k])]
 return tuple(row[-1] for row in Q)

def inv(A):
 cols=[solve(A,[int(i==j) for i in range(3)]) for j in range(3)]
 return tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))

def raw(p):
 b,c,pb,pc,a,d,u,v,r=p
 return ((b,0,0),(c,0,0),(1-pb,pb,0),(pc,1-pc,0),(0,d,0),(0,a,0),(u,v,0),(0,0,1),(r,0,1),(0,r,1))

def admissible(p):
 b,c,pb,pc,a,d,u,v,r=p
 return 0<b<c<1 and 0<a<d<1 and pb>0 and pc>0 and pb+pc<1 and u>0 and v>0 and u/b+v/a<1 and r>0

def moments(p):
 b,c,pb,pc,a,d,u,v,r=p
 AA=(b*v+a*u)/2;AB=(1-c)*pb/2;AC=pc*(1-d)/2;loss=AA+AB+AC
 JA=((b*v*(b+u)+a*u*u)/6,(b*v*v+a*u*(a+v))/6)
 JB=(AB*(2+c-pb)/3,AB*pb/3);JC=(AC*pc/3,AC*(2+d-pc)/3)
 js=add(add(JA,JB),JC)
 vol=(1+r+r*r-2*loss)/6
 J=((1+r+r*r+r**3)/24-js[0]/4-r*AB/12,(1+r+r*r+r**3)/24-js[1]/4-r*AC/12,(1+2*r+3*r*r-2*loss)/24)
 return vol,J,(AA,AB,AC),js

# Minimal sparse polynomial ring, solely for the two exact whole-family fan identities.
class Poly(dict):
 n=9
 def __init__(self,x=0):
  if isinstance(x,dict):super().__init__({e:F(c) for e,c in x.items() if c})
  else:super().__init__({(0,)*self.n:F(x)} if x else {})
 def __add__(self,o):
  o=Poly(o);v=dict(self)
  for e,c in o.items():v[e]=v.get(e,F(0))+c
  return Poly(v)
 __radd__=__add__
 def __neg__(self):return Poly({e:-c for e,c in self.items()})
 def __sub__(self,o):return self+-Poly(o)
 def __rsub__(self,o):return Poly(o)+-self
 def __mul__(self,o):
  v={}
  for e,c in self.items():
   for f,d in Poly(o).items():
    h=tuple(x+y for x,y in zip(e,f));v[h]=v.get(h,F(0))+c*d
  return Poly(v)
 __rmul__=__mul__
 def __truediv__(self,o):return self*F(1,o)
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  out=Poly(1)
  for k in range(n):out=out*self
  return out

def fan(Y,apex):
 D=0;J=(0,0,0);cells=[]
 for fi,f in enumerate(FACES):
  if apex in f:continue
  for k in range(1,len(f)-1):
   ids=(f[0],f[k],f[k+1]);vs=[Y[i] for i in ids]
   w=dot(sub(vs[0],Y[apex]),cross(sub(vs[1],Y[apex]),sub(vs[2],Y[apex])))
   D+=w;J=add(J,mul(w,add(add(Y[apex],vs[0]),add(vs[1],vs[2]))));cells.append((fi,ids,w))
 return D/6,mul(F(1,24),J),cells

def symbolic_moments():
 pars=[]
 for i in range(9):
  e=[0]*9;e[i]=1;pars.append(Poly({tuple(e):1}))
 Y=raw(pars);V,J,areas,js=moments(pars)
 for apex in(0,9):
  vv,jj,cells=fan(Y,apex);assert vv==V and jj==J
 return {'variable_order':('b','c','p','q','a','d','u','v','r'),'six_volume':sorted((6*V).items()),'24_first':[sorted((24*z).items()) for z in J],'fan_roots':(0,9)}

def quotient_trees():
 out=[]
 for ed in combinations(tuple(combinations(range(4),2)),3):
  adj=[[] for _ in range(4)]
  for i,j in ed:adj[i].append(j);adj[j].append(i)
  for root in range(4):
   par={root:root};queue=[root];ar=[]
   for i in queue:
    for j in adj[i]:
     if j not in par:par[j]=i;queue.append(j);ar.append((j,i))
   if len(par)==4:out.append((root,tuple(ar)))
 assert len(out)==64 and len({tuple(sorted(ar)) for _,ar in out})==64
 return out

def tail_power(ar,cb,choices,tangent=True):
 c1=mv(L,(0,0,-F(cb[2],4)));c2=mv(L,(F(cb[0],4),F(cb[1],4),-F(cb[2],4)))
 inc=[e for e in ar if 0 in e];ds={e:((0,0,0),(-2,2,0),(-2,0,2))[j] for e,j in zip(inc,choices)}
 pp=[(F(0),)*6 for _ in range(4)]
 for i,j in ar:
  E=sub(R[j],R[i]);pp[0]=sub(pp[0],syq(R[i],E));pp[1]=add(pp[1],syq(c1,E));pp[2]=add(pp[2],syq(c2,E))
  if i==0:
   d=ds[i,j];pp[1]=add(pp[1],syq(d,sub(mul(2,R[i]),R[j])));pp[2]=sub(pp[2],syq(c1,d));pp[3]=sub(pp[3],syq(c2,d))
   if tangent:
    anchor=(F(-4,3),F(2,3),F(2,3));pp[2]=add(pp[2],sub(mul(2,syq(d,anchor)),syq(anchor,anchor)))
  elif j==0:
   d=ds[i,j];pp[1]=sub(pp[1],syq(R[i],d));pp[2]=add(pp[2],syq(c1,d));pp[3]=add(pp[3],syq(c2,d))
 return tuple(pp)

def bernstein(pp):
 return tuple(tuple(sum(F(comb(k,j),comb(3,j))*HMAX**j*pp[j][i] for j in range(k+1)) for i in range(6)) for k in range(4))

def exact_tail():
 stream=hashlib.sha256();mins=[None]*3;cases=0
 for root,ar in quotient_trees():
  inc=[e for e in ar if 0 in e]
  for cb in product((0,1),repeat=3):
   for choices in product(range(3),repeat=len(inc)):
    pp=tail_power(ar,cb,choices);bb=bernstein(pp)
    for j in range(4):
     back=tuple(sum(bb[k][i]*comb(3,k)*comb(3-k,j-k)*(-1)**(j-k) for k in range(j+1)) for i in range(6))
     assert back==mul(HMAX**j,pp[j])
    for B in bb:
     q=tuple(x-(SHIFT if i<3 else 0) for i,x in enumerate(B));mm=minors(q);assert min(mm)>0
     a,b,c,d,e,f=q
     assert (mm[1]*(a*c-e*e)-(a*f-d*e)**2)/a==mm[2]
     for k,x in enumerate(mm):mins[k]=x if mins[k] is None else min(mins[k],x)
     stream.update(canonical(q))
    cases+=1
 assert cases==3456
 # A failed, purely relaxed lower matrix, not actual geometry or U1 feasibility.
 ar=((3,2),(0,3),(1,0));cb=(0,0,1);choices=(1,0);pp=tail_power(ar,cb,choices,False);h=F(1,7)
 bad=tuple(sum(h**j*pp[j][i] for j in range(4)) for i in range(6));assert minors(bad)[2]<0
 # Restoring the dropped source-square changes this test; neither tuple is claimed physical.
 d=mul(h,(-2,2,0));restored=add(bad,syq(d,d))
 return dict(tangent_anchor=(F(-4,3),F(2,3),F(2,3)),trees=64,common_centroid_box_corners=8,cases=cases,degree=3,h_interval=(0,HMAX),shift=SHIFT,PD_blocks=4*cases,positive_leading_minors=12*cases,leading_minima=mins,shifted_matrix_stream_sha256=stream.hexdigest(),failed_relaxed_r7=dict(arrows=ar,centroid_bits=cb,bottom_choices=choices,h=h,dropped_matrix=matrix(bad),leading_minors=minors(bad),source_square_restored_matrix=matrix(restored),source_square_restored_minors=minors(restored),actual_body=False))

def hull_faces(Y):
 out=set()
 for ids in combinations(range(len(Y)),3):
  a,b,c=[Y[i] for i in ids];n=cross(sub(b,a),sub(c,a))
  if n==(0,0,0):continue
  ds=[dot(n,sub(a,x)) for x in Y]
  if min(ds)>=0 or max(ds)<=0:out.add(tuple(i for i,d in enumerate(ds) if d==0))
 return out

def poles(Y,g):
 Q=[]
 for f in FACES:
  n=cross(sub(Y[f[1]],Y[f[0]]),sub(Y[f[2]],Y[f[0]]));h=dot(n,Y[f[0]])
  assert all(h-dot(n,Y[i])==0 if i in f else h-dot(n,Y[i])>0 for i in range(10))
  for k in range(len(f)):
   a,b=f[k],f[(k+1)%len(f)]
   assert all(dot(n,cross(sub(Y[b],Y[a]),sub(Y[j],Y[a])))>0 for j in f if j not in(a,b))
  assert h-dot(n,g)>0;Q.append(mul(1/(h-dot(n,g)),n))
 assert hull_faces(Y)=={tuple(sorted(f)) for f in FACES}
 return tuple(Q)

def physical(Y,M,V=None,g=None):
 Y=tuple(tuple(map(F,y)) for y in Y);M=tuple(tuple(map(F,r)) for r in M)
 vv,jj,c0=fan(Y,0);v9,j9,c9=fan(Y,9)
 assert vv==v9 and jj==j9 and vv>0 and all(c>0 for _,_,c in c0+c9)
 if V is not None:assert V==vv and g==mul(1/vv,jj)
 V=vv;g=mul(1/vv,jj);X=tuple(sub(y,g) for y in Y);Q=poles(Y,g)
 N=inv(M);assert min(minors(tuple(M[i][j] for i,j in PACK)))>0
 assert all(sum(M[i][k]*N[k][j] for k in range(3))==int(i==j) for i in range(3) for j in range(3))
 assert hull_faces(Q)=={tuple(i for i,f in enumerate(FACES) if v in f) for v in range(10)}
 dp={(i,j):dot(X[i],mv(M,sub(X[j],X[i]))) for i,j in ARROWS}
 dq={(i,j):dot(Q[i],mv(N,sub(Q[j],Q[i]))) for pair in EF.values() for i,j in(pair,pair[::-1])}
 U=[i for i in range(10) if all(z<0 for (a,j),z in dp.items() if a==i)]
 S=[i for i in range(9) if all(z<0 for (a,j),z in dq.items() if a==i)]
 wu=[i for i in range(10) if all(z<=0 for (a,j),z in dp.items() if a==i) and any(z==0 for (a,j),z in dp.items() if a==i)]
 H=[];HH=[];weak={};packets=[]
 for (i,j),(f,h) in EF.items():
  zz=(dp[i,j],dp[j,i],dq[f,h],dq[h,f]);e=sub(X[j],X[i]);t=-dp[i,j]/dot(e,mv(M,e));point=add(X[i],mul(t,e));normal=mv(M,point)
  gram=((dot(Q[f],Q[f]),dot(Q[f],Q[h])),(dot(Q[f],Q[h]),dot(Q[h],Q[h])))
  cc=solve(gram,(dot(Q[f],normal),dot(Q[h],normal)));assert add(mul(cc[0],Q[f]),mul(cc[1],Q[h]))==normal
  if max(zz)<0:H.append((i,j))
  if 0<t<1 and min(cc)>0:HH.append((i,j))
  if max(zz)<=0 and 0 in zz:
   assert 0<=t<=1 and min(cc)>=0
   typ=('VF' if min(cc)==0 else 'VE') if t in(0,1) else 'EF'
   weak.setdefault(point,[]).append(((i,j),typ))
  packets.append(dict(edge=(i,j),facets=(f,h),primitives=zz,foot_fraction=t,normal_coefficients=cc))
 assert H==HH
 assert U==[i for i in range(10) if all(dot(X[i],mv(M,sub(X[j],X[i])))<0 for j in range(10) if j!=i)]
 for f in S:
  foot=mul(1/dot(Q[f],mv(N,Q[f])),mv(N,Q[f]));assert all(dot(q,foot)<1 for h,q in enumerate(Q) if h!=f)
 return dict(vertices=Y,centred_vertices=X,volume=V,first_moment=jj,centroid=g,faces=FACES,edges=EDGES,poles=Q,M=M,N=N,strict_S=S,strict_U=U,strict_H=H,genuine_weak_U=wu,physical_weak=sorted(weak.items()),primal=sorted(dp.items()),polar=sorted(dq.items()),all_edge_packets=packets,zero_primitives=sum(z==0 for z in tuple(dp.values())+tuple(dq.values())))

def hull2(P):
 pts=sorted(set(P))
 def cr(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 lo=[];hi=[]
 for p in pts:
  while len(lo)>1 and cr(lo[-2],lo[-1],p)<=0:lo.pop()
  lo.append(p)
 for p in reversed(pts):
  while len(hi)>1 and cr(hi[-2],hi[-1],p)<=0:hi.pop()
  hi.append(p)
 return lo[:-1]+hi[:-1]

def automorphisms():
 autos=[];fs={frozenset(f) for f in FACES}
 for rev in(1,-1):
  for shift in range(7):
   for top in permutations((7,8,9)):
    p=tuple((shift+rev*i)%7 for i in range(7))+top
    if {frozenset(p[i] for i in f) for f in FACES}==fs:autos.append(p)
 assert autos==[tuple(range(10)),(5,4,3,2,1,0,6,7,9,8)]
 return autos

def projective_moments(Y,p):
 V,J,_=fan(Y,0);g=mul(1/V,J);X=[sub(y,g) for y in Y];ds=[1+dot(p,x) for x in X];assert min(ds)>0
 Z=[mul(1/d,x) for x,d in zip(X,ds)];vp=F(0);jp=(F(0),)*3
 for f in FACES:
  for k in range(1,len(f)-1):
   ids=(f[0],f[k],f[k+1]);a,b,c=ids;w=dot(X[a],cross(X[b],X[c]))/6;assert w>0
   w/=ds[a]*ds[b]*ds[c];vp+=w;jp=add(jp,mul(w/4,add(add(Z[a],Z[b]),Z[c])))
 vj,jj,_=fan(Z,0);assert vj==vp and jj==jp
 gp=mul(1/vp,jp);q0=poles(Y,g);qp=poles(Z,gp)
 assert qp==tuple(mul(1/(1-dot(add(q,p),gp)),add(q,p)) for q in q0)
 return dict(p=p,source_centroid=g,denominators=ds,vertices=Z,volume=vp,first_moment=jp,centroid=gp,poles=qp)

def flag_interval(data,r):
 threshold=2**14;polys=[]
 for typ,rows in(('P',data['primal']),('Q',data['polar'])):
  X=data['centred_vertices'] if typ=='P' else data['poles']
  for (i,j),old in rows:
   coeff=[]
   for vector,norm in zip(((1,2,-1),(7,-4,-1),(1,1,3)),(6,66,11)):
    v=tuple(F(vector[k],r if k<2 else 1) if typ=='P' else F(vector[k]*(r if k<2 else 1),norm) for k in range(3))
    coeff.append(dot(X[i],v)*dot(sub(X[j],X[i]),v))
   if typ=='P':coeff=coeff[::-1]
   shifted=(coeff[0]+threshold*coeff[1]+threshold**2*coeff[2],coeff[1]+2*threshold*coeff[2],coeff[2])
   sign=1 if old>0 else -1
   assert sign*shifted[0]>0 and all(sign*z>=0 for z in shifted)
   if typ=='P':assert shifted[0]==old
   else:assert shifted[0]==threshold**2*old
   polys.append(dict(kind=typ,edge=(i,j),power_L=coeff,power_L_minus_threshold=shifted,sign=sign))
 assert len(polys)==68
 return dict(L_lower=threshold,all_68_polynomials=polys,strict_S=[0,8],strict_U=[7,9],strict_H=[(7,9),(8,9)],physical_weak=0,all_primitives_nonzero=True)

def controls():
 base=tuple(map(F,('2/5','4/5','1/3','1/4','1/5','7/10','1/10','1/20')))
 uu=(1,2,-1);vv=(7,-4,-1);ww=(1,1,3);ell=2**14
 out=[]
 for r in(7,8,64):
  p=base+(F(r),);assert admissible(p);Y=raw(p);V,J,areas,js=moments(p)
  T=tuple(tuple(ell**2*uu[i]*uu[j]+ell*vv[i]*vv[j]+ww[i]*ww[j] for j in range(3)) for i in range(3))
  M=tuple(tuple(F(T[i][j],(r if i<2 else 1)*(r if j<2 else 1)) for j in range(3)) for i in range(3))
  c=physical(Y,M,V,mul(1/V,J));assert c['strict_S']==[0,8] and c['strict_U']==[7,9] and c['strict_H']==[(7,9),(8,9)] and c['physical_weak']==[] and c['zero_primitives']==0
  h=F(1,r);gn=(c['centroid'][0]/r,c['centroid'][1]/r,c['centroid'][2]);dx=gn[0]-F(1,4);dy=gn[1]-F(1,4);ze=F(3,4)-gn[2]
  assert 0<=dx<=h*h/4 and 0<=dy<=h*h/4 and 0<=ze<=h*(1+h)/4
  out.append(dict(identity='FREE_EIGHT_CUT_MODULI_EXPANSION_'+str(r),parameters=p,flag_L=ell,physical=c,whole_flag_interval=flag_interval(c,r)))
 p=tuple(map(F,('3/8','3/4','1/4','1/3','1/4','2/3','1/8','1/8','16/25')))
 assert admissible(p);Y=raw(p);V,J,_,_=moments(p);u,v=F(-3,10),F(-3,100)
 M=((1,0,-u),(0,1,-v),(-u,-v,1+u*u+v*v));c=physical(Y,M,V,mul(1/V,J))
 assert (len(c['strict_S']),len(c['strict_U']),len(c['strict_H']))==(6,7,11) and c['physical_weak']==[] and c['zero_primitives']==0
 shadow=[(x[0]-u*x[2],x[1]-v*x[2]) for x in c['centred_vertices']];hull=hull2(shadow);cy=tuple(shadow.index(z) for z in hull)
 assert cy==(5,6,7,0,1,8,2,3,9,4) and len(hull)==10
 assert all(tuple(sorted((cy[k],cy[(k+1)%10]))) in EDGES for k in range(10))
 convexity_min=min((hull[(k+1)%10][0]-hull[k][0])*(hull[j][1]-hull[k][1])-(hull[(k+1)%10][1]-hull[k][1])*(hull[j][0]-hull[k][0]) for k in range(10) for j in range(10) if j not in(k,(k+1)%10))
 assert convexity_min>0
 assert all(hull[i][0]*hull[(i+1)%10][1]-hull[i][1]*hull[(i+1)%10][0]>0 for i in range(10))
 shadowrows=[(cy[k],cy[j%10],dot(shadow[cy[k]],sub(shadow[cy[j%10]],shadow[cy[k]]))) for k in range(10) for j in(k-1,k+1)]
 shadowU=[i for i in cy if all(z<0 for a,j,z in shadowrows if a==i)];assert all(z!=0 for i,j,z in shadowrows)
 source=raw(p[:-1]+(F(1),));v0,j0,_=fan(source,0);g0=mul(1/v0,j0);b=F(9,16)
 transported=(g0[0]/(1+b*g0[2]),g0[1]/(1+b*g0[2]),(1+b)*g0[2]/(1+b*g0[2]))
 assert transported!=c['centroid'] and tuple((y[0]/(1+b*y[2]),y[1]/(1+b*y[2]),(1+b)*y[2]/(1+b*y[2])) for y in source)==Y
 out.append(dict(identity='ACTUAL_TEN_TRUE_CORNER_SHADOW_R16_OVER25',parameters=p,kernel=(u,v,1),physical=c,shadow=shadow,cycle=cy,shadow_primitives=shadowrows,shadow_strict_U=shadowU,shadow_convexity_min=convexity_min,axial_projective_b=b,old_centroid_transport=transported,actual_centroid_difference=sub(c['centroid'],transported)))
 # A true nonparallel-level member of the complete eleven-parameter chart.
 source=raw(base+(F(1),));pr=projective_moments(source,(F(1,5),F(-1,7),F(1,9)))
 M=((3,1,0),(1,2,1),(0,1,2));c=physical(pr['vertices'],M,pr['volume'],pr['centroid'])
 assert c['physical_weak']==[] and c['zero_primitives']==0
 n0=cross(sub(pr['vertices'][5],pr['vertices'][6]),sub(pr['vertices'][4],pr['vertices'][6]));n8=cross(sub(pr['vertices'][8],pr['vertices'][7]),sub(pr['vertices'][9],pr['vertices'][7]))
 assert cross(n0,n8)!=(0,0,0)
 out.append(dict(identity='ELEVEN_MODULI_NONPARALLEL_REFILLED_CONTROL',base_parameters=base,projective=pr,physical=c))
 return out

def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x

def canonical(x):return (json.dumps(enc(x),sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return len(b),hashlib.sha256(b).hexdigest()

def main():
 assert sys.argv[1:] in(['build'],['check'])
 syms=symbolic_moments();autos=automorphisms();tail=exact_tail();ctls=controls()
 assert F(1,32)-27*F(1,1024)==F(5,1024)
 report=dict(identity='HEPTAGON_TRIANGLE_NINE_MODULI_AND_FULL_EXPANSION_TAIL_V1',parent=PARENT,source_pin=pin(Path(__file__).read_bytes()),faces=FACES,edges=EDGES,graph_automorphisms=autos,actual_whole_family_moments=syms,regular_tetrahedron=R,normalizing_linear_map=L,tail_certificate=tail,controls=ctls,scope='All parallel-level labelled realizations have nine affine moduli. Every actual uniform member with r>=7 has U>=2 under every SPD; stronger no weak rooted tree under nonzero PSD, without a joint S1 assumption. The analytic tail mechanism also applies to every finite bottom polygon with the same three supporting directions, including point-contact limits. All other r, nonparallel projective members, and all-incidence closure remain unproved except previously accepted sectors.',tail_actual_centred_arbitrary_graph_collar=F(1,1024))
 data=canonical(report);out=Path(__file__).with_suffix('.json')
 if sys.argv[1]=='check' or out.exists():assert out.read_bytes()==data
 else:out.write_bytes(data)
 print('WHOLE_NINE_MODULI_ACTUAL_VOLUME_TWO_FANS_PASS')
 print('ALL_64_QUOTIENT_TREES_COMMON_CENTROID_BOX_EXACT_TAIL_PASS',tail['cases'],tail['PD_blocks'],tail['positive_leading_minors'])
 print('EIGHT_FREE_BASAL_MODULI_R_GE7_ALL_NONZERO_PSD_ROOTED_EXCLUSION_PASS')
 print('ACTUAL_TEN_CORNER_SHADOW_AND_FIVE_SAME_INVERSE_CONTROLS_PASS',[(len(c['physical']['strict_S']),len(c['physical']['strict_U']),len(c['physical']['strict_H'])) for c in ctls])
 print('THREE_NEW_SHAPES_ALL_L_GE16384_SAME_INVERSE_222_WEAK000_PASS')
 print('HEPTAGON_TRIANGLE_MODULI_RECOVERY_PASS',*pin(data))
if __name__=='__main__':main()
```
