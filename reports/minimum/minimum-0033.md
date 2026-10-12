# minimum-0033

AI research report · 2026-09-09 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NOVA24_TERMINAL_PROJECTION_AND_ACTUAL_COUNTERCONTROL_V1

## 1. Determination

**The terminal triangle does not force an additional equilibrium. Its local geometry forces the opposite: the interiors of the facet and all three of its edges are nonequilibrium regions.** With the next true-edge escape `5→4`, its vertices are not strict unstable equilibria either. This holds even when the chosen escape inequalities are weak.

I give a sharp normal form for this geometry and a completely checked **physical nine-vertex countercontrol**. The control has its actual uniform-volume centroid, Euclidean metric, full rank three, a genuine terminal facet567, every one of the 34 strict forbidden-redirection signs, the entire strict long-branch radial ordering, and seven of the eight required true-edge broom escapes. Its only failed broom escape is `4→3`. Its exact strict class is **(S,U,H)=(3,2,3)**, with the extra unstable vertex4 and a genuine saddle on edge34 outside the terminal facet. The properties persist on an independently certified full 27-coordinate box of radius `1/10000`, with the actual centroid recomputed throughout.

Thus the proposed shortcut “the obtuse terminal facet must itself contain a compensating equilibrium” is false. Rank three, supporting convexity, actual determinant masses, all forbidden redirections, and radial ordering do not repair a missing middle escape. This is an exact physical control against those intermediate implications, **not a nine-vertex U1 example**.

**No V≥10 theorem, new complete C32 exclusion, or attainer is claimed.** The accepted bracket remains `32≤C_min≤1374`; this result makes no catalogue-ledger subtraction. The new durable object is the independently checked physical control and its complete inline capsule, not any unresolved locator output.

### Authority

The literal direct parent is `minimum-0032`, SHA-256 `3c4347c3beb52ca549da23ff0b0eb42a85251a52c2a920bbf1deb68b4b73fe4d`. I retain its analytic lemma and its honestly conditional recovery status. The lead's later, distinct result completed both numerical reconstruction and independent frozen verification and accepted the universal285/omitted0567 reduction. It is that later result—not a relabelled parent—that makes the terminal lemma necessary for every actual nine-vertex U1 candidate. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

The imported checkpoint is `recover_quad10.py`, 24,289 bytes, SHA-256 `fc6fb7a3b0fd6e44fa4e69145e38453d131136e34cbe1cd9033e27791954f5f2`, including the journal's explicit transcription repair. Its universal coefficient file is 1,289,123 bytes, SHA-256 `3a00b679c994255debd3acbe5d3230e336d1e292b9cf88507dc1d2c61fc94496`. I did not repeat that numerical recovery. The new control below needs neither file as a reconstruction input. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

## 2. Sharp terminal-facet geometry

Write `D_ij=⟨x_i,x_j−x_i⟩_M`. The accepted reduction supplies

`T=(0,0,1,2,3,4,5,6,0)`,

with true terminal triangular maximal facet567, `D65≥0`, `D76≥0`, and `D75<0`. The last inequality is essential: replacing `7→6` by the actual edge `7→5` would give a different, excluded rooted-tree shape. Index278 is the rooted-tree index, not canonical C32 type278. :contentReference[oaicite:4]{index=4}

### 2.1 Complete local normal form, including weak equalities

Apply the invertible linear map associated with `M^(1/2)`, transporting the body and its uniform centroid together. Then choose orthogonal coordinates and uniformly scale about the centroid so that the terminal facet lies in `z=1`. This is legitimate metric transport, not an assertion that an arbitrary affine deformation preserves mechanics in a fixed metric.

Every such terminal configuration has the following form, after choosing the in-plane orientation:

```text
x5=(a+c, −e−f, 1)
x6=(a,   −e−f, 1)
x7=(−d,  −f,   1)

a≥0; c,d,e,f>0;
d(a+d) ≤ ef < d(a+c+d).
```

Conversely these inequalities imply exactly the three stated terminal signs. Indeed,

```text
D65 = ac,
D76 = ef−d(a+d),
D75 = ef−d(a+c+d),
(x5−x6)·(x7−x6) = −c(a+d)<0.
```

For completeness, align `x5−x6` with the positive x-axis and write `x6=(a,b,1)`, `x5=(a+c,b,1)`, `x7=(a−L,b+e,1)`, with `c,e>0`. The obtuse identity gives `L>0`. The first sign gives `a≥0`. Since `D75−D76=c(a−L)<0`, put `d=L−a>0`; the second sign then gives `b+e<0`, so put `f=−b−e>0`. The displayed half-open bounds follow. No strictness of `D65` or `D76` has been inserted: `a=0` and `ef=d(a+d)` remain covered.

The metric-normal projection of the centroid is now `q=(0,0,1)`. Its barycentric coordinates in the order `(5,6,7)` satisfy

```text
λ7=(e+f)/e>1,
λ5=[de+(a+d)f]/(ce)>0,
λ6=1−λ5−λ7<0.
```

This specifies the exterior region, not merely nonstability.

### 2.2 For a fixed obtuse triangle, the allowable projection region is bounded

In intrinsic planar coordinates put `v6=(0,0)`, `v5=(c,0)`, `v7=(−L,e)`, with `c,e,L>0`, and let the centroid's projection have coordinates `(s,t)`. The three terminal signs are equivalent to

```text
−L < s ≤ 0,
e+L(L+s)/e ≤ t < e+(L+c)(L+s)/e.
```

This is a half-open triangular region. Its closure has vertices

`(−L,e), (0,e+L²/e), (0,e+L(L+c)/e)`.

The left vertex and upper sloped side are excluded; the lower sloped side and right vertical side are included where the displayed inequalities permit. Its area is `cL²/(2e)`, or `L²/e²` times the area of facet567. If both chosen terminal escapes are strict, the right and lower sides are excluded as well. This describes the complete local projection domain; it is not a numerical bounding box.

### 2.3 The chord57 is necessarily nonsaddle

Edges56 and67 cannot carry a relative-interior saddle because `D65≥0` and `D76≥0` put their line-projection feet outside the respective open edges.

For edge57 put `K=a+c+d` and `ℓ=K²+e²`. Both `D75` and

`D57=−(a+c)K−e(e+f)`

are negative, so the line-projection foot `p` lies strictly inside the edge. That alone does **not** make it a saddle. Its horizontal component is

`p_horizontal=−(ed+Kf)(e,K)/ℓ`.

Consequently

`p·(x6−x5)=ce(ed+Kf)/ℓ>0`.

An equilibrium on edge57 would require its plane normal to `p` to support the entire convex body there. Vertex6 violates that support inequality strictly. Thus edge57 is nonsaddle **regardless of its other incident facet**. This uses the complete support condition, not a facet-only surrogate for a mixed normal cone.

The barycentric signs already exclude a stable equilibrium on the terminal facet. Vertices6 and7 have their chosen weak escapes, and in the broom vertex5 has `D54≥0` along a true edge. Therefore **no nondegenerate equilibrium lies on the closed terminal facet**. With weak escapes, possible degenerate vertex contacts are not being excluded by this statement. The physical control below has strict escapes at all three terminal vertices and has no equilibrium of any of the audited types on that closed facet.

### 2.4 Actual uniform centring does not invalidate the local region

Every strictly obtuse triangle and every projection in the region of §2.2 can occur as an exposed facet of an actual homogeneous tetrahedron at its own centroid. Place its three centred vertices in `z=1` and take the fourth vertex to be

`xA=−x5−x6−x7`.

Its height is `−3`, the tetrahedron is full-dimensional and convex, and its uniform-volume centroid is exactly zero. This realizes the three terminal signs with actual volume, not artificial weights. This tetrahedron does not supply the rest of the broom or the escape from vertex5; the following nine-vertex control supplies that additional escape and much more.

## 3. Exact physical nine-vertex countercontrol

Use **M=I₃** and the following literal integer vertices. Translate all of them by their actual centroid `C` below when computing mechanics.

```text
0: (−113,  66, −111)
1: (−126,   5,  −94)
2: (−117, −49,  −76)
3: ( −91, −99,  −44)
4: ( 156, −66,  108)
5: ( 163,  −9,   95)
6: ( 140,  44,   93)
7: (  90,  45,  122)
8: (−100,  63,  −94)
```

The complete outward facet cycles, in facet-ID order, are

```text
018, 021, 032, 043, 054, 065, 076,
087, 127, 178, 237, 347, 457, 567.
```

The complete true-edge list is

```text
01,02,03,04,05,06,07,08,12,17,18,23,27,34,37,45,47,56,57,67,78.
```

Thus `(V,E,F)=(9,21,14)`. **This is not a C32 catalogue member**; no canonical C32 or MP9 alias is assigned.

The exact physical mass quantities are

```text
6 Vol(P) = 6844728,
Vol(P) = 1140788,
C = (22288883/855591, −2357535/4563152, 355836587/13689456).
```

The minimum outward support determinant, negated to be positive, over all facet/nonincident-vertex pairs is `15584`. The independently computed determinant of rows `0,1,7` of `4(6844728)(P_i−C)` is

`12805084088515047476994637824`,

so rank three is explicitly checked as well as following from positive volume.

### Complete shadow-sign and feature determination

Exactly seven of all 72 directed unequal-vertex shadows are positive:

```text
1→0, 2→1, 3→2, 5→4, 6→5, 7→6, 8→0.
```

The other 65 are strictly negative. In particular, all 34 forbidden-redirection signs are present. Their complete reconstruction rule is

```python
RED = ([(i,j) for i in range(2,8) for j in range(i-1)]
       + [(i,8) for i in range(1,8) if i != 2]
       + [(8,j) for j in range(1,8)])
```

The optional shadow `2→8` is negative. All eight undirected broom edges are true edges. The only failed directed tree condition is

`D43=−17589489765/414832<0`.

Nevertheless,

`‖x0‖²>‖x1‖²>‖x2‖²>‖x3‖²>‖x4‖²>‖x5‖²>‖x6‖²>‖x7‖²`,

and `‖x0‖²>‖x8‖²`. Thus vertex0 is uniquely farthest, while vertex4 is also locally unstable. This explicitly separates radial ordering from the missing escape inequality.

The terminal values include

```text
D54 = 481403381/1140788 > 0,
D65 = 5413645561/13689456 > 0,
D76 = 839052195/2281576 > 0,
D75 = −5226468389/13689456 < 0,
(x5−x6)·(x7−x6) = −1145.
```

Facet567 has outward raw normal `(1539,767,2627)` and raw support constant `493519`. Its centroid-projection barycentric coordinates, in order `(5,6,7)`, are

```text
(3337985045819/11245818515932,
 −15295094729/30075734832,
 163523091690379/134949822191184).
```

At the line foot of57, the actual support violation toward vertex6 is exactly

`p·(x6−x5)=15295094729/27378912>0`.

The exhaustive strict feature classification is

```text
Stable facet IDs: [4,6,10] = [054,076,237].
Unstable vertices: [0,4].
Saddle true edges: [06,07,34].
(S,U,H)=(3,2,3).
```

No terminal facet, terminal edge, or terminal vertex is an equilibrium. The missing middle connection is a genuine geometric obstruction in this control: both endpoint derivatives on34 are negative, and its line foot belongs to the actual normal cone, so34 really is a saddle. This does not prove that every realization must fail that same arrow.

### The masses really are the common determinant volumes

The nine genuine apex fans have cell counts

`[6,10,10,10,10,10,11,6,11]`.

Their 84 occurrences use 65 distinct unordered tetrahedra. For every such tetrahedron `t`, the programs compute the one actual value

`d_t=|det(P_j−P_i,P_k−P_i,P_l−P_i)|`.

For every fan they independently verify

```text
Σ d_t = 6844728,
Σ d_t Σ_{i∈t} P_i = 4(6844728) C,
Σ d_t [(Σ_{i∈t}P_i)(Σ_{i∈t}P_i)^T+Σ_{i∈t}P_iP_i^T] = J,
```

where the same exact matrix is

```text
J = [[646558014992,   6472608984, 502183755467],
     [  6472608984, 145885764288,  −8326370975],
     [502183755467,  −8326370975, 428778877338]].
```

The raw uniform second moment is `J/[20(6844728)]`; subtracting `CCᵀ` gives the actual covariance. These equalities are checks on genuine tetrahedral partitions with determinant-computed masses. They do not infer physicality from moment matching and do not use the journal's fake-mass relaxation.

## 4. Independent exact checks and a robust physical neighbourhood

The first source computes the centroid by signed outward boundary integration, classifies edges by their two incident normals, and checks all nine actual fans. Its exact rational interval calculation proves the full class on the closed raw-coordinate box of radius `1/10000000` in all 27 coordinates.

The independent source **does not import the builder**. It recovers the hull by testing every one of the 84 vertex triples, computes tetrahedron volumes with 4×4 homogeneous-coordinate integer Bareiss determinants, independently recomputes all nine fan moments, and classifies edges by their supporting orthoplanes against every other vertex rather than by the builder's two-normal solve.

It then certifies the larger closed 27-coordinate box of radius **`1/10000`**, with the actual volume centroid varying throughout. It verifies every support inequality, all 72 shadow signs, eight radial comparisons, 14 facet classifications, and 21 full edge classifications. The 115 reported denominator-cleared checks count the last four groups; the 84 nonincidence support checks are additional.

Here is the reusable exact method behind that second certificate. In a genuine apex fan let

`V=Σd_t=6Vol(P)`, `m=Σd_tΣ_{i∈t}P_i=4VC`, `Y_i=4VP_i−m`.

These are coordinate polynomials, not independent masses. Shadow signs are the signs of `Y_i·(P_j−P_i)`. Radial comparisons use

`(P_i−P_j)·[4V(P_i+P_j)−2m]`.

For an edge set `e=P_j−P_i`, `ℓ=e·e`, and

```text
A=−Y_i·e,
B=4Vℓ+Y_i·e,
W=ℓY_i−(Y_i·e)e.
```

Its strict saddle condition is `A>0`, `B>0`, and `W·(P_k−P_i)<0` for every other vertex `k`. Its exclusion is certified by `A<0`, `B<0`, or one positive support violation. The denominators `4Vℓ` are positive; there is no near-parallel-normal Gram determinant in this test. Facet-side predicates are similarly denominator-cleared. Exact rational interval arithmetic on these polynomials supplies a continuum certificate, not a bounded sample scan.

A trial of that independent interval test at radius `1/1000` stopped at `('ORTHOPLANE_BOX_UNCERTIFIED',7,8)`. This is a failed interval certification, not an assertion that the geometry fails somewhere in that box. The accepted source uses `1/10000` and completed all checks. No larger neighbourhood is promoted.

The failed assertion was also reproduced from the accepted source by this exact patch; running `python -S verify_wider_unaccepted.py` exits with status1 and the stated assertion. It is not part of the accepted certificate.

```python
from pathlib import Path
import hashlib
b=Path('verify_broom_control.py').read_bytes()
assert hashlib.sha256(b).hexdigest()=='9df01d48ca770639ba74de060619e7f14efa07b8aa3d837a31ebf68e8cb9b4d1'
assert b.count(b'eps=Q(1,10000);B=')==1
Path('verify_wider_unaccepted.py').write_bytes(
    b.replace(b'eps=Q(1,10000);B=',b'eps=Q(1,1000);B='))
```

## 5. Remaining continuous complement and useful continuation

Moment-only coupling and additional local templates did not give me a universal exclusion. I therefore resolved the local equilibrium-forcing question by the exact arguments and physical control above; no unresolved numerical locator was interpreted as a physical witness or an infeasibility certificate.

The whole unresolved nine-vertex U1 domain remains the following geometric problem. In the normal form of §2.1, choose the six other vertices `x0,x1,x2,x3,x4,x8` so that all nine are actual vertices of a full-dimensional convex body, 567 is exactly a maximal triangular facet, the eight broom edges are true edges, and **all eight** inequalities `D_i,T[i]≥0` hold. Impose the actual homogeneous centroid, for an actual outward boundary triangulation, by

`Σ det(x_i,x_j,x_k)(x_i+x_j+x_k)=0`,

with actual positive total volume. All 34 strict forbidden signs also hold by the imported reduction. There is no imposed metric-condition cutoff, coordinate box, positive lower bound on cell volumes, or contraction of the long branch. The local normal form includes both weak terminal-equality boundaries. This description covers every physical SPD metric through the specified metric transport.

The control is **outside** that full domain precisely because `D43<0`; its independently certified neighbourhood preserves that failure. Its value is to rule out deriving the missing global connection from terminal-facet feasibility, uniform centring, forbidden signs, or the radius order. The next proof must use their interaction with the **entire seven-step true-edge ascent**, actual global volume, or genuinely additional `S=1/H=0` information. A local terminal-saddle argument is not merely unproved: §2.3 proves the relevant edge is nonsaddle.

## 6. Self-contained reconstruction and observed execution

Save the complete code in §7 as `recover_terminal_control.py`, UTF-8, LF, including its final LF. In an empty directory run

```sh
python -S recover_terminal_control.py > full_replay.log
python -S recover_terminal_control.py check > frozen_replay.log
```

Both commands were actually executed to completion in a clean directory. The capsule contains both complete sources, their literal integer inputs and all helper functions. It needs no previous journal, catalogue, coefficient file, numerical optimizer, network access, or downloaded archive. The checked environment is **CPython 3.13.5, standard library only, assertions enabled**, no randomness or parallelism. Exact nondefault interval radii are the two stated above. Source extraction alone is `python -S recover_terminal_control.py extract` and is explicitly not a mathematical check.

Pins:

| File | Bytes | SHA-256 |
|---|---:|---|
| recover_terminal_control.py | 10374 | 625a592931435b11bab3bd28cd92c3b7db393e611e57427f6f61c7603de78623 |
| broom_control.py | 7762 | 43d6dc75ff87ba4a9282ee3f27c9d130eed99ef49fac32f75f2c3c881a5d2f15 |
| verify_broom_control.py | 7370 | 9df01d48ca770639ba74de060619e7f14efa07b8aa3d837a31ebf68e8cb9b4d1 |
| broom_control.json | 5784 | 15d86cf49e6b0ed5a84a9dced39a1dbddbb99da251fdb5a705b7848cb5f26413 |
| broom_control_check.json | 519 | 4edddd62ff48306f8c21ce563ea83639875d0baf7a7b21b4f6bcc2127cfe8437 |
| full_replay.log | 986 | 0e54f272eb05a51cbdb902dc5bec0704a1178e0909d20c1dbd1a5068d7703e70 |
| frozen_replay.log | 482 | 34d70e18e16e7172724bdea4f89cefb8f499a96b9f76b52b561ae39e46533b0f |

The capsule also authenticates the decoded 15,477-byte source/input JSON and its 7,559-byte whitespace-free base85 encoding. Their hashes and the separate build/check transcript hashes are literal in the code.

Observed full-replay transcript:


[Encoded source block omitted; the code in this passage is incomplete.]


The separately executed frozen check reproduced the last eight lines and its pinned report. The source and report identities remained unchanged after both executions. This is an independently checked computer-assisted physical control, not proof-assistant formalization or external peer review.

Supplementary [complete bundle, including readable sources and transcripts](sandbox:/mnt/data/NOVA24_terminal_geometry_control.zip). It is a convenience; the complete reconstruction source follows inline.

## 7. Complete literal recovery capsule

```python
"""NOVA24_TERMINAL_PROJECTION_AND_ACTUAL_COUNTERCONTROL_V1.
Save as recover_terminal_control.py, UTF-8/LF/final LF.
Run in an empty directory: python -S recover_terminal_control.py
Frozen independent recheck: python -S recover_terminal_control.py check
Source extraction: python -S recover_terminal_control.py extract
Executed with CPython 3.13.5, standard library only, assertions enabled.
No external input, numerical locator, random seed, or parallel workers.
The two complete sources and all literal coordinates are embedded below.
"""
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
assert __debug__
B=r"""
c-pl)3v=Q)(tpLfTUXeL$Y36MF`D`kLMGH@fB`a_J;voS*nktTS=*4u*8KOcyCvD?k=)$g_wDWlS!%UftyVvEfBia&!f;`a!yt*m
`O)&_*YjV$)4%P`w~KOBbH>TanHSgLe6{ejzz@9Q+KUqJSxdZV;RnuKlara&=)NSgFwiPTX62~%Ax_-l+#el%4|=QMTw994Vqe={
^GIulS^)SXe+>BM;n+#SNQ3{pXIKT-@Pp+l(fn9j#hwco1&!Z>Nfa)$Nd#2-VGwKnVi`t>b}c(JC)TbdkPn!WFr24A<8Uzo`e~ws
SvtuKC{_?%`1~HokC_wW7<-7rfGudmiDSU2*|zJAR#V%Cjb8lDb-ies6?S~g;MX)5e3p+{jTO(T^kJT`V)cv_Pmb~P%!C2>s>0y+
K*N7@vj%fvzF9g25c9YKAndG$?P`fttL&@-?K5cBm{~3p)>4TPT-7kX2iJX|qQp#w^GmGEO!}>`GW}Lrg??+SO20rI{hqL6MFf1E
vJ+epW{ckw!d3<>_+0@k_*(@m_*(-kC%AUEgNvK2M8GD2mI(kC6HC!T`YFJ`gaL=ekXS^G=#HTuSlPVd$!a<GblqnU#ss9n2Qknh
CzyJG`INdIvM#@98pdHd<#c-ra>Ji!{x7_of}Kjt51U}Pjf-BhJ>Uf=p4!F7>SJSecJ>&qW~18d&+f_Rwtw>HO98-cc%d?`R;nlC
%E%kl%44TiJ#(FMWily^O5Uhic1~;Mn(4q$**PnhMx%)d@^XASs*X-76R+w58rPd>@oJ<yY-F5AUb2b;O_2Cpe9@4?XZC_LzWPf7
GQ=Fmb@$CVd~eQTHP>V2Y|V)ep2ZxT;Yd(7Og7NRtA+l2@E-DU6vpw!9Nih3*1>34wu%n?ftG18*(zaQNsKbtGO^DTqlyfV$YA3X
sUS=&hW!fAUvI4Ke1N+QM;`k@oH)VQgVC0OVv+TXpvRlXo_0-B1)?B~7P_;woZ`yZ3qY6XUE>_?iW~DG(s!VDhrX4H+{7Tcnqd37
Z`H3j^3II`g(i_+F~NBxng$Q>FJc)!<`H4jWfR40H)hv;!(i2eD;j#tM7Lt($am&3k|-A&3SOa%b%!I1b%%~+F!4E-pM;M1EU6aA
CeGNi6E9BmE^D(1?V6zYq#p2gea4YJfxuD!lcRj$o@R`=7yzw7ZrekI&QtS%%lnd=KSdj-5DVCY+V_M_hUU3-I2oRsmLX~L+-Z(B
k4>gT9!%q2eZr=EGOe%p<~sF+BY8!n13TEt5R|SAqrT*LrKlVCk-#9*4jP}ghZBpnhf}NWdI6^yVjD0>K+b$Qa|k!0Ucwd*2x?&z
MaRN85Ug4l3~=C_k(cDBEaa3xO$m0VC_X04EGCQ=Wrzk?GM<A;(pn^!z#ZH613$5CJ@)1k22i{m2A*+_pGOV{fj8>Z9$_1A$_Py?
0%>$5Mn+xQI5FiT7vO;Zf8hEg{&?YmQFrBfQ@97usmMKVUA<>@(OLkMQV8r;1ct_W$XiE<B{b?1OG_6^ABIN`6RSfL?<q`<Xf~Hv
Qk;P|l{iykT6$4TX5!b$C;;imQJ^#(d>$4RF)3`c7g&KE67Ccj1SkiKb~U%XH6Ny$6hvI^QtpssAJwalyT<KW89%`3($@yKAkXk4
`9Mo?xnxQ}60JOtt+$DghYO1wz#^YYOfR(BgJ$pB#jSnS`qt{VI&J%3&0eR#;v_<14A~%suW31M9kg`w0}L?yn`3XZOT`x3J_xQ!
>*T=ph)}%SG5_laG)a~ELI--}C_0I!gBqj_y{jnB3C&ULC4k*o%@bYPJMif|SNIm7Zibd|<Sdt7;OY~fF0)|G+zWKVU~pbGH79W4
n$LCYUSk(6z9zb8owYMxd9iNfP$2yFngddDhMK1BxGHCa;fgi5v^L;b8ufcVL|wLI4U&*0&VT`{-sVc>BV4xj73asN)#^$4lt^!I
u3zira`_bgsj$;pt#$?;+O=LRS86A<3ixQX<BC};V_&6KJFOhoPEVLwIX*pu5u$18g>dP?Q|H5?P)$e@EQ>l5e<onKr7;OIv(-kc
wYAMN^2fkhC1mNWjBb?ibRpog3A9vG?u%vb<w~DQ+P<}je^>l3I^lDia*q@uvG-^T?&%12DBAJ{&!o%v@MH5p^{Xqe(w|B|n@$!O
++KqSq=8?!Ac}^ruC@dUTw9n|$u>lDKIWz%1kCC2A(?|`BX!O0t$L1(9&F+h{5dqOt(|}`j@Wy^A^<o=-mXv+kLDg9`r5vekdy$w
6fN6~c=(0;XnM5?$T>JZnQL&*fd6~X+^TP_%GR6Lm~bI>q1Zl^Z~>1N_{%%bEd0H)@Q4K)*{y@vZUL9>M?D5ZFbAz6Z<?nGSg|6a
RG_)#a)*<0hz}u3vgmx$o+`tLOm@n3_z=S<5j=^YNU+D}W(A$2;l#J3OLU!zZOt<Bu90+5?uW;g7zEoOI!;u_6BoV_eUWCB4#-OS
3v1yotk~K(I4GlE!Nqz{YzyQGK@_ZVDaI-ET0*ZB^lA&bK60WLuA9YCaZE0G#yuQCaVrsv=*vV&O25k1ClkSgDKHeVifz_#o5#`t
l)Hw{)I1UV$5QSB5&{mgdctZ}5q^*5F9ep>=0)|CdXYyaBmz2y7_w4adO~sOiD4P)KBhWJ2}F8dRGf>DlN3w<AtSvxitUg3#0l(i
xC#=uC2#}0aTvJdeMxKPEWPLa<r0R>3HWf+R3IEP4mZOIbgT$LsyXX9?E+XpyI>299(@@(a+H-*kYvU&h_RF@6)2s6ND`ht^SIRT
soqG8y33tWtYh$l2RCAlIKi=Mc+kjB(fw2s2*qcjh$og|u7?`K#Nynor){_HrX;&Wt8z$1I0aHbbo)`9pm9`Tl%O^rNF_3mN^*e|
F<>W%vU1Ca)3^rbRmEF$Y_uLM-at?|T|Sg+>$$}r@{7Mo)#1jBgMA=BPx+S8mU{tl5fZ4p`*SIf@RMgL?1PID=>1I_%sh&9BM;|A
FtAvzKq|Fl7KN+nEL;J9W-wGfDZ2i`3t~UST-_*qW?JB_JrLL^eD#7Oj9MJmU&WwjOi-fYAEVxt86NSsrLT(ujI9qv!${q$<%Y+D
lJKp?8ZDj%<4VrHwT_%mrTQPKtJKP7cEMB1T%|5znTJnO__vK0S+C5&+_|mVhVvr2v{#;UiYSciDu+lB_)7HQx=OHLg};o;khj9t
l<@?|L76MU{z^LY59P&V5v@^w<*!H%%meL<L00kgr<Rj$^V|pfiknux1Iy*Yj6*bXr-mhoAp3w+7)9B9u>Sq#e$y`Ib8X@|;QE7D
VW8?y{IN*CY7X|neCPuC3PI>W_F`uNigz`~409N{n5*?rxQ?=jKu51*!<)#CPB4x9h|Ev<gZz}7(4)F1q6y_Iazpte6F<}KA|7^v
7XTi8+y<5e?R82rDl%8*57w5xOpX%$9a6l!1$&niuw{kj)#s*t*}1px+Kpy!(7J9luL{glF&XeF7p7x82l|Z+K{$Hgu0Kw6A54AX
CojAp$^dq|)o$9~09o_izGw{YAV7pT@k^@>jYj7VgT_XuJ?M3A?Qdp*E#W|e#KuFO2A~-dF7l~rAf7qp+A;6mP`Vil3jP?}DY)4T
&kC&Ob)Sg<P`Ppxgt6u9CB`CwtzwX&$x5tbu_0!V#V@ohix9{Dvn?tY{EEp2?*3Z80^4se(r%&e@}b~Ks^1%O{+}zL*R@g3;~k(L
+{2mUhEMjw0b-tk7=(~6v<e*PxC*7hjz4Yfs1>p3GK~GiUwgJd9&-pS7{HEv7f!_ndVJ8ubZ<Ds3BWLa4m66QiW5cQ6Z)zZxdW13
TQXIAG3C|RDdSZS6EbE?)(e3nM5@|jhofW_dp4*dVkP-v21|#RQTQOJ+u_%r);=&BT|+tuJkG5tIA(3GkEGR3Y&1q-$;iRlnnaHN
5d1nR1?2pIL!lh9%o$>$x`oIVp#TDOLsEwc_`7sO33KW82{|Mfb+_e-Mb48g?54d4QQB>(j>1UVQ<iBk8#I_LtsxRF4ILrEAtjTx
kA_XeSz?EneG!e35FR0_EsNp2c(uejm6RG1SsV1Q7r}xnu=O|-Lmt%42Ho}%*Rhy&<gOOWSckjMaF6z*_Y(6#v;tx9;JV^2Vy+h$
{Ci#iYf$+9Jt!DQUN8<_PX{CJBs0CRS<^$j0P__2xZxL2dOD@-mJ#eqFGvm2yJ-Kj0_vmv4YW#L!`$56-r5)KE4%Z1+y2(Mz5CL%
8%<O%tt-2G(eD@X$N;udwflo!t1+<QMzng(#-P<{_X$P6`K{TuJJ)uz_4#IC4|;b^n-pZT-?->D`#boqaq-(u`?Gxs1U7Df%&Qhq
+v#03dxY|?-TDext}l9nn`VDN8L}NTsd~J=Xfy|Q?fArQ+;;lSE9$UsF8X%6V>iFvwQgINz1H2A-Hiz@H9B9ublUb+Q(|ln>@NTb
l;h5cZPyoVxetbZJ;^Bg;0ryIbt8wlc@Ma4+GyhzrqQm-CxYK8qtSw7NQHthsIAn6_>yWuqz0up=N40Tq1_qScP4JSQ7PNa`^N1Z
<rksj^KIu6c6teh<jQW`T(mzo^Ni><yPe)ZkTEitti&D(BLY1~Gw<2;r)XJmVV`oq;5^ti=LOrwl%j1H&P8hRd+;m!6%?O8d9mLt
ezyYGL+=IdqBfp+<3}$#Cl44l9<9b0e$Z|6gQ*6J3%u93j-_d>`drm6!Djd|s!a;g;0R(yK`^Q=h;))!xSTrySaP^rGw_m=nIk-&
(aN8@UQ~!>1*bU1RD2xH*B&@Mo8@(ex;=26$OZRp6oH}yziIw*r1e%ouGap>PXD74`q!T+p|d4u=vDH!>goGR>D~XfkpAD7(LZ-O
m_Yp5TJ{etTBD@e-Bz3HwUg5-E0{I+^msg}o_WWklIPZ()2egkjy<<>=9uotbw{H!tQXhJi94z}C#Bj5=ADj5wMqH7YE}xWYU>B9
&BE&Njnc3zjrl<UanXNPy?sIn-CV>O>W_z}@sA2tWT9EcX3<HTqL%>n1=6y7D~vbX<qPtMFS)R>5gF|W=UiCzfRYxMMje8Kgq!tv
%1!B6=g<a4Q~1;mJn)_qU4Ph4RX(x+ov%xXOCXLm7!|!_9Q=@mz;c5nHSi06JjW^Q5+-r{!|)TSD8^HA%%~Us+Y=K43t&|d1a6a)
8`4&Md2lI0{o<tv^bZK@Lz=@`{e$+;OLYmzS06rL7h<5HWmW}@r!c)}TKGTtjKF^e-zBYpiwsT5fAE*BL*hL}j#-kyLK)aD!GL4K
-!boz=eW|ks{oMlN-%9lOJm=Lp5{EeEVvXWUt}ISZcM<69nr9$+|+`_rQj^{F+IwNgI;VJ#-~N>yn@n|o6RcXGy*Q<U0khPSzL9b
h4DJz7WXNTgUejWJR<`I2@?VsoW=Og03EK__*nXg)w<X?M+U-tk0NO=3gb7k;uQ9+K??HOC}b{8!}5V}ZDHRk(w1)|Fttsq!DI?P
@TG*f;}Ra-y!6B*?^NP(k|i2}^CE62SQeTukun@pEzGQ@6*}n{|FxC4#1%7KG*6w){z~1CTq;>$Ry28rO4=e#G?pVNE6?Q<u)-1F
NV)FKx4uRFX3kZRk7?I5;qyaePWez=xP0a`y~=p}t|1fRlpr+Hf*j8NB2t#?y)Qo`P9Ye?E+=5_TlvZcAAZ%>ta>1p$r5K@QfeBU
)8$z>OZ_VYPO4C&V2LzvU#2nFB8}PIpTz9$Phm>vgYN$H<<IP6fA&&R-{%}iekar_WEt%3wa$Mw^SsV7&+AMYvxsnQ<?!#12#L%+
aV3#=&xcBXG&a(bX`xc687fsOHI%0L{%)}n{c@R<AnG=<76mJJ%px6_uUG!HQA4}R)z8+Sc<Be{=p^9_8Id9p<Ug~$6-xoLC4?I}
7Ac82+Nm3>oU-v|rBjTT6d+YR@7^tS{#2#2pIMdN7YITd?lmT$*{m%2%d+lruA6S%Z(0XKf+^+Bv%Cm8$XOcH4~i5sXt`_&n0gn6
{V66;W36!{QeN<xS*v#~TtgZ$<6XUMZDmW>s<<sK0j{UKD>8S~@u_s)-+WMUlQB|?87XdJp2xRky`J!5?kaf32l3^x)Rn_qT>6-N
G&ij3k`M2N20Ba*JgJCw)#a;V(K0=n$NV*W+>(b!sWj-4<~f2}el=v3bC*4@DQmzaBi#8-YOd+&Nha-gvg%A%bSFhuAbZ!(>d@jQ
=hJ(IT<P;>Z)y4si<(dRfnfzK{{l;Zp?CE_TC0O~W>KE4+}$QGF?h6}`~)J}m~S|n|H@Si={+(QSyRU@Hw}0uY6Jm5rlB{(LU)MB
K)n~oa}O1Trt)HVSHg)FqEVhZ(G<%~SS*kgg5R`e;4VXe7UhMd<3}+<d(WVqG4!Tt6~yguY5?IUvxNt&)<)hue8MmxTqREsULVP{
IV_o_%}K?{f#n?J2Lh^W3@-N}mcrRHy4zR=SFnLM%^@k`I4eGjr>>fK!aAAcktysr@x@S3iNEmVnsn*;&^Z`oUXFOmOZWLjy&Thp
FUo{(m?8=j+*YhAOt{IfdP!)e^q8OH^H)xUyoznB@Z(jYiSdQQm}ON3K_Frq8yTn8+i#qQ>2~)AvSOA%o;}AM3hd*&m2pz&?MKUE
iy6oEhreR(?(=0qp_rY;!Yqr04VD`$XM+UyhPNi8;))(&GFH6GTP3*~Jh=t=go>WN@D;ucM5Q_e!UyD$Ezv$M^RAkL-hLtvp(voJ
ujM(%Q*qGR&cyRImq*BuM%1XdiY35-Sf$0*d2tY|hEeSFmNEaT%DqM%V*Vj4xi*S0z_4)$ja-4(+Ki>z?VROJeQ;@O<w21=T}oSf
scdc9Th8?w^>$m)9BdZ=*P>=CC;GWr;swk5@76?M74YFi+YJ~>xknmLo<E%>@y@=)Q;Ucy(Rmt5xd0ueuX!djbnB<w#3eRVuCiuS
dEP`|sM@eeMK?~DHlDI|s*>0Ad`Ho_am4Fz&c*S{(QHyUr)dBLE;(43+<kju;_GrVC;(fK#aHYp@2o5A`!CKUTt!F;kzU1;o`IEq
Vj8Il3BZ=1=)y(jVqaPm9LfqaS)07WtF&KQV3)^0=^#H}ycZ9g{0Uian2PSNsK~yOtkly*4%6(_->I?_DS2UdP?Ei|&mn1LR9IU+
Ts8~m;S{{`Wx*CBe*wgn_R;;W!z(INsm6NKeLSaUcS@9SS8aM0$2RZq2&qNabSO+@s@VU4UTc$LDwK<Zc%x|F&lSnDE1Utob4q!y
bV~~Ao+r))z0mrLmy;LxzTjk|p>=sFjHS2(>Zm-=U@yXZ{heng>3NJEQ;0))LDWV)Mooaoe^-+Ds3h^{ywglTZ_XvxF0!|ImzP;v
Fmsbfu~0C`!)!Kz00c}{O~K#IgMhhAFLZi?n@;!kqP^!K0uqMkx6UB)urBb%`-4{ds@ZMApY~wS`vXy6YTPs%|D@*!^#2xAj|{Rj
BRX5S@C@8UK0IS(FiusA(PI?5e+Ll?=9BuOs&yxRZVW5;OaLS4-Dd(K>6ELyp=(>A0xo!^HmKw<;(2$M34hf_f7RY!8pf5-KGFg?
H`tbLFu_u3D&{F8(Mxo4ZwEx_k000A)}sPBaKd&T8_1*vs<k~uVsS?QXLVw+fqz#m-Z=Z)Tl=&Mht<VHZM8q!gI=q9+Y}|tw79!l
)y*TR-dF9*i(a$U@2B-sB~@QKUjSscn)(JRS-H%KJ5qSvycpc|nzFc>q1qO$H;}@g4vO}m(*qPupj1?6sbH&cXVuwMR8l#};qA0<
|FAE6oz55gqSx#EZddI=$F9JZTep3=X@F=qKVJ-5-<q;Y`~O*e{qes=U(gT
"""

def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
b=''.join(B.split()).encode('ascii')
assert pin(b)==[7559, '46d668caeff3160308ae5ee9ef7f5cb3cef15d48164b4e9f25266c9f0560fa85']
r=zlib.decompress(base64.b85decode(b))
assert pin(r)==[15477, '4fb5bc748d90b4200fbb0235d1a2edeeed309370e4528274b6cde5ec26e83f6e']
M={'broom_control.py': [7762, '43d6dc75ff87ba4a9282ee3f27c9d130eed99ef49fac32f75f2c3c881a5d2f15'], 'verify_broom_control.py': [7370, '9df01d48ca770639ba74de060619e7f14efa07b8aa3d837a31ebf68e8cb9b4d1']}
D={'broom_control.json': [5784, '15d86cf49e6b0ed5a84a9dced39a1dbddbb99da251fdb5a705b7848cb5f26413'], 'broom_control_check.json': [519, '4edddd62ff48306f8c21ce563ea83639875d0baf7a7b21b4f6bcc2127cfe8437'], 'build.log': [504, '3fc7bc07b06ea9e375a9d8631aa5385e98f96b7195ecd3f3dcfb3f02883f3d4a'], 'check.log': [374, '2cbce973dadf95b2b6d3d7e63dfc8d12bdbabc965ba16508bb1a9aaf7d0b8d5d']}
S=json.loads(r);assert set(S)==set(M)
for name,text in S.items():
    b=text.encode('utf-8');assert pin(b)==M[name]
    Path(name).write_bytes(b)
mode=sys.argv[1] if len(sys.argv)>1 else 'all'
assert mode in ('all','check','extract')
def run(name,log):
    p=subprocess.run([sys.executable,'-S',name],stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT,check=False)
    Path(log).write_bytes(p.stdout)
    sys.stdout.buffer.write(p.stdout);sys.stdout.buffer.flush()
    if p.returncode:raise SystemExit(p.returncode)
    assert pin(p.stdout)==D[log],log
if mode=='all':
    run('broom_control.py','build.log')
if mode in ('all','check'):
    assert pin(Path('broom_control.json').read_bytes())==D['broom_control.json']
    run('verify_broom_control.py','check.log')
    for name in ('broom_control.json','broom_control_check.json'):
        assert pin(Path(name).read_bytes())==D[name],name
    for name,want in M.items():assert pin(Path(name).read_bytes())==want,name
    print('NOVA24_ACTUAL_TERMINAL_CONTROL_COMPLETE_EXACT_CHECK_PASS')
    print('NO_UNIVERSAL_V10_C32_CLOSURE_OR_ATTAINER_ASSERTION')
else:
    print('TERMINAL_CONTROL_SOURCES_AUTHENTICATED_NO_MATHEMATICAL_REPLAY')
```
