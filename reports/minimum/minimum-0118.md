# minimum-0118

Historical AI scientific report · saved 2026-09-20 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# NONADJACENT_FREE_VERTEX_EXCHANGE_AND_ORDER2_PURE_A_REGULARIZATION_V1

## 1. Main result and exact boundary

**A simplicial, uniformly filled, own-centroid three-polytope whose only physical weak points are simple VE contacts regularizes whenever two free vertices are nonadjacent. This holds for any number of contacts. In the obstructed first-order case, a simultaneous genuine vertex motion with an additional second-order vertex correction suffices at the original body.** Here “free” means neither endpoint of any weak edge, and “nonadjacent” refers to the true edge graph.

Consequently **every simplicial pure-four-A body with at least 13 vertices regularizes**, without a degree, symmetry, covariance, tensor-stress or conditioning hypothesis. More precisely, any still-uncovered body with a nonempty free set must have that set induce a clique of at most four vertices. This closes a substantial part of the parent's same-side, co-aligned-fold residual, not merely an additional nonsingular-Jacobian case.

The mechanism is an exchange of two volume-neutral, tangential centroid motions. It gives an **exact constant-volume, constant-centroid straight line** through the original body and makes a free vertex nonsingular. It does not require either actuator to supply a first-order normal centroid direction. The full reduced quadratic also has both normal signs even when the two individual kernel folds have the same sign.

Two additional sufficient tests are proved below: a volume-neutral exchange with a nonadjacent target-only contact endpoint, and a contact-preserving affine test using the actual free-vertex Jacobian and a unique positive tensor stress.

**Not claimed:** universal four-point regularization, impossibility of the first-order coexistence configuration itself, or an actual four-A body with obstructing FULL shape stress and only co-aligned free folds. The remaining free-clique sector is unresolved. The new rational 14-vertex control has two designated co-aligned same-side folds, but no mechanical weak points. A separate new actual nine-vertex four-A control realizes an exceptional tensor configuration, but its sole free vertex is nonsingular. Neither is the requested full coexistence counterexample.

The parent's residual and the distinction between a single-fold control and a four-A obstruction are explicit in its literal statement. The present theorem goes beyond that residual's previous sufficient tests. :contentReference[oaicite:0]{index=0}

## 2. Read closure, authority and verification status

I read the complete supplied 2023-line journal through EOF, including the shared notebook, branch memory, entire literal parent, and its complete executable source. The only supplied file was `research-journal(20260920-022403).md`, 309045 UTF-8 bytes, SHA-256 `aa4907b1658647010e22c8e2048be8f40019272a724eda34be7efee3283c4b34`.

The literal parent is `minimum-0117`. Re-serializing its literal payload as compact UTF-8 JSON with keys `version`, `result_markdown`, one final LF in the Markdown string, `ensure_ascii=False`, and no envelope-final LF authenticated the stated 53849 bytes and SHA-256 `7f40813c3823ad8abbdb572a916cbda1849eb438d7e6b7f396d086fc45190841`. Its embedded `vertex_fold.py` was extracted and authenticated at 16692 bytes, SHA-256 `c170ec179b96f692a3e2cb6d9a3cf6530b076912e9d5169b18658356183c0abc`. No scientific or source-identity conflict was found. I did not rerun that parent's full suite; the new program has no predecessor import or missing source dependency. :contentReference[oaicite:1]{index=1}

The results below are direct analytic proofs plus newly executed exact controls. They are not inferred from finite unsuccessful searches. No literature-priority or proof-assistant certification is claimed. All newly reported controls and computational findings reconstruct from the complete source in section 10.

## 3. Actual moments and the two-vertex exchange lemma

Use physical Euclidean coordinates; an initially specified common SPD metric can first be absorbed into one invertible linear map, which also transports the actual uniform centroid. Let V>0 denote volume, g the actual centroid, and A_w=D_w g.

For a vertex w with triangular incident maximal facets, use the parent's actual inward-oriented star:

    r_i=v_i-w,  c_i=r_i×r_(i+1),
    a_w=Σ c_i,
    S_w=Σ (r_i+r_(i+1)) c_i^T,
    r_w=4(g-w),  ell_w=a_w^T S_w^(-1),
    B_w=r_w a_w^T-S_w=24V A_w.

The actual supporting cone makes det S_w>0. Its positive action is strongly cone-positive, or has strongly positive square in degree three; the positive eigenvalue and trace S_w=0 exclude both zero determinant and negative determinant. In particular rank A_w≥2. At a singular vertex:

    k_w=S_w^(-1)r_w,
    a_w^T k_w=1,
    ker A_w=span(k_w),  leftker A_w=span(ell_w),
    adj(B_w)=det(S_w) k_w ell_w.

The exact one-vertex identities, not just Taylor expansions, are

    V(h)=V-a_w·h/6,
    J(h)-g V(h)=[B_w h-(a_w·h)h]/24.

These are the actual uniform-volume formulas in the parent, which also proves their arbitrary-valence scope. :contentReference[oaicite:2]{index=2}

### Lemma 1: exact separability for two nonadjacent triangular stars

Let w,z be distinct nonadjacent vertices with triangular incident maximal facets. For sufficiently small displacements h at w and l at z, with every other vertex fixed,

    V(h,l)=V-(a_w·h+a_z·l)/6,
    J(h,l)-g V(h,l)
      =[B_w h+B_z l-(a_w·h)h-(a_z·l)l]/24.                (1)

**Proof.** Fix the original outward boundary triangulation for integration. No boundary triangle contains both vertices: otherwise their triangular maximal facet would contain the true edge wz. Therefore each boundary determinant and each boundary first-moment contribution depends on at most one moving vertex. The two one-vertex changes add exactly. No free cell masses or refinement edges are introduced. The strict supporting guards retain the same chamber for sufficiently small motions. This argument permits nonsimplicial facets elsewhere, provided those facets are untouched.

### Lemma 2: tangential exchange unlocks a singular vertex

Suppose both A_w,A_z have rank two and the same left-kernel line, represented by a nonzero covector nu. Suppose a_w^T is not parallel to nu. Choose u with

    a_w·u=0,  nu(u)≠0.

The restriction A_z:ker(a_z^T)→ker(nu) is an isomorphism. Its kernel is trivial because a_z·k_z=1; both spaces have dimension two. Consequently there is a unique v in ker(a_z^T) with

    A_z v=-A_w u.                                         (2)

Move w by s u and z by s v. Equation (1) gives, **exactly for every sufficiently small s**,

    V(s)=V,  J(s)=gV.                                     (3)

The other moving vertex is not a neighbor of w. Differentiating the exact first-moment formula at the new position, while using the constant g and V from (3), gives

    24V A_w(s)=B_w-s u a_w^T.

The rank-one determinant identity and the displayed adjugate therefore give the exact formula

    det A_w(s)=-s det(S_w) ell_w(u)/(24V)^3.                (4)

Since ell_w is proportional to nu, the coefficient is nonzero. Thus every sufficiently small nonzero s makes w a nonsingular actual centroid actuator. The exchange preserves volume as well as the true centroid. It does not prescribe a kernel displacement at w and does not require nu A_z to be nonzero.

### The remaining parallel-a case also controls the centroid

If a_w^T=lambda_w nu and a_z^T=lambda_z nu, the two scalars have opposite signs. Indeed a_w lies strictly inside the inward normal cone at w, so a_w·(z-w)>0; similarly a_z·(w-z)>0. These inequalities force lambda_w lambda_z<0. Since a_j·k_j=1,

    nu(k_w)=1/lambda_w,  nu(k_z)=1/lambda_z

have opposite signs. The missing centroid coordinate on each pure kernel line has quadratic coefficient -nu(k_j)/(24V). Solving two tangential centroid coordinates by the implicit-function theorem leaves these quadratic coefficients unchanged. They have opposite signs, so the intermediate-value theorem gives local centroid openness. The same argument works after small prescribed changes of the other vertices: kernel amplitudes of order tau^(1/3) have quadratic terms dominating an O(tau) prescribed change.

**Conclusion.** Two nonadjacent triangular-star vertices always give local centroid controllability: an ordinary rank-three implicit-function theorem if their joint derivative has rank three; the exact exchange if a covector a_j is not parallel to the common left kernel; and the opposite-quadratic case otherwise. There is no same-side two-free-vertex obstruction when the vertices are nonadjacent.

## 4. Genuine pure-A regularization, with the FULL shape stress addressed

Now assume the entire polytope is simplicial and its only physical weak points are simple A contacts x_i→y_i, u_i=y_i-x_i. At the actual centroid 0, x_i·u_i=0 and the radial supporting plane at x_i exposes exactly the true edge [x_i,y_i]. Put r_i=|x_i|² and s_i=|y_i|²=r_i+|u_i|².

If both endpoints follow their radial law and the actual centroid is held fixed,

    x_i(t)=(1+t r_i)x_i,  y_i(t)=(1+t s_i)y_i,
    x_i(t)·(y_i(t)-x_i(t))=t r_i(s_i-r_i)(1+t r_i)>0.     (5)

A nonsingular free vertex supplies the exact centroid correction. Thus Lemma 2, followed by this radial step, already proves regularization in its exchange case. Neither endpoint of any weak edge moves during the preliminary exchange. The exact physical interpretation of a positive A escape and preservation of the other feature guards is the same as in the literal parent. :contentReference[oaicite:3]{index=3}

The stronger statement is that **a first- or second-order raw vertex arc suffices at the original body**, including when a FULL actual shape stress exists.

### 4.1 Full shape matrix and orientation of its entire stress cone

For all actual vertex velocities h_j, let R be the complete shape derivative:

    (R h)_i=(u_i-x_i)·h_(x_i)+x_i·h_(y_i)
                     -u_i·Σ_j A_j h_j.                  (6)

A nonzero nonnegative stress alpha satisfies R^T alpha=0. With c_alpha=Σ_i alpha_i u_i, its literal vertex equations are

    Σ_(source i=j) alpha_i(u_i-x_i)
      +Σ_(target i=j) alpha_i x_i = A_j^T c_alpha
                    for EVERY actual vertex j.          (7)

The parent proves these full equations and c_alpha≠0; they are stronger than tensor or projective stress identities. :contentReference[oaicite:4]{index=4}

For completeness, test (6) on h_j^rad=|v_j|²v_j and put d=Σ A_j h_j^rad. Then

    c_alpha·d=Σ_i alpha_i |x_i|²|u_i|²>0.                (8)

This both proves c_alpha≠0 and fixes its orientation. If the free-vertex block has rank two, every c_alpha lies on the common left-kernel line. Choose nu so that nu(d)>0. Then

    c_alpha=lambda_alpha nu^T,  lambda_alpha>0

for **every nonzero stress in the full nonnegative cone**, not only one selected ray. If the free block has rank three, no such stress can exist, so the strict linear alternative gives an all-positive first shape derivative.

### 4.2 The simultaneous second-order direction

In the exchange case normalize u so that nu(u)=1, and take v from (2). Choose

    theta=1/[2(1+|nu(k_w)|)]>0,
    h_w=u+theta k_w,  h_z=v,  all other h_j=0.

Then Σ A_j h_j=0. Equation (1), at g=0, gives the exact moment expansion

    V(s)=V-theta s/6,
    J(s)=-theta s²(u+theta k_w)/24,
    g(s)=-theta s²(u+theta k_w)/[24(V-theta s/6)].         (9)

All raw weak endpoints are fixed. The coefficient b_i of s² in their own-centroid escape is therefore

    b_i=theta u_i·(u+theta k_w)/(24V).

For every nonzero full shape stress,

    alpha·b=lambda_alpha theta[1+theta nu(k_w)]/(24V)>0. (10)

Strict finite-dimensional separation now supplies genuine vertex vectors delta_j such that

    b+R delta>0.

The raw polynomial curve v_j(s)=v_j+s h_j+s² delta_j, uniformly refilled and then recentered by its exact actual centroid, has every A escape positive at order s². This uses all available vertex equations in (7), and permits all necessary second-order vertex corrections; it is not a frozen-star or tensor-only argument.

In the parallel-a case, choose whichever kernel k_w or k_z has positive nu(k). Its second coefficient pairs positively with **every** full shape stress by the same orientation argument, and the same second-order correction applies. If the full stress cone is empty in either case, an all-positive first derivative already suffices.

All original strict feature-labelled equilibria persist by their strict guards. Every other inactive feature retains a positive excluding guard, while (5) or the positive second coefficients remove each complete simple-A packet. Thus the full lattice and all original strict S/U/H labels are retained, no new strict equilibrium appears, and all physical weak points disappear. Harmless isolated primitive zeros need not individually disappear. Uniform density and the actual recentering are retained throughout; no polar centroid is substituted.

## 5. Combinatorial consequence and the remaining small-vertex sector

With k simple A points at most 2k vertices are weak-edge endpoints. If there are at least five free vertices, the true planar three-polytope graph cannot make them a clique: K5 would have ten edges on five vertices, violating the planar bound nine. Hence

    n≥2k+5  implies regularization.

For k=4 this is the claimed **n≥13 theorem**. The sharper actual condition is simply a nonedge inside the free set, regardless of n or endpoint overlaps.

For 9≤n≤12, a configuration not covered by this theorem must have a nonempty free clique of size at most four. At n=12 it must have exactly eight distinct endpoints, four disjoint weak edges, and a free K4; any endpoint identification would yield five free vertices and is covered. At n=11 it needs seven or eight endpoints and a free K4 or triangle. At n=10 it needs at least six endpoints; at n=9 at least five. The earlier low-degree, cubic, nonaligned and endpoint-unlocking criteria still apply inside these small classes and must not be discarded.

This is a necessary description of the uncovered region, not a realizability assertion. It does not exclude the minimum's nonsimplicial 10/17/9 layer. The global bracket 34≤C_min≤622 and all registry counts remain unchanged. :contentReference[oaicite:5]{index=5}

## 6. Two further tests inside the free-clique residual

### 6.1 A volume-neutral target-endpoint exchange

Let w be free and singular. Let z be a nonadjacent vertex which is a target, but never a source, of weak A edges. With the sources fixed, its exact contact-zero space is the affine plane intersection with tangent

    E_z=intersection of x_i^perp over all contacts x_i→z.

Use its actual a_z and A_z. If there is v such that

    v∈E_z,  a_z·v=0,
    ell_w A_z v=0,
    ell_w S_w^(-1) A_z v≠0,                              (11)

put u=24V S_w^(-1)A_z v. Then a_w·u=0, A_wu=-A_zv and ell_wu≠0. The two straight vertex movements s u,s v preserve every raw contact equality exactly, and by (1) preserve V and g exactly. Formula (4) makes w nonsingular, after which radial regularization applies.

This is different from the parent's test ell_w A_z E_z≠0: (11) works precisely with a direction having zero first-order normal centroid effect. Multiple incoming contacts are allowed here because their exact zero constraints are linear planes; vertices that are also sources are not automatically covered.

If a FULL shape stress is present, ell_w A_z E_z=0 already follows from (7). The new test then asks whether the next covector ell_w S_w^(-1) survives on E_z∩ker(a_z^T). For a single incoming contact x→z, failure is exactly

    A_z^T (ell_w S_w^(-1))^T ∈ span{x,a_z}.

These are additional genuine necessary equalities for a still-uncovered body, not a proof they hold or fail automatically.

### 6.2 Contact-preserving affine motion plus a free Jacobian

Suppose the four tensors T_i=sym(x_i u_i^T) have rank three and unique positive relation Σ alpha_i T_i=0, alpha_i>0. Put c=Σ alpha_i u_i and W=span(T_i). Assume c≠0 and a free vertex w has A_w^T c=0. If

    W(c):={sym(c z^T):z·c=0} is NOT contained in W,        (12)

the body regularizes.

Indeed choose H∈W^perp with Hc not parallel to c and let B_epsilon^T B_epsilon=I+epsilon H. This small actual affine map keeps every contact equality exactly zero and keeps the own centroid at zero. Tensor congruence leaves the same unique stress alpha, whereas c becomes B_epsilon c and the actual Jacobian becomes B_epsilon A_w B_epsilon^(-1). Consequently

    A_w(new)^T c(new)
       =B_epsilon^(-T) A_w^T(I+epsilon H)c≠0.

Here ker A_w^T=span(c) by rank two. Thus the sole possible nonnegative tensor stress cannot satisfy the full shape equations of the new body. No full nonnegative shape stress remains; a positive first genuine shape derivative follows. Condition (12) is equivalent to the existence of this H by orthogonal-complement duality.

This test is sufficient, not automatic. The actual four-A control in section 8 realizes c≠0 and W(c)⊂W, so a proposed general argument deleting that exceptional tensor case would be false even for genuine own-centroid, simplicial, four-A bodies. That control is rescued instead by its nonsingular free vertex.

## 7. Full simultaneous moment jets for continuation

The preceding proof suggests computing the whole reduced jet, not only one scalar fold coefficient per free vertex. The following exact recipe handles every simultaneous vertex velocity.

At actual g=0, for an outward true boundary triangle (i,j,k), write p=(v_i,v_j,v_k), H=(h_i,h_j,h_k), z0=v_i+v_j+v_k and z1=h_i+h_j+h_k. Set

    d0=det(v_i,v_j,v_k),
    d1=det(h_i,v_j,v_k)+det(v_i,h_j,v_k)+det(v_i,v_j,h_k),
    d2=det(h_i,h_j,v_k)+det(h_i,v_j,h_k)+det(v_i,h_j,h_k).

Then

    V1=Σ d1/6,
    J1=Σ(d1 z0+d0 z1)/24,
    J2=Σ(d2 z0+d1 z1)/24,
    g1=J1/V,  g2=J2/V-V1 J1/V².                         (13)

For any simple A row, its quadratic coefficient on the straight raw velocity h is

    b_i(h)=(h_(x_i)-g1)·(h_(y_i)-h_(x_i))-u_i·g2.        (14)

Whenever Rh=0 and alpha·b(h)>0 for every nonzero full nonnegative shape stress, v+s h+s² delta with a separating correction delta regularizes. Equations (13)–(14) include actual common volume and first-moment terms and actual recentering. The supplied source implements (13) and checks it against independent whole-polynomial integration on two opposite-normal directions.

**Why adjacency remains a real proof boundary.** Adjacent vertices share two maximal triangles. Their moment contributions contain mixed determinants det(h,l,a-b) and generally cubic terms after multiplication by the triangle vertex sum. Thus the exact additivity (1) fails, and the volume-neutral exchange line need not preserve J. No conclusion about adjacent free cliques follows by silently deleting those mixed terms. The most useful next task is the full restricted quadratic/cubic form from (13) on a free edge, triangle or K4, together with the target-endpoint test (11). I did not prove that form indefinite in every adjacent case.

## 8. Two newly executed actual controls

### 8.1 Rational same-side two-fold body and exact exchange

This is a new body, not either old seven-vertex fold. Use the parent's seven raw vertices at t0=3/40:

    p0=(0,0,0), p1=(1,0,0), p2=(0,1,0),
    p3=(10,0,1), p4=(0,9,1), p5=(-1/10,-1/10,-1/10),
    p6=(33/40,33/40,3/4).

Define

    C=[[1,1,1],[1,-1,0],[1339,1469,-8831]],
    D=diag(-1,-1,1),
    L=3713858887533/25145530010,
    v_i=C p_i-(L,0,0),  v_(i+7)=D v_i  (0≤i≤6).

The true hull is simplicial **14/36/24**. Its complete maximal facets are the literal FACES array in the executable below. Two independent positive apex fans give

    V=9152054037381017863/377182950150,
    g=(0,0,15149/10).

Subtract this g for physical coordinates. The designated nonadjacent degree-five vertices are 5 and 12. Their actual Jacobians jointly have rank two. At vertex5,

    a5=(20470,0,0), det S5=313107869970792,
    ell5=(0,0,5/18252),
    k5=(1/20470,
        7410115904059/52682513078836045,
        3229978534215369241/105365026157672090),
    rho5=3229978534215369241/384624491485966197336>0.

At12, A12=D A5 D, a12=D a5, k12=D k5, ell12=ell5 and rho12=rho5. Both pure kernel folds therefore have the same normal sign. Neither has a first-order normal actuator direction.

Nevertheless the exact line

    v5(s)=v5+s e3,  v12(s)=v12+s e3,
    every other vertex fixed,

has constant V and constant actual g, because a5·e3=a12·e3=0 and A5e3+A12e3=0. Both determinants equal

    -s det(S5)(5/18252)/(24V)^3.

They are positive for s<0 and negative for s>0. The whole closed interval |s|≤1/65536 retains the full lattice and strict **244/weak000**. In sorted-facet labels the stable facets are [12,13], unstable vertices [3,6,10,13], and saddle edges [(2,4),(3,10),(6,13),(9,11)]. All 144 actual edge primitives are nonzero throughout. There are 432 rational guards: 264 nonincident supports, 24 interior-centroid plane guards, and 144 primitive signs; their 864 numerator/denominator polynomials have 1214 positive Bernstein coefficients, maximum degree three. Both endpoints are independently re-hulled, re-integrated and mechanically audited.

The source also verifies the opposite-normal quadratic directions h5=e3+theta k5, h12=e3 for theta=±1/100. Their exact first centroid coefficient is zero and their second coefficients have opposite vertical signs. This tests the complete simultaneous quadratic, not only the two diagonal kernel terms.

**Scope:** the other vertices are frozen for this two-actuator test. The body has no mechanical weak point and is not asserted to have all its free vertices singular. It is not a four-A/full-shape-stress coexistence example.

### 8.2 Genuine four-A affine-exception control

Let

    h=-2/7-(22/21)sqrt(15),
    X=[(1,0,0),(1,1/3,1),(0,1,0),(-1/3,1,2),
       (-1,0,0),(-1,-1/3,1),(0,-1,0),(1/3,-1,2),(0,0,h)].

The true hull is simplicial **9/21/14**, actual centroid exactly zero, and volume (100+22sqrt(15))/27. The root satisfies 21h²+12h-344=0 and -22/5<h<-43/10. The complete hull and two true positive fans are reconstructed in the source.

There are exactly four physical weak points, all simple A on 0→1, 2→3, 4→5, 6→7. Each true packet has signs (0,-,-,-); the other 80 edge primitives are nonzero. Strict mechanics is **6/5/9**. The four tensors have rank three, unique positive relation alpha=(1,1,1,1), and

    c=(0,0,6),
    W=span{sym(e1 e2^T),sym(e1 e3^T),sym(e2 e3^T)},
    W(c)⊂W.

Thus (12)'s exceptional algebra occurs in a genuine own-centroid four-A body, not just an endpoint array. But its sole free vertex8 has degree six and

    det A8=(-3470598351+897747378sqrt(15))/1645665920>0.

The rational lower bound sqrt(15)>38729/10000 certifies positivity. In particular A8^T c≠0, so the tensor stress is **not** a FULL actual shape stress. The earlier nonsingular-free-vertex theorem already regularizes this body. This is a preserved negative control for the affine criterion's universality, not a new obstruction or an attaining body.

## 9. What was tried, what remains, and the best continuation

I first examined contact-preserving affine stress transport and the full shape stress equations rather than assuming higher-degree Jacobians invertible. The affine route yields (12), but not an exhaustive four-tensor classification; section 8.2 shows its residual can be physically real. The decisive observation was that the kernel of the *joint* centroid derivative is larger than the span of the individual free-vertex kernels. Volume-neutral tangential exchanges create an exact constant-centroid line and a mixed quadratic term that the separate fold signs do not see.

A still-uncovered simplicial pure-four-A body with n≥9 must now have a free clique of size at most four, still satisfy all applicable older singular/common-left-kernel/same-side conditions, fail the target-only exchange tests (11), and, in the unique positive rank-three tensor case, lie in W(c)⊂W. Any genuine obstruction must satisfy every actual vertex equation (7) and defeat the full simultaneous jet criterion (13)–(14), not only a diagonal kernel test. These necessary restrictions have not been proved jointly inconsistent, and no actual body realizing the full conjunction has been supplied.

Mixed A/B contacts, VF alternatives outside the previously accepted sectors, nonsimplicial shape constraints, and the no-free-vertex pure-A complement remain outside the new regularization theorem. The separate simple pure-B/free-facet result is unchanged. No numerical non-success is an exclusion proof, no weak110 seed is produced, and no minimum or census value changes.

The best continuation is a genuine free-edge/free-triangle/free-K4 analysis of the mixed moment polynomial (13), with (11) tested first on every nonadjacent target-only endpoint. This is a smaller and more concrete problem than arbitrary simultaneous free folds.

## 10. Complete executable recovery

Save the following exact source as `nonadjacent_free.py`, UTF-8/LF with one final LF. It includes all helpers, both exact bodies, root and separation parameters, exhaustive hulls, two-fan uniform moments, every actual vertex Jacobian used, full mechanics, the whole line interval, and the full simultaneous two-jet check. It imports no parent file.

Executed environment: CPython3.13.5, SymPy1.14.0, its installed mpmath1.3.0 dependency, assertions enabled, PYTHONHASHSEED=0; no other package, RNG, solver, network or external input. Ordinary build/check and a fresh source-only cold build/check both completed, with byte-identical source, report and stdout. An implementation-stage symbolic/static census branch was corrected before the frozen version; it was not a mathematical failure or an accepted output.

    export PYTHONHASHSEED=0
    python nonadjacent_free.py build > build.txt
    python nonadjacent_free.py check > check.txt
    cmp build.txt check.txt

Pins:

    nonadjacent_free.py  13573 bytes
    SHA256 1b47e822e6073c3397bd2dcc2de544d09bb03f59634ded7a0e4200a88d3444a3
    nonadjacent_free.json 107411 bytes
    SHA256 aaa41f52c9575a5afa17527b4d99224e430c3a27c8f366683e1fb6cdd05a32b6
    build.txt / check.txt 429 bytes
    SHA256 d3bba8fd138e4890a814929aca1239206a29ca62af9fb61ef900b80477c39010

Exact stdout:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]

    nonadjacent_free.json 107411 aaa41f52c9575a5afa17527b4d99224e430c3a27c8f366683e1fb6cdd05a32b6
    NONADJACENT_FREE_VERTEX_EXCHANGE_RECOVERY_PASS

The additional cold comparison marker was `NONADJACENT_FREE_SOURCE_ONLY_COLD_BYTE_PARITY_PASS`.

Convenience copies: [exact source](sandbox:/mnt/data/coexistence/nonadjacent_free.py), [complete exact report](sandbox:/mnt/data/coexistence/nonadjacent_free.json). Neither is required because the complete source follows.

```python
"""NONADJACENT_FREE_VERTEX_EXCHANGE_V1.
CPython 3.13.5, SymPy 1.14.0; exact rationals, assertions, no RNG/network/input.
python nonadjacent_free.py build|check
The fourteen-vertex control has TWO co-aligned same-side centroid folds,
but NO mechanical weak points: strict244/weak000, NOT a four-A counterexample.
"""
from pathlib import Path
from itertools import combinations
from math import comb
import hashlib, json, sys
import sympy as s
assert __debug__ and s.__version__ == '1.14.0'
R=s.Rational; Z=s.zeros(3,1); E=s.eye(3)
t=s.Symbol('t')
PARENT='minimum-0117'
PARENT_SHA='7f40813c3823ad8abbdb572a916cbda1849eb438d7e6b7f396d086fc45190841'
C=s.Matrix([[1,1,1],[1,-1,0],[1339,1469,-8831]])
ROT=s.diag(-1,-1,1)
SEP=R(3713858887533,25145530010)
PARAM=R(3,40)
EPS=R(1,65536)
RAW=[(0,0,0),(1,0,0),(0,1,0),(10,0,1),(0,9,1),
     (-R(1,10),-R(1,10),-R(1,10)),(11*PARAM,11*PARAM,10*PARAM)]
FACES=[(0,3,5),(0,3,6),(0,4,5),(0,4,6),(1,2,3),(1,2,5),
 (1,3,5),(2,3,4),(2,4,5),(3,4,10),(3,6,13),(3,10,11),
 (3,11,13),(4,6,10),(6,10,13),(7,10,12),(7,10,13),
 (7,11,12),(7,11,13),(8,9,10),(8,9,12),(8,10,12),
 (9,10,11),(9,11,12)]
def clean(x):
    return x.applyfunc(s.cancel) if isinstance(x,s.MatrixBase) else s.cancel(x)
def det(a,b,c): return a.dot(b.cross(c))
def hull(X):
    inside=sum(X,Z)/len(X); faces={}
    for i,j,k in combinations(range(len(X)),3):
        n=(X[j]-X[i]).cross(X[k]-X[i])
        if n==Z: continue
        h=n.dot(X[i]); vals=[n.dot(v)-h for v in X]
        if min(vals)<0<max(vals): continue
        f=tuple(a for a,v in enumerate(vals) if v==0)
        assert len(f)==3, ('Nontriangular maximal face',f)
        if f in faces: continue
        if n.dot(inside)>h: j,k=k,j
        faces[f]=(i,j,k)
    fs=sorted(faces); tri=[faces[f] for f in fs]; edges={}
    for fi,f in enumerate(fs):
        for e in combinations(f,2): edges.setdefault(e,[]).append(fi)
    assert all(len(v)==2 for v in edges.values())
    assert len(X)-len(edges)+len(fs)==2
    assert set(sum((list(f) for f in fs),[]))==set(range(len(X)))
    return fs,tri,dict(sorted(edges.items()))
def mass(X,tri,apex,second=True):
    V=s.S(0); J=Z.copy(); Q=s.zeros(3); ds=[]
    for f in tri:
        p=[apex]+[X[i] for i in f]
        d=det(p[1]-apex,p[2]-apex,p[3]-apex); ds.append(clean(d))
        z=sum(p,Z); V+=d/6; J+=d*z/24
        if second: Q+=d*(z*z.T+sum((v*v.T for v in p),s.zeros(3)))/120
    return clean(V),clean(J),clean(Q),ds
def jac(X,tri,V,g,w):
    B=s.zeros(3)
    for i,j,k in tri:
        if w in (i,j,k):
            n=(X[j]-X[i]).cross(X[k]-X[i])
            B+=(X[i]+X[j]+X[k]+X[w]-4*g)*n.T
    return clean(B/(24*V))
def star(X,tri,w):
    a=Z.copy(); S=s.zeros(3)
    for f in tri:
        if w not in f: continue
        i=f.index(w); u=X[f[(i+1)%3]]-X[w]; v=X[f[(i+2)%3]]-X[w]
        c=-u.cross(v)
        assert all(c.dot(x-X[w])>=0 for x in X)
        a+=c; S+=(u+v)*c.T
    return a,S

def mechanics(X,tri,edges,g):
    Y=[clean(x-g) for x in X]; poles=[]
    for i,j,k in tri:
        n=(X[j]-X[i]).cross(X[k]-X[i]); h=clean(n.dot(X[i]-g))
        poles.append(clean(n/h))
    static=not any(z.free_symbols for x in X for z in x)
    pv=[[] for x in X]; pq=[[] for f in tri]; rows=[]
    for (a,b),(f,h) in edges.items():
        vals=list(map(clean,[Y[a].dot(Y[b]-Y[a]),Y[b].dot(Y[a]-Y[b]),
                    poles[f].dot(poles[h]-poles[f]),poles[h].dot(poles[f]-poles[h])]))
        rows.append([a,b,f,h,vals])
        if static:
            sg=[int(s.sign(z)) for z in vals]
            pv[a].append(sg[0]);pv[b].append(sg[1]);pq[f].append(sg[2]);pq[h].append(sg[3])
    out={'poles':poles,'rows':rows}
    if static:
        out.update(S=[i for i,v in enumerate(pq) if max(v)<0],
                   U=[i for i,v in enumerate(pv) if max(v)<0],
                   H=[(a,b) for a,b,f,h,v in rows if all(z<0 for z in v)],
                   zero_primitives=sum(z==0 for a,b,f,h,v in rows for z in v))
    return out

def moment_jet(X,tri,H,V):
    """First two centroid coefficients for arbitrary simultaneous vertex velocities.
    X MUST have its actual uniform centroid at zero. H is one vector per vertex.
    Coefficients use v(t)=v+t*H (no factorial convention).
    """
    V1=s.S(0); J1=Z.copy(); J2=Z.copy()
    for i,j,k in tri:
        a,b,c=X[i],X[j],X[k]; h,l,m=H[i],H[j],H[k]
        d0=det(a,b,c)
        d1=det(h,b,c)+det(a,l,c)+det(a,b,m)
        d2=det(h,l,c)+det(h,b,m)+det(a,l,m)
        z0=a+b+c; z1=h+l+m
        V1+=d1/6; J1+=(d1*z0+d0*z1)/24; J2+=(d2*z0+d1*z1)/24
    return clean(V1),clean(J1/V),clean(J2/V-V1*J1/V**2)

def bern(p):
    x=s.Symbol('x'); q=s.Poly(s.expand(p.subs(t,-EPS+2*EPS*x)),x)
    n=max(0,q.degree())
    b=[sum(q.nth(j)*R(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
    assert all(z>0 for z in b),(p,b)
    return b

def guard(z):
    p,q=s.fraction(clean(z))
    if q.subs(t,-EPS)<0:p,q=-p,-q
    return [bern(p),bern(q)]

def enc(x):
    if isinstance(x,s.MatrixBase):return [[enc(v) for v in row] for row in x.tolist()]
    if isinstance(x,s.Basic):return str(x)
    if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [enc(v) for v in x]
    return x

def build():
    left=[C*s.Matrix(x)-s.Matrix([SEP,0,0]) for x in RAW]
    X=left+[ROT*x for x in left]
    fs,tri,edges=hull(X)
    assert fs==FACES and len(edges)==36 and (5,12) not in edges
    assert sum(5 in e for e in edges)==sum(12 in e for e in edges)==5
    V,J,Q,ds=mass(X,tri,X[0]); V2,J2,Q2,ds2=mass(X,tri,X[5])
    assert V==V2 and J==J2 and Q==Q2 and all(d>=0 for d in ds+ds2)
    g=J/V
    assert V==R(9152054037381017863,377182950150)
    assert g==s.Matrix([0,0,R(15149,10)])
    A=jac(X,tri,V,g,5); A2=jac(X,tri,V,g,12)
    a,S=star(X,tri,5); a2,S2=star(X,tri,12)
    assert a==s.Matrix([20470,0,0]) and a2==ROT*a and S2==ROT*S*ROT
    assert S.det()==313107869970792 and s.trace(S)==0
    ell=clean(a.T*S.inv()); k=clean(S.inv()*4*(g-X[5])); rho=(ell*k)[0]
    assert ell==s.Matrix([[0,0,R(5,18252)]])
    assert k==s.Matrix([R(1,20470),R(7410115904059,52682513078836045),
                       R(3229978534215369241,105365026157672090)])
    assert rho==R(3229978534215369241,384624491485966197336)>0
    assert A.rank()==2 and A2.rank()==2 and A2==ROT*A*ROT
    assert A*k==Z and ell*A==s.zeros(1,3) and a.dot(k)==1
    assert s.Matrix.hstack(A,A2).rank()==2
    assert (ell*ROT*k)[0]==rho
    old=mechanics(X,tri,edges,g)
    assert old['S']==[12,13] and old['U']==[3,6,10,13]
    assert old['H']==[(2,4),(3,10),(6,13),(9,11)] and old['zero_primitives']==0
    u=s.Matrix([0,0,1])
    assert a.dot(u)==a2.dot(u)==0 and A*u+A2*u==Z and (ell*u)[0]>0
    Y=X.copy();Y[5]=X[5]+t*u;Y[12]=X[12]+t*u
    Vt,Jt,_,_=mass(Y,tri,X[0],False)
    assert Vt==V and Jt==J
    At=jac(Y,tri,V,g,5)
    assert clean(24*V*At-(24*V*A-t*u*a.T))==s.zeros(3)
    slope=clean(-S.det()*(ell*u)[0]/(24*V)**3)
    assert slope<0 and clean(At.det()-t*slope)==0
    At2=jac(Y,tri,V,g,12)
    assert At2==ROT*At*ROT and clean(At2.det()-t*slope)==0
    # Fourteen actual vertices, all true maximal faces and all original strict signs
    # are certified on the ENTIRE closed interval, not by endpoint sampling.
    guards=[]
    for f,(i,j,k0) in zip(fs,tri):
        n=(Y[j]-Y[i]).cross(Y[k0]-Y[i])
        guards.append(['centroid_inside',f,guard(n.dot(Y[i]-g))])
        for l in range(len(Y)):
            if l not in f:guards.append(['support',f,l,guard(n.dot(Y[i]-Y[l]))])
    new=mechanics(Y,tri,edges,g)
    for r0,r1 in zip(old['rows'],new['rows']):
        assert r0[:4]==r1[:4]
        for j,(v0,v1) in enumerate(zip(r0[4],r1[4])):
            guards.append(['primitive',r0[:4],j,guard(s.sign(v0)*v1)])
    assert len(guards)==432
    ends=[]
    for sign in (-1,1):
        YY=[clean(x.subs(t,sign*EPS)) for x in Y]
        ff,tt,ee=hull(YY);vv,jj,_,_=mass(YY,tt,YY[0],False)
        mm=mechanics(YY,tt,ee,g)
        assert ff==fs and ee==edges and vv==V and jj==J
        for key in ('S','U','H','zero_primitives'):assert mm[key]==old[key]
        ends.append({'t':sign*EPS,'vertices':YY,'mechanics':mm})
    # The full reduced quadratic has BOTH signs, despite same-side pure kernels.
    saddle=[]; centered=[x-g for x in X]
    for theta in (-R(1,100),R(1,100)):
        H=[Z.copy() for x in X];H[5]=u+theta*k;H[12]=u
        v1,g1,g2=moment_jet(centered,tri,H,V)
        assert v1==-theta/6 and g1==Z
        assert g2==-theta*(u+theta*k)/(24*V)
        assert s.sign(g2[2])==-s.sign(theta)
        # Independent exact whole-polynomial integration of this velocity field.
        shifted=[x+t*h for x,h in zip(centered,H)]
        vs,js,_,_=mass(shifted,tri,centered[0],False)
        assert clean(vs-(V-theta*t/6))==0
        assert clean(js+theta*(u+theta*k)*t*t/24)==Z
        saddle.append({'theta':theta,'velocity':H,'volume_first':v1,
                       'centroid_first':g1,'centroid_second':g2})
    return {'identity':'NONADJACENT_FREE_VERTEX_EXCHANGE_V1','full_reduced_saddle':saddle,
        'parent':[PARENT,PARENT_SHA],
        'scope':'Actual two same-side co-aligned centroid folds and an exact isochoric isocentroidal unlock. Strict244, weak000; NOT a four-A or full-shape-stress coexistence counterexample.',
        'affine_exception_control':exceptional_four_a(),
        'recipe':{'base':RAW,'C':C,'rotation':ROT,'separation':SEP,'parent_parameter':PARAM},
        'vertices_raw':X,'vertices_centered':[x-g for x in X],
        'facets':fs,'outward_triangles':tri,'edge_incidence':[[e,f] for e,f in edges.items()],
        'volume':V,'first_moment':J,'centroid':g,'covariance':clean(Q/V-g*g.T),
        'two_positive_fans':[ds,ds2],
        'A5':A,'A12':A2,'a5':a,'S5':S,'ell5':ell,'kernel5':k,'rho5':rho,
        'a12':a2,'S12':S2,'ell12':ell*ROT,'kernel12':ROT*k,'rho12':rho,
        'mechanics':old,'arc':{'interval':[-EPS,EPS],'velocity5':u,'velocity12':u,
          'exact_volume':Vt,'exact_first_moment':Jt,'A5':At,'determinant_slope':slope,
          'all_interval_guards':guards,'independent_endpoint_audits':ends}}

def exceptional_four_a():
    """A different own-COM body: the affine mixed-subspace exception is real.
    The sole free vertex is NONSINGULAR. This is NOT the coexistence counterexample.
    """
    h=-R(2,7)-R(22,21)*s.sqrt(15)
    X=list(map(s.Matrix,[(1,0,0),(1,R(1,3),1),(0,1,0),(-R(1,3),1,2),
        (-1,0,0),(-1,-R(1,3),1),(0,-1,0),(R(1,3),-1,2),(0,0,h)]))
    fs,tri,edges=hull(X)
    assert fs==[(0,1,7),(0,1,8),(0,6,7),(0,6,8),(1,2,3),(1,2,8),
        (1,3,7),(2,3,4),(2,4,8),(3,4,5),(3,5,7),(4,5,8),(5,6,7),(5,6,8)]
    V,J,Q,ds=mass(X,tri,X[0]);v,j,q,dd=mass(X,tri,X[8])
    assert s.simplify(V-v)==0 and clean(J-j)==Z and clean(Q-q)==s.zeros(3)
    assert all(s.sign(d)>=0 for d in ds+dd)
    assert J==Z and s.simplify(V-(100+22*s.sqrt(15))/27)==0
    assert s.simplify(21*h*h+12*h-344)==0 and -R(22,5)<h<-R(43,10)
    mm=mechanics(X,tri,edges,Z)
    assert len(edges)==21 and mm['S']==[3,5,6,8,10,13] and mm['U']==[1,3,5,7,8]
    assert mm['H']==[(0,8),(1,3),(1,7),(2,8),(3,5),(3,7),(4,8),(5,7),(6,8)]
    assert mm['zero_primitives']==4
    packets=[]
    for a,b,f,g,values in mm['rows']:
        if any(v==0 for v in values):
            assert [int(s.sign(v)) for v in values]==[0,-1,-1,-1]
            packets.append((a,b))
    assert packets==[(0,1),(2,3),(4,5),(6,7)]
    tensors=[];c=Z.copy()
    for a,b in packets:
        u=X[b]-X[a];t0=(X[a]*u.T+u*X[a].T)/2
        assert X[a].dot(u)==0
        tensors.append(t0);c+=u
    W=s.Matrix.hstack(*(T.reshape(9,1) for T in tensors))
    assert W.rank()==3 and sum(tensors,s.zeros(3))==s.zeros(3) and c==s.Matrix([0,0,6])
    for d in (E[:,0],E[:,1]):
        T=(c*d.T+d*c.T)/2
        assert W.row_join(T.reshape(9,1)).rank()==3
    A=jac(X,tri,V,Z,8);ad=s.simplify(A.det())
    assert sum(8 in e for e in edges)==6
    assert ad==(-3470598351+897747378*s.sqrt(15))/1645665920
    low=R(38729,10000)
    assert low*low<15 and (-3470598351+897747378*low)>0
    assert s.sign(ad)==1 and A.T*c!=Z
    return {'identity':'C2_CARDINAL_RISING_FOUR_A_AFFINE_EXCEPTION_V1',
        'scope':'Genuine pure-four-A, nonzero positive-stress c and W(c) contained in W. Free vertex8 nonsingular: NOT a full-shape-stress or fold-coexistence obstruction.',
        'vertices':X,'height':h,'facets':fs,'triangles':tri,
        'edges':[[e,f] for e,f in edges.items()], 'volume':V,'first_moment':J,
        'covariance':clean(Q/V),'positive_fans':[ds,dd], 'mechanics':mm,
        'contacts':packets,'tensors':tensors,'positive_tensor_stress':[1,1,1,1],
        'c':c,'A8':A,'detA8':ad}

def main():
    assert sys.argv[1:] in (['build'],['check'])
    obj=build(); b=(json.dumps(enc(obj),sort_keys=True,separators=(',',':'))+'\n').encode()
    assert len(b)==107411 and hashlib.sha256(b).hexdigest()=='aaa41f52c9575a5afa17527b4d99224e430c3a27c8f366683e1fb6cdd05a32b6'
    path=Path('nonadjacent_free.json')
    if sys.argv[1]=='build':path.write_bytes(b)
    else:assert path.read_bytes()==b
    print('ACTUAL_14_36_24_TWO_COALIGNED_SAME_SIDE_FOLDS_PASS')
    print('TWO_POSITIVE_FANS_TRUE_COM_AND_STRICT244_WEAK000_PASS')
    print('EXACT_ISOCHORIC_ISOCENTROIDAL_TANGENTIAL_EXCHANGE_PASS')
    print('FULL_LATTICE_144_PRIMITIVES_WHOLE_CLOSED_INTERVAL_PASS')
    print('ACTUAL_9_21_14_FOUR_A_NONZERO_C_MIXED_SUBSPACE_EXCEPTION_PASS')
    print('GUARDS',len(obj['arc']['all_interval_guards']))
    print(path.name,len(b),hashlib.sha256(b).hexdigest())
    print('NONADJACENT_FREE_VERTEX_EXCHANGE_RECOVERY_PASS')
if __name__=='__main__':main()
```
