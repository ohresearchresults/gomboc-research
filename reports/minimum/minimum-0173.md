# minimum-0173

Historical AI scientific report · saved 2026-09-22 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# POSITIVE_OCTANT_HIGH_ENDPOINT_TRACE_51_OVER_25_V1

## Determination

**The assigned high-endpoint value sector is closed:** for every actual body in the theorem below, `T < 51/25`. Together with J55's `T < 203/100` for `b,c,d<a`, this proves `T < 51/25` for the entire positive-endpoint, positive-octant root-only class with `a>b>0` and genuine protected `ABC/ABD`.

The new ingredient is a **same-body root-and-section moment constraint**. At the smaller remaining endpoint height, the actual section area and upper-cap volume are determined by the same original C-fan data that determine `E`. A root-area inequality alone is insufficient; an exact nonbody control below demonstrates that failure. Adding the actual-section constraint permits an exact six-variable exclusion. No endpoint, frame, root-edge, or full joint stationarity is assumed.

The starting parent is literal `minimum-0170`, SHA-256 `a9c5e679db7f7205a17ee83ce9b8196b26960822b4fe5e8e9089082458a5e279`. Its actual four-corner reduction supplies a bounded polygonal successor for a general convex root, without changing `V,E`, and without decreasing `N`. The present work resolves its remaining value problem, rather than repeating its horizon repair. :contentReference[oaicite:0]{index=0}

## 1. Theorem, actual integrals, and inherited inputs

Normalize `a=1`. Let

```text
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
T0=conv(A,B,C,D),
0<b<1, c>0, d>0, max(c,d)>=1,
ell=1+(d-1)x+(c-1)y+(b-1)z,
n=(1+b+c)x+(1+b+d)y.
```

Let `F` be a compact convex positive-area subset of `{ell=0,x>0,y>0,z>=0}`, and set `P=conv(T0,F)`. Then

```text
V=int_P 1, J=int_P (x,y,z), E=int_P ell, N=int_P n,
g=J/V, t=6V, T=N/(6VE)
```

satisfy **`T<51/25`**. The coordinate faces are exactly the genuine maximal triangles `ABC` and `ABD`. There is no restriction on the number of root vertices, the shape of the root, the endpoint ratio `max(c,d)/a`, or the original containing-triangle horizon regime.

All moments are original uniform-volume moments. If the parent successor is used, its own `J` and `g` are recomputed; neither is assumed preserved. For an actual tetrahedral fan, the formulas used are

```text
v_cell=abs(det(p1-p0,p2-p0,p3-p0))/6,
V=sum v_cell,
J=sum (v_cell/4)(p0+p1+p2+p3),
E=V+(d-1)Jx+(c-1)Jy+(b-1)Jz,
N=(1+b+c)Jx+(1+b+d)Jy.
```

The proof uses precisely the following **previously accepted actual-body bounds**, with their stated scope in the supplied working memory. These are inherited analytic inputs, not newly rerun older certificates:

* A genuine `T>=51/25` body has `1<t<45/7`. :contentReference[oaicite:1]{index=1}
* After reflecting `x<->y` and `c<->d`, write `c=max(c,d)>=1`. High trace requires `d<3/4` and `c<943(1+b)/1352`. Consequently `b>409/943` and `c<943/676`. These endpoint bounds apply to actual shapes, not only stationary maxima. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}
* With `u=4gx,v=4gy,w=4gz`, the accepted canonical actual-mass inequality is `u+v+w<=t+2`. Also `u,v,w>=1` here: a positive fan from respectively `D,C,B` proves these lower bounds directly because all coordinates are nonnegative. The upper sum bound is the supplied `z0<=t+2-(u+v)` statement. :contentReference[oaicite:4]{index=4}

Thus a putative counterexample lies in the closed overcover

```text
409/943 <= b <= 1,
1 <= c <= 943/676,
0 <= d <= 3/4,
1 <= t <= 45/7,
943(1+b)-1352c >= 0.
```

All new denominators are safely positive: `b>=409/943`, `c>=1`, `1-d>=1/4`, and `c-d>=1/4`. No additional assertion about a full joint maximum is used.

## 2. Five types in one actual C-fan

For a polygonal root, triangulate the genuine maximal faces not containing `C`, and cone them to `C`. Since the tangent cone at `A` is the positive octant, the only non-C facet containing `A` is exactly `ABD`. Its cone is exactly `T0`, with normalized volume `1/t`.

Every other cell belongs to one of four types. Denote their **actual volume fractions** by

```text
rho : C + three root vertices,
p   : C,B + two root vertices,
q   : C,D + two root vertices,
j   : C,B,D + one root vertex.
```

These are sums of actual determinant volumes in this one fan, divided by this body's `V`. In particular

```text
rho+p+q+j=f,  f=1-1/t,
rho>0, p,q,j>=0.
```

The first group is exactly `conv(C,F)`. Put

```text
h=1+b, delta=1-d, k=c-d, l=b-d,
eta=(b-d)p+bj,
E4=4E/V.
```

Averaging the four endpoint heights in every original tetrahedron gives

```text
E4=c+d+h/t-d*rho+eta.                         (2.1)
```

Thus `eta` is not an independently completed ell-moment: it is exactly `E4-c-d-h/t+d*rho` of the actual body. The four-corner root model can be substituted directly into the determinant definitions above. No projective density or artificial refilling occurs.

The ranges subsequently used are

```text
0<=rho<=f,
0<=eta<=b(f-rho)                         when d<=b,
(b-d)(f-rho)<=eta<=b(f-rho)              when b<=d.       (2.2)
```

They follow from the three remaining cell costs `b-d,0,b`. Passing to these ranges is a necessary overcover, not an assertion that arbitrary fractions realize a polytope.

## 3. Root area and the essential actual section

### 3.1. Planar area-moment inequality

For any bounded measurable set in `{y,z>=0}`, with positive area `A` and area centroid `(ybar,zbar)`,

```text
ybar*zbar >= 2A/9.                         (3.1)
```

The lower-left triangle cut out by `py+qz<=s`, with the same area, minimizes the integral of `py+qz`: subtract the integrals over the two differences and use the sign of `py+qz-s`. Its mean is `2s/3` and its area is `s^2/(2pq)`. Choose `p=1/ybar,q=1/zbar`; the mean on the original set is two. Hence `s<=3`, proving (3.1).

### 3.2. Root product from two fans of the same body

Project the actual root to its original `yz` plane. If its area is `A0`, then

```text
Vol(conv(C,F))=c A0/(3 delta)=rho V.
```

A C-fan gives `v-1>=3rho*ybar_F`. A B-fan of the same body gives `w-1>=3(b/c)rho*zbar_F`. Applying (3.1) yields

```text
(v-1)(w-1) >= b delta t rho^3/c^2.            (R)
```

These are two genuine fans, not independently chosen mass completions.

### 3.3. Cut at the actual endpoint height d

Assume `d<=b`. Let

```text
F_d=P intersect {ell=d},
P_+=P intersect {ell>=d},
S=Vol(P_+)/V,
R_d=Vol(conv(C,F_d))/V.
```

Both `C` and `B` belong to `P_+`; at `b=d`, the B-to-section cone has zero volume. If `A_d` is the original `yz` area of `F_d`, then

```text
A_d=3 delta V R_d/(c-d).
```

The C- and B-fans of the actual upper cap, followed by adding the nonnegative lower-cap coordinate moments, give

```text
v-S >= 3R_d*ybar_d,
w-S >= 3(b-d)R_d*zbar_d/(c-d).
```

Consequently

```text
(v-S)(w-S) >= delta t (b-d) R_d^3/(c-d)^2.    (S)
```

Its left and right sides belong to the same original section and cap.

### 3.4. Exact synchronization of S and R_d

Here are all single-cell upper-volume and section-cone fractions at `ell=d`:

```text
T0:     upper=1, section-cone=0.
CFFF:   upper=(1-d/c)^3, section-cone=(1-d/c)^3.
CBFF:   upper=1-3d^2/(bc)+d^3(b+c)/(b^2 c^2),
        section-cone=d(c-d)[2bc-d(b+c)]/(b^2 c^2).
CDFF:   upper=(1-d/c)^2, section-cone=(1-d/c)^2.
CBDF:   upper=1-d^2/(bc), section-cone=d(c-d)/(bc).
```

These follow by integrating actual barycentric coordinates of a uniformly filled tetrahedron. Below the smallest positive height, the lower-volume fractions for `CBFF` and `CBDF` are respectively `3s^2/(bc)-s^3(b+c)/(b^2 c^2)` and `s^3/(bcd)`. The section-cone fraction is `-(c-s)/3` times the derivative of the upper-volume fraction, evaluated at `s=d`. T0 contributes no section area at its minimum height.

The differences between the `CBFF,CBDF` coefficients and the `CDFF` coefficient are proportional to the **same costs `(b-d,b)`** appearing in (2.1). Therefore

```text
L=1-S
 =rho[1-(1-d/c)^3]+(f-rho)[2d/c-(d/c)^2]
  -d(2bc-bd-cd)eta/(b^2 c^2),

R_d=rho(1-d/c)^3+(f-rho)(1-d/c)^2
    -(c-d)(bc-bd-cd)eta/(b^2 c^2).             (3.2)
```

In particular `S`, `R_d`, and `E4` are **not independent scalar variables**. All are synchronized by one actual root-only fan and one actual cut. The coefficient of `eta` in `R_d` is allowed either sign; no unjustified monotonicity assumption replaces it.

## 4. Elimination of the actual centroid and exact value certificate

Put `y=v-1>=0`, `z=w-1>=0`, and `W=t+2-u-v-w>=0`. Define

```text
K=delta t-2-b+h/t+d-d*rho+eta,
J_tau=(h+c)t+h+d-K-tau t E4,
Z=J_tau/(1+c+d),   tau=51/25.
```

The exact affine mean and numerator identities are

```text
K=k y+l z+delta W,
(h+c)u+(h+d)v
 =(h+c)t+h+d-K-(1+c+d)z-(b+c+d)W.             (4.1)
```

Hence `T>=tau` forces `J_tau>=0`, `0<=z<=Z`, and `k y+l z<=K`.

Set

```text
A=k b delta t rho^3/c^2,
B=delta t l R_d^3,
M0=K-2lZ,
M1=K+(k-l)L-2lZ,
F0=KZ-lZ^2-A,
F1=k(K-lZ+kL)(Z+L)-B.
```

For `d<=b`, the following are necessary:

```text
K>=0,
KZ-A>=0,
K^2-4lA>=0,
k[(K+kL)L+(K+(k-l)L)Z]-B>=0.                 (4.2)
```

Additionally, `M0>=0` implies `F0>=0`, and `M1>=0` implies `F1>=0`. To see this, (R) requires `Kz-lz^2>=A`; (S) requires `k(K-lz+kL)(z+L)>=B`. The two derivative tests certify that their maxima on `[0,Z]` occur at `Z`. The coarse bounds in (4.2) drop the negative quadratic term. Their remaining linear coefficients are nonnegative because `K,L>=0` and `k-l=c-b>=0`. The discriminant bound remains valid at `l=0`, where it becomes `K^2>=0`.

When `d<=1/4` and `M0>=0`, one may also use

```text
F0 + (1/2)(1-4d)(1-rho)^2 F1 >= 0.            (4.3)
```

Indeed `M1>=M0` and this multiplier is nonnegative.

For `b<=d`, only the root inequality is needed. Here `l<=0`, and the required conditions are

```text
K-lZ>=0,  F0>=0.                            (4.4)
```

**K need not be nonnegative on actual high-d bodies; the proof does not impose it.** The first inequality follows from `k y+l z<=K` and `z<=Z`. The polynomial `Kz-lz^2` is convex, with endpoint values zero and `KZ-lZ^2`. Since (R) forces it to reach the strictly positive `A`, its maximum must be the second endpoint. This proves `F0>=0` even when `K<0`.

### Whole-domain exact verification

The C++ unit certifies that these necessary conditions cannot hold anywhere in the complete closed endpoint overcover. Two additional coordinates `R,q0` range over `[0,1]` and generate

```text
rho=f R,
eta=b(f-rho)q0                         for d<=b,
eta=(f-rho)[b-d+d q0]                 for b<=d.
```

Every actual choice is covered, including `rho=f` and vanishing cell groups. The high-d branch uses `b<=3/4,d>=409/943`; the low-d branch uses the full b interval. The sector inequality and `943(1+b)-1352c>=0` remain interval-certified guards, not sampled feasibility tests.

**No floating-point arithmetic is used in the certificate.** Intervals have integer endpoints divided by `2^40`. Products and divisions are rounded outward by exact signed-integer floor and ceiling. Checked `__int128` operations throw on overflow or unsafe magnitude. Rational initial boundaries are enclosed outward. Interval automatic differentiation gives a mean-value enclosure, intersected with the direct interval enclosure. A box is discarded only when the upper bound of a necessary nonnegative expression is strictly negative, with every required derivative condition certified on the whole box. Otherwise it is bisected into two closed children.

Completed outputs:

```text
sector b<=d nodes 12879 leaves 6440 pending 0 depth 25 margin 10769585/1099511627776 tags 0 2506 1489 146 469 1830 0 0 0 0 0
HIGH_ENDPOINT_ORIGINAL_MOMENT_THRESHOLD_EXACT_PASS

sector d<=b nodes 162671 leaves 81336 pending 0 depth 49 margin 85/1099511627776 tags 0 15637 4252 125 91 23370 7815 1467 25 28154 400
HIGH_ENDPOINT_ORIGINAL_MOMENT_THRESHOLD_EXACT_PASS
```

The stack empties in both runs: **87,776 closed leaves and 175,550 nodes** in total. These are proof cells, not counts of polytopes or incidence domains. The printed margins are certificate-expression margins, not claimed uniform improvements of the trace constant.

This contradicts `T>=51/25`. For a nonpolygonal root, first apply the accepted actual four-corner successor; it retains the endpoint sector and proper protected triangles, and its trace is at least the original trace. This completes the theorem.

## 5. Exact controls and useful failed methods

The standalone rational auditor reconstructs six original bodies, their maximal facets and true edges, original `V,J,E,N`, actual centroids, C-fan type fractions, and actual `ell=d` caps and sections. Two different positive interior fans agree on `V,J`; the independent C-fan agrees as well. Sections are recovered from actual segment intersections and a planar hull; upper caps are independently rehulled and integrated.

All inputs use the original root-plane recipe

```text
Root(y,z)=((1+(c-1)y-(1-b)z)/(1-d), y, z).
```

The first four use the complete cyclic `yz` list

```text
(1/10,1/10), (6/5,1/10), (7/5,1/2), (2/5,7/5), (1/10,1).
```

Their `(b,c,d)` triples are `(4/5,1,1/8)`, `(3/5,6/5,1/5)`, `(1/2,5/4,2/3)`, and `(1/2,6/5,1/2)`. The `root_on_z_zero` control uses `(4/5,1,1/8)` and

```text
(1/10,0), (6/5,0), (6/5,1), (1/10,1).
```

They retain the walls `c=a`, `b=d`, `b<d`, and a root edge in `z=0`. Their f-vectors and exact traces, including the sixth fixture described next, are

```text
c_equals_a:          (9,19,12), T=14145260535/12372191264,
strict_high_endpoint:(9,19,12), T=2784721/2661054,
b_below_d:           (9,19,12), T=37040645/42492632,
b_equals_d:          (9,18,11), T=175925535/185775436,
negative_K_high_d:   (8,17,11), T=68092930/80097601,
root_on_z_zero:      (8,15,9),  T=98902685/89408796.
```

These are nonwinning controls, not attainers. Their equilibrium censuses were not computed; no `110` or `weak000` claim is made.

### Actual countercontrol to an unconditional K>=0 shortcut

The sixth fixture has `(b,c,d)=(1/2,1,2/3)` and the same root recipe, with

```text
(1/100,9/5), (1/50,9/5), (1/50,19/10), (1/100,19/10).
```

It is a genuine proper root-only body inside the displayed endpoint and volume overcover, with

```text
V=2287/6000, E=35023/144000, N=6809293/14400000,
J=(101779/960000,460397/4800000,98507/480000),
g=(101779/365920,460397/1829600,98507/182960),
K=-423877/2287000<0.
```

Its trace is below the target. It refutes only an **unconditional** high-d `K>=0` reduction, not the target inequality or a separately proved high-trace condition. The accepted high-d certificate uses `K-lZ>=0` and the convex-quadratic argument instead. Its f-vector is `8/17/11`, not the mechanical `10/17/9` layer.

### Exact nonbody control: root products alone are insufficient

The following is explicitly **not a convex-body construction**:

```text
b=99/100, c=1, d=1/20, t=6,
rho=1/4, p=0, q=7/12, j=0, eta=0,
u=19654/7125, v=120029/28500, w=103/100,
E4=1643/1200, formal T=50518/24645 > 51/25.
```

It satisfies the endpoint overcover, the actual-mean linear constraints, the five-type nonnegative mass identities, (R), the other listed C-fan/two-fan root product tests, the B/D fan ell bounds, and both individual `10/9` trace caps. Its root-product slack is exactly `248503/30400000>0`.

But its synchronized cut data would be

```text
S=29039/32000, R_d=71117/96000,
(v-S)(w-S)-delta t(b-d)R_d^3/(c-d)^2
 =-14069464133694811/7004160000000000 <0.
```

The new actual-section inequality therefore excludes it. It is a countercontrol to an insufficient necessary relaxation, not a counterexample to the value theorem. The recovery preserves every tested inequality.

### Additional original-moment inequality retained

A stronger variant of (S), not needed by the threshold certificate, is also proved and checked. Write `a0=d/c`. The known canonical C and B contributions to the original lower-cap first moments are

```text
Cy=rho(6a0^2-8a0^3+3a0^4)
   +p[4d^3/(bc^2)-2d^4/(bc^3)-d^4/(b^2c^2)]
   +q(3a0^2-2a0^3)+j d^3/(bc^2),
Cz=p[4d^3/(b^2c)-d^4/(b^2c^2)-2d^4/(b^3c)]
   +j d^3/(b^2c).
```

Integrating in each original C-fan cell gives `4J_lower,y/V>=Cy` and `4J_lower,z/V>=Cz`; the remaining root-coordinate contributions are nonnegative. Hence

```text
(v-S-Cy)(w-S-Cz) >= delta t(b-d)R_d^3/(c-d)^2.
```

This retains more actual lower-cap information, not an independently adjustable correction.

## 6. Applicability boundaries and scientific effect

The new proof requires the genuine root-only representation, positive endpoint values, positive root area, and `z>=0`. Proper `ABC/ABD` is used decisively to identify the unique A-containing C-fan cell as `T0`. Extra positive-ell vertices, negative-z material, or enlarged coordinate facets cannot be inserted into the five-type formulas without a new argument.

The residual chart has no inverse-horizon singularity and no division by `1-b`, `b-d`, or `c-b`. The walls `c=a` and `b=d` are included. The algebraic closure includes `b=1`, `d=0`, `t=1`, and zero type fractions; these are certificate boundary parameters, not claims that every such point is a proper positive-area root body. The actual positive-area root supplies `rho>0` where needed in the high-d convex-quadratic argument. Endpoint regimes outside the finite overcover are closed by the inherited actual endpoint and volume theorems, not by truncating the search.

For a marked-closure body with `F` touching a coordinate plane, contracting `F` toward a point of it with positive x and y gives proper approximants. Original moments converge, so the proper theorem gives the conservative extension **`T<=51/25`** in that closure. Strictness there is not claimed by this limit argument, and enlarged coordinate faces must not be called maximal triangles.

J55 and this complement now cover all positive-endpoint positive-octant root-only bodies with `a>b`. J55's stronger `203/100` constant has not been transferred to the high-endpoint sector. :contentReference[oaicite:5]{index=5}

The sharp high-endpoint supremum remains undetermined. The most useful continuation is the negative-z root-only sector: investigate the same actual-cut synchronization, but replace or translate the quadrant area-product argument while retaining every resulting offset moment. No full endpoint reaction may be imposed merely to reuse this proof. No E17/FULL/LOCAL registry change or whole mechanical exclusion is asserted without an exact incidence bridge.

## 7. Recovery and verification

The capsule reconstructs all three complete source units, with no parent code, archive, external input, or random seed:

```text
high_value_exact.cpp       6104 bytes
SHA256 7c689e89c70c7dc2e14a1cd6fb0f1c42ea829b94644d19b88fefa893caf18c14
high_value_controls.py     7703 bytes
SHA256 5f3fb58b5ab89f0ee9e9e8a4ff39f5ac75b10b0dba2a3cbfc0fb80b696d79cfa
high_value_identities.py   1731 bytes
SHA256 8461b09e9622ffa782163f8c1a513fc27834a513d60b9539969fae2041375125
```

Executed environment: CPython 3.13.5; GCC `g++ (Debian 14.2.0-19) 14.2.0`; C++17 with checked `__int128`; SymPy 1.14.0 for the separate symbolic identity audit. The main certificate and body auditor do not use SymPy, NumPy, SciPy, or floating-point arithmetic. The certificate fixes `PREC=40` and a deterministic limit of 2,000,000 nodes per sector; both sectors terminate well before it.

Save the capsule as `recover_high_endpoint.py`, then run:

```sh
python -S recover_high_endpoint.py high_endpoint_recovered
cd high_endpoint_recovered
g++ -O3 -std=c++17 high_value_exact.cpp -o high_value_exact
./high_value_exact high > high.txt
./high_value_exact low > low.txt
python -S high_value_controls.py build controls.json > controls.txt
python -S high_value_controls.py check controls.json > check.txt
python high_value_identities.py > identities.txt
cmp controls.txt check.txt
```

Expected output pins:

```text
high.txt:       176 bytes, SHA256 9997e802cfe104fea023e088248087b0edc68922ae590162a9d96a3457da9772
low.txt:        186 bytes, SHA256 b4032402dac375d1dac5e3a981626fbf86f7403b67621c178b2998b4f7c1e5a8
controls.json:7706 bytes, SHA256 8494098bc8a51da43fba326feeb463f981c5936f5bb35a027d8adf4f58173500
controls.txt:  781 bytes, SHA256 46c62c881379aa63e6b9d5b291d07f63ce4a24f20aa19971be5ff25491a48a35
identities.txt: 52 bytes, SHA256 4f445f0a23dc0278a1acb5e8a2aedef59028c5f7d654093f81126a214384e0d9
```

The additional terminal markers are `HIGH_ENDPOINT_ORIGINAL_BODY_SECTION_AUDIT_PASS` and `HIGH_ENDPOINT_FAN_SECTION_AND_TRACE_IDENTITIES_PASS`. Normal execution, clean source-only recovery, and a C++ run with undefined-behavior sanitization were completed; reports match byte-for-byte. The analytic geometric argument is not a proof-assistant formalization. The old global endpoint/mass proofs remain inherited at the explicitly stated evidence tier.

Convenience files: [recovery capsule](sandbox:/mnt/data/recover_high_endpoint.py), [integer certificate source](sandbox:/mnt/data/high_value_exact.cpp), [rational body audit](sandbox:/mnt/data/high_value_controls.json). The complete inline capsule is the durable recovery source.

```python
# Recover all sources for POSITIVE_OCTANT_HIGH_ENDPOINT_TRACE_51_OVER_25_V1.
# CPython standard library; no external inputs or parent source import.
import base64,hashlib,json,sys,zlib
from pathlib import Path
DATA = """
c-p-?ZCBe!uYbkMo@e8iaT13>OPpa31-c7#X-nE}FCoXru^nP?Y-
2ki3FW_ENi$9ypgg@_?w)NtqmeWkjik}M@US%wugA{Jji!O)C2^4@QC?3MTb-
@nmA_B^`rA1^Kl=3X<ot_s@$usq=i~W@|8c%t92_1yJC@VhalTm{CCS3;Fm@v)bBi#+!Z7g{%8K1p{JV1aX;F-
mSlO;y+w~nKFWlI7Ghd0qVdiEFC5fYjt+-
L7gmF48a%d=m3|R$Hat|y<Su#;Znd@N}xe`v&BrBBn5}>%b@?Ih#VUa+`C6bp+h9DmiN}SX!#?W<%@d>I|v8;^U9NXAUp2RF)0Lc
MY->XfHt$sB7-6qHa(BTSXl~_jzvNi}056*f2fW2df>}YTm`@u+YeP4CiQ0rttG0kG7n5I#n&W(jKN-
|~67N8Sl8K#7!37UL5e2K<<jb<{9)PlKBXbOEUXpq8{sD4sxu+OIxRh{cEa~C5MgkF~9`39-
#_N{?F?6(G{3qMe@227Tk2y2Q~CQBB=EYVs@6Oc5_TQL>#iOvu%5y29J_$jWs>POR6ujH?p>Z&h-mpFpccp615HPt#-
v6Au}>>}{h9OOu`FC`o)Q4m9=%dN7X6yQYaMkDo(D3y%&2l!nn_>REJ{Wy#QVv%Y4mIBUD%AWO2&;|U0mgc~|*~#i@lBycfWpy`A
gV<N+RF^$xP?kmNJk|Ogpf^ON-@%FiNrTG**BOObUdR!;9H-
E};r*4RqS#L+J7sC#>I@9v2>fUuKA+>PEl`tloV5j1ZP(y_qg9SOMEcB)uLHHEb#D6M0Gf4mj)evMXpLPIA<w~W6?eb69*oO`iQZ
HuWxEtv;EP${9KUjU?2+pQIe&PRBM8|IyG0qQaX=LU3382Xi{Zpvm=t<f+P@jVfI&Vcs<*OAng;`j6A(9EsIk_;P#4D209(c!jWZ
UwHbmB(_XT9Gnd7x3qyx!k62>Z`Y29Xb;?6~RgC!!B4g1Yb%+Zrgi^ZBf=H^&-
VpjYZA%edTEuqxI44Z;@I)TVq1cDzjpK%Ve=4VODu^*wDZH?Uq3m&<Xq3<eT#~tQsOyjrRd9dcXp51L?7XHSO6ZM{E3D}gFMAQeU
l!$I9)&Li6%>yJI*xmy8`gtD-
>mf|~96U+T+#!;5OK8<f^`UO7v*w{O;#7HPi>uj#TB{1yKzrS0$6M61U>0O~AUy1r14ML;^WrUFxFD1m0+8N<{llkoJCJrJM<*i$
;tzlYnjTqUUm)FzF_0NbRBF%$cHm!cTC2C%oF;+TDcuQzTj`MAg5hYTNa&NqtPYL<?&40PLfw!~glmoU2U;0NLL4=WzsSoV_ux`D
LJI0zbW0wzc!b%Po*G5uJ~QyX7NH39A_*v=$W`){il<UXnu$fi(+n(%0Roq`=M#uYi3BPm;;UGMf{_c3%LH0N%K0W@*r{BFHGSLm
f(RX>3}uxebzTTg7DHiR22D$7o18}_dqF*i;@1E@+YlAmlK0b%iA4)0x>*u&T(i*f<{%!K;G!%np&(+OQtAc>_IXqEIl`LgU-
@QmsKA&oML1>X_E2xM8Kn&HFM*&!6%YqzRue-mCszfD7!c4jNX>p@r;LzFO-
=$gpJt$D5m$vuN##Q0yo|cG8&{NhA3)*=c^Zsc?PHQN&_yt1Py;1tPt_|!tz0+~=~9?j-
0SmFkN0d|8n^6#0ZoIjL|t3!yNo*IxFB3P>`mL~cUpsr83G>6C+GOZ^{~{7E*jXg@t1n?T!;~|I|(qkU_M(cX(UvEu$ijwnMxIy1
wY`H=_B(bDR^I1EkpIdtn`JcTINvGms-OQ(1yftps<c^z<5xR7u;;V-=q{_A-_v7mU3|xl-
Q3(sS4zm2G(qt<1%=s9q8Z3{!<vD6b06DC=Nxjg+0dcngApo8eU0&6<?5C2@`s5CKWrfkNG#*;pw`=({+cZ(4l?K<5)e_?1Jy=-
_`?usH`i*8C`-
F51h8<Bj*oIX0g`euaH<(lI_P$wFanKZKX?Elr>WDx|LU3OD)elcH;>z;#FfiTm?s!P=HzmWg*D~8bo$A(09sEFT9fiEAr~d6|E_
QNk=lnyauY;Y8W=8kKR}Wj35FEOHz>V+a<ZcYCpr04Xstf6N+uokO#7EVI2q1r}}_`QUj-K2tL6w_Lcq1PB>ze<HrWhtwuo-
q5EPhj6meN8D)7v;c~DCFs!e}P(QJc+q|tGH@-
nq0|vLAD}Zy)@Qrb!Fnv8UfDRioc9Zc+Dl5FFKgR`ebIvGd5xg?}8!*$|tf6k}et=UmWixh9DOJ0HvsI$v`cG|OB0}t`F*EMFyf9
F8*KXS6>I}_Uy@y|O2>kRy&vbpe;puv-<b#MJx}R~xFk9vj$71;9XzV<4y<6mKPR*HlzaIJ-SdfPrqK*uqE$YqyRz$W&R>$bEQv<
$$1xcL%6b97IGl)EfXO!fy`w_L0M;74bm;0etP?X~o>L8q^Nf?8B!}2Ji8<PNG^aXmrDim-
L5Jt`{@QNhk>Uz;<>qVcf7k!P<$_;Agr|g<0!J<iE$NZR`^K<rvpEpzp5c;vk4ju3|XLSfb7RS(v;2*<@b{0zqEdtD9RVU-
%HxdA;qd)Zu2PTE%#IQ4d#=IoSeB2oX4w$MVW`lm^UeE9HA$jNT%0Uz<sT+d##s#L0@;m~1g}qlciGn;AO(A9+U^Sr+d~;hV#(~m
0q8JYz9RXoZup*lVisVzrKD;R`8I@c<MG4Ai<gd4rVq><ksYzK&rY<fExS%n8h6PA#{4&9C^#D`fX;H42m_f`by>J_<YX)V;GRK?
(sib@@{<4z+D@ckY60LWp|4S=g$(Kgu&e+YY>d|E@q%|;IQ3xQk&pICAz}_TRf1;*+P?I5vh5WOW-GITSEJ#_HuGcEytJyt1OCjo
9_|n(hnFtR0H=-
TES`LxS{?O!^4uiqLHNda*ZE(nunSn>Obby$u0Jn(h1OLzj|AwZa?qO^&Jso(1r8d+d!gP=DE<88#1Y^myWLg4RrVIhEGm=4|2Qk
+CK;a4o#ECsNgRxr}u6h&zdSDG0tVBS$@G)kIUN+*EC9_f&_VdK$aDk%k>aOmZZ{ZiD-NsK_GrsC-TNjLkP-
Y9OZBYefnPp8hYsSC2x=ox~#7Q$wHt4CpCEwsXM82DRD&6SY#P?(ay`r18u3{2m-
e4l5HNNfh!v$%I8d}uQk_}5T`yxx?Yf_texDc8%50|efuhN?!mKqe{wLVQT8kC0Z$WSV)46M=l2F6H*Qw|o}<2?q`c;T}Z$z}k9O
-phgWR4qq<0Nw?$t0j?eYjvCClfL_B{32SP-RCTL|bjFl5FBe<yo-
0&T&}*EBz8SS$liTYOc>YAr+&_uBf!}vrQO4Nh`Sxn`+ayBM$nKsWGngl_lMNX=McR1y|3^2xG^sJ>`YDFqifWST5{)_+8pxxcX$
#(;8}_AGfjZA+8MQxYzDv0wps8Pv3Mja_miKGmrvQ-oqx~l0-i5Pfd%#0?c6LWUE!0sZ*0!%hg#1x-
tX6m2H(Cpe)jAWNU@EY!(5tN{>SUmoH4q1PwB(`cxg7z~YtUgL<D*JIUtjo6;eQY`+)nLw&P<_(3Kxr%kqpVCY*an>_`h=4l5J+&
_;ok#vz;;U1Oj3Uo{9H@e`L{rBn)*wT*3z=2b@auP^sNnW_cH0QPRkLT|`9{o>8nT1J&iz}_8kQ7Yas9aHCMF{So9u|ul8*;E<j{
7vwAqP9=khAh8`<F`tfb6x&rW~?8j=A7H1M@s?L+<f~fsE)jIfp{U9YH?wCirTr9by!~W?)V(g9l-
G7~?&M7r@&3etnc)Wa9MpDGH8ph4paT5$tAi!z&K&=Jl`$Cb_CTzQ8~n_Ap#0wH2fO1{=YovhAI(jsaYlkm|{*<M_dFdhIwgA9TL
DfGu`*jR!v4BCnSKh^BN7P#aFe$gi=QHx9hp8V+)?gmeJof+Zpbel-
S=UAD6ccvAveqTUj91XF#*LZj_5ZpUFqMZ5Bv=g?&5j#~qaHd0!|>#c_SbSAJs^PpmfZoJCGwnov4dRj@eBZy=tFe-
;Gp&Y*^<%7?T2y`vBUF~65%27q#T@P%NZya1h-
Zl%IGa*xz$XanP)klNhTWe$IWq`G}(&&mx!UmPTDH(<pVd*S`EP1ZA>ZEPX*pvBtJ~`FX3!0^Vd(f|))du9yu>QGR*d#f%m`D0$n
`;k$x)i}KE^{Hk;Kf|spH9+TMQ(IV=wLp`zd$YxD`o0tE^I$w83bEowN4F^g4)$pT+`}7>?MAnYBt^ga=iCjnRQ>B6M<J%?3#0F)
Ey+K-)G=|&Ts)iM+I3BpEk;JxP$}wt1nT&Qvj>HNuf*`2ii$9Fg<nNui+-
EHej_;jp<M=H%<upQey!5LapVF2eA4WKU{5nCJRVU_C>V;4McQOMoS0yp|+rt4Yk$=vXkEN;g^$-
=gwaTpMH)h!(Of0!Nu{Xj~Bq5ZnHoqOkSYY^Re67*(F$g9L)U?Hh+aU6PBc#H_RU|PX0PMKltE~yrnz`Uyn|{IG+xBJq#!?JC1`|
a~zl&$HB1WIJJ%lUsv%KtKMh_b5Kd$OVh2+R-^ID7urNdySVE>ZuEd3-
ex2t*rEZaPq0gg3$XHQ=i6d=pDw4jpWmgo=JMuqF}*$=M!^kJdVe3l_zB<L^LB#WH+%l@&FD?5x#L=Ig5d487wiq+T6??0*6!YJ^
KGj&Y>$GS;BBzid<*}#+B<LEouKt*PxSgxUbMry8t1UGDTgLZykaQDeWK)`6q7FApDlqQ?my!MZ{6vF9*lS)I35~?^+rjfX|DWrc
-T0M-
1u6d=pFc=Xc)THdaEG8coGz$S69vxWfUdA2M{TO!WyJZ^T5Yz{xJ5UsUIj^H@Z%UXnzBmW$t1F;^hTwyo(K3n1G1~?j|YV1#>S*i
ziU9qw5Wja3BCpa}*IxB~M)sw%CPlm(WXIj?F0m2nL=P!91n8R?hh@Q$AfBAM$o{qwx|pSC<gtx?OCArc1oKU#jq7m&#CkxKunl9
I1|jAp<nzK(mv~f($fvPq)&4!2YBdXUV;iP2(a2GY+yW$<(VYKn-cuO8l!W4VigeZmObJtF^2B_~GsIO8qC?a(5KKl71bB1!x6X$
@Si|A5m`D>c1v8H2<pHazFC_Blaj-3k{tNyS(`mPJTFp+$f2W$E9+|-Nq2oKKDPvlH;AJX5FSH_(J-
$;w#%t=*z_WGQ<#erYv(rqpn>JT}#xft>)F1Jxr1a($;J4cAKaHC~7V@U0V|8HeLEd?0(4W=`<fZL)W`iy|J6AwPww5|AT9^?KZg
8v>zpdDrU{Bp+3ZAWnLc!*BJ6xUdIz0ZKbMQ49Q&zS<9>RZu3vm?YMF@IAbR;?-
3i@Cn{RK3*+fTDj9~$da$gI)ku4IR8Cf^fo2!MLiz6g@F%(tCTX!)g-
x7+$4Bs%6D3IlT9^&>1X!L_wEaMi<kllLtVeXCg|#u%#@Zvwye2kZAvO_zO>H8xm&n(oCgB0?6EuC@%cYX`2mC>3rj)Q!8?S2Pjk
Z$yvMVqs9d<oV5CynN$LACVB#}Kx9s_7`=g(W72-R2%h1Oq>es2G95~m5Q5s+T47cf{hk_jFbCYkUHH{z>-
fE@0auVn9Gdz9eFL2y?NyDW}HalD4g(Xw%fBru|qq%4j_alD2;RnUfZqJ%{WYGFe&;}ALk=wro>j~-
5xnN4d;_k^AAU)x7(i=LssJt{{u>#~N%cvLaQBT(uQD)mT#)T%x+hV_|dL-IpxLJscSJ-
0){(6ah<KOAtEK7fXwQv3`>I;z;&Q?}->u{HlYTfq{n_H}-
y`x+<xnSlDQ35aNhK!1gO;~D$Le`Bvo1!ODU8q#cZ0K4B5_xxQif}C6VzW-gx@6_+rNT<6$LG*@C5d|vbL8}uk*cPo`8A8esdbbS
H!6I|bG2K6#9%Lt?LFQ!B0^ciklvAdhDJo>;XJ&M%0hQcgD!G>hLCh#EOERWRk~nEH<$aS8gM)wm`bPjQ0Kz|T-
EwDGJ>6$eaUt|0;i_oWUl^%yh40L2?bC7IG;-
AvcD_Gnv{J!Rtvx^{{#_Z;8!qN?e89!<MOSOU3ixafm^}N2rE>)PllH(S3Odzeeh}eN9;4GeMyGo$Uvj!-
5_q4vJj#a7{u}~>ok1rud@5)H<#^*}?=!=L!06c>*=K=VxKsXJ-LbUBceS-
6Ih^7hq6$rPn1y#*22^w)Gx7TwFTm7oENh0^qOU$Qi8r7~&X@eOkuTW+zt!<14J6RPS~9Hx#^pgohuPt0W=oIsOF{6y$<OplGtvR
!QZo-2P9ulPnP#>D?LeS?5C@LHOB^shxiJ8Ig1&H3@VTKv>rm540y)+TANZ}9NnU^;>M!0CyvT>FjpMJO-
kOo7e~_cH#DVLjajSm-PL~G!-kL%o5%zrHOBQIE34h--zN=zB=n%DyU6Mc`*n7)fA2dCj;z{+NXC30t_S)MzJ}b~nYkQ}qd(;?p%
!qW&z{bfhgj;}DP<ISfe!y;ZRXr0DelVaUhoI?~+7nSR(yteacgg%g_`xOk0j56ao_>(ph$oRQ9uQc#*RcFe+zfIodrcEgU@K7&`
h^m}lB&|~06G8h#IFR=5fHhRwP{jeHVMg1UJ8g0F2+MxwA6V$!iPum`dB`_gO7-
oC!lv5cwkvz8LB`tMOACG?1{h>XiR)4qgC8#0XsRqiVrvez@DI!6?h`SasUufW>uMQK;|1r=<OR68t*wylqDZc`Zt3Y1O1XOjS)1
8b>!Lb%%_r)ttm60z(Kfkm567Mtt=_gf&^GX#sC=${Ksbkwn;unnUGU`++Ahv4>yLzOaWygF;D<a{S8L_<HrmFUL7B1X@C4NgOIg
Bxr1~&n{+^hn7f;pyNJ2_BIX;xAB%4{iQXX5+ZT!2B@t?^HR$qQqmA&rO%897!`_P=tmY=_9-
<QP1zc+r*J={7RYAT`l4<eqXv1$^xD2N^twKFw7&J3@;4n@SSh!pzPoof*+GIkf_xZ$)q5zjx&y50KnWm6OK<vmvA5Zo1v^gwt<v
MeHd?t+-<v73Mfy&P7S`~t50{89zL7C4-
A(`y`%yCf#B1oX)Q8JBY3!AZ#d^|&@PkWrFFyPKM9k>!cfw72X*drZwQHq;gdklAwx=si44`OTx-
rxT5Llmq({t#PGRi0^TzwxUr+N!_Ug6C(jJ^0x<MRq-<JH`%%x*v$F^y9=2oG6@x#Q--Jc=;w{Ax9Cqtsg(0bi_*$>?sUnx9t=P(
G&iD>(9JMrctDp=dztvlm0{25Nz=zD=QvwXVPx&={;OdV86tg^so8I9(uULz(uCVcHiu33<`}l!rD6kdV|QlN5GWU@Ee6~;tDg+9
B{(71t0<m_(oS0LB&Z^7sS~w5<d~tkL&TEQgYs8QQ*$7Afss6&Ma#mmYEzJM=nFf7?8?UhnI&XG-
h#h@Ei71r|q>0F^M|plG?Nf)XJO_0-
Y9UHkH#Pb!45;4Z{{ap;=N1Y!1Gf4GS8lC2cNZzIcqL26Yfpdk}*FY81IozyZ`M?k<WfkRd>`%NOjVEb>-
&9_HM%V2rt!WC0fCYnJCLAauRq3|($%D~`Z`2Wv;e<Cc7%c)}zS>)fW!Li_Pi4g~AnpKX_WU%nomNz)|*OZlAL@i|UM=+pX&^m2)
%qPYU%LYtOgepiAyF7PQT7hw2HiZ;ZU#pJBccG7aXR*<{ZTIPZ8ce__xV*j9AZFRepP+x7~v!tu7&ehhi%YBd@v4q(Xmaq?miP<B
dC=wK({@}?Jf~ogBTn4J(LZ(42R3ey|SOP9{Ip2ickf5HRMH2zX#%ZN|!tEeLE5|_$T)V7ZUB!Sb-LPulkOd+2rcu9SD<!AC6hlT
&1hExpT!IEqq=n8mMUfG=WmlE|lbecvKK^qI^)G*49QXeI_~FPo{(f*MZY#=hJwCmZ2z>~jbSPi`q22p14vRouJGjwxFwDdw{9n7
Uc;OH1Y^ArDd|D`0-
D=mHbZQT~*dW6{&J%xNS6}_TTfUg23;YAR{3<S=uGAd|&l&N}2;Q>@HnppG{St)Ud@_0;367H2fy*$7a<w*8JjGWEB~!jC|3W@ER
c6Y)a)*~U;x&kT0aASwf-f~9@e1@RK7Rh#b0wCCSKW~c+dSBn0=kNyuf~aH_@ewTl+9zUo==Cl`Y)6B`{q~kM8mhdS8?x<uU~-
Jy>}qXHf$DsdUb?sbl8~S)93XIBfEFBrfC7q5e}dvfvvzh?(4VZ4$c?kRr(8{0E`m9hp$qMOz#~UU-
jNQ<6pgZWSl_h$iCnbe6a!p@l`DMk-bB0^U+H0Nc-
=P%r2UO>zcB6WZu61p6r>%p)d2pD|&rKaA96FU%~%f`74NFErir>3aMTc%z_C2@&S^IT>R1JW?mR4G2T?u`|e<_h|?G_;@&iy@ji
%mC#IC)eBSAIaz5`~n9ntezee#11!lEGxm!I&^YKO--EqY78OvtnUnpSLtlv9iy?3m41iwcEs$NhP=50`YPqEU>NGRow`I?!}gf^
ZbskoWHgS~X!4@V<)#O}1lwpO9cW~CmFF$2KItJP;P>nE*dKAkA^m{k#%Ux+0`&1i%ZFbQ0Id3r2Jd0Rf+pUM}UGx=!${wiKS(=t
6n;y-`9yc$a|Pa$zv&(PTD6;f2bHj;0bpO}usfAXZuRDby$v$QQdC(7#=@~@HQvm%hb`IGn8SMh1{^;0B#pY`fF(u-
m0wE0B#CNV4YV=3s8eMs3^S`D8|<wL5Rr5G-+oBS-*m-
qlqUqaR5pvSWm>v;N+f}l$SKF>8Mt>(JPmY^XZ!IP_{_OiN5WDAk0hw?;alkUYk`}YUu>zn%XBe^o29Kou1^5x{Xx4O9Bdi-
C&aK%X
"""
raw=zlib.decompress(base64.b85decode("".join(DATA.split())))
assert len(raw)==15980 and hashlib.sha256(raw).hexdigest()=="ce2722e79a08a8dbd0e37fe66dedff4e84627a7a8b34a23ec62ce76b87ebe7ae"
PINS={'high_value_exact.cpp': [6104, '7c689e89c70c7dc2e14a1cd6fb0f1c42ea829b94644d19b88fefa893caf18c14'], 'high_value_controls.py': [7703, '5f3fb58b5ab89f0ee9e9e8a4ff39f5ac75b10b0dba2a3cbfc0fb80b696d79cfa'], 'high_value_identities.py': [1731, '8461b09e9622ffa782163f8c1a513fc27834a513d60b9539969fae2041375125']}
files=json.loads(raw)
assert set(files)==set(PINS)
out=Path(sys.argv[1] if len(sys.argv)>1 else "high_endpoint_recovered")
out.mkdir(parents=True,exist_ok=True)
for name in sorted(files):
 data=files[name].encode()
 assert [len(data),hashlib.sha256(data).hexdigest()]==PINS[name]
 (out/name).write_bytes(data)
 print(name,*PINS[name])
print("HIGH_ENDPOINT_ALL_SOURCE_BYTES_RECOVERED")
```
