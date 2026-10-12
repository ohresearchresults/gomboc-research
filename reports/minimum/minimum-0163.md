# minimum-0163

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# TWO_ANCHOR_JOINT_ROTATION_EXCLUSION_254_OVER_125_V1

## 1. Main result and exact scope

**The remaining genuine two-anchor high-trace joint-stationary sector is excluded.** In fact, on the actual seven/eight-plane chart with both stars nonflat, positive endpoints, G(C),G(D)>=0, the four whole-facet hinge equations and the actual joint root equations imply

    T < 254/125 = 2.032 < 51/25.

Only the root tests h=x and h=y are needed. When the optional ordinary B facet is present, its full two-direction plane reaction is needed; the accepted genuine-triangle level condition implies that reaction exactly.

Consequently every genuine polyhedral **full-class joint local maximum** in the unbalanced, all-positive G(C),G(D)>=0 sector has T<254/125: the two nonflat stars are treated here, while the inherited flat-A bound 65/32 and flat-B bound 257/128 are both smaller. This is not a maximum constrained to keep the G signs along its competitors, nor a fixed-ell or fixed-lattice stationarity assertion. The original uniform filling and its actual V,E,N are retained throughout.

The decisive new variation rotates a genuine coordinate triangle about AB, slides its simple marked vertex along its actual third edge, and then affinely restores the canonical frame. The determinant and changed marked endpoint produce two additional exact reaction identities. These identities couple the whole-facet hinges to the joint root tilt; they are not consequences of greedy placement alone. A six-vertex convex scalar envelope then contradicts the accepted actual upper-defect value theorem, with the explicit defect gap

    4/125 - epsilon_B > 13427/229900000

under the high-trace assumption and the two new zero reactions.

The proof of the new obstruction does not need the ell<=1 height reduction, root-only auxiliary vertices, a bound on the root perimeter, or independently assigned projection moments. Indeed the coordinate-rotation argument also applies to an arbitrary finite proper two-anchor fan at a full joint maximum. The seven/eight-plane chart is the supplied finite domain on which the incompatibility with its specified hinge/root reactions is made explicit below.

**Boundary of the conclusion.** This is a complete original-trace bound on the stated actual reaction-defined sector, not a value bound for every nonstationary seven/eight-plane body. No proof is supplied that an arbitrary sector-constrained maximization has a full-class stationary maximizer. Negative G(C/D), zero-endpoint limits, the balanced a=b case at the stronger 254/125 constant, and the global auxiliary trace problem are not silently included. There is no mechanical E17 exclusion, registry decrement, C34 attainer, or change to 34<=Cmin<=622.

## 2. Source reading, identity, and inherited input

I read the new 1,740-line journal, its entire literal parent payload, the complete new polygon proof, and its complete executable source through EOF. The unchanged earlier geometric sources and earlier results remain accessible in this same chat and were retained. No supplied source used here was unreadable or left truncated.

| New supplied file | Bytes | SHA-256 |
|---|---:|---|
| research-journal(20260921-121832).md | 290980 | 96373006b79722306496fff1e70122ffd9f542a4a6b76d9291f37b4d51adeb6c |
| CONCAVE_FACET_ALL_POLYGON_POSITIVE_EDGE_OBSTRUCTION_V1.md | 6509 | 3def2fc37632f9e60a779bd64de787dfb20988f425dc76202da702efcdcaeb78 |
| polygon_moment_kernel.py.txt | 4154 | 5953753de38671320efc188348fe3c60382bf3c36761aa9d144e564489a6db77 |

The literal parent is **minimum-0162**, declared immutable SHA-256 **507ff8b483ef733adcfe0f45e16a82bd72324677cf020c0f00bef9d83adbd979**. Its no-ordinary-A theorem, actual small fan, and distinction between its controls and stationarity are retained. :contentReference[oaicite:0]{index=0}

One compressed notebook notation must not be read literally: the phrase `m<=halfS` does not mean m<=(c+d)/2. The literal height proof and parent use

    m <= (4-T)s0/[2(2Tt+T-2)],  s0=a+b,

half the displayed upper bound for S, not half the actual endpoint sum. Unequal c,d remain allowed. This handoff uses the literal formula, not an accidental symmetry restriction. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

The sole inherited numerical value input in the new nonflat proof is the parent's **actual-body** theorem

    T < max(129/64, 2+epsilon_B),
    epsilon_B=6(1-b) integral_Delta (x+y-hB(x,y)) dxdy.    (D)

Its exact domain is bounded proper33 two-anchor polytopes with positive endpoints and G(C),G(D)>=0. It does not assume stationarity. The parent proves (D) from the actual upper-facet flux, the literal T0 integral, and the accepted actual joint-mass inequality 4(gx+gy)<=t+1, together with gx,gy>=1/4. The original separate proof source of that joint upper bound is not attached; it remains explicitly inherited through (D), not newly verified here. The complete derivation of (D) itself is in the supplied literal parent. :contentReference[oaicite:3]{index=3}

No missing old greedy or root-duality executable is a recovery dependency. The new exact units below have complete literal inputs and were independently executed and source-only cold-replayed.

## 3. Actual geometry and first-variation conventions

Normalize a=1. Let

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    0<b<1, c,d>0, alpha=1-b, s0=1+b, S=c+d,
    hc=s0+c, hd=s0+d,
    ell=1+(d-1)x+(c-1)y-alpha z,  n=hc x+hd y,
    V=integral_P 1, E=integral_P ell, N=integral_P n,
    X=integral_P x, Y=integral_P y, g=integral_P(x,y,z)/V,
    t=6V, r=N/V, q=N/E=Tt, T=N/(6VE),
    G=n-r-q ell, LA=(r+q)/3, LB=(r+qb)/3.

The body P is bounded, full-dimensional, uniformly filled, contains T0=conv(A,B,C,D), lies in x,y,ell>=0, and has a positive-area root F0=P intersect {ell=0}. Proper33 means its actual maximal coordinate facets are ABC and ABD, not larger marked patches.

On the reduced nonflat chart,

    hA=max(-u x,-v y),             u,v>0,
    hB=max((1-kappa)x+y, x+(1-lambda)y, optional Ox x+Oy y),
    kappa,lambda>0,
    P={x,y>=0: hA<=z<=min(1-hB,[1-(1-d)x-(1-c)y]/alpha)}.

All declared facets are genuine and irredundant. The optional facet contains B and no other canonical mark. At a full maximum it is the actual root-based triangle supplied by the parent, with

    Ox=(1-d-omega hc)/alpha, Oy=(1-c-omega hd)/alpha,
    omega=3b/(4r+qb).

The proof below only needs its whole-plane reactions, so it never identifies a coordinate support patch or an integration triangle with a maximal facet.

For graph facets use projected xy measure. Define H_AC=integral_FAC G x dxdy, H_AD=integral_FAD G y dxdy, and similarly H_BC,H_BD. The four hinge equations are H_AC=H_AD=H_BC=H_BD=0. Their zero/sign is unchanged by the constant conversion to Euclidean facet area. The admissible whole-plane hinges fix the two canonical vertices, and remain valid when other vertices are nonsimple. :contentReference[oaicite:4]{index=4}

Write R for the actual xy projection of the root, and put

    Jx=(1/alpha) integral_R G x dxdy -qX+Y,
    Jy=(1/alpha) integral_R G y dxdy -qY+X.

These are exactly the joint root reactions for h=x,y, including the explicit change of n and ell. In the all-positive stratum both signs are admissible. In particular they are not fixed-body first moments assigned independently to R. :contentReference[oaicite:5]{index=5}

If an ordinary B facet O is present, let HOx=integral_O G x dxdy and HOy=integral_O G y dxdy. Its true triangle has values (-3LB,LB,LB), so the exact affine product integral gives HOx=HOy=0. The underlying ordinary-facet rigidity is a full-class theorem using whole-plane pivots and outward pyramids, not a fixed-lattice assumption. :contentReference[oaicite:6]{index=6}

## 4. A pointwise actual tetrahedron-plus-visible-caps budget

For any p=(x,y,z) in P put sigma=x+y, w=ell(p), and

    tp=6 Vol(conv(T0,p))=1+(-z)_+ +(sigma+z-1)_+.

The only visible canonical facets are ACD and BCD. Their genuine exterior pyramids have disjoint interiors. Besides tp<=t and sigma<=tp<=t, their actual uniform ell integrals give

    24 integral_conv(T0,p) ell
      =1+b+S +(1+S+w)(-z)_+ +(b+S+w)(sigma+z-1)_+.

Using the exact identity n(p)=1-w+(b+S)sigma-alpha z, rearrangement yields

    24 integral_conv(T0,p) ell
      =n(p)+w tp +(b+S)(1-sigma-z)_+ +(1+S)z_+.

Every displayed extra term is nonnegative. Since ell>=0 on the actual remainder P minus conv(T0,p),

    24E >= n(p)+ell(p) tp                     for all p in P.  (4.1)

This is stronger than n(p)<=24E and is a genuine uniform-mass inequality. It is not inferred from a chosen centroid. The exact visible-volume formula is also the one in the supplied height proof. :contentReference[oaicite:7]{index=7}

Two other actual inequalities used below are elementary. A positive tetrahedral fan from D, using x>=0 at its other vertices, gives gx>=1/4; the fan from C gives gy>=1/4. Hence

    Qx:=24X>=t, Qy:=24Y>=t.                             (4.2)

Finally T0 containment gives E>=(s0+S)/24, so

    r>=T(s0+S)/4.                                      (4.3)

Selected flat fan cells may have zero volume; all averages and denominators here are those of the one nondegenerate body.

## 5. The missing joint connection: rotate a coordinate triangle and restore its frame

### 5.1 A genuine two-sided family

The simple marked vertex C has third-edge direction

    (1,L,-u),  L=kappa+u-1,

because its two noncoordinate incident planes are z=-u x and z+(1-kappa)x+y=1. For small real e put

    beta=1+Le, C_e=(e,beta,-u e).

Replace only the physical coordinate inequality x>=0 by

    beta x-e y>=0,

keeping all other physical halfspaces and the physical ell fixed. Call this actual polytope P_e. Then apply the invertible affine map

    x'=x-(e/beta)y,  y'=y/beta,  z'=z+(u e/beta)y.        (5.1)

It sends A,B,C_e,D to the canonical A,B,C,D, and restores x',y'>=0. Its determinant is 1/beta.

The normalized family, not the unnormalized P_e alone, is the admissible canonical competitor. Both signs of sufficiently small e are admissible. C is simple; all other non-AB vertices lie strictly off the x=0 face. The root misses both proper coordinate triangles because its four canonical endpoint values are positive. Thus the physical root is unchanged for sufficiently small e, while the root after (5.1) is its affine image. Boundedness, positive root area, canonical containment and positive endpoints persist. This is an actual convex-body family, not a formal motion of a triangulation or an arbitrary change of moment weights.

The transformed root function has endpoints (1,b,c_e,d), where

    c_e=c+e dc,
    dc=d-c+(c-1)kappa+(c-b)u.                            (5.2)

Let V_e,E_e,X_e,Y_e denote original physical uniform integrals over P_e before (5.1). Retaining every determinant factor gives exactly

    T(new normalized body)
     ={ beta(s0+c_e)X_e +[hd-(s0+c_e)e]Y_e }/(6V_eE_e).   (5.3)

The c_e change and the beta factor are both essential.

### 5.2 Exact new coordinate reactions

The outward speed of the physical x=0 facet is -y. The exact triangle product moment is

    integral_ABC G y dydz
       =[G(A)+G(B)+2G(C)]/24
       =[2hd-4r-q(s0+2c)]/24.

Differentiating (5.3), with r,q frozen at the candidate, shows that a zero joint derivative is equivalent to

    [(1+2c)u+(b+2c)kappa] Qx
      =(s0+2c-d)Qx+hc Qy+2hd-4r-q(s0+2c).             (C)

Exchanging x,y and c,d gives

    [(1+2d)v+(b+2d)lambda] Qy
      =(s0+2d-c)Qy+hd Qx+2hc-4r-q(s0+2d).             (D)

These are original-trace reactions of actual uniformly refilled bodies, including their changing own centroids.

### 5.3 Why the stipulated hinge and root equations imply (C),(D)

This bridge also makes clear why a fixed-ell or merely greedy argument misses the constraint. Under the inverse of (5.1), the lower AC and upper BC planes stay fixed. The other two special parameters change with derivatives

    vdot=vL-u,  lambdadot=lambda L-kappa.

The root derivative is dc times the affine function y. If the optional ordinary plane is present, its upper y coefficient changes by

    Oydot=Oy L+Ox-u.

Thus the derivative numerator in (5.3) is exactly

    DC=(vL-u)H_AD +(lambda L-kappa)H_BD
          +dc Jy -(Oy L+Ox-u)HOy,                       (5.4)

with the final term absent in the seven-plane case. The D rotation has the reflected identity with Jx and HOx. Therefore the four whole-facet hinges, the two actual joint root tilts, and the ordinary plane reaction imply (C),(D).

The normalized ordinary plane generally leaves the artificially imposed one-parameter omega locus along this family. That is allowed. Its complete whole-plane reaction vanishes at the candidate; it would be invalid to restrict the variation by requiring the ordinary G-level relation at every nonstationary competitor. This is precisely a full-class versus reduced-parameter distinction.

The exact audit below verifies both identities (5.4), including their ordinary terms, on an asymmetric genuine body using independent tetrahedral mass and polygon-facet integrations.

## 6. Complete high-trace exclusion

Put

    tau=254/125, delta=tau-2=4/125,
    Hcrit=tau/(3-tau)=254/121,
    m=max(c,d), nu=min(c,d).

Assume T>=tau and the stated actual reactions vanish.

### 6.1 The lower hinge closes the first endpoint chamber

From (4.1), 4r=24TE>=T n(p)+T ell(p)tp. Therefore

    3[G(p)-LA]
      <=(3-T)n(p)-q-(3q+Ttp)ell(p).                    (6.1)

If T>=3 the right side is strictly negative everywhere, immediately contradicting a lower hinge. Otherwise n(p)<=(s0+m)t and q=Tt. If s0+m<=Hcrit, (6.1) gives G<=LA throughout P, strictly wherever ell>0.

Use the genuine AC facet and its nonnegative hinge function x. A fan from A gives

    integral_FAC G x <= [G(A)+3LA]/4 integral_FAC x=0.

The inequality is strict: C has ell(C)=c>0 and hence G(C)<LA; the first positive-area fan triangle along AC has a strictly positive coefficient of G(C) in its Gx integral. Thus H_AC<0, contrary to stationarity. This is an explicit improving lower-plane hinge, not a supremum or moment-completion argument.

Consequently a putative remaining stationary high-trace body must have

    T<3,  s0+m>254/121.                                (6.2)

### 6.2 Endpoint and volume constraints of this same body

After exchanging C,D as necessary, the mark whose ell value is m gives

    r+qm<=s0+nu.

Combining this with (4.3), q=Tt and nu<=m yields

    m <= (4-T)s0/[2(2Tt+T-2)] <=(123/512)s0.

Since s0<2, (6.2) places (s0,m,nu) in the following closed scalar overcover:

    1024/605 <=s0<=2,
    254/121-s0 <=m<=(123/512)s0,
    0<=nu<=m.                                          (6.3)

This overcover contains nonphysical boundary tuples, deliberately. They are not claimed to be bodies or true vertices of P; exclusion of the overcover is sufficient.

### 6.3 The coordinate reactions control the actual upper defect

Add (C) and (D), and use hc Qx+hd Qy=24N=4tr. Defining

    Rbal=4r(t-1)+2s0+S-q(s0+S),

gives

    [(1+2c)u+(b+2c)kappa]Qx
      +[(1+2d)v+(b+2d)lambda]Qy =2 Rbal>0.              (6.4)

Because Qx,Qy>=t, u,v>0 and c,d>0,

    bt(kappa+lambda)<2 Rbal.

The actual hB is at least each of its two special supporting forms. Hence

    0<=x+y-hB<=min(kappa x,lambda y).

Integrating this literal tent over Delta gives

    epsilon_B <=alpha kappa lambda/(kappa+lambda)
               <=alpha(kappa+lambda)/4
               <alpha Rbal/(2bt).                      (6.5)

There is no assumption here that the special supporting forms alone describe the upper boundary. The optional upper plane can only decrease the displayed defect.

### 6.4 Eliminate r,t without losing their actual coupling

Set A0=s0+nu and z0=A0-r>0. The actual mark inequality gives

    t<=z0/(tau m).

Also (4.3) implies 2s0+S-4r<0, since tau>2. Therefore

    Rbal/t
      <=4r-tau(s0+S)+(2s0+S-4r)/t
      <=(4-tau)(s0+nu)+3tau m
            -4z0-tau m(2s0+3nu-m)/z0
      <=Phi(s0,m,nu),                                  (6.6)

where

    Phi=(4-tau)(s0+nu)+3tau m
          -4 sqrt[tau m(2s0+3nu-m)].

The last step is exactly 4z+B/z>=4 sqrt(B), for B>0. All moments that led to (6.6) were those of P; z0 is not an independently assigned root mass.

### 6.5 Six exact rational checks cover the whole residual domain

The geometric mean sqrt(vw) is concave on v,w>0. Since m and 2s0+3nu-m are positive affine functions on (6.3), Phi is convex there. The bounded polytope (6.3) has exactly six vertices. Put

    L=(4-tau)(s0+nu)+3tau m,
    B=tau m(2s0+3nu-m),
    W(s0)=53/50-(2299/465)(2-s0).

At every vertex L-W>0. The complete table of positive rational differences is:

| (s0,m,nu) | W | 16B-(L-W)^2 |
|---|---:|---:|
| (1024/605,246/605,0) | -23/50 | 1521109631/22876562500 |
| (1024/605,246/605,246/605) | -23/50 | 126231756239/22876562500 |
| (2,12/121,0) | 53/50 | 423895631/915062500 |
| (2,12/121,12/121) | 53/50 | 23633519/915062500 |
| (2,123/256,0) | 53/50 | 5448012359/256000000 |
| (2,123/256,123/256) | 53/50 | 510808871/16000000 |

Thus Phi<W at each vertex, and convexity proves Phi<W throughout (6.3). The exact verifier independently enumerates the six vertices from the six halfspace inequalities; no sampled positivity or infeasible-cell pruning is involved.

Since alpha=2-s0 and b=1-alpha, (6.5)-(6.6) now give

    epsilon_B < alpha[53/50-(2299/465)alpha]/[2(1-alpha)]. (6.7)

The final strictly positive integer polynomial is

    Q(alpha)=114950 alpha^2-26133 alpha+1488,
    459800 Q(alpha)=(229900 alpha-26133)^2+1248711.

Exactly,

    delta-alpha[53/50-(2299/465)alpha]/[2(1-alpha)]
       =Q(alpha)/[46500(1-alpha)]
       >=13427/229900000>0.

Therefore

    epsilon_B <7343373/229900000<4/125.                  (6.8)

But the inherited actual-body theorem (D), with T>=tau>129/64, requires epsilon_B>T-2>=4/125. This is the contradiction.

### 6.6 What has been closed

The four hinges, two root tilts and ordinary whole-plane reaction are incompatible with T>=254/125 on the entire genuine nonflat chart. Combining this with the parent's full-class flat-A theorem and actual flat-B theorem excludes every unbalanced all-positive G(C),G(D)>=0 genuine polyhedral full joint maximum at or above 254/125.

More constructively, an actual high-trace body in the first chamber has a strictly improving lower hinge. In the second chamber, the two coordinate-rotation derivatives cannot both vanish; a sign of one of the explicit rotations improves its original trace. Such a competitor is not asserted to preserve an imposed G-sign constraint or the artificial omega relation. No statement about the mechanical equilibrium class is used in the exclusion.

## 7. A useful corollary of the supplied all-polygon tool

The new supplied concave-graph inequality was also read in full. It gives a small additional geometric observation, independent of the numerical value proof.

At a proper full two-anchor maximum with both stars nonflat and G(C),G(D)>=0, let R_C be the unique third neighbor of C, besides A and B. Then

    G(R_C)>G(C),  G(R_D)>G(D).

For G(C)=0 this follows from auxiliary positivity. For G(C)>0, suppose G(R_C)<=G(C). In either special polygon containing AC or BC, the true edges at C lead to its negative-G anchor and to R_C; hence C is a maximum of affine G on that polygon. With G as a normalized horizontal coordinate, the whole polygon has the form 0<=eta<=f(x), f concave, f(0)=0, now allowing f(1)=0 when C is the unique maximum. The supplied inequality 4D/C-3B/A-1<=0 contradicts the whole hinge plus spike inequalities unless f is exactly a positive linear function. That equality is the genuine triangle with the third vertex at the same G level as C, and anchor value -3G(C). Both the lower and upper special facets would therefore have to be such triangles, forcing G(A)=G(B), impossible for a>b. This proves the strict increase. :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9}

This is a recorded corollary of the supplied kernel, not a new 33-term kernel computation or an extension of a finite annular-fan enumeration to arbitrary polygons.

## 8. Exact actual-body cross-check and nonwinning successor

The actual audit starts from **Case R** of the literal parent, and checks its V,E,N against the parent's exact fractions. The complete halfspaces are defined by

    a=1, b=6/25, c=1/10000, d=1/20000,
    u=1/1000, v=1/2000, kappa=lambda=10, omega=23/100,
    hA=max(-u x,-v y),
    hB=max(y-9x,x-9y,Ox x+Oy y),
    Ox=(1-d-omega(1+b+c))/(1-b),
    Oy=(1-c-omega(1+b+d))/(1-b),
    x,y>=0, ell>=0.

It independently reconstructs every true vertex, maximal facet and physical edge, integrates the original mass twice using an interior fan and an A-based fan, and integrates the actual polygon reactions. Both coordinate identities (5.4) agree exactly with the independently calculated derivative of (5.3); both coordinate derivatives are positive.

The new exact successor uses e=1/1000000 in the C rotation, beta=1000009001/1000000000, the physical cut beta x-e y>=0, and the affine map (5.1). Its endpoint is

    c_new=900007101/10000000000000>0.

Both old and new bodies are proper33, have a genuine pentagonal root, and have true (V_true,E_true,F_true)=(9,15,8). The root before affine normalization is unchanged. Their literal maximal cycles, in lexicographic vertex order, are

    (0,1,2),(0,7,1),(0,2,3,5),(0,5,8,7),
    (1,4,3,2),(1,7,8,6),(1,6,4),(3,4,6,8,5).

The fifteen physical edges are

    (0,1),(0,2),(0,5),(0,7),(1,2),(1,4),(1,6),(1,7),
    (2,3),(3,4),(3,5),(4,6),(5,8),(6,8),(7,8).

The new actual uniform moments are

    V=5471684291300295186248929656076458282276172828935500
      /30058471345579032652039370477615632887389976200509387,

    E=379495238148886300409822238936648138831463150843939205249625913
      /7214033122938967836489448914627751892973594288122252880000000000,

    N=99884952516568913553029199972758266530808277931860953877767104579528754202119064613069955988801896540306638473
      /857086197280312204063517620969446333749343126693326912908906779471092652840331113690862553941601525801520000000.

Its trace is exactly

    25270892986691935128916387593107841432294494316760821331075077458620774813136123347106698865166879824697579533669
    /12458868799215154093908197599689489050951411419647259996127981464736309177697288960124816566234169361077902033669,

so

    T_old=2.028343714870837... < T_new=2.0283457024833487... <254/125.

The complete generator returns the original first moments and the true own centroid, not a selected reference center. With the same-origin primal/polar Euclidean convention M=Nmetric=I, both bodies have strict (S,U,H)=(4,4,6), physical weak count zero; all sixty physical edge primitives are nonzero. Integration diagonals are excluded from this census.

This is an exact audit control and a nonwinning successor, not a stationary body or a 110 attainer. The new optional upper plane is not assumed to remain on the imposed stationary omega locus. Its purpose is to check the genuine frame/root coupling and its finite original-trace improvement. The older parent 10/17/9 and other 9/15/8 controls remain distinct, unchanged objects.

## 9. Computation, failed methods, and recovery status

The first attempt was direct lower-star flattening and symmetric all-root rational differentiation. Floating gauge probes used seeds 5191 and 5192. The first accepted no T>=2, G(C/D)>=0 sample; the second accepted 5,234, all with negative lower hinge integrals. These are numerical observations, not a monotonicity theorem or an exclusion. The symmetric derivative expressions were not used in the proof.

I then derived the coordinate-rotation reactions. A loose scalar probe of their summed balance, seed 5193, showed that positivity of that balance alone was not the contradiction. A sharper necessary scalar defect probe, seed 5194, suggested that its combination with the upper defect had a substantial margin at the original 51/25 target. Its penalty optimum had slightly negative guards and was not a body. The final proof abandoned these numerical optima: it uses the displayed actual variations, the full six-vertex closed overcover, and rational checks at the stronger independent threshold 254/125.

All materially used source units, exact inputs and optional discovery programs are embedded in the capsule below. Their versions are CPython 3.13.5, SymPy 1.14.0 for exact symbolic algebra, and NumPy 2.3.5/SciPy 1.17.0 for the nonproof locators. The latter retain every seed, bound, population size, stopping tolerance and iteration limit in their source. The frozen exploration receipt retains the original counts, checkpoints and output hashes. No repeat of the stochastic searches is claimed by the exact cold replay.

The two **new exact** units were executed, copied alone into a fresh directory and replayed with byte-identical outputs. After the final parent-moment checks and uniform-gap addition, the complete recovery capsule was executed in another fresh directory and checked every final pin. The analytic shape-variation and convexity arguments are proved above; the programs are exact algebra/geometry audits, not proof-assistant formalizations of those arguments.

| Exact object | Bytes | SHA-256 |
|---|---:|---|
| joint_rotation_certificate.py | 6261 | 4c894c4e7456857421885bca0e82f3afeef521f67509456f836d6895f9de37df |
| joint_rotation_actual_audit.py | 9064 | a4bed339621d4335af617146478137897bc5dadbcb585ccb79c229ab69368055 |
| joint_rotation_certificate.json | 1325 | 3a801dc749713efa7041a4ca23765f2a7a276fc6a567cdc3b37631d7ad7d73f1 |
| joint_rotation_actual_audit.json | 64918 | 175fd7b67b4259ddf96c9353b50b79df608945eab007bee6f3801327ae5628fe |
| joint_rotation_certificate_stdout.txt | 401 | 5ed75cc52b5bcc6449c2c1ec228e25f3ce493f8fe4c2cf7a03d9c20fc9747e11 |
| joint_rotation_actual_audit_stdout.txt | 392 | 73a65f8d9ad82c120122bdc606a969212c67533bb6112b049123d02692dff201 |

## 10. Complete source-only recovery capsule

Save the following entire unit as `recover_two_anchor_v3.py`, UTF-8/LF with one final LF. It has **18696 bytes**, SHA-256 **639f5894596647090dea0c03c8ac104c7fabd795f709b8ba1d3e7dd20dbb8218**. It contains all eight complete source programs and four frozen discovery records, including both new exact generators/verifiers. No parent executable, archive, network, omitted helper or input table is required.

The decoded payload is **29517 bytes**, SHA-256 **3b6603447f55112d8088bfa5d40d2438ada02d7f73f8cd10859c076a9f2bc1cd**. In a fresh directory run

    python -S recover_two_anchor_v3.py recovered > recovery_stdout.txt

The observed recovery stdout is **1832 bytes**, SHA-256 **294c2c50d1b592fcbc46fd594ffdcdafe899838be15cac7c338f3ff2e947399e**. Expected terminal marker:

    TWO_ANCHOR_V3_JOINT_ROTATION_SOURCE_ONLY_COLD_RECOVERY_ALL_HASHES_PASS

The exact children include these markers:

    SIX_VERTEX_FULL_CONVEX_ENVELOPE_RATIONAL_CERTIFICATE_PASS
    POSITIVE_FINAL_QUADRATIC_GAP 1248711

[Encoded source block omitted; the code in this passage is incomplete.]

The locators are extracted but deliberately not run by the proof command. Their original output paths are preserved, including the explicit `/mnt/data/two_anchor_v3_work` destination in the defect locator. They are optional nonproof recovery, not hidden steps in the certificate.

```python
"""Complete deterministic recovery of the two-anchor joint-rotation result.
CPython 3.13.5; SymPy 1.14.0 for the symbolic child. Assertions required.
Usage: python -S recover_two_anchor_v3.py [OUTPUT_DIRECTORY]
Only the two new exact units run. Extracted floating locators are NONPROOF.
No old source file, archive, network, optimizer or input data is required.
"""
from pathlib import Path
from hashlib import sha256
import base64,json,platform,subprocess,sys,zlib
assert __debug__ and platform.python_version()=='3.13.5'
assert len(sys.argv)<=2
DATA="""
c-rlK`*Y$*^5^gOS7>`<0|`o4Z@`Qu!sB*7W<Bm6xBC^CAcQ20+8}6N4esmz{XUsh0)cVQes|-
(cX4sE+eWI&%F4>hXH`l1{w!TjN0V8!$R>Gjmd0r|UDUtKC;79}XWwt1CFvlI7rl6x#`n`nmM?CfouYWK%yD5_b<6S^t!Be%1wqq
soK~ahi`!@8`5mfnpS_tbvT^pn$hAc}8)td6NE2<ojN^1ZA1p_sP5t&6TFe*GVvaVQElS_FE#LBi*%m0Z8&<<@S<RN;vYRc-
Z3?UIG@6cY`z^0&xviETcqsGe&as<r;Cqg3+nzA(x)oSKv&H1uzH2p7(`o>=5jd?@(+*s}>G{n@K%foujjnyi_N}Jpxv6PeqTGG6
>DVAom|nf*T0tuSWFzpKR-mx@p4R~RP1kYJl^0Nv<uq-_YX)xMG_9uF72x6ZImUYg95v5n%|R>F^tqyip#_#_H(bv`GY1uSYp!v8
Oa0fh(S+vWZo@Sms#+Lu!|?(OOhwK8I8v>=h7)+U+rR)V+X<+rQBi4QUfq^WjA{aeIvdN1-
HcckSVpb#C93Rt)Ab!6^nn5kH2Pp7wfl-nx9$ba2E@f}HaygOD4%g7jMB1f*K=LB<$)wrEV!a!VR|78nD`)Qxj(w7SxZ@Y#ED~MJ
weYS#KNlw4aW|AOfR_Mwu;Gb75_DCs{ujk{s0AoY?St<Sw5E<ahFcUy}@V_E$UO^c*hM~3t)C&JAM-
M!QiIjdPx)5F$sOQktPG*ik#SXW6Uww><^OWz;fee5<v8lLFC7c#_cm2?sPWkr>vHQnt16Ad^b)ayBRzED6(S9^}T-
IAG9Jjjr*yeCbkpx(O+uY{ixY+V`l($05z7=Z+U(huOzr-
+bC%atTc`zzaL;O2AC_)5Bh16`nc{pjn=@2>J9?miKr*f!w3R<VE4TUyi1zR5?*IZunpz%SafVJ>JI{lXWt9rMk`G*;M5745fq?l
r(V<;G+RkCP69u11E_3d^}RGmJs0Hotz-|qqT3-pdqK-
f8!!jp=m3cQhV3@Nm;@Xcc+D7!l*CY6C{q%E&SsieNh^sXrw_6B`V#SMvXGWg*}Z+fH<~1^K>$7{F_ganY-
!Z*yNREsk?S}EpDc{)#;Milr>&@!co8N#ZK1nHWZ8p$v+w_`CpDsgSk;FBdXUV>4}#S86POt%_MEie@*8Q>9bjll9P}**A|3Y~KT
29HCyE*vA7&zH9rQDgqfs<F7?A@zdiyN)FoB>0B9+Abew-vxoPug6AxVm1Zv6q+A9;y8u+y}WM&1B+*7tq46{U^jXFbUg!8!uMNi
4fL!2CN=Y(;L9bP?veAGnS^0H3Uu54#H?>j&s2h$D=(<pt10m>#f0_A}p%$LV60#bDhmTUqtRdck9XC7@0kp4)d|?}H?DZEpb4@g
Qjf=n|M>lgxQ(6RdL}b1-X(>tIOEAZ;|fG-^agJF$yS{Dwyyi&~K5eiO(C{-
BZCPU6JT05jRNS`cuI$xATX{WxkQt=RU`IEZ7b1*7EHF$DW)Ck3-$gHUNXje%!F6k_Nj1kO(&s;<|75P%5q-D(Ai-HI&V9W<IPs7
Mfb@R=TQ&K}S>q?ww{m2~wYsO}X0m&`Yrc=%>^y0_16hN&i}O`E29G+J!53Hk0wi)N{oPZruBjpkW@lxqD+lBM&y#!b?Ak|)|Qnr
rh>b~jv%Hd>zEK@3)@cDIaX2>{<x-
*YXQFdk5Xy72_plRS&F#ip*kEBK%dCbRK!1a#k0)$ekScmc)Q0{!9NWR{NW+M66b%_qxQoC;8pCUY$UA%ofEA<ebPaxq;l=1lu^m
d?}JDoq5Vi?nzYWn*nJ(BjD`(Prs%6csUul-nm_9dZ{93y!7Xy0F($N5_a_qPz6p4R#dHre}HZiHKPOcqQ9w_?8EM-GW8-
e3T#(K{(WMUE67SUa<9l_Rcf48fXwutYPnB0L%88UQyHxV7}ZIyk)B?oVsTR0VLi<d;y>6H&|HYd_I;IAD-
*58mziYAzGse=BhW$a%O|+)M12S8XM&08Ud`k$-
2MS7O_P(UXIIcDfXPq63Ox#{5S{%eWKS!yw$Q09RUl2GV3VzbR4TeK?#B~Xn^N9;)(7lsI+{91qg8vRaq1+5Uas={NJ{~AJ=XA4g
nK)K?o*qM%uWTEmQJ1(M(1ha5I(-4Rw7ReIk7E>$XqPUjtSbylvP(;-
eIFc!(?<@<WJD11=^)Y(zNlSr&rMhD)&r&k%f&OYsoGFW==z)}lBGAuDKeyp~IX07Ga|zX%pEK99m3zv;V(9?&xhjpY#e-
%`>=o;lO4I}{B<KmuTM8x;HckLG$hnP;T5dovPGmbnVbh1ET5vY1R=sw+(wSd3r_f13z0j!YL!8eAG!AGiobFk8%ymJ`5q`%R|>&
*|`FkrQxiEASDwQ^@Yf8AKZ&u{yX-o~Pyg)m#BBLOBbORTEqa8q9wi4h62%cAB6T9#f)jBC>-fdLG5$2-
U!B3xOhH(gxV;Lt>gdfo`3AG6GbD(ij7VQp_u5A{0U+(m@mrjX|Lcog_VMIcNmYplNlRAfQ1pW?%z})i|6nh%lzqhqfb9Z+W)oQD
X5!lo)LTg7O^*9OV8HqnT4kE1(w+q|mjRP3E=ZVTv4djMx-
EO-N|~Ft-7EDd6>6=&8wr0h|SSwqfT2I4$ph(}QR<-(xitHGrB@Ebf4_0V#k>QVQlH;I*xt{5RpJ0|#hf-
ddc;5y3v$FrpPE4gp7lCV&!48;K7>$0h~iKwy(Kbn$-*t8H-C<~gO2BC>`cVYa--9BtZUAAJZPlnmWG;wYpR%G|)@K{_5wuGfOOM
1<<W3?bQbmFPlJz&t23Wu;C_4h1{_H(<HJMQAFQ!bBk7A$db0;=+Uc6+htwIEQm!nl1DqEk^*^cX<SmG{}hT&_y|5ku=Z*!wIzNP
5`rGH!!u7I@)XmU1Up*RttgyF$b@U8L<&aP|^(MK?@MgOAVxfdC)d66@hs32v0pYLkBrHaw4E}nWxfBz#nt4WVdXAKMwtI=?_m0x
xb~1JFebby}f?(=7m<QLQG~GEr}M9^49TU8I4SY9GjDL9gmiC@~v??TV#VQhIgH_KV79Ws!*9&z8rHLg;22W)_sPUZWcq1cyFJ%b
-O5?$C-kJ*KO1-S-
2VR3Oy?P@#8jsCiXMDXQ$7y@pLj<XxyEKkR_kq=C?V*Xf0huqaG2hV?ISO&EXBqlW}^RYkd)mL@dQh+>22Nn9gaV+m1rp?4vdtXb
2tjJs{(k(9#eD^?wcR(^<M$&T{Q)lBWQN#SZgnJ(|s;jo#^)OH5yvR!oGs>UIr4ET_|S7Ir$ec@M2Zon05UIqG&%m&c)9>(}CTp7
2E?2`FeLYPHFjX#|N9RXxJrJkdM4Z6@YqT+L(SBoerb`7Xg-spBnid~2u?Mr(QBIfZXAezj{hCEGN{a+STSIv940057CbVnn#52o
b?+mTMg_L~#2qQ%^M+Rm>u&v_496J(?Lj53=&ht};`_T9W1=z&aU-Gx-;km{jsbm3*NR35?-
H{ke`dAQq&03W>H3bp^S_aRMk+i)Pj@>tF0s8cM;_wNZ?14&h1@eV#6Kx;KpWJiWt^X|yC{kTHEA)<(gXLC5M=*R?^%?p84sjEIJ
JDPGY4AF?Uq5%i~HpLXR?$Dw{%du5zB?JNor^6ETWcQgkb*~8diGy_5c)^<Ti*8gizIRgf>=zU2*Au<rYxNFp+D$sSZsN4Q{tlo^
OQVOzumyukG_pd_g=)Jf!guHlVv_D>okFxw@QT`F-)I@0#w<HZZ5FsrYh5hRLOY`GpI~mgDEA!*4b{vNtFs-XFB%^9F{KYzz#g{e
xm3e7YlhKKujLc+cC`cOkXd;H$mf5k0;~k^-
=pRjr0SvSK5fn8asfOFlCX)qd!zgMrijSAIkFU7mekAUPq0aQP{xSKu;#yEnEjcYBCU7Umm_U$ZYxkfT_fcpP!a`Ve9<azFk@W?S
PjEMan+w9o0zl&W+ELK)NW{af)at{`#F$U?cvMAk0qiQ^Xe6TH6HT0|9*tx}Zd;3n3Ju+DQF(i)`XkYQ3ZY8~t9^;H>M~9)83HxR
L8U`|RUPW1>KI(S?X>E0rys(L@GATieh#gA``QYx*WvXhyw35H(=QcYUbE?fp>AKk-Cn-
u(r%SZl(d!Y_iqo2lve*W=SdD}vRL}^QJBZjw_2W%almNX`H+f+nJQA^ro={yZ00P(?Yv1XYG=;3U6~XrhFwKT66$DS_K9}@1G|E
1WVF+Aji+iH4^`YS=j!c@=Od91RcErnL6z(iC~T)dvED~fruP6vne06jn|&0-B0)?!j%HVV1l6@wD~8*bqjh9?Ui-;7-
KWOs%Es&3Pe$lIHA2;RQ~Qgtxj!45LXtBH-
d;aPX6qP0fyq;tHf2n^4u68}5NHo$ir`sE?EOwSr48E&XLf%QC}GsyTHmN<_olNOx6~rp2vg?mg!5oxB*=;F>}2nN`&)?iX0LWPh
&>!1Y9SHWzNm#nUi+#RQorp_wUDs4Ki5LSvkMJBhzoHguB{^m`fGS~a?zgQ?}zpc{z3&mR4<4NGNU0+`;g8ibKU#jZAxNW#7?NZ@
75pDTxt4lZl=SLm=58`m<)zPB!XyH0&ZExz;X-}Gt@#;pVht^yZKXy1a}Let!-
tesL4mQuW<L6L;8JHKzhpVW&K|qDMiO<>OVzOG0u;dCw;K(r2q6-
3;LZJVj4AqYX84JhL36tANR&UUCv99lzyF?vnr(IBr^4{)ek28+o#%R!w{%hQ`K5keKJ3D;f4w~s_?V<$>0cgmd>+e3DFs4^Mx*l
VAS}AyEG0`h628b68a}HdoXpcDhGVxO1vz%Nfs~koA5?_2qD)YBs;tkpTbY#bNE?&4Zn(6I1?|=pNE}1F=yu2YAo`YFOsfMLM?w-
Rzs#qNFt)qjvobCh9IYG367@e4`>1Ty<Q%T(_SwOE4|)0%JN>Xa;h|B#d!rUa0vwXEtyzM!%p4t1g~E3U(`~Pj*QKwyafO1j@xZd
!csmcWqwBC^HhAlKb>^$yWGb;_ffg2h{^~2yTHFI{KLTUSB?)CG`LFlhrtQy7h0q4ZMR)yvfPW7Nv1N?TmIk08a0@n><;rYGM5<b
WH#ocT4P{Z45!s~#;3&-Ig^X@goU`kU%$=I-*OtQ$rM^>NaXV*nkCvO>(4Ot+9V%s>e}0AmI6_RRA-SbHd;0Zz#^SRBN`*|RyTm{
YNF8!e7a7Nl0^McDme4kXk%5#?S~AeN>EOS^emZ-
d8MDw<@ik#;E*G{%?C5o4rUlAtpjK(HGiQBC_8_lfQXRAWHQ<U#glQLhRX{G5@s4Lh8R)-@fNqLW*E)OHS=NQ_yOcc-qNm`n2w?a
G59u*=5zD~$x71x@~+q8=(?z`%O#1PTD#B<2%h9?MJ^)1;_H#<Z==-3aym-&b#24qvKE^n(I6m0wwW*c$J&@bYcpPs^jJg(ZQ|-
$wxJf00!=21J@oVCSl8Fp<JiRu-
75Ns;c(`AP4$TK)PBc7YK%X)vb#cEQG!j$EY%8iMJcpwVRZ{?Ql>`4Tcnac*%_4=T$zkkDJq7Xi9HXgp$yhk>ht`-
iSBWNp*!+=*vY!o=spa;Nb4S<WKV_VLIP5O!-
WSI*7W50;fjM>5IJ0qMvl(gPIIPny1xdXYKpXm2s{|QzU7=z)#HL=hN*A4$K?eKFCB%QZhM%?MFpa4N|d2zHgMmD&_s<=4><W>Lx
<&;J049sCgz5IFl|$gLq?PObTZZ1z~NdM|EW>NJWEO3F`}s&WT_9h)4e{18TUay+dhWbt`A(7`%p{(NvD9Xp&9+E^|(CNSKJ?Y@_
Ck%;fhmzC0^`gc`*ab5fJiETd3~@c5j>##<iT{d%-
%gs>8C3=eqIZ2o9aaN084nwzxVaBoak;H;&b9K8|Mh^RT0n9*ONAIO=kNT`I6k5O%qVVuSQRqbP@~1m8-
s#)2f0a9i4rM$=&wMrOY~jKhdm2!{z@P#lU`B<X}$7So$0a~eX~nCiO)H`ysDa}DJ>rA~Ha1?iC0-
6;%^bw#PpKBy}))hYV|C@|?QOHMQz>0||R7MLM7%f*nTTGDXJwAabHvfQYlNJZltqdkb?biPxHJp@cYhzL8GBucPkr}=UW54T7a4
qiD@goNRcmxz+tWE$q_dZ8ChSNlzKZniSo(K_9AP&O7US$_)&6QdkY!|&2Gaks>*FWsGuAw0%uw#U669Gh>#&Uo6Hc6Yid4bXUMF
k<DqX!7C>6w_t)@?zu$1ELGyDkg$PD$Oo=AW2HR!Mt_F_QvXV4Y61499A15H)y48Q&)yUYWkNDB^g9`tyA^`0*p2WfJR?VyEXire
(B0ND=dQYVH-
A=rJ)en3}|2sR3L8vlqM8MDlt$jRd@OTY!!o!p4DvQAKVJ2+$gPeGL~Zt%>%>u!8Rq2!|!Qwx|Ny1{=`c%h?7KNni%zL4puR_hMX
e`d=!~Kc7q~$r;b(_kF$$a(O(@gC!$^bkOfjaO}b=ch~&3?01g0;vm{gufPY^V0>y}B>ysU#qyDT+om2wgG=4dzj>?_E=A?JbifE
dyrIGj$lJRQ)9!mRWRNZ2om8jkF{pdozEs9YYrd=%RlSl0kekFBOO>$Sh{c><ygA8|N^OX!7Sj5+Y>D<}wsajMwP67$7Sg`svv}6
Hg`4|itp5FxpU8@sM?D#w_qKLu;8%JUaxty+C#0T;FE&mO7+#^1>Ro6PIFr}qRawy96--SeieL^rK{-
aSiipKpU(x#_TO;60os7?V}(_?u_Aq4pZTspjQl<yi0V+lJ<7!b7=;fE@4>UT!_3YU3KS5L1^ynMMs2H2^=`5hr(8_nic+HGkDrp
As{JgV+a=(ajeBMrmvXiQPtRy%b|*upV>9BW}e-NH2v)J{@|>D`ecRbn5E<~A!-
S84KHy47X$=kA&3j&s^QP+3Wv$;A1)Dzb$yUlzRhi66??M=JEEPS^OAMDp)+Fe_QcGX48D(W1d1gBu+zbCpF=;-
t};3Rbj*V8NVCzN9f7Yue?B^SaXFL8gBZ<a5Np76V7>9kmVR5MZVk$R<au*o89R|6FTXX`j~D`-9t^zOK-
&Gu@j=B5hyEB<RvY7c~2THdiD#d(9+qj?rzeB%t$GfQ%JcFe0e_Twhw0!>laQp(XvLYY3-
W7mk2*VDHH^QP%ELx$~%;+b|nzA$3t@5sNINO22)}sL}7StjrRqHHuZoBFQ04xJLxF(?N<K+w1kNfYiIa*^~=d&(-
=%2Q!}u(i20xd@0szDR!hgj_?ebDs488aw10r%&hGeIUx$lhzzk`0wi6v*2Tb$J>U~IQ7|39lR5gGa>{*}&87@v6O6_3@^|fwmrp
2y9YgRhmhmV{(g^m2PbP}(0t$!G6==sdI*E`kW|J%t+H|;?XEAD7t4Sd~g&pz~Q*mb;SP1HGIvEk)q!HGKrgW2c90EOdliXsKjiE
Z<f3$gB3%}DSzE2mWKs6IzwuVLOo*2UZ#~oD22y`B@L;ge&4N><AIw|N59m|R@MMXvxUy2H*w=<BH@@9yvOqK2d4a-1-0%+J(-
m7FA*MC#ilU=9^C*?Sq<S-!>YpaqkBI6Rf%N*!naD4Bm`=J={y~{&Y%-
L>LLO#DBGeRTKD)Z>&u^4+7+OX{;G9P}CRKmF38{$ElK_aP0`3Ud}JS~gneDMTU6?pyxD-Gi~&M55c`42G|2$^xIaTaGPFtlH+k~
id@k#(|VUC!n2Jfiql_k;)iJ6MU80v8^piM!O0&22^r60=FLZ<tF9FJu_ae|bIk_waX7C`ov?UEZbTURu_r<z1RA!j!IiFT>8xp_
TOIV41hD7Clv5-
1GWxZ;_2a4qY;8sc8IH%t@0My*aNohVw;Hu*_A_atDJrjbI}2EsgHwQOMBZ@%0M5Q@_PJ8n0`fvMo7}VDGNUu}1T|UMom4^TTgZ&
y9b3_eU1@Ud@~Dzq~yc+Phb0yncu#zSS5EntiY7rh|s-MoBzKt%2vKb`Uk4e$sGU#|s*bcwjkJYz-
`{pAK3{6OjF+)o9gAX}n7R1L63*E+A}LotBplUy}68lSN`O4hxVS1Yec@IxYclT*3<jwp<vni-
m#W=+I;x7Keg{u`;#o$tEn$1`QKccw3mZu%qkd!Folpj3EPmv$V1y|I)mo)l%&058JHvi)9Ns0Hu)0DqFQck!_Clie-
z*T1++v;Oc~m;Blzp?tWNSfZ(^fI?<Q4m0`x!rMi-F^s=at;n-x9gyjVqT}>u(UD^skb*J)srAzT!n-
qr&W|gksi?5Y#dq}geql3#oRJtKeZ{XR!6*O9wYgx9_v^`rMOl^2R9bU9Ni%zaKab<~?WjE*<F}L9Zj?QS>78>HWh09ih9(JP>nk
_r9jf4I!RDaD@!{bw>f!p+4&ktP74FanbSacwf&LP{5hYJe;!VRo|&cIXeJ{?GHI3Atvr1O#u2mM%q>jQ-ypwc?*@=A3{1F;+c^K
nFvPSE0~<=DR8Xg2JI??Fp!IxTH`j_Wyg!)@7~>tJM_>o<G{I^bHq<=BDa`gD%cr6ZwEE1(0kP(7bcX4@?~IO|!CL(hi=jerhw1}
;c%f+J4AyQ-Jx;eBms+U?8d;i$GUZHkZMFfn6Fr);BoPrrSmx@;#&7@G+tTqqvVFN#-
yzdjG)wE8ut8Z*2tua>pM9GZOj$wc1u+0-
3qmFZO}W73BVMcdaz$My39N5aT$d9|v=j02aSP2_B!7)M;jk!*3qL)bOYvZ`L5n@gk0JXiZsv@%!IM^tlvSmSnUNi55DW|>=<`ec
J9waI#m@4%unSkX7eu&iD_H&=%}P;z=tHKW5C2Yn|;`nIU=HJa2Wn=QV_eV6?wrXiFp-
~}*nRNg+9x97iFs+^TLozAz$l&omGpDti5YnSI$RFTb7VIo;Q-
K1K93TdP`X5Q{H=Y|*#i_{LGA>HidcWMDe1+SwKZ>AN#SxeXS@P>A-
&6l$kJ&i*feA^&3UM|`)cp&g4J@zB_`R5w4zafPzw7a(R!_27yc}4Dj(gN(?Lb<5mbWat-
C=NUvnOwam#mMqis0{9|R+?;XQZ6u;RS9Fu$Z>&CYED~cX#)1`R!(w+s#U^VTK&u(Z^i5{Qf-+_oMl!h-
tgK+`YjIQ8hWoLvAmbIxkQ3A&;&^~dOu-5;Felz1nfa+>qs+>o%Y-
8ifsSD_{rdlEFeP`w>zj8IsyyC0haL#H@K;Ee_>F%fM54LVIxXlA-YcE3FzChLO>XD3^p2N4@mgOlQAN>xz^vXFoEH;L|ZHyjH4-
QLXxUSpYlb$B=8?Xn%^pS4X4yD%75o|D4u(@-8P|P1>Xci!r{qTLJ3V0%`!8)XnqlHJ5V-
si&!mQ?G^17v9?9Ln3d8Nc@L^3se}oni9JLHGrO&UZ0sZ6vAke!7;e$hQrDKy?bU^hy=m(>{9d8s2bI&x&Br&rv#ax0Z?1d4zj=L
i)4P6ib9VFk%~kL0{O0}HW$*mW)y?&r%iagOA}UkfYDcr5#hDcjW)y5s#++#KpGKStEySvFia(-)fmcrPM^wO_Y&6L$r=-
A@^IkFH%BfBzJl#^g4Q|$pxnV3ZD#_|e$?8F}DyKB_qOx0al21(XgNAcpy*?M$&kc1@qQ^#`&GZ47wB$lsa6_?0(boG=Io-
~Y*cJc2EB?Jye6cIOkch@<l%soaR-U*3@yO+9#cZ0+T$k(@EnAQI2}n|<w$`64hP062d4WcGhSi4jWYDe|nc}%Tcmdy3uh8P-
EczDebjF~bEXUKiPWy*ad<;Q*6}|g(Gv}ua#5~1p)6*14_#q|&L>We{a(kOsj5^v)61lfRM;r9Y&kmAMe`xb<hOzYen?*|ddfyDW
AdxTh%Ec!LW{<@7)$6O57m(LCC80fkb@uwI_xkz8)y?ah*B9@4Z_nPntCX56sebYL>h;Y<@9p)Qw-
?v03n_nd{rvUS+0Dfc*XyhE>x;8@7msk<T))3Si}zPI?|N@8pZBgVK2}6a*uH3r%DbEE*C6oS`&Sjg8Ly~(yg2)3MOY;aXwie7ux
{^43D?c_+4)69@N*w}VL~Bk)MBr$P<x|<;QHe2o9mkjC*8y~ArFl3b$ytwlZ+mr)XPndEB)E~=dW*g+`TKX_noXgyZ+pRojB{+w$
(ekxdE#$t}8z|&m?oyV~2-
I&(u6VI~0xX(*7)BOZ>Eby7+W{`TiYU!K?J%e7Lyo!L`6nJvuqmrYC;iZZ!FTO<lX1z_`;ByFwlGL0~iIb3f8%mCgwL-
+tz&0NSXBg5Lf6$AB2_UA<S-@mxxlRc`aW$Ad&F)?y<b#8)vB3-
PCT8@{W9hCaruSNdA4CE8M3Y4_SlOSQGO(H^v~+Duz$e`;?@U{pp=86@TPLz&eNYe{=PM<j&QeiV&WQlny86jamOoOX_E<$Kr4;c
m>R`f!`)Arh1|?Fwyf^UDk*{Shr@*;?;(Y*1{`Q%ceo$V>7F!scg|6wlt(5z)Yk>6clZHs1^mEWslLlaw%DX4M^1<^VO0QwrXyIu
oTx0<|^d+_Y8`gODT}4D>h^X}Pa-Jq644BsTRUshT0X#ds+k+(P5NPFuD5_ceJz1PWrq7j{=X@P*U;A?6vvoCN~*$x>Qq<4DI6wW
*icnQr;1`u{r}cHm%LCIE=h;Nv(V<8b3hTvmVFmHtp$R@cVAMY*XOOL~rAUR5{$K4v7EG{+<h82Hnj&|(g;=s)Rdi{i;%)&w*%{*
wVo6ei?xL{f+@pB@+K)DY?h3H({=uM~jRrpkIgS!<I`#W*?;q`hloz5mHT7zO3-
G(WiD^u07mf9F?1NFh{NDm|1pfbpdT?{a3KNwt=5XqW*VB$X1*PoKo+&*dR~`lNmSOhYQi<}o_`^r?u)=??$@{Q2>?m7b$56kU!R
W(R}WF`6*(I?CtmD9*P*CPKCh2_xsnoLW&Z$6KZ{7dq7(kB%<%&VD=BURF04!OOFd_O9D6f8*b3zy0z&9IAuMk12e4R(tsyruXIf
(RCb25-
kOBfteW9KWm`&ZS65I;GRo37%u}Lu)BZO9xv?N=Kl;)P}LV?9Z_GK&t>g=e#G)3w60x0huHm7ad0MdQ1B<Ae`}oRUUgw?StrAVc#
_kMA{I6mDWcwCn#?AA#z5;Yk<0R4bQ;CO;^6UMvYctFjNdO}^5Kp+n)5E2d_IA5zs?JOMw-O2TO7<Ds7F2zs<el3Xg<&a1-
0en6s!F(4XwSR2Y$A7xd>qaY7eGOm4r~iN7Kn%w%8Wh=Gxqt+-
@<2*LxV((4G%G4(GfEKA)4i;x7hkR8g<@w|5G32GE>Js*9<tHmcN@Y=}nF(k|J~G7RS?S{96cC*ReQ!q$(FUMMZ&SEPKKl(y!#r?
=(%QDkJV6?-{qI*8H3p%{-
vo{Jd*h=q7~C~M(xsEx;3jtm5SEVPG*iYQ(fA<e^WegpVxnXZhss|xKTg&7HNOy@SgUy#(z%o|ABur?mo@*KVy;-
_v%NN2{$0z5hkQJClL->i`9-72cb2(BQ1;Z`v37g8QUt$t=wTm7aw9vg+2&cvDd@IZcc1nUybLftcO4DOw}cB=&aSl-dt)MX2h^z
dL3SoJsS<e~7u-^#4{_Lvoi7zs=5TlE_-0OL1ObX<Kis#S-
Osu_KmPSiVaD32r^ilbGw*a&Tid@ZGdRl26*^iY~Dee<ug1q~Yn(vkYPE#{6$@RQ7)GMRH*n>!jR@XvWn@_=9o)!eSm9TW@^fW!2
aLN<l8Yt(6l=3QMu=mVj1ukdO|fXnQFSDB8o!A4h2Yx*4aXl|S66u`_6FiX);t(FAJ6;5GfDEQ==q=zwe%%X{^_N(ybM0Ziz9$Mk
66Q~l!iQCR~3Nl}bp+(!CCA_vnZzXUH@kn^>y)xT!kT_aCjYqDN<@3dC$*Iw3x9F<OS${$?*;d=~lwSWsk4LCCEYTtxue8+(+v`0
23NXw^D*a*9%V-r<)1i_gUmCxJ{a&V$q~a}1W=z&}I$M&J)h2PgoRJonw$yB430g$Om}$>S-o2~8rqf{QOm}!I3s3|Iuvc<5ME-
{gVwk<(L~gGE5850n2d2aF?rpx^Emo(6e|}gvD2@n^qeV&ho<1gQw8@?xgFJR<Se^F=a+yw?lB>${B^~;oszZ-di5OZps$_3vqv9
Y}M92NB(<6s|T!ZGRFW*BD30xf<InMZasycNHqt1t@!teUf+7mu6U^%0Cm&?;jc5p|5x<7W9{wGkCXIF|2qZl)WJ*j^z;7|l)wd$
<tw$m|nQJiEfCNeDgWS3H$m&oJ+QY6N6@<@B`z-hIF7r-CL7ebV(eCQtnGHz1U9dkH5VnF3fC)ldPO+lb*W#o)O+J@QWn>-
D}`xfls=*h+1*={D1#A~<`<CVx)p?uF*t}N<m=U!xi3YLe%Q))3jrAGN_zWTvSHnS)xwa}HPFn-
=>LGR64gino5u5aH((;b8zRH>)JEv-z6f(&MP<6*B-
?Mnd<Z%h$qwy*7|cI3kjyJNk~g)W_aDEct?hPstks!P5GQhqW}9t9|Q87`n`9R@84ZJXXnRh0|wRmXG!+jZq_&Gwqj$I-
CkI%q(4-
InY0MwKH7wP>$DB{&k+Fsa+)iIwNKnwC{10F&j>QiMsWh?OS2YPDh8dkDO$8U+!oMo@LaP{ICM?y96rTq#tikbH|APZ`4XoQ9Be$
m1Br?immFCy;w+8uYT%hI<UrO&Lkx3)k6i>I&~^czTsl;2n}|i>7SyuWwmAxg^MY2bClxfkb$d(dzv7id+i=MzsPaD!h({0=4Y*L
sWPby|)<7()p0L9!Mf@*n3r8_2T71mcXA?iZHhqN7Ej^;aJvDXdo)X-Y6X?XmXN-KpO1IX{Yl@MIuY;N8eILl8;lCj_5H0b&!eFt
vBqAd-
<{_6$<?)SqxF^vA*wKxOPXo8wAho)s{yQ*GuZ;iyuT~K*tYznY8gel4TlHEP+_|83$!kXXia++RJ(GH>Yx1$YVu4`dPekl)J95gq
>_f2uxSi+${i<l<k2GMiH{!-WXOP;|V+Q_S(+BWs7*YtB3TQG#P>@lrMln@e8>{Qmik7d)XjMlXek0-
N~SM!?sLDz~(mRK`u@QtSDjvUpC+bZ<8GEl1OR&H#bO*?vIq$%AedG+27uH_xg{wmlwVB(!&0W7q71_dcU8YzxnO;8Sby1_paXma
dCZi13fBsI24wTuijAW-JZzJHQKyH+4Ti_AbjuM|8dw#^?h@3bA9&e;`ue8-
jaTPeEsgCcX4^y!}Z0>YubHz^ZvSbe)g`kKcjHGd;O^gwY|Cc)O+#%l6N0J;Q9i8FW<aH|8gS&6##nu;`KREcYx#Vn|H5oUVpftO
&&o0`Tp!VH9POUJbPOah1uPLKQbq!-
45Py>0RFJ+moO4{a@IDc_vD)S$=l<tkd0=Jn_CS!HfTkY@DjCg54{^irs?kqu&tB{EnVRmpdGYKL^or1gXmJbb3!3+f{l4<}QLMA
CzY6&hHKj(W0(2S+853sJEI%n~weMSIEcGJzsE;fV>2W(>?^MTP+HpCr6v2jvR4P<+f%_H+(4%&xUAsLZ{*ShJ-NMt8&>M^nElHw
1a^0!z1hE?o8U0a~NuS3|!Ct0VgXr=#aU0N}C-LQTO<3%IE~F-
Zv9^9}68#L}Jo6V|54fNRQ_mwS&Q8sIEMD9Bp51HW@QL;qf=Q6>mJCO<I2R5R)~LM=BhCgISjAxTk0LyZk`gF3SMEQ0^BltCRi1O
sl;DTfKXMMWP@}p3ntHh?*OPXri_xi_@?>B=yCFU(;ZS;>~^ZmZ{wf>9*t9316M;qz*e-9Q9wHt~-
^Yd8I4VlX=C;!Pd~~3W0!W&h^SplVDrFRg9fR7O$06Iw@PhyA>X>BKY}*a;LwRPKg%{jJCw5?mMS$x1__)e}l?8KUZ1zUs2g(`d}
lKc9cf^h1wo%PH(|A{<~DS@&8r#|4G$#{*UPH)34u`Un8NnUTeob`=A~B?t}Kkhaa@ZUw+VzfBHc?^6dwq?Ox!m9sgX3cJzBC+OZ
FoXve--qCNG=679%0OSGpxTB05MYKiv5XG^prA0p9?eYiyXF26#e9h(LDX^`WSp*{}s<fO>2eH@z`^>q{N$mdNo^?eiV$Old|`C$
?5$d^Sl`7ILd@yAFs^<9>u{7_$JIl>pJQ=e1Oj(tx>+kQ|*d;CR}A1qVyHS^jN-
_+5HkLqau@{8tw{6wXG<{gz|<d@^ti`VcJ&XG1$Q#zBA!Mdia$!JN)Y5&K!PaI#paD~)Ee^BqbrIkpr5bI2kFMBATG8xNLCi$}cH
N2_PI@~7@wd+joPPRYO9q;<`?VsVI`pIj*#m{H2Jqu|g@{>n9k)J*J4y<CUbZq9!C-
+Ln#o2he$(QE%$=%X?$sRDgK0lEg@&NtQXph3{=c<6ZdCN~wPebWE@2jH|{k}Fbinq1V>wAAyr@Hx30Qq5rurtQMh1?OV(KUvE+p
qXbEa5HVF)qh^1yI{uXS^^^qvHy@anclg_ObNpkaQ|!5B%y9y&qx<LYjn-
<{?~&yLI@<Loaum@H71uPhx?2j0>X^B+MZwr=O8}!fDd~q9&EP5WTRN=Uv}sI<48M&yS+g*e$W9wY8lKxFdfR9+x5=9f*$ZxhH`o
l;K4fU}KD4>%_KPgC6AEUeW^FNyAVNck<t^pf^N?^rC4&-
xz>$gf>0X0&g1fTZF}QGMz)7Lx(QmVuyu0oT%Z<>g%n;!?l=*Ssl8Gzv^QT1j~-{WSlQf=#^C`i*J)&l*hx#thaJ|-
zKyBlc!yobgFX6puAA=y|S*HqQ{-<=Y^7a<#Zw{pnxigkO~ZeT=UtH^rKk2*w^_--
+U>%(Ia1v(2jgQLOb^T2<^xRB=#NSkxyG_kH2l99r?IL$rc{@=7v`O=*GWo3=ck0^TgY{{}Vg-ca80w(8d~n?V_~pE@*=Vbn+vl+
SPV@aEO@6e7W15N6rytIqmE1jH-
M$#!wm6a80T=nuKK=LPf)j%_?lmqB=$a9r<7zT16Ef`WP40MZ=vE|5E^^0N`!TTbZ<>2$dtPbpBc&yIW%cu}4h!h~)Mbe^`u({6v
&+4gfWVQ8R~Rm8(uo7D*$$y+v~q&8ehhdj83l2Y7yNVI);Tj%;f$+?~C!j@k=5IItHx3$e2sM@$7t!dp7PIj4`$kT_}_`_sPd?n^
UmEuR#xypy8L2VyBp**%U^I&rE@(9b{bL~rcBeRj;!NE5JUYj(O@8cv~!a#&@}dt`oYpWV{YTxo!geAsBGV&${3lpW5*wfN)kyy{
H5*8Zp%@}>Cg=kx+>n~pVIo17L_XSew}jH+>UR=uW^0MF^L2|-<(GvnlWdp--D>bjO7aa*Y?s_R#0{DSP1%Bm{U+}0Jfd8le=FN(
qDGlDunAaY%0EY(>}p{t?}qy82z={4P;;15v1XBhz9FUTd3RcW(uWl{s9ou<386!>Imp6^O?b4$z&n)`<#VdQ$lc#@=oUkA%Ow$P
20NJY-txWXl_bA!)B$)h-1tPZ_;#k?}w8qd(KLY<joaB+=PjZC7T_u&IXovqfnP3h1&kx>y$Ol4IOTVx+-
7p8Q7u}%Fd+yOejqw2Sl(MI3Hk4l41CvFAAsPmgDAW(O+G=;#@_7SKclRuaFsKP_^mYWfPE*~M2e)~W=|B=wgy(<5Z<nLTFiMSkS
@y!ANgrRk+M)3UN`t^s3D0uPg$N%_Wm0`BL
"""
raw=zlib.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==29517 and sha256(raw).hexdigest()=='3b6603447f55112d8088bfa5d40d2438ada02d7f73f8cd10859c076a9f2bc1cd'
files=json.loads(raw)
PINS={'joint_rotation_certificate.py': [6261, '4c894c4e7456857421885bca0e82f3afeef521f67509456f836d6895f9de37df'], 'joint_rotation_actual_audit.py': [9064, 'a4bed339621d4335af617146478137897bc5dadbcb585ccb79c229ab69368055'], 'geom_float.py': [3630, '16125d6b2648234d8598272b37edf50a2c13c4861825fd8f03c8d6084dfa5c77'], 'probe.py': [911, '7f0ecca5b6013f468456bede5f46b279f5ccef652a9a3e440a261f1b4a672d88'], 'probe2.py': [920, '4694e7251a2cf79e57138aa0dd8ef48c124dc198636d6d888ed0d9dca2b7904b'], 'rotation_scalar_probe.py': [806, '2d018fbf62ac0a380340159b6321f37e095521279b61ee6caeb9946339181b39'], 'rotation_defect_probe.py': [962, 'b3934186a566e15d1572c42eb957e83f0dddc6b02034cb25ad992aa76d672dd9'], 'symmetric_derive.py': [721, '027f41962ceccb5d5da2b34772c5749ae096d19a053f7896e46a45104ee6c1fa'], 'exploration_receipt.json': [4184, '4b5764a4a3c76a3bfc6f20aa294aadfc17f5e713cfb85ffa246c5bbb4d778b19'], 'rotation_scalar_probe.json': [238, 'c4f1bdeff53dcbbcddaceee92dcbe5c8905f013a4d3f1ee7ea4f49455539ae7d'], 'rotation_defect_probe.json': [784, '66bb5dc9307863eabb3d5eea322f5978133ce07be9a9d4a37ee988e7a01fb8b5'], 'probe.json': [2, '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945'], 'joint_rotation_certificate.json': [1325, '3a801dc749713efa7041a4ca23765f2a7a276fc6a567cdc3b37631d7ad7d73f1'], 'joint_rotation_actual_audit.json': [64918, '175fd7b67b4259ddf96c9353b50b79df608945eab007bee6f3801327ae5628fe'], 'joint_rotation_certificate_stdout.txt': [401, '5ed75cc52b5bcc6449c2c1ec228e25f3ce493f8fe4c2cf7a03d9c20fc9747e11'], 'joint_rotation_actual_audit_stdout.txt': [392, '73a65f8d9ad82c120122bdc606a969212c67533bb6112b049123d02692dff201']}
out=Path(sys.argv[1] if len(sys.argv)==2 else 'two_anchor_v3_recovered').resolve()
out.mkdir(parents=True,exist_ok=True)
for name,text in files.items():
 assert Path(name).name==name
 (out/name).write_bytes(text.encode('utf-8'))
for name,log in [('joint_rotation_certificate.py','joint_rotation_certificate_stdout.txt'),('joint_rotation_actual_audit.py','joint_rotation_actual_audit_stdout.txt')]:
 cmd=[sys.executable]+(['-S'] if name=='joint_rotation_actual_audit.py' else [])+[name]
 p=subprocess.run(cmd,cwd=out,capture_output=True,check=True)
 assert not p.stderr
 (out/log).write_bytes(p.stdout)
for name,(length,digest) in PINS.items():
 b=(out/name).read_bytes()
 assert len(b)==length and sha256(b).hexdigest()==digest,name
 print('EXACT_FILE_PASS',name,length,digest)
print('TWO_ANCHOR_V3_JOINT_ROTATION_SOURCE_ONLY_COLD_RECOVERY_ALL_HASHES_PASS')
```

## 11. Continuation after this closure

The actual positive-endpoint, unbalanced two-anchor **full joint maximum** with G(C),G(D)>=0 is no longer a surviving high-trace direction. The two root-tilt equations were the missing connection: after exact frame restoration they constrain the genuine special-facet slopes and force a defect too small for the inherited actual mass/value budget.

The natural next use is the same exact frame-reaction formula in proper simple-C/D geometries outside this sign sector. The rotation identities themselves still make sense there, but the endpoint bound r+qm<=s0+nu and the six-vertex cover do not. Zero endpoints require one-sided root/mark variations rather than the two-sided Jx=Jy=0 equations. No extension into either boundary is claimed here.

The independent global localization/attainment theorem is not reproved or replaced. Thus a proof about all nonstationary bodies, all negative-anchor polygon fans, or the whole mechanical E17 layer remains a separate obligation. The present output is an analytic whole-sector stationary/value theorem, with complete exact finite certificates and an actual uniform-body audit.

Supplementary convenience archive: [complete sources, exact reports and discovery records](sandbox:/mnt/data/two_anchor_v3_recovery.zip). The literal capsule above is sufficient without it.
