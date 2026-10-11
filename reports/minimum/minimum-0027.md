# minimum-0027

Historical AI scientific report · saved 2026-09-08 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# C32_TYPE53_ROOT3_ACTUAL_TWO_APEX_EXCLUSION_V1

## 1. Whole-root determination

**The entire unique-unstable-root3 realization domain of canonical C32 type53 is excluded.** For every full-dimensional homogeneous convex realization of the specified face lattice, evaluated at its own ordinary-volume centroid and in any positive-definite physical metric, vertex 3 cannot be the sole strict unstable vertex. This includes candidates with weak escape equalities or degenerate equilibrium primitives elsewhere.

The new finite certificate closes **all four** Hamiltonian paths left by `C32_TYPE53_ROOT3_FOUR_PATH_FRONTIER_V1`. Together with that starting theorem, the coverage is now **2,626/2,626 rooted spanning trees**. The automorphism group of this labelled type is trivial, so this removes **nine complete joint stable-face/unstable-vertex root orbits**, namely `(s,3)` for `s=0,...,8`.

This is a whole-root exclusion, not a bounded search, an unsolved necessary system, or a new attainer. It does **not** exclude canonical type53 with a different unique unstable vertex, exclude every C32 type, or prove `C_min>=34`. The inherited bracket `32<=C_min<=1374` is unchanged.

The decisive object is small: **56 rational positive-definite 9-by-9 matrices**, fourteen for each remaining path. They use just two genuine integration apices, **3 and 6**, and only the eight weak tree-escape inequalities. Both complete actual volume decompositions belong to the same body. Their opposite auxiliary matrix terms cancel exactly.

## 2. Source authority and the starting theorem

The frozen main attachment has 2,776,300 UTF-8 bytes and SHA-256 `068aac87bb25a759cf3db97a83f7aaa29ecedbf14f33c5fc06d89bec87ff3eb5`. The immutable authorities are:

- `minimum-0009`, SHA-256 `6f905a98d5d84d11e1369aebb34643ad59248a2485b95270c59bb52c48b92326`, **RAVEN_C30_CONE_FRONTIER_V1**. Only its generic physical cone theorem and exact source machinery are imported; its historical C30 counts and bound are superseded.
- `minimum-0023`, SHA-256 `e98bce6278e66a9d3f6c8f0863d55e65cc1a1ebb3c239742c782107c5cc61815`, **C32_COMMON_MASS_VARIANCE_KERNEL_V1**. Its actual-apex moment identities are used, not its separate finite control or a substitute polar centroid. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

The exact type binding is the following ordered maximal-facet list:

```text
[0,1,3]; [0,2,4,1]; [0,3,5,2]; [1,4,3];
[2,5,6,7,8,4]; [3,4,8]; [3,6,5]; [3,7,6]; [3,8,7].
```

Canonical53 and the previously used `C32D026` have the identity vertex and facet correspondences here. The sixteen true edges are:

```text
(0,1),(0,2),(0,3),(1,3),(1,4),(2,4),(2,5),(3,4),
(3,5),(3,6),(3,7),(3,8),(4,8),(5,6),(6,7),(7,8).
```

The accepted starting theorem excludes 2,614 trees by the old generic cone predicate and eight further trees by the exact physical forest certificates, leaving precisely:

```text
p0 = [2,0,5,-1,1,6,7,8,3]
p1 = [1,4,0,-1,8,3,5,6,7]
p2 = [2,0,4,-1,8,3,5,6,7]
p3 = [1,4,5,-1,2,6,7,8,3].
```

All indices are zero-based. The root entry is `-1`. Their leaf-to-root orders are, respectively,

```text
4-1-0-2-5-6-7-8-3
2-0-1-4-8-7-6-5-3
1-0-2-4-8-7-6-5-3
0-1-4-2-5-6-7-8-3.
```

Every non-tree true edge has both directed escapes strictly negative in an actual candidate. That consequence is preserved, but the new certificate is stronger: after reduction, its multipliers on **all chord signs and all separate norm-order inequalities can be removed**. The eight tree inequalities alone contradict the two actual-apex moment identities. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

I reconstructed and ran the existing frontier replay in this turn. It reproduced `type53_root3_frontier.json`, **19,458 bytes**, SHA-256 `4815ddae52600fbc09e7e7b5a8993a4280de85d028c4eb43a2bae94f23899f3c`, and the markers `EXHAUSTIVE_TYPE53_ROOT3_TREES_KIRCHHOFF_PASS 2626` and `EXACT_OLD_NEW_REMAINING_PARTITION_PASS 2614 8 4`. The old driver was 4,215 bytes, SHA-256 `f35f1c5010909dd450b798c88ff1f32c155348eca99ec45d5441f6cbf3598332`.

**Authentication correction.** The earlier export-level caveat for the mass parent is resolved for this attachment. The 45,639-byte Markdown without its terminal LF has the previously reported SHA-256 `7924c974570cac1f64254eaca90b4a0e7337f58f42cabe4237c62e1a55458e19`. It is not the immutable JSON envelope. Restoring one terminal LF to that `result_markdown` and serializing the compact UTF-8 v2 JSON envelope gives **46,441 bytes and exactly the advertised mass-parent hash**. The Raven parent similarly reproduces its advertised hash as a 44,043-byte compact envelope with no terminal LF in its Markdown. No mathematical incidence or class conflict was found. The optional complete authentication source below reproduces both checks.

## 3. The exact continuous-geometry certificate

### 3.1 Physical moment identities

Let `x_i=v_i-g(P)` be the nine vertex vectors relative to the actual uniform-volume centroid. In arbitrary affine coordinates let `M` be the one physical positive-definite metric and put

\[
Z_{ij}=x_i^T M x_j,
\qquad
D_i=x_i^T M(x_{p(i)}-x_i).
\]

Thus `Z` is one nonzero positive-semidefinite vertex-index Gram matrix, not independently chosen primal and polar metrics.

Use the following complete physical tetrahedralizations, in this exact order:

```text
apex 3:
(3,0,2,4), (3,0,4,1), (3,2,5,6),
(3,2,6,7), (3,2,7,8), (3,2,8,4)

apex 6:
(6,0,1,3), (6,0,2,4), (6,0,4,1), (6,0,3,5),
(6,0,5,2), (6,1,4,3), (6,3,4,8), (6,3,8,7).
```

Each is obtained by triangulating every actual maximal facet not containing its apex, using the first vertex of that facet as fan anchor, and coning to the apex. Convexity makes their interiors disjoint and their union the body: an interior ray from the apex has a unique terminal point on a nonincident boundary facet. Triangles of incident facets give zero-volume cones and need not be included.

For either family `r=0,1`, use its **actual determinant volumes**, not free mass variables:

\[
d_{rT}=6\operatorname{Vol}(T),\quad
\mathcal D=\sum_Td_{rT}=6\operatorname{Vol}(P),\quad
w_{rT}=d_{rT}/\mathcal D.
\]

For a physical affine chart the common Jacobian cancels in these ratios. With `chi_T` the nine-component incidence vector of the four vertices,

\[
\sum_Tw_{rT}=1,
\qquad
\sum_T w_{rT}\sum_{i\in T}x_i=0.
\tag{1}
\]

The second equality follows because a uniform tetrahedron has centroid one quarter of its vertex sum. Both equalities refer to the **same actual polyhedron and actual centroid**. These are precisely the parent’s physical, rather than independently assigned, mass identities. :contentReference[oaicite:4]{index=4}

### 3.2 Two-apex cancellation lemma

Write `sym(u,v)=(uv^T+vu^T)/2`, and for each nonroot `i` define

\[
A_i=\operatorname{sym}(e_i,e_{p(i)})-e_i e_i^T.
\]

Then `tr(A_i Z)=D_i`. For each path, the capsule supplies two rational vectors `gamma_0,gamma_1`, one symmetric rational matrix `K`, and nonnegative multipliers `lambda_{rT,i}`. Define

\[
Q_{rT}=\operatorname{sym}(\gamma_r,\chi_T)
-\sum_{i\ne3}\lambda_{rT,i} A_i+(-1)^rK.
\tag{2}
\]

**All fourteen matrices for each path satisfy `Q_{rT} > I_9/2`.** Their entries are exact rationals. The generator reconstructs the integer matrix `4 Q_{rT}-2 I_9` and proves all nine leading principal minors positive. A separately written verifier reconstructs (2) as a scalar quadratic polynomial, proves positive definiteness by exact Fraction `LDL^T`, and checks every reconstructed entry against the first implementation. Across the four paths, that is 56 matrices, 504 positive leading minors, 504 positive LDL pivots, and 4,536 agreeing matrix entries.

Now assume all eight proposed escapes are weakly valid, `D_i>=0`. Multiply (2) by the same physical Gram matrix, take traces, and average with the corresponding actual tetrahedral masses:

\[
\begin{aligned}
\sum_{r,T}w_{rT}\operatorname{tr}(Q_{rT}Z)
&=-\sum_{r,T,i}w_{rT}\lambda_{rT,i}D_i\\
&\le0.
\end{aligned}
\tag{3}
\]

The two linear moment terms vanish by (1). The `K` terms cancel because each physical decomposition has total mass one. `K` is an auxiliary vertex-index matrix; it is neither an independently varied physical metric nor an assumed material covariance.

On the other hand, positive definiteness gives

\[
\sum_{r,T}w_{rT}\operatorname{tr}(Q_{rT}Z)
>\tfrac12(1+1)\operatorname{tr}Z
=\operatorname{tr}Z>0.
\tag{4}
\]

Equations (3) and (4) contradict one another. This closes each path over the entire continuous geometry and metric domain. The certificate does not leave an unresolved common kernel: its shifted matrices are positive definite on all nine index coordinates.

### 3.3 Completion of the root argument

At a nonroot vertex which is not strictly unstable, at least one true neighbor satisfies `D_i>=0`. Along such an arrow,

\[
\|x_{p(i)}\|_M^2-\|x_i\|_M^2
=2D_i+\|x_{p(i)}-x_i\|_M^2>0.
\]

Actual vertices are distinct and the physical metric is positive definite, so weak escapes cannot form a cycle. If 3 were the sole strict unstable vertex, selecting one escape at every other vertex would therefore produce a spanning tree rooted at 3. The starting theorem leaves only the four printed paths; (3)–(4) exclude all four. Hence 3 cannot be the sole strict unstable vertex.

This last step, together with the independently replayed starting theorem, is the whole-root determination. The new standalone capsule reconstructs the **new four-path closure**; it does not pretend to regenerate the older 2,622-tree certificate without the already supplied parent capsule.

## 4. Actual cap planes, complete metric domain, and boundary strata

An explicit global affine chart makes the mass geometry transparent. Every strict realization has an affine representative

```text
v0=(0,1,0)       v1=(a,b,0)       v2=(0,0,0)
v3=(0,s,t)       v4=(1,0,0)       v5=(0,0,1)
v6=(x6,0,z6)     v7=(x7,0,z7)     v8=(x8,0,z8).
```

The basis `(v4-v2,v0-v2,v5-v2)` is nonsingular: the two distinct maximal cap planes meet in the nondegenerate edge `(2,4)`, and vertices 0 and 5 lie off that edge in their respective caps. The side quadrilateral `[0,3,5,2]` forces the first coordinate of `v3` to be zero. All ten displayed shape variables are positive in this orientation; full realization additionally requires the exact supporting-plane and strict cyclic-convexity inequalities. Those are not replaced by a rectangular parameter box. Concretely, for every listed facet `f`, with `n_f=(v_f1-v_f0) cross (v_f2-v_f0)`, require exact coplanarity of its vertices, `n_f dot (v_k-v_f0)>0` for every nonincident vertex, and positive in-plane turns for every cyclic edge against the other facet vertices.

The two root caps are **exactly** `z=0` on `[0,2,4,1]` and `y=0` on `[2,5,6,7,8,4]`. Put

\[
L=a+b,\quad
(h_0,h_1,h_2,h_3)=(x_6,z_6x_7-x_6z_7,z_7x_8-x_7z_8,z_8),
\]

\[
H=h_0(v_5+v_6)+h_1(v_6+v_7)+h_2(v_7+v_8)+h_3(v_8+v_4).
\]

Let `D_0` denote the common coordinate-determinant sum; physical `6 Vol(P)` is `sqrt(det M) D_0`. The common Jacobian cancels in the masses and centroid. The genuine common determinant sum and first moment are

\[
D_0=tL+s\sum h_j,
\quad
4D_0 g=D_0 v_3+t(aL+b,bL+a,0)+sH.
\tag{5}
\]

For the root3 fan, its six determinant masses are `t, t(L-1), s h0, s h1, s h2, s h3`. The complete eight masses for apex6 are generated directly from its listed tetrahedra. The symbolic source below verifies **identically in all ten variables** that their sum is the same `D_0` and that all three first-moment components agree with (5). It also checks all prescribed coplanarities. This is an identity audit, not a sampled substitute for the universal proof.

Any physical metric is an arbitrary `M>0` on this chart; its reciprocal polar metric is exactly `M^(-1)`. The proof covers the complete paired domain `{(M,M^(-1)): M>0}` with no bound on eigenvalues, condition number, shear, aspect ratio, or shape parameters. It uses no polar-centroid assumption, no independently selected polar metric, and no substitution of incidence masses for polar-volume Hessian masses.

**Weak escapes and norm ties.** The certificate permits `D_i=0`. The nonnegative multipliers need no strictly positive arrow margin. A Hamiltonian weak-escape candidate nevertheless has strictly increasing norms along the entire path, so norm ties cannot invalidate the tree reduction. The new four-path certificate also remains valid with any chord primitive zero because no chord inequality occurs in (2).

**Coplanarity and integration diagonals.** Both quadrilaterals and the hexagon remain actual planar maximal facets. Diagonals such as `(0,4)`, `(0,5)`, and the nonedge hexagon fan spokes are integration devices only; none is supplied as a mechanical escape. Every `A_i` uses a checked true edge. No planar four-neighbor ring, arbitrary independent tetrahedron mass assignment, or general-position hypothesis is assumed.

**Other boundary strata.** The new matrix argument works for nonnegative fan masses, provided both decompositions retain positive total volume, their common-centroid identities, and a nonzero Gram matrix. Thus vanishing individual tetrahedron weights do not defeat the four-path contradiction. The same algebra works for nonzero semidefinite metric limits. A zero-volume body, a collapsed vertex representation which changes the face lattice, or a singular physical metric is not an admissible full-dimensional realization; no additional global theorem about such changed combinatorics is asserted. Degenerate stable-face or edge-equilibrium primitives do not create an exception because the exclusion uses no stable-face or saddle assumption.

## 5. Uniform quantitative separation

The certificate gives more than nonexistence of a zero-margin path. Let `T=tr Z=sum_i ||x_i||_M^2`. For **every** actual realization of this type and each of the four prescribed paths, at least one of its selected edges satisfies

\[
\frac{D_i}{T}<-\eta_p,
\qquad
(\eta_0,\eta_1,\eta_2,\eta_3)
=\left(\frac1{1017280},\frac2{43113},\frac2{138379},\frac2{1134269}\right).
\]

Indeed, put `alpha_i=sum_(r,T) w_(r,T) lambda_(r,T,i)` and
`B=max_(root3 tetrahedra) sum_i lambda + max_(apex6 tetrahedra) sum_i lambda`.
Then `sum alpha_i<=B`, while the exact trace identity and the shifted-PD bound give `-sum alpha_i D_i>T`. The four `B` values are `1017280,43113/2,138379/2,1134269/2`. This establishes the printed gaps uniformly, even along unbounded shape or metric sequences; it is not inferred from optimizer residuals.

## 6. What was tried and what actually supplies the proof

Single-apex common-direction searches and direct physical-coordinate searches did not supply a conclusion. The successful change was to allow opposite vertex-index offsets for two decompositions of the same material body. A first numerical locator used all nine apices; removing seven apices left the pair `(3,6)`. Removing every chord and norm-difference multiplier then left only the eight weak escape forms. Rounding the resulting coefficients to half-integers produced the literal exact certificate below.

Numerical proposal generation used CPython 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. It is not a proof or reconstruction dependency: the printed exact coefficients plus the complete exact generator and independent verifier reproduce the finding without any numerical optimization. The SDP-to-exact-certificate strategy has published methodological precedent; that literature is not the source of this type-specific theorem or the stronger inherited project bounds. No historical-priority claim is made. :contentReference[oaicite:5]{index=5}

The result is supported by two independently written arithmetic reconstructions, not a claim of external peer review. Within the stipulated starting theorem, **nothing remains unresolved in canonical53/U3**. Other unstable-root domains and the global minimum remain outside this determination. The useful continuation is to remove these nine joint-root orbits from the working frontier and apply the same cancelling-offset two-apex test to other surviving roots before resorting to larger common-kernel analyses.

## 7. Complete deterministic recovery capsule

The complete source bundle below contains all four executable sources, including **all 700 exact integer coefficients**. It is a lossless encoding of the source, not a filename or hash standing in for missing data. The decoded main source contains four groups of 18 direction coefficients, 45 symmetric-offset coefficients and 112 nonnegative multipliers. Every coefficient is divided by two as specified in (2). No numerical rediscovery is required.

Save the decoder as `unpack_type53.py` and the complete following stream as `type53_source.b85`. The required proof replay uses only CPython 3.13.5 and the standard library, with assertions enabled:

```bash
python3 -S unpack_type53.py
python3 -S verify_type53_root3.py
python3 -S independent_type53.py
```

The optional all-shape determinant replay uses SymPy 1.14.0:

```bash
python3 verify_type53_masses.py
```

The optional authentication source is also included. Its command applies to the exact supplied frozen attachment, not a journal with subsequent entries appended:

```bash
python3 -S authenticate_parents.py 'research-journal(20260908-122010).md'
```

The whitespace-free stream has **9,505 bytes**, SHA-256 `9556d857fe13cc71ef1569598ee28957a6650420c89a6bd1ef55b54033a132e8`. The decoded JSON source bundle has **19,087 bytes**, SHA-256 `497968c834f7fca436928fb7dc9e1a24235b24173847ef59438d515987941769`. The decoder has **1,281 bytes**, SHA-256 `669e6b7f9a142f4732e667b5bdc2b0b7aba8184757c8b466a88398b8c3a2b8cc`, with UTF-8/LF and final LF. Individual source pins are checked before writing any source.

### 7.1 Complete decoder — `unpack_type53.py`

```python
#!/usr/bin/env python3
"""Recover all four exact sources from the complete inline Base85 stream.
CPython 3.13.5, standard library only. Run with assertions enabled.
"""
from pathlib import Path
import base64,hashlib,json,zlib
assert __debug__
PINS={'authenticate_parents.py': [1194, '06eb8b4e9824acee6302e6be36b422f9dfe08bf7063882f911c7be1f80749cc1'], 'independent_type53.py': [3478, '41d1ec2fe802211a3987c3b0525f35da9268ebfb75c8f7e8cbf580e6ddd25887'], 'verify_type53_masses.py': [3083, 'b5cbd03934ff0607bd5a295ec5227a274a9f1aff1feebfbca288632485b19866'], 'verify_type53_root3.py': [10791, '45476380fa379f8159f632be634f937f6365d2e65f708e783e12dfa3ab926159']}
s=b''.join(Path('type53_source.b85').read_bytes().split())
assert len(s)==9505
assert hashlib.sha256(s).hexdigest()=='9556d857fe13cc71ef1569598ee28957a6650420c89a6bd1ef55b54033a132e8'
r=zlib.decompress(base64.b85decode(s))
assert len(r)==19087
assert hashlib.sha256(r).hexdigest()=='497968c834f7fca436928fb7dc9e1a24235b24173847ef59438d515987941769'
S=json.loads(r)
assert set(S)==set(PINS)
for name,text in S.items():
    b=text.encode('utf-8')
    assert [len(b),hashlib.sha256(b).hexdigest()]==PINS[name]
    Path(name).write_bytes(b)
    print('RECOVERED',name,*PINS[name])
print('TYPE53_SOURCE_CAPSULE_RECOVERY_PASS')
```

### 7.2 Complete lossless source stream — `type53_source.b85`

```text
c-qZek8|3{lKxlpoT@Xj1<~lYoTsf~ZT#XF8#~6y+g;#P0)#Ca1dD`YXKVlW>#s*(A#jr0dv|r-T|m-IPf!2&x?3}|f9yre{4P%O
WEkafIFA<eJ8R6J_m1}7{O#>BTf7}4>DxGcROZk5-7GbGX>SkzT+Z`kmPQk$M1XE6v$2xjC7BXsS#q0B>B)Ykj2E-7ajM+UmJ4)=
pXReg-sq*DvgkHGDo88!j`9jO$|BC<XfeF27bI$iZaBKHdv#$Ly3p0ebks}Rvs{UkQ9O^+QJfB+B{Q*-#$Ra6;bfVC!(qJ0lQ9p`
Sk0!F5{px19_4qFWS}HdFsNM7WiKr*?xGCOwEJw9YT0wvOKFNkN(sYJJXqd_p%SGdWfG?~dfJE<w~uNN7`=26eF;EmeY-3AYGV;c
qj2z?$5~B%mj%?QF^Y$?QC!<!=Ht4zuhPgt)>tGom#5nP8|AwBxz!GjO+7rmY`4PG>&y1dS?fCdEYS9z+7?ZFz4Xl+Vjj{XJ=})B
fBiaqnl1kEn{jd6zFD5u^}7$F`2KibOQ>fQWZmTGzTa46`68Lu=+=O4m4`ky4I1>~;<6oHG&`N}bMyMF**<QCA6nP#);Y6q^g`ee
EbNm^XA32brm>dCPq~(AcS@2f-CnBH_QBRXyEkSh=d+3DMbm%Y{eD@$^Yy#?$-Wk8mZe*!w(pF6-Hv>3WRE;+Bt$Gs$B*K{z_c98
j7GL^SYAZ`*#qA;TzzQ!gMn=fEpOl(rs3?X+IqOxr7+NlnkBUT*!Kp**fCr$cAUr`nPX?@jdjm4N46b1_HZa7fzgMC>ARLObUj1p
?vNfh!V~ts+CQT4=x-F|Q2<kEjF!`RRvRV5y!IF`V1a?5kv%Ubc{q(052M+aG=P9qEl#uLA`YW$m?XhzG|6Hui^&V3e74Af+P+5r
9PO)WgNz%NqRO!fJA~z7ShBj5O|h`pMs^n&wj-Z4?&7CWavNuPjoRHw0&~)IUfXZ|(mcKi&n_-L-86qbZ-t+Y@Tz&;YTtyd_UG35
<yDKWJDq)vbxP`_@r$niy!>?CZk~rf|9aEvgq`<I8gO3&M`YNlR^bHq%8U@5Y%!Eh5{Bbs5{F^MLyB=aG|q8LQl>6jlyR>@c~9Ge
9ZO8e!~A(3+vblT+}TSnWf2u<w;&%)$;_8S+<2!PUrFpT8^UbZnv&%s0LUzzJQKKFFG&;QJYFcI`egiEj2<p#vm87$l#^MUDJkJr
fii%r+c=FeV0tUNCGp~ifQp}t7ZJ0Tt)870H^@ws)17FxjbtUz+Amnnzs$mD9zTU;_(bphO--$dt&|@Gmf?8o+ut#TAlM&yLuY6W
obh1n#Eut@t+6q1Mvm*7hBX=s%Nd))*z;pU_Xfsr<V3=@bw3*Fqu6)sXdn2+t~Z%Qql|}G4?pPcNAqMDXZ!si=$e|-XIG)yr03Z*
N#SdFW~}aKcgZ;C)<QG-z4Wws-0B3~uC58q>}&LGXqG1Um#Nv*Mx&M%KQrjs(Ok{btiC3Fjs9p@OY`V44X@e!?GhvS_B6LoV@S8d
D2ApJjk=)0Bq6gPuj8i2BhrHsb)t_>R^>T&VoJuEQok&gaa2f!C%Bq@5rc8RV2XT|V(>5yC-LYuUX&%h+hC><MTMuL`7V=zcGBz%
fn(6^zf*>@WlAm+=rVxJlaV$=;E2=Z6n+uch_8|r5_4*Sx*wpI{(-NcV~9?RD7}qqz6!d_MK)uyXo?m|xy8|o1o7<t<yoR_JmrD9
NxysF4?fTb{R~cP!|wiv{eD*t($@_2o&0$i2-!7H%0n+S$Yyg|Y>rhv#%RMTsj!fYl@*Ec5rGon#WLP(QkjQf*c_{MQJoI+7w172
6tywQkUsAD<50j%s*T?$KQEKXh~X+5Mw4iv{JxAvK&_!NpG}_OO9YoRcABKCHd$kv5*i18{JH&L6w?GpBa;4u_PC2-{5{0aLB5<%
;u?uMk4H5$S5=A^M7B#$`vHD6ZsWX0SK4V!SJlJEZDQXthibbAv?FmHt=MDjACvYMFb2}Sx_f{JEvaZ6AY!m%vQPG38+H;+rH!4_
C^^~Q1Dn_iYNP2-E90vENgfl8+E9DGC>*&<p2hsu@$BCql6AY4TxtSVx(EVYi7A;;$nXx>a~}HYx4EsKlC|!X;{~}mw7A2?x9{wp
6x)dQh?Z;|NghuLhF+Q8g=9FmpbxnEBj%I@!GoOB<6C2wdz6!h^ON)c%rzQ%GMRme309w#@p4klC3g76InR~Gx>qZ%T+BAvgt!yJ
&%dt6QNUA8`t@u%t)0th9~>A5C-hxWa-zPbKxvVqpY(Spjc5)L)JE#-hEs;wL!rIO9E+m>+uDWvQSf=se6IN2&8+%%v`x3*HJVIn
7X_XN<*A=Yx=eq|$ko^R+$HlZ{q5*a_7H5u)@~6B`>*m&T@a)5I|OL*XAawZlkf@m=<Aykw+_}*=Wd+s#G@i;@Au`yfB#&IfWI~o
lt-8cCZQn|(SO=xGzmvZbc@V8=#r<@o|rfXy_5bfx_LqY_gx{kb?hxBOd&WB);j4~B^rV4yp--``Kx%;OJ~bGsFiBDf_DueC#0y7
1viW3E2Ww&h07J&Mv_#nOlY>N?C8saFsVq7X!Msl>#Tj!x@yq}6=j{{=6Ulvyt+L9wS9SUM%7odeG;BtQxSJYg*u^5QLYv9)ck|u
*KT^v^YhTMO@~VSo9nY*sOY0Fs^;kO_`M|c((&}{yrq0=5}a#*_iBlTd;gck-)7}Ch3<do1y^%2sT1LOtWYLfpHCu6V@5Ga4@Cl@
dV={Tc@k&ulu8lUd7fT9E21H+hTix~FPPRhv*+pj8Kqn2mG@1ZMi>_F6~d6JCpjwBK#?}kGA-Ah9PO*4J-OOfS9|ibuU^n;5Y@qK
lGXMjWuRnAt~@!)S4Vkrm9MVy<SAeI_0v_*?KCbJ2x^b)cpNjkHDoQis?{(AzICcM<TnjS-$Gu$iW=NOP($KPC+_ge#V;4XJpA%h
q@AaKxz752jrAMJ;cL8@Wi^v{Sxa{{<HlW<N5hBORoCj*uevna6{W?iU$*?EHpn7Sv<g|P$Yi|;VQD~}$6d;w>-g6D)O<+eWqjKx
-QEBxpmL`XKg~(IHG-U3PVJMI#wyaOHRg_~^BvVqtmT6zxBlcDe1)zLp1k^#d+-$+r`f*e$X2_%J78*uSA^=U(z`p2@}YZ`XnjrQ
wYyB~)<~G72oflLl2GZB1gp}}+HW-6Nsu4ZqQilDm>q!VT}C(C!O6i@*X$qW2Wy+@Mn$`UHYk2Yn%+mh_q`O^&tjBu$^u4K#SB+L
g$Q$c{7OyoBJOo1#II3EB(D~7r2?o3X*~YB=?w3wEB3JJpEJ=sD<vkQV6C8f)m{#|g|@)bOOlr7U2)W38B8f~jb37)S}<}Lj99R&
sS*V#{*tMzxj^etrq)kj9IsoGBoFr5^s#A3QbOj6wL&`^@fkA;SQ`|a7tviz^<I!?S_u`ym)b82CJCYNG@92aa%;q%3gT~+=F8i(
1korV7Er$~W)rHavOH5}i-h=;>j}WP`79%#edIS|OO%rZiuck-jMK&25xgJiG_DKEq-smuxTY5R<{eWrN+4B!;_{Qy9lzR{00$<N
Ee8RM2Cmb66><9-_{8i#2HnR7^~y+PgBM7>>hH#nj|F~w+{BNM1%7;d4L>Aoe5AZ}-R38KyHF#?d02Z*$>a$SlmZXN<ZooShvV*%
*r-moMx){GF<eq&^P#x0G5T03kIUer%ITBQF?-VXj&>L_!XZWT+FYB=hS2>V$O<3Tqeo>eOp@%M>Wh$n+AfUwwNfz>Ui|Ge-+jpS
Ru5|Jx0EHHs3nrU^cT`&{Z@Y&^do7o75q_s7eP}~OGx!i;r`i6KLy=nJD&!=(d>UANwTDWfuM1v{#{qLlI?Hi>O^W6i`2cPzPt@I
LGRN#C;p`V#OqiwG7@R;g};VNs$Zi4rEHIQA2*D%;FDG)M$f_i&97H2%DIqOcHTFyS|O#TpD0hg`PXGgm%qrxq%&lnXE#VSKa2fJ
*072a#kY16K;dgdBeiH_O4-Aca2SK7WV8u8_+GWv+BDTF{lcTe66S=(>^3P$7gpt~@p3sJ<?`>S2BKlUBvycK;Y)hCt0<7~w2Qp>
MZU+)tMK^p>b%)*UZ36k$^}8OZg<kUX<c8OwVRabf4)5bbkVA&^h}2G{;Ts(ov?NGkM}n#eL+p69Z<V@f8A<@r)SrloABcD0`HNk
bUIWv9N&b6@~@kyMu^BI6%*|nzQO|L&Gn_MPr~*k4RmwUJZrbE_q9*EYm9G+=Ksw))9yu{?^YUEU0q4*^76*qa+B6C$D|Vo?z5nv
*Losp{J=^SnS8V$7fuF?Xz{ESNXlzNaSE>;5wT7lEqJLZzl&#!czUF4v2#koAXVMGFRwW_u-vYUCo^8Cs?TQ$7MsaL@1`*!fu_vn
c`{ADvPaR?LW!RUXA$)wcqPe{G>%8i!w)WPk@+w38PzSTXLG{srS#eCd&^&2WtQ^V(pS5A(NY5Czo{4SFIP?i<%f!v%>|oM{qn=h
Lp;)7Ss?oFEfKv@TG8-M0lYp#Z8fTgIdi*>7s|1+n0?7KWl4D=<;shMq7Z3!HeR>*pn(KHI*;R&o8xhu+}`Ds1f*$v8*y^C>M&hS
@?<_qsHjyNoG`NQE4R^f8fnT08JD8zU=)$T#W37#-8)l8$s+*-zhxyw5rLEDO%tM$0;s*nq1&yymSt#4-F5Nh=&r6Q!gmcvQw+m(
@W?Z5x>=`Bi@q#N`1Fh}{Jy4i>%uWTx=|N~N3ATww(;1~O?0(P)6*2wa2(L{b(e1XhD%Qj)9#lw(yg0@?g&kBb<j5ra3FLa90=Re
<(RsQo2E|f91Gk~3(EvK-8Sf3n7$>zvO^cXEj&E3ZS*oc2h;TEfn#HqbwgMd-7_tpd%8AV*p9%3Wnl={z(w6PJ<P=sf-uF_nSIN|
IG!#bF2lfc17p@b*CJMh5FkJ@BPLzUS~xD4F%1iR8@6xY((&XpJxELFj!z?4jw?r?gkAB`x6XsrO_O9+7FpSUgk`%nG2q%fcj1~O
dzz|nU5p?++Y`{N4qbXW)FKGRtIMXQZrNyOdzS7o*S7CNViuSZm<1j?I+ShNt_3o>;cb$^P7s%e!7NFA9;D&f0#h<{&o^w`7M@A{
Jww=ZX%ffwCK;iV5NHyfZ$nYkOn{ziSg<(i@A`B}N;0L=bQkn(OSoHvT*Jdqq+=+|c1=jyF)S0aa)qvgzU5dRu6_E0s$IwRD}*dk
tjQ`jVO%6;1Lo>GuCSOxOMsH$=uorJZ4=_O4YJ&dh)5qgnAIJd1xv~&-FpVB%k*@I<?Wj=C(jo!P8!@46^3lxhxPfUiT=VO$3X|z
g&Ug1ge;c@PBsFqk?tx)e8*(DxSkImCxhon3YYy(*e1kdxR{!4x;)M%1($}W9yU!%PG3MHCJ7K^$u!|Qf>6PL^^rEAa8j#LVZ_ia
Acbq$K8w?_btr<|$bg}+r<&yBphnID12_E&5yB&M@^z0TtCPtCE^Kx#VUqvx1RM{%`MM9oCWA7}DjCK?)AQK4OfqsCm?$jRoK91O
OlVGm6-Bn~GdkE6I%K;hJcz8EeZdz#u|r(@I&gqI3V7fc9`q&*(}Bkmx;h&o?ys`;4e%xdCf+4nKvNEU)`Z{N(7VNmL_BGV&RFdm
?5@BPHVb$ogo240KEnkOAkVKrv*EC}OVFgACSw4Gg<k8>gJCjY0xn^QhzLF#8>6%bzMu|-3w%P4c+R&V$vU`Z-_%!R*{kb5J%mlv
9fo<Z&C`W2bw*$Ou)rU;fO<?=Pu(y$S~wC+LB%L$UYC$BBZq6f3aTVj_9Db30#d{`8_Ze&6IL9#3`|*ft3WDMV<B?5I(s$%fvuaM
6&3`@CtX=p1eRKXkrGlO9tZ>x7$7DFTQWIn5OVm{zKCvykD-MRaZpQ^lf`}m^;izzVjBYt77+zWm&aw>1j>3)E=3Q_oh^+byjLC8
M<>EU_77Gq@R~;w1RJn#Oq}3n3wfYvgJD8C6sHfqj1$nd$@XfvZbeRnb7<q5cxqZOO2#k~8Z%%c9vqUGsv@Qf0Hf$=Lle*pXB8%<
EMOrXql@QNW+@!DG@g`9kJz4E8N1+arVB);kXHdD!}mCQfx;;e;I|9Yv^atY#6W`~jZ|C(MD}BYHAnExvjh~nNG1du5@EB&epWRk
!3s4vEi%|a1hgUpl?Nv^1%Q&Gc-4+{z`r3g0iE4gz+qe<sKKydvbIdp*7s40@;V?ACp^Ls>`P4AcO{3w0d`X#B636lRywDkKolf!
9^kVMho~D2Kb+=R@D0Nx@ZLl$hm~*W5=`JlHm7BrgmK^o$|9HH9ES2p&Vo%et#hI#SV~ZhV8F82Xm|>o+8Q3?pUgsKt_IcC!E2q7
h9RKtanM8n0`BmKq{96Bj9GAM3%3P_{W{w}At7g<@Ow+5qAQJ?6J*>bH1(NJAv5?_fz0zvnG|w#_Si8k7br%F2V;iMDYehpD9LRr
?Lk^X&Zcv&!p$sU7P$p%1+Z&#?(3UX*Ks5$bAdoA;6%mrI5F~IOoCz|e{o14QR~%^?z5K(=9^5B1GzvnGgzaP3Ai%0S~8oqs{J8Q
lhb{A3_bZ4V1QJ~T=0ZUPJU=YR>dD|lZ~AXl@c^hrV;q^@hMT>H;PoN+MCjHnY&q>*su%AstEL`{NgOdf>b<8^fo(NT%8FyKf_}P
vOIt$=gzVebC4915o~t#eCXWrfik|#kSSNi6cEl#gMruMtgV`OQ)bPGj+8{!6RvME40wjjZe>jYWA&*3tMv9EP691%Bz#6Wb`*9(
s`DT&i<30lsi?|k53o7+a%@P*XB;v(=26U*6(GJS>8=<W@_KNI$vVCaeJ12<Fz7oR&gquNEK!D7>Fzm<Ie6@GqC&N*O#0}K!%wLj
n=Ijv_kHLSRAaHX+a6~qT(^+_02nA?hp&^YIfwE%WsxvN9-tS+wJU3D7#)RZr?7mkaXr`)<>(w7WO~cyOo&xML(hQ191bSrj2ty=
7Qe~h!YZ;kWAT|8OAZS3r7D`a1(%fkNVwya)3z9td<HK|q9m&xRU<+Kay0U3NYex?TAaq$Ep~#ssdL83PiW#kkIuaL@;w75jy?mq
Z9oo|0Vm;Nn<@<sC!S!JFxkOLq&m;gbXLYAxZtBy5Qfg0vt&Q(^-`MRIAQ|T&y4Ei*YH^?)d7)|C&+vs?q~D63Nnm}AyGa6VUmX6
HJ;~kd5_XxR-K&c6U@R*I8AY!YEnh{KgP3MPH1QZOu(e7MaWFR<3!SD;X6KKxK34Ag%4t#+4P`oDhlDgR7FF;p5@3&R+l9viNxbT
U{}C^!~lRHJLRm(mNTcaiT%Uk65eDxrCh<}jDo^gC4!J<5IZaaIu@VqV0OfjeDOgF1jvxHKtO~$oUZ8AIAoeO+F35^)+y>i$46kH
^c*HbB`lkoFXI~J-j!Hl5g>6c>Vajdx>%Bwy2*swm!`w{HBu)WZmGW9a4~0+li(S-rks(%hOWcjT*gNqzFbYSbxvj|zvp*YF8d2v
uO~IaDCOwDcgu8(3bXo>hAMCfk)oNyuEn;E7Y^`c%V(%S)r*XTeVPJdl?#)V4O75?{DO<f!Y*Bp3suMRpbG*Q&cCUtQ_Z7Ii_;?q
^QNfB*{SRBn<c_n3HuJ$mX5=>4XC?HMZWG6{D#06{9XoZag8n*8-+#o4Z9$t2cJ}H@5nm)y|kBN$Fy8o8r5cl`_*dgBF>kKR4Ff6
(bI3OSM~NZ{`aW2r>cj&y&hiCmshRiSiB%r<HJCu;RZpOhj;t}pBrtiU=7sr*`wYb7JFz=riN9Q!Pc6~pt|Bxn%rQ;(>O|NQDx@c
ZnV9Bq_Vl5H<9evLGs;QByw1O{atLDtgUyemrlaqETCooz$t}?|D6L0kKG3lU+;)4MDt-afk_;VlJqv5CMlUf?P5jmjq)j-Cy%o{
9<A3_>f=QmEAb@Z<1%#PNZ}?Kzm6{`mG{c6_Wd`5?xK4nMZW<17sS(i5kCgv9d?ASw=WlhYX(7=*I*awOCKzpA2e4Rcq)4uys{ja
si28{+n9Vol<)qe^MI@EEqqVily6D)54(0IS9I|3+V17wwM8&W9;dTWttpjqz{Ay>#WrJRkPH)oP+#Ba8wA92K_U3PG)u^jDQ?QH
>-Fj1%0!F1o6Zwq^-P+<G)mI-PI&Br&4Oa5KxJz~qzzP6tvJ!Htp~idOB=kh<zf2-BM*ulb#hOxPg&rh&*x}M4ZGtV?rW~y7l*a@
c9*IG`NQgOnpPI)wN(@KKVGgZY>WEC(5yc<n%C%#%4avg-iztQ>wDW<W3VX;gk$yZ0lvpoajENRjpEy&i}vz-NQJbzjRh;~&w@YX
+3KAG{P_+Cs%O*LVt$uo(-;3*Z-6PUpw`ygwM%mWET+#jVvsEFZvnpN^sB$kl6s_UpF*PUB?i&6ymhh4ZV-&KiU)1*zp`S+gt=PT
_p~w76>zMW>u*MzVp$i%-gLs&$v;}1@aFpLGw-7QbaQ!ed42W%taHIT6eukD8l@wvy*0TWAk3H)+;YJ`olRD#0YSW}@#-%x-0H<D
u&MD<Z-2+$SbiqgVe!i?mVgaj6y7vm8kOi{@2p&9cGe>~>yhxw)a;!jIlN|UaI4i8T1Q(gJL6Ze(7YkCe_e)G?|<!_9YaP~{yuHC
J1YU1929e1r77?)u~JXzq+YOb3R=AE6vC3b#s?7P=|inJcDOoo_}W%td6ZM0<J3wAI0HlDgADS_=4-vnX9$BX^L88zwGY9Ab{<Tm
bq=)$jgPTm6?u)D(U(9bKfS&09gij1lx}U~UHOP?>CtzO$@cdCr{`p`V}Z|>$#a}IdU+eoD<F}KwAx&&9cvFu?OatikFNpHR~mwR
)EyfHF~?(db)FXc*l=e^cVzy<JN}N<o&C-c2ds^biy6e_$#h`$1)a~;ox2jDnA#IH#>SLV^W(#FWqpVQ<bJF-H-A{}ZvFIAv6Xhk
(sxFfcTI{>b@6iSBxXP(p}e%EL~0zQ@l#&gu_urZp{)YmyfngWF)Eaq1fcNp<jWoJyZIZ9TLoFk)tVmDcqhMBn474e2n64$DsIb4
#gzD}TNgA*^QCz@OR*<v=N?C%&))*GM7_Cjnr+>qpi-H_J+rn>@^)=<tc35?-}~3I@k&E^IxeUi@8oaF!`>I^HRZ3(m89O6wDEJW
+J97=Mo)4t;c}{-caNMtl~$YgoFi<pH%i^%k1Mj+_bA@}T;4nWA=s!pHmsAkt|!>3z3H>Lewc5a|6P#zVryvfcSoLTr1@mG!PfE3
&0b$flW8t<78>XEG^KoY^H?5|J@`VBJLHRdTqHZrm=)*y@=}`2Qr}McccjgS#zA&_P?SM+<A6EENy^;^Bsb4ies?BR++@L4&9vF(
4b9g&sC}%Ty*1Q^a<$sTzABJpH;S(_y7}=ZYE?M`TAY~w<`KEg^LoLB_Ra0T1+0{~4lt9l{8r&!{?9<xTitm3AMbZNX`N6^0}t%w
ny`xAuSLY|^Z(SpIAFIC^Emnh-QJ#fD|F!+p3ZL}jJMbgWEQ`L>6xy-x)3H_i}v;^xyq;Z+3Dr=McAf~=K0xgtrN=bTCK3vImR~G
e>AU<vtYc+TL?Mp&ik{|8|u@!qW^w9|J>@_w60f~4$!XPUh@x1SKG0D;}l_en18*$Ja4V`7Jh1X<o|C)ZZcd68JjIHcI>_E?NxYg
pS4@zKQGVPH%uYCy#DzNN$rYG`!akPkDi9drWGEaH_tBCq`tE&c5^(rH@1+(4{na_rGzA5h_^d9rPkXELzJ3f*xNfQiq2lT_ve2B
*qB`X
```

The decoder was run in a fresh directory containing only these two capsule files. Both exact proof scripts and the symbolic mass script were then executed. The regenerated four sources and four certificate outputs matched the original hashes, producing `TYPE53_SOURCE_CAPSULE_RECOVERY_PASS` and `INLINE_CAPSULE_ALL_SOURCES_AND_OUTPUTS_BYTE_IDENTICAL_PASS`.

## 8. Observed exact replay and byte identities

The two exact proof implementations passed in the working directory, in a fresh directory containing only the four recovered sources, and after extracting the convenience archive. All twelve manifest entries remained byte-identical after the clean extraction replay. The four proof-certificate outputs are generated completely from the inline source capsule; none depends on downloading a file.

Observed terminal markers included:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


Exact source and output pins:

| File | Bytes | SHA-256 |
|---|---:|---|
| `verify_type53_root3.py` | 10791 | `45476380fa379f8159f632be634f937f6365d2e65f708e783e12dfa3ab926159` |
| `independent_type53.py` | 3478 | `41d1ec2fe802211a3987c3b0525f35da9268ebfb75c8f7e8cbf580e6ddd25887` |
| `verify_type53_masses.py` | 3083 | `b5cbd03934ff0607bd5a295ec5227a274a9f1aff1feebfbca288632485b19866` |
| `authenticate_parents.py` | 1194 | `06eb8b4e9824acee6302e6be36b422f9dfe08bf7063882f911c7be1f80749cc1` |
| `type53_two_apex_certificate.json` | 4268 | `d8c6c4b6fbf6e68af4f2b6d679324df146f3ce89e208b2cd6a15509ac0de965a` |
| `type53_two_apex_matrix_ledger.json` | 40586 | `ccef7946e03fa5df05f69778ab518800bfd69900c1a3585e7adc9778a7c61a09` |
| `type53_independent_ldl.json` | 23102 | `bef04807de12ce260b6c96ab46ff7f2078b73422ea3684eb1f44c2099f63b103` |
| `type53_actual_mass_identities.json` | 1326 | `272e1f151d25a9af1e6fd3dbfc186ae3bf4d74d453f00936f70b5dee866bff78` |
| `primary.log` | 880 | `8001f5f05e9a108e30db0b116c2d4f9fd49a7ce548132b88c7292e08c4c5c8ee` |
| `independent.log` | 287 | `6965ec258f6aa6cf020b73d1f8f9b10726345dd74b816c3b22d49b44df5f8781` |
| `masses.log` | 387 | `adc295259651807908443864f82713f3ad4efa941adc8166dd1463fd1ac6c479` |
| `authentication.log` | 451 | `dfb8b39e427b84efde77537d42828d8ac9187f29cc7e0df8ef512852eabe5368` |

The archive manifest itself has **1,628 bytes**, SHA-256 `a408db794ec51c57de959813ca140de961ef2cb0a8218b4e99745716438df7b6`.

Convenience artifacts: [exact sources, certificates, and replay logs](sandbox:/mnt/data/C32_TYPE53_ROOT3_ACTUAL_TWO_APEX_EXCLUSION_V1.zip), and [this complete self-contained handoff](sandbox:/mnt/data/C32_TYPE53_ROOT3_ACTUAL_TWO_APEX_EXCLUSION_V1.md). The ZIP has **40,651 bytes**, SHA-256 `c36a90530d6af3affa77edd596c2e15f7c48bf5e3521c448546dad0618fd5b91`. Its thirteen members are the twelve pinned files and their manifest. These links supplement, rather than replace, the complete inline capsule.

**Final scope:** canonical C32 type53, unique unstable vertex 3, all physical realizations and all paired reciprocal metrics: **excluded**. All four inherited Hamiltonian paths: **closed**. Other roots and the global C32 minimum: **not determined here**.
