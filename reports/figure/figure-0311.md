# figure-0311

Historical AI scientific report · saved 2026-09-05 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Exact polynomial sources and a 4,355-vertex finite successor

## Determination

**The C<1000 objective is not reached.** I obtained two exactly uniform-volume-centred, strictly convex polynomial sources with precisely two equilibria, and a new fully materialized quadratic-algebraic homogeneous convex polyhedron with

`(V,E,F)=(4355,13056,8703), (S,U,H)=(1,1,0), C=26112`.

The 13,056 edges are actual true edges, not triangulation edges. This is a factor **30.8007046568** reduction in mechanical complexity from the inherited C=804268 object, but still a factor 26.112 above the present target. It is a NEW source-derived body, not a coarsening of the inherited 134131-row table. The journal's current compression objective and that parent distinction are explicit. :contentReference[oaicite:0]{index=0}

The strongest source-conditioning result is **G50**: its physical radial-normal gap obeys a certified global inequality with coefficient 1/200. An interval witness proves that the inherited epsilon1/50 source cannot have the corresponding uniform coefficient as large as 9/10000. Thus the new certified coefficient is more than 50/9 times the old source's best possible coefficient, in the precisely specified scale-invariant metric below. Both new sources have certified remote first-moment capacity nine times the inherited proved capacity. Neither statement proves an optimal source or guarantees C<1000.

The smaller finite body comes from the more balanced **P50** source. The same construction on G50 also produced a separately exactly audited 8,287-vertex body, but not a smaller one. This distinction matters: maximizing one global gradient coefficient is not sufficient to minimize the final face lattice.

## 1. A polynomial, exactly centred source family

Put `t=z^2`, `e=1/20`, and define

`K(f,g)={ (x,y,z): -1<=z<=1, (x-e*f(z^2))^2+(y-e*z*g(z^2))^2<=1-z^2 }`.

All coefficient lists below are exact rationals in ascending powers of t. This leaves the old constant-length phase trajectory: the horizontal centre follows a variable-length polynomial curve. It does not change density.

### P50 — source of the smallest finite body

```
f = [1, -241163387/28875000, 644213/125000,
     127043/6250, -106768/3125, 44096/3125]
g = [1740161/500000, -533263/125000, -1007773/31250,
     1493996/15625, -1627536/15625, 135632/3125]
```

### G50 — stronger certified physical-gap source

```
f = [1, -6452545591/734825000, 455903/125000,
     292306/3125, -2074826/3125, 41594336/15625,
     -94559008/15625, 119155584/15625,
     -77773312/15625, 821248/625]
g = [381079/100000, -114312/15625, -1826377/31250,
     8157112/15625, -41754268/15625, 131266896/15625,
     -247633536/15625, 274861824/15625,
     -165805056/15625, 41893888/15625]
```

The ordinary volume is exactly `4*pi/3`. The x first moment is

`Mx=e*pi*sum_k 4*f_k/((2*k+1)*(2*k+3))=0`.

The displayed rational lists satisfy this identity literally. The y and z moments vanish by `(x,y,z)->(x,-y,-z)`. These are therefore own-centred uniform-volume sources, not bodies balanced at a freely selected point. In this family centring is one linear coefficient equation; the odd horizontal component g does not consume moment capacity.

### A sufficient theorem with explicit polynomial certificates

Primes in this paragraph mean d/dt. Set

```
H=f^2+t*g^2
J=(1-t)*H
A=2*f'+4*t*f''
B=6*g'+4*t*g''
Kc=(1-t)^3*(A^2+t*B^2)
L=-J'-r0
```

It suffices that `H>0`, `L>0`, `L^2-e^2*J*(H')^2>0` and `e^2*Kc<k^2<1`. Both sources satisfy the stronger `1/2<H<25`, with

```
         r0       k       m        critical half-Hessian lower bound
P50      12/25    21/25   3/10     7/500
G50      1/6      9/10    9/25     9/1000
```

Here m certifies `sqrt(1-z^2)*|c'(z)|<m`, where `c=e*(f(z^2),z*g(z^2))`; k certifies `(1-z^2)^(3/2)*|c''(z)|<k`.

**Convexity proof.** Each horizontal directional support is `sqrt(1-z^2)+u dot c(z)`. Its second derivative is at most `-(1-k)/(1-z^2)^(3/2)`. Concavity of every such support proves convexity of the whole body. The original polynomial sources are smooth and strictly convex, including the poles.

**Two-equilibrium proof.** Since H is positive, the two angularly stationary squared-radius profiles are

`Gplus(t)=1+e^2*H+2*e*sqrt(J)`,
`Gminus(t)=1+e^2*H-2*e*sqrt(J)`.

The certified L inequalities imply `-J'>e*sqrt(J)*|H'|`; hence Gplus is strictly decreasing and Gminus strictly increasing for `0<t<1`. The only equilibria are

`S=(-19/20,0,0)`, `U=(21/20,0,0)`.

At a pole the normal is vertical but c(1) is nonzero, so a pole is not an equilibrium. The exact radial range is `[19/20,21/20]`.

Critical nondegeneracy is independently algebraic. Write `f1=f[1]`, `g0=g[0]`. In physical yz graph coordinates the half-Hessian at S, and the negative half-Hessian at U, are respectively

```
MS=[[e, e*(1-e)*g0],
    [e*(1-e)*g0, e-2*e*(1-e)*f1-e^2*(1-e)*g0^2]]
MU=[[e,-e*(1+e)*g0],
    [-e*(1+e)*g0,e-2*e*(1+e)*f1+e^2*(1+e)*g0^2]]
```

Subtracting the stated lower bound times the identity gives strictly positive leading entry and determinant in both matrices, using exact fractions.

The principal curvatures have the conservative bounds

`(1-k)/(1+m)^3 <= curvature <= (1+k)/(1-m)^3`.

Thus P50 has bounds `[160/2197,1840/343]`, and G50 has bounds `[3125/78608,59375/8192]`. To derive these, parameterize `X=u+(c(u_z),0)` on the unit sphere. The first fundamental form is between `(1-m)^2 I` and `(1+m)^2 I`; the second form is `( |v|^2-u_h dot c'' * v_z^2 )/|N|`, with `1-m<=|N|<=1+m`. No sampled-curvature minimum is used as proof.

### Exact Bernstein reconstruction of the source certificates

A leaf `(d,i)` denotes `[i/2^d,(i+1)/2^d]`. These complete leaf partitions certify positive Bernstein coefficients for the named polynomials:

```
P50:
 H-1/2:       (1,0),(1,1)
 25-H:        (0,0)
 L:           (3,0),(3,1),(2,1),(2,2),(2,3)
 L^2-e^2*J*H'^2: (2,0),(2,1),(2,2),(2,3)
 k^2-e^2*Kc:  (3,0),(3,1),(2,1),(1,1)
 m^2-e^2*(1-t)*[4*t*f'^2+(g+2*t*g')^2]:
              (1,0),(2,2),(3,6),(4,14),(4,15)

G50:
 H-1/2,25-H:  (1,0),(1,1)
 L, L^2-e^2*J*H'^2: (1,0),(2,2),(2,3)
 k^2-e^2*Kc:  (2,0),(2,1),(2,2),(3,6),(4,14),(4,15)
 m^2-e^2*(1-t)*[4*t*f'^2+(g+2*t*g')^2]:
              (1,0),(2,2),(3,6),(4,14),(5,30),(6,62),(6,63)
```

These certificates reconstruct directly from the coefficient lists. For `p(t)=sum p_k*t^k` on `[a,b]`, compute `q_j=(b-a)^j*sum_{k>=j} p_k*binom(k,j)*a^(k-j)`, then Bernstein coefficient `beta_i=sum_{j<=i} q_j*binom(i,j)/binom(n,j)`. Every coefficient on every listed leaf is strictly positive. Tensor certificates below apply this conversion in each variable. All calculations were independently replayed with Python Fraction arithmetic, without numerical quadrature, optimization or a CAS. The bundled standard-library scripts terminate `EXACT_POLYNOMIAL_SOURCE_AND_ACTUATOR_PASS` and `EXACT_METRIC_BOUNDS_PASS`.

## 2. A scale-invariant physical radial-gradient margin

Define on the actual physical surface

`rho(X)=sqrt(X_y^2+X_z^2)`,
`N=(p_x,p_y,z-c'(z) dot p)`, where `p=(x,y)-c(z)`,
`delta(X)=|X cross N|/|N|`.

The completed directed certificates establish

`P50: delta(X)>=rho(X)/500`,
`G50: delta(X)>=rho(X)/200`.

Equivalently, `sin(angle(X,N))>=gamma*sin(angle(X,e_x))`. This is not an untwisted-coordinate gradient, and it is unchanged under uniform scaling.

For the inherited phase source, take exactly `z=53/200`, relative phase `psi=39/1000`, and the journal's epsilon1/50 and `P=eta-(41/100)*sin(2*eta)-(9/200)*sin(4*eta)`. Outward interval evaluation gives the physical ratio in

```
[0.000888688595583033943461558075315699779214738874787753041431074683726871568086,
 0.000888688595583033943461558075315699779214738874787753041431074683727429031799]
```

It is strictly below 9/10000. This is an upper witness for the OLD uniform coefficient, not a claimed computation of its global minimum. Combined with the NEW global certificate it proves the more-than-50/9 improvement for G50. The inherited source formula and its different sufficient curvature estimate are recorded in the journal. :contentReference[oaicite:1]{index=1}

### Self-contained physical-gap certificate recipe

Use eight rational blow-up charts, with `a,w in[0,1]`, `sigma,tau in{+1,-1}`. For kind0 put `u=a,v=tau*a*w`; for kind1 put `u=a*w,v=tau*a`. In both cases

`z=2*u/(1+u^2)`, `r=(1-u^2)/(1+u^2)`,
`p_x=sigma*r*(1-v^2)/(1+v^2)`, `p_y=sigma*r*2*v/(1+v^2)`.

Set `Z=z/a`, `Y=p_y/a` using the removable-limit formulas

```
kind0: Z=2/(1+a^2), Y=sigma*r*2*tau*w/(1+a^2*w^2)
kind1: Z=2*w/(1+a^2*w^2), Y=sigma*r*2*tau/(1+a^2)
```

Evaluate f,g and their t-derivatives at `t=(a*Z)^2`. Define

```
Dbar=2*Z*f'*p_x+(g+2*t*g')*Y
Bbar=f*Y-Z*g*p_x
Cx=e*a*(Z^2*g-(Y+e*Z*g)*Dbar)
Cy=e*(-f*Z+(p_x+e*f)*Dbar)
Cz=e*Bbar
N2=p_x^2+a^2*Y^2+a^2*(Z-e*Dbar)^2
Qgap=Cx^2+Cy^2+Cz^2-gamma^2*N2*((Y+e*Z*g)^2+Z^2)
```

Qgap is exactly the desired inequality divided by a^2; no division by a is evaluated numerically. The charts cover the upper hemisphere, and C2 covers the lower hemisphere. Positive limits at a=0 certify the critical neighborhoods rather than omitting them.

The successful accelerator is important for continuation. Convert `f(z^2)`, `g(z^2)`, `f'(z^2)`, `g'(z^2)` to exact Chebyshev coefficients using

`z^n=sum_{j<=n/2} binom(n,j)*(1 if n=2*j else 2)/2^n * T_(n-2*j)(z)`.

For each polynomial's z derivative, build exact Bernstein coefficients on [-1,2], then subdivide ten times at midpoints, giving 1,024 rational derivative-range cells. Convert minima and maxima outward to binary64. A queried interval uses every intersecting cell, with one additional cell on either side; outside [-1,2], use the ordinary interval Clenshaw fallback.

Evaluate polynomial values by midpoint Clenshaw plus interval displacement times this certified derivative range. Propagate first-order interval derivatives through Qgap. On a box use the larger lower bound from natural interval evaluation and `Qgap(mid)+Q_a(box)*(a-mid_a)+Q_w(box)*(w-mid_w)`. Bisect the coordinate maximizing width times maximum absolute derivative. Every elementary arithmetic endpoint is rounded outward with nextafter; rational constants are enclosed by exact Fraction comparisons. Accept a leaf only when its lower bound is positive. This algorithm and the displayed formulas reconstruct the certificate without stored leaf files.

For G50 at gamma1/200, the eight leaf counts, ordered by kind, sigma=+,- and tau=+,-, are

`377,740,582,1824,1951,3429,1597,5323`.

There are 15,823 leaves, 31,638 processed nodes, and minimum directed Qgap lower bound greater than 1.77e-8. A separate portable replay produced the same leaf counts and bound. P50's earlier gamma1/500 certificate has 19,815 leaves and minimum directed bound greater than 1.53e-10. Stored partitions supplement these reconstruction rules.

## 3. Exact physical moment capacity, not a moved mechanical centre

Use the even bump

```
b(z)=0                                  for |z|<=1/4
b(z)=(4096/81)*(|z|-1/4)^2*(1-|z|)^2     otherwise
c_lambda(z)=c(z)-lambda*b(z)*e_x
```

It is C1 and piecewise polynomial. For BOTH P50 and G50, every `|lambda|<=3/1000` preserves strict convexity and exactly the same two origin-relative equilibria, while

`Mx(lambda)=-(33*pi/70)*lambda`, `My=Mz=0`, `volume=4*pi/3`.

The exact first-moment capacity is `99*pi/70000≈0.00444310961008`, nine times the inherited proved `33*pi/210000` capacity. The inherited actuator bound was 1/3000. :contentReference[oaicite:2]{index=2} A nonzero-lambda source is NOT itself centred; this is physical shape freedom reserved for finite approximation error.

To reconstruct the exact certificate on `z in[1/4,1]`, `lambda in[-3/1000,3/1000]`, put

```
x=e*f(z^2)-lambda*b(z); y=e*z*g(z^2)
Hlambda=x^2+y^2; Jlambda=(1-z^2)*Hlambda
Alambda=-dJlambda/dz
Qlambda=Alambda^2-Jlambda*(dHlambda/dz)^2
```

Tensor Bernstein coefficients are positive for `Hlambda-1/1000`, `Alambda-1/10000`, `Qlambda`, and `k_lambda^2-(1-z^2)^3*((x'')^2+(y'')^2)`. Use k_lambda9/10 for P50 and49/50 for G50. Normalize `z=1/4+3*u/4`, `lambda=-3/1000+6*v/1000`. No subdivision of v is required. P50 uses the whole u interval for H and its two halves for the other three tests. G50 uses two halves for H and Q; `(1,0),(2,2),(2,3)` for A; `(1,0),(2,2),(3,6),(3,7)` for curvature. These cover the full rectangle. The bump is zero in the critical slab; C2 covers negative z. This proves the safety interval rather than extrapolating it from a mesh experiment.

## 4. Smallest materialized exact polyhedron: P50-4355

The exact body is

`v_i(t)=((Ix_i-t*B_i)/D,Iy_i/D,Iz_i/D)`,
`D=100000000000000`, `T=4294967296`, `lambda=t*T/D`.

The primitive quadratic, in ascending coefficients c,b,a, is

```
c=-2458895097909393604003230247672682541272295059410392561
b=-76845903111534169678343144953904459705739084116550128
a=16469301691355479439928224189459141276130854166
```

Let `q=10^80` and

```
L=-3199751888387241117934369281474033122766034549675022136465278011175366054576978798
```

The selected root is the unique root in `[L/q,(L+1)/q]`; both the sign change and derivative sign are checked exactly. Its approximations are

`t=-31.99751888387241117934369281474033122766034549675022...`,
`lambda=-0.001374282971593744278519459514...`.

This lies strictly inside the proved actuator interval. The exact x first-moment numerator is `2*(c+b*t+a*t^2)` over `24*D^4`; both y and z numerator polynomials vanish identically. The exact volume is

```
(24899738563928013634860482018312708648031522
 -3960199531264700532090575492453660212*t)/(6*D^3)
```

and is approximately 4.149977546747883.

There are 4,355 actual extreme vertices, 8,706 oriented triangles, 13,059 triangulated edges, exactly three coplanar internal diagonals, 8,703 maximal faces and 13,056 true edges. The sole stable face is a genuine hexagon in `x=-473/500`; its canonical boundary cycle is `[0,3,4,5,2,1]`. Integer coordinates in that cycle order are

```
(-94600000000000,-8935323161475,0)
(-94600000000000,0,18961185142924)
(-94600000000000,8696776475800,15063258718155)
(-94600000000000,8935323161475,0)
(-94600000000000,0,-18961185142924)
(-94600000000000,-8696776475800,-15063258718155)
```

All six bump weights are zero. The unique unstable vertex is 4354, exactly `(527/500,0,0)`, with 12 true neighbors. There are no saddle edges or degenerate equilibria.

### Exact replay and positive margins

The verifier recomputed the moments rather than trusting root.json. It checked a connected oriented closed two-manifold, single-cycle links at every vertex, Euler characteristic2, 8,706 positive radial determinants, exact convexity of every hinge, and radial degree1 using ray(5,7,19), with no boundary hit. Positive local orientation and degree1 establish the complete nonoverlapping radial fan; convex hinges then make its piecewise-linear gauge convex. This is the actual global convex boundary, not a Qhull assertion. Exact coplanar merging yields single boundary cycles, and every vertex has three linearly independent incident supporting normals.

For each true oriented edge i->j with incident outward normal N, use the face-side predicate `N dot(v_i cross v_j)`. For its two incident faces use values u,v with opposite edge orientations. Put `p=v_i dot(v_j-v_i)`, `r=v_j dot(v_i-v_j)`. A face is stable precisely when all boundary side predicates are positive; a vertex is unstable precisely when every outgoing p is negative; an edge is a saddle precisely when `p<0,r<0,u>0,v>0`. Weak versions detect degeneracies. This explicitly tests both line-foot and both full normal-cone conditions; absence of saddles is not inferred from Euler's equilibrium identity.

All these polynomials have degree at most2 in t. For `p0+p1*t+p2*t^2`, multiply by a>0 and reduce to `(a*p0-c*p2)+(a*p1-b*p2)*t`; its signs at the rational isolating endpoints agree strictly. Exactly zero is detected algebraically, not by tolerance.

Additional exact normalized lower bounds are: radial determinants >10^-7; nonzero hinge determinants in absolute value >10^-12; every directed vertex predicate in absolute value >10^-9; every true-edge face-side predicate in absolute value >10^-13. Normalizations are D^3,D^3,D^2,D^4 respectively. The only zero hinge determinants are the three cap diagonals. These are raw polynomial margins, not manufacturing tolerances.

A conservative explicit open neighborhood is available: perturb every coordinate by at most10^-60, keep the six cap points in their common x=-473/500 plane, and evaluate at the perturbed body's own volume centroid. The source coordinates have absolute value<2 and volume>4. Selected rank-three normal determinants, normalized byD^6, are all greater than10^-40; so are the other nonzero primitives. On the coordinate box of radius3, their degree<=6 expansions have at most4096 signed monomials, giving the deliberately loose Lipschitz bound10^8. The8,706 tetrahedra bound volume change by3*10^5*delta and each first-moment change by10^6*delta; the recentered-coordinate change is therefore <2*10^6*delta. Every relevant primitive changes by <2*10^14*delta<10^-40. Convexity, extremality and the full class persist. This establishes openness only, not printability.

### Exact-data and reconstruction authority

Raw little-endian signed-int64 array SHA256 values are

```
I f22b39fafe89a04654f9924aa0f8c223cc0d53ca83d5f4b0ccb9ad1112b2a875
B 14393621a6079da523eb0f6854065ef6bae23650c7a5146514cee4578b0dbba4
F 29bef6ca53dcb3cc1cab5ac1b081c25559f0ed0a83ec7a688c3de6405ec7420e
```

The complete reconstruction program below regenerates the initial7,575-point source mesh, applies a literal1,610-orbit deletion mask and produces these exact arrays. It was successfully replayed from scratch, including after fresh archive extraction. Its numerical proposal environment was Python3.13.5, NumPy2.3.5, SciPy1.17.0, x86_64 Linux/glibc2.41, OPENBLAS_NUM_THREADS=1. Different numerical-library rounding must not be silently identified with this exact body: the hashes are fail-closed, and supplied literal integer tables are final authority. The numerical hull is only a proposal subsequently checked by the exact verifier.

The finite verifier is the inherited independent implementation recovered from POLYHEDRAL_GOMBOC_VERIFICATION.zip, with only its parent-specific `coplanar_count==253` assertion relaxed. I did not write that implementation independently in this assignment. It independently consumes the NEW data, imports no construction code, and returned `INDEPENDENT_EXACT_AUDIT_PASS` in a fresh directory. OBJ and ASCII STL were materialized;17-digit decimal readback reproduces the same display vertex/triangle arrays. Display meshes are not the exact definition.

## 5. The stronger source also has a finite bridge

The same source-mesh program with G50 coefficients, cap root-search bracket[0,1/2], `N=500,capn=12,delta=.012,iters=35,maxV=15000`, and no deletion mask produces the separate exactly audited body

`(V,E,F)=(8287,24850,16565), C=49700, (S,U,H)=(1,1,0)`.

It has16,570 triangles, five coplanar internal diagonals and one stable octagon. Quantize with the same D,T. For the proposal hull use `float.fromhex('-0x1.a65b3edc31ffep-12')`; orient returned triangles outward. No exact hinge repair was needed. Its quadratic is

```
c=-716836155288994607736718472150773619094358144329796061
b=-76436441629926912597018955478987565949674683248783686
a=2011847943307464238468966198438790440498364087
L=-937819661747777066333090315240328835207989716550205757743480633923114365626422426
q=10^80, interval=[L/q,(L+1)/q]
```

Here lambda≈-0.00040279047767524847. Raw array hashes are

```
I 90ee5ee542ea721d974e31c0de9983463844afc9f55f77b4fa564e3eeaae053e
B 35e6636165e2f7423748fa34ee070b5f430bec6b239753f5baf6f3b7b1524c30
F 59cfc2e078252b66f98c88524492c785ebd0faa3441b9e9f875ca0a8c2978de9
```

Its independent exact audit passes the same full gate. This auxiliary result prevents presenting the better source gap as an already demonstrated finite-complexity improvement over P50.

## 6. Search evidence, limitations and next construction gate

I optimized variable-length polynomial centre curves, first for amplitude/convexity, then for radial-normal gap and critical conditioning. A zero-critical-shear restriction and amplitude-only objectives were not competitive. A seemingly excellent untwisted-coordinate gap produced a weak physical critical direction and a larger mesh; a coarse azimuth grid also missed narrow minima. I replaced those objectives by the physical ratio above and added a critical-Hessian constraint. Polynomial promotion, exact centring, Bernstein positivity and all-sphere interval proofs followed optimization. No numerical optimum is claimed global.

Finite search used whole strict ascent paths, not isolated support-point additions, followed by stable-face refinement. This produced the exactly audited7,575-vertex P50 body. Symmetry-paired deletion, always recomputing the actual volume-moment root, reduced it first to6,423 and then4,355 vertices. The final local search attempted30,000 deletions; its last stage accepted1,034 paired deletions. The final figure was re-promoted and completely exactly audited. Deletion search is not the certificate, and failure to delete further is not a lower bound.

The next source-to-mesh interface is explicit. At requested squared radius R2,

`cos(psi)=(R2-1-e^2*H(t))/(2*e*sqrt(J(t)))`,
`phi=atan2(z*g(t),f(t)) +/- acos(cos(psi))`,
`X=(c_x+sqrt(1-z^2)*cos(phi),c_y+sqrt(1-z^2)*sin(phi),z)`.

Endpoints in z solve `(R2-1-e^2*H)^2=4*e^2*J`. These are the new sources' radial-height level curves; the old constant-amplitude linear norm identity must NOT be reused unchanged. For direct ascent on the unit-sphere parameter u, put `Y=X+(X_h dot c'(z))*e_z`, `w=Y-(Y dot u)*u`. Then `d|X|^2/dtau=2*|w|^2>0` along `du/dtau=w` away from the critical points.

A quantitative full-normal-cone transfer test is available. If an entire finite exposed feature lies within eta of source point X0, and all incident unit normals lie within nu<sqrt(2) of source unit normal n0, every unit vector in their positive cone lies in that same spherical cap. An equilibrium there would force

`delta(X0)<=eta+(|X0|+eta)*nu`.

Consequently `eta+(21/20+eta)*nu<gamma*rho0` excludes every feature whose source anchor has rho>=rho0, including mixed edges and vertices. For example, G50 on rho>=1/10 admits the sufficient budget eta<=1/10000 and nu<=1/3000. This is a conditional separator budget, not a proved number of cells. Finite moment actuation must be included in these errors, or checked directly as here; the unactuated gamma certificate cannot simply be assigned to nonzero lambda.

A separate endpoint diagnostic is encouraging but limited. An m-edge strict radial-ascent path spanning angle pi with endpoint ratio R must satisfy `R*cos(pi/m)^m>1`. The first possible m is124 for the old source ratio51/49 and50 for the new ratio21/19. This quantifies radial headroom, not a polyhedral complexity theorem or a proof that three50-step strips close consistently.

**The remaining gate is an actual moment-closed, Morse-aligned finite complex with E<500.** A simplicial body then permits at most168 vertices. It must close both critical collars and every transverse mixed cone while keeping the scalar moment root inside the proved actuator interval. The4,355-vertex construction proves that the source and physical moment capacity work together in a finite exact body; it does not solve that much smaller incidence-design problem. The most useful continuation is to feed P50 and G50, their explicit radial levels and certified physical-gap budgets into the lead's Morse-aligned mesher, comparing G50's weaker critical Hessian against its stronger noncritical gap rather than optimizing either alone.

## 7. Supplemental artifacts

[Complete exact tables, source certificates, reconstruction program, independent replay, true-edge/maximal-face lists and display meshes](sandbox:/mnt/data/POLYNOMIAL_SOURCE_GOMBOC_HANDOFF.zip).

[Complete handoff as Markdown](sandbox:/mnt/data/POLYNOMIAL_SOURCE_HANDOFF.md).

Archive:1,613,638 bytes; SHA256 `5d4e3a2b942e9c906f0bbc50df4e87aad4248ec998f3d54a26925a823a697a8e`. All55 internal manifest entries passed after fresh extraction, followed by successful exact finite replay and full integer-table reconstruction.

These files supplement the formulas, certificate partitions, exact roots and reconstruction below. No minimality, C<1000 success, manufacturing tolerance, outside peer review or formal proof-assistant certification is claimed.

## Appendix — complete primary-body integer-table reconstruction

Run with the environment and thread setting above. All final array hashes must match. The numerical proposal phase is fully specified here; the accepted figure is the exact integer/quadratic body in section4.

```python
import numpy as np,json,time
from scipy.spatial import ConvexHull,cKDTree
from scipy.optimize import brentq
from fractions import Fraction
from numpy.polynomial import polynomial as P
f=np.array([float(Fraction(q)) for q in ['1', '-241163387/28875000', '644213/125000', '127043/6250', '-106768/3125', '44096/3125']]);g=np.array([float(Fraction(q)) for q in ['1740161/500000', '-533263/125000', '-1007773/31250', '1493996/15625', '-1627536/15625', '135632/3125']]);eps=.05
f1=P.polyder(f);f2=P.polyder(f,2);g1=P.polyder(g);g2=P.polyder(g,2)
def center(z,der=0):
 t=z*z
 if der==0:return np.stack([eps*P.polyval(t,f),eps*z*P.polyval(t,g)],axis=-1)
 if der==1:return np.stack([eps*2*z*P.polyval(t,f1),eps*(P.polyval(t,g)+2*t*P.polyval(t,g1))],axis=-1)
 if der==2:return np.stack([eps*(2*P.polyval(t,f1)+4*t*P.polyval(t,f2)),eps*z*(6*P.polyval(t,g1)+4*t*P.polyval(t,g2))],axis=-1)
def bump(z,der=0):
 u=np.maximum((abs(z)-.25)/.75,0)
 if der==0:return 16*u*u*(1-u)**2
 if der==1:return (128/3)*u*(1-u)*(1-2*u)*np.sign(z)
 if der==2:return np.where(abs(z)>.25,(512/9)*(1-6*u+6*u*u),0)
def support(d,lam=0.):
 d=np.atleast_2d(d);h=np.linalg.norm(d[:,:2],axis=1);z=np.clip(d[:,2]/np.linalg.norm(d,axis=1),-.999999,.999999);lo=np.full(len(z),-1.);hi=np.full(len(z),1.)
 for _ in range(35):
  r=np.sqrt(1-z*z);cp=center(z,1);cp[:,0]-=lam*bump(z,1);cpp=center(z,2);cpp[:,0]-=lam*bump(z,2)
  val=d[:,2]-h*z/r+np.sum(d[:,:2]*cp,axis=1)
  sec=-h/r**3+np.sum(d[:,:2]*cpp,axis=1)
  lo=np.where(val>0,z,lo);hi=np.where(val<0,z,hi)
  new=z-val/sec
  z=np.where((new>lo)&(new<hi),new,(lo+hi)/2)
 c=center(z);c[:,0]-=lam*bump(z);r=np.sqrt(1-z*z)
 return np.c_[c+r[:,None]*d[:,:2]/h[:,None],z]
def oriented_hull(V):
 h=ConvexHull(V);F=h.simplices.copy();N=np.cross(V[F[:,1]]-V[F[:,0]],V[F[:,2]]-V[F[:,0]])
 bad=np.sum(N*h.equations[:,:3],axis=1)<0;F[bad,1],F[bad,2]=F[bad,2].copy(),F[bad,1].copy()
 return h,F

def moment_root(V,F):
 B=bump(V[:,2]);a,b,c=V[F[:,0]],V[F[:,1]],V[F[:,2]];ba,bb,bc=B[F[:,0]],B[F[:,1]],B[F[:,2]]
 det0=np.sum(a*np.cross(b,c),axis=1)
 det1=ba*(b[:,1]*c[:,2]-b[:,2]*c[:,1])+bb*(c[:,1]*a[:,2]-c[:,2]*a[:,1])+bc*(a[:,1]*b[:,2]-a[:,2]*b[:,1])
 T=(a+b+c)[:,0];Bs=ba+bb+bc
 co=np.array([np.sum(det0*T),-np.sum(det1*T+det0*Bs),np.sum(det1*Bs)])
 root= -co[0]/co[1]
 for _ in range(5):root-=np.polynomial.polynomial.polyval(root,co)/(co[1]+2*root*co[2])
 return root

def audit(V,centred=True,detail=False):
 hull,F=oriented_hull(V)
 a,b,c=V[F[:,0]],V[F[:,1]],V[F[:,2]];det=np.einsum('ij,ij->i',a,np.cross(b,c));vol=det.sum()/6
 centroid=np.sum(det[:,None]*(a+b+c),axis=0)/(24*vol)
 X=V-centroid if centred else V
 A,B,C=X[F[:,0]],X[F[:,1]],X[F[:,2]]
 normal=np.cross(B-A,C-A);nn=np.linalg.norm(normal,axis=1);N=normal/nn[:,None]
 sides=np.stack([np.einsum('ij,ij->i',N,np.cross(A,B))/np.linalg.norm(B-A,axis=1),np.einsum('ij,ij->i',N,np.cross(B,C))/np.linalg.norm(C-B,axis=1),np.einsum('ij,ij->i',N,np.cross(C,A))/np.linalg.norm(A-C,axis=1)],axis=1)
 stable=sides.min(axis=1)>1e-10
 cap=(np.ptp(V[F,0],axis=1)<1e-12)&(N[:,0]<-.999999999)
 stable[cap]=False
 edges=np.concatenate([F[:,[0,1]],F[:,[1,2]],F[:,[2,0]]]);fi=np.tile(np.arange(len(F)),3)
 perm=np.lexsort((np.max(edges,axis=1),np.min(edges,axis=1)));edges=edges[perm];fi=fi[perm];aidx=edges[::2,0];bidx=edges[::2,1];f0=fi[::2];f1=fi[1::2]
 assert np.all(np.sort(edges[::2],axis=1)==np.sort(edges[1::2],axis=1))
 diff=X[bidx]-X[aidx];dotA=np.einsum('ij,ij->i',X[aidx],diff);dotB=-np.einsum('ij,ij->i',X[bidx],diff)
 maxdot=np.full(len(V),-np.inf);np.maximum.at(maxdot,aidx,dotA);np.maximum.at(maxdot,bidx,dotB)
 U=hull.vertices[maxdot[hull.vertices]<-1e-12]
 n0=N[f0];n1=N[f1];ncross=np.cross(n0,n1);gram=np.einsum('ij,ij->i',ncross,ncross)
 true=gram>1e-20
 t=-dotA/np.einsum('ij,ij->i',diff,diff);p=X[aidx]+t[:,None]*diff
 be0=np.einsum('ij,ij->i',np.cross(p,n1),ncross);be1=np.einsum('ij,ij->i',np.cross(n0,p),ncross)
 saddle=true&(t>1e-10)&(t<1-1e-10)&(be0>1e-13*gram)&(be1>1e-13*gram)
 out={'V':len(hull.vertices),'E':int(true.sum()),'F':int(len(F)-np.count_nonzero(~true)),'S':int(stable.sum()+np.any(cap)),'U':len(U),'H':int(saddle.sum()),'volume':vol,'centroid':centroid,'Sidx':np.flatnonzero(stable),'Uidx':U,'Ftri':F,'normals':N,'maxdot':maxdot,'edges':np.stack([aidx,bidx],axis=1),'saddle':np.flatnonzero(saddle),'active':hull.vertices}
 if detail:return out
 return {k:out[k] for k in ['V','E','F','S','U','H','centroid','volume']}

def cap_points(xcut,m):
 pts=[]
 for j in range(m//2):
  th=2*np.pi*j/m
  def eq(rho):
   y=rho*np.cos(th);z=rho*np.sin(th);c=center(np.array(z));return (xcut-c[0])**2+(y-c[1])**2+z*z-1
  rho=brentq(eq,0,.2,xtol=1e-15);pts.extend([[xcut,rho*np.cos(th),rho*np.sin(th)],[xcut,-rho*np.cos(th),-rho*np.sin(th)]])
 return np.array(pts)
def seed(N=1000,capn=24,delta=.001):
 z=(np.arange(N//2)+.5)/(N//2);theta=np.arange(N//2)*(np.pi*(3-np.sqrt(5)));r=np.sqrt(1-z*z);c=center(z)
 V=np.c_[c[:,0]+r*np.cos(theta),c[:,1]+r*np.sin(theta),z]
 V=np.vstack([V,V*np.array([1,-1,-1])]);xcut=eps-1+delta
 V=V[V[:,0]>xcut+1e-12]
 return np.vstack([cap_points(xcut,capn),V,[[1+eps+delta,0,0]]])

def build(N=1000,capn=24,delta=.001,iters=80,maxV=50000):
 start=time.time();V=seed(N,capn,delta);apex=np.array([1+eps+delta,0,0]);xcut=eps-1+delta
 for it in range(iters):
  lam=0.
  for ii in range(4):
   W=V.copy();W[:,0]-=lam*bump(W[:,2]);h,F=oriented_hull(W);newlam=moment_root(V,F)
   if abs(newlam-lam)<1e-12:break
   lam=newlam
  W=V.copy();W[:,0]-=lam*bump(W[:,2]);a=audit(W,False,True)
  print(it,len(V),'lam',lam,'counts',tuple(a[k] for k in ['V','E','F','S','U','H']),'mom',a['centroid'],'time',time.time()-start,flush=True)
  if a['S']==1 and a['U']==1 and a['H']==0:return V,lam,a
  if len(V)>maxV:break
  V=V[a['active']]
  added=[];tree=cKDTree(W[a['active']]/np.linalg.norm(W[a['active']],axis=1)[:,None]);WW=W[a['active']]
  st=a['Sidx'];dirs=a['normals'][st];starts=support(dirs,lam) if len(st) else np.empty((0,3))
  starts=np.vstack([starts,W[a['Uidx']][np.linalg.norm(W[a['Uidx']]-apex,axis=1)>1e-10]])
  starts=starts[(starts[:,2]>1e-12)|((abs(starts[:,2])<=1e-12)&(starts[:,1]>=0))]
  if len(starts)==0:break
  p=starts
  added.extend(p.copy())
  for step in range(1000):
   q=support(p,lam)
   advance=np.einsum('ij,ij->i',p,q-p)>1e-12
   q=q[advance]
   if len(q)==0:break
   added.extend(q.copy())
   q=q[(q[:,0]>xcut+1e-10)&(np.einsum('ij,ij->i',q,apex-q)<=1e-10)]
   if len(q)==0:break
   anchors=np.vstack([WW,np.array(added)])
   tree=cKDTree(anchors/np.linalg.norm(anchors,axis=1)[:,None])
   _,ids=tree.query(q/np.linalg.norm(q,axis=1)[:,None],k=min(30,len(anchors)))
   can_stop=np.max(np.einsum('nki,ni->nk',anchors[ids]-q[:,None,:],q),axis=1)>1e-10
   p=q[~can_stop]
   if len(p)==0 or len(added)>maxV:break
  if not added:break
  add=np.array(added);add[:,0]+=lam*bump(add[:,2]);add=np.vstack([add,add*np.array([1,-1,-1])]);V=np.vstack([V,add]);V=np.unique(np.round(V,14),axis=0)
 return V,lam,a

if __name__=='__main__':
 import hashlib,zlib,base64
 from pathlib import Path
 V,_,_=build(N=300,capn=12,delta=.004,iters=50,maxV=30000)
 assert len(V)==7575
 assert hashlib.sha256(V.astype('<f8').tobytes()).hexdigest()=='f03f510d8ccf0b5a32a72f1a3d39d88924c98cc2f82146f663cad8d19b80d567'
 packed='c-mc5U5gt*3~OCuj2VVu385VK(1-s2-&jd@Hldf>WY^;lS+e)Xub*k}KY!l_u524WaU1a!5nix5uAsr;>AY2f<Ux+V<1CyZ(cVgzF4v3+3%F-`xYuN=>?AN&bgH!C4Fa>ObQ%cUgy76xj668lENESB+1kX+g3F3fnRF39(ZnHK`r~K2tG_}^p=Nv=tzEnFV%M8M7t(EI#UV2=2`Xf>gmZ)@yFMkB5+5EU!59xNZ*m3RR;WiZMjk>z&bmBD?T8nlc9epj$4i)?osI~_?-PE-DlQJt78|dHT#?H*6ez#8iA`_q(HhRFEHJ_$<FZz46Rxcyy%IayUo()Ng3U~XTXWK(7jp_@4Nw7MQ^ki44OyKHB)Ovinv5P4ULqol#CR9iU`gd-)@3ajEs;{hC9AY<l}(98T1npB=rMYxya&TM<1j7VPfzB@q(k<4wD2<?J)~{93D9FS7pD~>=(<-*Si~<CZY(Vu{A(r`oS=2@zLHg(0?uqeTZTUAyM`FY2C4g;_H5w4s)^y`F(*<5aTj0_a+h`#yOA^4*uqUTNOFxZ2RnV#um<?Br!{)H&(!up<MCRJg|V2I10d&N`yw@8)hv7`IIolpd-RH(_9wX7D2p9|OAd9|EA8IOrMX&&!Sxr@jm(*alEBR+^apZ&#gnl3)@d%2O@Tb$o20~*cFo%T?pZ9;Dq!w2mU<SOn`7aRXtp;ci5)#5aAbkJo)t@k>Xjh=gR4!onv>VC&0_a7^s8k4^F9B5zk+X3?Damq-#;IrdWipw^D_5|dnKH`>H4?dXV8b`Gu3VV2hq+QlK'
 raw=zlib.decompress(base64.b85decode(packed));reps=[];last=0;value=0;shift=0
 for b in raw:
  value|=(b&127)<<shift
  if b&128:shift+=7
  else:last+=value;reps.append(last);value=shift=0
 assert len(reps)==1610 and shift==0
 D=10**14;T=2**32;initial=np.rint(V*D).astype(np.int64);lookup={tuple(v):i for i,v in enumerate(initial)}
 remove=set(reps)
 for i in reps:
  x,y,z=map(int,initial[i]);remove.add(lookup[(x,-y,-z)])
 V=V[[i for i in range(len(V)) if i not in remove]]
 assert len(V)==4355
 lam=float.fromhex('-0x1.684291ac86e85p-10');W=V.copy();W[:,0]-=lam*bump(W[:,2]);h,F=oriented_hull(W)
 assert len(h.vertices)==len(V)
 I=np.rint(V*D).astype(np.int64);B=np.rint(T*bump(V[:,2])).astype(np.int64)
 expected={'I':'f22b39fafe89a04654f9924aa0f8c223cc0d53ca83d5f4b0ccb9ad1112b2a875','B':'14393621a6079da523eb0f6854065ef6bae23650c7a5146514cee4578b0dbba4','F':'29bef6ca53dcb3cc1cab5ac1b081c25559f0ed0a83ec7a688c3de6405ec7420e'}
 for name,array in [('I',I),('B',B),('F',F)]:
  assert hashlib.sha256(array.astype('<i8').tobytes()).hexdigest()==expected[name],name
 out=Path(__file__).with_name('regenerated_exact_polyhedron.npz')
 np.savez_compressed(out,I=I,B=B,F=F,D=np.array(D,dtype=np.int64))
 print('LITERAL_INTEGER_TABLE_AND_TRIANGULATION_RECONSTRUCTION_PASS')
```
