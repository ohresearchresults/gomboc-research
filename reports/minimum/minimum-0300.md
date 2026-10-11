# minimum-0300

Historical AI scientific report · saved 2026-09-28 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# INCIDENT_ZERO_EDGE_ONE_ARC_SHARP_THREE_HALVES_V1

## 1. Determination and remaining scope

**The complete one-arc mechanism with a density-zero contact on the whole marked edge is closed.** There are two parts.

First, for both possible one-arc supports whose density vanishes on an edge incident to the marked edge, I prove the unconditional FULL marked three-dimensional matrix bound alpha T ≤ (3/2) Sigma. The constant is sharp in each family, as is the weaker centroid-leverage constant. The result covers the entire unbounded four-parameter domain, including arbitrary positive curvature before normalization and all affine images. It is not merely a necessary stationary condition. The transverse block has the stronger bound5/4. Positive-length curved members in the stated genuine domain have a strictly positive three-halves matrix gap.

Second, a self-consistent one-arc maximum cannot have an isolated density-zero marked endpoint either: a weighted whole-connector hinge reaction and a subsequent genuine inward parallel cut give a strict first-order ascent. Therefore **every hypothetical supercritical one-arc maximum must have strictly positive density on the ENTIRE marked edge**.

A separate advance applies to the remaining same-side two-arc class. Releasing its actual intervening density-zero chord into the common parabolic carrier replaces the old averaged boundary Gram penalty G_Gamma/2 by the full G_Gamma in the adapted-test density Hessian. This is a stronger necessary condition, not a complete exclusion of that class.

I did not determine every positive-marked-density one-arc alternative, the same-side two-arc class, or the universal constant. No strict actual counterexample, universal weak-attainment theorem, equilibrium conclusion, E17 exclusion or minimum improvement is claimed.

## 2. Exact input authority

The complete current journal and the complete newly supplied adapted-test source were read through EOF, including the literal immediate parent and all embedded source code. Their verified pins are:

```
research-journal.md: 361041 bytes; 1725 lines
b32cbf12d0a4203cb1c0f91ca2cfc6d4a7b50e78527e2767fe3c3ebc51938bf7
ADAPTED_TEST_DENSITY_HESSIAN_GATE_AND_EXACT_6_9_5_ASCENT_V1.md: 18838 bytes
db02c3d623c7ce39099ac610255dc9b962bdaa747b931cd43bd7c8a3db8117ae
```

Immediate literal parent: `[internal-source-reference]-`, SHA-256 `91b7c0b0ce11005bce9c62a5726cb7dcfb0877ca85d118a852e3e0234a3e6e71`. Reassembling its compact UTF-8 version-2 JSON envelope, with the Markdown's terminating LF, gives31661 bytes and that exact SHA. Its previously noted short report-pin typo remains resolved by its following full pin; there is no new mathematical or identity conflict.

The unchanged exact-reduction, clipping, conic-attainment, full convex-height and triangular45/32 evidence from the earlier turns remains available and was not silently replaced. In particular the immediate parent's zero-length opposite-wing chart is NOT treated as every one-arc body. No missing external archive or inaccessible sandbox is needed for the new proof or its recovery.

The imported conic theorem supplies actual strong attainment, the common self-consistent parabola, the restriction that positive-density straight edges meet marked endpoints, and the positive separation of a supercritical parabola from the marked edge. These are analytical inputs, not numerical vertex localization. The new adapted-test theorem is used only where stated in Section7. Neither imported program was assigned a routine replay here. fileciteturn4file4L40-L45 fileciteturn4file4L47-L85 fileciteturn4file0L53-L95

## 3. Both complete incident-zero-edge one-arc families

Use coordinates(t,r,z). The four parameters are

```
x>0, y>0, k>0, j>=0,
u=1+x, v=1+x+y,
D=x+y+2,
H=k(x+y)+j y+y².
```

Here x is the straight stem's horizontal length, y is the curved arc's horizontal length, k is the stem slope, and j is the nonnegative jump in slope at the join. Curvature is normalized to1. Define

```
U(r)=H(r+1)/D,
F(r)=0                                      for -1<=r<=1,
F(r)=k(r-1)                                 for 1<=r<=u,
F(r)=k(r-1)+j(r-u)+(r-u)²                    for u<=r<=v,
K={(t,r):-1<=r<=v, F(r)<=t<=U(r)}.
```

The two actual affine heights are

```
ell_U(t,r)=H(r+1)-D t,        upper return edge is density-zero;
ell_L(t,r)=D[t-k(r-1)],       lower stem is density-zero.
```

For either height use the uniformly filled body

```
P={(t,r,z):(t,r) in K, 2|z|<=ell(t,r)}.
```

The marked whole facet is P intersect{t=0}, projecting to the ENTIRE edge -1≤r≤1. It is a genuine positive-area triangle. Multiplying either height by any positive constant is allowed.

**Actual convexity.** F is convex: its slopes are0, k, and k+j+2(r-u). It is nonnegative, F(-1)=0 and F(v)=H, so the chord U dominates F throughout. For ell_U, nonnegativity is exactly t≤U. For ell_L, the core satisfies t≥0≥k(r-1), the stem has equality, and the arc has t-k(r-1)≥j(r-u)+(r-u)²≥0. The lift is convex because its defining upper/lower height constraints are affine over convex K. Its moments below are uniform-volume moments, not vertex masses.

**Why these are the complete incident-zero-edge alternatives.** At a one-arc supercritical conic maximum, orient the arc to the right of the marked-test interval. The lower connector joins(0,1) to the near arc end and the upper return joins the far arc end to(0,-1). If the zero edge meets a marked endpoint, it is one of these connectors. An additional off-mark corner would require a further nonzero-density straight edge with neither endpoint on the marked edge, forbidden by the imported boundary theorem; subdividing the zero line does not create another edge. The nonnegative affine density is therefore proportional either to U-t or to t-k(r-1). Normalize the quadratic coefficient by a positive t scaling and normalize the marked interval to[-1,1]. Convexity gives exactly j≥0. Thus the above is a genuine exhaustive chart for this mechanism, not an assumption that an unrelated corner lies on the parabola. fileciteturn4file4L55-L75

### Theorem A

For every body in either family, at its OWN uniform centroid g, with Sigma=E_P[(X-g)(X-g)^T], whole marked-facet T=E_F[(X-g)(X-g)^T], and actual alpha=Area(F)dist(g,F)/Vol(P),

```
alpha T < (3/2) Sigma
```

in positive-definite order. The optimal constant over either full family is3/2. The optimal weaker constant alpha c_F^T Sigma^-1 c_F is also3/2. No assertion about every other facet of the body is included.

## 4. Full-domain exact proof of Theorem A

All integrals in this section use the actual chosen ell. Put

```
V=int_K ell,       J=int_K t ell,       Q=int_K r ell,
K2=int_K t² ell,   L2=int_K tr ell,     M2=int_K r² ell.
```

The actual horizontal centroid is g_h=(J,Q)/V. The raw whole-edge moments(E0,E1,E2) are

```
ell_U: (2H, 2H/3, 2H/3),
ell_L: (2Dk, -2Dk/3, 2Dk/3).
```

Let f_h=(0,E1/E0). Then

```
Sigma_h = [[K2,L2],[L2,M2]]/V - g_h g_h^T,
T_h = [[0,0],[0,E2/E0]] - g_h f_h^T - f_h g_h^T + g_h g_h^T,
alpha = J E0/V².
```

Thus no facet is centered at its own mean in place of the actual volume centroid.

### Two exact polynomial positivity problems

Write G=(3/2)Sigma_h-alpha T_h and define

```
A = 2V⁴ G11 = 3V²(V K2-J²)-2J³E0,
O = 2V⁴ G12 = 3V²(V L2-JQ)+2J²(V E1-Q E0),
C = 2V⁴ G22 = 3V²(V M2-Q²)
                   -2J(V²E2-2VQ E1+Q²E0),
N = (A C-O²)/V² = 4V⁶ det G.
```

The actual six raw moments are rational polynomials in(x,y,k,j). The source generates them by exact integration over the upper triangle and subtraction of the two genuine under-floor regions. Its polynomial division by powers of D is exact and checked, not a rational approximation. The source also verifies the complete generic13-term expansion of N and independently compares the resulting matrix formulas with direct actual integrations.

Naive power-coefficient positivity fails: upper A and N have182 and660 negative coefficients; lower A and N have459 and2286. These failures are not negative values or counterexamples. The useful change is the complete width-balance split

```
b=y(j+y)/2>0.
Above balance: k=b+z, z>=0.
Below balance: k=tau b, 0<=tau<=1.
```

Above balance use the ordinary power basis in(x,y,j,z). Below balance use the power basis in(x,y,j) and the Bernstein basis binomial(n,i)tau^i(1-tau)^(n-i). This covers every admissible k, without an upper truncation, feasibility pruning or sampled sign inference.

The executed exact certificate is:

| Density | Polynomial | Original nonzero / negative | Above positive coefficients | Below positive coefficients | Bernstein degree |
|---|---|---:|---:|---:|---:|
| ell_U | A |2730 /182|3578|6998|10|
| ell_U | N |9640 /660|11933|24530|14|
| ell_L | A |3803 /459|4167|7493|10|
| ell_L | N |13740 /2286|13983|26580|14|

All99262 reported nonzero coefficients are strictly positive. Every above-balance polynomial contains a positive pure-y term. Every one of the below-balance Bernstein controls also contains a positive pure-y term. Hence A,N>0 when y>0, including j=0 and the balance wall. Since V>0, Sylvester's criterion gives G positive definite.

This is a finite exact certificate of a continuous unbounded family. The source reverses the ENTIRE above-balance substitution and expands the ENTIRE Bernstein expression back to its power polynomial. It does not check those identities only on a grid. All coefficient integers are regenerated by the inline source; the three-megabyte coefficient output is not a missing input. Large sparse products use exact integer Kronecker substitution with coefficient and exponent radices explicitly checked to preclude carry collisions, not floating FFT arithmetic.

### Direct transverse5/4 certificate

Set I3=int_K ell³ and E3=int_e ell³. Here

```
E3=4H³ for ell_U,         E3=4(Dk)³ for ell_L,
R_z=J E3/(V I3).
```

The exact polynomial5V I3-4J E3 has438 strictly positive nonzero power coefficients for ell_U and667 for ell_L, in the ORIGINAL variables(x,y,k,j). Therefore R_z≤5/4. These additional1105 coefficients give100367 positive coefficients in the complete acceptance run.

Reflection z→-z makes both the volume and whole-facet horizontal/vertical mixed moments zero. Thus the full3D marked matrix follows from the horizontal proof and5/4<3/2. Arbitrary affine images preserve the matrix inequality and transport every mixed test. This part of the new proof does not need a fresh invocation or replay of the older sharp transverse theorem.

### Boundary bookkeeping

Tangent joins j=0 are included. The formulas and coefficient proof extend to x=0 when the genuine whole marked facet remains the stated one; this is a limit with no lower straight stem, not a missing stationary case. Zero arc length and zero curvature can be handled by actual support/height continuity whenever volume and the marked facet remain nondegenerate. The positive-curvature conic mechanism itself has x,y,k>0 because its parabola is strictly separated from t=0.

Do NOT substitute k=0,x>0 into the old whole-edge interpretation: the t=0 support face then extends to r=1+x. In the upper-height case it must be renormalized as that enlarged whole facet; in the lower-height case ell=Dt gives zero marked area and is outside the problem. Likewise a volume-zero limit is not assigned a covariance inverse. No claim divides away an arc length or treats a shortened segment as a maximal facet.

## 5. Both constants are sharp, with exact actual sequences

For either density use the actual rational-data sequence

```
(x,y,k,j)=(n,1,1/2,0), integers n>=1,
Y_n=t-m_n, where m_n=int_P t/Vol(P).
```

The parabola minimum is n/2-1/16>0, so these are nondegenerate one-arc bodies in the genuine domain, not formal stationary curves. Direct actual moments give:

For ell_U,

```
V_n=(n+3)(5n+6)/10,
m_n=(35n²+84n+67)/[28(5n+6)],
R_n=45(35n²+84n+67)³ /
 [14(5n+6)²(3675n⁴+17640n³+42210n²+52220n+22263)].
```

For ell_L,

```
V_n=(n+3)(15n+32)/30,
m_n=(105n²+448n+520)/[28(15n+32)],
R_n=45(105n²+448n+520)³ /
 [14(15n+32)²(11025n⁴+94080n³+327600n²+533820n+327616)].
```

The numerator and denominator leading coefficients give R_n→3/2 in both cases, checked exactly. The actual normal test is constant on the entire marked facet, so its strong and weak scalar ratios coincide. Together with Theorem A and facet Cauchy, this proves that the FULL strong constant and the optimized weaker centroid-leverage constant are each3/2 in each family. It does not assert equality at any finite positive-arc member or classify equality in an enlarged closure.

## 6. Isolated marked density zeros are also impossible at a one-arc maximum

This is a separate analytical stationary exclusion, not an unconditional value inequality for arbitrary heights on the support.

At a hypothetical nonnormal supercritical one-arc maximum, write the actual self-consistent parabola as f, with positive leading coefficient A. Its first-variation kernel is Phi=(t-f(r))/J. Suppose a marked endpoint p=(0,r0) is the only zero of ell on K. The adjacent nonmarked connector reaches the actual arc endpoint q=(f(w),w); after reflection take d=w-r0>0. Let b=ell(q)>0. Parameterize the ENTIRE connector by

```
r=r0+d s,          t=f(w)s,          0<=s<=1.
```

Then

```
ell=b s,
Phi=(A d²/J)(1-s)(s-kappa),       kappa=f(r0)/(A d²).
```

A true two-sided connector hinge fixing p has stationarity

```
int_0^1 s [b s](1-s)(s-kappa) ds=0,
```

so kappa=3/5. More generally, with affine endpoint densities a,b≥0,a+b>0, the exact reaction gives

```
kappa=(2a+3b)/[5(a+b)],
int_0^1 [a(1-s)+bs](1-s)(s-kappa) ds
       =-(3a²+6ab+b²)/[60(a+b)].
```

In the isolated-zero case a=0 this implies

```
int_connector ell Phi dr = -A b d³/(60J)<0.
```

Now translate that WHOLE supporting line parallel INWARD by epsilon in t-distance and intersect with the original body. This is a genuine convex subset, not a separately movable integration patch. For a lower connector increase the floor; for an upper connector decrease the ceiling. The removed layer has the negative integral above, hence

```
(d/d epsilon) log R |0+ = A b d³/(60J)>0.
```

The moved endpoint shortens the whole marked edge, but ell(p)=0 makes its removed weighted edge moments O(epsilon²), so they have no first-order term. The volume mean is recomputed; its first-order effect is already exactly the actual-centering term in Phi. Thus neither the facet nor the test has been surrogate-recentered.

For completeness, a lower tangent join cannot evade the hinge equation: there kappa=1 and Phi is negative on the connector interior; the inward hinge alone removes negative-Phi mass and improves the ratio. It is realized by intersecting the old convex body with the tilted halfspace. An upper tangent return is incompatible with a nonempty strictly convex lower arc lying below it. At the remaining nontangent joins both hinge signs are admissible; positivity of ell away from its isolated marked zero persists on the small rotated cone.

This first-order ascent does NOT discard the parent's second-order density-zero marked-endpoint correction. That correction remains necessary for neutral first variations; here the leading derivative is already strictly positive. fileciteturn4file0L63-L84

If ell also vanished at another point, convexity and affinity would make the zero set a whole supporting segment through p. That is the incident-zero-edge case closed by Theorem A. Since B0>0 excludes ell vanishing on the entire marked edge, these two alternatives exhaust all one-arc supercritical maxima with any marked density zero. A surviving one-arc maximum must therefore satisfy min_e ell>0.

## 7. Full release of the same-side zero chord strengthens the Hessian

Consider a self-consistent same-side two-arc candidate whose two arcs are separated by the unique density-zero chord Gamma. Replace ONLY that chord in the lower boundary by the continuation of the SAME parabola across its gap, leaving the rest of the support fixed. Call the resulting compact convex carrier Q. It is convex because the intervening parabola has precisely the monotone slopes of the two adjoining arcs. The original body is

```
K=Q intersect{ell>=0}.
```

The signed values of ell on Q\K are never treated as a probability density. They define the following ACTUAL affine-height lifts, for either sign of small s and any affine psi:

```
P_s={(x,z):x in Q, 2|z|<=ell(x)+s psi(x)},
K_s=Q intersect{ell+s psi>=0}.
```

These are convex uniform bodies. Gamma is transversely interior to Q except at its two endpoints. It is disjoint from the marked edge, where the density is strictly positive: otherwise the zero face would connect to a marked endpoint and would not be the chord between two off-mark arcs.

For every bounded continuous raw test a(x), coarea across Gamma gives, for BOTH signs of s,

```
int_Q a(ell+s psi)_+
 = int_K a(ell+s psi)
   + s²/(2|grad ell|) int_Gamma a psi² ds + o(s²).
```

Unlike clipping only inside K, release admits the added strip on the formerly negative side as well as deletion on the positive side. Thus the positive/negative parts combine into the FULL psi² for each sign. At the two chord endpoints the parabola and chord have distinct slopes, and their vanishing-width contributions are o(s²). The whole marked edge is unchanged and has no density-zero endpoint term in THIS class.

Here are the precise adapted-test quantities, so continuation does not require recovering a hidden convention. Let Y be the actual-centered maximizing test, eta=B1/B2, and

```
Z=t-m+m eta Y,
D_Z=int_K ell Z²,       C_Z=int_e ell Z²,
gamma=D_Z/I-C_Z/B2>0.
```

The positivity and the simultaneous volume/facet orthogonality of Y,Z follow from test stationarity and the strict normal spectral gap at R>3/2. For affine psi define

```
pY=int_K psi Y/V,       pZ=int_K psi Z/V,
B_Z=int_e ell Z,
Kpsi=int_e psi YZ/B2-pY B_Z/B2-pZ B1/B2-int_K psi YZ/I.
```

All derivative bulk integrals here are UNWEIGHTED area integrals. Remove the scaling direction from psi so int_K psi=0 and set

```
p=pY, jpsi=int_K t psi/J, qpsi=int_K Y² psi/I,
E1psi=int_e Y psi,
H_form=2jpsi(qpsi-jpsi)+2p²(B0/B2+V/I)-4p E1psi/B2.
```

Use the actually recentered tests Y_s,Z_s on the new uniform P_s and choose Y_s+s(Kpsi/gamma)Z_s. The exact necessary second-order condition becomes

```
H_form(psi)+2Kpsi²/gamma+G_Gamma(psi)<=0,
G_Gamma(psi)=int_Gamma Phi psi² ds/|grad ell|.
```

This is stronger than the former averaged condition with G_Gamma/2. It follows from the new full-release raw expansion and the accepted adapted-test identity; an O(s) test change times the O(s²) boundary correction has no second-order contribution. It holds at a full joint maximum, not a maximum confined to the unreleased fixed support. The old adapted-test formula alone did not supply this full Gram penalty. fileciteturn4file0L16-L28 fileciteturn4file0L32-L49 fileciteturn4file0L71-L95

There is an explicit positive definite quotient form. Normalize f(r)=r²+2Br+C and ell=t-Z_line(r), where Z_line is the chord of f between c<d. Put a0=(c+d)/2 and w=(d-c)/2. If psi restricted to Gamma is A0+B0(r-a0), then

```
Phi|Gamma=[w²-(r-a0)²]/J,
G_Gamma=4w³/(3J) [A0²+(w²/5)B0²].
```

This exact identity is checked by the source. It is strictly positive unless psi is proportional to ell, the removed scaling direction. The result does not assert that every actual candidate fails the strengthened matrix gate. Isolated off-mark zero contacts and other positive-marked-density one-arc arrangements require their own analysis.

## 8. Exact actual curved controls and useful failed methods

The standalone recovery supplies six complete actual curved lifts: both density types at

```
(x,y,k,j)=(1,1,1/4,1/2), (4,1,1/2,0), (2,1,1,1/2).
```

They exercise below-balance, balance and above-balance geometry. All have positive parabola minimum but are NOT asserted self-consistent stationary points. For each, direct fibre integration independently verifies the polynomial moments, actual3D centroid and covariance, actual whole marked triangle, its independent triangle second-moment formula, and all FOUR positive-area maximal flat support faces. The remaining side is curved, so there is no finite polytope or equilibrium census. All six are nonviolating.

The balanced pair is especially useful because its actual normal ratios exceed the sharp triangular-lift45/32 bound, while remaining below3/2. Thus the new one-arc theorem is not just a re-labeling of that triangular-support theorem. The planar support is the same in the two controls:

```
D=7, H=7/2, u=5, v=6, U(r)=(r+1)/2;
floor:0 on[-1,1], (r-1)/2 on[1,5],
      (r-1)/2+(r-5)² on[5,6].
```

### Upper-zero balanced control

```
ell=7(r-2t+1)/2,
V=91/5,        g=(963/728,35/12,0),
Sigma=[[2976263/4769856,3389/2912,0],
       [3389/2912,31349/13104,0],
       [0,0,5299/2808]],
T_marked=[[927369/529984,9951/2912,0],
          [9951/2912,331/48,0],
          [0,0,49/24]],
alpha=4815/9464.
```

The WHOLE marked triangle has raw vertices(0,-1,0),(0,1,-7/2),(0,1,7/2). The exact normal ratio is40187535615/28167353032. The actually centered mixed test

```
Y=(2184r+6552t-15037)/6552
```

has ratio198192573387/135343708136. The transverse ratio is43335/78728.

### Lower-zero balanced control

```
ell=-7(r-2t-1)/2,
V=322/15,      g=(499/322,125/46,0),
Sigma=[[1034251/1244208,94419/59248,0],
       [94419/59248,48221/14812,0],
       [0,0,3577/1656]],
T_marked=[[249001/103684,210079/44436,0],
          [210079/44436,60491/6348,0],
          [0,0,49/24]],
alpha=7485/14812.
```

The WHOLE marked triangle has raw vertices(0,-1,-7/2),(0,-1,7/2),(0,1,0). The exact normal ratio is5591317455/3829831453. The actually centered mixed test

```
Y=(161r+483t-1186)/483
```

has ratio46183457980/31173849917. The transverse ratio is22455/47012.

The code checks both actual mean equalities, int_P Y=0 and E_P[t/m]=1, and verifies every marked three-halves matrix gap by exact principal minors. Other whole-flat-face moments are preserved as exact generated data; no unproved all-face bound is attributed to them.

The direct coefficient failure recorded in Section4 is retained with its exact negative-term counts and reconstruction, but is superseded by the complete balance certificate. The value proof does not interpolate the nonlinear ratio across independently chosen densities: a positive mixture of the two certified height rays is not automatically covered. Nor does a finite nonviolating control set exclude the positive-marked-density alternatives.

## 9. Continuation frontier and evidence tier

The complete new conclusion is the sharp full-matrix value theorem for both incident-zero-edge one-arc families, plus exclusion of an isolated marked zero at a supercritical one-arc maximum. Therefore the remaining one-arc search should retain min_e ell>0 and genuinely allow its off-mark zero line or corner to be off the parabola. Strictly positive densities and isolated off-mark zero contacts are not eliminated here. Same-side two-arc candidates now have the full-release adapted Gram condition, but have not been excluded.

The most concentrated next problem is the positive-marked-density one-arc system with actual density stationarity, self-consistent mean coefficients and the new source's adapted spectral term. The immediate parent's required negative inward raw slice-inertia derivative remains a useful condition there; its opposite-wing positivity proof must not be transplanted to a nonconic opposite corner. For the same-side chord case, evaluate the stronger full G_Gamma condition rather than its older half penalty. These are actual-support problems, not free-moment or vertex-budget relaxations.

The analytical arguments in Sections3,5–7 are separate from the executed finite coefficient certificate of Section4. The latter exhausts its continuous parameter domain because its basis identities and all coefficients are checked exactly. The six actual controls audit geometric conventions; they are not the universal proof. The universal3/2 and general weaker problem remain unresolved, and there is no new mechanical implication.

## 10. Complete standalone recovery and executed pins

Save the entire following source as `one_arc_zero_edge_exact.py`, with its final LF. Exact acceptance used CPython3.13.5 and SymPy1.14.0, assertions enabled. No optimizer, random seed, parent code, coefficient input, checkpoint array or archive is required.

```
python -B one_arc_zero_edge_exact.py > one_arc_zero_edge.log
```

A normal execution and a fresh directory initially containing ONLY this source completed successfully. Source, full coefficient output, report and stdout were byte-identical. This is current-worker exact execution, not a claimed coordinator replay or proof-assistant formalization.

```
one_arc_zero_edge_exact.py:19162 bytes
63fbb449819f5f93513834214530c3a3bfd01ddf090e4726c78160363538aa2c
one_arc_zero_edge_coefficients.json:3002813 bytes
54306cdeb38d4412fb97c043c72deb9f87ab3b6afb131a061a741c6c7a85f2f0
one_arc_zero_edge_report.json:52473 bytes
52d6b4e1c1539cd478fff993a1f0e9fa39fabca9e12105b82f183034b896ff27
one_arc_zero_edge.log:508 bytes
93eccee453e156d7cdbb2d96dc57fc975b760bb6a2400461a6ecbc5fef9c6614
```

Expected terminal output:

```
BOTH_COMPLETE_ONE_ARC_ZERO_EDGE_FAMILIES_PASS
EXACT_POSITIVE_COEFFICIENTS 100367; FULL_BASIS_RECONSTRUCTION_PASS
FULL_HORIZONTAL 3/2 AND TRANSVERSE 5/4; ALL_PARAMETERS_PASS
SIX_ACTUAL_CURVED_CONTROLS; WHOLE_MARKED_AND_24_FLAT_FACETS_PASS
BOTH_NORMAL_SHARPNESS_LIMITS 3/2; BOUNDARY_IDENTITIES_PASS
COEFFICIENTS 3002813 54306cdeb38d4412fb97c043c72deb9f87ab3b6afb131a061a741c6c7a85f2f0
REPORT 52473 52d6b4e1c1539cd478fff993a1f0e9fa39fabca9e12105b82f183034b896ff27
INCIDENT_ZERO_EDGE_ONE_ARC_EXACT_RECOVERY_PASS
```

Convenience copies supplement the complete inline recovery: [standalone source](sandbox:/mnt/data/one_arc_zero/one_arc_zero_edge_exact.py), [source, coefficients and exact outputs](sandbox:/mnt/data/one_arc_zero_edge_capsule.zip). The capsule is1098088 bytes, SHA-256 `2efec7cfbddc86f4e1115ce4f8bca5523a38571d50f3f39da21e9eaf96fbb762`.

```python
"""INCIDENT_ZERO_EDGE_ONE_ARC_SHARP_THREE_HALVES_V1.
Exact acceptance: CPython 3.13.5, SymPy 1.14.0, assertions enabled.
No input files, optimizer, seeds, coefficient tables or parent code required.
The source proves the finite all-parameter polynomial certificates, verifies
actual uniform curved controls, and checks the two boundary-variation identities.
"""
from pathlib import Path
from math import gcd, lcm, comb, factorial
from functools import reduce
from fractions import Fraction
import hashlib, json
import sympy as S

# Rational sparse polynomials. Large products use exact integer Kronecker
# substitution, not FFT or floating arithmetic. Exponent radices exceed the
# coordinatewise product degrees; balanced coefficient radix exceeds 4 ||a||1||b||1.
class P:
    def __init__(self, terms, den=1, n=4):
        self.n=n
        if isinstance(terms,int): terms={(0,)*n:terms}
        terms={tuple(m):int(c) for m,c in terms.items() if c}
        if den<0: den=-den;terms={m:-c for m,c in terms.items()}
        g=reduce(gcd,terms.values(),den)
        self.t={m:c//g for m,c in terms.items()};self.d=den//g
    @classmethod
    def from_sympy(cls,p):
        den,num=p.clear_denoms(convert=True)
        return cls(dict(num.terms()),int(den),len(p.gens))
    def __eq__(self,b):
        return isinstance(b,P) and self.n==b.n and self.d==b.d and self.t==b.t
    def __add__(self,b):
        if not isinstance(b,P): b=P(b,n=self.n)
        den=lcm(self.d,b.d);a=den//self.d;c=den//b.d
        out={m:v*a for m,v in self.t.items()}
        for m,v in b.t.items(): out[m]=out.get(m,0)+c*v
        return P(out,den,self.n)
    __radd__=__add__
    def __neg__(self): return P({m:-c for m,c in self.t.items()},self.d,self.n)
    def __sub__(self,b): return self+-b
    def __rsub__(self,b): return -self+b
    def __mul__(self,b):
        if not isinstance(b,P): b=P(b,n=self.n)
        if not self.t or not b.t: return P(0,n=self.n)
        if len(self.t)*len(b.t)<10000:
            out={}
            for m,c in self.t.items():
                for nn,d in b.t.items():
                    kk=tuple(a+b for a,b in zip(m,nn))
                    out[kk]=out.get(kk,0)+c*d
            return P(out,self.d*b.d,self.n)
        da=[max(m[i] for m in self.t) for i in range(self.n)]
        db=[max(m[i] for m in b.t) for i in range(self.n)]
        rad=[da[i]+db[i]+1 for i in range(self.n)];step=[1]
        for r in rad[:-1]: step.append(step[-1]*r)
        bound=sum(abs(v) for v in self.t.values())*sum(abs(v) for v in b.t.values())
        width=(bound.bit_length()+9)//8;base=1<<(8*width);half=base//2
        assert base>4*bound
        def pack(terms):
            vals={sum(i*j for i,j in zip(m,step)):v for m,v in terms.items()}
            size=(max(vals)+1)*width;pos=bytearray(size);neg=bytearray(size)
            for ix,v in vals.items():
                target=pos if v>0 else neg
                target[ix*width:(ix+1)*width]=abs(v).to_bytes(width,'little')
            return int.from_bytes(pos,'little')-int.from_bytes(neg,'little')
        result=pack(self.t)*pack(b.t);sgn=1 if result>=0 else -1;result=abs(result)
        raw=result.to_bytes((result.bit_length()+7)//8,'little')
        raw+=bytes((-len(raw))%width);out={};carry=0
        for ix in range(len(raw)//width):
            c=int.from_bytes(raw[ix*width:(ix+1)*width],'little')+carry
            if c>=half: c-=base;carry=1
            else: carry=0
            if c:
                assert abs(c)<=bound
                kk=ix;mm=[]
                for r in rad: mm.append(kk%r);kk//=r
                assert kk==0
                out[tuple(mm)]=c*sgn
        assert carry==0
        assert sum(out.values())==sum(self.t.values())*sum(b.t.values())
        return P(out,self.d*b.d,self.n)
    __rmul__=__mul__
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        out=P(1,n=self.n);a=self
        while k:
            if k%2: out=out*a
            k//=2
            if k: a=a*a
        return out
    def evaluate(self,values):
        return sum((Fraction(c,self.d)*reduce(lambda a,b:a*b,
                    (Fraction(v)**e for v,e in zip(values,m)),Fraction(1))
                    for m,c in self.t.items()),Fraction(0))

Q=S.Rational
x,y,k,j,z,r,t=S.symbols('x y k j z r t',real=True)
variables=(x,y,k,j)
D=x+y+2;H=k*(x+y)+j*y+y*y

def simp(f): return S.factor(S.cancel(f))
def zero(f): assert simp(f)==0, simp(f)
def integral(f,v,a,b):
    return simp(sum(c*(b**(m[0]+1)-a**(m[0]+1))/S.Integer(m[0]+1)
                    for m,c in S.Poly(S.expand(f),v).terms()))
def iz(f,b):
    return S.expand(sum(c*b**(m[0]+1)/S.Integer(m[0]+1)
                       for m,c in S.Poly(S.expand(f),z).terms()))

def raw_polynomials(kind):
    # Integrate first in T=D*t, with height D times the canonical rho.
    # Division by D^(p+1) gives the actual moments in coordinates (t,r)
    # with ell_U=H(r+1)-D*t or ell_L=D*(t-k(r-1)).
    def primitive(p,q,R,T):
        if kind=='upper':
            f=H*(R+1)*T**(p+1)/S.Integer(p+1)-T**(p+2)/S.Integer(p+2)
        else:
            f=T**(p+2)/S.Integer(p+2)-D*k*(R-1)*T**(p+1)/S.Integer(p+1)
        return R**q*f
    out={};divisor=S.Poly(D,*variables)
    for p,q in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]:
        expr=iz(primitive(p,q,z-1,H*z),D)
        for length,R,T in [(x,1+z,D*k*z),
                           (y,1+x+z,D*(k*(x+z)+j*z+z*z))]:
            expr-=iz(primitive(p,q,R,T),length)
        poly=S.Poly(expr,*variables).exquo(divisor**(p+1))
        assert all(c>0 for m,c in poly.terms())
        out[p,q]=poly
    E=2*H if kind=='upper' else 2*D*k
    F=E/3 if kind=='upper' else -E/3
    edge=[S.Poly(E,*variables),S.Poly(F,*variables),S.Poly(E/3,*variables)]
    return out,edge

def vertical_polynomials(kind,mom):
    expr=0
    for length,R,L in [(2,z-1,S.S.Zero),(x,1+z,D*k*z),
                       (y,1+x+z,D*(k*(x+z)+j*z+z*z))]:
        U=H*(R+1);stem=D*k*(R-1)
        f=((U-L)**4 if kind=='upper' else
           (U-stem)**4-(L-stem)**4)/S.Integer(4)
        expr+=iz(f,length)
    I3=S.Poly(expr,*variables).exquo(S.Poly(D,*variables))
    E3=S.Poly(4*H**3 if kind=='upper' else 4*(D*k)**3,*variables)
    gap=(5*P.from_sympy(mom[0,0])*P.from_sympy(I3)
         -4*P.from_sympy(mom[1,0])*P.from_sympy(E3))
    assert len(gap.t)==({'upper':438,'lower':667}[kind])
    assert all(c>0 for c in gap.t.values())
    return I3,E3,gap

def gap_polynomials(mom,edge):
    V,J,Y,K,L,M=[P.from_sympy(mom[key]) for key in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]]
    E,F,B=P.from_sympy(edge[0]),P.from_sympy(edge[1]),P.from_sympy(edge[2])
    A=3*V*V*(V*K-J*J)-2*J**3*E
    N=(4*(E*B-F*F)*J**4-6*E*J**3*M*V+12*E*J**2*L*V*Y
       -6*E*J*K*V*Y**2-12*F*J**2*L*V**2+12*F*J*K*V**2*Y
       +6*B*J**3*V**2-6*B*J*K*V**3-9*J**2*M*V**3
       +18*J*L*V**3*Y+9*K*M*V**4-9*K*V**3*Y**2-9*L**2*V**4)
    return A,N

def shift_balance(obj,sign=1):
    # k = z + sign*y*(j+y)/2. Output variables (x,y,j,z).
    n=max(m[2] for m in obj.t);out={}
    for (a,b,c,d),v in obj.t.items():
        for i in range(c+1):
            coeff=v*comb(c,i)*2**(n-c+i)*sign**(c-i)
            for h in range(c-i+1):
                m=(a,b+2*(c-i)-h,d+h,i)
                out[m]=out.get(m,0)+coeff*comb(c-i,h)
    return P(out,obj.d*2**n)

def below_balance(obj):
    # k=tau*y*(j+y)/2; return its exact Bernstein controls in 0<=tau<=1.
    n=max(m[2] for m in obj.t);raw={}
    for (a,b,c,d),v in obj.t.items():
        for h in range(c+1):
            m=(a,b+2*c-h,d+h,c)
            raw[m]=raw.get(m,0)+v*comb(c,h)*2**(n-c)
    fac=factorial(n);out={}
    for (a,b,d,c),v in raw.items():
        for i in range(c,n+1):
            m=(a,b,d,i)
            out[m]=out.get(m,0)+v*comb(i,c)*(fac//comb(n,c))
    result=P(out,obj.d*2**n*fac)
    # Expand the complete Bernstein identity back to its power polynomial.
    back={}
    for (a,b,d,i),v in result.t.items():
        for h in range(n-i+1):
            m=(a,b,d,i+h)
            back[m]=back.get(m,0)+v*comb(n,i)*comb(n-i,h)*(-1)**h
    assert P(back,result.d)==P(raw,obj.d*2**n)
    return n,result

def coefficient_record(name,obj,basis,degree=None):
    assert obj.t and all(c>0 for c in obj.t.values())
    rec={'name':name,'basis':basis,'denominator':obj.d,
         'terms':[[*m,c] for m,c in sorted(obj.t.items())]}
    if degree is not None: rec['Bernstein_degree']=degree
    return rec

def certify(kind,mom,edge):
    A,N=gap_polynomials(mom,edge);cert=[];summary=[]
    expected={'upper':[(2730,182,3578,6998),(9640,660,11933,24530)],
              'lower':[(3803,459,4167,7493),(13740,2286,13983,26580)]}
    for label,obj,pin in zip(['pivot','determinant'],[A,N],expected[kind]):
        assert (len(obj.t),sum(c<0 for c in obj.t.values()))==pin[:2]
        above=shift_balance(obj)
        # Invert the complete shift, not just at selected parameter values.
        swapped=P({(a,b,d,c):v for (a,b,c,d),v in above.t.items()},above.d)
        inverse=shift_balance(swapped,-1)
        target=P({(a,b,d,c):v for (a,b,c,d),v in obj.t.items()},obj.d)
        assert inverse==target
        degree,below=below_balance(obj)
        assert (len(above.t),len(below.t))==pin[2:]
        assert any(a==d==e==0 and c>0 for (a,b,d,e),c in above.t.items())
        for i in range(degree+1):
            assert any(a==d==0 and e==i and c>0 for (a,b,d,e),c in below.t.items())
        cert.append(coefficient_record(kind+'_'+label+'_above',above,'power (x,y,j,z)'))
        cert.append(coefficient_record(kind+'_'+label+'_below',below,
                    'power (x,y,j), Bernstein_i^n(tau)',degree))
        summary.append({'quantity':label,'original_nonzero':pin[0],
                        'original_negative':pin[1],'above_positive':pin[2],
                        'below_positive':pin[3],'Bernstein_degree':degree})
        # Independent exact matrix evaluation at two nondefault rational inputs.
        for values in [(1,1,Q(1,4),Q(1,2)),(2,1,1,Q(1,2))]:
            sub=dict(zip(variables,values));mm={p:simp(v.as_expr().subs(sub)) for p,v in mom.items()}
            ee=[simp(v.as_expr().subs(sub)) for v in edge]
            V,J,Y,K,L,M=[mm[p] for p in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]]
            g=S.Matrix([J,Y])/V;cov=S.Matrix([[K,L],[L,M]])/V-g*g.T
            tf=S.Matrix([[0,0],[0,ee[2]]])/ee[0]
            ef=S.Matrix([0,ee[1]/ee[0]])
            tf=tf-g*ef.T-ef*g.T+g*g.T
            G=Q(3,2)*cov-(J*ee[0]/V**2)*tf
            actual=2*V**4*G[0,0] if label=='pivot' else 4*V**6*G.det()
            vals=[Fraction(int(v.p),int(v.q)) if isinstance(v,S.Rational) else v for v in values]
            zero(S.Rational(obj.evaluate(vals))-actual)
    return cert,summary

def actual_control(kind,values,mom,I3):
    sub=dict(zip(variables,map(S.Rational,values)))
    xx,yy,kk,jj=[sub[v] for v in variables];DD=xx+yy+2
    HH=kk*(xx+yy)+jj*yy+yy*yy;u=1+xx;v=u+yy
    lower=kk*(r-1);curve=lower+jj*(r-u)+(r-u)**2;upper=HH*(r+1)/DD
    ell=HH*(r+1)-DD*t if kind=='upper' else DD*(t-kk*(r-1))
    pieces=[(-1,1,S.S.Zero),(1,u,lower),(u,v,curve)]
    def bulk(f):
        return simp(sum(integral(integral(f,t,L,upper),r,a,b) for a,b,L in pieces))
    raw={(p,q):bulk(ell*t**p*r**q) for p,q in mom}
    for key,value in raw.items(): zero(value-mom[key].as_expr().subs(sub))
    zero(bulk(ell**3)-I3.as_expr().subs(sub))
    V=raw[0,0];g=S.Matrix([raw[1,0],raw[0,1],0])/V
    cov=S.Matrix([[raw[2,0],raw[1,1],0],[raw[1,1],raw[0,2],0],
                  [0,0,bulk(ell**3)/12]])/V-g*g.T
    assert all(cov[:i,:i].det()>0 for i in (1,2,3))
    ell0=ell.subs(t,0);B0=integral(ell0,r,-1,1)
    Y=r-g[1];I=bulk(ell*Y**2);edge2=integral(ell0*Y**2,r,-1,1)
    T=S.Matrix([[g[0]**2,-g[0]*integral(ell0*Y,r,-1,1)/B0,0],
                [-g[0]*integral(ell0*Y,r,-1,1)/B0,edge2/B0,0],
                [0,0,integral(ell0**3,r,-1,1)/(12*B0)]])
    alpha=g[0]*B0/V;pole=S.Matrix([-1/g[0],0,0])
    verts=([(0,-1,0),(0,1,-HH),(0,1,HH)] if kind=='upper' else
           [(0,-1,-DD*kk),(0,-1,DD*kk),(0,1,0)])
    X=[S.Matrix(vv)-g for vv in verts];sm=sum(X,S.zeros(3,1))
    triangle=(sm*sm.T+sum((vv*vv.T for vv in X),S.zeros(3)))/12
    assert triangle==T
    gap=Q(3,2)*cov-alpha*T
    assert all(gap[:i,:i].det()>0 for i in (1,2,3))
    flats=[{'name':'whole marked triangle','alpha':alpha,'T':T,
            'c':sum(X,S.zeros(3,1))/3,'pole':pole,'vertices':verts}]
    # The other positive-height side: full stem for upper-zero; full return for lower-zero.
    if kind=='upper':line=lower;lo=1;hi=u;n=S.Matrix([-1,kk,0]);b=kk
    else:line=upper;lo=-1;hi=v;n=S.Matrix([1,-HH/DD,0]);b=HH/DD
    el=ell.subs(t,line);W=integral(el,r,lo,hi);Xr=S.Matrix([line-g[0],r-g[1],0])
    c=Xr.applyfunc(lambda a:integral(el*a,r,lo,hi)/W)
    TT=(Xr*Xr.T).applyfunc(lambda a:integral(el*a,r,lo,hi)/W)
    TT[2,2]=integral(el**3,r,lo,hi)/(12*W);dist=b-n.dot(g)
    flats.append({'name':'whole positive side','alpha':simp(W*dist/V),
                  'T':TT.applyfunc(simp),'c':c.applyfunc(simp),'pole':n/dist})
    area=bulk(S.S.One)
    at=S.diff(ell,t);ar=S.diff(ell,r);a0=ell.subs({t:0,r:0});height=simp(a0+at*g[0]+ar*g[1])
    for sign in (-1,1):
        Xr=S.Matrix([t-g[0],r-g[1],sign*ell/2]);n=S.Matrix([-at,-ar,2*sign])
        c=Xr.applyfunc(lambda a:bulk(a)/area)
        TT=(Xr*Xr.T).applyfunc(lambda a:bulk(a)/area)
        flats.append({'name':'whole graph '+str(sign),'alpha':simp(height*area/(2*V)),
                      'T':TT,'c':c,'pole':n/height})
    for F in flats:
        assert F['alpha']>0
        assert (F['T']*F['pole']-F['c']).applyfunc(simp)==S.zeros(3,1)
        zero(F['pole'].dot(F['c'])-1)
    # Both actual mean equalities, and one explicitly centered mixed test.
    test=t+r/3-g[0]-g[1]/3
    zero(bulk(ell*test));zero(bulk(ell*t/g[0])/V-1)
    mixed=simp(g[0]*integral(ell0*test.subs(t,0)**2,r,-1,1)/bulk(ell*test**2))
    normal=simp(alpha*g[0]**2/cov[0,0])
    vertical=simp(alpha*T[2,2]/cov[2,2]);assert vertical<=Q(5,4)
    if (xx,yy,kk,jj)==(4,1,Q(1,2),0): assert Q(45,32)<normal<Q(3,2)
    return {'kind':kind,'parameters':[xx,yy,kk,jj],'support_pieces':pieces,'upper':upper,
            'density':ell,'volume':V,'centroid':g,'Sigma':cov,'marked_T':T,
            'marked_alpha':alpha,'marked_R_y':simp(g[0]*edge2/I),'mixed_test':test,
            'mixed_R':mixed,'normal_R':normal,'vertical_R':vertical,'gap_leading_minors':[simp(gap[:i,:i].det()) for i in (1,2,3)],
            'four_maximal_flat_facets':flats,'curved_side_patches':1,
            'scope':'Actual uniform curved body, not a polytope or an equilibrium construction.'}

def boundary_algebra():
    V,J,Y,K,L,M,E,F,B=S.symbols('V J Y K L M E F B')
    A=3*V*V*(V*K-J*J)-2*J**3*E
    C=3*V*V*(V*M-Y*Y)-2*J*(V*V*B-2*V*Y*F+Y*Y*E)
    O=3*V*V*(V*L-J*Y)+2*J*J*(V*F-Y*E)
    N=(4*(E*B-F*F)*J**4-6*E*J**3*M*V+12*E*J**2*L*V*Y
       -6*E*J*K*V*Y**2-12*F*J**2*L*V**2+12*F*J*K*V**2*Y
       +6*B*J**3*V**2-6*B*J*K*V**3-9*J**2*M*V**3
       +18*J*L*V**3*Y+9*K*M*V**4-9*K*V**3*Y**2-9*L**2*V**4)
    zero(A*C-O*O-V*V*N)
    z=S.Symbol('z');a,b,kap=S.symbols('a b kap',real=True)
    density=a*(1-z)+b*z;kernel=(1-z)*(z-kap)
    hinge=integral(z*density*kernel,z,0,1)
    root=(2*a+3*b)/(5*(a+b));zero(hinge.subs(kap,root))
    total=simp(integral(density*kernel,z,0,1).subs(kap,root))
    zero(total+(3*a*a+6*a*b+b*b)/(60*(a+b)))
    zero(total.subs(a,0)+b/60)
    w,A,B,J=S.symbols('w A B J',positive=True)
    gram=integral((w*w-z*z)*(A+B*z)**2/J,z,-w,w)
    zero(gram-4*w**3*A*A/(3*J)-4*w**5*B*B/(15*J))
    return {'hinge':hinge,'stationary_root_fraction':root,'translation_integral':total,
            'zero_marked_endpoint_translation':-b/60,'released_zero_chord_Gram':gram}

def sharpness(kind,mom,edge):
    n=S.Symbol('n',positive=True);sub={x:n,y:1,k:Q(1,2),j:0}
    V,J,K=[simp(mom[p].as_expr().subs(sub)) for p in [(0,0),(1,0),(2,0)]]
    E=simp(edge[0].as_expr().subs(sub))
    ratio=simp(J**3*E/(V**2*(V*K-J*J)))
    num,den=S.fraction(ratio)
    assert S.degree(num,n)==S.degree(den,n)
    zero(S.Poly(num,n).LC()/S.Poly(den,n).LC()-Q(3,2))
    return {'kind':kind,'parameters':['n',1,'1/2',0],'domain':'integers n>=1',
            'V':V,'normal_mean':simp(J/V),'normal_R':ratio,'normal_limit':Q(3,2)}

def encode(a):
    if isinstance(a,S.MatrixBase): return [[encode(v) for v in row] for row in a.tolist()]
    if isinstance(a,S.Basic): return str(simp(a))
    if isinstance(a,dict): return {str(k):encode(v) for k,v in a.items()}
    if isinstance(a,(tuple,list)): return [encode(v) for v in a]
    return a

def main():
    assert __debug__
    certificates=[];reports=[];controls=[];limits=[]
    for kind in ['upper','lower']:
        mom,edge=raw_polynomials(kind);cert,summary=certify(kind,mom,edge)
        I3,E3,vgap=vertical_polynomials(kind,mom)
        certificates+=cert+[coefficient_record(kind+'_vertical_five_fourths',vgap,'power (x,y,k,j)')]
        reports.append({'kind':kind,'raw_moments':{str(p):v.as_expr() for p,v in mom.items()},
                        'raw_edge_moments':[v.as_expr() for v in edge],'certificates':summary,
                        'volume_density_cube':I3.as_expr(),'edge_density_cube':E3.as_expr(),
                        'vertical_bound':Q(5,4),'vertical_positive_coefficients':len(vgap.t)})
        for values in [(1,1,Q(1,4),Q(1,2)),(4,1,Q(1,2),0),(2,1,1,Q(1,2))]:
            controls.append(actual_control(kind,values,mom,I3))
        limits.append(sharpness(kind,mom,edge))
    coeff=(json.dumps(certificates,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('one_arc_zero_edge_coefficients.json').write_bytes(coeff)
    assert sum(len(c['terms']) for c in certificates)==100367
    report={'theorem':'INCIDENT_ZERO_EDGE_ONE_ARC_SHARP_THREE_HALVES_V1',
            'parent':'[internal-source-reference]-',
            'parent_sha256':'91b7c0b0ce11005bce9c62a5726cb7dcfb0877ca85d118a852e3e0234a3e6e71',
            'actual_density_test_gate_source_sha256':'db02c3d623c7ce39099ac610255dc9b962bdaa747b931cd43bd7c8a3db8117ae',
            'coefficient_byte_count':len(coeff),'coefficient_sha256':hashlib.sha256(coeff).hexdigest(),
            'families':reports,'boundary_algebra':boundary_algebra(),'actual_controls':controls,
            'sharpness_sequences':limits,
            'scope':'Full actual one-arc incident-zero-edge value theorem; isolated marked-zero stationary exclusion; stronger same-side zero-chord gate, not its exclusion. No universal or mechanical claim.'}
    data=(json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    Path('one_arc_zero_edge_report.json').write_bytes(data)
    print('BOTH_COMPLETE_ONE_ARC_ZERO_EDGE_FAMILIES_PASS')
    print('EXACT_POSITIVE_COEFFICIENTS 100367; FULL_BASIS_RECONSTRUCTION_PASS')
    print('FULL_HORIZONTAL 3/2 AND TRANSVERSE 5/4; ALL_PARAMETERS_PASS')
    print('SIX_ACTUAL_CURVED_CONTROLS; WHOLE_MARKED_AND_24_FLAT_FACETS_PASS')
    print('BOTH_NORMAL_SHARPNESS_LIMITS 3/2; BOUNDARY_IDENTITIES_PASS')
    print('COEFFICIENTS',len(coeff),hashlib.sha256(coeff).hexdigest())
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('INCIDENT_ZERO_EDGE_ONE_ARC_EXACT_RECOVERY_PASS')
if __name__=='__main__': main()
```
