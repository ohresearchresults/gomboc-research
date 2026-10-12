# minimum-0129

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# BALANCED_E17_PLANAR_CENTROID_AND_QUARTIC_RECIPROCAL_PENCIL_V1

## Determination

**The complete balanced domain now has a fixed-central-plane reduction and an exact low-degree elimination of two continuous variables.** For fixed cuts and horizontal projectivity, every actual uniform centroid lies in one fixed affine plane parallel to the apex edge. The signed heights of all ten vertices relative to that central plane are independent of apex separation. For every common reciprocal metric, all 68 physical edge primitives reduce to forms `A(a)+y B(a)`, with `deg A<=4` and `deg B<=2`, where `a` is apex separation and `y` is the metric Schur complement. Consequently the full problem becomes a fourteen-parameter outer family of finite univariate sign problems of degree at most six.

Two complete two-dimensional fibers of this reduction were excluded by executed exact certificates: 1,777 algebraic event roots and 26,389 open sign cells, with an independent rational Sturm completeness check. Neither fiber contains a proper own-centroid110 body, including on its event walls. These fibers are not all-SPD exclusions for their individual shapes.

**I did not prove an obstruction on the whole fourteen-parameter outer domain and did not construct an exact110.** The accepted bounds `34<=C_min<=622` and all incidence-register counts remain unchanged. The previously known linearity of the fixed-shape height pencil is background; the new content is the actual separation-variable centroid compression, persistent central plane, quartic/quadratic joint pencil, and exact two-variable elimination. The older height-only method is recorded in the supplied notebook. :contentReference[oaicite:0]{index=0}

## 1. Input authority and complete domain

I read the entire supplied 1,950-line journal, including common memory, branch memory and the complete literal parent. The mounted journal is 319,563 bytes, SHA-256 `17dacdf802796b2ac0ce1682b35b245aeea2c45d02e603da41f25ce842aef389`. The required parent is `minimum-0125`. Its literal result, serialized as the compact version-2 JSON envelope, authenticates to 30,126 bytes and SHA-256 `3e3db66e34ca7337ba6d0afc4e4cdcd2b9b4d7735f5b3c1cd75b959956def185`. No authority conflict was found. Other historical sources named in the notebook were not treated as attached executable dependencies.

Write the four independent cut pairs as `((sx,sy),(wx,wy),(nx,ny),(ex,ey))`. All eight entries are positive, and

` sx+ex<2, wx+nx<2, sy+wy<2, ny+ey<2. `

The raw vertices are

```text
P0=(-1+sx,-1,0)       P1=(-1,-1+sy,0)
P2=(-1,1-wy,0)        P3=(-1+wx,1,0)
P4=(1-nx,1,0)         P5=(1,1-ny,0)
P6=(1,-1+ey,0)        P7=(1-ex,-1,0)
P8=(-a,0,1)           P9=(a,0,1),       a>0.
```

Set `fi=1+u*Pi_x+v*Pi_y`, `Yi=Pi/fi`, requiring every `fi>0`. In particular `|u|a<1`. **The coefficients u,v are real, not individually positive.** Their positivity condition is exactly the ten denominators in the literal parent. The actual maximal facets are

```text
F0=(0,1,2,3,4,5,6,7)
F1=(0,8,1) F2=(1,8,2) F3=(2,8,3) F4=(3,8,9,4)
F5=(4,9,5) F6=(5,9,6) F7=(6,9,7) F8=(7,9,8,0).
```

Their cyclic edges give precisely 17 true edges: the base cycle, spokes `8--{0,1,2,3}`, spokes `9--{4,5,6,7}`, and `8--9`. The parent proves this entire strict geometric domain covers every balanced realization up to affine equivalence. No cut, slope, shear, root-location or metric-conditioning restriction is added to the new structural theorems. :contentReference[oaicite:1]{index=1}

## 2. Six actual planar functions determine the moving centroid

Fix the cuts,u,v with positive basal denominators. Define

```text
b = sum(j=1..6) abs(det2(Pj-P0,P(j+1)-P0))/(f0*fj*f(j+1)),
L = sum over edges 01,12,23 of abs(Pj_y-Pi_y)/(fi*fj),
R = sum over edges 45,56,67 of abs(Pj_y-Pi_y)/(fi*fj),
c = L+R.
```

Thus `b` is twice the actual area of the transformed filled base. Define `bu,bv,cu,cv` by actual differentiation in u,v while holding cuts fixed. For each summand `w` in b, its u-derivative is `-w*sum(Pi_x/fi)` over its three vertices; for each summand in c, it is `-w*(Pi_x/fi+Pj_x/fj)`. The v formulas replace x by y. These are coupled functions of one actual polygon, not six independently admissible moments.

**Theorem 1.** Throughout the complete domain,

```text
L-R = u*b,                 c>|u|*b,
k = 1-u^2*a^2,             W=b+a*c,
Vol = W/(6*k),             D=4*W*k,
Nx = -(bu+a*cu)*k-2*a^2*u*W,
Ny = -(bv+a*cv)*k,
Nz = b*(1+u^2*a^2)+2*a*c,
g = (Nx,Ny,Nz)/D.
```

Here g is the centroid of the uniformly refilled projective image.

**Proof.** The true fan from apex8 contributes `b/(1-u*a)` from the base and `2*a*R/k` from the three opposite triangular facets. The true fan from apex9 gives `b/(1+u*a)+2*a*L/k`. Equality of these actual six-volumes gives `L-R=u*b`; their common value is `(b+a*c)/k`. Both L and R are strictly positive, proving `c>|u|b`.

The exact projective Jacobian gives `partial_u log Vol=-4 gx` and `partial_v log Vol=-4 gy`. For the third coordinate, temporarily include a vertical denominator coefficient w. The parent's body identity gives `Vol(u,v,w;a)=(1+w)^(-1)*Vol(u,v,0;a/(1+w))`. Hence `gz=(1+a*partial_a log Vol)/4`. Differentiating the displayed actual volume yields all three numerator formulas. This uses true volume weighting, not a transported old centroid. The underlying actual fan transformation is the parent's `d_tau/product(fi)` identity. :contentReference[oaicite:2]{index=2}

## 3. A persistent actual central plane and fixed section incidence

Define auxiliary vectors

```text
c0=(-bu/(4*b),-bv/(4*b),1/4),
c1=(-cu/(4*c),-cv/(4*c),1/2),
d=(1,0,-u),                 lambda=b/(b+a*c).
```

**Theorem 2.** The exact centroid identity is

`g(a)=lambda*c0+(1-lambda)*c1-[a^2*u/(2*(1-u^2*a^2))]*d.`

Also

`Y8=e3-[a/(1-u*a)]d,  Y9=e3+[a/(1+u*a)]d.`

Therefore every g(a) belongs to the fixed affine space `c0+span(c1-c0,d)`, of dimension at most two. If `n=(c1-c0) cross d` is nonzero, the fixed plane `n.(X-c0)=0` contains the actual centroid for every admissible a and is parallel to the ridge. If the cross product is zero, any nonzero `n perpendicular d` defines such a plane; `n=e_y` suffices.

For this plane, **each of the ten actual centered vertex heights**

`hi=n.(Yi(a)-g(a))=n.(Yi(a)-c0)`

is independent of a. The eight base vertices are fixed; the two apices move along one fixed line parallel to the plane. This proves the statement without any metric assumption. The vectors c0,c1 are algebraic aids; in particular c1 is not being declared the centroid of an inadmissible infinite-separation body.

When no hi vanishes, the set of true edges crossing this central plane is fixed throughout the whole a-domain. On a crossing edge ij its exact interpolation parameter is the constant `tij=-hi/(hj-hi)`. Thus the actual section vertices are `(1-tij)Yi(a)+tij Yj(a)`, followed by subtraction of the true g(a). Zero-height vertices or an edge in the plane must be retained as their own fixed incidence strata.

This is useful beyond the computation below: unlike the old base-parallel central plane, it does not change its half-vertex partition when an apex crosses the actual COM height. It gives a single genuine section framework for coupling section stress and ridge/rim arguments while a varies.

## 4. Exact below-COM phase and sharp ratio restrictions

Put `t=|u|a`, `Hhi=1/(1-t)`, `Hlo=1/(1+t)`. Theorem 1 gives, on the whole domain,

`Hhi/4 < gz < (Hhi+Hlo)/4.`

For the lower inequality, after multiplying by `4Wk`, the positive difference is `(1-t)(a*c-b*t)`; for the upper inequality it is `b*k>0`. These include u=0, when `1/4<gz<1/2`.

Consequently, if `Hhi/Hlo<=3`, both apices are strictly above the actual centroid. If `Hhi/Hlo>=4`, the lower apex is strictly below it.

For u nonzero set `K=c/(|u|b)>1`. The unique crossing occurs at

```text
tstar=(K-2+sqrt((K+1)*(K+7)))/(1+4*K),
1/2<tstar<3/5,             astar=tstar/|u|.
```

Indeed the sign of `Hlo-gz` is the sign of

`3+(2K-4)t-(1+4K)t^2`,

which has exactly one positive root, is positive at 1/2 and negative at 3/5. Thus the crossing height ratio lies strictly between 3 and 4. These ratio endpoints are sharp limits within the balanced family: with all cuts 1/2 and v=0, taking u to 0 from above gives K tending to infinity; taking u to 1 from below gives K tending to 1. In the latter limit R stays bounded while b diverges and `c=u*b+2R`. The limiting degenerate bodies are not asserted to retain the E17 lattice.

This classifies an entire geometric transition. It is not a monostatic obstruction by itself.

## 5. The complete common-metric quartic/quadratic pencil

Fix arbitrary `G=G^T>0` of order two and arbitrary shear `s=(s1,s2)`. Every SPD3 metric has the unique decomposition

```text
M_y=((G,G*s),(s^T*G,s^T*G*s+y)),                 y>0,
N_y=((G^-1+s*s^T/y,-s/y),(-s^T/y,1/y))
   =N0+w*w^T/y,
N0=diag(G^-1,0),                               w=(s1,s2,-1).
```

Thus N_y is literally M_y inverse. Scaling the whole metric permits `G11=1`; it imposes no mechanical restriction. The fourteen remaining outer parameters are eight cuts, u,v, two normalized entries of G and two shear entries. The inner variables are a,y.

**Theorem 3.** Each of the 68 actual directed primal/polar primitives has exactly the sign, including zero, of

`A_e(a)+y*B_e(a),       deg A_e<=4, deg B_e<=2.`

Only strictly positive factors are removed. At least 24 B polynomials vanish identically: the sixteen directed basal primal rows and the eight outgoing base-pole rows. There are at most 44 nonconstant height thresholds.

**Primal proof and reconstruction.** Let `Wi=D*Yi-N`, where N is the centroid numerator from Theorem 1. Every coordinate of Wi is polynomial of degree at most three and its z-coordinate has degree at most two. Use these positively rescaled actual edge directions:

```text
basal ij:          e=Yj-Yi;
base i to apex sigma: e=(sigma*a,0,1)-(1+sigma*u*a)*Yi;
ridge 8 to 9:      e=d=(1,0,-u).
```

Here sigma=-1 for8 and +1 for9. The removed factors are respectively 1, `1/(1+sigma*u*a)`, and `2a/k`, all positive. Reverse rows use -e at the reverse endpoint. With `M0=M_y-y*e_z*e_z^T`, the row is

`A=Wi^T M0 e,      B=Wi_z*e_z.`

The degree bounds follow immediately. In the matrix expression, `e_z` denotes the fixed vertical unit vector; in the scalar expression for B, it denotes the z-component of the edge direction e.

**Dual proof and reconstruction.** Write the actual uncentered supporting planes as `n_f(a).Y<=h_f`. Their horizontal normal coordinates are constant and their vertical coordinate is affine in a. For a side facet incident to apex sigma the normal has the form

`n_f=(l,m,(1+sigma*u*a)*h_f-sigma*a*l).`

The full exact normal list is generated in the capsule from the displayed cut lengths and facets. Define `H_f=h_f*D-n_f.N>0`. The centered pole is `q_f=D*n_f/H_f`.

Direct substitution of Theorem 1 proves: on an apex-sigma side facet, `H_f` is divisible by `1+sigma*u*a`, with quotient degree at most two. On either quadrilateral, `H_f` is divisible by k, with quotient degree at most one. For example, a quadrilateral normal has form `(h*u,m,h)`, and

`H_f=k*[h*(3b+2ac)+h*u*(bu+a*cu)+m*(bv+a*cv)].`

For adjacent facets f,h set `E=H_f*n_h-H_h*n_f`. Divide E by the positive factor `1+sigma*u*a` on a spoke, by k on the ridge, and by1 on a basal edge. Write the resulting vector as Ebar. The dual row f to h is

```text
A=(n_f.w)*(Ebar.w),
B=n_f^T*N0*Ebar.
```

The actual primitive is this row times `D^2*factor/(y*H_f^2*H_h)>0`. Reverse rows use -Ebar. Reduced Ebar has horizontal degree at most two and vertical degree at most three. Since n_f has horizontal degree zero and vertical degree one, the claimed bounds follow. For a basal dual edge, the horizontal part of E is a constant horizontal normal times `H_0=Nz`, also degree two.

All factorizations were additionally checked as generic symbolic identities, not just at the two example fibers. The projectivity is a shape construction; only the final affine metric change uses a constant M,N, exactly as required by the parent. :contentReference[oaicite:3]{index=3}

## 6. Finite decisive inner problem, including a rigorous wall argument

For any fixed outer parameters, form the nonzero polynomials

`A_i, B_i, A_i*B_j-A_j*B_i`.

Only pairs of rows with nonzero B are needed in the last set. Their degrees are at most4,2,6. Their real roots divide the entire admissible a-domain, `(0,1/|u|)` or `(0,infinity)` when u=0. On every open resulting interval, all positive height roots `-A_i/B_i` have fixed order and all coefficient signs are fixed. One exact a representative per interval and one exact positive y representative per height interval therefore determine every open physical sign chamber. This is a complete event decomposition, not a sampled grid.

A simple universal bound is

`68*4+44*2+binom(44,2)*6=6036`

a-event roots, hence at most `6037*45=271665` open representatives at any fixed outer point. This is only a bound in a; it is not a degree bound in the fourteen outer parameters.

There is also a direct formula for any selected set of positive rows. Existence of y>0 satisfying every `A_i+yB_i>0` is equivalent to

```text
for each i:                 B_i>0 OR A_i>0;
for each B_i>0, B_j<0:      A_j*B_i-A_i*B_j>0.
```

This follows by intersecting the lower and upper bounds for y. Zero B requires positive A. Thus no numerical optimization of y is necessary. A selected seventeen-row certificate needs only degree-at-most-six univariate sign tests; the complete census implementation instead examines all 68 rows and does not assume a particular tree pair.

**Why the omitted event walls cannot hide a proper110.** A body with strict110 and no additional physical weak point has a finite collection of strict guards: negative outgoing products at its strict U/S roots, a positive outgoing escape at each other vertex/pole, and a positive member of every edge packet to exclude both H and weak contacts. These persist under small changes of a,y inside the geometric domain. Harmless zero primitives need not be made nonzero individually. Therefore any proper110 on an event wall would imply a nearby proper110 in an open chamber. Exhausting the open chambers excludes the proper target on all walls too.

This argument **does not exclude strict counts S=U=1 with additional weak resting points on every multiple wall**. Such a stronger assertion requires the wall census and is not claimed. Persistent identically zero rows must be retained; the generator handles them explicitly.

## 7. Executed exact two-dimensional exclusions

Both fibers use the complete literal cut input

`((1/5,7/10),(9/10,3/5),(4/5,1/4),(2/3,6/5))`.

These independent-slope cuts are the parent's fingerprint outside the older isosceles-cut projective orbits. That orbit separation is inherited, not newly inferred from the computations here. :contentReference[oaicite:4]{index=4}

| Fiber | Fixed outer data | Entire inner domain | Projection factors | Event roots | a cells | Open (a,y) cells |
|---|---|---|---:|---:|---:|---:|
| A | u=1/2, v=1/8; G=diag(1,1/100); shear=(0,0) | 0<a<2, y>0 | 964 | 992 | 993 | 16611 |
| B | u=0, v=1/7; G=((1,1/5),(1/5,2)); shear=(1/3,-1/5) | a>0, y>0 | 872 | 785 | 786 | 9778 |

Every examined open cell has S>=2 and U>=2, no zero primitive and no physical weak point. No target cell exists. The openness argument therefore excludes proper110 on each whole stated two-dimensional domain, including its algebraic walls. The second certificate includes the final unbounded a interval and every final unbounded y interval.

The root isolators were checked by an independently written standard-library rational Sturm implementation: 5,827 sequence members for A and 3,975 for B, with all 1,777 roots simple, globally complete in the stated domains and pairwise disjoint across factors. Polynomial factor multiplication is checked exactly. Complete rows, root polynomials, isolators, interval representatives and cell counts reconstruct from source; no missing coefficient table is needed.

For BOTH fibers, the persistent central plane has constant positive vertex set `{2,3,4,5,6}`, negative set `{0,1,7,8,9}`, and no zero-height vertex. Its true section is a heptagon throughout the whole a-domain, on precisely

`(1,2),(2,8),(3,8),(4,9),(5,9),(6,7),(6,9)`.

The generator recovers all seven exact, a-independent interpolation coefficients. One integer equation of fiber A's central plane, in uncentered projective coordinates, is

```text
-105273982229925494100*x
+700927491797662436575*y
-210547964459850988200*z
+183385786284846666456 = 0.
```

Its low-apex COM transition is the unique positive root of

`-251425973683*a^2-95667880268*a+462791805268`,

strictly between1 and6/5. The fixed central-plane partition does not change across that transition.

### Actual nonrecord controls and the genuine weak wall

Every control below was independently reconstructed by all120 supporting triples, the nine actual maximal facets, the17 true edges, two positive apex-fan volume/centroid integrations, centered poles, exact M*N=I, and all68 true-edge primitives. The signs were then compared against the compressed polynomial rows. All bodies have actual V/E/F=10/17/9. Rational M can be realized as an ordinary uniform Euclidean body by applying its positive square root after subtracting its own centroid.

| Fiber | a | y | Strict S/U/H | Physical weak points | Zero primitives |
|---|---:|---:|---|---:|---:|
| A | 1/2 | 1/10000 | 2/2/2 | 0 | 0 |
| A | 1 | 1/900 | 2/2/2 | 0 | 0 |
| A | 6/5 | 1/900 | 2/2/2 | 0 | 0 |
| A | 3/2 | 1/10000 | 2/2/2 | 0 | 0 |
| A | 3/2 | 390244572502123196551201/189220125747193145108706991 | 2/2/2 | 1 EF | 1 |
| B | 1/3 | 1/25 | 2/5/5 | 0 | 0 |
| B | 2 | 1 | 3/7/8 | 0 | 0 |
| B | 10 | 9 | 3/4/5 | 0 | 0 |

The first A control has both U in the base, `{1,6}`; the next has U `{1,9}`; the third has U `{8,9}`. The fourth is a calibration against the parent's below-COM control, up to overall metric scale, rather than a claimed new independent construction.

At the genuine EF wall the strict labels are `S={0,8}`, `U={8,9}`, `H={(0,8),(2,8)}`. The additional weak point lies in the relative interior of true edge `(3,8)`, with interpolation parameter from3 to8

`1906647547865895411002302607/5992970347828083836511256500`.

Its two actual normal-cone coefficients are nonnegative with exactly one zero. The source checks the physical vector equality `M*r=lambda_f*q_f+lambda_h*q_h`; it is not merely a zero primitive counted as a contact. Complete rational point coordinates, normal coefficients and every packet are regenerated in `pencil_controls.json`. None of these bodies is110.

## 8. Numerical attempts and their limited meaning

I also executed 100 joint S/U starts, 300 U-only starts and300 S-only starts in the full eight-cut/two-projective/metric parameterization. Each iteration recomputes actual fan centroid and covariance; the reciprocal metric is never independently fitted. Seeds were193757,193758,193759. The complete optional source, all bounds, logistic maps, initial-distribution rules, tolerances, margin0.005, maximum400 function evaluations and condition penalty used only in joint mode are included in the recovery capsule.

Best residuals were respectively `0.010386985736101702`, `0.007078329892401022`, `0.007071696282731364`, at starts25,208,206. The floating S/U labels were respectively `{3,4,6}/{6,7,9}`, `{2,4,6}/{3,4,7}`, and `{2,6}/{0,3,9}`. These are failed, finitely bounded numerical locators, not positive lower bounds, global minima, full exact weak censuses, or exclusions. All700 starts finished. A source-only cold run reproduced all three complete locator JSON files byte for byte. No numerical body is promoted to an exact successor.

## 9. The remaining decisive task

The unresolved object is the **whole fourteen-parameter outer family of the exact rows above**. No uniform sign obstruction over that domain has been certified. The two fiber exclusions demonstrate executable inner elimination, not coverage of neighboring G, shear, cuts or projectivities.

The most useful continuation is to exploit the persistent central plane: its fixed half-vertex sets and constant true-edge section interpolation coefficients give actual section stresses and ridge/rim comparisons without the previous changing base-parallel partition. They must still be evaluated with the SAME M,N and genuine centroid. This route may supply outer-domain inequalities strong enough to rule out every positive chamber of the degree-six inner feasibility problem. Conversely, any outer point with a surviving positive chamber supplies an exact route to a rational own-centroid construction and a complete physical audit. Merely repeating finite metric searches on either excluded fiber would add little.

No external theorem is needed in the new proofs or recovery. No research connector, archive, missing parent code, or journal update is required. The inherited normal-form coverage is the only parent theorem needed to identify this reduction with the whole balanced realization type.

## 10. Complete source-only recovery capsule

The literal source below reconstructs TWO complete runnable units, not isolated fragments: the exact generator/verifier and the optional numerical locator. It embeds all exact geometric inputs, normal formulas, symbolic identities, cell generation, actual hull/mass/weak-packet checks and independent rational Sturm routines. No report download or old source file is a dependency.

Save the entire following block as `recover_balanced_quartic.py`, UTF-8/LF with one final LF. Run in a fresh directory:

```sh
python -S recover_balanced_quartic.py
python balanced_quartic.py build
python balanced_quartic.py check
python -S balanced_quartic.py sturm
```

Executed exact environment: CPython3.13.5, SymPy1.14.0, assertions enabled. The recovery wrapper and `sturm` command use only the Python standard library. Both ordinary build/check and fresh-directory source recovery were executed; fresh recovery regenerated all three exact reports byte for byte, and its separate standard-library Sturm check passed.

Optional locator reproduction uses NumPy2.3.5 and SciPy1.17.0 in the same environment; BLAS/OMP threads are set to1 in the source:

```sh
python locate_full_recovery.py 193757 100 both
python locate_full_recovery.py 193758 300 U
python locate_full_recovery.py 193759 300 S
```

Exact pins:

```text
recover_balanced_quartic.py 13001 bytes
7fcf13683f4b90d836dcdff1d630703881e5aec93cfa3dd2ef8c9f1a34035ee7
Decoded two-source JSON pack 21408 bytes
f2b816f286fa8f5396b7aaed5097cdb526b27e9591a583330f0f1b829d4eaef6
balanced_quartic.py 17512 bytes
7e2648be6ea8ccbba3ac5b64ab5ca5d6e6807550859b3279d8992f3c69f2ce2d
locate_full_recovery.py 3400 bytes
8190131880beedf3803a71cb757ae3776271728b8b5977489bd271e520ee2a5c
pencil_A.json 549950 bytes
b8df1570f2ffa247b3049359d625130d9cbbfd440d6b1082f51d40746c4457db
pencil_B.json 248042 bytes
8615f0c46fb63ea24434ed29ef8c978d3416c37f90c1327186be6ed921c9c913
pencil_controls.json 78119 bytes
3200389363d9f78d6d36d6893568816d7fb1b3c042a40af5b32940c5341d1ca4
locate_193757_both.json 113665 bytes
7621f8622def655a4acf77322741284cc3979a165b4e7e44b63e5ed2f20fb992
locate_193758_U.json 340659 bytes
7a89d5bd21b341d91d9589a3607456f1ebf0736cf01adc4ca0b294898189fe65
locate_193759_S.json 340296 bytes
fa5e396afeb10cfe675ffd80dac0230adcde2c26d5d1871e41819ba05941b7ac
```

Expected terminal markers:


[Encoded source block omitted; the code in this passage is incomplete.]


The generic symbolic identity marker `GENERIC_MOMENT_PLANE_SIDE_FACTOR_AND_PHASE_IDENTITIES_PASS` is stored in the controls report.


[Encoded source block omitted; the code in this passage is incomplete.]


**Capsule transport limitation:** The compressed stream in this response is not complete and must not be used as a durable recovery source. The complete tested 13,001-byte wrapper and the readable exact source exist at the supplemental links below, but links alone do not satisfy the requested recovery contract. Accordingly, the newly computed certificate objects remain **ephemeral for a fresh executor receiving only this response**, despite the executed build/check and the hashes reported above. The analytic formulas, proofs, exact fiber inputs, domain specifications, control parameters and continuation direction in Sections1–9 remain self-contained. A continuation requiring the exact computed certificates needs the complete literal `recover_balanced_quartic.py` or both complete readable source units; their contents must not be guessed from this incomplete stream.

Supplemental copies: [complete tested recovery wrapper](sandbox:/mnt/data/recover_balanced_quartic.py), [readable exact source](sandbox:/mnt/data/balanced_quartic.py), [optional numerical locator](sandbox:/mnt/data/locate_full_recovery.py), [fiber A certificate](sandbox:/mnt/data/pencil_A.json), [fiber B certificate](sandbox:/mnt/data/pencil_B.json), and [full actual control audits](sandbox:/mnt/data/pencil_controls.json).
