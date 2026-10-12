# minimum-0179

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# EQUAL_ENDPOINT_SINGLE_B_FAN_NEGATIVE_APPENDAGE_V1

## Determination

The requested comparison is proved on a complete geometric class, not a bounded depth or endpoint collar:

> Let `a>b>0` and `c=d=q` with `0<q<a`. Let `P=conv(T0,F)` be proper root-only, with exactly one negative-z root vertex. Suppose its root-clipped body `Q=conv(T0,F intersect {z>=0})` has only the root and its z=0 base as maximal facets not containing B. Then
>
> `T(P)<max(2,T(Q))`.

The root can have arbitrarily many vertices; the proof uses its actual area and first height moment, not a trapezoid assumption. It also applies to curved roots with the corresponding actual two-piece B-fan decomposition. All admissible positive slopes, including the parent's previously unresolved positive-slope sector, are covered in this class.

More specifically, **`T(Q)>=2` forces the parent's `C1>=0` in this class**. Therefore `b_tau>0` for `tau=T(Q)>2`: an actual negative appendage cannot increase a trace already above two. When `C1<0`, the whole admissible depth family remains strictly below two, even when the unconstrained depth polynomial has positive discriminant.

Using the accepted positive single-B-fan bound gives the stronger value corollary **`T(P)<Cstar<2.029`**. Independently, J55 gives `T(P)<203/100`. The positive single-B-fan bound and Cstar are inherited inputs at the supplied notebook's evidence tier, not newly recomputed sharp constants.

The arbitrary unequal-endpoint class and equal-endpoint clipped bodies with additional non-B, nonroot facets remain open under this comparison. A new exact above-two control realizes that latter distinction. No actual counterexample to `T(P)<=max(2,T(Q))` is claimed.

The geometric starting point is literal `minimum-0177`, SHA-256 `dbe60e47a944154d8a3acc376b60f1a45bad6b2a6feae1779c20e7ac3d49e376`, including its actual paired wedge and retained root-cut endpoints.

## 1. Exact hypotheses and original integrals

Normalize `a=1`. Throughout the new theorem,

```text
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
T0=conv(A,B,C,D),
0<b<1, 0<q<1, c=d=q,
alpha=1-b, delta=1-q, nu=1+b+q,
ell=1-delta(x+y)-alpha z, n=nu(x+y).
```

The compact convex root F has positive area, lies in `ell=0,x>0,y>0`, and has exactly one negative-z extreme point p. Thus `ABC/ABD` are genuine maximal triangles. Put `Fplus=F intersect {z>=0}` and `Q=conv(T0,Fplus)`. Initially assume Fplus has positive area; the zero-area boundary is treated below.

All bodies use their own original uniform-volume moments:

```text
V=int 1, J=int (x,y,z), E=int ell, N=int n,
g=J/V, T=N/(6VE).
```

No projective refilling, freely completed centroid, or endpoint/frame stationarity is used. Changes in J and g are retained.

The additional **single-B-fan hypothesis is imposed on the actual clipped Q**, not on the original P. For polytopes it means that every maximal facet of Q not containing B is either Fplus or `K0=Q intersect {z=0}`. Equivalently, its actual positive B-fan consists of exactly the two regions

```text
Q=conv(B,K0) union conv(B,Fplus),
```

with disjoint interiors. The side facet BCS below may be a quadrilateral or larger polygon; it is not treated as an independently movable triangle.

## 2. Genuine root support, paired wedge, and admissible depth

Write the root cut as `[R,S]`, where

```text
R=(1/delta-r,r,0), S=(1/delta-s,s,0),
0<r<s<1/delta, L=s-r,
K0=conv(A,D,R,S,C).
```

Let `h=-p_z>0`. The B-projection `pXY/(1+h)` is an actual clipping vertex only when it lies outside K0. If it is inside, the parent's pyramidal-cap erasure already gives the desired comparison with Q.

Otherwise reflect x and y so that the projection lies in the D corner. Define

```text
m=(r-p_y)/h,
w=(alpha/delta+m,-m,-1), p=R+h w,
e=q m+(q-b)r>0,
eta=e/(6delta).
```

Convexity of the original root gives `y>=r+mz` on Fplus. The parent proves that BDR is a **true maximal triangle** and that, up to boundaries,

```text
P minus Q = conv(p,K0) disjoint-union conv(p,B,D,R).       (2.1)
```

The second piece has volume `h*eta`. Its positive clipping wedge has volume `h*eta/(1+h)` and its negative partner has volume `h^2*eta/(1+h)`. They are two portions of one actual tetrahedron, not adjustable cap masses. These are the literal parent's geometric conclusions.

The new single-B-fan hypothesis supplies the other genuine support plane: the facet along the base edge CS contains B. Its root-plane inequality is

```text
y<=s+mS z,  mS=((b-q)s-b)/q<0.
```

Therefore, with

```text
k=m-mS=[e+b+(q-b)L]/q>0,                                (2.2)
```

the actual root section at height z has y-length at most `L-kz`. In particular its maximum positive height is at most `L/k`. Positivity of k follows from e>0 and `b+(q-b)L>0`; the latter holds throughout `0<L<1/delta`.

For fixed Q and m retain **all of Fplus, including R and S**, and set `P_h=conv(Q,R+h w)`. The root cut remains exactly `[R,S]`: the lower support gives the R inequality, while

```text
y-s-mz <= (mS-m)z <0
```

on every positive-height root point gives the S inequality. The entire admissible depth interval is consequently

```text
0<h<r/m   when m>0;
0<h<infinity when m<=0.
```

The apex x-coordinate increases since `w_x>0`; its y-coordinate supplies the only finite coordinate wall. On an original fixed input, smaller depths are genuine bodies. No cut endpoint is discarded merely because it becomes collinear with an old root edge.

## 3. Original moments reduce to one actual root area and one height moment

Use physical root-plane yz coordinates and let

```text
M0=int_Fplus dy dz,
M1=int_Fplus z dy dz,
G=2M0.
```

Both belong to the same Fplus. The support strip (2.2) proves

```text
0<G<=L^2/k,  M1>=0.                                    (3.1)
```

This is simply integration of the actual section-length bound. It does not require Fplus to fill the containing triangle or have any prescribed lower or upper graph.

Define the following base quantities:

```text
Z=1+qL,
H=1+q+q^2 L,
B0=2-q+q(3-q)L.
```

The actual base has area `AK=Z/(2delta)`, mean ell `H/(3Z)`, and the corresponding base-pyramid n-integral encoded by B0. Set

```text
D=6delta V_Q = Z+bG,
Ecal=24delta E_Q = bZ+H+b^2G,
Ncal=24delta^2 N_Q/nu = B0+3bG-6b alpha M1.              (3.2)
```

These are exact cone integrals. Indeed `Vol(conv(B,Fplus))=bM0/(3delta)`, and on the root `n=(nu/delta)(1-alpha z)`. No independent height-law or horizontal-location completion replaces (3.2).

For completeness the original vector first moment is also fixed geometrically. If `kbar` and `fbar` are the actual area centroids of K0 and Fplus, then

```text
J_Q=(AK/12)(B+3kbar)+(bM0/(12delta))(B+3fbar).
```

The constant root-plane Jacobian makes fbar the same centroid in physical area or yz area.

The paired appendage gives

```text
D1=Z+e,
E1=H+e(b+q),
N1=Z+B0+(3-q)e,
N2=alpha D1,

6delta V_h=D+hD1,
24delta E_h=Ecal+hE1,
24delta^2 N_h/nu=Ncal+hN1+h^2N2.                         (3.3)
```

The actual vector update, useful for continuation, is

```text
J_h=J_Q+h J1+h^2 J2,
J1=AK(R+3kbar)/12+eta(2R+B+D)/4,
J2=(AK/3+eta)w/4.
```

Thus `g_h=J_h/V_h` is recomputed, not preserved. In these scaled variables,

```text
T(Q)=nu*Ncal/(D*Ecal),
T(P_h)=nu*(Ncal+hN1+h^2N2)/[(D+hD1)(Ecal+hE1)].
```

## 4. The exact coefficient dichotomy

Write

```text
F0=2D Ecal-nu Ncal,
F1=2(D E1+Ecal D1)-nu N1,
F2=2D1 E1-nu N2.
```

Then

```text
24delta^2[12V_h E_h-N_h]=F0+hF1+h^2F2.                  (4.1)
```

In particular F1 has the same sign as the parent's C1. Direct factorization gives

```text
F2=(Z+e)(2Lq^2+b^2+2be+bq+2eq+q+1)>0.                  (4.2)
```

Let `f0,f1` be F0,F1 with G=M1=0, meaning the algebraic base-pyramid contribution, not a replacement of the actual body:

```text
f0=2Z(bZ+H)-nu B0,
f1=2[Z E1+(bZ+H)D1]-nu N1.
```

The exact identities are

```text
F0=f0+bG[-alpha-q+2qL(2b+q)]+2b^3G^2+6b alpha nu M1,
F1=f1+2bG[Lbq+Lq^2+2be+b+eq+q+1].                     (4.3)
```

The added term in F1 is nonnegative. Also f1 is affine in e, with

```text
f1 at e=0 = alpha+bq+q^2+2q+Lq^2(b+q+5)+2L^2q^2(b+2q)>0,
f1 at e=1 = 2bq+2q^2+4q+Lq^2(b+q+5)+2L^2q^2(b+2q)
             +4Lq(b+q)>0,
partial_e f1 = b+2q-1+4Lq(b+q)+bq+q^2.
```

Consequently,

```text
F1<0 implies e>1 and 0<q<(1-b)/2.                       (4.4)
```

This statement covers the whole endpoint domain, including the equality `b+2q=1` in its positive-coefficient branch. No stationarity reaction is used.

## 5. The same root support pays for the entire negative first coefficient

Only the case F1<0 remains. Put

```text
rstar=1/delta-L,
DG=e+b+(q-b)L=qk,
DH=e+(b-q)rstar.
```

Under (4.4), DH and DG are strictly positive, and `m>0`. In particular `q<1/2`, and both DH and the actual numerator `e+(b-q)r` exceed `1-q/delta>0`. The actual parameter satisfies `r<rstar`, and the function `r/[e+(b-q)r]` is strictly increasing. Thus the physical depth wall gives

```text
h < hstar=q*rstar/DH.                                   (5.1)
```

The same geometry gives the area capacity `G<=qL^2/DG`. Since f1<0, (4.1)–(4.3) imply, throughout the entire admissible interval,

```text
F0+hF1+h^2F2 >= Lambda,
Lambda=f0+hstar*f1-b(alpha+q)qL^2/DG.                    (5.2)
```

The estimate drops only nonnegative terms. In particular, it does not apply the negative-coefficient polynomial at a depth beyond the coordinate wall.

### Whole-domain exact positivity certificate

Define the polynomial

```text
Psi=(delta/q)[f0*DG*DH+q*rstar*f1*DG
             -b(alpha+q)qL^2*DH]
    =(delta/q)*DG*DH*Lambda.
```

The apparent denominator in rstar cancels, so Psi is a polynomial in `(b,q,L,e)`. Introduce nonnegative certificate parameters `(x,y,z,u)`, distinct from the physical coordinates:

```text
b=x/(1+x),
q=(1-b)y/[2(1+y)],
L=z/[delta(1+z)],
e=1+u.
```

They cover the whole branch `0<b<1,0<q<(1-b)/2,0<L<1/delta,e>=1`, with no upper bound on e or the physical slope. Multiply by the explicit positive factor

```text
16(1+x)^6(1+y)^4 delta^3(1+z)^4.
```

The resulting polynomial has **518 strictly positive nonzero coefficients**, minimum coefficient **2**, constant coefficient **16**, and degrees **(6,4,4,2)**. The complete runnable generator and verifier are in the capsule below. Every denominator-clearing step is exact symbolic rational arithmetic. The three additional rational evaluations in the source are labelled identity diagnostics; positivity is proved by the complete coefficient expansion, not by these evaluations.

Therefore `Psi>0`, hence `Lambda>0`, on the whole stated open domain. Equation (5.2) proves

```text
F1<0 implies T(P_h)<2 for every admissible h.             (5.3)
```

It also proves T(Q)<2: from (4.3),

```text
F0>=Lambda-hstar*f1>0.
```

This is the desired actual-body distinction between high-TQ first variation and low-TQ discriminant behavior.

## 6. Completion of the comparison and its value consequence

If F1>=0, then F2>0 gives a strictly positive two-cross increment for every h>0. The actual trace is therefore strictly below `max(2,T(Q))`. If F1<0, (5.3) gives T(P_h)<2 directly. This proves the theorem.

For clarity, at an arbitrary threshold `tau>=max(2,T(Q))`, the exact normalized polynomial is

```text
c_tau+h*b_tau+h^2*a_tau,
c_tau=tau D Ecal-nu Ncal,
b_tau=F1+(tau-2)(D E1+Ecal D1),
a_tau=F2+(tau-2)D1E1>0.                                 (6.1)
```

These coefficients are `24delta^2` times the parent's corresponding unscaled coefficients. If T(Q)>2, the preceding dichotomy forces F1>=0, so at tau=T(Q), `c_tau=0` and **`b_tau>0`**. In particular the actual depth derivative at zero is strictly negative. The theorem does not assert monotonicity of T throughout every below-two ray.

The inherited single-B-fan octant theorem gives `T(Q)<=Cstar`, where the accepted constant is the maximum of

```text
2(1-b^2)(1-b*z^3)/[(1-b*z^2)(1-b^2*z^2)], 0<b,z<1,
```

and `2.0287830356734117251411563027<Cstar<2.0287830356734117251411563029`. Strict paired dominance gives `T(P)<Cstar`. This sharp positive-core result is inherited, not recertified here. The new coefficient theorem itself needs no numerical value of Cstar.

## 7. Exact actual controls and useful failures

### 7.1. Positive discriminant is not an admissible-depth counterexample

Take `b=q=1/100`. With canonical vertices indexed 0–3, the actual original P has root vertices

```text
4=(1/198,199/198,0),
5=(1/198,16600/16533,1/1002),
6=(50/99,16667/33066,1/1002),
7=(199501/198000,1/396,-1/198000).
```

Its true maximal facet cycles are

```text
(0,1,2), (0,3,1), (0,2,7), (0,7,3),
(1,5,4,2), (1,3,7), (1,6,5), (1,7,6),
(2,4,7), (4,5,6,7).
```

Thus P is proper `8/16/10`, not the mechanical `10/17/9` layer. Its original integrals are

```text
V=3339815867/19641204000,
E=337341235367/7856481600000,
N=3792591732497515913/43297070097600000000,
J=(222656087683289/5185277856000000,
   223085862788111/5195648411712000,
   110433795895238711/2597824205856000000),
g=J/V,
T(P)=2252799489103524452322/1126657610472088168189.
```

The clipped root adds the retained point `R=(199/198,1/198,0)` and removes p. In Q, order its four roots as R, P4, P5, P6, with indices 4–7. Q is `8/14/8`, with maximal cycles

```text
(0,1,2), (0,3,1), (0,2,5,4,3), (1,6,5,2),
(1,3,4), (1,4,7), (1,7,6), (4,5,6,7).
```

Its complete original moments are

```text
V_Q=67469/396792,
E_Q=6814937/158716800,
N_Q=19153642637/218672071200,
J_Q=(2248861/52376544,1126690361/26240648544,9218719/216864864),
g_Q=J_Q/V_Q,
T(Q)=919374846576/459796984453.
```

Here `m=500,e=5,L=1`, and

```text
F0=21912233/44622400000,
F1=-640320913/167000000,
F2=909313/125000,
F1^2-4F0F2=409612370058634989/27889000000000000>0.
```

The old paired guard is negative, `-640761967/166983300`. Nevertheless the actual depth interval is only `0<h<1/99000`. At its coordinate wall,

```text
F(1/99000)=15454987436829757/34167511125000000000>0,
F'(1/99000)=-7923667587833/2066625000000<0.
```

So the entire actual ray remains below two. The actual selected values satisfy

```text
T(Q) approximately 1.999523436783,
T(P) approximately 1.999542246166.
```

Raw trace increases, but **the requested max comparison does not fail**. This control demonstrates why the admissible depth must remain coupled to the root width and the same e; a positive unrestricted discriminant is not a physical construction.

### 7.2. Above-two first variation and larger roots

A high-trace input uses `(b,q)=(1/4,1/10000)`. Its Q root is

```text
(19999/19998,1/19998,0),
(1/19998,19999/19998,0),
(2503/79992,62497/79992,1/4),
(42499/79992,22501/79992,1/4).
```

Append

```text
p=(166637501/166627780,1/22220,-1/224970).
```

The true f-vectors are Q `8/14/8`, P `8/16/10`, and

```text
T(Q)=5645482827498/2786172703127 approximately 2.026250139183,
T(P)=11905335289757410157430/5875560318482876579857
     approximately 2.026246799357,
F1=49227895813/50000000000>0.
```

The report reconstructs all V,J,E,N, g, maximal facets, true edges, the positive clipping wedge and both pieces in (2.1). A second depth on the same ray and its full actual moments are also retained.

The controls are not restricted to trapezoidal roots. The source includes eight-vertex positive roots with piecewise-linear convex lower and concave upper chains. Their true Q/P f-vectors are `12/23/13` and `13/27/16`. One has both traces above 2.0249; another has F1<0 and the old guard negative but remains below two throughout its admissible ray by the theorem. A large-slope control and a negative-slope control at original depth 100 are preserved as nonwinners. There are ten covered input records, not ten independent incidence exclusions.

### 7.3. The single-B-fan hypothesis cannot be erased

Start with the high-trace Q root above and replace its third root point by

```text
(2503/79992-1/10000,62497/79992+1/10000,1/4).
```

Keep the other three root points and the same negative apex. The new bodies remain genuine proper root-only bodies with c=d, but Q now has an additional maximal **C-root triangle not containing B**. The true f-vectors become Q `8/15/9` and P `8/17/11`.

The exact traces are

```text
T(Q)=141138097917996870000/69654801797547667813
     approximately 2.026250800745,
T(P)=7936947959482437236616870000/3917067442496637078064513813
     approximately 2.026247460887.
```

For this actual Q,

```text
6delta V_Q-(Z+2bM0)=1/100000000>0.
```

Thus extending (3.2) by deleting the single-B-fan hypothesis gives the wrong actual volume, even above two and even with equal opposite endpoints. The complete coordinates, facets, V,J,E,N and actual centroid are recovered by the source. This is an exact control of the **formula's applicability boundary**, not a counterexample to the desired trace comparison.

No mechanical S/U/H or weak-contact census is claimed for any of these controls.

## 8. Role of the new deficit material and the remaining problem

The supplied `ROOT_CONE_SLICE_DEFICIT_V2` is a necessary actual-body theorem, not a threshold certificate or a body realization. Its formal separator remains a nonbody.

For the new actual controls, the original A-cone coefficient is exactly `kappa=1` on Q and `kappa=1+alpha*h` on P. The auditor checks the Jensen, first-height, reflected-height and both directional-strip deficit inequalities on these actual moments. Their inputs are computed from the reconstructed hull, never freely completed. The new comparison proof needs the more specific actual single-B-fan formulas, root width capacity and coordinate depth wall, rather than inferring realization from those necessary deficit tests.

The general remaining interface is now clearer. Equal endpoints make n on the root depend only on z, and the two actual B-cones make V and E depend on exactly the same root area. Their compatibility supplies (4.3) and the positive polynomial in §5. Unequal endpoints retain a transverse first moment. Additional non-B facets retain extra original determinant volumes and their first moments, as the above-two C-facet control explicitly demonstrates. Neither correction can be omitted.

The most useful continuation is to retain those extra cone contributions in the first-coefficient inequality, rather than enlarge the present system into an independently fitted moment model. The arbitrary unequal-endpoint positive-slope class is not closed here. No mechanical E17 exclusion, 110 realization, registry change or new minimum is implied.

## 9. Boundaries and provenance

The theorem covers all positive b,q below a, all genuine positive-area roots of the stated B-fan class, and all admissible depths. It does not impose a bounded parameter box, a fixed number of root vertices, or any stationarity. The only finite depth wall when m>0 is the actual apex y=0 wall. The algebraic extremal value `rstar=1/delta-L` is used as a bound; no enlarged coordinate-face body is substituted for the proper input.

The e=0 visible-wedge wall is covered by the direct zero-tetrahedron formulas or the parent's cap theorem. If the B-projection lies strictly inside K0, the parent gives the comparison directly. If Fplus has zero area, Q and the positive clip are B-pyramids with trace below two, and the actual negative cap is pyramidal; the parent then gives T(P)<2. The equality h=0 is the unchanged body Q and is excluded from the new strict comparison. No q=0, q=1 or b=1 extension is claimed.

There is one metadata conflict in the supplied journal: the branch note gives parent-wrapper SHA `736347952c74f07a0a88bf7ec080aafb8c638328575f132de0516f9d36ad2fd7`, while the literal parent gives `775187275a045f86c46a7b6cab213b5bc09d8cd8f085c7f05382ebfc08a3923e`. The literal parent pin is the retained one; this discrepancy has no role in the new theorem or its standalone recovery.

## 10. Complete recovery and actual execution status

Save the capsule below as `recover_equal_cap.py`, UTF-8 with LF and one final LF. It reconstructs both complete source units with all exact inputs and helpers, without the parent source, an archive, or any other file.

Executed dependencies: **CPython 3.13.5**, standard library for recovery and the actual body auditor; **SymPy 1.14.0** for the polynomial certificate. Assertions are enabled. The exact acceptance code has no floating-point hull, numerical optimizer, random seed, NumPy or SciPy dependency.

```sh
python -S recover_equal_cap.py equal_cap_recovered
cd equal_cap_recovered
python -S equal_cap_audit.py build controls.json > controls.txt
python -S equal_cap_audit.py check controls.json > check.txt
python equal_cap_certificate.py build coefficients.json > certificate.txt
python equal_cap_certificate.py check coefficients.json > cert_check.txt
cmp controls.txt check.txt
cmp certificate.txt cert_check.txt
```

The whole-domain certificate reports

```text
POSITIVE_MONOMIALS 518 MIN 2 CONSTANT 16 DEGREES (6, 4, 4, 2)
REPORT 8634 e272cdb3c6214687a7f50a1ceabd88296c5d4c6e3f30d0266daa0ee37b38c356
EQUAL_ENDPOINT_SINGLE_B_FAN_WHOLE_DOMAIN_COMPARISON_CERTIFICATE_PASS
```

The other terminal markers are

```text
EQUAL_ENDPOINT_PAIRED_APPENDAGE_SOURCE_RECOVERY_PASS
EQUAL_ENDPOINT_SINGLE_B_FAN_ACTUAL_PAIRED_APPENDAGE_AUDIT_PASS
```

Exact pins:

```text
recover_equal_cap.py: 8978 bytes
SHA256 871e5eeff7b529772754e779cf3c895f91fe18d42d604e1ac0d3ca01df87d812
equal_cap_audit.py: 11978 bytes
SHA256 dea2fef518b53019e6c96a540dec6b91058a3f22db6f09bd768a670ea3a23104
equal_cap_certificate.py: 2884 bytes
SHA256 5687b9ddbf2d4de40a35e7225b95e6fee2e0715d0e34bda8713d9c93d212e191
controls.json: 58032 bytes
SHA256 5baa3f526ff08a383571b73c13fbf83619adb3a1045fdeabced8ee6eb6f08cae
coefficients.json: 8634 bytes
SHA256 e272cdb3c6214687a7f50a1ceabd88296c5d4c6e3f30d0266daa0ee37b38c356
controls.txt and check.txt: 1571 bytes each
SHA256 7285fd0af7083826861657032e4509ded7af74ad592dd963769d50c1db10b3ff
certificate.txt and cert_check.txt: 208 bytes each
SHA256 208cd5fe5eb48b89feb75cfbddcbba894ed00725f8ac5b4dfba433233a89aea0
```

Normal execution and fresh-directory source-only recovery/build/check were completed, with byte-identical reports and stdout. Two positive interior fans independently reproduce each actual vector first moment. The genuine visible cones and tetrahedron reproduce the full hull's differences in V and J. The positive wedge is checked against two independently rehulled constructions of the actual clip. Maximal facets are recovered before true edges; triangulation diagonals are not counted as edges.

The coefficient expansion certifies a whole unbounded continuous parameter domain. The finite bodies are controls, not a sampling-based proof of that domain. The geometric proof is not a proof-assistant formalization. The older sharp Cstar and octant results retain their inherited evidence status.

Convenience copies: recovery capsule (`recover_equal_cap.py`), actual-body auditor (`equal_cap_audit.py`), whole-domain certificate (`equal_cap_certificate.py`), exact control report (`controls.json`). The following literal capsule is sufficient without these files.

```python
# EQUAL_ENDPOINT_SINGLE_B_FAN_NEGATIVE_APPENDAGE_V1
# Complete deterministic source recovery; standard library only.
# Parent minimum-0177
# SHA dbe60e47a944154d8a3acc376b60f1a45bad6b2a6feae1779c20e7ac3d49e376
import base64,hashlib,json,sys,zlib
from pathlib import Path
DATA="""
c-p0VZFAbl()M4`v-<%_3>e9dlYl2xPQZ@6n2^|;tqP$i0kTmHk}L@uoXUT{ukINMVY5m0Jg4^HdFkot>GvK@zW?FhExq|@;>9Cx
ISsOUy#Ay4$Dc;$<KM^KQK#4Le>m%1jV{l6r`^uz?dasVH|ljxkFU-?cSgtkJ|K=yJEPCe*YHo{U4Na;qR`l{JNxw)!bmeOoO;RB
m<Qv;OV+~h($r6~APQ5%554i+pVp0DWcaJhPeN~Q1Yx|)(mEk~znsta7Fb}!Nw5gA;NDM-#Lv7S^ryyk5-orh%djf;5<kp<{ALv1
yL0EpJ%0V==KkCI+reMc+wA@6O@mSP72M_fV`Dn@4;%i$OYil;f%D>E`pVn)CX@Y_hvUP>wc{PU7<<#hvFjaP`=0N-eEE9fHvE^~
WPf__+6Nf$F$vd+H&N#a7IBnh#)%#PHO7esA~LfmnioKmXfX~#j~8l~*vn>MQx4Hb_iLy-GcTn%@hy!)k*=}iSehqh!xF`h)q1-<
<Y4GsG34Y>Z5nd67QQ>~$-%LBE8dCr@M}2ruMKZHH9ax5n&9^`35{$S&wX=MT^rX?Vywg(f-)Y1n1L*{CS8tqt*QNN&0;w>GvPg1
li4e^hE{kQbQ)z_=+ouGG*|X+?CNA{;UtODbZe>U4V<Ap9=OArhaa?@q0p@cjWyJ)&@G3?95tI$<1;m4QXp0Ism*9y14c;zm3snf
7W-JXImz)`HM7`@$8#8kX$E_6&Dd&w4UJf)&<lTRrl2FHy^P@6nEN3*N7Bjni80Pgz4^6y$19CQ4u<r%VDKFe8xON!?lX$SdgB-{
+?@7gPy;XU3ofmIzR^tTaTJ>tuS@D)9Q)zaTybCToS?0nym@R5npj^|ok5d2YDg<w;(Md(AW1WQLQj$iTi@iM&{QJ(iLhf451i((
3XH(V2bszhNo`G>T#?k)=(fD7obI{#xdU3Cc;St2x>obsAQ)oWHdoYG<Hy=NBof$H8Qz=5<}jX6D*CM?l>MA!1+SzaCH>XnX<d60
Kb7Bq=o19uo46$!%6`C91gYhg*jL91rBW%fu6Xcmhy#N@p}M!a%bbS-gb~OM*JfxnCsCLM;nJs>nIz>56>RI?o2PQ1MpjmBw$X%m
sPQa<&?GSHsByILR;s;)l7RAwH;rZ}$&zc12(8vk)@FK>TFH)SMB$%eCeVDirzt;NF5t&AU*RL<_fkS?(<F)|?W0(;Z;4xfE$7~1
JoSvA>5Wq}<ny<@mA}Edk?uYt3;v%ZOuT!XM9?WEMB)cn%8S0SuK^Zog9DTfTaz{LPSXJ`tOpSK3YMhS+!2sAOUzn1`-rz?sZB^3
NmLWk#X@@Mx#eLC+&gMCC+m9R-}_1GD+{}o7*QLOTqbKA7euKeVCgONAAg#+L#=1}blO7@{17Ne^;ioB3g}jyfz?oh@`N>P`O}+i
ZJn&Q#iRh6xjDhP<pw!f3p%YPiENUQ)nN!Q7jHSw%q{AaySBt&Xytw+pi|@gS(-b!?;dZXsNlWTwroM`ACSJb)cKsv=N{JQGKf+y
rU0t7^iz{<rDUnRkyWE6!&y~ossjSc#`1YcXo?i5;Kg4<<qEDn7_LxY5i{qr@?qyX3S0JmYvRwzFmhK`I#P3ob8-X`0}0j~#ceho
ll6u89H`$a_}qe56pwNcZwZz(nAhD$b4f9aG;am+SOwR4;}H$z^NgG~Snx(R)SlPWQ~MjAs}dcYiBg1fL1vHs-htqh0soKSRJa3j
AX!TtITx-8iUbz07&K=;i*vz1IVTssmo5{qS@~7PQf9g0xXit7%L_})eDH&tS(ehd%>gAjLt8mhfgYG-J!P+UwK{M_+N3D4c(7MF
A0NajS8lz5z?waVQhjT~@7(LK;expQ*xR}>Xu89a8UhaTl#>2ZJk0rGs|oS!{5hY-(R6LbQ4oSAq!(hUbAx$+Fggt;S)DRVxXe^T
K^nyD=L{`ze3MEj(>PLGViv`uU%_z0M+O=G7E%Z}_uQ+dQ#Gg1X`4cI)tsm%(gSm>nl7;+3^xl*r#h}q@&(kHswEpXl5@l+$U{mI
%~DF-k)QRB=bIhRH#?qV$5u~<p?O{s%;z@^&VxGT41oBm*(sGs(I_2WDi&Oi?)^y?B~ojd*mxMR@i3P7EWtc^E^au2I(z6@q9Z$^
Cwt;b_V&y}`?K94jrtmDx<;d^KVII9MoJA3dtyH^6Q61Ytpchus3<}!xruxeS;B%d&4&2SIsXq!z|U~I{lijn*86-fh3}ZOVufgl
!2Cl>peX@T&hdR)GvJpQs^sQ!niS6}d0w0OS>l;-rUHtmG+CnGx|bB;bGJ1{oxt8|k~gMkXuqX}bFUmy$sJLA;SQNcQ4%b35%QkV
GJ|3>r7@qCr|7^j^a2|6B=g+L+O++-igU~)my%9*h*%EHxeFi~R!klN?D21nz;a)_vaGUK++oDPmY-m}4CYf*?MM<rZ{dS!ccR-6
zDN==n~5Zfu9=|iapY35c_Pg1QA(fY@ywG>ZQPpr^Nd<|t#B#H&hCJvE4z(7o@pgW$E2e=wQehsNn+DjE0syL3)qD;eX^=M%TBDl
yVe2$OLf!Qm<Dd;qP9pkR@OKgAE|nyadcO-x((g*wGlRslH|zQEW4Go(YR{f0j=EyW@V*Ol;v&%5vXaJPK}AR*EK$+{b(ubDP9u4
KS^3+CIX@QQngcRKS+}oDCp`!)D|d1;4Ns;OwML@vbW$w7!>;R)Hi0c4S6$7wz)vTgi6Yo9RZw{LbK)IleiozPfMbbvH}~3{l_Sn
R#=bzG&(D9lEF9<_%&}{+%p&tyujIWg>j8AXn5DxLFgL~!8Ds0OJwMCBb)g~7R7Z!^eDS~rfc6?E$myTdlu;8K%Ka{uphw#q0U@g
q}&}UZ@nQciI&j0>8nbSqGaqs5MspvUoJrV@n>JW(EfvVwX?n3Ryqr=Gisyvif49HQDwj<wAAuJO;PGM6E6UtkMm2UPLf1$e5CBe
*!81S+4un2wL_UTtgB?!2vy7msdgs$^DG)XzkVD(DdRFq0?mV+a#AvXRSx8cJ~85p7Cq5WG}(`A(ei8|pe1pGfC~gil9|C{&sN9&
iu15f>{n*u!76fLiiR}LxrU~K`{b9f_M_zN;oWhs8gu$^C+@6Pe`~ZlpcO+sNgP&@<|DYMTK&=?C?itnH&LU%i9lea^DGU}rfG6m
U-2D?GSVF>K)5W!k#B?dql>GyfHjGC!xjy=a=>Ta&_JWZ*70BB{4ZI$W?*2ebvu^k`CmZ0#}GhG4Sju7md{(l_5I`KKu^OR894!N
gWw!e3tj_SIiUXx*m?%KiJl*~0_Rrb{RvT0et%00`tk3W?t?TK&;6%GNePN=TGto<zSp3+KipjbQ*6_927(;7NU^B%rqR^<=W!CJ
eo~>Sd0ma^iNQ}Lu{nia3>ggQE{23|3C)rr3F3c1q?d~VA)Wf7Aud?4$~p#*Vzo}CYhN^47mic_TS@DMQ-rtEBRI<L-Yq7-AoAYX
-PU{hix#!tHl$mlj=4|4ltOL0Ex%O9_Gzorkz@Ny^*uV&?e*l_Ms=UswL|<Wle!@DYdcutw>pk|U-fMh;oWNWXbcM!V!zdMrCQN0
g<I?;4{c?x;MnJia#7e>x(A!_jvfaIoAF|{R~hbw%MH>TVV@C7*=|>7*p)F9tNV;q%1#H9of1h;@b`24QucZP?K$|tAJUpXjWdKW
(l0;E=4)hd2$>Wn5mc9mu3Eb6D|q)Eb8p+9D56g8<;*_*YY(;jH_q87MY>5kO(Xl_cC2!_>|SKwq{?vFnF`jOVd18;dkJ(tW%+!H
lI|;})IMt7Ozx}MJ<~?^gUR#CP<-S+Fb&Rdk=@h1q;VJPVgiNI4B2lU2CDiVf;{<rnJQmTxp3J{=b?ZgTm@3Hkm}$rE(L_#_0u&c
;J3VeKIoQ4RT!dZN6@!a^(qiFRTbUf)B;BqIGKRt1*FQne7F}61uyU7oRb?W9>B}&UL9J+PbR6%#D@(B)#MfvAHD(E3GB>nx9v`+
hKSSawN4xim^9*4I~}N}#S>2J#3e`v<2+FEPA9ImYF@}XZP}()U|w!+t0*=<X`p?g22Kc9<}LZ|^Tb4U1sbnFW9#je#P}|9wiE}j
M}T7*bQfqE`@(57N*oK}rWNKl(q-Ti=ZFEK`SfP#B~zU6_%GXhzxM@Mc9s4(HTaEiS>vOr+}Ki%#M=8p-x~t&CXCW7n8+TiOeML5
wp>~I`U}Ij>e_kEuLwDE%S7{yefw0F68%>Dy(|h0@P{DCY)NciKnVFkX35(|KE(q3LJZT>TU;~d(Sx5z#(_;3>0TQ^ytFp9RT+Q-
k{^bLZl9J;!i%}`D4(1!2|#!IRDj&}dvP<5#@-xtdz{TiV@jxHv6G0Sls|8d7@3~twosRD@ob$2lPBv@PKc9{myL>9H4a5Gsnj54
QVrXMMrl-2KMC$V-fhQH2lCL1U5owZ<uZ=vfj`Z?;c<<9XF3liKC-v#U=mO@z+aJZ2tO6-D+CG_->)sA1$}V64zjxX6h+{rE4zp<
j?IsvuL_4-FGk2y(MRb%{8f!|+0~$&(?#QwQ?XhZLK6+a##>7PKcQ|@4g?L}klien@_<1QO7?P4Kl2(o)Rh8B>*9j#Zme9K(QZhP
RU=?KYqcBYuDw{cx+@y6OM?m-X4boB?pxiIXH5K5p^96x=CXRv8{c>_SmnO7FD~qEivMbd2X?z*+xvpMXg6wV<Uo&@2L#-1)G%cg
a|c9%-CfnpS2TiY{g;vi{L=re9BTbjs9{O<Ni0O8zGExIn`d%t1i%@4bXWmCwi^No2=Ium?4|;o>#hX2)LjccEMv2t+_lmDhU80*
*h}ySC2^_@Y%C!oNmm(?ZZjm^XGnF?q3=K>*M?kFjyU8|trPk;+5otIqNt1@I0DJ~T92!9k<L-#$b}#`FruVRqA*}g>qpf`&X@OR
d=)%W`YtaVZEeN>xICv<79KdX9;I_{a;wt4+Nnrkf&NrG4J1Ky|Hl`AJ!Y39kgjzcfjq5;Usv{Afhcv-5C}~tjzAoOd5=dFFy3B?
X^>9n!9?hRk`o7R0E%$ZAd41o>m%jYa|gfS23;n}jSqWz0-Xkp^o^(PijNY;EBm6a*oz<WK-Zk=G@lW1#W@12CCF{$gA*E@V34DE
KAO=eG8my1X*8MnlUvAI>s9_meVL`fln4n&^hq*_=BB#qlIljHb;k{aIw)-ELMu_juV24@Wwp|jdT77aBYYEN<~Li3Nc8K7%gtb#
3jCMXhJVv%9rp!->PsMSt=eW&z#O^<uV3n!>edXANbCQh^#=fZt-&zo0-v+#=Af*obl-A#c)0(PK&a)ueECXabn!p(l&X!L6^VQq
M%pa?7XJ)erJA2+b`<?I{F_z(FAI6op?Iwed4ENM9!%D|D@@7}-g4mhRgq1}0SB1hs<g|{zfo>Kx&C3I>E43zy!$C_42#3lM^kbR
;#o2Hv#TlMI|Z_?Ow(G@()AzRrUq#mgf~x0ubTM<ff|J!uv_IXAPlT?Po3DQOzI7(D$+mq#ZLEH@x~EcK=u%ga`PfgF!#4)XO)r%
WzE^)LUTvJj2MMc_?CWn9ZOl}9MbM?bRW%^3xA}E9?>l~6A%afMDHv0<WpaiW?lwTDj)v7x;$%lMpy4Uqh9Bq?N@3T{P3xB(bD+{
_~-Kl>IA6{Vu-);7BR{?h+yGQW?o2nkTIc)MYtO;^DEll_~FD{v4f$f1R#fAwM~3;B~CVvk+MX+e|ZW*EH0qF6WFcQB#ig^tD$-U
v8o4|zer8%#||7OeF{+TPOJjgpoB!BD1A9xl|B+E-^ig8k?kuLSB3QENZh<+ROFxK(1F6s*@M$6{eAsfH(v0dTl{V=MJ=Is09q2J
N?5g<&QUeWjn@imj+Q!`KhF>sq+$kIlFne+(F5Z<D6nd@uZxaTYPq`q8`!754|n%pk^dX%Dnnp{px2hU5dI6Fi<|h}C}-3q%Ktk*
c3}_whaxE&=>&fbICqce+E>Ti=Y4)jXpTm|Y?*F^u+P}sz5U<OtGSolK<bp4J>^?TYhL{7WXo`@MhYn?oLh?eq9AUgGz})z<w5Rj
Fmvpn=Ln@wb9P+*{J<tSeEQvgP$`nK3f-Oa4T+vno)VF!a^n1Ca?5OoT#P>1qEBEH2J(TAdSDA<4t3-{$FP+q@}@s2B%jgxZ1u^m
MNcVrON5pJSb^CspKMov^XPRgzbNrgtElhG5RvwaEgkCQ&Wy5^cn{K~7q|84auKH{Ib4pI6NJhH`8rUE($X9a-Ec=qHlk0q@+w*S
BK1l3S%kX9gwBXcvtn7*%Ga-9#i|2sG*wT%N~uS>Mj4gd&`YL$b!DXokUXdxGCl-wagtm?ZYJr;aItWpo|qt(lvYZqmo?-1LxPYq
8m}{-ULHOapV%}JaUHqERL_G7faD*+`K4T_9xTNPtQuKgh0=)1P*hGnR|JwiC71jW1WjChtccY{o*3x!K))Dx=OBQe_9}w#ZL9tp
RI|@Vk5rbcXeg2a#D0*Vh4C+h6tmmpY%jV}-$yk1Po4gUPgfOwyg~dD`cZZrG01&!$Yb@HznTU&KC-<sWj}jMfBf!>Ci}-{pE~W*
gZksY+h<o8zPzM71Y#VGh{dB3WH=g;K95F~rqb)L;UA*(j=z+{{C~aXS6`sL`HeqLykJt!japBh`m>5&t{45a;nbajx_WNki`095
<2so0#Spz8<TNXaGx)1VenKIP>v@D$c!R__$Y!YUQGHTgrl0kzNAUEI0{-<m{4Zb7r|U($rYHHAyI#@odkEpn%R1o3(L9BD8Fxn4
;3QB#jL<bCioqH(^WXVIQ+h&i+St0oJasmAm|sH_^Otph6@!W9vr9}6fHJ={ZvvqBcw-e;nkWh2diZX+{56O4P+gCD)v?W#(w%Fy
YZJ|cqx!<aNY^e#Fs&ES#pzfr!0*AYmjR}$=dFU#1??wJJzb9BNd?TAiJ}VZXK;>!b9TdB)~CVsHNb^WZ|8}Eno}krKe46OpNexa
D+~G5I5%b_;^ITv_II==pV91dK>p?jH2!$j-x6%wR-Y75ac>J$-Q{mCr2*h>E!=!#*um9)qju7$fk@k|c{L@hu8n1^A2pJoy^mSj
)u#ZW^W6;XJGB#sR{&X;MbF~pVw3dOCw^8P&Cfhtb|otx?Ww@QzI+KU&X?`j(XAC&6w*J9z8*ly7DklSz;QQ?J24ff4RJ~zOsU>}
qs#KUBfe<ZbKxKQX#l=WsBW5@Q`<ag*r)i9EH$xD9CY|PpRV$i;+{Iz-j=53&umPfvN&QwjQr_aEX$g+GS<eUu_WE;Z??oDrMX@4
xJLvyReA$!Pe}sYvF(H1+ZCJjH<IrcW>8&PPj*sMcS7B=tm%ypHdxbc&Y^1l-d@`X$6`ev&{jahe{B2k7dT?z=tuLl*%z8mNS&ew
B*FuJ!nUvk1;L4aGrtfMPKN9BvI&{Ru)xlN6$_yTFPv8_TYm3eUZ&^WVo_Y5ME>>lXc3XBcyrUS-mnsNyveMrK()ynH7Ny|ypl2a
&I6^k;d7u<vPGQRL?Mo1$A-?|d?Vq2<;`nc%ov<{5rQb3106lLM!X`_rE65ae$YCOso(l{V;=!TnHCrdj)J92^=8u%uGptHSEef*
aR4_e%$FEJPrbb2e|GVG)x4~K(xjTJl_l2Yf%V!FkL7{KM@uZr1Is1fLyS|og$HT~WUV`7u~53yvbT^5rGWIW6Q(J}N_yfqpQW-e
itpp*I2CuzyHs?y_Xp-jdX|?8zX@Gm{(#A(xy`WA<Vww2&8o?|SxTC*lhjJg|BB>m_%wm%<UJRWto-Mks3Pv68uX7Aq1=@fa&M}J
AMyVs63D54llYj4>#8+k?WZel=(%LY{U7TB{T%yeB>|E`RR`qh`?FeLS31x6{_ocvMfHFs&+$L6Cv^7P|8RN6yuA3(`*3k~+`ZIE
G_#~~afWn#x1pmX_|Ut&I_@Fu-eKsX((aso>U1t?c8lqo&Hsn2{Wp^Kf8KvUyZzzf_^da2_u-;{{ORoS1Dc&rS7#?@?~boJMe6>?
kN*S9x!rs
"""
raw=zlib.decompress(base64.b85decode("".join(DATA.split())))
assert len(raw)==15204 and hashlib.sha256(raw).hexdigest()=="2a7c0c1d035356f22bb423d4f6aadf9fe3d209c5c3d027c5560ac8abaf22c031"
PINS={'equal_cap_audit.py': [11978, 'dea2fef518b53019e6c96a540dec6b91058a3f22db6f09bd768a670ea3a23104'], 'equal_cap_certificate.py': [2884, '5687b9ddbf2d4de40a35e7225b95e6fee2e0715d0e34bda8713d9c93d212e191']}
files=json.loads(raw)
assert set(files)==set(PINS)
out=Path(sys.argv[1] if len(sys.argv)>1 else "equal_cap_recovered")
out.mkdir(parents=True,exist_ok=True)
for name in sorted(files):
 data=files[name].encode()
 assert [len(data),hashlib.sha256(data).hexdigest()]==PINS[name]
 (out/name).write_bytes(data)
 print(name,*PINS[name])
print("EQUAL_ENDPOINT_PAIRED_APPENDAGE_SOURCE_RECOVERY_PASS")
```
