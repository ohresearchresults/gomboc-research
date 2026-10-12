# minimum-0190

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# QUAD_LEAF_MAX_EAR_AND_EXTERNAL_GATE_V1

## 1. Result and scope

The remaining **internal-root quadrilateral classification is complete**. For a genuine cyclic quadrilateral

`x0=a, x1=a+e, x2=a+e+f, x3=a+u e+v f`,

there is one physical SPD metric making the facet strictly stable and realizing `0→1→2←3` weakly **if and only if `u<0` and `0<v<1`**. All three arrows can be strict. Together with B9's endpoint criterion, this gives a complete rule: **a nontrapezoidal quadrilateral can be a stable selected dual-root leaf only when its boundary path is oriented toward its unique largest-ear vertex.** Exactly four of its sixteen local rooted boundary-path patterns survive. Every trapezoid has none.

The main advance beyond root signs is an **actual external-edge saddle-forcing theorem**. A specified true outside ingress, in an explicit actual-origin cone, forces a strict saddle on the missing boundary edge. Equivalently, it forces the mandatory nonroot polar escape across that edge to be strictly negative. This uses one metric and its inverse, not independent root fans or an optional tree assumed to extend to a matching.

The theorem is certified on an entire **three-parameter positive-projective, uniformly refilled, own-centred E17 family**. On its literal lattice and with F0 the selected stable dual-root leaf, the largest-ear test closes 17,356 of 22,520 raw labelled domains; the external mechanism closes another **740 disjoint domains**, leaving **4,424**. These are shape-sector/raw-labelled counts, not new canonical orbits or a subtraction from a global registry. Overlap with older universal primal exclusions has not been mapped.

A strict local independent-feasibility witness uses **four genuine primal arrows, the full four-arrow root fan, and one nonroot dual escape**. Both local SPD cones are strictly nonempty. The same independent pair has

`rho = 39410303281/108096690578 < 1/2`,

and thus remains inside the mutual cofactor blind cone, although no reciprocal pair realizes those signs. Its primal metric has actual-covariance condition number **less than 7**. This is not a separately feasible complete U1/S1 system.

**No whole E17 type, entire S1/U1 realization family, C34 attainer, or global lower bound is newly established. The accepted interval remains 34 ≤ C_min ≤ 622.** The parent expressly separates local feasibility from its older full-U1-empty bevel fixture; that distinction is retained. :contentReference[oaicite:0]{index=0}

## 2. Source authority and reading

The entire continuation journal, including the literal B9 payload, was read consecutively through EOF. Complete delivered file: 243,195 bytes, SHA-256 `99af6d5d4722e1991272964d256bc66bc7c4df552068374d3ad2c5d2c091f16c`. Its internal working-memory hash is a different object. Files rendered 1,397 lines; the raw Markdown has 1,385. No text was missing.

Authoritative parent: `minimum-0189`, SHA-256 `72a6196fc990a16a545b77e6c52a543c4eac04d17fa9cd4b9372e2c2f17b8cfa`. Its accepted endpoint proof, facet-foot lift, mixed cubic, and true-feature conventions are used without claiming a new independent replay. The unchanged earlier evidence remains available. The mounted complete `quad_blind.py` was read for its exact geometry helpers. No scientific alias conflict or missing computational dependency was found. No research connector, unselected archive, or external source is used.

The new source below is autonomous: it includes every helper and input rather than importing the parent. The new proof is given here, separately from the inherited results. B9's actual endpoint637 sharpness control is not renamed as one of the new internal-root controls. :contentReference[oaicite:1]{index=1}

## 3. Complete internal-root proof

Assume strict convexity: `u<1, v>0, v>u`. Let the actual physical foot be

`p0=M^-1 q/(q^T M^-1 q)=a+eta e+theta f ∈ relint F`.

Scale the tangent metric so `e^TMe=1`, and write

`e^TMf=t, f^TMf=t²+d, d>0`.

Put `A=a^TMe` and `B=(a+e)^TMf`. The first two weak arrows give A,B≥0. The actual foot equations are

`eta+t theta=-A`, `t eta+(t²+d)theta=t-B`.

Hence `d theta=t(A+1)-B>0`, since theta>0 at an interior foot. Thus t>0. This is also the tangent restriction encoded by B9's actual-edge mixed cubic; no diagonal is being treated as an edge. :contentReference[oaicite:2]{index=2}

If u≥0, the interior foot has eta,theta>0, and

`0=p0^TMe=A+eta+t theta>0`,

a contradiction. Therefore u<0. The e-projections at vertices 0,1,2 are A,A+1,A+1+t, with the last two positive. Their positive interior convex combination is zero, so the projection at vertex 3 must be negative. Set `h=u+vt`; then `A+h<0`.

Since eta=−A−t theta, the third internal arrow is exactly

`C=x3^TM(x2-x3)=(A+h)(1+t-h)+d(v-theta)(1-v)`.

If v≥1, strict interiority gives theta<v. The first term is strictly negative and the second nonpositive. Thus C≥0 forces v<1.

### Constructive sufficiency

For arbitrary u<0 and 0<v<1, define

```
t = -u/(3v),       h = u+vt = 2u/3,
J = 1+t-h,        B0 = 1-u+2t(1-v),
d0 = 1 + t B0/[2(v-u)] + t/(2v)
       + [-h J + (t/2)(1-v)]/[v(1-v)].
```

Choose any d≥d0, and put

```
theta=t/(2d),  eta=-2t theta,
G=[[1,t],[t,t²+d]].
```

G is SPD. The four strict polygon inequalities are

`theta>0`, `eta<1`, `eta>(u/v)theta`,

`(1-u)theta-(v-1)eta<v-u`.

The positive B0 in d0 safely dominates the coefficient of theta in the last inequality. The first two arrows equal

`A=t theta>0`, `B=t/2+t² theta>0`.

The third is

`C=hJ+(t theta)J+d v(1-v)-t(1-v)/2>0`

by the chosen d. In the genuine linear frame with columns e,f,a, set p=(eta,theta) and, for any y>0,

`Mhat(G,p,y)=[[G,-Gp],[-p^TG,y+p^TGp]]`.

Its Schur complement is y, its foot is (p,1), and it realizes the three strict arrows. Congruence back to the actual coordinates changes the metric, not the reference or volume centroid.

This completes both directions, including weak selected arrows in the necessity statement.

## 4. The largest-ear rule and what it does not exclude

B9 gives the endpoint case `0→1→2→3` exactly when u<0,v>1. :contentReference[oaicite:3]{index=3} For completeness, the first two arrows give u<0,t>0 as above, and the third is

`(u-1)(A+1+t)+(v-1)(B+t²+d)≥0`,

which is impossible for v≤1. A complete endpoint constructor uses the same t,theta,eta,G,Mhat as Section3, now with

`d≥1+t[1-u+2t(v-1)]/[2(v-u)]+(1-u)(1+t+t²)/(v-1)`.

The foot is strictly interior, the first two arrows have the same positive values, and the d(v−1) term strictly dominates the negative part of the third arrow. Thus this handoff includes the recovery formulas for both cases, without claiming the endpoint result as new.

The areas of the triangles remaining after deletion of vertices 0,1,2,3 are proportional to

`(1-u, v-u, v, 1)`.

Applying the two criteria to the eight oriented cyclic paths yields:

| Shape sector | Unique smallest remaining triangle | Required local attachment |
|---|---:|---:|
| u>0, v>1 | delete 0 | 0 |
| u>0, v<1 | delete 1 | 1 |
| u<0, v<1 | delete 2 | 2 |
| u<0, v>1 | delete 3 | 3 |

Deleting the least-area triangle removes the largest ear, so this is the largest-ear vertex. For each missing edge exactly one orientation, toward that vertex, is locally possible. The four possibilities comprise two endpoint-root and two internal-root paths. If u=0 or v=1, the minimum is tied and all sixteen patterns fail, recovering the trapezoid theorem.

For explicit reconstruction of this finite relabelling argument, the transformed (U,V) parameters for the paths are

```
0123: (u,v)
1230: ((v-1)/(u-1), -1/(u-1))
2301: (u/(u-v), (u-1)/(u-v))
3012: ((v-1)/v, -(u-v)/v)
3210: (u/(u-1), (u-v)/(u-1))
2103: (1-v,1-u)
1032: (u/v,1/v)
0321: (-(v-1)/(u-v), -v/(u-v)).
```

Use U<0,V>1 for the endpoint root and U<0,0<V<1 for the internal root. All denominator signs follow from strict convexity.

This classifies a local boundary path, not an entire rooted primal tree. A complete tree may impose incompatible outside arrows even when its local attachment passes this test. The external theorem below gives a concrete such incompatibility.

## 5. Closed-root upgrade and the exact cross-edge identity

### 5.1 A useful weak-boundary lemma

Let F be any true polygon, not necessarily a quadrilateral. Suppose its boundary minus one true edge [a,b] is a selected weak primal path, oriented toward a local attachment. Assume its physical root fan is closed: all outgoing polar arrows from q are ≤0. Let r be the actual neighboring pole across [a,b], and assume the selected incoming arrow r→q is ≥0.

Then the physical foot is actually **strictly inside F**. Indeed,

`D(q→r)+D(r→q)=-|q-r|_N²<0`,

so q→r<0 and the foot is not on [a,b]. It cannot be inside another boundary edge: either direction of that selected primal edge would have a strictly negative arrow. At a boundary vertex, any selected child arrow into that vertex would also be strictly negative. Every internal vertex of a rooted path has a child; the only possible exceptions are its endpoints, already on [a,b]. Thus no boundary location remains.

Consequently the exclusions below also hold for **closed sign cones**, not only a strict root fan. This matters for compactness arguments.

For a strict stable facet and such a rooted boundary path, both missing-edge primal arrows are strictly negative. A nonroot endpoint has a weak outgoing selected edge; since the foot is interior, its other boundary direction must have negative scalar product. If an endpoint is the local root, strict norm growth along the path makes its arrow to the other endpoint negative as well. Therefore, writing d=b−a,

`U=a^TMd<0<V=b^TMd=U+J`, where `J=d^TMd>0`.

### 5.2 Genuine external-edge identity

Take an actual vertex w in R but outside F, with a true edge to a or b, and use the same actual origin for q and r. Thus

`q.a=q.b=r.a=r.b=r.w=1`, `z=q.w<1`.

For N=M^-1, define

```
J=d^TMd, U=a^TMd, W=w^TMd,
s=q^TNq, beta=q^TNr, tau=r^TNr, D=s tau-beta²>0.
```

Then

**`D(w→a) = W(U-W)/J + (1-z)(tau z-beta)/D`.**

Proof: in physical orthonormal coordinates, split into the true edge direction and its perpendicular plane. The normal plane is spanned by M^-1/2 q and M^-1/2 r, with Gram matrix `[[s,beta],[beta,tau]]`. The normal coordinates of w and a are (z,1) and (1,1). Multiplication by the inverse Gram matrix gives the second term; the edge projections give the first. Every object is an actual incident feature.

There is also a homogeneous mixed form suitable for a scale-invariant metric model. For any reciprocal pair N=alpha M^-1, with `alpha=tr(MN)/3`,

```
3 J D D(w→a) - 3 D W(U-W)
    - tr(MN) J(1-z)(tau z-beta) = 0.
```

This has degree two in M and two in N. It is not a scalar cofactor transfer.

If r→q≥0, then beta≥tau, and

`D(w→a) ≤ W(U-W)/J - tau(1-z)²/D < W(U-W)/J`.

Thus a weak ingress w→a forces **U<W<0** and

`D W(U-W) ≥ J tau(1-z)²`, hence `D U² ≥ 4J tau(1-z)²`.

At b the corresponding necessary interval is **0<W<V**. An outside vertex whose edge projection is beyond either endpoint cannot escape to either endpoint while the incoming polar arrow is nonnegative.

## 6. An all-metric actual external-cone saddle theorem

Use either admissible quadrilateral pattern in the canonical chart: endpoint `0→1→2→3`, or internal `0→1→2←3`. Let a=x0,b=x3,d=b−a, and suppose F is strictly stable.

Both cases force

`d^TMe<0`, `d^TMf>0`, `a^TMd<0<b^TMd`.

For the internal case, t>0 and the first two arrows imply x3^TMe<0. Since 1-u and 1-v are positive, the third arrow then implies x3^TMf>0. Vertices 1 and 2 have f-projections ≥0 and >0; the zero interior convex combination forces x0^TMf<0. The four displayed signs follow directly.

For the endpoint case, put h=u+vt<0. Its third arrow is

`(A+1+t)(h-1-t)+d0(1-theta)(v-1)≥0`,

where d0 denotes the tangent Schur parameter, not the edge vector. This forces theta<1 and `d0(v-1)>(-h)t`. Hence `d^TMf=th+v d0>0`. The remaining signs follow from the negative e-projection at vertex 3 and the missing-edge lemma.

**Theorem.** Let R be the actual neighboring facet across missing edge [a,b]. Suppose w is an actual vertex in R but outside F, [w,b] is a true edge, and, at the actual reference,

`w-b = -lambda e + mu f - nu a`, with `lambda,mu≥0`, `nu>0`.

If the three boundary arrows and the true ingress w→b are weakly nonnegative under one M, while F is strictly stable under its inverse N, then **[a,b] is a strict physical saddle edge**.

Indeed,

`(w-b)^TMd=-lambda e^TMd+mu f^TMd-nu a^TMd>0`,

so W>V>0. Apply the cross-edge identity with endpoint b. Since w→b≥0,

`beta-tau ≤ -tau(1-z) - D W(W-V)/[J(1-z)] < 0`.

This is an explicit forced negative **nonroot** polar arrow r→q. The opposite polar arrow is negative because F is strictly stable. Both primal arrows on [a,b] are negative by the missing-edge lemma. All four primitives are therefore strictly negative: a genuine saddle, not a weak packet or an integration-edge artifact.

The reflected cone

`w-a=lambda e-mu f-nu b`, with `lambda,mu≥0`, `nu>0`,

similarly forbids ingress w→a and forces the same saddle.

In particular, a selected complementary pair with F the dual-root leaf cannot contain the stated external ingress: its complement necessarily selects r→q≥0. By the closed-root upgrade, this is a **closed-system exclusion** even when the root inequalities were imposed only weakly. More generally, the saddle conclusion needs no selected matching at all; actual H=0 mechanics excludes the local configuration whenever those true arrows occur.

The cone depends on the actual reference through a or b. Replacing the own volume centroid by convenient fitted weights is not licensed.

## 7. Why the external hypothesis is substantive

It would be false to eliminate the four surviving quad patterns merely by adding the single mandatory incoming polar arrow. **Every locally admissible pattern, on every actual quadrilateral at its fixed interior reference, can realize all three arrows, the strict full root fan, and r→q>0 simultaneously.**

Use the endpoint constructor from B9 or the internal constructor above, increasing its tangent parameter d. In the frame [e,f,a], q=(0,0,1), and the true adjacent pole r=(r1,r2,1) satisfies

`r1<0`, `r2=3t r1`.

The constructed foot approaches a through the interior. Put `k=r.(eta,theta,1)` and `h=1-k`. For sufficiently large d, 0<h<1. Explicitly, h=−t²r1/(2d); adding `t²(-r1)` to the constructor's d ensures h<1/2. Set

`A_r=(r1,r2)^T G^-1(r1,r2)>0`.

For the complete metric Mhat(G,p,y), direct inversion gives

`y D(r→q)=h(1-h)-A_r y`.

Choosing `y=h(1-h)/(2A_r)` makes the incoming arrow strictly positive without changing the boundary arrows or foot. This is a universal constructive local extension, not just another numerical example.

On the actual body below, the source preserves all four rational examples. Their full physical signatures, respectively, are:

| Path | Kind | Own strict (S,U,H) |
|---|---|---|
| (1,2,3,0) | endpoint | (2,4,4) |
| (2,3,0,1) | internal | (2,3,3) |
| (3,2,1,0) | endpoint | (2,3,3) |
| (2,1,0,3) | internal | (2,5,5) |

All have weak000 and all 68 primitives nonzero. None is110; the source retains their full metrics and censuses. Thus the new obstruction genuinely needs external continuation, not an unsupported extension of the trapezoid ban.

## 8. Whole three-parameter actual E17 family

Start from the following ten raw vertices:

```
0=(-1,-1/2,-1)  1=(1,-1/2,-1)  2=(1,1,-1)  3=(-1,1,-1)
4=(-1,-1,-1/2)  5=(1,-1,-1/2)  6=(-1,-1,1)  7=(1,-1,1)
8=(-1,1,1)      9=(1,2,3).
```

For parameters in the COMPLETE CLOSED box

```
alpha ∈ [1/5,3/10],
beta  ∈ [3/20,1/4],
gamma ∈ [-1/20,1/20],
```

form `Yi=raw_i/(1+alpha raw_ix+beta raw_iy+gamma raw_iz)`, uniformly refill the convex hull, compute its actual volume centroid g, and set Xi=Yi−g. Every denominator is at least 2/5. Positive projectivity preserves the true lattice; actual uniform refilling, not transformation of the old centroid, is mandatory.

The complete maximal-facet sets, with cyclic order up to orientation, are

```
F0=(0,1,2,3)    F1=(0,4,5,1)    F2=(0,3,8,6,4)
F3=(1,5,7,9,2)  F4=(2,9,3)      F5=(3,9,8)
F6=(4,6,7,5)    F7=(6,9,7)      F8=(6,8,9).
```

The seventeen true edges are

```
01,03,04,12,15,23,29,38,39,45,46,57,67,68,69,79,89.
```

Because the original F0 is a parallelogram, the four deletion-triangle areas after projectivity are a common positive factor times its four vertex denominators. Vertex0 has the uniquely least denominator throughout this box. Thus its uniquely largest ear is always 0, with no trapezoidal point in the box.

### Two uniform external gates

The complete box satisfies the b-side cone for both:

```
Path (2,3,0,1), internal root0:
missing edge12, neighbor F3, true ingress5→1 forbidden.

Path (3,2,1,0), endpoint root0:
missing edge03, neighbor F2, true ingress4→0 forbidden.
```

This is proved with exact actual-centroid polynomials, not nine sampled geometries.

Write di for the ten projective denominators and Pi=product(di²). For each path let a=X_path0, b=X_path3, e=X_path1−a, f=X_path2−X_path1, and let sigma be the fixed sign of det(e,f,a). The two cleared numerators are

```
P_lambda = sigma·4 Vol(P)·Pi·det(b-w,f,a),
P_mu     = sigma·4 Vol(P)·Pi·det(e,w-b,a).
```

Their positivity proves lambda,mu>0 by Cramer's rule. Also nu=1-qF0.w>0 follows from genuine outside incidence.

For recovery, the source constructs the sixteen positive tetrahedra of the raw origin fan. Under projectivity a cell (0,i,j,k) has actual volume `Vcell_raw/(di dj dk)` and actual centroid `(Yi+Yj+Yk)/4`. Consequently the actual first moment is shared across both cleared numerators. Each determinant of three point differences expands into four oriented tetrahedral determinants, using

`det(Tj-Ti,Tk-Ti,Tl-Ti)=det(raw_j-raw_i,raw_k-raw_i,raw_l-raw_i)/(di dj dk dl)`.

Multiplying by Pi clears the denominators exactly. No freely selectable masses occur.

On affine unit-box coordinates, each of the four resulting polynomials has total degree12, 455 nonzero monomial coefficients, and tensor Bernstein degree(12,12,12). All **2,197 coefficients per polynomial are strictly positive**, 8,788 in total. The exact minima are:

| Path | Numerator | Minimum Bernstein coefficient |
|---|---|---|
| (2,3,0,1) | lambda | 19978932915567/1280000000000 |
| (2,3,0,1) | mu | 1933783948629/32768000000000 |
| (3,2,1,0) | lambda | 80932086975681/6553600000000 |
| (3,2,1,0) | mu | 32559581545659/5120000000000 |

The source reconstructs the full monomial polynomial independently from the Bernstein basis. No cell pruning or parameter truncation is used. Eight box corners and its centre have additional full actual hull/two-fan moment audits and exact comparison to the cleared determinant formulas; these nine evaluations are secondary algebra checks, not the continuum proof.

### Exact selected-tree coverage

The source enumerates all 5,440 true primal spanning trees and verifies their complementary dual trees. Exactly 2,252 have F0 a dual leaf; with ten primal root labels this is 22,520 raw domains. The largest-ear condition leaves 1,291 domains per missing edge, 5,164 total. The external gates remove 471 with parent(5)=1 and missing12, and 269 with parent(4)=0 and missing03. The sets are disjoint. Total closed18,096; remaining4,424.

One complete TOPOLOGICAL selected example, rootU=0 and rootS=F0, is

```
Primal edges: 01,03,15,23,45,46,67,79,89.
Primal parents: (0,0,3,0,5,1,4,6,9,7).
Complementary dual parents: (0,2,5,0,3,4,3,8,2).
```

It contains the required boundary path, ingress5→1, and F3→F0. Both are actual spanning trees and exact complements, but **their simultaneous physical feasibility is excluded**, not asserted. The full separately feasible primal or dual cones of this complete example were not decided. All22,520 domain masks, root labels, attachment vertices and classifications regenerate from the capsule.

## 9. Strict independent blind witness and physical controls

At `(alpha,beta,gamma)=(1/4,1/5,0)`, the actual uniform volume and raw centroid are

```
Vol=6815974520000/501096769173,
g=(-956319634108060/2161630598426299,
   -601799320007230/2161630598426299,
    94557408739865/341310094488363).
```

Centre once: Xi=Yi−g. For path(2,3,0,1), let `H=[X3-X2, X0-X3, X2]^-1`. In this genuine linear chart u=−6/23,v=13/23 and

```
q0=(0,0,1),
q3=(-4430383438/3385375499,-2044792356/3385375499,1).
```

No polar recentering is performed. Define the small exact chart matrices

```
MC=[[1,1/4,3/320],
    [1/4,1,-9/160],
    [3/320,-9/160,803/800]],

NC=[[49/100,-51/100,33/100],
    [-51/100,33/25,9/50],
    [33/100,9/50,34/25]].
```

Their leading principal minors are `(1,15/16,15/16)` and `(49/100,3867/10000,3057/10000)`, so both are SPD. In actual coordinates the independent matrices are `M=H^T MC H`, `N=H^-1 NC H^-T`.

The four primal values are

```
2→3: 3/320,
3→0: 31/160,
1→0: 9141/169280,
5→1: 12602717213009763863638042456781/
      156571129482911194369265892302400.
```

The full root fan F0→F1,F2,F3,F4 has values

```
-141231763236564/189565375841675,
-31083059002919/15837558065250,
-91504457931/169268774950,
-1857740885650188/8074868650080275.
```

The additional nonroot escape is

`F3→F0 = 14945985612561854143/573038363461474950050 > 0`.

Every one of these nine true-edge arrow forms has rank two and inertia(+,-,0), up to the sign convention for root inequalities. The exact mixed diagnostics are

```
tr(MC NC)=232483/80000,
Delta=609918417/800000000>0,
R=39410303281/12800000000,
rho=39410303281/108096690578.
```

Therefore the SAME pair survives every inherited mutual aggregate/cofactor operation. The hierarchy's precise scope, not an arbitrary mixed inference system, is what is being defeated. :contentReference[oaicite:4]{index=4}

At this own centroid the external cone coefficients for w=X5,b=X1 are

```
lambda=28869266884651/104273654884539,
mu=16778484501455/312820964653617,
nu=71226933734/215887484233.
```

They are positive. For d=X1−X2, the chart projections under MC are

```
U=-63/1840,
V=11831/42320,
W=201904399020503167/575590574962655280,
```

so U<0<V<W. The external theorem excludes every common reciprocal metric realizing the nine signs, not merely MC. At the independent pair, the scale-invariant mixed identity's exact residual is

`30417264601183321720800050990978367616943269397067 / 205504624027582220053453973262888329729537368000000`,

whereas it is exactly zero for each audited physical inverse pair and its positive reciprocal rescalings.

### Actual covariance conditioning

Let SigmaC=H Sigma H^T, where Sigma is the integrated actual volume covariance. Exact principal-minor certificates prove

`MC-(1/14)SigmaC^-1 ≻0`, `(1/2)SigmaC^-1-MC ≻0`.

Hence `kappa(SigmaC^1/2 MC SigmaC^1/2)<7`. This uses the actual second volume moment, not an auxiliary normalization tensor or approximate eigenvalues.

### Physical censuses: not a census of the independent pair

| Physical chart primal metric | Stable facets | Unstable vertices | Saddle edges |
|---|---|---|---|
| MC | 0,2,3,4,5,6 | 0,6,9 | 12,29,38,39,46,57,69 |
| NC^-1 | 0,2,4,5,6,8 | 0,6,8,9 | 01,23,38,39,46,68,69,89 |
| MC+(1/10000−1)e3e3^T | 0,2 | 0,5,7,9 | 38,45,57,79 |

All three controls have physical weak000 and all68 primitives nonzero, giving signatures637,648,244. The first has the **predicted strict saddle12**. The last retains the stable facet, all three boundary arrows, and the incoming polar escape, but loses outside ingress5→1. The independent pair (MC,NC) has no physical census.

The new internal637 is a different metric from B9's endpoint637, despite having the same numerical signature. Neither is an own110 construction.

## 10. Exact costs and important failed simplifications

### A sharp cost with a nonroot constraint

Fix MC and let `B=sym(r(q-r)^T)` for q=q0,r=q3. Set A=MC^-1, c=tr(AB), d=tr(ABAB), L=3d−c². The exact SPD matrix

`Nstar=(1+c²/L)A-(3c/L)ABA`

has tr(MC Nstar)=3, incoming arrow zero, and all four actual root arrows strictly negative. The inherited directional defect inequality therefore gives the **sharp minimum for all five polar constraints**, not merely a lower bound:

`rho_min=1303600384549663417815722881/3703033492313974612111061762`.

Its Delta is positive. The strict incoming version has the same nonattained infimum. The complete Nstar, principal minors, root values and diagnostics regenerate exactly. The fixed-M cost is not a uniform all-M theorem.

### The whole normal-height line is excluded, but cannot itself produce the blind witness

Keep MC's tangent G and foot p=(−1/40,1/16), varying only its normal Schur parameter y>0:

`MC(y)=MC+(y-1)e3e3^T`.

All three boundary arrows and strict root stability persist. The actual external arrow5→1 is nonnegative exactly when y≥L0; the incoming F3→F0 is nonnegative exactly when y≤U0, where

```
L0=22011229100292329660584240528819/
   34613946313302093524222282985600 >3/5,
U0=101050066881/36206456650240 <3/1000.
```

Thus the complete half-line is excluded, including both equality walls. These are exact affine-in-y and cleared-dual-affine-in-y identities, not a sampled search.

Moreover, attempting independent matrices only as `M=MC(y_high)`, `N=MC(y_low)^-1` cannot place this constrained pair in the blind cone. Their product spectrum is `(1,1,y_high/y_low)` and Delta has sign `r(4-r)`. Feasibility requires r≥L0/U0>200. The successful NC changes more than the normal height. This failed restricted route is not evidence against the independently feasible pair already exhibited.

### Compactness and the previous zero-infimum barrier

The explicit external theorem rules out a zero defect on the CLOSED local sign systems. On the compact three-parameter box, normalize `tr(Sigma M)=3`, impose any fixed finite actual-covariance condition cap, and normalize `tr(MN)=3`. Allowing N to be PSD in closure gives a compact feasible set: M stays uniformly SPD and N is bounded. At R=0, trace normalization forces N=M^-1, which is forbidden by the closed-system theorem. Therefore any nonempty such set has a **strictly positive uniform minimum rho**. For the nine-sign system the cap48 set is nonempty, as the strict witness even has cap7.

This is an exact existence conclusion from compactness, **not a computed numerical value for the uniform floor**. The effective quantities delivered here are the mixed identity, the forced-negative-arrow estimate, the all-height separation, and the exact fixed-M minimum. B9's unrestricted facet-only rho→0 theorem remains intact; it does not retain this actual external continuation and compact metric hypothesis. :contentReference[oaicite:5]{index=5}

## 11. What was tried, uncertainty and concrete continuation

The work began with the unresolved internal-root geometry, rather than another cofactor iteration. Completing that classification exposed the largest-ear rule. Splitting a true shared edge into its edge direction and two-pole normal plane then produced the mixed identity and external saddle-forcing cones. Rational local probes found the strict independent pair; all reported claims are reproduced from literal exact inputs by the final source. A naive interval enclosure of the parameter box was abandoned without an exclusion claim; clearing the actual shared centroid into four polynomials yielded the complete Bernstein proof.

The principal preserved negative results are that all four allowed patterns admit a real incoming polar escape, and that a height-only independent construction cannot realize the new blind witness. The parent nontrapezoid endpoint control and facet-only zero-infimum mechanism are not contradicted.

No separately feasible complete U1/S1 system, surviving canonical E17 orbit, or own110 body has been supplied. The local nine-sign primal and dual cones are strictly nonempty; this is established directly, not inferred from a failed solver. The full oriented example and all raw counted domains are topological domains with necessary selected signs, not certified feasible mechanisms. Other root facets, F0 with selected dual degree greater than one, the remaining4,424 F0-leaf domains, and geometries outside the stated cones are not excluded by this result.

The useful continuation is to attach **the uniquely largest-ear attachment and these true outside-ingress cones to the surviving selected E17 domain catalogue**, retaining the actual centroid. The cross-edge identity also offers a quantitative test beyond those sufficient cones: an incoming dual escape forces each outside primal ingress into a strict projection interval and a determinant-margin inequality. The first local target is the remaining4,424 domains on this box, especially missing01 and missing23, not another root-fan-only or height-only relaxation. No missing archive is needed to continue the actual family here; a canonical-registry overlap calculation would require that registry's exact source, which was not supplied or inferred.

## 12. Complete source-only recovery

The following lossless capsule contains the complete standalone source, including the raw body, actual hull and two-fan moment routines, all small matrices, full physical censuses, full22,520 labelled-domain enumeration, four polynomial generators and all8,788 Bernstein coefficients, inverse-basis reconstruction, nine actual box controls, the sharp cost, and all four constructive local extensions. There is no download-only datum or external parent-code dependency.

Environment actually executed: CPython3.13.5, standard library only, assertions enabled; transport decoder zlib1.3.1. No RNG or numerical optimization is needed. The continuum geometric statements are proved above; the finite exact code verifies their controls and polynomial certificate, not theorems by sampling.

Save the capsule as `recover_quad_gate.py` with its final newline, then run

```sh
python -B -S recover_quad_gate.py fresh
cd fresh
python -B -S quad_gate.py build > build.stdout
python -B -S quad_gate.py check > check.stdout
cmp build.stdout check.stdout
```

Both normal build/check and a separate source-only cold decode/build/check were actually executed. The report and stdout matched byte-for-byte across the original and cold directories. The capsule was additionally extracted from the serialized result itself and decoded successfully. This is a cold rebuild, not a proof-assistant formalization or an independent mathematical auditor.

| Object | Bytes | SHA-256 |
|---|---:|---|
| recover_quad_gate.py | 13401 | 84579271615f4acd1e03b4004b5e1a634beaf6ad2e8a586385699f318a164fa9 |
| decoded quad_gate.py | 27291 | 04f4044385897dc6a096d2d5b02920b91fa912dce7c1964d9ae2d800b81147a0 |
| quad_gate.json | 2460301 | 9d15f0324c64e8c8b254ed4cae760debfe15f59c36f4eef89c53c27f2052c34a |
| identical build/check stdout | 539 | 8f84c40f374fb9a226057663da0d588ea5de0e7356deab4a24c1775af0f4db17 |

Expected terminal output:


[Encoded source block omitted; the code in this passage is incomplete.]


Complete capsule:

```python
#!/usr/bin/env python3
"""Complete lossless QUAD_LEAF_MAX_EAR_AND_EXTERNAL_GATE_V1 source capsule.
CPython 3.13.5 standard library. Usage: python -B -S recover_quad_gate.py fresh
"""
import base64
import hashlib
from pathlib import Path
import sys
import zlib

PAYLOAD = """
c-qB%YjfMUlIVB;3eGuISELNtBK5MYAay++&y4pbc49l5v#YCOQ6gp0rbLCLWGT7%@7vt~NRXnFIeWJ1x)O;5@n|&qjRy7iUrsk^
aykuHr@?A#toPX>UUiQC_P4)%{B-e~`|j%EclZ6pKisQ}JNM$|H}~ov4_9|L7w_CZE*`Gjf45JLE<aEkqjO?+PI^X~c`M&bd?N~{
iI?n0MzHf{nGvqmn=EC<DmLzJ{xIUi@Z*<N6nlPpa`Y+n9)oi^y3zX8Xx$rMHlFW3dRcI?-W$_R82SHiwg_g=M<2W-SY?KnKDxgS
pU%$S-+x?Zm+t2;^ZkE5wZozF>y#bc|9Ro``o_TV`u4CtpACm?&+dD@Zf`mm1pQghf$Pq!8+fyJ*S80AZ#eV2(_v@e1kTKv+k@%Z
Z0?;L-2^X26wkZ}<}r&lX&A54k#TeTV0gwXUaq4c3ye?p>Ah{t11}AyQD97Ce~&YKjN&OYoW`4#e}XtYnkVtnm?wY`?8gX~>p01b
-(>;J$@nPhgjtYeaUA7!U@TZ9kJ>R~oy7iTmWjHvIEsRDkC!kc^dQIEtY)RYqGaRFJiw-SzVxz%K8z?`Ln*AGdhh{mkL2~jOYxDq
eM;k%x=#1$(UBj_jcqV9x7PWQ0e?x5ZIYFdZ2(*5(p#G!nX$F3BT>`yebZycw65~*cyG)BlRIYYfrN~&;ab#HjnmEa^~SBAHHKvk
%#0acUGuED6V0)$r`q^&Rx@C_S(>}%PllT%ahldNHodVuX->z^q~*Z}T-g(VNnEzEuq_@lYNh^Uv5ggMQB{q!+~P31x>+Io2|goO
lhWL>#9IM?<z`WsX0&K{!Dv=Z&&nsYT-MBJJeI@E#4t03kLJ{xXai3aQiH5IEa4fZ#1z_cq~t?~t8L!OH@NJDZoM=G{xSU0{AqS$
vFP@xU)OUP!{V=|fkO@2f4xDQ8raZaq9J=0RA-HJ<c-4#{3A4lh$evhF)%y%yw`r-OwQ9YIL}wFLR#$!{4?GfZ36_eA@7?Aj3Avh
em9#ARw>gLR2L}4M>+k6-eVQ&@%SS_Z5bh~3c~Va1W_6oAI-KPfG2$(lhQB;(?p`U#^uD3#x^tXAE50&ukLQ47zK;jW(NMVbf{Kw
nuW8}T!NA*qX!VSv}itXwGs$gLsvk%RGA8Zwl@Zs%d)nZyn;GwkhfL|t=}41;~ZNwHt@ZH@85zb^RTR$wVdXrOcsqhc+zQZTJRL=
CW{#EO<7=_n)vx$&SbHPqFiu-%D9Lkpo%pL*KqX+K!w1?#yav=0qCJ+kUR!HNbp^_1Whvsh^3N6jKnK1N>5Pl(2S`KO!3?Iqa5+f
cw)vgqF+}qrdW$8SOF-2ijIT_|5nh0AZwJp+wl{S_7)eP8KU4>6<B#2Ad6KDWV+g$E3GU1o5d@b*e1ve7r6Am{43c@{=i4r$MVtI
YAt96YlM9}(T7@wE7MOc;|<XK8^jIX{bW>ZCMqJamn*|?3nqpatlhGaYM9Z2;&DsU5`L-yLJfq_ji^clonWnCwSjd5%Z7%NxbcgL
iiH|O2NUQ4XS)y&ad`;}Acnv<MLqE-@E`R@-^94`E)`t-zYM&XTH3-?84*SK0Wr|9%y8<P0sKfO)iF>CINuf5q?;(i)teNQ2k3!;
sP6*Z!qS3@0aXeJT{JZq273-*Svg%n2bv_2oQ{xCA2dGRVYLFYV8o#D6l}wI15=u960#*>KqMOKk{LJgDqw~x$Q!>bLg2iIWD``#
V_M+-DVKn%Ym$Ru&TKd#0<adB5}&Fq)HShDWx=$$uBHOfWq@`#qgAlWOpP`HOz3)N{K9htl)FVj#Fm`U1bX580LEz&c+aI$ta{?D
*TD)T>n<zzSchnN#c-_Z>fy3thcqX(#z#6ELI)am=-i8PK^IFj2YW)YNX}<ctF2LC7cHDh3kx|NCCT~0w2^95y<@sKZ=bj90xCiF
3OlA?Ntz#{$yg;@1?Ov>Y*xT>W|P=yjur+j;GFa$b!X+sDaq(kSE8(iU&K7tF<#2{1-(dRCd!%MGiBAqOIW1T+%iLQzqbx{g;x3y
r(qUu1L50%n+MfkO5qAzBp>zE*C2^o+c*MA2f(6x0%~d&M4CPlPho&CNs%(pSO9s7Uz28ss-yu3YBcS}s+iE>9$FJpqzJ^;2$qTw
0s>qKhn8K@4JZSFVsTVdX4Ldq@S>lRC5PWn>iZaMld?tg5`>S7OsX;Ipb+|)rZ}g08Q#t0on@W&>v&yu`Ic8~v~?W9G9jqgoGIAL
@DzFo&C9j2ElG2V4y-z3Q}05q<T00!{Mdp!6dbh1IB?!W6Igh1+C8e%LeD?$te_0El%MrZP3#rAexAH4U-9qQP?%`0)e`IIuuh$}
&QNmt%0gDgwW46@Zl20&xyYqiSA@=Zd{{4uU!+$Qzu>)?T<$4&36z`YR)SVK^pfBK_<Ku1NPBecG}rnG*kCo=D;+Mxf#?FBBV*;d
X<oKXsD*W?cS$Pg=q)SiNy#q(TNe3jC!|g><6vI0r-Qk2k%LvbA+fWLqa0xPnio??0~B4qr8MLdGJRnxrm$uOy3lq+NsfHFw5*bK
BP87+-6;ia3YV4{#HE&;t-q-mhQOqu#1#&=stz|l`sYU4tkTTGKoX1=R@qAm{G%GX0nzP~*{g<^7N^7!R>6e`<v2eXg=Tax(vQX=
6djD>`97`X3m6Z8CvWx~2$==A`u3gaR-rI=03C!D6*b6-KobVS8>n0Bf&!FlLZy{y=*#Ej%Qu|}%U*vv&7XSobfTG)G!>=cbz?>I
Ck~7UiIChdsF-*`q&Mc(*0^33&#Uwt6;BK0f}A;th5$qwmIYctot|mqfEj++WjzC(Vw_I&na9nlz2FL;fRF%I_Q0k<&v`tt>L!{y
((l0)26!4b@C~}VaSz{uF5%`Ade^J`_D_5!sj2K><G}E6{H;L}94=w#2GI>%2kCbq;sIjvI;6Eu;D%YSOif_DN|$KCxX3tU=wLS#
<U`7C>%v;mvo6gm)Yg!7+;HV0Om3X`L4rVva`gT0E<OW}^I+RH0Fz)$p5{mVbkN<jku$0#Y9x4IGf|~gx`cnSfoQJZ=Z!@@JFijn
Bg-5HrWP#T<$qkhySgVi*k+;_p0`<-^+eS+>##G{XI;^*#|CVOz-kyV9Vnu99k@8di!QVnupVCap==;7&e#yx?drEbiV-b_BhV*|
U=kj182BVuuy6S6V7J)4J}``e^<XUc?BO6VhWI?APi#4$Pcbt5eYm*0x_N-n8$a4`Xvli*{ht?D_g~$2XdL}|`ww*f&5vSoA7L(b
n^q7noi-NPfC5p1%PEWC8<z=yxw=!~GEtSuzA$X|;o{*>>>qH(5UWS;FLm-0vEG~zP19z1A05`gF%(`^=R{RQX7>vyI|3$I3Rh=s
SeG^eh%ny#c*u`t7aF!j7d=~Db~<#Wk6(W35W0q}SFR-6sYh71i**Go((MUXadHp=AIqRA`$6=S$xx|^XoCUwm~6oG3Q(0T${k|d
acPQpEjojqMIjz(v&}NlqAu<sfwP!+%ODF9WwQybXCI?1FCH=(%_s2#f}~`F$!OSHX}WqZ*h3MbR!y0&v@LYN^4N-QH$p>-PC_3g
cat7+PHd`|k87M*>Tkk%zU)wk37H}_0~p8bkqHx+D?b#5WC9e70+&WVtO8f#;l$$H)ccaX^D!#V9edPJ1`XtF=PU@g48baBZ1!lg
G<;loyl{)5=Btp<(`^Al(ScQQDs0Z-lOofPa7__z8Kyq050G)O4p?Q3h}G~q2c%ZZ2-m_$M*D^5%f4VMD|eY!Y$1E7n(m9Y?ZaAD
ZmfM_rhJlHYQk!t>xLS6-fUNPF1A&lTkh8YS$_eN<lIIJicDk-6jBgPJ$z%AJfLu<vjW$+0$6etFENY>OwBPk01NGIVW1EY!;xT)
$__5B29l2pen^(Yq0b*#UVqDG@zzU1515+M@)XTy`xznlU{RQ04q?HHRS-BT%sn&+MBtul{@Pr$w3w6!1w?kyHhTdRMTTOakCp3f
{1E!VAZ5PmxbTw9L~+6>_H-`!087RVHM_=S<gqE6F`tjOrQIiNBq(FS(d|;(XcWT$$tA)U;KO)e9*m}7(NHxRvflAA7@P~X-3o%+
Znb#*mo+^VJz`6XeG%2ZU@ZY5p{p^Go)L7!zVe+2ymclelKqNggS@eMBfhuWw{3N?(TQfkcI?ZVVQ&&km}uaJKrmUD?M+0*3;V(n
wq$C<0+)lUS&yDLnbT0l$e_k6DZn;d>=A3_qn8&dd^xC`azWNmzJkdE0)x!c%MvKdJke*87YSwH^Rx-iTG*zEAEU3bX<0x&Ni_Jr
x}eTpEQPSIlBc3Y%AcCP-xU7O3xiomdmWxY`O8bw+_YX^tmCJqX}7*wO%niUekBm(n9+LS@qF_P5on!?aNZ(b#*e`&h&L(kG-0q-
r>S=ex751%YUeuB{~Lc|pZJD-<}WWS<tZc7;Ri#6!GHD}zzpQ_^)T)$JYtvT$@SSX^kGZo2@t}nCUl$xX^53MP6Y77wCTA?FbmfS
2KwE+p7z`-%!I(5#ld_Y&O%ZiIimsrg40Cq%)h|10h{v!RxN22IR-@|WH_5i?h+N_Y!M{fLxHR+b1rL0$xQWTGY;gbi3k{*QDY3F
3zzj}0*X=fqIL))Z^>J;8H&!=$Drp_eYxRqWB;gfiz<j{(T4hVCZ)(749S)ow%VwLz;#$q4AI<6bT9cBmVbO+3eCO0lt4g_@b8%K
TlT?LbII0IrlkkYA8tD)ab(I7a5=ed?+L5Dv_5jlNj)_{$A2{YXLfHm==Pj8{DCQJw}<^fe`pUnH4SxThRw+x$VnM(^IpFLo=T@{
x6j)BHgoL0-S4z}!?Ui_cZRzE1hxBZdoUb!aOi>4`AO|zx7QnV+h>E$@T}isFhmC|@L{)mcGl^4)Sg8li@Bz%&_5|n$Ak)KPazP@
>5wzi!3(jm|78v2A*a_SkH)Gj%lpeb1>ojVh7LVGmR=)xLF7la$uqR2^}F7B5omQ8fW_Fy4x=vEm5Aa!32rN?A!;-}@1Q}Zc|jdp
c|k+Fi`PTvtZf~b>eO0U>!5)+%?vOE#4YG5jxz<)7c2*WZZ5Sn3*oGTOD5`vs~H+WkD4@7^H;-qI}>}g-n8GS+RDgV!t{&q90;<2
ZBs^Fr3~z>B&6J)vDpw3wE?TS_7Fp5foY;1_mT!KHTv;SwE!QFX(4Drld=gZaV<u!#M9zUG7Fd=rfa^XU@Qq63dYiXCDg^oV^g#l
KTn$2Y#dFFWl1DUo+s9+Q@cA6m3E&FH!LQ#mMwXQoR_z6pvkktMbghRZe@UH8BO3{i|!-zEMM8kpkZ0`O6CTTv{N79qaok4s}bpC
5yeE^iVMwYwFO#u2s$-+3^LHUOAl6k$36DLEf!E$UbG1$)rn;hOCqR7v46Ol$6Qa}d4E}@PpmR-WJ3Bm9jALnQ3P=24{M1$93dy$
!=ZiFwFjayHF(=TY=Y@H)Sxp2A=qhmoHGn3oPk*F58J)Lne~R^DpuJH++o_-4ztEapy;1u0w$*f6_OI53}G(9*3*dHVHkudOAM_&
%8XXO!vJy-(6P@za&#S%B0s=5V5V&k+uhD^*ml~zcE|1ySZ~nl;S{>VzSHmZ4g`)iFbEl7f4#t-ly0R41ug%I(SjnIf`C<#Hk&ED
uNV6?1e-{gDJyW-*is6S5VKZSUexal8YD!p$PbV(VIY@ei0h@U>Zsp6YcMo9fMn{?gB=Kw=1w=6yNcalC&qBP-3HV2J}$CNRATAE
N02Mm0y;~!C|C=4LvC7CjWbsAUl@f)WSQpkHFAciW<y|B5C|j@+n$i_!rN+GdZG)JV7I2NcK)q|%5$?10(M}rpJNlNb}<}UgUlbI
@*F6;3qt(+7+3TlGe;&u1walcb}emNy>Z`QjZg6Z&xQpeQqAG0oR~Bf`(+~F>!5-!YXNfJc-fEJ;g-z~cW`#&-b6ZdV(+k4I8sB9
2-0FF+!EsDgP&OV<+aFDLH)l1)p*=#&WdE&>XxtodQuCu804RXPOW)K?BmLDVn{N@-1mIR1a$+EOO!1gUSb-hXFQuLJE?~=v&l{x
dCo!cQi{?vir1hZoR(*gB5=2CxHzRk;ojPs$%6BT?yQmTaHm-=Un&r&t?P5&Y5DeO0RZxr>Dw(?Zk@`DQrZm`Nw-)&ep6Bs2pQ@f
5U;l53_(ITLy*Rx9NImwdb@29t7rBQ%-g;V8U(EAP6s6Lu+ww84*Z=t!?Rw$qO1ru=+y@6z1ME{`_KjJ^qqFU+w1pxZRpmj0Pz-W
$)2!bvH2UZB>){$5!5)v;<sR%=dzXZ&^5uv#3g;>heKCwot2h*Uh;*ie0;E&dtg~YT+`gQ0E&Ya`|5J-E!D*Ju@QoO(CWbGhGu1>
8%=B=>D=5tfHaECvYD(#f77lpJ|ziZT+b!y=ORqMkTSan{xv2RQ^9*{l!g@V(i&RQx!bJ#lJ!gxc5^&_e~Ec3Pm@*}ii=abTazVS
lNntV%Hwg~h0{{q{<W^OB`<s=-x>+9l~j-$BEH1V-;H~i;M$mnyTEU~2g@_f&JA$!0dK3vD9D`+W8p>fbPXELh}RkDD$rW6AZaYS
Nx@o8=V6c<0VvG9-1H#drfAB*vNu9t(KrG{hr@(;Yye}s!YDb(y%aR*6HMnZzaU~0_^^)g6AMBtz<lIW=da;LaGuAd&>4ACqy^7o
IFvP-*)qK4P2t8VVqM;pc~cdf!`L$ineMb^c5`M!Cmxq|WH1XiwiAThKBg+C)W&Lho}`aXUf6`zqVOP<<gd*JhjQy|Z33bsYi9PF
cAhLxPla$)JxEi$Q!SOIciF_&o=ZDhn<_~_Ft|ZFcFwvzuu?G&F*vh(1IHnWI6!;6(*=PGvULCw*0F87-M0sQrv$SWsUwJ$rh8Qs
h-yC)1W4$dwBoNE*PX$#&uj+kJ#(abyrBi8u9${ao=^I~h(ZE)$uUZ+KD<PAjaSSB7jnsrqN4Ji3UjXB0Fq8hVQSR*SCvk53+NYR
0UcKQslD+FZy!W$Ddt7~f)KLgHO%5T@zI41P=W&8@`XfkzWcJ%He2Y4*i6C55y#lkHaA&df^vEI&80N1U5Uc6#38yC@)AQ0Mc=e0
t_Xb4XK7(+O$o!g%cfmxKvtb3KAW)vB*Gf;gF;5M=gx6cN7(3~TrhZ;W}F^r;L6RRTsL8e(GL+87toWs8KBc0sObyg&JK(~6_|v%
$Py+D02ct8g^}O`Q0_s(;gfAZJ0u+Sw$_)3s0*WxKA8Z176o1s`1%vqX9>nDxUyP`GhG035(F~kOYObLGX`Qu>=(Xj+2@j`eg~xz
$Y37km5YsKA^TRjD4v7H0&TX_l%B}u7mda{Al2RZj_0>p4mS<6JF3K?2oz0)vMHw_LW|M&Qz;e9<9vDuaRD_r1bnKq3U1)3$aI3_
qY%O<P<O6o%*QQz(p-(;a*R(V96v{2Ho+#~q9li$wqWVWd7W!jnGya0qe|#^BCbxG0Mq=oWmgXn?B7apfdK6%Z`$YLg6{-O%C6WS
<g3$TklQOA4bV70Ef)l0catPYo=-6Y!GT8BXoe?VQ!Wp_nqbK6f$CGVOZd0%qhQW!TyJ5h`CMfdDd(~yvy2XotJH+rY;dcG8et)%
d`#YcX-}qlU;*8GMeX>3cKP|ixg;^IaRW3MRRy4rd4YD?R~iTNn)8AHmpF_<169UXl3$LG-M}Pt@GvMT5`W+D;<Q0mhO#K%7n=e%
c3y`XIDcLTwptiEqoN)4nfkP;qd=wsN^^B3mrJG)aI?1NJy3?d=vYf?1q{)OoS?AXnR0xK_K-qQQwQ#cHrQD7S@NERXD*<W=x$rp
BO-|cQ!cOI-Ey*Kyyn$|IttTtT!#}w<6&}Sq}}9gr`!S90vUMcjerDgoCbaa+d;pmxQR<and9aY%(qcxR~(+V4>Ro5`eCm?c_8=w
@&e`uf^sGs%Wn{5dD+P$5RSZtMLM?Yl9m-MaN@pPc=Q0@_PLrK>fD~KX87Z7ka6>Fy0~nmZo2K-Zse3j&4am0K~oBrkR(}p=`#iJ
?Kf}260=*h+_Zd$u`~s(LXMYZ-fV&CLmbwGNqEIqc_&NCIiZnrsla>PZkrYC#vP~Uu!1PKJ?QlMTGC0eu)JsYyR3v@-W}Mige&g!
hb*Tf-t9WwgTqVOx(f@}L_hzV?F?;k;569ratf!OwyCFPilj_E5mO$h<RvZ+G+7kvCZqq3FkG({lLk9v(Y7`6*Y)B>xyisXW87lI
#K|7B8K$ld*`O3y_eCWKDqzJf<;0fvplJc+YHHUOlj{PeSCVV6vH8qo1`S+jDa;zuYZ94*oriCzaHVY~bCGteQZD2i7=P>h3CTZE
pRjPyr6wSuO3_fU+CvQ1U;K!+q!F*8{Rj^wF9S61sZ6{qBaFZTHfE6*E*qLv3uKKO*F?{Lj8vC$$%6SI_~j-t*X)awy74CC+PP*=
B%G}kQpy(3lu=;p%i&Y}d*&imy*+*rDNF37c%1{d_ahi<{5;|CMFQ@b;n_6nc-P#QQrm-b5zh@6MRc*c9FNX;ssrEa0JsHavO9be
z^p0X^C4VDbGK_YS3*(j*h&Ef%c-=o7%881j;nGnDw)&+tYRRrY$5K_b9m6?I~^J*QHEHs0@8D*K>~hgfE(5-H8lj6Nxk9&m{Ucf
h&|UeuK}>~g<Buh1~arX=evA$^AktA^#NYbkA85H3>u)DjbOs}v0ZbpED+uU)U-wjKYtzta!SGBfg1p7985TT5g7!M3}(%bCYp&r
7h*_@(XAX<6&C#w=~jpZJ1rB7h?`v(z9M1(mIYrM6VGKB?N_xb#uT^<E!GT}F2*cKd=r2$cQHc`#{5@sj(z<9LAuyfo;6D-eYToq
j5p1eZ8e+bb4wQd)y1Rk^U8#(zqT|g=>}U!dRAc`B`4$<8dC_iG@Hs_1^kFDQ94Tnld}%<LqxB6I=9j#%an;Hl1=B{GK}`_48tdL
5V%>ORtg0x?%M$o`TXwU^YIwdjwiXNoXK<7CFfQondwbm_iePJiFxK(aqe}d6489-sT_bPTm|UMR(w?ePCM_#zfocjnA!F*3dbmJ
?u6A0muvx!_im>|;;*;=0C{SCuOuOxMNO-mkE}I1uNuj_-MK#&1PT0PhMYguotK?(a}l<p*aEPM_ZiU4a<frP_kZW_Uo!Dk14WPm
*g6SPX$fe6fXR_h9tHOIN@mQeJeg{9{e0IOzIwx*AF-^{T3P2XqEN7FCZ<rzqEX(tpz~x7mZ3<RhZVC%bjq8TU-h8U$CLRFj%2@j
B0Eb$t`1+zv)B32>(MrjIMOV5V9Yv(s;?ZOhI((?0=VKxeiAY$KRi88)i6D_FQVK)Z(9PGT2LfF*7#_42dt~DVK@gHJV-!3gzSku
vq;M!)(@4ygv}=wLXD*bc5X}FMs#~1ukz>5m`}^hy!I+To{EY-j`l*>n=*wIUr`1$R-y;R&se3f>tv!REFtbp<CixPoQl^oQ8d-4
Kpcs%)yo$G$>ej@7G%^xm`IpuBZLYl9UY5`ijgbQ&QV;WUPRV_TJA%QLfGfpLimUXn6$^9pM}s?SmDY^)@ozD7v_uFwHaU-j%6|;
L~ZKNs8jS;oD^u{oSN9KnN{CwQGEvorhQ<`!?4PMzbf@4((y6&c|xUTcp#r}kGHlPEd@}BjjD7g##2i+riv3@l#qI(Qe^`n{H1jj
PpMqS(Nx=7GveoXAW8`KsP#x&mPBWLr;-52&`h)5p$`q{=2m+(%U`zS<q?~GN$d#@6p2mwIXm)l@c<vAT+?nf%`vA;O(0hTOZ-P{
UaG3u1-!;^uT4}$GoG6^0Equ&asi$O2VvLk_40dZh;Z)M!$IYx6o83Rs05)Tal-(2lv}8Q%=0T&!^#A-A3S1Im8PT2Syym?0FC9-
(uyU7b<vkqxZErYTyV{@syQow`yQ~gDB?<vmU<7<YiEebhRnwh{WIzf_se1^Pd2n~Bo6F|^~kqkBq^=p1bp=HE67SRl$F(J()&`-
9I!zDt^+UQV1*oyO_8j~tfowffVsJ1yA`dCoIHubiq6mVEeYkwMe(sRYO<_kYh{^kYh{{rIY?^9{`9wa$w0h*IIA%kMKPBr6}2d_
0z8W4d%eWH0j>?sMTl-}mOo+u>%mK*;<uQ<1FV-n`MdEuqF@o=_R1qb5#hAGC<>zZG4Ymob}S0;jcYC3fed!2m^?~x@RGnwwT|Fk
yb2Tu(@=-8@a$cNBZNzlxd0Us5KwE}om)NXC(}+2LeG?oDUdO?&%2t+U5C8v%ll2gNG;KEN3TlFX($g_2O>a#40`xNBMh;O8+Zll
@gnXdzv@R#s(FsDoII%-7Nrv?BUFVz(PhKIt0*bW!VvXqEQ(?ml$*-s@Yw;3FB9w4VKk*fbI#?F$p6a^9|oEmQ!@bbt-_@#BrtTD
Nh6@!ET86RuEVB){pirg6>%XFpJH7|3Q_J+t>6}|xESzlISujkq+O{$)PbK-ZQ8DWRFRk7EO&5Xs4{&p+^btLHQR9Is4gZ<*KEvG
j)|6%YsX1Asa<nkiQ|`&QPmt?H0Tk+;vjRGn_f|Ag(9m`50k4ezJ8W3Uz;+Z;ZrGwa>iz%9WqwrR)`VZ!ccIfKoDP6HAmac^Ko)9
Sx(y6ag_6#*m8wmScX@Wv7@S@)!OkwR149I=T<qH`m6w#PRZ`IOoc4YFu4G8IkIS99C|I(>)GJ!jI96wSDg3ulD(U!M@W^bF7m)A
te=}J;y5`tCR=|vi7MzA+{lcn?JttvGTz#pnw_RRMGnNgeQWE%4Es34Gme{MrwJEZaCxm$)4{6^C~<sZ!SmznSiB(=E0l9o&>kr<
ANaz|lvhl?%TARz1%npC`5E|)H`EC_u^Wc6t^jkf;G5%ZGaEfUA;7K0LYskEo`T)lmZp&5^|s8u$0l^qe0n;T^-mp~nr!>8%&$|F
ROhGC;2TH(oCNzHl3a9t3#5}0tO>xVPTeMS=0Z5{$2>zUwi0@aGm+2&kFydQeQSi*EkraGkJjR(8=ZB<f-*x>k<4j^D|s3k%goK`
))IY`4%ZRAQE`iCt%=QGA*s?M$Jg(H?~+Z}IAZ|Au`f?vKd$l2=ObHNqxG7!`I<dS$KqL@SuR70iTl>*(OYx7^{f&tO`LX<K1}M~
g1O2vdjbXYg&)>wDSNy926~dmbHw|NJ*l(y9G)O)!57h`%DTi{(MS10k4N$T4%T|aLw1Gr4i#)!!Okn-%OuC5ro3nS<Mq0H2E91{
S<dp)@|dl|^K3th^2TwdpG3@$1ge~7>-FP*l{0>Hx=<3`;mJViSN1r{vjat~a$e`YnYY#v-SRxS3-&*7E~awi#;SSkgVMpo>-dpp
17@HP!M<e3I63igL4w5|2Wd~4?9TVvsRt>8<UvP~6)0C!`f*2fIh_i{EXR(zU`4K7exO1f0*?TxB1(^WdrC>wCpzW+8@+NuoQcU_
#FPgXDjS~9dR|G5;ZJ>ypU)@9;_AHe{=}cDLCu2JRpEIhZQ=*&_8<bQwtG46>W@@@S2AwkayPWM$rmj|dWJe0?l7eTxKr$P>P-$(
;jw$+2jP)&^b6E*T+^7sGbpM$lRWP@f3+(0FV`6;Irf7*3la518e%ptQuvO2v{Z^9;0J2eR>G;}^}b=nXX{*cTuu<!si?&F+K$BQ
Xc>kSth~c<xhK(2DQjV;9cMSo*_kN@eUitm^$T|}VM*QNQGJ<qVK(T8JQ}P)c4$Kni+dp;^L`J;-12G{W@h7``B9KYDR#okhwZg@
Pz%z?!Ym4S<FEa~NrTCpGx3HmR!QA-(}m~s`n-7m7t=>qCTG!1y$zQVb(ApB(i>%iaRZs7p}(_uzQJ^#1y;@9a-;9?@w!dFa#qDW
-hky!Y1%-v$Q7yk5&~D|^6E8V^g3AS4D)&$@95Rtz}Z0y#rUa+h_vJxas9_r@Euf<HwBYF@G;MR9klR32apUVikukL{I14LT>Yt)
G(Zf%t)51Lc^~2&iEX#VkFbQPNG=Kd6G<Yz2Wr5?pDa1?H_LTuN|KjvM`maiy3fI0yhMk|fiQX61hQp~^9C5VjsLr9SSPZjG}pxO
X#ANJvr&*K4%En5Sz`$hB!U;tMaz?y1o+jR?z12@5lE}XAXoOCXc6pyc`*o$@>Z550gNm<K|u)pu*Q3lAcXi?hUwDFfMtC7vph+F
zbw#DZ&F<W-(6fjd;;>nvIp+N=Ueypi<^7*;qKFw`|jf5;rjB*y}x*W<=)<1|8afeez>^5Z&-Tso9mk^QUBuZ?)J0$`|aKPd-wj~
?)vh<{q@~7u-J!-Yr$)BsLP8FgPNXlPDB&I{p0T9y?gx|FxmCPe~8xa-noBXUH|bXu-z5#-^IiAZ5>276Jm2pf+I%%@b1&SJLt9r
lVduYdw2Ez0w#2K@wujphd=MGu3Q}B{S^S^e*W|J-IWV2v5Rh}`{DNf`r-QDp#%WFf4G8v5Wo+&pP}yE)#WV|-hH}!1wN1&cOTr}
vHgeJcL3e}^&dCx<?a20dwp{cQ<i9hZmw#Y|9<=F&V6@#35fatD})drY5?`uH<!2XuW$a4-Co@TqU(B)%h2x(+<y1Wb-G;~>*4P9
-M#zy>f-;j+imye_Q3_VDm9ceM+Zhx0}$CV`RhO@LNJQLlSQ!e!$;hqp{yj}1=q!Pt_zIdx+F5)hJ5h~>6WAa0_uKSzy
"""

def main():
    if len(sys.argv)!=2:
        raise SystemExit('Usage: python -B -S recover_quad_gate.py fresh')
    data=zlib.decompress(base64.b85decode(''.join(PAYLOAD.split())))
    assert len(data)==27291
    assert hashlib.sha256(data).hexdigest()=='04f4044385897dc6a096d2d5b02920b91fa912dce7c1964d9ae2d800b81147a0'
    folder=Path(sys.argv[1]);folder.mkdir(parents=True,exist_ok=True)
    target=folder/'quad_gate.py'
    if target.exists() and target.read_bytes()!=data:
        raise SystemExit('Refusing to overwrite different source bytes')
    target.write_bytes(data)
    print('EXACT_QUAD_GATE_SOURCE_RECOVERED',len(data),hashlib.sha256(data).hexdigest())

if __name__=='__main__':
    main()
```

Optional convenience copies: [decoded source](sandbox:/mnt/data/quad_gate/quad_gate.py), [complete exact report](sandbox:/mnt/data/quad_gate/quad_gate.json), [source-only recovery capsule](sandbox:/mnt/data/quad_gate/recover_quad_gate.py). The embedded capsule is sufficient without these links.
