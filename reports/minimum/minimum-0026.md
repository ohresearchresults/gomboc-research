# minimum-0026

AI research report · 2026-09-08 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# C32_TYPE294_WHOLE_ACTUAL_U_GE_2_V1

## Exact determination

**Canonical C32 type 294 is excluded over its entire continuous realization space.** More strongly, every full-dimensional homogeneous convex polyhedron of this type has **at least two strictly unstable vertices at its own ordinary-volume centroid, for every positive-definite physical metric**. All nine possible unstable vertices, every stable-facet choice, all nonsimple incidences, all five quadrilateral facets, and arbitrarily ill-conditioned affine images are covered. No symmetry of the realization is assumed.

The certificate closes **one whole nonpyramidal type and all 15 of its joint-root orbits**. It comprises 4,067 rooted-tree certificates and 35,392 integer positive-definite matrices. A separately written standard-library verifier checked every matrix by fraction-free Bareiss/Sylvester elimination and, more strongly, verified `R-I > 0` for every certificate matrix. Four clean reconstructions—two direct and two executed by the literal capsule below—produced identical certificate and transcript bytes.

**No global C>=34 theorem and no C32 attainer are claimed.** The inherited bracket remains `32 <= C_min <= 1374`. The lower-bound and upper-construction provenance is inherited, not independently re-proved here. The supplied current register distinguishes the accepted wheel exclusion from the separately preserved map295/U7 result; that distinction is retained below.

## 1. Authority and literal type identity

The immutable analytical parent is `minimum-0024`, SHA-256 `b578a01ead261c6f7745122c22f4bb4767884e46ac46e1531b4e749a19332f95`, entitled `NOVA24_F9_SYNTHESIS_AND_RECIPROCAL_ACTUAL_TRACE_V1`. Its envelope authenticated at 57,975 bytes. Its Markdown, including terminal LF, has 57,109 bytes and SHA-256 `927f610bfdf4e8a21074a32aa5581fffe4e1725727bf7ec848a22a26db66b6c3`. No parent/alias conflict was found. The accepted `F>=9`, `V>=9` and C32 f-vector reduction are parent results, not new computations in this handoff.

The canonical catalogue used here is exactly `c32_catalogue.json`, 240,929 bytes, SHA-256 `efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d`. Its incidence layer is 329,358 bytes, SHA-256 `8954c59d7ca3fe9c12711833222fe77cf3d1a2f57d9705f656c4e484dcec88e0`. The literal maximal facet cycles defining the newly excluded type are:

```text
F0 = [0,1,3]
F1 = [0,2,5,1]
F2 = [0,3,7,2]
F3 = [1,4,8,3]
F4 = [1,5,4]
F5 = [2,6,4,5]
F6 = [2,7,8,6]
F7 = [3,8,7]
F8 = [4,6,8]
```

Its complete true-edge list is:

```text
[(0,1),(0,2),(0,3),(1,3),(1,4),(1,5),(2,5),(2,6),
 (2,7),(3,7),(3,8),(4,5),(4,6),(4,8),(6,8),(7,8)]
```

These literal cycles, not a pictorial alias, define the theorem. The independent checker reconstructs their eight automorphisms, verifies the coherent sphere and 3-connectivity, and obtains vertex-orbit representatives `0,1,2`. Automorphisms only relabel arbitrary coordinates; they do **not** constrain the solid to a symmetric shape.

The complete newly closed canonical joint-root list, written `(unstable vertex, stable facet)`, is:

```text
[(0,0),(0,1),(0,3),(0,4),(0,5),(0,8),
 (1,0),(1,1),(1,2),(1,3),(1,6),(1,7),
 (2,0),(2,1),(2,3)]
```

## 2. The actual-area gate remains hard

Use the inherited physical notation: vertex rows `X`, pole rows `Q`, `S=J-QX^T`, `U=J-S`, and the incidence matrix `B`. In a nonzero row chart `R`, retain literally

```text
t_R(T) = det U[R,T]
D_R    = sum_T t_R(T)
N_R,vi = sum of t_R(T) over facet-i triangles containing v
D_R B_vi = N_R,vi                 for every incidence (v,i).
```

One coherent fixed fan on each entire maximal facet suffices. Together with the exact polytopal slack support, positive incidence support, `sum B=3`, and `SBS+S=4J`, this is the actual-area-gated model, not the free-B relaxation. Its physical metrics remain exactly

```text
G = X0 M X0^T,
H = Q0 M^(-1) Q0^T,
M > 0.
```

In particular, no independently adjustable inverse block is substituted for `M^(-1)`. The preserved false-centering control proves why the weaker joint identity, actual column masses and rank-three common geometry are insufficient without the area gate.

For actual B, integration gives `SBS+S=4J-4(Qg)1^T`, where g is the ordinary-volume centroid. Consequently the hard gate and `SBS+S=4J` give `Qg=0`, hence `g=0` because Q has rank three. This is the point at which physical centering enters the exclusion.

The successful route was not a numerical solution of these equations followed by a metric relaxation. It was an exact contradiction valid for **every** actual solution of them: express several genuine tetrahedralizations of the same solid, with their actual determinant weights, and certify the resulting entire vertex-escape disjunction. Excluding this larger necessary set excludes the full hard-gated model. Nothing is inferred from feasibility of a relaxed PSD block.

## 3. Whole-domain proof

### 3.1 A unique strict unstable vertex supplies a weak true-edge escape tree

Work in any affine chart with physical metric M>0. Write

`d(i,j)=x_i^T M(x_j-x_i)`.

At a vertex that is not strictly unstable, some true incident edge has `d(i,j)>=0`. Along such an edge,

`|x_j|_M^2-|x_i|_M^2 = 2d(i,j)+|x_j-x_i|_M^2 > 0`.

Thus choosing one weak escape at every vertex except a presumed unique strict unstable vertex r gives no directed cycle. Every path terminates at r, so these eight true edges form a spanning tree directed toward r. This also covers a zero escape derivative. A farthest vertex is always strictly unstable: for any distinct neighboring vertex j, the same identity gives a strictly negative derivative because the squared edge length is positive. Therefore ruling out U=1 really proves U>=2.

The graph above has exactly 3,600 spanning trees. Enumerating all eight-edge subsets and testing connectivity is exhaustive. Quotienting only by root-preserving graph automorphisms gives the following complete cover:

| Root representative | Rooted-tree orbits | Exact certificate matrices |
|---|---:|---:|
| 0 | 1,808 | 17,368 |
| 1 | 1,800 | 15,030 |
| 2 | 459 | 2,994 |
| **Total** | **4,067** | **35,392** |

There is no tree/cotree sufficiency assumption here. Only the elementary **necessary primal escape tree** is used. Since every one of those trees is excluded, no stable-root or saddle-choice branching remains.

### 3.2 Actual tetrahedral masses, not a surrogate barycentric center

For a vertex a and shift s in `{0,1}`, construct `fan(a,s)` as follows. For each maximal facet not containing a, rotate its displayed cycle by s positions, triangulate the polygon from its first vertex, and cone each resulting triangle from a. This is a tetrahedralization of every actual convex realization of the displayed map.

For an oriented tetrahedron `T=(a,b,c,d)`, choose the common outward orientation and put

```text
d_T = det(x_b-x_a, x_c-x_a, x_d-x_a) > 0,
D   = sum_T d_T = 6 Vol(P),
w_T = d_T/D,
chi_T = e_a+e_b+e_c+e_d.
```

Every fan of the same solid has this same positive D. Actual uniform-volume integration at g=0 gives

```text
sum_T w_T = 1,
sum_T w_T X^T chi_T = 0.
```

These identities hold simultaneously for all chosen fans. A tetrahedron common to two fans has the same determinant mass; unrelated tetrahedra are not assigned equal weights. Changing the fan diagonal of an actual quadrilateral changes neither its supporting plane nor the solid's volume or first moment. No added diagonal becomes a true polyhedral edge.

The fixed B used in the area gate need not be replaced when a second fan is used: the second fan's weights are computed from the **same actual X**. This is precisely the physical coupling that a freely chosen incidence matrix or independently centered fan would lose.

### 3.3 The exact positive-definite contradiction

Fix a rooted parent tuple p and define the symmetric index matrices

`L_i = 2 e_i e_i^T - e_i e_{p(i)}^T - e_{p(i)} e_i^T`, for `i != r`.

For `G=X M X^T`,

`<L_i,G> = -2 d(i,p(i)) <= 0`.

Each stored certificate selects A=1 or A=2 actual fans. It supplies integer vectors gamma_a, nonnegative integer multipliers lambda_aTi, and symmetric integer offsets O_a satisfying `sum_a O_a=0`. For every tetrahedron T of fan a, the checker constructs

`R_aT = gamma_a chi_T^T + chi_T gamma_a^T + sum_i lambda_aTi L_i + O_a`.

**Every one of the 35,392 matrices satisfies `R_aT-I` positive definite.** This was checked exactly, without floating eigenvalues. The file's offset convention is unambiguous: each stored upper-triangular coefficient contributes twice its value on a diagonal and its value to each corresponding off-diagonal entry; the last fan receives the negative sum of all preceding offsets.

Weight and sum these identities using the actual `w_aT=d_aT/D`. The gamma terms vanish by the actual centroid equations. The offsets vanish because each fan has total mass one. Therefore

`sum_a,T w_aT <R_aT,G> = sum_a,T,i w_aT lambda_aTi <L_i,G> <= 0`.

On the other hand, G is nonzero positive semidefinite, and every `R_aT>I`, so

`sum_a,T w_aT <R_aT,G> > A tr(G) > 0`.

Contradiction. This proves infeasibility for that complete continuous escape-tree branch. Exhaustive coverage of all 4,067 rooted-tree orbits proves the stated **whole-type U>=2 theorem**.

The numerical locator only found the integer coefficients. The proof consists of these displayed identities, nonnegative multipliers, the complete tree enumeration, and exact positive leading principal minors. It does not rely on an optimizer's infeasibility status.

### 3.4 The decisive alternate-diagonal closures

Of the final plans, 3,708 use one shift-zero fan, 66 use one shift-one fan, 290 use two shift-zero fans, and exactly three use a shift-one second fan. Those three final certificates are:

```text
root 0, rooted-orbit index 575:
p = [0,0,0,8,5,1,4,3,6]
fans = [(0,0),(7,1)]

root 1, rooted-orbit index 1178:
p = [1,1,6,8,5,1,4,2,7]
fans = [(1,0),(4,1)]

root 2, rooted-orbit index 75:
p = [1,3,2,7,6,2,2,8,4]
fans = [(2,0),(4,1)]
```

These indices refer to the lexicographically sorted **rooted automorphism orbits**, not to indices in the unquotiented 3,600-tree list. The capsule reconstructs all coefficients, including these three, rather than leaving a final residue or relying on unavailable solver checkpoints.

## 4. A rigorous compact metric bound in all 84 affine charts

The exclusion above already works for every M>0. Independently, the inherited inertia theorem translates into a useful fully bounded version of the actual-area-gated global model; this does **not** assume that an affine chart has identity covariance.

For a maximal row triple R, retain the inherited construction

```text
X0 = U_R^T,
K  = X0^T X0,
Q0 = U X0 K^(-1),
det K >= 16/567,
Q0_R = I,
[-1/3,1/3]^3 subset P0 subset [-3,1]^3,
8/27 <= Vol(P0) <= 64.
```

All 84 maximizing-chart choices and ties are retained. These are inherited global bounds, not fitted boxes.

Let C0 be the **actual** ordinary-volume covariance of P0. The inherited inertia inclusions are

`sqrt(5/3) C0^(1/2) B2 subset P0 subset sqrt(15) C0^(1/2) B2`.

They follow from actual tetrahedral second moments and the Berwald inequality; their spectral consequences for a physical 110 body are the two eigenvalue ratios at most nine.

The contained cube has support at least 1/3 in every unit direction. The outer inertia inclusion therefore gives `C0 >= I/135`. Each selected pole is e_i, hence `h_P0(e_i)=1`. The inner inclusion gives `(C0)_ii<=3/5`, so

`I/135 <= C0 <= (9/5) I`.

Normalize `tr M=1` and put `A=C0^(1/2) M C0^(1/2)`. Its eigenvalues are those of the physical covariance, up to the harmless uniform scale. The two inherited ratio bounds imply

`lambda_min(A) >= tr(A)/91 >= 1/(135*91)`.

Consequently

```text
M >= (1/(135*91)) C0^(-1) >= I/22113,
M <= I,
I <= N=M^(-1) <= 22113 I.
```

Thus every genuine 110 candidate is represented in at least one of the 84 max-volume charts with the **hard reciprocal equation `MN=I`** and the explicit trace-one compact metric box above. Shape coordinates, B, S and metric variables are bounded, while `|D_R|=6 Vol(P0)>=16/9` keeps the actual-area denominator nonzero.

For an overlapping chart R', write `A0=(Q0)_R'`. The exact switch is

```text
X0' = X0 A0^T,
Q0' = Q0 A0^(-1),
M'  = A0^(-T) M A0^(-1),
N'  = A0 N A0^T.
```

Renormalize M' to trace one and multiply N' by the reciprocal normalization factor. All determinant area numerators and D_R acquire the same factor `det A0`; reverse the global facet orientation when that factor is negative. No chart sign, maximizing tie, or metric direction is discarded.

Rather than subdividing this bounded domain into boxes, the exact type294 matrices give a **uniform contradiction on its entirety**, and even on the larger domain with unrestricted M>0. Therefore the compactification is not being mistaken for an exclusion: the actual eliminated continuous set is every physical type294 realization, in every chart and every physical reciprocal metric.

## 5. Boundaries and strictness

Maximal facets and true edges are exactly the displayed cycles and edge list. Quadrilateral coplanarity and nonsimple vertices are retained exactly; they are not generically perturbed into another map. Nonincidences are strictly positive in the proper realization domain.

The escape inequalities used in the proof are weak, `d(i,p(i))>=0`. Hence irrelevant zero mechanics primitives and ties do not evade the certificate. No lower bound on individual tetrahedron weights, inactive slacks, or edge lengths is used. The positive-definite gap remains valid when some tetrahedron masses approach zero, provided the actual normalized fan identities and positive total volume remain. This handles limiting incidence sequences from the stated charts without an arbitrary clearance cutoff.

A collapsed object having a different maximal-face lattice is not silently reclassified as type294, and a lower-dimensional object is not a full-dimensional polyhedron. No exclusion of such a different type is claimed merely from a boundary label. For proper type294, the remaining continuous set is **empty**, not a collection of unsampled boxes.

## 6. Exact recovery and observed verification

The complete source and inputs are embedded below. The locator uses CPython **3.13.5**, NumPy **2.3.5**, SciPy **1.17.0**, Linux x86_64, NumPy/SciPy OpenBLAS **0.3.30**, one BLAS thread, and four fork workers. It uses the fixed complete plan strings; no discovery-time file is needed. Its log-determinant continuation has initial barrier 0.05, multiplier 0.18, at most 70 Newton steps per barrier, acceptance threshold 1e-7, 60 backtracks with factor 1/2, Armijo coefficient 0.05, positivity fraction 0.99, and coefficient rounding at normalized scale 10^6. The three alternate-diagonal plans allow 11 outer iterations; the other plans allow 10. Every proposed certificate is checked by exact Fraction LDL before serialization.

The independent verifier imports no builder or optimizer. It reconstructs the graph, automorphisms, all trees, all certificate matrices and their integer Sylvester minors from the literal data. Its stronger `--unit-gap` test checks `R-I>0` as well. The exact recovery capsule was itself executed, not merely assembled.

```text
type294_exact.json
2591036 bytes
4dfca8754813888b49e7a68e29bb9b45bb8dc5353b214d4f61a0a57b2b428cc4

build294.py
8016 bytes
b7495503c0b8bfc24e705ecf292b5a63d574e55964bc7902285cf1f30efaad1d

verify294.py
6581 bytes
f142c611eaafb1e1588c00da546246fe65d7587efb151fc82e3ba210babfa385

complete fixed-plan JSON, embedded inside build294.py
4090 bytes
c3276eb554f7428d84a1a4013fc5c64ca2846c1bda7b5468077d02cabbf31992

build.log
144 bytes
18c0509992b369cd7fdbf7d8ca8c54ce6b066285edbe6459367e855610c697d8

verify.log
436 bytes
1ca630ddb1d7b5658375f9962c3fdf365282cb3f9b074692efadf23727bb093d

recover294.py, the literal capsule below
10196 bytes
fbc634c1ebef62df5f0754daf9b801d244c6aef733d4ebbf5a90c1d0c6a43ad3

capsule_replay.log
1311 bytes
2859b8d0e552ea5f05f1aa705a995370e91a1e74aa221f7a435b7fd724e48242
```

Save the following complete unit as `recover294.py` and run `python recover294.py` in an empty working directory with the stated dependency versions. It expands both complete source files, reconstructs the certificate twice, runs the independent verifier, and checks all source/output hashes and byte identity. Alternatively, the materialized report in the supplementary archive can be checked using only `python -S verify294.py type294_exact.json --unit-gap`.

```python
"""Complete self-contained C32 canonical-type294 recovery.
Save as recover294.py; run in an otherwise empty directory with
CPython 3.13.5, numpy==2.3.5, scipy==1.17.0, Linux x86_64,
NumPy/SciPy OpenBLAS 0.3.30. No journal or external exact-data file.
The extracted independent verifier uses only the Python standard library.
"""
import base64,hashlib,json,os,subprocess,sys,zlib
from pathlib import Path
assert __debug__
B=r"""
c-q}NX?xm8li&AO$dgQvKoG=zSf0T)j!7^khD;8^Xj(`DaY(WxFxc_@_O0rcggBge-*=z=uuBph-PP6ARn^sXC{MqrOLMN}s)dZR
`K9*DclzfdpHuo@yG>|TK40Iqn@Z!N|EbYdJ}K{-N>2Gh;xygY-GynHo^OsgS0C9c-Q8rqTNmApKd~(?pONyJqR4fYi|&TYW#~(9
WWtM-k;<8@$hA#tx#rfDl2R(bNDBFuf!sQ}b>43DxGW6JXX~78=^SnFC$3I3ku&V23m13BJ-|hGJ;2cLJl*w8+wwTwBI;b%GF->z
JOCZ(+!SsWnTy<r_+)O6mpW&dbDgtYfS3dMoI^%4GS)du*EJaX-MU*^oWs@=;}cg88`C`w#+k+@=<qj=j!e_nWaMY29)hHomg%R*
#QAP9?tZt-g=4!uXM5i*SOGWFH=Jp4eB!p-?BF7m&Zirte|^_%T=o)T;`XMy*K+frz0)GpY%il*E7P^D0iYYo2`LfHqY_Uq6~qbg
CUa92O^}>#+jCDu0>#C0?wgKlk95y7t+D8BJn@0J7Cd|6BMbl{U3<Y9F06_2Hb8q7G;qY@t^y#3_&7%h(uLQE3~RXn76Gv3L~Y*4
bT+|Q`ka}YAfs`JfC}cjMW|poMbUJ1IaU;oSQ-a}W`O%1kf4~r$U!YXlx03IN_nv;M1w3RqbMPqBFhP?iwTB;PPyC7v=g`&G9d$6
0xSz(`Gh&PY*$af6rILRQ%?Nzb^&bN#$B`1mlMPrEA7IEY)iUOJ-bpdFO;&@UKYwXxekI|%L%nuu8^z*YMv`eqmofB7m89YH_GLV
f~pqErE;ZG&<iCpDwK4on3vRoUM^ILRL$peMzsiNE&z>gs8W^`O2sm%RHcz7<&Bb2%4uq~Ae9QLR#5ZVY*DXfE83`7Bt);2HMLO8
R`Xe-oGoa8=Bg(T23b)O^FtBtIk6~8^eHcv#T-0IVnM9XUJ3dNL-D)C!EcZgOVCq<_8dS~#1cH^;a-M&0s1P#;diUqlRXf!uJKR)
(wXag@TLm_?rhG$U2)Z;&pJLonhtM>#z3kKQ^ues4TWbALi0<vdC_lP%6zU^m9qJgm?&t*h*ZkOLPg3~DiyU*)yt$*fxW4!Ram2{
;+pftyqc2=TEQquBuk2AHK!JGmC>kxvOTX9<-{oM&iLC8C#%!K`NUWJ$yvu5wZ=E+uOA9zQgGboa#nb)T#t>7cIRG^caNPfmxYh-
){E=n<tX_^K2>ifi_eY6Y5GIH+8XQ4&6~g7vk!m&&Hpg3RPV3!&6m^r>2<f^p7vk;S^WLSrz^AH{(7?N=(&%sdnJ!@r|U13kNqDN
<Mp4<jUSTp;dv@K-Sa=EzdpZSp7!6guO3oQpD*&I+q_#@G@s7jznY)k3&k(hZ=Y|33;rx?m88y+e{=HcWO7L^TR%GQPR8Ek>2mZ}
_EYQC^W(S0$9(&BckDhiv|k&q1n<jv(bt4#@$_jVKTLa#+t12H@qJxAwHud??%wDAEZw%fSGONupYfk(v&Q+;*Y<}C`}+OKb-UZI
Y%bm056^rzYHjZ1$=U43m#6NhdXJQ^p0#Y_!S9UA!c+UCxlEosz5Z(cspWtD^F-^mu1`K(e-Tc*A7523_|3Q0Z~E7V(w&?B>&xTx
VfMy(e|~lH)HwUC@b{)Xdw-ce7k)Q3@6W#c{^=~~YTv#&jT^rA=H$0J|MlzVtCrh$J@Wg9)T428ng4ZC;3aEho&S2-nm+yU`1!9(
`{YORvDEwWbU!I{OK-9#pz*4VCNHDGfwpj5Fo`^~o*A`L#70f$K{14_d70}LuL`nU$X2t|rUYg-<4s7eSc1OHL|<#>SoeG$;1Z*J
u3Xa9VzFS9LEE%Sfk>o~h21$Sj!K0Q$yExak)&#*tQHHUO150qvbhmaRU<D|t2s0h?MA03qxH_rZK45<K+kte(+$ob7EeS^sKG|G
m%coJeHPzL*v^>-NAT6Cjcm(@Q&`8=sqFoVt1*PSAsd4!+hkKjfT%M1+Se_O2lU1uJA})OUQ)0P=?pVO=@M(K^ODFAr6uGPxCcHQ
y@(_vlPrCEVY|-6^cEgZsnztcJn)ta-b6h5cGow148OU>Uloulhq%562Fg6_#w7y6fe9yqHl+O;_6HWm(|sPg1&U^eO{0lz!bym*
(K(rc(@|TFd_Kv?+Q9u;`h=c{yu&DTa2TaZpiAP$@*Er_KBNkH!2rek(4J9nF_@N(V#^Vy5r}v%)aY8Kf%JCmC69gLcrYCbf#nPa
H+#>rjB5oJ)=-4RaZrTgm{0;7&<l-?Pknh$H1(LCLpNw}B^09X>bl3fw(UpihLZ{Pk-fBhIa?=09*ikLV<ZQLBk|(_4gtZ?Tflc+
8}D-+cAyH*0ON48Csr7Dh&Bb8509%veDxG%4Zwjr;mW759%z_G4JMU|BM;KjFj=iT0d07#`?hAwgOJMYgxJ0n6rGFB!Wwan4oq>H
t>H~JDWWX}feewM*dd(A)t!AvxtEfqy6viFpqg7I62fM=4@llBOq>_B`vEG&P#zB)yi+KOFQkKM&^^;hsvDZdgG0|#DB2uIo=H>A
m$J;jA>pVlvW!pE77aY#Wr{F-Nwt{DI2uo=7(p}W)>sgSzY^U*Z(X{=P$y<PD?&OonSj-SzX1=mQ#o4;X1gMDPv4Of8wv(WtO|Sb
VqGS75Reh>Edm!5S8z|$`)rt`{j=d)ZM(3(i;`k18cp=kjE4Y-PJuj-;boA(r^K-Cus7J{x`pqaqmNh<SZW2|pz)ElJSOPM4S5h+
aY`^eP}2pl!+L`<-2fXslhIfr|DZ*L7NKr=awAzy&61U^^bq_JWMz3Nz5(_)StwE|qNpDS0A91ap>QT=VTc9C8yM6V?5TOec5K}@
DKw+ar^M;t-0Lp!btH|MJ|aI32%zUl3TCZFTI|y;<S~Ifz-*S!OuqkunWwrw7^6Ir4<L-x7)1h)=5Sx2FyJK|^My>8oAS+MrG^i@
Zz5$CTo7!xNI^!nXojYDz7Q!>0{wwA61P+R9(BVUrsQ05WV1KW7@0m(ZNldWp|_<5C9t&;1UQcD;60Ic#H|3wd1G0kP+-G39h93(
OZ7Qr{n0JY+K=jZ&;?7Ay>aq!0LtKjBBbWS`aE1ZBgvHIX)Ra~TVB|S6l{C8OHGAK4HOQx_<hU>%)*W0Z5E)@su1p19s)Bk4Z2HP
Q_-6$5<z&I3y00^5vmp2Kq71mPt+Yxmh^O4T#z*#BTG5DMvHC^1}cPG1x5(<rVRM?jm}#_y|sP*iOyRBnsJH>7I`9@s74SD;WC<d
-r^<Q97G^PA;Lg$4(kg_Ko4j6urqKPgAHdp5St|o>l(%I;b61lnkeye*zi_;?%|S1fNCyUbFcvmY7f|By|dl_T1u)fmU1VJVqfFH
N8PnOz9ZDvgSj`9rMEmCy&f!<Lm71Ld<W>90m0w}LHBD|S53V7rndf>T|k;^FBpL)I}G6X$lyA&Lfu@)T_=*XL}o`UK}f|qV0k!i
a)E2+@ezR*>{R30jO)7iAZ)$KVX8-I4fP&(*eP(PW<paOwU;7EO+>!YnKdx5?Uek14x*c3yAh{*JNyvUG(a_tp&Fz=($ODr^ap09
R5LuFsYG3};Q<*+0>&W254zi_LAo`hE2ifWnUDCj=#!;5f$&Afvq}iPel+@2$U^Mk?AR7NH|6vieTp=UO#=G4Jr01WP(r^2v9hI)
cl2V6V^LkkR6!8STRNP=UT<Ofj@W_4TtlCTkP%=qnTyWvwb%}Auxg69@W6_Fq`TL&kfa0=i8)Q5nbU;09+>N)*k*$F-A(Nd0a-RF
1Mc-)_huXZBkR}KBi*5?p#Y$5T8;U*>AJSN&lb)|gB^_V1a6v1#{8WSW6UmRxX-c4X%373D7J+9=XRWWb1IVQEPY1ISwj3A(hmMH
tRyW5Gx{zW>HO!mNY<t&$r8Qi<XixJJpdSUt$>z@=2`%29E^)t1hc496J}9ik~aLMBSRx>h-2|u2#9B=j1lZ%)8A@!Xla=cU<x^t
EhaNkC7Cq+P-wATP|gP8!k}QQk`b$*nKM1g<3oNUNismxzr~dX+&K6Lit}wy>xi|^P`-vo_H@n~@rj~vC)6Uk${;-!rS$pl>tUo9
j?4t|O#~<r4lS@y3Xv0FDH0;}<`l!UAPkYIM=1c}VO(jN^aeo*VA=|K?)lz*fYXI@T*DJeDhLoMM+h{1<jU#s?@q`CY&gX|Nl!Br
Tqc_Z^P##rnXxl<E=!rZWr5oP8{{+_j<l={u{IDm0{|i*b1_q`qTKN<O}Ep)vW9P+@F_5fC?{nrr&1^<ZoQV*DKbwwb#OqL#F!Of
T!?%Y!$85I-+}_8uB2g{%0>zm0><;OzW54Y2}wCq+*-{*+-uqbldc21LT%3(ob8y9M_#}wWYKf%6dEIp+u@;y5ELJHpLny#2^UT1
TZ@6)FxP!_6A%LWY4C*&$cIE$O4O)VJ{SZ8eV%m-G;Y%8yYP+ki_7NKyX)5Ou<TGA#QHLH{tyxLGE~8-5&7m3R-%qzE#rxqs2^b6
_U&PnDAre8xH~y1%TCt`RyE8qswU^mi6wH96!l;Q1q6pVZHTV*G#WD-AxCrDTe><{Qn-aJOVS>vwsbH<A!VrtvFo9|9J?Ix+ZJ{#
&RicT7E=j2gx?Akhj^f&x(s-DqI$eBw~5cMf*^8*Gp+|U7>l5f7{V{%#0;U{(!oh7n@pAtMhvNnjbzOn`8<o}qKW0WPO<Yn@HNFS
n3M4$KFW_c^ENcB2U-iyq1G-4Y*ebQsFmI}1BLTpOn_<k+}2|P`_4P!NZ9qN@O+G=VZ?)IT&Pj>q1O<w5f%Zckj4kopKyC6pv+kJ
6^upnwa+K8#+DE=UE7}X1p(_f4m{Ry*SVS(umM^!Cc3A=W)$hH@hk#5vcVXdEiILq2kFA$#WD<dT;adKYo|)Iqebg@(9C+))RYBi
k%5~0WVrUDZeb=0Leapl7mZ!MUG;=#0H3;11p@6RKOU@xqM;48D8^xwX|nw3z!(a_++j{DrbAJ<9A#X?7A#b7HdCvh+5~60se$&G
{zk?^QlMB0Fw7iV3)C@IGzvRdMp^D&i(yR0ZEKlf@5Qx<RY=9u<Xp7?iaFB3OTX%gJ9#}B=#F8T+F<n*)D6YeG3^c05#L-vWHfa}
+KyVr1O>V(Rk9TkE?KcqtPW#{=0w%!b6typ)5MXuBkA~yIKq;xVWJK3<d`T`nWq_UZMkqf-WE|%%1qxdmsa$2;0p0=*OU2#2!Cn`
2n`b7zgwWJx<xbfG4<nFo?iTEb{-TnEGCKn+5ngUYn*)Iu<{FJJh<RSDC!1QMpN`5F+UlC#qD4OP@`g&+r<+paoOxQ?`~S1R<GZ>
h{}z3&5PSVns;B7M(0wwx@%nYTelshec4vJjb4w#ZN}w``DzX;S|O^tX7~24pAeJbVxbQ#y`oqITp_H1Dhiq>MM>0{nfh-1BK{Ju
bVr{Gw7{65WdViZ=t7v))7=cW`z1h~^L()B#ML-pr%T)oXIpdpVxVIO)n1RIbzs73?O;SW8yu~L>EUBky~jXqP0z0RR{Jvt#r2U5
ddLdaFIB$1jrX&%^?uR$|42FX|9egPf2rIX)us5*Bi8gW7%^6pTD?${S{)`DITaitJkSTLBL@SkO95UuX?|9k0tg{Q7!|0(1m%BJ
qf!~gDh^{L3fsgWmOu_mRa}%%RK-ygj?=Mw6)P?dyb>QGU~n^P4zBfK3wKz+at355Is-K-U=dLb3Rovm0c$rq%55`_u@fJs+H&34
**MSgu5Yl@w?!JOlQ{twUan`5`CQp6gB=l=w^U)uf2q0^3gcKk3JmCI7Ar`_I8GG^yN`$?;3XqsuRjpSDo8|gEJJ(9>G1a;la!iX
9Yx{{9$3xmVJNQ{u^}TLgdOSQ(MtQ_h^xj6lT0g|Q2S!8BZ>?eA5@)K{Rusbf07U_XQAH^1}M}6CM0CH<LroPr^Xi28&oV={o@FC
c4~1P_fG}6C}SKGxO22F7cC6EQ^$!G<?FsnCc5Slo;VPacoWljQTxyZj1~W*RpCgwOQ8SAqCA;mWuF89h)`e2cprFp+~7ma+f&2o
{ucl%`~n~@U`Fl=zaLl)ru2f}59}^B_ML#YnS&F`iUd20d=-6umNqb)^)`zIFvT2UyuJuFR-JRq6)5%$Bg;9QT@c(LE3vkik}`q0
h8;Di4fpDgM`ft8vQL_ECeR;OUzzsO3#%x{3zzJt$?CRzxnsi67vwbo=>!*z2EW=_R^$_%+fMhk*Xp<aXe#Yy<FeIxr+^oDdzTPr
q89MvMZJsHKDiepWgbG{4?-nbOR7O>OAU&ll>X`P5Ip?YZn^k1;z(GkivI$Hzz9}#g#mBhh9hG8A;h6=<7JdC8rq=Liu&?DueR=5
83zp#<-QaDNMQ#KOg>M=wT{FUMWT<phD$o7#tP>ZPUYNjG(?CAJ$ovXQ$~RoBmoW*DZw0AP>~05OK`McY#FgKSP*3&)RAzz`^5ES
%YZ`%HmXctQ<hIl$-7L#YBGSNc*|h*<Q)iBSEj>j02P*&V*q4L2_UK`J_^7WnuuW_|6&0elt$IvcqNpGhVfFpiT%c8vA~jaHA!ml
FIC;MT|PUY4P$RFn3jgIsqMxq)%we|YA$vt4Ctg-w~nx|`Zcyr<E{TzDLeYnnl_VECCQjl3txHmo|1%+U$H{(cG+{Xc)8jg{~cDo
Vd%E>&0d1qH@qCqG>KI^jcplx&xwdi;uDcUz3hu%mL#f>PofGr@u_weipk00m=~+&N8tY1MuxwYjI<;l2LzOp_y>&MQHyPDeH9km
8SSf=2QlTx!hBG2--F$l`ds7g4|9w3e52_G{92m0<JCYKMlM*;B%Dc%f`3j)?Cj)!H>VP~C%Ydm;zwdM>e@kV4-!F^ECDuHq6QJ#
!h9JvVw@Yc2N^GH2J-hY9pu#zj>Wzqf}IQ-?Y<7X_A_kQdvU!#2g|czA4KTE$eoNEb`cVNKm`sc{gQ6awnCf(%PmD<SNI<Il^Xrr
F_zcJTwnqXd?V_$ALIxEzyB~xu*+(O_BdYr79);}!e;cjj$HKkJxnxor4TDJU!uAI@lVoo=&@azaPazEJ`H=?!nsx;N|rBz<IuA)
`ktVGX)ch~Dp*Qs>=FmfhXan}Q7<bW-<{Nv(--zi*M1Umg$6*J?eA<*JYWbeCJKhr^o`*Z>YlD!GEEp$P~ka<%xD0Oox+ir_@xMK
FG_3nUa&K<DD9tuw4VlQ0WKP$Q}U^<J%j-ul3&9M{T}c^csY*S5j-$Nrr5TQnYWW#ABTZ?5MUiipFBt3nzG?CO||8MGjDF&v!(NI
W%u#aI+oyPsCJV4{&4$Q%3+fKD7i1>__thvxxqi9;oLe_tpLODa=JY+97cP8>Y^<Oy(|2lc0sRU5<V8D1T`bZxOg7HiIyLWgQF05
`_b}V9^*MCXEt4^0n|%&_R~XHP}&s%!0ah9R@Km)#?t+X;Y%lGc*4Y-dyziV5*)lRzV3MYXl=Ijts{Goesg^+j@a=kqKNZe%+gP8
jvnW)xIUP5nxLk&Q_pv8&;pkW|F;(yGtHzQIZzuW(hWv{MQ|=!)IM@BjS2Ym%u!D$vHhQ83A!_b)4CR?P})_wKsAuh`$Zc(fA;D&
yYYx0WLEY?6jbZjN23S@5b**IBBmvV{Uh;6Er`NKNt>V?anXPvw{_8Iqvz4;bU*c##;5-6&Fx+Hy4Aa3rH#f#v)^MyjVcERWR<IM
QZXUyU~076%H8cPxEf0T?o(4~UcPI>Q?seu-krC?@yG<cWI15M9)?!uve|9IrPEi=!9!^EdP?tW`;TU?-@IeP=~}s)M*psL(F{r~
7tOnV>k8J;Z}t+~ZzWz7VKiI6`3~^LhAW>st*hI+8@%_G?xpgs(WUe55z2D<5$mE{|8AC_5{z8wT{pVTo`R1zO{9DuU#Iyws1qP2
U=oKd?{9%b%F=*?z;o_h`}Q2BxX2fj4s>+yZvSXr?xFjSN=(oH_21uwnuh
"""
raw=zlib.decompress(base64.b85decode(''.join(B.split())))
assert (len(raw),hashlib.sha256(raw).hexdigest())==(14991, '291e7cfcbf8dd0629fc7ac5cb9281e303498ccd3a45b69bd0ca51c5408652860')
source=json.loads(raw)
M={'build294.py': [8016, 'b7495503c0b8bfc24e705ecf292b5a63d574e55964bc7902285cf1f30efaad1d'], 'verify294.py': [6581, 'f142c611eaafb1e1588c00da546246fe65d7587efb151fc82e3ba210babfa385'], 'type294_exact.json': [2591036, '4dfca8754813888b49e7a68e29bb9b45bb8dc5353b214d4f61a0a57b2b428cc4'], 'build.log': [144, '18c0509992b369cd7fdbf7d8ca8c54ce6b066285edbe6459367e855610c697d8'], 'verify.log': [436, '1ca630ddb1d7b5658375f9962c3fdf365282cb3f9b074692efadf23727bb093d']}
assert set(source)=={'build294.py','verify294.py'}
def check(path,name):
 b=path.read_bytes();assert [len(b),hashlib.sha256(b).hexdigest()]==M[name],str(path)
 return b
root=Path('type294_recovery')
assert not root.exists(), 'Use an empty recovery destination; existing files are not overwritten.'
root.mkdir()
env=os.environ.copy()
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):env[key]='1'
for label in ('run1','run2'):
 d=root/label;d.mkdir()
 for name,text in source.items():
  (d/name).write_bytes(text.encode());check(d/name,name)
 for command,log in (([sys.executable,'build294.py'],'build.log'),
                     ([sys.executable,'-S','verify294.py','type294_exact.json','--unit-gap'],'verify.log')):
  with (d/log).open('wb') as f:subprocess.run(command,cwd=d,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
  check(d/log,log)
 for name in M:check(d/name,name)
 print((d/'build.log').read_text(),end='');print((d/'verify.log').read_text(),end='')
for name in M:assert (root/'run1'/name).read_bytes()==(root/'run2'/name).read_bytes()
print('TWO_CLEAN_RECOVERIES_BYTE_IDENTICAL_PASS')
print('ALL_TYPE294_SOURCE_CERTIFICATE_AND_TRANSCRIPT_HASHES_PASS')
print('C32_TYPE294_WHOLE_CONTINUOUS_ACTUAL_DOMAIN_EXCLUDED')
```

Observed terminal markers include:

```text
ALL_ROOTED_TRUE_EDGE_TREE_ORBITS_PASS 1808 1800 459
INDEPENDENT_BAREISS_SYLVESTER_PASS 35392 MATRICES 4067 CERTIFICATES
INTEGER_CERTIFICATE_UNIFORM_UNIT_PD_GAP_PASS
WHOLE_CANONICAL_TYPE294_ACTUAL_U_GE_2_PASS ALL_SHAPES_ALL_METRICS
TWO_CLEAN_RECOVERIES_BYTE_IDENTICAL_PASS
ALL_TYPE294_SOURCE_CERTIFICATE_AND_TRANSCRIPT_HASHES_PASS
C32_TYPE294_WHOLE_CONTINUOUS_ACTUAL_DOMAIN_EXCLUDED
```

## 7. Exact remainder and continuation

Relative to the accepted full-type baseline in the supplied journal, the newly surviving type set is precisely

`{t in Z : 0<=t<=295, t not in {192,294}}`.

That is **294 types and 21,660 canonical joint-root orbits**, with each remaining orbit given by that type's `joint_root_representatives` in the pinned catalogue. The present result removes exactly the 15 literal type294 pairs listed above and no root of another type.

The separately preserved map295/U7 theorem, if incorporated with its own complete capsule, additionally removes exactly `(295,7,0)`, `(295,7,1)`, `(295,7,5)`, leaving **21,657** joint-root domains. That is separate preserved evidence, not a new immutable result or a new computation claimed here. The current journal explicitly records its status.

The useful continuation is to reuse the exact uniform multifan contradiction before attempting bounded-domain subdivision on another type. In particular, alternate diagonals of actual nonsimplicial facets should enter the fan list explicitly: they supplied all three final closures here. The same proof engine can be used inside the bounded 84-chart model with `M>=I/22113` and `N=M^(-1)` for branches not closed by a uniform index certificate. This handoff supplies no exclusion of those remaining domains and no claimed feasibility of their complement.

A supplementary complete materialized certificate and source archive (`C32_TYPE294_WHOLE_ACTUAL_U_GE_2_V1.zip`) is saved in Library as `/C32_TYPE294_WHOLE_ACTUAL_U_GE_2_V1.zip`. It has **1,132,413 bytes**, SHA-256 **8ab3f88a750fdf293a28590c6452f5315c5b60e202f35ca5f1bacb5709e2e543**. All nine archive members and the eight manifest-bound payloads were checked after packaging. The inline theorem and complete reconstruction capsule, not this link, are the recovery authority.
