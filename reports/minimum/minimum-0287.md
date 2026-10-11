# minimum-0287

Historical AI scientific report · saved 2026-09-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# CENTERED_WHOLE_FACET_THREE_HALVES_SUBCLASSES_V1

## 1. Results and scope

The universal assertion **alpha T ≤ 3 Sigma/2 is not determined here**. There is no certified counterexample. Three complete positive results advance the actual realization constraints beyond the optimized one-constraint family.

**Opposite-section theorem.** The full centered inequality holds whenever the marked whole facet has an equal-area, second-moment-matched opposite section inside the actual body. In fact a stronger tangential inequality holds. This covers every facet of every centrally symmetric convex three-body, every marked prismatic base, and nonsymmetric bodies satisfying a finite antipodal-containment test. Equality in the three-halves inequality occurs precisely in the marked-prism case and only in its normal direction.

**Affine-thickness theorem.** The full inequality holds on both graph facets of every body with nonnegative affine thickness over an arbitrary centrally symmetric planar base. If that base is a parallelogram, it holds on **every genuine whole facet**, including the nonhomothetic lateral facets and all positive-area boundary cases. This is a complete continuous subclass, not a search over a few quadrilaterals.

**Actual E17 moment sector.** A separate exact calculation proves the strict inequality on **all nine facets of an entire noncentral 10/17/9 corner-cut family**, throughout its full nondegenerate cut-depth interval. This is a whole-parameter moment certificate, not an equilibrium exclusion. It is not the already closed five-parameter H5 family.

An additional closed four-parameter, nonsymmetric 19/42/25 family has a marked triangular facet satisfying an explicit strict antipodal-depth bound. Its facet mass lies throughout **(1/10,1/8)**, inside the interval where the inherited one-constraint leverage envelope does not prove three-halves. Its actual cross-covariance defect is nonzero.

No result here establishes S1/U1 infeasibility, changes the E17 incidence register, or supplies a110 attainer. The accepted bracket remains **34 ≤ C_min ≤ 622**. fileciteturn49file0L19-L21

### Input authority and execution

Both newly supplied files were read completely through EOF, including the entire journal, the literal matrix parent, and all three source units in the coordinator material. Their bytes and SHA-256 values matched the manifest. The required parent reconstructs as a29943-byte compact UTF-8 JSON envelope with one final LF in its Markdown and SHA

`ec3e7ca08d14c71e6cf37ae2af31fdaec58102245973083b9fd0438ff2985db6`.

The coordinator material is42799bytes, SHA `d1608c04cd8061ccca228a1354680e55d0dd6faf2507e08b0750cf15d6c661b4`. The updated journal is314242bytes, SHA `6a5d515777fc3e3eb0061850178d0bb297240f47fbb465b2500802cb7e16b15f`. No required dependency was missing or conflicting.

Both new exact programs were run normally, in a source-only directory, and after decoding the recovery capsule into another fresh directory. Their respective reports and stdout were byte-identical across those runs. These are observed author executions, not a claimed coordinator replay or proof-assistant formalization. The continuum theorems below are analytic; finite algebra and actual-region claims have the executed exact certificates described in Section8.

## 2. Definitions and relation to the parent

Let P be a full-dimensional compact convex three-body, uniformly filled and translated to its actual volume centroid. Let F be the entire genuine positive-area facet q·x=1. Write

    V = Vol(P),    w = Area(F)/||q||,    alpha = w/V,
    c = E_F x,    T = E_F xx^T,    Sigma = E_P xx^T,
    C_F = T−cc^T.

Here C_F has rank two and kernel span(q); T and Sigma are positive definite. These are uniform whole-facet and volume moments of one body. The requested assertion is

    Sigma >= (2 alpha/3) T.                          (1)

The accepted one-fifth parent instead proves

    5 Sigma >= alpha T + alpha^2 cc^T/(1−alpha).

The later paired-trace family has optimized centered variance coefficient Lambda* >2.0769, so retuning that family does not prove(1). Its leverage envelope leaves the stated middle mass interval unresolved. These distinctions are retained. fileciteturn50file2L54-L65

All conclusions below are affine-covariant: Sigma and T transform by L(·)L^T, c by L, and q by L^(-T). Alpha is invariant. No independent polar centroid or physical inverse is introduced.

## 3. Opposite whole-section moments control all mixed directions

### Theorem A

Suppose there is a planar convex set G contained in P∩{q·x=−1}, with

    Area(G)=Area(F),    E_G xx^T=T.

G need not itself be a facet. Then

    Sigma >= (4 alpha/3) C_F + (2 alpha/3) cc^T.      (2)

In particular(1) holds. Since Tq=c while E_G xx^T q=−E_Gx, the assumed second moments automatically give E_Gx=−c.

Two useful sufficient conditions are **−F⊂P** and **F−2c⊂P**. The first covers all centered centrally symmetric bodies. The second covers any prism with marked base F, without requiring that the planar base be centrally symmetric.

### Proof by an actual dominated section measure

Fix a covector u and put Y(x)=u·x. Identify the two parallel planes with a common Euclidean plane. Choose its first coordinate in the tangential direction of u; for a purely normal u choose any first coordinate.

Transport normalized area on F to normalized area on G as follows. Map the first-coordinate marginal by its increasing quantile map. On each first-coordinate fibre, map its interval increasingly and affinely onto the corresponding target interval. This triangular map S is one-to-one in the interiors and has positive diagonal derivatives a,b with ab=1 almost everywhere. This follows directly from the marginal and conditional uniform-density change-of-variables formulas.

For 0≤lambda≤1, the triangular interpolation

    Phi_lambda = lambda Id+(1−lambda)S

is also injective, lies in lambda F+(1−lambda)G, and has Jacobian

    [lambda+(1−lambda)a][lambda+(1−lambda)b] >=1.

The change of variables is valid by one-dimensional monotone substitution followed by affine interval substitution. Convex-section endpoint functions are locally Lipschitz in the interiors; exhaustion handles their null boundary sets. Thus this is a measure dominated by actual area in the intermediate section, not a freely fitted endpoint mass.

Let m=E_FY and v=Var_FY. The endpoint means are m,−m and both endpoint variances are v. The two endpoint values are increasing functions of the same first quantile coordinate. Their centered covariance is nonnegative: for increasing functions f,g, this follows by integrating

    [f(s)−f(t)][g(s)−g(t)] >=0

over two independent quantile parameters. Therefore

    E[lambda Y_F+(1−lambda)Y_G]^2
      >= [lambda^2+(1−lambda)^2]v+(2lambda−1)^2m^2.

The convex hull of F and G lies in P. Its section separation is2/||q||. Integrating the actual dominated area measure gives

    integral_P Y^2
       >= (Area(F)/||q||)[(4/3)v+(2/3)m^2].

Divide by the actual V. This holds for every u, proving(2). Different test directions may use different auxiliary transports; every transport is dominated by the same physical volume measure and has the same displayed moment bounds.

### Equality and strictness

The difference between(2) and(1) is (2alpha/3)C_F. Hence equality in(1) in a nonzero direction is possible only in the normal direction q.

Normal equality forces P=conv(F,G): any positive-volume part outside that hull has a positive integral of(q·x)^2. It also forces every intermediate section to have the same area as F. The same triangular-Jacobian argument then forces its diagonal derivatives to equal1. Repeating with any first-coordinate direction shows that each projected quantile map is a translation. The shifts are fixed by the centroid difference, so G=F−2c. Thus P is exactly the centered prism conv(F,F−2c).

Conversely a prism has alpha=1/2 and

    Sigma=C_F+cc^T/3,

so its gap in(1) has rank two and kernel span(q). Therefore the constant3/2 is sharp on this subclass. Under TheoremA, the gap is positive definite for every nonprism.

### Quantitative antipodal depth

There is also a useful complete geometric extension. Suppose r>0 and **−rF⊂P**. Define

    m0(r)=(r+1)(r^2+r+1)/3,
    m1(r)=−(r−1)(r+1)(3r^2+4r+3)/12,
    J(r)=(r+1)(3r^4−r^2+3)/15,
    kappa(r)=(r+1)(6r^4+3r^3+2r^2+3r+6)/30.

The triangular map now has Jacobian r^2, and its interpolation has Jacobian at least [lambda+r(1−lambda)]^2. The same argument proves

    Sigma >= alpha kappa(r) C_F+alpha J(r)cc^T
          >= alpha J(r)T.                           (3)

The last comparison uses kappa(r)−J(r)≥0, also immediate by integrating the nonnegative missing cross term.

More is available from actual centering. The dominated submeasure used above has mass w m0 and first moment w m1 c. The remaining positive volume measure has the opposite first moment. Consequently alpha m0≤1 and, when r≠1,

    Sigma >= alpha kappa(r) C_F
       +[alpha J(r)+alpha^2 m1(r)^2/(1−alpha m0(r))]cc^T.           (4)

The denominator is strictly positive for r≠1: otherwise the residual mass is zero but its required first moment is nonzero. At r=1 the correction is zero, including the prism mass-equality case. This is a residual-measure covariance inequality, not a reassignment of endpoint masses.

J(1)=2/3, and J is increasing for r≥1. For a rational polytope, the largest admissible r is exactly

    r_F=min{−1/(q_j·v): v a true vertex of F, q_j·v<0}.

Every q_j and v is at the actual centroid. This is a finite true-support test.

## 4. A closed nonsymmetric four-parameter application inside the unresolved mass interval

Let delta∈[19/20,1] and tau_i∈[1/5,1/3], i=1,2,3. Start from the cube[−1,1]^3, cut its four corners with sign product+1 by

    sigma·x <=3−delta,    sigma∈{−1,1}^3, sigma_1 sigma_2 sigma_3=1,

and take the convex hull with the three axial tips(1+tau_i)e_i. This is a complete rational generator of an actual19/42/25 body. Its marked facet F is the whole triangle with raw vertices

    (1−delta,1,1), (1,1−delta,1), (1,1,1−delta).

The complete25 support planes consist of the three negative coordinate planes, the four corner-cut planes, and, for each i with other indices j,k,

    x_i ± tau_i x_j <=1+tau_i,
    x_i ± tau_i x_k <=1+tau_i,
    (2−delta)x_i ± tau_i(x_j+x_k) <=(2−delta)(1+tau_i).

These planes, not a triangulated hull, define the true incidence throughout the box.

Put A=4−delta^2. Its actual volume and first integrals are

    V=8−2delta^3/3+(A/3)(tau_1+tau_2+tau_3),
    J_i=(A/3)tau_i(1+tau_i/4),    g_i=J_i/V.

Its actual second integrals are also polynomial and are reconstructed in the executable. All thirteen independent volume/first/second moment identities agree identically with complete oriented-boundary integration. For the marked facet,

    c=(1−delta/3)(1,1,1)−g,
    C_F=(delta^2/36)[3I−11^T],
    T=C_F+cc^T,
    alpha=delta^2(3−delta−sum g_i)/(2V).

The exact whole-box certificate proves

    1/10 < alpha < 1/8,
    −(201/200)(F−g) lies inside the actual centered body.

It uses **528 positive polynomial guards and4868 positive tensor Bernstein coefficients**, with independent inverse coefficient reconstruction and no subdivision. The guards cover all true supports, polygon turns, vertex ranks, positive volume, actual support, both alpha bounds and every antipodal inclusion inequality. The smallest lower bound among the cleared guards is6733/180000; this is a cleared polynomial bound, not a normalized Euclidean distance.

Since

    J(201/200)−2/3=40353643603/4800000000000,

the entire closed box has the explicit strict matrix gap

    (3/2)Sigma−alpha T
       >= alpha [40353643603/3200000000000] T >0.     (5)

This is a genuine mixed-moment statement throughout four independently varying actual parameters. Its entire mass interval lies beyond what the inherited min(15alpha,Lambda*−alpha) envelope proves at three-halves. fileciteturn50file2L59-L62

At delta=1 and tau=(1/5,1/4,1/3), the exact control has

    V=487/60,
    g=(63/2435,255/7792,65/1461),
    alpha=221711/1897352,
    r_F=235409/232111 >201/200.

Its centroid-regression defect is

    c−Sigma q/(q^T Sigma q)
      =(686759134,138926308,−825685442)/27916764207,

which is nonzero. The body has19 genuine vertices, so in particular it is not centrally symmetric. The exact report preserves its full actual covariance, every whole-facet moment and a positive tetrahedral fan. A fixed nonsingular affine-image check transports Sigma,T,c,q and alpha consistently. No equilibrium census or110 claim is made for this moment control.

## 5. A complementary complete affine-thickness subclass

### Theorem B: graph facets over any centrally symmetric planar base

Let K⊂R^2 be any full-dimensional centrally symmetric convex body with centroid0 and covariance S. Let ell(u)=1+b·u be nonnegative on K, and form the actual uniform body

    P={ (u,z): u∈K, |z|≤ell(u) }.

Set a=Sb and s=b^T S b. Symmetry and the even concave one-dimensional section-length density imply0≤s≤1/3: an even decreasing density on[−h,h] has second moment at most h^2/3, and nonnegativity of ell gives h≤1.

Actual integration, without assigning section means, gives

    V=2 Area(K),    g=(a,0),
    Sigma=diag(S−aa^T,(1+3s)/3).

For either whole graph facet z=±ell(u),

    alpha=(1+s)/2,
    c=(−a,±1),
    T=diag(S+aa^T,1+s).

In particular the mixed facet block vanishes because E_K[u ell(u)]=a, exactly the same a occurring in the actual volume centroid.

The generalized eigenvalues of alpha T relative to Sigma are

    (1+s)/2,
    (1+s)^2/[2(1−s)],
    3(1+s)^2/[2(1+3s)].

All are at most3/2 for0≤s≤1/3. The second is at most4/3. The third equals3/2 only at s=0. Thus(1) holds on both graph facets, strictly unless b=0. At b=0 the marked graph facet is a prismatic base and its equality direction is normal.

This theorem does not assert the lateral-facet inequality for an arbitrary planar K. The next result does cover all lateral facets when K is a parallelogram.

### Theorem C: every whole facet over a parallelogram

Up to an invertible affine map and an affine vertical shear, the complete subclass is

    P_{b,c}={−1≤x,y≤1, |z|≤1+bx+cy},
    |b|+|c|≤1.                                     (6)

The body is generally nonsymmetric and nonhomothetic. All its genuine positive-area facets satisfy alpha T≤3Sigma/2. A zero-area side at a boundary parameter is not counted as a facet.

Here

    V=8,    g=(b/3,c/3,0),
    Sigma_H=I/3−(b,c)(b,c)^T/9,
    Sigma_zz=(1+b^2+c^2)/3,    Sigma_Hz=0.

The graph facets are covered by TheoremB. For the whole lateral facet x=1, assuming1+b>0,

    alpha=(1+b)(3−b)/6,
    T11=(3−b)^2/9,
    T12=−bc(3−b)/[9(1+b)],
    T22=1/3−2c^2/[9(1+b)]+c^2/9,
    T33=[(1+b)^2+c^2]/3,    T13=T23=0.

Its centered gap G=3Sigma/2−alpha T has

    G_H=(1/54)[[b^2(b^2−8b+9), b^2c(b−6)],
              [b^2c(b−6), b^2c^2+3b^2−4bc^2−6b−6c^2+18]],

    det G_H=b^2 D/2916,
    G33=W/18,

where

    D=3b^4−30b^3−b^2c^2+93b^2+12bc^2−198b−54c^2+162,
    W=b^4+b^2c^2+3b^2−2bc^2−8b+6c^2+6.

These polynomials prove the entire diamond(6), not just sampled parameters. The coefficient of c^2 in D is negative. Substitute c^2≤(1−|b|)^2 to obtain

    D≥2(b^4−8b^3+7b^2−39b+54)≥30,       0≤b≤1,
    D≥2(b^4−10b^3+31b^2−147b+54)≥108,   −1≤b≤0.

For the first bound, the derivative of the bracket is at most−21 and its value at1 is15. For the second, all terms are nonnegative after putting b=−u. Also b^2−8b+9≥2, and

    W=(b^2−2b+6)c^2+b^4+3b^2−8b+6>0

on−1≤b≤1. Thus G is positive definite if b≠0. At b=0 its only kernel direction is the x-axis. Reflection and exchanging x,y cover the other three lateral facets.

Consequently equality is exactly the corresponding prism case: b=0 for x-facets, c=0 for y-facets, and b=c=0 for graph facets. In every equality case the facet-centroid leverage is3/2. The proof includes the whole closed parameter diamond and all genuine positive-area boundary facets.

These classes are complementary to TheoremA. At b=1/2,c=1/3 the upper graph facet has

    alpha=121/216>1/2,
    generalized ratios=(121/216,14641/20520,14641/10584).

It cannot have an equal-area opposite mate: such a mate would force V≥2w and hence alpha≤1/2. Nevertheless its full matrix inequality is strict. Its alpha is also below0.5769, inside the inherited unresolved leverage mass range. The exact source checks these values, plus all whole facets of seven actual parameter controls, including the degeneracies(1,0),(0,−1) and(1/2,1/2).

## 6. Strict centered moments on all facets of an actual E17 interval

This is a separate direct certificate, not an inference from an antipodal condition.

Let

    P0=conv{±e1,±e2,±e3,±(1,1/2,1/2)},
    P_t=P0∩{−3x+y+z≤3−t},    0<t<1.                (7)

The cut removes only the degree-three vertex−e1 before any other original vertex is reached. The complete true raw vertices, in order, are

```text
0=(1,0,0)             1=(0,−1,0)          2=(0,1,0)
3=(0,0,−1)            4=(0,0,1)
5=(−1,−1/2,−1/2)      6=(1,1/2,1/2)
7=(t/2−1,t/2,0)       8=(t/2−1,0,t/2)     9=(−1,−t/2,−t/2).
```

Its nine complete outward facet cycles are

```text
(2,3,5,9,7), (2,7,8,4), (1,4,8,9,5),
(0,1,3), (0,3,2,6), (0,6,4,1),
(1,5,3), (2,4,6), (7,9,8).
```

Thus its genuine lattice is10/17/9 throughout the entire open interval. This has pentagonal maximal facets, not the immutable heptagon–triangle H5 body.

The actual volume and centroid are

    V=(40−t^3)/24,
    g=(t^3(4−t)/[4(40−t^3)],0,0).

Writing R=40−t^3, its actual covariance is symmetric under y↔z, with

    Sigma_xx=(t^8−240t^5+1600t^4−3648t^3+17920)/(80R^2),
    Sigma_xy=Sigma_xz=(112−t^5)/(80R),
    Sigma_yy=Sigma_zz=(184−t^5)/(40R),
    Sigma_yz=(80−t^5)/(80R).

**Every one of its nine genuine whole facets satisfies**

    3Sigma/2−alpha_f T_f >0,    for every 0<t<1.      (8)

The exact verification integrates the complete moving boundary and every complete facet. To describe the matrix certificate explicitly, let D=6V, K=Dg, J=D E_P(xx^T) in raw coordinates. Let A0,A1,A2 be the raw zeroth, first and second facet integrals divided by its normal length, and H=hD−n·K. Define

    L=D^2 A2−D(A1K^T+KA1^T)+A0 KK^T.

Then the polynomial matrix

    3D^2(DJ−KK^T)−12HL

is exactly2D^4 times the physical centered gap in(8). The program proves its three leading principal minors strictly positive for each of the nine facets. It also proves all true supports, polygon turns, vertex ranks, pole denominators and volume signs.

There are **137 polynomial certificates and952 positive Bernstein coefficients**, all on the complete parameter interval, with no subdivision. The maximum polynomial degree is42. Endpoint factors t and1−t are removed only from geometry guards when necessary; all are positive on the stated open interval. No matrix-minor certificate needs an endpoint factor removed. The ends t=0,1 have different incidence and are not silently included in the10/17/9 claim.

At t=1/2 the independently recovered actual hull has V=319/192 and g=(7/2552,0,0). All nine strict matrix gaps are independently checked against the polynomial formula. This proves a genuine continuous E17 **moment constraint**, not U2, S2, a full escape-tree exclusion, or an equilibrium census.

## 7. Effective consequences and what remains open

On any of the proved subclasses, the requested inequality implies the weaker leverage bound because cc^T≤T:

    alpha c^T Sigma^(-1)c ≤3/2.

It also gives the actual-facet inverse inequality

    alpha^(-1)T^(-1) >= (2/3)Sigma^(-1),
    B >= (2/3)Sigma^(-1)−qq^T.                      (9)

Thus on physical spatial directions u with q·u=0, the curvature coefficient is at least2/3, stronger than the inherited1/Lambda* coefficient. The stronger opposite-section inequality(2) gives

    B >= (4/3)Sigma^(-1)−(1+1/alpha)qq^T,

and hence coefficient4/3 on those directions. These are full actual-moment consequences, not bounds for independently chosen endpoint covariances.

For a regular active completion of a **fixed released kernel**, the inherited B=−Hess log V interpretation may be applied to these inequalities when the actual completed body belongs to the stated subclass. It does not describe arbitrary simultaneous movements of all other facets. Similarly H0=alpha V T gives H0^(-1)≥2Sigma^(-1)/(3V), but a mechanical escape or a new attaining body still requires its genuine physical obligations.

### Limits of localization and numerical exploration

The primary Fradelizi–Guédon2004 Theorem3 says that with p constraints and s≤1/(p+1), an extreme measure has support dimension at most p; **when the dimension equals p**, it is s-affine and all p constraint integrals vanish. For p=2,s=1/3, the full-dimensional planar case has affine density, but the theorem neither makes its support a triangle/quadrilateral nor automatically gives the same conclusion in every lower-dimensional branch. Its statement does not justify replacing an equality EY=0 by the inequality EY≥0. The new proofs above do not invoke such a replacement. citeturn540875view0

Four larger actual-hull locators were run. Affine-thickness polygon searches with3 and5 additional supplied points returned centered second-moment maxima approximately1.4999999745 and1.4999997758 after15456 and34704 calls. An8-point leverage search returned1.4999999769 after69336 calls. A general triangular-facet3D hull search with6 positive-height supplied points returned1.4969116832 after56376 calls. All reached their configured iteration limits. Redundant points were removed by the actual hull; these call counts are not incidence coverage. They are not universal bounds or exact counterexamples.

The complete source and exact settings for those locators are preserved below. The harder arbitrary planar-support problem remains open in this handoff. Neither the centrally symmetric-base graph theorem nor the parallelogram all-facet theorem covers arbitrary affine-thickness polygons. The universal centered matrix and leverage assertions remain unresolved outside the proved domains; no failure of an exploratory algebraic certificate has been promoted to a counterexample.

## 8. Complete source recovery and observed exact evidence

The capsule contains all five complete source units: exact whole-hull/facet integration, subclass algebra and four-parameter verification, the complete E17 interval verifier, and both numerical locators. It does not require an old sandbox, output checkpoint or external research library.

Exact environment: **CPython3.13.5, SymPy1.14.0**, assertions enabled. The geometry and recovery code use only the standard library. Numerical discovery additionally used **NumPy2.3.5, SciPy1.17.0**, single-thread OpenBLAS/OMP. The exact verification has no dependency on numerical outputs.

Save the complete block below with its final LF as `recover_centered_facet.py`. Run

```sh
python -B -S recover_centered_facet.py fresh
cd fresh
python -B centered_subclasses_exact.py > exact.log
python -B e17_moment_interval.py > e17_exact.log
```

Expected and observed markers are

```text
CENTERED_FACET_SUBCLASSES_COMPLETE_SOURCE_RECOVERY_PASS
REGION 528 4868
ACTUAL_FACETS 65
CENTERED_WHOLE_FACET_MOMENT_SUBCLASSES_EXACT_PASS
E17_CENTERED_ALL_FACETS_MOMENT_INTERVAL_PASS 137 137 127828 9ceac0f011e617fcb8c0b618b049a72ae8a6801687e63ba4a8c709f31bebbfef
```

The65 count is40 exact whole-facet controls in the affine-thickness family plus25 facets of the nonsymmetric control; it is not the number of facets covered by the continuum theorems. The E17 interval contributes its separate nine whole-facet matrices.

Pins:

```text
centered_geometry.py —7285 bytes
d5a46b53940e87f3d5a9a4b40a90194f40c452cf3f9c4c368bc08da5ac8bd393
centered_subclasses_exact.py —13783 bytes
8b3148b3b3640b999e1dc61daa7aac5604da74653301a96c70bf52311e117b03
e17_moment_interval.py —5893 bytes
f46a45ad2bdc4b226e30b97afbf5b9f160956a0145bf608d9e8898048636e0db
centered_subclasses_exact_report.json —387079 bytes
3f803ffcaf958d06fcaf9cf9c457bb7a46cfdbaf355b2cf3d582d48788a083b9
e17_moment_interval_report.json —127828 bytes
9ceac0f011e617fcb8c0b618b049a72ae8a6801687e63ba4a8c709f31bebbfef
exact.log —162 bytes
ecf260103d166d217fbdea60f6a98519a2d74335945e834a1106fd26c4fc28a9
e17_exact.log —125 bytes
c89b6f416e550b5b4964f9e295102698d941a4cf0260134d77600c4bb2124f5d
Decoded five-source map —33702 bytes
b9b468e59ef8c4e9d127e87f6dc5c9eb35086df0999e89ab6d8c63a43dea766b
recover_centered_facet.py —15694 bytes
077b80a3a2628b5274d5d6ed9950205d710acefff48db4c7e73a5813b814e0a1
```

The generic geometry module is an exact descendant of the literal matrix parent's11905-byte `facet_matrix_exact.py`, SHA `d9c0671ab4deee1b8b28ce42843f0183786581c6281153fdff741829710daefb`; its complete modified text is in the capsule. No old one-fifth assertion is used to accept a new three-halves gap.

Optional numerical replay commands:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python affine_polygon_search.py 3 270943 second 160
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python affine_polygon_search.py 5 270944 second 240
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python affine_polygon_search.py 8 270946 mean 320
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python hull_centered_search.py 6 triangle 270945 260 second
```

All bounds, rounding-free parameterizations, seeds, population sizes, tolerances and iteration limits are literal in those sources. Floating replay is not promised to be byte-identical on another numerical stack. The exact reports are independent of it.

Convenience copies supplement the inline source: [complete certificate bundle](sandbox:/mnt/data/centered_facet_subclasses_certificate.zip), [subclass report](sandbox:/mnt/data/centered_facet/centered_subclasses_exact_report.json), [E17 interval report](sandbox:/mnt/data/centered_facet/e17_moment_interval_report.json), and [recovery source](sandbox:/mnt/data/centered_facet/recover_centered_facet.py).

```python
"""Recover the complete centered-facet subclass certificate and numeric locators."""
from pathlib import Path
import base64,hashlib,json,sys,zlib
PAYLOAD=r"""
c-qx{4U^hBvglu7v-Jua1lZ<dm?26%GLxL_B<GwYGn?Id9Evi=fM>uawwYm)%74GzEy<RRNpg1g-d8ufhq2{W>#No3FG*jYErX4p
JiGY%%v~;n(4Xz1&C@ChXNm8|-nzYedUo;b5BlG4`>h`bp1Y}SBF{~uxE6(*r*>^j8C&T(@a{uDNow<G5%@_hdhp}g$`AMOwI<Ql
*89ySX$ypZgu!+f#c3@{{s^O_?S~IR9EFqm@9$sz_VV5MX7=0Pf1TaF`S@ylbyJ`6x?LX?z<zyy43QyCo)UJKMByLdGLE*jotv&V
!MrBFzK7QgG~91@Pc=8Gg*yqIc){+eoj|4l+AF~>qwv8$ynz-Jpf*A1ZdMA&4^|KECRrCiqFowngD<`US_I3bANwI<pZO2bW}gOF
)0g9$S3KOc-8goijLF1mvzFbSGJK%FcAHu4>D2rKfEWI<mZWZ)7&|v+p?UE~Sc8AN9brfW4)`>=a2ny%Y{!1Gc6YuJGRJIt(eBAG
N4wqRf>~3{;U9K}d^Jb!G35cUd-sNcwPL%SX^H}H2zlNY#(M;RKf&ZS40#%Oeli_-9E)x_Q;})Tx9-6(T6W88>?Zcq?Cd7iw6+8)
+SP)v_P!P@Ynb%HGMlP4h`^r8V)xu`&KvKkf=!PeY>6DQZiCR+o6oI_*bNfD_Q~Ds{a0}u#fHqD#)00m@1ZF6eiG16)1Hc|1Xz{W
4OhNlvyC4@+gi4%YOr2Y6#x^IEvunkR8`#AcN6Z;69Wnpl+j-JsUhI(i)l;dfOeT3M`XI;>vcQXZw>blB-}Pf2?wY`$|DU?5Mo+A
3|JW4wO)jGb+%qJfR!}_N<z3rlp0hKc4KzB;?rFL0pxGJ2<l8g88=X)-=ff;Hj?He)XSC?`&`Zhg$8#jo604#mMVz#L)e5RVni#y
J)ZpbSdlNdga7Wa;rI2d_-WH=h+d$cFgpWF)PC!`A;0TDr;NPlfq%xQ7GR9_sUI8omEn)<J9o2NyWDAD5)cPvTY4JJz#Q~C-Kp6^
2$5%*@(kb7V@uB*Ez^k&)X?O1rwg?1b<PE-|G=q)hGG!LGG$OLS^CC@spGDE3AFV7Z%#i+w0ZCifW-m?_+Nn;ZFd_#^=s>B8v&Q~
qkTeLHjK8&v({ZG5@vy$`iq*I*3xzC`!zpY?4lq{Yip>+It5NFD7(wCkJoFOU5!T2php`X@5G}6k4Co@wC>FEOzDY~J1wOZC}t6K
iv+pu0(HspSq5`ImJNp9ZWuO9D9`K!l4N5)-Nzv?OD{F3)(L;#PNPkbq=w1ne7T9-)R>#hlaHRske6<K`3^584Kc@`JS$QI{Ff()
u@{->*<?%C^V1n%_Hr<hcFUJ(o(BEshuqhYiDn68^lY+hbVaIqHCf_Cu}Vb-=|3RH6DUkGWAj@V*qdVTA&0IoV0i<=Ts<H!9VNcM
D5g4)x{Ve-&r-V6Q2=zB6ybVP6WJ&7I+bR==+*oUFj2>n0|jgTCgIj7_My59j+1UQ_mh;jYyp6EjOKU7PSug>3F1M7;sRx7A~VB$
IShS*xss=(@soxF|9#<dm4h{I1SHMBOzNr!>%{x9oxF}?To*O3Q@_@yMMMA^MzGrN+Cc&$3-pEo=*$`rFZ{)|LlB(p5Auxu!Si=%
?G^ojMY<9QFaw4c*tSyTshi-N>bo!UVN!?H&E5JqA|SZzGV(d9GGcgPxBC|SvoCfr4qyHK?>9Gpd-?8For%sxAhz7>lQqAM_r8Wj
R<{LpkbEvoc(wdtz!0*D(dvPKz>HRxbxq*vO-N~<!#_s9_+^M+SRAf!Zo`ycL|a(omhOI&&LGu5a)gNoYZo++6V<U@v`at&;<m$}
soeHkwgrjM=rw;0{Lp8QQGAc|X|w%q0fHBxuLs+$zX*Vb)lJ0{MDIxv6uOSsL&!r$lK_7h5d{8--r=H;{%n2b(LP)xd@{if0oe;X
WJ(<}(K`gc4Dky~_8y2n37<#N#(-{a%LK&>QRXz3^^&0dHT*XFiq(ccSm$qTlv?X%`!R-^&Qkx78ko{vfRvgTavBA|7s8Y~ECG3P
cJDtWV&I$gKmG_+XGvnY`u#T`6wyH}@0JRp0dkwoLLkf83?|fUhJ0r>t6vEI^GEoMJ@cSgAf3f*<wroi@sm&y{`!~BK8ZW?AnbsA
UfVsT>nH?1E+qX|2iHq$kLzgTw@^-GHNmHW7#A{`cq=R+slSR{q{a~nx8cH#7d4REV;4&LBfJ6)<N+2mlC1?h-ny{rA7(xl0d=X}
ycyRP=bkk<v)y@b;rqTlAI_bj=l7gpue-GDVfSn}=nrjg;0$fM-(4=2%d?(6bk5IgYvKCKIh6EUgd!s>XZsCR2bLihh6}ZUq~?Nb
;jP_}v>|`7^4qGVQtV&GP#egVD2e~IOh7H;wFE*!Oo3K1ATQcN2U2kfgVBo?doPv1(9E@hTX_ps+j!fbP;J(3g5Ow8s6t{nq2-v(
%?rgHaPc<|jVD^j59|q-@-M-TfK2w<u#kjF-`LNKInzBzA;zIqomFJ=;wVXq*$fxft;QUdsg?^r@C2)#e6ldj5?`5ovN6pTUnN$Q
s>eA-Y||KpdQsXK5sq;gl;CNsLt}%-ApOJt%i>Ho&jE9I7bU))QM4Bu*cdCoE#P7=%P`^>s}(a(h)AC5oW@I2q{NsqR(Ku&&!LP*
U^rC33%RpmIOL$n@uVS{i~I+Cc2#-qVsX0Whi3JdQX)L5L`0yd1EvFHXX9#&Y2%PrBCcrA7e9`Sa$W<;kC~0`$$|2pe51O=*G9nk
-I09SHO-UAg75*yTgo+DP}#^$5+C*Uf?z6|Yj+kbCl#Yiei=PFm|$rM7ABw?n9)%XMsbptE(;xVu9IS+3dZCl6;GQ*Q9?mB#*@1#
{J%x-cOch0A~T~N(s_`faDhNDZB9gAsQI^B{HUhH-Lajd*6VK#Y&cG8dPg<GkpQBM7nWjGu!L=c6nMT7vb8Gi3ny7AG@Fz4bOZ|_
2WDtAi~~p^sQ!dxoyth<i&}uc@Ch!6hX#OY^Wn>MwBo>1jmDQ^@5+hL>8x~QS=BZ!EaTpj2QWfCVZkEF4Ka&2+VK#V@8EcJNEn3y
0Ma`6AY_~X3I4(njk0rqID+fFzc8>QSoQhF-Od+oEx3?Xz%fOP(63WgO0uU@)f2?upos>II=k1Uc9_|qPfcXjR1g*}%ryx+9qk$D
vVibN$Ta4YJu>S3)NB~u<N==_Kw*Y-^^EBXMryv%BM4;^K)c(~gH#SxcR)+E>OHQ5jZf+d<uhM!hv<eHLrG|JV)6+lVPHPz)&;${
LFUs1Y?0_fu_1J*St>V16(bQ{ZC2KRDqO4qB~cCJQ&t0dFV{dMmTCYL#YO!uAbV3F!bio0uxtQ=lBJ?t95bC60NCULWYf$}hO0>^
Sr9Jfa|XIDK6uF6(SQb7+OqAcs`nfdQRF-rXlTR2%~4^JU_tj6(<T*opBpHZlnAWkF|$w#U0!F@TX$!?W;@B3cVZemntF>9Us(Z6
lXFawZxSia#)N<UrVS&~>j|Ew<u^f_(bZO-_m1q*J8de7-jc8P`UkV152B{&hEKqxF1!d7t#I$>-`8A>L!Nn*Z1`l|lF3>(2#{$3
H;zHFfx&u?HUoI7C<4L6N2I<`_I68KfkB&I^VXV5*3*;Cv<eLeG{?mt4=VELkr;^ye3_~-7EFXCh~5v;j{qtiB1QZOU{;e4B>JSl
0ssqgRjQZZd;)zNgy(Hyn8lIPi3xHd>6_Tf*9N}9%LpgeNyeR{qKc@AiNwvYX?iW&SRF%S!OM#!F7G2WfoE*`tKjQP%#LlKtoig@
ev>FshbR*7GGGQmQ^Cc4BP4pm1+njnP?EY!_K1Y%M5bm}@`77OW(TStwdF#B88lFw8-Z$xS**f+zIx&GB8YPNI44s+!EY1ezL}W+
Cj%91D=Ek@#mq_yEAg-&&C)dcaEH>?i&A5$@7us$qzOZ^Bsqe(>Om$pnVO0omPc!a=qHU5frvvfjB*I`!B>5YZ(93g+mL0T4CG2V
`-pvkX4qAPsPb$!qQesy9U;su#Z;q~p%vK2sY1&X0#bF&7CsV)*;Io-7zFYwj)M2-EuY}uX`?&3=0ZT%h_u`~U6A0i(`l@&>9j~J
cV$-#(Ll>C6AZ3wI-<K=t`YC(ycsRH&}juxKpvBvC^V2R&_i>MKi(;IPcQJQ$rsq_x0qwmKx*prD#Yv3yh^xG$I#tT{FJeBgVt&D
0$@q?N)jgW?AWeci)#UL&4iM%=r|V3ElG0VuU=Rnxhg63Drezu&CyM;+PbnFsi$1AYg6KD*|O*rTLE>CK$xctnR{Ujf)^~{Nbi1_
!YY&yhp(lun7eC#5xW~0@lbdc{F*Dwv9)MfyZ!k0S2g7al>UWCRua|jY$~e3xXWgc*~zK%<Tzb9k}w^OG95{pBdAkh{rE10ie6L<
F)DC|KSQG^mm8AInWR#dQ77=(lkyqlED@5RWMOBC%z~sADM>BDAydq-%+3-;_Yo5C4~c(t<p9AKQDE1;btL_toB*Q_9~8|eNSmjq
K4OyY0iNjb!-wzCy(0<V(JBAK2a|?2Taj_SUX*78=T|}$f6Mt>@pR4kwWC{(QM!P+!BNfEDgMtcxi^9cFLN5ay;U^m{-;<U^x97_
zhb6Gek9_9jIV@z4<AjlV>k@~7Uq=nctlBxfeIoLRCJ1rZkqfNyW<j}9tGR%{*Y~c_!+JV<byo{1SIL_H2J_F5XkMVB%jBQ?XV9z
*k#5rZ*qotX^w6|;oyo@-mu$S5EeOh+9j~aJi9DFlmc1G4E2&2D$^LR#%nL(OPTN9YRD5%_CV~&WVBT-qlquT@IPnumub30uQ4}r
X$~4U4GGq{Qn;+=^zk{6aF_MWBZjzrFmBmrkOVwol7XsxhWX2NH{HwP(n1IsPO4k;XpQ*{$V6LTYK6TFbQA)?t;#E$!VRZm*e&Uh
6}UWH+OuBSZjG1hWdKzp8(@xn<?eLseJ195UNgvKjsOZ&DK719@TRM9A*sL_qL(V~YnZfs6A<b|1&WdX{Q`fct=+1&>c!|5msRX1
35bMTtO<%J#At0Lcf+2~=|fK~xCn_eD&|TKHQ`$!m7fD&BxQ*U<`~6Wcf(=5TrNRq=4*-unPIfoOnjRGPg|vHe#45BGjkm&GM9hR
?dJ2((hDzo2WHkxy5J#K90d!032UgwZuu>H$zjxIa)kKHpj6Hh1eF;zbOuAaPi8qR3?~$`nW1OQ3wBUfG5B1NLJ5&<&V!4NAkXK=
ealqsX8C~3K#%afl;<fG{Xlt2K_7_T6X?arABRC;w@CAe)Lhee@6S+V@((y%D0Fd>pu`uUSV~<+2>VQTwgU)tGpvit3RQKg0xGUL
gRHH5C8(Q=ZphIoDG^YHGj|816EQsv2q<K-I7xJQB%2SNyfF@H5kxg92}1M%dO+9gwW&PsNg4xKH57JI2KW^r??K)cs2{{kxMvU8
yo0hJe5=MJv_OW2W;4S$DWVdHriEcT6uqP{IlT>Xt0ePKW&xF#5~$z-?RK1t8i4`}U-|RcB_<5-dw0`P=#b&SSYRk+c=?{3t+j63
?za1^cJs7-|5UTvcCT%<YrjP`3NH!571VaO2g0bya75B58HPV3(LVNkbSNPJ;uMCS{T98D5q6Cb^F7c-cc7ypHfic7r4=ezjskV#
6%bCC0=AF)@ItzTYps{H?{!Yek9y>7R!+`Fg<BN$WG(zt#&jk-r~prP?T^%641-WKhhEy8;to1cMqzSTUmN5(XzxrW9zKic9Dyj7
xui2XcZ^i{q^QvGBw%;bBgfRZ?ZKEHd#A?jIC@O<60^>qNh-<0gJQP9hCuu0fXk@IwM`wB;kXHFX>2w&qc7aBoA}g<WuTmeIe`As
C^p15cvrr7P}>>_Gd9d(cE*&p_7Af(zLYcF-Tg$S<81f$Kh9=s8k=U^h#SzzjR~u%S;nG728(keZrWzU0PrS0sSrseYEkql(6q6&
n?~FsP|DD4V3r>Ihf!<}nnVjZp?zEfZS-2PgzXpLpg{_5KyXb0?=~GO0A88{s8tzx8|F)5#Ly<rKN=3}3X9JDeepvNK9n2uKH5AP
dBfldLx7CCI~JQ+?&by-w2j%u1=5RrSl$glII$TN)<c;GaNFYVaL8<W=(9|wkJk}a%d(kcStML>qV>Gu0AaR7&5JceSdd10R=3|B
^tuBJ<kF#)|EpLDw~&=1gWp;hau+A5c(XyQf~6%~NMVFh@9whHY%!<B;odB*&8i_(bF44Bu4)A&OW7iQjAp>}P_q;Qq?)0RxY{1g
PBaAQvvXea>I~$kjR?URJ>b`01s9nB@YEc|eBPL2WTXlf#&HC3*8vh~Jv1KLw<^X|tjaXF?h3?Io6&6Pbfr0Ha^bKGXUcE%h*toa
Bf+-jW=Dp!fffZwP@7FaWdqH2VquUt!JwdeuD~GOo^tqW<M-CQ;Ymcsd4uqp86*b90(sal_ARG@fw37(Qwx&?NQXfc4N<LzBSJ#u
4E=>0A3<kv%m%ebh|3L7)lhcbJT3R3XJo8GmOaMqYZ&m;8bUvwo1>SM0#%*21`_B}CV4RV5V9xUS_60<P`W)-W>JKIsok~kFSJ%>
Jg1yZ+mTuAb11IW?}^+4X@&R)$IQ)QX(|iWPn0$|GVtb;_kesS7wUhJquSC4XEJ6lr)=_)T~4QFr{6PAFt~B!vh}j@lG<=ZXpy1h
-+!UOX#JyO4|8U>*l`E@6Z&9CUC=zER&>vy`dL|vFoUv1Pc^$X!P&ht9q_19S7M@h%mzwoEp|t2whFX~pkWUB*V=m_cn0ZH4a5%L
_0~0S6D1&SCBZ7Jt=-KMgc9_#)(Bf7!nHz-TMa?)BXj2*rK8rot+pWOQ+HoKHp3rYXd|Qe?jjV`oU_*6Wcwn6Re~&(8S}+XZ3#GP
s$$s$$e^`GPtc#!6Li<3Aux}6i!!JR;0j^)X_R}A1u}5na_kdj{-b3`@`Uw>D3k_NQY}%dsdxED6ct6FIYy+%?k4yG{Y}zQGC~P5
@oQpoO6fB}`4ajWdIYyl)Sh#Ye`RmSaZ!%RLO`Ju;6=?iCT0XnC~~<NEetLcx$!rpuiX}YEw@q16M~<#5GjC3V9FNb3T;+VUoopH
6=Vfiy&+Q{ep@hOw8C>N`Wlu53xBr8&H!;6q(^CPM16EJNho5C;h&c#OlI*w@0aFunyp)eWC4nDmYbF~F{K%O71nsY00Q|(zW6OL
5E%n!!gNNl2eV9X!-+!RFcaA^oSG^cT$tm<ZdFzRA_IcJRFly+)p^=im88`!!T?lW$89xpvx$E^^EtOi+V(P0+ZNg)L||w_+tcbt
E3(p@vL#vg$M{49no+PLGtkQ8;2SPj^xi5Y6r~2070qeI%#M855ECRwl}c^`t*hX&fK{J7B2+ESB)r>YUS-fvpV${#J{t#EA)l0$
2a_pkK*WyXhAWu!AYkl#H|1UPn{Fdp@hm!HmwSU(t4Uob{q-s5L*f;frnG-dHRhczZiZo&hEGTzh9SBL*ObmVLzw{n$i`=H1mS6)
j-;@BG#E8=E(HPe*j|aXqr$Oj^iZ_7V^ALf3A(6HOLq2>vG6rb>yiO)IjNJdQJ*q+ysb~mmgjAt+YvJZWe^(Mz&vuWha9koc~P}X
VFD5mw=RxF(*Txe0<flHr-MD3`<xt}lVExb?|<F{6HcEvK$Ytt3sWE$x%C&VWGa9XRGOeFfD!`%Kq@Ry0F?-}y2y*=+&d~*#S@^P
8#_yc6{tLwdp5F4?iM9GEe*1uPBIkG@<YsM27o{j@H^50;Qh$_2VmQvvXaZ3@H2B=eJV`n&hciAa%Wa&=SSHgD-9xaYLWAlXn@u}
iYZ)HlQv?~NDBz*MR|l|)eu!i)L0|ifr9OU`9jp-$C;kLHu`6Sb7pHQT2|4L){>=@EC5`BR_M-vRV~%5YIQ$RA%Ty&P1YZ~t~cnR
8rpZP{MEMl!(JJUXpknY%rZg|sG)DfLsh;on$d{Qgb92{%aD&&ARJ}UPcQ6_Bg}O!F8Uy1!hb+^!FIou+aT&WZdeQocKA7;li6Ew
YQ9>P?81;kvuL^7VDltR#4y1&smoG#ugC}`-$Vq@o?0PrPcWb4fmAZO>C45JrqvJ#m4Qk`Wg$um<HERJ3^IiuXZqaIR<s=OqCoP+
EHBCo@5p(0vD>N6k?{l=ziikosuyBJZY3FGCDT${q(Q<>b2N4n`Uw4+1q`yeKN~!*5hVo|B44x53q!Tr9gh@6vmK9A7#>H$X5A3x
j&K>)XP2s8QE4=Vm4@UL4g6q~wBi%i6`gOIrz)G{y1VC-yW^Ts)&IhSDlhrneFaTW-9?>`yMlV+KI@63kq<4T-s$~wU+N!81!gI%
?YqS}Iqg*xT2YG1VK$7sz+>_WQI~c41@Z~QBl6isXkxFRpE2)=a)61BK3RMSTAY0EcDkca{FBujH!vOtGb#JZ^);W28!1(-(=(+5
pQ673Ob*azi+?nR!j7X*W|OevG*z)3+sY8*@+3`@S+$yajZ|t+*`T(;!C&wU7z>c_ovv1dTBkmI&`nl9ro|5*CIJhk{4;ig7>0a6
pb;`jwW5g)P~8Pg=QI_Yo&L#aj{sv}$nwwO?;Vy;&7=y@=IUvuIOLz$^)>tOAs_clEt~ssn52GyVa%H+MrO_V#!uKhI^==Yn<sv3
{l#RHHL@(ZFAcx6gJg#NC{I!t6HS7uE>2UZ{~e@{o$ukUa)inw!&ZAYUevYy>F9DzYm-gH);Rw{Qu4hhiWeBn2sK5601%cRCK&61
+GHz@S}#?@q!}PBSOHS&qTWO;ks`&i7G#_~Yc4g#MaR-EHl&UF>%)cHH0CXse0$-*W3;D<?bT+cLN~J1{00j2b`Qix`|E{`R&^tE
VVZ5HSn*wZfev4PCid};P*F~BV=w-NcQp7EdHO-;!3`OhzG%voYk^+@WkCkS?a#DX&x_Cpf|-qv20Ffsfcdzy9iA5OB-beBvxRC~
aA5v{5yoRhfWYCi7tv(LIwL`#P0N4IMHI8o0)-18g9FC7KqYS4{|^Y^SS`aH(H1l6*?>wCVa1`r8UZqfTe0<k3V*3sZT{u2wQ()+
(Lj*;DndgMP-eu#Si)e5C(xkFa=8bp3owWg#BxbebJru6lBl^pBC`G1#Ge=#hPBj(2N5^9Ha2oR0w6d%RRNgT9>iK>(ULmVo(1^;
rPvMH_?&d#U@@&--i1VoYTh23nFL)X96OrKj)528szIA5s0m`fjBs?&1`kX$#U2)!>K;_;G4ascoe6?Rob;r7E9Ghx`zzdLp6{;H
XEyQlI?S8me0TTOMHiAEKxtSovndY`fawWJ#7DzEXDH*t1JulHQj%~{2|JD1=&JQ(!D0Rzo2a=4Che&CPwdIe=D*;d-?F20Cb?Bz
-<464vw>4gM<7|3ggU19gU~5*bIU|?1s?=&g8J#9I)yDDJGED8{)C~XUzc(81&AKhXP`b!5fsHt>RMPwefn*rc2$gM{uTFEV9aCq
z}Dq}$1o}GtjN0|d@x5?3(<t&#O8yY*xHei?0Ve_=@^h5*+P%GMcyXdZ$(>Hv9ZN18JyB4McC=6uv?>IV?tH+%KIY7X<kv;>WvXt
h|=*PYuUm<Mi9~4nY_5H%W$XJ*Jbc+_BHrcXUV24Y~KCE9tsssyp!7~?wa@dHi`<dvt$`Msu}VMS*<&)R@M`u8)(UFi-=OMHP?dD
O8c`!n5-tbR_<$A{={~caz8*P{9vEPl7g<WH*DD(=JeFY4XxTDCW`Z(2pG=xQsi4HDt1y-%9r+eL2(MbOxvk$aZXIrk++T#KctgY
N~C)@+5rNXi#yijAt}16NI3#S3beO0c{Mmdf1u^fl!vM0?B|Ho;roTG*%x)ji6vB=)|b&d_TBrVc`V>DU<mDYbX3d{xyf)f=(c+?
4@4$2TjgKlqKyUvkTU5Q4i_VTRKSN=*b{f_*LLftgbrcYhXFKki)YWNRsQOVTO-hDa=idFxX~#^VR>Q?3rw<~iQqo9a|N?g)HXfP
UX@4g(yW@R8AW?l+~&MlvXxz3VNCV)HT*V`P7kV%PZ;jfzHPb<7k=lBIsAGJuYC(^n&d*DG+69|#mhQkwj3S%QLkEq#-}4!SJCf$
eGM8Bz+GFYvnn6-cg!Hg>{9aq1RpFB{Zxsf!g3*ymZ(ViDA=dW9#)J$*}CyPXpp+Glo=|rAJ=*sY!-@%7;;Vl6Pb}Dih~s%zr`nt
&-{dmg=EU#L*G2nF3prMEf!O2^4dh0Q_LS5XsXOIWowaW|AijryWEiCM&V!Uh@z+@qqw%r79=%3HGoi$EHQb%<vdJPyiD~+lidZ$
dlxO-4Nmp)`m%0((&83ElO{%1(R`hGgTW^Y6QM!-xweWlA&q$xqh1a%uCq5Ls32sBow@S}6ldT_AgYGxy3YEI1^n+#>l4s^g;<MT
D4BKcgM>_3>D)BP3wc^Skv}^i&;zP3NLP52j*vY>O|`y4*n*`OVL4@JG^(_GCS}vAuwdyRolHog#M8_0?_6%Fl!tXd<|!-2Hpy6A
F%v4hM-{=tf~<se$;C?^1dS|szi~M^t9PAGnh<+!O)E+elQ_$V*<dIz%2|eMNv6M%4spdgjwfH$2^bXxN)Z@)pV9NogY_j9st_ca
EbDUl1qtpjsq2bUeVPmEl<8R2kzQs^*Fh)nC{2Zfr!O2lz0A)u0^K0j502D}w8UCTMgeds>lfp{>r;~zzth+qCo2_!oOz&0^&IB(
OObg9oV$Zx8@=Hf8(1RpkUkdt!mo`%mpQ#Iwa@AI+1c4SIkN_RX7>gecTN1wu^S7qo$zCoxwBfq{7u1y<v8}44Pe9bvu@w1fIS_q
j|h~{^T3?5b9-<$=sDJzrj!|j;oz))Zg+dk?henLLDw3x*3jt>hW%d8$yTaLe=;>sx~Vg_vfcnjFXUPt72KTvg!zQKnOUj7wb?~q
^34HtC9t5+Dd3ZqP5VNiLvgDG6!lMB!t)s;`UdxSNYbtzkO~}`pGR|eQ=uk}N4MXzKtu03wr!(hQLWAy75vC^TLd}jyDe?t5#355
^Rs;YS@=8P+ypM`sN~ICkS9@cRAMXjF^Dfu7)Fj$GVm^H5)qzkOolN$p(5Mp3VlO4VTq<S+b0=S%uA?F+Aj3cSLr-xtmMH9D|S#~
NokOahhiL!^S8fnRJ@MTWz*hKJce*5mqSo&@uSD5hy)Nv*TIrF6^80kw2I(ZXDoA|23y>?QnqMR92&KKFy28U7~%YGTc+mdo!FWA
t~hn6EG@=kyEWkd?@CiDKYHk0p^~#IW+PD+*iCL#$tD9(ah|Nt60@R)vm!gv--ummK(~4`vUy+CgyRCl^n>gVh6W#)O#50TBcOea
FVIQE(^PXP`w`|8k|8`Wc|PG5xY#>UBXI&ArxC1JQ?t4W9N8-qPhOP8To(sYTQv&@oXRH8V8YJ#tJy3MlcI(wV=k{>zWVL<)yG#?
vwyt#{oSkC>+$8Q+u5(b{|d>oo4>!jd^f(id37`UWY<}?UxHWcoG7<R_CU6mMM3gXOgB3MRKaDu9BXz|M434W+bAztN|}TULGf3d
NMYq=QKMW&;zc{3*KZ#qAU}8W1dK}UBO+#(Z@(F#{*2aiJgrsjO6qnTARru>1U@f(4?2E98;bnT`vA{m4E9@$k9}pI;W4S3Juav1
EKJjV<odyta_bZfqggt%GCRytonG1YLk}3Op`V*sKe=lNItz!hcx>kUDfJUNbf|C?=EqmR{O$MO>bSwOVu297UY}0tnrH|t_(#ws
kujTove5D6?cc}m1bN<o_5%VX%3%kLI}wu*kz~SHE^ml(Pth2FHZyT8Yv23dKi<|!&cnttdH!QNS-T*nP+EKK9~J=!glT5UlDU6!
KE3)Uv}pDoUg|%0W~gtUNh<`&^YMeb(f7f<lDpkDatoXQt-%1M7`p9dQJzR>UKEFZ-17F~uu#JFNB9v*5(K(h)$ydne80EpjEGvD
(I2-@?LjN&)b^q&K1Qymrx`Rj-|^ulJ}(|hn3(!Wi27zi1H@d6sbhu(;;#6Mo0u4+7o$p#3<}C_v03D+GL~(Q?zuGrzC7`T7mp}w
vnZ+t6u>|le&Lug(80MnWemkGnx~UEKe~|+>8q%)J7??URGnF^86|N7#A>Bd&UC`2im1}>)FJ#_*raoO*vQHKRP5&_;ZB+FOE7r)
PZ{x0IqvVxN_TTz#6ul<f$qvK1?p;rOEUrZ!hEcU!3beQqW~ZC9k33lAVMn|Y3F;5F!i9|%+zAHKuv5M_e(QP8x=@$x7bIbs1XRR
bN{<Os+9edmrB=B3F&vWR2`zAr^*jSB^4&a89OhY`8Lt|D9&|8GRI~6IpKrYuwI|)XRj9MciNnwrK?3FU}}dhY96<ow9SjSs5HgW
WT)5qC%kXrvG+|htl&;KXoBdUak>?}Zfa@^uR_7Sh6kgeZ!I{K{AqaD-@orp`++|#IQ&m|)9Bp7lg>0ey3n|5ei7aygq5zeFaH@=
+K+r`|9gC8ung<IvWLu9_VClbGVA}NuWaF`R<*lKM8=Bq3(0S0Ry)qz6b}Zrbgp<r*KVqOX9y}%GVd8C{r5T0uCDUvmeJd{B@bA^
CHB9;1NQc<@_-3n*pEG6q66eMt*a{&JK^oy%1xr!9oN_2**|*9?*wSk$%Go2c4j4=caAop<&z<-|9YqFs-p2g?avr94*5<+@{I5Y
WH&rp#ws5`3;AJ+85W((xf7dyAB-JS1*Cx0gmEJzg&Q^s`R!BrL7Gq)p!@=Yjqg5)B`u8>5iGwS4H<$166>^F5W-aOTr$RS{8&B|
SKR`FM_(PgLA1azXe0cH2)^>dBCqWzMlV)us8Oe=VQrq<111Mei>*4&v*iZRDo`7>KleUuRkNBXu)A!Vy-lk&$%t+&_<)o~!;c&}
vcKq;H5#6Ie8oq}iv+5B^nhm78HH!j;bd7Nda~sHb@>_ZajJBIX_pF#?Rk3KnIr}Ar+k!}l5I-DP40V@VvasT#+Jsq#&(Hyjh({A
bobxmPU3jAO8%5B*05UV%e99uba<Nl9)^N*0XYEgDlxCIh0JSg3+B~@%InMvxEHZ6;9tbRfP)bWQ&(^0ogvxS7{oW|kg;9O#-MA)
&Ue@tc~RdKq_W1<l@iR}zSRlp-8+7D1z#Iurv<;p*lqy#yluXH+koP4&F0vG1WL;@{qhSpx|j)rwc*e8bxXoP-#d*rZyN93nLnuD
PHt{`$fb#rJY6)@K2#fOmwIDJRj+o*NZe(o%ud_vw>#eLr|&${&V2dhmx7YS<ymqLp79|IQhqeE(daQ%FMUU5d7VcUd8P}xb@t{>
rI3p%97;MzDCG4hFhdtXxGGAflCpmJWpZ)HF7BpMywM9#3*7PHVA`=@>P)bSJWxkFkuIF7bHb2!05dqjWO9al;xIAV4y}&*(A>h}
G^o79u|54!5!J5cvGZ@bmJ9!&UtF{qiSCz0Ku7<HBFsWmK}o2n3@@0Lgt^k(xhU-Y{psmYvGtYwllrNM@Zs2fw;CNKAN%Z96|M?0
nc)xf_Ng=*@OyeWO=(m5t`nQo<EsLe)!kdXZaq(*+avPlg=k|`wnjRWOYS7EQ$&Jt^~u513*Su(c94^S4pgtJtIi-lI8IP-J{b=k
6fCu)eBV}~(|jtE5&{g<0wM!6z<+TM3;fb69*Xp@Q+FX$M7wzjJ48J&L8O6)L3$#_Lis9)wkjJ^jJ}Wpg=QlcDFwTD9&>TZ_$+CP
>-O01x+UVDcS?+eKcd2@{bxK8uONG7Zy&!??g3?P{~Lb!G=3+{><leU(isuwUGitl{Lk1kym>3%-uk@@eiuRFArF3{GZaJ+5xGC)
omd;clYHLefgSqMb(!Z#MjZZ+T=V;<@9t$EupdYt`0u*LSAIq^V98VRy=%JU`EmQu08qT1SKQJj?x@4N+O+c!={u0Q8iRUa=LxV(
{pMhFBjAO>@-Mj)K+2`F0L{^Ss{z{`5U%ks2fQC)sbjG__K>yU+klXWCrT7JEpZ!hZG@{fZ>ykh)NW2!t<~-`{0~tSALUa^J(jAQ
$^D{|bjTG}(P8w1)u(#cGT1`!7E4`Ki8n85RwH$1Wm<h_CFT`3<UuxlUlOE)HayzpO-l8<m7#h&x-T`mQ<>gMS1QxuR<MR1-+Q@U
mu^{(`1>|qaw#qa26X`MG=4w9yMuwIHgxZDD=HrcU3nKVp8L%o>4xE|+lE&bHy-mlfzAA*1?o?)aaGc1FS${=D46c?mDl)|FY;yK
J$%2<0P>rA4aWl9`5nD0i>=Bh3#|CcYDOcE&$q4B=$3oSW(JQZ=8n|K$4Co})x?3ducUn+UB!FLF3r&<OFzDR_Yx7KVh%vnSB{FC
TYu`p(fkV0{?R?7Mt*a(#;90cpLanx-mECK8qv?)MatE2vig;}nU{uEb)c*47=H~!@E-b{kzM}1aQ|*m&{^eB;;5L*?_R*`aqZ^a
TYme!D|e6Y*9B=dyI+;(*Y#HJagevGR$Z=2TmV4+V|T0KrK(K(<KPvm|Mpd?=l|MGs@2!1(khd$Me<73KUahN?o_-qm1%z*yh2so
%SzpQ^4iq=9@pXpswBsJr5b+w7p_nJ(cP(|!nLW|Lhw^prQ%XvzMq+C*D|xh$L`c*<@=a(=swyFpM7J`cECEHU3`63x;j=9;U-<n
vDmZu+*vHo&z5J_VzKBu{k~({gTa~8b3JR>?=QRkq1SZ>-SfrVwfaM6c{UjI+@W)}=vnTfYd@Qwy5V(l<_!Dn*`n|E2J?RRyl45t
vt<|F&)wb}a-UoFd2iXXyk6h&mfhvK*YmoA;oP%^3%Boj!}+3n-YpbRc{uXK?w$?1?AdVMwR`Y0?+$v_{QUgfw-?^PUbya=>w5ix
)myk{y+Oa*wQTo%;GJ3XW#8%Awr|^KbBjtk6?ih~56_{9WpCj2`tHJ+FTCE|aRz=DN;-3wfN6fdv<KFCf8bhnuRmW7pc&`>aCknn
dc#3?;9HA17I9Ljo;W>_lb*R}{l4eg&Y5fX{Qj^v^c=?-+K$!p&xZ~aw;Z^A%bx?zzSZw}J*VrR4Z1zo_Rr>ixBqPV?c09=v>AeH
"""
def main():
    raw=zlib.decompress(base64.b85decode(''.join(PAYLOAD.split())))
    assert len(raw)==33702 and hashlib.sha256(raw).hexdigest()=="b9b468e59ef8c4e9d127e87f6dc5c9eb35086df0999e89ab6d8c63a43dea766b"
    obj=json.loads(raw);root=Path(sys.argv[1] if len(sys.argv)>1 else 'centered_facet_recovered')
    root.mkdir(parents=True,exist_ok=True)
    for name,source in sorted(obj['files'].items()):
        assert Path(name).name==name
        b=source.encode();pin=[len(b),hashlib.sha256(b).hexdigest()]
        assert pin==obj['pins'][name]
        p=root/name
        if p.exists() and p.read_bytes()!=b:raise FileExistsError(str(p))
        p.write_bytes(b);print(name,*pin)
    print('CENTERED_FACET_SUBCLASSES_COMPLETE_SOURCE_RECOVERY_PASS')
if __name__=='__main__':main()
```

## 9. Most useful continuation

The geometric opposite-section test and its quantified depth version can now be imposed directly on actual facet/volume moments, with no reference optimization. The affine-thickness results provide a complete positive benchmark for any justified planar localization, while the E17 cut interval supplies a noncentral, all-facet exact test outside the old H5 chart. The unresolved step is arbitrary centered actual geometry lacking these structures—not the already optimized one-constraint coefficients. Any further universal proof must retain the tangential mean and the actual planar support, and any negative result must provide an exact genuine whole-facet violation rather than a numerical hull or a formal moment law.
