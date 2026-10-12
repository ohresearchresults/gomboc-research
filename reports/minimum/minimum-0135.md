# minimum-0135

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# PARALLEL_RIDGE_FOUR_A_COMPLETE_V1

## 1. Resolution and exact scope

**The entire pure-four-A sector of true two-apex E17 bodies whose ridge is parallel to the octagonal base is regularizable.** Every such uniformly filled body, at its actual volume centroid and with one reciprocal metric pair, has arbitrarily close actual convex realizations of the same full face lattice, with exactly the original feature-labelled strict equilibria and no physical weak equilibria.

The decisive new statement is stronger on the previously critical subcase: **a horizontal weak ridge with three basal A points, all free vertices target-side, and all their horizontal moment coefficients zero is always first-order regularizable in the full intrinsic realization space. Its entire nonnegative intrinsic stress cone is zero.** This does not assert a one-dimensional signed stress space.

That critical geometry is **physically realizable as pure four-A**. A new exact quadratic-field family below realizes it on the previously exceptional degree7-source/degree3-target incidence, with the three basal edges matching all six source-side vertices. Both free vertices are target-side, and every simultaneous horizontal motion of them, followed by actual recentering, has the wrong sign. Nevertheless a true ridge-source motion unlocks the contact. The family is pure-four-A for every physical height H>=2, with strict8/4/10, and there is also a separate exact H=1 control with strict3/4/5.

Thus the failed free-target actuator is a real physical method boundary, but not a full-shape obstruction. The new proof closes the **whole** critical horizontal residual, not just this family or a finite sample. Combined with the accepted normal-height and basal theorems, it closes all parallel-ridge four-A configurations, including weak spokes and all three two-apex degree types3/7,4/6,5/5.

Unequal-height unique-adverse configurations and the apex-at-centroid-height wall remain outside the new theorem. Non-B8 E17 lattices and mixed EF/VF packets remain separate. No weak110 body,110 attainer, wholeE17 exclusion, census change or improvement of34<=C_min<=622 is claimed.

## 2. Input authority and verification status

The complete1680-line `research-journal(20260920-180602).md` was read consecutively through EOF, including the full literal required parent and its recovery capsule. It has302440 UTF-8 bytes and SHA-256 `a2a9f942eb269188f01da4c748bd6e895bb7092d9217f20bd4028219bdf760f3`.

The authoritative parent is `minimum-0132`, title `NONBASAL_E17_NORMAL_AND_HORIZONTAL_RIDGE_V1`. Its41068-byte compact JSON envelope authenticates to the required SHA-256 `efc1244ee8a82c455c640b3c9f5674520f4579b93aff31d50744e24cb616496c`. Serialization is UTF-8, `ensure_ascii=False`, separators `(',',':')`, keys `version,result_markdown`, exactly one final LF in the Markdown string and no envelope-final LF. No source conflict was found. The parent's stated critical boundary and absence of a realizing pure-four fixture are preserved as historical status, now advanced below.

The inherited basal and at-most-three-A results are working premises, not new claims or generic replays. The new computation imports no parent source or report. The full new source, original build/check, fresh source-only build/check and capsule-only build/check all executed with byte parity. All signs are exact in a real quadratic field; no floating tolerance or failed search is used as a proof. The analytic theorem is proved below independently of the controls. No proof-assistant formalization or literature-priority claim is made.

## 3. Actual moments and a new endpoint actuator

### 3.1 Physical coordinates and admissible motions

Absorb the initial common metric into an actual affine image, then use physical orthonormal coordinates. Put B in z=0 and the horizontal ridge in the form

    a=(0,c,H),  b=(L,c,H),  H>0, L>0.

The weak arrow a->b forces the actual centroid to have x-coordinate0. Write it as g0=(0,g_y,gamma), gamma>0. These are coordinates of the same genuinely uniformly filled body, not a prescribed replacement center.

For y in [y0,yN], the true base interval is [l(y),r(y)], with l convex and r concave. Set

    w=yN-y0,
    A=integral (r-l) dy,
    Delta=integral (r+L) dy.

On E17, the two ridge quadrilaterals meet B in its two horizontal supporting edges. All other side facets are triangles. The left chain consists of the base vertices adjacent to a, the right chain those adjacent to b. Internal nodes on each chain have strictly monotone y-coordinates and strict turns.

Three kinds of motion used below are actual realization motions: any base vertex can slide horizontally; an internal chain vertex can move in both planar coordinates; and either apex can slide on the existing ridge line. The first preserves each incident quadrilateral plane, the second touches only B and triangular side facets, and the third preserves both ridge quadrilateral planes. All remaining support and face-convexity inequalities are initially strict and therefore persist locally. No triangulation diagonal is made into a mechanical edge.

At height z=tH the actual section has transverse coordinate (1-t)y+t c and x-interval

    [(1-t)l(y), (1-t)r(y)+tL].

The transverse Jacobian is1-t. Direct integration of these true sections gives

    V = H(2A+Lw)/6,
    Jz = H^2(A+Lw)/12,
    Jx = H/24 integral [3(r^2-l^2)+2Lr+L^2] dy = 0.       (1)

### 3.2 The ridge-source modulus, including its exact bad boundary

Move a to a_sigma=(sigma,c,H), keep b and every base vertex fixed, and integrate the new uniform body. Then

    V_sigma  = V-Hw sigma/6,
    Jz_sigma = Jz-H^2 w sigma/12,
    Jx_sigma = -H sigma integral(l)dy/12-Hw sigma^2/24.   (2)

For its actual centroid g(sigma), use the facet-fixed affine correction

    F_sigma(X)=X+z(g0-g(sigma))/g_z(sigma).               (3)

It fixes B pointwise, sends the true centroid exactly to g0, and has positive determinant gamma/g_z(sigma). A uniform affine image has the affine image of the volume centroid, so there is no freely chosen density or polar center here.

The corrected apex difference is (L-sigma)e_x. Consequently the true own-centroid ridge escape is exactly

    phi(sigma)=(L-sigma) H^2/[12 Jz_sigma]
                         [Delta sigma-w sigma^2/2].      (4)

If Delta is nonzero, choose the sign of sigma to match it. The ridge then opens to first order, while every basal contact is preserved identically. At Delta=0 this particular endpoint modulus has a negative quadratic sign. That is its exact method boundary, not a full regularization obstruction.

There is a useful connection to the **actual** covariance. Integrating xz and using Jx=0 in(1) yields

    integral_P xz = H^2 L Delta/60,
    Cov_P(x,z) = H^2 L Delta/(60V),
    phi'(0) = 5 Cov_P(x,z)/gamma.                        (5)

Thus the endpoint actuator measures a true cross-covariance of the same uniformly filled body. Neither a tensor-stress surrogate nor a covariance of tetrahedral centroids can replace it.

### 3.3 The missing transverse component at a free target vertex

Let w_j=(r_j,y_j,0) be an internal target-chain vertex avoiding every basal weak-edge endpoint. Put

    d_-=y_j-y_(j-1)>0,  d_+=y_(j+1)-y_j>0.

With all other raw vertices fixed, the complete first derivatives of the true Jx are

    Ax = H/24 [d_-(r_(j-1)+2r_j+L)
                         +d_+(r_(j+1)+2r_j+L)],
    Ay = H/24 (r_(j-1)-r_(j+1))
                          (r_(j-1)+r_j+r_(j+1)+L).      (6)

The first is the parent's horizontal test. The second is a genuinely available motion at an internal vertex, not at a quadrilateral endpoint.

For verification, the contribution of one linear right-chain segment to24Jx/H is

    (y_(i+1)-y_i)
    [r_i^2+r_i r_(i+1)+r_(i+1)^2+L(r_i+r_(i+1))+L^2],

apart from the unchanged left-chain term. Differentiation gives both components of(6), including movement of the integration breakpoint. In particular, changing only y_j makes Jx affine in that displacement exactly.

If either component is nonzero, move in its negative-gradient direction so Jx<0. Since both raw apices are fixed, correction(3) gives

    phi_ridge=-HL Jx/Jz>0.                              (7)

All basal weak endpoints remain fixed, and(3) fixes B, so all their equalities remain exact.

## 4. Concavity closes the entire critical target-side residual

Assume the parent’s difficult case: every free base vertex lies on the target chain and its Ax is zero. There are at least two such vertices for three basal edges on an octagon.

Define f_i=r_i+L/3 on the target-chain nodes0,...,N. The piecewise-linear f is concave, with a strict turn at every internal true vertex.

**Internal critical-star lemma.** If an internal vertex has Ax=Ay=0, then

    f_(j-1)=f_(j+1)=-2f_j<0<f_j.                        (8)

Indeed, if r_(j-1) differs from r_(j+1), Ay=0 would give r_(j-1)+r_j+r_(j+1)+L=0. Substituting this into Ax=0 says that r_j is exactly the linear interpolation of its two neighbors. That contradicts the strict concave turn. The neighbors must therefore be equal, and Ax=0 gives their value relative to r_j. Strict concavity gives the signs in(8).

Such a vertex is a strict local maximum of a concave function, so there is at most one. Moreover it cannot coexist with a horizontally critical free endpoint. For the left endpoint, Ax=0 reads

    2f_0+f_1=0.                                        (9)

If the internal critical vertex is j=1, equation(8) makes the left side of(9) equal to -3f_1<0. If j>=2, concavity and the positive incoming slope at j imply f_0<f_1<=f_(j-1)<0, again contradicting(9). The right endpoint is treated symmetrically.

Therefore, after all nonzero components in(6) have been tested, a set of at least two free target vertices can remain critical only when its free vertices are precisely **both target-chain endpoints**, and both endpoint equations hold:

    2f_0+f_1=0,  f_(N-1)+2f_N=0.                       (10)

If N=1, these equations give f_0=f_1=0. If N>=2, strict concavity forces f_1>0 and f_(N-1)>0. To see the first assertion, f_1<=0 would make the initial slope nonpositive. All later slopes are strictly smaller, whereas the right equation in(10) requires a nonnegative final slope once f_(N-1)<=0. This is impossible. The symmetric argument proves the other assertion.

All internal f_i are consequently positive, and the integrals on the two end segments are positive too: their endpoint sums are f_1/2 and f_(N-1)/2. Thus

    Delta = integral f dy + 2Lw/3
          = 2Lw/3>0                 when N=1,
          > 2Lw/3>0                 when N>=2.           (11)

The endpoint actuator(4) now opens the ridge to first order.

This exhausts every case in the old critical target-side residual. It uses the whole true polygon and exact uniform moments, not a sampled search or an assumed rank condition.

### Full intrinsic stress consequence

Let R be the actual contact derivative on the genuine realization tangent space, with all maximal-facet coplanarity equations retained. A nonnegative intrinsic stress satisfies R^T alpha=0 there, equivalently the parent’s equation Q^T alpha=C^T lambda with its polygon reactions.

No nonzero nonnegative stress is supported only on the basal rows: the inherited basal construction is an actual tangent motion positive on all of them. Hence any nonzero stress in the ridge-plus-basal problem would have alpha_ridge>0. The motion just constructed has basal derivatives0 and ridge derivative strictly positive. It contradicts alpha^T R h=0 for **every** such stress. Therefore the entire nonnegative intrinsic cone is{0} on the critical target-side residual. No reduction to one selected stress or to affine tensors occurred.

### Actual full regularization, and the parallel-ridge corollary

After opening the ridge, apply the inherited basal flow and its true quadrilateral lift, followed by the actual facet-fixed centroid repair. For a two-parameter analytic realization P(t,delta), the basal derivatives in delta are d_i>0. If the first ridge opening is c t^r with c>0, r=1 or2, and its delta derivative is R0, choose

    epsilon=min(1,c/[2(1+abs(R0))]),  delta=epsilon t^r.  (12)

Every basal leading coefficient is epsilon d_i>0, and the ridge coefficient is at least c/2. This supplies a genuine first-order full regularization in the new target-critical sector. A source-side free vertex from the parent may require r=2; its exact negative Jx quadratic then gives the same second-order conclusion. The coupled realization is analytic because the original nonzero plane-intersection pivots remain nonzero. The intrinsic second jet necessarily includes C z2=-d and alpha.b-lambda.d; it is not obtained by adding frozen-star Hessians. The underlying basal construction and polygon-reaction distinction are the accepted parent's premises.

More generally, a horizontal weak ridge plus any number of basal simple A points regularizes by these arguments whenever at least two base vertices avoid all basal weak endpoints, on a polygonal roof with the same two-quadrilateral side structure.

For four-A E17, the remaining possibilities are already settled: all basal is the accepted basal theorem; a parallel-ridge body with any weak spoke has both apices above its true centroid, and the accepted normal-height move opens a spoke while keeping the zero-height rows zero, leaving at most three A points. Otherwise there is one horizontal weak ridge and three basal points, which leave at least two free base vertices and are covered above. This proves the complete parallel-ridge statement. A projective equalization of an unequal-height body does **not** transfer this conclusion without re-integrating its true centroid and rechecking its physical packets.

## 5. A genuinely realized critical family and its exact method boundary

### 5.1 Complete coordinates, mass and lattice

Let q be the positive root

    q^2=35235/75712.

Use the six left-chain base vertices

    0=(-12/13,-5/13,0),  1=(-25/26,-19/65,0),
    2=(-1,0,0),          3=(-1,1/10,0),
    4=(-12/13,5/13,0),   5=(-23/26,31/65,0),

and

    6=(-q,-5/13,0),  7=(-q,31/65,0),
    8=(0,c,H),       9=(3q,c,H).

All true left-chain slopes are strictly increasing. Put

    w=56/65,
    A=54/65-qw,
    c=3(-9403/263640)/(A+3qw),
    gamma=H(A+3qw)/[2(2A+3qw)].                         (13)

Subtract (0,0,gamma) from every vertex. These are complete exact Euclidean coordinates in Q(q), with M=N=I.

The outward maximal-facet cycles, in fixed labels0,...,8, are

    (0,1,2,3,4,5,7,6),
    (1,0,8), (2,1,8), (3,2,8), (4,3,8), (5,4,8),
    (6,7,9), (0,6,9,8), (5,8,9,7).                    (14)

They give10/17/9; apex8 has degree7 and apex9 degree3. On the certified H=1 and H>=2 members, the weak arrows are

    0->1, 2->3, 4->5, 8->9.

The three basal arrows match all six source-side vertices. Only6 and7 are free, and both are target-side. This is not a relabelled balanced control from the parent.

The exact base integrals are

    integral l = -54/65,
    integral l^2 = 7047/8788 = 2q^2 w,
    integral y l = -9403/263640.

Since r=-q and L=3q, formula(1) gives Jx=0; formula(13) gives Jy=0. The actual mass is

    V=H[18/65+(28/195)q],
    gamma=H[1013/7097+(9464/21291)q].                    (15)

The source checks these identities against two distinct positive apex fans, including full second moments and allowed flat selected cells, and reconstructs the maximal hull from all supporting triples.

For **every H>=2**, the only physical weak points are the four listed simple A points, with no harmless primitive zeros. Strict labels are

    S=[1,2,3,4,5,6,7,8],
    U=[1,3,5,9],
    Hedges=[(0,8),(1,2),(1,8),(2,8),(3,4),
            (3,8),(4,8),(5,8),(6,9),(7,9)].             (16)

The unbounded height assertion is a continuous certificate, not an inference from H=2,3,4. In the H=1 chart, use M_Y=diag(1,1,Y), N_Y=diag(1,1,1/Y), Y=H^2>=4. Each primal primitive, and each polar primitive multiplied by Y, is A_i+B_iY. All64 nonzero original signs satisfy sign_i(A_i+4B_i)>0 and sign_i B_i>=0. The four zero rows are identically zero. The full68 coefficient pairs are generated by the capsule. The separate H=1 control is also pure four-A, with strict3/4/5; no claim covers all intermediate heights without their possible EF walls.

### 5.2 The old actuator truly fails here

At both free endpoints, 3r+L=0, so both horizontal first-moment derivatives vanish exactly. For arbitrary simultaneous horizontal displacements u,v of6,7, with every other raw vertex fixed,

    Delta Jx=Hw(u^2+uv+v^2)/24>0                       (17)

unless u=v=0. This retains the adjacent mixed term. After the genuine correction(3), the ridge escape is negative. For all sufficiently small nonzero such motions, the three basal A packets stay exact and all other signs stay open, while the ridge unfolds into an unwanted strict unstable vertex8 and strict saddle edge8-9. Arbitrary higher-order parameterizations of these same two horizontal freedoms do not evade(17).

This is an actual, all-orders **restricted-actuator** obstruction. It is not a nonregularizable body: here Delta=2qw>0, and moving the weak ridge source8 positively on its true ridge line gives the positive escape(4).

The controls also do not realize an obstructing affine or full-shape stress. In fact the contact-zero affine obstruction is absent already: the symmetric matrix

    Haff=[[0,0,1],[0,0,-1],[1,-1,0]]

gives positive first coefficients

    [17gamma/130, gamma/10, 7gamma/130, L(H-gamma)]

on all four rows. I+epsilon Haff is SPD for sufficiently small epsilon. This additional fact is recorded to prevent interpreting a failure of free-target motions as a global stress counterexample.

### 5.3 Full actual contact rank at the critical control

At H=2, take four raw directions: move vertex1 by(-12/13,-5/13,0), vertex3 by(-1,0,0), vertex4 by(1/26,6/65,0), and vertex8 by(1,0,0), one at a time. Follow each by the exact correction(3). Every direction is a genuine full-lattice, true-COM motion. The actual contact derivative, in the listed arrow and direction order, is

    [[1,0,0,0],
     [0,1,0,0],
     [0,0,1/100,0],
     [820845/422656-8177q/4064,
      832155/422656-24869q/12192,
      -16095/845312+481q/24384,
      -11745/4064+3045q/508]].                           (18)

Its determinant is

    -2349/81280+(609/10160)q>0.

Thus the **full intrinsic contact rank is4** at this actual critical body. The code checks the coplanarity and actual first-moment identities of these four realization curves, not just this matrix. No universal signed-rank4 assertion is inferred from the fixture.

## 6. Complete own-centroid curve and whole-interval certification

For the H=2 body, denote its raw vertices above by v_i and g0=(0,0,gamma). Define raw polynomial vertices W_i(t) by

    W8=v8+t(1,0,0),
    W1=v1+t^2 v0,
    W3=v3+t^2 v2,
    W4=v4+t^2(v5-v4),
    Wi=vi for i in {0,2,5,6,7,9}.                       (19)

All vectors in the three basal changes have z=0. The moved basal vertices are internal source-chain vertices; both ridge quadrilateral planes remain fixed exactly. Let V(t),J(t) be the **actual raw volume and first moment**, obtained from(14), and D(t)=Jz(t). The final coordinates are the following complete rational functions in Q(q,t):

    Xi(t)=Wi(t)-g0+Wi,z(t)[g0 V(t)-J(t)]/D(t).           (20)

The actual centroid is identically0 and the actual volume is gamma V(t)^2/D(t). The three basal escapes are exactly

    t^2,  t^2,  t^2(1-t^2)/100.

The ridge escape is

    (L-t)[t D(t)-2Jx(t)]/D(t),                          (21)

with positive first coefficient -11745/4064+(3045/508)q. This source-only recipe determines every vertex, actual moment, pole and derivative; the code includes all integration helpers, not an implicit missing solver.

**Every t in0<t<=1/65536 is certified.** There are218 polynomial guards,4438 strictly positive exact Bernstein coefficients, maximum degree40. They cover the raw volume, correction denominator and determinant; all nine centroid-inside conditions; all56 strict vertex/facet nonincidences; all82 strict polygon-edge guards; and all68 true-edge mechanical primitives, dividing each initial zero by its indicated positive leading power. The full old strict labels(16) persist and weak000 holds throughout.

The source represents q exactly as a+bq with rational a,b, and determines signs by rational squaring in the ordered real quadratic field. Each Bernstein vector is returned completely. The positivity proof is the Bernstein convex-combination identity on the entire interval, not grid sampling or floating arithmetic. The endpoint is independently re-hulled and re-integrated from two positive apex fans, with its full physical census checked.

Actual mixed jets are also audited. In homogeneous polynomial coordinates Z_i=D X_i, the code verifies identically

    J_homogeneous=0,
    V_homogeneous=gamma V_raw^2 D^2.

It computes both vertex and pole first and second coefficients and checks, at every literal incidence,

    q_f.h_v+x_v.k_f=0,
    q_f.eta_v+x_v.xi_f+h_v.k_f=0.

A separate straight-vertex expansion retains every shared-triangle determinant term. Its genuine quadratic centroid coefficient is generally nonzero; adding the linear centroid response to the actual acceleration gives zero. The independently recovered contact coefficients agree with(20)-(21). Thus neither actual recentering nor the polygon-curvature contribution has been dropped.

## 7. Exact source-only recovery and observed pins

The capsule below embeds the complete18112-byte `critical_ridge.py`, using only the Python standard library. It reconstructs all four static controls, the full H>=2 family certificate, the true-rank certificate, the exact arc, every Bernstein vector, the mixed jets, and the endpoint. No old source, parent report, numerical library, external file or network is a dependency.

Observed environment: CPython3.13.5, assertions enabled, `PYTHONHASHSEED=0`; no RNG or floating computation is used for acceptance. Save the capsule as `recover_critical_ridge.py`, UTF-8/LF with one final LF, then run in a fresh directory:

    export PYTHONHASHSEED=0
    python -S recover_critical_ridge.py build > build.txt
    python -S recover_critical_ridge.py check > check.txt
    cmp build.txt check.txt

`extract` materializes the complete plain source without running the audits. Both source-only and capsule-only cold build/check were executed and matched the original bytes.

    recover_critical_ridge.py 10494 bytes
    SHA256 c381fddd802953dc94be8cb57a132e40493117832952eb5bb9291b6be4ba3fc2
    critical_ridge.py 18112 bytes
    SHA256 551e676d836b97951d85d48c157ebb3fbbc9ff1e4c02cb8c07c53852e57259f4
    critical_ridge.json 1969450 bytes
    SHA256 dc02862ba308f010514504b70860a32c1f98fd9cbd46f26c5bf9d0511ff79c79
    build.txt and check.txt 508 bytes each
    SHA256 8805f0ca4655e67de3dc0d53ca79f32af1e8378025ea769b5ff135bcaeb2ab28

Expected complete main stdout:


[Encoded source block omitted; the code in this passage is incomplete.]

    critical_ridge.json 1969450 dc02862ba308f010514504b70860a32c1f98fd9cbd46f26c5bf9d0511ff79c79
    PARALLEL_RIDGE_FOUR_A_COMPLETE_RECOVERY_PASS

Convenience copies: plain complete source (`critical_ridge.py`), complete exact report (`critical_ridge.json`), recovery capsule (`recover_critical_ridge.py`), executed receipt (`build.txt`). The literal capsule is sufficient without these links.

```python
"""PARALLEL_RIDGE_FOUR_A_COMPLETE_V1 exact recovery.
CPython3.13.5 standard library, assertions, PYTHONHASHSEED=0.
python -S recover_critical_ridge.py build|check|extract
Parent minimum-0132,
SHA256 efc1244ee8a82c455c640b3c9f5674520f4579b93aff31d50744e24cb616496c.
"""
from pathlib import Path
import base64,hashlib,subprocess,sys,zlib
assert __debug__
DATA=(
    'c-pl*`*Y$rlfUP$aMjj#ejpM|-mscFCLxn#vPmYdnGDCdjBUUP7-Aa&+1vm9x?7TM9+{c_Zf|P`Y^l|1wfZd)UDvN0H;s#n=7n=}'
    'cKoU7oLt@CI1T6M>W}M-=3Ucyus1i3uIFig6lvR=_V(tkmZWavyRokg!cOeQ^Sb6HNf4*uC`y=i{djkJb$QyjJ-ux<k9lQtV=P9O'
    'Z#6Ft)6jDVP8|BZU~@dzI+JkV|Bu%XyyuN;Hx8l{koBBf-+BG&9v`{;ZzF%&zwxHid(Yqf$Tn_I8`a%CE$Di7b!R6C4%~yPx3jzJ'
    '?d?=L+umV!cW-}Zw_54$?Cu|S4!7NIciZ-NEBgRk-SIkm_TJ9np0~N7>-t7F9u2i_?0Q7I77oXwIMq&M15l!!2$(R1^^Hb@48|J`'
    'J7MI~H~}(r(|)m6w2q+_*rYnH;dMhkKP97xX?-_A0H!7LWaGHXPmJx|>h><%-`%&X=7u)_-fEv~8=4<<HOC2~Fm)Uw2?kx}@(Szl'
    'iV2-s*ww-$jBsnbz;M}TvxYF6E~Bpwcj3|9>;PymNP?x#6T>yxiP16DG_LQfS!N1<G)jwe%$V_+ov<)UO|upU=_HP{%TanZ91nsa'
    '>|@}=uo?es%*?v%{%nY8OS5chc*I#9C#EU6oLbQl1wBbeHpge9EQuH2Inl|a^N$cM+YwQzjP$Ds;>8&<f@WrkXi;#($>9Hydlqo7'
    'bX>K>>fx=!vW`wEYjp)%i54ztQUs>)B=E!OKS`v|XM(gckTw%^)rDQqmY8b6fK7MHXJvrd@^kjCl2u^wR*}Qw(W`=rh<G_uf%u5%'
    'mh1YxqEHz&Au=t?C`Z^G1O2vH?{I-%d+mpVK#LG54gC+h7W3Fb&Cxo%V|D7$))uekONtdy!OOqH&=VK*ab>f`j&fwG2G&-SiVE)?'
    'HC+en(Xw)2n-mjm6l)6#l7ziTLg&N@h>SU6=!c3~mXE(z%q3uV5xA2BcQRlpj|$*t=zU%sKoTUySbVLKBV#Qt(=rU7ntXgyoEoI7'
    'B1P|{-R357#{9jK!3Vzt&$9u&Uz*@U4*yFNe8?woJIV4^lf}uHt(HL6T`Q_e9E{`TvHHJ~lJT#^v|jXo84Iq!+;{;wtT51s@7(xo'
    'n9Q`cH>O~e`M@1^e2_-gsihOJ0LH8|*Sa8OGd9=4NP7#%;CMQ~_9@uOHQ?oUz!QiFf*jtH@SZgj@CXgo%paviq{(Dx7&B`<P6l#?'
    '%lG0@l2B8|X18Uxtxl`jF1zpnPj;KhrwX=JL@$$1Hn!QKSK#!66frU{!wHl@i<k@B&5ff+-a;<2D%)l|4BR=}Gux$>5teKgvICQ-'
    '4w2^Aje3ExOTBvlcW5#gxyKFxiW$4?0G{^E_QuIAZwbaE5IqFG(KQ8@E@C-)Y;WA%oWZOf5X!vP6MdBIwgB=35IsNT)7oqhM22UU'
    'ZI}U~wLkybAe14a0YNkw2C<t4#?d2M4eW!ZD^`0jg<WfxyjBh7sWp!`lOP2axsyR^EYK=;#bm9vx#^C_K?LN7CeG-GUaFt~0R&pZ'
    '!~jsG^GILw*yP;aCqw8C1_riup{bg$ABIld!6d-38%I}{ca5XFTd@bgMc4)SgnfWd;3upVH?ltgT;IgHCJ`E;)G);&L-xd;5pOZh'
    'GbGO{CZIzb8ga4bDDTEMWcjyN*fyDbf0pmcf^z=7=8d8>j3xnDy%q{iB*149HW&GC?RwJVtv9LL)bWNLep?_c+xV9Bh%fTFI03C{'
    '6I563MJSi{wz##vsqFh3k}CPGgbZ;2tL5v-tz?iCx;0$rg0|qoyC8=-FS?*od8<j(AuY2-T3|PntzTq~9LITuLR}oy6}E0YAR2RU'
    'vq78$BDgQ^ZkP2}_V(nKRcTWLz96|ctZV)Ue)UZvydanXIDx9z4DkvwSzDNv*dOF<U8ISK0_hfHdGmLf>dhrr;i1S@c&!%O6=RD^'
    'I%hZ<)pRcO6eAe~ni3P{^o~oIif{#OBpS@ZMl8_M!TH>rhN*lvArwOwC&$^9vb|qA<j5dtC+{G>+aT2&0+8{Ix#M8QzavEt;C0OU'
    'Isab2;jPwZDeeVJwQaVSZ6-9;UxTpMPZQp17vvHQAuejnTQ~t2R#dHgbhi!BDq3;NkYa;i1<e~HyTAm!DN!I-qi_filL3+DDoMBl'
    'k|<^Ae6#*g;{MhitPee@an8u)8E?$rs_x|4P{fn%(gF`^H$Vj#8bD_mZ}4or;af(aHG|g`D$OmsTFG|dft|A(CTW!05qNz!3cW;_'
    '!|`YkEV1<8SM@q!Q@juhkC?qB^fm(nCXA=B^@V)`132zxP0G#H<IyV;2V3tx<9FYUhcH7<Fo`cSK+8?(8l+djB~18|7=tWO3z6CC'
    'x0!h8LXYq$!b~G9o0zODUOM!G&kCIRvNJ>Eo5F%mix!-eP9R1zKAr;Jj5$3FGV0LQDYn_z)`ckwZB^0MFScz%8!|^VwJ=HnE-*Qr'
    '^g}~;2GD3qYskU{=%hzb!2sYY(xWK;t^t%1^`}m2)@$^|bR<Hr;V08^3Y{imy27MqIGKK{*ILRkO&6WPxN9nUr(n?AOw;dw06krS'
    'J_TqJ24xckH%Os?I0VOV;tj&)%(+g@_Fu|IJqN}qC$BIFx+z2x<rBlMG8=*kc-qAWkTZC!?y~A0HQI-4Z<ktah(YNK8X3e40#XiN'
    '9KB7WPmFDw27_F@a)8*wxBA(D<77MHWlnF0I~5$Wy|+^_>kVFhv0lq(gZc&EwqEKUd;;8-(I{P5ueeL@s|p>5?ieyquy}KzP6Znx'
    'cE%-Q3|f8xn}IJNizs?zL0F-=Y!}-xMeyMH6kjgXBP@ZUE0`LL9~m6K!pZ7G6N7&w=~D=^V&)$%_8hje=<k8^DTO!ZoIlaS4d-zd'
    '2v&aQZ-uz1Qt}UBy*)0h%sE(@hYS_!7U!r<9P_GgpqIk<_X?IDrU!!};==lH$cu(?A^cS#W})_wS&1bBW72#I3dvrE3>Bml#DXIL'
    '!4UyZ(KQz}4`lolG|qhmg#-TSJ-yar`h#A3VEQ+`_KoSo5!Pxz>28?bbt8Ca`4wP#8@kl;^xAL;x*GavAC#5pZXCFJtpSL!Pzwoh'
    ')We<&P>tWT>(O8yjfSB+NVL&3h_x@qi^;SXEljkuAAtKv!Ze&h8u~H;M4)Rx`>3lOS2txn^LlMP)04GK%0xXr2os1rHa&BxxaqNL'
    'Q-ppk%$D=b^V%zrBJyR3%FG9OD4(*>gK?Xf(EMPNU}cpK4@F&6O1;hTXl$52D!sVTTp?Op5GodSJkGCy^iA*Gdh3h;R5j?@Xkj0^'
    '`pm%>;sUgJg>_I)H-iVz!@pNsg?Y+_q+8%?zf)jcD3f0Qv`l*a^D?PgG{*q2Z57v4Qfq=tHA^1cMGqiBRprhVfi3Y$C~XcpQ*Z>?'
    'sl~0Zgi)1Cb-s+^_;1xvb0)f5nPj@_82QWPOCgXSgaHBW{G?Fn$_1=1RJwWjDaD9Lk?^!6oG4-F|9|ICzZbSZsLyAm1rSse_s-?i'
    'lNTE#u38P12nm~&ycJsfu-jb`!6!=!`}%5yBnR>V=%uQRC~x+|ZtD1>R{_DEi;P99tMqye;%Bp<YLf8hT493!9LJ+EAeu|EgI*j2'
    'i-Z?QE89ORzF}KtDN@+fR)t}Rcm16k*RtS70SH7>b4O%KB1O8U6zTf=QjJ2UJ0ho%-h^rq&uz?MDCMA!tj`pkFz9EANuDzZnmR!Y'
    '5*mb&F=oLyLAoM7-V_YUz+04%jA16r04U3PGOZH>^KIi9#EsEY1Wzkz-gC(|3#rv}-V>FuMny!#n6o=iu-Y*M*+9Z?+MPQepyZ8$'
    'Za4Hoba>#4;?bnnhh6l+Nu{qNMz$SZ!l{c6D%pgjgZaQ$NR+NIPgAZOb{!H~K8Eitd;zV4<=E}AkF`M86pbD>R%K%czN%SY#tNzw'
    '3bNga56%wAPK@sfJ7&=+9)b^L$z+TNf(eTQvP$1nw3e^)jUAhSwHT)6*~E9uB>K~LM%h0a6}&g9`lC@_RtFthZ;);+kQj+!ktnuc'
    'DPnoS=!T!W?;^ARHnQM-WYxcoOv=JH2si_;1;JFCtnnB5p2tq@mdt-(kT;1zwkC0qr_W5(b(U+XD<zmh82JVB$^Nu8ZJQ+#EKb|('
    '8B;(ROro+wJAufKdNy^Is7)c?@kz~BkOxc11Hw`A3H@(cGfG2<+>$hQu}n~gC@&3Wng@Cnk3wGyW@!*5As%3ZoVyUkMLjgKV1*&#'
    '^UG-*g3^L}N`rWaYNjx${Q;{tWBs<uK(dXPvRA44@T3~Q0WWYzzzXr)C@Pd@y=Tip%@fGX)`OBlGArkp5LC1Ns^~92pvq?8mQ`IG'
    'p>hVBbFj9q=LLg*lkz}N-eBjA0_}v+tbYRDEs)+=q`i@oLiV{=WjMqns<6`QdWG88n$%>*F|nu@iynAZ+ZXSBEHt2;Q5hr<jR7?V'
    ')Cd?nTS*$#KS*L`%<ofQmHL8Wp8$k@1sPC5VFr})Tq&{ddy=I<@Cb8K16coK*p5P>Rg4vfQJ&2_>QjqfC`wRoJLj1K!c4YWgS-#p'
    'N`}Y1LY1?Ad!>IBM|BZKWc3wu8Pzs`wLeq}8Jf@?ryIses@M8crdpB!M)^*`XX&*7y3v>@@aL|4Uklu2B8J8P^f2;5KY-ZL$t;0h'
    '%O07o^u_7fkR#f~hAK2vnLY@kz>V?lj{{Ps*HG4&E|*rE8uCT8U|B4oO>*4WGo%y4q667UOikPMUPZk1@Yx*>UEZqzqw1#+Hd4o_'
    '4l;NlhZK{}c3mP8*(vPI*IX5g>0i-JVIB{Ft%J4*Z14$^L5A_wwL#U!uUH9?opxIWKB6$eQj|b~+0J0Li!jw9%uWWgqhLs?5pcIn'
    'C5;^jxzvEHm}%^@gVl4SudSm;u*FnbRnK{ORkc)?dd<}eL!?Gbmq76lCF2yeo6ENKt64wh=P=6#czoWX<rP*oWxWdMsaagDc<fc!'
    'gUQZ;S}ai(cH}Es!9F|h7iRgM<hqJfKPk$D_3MlD=b_IziH!9C9JJ6n6zjaH8$&*$46ZVMts3lC3t7&x56iI2v<X|FxNUQ(bn~7$'
    ';#|xiCnnkC#zi?bEdv_Mr`Ea15f*VB<hTwA*8$<8;np$w*y{;;*wG~Rf-)XJXu}cRI)neQijug)07BQW7e?+t>x}$4xY4U$6aD&C'
    'Ciz#ZlK+sf^Q5p1SFqW^06bCEda+)!g{0OwT0LA~LbbC~;vs=rY5CPcUTz^btJ#=`L`FvsIt~Pwt-Y+1(B=IWZEBgYA|RrH$O8?D'
    'mV}UNLn0iECW+RC)S@i6xepw9L(?<RMjbF<6FNy_uyAhx;Wb1dAw>Sea2EI!djQYwe$`wQ4P53_C!${5GDJOBoG07z6OYYNjP6CT'
    '>dvg+xAr9C@rfA|tH65b-OqaWp?7L6Y>eix^Si>v+!wU^{7&w{s|83WrHM5yO|7XZcVUNoVorbN7lD38V^KtV6F2t7+9)9bLI!Rp'
    '7_hM^4$LqUQb`adKOZV}F-GD0Q>OuXO^gHI^cuu^ZTuH10H8y2?@UJnh;?;_#aC=Ye@E9oMJdt&FEtwC$?GWA!HNhV6<dPmn*}kz'
    ';PwF!z{|)Pp`{^!*<{F$CqOD{|9Q;4U}-@q<+-YO%B`$;uP*eM^*$G7HE%<Vf(*r<$jqowO?|PzR=&azLT4ZNgF(Jo%mlKUFC_%Y'
    '!1bPaznslF6|p=W)r!199o7@1$PDOur<f4*BLuG;jiM|zfJqtn0~+v;9v0JtD7w8-gp*)A1`}aPV#TIrOrB;fk(t-m>6B(P@QEWU'
    'sTLhBk=8|B7WKK@08DDsV;@AK%aT4<TY;U~bDz%L;&4bsYI(f(ZZIl4J9(!|ogM7Vqc8d|=~}c`NS9eo`q^6-Jf(c=<6Bul_7SqZ'
    'p{kSyta=K{xG1~0G0?$sn$4`piJO3f#J)&zAU}$(QyhL3asmM*_exahod7)dIB;Gj;C?Wyq^+~5g39@UsQN*?Gu|vz*p|D=dKE<v'
    'XmT=o1xno2C)`(c9@;LxSmWG<Vku3S9lTIsA3$P1PB=!~d%L^ad!UK#U<$TAL5UY-P`p||4t+4_@K#=>>b0baYE!w2_}oK|2>kLU'
    '4F(_H2N8RaE+Cq`lnL_Pi39f;6Pa<c#j6<sC2k9`?d3WoFf&A9)?ogO7`@Fqu$0JG4(Sc=EMbAn+&a!4e^leagDDtq)*k|P9<ZAr'
    'J5_^L2LHsVTELzH1|h#XSW}&cg)rqI;Cvd0vo&~pf`8w|0b77BIy+*UeULHPta!v$Kq4)2MnAfvd^H=|Fesd&5%F^HFldR>VN9w-'
    '7KKgOAu%;?<YhoZztx$35C2Z}>~;!_cy6z$$UMVHthDi8D!LW2HS}MYG(qn4l@+}i9;o4~@L_uGoaz11aMTMZNO6RZ!$WYGMlX7}'
    '+A-P*o%jTK7Je}uf}9CBM1i~D;A(lKy9~4jr%05f0vC`_J6r5t8m^1T6PDvo20%ZBb<lxdgj@EHB8WyZ79?z;J>vzmivZ0jL}d>B'
    'tb=mJJTM{LAQ|BR{6q~N@LGUSCI^2p;Z#9ifzC-{@8LZG(ZzJ3RlpyiU5F)9EJ#f!NCsA&@q`=fhfqJ0=|gwsi0ZUn!*jCSAjqQi'
    'vPpn3C@p#oKLxdsKOTiR!Jm4*&8Sp*#u(r>W$ZaiFyj_EyK1@#es};I{3UbgE~vSqvTg_oo>fl$n|1=s*FfYZkf~$T3UccX!Z*6Z'
    'ruktkFP6cY1_M~7uXW}kH3tvy2cA5*VZ8an<lMs*MR_O{Mt(43(_k?2!gQ`eVR?YhjBO^;VY*(qChMgOmj;$pn5diJp(GmWUrgfb'
    'Ut2^$mST%Hm3T_BSejj;Dqf;nPON3L_jNJY`>JBSuf<z*KhCBV;6f_x&FMtty+m4j{Kpb$OcWjqvpi--bxj)mDC%Xjtyx;ISc-eh'
    'f}cl>bRG+JI8}vTDlVcY8M+W(&UlM*pIDF>D=%ot84IN}0gstEr#pVROyECA*H!gxrD>tyMm?0lWEldNsJGkjKW6vYK~4^{P?O75'
    '1(dO+<Qe8u@(hn_<r&(S<r!cLRXC-$f+Dmz_>CSRqeQP2Uce-vx`TO%F)i>G6ko6HNSn|Pdwr)*clMmFI}8VNqvIw4b5kdM9SP%b'
    'CJG0q+}6OV#3|GMa2~lIx;<nado-DLS!}Sku<4PX{&)2Q-`T{2C&Wod9rZ8rdEGHb9hf&#iR7A~T@dwd+`f7RZz@{8;H|kYq8=r('
    'S>B?HGFYOYz(<K*Y<#iBSUhr@ko}=OFv^Hkfr}RfF5Z^lzldU*g<3{a<Jc)q^+gon;Kk0dBZV2bc$4trMZp(BdZWQUn(S>&OiwFB'
    'p2=`N>2Y=0Tgk7{DD7Au)ek~APkJ)$PkLGI*Rwu;D5id*xxx8Il?MDcACQ~5a%=F30p;?dUm-A;;6TjYLGcEl8@odkYrUo`k*bSp'
    'c6bM<QTk{-*6~Q&jYTUKc*5}@6i(_<7Xgj9IVh%JDuKP#YimX77NU9ubN>#^z1|k#i~u`*2kaD4jr;S2>J%83I&LheQM^)>?#LVY'
    'fp5^YhsFCwGyK_Qb_AZr_%k;!?ex$=nOFwD&cPL0ukd?~*`~K<&`Ew>12LPc5cr#l4CqgUdNyln0_kC&MO|yA?#BMLipD_0&d5uf'
    'tArLk^(;T{p2>Rx_`6=ZaVtf~fhepq>EZnuv~ckVOE=<*r9gB_F~0o8j42HZNP@VjFGir642LVxeqJRT4huO2Nph>g%C`8wz21|F'
    '%wxEkd4MHVM-xgPRqYZBaR&LM1H6~XPK@dSvk!L{ej%V@Dyn*(S_EFPx7mK>a36;p?(FTbs$D&_i=$eoWI)by+k7YY0c=K#epW>H'
    'bWS-Kd~vny02*y7Mr(ORck%FKfjD(FuuUgqMCGZq<_N|jY+HMD4GBW|NE~m!cj~CkvLo}t>0{PJhmZ(H_mcTcnCmLuZL3PdJrh>D'
    'iceKxzY8%Ljr#yjo=8!Ki(2Uyoj8%`bFwN2Y$8ZRh2dQrM&D(8AknB`II(`1Or93bzS>+sq0fB?;;=g>zl+x#%OLyWFkG-!!>U^<'
    '17`#hDV>JCRg={+aJ&PqBpf$FMCGm8UK=m};_o8P237GrABbyKOJ%zO8_-V{=o-+RXTMs5fhF$GEdzhdR-&J<ZQ+G5z?Zi}lvk2J'
    'c9TGKMzW1?b2+|h5d`8aWj~A)u+&zi!PIIND*iw|KQYSU@-pcet^}I)D?9t_VE^Diw$24$@m_O=<i&d79L8+{6$@;VGL4Y2$MX}&'
    '49H%%qpr3B9Mn($=7I1=WBP*x5FzS6`kMrxl>gViMj(AuHw*?okoUq1S7_r@{6&B*@fQK=8k)7XbVJ}=OC9Tl9IL#OtD)6~_QV6F'
    'Ah8pR>AD`JwI{bsA5GF%$aNiW?$N#dqesZ!;|Yj6Xg$1BL|^zd9@Fu6OFc>&B1c{B0KmJOGeW-BVKN=X+{x}Ax6TF(_L0GEx5cqC'
    '?vgl4#wWaX?16udJ;IrX#25-Y9%kO4gAhIGwbc~4xamxP?c<sGYS66L)&$Z8p<+ce;P6AbC<}p&<8ZD!5Y>l~<LJ3tOXd(b#l0!2'
    '9~tVFPOcAjw53!1g9LQcdE(L~)_oTYvw?s8Vbh-s$5<2-9u<HfS{TKt^Bl|*jwMZ&1Q=MQqd4IP2pR+FFwK(wUy*KZig9QT@UKj8'
    '{M!<SzVs(Ha2j2N2sx=>=p~gk9J%=lV*;l$PlLoj>HxkNN)k*QxV{8|&<~+Du!tU|hED49sd;&ScG+}}ZqDw`jv5!vUE}6c^Uk@t'
    'ym)l3?{6|KYuft`O32OC#jSJQxV=U4BqorWdl-6q_Q(CjUE{KOb${!eUfrC1M~S*{uCHzZ`9stBa^E<<X}~;A<MP;PTsOZt&D$gR'
    'UPgF#bKi9CFV9Y{ZvLQq4JY>(7tSAN-<rqHZ4<~icFvo3w}j^U>f-U!)unTEfAi3|LyDJ>eLcOpXgX(?cTE7eaIP)@2PnYNopa#q'
    'ICjPP+H8ETR4U8kXigY*b9Q+PBun*hZW@=Lcf<mq{}edrRCD$fS+<0)d3}3!adoLP5SSL}3>ZUIQUlHUbl<o+hIj!3i6V$Bp|$gK'
    '3;kpB=JNKgdA5XXxv~aG|7d(WZhl$>E7aE78F?fvs4_G^i4&85<YY7HyVc!2(YV<UW_}3fCN<1_Z9lQhH?U_9&6`KXlK%yc&V3>'
)
b=zlib.decompress(base64.b85decode(DATA))
assert len(b)==18112
assert hashlib.sha256(b).hexdigest()=='551e676d836b97951d85d48c157ebb3fbbc9ff1e4c02cb8c07c53852e57259f4'
p=Path('critical_ridge.py');p.write_bytes(b)
assert sys.argv[1:] in (['build'],['check'],['extract'])
if sys.argv[1]=='extract':print('CRITICAL_RIDGE_SOURCE_EXTRACTION_PASS')
else:
 subprocess.run([sys.executable,'-S',str(p),*sys.argv[1:]],check=True)
 r=Path('critical_ridge.json').read_bytes()
 assert len(r)==1969450
 assert hashlib.sha256(r).hexdigest()=='dc02862ba308f010514504b70860a32c1f98fd9cbd46f26c5bf9d0511ff79c79'
```

## 8. Remaining problem and most useful continuation

The old critical horizontal-ridge geometry must no longer be treated as either physically empty or an unresolved regularization obstruction. It has genuine pure-four-A realizations, but its whole nonnegative intrinsic stress cone is trivial, and the complete parallel-ridge four-A sector is closed.

The consequential remaining two-apex cases have genuinely unequal heights: the unique positive-beta packet competing with at least one negative-beta packet, or a nonbasal source exactly on the true centroid-height plane with the other three points basal. The positive-beta stress identity from the parent remains necessary there, but the present proof neither empties that cone nor constructs a realizing obstruction. The new formulas were derived from actual equal-height slices and cannot be transferred by projectively transporting an old centroid.

The useful continuation is a base-fixed, true-COM apex-modulus calculation for unequal heights, evaluated on the **whole** unique-adverse intrinsic cone. Equation(5) gives a model for the needed connection to actual covariance. Non-B8 lattices and mixed/VF packets remain separate. No failure of a selected actuator, formal stress, or finite computation has been promoted to a global impossibility theorem.
